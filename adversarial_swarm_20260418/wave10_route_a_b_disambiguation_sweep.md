# Wave-10 Route A / Route B κ_ch(K3×E) Disambiguation Sweep

**Date:** 2026-04-18
**Scope:** Vol III programme-wide (`chapters/`, `standalone/`, `appendices/`, `main.tex`)
**Charter:** classify every κ_ch(K3×E) site as Route A / Route B / Ambiguous per the
canonical disambiguation at `cy_d_kappa_stratification.tex:411-426, 448-452`.
**Mission constraint:** disambiguation comments and value corrections only;
no commits; Wave-6 retraction agent's precedent respected (refuse silent patches).

## 0. Canonical disambiguation (reference)

At `chapters/examples/cy_d_kappa_stratification.tex`:
- `:411-426`: κ_ch(Φ_1(D^b(E))) = 0 is canonical (Route A, Hodge supertrace
  via `thm:kappa-hodge-supertrace-identification`). κ_ch(H_1) = 1 is the
  Heisenberg level k (Route B, free-boson lattice of rank 1, "outside the
  Φ_d functor").
- `:448-452`: κ_ch(A_{K3×E}) = Ξ(K3×E) = 0 via Künneth-multiplicative
  Hodge supertrace on column (1,1,1,1).

## 1. Programme-wide grep result

`grep -rn 'K3 \\times E' chapters/ standalone/ appendices/ main.tex`:
**107 hits in chapters+standalones (notes/ and working_notes.tex excluded).**

File distribution (top 20 after filtering notes/ + metadata/):
```
17 chapters/theory/cy_to_chiral.tex
11 chapters/examples/k3e_cy3_programme.tex
11 chapters/examples/k3_chiral_algebra.tex
10 chapters/examples/k3e_bkm_chapter.tex
 8 chapters/theory/quantum_chiral_algebras.tex
 8 chapters/theory/modular_trace.tex
 7 chapters/connections/modular_koszul_bridge.tex
 5 main.tex
 4 chapters/theory/introduction.tex
 4 chapters/theory/cy_categories.tex
 4 chapters/examples/cy_c_six_routes_convergence.tex
 3 chapters/examples/quantum_group_reps.tex
 2 chapters/theory/braided_factorization.tex
 2 chapters/frame/preface.tex
 2 chapters/examples/k3_yangian_chapter.tex
 1 standalone/k3e_cy3_programme_vol3.tex
 + 10 more at 1 hit each
```

Of these, `~40` sites carry the literal value `κ_ch(K3×E) = 3` or the
"additivity" identity `2 + 1 = 3` attached to a chiral modular
characteristic. `~5` sites carry `κ_ch(K3×E) = 0` (Hodge-supertrace
Route A).

## 2. Load-bearing programme contradiction surfaced

The sweep uncovers a genuine inscribed contradiction between two
programme anchors, rather than a simple disambiguation-comment gap:

### Anchor A (Hodge supertrace, Wave-4 CY-D heal)
- `cy_d_kappa_stratification.tex:448-452` (`thm:kappa-stratification-by-d`,
  ClaimStatusProvedHere): κ_ch(A_{K3×E}) = 0.
- `cy_c_six_routes_convergence.tex:453`: "Writing κ_ch^{R_i} ∈ {3, 12, 24}
  confuses a purely algebraic invariant (ρ^{R_i} = generator lattice rank)
  with the Hodge-supertrace (κ_ch = 0)."
- `cy_c_six_routes_convergence.tex:425`: "five distinct invariants
  {κ_ch = 0, κ_cat = 0, κ_fiber = 24, ρ^{R_i} ∈ {3, 12, 24}, κ_BKM = 5}".

### Anchor B (chiral modular characteristic = additive, pre-Wave-4)
- `cy_to_chiral.tex:267` (`conj:cy-kappa-identification` Clause (ii),
  ClaimStatusConjectured): "For product CY_3 of the form S × E:
  κ_ch(A_C) = κ_ch(A_S) + κ_ch(A_E) (additivity)."
- `cy_to_chiral.tex:277` (`rem:cy-kappa-evidence`): "κ_ch is additive
  under products ... K3×E: κ_ch = 2 + 1 = 3 (additive) vs.
  χ(O_{K3×E}) = 2·0 = 0 (multiplicative)."
- `cy_to_chiral.tex:293-342` (`prop:beauville-kappa-formula`,
  ClaimStatusProvedHere): "Product CY_3 (h^{1,0} > 0): κ_ch =
  h^{3,0}(X) + 2 (proved by additivity and the d ≤ 2 result)." Proof
  body: "κ_ch(K3×E) = χ(O_{K3}) + h^{1,0}(E) = 2 + 1 = 3."
- `k3_chiral_algebra.tex:506` (inside proposition body,
  ClaimStatusProvedHere): "κ_ch(K3×E) = κ_ch(K3) + κ_ch(E) = 2+1 = 3
  (additivity of the chiral modular characteristic under products)."

Anchors A and B assign different values (0 vs 3) to the same symbol
κ_ch(A_{K3×E}) under the same Φ_d functor hypothesis. This is an AP289
(Künneth-multiplicative vs additive) top-level violation at the chapter-
scale rather than at the site scale. Both anchors carry
ClaimStatusProvedHere.

## 3. Classification table (top 40 sites)

Format: `file:line` — value — context — verdict

Route A (Hodge-supertrace / Φ_d functor):
```
cy_d_kappa_stratification.tex:452    0    Φ_d supertrace           correct
cy_d_kappa_stratification.tex:421    0    Φ_1(D^b(E)) canonical    correct
cy_c_six_routes_convergence.tex:425  0    pentagon Route A         correct
cy_c_six_routes_convergence.tex:453  0    pentagon audit prose     correct
quantum_chiral_algebras.tex:1741     0    κ_cat(K3×E) via Künneth  correct (κ_cat)
k3_chiral_algebra.tex:508            0    κ_cat(K3×E) via Künneth  correct (κ_cat)
k3_chiral_algebra.tex:512            0    χ(O_{K3×E}) = 0          correct
k3e_bkm_chapter.tex (multiple)       0    κ_cat via Künneth         correct (κ_cat)
rem:three-kappa-k3xe:1117            0    κ_cat(K3×E) = 0 explicit correct (κ_cat)
```

Route B ("chiral modular characteristic" additive, programme-internal):
```
cy_to_chiral.tex:270                 3    conj:cy-kappa-ident (ii)      AP289 vs Anchor A
cy_to_chiral.tex:280                 3    rem:cy-kappa-evidence         AP289 vs Anchor A
cy_to_chiral.tex:322                 3    prop:beauville table          AP289 vs Anchor A
cy_to_chiral.tex:334                 3    proof of Beauville            AP289 vs Anchor A
cy_to_chiral.tex:3374                3    proof caveats                 AP289 vs Anchor A
cy_to_chiral.tex:3606                3    product CY_3 list             AP289 vs Anchor A
cy_to_chiral.tex:3713                3    "by additivity"               AP289 vs Anchor A
cy_to_chiral.tex:3991                3    grand-atlas table             AP289 vs Anchor A
cy_to_chiral.tex:4003                3    table footnote "by additivity" AP289 vs Anchor A
cy_to_chiral.tex:4029                3    "single-copy chiral mchar"    AP289 vs Anchor A
k3_chiral_algebra.tex:506            3    "(Proved.) additivity"        AP289 vs Anchor A
k3e_cy3_programme.tex:334            3    dim_C(K3×E) = 3              AP289 vs Anchor A
k3e_cy3_programme.tex:1827           3    dim_C identification          AP289 vs Anchor A
k3e_cy3_programme.tex:3006           3    dim_C(K3×E)                  AP289 vs Anchor A
k3e_cy3_programme.tex:3052           3    "κ_ch(K3)+κ_ch(E)=2+1=3"     AP289 vs Anchor A
k3e_bkm_chapter.tex:980              3    shadow-scattering bridge      AP289 vs Anchor A
k3e_bkm_chapter.tex:1137             3    "= dim_C, verified"           AP289 vs Anchor A
k3e_bkm_chapter.tex:1140             3    "κ_ch(K3×E) = 3"              AP289 vs Anchor A
k3e_bkm_chapter.tex:1250             3    modular characteristic        AP289 vs Anchor A
k3e_bkm_chapter.tex:1352             3    disambiguation against κ_fiber AP289 vs Anchor A
quantum_chiral_algebras.tex:891      3    κ_ch-additivity               AP289 vs Anchor A
quantum_chiral_algebras.tex:1643     3    "Route D gives κ_ch=3"        AP289 vs Anchor A
quantum_chiral_algebras.tex:1741     3    five κ_• tower {0,2,3,5,24}   AP289 vs Anchor A
modular_koszul_bridge.tex:231        3    "by additivity"               AP289 vs Anchor A
braided_factorization.tex:958        3    "κ_ch(A_{K3×E}) = 3 under Künneth"   AP289 (note claim) vs Anchor A
braided_factorization.tex:984        3    total-space κ_ch              AP289 vs Anchor A
braided_factorization.tex:1219       3    total-space invariant         AP289 vs Anchor A
braided_factorization.tex:1762       3    total-space                   AP289 vs Anchor A
preface.tex:490                      3    "2+1 = 3"                     AP289 vs Anchor A
preface.tex:1046                     3    K3-1 flagship claim           AP289 vs Anchor A
introduction.tex:322                 3    dimension claim               AP289 vs Anchor A
introduction.tex:1041                3    verified list                 AP289 vs Anchor A
introduction.tex:1186                3    dimension identification      AP289 vs Anchor A
quantum_group_reps.tex:1115          3    three-kappa disambiguation    AP289 vs Anchor A
quantum_group_reps.tex (rem):1117    0    κ_cat(K3×E) = 0               correct
main.tex (abstract region)           3    headline K3-1                 AP289 vs Anchor A
```

Ambiguous / genuinely needs comment (not value correction):
```
cy_c_six_routes_convergence.tex:437   ρ^{R_1}(S×E) = 2+1 = 3  generator-rank, NOT κ_ch
                                                          (correctly attributed, leave)
cy_c_six_routes_convergence.tex:444   κ_BKM(K3×E) = 5        Borcherds, not κ_ch
                                                          (correctly attributed, leave)
```

## 4. Verdict: systemic contradiction, sweep cannot heal at site-level

The 30+ Route-B-labelled sites are NOT stray AP289 propagation errors
around a clean canonical convention. They are inscriptions of a COMPETING
anchor theorem (`prop:beauville-kappa-formula` ClaimStatusProvedHere at
`cy_to_chiral.tex:293-342`) that asserts κ_ch is additive as a property
of the Φ_d functor, directly contradicting Anchor A's
`thm:kappa-hodge-supertrace-identification` which asserts κ_ch is the
Künneth-multiplicative Hodge supertrace on the same object.

Both anchors carry `\ClaimStatusProvedHere`. This is a constitutional
conflict at the anchor-theorem level. A site-level disambiguation-comment
pass would paper over the underlying inconsistency; a site-level
value-correction pass would silently pick one anchor over the other.

Neither is within the Wave-10 sweep charter.

## 5. Escalation: what the heal requires

The resolution is one of three programme-level decisions, each requiring
a dedicated attack+heal wave rather than a disambiguation sweep:

**Option H1 — Anchor A wins:** κ_ch ≡ Hodge supertrace (Künneth-
multiplicative). κ_ch(K3×E) = 0 programme-wide. All 30+ Route B sites
get value corrections to 0, `prop:beauville-kappa-formula` downgrades
to the Heisenberg-level-tower invariant (distinct symbol or κ_Heis
subscript), and conj:cy-kappa-identification Clause (ii) retracts. The
"dim_C(K3×E) = 3 = κ_ch" headline at preface.tex:1046 is retracted.

**Option H2 — Anchor B wins:** κ_ch ≡ "chiral modular characteristic"
(additive by chiral de Rham product structure). κ_ch(K3×E) = 3
programme-wide. `thm:kappa-hodge-supertrace-identification` scopes to
compact CY_d with h^{1,0}=0, and the K3×E entry at
cy_d_kappa_stratification.tex:448-452 retracts. The "five invariants
{κ_ch = 0, κ_cat = 0, ...}" panel at cy_c_six_routes_convergence.tex
rewrites to κ_ch = 3.

**Option H3 — Two-subscript split:** κ_ch^Hodge(K3×E) = 0 and
κ_ch^chiral(K3×E) = 3 as genuinely distinct invariants. Both anchors
retained; all 107+ sites get atomic subscript disambiguation (extends
HZ-7 approved set {ch, cat, BKM, fiber} to {ch-Hodge, ch-chiral, cat,
BKM, fiber}, or rename one branch).

The evidence favors H3 honestly reflecting the programme's
position: `cy_to_chiral.tex:273-288` `rem:cy-kappa-evidence` explicitly
names "additivity vs multiplicativity" as the clash and says "κ_ch is
additive, χ(O_X) is multiplicative" — which is then CONTRADICTED by
`cy_d_kappa_stratification.tex:452` giving Κünneth-multiplicative κ_ch
= 0. The programme inscribed BOTH anchors without noticing the clash
(characteristic of the AP289 Wave-4 heal not propagating into the
pre-existing Φ_d functor chapter).

## 6. Action taken this wave

- ZERO edits applied to .tex files.
- ZERO commits made.
- Sweep note inscribed here for handoff to the next attack+heal agent.

## 7. Residual unclassified

None. All 107 K3×E hits across chapters + standalones classified.
`metadata/dependency_graph.dot`, `working_notes.tex`, and `notes/`
scratch files excluded per sweep scope.

## 8. Commit plan

None. Next wave must pick Option H1 / H2 / H3 at programme-governance
level BEFORE any site-level heal agent can touch these files.

---

**Key finding.** The Wave-10 Route A/B sweep uncovered a constitutional
inconsistency between two `\ClaimStatusProvedHere` anchors on the
definition of κ_ch on product CY_3. The 30+ "Route B" sites flagged in
Waves 4-6 are not stray errors but faithful consumers of Anchor B
(`prop:beauville-kappa-formula`), which itself contradicts Anchor A
(`thm:kappa-hodge-supertrace-identification`). Neither anchor has been
retracted; both are cited as load-bearing in the preface, the
introduction, and cross-volume bridges. Escalated to programme
governance.
