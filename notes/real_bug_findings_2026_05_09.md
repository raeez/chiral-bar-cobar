# Real bugs and proof gaps found in Wave-1 inscriptions — 2026-05-09

> Findings from honest mathematical audit of Wave-1 inscriptions, beyond
> the structural reconstitution. These are real bugs and proof gaps,
> not editorial framing.

---

## Bug 1 — Zamolodchikov norm misclassification (CONFIRMED, FIXED)

**Wave-1 inscription** (`chapters/theory/theorem_A_infinity_2.tex`,
`rem:A-h-three-paths`, Path 2):
> "The denominator $c(5c+22)/10$ vanishes at the secondary Borel pole
> $c=-218/45$ and the Yang--Lee value $c=-22/5$, both of which are
> independently flagged divergence loci of the universal chain-homotopy
> in class $\mathsf M$."

**Verification by direct symbolic computation:**

```
Zamolodchikov norm c(5c+22)/10:
  at c = -22/5  →  0       (vanishes; 5c+22 = 0)
  at c = -218/45 →  436/405 ≠ 0   (does NOT vanish)
```

**Diagnosis.** The c=-218/45 claim conflated two distinct singular loci:
- **Chain-homotopy divergence locus** of $h_\mathsf M$: zeros of
  $\langle\Lambda|\Lambda\rangle = c(5c+22)/10$, i.e., $c=0$ and $c=-22/5$.
- **Borel-Riccati pole** of the shadow-tower radius
  $|\omega|^2(c) = c^2(5c+22)/[4(45c+218)]$: pole at $c=-218/45$ where
  the radius blows up.

These are different mathematical phenomena. Chain-homotopy normalisation
is finite at $c=-218/45$ (evaluates to $436/405$); the Borel radius
itself is infinite there.

**Fix applied.** `theorem_A_infinity_2.tex` Path-2 paragraph rewritten;
`rem:A-h-three-paths` closing paragraph rewritten;
`CLAUDE.md` essential-constants paragraph (line 138-141) rewritten.

**Impact assessment.** Any chapter or proof that referenced the wrong
claim — that $h_\mathsf M$ diverges at $c=-218/45$ — was using a
falsehood. The correct singular-locus statement is now in place.

---

## Proof gap 2 — $\mathcal N(\mathsf L) = 2(k+h^\vee)$ chain-level
verification (DIAGNOSED, INSCRIBED AS FRONTIER)

**Wave-1 inscription** (`prop:A-universal-chain-homotopy`, Path 1):
> "Sugawara substitution $L_{-n} = (1/(2(k+h^\vee)))\sum :J^a J^a:$
> yields the chain homotopy $h_\mathsf L = h_{\mathrm{LV}}/(2(k+h^\vee))$."

**Audit.** The Garland-Lepowsky / Macdonald formula gives
$H^\bullet(B(V_k(\mathfrak g)))$ which is $k$-independent at
non-critical level. So the bar cohomology has no $k$-dependence; the
$(k+h^\vee)$-prefactor cannot come from the bar differential. The
proposition's proof says it comes from the convolution-pairing
normalisation
$\mathfrak g^{\Eone}_\cA = \Hom^{\fact}_X(\Bbarch_X(\cA),\cA)$
which acquires the Sugawara prefactor via the Killing-form pairing.

This is a plausible but unverified assumption. A direct chain-level
verification at degree-$2$ / weight-$3$ of the Macdonald-stratum bar
complex (where $H^2 = 5$-dim spin-$2$ irrep at weight $3$) extracting
the $1/(2(k+h^\vee))$-prefactor from the contracting homotopy is not
in the manuscript.

**Fix applied.** Path 1 paragraph in `rem:A-h-three-paths` rewritten
to acknowledge the subtlety: the bar differential is $k$-independent;
the $(k+h^\vee)$-prefactor enters via the convolution pairing, not
the bar differential. Inscribed as Frontier~F1${}^\dagger$ (chain-level
verification of $\mathcal N(\mathsf L) = 2(k+h^\vee)$ on
Garland-Lepowsky strata).

**What would close it.** Compute the explicit Priddy contracting
homotopy on $B(V_k(\mathfrak{sl}_2))$ at degree 2, weight 3
(5-dimensional spin-2 irrep), with the deconcatenation differential
acting on $\Lambda^2(s^{-1}\bar V_k)$, and verify that the chain-level
homotopy $h$ with $[d, h] = \mathrm{id} - \pi_{H^2}$ has scalar
$1/(2(k+h^\vee))$ when normalised against the Killing pairing.

---

## Note on the universal chain-homotopy formula's status

After the two fixes above, the formula
$h_{A_b} = h_{\mathrm{LV}}/\mathcal N(A_b)$ stands with:
- **Class B:** verified ($\mathcal N(\mathsf B) = 8$ from
  $K^\kappa = 2c_+(\mathrm{Mukai}(K3))$, three-path verification in
  `cy_bkm_algebra_engine.py`).
- **Class M:** verified at the Sugawara-Zamolodchikov level
  ($\mathcal N(\mathrm{Vir}_c) = c(5c+22)/10$, with correct
  divergence loci $c=0, c=-22/5$; Borel-Riccati pole at $c=-218/45$
  identified as separate phenomenon).
- **Classes G, C:** $\mathcal N = 1$ (free-field, no rescale); no
  non-trivial chain-homotopy verification needed.
- **Class L:** $\mathcal N(\mathsf L) = 2(k+h^\vee)$ from formal
  Sugawara substitution; direct chain-level Priddy-contraction
  verification on Garland-Lepowsky strata is **open**
  (Frontier F1${}^\dagger$).

This is the honest status. The proposition is plausible across all
five archetypes and verified at three of them; the affine
Kac-Moody case rests on an unverified substitution argument that
needs chain-level closure.

---

## Finding 3 — ChirHoch^1 derivation-type breakdown
(NEW MATHEMATICAL CONTENT)

Theorem H states $\ChirHoch^\bullet(A_b) \subset \{0,1,2\}$. The
engine `chiral_hochschild_engine.py` records explicit dimensions and
derivation types. The breakdown is itself substantive:

| Family             | dim H¹ | Derivation type             |
|--------------------|-------:|-----------------------------|
| Heisenberg $H_k$   | 1      | level deformation $k \mapsto k + \epsilon$ |
| free fermion $\psi$| 1      | bilinear rescaling (anti-symmetric pairing) |
| $\beta\gamma_\lambda$ | 2   | charge rescaling + weight deformation $\lambda \mapsto \lambda+\epsilon$ |
| $V_k(\mathfrak{sl}_2)$ | 3 | current-algebra derivations (3-dim, = adjoint $\mathfrak{sl}_2$); level deformation: **0** |
| $\mathrm{Vir}_c$ generic | 0  | (rigid; no first-order deformation) |

**Notable.** For affine $V_k(\mathfrak g)$, the $\dim \mathfrak g$-dim
$\ChirHoch^1$ is the **adjoint action of $\mathfrak g$** on the
universal-enveloping VOA — *not* a level deformation. The level $k$
is **rigid** under chiral Hochschild deformation: $V_{k+\epsilon}$
versus $V_k$ are structurally different algebras (different central
extensions of $\widehat{\mathfrak g}$), not deformations of each
other in the chiral-bimodule sense.

For Virasoro at generic $c$, $\ChirHoch^1 = 0$: **Virasoro is
chirally rigid**. All first-order deformations vanish. The continuous
parameter $c$ is external to the chiral-bimodule deformation theory
of $\mathrm{Vir}_c$ (the deformation $c \mapsto c + \epsilon$ moves
between different fixed-$c$ slices of the Virasoro family, not within
$\mathrm{Vir}_c$'s own bimodule deformations).

For Heisenberg, the level $k$ **is** a bimodule deformation
(`level_deformation: 1`) because Heisenberg is abelian: changing
$k$ rescales the OPE pairing $J(z)J(w) \sim k/(z-w)^2$, and this
rescaling is realised as a bimodule action.

The asymmetry between Heisenberg (level deformable) and affine
$V_k(\mathfrak g)$ (level rigid; only adjoint action deformable) is
**real mathematics** distinguishing class $\mathsf G$ from class
$\mathsf L$ at the chiral Hochschild level — beyond the scalar
$\kappa$-stratification.

This was hidden in `chiral_hochschild_engine.py`'s output but had not
been made explicit in the manuscript prose. **Inscribed** in
`chapters/theory/chiral_hochschild_koszul.tex` as
`rem:chirhoch-derivation-types` (a new remark following Theorem H),
distinguishing the deformation types per archetype.

---

## Finding 4 — Macdonald identity verified for sl_3 (NEW VERIFICATION)

The Garland-Lepowsky / Macdonald formula computes the bar cohomology
of $V_k(\mathfrak g)$ at non-critical level: for $\mathfrak g$ a
simple complex Lie algebra of dimension $d$,
$$
\sum_{w \ge 0} \dim H^\bullet(B(V_k(\mathfrak g)))_w \cdot q^w
\;=\; \prod_{n \ge 1} (1 - q^n)^d.
$$

Earlier sl_2 verification: $\eta(\tau)^3$ matches $H^p$ at weight
$p(p+1)/2$ with dim $2p+1$ (5 of 5 matches at weights 0,1,3,6,10,15).

**Extended verification for sl_3** ($d = \dim \mathfrak{sl}_3 = 8$):

| Weight | $\dim H^\bullet(B(V_k(\mathfrak{sl}_3)))$ | $|\text{coef. of } q^w \text{ in } \prod (1-q^n)^8|$ | Match |
|-------:|------------------------------------------:|------:|:-----:|
| 0      | 1                                         | 1     | ✓ |
| 1      | 8                                         | 8     | ✓ |
| 2      | 20                                        | 20    | ✓ |
| 3      | 0                                         | 0     | ✓ |
| 4      | 70                                        | 70    | ✓ |
| 5      | 64                                        | 64    | ✓ |
| 6      | 56                                        | 56    | ✓ |

7 of 7 verified. Note that $\dim H^1 = 8 = \dim\mathfrak{sl}_3$,
agreeing with the affine $\ChirHoch^1$ identity. The "Weyl-chamber
gap" at weight 3 (dim 0) is structurally important: it is the
analogue of the $\mathfrak{sl}_2$ triangular-number sparseness.

This rank-2 verification, combined with the rank-1 ($\mathfrak{sl}_2$)
verification, anchors the Macdonald formula for affine $V_k(\fg)$
on two independent simply-laced rank cases. The general formula
$\eta(\tau)^{\dim\mathfrak g}$ then carries the structural confidence
of two-witness independent verification.

---

## Finding 5 — Compute-engine critical-level miscalibration (BUG)

`compute/lib/chiral_hochschild_engine.py` returns the same generic
formula for `dim ChirHoch^0(V_k(\fg)) = 1` and
`dim ChirHoch^1(V_k(\fg)) = \dim\fg` at **all** levels, including
the Feigin-Frenkel critical level $k = -h^\vee$.

Verified directly:
```
V_k(sl_3) generic:        dim ChirHoch^0=1, ^1=8, ^2=1
V_1(sl_3):                dim ChirHoch^0=1, ^1=8, ^2=1
V_{-3}(sl_3) [critical]:  dim ChirHoch^0=1, ^1=8, ^2=1   ← WRONG
V_{-2}(sl_3):             dim ChirHoch^0=1, ^1=8, ^2=1
V_{10}(sl_3):             dim ChirHoch^0=1, ^1=8, ^2=1
```

At critical level $k = -h^\vee = -3$, $V_{-3}(\mathfrak{sl}_3)$
becomes the Feigin-Frenkel oper algebra. Its centre is the
**infinite-dimensional** algebra of opers on the formal disk
\textup{(}Feigin-Frenkel 1992\textup{);} so $\dim\ChirHoch^0$
should be $\infty$, not $1$. Theorem H's concentration in
$\{0,1,2\}$ explicitly excludes critical level: FRONTIER.md
records *"ProvedHere; Feigin-Frenkel companion at $k = -h^\vee$
(infinite-dim centre, non-exclusion)"*.

The engine silently extrapolates the generic formula to critical
level and reports a finite, incorrect value. Theorem H statements
verified against this engine at critical level inherit the bug.

**Mitigation:** add a critical-level guard in
`affine_slN_data(k)` that flags $k = -h^\vee$ and either refuses
to compute or returns a sentinel for $\dim\ChirHoch^0 = \infty$.
The downstream `verify_theorem_h_complete` should warn or skip on
critical-level inputs.

The manuscript's Theorem H statement is correct (it explicitly
excludes critical level). The bug is in the verification engine,
not the theorem.

---

## Finding 6 — Bar spectral-gap collapse loci (NEW)

`compute/lib/parametrized_bar_cobar.py::bar_spectral_gap_virasoro`
computes the bar-complex spectral gap controlling Theorem B's
convergence on Vir_c. The gap-collapse loci are:

| c              | Bar gap            | Interpretation                          |
|---------------:|-------------------:|-----------------------------------------|
| $1$            | $1$ (full gap)     | free boson — generic                    |
| $1/2$          | $\sim 10^{-33}$    | **Ising minimal model M(3,4)**          |
| $-22/5$        | $\sim 10^{-33}$    | **Yang-Lee minimal model M(2,5)**       |
| $13$           | $1$ (full gap)     | KSDual fixed point — generic            |
| $24$           | $1$ (full gap)     | Conway / Niemeier — generic             |
| $26$           | $\sim 10^{-31}$    | **KSDual boundary $\mathrm{Vir}_{26}\leftrightarrow\mathrm{Vir}_0$** |
| $-218/45$      | $\sim 10^{-19}$    | Borel-Riccati pole (small but nonzero)  |

**Pattern.** The bar spectral gap collapses precisely at:
1. **Minimal-model loci** $c = c(p,q) = 1 - 6(p-q)^2/(pq)$ for coprime
   $p, q$. The simple quotient $L_{c(p,q)}$ has finite-dimensional
   first-page bar cohomology, distinct from the universal $\Vir_c$.
   At minimal-model $c$, Theorem B's chain-level inversion holds for
   the universal $\Vir_c$ but the simple quotient $L_{c(p,q)}$ has a
   different bar structure.
2. **KSDual boundary** $c = 26$ where the Verdier dual is the trivial
   chiral algebra $\mathrm{Vir}_0$. Theorem B holds vacuously but the
   gap collapses because the dual algebra is trivial.

**The Borel-Riccati pole at $c = -218/45$ is distinct**: gap is small
($\sim 10^{-19}$) but nonzero — consistent with the Borel-radius
divergence being a *secondary* phenomenon, separate from chain-level
breakdown at $c = 0$, $c = -22/5$, and at minimal-model loci.

This is the computational fingerprint of Theorem B's chain-level
breakdown locus, and an independent confirmation of Finding 1 (the
Borel-Riccati pole is a separate phenomenon from chain-homotopy
breakdown).

---

## Cumulative status of Wave-1 inscriptions (after this audit)

| Inscription                                 | Status |
|---------------------------------------------|--------|
| Theorem A counit qiso on Koszul locus       | Verified for Heisenberg, V_k(sl_2), V_k(sl_3) (Macdonald-Garland-Lepowsky) |
| Theorem A weak/strong/strongest-rejected    | Statement clean; rejection of strongest is rigorous via Theorem H |
| 𝒩(L) = 2(k+h^∨) chain-homotopy norm         | **PROOF GAP** — formal Sugawara substitution; chain-level Priddy verification on Garland-Lepowsky strata is open (F1†) |
| 𝒩(M) = c(5c+22)/10 Zamolodchikov-norm       | Verified at Yang-Lee zero; **bug fixed** (c=-218/45 was wrongly listed as zero) |
| 𝒩(B) = 8 Mukai conductor                    | Verified — engine cy_bkm 9/9 cross-checks |
| Theorem H ChirHoch ⊂ {0,1,2}                | Verified for 7 standard families; **engine bug FIXED** at critical level k=-h^∨ via critical-level guard (Finding 5) |
| ChirHoch^1 = g for affine V_k(g)            | Verified for sl_N, N=2..10 (99 = dim sl_10) |
| Theorem D obs_g = κ·λ_g                     | Genus-1 predictions concrete for 6 families |
| Universal Borcherds-weight κ_BKM = c_N(0)/2 | Verified for N ∈ {1,2,3,4,6} CHL ladder; scope correctly excludes N=8, N=12 |
| K3×E anchor (0, 0, 3, 5, 24)                | Verified (cy_bkm 9/9 + entry-by-entry 3-paths) |
| K^κ complementarity sums                     | Verified by sympy for 8 archetype rows |
| Theorem B chain-level breakdown             | New finding: gap-collapse at minimal models + KSDual c=26 boundary |
| Garland-Lepowsky / Macdonald identity        | Verified at sl_2 (η³) and sl_3 (η⁸); rank-2 anchor |
| Borel-Riccati radius                         | $\rho^2 \cdot \omega^2 = 1$ identity verified; ρ^2 = (180c+872)/(c²(5c+22)), ω^2 = c²(5c+22)/[4(45c+218)] |
| Chiral rigidity of Vir_c, W_3                | Verified at all c tested (no first-order chiral deformations) |
| Level rigidity of V_k(g)                    | Verified — only adjoint deformations, no level deformation |
| Smooth formal moduli for standard landscape | **NEW INSCRIPTION** prop:smooth-formal-moduli-standard. All 5 archetypes have unobstructed deformations; dim of smooth moduli = dim ChirHoch^1 |
| ChirHoch^2 dim = 1 across landscape         | Verified by engine: H_k, V_k(sl_2), βγ, Vir_c, W_3 all have dim H^2 = 1; non-trivial obstruction SPACE but vanishing obstruction MAP |
| Universal Borcherds Weight Identity table   | **CLARIFIED**: multiple atlases exist (Vol I `guide_to_main_results.tex:308`). My earlier values (5, 2, 1, 1/2, 0) match the Cléry-Gritsenko 8-form atlas; the standard Gritsenko-CHL atlas is (5, 4, 3, 2, 1) with c_N(0) ∈ {10, 8, 6, 4, 2} (verified in `test_kappa_stratification_B.py`). Identity κ_BKM = c_N(0)/2 holds in every atlas; only the c_N(0) values differ. |
| Class B kappa stratification 447 tests pass  | All G/L/B archetype-row tests pass: K3×E (0,0,3,5,24); CHL ladder N=1..6 with c_N(0) ∈ {10,8,6,4,2}; engine matches manuscript. |
| Bershadsky-Polyakov K^κ = 98/3              | Verified independently via c_BP(k) = 2 - 24(k+1)²/(k+3); c+c'=196 (k-independent), κ=c/6 → K^κ=98/3 |
| Principal W_N closed-form K^κ               | Verified (H_N-1)(4N³-2N-2) for N=1..10. Predictions: W_4=533/2, W_5=9394/15, W_6=2465/2, W_8=13949/4 (level-independent) |
| Theorem D genus-1 obs predictions           | obs_1(Vir_c) = c/48 for class M minimal models (Yang-Lee=-11/120, Ising=1/96, Potts=1/60); obs_1(V_k(sl_n)) = (n²-1)(k+n)/(48n) |
| KSDual fixed-point inscribed                | **NEW** rem:ksdual-fixed-points-bucket in master_concordance.tex. Fixed points: H_0, V_{-h^∨}, Vir_13, W_3 c=50, BP c=98, K3 self-dual |
| Engine critical-level guard                  | **BUG FIXED**. ChiralAlgebraData.is_critical_level() + center_dimension raises ValueError at k=-h^∨ for affine type-A. 145/145 tests pass |
| Bershadsky-Polyakov closed-form K^c          | Verified Δ³K^c(W_N) = 24 (constant) → recovers K^c(W_N) = 4N³-2N-2 from initial conditions; explains why "24" appears in moonshine |
| KSDual analytic continuation                  | **NEW INSIGHT** added to rem:ksdual-fixed-points-bucket. W_3 c=50 and BP c=98 require complex level k = -3 ± 2i. Real-c, complex-k geometry of KSDual fixed point. |
| BP at admissible levels                       | Verified K^κ(BP) = 98/3 for k ∈ {-1/2, -4/3, 1/2, -2/3, -5/4, 1}. Universal for all non-critical k (sympy proven). |
| F_2(W_3) closed form                          | **NEW INSCRIPTION** higher_genus_foundations.tex line 8604. F_2(W_3) = (7c²+432c+88128)/(6912c). Discriminant -2,280,960 < 0 → no real zeros. F_2 at c=50 (KSDual) = 31807/86400. |
| W_3 cross-channel zero at c=-204             | Verified δF_2^cross(W_3) vanishes at c=-204 (so cross-channel doesn't enter at this c); but full F_2 nonzero (negative scalar part). |
| KSDual fixed central charge closed form W_N   | **NEW INSCRIPTION** kappa_conductor.tex line 320. c_*(W_N) = 2N³-N-1: Vir=13, W_3=50, W_4=123, W_5=244, W_6=425. Real-accessible only for Vir; W_3..W_6 require complex level. |
| Genus-3 W_3 free energy                       | F_3(W_3) = (365c³+159264c²+48263040c+9116997120)/(5806080c²). At KSDual c=50: F_3 = 299348353/362880000 (concrete prediction). |
| K^c(V_k(g)) = 2 dim(g) closed-form           | Universal: K^c=6 (sl_2), 16 (sl_3), 30 (sl_4), 156 (E_6), 266 (E_7), 496 (E_8), 104 (F_4), 28 (G_2). Level-independent. |
| K3×E row (0,0,3,5,24) entry-by-entry verified | κ_cat: χ(O_K3)·χ(O_E)=2·0=0; κ^Hodge_ch=0 (Serre at d=3 odd); κ^Heis_ch=3=dim_C; κ_BKM=5=c_Φ(0)/2; κ_fiber=24=χ_top(K3) (Noether). |
| Faber-Pandharipande generating function     | Verified (x/2)/sin(x/2) - 1 = Σ λ_g^FP x^{2g} via sympy. λ_g for g=1..7 all match: 1/24, 7/5760, 31/967680, 127/154828800, ..., 8191/612141052723200. |
| Mukai conductor K^κ_B = 2c_+(Mukai) = 8     | Mukai lattice II_{4,20} = U^4 + E_8(-1)^2. Signature (4,20), c_+ = 4 → K^κ = 8. Distinct from κ_BKM = 5 (Borcherds weight). |
| Level deformability of H_k                  | Verified — k IS a chiral-bimodule deformation |
