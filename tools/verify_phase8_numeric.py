"""Independently recompute the A09–A14 syllabus examples with circuit equations.

This checks ideal mathematical models only. It is not SPICE, ERC or a physical test.
Run: python tools/verify_phase8_numeric.py
"""

from fractions import Fraction as F
from math import exp, pi, sqrt
import json


def solve_resistor_network(unknowns, branches, fixed):
    """Solve nodal conductance equations for (node_a, node_b, ohms) branches."""
    n = len(unknowns)
    matrix = [[F(0) for _ in range(n + 1)] for _ in range(n)]
    loc = {node: i for i, node in enumerate(unknowns)}
    for a, b, ohms in branches:
        g = F(1, ohms)
        for node, neighbor in ((a, b), (b, a)):
            if node not in loc:
                continue
            row = matrix[loc[node]]
            row[loc[node]] += g
            if neighbor in loc:
                row[loc[neighbor]] -= g
            else:
                row[-1] += g * F(fixed[neighbor])
    for col in range(n):
        pivot = next(i for i in range(col, n) if matrix[i][col])
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        scale = matrix[col][col]
        matrix[col] = [value / scale for value in matrix[col]]
        for row_index in range(n):
            if row_index == col:
                continue
            factor = matrix[row_index][col]
            matrix[row_index] = [
                value - factor * pivot_value
                for value, pivot_value in zip(matrix[row_index], matrix[col])
            ]
    return {node: matrix[i][-1] for i, node in enumerate(unknowns)}


def near(actual, expected, tolerance=1e-9):
    assert abs(float(actual) - expected) <= tolerance, (actual, expected)


def main():
    results = {}
    a09 = solve_resistor_network(
        ["X"], [("V5", "X", 1000), ("X", "G", 2000), ("X", "G", 2000)],
        {"V5": 5, "G": 0},
    )["X"]
    source_ma = (F(5) - a09) / 1000 * 1000
    each_ma = a09 / 2000 * 1000
    near(a09, 2.5)
    near(source_ma, 2.5)
    near(each_ma, 1.25)
    near(float(source_ma) * 5, 12.5)
    near(float(source_ma) ** 2 * 1000 / 1000, 6.25)
    results["A09"] = {"Vx_V": float(a09), "Isource_mA": float(source_ma), "Ibranch_mA": float(each_ma)}

    a10_branches = [("V10", "A", 2000), ("A", "G", 2000), ("A", "B", 2000), ("B", "G", 2000)]
    a10 = solve_resistor_network(["A", "B"], a10_branches, {"V10": 10, "G": 0})
    near(a10["A"], 4)
    near(a10["B"], 2)
    near((a10["A"] - a10["B"]) / 2000 * 1000, 1)
    results["A10"] = {"Va_V": float(a10["A"]), "Vb_V": float(a10["B"])}

    a11_branches = [("V1", "X", 1000), ("V2", "X", 1000), ("X", "G", 1000)]
    def a11_solve(v1, v2):
        return solve_resistor_network(["X"], a11_branches, {"V1": v1, "V2": v2, "G": 0})["X"]
    total, first, second = a11_solve(10, 5), a11_solve(10, 0), a11_solve(0, 5)
    assert total == first + second == 5
    near(a11_solve(6, 5), 11 / 3)
    results["A11"] = {"Vx_V": float(total), "V_from_10V": float(first), "V_from_5V": float(second)}

    divider = [("V12", "OUT", 2000), ("OUT", "G", 4000)]
    open_v = solve_resistor_network(["OUT"], divider, {"V12": 12, "G": 0})["OUT"]
    rth = F(2000 * 4000, 2000 + 4000)
    inorton_ma = open_v / rth * 1000
    assert open_v == 8
    near(rth, 4000 / 3)
    near(inorton_ma, 6)
    loaded = {}
    for load in (1000, 2000, 4000, 8000):
        direct = solve_resistor_network(["OUT"], divider + [("OUT", "G", load)], {"V12": 12, "G": 0})["OUT"]
        equivalent = open_v * F(load, 1) / (rth + load)
        assert direct == equivalent
        loaded[str(load)] = float(direct)
    near(loaded["4000"], 6)
    near(loaded["2000"], 4.8)
    near(float(open_v * open_v / (4 * rth) * 1000), 12)
    results["A12"] = {"Vth_V": float(open_v), "Rth_ohm": float(rth), "In_mA": float(inorton_ma), "loads_V": loaded}

    rc_tau = 10_000 * 100e-6
    rl_tau = 100e-3 / 10
    rc_1tau = 5 * (1 - exp(-1))
    near(rc_tau, 1)
    near(rl_tau, 0.01)
    near(rc_1tau, 3.160602794, 1e-8)
    near(3 * (1 - exp(-1)), 1.896361676, 1e-8)
    results["A13"] = {"RC_tau_s": rc_tau, "RC_1tau_V": rc_1tau, "RL_tau_s": rl_tau}

    r, l, c = 100, 10e-3, 100e-9
    f0 = 1 / (2 * pi * sqrt(l * c))
    bandwidth = r / (2 * pi * l)
    omega_low = (sqrt(r * r + 4 * l / c) - r) / (2 * l)
    omega_high = (sqrt(r * r + 4 * l / c) + r) / (2 * l)
    f_low, f_high = omega_low / (2 * pi), omega_high / (2 * pi)
    near(f0, 5032.921210, 1e-5)
    near(bandwidth, 1591.549431, 1e-6)
    near(f_high - f_low, bandwidth, 1e-9)
    near(1 / r * 1000, 10)
    near(1 / (2 * pi * sqrt(l * 400e-9)), f0 / 2, 1e-9)
    results["A14"] = {"f0_Hz": f0, "bandwidth_Hz": bandwidth, "f_low_Hz": f_low, "f_high_Hz": f_high, "I_at_f0_mArms": 10}
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
