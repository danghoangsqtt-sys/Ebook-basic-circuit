/* Local JSON backup and restore. No upload or remote dependency. */
(function () {
  'use strict';

  const root = new URL('../../', document.currentScript.src);
  const STORAGE = { highlights: 'ebook-highlights-v1', progress: 'lessonProgress', font: 'ebook-fontsize-px', theme: 'ebook-theme', weeks: 'weekStates' };
  const maxFileBytes = 5 * 1024 * 1024;
  const dayPattern = /^day(0[1-9]|[1-4][0-9]|5[0-6])$/;
  const exportButton = document.querySelector('#export-button');
  const exportStatus = document.querySelector('#export-status');
  const fileInput = document.querySelector('#import-file');
  const importStatus = document.querySelector('#import-status');
  const previewPanel = document.querySelector('#import-preview');
  const previewSummary = document.querySelector('#preview-summary');
  const previewDetails = document.querySelector('#preview-details');
  const importButton = document.querySelector('#import-button');
  let pending = null;
  let previewFingerprint = null;

  function plain(value) { return value !== null && typeof value === 'object' && !Array.isArray(value); }
  function keysAre(value, allowed, required = []) {
    return plain(value) && Object.keys(value).every(key => allowed.includes(key))
      && required.every(key => Object.hasOwn(value, key));
  }
  function validDate(value) {
    return typeof value === 'string'
      && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/.test(value)
      && !Number.isNaN(Date.parse(value));
  }

  function validHighlight(record) {
    return keysAre(record, ['version', 'id', 'lessonId', 'quote', 'anchor', 'createdAt'],
      ['version', 'id', 'lessonId', 'quote', 'anchor', 'createdAt'])
      && record.version === 1 && typeof record.id === 'string' && record.id.length > 0 && record.id.length <= 128
      && dayPattern.test(record.lessonId)
      && typeof record.quote === 'string' && record.quote.length > 0 && record.quote.length <= 1000
      && keysAre(record.anchor, ['prefix', 'suffix', 'occurrence', 'sectionId'], ['prefix', 'suffix', 'occurrence'])
      && typeof record.anchor.prefix === 'string' && record.anchor.prefix.length <= 120
      && typeof record.anchor.suffix === 'string' && record.anchor.suffix.length <= 120
      && Number.isInteger(record.anchor.occurrence) && record.anchor.occurrence >= 0 && record.anchor.occurrence <= 1000000
      && (record.anchor.sectionId === undefined || (typeof record.anchor.sectionId === 'string' && record.anchor.sectionId.length <= 256))
      && validDate(record.createdAt);
  }

  function validDayMap(value) {
    return plain(value) && Object.entries(value).every(([day, done]) => dayPattern.test(day) && typeof done === 'boolean');
  }
  function validChecklists(value) {
    return plain(value) && Object.entries(value).every(([day, checks]) => dayPattern.test(day)
      && plain(checks) && Object.entries(checks).every(([index, done]) => /^(0|[1-9][0-9]?)$/.test(index) && typeof done === 'boolean'));
  }
  function validWeeks(value) {
    return plain(value) && Object.entries(value).every(([week, expanded]) => /^week[1-8]$/.test(week) && typeof expanded === 'boolean');
  }
  function validate(bundle) {
    if (!keysAre(bundle, ['format', 'version', 'exportedAt', 'data'], ['format', 'version', 'exportedAt', 'data'])
      || bundle.format !== 'electric-basic-reader-data' || bundle.version !== 1 || !validDate(bundle.exportedAt)) {
      throw new Error('Tệp không đúng định dạng hoặc phiên bản 1 của giáo trình.');
    }
    const data = bundle.data;
    if (!keysAre(data, ['highlights', 'progress', 'checklists', 'settings'],
      ['highlights', 'progress', 'checklists', 'settings'])
      || !Array.isArray(data.highlights) || data.highlights.length > 2000
      || data.highlights.some(record => !validHighlight(record))
      || new Set(data.highlights.map(record => record.id)).size !== data.highlights.length
      || !validDayMap(data.progress) || !validChecklists(data.checklists)
      || !keysAre(data.settings, ['fontSizePx', 'theme', 'weekStates'], ['fontSizePx', 'theme', 'weekStates'])
      || !Number.isInteger(data.settings.fontSizePx) || data.settings.fontSizePx < 16 || data.settings.fontSizePx > 24
      || !['dark', 'light'].includes(data.settings.theme) || !validWeeks(data.settings.weekStates)) {
      throw new Error('Tệp có dữ liệu thiếu, trùng hoặc sai kiểu/giới hạn. Dữ liệu hiện có chưa thay đổi.');
    }
    return data;
  }

  function parseStored(key, fallback) {
    const raw = localStorage.getItem(key);
    return raw === null ? fallback : JSON.parse(raw);
  }
  function checklistKey(day) {
    const number = Number(day.slice(3));
    return `checklist_${new URL(`week${Math.ceil(number / 7)}/${day}.html`, root).pathname}`;
  }
  function currentChecklistKeys() {
    const found = new Map();
    for (let index = 0; index < localStorage.length; index += 1) {
      const key = localStorage.key(index);
      if (!key || !key.startsWith('checklist_')) continue;
      const path = key.slice('checklist_'.length);
      if (!path.startsWith(root.pathname)) continue;
      const match = path.match(/\/week[1-8]\/(day\d\d)\.html$/);
      if (match && dayPattern.test(match[1]) && key === checklistKey(match[1])) found.set(match[1], key);
    }
    return found;
  }

  function readCurrent() {
    const checklists = {};
    for (const [day, key] of currentChecklistKeys()) checklists[day] = parseStored(key, {});
    const font = localStorage.getItem(STORAGE.font);
    const legacy = localStorage.getItem('ebook-fontsize');
    const oldSizes = [13, 15, 16, 18, 20];
    const legacyIndex = legacy === null ? -1 : Number(legacy);
    const legacySize = Number.isInteger(legacyIndex) && legacyIndex >= 0 && legacyIndex < oldSizes.length
      ? Math.max(16, oldSizes[legacyIndex]) : 16;
    const bundle = {
      format: 'electric-basic-reader-data', version: 1, exportedAt: new Date().toISOString(),
      data: {
        highlights: parseStored(STORAGE.highlights, []),
        progress: parseStored(STORAGE.progress, {}),
        checklists,
        settings: {
          fontSizePx: font === null ? legacySize : Number(font),
          theme: localStorage.getItem(STORAGE.theme) || 'dark',
          weekStates: parseStored(STORAGE.weeks, {})
        }
      }
    };
    validate(bundle);
    return bundle.data;
  }

  function fingerprint(data) { return JSON.stringify(data); }
  function conflictCount(incoming, current) {
    const byId = new Map(current.highlights.map(record => [record.id, record]));
    return incoming.highlights.filter(record => byId.has(record.id)
      && JSON.stringify(byId.get(record.id)) !== JSON.stringify(record)).length;
  }

  function showPreview() {
    const current = readCurrent();
    previewFingerprint = fingerprint(current);
    const incoming = pending.data;
    const conflicts = conflictCount(incoming, current);
    const existingIds = new Set(current.highlights.map(record => record.id));
    const additions = incoming.highlights.filter(record => !existingIds.has(record.id)).length;
    previewSummary.textContent = `${incoming.highlights.length} dấu trong tệp, ${current.highlights.length} dấu đang có; ${additions} dấu mới, ${conflicts} xung đột cùng ID.`;
    const details = [
      `${Object.keys(incoming.progress).length} bài có tiến độ; ${Object.keys(incoming.checklists).length} bài có checklist.`,
      `Cỡ chữ ${incoming.settings.fontSizePx} px; giao diện ${incoming.settings.theme === 'light' ? 'sáng' : 'tối'}.`,
      `Tệp được tạo: ${new Date(pending.exportedAt).toLocaleString('vi-VN')}.`,
      'Gộp giữ bản ghi hiện có khi cùng ID khác nội dung; thay thế dùng toàn bộ dữ liệu trong tệp.'
    ];
    previewDetails.replaceChildren(...details.map(message => {
      const item = document.createElement('li'); item.textContent = message; return item;
    }));
    previewPanel.hidden = false;
  }

  function mergeData(incoming, current) {
    const ids = new Set(current.highlights.map(record => record.id));
    const highlights = [...current.highlights, ...incoming.highlights.filter(record => !ids.has(record.id))];
    const progress = { ...current.progress };
    for (const [day, done] of Object.entries(incoming.progress)) progress[day] = Boolean(progress[day] || done);
    const checklists = { ...current.checklists };
    for (const [day, checks] of Object.entries(incoming.checklists)) {
      const merged = { ...(checklists[day] || {}) };
      for (const [index, done] of Object.entries(checks)) merged[index] = Boolean(merged[index] || done);
      checklists[day] = merged;
    }
    return { highlights, progress, checklists, settings: incoming.settings };
  }

  function writeData(data) {
    const checklistKeys = [...currentChecklistKeys().values()];
    const values = new Map([
      [STORAGE.highlights, JSON.stringify(data.highlights)],
      [STORAGE.progress, JSON.stringify(data.progress)],
      [STORAGE.font, String(data.settings.fontSizePx)],
      [STORAGE.theme, data.settings.theme],
      [STORAGE.weeks, JSON.stringify(data.settings.weekStates)]
    ]);
    for (const [day, checks] of Object.entries(data.checklists)) values.set(checklistKey(day), JSON.stringify(checks));
    const touched = new Set([...checklistKeys, ...values.keys()]);
    const oldValues = new Map([...touched].map(key => [key, localStorage.getItem(key)]));
    try {
      for (const key of checklistKeys) if (!values.has(key)) localStorage.removeItem(key);
      for (const [key, value] of values) localStorage.setItem(key, value);
    } catch (error) {
      let rollbackFailed = false;
      for (const [key, value] of oldValues) {
        try { if (value === null) localStorage.removeItem(key); else localStorage.setItem(key, value); }
        catch { rollbackFailed = true; }
      }
      throw new Error(rollbackFailed
        ? 'Lưu thất bại và không thể khôi phục toàn bộ dữ liệu cũ. Hãy dùng tệp sao lưu để nhập lại.'
        : 'Lưu thất bại; dữ liệu cũ đã được khôi phục. Hãy kiểm tra dung lượng hoặc quyền lưu trữ.');
    }
  }

  exportButton.addEventListener('click', () => {
    try {
      const bundle = { format: 'electric-basic-reader-data', version: 1,
        exportedAt: new Date().toISOString(), data: readCurrent() };
      validate(bundle);
      const blob = new Blob([JSON.stringify(bundle, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `electric-basic-reader-${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(link);
      link.click();
      link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 30000);
      exportStatus.textContent = 'Đã tạo tệp sao lưu JSON từ dữ liệu trên thiết bị này.';
    } catch { exportStatus.textContent = 'Không thể đọc dữ liệu hiện có để xuất. Chưa tạo tệp sao lưu.'; }
  });

  fileInput.addEventListener('change', async () => {
    pending = null;
    previewPanel.hidden = true;
    const file = fileInput.files?.[0];
    if (!file) { importStatus.textContent = 'Chọn tệp để xem trước.'; return; }
    if (file.size > maxFileBytes) { importStatus.textContent = 'Tệp lớn hơn 5 MB; chưa đọc hoặc thay đổi dữ liệu.'; return; }
    try {
      const parsed = JSON.parse(await file.text());
      validate(parsed);
      pending = parsed;
      showPreview();
      importStatus.textContent = 'Tệp hợp lệ. Xem trước rồi chọn cách nhập.';
    } catch (error) {
      pending = null;
      previewPanel.hidden = true;
      importStatus.textContent = error instanceof SyntaxError
        ? 'JSON không hợp lệ. Dữ liệu hiện có chưa thay đổi.'
        : (error.message || 'Không thể đọc tệp. Dữ liệu hiện có chưa thay đổi.');
    }
  });

  importButton.addEventListener('click', () => {
    if (!pending) return;
    try {
      const current = readCurrent();
      if (fingerprint(current) !== previewFingerprint) {
        showPreview();
        importStatus.textContent = 'Dữ liệu trên thiết bị đã thay đổi. Hãy xem lại số liệu và xác nhận lần nữa.';
        return;
      }
      const mode = document.querySelector('input[name="import-mode"]:checked').value;
      const data = mode === 'replace' ? pending.data : mergeData(pending.data, current);
      validate({ format: 'electric-basic-reader-data', version: 1, exportedAt: pending.exportedAt, data });
      writeData(data);
      pending = null;
      previewPanel.hidden = true;
      importStatus.textContent = 'Đã nhập dữ liệu trên thiết bị này. Tải lại các bài đang mở để thấy thay đổi.';
    } catch (error) { importStatus.textContent = error.message || 'Không thể nhập dữ liệu; dữ liệu cũ được giữ nguyên.'; }
  });

  window.ReaderData = { validate, readCurrent, mergeData };
})();
