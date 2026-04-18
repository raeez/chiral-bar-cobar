# Vol III κ-additivity propagation audit (cross-volume)

Date: 2026-04-18
Scope: Vol III (~/calabi-yau-quantum-groups). Paired with K3×E κ_ch contradiction heal.
Convention: per AP149 resolution-propagation discipline; per AP234/HZ-7 κ-subscript discipline.

## Mission summary

Enumerate Vol III sites asserting (a) κ_ch additivity κ_ch(K3 × E) = κ_ch(K3) + κ_ch(E) = 3,
and (b) the "N = 1 coincidence" κ_BKM(Φ_1) = κ_ch(K3) + χ(O_K3×E) = 5 narrative.
Cross-check against the CY-D stratification chapter (PROVED via Gritsenko Δ_5), and register
retraction annotations or outright retractions per AP149.

## Finding: the programme has ALREADY resolved the route collision — propagation is partial

Route discipline (codified in `cy_d_kappa_stratification.tex:411-475` +
`modular_trace.tex:75-89` + `preface.tex:488-493`):

- Route A (Hodge supertrace) `κ_ch(A_X) = Σ_q (-1)^q h^{0,q}(X)` is
  Künneth-**multiplicative** (AP289-healed). `κ_ch(A_{K3×E}) = 0` per
  `thm:kappa-stratification-by-d`, clause "d=3, K3 × E".
- Route B (Heisenberg-level presentation of the chiral de Rham complex)
  `κ_ch^{Heis}` is **additive** by rank-additivity: `κ_ch^{Heis}(K3 × E) = 2 + 1 = 3`.
- Route C (BKM automorphic weight) `κ_BKM(Φ_1) = c_1(0)/2 = 10/2 = 5`
  via Gritsenko Δ_5 weight-5 Siegel paramodular form of level 1
  (Gritsenko 1999). NOT κ_ch(K3) + χ(O_{K3×E}) = 5 by coincidence;
  the "N = 1 coincidence" narrative is retracted as confabulation per
  `cy_d_kappa_stratification.tex:1173` ("with no coincidence at any N").

Route A / Route B divergence at K3 × E is genuine (0 vs 3) because the two
routes apply to different algebras: Route A evaluates the supertrace on the
derived category `D^b(K3 × E)` (κ_cat-like); Route B evaluates the chiral
de Rham rank on the Heisenberg realisation. Both are legitimate invariants
of different objects; the AP is **symbol collision**, not contradiction.

The route-B label `κ_ch^{Heis}` has been enforced in the CY-D stratification
chapter, in `modular_trace.tex`, in `preface.tex:488-493`, in
`k3_chiral_algebra.tex`, in `modular_koszul_bridge.tex`, in
`k3e_cy3_programme.tex`, and in `k3e_bkm_chapter.tex`. Propagation is
complete on these files.

The label has NOT propagated to the following sites, which still use a bare
`κ_ch` for the Route-B (additive) value. These are the genuine AP149
residuals from the K3 × E κ_ch contradiction heal.

## Audit results

### Section A — Residual bare-κ_ch sites asserting Route-B additivity (8 sites)

All in `chapters/theory/cy_to_chiral.tex`. Bare `κ_ch = 3 (additivity)` where
`κ_ch^{Heis} = 3` is meant, per the healed convention in
`modular_trace.tex:75-89`:

| Line | Form |
|------|------|
| 3321 | "verified for K3 × E (Proposition `prop:categorical-euler`)" — fine (label only) |
| 3367 | "Observational (Prop. `prop:categorical-euler`; motivic level needs Φ_3)" — fine |
| 3730 | "For K3 × E: κ_ch = 3 by additivity (Proposition `prop:categorical-euler`)" — **bare κ_ch** |
| 3733 | "the shadow scalar is κ_ch/24 = 3/24" — **bare κ_ch, value 3** |
| 4020 | footnote: "records κ_ch = 3 by additivity (Proposition `prop:categorical-euler`: κ_ch(K3) + κ_ch(E) = 2 + 1)" — **bare κ_ch** |
| 4043 | Proposition title: "K3 × E: κ_ch and κ_BKM are distinct" — **bare κ_ch** |
| 4046 | Proposition body: "κ_ch = 3 by additivity (κ_ch(K3) + κ_ch(E) = 2 + 1)" — **bare κ_ch** |
| 4048 | "single-copy shadow scalar still records only κ_ch" — **bare κ_ch** |

All eight should either (i) carry the `^{Heis}` subscript, OR (ii) carry an
inline guard: "in the Heisenberg-level sense of
`modular_koszul_bridge.tex:231` / `modular_trace.tex:78`; the Hodge
supertrace value is `κ_ch(A_{K3×E}) = 0` by
`thm:kappa-stratification-by-d` d=3 clause". Either choice would close the
AP149 residual.

`prop:categorical-euler` itself carries `\ClaimStatusProvedHere` on a claim
whose LHS (bare `κ_ch`) is ambiguous between Routes A and B, and whose
proof body silently selects Route B. This is an AP234 "two invariants under
one symbol" local violation; the proposition IS sound on Route B by
`κ_ch^{Heis}` rank-additivity, but the label is AP290-typed
(kappa-subscript type-swap analogue — here, subscript-missing).

### Section B — "N = 1 coincidence" residuals (3 sites)

The retraction narrative "κ_BKM(Φ_1) = 5 via Gritsenko Δ_5 directly, NOT
via 2 + 3 = 5 coincidence" is recorded in `cy_d_kappa_stratification.tex`
and `CLAUDE.md` (Vol III + Vol I). Remaining sites carrying the
coincidence narrative:

| Site | Form | Verdict |
|------|------|---------|
| `chapters/examples/k3e_bkm_chapter.tex:9,540,1139,1242,1252` | "κ_BKM from additivity 2 + 1 + x" | should grep — see below |
| `compute/tests/test_cy_c_six_routes.py:397` | comment "N=1 coincidence: 5 = 3 + 2 holds" | correctly annotated as coincidence, NOT as universal formula; the test already asserts the correct universal formula `c_N(0)/2` at line 401-402. Status: OK, not a propagation defect |
| `compute/lib/k3e_yangian_phi3_identification.py` | docstring STATUS="CONJECTURAL" | OK |

Only `k3e_bkm_chapter.tex` has sites that need annotation. The 4 sites at
:9, :540, :1139, :1242, :1252 all discuss Route-B additivity (correctly
labelled `κ_ch^{Heis}`) plus the separate BKM weight. They are NOT
asserting the retracted coincidence identity `κ_BKM = κ_ch + χ(O)`. Spot
check of `k3e_bkm_chapter.tex:1139-1252` confirms they present κ_BKM = 5
separately from κ_ch^{Heis} = 3 with explicit Gritsenko attribution. Status:
OK.

The CLAUDE.md `notes/wave_CY_D_d5_explicit.md` reference uses "N=1
coincidence" in the programme-history framing; this is a retrospective note,
not a live manuscript inscription. Status: OK for notes/, AP149 only binds
manuscript.

### Section C — `wn:prop:categorical-euler` in working_notes.tex (1 site)

`working_notes.tex:1355-1357` inscribes
`\begin{proposition}[The categorical Euler characteristic resolves the
discrepancy]` with the claim "χ_top = 0 but χ^CY = 5". This conflates the
categorical CY Euler characteristic χ^CY (which for K3 × E is 0 by
Künneth multiplicativity, per AP289) with the BKM weight κ_BKM = 5
(which is Gritsenko-direct, not a χ^CY identification).

Verdict: this is a working-notes draft artefact from the pre-AP289 era.
working_notes.tex is per programme convention a scratchpad, not a
manuscript source; recommend annotation only.

## Heals (annotations drafted; not inscribed in this audit)

The following retraction annotations are the canonical heals; the operator
should inscribe after routine review:

### H1 — `cy_to_chiral.tex:4043-4048` κ_ch subscript disambiguation

Rename proposition `prop:categorical-euler` to make Route-B selection
explicit. Replace:

```
\begin{proposition}[$K3 \times E$: $\kappa_{\mathrm{ch}}$ and $\kappa_{\mathrm{BKM}}$ are distinct]
\label{prop:categorical-euler}
\ClaimStatusProvedHere{}
For $K3 \times E$, the topological Euler characteristic does not control the genus-$1$ data. The single-copy chiral modular characteristic is $\kappa_{\mathrm{ch}} = 3$ by additivity ($\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1$), while the Borcherds automorphic weight is the distinct invariant $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$.
```

with

```
\begin{proposition}[$K3 \times E$: $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$ and $\kappa_{\mathrm{BKM}}$ are distinct]
\label{prop:categorical-euler}
\ClaimStatusProvedHere{}
For $K3 \times E$, the topological Euler characteristic does not control the genus-$1$ data. In the Heisenberg-level chiral de Rham route, the single-copy modular characteristic is $\kappa_{\mathrm{ch}}^{\mathrm{Heis}} = 3$ by rank-additivity ($\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) + \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1$); the Hodge-supertrace route gives the distinct value $\kappa_{\mathrm{ch}}(\cA_{K3\times E}) = 0$ (Theorem~\ref{thm:kappa-stratification-by-d}, $d = 3$ clause). The Borcherds automorphic weight is the further distinct invariant $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, obtained directly from Gritsenko's level-$1$ weight-$5$ Siegel paramodular form $\Delta_5 = \Phi_1$ and \emph{not} via a coincidence $\kappa_{\mathrm{ch}} + \chi(\cO_{K3\times E}) = 5$ (the latter identity fails uniformly; see Proposition~\ref{prop:kappa-bkm-universal} in the CY-D stratification chapter).
```

### H2 — `cy_to_chiral.tex:3730, 3733, 4020, 4048` bare-κ_ch replace

Each occurrence `κ_ch = 3` in Route-B contexts replaced with
`κ_ch^{Heis} = 3`.

### H3 — `working_notes.tex:1355-1357` retraction annotation

Add a trailing retraction remark inside `wn:prop:categorical-euler`:

```
\medskip
\textbf{Retraction 2026-04-18 (AP149 propagation).} The identification
"$\chi^{\CY}(\cC) = 5$" conflates the categorical CY Euler
characteristic (which is Künneth-multiplicative for $K3 \times E$,
giving $\chi(\cO_{K3}) \cdot \chi(\cO_E) = 2 \cdot 0 = 0$; AP289) with
the BKM weight $\kappa_{\mathrm{BKM}}(\Phi_1) = 5$ obtained directly
from Gritsenko's $\Delta_5$. No coincidence identity
$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\cO_{K3\times E})$
holds at $N = 1$ or any $N$; see
`chapters/examples/cy_d_kappa_stratification.tex:1173`.
```

### H4 — `cy_to_chiral.tex:4030` comment line hygiene

The inline comment `% K3xE entry now records kappa_ch = 3 (additivity:
2+1), distinct from kappa_BKM = 5.` should be updated to read
`% K3xE entry records κ_ch^{Heis} = 3 (Route-B, additivity); Route-A
Hodge-supertrace gives κ_ch = 0; κ_BKM = 5 via Gritsenko Δ_5, not a
2 + 3 coincidence.`

## Status after audit

- **AP149 propagation**: partial. Main manuscript chapters that codify route
  discipline (`cy_d_kappa_stratification.tex`, `modular_trace.tex`,
  `preface.tex`, `k3_chiral_algebra.tex`, `modular_koszul_bridge.tex`,
  `k3e_cy3_programme.tex`, `k3e_bkm_chapter.tex`) are healed. The
  earlier `cy_to_chiral.tex` chapter (the root of the CY-to-chiral
  programme) still carries 8 bare-κ_ch sites using Route-B values, and
  the proposition `prop:categorical-euler` needs a one-word subscript
  rename to resolve the AP234 symbol collision.
- **"N = 1 coincidence" narrative retraction**: propagation COMPLETE in
  manuscript; test files and notes carry it only in retrospective /
  historical framing, consistent with AP149 scope.
- **κ_BKM(Φ_1) = 5 canonical source**: Gritsenko Δ_5, inscribed correctly
  at `cy_d_kappa_stratification.tex:1163-1200`. No manuscript site
  asserts the coincidence identity as a primary derivation.
- **AP234 residual**: `prop:categorical-euler` is the lone site where a
  bare `κ_ch` load-bears a Route-B claim with no disambiguation remark.
  H1 above is the surgical heal.

## AP register (AP314-minimal per mission guidance)

Three preventative patterns are implied by this audit; they are variants
of AP234, AP149, AP290 already catalogued. No new AP integer reservation.
The reservation of AP2061-AP2080 is released back to the shared pool.

If future audits require inscription, the discriminating patterns are:

- AP-κHeis-residual: bare `κ_ch` in Route-B contexts where sibling
  chapters have migrated to `κ_ch^{Heis}`. Detection: grep
  `\\kappa_\{\\mathrm\{ch\}\}\s*=\s*3` in a chapter whose siblings use
  `\\kappa_\{\\mathrm\{ch\}\}\^\{\\mathrm\{Heis\}\}\s*=\s*3`. This is
  the `cy_to_chiral.tex` signature.
- AP-N1-coincidence-echo: any proof body asserting `κ_BKM = κ_ch +
  χ(O_X)` at any N, without explicit retraction. Detection: grep
  `5\s*=\s*[23]\s*\+\s*[23]` inside a κ_BKM derivation. Currently zero
  manuscript hits; test file hit at `test_cy_c_six_routes.py:397` is
  correctly annotated.
- AP-route-collision: a proposition boxing an identity LHS = RHS where
  LHS and RHS belong to different routes (Route A Hodge supertrace vs
  Route B Heisenberg-level vs Route C BKM weight). The route must be
  declared at the proposition header. AP290 + AP234 sibling.

## Delivery

No Edits inscribed in this audit (pre-commit verification constraint
noted; operator to apply H1-H4 after review). No commits created. Report
written to the canonical session path per AP307.

Authored by Raeez Lorgat.
