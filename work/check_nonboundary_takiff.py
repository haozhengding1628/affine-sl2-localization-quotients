"""Exact finite checks of the two-variable current-algebra subspace.

These tests check formulas and examples, not the infinite-dimensional proofs.
Monomial (q,k) means f_0^q f_1^k u. In the quotient only q<0 survive.
"""
from fractions import Fraction as Q


def clean(v):
    return {key: value for key, value in v.items() if value}


def add(*vs):
    out = {}
    for v in vs:
        for key, value in v.items():
            out[key] = out.get(key, Q(0)) + value
    return clean(out)


def scale(v, s):
    return clean({key: value * s for key, value in v.items()})


def act(name, v, lam0, lam1, quotient=True):
    out = {}
    for (q, k), value in v.items():
        terms = {
            "f0": [(q + 1, k, 1)],
            "f1": [(q, k + 1, 1)],
            "h0": [(q, k, lam0 - 2*q - 2*k)],
            "h1": [(q, k, lam1), (q - 1, k + 1, -2*q)],
            "e0": [(q - 1, k, q*(lam0-q+1-2*k)),
                   (q, k - 1, k*lam1)],
            "e1": [(q - 1, k, q*lam1),
                   (q - 2, k + 1, -q*(q-1))],
        }[name]
        for nq, nk, coefficient in terms:
            if coefficient and nk >= 0 and (not quotient or nq < 0):
                out[nq, nk] = out.get((nq, nk), Q(0)) + value*coefficient
    return clean(out)


def power(name, v, n, p, lam1, quotient=True):
    for _ in range(n):
        v = act(name, v, p, lam1, quotient)
    return v


def main():
    checks = 0
    # All nontrivial brackets of the six Takiff generators.
    relations = [
        ("h0", "e0", "e0", 2), ("h0", "e1", "e1", 2),
        ("h0", "f0", "f0", -2), ("h0", "f1", "f1", -2),
        ("h1", "e0", "e1", 2), ("h1", "f0", "f1", -2),
        ("e0", "f0", "h0", 1), ("e0", "f1", "h1", 1),
        ("e1", "f0", "h1", 1),
        ("e0", "e1", None, 0), ("f0", "f1", None, 0),
        ("h0", "h1", None, 0), ("h1", "e1", None, 0),
        ("h1", "f1", None, 0), ("e1", "f1", None, 0),
    ]
    for p in [Q(-4), Q(-1), Q(0), Q(3), Q(1, 2)]:
        for lam1 in [Q(0), Q(1), Q(3, 2)]:
            for m in range(1, 6):
                for k in range(5):
                    v = {(-m, k): Q(1)}
                    for x, y, z, factor in relations:
                        left = add(
                            act(x, act(y, v, p, lam1), p, lam1),
                            scale(act(y, act(x, v, p, lam1), p, lam1), -1),
                        )
                        right = {} if z is None else scale(act(z, v, p, lam1), factor)
                        assert left == right, (p, lam1, m, k, x, y)
                        checks += 1
    # Integral parameters: construct an e0-highest numerator v_k.
    for p in range(-7, 8):
        k = max(1, p + 2)
        for lam1 in [Q(0), Q(1), Q(3, 2)]:
            coeff = Q(1)
            highest = {(0, k): coeff}
            for j in range(1, k + 1):
                coeff *= -(k-j+1)*lam1 / Q(j*(p-2*k+j+1))
                highest[j, k-j] = coeff
            highest = clean(highest)
            assert not act("e0", highest, p, lam1, quotient=False)
            residue = clean({(q-1, ell): value for (q, ell), value in highest.items() if q == 0})
            assert residue == {(-1, k): Q(1)}
            n = 2*k-p-1
            assert power("e0", residue, n-1, p, lam1)
            assert not power("e0", residue, n, p, lam1)
            m0 = max(1, -p)
            assert power("e0", {(-m0, 0): Q(1)}, 15, p, lam1)
            checks += 5
    # The natural cyclic vector has a resonance precisely at p=-s, s>=2.
    for s in range(2, 10):
        assert power("e0", {(-1, 0): Q(1)}, s-2, -s, Q(1))
        assert not power("e0", {(-1, 0): Q(1)}, s-1, -s, Q(1))
        checks += 2
    print(f"PASS: {checks} exact finite checks; no truncation in monomial degree.")


if __name__ == "__main__":
    main()
