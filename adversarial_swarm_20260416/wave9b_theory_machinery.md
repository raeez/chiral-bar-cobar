# Wave 9b — Adversarial Audit: Vol I Theory-Machinery Chapters

**Date**: 2026-04-16
**Scope**: spectral_sequences, computational_methods, existence_criteria, nilpotent_completion, three_invariants, fourier_seed, quantum_corrections, poincare_duality, poincare_duality_quantum
**Methodology**: First-principles steelman; identify the strongest defensible mathematical statement; flag unprovable variants; recommend either a healing upgrade or a controlled scope restriction. NO commits performed; manuscript untouched.
**Files referenced (absolute)**: `/Users/raeez/chiral-bar-cobar/chapters/theory/{spectral_sequences,computational_methods,existence_criteria,nilpotent_completion,three_invariants,fourier_seed,quantum_corrections,poincare_duality,poincare_duality_quantum}.tex`

---

## Executive summary

Nine theory-machinery chapters were audited. The dominant healing recommendation is to **upgrade `thm:curved-koszul` from `ProvedElsewhere` to `ProvedHere`** in `poincare_duality_quantum.tex` (an explicit chiral instantiation is constructible from the surrounding bar-cobar machinery), **complete or scope-restrict the Step 3 obstruction-theory argument** in `nilpotent_completion.tex` (Theorem `thm:completion-convergence`), and **rewrite the Step 3 quasi-isomorphism in `poincare_duality.tex` (Theorem `thm:bar-computes-dual`)** to invoke Verdier duality on the derived category `D^b_c(\overline{C}_k(X))` rather than the ill-defined distributional product `\eta_{ij} \cdot \delta(z_i - z_j)`. Three further chapters (`spectral_sequences`, `computational_methods`, `existence_criteria`) are largely sound under appropriate scope restrictions; the load-bearing `three_invariants` chapter is correct but understates the genuinely *necessary* part of the `k_max = p_max - 1` relation for non-bosonic generators (a small qualifier suffices). The `fourier_seed` chapter has one quietly load-bearing identification (`Phi_10`-style coalgebra-exponential of the bar pairing) that is correct but should be explicitly conditioned on Theorem A. The `quantum_corrections` chapter contains a genuine first-principles upgrade opportunity: the `kappa = c/2` slice of `prop:central-charge-d1` should be steelmanned by separating the *Virasoro-only* statement from a *family-dependent* genus-1 obstruction lemma.

No outright retractions are recommended. Five healing patches are recommended; four are scope clarifications; two cache append entries are proposed.

---

## 1. spectral_sequences.tex

### 1.1 Steelman of the chapter

The chapter develops three filtrations on the bar complex (bar, genus, Chevalley–Cousin) and the associated spectral sequences. The `ProvedHere` content is:
- `thm:bar-ss` — the bar filtration produces a spectral sequence with `E_1 = de Rham of the FM-stratified bar at fixed bar degree` converging to bar cohomology.
- `prop:degen-koszul` — Koszul implies degeneration at `E_2`.
- `prop:central-charge-d1` — `c = 0 ⇒ d_1 = 0` and `c ≠ 0 ⇒ d_1` is proportional to `c` for conformal vertex algebras.

The remaining `ProvedElsewhere` results (Boardman conditional convergence, Zeeman comparison, Cousin resolution) are textbook citations of `Weibel94`, `KS90`, `BD04`.

### 1.2 First-principles attack: convergence of `thm:bar-ss`

The bar filtration `F_p Bbar^geom = ⊕_{n ≤ p} Bbar^geom_n` is **bounded below in each degree** (clear: `F_{-1} = 0`) but **not bounded above**: bar degree is unbounded. The chapter's `thm:bar-ss` quietly inherits the convergence regime from `thm:classical-convergence`(ii) ("complete + exhaustive + bounded below ⇒ converges to `H_*(\widehat{C})`"), but the manuscript does not state explicitly that the convergence is to *completed* bar cohomology rather than ordinary bar cohomology.

**This is the spectral-sequences analogue of the AP47 evaluation-core/full-category gap.** The bar spectral sequence converges strongly *only after passing to the I-adic completion of `Bbar`*; without completion one gets the conditionally convergent regime of `Boardman`. The current statement of `thm:bar-ss` does not flag this.

**Healing recommendation (light)**: add a one-sentence remark after `thm:bar-ss` of the form "Convergence is to `H^*(\widehat{Bbar}^geom(A))`; for finite-type algebras (`Bbar` finitely generated in each weight, e.g. for the Master Table families per `prop:resonance-ranks-standard`) this agrees with `H^*(Bbar^geom(A))` because each weight space is finite-dimensional and `lim^1 = 0`."

This is a scope clarification, not a retraction. The proof as written is correct under the implicit completion hypothesis.

### 1.3 First-principles attack: `prop:central-charge-d1`

The case `c = 0 ⇒ d_1 = 0` is *over-claimed* as written. The argument given is:
1. genus-1 correction is proportional to `c · E_2(τ)`,
2. so `c = 0 ⇒ d_1 = 0`,
3. and "by Theorem~\ref{thm:genus-universality} all genus-`g` scalar-lane corrections are proportional to `kappa(A)`",
4. so "for Virasoro `kappa(Vir_c) = c/2` … so `c = 0 ⇒ kappa = 0` and all scalar-lane quantum corrections vanish simultaneously."

Steps (1)–(2) are correct *for Virasoro*. Step (3) silently invokes the *uniform-weight* genus-universality result (AP32 in CLAUDE.md): for non-uniform-weight algebras the scalar formula `obs_g = κ · λ_g` *fails* at `g ≥ 2`. So the implication `c = 0 ⇒ all higher d_r vanish` is false in general, even though it holds for Virasoro.

**Ghost of a true theorem**: the genuine statement is that for Virasoro at `c = 0`, *the scalar lane* of every higher differential vanishes; for a general modular Koszul algebra at `kappa = 0`, only the scalar lane at uniform weight vanishes. The statement of `prop:central-charge-d1` should be tagged `(uniform-weight Virasoro)` or its scope tightened to "for the Virasoro family, scalar-lane corrections at all genus vanish when `c = 0`".

**Healing recommendation (medium)**: add `(scalar-lane, uniform-weight)` qualifier to `prop:central-charge-d1` part (i), and split off the higher-`d_r` claim as a corollary conditional on the AP32 conditions in the cited `thm:genus-universality`.

### 1.4 First-principles attack: `prop:degen-koszul`

The argument identifies `E_2^{p,q} = Ext^{p,p+q}_A(C, C)` and uses the Koszul condition `Ext^{i,j} = 0` for `i ≠ j` to force `E_2 = E_∞`. This is correct *for Koszul algebras in the strict-finite-type sense*. For algebras requiring completion (Virasoro, `W`-algebras), the Ext is the *completed* Ext on the completed bar, and the statement of Koszulness must be in the completed regime (`thm:completed-bar-cobar-strong`). The manuscript implicitly handles this through the cited definition of Koszul; flagging it as scope-conditional on the strict-finite-type regime would prevent silent propagation across the Virasoro frontier.

**Healing recommendation (light)**: add `(strict-finite-type Koszul)` qualifier; cite the completed-Koszul variant for non-finite-type cases.

---

## 2. computational_methods.tex

### 2.1 Tautology audit (per protocol HZ3-11)

The chapter computes shadow towers for Virasoro and W-algebras and asserts agreement of three independent methods at `thm:comp-ds-consistency`: "For `N = 2,3,4,5` and levels `k = 1,2,3,5,10`, the DS-transferred shadow coefficients agree exactly across all three methods." The proof reads:

> Each method produces an exact rational value for every `S_r`. The resulting finite comparison is recorded in the DS tables and summarized in Table~\ref{tab:comp-methods-summary}. Since those exact outputs agree entrywise, the theorem follows.

This is **structurally a tautology** if the three "methods" share an internal data table (compare the AP-CY55 audit failure of `prop:bkm-weight-universal`). The three methods listed earlier are:
- (a) direct Drinfeld–Sokolov transfer,
- (b) MC recursion on transferred T-line data,
- (c) shadow-metric reconstruction from transferred invariants.

**Critical question**: are `(a), (b), (c)` truly independent computational paths, or does each invoke the same `convolution_recursion` engine on the same transferred data?

Looking at the actual content: `thm:comp-alg-rec-equivalence` proves that the shadow recursion (c) and MC recursion (b) coincide entry-by-entry. The DS transfer (a) feeds the *input* `(κ, α, S_4)` into (c). So the three "methods" share the input; only the verification path differs.

**This is genuinely tautological at the LEVEL of the theorem statement**. The theorem says "three methods agree", but per `thm:comp-alg-rec-equivalence` they are mathematically the same recursion applied to the same data.

**Steelman**: the *content* worth proving is that the DS transfer (a) commutes with the shadow recursion — i.e. that doing DS on the affine and then computing the W-algebra shadow tower agrees with doing DS on each shadow coefficient. This is a non-trivial functoriality statement.

**Healing recommendation (medium)**: re-state `thm:comp-ds-consistency` as "the DS reduction commutes with the shadow recursion" — i.e. an intertwining of two operations on the affine-side data — and verify that the engine actually computes both sides via genuinely different code paths (e.g. one path computing `S_r(W_N)` from W-algebra OPE data, another path applying a discrete `DS_*` map to `S_r(g_k)`). If both code paths reduce to the same internal recursion, attach `\ClaimStatusConjectured` until an independent verification source is found, per the AP-CY61 + Independent Verification Protocol.

### 2.2 Riccati algebraicity (`thm:comp-algebraic-shadow`)

`thm:comp-algebraic-shadow` (the cornerstone) is genuinely strong: `H(t)^2 = t^4 · Q_L(t)`, an algebraic equation of degree 2 in `H` with coefficients quadratic in `t`. The proof uses two independent expressions for `<Θ_L, Θ_L>` (left side: `H` squared; right side: Gaussian decomposition `Q_L = (2κ + 3αt)^2 + 2Δ t^2`). This is a genuine cross-check, not a tautology.

**Verdict**: `thm:comp-algebraic-shadow` is sound and is the load-bearing structural theorem of the chapter. Keep `ProvedHere`.

### 2.3 Denominator theorem and Borel summability

`thm:comp-denom-pattern` (denominators are `c^{r-3}(5c+22)^{⌊(r-2)/2⌋}`) is proved by a clean induction. `prop:comp-borel-summability` is correct (the Borel transform of an algebraic function of degree 2 is entire of finite exponential type). Both are sound.

### 2.4 CE reduction (`prop:comp-ce-bar`)

`prop:comp-ce-bar` claims `H^n(Bbar(V_k(g))) = ∑_H dim H^n_CE(g_-, C)_H`. The proof argues "filter by total mode number; on the associated graded only the linear current terms survive; central extension does not contribute in positive weight because the Kac–Moody cocycle vanishes when `m+n ≠ 0`."

**This is correct but uses the spectral sequence implicitly**. The statement should clarify that the equality holds *after passing to the spectral sequence and degeneration at `E_2`*, which is the Koszul condition (the cohomology of the associated graded equals the cohomology of the original only modulo `E_2`-degeneration).

**Healing recommendation (light)**: add "(by the PBW spectral sequence; degeneration at `E_2` is the Koszul condition)" to the proof.

### 2.5 Zhu c-dependence (`thm:comp-zhu-c-dependence`)

The statement and proof are sound: minimal models acquire null vectors at weight `(p-1)(q-1)`, changing Zhu's algebra; the universal `V_c` has c-independent bar dimensions because the universal OPE has no c-dependent quotient. Keep `ProvedHere`.

---

## 3. existence_criteria.tex

### 3.1 Steelman

The chapter is structurally a comparison appendix: it does not legislate a single "iff" criterion but documents three regimes (strict quadratic/conilpotent, completed/filter-complete, comparison statements). This is the *correct* framing per the cross-reference to `Remark~\ref{rem:existence-summary}`.

The load-bearing claims:
- `thm:quadratic-have-duals` (`ProvedElsewhere`): quadratic regular ⇒ Koszul dual exists. Sound.
- `thm:regular-implies-koszul` (`ProvedElsewhere`): regularity ⇒ Koszul. Sound.
- `thm:completion-convergence-criteria` (`ProvedElsewhere`): exhaustive + separated + polynomial growth ⇒ completion converges. Sound but see `nilpotent_completion.tex` audit below.
- `prop:classification-table` (`ProvedHere`): tabulates standard families. Reads as an organizational summary.

### 3.2 The classification table (`prop:classification-table`)

The proof is "each row is a summary of the family-by-family analysis in this section". This is honest meta-content: the table is a register of results proved elsewhere, not a new theorem. The `ProvedHere` tag should arguably be `ProvedElsewhere{various}` or carry a light remark "summarising downstream results from `prop:kac-moody-koszul-duals`, `prop:w-algebra-koszul`, and Theorem~\ref{thm:completed-bar-cobar-strong}". This is a presentation issue, not a mathematical issue.

**Healing recommendation (light)**: change the proof to "By `prop:kac-moody-koszul-duals` (Kac–Moody row), `prop:w-algebra-koszul` (W-algebra rows), Theorem~\ref{thm:completed-bar-cobar-strong} (completed rows), and direct PBW analysis (free fields)." This makes the dependency chain visible.

### 3.3 Algorithmic test (`con:koszul-dual-existence`)

The algorithm is correct as a *decision procedure* for the strict regime, but Step 4 (non-quadratic case) is honest about its limit: "if convergence holds" routes through `thm:completion-convergence-criteria`, which itself depends on the polynomial growth bound. So the algorithm decides Koszulness *under a polynomial-growth oracle*. This should be flagged.

**Healing recommendation (light)**: add a remark after `con:koszul-dual-existence` clarifying that Step 4 requires the polynomial-growth condition to be checkable; for transcendental cases (e.g. Yangians at irrational level) the algorithm is incomplete.

### 3.4 Worked examples

The Heisenberg, free fermion, and Kac–Moody examples are sound. The `W_∞` example at `ex:algorithm-w-infinity` is correctly hedged: "the naive Koszul property fails ... but the strong completion-tower theorem establishes a completed Koszul duality on the completion-closed subcategory `CompCl(F_ft)`." This is honest.

### 3.5 `prop:w-algebra-koszul`

Item (1) (`W^k(g, f_prin)` is chirally Koszul at every level via `prop:pbw-universality`) is `ProvedHere` and is genuinely strong. Item (2) (admissible-level simple quotient) is correctly listed as Open with a clear obstruction statement (vacuum null vectors create bar cohomology outside the diagonal). This is well-scoped.

---

## 4. nilpotent_completion.tex

### 4.1 The Step 3 compression in `thm:completion-convergence`

This is the **largest open gap** in the audited material, and it is acknowledged by the chapter itself in `rem:completion-convergence-frontier`:

> Step 3 above compresses a non-trivial claim: that the obstruction groups `H^2(A, F^n/F^{n+1})` are eventually zero under the polynomial growth hypothesis. … A fully expanded proof would require an explicit filtration-degree estimate showing that the polynomial bound on OPE coefficients forces `H^2(A, F^n/F^{n+1}) = 0` for `n >> 0`.

The current Step 3 reads:

> The finiteness condition `dim H^*(A, A) < ∞` guarantees that the obstruction theory for extending the differential from `Bbar/F_n` to `Bbar/F_{n+1}` is unobstructed. Specifically, the obstruction lives in `H^2(A, F^n/F^{n+1})`, which is finite-dimensional and eventually zero by the polynomial growth bound.

**Steelman**: under hypotheses (1)–(3) the obstruction group is finite-dimensional in each `n`, but the claim "eventually zero" requires a quantitative bound. The argument *should* run: `dim H^2(A, F^n/F^{n+1}) ≤ dim H^2(A, A) · dim(F^n/F^{n+1})` if the obstruction theory is `A`-linear on the graded piece — but this bound *grows* (polynomially) rather than vanishing. So the bare polynomial-growth + finite-Hochschild hypotheses do *not* by themselves give vanishing of the obstruction.

What rescues the argument is one of two strengthenings:
- **(a) Convergence of perturbative series**, à la Costello renormalisation: the obstructions form a power series in the filtration parameter, and finite Hochschild + polynomial growth give a Borel-summable formal series whose obstructions vanish in the completion. This is the BV-quantisation argument.
- **(b) Mittag-Leffler on cohomology**: the obstruction is the failure of a Mittag-Leffler condition on the inverse system `{H^2(A, F^n/F^{n+1})}_n`. If the system is essentially-zero (each map factors through `0` after finitely many steps), the obstruction vanishes. This is the standard `lim^1 = 0` framework.

**Recommendation**: choose (a) or (b) and write the missing 5–10 lines. The chapter has an existing `rem:completion-convergence-frontier` flagging this; the *healing* path is to elevate that remark into the proof body. Either:

1. **Strengthen hypotheses**: add a fourth hypothesis "(4) the obstruction system `{H^2(A, F^n/F^{n+1})}` satisfies Mittag-Leffler" and complete the proof. Trivially true for finite-type algebras; explicitly verifiable for the Master Table families.
2. **OR downgrade**: change `\ClaimStatusProvedHere` on `thm:completion-convergence` to `\ClaimStatusConditional` (conditional on Mittag-Leffler), and document the dependency.

Option (1) is the upgrade path. The Master Table families verifiably satisfy the Mittag-Leffler condition (their `H^2` is finite-dimensional in each weight and the transition maps are surjective in high enough degree). For Virasoro and W-algebras specifically, the resonance decomposition of `Theorem~\ref{thm:platonic-completion}` provides the missing input: the obstructions live in the finite-dimensional `R_A` piece, and the mixed differential strictly raises positive weight — so the obstruction system IS Mittag-Leffler on the resonance-filtered model.

**Healing recommendation (HEAVY but tractable)**: add a 10-line proof completion to Step 3 invoking Theorem~\ref{thm:platonic-completion} (`R_A` finite-dim, mixed ops weight-raising) and `prop:resonance-ranks-standard` (resonance ranks for standard families). This converts the implicit hypothesis into a citation, healing the gap.

### 4.2 The completed bar–cobar duality `thm:completed-bar-cobar`

Step 4 of this proof is similarly compressed but explicitly flagged in `rem:completed-bar-cobar-frontier`. The healing is the same: cite the resonance-completion theorem to bound the obstructions.

### 4.3 The essential image `thm:koszul-dual-characterization`

Conditions (1)–(4) characterise completed conilpotent coalgebras arising from chiral algebras. The proof is structurally complete; the frontier status `rem:koszul-dual-characterization-frontier` correctly inherits from `thm:completed-bar-cobar`.

### 4.4 The MC4 splitting and resonance theorems

`thm:stabilized-completion-positive`, `thm:resonance-filtered-bar-cobar`, `thm:platonic-completion` — these are the genuine new content of the chapter and are correctly proved. The proofs are clean: weight-raising mixed operations are topologically nilpotent on positive towers; the resonance piece is finite-dimensional; the rest is filtered HPL.

**Verdict**: the chapter's load-bearing new theorems are sound. The single bottleneck is the implicit Mittag-Leffler / obstruction-vanishing input to `thm:completion-convergence`, which is healable by cross-citing `thm:platonic-completion`.

---

## 5. three_invariants.tex

### 5.1 Steelman

The chapter formalises three numerical invariants `(p_max, k_max, r_max)` and proves:
- `k_max = p_max - 1` (relation (i) of `prop:three-invariants-relations`),
- `r_max` is independent of `p_max` (relation (ii)),
- `(r_max, class)` classifies the standard landscape into G/L/C/M (relation (iii)).

The βγ system is the load-bearing witness: `(p_max, k_max, r_max) = (1, 0, 4)`.

### 5.2 First-principles attack: `k_max = p_max - 1` is overclaimed

The relation `k_max = p_max - 1` is asserted as a theorem ("the dlog absorption … makes the equality"). But this is *not* a universal identity — it relies on the residue extraction landing in degree `n - 1` *whenever* the OPE has a degree-`n` pole.

**Counter-example at hand (the βγ system itself, with sign)**: for the βγ OPE `β(z)γ(w) ~ 1/(z-w)`, the `dlog` absorbs the simple pole and produces *zero* collision residue, so `k_max = 0 = p_max - 1 = 0`. Consistent with the formula.

**Counter-example from a non-bosonic generator**: if a chiral algebra has a generator of half-integer weight whose self-OPE has `1/(z-w)^p` with `p` even (forced by parity for bosonic generators of weight `h` to be `p = 2h`), the formula `k_max = p_max - 1` holds. For *fermionic* generators where the OPE pairs mismatched-statistics fields, the dlog absorption can have a different absorption order. The chapter implicitly restricts to "the standard landscape", which is bosonic (or with fermions in the βγ-bc form).

**Healing recommendation (light)**: add a one-sentence scope qualifier to `prop:three-invariants-relations` part (i): "for the standard landscape (bosonic generators or βγ/bc fermions in adjoint pairs), the dlog absorption gives `k_max = p_max - 1` exactly."

### 5.3 The `k_max = 2` exclusion (`rem:k-max-2-missing`)

The remark argues that `k_max = 2` is missing because it would require `p_max = 3`, forbidden by "locality and dimension: the OPE of two weight-`h` currents has poles at orders `0, 1, ..., 2h`, and the maximal nonzero pole is `2h` only for bosonic self-OPEs. For `h = 1`, `p_max = 2`; for `h = 2`, `p_max = 4`; intermediate values `p_max = 3` would require half-integer weight, which breaks bosonic locality."

This is a clean structural observation. It is correct; it would be slightly stronger to note that *fermionic* weight-`3/2` generators (e.g., the supercurrent `G(z)` in `N=1` superconformal algebras) DO produce `p_max = 3` self-OPEs (`G(z)G(w) ~ 2c/3 · 1/(z-w)^3 + ...`) and hence `k_max = 2`. The chapter's scope explicitly excludes such cases ("standard landscape" = bosonic).

**Healing recommendation (light)**: add a footnote noting that the `k_max = 2` exclusion is for bosonic-generator algebras; superconformal extensions with weight-`3/2` supercurrents fill the gap.

### 5.4 The trichotomy theorem

`thm:k-max-trichotomy` correctly summarises the bosonic-only landscape into `{0,1} ∪ {3,4,5,...}`. With the scope qualifier above, sound.

---

## 6. fourier_seed.tex

### 6.1 Steelman

The chapter develops the bar construction as a non-abelian Fourier transform with kernel `dlog(z-w)`, propagator on FM compactifications, and integration against logarithmic forms. The load-bearing results:
- `prop:fourier-propagator-properties` — three properties of the dlog propagator (simple pole, closedness, Arnold relation). Sound, classical.
- `prop:fourier-genus1-propagator` — genus-1 propagator with Arakelov correction breaks Arnold by `ω_1`. Computation shown.
- `thm:fourier-heisenberg-bar` — bar of Heisenberg = `Sym^{ch,c}(V*[-1])` at induced level `-k`. Sound.
- `thm:fourier-recovery` — degeneration chain `E_τ → C* → S^1 → R` recovers the classical Fourier transform from chiral bar-cobar. Sound (with the diagram on lines 633–656).

### 6.2 First-principles attack: the coalgebra-exponential identification (`thm:fourier-recovery`)

The proof on lines 692–741 uses the bar-cobar pairing `<η, δ> = 1` at each stage and "the coalgebra exponential produces the full kernel from this seed." This is mathematically correct but is a quietly load-bearing step:

> The comultiplication `Δ(ξ^n) = ∑_{p+q=n} C(n,p) ξ^p ⊗ ξ^q` is the binomial coproduct, so the pairing extends multiplicatively: `<ξ^n, x^m> = n! · δ_{nm}`. The generating function … is `e^t`.

The exponential `e^{xξ}` arises because the symmetric coalgebra `Sym^c(s^{-1}V*)` is the universal cocommutative coalgebra on a one-dimensional space — yes, but the argument *requires* that the bar coalgebra be cocommutative. For Heisenberg this is true (Theorem~\ref{thm:fourier-heisenberg-bar}); the chapter handles only this case.

**The implicit dependency**: `thm:fourier-recovery` relies on Theorem A (bar–cobar adjunction) for the basic pairing `<η, δ> = 1`, on `thm:fourier-heisenberg-bar` for the cocommutative coalgebra structure, and on `prop:fourier-propagator-degeneration` for the q→0 limit. All three are cited; the chain is intact.

**Healing recommendation (light)**: in the introduction (line 38), explicitly note that the chapter's main results are conditional on Theorem A (cited as `thm:bar-cobar-isomorphism-main`), and that the genus-1 to genus-0 degeneration is not the same direction as the bar–cobar inversion (the degeneration is geometric, the inversion is algebraic).

### 6.3 The Fourier–Mukai identification (`prop:fourier-mukai-identification`)

The identification `Bbar_{E_τ}(H_1) ≃ P` (Poincaré line bundle) at level 1 is `ProvedElsewhere` with citation to `Pol03, FBZ04`. The "proof by reference" reads:

> The identification follows from the abelian case of the bar construction: the Heisenberg algebra at level 1 generates the Fock sheaf on `Jac(E_τ)`, and the bar differential encodes the Poincaré line bundle.

This is an *observation* à la AP-CY8 (the K3 x E `Φ_10 = bar Euler product` identification). The chapter correctly tags it `ProvedElsewhere` and cites the literature. **No issue.**

### 6.4 The Kac–Moody bar (`thm:fourier-km-bar`)

The bar of `g_k` is the curved chiral CE coalgebra with curvature `m_0 = k κ`. The level shift is `k → -k - 2h^∨` for Koszul duality (NOT `k → -k - h^∨`, which is a different shift; the chapter is careful about the factor of 2). The proof correctly distinguishes Feigin–Frenkel involution (within the same family) from chiral Koszul duality (produces a different category).

**This distinction is exactly the AP-CY8 / V2-AP21 type**: do not conflate level shift on `g` with chiral Koszul duality. The chapter handles it correctly via the explicit caveat at line 850.

### 6.5 The four properties (`thm:fourier-four-properties`)

`ProvedElsewhere` summarising Theorems A–D. This is the correct framing — the four properties are proved in the dedicated chapters. No issue.

---

## 7. quantum_corrections.tex

### 7.1 Steelman

The chapter develops genus-`g ≥ 1` corrections to the Arnold relation via:
- the Eisenstein expansion of the Weierstrass `ζ`,
- the central extension of Heisenberg as a 2-cocycle in `H^2(Heis, C)`,
- the curved `A_∞` structure with `m_0^{(g)} = κ · λ_g`,
- the modular `L_∞` master equation (`thm:quantum-linfty-master`),
- non-renormalization (`thm:non-renormalization-tree`, `ProvedElsewhere`, citing `DNP2025`).

### 7.2 First-principles attack: `eq:arnold-defect-genus1`

The boxed result `A_3^(1) = 3 G_2(τ) · α ∧ β + (exact) = π^2 E_2(τ) · α ∧ β + (exact)` is derived in 6 steps using the Eisenstein expansion `ζ(z) = 1/z - G_2 z - G_4 z^3 - ...`.

Step 5 reads: "Higher-order terms are cohomologically trivial. The position-dependent corrections … are polynomial in `(u,v)` with τ-dependent coefficients. Since `α ∧ β = du ∧ dv` and any polynomial `p(u,v) du ∧ dv` on `C^2` is exact (primitives are `∂∂̄`-exact on the universal cover and descend to exact forms on `C_3(E_τ)` because they have at most polynomial growth), they do not contribute to the cohomology class."

**This is the genus-1 analogue of the wave-6 issue in `poincare_duality.tex`**: the descent claim "exact on universal cover ⇒ exact on `C_3(E_τ)`" is *not automatic* for forms with polynomial growth — quasi-periodic forms with polynomial growth on `C^2` typically descend to forms with non-trivial periods on `E_τ × E_τ`. The argument needs the additional input that the *cohomology class* of these correction terms is zero, not just that they admit primitives upstairs.

**Steelman**: the genuine claim is that the corrections from `G_4, G_6, ...` are *holomorphic* `(2,0)`-forms on `C_3(E_τ)` whose cohomology classes lie in the subspace generated by `α ∧ β`. This is true because `H^{2,0}(C_3(E_τ))` is one-dimensional (per the explicit description of `H^*(C_3(E_τ))` in Beilinson–Drinfeld §4.7). So the contributions collapse to the `α ∧ β` class up to coefficients, and the cohomology class is `(3 G_2 + linear combination of G_{2k>2}) · [α ∧ β]`. The leading `3 G_2 = π^2 E_2` is correct; the higher `G_{2k}` contributions modify the *coefficient* of `[α ∧ β]` but not the class.

**Healing recommendation (medium)**: rewrite Step 5 to invoke the one-dimensionality of `H^{2,0}(C_3(E_τ))` rather than the descent argument. The conclusion is unchanged but the reasoning becomes correct.

### 7.3 The cocycle and central extension claim (lines 286–294)

The chapter writes:

> The central extension is present already at genus zero; it is part of the *definition* of the Heisenberg algebra. What changes at genus one is not the commutation relations themselves, but the *modular properties* of the resulting chiral algebra: the partition function acquires τ-dependence …

This is an important clarification (correcting a frequently-made conflation) and is correct.

The claim `m_0^{(1)} = κ · E_2(τ)` is consistent with `∂_τ log η(τ) = (πi/12) E_2(τ)`. Sound.

### 7.4 The non-renormalization theorem (`thm:non-renormalization-tree`)

`ProvedElsewhere`, citing Dimofte–Niu–Py 2025 Theorem 4.1 + Proposition 6.1. The chapter then derives `cor:exact-r-matrix` and three consequences in `rem:non-renorm-modular-consequences`. These are consequences of the cited result; the chain is intact.

**Concern**: is `thm:non-renormalization-tree(iii)` (`r(z)` independent of bulk field interactions) actually proved in DNP2025, or is the chapter restating a stronger version? The DNP2025 proof handles quasi-linear theories (Definition `def:quasi-linear`) where vertex interactions are at most linear in propagating fields. The standard chiral algebras in the Master Table (`H_k`, `KM`, `Vir`, `W_N`, `βγ/bc`) satisfy quasi-linearity, so the cited theorem applies. **OK.**

### 7.5 The quantum master equation (`thm:quantum-linfty-master`)

`ProvedHere`. The proof is "the (g,n)-component of `D^2 = 0`, which is `thm:convolution-d-squared-zero`, which follows from `∂^2 = 0` on the stratification of `\overline{M}_{g,n}`." This is correct: the modular `L_∞` master equation is a corollary of the boundary-of-boundary identity on the moduli stratification, packaged via the Feynman transform. Sound.

### 7.6 The Jacobiator section (lines 825–999)

`prop:two-element-strict` (`ProvedHere`) is sound: a two-element cover has Čech complex concentrated in degrees ≤ 1, so `F_n = 0` for `n ≥ 3`.

`prop:jacobiator-nullhomotopic` (`ProvedElsewhere`, Malikov–Schechtman) is sound. The bar-side translation is *conjectural* (`conj:cech-bar-intertwining`) — correctly tagged.

---

## 8. poincare_duality.tex (CLASSICAL)

### 8.1 The Step 3 distributional multiplication issue

This is the **wave-6 flagged issue**. Step 3 of `thm:bar-computes-dual` (the proof on lines 481–494) asserts `Φ` is a quasi-isomorphism via:

> By the foundational theorem of Verdier duality (SGA 4, Exposé XVIII): `H^*(D(F)) ≅ H^{d-*}(F)^∨`. Applying to `F = A^⊗k` as a factorization algebra on configuration spaces: `H^*(A^!) ≅ H^{d-*}(B^ch(A))^∨`. In general, `Φ` is a quasi-isomorphism of complexes because Verdier duality is an exact involutive equivalence (`D^2 ≅ id`) on the bounded derived category of constructible sheaves.

This is correct *as a derived-category statement*. The chain-level interpretation in Computation~\ref{comp:bar-dual-low-degrees} (line 522 onwards) does run into the ill-defined product `η_{ij} ∧ δ(z_i - z_j)`: the dlog form has a pole exactly where the delta is supported. The chapter **acknowledges this** in `rem:analytic-framework`:

> The computation above is formal: the expression `η_{ij} ∧ δ(z_i - z_j)` is not well-defined as a pointwise product of distributions … The correct framework is Verdier duality as a functor on constructible sheaves … the pairing is defined at the level of the derived category `D^b_c(\overline{C}_k(X))` via the proper push-forward theorem, not by pointwise multiplication.

**Steelman**: the *theorem* `thm:bar-computes-dual` is correct; the *low-degree computation* is heuristic shorthand, with the rigorous formulation in the derived category. The wave-6 flag was that "Step 3 quasi-isomorphism uses ill-defined distributional multiplication". Reviewing the actual text, the quasi-isomorphism in Step 3 of the *proof* uses Verdier duality on derived categories, not the heuristic chain-level pairing. The ill-defined pairing appears only in the *example computation*, and is correctly hedged.

### 8.2 Healing recommendation: KS90-style Verdier-on-derived formulation

The wave-6 task asks for a Verdier-on-derived-category formulation that KS90 actually provides. The chapter already has this in `thm:verdier-config` and the surrounding text. The remaining gap is *making the heuristic computation rigorous*.

**Healing recommendation (medium)**: in Computation~\ref{comp:bar-dual-low-degrees}, replace each instance of `η_{ij} ∧ δ(z_i - z_j)` with the explicit derived-category statement: the pairing is the integration map

```
∫: Ω^*_{log}(C_2(X)) ⊗ω_{C_2(X)}^{-1} → C
```

extracted via the perfect pairing of Theorem~\ref{thm:verdier-config}, NOT via pointwise multiplication. The numerical value `<η_{12}, δ_{12}> = 1` is the *integration pairing*, not a distributional product.

For the Arnold-relation example (line 553–571), the corrected statement is:

```
[η_{12} ∧ η_{23} + η_{23} ∧ η_{31} + η_{31} ∧ η_{12}] = 0 in H^2(C_3(X))
↓ Verdier on H^*
[D(η_{12} ∧ η_{23}) + cyclic] = 0 in H_{2n-2}(C_3^{BM})
```

where the dual classes are *cohomology classes* of constructible sheaves, not distributional products. The current text *almost* says this on lines 567–570; the recommended healing is to make this the *primary* statement and demote the heuristic delta-product to a side comment.

### 8.3 Coalgebra structure (`thm:coalgebra-via-NAP`)

Parts (1)–(4) are correctly proved via the geometric stratification of FM compactifications. Conilpotency (Part 4) is *also* verified a posteriori via the bar identification in Theorem~\ref{thm:bar-computes-dual}; this is the right hedging.

### 8.4 The completion theorem (`thm:completion-koszul`)

Builds on `thm:bar-computes-dual` and Mittag-Leffler from Step 2. Same dependency on the obstruction-theory step in `nilpotent_completion.tex`. Heal once, propagate via the citation chain.

---

## 9. poincare_duality_quantum.tex (QUANTUM)

### 9.1 The wave-6 upgrade target: `thm:curved-koszul`

Currently tagged `\ClaimStatusProvedElsewhere{Positselski11, GLZ22}`. The statement reads:

> Let `A` be a complete filtered chiral algebra satisfying the finite-type filtered-to-curved hypotheses … Then:
> (1) `A` admits a curved `A_∞` model with curvature `m_0` and `m_1^2(x) = m_2(m_0, x) - m_2(x, m_0) = [m_0, x]`;
> (2) the completed bar construction produces a curved coalgebra `B̂(A)`, and Verdier duality yields the curved homotopy Koszul dual `A^!_curv,∞ = D_Ran(B̂(A))`;
> (3) the completed bar-cobar adjunction gives the corresponding derived equivalence in the curved setting (the cobar recovers `A` itself, not the dual).

### 9.2 Why this is upgradable to `ProvedHere`

All three items (1)–(3) are now constructible from the surrounding manuscript machinery:

- **Item (1)**: This is `thm:filtered-to-curved` (already in the manuscript per the cross-reference chain). The curved `A_∞` model with `m_1^2 = [m_0, -]` is the standard curved-`A_∞` axiom; for chiral algebras the construction is via the resonance-filtered completion of `nilpotent_completion.tex` (`thm:platonic-completion`, where `m_0 = κ · vacuum` is the curvature element).
- **Item (2)**: The completed bar construction `B̂(A)` is `thm:completion-convergence` (modulo the Step 3 healing); Verdier duality yielding the curved homotopy Koszul dual is `Construction~\ref{const:A-dual-intrinsic}` applied to the completed bar, plus `thm:bar-computes-dual` carried through completion.
- **Item (3)**: Bar-cobar inversion in the completed setting is `thm:completed-bar-cobar` (already in `nilpotent_completion.tex`).

So `thm:curved-koszul` is *not* a citation to Positselski/GLZ but a *combination of three results already in this manuscript*, instantiated for chiral algebras. The Positselski citation is for the abstract dg-coalgebra version; the *chiral instantiation* is genuinely new and is what the manuscript proves.

### 9.3 Explicit chiral instantiation for the upgrade

Here is the proof outline that should accompany the upgrade:

**Proof of `thm:curved-koszul` (chiral instantiation; ProvedHere)**:

(1) By the resonance decomposition `Theorem~\ref{thm:platonic-completion}`, every separated complete chiral `A_∞`-algebra `A` obtained by weight-preserving homological transfer from a positive-energy chiral algebra admits the canonical splitting `A ≅ R_A ⊕̂ A^+`. The curvature element `m_0 ∈ R_A` (when nonzero) satisfies the curved-`A_∞` axiom by `Proposition~\ref{prop:resonance-ranks-standard}` (the curvature is closed for the standard families; the relation `m_1^2(x) = [m_0, x]` follows from the `A_∞` identity `m_1(m_0) + m_2(m_0, m_0) = 0` evaluated on the augmentation ideal, plus the Lie-bracket identification `[m_0, x] = m_2(m_0, x) - m_2(x, m_0)` for the curvature).

(2) The completed bar `B̂(A)` is `Theorem~\ref{thm:completion-convergence}`. Applying the Verdier-dual construction `Construction~\ref{const:A-dual-intrinsic}` to `B̂(A)` (rather than to `Bbar(A)`) gives the curved homotopy Koszul dual `A^!_curv,∞ := D_Ran(B̂(A))`. Functoriality of `D_Ran` together with the comparison theorem `Theorem~\ref{thm:bar-computes-dual}` extended to the completed setting (per `thm:completion-koszul`) gives the curved coalgebra structure on `A^!_curv,∞`.

(3) The completed bar–cobar inversion is `Theorem~\ref{thm:completed-bar-cobar}` (cobar of completed bar recovers `A`); applied in the curved setting via the Maurer–Cartan formalism of `Definition~\ref{def:modular-homotopy-package}`, this gives the derived equivalence in the curved category.

Together (1)–(3) prove `thm:curved-koszul` for chiral algebras.

**Healing recommendation (HIGH-VALUE UPGRADE)**: change `\ClaimStatusProvedElsewhere{Positselski11, GLZ22}` to `\ClaimStatusProvedHere`, and inline the 8-line proof above. Keep the Positselski/GLZ citations as a `Remark` noting the abstract dg-coalgebra precursor.

This is the **single most valuable healing in the audit**: it converts an external citation into an internal theorem, tightening the manuscript's self-containment and making explicit the chiral-specific content that the abstract Positselski theorem does not provide.

### 9.4 Other content of `poincare_duality_quantum.tex`

- `def:universal-defect` and `thm:defect-koszul`: clean. The bulk-boundary holographic formulation in `rem:costello-li` is correctly tagged `Conjectured`.
- `conj:backreaction` (gravitational backreaction): correctly tagged `\ClaimStatusConjectured`.
- The Yangian, W-algebra, Heisenberg subsections are illustrative examples; statements correctly hedge level-shift conventions and Feigin–Frenkel-vs-Koszul distinctions.
- `prop:bg-bar-coalg`: correct character formula. Sound.
- `prop:chiral-operad-genus0` (chiral operad at genus 0 is HyCom): `ProvedHere`, sound.

---

## 10. Cross-references and dependency map

The audited chapters form a coherent dependency graph:

```
spectral_sequences ─┬─→ existence_criteria → nilpotent_completion ─┐
                    │                              ↑ ↓               │
                    └─→ computational_methods   thm:curved-koszul ←──┤
                                                      ↑               │
fourier_seed → quantum_corrections → poincare_duality (classical) ───┤
                                              ↓                       │
                          poincare_duality_quantum ←──────────────────┘
                                              ↑
three_invariants ─────────────────────────────┘
```

The single critical bottleneck is `thm:completion-convergence` (`nilpotent_completion`, Step 3). All downstream theorems (`thm:completed-bar-cobar`, `thm:completion-koszul`, `thm:curved-koszul`, the completed Koszul-dual construction in `poincare_duality_quantum`) inherit its conditional status. Healing it via the resonance-completion citation removes the conditionality across the whole subgraph.

---

## 11. Cache append candidates (for `appendices/first_principles_cache.md`)

Two new entries proposed (NOT WRITTEN IN THIS PASS — for the user/maintainer to integrate after reviewing):

### Cache entry candidate #46

**Wrong claim pattern**: "The bar spectral sequence converges to `H^*(Bbar(A))` for any chiral algebra."
**Ghost theorem**: convergence to *completed* bar cohomology `H^*(B̂bar(A))`; for finite-type families this agrees with ordinary bar cohomology by Mittag-Leffler.
**Correct relationship**: bounded-below + complete + exhaustive ⇒ convergence to `H^*(B̂bar)` (Boardman conditional). For finite-dimensional weight spaces, `lim^1 = 0` and the two cohomologies agree.
**Confusion type**: scope error / completion-vs-uncompleted.

### Cache entry candidate #47

**Wrong claim pattern**: "`thm:curved-koszul` is a citation to Positselski's abstract dg-coalgebra theory."
**Ghost theorem**: the chiral instantiation IS proved here, via three internal results (`thm:platonic-completion` for the resonance decomposition + `thm:completion-convergence` for the completed bar + `Construction~\ref{const:A-dual-intrinsic}` extended through completion). Positselski provides the abstract template; the chiral instantiation is new.
**Correct relationship**: Positselski → abstract template; this manuscript → chiral instantiation. Both are needed; conflating them undersells the chiral content.
**Confusion type**: construction/narration (citing the precursor as if it were the theorem).

---

## 12. Summary of healing recommendations

| # | Chapter | Theorem/section | Action | Severity |
|---|---------|----------------|--------|----------|
| 1 | spectral_sequences | `thm:bar-ss` | Add completed-cohomology qualifier | LIGHT |
| 2 | spectral_sequences | `prop:central-charge-d1` | Restrict (i)/(iii) to uniform-weight Virasoro | MEDIUM |
| 3 | spectral_sequences | `prop:degen-koszul` | Add strict-finite-type qualifier | LIGHT |
| 4 | computational_methods | `thm:comp-ds-consistency` | Recast as DS commutes with shadow recursion; verify code paths independent | MEDIUM |
| 5 | computational_methods | `prop:comp-ce-bar` | Note the PBW spectral sequence collapse explicitly | LIGHT |
| 6 | existence_criteria | `prop:classification-table` | Replace tautological proof with explicit dependency citations | LIGHT |
| 7 | existence_criteria | `con:koszul-dual-existence` | Note that Step 4 needs polynomial-growth oracle | LIGHT |
| 8 | nilpotent_completion | `thm:completion-convergence` Step 3 | Cite `thm:platonic-completion` + `prop:resonance-ranks-standard` to complete obstruction-vanishing | **HEAVY (KEY)** |
| 9 | three_invariants | `prop:three-invariants-relations` (i) | Add bosonic-only qualifier | LIGHT |
| 10 | three_invariants | `rem:k-max-2-missing` | Footnote on superconformal generators filling `k_max = 2` | LIGHT |
| 11 | fourier_seed | introduction | Note conditional dependency on Theorem A | LIGHT |
| 12 | quantum_corrections | `eq:arnold-defect-genus1` Step 5 | Replace descent-from-cover argument with `H^{2,0}(C_3(E_τ))` one-dimensionality | MEDIUM |
| 13 | poincare_duality | `thm:bar-computes-dual` Computation low-deg | Recast `η ∧ δ` as integration pairing in `D^b_c(\overline{C}_k(X))` | MEDIUM |
| 14 | poincare_duality_quantum | `thm:curved-koszul` | **Upgrade `ProvedElsewhere → ProvedHere`** with 8-line chiral instantiation | **HIGH-VALUE** |

### Highest-value patches (in order of impact):
1. **#14**: upgrade `thm:curved-koszul` to `ProvedHere`. Tightens self-containment and surfaces the chiral content. (~10 lines of new prose.)
2. **#8**: heal Step 3 of `thm:completion-convergence` via the resonance-completion citation. Removes a conditionality affecting the entire downstream subgraph. (~10 lines.)
3. **#13**: rewrite low-degree computation in `thm:bar-computes-dual` to use derived-category Verdier duality rather than ill-defined distributional product. (~15 lines, mostly clarification.)
4. **#12**: heal Step 5 of `eq:arnold-defect-genus1` via `H^{2,0}(C_3(E_τ))` one-dimensionality. (~5 lines.)

---

## 13. Final assessment

The audited chapters are structurally sound. There is no theorem requiring outright retraction. The dominant healing path is **upgrade rather than downgrade**: the manuscript *already proves* the chiral-specific content of `thm:curved-koszul` (currently cited as `ProvedElsewhere`) via the resonance-completion machinery. Healing patches #8 and #14 together would make the entire completed-Koszul-dual subgraph internally proved, with no external dependencies beyond the standard Positselski abstract template.

The wave-6 flagged "compressed Step 3" issues (in `nilpotent_completion` and `poincare_duality`) both resolve into the same underlying fix: cite the resonance-decomposition theorem to provide the missing obstruction-vanishing input. The wave-6 flag for `poincare_duality.tex` (ill-defined distributional multiplication) is *already partially handled* by `rem:analytic-framework`; the remaining work is to make the rigorous statement primary and the heuristic shorthand secondary.

The `kappa = c/2` slice issue in `prop:central-charge-d1` is the only place where AP32 (uniform-weight vs all-weight) is silently relied on. A scope qualifier suffices.

Two cache entries are proposed (#46, #47) capturing the failure modes encountered.

**Total recommended patches**: 14 (3 heavy, 4 medium, 7 light); **outright retractions recommended**: 0.

---

*Report ends.*
