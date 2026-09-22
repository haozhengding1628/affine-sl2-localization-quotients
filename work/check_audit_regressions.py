#!/usr/bin/env python3
"""Regression checks for the counterexamples of the 2026-09-22 audit
(audits/2026-09-22/audit_report_cn.md), added per its recommended step 4.

Full affine current bracket, dynamic modes, no index truncation, no
assertion imported from the notes under review. Finite exact tests.
Design follows the audit's independent_pbw_audit.py.

Run: python check_audit_regressions.py   (dependency: SymPy)
"""
from collections import defaultdict
from functools import lru_cache
import sympy as sp

mu, lam, kap = sp.symbols('mu lambda1 kappa')
Gen = tuple
Word = tuple
E, F, H, K = ('e', 0), ('f', 0), ('h', 0), ('K', 0)
CHECKS = 0


def check(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError('FAILED: ' + label)
    CHECKS += 1


def clean(v):
    return {k: sp.expand(c) for k, c in v.items() if sp.expand(c) != 0}


def add(*vs):
    out = defaultdict(lambda: sp.S.Zero)
    for v in vs:
        for w, c in v.items():
            out[w] += c
    return clean(out)


def scale(c, v):
    return clean({w: c*a for w, a in v.items()})


def bracket(x, y):
    a, i = x
    b, j = y
    if a == 'K' or b == 'K':
        return {}
    if a == b:
        return {K: sp.Integer(2*i)} if a == 'h' and i+j == 0 and i else {}
    if a == 'h':
        return {(b, i+j): sp.Integer(2 if b == 'e' else -2)}
    if b == 'h':
        return scale(-1, bracket(y, x))
    if a == 'e' and b == 'f':
        out = {('h', i+j): sp.S.One}
        if i+j == 0 and i:
            out[K] = sp.Integer(i)
        return out
    return scale(-1, bracket(y, x))


def is_character(x):
    a, i = x
    return a == 'K' or (a == 'h' and i >= 0) or (a == 'e' and i >= 0) or (a == 'f' and i >= 2)


def character(x):
    a, i = x
    if a == 'K':
        return kap
    if a == 'h':
        return mu if i == 0 else lam if i == 1 else sp.S.Zero
    return sp.S.Zero


def order(x):
    a, i = x
    if x == F:
        return 0, 0, 0
    if not is_character(x):
        return {'f': 1, 'e': 2, 'h': 3}[a], i, 0
    return 4, {'h': 0, 'e': 1, 'f': 2, 'K': 3}[a], i


@lru_cache(maxsize=None)
def normal(word):
    if not word:
        return {(): sp.S.One}
    if is_character(word[-1]):
        c = character(word[-1])
        return {} if c == 0 else scale(c, normal(word[:-1]))
    for i in range(len(word)-1):
        if order(word[i]) > order(word[i+1]):
            x, y = word[i:i+2]
            terms = [normal(word[:i]+(y, x)+word[i+2:])]
            for z, c in bracket(x, y).items():
                terms.append(scale(c, normal(word[:i]+(z,)+word[i+2:])))
            return add(*terms)
    return {word: sp.S.One}


def fraction(pole, numerator=()):
    out = defaultdict(lambda: sp.S.Zero)
    for w, c in normal(numerator).items():
        r = 0
        while r < len(w) and w[r] == F:
            r += 1
        if pole-r >= 1:
            out[(pole-r, w[r:])] += c
    return clean(out)


def act(x, v):
    # x F^{-m} = sum_j binom(m+j-1, j) F^{-m-j} (ad F)^j (x)
    out = {}
    for (m, word), c in v.items():
        if m == 0:
            for w, cc in normal((x,) + word).items():
                out[w] = out.get(w, 0) + c * cc
            continue
        cur = {x: sp.S.One}
        j = 0
        while cur:
            for y, a in cur.items():
                for key, cc in fraction(m+j, (y,)+word).items():
                    out[key] = out.get(key, 0) + c*a*cc*sp.binomial(m+j-1, j)
            nxt = {}
            for y, a in cur.items():
                for z, b in bracket(F, y).items():
                    nxt[z] = nxt.get(z, 0) + a*b
            cur = clean(nxt)
            j += 1
    return clean(out)


def A(word):
    # E x = sum_r F^r A_r x on M: returns {r: dict(word->coeff)}
    out = {}
    for w, c in normal(word).items():
        r = 0
        while r < len(w) and w[r] == F:
            r += 1
        out.setdefault(r, {})[w[r:]] = out[r].get(w[r:], 0) + c
    return {r: clean(v) for r, v in out.items()}


# ---- 1. E-action counterexample: E F^{-2} f_{-1} f_1 u must contain -2 w_1 ----
X = (('f', -1), ('f', 1))
EX = act(E, {(0, X): 1})
check(EX == {(('f', 1), ('h', -1)): 1, (('f', -1),): lam, (F,): -2},
      'EXu = (f_1 h_{-1} + lam f_{-1} - 2F)u')
v = fraction(2, X)
Ev = act(E, v)
check(Ev.get((1, ()), 0) == -2, 'E-action keeps the F^1 numerator term: residual -2 w_1')
# the truncated (pi_0-only) formula would give: F^{-2}T(X)u - 2(mu-1)F^{-3}Xu
trunc = add(fraction(2, (('f', 1), ('h', -1))), scale(lam, fraction(2, (('f', -1),))),
            scale(-2*(mu-1), fraction(3, X)))
resid = add(Ev, scale(-1, trunc))
check(resid == {(1, ()): -2}, 'truncated pi_0 formula misses exactly -2 w_1')

# ---- 2. T-truncation counterexample: T(h_{-1}^2)u = -4 e_{-1} h_{-1} u - 4 e_{-2} u ----
Th = act(E, {(0, (('h', -1), ('h', -1))): 1})
check(Th == {(('e', -1), ('h', -1)): -4, (('e', -2),): -4},
      'T(h_{-1}^2)u = -4 e_{-1} h_{-1} u - 4 e_{-2} u')

# ---- 3. Z commutes with E, F, H; Z^n w_1 in P_0 with distinct leading degrees ----
ZU = add(normal((('h', -1), ('h', -1))), scale(4, normal((('f', -1), ('e', -1)))),
         scale(2, normal((('h', -2),))))
zu = {(0, w): c for w, c in ZU.items()}
check(act(E, zu) == {}, 'EZ u = [E,Z] u = 0')
zuf = add(*(scale(c, normal(w + (F,))) for w, c in ZU.items()))
check(act(F, zu) == zuf, 'F(Zu) = Z(Fu): [F,Z] u = 0')
check(act(H, zu) == {w: c * mu for w, c in ZU.items()}, 'H(Zu) = Z(Hu) = mu Zu: [H,Z] u = 0')
for n in [0, 1, 2, 3]:
    acc = {(): sp.S.One}
    for _ in range(n):
        acc = add(*(scale(c, normal(w + (('h', -1), ('h', -1)))) for w, c in acc.items()),
                  *(scale(4*c, normal(w + (('f', -1), ('e', -1)))) for w, c in acc.items()),
                  *(scale(2*c, normal(w + (('h', -2),))) for w, c in acc.items()))
    p = add(*(scale(c, fraction(1, w)) for w, c in acc.items()))
    ep = clean({k: v.subs(mu, -2) for k, v in act(E, p).items()})
    check(ep == {}, f'Z^{n} w_1 in P_0 (mu=-2)')
    check(p != {}, f'Z^{n} w_1 nonzero')

# ---- 4. corrected recursion at mu = -1: T^2 x_2 = 8 e_{-1} u, A_1 x_2 = -8 e_{-1} u ----
# p = lam F^{-1} u + F^{-2} f_1 u in P_1 at mu = -1 (checked by direct E-action below)
p1 = add(scale(lam, fraction(1)), fraction(2, (('f', 1),)))
check(clean({k: v.subs(mu, -1) for k, v in act(E, p1).items()}) == {},
      'p = lam w_1 + f_1 w_2 in P_1 at mu=-1')
# Z p: layers x_1 = (lam Z - 4 h_{-1})u, x_2 = (f_1 Z - 4(kappa+1) f_{-1})u
x2 = add(scale(1, normal((('f', 1), ('h', -1), ('h', -1)))),
         scale(4, normal((('f', 1), ('f', -1), ('e', -1)))),
         scale(2, normal((('f', 1), ('h', -2)))),
         scale(-4*(kap+1), normal((('f', -1),))))
# E x_2 u = sum_r F^r A_r x_2 u; T^2 x_2 u = A_0 A_0 x_2 u; A_1 x_2 u = F^1-part
Ex2 = act(E, {(0, w): c for w, c in x2.items()})
parts = {}
for w, c in Ex2.items():
    r = 0
    while r < len(w) and w[r] == F:
        r += 1
    d = parts.setdefault(r, {})
    d[w[r:]] = d.get(w[r:], 0) + c
A1x2 = clean(parts.get(1, {}))
A0x2 = clean(parts.get(0, {}))
check(A1x2 == {(('e', -1),): -8}, 'A_1 x_2 u = -8 e_{-1} u')
# T^2 x_2 u = A_0(A_0 x_2)u: A_0 x_2 is a combination of words; apply A_0 again
T2 = {}
for w, c in A0x2.items():
    Ew = act(E, {(0, w): 1})
    for w2, c2 in Ew.items():
        r2 = 0
        while r2 < len(w2) and w2[r2] == F:
            r2 += 1
        if r2 == 0:
            T2[w2] = T2.get(w2, 0) + c*c2
check(clean(T2) == {(('e', -1),): 8}, 'T^2 x_2 u = 8 e_{-1} u (the old T^{nu+1} criterion fails)')
check(add(clean(T2), A1x2) == {}, 'A_0^2 + A_1 kills x_2: corrected compatibility')

# ---- 5. weight-tail obstruction: [h_1, h_{-1}] w_1 = 2 kappa w_1 ----
w1 = fraction(1)
h1 = act(('h', 1), w1)
hm1 = act(('h', -1), w1)
comm = add(act(('h', 1), hm1), scale(-1, act(('h', -1), h1)))
check(comm == {(1, ()): 2*kap}, '[h_1, h_{-1}] w_1 = 2 kappa w_1')

# ---- 6. nonzero lowering projection l_1: P_2 -> P_0 at mu = -2 ----
p2 = clean({k: v.subs(mu, -2) for k, v in act(('e', -1), w1).items()})
check(clean({k: v.subs(mu, -2) for k, v in act(E, p2).items()}) == {},
      'p_2 = e_{-1} w_1 in P_2 at mu=-2')
ell = add(act(('f', 1), p2),
          scale(-sp.Rational(1, 2), act(F, act(('h', 1), p2))),
          scale(-sp.Rational(1, 6), act(F, act(F, act(('e', 1), p2)))))
ell = clean({k: v.subs(mu, -2) for k, v in ell.items()})
expected = {(1, (('f', 1), ('e', -1))): sp.Rational(1, 3),
            (1, (('h', -1),)): lam/6,
            (1, ()): sp.Rational(2, 3)*kap - sp.Rational(2, 3)}
check(ell == expected, 'l_1(p_2) = F^{-1}((1/3)f_1 e_{-1} + (lam/6) h_{-1} + (2kap-2)/3)u in P_0')
check(clean({k: v.subs(mu, -2) for k, v in act(E, ell).items()}) == {}, 'l_1(p_2) in P_0')
check(ell != {}, 'l_1(p_2) nonzero')

print(f'PASS: {CHECKS} audit-regression checks')
