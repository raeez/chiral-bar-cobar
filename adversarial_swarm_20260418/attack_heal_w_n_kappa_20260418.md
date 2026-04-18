# Attack+Heal: Principal W_N κ formula + K(W_N) complementarity

**Date:** 2026-04-18
**Author:** Raeez Lorgat
**Target:** CLAUDE.md C4 principal W_N κ; HZ-4 AP136 harmonic-number off-by-one
  discipline; K(W_N) = 2·c_self-dual prediction from the dual-level audit.

## Mission (brief)

1. Grep Vol I for every κ(W_N) inscription + every H_N, H_{N-1}, harmonic-number
   invocation relevant to principal W_N κ.
2. Confirm each κ(W_N) site uses c·(H_N − 1), never c·H_{N-1} (AP136 forbidden
   form) and never c·H_N − 1 (parenthesization drift).
3. Numerical cross-check at N=2 (→ c/2 = κ_Vir) and N=3 (→ 5c/6), confirming
   H_N − 1 is computed correctly and no site uses the off-by-one H_2 − 1 = 1.
4. Audit the K(W_N) = c(W_N) + c(W_N^!) = 2(N−1)(2N²+2N+1) = 4N³ − 2N − 2
   census value against the prediction K(W_N) = 2·c_self-dual(W_N) for
   N = 2, 3, 4, 5, 6.

## Phase 1. κ(W_N) formula — coverage

Grep scope: every `\kappa(\cW_N)`, `\kappa(W_N)`, `\kappa^{W_N}`, plus prose
forms referring to principal W_N κ. ~30 hits across Vol I chapters,
standalones, appendices, surveys.

**Canonical form, used universally:** κ(W_N) = c · (H_N − 1) with
H_N = ∑_{j=1}^{N} 1/j.

Inscribed verbatim at:
* `chapters/examples/w_algebras_deep.tex:45,2211`
* `chapters/examples/w_algebras.tex:26` (with explicit AP136 warning at :39)
* `chapters/examples/w3_composite_fields.tex:20`
* `chapters/examples/minimal_model_fusion.tex:49`
* `chapters/frame/preface.tex:103,3387`
* `chapters/frame/part_iii_platonic_introduction.tex:212,366`
* `chapters/theory/shadow_tower_other_class_M_platonic.tex:363,374–381`
  (with spin-stratified form κ_{W_s}(W_N)(c) = c/s, summed 2..N → c(H_N − 1))
* `chapters/theory/chiral_climax_platonic.tex:365`
* `chapters/theory/higher_genus_modular_koszul.tex:3575`
* `chapters/theory/universal_conductor_K_platonic.tex:44`
* `chapters/theory/shadow_tower_quadrichotomy_platonic.tex:147`
* `chapters/theory/introduction.tex:432`
* `chapters/theory/motivic_shadow_full_class_m_platonic.tex:223` (κ_j form)
* `standalone/N6_shadow_formality.tex:424`
* `standalone/N3_e1_primacy.tex:1194–1195` (with AP136 warning)
* `standalone/chiral_chern_weil.tex:1063,1078–1080,1411` (explicit
  AP136 note: "H_{N-1} ≠ H_N − 1. At N=2: H_1 = 1 but H_2 − 1 = 1/2.")
* `standalone/multi_weight_cross_channel.tex:135,158` (with AP1 comment)
* `standalone/five_theorems_modular_koszul.tex:932–933,2182–2189,2582–2584`
  (with AP136 comment)
* `standalone/koszulness_fourteen_characterizations.tex:2070`
* `standalone/sc_chtop_pva_descent.tex:1455`
* `standalone/shadow_towers.tex:1552`
* `standalone/shadow_towers_v3.tex:3113`
* `standalone/survey_modular_koszul_duality.tex:2562`
* `compute/audit/standalone_paper/paper.tex:711`

No site uses the AP136 forbidden form c·H_{N-1}. No site uses the
parenthesization drift c·H_N − 1 (i.e. c·H_N subtracted by 1 at the top level).

Every `H_{N-1}` match across the repo falls into one of three categories,
none of which is an AP136 violation:
* (a) Explicit anti-pattern warnings: `w_algebras.tex:39`,
  `standalone/N3_e1_primacy.tex:1195`, `standalone/chiral_chern_weil.tex:1078`,
  `standalone/survey_modular_koszul_duality_v2.tex:2901`,
  `tmp_standalone_audit/survey_v2_xr.tex:1623`,
  `chapters/theory/higher_genus_modular_koszul.tex:3579`,
  `standalone/five_theorems_modular_koszul.tex:2189`.
* (b) A different object: H_{N−1}(u) and H_{N−1}(u−1) in
  `w_algebras_deep.tex:4911–4912` and `connections/genus_complete.tex:1935–2193`
  are shifted-index Hurwitz polynomials attached to super-Yangian transfer
  matrices, not harmonic numbers in κ(W_N).
* (c) The Heisenberg algebra `\cH_{N-1}` of rank N−1 in
  `standalone/seven_faces.tex:1154–1157`.

## Phase 2. Numerical N=2 and N=3 checks

N=2: H_2 = 1 + 1/2 = 3/2, H_2 − 1 = 1/2, κ(W_2) = c·(1/2) = c/2 = κ_Vir. ✓

N=3: H_3 = 1 + 1/2 + 1/3 = 11/6, H_3 − 1 = 5/6, κ(W_3) = 5c/6. ✓

`preface.tex:3387` explicitly writes this: "$\kappa(\cW_3) = 5c/6$ (from
$\kappa(\cW_N) = c(H_N-1)$ at N = 3)". The off-by-one error H_2 − 1 = 1
(which would spuriously give κ(W_2) = c) appears nowhere in the manuscript
outside the anti-pattern warnings. Zero violations of AP136.

## Phase 3. K(W_N) = 2·c_self-dual prediction

The mission proposes: K(W_N) = 2·c_self-dual(W_N), with c_self-dual the fixed
point of the Feigin–Frenkel involution c ↦ K_N − c, i.e. c_self-dual = K_N/2.
The prediction K = 2·c_self-dual is therefore a tautology once c_self-dual =
K_N/2 is given (and it is — `landscape_census.tex:940`,
`higher_genus_complementarity.tex:3038`, `ordered_associative_chiral_kd.tex:6276`
all inscribe c^* = K_N/2 explicitly).

The non-tautological content is: the specific closed form

  K_N = 2(N − 1)(2N² + 2N + 1) = 4N³ − 2N − 2,

and the prediction K(W_2) = 26, K(W_3) = 100, K(W_4) = 246, K(W_5) = 488,
K(W_6) = 850.

**Census value** (inscribed at `landscape_census.tex:938–941,1520–1522`):

  K_N = 4N³ − 2N − 2, K_2 = 26, K_3 = 100, K_4 = 246, K_5 = 488.

Hand-check N=6: 4·216 − 12 − 2 = 864 − 14 = 850. ✓

All six predicted values match the inscribed census. No drift.

Arithmetic cross-check via the dual-level complementarity table at
`higher_genus_foundations.tex:6996–7006`:

| N | ϱ = H_N − 1 | K_N | κ + κ' = ϱ·K_N |
|---|-------------|-----|----------------|
| 2 | 1/2 | 26 | 13 |
| 3 | 5/6 | 100 | 250/3 |
| 4 | 13/12 | 246 | 533/2 |
| 5 | 77/60 | 488 | 9394/15 |

Verification: 13·246/12 = 3198/12 = 533/2 ✓. 77·488/60 = 37576/60 = 9394/15 ✓.
All rows self-consistent. H_5 = 137/60, H_5 − 1 = 77/60 ✓.

Self-dual central charges c^* = K_N/2: c^*_2 = 13, c^*_3 = 50, c^*_4 = 123,
c^*_5 = 244, c^*_6 = 425. `landscape_census.tex:940` inscribes c^* = 13
(Vir), 50 (W_3), 123 (W_4) explicitly.

## Phase 4. K(W_N) inscription discipline — zero drift

Every K(W_N) inscription in Vol I uses either 2(N−1)(2N²+2N+1) or the
expanded 4N³−2N−2; the two are equal and both appear. No site uses a
different leading coefficient, wrong cubic prefactor, or shifted-index
error.

Sites:
* `chapters/examples/landscape_census.tex:938–939,1520–1522`
* `chapters/examples/w_algebras_deep.tex:668,671,918,2449,2478,4132`
* `chapters/examples/w3_holographic_datum.tex:276,318,738`
* `chapters/frame/preface.tex:2738`
* `chapters/connections/frontier_modular_holography_platonic.tex:5405`
* `chapters/connections/outlook.tex:581`
* `chapters/theory/higher_genus_foundations.tex:6996`
* `chapters/theory/higher_genus_modular_koszul.tex:8992,21710–21738`
* `chapters/theory/higher_genus_complementarity.tex:3034,3064,3266,3269`
* `chapters/theory/universal_conductor_K_platonic.tex:646–697`
* `chapters/theory/kappa_conductor.tex:231–256`
* `chapters/theory/chiral_climax_platonic.tex:892`
* `appendices/nonlinear_modular_shadows.tex:3919`
* `appendices/ordered_associative_chiral_kd.tex:6274–7928`
* `standalone/classification.tex:735,748`
* `standalone/shadow_towers_v3.tex:2259`
* `standalone/survey_modular_koszul_duality.tex:2562`
* `standalone/survey_modular_koszul_duality_v2.tex:1271,5011`
* `standalone/survey_track_a_compressed.tex:1432`
* `standalone/w3_holographic_datum.tex:256`

## Findings

**No heal required.** The manuscript is internally consistent at the κ(W_N)
and K(W_N) level:
* κ(W_N) = c·(H_N − 1) is the only form in use.
* AP136 is actively policed by anti-pattern warnings in five standalones
  and two chapters.
* K(W_N) = 4N³ − 2N − 2 matches 2·c_self-dual at N = 2, 3, 4, 5, 6.
* Dual-level κ + κ' = (H_N − 1)·K_N arithmetic self-consistent through N = 5.

The CLAUDE.md Wave-1 audit note "K(W_N) for N ≥ 4 — Vol I census carries
no entry for the Koszul conductor" is stale: `landscape_census.tex:938`
explicitly writes K_4 = 246, and the general closed form K_N = 4N³−2N−2
was inscribed long before the audit note. The frontier item, if it stands,
is narrower: the derivation of K_N = 4N³−2N−2 from first principles
(BRST ghost content / principal DS bc-tower) as opposed to its Feigin–Frenkel
fixed-point characterisation. That derivation IS inscribed at
`chapters/theory/universal_conductor_K_platonic.tex:646–697` via the
spin-tower sum K(W_N) = ∑_{j=2}^{N} 2(6j² − 6j + 1), whose closed form is
4N³ − 2N − 2 (third forward difference Δ³ = 24, as noted at :649 and
`kappa_conductor.tex:236`).

**CLAUDE.md stale-frontier candidate for removal:** Wave-1 audit 2026-04-17
open-frontier bullet "**K(W_N) for N ≥ 4** — Vol I census carries no entry".
Replace with: CLOSED. `landscape_census.tex:938–939,1520–1522` inscribes
K_N = 4N³ − 2N − 2 with K_4 = 246, K_5 = 488; spin-tower derivation at
`universal_conductor_K_platonic.tex:646–697`; dual-level κ+κ' = ϱ_N·K_N
complementarity table at `higher_genus_foundations.tex:6996–7006` for
N = 2, 3, 4, 5. The ϱ_BP structural-origin bullet on the same audit line
(Wave-1 F1.b) is the remaining open item in that audit cluster; the W_N
half is closed.

## Minimal AP inscription

Per AP314 (inscription-rate discipline) and the mission's explicit "minimal"
instruction: no new APs inscribed. The audit confirmed existing AP136
discipline is airtight; no new failure mode surfaced.

## Audit trail

* Grep scope: Vol I (chapters/, standalones/, appendices/, compute/audit/,
  tmp_standalone_audit/). Not Vol II, not Vol III — mission scope was Vol I.
* Zero manuscript edits. Zero CLAUDE.md edits (the stale-frontier note is
  flagged above for future CLAUDE.md hygiene but not touched here, to avoid
  AP304 concurrent-edit collisions with sibling swarms in this cron
  iteration).
* Zero commits.
