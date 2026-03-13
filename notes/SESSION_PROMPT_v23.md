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
   - KL note: the root-of-unity `q`-bar certificate is now an M-level fact, the first admissible `sl_2` packet is computed with `dim H^{1,2}_2 = dim H^{2,1}_3 = 3`, the whole first sparse `N=4` degree-1 packet vanishes with `H^{3,1}_1 = H^{2,2}_1 = H^{1,3}_1 = 0`, and the tractable degree-2 channels also vanish with `H^{3,1}_2 = H^{2,2}_2 = 0`; the remaining `H^{1,3}_2` channel is now compressed by a split-form sparse certificate to `rank(im d_q^3) >= 3903`, hence `dim H^{1,3}_2 <= 66`, with residual cokernel supported on left factors `F`, `E`, and `K-1`, and even the full generator-prefix cube `{F,E,K-1}^3 x I^2` adds no new residual rank; do not spend cycles re-proving `d_q^N = 0` when the live gap is deciding whether one flavor or that paired packet carries the KL periodic shadow and then resolving this residual packet
2. **Category O generation routes**
   - Entry: yangians.tex sec:cat-O-strategies
   - Track thick generation vs sectorwise finiteness hypotheses explicitly

### MC4 Work Surfaces

1. **Yangian**: after the standard completed M-level package, prove `K^line_{a,b}(N) = K^RTT_{a,b}(N)` on boundary strip
   - Reduced to auxiliary-kernel identity L_a(u) = R_{0a}(u-a)
   - Type-A: three local checks (sl_M-equivariance, unit asymptotic, residue -hbar*P)
   - Entry: yangians.tex, concordance.tex
2. **W-infinity**: exact six-entry identity packet on `\mathcal I_4`
   - Four higher-spin channels: `c_{334}`, `c_{444}`, `C_{3,4;3;0,4}`, `C_{3,4;4;0,3}`
   - Two theorematic Virasoro-target identities: `C^{res}_{4,4;2;0,6}=2`, `C^{res}_{3,4;2;0,5}=0`
   - Promotion `\mathcal I_4 \to \mathcal I_N` is linearized by the incremental packets `\mathcal J_{N+1}` and their reduced forms `\mathcal J_{N+1}^{\mathrm{red}}`
   - `prop:winfty-stage-growth-virasoro-target-contraction` gives the uniform target-`2` contraction of the reduced packets under the normalized residue package
   - The first next reduced stage is the explicit `11`-entry packet `\mathcal J_5^{\mathrm{red}}`, with `cor:winfty-stage5-residue-eight-channel` as the first concrete specialization to `8` higher-spin channels
   - The further stage-`4` contraction to four channels is conditional on `conj:winfty-stage4-ward-inheritance`, whose open content is the visible pairing package isolated in `prop:winfty-stage4-visible-pairing-gap`
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
