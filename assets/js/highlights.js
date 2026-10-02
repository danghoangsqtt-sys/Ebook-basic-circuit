/* Persistent, conservative highlights for one lesson's prose. */
(function () {
  'use strict';

  const script = document.currentScript;
  const STORAGE_KEY = 'ebook-highlights-v1';
  const CONTEXT_LENGTH = 120;
  const PROSE_SELECTOR = 'p, li, blockquote';
  const FORBIDDEN_SELECTOR = 'input, textarea, select, button, pre, code, table, form, script, style, nav, [contenteditable], .ebook-highlights-panel, .ebook-selection-trigger, .ebook-search-trigger';
  let content;
  let panel;
  let list;
  let summary;
  let status;
  let records = [];
  let locations = new Map();
  let storageReady = true;
  let initialized = false;

  function loadCss() {
    if (document.querySelector('link[data-ebook-highlights-css]')) return;
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.dataset.ebookHighlightsCss = 'true';
    link.href = script?.src
      ? new URL('../css/highlights.css', script.src).href
      : new URL('../assets/css/highlights.css', document.baseURI).href;
    document.head.appendChild(link);
  }

  function currentLessonId() {
    const match = window.location.pathname.match(/(?:^|\/)day(0[1-9]|[1-4][0-9]|5[0-6])\.html$/);
    return match ? `day${match[1]}` : null;
  }

  function validRecord(record) {
    return record && typeof record === 'object' && record.version === 1
      && typeof record.id === 'string' && record.id.length > 0
      && /^day(0[1-9]|[1-4][0-9]|5[0-6])$/.test(record.lessonId)
      && typeof record.quote === 'string' && record.quote.length > 0 && record.quote.length <= 1000
      && record.anchor && typeof record.anchor === 'object'
      && typeof record.anchor.prefix === 'string' && record.anchor.prefix.length <= 120
      && typeof record.anchor.suffix === 'string' && record.anchor.suffix.length <= 120
      && Number.isInteger(record.anchor.occurrence) && record.anchor.occurrence >= 0
      && (record.anchor.sectionId === undefined || typeof record.anchor.sectionId === 'string')
      && typeof record.createdAt === 'string' && !Number.isNaN(Date.parse(record.createdAt));
  }

  function readStorage() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw === null) {
        records = [];
        storageReady = true;
        return;
      }
      const parsed = JSON.parse(raw);
      if (!Array.isArray(parsed) || parsed.some(item => !validRecord(item))
        || new Set(parsed.map(item => item.id)).size !== parsed.length) {
        records = [];
        storageReady = false;
        return;
      }
      records = parsed;
      storageReady = true;
    } catch {
      records = [];
      storageReady = false;
    }
  }

  function persist(nextRecords) {
    if (!storageReady) return false;
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(nextRecords));
      records = nextRecords;
      return true;
    } catch {
      storageReady = false;
      return false;
    }
  }

  function announce(message) {
    if (panel) panel.open = true;
    if (status) status.textContent = message;
  }

  function isProseBlock(block) {
    return block && content.contains(block)
      && !block.closest(FORBIDDEN_SELECTOR)
      && !block.querySelector(PROSE_SELECTOR);
  }

  function proseBlock(node) {
    const element = node?.nodeType === Node.ELEMENT_NODE ? node : node?.parentElement;
    const block = element?.closest(PROSE_SELECTOR);
    return isProseBlock(block) ? block : null;
  }

  function allProseBlocks() {
    return [...content.querySelectorAll(PROSE_SELECTOR)].filter(isProseBlock);
  }

  function headingFallbackId(heading, index) {
    const text = heading.textContent.replace(/\s+/g, ' ').trim();
    let hash = 2166136261;
    for (const char of text) {
      hash ^= char.codePointAt(0);
      hash = Math.imul(hash, 16777619);
    }
    return `heading-${index}-${(hash >>> 0).toString(36)}`;
  }

  function sectionIdFor(block) {
    let sectionId = 'intro';
    for (const [index, heading] of [...content.querySelectorAll('h2, h3')].entries()) {
      if (!(heading.compareDocumentPosition(block) & Node.DOCUMENT_POSITION_FOLLOWING)) break;
      sectionId = heading.id || headingFallbackId(heading, index);
    }
    return sectionId;
  }

  function offsetsForRange(block, range) {
    try {
      const beforeStart = document.createRange();
      beforeStart.selectNodeContents(block);
      beforeStart.setEnd(range.startContainer, range.startOffset);
      const beforeEnd = document.createRange();
      beforeEnd.selectNodeContents(block);
      beforeEnd.setEnd(range.endContainer, range.endOffset);
      return { start: beforeStart.toString().length, end: beforeEnd.toString().length };
    } catch { return null; }
  }

  function quoteOccurrences(text, quote) {
    const positions = [];
    for (let at = text.indexOf(quote); at !== -1; at = text.indexOf(quote, at + 1)) {
      positions.push(at);
    }
    return positions;
  }

  function occurrenceFor(block, start, quote, sectionId) {
    let ordinal = 0;
    for (const candidate of allProseBlocks()) {
      if (sectionIdFor(candidate) !== sectionId) continue;
      for (const at of quoteOccurrences(candidate.textContent, quote)) {
        if (candidate === block && at === start) return ordinal;
        ordinal += 1;
      }
    }
    return -1;
  }

  function locate(record) {
    if (record.lessonId !== currentLessonId()) return null;
    const matches = [];
    let ordinal = 0;
    for (const block of allProseBlocks()) {
      if (record.anchor.sectionId !== undefined && sectionIdFor(block) !== record.anchor.sectionId) continue;
      const text = block.textContent;
      for (const at of quoteOccurrences(text, record.quote)) {
        const prefix = text.slice(Math.max(0, at - record.anchor.prefix.length), at);
        const suffix = text.slice(at + record.quote.length, at + record.quote.length + record.anchor.suffix.length);
        if (prefix === record.anchor.prefix && suffix === record.anchor.suffix) {
          matches.push({ block, start: at, end: at + record.quote.length, occurrence: ordinal });
        }
        ordinal += 1;
      }
    }
    // An ordinal alone is unsafe after editing. Both context and ordinal must agree uniquely.
    return matches.length === 1 && matches[0].occurrence === record.anchor.occurrence
      ? matches[0] : null;
  }

  function overlaps(a, b) {
    return a.block === b.block && a.start < b.end && b.start < a.end;
  }

  function clearMarks() {
    content.querySelectorAll('mark[data-ebook-highlight-id]').forEach(mark => {
      const parent = mark.parentNode;
      mark.replaceWith(...mark.childNodes);
      parent.normalize();
    });
  }

  function paint(location, id) {
    const walker = document.createTreeWalker(location.block, NodeFilter.SHOW_TEXT);
    const pieces = [];
    let node;
    let cursor = 0;
    while ((node = walker.nextNode())) {
      const next = cursor + node.length;
      if (next > location.start && cursor < location.end) {
        pieces.push({ node, from: Math.max(0, location.start - cursor), to: Math.min(node.length, location.end - cursor) });
      }
      cursor = next;
    }
    for (const piece of pieces) {
      let selected = piece.node;
      if (piece.from > 0) selected = selected.splitText(piece.from);
      const length = piece.to - piece.from;
      if (length < selected.length) selected.splitText(length);
      const mark = document.createElement('mark');
      mark.className = 'ebook-highlight';
      mark.dataset.ebookHighlightId = id;
      mark.title = 'Đoạn đã đánh dấu';
      selected.replaceWith(mark);
      mark.appendChild(selected);
    }
  }

  function renderMarks() {
    clearMarks();
    locations = new Map();
    const candidates = records.filter(item => item.lessonId === currentLessonId())
      .map(record => ({ id: record.id, location: locate(record) }));
    const conflicted = new Set();
    for (const candidate of candidates) {
      if (!candidate.location) continue;
      if (candidates.some(other => other !== candidate && other.location
        && overlaps(candidate.location, other.location))) {
        conflicted.add(candidate.id);
      }
    }
    for (const candidate of candidates) {
      if (!candidate.location || conflicted.has(candidate.id)) continue;
      paint(candidate.location, candidate.id);
      locations.set(candidate.id, candidate.location);
    }
    renderList();
  }

  function makeButton(label, onClick) {
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = label;
    button.addEventListener('click', onClick);
    return button;
  }

  function renderList() {
    if (!list) return;
    list.replaceChildren();
    const current = records.filter(item => item.lessonId === currentLessonId());
    const orphanCount = current.filter(item => !locations.has(item.id)).length;
    summary.textContent = `Dấu đã lưu trong bài (${current.length})${orphanCount ? ` · ${orphanCount} mất vị trí` : ''}`;
    if (!current.length) {
      const item = document.createElement('li');
      item.className = 'ebook-highlights-empty';
      item.textContent = 'Chưa có đoạn nào được đánh dấu.';
      list.appendChild(item);
      return;
    }
    for (const record of current) {
      const item = document.createElement('li');
      item.className = 'ebook-highlights-item';
      const quote = document.createElement('div');
      quote.className = 'ebook-highlights-quote';
      quote.textContent = record.quote.replace(/\s+/g, ' ').trim();
      const state = document.createElement('span');
      state.className = 'ebook-highlights-state';
      const anchored = locations.has(record.id);
      state.textContent = anchored ? 'Đã tìm thấy trong bài' : 'Mất vị trí trong bài';
      const controls = document.createElement('div');
      controls.className = 'ebook-highlights-controls';
      const jump = makeButton('Đến đoạn', () => jumpTo(record.id));
      jump.disabled = !anchored;
      jump.setAttribute('aria-label', `Đến đoạn: ${quote.textContent.slice(0, 80)}`);
      const removeButton = makeButton('Xóa dấu', () => remove(record.id));
      removeButton.setAttribute('aria-label', `Xóa dấu: ${quote.textContent.slice(0, 80)}`);
      controls.append(jump, removeButton);
      item.append(quote, state, controls);
      list.appendChild(item);
    }
  }

  function jumpTo(id) {
    const mark = [...content.querySelectorAll('mark[data-ebook-highlight-id]')]
      .find(item => item.dataset.ebookHighlightId === id);
    if (!mark) {
      panel.open = true;
      announce('Không tìm thấy vị trí của dấu này trong bài hiện tại.');
      return false;
    }
    mark.tabIndex = -1;
    mark.scrollIntoView({ behavior: 'smooth', block: 'center' });
    mark.focus({ preventScroll: true });
    announce('Đã chuyển tới đoạn được đánh dấu.');
    return true;
  }

  function addHighlight(selectedText, range) {
    if (!storageReady) {
      panel.open = true;
      announce('Không thể lưu dấu trên thiết bị này. Dữ liệu hiện có không truy cập được hoặc không đúng định dạng.');
      return false;
    }
    if (!range || range.collapsed || !content.contains(range.commonAncestorContainer)) {
      announce('Hãy chọn một đoạn văn trong bài học.');
      return false;
    }
    const block = proseBlock(range.startContainer);
    if (!block || proseBlock(range.endContainer) !== block
      || range.cloneContents().querySelector(FORBIDDEN_SELECTOR + ', p, li, blockquote, div')) {
      announce('Chỉ đánh dấu văn xuôi trong cùng một đoạn; không chọn bảng, mã hoặc nút điều khiển.');
      return false;
    }
    const offsets = offsetsForRange(block, range);
    const text = block.textContent;
    const quote = range.toString();
    if (!offsets || offsets.start >= offsets.end || !quote.trim() || quote.length > 1000
      || text.slice(offsets.start, offsets.end) !== quote) {
      announce('Đoạn chọn không thể lưu an toàn. Hãy chọn lại một đoạn ngắn.');
      return false;
    }
    const sectionId = sectionIdFor(block);
    const occurrence = occurrenceFor(block, offsets.start, quote, sectionId);
    if (occurrence < 0) {
      announce('Không xác định được vị trí duy nhất của đoạn đã chọn.');
      return false;
    }
    const location = { block, start: offsets.start, end: offsets.end };
    if ([...locations.values()].some(existing => overlaps(location, existing))) {
      announce('Đoạn này đã giao với một dấu khác. Hãy chọn phần văn bản không chồng lấn.');
      return false;
    }
    const record = {
      version: 1,
      id: window.crypto?.randomUUID?.() || `h-${Date.now()}-${Math.random().toString(36).slice(2)}`,
      lessonId: currentLessonId(),
      quote,
      anchor: {
        prefix: text.slice(Math.max(0, offsets.start - CONTEXT_LENGTH), offsets.start),
        suffix: text.slice(offsets.end, offsets.end + CONTEXT_LENGTH),
        occurrence,
        sectionId
      },
      createdAt: new Date().toISOString()
    };
    if (!locate(record)) {
      announce('Đoạn này trùng với vị trí khác hoặc không thể neo chắc chắn; chưa lưu dấu.');
      return false;
    }
    if (!persist([...records, record])) {
      panel.open = true;
      announce('Không thể lưu dấu trên thiết bị này. Vui lòng kiểm tra chế độ riêng tư hoặc bộ nhớ trình duyệt.');
      return false;
    }
    renderMarks();
    panel.open = true;
    announce('Đã đánh dấu và lưu trên thiết bị này.');
    return true;
  }

  function remove(id) {
    if (!initialized) readStorage();
    if (typeof id !== 'string' || !records.some(item => item.id === id)) return false;
    if (!persist(records.filter(item => item.id !== id))) {
      announce('Không thể xóa dấu vì không lưu được thay đổi trên thiết bị này.');
      return false;
    }
    if (initialized) renderMarks();
    announce('Đã xóa dấu.');
    return true;
  }

  function getAll() {
    if (!initialized) readStorage();
    return JSON.parse(JSON.stringify(records));
  }

  function verify(record) {
    if (!validRecord(record)) return { status: 'invalid' };
    if (record.lessonId !== currentLessonId()) return { status: 'different-lesson' };
    return { status: locate(record) ? 'anchored' : 'orphan' };
  }

  function makePanel() {
    panel = document.createElement('details');
    panel.className = 'ebook-highlights-panel';
    summary = document.createElement('summary');
    list = document.createElement('ul');
    list.className = 'ebook-highlights-list';
    status = document.createElement('p');
    status.className = 'ebook-highlights-status';
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    const privacy = document.createElement('p');
    privacy.className = 'ebook-highlights-privacy';
    privacy.textContent = 'Dấu chỉ lưu trên thiết bị này; bạn có thể xóa từng dấu bất cứ lúc nào.';
    panel.append(summary, status, privacy, list);
    const selectionStatus = content.querySelector('.ebook-selection-status');
    if (selectionStatus) selectionStatus.after(panel);
    else content.prepend(panel);
  }

  function init() {
    if (initialized) return true;
    content = document.querySelector('.content-area');
    if (!content || !currentLessonId()) return false;
    loadCss();
    readStorage();
    makePanel();
    renderMarks();
    if (!storageReady) {
      panel.open = true;
      announce('Không thể đọc hoặc lưu dấu trên thiết bị này. Bài học vẫn đọc được bình thường.');
    } else {
      const orphanCount = records.filter(item => item.lessonId === currentLessonId() && !locations.has(item.id)).length;
      if (orphanCount) {
        panel.open = true;
        announce(`${orphanCount} dấu đã lưu không còn vị trí chắc chắn trong bài; chưa tô các đoạn này.`);
      }
    }
    window.EbookSelectionActions?.registerAction({
      id: 'highlight', label: 'Đánh dấu đoạn văn', run: addHighlight
    });
    initialized = true;
    const requestedId = new URLSearchParams(window.location.search).get('highlight');
    if (requestedId && records.some(item => item.id === requestedId && item.lessonId === currentLessonId())) {
      window.setTimeout(() => jumpTo(requestedId), 250);
    }
    return true;
  }

  function refresh() {
    if (!initialized) {
      readStorage();
      return storageReady;
    }
    readStorage();
    renderMarks();
    announce(storageReady ? 'Đã nạp lại dấu trên thiết bị.' : 'Không thể đọc dữ liệu dấu trên thiết bị này.');
    return storageReady;
  }

  window.EbookHighlights = { init, getAll, remove, verify, refresh, jumpTo };
})();
