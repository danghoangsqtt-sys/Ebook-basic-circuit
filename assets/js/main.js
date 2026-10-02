/**
 * Giáo trình Tự học Điện tử Thực hành
 * Main JavaScript — Navigation, Progress, Interactive Elements
 */

// ═══════════════════════════════════════
// SIDEBAR NAVIGATION
// ═══════════════════════════════════════

class SidebarController {
  constructor() {
    this.sidebar = document.querySelector('.sidebar');
    this.menuBtn = document.querySelector('.btn-menu');
    this.overlay = null;
    this.weekHeaders = document.querySelectorAll('.sidebar-week-header');
    this.init();
  }

  init() {
    if (this.menuBtn && this.sidebar) {
      if (!this.sidebar.id) this.sidebar.id = 'sidebar';
      this.sidebar.setAttribute('aria-label', 'Danh sách bài học');
      this.menuBtn.setAttribute('aria-controls', this.sidebar.id);
      this.menuBtn.setAttribute('aria-expanded', 'false');
      this.menuBtn.setAttribute('aria-label', 'Mở danh sách bài học');
      this.menuBtn.addEventListener('click', () => this.toggleMobile());
      this.createOverlay();
      document.addEventListener('keydown', event => this.onKeydown(event));
      window.addEventListener('resize', () => {
        if (window.innerWidth > 768 && this.sidebar.classList.contains('open')) {
          this.closeMobile(false);
        }
      });
    }
    this.weekHeaders.forEach(header => {
      header.addEventListener('click', () => this.toggleWeek(header));
    });
    this.restoreWeekStates();
    this.highlightActive();
  }

  toggleMobile() {
    if (this.sidebar.classList.contains('open')) this.closeMobile();
    else this.openMobile();
  }

  openMobile() {
    this.sidebar.classList.add('open');
    this.overlay.hidden = false;
    document.body.classList.add('sidebar-is-open');
    this.menuBtn.setAttribute('aria-expanded', 'true');
    this.menuBtn.setAttribute('aria-label', 'Đóng danh sách bài học');
    (this.sidebar.querySelector('.sidebar-lesson.active') ||
      this.sidebar.querySelector('.sidebar-week-header'))?.focus();
  }

  closeMobile(returnFocus = true) {
    this.sidebar.classList.remove('open');
    this.overlay.hidden = true;
    document.body.classList.remove('sidebar-is-open');
    this.menuBtn.setAttribute('aria-expanded', 'false');
    this.menuBtn.setAttribute('aria-label', 'Mở danh sách bài học');
    if (returnFocus) this.menuBtn.focus();
  }

  onKeydown(event) {
    if (!this.sidebar.classList.contains('open')) return;
    if (event.key === 'Escape') {
      event.preventDefault();
      this.closeMobile();
    } else if (event.key === 'Tab') {
      const items = [...this.sidebar.querySelectorAll('button, a[href]')]
        .filter(item => item.getClientRects().length > 0);
      if (!items.length) return;
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  }

  createOverlay() {
    this.overlay = document.createElement('div');
    this.overlay.className = 'sidebar-overlay';
    this.overlay.hidden = true;
    this.overlay.addEventListener('click', () => this.closeMobile());
    document.body.appendChild(this.overlay);
  }

  toggleWeek(header) {
    const weekId = header.dataset.week;
    const lessonsEl = header.nextElementSibling;
    if (!lessonsEl) return;
    const expanded = header.getAttribute('aria-expanded') === 'true';
    this.setWeekExpanded(header, !expanded);

    const states = this.getWeekStates();
    states[weekId] = !expanded;
    try { localStorage.setItem('weekStates', JSON.stringify(states)); }
    catch { /* Storage may be disabled; the menu still works. */ }
  }

  setWeekExpanded(header, expanded) {
    const lessonsEl = header.nextElementSibling;
    if (!lessonsEl) return;
    header.classList.toggle('collapsed', !expanded);
    header.setAttribute('aria-expanded', String(expanded));
    lessonsEl.hidden = !expanded;
  }

  getWeekStates() {
    try { return JSON.parse(localStorage.getItem('weekStates') || '{}'); }
    catch { return {}; }
  }

  restoreWeekStates() {
    const states = this.getWeekStates();
    this.weekHeaders.forEach(header => {
      const weekId = header.dataset.week;
      this.setWeekExpanded(header, states[weekId] !== false);
    });
  }

  highlightActive() {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.sidebar-lesson').forEach(link => {
      const href = link.getAttribute('href')?.split('/').pop();
      if (href === currentPath) {
        link.classList.add('active');
        link.setAttribute('aria-current', 'page');
        // Ensure parent week is expanded
        const weekSection = link.closest('.sidebar-section');
        if (weekSection) {
          const header = weekSection.querySelector('.sidebar-week-header');
          const lessons = weekSection.querySelector('.sidebar-lessons');
          if (header && lessons) {
            this.setWeekExpanded(header, true);
          }
        }
        // Keep the active item visible inside the sidebar without moving the lesson page.
        setTimeout(() => {
          const top = link.offsetTop - this.sidebar.clientHeight / 2;
          this.sidebar.scrollTop = Math.max(0, top);
        }, 100);
      }
    });
  }
}

// ═══════════════════════════════════════
// PROGRESS TRACKER
// ═══════════════════════════════════════

class ProgressTracker {
  constructor() {
    this.storageKey = 'lessonProgress';
    this.totalLessons = 56;
    this.init();
  }

  init() {
    this.updateProgressBar();
    this.markCurrentAsVisited();
    this.updateCheckmarks();
  }

  getProgress() {
    try { return JSON.parse(localStorage.getItem(this.storageKey) || '{}'); }
    catch { return {}; }
  }

  markLesson(lessonId, completed = true) {
    const progress = this.getProgress();
    progress[lessonId] = completed;
    localStorage.setItem(this.storageKey, JSON.stringify(progress));
    this.updateProgressBar();
    this.updateCheckmarks();
  }

  markCurrentAsVisited() {
    const lessonId = this.getCurrentLessonId();
    if (lessonId) {
      const progress = this.getProgress();
      if (!progress[lessonId]) {
        this.markLesson(lessonId, true);
      }
    }
  }

  getCurrentLessonId() {
    const path = window.location.pathname;
    const match = path.match(/day(\d+)\.html/);
    return match ? `day${match[1]}` : null;
  }

  updateProgressBar() {
    const progress = this.getProgress();
    const completed = Object.values(progress).filter(Boolean).length;
    const percentage = Math.round((completed / this.totalLessons) * 100);

    const fill = document.querySelector('.progress-bar-fill');
    const label = document.querySelector('.progress-label');
    if (fill) fill.style.width = percentage + '%';
    if (label) label.textContent = `${completed}/${this.totalLessons} bài`;
  }

  updateCheckmarks() {
    const progress = this.getProgress();
    document.querySelectorAll('.sidebar-lesson').forEach(link => {
      const href = link.getAttribute('href') || '';
      const match = href.match(/day(\d+)\.html/);
      if (match) {
        const lessonId = `day${match[1]}`;
        const check = link.querySelector('.lesson-check');
        if (check) {
          check.textContent = progress[lessonId] ? '✓' : '';
          check.style.color = 'var(--clr-success)';
        }
        if (progress[lessonId] && !link.classList.contains('active')) {
          link.classList.add('completed');
        }
      }
    });
  }
}

// ═══════════════════════════════════════
// CHECKLIST PERSISTENCE
// ═══════════════════════════════════════

class ChecklistManager {
  constructor() {
    this.storageKey = `checklist_${window.location.pathname}`;
    this.init();
  }

  init() {
    const checkboxes = document.querySelectorAll('.checklist-item input[type="checkbox"]');
    if (!checkboxes.length) return;

    const saved = this.getSaved();
    checkboxes.forEach((cb, i) => {
      if (saved[i]) cb.checked = true;
      cb.addEventListener('change', () => this.save());
    });
  }

  getSaved() {
    try { return JSON.parse(localStorage.getItem(this.storageKey) || '{}'); }
    catch { return {}; }
  }

  save() {
    const checkboxes = document.querySelectorAll('.checklist-item input[type="checkbox"]');
    const data = {};
    checkboxes.forEach((cb, i) => { data[i] = cb.checked; });
    localStorage.setItem(this.storageKey, JSON.stringify(data));
  }
}

// ═══════════════════════════════════════
// ANSWER TOGGLE
// ═══════════════════════════════════════

function initAnswerToggles() {
  document.querySelectorAll('.answer-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const content = btn.nextElementSibling;
      if (!content) return;
      const isVisible = content.classList.contains('visible');
      content.classList.toggle('visible', !isVisible);
      btn.textContent = isVisible ? '👁 Xem đáp án' : '🙈 Ẩn đáp án';
    });
  });
}

// ═══════════════════════════════════════
// SMOOTH SCROLL FOR ANCHOR LINKS
// ═══════════════════════════════════════

function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const headerHeight = parseInt(getComputedStyle(document.documentElement)
          .getPropertyValue('--header-height')) || 60;
        const top = target.getBoundingClientRect().top + window.scrollY - headerHeight - 20;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });
}

// ═══════════════════════════════════════
// TABLE OF CONTENTS (auto-generate)
// ═══════════════════════════════════════

function buildTOC() {
  const tocEl = document.getElementById('auto-toc');
  if (!tocEl) return;

  const headings = document.querySelectorAll('.content-area h2, .content-area h3');
  if (!headings.length) return;

  const ul = document.createElement('ul');
  ul.style.cssText = 'list-style:none;padding:0;';

  headings.forEach((h, i) => {
    if (!h.id) h.id = `heading-${i}`;
    const li = document.createElement('li');
    li.style.cssText = `padding:4px 0 4px ${h.tagName === 'H3' ? '16px' : '0'};`;
    const a = document.createElement('a');
    a.href = `#${h.id}`;
    a.textContent = h.textContent;
    a.style.cssText = `
      font-size:${h.tagName === 'H3' ? '0.8rem' : '0.875rem'};
      color:var(--clr-text-muted);text-decoration:none;
      transition:color 0.15s;display:block;
    `;
    a.addEventListener('mouseover', () => a.style.color = 'var(--clr-text-secondary)');
    a.addEventListener('mouseout', () => a.style.color = 'var(--clr-text-muted)');
    li.appendChild(a);
    ul.appendChild(li);
  });

  tocEl.appendChild(ul);
}

// ═══════════════════════════════════════
// READING POSITION INDICATOR
// ═══════════════════════════════════════

function initReadingProgress() {
  const bar = document.createElement('div');
  bar.style.cssText = `
    position:fixed;top:var(--header-height,60px);left:0;height:2px;
    background:linear-gradient(90deg,var(--clr-accent),var(--clr-blue));
    z-index:1001;width:0;transition:width 0.1s linear;pointer-events:none;
  `;
  document.body.appendChild(bar);

  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = progress + '%';
  }, { passive: true });
}

// ═══════════════════════════════════════
// COPY CODE BUTTON
// ═══════════════════════════════════════

function initCopyButtons() {
  document.querySelectorAll('pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.textContent = 'Sao chép';
    btn.style.cssText = `
      position:absolute;top:8px;right:8px;padding:4px 10px;
      background:var(--clr-bg-elevated);border:1px solid var(--clr-border);
      color:var(--clr-text-muted);font-size:11px;border-radius:6px;
      cursor:pointer;font-family:var(--font-mono);transition:all 0.15s;
    `;
    btn.addEventListener('click', async () => {
      const code = pre.querySelector('code')?.textContent || pre.textContent;
      try {
        await navigator.clipboard.writeText(code);
        btn.textContent = '✓ Đã sao chép';
        btn.style.color = 'var(--clr-success)';
        setTimeout(() => { btn.textContent = 'Sao chép'; btn.style.color = ''; }, 2000);
      } catch {
        btn.textContent = 'Lỗi';
        setTimeout(() => { btn.textContent = 'Sao chép'; }, 2000);
      }
    });
    pre.style.position = 'relative';
    pre.appendChild(btn);
  });
}

// ═══════════════════════════════════════
// INIT
// ═══════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
  new SidebarController();
  new ProgressTracker();
  new ChecklistManager();
  initAnswerToggles();
  initSmoothScroll();
  buildTOC();
  initReadingProgress();
  initCopyButtons();
  new ThemeController();
  new FontSizeController();

  // Fade in content
  document.querySelector('.content-area')?.classList.add('animate-fade-in-up');
});

// ═══════════════════════════════════════
// THEME CONTROLLER — Dark / Light
// ═══════════════════════════════════════

class ThemeController {
  constructor() {
    this.htmlEl = document.documentElement;
    this.storageKey = 'ebook-theme';
    this.current = localStorage.getItem(this.storageKey) || 'dark';
    this.applyTheme(this.current);
    this.injectButton();
  }

  applyTheme(theme) {
    this.current = theme;
    if (theme === 'light') {
      this.htmlEl.setAttribute('data-theme', 'light');
    } else {
      this.htmlEl.removeAttribute('data-theme');
    }
    localStorage.setItem(this.storageKey, theme);
    if (this.btn) {
      this.btn.textContent = theme === 'dark' ? '☀️' : '🌙';
      this.btn.title = theme === 'dark' ? 'Chuyển sang giao diện sáng' : 'Chuyển sang giao diện tối';
    }
  }

  toggle() {
    this.applyTheme(this.current === 'dark' ? 'light' : 'dark');
  }

  injectButton() {
    const toolbar = this.ensureToolbar();
    this.btn = document.createElement('button');
    this.btn.className = 'a11y-btn a11y-btn-theme';
    this.btn.textContent = this.current === 'dark' ? '☀️' : '🌙';
    this.btn.title = this.current === 'dark' ? 'Chuyển sang giao diện sáng' : 'Chuyển sang giao diện tối';
    this.btn.setAttribute('aria-label', 'Chuyển đổi giao diện sáng/tối');
    this.btn.addEventListener('click', () => this.toggle());
    toolbar.appendChild(this.btn);
  }

  ensureToolbar() {
    let toolbar = document.querySelector('.a11y-toolbar');
    if (!toolbar) {
      toolbar = document.createElement('div');
      toolbar.className = 'a11y-toolbar';
      const header = document.querySelector('.site-header');
      if (header) header.appendChild(toolbar);
    }
    return toolbar;
  }
}

// ═══════════════════════════════════════
// FONT SIZE CONTROLLER
// ═══════════════════════════════════════

class FontSizeController {
  constructor() {
    this.storageKey = 'ebook-fontsize';
    this.sizes = [13, 15, 16, 18, 20]; // px steps
    this.labels = ['A₋', 'A', 'A', 'A⁺', 'A⁺⁺'];
    this.idx = parseInt(localStorage.getItem(this.storageKey) ?? '2', 10);
    this.applySize(this.idx);
    this.injectControls();
  }

  applySize(idx) {
    this.idx = Math.max(0, Math.min(this.sizes.length - 1, idx));
    document.documentElement.style.fontSize = this.sizes[this.idx] + 'px';
    localStorage.setItem(this.storageKey, this.idx);
    this.updateButtons();
  }

  updateButtons() {
    if (!this.btnDec || !this.btnInc) return;
    this.btnDec.disabled = this.idx <= 0;
    this.btnInc.disabled = this.idx >= this.sizes.length - 1;
    this.btnDec.style.opacity = this.idx <= 0 ? '0.4' : '';
    this.btnInc.style.opacity = this.idx >= this.sizes.length - 1 ? '0.4' : '';
  }

  injectControls() {
    const toolbar = this.ensureToolbar();

    // Divider
    const div = document.createElement('div');
    div.className = 'a11y-divider';
    toolbar.appendChild(div);

    // Decrease button
    this.btnDec = document.createElement('button');
    this.btnDec.className = 'a11y-btn a11y-btn-font a11y-btn-font-sm';
    this.btnDec.textContent = 'A−';
    this.btnDec.title = 'Giảm cỡ chữ';
    this.btnDec.setAttribute('aria-label', 'Giảm cỡ chữ');
    this.btnDec.addEventListener('click', () => this.applySize(this.idx - 1));
    toolbar.appendChild(this.btnDec);

    // Reset button
    this.btnReset = document.createElement('button');
    this.btnReset.className = 'a11y-btn a11y-btn-font a11y-btn-font-md';
    this.btnReset.textContent = 'A';
    this.btnReset.title = 'Cỡ chữ mặc định';
    this.btnReset.setAttribute('aria-label', 'Cỡ chữ mặc định');
    this.btnReset.addEventListener('click', () => this.applySize(2));
    toolbar.appendChild(this.btnReset);

    // Increase button
    this.btnInc = document.createElement('button');
    this.btnInc.className = 'a11y-btn a11y-btn-font a11y-btn-font-lg';
    this.btnInc.textContent = 'A+';
    this.btnInc.title = 'Tăng cỡ chữ';
    this.btnInc.setAttribute('aria-label', 'Tăng cỡ chữ');
    this.btnInc.addEventListener('click', () => this.applySize(this.idx + 1));
    toolbar.appendChild(this.btnInc);

    this.updateButtons();
  }

  ensureToolbar() {
    let toolbar = document.querySelector('.a11y-toolbar');
    if (!toolbar) {
      toolbar = document.createElement('div');
      toolbar.className = 'a11y-toolbar';
      const header = document.querySelector('.site-header');
      if (header) header.appendChild(toolbar);
    }
    return toolbar;
  }
}
