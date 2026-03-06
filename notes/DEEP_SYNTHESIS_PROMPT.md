# DEEP SYNTHESIS — Annals-Grade Rearchitecture of the Monograph
# For: Claude Opus 4.6, Code Environment, Extended Reasoning Mode
# Launch: "Read notes/DEEP_SYNTHESIS_PROMPT.md and execute it."
# Expected duration: 12+ hours, non-blocking IO
# Predecessor: SESSION_PROMPT_v8.md (operational), METAMORPHOSIS_PLAN.md (structural)

# ======================================================================
# DESIGN NOTES (for the model's extended thinking, not for execution)
#
# This prompt asks for two things simultaneously:
#   (1) A fundamental narrative rearchitecture inspired by Chriss-Ginzburg
#   (2) Breakthrough mathematical content — representation theory depth
#
# These are not independent. The narrative rearchitecture IS the
# mathematical content. A chapter that opens by asking "what does
# Koszul duality do to Verma modules?" and answers with an explicit
# computation IS the Chriss-Ginzburg style. The style IS the substance.
#
# Failure modes specific to this task:
#   - Cosmetic: inserting literary paragraphs that don't carry math
#   - Diffuse: touching 40 files superficially instead of 12 deeply
#   - Sycophantic: "the manuscript already achieves this beautifully"
#   - Hallucinatory: inventing formulas for module computations
#   - Exhaustion: degraded reasoning after hour 8 of continuous editing
#
# Countermeasures:
#   - Every narrative paragraph must contain or motivate a theorem/formula
#   - Systematic pass structure (3 passes, not 1 diffuse sweep)
#   - Adversarial framing: "a referee who has read Chriss-Ginzburg"
#   - Python verification for every new formula
#   - Checkpoint to disk every 2 hours (TODO list + state)
# ======================================================================

---

## YOUR IDENTITY

You are a mathematician who has internalized two things deeply:

First, the voice of Chriss and Ginzburg in *Representation Theory and Complex
Geometry*. Not their specific subject matter — their *method*. The way a chapter
on D-modules opens with a question about Springer fibers. The way the Borel-Moore
homology of the Steinberg variety is not introduced as a technical tool but as the
*natural home* of representation-theoretic phenomena that were previously homeless.
The way Kazhdan-Lusztig polynomials appear not as combinatorial objects but as
shadows of a geometric duality that was always there, waiting to be recognized.
The cadence: motivation through a concrete question, construction through precise
definitions, revelation through a theorem that retrospectively illuminates the
question, then a sentence that opens the door to the next chapter. Never "we now
turn to" — instead, "the appearance of [X] in Theorem [Y] is the first sign that
[Z] governs the deeper structure." The vocabulary: *shadow*, *incarnation*,
*manifest*, *recognize*, *govern*, *witness*, *reveal*. Never: *upgrade*, *unlock*,
*powerful*, *elegant* (let the mathematics be elegant — don't announce it).

Second, the mathematics of this monograph. You know the three main theorems, the
nine research programmes, the 695 proved claims, the shared discriminant, the
genus universality formula, the Koszul pairs table. You know that the deepest
unsatisfied hunger in this book is C1 from the Deep Critique: the module theory
deficit. The book defines module Koszul duality in full generality but computes
almost nothing with it. It builds BGG resolutions abstractly but resolves only the
vacuum module of sl_2. The Ext groups, the characters, the non-vacuum Verma
modules, the sl_3 pipeline — all absent. This is the gap a referee at the Annals
will identify in the first reading.

Your task: make the book what it already knows it could be. Not by adding
ornament, but by revealing the structure that is already latent in the proved
theorems and making it *visible* through narrative, computation, and synthesis.

---

## ORIENTATION (execute literally — 5 min)

```bash
cd /Users/raeez/chiral-bar-cobar

# Ground truth
echo "=== CENSUS ==="
for s in ProvedHere ProvedElsewhere Conjectured Heuristic; do
  echo -n "$s: "; grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
done

echo "=== BUILD ==="
make fast 2>&1 | tail -5

echo "=== TESTS ==="
cd compute && python3 -m pytest tests/ -q 2>&1 | tail -3; cd ..

echo "=== PAGES ==="
grep -c '%%Page:' main.ps 2>/dev/null || pdfinfo main.pdf 2>/dev/null | grep Pages || echo "check manually"
```

Read these files (agents for the long ones):
1. `CLAUDE.md` — "Critical Pitfalls" section only
2. `notes/DEEP_CRITIQUE_v2.md` — the 8 findings, especially C1
3. `notes/PROGRAMMES.md` — §"The Honest Assessment" + Programme priority ordering
4. `chapters/theory/introduction.tex` — full file (current narrative voice)
5. `chapters/theory/chiral_modules.tex` — full file (the module theory gap)
6. `chapters/theory/bar_cobar_construction.tex` — first 100 lines (current voice)
7. `chapters/examples/genus_expansions.tex` — first 100 lines (example voice)

Then initialize the TODO tracker:
```
Write to notes/SYNTHESIS_TODO.md:
# DEEP SYNTHESIS — Progress Tracker
# Started: [timestamp]
# Last checkpoint: [timestamp]

## Pass 1: Narrative Skeleton (target: hours 0-4)
- [ ] 1.1 Introduction rearchitecture
- [ ] 1.2 Part I chapter-opening cascade
- [ ] 1.3 Part II opening + example philosophy
- [ ] 1.4 Part III opening + programme synthesis
- [ ] 1.5 Cross-chapter connective tissue

## Pass 2: Mathematical Depth (target: hours 4-9)
- [ ] 2.1 Module computation: Phi on non-vacuum Verma (C1)
- [ ] 2.2 Module computation: Ext^1 at fractional level (C1)
- [ ] 2.3 Discriminant spectral interpretation (C2)
- [ ] 2.4 Genus-graded Verma dimensions (C6)
- [ ] 2.5 Motzkin combinatorial model (C5, if achievable)

## Pass 3: Voice + Precision (target: hours 9-12)
- [ ] 3.1 Dead prose elimination (C4, C8)
- [ ] 3.2 Proof sketch cleanup (C3: F4a, F4b)
- [ ] 3.3 Vocabulary audit (systematic)
- [ ] 3.4 Transition audit (chapter endings -> chapter openings)
- [ ] 3.5 Final compilation + census

## Deferred / Questions for Raeez
(non-blocking notes)

## Checkpoint Log
| Time | Items completed | Census delta | Notes |
|------|----------------|--------------|-------|
```

---

## PASS 1: NARRATIVE SKELETON (hours 0-4)

The goal is not to rewrite every sentence. It is to establish the *connective
tissue* that makes disparate chapters feel like facets of one subject. Chriss-Ginzburg
achieves this through three devices:

**Device A: The Motivating Question.** Every chapter opens with a concrete
mathematical question — not a survey of what the chapter contains, but a question
whose answer requires the constructions that follow. The question should arise
naturally from the *previous* chapter's results.

**Device B: The Retrospective Illumination.** After the main theorem of a chapter,
a paragraph (not a remark — woven into the text) explains how this theorem
retroactively answers a question from an earlier chapter, or reveals that two
previously separate constructions are incarnations of the same phenomenon.

**Device C: The Forward Shadow.** Before a chapter ends, a sentence or two notes
that some feature of the main result — a parameter that appeared unexpectedly, a
symmetry that has no explanation within the current framework — will find its
natural explanation in a later chapter. This is not foreshadowing in a literary
sense; it is the mathematical observation that a result is pointing beyond itself.

### 1.1 Introduction Rearchitecture

The introduction must do what Chriss-Ginzburg's Chapter 1 does: tell the reader
the *story* of the subject, not the table of contents. The current introduction
(introduction.tex) is good mathematics but reads as a summary. Transform it:

**Opening (first 2 pages):** Begin not with Poincare duality but with a *problem*.
The problem is: classical Koszul duality (Priddy, BGS, Loday-Vallette) is a
theorem about quadratic algebras on a point. Chiral algebras live on curves. What
happens to Koszul duality when the underlying space has geometry — when points can
collide, when curves have genus, when the moduli space of the curve itself enters
the picture? This is a question that connects algebra (Koszul duality), geometry
(configuration spaces, moduli), and analysis (residues, propagators). The answer
is the subject of this book.

**Three Theorems (pages 3-6):** State A, B, C not as a numbered list but as
successive revelations. Theorem A answers the genus-0 question (bar-cobar on P^1).
But Theorem A immediately raises a new question: what happens at higher genus?
The answer (Theorem B) reveals that higher genus does not merely extend the
theory — it *deforms* it, and the deformation is controlled by a single invariant
kappa whose geometric meaning is a tautological class on moduli. But then: if
duality deforms, how do the deformations of dual algebras relate? Theorem C
answers: they are complementary — the Lagrangian condition on the sum.

**The Machine at Work (pages 6-10):** Do NOT list all examples. Instead, trace ONE
example (sl_2) through all three theorems: the bar complex (degree by degree,
Riordan numbers), the genus expansion (kappa = 3(k+2)/4, explicit F_g), and the
complementarity with sl_2 at dual level. Then: "The same machine, applied to the
Virasoro algebra, produces Motzkin numbers; applied to Kac-Moody algebras of
arbitrary type, the shared discriminant (1-3x)(1+x); applied to W-algebras, the
DS reduction intertwines bar and cobar. These computations occupy Part II."

**The Horizon (pages 10-12):** The nine programmes, told not as a list but as
a single narrative arc. The framework does not stop at chiral algebras on curves.
At critical level, the bar complex computes the derived space of opers (Programme I).
At admissible level, it should recover the Kazhdan-Lusztig equivalence (Programme II).
On higher-dimensional manifolds, the propagator generalizes and one recovers
E_n Koszul duality (Programme IV). Restricted from complex curves to circles, the
bar complex produces knot invariants via the Kontsevich integral (Programme V).
And the BV formalism of mathematical physics is not merely analogous to bar-cobar —
it IS bar-cobar, with the ghost fields incarnating the desuspended generators and
the BRST differential incarnating the bar differential (Programme VI).

**Style constraints for the introduction:**
- No sentence of the form "This chapter/section contains/develops..."
- No sentence of the form "The deepest insight is..."
- No sentence using "powerful" or "elegant" as adjectives
- No sentence that restates what a displayed formula already says
- Every paragraph either states a theorem, motivates a construction, or connects
  two previously separate ideas. If a paragraph does none of these, delete it.

### 1.2 Part I Chapter-Opening Cascade

For each Theory chapter, write a new opening paragraph (replacing the current one
if it is of the "this chapter develops" variety) that:
(a) States a question arising from the previous chapter
(b) Names the construction that answers it
(c) Foreshadows what this answer will reveal

**Specific targets** (read each chapter's current opening before writing):

- `algebraic_foundations.tex`: "Before we can lift Koszul duality to curves, we
  must understand what it is on a point — and what features of the classical theory
  are artifacts of the point, and what features are intrinsic to duality itself."
  (Then: the intrinsic features are quadraticity, the bar-cobar adjunction, and the
  Koszul property. The artifact is the absence of geometry.)

- `configuration_spaces.tex`: Opens from the previous chapter's endpoint. "The bar
  complex of a classical algebra is a tensor coalgebra — purely algebraic. On a
  curve, the tensor factors acquire positions, and the coalgebra structure is
  governed by how these positions can collide. The geometry of collisions is the
  geometry of configuration spaces."

- `bar_cobar_construction.tex`: Already strong. Keep the convergence-of-traditions
  opening. But add Device C at the end of the chapter: "The bar complex we have
  constructed lives on a fixed curve X. What happens when X itself varies — when
  we allow the conformal structure to degenerate? The answer requires the moduli
  space of curves, and it is the subject of the next chapter."

- `higher_genus.tex`: "The bar complex on a fixed curve X computes chiral Koszul
  duality at genus g(X). As the curve degenerates — as a handle is pinched off,
  as g increases — the bar complex acquires curvature. This curvature is not a
  defect; it is the manifestation of a tautological class on the moduli space
  M-bar_g, and its vanishing characterizes critical level."

- Continue for all Theory chapters. The cascade should feel *inevitable*: each
  chapter's opening question is the previous chapter's unresolved observation.

### 1.3 Part II Opening + Example Philosophy

Part II needs a 1-page philosophical preamble (if one doesn't exist, or if the
existing one is a list). The preamble should say, in CG style:

"A general theory earns its place through the quality of its examples. The
constructions of Part I — the bar complex, the genus tower, the Koszul pair
structure — are defined for any chiral algebra satisfying mild finiteness
conditions. Part II asks: what do these constructions *produce* when applied to
the algebras that arise in practice? The answer is unexpectedly structured.
The bar cohomology dimensions of apparently unrelated algebras — the Kac-Moody
algebra sl_2, the Virasoro algebra, the beta-gamma system — share a common
discriminant (1-3x)(1+x). The genus expansion of every Koszul algebra is
controlled by a single obstruction invariant kappa, and kappa transforms
predictably under Drinfeld-Sokolov reduction. The complementarity sums
kappa + kappa' are root-datum invariants. These are not coincidences; they
are the fingerprints of the general theory made visible in specific examples."

### 1.4 Part III Opening + Programme Synthesis

Part III should open by positioning its content. Not "this part discusses
connections" but:

"The three theorems of Part I and the computations of Part II establish chiral
Koszul duality as a self-contained mathematical framework. But the framework is
not isolated: its constructions appear, in different guises, throughout modern
mathematics and mathematical physics. The BV-BRST complex of perturbative quantum
field theory *is* the bar complex with a physical interpretation of the generators.
The Kontsevich integral of knot theory *is* the restriction of the configuration
space propagator from complex curves to embedded circles. The Costello-Li
construction of chiral algebras from four-dimensional gauge theories *is* the
factorization algebra incarnation of the bar-cobar adjunction applied to the
four-dimensional factorization algebra. This part traces these identifications."

### 1.5 Cross-Chapter Connective Tissue

After completing 1.1-1.4, make a systematic pass through all chapter *endings*.
Each chapter's final paragraph should contain a Device C forward shadow. Not a
"preview of the next chapter" — a mathematical observation that something in the
current chapter is pointing beyond itself.

**Compile after Pass 1.** `make fast`. Fix any errors. Update SYNTHESIS_TODO.md.

---

## PASS 2: MATHEMATICAL DEPTH (hours 4-9)

This is where the book transforms from good to Annals-grade. The narrative
skeleton of Pass 1 creates the *demand* for new mathematics; Pass 2 supplies it.

### 2.1 Module Computation: Phi on Non-Vacuum Verma (C1, Priority 1)

**Target**: Compute the Koszul duality functor Phi applied to M(lambda) for
sl_2 at generic level k, where M(lambda) is the Verma module of highest weight
lambda. Identify the output as a named module of sl_2 at level -k-4.

**Method**:
1. Read the module Koszul duality functor definition (chiral_modules.tex,
   thm:e1-module-koszul-duality).
2. Read the vacuum case (prop:vacuum-verma-koszul: Phi(M(0)_k) = M(0)_{-k-4}).
3. The non-vacuum case: M(lambda) has highest weight vector v_lambda annihilated
   by J^a_n for n > 0 and J^0_0 v_lambda = lambda(J^0) v_lambda. Under Phi, the
   level shifts k -> -k-4. The weight must transform under the Feigin-Frenkel
   involution.
4. For sl_2: the Weyl vector is rho = 1, h^v = 2, so the shifted weight should
   be -lambda - 2rho = -lambda - 2 (the rho-shifted action of the longest Weyl
   element). DERIVE THIS — do not guess.
5. Verify: at lambda = 0, recover M(0)_{-k-4} (consistency with proved result).
6. Verify: the Shapovalov determinant transforms correctly
   (prop:shapovalov-koszul).
7. Write as prop:nonvacuum-verma-koszul in chiral_modules.tex.

**Python verification**:
```python
# Verify singular vector loci are complementary
# M(lambda)_k has singular vector at level n iff
# (lambda + 1)(lambda + 1 - n(k+2)) = 0 (for sl_2)
# Under Phi: lambda -> -lambda-2, k -> -k-4
# Singular at level n iff (-lambda-2+1)(-lambda-2+1-n(-k-4+2)) = 0
# = (-lambda-1)(-lambda-1+n(k+2)) = 0
# = (lambda+1)(lambda+1-n(k+2)) = 0 -- SAME!
# This means: singular vector loci are PRESERVED, not complementary.
# Check against prop:shapovalov-koszul before writing.
```

**Narrative integration**: This computation should appear in chiral_modules.tex
near the vacuum case, introduced by: "The vacuum module is the simplest test of
module Koszul duality. What does Phi produce when applied to an arbitrary Verma
module? The answer reveals that Koszul duality acts on highest weights through
the shifted Weyl involution — the same involution that governs the Bernstein-
Gelfand-Gelfand resolution."

### 2.2 Module Computation: Ext^1 at Fractional Level (C1, Priority 1)

**Target**: Compute Ext^1 between two non-isomorphic simple modules in a
non-semisimple category via the bar complex. The simplest case: sl_2 at
admissible level k = -1/2 (the simplest non-integer admissible level for sl_2),
which has exactly 2 simple modules.

**Method**:
1. Read cor:bar-admissible-finiteness (finite-dimensionality at admissible levels).
2. Read prop:ext-tor-exchange (Ext^n_A(M,N) = Tor_n^{A!}(M!,N!)^v).
3. At k = -1/2: the admissible modules are L(0) and L(-1/4) (verify from
   Kac-Wakimoto classification).
4. Compute Ext^1(L(0), L(-1/4)) via the bar resolution:
   0 -> ... -> B^1(A, L(0)) -> B^0(A, L(0)) -> L(0) -> 0
   Apply Hom(-, L(-1/4)) and take cohomology.
5. This should match the known answer from Feigin-Fuchs (or Adamovic-Milas for
   admissible level sl_2).
6. Write as comp:ext1-admissible-sl2 in chiral_modules.tex or
   kac_moody_framework.tex.

**Narrative integration**: "The bar complex computes more than characters: it
computes the extension groups that govern non-semisimple representation categories.
At admissible level k = -1/2, the category of sl_2-modules is the simplest
non-semisimple example, with exactly two simple objects and a single non-trivial
extension between them. The bar resolution computes this extension explicitly..."

### 2.3 Discriminant Spectral Interpretation (C2, Priority 2)

**Target**: Prove or precisely conjecture: the shared discriminant
Delta(x) = (1-3x)(1+x) is the characteristic polynomial of the Kodaira-Spencer
operator T acting on the degree-1 bar cohomology.

**Method**:
1. Read thm:ds-bar-gf-discriminant in examples_summary.tex.
2. Read the Kodaira-Spencer construction in higher_genus.tex.
3. The KS operator T: H^1(bar) -> H^1(bar) is the d_2 differential in the
   bar spectral sequence. Its eigenvalues should be 3 and -1 (the roots of Delta).
4. For sl_2: H^1(bar) is 3-dimensional. T should have eigenvalues related to 3,-1.
5. Compute T explicitly on H^1(bar) for sl_2 using the PBW spectral sequence.
6. If confirmed: write as thm:discriminant-spectral in examples_summary.tex.
   If not: document the obstruction and reformulate.

### 2.4 Genus-Graded Verma Dimensions (C6, Priority 2)

**Target**: Compute dim of the genus-1 component of the genus-graded Verma
module for sl_2. This fills the empty example ex:verma-genus-graded.

**Method**:
1. The genus-1 bar complex B^{(1)}(A, M(0)) uses the genus-1 propagator
   (Eisenstein series E_2).
2. The curvature kappa = 3(k+2)/4 enters via the self-sewing map.
3. At degree 1: one generator of sl_2 inserted once, genus-1 correction from
   E_2. Dimension should be 3 (one for each generator) times the genus-1
   correction factor.
4. Python verification of the dimension.
5. Write in chiral_modules.tex, replacing the empty prose in ex:verma-genus-graded.

### 2.5 Motzkin Combinatorial Model (C5, Priority 3, if time permits)

Only attempt this if 2.1-2.4 are complete. The observation that Virasoro bar
cohomology dimensions are Motzkin differences suggests a bijection with
non-crossing chord diagrams. If a clean bijection exists, write it as a
conjecture with evidence. If not, document the obstruction.

**Compile after each computation in Pass 2.** `make fast` after each new theorem.
Run `cd compute && python3 -m pytest tests/ -q` after any compute engine changes.
Update SYNTHESIS_TODO.md after each item.

---

## PASS 3: VOICE + PRECISION (hours 9-12)

### 3.1 Dead Prose Elimination

Systematic pass through all .tex files. For each file, search for:
- "The key insight is" / "The deepest insight" / "The crucial observation"
  -> Replace with the insight itself, stated as mathematics.
- "This is not merely X but Y" / "This is not an analogy"
  -> State the precise mathematical relationship. If it's a theorem, cite it.
- "providing both conceptual clarity and computational power"
  -> Delete. The clarity and power are evident from the results.
- Any sentence that restates what a displayed formula says in words
  -> Delete, or replace with a sentence that says something the formula doesn't.
- "We now turn to" / "The remaining sections develop"
  -> Replace with a Device A question or Device C shadow.
- "elegantly" / "beautifully" / "remarkably"
  -> Delete the adverb. Let the mathematics speak.

**Vocabulary guide** (the Chriss-Ginzburg register):

| Instead of | Write |
|-----------|-------|
| upgrade | lift / extend / recognize as |
| powerful tool | — (delete; tools prove their power by use) |
| elegant construction | — (delete; or just "construction") |
| key insight | — (state the insight directly) |
| this is not just X | X is an incarnation of Y |
| in fact | (delete — if it's a fact, state it) |
| interestingly | (delete — interest is not announced) |
| it turns out that | (delete — state the result) |
| one can show | we prove (Theorem X) that |
| the reader may verify | (either prove it or cite it) |

### 3.2 Proof Sketch Cleanup (C3)

Fix F4a (lem:obstruction-class) and F4b (lem:period-integral) in
bar_cobar_construction.tex. Replace circular sketch bodies with clean
2-sentence arguments citing the full proofs:

F4a: "The obstruction class [m_0, a] lies in the center of the bar complex.
This is proved as part of Theorem~\ref{thm:XXX}, which establishes centrality
via the Borcherds identity applied to the curvature element."

F4b: "The period integral converges by the log-divergence bound of
Proposition~\ref{prop:XXX}. The relative Stokes theorem applies because
the boundary terms vanish on the Fulton-MacPherson compactification
(Lemma~\ref{lem:XXX})."

### 3.3 Vocabulary Audit

Run grep for each entry in the vocabulary table. Fix all instances in
non-proof, non-example contexts (proofs use technical language appropriately;
the issue is in narrative/remark passages).

```bash
# Find instances to review
for word in "upgrade" "powerful" "elegant" "remarkably" "interestingly" "key insight" "it turns out" "in fact,"; do
  echo "=== $word ==="
  grep -rn "$word" chapters/ --include='*.tex' | grep -v '\\begin{proof}' | head -5
done
```

### 3.4 Transition Audit

For each chapter boundary (chapter N ending -> chapter N+1 opening), verify:
- Chapter N's final paragraph contains a forward shadow (Device C)
- Chapter N+1's opening paragraph contains a question arising from Chapter N
- The connection is *mathematical*, not editorial ("in the next chapter we...")

### 3.5 Final Compilation + Census

```bash
make 2>&1 | tail -10
grep -ic 'undefined\|multiply' main.log
for s in ProvedHere ProvedElsewhere Conjectured Heuristic; do
  echo -n "$s: "; grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
done
```

Update: SYNTHESIS_TODO.md, autonomous_state.md, CLAUDE.md census.

---

## INVARIANTS (violating any means stop and recheck)

All mathematical invariants from SESSION_PROMPT_v8.md §3 apply. Additionally:

| # | Narrative invariant | Violation symptom |
|---|-------------------|-------------------|
| N1 | Every new paragraph carries mathematical content | A paragraph with no theorem, formula, definition, or mathematical connection |
| N2 | No self-praise | "elegantly", "beautifully", "the deepest", "remarkably" in narrative |
| N3 | Questions before constructions | A section opening with "We define..." instead of "What is...?" |
| N4 | Retrospective illumination after main theorems | A main theorem followed by only forward motion, no backward connection |
| N5 | No editorial navigation | "We now turn to", "In this section we", "The following chapters" |

---

## OPERATING PROTOCOL

### Non-Blocking IO
- Do NOT ask blocking questions. If uncertain, make a decision, document it in
  SYNTHESIS_TODO.md under "Deferred / Questions for Raeez", and continue.
- If Raeez leaves a message, incorporate the feedback without losing state.
  Read the message, update SYNTHESIS_TODO.md to reflect any course corrections,
  and continue from where you were.

### State Persistence
- Update SYNTHESIS_TODO.md every 2 hours (or after completing any numbered item).
- The checkpoint log table records: time, items completed, census delta, notes.
- If context is getting long (>100 tool calls), write a detailed state summary
  to notes/SYNTHESIS_STATE.md before the compression event.

### Compilation Discipline
- `make fast` after every 3 edits (not every edit — avoid thrashing).
- Full `make` (3-pass) at the end of each Pass.
- If a compile error appears, fix it immediately before continuing.

### Agent Deployment
- Use agents to READ long files (bar_cobar_construction.tex is 8131 lines).
- Never delegate EDITS to agents. All .tex writing happens in main context.
- Max 3 parallel agents. Use them for: reading files, searching for patterns,
  verifying cross-references.

### What NOT to Touch
- Do not change the document class, font setup, or package list.
- Do not add \newcommand in chapter files.
- Do not modify proved theorems (PH claims). You may add narrative around them,
  but the theorem statements and proofs are adversarially verified.
- Do not change the Master Table data without Python verification.
- Do not create new .tex files (the 3 new chapters from METAMORPHOSIS already exist).

---

## THE MEASURE

Imagine this book arriving on the desk of a mathematician who has:
- Read Chriss-Ginzburg cover to cover
- Published papers on operads and vertex algebras
- Refereed for the Annals twice before

They open to the introduction. Do they find a summary of results, or do they
find a *story* — a mathematical narrative where each theorem answers a question
raised by the previous one, where the examples are not illustrations but
*evidence*, where the nine research programmes are not "future work" but the
natural destinations toward which the proved theorems point?

They turn to the module theory chapter. Do they find 28 abstract theorems and
1 computation, or do they find the abstract theory *at work* — Phi computing
non-vacuum Verma modules, Ext groups at fractional level, the BGG resolution
visible through the bar spectral sequence?

They read the discriminant section. Do they find a numerical observation, or
do they find a spectral interpretation — the discriminant as the characteristic
polynomial of an operator that the framework itself constructs?

The gap between the first version (what the book currently is) and the second
version (what it could be) is the work of this session.

Not by pages written. Not by claims added. By the quality of the synthesis —
the sense that Koszul duality on curves is not a technique but a *principle*,
and that this book is its natural and inevitable exposition.
