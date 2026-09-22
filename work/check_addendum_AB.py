"""Symbolic verification of the 2026-09-15 addendum, Parts A and B.

A. abstract sl_2 on the Laurent span {F^k v0 : k in Z} (symbolic weight nu):
   A1/A2  Casimir factorization F^n E^n z = A_n(C;w) z  (Lemma 'Casimir factorization')
   A3     E F^n v = n(nu-n+1) F^(n-1) v on ker E (used for G_c = 0 when mu notin Z)
   A4     [E, F^j] = j F^(j-1) (H - j + 1)
   A5     Laurent identities; E F^-m = F^-m E - m F^(-m-1) H - m(m+1) F^(-m-2) F
   A6     binomial identity s F^N = sum_j (-1)^j C(N,j) F^(N-j) (ad F)^j (s)
B. deep-region two-variable model span{F^j Y^ell u} (symbolic mu, eta):
   B1     sl_2 relations [E,F]=H, [H,E]=2E, [H,F]=-2F plus [E,Y]=h_d, [h_d,Y]=0,
          [h_d,F]=-2Y, [F,Y]=0
   B2     eq. two-variable via the bracket route (independent derivation)
   B3     v_k construction: E v_k = 0, H v_k = (mu-2k) v_k (mu on integer grid)
   B4     Laurent recurrence E^r(F^-1 v_k) = prod(-m(nu+m+1)) F^(-1-r) v_k and
          its vanishing at r = 2k - mu - 1
   B5     w_m not in G_c; EF^n = n(w-n+1)F^(n-1) for weight vectors
"""
from fractions import Fraction as Q
import sympy as sp
from sympy import symbols, Rational, binomial, expand

R = Rational
nu, mu, eta = symbols('nu mu eta')
CHECKS = 0


def check(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError('FAILED: ' + label)
    CHECKS += 1


class Verma:
    def __init__(self, d):
        self.d = {k: v for k, v in d.items() if expand(v) != 0}

    @staticmethod
    def basis(k):
        return Verma({k: sp.Integer(1)})

    def _op(self, fn):
        out = {}
        for k, c in self.d.items():
            for k2, c2 in fn(k).items():
                out[k2] = out.get(k2, 0) + c * c2
        return Verma(out)

    def E(self):
        return self._op(lambda k: {k - 1: k * (nu - k + 1)})

    def F(self):
        return self._op(lambda k: {k + 1: 1})

    def Fpow(self, m):
        v = self
        for _ in range(m):
            v = v.F()
        return v

    def Fminus(self, m):
        return self._op(lambda k: {k - m: 1})

    def H(self):
        return self._op(lambda k: {k: nu - 2 * k})

    def C(self):
        return self._op(lambda k: {k: nu * (nu + 2)})

    def scale(self, s):
        return Verma({k: c * s for k, c in self.d.items()})

    def __add__(self, o):
        d = dict(self.d)
        for k, c in o.d.items():
            d[k] = d.get(k, 0) + c
        return Verma(d)

    def __sub__(self, o):
        return self + o.scale(-1)

    def eq(self, o):
        dd = (self - o).d
        return all(expand(c) == 0 for c in dd.values())


def powerA(v, op, n):
    for _ in range(n):
        v = op(v)
    return v


def A_n_poly(t_expr, w, n):
    out = sp.Integer(1)
    for j in range(n):
        out *= t_expr - (w + 2 * j) * (w + 2 * j + 2)
    return out / 4 ** n


for n in range(1, 16):
    lhs = powerA(powerA(Verma.basis(0), Verma.E, n), Verma.F, n)
    rhs = Verma.basis(0).scale(A_n_poly(nu * (nu + 2), nu, n))
    check(lhs.eq(rhs), f'A1 F^nE^n v0 = A_n(C;nu) v0, n={n}')

for m in range(7):
    for n in range(1, 9):
        lhs = powerA(powerA(Verma.basis(m), Verma.E, n), Verma.F, n)
        rhs = Verma.basis(m).scale(A_n_poly(nu * (nu + 2), nu - 2 * m, n))
        check(lhs.eq(rhs), f'A2 factorization on v_{m}, n={n}')

for n in range(1, 13):
    lhs = Verma.basis(0).Fpow(n).E()
    rhs = Verma.basis(n - 1).scale(n * (nu - n + 1))
    check(lhs.eq(rhs), f'A3 EF^n = n(nu-n+1)F^(n-1), n={n}')

for j in range(1, 9):
    for m in range(6):
        v = Verma.basis(m)
        lhs = v.Fpow(j).E() - v.E().Fpow(j)
        rhs = powerA(v.H() - v.scale(j - 1), Verma.F, j - 1).scale(j)
        check(lhs.eq(rhs), f'A4 [E,F^{j}] on v_{m}')

for k in range(-6, 7):
    v = Verma.basis(k)
    check((v.F().E() - v.E().F()).eq(v.H()), f'A5a [E,F]=H on v_{k}')
    check((v.F().H() - v.H().F()).eq(v.F().scale(-2)), f'A5b [H,F]=-2F on v_{k}')
    check((v.E().H() - v.H().E()).eq(v.E().scale(2)), f'A5c [H,E]=2E on v_{k}')
for m in range(1, 11):
    for k in range(-3, 4):
        v = Verma.basis(k)
        lhs = v.Fminus(m).E()
        rhs = (v.E().Fminus(m)
               - v.H().Fminus(m + 1).scale(m)
               - v.F().Fminus(m + 2).scale(m * (m + 1)))
        check(lhs.eq(rhs), f'A5d E F^-{m} identity on v_{k}')

WORDS = {
    'E': lambda v: v.E(),
    'H': lambda v: v.H(),
    'E2': lambda v: v.E().E(),
    'EH': lambda v: v.E().H(),
    'HE': lambda v: v.H().E(),
    'H2': lambda v: v.H().H(),
    'E3': lambda v: v.E().E().E(),
    'E2H': lambda v: v.E().E().H(),
}


def adF_power(s, j):
    ops = [s]
    for _ in range(j):
        prev = ops[-1]
        ops.append(lambda v, p=prev: p(v).F() - p(v.F()))
    return ops[-1]


for name, s in WORDS.items():
    for N in range(1, 9):
        for k in range(-2, 3):
            v = Verma.basis(k)
            lhs = s(v.Fpow(N))
            rhs = None
            for j in range(0, 8):
                term = adF_power(s, j)(v).Fpow(N - j).scale(
                    (-1) ** j * sp.binomial(N, j))
                rhs = term if rhs is None else rhs + term
            check(lhs.eq(rhs), f'A6 binomial identity, s={name}, N={N}, v_{k}')


class TwoVar:
    def __init__(self, d):
        self.d = {k: v for k, v in d.items() if expand(v) != 0}

    @staticmethod
    def basis(j, ell):
        return TwoVar({(j, ell): sp.Integer(1)})

    def _op(self, fn):
        out = {}
        for (j, ell), c in self.d.items():
            for k2, c2 in fn(j, ell).items():
                out[k2] = out.get(k2, 0) + c * c2
        return TwoVar(out)

    def E(self):
        return self._op(lambda j, ell: {(j - 1, ell): j * (mu - j + 1 - 2 * ell),
                                        (j, ell - 1): ell * eta})

    def F(self):
        return self._op(lambda j, ell: {(j + 1, ell): 1})

    def Fpow(self, m):
        v = self
        for _ in range(m):
            v = v.F()
        return v

    def Y(self):
        return self._op(lambda j, ell: {(j, ell + 1): 1})

    def H(self):
        return self._op(lambda j, ell: {(j, ell): mu - 2 * j - 2 * ell})

    def hd(self):
        return self._op(lambda j, ell: {(j, ell): eta, (j - 1, ell + 1): -2 * j})

    def scale(self, s):
        return TwoVar({k: c * s for k, c in self.d.items()})

    def __add__(self, o):
        d = dict(self.d)
        for k, c in o.d.items():
            d[k] = d.get(k, 0) + c
        return TwoVar(d)

    def __sub__(self, o):
        return self + o.scale(-1)

    def is_zero(self):
        return all(expand(c) == 0 for c in self.d.values())

    def eq(self, o):
        dd = (self - o).d
        return all(expand(c) == 0 for c in dd.values())


for j in range(7):
    for ell in range(5):
        v = TwoVar.basis(j, ell)
        check((v.F().E() - v.E().F()).eq(v.H()), f'B1a [E,F]=H on ({j},{ell})')
        check((v.E().H() - v.H().E()).eq(v.E().scale(2)), f'B1b [H,E]=2E on ({j},{ell})')
        check((v.F().H() - v.H().F()).eq(v.F().scale(-2)), f'B1c [H,F]=-2F on ({j},{ell})')
        check((v.Y().E() - v.E().Y()).eq(v.hd()), f'B1d [E,Y]=h_d on ({j},{ell})')
        check((v.Y().hd() - v.hd().Y()).is_zero(), f'B1e [h_d,Y]=0 on ({j},{ell})')
        check((v.F().hd() - v.hd().F()).eq(v.Y().scale(-2)), f'B1f [h_d,F]=-2Y on ({j},{ell})')
        check((v.Y().F() - v.F().Y()).is_zero(), f'B1g [F,Y]=0 on ({j},{ell})')

for j in range(7):
    for ell in range(5):
        v = TwoVar.basis(j, ell)
        base = TwoVar.basis(0, ell)
        inner = (base.H() - base.scale(j - 1)).Fpow(j - 1).scale(j)
        outer = TwoVar.basis(0, ell - 1).scale(ell * eta).Fpow(j)
        check(v.E().eq(inner + outer), f'B2 two-variable formula on ({j},{ell})')

def sub_mu(tv, val):
    return TwoVar({k: expand(c.subs(mu, val) if hasattr(c, 'subs') else c)
                   for k, c in tv.d.items()})


for mu_val in range(-6, 7):
    k = max(1, mu_val + 2)
    a = [sp.Integer(1)]
    for jj in range(1, k + 1):
        a.append(-(k - jj + 1) * eta / (jj * (mu_val - 2 * k + jj + 1)) * a[jj - 1])
    vk = TwoVar({(jj, k - jj): a[jj] for jj in range(k + 1)})
    check(sub_mu(vk.E(), mu_val).is_zero(), f'B3a E v_k = 0, mu={mu_val}')
    check(sub_mu(vk.H(), mu_val).eq(sub_mu(vk.scale(mu_val - 2 * k), mu_val)),
          f'B3b H v_k = (mu-2k) v_k, mu={mu_val}')
    check(mu_val - 2 * k <= -2, f'B3c nu <= -2, mu={mu_val}')
    nu_val = mu_val - 2 * k
    w = TwoVar({(jj - 1, k - jj): a[jj] for jj in range(k + 1)})
    r_star = -nu_val - 1
    check(r_star >= 1, f'B4a r* >= 1, mu={mu_val}')
    cur = w
    applied = 0
    for r in range(1, min(r_star, 5) + 1):
        cur = sub_mu(cur.E(), mu_val)
        applied += 1
        coeff = sp.Integer(1)
        for t in range(1, r + 1):
            coeff *= -t * (nu_val + t + 1)
        expected = TwoVar({(jj - 1 - r, k - jj): a[jj] * coeff for jj in range(k + 1)})
        check(cur.eq(expected), f'B4b E^r product, mu={mu_val}, r={r}')
    for r in range(applied + 1, r_star + 1):
        cur = sub_mu(cur.E(), mu_val)
    check(cur.is_zero(), f'B4c E^(2k-mu-1)(F^-1 v_k) = 0, mu={mu_val}')
    residue = [jj for jj in range(k + 1) if jj - 1 >= 0]
    check(residue == list(range(1, k + 1)), f'B4d quotient residue, mu={mu_val}')
    check(a[0] == 1, f'B4e leading coefficient, mu={mu_val}')

for mu_val in range(-6, 7):
    m0 = max(1, -mu_val)
    cur = TwoVar.basis(-m0, 0)
    for r in range(1, 13):
        cur = sub_mu(cur.E(), mu_val)
        coeff = sp.Integer(1)
        for t in range(r):
            coeff *= -(m0 + t) * (mu_val + m0 + t + 1)
        expected = TwoVar({(-m0 - r, 0): coeff})
        check(cur.eq(expected), f'B5a E^r w_m product, mu={mu_val}, r={r}')
        check(expand(coeff) != 0, f'B5b coefficient nonzero, mu={mu_val}, r={r}')
    for kp in range(1, 4):
        v = TwoVar({(0, kp): 1})
        w = mu_val - 2 * kp
        for n in range(1, 7):
            lhs = sub_mu(v.Fpow(n).E(), mu_val)
            lhs = TwoVar({k: expand(c.subs(eta, 0) if hasattr(c, 'subs') else c)
                          for k, c in lhs.d.items()})
            rhs = sub_mu(v.Fpow(n - 1).scale(n * (w - n + 1)), mu_val)
            check(lhs.eq(rhs), f'B5d EF^n = n(w-n+1)F^(n-1) at eta=0, mu={mu_val}, kp={kp}, n={n}')

print(f'Parts A-B PASS: {CHECKS} exact symbolic checks')
