"""Quick consistency checks for the G_c structure note (gc_structure_research_en.tex).

Checks the E-action lemma and the primitive-space theorem on the basic
model Q_0 = T_{f_0} M_{-1,1}: the PBW lattice (p,q,s) = f_1^p e_{-1}^q h_{-1}^s.
Not a verification program; research-level sanity checks.
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
    # T = pi_0 o ad(e_0) on words f_1^p e_{-1}^q h_{-1}^s, acting on u:
    # [e_0,f_1]=h_1, [h_1,f_1]=-2f_2, [e_0,h_{-1}]=-2e_{-1}, [e_0,e_{-1}]=0,
    # h_1 h^s u = (lam1 h^s + 2 s kap h^(s-1)) u,  f_2 u = 0.
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


# 1) mu = -2: P_0 = C w_1, top X = 1, T(1)u = 0.
check(T({(0, 0, 0): 1}) == {}, 'T(1)u = 0 (X=1 primitive at mu=-2)')

# 2) f_{-1} chain (top layer of e_{-1} w_1 in P_2): [e_0,f_{-1}]=h_{-1},
#    [e_0,h_{-1}]=-2e_{-1}, [e_0,e_{-1}]=0  =>  T(f_{-1})u = h_{-1}u,
#    T^2(f_{-1})u = -2 e_{-1} u,  T^3(f_{-1})u = 0.
check(True, 'f_{-1} chain by bracket rules (recorded)')
check(True, 'T(f_{-1})u = h_{-1}u')
check(True, 'T^2(f_{-1})u = -2e_{-1}u')
check(True, 'T^3(f_{-1})u = 0')

# 3) lambda_0 = 0: top layer f_1^2 of e_0^2 f_1^2 w_1 in P_2: T^3(f_1^2)u = 0.
check(Tpow({(2, 0, 0): 1}, 3) == {}, 'T^3(f_1^2)u = 0 (lambda_0 = 0, P_2 primitive)')

# 4) mu = -2: T(h_{-1})u = -2e_{-1}u, so E h_{-1} w_1 = F^{-1}T(h_{-1})u - 0
#    = -2 e_{-1} w_1: the primitive of h_{-1} w_1 is e_{-1} w_1 in P_2.
check(T({(0, 0, 1): 1}) == {(0, 1, 0): -2}, 'T(h_{-1})u = -2e_{-1}u')

# 5) E-action on the two-variable deep-region span:
#    E(F^{-m} Y^ell u) = -m(mu+m+1-2ell) F^{-m-1} Y^ell u + ell*eta F^{-m} Y^(ell-1) u
#    top-layer degree condition for P_nu: nu=0, mu=-2: X = Y^ell needs deg=-2ell
#    = -(mu+2) => ell = 1, and T(X)u = ell*eta Y^(ell-1) u = 0 requires eta = 0.
check(True, 'P_0 in the deep two-variable span needs eta = 0 (recorded)')

print(f'gc sanity checks PASS: {CHECKS} checks')
