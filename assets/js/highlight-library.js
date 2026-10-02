/* Cross-lesson view of locally stored highlights. */
(function () {
  'use strict';

  const STORAGE_KEY = 'ebook-highlights-v1';
  const root = new URL('../../', document.currentScript.src);
  const titleById = new Map(CURRICULUM.weeks.flatMap(week => week.lessons.map(lesson => [
    `day${String(lesson.day).padStart(2, '0')}`, `Bài ${lesson.day}: ${lesson.title}`
  ])));
  const query = document.querySelector('#highlight-query');
  const lessonFilter = document.querySelector('#highlight-lesson');
  const stateFilter = document.querySelector('#highlight-state');
  const status = document.querySelector('#highlight-status');
  const list = document.querySelector('#highlight-list');
  let records = [];
  let storageReadable = true;
  const anchorStates = new Map();

  function valid(record) {
    return record && record.version === 1 && typeof record.id === 'string' && record.id.length > 0
      && /^day(0[1-9]|[1-4][0-9]|5[0-6])$/.test(record.lessonId)
      && typeof record.quote === 'string' && record.quote.length > 0 && record.quote.length <= 1000
      && record.anchor && typeof record.anchor.prefix === 'string' && record.anchor.prefix.length <= 120
      && typeof record.anchor.suffix === 'string' && record.anchor.suffix.length <= 120
      && Number.isInteger(record.anchor.occurrence) && record.anchor.occurrence >= 0
      && (record.anchor.sectionId === undefined || typeof record.anchor.sectionId === 'string')
      && typeof record.createdAt === 'string' && !Number.isNaN(Date.parse(record.createdAt));
  }

  function read() {
    try {
      const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
      if (!Array.isArray(parsed) || parsed.some(item => !valid(item))
        || new Set(parsed.map(item => item.id)).size !== parsed.length) throw new Error('invalid data');
      records = parsed;
      storageReadable = true;
    } catch {
      records = [];
      storageReadable = false;
      status.textContent = 'Không thể đọc dữ liệu dấu trên thiết bị này. Bài học vẫn mở được bình thường.';
      return false;
    }
    return true;
  }

  function lessonUrl(id) {
    const day = Number(id.slice(3));
    return new URL(`week${Math.ceil(day / 7)}/day${String(day).padStart(2, '0')}.html`, root);
  }

  function headingFallbackId(heading, index) {
    const text = heading.textContent.replace(/\s+/g, ' ').trim();
    let hash = 2166136261;
    for (const char of text) { hash ^= char.codePointAt(0); hash = Math.imul(hash, 16777619); }
    return `heading-${index}-${(hash >>> 0).toString(36)}`;
  }

  function sectionIdFor(content, block, headings) {
    let sectionId = 'intro';
    for (const [index, heading] of headings.entries()) {
      if (!(heading.compareDocumentPosition(block) & Node.DOCUMENT_POSITION_FOLLOWING)) break;
      sectionId = heading.id || headingFallbackId(heading, index);
    }
    return sectionId;
  }

  function anchoredIn(record, content) {
    if (!content) return false;
    const headings = [...content.querySelectorAll('h2,h3')];
    const blocks = [...content.querySelectorAll('p,li,blockquote')].filter(block =>
      !block.closest('pre,code,table,form,nav') && !block.querySelector('p,li,blockquote'));
    let ordinal = 0;
    const matches = [];
    for (const block of blocks) {
      if (record.anchor.sectionId !== undefined && sectionIdFor(content, block, headings) !== record.anchor.sectionId) continue;
      const text = block.textContent;
      for (let at = text.indexOf(record.quote); at !== -1; at = text.indexOf(record.quote, at + 1)) {
        const prefix = text.slice(Math.max(0, at - record.anchor.prefix.length), at);
        const suffix = text.slice(at + record.quote.length, at + record.quote.length + record.anchor.suffix.length);
        if (prefix === record.anchor.prefix && suffix === record.anchor.suffix) matches.push(ordinal);
        ordinal += 1;
      }
    }
    return matches.length === 1 && matches[0] === record.anchor.occurrence;
  }

  async function verifyAll() {
    const groups = new Map();
    for (const record of records) {
      if (!groups.has(record.lessonId)) groups.set(record.lessonId, []);
      groups.get(record.lessonId).push(record);
    }
    await Promise.all([...groups].map(async ([id, group]) => {
      try {
        const response = await fetch(lessonUrl(id));
        if (!response.ok) throw new Error('lesson unavailable');
        const doc = new DOMParser().parseFromString(await response.text(), 'text/html');
        const content = doc.querySelector('.content-area');
        if (!content) throw new Error('content unavailable');
        group.forEach(record => anchorStates.set(record.id, anchoredIn(record, content) ? 'anchored' : 'orphan'));
      } catch { group.forEach(record => anchorStates.set(record.id, 'unknown')); }
    }));
    render();
  }

  function remove(id) {
    const next = records.filter(record => record.id !== id);
    if (next.length === records.length) return;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
      records = next;
      anchorStates.delete(id);
      render();
      status.textContent = 'Đã xóa một dấu. Các dấu khác được giữ nguyên.';
    } catch { status.textContent = 'Không thể xóa dấu vì trình duyệt không cho lưu thay đổi.'; }
  }

  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function render() {
    const needle = query.value.trim().normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    const visible = records.filter(record => {
      const title = titleById.get(record.lessonId) || record.lessonId;
      const haystack = `${record.quote} ${title}`.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
      return (!needle || haystack.includes(needle)) && (!lessonFilter.value || record.lessonId === lessonFilter.value)
        && (!stateFilter.value || (anchorStates.get(record.id) || 'unknown') === stateFilter.value);
    });
    list.replaceChildren();
    status.textContent = records.length
      ? `${visible.length} trong ${records.length} dấu phù hợp.`
      : 'Chưa có dấu nào. Mở một bài, chọn đoạn văn rồi dùng “Đánh dấu đoạn văn”.';
    for (const record of visible) {
      const state = anchorStates.get(record.id) || 'unknown';
      const item = element('li', 'highlight-item');
      const title = element('h3', '', titleById.get(record.lessonId) || record.lessonId);
      const quote = element('p', 'highlight-quote', record.quote.replace(/\s+/g, ' ').trim());
      const meta = element('p', 'highlight-meta', `Lưu ngày ${new Date(record.createdAt).toLocaleDateString('vi-VN')}`);
      const stateText = { anchored: 'Còn vị trí trong bài', orphan: 'Mất vị trí trong bài', unknown: 'Chưa kiểm tra được vị trí' }[state];
      const stateNode = element('p', 'highlight-state', stateText);
      stateNode.dataset.state = state;
      const controls = element('div', 'highlight-controls');
      const lesson = element('a', '', state === 'anchored' ? 'Đến đoạn' : 'Mở bài');
      const url = lessonUrl(record.lessonId);
      if (state === 'anchored') url.searchParams.set('highlight', record.id);
      lesson.href = url.href;
      const del = element('button', '', 'Xóa dấu');
      del.type = 'button';
      del.setAttribute('aria-label', `Xóa dấu trong ${title.textContent}: ${quote.textContent.slice(0, 80)}`);
      del.addEventListener('click', () => remove(record.id));
      controls.append(lesson, del);
      item.append(title, quote, meta, stateNode, controls);
      list.appendChild(item);
    }
  }

  for (const [id, title] of titleById) {
    const option = element('option', '', title);
    option.value = id;
    lessonFilter.appendChild(option);
  }
  [query, lessonFilter, stateFilter].forEach(control => control.addEventListener('input', () => {
    if (storageReadable) render();
  }));
  if (read()) { render(); verifyAll(); }
})();
