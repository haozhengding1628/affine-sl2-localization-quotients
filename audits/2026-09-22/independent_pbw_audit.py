#!/usr/bin/env python3
"""Independent exact PBW checks for affine sl2 localization quotients.

Model: Q = D_{f_0} M_{-1,1}(mu, lambda1, kappa) / M_{-1,1}.
Uses the full affine current bracket and dynamically creates every required
mode. There is NO mode-index truncation and NO assertion imported from the
repository under review. This is a finite test suite, not a formal proof.

Run: python independent_pbw_audit.py   (dependency: SymPy)
"""
from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path
import sympy as sp

mu, lam, kap = sp.symbols('mu lambda1 kappa')
Gen = tuple[str, int]
Word = tuple[Gen, ...]
E: Gen = ('e', 0)
F: Gen = ('f', 0)
H: Gen = ('h', 0)
K: Gen = ('K', 0)

def gen(kind: str, index: int) -> Gen:
    return kind, index

def clean(v: dict) -> dict:
    return {k: sp.expand(c) for k, c in v.items() if sp.expand(c) != 0}

def add(*vectors: dict) -> dict:
    out = defaultdict(lambda: sp.S.Zero)
    for v in vectors:
        for w, c in v.items():
            out[w] += c
    return clean(out)

def scale(c, v: dict) -> dict:
    return clean({w: c*a for w, a in v.items()})

def bracket(x: Gen, y: Gen) -> dict[Gen, sp.Expr]:
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

def is_character(x: Gen) -> bool:
    a, i = x
    return a == 'K' or (a == 'h' and i >= 0) or (a == 'e' and i >= 0) or (a == 'f' and i >= 2)

def character(x: Gen):
    a, i = x
    if a == 'K':
        return kap
    if a == 'h':
        return mu if i == 0 else lam if i == 1 else sp.S.Zero
    return sp.S.Zero

def order(x: Gen) -> tuple[int, int, int]:
    a, i = x
    if x == F:
        return 0, 0, 0
    if not is_character(x):
        return {'f': 1, 'e': 2, 'h': 3}[a], i, 0
    return 4, {'h': 0, 'e': 1, 'f': 2, 'K': 3}[a], i

@lru_cache(maxsize=None)
def normal(word: Word) -> dict[Word, sp.Expr]:
    """Canonical PBW normal form of word*u in M (not in a truncated model)."""
    if not word:
        return {(): sp.S.One}
    if is_character(word[-1]):
        c = character(word[-1])
        return {} if c == 0 else scale(c, normal(word[:-1]))
    for i in range(len(word)-1):
        if order(word[i]) > order(word[i+1]):
            x, y = word[i:i+2]
            terms = [normal(word[:i]+(y,x)+word[i+2:])]
            for z, c in bracket(x,y).items():
                terms.append(scale(c, normal(word[:i]+(z,)+word[i+2:])))
            return add(*terms)
    return {word: sp.S.One}

def ad_F(v: dict[Gen, sp.Expr]) -> dict[Gen, sp.Expr]:
    return add(*(scale(c, bracket(F,x)) for x,c in v.items()))

def fraction(pole: int, numerator: Word = ()) -> dict:
    """Construct a vector; this does not define f_0^{-1} as an operator on Q."""
    out = defaultdict(lambda: sp.S.Zero)
    for w, c in normal(numerator).items():
        r = 0
        while r < len(w) and w[r] == F:
            r += 1
        if pole-r >= 1:
            out[(pole-r, w[r:])] += c
    return clean(out)

def act(x: Gen, v: dict) -> dict:
    """x F^{-m} = sum_j binom(m+j-1,j) F^{-m-j} (ad F)^j(x)."""
    out = {}
    for (m, word), c in v.items():
        current = {x: sp.S.One}
        j = 0
        while current:
            for y, a in current.items():
                term = fraction(m+j, (y,)+word)
                out = add(out, scale(c*a*sp.binomial(m+j-1,j),term))
            current = ad_F(current)
            j += 1
    return out

def act_word(word: Word, v: dict) -> dict:
    for x in reversed(word):
        v = act(x,v)
    return v

def substitute(v: dict, **values) -> dict:
    syms = {'mu': mu, 'lambda1': lam, 'kappa': kap}
    sub = {syms[k]:sp.sympify(val) for k,val in values.items()}
    return clean({w:c.subs(sub) for w,c in v.items()})

def T(v: dict[Word, sp.Expr]) -> dict[Word, sp.Expr]:
    """The ACTUAL pi_0 E on F-free PBW numerators (full reordering)."""
    out = {}
    for word, c in v.items():
        out = add(out, scale(c, {w:a for w,a in normal((E,)+word).items() if not w or w[0] != F}))
    return out

# Horizontal-sl2 invariant negative-current quadratic.
Cminus = {
    (('h',-1),('h',-1)): sp.S.One,
    (('f',-1),('e',-1)): sp.Integer(4),
    (('h',-2),): sp.Integer(2),
}

def quadratic(v: dict) -> dict:
    return add(*(scale(c,act_word(word,v)) for word,c in Cminus.items()))

def express(v: dict) -> str:
    return str(v)

CHECKS: list[str] = []
EVIDENCE: dict[str, object] = {}

def check(cond: bool, label: str) -> None:
    if not cond:
        raise AssertionError(label)
    CHECKS.append(label)

def run() -> None:
    w1 = fraction(1)
    # Validate the independent engine against all affine brackets in a small
    # generator set, on nontrivial input words. Generated modes remain unbounded.
    generators = [gen(a,i) for a in ('e','f','h') for i in (-1,0,1)]
    samples = [w1, fraction(2,(('f',-1),('f',1))),
               fraction(1,(('h',-1),('h',-1)))]
    for si, v in enumerate(samples):
        for x,y in combinations(generators,2):
            lhs = add(act(x,act(y,v)), scale(-1,act(y,act(x,v))))
            rhs = add(*(scale(c,act(z,v)) for z,c in bracket(x,y).items()))
            check(lhs == rhs, f'affine bracket on sample {si}: {x},{y}')

    # Counterexample 1: positive F numerator terms survive after localization.
    X = (('f',-1),('f',1))
    actual = act(E,fraction(2,X))
    TX = T({X:sp.S.One})
    predicted = add(*(scale(c,fraction(2,word)) for word,c in TX.items()))
    predicted = add(predicted,scale(-2*(mu-1),fraction(3,X)))
    residual = add(actual,scale(-1,predicted))
    check(residual == scale(-2,w1), 'omitted positive-F term: residual = -2 w1')
    EVIDENCE['E_action_counterexample_residual'] = express(residual)

    # Counterexample 2: quadratic reordering leaves the three-mode lattice.
    h_square = (('h',-1),('h',-1))
    true_T = T({h_square:sp.S.One})
    script_T = {(('e',-1),('h',-1)): sp.Integer(-4)}
    residual = add(true_T,scale(-1,script_T))
    check(residual == {(('e',-2),):sp.Integer(-4)},
          'script truncation: T(h_-1^2) residual = -4 e_-2 u')
    EVIDENCE['truncated_T_counterexample_residual'] = express(residual)

    # Cminus commutes with the horizontal sl2 on test vectors.
    for x in (E,F,H):
        check(act(x,quadratic(w1)) == quadratic(act(x,w1)),
              f'Cminus commutes with {x} on w1')

    # Counterexample 3: P0 is not C*w1 at mu=-2. Display four independent
    # primitive vectors, with distinct maximal numerator degrees 0,2,4,6.
    v = w1
    degrees = []
    for n in range(4):
        v_at = substitute(v,mu=-2)
        check(bool(v_at), f'Cminus^{n} w1 is nonzero')
        for x in (E,F,H):
            check(not substitute(act(x,v),mu=-2), f'Cminus^{n} w1 killed by {x}')
        degree = max(len(word) for _,word in v_at)
        degrees.append(degree)
        check(degree == 2*n, f'Cminus^{n} w1 has maximal numerator degree {2*n}')
        if n == 1:
            EVIDENCE['P0_second_independent_vector'] = express(v_at)
        v = quadratic(v)
    EVIDENCE['P0_distinct_leading_degrees'] = degrees

    # Counterexample 4: a TRUE primitive has top layer not in ker(T^2).
    # At mu=-1, p = lambda1*w1 + F^-2*f1*u is a weight-1 primitive.
    p = add(scale(lam,w1),fraction(2,(('f',1),)))
    check(not substitute(act(E,p),mu=-1), 'weight-1 seed is E-primitive')
    q = quadratic(p)
    q_at = substitute(q,mu=-1)
    check(not substitute(act(E,q),mu=-1), 'Cminus times weight-1 seed is primitive')
    check(max(m for m,_ in q_at) == 2, 'primitive has expected highest pole 2')
    top = {word:c for (m,word),c in q_at.items() if m == 2}
    TTtop = {word:sp.expand(c.subs(mu,-1)) for word,c in T(T(top)).items()}
    TTtop = clean(TTtop)
    check(TTtop == {(('e',-1),):sp.Integer(8)},
          'actual primitive violates proposed T^2 condition by 8 e_-1 u')
    EVIDENCE['true_P1_primitive_top_layer'] = express(top)
    EVIDENCE['T_squared_of_true_primitive_top'] = express(TTtop)

    # The failure of G^{>=2}-stability uses the exact affine central bracket.
    hp, hm = ('h',1), ('h',-1)
    for hr in (hp,hm):
        # At mu=-2, h_r*w1 = -F*e_r*w1 belongs to a horizontal L(2)-block.
        check(not substitute(add(act(hr,w1),act(F,act(('e',hr[1]),w1))),mu=-2),
              f'{hr} w1 is in a horizontal L(2)-block')
    comm = add(act(hp,act(hm,w1)),scale(-1,act(hm,act(hp,w1))))
    check(comm == scale(2*kap,w1), 'two L(2)-block images return 2*kappa*w1')
    EVIDENCE['weight_tail_central_obstruction'] = express(comm)

    # Corrected lowering projection, which the proposed block filtration omits.
    # Test on p=e_-1*w1 (highest weight 2 at mu=-2).
    p2 = act(('e',-1),w1)
    j = 1
    down = add(act(('f',j),p2),
               scale(-sp.Rational(1,2),act(F,act(('h',j),p2))),
               scale(-sp.Rational(1,6),act(F,act(F,act(('e',j),p2)))))
    down_at = substitute(down,mu=-2)
    check(not substitute(act(E,down),mu=-2), 'lowering projection gives an E-primitive')
    check(bool(down_at), 'the omitted P2-to-P0 lowering projection is nonzero')
    EVIDENCE['nonzero_P2_to_P0_projection'] = express(down_at)

    # Rank-one factorization in the valid September 15 proof, checked separately.
    Csym, eta = sp.symbols('C eta')
    for n in range(12):
        A = sp.Rational(1,4**n)*sp.prod(Csym-(eta+2*j)*(eta+2*j+2) for j in range(n))
        B = sp.Rational(1,4**(n+1))*sp.prod(Csym-(eta+2*j)*(eta+2*j+2) for j in range(n+1))
        check(sp.expand(B-(Csym-eta*(eta+2))*A.subs(eta,eta+2)/4) == 0,
              f'rank-one Casimir factorization recurrence n={n}')

    output = {'model':'full affine PBW, no mode cutoff',
              'repository_snapshot':'5f766461cb0a01d171b136b55a64cd1f214886de',
              'checks_passed':len(CHECKS), 'checks':CHECKS, 'evidence':EVIDENCE,
              'scope':'Independent finite exact tests; not formal verification and not an execution of the original repository suite.'}
    target = Path(__file__).with_name('independent_pbw_audit_results.json')
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'PASS: {len(CHECKS)} independent exact checks')
    for name,val in EVIDENCE.items():
        print(f'{name}: {val}')
    print(f'Results: {target}')

if __name__ == '__main__':
    run()
