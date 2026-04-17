# Wave Supervisory — Vol I main.tex Part Re-architecture around the Four Pillars

**Date.** 2026-04-16. **Author.** Raeez Lorgat.
**Mode.** Read-only supervisory draft. No edits to `main.tex`, no commits, no test runs. Russian-school delivery (Gelfand, Etingof, Kazhdan, Bezrukavnikov, Polyakov, Nekrasov, Kapranov, Beilinson--Drinfeld, Witten, Costello, Gaiotto). Chriss--Ginzburg discipline: every Part-opener begins with a Platonic theorem stated in one display, never a "this part discusses" sentence.

**Companion files.** `PLATONIC_MANIFESTO.md` (synthesis), `MASTER_PUNCH_LIST.md` (V5--V19), `wave14_reconstitute_theoremA.md` (V5 Koszul Reflection), `wave14_reconstitute_kappa_conductor.md` (V6 BRST Ghost Identity), `wave14_reconstitute_climax_theorem.md` (V7 Climax), `wave14_reconstitute_shadow_tower.md` (V8 Shadow Quadrichotomy), `wave14_reconstitute_chiral_hochschild_trinity.md` (V19 single-colour Pentagon), `wave11_main_global.md` (HU-W11g.5/6).

This is the second attempt; the first was rate-limited mid-flight. The task is the structural decision that the manifesto names but does not execute: re-architect the Vol I Part structure so that the **four Platonic pillars** (V5 Koszul Reflection / V6 κ-Conductor / V7 Climax / V8 Shadow Quadrichotomy) are the **named, foregrounded organising principle** of Vol I, not a thematic gloss laid over a 2025-vintage 6-Part skeleton.

---

## §1. Current 6-Part state (2026-04-16)

The Vol I `main.tex` (1956 lines, sha-stamped 2026-04-13 19:44) declares **one unnumbered Overture and six numbered Parts**, all from inside `main.tex` itself (no `\part{}` leakage into chapter files; verified Wave 11 §1.2):

| #        | Line | Title                                       | Label                       | Annals build? |
|----------|-----:|---------------------------------------------|-----------------------------|---------------|
| Overture | 871  | (unnumbered `\part*{Overture}`)             | none (TOC line only)        | yes           |
| I        | 899  | The Bar Complex                             | `part:bar-complex`          | yes           |
| II       | 1088 | The Characteristic Datum                    | `part:characteristic-datum` | yes           |
| III      | 1182 | The Standard Landscape                      | `part:standard-landscape`   | yes           |
| IV       | 1390 | Physics Bridges                             | `part:physics-bridges`      | yes           |
| V        | 1511 | The Seven Faces of the Collision Residue    | `part:seven-faces`          | **archive only** |
| VI       | 1544 | The Frontier                                | `part:v1-frontier`          | yes (mostly)  |

Plus the "**E_1 Wing**" header (`main.tex` L1136--1147), an absorbed pseudo-Part that lost its own `\part{}` declaration in an earlier promotion and now floats inside Part II without a numbered banner.

**Stale 3-Part bucketing.** The auto-generated `standalone/theorem_index.tex` (4303 lines, last regenerated 2026-04-13) summarises the 2262 indexed entries under a *different* 3-bucket scheme:

```
Frame                  19
Part I: Theory       1125
Part II: Examples     713
Part III: Connections 405
```

This is the **directory bucketing** (`chapters/{frame, theory, examples, connections}`), promoted to "Part" labels that **do not exist in `main.tex`**. The rebucketing was honest in 2025 when Vol I had three thematic parts; it has been wrong since the 2026 6-Part re-architecture and no reader of the index can map "Part I: Theory" onto the real `part:bar-complex` / `part:characteristic-datum` split or trace any theorem to its actual numbered Part. The drift is silent because nobody re-ran the index generator with awareness of the Part-renaming.

Symptoms surveyed (Wave 11):

- **HU-W11g.5** (abstract scope): the abstract (L724--799) advertises the seven-face identification (Part V) and the chiral quantum group equivalence (Part VI frontier), but Part V is `\ifannalsedition\else`-quarantined (line 1510 wraps the entire `\part`). The Annals reader is told the centrepiece exists, then shown phantom `\label`s in lieu of content.
- **HU-W11g.6** (Part VI opener): line 1548 cross-refs `Parts~\ref{part:bar-complex}--\ref{part:seven-faces}`. In the Annals build, `part:seven-faces` is defined only inside the `\ifannalsedition\else` block at line 1512 — so the `\ref` is **undefined** in the public PDF. A genuine Annals build bug.
- **AP106** (CG opening): Parts I, II, III, IV all open with strong direct paragraphs (verified Wave 11 §3); Part V opens with one sentence ("One mathematical object … realized in seven independent mathematical frameworks, all proved to agree.") then dives in — adequate but not *theorem-fronted*; Part VI opens with a meta-paragraph announcing what the frontier will discuss. Neither V nor VI is Chriss--Ginzburg-canonical.
- **No reading paths.** Vol III installed three reading paths (`chapters/theory/introduction.tex` L573 ff.: algebraist / physicist / number theorist) in the 2026-04 wave; Vol I has none. The 4717-line `chapters/frame/preface.tex` hints at audience targeting via per-chapter assessments but exposes no explicit reading-path table in `main.tex` or `guide_to_main_results.tex`.

---

## §2. Diagnosis — why the present skeleton is no longer load-bearing

The current 6-Part structure dates to a moment when Theorem A, the κ-conductor, the Climax, and the Shadow Quadrichotomy were not *named*. They are now (V5--V8 of the punch list, with V9, V10, V11, V12, V13, V15, V16, V17, V19 as supervisory drafts already chapter-quality). The skeleton therefore **scatters its own pillars**:

1. **Pillar 1 (Koszul Reflection, Theorem A)** is fragmented across **eight files** (`wave14_reconstitute_theoremA.md` §1.1 catalogue: A0--A8 in `algebraic_foundations`, `cobar_construction`, `chiral_koszul_pairs`, `bar_cobar_adjunction_inversion` × 4, `bar_cobar_adjunction_curved`, `coderived_models`). The *involutive symmetry* `K^2 ≃ id` that organises the entire programme appears nowhere as a single theorem. The four-clause `thm:bar-cobar-inversion-qi` mixes proved with conditional-promotion content (Wave 5 F3 / AP4 violation).

2. **Pillar 2 (κ-Conductor / BRST Ghost Identity)** is **eight per-family κ formulas** (`wave14_reconstitute_kappa_conductor.md` §1.1 table: Heisenberg, free fermion, bc(λ), βγ(λ), affine KM generic, KM at k=1, Vir, W_N, BP) plus six concrete numerical inconsistencies (B1--B6 of that report). The unifying theorem `K(A) = -c_ghost(BRST(A))` exists only as a draft chapter (`wave14_brst_ghost_identity_chapter_draft.md`, V13).

3. **Pillar 3 (Climax: `d_bar = KZ^*(∇_Arnold)`)** has no home file. It belongs in a Part-opener and an abstract paragraph (HU-W11g.6 placement drafts) and a new Theorem 0.1 of the DK standalone, none of which exist. Drinfeld--Kohno (`drinfeld_kohno_bridge.tex`), Verlinde (scattered), Borcherds (`landscape_census.tex` + `chapters/connections/arithmetic_shadows.tex`), and Arnold (`appendices/arnold_relations.tex`) are presented as four separate theorems without the unifying KZ-pullback.

4. **Pillar 4 (Shadow Quadrichotomy)** is split across `shadow_towers.tex`, `shadow_towers_v2.tex`, `shadow_towers_v3.tex`, `classification_trichotomy.tex`, `N6_shadow_formality.tex`, with a **wrong title** ("trichotomy" enumerating four classes — P2-6 in the master punch list) and a class M asymptotics inconsistency (P2-5: convergent vs Borel-summable — the Wave 14 Quadrichotomy report fixes this with the `H^2 = t^4 Q` Riccati identity and the explicit $c_S = -178/45$ Stokes line, but the chapter has not been written).

The fragmentation is not a writing failure. It is a *structural* failure: the present 6 Parts are organised around **content topics** (the bar complex; the modular characteristic; standard families; physics bridges; seven faces; frontier) rather than around the **four Platonic theorems** that were extracted from the manuscript by the 2026-04-16 reconstitution wave. A Part structure organised by content topics will always scatter a Platonic theorem across multiple Parts: Theorem A touches Parts I and II (existence and complementarity); the κ-conductor touches I, II, III (definition, additivity theorem, family computations); the Climax touches I (bar differential), III (DK and Verlinde families), IV (BV/BRST and Kontsevich), V (seven faces); the Shadow Quadrichotomy touches II (the tower) and IV (Borcherds via arithmetic_shadows).

The Platonic theorems are not subordinate to the Part structure. **They are the architecture.** The Part structure must serve them, not vice versa.

---

## §3. Three options

### Option A — "Pillar Part" (single new Part collecting all four pillars)

Insert a new **Part 0: The Four Pillars** between the Overture and Part I. Roman numerals shift: present I→II, II→III, III→IV, IV→V, V→VI, VI→VII. The new Part 0 contains four chapters, one per pillar, each stating the Platonic theorem as a `\begin{maintheorem}` block followed by the master proof (~30 pages each in the wave 14 drafts).

**Pros.** Maximum visibility for the pillars. Anyone opening the book sees the four theorems before any content. Single insertion in `main.tex` (~60 lines around L860). No renaming of the 6 existing Parts; their internal logic is preserved.

**Cons.** Loses the *interlocking* — the four pillars become four sequential chapters in one Part rather than the load-bearing skeleton of the whole book. The κ-Conductor and Climax theorems then *re-appear* in Parts III and V, creating a "stated upfront, proved downstream" pattern that conflicts with AP4 (`ProvedHere` must accompany the proof, not the announcement). Also continues to embed Pillar 4 in Part II (the Characteristic Datum) and Pillar 1 in Part I (Bar Complex), so the new Part 0 is a *summary* rather than a *structural reorganisation*.

### Option B — "3+4 hybrid" (3 keep-Parts plus 4 pillar-Parts)

Reorganise into **seven Parts**: three "machine" parts (I: Foundations / Bar Complex; II: Standard Landscape; III: Frontier) and four "pillar" parts (IV: Koszul Reflection; V: κ-Conductor; VI: Climax; VII: Shadow Quadrichotomy). Pillars are full Parts each, with the master theorem as the Part-opener and the per-family corollaries as chapters.

**Pros.** Each pillar gets first-class status and full Part real estate (5--8 chapters each), enough room for the master theorem proof, the corollaries, the verifications, and the frontier conjectures (Π1--Π4 of V5; ZTE/factorisation tests of V6; KZB / W-algebra / GRR of V7; class M Stokes / mock modular of V8). Vol III precedent (7 Parts) confirms 7-Part structures are readable at this scale (~700pp).

**Cons.** Over-architects. The Bar Complex (Part I in this scheme) is *itself* the existence + invertibility + branch + leading-coefficient package (the four properties of the categorical logarithm) — three of those four properties **are** already corollaries of Pillar 1. So Part I in Option B ends up as a thin existence-of-`\bar B`/preliminaries part, with no real theorems left in it. Worse: Physics Bridges has no obvious home — it overlaps with Pillar 3 (Climax classical-theorems pulldowns) and Pillar 4 (arithmetic shadows = Borcherds at low genus). Forces an awkward demotion of the Standard Landscape (KM, Virasoro, W-algebras — the bread of the book) from a structural Part to a pillar-of-pillars sandbox.

### Option C — "Four-Pillar Part-spine" (the four pillars ARE the four interior Parts; Foundations and Frontier bookend)

Reorganise into **six Parts**:

```
Overture
Part I:   Foundations          (Bar/cobar, Hochschild, configuration spaces, Heisenberg frame)
Part II:  Pillar 1 — KOSZUL REFLECTION  (Theorem A in Platonic form)
Part III: Pillar 2 — κ-CONDUCTOR        (BRST Ghost Identity + standard landscape)
Part IV:  Pillar 3 — CLIMAX              (KZ pullback + DK, Verlinde, Borcherds, Arnold)
Part V:   Pillar 4 — SHADOW QUADRICHOTOMY (G/L/C/M, Riccati, Stokes, mock modular)
Part VI:  Frontier             (Cross-volume bridges, derived Langlands, modular holography)
```

The four pillars become the **interior spine** of the book; Foundations prepares them; Frontier extends them. Each Part-opener begins with the pillar's Platonic theorem in one display, then the corollaries, the worked families, the analytic shadows.

**Pros.** Each pillar is a full Part with a Part-opener that *is* the Platonic theorem. The interlocks (Climax → Koszul restriction → Pillar 1; Climax → Faltings GRR → Pillar 2; Pillar 1 → hyperelliptic involution → Pillar 4; Pillar 1 → MC element → Pillar 4) become **inter-Part dependencies**, exposed by the ordering. No content moves out of the manuscript; everything is repackaged. The Standard Landscape (Heisenberg, KM, Virasoro, W_N, BP, βγ, lattice, Yangian) **distributes naturally** across Pillar 2 (where κ-formulas live) and Pillar 4 (where shadow classes live), with the result that each family is shown *under the structural lens that classifies it*. The Universal Trace Identity (V11 §8.5) sits at the head of Part VI as the cross-volume bridge to Vol III.

**Cons.** Most aggressive restructuring. Renames every Part (the labels persist; labels are stable; only `\part{}` titles change). Requires the largest Wave 11 phantom-label audit. Cross-volume `\ref{part:...}` calls from Vols II and III must be re-indexed (~12 hits). The "Standard Landscape" loses its identity as a Part — but gains it back as a *thematic axis* shared between Pillars 2 and 4: every family appears twice, once for κ, once for shadow.

### Recommendation

**Option C.** Decisive reasons:

1. **The pillars are not corollaries of the present Parts; they are the architecture.** Option A treats them as corollaries (a summary Part); Option B treats them as additions (extra Parts). Only C treats them as *the* architecture.

2. **CG discipline.** Option C lets every Part open with the master theorem in one display (the wave 14 reconstitutions all open this way). This is the Chriss--Ginzburg standard the Vol III preface (see `chapters/frame/preface.tex` L27, "organised in seven parts with three reading paths") and Vol III's introduction (`chapters/theory/introduction.tex` L573 ff.) already enforce. Vol I's preface has the Heisenberg frame as Overture but no pillar-fronted Part-openers; Option C closes the gap.

3. **AP4 cleanly satisfied.** Each Part contains the proof of its pillar; `\ClaimStatusProvedHere` aligns with `\begin{maintheorem}` in the same Part. The "stated upfront, proved downstream" pattern that Options A and B both create is eliminated.

4. **Cross-volume centrepiece in the right place.** The Universal Trace Identity (V11 §8.5: `tr_{Z(C)}(K_C) = -c_ghost(BRST(Φ(C))) = c_N(0)/2 ∘ Φ`) bridges Pillar 1 (`K`) and the Vol III Borcherds reflection. In Option C this lives at the head of Part VI (Frontier) as the Pillar-1 → Vol-III bridge, which is its natural home. In Options A and B it has no obvious placement.

5. **Standard Landscape distributed by structural lens, not by topic.** Heisenberg appears in Pillar 1 (it is the Platonic example of a Koszul-self-dual chiral algebra), Pillar 2 (κ_Heis = k), Pillar 3 (its bar differential is the classical KZ at level 1), Pillar 4 (class G — bar Euler is polynomial). Vir, KM, W_N, βγ, BP, Yangian, lattice each get the same treatment. **The reader sees the same family from four sides.** This is the 7-faces logic of Part V re-applied at the family level.

6. **Vol III precedent.** Vol III's 7-Part structure (Foundations / Functor / E_n Hierarchy / K3 Yangian / Landscape / Seven Faces / Frontier) bookends a 5-Part interior with Foundations and Frontier. Option C does the same for Vol I with a 4-Part interior (the four pillars). Cross-volume symmetry is maintained.

The remaining sections develop Option C in detail.

---

## §4. Detailed chapter mapping for Option C

The mapping below uses the present chapter file names (`chapters/{theory,examples,connections,frame}/*.tex`) and proposes a new `\part{}` and chapter ordering. **No file renames; no content rewrites; no `\input{}` deletions.** Only the `\part{}` declarations and the Part-opener prose change. Files re-bucket across Parts as listed.

### Part I — Foundations (Overture stays, then ~7 chapters)

```
\part*{Overture}                                       % L871, unchanged
\include{chapters/frame/heisenberg_frame}              % unchanged

\part{Foundations}
\label{part:foundations}                               % renamed from part:bar-complex

\include{chapters/theory/introduction}                 % unchanged
\input{chapters/theory/algebraic_foundations}          % unchanged
\input{chapters/theory/three_invariants}               % unchanged
\input{chapters/theory/configuration_spaces}           % unchanged
\input{chapters/theory/bar_construction}               % unchanged
\input{chapters/theory/cobar_construction}             % unchanged
\input{chapters/theory/poincare_duality}               % unchanged
```

This is the categorical and geometric setup: factorisation algebras, Fulton--MacPherson compactification, Arnold relations, the bar and cobar functors as objects (not yet as adjoint pair). No theorem of pillar-status; everything here is a definition or a classical input.

### Part II — Pillar 1: Koszul Reflection (~8 chapters)

```
\part{The Koszul Reflection}
\label{part:koszul-reflection}                         % new label

\input{chapters/theory/bar_cobar_adjunction_curved}    % unchanged
\input{chapters/theory/bar_cobar_adjunction_inversion} % unchanged
\input{appendices/homotopy_transfer}                   % promoted to part
\input{chapters/theory/chiral_koszul_pairs}            % unchanged
\input{chapters/theory/koszul_pair_structure}          % unchanged
\input{chapters/theory/chiral_hochschild_koszul}       % unchanged (V19 trinity sits here)
\input{chapters/theory/hochschild_cohomology}          % \input continuation, unchanged
% NEW chapter installation (per V19 / wave14_reconstitute_chiral_hochschild_trinity):
\input{chapters/theory/chiral_hochschild_trinity}      % new file, single-colour Pentagon
% NEW chapter installation (per V5 / wave14_reconstitute_theoremA):
\input{chapters/theory/koszul_reflection_platonic}     % new file, thm:koszul-reflection
```

The Part-opener states **`thm:koszul-reflection`** as `\begin{maintheorem}` (one display), then unfolds the four named morphisms (twisting unit η, twisting counit ε, reflection K, genus-completed counit ψ(ℏ)). The chiral Hochschild Trinity (V19) sits as the single-colour analogue and the proof that **Theorem A is involutive** ($K^2 \simeq \id$ on $\Kosz(X)$) closes the part.

### Part III — Pillar 2: The κ-Conductor (~10 chapters)

```
\part{The $\kappa$-Conductor}
\label{part:kappa-conductor}                           % new label

% NEW chapter installation (per V13 / wave14_brst_ghost_identity_chapter_draft):
\input{chapters/koszul/chiral_chern_weil_brst_conductor} % new file, thm:brst-ghost-identity

% Standard landscape, viewed through the κ lens:
\include{chapters/examples/lattice_foundations}        % κ_lattice = rank
\include{chapters/examples/moonshine}
\include{chapters/examples/level1_bridge}              % κ at k=1, FKS collapse
\include{chapters/examples/free_fields}                % κ_Heis = k, κ_ψ
\include{chapters/examples/beta_gamma}                 % κ_βγ = 0, r_coll vs r_dual
\input{chapters/examples/heisenberg_eisenstein}        % \input continuation
\include{chapters/examples/kac_moody}                  % κ_KM
\include{chapters/examples/w_algebras}                 % K^c_N = 4N^3 - 2N - 2
\input{chapters/examples/w3_composite_fields}          % \input continuation
\input{chapters/examples/n2_superconformal}            % κ_N=2
\input{chapters/examples/bershadsky_polyakov}          % K_BP = 196
\input{chapters/examples/y_algebras}                   % K(Y_N1,N2,N3)
\include{chapters/examples/w3_holographic_datum}       % H(W_3) datum
\input{chapters/examples/symmetric_orbifolds}          % κ_Sym^N
\input{chapters/examples/logarithmic_w_algebras}       % W(p)
% Part II of the present manuscript (Characteristic Datum) substantively migrates here:
\input{appendices/nonlinear_modular_shadows}           % was in present Part II
\input{appendices/branch_line_reductions}              % was in present Part II
\input{chapters/theory/computational_methods}          % was in present Part II
% E_1 Wing absorbed (no longer pseudo-Part):
\input{chapters/theory/e1_modular_koszul}
\input{chapters/theory/ordered_associative_chiral_kd}
\input{chapters/theory/en_koszul_duality}
\input{chapters/connections/thqg_open_closed_realization}
\input{chapters/examples/deformation_quantization}
\input{chapters/examples/deformation_quantization_examples}  % continuation
\input{chapters/examples/yangians_foundations}
\input{chapters/examples/yangians_computations}
\input{chapters/examples/yangians_drinfeld_kohno}
```

The Part-opener states **`thm:brst-ghost-identity`**: `K(A) = Σ_α (-1)^{ε_α+1} 2(6λ_α^2 - 6λ_α + 1) = -c_ghost(BRST(A))`. The Trinity Theorem `K_E = K_c = K_g` follows. Then every standard family appears with its κ-formula computed, no longer as scattered facts but as **corollaries of the BRST Ghost Identity**: K_Vir = 26 = 2(6·4 − 6·2 + 1); K_KM = 2 dim(g); K^c_N = 4N^3 − 2N − 2; K_BP = K(ŝl_3) + K(DS-ghosts) = 16 + 180 = 196. The fragmentation that the κ-conductor wave found in the standalone files is *cured by structure*: the per-family formulas are no longer the ground truth, they are *outputs of one functor* `K`.

This is the largest Part. By chapter count, ~18 chapters. By page count, the heaviest of the four pillars (the standard landscape of present Part III lives here). This is correct: the κ-conductor is the pillar with the most worked examples and the most numerical inconsistencies in the present text.

### Part IV — Pillar 3: The Climax (~7 chapters)

```
\part{The Climax}
\label{part:climax}                                    % new label

% NEW chapter installation (per V7 / wave14_reconstitute_climax_theorem):
\input{chapters/theory/climax_kz_pullback}             % new file, thm:climax
% Existing chapters that ARE shadows of the climax:
\input{chapters/connections/poincare_computations}     % was in present Part IV
\input{chapters/theory/derived_langlands}              % moved up from Part VI
% The four classical theorems as KZ-pullback specialisations:
\input{chapters/connections/feynman_diagrams}          % BV/BRST = chiral bar (Witten branch)
\input{chapters/connections/feynman_connection}
\input{chapters/connections/bv_brst}
% Drinfeld--Kohno (with V9 q-bridge):
\input{chapters/examples/yangians_drinfeld_kohno}      % DUPLICATE — see note below
% NEW supervisory installation (per V9 / wave_supervisory_q_convention_bridge):
\input{appendices/appendix_q_conventions}              % new file, q_KL^2 = q_DK
% Borcherds / arithmetic via Climax pullback:
\input{chapters/connections/arithmetic_shadows}        % was in present Part IV
% NEW supervisory installation (per V12 / wave_supervisory_mc5_theorem):
\input{standalone/N5_mc5_theorem}                      % new file, MC5 theorem
```

**Note on `yangians_drinfeld_kohno`.** This file naturally lives in *both* Part III (κ side: Y(g) is a chiral algebra with K) and Part IV (Climax side: DK is a KZ-pullback specialisation). The Vol III strategy for cross-Part files is to use `\include` once and `\ref` everywhere else; we follow it. The chapter is `\input`'d in Part III (its κ-computation is the entry point); Part IV cross-references `\ref{ch:dk-bridge}` rather than re-`\input`ing.

The Part-opener states **`thm:climax`**: `d_bar = KZ^*(∇_Arnold)` and `κ(A) = -c_ghost(BRST(A))`. The four classical theorems (DK, Verlinde, Borcherds, Arnold) appear as four fibres of the structure functor `KZ : ChirAlg → ConnConf`. The MC5 sewing theorem (V12) closes the genus-0 to genus-1 corner.

### Part V — Pillar 4: The Shadow Quadrichotomy (~6 chapters)

```
\part{The Shadow Quadrichotomy}
\label{part:shadow-quadrichotomy}                      % new label

% NEW chapter installation (per V8 / wave14_reconstitute_shadow_tower):
\input{chapters/theory/shadow_quadrichotomy_platonic}  % new file, thm:shadow-quadrichotomy
% Existing chapters that ARE the four classes:
\input{chapters/theory/higher_genus_foundations}       % was in present Part I
\input{chapters/theory/higher_genus_complementarity}
\input{chapters/theory/higher_genus_modular_koszul}
\input{chapters/theory/filtered_curved}                % when does filtering degenerate to curved
\input{chapters/theory/quantum_corrections}            % was in present Part I
\input{chapters/theory/poincare_duality_quantum}       % was in present Part I
\input{chapters/theory/chiral_modules}                 % was in present Part I
% NEW supervisory installation (per V10 / wave_supervisory_S5_wick):
% (compute engine, no .tex installation — but a remark in shadow chapter cites it)
% Archive-only census reattaches here:
\ifannalsedition\else
 \input{chapters/examples/genus_expansions}            % was in present Part III
 \input{chapters/examples/bar_complex_tables}
 \input{chapters/examples/landscape_census}            % G/L/C/M census
 \input{appendices/combinatorial_frontier}
\fi
```

The Part-opener states **`thm:shadow-quadrichotomy`** in one display: `H^2 = t^4 Q_c(t)` with `Q_c(t) = (a_0 + a_1 t)^2 + 2Δ t^2`. The four analytic classes G/L/C/M are characterised by the algebraic factorisation type of `Q_c`. The class M Stokes line `c_S = -178/45`, alien amplitudes `A_± = ±√(Q'(t_±)/2) t_±^2`, instanton actions `S_± = 1/t_±` are the climax; the trans-series of `Z_chiral(Vir_c)` follows. The Riccati identity `H^2 = t^4 Q` is the shadow Maurer--Cartan equation, named explicitly as the Pillar 1 → Pillar 4 bridge (hyperelliptic involution = Koszul reflection, `wave14_reconstitute_shadow_tower.md` §interlocks).

### Part VI — Frontier (~6 chapters)

```
\part{Frontier}
\label{part:frontier}                                  % renamed from part:v1-frontier

% NEW: cross-volume universal trace identity centrepiece (per V11 §8.5):
\input{chapters/connections/universal_trace_identity}  % new file, V11 §8.5

% Existing frontier chapters (preserved):
\input{chapters/connections/frontier_modular_holography_platonic}
\input{chapters/connections/entanglement_modular_koszul}
\input{chapters/connections/thqg_entanglement_programme}
% NEW supervisory installation (per V16 / wave_supervisory_holographic_verdier_distance):
\input{chapters/connections/holographic_codes_koszul}  % rewritten L339-421
\input{chapters/connections/semistrict_modular_higher_spin_w3}
\input{chapters/theory/nilpotent_completion}
\input{chapters/theory/coderived_models}
\input{chapters/connections/subregular_hook_frontier}
\input{chapters/connections/outlook}
\input{chapters/connections/master_concordance}

% Seven Faces Part V is reabsorbed into Frontier in archive build:
\ifannalsedition\else
 \input{chapters/connections/holographic_datum_master}    % was Part V opener
 \input{chapters/connections/genus1_seven_faces}          % was Part V
\fi
```

**Critical structural decision for Frontier.** The present Part V (Seven Faces, archive-only) does *not* survive as a standalone Part — the seven-face identification is reframed as a *frontier theorem about the collision residue*, with the seven-way master theorem (`thm:hdm-seven-way-master`, `thm:seven-faces-master`) presented as a *consequence of Pillars 2--4* (κ + Climax + Shadow): the collision residue `r(z) = Res^coll_{0,2}(Θ_A)` is the Pillar-1 universal MC element restricted to depth 2 (Pillar 4 reading), is the κ-additivity test (Pillar 2 reading), and is the KZ pullback at the depth-2 stratum (Pillar 3 reading). Seven faces = seven specialisations of the four pillars, which is a frontier-grade synthesis, not a separate Part. This **closes HU-W11g.5** (abstract scope cascade).

### Total Part count: 6 (Overture + 5 numbered + Frontier ≡ 6 numbered if Overture is unnumbered as today). Total chapter count: ~50 (similar to present). Page count expected to be slightly larger (~590pp → ~620pp) due to four new master-theorem chapters; the wave 14 drafts give explicit page budgets (~30pp for V13, ~25pp for V5, ~35pp for V7, ~30pp for V8, ~20pp for V19).

---

## §5. Part openers (1--2 paragraphs each)

Each opener begins with the Platonic theorem as a `\begin{maintheorem}` block (one display only), then a single short paragraph naming the inner motion, the inner music, and the corollaries developed in the part. Chriss--Ginzburg discipline: no "this part discusses", no "we will prove", no "the goal is to". Construct, do not narrate.

### Part I opener — Foundations

> Place sections $a_1, \ldots, a_n$ of a chiral algebra $\mathcal{A}$ at distinct points $z_1, \ldots, z_n$ on a smooth curve $X$. Wedge the tensor $a_1(z_1) \otimes \cdots \otimes a_n(z_n)$ against the logarithmic $n$-form $\eta = \bigwedge_{i<j} d\log(z_i - z_j)$ on the Fulton--MacPherson compactification $\overline{C}_n(X)$, and extract residues at each collision divisor. The result is a differential. Arnold's three-term identity $\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} = 0$ forces $d^2 = 0$. This is the bar complex $\overline{B}_X(\mathcal{A})$.
>
> The four pillars of this volume act on $\overline{B}_X(\mathcal{A})$. Part~\ref{part:koszul-reflection} proves that bar and cobar are an involutive symmetry. Part~\ref{part:kappa-conductor} proves that the leading coefficient of the bar logarithm is the BRST ghost charge of the underlying chiral algebra. Part~\ref{part:climax} proves that the bar differential is the pullback of Arnold's universal KZ connection along a structure functor; Drinfeld--Kohno, Verlinde, Borcherds and the bar differential itself are four shadows of one form. Part~\ref{part:shadow-quadrichotomy} proves that every chirally Koszul vertex algebra of finite type belongs to exactly one of four analytic classes G/L/C/M, characterised by the factorisation type of one quadratic invariant on a hyperelliptic spectral curve. The present part assembles the categorical and geometric raw material on which the four pillars act.

(*Lifted with edits from present Part I opener at L902--960; only the second paragraph is new.*)

### Part II opener — The Koszul Reflection (Pillar 1)

> **Theorem (Koszul Reflection).** *$(\Omega_X, \overline{B}_X)$ is a symmetric-monoidal adjoint equivalence of stable presentable $(\infty,1)$-categories between $\mathrm{Alg}^{\mathrm{fact, aug, comp}}_X$ and $\mathrm{CoAlg}^{\mathrm{fact, conil, co}}_X$, with unit and counit the universal Maurer--Cartan element and its dual. On $\mathrm{Kosz}(X)$, the equivalence restricts to a chain-level quasi-isomorphism. The Koszul reflection $K = \overline{B}_X$ is involutive: $K^2 \simeq \id_{\mathrm{Kosz}(X)}$.*
>
> Bar and cobar are two faces of one symmetry; the unit and counit are the universal Maurer--Cartan element and its dual. Three hypotheses suffice — augmentation, augmentation-ideal completeness, finite-dim graded bar pieces — and conilpotency and Koszulness emerge as automatic. Four named morphisms animate the reflection: the twisting unit $\eta$, the twisting counit $\varepsilon$, the reflection $K$ itself, and the genus-completed counit $\psi(\hbar)$. The chiral Hochschild Trinity (geometric / algebraic / bigraded), the single-colour shadow of Vol II's Pentagon, is the cohomological avatar of $K^2 \simeq \id$. Every other pillar of this volume is a manifestation, a colour, or a pullback of $K$.

### Part III opener — The κ-Conductor (Pillar 2)

> **Theorem (Universal $\kappa$-Conductor / BRST Ghost Identity).** *For any chiral algebra $A$ with quasi-free BRST resolution,*
> $$K(A) \;=\; \sum_{\alpha} (-1)^{\varepsilon_\alpha+1} \cdot 2(6\lambda_\alpha^2 - 6\lambda_\alpha + 1) \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(A)).$$
> *The trinity $K_E = K_c = K_g$ holds on the Koszul-self-dual subcategory.*
>
> The conductor IS the cost of restoring chiral conformal symmetry by BRST gauging. Every ghost in the resolution is the price of one constraint. The bc-ghost central charge at spin $j$ is $c_j = -2(6j^2 - 6j + 1)$; each generator of $A$ contributes its bc-spin. The W_N family is the fugue: each spin enters in turn, contributing its anomaly note, with $\Delta^3 K^c_N = 24 = 6 \cdot 4$ as the constant cubic difference. Vir is the simplest entry (single $j=2$ note, $K = 26$); BP enters at the $f_{(2,1)}$ subregular, summing $K(\widehat{\mathfrak{sl}}_3) + K(\mathrm{DS\ ghosts}) = 16 + 180 = 196$. The standard landscape — Heisenberg, KM, Vir, W_N, BP, βγ, lattice, Yangian — is recomputed family by family as a corollary of one identity.

### Part IV opener — The Climax (Pillar 3)

> **Theorem (Vol I Climax).** *The chiral bar differential and the $\kappa$-conductor are governed by ONE universal datum:*
> $$d_{\mathrm{bar}} \;=\; \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}}), \qquad \kappa(A) \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(A)).$$
> *Specialisations of $d_{\mathrm{bar}}$ along the structure functor $A \mapsto \mathrm{KZ}$-arena recover Drinfeld--Kohno (along $A \mapsto U_q$), Borcherds (along $A \mapsto \Lambda$-VOA), Verlinde (along $A \mapsto \mathrm{RCFT}$). All four classical theorems reduce to Arnold's universal KZ-monodromy theorem.*
>
> Many shadows of one form. Drinfeld--Kohno, Verlinde, Borcherds, and the chiral bar differential are pullbacks of one universal connection on $\mathrm{Conf}(C)$ — Arnold's. The differences are the structure functors $A \mapsto \mathrm{KZ}$-arena chosen at each end. The MC5 sewing theorem closes the genus-0 to genus-1 corner of this Climax, identifying the elliptic 3-point trace as the universal KZ sewing kernel. The q-convention bridge $q_{KL}^2 = q_{DK}$ is the algebraic shadow of the topological double cover $B_2 \to S_2$ (one of the structural specialisations).

### Part V opener — The Shadow Quadrichotomy (Pillar 4)

> **Theorem (Shadow Quadrichotomy).** *Every chirally Koszul vertex algebra of finite type belongs to exactly one of four analytic classes G/L/C/M, characterised by the algebraic factorisation type of $Q^{(\mathbf{q})}(t) = (a_0 + a_1 t)^2 + 2\Delta t^2$ on each charged primary line, via the master Riccati identity*
> $$H(t)^2 \;=\; t^4 \, Q_c(t).$$
>
> The classes are: **G (Allegro)** — $Q$ factors completely, bar Euler is polynomial; **L (Andante)** — linear factors, rational; **C (Scherzo)** — quadratic irreducibles, entire of finite order; **M (Adagio resoluto)** — generic, Gevrey-1 divergent and Borel summable, with explicit Stokes data (single Stokes line at $c_S = -178/45$ for Virasoro at generic $c$). The structural data lives on the spectral curve $\Sigma_c = \{y^2 = Q_c(t)\}$, a hyperelliptic Riemann surface; the shadow connection $\nabla^{\mathrm{sh},c}$ is its Picard--Fuchs equation; Koszul monodromy is the hyperelliptic involution. The Riccati identity is the shadow Maurer--Cartan equation, which projects from the Pillar 1 universal MC element via Picard--Fuchs.

### Part VI opener — Frontier

> **Theorem (Universal Trace Identity, cross-volume).** *Vol I's $K(A) = -c_{\mathrm{ghost}}(\mathrm{BRST}(A))$ (Koszul reflection trace) and Vol III's $\kappa_{\mathrm{BKM}}(\mathfrak{g}_X) = c_N(0)/2$ (Borcherds reflection trace) are TWO REFLECTIONS OF ONE IDENTITY:*
> $$\mathrm{tr}_{Z(\mathcal{C})}(K_{\mathcal{C}}) \;=\; \begin{cases} -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal{C}))) & \text{Vol I (Koszul)} \\ c_N(0)/2 & \text{Vol III (Borcherds)} \end{cases}$$
> *with $\Phi: \mathrm{CY}_d\text{-Cat} \to E_n\text{-ChirAlg}(\mathcal{M}_d)$ the cross-volume bridge.*
>
> This identity is the gateway to the frontier: derived geometric Langlands, modular holography, holographic codes (with Verdier-pairing distance, V16), the entanglement programme, and the seven-face identification of the collision residue (reabsorbed here as a frontier theorem on the depth-2 specialisation of the Pillar-1 universal MC element, jointly with the Pillar-2 κ-additivity and the Pillar-3 KZ-pullback).

---

## §6. Reading paths (per Vol III precedent)

Vol III installs three reading paths in `chapters/theory/introduction.tex` L573 ff. (algebraist / physicist / number theorist). Vol I should mirror this. Insertion target: end of `chapters/theory/introduction.tex` (currently extends from the front-matter Notation and Conventions block); add after present last paragraph, before `\input{chapters/frame/heisenberg_frame}`.

### Path 1 — The Algebraist (Parts I, II, III; ~25 chapters)

This is the categorical-and-operadic spine. Part I assembles the bar/cobar functors as objects on `Fact(X)`. Part II proves the Koszul Reflection (Theorem A): bar and cobar are involutive adjoint equivalences on $\Kosz(X)$, with $K^2 \simeq \id$. Part III computes the κ-conductor for every standard family (Heisenberg, KM, Vir, W_N, βγ, BP, lattice, Yangian) as a corollary of the BRST Ghost Identity. The reader stops at the end of Part III with the full algebraic engine.

A reader who wants only Theorems A, H, and the κ-formulas can stop after Chapter ~22 of Part III. Prerequisites: dg categories, $(\infty,1)$-monoidal categories at the level of Lurie HA, basic factorisation algebras at the level of BD/CG/FG.

### Path 2 — The Physicist (Overture, Part I, Part III, Part IV, then Part VI; ~22 chapters)

This is the BV/BRST and KZ-monodromy spine. Read the Heisenberg frame Overture as motivation. Skim Part I for the bar-as-residue construction. Read Part III for the BRST Ghost Identity (which is `K = -c_ghost`, the cost of gauge symmetry restoration). Read Part IV for the Climax: every classical theorem in 2d CFT — Drinfeld--Kohno, Verlinde, Borcherds — is a pullback of Arnold's KZ. The MC5 sewing theorem and the q-bridge close the genus-0 to genus-1 corner. Then Part VI for the Universal Trace Identity (cross-volume bridge to BPS/Calabi--Yau quantum groups), modular holography, entanglement, holographic codes.

A reader from string theory, twisted holography, or 2d/3d CFT should read in this order. The mathematical prerequisites are lighter than Path 1; the conceptual prerequisites are heavier.

### Path 3 — The Number Theorist (Overture, Part I, Part IV, Part V, Part VI; ~20 chapters)

This is the modular-and-arithmetic spine. Read the Heisenberg frame Overture. Skim Part I for the bar complex. Read Part IV for the Climax: Borcherds is a KZ-pullback specialisation, with `Φ_10` as a fibre. Read Part V for the Shadow Quadrichotomy: class M is mock modular at d=2 (with explicit Borel summability and Stokes data); the spectral curve $\Sigma_c$ is a hyperelliptic Riemann surface; the Riccati identity $H^2 = t^4 Q$ is the shadow Maurer--Cartan equation. Read Part VI for the cross-volume Borcherds reflection trace identity.

A reader interested in mock modular forms, Borcherds products, automorphic L-functions, or arithmetic-geometric shadows should read in this order. Pillar 4 (Quadrichotomy) is the natural home for mock modular K3 (`thm:mock-modular-k3-d2`, with Vol III §8); Pillar 2 contains the Eisenstein series in the Heisenberg genus expansion and the universal cubic conductor identity $K^c_N = 4N^3 - 2N - 2$.

---

## §7. Replacement table for `theorem_index.tex`

The auto-generated `standalone/theorem_index.tex` rebucketing must match the Part rearchitecture. Currently:

```
Frame                  19
Part I: Theory       1125
Part II: Examples     713
Part III: Connections 405
```

Replacement (Option C, with Part numerals matching the new Part structure):

```
Overture & Foundations  ~150 (frame 19, theory L1-L7 of Part I)
Part II: Koszul Reflection      ~280 (theory 8 chapters + new chiral_hochschild_trinity + new koszul_reflection_platonic)
Part III: κ-Conductor           ~720 (examples 18 chapters + nonlinear_modular_shadows + branch_line_reductions + computational_methods + e1_modular_koszul + ordered_associative_chiral_kd + en_koszul_duality + thqg_open_closed_realization + new chiral_chern_weil_brst_conductor)
Part IV: Climax                 ~250 (theory derived_langlands + connections poincare_computations + feynman_diagrams + feynman_connection + bv_brst + arithmetic_shadows + new climax_kz_pullback + new appendix_q_conventions + new N5_mc5_theorem)
Part V: Shadow Quadrichotomy    ~280 (theory higher_genus_foundations + complementarity + modular_koszul + filtered_curved + quantum_corrections + poincare_duality_quantum + chiral_modules + new shadow_quadrichotomy_platonic + archive: genus_expansions + bar_complex_tables + landscape_census + combinatorial_frontier)
Part VI: Frontier               ~580 (connections frontier_modular_holography_platonic + entanglement_modular_koszul + thqg_entanglement_programme + holographic_codes_koszul + semistrict_modular_higher_spin_w3 + nilpotent_completion + coderived_models + subregular_hook_frontier + outlook + master_concordance + new universal_trace_identity + archive: holographic_datum_master + genus1_seven_faces)
```

(Chapter counts are estimates; the index generator can be re-run mechanically once `main.tex` is restructured.)

The script `scripts/build_theorem_index.py` (or whatever generates `theorem_index.tex`) should be updated to read `\part{...}` declarations from `main.tex` and bucket entries by their containing Part rather than by their containing directory. The replacement specification is:

```python
# Pseudo-spec: bucket by Part, not by directory
PART_LABELS_TO_TITLES = {
    'foundations':        'Part I: Foundations',
    'koszul-reflection':  'Part II: The Koszul Reflection (Pillar 1)',
    'kappa-conductor':    'Part III: The κ-Conductor (Pillar 2)',
    'climax':             'Part IV: The Climax (Pillar 3)',
    'shadow-quadrichotomy': 'Part V: The Shadow Quadrichotomy (Pillar 4)',
    'frontier':           'Part VI: Frontier',
}
# For each theorem entry, locate the most-recent \part{...}\label{part:X} above it
# in main.tex (after expanding all \include and \input directives),
# and bucket by X.
```

The index generator currently uses a flat directory walk; it must instead build a tree of `\part`/`\input` and assign each theorem to its enclosing Part. Once installed, every regeneration mechanically inherits the correct bucketing — no manual maintenance.

The four duplicate labels noted in the present index (`prop:fermion-complementarity`, `prop:finite-jet-rigidity`, `prop:gaussian-collapse-abelian`, `prop:polynomial-level-dependence`) survive the restructuring (they are content-level duplicates, not architectural). Address them as a separate cleanup pass; not in scope here.

---

## §8. Cross-volume reference mapping

### From Vol II → Vol I

Vol II currently `\ref{part:bar-complex}` 6 times, `\ref{part:characteristic-datum}` 4 times, `\ref{part:standard-landscape}` 3 times, `\ref{part:physics-bridges}` 1 time, `\ref{part:seven-faces}` 0 times (correctly avoided due to Annals quarantine), `\ref{part:v1-frontier}` 1 time. Mapping:

| Old label                        | New label                       | Mapping reason                                |
|----------------------------------|---------------------------------|-----------------------------------------------|
| `part:bar-complex`               | `part:foundations`              | Direct rename                                 |
| `part:characteristic-datum`      | `part:kappa-conductor`          | Pillar 2 absorbs the Characteristic Datum     |
| `part:standard-landscape`        | `part:kappa-conductor`          | Standard families distribute into Pillar 2    |
| `part:physics-bridges`           | `part:climax`                   | BV/BRST/Feynman is the Climax pullback target |
| `part:seven-faces`               | `part:frontier`                 | Reabsorbed; cite as frontier theorem          |
| `part:v1-frontier`               | `part:frontier`                 | Direct rename                                 |

### From Vol III → Vol I

Vol III (`~/calabi-yau-quantum-groups/`) `\ref`s to Vol I parts: 0 hits direct (Vol III refs Vol I theorems by label, not by part). Cross-volume Universal Trace Identity (V11 §8.5) cited from Vol III preface and `chapters/theory/introduction.tex` should `\ref{part:frontier}` in Vol I. The §8.5 paragraph is a candidate for Vol III's `chapters/theory/introduction.tex` *and* Vol I's `chapters/connections/universal_trace_identity.tex`.

### Stable labels (do not change)

All `\label{thm:...}`, `\label{prop:...}`, `\label{lem:...}`, `\label{def:...}`, `\label{conj:...}` survive the Part rearchitecture. **No `\ref` to a theorem/proposition breaks.** Only `\ref{part:...}` calls require the mapping above.

The 280 phantom labels in `main.tex` L1616--1924 (Annals build cross-references to archive-only content) require an audit pass: every phantom guards a label that lives inside a Part-quarantine block; with the new structure (Part V eliminated, Frontier reabsorbs the seven-face content), some phantoms become live and should be removed (those inside the new Part VI), others remain phantom (those inside the still-archive `genus_expansions.tex`, `bar_complex_tables.tex`, `landscape_census.tex`, `combinatorial_frontier.tex`).

---

## §9. Migration checklist (numbered, in execution order)

The migration should be a **single commit** to avoid intermediate broken builds. Pre-commit gates: build passes, tests pass, no AI attribution.

1. **Pre-flight inventory.** `grep -n '^\\part' main.tex` (record current 6 Part lines: 871, 899, 1088, 1182, 1390, 1511, 1544). `grep -rn '\\ref{part:' chapters/ appendices/ standalone/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/` (record every cross-Part reference site).

2. **Create the four new chapter files** (skeletons, content from wave 14 drafts):
   - `chapters/theory/koszul_reflection_platonic.tex` (Pillar 1 master theorem, V5)
   - `chapters/koszul/chiral_chern_weil_brst_conductor.tex` (Pillar 2 master theorem, V13; note new directory `chapters/koszul/`)
   - `chapters/theory/climax_kz_pullback.tex` (Pillar 3 master theorem, V7)
   - `chapters/theory/shadow_quadrichotomy_platonic.tex` (Pillar 4 master theorem, V8)

3. **Create the supporting supervisory files**:
   - `chapters/theory/chiral_hochschild_trinity.tex` (V19, single-colour Pentagon)
   - `appendices/appendix_q_conventions.tex` (V9, q-bridge)
   - `standalone/N5_mc5_theorem.tex` (V12, MC5 theorem) and rename present `standalone/N5_mc5_sewing.tex` → `standalone/N5b_analytic_sewing.tex` (per V12)
   - `chapters/connections/universal_trace_identity.tex` (V11 §8.5, cross-volume centrepiece)
   - `compute/lib/s5_virasoro_wick.py` + tests (V10, first independent-verification anchor)
   - `compute/lib/climax_verification.py` + tests (V7 H10 healing edit)

4. **Restructure `main.tex` Part declarations.** In one editing pass (Edit tool, not bulk replace; AP-CY27 / FM42 — never bulk-replace short substrings):
   - L871: leave Overture unchanged.
   - L899: rename `\part{The Bar Complex}\label{part:bar-complex}` → `\part{Foundations}\label{part:foundations}`. Keep label as-is *or* add `\label{part:bar-complex}` as an alias for backwards compatibility (`\label{part:bar-complex}` immediately after `\label{part:foundations}` will let Vol II `\ref{part:bar-complex}` continue to resolve). Recommend the alias for Wave-1 migration safety; remove aliases in a follow-up cleanup commit.
   - L1088: `\part{The Characteristic Datum}\label{part:characteristic-datum}` → reabsorbed into Part III. Replace with `\part{The κ-Conductor (Pillar 2)}\label{part:kappa-conductor}` and add `\label{part:characteristic-datum}` alias.
   - L1182: `\part{The Standard Landscape}\label{part:standard-landscape}` → DELETE the `\part` declaration; the standard landscape chapters re-`\input` inside Part III. Add `\label{part:standard-landscape}` as a phantom inside Part III opener for backwards compatibility.
   - L1390: `\part{Physics Bridges}\label{part:physics-bridges}` → rename to `\part{The Climax (Pillar 3)}\label{part:climax}` with alias.
   - L1511: `\part{The Seven Faces of the Collision Residue}\label{part:seven-faces}` → reabsorbed into Frontier. Phantom `\label{part:seven-faces}` inside Frontier opener.
   - L1544: `\part{The Frontier}\label{part:v1-frontier}` → `\part{Frontier}\label{part:frontier}` with `\label{part:v1-frontier}` alias.
   - **NEW Part insertion** between L1086 and L1088: insert `\part{The Koszul Reflection (Pillar 1)}\label{part:koszul-reflection}` and reorder the chapter `\input` lines so that bar_cobar_adjunction*, chiral_koszul_pairs, koszul_pair_structure, chiral_hochschild_koszul, hochschild_cohomology, NEW chiral_hochschild_trinity, NEW koszul_reflection_platonic land here.
   - **NEW Part insertion** between L1180 and L1390: insert `\part{The Shadow Quadrichotomy (Pillar 4)}\label{part:shadow-quadrichotomy}`.

5. **Insert the six new Part-opener prose blocks** (§5 above), each immediately after its `\part{...}` declaration and before the first `\input`/`\include`.

6. **Insert reading-paths block** at the end of `chapters/theory/introduction.tex`, mirroring Vol III's L573 ff. structure.

7. **Update `standalone/theorem_index.tex` generator script** per §7 (bucket by Part, not by directory). Re-run; commit the regenerated index.

8. **Audit phantom labels** L1616--1924: for each `\phantomsection\label{X}`, check whether `X` is now defined in a non-quarantined chapter (those become removable) or remains in archive-only content (those stay). Expect ~40 phantoms to retire after the seven-face → Frontier reabsorption.

9. **Cross-volume `\ref` audit.** Run the §8 mapping table as a `sed` preview (do NOT execute as bulk replace — AP-CY27 / FM42); for each `\ref{part:X}` in Vol II and Vol III, manually verify the mapping is correct in context and apply the rename. The aliases installed in step 4 mean this can be deferred to a follow-up commit if needed.

10. **Build verification.** `make fast` (Annals build); `pdflatex "\def\archivebuild{1}\input{main}"` (archive build); `make test` (compute engines); `make verify-independence` (reads compute/lib/s5_virasoro_wick decorator). All four must pass clean.

11. **HU-W11g.5 verification.** Open the Annals PDF; confirm the abstract paragraph 1 (lines 724--773) mentions only content that exists in the Annals build; confirm no `??` cross-reference appears; confirm `\ref{part:frontier}` (replaces `\ref{part:seven-faces}` in the Annals abstract) resolves.

12. **HU-W11g.6 verification.** Confirm the Part VI opener (`\ref{part:frontier}`) cross-references `\ref{part:foundations}--\ref{part:shadow-quadrichotomy}` (now all live in the Annals build).

13. **CLAUDE.md update.** Update Vol I `~/chiral-bar-cobar/CLAUDE.md` to reflect the new Part structure (Part labels, page count, theorem locations). Mirror in Vol II and Vol III if they cite Vol I parts by name.

14. **Commit.** Single commit, message:

```
Vol I main.tex re-architecture around the four Platonic pillars.

Six-Part structure: Foundations / Koszul Reflection (Pillar 1) /
κ-Conductor (Pillar 2) / Climax (Pillar 3) / Shadow Quadrichotomy
(Pillar 4) / Frontier. The four pillars (V5/V6/V7/V8 of the
2026-04-16 swarm reconstitution) become first-class Parts; the
Standard Landscape distributes into Pillar 2 (κ-formulas) and
Pillar 4 (shadow classes); the Physics Bridges become Pillar 3
KZ-pullback specialisations; the Seven Faces are reabsorbed into
Frontier. Each Part-opener begins with the pillar's master theorem
in one display. Three reading paths installed (algebraist /
physicist / number theorist) per Vol III precedent. Aliases
preserved for backwards-compatible \ref{part:...} from Vols II--III.

Closes HU-W11g.5 (abstract scope cascade), HU-W11g.6 (Annals
\ref{part:seven-faces} undefined), AP106 (CG opening for Parts V,
VI), and the V18 Manifesto editing roadmap Phase 1 and Phase 2.

All commits by Raeez Lorgat.
```

---

## §10. Risk assessment

| Risk | Likelihood | Severity | Mitigation |
|------|:---:|:---:|---|
| Broken cross-volume `\ref{part:bar-complex}` etc. | high if no aliases | medium (Annals & archive both render `??`) | Step 4 installs aliases; Step 9 plans audit. The aliases are ~12 lines of `\label{part:X-old}` immediately after `\label{part:X-new}`. Removable in follow-up. |
| Theorem-index generator breaks on rebucketing | medium | low (script-only, doesn't affect manuscript) | Step 7 explicitly updates the generator; regression test on a known Part assignment before commit. |
| Phantom-label retirement misses live → archive labels | medium | low | Step 8 is per-label audit; the converse (archive → live) is the risk, not the reverse. Worst case: a phantom remains where a live label exists, and the live one wins (LaTeX silently uses the latter, no `??`). |
| AP-CY27 / FM42 (bulk substring corruption) on Part-rename | medium | high if triggered (45-corruption count in Vol III) | Step 4 explicitly forbids bulk replace; uses Edit tool per-Part. Pre-commit grep for `Foundationss`, `Climaxx`, `Shadoww`, `pdegree`, `ldegree`, etc. |
| Wave 14 master-theorem chapter writers introduce AP4 violations | medium | medium | Each new chapter MUST have a `\begin{maintheorem}` with `\ClaimStatusProvedHere` followed by `\begin{proof}` within 50 lines. Verify before commit (grep). |
| Reading-paths block conflicts with present preface assessment | low | low | Vol III precedent shows the two coexist; reading-paths go in `introduction.tex`, preface assessments in `preface.tex`. |
| Annals build still advertises Pillar 4 mock modular but quarantines it | low | medium | The Quadrichotomy theorem itself is not archive-only; only the genus_expansions / landscape_census *census* tables are. Part V opener is Annals-visible. |
| Universal Trace Identity chapter (V11 §8.5) duplicated across Vol I and Vol III | medium | low | Use `\input` of a shared file, OR duplicate with explicit cross-reference. The latter is simpler and survives Vol I-as-standalone builds. |
| Migration commit too large to review | high | medium | Acceptable: the alternative (multi-commit migration) leaves intermediate broken builds. Document the 14-step checklist in the commit body. |
| Pre-commit hook flags new files as AI-attributed | very low | low (but blocking) | Wave 14 drafts and this supervisory draft are author-prose only; no AI-attribution strings are introduced. The hook should pass. |

**Overall risk verdict.** Medium-low. The largest risk is the master-theorem chapter writers (Step 2--3) producing AP4 violations; this is mitigated by the Wave 14 drafts being already chapter-quality (V5, V6, V7, V8, V13, V19) — the writer's task is *insertion*, not *composition*. The migration is structurally simple: rename Parts, insert four new Part declarations, insert four to six new Part-opener prose blocks, install supporting supervisory files. No content is deleted; no theorem is moved across files; only `\part{...}` ordering changes.

---

## §11. The inner music of the proposed Part structure

Six Parts. Six voices. Six movements of the chiral symphony.

| Part | Voice | Role in the symphony |
|------|-------|---------------------|
| I. Foundations | **Strings (basso continuo)** | The ostinato of the bar/cobar functors on $\mathrm{Fact}(X)$; logarithmic 1-forms, Arnold relations, Heisenberg as the simplest entry — the rhythmic ground on which the four pillars enter in turn. |
| II. Koszul Reflection | **Bass line** | The involutive ground, $K^2 \simeq \id$. Bar and cobar are two faces of one symmetry. The Trinity Theorem (chiral Hochschild) is the cohomological rumble beneath every pillar. |
| III. κ-Conductor | **Counterpoint** | The W_N fugue. Each spin enters in turn, contributing its bc-anomaly note: $K_{1/2} = -1, K_1 = 2, K_{3/2} = 11, K_2 = 26, K_{5/2} = 47, K_3 = 74, K_4 = 146, K_5 = 242, K_6 = 362$. Vir is the simplest entry; W_N is the stretto; BP is the inversion. The constant third difference $\Delta^3 K^c_N = 24 = 6 \cdot 4$ is the octave. |
| IV. Climax | **Theme (the universal melody)** | Arnold's KZ — the universal monodromy that all four classical theorems play in different keys. DK is the algebraic key, Verlinde the modular, Borcherds the lattice, the bar differential the chiral. Four shadows of one form. |
| V. Shadow Quadrichotomy | **Form (the four movements)** | G-Allegro / L-Andante / C-Scherzo / M-Adagio resoluto. The Riccati identity $H^2 = t^4 Q$ is the underlying meter. Class M's Stokes caesura at $c_S = -178/45$ is the structural cadence. The hyperelliptic involution on $\Sigma_c$ closes the symphony onto itself: it is the same involution as the Koszul reflection $K$ of Part II. |
| VI. Frontier | **Bridge (cross-volume modulation)** | The Universal Trace Identity, modulating from the Vol I (Koszul) reflection to the Vol III (Borcherds) reflection through the cross-volume $\Phi$. Holographic codes, modular holography, derived Langlands as the open-ended horizon. |

The four interior Parts (II--V) form a closed harmonic structure: bass / counterpoint / theme / form. The Climax (Part IV) is not the *end* of the symphony — it is the centre of mass. Pillars 1, 2, 3, 4 interlock via the four named derivations:

- Climax $\to$ KZ-arena restriction $\to$ Koszul Reflection: Part IV pulls back to Part II.
- Climax $\to$ Faltings GRR at genus 1 $\to$ κ-Conductor: Part IV traces to Part III.
- Koszul Reflection $\to$ hyperelliptic involution on $\Sigma_c$ $\to$ Shadow Quadrichotomy: Part II descends to Part V.
- Universal Maurer--Cartan element $\to$ Picard--Fuchs projection $\to$ Riccati identity: Part II projects to Part V.

These four arrows are the **four named derivations** of the manifesto §II. They are not analogies. They are derivations; they connect adjacent Parts; they constitute the inner motion of the architecture.

The reader who walks Path 1 hears: bass (Part II) → counterpoint (Part III). The reader who walks Path 2 hears: counterpoint (III) → theme (IV) → bridge (VI). The reader who walks Path 3 hears: theme (IV) → form (V) → bridge (VI). All three paths converge at the Universal Trace Identity, where Vol I closes and Vol III opens: *one identity, two reflections, one bridge*.

The symphony is six movements long. Each pillar plays a structural role. Removing any one fragments the architecture.

— Raeez Lorgat, 2026-04-16
