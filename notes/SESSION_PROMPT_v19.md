# SESSION PROMPT v19 — SEMANTIC DEBT ELIMINATION
# For: Claude Opus 4.6, Code Environment, Extra-High Reasoning Mode
# Date: March 2026
# Supersedes: v18 (constitutional enforcement engine — retained as guardrail)
# Launch: "Read notes/SESSION_PROMPT_v19.md and execute it."

# ======================================================================
# DESIGN RATIONALE
#
# v18 was a constitutional enforcement engine: it repaired mathematical
# errors, deployed regime tags, propagated status discipline, and built
# the proof-programme infrastructure. It succeeded. The priority queue
# is largely exhausted. The mathematical content is sound.
#
# What remains is not mathematics but *craft*. The monograph reads like
# a construction site where the building is structurally complete but
# scaffolding, temporary signage, and construction debris remain
# visible. The task now is demolition of that scaffolding — revealing
# the building's actual architecture.
#
# v19 is a PROSE SURGERY ENGINE. Its target: every line that does not
# earn its place in a book aspiring to the standard of Chriss-Ginzburg,
# Polyakov, and Witten.
#
# The metaphor: "technical debt" applied to prose. In a codebase,
# technical debt is working code that is harder to read, maintain, or
# extend than it needs to be. In a monograph, semantic debt is correct
# mathematics that is harder to read, absorb, or believe than it needs
# to be. Both slow down everyone who touches the system. Both
# accumulate invisibly. Both are eliminated not by adding but by
# subtracting.
#
# Architecture for Opus 4.6 extended reasoning:
#   LEVERAGE: Extended thinking for prose surgery (rewrite in mind,
#             then emit clean version — never draft-then-revise in file)
#   LEVERAGE: Parallel agents for chapter-pair consistency audits
#   LEVERAGE: The monograph's own gold standard (heisenberg_frame.tex)
#             as the concrete template — not an abstract style guide
#   LEVERAGE: Compositional prose (build complex paragraphs from simple
#             sentences, each carrying one idea — mirrors how Opus 4.6
#             generates coherent long-form output)
#   LEVERAGE: Concrete before abstract (always anchor definitions in
#             the example the reader already knows — mirrors how the
#             model's attention works best)
#   PREVENT: Prose hallucination (never invent motivation or physical
#            interpretation — only sharpen what exists or delete what
#            doesn't earn its place)
#   PREVENT: Over-deletion (never remove mathematical content, cross-
#            references, or index entries — only compress prose wrapper)
#   PREVENT: Style drift (every edit must pass the heisenberg_frame
#            test: would this paragraph be at home in Chapter 1?)
#   PREVENT: Uniformity fetish (different chapters have different
#            densities — a proof chapter reads differently from a
#            portrait chapter — do not flatten this)
#   PREVENT: Adding while subtracting (do not introduce new remarks,
#            new scope disclaimers, new status legends while removing
#            old ones — net line count must decrease or stay flat)
#   PREVENT: Breaking compilation (make fast after every file touched)
# ======================================================================

---

## 0. THE THREE VOICES

The monograph lives at a triple intersection. Each voice has a master
and a failure mode. Know both.

### Voice 1: The Mathematician (Chriss-Ginzburg)

**The standard**: Every section opens with a governing question that
the reader can hold in mind. Definitions are motivated by the question
they answer. Theorems are stated before they are proved. Proofs are
complete but not longer than necessary. Examples follow theorems
immediately and show the theorem *working*, not merely *existing*.

**The gold standard in this monograph**: heisenberg_frame.tex. Lines
1-31. The algebra is defined in 19 lines. The governing question is
stated in 5 lines. No preamble. No "In this chapter we will..." No
"Recall that..." The reader is inside the mathematics from sentence
one.

**The failure mode you are eliminating**: Scaffolding voice. "We now
turn to..." "It is natural to consider..." "One might ask..." "Recall
that..." These are the sounds of a writer who has not yet decided
what to say. Replace them with assertions. Instead of "We now explain
why logarithmic forms are forced," write "Logarithmic forms are
forced by three constraints:" — or, better, state the theorem that
*proves* they are forced.

**Specific debt patterns**:
- Bullet lists where prose would be clearer (~15% of 940 itemizations)
- Definitions nested inside definitions (bar_cobar_construction.tex
  sign section)
- Forward references without intuitive content ("as we will see in
  Chapter X" — either give the content or delete the forward ref)
- Duplicate definitions across chapters (Heisenberg defined 3×,
  Arnold relations explained 3×)

### Voice 2: The Physicist (Polyakov)

**The standard**: Physical content comes first. A formula is not
understood until its physical meaning is clear. When a computation
yields a number, the text says what it means — not what theorem
produced it, but what it *is*. Central charge is the conformal
anomaly. The curvature m₀ is the cosmological constant. κ = 0 is
anomaly cancellation.

**The gold standard in this monograph**: higher_genus.tex lines 36-59.
The physical parallel track table. "Fiberwise curvature ↔ conformal
anomaly. κ = 0 ↔ anomaly cancellation. Coderived ↔ off-shell."
Then: "These identifications are theorems, not analogies." That
sentence is the Polyakov voice at its best: the physics is real.

**The failure mode you are eliminating**: Physics as decoration.
Remarks that say "The physical interpretation is..." followed by a
vague analogy. If the identification is a theorem, state the theorem
number. If it is a conjecture, give the conjecture number. If it is
neither — if it is just a suggestive parallel — then it is scaffolding
and should be compressed to a single sentence or deleted.

**Specific debt patterns**:
- "The physical interpretation is..." without theorem/conjecture ref
  (~8-12 instances across connections chapters)
- Heuristic sections that blur proved/open boundary (feynman_diagrams
  has 9 heuristic claims without clear section break)
- Conditional language for unconditional results ("should satisfy"
  for things that are proved)

### Voice 3: The Mathematical Physicist (Witten)

**The standard**: The deepest insight is always structural: *why* does
this formula have this form? Because of a deeper theorem. The Todd
genus appears in the genus expansion not by accident but because
of the family index theorem. The bar complex is the BRST complex
not by analogy but by Verdier duality on the FM compactification.
Every "coincidence" is the shadow of a theorem.

**The gold standard in this monograph**: genus_expansions.tex lines
129-144. The connection to the Â-genus is explained *with* the
structural reason (family index theorem). The text shows the formula,
then shows *why*: "This identification is not coincidental."

**The failure mode you are eliminating**: Structural insight without
structural proof. Remarks that say "This is not a coincidence" but
then gesture at a connection without stating the precise theorem
that explains it. Either state the theorem (with \ref) or mark the
connection as conjectured (with status tag). The in-between — the
confident wave of the hand — is the debt.

**Specific debt patterns**:
- "This is related to..." without precise statement (~10 instances)
- Parallel track tables without theorem references for each row
- Concordance entries that describe connections without cross-refs
  to the exact proving theorem

---

## 1. ORIENT (execute literally)

```bash
cd /Users/raeez/chiral-bar-cobar

# Census
echo "=== CENSUS ==="
for s in ProvedHere ProvedElsewhere Conjectured Heuristic; do
  echo -n "$s: "; grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
done

# Line counts by part
echo "=== LINE COUNTS ==="
echo -n "Theory: "; wc -l chapters/theory/*.tex | tail -1
echo -n "Examples: "; wc -l chapters/examples/*.tex | tail -1
echo -n "Connections: "; wc -l chapters/connections/*.tex | tail -1
echo -n "Appendices: "; wc -l appendices/*.tex | tail -1
echo -n "Frame: "; wc -l chapters/frame/*.tex | tail -1

# Build gate
echo "=== BUILD ==="
pkill -9 -f pdflatex 2>/dev/null; sleep 2
make fast 2>&1 | tail -5
```

Read: heisenberg_frame.tex (FULL — this is your style template for
the session).

---

## 2. SELECT CHAPTER

### The Debt Inventory (by severity × volume)

**Tier A — Highest leverage** (prose surgery changes reading experience):

| ID | Chapter | Debt Type | Volume | Lever |
|----|---------|-----------|--------|-------|
| A1 | bar_cobar_construction.tex | Sign section dense; nested defs; W∞ "no dual" framing now fixed but surrounding prose still scaffolded | 8131 lines | Core chapter — every reader hits this |
| A2 | higher_genus.tex | A∞ section feels inserted; some scope remarks verbose; genus-2 d²=0 proof cleaned but surrounding narrative patchy | 7472 lines | Deepest chapter — reviewer scrutiny highest |
| A3 | configuration_spaces.tex | 60% geometric preliminaries that could be tighter; opening doesn't distinguish standard from novel | 3942 lines | Prerequisite chapter — sets tone |
| A4 | free_fields.tex | Heisenberg exposition duplicates frame chapter; surjectivity argument repeated 3× | 3540 lines | Most-read example chapter |

**Tier B — High leverage** (voice alignment):

| ID | Chapter | Debt Type | Volume | Lever |
|----|---------|-----------|--------|-------|
| B1 | chiral_modules.tex | Module Koszul duality stated abstractly; few worked examples | 4400 lines | Machinery without payoff |
| B2 | kac_moody_framework.tex | Opening lacks "why KM?" motivation; some conditional language | 2760 lines | Key portrait |
| B3 | w_algebras_framework.tex | DS reduction reads as appendix, not structural transport | 2298 lines | Key portrait |
| B4 | genus_expansions.tex | Three Theorems showcase reads like data dump in table sections | 2500 lines | Climax chapter |

**Tier C — Medium leverage** (consistency):

| ID | Chapter | Debt Type | Volume | Lever |
|----|---------|-----------|--------|-------|
| C1 | holomorphic_topological.tex | Proved/open blur in AGT section; 14 conjectures mixed with proved | 1158 lines | Referee target |
| C2 | bv_brst.tex | "We now explain" scaffolding voice; 4 heuristics need separation | 739 lines | Physics bridge |
| C3 | feynman_diagrams.tex | 9 heuristics with no section break from proved content | 1264 lines | Referee target |
| C4 | concordance.tex | "Control interface" terminology; redundant proof-roadmaps | 569 lines | Constitutional |

**Tier D — Appendix polish** (diminishing returns):

| ID | Appendix | Notes |
|----|----------|-------|
| D1 | arnold_relations.tex | Technically clean; may cross-ref better |
| D2 | signs_and_shifts.tex | Reference material; minimal prose surgery |

### Selection Protocol

1. Read the line counts from Phase 1. Identify the 3 largest files
   you have not yet examined in this session.
2. Use extended thinking to assess: which chapter, if surgically
   edited to heisenberg_frame standard, would most improve the
   reader's experience of the monograph as a whole?
3. Select ONE chapter. Announce: "TARGET: [file], [debt type]."
4. Do not select concordance.tex — it is the constitution, not the
   patient.

---

## 3. DIAGNOSE (extended thinking + agents)

### The Heisenberg Test

For every paragraph in the target chapter, ask:

1. **Does it open with content?** (Not "We now..." or "Recall...")
   If not: rewrite the opening sentence as an assertion.

2. **Does it carry exactly one idea?** (Not two ideas glued with
   "moreover" or "furthermore")
   If not: split into two paragraphs, or delete the weaker idea.

3. **Is the ratio of prose to mathematics appropriate?** A paragraph
   of prose surrounding a one-line equation is suspicious. A
   paragraph of prose surrounding a theorem statement is correct.

4. **Does it survive the deletion test?** If you delete this
   paragraph, does the logical flow from the previous paragraph to
   the next one *improve*? If yes: delete it.

5. **Is it a scope remark that could be a single sentence?** Many
   scope remarks run 6-10 lines. Most can be compressed to: "This
   result is proved at M-level; the H-level realization is
   Conjecture~\ref{conj:xxx}."

### Deploy agents for context

```
Agent 1 (research): Read [target chapter] in full. List every:
  - Paragraph beginning with "We now", "Recall", "It is natural",
    "One might", "Note that", "As discussed", "As we saw"
  - Bullet list with ≤ 2 items (should be prose)
  - Remark with > 8 lines (candidate for compression)
  - Duplicate definition (cross-ref to Part 1 would suffice)
  Return: list of (line_number, first_10_words, debt_type)

Agent 2 (research): Read heisenberg_frame.tex in full. Extract:
  - Every paragraph-opening pattern (first 5 words of each ¶)
  - Every transition between sections (how does CG do it?)
  - The ratio of prose lines to math lines per section
  Return: the heisenberg_frame style fingerprint
```

While agents run: in extended thinking, read the chapter yourself.
Mark (mentally) every passage that makes you wince. Those are the
targets.

---

## 4. OPERATE (the surgery)

### Principles (in priority order)

**Principle 1: Subtract, do not add.**
The target is net negative line count. Every line you add must be
justified by removing at least two. If you find yourself writing
new scope remarks, new status legends, new "reading mode" metadata:
STOP. You are creating debt, not eliminating it.

**Principle 2: Preserve the mathematics.**
Never alter a theorem statement, a proof step, a formula, a label,
a cross-reference, or an index entry. The surgery is on the prose
*around* the mathematics, not on the mathematics itself. If you
cannot improve a passage without changing its mathematical content,
leave it alone.

**Principle 3: The opening paragraph is the highest-leverage edit.**
Readers form their impression of a chapter in the first 30 lines.
If the first paragraph says "In this chapter we study..." — rewrite
it. If it says "Let X be a smooth algebraic curve. The algebra A
has..." — leave it. The heisenberg_frame test: does the reader
encounter mathematics in the first sentence?

**Principle 4: Replace scaffolding with structure.**
"We now turn to the sign compatibility question" → delete, because
the section heading already says "Sign compatibility."
"Recall that the bar complex was defined in §X" → replace with
"The bar complex (§X) satisfies..."
"It is natural to ask whether..." → replace with "Theorem X shows
that..." or "Conjecture X asks whether..."

**Principle 5: Compress scope remarks to one sentence.**
Before: "This result is proved at the model level, using the
explicit bar complex computation of Chapter X. The stronger
homotopy-level realization, which would require constructing the
universal Maurer-Cartan class, remains conjectural and is recorded
as Conjecture Y in the concordance chapter."
After: "Proved at M-level; H-level realization is
Conjecture~\ref{conj:Y}."

**Principle 6: Kill duplicate expositions.**
If heisenberg_frame.tex already explains the bar complex, the
Heisenberg section of free_fields.tex should not re-explain it.
Replace the duplicate with: "The bar complex of $\mathcal{H}_k$
was computed in Chapter~\ref{ch:heisenberg-frame}; here we record
the invariants that feed the Master Table."

**Principle 7: Convert suitable bullet lists to prose.**
A list of 2 items is always better as a sentence with "and."
A list of 3 items describing a single concept is better as a
sentence with serial comma.
A list of 4+ items performing genuine case analysis should stay.

**Principle 8: Physical meaning in the same sentence as the formula.**
Not: "[formula]. The physical interpretation is: [separate paragraph]."
But: "[formula], which is the conformal anomaly of the theory."

### Execution

For each passage identified in Phase 3:

1. Compose the replacement in extended thinking. Do not touch the file
   until you have the full replacement ready.
2. Use the Edit tool with precise old_string / new_string.
3. After each file edit: `pkill -9 -f pdflatex; sleep 2; make fast`
4. If compilation fails: revert immediately. Diagnose. Re-edit.
5. Every 5 edits: count lines changed. If net positive: pause and
   reconsider whether you are adding debt.

### What NOT to do

- Do not add comments explaining why you deleted something
- Do not add "Note: this section was simplified in the March 2026 edit"
- Do not restructure section ordering (that is architecture, not prose)
- Do not merge or split chapters
- Do not touch the concordance (constitution)
- Do not touch the bibliography
- Do not add or remove \ClaimStatus tags (that is v18 territory)
- Do not add or remove theorem environments (that is mathematics)

---

## 5. VERIFY

```bash
# Compile
pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast 2>&1 | tail -5

# Line count comparison
echo "=== POST-SURGERY LINE COUNT ==="
wc -l [target-file]

# Census (must be unchanged — surgery is prose, not claims)
echo "=== CENSUS ==="
for s in ProvedHere ProvedElsewhere Conjectured Heuristic; do
  echo -n "$s: "; grep -rc "\\\\ClaimStatus$s" chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
done

# Verify no new undefined refs
grep -c 'undefined' main.log 2>/dev/null || echo "No log found"

# Verify no deleted labels still referenced
grep 'LaTeX Warning.*ref' main.log | head -20
```

**Success criteria**:
- Compilation clean
- Census UNCHANGED (same PH, PE, CJ, HE counts)
- Net line count of target file: DECREASED or UNCHANGED
- No new undefined references
- No deleted cross-references

---

## 6. LOOP

Return to Phase 2 and select next chapter.

**Session pacing**: Aim for 2-3 chapters per session. Depth over
breadth. A single chapter brought fully to heisenberg_frame standard
is worth more than five chapters with scattered touch-ups.

**Session end protocol**: Same as v18 §7 — full build, census, update
autonomous_state.md.

---

## 7. THE ESSENTIAL CORE (what the reader must walk away with)

This section exists so you never lose sight of *why* you are editing.
The monograph proves four theorems and situates them in a landscape.
Everything else is in service of that.

**The four theorems** (Stratum I — proved):
- **A**: Bar-cobar adjunction via configuration space integrals
- **B**: Inversion on the Koszul locus (spectral sequence collapse)
- **C**: Deformation-obstruction complementarity (Q_g(A) + Q_g(A!) = H*(M_g, Z(A)))
- **D**: Modular characteristic (single scalar κ controls all genera)

**The landscape** (Stratum II — programme):
- Five master conjectures (MC1-MC5) with proof roadmaps
- Nine futures, each connected to the four theorems
- Physics dictionary (BRST = bar, anomaly = curvature, holography = Koszul)

**The reader's experience should be**: "I understand what these four
theorems say, I believe the proofs, and I see why they matter — both
mathematically and physically." Every sentence that does not contribute
to this experience is a candidate for deletion.

---

## 8. MATHEMATICAL INVARIANTS

Same as v18 §8. These are non-negotiable and unchanged by prose surgery.

---

## 9. FAILURE MODES (prose-specific)

| Mode | Signal | Exit |
|------|--------|------|
| **Adding while subtracting** | Net line count increasing | STOP. Delete your additions. The goal is subtraction. |
| **Style uniformity** | Every paragraph sounds the same | STOP. Different chapters have different textures. A proof chapter is dense. A portrait chapter breathes. |
| **Motivation invention** | Writing physical intuition not in the source | STOP. You are hallucinating motivation. Only sharpen what exists. |
| **Perfectionism** | Rewriting a paragraph 3+ times | STOP. Move to the next passage. Diminishing returns. |
| **Census drift** | Claim counts changed | STOP. You accidentally deleted or added a claim tag. Revert. |
| **Cross-ref breakage** | Compilation warnings about undefined refs | STOP. You deleted a labeled environment. Restore it. |
| **Concordance edit** | Touching concordance.tex | STOP. The constitution is not the patient. |

---

## 10. EXEMPLAR

To anchor the target, here is a before/after at the paragraph level.

**Before** (scaffolding voice):
```
We now turn to the question of sign compatibility. As discussed in
§3.2, the bar construction involves three types of signs: Koszul
signs from the tensor algebra, orientation signs from configuration
space coordinates, and operadic signs from the operad composition.
It is natural to ask whether these signs are compatible. The following
proposition shows that they are.
```

**After** (heisenberg_frame voice):
```
The bar construction carries three sign sources — Koszul, orientation,
and operadic — which must be mutually consistent for $d^2 = 0$.
```

The proposition follows immediately. Five lines become two. No
information is lost. The reader's cognitive budget is respected.

---

## 11. META-INSTRUCTION FOR EXTENDED THINKING

When you enter extended thinking for a passage rewrite, use this
internal protocol:

1. Read the passage. Identify the ONE idea it communicates.
2. State that idea in one sentence.
3. Ask: does the passage add anything beyond that one sentence?
   - If yes: write the minimal paragraph that carries the idea
     plus the additions.
   - If no: the one sentence IS the replacement.
4. Check: does the replacement preserve all \ref, \label, \index,
   \eqref references from the original?
5. Emit the replacement.

This protocol prevents the most common Opus 4.6 failure mode in
prose editing: generating a replacement that is *different* but not
*shorter*. The goal is always: fewer words, same content, same
references.
