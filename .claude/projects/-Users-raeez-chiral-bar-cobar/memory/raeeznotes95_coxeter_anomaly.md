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
