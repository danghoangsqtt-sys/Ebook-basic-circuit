/**
 * sidebar-data.js — Dữ liệu navigation cho toàn bộ giáo trình 56 bài
 * Được include trong mỗi bài để render sidebar nhất quán
 */

const CURRICULUM = {
  weeks: [
    {
      id: 'week1',
      label: 'Tuần 1',
      title: 'Điện học cơ bản',
      color: '#f59e0b',
      lessons: [
        { day: 1, title: 'Điện áp, dòng điện & GND', file: '../week1/day01.html' },
        { day: 2, title: 'Breadboard & Multimeter', file: '../week1/day02.html' },
        { day: 3, title: 'Điện trở & mã màu', file: '../week1/day03.html' },
        { day: 4, title: 'LED & điện trở hạn dòng', file: '../week1/day04.html' },
        { day: 5, title: 'Mạch nối tiếp & song song', file: '../week1/day05.html' },
        { day: 6, title: 'Cầu chia áp, KVL & KCL', file: '../week1/day06.html' },
        { day: 7, title: 'Ôn tập & Mini Project LED', file: '../week1/day07.html' },
      ]
    },
    {
      id: 'week2',
      label: 'Tuần 2',
      title: 'Tụ điện, Diode & Nguồn',
      color: '#f97316',
      lessons: [
        { day: 8,  title: 'Tụ điện & điện dung', file: '../week2/day08.html' },
        { day: 9,  title: 'Mạch RC nạp/xả', file: '../week2/day09.html' },
        { day: 10, title: 'Diode & PN junction', file: '../week2/day10.html' },
        { day: 11, title: 'Diode bảo vệ & flyback', file: '../week2/day11.html' },
        { day: 12, title: 'Chỉnh lưu & cầu diode', file: '../week2/day12.html' },
        { day: 13, title: 'Linear regulator 7805', file: '../week2/day13.html' },
        { day: 14, title: 'Project nguồn DC', file: '../week2/day14.html' },
      ]
    },
    {
      id: 'week3',
      label: 'Tuần 3',
      title: 'Transistor BJT & MOSFET',
      color: '#a855f7',
      lessons: [
        { day: 15, title: 'Transistor NPN/PNP', file: '../week3/day15.html' },
        { day: 16, title: 'Base, Collector, Emitter', file: '../week3/day16.html' },
        { day: 17, title: 'BJT làm switch', file: '../week3/day17.html' },
        { day: 18, title: 'Tính base resistor & saturation', file: '../week3/day18.html' },
        { day: 19, title: 'Relay driver + flyback diode', file: '../week3/day19.html' },
        { day: 20, title: 'LDR + BJT mạch tự động', file: '../week3/day20.html' },
        { day: 21, title: 'Project đèn tự động khi tối', file: '../week3/day21.html' },
      ]
    },
    {
      id: 'week4',
      label: 'Tuần 4',
      title: 'MCU & Giao tiếp số',
      color: '#3b82f6',
      lessons: [
        { day: 22, title: 'MOSFET & MOSFET switch', file: '../week4/day22.html' },
        { day: 23, title: 'VGS(th), RDS(on) & datasheet', file: '../week4/day23.html' },
        { day: 24, title: 'UART — Giao tiếp nối tiếp', file: '../week4/day24.html' },
        { day: 25, title: 'I2C — Bus 2 dây đa thiết bị', file: '../week4/day25.html' },
        { day: 26, title: 'SPI — Giao tiếp tốc độ cao', file: '../week4/day26.html' },
        { day: 27, title: 'ADC/DAC — Tín hiệu tương tự', file: '../week4/day27.html' },
        { day: 28, title: 'Ôn tập Tuần 4', file: '../week4/day28.html' },
      ]
    },
    {
      id: 'week5',
      label: 'Tuần 5',
      title: 'Mô phỏng, Nguồn & PCB',
      color: '#10b981',
      lessons: [
        { day: 29, title: 'Mô phỏng Falstad & LTSpice', file: '../week5/day29.html' },
        { day: 30, title: 'Oscilloscope thực hành', file: '../week5/day30.html' },
        { day: 31, title: 'Bộ lọc RC — LPF, HPF, BPF', file: '../week5/day31.html' },
        { day: 32, title: 'Buck/Boost converter', file: '../week5/day32.html' },
        { day: 33, title: 'Nhập môn KiCad PCB', file: '../week5/day33.html' },
        { day: 34, title: 'Hàn SMD & Kiểm Tra PCB', file: '../week5/day34.html' },
        { day: 35, title: 'Ôn tập Tuần 5 & Mini Project PCB', file: '../week5/day35.html' },
      ]
    },
    {
      id: 'week6',
      label: 'Tuần 6',
      title: 'Dự án thực tế',
      color: '#06b6d4',
      lessons: [
        { day: 36, title: 'RTC DS3231 — Đồng hồ thực', file: '../week6/day36.html' },
        { day: 37, title: 'WiFi & IoT — ESP32 Web Server', file: '../week6/day37.html' },
        { day: 38, title: 'Stepper Motor & Servo', file: '../week6/day38.html' },
        { day: 39, title: 'H-Bridge & Motor DC 2 chiều', file: '../week6/day39.html' },
        { day: 40, title: 'HC-SR04 & Cảm Biến Khoảng Cách', file: '../week6/day40.html' },
        { day: 41, title: 'Pin LiPo & BMS', file: '../week6/day41.html' },
        { day: 42, title: 'Ôn tập Tuần 6 & Capstone Robot', file: '../week6/day42.html' },
      ]
    },
    {
      id: 'week7',
      label: 'Tuần 7',
      title: 'Đồ án kỹ thuật',
      color: '#6366f1',
      lessons: [
        { day: 43, title: 'Đồ Án — Lên Ý Tưởng & SRS', file: '../week7/day43.html' },
        { day: 44, title: 'Đồ Án — Schematic & Firmware Khung', file: '../week7/day44.html' },
        { day: 45, title: 'Đồ Án — Phát Triển Firmware & Debug', file: '../week7/day45.html' },
        { day: 46, title: 'Đồ Án — PCB Layout & Assembly', file: '../week7/day46.html' },
        { day: 47, title: 'Đồ Án — Integration Test', file: '../week7/day47.html' },
        { day: 48, title: 'Viết Tài Liệu Kỹ Thuật', file: '../week7/day48.html' },
        { day: 49, title: 'Ôn Tập Tuần 7 & Chuẩn Bị Demo', file: '../week7/day49.html' },
      ]
    },
    {
      id: 'week8',
      label: 'Tuần 8',
      title: 'Nâng cao & Tổng kết',
      color: '#ef4444',
      lessons: [
        { day: 50, title: 'Demo Đồ Án & Tổng Kết', file: '../week8/day50.html' },
        { day: 51, title: 'PID Control — Điều Khiển Vòng Kín', file: '../week8/day51.html' },
        { day: 52, title: 'FreeRTOS — Đa Nhiệm Thực Thời', file: '../week8/day52.html' },
        { day: 53, title: 'BLE — Bluetooth Low Energy', file: '../week8/day53.html' },
        { day: 54, title: 'EMC & Thiết Kế Chống Nhiễu', file: '../week8/day54.html' },
        { day: 55, title: 'Con Đường Tiếp Theo', file: '../week8/day55.html' },
        { day: 56, title: '🎓 Tổng Kết 8 Tuần — Chúc Mừng!', file: '../week8/day56.html' },
      ]
    }
  ]
};

/**
 * Render sidebar vào element có class .sidebar
 * @param {string} activeFile - tên file hiện tại, vd: 'day01.html'
 * @param {string} rootPrefix - tiền tố path đến root, vd: '../' hoặc './'
 */
function renderSidebar(activeFile, rootPrefix = '../') {
  const sidebar = document.querySelector('.sidebar');
  if (!sidebar) return;

  const progress = (() => {
    try { return JSON.parse(localStorage.getItem('lessonProgress') || '{}'); }
    catch { return {}; }
  })();

  let html = '';
  CURRICULUM.weeks.forEach(week => {
    html += `
    <div class="sidebar-section">
      <button class="sidebar-week-header" type="button" data-week="${week.id}"
        aria-controls="${week.id}-lessons" aria-expanded="true"
        aria-label="${week.label}: ${week.title}">
        <div class="week-badge">${week.label.replace('Tuần ','')}</div>
        <span class="week-label">${week.title}</span>
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </button>
      <div class="sidebar-lessons" id="${week.id}-lessons">`;

    week.lessons.forEach(lesson => {
      const lessonId = `day${lesson.day}`;
      const isActive = lesson.file.includes(activeFile);
      const isDone = progress[lessonId];
      const classes = ['sidebar-lesson', isActive ? 'active' : '', isDone && !isActive ? 'completed' : ''].filter(Boolean).join(' ');
      html += `
        <a class="${classes}" href="${lesson.file}"${isActive ? ' aria-current="page"' : ''}>
          <span class="lesson-num">N${lesson.day}</span>
          <span>${lesson.title}</span>
          <span class="lesson-check">${isDone ? '✓' : ''}</span>
        </a>`;
    });

    html += `</div></div>`;
  });

  sidebar.innerHTML = html;
}
