# Chiral Koszul Duality

*Associative Chiral Algebras, Ordered Quantum Fields, and the Geometry
of Defects*, by Raeez Lorgat.

```bash
make volume        # the normative volume → out/main_ordered_chiral.pdf
```

## The primitive objects

A protected field theory on $X^{\mathrm{an}} \times \mathbb{R}$, with
$X$ a smooth complex algebraic curve, has two elementary local motions.
Points collide in the curve and produce a singular operator product.
Intervals compose along the oriented line and produce an ordered
associative product. Each motion carries its own associative structure,
and the phrase *noncommutative chiral algebra* has been used for both:

- a **transversely ordered chiral algebra** is an augmented
  $E_1$-algebra for the componentwise coefficient tensor,
  $A \in \mathrm{Alg}^{\mathrm{aug}}_{E_1}(\mathrm{FactD}(X), \otimes^!)$;
- an **associative chiral algebra** is an augmented $E_1$-algebra for
  chiral convolution,
  $C \in \mathrm{Alg}^{\mathrm{aug}}_{E_1}(\mathrm{DMod}(\mathrm{Ran}\,X), \star^{\mathrm{ch}})$,
  whose formal-disc realization is a nonlocal vertex algebra, and a
  quantum vertex algebra once braided data is supplied.

Neither determines the other. There are correspondingly **three** bars —
$\mathrm{Bar}^\perp$, $\mathrm{Bar}^{\mathrm{ch}}_{\mathsf{Ass}}$, and
chiral Chevalley chains $\mathrm{Bar}^{\mathrm{ch}}_{\mathsf{Lie}}$ — and
an equality between any two of them requires a named comparison functor.

The ordered bar is the transverse interval amplitude

$$\mathrm{Bar}^{\perp}_X(A) \;\simeq\; \mathbf{1}\otimes^{L}_{A}\mathbf{1}
\;\simeq\; \int_{([0,1],\,\partial[0,1])} A,$$

and its differential multiplies adjacent transverse letters. It does not
extract a collision residue: the de Rham differential of a configuration
space, the residue differential along a collision divisor, and the
simplicial bar differential are three distinct operators, and the chiral
coefficient accompanies every bar term uncontracted.

The two products on the Ran category do **not** interchange. The
canonical comparison is a retraction with an idempotent onto the
common-decomposition sector; strong duoidality holds only on aligned
windows, and sheaf-level locality is the family of disjointness-locus
squares.

## Status of the earlier architecture

The five-level Beilinson tower, Theorems A/B/C/D/H, the five-archetype
classification, the $5\times5$ $\kappa$-matrix, and the Universal Trace
Identity are **retracted**. They rested on placing the bar complex on
$\overline{M}_{g,n}$ over a relative factorisation stack, which fuses the
transverse and modular directions in the primitive object.

Nothing has been deleted. The retracted-architecture manuscript still
builds via `make legacy-manuscript`, every file remains tracked, and
**[`PORT_LEDGER.md`](PORT_LEDGER.md)** records the disposition of the
corpus file by file: what has been upgraded, what survives the reframing
and awaits porting, and what is keyed to the dead architecture.

The obstruction theorems that make each retraction explicit are in
`volume/no_go.tex`. The falsified Motzkin/Riordan bar-cohomology tables
are settled in `volume/enveloping_audit.tex`, verified by
`compute/tests/test_witt_pentagonal_rigidity.py`.

## Sections below

What follows describes the archived architecture and is retained for
citation archaeology. Read `PORT_LEDGER.md` first.

## The three volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | Open quadrant: bar–cobar, five theorems, five archetypes, modular tower |
| **II** | *$A_\infty$ Chiral Algebras and 3D HT QFT* | Vertical equivalences at levels 3–5: $\mathsf{SC}^{\mathrm{ch,top}}$, PVA descent, gravity-line completion |
| **III** | *Calabi–Yau Quantum Groups* | CY quadrant: two-stage functor $\Phi_d^{(\Sigma_{d-1}, C)}$, Yangians, BKM, $\kappa$-stratification |

## The five theorems (restratified by Beilinson-tower level)

| Theorem | Statement | Level | Hypothesis package |
|:-------:|-----------|:-----:|--------------------|
| **A** | Enhanced associative bar–cobar reconstruction $\Omega_XB_X(A_b)\simeq A_b$; Verdier algebra $K_X(A_b)=\mathbb D_{\operatorname{Ran}}B_X(A_b)$ on the dualizable surface | 1 ↔ 2 | augmented/conilpotent Ran objects; $H_{\mathrm{fact}}$, $H_{\mathrm{conv}}$, $H_{\mathrm{VD}}$ for the three comparison lanes |
| **B** | For a chosen quadratic presentation, $q_{A_b}\colon A_b^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)\to B_X(A_b)$ is a quasi-isomorphism, equivalently $\Omega_X(A_b^{\mathrm i})\simeq A_b$ | 1 ↔ 2 | $H_{\mathrm{CL}}(A_b,A_b^{\mathrm i},\tau_{\mathrm i})$; $H_{\mathrm{PBW}}^{\mathrm{det}}$ for the detecting spectral sequence |
| **C** | The ordinary centre local system gives $\mathbf C_g(A_b)=R\Gamma(\overline{\mathcal M}_g,\mathcal Z(A_b))$ and its represented Verdier splitting; $K^\kappa$ is the later normalized scalar trace | 3 and 5 | strict-flat fibre comparison, represented Verdier involution, perfect pairing; derived-centre brace comparison and C2 BV package when supplied |
| **D** | Four typed outputs: $\operatorname{Obs}^{\mathrm{def}}_g$, its pointed genus-one trace, the perfect Hodge object $\mathfrak O_g^K$, and the stable-graph scalar $F_g$ | 4–5 | $H_D^1$, $H_D^K$, $H_D^{\mathrm{tr}}$, $H_D^{\mathrm{graph}}$ |
| **H** | Each family datum $H_H(A_b;S)$ gives a strong deformation retract of the derived chiral centre onto a complete model supported in $S$ | 3 | complete chart and family models, retract, filtration convergence, ordered-to-symmetric and bounded-to-chart comparisons |

**Family chain rescaling.**  Once maps $(\iota_A,p_A)$ and an operator
$h_A$ satisfy
$d_Ah_A+h_Ad_A=\nu_A(\mathrm{id}-\iota_Ap_A)$ with
$\nu_A\in k^\times$, the operator $\nu_A^{-1}h_A$ is a contraction.
Identifying $\nu_A$ with the algebra-level Verdier sum $K^\kappa(A)$
is a further comparison to the scalar trace complex.

## Five archetypes × five-$\kappa$ stratification matrix

The standard landscape collapses, under averaging at chart level,
into five archetypes with shadow-depth $r_{\max} \in \{2, 3, 4,
\infty, 5\}$:

| Class | Shadow depth | Archetype | Defining property |
|:-----:|:-----------:|-----------|-------------------|
| **G** | 2 | Heisenberg | Gaussian: tower terminates at $\kappa$ |
| **L** | 3 | Affine Kac–Moody | Lie / tree: cubic shadow, then terminates |
| **C** | 4 | $\beta\gamma(\lambda)$ | Contact / quartic: quartic shadow, terminates |
| **M** | $\infty$ | Virasoro, $\mathcal{W}_N$ | Mixed: infinite tower |
| **B** | 5 | Mukai-K3 Heisenberg | Borcherds: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ |

Each row admits five $\kappa$-measurements
$\{\kappa_{\mathrm{cat}}, \kappa^{\mathrm{Hodge}}_{\mathrm{ch}},
\kappa^{\mathrm{Heis}}_{\mathrm{ch}}, \kappa_{\mathrm{BKM}},
\kappa_{\mathrm{fiber}}\}$ — five distinct invariants per family.
K3 × E anchors row B at $(0, 0, 3, 5, 24)$. The collapse pattern
across rows is itself a refined classification axis.

## Five objects, never conflated

$A_b$ (chart algebra) — $B(A_b)$ (bar coalgebra) —
$A_b^{i} = H^\star B(A_b)$ (cohomology coalgebra) —
$A_b^{!}$ (Verdier dual) — $Z^{\mathrm{der}}_{\mathrm{ch}}(A_b)$
(derived chiral centre = bulk).

$\Omega(B(A_b)) = A_b$ is **inversion**, not Koszul duality. $A_b^!$
via **Verdier**. Bulk via **Hochschild** cochains.

## Standalone papers programme

Sixteen papers extracting the three-volume programme into publishable
units, plus a survey:

| Paper | Title | Pages |
|:-----:|-------|------:|
| A | Five Theorems of Modular Koszul Duality | 27 |
| B | The Shadow Obstruction Tower | 43 |
| C | The Ordered Bar Complex and $E_1$ Primacy | 27 |
| D | Chiral Koszulness: bidirectional and conditional characterizations | 22 |
| E | $E_n$-Chiral Algebras and the Operadic Circle | 37 |
| F | Chiral Quantum Groups and the $\mathfrak{gl}_N$ Tower | 81 |
| G | The Drinfeld–Kohno Bridge | 19 |
| H | Seven Faces of the Collision Residue | 25 |
| I | Arithmetic Shadows | 14 |
| J | Multi-Weight Cross-Channel Corrections | 18 |
| K | $\mathsf{SC}^{\mathrm{ch,top}}$ and PVA Descent | 18 |
| L | The Holographic Modular Koszul Datum | 15 |
| M | Algebraic Holographic HT Sector with Virasoro Boundary | 30 |
| N | Analytic Sewing for Chiral Algebras | 40 |
| O | The CY-to-Chiral Functor (two-stage) | 11 |
| P | CY Quantum Groups and 6d hCS | 11 |

Survey paper: 122pp (`standalone/survey_modular_koszul_duality_v2.tex`).

## Programme totals

| Metric | Value |
|--------|------:|
| Pages, Vol I | ~2,700 |
| Pages, three volumes | ~5,142 |
| Tagged claims (Vol I) | ~3,900 |
| Compute tests | 125,000+ |
| Source tree | 106 chapter `.tex`, 16 appendices, 67+ standalone `.tex` |
| Standalone papers | 16 + survey |
| Master conjectures | MC1–MC5 proved at their inscribed scopes |

## Structure

Six parts plus appendices:

- **Part I** (Foundations + Open Beilinson Tower): tangential log
  curve, factorisation dg-category, chart selection, Morita
  reconstruction, Heisenberg overture
- **Part II** (Bar–Cobar Engine): Theorem A in parametric strength
  (four lanes L1 chain / L2 Quillen / L3 $(\infty,1)$ /
  L4 $(\infty,2)$-properad); Priddy / Positselski lane split;
  family contractions obtained from
  $d_Ah_A+h_Ad_A=\nu_A(\mathrm{id}-\iota_Ap_A)$ after constructing
  the four pieces $(\iota_A,p_A,h_A,\nu_A)$ on one complex
- **Part III** (The Bulk): Theorem H family-indexed support transport
  in the completed derived centre; Theorem B quadratic recognition
  through $q_A\colon A^{\mathrm i}\to B_X(A)$; a named open–closed
  comparison carries the derived centre to a physical bulk realization
- **Part IV** (Five-Archetype Landscape): the 5×5 $\kappa$
  stratification matrix, chart-class enumeration per archetype,
  archetype-by-archetype computation
- **Part V** (Modular Tower): Theorem D four-stage trace tower:
  $\operatorname{Obs}^{\mathrm{def}}_g$ in the deformation complex;
  $\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_1
  =\kappa\lambda_1$ under $H_D^1$;
  $\mathfrak O_g^K=\kappa\lambda_{-1}(\mathbb E_g)$ under $H_D^K$;
  and $F_g=\kappa\lambda_g^{\mathrm{FP}}+
  \delta F_g^{\mathrm{cross}}$ under $H_D^{\mathrm{graph}}$;
  modular trace + clutching on the open category and the
  shadow-tower quadrichotomy with weighted-Riccati structure
  $|\omega|^2(c) = c^2(5c+22)/[4(45c+218)]$
- **Part VI** (Seven Faces and Frontier): seven faces of $r(z)$ as
  two GRT-orbits + Brown motivic bridge; KSDual as $\mathbb{Z}/2$-fixed
  symmetric locus; cross-volume vertical equivalences to Vols II, III
  (levels 0, 2, 4); the **Master Reconstruction Theorem** as the
  structural climax (subsuming Theorems A, B, C, D, H as corollaries
  restratified by Beilinson-tower level); open frontiers F1–F12

```
chiral-bar-cobar/
  main.tex                  entry point
  Makefile                  build system
  chapters/
    frame/                  overture + preface + introduction
    theory/                 Parts I–III (~30 files)
    examples/               Part IV (~20 files)
    connections/            Parts V–VI (~30 files)
  appendices/               signs, FM proofs, tables, type system, hypothesis lattice
  compute/
    lib/                    1,352 Python files
    tests/                  1,421 test files
  standalone/               51 .tex sources
```

## Build

All compiled output goes to `out/`.

```bash
make fast                    # quick converging build → out/main.pdf
make                         # full build → out/
make release                 # manuscript + standalone → out/ + iCloud
make standalone              # standalone papers → out/
make test                    # non-slow test suite
make test-full               # full suite
make clean-builds            # remove /tmp/mkd-* isolated build dirs
```

Each build runs in its own `/tmp/mkd-chiral-bar-cobar-<NS>/` so
parallel agents never clobber each other's `.aux` files. Set
`MKD_BUILD_NS` to reuse a build directory across invocations:

```bash
export MKD_BUILD_NS="agent-$$"   # stable for the agent's session
make fast                         # cold first time
make fast                         # warm — reuses .aux
```

Requires TeX Live 2024+ with pdflatex (`memoir`, EB Garamond,
`newtxmath`).

## Independent verification protocol

Every `\ClaimStatusProvedHere` theorem is paired with a test module
decorated with
`@independent_verification(claim, derived_from, verified_against, disjoint_rationale)`.
The decorator enforces token-level disjointness between the
programme-internal derivation and the external-source verification;
tautological decoration fails at import.

```bash
make verify-independence           # summary audit (no tautology / no orphan gate)
make verify-independence-verbose   # full list of uncovered claims
```

See `notes/INDEPENDENT_VERIFICATION.md` for the three-healing rubric
(find disjoint source / restrict scope / downgrade status) and
`compute/lib/independent_verification.py` for the decorator
implementation.

## Constitution and discipline

The repo constitution is `chapters/connections/master_concordance.tex`.
The mathematician's working manifesto is `CLAUDE.md` (Claude Code
harness) and `AGENTS.md` (Codex / GPT-5-family harness): they carry
the platonic-ideal architecture, the master critique discipline, the
master patterns MA-1 … MA-13, the writing standard, the essential
constants, and the operational rules.

The canonical formulas for every family live in
`chapters/examples/landscape_census.tex`. The anti-pattern catalogue
lives in `notes/antipatterns_catalogue.md`. The first-principles
confusion-pattern registry lives in
`notes/first_principles_cache_comprehensive.md` (hook-checked on
inscription).

Open frontiers F1–F12 are tracked in `FRONTIER.md`.
