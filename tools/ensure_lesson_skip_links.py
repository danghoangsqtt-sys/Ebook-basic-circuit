"""Add/check keyboard skip links for 56 foundation + published advanced pages."""

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = '<a class="skip-link" href="#lesson-main">Đi tới nội dung chính</a>'
MAIN_OLD = '<main class="main-content">'
MAIN_NEW = '<main class="main-content" id="lesson-main" tabindex="-1">'


def pages():
    return [*sorted(ROOT.glob("week*/day*.html")), *sorted((ROOT / "advanced").glob("*.html"))]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    selected = pages()
    if len(selected) != 89:  # 56 foundation + 32 lessons + path
        raise SystemExit(f"Expected 89 pages, found {len(selected)}")
    changed = 0
    for path in selected:
        content = path.read_text(encoding="utf-8")
        if content.count("<body>") != 1 or content.count("main-content") < 1:
            raise SystemExit(f"Unexpected HTML shell: {path}")
        if LINK not in content or MAIN_NEW not in content:
            if args.check:
                raise SystemExit(f"Missing skip link/main target: {path}")
            if LINK not in content:
                content = content.replace("<body>", f"<body>{LINK}", 1)
            if MAIN_NEW not in content:
                if MAIN_OLD not in content:
                    raise SystemExit(f"Missing main target: {path}")
                content = content.replace(MAIN_OLD, MAIN_NEW, 1)
            path.write_text(content, encoding="utf-8", newline="\n")
            changed += 1
    print(f"Skip links: {len(selected)} pages PASS; changed {changed}")


if __name__ == "__main__":
    main()
