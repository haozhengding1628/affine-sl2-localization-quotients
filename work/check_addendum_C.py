"""Symbolic verification of the 2026-09-15 addendum, Part C.

Critical-level Sugawara T(n) on the localized basic module M_{-1,1}
(F = f_0, symbols lam0, lam1, kappa).  The module model uses a PBW
normal form: canonical words are f-tuple . e-tuple . h-tuple . u with
free modes f_j (j<=1), e_i (i<=-1), h_r (r<=-1); a rewrite system
(f < e < h order plus commutator rules) computes the left action.

  C0  consistency of the action with the affine brackets
  C1  [T(n), x] u = 0 for x in {e_0, f_0, f_1, h_0, h_1}, n in [-2..2], kappa=-2
  C2  T(n)(F^-m u) = F^-m T(n) u, n in [-2..2], m in [1..3]
  C3  ad-iteration identity [x_r, F^m] = sum C(m,k) (adF)^k(x_r) F^(m-k), c=0
  C4  smoothness formulas for GENERAL c (symbolic r, c, m) derived via
      ad-iteration plus the h-push rule, compared with eq. smooth-h/e.
"""
import functools
import sympy as sp
from sympy import symbols, Rational, binomial, expand, KroneckerDelta

lam0, lam1, kap = symbols('lam0 lam1 kap')
CHECKS = 0


def check(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError('FAILED: ' + label)
    CHECKS += 1


def br(x, y):
    if x == 'K' or y == 'K':
        return []
    t1, r = x
    t2, s = y
    d = r + s
    if t1 == 'h' and t2 == 'h':
        return [(2 * r * int(d == 0), 'K')]
    if t1 == 'h' and t2 == 'e':
        return [(2, ('e', d))]
    if t1 == 'h' and t2 == 'f':
        return [(-2, ('f', d))]
    if t1 == 'e' and t2 == 'e':
        return []
    if t1 == 'e' and t2 == 'f':
        return [(1, ('h', d)), (r * int(d == 0), 'K')]
    if t1 == 'e' and t2 == 'h':
        return [(-2, ('e', d))]
    if t1 == 'f' and t2 == 'e':
        return [(-1, ('h', d)), (-s * int(d == 0), 'K')]
    if t1 == 'f' and t2 == 'f':
        return []
    if t1 == 'f' and t2 == 'h':
        return [(2, ('f', d))]
    raise ValueError((x, y))


FAM = {'f': 0, 'e': 1, 'h': 2}


def act_u(x):
    if x == 'K':
        return {(0, (), (), ()): kap}
    t, r = x
    if t == 'h':
        if r <= -1:
            return {(0, (), (), (r,)): 1}
        return {(0, (), (), ()): {0: lam0, 1: lam1}.get(r, 0)}
    if t == 'e':
        return {(0, (), (r,), ()): 1} if r <= -1 else {}
    if t == 'f':
        return {(0, (r,), (), ()): 1} if r <= 1 else {}
    raise ValueError(x)


def is_free(x):
    if x == 'K':
        return False
    t, r = x
    if t == 'h':
        return r <= -1
    if t == 'e':
        return r <= -1
    return r <= 1


def list_to_key(modes):
    ft, et, ht = [], [], []
    for m in modes:
        (ft if m[0] == 'f' else et if m[0] == 'e' else ht).append(m[1])
    return (0, tuple(sorted(ft)), tuple(sorted(et)), tuple(sorted(ht)))


def fam_of(m):
    if m == 'K':
        return -1
    # non-free modes (h_r with r>=0, e_r with r>=0, f_r with r>=2) must be
    # pushed all the way to the right to be evaluated on u
    if not is_free(m):
        return 3
    return FAM[m[0]]


def inv_pos(modes):
    for i in range(len(modes) - 1):
        if fam_of(modes[i]) > fam_of(modes[i + 1]):
            return i
    return -1


@functools.lru_cache(maxsize=None)
def norm(modes):
    # canonical normal form of the word (modes applied to u), returns
    # {(0, ft, et, ht): coeff}
    out = {}
    if 'K' in modes:
        idx = modes.index('K')
        rest = modes[:idx] + modes[idx + 1:]
        for key, c in norm(tuple(rest)).items():
            out[key] = out.get(key, 0) + kap * c
        return out
    i = inv_pos(modes)
    if i >= 0:
        left, right = modes[i], modes[i + 1]
        mid = list(modes[:i])
        tail = list(modes[i + 2:])
        # swap term
        for key, c in norm(tuple(mid + [right, left] + tail)).items():
            out[key] = out.get(key, 0) + c
        # bracket terms
        for cc, y in br(left, right):
            if cc == 0:
                continue
            for key, c in norm(tuple(mid + [y] + tail)).items():
                out[key] = out.get(key, 0) + cc * c
        return out
    if not modes:
        return {(0, (), (), ()): 1}
    last = modes[-1]
    if is_free(last):
        return {list_to_key(modes): 1}
    # evaluate the last mode on u
    for key, c in act_u(last).items():
        if c == 0:
            continue
        # key is a canonical word (0, ft, et, ht); multiply the remaining
        # modes on the left of it:
        full = list(modes[:-1]) + [('f', i) for i in key[1]] + [('e', i) for i in key[2]] + [('h', i) for i in key[3]]
        for key2, c2 in norm(tuple(full)).items():
            out[key2] = out.get(key2, 0) + c * c2
    return out


def push_through(x, ft, et, ht):
    full = [x] + [('f', i) for i in ft] + [('e', i) for i in et] + [('h', i) for i in ht]
    return norm(tuple(full))


CAPS = {'m': 12, 'f': 12, 'e': 12, 'h': 8, 'idx': 24}


def guard(key):
    m, ft, et, ht = key
    if m > CAPS['m'] or len(ft) > CAPS['f'] or len(et) > CAPS['e'] or len(ht) > CAPS['h']:
        raise AssertionError('cap exceeded: ' + str(key))
    for t in ft + et + ht:
        if abs(t) > CAPS['idx']:
            raise AssertionError('index cap exceeded: ' + str(key))


def add_term(out, key, coeff):
    if coeff == 0:
        return
    out[key] = out.get(key, 0) + coeff


def act(x, vec):
    out = {}
    for (m, ft, et, ht), c in vec.items():
        guard((m, ft, et, ht))
        if m == 0:
            for key, c2 in push_through(x, ft, et, ht).items():
                add_term(out, key, c * c2)
        elif x == 'K':
            add_term(out, (m, ft, et, ht), c * kap)
        elif x[0] == 'h':
            r = x[1]
            for key, c2 in push_through(('h', r), ft, et, ht).items():
                add_term(out, (m, key[1], key[2], key[3]), c * c2)
            for key, c2 in push_through(('f', r), ft, et, ht).items():
                add_term(out, (m + 1, key[1], key[2], key[3]), c * 2 * m * c2)
        elif x[0] == 'e':
            r = x[1]
            for key, c2 in push_through(('e', r), ft, et, ht).items():
                add_term(out, (m, key[1], key[2], key[3]), c * c2)
            for key, c2 in push_through(('h', r), ft, et, ht).items():
                add_term(out, (m + 1, key[1], key[2], key[3]), c * (-m) * c2)
            add_term(out, (m + 1, ft, et, ht), c * (-m) * r * int(r == 0) * kap)
            for key, c2 in push_through(('f', r), ft, et, ht).items():
                add_term(out, (m + 2, key[1], key[2], key[3]), c * (-m) * (m + 1) * c2)
        elif x[0] == 'f':
            r = x[1]
            for key, c2 in push_through(('f', r), ft, et, ht).items():
                add_term(out, (m, key[1], key[2], key[3]), c * c2)
        else:
            raise ValueError(x)
    return out


def clean(vec, subs=None):
    out = {}
    for key, c in vec.items():
        cc = expand(c)
        if subs is not None:
            cc = expand(cc.subs(subs))
        if cc != 0:
            out[key] = cc
    return out


def vec_eq(a, b, subs=None):
    ca = clean(a, subs)
    cb = clean(b, subs)
    if set(ca) != set(cb):
        return False
    return all(expand(ca[k] - cb[k]) == 0 for k in ca)


def act_all(modes, vec):
    v = vec
    for md in modes:
        v = act(md, v)
    return v


MODES0 = [('e', r) for r in range(-2, 3)] + [('f', r) for r in range(-2, 3)] + \
    [('h', r) for r in range(-2, 3)] + ['K']
WORDS0 = [
    (0, (), (), ()),
    (0, (0,), (), ()),
    (0, (1,), (), ()),
    (0, (-1,), (), ()),
    (0, (), (-1,), ()),
    (0, (), (), (-1,)),
    (0, (0, 1), (), ()),
    (1, (), (), ()),
]
for x in MODES0:
    for y in MODES0:
        for w in WORDS0:
            v = {w: 1}
            lhs = act(x, act(y, v))
            lhs2 = act(y, act(x, v))
            diff = clean(lhs, None)
            for key, c in lhs2.items():
                add_term(diff, key, -c)
            rhs = {}
            for cc, z in br(x, y):
                for key, c2 in act(z, v).items():
                    add_term(rhs, key, cc * c2)
            check(vec_eq(diff, rhs), f'C0 [{x},{y}] on {w}')


def pair_apply(a, b, v):
    if a[1] < 0:
        return act(a, act(b, v))
    return act(b, act(a, v))


def T_apply(n, v, R):
    out = {}
    for j in range(-R, R + 1):
        for key, c in pair_apply(('e', -j), ('f', n + j), v).items():
            add_term(out, key, sp.Rational(1, 4) * 2 * c)
        for key, c in pair_apply(('f', -j), ('e', n + j), v).items():
            add_term(out, key, sp.Rational(1, 4) * 2 * c)
        for key, c in pair_apply(('h', -j), ('h', n + j), v).items():
            add_term(out, key, sp.Rational(1, 4) * c)
    return out


KAP2 = {kap: sp.Integer(-2)}
u_vec = {(0, (), (), ()): 1}

for n in range(-2, 3):
    t6 = clean(T_apply(n, u_vec, 6), KAP2)
    t10 = clean(T_apply(n, u_vec, 10), KAP2)
    check(vec_eq(t6, t10), f'Cconv T({n}) j-range convergence')

for n in range(-2, 3):
    for x in [('e', 0), ('f', 0), ('f', 1), ('h', 0), ('h', 1)]:
        xu = act(x, u_vec)
        lhs = clean(T_apply(n, xu, 6), KAP2)
        tnu = clean(T_apply(n, u_vec, 6), KAP2)
        rhs = clean(act(x, tnu), KAP2)
        check(vec_eq(lhs, rhs), f'C1 [T({n}), {x}] u = 0')

for n in range(-2, 3):
    for m in range(1, 4):
        lhs = clean(T_apply(n, {(m, (), (), ()): 1}, 6), KAP2)
        tnu = clean(T_apply(n, u_vec, 6), KAP2)
        rhs = {(m + k[0], k[1], k[2], k[3]): c for k, c in tnu.items()}
        check(vec_eq(lhs, rhs), f'C2 T({n}) F^-{m} u = F^-{m} T({n}) u')


def adF_k(x, k):
    # list of (coeff, mode): sum coeff*mode = (ad f_0)^k (x)
    modes = [(1, x)]
    for _ in range(k):
        nxt = []
        for cc1, md in modes:
            for cc2, z in br(('f', 0), md):
                if cc2 != 0:
                    nxt.append((cc1 * cc2, z))
        modes = nxt
    return modes


for r in range(-2, 3):
    for m in range(1, 5):
        for w in WORDS0[:6]:
            v = {w: 1}
            fm_w = (0, w[1] + (0,) * m, w[2], w[3])
            lhs = clean(act(('e', r), {fm_w: 1}), None)
            lhs2 = act(('f', 0), act(('e', r), v))
            for _ in range(m - 1):
                lhs2 = act(('f', 0), lhs2)
            for key, c in lhs2.items():
                add_term(lhs, key, -c)
            rhs = {}
            for k in range(1, m + 1):
                fkw = (0, w[1] + (0,) * (m - k), w[2], w[3])
                for cc, md in adF_k(('e', r), k):
                    for key, c in act_all([md], {fkw: 1}).items():
                        add_term(rhs, key, -sp.binomial(m, k) * cc * c)
            check(vec_eq(lhs, rhs), f'C3e [e_{r}, F^{m}] ad-iteration on {w}')
    for m in range(1, 5):
        for w in WORDS0[:6]:
            v = {w: 1}
            fm_w = (0, w[1] + (0,) * m, w[2], w[3])
            lhs = clean(act(('h', r), {fm_w: 1}), None)
            lhs2 = act(('f', 0), act(('h', r), v))
            for _ in range(m - 1):
                lhs2 = act(('f', 0), lhs2)
            for key, c in lhs2.items():
                add_term(lhs, key, -c)
            rhs = {}
            for k in range(1, m + 1):
                fkw = (0, w[1] + (0,) * (m - k), w[2], w[3])
                for cc, md in adF_k(('h', r), k):
                    for key, c in act_all([md], {fkw: 1}).items():
                        add_term(rhs, key, -sp.binomial(m, k) * cc * c)
            check(vec_eq(lhs, rhs), f'C3h [h_{r}, F^{m}] ad-iteration on {w}')

# ---------------- C4: general-c smoothness formulas ----------------
# mini-algebra: term = (coeff, kL, tup, kR)  =  coeff * F^kL * tup * F^kR
# normalize moves right F-powers left: h_s . F^b = F^b . h_s - 2b F^(b-1) f_(s+c)
r, c, m = symbols('r c m', integer=True)


def br_sym(x, y):
    if x == 'K' or y == 'K':
        return []
    t1, r1 = x
    t2, s1 = y
    d = r1 + s1
    dd = KroneckerDelta(d, 0)
    if t1 == 'h' and t2 == 'h':
        return [(2 * r1 * dd, 'K')]
    if t1 == 'h' and t2 == 'e':
        return [(2, ('e', d))]
    if t1 == 'h' and t2 == 'f':
        return [(-2, ('f', d))]
    if t1 == 'e' and t2 == 'e':
        return []
    if t1 == 'e' and t2 == 'f':
        return [(1, ('h', d)), (r1 * dd, 'K')]
    if t1 == 'e' and t2 == 'h':
        return [(-2, ('e', d))]
    if t1 == 'f' and t2 == 'e':
        return [(-1, ('h', d)), (-s1 * dd, 'K')]
    if t1 == 'f' and t2 == 'f':
        return []
    if t1 == 'f' and t2 == 'h':
        return [(2, ('f', d))]
    raise ValueError((x, y))


def adF_sym(x, k):
    modes = [(1, x)]
    for _ in range(k):
        nxt = []
        for cc1, md in modes:
            for cc2, z in br_sym(('f', c), md):
                if cc2 != 0:
                    nxt.append((cc1 * cc2, z))
        modes = nxt
    return modes


def normalize(terms):
    out = []
    for (coeff, kL, tup, kR) in terms:
        k = sp.simplify(kL + kR)
        out.append((coeff, k, tup, 0))
        for i, md in enumerate(tup):
            if md == 'K':
                continue
            if md[0] == 'h':
                s = md[1]
                pre = tup[:i]
                post = tup[i + 1:]
                out.append((-2 * kR * coeff, sp.simplify(k - 1), pre + (('f', s + c),) + post, 0))
    return out


def left_F_sym(a, terms):
    return [(coeff, sp.simplify(kL + a), tup, kR) for (coeff, kL, tup, kR) in terms]


def right_F_sym(terms, a):
    return normalize([(coeff, kL, tup, sp.simplify(kR + a)) for (coeff, kL, tup, kR) in terms])


def term_dict(terms):
    out = {}
    for (coeff, kL, tup, kR) in terms:
        key = (sp.simplify(kL), tup, sp.simplify(kR))
        out[key] = out.get(key, 0) + expand(coeff)
    return out


def sym_eq(t1, t2):
    d1 = term_dict(t1)
    d2 = term_dict(t2)
    if set(d1) != set(d2):
        return False
    return all(sp.combsimp(expand(d1[k] - d2[k])) == 0 for k in d1)


# [e_r, F^m] by ad-iteration: sum C(m,k) (ad f_c)^k (e_r) F^(m-k), k=1,2
terms_ef = []
for k in [1, 2]:
    for cc, md in adF_sym(('e', r), k):
        terms_ef.append((sp.binomial(m, k) * cc, 0, (md,), sp.simplify(m - k)))
claimed_ef = [(-m, 0, (('h', r + c),), m - 1),
              (-m * r * KroneckerDelta(r + c, 0), 0, ('K',), m - 1),
              (-m * (m - 1), 0, (('f', r + 2 * c),), m - 2)]
check(sym_eq(terms_ef, claimed_ef), 'C4a [e_r, F^m] ad-iteration (symbolic r,c,m)')

# (ad f_c)^k (h_r) vanishes for k>=2
terms_hf = []
for k in [1]:
    for cc, md in adF_sym(('h', r), k):
        terms_hf.append((sp.binomial(m, k) * cc, 0, (md,), sp.simplify(m - k)))
claimed_hf = [(2 * m, 0, (('f', r + c),), m - 1)]
check(sym_eq(terms_hf, claimed_hf), 'C4b [h_r, F^m] ad-iteration (symbolic r,c,m)')

# [e_r, F^-m] = -F^-m [e_r, F^m] F^-m = F^-m . Sigma_e . F^-m
derived = left_F_sym(-m, claimed_ef)
derived = right_F_sym(derived, -m)
claimed_ef_neg = [(-m, sp.simplify(-m - 1), (('h', r + c),), 0),
                  (-m * r * KroneckerDelta(r + c, 0), sp.simplify(-m - 1), ('K',), 0),
                  (-m * (m + 1), sp.simplify(-m - 2), (('f', r + 2 * c),), 0)]
check(sym_eq(derived, claimed_ef_neg), 'C4c [e_r, F^-m] -> eq. smooth-e')

derived_h = left_F_sym(-m, claimed_hf)
derived_h = right_F_sym(derived_h, -m)
claimed_h_neg = [(2 * m, sp.simplify(-m - 1), (('f', r + c),), 0)]
check(sym_eq(derived_h, claimed_h_neg), 'C4d [h_r, F^-m] -> eq. smooth-h')

print(f'Part C PASS: {CHECKS} exact symbolic checks')
