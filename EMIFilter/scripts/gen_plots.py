#!/usr/bin/env python3
"""Generate the pgfplots data files in ../figures from the example circuits.

Run from anywhere: python3 scripts/gen_plots.py
The .dat files are committed so the LaTeX build does not need numpy.
"""
from pathlib import Path

import numpy as np

FIG = Path(__file__).resolve().parent.parent / "figures"
f = np.logspace(3, 6, 600)
s = 2j * np.pi * f


def par(a, b):
    return a * b / (a + b)


def write(name, cols, header):
    FIG.mkdir(exist_ok=True)
    data = np.column_stack([f] + [np.abs(c) for c in cols])
    np.savetxt(FIG / name, data, header=header, comments="", fmt="%.6g")


# Examples 2.1 and 3.1: first-try single LC, undamped and optimally Rd-Ld damped
L, RL, C, ESR = 68e-6, 0.12, 6.8e-6, 0.01
R0 = np.sqrt(L / C)
ZL = RL + s * L
ZC = ESR + 1 / (s * C)
cols = [par(ZL, ZC)]
# Largest n meeting the 26.9 ohm target (Example 3.1)
n_max = (-1 + np.sqrt(1 + 4 * (26.9 / R0) ** 2)) / 4
for n in (0.5, 1.0, n_max):
    Rd = R0 * np.sqrt(n * (3 + 4 * n) * (1 + 2 * n) / (2 * (1 + 4 * n)))
    cols.append(par(par(ZL, Rd + s * n * L), ZC))
write("single-stage-zo.dat", cols, "f undamped n05 n1 nmax")

# Example 4.2: candidate design, undamped and with the n = 1, Rd = 3.4 ohm leg
L1, C1, L2, C2 = 39e-6, 2.2e-6, 4.7e-6, 4.7e-6


def ladder(Rd=None, n=1.0):
    ZL1 = 0.08 + s * L1
    if Rd is not None:
        ZL1 = par(ZL1, Rd + 0.05 + s * n * L1)
    Zup0 = 0.06 + s * 2e-6 + ZL1
    ZC1 = 0.01 + 1 / (s * C1)
    Zup1 = par(ZC1, Zup0)
    ZC2 = 0.005 + 1 / (s * C2)
    ZL2 = 0.02 + s * L2
    Zo = par(ZC2, ZL2 + Zup1)
    H = ZC2 / (ZC2 + ZL2 + Zup1) * ZC1 / (ZC1 + Zup0)
    return Zo, H


Zo_u, H_u = ladder()
Zo_d, H_d = ladder(3.4)
write("two-stage-zo.dat", [Zo_u, Zo_d, H_u, H_d], "f Zo_undamped Zo_damped H_undamped H_damped")
