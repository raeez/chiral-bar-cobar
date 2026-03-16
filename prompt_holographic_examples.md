# Holographic Example Absorption

## The situation

You are extending a two-volume research monograph — *Modular Koszul Duality* (Vol I, ~1,767pp) and *A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT* (Vol II, ~497pp) — by absorbing concrete worked examples from four recent physics papers into the monograph's existing chapter structure. Both volumes compile. The codebase is a git repo at `/Users/raeez/chiral-bar-cobar` (Vol I) and `~/chiral-bar-cobar-vol2` (Vol II).

The monograph proves five theorems (A through H) about bar-cobar duality for chiral algebras on curves, then applies them to 3d holomorphic-topological QFT. The four source papers provide exactly the concrete computations that make the abstract engine sing. Your job is to write them into the correct places. All content, no placeholders.

**Author: Raeez Lorgat. No AI attribution anywhere — not in commits, not in text, not in comments.**

## The intellectual key

Every task below has a single conceptual hinge. If you internalize these five identifications, every placement decision and every bar-cobar remark writes itself:

1. **The bar complex IS the BV complex.** The bar differential d_B on the chiral envelope reproduces the BV-BRST differential of the 3d holomorphic-topological theory. This is Theorem A specialized to C × R.

2. **Line operators ARE A!-modules.** The Koszul dual algebra A! acts on line operators; the spectral r-matrix is the universal twisting cochain. This is the Yangian/RTT axis of Ring 3.

3. **Mirror symmetry IS bar-cobar equivalence.** The SQED boundary VOA and the XYZ boundary VOA are related by Theorem B (bar-cobar inversion). Mirror symmetry is not a mystery — it is a quasi-isomorphism.

4. **The PVA λ-bracket IS the classical limit of the chiral OPE.** Khan-Zeng's PVA framework gives the 3d action whose holomorphic twist produces the chiral algebra. The bar complex computes this theory at all genera.

5. **Level-rank IS Koszul duality.** U(N)_k ↔ U(k)_{-N} at the level of boundary VOAs is complementarity (Theorem C): Q_g(g_k) + Q_g(g_{-k-2h∨}) = H*(M_g, Z(g)).

These are not metaphors. They are theorems (proved or conjectural). Write every new section so the reader sees the identification, not just the physics.

## The four source papers

| Key | Paper | What it gives us |
|-----|-------|-----------------|
| CDG20 | Costello-Dimofte-Gaiotto, "Boundary Chiral Algebras" | Interval compactification, boundary VOAs for gauge theories, mirror symmetry, flip operations |
| DNP25 | Dimofte-Niu-Py, "Line Operators and dg-Shifted Yangians" | Vortex lines V_N, explicit r(z), A∞ truncation by W-degree, non-renormalization, gauge A! |
| KZ25 | Khan-Zeng, "PVA and 3d Gauge Theory" | Affine/Virasoro/W₃ PVA brackets and 3d actions, Beltrami phase space, superVirasoro |
| CG18 | Costello-Gaiotto, "Twisted Holography" | Witten diagrams, N=4 symmetry matching, mode algebras |

All four are in the bibliography. Cite keys: `\cite{CDG20}`, `\cite{DNP25}`, `\cite{KhanZeng25}`, `\cite{CG18}`. Verify each key exists in the .bib file before first use; if missing, note it and use the appropriate existing key.

## What you must get right

The monograph has hard conventions. These are the ones that would trip a careful mathematician:

- **Four objects that must never be conflated**: A (the algebra), B(A) (the bar coalgebra), A^i = H*(B(A)) (the dual coalgebra), A^! = (A^i)^∨ (the dual algebra). Omega(B(A)) = A is bar-cobar INVERSION. A^! is obtained by VERDIER/LINEAR duality, not cobar.
- **Grading**: cohomological (|d| = +1). Bar uses desuspension.
- **Com^! = Lie** (not coLie). Heisenberg is NOT self-dual. Vir_c^! = Vir_{26-c}, self-dual at c = 13 not c = 26.
- **Sugawara**: undefined at critical level k = -h∨ (not "c diverges"). Feigin-Frenkel duality: k ↔ -k-2h∨.
- **QME**: ℏΔS + ½{S,S} = 0 (the factor ½).
- **Claim status tags**: `\ClaimStatusProvedHere`, `\ClaimStatusProvedElsewhere`, `\ClaimStatusConjectured`, `\ClaimStatusHeuristic` — every theorem/proposition/conjecture gets one.
- **Macros**: all in main.tex preamble. Never `\newcommand` in chapter files.
- **No new .tex files.** Everything goes into existing chapters.
- **Build**: `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast` (Vol I), `cd ~/chiral-bar-cobar-vol2 && make` (Vol II).

## How to work

Read each target file before writing. Match its existing style — label prefixes, enumeration format, citation patterns, prose register. The monograph is written by a working mathematician: terse theorem-proof-remark blocks, no padding, every sentence pulls weight. Interpret through the bar-cobar lens — don't just summarize the physics paper, show the reader why it's an instance of the monograph's theorems.

Work autonomously. Make placement decisions. If two tasks naturally compose into one section, merge them. If a task fits better in a different file than I've suggested, move it — you have the full codebase. Build after each batch of related edits (not after every single file touch — that's wasteful). Fix errors before moving on.

Use subagents when genuinely parallel work is available (e.g., Vol I batch + Vol II batch). Don't use them for sequential dependencies.

## The 18 examples to absorb

### Tier 1 — Transformative

**1. Free chiral vortex lines V_N and explicit r(z)**
Source: DNP25 §3-4. Target: Vol I `chapters/examples/beta_gamma.tex` (append after existing holographic section, ~line 1845). Also: brief remark in Vol II `chapters/connections/line-operators.tex`.

The vortex line modules V_N = C[ψ₀,...,ψ_{N-1}] are explicit A!-modules. The r-matrix is r(z) = Σ_{n,m≥0} (-1)^n C(n+m,m)(ψ_n⊗X_m − X_n⊗ψ_m)/z^{n+m+1}. The translation coproduct is τ_z(X_n) = Σ_{m=0}^n C(n,m) z^m X_{n-m}. The simplest line OPE: V₁ ⊗_z V_{-1} has differential r_{1,-1}(z) = (1/z)ψ₀X₀. Bar-cobar interpretation: V_N is a B(A)-comodule; the r-matrix is the universal twisting cochain evaluated on the spectral parameter. Tag: ProvedElsewhere.

**2. Affine PVA → Chern-Simons action**
Source: KZ25 §4. Target: Vol I `chapters/examples/kac_moody.tex` (new subsection near end).

PVA bracket: {B_a λ B_b} = f^c_{ab} B_c + k κ_{ab} λ. The 3d action is S = ∫ B_a(dt+∂̄)A^a + ½f^c_{ab} B_c A^b A^a + ½kκ_{ab} A^a∂A^b. The bar differential d_B reproduces this BV-BRST differential; the coproduct gives R-direction factorization. Note the connection to level-rank: bar-cobar duality for g_k relates to U(N)_k ↔ U(k)_{-N}. Tags: ProvedElsewhere for brackets/action; Conjectured for level-rank = Koszul.

**3. SQED-XYZ mirror symmetry as bar-cobar equivalence**
Source: CDG20 §5-6. Target: Vol II `chapters/examples/examples-worked.tex` (new section).

SQED boundary: βγ ⊗ affine gl₁, gauge-invariant subalgebra. XYZ boundary: three chirals with W = XYZ, BRST reduction. CDG20 proves these are equivalent. Bar-cobar interpretation: mirror symmetry exchanges A and A!; SQED is bar-side, XYZ is cobar-side; equivalence IS Theorem B for this family. Tags: ProvedElsewhere for equivalence; Heuristic for "mirror = bar-cobar."

**4. Non-renormalization theorem**
Source: DNP25 §5. Target: Vol I `chapters/theory/quantum_corrections.tex` (this file is only 455 lines — excellent target). Also: remark in Vol II `chapters/connections/modular_pva_quantization.tex`.

For quasi-linear theories, the spectral r-matrix r(z) is exact at tree level — no loop corrections. This is WHY every tree-level A∞ computation in Parts I-II is exact. The bar complex computations are complete, not approximate. Tag: ProvedElsewhere.

### Tier 2 — Enriching

**5. W = X^d/d! full A∞ truncation**
Source: DNP25 §3.2. Target: Vol I `chapters/examples/deformation_quantization_examples.tex` (only 574 lines).

For W = X^d/d!, the operations m_k are nonzero only for k ≤ d-1. The degree of W controls A∞ truncation. B(A) has differential terminating at bar-length d-1. Examples: W=X²/2 (m₁ only), W=X³/6 (m₁+m₂), W=X⁴/24 (m₁+m₂+m₃). Tag: ProvedElsewhere.

**6. Beltrami/Teichmüller as phase space**
Source: KZ25 §4.2. Target: Vol I `chapters/examples/w_algebras.tex` (near the existing W₃ PVA section).

μ = Beltrami differential (complex structure), T = quadratic differential (cotangent fiber), phase space = T*T_g. Virasoro 3d action: S = ∫ μ(dt+∂̄)T + Tμ∂μ + (c/24)μ∂³μ. Schwarzian: T̃(φ(z)) = (∂φ/∂z)²T(φ(z)) − (c/12){φ;z}. The curvature d² = κ·ω_g has phase-space origin: curvature of the Beltrami connection on the universal curve. Tags: ProvedElsewhere for PVA/action; Conjectured for curvature interpretation.

**7. Level-rank duality as Koszul duality**
Source: CDG20 §7. Target: Vol I `chapters/examples/kac_moody.tex` (combine with task 2 or separate subsection).

U(N)_k ↔ U(k)_{-N} at boundary-VOA level is Koszul duality: bar of one level ≃ cobar of dual level. Evidence: complementarity Q_g(g_k) + Q_g(g_{-k-2h∨}) = H*(M_g, Z(g)) is exactly the level-rank pairing. Tag: Conjectured.

**8. Monopole operators via affine Grassmannian**
Source: CDG20 §6. Target: Vol I `chapters/examples/yangians_computations.tex` (new subsection near end).

Dirichlet b.c. produce monopole operators parametrized by Gr_G. Coulomb branch = ring of monopole operators. Bar-cobar: Coulomb branch algebra is H*(B(A)) for the Dirichlet boundary chiral algebra. Tag: Heuristic.

### Tier 3 — Completing the landscape

**9. Massive chiral (W = m·XY)**
Source: CDG20 §4.3. Target: Vol I `chapters/examples/beta_gamma.tex` or `free_fields.tex` (check for existing mass-deformation discussion).

W = m·XY; boundary algebra = quotient killing massive modes. Mass term adds quadratic piece to bar differential; bar cohomology = boundary algebra. Tag: ProvedElsewhere.

**10. XYZ model (W = XYZ)**
Source: CDG20 §5.1. Target: Vol I `chapters/examples/deformation_quantization_examples.tex`.

Three chirals X, Y, Z; W = XYZ. Boundary algebra = BRST reduction. m₂ from cubic vertex, m₃ = 0 (truncation by degree). Tag: ProvedElsewhere.

**11. SQED boundary VOA**
Source: CDG20 §5. Target: Vol II `chapters/examples/examples-worked.tex` (pairs with task 3).

βγ ⊗ affine gl₁, gauge-invariant subalgebra. Explicit generators: gauge-invariant combinations of β, γ, J. Tag: ProvedElsewhere.

**12. SQCD boundary algebra**
Source: CDG20 §6. Target: Vol II `chapters/examples/examples-complete.tex`.

SU(N) with N_f fundamentals. Boundary VOA = (βγ)^{⊗N_f} ⊗ affine su(N), gauge invariants. Tag: Heuristic.

**13. Flip operations as A!-morphisms**
Source: CDG20 §5.4. Target: Vol II `chapters/examples/examples-worked.tex`.

2d boundary couplings changing b.c. type = morphisms in A!-mod = bar-cobar engine for boundary condition changes. Tag: Heuristic.

**14. Multiple chirals with character formulas**
Source: CDG20 §4. Target: Vol I `chapters/examples/genus_expansions.tex`.

Graded characters as q-series = graded dim of bar cohomology = partition function. Multi-chiral product formulas. Tag: ProvedElsewhere.

**15. SuperVirasoro PVA → 3d supergravity**
Source: KZ25 §4.3. Target: Vol I `chapters/examples/w_algebras.tex`.

N=1 super-PVA with superpartner G, λ-brackets, 3d supergravity action. Supersymmetric shadow tower. Tag: Conjectured.

**16. Gauge theory A! as shifted cotangent loop algebra**
Source: DNP25 §4. Target: Vol I `chapters/examples/yangians_computations.tex`.

A! = T*[-1]g[λ]* for gauge theories. This IS the dg-shifted Yangian = bar-cobar dual of boundary chiral algebra. Tag: ProvedElsewhere.

**17. Witten diagrams in twisted holography**
Source: CG18 §4-5. Target: Vol II `chapters/connections/celestial_holography.tex`.

2-point and 3-point functions in holomorphic CS / KS theory. Mode algebra matching: open ↔ closed. Tags: ProvedElsewhere (low-point); Conjectured (full matching).

**18. N=4 chiral algebra symmetry matching**
Source: CG18 §3. Target: Vol II `chapters/connections/celestial_holography.tex` or `ht_bulk_boundary_line.tex` (choose based on existing N=4 discussion).

Complete fermionic + bosonic symmetry matching between boundary VOA and bulk theory. The Koszul triangle: A_bulk ≃ Z_der(boundary) ≃ HH•(A!). Tags: ProvedElsewhere / Conjectured.

## What done looks like

Both volumes compile cleanly. Each task has produced 20-80 lines of tightly integrated LaTeX in the correct file. Every theorem environment has a claim status tag. Every label follows the file's existing convention. No existing content has been altered. The reader who opens any example chapter now sees the abstract engine instantiated in explicit formulas from the physics literature — and understands immediately that bar-cobar duality is not formalism, it is the computation.
