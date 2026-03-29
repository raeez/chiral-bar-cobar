# HEATMAP — INTERSECTIONS, UNIONS, CRITICAL HOTSPOTS

## The one-to-many map's image

Each catalogue item hits multiple manuscript files. When the images of
different items overlap, the overlapping file must integrate multiple
conceptual threads simultaneously. These intersections are the hardest
rewrites and must be done with the most care.

---

## INTERSECTION TABLE

Files hit by multiple clusters:

| File | Clusters | Intensity | Notes |
|------|----------|-----------|-------|
| chapters/theory/introduction.tex | A, B, G | CRITICAL (3x) | Must integrate open-sector reorientation, A_infty definition, scope narrowings simultaneously. This is the single hardest rewrite. |
| chapters/frame/preface.tex | A, G | CRITICAL (2x) | Open-sector thread + editorial finalization. Must tell the whole story in four acts. |
| chapters/theory/chiral_hochschild_koszul.tex | A, D | CRITICAL (2x) | Must restructure from closed-only to three-part (chains, cochains/braces, center theorem). Also needs bar-vs-center distinction. |
| chapters/theory/higher_genus_modular_koszul.tex | A, E | HIGH (2x) | Open-sector perspective on shadow tower + new subsection on modular traces. These are complementary, not conflicting. |
| chapters/theory/e1_modular_koszul.tex | A, E | HIGH (2x) | E_1 modular + ribbon/'t Hooft + cyclic traces. These are three facets of the same object. |
| chapters/connections/concordance.tex | A, E, G | HIGH (3x) | Open-sector architecture + modular-traces framework + meta-theorem alignment. Many additions, none conflicting. |
| chapters/connections/holomorphic_topological.tex | A, (D) | MODERATE (1.5x) | Ground "why 2d+1" in center theorem. Also needs bar-vs-center clarification. |
| introduction.tex (Vol II) | A | CRITICAL (1x) | Complete rewrite to open-sector-primary perspective. |
| preface.tex (Vol II) | A | CRITICAL (1x) | Complete rewrite. |
| ht_bulk_boundary_line_core.tex (Vol II) | A | CRITICAL (1x) | Promote universal center theorem from HT-specific. |
| hochschild.tex (Vol II) | A, D | HIGH (2x) | Connect to Deligne-Tamarkin + bar-vs-center separation. |
| brace.tex (Vol II) | A | HIGH (1x) | State brace theorem as standalone; connect to initiality. |
| chapters/theory/configuration_spaces.tex | C | CRITICAL (1x) | Major expansion for bordered/mixed geometry. |

---

## THE 7 CRITICAL HOTSPOTS

These files require the deepest, most careful rewriting. They sit at the
intersection of multiple conceptual threads and will determine whether the
rewrite succeeds or fails.

### 1. Vol I Introduction (chapters/theory/introduction.tex)
**Clusters:** A + B + G
**Why critical:** This is the reader's first encounter with the theory. It
must tell the story from Arnold to modularity, through the center theorem.
Currently it stops before the center theorem. The entire dependency DAG
must be presented. The staircase must be stated.
**Dependency:** Requires Chapter 8 (open sector) to exist first, so it can
forward-reference. But conceptually, the introduction should be written
LAST, once the whole story is clear.
**Risk:** Scope inflation (AP7). The introduction must not claim more than
the manuscript proves. Every universal claim must be qualified.

### 2. Vol I Preface (chapters/frame/preface.tex)
**Clusters:** A + G
**Why critical:** The Heisenberg atom is the anchor. The open-sector thread
must grow organically from it, not be bolted on. The four-act structure
(seed → duality → open sector → modularity) must feel inevitable.
**Risk:** Over-narrating. The preface should SHOW (via the Heisenberg atom)
not TELL (via slogans). Every formula must be independently verified.

### 3. Vol I Chiral Hochschild chapter (chapters/theory/chiral_hochschild_koszul.tex)
**Clusters:** A + D
**Why critical:** Currently closed-sector only. Must absorb the brace algebra
(from V2-7), the center theorem (RL-10), and the bar-vs-center distinction
(RL-14). This is where the open sector first becomes visible in the closed
theory.
**Risk:** Becoming a kitchen sink. The restructuring into three clean parts
(chains, cochains, center) must be disciplined.

### 4. Vol I Configuration spaces (chapters/theory/configuration_spaces.tex)
**Cluster:** C
**Why critical:** The bordered/mixed geometry (RL-2, RL-3) is FOUNDATIONAL.
Without it, the global open sector cannot be defined. This chapter must
contain: real oriented blowup, tangential log curves, boundary intervals,
mixed configuration spaces, bordered FM compactification, four types of
codimension-one strata.
**Risk:** The Mok25 dependency (AP11). The log-FM material must be cleanly
isolable. Flag every result that depends on Mok25 with an explicit fallback.

### 5. Vol II Introduction
**Cluster:** A
**Why critical:** Must present the open-sector-primary perspective from the
start. Not "here is another way to think about chiral algebras" but "the
primitive object is the open category; everything else is a shadow."
**Risk:** Disconnection from Vol I. The Vol II introduction must reference
the Vol I center theorem explicitly.

### 6. Vol II Preface
**Cluster:** A
**Why critical:** Sets the tone for the entire second volume. Must motivate
WHY we need a separate volume: Vol I proves the algebraic engine; Vol II
develops the categorical/geometric depth of the open sector and its physics.

### 7. Vol II Bulk-boundary-line (ht_bulk_boundary_line_core.tex)
**Cluster:** A
**Why critical:** This is the file that currently ALMOST states the universal
center theorem but restricts it to HT theories. The rewrite promotes it to
a universal result: bulk = center = HH^bullet(A^!) for any A_infty-chiral
algebra, not just HT boundary algebras.
**Risk:** The +1075 lines of existing content contain HT-specific material
that must be separated from the universal theorem. Don't delete the HT
material — separate it into a "physical realization" section after the
universal theorem.

---

## HEAT GRADIENTS

Files sorted by total rewrite intensity, combining all clusters:

### VOLCANIC (complete rewrite or new creation)
1. NEW: Vol I Chapter 8 "The open sector"
2. NEW: Vol II Chapter 6 "Tangential log curves"
3. NEW: Vol II Chapter 7 "Jacobi coalgebra"
4. NEW: Vol II Chapter 14 "Modular completion from traces"
5. NEW: Vol I Chapter 38 "Staircase of examples"
6. NEW: Vol II Chapters 15-20 (6 example chapters)

### RED (heavy rewrite of existing content)
7. Vol I introduction
8. Vol I preface
9. Vol I chiral Hochschild chapter
10. Vol I configuration spaces chapter
11. Vol II introduction
12. Vol II preface
13. Vol II bulk-boundary-line chapter

### ORANGE (moderate rewrite)
14. Vol I higher-genus modular Koszul
15. Vol I E_1 modular Koszul
16. Vol I concordance
17. Vol I holomorphic-topological connections
18. Vol I algebraic foundations
19. Vol II foundations
20. Vol II hochschild
21. Vol II brace
22. Vol II bar-cobar review
23. Vol II spectral braiding
24. Vol II modular PVA quantization
25. Vol I arithmetic shadows
26. Vol I all example chapters (7 files)

### YELLOW (light touch)
27-120. All remaining files: cross-references, editorial, metadata.

---

## UNION: THE FULL REWRITE FOOTPRINT

Total unique files touched: ~120 across both volumes
  - Vol I: ~85 files (of ~98 modified + new)
  - Vol II: ~35 files (of ~86 modified + new)

New files to create: ~11
  - Vol I: 2 new chapters
  - Vol II: 3 new chapters + 6 new example chapters

Files requiring NO changes: ~30
  - Most appendices (signs, Arnold, nilpotent completion, etc.)
  - Bar complex tables
  - Some THQG files (after status audit)

---

## CRITICAL PATH

The dependency ordering for the rewrite is:

    Configuration spaces (C) ──> Open sector chapter (A) ──> Chiral Hochschild (A+D)
         │                              │                          │
         │                              v                          v
         │                    Vol II center theorem         Higher-genus traces (E)
         │                              │                          │
         v                              v                          v
    Bordered FM ──────────> Modular cooperad ──────────> Modular MC equation
         │                                                         │
         v                                                         v
    Vol I Introduction ────────────────────────────────> Concordance
         │
         v
    Vol I Preface

So the critical path is:
  1. Configuration spaces (foundations)
  2. Open sector chapter (conceptual heart)
  3. Chiral Hochschild restructure
  4. Higher-genus traces subsection
  5. Introduction
  6. Preface
  7. Concordance

Everything else can proceed in parallel after step 2.
