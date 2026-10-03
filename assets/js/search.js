/* Local search for the generated lesson index. No network requests. */
(function () {
  'use strict';

  const script = document.currentScript || document.querySelector('script[src$="/search.js"]');
  const siteRoot = script ? new URL('../../', script.src) : new URL('../', document.baseURI);
  const stopWords = new Set('và là của cho trong một những các với được từ đến khi như trên dưới này đó thì sẽ có bạn bài học phần để về bằng tại hay hoặc mà cần nên sau trước theo tìm giải thích liên quan'.split(' '));
  // Editorial aliases for terms used in the lessons, not an open-ended query expansion.
  const concepts = [
    ['dien ap', 'voltage', 'volt'],
    ['dong dien', 'current', 'ampere'],
    ['dien tro', 'resistor', 'resistance'],
    ['tu dien', 'capacitor', 'capacitance'],
    ['vi dieu khien', 'microcontroller', 'mcu'],
    ['mach in', 'pcb', 'printed circuit board'],
    ['cam bien', 'sensor']
  ];
  const limit = 8;
  let overlay, input, results, status, trigger, returnFocus, previousOverflow;
  let cachedIndex, normalizedIndex;

  function normalize(value) {
    return String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase();
  }

  function terms(query) {
    let remaining = normalize(query).replace(/[^a-z0-9]+/g, ' ').trim();
    const units = [];
    for (const aliases of concepts) {
      const matched = aliases.find(alias => new RegExp(`(?:^| )${alias}(?: |$)`).test(remaining));
      if (!matched) continue;
      units.push({ variants: aliases, exact: matched });
      remaining = remaining.replace(new RegExp(`(?:^| )${matched}(?= |$)`), ' ').replace(/\s+/g, ' ').trim();
    }
    const words = remaining.match(/[a-z0-9]+/g) || [];
    for (const word of new Set(words.filter(part => part.length >= 2 && !stopWords.has(part)))) {
      units.push({ variants: [word], exact: word });
    }
    return units.slice(0, 10);
  }

  function getIndex() {
    const data = window.EbookSearchIndex;
    if (!data || data.version !== 1 || !Array.isArray(data.lessons)) return [];
    if (cachedIndex !== data) {
      cachedIndex = data;
      normalizedIndex = data.lessons.map(lesson => ({
        lesson,
        title: normalize(lesson.title),
        headings: lesson.headings.map(normalize),
        text: normalize(lesson.text)
      }));
    }
    return normalizedIndex;
  }

  function snippet(text, units) {
    // Map accent-folded positions back to the original text so Vietnamese snippets start at the match.
    let flat = '';
    const offsets = [];
    for (let at = 0; at < text.length;) {
      const char = String.fromCodePoint(text.codePointAt(at));
      const folded = normalize(char);
      flat += folded;
      for (let i = 0; i < folded.length; i += 1) offsets.push(at);
      at += char.length;
    }
    const positions = units.flatMap(unit => unit.variants.map(variant => flat.indexOf(variant)))
      .filter(position => position >= 0);
    const first = positions.length ? Math.min(...positions) : 0;
    const startPosition = Math.max(0, first - 55);
    const endPosition = Math.min(flat.length, Math.max(first + 105, startPosition + 155));
    const start = offsets[startPosition] || 0;
    const end = endPosition >= offsets.length ? text.length : offsets[endPosition];
    return (start ? '…' : '') + text.slice(start, end).trim() + (end < text.length ? '…' : '');
  }

  function search(query) {
    const units = terms(String(query || '').slice(0, 240));
    if (!units.length) return [];
    const phrase = normalize(query).trim();
    return getIndex().map(item => {
      const hits = field => units.filter(unit => unit.variants.some(variant => field.includes(variant))).length;
      const exactHits = field => units.filter(unit => field.includes(unit.exact)).length;
      const titleHits = hits(item.title);
      const headingHitsByIndex = item.headings.map(hits);
      const headingHits = Math.max(0, ...headingHitsByIndex);
      const bodyHits = hits(item.text);
      const tier = titleHits ? 1000 : headingHits ? 100 : bodyHits ? 10 : 0;
      if (!tier) return null;
      const score = tier + titleHits * 20 + headingHits * 8 + bodyHits * 2
        + exactHits(item.title) * 10 + exactHits(item.text)
        + (phrase.length <= 80 && item.title.includes(phrase) ? 35 : 0)
        + (phrase.length <= 80 && item.headings.some(heading => heading.includes(phrase)) ? 12 : 0);
      const headingIndex = headingHits ? headingHitsByIndex.indexOf(headingHits) : -1;
      const heading = headingIndex >= 0 ? item.lesson.headings[headingIndex] : '';
      return { id: item.lesson.id, title: item.lesson.title, heading,
        url: new URL(item.lesson.url, siteRoot).href,
        snippet: snippet(item.lesson.text, units), score };
    }).filter(Boolean).sort((a, b) => b.score - a.score || a.id.localeCompare(b.id)).slice(0, limit);
  }

  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function render() {
    const query = input.value.trim();
    results.replaceChildren();
    if (!query) {
      status.textContent = `Nhập từ khóa hoặc một câu ngắn để tìm trong ${window.EbookSearchIndex?.lessons?.length || 56} bài.`;
      return;
    }
    if (!getIndex().length) {
      status.textContent = 'Chỉ mục tìm kiếm chưa được tải. Hãy tải lại trang.';
      return;
    }
    const found = search(query);
    if (!found.length) {
      status.textContent = 'Không tìm thấy bài phù hợp. Thử một thuật ngữ ngắn hơn, có hoặc không dấu.';
      return;
    }
    status.textContent = `Tìm thấy ${found.length} bài phù hợp${found.length === limit ? ' (hiển thị tối đa 8)' : ''}.`;
    found.forEach(item => {
      const li = element('li', 'ebook-search-item');
      const link = element('a', 'ebook-search-link', item.title);
      link.href = item.url;
      const heading = item.heading ? element('span', 'ebook-search-heading', `Đề mục: ${item.heading}`) : null;
      const excerpt = element('span', 'ebook-search-excerpt', item.snippet);
      if (heading) link.appendChild(heading);
      link.appendChild(excerpt);
      li.appendChild(link);
      results.appendChild(li);
    });
  }

  function close() {
    if (!overlay || overlay.hidden) return;
    overlay.hidden = true;
    document.body.style.overflow = previousOverflow;
    if (returnFocus && returnFocus.isConnected) returnFocus.focus();
  }

  function open(query = '') {
    if (!overlay && !init()) return;
    returnFocus = document.activeElement instanceof HTMLElement ? document.activeElement : trigger;
    previousOverflow = document.body.style.overflow;
    overlay.hidden = false;
    document.body.style.overflow = 'hidden';
    input.value = String(query || '').slice(0, 240);
    render();
    input.focus();
    input.select();
  }

  function loadCss() {
    if (document.querySelector('link[data-ebook-search-css]')) return;
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.dataset.ebookSearchCss = 'true';
    link.href = new URL('../css/search.css', script ? script.src : siteRoot).href;
    document.head.appendChild(link);
  }

  function init() {
    if (overlay) return true;
    const content = document.querySelector('.content-area');
    if (!content) return false;
    loadCss();
    trigger = element('button', 'ebook-search-trigger', `🔎 Tìm trong ${window.EbookSearchIndex?.lessons?.length || 56} bài`);
    trigger.type = 'button';
    trigger.addEventListener('click', () => open());
    content.prepend(trigger);

    overlay = element('div', 'ebook-search-overlay');
    overlay.hidden = true;
    const dialog = element('section', 'ebook-search-dialog');
    dialog.setAttribute('role', 'dialog');
    dialog.setAttribute('aria-modal', 'true');
    dialog.setAttribute('aria-labelledby', 'ebook-search-title');
    const header = element('div', 'ebook-search-header');
    const title = element('h2', '', `Tìm trong ${window.EbookSearchIndex?.lessons?.length || 56} bài học`);
    title.id = 'ebook-search-title';
    const closeButton = element('button', 'ebook-search-close', 'Đóng');
    closeButton.type = 'button';
    closeButton.setAttribute('aria-label', 'Đóng tìm kiếm');
    closeButton.addEventListener('click', close);
    header.append(title, closeButton);
    const label = element('label', 'ebook-search-label', 'Từ khóa hoặc câu cần tìm');
    label.htmlFor = 'ebook-search-input';
    input = element('input', 'ebook-search-input');
    input.id = 'ebook-search-input';
    input.type = 'search';
    input.maxLength = 240;
    input.autocomplete = 'off';
    input.addEventListener('input', render);
    status = element('p', 'ebook-search-status');
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    results = element('ul', 'ebook-search-results');
    dialog.append(header, label, input, status, results);
    overlay.appendChild(dialog);
    overlay.addEventListener('click', event => { if (event.target === overlay) close(); });
    overlay.addEventListener('keydown', event => {
      if (event.key === 'Escape') { event.preventDefault(); close(); return; }
      if (event.key !== 'Tab') return;
      const focusable = [...dialog.querySelectorAll('button,input,a[href]')];
      const first = focusable[0], last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    });
    document.body.appendChild(overlay);
    return true;
  }

  window.EbookSearch = { init, open, close, search, normalize };
})();
