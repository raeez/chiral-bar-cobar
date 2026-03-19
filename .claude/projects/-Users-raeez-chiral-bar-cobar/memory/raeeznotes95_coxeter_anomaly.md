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

### Open Question
Does Kac determinant at level n factor through A_{n-1} Chevalley discriminant in spectral (eigenvalue) variables?

### Files Created
- `compute/lib/coxeter_anomaly_test.py` — S_n representation analysis
- `compute/lib/coxeter_arity4_deep.py` — rewritten by user for W_3 depth analysis
- `compute/lib/w3_multivariable_shadow.py` — W_3 quartic from Λ-exchange, Kac-shadow principle, DS compatibility
- `compute/tests/test_coxeter_anomaly.py` — 44 tests, all passing
