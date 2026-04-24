# UTI Functor Equality — Brutal Adversarial Report

1. **VERDICT: SCOPE-LIMITED.** The d=1 value check is vacuous: the source itself says the elliptic case is cancellation, `Xi(E)=1-1=0`, and “0 = 0” is not a nonzero conductor test (`cy_d_kappa_stratification.tex:530-536`). The only non-trivial d=2 datum is the K3 Hodge side, column `(1,0,1)`, giving `Xi(K3)=2` and `kappa_ch=2` (`cy_d_kappa_stratification.tex:1016-1019`). Save: cite d=2 only as the Hodge-supertrace target, not as UTI evidence without the Vol I ghost computation.

2. **VERDICT: FAIL (INCONCLUSIVE FROM SOURCES).** The memory identifies `Phi_2(K3)=E_2`-Mukai-Heisenberg (`platonic_ideal...md:150`) but only says its conductor has “an explicit lattice value” (`platonic_ideal...md:336`); it does not compute `K=-c_ghost=2`. Save: retract “value maps PROVED for d=2” (`platonic_ideal...md:305`) until `c_ghost(E_2-Mukai-Heisenberg)=-2` is written with conventions.

3. **VERDICT: FAIL.** UTI-2 needs `K(Phi_3(K3xE))=10`. Sources establish `kappa_BKM=5=c_1(0)/2` (`cy_d_kappa_stratification.tex:2030-2032`) and assert a bridge `kappa_BKM=K/2` (`platonic_ideal...md:340`), but Vol III also says Vol I’s three-faces value is `12=2*5+0+2` (`cy_d_kappa_stratification.tex:2043-2051`). Save: separate Borcherds weight, shifted three-faces index, and ghost conductor before claiming UTI-2.

4. **VERDICT: FAIL.** The additive formula is already dead: at N=1 the text gives `5` versus `0+0=0` with the elliptic fiber (`cy_d_kappa_stratification.tex:2033-2041`, `2088-2095`); with K3 as “fiber” it gives `2`, still not `5`. The “N=1 coincidence” language in memory (`platonic_ideal...md:347`) is stale. Save: retract the additive identity completely; do not rescue it by mixing K3-fiber `2` with Heisenberg-Mukai `3` (`cy_d_kappa_stratification.tex:177-183`).

5. **VERDICT: MAL-STATED.** The three-factor identity literally writes `tr_ghost(Q_BRST^2)=...=c_N(0)/2` (`CLAUDE.md:528-535`) while immediately saying `Q_BRST^2=0` (`CLAUDE.md:537-538`). Literal trace gives zero, not `5` at N=1. Save: replace it by a defined regularized BRST anomaly/index class landing in the Euler-characteristic class; never trace the square itself.

6. **VERDICT: SCOPE-LIMITED.** The eight-form spread is internally inconsistent: `CLAUDE.md:502-508` and the early Vol III summary give `{5,2,1,1,1/2,1,1/4,0}` (`cy_d_kappa_stratification.tex:160-169`), while the later corollary gives `{5,4,3,2,2,1,1,1}` (`cy_d_kappa_stratification.tex:2394-2413`). Class A theorem scope is only CHL `N={1,2,3,4,6}` (`cy_d_kappa_stratification.tex:2013-2029`); `N={5,7,8}` are excluded from smooth `K3xE` CY3 hosts (`cy_d_kappa_stratification.tex:2455-2463`). Save: choose one family and keep non-CHL continuations out of functor-level UTI.

## Retraction Candidates

- Retract “UTI-1 value maps PROVED for d=1,2” until the d=2 ghost-conductor calculation is explicit.
- Retract UTI-2 as a proved value identity until the `10` versus `12` versus `5` normalization conflict is resolved.
- Retract the additive decomposition and the literal three-factor trace identity; restate them only as scoped, regularized anomaly formulas.
