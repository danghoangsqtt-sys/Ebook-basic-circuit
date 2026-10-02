/* Actions for selected lesson prose. Other reader features can register actions. */
(function () {
  'use strict';

  const script = document.currentScript;
  const actions = [];
  let content, trigger, menu, actionList, status, saved, returnFocus;
  let initialized = false;
  let mobileTimer;
  let dismissedRange;
  let repositionFrame;

  function loadCss() {
    if (document.querySelector('link[data-ebook-selection-css]')) return;
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.dataset.ebookSelectionCss = 'true';
    link.href = script?.src
      ? new URL('../css/selection-actions.css', script.src).href
      : new URL('../assets/css/selection-actions.css', document.baseURI).href;
    document.head.appendChild(link);
  }

  function elementInContent(node) {
    return content && node && content.contains(node.nodeType === Node.ELEMENT_NODE ? node : node.parentElement);
  }

  function forbidden(node) {
    const element = node.nodeType === Node.ELEMENT_NODE ? node : node.parentElement;
    return !!element?.closest('input, textarea, select, button, pre, code, script, style, nav, .ebook-selection-trigger, .ebook-search-trigger');
  }

  function capture() {
    const selection = window.getSelection();
    if (!selection || selection.isCollapsed || !selection.rangeCount) return null;
    const range = selection.getRangeAt(0);
    if (range.collapsed || !elementInContent(range.startContainer) || !elementInContent(range.endContainer)) return null;
    if (forbidden(range.startContainer) || forbidden(range.endContainer)) return null;
    const text = selection.toString().replace(/\s+/g, ' ').trim();
    if (!text || text.length > 240) return null;
    const fragment = range.cloneContents();
    if (fragment.querySelector('input, textarea, select, button, pre, code, script, style, nav')) return null;
    const rects = [...range.getClientRects()].filter(rect => rect.width > 0 && rect.height > 0);
    if (!rects.length) return null;
    return { text, range: range.cloneRange(), rects };
  }

  function sameRange(a, b) {
    if (!a || !b || a.text !== b.text) return false;
    try {
      return a.range.compareBoundaryPoints(Range.START_TO_START, b.range) === 0
        && a.range.compareBoundaryPoints(Range.END_TO_END, b.range) === 0;
    } catch { return false; }
  }

  function pointOnSelection(x, y, rects) {
    return rects.some(rect => x >= rect.left - 5 && x <= rect.right + 5
      && y >= rect.top - 5 && y <= rect.bottom + 5);
  }

  function anchorRect(snapshot) {
    const rects = [...snapshot.range.getClientRects()].filter(rect => rect.width > 0 && rect.height > 0);
    return rects[rects.length - 1] || snapshot.range.getBoundingClientRect();
  }

  function positionMenu(snapshot, x, y) {
    const gutter = 8;
    const viewportWidth = window.visualViewport?.width || window.innerWidth;
    const viewportHeight = window.visualViewport?.height || window.innerHeight;
    const rect = anchorRect(snapshot);
    const menuRect = menu.getBoundingClientRect();
    const desiredX = Number.isFinite(x) ? x : rect.left;
    const desiredY = Number.isFinite(y) ? y : rect.bottom + 8;
    const left = Math.max(gutter, Math.min(desiredX, viewportWidth - menuRect.width - gutter));
    const below = desiredY + menuRect.height <= viewportHeight - gutter;
    const above = rect.top - menuRect.height - 8;
    const top = below ? desiredY : above >= gutter ? above
      : Math.max(gutter, viewportHeight - menuRect.height - gutter);
    menu.style.left = `${Math.round(left)}px`;
    menu.style.top = `${Math.round(top)}px`;
  }

  function schedulePosition() {
    if (!menu || menu.hidden || !saved || repositionFrame) return;
    repositionFrame = window.requestAnimationFrame(() => {
      repositionFrame = 0;
      if (!menu.hidden && saved) positionMenu(saved);
    });
  }

  function close(restoreFocus = true) {
    if (!menu || menu.hidden) return;
    menu.hidden = true;
    trigger.setAttribute('aria-expanded', 'false');
    dismissedRange = saved;
    if (restoreFocus && returnFocus?.isConnected) returnFocus.focus();
  }

  function show(snapshot, source, x, y) {
    saved = snapshot;
    if (menu.hidden) {
      returnFocus = document.activeElement instanceof HTMLElement && document.activeElement !== document.body
        ? document.activeElement : trigger;
    }
    status.textContent = 'Đã chọn văn bản. Chọn thao tác trong menu.';
    menu.hidden = false;
    trigger.setAttribute('aria-expanded', 'true');
    positionMenu(snapshot, x, y);
    actionList.querySelector('button')?.focus();
  }

  function openFromSelection(source = 'keyboard', x, y) {
    const snapshot = capture();
    if (!snapshot) {
      if (source === 'button') {
        status.textContent = 'Hãy chọn một đoạn văn trong bài học, rồi mở lại menu.';
        trigger.focus();
      }
      return false;
    }
    show(snapshot, source, x, y);
    return true;
  }

  function addActionButton(action) {
    if (!actionList) return;
    const button = document.createElement('button');
    button.type = 'button';
    button.dataset.action = action.id;
    button.textContent = action.label;
    button.addEventListener('click', () => {
      const snapshot = saved;
      if (!snapshot) return;
      close();
      // Keep the command synchronous: browser popup blockers require a user gesture.
      try {
        const result = action.run(snapshot.text, snapshot.range.cloneRange());
        if (result?.catch) result.catch(error => console.warn('Thao tác văn bản thất bại:', error));
      } catch (error) {
        console.warn('Thao tác văn bản thất bại:', error);
      }
    });
    actionList.appendChild(button);
  }

  function registerAction(action) {
    if (!action || typeof action.id !== 'string' || !/^[a-z][a-z0-9-]*$/.test(action.id)
      || typeof action.label !== 'string' || !action.label.trim() || typeof action.run !== 'function'
      || actions.some(item => item.id === action.id)) return false;
    actions.push(action);
    addActionButton(action);
    return true;
  }

  function externalSearch(base, parameter, query) {
    const url = new URL(base);
    url.search = new URLSearchParams({ [parameter]: query }).toString();
    window.open(url.href, '_blank', 'noopener,noreferrer');
  }

  function copyText(text, range) {
    if (navigator.clipboard?.writeText) {
      return navigator.clipboard.writeText(text).catch(() => fallbackCopy(text, range));
    }
    fallbackCopy(text, range);
  }

  function fallbackCopy(text, range) {
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    if (!document.execCommand('copy')) {
      status.textContent = 'Không thể sao chép tự động. Hãy dùng Ctrl+C.';
      return;
    }
    status.textContent = 'Đã sao chép đoạn văn.';
  }

  function init() {
    if (initialized) return true;
    content = document.querySelector('.content-area');
    if (!content) return false;
    loadCss();

    trigger = document.createElement('button');
    trigger.type = 'button';
    trigger.className = 'ebook-selection-trigger';
    trigger.textContent = 'Tra cứu đoạn đã chọn';
    trigger.setAttribute('aria-controls', 'ebook-selection-menu');
    trigger.setAttribute('aria-expanded', 'false');
    trigger.setAttribute('aria-haspopup', 'true');
    trigger.addEventListener('click', () => openFromSelection('button'));
    content.prepend(trigger);

    status = document.createElement('p');
    status.className = 'ebook-selection-status';
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    trigger.after(status);

    menu = document.createElement('div');
    menu.id = 'ebook-selection-menu';
    menu.className = 'ebook-selection-menu';
    menu.setAttribute('role', 'group');
    menu.setAttribute('aria-label', 'Thao tác với văn bản đã chọn');
    menu.hidden = true;
    actionList = document.createElement('div');
    actionList.className = 'ebook-selection-actions';
    actions.forEach(addActionButton);
    menu.appendChild(actionList);
    document.body.appendChild(menu);

    content.addEventListener('contextmenu', event => {
      const snapshot = capture();
      if (!snapshot || !pointOnSelection(event.clientX, event.clientY, snapshot.rects)) return;
      event.preventDefault();
      show(snapshot, 'pointer', event.clientX, event.clientY);
    });
    document.addEventListener('keydown', event => {
      if (!menu.hidden && event.key === 'Escape') {
        event.preventDefault();
        close();
        return;
      }
      if ((event.key === 'F10' && event.shiftKey) || event.key === 'ContextMenu') {
        if (!content.contains(document.activeElement) && document.activeElement !== document.body) return;
        if (openFromSelection('keyboard')) event.preventDefault();
      }
    });
    document.addEventListener('pointerdown', event => {
      if (!menu.hidden && !menu.contains(event.target) && event.target !== trigger) close(false);
    });
    document.addEventListener('selectionchange', () => {
      if (!menu.hidden || !window.matchMedia('(pointer: coarse)').matches) return;
      window.clearTimeout(mobileTimer);
      mobileTimer = window.setTimeout(() => {
        const snapshot = capture();
        if (snapshot && !sameRange(snapshot, dismissedRange)) show(snapshot, 'touch');
      }, 180);
    });
    window.addEventListener('resize', schedulePosition);
    window.addEventListener('scroll', schedulePosition, { passive: true });
    window.visualViewport?.addEventListener('resize', schedulePosition);
    window.visualViewport?.addEventListener('scroll', schedulePosition, { passive: true });
    initialized = true;
    return true;
  }

  registerAction({ id: 'copy', label: 'Sao chép', run: copyText });
  registerAction({
    id: 'google',
    label: 'Giải thích trên Google',
    run: text => externalSearch('https://www.google.com/search', 'q', `${text} giải thích`)
  });
  registerAction({
    id: 'youtube',
    label: 'Video liên quan trên YouTube',
    run: text => externalSearch('https://www.youtube.com/results', 'search_query', `${text} điện tử`)
  });
  registerAction({
    id: 'related',
    label: 'Bài học liên quan',
    run: text => window.EbookSearch?.open(text)
  });

  window.EbookSelectionActions = { init, registerAction, close, openFromSelection };
})();
