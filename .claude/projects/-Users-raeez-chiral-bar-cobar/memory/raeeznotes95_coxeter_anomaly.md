## raeeznotes95 Analysis (2026-03-19)

**Source**: 43K-line ChatGPT transcript, ~95% noise, ~5% signal.

### Claims Tested
- **Claim A (Coxeter anomaly in sign rep)**: REFUTED. Shadow amplitudes are symmetric tensors → trivial S_n rep. 44 tests in test_coxeter_anomaly.py.
- **Claim B (Chevalley-shadow correlation)**: TAUTOLOGICAL. Shadow depth n ↔ Chevalley rank n-1 is dimensional coincidence.

### Genuine Discoveries
1. **W_3 multi-variable quartic shadow**: Q_TTTT = 10/[c(5c+22)], Q_TTWW = 160/[c(5c+22)²], Q_WWWW = 2560/[c(5c+22)³]. First multi-generator shadow computation.
2. **Kac-shadow singularity principle**: Shadow denominators = Kac determinant factors. Null vector decoupling = shadow divergence.
3. **DS increases shadow depth**: V_k(sl_3) class L → W_3 class M. Composite Λ breaks quadratic OPE.
4. **T-line autonomy**: Sh_r(W_3)|_{x_W=0} = Sh_r(Vir) at all computed arities. Sub-VOA structure preserved by block-diagonal kappa.
5. **Denominator filtration by W-charge**: (5c+22)^{1+k} for 2k W-legs.

6. **W_4 two-propagator quartic**: W_4 has TWO weight-4 quasi-primaries (Λ and W_4 itself). Breaks uniform denominator filtration: Q_T4T4 = 64/c has NO (5c+22).
7. **Autonomy requires OPE-closedness**: thm:shadow-subalgebra-autonomy corrected. W_3 ⊂ W_4 is NOT OPE-closed (c334 coupling). Only Virasoro ⊂ W_N is OPE-closed.
8. **Cubic coefficient C_{TWW} = 3** (from T_(1)W = 3W), not 2 (from W_(3)W = 2T which is curvature).
9. **W-line alternating vanishing**: Sh_r|_{x_T=0} = 0 for odd r (parity argument).
10. **E_1 sign rep**: Vandermonde appears in ordered shadow as sign component; projected away by E_∞.

### Resolved Questions
- Kac-Chevalley factorization: **SPURIOUS** (Kac det and Chevalley disc are algebraically independent).
- Weight-6 quasi-primaries in W_3: dim = 4 (controls sextic shadow).
- kappa(W_N) = c·(H_N - 1) where H_N = harmonic number.

### Tex Content Added
- nonlinear_modular_shadows.tex: 4 theorems + 2 remarks (~250 lines)
- w_algebras.tex: W_3 archetype subsection with quartic channels, denominator filtration (~150 lines)
- concordance.tex: 2 new blocks

### Files Created
- `compute/lib/coxeter_anomaly_test.py` — S_n representation analysis
- `compute/lib/coxeter_arity4_deep.py` — rewritten for W_3/W_4 depth analysis
- `compute/lib/w3_multivariable_shadow.py` — W_3 quartic, corrected tower through arity 9
- `compute/lib/w4_multivariable_shadow.py` — W_4 two-propagator quartic, autonomy failure
- `compute/lib/kac_chevalley_test.py` — resolves open question as SPURIOUS
- `compute/tests/test_coxeter_anomaly.py` — 44 tests
- `compute/tests/test_w3_multivariable_shadow.py` — 50 tests
- `compute/tests/test_w4_multivariable_shadow.py` — 34 tests
- `compute/tests/test_kac_chevalley.py` — 14 tests
- `compute/lib/shadow_potential_singularity.py` — singularity theory module
- `compute/tests/test_shadow_potential_singularity.py` — 30 tests
- `compute/lib/mc_moduli_curve.py` — MC moduli curve computation

### Shadow Potential Singularity Theory (2026-03-20)

**MC potential identification** (thm:nms-shadow-mc-potential): S_A = W(x·η) where W is the cyclic L∞ MC potential. Sh_r = ⟨η, ℓ_{r-1}^tr(η,...,η)⟩_cyc. Coincides with complementarity action (def:complementarity-action) on primary line.

**Convergence** (prop:nms-shadow-convergence): S_Vir(x) is ENTIRE for c ∉ {0, -22/5}. A_r ~ 2.4·r^{-2/3}. Order ρ = 0.

**Discriminant instability** (rem:nms-discriminant-instability): Numerator changes at every truncation N. Roots cluster toward Kac zeros. Denominators stable (Kac-shadow principle). WDVV fails (not Frobenius).

**MC moduli curve** (sec:nms-mc-moduli-curve): M_A = {dS/dx = 0, x ≠ 0} is an analytic curve over C_c. Discrete fibers, branch points accumulate at Kac zeros, essential singularity at each Kac zero.

**Hadamard factorization** (thm:nms-hadamard-mc-potential): dS/dx = (κ/2)·x·∏(1-x/x_k(c)). Verified to machine precision (10^{-15}).

**MC counting** (cor:nms-mc-solution-counting): N(R;c) sub-polynomial (order 0 entire function).

**Isomonodromy**: Trivially isomonodromic at rank 1 (scalar residues commute). W_3 rank-2 branch point is at c = 0 (Kac zero). conj:nms-rank2-isomonodromic remains open.

**Total**: 172+ tests, 10+ compute modules, ~500 lines new tex in nonlinear_modular_shadows.tex.
