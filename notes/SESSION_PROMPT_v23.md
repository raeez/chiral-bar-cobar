# SESSION PROMPT v23 — Proof Forge
# Launch: "Read notes/SESSION_PROMPT_v23.md and execute it."
# Supersedes: v21 (unified proof forge). References CLAUDE.md for invariants.
# Date: March 2026

> **Active doctrine note (March 13, 2026).**
> This is the live execution prompt. Older session/audit prompts in
> `notes/` are historical provenance documents unless they are
> explicitly promoted by the current control layer.

---

## PERMANENT MANDATE

Treat the monograph as the definitive dimension-one treatise of modular
homotopy theory for factorization algebras on curves, not as a proved
core with an optional programme appendix.

Therefore every session should prefer work that materially builds one
of the load-bearing foundations and frontier extensions:
modular-operadic functoriality, curved/coderived factorization on
`Ran(X)`, the H-level bar-cobar adjunction, and the staged
factorization / infinite-tower comparison packages.

Status discipline remains absolute: `Def_cyc(A)` and `Theta_A` are now
proved on the theorem surface, while MC3/MC4 remain live frontier and
MC5 remains downstream.

---

## ORIENT (first 10 minutes)

1. Run fresh census:
   ```
   for s in ProvedHere ProvedElsewhere Conjectured Heuristic Open; do
     echo -n "$s: "; grep -rc "ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
   done
   ```
2. Build: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast`
3. Tests: `cd compute && .venv/bin/python -m pytest tests/ -q`
4. Read `notes/autonomous_state.md` for recent session results
5. Read concordance.tex rem:proof-roadmaps for MC status
6. Record state in extended thinking. Then classify and select.

---

## CLASSIFY — Work Surfaces

Each work unit falls on exactly one surface:

| Surface | Description | Key files | Risk |
|---------|-------------|-----------|------|
| CONTROL | Constitution, MC roadmaps | concordance.tex, introduction.tex | HIGH |
| THEOREM | Proofs in theory chapters | higher_genus, bar_cobar, chiral_koszul_pairs | HIGH |
| PORTRAIT | Examples, computations | All examples/, detailed_computations | MEDIUM |
| FRONTIER | Open conjectures, MC3-5 (+ periodicity flank) | concordance, higher_genus, yangians | HIGH |
| COMPUTE | Python verification | compute/lib/, compute/tests/ | LOW |
| PROSE | Exposition, cross-refs | Any .tex file | LOW |

---

## SELECT — Prioritization

```
Is there a CRITICAL audit finding?       → Fix it NOW
Is MC3/MC4 actionable?                   → Work on MC3/MC4
Is there a Conjectured with proof ready? → Upgrade it
Is there a proof gap in ProvedHere?      → Fix it
Is there a cross-ref inconsistency?      → Fix it
Else                                     → doctrinal propagation or prose
```

### MC3 Work Surfaces (live structural extension)

1. **DK ladder beyond the proved core**: extension from the evaluation-generated core to the ordinary-derived/completed/coderived enlargement
   - Entry: concordance.tex rem:corrected-mc3-frontier
   - Targets: full category `O`, KL completion, compact-generator comparison
   - KL note: the root-of-unity `q`-bar certificate is now an M-level fact, the first admissible `sl_2` packet is computed with `dim H^{1,2}_2 = dim H^{2,1}_3 = 3`, and each of those two `N=3` flavors already has the same sparse S-level fingerprint `{-3:1,0:1,3:1}` with class-support sizes `1,6,1`; the whole first sparse `N=4` degree-1 packet vanishes with `H^{3,1}_1 = H^{2,2}_1 = H^{1,3}_1 = 0`, and the tractable degree-2 channels also vanish with `H^{3,1}_2 = H^{2,2}_2 = 0`; the remaining `H^{1,3}_2` channel is now resolved exactly: after the split-form seed certificate `rank(im d_q^3) >= 3903`, the later precursor stages are quotient-zero, the common `57`-plane carries the witness-basis scalar cancellation `(-1-i) Id`, and the exhaustive compressed verification of all `354,668` surviving prefix signatures covering `42,718,284` raw surviving columns shows that every weighted surviving column vanishes in the seed quotient. Hence `image_rank = 3903` exactly and `dim H^{1,3}_2 = 66`; this exact packet already has the rigid support fingerprint `F⊗48 ⊕ E⊗15 ⊕ (K-1)⊗3` and palindromic total root-weight profile `1,4,8,12,16,12,8,4,1`, equivalently the unit-step interval staircase `[-4,4] + 3[-3,3] + 4[-2,2] + 4[-1,1] + 4{0}`. The simple convolutional route from the first `N=3` packet is now ruled out exactly: support forces any exact symmetric transport to radius `<=1`, but the exact radius-`0` and radius-`1` systems are inconsistent for both one flavor and the paired packet; signed radius-`4` kernels exist only as window-matching artifacts on `[-4,4]` and spill outside the target support. The first surviving structured non-convolutional finite-window candidate is now explicit: the paired `N=3` profile is recovered exactly from the `N=4` staircase on `[-4,4]` by a Dirichlet operator `aΔ+V_6(w)` with `a=-3/140`, while pure multiplication needs degree `8`. So the live next object is whether that second-order finite-window operator reflects a real H/M-level periodic-coderived KL mechanism, or whether the `N=4` staircase is genuinely new
2. **Category O generation routes**
   - Entry: yangians.tex sec:cat-O-strategies
   - Track thick generation vs sectorwise finiteness hypotheses explicitly

### MC4 Work Surfaces

1. **Yangian**: after the standard completed M-level package, equip the canonical dg model `U^{\mathrm{comp}}(\mathfrak g_{\cA})` of the formal-moduli target with an RTT-adapted realization and prove `K^line_{a,b}(N) = K^RTT_{a,b}(N)` on boundary strip
   - Reduced to auxiliary-kernel identity L_a(u) = R_{0a}(u-a)
   - Type-A: three local checks (sl_M-equivariance, unit asymptotic, residue -hbar*P)
   - The H-level target itself is no longer the frontier; the frontier is RTT-adapted realization plus the boundary-strip packet
   - Entry: yangians.tex, concordance.tex
2. **W-infinity**: exact six-entry identity packet on `\mathcal I_4`
   - Four higher-spin channels: `c_{334}`, `c_{444}`, `C_{3,4;3;0,4}`, `C_{3,4;4;0,3}`
   - Two theorematic Virasoro-target identities: `C^{res}_{4,4;2;0,6}=2`, `C^{res}_{3,4;2;0,5}=0`
   - Promotion `\mathcal I_4 \to \mathcal I_N` is linearized by the incremental packets `\mathcal J_{N+1}` and their reduced forms `\mathcal J_{N+1}^{\mathrm{red}}`
   - `prop:winfty-stage-growth-virasoro-target-contraction` gives the uniform target-`2` contraction of the reduced packets under the normalized residue package
   - The first next reduced stage is the explicit `11`-entry packet `\mathcal J_5^{\mathrm{red}}`; its contracted higher-spin core is the `8`-channel packet `\mathcal J_5^{\mathrm{hs}}`, already split as `1+3+3+1` by source pair, then as the two singleton entry identities `(3,4;5;0,2)` and `(5,5;4;0,6)`, and also by target spin so that the first local strip is the target-`5` corridor `(3,4;5;0,2)`, `(3,5;5;0,3)`, `(4,5;5;0,4)`; `prop:winfty-stage5-reduced-tail-singleton` identifies `(3,4;5;0,2)` as the exact reduced tail input, `prop:winfty-stage5-tail-mechanism` identifies the exact missing comparison mechanism there as the `W^{(5)}`-projection in the top pole of `W^{(3)}(z)W^{(4)}(w)`, `cor:winfty-stage5-target5-residual` identifies the residual target-`5` surface as the two-channel ladder `\mathcal J_5^{\mathrm{tr},5}`, `prop:winfty-stage5-target5-transport-mechanism` identifies that residual continuation as the comparison of the `W^{(5)}`-projection in `W^{(3)}(z)W^{(5)}(w)` and `W^{(4)}(z)W^{(5)}(w)`, and `prop:winfty-stage5-target5-transport-singletons` then splits that residual continuation into the pole-`3` singleton `(3,5;5;0,3)` and the pole-`4` singleton `(4,5;5;0,4)`; `prop:winfty-stage5-visible-w5-normalization` makes the visible `W^{(5)}` normalization theorematic under the stage-`5` Virasoro package, and on the visible pairing loci of `prop:winfty-stage5-target5-pole3-pairing-vanishing` through `cor:winfty-stage5-tail-cross-target-reduction` the same target-`5` staircase becomes partially rigid: the pole-`3` singleton vanishes, the pole-`4` singleton is tied to the self-return singleton, and the tail singleton is tied to neighboring target-`4` / target-`3` channels; `cor:winfty-stage5-target5-corridor-to-tail` kills the transport part on the visible `W^{(4)}` / `W^{(5)}` pairing locus, and `cor:winfty-stage5-target5-no-new-independent-data` shows that on the full visible `W^{(3)}` / `W^{(4)}` / `W^{(5)}` pairing locus the whole target-`5` corridor carries no new independent coefficient; `prop:winfty-stage5-target4-pole5-w4-vanishing`, `prop:winfty-stage5-target3-pole5-w3-vanishing`, and `prop:winfty-stage5-transport-cross-target-reduction` then collapse the remaining target-`4` / target-`3` transport front to one effective coefficient, and `cor:winfty-stage5-effective-independent-frontier` shows that on that full visible pairing locus the whole stage-`5` higher-spin packet carries one effective independent coefficient, represented by `(3,5;4;0,4)`; `conj:winfty-stage5-principal-target5-no-new-independent-data` and `conj:winfty-stage5-principal-residual-front-one-coefficient` then split the remaining principal-side structural input into the target-`5` corridor and the residual front, `prop:winfty-stage5-principal-one-coefficient-factorization` packages their conjunction as `conj:winfty-stage5-principal-one-coefficient-normal-form`, and `prop:winfty-stage5-one-coefficient-reduction` reduces the full visible-pairing stage-`5` comparison to the single identity `C^{res}_{3,5;4;0,4}(5)=C^{DS}_{3,5;4;0,4}(5)` of `conj:winfty-stage5-one-coefficient-comparison`; `conj:winfty-stage5-higher-spin-identities` remains the next finite bar-vs-DS list
   - The further stage-`4` contraction to four channels is conditional on `conj:winfty-stage4-ward-inheritance`; once the visible Virasoro Ward action is fixed, `prop:winfty-stage4-visible-pairing-gap` reduces its open content to the single visible weight-`4` normalization conjecture `conj:winfty-stage4-visible-diagonal-normalization`, equivalently `C^{res}_{4,4;2;0,6}(4)=2`, and `cor:winfty-stage4-single-scalar-equivalent` packages this as the exact theorematic form of the refinement
   - On the canonical Yangian target, once `U^{comp}(\mathfrak g_{\cA})` carries the RTT-adapted finite-quotient/shared-seed package, `cor:yangian-canonical-realization-to-spectral-seed` reduces the remaining canonical-target input to the standard spectral vector seed-and-shift datum; `cor:yangian-canonical-realization-plus-vector-line` shows that on the spectral vector-line locus DK-4/DK-5 already closes on the canonical target, and `cor:yangian-canonical-realization-plus-one-seed` sharpens the equivariant multiplicative spectral realization locus further to the single canonical seed `V^\omega(0)=J_q^\omega(V(0))`
3. **Finite-detection closure**
   - W-side packet: `I_N`
   - Yangian-side packet: `Delta_{a,0}(N)`
4. **Separate non-principal orbit frontier**
   - Keep distinct packets explicit: dual-orbit input, orbit-indexed level shift, paired DS seed transport/globalization

---

## EXECUTE — Work Protocol

### THEOREM / FRONTIER surface
1. Read the FULL file containing the theorem
2. Read all cited dependencies
3. Write in theorem-proof format
4. Verify signs/conventions against CLAUDE.md Critical Pitfalls
5. `make fast` after each edit
6. Update concordance.tex if status changes

### COMPUTE surface
1. Write tests FIRST
2. Verify against known mathematical facts
3. `cd compute && .venv/bin/python -m pytest tests/ -q`
4. Never change verified formulas — if computation disagrees, the code is wrong

### PROSE surface
1. CG standard (Chriss-Ginzburg prose quality)
2. Never change mathematical content during prose editing
3. No overclaiming (F7), scope creep (F8), or frontier overreach (F9)

### All surfaces
- After each batch (10 edits): `make fast` as gate
- At session end: full `make`, update autonomous_state.md
- Never guess a formula — compute it or cite it

---

## VERIFY — After Each Work Unit

1. `make fast` compiles clean
2. Census unchanged (unless work intentionally changed status)
3. No new undefined refs or multiply-defined labels
4. If claim status changed: update concordance.tex

---

## FAILURE MODES

| # | Mode | Signal | Prevention |
|---|------|--------|------------|
| F3 | Diffuse attention | Switching tasks mid-work | ONE work unit at a time |
| F7 | Overclaiming | "We have shown" without proof | Every ProvedHere needs complete proof |
| F8 | Scope creep | "While here, I should also..." | Only the selected work unit |
| F9 | Frontier overreach | Conjectured->ProvedHere without proof | Check proof density before status change |
| F11 | Local patching | Editing without reading concordance | Always read constitution first |
| F12 | Census drift | Stale numbers in notes | Always grep fresh |

---

## SESSION END PROTOCOL

1. Full build: `make` (multi-pass)
2. Final census verification
3. Update `notes/autonomous_state.md` (recent sessions, next priorities)
4. Update MEMORY.md only if new verified facts discovered
5. Do NOT update CLAUDE.md unless a new Critical Pitfall was found
