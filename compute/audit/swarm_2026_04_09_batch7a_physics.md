# Adversarial Swarm 2026-04-09/10 — Batch 7a: Physics identifications

**Scope.** 10 agents, 10 distinct angles on the physics-side identifications connecting the algebraic programme to QFT/gravity: BV-BRST = bar, Z^der = bulk, entanglement, factorization envelope, 3D HT QFT, slab, holographic datum, QME = MC, CGD integration.

## Master verdict

**The manuscript is INTERNALLY HONEST on physics identifications** — chapter-level remarks consistently flag gaps with `\ClaimStatusHeuristic` or `conj:` tags. The problem is a **systematic disconnect between chapter-level honesty and headline prose** (preface / introduction / CLAUDE.md / MEMORY.md). Every physics identification has:
- A load-bearing PROVED clause (usually Heisenberg-only, or genus-0 only, or compact-generator-only, or coderived-category-only)
- An honest chapter-level remark tagging the general case as heuristic/conjectural
- A headline statement in preface/intro/CLAUDE.md that advertises the unrestricted version

## 10-angle verdicts

### Angle 1 — BV-BRST = bar

**Verdict: PROVED-RESTRICTED.**

Multiple theorems at different scopes found in `bv_brst.tex`:
- `thm:bv-bar-geometric` (g=0, all classes, ProvedElsewhere via CG17)
- `thm:brst-bar-genus0` (g=0, all, requires c=26, ProvedHere)
- `thm:bv-bar-coderived` (all g, all classes, IN CODERIVED CATEGORY) — nearly tautological per author's own `rem:bv-bar-coderived-why` at L1978-2018
- `thm:heisenberg-bv-bar-all-genera` (Heisenberg only, SCALAR level F_g=κ·λ_g^FP, all-genera, 4 independent proofs)
- `conj:master-bv-brst` at `editorial_constitution.tex:433-457` is the full-chain-level master, explicit `\ClaimStatusConjectured`

**AP73 correction**: CLAUDE.md says "PROVED G/L, CONDITIONAL C/M" but actually G/L/**C** are unconditional and only **M** conditional AT THE CHAIN LEVEL. BUT this split is for the SEWING-OPERATOR identification (Δ_BV = d_sew), not the full chain-level BV/BRST = bar. Full chain-level BV = bar is proved only for Heisenberg at scalar level and for all classes at coderived level.

Fix: update AP73 to distinguish the three proof layers.

### Angle 2 — Z^der_ch(A) = bulk

**Verdict: PROVED-OVER-SCOPED.**

**Anchor theorems**:
- `thm:derived-center-hochschild` at `hochschild_cohomology.tex:1028-1044` (ProvedHere, compact-generator hypothesis explicit): Z_der(C) ≃ HH^•(A_b) via Keller/BZFN/Toen Morita
- `cor:bulk-derived-center-categorical` at Vol II `foundations.tex:349-373` (ProvedHere, compact-generator explicit)

**Over-scoping**:
1. Compact-generator hypothesis HIDDEN in Vol I intro (L246-274), Vol II preface (L29-42), Vol III preface (L271-279)
2. "Drinfeld double = universal bulk" jump is conjectural (condition C4, A^!_∞ → A^! passage)
3. Vol I `prop:hdm-u-a-recoverability` is `\ClaimStatusHeuristic` because R2 needs bar-cobar inversion beyond Koszul locus
4. **Vol III preface L271-279 is the most egregious**: "A → Z^der_ch(A) is the universal boundary-bulk reconstruction functor ... = bulk gravity" (unhedged)
5. F13, F14, F15 from prior batches all STILL OPEN

### Angle 3 — Entanglement S_EE = (c/3) log(L/ε)

**Verdict: IMPORTED-AND-MATCHED, VIR-SPECIFIC κ-link.**

`thm:ent-scalar-entropy` at `entanglement_modular_koszul.tex:158-178`: S_EE = (c(A)/6)(1+1/n) log(L/ε). Formula is in c(A), NOT κ.

Proof is STANDARD Calabrese-Cardy replica trick; twist-operator lemma `lem:ent-twist-dimension` is ProvedElsewhere citing Calabrese-Cardy 2004 Eq. (2.5).

**For Heisenberg**: census table shows S_EE/log(L/ε) = 1/3 (because c_Heis = 1, independent of k). κ_Heis = k decouples from S_EE entirely. MEMORY.md's "S_EE from κ" is misleading: the leading term is from **c** (imported), not from κ.

**Genuine new content**:
- κ-controlled shadow corrections `δS_r ≤ Cρ^r r^{-5/2} log(L/ε)` (Prop `prop:ent-complexity-classification`) — genuinely new
- Vir+Vir^! sum rule: S_EE(Vir_c) + S_EE(Vir_{26-c}) = (26/3) log(L/ε) from κ+κ'=13 — genuinely new
- Four-class G/L/C/M complexity tower — genuinely new

Manuscript is internally honest; headline overclaim lives in MEMORY.md only.

### Angle 4 — Factorization envelope U^mod_X

**Verdict: NOVEL-REFINEMENT, with overlapping theorem/conjecture pair.**

**Theorem** (ProvedHere): `thm:platonic-adjunction` at `higher_genus_modular_koszul.tex:26593-26650`. States the adjunction Hom_{Fact_cyc}(U^mod_X(L), F) ≅ Hom_{LCA_cyc}(L, Prim^mod(F)).

**Parallel conjecture**: `conj:universal-modular-factorization-envelope` at `frontier_modular_holography_platonic.tex:3523-3577` (Conjectured). Nearly identical adjunction with a stronger target (ModKoszul(X)).

**These two are NOT RECONCILED in either file** — potential AP124-like duplication of meta-theorem content with different status tags.

**Distinction from BD §3.7**: genuine refinement. BD's U^ch(L) inputs a Lie-* algebra and outputs a chiral algebra at genus 0. U^mod_X inputs a **cyclically admissible** Lie conformal algebra (extra invariant pairing + conformal grading + PBW filtration + bounded pole order) and outputs a **cyclic factorization algebra carrying modular/stable-graph data** via the G_mod coefficient algebra. The "mod" = modular, not module.

**CRITICAL: single-point dependency on Nishinaka 2026** — existence of Fact_X(L) and the modular bar functor is delegated to arXiv:2512.xxxxx (unpublished preprint). This is the **second Mok25-class AP11 dependency risk** found in the programme.

**Class M gap**: higher-genus class M (Vir, W_N) is open in 2 of 3 construction strategies.

### Angle 5 — 3D HT QFT climax (Vol II Part VI)

**Verdict: CLIMAX-CONDITIONAL, leaning NOT-A-CLIMAX.**

Part VI at `~/chiral-bar-cobar-vol2/main.tex:1381` (7 chapters, ~23,258 lines). 46 ProvedHere theorems in `3d_gravity.tex` alone — genuinely substantive.

**But**:
- **NO master theorem "3D gravity from chiral algebra"**. The closest is `thm:gravity-koszul-triangle` with one trivial vertex (ℂ[[c]]) and one abstract vertex (lines = open-colour module package).
- **Brown-Henneaux c = 3ℓ/(2G) is explicitly IMPORTED, not derived**. `rem:brown-henneaux-from-thesis` at `3d_gravity.tex:3780` admits verbatim: "this remark is not a derivation of Brown-Henneaux from Koszul duality; it is an interface observation."
- **Cardy formula**: `conj:gravity-cardy` at L3941, explicitly Conjectured
- **BTZ entropy**: `conj:gravity-btz-entropy` at L4012, explicitly Conjectured
- **Virasoro line identification**: `conj:gravity-line-identification`, Conjectured
- **Vol II CLAUDE.md "Cross-Volume Bridges" table has NO gravity row** — the "climax" has no entry in the bridge index

Honest framing: "conditional reorganization of AdS_3/CFT_2 in κ-language", not derivation of 3D quantum gravity.

### Angle 6 — Slab = bimodule (RS-9)

**Verdict: BIMODULE-CLEAN.**

Three canonical sites consistently enforce RS-9:
- Vol I `koszul_pair_structure.tex:1812-1834` (`rem:dimofte-transverse-boundary`)
- Vol II `ht_bulk_boundary_line_core.tex:198-247` (`rem:slab-fiber-functor`)
- Vol II `preface.tex:251-269`

Both boundary algebras are **DIFFERENT**: H_D = A (open-colour), H_N = A^! (Koszul dual). The slab is an (A, A^!)-bimodule, not A⊗A^op-module.

**Zero RS-9 violations.** Grep for `slab.{0,40}[Ss]wiss|[Ss]wiss.{0,40}slab` returns 0 matches outside contrastive negations.

Literature: Dimofte-Niu-Py 2025 (arXiv:2508.11749), CDG 2024, CG 17.

All slab references are Remarks (not theorems/definitions), consistent with AP40 — physics-side claims grounded in proved theorems.

**Minor verification gap**: `higher_genus_modular_koszul.tex:2770` uses the bimodule structure in a proof step via Remark-strength citation; should cite Theorems A/B directly.

### Angle 7 — Holographic datum 8-fold

**Verdict: 6-FOLD-PROMISED-8 with HEURISTIC-RESIDUE.**

**TWO distinct objects share the "holographic datum" branding**:
1. **6-tuple H(T)** = (A, A^!, C, r(z), Θ_A, ∇^hol) at `frontier_modular_holography_platonic.tex:1146-1235` (`def:holographic-modular-koszul-datum`)
2. **8-tuple Π^oc_X(A)** = (A, A^!, Z^der_ch(A), Θ^oc_A, r(z), ∇^hol, Tr_A, R^oc_•(A)) at `thqg_open_closed_realization.tex:1477-1525` (`def:thqg-completed-platonic-datum`)

**MEMORY.md "6 components" is correct for H(T). CLAUDE.md "8-fold" refers to Π^oc_X, a DIFFERENT OBJECT.** These are not clearly distinguished in the index.

**Per-component status of H(T)**:
| # | Component | Status |
|---|---|---|
| (i) A | Definitional input | — |
| (ii) A^! | Koszul dual; passage A^!_∞→A^! conditional beyond Koszul locus | R2 conditional |
| (iii) C | Definitional | — |
| (iv) r(z) | ProvedHere via `thm:seven-faces-master` | clean |
| (v) Θ_A | ProvedHere via `thm:mc2-bar-intrinsic` | clean |
| (vi) ∇^hol | Defined; flatness proved only on sphere | conditional at g≥1 |

**∇^hol identification**: ∇^hol_{g,n} := d − Sh_{g,n}(Θ_A). NOT a connection on a fixed bundle — one connection per (g,n)-stratum of the derived coinvariant tower V_{g,n}(A). (∇^hol)^2 = 0 proved only on sphere unconditionally.

**No uniqueness theorem** exists for H(T).

### Angle 8 — Z^der = HH*_chiral

**Verdict: NON-UNIVERSAL (but manuscript AP94-CLEAN).**

**Categorical identification** (`thm:derived-center-hochschild` at `hochschild_cohomology.tex:1028-1044`, ProvedHere): rigorous via Morita reduction on pretriangulated dg-categories with compact generator.

**Chiral upgrade** (`thm:hochschild-bar-cobar` at `chiral_hochschild_koszul.tex:324-358`, ProvedHere, Koszul locus): reduces chiral Hochschild to Hom of bar-cobar resolution.

**Vir at generic c** (`prop:derived-center-explicit`(iii) at `chiral_center_theorem.tex:1824-1849`): HH^0 = C, HH^1 = 0, HH^2 = C·Θ. **Total dim 2, bounded, NOT polynomial-ring.**

**Critical level failure**: At k=-h^v, HH^0 = z(ĝ_{-h^v}) is infinite-dim (Feigin-Frenkel center). Violates Theorem H concentration. Acknowledged at `chiral_center_theorem.tex:1819-1822`. Theorem H statement does NOT explicitly exclude critical level (F3 again).

**Affine KM non-critical** (`prop:derived-center-explicit`(ii)): HH^0=C, HH^1=sl_2, HH^2=C. Polynomial growth holds via three-term Koszul resolution.

**Francis arXiv:1104.0181**: Cited at `en_koszul_duality.tex:2820-2868` for E_3 structure on Z^der (`prop:e3-bar-structure`), NOT for the identification itself. Theorem H proof goes via Brylinski D_X-amplitude route, not Francis tangent complex.

**AP94 residue check**: Manuscript `chapters/` is CLEAN. 0 hits for `C[\Theta]`, "polynomial ring", "Gelfand-Fuchs = ChirHoch". The `w_algebras.tex:2749` "polynomial in degrees {0,1,2}" refers to Hilbert polynomial degree, not polynomial ring. The Vir computation at `chiral_center_theorem.tex:1824-1849` correctly distinguishes ChirHoch (bounded, dim 2) from Gelfand-Fuchs (infinite). **The AP94 violation is confined to compute layer** — the other swarm is handling it.

### Angle 9 — Costello-Gaiotto-Dimofte integration

**Verdict: GAP-ADMITTED with PARTIAL-INTEGRATION.**

**Citation density in Vol II**: Costello 198 / Gaiotto 115 / Dimofte 86 hits across ~57 files. Ratio math-core:connections ≈ 1:5 — RS-4 PARTIALLY honored but connections-heavy.

**All 4 key papers cited** (unlike Vol III which lacks them):
- arXiv:2005.00083 (CDG20 "Boundary chiral algebras")
- arXiv:1812.09257 (CG18 "Twisted holography")
- arXiv:1804.06460 (CG18 "VOAs and 3d N=4")
- Dimofte25 (PIRSA lecture series)

**Bibitem alias hygiene issues**:
- CDG20 has 3 aliases: `CDG20`, `CDG2023`, `CostelloDimofteGaiottoBoundary`
- CG18 has 4 aliases: `CostelloGaiatto18`, `costello-gaiotto`, `CG18`, `CostelloGaiotto2020`
- Creates phantom distinct references

**Drinfeld double gap**: HONESTLY acknowledged. `rem:drinfeld-double-programme` at `ordered_associative_chiral_kd_core.tex:1367-1370` explicitly says "not yet constructed at the bar-complex level... assembly... is the Drinfeld double programme".

**Six-workpackages status**: DOWNSCOPED to four-part programme (parts a-d per `compute/audit/beilinson_audit_drinfeld_double_wave11.md`). Parts (a) construction and (b) antipode are Conjectured. MEMORY.md "six workpackages" is stale; two workpackages absorbed/dropped.

### Angle 10 — QME = MC identification

**Verdict: PARTIAL-MATCH.**

**Proved at**:
- **Graph level** for {m_n^(g)} via ∂²=0 on M̄_{g,n}: `thm:quantum-master-equation` at `chiral_hochschild_koszul.tex:2935-3010`
- **Closed sector reduction** via `thm:modular-mc-clutching` at `configuration_spaces.tex:2820+`
- **Heisenberg** chain-level all-genera: `thm:bv-bar-heisenberg-all-genera` at `bv_brst.tex:1388+`

**FOLKLORE-ASSERTED** for general chiral algebras at chain level. Tagged Heuristic at 4+ sites:
- `rem:qme-bar-cobar` at `bv_brst.tex:255-274`
- `rem:modular-qme-bv` at `bv_brst.tex:89-139`
- `rem:quantum-master-complete` at `bv_brst.tex:1320-1327`
- `rem:bv-equals-bar-cobar`

**`prop:chain-level-three-obstructions`** at `bv_brst.tex:1644+` enumerates 3 explicit OPEN obstructions:
1. Chain-level qi at g≥1
2. BV-Laplacian = sewing operator
3. Full QME as chain-level identity (not just scalar trace)

**CLAUDE.md C25** ("MC equation. ... QME: ...") juxtaposes the two equations side-by-side "without scope qualifier" — technically correct but misleadingly suggestive.

**Parity check (AP138)**: ||Θ_A|| = +1 (odd). ||S|| also odd-shifted. Parities match; no conflict. 1/2 factor is present.

## New findings (F35-F42)

**F35 — Overlapping theorem/conjecture pair for U^mod_X**: `thm:platonic-adjunction` (ProvedHere) at `higher_genus_modular_koszul.tex:26593` and `conj:universal-modular-factorization-envelope` (Conjectured) at `frontier_modular_holography_platonic.tex:3523` state nearly identical adjunctions with overlapping scope. Not reconciled; neither cites the other.

**F36 — Nishinaka 2026 single-point dependency (arXiv:2512.xxxxx)**: U^mod_X existence rests on an unpublished preprint. Same AP11 pattern as Mok25 (second such dependency found in the programme).

**F37 — Vol III preface L271-279 most egregious boundary-bulk overclaim**: "A → Z^der_ch(A) is the universal boundary-bulk reconstruction functor ... = bulk gravity" (unhedged, no Koszul-locus or compact-generator hypothesis). Strongest of the three preface violations. Extends F15 to Vol III.

**F38 — Bibitem alias hygiene issue**: 3 aliases for CDG20, 4 aliases for CG18. Creates phantom distinct references in citation analytics. Needs canonicalization.

**F39 — 3D gravity has NO Cross-Volume Bridges row**: Vol II CLAUDE.md Cross-Volume Bridges table lists 14 bridges, conspicuously omits a Gravity bridge. The "climax" has no bridge entry.

**F40 — MEMORY.md six-workpackages stale**: Dimofte programme downscoped to four-part; two workpackages absorbed/dropped. Documentation lag.

**F41 — Two distinct "holographic datum" definitions coexist**: 6-tuple H(T) vs 8-tuple Π^oc_X. CLAUDE.md/MEMORY.md conflate them. Both are real objects; Π^oc_X extends H(T) by (Z^der_ch, Tr_A, R^oc_•).

**F42 — Manuscript AP94-CLEAN at .tex level**: 0 hits for forbidden strings in `chapters/`. The violation is confined to compute layer (other swarm handling).

## Batch 7a cross-cutting themes

1. **Chapter-level honesty vs headline overclaim** — this is the dominant pattern across all 10 angles. The manuscript contains honest hedges at bv_brst.tex:89-139, editorial_constitution.tex:179-191, rem:brown-henneaux-from-thesis, prop:chain-level-three-obstructions, etc. The problem is preface/intro/CLAUDE.md/MEMORY.md advertising stronger claims.

2. **Heisenberg is the unconditional atom** — the one case where BV=bar, Z^der=HH*, entanglement, 3D gravity scalar level, and QME all hold unconditionally. Per Vol I CLAUDE.md RS-1 / AP108, Heisenberg is the CG opening, not the atom — but in physics it IS the atom.

3. **Compact generator / Koszul locus / Heisenberg-only / genus-0-only**: the four recurring scope restrictions across every physics identification. They should be promoted from hidden hypotheses to explicit disclaimers at the headline level.

4. **Two classes of single-point external dependencies**: Mok25 (for D²=0 ambient) and Nishinaka26 (for U^mod_X). Both are unpublished 2025/2026 preprints. AP11 risk × 2.

5. **Three bibliography hygiene classes**:
   - Wrong title (Huang05 — Batch 4)
   - Wrong author (Mok25 — Batch 4)
   - Alias duplication (CDG20 ×3, CG18 ×4 — Batch 7a)
   All signal systematic bibliography decay that no prior audit caught.

## Ready-to-apply deliverables (Batch 7a)

1. **AP73 update** — clarify G/L/C/M split between sewing-operator and full-chain-level layers
2. **Compact-generator / Koszul-locus disclaimers** — hoist from theorem statements to preface/intro (3 sites: Vol I intro, Vol II preface, Vol III preface)
3. **Vol III preface L271-279 hedging** — most egregious unhedged boundary-bulk claim
4. **U^mod_X reconciliation** — pick theorem OR conjecture, not both; reconcile `thm:platonic-adjunction` and `conj:universal-modular-factorization-envelope`
5. **Brown-Henneaux honest framing** — Vol II CLAUDE.md "Part VI climax" should read "conditional κ-reorganization of AdS_3/CFT_2"
6. **Cross-Volume Bridges gravity row** — add to Vol II CLAUDE.md
7. **MEMORY.md holographic datum count** — disambiguate 6-tuple H(T) vs 8-tuple Π^oc_X
8. **MEMORY.md six-workpackages** — update to four-part programme
9. **CDG/CG bibitem alias canonicalization** — pick one canonical key per paper
10. **QME-chain-level-obstructions** — hoist `prop:chain-level-three-obstructions` honesty to CLAUDE.md C25 scope qualifier

## Open items

- Full Vol II Seven Faces chapter-level audit (Batch 7b in flight)
- Full three-volume bibliography audit (Batch 7c pending)
- Reconcile thm:platonic-adjunction vs conj:universal-modular-factorization-envelope (needs domain expert)
- Independent verification of Nishinaka 2026 arXiv:2512.xxxxx existence and content
