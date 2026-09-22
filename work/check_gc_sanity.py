"""Sanity checks on the f_1^p e_{-1}^q h_{-1}^s lattice of Q_0 = T_{f_0} M_{-1,1}.

Scope note (after the 2026-09-22 audit): the lattice IS closed under the
full E-action because [e_0, X] contains no f_0 for X in this lattice (f_0
arises only from [h_j, f_{-j}] pairs, and f_{-1} is not in the lattice), so
the higher components A_r (r >= 1) vanish here and the formula
E(F^{-m}X) = F^{-m}T(X) - m(mu+deg+m+1)F^{-m-1}X is the FULL action on
this subspace. Out-of-lattice words (e.g. f_{-1}f_1, h_{-1}^2 with its
-4e_{-2}u term) are covered by check_audit_regressions.py.
"""
import sympy as sp
from sympy import symbols, expand

lam0, lam1, kap = symbols('lam0 lam1 kap')
CHECKS = 0


def check(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError('FAILED: ' + label)
    CHECKS += 1


def T(vec):
    # T = pi_0 ad(e_0) on words f_1^p e_{-1}^q h_{-1}^s acting on u
    out = {}
    for (p, q, s), c in vec.items():
        out[p - 1, q, s] = out.get((p - 1, q, s), 0) + c * p * lam1
        out[p - 1, q, s - 1] = out.get((p - 1, q, s - 1), 0) + c * p * 2 * s * kap
        out[p, q + 1, s - 1] = out.get((p, q + 1, s - 1), 0) - c * 2 * s
    return {k: v for k, v in out.items() if expand(v) != 0}


def Tpow(vec, n):
    for _ in range(n):
        vec = T(vec)
    return vec


check(T({(0, 0, 0): 1}) == {}, 'T(1)u = 0 (X=1 primitive at mu=-2)')
check(Tpow({(2, 0, 0): 1}, 3) == {}, 'T^3(f_1^2)u = 0 (lambda_0 = 0, P_2 primitive)')
check(T({(0, 0, 1): 1}) == {(0, 1, 0): -2}, 'T(h_{-1})u = -2e_{-1}u')
print(f'gc sanity checks PASS: {CHECKS} checks')
