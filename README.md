# affine-sl2-localization-quotients

Boundary and nonboundary **localization quotients** of smooth modules over the
affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_2$ (without the degree
derivation). This repository is a working archive of research notes, their
symbolic verification scripts, and an LLM-review (Danus) trial.

## What is studied

Let $\mathfrak g=(\mathfrak{sl}_2\otimes\mathbb C[t,t^{-1}])\oplus\mathbb CK$
with the standard brackets, and let
$M_{a,b}(\chi)=U(\mathfrak g)\otimes_{U(S_{a,b})}\mathbb C_\chi$ be the
smooth induced modules of Futorny--Guo--Xue--Zhao. For a root mode $F=f_c$
acting injectively, the localization quotient is
$\mathcal T_FM=D_FM/M$, $D_FM=U[F^{-1}]\otimes_UM$.

Main results:

- **Boundary case** ($F=f_b$): PBW well-definedness and the isomorphism
  $\mathcal T_{f_b}M_{a,b}(\chi)\cong M_{a+1,b-1}(\chi^+)$, together with
  iterated boundary moves and the derivation (degree operator) version.
- **Nonboundary case** ($F=f_c$, $c<b$): PBW models, the gap invariant of
  locally nilpotent root modes, weight structure, cyclicity, annihilator
  preservation, and derived-functor properties of $\mathcal T_F$.
- **Deep region** ($c\le-a-1$): the exact simplicity criterion
  $\mathcal T_{f_c}M_{a,b}$ simple $\iff\lambda_0-c\kappa\notin\mathbb Z$
  (under $\lambda_L\ne0$, $\kappa\ne-2$), the unique maximal submodule at
  integral parameters, and the compatibility of critical central reduction
  with quotient localization.
- **Structure of the locally nilpotent part** $G_c$: an
  $\mathfrak{sl}_2$-decomposition $G_c\cong\bigoplus_{\nu\ge0}P_\nu\otimes
  L(\nu)$, an exact description of the primitive spaces $P_\nu$ by a
  top-layer condition $T^{\nu+1}(X)u=0$, and a canonical **weight filtration**
  $G_c=G^{\ge\nu_0}\supsetneq G^{\ge\nu_0+1}\supsetneq\cdots$ with simple
  quotients $P_\nu^{(q)}\otimes L(\nu)$ and one trivial quotient at weight
  zero. Consequently $G_c$ is never simple, $\operatorname{soc}(G_c)=0$ (and
  $\operatorname{soc}(Q_c)=0$), and its composition length is infinite; in
  the shallow region $G_c=0$.

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
  gc_structure_advisor_en                               (structure of G_c, advisor style)
  gc_structure_research_cn                              (structure of G_c, CN)
  v8_boundary_iterated_flows_en                         (living note v8)
  danus_* / reply_to_author_en.txt                      (review artifacts)
work/          symbolic verification scripts and the Danus run artifacts
  check_addendum_AB.py, check_addendum_C.py, check_addendum_D.py
  check_gc_filter.py, check_gc_sanity.py, check_nonboundary_takiff.py
  danus-runs/                                           (fact graph, verdicts, manifests)
danus_trial/   bounded Windows adaptation of the Danus LLM-review gate
```

## Verification status

The key formulas of the addendum were checked with exact symbolic
computation (SymPy): 1,533 checks for the rank-one machinery and the
two-variable model, 2,337 for the critical-level Sugawara and the smoothness
formulas, and 568 for the central-reduction toy model; the $G_c$-structure
identities have additional focused checks. Two boundary facts were accepted
into a genuine Danus fact graph (IDs `d6bf6fef62dc8971`,
`b388fabb701946d3`) through an independent LLM verifier. These are
corroborations, **not** peer review or formal (Lean/Coq) verification; the
notes are research drafts.

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
