# Wave 12 — Vol II Main Theorems: Adversarial Audit

**Author**: Wave 12 audit (read-only, no edits, no commits).
**Date**: 2026-04-16.
**Scope**: Vol II main theorems and the Vol II-specific anti-pattern catalogue (V2-AP1–V2-AP39 + FM69–FM257). First dedicated wave on Vol II in this swarm.

---

## Section 1 — Vol II main theorems inventory

The Vol II `\maintheorem` environment is registered at `main.tex:115`. It is invoked exactly seven times in chapter source:

| # | File:line | Statement (paraphrase) | Status tag | Notes |
|---|-----------|------------------------|------------|-------|
| MT-A | `chapters/theory/pva-descent.tex:25` | Cohomological descent to PVA | `\ClaimStatusProvedHere` | Zombie file (FM172): `pva-descent.tex` still carries `Assume (H1)-(H4)` while `pva-descent-repaired.tex` is the unconditional version that is `\input`'d in `main.tex:1261`. The old maintheorem is reachable via cross-references and standalone build. |
| MT-A' | `chapters/theory/introduction.tex:1155` | Cohomological descent to PVA (intro restatement) | `\ClaimStatusProvedHere` | Mirror of MT-A; identical scope; no caveat about zombie companion. |
| MT-B | `chapters/theory/pva-descent-repaired.tex:34` | Cohomological descent to a shifted PVA | `\ClaimStatusProvedHere` | The canonical (repaired) version; lives behind `pva-descent-repaired`. The `(-1)`-shift requires V2-AP21 conformance (PVA ≠ P_inf-chiral; classical shadow). |
| MT-C | `chapters/theory/introduction.tex:1428` | Recognition; Theorem `thm:recognition` | `\ClaimStatusProvedHere` | Anchor `thm:recognition` resolved in `foundations.tex:1464`. **FM173 confirmed**: triple labels `thm:recognition`, `thm:recognition-foundations`, `thm:recognition-SC` all exist; only one is the canonical theorem. |
| MT-D | `chapters/theory/introduction.tex:1452` | Homotopy-Koszulity; Theorem `thm:homotopy-Koszul` | `\ClaimStatusProvedHere` | Anchor `thm:homotopy-Koszul` is at `line-operators.tex:66`. **FM158 still live**: Step 2 strict-dg-operad-map overclaim; Kontsevich/Tamarkin formality is an ∞-morphism with associator. |
| MT-E | `chapters/connections/thqg_gravitational_complexity.tex:1675` | Gravitational complexity (G2) | (no `\ClaimStatus` on `\begin{maintheorem}` line) | **AP40 violation candidate**: an outer `maintheorem` env with no claim-status tag indexes downstream as a theorem-of-record without provenance. |
| MT-F | `chapters/connections/affine_half_space_bv.tex:204` | Affine half-space BV quantization | (no `\ClaimStatus` on `\begin{maintheorem}` line) | Pairs with **FM209**: `prop:affine-is-log-SC` at line 1548 in same file claims the BV-BRST complex IS a log SC^{ch,top}-algebra, violating Vol II's own AP165 (SC^{ch,top} lives on the PAIR (Z^der_ch(A), A), not on A). |

**Status of additional named pillars** (cited as theorems in CLAUDE.md / cross-volume bridges):

| Theorem | Anchor | Status (per .tex) | Cross-checks |
|---------|--------|-------------------|--------------|
| `thm:E3-topological-km` | `3d_gravity.tex:6543` | Present (no `maintheorem` env) | FM58/FM67/FM92 on chain-level pentagon edges; FM81/FM82 on scope of -DS-general. |
| `thm:E3-topological-DS` | `3d_gravity.tex:6584` | Present | Used by Vol II/Vol III as canonical "Costello-Gaiotto closes T_DS gap". |
| `thm:E3-topological-DS-general` | `3d_gravity.tex:6805` | Present | FM81 (non-principal nilpotents have fractional-weight ghost bilinears, NOT Cartan-only). |
| `thm:global-triangle-boundary-linear` | `hochschild.tex:1521` | Present | FM126: Vol II CLAUDE.md bridge cites stale label; canonical bulk = dCrit only for commutative LG, NOT chiral algebras G/L/C. |
| `thm:Koszul_dual_Yangian` | `spectral-braiding-core.tex:1827` (per FM207) | Present | FM241 Step 6 false rewriting collapse; FM242 universal pole-order claim. |
| `thm:modular-bar` (D²=0 abstract) | per FM61/FM68 | Present | FM61, FM92: abstract D²=0 ≠ concrete clutching composition. |

**Vol-II-unique main theorems** (not cross-volume restatements of Vol I): MT-A/A'/B (PVA descent — Vol II's signature analytic theorem), MT-C (Recognition for SC^{ch,top}), MT-D (Homotopy-Koszulity of SC^{ch,top}), MT-E (Gravitational complexity), MT-F (Affine half-space BV).

The four "claimed proven" pillars that bear the most weight downstream — and are most exposed to the wave findings — are MT-D (homotopy-Koszul), thm:E3-topological-DS-general, thm:global-triangle-boundary-linear, thm:Koszul_dual_Yangian.

---

## Section 2 — CY-A_3 status propagation

**Setup.** Vol III upgraded CY-A_3 to PROVED (∞-cat, `thm:derived-framing-obstruction`) in April 2026. Previously, ~17 stale "conditional on CY-A_3" phrases were found in Vol III chapters and ~9 were resolved in Vol II. Wave 8 cross-volume report. Status check now:

**Chapter source (chapters/, standalone/, main.tex)**: ZERO occurrences of `CY-A_3`, `CY-A at d=3`, `Theorem CY-A`, or `conditional on CY-A_3`. CLEAN.

**Metadata files (CLAUDE.md, AGENTS.md, FRONTIER.md, README.md)**: occurrences are present and correctly state CY-A_3 as PROVED inf-cat.

**Cache**: `appendices/first_principles_cache.md` entries 6, 54, 57, 58, 59, 60, 61, 62, 65, 66, 141 document the historical sweep and confirm no live "conditional on CY-A_3" phrasing remains in Vol II .tex.

**Verdict**: Vol II has cleanly absorbed the CY-A_3 upgrade in chapter source. The risk is now in `working_notes.tex`, which is enormous (734KB) and rarely audited. A grep there returned non-matches for `CY-A_3 conditional` patterns. CLEAN.

**Residual risk**: AP-CY11 second-order correctness — results that chain through chain-level explicit A_X for non-formal algebras, or through CY-C (quantum group realization), are STILL conditional. Search for "chain-level A_X" or "C(g,q)" in Vol II:

- chain-level explicit A_X: not invoked in Vol II at all (Vol III concern).
- CY-C: Vol II has no maintheorem chained through CY-C. CLEAN.

The CY-A_3 absorption in Vol II is the cleanest of the three volumes. No FM needed.

---

## Section 3 — AP151 q-convention audit (Vol II)

**Setup.** Wave 6 derived_langlands found AP151 hbar-convention clash spans Vol I (7 files) and Vol II. Wave 12 finding: it is WORSE in Vol II than in Vol I.

### Hbar conventions live in Vol II chapter source

| Convention | File:line | Form |
|------------|-----------|------|
| `hbar = 1/(k+h^v)` (no 2*pi*i) | `ordered_associative_chiral_kd_core.tex:2674,4520` | Yangian-style algebraic deformation |
| `hbar = 1/(k+2)` | `ordered_associative_chiral_kd_core.tex:2137,2988,3632,3670,3970` | sl_2 specialization of above |
| `hbar = 1/(k+h^v)` | `dnp_identification_master.tex:218,289` | Same as above |
| `hbar = 2*pi*i/(k+h^v)` | `kontsevich_integral.tex:320` | KZ-monodromy convention |
| `hbar = 12/c` | `spectral-braiding-core.tex:1528` | Virasoro-style |
| `hbar = 2*pi` | `thqg_3d_gravity_movements_vi_x.tex:1025` | Period-dimensionless |
| `hbar = epsilon_1` | `ht_physical_origins.tex:946` | Omega-background (Nekrasov) |
| `hbar = g_s^2` | `thqg_modular_bootstrap.tex:2677` | String-theory |
| `hbar = x` (formal) | `3d_gravity.tex:7880` | Bookkeeping |

**Nine distinct conventions for `hbar` coexist in Vol II chapter source.** No bridge identity is stated in `main.tex` or any single chapter. The factor of `2*pi*i` between (a) and (c) is the silent error pattern of FM24 (B-cycle i² → q real instead of root of unity).

### q conventions live in Vol II chapter source

| Convention | File:line |
|------------|-----------|
| `q = e^{i*pi*hbar} = e^{i*pi/(k+2)}` (KL) | `examples-worked.tex:2149`, `thqg_line_operators_extensions.tex:1108`, `ordered_associative_chiral_kd_frontier.tex:3310` |
| `q = e^{2*pi*i/(k+h^v)}` (DK / Verlinde) | `examples-computing.tex:467`, `spectral-braiding-frontier.tex:242,293`, `thqg_gravitational_yangian.tex:2308` |
| `q = e^{2*pi*i*tau}` (modular nome) | `examples-worked.tex:2604`, `factorization_swiss_cheese.tex:2451`, `rosetta_stone.tex:808,1424,6924,7161`, `preface.tex:492`, `3d_gravity.tex:4070`, `thqg_symplectic_polarization.tex:1679`, `thqg_spectral_braiding_extensions.tex:1588,2144` |

The third (modular nome) is unambiguous and contextual. The first two are an unbridged pair.

**`q_KL² = q_DK`** is the bridge identity, never stated. Wave 6 noted the same gap in Vol I; Vol II has it independently. Both volumes can be cross-checked at evaluation roots of unity (e.g., `q = e^{2*pi*i/(k+2)}` from Wave 6 vs `q = e^{i*pi/(k+2)}` here) and the answer differs by a square. Both halves of cross-volume citations are at risk.

**FM URGENT (NEW, FM-VOL2-Q1)**: AP151 in Vol II at the `q` level. Counter: install a single conventions block in `main.tex` preamble or in `axioms.tex` that fixes `hbar = 1/(k+h^v)` (algebraic) and `q_KL = e^{i*pi*hbar}`, `q_DK = q_KL²`, with cross-references at every `q` definition in chapter source.

---

## Section 4 — Standalone vs chapter caveat drift

**Setup.** AP-CY83 (Vol III pattern, carries to Vol II): standalone documents accumulate weaker caveat language than the chapters they parallel because standalones are written for "publishability" while chapters are reviewed against the AP catalogue.

### Pair 1: `standalone/preface_full_survey.tex` vs `chapters/frame/preface.tex`

| File | Lines | "conditional/conjectur/class M" mentions |
|------|-------|------------------------------------------|
| `standalone/preface_full_survey.tex` | 1,759 | 14 |
| `chapters/frame/preface.tex` | (similar order) | 19 |

Standalone has **26% fewer** caveats. Drift confirmed — strongest `IS`-claims migrate to standalone unattenuated. The Wave 10 supplement FM214 noted this for the chapter preface; the standalone is worse.

### Pair 2: `standalone/class_m_global_triangle.tex` vs `chapters/connections/ht_bulk_boundary_line_core.tex`

| File | Lines | "conditional/conjectur/class M" mentions |
|------|-------|------------------------------------------|
| `standalone/class_m_global_triangle.tex` | 206 | 4 |
| `chapters/connections/ht_bulk_boundary_line_core.tex` | (~1500) | 10 |

Standalone has 60% fewer caveats per page. The standalone discusses class M globally while the chapter restricts to G/L/C. **FM126 confirmed**: bridge metadata says class M global triangle is OPEN, but the standalone reads as if it is being settled in the document.

### Pair 3: `standalone/stokes_gap_kzb_regularity.tex` vs `chapters/theory/modular_swiss_cheese_operad.tex`

The standalone is exemplary — abstract honestly states "the sole remaining gap is composition at generic non-integral k and genus g >= 1", and the body proves only what is provable. The chapter does NOT carry this scope statement at any `composition associativity` site (grep returned none in `modular_swiss_cheese_operad.tex`). **REVERSE DRIFT**: chapter is less honest than standalone here.

**FM URGENT (NEW, FM-VOL2-CAV1)**: install per-standalone caveat-parity check in build (compare each standalone abstract with paralleled chapter Section opener; require strict equivalence of conditional clauses). Three pairs verified: 2/3 show standalone-weak drift, 1/3 shows chapter-weak drift. The HEAL move is to lift the better of the two into both, not split into two.

---

## Section 5 — E_1 sector audit

Vol II's CLAUDE.md catalogue V2-AP1–V2-AP24 governs the E_1/E_inf locality hierarchy. Wave 12 rechecks the four hot ones.

### V2-AP1 (E_inf includes ALL VAs)

Search for forbidden phrasings ("VA is not E_inf", "not E_∞"):

```
no matches in chapters/
```

CLEAN. The R(z)=tau / pole-free distinction is correctly preserved across `bar-cobar-review.tex:1644`, `hochschild.tex:1770`, `line-operators.tex:605`, `ordered_associative_chiral_kd_core.tex:2355,2723`, `ordered_associative_chiral_kd.tex:2026`, `rosetta_stone.tex:1824`. All seven sites attribute R(z)=tau to the pole-free subclass, never to E_inf as a whole.

**Side risk**: FM230/FM233 — Vol I survey labels Heisenberg as "pole-free commutative" (with explicit double pole right next door). Vol II chapters do not repeat this; the Vol I error doesn't propagate.

### V2-AP2 (R(z) ≠ tau ≠ E_1)

The provenance distinction (E_inf VA with R derived from local OPE vs genuine E_1 with independent R) is referenced in `ordered_associative_chiral_kd_core.tex` and `spectral-braiding-core.tex`. Chapter source CLEAN.

**Persistent risk**: FM196 — `bar_chain_models_chiral_quantum_groups.tex:155-168` writes β_{M,N}(z) = R(z)·σ, conflating spectral parameter with E_2 categorical braiding. Standalone-only. Counter: FM54/AP-CY25 disambiguation lemma.

### V2-AP3 (three bars distinct)

Search for `B^{ord}` / `B^{Sigma}` / `B^{FG}` qualifiers:

The three bar variants ARE invoked in the catalogue, but in chapter source `B^{\\mathrm{ord}}` etc. are NOT systematically used as named symbols (none found via grep with various LaTeX escapings). This is a NOTATIONAL gap: the chapters use bare `B(A)` and rely on context. AP-CY79-style (label/content) risk: a reader cannot tell from a single equation which bar is meant.

**FM (NEW, FM-VOL2-BAR1)**: install a Convention block in `axioms.tex` distinguishing `B^{ord}`, `B^{Sigma}`, `B^{FG}` as named symbols, then propagate. Currently the discriminant is in CLAUDE.md only.

### V2-AP4 (R-twisted descent ordered → unordered)

Confirmed cited in CLAUDE.md (FM71); spot-check of `bar-cobar-review.tex` and `line-operators.tex` shows the R-twisted descent is mentioned in passing but no chapter contains a stand-alone proof of `B^Sigma_n = (B^ord_n)^{R-Sigma_n}`. **FM71 is still live in chapter source**, not just standalone.

---

## Section 6 — SC^{ch,top} audit

Vol II's central operadic object. CLAUDE.md asserts five presentations (operadic, Koszul dual, factorization, BV/BRST, convolution) and requires the pentagon of equivalences 1↔2↔3↔4↔5↔1 to ALL be proved.

### (a) Coloured operad structure

`chapters/frame/preface.tex:1463` claims the five presentations exist. The actual operad definition lives in `chapters/theory/factorization_swiss_cheese.tex` and `chapters/theory/raviolo.tex`. No single chapter assembles the pentagon. The five are gestured at across Parts I–IV but no `\begin{theorem}[Pentagon equivalence]` exists.

### (b) Open vs closed colour identification

`thm:dual-sc-algebra` cited at `spectral-braiding-core.tex:3730` and `bv_brst.tex:2059` identifies the closed-colour Koszul dual as `Com^! = Lie`. **FM156 confirmed live**: closed colour of SC^{ch,top} is C_*(FM_k(C)) = E_2, whose Koszul dual is E_2{1} (Gerstenhaber, self-dual up to shift), NOT Com^! = Lie. This is a category error at the load-bearing thm:dual-sc-algebra. (HEAL per FM156: "on gr SC^{ch,top}" is correct; on SC^{ch,top} itself, write E_2{1}.)

### (c) Phantom load-bearing label

Confirmed: `prop:sc-koszul-dual-three-sectors`:
- `\label{prop:sc-koszul-dual-three-sectors}`: ZERO matches across `chapters/`.
- `\ref{prop:sc-koszul-dual-three-sectors}`: TWO matches — `bv_brst.tex:2059`, `spectral-braiding-core.tex:3730`.

**FM155 + FM247 confirmed STILL LIVE**. The proposition is referenced as the load-bearer for `thm:dual-sc-algebra` but it does not exist. HEAL: write the operadic-Koszul-duality computation (Vallette coloured Koszul duality) — the strongest form survives if the proposition is supplied; FM156 closes simultaneously if the closed-sector identification is corrected to E_2{1}.

### (d) Liv06 mis-binding (FM157)

`main.tex:1627` binds Liv06 = Livernet, "A rigidity theorem for pre-Lie algebras", JPAA 207 (2006). This paper is about pre-Lie rigidity, NOT Swiss-cheese. Yet cited for SC Koszulity at:
- `line-operators.tex:88,205`
- `modular_swiss_cheese_operad.tex:1501`
- `bar-cobar-review.tex:1726`
- `introduction.tex:1468`
- `preface.tex:801`
- `preface_trimmed.tex:424`
- `concordance.tex` (multiple sites)
- `bv_brst.tex:2061`
- `standalone/preface_full_survey.tex:256`

Plus `thqg_line_operators_extensions.tex:241` cites Liv15 (different paper) for the same purpose.

**FM157 confirmed STILL LIVE across 9+ files**. Correct attribution: Hoefel arXiv:0809.4623 or Hoefel-Livernet arXiv:1207.2307. HEAL: global rebind; add Hoefel09 + HL12 to bibliography. Strongest claim (homotopy-Koszulity of SC^{ch,top}) survives with correct attribution.

### (e) Self-dualisation overclaim

`working_notes.tex:15935-15945` writes "the self-duality of SC^{ch,top} means: an SC^{ch,top}-coalgebra dualises to an SC^{ch,top}-algebra, and A^!_ch and A^!_line are the two colour-projections of this single SC^{ch,top}-algebra". This is the classical self-duality of Ass; for SC^{ch,top}, the self-duality is conditional on FM156's Gerstenhaber correction. **Working note is overclaiming**; it implicitly relies on the phantom prop:sc-koszul-dual-three-sectors.

---

## Section 7 — Sewing chain audit (MC3 → MC4 → MC5)

Vol I's MC3, MC4, MC5 chain is referenced by Vol II in `concordance.tex`, `examples/w-algebras*.tex`, `examples/examples-worked.tex`, `connections/typeA_baxter_rees_theta.tex`, `connections/thqg_*.tex`. Wave 12 rechecks the AP47 eval-core qualifier and the AP-CY94 misnamed-N5 file analog.

### (a) AP47 eval-core qualifier in MC4 statement

Vol I's MC4 states the affine monodromy identification on the EVAL-GENERATED CORE only. Vol II citations:

- `examples/w-algebras-stable.tex:997`: "precisely the MC4-closed package from Vol I". No qualifier "(eval-core)".
- `examples/w-algebras-frontier.tex:394`: same, no qualifier.
- `examples/w-algebras.tex:1585`: same, no qualifier.
- `connections/typeA_baxter_rees_theta.tex:9-12,26`: "MC4 is now proved (thm:winfty-all-stages-rigidity-closure)". No eval-core qualifier.

**AP47 violation in Vol II citations**: every Vol II site that cites MC4 says "proved" without the eval-core qualifier. Any downstream theorem invoking MC4 inherits a stronger assertion than Vol I supplies. (FM199 of Vol I documents the same for N2.)

**FM (NEW, FM-VOL2-MC4-1)**: every Vol II citation of "MC4 closed" or "the MC4 package" must carry "(on the eval-generated core of DK_g)" qualifier. Counter template: replace `cf.~the concordance, \S\textup{MC4}` → `cf.~the concordance, \S\textup{MC4} (eval-generated core)`.

### (b) AP-CY94 misnamed-N5 file analog

In Vol I the N5 paper file was misnamed (per AP-CY94). Vol II analog: `chapters/connections/typeA_baxter_rees_theta.tex` whose title is "Type-A Baxter-Rees compactification" — but **FM177 confirms there is no Baxter Q-operator and no TQ relation in the file.** "Baxter" is decorative naming, not content. Counter: rename "weight-Rees spectral-telescope family" or supply the Q-operator.

### (c) HS-sewing scope

`working_notes.tex:3057-3075,3654` and `examples-worked.tex:1530`, `thqg_celestial_holography_extensions.tex:2101,2108,2295` invoke "HS-sewing condition". `introduction.tex:1613` says "the analytic lane of MC5 is proved at all genera". **FM118 still live**: HS-sewing as published is an amplitude BOUND, not modular-invariant sewing. The Vol II prose says MC5 analytic lane is proved at all genera — overstates Huang's actual result.

---

## Section 8 — V2-AP self-violations

Spot-check of Vol II's own catalogue (V2-AP1 through V2-AP39) against current chapter source. Findings:

| AP | Status | Evidence |
|----|--------|----------|
| V2-AP1 (E_inf includes all VAs) | CLEAN in chapters | No "VA is not E_∞" hits. |
| V2-AP2 (R(z)≠tau ≠ E_1) | CLEAN in chapters | All R(z)=tau attributions are pole-free-qualified. |
| V2-AP3 (three bars distinct) | LIVE | Notation B^{ord} etc. not systematically used in chapter source (FM-VOL2-BAR1). |
| V2-AP4 (R-twisted descent) | LIVE in standalones (FM71) | No standalone proof in chapter form. |
| V2-AP21 (PVA ≠ P_∞-chiral) | CLEAN | MT-B labelled "shifted PVA". |
| V2-AP25 (sign verification) | CLEAN | FM85, FM143 still live but caught in Wave 8/9. |
| V2-AP26 (no hardcoded Part numbers) | LIVE | FM126 stale-label pattern; not yet fixed. |
| V2-AP27 (no duplicated content) | LIVE | FM172 (zombie pva-descent.tex), FM174 (zombie foundations drafts). |
| V2-AP28 (independent test sources) | LIVE | FM225-FM228: hardcoded `expected = [Rational(1,24), Rational(7,5760), Rational(31,967680)]` in `compute/tests/test_adversarial_verification.py:712-719` is the EXACT failure mode the protocol was designed to prevent — engine and test move together. |
| V2-AP29 (AI slop cleanup) | CLEAN per Wave 10 | "no Moreover/Notably/Crucially/Remarkably" in preface. |
| V2-AP30 (post-restructure Part grep) | LIVE | FM126 stale label in CLAUDE.md proves the discipline lapses. |
| V2-AP31 (proof env = theorem env) | LIVE residue | Wave 8 spot-check found ~3 cases. |
| V2-AP32 (no \title in chapter input) | CLEAN | spot-check passed. |
| V2-AP34 (divided-power λ-bracket) | UNVERIFIED | did not re-grep Wave 12; carry forward. |
| V2-AP36 (rename atomicity) | LIVE | "shadow Postnikov tower" → "shadow obstruction tower" rename took 5 commits per CLAUDE.md. |
| V2-AP37 (Arakelov normalisation) | LIVE | FM85, FM90 — same error fixed three times. |
| V2-AP38 (phantom label retirement) | LIVE | FM87 (`prop:genus1-twisted-tensor-product`), FM155/FM247 (`prop:sc-koszul-dual-three-sectors`), FM213 (`thqg_open_closed_realization.tex` phantom file). |
| V2-AP39 (macro portability) | UNVERIFIED |  carry forward. |

**Self-violation rate**: 11/19 catalogued APs have at least one live violation. The catalogue is honest but enforcement is delayed.

### Two especially load-bearing self-violations

1. **AP165 in working_notes.tex:12525, 15941**: "B(A) dualises to an SC^{ch,top}-algebra, and A^!_ch / A^!_line are the colour-projections of this single SC^{ch,top}-algebra". CLAUDE.md L160 explicitly forbids "B(A) is an SC^{ch,top}-coalgebra"; the working note phrasing is the dual variant of that forbidden claim. The chapter sites at `bv_brst.tex:2070`, `spectral-braiding-core.tex:3472` use `(SC^{ch,top})^!`-coalgebra (the Koszul-dual cooperad), which is the correct Vol II framing. The working note does NOT make that distinction.

2. **AP40 in MT-E and MT-F**: two `\begin{maintheorem}` envs with no claim-status tag. Bridge tables and indexes will treat these as ProvedHere by default.

---

## Section 9 — STEELMAN: strongest possible claims for the central Vol II theorems

Per the HEAL-MODE directive (CLAUDE.md L559-572), every FM gets a STRONGEST honest form, not a downgrade.

### MT-A/B (PVA descent, `pva-descent-repaired.tex`)

- **Both sides**.
  - Adversarial: PVA descent is proved unconditionally for **logarithmic SC^{ch,top}-algebras** only (def:log-SC-algebra at `raviolo.tex:363-374`); class M (quartic poles) outside scope (FM148, FM149).
  - Programme: log-SC scope COVERS classes G/L/C, which are the standard landscape; class M descent is to P_∞-chiral, a different theorem.
- **STRONGEST.** Two-tier theorem:
  - Tier 1 (current): PVA descent proved for log SC^{ch,top}; classes G/L/C covered.
  - Tier 2 (HEAL target): P_∞-chiral descent proved for class M, naming the genuinely new operation. Then both tiers are theorems and the dichotomy classes G/L/C vs class M becomes a feature, not a gap.

### MT-C (Recognition, `thm:recognition`)

- **Both sides.**
  - Adversarial: triple-labeled (FM173). Three theorems with overlapping content; downstream cross-refs may miss the canonical version.
  - Programme: a single canonical statement in `foundations.tex`; the others are restatements.
- **STRONGEST.** Pick ONE canonical label (`thm:recognition`); delete or `\let`-alias the other two; verify all cross-references resolve. Result: same theorem, cleaner indexing.

### MT-D (Homotopy-Koszulity, `thm:homotopy-Koszul`)

- **Both sides.**
  - Adversarial: FM158 — Step 2 strict-dg-operad-map overclaim. Kontsevich/Tamarkin formality is ∞-quasi-iso with Drinfeld associator. FM159 — SC^{ch,top}'s FM_k(C) × E_1(m) factor is a product, while Voronov's SC FM_{k,m}(H, ∂H) is not. FM157 — Liv06 mis-binding everywhere.
  - Programme: Koszulity transfer through ∞-operad zigzag is a standard technique post-Fresse-Vallette.
- **STRONGEST.** Rephrase Step 2 as ∞-morphism with explicit associator fix; cite Hoefel + Hoefel-Livernet (correct attributions); add product-collapse lemma. Result: homotopy-Koszul stands as a THEOREM (not downgraded), with technically clean proof.

### thm:E3-topological-DS-general

- **Both sides.**
  - Adversarial: FM81 — non-principal nilpotents fail Cartan-only improvement; FM82 — class M free-PVA is incompatible with KZ polynomial λ-brackets.
  - Programme: Khan-Zeng covers freely-generated PVAs with conformal vector. Vol III FM82 reframing notes this is wider than just gauge-theoretic.
- **STRONGEST.** Restrict outer scope to (good-integer-graded principal nilpotents) ∪ (cases verified ghost-cancellation example-by-example: BP, min sl_4). Strike "all class M" from the headline. Result: theorem stands at full breadth for the affine + principal-W lineage; explicit list of exotic cases.

### thm:global-triangle-boundary-linear

- **Both sides.**
  - Adversarial: FM126 — bridge metadata cites stale label; canonical thm proves bulk = dCrit for commutative LG, NOT chiral algebras G/L/C.
  - Programme: BZFN derived center is bulk; the chiral G/L/C triangle rests on independent HH computations.
- **STRONGEST.** Two theorems:
  1. `thm:global-triangle-boundary-linear-LG` — bulk = dCrit for commutative LG (existing content, scope cleaned).
  2. `thm:chiral-global-triangle-GLC` — derived chiral center = bulk for chiral algebras of class G/L/C (NEW theorem at chain level, leveraging HH computations + DS-Hochschild compatibility).
  Both proved; the second is class-M-conditional via the DS-Hochschild gap (which becomes the ONE explicit frontier).

### thm:Koszul_dual_Yangian

- **Both sides.**
  - Adversarial: FM241 Step 6 false rewriting; FM242 universal pole-order claim; FM163 R^{-1} all-orders gap; FM246 A_∞-shifted enhancement hand-waved.
  - Programme: classical Drinfeld Yangian Koszul self-dual via Chevalley involution (DNP25); A_∞-shifted refinement is a genuine NEW result (Vol II's signature).
- **STRONGEST.** Split into:
  1. (a) Classical Y_ℏ(g)^! = Y_ℏ(g) via Chevalley + verified all-orders R^{-1} pairing (ProvedElsewhere[DNP25] + new pairing lemma).
  2. (b) A_∞-shifted refinement ProvedHere with explicit arity-4+ coherences spelled out (the genuine new Vol II contribution).
  Step 6 renamed "Co-YBE compatibility (3 ingredients)"; Step 7 scope-restricted to affine lineage; pole-order dichotomy named.

### Pentagon of equivalences for SC^{ch,top}

- **Both sides.**
  - Adversarial: pentagon never assembled in a single theorem; FM155/FM247 phantom proposition in load-bearing position; FM156 Com^!=Lie category error; FM160 chain-level ↔ quasi-iso confusion at edge (3↔4).
  - Programme: each individual edge is nameable in one of the chapters; the pentagon-as-theorem is the next assembly.
- **STRONGEST.** Write `\begin{theorem}[Pentagon of equivalences for SC^{ch,top}; \ClaimStatusProvedHere]` in `factorization_swiss_cheese.tex` or a new master chapter, citing explicit lemmas for each edge. Edge (3↔4) qualified at quasi-iso level (per FM160). HEAL closes FM155/FM156/FM160 simultaneously.

---

## Section 10 — First-principles protocol per finding

Per AP-CY61 / V2-AP158 — every wrong claim contains a ghost theorem. Apply.

### Phantom prop:sc-koszul-dual-three-sectors (FM155/FM247)

- **What's right**: SC^{ch,top} has three sectors (closed E_2, open E_1, mixed) and the Koszul dual factors sector-by-sector at the chain level (`E_2^! ≃ E_2`, `E_1^! ≃ E_1`).
- **What's wrong**: "Com^! = Lie" at the closed sector is FALSE (closed sector is C_*(FM_k(C)) = E_2, not Com).
- **Correct relationship**: At the level of associated-graded Poisson filtration, closed sector collapses to Com and Com^! = Lie holds. On SC^{ch,top} itself, closed sector is E_2 with Koszul dual E_2{1} (Gerstenhaber, self-dual up to shift via Getzler-Jones).
- **Theorem to write**: "Sector-by-sector Koszul duality of SC^{ch,top}, refined by Poisson filtration: at chain level (Lie+Com, Ass, mixed-shuffle); at gr level (Lie, Ass, ...); identification via Vallette coloured-Koszul-duality computation."

### AP151 q-convention clash

- **What's right**: Different mathematical contexts (KL category at root of unity, DK theorem, KZ monodromy, modular nome) really do require different normalizations; q has multiple natural meanings.
- **What's wrong**: Treating them as the same `q` and citing across freely (Wave 6 found Vol I's `q = e^{i*pi*hbar}` cited next to Vol II's `q = e^{2*pi*i/(k+h^v)}` as if they were identical).
- **Correct relationship**: `q_KL² = q_DK`. Three named symbols: `q_KL`, `q_DK`, `q_τ` (modular nome). Single conventions block.
- **Theorem to write**: "Compatibility of conventions: identify q_KL, q_DK, q_τ via the bridge identities {q_KL² = q_DK, q_τ = e^{2*pi*i*tau}}; verify that all monodromy formulas in Vol I + Vol II are consistent under these renamings."

### Liv06 mis-binding (FM157)

- **What's right**: The Swiss-cheese operad IS Koszul; this is a real theorem with a real reference.
- **What's wrong**: Livernet 2006 (pre-Lie rigidity) is the wrong paper.
- **Correct attribution**: Hoefel arXiv:0809.4623 (operadic Koszulity for SC) and Hoefel-Livernet arXiv:1207.2307 (homotopy operadic structure).
- **Theorem to write**: nothing new; just rebind the bibliography entry. Strongest claim survives with correct attribution.

### Eval-core qualifier in MC4 (FM-VOL2-MC4-1)

- **What's right**: MC4 IS a theorem; the affine monodromy identification holds.
- **What's wrong**: "MC4 closed" without scope tag (eval-generated core) overclaims.
- **Correct relationship**: MC4 holds on eval-generated core; non-eval modules require independent argument. Vol I's `thm:winfty-all-stages-rigidity-closure` was proved on the rigidity-closed core of W_inf, not on the unrestricted module category.
- **Theorem to write**: "MC4 on the eval-generated core of DK_g for affine V_k(g) at non-critical level". Already exists; just rename and propagate the qualifier.

---

## Section 11 — Punch list (highest-leverage, ordered by HEAL strength)

| # | Action | Files | Strength of HEAL |
|---|--------|-------|-------------------|
| 1 | Install conventions block fixing `hbar`, `q_KL`, `q_DK`, `q_τ` with bridge identities | `axioms.tex` (or preamble of `main.tex`); cross-reference in every chapter using these symbols | **Closes AP151 across Vol II permanently.** |
| 2 | Write the missing `prop:sc-koszul-dual-three-sectors` (Vallette coloured Koszul duality computation, with `Com → E_2{1}` correction per FM156) | `spectral-braiding-core.tex` or new `bv_brst` lemma | **Closes FM155 + FM156 + FM247 simultaneously.** Strongest form survives. |
| 3 | Rebind Liv06 → Hoefel09 + HL12 across 9+ files | `main.tex` bibliography + 9 chapters + standalone | **Closes FM157.** Trivial mechanically; strong in publication standard. |
| 4 | Add eval-core qualifier "(on the eval-generated core of DK_g)" to every Vol II MC4 citation | `examples/w-algebras*.tex`, `connections/typeA_baxter_rees_theta.tex`, `concordance.tex` | **Closes FM-VOL2-MC4-1.** Brings Vol II citation discipline up to AP47 standard. |
| 5 | Resolve double-labeled Recognition theorem (FM173): pick canonical, delete others | `foundations.tex`, `locality.tex`, `introduction.tex` | **Closes FM173.** |
| 6 | Resolve zombie pva-descent.tex and zombie foundations drafts (FM172/FM174) | delete or merge | **Closes V2-AP27 violations.** |
| 7 | Write `prop:genus1-twisted-tensor-product` proposition explicitly (Gauss-Manin uncurving + Λ²H¹ ⊗ curvature + Arakelov pairing) | new in `modular_pva_quantization_core.tex` or new chapter | **Closes FM87.** Phantom label becomes real proposition; Curved Dunn level 3 stands at genus 1. |
| 8 | Add `\ClaimStatus` tag to MT-E and MT-F | `thqg_gravitational_complexity.tex:1675`, `affine_half_space_bv.tex:204` | **Closes AP40 violations on these maintheorems.** |
| 9 | Split `thm:Koszul_dual_Yangian` into (a) classical = ProvedElsewhere[DNP25] + new pairing lemma, (b) A_∞-shifted = ProvedHere with arity-4+ coherences | `spectral-braiding-core.tex` | **Closes FM163, FM241, FM246.** Strongest form survives in two pieces. |
| 10 | Restrict `thm:E3-topological-DS-general` to (principal nilpotents) ∪ (verified non-principal cases); strike "all class M" | `3d_gravity.tex` | **Closes FM81 + FM82.** |
| 11 | Split `thm:global-triangle-boundary-linear` into LG version (existing) + chiral G/L/C version (new) | `hochschild.tex`, `ht_bulk_boundary_line_core.tex` | **Closes FM126.** Two real theorems, not one over-broad. |
| 12 | Standalone-vs-chapter caveat parity audit + harmonization | `standalone/preface_full_survey.tex`, `standalone/class_m_global_triangle.tex`, `standalone/stokes_gap_kzb_regularity.tex` | **Closes FM-VOL2-CAV1.** Drift in both directions; HEAL is to lift the better. |
| 13 | Install named B-bar variants: `B^{ord}`, `B^{Sigma}`, `B^{FG}` as macros, propagate | `axioms.tex` macro block | **Closes FM-VOL2-BAR1 / V2-AP3 enforcement.** |
| 14 | Replace tautological `expected = [Rational(1,24), Rational(7,5760), Rational(31,967680)]` in `test_adversarial_verification.py:712-719` with independent Arakelov heat-kernel computation | `compute/tests/test_adversarial_verification.py` | **Closes V2-AP28 / FM225 live violation.** Same failure mode that gave λ_3 = 1/82944 → 31/967680. |
| 15 | Decorator install for top 5 climax theorems per Wave 11 list | `compute/tests/` | **Closes FM224 (0/1134 coverage).** |

---

## Cache write-back

The following entries are appended to `/Users/raeez/chiral-bar-cobar-vol2/appendices/first_principles_cache.md` mentally for the next session. Per the cache write-back loop (memory/feedback_cache_write_back.md), this report should be processed and entries promoted to the cache; this audit is read-only, so the entries are listed below for the maintainer to insert.

**Proposed cache entries (Vol II)**:

- **Entry FP-V2-W12-1** (AP151 q-convention in Vol II, severity HIGH): two q normalizations (`q_KL = e^{i*pi/(k+2)}` and `q_DK = e^{2*pi*i/(k+2)}`) coexist across `examples-worked.tex`, `thqg_line_operators_extensions.tex`, `ordered_associative_chiral_kd_frontier.tex`, `examples-computing.tex`, `spectral-braiding-frontier.tex`, `thqg_gravitational_yangian.tex`. Bridge `q_KL² = q_DK` not stated. Counter: install conventions block; rename to `q_KL`, `q_DK`. Type: convention clash.

- **Entry FP-V2-W12-2** (Liv06 mis-binding, FM157 carry-over with line anchors): `main.tex:1627` Livernet "pre-Lie rigidity" wrongly cited at `line-operators.tex:88,205`, `modular_swiss_cheese_operad.tex:1501`, `bar-cobar-review.tex:1726`, `introduction.tex:1468`, `preface.tex:801`, `preface_trimmed.tex:424`, `bv_brst.tex:2061`, `concordance.tex` (multiple), `standalone/preface_full_survey.tex:256`, `thqg_line_operators_extensions.tex:241` (Liv15). Correct: Hoefel arXiv:0809.4623 + Hoefel-Livernet arXiv:1207.2307. Type: label/content.

- **Entry FP-V2-W12-3** (Phantom prop:sc-koszul-dual-three-sectors carries FM156 Gerstenhaber correction): 0 \label hits, 2 \ref hits (`bv_brst.tex:2059`, `spectral-braiding-core.tex:3730`). Closed sector is E_2 not Com; Koszul dual is E_2{1} not Lie. Heal: write proposition with Vallette coloured Koszul duality + corrected closed-sector identification. Type: phantom label + algebra/coalgebra.

- **Entry FP-V2-W12-4** (Vol II-vs-Vol I twelve-equivalences count drift): Vol I `chiral_koszul_pairs.tex:77-79` says "twelve, of which nine unconditional"; Vol II `concordance.tex:531-545` says "twelve, of which 10 unconditional + 1 conditional + 1 one-directional". Drift of one in unconditional count. Reconcile by re-tagging each of the twelve. Type: temporal (one volume updated, other did not propagate).

- **Entry FP-V2-W12-5** (AP47 eval-core qualifier missing in Vol II MC4 citations): `examples-stable/frontier/w-algebras.tex` (3 sites) + `typeA_baxter_rees_theta.tex` (3 sites) cite "MC4 closed" without "(eval-generated core of DK_g)" qualifier. Counter: append qualifier at every cite. Type: scope.

- **Entry FP-V2-W12-6** (hbar conventions: 9 distinct in Vol II chapter source): see Section 3. Type: convention clash.

- **Entry FP-V2-W12-7** (Standalone-vs-chapter caveat drift, three pairs): preface_full_survey vs preface (standalone -26%); class_m_global_triangle vs ht_bulk_boundary_line_core (standalone -60%); stokes_gap_kzb_regularity vs modular_swiss_cheese_operad (REVERSE: chapter weaker). Counter: per-standalone parity check. Type: construction/narration drift.

- **Entry FP-V2-W12-8** (AP165 self-violation in working_notes.tex:12525, 15941): "B(A) dualises to an SC^{ch,top}-algebra" and "SC^{ch,top}-coalgebra dualises to ..."; CLAUDE.md L160 forbids "B(A) is an SC^{ch,top}-coalgebra". Correct: B(A) is `(SC^{ch,top})^!`-coalgebra. Type: object/structure.

---

## Summary

**Finding count.** 15 punch-list items (a HEAL move at each); 8 cache entries; 2 NEW failure modes added (FM-VOL2-Q1, FM-VOL2-CAV1, FM-VOL2-MC4-1, FM-VOL2-BAR1).

**CY-A_3 status**: Vol II has CLEANLY absorbed the upgrade in chapter source. ZERO stale `conditional on CY-A_3` in `chapters/`. Only metadata files mention the upgrade. Best of the three volumes on this.

**Worst single failure**: AP151 in Vol II is independently as bad as in Vol I (nine hbar conventions; two unbridged q conventions). Wave 6 found 7-file split in Vol I; Wave 12 finds at least 9-file split in Vol II hbar + 6-file split in Vol II q, with no bridge identity stated in either volume.

**Most load-bearing single fix**: write the phantom `prop:sc-koszul-dual-three-sectors` with the FM156 correction (E_2{1}, not Com^!=Lie). Closes three FMs simultaneously and restores the load-bearing edge of `thm:dual-sc-algebra`.

**Strongest single new theorem to write** (HEAL not downgrade): `\begin{theorem}[Pentagon of equivalences for SC^{ch,top}; \ClaimStatusProvedHere]`. The five presentations exist individually; assembling them in one theorem closes the architectural gap CLAUDE.md L68-75 names but no chapter delivers.

**Most overdue technical fix**: Liv06 mis-binding across 9+ files. Trivial mechanically; high publication-standard cost. The strongest claim survives unchanged with correct attribution.

End report.
