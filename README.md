# affine-sl2-localization-quotients

Boundary and nonboundary **localization quotients** of smooth modules over the
affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_2$ (without the degree
derivation). This repository is a working archive of research notes, their
symbolic verification scripts, and an LLM-review (Danus) trial. All results
are research drafts, not peer-reviewed publications.

## What is studied

Let $\mathfrak g=(\mathfrak{sl}_2\otimes\mathbb C[t,t^{-1}])\oplus\mathbb CK$
with the standard brackets, and let
$M_{a,b}(\chi)=U(\mathfrak g)\otimes_{U(S_{a,b})}\mathbb C_\chi$ be the
smooth induced modules of Futorny--Guo--Xue--Zhao. For a root mode $F=f_c$
acting injectively, the localization quotient is
$\mathcal T_FM=D_FM/M$, $D_FM=U[F^{-1}]\otimes_UM$.

### Established results

- **Boundary case** ($F=f_b$, $\lambda_L\ne0$): PBW well-definedness and the
  isomorphism $\mathcal T_{f_b}M_{a,b}(\chi)\cong M_{a+1,b-1}(\chi^+)$,
  iterated boundary moves, and the derivation (degree operator) version.
- **Nonboundary case** ($F=f_c$, $c<b$): PBW models, the gap invariant of
  locally nilpotent root modes, weight structure, cyclicity, annihilator
  preservation, and derived-functor properties of $\mathcal T_F$.
- **Deep region** ($c\le-a-1$): the exact simplicity criterion
  $\mathcal T_{f_c}M_{a,b}$ simple $\iff\lambda_0-c\kappa\notin\mathbb Z$
  (under $\lambda_L\ne0$, $\kappa\ne-2$), the unique maximal submodule $G_c$
  at integral parameters with simple head $Q_c/G_c$ and nonsplit extension,
  and the compatibility of algebraic central reduction with quotient
  localization.
- **Structure of the locally nilpotent part** $G_c$: the transverse
  $\mathfrak{sl}_2$-decomposition
  $G_c\cong\bigoplus_{\nu\ge0}P_\nu\otimes L(\nu)$ and the corrected
  primitive recursion through the full E-action components $A_r$. **The
  internal classification of $G_c$ (simplicity, socle, composition length)
  is OPEN**: an independent audit of 2026-09-22 found counterexamples to
  earlier claims about the primitive space, $P_0$, and a weight filtration;
  those claims have been withdrawn (see below).

### Audit and correction history

- `audits/2026-09-22/` — independent audit (report + a PBW checker with 154
  exact checks). It disproved: the $A_0$-only E-action formula (counterexample
  $Ef_0^{-2}f_{-1}f_1u$ contains $-2w_1$), the description
  $P_\nu\cong\{X:T^{\nu+1}(X)u=0\}$ (the $Z$-counterexample), the claim
  $P_0=\mathbb Cw_1$ at $\mu=-2$ (the infinite family $Z^nw_1$), and the
  statement that the weight tails $G^{\ge\nu}$ are affine submodules
  ($[h_1,h_{-1}]w_1=2\kappa w_1$ and the nonzero lowering projection
  $\ell_1$). The audit did **not** disprove the boundary isomorphism, the
  deep-region simplicity criterion, or the unique-maximal-submodule theorem.
- `outputs/gc_structure_advisor_en.{tex,pdf}` and
  `outputs/gc_structure_research_cn.{tex,pdf}` are the corrected notes: they
  record the corrected E-action, the corrected triangular recursion, the
  complete projection set including the lowering map
  $\ell_j:P_\nu\to P_{\nu-2}$, and withdraw the weight-filtration
  consequences.
- `work/check_audit_regressions.py` reproduces the four classes of
  counterexamples (24 exact checks).

## Repository layout

```
outputs/       canonical notes (.tex + compiled .pdf, EN and CN)
  boundary_localization_pbw_general_note_*_well_defined  (PBW well-definedness)
  boundary_localization_advisor_note_*                   (advisor-style boundary note)
  boundary_derivation_extension_*                       (derivation extension)
  nonboundary_localization_results_en                   (nonboundary quotients)
  localization_quotients_unified_*                      (unified note, EN/CN)
  localization_quotients_additional_progress_en         (addendum: deep-region
                                                         simplicity, unique maximal
                                                         submodule, central reduction)
  gc_structure_advisor_en                               (structure of G_c, corrected)
  gc_structure_research_cn                              (structure of G_c, CN, corrected)
  v8_boundary_iterated_flows_en                         (living note v8)
  danus_* / reply_to_author_en.txt                      (review artifacts)
audits/        independent audits
  2026-09-22/  audit report, independent PBW checker, results, log
work/          symbolic verification and regression scripts
  check_addendum_AB.py, check_addendum_C.py, check_addendum_D.py
  check_gc_filter.py, check_gc_sanity.py, check_nonboundary_takiff.py
  check_audit_regressions.py
  danus-runs/                                           (fact graph, verdicts, manifests)
danus_trial/   bounded Windows adaptation of the Danus LLM-review gate
```

## Verification status

The addendum's key formulas were checked with exact symbolic computation
(SymPy): 1,533 checks for the rank-one machinery and the two-variable model,
2,337 for the critical-level Sugawara and the smoothness formulas, and 568
for the central-reduction toy model. Two boundary facts were accepted into a
genuine Danus fact graph (IDs `d6bf6fef62dc8971`, `b388fabb701946d3`) through
an independent LLM verifier. The 2026-09-22 audit added 154 independent exact
checks and found the errors documented above. These are corroborations,
**not** peer review or formal (Lean/Coq) verification.

## Compiling the notes

XeLaTeX (TeX Live 2023):

```sh
cd outputs
xelatex -interaction=nonstopmode gc_structure_advisor_en.tex
```

## Third-party components

The Danus trial (`danus_trial/`) wraps upstream
[frenzymath/Danus](https://github.com/frenzymath/Danus), release
`v0.1.0-codex` (Apache-2.0), which is **not** vendored in this repository;
see `danus_trial/README.md` for the adaptation notes and how to obtain the
upstream checkout.

## License

[MIT](LICENSE).
