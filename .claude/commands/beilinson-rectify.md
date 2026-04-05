---
description: "Run the full Chriss-Ginzburg fortification + Beilinson rectification programme on a chapter file"
---

RECTIFICATION_SESSION_ACTIVE

# Chriss-Ginzburg Fortification + Beilinson Rectification

You are applying the full fortification and rectification programme to: $ARGUMENTS

The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg. Every object earns its place by solving a problem. Every paragraph forces the next. The mathematics has momentum.

This is a 5-phase programme. Phases 1-2 BUILD CONNECTIVE TISSUE (the creative work). Phase 3 is the BEILINSON SWEEP (verification). Phase 4 is DEEP STRUCTURAL REWRITE. Phase 5 is CONVERGENCE. The loop repeats Phases 3-5 until convergence.

---

## PHASE 1: DIAGNOSTIC AUDIT (read-only, adversarial)

Read the ENTIRE file. Produce findings in six categories:

### A. NARRATIVE THREAD
Map the logical connection between each section and the next. Where does the thread BREAK? Where does the reader feel "why are we talking about this now?" For each break, design the connective tissue: 1-3 sentences of mathematical content that make the next section INEVITABLE.

### B. MOTIVATION GAPS
Does each section/subsection open with WHY before WHAT? The Gelfand test: does the reader feel "of course this must be defined" BEFORE encountering the definition? List every subsection that opens with a definition dump rather than a question or motivating observation.

### C. DEFINE-BEFORE-USE
For every symbol in every formula: is it defined before this point in the chapter? List every violation. For standard concepts (D-modules, L∞-algebras, Hodge bundle, Gauss-Manin connection, etc.), design parenthetical first-principles definitions.

### D. OPENING AND CLOSING
Does the chapter open with a concrete mathematical object (Gelfand) or with a summary of conclusions (anti-Gelfand)? Does the closing crystallize the chapter's content into a forward-looking statement?

### E. PROSE QUALITY
Flag: hedging words, filler, AI slop ("notably", "crucially", "remarkably"), signpost transitions ("To state X, we need Y" / "Having established X, we now turn to Y"), redundant restatements, dashes where colons suffice.

### F. FORMULA VERIFICATION
Check every formula against CLAUDE.md anti-patterns AP1-AP50. Especially:
- AP1: κ values correct for each family
- AP7: Universal claims qualified
- AP14: Koszulness ≠ formality
- AP19: r-matrix poles one less than OPE
- AP24: κ+κ' = 0 only for KM/free; = 13 for Vir
- AP25: Three functors distinguished (bar ≠ Verdier ≠ cobar)
- AP27: Bar propagator weight 1, not weight h
- AP33: H_k^! ≠ H_{-k}

---

## PHASE 2: BUILD CONNECTIVE TISSUE (the creative work)

This is the Chriss-Ginzburg phase. For each finding from Phase 1:

### Narrative breaks → Mathematical transitions
At each thread break identified in 1A, write 1-3 sentences that:
- Close what came before (one sentence summarizing the mathematical content)
- Name the forcing question (what PROBLEM does the next section solve?)
- Open what comes next (the answer, or the first step toward it)

These must be MATHEMATICS, not signposts. Not "We now turn to X" but "The curvature κ·ω_g obstructs d²=0 at genus g≥1; restoring nilpotence requires a connection on the Hodge bundle."

### Motivation gaps → Question-driven openings
For each subsection that opens with a definition:
- Add 1-3 sentences BEFORE the definition explaining what QUESTION forces this construction
- The reader should feel "of course" when the definition arrives

### Define-before-use → First-principles definitions
For each undefined symbol:
- If it's a standard concept: add a parenthetical at first use. E.g., "(a D_X-module is a sheaf with a flat connection)" or "(the Hodge bundle E = π_*ω_π, whose fibre over [C] is H⁰(C, ω_C))"
- If it's a novel concept: add a full defining sentence before first use
- If it's used in a forward-looking paragraph (previewing what comes later): either remove the forward reference or qualify it ("a scalar κ(A), to be defined in §2")

### Opening → Concrete mathematics
If the chapter opens with a summary dump:
- DELETE the summary paragraph
- Start directly with the first mathematical construction
- Theorems should be stated ONCE, in their natural place (after the machinery to appreciate them), not previewed

### Prose → Mathematical content
- Delete every signpost sentence
- Replace every hedging word with a direct statement
- Merge every redundant restatement into a single clean version

Build after every 5 edits.

---

## PHASE 3: LINEAR BEILINSON SWEEP (sequential verification)

Read the file from line 1 to the end, 100 lines at a time. For each chunk:

1. **Verify every formula** against CLAUDE.md (AP1-AP50)
2. **Check for redundancies** introduced by Phase 2 (the #1 issue: two paragraphs at a subsection boundary saying the same thing in different words because the motivation and the original text overlap). MERGE into one.
3. **Check scope** of every universal claim (AP7)
4. **Check prose** quality line by line
5. **Fix** every issue with the Edit tool

The sweep is COMPLETE when you reach the end of the file.

---

## PHASE 4: DEEP STRUCTURAL ASSESSMENT

Re-read the chapter with completely fresh eyes. Ask:

1. Does the chapter open with a concrete mathematical object? (If it opens with "In this chapter we..." or a summary of results, the opening is wrong.)
2. Can a reader follow the first page knowing only: basic algebraic geometry, homological algebra, the definition of a vertex algebra?
3. Does each concept feel INEVITABLE?
4. Is every theorem stated exactly ONCE?
5. Does the chapter build to a CLIMAX — a single most important result — or is it a flat catalog?
6. Is there MOMENTUM? Does each page pull the reader to the next?
7. Would Gelfand, reading this at his seminar, say "yes, now I understand"?

Apply structural rewrites as needed. Do NOT cut mathematical content — restructure it.

---

## PHASE 5: CONVERGENCE CHECK

Re-read the entire file. Run:
- Formula verification (AP1-AP50)
- Redundancy scan
- Prose scan (no hedging, no signposts, no filler)
- Define-before-use check

If ZERO actionable findings at severity ≥ MODERATE: **CONVERGED.**
If ANY findings: return to Phase 3 and sweep again.

Build after convergence.

Report: total findings fixed, phases completed, final line count, build status.

---

## THE CONNECTIVE TISSUE STANDARD

The connective tissue is the difference between an encyclopedia and a monograph. Every transition between sections must answer THREE questions for the reader:

1. **Where are we?** (One sentence: what was just established)
2. **What forces the next step?** (One sentence: the mathematical question or obstruction)
3. **What is the answer?** (One sentence: the construction or theorem that resolves it)

Example (from the preface session):
- "Everything above takes place at genus 0. On a curve of genus g ≥ 1, the function z₁-z₂ has no global meaning: the curve is compact. The Arnold relation acquires a defect, and the defect is a scalar."

This is three sentences. The first locates the reader. The second names the obstruction. The third announces the resolution. Every section break needs exactly this.
