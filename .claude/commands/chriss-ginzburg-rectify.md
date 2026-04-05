---
description: "Full Chriss-Ginzburg fortification + Beilinson rectification on a chapter"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Chriss-Ginzburg Fortification + Beilinson Rectification

**Target file**: $ARGUMENTS

You are performing the complete editorial fortification and mathematical rectification of one chapter of the monograph *Modular Koszul Duality*. Read CLAUDE.md before beginning. The anti-patterns AP1-AP50 are the law. The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

## THE STANDARD

### The shared essence

What Gelfand, Beilinson, Drinfeld, Etingof, Kazhdan, Polyakov, Nekrasov, Kapranov, and Chriss-Ginzburg all share is this: **the mathematics speaks for itself, and every sentence serves the mathematics.** There is no layer between the reader and the object. No throat-clearing, no self-congratulation, no signposting where you are going or where you have been. The reader is treated as an equal who will see the force of the argument if it is stated with sufficient precision, and who will see through any attempt to paper over a gap with rhetoric.

The writing is not a *description* of mathematics. It IS mathematics. The prose carries the same logical force as the displayed equations. A transition sentence is not connective tissue gluing two results together — it is itself a mathematical observation: the reason the next construction is forced.

The common thread: **inevitability**. Every definition answers a question the reader already has. Every theorem resolves a tension that has been building. Every proof step follows from what came before with the feeling that no other step was possible. The reader finishes each page not thinking "that was clever" but thinking "of course — what else could it be?"

The second common thread: **courage**. The unifying principle is stated as a unifying principle, not hedged as an "analogy" or "motivation." If the bar complex curvature is the central charge, say so as an identification. If the partition function and the characteristic class are the same object, say "the same object," not "closely related." The mathematics earns the identification; the prose must not flinch from it.

The third common thread: **economy**. Not minimalism — economy. Every word carries weight. A paragraph that can be one sentence must be one sentence. A sentence that can be a clause must be a clause. But a construction that needs a full page of careful development gets a full page. Economy is not about brevity; it is about the absence of waste. Nothing is there for decoration, for emphasis, or for the author's comfort. Everything is there because the mathematics needs it.

### The individual peaks

Each of these mathematicians brings something unique. The standard for this monograph requires ALL of these simultaneously, not any one in isolation:

- **Gelfand** — the seminar question: "What IS this, concretely?" Before the abstract machine runs, show the object. Compute the first nontrivial example. The example is not an illustration of the theory; the theory is a generalization of the example. The reader should understand the example so well that the general definition feels like a formality.

- **Beilinson** — intellectual honesty as methodology. Every claim is false until independently verified. A smaller true theorem beats a larger false one. The willingness to retract, narrow, and qualify is not weakness; it is the engine of progress. The most important cognitive move is not creation but falsification. Apply this to your own writing: if a claim feels too good, it probably is.

- **Drinfeld** — the unifying principle stated with precision. Yangians, quantum groups, and geometric Langlands are not separate subjects; they are views of one object. When you see the same structure from multiple sides, SAY what the structure is and PROVE the identifications. The deepest mathematics is not in any one view but in the passage between views.

- **Etingof** — the clarity that makes the reader feel smarter, not the author. The best mathematical writing in the world. Every step justified not by citation but by understanding. Every example chosen to illuminate exactly the feature that the general theory will abstract. The reader finishes each section feeling that they could have invented the next one.

- **Kazhdan** — compression. Not compression to the point of obscurity, but compression to the point where every word is load-bearing. If you remove any sentence, the logical structure collapses. The text is a proof in the engineering sense: it carries exactly the load it needs to carry, with no excess material.

- **Polyakov** — physical intuition as mathematical content. The identification "the bar complex curvature IS the central charge" is not a metaphor or a motivation; it is a theorem. The physical insight does not live in an introductory paragraph to be forgotten; it lives in the proof, as an essential step. When physics and mathematics say the same thing, that coincidence IS the theorem.

- **Nekrasov** — the seamless passage. The partition function and the characteristic class appear in the same equation, related by an equals sign, and neither side apologizes for the other. A reader who knows physics gains mathematical insight from the right-hand side; a reader who knows mathematics gains physical insight from the left. Both are enriched by the identification, which is the actual content.

- **Kapranov** — the higher structure IS the mathematics. Operadic architecture is not formalism applied to a pre-existing subject; it is the skeleton that determines the shape of the subject. Homotopy coherence is not a technical condition to be verified; it is the flesh that gives the skeleton life. When you state a higher-categorical structure, you are not decorating the mathematics; you are revealing it.

- **Chriss-Ginzburg** — the architecture of the text mirrors the architecture of the mathematics. Nothing is used before it is defined. Everything is introduced at the exact moment it becomes necessary — not one page earlier (the reader is not ready) and not one page later (the reader is lost). The text has the structure of a symphony: each theme is introduced, developed, and resolved, and the themes interact to produce something greater than their sum.

### The synthesis

A page of this monograph should feel like sitting in Gelfand's seminar while Drinfeld explains the unifying principle, Beilinson challenges every claim, Etingof makes every step crystal clear, Kazhdan insists on compression, Polyakov provides the physical identification, Nekrasov writes both sides of the equals sign, Kapranov reveals the operadic skeleton, and Chriss-Ginzburg orchestrates the pacing.

No page achieves this by following one of these principles. Every page achieves this by following all of them simultaneously. The tension between them — Kazhdan's compression against Etingof's clarity, Beilinson's skepticism against Drinfeld's unifying vision, Gelfand's concreteness against Kapranov's abstraction — is not a contradiction. It is the engine. The resolution of each tension, on each page, is what produces mathematics at this level.

---

## THE PROGRAMME

The programme has four phases:

1. **GLOBAL DIAGNOSTIC** — read the chapter, map its current state
2. **STRUCTURAL RECTIFICATION** — get the platonic ideal skeleton right (sections, sequencing, scope, content delivery). Iterate until the structure converges.
3. **LINEAR BEILINSON RECTIFICATION LOOP** — chunk-by-chunk deep audit + fortification, advancing only when each chunk converges. This is where the real work happens.
4. **FINAL CONVERGENCE** — structural re-assessment, build, report.

The ordering is load-bearing: you do NOT sweep chunks until the skeleton is right. Rectifying prose in a section that will be moved, merged, or deleted is wasted work.

---

## PHASE 1: GLOBAL DIAGNOSTIC (read-only, fast)

Read the ENTIRE file in one pass. Do NOT edit yet. Produce a brief diagnostic under six headings:

**1A. Narrative thread.** Map the logical arc: what does each section establish, and what forces the next? Note where the thread breaks.

**1B. Motivation gaps.** Which subsections open cold with a definition instead of a question?

**1C. Define-before-use violations.** Symbols used before defined.

**1D. Opening and closing.** Concrete math or summary dump? Does the closing crystallize?

**1E. Prose.** Flag hedging, signposts, AI slop ("notably", "crucially", "remarkably", "it is worth noting", "Having established X, we now turn to"), dashes where colons suffice, redundant restatements.

**1F. Formula red flags.** Quick scan for obvious AP1-AP34 violations. Don't recompute yet — that's Phase 3.

This diagnostic is your MAP for Phase 2. Keep it short — a numbered list, not an essay.

---

## PHASE 2: STRUCTURAL RECTIFICATION (the skeleton)

Before touching individual lines, get the GROSS STRUCTURE right. This phase asks: what is the platonic ideal of this chapter? What sections does it need, in what order, delivering what content, at what scope?

### 2A. The Platonic Ideal

Using the Phase 1 diagnostic AND the compute infrastructure, design the ideal structure.

**Compute as guide.** Before designing the structure, survey the compute layer for this chapter's mathematical content. Run:
```bash
# Find all compute modules relevant to this chapter's topics
grep -rl "RELEVANT_KEYWORDS" ~/chiral-bar-cobar/compute/lib/ ~/chiral-bar-cobar/compute/tests/
# Also check Vol II and Vol III compute layers if they exist
grep -rl "RELEVANT_KEYWORDS" ~/chiral-bar-cobar-vol2/compute/ ~/calabi-yau-quantum-groups/compute/ 2>/dev/null
```
The compute modules tell you what has been INDEPENDENTLY VERIFIED. A theorem with 50 passing tests is load-bearing; a theorem with zero tests is suspect. The structural design should:
- Lead with content that has strong compute backing (this is the proved core)
- Flag content that has no compute verification (these need tests or qualification)
- Use compute test names as a guide to what the chapter's "greatest hits" are — the formulas readers will actually use
- Identify compute modules that SHOULD exist but don't (gaps in verification)

1. **What is this chapter's single organizing question?** Every chapter in the monograph answers one question. Name it. If the chapter currently answers three questions, it either needs to be split or needs a unifying thread that makes the three into aspects of one.

2. **What is the climax?** The single most important theorem or construction. Everything before it builds toward it; everything after it flows from it. If the chapter has no climax, it is a catalogue, not a chapter.

3. **What is the ideal section sequence?** List each section by its mathematical content (not its current title). For each section:
   - What question does it answer?
   - What does it need from the previous section?
   - What does it provide to the next section?
   - Is it in the right place? Should it come earlier (because something downstream needs it) or later (because the reader isn't ready)?

4. **What should be cut?** Sections that don't serve the organizing question. Redundant material. Content that belongs in a different chapter. Content that is repeated from an earlier chapter without adding anything.

5. **What is missing?** Constructions that are referenced but never given. Motivating examples that should precede abstract machinery. Transitions that would make the next section inevitable.

6. **What is the scope envelope?** For each major claim in the chapter, what is the HONEST scope? Flag any claim whose scope will need to be adjusted (AP7, AP32).

### 2B. Structural Edits

Execute the structural changes:

- **Reorder** sections to match the ideal sequence
- **Merge** sections that cover the same ground
- **Split** sections that do two things
- **Move** material that belongs in a different chapter (leave a `% MOVED TO [target]` comment; do not delete mathematical content)
- **Delete** genuine redundancies (material restated verbatim or near-verbatim from within the same chapter)
- **Add section stubs** for missing material (mark with `% STRUCTURAL-STUB: [description]`)
- **Rewrite the opening** if it is a summary dump: start with the first mathematical object, not with "In this chapter we establish..."
- **Rewrite the closing** if it doesn't crystallize: the last paragraph should make the reader feel the chapter's question has been answered, and hint at what the answer forces next

Build after structural edits. The build command depends on which volume the target file belongs to:
- Vol I (`~/chiral-bar-cobar`): `pkill -9 -f pdflatex 2>/dev/null; sleep 2; cd ~/chiral-bar-cobar && make fast`
- Vol II (`~/chiral-bar-cobar-vol2`): `pkill -9 -f pdflatex 2>/dev/null; sleep 2; cd ~/chiral-bar-cobar-vol2 && make`
- Vol III (`~/calabi-yau-quantum-groups`): `pkill -9 -f pdflatex 2>/dev/null; sleep 2; cd ~/calabi-yau-quantum-groups && pdflatex main.tex`

### 2C. Structural Convergence

Re-read the chapter after structural edits. Ask:

1. Does the sequence feel inevitable? Could any section be moved without breaking the logic?
2. Does every section serve the organizing question?
3. Is the climax in the right place?
4. Are there still redundancies?
5. Would Chriss-Ginzburg approve of the architecture?

If ANY structural issue remains at severity >= SERIOUS: loop back to 2B. The structure must converge before the linear sweep begins.

**Typical iteration count**: 2-3 rounds. If > 4, the chapter may need to be split.

---

## PHASE 3: LINEAR BEILINSON RECTIFICATION LOOP

This is the core of the programme. You step through the chapter sequentially in chunks of ~50-100 lines. For each chunk, you run a FULL Beilinson rectification loop. You do not advance to the next chunk until the current chunk converges.

### The Chunk Loop

```
Set cursor = line 1

WHILE cursor < end of file:
    chunk = lines [cursor, cursor + 100]
    
    REPEAT:
        === AUDIT (adversarial, falsification-first) ===
        
        Read the chunk in context of everything already processed.
        For every mathematical claim in the chunk:
        
        (a) FORMULA VERIFICATION. Recompute from first principles.
            Do NOT pattern-match against other occurrences (AP3).
            Key checks:
            - κ values: H_k→k, KM→(k+h∨)dim g/2h∨, Vir→c/2 (AP1)
            - Complementarity: κ+κ'=0 for KM/free; =13 for Vir (AP24)
            - Three functors: B(A) coalgebra, D_Ran(B(A))≃B(A!), Ω(B(A))≃A (AP25)
            - Propagator weight 1, not h (AP27)
            - H_k^! = Sym^ch(V*) ≠ H_{-k} (AP33)
            - r-matrix poles one less than OPE (AP19)
            - Scope: "for all" means ALL (AP7)
            - Self-dual Virasoro: specify c=13 (AP8)
            - Koszulness ≠ Swiss-cheese formality (AP14)
            - Genre-1 ≠ all-genera (AP32)
            - Bar-cobar inversion ≠ open-to-closed (AP34)
            Cross-check against compute/tests/ and compute/lib/ where applicable.
        
        (b) PROOF LOGIC. Check every proof step. Are hypotheses of cited
            results satisfied? Circular dependencies? (AP4, AP13)
        
        (c) SIGN/SHIFT CONVENTIONS. Verify against signs_and_shifts.tex.
        
        (d) CROSS-REFERENCES. Every \ref resolves? Cited result matches usage?
        
        (e) STATUS TAGS. Does \ClaimStatusProvedHere match what the proof
            actually proves? (AP4, AP12)
        
        (f) SCOPE. Every universal claim checked against edge cases.
            Critical level, admissible level, self-dual point. (AP7, AP18)
        
        (g) PROPAGATION. After ANY error found, grep ALL THREE volumes: ~/chiral-bar-cobar,
            ~/chiral-bar-cobar-vol2, AND ~/calabi-yau-quantum-groups
            for all variant forms. (AP5)
        
        === FORTIFY (the Chriss-Ginzburg creative work) ===
        
        (h) CONNECTIVE TISSUE. At every section/subsection boundary in
            this chunk, ensure three sentences:
            1. Where are we? (what was just established)
            2. What forces the next step? (the obstruction or question)
            3. What is the answer? (the construction that resolves it)
            These must be MATHEMATICS, not signposts.
        
        (i) MOTIVATION. Every definition preceded by the question it answers.
            The reader should feel "of course" before the definition arrives.
        
        (j) DEFINE-BEFORE-USE. Every symbol defined at or before first use.
            For standard concepts, add parenthetical first-principles definitions.
        
        (k) PROSE. Delete signposts. Replace hedges with direct statements.
            Merge redundancies. No "notably/crucially/remarkably."
            No dashes where colons or periods suffice.
            Standard: Kac, Etingof, Bezrukavnikov, Gelfand.
        
        (l) OPENING. If this is the first chunk and it opens with a summary
            dump (conclusions before constructions): delete it. Start with
            the first mathematical object.
        
        === FIX ===
        
        Apply all fixes to the chunk using the Edit tool.
        After every 3 fixes, build the volume containing the target file:
            pkill -9 -f pdflatex 2>/dev/null; sleep 2
            # Use the appropriate build command for the target volume
            # Vol I: cd ~/chiral-bar-cobar && make fast
            # Vol II: cd ~/chiral-bar-cobar-vol2 && make
            # Vol III: cd ~/calabi-yau-quantum-groups && pdflatex main.tex
        After every fix to a formula, grep all three volumes for variants (AP5).
        
        === RE-AUDIT ===
        
        Re-read the chunk after fixes. Check:
        - Every fix is correct (the double-edged Beilinson: wrong
          corrections are worse than no correction)
        - No new errors introduced by the rewrite
        - No redundancies created (the #1 Phase 2 failure mode:
          motivation text that duplicates existing content)
        - Prose meets the standard
        
        === CONVERGENCE TEST ===
        
        If zero actionable findings at severity >= MODERATE: CONVERGED.
        Advance cursor to next chunk.
        
        If any findings: LOOP BACK to AUDIT on this same chunk.
    
    END REPEAT
    
    cursor += (chunk size, adjusted for edits)

END WHILE
```

### Critical Rules for the Chunk Loop

1. **Progressive model.** As you process chunks, you build an accumulating model of the chapter. Each chunk's audit is informed by everything already processed. If chunk 5 reveals that a symbol was defined differently in chunk 2, go back and fix chunk 2 (but only the specific issue — don't re-audit the whole thing).

2. **Never skip forward.** If a chunk won't converge after 3 iterations, flag the specific issue with `% RECTIFICATION-FLAG: [reason]` and proceed — but document why in your report. A flagged issue is better than an infinite loop.

3. **Build discipline.** After every 3 edits, build. If a fix breaks the build, revert immediately. Never accumulate > 3 unfixed findings.

4. **Grep discipline.** After EVERY formula change, grep all three volumes (`~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`) for all variant forms (AP5). Fix all instances.

5. **The double-edged Beilinson.** Every correction must be independently verified. If you cannot verify a correction, mark it `% RECTIFICATION-FLAG: [reason]` rather than silently applying. A wrong correction is worse than no correction.

6. **Compute verification.** For any numerical formula (κ values, F_g, Q^contact, discriminants, growth rates), verify against compute/tests/ and compute/lib/. Run targeted tests if needed.

---

## PHASE 4: STRUCTURAL RE-ASSESSMENT (post-loop)

After the linear loop completes (all chunks converged), re-read the ENTIRE file with fresh eyes. The linear sweep may have revealed structural issues invisible at the Phase 2 level:

1. Does it open with a concrete mathematical object?
2. Can a working algebraic geometer follow the first page?
3. Does each concept feel INEVITABLE?
4. Is every theorem stated exactly ONCE?
5. Does the chapter build to its CLIMAX?
6. Is there MOMENTUM? Does each page pull the reader to the next?
7. Would Gelfand say "yes, now I understand"?

If structural rewrites are needed, apply them, then re-run the Phase 3 Beilinson loop on the affected chunks only (not the entire chapter).

---

## PHASE 5: FINAL CONVERGENCE

Build all three volumes:
```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 3
cd ~/chiral-bar-cobar && make fast
cd ~/chiral-bar-cobar-vol2 && make
cd ~/calabi-yau-quantum-groups && pdflatex main.tex
```

Re-read the entire file one last time. If zero findings: **CONVERGED.**

Report:
- Phase 2 structural iterations (how many rounds to converge the skeleton)
- Total chunks processed in Phase 3
- Total chunk-loop iterations (sum across all chunks)
- Total findings fixed, by severity (CRITICAL/SERIOUS/MODERATE/MINOR)
- Total findings fixed, by class (A-logical, B-formula, C-structural, D-status, E-editorial)
- Chunks that required > 1 iteration (and why)
- Any RECTIFICATION-FLAGs left open
- Final line count
- Build status (both volumes)

---

## THE CONNECTIVE TISSUE STANDARD

The connective tissue is the difference between an encyclopedia and a monograph. It is the creative work.

**At every section boundary**, three sentences:
1. **Where are we?** (One sentence: what was just established)
2. **What forces the next step?** (One sentence: the mathematical question or obstruction)
3. **What is the answer?** (One sentence: the construction or theorem that resolves it)

**At every subsection boundary**, one sentence:
- The question this subsection answers, stated as mathematics.

**At every definition**, the reader should already feel: *of course*.

**At every theorem**, the reader should feel: *inevitable*.

Example:
> "Everything above takes place at genus 0. On a curve of genus g ≥ 1, the function z₁ − z₂ has no global meaning: the curve is compact. The Arnold relation acquires a defect, and the defect is a scalar."

Three sentences. The first locates. The second names the obstruction. The third announces the resolution.
