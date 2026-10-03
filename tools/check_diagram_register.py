"""Verify current evidence locations for all 80 Phase 7 diagram IDs.

--refresh updates line references and records the chosen presentation. It does
not certify electrical correctness or hardware safety.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs/curriculum/diagram-register.csv"
CLAIMS = ROOT / "docs/curriculum/technical-claims.csv"
SPECIAL_SVG = {
    "D01-1": "d01-aa-series.svg",
    "D01-2": "d01-current-loop.svg",
    "D01-3": "d01-ground-reference.svg",
    "D01-4": "d01-ac-dc-wave.svg",
    "D02-1": "d02-breadboard-connectivity.svg",
    "D03-1": "d03-resistor-symbols.svg",
}
HTML_IDS = {"D03-2", "D03-3", "D10-1", "D33-1", "D43-1", "D44-1",
            "D45-1", "D46-1", "D53-1", "D55-1"}
TEXT_CLAIM_MARKERS = {
    "C006": "Các bài thực hành cơ bản dùng nguồn DC điện áp thấp",
    "C007": "Không thực hành trực tiếp với điện lưới",
    "C010": "Nét gấp khúc và hình chữ nhật",
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    with REGISTER.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)
    if fields is None or len(rows) != 80 or len({row["id"] for row in rows}) != 80:
        raise SystemExit("Register must contain 80 unique IDs")
    errors = []
    for row in rows:
        path = ROOT / row["path"]
        if not path.is_file():
            errors.append(f"{row['id']}: missing page {path}")
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        diagram_id = row["id"]
        if diagram_id in HTML_IDS:
            marker = f'id="diagram-{diagram_id.lower()}"'
            content = "HTML anchor " + marker
            action = "converted_accessible_html"
        else:
            asset = SPECIAL_SVG.get(diagram_id, diagram_id.lower() + ".svg")
            marker = f'src="../assets/images/lessons/{asset}"'
            content = "SVG " + asset
            action = "redrawn_svg_with_transcript"
            if not (ROOT / "assets/images/lessons" / asset).is_file():
                errors.append(f"{diagram_id}: missing SVG {asset}")
            html = "\n".join(lines)
            image_at = html.find(marker)
            if image_at >= 0:
                figure_start = html.rfind("<figure", 0, image_at)
                figure_end = html.find("</figure>", image_at)
                if figure_start < 0 or figure_end < 0:
                    errors.append(f"{diagram_id}: image has no figure wrapper")
                else:
                    figure_html = html[figure_start:figure_end]
                    if f'href="../assets/images/lessons/{asset}"' not in figure_html:
                        errors.append(f"{diagram_id}: missing full-size image link")
                    if "<details" not in figure_html and "summary-transcript" not in html[figure_end:figure_end + 600]:
                        errors.append(f"{diagram_id}: missing nearby text transcript")
        positions = [i for i, line in enumerate(lines, 1) if marker in line]
        if len(positions) != 1:
            errors.append(f"{diagram_id}: expected marker once, found {len(positions)}")
            continue
        line = positions[0]
        if args.refresh:
            row["line"] = str(line)
            row["current_content"] = content
            row["current_source_evidence"] = f"{row['path']}:{line}"
            row["planned_action"] = action
            if row["visual_review_status"] == "open_visual_review":
                row["visual_review_status"] = "pending_mobile_and_content_review"
        elif row["line"] != str(line) or row["current_content"] != content or row["planned_action"] != action:
            errors.append(f"{diagram_id}: stale register row, current location {row['path']}:{line}")
    diagrams = {row["id"]: row for row in rows}
    with CLAIMS.open(encoding="utf-8", newline="") as handle:
        claim_reader = csv.DictReader(handle)
        claim_fields = claim_reader.fieldnames
        claims = list(claim_reader)
    if claim_fields is None or len(claims) != 17 or len({claim["claim_id"] for claim in claims}) != 17:
        errors.append("Technical claims must contain 17 unique IDs")
    for claim in claims:
        diagram = diagrams.get(claim["diagram_id"])
        if diagram is None:
            errors.append(f"{claim['claim_id']}: unknown diagram {claim['diagram_id']}")
            continue
        if claim["path"] != diagram["path"]:
            errors.append(f"{claim['claim_id']}: path differs from diagram")
            continue
        source_url = claim["source_url"]
        if source_url and not source_url.startswith("https://"):
            errors.append(f"{claim['claim_id']}: source must use HTTPS")
        lines = (ROOT / claim["path"]).read_text(encoding="utf-8").splitlines()
        if claim["claim_id"] in TEXT_CLAIM_MARKERS:
            marker = TEXT_CLAIM_MARKERS[claim["claim_id"]]
            positions = [i for i, line in enumerate(lines, 1) if marker in line]
            if len(positions) != 1:
                errors.append(f"{claim['claim_id']}: text marker missing or duplicated")
                continue
            expected_line = positions[0]
        else:
            expected_line = int(diagram["line"])
        if args.refresh:
            claim["line"] = str(expected_line)
        elif claim["line"] != str(expected_line):
            errors.append(f"{claim['claim_id']}: stale claim location, current {claim['path']}:{expected_line}")
    if errors:
        print("\n".join(errors))
        return 1
    if args.refresh:
        with REGISTER.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        with CLAIMS.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=claim_fields)
            writer.writeheader()
            writer.writerows(claims)
        print("Refreshed 80 diagram decisions and 17 claim locations")
    else:
        print("Diagram register current: 80 unique IDs, 70 SVGs, 10 HTML references; 17 claim locations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
