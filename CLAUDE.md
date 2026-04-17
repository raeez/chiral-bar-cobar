# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## /chriss-ginzburg-rectify: READ THE WHOLE FILE, CHUNK BY CHUNK, LINEARLY (TOP-LEVEL INJUNCTION)

When the user invokes `/chriss-ginzburg-rectify` (or the skill `chriss-ginzburg-rectify`) on a target file, Phase 1 (Global Diagnostic) is NOT OPTIONAL and is NOT ABBREVIATED. You must analyse the **whole file**, **chunk by chunk**, **linearly progressing from start to finish**, with **small chunk size**. Every line must pass under your eyes.

**Binding rules**:
- The skill's wording "For files >3000 lines: sample strategically" is OVERRIDDEN. Do NOT sample. Do NOT jump. Do NOT read section heads via Grep and call it Phase 1. Do NOT read only opening + closing + dense midsection.
- **Chunk size: ~250-500 lines per Read call, at most**. Large chunks (1000+ lines) that approach the 25000-token Read cap are forbidden: they compress context and invite skimming. Prefer many small Reads to few large ones.
- **Linear progression**: start at line 1. Each subsequent Read starts exactly where the previous one ended (offset = prev_offset + prev_limit). No ranges are skipped; no ranges are revisited unless a Phase 3 edit requires re-reading a specific chunk.
- **Coverage is a proof obligation**. Before leaving Phase 1, verify: the sum of (limit) across all Phase 1 Reads equals the file line count, and the starting offsets form a contiguous cover of [1, EOF]. If you cannot state this, Phase 1 is incomplete.
- Grep does NOT substitute for Phase 1 reading. Grep is Phase 3 cross-file propagation (AP5), not the global diagnostic.
- If a Read fails with the 25000-token cap, cut the `limit` in half and retry. Never "skip ahead past the oversized region."

This injunction applies to EVERY invocation of `/chriss-ginzburg-rectify`, on files of any size. A 5000-line chapter takes ~10-20 small Reads. That is the cost; it is not negotiable.

## Today's Reconstitution Headlines (2026-04-16, Wave 14)

Load the file behind any headline you intend to extend. Each is a self-contained reconstitution draft, not yet inscribed into the .tex; treat as Platonic-ideal source for next-pass scribing.

- `adversarial_swarm_20260416/wave14_reconstitute_theoremA.md` — Koszul Reflection Theorem as Platonic Theorem A.
- `adversarial_swarm_20260416/wave14_reconstitute_kappa_conductor.md` — universal ghost-charge K formula.
- `adversarial_swarm_20260416/wave14_reconstitute_climax_theorem.md` — d_bar = KZ^*(∇_Arnold) and κ = −c_ghost(BRST).
- `adversarial_swarm_20260416/wave14_reconstitute_shadow_tower.md` — Quadrichotomy + spectral-curve Picard-Fuchs.
- `adversarial_swarm_20260416/wave14_brst_ghost_identity_chapter_draft.md` — chapter-quality draft, ready for `chiral_chern_weil_brst_conductor.tex`.
- `adversarial_swarm_20260416/wave_supervisory_mc5_theorem.md` — MC5 theorem draft.
- `adversarial_swarm_20260416/wave_supervisory_q_convention_bridge.md` — q_KL² = q_DK as KZ cocycle.
- `adversarial_swarm_20260416/wave_supervisory_S5_wick_implementation.md` — S_5 = −48/(c²(5c+22)) verified independently; coverage 0/2275 → 1/2275.
- `adversarial_swarm_20260416/wave14_reconstitute_phi_functor_volIII.md` — Vol III Φ Platonic + universal trace identity unifying Vol I K = −c_ghost with Vol III κ_BKM = c_N(0)/2.

## Reference files (load on demand)

- `notes/cross_volume_aps.md` — Vol II V2-AP1-39 + Vol III AP-CY1-67 (AP-CY62..67 added 2026-04-16). Read before any cross-volume edit.
- `notes/true_formula_census.md` — Full C1-C31 census (externalized 2026-04-16). The top-5 most-violated stay inline below.
- `notes/first_principles_cache_comprehensive.md` — 210+ confusion-pattern registry with regex triggers. Append new patterns there per the first-principles protocol.
- `chapters/examples/landscape_census.tex` — Canonical kappa / r(z) / central charges per family. AP1 MANDATES reading this file (not memory) before any formula.

# Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,700pp, 139,568 tests, 3,726 engines). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,749pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~693pp, ~34,000 tests, ~460 engines). Total ~5,142pp, ~177K tests, ~4,186 engines, 3,500+ tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

**Architecture (2026-04-13):** E_n chiral algebra theory stays in Vol I (algebraic-geometric objects on curves and configuration spaces: factorisation algebras, FM compactifications, Mok's logarithmic spaces, bar complexes at all E_n levels, derived chiral centres -- inherently geometric, never "pure algebra"). Derived centres are constructed and their E_n properties proved in Vol I; Vol II interprets them physically as 3d HT gauge theories. Vol III constructs concrete CY quantum groups as examples of Vol I's abstract E_1-chiral quantum groups, via 6d hCS, 4d/5d HT CS, little string theory, M5 branes.

**North star:** platonic_ideal_reconstituted_2026_04_13.md is THE SINGLE REFERENCE for all structural questions. (Supersedes the 2026-04-12 version.)

## HOT ZONE -- Top 10 Repeat Offenders

Read this section BEFORE any Edit. These are the APs that fire repeatedly across waves despite being catalogued. Each entry is an operational template, not prose. Source: ap_recurrence_archaeology_wave12.md. If you only read 80 lines of CLAUDE.md, read these.

Full AP catalog: see sections below. This HOT ZONE covers ~80% of real-world violation patterns.

### HZ-1. AP126/AP141 (r-matrix level prefix) -- 6 waves, 90+ instances

Template, fill BEFORE writing any r-matrix:

```
family:               [Heis / affine KM / Vir / W_N / Yang rational / Calogero-Moser]
r(z) written:         [formula with level prefix visible]
level parameter:      [k / k+h^v / hbar / c]
AP141 k=0 check:      r(z)|_{level=0} = [value]    required: 0 (trace-form convention)
match?                [Y/N]   <-- must be Y for trace-form; for KZ convention, k=0 gives Omega/(h^v*z) != 0 for non-abelian g (correct: Lie bracket persists)
source:               landscape_census.tex line [N] OR compute engine
FORBIDDEN bare forms: Omega/z (no level), k Omega/z^2
```

Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.

### HZ-2. AP40 (environment matches tag) -- 5 waves, 70+ instances

Decision tree, answer BEFORE writing `\begin{...}`:

```
Q1: Is there a complete proof here or in cited literature?
    NO  -> \begin{conjecture} + \ClaimStatusConjectured. STOP.
    YES -> Q2
Q2: Backbone main result / supporting / auxiliary?
    main       -> \begin{theorem}
    supporting -> \begin{proposition}
    auxiliary  -> \begin{lemma}
Q3: Self-contained or cited?
    self-contained -> \ClaimStatusProvedHere + \begin{proof}
    cited          -> \ClaimStatusProvedElsewhere + Remark[Attribution]
UNCERTAIN -> default \begin{conjecture}. Downgrade is cheaper than rename.
```

Vol III default: `\begin{conjecture}` regardless. Label prefix follows environment (AP125).

### HZ-3. AP32 (uniform-weight tag on F_g) -- 4 waves, 30+ instances

Every formula of the form `F_g = ... lambda_g ...` or `obs_g = ...` MUST be followed within the same sentence by ONE of:

```
(a) (UNIFORM-WEIGHT)
(b) (ALL-WEIGHT, with cross-channel correction delta F_g^cross)
(c) (g=1 only; ALL-WEIGHT at g=1 is unconditional)
(d) (LOCAL: scope defined in surrounding paragraph, see ref:...)
```

No "in a theorem" loophole: tag required in prose, remarks, and definitions.

### HZ-4. AP1 (kappa from memory) -- 4 waves, 15+ instances

Writing kappa from memory is FORBIDDEN. Before writing ANY kappa expression:

```
Step 1: Identify family (Heis / Vir / KM / W_N / free / coset / SVir / BP / betagamma)
Step 2: Open landscape_census.tex, copy the formula WITH citation comment
Step 3: Paste with comment: % AP1: formula from landscape_census.tex:LINE; k=0 -> VALUE verified
Step 4: Evaluate at two boundary values and write results in comment
```

Quick reference (cross-check census before use):
- KM: `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`; k=0 -> dim(g)/2; k=-h^v -> 0 (critical)
- Vir: `kappa(Vir_c) = c/2`; c=13 -> 13/2 (self-dual)
- Heis: `kappa(H_k) = k`; k=0 -> 0
- W_N: `kappa(W_N) = c*(H_N - 1)` where `H_N = 1 + 1/2 + ... + 1/N`. NOT `H_{N-1}`. Verify at N=2: H_2=3/2, H_2-1=1/2, so kappa(W_2)=c/2 matches Virasoro.

### HZ-5. AP125/AP124 (label prefix and uniqueness) -- 3 waves, 25+ instances

Before writing `\label{foo}`:

```
(i)  Prefix matches environment: thm: theorem, prop: proposition, lem: lemma,
     conj: conjecture, rem: remark, def: definition, eq: equation
(ii) Uniqueness across all three volumes:
     grep -rn '\\label{foo}' ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups
     0 matches -> safe. >=1 match -> rename with volume suffix (v1-, v2-, v3-).
```

Downgrade atomicity: when downgrading theorem -> conjecture, rename `thm:foo -> conj:foo` AND update every `\ref{thm:foo}` across three volumes in the SAME tool-call batch. No intermediate commit.

### HZ-6. AP10/AP128 (hardcoded expected values) -- 3 waves, 12+ engines

Every hardcoded expected value in a test file requires a `# VERIFIED` comment citing at least TWO sources from different categories:

```
[DC] direct computation     [LT] literature (paper + eq #)
[LC] limiting case          [SY] symmetry
[CF] cross-family           [NE] numerical (>=10 digits)
[DA] dimensional analysis
```

Engine-test sync check: when correcting an engine formula, derive the new expected value from an INDEPENDENT source, NOT from the corrected engine output. Then update both. The engine and test sharing the same wrong mental model is the most dangerous AP10 variant.

### HZ-7. AP113 (bare kappa in Vol III) -- 3 waves, 165 baseline instances

Bare `\kappa` in Vol III is permitted IFF the section begins with a local definition:

```
"In this section we write kappa for kappa_{ch}(H_Lambda) (respectively kappa_{BKM}, kappa_{cat}, kappa_{fiber})."
```

Approved subscripts (closed set): `{ch, cat, BKM, fiber}`. FORBIDDEN: `{global, BPS, eff, total, naive}`.

Decision tree:
- chiral algebra -> `kappa_ch`
- BKM algebra -> `kappa_BKM`
- Euler characteristic -> `kappa_cat`
- lattice/fiber -> `kappa_fiber`

### HZ-8. AP4 (proof after conjecture) -- 3 waves, 40+ instances

Before `\begin{proof}`:

```
Step 1: Look at the nearest preceding \begin{...} within 30 lines
Step 2: theorem/prop/lemma -> proof may follow
        conjecture/heuristic/remark/definition -> STOP, use \begin{remark}[Evidence]
Step 3: ClaimStatus tag check
        ProvedHere -> self-contained proof body
        ProvedElsewhere -> paragraph attributing, NOT re-proof
        Conjectured -> AP40 upstream violation
```

### HZ-9. AP25/AP34/AP50 (four-functor discipline) -- 3 waves, 15+ instances

Write this list before any paragraph mentioning "bar", "cobar", "Koszul dual", or "derived center":

```
% FOUR OBJECTS:
% 1. B(A) = bar coalgebra = T^c(s^{-1} A-bar) with deconcatenation + twist
% 2. A^i = H^*(B(A)) = dual coalgebra (Koszul cohomology of bar)
% 3. A^! = ((A^i)^v) = dual ALGEBRA (linear or Verdier dual)
% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk
```

FORBIDDEN conflations:
- "bar-cobar produces bulk" (wrong: bar-cobar inverts to A; bulk is Hochschild)
- "Omega(B(A)) is the Koszul dual" (wrong: that is INVERSION)
- "the Koszul dual equals the bar complex" (wrong: bar is coalgebra, dual is algebra)
- "D_Ran(B(A)) is the cobar complex" (wrong: D_Ran is Verdier; cobar is Omega)

### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances over 3 zero-tolerance commits

PRE-WRITE mental check: does the sentence start with one of the banned tokens below? If yes, REWRITE before typing.

POST-WRITE grep (mandatory):

```
Banned (case-insensitive): moreover, additionally, notably, crucially, remarkably,
interestingly, furthermore, "we now", "it is worth noting", "worth mentioning",
"it should be noted", "it is important to note", delve, leverage, tapestry,
cornerstone, landscape (as metaphor), journey, navigate (non-geometric)

Em-dash (---, U+2014) FORBIDDEN. Use colons, semicolons, separate sentences.

Hedging ban in math: arguably, perhaps, seems to, appears to. If math clear, state it. If not, mark as conjecture.
```

Three separate cleanup commits in Vol II prove aspirational instructions insufficient. Post-write grep is the only reliable enforcement.

### HZ-IV. Independent Verification Protocol (cross-volume, 2026-04-16)

**Canonical (verbatim) location:** Vol III CLAUDE.md §HZ3-11 ("Independent Verification Protocol", lines 287-385). The protocol is STANDALONE there with the same machinery, decorator API, enforcement targets (`make verify-independence`), three-healings menu, and file inventory. Identical code lives at `compute/lib/independent_verification.py`, `compute/scripts/audit_independent_verification.py`, `compute/tests/test_independent_verification_infra.py`, `notes/INDEPENDENT_VERIFICATION.md`.

**Operational summary (sufficient without loading Vol III):** every `\ClaimStatusProvedHere` test must declare `derived_from`, `verified_against`, `disjoint_rationale`. Disjointness checked at import time. Three healings when honest decoration fails: (1) find a disjoint source; (2) restrict scope (`\begin{proposition}` for partial); (3) downgrade to `\ClaimStatusConjectured`. Coverage snapshot at installation (2026-04-16): Vol I 0/2275, Vol II 0/1134, Vol III 2/283. The gap closes only through GENUINE verification or explicit status downgrade, never tautological decoration. Vol I working queue: to be seeded as adversarial audits identify candidates (Vol III seed in `notes/tautology_registry.md`).

## The Beilinson Principle

"What limits forward progress is not the lack of genius but the inability to dismiss false ideas." Every claim is false until independently verified from primary source. Prefer a smaller true theorem to a larger false one. Every numerical claim requires 3+ genuinely independent verification paths (direct computation, alternative formula, limiting case, symmetry/duality, cross-family, literature+convention, dimensional analysis, numerical evaluation).

**Epistemic hierarchy** (higher wins): (1) Direct computation > (2) .tex source +/-100 lines > (3) Build system > (4) Published literature > (5) concordance.tex > (6) This file > (7) Memory. Before every assertion: "How do I know this? Read the source, computed it, or assumed it?" If assumed, stop and verify.

## Manuscript Metadata Hygiene (CONSTITUTIONAL, ZERO TOLERANCE)

**The anti-pattern catalogue, the confusion-pattern cache, and all metacognitive accounting stay out of the manuscript and out of the standalone papers.** They live only in `CLAUDE.md`, `notes/first_principles_cache_comprehensive.md`, `MEMORY.md`, `notes/`, and the `memory/` directory. The manuscript and standalones are the mathematics; the metacognitive architecture is scaffolding that the reader must never see.

**FORBIDDEN tokens in any typeset line** of `chapters/**/*.tex`, `standalone/**/*.tex`, `main.tex` (outside `%` comments), or any `.tex` file that compiles into the monograph or a standalone paper:

- `AP\d+` (e.g. `AP1`, `AP113`, `AP234`), including in prose, remark/theorem titles, and section headers.
- `V\d-AP\d+` (e.g. `V2-AP39`), `AP-CY\d+`, `FM\d+`, `B\d+` when used as blacklist identifiers.
- `HZ-\d+`, `HZ-[IVX]+` (e.g. `HZ-4`, `HZ-IV`): CLAUDE.md HOT ZONE labels.
- `Pattern \d+`, `Cache #\d+`: first-principles-cache entry identifiers.
- `first_principles_cache` or `first principles cache` referenced by name in typeset prose.
- "cache entry", "anti-pattern catalogue", "catalogue of anti-patterns", "the AP catalogue", or any variant, in typeset prose.
- Titles of the form `\section{Universal APxxx healing}`, `\begin{remark}[..., AP\d+]`, `\label{...-ap\d+}`.
- Commit-message style metadata in the manuscript: `RECTIFICATION-FLAG`, "(per AP...)", "(per cache...)".

**ALLOWED:**

- LaTeX comments starting with `%` (invisible in the PDF). `% AP126 check: k=0 gives r=0.` is fine as scaffolding.
- References in `CLAUDE.md`, `MEMORY.md`, `notes/first_principles_cache_comprehensive.md`, `notes/`, `memory/`, `adversarial_swarm_*/`, `compute/` Python files, test files.
- Referring to a mathematical pattern by its mathematical content (e.g. "level-prefix convention", "trace-form r-matrix at k=0", "family-dependent anomaly ratio"). Rename and describe in substance, not by catalogue index.

**Healing protocol** when an AP reference is found in typeset prose:

1. If it is a parenthetical tag (`, AP1 / AP39` in a remark title; `(AP77)` in prose): remove the tag entirely; the mathematical substance of the surrounding paragraph already conveys the point.
2. If it is a section header (`\section{Universal AP126 healing}`): rename to describe the mathematics (`\section{Universal level-prefix healing}` or similar). Update `\ref{sec:...}` targets if the label also carries the AP index.
3. If it is a load-bearing prose sentence (`By AP77, the series is Pade-summable`): rephrase to state the mathematical content (`The series is convergent and therefore Pade-summable rather than Borel-summable`).
4. If it is a label (`\label{rem:foo-ap42}`): rename to `\label{rem:foo}` and grep the whole Vol for `\ref{rem:foo-ap42}` to update. Labels stay unique (AP124/125 discipline).

**Enforcement.** Before every commit whose diff touches `.tex` files under `chapters/`, `standalone/`, or the abstract of `main.tex`:

```bash
# Vol I:
grep -rn '\bAP[0-9]\+\b\|\bHZ-[0-9IVX]\+\b\|V[0-9]-AP[0-9]\+\|AP-CY[0-9]\+\|\bPattern [0-9]\+\b\|Cache #[0-9]\+\|first_principles_cache' \
  /Users/raeez/chiral-bar-cobar/chapters/ \
  /Users/raeez/chiral-bar-cobar/standalone/ \
  2>/dev/null | grep -v ':[0-9]*:\s*%'
# Vol II: same under /Users/raeez/chiral-bar-cobar-vol2/
# Vol III: same under /Users/raeez/calabi-yau-quantum-groups/
```

Zero hits is the commit-gate. If any hit appears: stop, heal via the protocol above, re-grep until zero.

**Cross-volume.** The rule applies identically to all four volumes. The two anti-patterns catalogued in this session (AP234: K-notation collision; AP235: quaternitomy/quadrichotomy drift) and the two cache entries (Pattern 218, Pattern 219) are registered in `CLAUDE.md` and `notes/first_principles_cache_comprehensive.md` only; the Vol~I preface, introduction, and main-abstract edits that resolved them contain the mathematical substance of the healing without any catalogue label.

**Why.** The manuscript is the object of study for the reader; the catalogue is the author's working notebook. A reader who opens the PDF and encounters `(AP225)` in a theorem statement sees scaffolding, not mathematics. Catalogue indices also rot: they renumber, reorganise, and get retired; prose coupled to them breaks. Every AP-labelled sentence must be rewritten to stand on its mathematical content alone.

## E1-First Prose Architecture (MANDATORY)

The ordered bar B^ord(A) is the primitive object of this programme. Every chapter, every section, every theorem presentation MUST construct the E1 ordered story first, then derive the symmetric story by averaging. The pattern:

1. CONSTRUCT the E1 object (B^ord, r(z), Theta_A in g^{E1}, the matrix-valued curvature).
2. EXHIBIT the E1 structure (deconcatenation coproduct, R-matrix, Yangian).
3. APPLY the averaging map av: g^{E1} -> g^mod (lossy Sigma_n-coinvariant projection).
4. DERIVE the symmetric result (kappa from av(r(z)); for non-abelian affine KM, av(r(z)) + dim(g)/2 = kappa; obs_g = kappa*lambda_g, the shadow tower).

NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" — they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.

The convolution algebra has two levels: g^{E1}_A (the primitive, carrying the R-matrix) and g^mod_A (the coinvariant shadow, carrying only kappa). Theta_A lives in g^{E1}_A; everything in this monograph is its Sigma_n-coinvariant projection.

## The Five Objects (NEVER CONFLATE)

A (algebra) -- B(A) (bar coalgebra) -- A^i=H*(B(A)) (dual coalgebra) -- A^!=((A^i)^v) (dual algebra) -- Z^der_ch(A) (derived center = bulk). Omega(B(A))=A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.

## Key Constants

kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(Heis)=k. kappa(W_N)=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j. Vir^!=Vir_{26-c}. Self-dual at c=13. kappa+kappa'=0 (KM/free), 13 (Vir). QME: hbar*Delta*S+(1/2){S,S}=0. sl_2 bar H^2=5 (not 6). Desuspension: |s^{-1}v|=|v|-1, NOT +1. eta(q)=q^{1/24}*prod(1-q^n). Bar propagator d log E(z,w): ALWAYS weight 1. Prime form: section of K^{-1/2} boxtimes K^{-1/2}. FM_n(X): blowup along diagonals, NOT complement. Grading: COHOMOLOGICAL (|d|=+1). Curved A-inf: m_1^2(a)=[m_0,a]. Bar d^2=0 always; curvature appears as m_1^2 != 0.
alpha_g = 2*rank + 4*dim*h^v (universal Hilbert-series growth, all simple types). d_alg in {0,1,2,inf} (depth gap: 3 impossible, prop:depth-gap-trichotomy). kappa(BP)+kappa(BP^!)=98/3 (self-dual k=-3).
C_A := limsup |A_{r+1}/A_r| = 6 uniformly on non-logarithmic class M T-line with Virasoro subalgebra (thm:shadow-exponential-base-Virasoro + thm:universal-class-M-C-is-6). Closed form: Sigma_Vir(z) = 4z^3/9 - z^2/9 + z/27 - log(1+6z)/162. Pole-doubling all k: Sigma_Vir^{(k)}(z) = [P_k + Q_k*log(1+6z)]/(1+6z)^{2k}. Decomposition: 6 = r_0 * S_{r_0} = 3 * 2. Cross-volume bridge: beta_A (Vol II tempering rate) equals C_A at leading 1/c. W_3 W-LINE SECOND LANE (thm:w3-wline-closed-form + thm:w3-wline-exponential-base, iter 58): a_n = 2*3^{n-2}*(2n-4)!/[(n-2)!*n!] = 2*3^{n-2}*C(2n-4,n-2)/[n(n-1)]; a_{n+1}/a_n = 6(2n-3)/(n+1) = 12 - 30/(n+1); C_{W_3}^{W-line} = 12 = 2*6 (doubling from Hessian ratio 3/2 * kernel ratio 4/3). Stirling: a_n ~ 12^n/(72*sqrt(pi)*n^{5/2}). Koszul-dual invariant under c->4-c (K_3=4). Conjectural spin-stratified lattice: C_{W^{(s)}} = s(s+1) for each primary in principal W_N (s=2: 6; s=3: 12; s=4: 20).

## True Formula Census (top 5 kept inline)

Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Full C1-C31 reference: `notes/true_formula_census.md`.

**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).

**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one); c*H_N - 1 (parenthesization); (c/2)*H_N.

**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)`. Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit); k=-h^v -> critical. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges. Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp; full kappa = av(r) + dim(g)/2 (Sugawara shift). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).

**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).

**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).

## Wrong Formulas Blacklist

Concrete forbidden forms repeatedly emitted. Grep after every .tex write; match = fix immediately. Format: `BAD → CORRECT. [ref]`.

r-matrix / level prefix:
- B1. `r(z)=\Omega/z` (bare) → trace-form `k\Omega/z` or KZ `\Omega/((k+h^\vee)z)`. AP126. Regex: `r\(z\)\s*=\s*\\Omega\s*/\s*z`.
- B2. `r^Vir(z)=(c/2)/z^4` → `(c/2)/z^3 + 2T/z`. AP19/AP21.
- B3. `r^Vir(z)=(c/2)/z^2` → cubic + simple. AP19/AP27.
- B4. `\Omega\,d\log z` (no k) → `k\Omega\,d\log z`. AP117/AP126.

central charges / kappa:
- B5. `c_{bc}=2(6λ²-6λ+1)` (bosonic form on fermionic label) → `c_{bc}=1-3(2λ-1)²`. AP137.
- B6. `c_{βγ}=1-3(2λ-1)²` → `c_{bg}=2(6λ²-6λ+1)`. AP137.
- B7. `κ(W_N)=c*H_{N-1}` → `c*(H_N-1)`. AP136.
- B8. `κ=c/2` unqualified → specify family; c/2 is Vir ONLY. AP1/AP39.
- B9. `κ+κ'=0` unscoped → 0 (KM/free), 13 (Vir), family-specific otherwise. AP24/AP8.
- B10. `κ=S_2/2` → `S_2=κ` (no factor 2). Only Vir has κ=c/2. AP39.
- B11. `av(r(z))=κ` for non-abelian KM → `av(r(z))+dim(g)/2=κ(V_k(g))`. FM11.
- B12. Bare `\kappa` in Vol III → subscripted `\kappa_{ch|cat|BKM|fiber}`. AP113.
- B13. `\kappa_{global|BPS|eff|total|naive}` → approved set only. AP113.

bar complex / suspension:
- B14. `T^c(s^{-1} A)` → `T^c(s^{-1} \bar A)`. AP132.
- B15/B16. `T^c(s A)` or `|s^{-1}v|=|v|+1`. See AP-DESUSP.
- B17. eta as bare `prod(1-q^n)` → `\eta(q)=q^{1/24}*prod(1-q^n)`. FM13.

boundaries / combinatorics:
- B18. W_N weights `{2,...,N+1}` → `{2,...,N}`.
- B19. `H_N=sum_{j=1}^{N-1} 1/j` → upper limit N. AP116.
- B20. `C_n` as binary trees with n leaves → n+1 leaves (n internal nodes). AP133.

numerical:
- B21. E_8 fund=779247 → not any E_8 irreducible. FM5.
- B22. `dim H^2(B(sl_2))=6` → 5.
- B23. Genus-2 stable graphs=6 → 7. AP123.
- B24. `1/\eta(q)^2` coeffs (1,3,6,10,...) → (1,2,5,10,20,...) bicoloured. AP135.
- B25. `K_{BP}=2` → 196. AP140.

scope / quantifier:
- B26. `obs_g=κ*λ_g` untagged → append scope tag. See AP-UNIFORM-WEIGHT-TAG.
- B27. `A ⇔ B` when only forward proved → `\implies` + Remark. AP36.
- B28. "k=0 r-matrix vanishes → algebra fails Koszulness" (KM) → k=0 abelian, still Koszul; k=-h^v critical. FM4.
- B29. Free variable n on RHS but only g on LHS (Thm C^{E1}) → quantify n with `2g-2+n > 0`. AP139.

macros / labels / LaTeX:
- B30. `\end{definition>` (`>` instead of `}`). Regex: `\\end\{[^}]*>`. FM7.
- B31. `\begin{theorem>`. Symmetric.
- B32. `\cW` in standalone without `\providecommand`. FM6.
- B33. `Part~IV`, `Chapter~12` hardcoded → `\ref{part:...}`. V2-AP26/FM10.
- B34/B35. See AP-LABEL-DISCIPLINE.
- B36. `\cite{GeK98}` without bibitem → emits [?]. AP28.

numerical coefficients:
- B37. `F_2=1/5760` or `7/2880` → `7/5760`. FM21.
- B38. `\frac{1}{2\pi}\oint` (missing i) → `\frac{1}{2\pi i}\oint`. AP120.
- B39. KM r-matrix not vanishing at k=0. See AP-RMATRIX.

prose hygiene:
- B40. Markdown in LaTeX (`\`num\``, **bold**, _italic_) → `$...$`, `\textbf`, `\emph`. AP121.
- B41. Em-dash (`---` / U+2014) → colon, semicolon, separate sentences.
- B42. AI slop: `notably, crucially, remarkably, interestingly, furthermore, moreover, delve, leverage, tapestry, cornerstone`.

depth / dimension / fiber-base:
- B43. `d_alg(Vir)=3` → `d_gen(Vir)=3, d_alg(Vir)=inf` (class M). AP131/FM18.
- B44. Bare `d(Vir)=3` without `gen`/`alg` subscript. AP131.
- B45. `vdim ChirHoch^*(A)=2` → amplitude [0,2], NOT vdim. AP134/FM17.
- B46. `\omega_g=d\tau` → `\omega_g=c_1(\lambda)` on M̄_g; d\tau lives on curve. AP130/FM19.

grading / curved:
- B47. `[m,[m,f]]=(1/2)[[m,m],f]` at even `||m||` → tautological at even; identity needs odd. AP138.
- B48. `m_1^2=0` universally in curved A-inf → `m_1^2(a)=[m_0,a]`. AP46.
- B49. `d^2=kappa*omega_g` as bar differential → `d^2_bar=0` always; `d^2_fib=kappa*omega_g` is FIBERWISE at g>=1. AP46/AP87.

promotion / sector:
- B50. `dim SC^mix_{k,m}=(k-1)!*m!` → `(k-1)!*C(k+m,m)`. AP89.
- B51. `B_{SC}(A)` one-colour → SC two-coloured, use promotion A→(A,A). AP86.
- B52. `kappa(BP)+kappa(BP^!)=1/3` → `98/3`. AP140/C31.
- B53. "Koszul duality over a point = over P^1". FALSE. AP142. Regex: `over a point.*is.*over.*P\^1|over a point.*is.*over.*\\mathbb\{P\}`.
- B54/B55/B56. B(A) as SC-coalgebra / "bar differential = closed color" / "curved SC^{ch,top}-algebra". See AP-SC-BAR. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`.
- B57. `(SC^{ch,top})^! ~ SC^{ch,top}`. See AP-SC-NOT-SELFDUAL.
- B58/B59. Chiral label on topologized derived center / "Topologization for all". See AP-TOPOLOGIZATION.
- B60. "A^! is SC-algebra" → A^! is SC^!-algebra = (Lie, Ass). AP172.
- B61. "Chiral QG equiv for all four families" → proved abstractly on Koszul locus; verified for sl_2 Yangian + affine KM. AP174.
- B62. `Δ_z(T) = T⊗1 + 1⊗T + (1/Ψ)(J⊗J)` → `(Ψ-1)/Ψ`. AP128/FM31. Regex: `1/\\Psi.*J\s*\\otimes\s*J` without `Psi\s*-\s*1`.
- B63. `nabla=d+A` with `dPhi=+A*Phi` INCONSISTENT → `nabla=d-A` gives `dPhi=+A*Phi`. Regex: `\\nabla\s*=\s*d\s*\+\s*` with flat section `dPhi = +A*Phi`.

(B64-B67 RETRACTED; B68 merged into AP177.)

- B68. "S_2=c/12, the Virasoro central charge itself" → S_2=c/2; central charge is c (not c/12). AP177.
- B69. `pi_3(BU)=Z` → `pi_3(BU)=0` (Bott periodicity). AP181.
- B70. `\kappa_{ch}=h^{1,1}` for local surfaces → `\kappa_{ch}=\chi(S)/2`. AP182.
- B71. McKay quiver of Z_3 = K_{3,3} → 3 oriented 3-cycles (directed). AP183.
- B72. "Excision at t gives B(A)⊗B(A)" → excision: B_L⊗_A B_R = B(A) (one copy over A); coproduct: B(A)→B(A)⊗B(A) (two copies plain). AP184.
- B73. "pi_4(BU)=Z provides native E_2 for CY_4" → pi_4(BU)=Z is obstruction GROUP, not guarantee. AP185.

Vol II 2026-04-12/13 cross-volume (B74-B85):
- B74. Cauchy on formal power series → FORMAL needs flatness+homotopy-invariance; Cauchy needs CONVERGENT.
- B75. Non-holomorphic maps (retraction ρ_t using |z|) on holomorphic-form complexes → introduces dz-bar; use algebraic de Rham / local system.
- B76. Chain-level decomp != cohomological decomp. Specify chain/cohomology/associated-graded.
- B77. Abstract machine theorem != input verification. Output well-defined IF input satisfies axioms; verifying input is a separate theorem.
- B78. "Proof sketch" + ClaimStatusProvedHere ambiguous → upgrade or re-tag.
- B79. Conjecture → theorem upgrade requires EXHAUSTIVE `\ref{conj:X}` sweep across all files + standalones. Grep all three volumes.
- B80. Two obstruction complexes for one obstruction → exactness in one does NOT imply exactness in another. Specify WHICH.
- B81. Level-by-level rationality != convergence. Gap is EIGENVALUE (λ_min(G_N)), not DETERMINANT bounds.
- B82. Cohomological compatibility != chain-level. DS-Hochschild all-degrees does NOT close global triangle for class M.
- B83. Stale classification lists ("stuck at X") → update when new theorems expand proved scope.
- B84. Khan-Zeng scope: 3d Poisson sigma model covers ALL freely-generated PVAs with conformal vector. Check gr_Li(A) first.
- B85. Orbifold route: Z/n-invariants preserves E_n structure.

Session 2026-04-17 corrections (B86-B92, Beilinson-rectified):
- B86. Super-Yangian complementarity κ(Y(sl(m|n))) + κ(Y(sl(n|m))^!) = 0 (Virasoro analogy) → CORRECT `= max(m, n)` at Sugawara-shifted dual level. Verified symbolically at small rank.
- B87. "Tempered stratum obstruction κ^(∞)_orig = 1/e" (dichotomy) → RETRACTED. Stirling factor dropped; correct limsup = 0 universally at generic c.
- B88. "First Kummer-irregular prime 691" (unqualified) → imprecise. 691 is BERNOULLI-LEADING first (B_12). SIZE-LEADING first Kummer-irregular is 37 (B_32). Always qualify.
- B89. "Six routes to G(K3×E) converge isomorphically" (CY-C naive) → FALSIFIED. Pentagon of five intertwiners; R_2 source branch; generator rank stratification.
- B90. "CY-C pentagon κ_ch stratification {3,12,24}" → CATEGORY ERROR. κ_ch = 0 route-independent (Hodge supertrace). The stratification is GENERATOR RANK ρ^{R_i}, orthogonal to κ_ch.
- B91. "C_2-cofiniteness ⟹ bounded Massey ⟹ tempered" (W(p)) → FAILS. Gurarie 1993 + Flohr 1996 logarithmic CFT amplitudes exhibit unbounded Massey despite finite-dim Zhu. W(p) tempering OPEN.
- B92. Primes 1423, 3067, 23, 43, 419 labelled Kummer-irregular → VERIFIED REGULAR at primary source. They still appear in S_r numerators as RICCATI-ARITHMETIC characteristic primes, NOT Kummer-arithmetic.
- B93. `κ(A)+κ(A^!)=K(A)` (bare) → `κ(A)+κ(A^!)=ϱ_A·K(A)`. Two K's with same letter: Trinity K=c+c^!=-c_ghost(BRST) gives {-k, 2dim(g), 26, 100, 196}; scalar complementarity κ+κ^! gives {0, 13, 250/3, 98/3}. Relation: κ+κ^!=ϱ_A·K with ϱ_N=H_N-1 (principal W_N), ϱ_KM=ϱ_free=0, ϱ_BP=1/6. Canonical values: universal_conductor_K_platonic.tex:795-821. AP234. Cache #218.
- B94. "quaternitomy" → "quadrichotomy". Canonical: thm:quadrichotomy in shadow_tower_quadrichotomy_platonic.tex. AP235. Cache #219.

## Cross-Volume Anti-Patterns
Before cross-volume edits, Read `notes/cross_volume_aps.md` (Vol II V2-AP* and Vol III AP-CY1..AP-CY61 catalogs). The Geometric/Algebraic Model Conflations (AP-CY62..AP-CY67) are kept inline below under "Geometric vs Algebraic Models."

## Consolidated / Merged Anti-Patterns

**AP-RMATRIX (= AP126 + AP141 + AP148).** Rule: every r-matrix carries level prefix; verify k=0 in the chosen convention. Counter: (a) substitute k=0 and verify r vanishes (trace-form) or gives Omega/(h^v*z) (KZ non-abelian); (b) state convention; (c) grep bare `\Omega/z`. Two conventions for affine KM: trace-form `r(z)=k*Omega/z` (AP126 k=0 check; av(r)=kappa_dp; Sugawara shift dim(g)/2 for full kappa) and KZ `r(z)=Omega/((k+h^v)*z)` (k=0 nonzero for non-abelian). Bridge: `k*Omega_tr = Omega/(k+h^v)` at generic k. 42+ instances; THE MOST VIOLATED AP.

**AP-KAPPA (= AP1 + AP9 + AP20 + AP24 + AP48 + AP136).** Rule: kappa DISTINCT per family. Always qualify (`kappa^{KM}`, `kappa^{Vir}`). Counter: Read landscape_census.tex; evaluate at k=0, k=-h^v (KM), c=13 (Vir); cross-check compute/. Writing from memory FORBIDDEN. Values: KM=dim(g)(k+h^v)/(2h^v); Vir=c/2; W_N=c*(H_N-1), H_N=sum_{j=1}^{N} 1/j (NOT c*H_{N-1}; at N=2, H_1=1 but H_2-1=1/2); Heis=k. Complementarity: 0 (KM/free), 13 (Vir), 250/3 (W_3), 196 (BP). State WHICH algebra: intrinsic vs kappa_eff=kappa(matter)+kappa(ghost) vs kappa(B=A^!).

**AP-DESUSP (= AP22 + AP45 + B15 + B16).** Rule: `|s^{-1}v|=|v|-1`. Counter: `T^c(s^{-1} A-bar)`, NOT `T^c(s A-bar)`; bar=down=desuspension=s^{-1}.

**AP-SC-BAR (= AP165 + FM25 + B54 + B55 + B56).** Rule: B(A) = T^c(s^{-1} A-bar) is a SINGLE E_1 chiral coassociative coalgebra. SC^{ch,top} lives on the derived center pair (C^bullet_{ch}(A,A), A), NOT on B(A). Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`. The 6-step chain of errors (FM25): (1) "bar differential is closed color" WRONG — d_B is single degree-1 map over (ChirAss)^!, not parametrized. (2) "deconcat = open color" WRONG — cofree coassociative on T^c(V); single-colored E_1. (3) "d_B + Delta = SC-coalgebra" WRONG — two structures != two colors. (4) "SC on B(A) dual to SC on (Z^{der}(A), A)" WRONG — B(A) is INPUT; SC emerges in OUTPUT via Hom(B(A),A). (5) "E_1-chiral = E_1-topological" WRONG — chiral is on CURVE (2-real-dim holomorphic); topological is Conf_k(R); bar is over (ChirAss)^!, not (Ass)^!. (6) Steinberg analogy RETIRED. FORBIDDEN: "B(A) is SC-coalgebra", "bar presents Swiss-cheese", "bar differential is closed color", "bar coproduct is open color", "Curved SC^{ch,top}-algebra" for g>=1 (genus>=1 bar is curved A_infinity-chiral; d^2_{fib}=kappa*omega_g is on A_infinity structure). Counter: after writing B(A) + SC^{ch,top} in same paragraph, verify SC attributed to derived center pair. C^bullet_{ch}(A,A) via End^{ch}_A (spectral params from FM_k(C)), NOT topological RHom_{A^e}(A,A).

**AP-TOPOLOGIZATION (= AP158 + AP167 + AP168 + B58 + B59).** Rule: topologization (SC^{ch,top} → E_3-TOPOLOGICAL via Sugawara) PROVED for affine KM V_k(g) at non-critical level k!=-h^v; CONJECTURAL for general chiral algebras with conformal vector (conj:topologization-general). Proof COHOMOLOGICAL (Q-cohomology), not chain-level; for class M chain-level E_3 may fail. Counter: every reference carries "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)." SC is two-coloured with directionality; Dunn does NOT apply to coloured operads. E_3 requires SC^{ch,top} + conformal vector making C-translations Q-exact; conformal vector KILLS chiral direction at cohomological level, two colors collapse, E_2^{hol}×E_1^{top} → E_3^{top} via Dunn. Without conformal vector: stuck at SC^{ch,top}. At k=-h^v: Sugawara undefined. "Chiral" label FORBIDDEN for topologized bulk; write E_3-topological.

**AP-SC-NOT-SELFDUAL (= AP166 + FM26 + B57).** Rule: `(SC^{ch,top})^! != SC^{ch,top}`. SC^! = (Lie^c, Ass^c, shuffle-mixed), closed dim (n-1)!. SC = (Com, Ass, product-mixed), closed dim 1. Confusion: "duality FUNCTOR is involution" != "OPERAD is self-dual". (P^!)^!~P does NOT mean P^!~P. Livernet proves Koszulity NOT self-duality. Counter: verify dim P(n) = dim P^!(n) at all degrees before claiming self-dual. CORRECT: "SC Koszul duality exchanges Com↔Lie while preserving Ass; duality functor is involution."

**AP-UNIFORM-WEIGHT-TAG (= AP32 + B26).** Rule: every obs_g, F_g, lambda_g in theorem/remark/definition MUST carry explicit scope tag: (UNIFORM-WEIGHT), (ALL-WEIGHT + cross-channel correction delta F_g^cross), (g=1 only), (LOCAL: scope in surrounding paragraph). Untagged = violation.

**AP-LABEL-DISCIPLINE (= AP124 + AP125 + B34 + B35 + FM14 + FM15).** Rule: (i) prefix matches env (thm→theorem, prop→proposition, lem→lemma, conj→conjecture, rem→remark, def→definition); (ii) uniqueness across all three volumes. Counter: before any `\label{foo}`, grep all three volumes (`~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups`); if duplicate, prefix v1/v2/v3. When upgrading/downgrading environment: atomic rename (env + label + all `\ref` instances) in SAME tool-call batch, NO intermediate commit.

**FM-LIE-NUMERICS (= FM5 + FM21 + C16).** Rule: never generate exceptional Lie dimensions from memory. Plausible fabrications (779247 for E_8 is not any irreducible); prefactors (1/2, 1/24, 1/(2*pi*i), 7/5760) frequently wrong. Counter: grep `compute/lib/` before writing; if no match, use symbolic name `V_{omega_1}(E_8)`. E_8 fundamentals: `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.

## Opus 4.6 Quirks and Failure Modes

Model-specific recurrent patterns. Full source: opus_46_failure_modes_wave12.md.

- FM1. Generic-formula reaching. Falls back to textbook form when uncertain. Counter: substitute k=0 and verify r vanishes before proceeding with any r-matrix.
- FM2. Level-prefix dropping on summarisation (omits k, c/2, kappa, 1/(2*pi*i)). Counter: re-Read source lines verbatim; do not rely on context cache.
- FM3. Bosonic/fermionic conformal-anomaly conflation (c_bg, c_bc swap). Counter: substitute lambda=2 AND lambda=1, verify c_bc(2)=-26, c_bg(2)=+26, sum=0.
- FM4. k=0 (abelian, still Koszul) vs k=-h^v (critical, not Koszul) confusion at KM. Counter: two-row table before any KM limit statement.
- FM5. See FM-LIE-NUMERICS.
- FM6. Undefined macros in standalone extraction (`\cW`, `\hol`, `\Ran`, `\FM`, `\chHoch` not inherited). Counter: grep `\\[a-zA-Z]+` against standalone preamble.
- FM7. LaTeX typo `\end{definition>`. Counter: after every .tex Edit, grep `\\end\{[^}]*>` and `\\begin\{[^}]*>`.
- FM8. Universal-quantifier drift on uniform-weight theorems. Counter: three-line template (scope, tag, equation) before any obs_g or F_g.
- FM9. Harmonic-number off-by-one (H_{N-1} vs H_N-1). Counter: evaluate at N=2 AND N=3 numerically.
- FM10. Hardcoded Part~IV/Chapter~12. Counter: after any Edit, grep `Part~[IVX]+|Chapter~[0-9]+` and replace with `\ref{part:...}`.
- FM11. Sugawara shift missing in av(r(z))=kappa. Abelian: av(r)=kappa; non-abelian KM: av(r)+dim(g)/2=kappa(V_k(g)). Counter: state family first.
- FM12. Mid-response truncation on long audit tasks. Counter: separate fix from report across two tool calls.
- FM13. Auto-completion to majority-variant (Dedekind eta as bare `prod(1-q^n)`, missing `q^{1/24}`). Counter: break formula across lines; annotate each term's convention.
- FM14/FM15. See AP-LABEL-DISCIPLINE.
- FM16. Silent kappa-family conflation. Counter: every kappa formula carries explicit family superscript.
- FM17. Amplitude/dimension conflation for ChirHoch. "amplitude [0,2]" != "virtual dimension 2". Counter: choose explicitly.
- FM18. d_gen vs d_alg conflation. d_gen(Vir)=3, d_alg(Vir)=inf. Counter: subscript mandatory; refuse bare `d(...)`.
- FM19. Fiber-base confusion. dτ is on Σ_g; omega_g=c_1(lambda) is on M̄_g. Counter: state space for each side.
- FM20. Iff-drift. Counter: two-line template "Forward:... Reverse:... proved/CONJECTURED" before `\iff`.
- FM21. See FM-LIE-NUMERICS.
- FM22. Koszul conductor K_BP=2 instead of 196. Counter: write K=c+c', substitute two central charges, evaluate.
- FM23. Local-global conflation "over a point = over P^1". Three errors: (1) homotopy retract is DATA, (2) D != point, (3) A^1 already has Arnold relations. Counter: name specific space (point/D/A^1/P^1/X), comparison data, on-the-nose-or-extra-structure. See AP142.
- FM24. B-cycle monodromy i^2 error. hbar with pi*i factor: q=e^{2*pi*i*hbar} becomes real, not root of unity. Counter: substitute integer k; verify |q|=1.
- FM25. See AP-SC-BAR.
- FM26. See AP-SC-NOT-SELFDUAL.
- FM27. Scope inflation in metadata. Counter: scope qualifiers match actual verification level.
- FM28. See AP-TOPOLOGIZATION.
- FM29. Sign convention d+A vs d-A inconsistency. nabla=d+A gives dPhi=-A*Phi; physics nabla=d-A gives dPhi=+A*Phi. Counter: verify nabla(Phi)=0 gives displayed flat section.
- FM30. Belavin r-matrix Weierstrass (WRONG: `zeta(z)=theta_1'/theta_1 + 2*eta_1*z` breaks CYBE) vs Pauli decomposition `r(z)=sum w_a sigma_a⊗sigma_a/2`. Degeneration is TWO-STEP: elliptic→trigonometric (XXZ, Im tau→inf)→rational (z→0). Counter: verify CYBE numerically.
- FM31. Miura coefficient universality. (Psi-1)/Psi on cross-terms in Δ_z is UNIVERSAL across spins (J⊗J at s=2; J⊗T+T⊗J at s=3). Composite corrections appear; primary coefficient persists. Counter: verify at leading cross-term.
- FM31a. Asymptotic cancellation. 10/(5c^2)=2/c^2, NOT 2/(5c^2). Counter: substitute c=100 against exact formula.
- FM32. pi_k(BU): use fiber sequence pi_k(BX)=pi_{k-1}(X); check Bott periodicity parity. pi_3(BU)=0.
- FM32a. RTT sign depends on R-matrix convention. Additive R(u)=uI+Psi*P: [t_ij,t_kl]=Psi(delta_il t_kj - delta_kj t_il). Molev's 1-P/u: opposite sign. Counter: state convention.
- FM33. Formula applied outside hypothesis domain. kappa_ch=chi(S)/2 valid only for Tot(K_S→S); conifold NOT local surface. Counter: verify input satisfies hypotheses before applying.
- FM33a. qdet column ordering DECREASING (j=N-1 leftmost). Left-to-right NOT central at N>=3 (agrees N=2 by coincidence). Cite Molev 1.6.4.
- FM34. Excision=gluing (B_L⊗_A B_R=B(A), one copy over A); coproduct=splitting (B(A)→B(A)⊗B(A), plain). Counter: verify codomain.
- FM34a. Heat equation prefactor: 1/(4πi) diagonal (a=b), 1/(2πi) off-diagonal. Symmetric-matrix chain rule gives factor 2.
- FM35. NEVER REVERT MATHEMATICAL CONTENT TO FIX BUILD ERRORS (CONSTITUTIONAL). Build errors are LaTeX; math is never at fault. Counter: (a) identify specific LaTeX error, (b) fix it, (c) rebuild. 100 macro errors = add 100 `\providecommand` lines. NEVER DROP MATHEMATICS.
- FM36. Macro portability on cross-volume insertion. Counter: grep undefined control sequences after insertion; add `\providecommand`. Related V2-AP39.
- FM37. Double superscript from macro with built-in superscript (`\SCchtop`). Use explicit `\mathsf{SC}^{ch,top,an}`.
- FM38. Vertex-IRF not automatic. If vertex-DYBE fails, attack from IRF/face-model side directly. Genus-2 DDYBE breakthrough bypassed vertex-IRF (29 tests).
- FM39. Spectral coassociativity uses SHIFTED parameters. (Δ_{z1}⊗id)∘Δ_{z1+z2}=(id⊗Δ_{z2})∘Δ_{z1}. NOT Δ_z with itself.
- FM40. Naive center != derived center. Z(Drin(H_k)) dim 1 vs Z^{der}_{ch}(H_k) dim 3. Ext^1,2 invisible to commutant. Specify: commutant, Hochschild, or categorical.
- FM41. Jones polynomial = Markov trace + writhe normalization + quantum dim. Raw KZ trace != Jones.
- FM42. Bulk substring replacement corruption (CRITICAL). `replace_all` "arity"→"degree" corrupts singularity→singuldegree, parity→pdegree, etc. 45 corruptions in Vol III campaign. Counter: (1) NEVER bulk-replace short strings inside common words; (2) after any bulk replace, grep `ldegree|ndegree|rdegree|pdegree|tdegree`; (3) checklist {singularity, complementarity, unitarity, regularity, modularity, parity, familiarity, similarity, polarity, disparity, linearity, popularity, circularity, hilarity}.
- FM43. E_n output scope of CY-to-chiral Φ: E_2-chiral at d≤2, E_1-chiral at d≥3. Counter: always state scope `(n=2 for d≤2; n=1 for d≥3)`.
- FM44. Agent rate limiting. Counter: batches of 3, not 30+. Expect 5-13 min per agent on 1000-3000 line files.
- FM45. Agent skill fidelity gap (200-word brief vs 15,000-word skill). Counter: for full rectification, invoke skill in main conversation.
- FM46. Stale preface line counts. Counter: after campaign, update with `wc -l` comparison.
- AP186 (Opus). Coincidental agreement masks bugs. (Psi-1)/Psi=1/Psi at Psi=2; comb(d+2,2)=comb(d+2,3) at d=3. Verify at 3+ parameter values.
- AP187 (Opus). Miura coefficients from elementary symmetric expansion. T(u)=prod(u+Λ_i) → ψ_s=e_s(Λ_i). Coefficient of :J*W_{s-1}: is 1/Psi at all s>=2 (thm:miura-cross-universality).

## Theorem Status

**2026-04-17 Beilinson-rectified addendum**: the status table below reflects the 2026-04-16 closure wave inscriptions. Subsequent audit findings (Vol~I `notes/rectification_map_beilinson_audit.md`) refined the following claims: (i) Programme climax `thm:programme-climax` (Vol II) is SCOPE-QUALIFIED to non-logarithmic C_2-cofinite standard landscape + irrational cosets; logarithmic W(p) excluded pending Adamovi\'c-Milas character-amplitude bound (see Open Frontiers section). (ii) CY-C pentagon (Vol III) stratifies generator rank ρ^{R_i}, NOT κ_ch (Hodge-supertrace invariant = 0 route-independent). (iii) Kummer-irregular prime labels 1423, 3067, 23, 43, 419 retracted at primary-source verification. (iv) Super-Yangian max(m, n) complementarity identity replaces naive sum=0 analogy. (v) Topologization class M original-complex chapter carries explicit RETRACTION NOTICE; the 1/e obstruction is a Stirling cancellation error, unconditional heal at `thm:tempered-stratum-contains-virasoro` (Vol II). The theorems A-D+H remain PROVED at their stated scopes; only scope qualifiers and cross-reference labels changed.

| Thm | Status | Key result |
|-----|--------|------------|
| A | **PROVED unconditional** (fixed curve + relative smooth + M̄_{g,n} including boundary for standard landscape) | Genus-0 clause: seven-fold hub-and-spoke TFAE (`thm:ftm-seven-fold-tfae-via-hub-spoke`, Vol I `chapters/theory/ftm_seven_fold_tfae_platonic.tex` 700 lines + 8 HZ-IV decorators, 2026-04-16): six spokes (Koszul morphism, counit qi, unit weak eq, twisted tensor acyclic, bar concentrated in weight 1, SC-formality) each bidirected to the PBW E_2-collapse HUB (6 bidirections, not 21 arrows via transitivity). Spoke 4 (twisted tensor ⇔ PBW) is the load-bearing non-tautology witnessed by V_k(sl_2) at generic k. SPOKE 7 (SC-formality) is CLASS-G SCOPED (class L / class M are Koszul but not SC-formal, AP14). Spoke 5 (bar concentration weight 1) extends to g≥1 only for class G (d²_fib = κ·ω_g obstruction off class G). Patterns #246-252 cached. Prior ghost-label `thm:FTM-seven-fold` (never defined) retargeted at `theorem_A_infinity_2.tex:570`. **Modular-family PROVED (2026-04-16)**: (1) hypothesis (c) base change proved via BD holonomic + GR17 Vol II six-functor formalism on relative Ran prestack; (2) nodal sewing theorem via Mok25 log FM + Francis-Gaitsgory factorization-gluing + HS-sewing convergence (chain-level at nodes); (3) full M̄_{g,n} assembly via K-theoretic filtration globalization (Thm-D template: filter by collision depth, assoc-graded = Arnold OS, λ_{-1}(bundle) Euler char). **PTVV/factorization-homology alternative** H01 upgraded to proposition: Costello-Gwilliam factorization homology + PTVV 1-shifted symplectic Lagrangian correspondence, genuinely independent (no Verdier-pair hypothesis). **E_1-ordered variant** `thm:theorem-A-E1` PROVED via pure braid Orlik-Solomon Koszulity (Shelton-Yuzvinsky); Yangian instance concrete (Cherednik monodromy). Residual: only non-finitely-generated MC4-completion regime; finitely generated standard landscape unconditional. |
| B | **PROVED unconditional** at coderived level; chain-level class G/L via explicit MacLane-splitting | **thm:chiral-positselski-7-2 inscribed (2026-04-16)**: for conilpotent chiral CDG-coalgebra C on X with finite-dim graded pieces, counit Ω_X(B_X(C)) → C is iso in D^co_chi(X). 6-step proof: chiral Φ/Ψ adjoints + bicomplex totalization + conilpotent contracting homotopy + coacyclic cone. Thm B (2) off-locus UNCONDITIONAL after inscription (no phantom "chiral adaptation"). **thm:chiral-positselski-5-3 inscribed**: co-contra correspondence D^co ≃ D^ctr. Class G (Heisenberg): explicit chain-level inverse σ_Heis via MacLane splitting on Sym(V_{[1]}) free structure — chain-level qi unconditional. Class L (affine KM non-critical): σ_KM via PBW filtration + E_2-collapse lifting. **FTM seven-fold TFAE** resolves g=0 tautology (adds shadow-truncation + SC-formality equivalences to original four-fold). Ordered E_1-variant proved for Yangian (EK quantization acyclicity = FM^ord Koszulness). Class M chain-level: GENUINELY FALSE at direct-sum level (S_4≠0 forces bar cohomology at weight 4); weight-completed PROVED. |
| C | **PROVED unconditionally on Koszul locus** (C0, C1); C2 Lagrangian upgrade conditional only on BV package | **9 strengthening inscriptions (2026-04-16)**: (T1) `lem:derived-center-koszul-equivalence` resolves F1 naive/derived equivocation — brace dg algebra level Z^der_ch(A) ≅ Z^der_ch(A^!) (E_2 after Deligne-Tamarkin) + H^0 recovers naive center iso with Koszul pairing. (T2) `prop:perfectness-standard-landscape` UNCONDITIONAL: verified family-by-family (Heisenberg finite at each weight; affine KM non-critical via Kac-Kazhdan; Virasoro generic c; W_N Fateev-Lukyanov; lattice via theta/eta; betagamma via character). (T3) C1 reflexivity unconditional on Koszul locus (perfectness now a THEOREM, not hypothesis). (T4) `thm:theorem-C-g0` separate statement: M̄_{0,3} = point, σ acts trivially, Q_0(A^!) = 0, Verdier pairing degree 0 (not -3) — the +3 shift contradiction resolved. (T5) C2 hypotheses pinned: BV package + Verdier + bar-chart lift ONLY; uniform-weight is NOT a C2 hypothesis (belongs to scalar-complementarity corollary). (T6) C0 unconditional with identifications (perfectness absorbed via T2). (T7) AP203 resolution (via MC5 strengthening) closes class-M C2(iii) in weight-completed category. (T8) `prop:delta-f-cross-w3-g2` explicit: δF_2^cross(W_3) = (c+204)/(16c). (T9) `thm:C-PTVV-alternative` GENUINELY INDEPENDENT proof for C1 g≥2 via mapping-stack RMap(M̄_g, BG_A) + PTVV shifted-symplectic + Verdier anti-symplectic involution. |
| D | PROVED unconditionally (uniform-weight, Koszul locus, all g≥1) | obs_g=kappa·lambda_g uniform-weight; multi-weight: +delta_F_g^cross (thm:multi-weight-genus-expansion gives delta_F_2(W_3) = (c+204)/(16c) explicit). **All 3 prior gaps CLOSED (2026-04-16)**: (i) Step 1 virtual-class globalization via K-theory filtration + lambda_{-1}(E) + top-degree Chern character identity `ch_g(lambda_{-1}(E)) = c_g(E)` (splitting principle); (ii) Faltings citation retargeted to Arakelov 1974 + Faltings 1984 §2 + Soulé 1992 Ch.III (fiberwise Chern-curvature formula for Hodge bundle in Arakelov metric); (iii) BGS c_1(det E) → c_g(E) bridge via splitting principle + scalar-channel linearity (Chern-Weil for scalar-endomorphism-valued curvature reads off top Chern class with LINEAR scalar coefficient, not multiplicative). **AP225 resolved**: clutching-uniqueness proposition (genus-1 base + separating clutching additivity + nonseparating clutching trivialization + tautological-ring purity) pins obs_g/kappa = lambda_g uniquely (Graber-Vakil socle theorem). **H04 upgraded**: factorization-homology + PTVV 1-shifted-symplectic alternative is GENUINELY DISJOINT (derived-categorical, no uniform-weight hypothesis) — suggests the uniform-weight restriction is technical, not essential. |
| H | PROVED sharp Hilbert series on Koszul locus; E_1-variant PROVABLE | ChirHoch*(A) concentrated in degrees {0,1,2} with exact formula `P(t,q) = HS_{Z(A)}(q) + HS_{ChirHoch^1(A)}(q)·t + HS_{Z(A^!)}(q)·t^2`. Critical level k=-h^v excluded. **Step 3 circularity RESOLVED (2026-04-16)**: rerouted through `thm:pbw-koszulness-criterion` (PBW collapse) directly via Shelton-Yuzvinsky Koszulity of braid-arrangement Orlik-Solomon algebras + chiral quadratic-Koszul lemma; bar-concentration and fm-tower-collapse now parallel consequences of PBW, not sequential. **AP222 healed**. Three independent-verification decorators drafted: Heisenberg via Feigin-Frenkel CE (disjoint from bar), Virasoro via Wang BRST/Feigin-Fuks (disjoint), affine sl_2 via Whitehead+Kunneth (disjoint). **E_1-variant `thm:hochschild-concentration-E1`** (for Yangian input): provable via FM^ord + pure braid Orlik-Solomon + ordered Koszul dual; symmetric-bar obstruction R(z)≠τ IS the quantum-group content. ALT H05 retrievable as sharp-Hilbert-series from `fm-tower-collapse` E_2 page. |
| MC1-4 | **PROVED UNCONDITIONAL** at generic parameters (principal class M); **MC3 PROVED via five-family mechanism (Baxter RETRACTED)** | MC1 universal (semisimple hyp) via Whitehead; **MC1 Virasoro g≥2 PROVED unconditionally** via L_0-diagonalization on augmentation ideal (bypasses hypothesis (c) semisimple — family-specific L_0 argument suffices). **Feigin-Fuks resolution provides independent verification** + extends to principal W_N generic Ψ via Feigin-Frenkel screening. MC2 bar-intrinsic PROVED. **MC3 PROVED via five-family mechanism on the EVALUATION-GENERATED CORE** (AP47 scope; Vol I `chapters/theory/mc3_five_family_platonic.tex` 676 lines + 8 HZ-IV decorators, 2026-04-16): asymptotic prefundamentals (type A); reflection-equation Shapovalov (B/C/D); Chari-Moura multiplicity-free ℓ-weights (uniform); theta-divisor complement (elliptic); parity-balance (super-Yangian). Baxter constraint retracted as type-A rational artifact. Extension to full DK_g unconditional only in type A modulo `conj:dk-compacts-completion`; CONJECTURAL elsewhere. Silent non-coverage: logarithmic W, N=2 SCA, cosets, non-rational lattice, roots of unity (see `thm:mc3-full-DK-conjectural`). Six confusion patterns #240-245 cached. MC4⁺ UNCONDITIONAL. **MC4⁰ PROVED UNCONDITIONAL (2026-04-16)** at generic parameters for class M principal: explicit SDR via Wakimoto one-step (Virasoro) / Feigin-Frenkel screening (W_N), homotopy h_htpy = (1 − ιp)/(L_0 − h − N + 1) invertible generically. Non-principal hook-type (r ≤ N-3) PROVED via parabolic screenings (KRW03, Arakawa07). Subregular/minimal W reduce to class-C SDR (βγ) — genuine remaining math, not plumbing. MC2 ALT H06 (KS scattering) conditional on support-property comparison (open). |
| MC5 | **PROVED on THREE equivalent ambients of the original complex** (pro-object / J-adic topological / weight-completed filtered) for all four shadow classes; direct-sum chain-level in `Ch(Vect)` genuinely FALSE (ambient artefact, NOT a gap) | Analytic: HS-sewing unconditional. Coderived: coacyclic characterization. **Chain-level class M PROVED in THREE EQUIVALENT AMBIENTS of the raw bar complex (2026-04-17, originally 2026-04-16 weight-completed + 2026-04-17 pro-ambient/J-adic upgrades)**: (i) `thm:mc5-class-m-chain-level-pro-ambient` in `chapters/theory/mc5_class_m_chain_level_platonic.tex:229-437` — pro-object ambient pro-Ch(Vect), strict chain-level qi at every genus g ≥ 0, 4-step proof (finite-stage qi via h_N = Σ h·m_0^{j-1} → Mittag-Leffler in every cohomological degree → pro-qi); (ii) `thm:mc5-class-m-topological-chain-level-j-adic` — J-adic topological complex; (iii) weight-completed via `thm:completed-bar-cobar-strong` + `prop:standard-strong-filtration`. **The direct-sum "genuine falsity" is an ambient-choice artefact**: S_4(Vir_c) = 10/[c(5c+22)] nonzero forces bar cohomology in weight 4 ONLY in the bounded-direct-sum ambient `Ch(Vect)`, which is NOT the ambient of the raw bar complex with its weight topology; direct sum embeds into product as a dense subspace and the inverse limit IS the original bar complex. The 2026-04-17 adversarial Wave 1 surfaced this propagation gap and closed the "chain-level class M on the ORIGINAL complex" frontier item. **AP203 HEALED**: uniqueness of central degree-2 m_0 via Hodge + vacuum-proportionality (H^{2,0}(curve)=0 kills competing bar-length-2 insertions). **c_r = S_r proved** (not just named): harmonic projector on H_g coincides with av on degree-r component. `prop:harmonic-factorization` duplicate + truncated proof HEALED at bv_brst.tex. **H07 UPGRADED**: direct SC^{ch,top} homotopy-Koszulity via Ginzburg-Kapranov for Com⊥Lie closed color + Ass self-duality open + Deligne-purity degeneration (Mok25 log-FM smoothness) — replaces Livernet transport. |
| Koszul | 10+1+1 | 10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir). Equiv (vii): uniform-weight all-genera / multi-weight genus-0 only. Equiv (viii): concentration proved; freeness conditional on Massey vanishing. ALT: proof web (H09). |
| D^2=0 | PROVED | Convolution on universal family over M-bar_{g,n}; ambient Mok25 log FM. |
| Theta_A | PROVED | Bar-intrinsic; all-degree inverse limit (thm:recursive-existence). |
| SC-formal | PROVED | SC-formal iff class G. Forward: operadic tower truncation (Delta=0). Converse: shadow tower controls SC ops. ALT: operadic both directions (H11). |
| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3. Betagamma d_alg=2 witness on standard conformal-weight line. Impossibility of 3 via MC relation + shadow Lie Jacobi. ALT: representation-theoretic (H10). |
| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g))=g; total dim=dim(g)+2 (prop:chirhoch1-affine-km). |
| Topologization | **PROVED chain-level on original complex for G/L/C/critical; PROVED weight-completed for M** (thm:topologization-tower) | **Topologization tower theorem (2026-04-16)**: (1) class G (Heisenberg): E_3^top immediate (commutative ⇒ Dunn on F^{H_k}); (2) class L (V_k(g), k≠-h^v): **E_3^top on ORIGINAL complex** via Dunn-additivity rerouted through CG factorization algebra F^{CS}_k on R×C (single-colored, not SC^{ch,top}!) + explicit η_1^(i) = (1/2(k+h^v)) Σ f^a_bc :bar c_b c^c bar c_a: and η_1^(ii) = (1/2(k+h^v)) Σ f_{ab}^c :bar c_a bar c_c c^b:, making [Q, tilde G_1] = T_Sug STRICT chain-level (not up to Q-exact); (3) class C (βγ, bc): E_3^top via FMS bosonization reducing to Heisenberg; (4) class M (Vir, W_N): **weight-completed chain-level E_3^top** via half-BRST + MC5 pattern (original complex remains open); (5) critical level k=-h^v: **E_2^top (not E_3)** — Sugawara collapse is a dimension drop, not a failure. Original chain-level for class M is the single remaining open direction; everything else PROVED on original complex. ALT via CG factorization homology H08 no longer conjectural. |
| E_3 identification | **PROVED simple; gl_N; semisimple; reductive; nilpotent (Heisenberg); solvable (finite derived series is UNCONDITIONAL)** | Z^der_ch(V_k(g)) ≅ A^λ as E_3-families. **9 strengthening inscriptions (2026-04-16)**: (1) `prop:e3-gl-N` promoted from remark to proposition — 2-param (B_tr, B_ab); (2) `thm:e3-identification-semisimple` r-param via Cartan-Whitehead + Kunneth; (3) `thm:e3-identification-reductive` N = r + C(d+1,2) params with abelian center contributing via Sym^2(z^*) invisible to H^3; (4) `prop:e3-heisenberg` 4-dim Sym^2(h^*)^h (not 1-dim H^3(h))—Whitehead failure explicit; (5) `thm:e3-identification-solvable` UNCONDITIONAL (finite derived series = finite filtration, converges strongly); (6) part (iv) Sugawara unconditional; (7) explicit E_3-algebraic vs E_3-topological comparison diagram; (8) chain-level on qi-model via Fresse Vol II Thm 16.2.1 operad-level→algebra-level formality; (9) CY_4 p_1-twisted double current algebra (π_4(BU)=Z is obstruction GROUP, not structure — cross-link Vol III AP-CY46). |
| Elliptic chiral QG | PROVED leading-order ℏ for sl_2 via Felder R + KZB + Fay trisecant | θ_1'/θ_1 propagator (NOT Weierstrass ζ). Heat prefactor 1/(4πi) diag / 1/(2πi) off-diag. |
| CY_4 p_1-twisted | PROVED as Y_{p_1}(X) double current algebra with c(x,y) = ⟨x ∪ y ∪ p_1(T_X), [X]⟩/24 | Derived from π_4(BU) = Z obstruction. 7d hCS realization. K3×K3: N(X) = 0, unobstructed E_4. |
| Toroidal chiral QG | PROVED formal-disk via DIM + SV CoHA; global P¹×P¹ conditional on class-M chain-level | 2-param RTT; Miki S_3 = Weyl of Ω-background. |
| Chiral QG equiv | **PROVED on ORDERED Koszul locus (E_1-chiral input included); elliptic PROVED; toroidal formal-disk PROVED** | Three structures (R-matrix, A_inf, ordered coproduct) determine each other on ordered Koszul locus. **8 strengthening inscriptions (2026-04-16)**: (1) `def:ordered-koszul-chiral-algebra` explicit; (2) `prop:yangian-ordered-koszul` Y_ℏ(g)^ch via Drinfeld second presentation + Etingof-Kazhdan flatness; (3) `thm:chiral-qg-equiv-ordered` covers E_1-chiral input (Yangian); (4) `prop:sl2-yangian-triangle-concrete` with explicit α,β,γ order-ℏ computation including triangle coherence α∘γ∘β=id; (5) `thm:glN-drinfeld-double-internal` bypasses JKL26 via Miura + cross-arity Stasheff + U(ĝl_1) screenings; (6) `thm:w-infty-chiral-qg-completed` resolves class-M contradiction via weight-completed category (MC5 pattern); (7) `thm:grt1-rigidity` makes associator-dependence explicit: trivial on H^0, homotopic on cochains; (8) `thm:chiral-qg-equiv-elliptic` with Felder dynamical R(z,τ) and Fay trisecant replacing pentagon; `thm:chiral-qg-equiv-toroidal-formal-disk` via SV CoHA + Miki DIM. |
| Non-principal W | PROVED hook-type (r ≤ N-3) via parabolic screening (KRW03) | Subregular via (principal W_{N-2}) × sl_2 × βγ. Minimal via coset. Screening-kernel Koszul-locus preservation proved. Logarithmic W(p) Massey ⟨Ω,Ω,Ω⟩ obstruction explicit. |
| gl_N chiral QG | **PROVED UNCONDITIONAL all N≥2 via Feigin-Frenkel screening** (JKL26 phantom eliminated) | Feigin-Frenkel replacement of Argument B (2026-04-16): W_N = ∩ ker(Q_{α_i}) inside rank-(N-1) Heisenberg (class G with explicit chiral QG datum). Drinfeld coproduct descends to intersection; RTT inherited from abelian parent. **Lemma (qdet-central-all-N)** inscribed internally (Molev's antisymmetriser argument, not external citation). Concrete N=4,5 via engine extension. **Ψ=0 degenerate case** (free abelian chiral algebra, identity QG) and **Ψ=1 free-boson point** (OPE obstruction vanishes) inscribed. **Two-parameter gl_N RTT** matches rem:e3-non-simple-gl-N (both give Sym^2(gl_N^*)^{gl_N} = 2-dim). **Non-principal W hook-type (r ≤ N-3)** via parabolic screenings (KRW03, Arakawa07). DS intertwining HZ-IV fix via independent sl_3 RTT computation inscribed (no longer tautological). |
| Verlinde recovery | PROVED | Verlinde Z_g = sum S_{0j}^{2-2g} recovered from ordered chiral homology at integer level (prop:verlinde-from-ordered). |
| ker(av) formula | PROVED (all simple g) | dim(ker(av_n)) = d^n - C(n+d-1,d-1) for d-dim rep (prop:ker-av-schur-weyl). |
| Genus-2 construction | CONSTRUCTED | KZB with 2x2 Siegel period matrix, chi=-12 at degree 2, doubly-dynamical (conj:g2-ddybe). |
| Miura coefficient | PROVED (thm:miura-cross-universality) | (Psi-1)/Psi on J⊗W_{s-1}+W_{s-1}⊗J at ALL spins s>=2. Three-step proof; verified spins 2-6, 142 tests. |
| Z_g closed forms | DISCOVERED g=0..9; PROVED all g via Hurwitz-Bernoulli; arithmetic duality at leading Kummer-irregular primes {691, 3617} PROVED through r=11 | P_g(n) = n^{g-1}(n²-1)·R_{g-2}(n²), n=k+2. Leading = B_{2g-2}/(g-1). Kummer-congruence prediction (691 at Z_7, 3617 at Z_9) is falsification test. Arithmetic duality `thm:z-g-s-r-arithmetic-duality` (z_g_kummer_bernoulli_platonic.tex): leading Kummer-irregular primes {691, 3617} present on Z_g (via B_{2g-2}) AND absent on S_r(Vir_c) through r=11 `thm:s-r-kummer-absent-through-r-11` (shadow_tower_higher_coefficients.tex). Sharp at {691, 3617}: the higher Kummer-irregular prime 2111 appears in N_9 (via 29554 = 2·7·2111), but is not witnessed on Z_g at g≤9 since 2111 ∤ num(B_{2m}) for 2m≤16. Geometric disjointness: Z_g localises on Bun_{SL_2}(Σ_g), S_r on ChirHoch(Vir_c). Characteristic S_r primes include {61, 193, 2111, 16657, 3988097}. HZ-IV decorator at compute/tests/test_z_g_s_r_arithmetic_duality.py. |
| W_N Stokes count | DISCOVERED | Stokes rays for W_N KZ = 4N-4 (linear in N). W_2: 4. W_3: 8. Poincare rank = 2N-2. |
| Shadow = GW(C³) | IDENTIFIED | Shadow tower at κ=Ψ produces perturbative constant-map GW free energies F_g^{GW,const}(C³). MacMahon M(q) on DT side via MNOP. |
| Conformal anomaly | QUANTIFIED | Obstruction to constant coproduct = c/2 = κ(Vir_c). At c=0: obstruction vanishes. At c≠0: spectral parameter FORCED. |
| Chiral Higher Deligne | **PROVED (Vol II `chapters/theory/chiral_higher_deligne.tex`, 2026-04-16)** | `thm:chiral-higher-deligne`: Z^{der}_ch(A) is universal E_3-chiral algebra acted on by SC^{ch,top} via heptagon edges (3)↔(4)↔(5). `thm:H-concentration-via-E3-rigidity`: Thm H concentration is CONSEQUENCE of E_3-rigidity-at-a-point plus PBW collapse. `thm:chd-ds-hochschild`: ChirHoch^•(W_k(g)) ≃ H^•_DS(ChirHoch^•(V_k(g))) chain-level E_2-chiral Gerstenhaber. `cor:universal-holography-class-M`: closes class-M chain-level 3d HT holography. |
| Curved-Dunn H²=0 at g≥2 | **PROVED (Vol II `chapters/theory/curved_dunn_higher_genus.tex`, 2026-04-16)** | `prop:modular-bootstrap-to-curved-dunn-bridge`: chain map Φ on H²; `prop:genus1-twisted-tensor-product`: explicit Gauss–Manin uncurving + Arakelov pairing (phantom FM87 resolved); `thm:curved-dunn-H2-vanishing-all-genera`: curved-Dunn H²=0 ∀g≥2 via bridge from modular-bootstrap H²=0. `thm:irregular-singular-kzb-regularity`: Jimbo–Miwa replaces KZ Stokes, closes modular operad composition at generic non-integral level. Closes FM67/FM88/FM91/FM92/FM192/FM215. |
| SC^{ch,top} heptagon | **PROVED (Vol II `chapters/theory/sc_chtop_heptagon.tex`, 2026-04-16)** | Five classical faces + face (6) Drinfeld-centre `Z(Rep_fact(A)) ≃ Rep_fact(Z^der_ch(A))^{E_2}` via categorified bar-cobar with half-braiding (AP-CY25) + face (7) derived-AG via PTVV on `Map(X×R_≥0, B SC-Alg)`. Seven named edge theorems prove the closed heptagon. SC^{ch,top} is the GENERIC case; topologization to E_3-top at affine KM non-critical is proved, general chiral conjectural. |
| Universal celestial holography | **PROVED chain-level (Vol II `chapters/connections/universal_celestial_holography.tex`, 2026-04-16)** | `thm:uch-main`: SC^{ch,top}-structure on `(A^cel, Z^der_ch(A^cel))` + celestial OPE = chiral factorization homology on `P^1_cel` + shadow-tower coefficients = soft-factor hierarchy. Coverage: self-dual gauge (KM), gauge+matter (DS), gravity (Virasoro + w_{1+∞}), YM (Beem–Rastelli χ-functor). Closes FM102/FM103. Chain-level class M at g≥1 still open as `conj:uch-gravity-chain-level`. |
| Periodic CDG admissible KL | **PROVED (Vol I `chapters/theory/periodic_cdg_admissible.tex`, 2026-04-16)** | `thm:periodic-cdg-is-koszul-compatible`: periodic-CDG filtration `F^n = ker(Q^n_{adm})` on `KL_k^{adm}` at `k+h^v = p/q` compatible with chiral Koszul duality. `thm:admissible-kl-bar-cobar-adjunction`: `Ω^ch ⊣ B^ch` descends unconditionally to `KL_k^{adm} ⇄ (KL_{k^!}^{adm})^op`; proof via Arakawa C_2-cofiniteness + periodic-CDG finite length + Adams-type spectral sequence with `d_1 = Q_{adm}`. `thm:adams-analog-construction`: chiral Steenrod algebra `A^{ch}_k` + chiral Adams functor; closes FM256. `cor:class-M-admissible-minimal-model`: `KL^{adm}_{Vir}(c_{p,q})` has `(p-1)(q-1)/2` simples, all finite-length (closes FM76 scope hole). Closes FM251 + the sole remaining irreducible-open programme frontier. |
| E_∞-Topologization | **PROVED (Vol II `chapters/connections/e_infinity_topologization.tex`, 2026-04-16)** | `thm:iterated-sugawara-construction`: higher-spin Casimir tower `{T^{(n)}}_{2 ≤ n ≤ N+1}` each inner, admitting BRST primitive G^{(n)} with `T^{(n)} = [Q_tot, G^{(n)}]` on cohomology. `thm:e-infinity-topologization-ladder`: k inner stress tensors ⟹ E_{k+2}-top via Dunn with E_2-chiral ⊗ E_1-top(T^{(n_1)}) ⊗ ... ⊗ E_1-top(T^{(n_k)}). Specializations: Virasoro (N=2) → E_3-top; W_N → E_{N+1}-top; W_∞ → E_∞-top (Platonic endpoint). `thm:operadic-spiral`: infinite bidirectional spiral with bar B descending, center Z ascending, meeting at E_∞. Closes FM47/48/81/82/215 (W_N hook-type via branched cover, class M free-PVA via Li-filtration). Climax restatement: 3d quantum gravity Vol II Part VI is N=2 shadow of a 3d+∞ topological theory. |
| Theorem A^{∞,2} | **PROVED (Vol I `chapters/theory/theorem_A_infinity_2.tex`, 2026-04-16)** | `thm:A-infinity-2`: Francis-Gaitsgory bar-cobar (∞,2)-equivalence at properad level. `B̄^ch_X : Fact^{aug}(X) ⇄ CoFact^{conil,comp}(X) : Ω^ch_X` (∞,2)-adjoint equivalence on conilpotent-complete locus. Three clauses: (i) properad lift via Hackney-Robertson in FG ambient; (ii) pole-free restriction recovers LV12 (Ass, Ass^!) via `(D_X-mod, ⊗^!) ↪ Fact(X)`; (iii) R-twisted Σ_n-descent (`lem:R-twisted-descent`) relates `B^{ord}(A)` to `B^Σ(A)`. Closes FM69/70/72/73/74/195 (ambient category corrections, cross-volume citation drift). 14+ downstream corollaries enumerated (classical Theorem A, bar-cobar adjunction, Vol II bridge I.3.2, Vol III Φ, ...). `cor:chiral-KK-formal-smoothness`: FG ambient + R-twisted descent ⟹ formally smooth at properad level. |
| CY-D dimension stratification | **PROVED (Vol III `chapters/examples/cy_d_kappa_stratification.tex`, 2026-04-16)** | `thm:kappa-hodge-supertrace-identification`: `κ_ch(A_X) = Σ_q (-1)^q h^{0,q}(X)` unconditionally for compact CY_d via HKR + Mukai pairing + HC^-_d trace. `thm:kappa-stratification-by-d`: explicit values across d ∈ {1,2,3,4,5} — E(0), K3(2), abelian/bielliptic(0), quintic/K3×E/E³(0), local P²(3/2 via `thm:local-p2-shadow`), CY_4 sextic(2), CY_5 generic(0). `cor:conifold-non-local-surface` closes AP-CY34/AP-CY44 (conifold is NOT local surface at d=3; κ_ch=1 via direct McKay). `thm:borcherds-weight-kappa-BKM-universal`: κ_BKM(Φ_N) = c_N(0)/2 universal across N ∈ {1,2,3,4,6}; N=1 coincidence κ_BKM = κ_ch + χ(O_fiber) fails for N ≥ 2 (closes AP-CY37 + top-15 #15). |
| BP Koszul-conductor polynomial identity | **PROVED IN ARAKAWA CONVENTION (Vol I `standalone/bp_self_duality.tex:253-297`, 2026-04-16)** | `thm:bp-koszul-conductor-polynomial`: in Arakawa convention `c(BP_k) = 2 - 24(k+1)²/(k+3)`, `K_BP(k) := c(BP_k) + c(BP_{-k-6}) ≡ 196 ∈ Q(k)` constant rational function; `c(BP_k) - 98` is odd function of `(k+3)`. Fixed point `k = -3` coincides with critical level `-h^v(sl_3)`; `κ(BP_{-3}) = 49/3` is principal-value symmetric limit. 73+7 tests pass with 2 disjoint HZ-IV decorators. **Convention caveat (Vol II cross-check, 2026-04-17)**: Fateev-Lukyanov screening convention `c^{FL}(k) = -(2k+3)(3k+1)/(k+3)` gives `K^{FL}_BP(k) = -12(k+3) - 48/(k+3)` — meromorphic with pole at k=-3, NOT polynomial. Both conventions parametrize the SAME BP algebra via level reparametrization; the polynomial-identity theorem is Arakawa-convention specific. Vol II `bp_chain_level_strict_platonic.tex` uses FL convention consistently with `fm81_fractional_ghost_platonic.tex` template. |
| Critical level jump | PROVED | At k=-h^v: kappa=0, monodromy trivial, H^1 doubles (4→8), Koszulness fails, bar H* = Omega*(Op_g^v(D)). 72 tests. |
| Genus-2 degree decomp | PROVED | CB_{2,2}(k) = 2k(k+1)(k+2)/3 (cubic). At k=1: 4. Singlet+triplet channels (prop:g2-conformal-block-degree). |
| Antipode non-lifting | PROVED (negative) | S(T(u))=T(u)^{-1} does NOT lift to vertex-algebraic antipode. Two obstructions (OPE and Hopf axiom). |
| DS intertwining | VERIFIED | (pi_3×pi_3)∘Delta_z^{sl_3} = Delta_z^{W_3}∘pi_3 verified 57 tests. Spectral coassociativity uses shifted parameters. |
| AP128 bar H^2 | FIXED | sl2_bar_dims gave h_2=6 (CE/Riordan). Correct chiral bar: h_2=5. AP63: Orlik-Solomon form factor. |
| Quantum det ordering | FOUND | Central qdet uses DECREASING column index. At N=3, increasing-index NOT central. 74 tests. |
| E_3 via Dunn | PROVED (alt) | prop:e3-via-dunn: CG factorization E_1^top×E_2^hol + Sugawara + Dunn = E_3^top. Independent of HDC. |
| E_3 for gl_N | EXTENDED | E_3 identification extends to gl_N via two invariant bilinear forms B_tr, B_ab. |
| 6d hCS defect | PROVED | Codim-2 defect on C⊂C³: boundary algebra = W_{1+inf} with Psi=-sigma_2. c=1 (Sugawara). N_{C/Y}=C² gives spectral params. 48 tests. |
| DDYBE face model | **NUMERICAL EVIDENCE** + **CONJECTURED** at generic Ω (Platonic form, Vol I `chapters/theory/genus_2_ddybe_platonic.tex`, 2026-04-16) | Face-model strategy bypasses vertex-IRF (the latter not established at g=2). Tolerance ladder T1(10^{-12})/T2(10^{-10})/T3(10^{-6})/T4(10^{-4}). Generic-Ω DDYBE: 5 tests at T4 (10^{-4} relative); diagonal-Ω factorization exact via two genus-1 DYBE copies (T3 10^{-6}); separating degeneration AP157-empty. Full 29 face-model tests span θ_1 antisymmetry (T1), weight-zero matrix entries (T2), classical limit + degeneration (T3), generic-Ω DDYBE (T4). `conj:g2-ddybe` remains ClaimStatusConjectured — finite-ℏ commutativity of doubly-dynamical Casimirs is the residual conjecture (infinitesimal proved via heat-equation symmetry). "Fay trisecant extends to g=2" resolved: Szegő three-term identity (Fay 1973 Cor. 2.5) holds universally at all g ≥ 0; distinct from theta-nulls quartic identity on theta-divisor. Cache entries #220-227. |
| Drinfeld center Heis | VERIFIED | conj:drinfeld-center-equals-bulk for H_k: 5 invariants at 6 levels. Naive dim 1 vs derived dim 3. 72 tests. |
| Toroidal coproduct | CONJECTURED | conj:toroidal-two-param-coprod: Delta_{z,w}(T(u,v))=T(u,v)⊗T(u-z,v-w). Miki equivariance. 5-step. |
| Coderived E_3 | PARTIAL | Steps 1-2 proved (D^co stable ∞-cat; obstruction coacyclic). Step 3 open. |
| KZB flatness | VERIFIED | d_tau(wp_1) = (1/(4πi))d_w(wp+wp²) at machine precision. Prefactor 1/(4πi) diagonal vs 1/(2πi) off-diagonal. |

## Anti-Patterns by Topic

### Epistemic
AP2: Read actual .tex proof, not CLAUDE.md description. Descriptions are claims ABOUT source.
AP4: ClaimStatusProvedHere = verify proof proves stated claim. Status tag != ground truth.
AP11: Single-point external dependency -> flag in concordance with source/status/fallback.
AP13: Forward references transparent about genus/level/type restrictions.
AP15: E_2* is quasi-modular. Genus-1 propagator IS E_2*. Graph sums produce {E_2*,E_4,E_6}, NOT {E_4,E_6}.
AP17: After writing ANY new theorem, IMMEDIATELY audit before building next result.
AP26: Fock inner product != BPZ for weight>=4, rank>=3 W-algebras.
AP28: NEVER use undefined terminological qualifier in 3+ locations.
AP35: False proof, true conclusion -> two cancelling errors. Fix BOTH.
AP37: SS page from FULL differential, not pole order heuristics. Lie homology != Hochschild homology.
AP38: Literature values: record source paper AND convention. DVV != Eichler-Zagier. Derive independently.
AP39: kappa != S_2 for non-Virasoro. Coincide only rank-1. Heis: kappa=k. Vir: kappa=c/2 (ONLY family where kappa=S_2/2). KM: kappa=dim(g)(k+h^v)/(2h^v).
AP41: Prose mechanism != mathematical mechanism. "Residue extracts simple-pole coefficient" WRONG.
AP42: State level of validity explicitly for sophisticated identifications.
AP43: Central object without \begin{definition} -> property list is conjecture, not definition.
AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.
AP60: Tag only genuinely new content ProvedHere. Classical parts ProvedElsewhere with attribution.
AP147: Circular proof routing. When proof chain involves multiple theorems referencing each other, insert ROUTING REMARK citing the primitive non-circular anchor. If none exists, proof is genuinely circular.
AP149: Resolution propagation failure. When conjecture proved/disproved/retracted, ALL references retain old status unless updated: (a) concordance, (b) preface, (c) introduction, (d) standalones, (e) theorem status table, (f) label prefixes, (g) other volumes. All updates SAME session.
AP150: Agent confabulation of mathematical structures. Every claimed multi-step structure verified arrow-by-arrow; each arrow needs independent theorem reference. Any conjectural arrow → structure is conjectural.
AP155: "New invariant" overclaiming. Architectural novelty (new framework) != computational novelty (new numbers). Check Bernard/Felder/Etingof-Varchenko/Calaque-Enriquez-Etingof for recovered invariants.
AP157: Degeneration-dependent "invariants." Formula from specific degeneration is NOT invariant unless degeneration-independence proved. Separating degeneration of genus-2 has ZERO genuinely genus-2 info.

### Computational
AP3/AP10/AP61 (discipline): Compute independently. NEVER pattern-match across occurrences. Every hardcoded expected value MUST have comment citing 2+ independent derivation paths. Bare numbers without derivation trail = future AP10 violations.
AP6: Specify genus, degree, level (convolution vs ambient) for D^2=0, kappa, Theta_A.
AP7: Before universal quantifier, verify proof has no implicit type/genus/level restriction.
AP8: NEVER "self-dual" unqualified. Virasoro self-dual at c=13.
AP14: Koszulness != SC formality. Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k>=3. All standard families Koszul; only class G SC-formal.
AP18: "Entire standard landscape" -> list every family, check each against hypotheses.
AP29/AP31/AP33: H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree independent. F_1=0 does NOT imply F_g=0.
AP30: CohFT flat identity requires vacuum in V. ALWAYS list conditional axioms.
AP36: "implies" proved, "iff" claimed -> write "implies" until converse has independent proof.
AP59: Three invariants: p_max(OPE pole) != k_max(collision depth=p-1) != r_max(shadow depth). betagamma: p=1,k=0,r=4.
AP62: "depends only on dim(g)" = Euler char only. Individual bar cohom dims need full bracket.
AP63: CE(g_-) != chiral bar for multi-gen. Orlik-Solomon form factor. sl_3 chiral H^2=36 vs CE H^2=20.
AP64: CE weight vs PBW degree produce different sequences. Always specify grading.
AP66: Free-field GFs NOT D-finite. Interacting algebras ARE.
AP67: Strong gen != FREE strong gen. W(p) has 4 strong generators; FREE strong gen OPEN.
AP68: PVA slab ghost c != kappa. SVir: kappa=(3c-2)/4. Hierarchy: Sigma_0=13 > Sigma_1=41/4 > Sigma_2=1 > Sigma_4=0.
AP69: tau_shadow = kappa-deformed KdV. Obstruction kappa(kappa-1). Standard KdV only at kappa=1.
AP70: Shadow L^sh has POLES at s=1,2. Negative integers are trivial zeros. F_g <-> L^sh(1-2g) FAILS.
AP71: Shadow kappa != Dyson beta. At c=13, kappa=6.5, not 13.
AP72: W-algebra NOP bar has d^2 != 0. Needs full singular OPE + Orlik-Solomon.
AP73: BV=bar: PROVED G/L, CONDITIONAL C/M (harmonic decoupling).
AP74: False Bernoulli-Dirichlet identity. LHS entire, RHS has poles s=1,2. Verify numerically at s=0.
AP75: Koszulness = PBW degree concentration, NOT conformal weight grading.
AP76: Y_{1,1,1} has c=0, kappa=Psi, NOT c=3.
AP77: Stokes ratio on convergent series spurious. Use direct Pade, not Borel.
AP78: Never conjecture from isolated number-theoretic coincidences.
AP79: W(p) has 4 generators (T + sl_2 triplet), not 2.
AP80: Engine without test file -> verify BOTH exist after every agent completion.
AP133: Catalan index shift. C_n counts binary trees with n+1 leaves (n internal nodes). Verify: count leaves, subtract 1.
AP135: q-expansion coefficients. 1/eta(tau)^r has r-coloured partition numbers p_{-r}(n). r=2: (1,2,5,10,20,...). OEIS lookup before hardcoding.
AP140: Koszul conductor vs local constant. K=c+c' is GLOBAL invariant. Ghost numbers/grading shifts are LOCAL. K_BP=196, not 2.
AP143: DS ghost charge background shift omission. c_ghost(N,f,k) = c(sl_N,k) - c(W_{N,f},k); simplified N*(N-1) OMITS background charge. At N=7: 1722 vs 42. Before any DS ghost formula for N>=3, compute c(sl_N,k) - c(W_{N,f},k) directly from Fateev-Lukyanov.
AP178: S_4 large-c asymptotic off by factor 5. 10/[c(5c+22)] ~ 2/c^2 at large c, NOT 2/(5c^2). Counter: substitute c=100 and verify numerically.

### Empirical (AP116-AP186)
AP116: sum_{j=a}^{b}: substitute smallest index. H_N=sum_{j=1}^{N}, NOT N-1. Off-by-one = #1 error.
AP117: Connection 1-form = r(z)dz, NOT d log(z). KZ=sum r_{ij} dz_{ij}. Arnold d log(z_i-z_j) is bar coefficient, not connection.
AP118: Genus-1 scalar collapse. (Im Omega)^{-1} scalar at g=1, matrix at g>=2. Write in full matrix form; verify at g=2.
AP119: Before Borel: verify Gevrey-1 (factorial divergence). If |F_{g+1}/F_g|→const, series is Gevrey-0; use direct Pade.
AP120: Cauchy = 1/(2πi), NOT 1/(2π). Verify F_1=κ/24.
AP121: In LaTeX, NEVER Markdown (`29`→$29$, **bold**→\textbf, _italic_→\emph). Grep backticks after every write.
AP122: Test tolerance relative, not absolute. abs(computed-expected)/abs(expected) < rtol.
AP123: Combinatorial counts verified against known formula/GF BEFORE hardcoding. Genus-2 stable graphs=7 (not 6).
AP129: Ratio a/b most common transcription error is b/a or -b/a. Substitute known value and check NUMBER.
AP130: Objects on fiber (dτ ∈ H^{1,0}(E_τ)) != objects on base (c_1(λ) ∈ H^2(M̄_g)).
AP131: d_gen (finite) != d_alg (∞ for Vir). Always specify WHICH depth.
AP132: B(A)=T^c(s^{-1} Ā), Ā=ker(ε). NOT T^c(s^{-1} A). Mnemonic: bar uses bar A.
AP134: Cohomological amplitude [0,2] (topological) != virtual dimension (arithmetic).
AP137: c_{βγ}(λ)=2(6λ²-6λ+1) vs c_{bc}(λ)=1-3(2λ-1)². VERIFY c_total=0. At λ=1: c_{βγ}=2, c_{bc}=-2.
AP138: At even ||m||=0, [[m,m],f]=0 tautological. Identity [m,[m,f]]=½[[m,m],f] requires ||m|| ODD. Check parity.
AP139: Every variable in displayed equation must be quantified. LHS ⊇ RHS.
AP144: When multiple conventions coexist, BRIDGE IDENTITY stated at every site; boundary behavior checked in EACH.
AP145: Restructuring = O(N) debt. BEFORE: grep all three volumes; AFTER: verify every ref resolves.
AP146: After 100+ agent campaigns, expect follow-up commit for stragglers.
AP151: Convention clash in single file (hbar with/without πi). Counter: grep file for all definitions after any formula.
AP152: "Ordered" on curve = LABELED (non-coinvariant), NOT totally ordered. Total order lives in R. Specify.
AP153: E_3 scope inflation. HDC needs B^Σ(A) as E_2-coalgebra. E_inf input → B^Σ exists → E_3. E_1 input (Yangian) → B^Σ doesn't exist → ordered bar gives only E_2.
AP154: Two E_3 structures: (a) algebraic (HDC on E_2 bar, no conformal vector); (b) topological (Sugawara, conformal vector at non-critical). Identification CONJECTURAL (conj:e3-identification). Topological: PROVED affine KM; CONJECTURAL general. Chain-level may fail class M.
AP156: wp_1 conventions: (a) θ_1'/θ_1 vs (b) Weierstrass ζ_τ=(a)+2η_1*z. DIFFERENT monodromy. Specify.
AP177: S_2=c/12 lambda-bracket confusion. Shadow invariant S_2=κ=c/2 for Vir. c/12=(c/2)/3! is divided-power coefficient. S_2 is convention-INDEPENDENT. Verify any S_r against Vol I census.
AP180: Cross-volume shadow bridge: S_2^{VolI}=κ=c/2=6*S_2^{lambda-bracket}. Most likely S_2^{Vol II} is WRONG.
AP181: pi_3(BU)=0 (Bott periodicity), NOT Z. pi_3(U)=Z confusion. Before pi_k(BX): fiber sequence pi_k(BX)=pi_{k-1}(X); check Bott parity.
AP182: κ_ch=χ(S)/2 applies to Tot(K_S→S). Conifold (Tot(O(-1)²→P^1)) is NOT local surface. Verify geometry.
AP183: McKay quiver of Z_3 = 3 oriented 3-cycles (9 directed arrows), NOT K_{3,3}. K_{a,b} undirected; McKay directed.
AP184: Excision=gluing (B_L⊗_A B_R=B(A), one copy over A); coproduct=splitting (B(A)→B(A)⊗B(A), two copies plain). Verify codomain.
AP185: pi_4(BU)=Z is obstruction GROUP, not guarantee E_2 exists. Nonzero homotopy = potential obstruction, not automatic structure.
AP186: Shallow correction without first-principles investigation. Before any correction, write down first-principles analysis; state correct theorem. Every wrong claim contains seed of correct theorem. Examples: "categorified averaging" wrong but factorization E_1→^Z E_2→^{Sym} E_inf real; "CoHA=bar" wrong but character coincidence reflects SV theorem CoHA=Y^+.

### Operadic-Structural
AP25/AP34/AP50 (four functors): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A (INVERSION, not Koszul duality). Z^der_ch(A)=bulk. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain) != A^! (linear, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."
AP65/AP81-AP85/AP88/AP103/AP104 (operadic): B_P(A)=P^!-coalgebra != BP=cooperad (different levels). Three coalgebras: Lie^c (Harrison/coLie), Sym^c (coshuffle, 2^n terms), T^c (deconcatenation, n+1 terms). Coshuffle != deconcatenation. Factorization coproduct (Sym^c on Ran) != deconcatenation (T^c on ordered); R-matrix descent relates. B_{Com}(A) is coLie, not cocommutative. P^i=cooperad != P^!=(P^i)^v=operad. Cotriple bar != operadic bar. E_1 is PRIMITIVE; modular/symmetric is av-image.
AP86/AP87/AP89-AP93 (SC/promotion): B_{SC}(A) for one-colour ill-formed; SC two-coloured, use promotion A→(A,A). Closed=B_{Com}(A), open=B_{Ass}(A) + mixed sector. SC mixed-sector dim=(k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=κ*ω_g NOT coderivation. Two curvatures: μ_0 (algebra, g=0) vs d_fib^2=κ*ω_g (fiberwise, g>=1). δF_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed).
AP94-AP98/AP100/AP102 (shadow/Hochschild): ChirHoch*(Vir_c) degrees {0,1,2}. NEVER C[Θ]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket NOT ring. av: g^{E_1}→g^mod LOSSY; at deg 2 recovers κ in abelian/scalar; for non-abelian KM gives κ_dp, full κ adds dim(g)/2. C0 fiber-center; C1 Lagrangian eigenspace; C2 shifted symplectic/BV conditional. Scalar κ+κ'=K from C1 + Theorem D not C2. Theorems specify which bar: B^ord, B^Σ, B^Lie.
AP99: K11 Lagrangian CONDITIONAL (perfectness + bar-cobar normal-complex).
AP101: "qi not merely iso on cohomology" tautological. Use "qi of A-inf-algebras" vs "chain qi."
AP127: Migrating `\input{chapter}`: add `\phantomsection\label{}` stubs for EVERY label and grep `\ref{}` pointing to them.
AP128: Engine-test synchronized to same wrong value. NEVER update test expectations from engine output. Derive INDEPENDENTLY. Most dangerous AP10 variant.
AP142: Local-global conflation on curves. "Koszul duality over point = over P^1" FALSE. Three errors: (a) HOMOTOPY RETRACT IS DATA (A^1→point comparison needs retraction/homotopy/transfer); (b) DISK != POINT (formal D thickening carries content; VAs live on D not point); (c) A^1 ALREADY HAS ARNOLD RELATIONS (Conf_n(A^1) has Arnol'd algebra; P^1 adds compactness). Consequences: (i) genus-0 chiral Koszul NOT "just" classical; (ii) "everything new at g>=1" overstated; (iii) fiber over point←D→A^1→P^1→X not studied; (iv) formal disk vs point still needs retraction. Counter: specify WHICH space (point/D/A^1/P^1/X), COMPARISON DATA (retraction/localization/thickening), on-the-nose vs extra-structure, WHAT content each step.
AP159: Four Yangian types: (1) Classical Y_ℏ(g): E_1-top on R. (2) dg-shifted Y^{dg}_ℏ(g): at point/formal disk. (3) Chiral Y(g)^{ch}: E_1-chiral on curve X, D-module. (4) Spectral: factorization on A^1_u. Conflating = type error. Use ^{ch}/^{dg} superscripts.
AP160: Three Hochschild, geometry determines which: (i) Top HH: E_1 → E_2 (Deligne); (ii) Chiral ChirHoch: E_inf-chiral → {0,1,2} (Thm H); (iii) Categorical HH: dg cat → E_2 w/ CY shifted Poisson. Bare "Hochschild" MUST carry qualifier. Conv:three-hochschild in concordance constitutional.
AP161: Five E_1-chiral notions NOT interchangeable: (A) strict ChirAss, (B) A_inf in End^{ch}, (C) EK quantum VA, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}. Each has own derived center. (B)↔(C) on Koszul locus only.
AP162: E_3 requires (a) conformal vector, (b) non-critical level, (c) T(z) Q-exact. At k=-h^v: Sugawara undefined. PROVED affine KM; CONJECTURAL general. Cohomological; class M chain-level open.
AP163: "Lives on R × C" unjustified for E_1-chiral. End^{ch}_A on curve X; SC^{ch,top} bar is coalgebra over PRODUCT operad, NOT factorization algebra on product space. Chiral Deligne-Tamarkin needed.
AP164: Chiral Gerstenhaber != topological Gerstenhaber. Chiral: OPE residues on FM_k(C); topological: little 2-disks. Agree for E_inf via formality; diverge for E_1.
AP169: SC^{ch,top} is GENERIC case; E_3 is special. Most chiral algebras lack conformal vector (Heis, lattice, critical, E_1-chiral, free fields); for these SC^{ch,top} is FINAL answer. Treat as first-class object, multiple presentations.
AP170: Two Yangian definitions: def:e1-chiral-yangian (E_1-factorization + RTT, weaker) vs def:chiral-yangian-datum ((A, S(z), Δ^{ch}, {m_k}) + modular MC tower, stronger). Equivalence OPEN.
AP171: Associator dichotomy. Chiral QG equiv holds "up to Drinfeld associator Φ". COHOMOLOGICAL derived center = ASSOCIATOR-INDEPENDENT (sl_2 proved). COCHAIN-LEVEL = ASSOCIATOR-DEPENDENT. Bar-side (κ, shadow) associator-FREE; cobar/coproduct depend on Φ.
AP172: A^! is SC^!-algebra = (Lie Sklyanin, Ass), NOT SC-algebra. FORBIDDEN: "A^! is an SC-algebra."
AP173: Z^{der}_{ch}(Y(g)^{ch}) NOT computed. Predicted infinite-dim (C[qdet T(u)]). E_1 input: only E_2, not E_3.
AP174: Chiral QG equiv proved abstractly on Koszul locus. Concrete: sl_2 Yangian + affine KM only. Elliptic partial; toroidal absent.
AP175: Pentagon of equivalences is a STAR. Five SC presentations (operadic/Koszul/factorization/BV-BRST/convolution) route through operadic hub. Three direct links: Koszul-BV, BV-Convolution, Factorization-Convolution.
AP176: CONSTITUTIONAL — "arity" BANNED. "Degree" universal for bar grading, operadic input count, tree vertex valence, Stasheff identity level, SC mixed sector params, cooperad/operad component indices, endomorphism operad components, brace insertion count. NEVER reintroduce "arity." Grep `grep -rn '\barity\b' chapters/ appendices/ standalone/` must return ZERO hits.
AP179: Graph vertex valence context-dependent. Graph: "degree"; operad: "arity" (BANNED per AP176; use "valence"). For vertices carrying operadic ell_k, use "valence."

### Label / Prose / Scope
AP5: Grep ALL THREE volumes for variants (~/chiral-bar-cobar, ~/chiral-bar-cobar-vol2, ~/calabi-yau-quantum-groups) after EVERY correction.
AP12: When proving a claim, grep entire manuscript for variants. Update same commit.
AP40: Environment matches tag. Conjectured → `\begin{conjecture}`. ProvedElsewhere → theorem + Remark attribution.
AP105: Heisenberg = abelian KM at level k = abelian CS boundary. SAME OPE J(z)J(w)~k/(z-w)^2. Simple-pole needs ODD generator (symplectic fermion).
AP106: NEVER "This chapter constructs..." Open with PROBLEM (CG deficiency).
AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
AP108: Heis = CG opening, NOT atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
AP109: NEVER list results before proving.
AP110: Each volume's preface tells its OWN story; cross-volume in delineated subsections.
AP111: No "What this chapter proves" blocks. Restructure.
AP112: Never trust stale page counts. Verify against fresh builds.
AP113: See HZ-7.
AP114: Stub chapters (<50 lines, no theorems) → develop or comment out.
AP115: Architectural CLAUDE.md claims must be enacted in .tex. Metadata-source gap is most dangerous AP.
**Prose laws**: no AI slop; no hedging where math clear; no em dashes; no passive-voice hedging; every paragraph forces next; state/prove once; scope always explicit; prior work = one sentence per paper.
AAP1: Grep `antml` or `</invoke>` in .tex after every write.
AAP7: Grep current file before writing a formula that appears elsewhere in same file.

### 732-Agent Adversarial Campaign (AP186-AP233). Full catalogue: `compute/audit/new_antipatterns_wave12_campaign.md`.

AP186-210 (specialized): AP186 ProvedHere-no-proof-block; AP187 orphaned chapters; AP188 empty sections; AP189 dead labels; AP190 hidden imports (cited result doesn't prove claim, 119 findings); AP191 circular proof chains; AP192 scope inflation statement-vs-proof; AP193 biconditional, only forward proved; AP194 curved complex with flat tools (45); AP195 five-object conflation (47); AP196 SC misattribution non-formula; AP197 bare Hochschild (89); AP198 Whitehead lemma semisimple-only; AP199 strong filtration inequality direction; AP200 transfer theorem gap (H*(A) results applied to A); AP201 Baxter constraint not vacuous at λ=0; AP202 coderived element-wise invalid; AP203 class-M harmonic unproved; AP204 genus-0 boundary contradiction; AP205 reflexivity hidden in duality; AP206 object switch mid-proof (Verdier != cobar); AP207 center-side vs bar-side lift missing; AP208 Theorem A Verdier algebra/coalgebra flip; AP209 missing lemma cited; AP210 topologization chain-level vs cohomological.

AP211-224 (new): AP211 test file absent (219); AP212 TODO/FIXME unresolved; AP213 stub chapter false coverage; AP214 cross-volume bridge outdated; AP215 preface advertising stronger than proved; AP216 Koszul (vii) genus-0 scope; AP217 Koszul (viii) ChirHoch freeness overclaim; AP218 SC-formality restricted to metric families; AP219 depth-gap d_alg=2 wrong line; AP220 D^2=0 wrong geometric space; AP221 Gerstenhaber single insertion; AP222 Theorem H config-space collapse unjustified; AP223 Theorem H bar-coalgebra/Koszul-dual conflation; AP224 README scope inflation.

AP225-233 (deep structural): AP225 (CRITICAL) genus-universality gap — all-genera scalar factorization NOT proved; genus-1 unconditional; clutching-uniqueness needed; affects Theorem D; AP226 K_0-class vs scalar (use Chern character); AP227 ProvedHere forwarding ("By Theorem X" is ProvedElsewhere); AP228 anomaly-Koszul dependency inversion; AP229 SC-formality propagation debt (Vol III stale); AP230 genus-1 sufficient claimed all-genera; AP231 draft artifacts in theorem statements; AP232 duality clause overclaiming family scope; AP233 compact/completed comparison gap MC3.

AP234-235 (preface rectification 2026-04-17): AP234 two-Koszul-conductors-same-letter — κ(A)+κ(A^!) (scalar complementarity, family-dependent: 0/13/250/3/98/3) distinct from Trinity K(A)=c+c^!=-c_ghost(BRST) (-k/2dim(g)/26/100/196); related by κ+κ^!=ϱ_A·K with ϱ_N=H_N-1 for principal W_N, ϱ_A=0 for KM/free, ϱ_BP=1/6. The equation κ+κ^!=K (bare, no ϱ) is FALSE for every standard family. Canonical K-values in universal_conductor_K_platonic.tex:795-821 and higher_genus_complementarity.tex:3015-3120. Grep trigger: any `K(Vir)=13` or `K=250/3 for W_3`. Counter: cross-check K at self-dual c=13 — correct is K=26, not 13. Confusion pattern #218 (cache). AP235 quaternitomy/quadrichotomy drift — "quadrichotomy" is canonical (matches thm:quadrichotomy, chap:shadow-quadrichotomy-platonic); "quaternitomy" is invented hybrid, drifts across preface, working_notes, part-introductions. Grep `quaternitomy` after any write naming the G/L/C/M partition. Confusion pattern #219 (cache).

AP236 (bar_construction.tex rectification 2026-04-17): blacklist-slug leakage into typeset parenthetical. `/B\d+` identifiers from the Wrong-Formulas Blacklist leak into manuscript `\textup{(}...\textup{)}` annotations during agent edits (e.g. `\textup{(}/B49; treated in Chapter~X\textup{)}`). A reader sees a non-existent citation; the slug rots with every blacklist renumbering. Constitutional metadata hygiene violation. Grep `\\textup\{\(\}\s*\/B\d+|(\s*\/B\d+;` before every commit touching `.tex`. Healing: delete the slug; keep only the mathematical cross-reference to the target chapter. Companion symptom: orphaned `\textup{(}\textup{)}` empty parentheticals left behind when a macro-resolved reference is deleted between the delimiters — grep `\\textup\{\(\}\\textup\{\)\}`. Confusion pattern #221 (cache).

**WARNING (AP225):** Theorem D all-genera may rest on unproved universality step. Genus-1 obs_1=κ*λ_1 unconditional. All-genera requires (a) clutching-uniqueness (not yet proved), or (b) GRR (H04 sketched not inscribed). Until resolved: state genus-1 unconditional, all-genera conditional.

New wrong formulas B74-B78 in Blacklist above. New failure modes (FM35-FM38, AP42 variants): rate-limit cascade (batch<=5), timeout on >15K line files, "vacuous constraint" confabulation, circular proof chain detection needs DAG tracing.

## Regression Safeguards (non-AP)

RS-3: Physics IS the homotopy type, not a "bridge." Costello-Gaiotto-Dimofte are substance.
RS-4: Costello/Dimofte/Gaiotto content in mathematical core, not "connections" chapters.
RS-9: The slab is a bimodule, NOT a Swiss-cheese disk. Two boundary components.
RS-10: Single-pass agent work without audit FORBIDDEN. Beilinson loop mandatory.
RS-12: The programme is THREE volumes.
RS-13: In Vol II, gravity is the CLIMAX (Part VI).
RS-14: Introduction orients, Overture instantiates.
RS-15: Koszul programme before higher_genus in dependency DAG.
RS-19: Preface is complete survey. Save before compressing.

## Agent Anti-Patterns

AAP2: Terminology rename ATOMIC across all three volumes in single session.
AAP3: Formula implemented ONCE in canonical module, import everywhere.
AAP4: \begin{proof} only after theorem/prop/lemma with ProvedHere. Use Remark[Evidence] for conjectures.
AAP5: Build-artifact commits batched with content. Never standalone artifact commits.
AAP6: Search ALL THREE volumes before downgrading a status tag.
AAP8: README claims independently verifiable by test suite.
AAP9: Wait for ALL agents to finish before launching new batch.
AAP10: After agent completion, verify BOTH engine AND test files exist.
AAP11: Every hardcoded expected value derivable by 2+ independent paths.
AAP12: Asymptotic tolerance proportional to 1/log(N) or verified by two methods.
AAP13: NEVER downgrade model without user permission. Wait and retry on rate limit.
AAP14: Unique branch name per agent.
AAP15: Serialize builds or use isolated worktrees. Parallel pdflatex kills.
AAP16: git stash FORBIDDEN. Use git diff > patch.diff + git apply.
AAP17: Verify edits via git diff, not agent narrative.
AAP18: Confabulating operadic theory -> compute or cite (Loday-Vallette, Vallette, Livernet). NEVER analogize.

## Pre-Edit Verification Protocol

Fill-in-the-blank templates mandatory BEFORE writing listed formula classes. Filling out a template IS the verification. Source: pre_edit_verification_protocol_wave12.md (PE-1 through PE-12).

Invocation protocol: before every Edit touching a trigger pattern, write the relevant template as a fenced block in the reply text (NOT in .tex), fill it in, end with `verdict: ACCEPT`, THEN invoke Edit. If any `match?` is `N` or required source blank, `verdict: REJECT` and re-draft.

Eight highest-priority templates follow. Remaining four (PE-3, PE-6, PE-9, PE-12) in source draft.

**PE-1. r-matrix write** (AP126, AP141, AP19, AP20)

Trigger: any r-matrix formula or reference to `r(z)`, `r_{ij}`, classical r-matrix.

```
## PRE-EDIT: r-matrix
family:                    [Heis / affine KM / Vir / W_N / lattice / Yangian / other]
r(z) written:              [full formula with level prefix]
level parameter symbol:    [k / k+h^v / hbar / c / Psi]
OPE pole order p:          [_]
r-matrix pole order p-1:   [_]              # AP19: d log absorbs one pole
convention:                [trace-form k*Omega/z / KZ Omega/((k+h^v)*z)]
AP126 check (trace-form):  r(z)|_{k=0} = [_]    expected: 0
  (KZ convention: k=0 gives Omega/(h^v*z) != 0 for non-abelian g; this is correct)
match?                     [Y/N]            # must be Y for trace-form; N/A for KZ non-abelian
AP141 grep check:          bare \Omega/z instances in edit scope: [N]
bare \Omega/z allowed?     N
critical-level check (KM): r(z)|_{k=-h^v} = [_]    (trace-form: finite; KZ: diverges)
source:                    [landscape_census.tex:LINE / compute/module.py]
verdict:                   [ACCEPT / REJECT]
```

**PE-2. kappa formula write** (AP1, AP9, AP24, AP39, AP48, AP136)

Trigger: any formula involving kappa or variants (kappa_eff, kappa(B), kappa_ch, kappa_BKM, kappa_cat, kappa_fiber).

```
## PRE-EDIT: kappa
family:                    [Heis / Vir / KM / W_N / bc / betagamma / svir / other]
kappa formula written:     [_]
census citation:           landscape_census.tex:LINE, kappa^{family} = [_]
match?                     [Y/N]            # STOP if N
AP39 uniqueness: is kappa = S_2?  [Y/N]
  if Y, is family Vir?     [Y/N]            # only Vir has kappa = S_2/2 = c/2
evaluation paths:
  at k=0:                  [_]  expected [_]
  at k=-h^v (KM):          [_]  expected 0
  at c=13 (Vir):           [_]  expected 13/2
AP136 boundary (W_N):      formula uses [H_N / H_{N-1} / H_N - 1]
  substitute N=2:          [_]  expected c/2 (W_2 = Vir)
wrong variants avoided:
  NOT kappa(Vir) = c       NOT kappa(W_N) = c*H_{N-1}
  NOT kappa(Heis) = k/2    NOT kappa(KM) = (k+h^v)/(2h^v) (missing dim(g))
verdict:                   [ACCEPT / REJECT]
```

**PE-4. bar complex formula** (AP132, AP22, AP23, AP44)

Trigger: `B(A)`, `T^c(...)`, any bar-construction formula, any desuspension.

```
## PRE-EDIT: bar complex
object written:            B(A) = [_]
T^c argument:              [s^{-1} \bar A / s^{-1} A / s \bar A / bare A]
AP132 augmentation:        \bar A = ker(epsilon) present?  [Y/N]   # must be Y
AP22 desuspension:         |s^{-1} v| = |v| [-1 / +1]              # must be -1
s^{-1} (NOT bare s) used?  [Y/N]                                   # must be Y
coproduct type:            [deconcatenation T^c / coshuffle Sym^c / coLie]
match to intended bar?     [B^ord -> deconc / B^Sigma -> coshuffle / B^Lie -> coLie]
grading:                   cohomological |d|=+1?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

**PE-5. Vol III kappa write** (AP113)

Trigger: ANY kappa occurrence in `~/calabi-yau-quantum-groups/**/*.tex`. Zero tolerance.

```
## PRE-EDIT: Vol III kappa
subscript written:         [kappa_ch / kappa_cat / kappa_BKM / kappa_fiber / OTHER]
subscript present?         [Y/N]   # must be Y; bare kappa FORBIDDEN
subscript justification:   [chiral shadow / categorified / BKM / fiber correction]
census citation:           Vol III landscape_census_cy.tex:LINE
grep BEFORE write:         bare `\kappa[^_]` hits: [N]
grep AFTER write:          bare `\kappa[^_]` hits: [N]
delta = 0?                 [Y/N]   # must be Y
verdict:                   [ACCEPT / REJECT]
```

**PE-7. Label creation** (AP124, AP125)

Trigger: any `\label{...}` write.

```
## PRE-EDIT: label
environment:               [theorem / proposition / conjecture / definition / remark / lemma]
label written:             \label{prefix:name}
prefix match (AP125):      theorem->thm, prop->prop, conj->conj, def->def, rem->rem, lem->lem
match?                     [Y/N]   # must be Y
AP124 duplicate check (grep all three volumes):
  Vol I matches:           [N]
  Vol II matches:          [N]
  Vol III matches:         [N]
  total BEFORE:            [N]
  total AFTER:             [N]
  delta = 1?               [Y/N]   # must be Y
if duplicate, rename with volume suffix and update all \ref
verdict:                   [ACCEPT / REJECT]
```

**PE-8. Cross-volume formula** (AP5, AP3)

Trigger: any formula shared across volumes (kappa, r-matrix, Theta_A, bar differential, connection 1-form, complementarity).

```
## PRE-EDIT: cross-volume formula
formula:                   [_]
Vol I grep:                [hits, canonical form]
Vol II grep:               [hits, canonical form]
Vol III grep:              [hits, canonical form]
consistent across volumes? [Y/N]
if inconsistent:
  canonical volume:        [Vol I / II / III]
  other volumes updated same session?  [Y/N]  # must be Y (AP5)
convention conversion?     [OPE(I) -> lambda(II) / motivic(III) / NA]
conversion applied?        [Y/N/NA]
verdict:                   [ACCEPT / REJECT]
```

**PE-10. Scope quantifier** (AP6, AP7, AP32, AP139)

Trigger: any theorem statement, any obs_g / F_g / lambda_g formula, any universal quantifier.

```
## PRE-EDIT: scope quantifier
statement:                 [_]
genus:                     [g=0 / g=1 / g>=2 / all g / UNSPECIFIED -> REJECT]
degree:                     [n=_ / all n / UNSPECIFIED -> REJECT]
level:                     [convolution M-bar_{g,n} / ambient Mok25 log FM / both / NA]
AP32 weight tag:           [(UNIFORM-WEIGHT) / (ALL-WEIGHT + delta F_g^cross) / NA]
tagged in statement?       [Y/N]  # must be Y for any g>=2 claim
AP139 free-variable audit:
  variables on LHS:        {_}
  variables on RHS:        {_}
  LHS superset RHS?        [Y/N]  # if N, bind the free variable
AP36 implies vs iff:       [implies / iff]
  if iff, converse proved in same theorem?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

**PE-11. Differential form type** (AP117, AP27, AP130)

Trigger: any write of a connection 1-form, KZ connection, Arnold form, bar propagator.

```
## PRE-EDIT: differential form
what:                      [connection 1-form / bar propagator / Arnold form / KZ / other]
form written:              [_]
expected type:
  connection 1-form: r(z) dz  (NOT d log)
  KZ:                sum r_{ij} dz_{ij}
  Arnold form:       d log(z_i - z_j)  (bar coefficient, NOT connection)
  bar propagator:    d log E(z,w)  (weight 1 ALWAYS, AP27)
match?                     [Y/N]
AP27 propagator weight:    1?  [Y/N]
AP117 d log check:         if d log appears, Arnold-form context? [Y/N]
space the form lives on:   [fiber Sigma_g / base M-bar_{g,n} / FM_n(X) / Ran(X)]
AP130 fiber-base:          object on fiber vs class on base correctly distinguished? [Y/N]
verdict:                   [ACCEPT / REJECT]
```

Refusal criteria: reject own edit if any `match?` = N, any blank source, any `FORBIDDEN` ticked, grep delta mismatch. On reject: re-draft, re-fill, proceed only when `verdict: ACCEPT`.

Remaining templates PE-3 (complementarity), PE-6 (exceptional dimensions), PE-9 (summation boundary), PE-12 (prose hygiene) in `compute/audit/pre_edit_verification_protocol_wave12.md`.

## Structural Facts

**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).

**Convolution**: dg Lie Conv_str is strict model of L-inf Conv_inf. MC moduli coincide. Full L-inf needed for transfer/formality/gauge equivalence.

**E_1 primacy**: B^ord is the primitive (Stasheff). av: g^{E_1} → g^mod lossy Sigma_n-coinvariant projection. At degree 2, av(r(z)) recovers kappa in the abelian and scalar families; for non-abelian affine KM gives kappa_dp and the full kappa adds dim(g)/2. All standard chiral algebras are E_inf (local); E_1=nonlocal (Yangian, EK quantum VA). NEVER "E_inf means no OPE poles."

**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).

## Architecture

**Vol I**: Introduction + Overture (Heisenberg CG opening, unnumbered) + Part I (Bar Complex: Thms A-D+H, 12 Koszul equivs) + Part II (Characteristic Datum: shadow tower, G/L/C/M/M*/W, higher-genus, E_1 modular) + Part III (Standard Landscape: all families, census) + Part IV (Physics Bridges: E_n, factorization envelopes, derived Langlands) + Part V (Seven Faces of r(z): F1 bar-cobar twisting, F2 DNP25 line-operator, F3 Khan-Zeng PVA, F4 Gaiotto-Zeng sphere Hamiltonians, F5 Drinfeld Yangian, F6 Sklyanin/STS83, F7 FFR94 Gaudin) + Part VI (Frontier) + Appendices.

**Vol II** (~1,749pp): SC^{ch,top} bar differential = holomorphic factorization on C, coproduct = topological factorization on R. Seven parts: I(Open Primitive) II(E_1 Core) III(Seven Faces) IV(Char Datum) V(HT Landscape) VI(3D Quantum Gravity = CLIMAX) VII(Frontier). See Vol II CLAUDE.md and notes/cross_volume_aps.md for V2-AP* catalog.

**Vol III** (~693pp): CY → chiral functor Phi. ~34,000 tests, ~460 engines. 10 proofs at publication standard. Clean build. Seven parts: I(Foundations) II(CY-to-Chiral Functor) III(E_n Hierarchy) IV(K3 Yangian) V(CY Landscape) VI(Seven Faces r_CY) VII(Frontiers). 4 stub chapters. kappa subscripts MANDATORY. CY-A_3 PROVED (inf-cat). K3 abelian Yangian PROVED. ZTE T COMPUTED. kappa_BKM = c_N(0)/2 universal. Class M E_3 bar dim = 6^g. Shadow tower through m_8 (160 tests, S_8=4144720/19683). Mock modular K3: THEOREM at d=2. CY-D dimension-stratified. See Vol III CLAUDE.md and notes/cross_volume_aps.md for AP-CY1..AP-CY61.

## Writing Standard

Channel: Gelfand (inevitability), Beilinson (falsification), Drinfeld (unifying principle), Kazhdan (compression), Etingof (clarity), Polyakov (physics=theorem), Nekrasov (seamless passage), Kapranov (higher structure IS math), Ginzburg (every object solves a problem), Costello (factorization), Gaiotto (dualities compute), Witten (physical insight precedes proof). **Convergent loop mandatory**: WRITE → REIMAGINE (Gelfand/Beilinson/Drinfeld) → REWRITE from scratch → BEILINSON AUDIT (adversarial) → REIMAGINE AGAIN → REWRITE AGAIN → CONVERGE (zero findings >= MODERATE). Preface/intro: 3+ iterations. Chapter openings: 2+. **CG structural moves**: deficiency opening, unique survivor, instant computation, forced transition, decomposition table, dichotomy, sentence-as-theorem.

## Skills

### `/chriss-ginzburg-rectify` — MANDATORY execution protocol (CONSTITUTIONAL)

When `/chriss-ginzburg-rectify <file>` is invoked, you MUST analyse the WHOLE file, chunk by chunk, linearly progressing from start to finish, with SMALL chunk size (~50 lines). No exceptions.

- **Whole-file coverage is non-negotiable.** Do not declare convergence on a partial sweep. Do not skip to "hot spots" and ignore the rest. Do not skim large regions via screening-grep in lieu of chunk-by-chunk audit. The file is not done until every line from 1 to EOF has passed the five-gate check.
- **Linear order.** Start at line 1 (or at the resume cursor if the queue entry is `[~]`), advance monotonically. Never skip forward. A chunk-N issue discovered from chunk-(N+k) context propagates back to chunk N; fix in place, continue forward.
- **Small chunks.** ~50 lines per chunk is the default. The user is watching and wants tight verdicts. 100 lines is the absolute maximum. Larger chunks dilute the audit (Gate 2 define-before-use and Gate 3 motivation cannot be checked reliably in 200-line blocks).
- **Budget-rule partial is legitimate, shallow-screen is not.** If the file is large (>3000 lines) and the session budget runs out, mark `[~]` with a resume cursor `% RESUME-FROM: <line/label>` and commit partial progress. This is fine. What is NOT fine: declaring `[x]` after editing only a few "obvious" spots and claiming the rest was "already clean" based on a grep pass. The queue file records what counts as done; only the full five-phase sweep counts.
- **If the skill was invoked without a file argument or on a non-existent path, STOP and ask.** Do not silently rectify an unrelated file.

Why: prior sessions have cut corners by running a lightweight `rg` screen for obvious prose slop and declaring "CONVERGED (0 edits)". That screen misses formula bugs, define-before-use violations, unmotivated definitions, operadic conflations, scope inflations, and circular-proof routings that the five-gate audit is designed to catch. Every shortcut becomes a future AP. The only reliable protection is linear whole-file coverage.

### Skill index

```
/build                      Build all three volumes, tests, census
/audit [target]             Deep Beilinson audit (6 hostile examiners)
/chriss-ginzburg-rectify [file]  Full 5-phase CG + Beilinson rectification (canonical) — WHOLE FILE, chunk by chunk, linear, small chunks
/rectify-all                Rectification across all chapters, all volumes, parallel tiers
/research-swarm [topic]     Launch 30+ research agents on frontier
/verify [claim]             Multi-path verification (3+ independent paths)
/propagate [pattern]        Cross-volume AP5 propagation check
/compute-engine [name]      Scaffold compute engine with multi-path tests
/beilinson-swarm            Beilinson rectification swarm across all chapters
/rectify [file]             Beilinson rectification loop (lighter than CG)
/beilinson-rectify [file]   CG fortification + rectification (v1)
/chriss-ginzburg-rectify-v1 [file]  CG rectification v1 (superseded)
```

RS-1,2,5,6,7,8,11,16,17,18,20 merged into corresponding APs. AP16 superseded by AP27.

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
cd ~/calabi-yau-quantum-groups && make fast                       # Vol III
make test                                                         # Fast tests
make test-full                                                    # All tests (~119K)
python3 scripts/generate_metadata.py                              # Census
```

CAUTION: Watcher spawns competing pdflatex; always kill before builds.

## Session Protocol

1. Read this file. 2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. 3. Tests: `make test`. 4. `git log --oneline -10`. 5. Read .tex source before any edit (never from memory). 6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5). 7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1). 8. Apply convergent writing loop to all prose. 9. Session end: build all three volumes, run tests, summarize errors by class. 10. Before first Edit, read the HOT ZONE (HZ-1 through HZ-10) and run Pre-Edit Verification Protocol mental check: is the pending edit touching an r-matrix, kappa, bar complex, label, Vol III kappa, cross-volume formula, scope quantifier, or differential form? If yes, fill the corresponding PE-1..PE-12 template as a fenced block in the reply BEFORE invoking Edit, ending with `verdict: ACCEPT`.

Details: FRONTIER.md (research programme status), MEMORY.md (session history), concordance.tex (constitution), notes/cross_volume_aps.md (Vol II/III AP catalog), notes/true_formula_census.md (full C1-C31).

## LaTeX

All macros in main.tex preamble. NEVER \newcommand in chapters (use \providecommand). Memoir class, EB Garamond (newtxmath + ebgaramond). Tags: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic. Label everything with \label{def:}, \label{thm:}. Cross-reference with \ref. Do not add packages without checking compatibility. Do not create new .tex files when content belongs in existing chapters.

## Vol III 6d hCS Session Cross-Awareness (2026-04-12/13)

Feeds back into Vol I. AP-CY23-34 detailed in notes/cross_volume_aps.md. Capsule: AP-CY23 E_1-chiral bialgebra is correct Hopf home (B^ord preserves R-matrix; B^Σ kills Hopf); AP-CY24 docstring confabulation; AP-CY25 R=(id⊗S)∘Δ(1) WRONG, use half-braiding; AP-CY26 σ_2 even under h_i→-h_i (k^!=-k from Shapovalov); AP-CY27 sandbox non-persistence (verify with ls); AP-CY28 pole-unsafe test points (avoid z=±h_i); AP-CY29 wrong-repo writes; AP-CY30 factored != solved (YBE does NOT imply ZTE); AP-CY31 spectral z != worldsheet z; AP-CY32 reorganisation != bypass; AP-CY33 chain-level != rational (E_3 collapses under formality); AP-CY34 total {b,B^{(2)}}=0 via Costello TCFT but individual {b_k,B^{(2)}}!=0.

Key Vol I infrastructure results: Shadow tower S_k = A_∞ coproduct correction δ^{(k)} PROVED; shadow-Feynman L-loop=S_{L+1}. ZTE fails for Yang R-matrix at O(κ²); E_3 nontrivial beyond E_2; S^{corr} EXISTS. E_3 bar cohomology: class L=(1+t)^{3g}=2^{3g}; class C=2^{3g}; class M=6^g (Kunneth, chain-level P(q)^{6g}). Universal coproduct Δ_z(e_s)=Σ C(N_R-b,k) z^k e_a^L·e_b^R (all spins). Conductors: G/L ρ_K=0; M(Vir) 13; K3×E 0. Chiral CE: B(U^ch(L))=CE_*(L) PROVED. κ_BKM=c_N(0)/2 universal (Borcherds weight); naive κ_ch+χ(O_fiber) is coincidence for K3×E. CY-A_3 PROVED in inf-categorical framework; chain-level [m_3,B^{(2)}]!=0 is NOT obstruction; Obs_Ainf=0 UNIVERSALLY via Costello TCFT.
See ~/calabi-yau-quantum-groups/FRONTIER.md F13-F24 and CLAUDE.md for full details.

## Alternative Proofs Secured (2026-04-13)

Every main theorem has at least TWO independent proof paths:

| Theorem | Primary | Alternative |
|---------|---------|-------------|
| A | Twisting morphisms + filtered comparison | Lurie inf-cat nerve-realization (H01) |
| B | Bar filtration spectral sequence | Keller deformation + Kontsevich formality (H02) |
| C | Fiber bar + eigenspace decomp | PTVV shifted symplectic (H03) |
| D | Shadow tower + genus universality | GRR on universal curve (H04) |
| H | Bar-Hochschild comparison | Deformation-theoretic dimensional analysis (H05) |
| MC2 | Recursive inverse limit | KS scattering diagram (H06) |
| MC5 | Harmonic mechanism + coacyclic | Operadic Koszul duality (H07) |
| Topol | Sugawara [Q,G]=T | CFG factorization homology (H08) |
| SC-formal | Shadow tower truncation | Operadic tower truncation (H11) |
| Depth gap | MC relation at degree 4 | Shadow Lie Jacobi (H10) |
| Compl K | Fiber-center + Theorem D | Index theory / Euler characteristic (H12) |

Condition removal: uniform-weight (H13), Koszul locus (H14), chain-level topol (H15), perfectness C1 (H17).

## Platonic Ideal Roadmap (2026-04-13)

**Unconditional (high confidence):** Thms A (fixed-curve), B (on-locus), C0 (D^co), C1 (g>=1), D (non-circular; but see AP225), H, MC1, MC2, MC4, SC-formality, depth gap, D^2=0, Theta_A, ChirHoch^1, 10 Koszul equivs, Verlinde recovery, ker(av), Miura coefficient, critical level jump, E_3 identification (simple g), chiral QG equiv, gl_N chiral QG.

**Conditional (genuine mathematical restrictions):** C2 (uniform-weight), MC3 type-A (Baxter b=a-1/2), MC4 resonance (transfer comparison), MC5 chain-level (class M false), Koszul (vii) multi-weight (genus-0), Koszul (viii) freeness (Massey vanishing).

**Conjectural:** Topologization chain-level original complex (A-inf coherence), topologization general (non-KM), Theorem A modular-family (relative Ran base-change), off-locus chain qi (beyond class G/L).

**Open frontier (status 2026-04-16 reconstitution):** All five previously-deepest frontiers CLOSED or substantially REDUCED: (1) chain-level E_3 on original complex — CLOSED by Vol II `e_infinity_topologization.tex` (`thm:iterated-sugawara-construction`, `thm:e-infinity-topologization-ladder`) and `chiral_higher_deligne.tex` (`thm:chiral-higher-deligne`); (2) MC5 chain-level class M — CLOSED weight-completed (`prop:bv-bar-class-m-weight-completed`; direct-sum class M genuinely false, correct scope); (3) modular-family Theorem A over M̄_{g,n} — reduced via Thm A^{∞,2} properad equivalence (Vol I `theorem_A_infinity_2.tex`); (4) topologization for general chiral with conformal vector — CLOSED by iterated Sugawara tower giving E_{k+2}-top for depth-k stress tower (Vol II `e_infinity_topologization.tex`); (5) chiral coproduct for non-gauge-theoretic families — CLOSED by unified `Q_g^{k,f,μ}` theorem covering nine specialization fibres (Vol II `unified_chiral_quantum_group.tex`). The sole remaining genuine frontier of the 2026-04-16 wave, `conj:periodic-cdg` for admissible KL (FM251), was CLOSED by Vol I `periodic_cdg_admissible.tex` (`thm:periodic-cdg-is-koszul-compatible`).

**Beilinson-rectified open frontiers (2026-04-17 audit, surfaced AFTER the 2026-04-16 wave):**
- **W(p) triplet tempering** — the Vol II commit `a5640de` inscription RETRACTED `thm:tempered-stratum-contains-wp` from ProvedHere to Conjectured. The Zhu-bounded-Massey proof chain fails: Gurarie 1993 (arXiv:hep-th/9303160) and Flohr 1996 (arXiv:hep-th/9605151) construct logarithmic-CFT amplitudes with unbounded Massey products despite finite-dim Zhu. The CORRECT tempered scope is: principal + non-logarithmic + non-minimal standard landscape; W(p) is open pending Adamović-Milas character-amplitude bound.
- **Non-tempered stratum OVERCLAIM** — the programme-climax statement "non-tempered stratum is EMPTY on the C_2-cofinite standard landscape" is SCOPE-QUALIFIED: emptiness holds on the non-logarithmic subset (Virasoro, W_N, all Schellekens, Monster, irrational cosets). Logarithmic W(p) remains open.
- **CY-C pentagon invariant** — Vol III commit `cade61c` healed the pentagon stratification `{3, 12, 24}` from `κ_ch^{R_i}` to `ρ^{R_i}` (generator-lattice rank). Category error: κ_ch is route-independent = 0 for K3×E by Hodge supertrace; the stratification is an algebraic invariant orthogonal to κ_ch.
- **Kummer-irregular prime labelling** — Vol I commit `9668336` retracted primes 1423, 3067, 23, 43, 419 from the Kummer-irregular label (primary-source Bernoulli witness search found no witness). These primes still appear in S_r numerators as Riccati-arithmetic characteristic primes, NOT Kummer-arithmetic. Corrected Tier-3 emergence: {37, 691, 811}; 3067 dropped.
- **β_N exact closed form** — RESOLVED (Vol II `chapters/theory/beta_N_closed_form_all_platonic.tex`, `thm:beta-N-closed-form-proved-all-N`): β_N = 12(H_N - 1) = sum_{s=2}^{N} 12/s (per-spin-s lane contribution). Both prior candidates RULED OUT at N=4: (N+1)(N+2)/2 predicts 15; N²-N+4 predicts 16; proved value is 13. Closed form β_N is RATIONAL (not integer) for N ≥ 5; β_5 = 77/5, β_6 = 87/5. No longer an open frontier.
- **Super-complementarity canonical pairing** — the `κ + κ^! = max(m,n)` identity for super-Yangians scopes to sub-Sugawara line; two pairings (super-trace vs Berezinian) coexist without programme-level canonicalisation. Verdier pairing inscription pending.

The Beilinson audit inscribed `notes/rectification_map_beilinson_audit.md` (926 lines) with full verdicts and heal paths; the post-audit priority order places the climax-rewrite and preface-refresh tasks LAST to prevent propagation of unverified closures.

**Recovery infrastructure:** `scripts/resume_failed.py`, `scripts/campaign_dashboard.py`, 9 campaign scripts.

## Geometric vs Algebraic Model Conflations (AP-CY62--AP-CY67)

Migrated 2026-04-16 to `notes/cross_volume_aps.md` (full AP-CY62..67 entries, all triggers, ramification guards). Vol I agents MUST read that file before edits touching ChirHoch, End^ch_A, BZFN, spectral parameters, FM_k(C), or geometric-vs-algebraic chiral model claims.

Operational capsule (sufficient if cross_volume_aps not loaded):
- AP-CY62: specify "geometric (FM)" vs "algebraic (bar/operadic)" for any chain-level C^*_ch(A,A).
- AP-CY63: "chiral endomorphism operad on FM_k(C)" FIRES (End^ch is algebraic, not on FM).
- AP-CY64: HH*(Weyl)=1-dim; "Theorem H has no THH analogue" is FALSE; the unbounded object is Gel'fand-Fuchs, not THH.
- AP-CY65: Yangian Y(g) has spectral parameters in its Drinfeld centre via evaluation modules; "topological center has no spectral parameters" is FALSE.
- AP-CY66: BZFN uses SAME S; two centres come from two DIFFERENT algebras (chiral A vs A_mode), not from varying S.
- AP-CY67: spectral parameters are formal algebraic variables in End^ch_A; FM_k(C) enters via comparison, not definition.

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. No co-authored-by, no generated-by, no AI attribution anywhere. Constitution: concordance.tex. git stash FORBIDDEN (AAP16).
