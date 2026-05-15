# Modular Koszul Duality

**Volume I** of *Modular Homotopy Theory for Algebraic Factorization
Algebras on Algebraic Curves*, by Raeez Lorgat.

The ordered bar complex $B^{\mathrm{ord}}(A_b) = T^c(s^{-1}\bar A_b)$
is an $E_1$-chiral coassociative coalgebra at a chosen vacuum $b \in
\mathcal{C}^{\mathrm{op}}$ on a tangential log curve $(X, D, \tau)$.
Its differential encodes the chiral product via collision residues on
$\mathrm{FM}_n(C)$; its deconcatenation coproduct, the cofree-tensor
structure. The symmetric bar $B^\Sigma$ is the $\Sigma_n$-coinvariant
shadow. Integration over Fulton–MacPherson compactifications computes
the bar complex; Verdier duality interchanges bar and cobar; the
failure of nilpotence at genus $g \ge 1$ is controlled by a single
scalar invariant $\kappa(A_b)$ that organises quantum corrections
across all genera. The geometry determines the operad, the operad
determines the bar complex, the bar complex computes the factorisation
(co)homology.

## Architecture

Vol I is the **Open quadrant** of the four-quadrant programme, the
complete five-level **Beilinson tower**:

```
factorisation dg-cat C^op on (X,D,τ)  [0: primitive]
   → A_b = End_C(b) at chosen vacuum   [1: chart]
   → B(A_b) = T^c(s^{-1} Ā_b)          [2: bar / twisting]
   → Z^der_ch(A_b) ≃ ChirHoch^•        [3: BULK]
   → line / brane operators             [4: operator]
   → modular trace + clutching          [5: scalar]
```

Reconstruction theorems at each step (Morita, Theorem A, Theorem H/B,
Drinfeld-double, modular reconstruction) carry named hypothesis
packages. The **KSDual** sublocus is the $\mathbb{Z}/2$-fixed
sublocus under chiral / antichiral involution $A \mapsto A^!$.
**Vertical holographic equivalences** to Vol II (level 3
$\mathsf{SC}^{\mathrm{ch,top}}$-brace; level 5 gravity-line
completion) and Vol III (levels 0, 1, 2, 4, 5) are named at every
level. The **Master Reconstruction Theorem** (the structural climax)
states the tower with all reconstruction theorems and KSDual
identification; Theorems A, B, C, D, H are corollaries.

## The three volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | Open quadrant: bar–cobar, five theorems, five archetypes, modular tower |
| **II** | *$A_\infty$ Chiral Algebras and 3D HT QFT* | Vertical equivalences at levels 3–5: $\mathsf{SC}^{\mathrm{ch,top}}$, PVA descent, gravity-line completion |
| **III** | *Calabi–Yau Quantum Groups* | CY quadrant: two-stage functor $\Phi_d^{(\Sigma_{d-1}, C)}$, Yangians, BKM, $\kappa$-stratification |

## The five theorems (restratified by Beilinson-tower level)

| Theorem | Statement | Level | Hypothesis package |
|:-------:|-----------|:-----:|--------------------|
| **A** | Bar–cobar Koszul reflection $K^2 \simeq \mathrm{id}$ on $\mathrm{Kosz}(X)$ | 1 ↔ 2 | augmented + complete + finite-dim graded |
| **B** | Strict bar–cobar inversion $\Omega(B(C)) \xrightarrow{\sim} C$ | 1 → 3 | Koszul locus; coderived / weight-completed off-locus for class M |
| **C** | Complementarity per family stratum: $\kappa + \kappa^!$ ceiling | 5 | five $\kappa$-measurements per family; collapse pattern |
| **D** | Modular characteristic $\mathrm{obs}_g = \kappa \cdot \lambda_g$ uniform-weight | 4 | $H^*(\overline{M}_{g,n})$ class; multi-weight via $\delta F_g^{\mathrm{cross}}$ |
| **H** | Chiral Hochschild concentration $\subset \{0,1,2\}$ | 3 | finiteness + completion (class M needs completed / pro / $J$-adic) |

**Universal chain-homotopy** (load-bearing): $h_{A_b} = h_{\mathrm{LV}}/(\kappa + \kappa^!)$.

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
  universal chain-homotopy $h_{A_b} = h_{\mathrm{LV}}/\mathcal N(A_b)$
  with $\mathcal N(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{LV}}(A_b)$
  the Verdier-Ran-on-bar norm (distinct from the master-concordance
  scalar Verdier sum $K^\kappa$; cf.
  Convention~`conv:A-two-kappa-shriek`)
- **Part III** (The Bulk): Theorem H Hochschild concentration ⊂
  $\{0,1,2\}$ in completed ambient; Theorem B Positselski inversion
  on Koszul locus; bar $\neq$ bulk firewall (MA-4)
- **Part IV** (Five-Archetype Landscape): the 5×5 $\kappa$
  stratification matrix, chart-class enumeration per archetype,
  archetype-by-archetype computation
- **Part V** (Modular Tower): Theorem D genus tower
  $\mathrm{obs}_g(A_b) = \kappa(A_b) \cdot \lambda_g$ on the
  uniform-weight scalar lane, modular trace + clutching on the open
  category, shadow-tower quadrichotomy with Borel-Riccati structure
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
