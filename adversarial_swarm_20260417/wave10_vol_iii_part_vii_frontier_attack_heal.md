# Wave-10 Attack+Heal: Vol III Part VII (Frontiers)

**Target.** `~/calabi-yau-quantum-groups/main.tex` lines 1161–1248 (the typeset Part VII `\part{Frontiers}`) + `~/calabi-yau-quantum-groups/FRONTIER.md`.
**Scope.** Reconcile the typeset four-front narrative with the Wave 1–10 audit findings and with `FRONTIER.md §1–§4` (the DEFINITIVE state as of 2026-04-17).
**Voice.** Nekrasov–Okounkov BPS; Kontsevich–Soibelman motivic; Borcherds Siegel; Kapustin–Witten geometric Langlands physics.

---

## Phase 1: attack (five findings)

### ATT-1. CG deficiency opening: absent.

Part VII opens with a flat **"Four fronts, three directions"** header. There is no deficiency opening — no line naming the *unique* surviving problem whose shape forces the four fronts to exist. The reader is told *what* the frontier is, not *why* this frontier and not a different one. A Chriss–Ginzburg opening would start from the single observation that CY–A closes the existence direction but leaves every *structural* question (Langlands kernel, tetrahedron closure, Siegel covariance, non-abelian lift) open precisely because those are not existence statements. The four fronts are the *minimal* set of structural problems required to promote CY–A from existence-theorem to classification.

### ATT-2. Wave-5 AP247 (Φ as correspondence, not functor): not reflected.

Front~2 writes **"$\Phi(\cC) \leftrightarrow \mathrm{D}\text{-mod}(\mathrm{Bun}_{G^\vee})$"** and elsewhere speaks of "the functor $\Phi$". Wave-5 established AP247: **Φ is a correspondence programme, not a single functor** on the nose. The correspondence has distinct bulk/boundary legs (CY category ↔ E_1-chiral algebra ↔ derived centre), each with its own convergence scope. A Langlands-kernel reformulation that conflates these is a category error identical to the one Wave-5 retracted for Vol II.

### ATT-3. Wave-7 AP246 (osp(4|20) vs gl(4|20)): silently absent.

Part VII does not mention the super-Yangian at all. **FRONTIER.md §2 (V3-NF-osp) renamed `Y(gl(4|20))` → `Y_{osp(4|20)}`** (Mukai signature (4,20) is a symmetric indefinite lattice, not a Z/2-super-grading). A reader of Part VII who later meets `Y_{osp(4|20)}` in `chapters/examples/k3_yangian_chapter.tex` sees no orientation from the frontier statement. Worse, Front~1 speaks of "nonabelian $Y(\mathfrak{g}_{K3})$" with matrix Miura transform but does not tie this to the osp-reflection-equation direction that is the actual open frontier (V3-F19b, V3-F26).

### ATT-4. Wave-7 AP-UTI-1 (universal trace identity factor-13 retraction): absent.

The Φ universal trace identity `K = −c_{ghost}(BRST)` unifying Vol I with `κ_BKM = c_N(0)/2` is a load-bearing frontier statement (see `FRONTIER.md §1` Φ-functor bullet). Wave-7 retracted the naïve factor-13 scalar-equality form (AP-UTI-1): the identity is a *reflection* identity across the two conductor families, not a scalar equality. Part VII does not mention the universal trace identity at all and hence does not carry the Wave-7 scope qualifier.

### ATT-5. FRONTIER.md §3 (~20 items V3-F13b..F37): compressed to four.

FRONTIER.md enumerates V3-F13b, F14a/b/c, F15a/b/c, F16, F17a/b/c, F18, F19a/b/c, F20, F20-hocolim, F21, F22a/b, F23, F24-algebra/category, F25a/b/c, F26, F27a/b/c, F28a/b, F30', F33a/b, F34, F35, F36, F37. The typeset Part VII lists exactly four fronts. No cross-reference from the typeset Part VII to FRONTIER.md exists: the reader has no pointer to the detailed frontier inventory. This is a metadata/manuscript hygiene gap: FRONTIER.md is the author's working ledger, but the reader needs at minimum an anchor in typeset prose ("for the detailed frontier inventory see the cross-volume concordance").

### ATT-6. Wave-6 CY_4 p_1-twisted: K3×K3 claim absent but should be.

Wave-6 established: K3×K3 is **Z-twisted by `p_1 = −96`**, NOT unobstructed E_4 (the Vol I status-table claim "K3×K3: N(X) = 0, unobstructed E_4" is scope-qualified by Wave-6 to CY_4 p_1-twisted with `p_1 = −96` on K3×K3). Part VII does not mention the CY_4 p_1-twisted direction at all; it stops at "general compact CY_3 (chart-gluing programme replaces toric techniques)". A full Part VII should open an **Outward d=4** direction.

### ATT-7. CY-A_3 stated as proved; FRONTIER.md §3 V3-F18 says SEVERITY DOWNGRADED but not CLOSED on non-formal CY_3.

Line 1165: "With CY-A proved at every d (including the $\infty$-categorical proof of CY-A$_3$)". FRONTIER.md §3 V3-F18: inf-cat resolved, but **chain-level A_∞-compatible S³-framing on HC^-_3(C) for non-formal CY_3 (e.g. quintic) remains open.** The typeset Part VII opening overstates.

---

## Phase 2: heal

Surgical edits to `main.tex` Part VII (lines 1161–1248) and to `FRONTIER.md`. Minimal prose additions; no restructuring.

### Edit A. Deficiency opening (ATT-1) + CY-A_3 scope (ATT-7).

Replace the opening two lines with a deficiency opening that names the surviving problem.

### Edit B. Φ-as-correspondence (ATT-2) + universal trace identity (ATT-4).

Front~2 rewritten to make Φ a correspondence (not an on-the-nose functor) and to cite the universal trace identity as a *reflection* identity across the two Koszul-conductor families.

### Edit C. Front~1 osp(4|20) anchor (ATT-3).

Front~1 extended with a single sentence fixing the super-Yangian target at `Y_{osp(4|20)}` and pointing to V3-F19b/F26.

### Edit D. Three → four directions (ATT-6).

"Three directions" upgraded to "four directions", adding an Outward-d=4 direction (CY_4 p_1-twisted with K3×K3 p_1 = −96 Z-twisted anchor).

### Edit E. Pointer to FRONTIER.md inventory (ATT-5).

One-line closing pointer to the detailed frontier inventory (FRONTIER.md §3 V3-F13b–F37), appended after the chapter-insert block.

### Edit F. FRONTIER.md header.

Add a one-line Wave-10 audit acknowledgement to the top-of-document header so the metacognitive record matches.

---

## Metadata hygiene audit

Before committing any surgical edit, grep the typeset region for HOT ZONE metadata-slug leakage:

```
grep -n 'AP[0-9]\+\|V3-F[0-9]\+\|HZ-[0-9]\+\|first_principles_cache' \
  /Users/raeez/calabi-yau-quantum-groups/main.tex | sed -n '1150,1260p'
```

Zero hits expected; the edits below carry NO catalogue labels in typeset prose.

---

## Cross-volume sync

- **FRONTIER.md §1** already acknowledges the 2026-04-17 Beilinson-rectified state. Append Wave-10 acknowledgement.
- **Vol I** `part_vi_frontier_attack_heal.md` (this swarm) separately audits Vol I Part VI Frontier; this wave file covers Vol III.
- **Vol II** Part VII Frontier is a separate file (not this wave's scope).

---

## Verdict

ACCEPT. Six surgical edits; zero mathematical content retracted; four Wave 1–10 findings propagated into typeset Part VII; one pointer line added linking typeset to FRONTIER.md inventory. No commit.
