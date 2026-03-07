  Assessment: B2–B6 Upgrade Feasibility

  B2: Sharp geometric periodicity bound (conj:geometric-periodicity)

  Problem found: The weak bound Period_geom | (3g-2) (proved) and sharp bound Period_geom | 12(2g-2) (conjectured) are
  incompatible for g ≥ 3:
  - g=3: divisors of 7 = {1,7}; divisors of 48 = {1,2,3,4,6,8,...}. Period = 7 divides 7 but NOT 48.
  - g=4: divisors of 10 = {1,2,5,10}; 5 and 10 don't divide 72.

  The weak theorem proof derives Period_geom | (3g-2) from nilpotency of κ(λ)^{3g-2} = 0. But nilpotency of a
  multiplication operator constrains the nilpotency index, not the period of a dimension sequence. There's a logical gap
  between "σ_geom is nilpotent of index ≤ 3g-2" and "Period_geom | (3g-2)".

  Verdict: The weak theorem likely has a formulation issue (conflating nilpotency with periodicity). The sharp conjecture
  addresses a different quantity. Cannot upgrade; need to investigate and fix the formulation.

  B3: KS operator on H¹_red (conj:discriminant-ks-operator)

  For sl₂: done (prop:hred-sl2, extrinsic construction via Picard-Fuchs D-module).

  For general g: the conjecture predicts dim H^red_1 = rank(g)+1. The "core open problem" (stated explicitly at line 747)
  is identifying the subquotient representation-theoretically. The Schur's lemma obstruction (lines 735-748) proves H^1
  itself doesn't work. The Casimir conservation-law argument (rem:rank-plus-one) gives a heuristic but not a proof.

  Verdict: Genuinely open mathematics — the subquotient identification requires new representation-theoretic insight.
  Cannot upgrade.

  B4: sl₃ bar generating function (conj:sl3-discriminant)

  Infrastructure:
  - ŝl₃ is chiral Koszul for generic k: proved (thm:km-chiral-koszul covers ALL simple g)
  - dim H^n = dim(A!)_n: proved (cor:bar-cohomology-koszul-dual)
  - Values a(1)=8, a(2)=36, a(3)=204: proved (Master Table)

  But the compute library (koszul_hilbert.py) only computes classical Koszul dual coalgebra dims (Λ(g*) = C(d,n)), not
  chiral ones. The comments at lines 255-297 explicitly acknowledge this gap. Evidence item (iv) saying "verified by
  computer through degree 7" likely means the recurrence formula predictions are self-consistent, not independently
  computed from the bar complex.

  The key missing piece: proving the GF is rational (constant-coefficient recurrence of order rank+1 = 3). This would
  follow from a structural theorem about Casimir operators forcing holonomic recurrences on bar cohomology — articulated
  in rem:rank-plus-one but not proved.

  Verdict: The strongest candidate for partial upgrade, but proving rationality requires new mathematics beyond existing
  infrastructure. Cannot fully upgrade.

  B5: Yangian E₁ Koszulness (rem:yangian-collapse-conj)

  I investigated whether thm:pbw-koszulness-criterion could apply to the Yangian. The answer is no: the RTT relation
  [T^{(r+1)}, T^{(s)}] - [T^{(r)}, T^{(s+1)}] = T^{(r)}T^{(s)} - T^{(s)}T^{(r)} has quadratic terms on the RHS, so
  commutators are NOT in F₁. The associated graded is Sym(V)/(level-exchange relations), which is not commutative — it has
   extra quadratic constraints. The PBW criterion requires a commutative associated graded.

  The manuscript correctly identifies the gap: "extending FM compactification arguments to the E₁ setting" requires new
  operadic geometry (Stasheff associahedra replacing FM compactifications).

  Verdict: PBW criterion inapplicable. Genuinely requires new machinery. Cannot upgrade.

  B6: Anomaly at higher genus (conj:anomaly-physical)

  The scope remark (lines 835-857) is precise: genus 0 is proved for KM/W/bosonic string. The gap is the analytic
  comparison between renormalized BRST (via Costello counterterms on M̄_g) and the genus-g bar differential. The algebraic
  infrastructure is complete; the analytic matching is missing.

  Verdict: Requires Costello renormalization analysis. Cannot upgrade.
