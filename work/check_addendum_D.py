"""Symbolic verification of the 2026-09-15 addendum, Part D.

Central-reduction commutation, Proposition 'Algebraic reduction by commuting
endomorphisms', in the toy U = C[F,G], V = U, R = C[z] with z = G - phi(F)
(phi a polynomial in F, symbolic coefficients).  z commutes with U.

  D1  D_F(V/IV) = D_FV / I(D_FV):  G -> phi(F) reduction, well-definedness,
      and the explicit congruence F^m G^n - F^m phi(F)^n = (G-phi) q.
  D2  T_F(V/IV) = (T_FV)/I(T_FV):  reduction step, image membership,
      independence of the classes [F^m], m < 0.

Exact symbolic linear algebra; no truncation in m or n for the identities,
and a symbolic linsolve for the independence statement.
"""
import sympy as sp
from sympy import symbols, expand, linsolve, Matrix

theta, a, b = symbols('theta a b')
CHECKS = 0


def check(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError('FAILED: ' + label)
    CHECKS += 1


class L:
    # element of C[F, F^-1, G]: dict {(m, n): coeff}, m in Z, n >= 0
    def __init__(self, d):
        self.d = {k: v for k, v in d.items() if expand(v) != 0}

    def F(self):
        return L({(m + 1, n): c for (m, n), c in self.d.items()})

    def G(self):
        return L({(m, n + 1): c for (m, n), c in self.d.items()})

    def polyF(self, phi):
        out = {}
        for (m, n), c in self.d.items():
            for k, ck in phi.items():
                out[m + k, n] = out.get((m + k, n), 0) + c * ck
        return L(out)

    def scale(self, s):
        return L({k: c * s for k, c in self.d.items()})

    def __add__(self, o):
        d = dict(self.d)
        for k, c in o.d.items():
            d[k] = d.get(k, 0) + c
        return L(d)

    def __sub__(self, o):
        return self + o.scale(-1)

    def is_zero(self):
        return all(expand(c) == 0 for c in self.d.values())

    def eq(self, o):
        dd = (self - o).d
        return all(expand(c) == 0 for c in dd.values())

    def rho(self, phi):
        # G -> phi(F): image in C[F, F^-1]
        out = {}
        for (m, n), c in self.d.items():
            acc = {m: c}
            for _ in range(n):
                nxt = {}
                for mm, cc in acc.items():
                    for k, ck in phi.items():
                        nxt[mm + k] = nxt.get(mm + k, 0) + cc * ck
                acc = nxt
            for mm, cc in acc.items():
                out[mm] = out.get(mm, 0) + cc
        return L({(mm, 0): cc for mm, cc in out.items()})


def z_of(phi):
    def z(v):
        return v.G() - v.polyF(phi)
    return z


PHIS = {
    'phi=theta': {0: theta},
    'phi=F': {1: sp.Integer(1)},
    'phi=F^2': {2: sp.Integer(1)},
    'phi=aF+bF^2': {1: a, 2: b},
}

for name, phi in PHIS.items():
    z = z_of(phi)
    # D1a: the reduction G -> phi(F) is well defined: rho(z . v) = 0
    for m in range(-4, 5):
        for n in range(5):
            v = L({(m, n): 1})
            check(z(v).rho(phi).is_zero(), f'D1a rho(z.v)=0, {name}, m={m}, n={n}')
    # precomputed powers of phi (as dicts {deg: coeff})
    phipow = [{0: sp.Integer(1)}]
    for _ in range(6):
        nxt = {}
        for mm, cc in phipow[-1].items():
            for k, ck in phi.items():
                nxt[mm + k] = nxt.get(mm + k, 0) + cc * ck
        phipow.append(nxt)
    # D1b: explicit congruence F^m G^n - F^m phi^n = (G-phi) q
    for m in range(-3, 4):
        for n in range(1, 6):
            q = L({})
            for i in range(n):  # q = F^m sum_{i=0}^{n-1} phi^(n-1-i) G^i
                for mm, cc in phipow[n - 1 - i].items():
                    q = q + L({(m + mm, i): cc})
            lhs = z(q)
            # rhs = F^m G^n - F^m phi(F)^n
            rhs = L({(m, n): 1})
            sub = L({(m, 0): 1})
            for _ in range(n):
                sub = sub.polyF(phi)
            rhs = rhs - sub
            check(lhs.eq(rhs), f'D1b congruence, {name}, m={m}, n={n}')

    # D2a: reduction step in T_FV: (G-phi)(F^m G^(n-1)) = F^m G^n - phi(F) F^m G^(n-1)
    for m in range(-3, 4):
        for n in range(1, 5):
            v = L({(m, n - 1): 1})
            lhs = z(v)
            rhs = L({(m, n): 1}) - L({(m, n - 1): 1}).polyF(phi)
            check(lhs.eq(rhs), f'D2a reduction step, {name}, m={m}, n={n}')
    # D2b: image membership: F^m phi^n = (G-phi) q  with q = F^m sum phi^(n-1-i) G^i
    for m in range(-3, 4):
        for n in range(1, 5):
            q = L({})
            for i in range(n):
                for mm, cc in phipow[n - 1 - i].items():
                    q = q + L({(m + mm, i): cc})
            lhs = z(q)
            target = L({(m, 0): 1})
            for _ in range(n):
                target = target.polyF(phi)
            check(lhs.eq(L({(m, n): 1}) - target), f'D2b image membership, {name}, m={m}, n={n}')

    # D2c: independence of {[F^m] : m<0} in (T_FV)/I(T_FV):
    # sum_{m in S} s_m F^m = (G-phi) q + p,  q,p in C[F,G] -> all s_m = 0.
    S = list(range(-5, 0))
    s_syms = {m: symbols(f's_{m}') for m in S}
    N = 4
    M_LO, M_HI = -8, 8
    q_syms = {(m, n): symbols(f'q_{m}_{n}') for m in range(M_LO, M_HI + 1) for n in range(N + 1)}
    p_syms = {(m, n): symbols(f'p_{m}_{n}') for m in range(0, M_HI + 1) for n in range(N + 1)}
    unknowns = list(s_syms.values()) + list(q_syms.values()) + list(p_syms.values())
    # (G-phi) q = G q - phi(F) q
    gq = {}
    for (m, n), s in q_syms.items():
        gq[m, n + 1] = gq.get((m, n + 1), 0) + s
    phiq = {}
    for (m, n), s in q_syms.items():
        for k, ck in phi.items():
            phiq[m + k, n] = phiq.get((m + k, n), 0) - ck * s
    lhs = {}
    for m in S:
        lhs[m, 0] = lhs.get((m, 0), 0) + s_syms[m]
    eqs = []
    for m in range(M_LO, M_HI + 1):
        for n in range(N + 2):
            expr = gq.get((m, n), 0) + phiq.get((m, n), 0) + p_syms.get((m, n), 0) - lhs.get((m, n), 0)
            if expr != 0:
                eqs.append(expr)
    sol = linsolve(Matrix(eqs), unknowns)
    check(sol != sp.EmptySet, f'D2c system consistent, {name}')
    for soln in list(sol)[:1]:
        for m in S:
            check(expand(soln[unknowns.index(s_syms[m])]) == 0,
                  f'D2c s_{m} = 0, {name}')

print(f'Part D PASS: {CHECKS} exact symbolic checks')
