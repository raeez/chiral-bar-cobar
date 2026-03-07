# Session v18 — Constitutional Enforcement (Human-Readable)

## What this session does

Five external reviews (raeeznotes10-14) diagnosed the manuscript after all prior repair campaigns. Their verdict: **the core theorems are architecturally sound, but the manuscript hasn't fully become what it already knows it should be.**

This session enforces consistency between what the manuscript knows (Chapter 34's status hierarchy) and what every other chapter says.

## The diagnosis in one paragraph

The four main theorems (A/B/C/D) are structurally repaired. The introduction correctly separates curved fiberwise differentials from strict total differentials, the scalar package from the full Maurer-Cartan package, and unconditional free-field Koszulity from conditional interacting-family Koszulity. But: (1) two critical mathematical issues survive in the source, (2) several proofs are too compressed to be referee-secure, and (3) many chapters still speak in a pre-repair dialect that contradicts the corrected theory.

## What needs to happen, in priority order

### Critical (mathematical errors)

| # | Problem | Fix |
|---|---------|-----|
| C1 | A theorem says "for any chiral algebra, cobar of bar gives a free resolution" — this contradicts the corrected theory (resolution only on Koszul locus) | Delete or rewrite to scoped version |
| C2 | The minimal-model and WZW modular periodicity proofs rely on theta/eta coefficient periodicity, which is false (Ising check: offsets 0,48,96 give 1,2048,223561) | Either downgrade to conjectured, or supply a different proof |

### High (proof quality)

| # | Problem | Fix |
|---|---------|-----|
| C3 | A proved theorem cites a conjecture in its proof | Make the T-matrix argument self-contained, or split into proved + conjectural parts |
| H1 | Theorem A₀ (fundamental twisting morphisms) asserts mapping-cone identifications without constructing them | Add explicit lemma package |
| H2 | Theorem A₁ (bar concentration) uses "degree" ambiguously — cohomological vs internal | Restate in bigraded form |
| H3 | Theorem C₀ (fiber-center) inherits H2's instability | Fix after H2 is resolved |
| H4 | Frame chapter presents Θ_A as if fully constructed, but it's conjectural | Split into proved scalar + conjectural full package |

### Medium (propagation)

| # | Problem | Fix |
|---|---------|-----|
| M1 | Algebraic foundations still previews old definition-by-conclusion | Rewrite to 3-layer preview |
| M2 | Introduction occasionally writes as if full MC package is established | Add qualifying sentence |
| M3 | Three connection/appendix files use mixed differential notation | Standardize to dfib/Dg/d0 |
| M4 | Some passages say "single scalar determines entire genus tower" without "scalar" qualifier | Add "scalar package" everywhere |
| M5 | Scalar Period(A) still appears as primary; should be Π(A) | Promote periodicity triple |
| M6 | KL discussion slides between semisimplified tilting, full abelian, and evaluation-locus categories | Add explicit regime tags |
| M7 | Some example chapters say "modular Koszul" without "conditional on PBW degeneration" | Add qualifier for interacting families |
| M8 | One conjecture has two labels | Remove duplicate label |

## The constitutional principle

Chapter 34 (concordance) already gives the correct:
- Three conjecture tiers
- Five master conjectures
- Seven homotopy templates
- Nine-futures assessment
- Two-stratum (proved core / programme) separation

**Every earlier chapter should be subordinate to Chapter 34.** When they disagree, the earlier chapter needs to be corrected. This is the single organizing principle.

## The five master conjectures

The ~119 remaining conjectures collapse to five structural ones:

1. **PBW degeneration at higher genus** — makes interacting families unconditional
2. **Cyclic L∞ and universal Θ_A** — the principal open problem
3. **Full factorization-categorical DK/KL** — quantum groups
4. **Completed bar for infinite generators** — W∞, Yangians
5. **BV/BRST = bar at all genera** — physics completion (downstream)

These are the real theoremization targets. Don't try to prove 119 conjectures one at a time.

## What this does NOT do

- Does not change any correct proofs
- Does not add new theorems (unless a proof is genuinely available)
- Does not touch the preamble or document class
- Does not add packages or create new .tex files
- Does not expand prose — cuts it

## How each session works

1. **Orient**: Fresh census, compile check, read memory files (3 min)
2. **Select**: Pick ONE target from the priority queue
3. **Gather**: Deploy agents to read relevant source files
4. **Derive**: Work out the mathematics in extended thinking, verify in Python
5. **Write**: Minimum viable edit, compile after each change
6. **Verify**: Census, compilation, Chapter 34 consistency check
7. **Loop**: Select next target if time remains

## Expected trajectory

If executed over several sessions:
- C1+C2: The two critical items should be resolved first (1 session)
- H1-H4: Foundation repairs make A₀/A₁/C₀ referee-secure (1-2 sessions)
- M1-M8: Propagation sweep enforces the constitutional principle (1-2 sessions)
- Research: Master conjectures become the active frontier (ongoing)

## The measure

A reader who has proved theorems about operads and vertex algebras is asking:
1. Are the proofs correct?
2. Does the framework compute?
3. Does the manuscript know what it has proved and what it hasn't?

Question 3 is what this session fixes.
