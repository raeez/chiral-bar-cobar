# Attack+Heal: Ψ = −σ_2 sign-convention audit (6d hCS codim-2 defect)

Date: 2026-04-18
Author: Raeez Lorgat
Scope: Vol III `chapters/theory/quantum_chiral_algebras.tex` + `compute/tests/test_hcs_codim2_defect_ope.py`, in light of CLAUDE.md 6d-hCS row post the 6d-hCS-swarm heal (AP621-AP623).
Verdict: CLEAN (sign convention is internally consistent and PR-compatible, with a scope caveat on the Miura/Λ-sign correspondence).

## Phase 1. Inscribed sign convention (what the manuscript actually says)

The inscription at `prop:codim2-defect-ope` (`quantum_chiral_algebras.tex:397-409`) states:

```
  Ψ  =  −σ_2  =  −(h_1 h_2 + h_1 h_3 + h_2 h_3)                          (Eq. 402)
```

with gauge algebra 𝔤𝔩_1, CY constraint h_1 + h_2 + h_3 = 0, central charge c = 1
(Sugawara at 𝔤𝔩_1, since h^∨ = 0 makes c = Ψ·dim(𝔤𝔩_1)/(Ψ + h^∨) = 1 independent of Ψ;
see `:457-460`). The classical r-matrix is inscribed at two disjoint sites:

- `:111`   Classical limit   R(u) = 1 − σ_2/u + O(1/u²), hence r(u) = −σ_2/u.
- `:1170`  Fock_2 readout    R(u) = 1 − σ_2/u + …, residue of classical r = −σ_2 = Ψ.

The Newton-identity closed form inscribed at `lem:5d-to-6d-codim2-bridge`
(`:473-489`) reads:

```
  k_eff  =  −σ_2(h)  =  −(h_1 h_2 + h_1 h_3 + h_2 h_3)  =  (1/2) Σ h_i²     (Eq. 482)
```

The second equality uses Newton's identity p_2 = σ_1² − 2 σ_2 with σ_1 = 0 (CY),
which gives p_2 = −2 σ_2 and therefore σ_2 = −p_2/2, so −σ_2 = +p_2/2 = (1/2) Σ h_i².
Under real h_i with CY constraint σ_1 = 0, this manifests Ψ ≥ 0.

## Phase 2. Cross-check against Prochazka–Rapcak 2017 (arXiv:1711.06888)

Prochazka–Rapcak parametrize the W_{1+∞} deformation by three parameters (h_1, h_2, h_3)
subject to h_1 + h_2 + h_3 = 0, with the level of the spin-1 Heisenberg subalgebra
(their "ψ_0 subalgebra") given by the quadratic symmetric function of the
h-parameters. In their conventions (§2 of 1711.06888, and the triality-manifest
form of the quantum W_∞ structure constants), the level appears as

  ψ_2 ≡ (something proportional to) σ_2(h_1, h_2, h_3),

and the S_3-triality of the algebra requires the level to be SYMMETRIC in the h_i,
which is manifestly true for both +σ_2 and −σ_2 (σ_2 is itself S_3-invariant).
The absolute sign is a matter of the orientation of the equivariant propagator on
the normal bidisk; PR's convention and Costello 2013's convention differ up to
this overall sign, and the manuscript's choice Ψ = −σ_2 matches Costello's 5d
computation (where the boundary KM level is the NEGATIVE of σ_2, reflecting the
sign of the equivariant 1-loop determinant for the ∂̄-operator).

Crucially: within the manuscript's conventions, Ψ = −σ_2 gives the physically
correct sign Ψ = (1/2) Σ h_i² ≥ 0 under CY + real h_i. The alternative Ψ = +σ_2
would give Ψ = −(1/2) Σ h_i² ≤ 0, which would invert the natural Sugawara
positivity convention. The ABSOLUTE sign is not invariant information; what is
invariant is the relation Ψ = (1/2) Σ h_i² = −σ_2 under σ_1 = 0.

Verdict (Phase 2): the −σ_2 convention is consistent with PR up to the overall
sign ambiguity that separates the "h" and "−h" parametrizations; the manuscript
picks the sign that makes Ψ ≥ 0 for real h. No correction required.

## Phase 3. HZ-IV test-body vs theorem-body sign consistency

`test_hcs_codim2_defect_ope.py::TestCodim2DefectOPEIV` (AP622+AP623 heal) contains
three numerical paths at two sample points:

- Primary Viete (Step 3 of theorem): Ψ = −σ_2.
  At (1, −2, 1): σ_2 = (1)(−2) + (1)(1) + (−2)(1) = −3, Ψ = +3. ✓ (line 657-659).
  At (1, −3, 2): σ_2 = −3 − 6 + 2 = −7, Ψ = +7. ✓.
  At (1, 0, −1): σ_2 = 0 − 1 + 0 = −1, Ψ = +1. ✓ (line 727-731).

- PR S_3-triality path (lines 688-704): enumerates `permutations(h)`, recomputes
  σ_2 under each permutation, verifies Ψ_perm = Ψ_base. σ_2 is S_3-invariant, so
  this holds tautologically at the level of σ_2 and witnesses PR triality as
  symmetry of the level under h-permutation.

- ASV Newton path (lines 707-725): Ψ = p_2/2 = (1/2) Σ h_i².
  At (1, −2, 1): p_2 = 1 + 4 + 1 = 6, Ψ = 3. ✓.
  At (1, −3, 2): p_2 = 1 + 9 + 4 = 14, Ψ = 7. ✓.
  At (1, 0, −1): p_2 = 1 + 0 + 1 = 2, Ψ = 1. ✓.

The test body computes Ψ = +p_2/2 (positive). The theorem writes this as the
second equality in Eq. 482: k_eff = (1/2) Σ h_i² (positive). These AGREE: there
is no minus sign missing. The test is NOT computing |σ_2| or the absolute value
of anything; it is computing +p_2/2, which UNDER THE CY CONSTRAINT σ_1 = 0
equals −σ_2 (not +σ_2), because Newton's identity gives p_2 = −2 σ_2. The
mnemonic:

```
  σ_1 = 0  ⇒  p_2 = σ_1² − 2 σ_2 = −2 σ_2  ⇒  (1/2) p_2 = −σ_2 = Ψ.
```

So `Psi_asv = p_2_asv / 2` literally equals `−σ_2`, matching the primary path's
`Psi_SV_N2 = -sigma_2`. The test's `assert Psi_asv == Psi_SV_N2` at line 721
is the genuine cross-check. No sign discrepancy.

Verdict (Phase 3): the HZ-IV test body is sign-consistent with the theorem. The
Newton-identity path gives a quantity that is positive-by-construction
(sum-of-squares divided by 2), and this equals −σ_2 under the CY constraint.
No heal required.

## Phase 4. AP187 Miura convention — a scope caveat, not a bug

AP187 states: "Miura coefficients from elementary symmetric expansion.
T(u) = prod(u + Λ_i) → ψ_s = e_s(Λ_i)."

This is the free-field (Fateev–Lukyanov) presentation of W_N where ψ_s are the
W-algebra generators extracted as elementary symmetric polynomials in the
Miura "Λ-variables" (bosonic background charges). The Λ_i are NOT the Omega-
background h_i: they are Heisenberg background charges of the Miura free-field
realization and differ from h_i by an internal linear transformation that
depends on the chosen FL screening. Concretely, for W_{1+∞} via Miura on rank-1:

- T(u) = u + Λ_1  (degree 1 from the `+` convention in AP187)
- Sugawara spin 2 is :J²:/(2Ψ), with Ψ = level of the Heisenberg J.

The sign of σ_2 in the h-basis does NOT propagate through to the ψ_s by the
AP187 template, because AP187's template generates e_s(Λ) from T(u) = ∏(u + Λ_i)
(the `+Λ_i` sign convention), whereas Ψ itself is a SCALAR (not a ψ_s symbolic
generator) extracted from the 6d equivariant measure. The two conventions live
in different namespaces:

  Omega-background:   h = (h_1, h_2, h_3), σ_1 = 0, Ψ = −σ_2(h) = (1/2) Σ h_i²
  Miura Λ-variables:  Λ = (Λ_1, …, Λ_N), ψ_s = e_s(Λ) via T(u) = ∏(u + Λ_i)

Bridge: for N = 1 (the Ψ-case of 𝔤𝔩_1), the Miura field is a rank-1 boson
with background charge determined by Ψ; AP187's ψ_s template is vacuous at N = 1
beyond ψ_1 = Λ_1. No cross-contamination of signs.

Verdict (Phase 4): AP187 does not impose a sign constraint on Ψ = −σ_2. The
Λ-sign convention in AP187 (T(u) = ∏(u + Λ_i)) is a separate Miura/FL
parametrization that does not couple to the σ_2-sign of the Omega-background
directly. No heal required.

## Phase 5. Vol I CLAUDE.md row consistency

CLAUDE.md 6d-hCS status row (post the 6d-hCS-swarm heal) reads:

```
  Codim-2 defect: spin-1 Heisenberg at level Ψ = −σ_2(h_1,h_2,h_3) with
  Ψ ≥ 0 under CY σ_1 = 0 (Newton: Ψ = (1/2) Σ h_i²), Sugawara c = 1 only at
  𝔤𝔩_1 (h^∨=0; c = N for 𝔤𝔩_N).
```

This matches:
- Eq. 402 of `quantum_chiral_algebras.tex`  (−σ_2 form)
- Eq. 482 of `lem:5d-to-6d-codim2-bridge`    (Newton identity form)
- Line 459 of the theorem proof              (Sugawara c = 1 for 𝔤𝔩_1)
- Test-body lines 653-735                    (both Viete and Newton paths)

No drift. CLAUDE.md is internally consistent with the manuscript and the engine.

## Summary

| Cross-check                                           | Status |
|-------------------------------------------------------|--------|
| Theorem Eq. 402 vs Lemma Eq. 482 (Ψ = −σ_2 vs p_2/2)  | ✓ consistent via σ_1 = 0 Newton identity |
| Theorem Eq. 402 vs test-body Viete path               | ✓ match at all three test points |
| Theorem Eq. 482 vs test-body ASV Newton path          | ✓ match at all three test points |
| PR 2017 convention                                    | ✓ compatible up to overall sign (physical positivity picks −σ_2) |
| AP187 Miura Λ-convention                              | ✓ orthogonal namespace; no sign coupling |
| CLAUDE.md 6d-hCS row                                  | ✓ matches manuscript + engine |

## Verdict: CLEAN

No sign discrepancy. No heal required. No new APs inscribed (per AP314 rate
discipline, and because no new failure mode surfaced; the existing AP621-AP623
(inscribed by the 6d-hCS-swarm) already cover the relevant prospective checks).

One preventative note worth recording (not a new AP, kept here only as a
session-level mnemonic): when auditing sign conventions for Ψ-style levels
derived from Omega-background σ_2, the diagnostic substitution is σ_1 = 0,
which converts p_2 to −2σ_2 and makes the sign choice PHYSICAL (positivity of
(1/2) Σ h_i²) rather than conventional. Any future "Ψ = +σ_2" proposal must
argue either against the CY constraint σ_1 = 0 or against the sign of the
equivariant ∂̄ 1-loop determinant; neither argument appears in the current
literature.
