# SESSION PROMPT v23 — Proof Forge
# Launch: "Read notes/SESSION_PROMPT_v23.md and execute it."
# Supersedes: v21 (unified proof forge). References CLAUDE.md for invariants.
# Date: March 2026

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

1. **DK ladder beyond the proved core**: extension beyond the evaluation-generated core
   - Entry: concordance.tex rem:corrected-mc3-frontier
   - Targets: full category `O`, KL completion, compact-generator comparison
2. **Category O generation routes**
   - Entry: yangians.tex sec:cat-O-strategies
   - Track thick generation vs sectorwise finiteness hypotheses explicitly

### MC4 Work Surfaces

1. **Yangian**: K^line_{a,b}(N) = K^RTT_{a,b}(N) on boundary strip
   - Reduced to auxiliary-kernel identity L_a(u) = R_{0a}(u-a)
   - Type-A: three local checks (sl_M-equivariance, unit asymptotic, residue -hbar*P)
   - Entry: yangians.tex, concordance.tex
2. **W-infinity**: 4 free channels + 2 residue checks
   - c_{334}, c_{444}, C_{3,4;3;0,4}, C_{3,4;4;0,3}
   - Checks: C^res_{4,4;2;0,6}=2, C^res_{3,4;2;0,5}=0
3. **Finite-detection closure**
   - W-side packet: I_N
   - Yangian-side packet: Delta_{a,0}(N)
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
