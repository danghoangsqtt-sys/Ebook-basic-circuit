"""Refresh only A28's next-lesson link after Phase 10 publication."""

import build_phase9_sensor_lessons as sensor

board = sensor.board
last = board.LESSONS[-1]
assert last["id"] == "a28"
(board.ROOT / "advanced/a28.html").write_text(
    board.render(last, len(board.LESSONS) - 1), encoding="utf-8"
)
print("A28 to A29 link refreshed")
