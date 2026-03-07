# SESSION PROMPT v16 — HUMAN-READABLE VERSION

## What This Session Does

The v15 campaign fixed the proof architecture — circularity, false citations, missing lemmas, contradictions. That was surgery. This session is chemotherapy: it propagates the consequences of all eight raeeznotes files into every corner of the manuscript.

## What's Already Done (Don't Redo)

1. Definition-theorem circularity killed
2. Bar concentration theorem added
3. "For any algebra" contradiction fixed
4. Fiber-cohomology lemma strengthened
5. Hochschild duality unified
6. Theorem D properly split
7. Conjecture stratification added
8. Three differential macros deployed (\dfib, \Dg{g}, \dzero)
9. KL target category fixed (C(U_q(g)))
10. Parameter source fixed (H^1(Sigma_g))

## The Ten Workstreams

### 1. Homotopy-Native Remarks (4 files, ~120 lines)
Add short Remarks after main theorems giving the derived/infinity-categorical formulation. The current statements are cohomological shadows — say so explicitly. Don't rewrite theorems, just add perspective.

### 2. Periodicity Profile (4-8 files, ~40 lines)
Replace any scalar "Period(A)" with the triple Pi(A) = (M_A, Q_A, G_A). The periodicity of a chiral algebra is not a number — it's a module with an exterior algebra and a Galois group.

### 3. Prose Sculpting (all files, net -500 to -1000 lines)
Kill announcements ("We will now prove..."), dead transitions ("Having established X..."), passive hedging ("It might be noted..."), preamble bloat, redundant re-derivations. The Chriss-Ginzburg standard: computation first, explanation after, no filler.

### 4. Parameter-Source Diagram (1 file, ~15 lines)
One diagram showing how parameters flow from curves to moduli. Goes in higher_genus.tex near the convention block.

### 5. Coderived Appendix (1 file, ~100 lines)
The manuscript references coderived categories in several places but never defines them self-containedly. Add a short appendix with the Positselski definitions.

### 6. Physics Programme Branding (3 files, ~30 lines)
Chapters 29-31 are programme material, not proved results. Add a brief remark at the start of each making this explicit and pointing to the conjecture stratification.

### 7. Master Table Stratification (1 file, ~30 lines)
The Master Table of Computed Invariants needs proof-status tiers: fully proved / conditional on Koszulness / conjectural.

### 8. Regime Tags (15 files, ~30 edits)
Add parenthetical regime indicators to theorem names where not already clear: "genus-0", "Koszul locus", "all genera", "completed/coderived".

### 9. Cross-Reference Verification (scanning pass)
After v15's label changes, verify all \ref{thm:...} targets still exist.

### 10. Differential Notation Completion (scanning pass)
Verify no bare d_g or d^2=kappa remains outside the 11 files already converted.

## What This Does NOT Do

- Does not change any proofs
- Does not rewrite theorem statements
- Does not add new theorems or conjectures
- Does not touch the preamble or document class
- Does not delete proved content
- Does not add packages

## Expected Outcome

The manuscript will be internally consistent with its own proof architecture, every theorem will carry its homotopy-native context, the prose will be 5-10% leaner, and the physics chapters will be honestly branded. The book becomes referee-ready at the architectural level.
