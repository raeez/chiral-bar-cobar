# Wave 7: Verlinde recovery + DS intertwining — adversarial attack and heal

**Date**: 2026-04-17
**Targets**:
- `prop:verlinde-from-ordered` (Vol I `chapters/theory/higher_genus_modular_koszul.tex:33368-33517`)
- `rem:ds-intertwining-w3` (Vol I `chapters/theory/ordered_associative_chiral_kd.tex:12031-12057`)
- Engine: `compute/lib/ds_coproduct_intertwining_engine.py`, `compute/lib/verlinde_ordered_engine.py`
- Tests: `test_ds_coproduct_intertwining_engine.py` (53 base + 5 parametrize = 57 collected), `test_verlinde_ordered_engine.py` (27 base)

Russian-school voice: Beauville-Laszlo, Faltings, Tsuchiya-Ueno-Yamada (Verlinde); Drinfeld-Sokolov, Feigin-Frenkel, Etingof-Frenkel-Kirillov (DS reduction & intertwining).

---

## Phase 1 — adversarial findings

### (i) Verlinde recovery: manuscript and engine honest

The proposition `prop:verlinde-from-ordered` (higher_genus_modular_koszul.tex:33368) reads:

> Let `k ≥ 1` be a positive integer, and let `S_{jl} = √(2/(k+2)) sin(π(j+1)(l+1)/(k+2))` be the modular S-matrix for `ŝl_2` at level k. The ordered chiral homology at integer level recovers `Z_g(k) = Σ_j S_{0j}^{2-2g}`.

**Scope is properly integer-level-restricted.** The proof of part (iii) (the load-bearing `g ≥ 2` clause) reads:

> *The Verlinde formula [Verlinde88] gives `Z_g = Σ_j S_{0j}^{2-2g}` as the dimension of the space of conformal blocks on a genus-g curve with no insertions. From the ordered chiral homology: the symmetric coinvariants of the ordered chain complex compute the conformal blocks via the factorization property (TUY [TUY89]).*

This is **citation-level Verlinde** (Verlinde88 + TUY89), plus an internal argument that ordered chiral homology → symmetric coinvariants → conformal blocks. The ordered→symmetric step is the AP152-correct sense (labeled, non-coinvariant) and the factorization is Tsuchiya-Ueno-Yamada. The engine `verlinde_ordered_engine.py` computes via three independent paths (direct S-matrix sum, quantum-dimension formula, handle recursion) and cross-checks against the Verlinde table of `verlinde_shadow_algebra.py`.

**Small case verification**:
- SU(2), k=1, g=2: `Z_2(1) = 2 · (1/√2)^{-2} = 2 · 2 = 4`. Manuscript (line 33419) reports `Z_2(1) = 4`. ✓
- SU(2), k=2, g=2: `Z_2(2) = 10`. Manuscript (line 33420). Cross-check Faltings: `h^0(M_{SU(2)}(Σ_2), L^2) = 10` at level 2. ✓
- Genus-2 degree-decomposition `CB_{2,2}(k) = 2k(k+1)(k+2)/3` (status table). At k=1: 4 ✓; at k=2: 16 (≠ Z_2(2)=10 because CB_{2,2} is `dim H^2` in the bar-degree sense, not `dim H^0`-conformal-blocks). Different objects. This is internally consistent with the distinction `rem:verlinde-vs-shadow` makes.

**Integer-level scope**: correctly restricted in proposition hypothesis and explained in the intro paragraph (line 33341): *"the Verlinde formula, by contrast, counts conformal blocks at integer level: the dimension `Z_g(k) = Σ_j S_{0j}^{2-2g}` is a positive integer that makes sense only when `q = e^{2πi/(k+h^∨)}` is a root of unity"*. Admissible (non-integer rational) level is scoped out; Feigin-Tipunin modified Verlinde not claimed.

**HZ-IV decorator**: `test_hz_iv_decorators_wave1.py:316-342` carries `prop:verlinde-from-ordered` with `derived_from = [ordered chiral homology sum, engine]`, `verified_against = [S-matrix unitarity Z_0=1, WZW rep count Z_1=k+1, Beauville-Laszlo moduli-bundle H^0]`, `disjoint_rationale` properly articulated. Disjointness is genuine (S-matrix axioms vs. WZW representation theory vs. algebraic geometry of `M_G(Σ_g)`).

**Verdict**: Verlinde recovery survives the attack. Stays ProvedHere.

### (ii) DS intertwining — Wave-2 heal already in place in manuscript

Wave-1 finding F5 reported: engine `ds_coproduct_intertwining_engine.py` docstring lines 103-104 declare "*AT DEGREE 1, the intertwining is a TAUTOLOGY for the Cartan sector*", contradicting CLAUDE.md status table line 619 ("verified 57 tests").

Wave-2 healed the manuscript remark `rem:ds-intertwining-w3` (chapters/theory/ordered_associative_chiral_kd.tex:12031-12057):

> *At degree 1 the intertwining is tautological on the Cartan sector: both sides compute the same Drinfeld primitive formula on `Δ_z(J)` and `Δ_z(ψ_n)`, so the 57 compute tests at degree 1 verify a self-consistent specialisation rather than an independent identity. At degree ≥ 2 the intertwining is non-tautological: it is equivalent to the matching of the independent `sl_3` RTT commutators `[t_{ij}^{(1)}, t_{kl}^{(1)}] = Ψ(δ_{il} t_{kj}^{(1)} − δ_{kj} t_{il}^{(1)})` with the `W_3` OPE after `π_3`-reduction; these are cross-verified on the 81 RTT components at `gl_3`. The spin-3 sector with its gravitational `HPL_3` contributions is the genuinely chiral content and remains the sharpest non-tautological witness.*

This heal is **internally consistent with the engine docstring** (line 103) and honest about the tautological degree-1 sector. The spectral coassociativity form `(Δ_{z_1} ⊗ id) ∘ Δ_{z_1+z_2} = (id ⊗ Δ_{z_2}) ∘ Δ_{z_1}` is stated correctly in the remark (lines 12053-12056) per FM39.

### (iii) 57 tests count — numerical audit

- `compute/tests/test_ds_coproduct_intertwining_engine.py`: 53 `def test_*` declarations + 1 `@pytest.mark.parametrize("k_val", [0, 1, 2, 5, 10])` expanding one method over 5 values = **57 collected pytest items**. Consistent.
- Actual coverage:
  - Tests 1-13: `Δ_z(ψ_1)`, `Δ_z(ψ_2)` formulae in sl_3/W_{1+∞} — tautological degree-1 (Drinfeld primitive).
  - Tests 14-30: DS projection (Cartan survives, roots killed), level identification `Ψ = k+3`, counit, coassociativity.
  - Tests 31-45: ghost-number, spectral degree, central-charge consistency, z=0 specialisation.
  - Tests 46-53: critical level k=-3, Miura-inverted spin-2 coproduct.
  - Parametrized test 414-420 (5 values): intertwining at integer levels.
- **Zero tests** inspect `Δ_z` at spin ≥ 3 — the genuinely non-tautological sector is *delegated to* `w3_gravitational_coproduct.py` (which is listed in docstring "References" line 115). The spin-3 gravitational sector test coverage is a Wave-7 residual.

### (iv) Remaining propagation drifts

- **Standalone `w3_holographic_datum.tex:90-101`** carried pre-Wave-2 framing (no degree-1/degree-≥2 hedge). **Healed in this wave** (see Phase 2).
- **CLAUDE.md line 619** still reads *"DS intertwining | VERIFIED | ... verified 57 tests. Spectral coassociativity uses shifted parameters."* This is project-memory (not manuscript); manuscript is the canonical source and is now healed. Out of manuscript scope for hygiene.
- **No HZ-IV decorator** on `test_ds_coproduct_intertwining_engine.py`. Honest disjointness at degree 1 is impossible (the intertwining IS tautological by construction there); the sound move is to NOT decorate rather than decorate tautologically (HZ-IV explicit three-healings menu: downgrade rather than tautologise). At degree ≥ 2 the `sl_3` RTT cross-check is cited to `Remark~\ref{rem:gl3-explicit}`, itself an internal remark — not genuinely disjoint. A proper HZ-IV decoration awaits either (a) external Tsymbaliuk arXiv:1404.5240 / Prochazka-Rapcak arXiv:1711.11582 affine-Yangian coproduct comparison at spin ≥ 3, or (b) a spin-3 gravitational coproduct test that is disjoint from the Miura derivation. Flagged for Wave 8+.

---

## Phase 2 — surgical heal

### Edit 1 — standalone `w3_holographic_datum.tex`

Propagated the Wave-2 degree-1-tautological hedge into the standalone. Diff:

```
- $(\pi_3 \otimes \pi_3) \circ \Delta_z^{\fsl_3}
-  = \Delta_z^{W_3} \circ \pi_3$ is verified with~$57$ tests (Vol~I
- theorem status table). Spectral coassociativity uses \emph{shifted}
- parameters ...
+ $(\pi_3 \otimes \pi_3) \circ \Delta_z^{\fsl_3}
+  = \Delta_z^{W_3} \circ \pi_3$ is verified at $57$~tests
+ (Vol~I theorem status table). At degree~$1$ the intertwining is
+ \emph{tautological} on the Cartan sector: both sides reduce to the
+ same Drinfeld primitive formula ..., so the degree-$1$ tests witness
+ a self-consistent specialisation rather than an independent identity.
+ The genuinely non-tautological content lives at degree~$\geq 2$,
+ where matching the $\mathfrak{sl}_3$ RTT commutators with the $W_3$
+ OPE after $\pi_3$-reduction becomes a non-trivial identity; the
+ spin-$3$ sector with its gravitational $\mathrm{HPL}_3$ contributions
+ is the sharpest witness. Spectral coassociativity uses \emph{shifted}
+ parameters ...
```

### Edits 2+ — none

The manuscript remark `rem:ds-intertwining-w3` was already Wave-2 healed. The Verlinde proposition survives the attack unchanged. No further surgical edits warranted in this wave; the spin-3 gravitational test coverage and the HZ-IV decoration at degree ≥ 2 are genuine open residuals for Wave 8.

---

## Residual frontier for later waves

1. **Spin-3 gravitational coproduct test coverage** — `w3_gravitational_coproduct.py` placeholder-referenced but not audited in Wave 7; the genuinely non-tautological DS-intertwining content lives there.
2. **HZ-IV decorator for `rem:ds-intertwining-w3`** — requires external Tsymbaliuk / Prochazka-Rapcak affine-Yangian coproduct comparison at spin ≥ 3, or an independent-construction test. Deferred.
3. **CLAUDE.md line 619 status-table phrasing** — operational scaffolding, not manuscript. Project memory hygiene, not constitutional.

---

## Verdict

- `prop:verlinde-from-ordered`: **SURVIVES**. Honest scope (integer level), three verification paths, proper HZ-IV decoration, cited to TUY89 + Beauville-Laszlo.
- `rem:ds-intertwining-w3`: **SURVIVES WITH SCOPE QUALIFICATION** (already inscribed Wave 2). Degree-1 tautology + degree-≥2 RTT cross-check are now propagated to the standalone as well.
- Spin-3 gravitational content: **OPEN RESIDUAL** (not a gap in the current manuscript claim, but a gap in the independent-verification infrastructure).
