# CLAUDE.md — Modular Homotopy Theory for Factorization Algebras on Curves

## What This Is

Two-volume research monograph by Raeez Lorgat. Vol I (~1,675pp, 67 active files, ~1,795 claims) is the algebraic engine: bar-cobar duality for chiral algebras on curves, proved at all genera. Vol II (~476pp, at ~/chiral-bar-cobar-vol2, 38 files, ~444 claims with 100% tag coverage) applies the engine to 3d holomorphic-topological QFT, PVA quantization, and holography.

**Vol I structure**: Overture (Heisenberg atom) + Part I (The Algebraic Engine, Thms A-D+H) + Part II (The Standard Landscape, all example families) + Part III (Bridges and Programmes) + Part IV (The Frontier, concordance) + Appendices (4 clusters: Foundations, Nonlinear Calculus, Family Frontiers, Physics Bridges).

**Vol I title**: *Modular Koszul Duality*
**Vol II title**: *A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT*

## The Dual Imperative

Maximalist ambition synergizes with maximal truth-seeking. Precision enables ambition. When claims outrun proofs, strengthen the proof first.

## Five Main Theorems (all proved)

- **(A)** Bar-cobar adjunction + Verdier intertwining on Ran(X)
- **(B)** Bar-cobar inversion: Omega(B(A)) -> A quasi-iso on Koszul locus
- **(C)** Complementarity: Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)); upgraded to shifted-symplectic Lagrangian geometry
- **(D)** Modular characteristic: kappa(A) universal, additive, anti-symmetric, A-hat GF
- **(H)** Hochschild: ChirHoch*(A) polynomial, Koszul-functorial

## Three Concentric Rings (the architecture)

**Ring 1** — Proved core: Theorems A-H, MC1/MC2, DK-0 through DK-3, **MC4 closed** (W_N rigidity at all stages + Yangian eval-core).
**Ring 2** — Nonlinear characteristic layer: kappa -> Delta -> [C], o^(4), [Q] -> Theta. Ambient complementarity = shifted-symplectic formal moduli with Lagrangian maps. Complementarity potential S_A. Quartic resonance class Q^contact_Vir = 10/[c(5c+22)].
**Ring 3** — Physics-facing frontier: W-algebra axis (MC4 W_infty closed unconditionally), Yangian/RTT axis (eval-core closed, DK-5 downstream of MC3), holographic/celestial axis (anomaly-completed Koszul duality).

**Unifying principle**: Filtration controls everything.

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
make test                                                         # Fast tests (~6.8K)
make test-full                                                    # All tests (~7.5K)
python3 scripts/generate_metadata.py                              # Census (authoritative)
```

**CAUTION**: Watcher spawns competing pdflatex; always kill before builds.

## Session Entry

1. Read this file and concordance.tex (the constitution)
2. Build: `make fast` (kill pdflatex first)
3. Read relevant source files before writing
4. After each change: verify build compiles
5. Never guess a formula — compute it or cite it

## Critical Pitfalls — MEMORIZE THESE

**Four objects that must never be conflated:**
- A: the algebra. B(A): the bar coalgebra. A^i = H*(B(A)): the dual coalgebra. A^! = (A^i)^v: the dual algebra.
- Omega(B(A)) = A (bar-cobar INVERSION, not duality). A^! is obtained by VERDIER/LINEAR duality, not cobar.

**Grading**: COHOMOLOGICAL (|d|=+1). Bar uses DESUSPENSION.
**Koszul duality**: Com^! = Lie (NOT coLie). Heisenberg NOT self-dual. Chiral Koszulness != classical Koszulness.
**Curved A-infinity**: m_1^2(a) = [m_0, a] (COMMUTATOR, MINUS sign). Bar d^2=0 always; curvature shows as m_1^2 != 0.
**Sugawara**: UNDEFINED at critical level k=-h^v (not "c diverges"). Feigin-Frenkel: k <-> -k-2h^v.
**Virasoro**: Self-dual at c=13, NOT c=26. Vir_c^! = Vir_{26-c}.
**FM compactification**: Blowup along diagonals, NOT complement of diagonal.
**Prime form**: Section of K^{-1/2} boxtimes K^{-1/2} (NOT K^{+1/2}).
**QME**: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2).
**d_bracket^2 != 0**: PROVED (all 2048 signs). Full Borcherds d gives d^2=0.
**sl_2 bar H^2 = 5** (not 6; Riordan WRONG at n=2).

## LaTeX Rules

- All macros in main.tex preamble — NEVER \newcommand in chapter files (use \providecommand for compatibility)
- Document class: memoir; fonts: EB Garamond via newtxmath + ebgaramond
- Claim status: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic
- Label everything: \label{def:}, \label{thm:}, etc. Cross-reference with \ref, never hardcode.

## What NOT To Do

- Do not add packages without checking preamble compatibility
- Do not change verified formulas without checking Critical Pitfalls
- Do not create new .tex files when content belongs in existing chapter
- Do not duplicate definitions — reference from Part I
- Do not guess file locations — use Glob/Grep to find them

## Key File Renames (from platonic cleanup)

| Old name | New name |
|----------|----------|
| kac_moody_framework.tex | kac_moody.tex |
| w_algebras_framework.tex | w_algebras.tex |
| detailed_computations.tex | bar_complex_tables.tex |
| examples_summary.tex | landscape_census.tex |
| deformation_theory.tex | chiral_hochschild_koszul.tex |
| deformation_examples.tex | deformation_quantization_examples.tex |

## Titan Splits (dispatchers → parts)

| Original | Split into |
|----------|-----------|
| higher_genus.tex | higher_genus_foundations + higher_genus_complementarity + higher_genus_modular_koszul |
| yangians.tex | yangians_foundations + yangians_computations + yangians_drinfeld_kohno |
| bar_cobar_adjunction.tex | bar_cobar_adjunction_curved + bar_cobar_adjunction_inversion |

## Git — HARD RULE

All commits authored by Raeez Lorgat. **Never credit an LLM.** No "co-authored-by", no "generated by", no AI attribution anywhere.

## Constitution

**Single source of truth**: concordance.tex (the constitution). When chapters disagree, the constitution is right.

**MC frontier** (MC3 is the remaining algebraic frontier):
- MC1: **PROVED** (PBW concentration)
- MC2: **PROVED** (universal Theta_A)
- MC3: DK beyond eval-gen core (categorical enlargement) — **the single remaining algebraic bottleneck**
- MC4: **CLOSED** — W_infty unconditional at all stages via W_N rigidity (21 conjectures resolved); Yangian eval-core verified (249 tests), DK-5 downstream of MC3
- MC5: Genus 0+1 proved; g>=2 requires Costello renormalization (analytic, not algebraic)
- Theta_A: structured by nonlinear shadow tower; Q^contact_Vir extracted

## Vol II (~/chiral-bar-cobar-vol2)

Five parts: I (Bar Complex -> Swiss-Cheese), II (Descent Calculus), III (Dualities and Bulk-Boundary-Line), IV (Standard Landscape), V (Quantization and Holography).

The bar complex's differential = C-direction factorization. Its coproduct = R-direction factorization. Together: Swiss-cheese algebra on FM_k(C) x Conf_k(R). At genus g >= 1: curved Swiss-cheese with curvature kappa * omega_g.

**Vol II status**: Recognition theorem PROVED. Homotopy-Koszulity of SC^{ch,top} PROVED (via Kontsevich formality + transfer from classical Swiss-cheese). Zero conjectural algebraic inputs remain; only the standing physical axioms (H1)-(H4). All claim status tags at 100% coverage. Cross-volume bridges catalogued in concordance.
