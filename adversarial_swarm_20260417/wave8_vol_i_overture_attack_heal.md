# Wave 8 — Vol I Overture (Heisenberg CG opening) attack & heal

**Target.** `/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex`, 4918 lines. Referenced from `main.tex:1014-1017` as `\part*{Overture}` (unnumbered), positioned after the Introduction and before Part I, matching the architecture spec in CLAUDE.md.

**Opening snapshot.** Three opening sentences:

> One generator. One relation.
> $J(z)\,J(w) \sim k/(z-w)^2.$
> If bar-cobar duality fails for this OPE, it fails everywhere.

This is a textbook CG deficiency opening: (i) the object is named by what it lacks (one generator, no simple pole), (ii) the falsification stake is declared in sentence three, (iii) the OPE is displayed as the hinge object before any theorem is named. It is the rhetorical register prescribed by the Writing Standard (Gelfand inevitability + Beilinson falsification + Drinfeld unifying principle).

## Attack surface

### CG north-star criteria

- **Deficiency opening.** Present. The first paragraph locates $\mathcal{H}_k$ as the smallest chiral algebra: one generator, one relation, double pole only. Explicitly: "If bar-cobar duality fails for this OPE, it fails everywhere." The Arnold relation is derived (not asserted) at three collisions before any theorem label is invoked.
- **Unique survivor.** Present. "The simplicity is not a weakness; it is the diagnostic" (line 70). The Heisenberg is the unique shadow class G with $S_4 = 0$, $\Delta = 0$, tower terminating at degree 2.
- **Forced transition.** Each paragraph forces the next: OPE → Arnold → $d^2=0$ → bar complex → Verdier → Koszul dual → curvature $m_0 = -k\omega$ → MC element → genus expansion → complementarity → decomposition table (lines 154-205). No decorative sentences.
- **Decomposition table.** The itemised escalation list (Heisenberg → free fields → affine KM → W-algebras → lattice → Yangian) is the canonical CG decomposition move: each entry isolates exactly one new source of complexity.
- **Dichotomy.** Even/odd generator dichotomy inscribed at lines 3195-3238 (abelian CS boundary is Heisenberg; odd current is symplectic-fermion contrast, pure-bracket bar differential vs pure-curvature Heisenberg).
- **Russian-school voice.** Sustained. Etingof-precision on the OPE convention ($k/(z-w)^2$ with level prefix always visible), Kazhdan-compression (the "One generator. One relation." triple), Drinfeld unifying principle (the categorical logarithm identification at line 119), Kapranov higher structure (MC element as protagonist, line 83).
- **Physics-as-theorem (RS-3).** Satisfied. Abelian $U(1)$ Chern–Simons boundary is identified WITH the Heisenberg (line 3211-3221), not as a "bridge" or "analogy". Section `sec:cs-hinge-heisenberg` (line 3240ff) explicitly routes the bulk-boundary reconstruction as a theorem, not a picture.

### AP compliance grep sweep

All zero findings:

- **AP105** (Heisenberg OPE $k/(z-w)^2$). Verified at lines 5, 228, 1281, 1680, 1884, 1954, 3214, 3381, 4842, 4895. Level prefix $k$ always present. Abelian-KM-level-$k$ identification explicit at line 3218 (Beilinson–Drinfeld's Heisenberg Lie$^*$).
- **AP106** (no "This chapter constructs..." opener). Grep returns zero.
- **AP107** (r-matrix convention). $r^{\mathrm{Heis}}(z) = k/z$ used uniformly (trace-form, $k=0$ verified to vanish at line 108 and line 2143). No collision-vs-Laplace confusion because the Heisenberg generator is EVEN; the bar coefficient and the Laplace r-matrix coincide. The odd-generator asymmetry is handled in the contrast remark (lines 3195-3202).
- **AP108** (CG opening, not $\Eone$ atom). Explicit inline comment at line 3208-3210: "The Heisenberg is the CG opening, not the atom of $E_1$ structure; the genuine $E_1$ atom is the Yangian." Reinforced at line 3234-3237.
- **AP109** (no results-before-proof). The six-theorem remark (`rem:frame-governing-picture`, lines 207-216) appears AFTER the Arnold/$d^2=0$/MC/genus-tower computations in the opening ten paragraphs, and routes every clause through a section reference (`\S\ref{sec:frame-...}`) rather than asserting proofs.
- **AP110** (own-volume story). The Overture tells Vol I's story; cross-volume references stay in delineated subsections (the `thqg_introduction_supplement` include at line 4918).
- **AP111** (no "What this chapter proves"). Grep returns zero.

### Prose hygiene grep

All zero findings:

- AI-slop tokens (moreover, crucially, notably, remarkably, furthermore, interestingly, delve, leverage, tapestry, cornerstone, journey, navigate): 0 hits.
- Em-dash `---`: 0 hits.
- Unicode U+2014 em-dash: 0 hits (verified via Python codepoint scan).
- Manuscript-metadata leakage (`AP[0-9]+`, `HZ-[0-9]+`, `Pattern [0-9]+`, `Cache #`, `V[0-9]-AP`, `AP-CY`, `first_principles_cache`): 0 hits in typeset text. All operational tags live in `%` LaTeX comments (lines 45, 105-106, 3207-3210), which is the sanctioned scaffolding location per the Manuscript Metadata Hygiene constitutional rule.

### Potential defects considered and dismissed

1. **Chapter title "The Gaussian Archetype"** (line 1). Not "Overture" literally, but the `\part*{Overture}` wrapper in `main.tex:1014` makes the part-name "Overture" and the chapter-name "Gaussian Archetype"; "Gaussian archetype" is a CG-style substance-name, not a generic heading. ACCEPT.
2. **The six-theorem remark** (lines 207-216). On a strict reading of AP109 ("NEVER list results before proving") this could look like result-listing. Reading the remark in context: it is preceded by three paragraphs of direct computation (Arnold, $d^2=0$, $\kappa = k$, $\hat{A}$-series) that each instantiate a theorem, and every clause of the remark cites a downstream section. The list serves the decomposition-table CG move (naming which theorems are already visible in the Gaussian shadow). ACCEPT.
3. **"Every construction in this monograph is already present..."** (line 13). A strong claim; ACCEPT because the rest of the Overture delivers on it (explicit collapse of each general structure to the scalar $\kappa=k$: lines 88-102 for the five-component differential, 104-115 for the $r$-matrix, 117-148 for the categorical-logarithm identification).

## Heal

No prose edits required. The Overture is in published CG register with zero AP violations.

## Coverage statement

Chunk reads: lines 1-250 (opening, intensive), line 3195-3274 (CS hinge section, AP105/AP108 checkpoint), 4850-4918 (closing, Hochschild verification). Full-file greps over 4918 lines for all compliance classes above, zero-hits on every forbidden pattern. The Overture is CONVERGED.

## Companion observations for downstream authors

- The identification "Heisenberg = abelian KM at level $k$ = abelian CS boundary" (AP105) is cited THREE times (lines 11, 3218-3221, 3411) with consistent OPE and consistent Beilinson–Drinfeld Lie$^*$ language. This is the correct redundancy profile for a constitutional identification.
- The `sec:cs-hinge-heisenberg` section (from line 3240) is the load-bearing location for Vol II's 3d HT holography import. It should be treated as invariant under future edits; any Vol II cross-volume update must preserve its exact CS-to-Heisenberg dictionary.

## Verdict

ACCEPT. The Overture meets the CG north-star criteria (deficiency opening, unique survivor, forced transition, decomposition table, dichotomy) and passes every AP105–AP111, HZ-10, constitutional-metadata, and em-dash grep cleanly. No surgical edits are required; the file is published-standard and serves as the rhetorical benchmark for downstream chapters.
