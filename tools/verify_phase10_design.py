"""Independent arithmetic and artifact gate for the four-stage design example."""

import csv
import importlib.util
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def main():
    # Check the physical-unit arithmetic without importing the authoring model.
    assert abs((0.5 + 0.01 * 20) - 0.70) < 1e-12
    assert abs((0.5 + 0.01 * 40) - 0.90) < 1e-12
    assert abs(3.3 * 50e-6 * 1000 - 0.165) < 1e-12  # mW
    code_25 = round(0.75 / 3.3 * 65535)
    assert code_25 == 14894
    decoded_25 = (code_25 * 3.3 / 65535 - 0.5) / 0.01
    assert abs(decoded_25 - 24.9984) < 0.0001
    quant_half_c = 3.3 / 4096 / 2 / 0.01
    assert abs(quant_half_c - 0.04028) < 0.0001
    vref_component_c = 0.75 * 0.01 / 0.01
    assert abs(vref_component_c - 0.75) < 1e-12

    spec = importlib.util.spec_from_file_location("phase10_model", ROOT / "tools/simulate_phase10_design.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = module.scenarios()
    assert len(rows) == 10
    baseline_25 = next(r for r in rows if r["stimulus_c"] == 25 and r["actual_reference_v_assumed"] == 3.3)
    shifted_25 = next(r for r in rows if r["stimulus_c"] == 25 and r["actual_reference_v_assumed"] == 3.333)
    assert baseline_25["adc_u16"] == 14894
    assert -0.76 < shifted_25["error_c"] < -0.73

    matrix = list(csv.DictReader((ROOT / "docs/curriculum/advanced-coverage-matrix.csv").open(encoding="utf-8", newline="")))
    ids = [row["id"] for row in matrix]
    assert ids == [f"A{number:02}" for number in range(1, 33)]
    for number in range(29, 33):
        ident = f"a{number:02}"
        html = (ROOT / "advanced" / f"{ident}.html").read_text(encoding="utf-8")
        svg = ElementTree.parse(ROOT / "assets/images/advanced" / f"{ident}.svg").getroot()
        assert svg.tag.endswith("svg")
        assert "docs/projects/pico-tmp36-design.md" in html
        assert "Bài tập độc lập" in html and "answer-content" in html
    document = (ROOT / "docs/projects/pico-tmp36-design.md").read_text(encoding="utf-8")
    for stage in ("A29", "A30", "A31", "A32"):
        assert f"## {stage}" in document
    for gate in ("BOM", "Schematic", "Mô phỏng", "Sai khác", "ERC", "DRC", "pending"):
        assert gate.lower() in document.lower()
    print("Phase 10 design: four pages/artifacts, units and staged evidence PASS")


if __name__ == "__main__":
    main()
