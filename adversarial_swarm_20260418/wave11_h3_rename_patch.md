# Wave-11 H3 Two-Subscript Rename Patch — Draft for User Review

**Status**: DRAFT. **Not yet applied.** PREP agent (Wave-11) drafted this patch per the
Wave-10 Anchor A vs Anchor B adjudication
(`adversarial_swarm_20260418/wave10_anchor_a_vs_b_adjudication.md`). Execution requires
user approval for scale (~35 sites across Vol III).

**Scope**: atomic rename of `\kappa_{\mathrm{ch}}(-)` → `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(-)` at
every consumer site where the invariant is used in the Heisenberg-level rank-additive
sense (Route B; value 3 for K3×E, 1 for E, additive under product).

**Out of scope**: Route A sites (Hodge supertrace, Künneth-multiplicative, value 0 for
K3×E). Those retain bare `\kappa_{\mathrm{ch}}`. See `rem:cy-kappa-evidence` and
`thm:kappa-hodge-supertrace-identification`.

## Endpoints inscribed (already applied this session)

1. **Anchor B canonical restatement**:
   `chapters/theory/cy_to_chiral.tex:293-343` `prop:beauville-kappa-formula` rewritten
   with `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}` throughout; new companion remark
   `rem:beauville-kappa-formula-subscript-split` inscribed immediately above the
   proposition.

2. **HZ-7 extension** at `/Users/raeez/chiral-bar-cobar/CLAUDE.md` HZ-7 block:
   approved subscript set extended to `{ch, cat, BKM, fiber, ch^Heis}`; Route A vs
   Route B discipline block inscribed.

3. **AP-CY69 annotation** at `/Users/raeez/chiral-bar-cobar/notes/cross_volume_aps.md`:
   Wave-10/11 adjudication paragraph appended; H3 adoption recorded; this patch
   file referenced as the propagation deliverable.

## Rename rule (per site)

For each matched site:

- **If the RHS value is 3** (for `K3 × E`), **1** (for `E`), **2** (for `T^4`),
  **3** (for `T^6`), **2** (for `Enr × E`), OR arises via additivity `2 + 1`,
  `1 + 1`, `3 · 1`, etc. — **rename `\kappa_{\mathrm{ch}}(X)` →
  `\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(X)`** for that X only.

- **If the RHS value is 0** (for `K3 × E` via Künneth-multiplicative) or **2** (for
  K3 alone where Route A and Route B coincide at d=2 via `thm:kappa-hodge-supertrace-identification`)
  — retain bare `\kappa_{\mathrm{ch}}(X)`.

- **Mixed lines** (one clause Route A, another Route B) — split into two literals;
  keep bare for Route A, add `^{\mathrm{Heis}}` for Route B.

## Route-B site inventory (35 sites)

Each entry: `file:line` — local patch directive.

### chapters/frame/preface.tex (3 sites)

```
preface.tex:489-490  \kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3
  → \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) + \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1 = 3
  (Both K3 and E are Heisenberg-level factors here per the additivity chain.)

preface.tex:1046  \kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C
  → \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3 = \dim_\C

preface.tex:1050  \kappa_{\mathrm{ch}}(K3) = 2, \kappa_{\mathrm{ch}}(E) = 1.
  → \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) = 2, \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 1.
  (Both entries are rank-additive inputs; d=2 K3 coincides but context is additivity.)
```

### chapters/theory/introduction.tex (5 sites)

```
introduction.tex:321-322  (\kappa_{\mathrm{ch}}(E) = 1, \kappa_{\mathrm{ch}}(K3 \times E) = 3)
  → (\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 1, \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3)

introduction.tex:707-708  \kappa_{\mathrm{ch}}(K3 \times E) = 3 ... \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1
  → \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3 ... \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) + \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 2 + 1

introduction.tex:1041  \kappa_{\mathrm{ch}}(K3 \times E) = 3
  → \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3

introduction.tex:1186  \kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C
  → \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3 \times E) = 3 = \dim_\C

introduction.tex:1190  \kappa_{\mathrm{ch}}(K3) = 2, \kappa_{\mathrm{ch}}(E) = 1.
  → \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3) = 2, \kappa_{\mathrm{ch}}^{\mathrm{Heis}}(E) = 1.
```

### chapters/examples/k3e_cy3_programme.tex (6 sites)

```
k3e_cy3_programme.tex:333-334  \kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3 = \dim_\bC(K3 \times E)
  → all three κ_ch → κ_ch^{Heis}

k3e_cy3_programme.tex:983  \kappa_{\mathrm{ch}} = 3 = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1
  → all → κ_ch^{Heis}

k3e_cy3_programme.tex:1824  \kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(K3 \times E) = 2 + 3 = 5
  → κ_ch^{Heis} on both κ_ch in the sum

k3e_cy3_programme.tex:1827  \kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\bC
  → κ_ch^{Heis}

k3e_cy3_programme.tex:1856  \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(K3 \times E) = 2 + 3 = 5
  → both → κ_ch^{Heis}

k3e_cy3_programme.tex:2607  \kappa_{\mathrm{ch}} = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(K3) = 2 + 2 = 4
  → all → κ_ch^{Heis}

k3e_cy3_programme.tex:3052  \kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3
  → all → κ_ch^{Heis}
```

### chapters/examples/k3e_bkm_chapter.tex (6 sites)

```
k3e_bkm_chapter.tex:980   \kappa_{\mathrm{ch}}(K3 \times E) = 3; \kappa_{\mathrm{ch}}(K3) = 2 (fiber)
  → κ_ch^{Heis}(K3×E) = 3; κ_ch(K3)=2 stays bare IF meant as Route-A fiber; verify on-site.
  (Line marks "fiber" — likely Route-A categorical; rename ONLY K3×E.)

k3e_bkm_chapter.tex:1137  \kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\mathbb{C}
  → κ_ch^{Heis}

k3e_bkm_chapter.tex:1139-1140  \kappa_{\mathrm{ch}}(K3) = 2, \kappa_{\mathrm{ch}}(E) = 1, additivity gives \kappa_{\mathrm{ch}}(K3 \times E) = 3
  → all → κ_ch^{Heis}

k3e_bkm_chapter.tex:1242  \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1
  → both → κ_ch^{Heis}

k3e_bkm_chapter.tex:1250  \kappa_{\mathrm{ch}}(K3 \times E) = 3
  → κ_ch^{Heis}

k3e_bkm_chapter.tex:1352  \kappa_{\mathrm{ch}}(K3 \times E) = 3 (the chiral modular characteristic via Φ)
  → κ_ch^{Heis}. NB: prose says "via Φ" which is Φ_d functor = Route A; this site is a
  PROSE DRIFT: the numeric 3 is Route B, not Route A. Heal: rewrite prose to
  "the Heisenberg-level rank-additive characteristic" and rename the symbol.
```

### chapters/examples/k3_chiral_algebra.tex (6 sites)

```
k3_chiral_algebra.tex:241   \kappa_{\mathrm{ch}}(K3 \times E) & 3 & algebraization & Additivity: 2 + 1
  → κ_ch^{Heis}

k3_chiral_algebra.tex:447   \kappa_{\mathrm{ch}}(E) = 1; \kappa_{\mathrm{ch}}(K3) = 2
  → κ_ch^{Heis} for the E entry (value 1 forces Route B); K3 at d=2 coincides but
  context is additivity discussion — rename to Heis for consistency.

k3_chiral_algebra.tex:449   0 ≠ 3 = \kappa_{\mathrm{ch}}(K3 \times E)
  → κ_ch^{Heis}

k3_chiral_algebra.tex:452   \kappa_{\mathrm{ch}} = 3 comes from additivity (\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1)
  → all → κ_ch^{Heis}

k3_chiral_algebra.tex:503-504  \kappa_{\mathrm{ch}}(E) = 1 ≠ 0 = \kappa_{\mathrm{cat}}(E); \kappa_{\mathrm{ch}}(E) = \dim_\C(E) = 1
  → κ_ch^{Heis} for the =1 entries (Route B). κ_cat stays as-is.

k3_chiral_algebra.tex:506   \kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3
  → all → κ_ch^{Heis}

k3_chiral_algebra.tex:512   \kappa_{\mathrm{BKM}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3 \times E) + \kappa_{\mathrm{cat}}(K3) = 3 + 2 = 5
  → κ_ch^{Heis} on the K3×E entry; κ_cat stays.

k3_chiral_algebra.tex:539-541  \chi_{\mathrm{top}}(...)/24 ≠ 1 = \kappa_{\mathrm{ch}}(E), ≠ 2 = \kappa_{\mathrm{ch}}(K3), ≠ 3 = \kappa_{\mathrm{ch}}(K3 \times E)
  → all → κ_ch^{Heis}

k3_chiral_algebra.tex:744   \kappa_{\mathrm{ch}}(E) = 1 by all routes
  → κ_ch^{Heis}(E) = 1. "All routes" language requires rephrasing: at d=1 only Route B
  gives 1; Route A gives 0. Heal prose: "κ_ch^{Heis}(E) = 1 by rank-additivity on all
  Heisenberg-level presentations".
```

### chapters/examples/quantum_group_reps.tex (2 sites)

```
quantum_group_reps.tex:932   \kappa_{\mathrm{ch}}(K3 \times E) = \chi^{\mathrm{Hodge}}(K3) \cdot \chi^{\mathrm{Hodge}}(E) = 2 \cdot 0 = 0
  → KEEP BARE κ_ch. This is Route A (Hodge supertrace multiplicative). No rename.

quantum_group_reps.tex:1115  \kappa_{\mathrm{ch}}(K3 \times E) = 3 (chiral algebra invariant
  → κ_ch^{Heis}(K3 \times E) = 3. Rephrase prose: "Heisenberg-level chiral algebra
  invariant" (not the Hodge supertrace).
```

### chapters/examples/k3_yangian_chapter.tex (1 site)

```
k3_yangian_chapter.tex:3779  \kappa_{\mathrm{ch}}(K3 \times E) ... Π_{++} entry 0
  → VERIFY on-site which route: if the context routes through Φ_d Hodge supertrace
    (giving 0), KEEP bare. If rank-additive giving 3, RENAME to κ_ch^{Heis}.
  Line context suggests Route A (value 0 entry) — LIKELY KEEP BARE.
```

### chapters/examples/k3_quantum_toroidal_chapter.tex (1 site)

```
k3_quantum_toroidal_chapter.tex:462   \kappa_{\mathrm{ch}}(K3 \times E) + \kappa_{\mathrm{cat}}(K3)
  → κ_ch^{Heis}(K3 × E) + κ_cat(K3). Context is the BKM decomposition 3 + 2 = 5
    where the first term is Heisenberg-additive (3).
```

### chapters/theory/quantum_chiral_algebras.tex (4 sites)

```
quantum_chiral_algebras.tex:891   κ_ch-additivity: \kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3
  → all → κ_ch^{Heis}

quantum_chiral_algebras.tex:1463   \kappa_{\mathrm{ch}}(K3 \times E) | Additivity: 2 + 1 | 3
  → κ_ch^{Heis}

quantum_chiral_algebras.tex:1643   Route~D gives \kappa_{\mathrm{ch}} = 3 by additivity: \kappa_{\mathrm{ch}}(K3 \times E) = 2 + 1
  → both → κ_ch^{Heis}. NB: same line has Route A κ_ch = 24 and Routes B,C κ_ch = 2 —
    those values are different invariants (fiber / supertrace / Route B labelled
    separately); only Route D additivity-3 value needs the Heis superscript.

quantum_chiral_algebras.tex:1741   \kappa_{\mathrm{ch}}(K3) = 2 (K3 chiral algebraisation), \kappa_{\mathrm{ch}}(K3 \times E) = 3 (by additivity: 2 + 1), ... tower are \{0, 2, 3, 5, 24\}
  → κ_ch^{Heis} for the K3×E=3 additivity site. The K3=2 entry is d=2 coincidence;
    either keep bare (since Route A also gives 2) or superscript for consistency.
    Recommend: keep bare K3=2 (canonical Route-A value) and superscript K3×E=3 (Route B).
```

### chapters/connections/modular_koszul_bridge.tex (2 sites)

```
modular_koszul_bridge.tex:231  \kappa_{\mathrm{ch}}(K3 \times E) = 3 by additivity
  → κ_ch^{Heis}(K3 × E) = 3 by rank-additivity

modular_koszul_bridge.tex:341  \kappa_{\mathrm{ch}}(\cA_{K3} \otimes H_1) | 3 | Additivity: \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1
  → all → κ_ch^{Heis}. The argument \cA_{K3} \otimes H_1 is Heisenberg-product form.
```

### chapters/theory/modular_trace.tex (1 site — VERIFY)

```
modular_trace.tex:80  \kappa_{\mathrm{ch}}(K3) \cdot \kappa_{\mathrm{ch}}(E) = 2 \cdot 1 = 2
  → KEEP BARE if multiplicative (Route A Künneth)? But 2·1=2 uses Route-B values
    (Route A would give 2·0=0). Needs on-site check: this formula is a MIXED error
    where Route-B values (2 and 1) are combined multiplicatively. Heal: either
    rename to κ_ch^{Heis} and note multiplicativity is incorrect for Route B (Route B
    is ADDITIVE), or keep bare and fix the values to 2·0=0. Flag for user review.
```

### chapters/theory/cy_to_chiral.tex (pre-existing Route-B sites outside the prop)

```
cy_to_chiral.tex:280   For K3 × E: \kappa_{\mathrm{ch}} = 2 + 1 = 3 (additive) vs. 2·0 = 0 (multiplicative). Already at d = 1: \kappa_{\mathrm{ch}}(E) = 1 ≠ 0 = \chi(\cO_E)
  → The first "\kappa_{\mathrm{ch}} = 3" is Route B → κ_ch^{Heis}. The "\kappa_{\mathrm{ch}}(E) = 1" is Route B → κ_ch^{Heis}.
  This is inside rem:cy-kappa-evidence which Wave-10 recommends rewriting to use the
  split. Partial heal: rename the Route-B occurrences; keep the discussion framing.

cy_to_chiral.tex:411  \kappa_{\mathrm{cat}}(S \times E) = \kappa_{\mathrm{ch}}(S) + \kappa_{\mathrm{ch}}(E) = 1 + 1 = 2
  → κ_ch^{Heis} on both κ_ch entries. NB: equation LHS is κ_cat ≠ κ_ch^{Heis}, so this
    is a CATEGORY JUMP drift already present. Flag for separate heal (AP290 class).

cy_to_chiral.tex:1435  \kappa_{\mathrm{ch}} = 2 (abelian surface, additivity: \kappa_{\mathrm{ch}}(E) + \kappa_{\mathrm{ch}}(E) = 1 + 1)
  → all → κ_ch^{Heis}

cy_to_chiral.tex:4011  \kappa_{\mathrm{ch}} = 3 by additivity (\kappa_{\mathrm{ch}}(\mathrm{K3}) + \kappa_{\mathrm{ch}}(E) = 2 + 1)
  → all → κ_ch^{Heis}

cy_to_chiral.tex:4037  \kappa_{\mathrm{ch}} = 3 by additivity (\kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1)
  → all → κ_ch^{Heis}
```

### main.tex (2 sites)

```
main.tex:445-446  (\kappa_{\mathrm{ch}}(E) = 1, \kappa_{\mathrm{ch}}(K3 \times E) = 3)
  → both → κ_ch^{Heis}
```

### chapters/examples/cy_c_six_routes_convergence.tex (1 site — VERIFY)

```
cy_c_six_routes_convergence.tex:479  \kappa_{\mathrm{bare}}(K3) ambiguous ... \kappa_{\mathrm{ch}}(K3) = 2 (routes R_1, R_5) vs \kappa_{\mathrm{fiber}}(K3) = 24, with \kappa_{\mathrm{ch}}^{R_3}(K3) = 24 on lattice-VOA route
  → The prose ALREADY uses Route-superscripted notation (R_3). Heal: unify with this
    patch by adding R^{Heis} or ch^{Heis} column on the Beauville-reduction route.
    Low-priority: this site is already route-aware.
```

## Count recap

| Chapter | Route-B sites |
|---|---|
| preface.tex | 3 |
| introduction.tex | 5 |
| k3e_cy3_programme.tex | 7 |
| k3e_bkm_chapter.tex | 6 |
| k3_chiral_algebra.tex | 8 |
| quantum_group_reps.tex | 1 (second kept bare) |
| k3_yangian_chapter.tex | 0-1 (verify on-site) |
| k3_quantum_toroidal_chapter.tex | 1 |
| quantum_chiral_algebras.tex | 4 |
| modular_koszul_bridge.tex | 2 |
| modular_trace.tex | 0-1 (mixed route, flag) |
| cy_to_chiral.tex (outside prop) | 5 |
| main.tex | 2 |
| cy_c_six_routes_convergence.tex | 0-1 (already routed) |

**Total**: ~38 sites (matches Wave-10 a780f1fe "~35" within enumeration variance).

## Execution recommendation

Apply as a single atomic commit per chapter (AP5 + AP149 + HZ-5 downgrade atomicity).
For each file, the edit pattern is a scoped `replace_all`-like pass, but NOT a bulk
`sed` (risk of AP42 bulk substring corruption — "ch" is inside "chiral" etc.).

Safer approach: iterate `Edit` with exact match strings per line, matching the full
`\kappa_{\mathrm{ch}}(K3 \times E)` or `\kappa_{\mathrm{ch}}(E)` or `\kappa_{\mathrm{ch}}(K3)`
token in its immediate arithmetic context. This also lets us make the Route-A vs
Route-B judgement per site (K3=2 is d=2 coincidence; K3=24 is fiber; etc.).

Post-rename verification:

```
# Every site still shows: κ_ch^{Heis} wherever the numeric value is Route B.
grep -rn 'kappa_\{\\mathrm\{ch\}\}(K3 \\times E) = 3' chapters/ main.tex  # expect 0 hits
grep -rn 'kappa_\{\\mathrm\{ch\}\}\^\{\\mathrm\{Heis\}\}(K3 \\times E) = 3' chapters/ main.tex  # expect all renamed sites

# Zero bare Route-B stragglers:
grep -rn 'kappa_\{\\mathrm\{ch\}\}(E) = 1' chapters/  # expect 0 hits

# Route A multiplicative sites preserved:
grep -rn 'chi\^\{\\mathrm\{Hodge\}\}(K3) \\cdot \\chi\^\{\\mathrm\{Hodge\}\}(E)' chapters/  # expect 1 hit (quantum_group_reps.tex:932)
```

## Deferred items (NOT part of this patch)

1. `rem:cy-kappa-evidence` (cy_to_chiral.tex:273) — prose framing ("additivity vs
   multiplicativity") should be rewritten post-rename to: "Route A multiplicative
   (Hodge supertrace, κ_ch); Route B additive (Heisenberg-level, κ_ch^{Heis}); the
   two invariants coincide numerically at d=2 K3 only." Wave-12 heal candidate.

2. `conj:cy-kappa-identification` (cy_to_chiral.tex:262) — the κ_ch(quintic) = -25/3
   entry attaches to Route B (κ_ch^{Heis}). Rewrite conjecture to scope Heis variant.
   Wave-12 heal candidate.

3. Compute engine `compute/lib/kappa_ch_universal_formula.py` — 65 tests operate on
   the Heisenberg-level sum. Docstring rename to κ_ch^{Heis} + test-file rename.
   Does NOT affect correctness.

4. Vol I propagation (notes/cross_volume_aps.md AP289 kin): Vol I does not use the
   Heisenberg-level form in loaded-bearing theorems; propagation is Vol III-local.

## Approval required before execution

This patch modifies manuscript prose at ~38 sites across 14 files + main.tex. Per
CLAUDE.md atomic-rename discipline (HZ-5, AP5, AP149), execution should be:

- **Single session**: all 38 edits in one tool-call batch;
- **No intermediate commits**: the rename is atomic across Vol III;
- **Post-rename build verification**: `cd ~/calabi-yau-quantum-groups && make fast`;
- **Post-rename test verification**: `make test`;
- **Final commit by user** (per session policy): authored by Raeez Lorgat only.

User directive to execute requested.
