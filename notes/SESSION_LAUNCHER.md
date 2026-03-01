# Session Launcher — Chiral Bar-Cobar Monograph

## For Claude Opus 4.6 — Code Environment — Maximum Reasoning

---

You are the mathematical architect for a 929-page research monograph on chiral bar-cobar duality. The book is structurally complete: 65 active .tex files, zero compilation errors, zero ClaimStatusOpen, three main theorems with proofs (one gap remaining in Theorem C). What remains is the transformation from "substantial contribution with conjectures" to "landmark work with proofs."

**Read these files first** (in this order — each builds on the previous):
1. `CLAUDE.md` — Identity, standards, current state, file map
2. `notes/EXECUTION_PLAN.md` — The Five Moves, Phases 8-9, execution protocol
3. `notes/CONJECTURE_REGISTRY.md` — All ~97 conjectures with labels, files, priorities

**Then read** the MEMORY.md file at the path Claude Code uses for persistent memory — it contains verified formulas, convention decisions, and session history that you must not contradict.

---

## Your Task

Pick exactly one of the following and execute it completely within this session. Do not attempt multiple Moves in a single session.

### Option A: Execute a Move (Phase 7)

Choose one of Moves 1-5 from EXECUTION_PLAN.md. For the chosen Move:

1. **Read all source files** listed in the Move's "Files to modify" section, in full
2. **Read all dependency files** referenced by the Move
3. **Write the mathematics**: theorem statements with complete proofs, in LaTeX
4. **Verify compilation**: run `make` after each significant change
5. **Update claim status**: change \ClaimStatusConjectured to \ClaimStatusProvedHere for each proved result
6. **Run consistency checks** specified in the Move's "Completion criterion"

### Option B: Execute a Phase 8 Task (Examples Engine)

Choose one of 8A-8E from EXECUTION_PLAN.md. Read the relevant files, then write new mathematics: theorems, proofs, computations. Each computation must be explicit (not "one can show") and each formula must be verified against known special cases.

### Option C: Execute a Phase 9 Task (Connections Cleanup)

Choose one of 9A-9C. This involves labeling physics conjectures precisely, upgrading provable conjectures, and ensuring the connections chapters correctly reference the theory.

### Option D: Physics Labeling Pass

For every conjecture marked "Physics" in CONJECTURE_REGISTRY.md:
1. Read the surrounding context
2. Add a \begin{remark} after the conjecture stating: (a) the precise mathematical content, (b) what physics input would be needed to prove it, (c) why it is beyond the scope of this book
3. Ensure the claim stays \ClaimStatusConjectured but has precise hypotheses

---

## How to Write Mathematics

**Theorem format:**
```latex
\begin{theorem}[Descriptive Name; \ClaimStatusProvedHere]\label{thm:descriptive-label}
Let [hypotheses]. Then [conclusion]:
\[
  [precise formula]
\]
\end{theorem}

\begin{proof}
[Complete proof in at most 5 steps. Each step must follow logically from the previous, with explicit references to earlier results in the manuscript.]

\textbf{Step 1.} [First step with reference: by Theorem~\ref{thm:earlier-result}, ...]

\textbf{Step 2.} [...]

...
\end{proof}
```

**Computation format:**
```latex
\begin{calculation}[Name; \ClaimStatusProvedHere]\label{calc:name}
[Explicit computation with every step shown. No "one can verify" or "a straightforward computation shows."]
\end{calculation}
```

**When stuck:**
- If a proof strategy fails → state as Conjecture with precise hypotheses and the obstruction
- If a computation gets too long → compute through degree 3, state the pattern, prove the pattern for n=3
- If two approaches conflict → write both, mark the discrepancy
- **Never guess a formula** — compute it or cite it
- **Never change a verified formula** from MEMORY.md

---

## Compilation and Verification

After every significant edit:
```bash
make          # Must compile with zero errors
```

After completing a Move:
```bash
# Count claim status changes
grep -c "ClaimStatusProvedHere" chapters/examples/[modified_file].tex
grep -c "ClaimStatusConjectured" chapters/examples/[modified_file].tex
```

---

## Session Close Protocol

Before ending the session:
1. Verify `make` compiles cleanly
2. List every theorem whose status changed (Conjectured → ProvedHere)
3. List any new conjectures introduced
4. List any verified formulas discovered (to add to MEMORY.md)
5. Note any gaps encountered that need future work
6. State what the next session should tackle

---

## Critical Constraints

- **Cohomological grading**: |d| = +1 throughout the manuscript
- **Bar desuspension**: our convention absorbs sign representation (Ass^! ≅ Ass, not Ass ⊗ sgn)
- **Configuration space forms**: η_ij = d log(z_i - z_j) are SYMMETRIC
- **Koszul dual notation**: A^! (with exclamation mark, using \cA^! in LaTeX)
- **Central charges**: DS formula ≠ minimal model formula — use case-by-case, never a universal W_N formula
- **Sugawara is UNDEFINED at critical level** k = -h∨
- **Factorization homology** (chains) is DUAL to bar complex (cochains)
