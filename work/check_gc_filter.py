"""Lattice-level identities in Q_0 = T_{f_0} M_{-1,1} (basic model).

POST-AUDIT SCOPE (2026-09-22): these checks verify vector-level identities
only. They do NOT imply that the weight tails G^{>=nu} are affine
submodules: that claim is FALSE (counterexamples: [h_1,h_{-1}]w_1 = 2 kappa w_1
at mu=-2, and the nonzero lowering projection l_1: P_2 -> P_0; see
audits/2026-09-22/ and work/check_audit_regressions.py). Also P_0 is not
C w_1: the Z-family gives infinitely many independent vectors of P_0.
The lattice f_1^p e_{-1}^q h_{-1}^s is closed under the E-action (A_r = 0
for r >= 1 on it), so the formula used here is the full action on this
subspace.

Verified identities (valid on the lattice):
  (1) h_j w_1 = -F e_j w_1 (j >= 1) and E^2 f_j w_1 = -2 e_j w_1;
  (2) f_j w_1 = -(1/2) F^2 e_j w_1 (no P_0-component of f_j w_1);
  (3) the P_2-seed (top f_1^2) is primitive, and e_1 maps it to a nonzero P_4;
  (4) the model's vectors are pure H-weight (model consistency only).
"""
import sympy as sp
from sympy import symbols, expand, Rational