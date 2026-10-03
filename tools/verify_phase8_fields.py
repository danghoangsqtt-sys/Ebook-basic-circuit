"""Check the ideal A15/A16 field examples independently of their prose.

These calculations assume uniform fields and fixed geometry. No FEM, EMC, or
physical measurement is performed. Run: python tools/verify_phase8_fields.py
"""

import json
from math import isclose


EPSILON_0_F_PER_M = 8.854187817e-12


def parallel_plate(area_m2, spacing_m, voltage_v):
    capacitance_f = EPSILON_0_F_PER_M * area_m2 / spacing_m
    field_v_per_m = voltage_v / spacing_m
    energy_j = 0.5 * capacitance_f * voltage_v**2
    return capacitance_f, field_v_per_m, energy_j


def emf_magnitude(length_m, return_spacing_m, db_dt_t_per_s, cosine_to_normal=1.0):
    area_m2 = length_m * return_spacing_m
    return area_m2, abs(area_m2 * db_dt_t_per_s * cosine_to_normal)


def near(value, expected, rel_tol=0.0001):
    assert isclose(value, expected, rel_tol=rel_tol), (value, expected)


def main():
    electric = {}
    for spacing_mm in (0.5, 1.0, 2.0):
        c, e, u = parallel_plate(0.01, spacing_mm * 1e-3, 5.0)
        electric[str(spacing_mm)] = {
            "C_pF": c * 1e12,
            "E_kV_per_m": e * 1e-3,
            "U_nJ": u * 1e9,
        }
    near(electric["1.0"]["C_pF"], 88.54187817)
    near(electric["1.0"]["E_kV_per_m"], 5.0)
    near(electric["1.0"]["U_nJ"], 1.106773477)
    near(electric["2.0"]["C_pF"], 44.270939085)
    near(electric["2.0"]["U_nJ"], 0.5533867385)
    near(electric["0.5"]["U_nJ"], 2 * electric["1.0"]["U_nJ"])

    magnetic = {}
    for spacing_mm in (10.0, 2.0):
        area, emf = emf_magnitude(0.100, spacing_mm * 1e-3, 0.1)
        magnetic[str(spacing_mm)] = {"area_m2": area, "emf_uV": emf * 1e6}
    near(magnetic["10.0"]["emf_uV"], 100)
    near(magnetic["2.0"]["emf_uV"], 20)
    exercise_area, exercise_emf = emf_magnitude(0.050, 0.004, 0.2)
    near(exercise_area, 0.0002)
    near(exercise_emf * 1e6, 40)
    _, perpendicular_to_normal_emf = emf_magnitude(0.100, 0.010, 0.1, 0.0)
    near(perpendicular_to_normal_emf, 0.0)
    magnetic["exercise"] = {"area_m2": exercise_area, "emf_uV": exercise_emf * 1e6}
    magnetic["field_90deg_to_normal_emf_uV"] = perpendicular_to_normal_emf * 1e6
    print(json.dumps({"A15": electric, "A16": magnetic}, indent=2))


if __name__ == "__main__":
    main()
