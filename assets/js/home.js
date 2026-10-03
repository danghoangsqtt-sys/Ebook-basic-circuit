/* Trang chủ dùng cùng dữ liệu mục lục với thanh điều hướng trong bài học. */
(function () {
  'use strict';

  const roadmap = document.getElementById('week-roadmap');
  const catalog = document.getElementById('full-catalog');
  if (!roadmap || !catalog || typeof CURRICULUM === 'undefined') return;

  const lessonPath = (file) => {
    const path = String(file || '').replace(/^\.\.\//, '');
    return /^(?:week[1-8]\/day\d{2}|advanced\/a\d{2})\.html$/.test(path) ? path : null;
  };

  roadmap.replaceChildren();
  catalog.replaceChildren();

  CURRICULUM.weeks.forEach((week, index) => {
    const lessons = week.lessons.filter((lesson) => lessonPath(lesson.file));
    if (!lessons.length) return;

    const card = document.createElement('article');
    const label = document.createElement('small');
    label.textContent = week.label.toUpperCase();
    const title = document.createElement('h3');
    title.textContent = week.title;
    const count = document.createElement('p');
    count.textContent = lessons[0].number
      ? `${lessons[0].number}–${lessons[lessons.length - 1].number} · ${lessons.length} bài học`
      : `Bài ${lessons[0].day}–${lessons[lessons.length - 1].day} · ${lessons.length} bài học`;
    const weekLink = document.createElement('a');
    weekLink.href = `#catalog-week-${index + 1}`;
    weekLink.textContent = `Xem bài học ${week.label.toLowerCase()} →`;
    card.append(label, title, count, weekLink);
    roadmap.appendChild(card);

    const group = document.createElement('details');
    group.id = `catalog-week-${index + 1}`;
    const heading = document.createElement('summary');
    heading.textContent = `${week.label} · ${week.title}`;
    const links = document.createElement('div');
    links.className = 'catalog-links';
    lessons.forEach((lesson) => {
      const link = document.createElement('a');
      link.href = lessonPath(lesson.file);
      link.textContent = `${lesson.number || `Bài ${lesson.day}`} · ${lesson.title}`;
      links.appendChild(link);
    });
    group.append(heading, links);
    catalog.appendChild(group);
  });

  // Mở đúng tuần khi người đọc đi từ thẻ lộ trình đến mục lục.
  roadmap.addEventListener('click', (event) => {
    const link = event.target.closest('a[href^="#catalog-week-"]');
    if (!link) return;
    const group = document.querySelector(link.getAttribute('href'));
    if (group) group.open = true;
  });

  const mobileNav = document.querySelector('.mobile-nav');
  if (mobileNav) {
    mobileNav.addEventListener('click', (event) => {
      if (event.target.closest('nav a')) mobileNav.open = false;
    });
    mobileNav.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        mobileNav.open = false;
        mobileNav.querySelector('summary').focus();
      }
    });
  }
}());
