/**
 * sidebar-data.js — Dữ liệu navigation cho 56 bài nền và các bài chuyên sâu đã xuất bản
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
        { day: 1, title: 'Điện Áp, Dòng Điện, GND & Mạch Điện', file: '../week1/day01.html' },
        { day: 2, title: 'Breadboard & Multimeter — Hai Công Cụ Không Thể Thiếu', file: '../week1/day02.html' },
        { day: 3, title: 'Điện Trở & Mã Màu', file: '../week1/day03.html' },
        { day: 4, title: 'LED & Điện Trở Hạn Dòng', file: '../week1/day04.html' },
        { day: 5, title: 'Mạch Nối Tiếp & Song Song', file: '../week1/day05.html' },
        { day: 6, title: 'Cầu Chia Áp, KVL & KCL', file: '../week1/day06.html' },
        { day: 7, title: 'Ôn Tập Tuần 1 & Mini Project: Mạch LED Đa Màu', file: '../week1/day07.html' },
      ]
    },
    {
      id: 'week2',
      label: 'Tuần 2',
      title: 'Tụ điện, Diode & Nguồn',
      color: '#f97316',
      lessons: [
        { day: 8,  title: 'Tụ Điện & Điện Dung', file: '../week2/day08.html' },
        { day: 9,  title: 'Mạch RC — Nạp & Xả Tụ Điện', file: '../week2/day09.html' },
        { day: 10, title: 'Cuộn Cảm & Mạch RL', file: '../week2/day10.html' },
        { day: 11, title: 'Diode — Nguyên Lý & Ứng Dụng', file: '../week2/day11.html' },
        { day: 12, title: 'Diode Zener & Mạch Ổn Áp', file: '../week2/day12.html' },
        { day: 13, title: 'Nguồn DC & IC Ổn Áp Tuyến Tính', file: '../week2/day13.html' },
        { day: 14, title: 'Ôn Tập Tuần 2 & Mini Project: Mạch Nguồn DC Hoàn Chỉnh', file: '../week2/day14.html' },
      ]
    },
    {
      id: 'week3',
      label: 'Tuần 3',
      title: 'Transistor BJT & MOSFET',
      color: '#a855f7',
      lessons: [
        { day: 15, title: 'Transistor BJT — NPN & PNP', file: '../week3/day15.html' },
        { day: 16, title: 'Mạch Switch BJT — Điều Khiển Relay & Motor DC', file: '../week3/day16.html' },
        { day: 17, title: 'Mạch Khuếch Đại BJT — Common Emitter', file: '../week3/day17.html' },
        { day: 18, title: 'MOSFET — NMOS & PMOS', file: '../week3/day18.html' },
        { day: 19, title: 'PWM — Điều Rộng Xung & Điều Khiển Tốc Độ', file: '../week3/day19.html' },
        { day: 20, title: 'Op-Amp — Khuếch Đại Thuật Toán Cơ Bản', file: '../week3/day20.html' },
        { day: 21, title: 'Ôn Tập Tuần 3 & Mini Project: Mạch Báo Nhiệt Tự Động', file: '../week3/day21.html' },
      ]
    },
    {
      id: 'week4',
      label: 'Tuần 4',
      title: 'MCU & Giao tiếp số',
      color: '#3b82f6',
      lessons: [
        { day: 22, title: 'Giao Tiếp Số — UART Cơ Bản', file: '../week4/day22.html' },
        { day: 23, title: 'I2C — Giao Tiếp Đa Thiết Bị Trên 2 Dây', file: '../week4/day23.html' },
        { day: 24, title: 'SPI — Giao Tiếp Nối Tiếp Tốc Độ Cao', file: '../week4/day24.html' },
        { day: 25, title: 'ADC & DAC — Chuyển Đổi Tín Hiệu Analog ↔ Số', file: '../week4/day25.html' },
        { day: 26, title: 'Interrupt — Ngắt Phần Cứng & Timer', file: '../week4/day26.html' },
        { day: 27, title: 'Cảm Biến Số — DHT22, DS18B20 & PIR', file: '../week4/day27.html' },
        { day: 28, title: 'Ôn Tập Tuần 4 & Mini Project: Trạm Đo Môi Trường', file: '../week4/day28.html' },
      ]
    },
    {
      id: 'week5',
      label: 'Tuần 5',
      title: 'Mô phỏng, Nguồn & PCB',
      color: '#10b981',
      lessons: [
        { day: 29, title: 'Mô Phỏng Mạch — Falstad & LTSpice', file: '../week5/day29.html' },
        { day: 30, title: 'Oscilloscope — Đọc & Đo Dạng Sóng', file: '../week5/day30.html' },
        { day: 31, title: 'Bộ Lọc Tín Hiệu — Low Pass, High Pass, Band Pass', file: '../week5/day31.html' },
        { day: 32, title: 'Nguồn Switching — Buck, Boost, Buck-Boost', file: '../week5/day32.html' },
        { day: 33, title: 'Thiết Kế PCB — Nhập Môn KiCad', file: '../week5/day33.html' },
        { day: 34, title: 'Hàn SMD & Kiểm Tra PCB', file: '../week5/day34.html' },
        { day: 35, title: 'Ôn Tập Tuần 5 & Mini Project: PCB Buck Converter', file: '../week5/day35.html' },
      ]
    },
    {
      id: 'week6',
      label: 'Tuần 6',
      title: 'Dự án thực tế',
      color: '#06b6d4',
      lessons: [
        { day: 36, title: 'RTC DS3231 — Đồng Hồ Thời Gian Thực', file: '../week6/day36.html' },
        { day: 37, title: 'WiFi & IoT — ESP32 Web Server', file: '../week6/day37.html' },
        { day: 38, title: 'Stepper Motor & Servo — Điều Khiển Góc Chính Xác', file: '../week6/day38.html' },
        { day: 39, title: 'H-Bridge & Điều Khiển Motor DC 2 Chiều', file: '../week6/day39.html' },
        { day: 40, title: 'Cảm Biến Khoảng Cách — HC-SR04 & IR', file: '../week6/day40.html' },
        { day: 41, title: 'Pin LiPo & BMS — Quản Lý Nguồn Di Động', file: '../week6/day41.html' },
        { day: 42, title: 'Ôn Tập Tuần 6 & Capstone: Robot WiFi Tránh Vật Cản', file: '../week6/day42.html' },
      ]
    },
    {
      id: 'week7',
      label: 'Tuần 7',
      title: 'Đồ án kỹ thuật',
      color: '#6366f1',
      lessons: [
        { day: 43, title: 'Đồ Án — Lên Ý Tưởng & Thiết Kế Hệ Thống', file: '../week7/day43.html' },
        { day: 44, title: 'Đồ Án — Schematic & Firmware Khung', file: '../week7/day44.html' },
        { day: 45, title: 'Đồ Án — Phát Triển Firmware & Debug', file: '../week7/day45.html' },
        { day: 46, title: 'Đồ Án — PCB Layout & Assembly', file: '../week7/day46.html' },
        { day: 47, title: 'Đồ Án — Integration Test & Calibration', file: '../week7/day47.html' },
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
        { day: 50, title: 'Demo Đồ Án & Tổng Kết Giai Đoạn', file: '../week8/day50.html' },
        { day: 51, title: 'PID Control — Điều Khiển Vòng Kín', file: '../week8/day51.html' },
        { day: 52, title: 'FreeRTOS — Đa Nhiệm Thực Thời Trên ESP32', file: '../week8/day52.html' },
        { day: 53, title: 'BLE — Bluetooth Low Energy Với ESP32', file: '../week8/day53.html' },
        { day: 54, title: 'EMC & Thiết Kế PCB Chống Nhiễu', file: '../week8/day54.html' },
        { day: 55, title: 'Con Đường Tiếp Theo — Học Gì Sau Khóa Này?', file: '../week8/day55.html' },
        { day: 56, title: 'Chúc Mừng Hoàn Thành!', file: '../week8/day56.html' },
      ]
    },
    {
      id: 'advanced-phase8',
      label: 'Chuyên sâu',
      title: 'Linh kiện và mạch',
      badge: 'A',
      color: '#14b8a6',
      lessons: [
        { id: 'a01', number: 'A01', title: 'Họ Điện Trở Cố Định', file: '../advanced/a01.html' },
        { id: 'a02', number: 'A02', title: 'Điện Trở Chức Năng & Phép Đo', file: '../advanced/a02.html' },
        { id: 'a03', number: 'A03', title: 'Các Họ Tụ Điện', file: '../advanced/a03.html' },
        { id: 'a04', number: 'A04', title: 'Tụ Điện Trong Mạch Thực', file: '../advanced/a04.html' },
        { id: 'a05', number: 'A05', title: 'Các Họ Diode', file: '../advanced/a05.html' },
        { id: 'a06', number: 'A06', title: 'Cuộn Cảm, Biến Áp & Ferrite Bead', file: '../advanced/a06.html' },
        { id: 'a07', number: 'A07', title: 'Adapter, Bộ Ổn Áp & Pin', file: '../advanced/a07.html' },
        { id: 'a08', number: 'A08', title: 'Chọn Linh Kiện Bằng Datasheet', file: '../advanced/a08.html' },
        { id: 'a09', number: 'A09', title: 'Mô Hình Mạch DC & KCL/KVL', file: '../advanced/a09.html' },
        { id: 'a10', number: 'A10', title: 'Phương Pháp Nút & Vòng', file: '../advanced/a10.html' },
        { id: 'a11', number: 'A11', title: 'Chồng Chất & Nguồn Phụ Thuộc', file: '../advanced/a11.html' },
        { id: 'a12', number: 'A12', title: 'Thévenin & Norton', file: '../advanced/a12.html' },
        { id: 'a13', number: 'A13', title: 'Phân Tích Mạch RC/RL Quá Độ', file: '../advanced/a13.html' },
        { id: 'a14', number: 'A14', title: 'Mạch RLC & Cộng Hưởng', file: '../advanced/a14.html' },
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
        <div class="week-badge">${week.badge || week.label.replace('Tuần ','')}</div>
        <span class="week-label">${week.title}</span>
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </button>
      <div class="sidebar-lessons" id="${week.id}-lessons">`;

    week.lessons.forEach(lesson => {
      const lessonId = lesson.id || `day${String(lesson.day).padStart(2, '0')}`;
      const isActive = lesson.file.includes(activeFile);
      const isDone = progress[lessonId];
      const classes = ['sidebar-lesson', isActive ? 'active' : '', isDone && !isActive ? 'completed' : ''].filter(Boolean).join(' ');
      html += `
        <a class="${classes}" href="${lesson.file}"${isActive ? ' aria-current="page"' : ''}>
          <span class="lesson-num">${lesson.number || `N${lesson.day}`}</span>
          <span>${lesson.title}</span>
          <span class="lesson-check">${isDone ? '✓' : ''}</span>
        </a>`;
    });

    html += `</div></div>`;
  });

  sidebar.innerHTML = html;
}
