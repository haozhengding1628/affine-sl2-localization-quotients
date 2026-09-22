"""Corrected-filter checks: the weight filtration for G_c structure (round 2).

Basic model Q_0 = T_{f_0} M_{-1,1} at mu = -2 (P_0 = C w_1), lambda_1 != 0.
  (1) h_j w_1 = -F e_j w_1  (h_j kills the nu=0 quotient), j >= 1;
  (2) f_j w_1 = -(1/2) F^2 e_j w_1, so f_j w_1 has NO P_0-component;
      E^2 f_j w_1 = -2 e_j w_1;
  (3) the P_2-seed (top f_1^2) is primitive, and e_1 maps it to a nonzero P_4;
  (4) spot checks that G^{>=nu} is g-stable (weight accounting).
Vectors: dicts {(m, p, q, s): coeff} = F^{-m} f_1^p e_{-1}^q h_{-1}^s u.
"""
import sympy as sp
from sympy import symbols, expand, Rational

lam0, lam1, kap = symbols('lam0 lam1 kap')
CHECKS = 0


def check(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError('FAILED: ' + label)
    CHECKS += 1


def clean(d):
    return {k: sp.expand(v) for k, v in d.items() if sp.expand(v) != 0}


def add(out, k, c):
    if c == 0:
        return
    out[k] = out.get(k, 0) + c


def F(v):
    out = {}
    for (m, p, q, s), c in v.items():
        if m >= 2:
            add(out, (m - 1, p, q, s), c)
    return clean(out)


def E_mu(v, mu):
    # E F^{-m} X = F^{-m} T(X) - m(mu + deg + m + 1) F^{-m-1} X
    # T(f_1^p e^q h^s)u = p(lam1 h^s + 2 s kap h^(s-1)) f_1^(p-1) e^q u - 2 s f_1^p e^(q+1) h^(s-1) u
    out = {}
    for (m, p, q, s), c in v.items():
        if p >= 1:
            add(out, (m, p - 1, q, s), c * p * lam1)
            if s >= 1:
                add(out, (m, p - 1, q, s - 1), c * p * 2 * s * kap)
        if s >= 1:
            add(out, (m, p, q + 1, s - 1), -c * 2 * s)
        add(out, (m + 1, p, q, s), -c * m * (mu + 2 * q - 2 * p + m + 1))
    return clean(out)


def E(v):
    return E_mu(v, Rational(-2))


def h_j(j, v):
    # h_j F^{-m} = F^{-m} h_j + 2m F^{-m-1} f_j ;  h_j X u = lam_j X u + [h_j, X]u
    out = {}
    for (m, p, q, s), c in v.items():
        add(out, (m, p, q, s), c * (lam1 if j == 1 else 0))
        if s >= 1 and j == 1:
            add(out, (m, p, q, s - 1), c * 2 * s * kap)
        if j == 1:
            add(out, (m + 1, p + 1, q, s), c * 2 * m)
        if j == 2 and s >= 1:
            add(out, (m + 1, p + 1, q, s - 1), c * 2 * m * 2 * s)  # [f_2, h_{-1}] = 2 f_1
    return clean(out)


def e_j(j, v):
    # e_j F^{-m} = F^{-m} e_j - m F^{-m-1} h_j - m(m+1) F^{-m-2} f_j (j>=1)
    # e_j on the lattice: [e_j,f_1]=h_{j+1} and h_{j+1} kills u (lam_{j+1}=0),
    # all cascades kill u; so the F^{-m} e_j X u part vanishes for j>=1.
    out = {}
    for (m, p, q, s), c in v.items():
        add(out, (m + 1, p, q, s), -c * m * (lam1 if j == 1 else 0))
        if s >= 1 and j == 1:
            add(out, (m + 1, p, q, s - 1), -c * m * 2 * s * kap)
        if j == 1:
            add(out, (m + 2, p + 1, q, s), -c * m * (m + 1))
        if j == 2 and s >= 1:
            add(out, (m + 2, p + 1, q, s - 1), -c * m * (m + 1) * 2 * s)
    return clean(out)


def f_j(j, v):
    out = {}
    for (m, p, q, s), c in v.items():
        if j == 1:
            add(out, (m, p + 1, q, s), c)
        elif j == 2 and s >= 1:
            add(out, (m, p + 1, q, s - 1), c * 2 * s)  # [f_2, h_{-1}] = 2 f_1
    return clean(out)


w1 = {(1, 0, 0, 0): 1}
check(E(w1) == {}, 'E w_1 = 0 (mu=-2)')

# (1) h_j w_1 = -F e_j w_1
for j in [1, 2]:
    lhs = h_j(j, w1)
    rhs = clean({k: -v for k, v in F(e_j(j, w1)).items()})
    check(lhs == rhs, f'h_{j} w_1 = -F e_{j} w_1')

# (2) f_j w_1 = -(1/2) F^2 e_j w_1  and  E^2 f_j w_1 = -2 e_j w_1
for j in [1, 2]:
    lhs = f_j(j, w1)
    rhs = clean({k: -sp.Rational(1, 2) * v for k, v in F(F(e_j(j, w1))).items()})
    check(lhs == rhs, f'f_{j} w_1 = -(1/2) F^2 e_{j} w_1 (no P_0-part)')
    check(E(E(f_j(j, w1))) == clean({k: -2 * v for k, v in e_j(j, w1).items()}), f'E^2 f_{j} w_1 = -2 e_{j} w_1')

# (3) P_2 seed by the recursion: top f_1^2 at pole 3, mu = 0
p2 = {(3, 2, 0, 0): 1, (2, 1, 0, 0): lam1, (1, 0, 0, 0): sp.Rational(1, 2) * lam1 ** 2}
check(E_mu(p2, 0) == {}, 'P_2 seed primitive (mu=0)')
up = e_j(1, p2)
check(up != {}, 'e_1 . P_2 nonzero')
check(E_mu(up, 0) == {}, 'e_1 . P_2 in P_4')

# (4) weight accounting: all test vectors have weights as predicted (m,p,q,s -> mu+2m-2p+2q)
def wt_of(m, p, q, s):
    return 2 * m - 2 * p + 2 * q  # mu added outside

for name, vec, mu in [('h_j w_1', h_j(1, w1), -2), ('f_1 w_1', f_j(1, w1), -2),
                      ('e_1 w_1', e_j(1, w1), -2), ('P_2 seed', p2, 0),
                      ('e_1 . P_2', up, 0)]:
    ws = {wt_of(*k) for k in vec}
    check(len(ws) == 1, f'{name} pure weight')

print(f'corrected-filter checks PASS: {CHECKS} checks')
