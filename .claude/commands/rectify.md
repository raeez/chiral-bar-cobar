---
description: "Beilinson rectification loop on a chapter — converges to platonic ideal"
model: opus
---

RECTIFICATION_SESSION_ACTIVE

# Beilinson Rectification Loop

**Target**: $ARGUMENTS

Read CLAUDE.md before beginning. The anti-patterns AP1-AP50 are the law. The standard: Kac, Gelfand, Etingof, Beilinson, Drinfeld, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Ginzburg, Chriss-Ginzburg.

## THE STANDARD

The mathematics speaks for itself, and every sentence serves the mathematics. There is no layer between the reader and the object. The writing is not a *description* of mathematics — it IS mathematics.

- **Gelfand**: "What IS this, concretely?" Show the object. The example is not an illustration of the theory; the theory is a generalization of the example.
- **Beilinson**: Falsification as methodology. Every claim false until independently verified. A smaller true theorem beats a larger false one.
- **Drinfeld**: The unifying principle stated with precision. When you see the same structure from multiple sides, SAY what the structure is and PROVE the identifications.
- **Etingof**: Clarity that makes the reader feel smarter, not the author. Every step justified by understanding.
- **Kazhdan**: Compression. If you remove any sentence, the logical structure collapses.
- **Polyakov**: Physical intuition as mathematical content. The identification IS the theorem, not a metaphor.
- **Nekrasov**: The seamless passage. Partition function and characteristic class in the same equation.
- **Kapranov**: The higher structure IS the mathematics. Operadic architecture is not formalism — it is the skeleton.

Three threads: **inevitability** (every definition answers a question the reader already has), **courage** (identifications stated as identifications, not hedged as analogies), **economy** (nothing for decoration, nothing for comfort).

## THE PROGRAMME (4 phases, iterated to convergence)

### PHASE 1: GLOBAL DIAGNOSTIC (read-only)

Read the ENTIRE file. Do NOT edit. Produce a brief diagnostic:

**1A. Narrative thread** — where does the logical arc break?
**1B. Motivation gaps** — which subsections open cold?
**1C. Define-before-use violations**
**1D. Opening/closing quality** — concrete math or summary dump?
**1E. Prose** — hedging, signposts, AI slop, dashes
**1F. Formula red flags** — quick AP scan

### PHASE 2: STRUCTURAL RECTIFICATION (the skeleton)

Before touching lines, get the gross structure right:

1. **What is this chapter's single organizing question?**
2. **What is the climax?** The single most important theorem.
3. **What is the ideal section sequence?**
4. **What should be cut?** (Material not serving the question)
5. **What is missing?**
6. **What is the scope envelope?** (AP7, AP32 check per claim)

Survey the compute layer for relevant verified content:
```bash
grep -rl "RELEVANT_KEYWORDS" ~/chiral-bar-cobar/compute/lib/ ~/chiral-bar-cobar/compute/tests/ 2>/dev/null
```

Execute structural changes. Build after. Iterate until skeleton converges (max 3 rounds).

### PHASE 3: LINEAR BEILINSON SWEEP (the core)

Step through the file in ~100-line chunks. For each chunk, run a full convergence loop:

```
WHILE cursor < end of file:
    chunk = [cursor, cursor+100]
    
    REPEAT:
        === AUDIT (adversarial, Beilinson-first) ===
        (a) FORMULA VERIFICATION — recompute from first principles (AP1,AP3)
            Key: kappa values, complementarity (AP24), three functors (AP25),
            propagator weight 1 (AP27), H_k^! != H_{-k} (AP33), r-matrix 
            poles (AP19), scope (AP7), self-dual Vir c=13 (AP8),
            Koszulness != formality (AP14), genus-1 != all-genera (AP32)
        (b) PROOF LOGIC — hypotheses match? circular deps? (AP4,AP13)
        (c) SIGN/SHIFT — verify against signs_and_shifts.tex
        (d) CROSS-REFERENCES — every \ref resolves?
        (e) STATUS TAGS — ProvedHere matches actual proof? (AP4,AP12)
        (f) SCOPE — universal claims vs edge cases (AP7,AP18)
        (g) PROPAGATION — after ANY fix, grep ALL THREE volumes (AP5)
        
        === FORTIFY (Chriss-Ginzburg creative work) ===
        (h) CONNECTIVE TISSUE — 3 sentences at section boundaries:
            1. Where are we? 2. What forces the next step? 3. What is the answer?
        (i) MOTIVATION — every definition preceded by the question it answers
        (j) DEFINE-BEFORE-USE — every symbol defined at first use
        (k) PROSE — delete signposts, replace hedges, merge redundancies
            No: notably, crucially, remarkably, "having established X"
            Standard: Kac, Etingof, Bezrukavnikov, Gelfand
        
        === FIX ===
        Apply with Edit tool. Build every 3 fixes. Grep both volumes after formula fixes.
        
        === CONVERGENCE TEST ===
        Zero findings at severity >= MODERATE → advance cursor
        Any findings → LOOP BACK on this chunk
    END REPEAT
END WHILE
```

**Critical rules:**
- After every 3 edits, build: `pkill -9 -f pdflatex; sleep 2; make fast`
- After every formula change, grep ALL THREE volumes (AP5)
- If a chunk won't converge after 3 iterations, flag with `% RECTIFICATION-FLAG`
- A wrong correction is worse than no correction (the double-edged Beilinson)

### PHASE 4: FINAL CONVERGENCE

Re-read the entire file with fresh eyes. Check:
1. Concrete mathematical object as opening?
2. Each concept feels INEVITABLE?
3. Every theorem stated exactly ONCE?
4. Chapter builds to its CLIMAX?
5. MOMENTUM — each page pulls to the next?
6. Would Gelfand say "yes, now I understand"?

Build all volumes:
```bash
pkill -9 -f pdflatex; sleep 3; make fast
cd ~/chiral-bar-cobar-vol2 && make
```

Run tests: `make test`

If ZERO findings: **CONVERGED.**
If ANY findings: return to Phase 3 on affected chunks.

## Report

- Structural iterations
- Total chunks processed
- Total chunk-loop iterations
- Findings by severity and class
- RECTIFICATION-FLAGs remaining
- Final line count
- Build status
