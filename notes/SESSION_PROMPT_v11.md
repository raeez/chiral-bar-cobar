# SESSION PROMPT v11 — Vision Integration & Depth Engine
# For: Claude Opus 4.6, Code Environment, Extended High Reasoning Mode
# Date: March 2026
# Supersedes: v1-v10, all specialized prompts
# Launch: "Read notes/SESSION_PROMPT_v11.md and execute it."

# ======================================================================
# WHY v11 EXISTS
#
# v10 solved the audit-crash problem by inverting to depth-first.
# But depth work operates on individual theorems. The monograph is
# 1310 pages with 695 proved theorems. It does not lack volume.
#
# What it lacks is ARCHITECTURAL COHERENCE at the highest level:
# the manuscript already contains the vision of modular Koszul duality
# (introduction.tex:129-227, concordance.tex:844-1072) but the
# meta-cognitive architecture (*.md files) and the manuscript's
# pedagogical spine do not yet fully embody it.
#
# raeeznotes.md is an external analysis identifying this gap.
# Its core insight: the book yearns to become a first-principles
# theory of modular homotopy for factorization algebras on curves,
# in which genus is not an external parameter but a deformation
# variable internal to Koszul duality itself.
#
# The manuscript is ~80% there. The delta is specific and actionable.
#
# v11 integrates vision work AND depth work in a single session:
#   Phase 0: Orient (2 min)
#   Phase 1: Vision integration into *.md architecture (30 min)
#   Phase 2: Manuscript strengthening — pedagogical spine (40 min)
#   Phase 3: Mathematical depth — one theorem (remaining time)
#
# Opus 4.6 design:
#   LEVERAGE: Extended thinking for sustained mathematical synthesis
#     — synthesizing raeeznotes vision with existing manuscript content
#     — crafting mathematically precise prose at monograph quality
#     — deriving new mathematical content with full sign/grading tracking
#   LEVERAGE: Parallel agents for independent reading/writing tasks
#   LEVERAGE: Python verification as structural proof-checking
#   LEVERAGE: Pre-specified insertion points (no searching = no waste)
#   PREVENT: Re-reading what's already understood (file:line citations below)
#   PREVENT: Audit gravity (the audit is DONE — 234/234 findings resolved)
#   PREVENT: Target diffusion (three phases, one target per phase, commit)
#   PREVENT: Sycophantic agreement that "it's already there" when it's shallow
#   PREVENT: Hallucinated formulas (compute or cite, never recall)
#   PREVENT: Context starvation (strict reading budget per phase)
# ======================================================================

---

## THE VISION (read this ONCE, hold it in extended thinking, never re-read)

The monograph proves three theorems (A: geometric bar-cobar duality,
B: bar-cobar inversion, C: deformation-obstruction complementarity)
about Koszul duality lifted from points to curves. These are three
aspects of a SINGLE object: the modular Koszul chiral algebra.

**Four irreducible pieces** (the minimal kernel from which everything grows):

1. **Three-point collision** (Arnold relation = factorization coherence).
   The bar differential is residue along collision divisors on FM
   compactifications. Arnold's relation w12^w23 + w23^w31 + w31^w12 = 0
   is the coherence statement that fusing three insertions doesn't depend
   on order. This is the genus-0 seed.

2. **Verdier duality on Ran(X)** (bar-cobar = Verdier exchange).
   D_Ran B_X(A) ~ B_X(A!). The propagator w_ij passes from algebra to
   coalgebra; Verdier exchanges the two. This makes the Koszul dual a
   theorem, not an analogy. Chain-level shadow of Ayala-Francis NAP.

3. **Genus-1 curvature** (d^2 = kappa * omega_1 * id).
   Once the propagator acquires periods, the differential develops
   curvature. The ordinary derived category is too coarse — the natural
   home is Positselski's coderived category. This is the precise form
   of the intuition that quantum corrections are a change in the
   ambient homological category, not extra terms.

4. **Clutching of stable curves** (modular operad = genus tower).
   Genus enters via stable graphs, not just trees. The universal class
   Theta_A is compatible with clutching, trace, and Verdier duality.
   This is where the theory becomes genuinely modular homotopy theory.

**The correct object** is not kappa(A), not Q_g(A), not the genus-g
bar complex separately. It is the modular characteristic package
(Theta_A, H_A, Delta_A) of a factorization algebra on Ran(X):
- Theta_A in MC(Def_cyc(A) hat-tensor RGamma(M-bar_{g,.}, Q))
- H_A := RGamma(M-bar_g, Z_A) with Verdier duality
- Delta_A(x) := det(1 - xT) the spectral discriminant

kappa(A) is the first characteristic number of Theta_A.
The genus tower is one Maurer-Cartan deformation, not a list.
The discriminant is the first non-scalar characteristic class.
The A-hat genus is an index theorem trying to surface.

**The theorematic silhouette** the theory aims toward:
- A_mod: Verdier-intertwined bar-cobar, functorial over M_{g,n}
- B_mod: Inversion on Koszul locus, coderived persistence off it
- C_mod: (-1)-shifted symplectic complementarity (Lagrangian polarization)
- Index: GRR for modular deformations (genus series = A-hat pushforward)
- DK: Derived Drinfeld-Kohno (E1-factorization equivalence, R -> R^{-1})

**Free fields are atoms, not easy examples.** They are the irreducible
kernel displaying full generality: fermion (antisymmetric collapse),
Heisenberg (universal genus series / A-hat), betagamma (discriminant),
KM/Vir/W (functorial shadows), Yangian (E1 door to braided world).

**The ultimate generalization principle**: Arnold (genus 0, additive) ->
clutching + Theta_A (modular, on curves) -> Fay (elliptic, multiplicative).

---

## 0. ORIENT (2 minutes — verify, don't explore)

```bash
cd /Users/raeez/chiral-bar-cobar

# Three numbers (30 seconds)
echo -n "PH: "; grep -rc '\\ClaimStatusProvedHere' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
echo -n "Tests: "; cd compute && .venv/bin/python -m pytest tests/ -q 2>&1 | tail -1; cd ..
make fast 2>&1 | tail -1
```

Expected: PH ~695, 1187 passed, Output written on main.pdf.
If ANY fail: stop, diagnose, do not proceed.

Read ONE file: `memory/ground_truth_mar2026.md` (56 lines).
Do NOT read CLAUDE.md, PROGRAMMES.md, HORIZON.md, autonomous_state.md.

---

## 1. VISION INTEGRATION — Meta-Architecture (30 min)

### What to produce

Update the *.md files so the modular Koszul duality vision is the
ORGANIZING PRINCIPLE, not a side note. Specific deliverables:

### 1a. MEMORY.md — Add Vision section (after "Scope: TRIPLE INTERSECTION")

Insert a "## Modular Koszul Vision" section containing:
- The four irreducible pieces (one line each)
- The correct object (Theta_A, H_A, Delta_A)
- The theorematic silhouette (A_mod through DK)
- Source: raeeznotes.md
- What the manuscript already has vs what it needs

Keep it under 30 lines. MEMORY.md has a 200-line soft cap.

### 1b. PROGRAMMES.md — Reframe around modular Koszul programme

The current PROGRAMMES.md organizes as 9 independent programmes.
raeeznotes shows they are all facets of the single modular Koszul
programme. Add a section at the top (after "The Honest Assessment")
titled "## The Modular Koszul Programme" that:
- States the unifying vision (3 sentences)
- Maps each of Programmes I-IX to its role in the modular Koszul programme
- Identifies the four irreducible pieces as the conceptual foundation
- Identifies the theorematic silhouette as the target

Do NOT restructure the existing programme entries. Add framing above them.

### 1c. Create notes/VISION.md — The distilled architectural document

A standalone document (60-80 lines) that:
- States the modular Koszul duality vision precisely
- Lists the four irreducible pieces with manuscript theorem references
- Lists the theorematic silhouette with manuscript conjecture labels
- Lists where each piece already lives in the manuscript (file:line)
- Lists the specific gaps raeeznotes identifies (with action items)
- Defines the "next volume" skeleton (5 chapter titles from raeeznotes XII)
- Can be read in 3 minutes by a future session for instant orientation

### 1d. Update notes/autonomous_state.md — 5-line summary

Replace the priority queue with the vision-oriented priority:
1. Vision integration (this session)
2. Discriminant promotion (Phase 2)
3. Mathematical depth D1-D6 (Phase 3 and future sessions)

### How to work

Use extended thinking for synthesis. You already have the vision
(Section "THE VISION" above) and the manuscript state (ground_truth).
Write the files directly. Do not re-read raeeznotes.md or the
manuscript chapters — the analysis is pre-computed in this prompt.

**Anti-drift**: After writing each file, ask: "Does this file make the
modular Koszul vision the organizing principle? Would a new session
reading only this file understand the programme?" If no, revise.

---

## 2. MANUSCRIPT STRENGTHENING — Pedagogical Spine (40 min)

The manuscript already says most of what raeeznotes wants. The gap is
sharpness, not content. Three specific edits:

### 2a. introduction.tex — Four-kernel remark

**Location**: After line ~227 (end of the structural perspective section),
before "The formal statements of the three theorems."

**What to add**: A remark (5-15 lines) titled "The four irreducible
pieces" that explicitly identifies Arnold, Verdier, genus-1 curvature,
and clutching as the minimal kernel from which the entire theory grows.
Cross-reference: Arnold relations (Theorem in configuration_spaces.tex),
Verdier exchange (Theorem A), genus-1 curvature (Theorem B + kappa),
clutching (modular operad structure in higher_genus.tex).

**Why**: raeeznotes Section I identifies this as the pedagogical key.
The introduction discusses these four things but doesn't isolate them
as the irreducible kernel. One remark makes this explicit.

### 2b. introduction.tex or free_fields.tex — Atoms framing

**Location**: Either in the introduction's overview of Part II, or at
the start of free_fields.tex (which already has some of this).

**What to add**: A remark (5-10 lines) titled "Free fields as atoms"
stating that the free fermion, Heisenberg, and betagamma/bc systems
are not easy examples but the atoms from which all later examples are
assembled, each displaying a distinct face of modular Koszul duality.
Map: fermion -> antisymmetric collapse, Heisenberg -> universal genus
series (A-hat), betagamma -> discriminant, and note that KM/Vir/W
display the same phenomena via DS reduction.

**Why**: raeeznotes Section V. The manuscript has fragments of this
but never the clean one-paragraph synthesis.

### 2c. concordance.tex — Discriminant promotion

**Location**: In the programme section (concordance.tex:844+), add a
subsection "The discriminant as spectral invariant" between the
existing subsections.

**What to add**: 10-20 lines promoting Delta_A(x) from "shared
generating function curiosity" to "the first genuinely nontrivial
non-scalar characteristic class of the modular Koszul object." State
that distinct chiral theories can lie on the same modular spectral
sheet even when their local operator content is different. The real
invariant is the branch geometry of Delta, not the individual GF.
DS reduction changes the growth pole while preserving the discriminant
family — this is a functorial consequence of the modular structure.
Cross-ref: thm:ds-bar-gf-discriminant (examples_summary.tex).

Optionally formulate this as a conjecture:
"For a modular Koszul object A, the discriminant Delta_A(x) = det(1-xT)
where T is the Kodaira-Spencer operator on H^1(bar(A))."
This connects to depth target D4.

**Why**: raeeznotes Section VI. The manuscript proves the shared
discriminant theorem but doesn't name it as a characteristic class
or connect it to the spectral interpretation.

### How to work

Read the exact insertion points (+-30 lines) before writing.
Write in the manuscript's voice: impersonal, cross-referenced,
indexed, with \label and \ref. Use existing macros.

After each edit: `make fast 2>&1 | tail -3`.
If compilation fails: fix before next edit.

**Anti-hallucination**: Every theorem cited must be verified by reading
its label in the manuscript. Every formula must be computed or quoted.
Do NOT invent cross-references — read the target first.

**Quality check**: After all three edits, re-read the modified passages
in context (+-100 lines). Ask: "Would Serre find this precise? Would
Witten find this illuminating? Would Polyakov find this physical?"

---

## 3. MATHEMATICAL DEPTH (remaining time)

If time remains after Phases 1-2, execute the highest-scoring depth
target from memory/depth_targets.md. The targets are pre-scored:

- **D1** (Phi on Verma, score 100) — show the machine works on modules
- **D4** (Discriminant spectral, score 60) — prove Delta = det(1-xT)
  (connects directly to the discriminant promotion in Phase 2)
- **D3** (BRST=bar, score 64) — ALREADY DONE at genus 0

D4 is now the natural target because Phase 2c promotes the discriminant
and D4 would substantiate it. But D1 has higher impact.

Follow the v10 DERIVE protocol (Sections 3-4 of SESSION_PROMPT_v10.md):
- Gather via agents (2 readers, no edits)
- Derive in extended thinking (hypothesis verification, step-by-step, self-adversarial)
- Python verification (mandatory for every formula)
- Write only after derivation is complete and verified

---

## 4. CLOSE (5 min)

```bash
make fast 2>&1 | tail -5
echo -n "PH: "; grep -rc '\\ClaimStatusProvedHere' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print s}'
cd compute && .venv/bin/python -m pytest tests/ -q 2>&1 | tail -1; cd ..
```

Update ONLY:
1. `memory/ground_truth_mar2026.md` — census if changed
2. `memory/MEMORY.md` — if Phase 1a was done
3. `notes/autonomous_state.md` — 5-line session summary
4. `notes/VISION.md` — if Phase 1c was done (already created this session)

Do NOT update: CLAUDE.md, SESSION_PROMPT_v11.md, PROGRAMMES.md (unless Phase 1b).

---

## 5. INVARIANTS

| # | Fact | Trap |
|---|------|------|
| 1 | Com! = Lie (NOT coLie) | Koszul dual coalgebra = SUB of cofree |
| 2 | H! = Sym^ch(V*) (NOT self-dual) | F! = betagamma (NOT Heisenberg) |
| 3 | FF involution: k <-> -k-2h^v | NOT -k-h^v |
| 4 | Cohomological grading: \|d\| = +1 | Bar uses desuspension s^{-1} |
| 5 | Curved: m1^2(a) = [m0, a] | MINUS sign in commutator |
| 6 | P-inf-chiral != Coisson | Different quantization levels |
| 7 | d_bracket^2 != 0 | Use PBW SS, not matrix rank |
| 8 | sl2: h^v=2, rho=1, dim=3 | Weyl-Kac: k -> -k-4 (not -k-2) |

---

## 6. CONTEXT BUDGET

| Phase | Tool calls | Context % |
|-------|-----------|-----------|
| Orient | 3-5 | 5% |
| Vision (*.md) | 8-12 | 15% |
| Manuscript | 15-25 | 30% |
| Depth | 20-30 | 40% |
| Close | 3-5 | 5% |

Checkpoint at tool call 50: write state to notes/autonomous_state.md.
Checkpoint at tool call 100: repeat.

If blocked in any phase: document obstruction, move to next phase.
Never loop. Never retry the same approach. The session has three
independent phases — a block in one does not kill the others.

---

## 7. THE MEASURE

A session succeeds if it produces ALL of:
- [ ] notes/VISION.md exists and is the definitive 60-80 line reference
- [ ] memory/MEMORY.md has a "Modular Koszul Vision" section
- [ ] At least one manuscript edit compiles cleanly
- [ ] PH count unchanged or increased; zero new compilation errors

A session excels if it ALSO produces:
- [ ] All three manuscript edits (2a, 2b, 2c) compile cleanly
- [ ] One depth target advanced (D1 or D4)
- [ ] Every new passage survives the Serre/Witten/Polyakov test

The book has 695 proved theorems and the modular Koszul vision
already written in its introduction. What it needs is for that
vision to permeate the architecture — the *.md files that guide
future sessions, the pedagogical spine that guides the reader,
and (when the architecture is right) the mathematical depth that
proves the machine works on non-trivial examples.

That is what this session is for.
