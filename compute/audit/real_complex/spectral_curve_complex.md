# The Shadow Spectral Curve as a Complex-Geometric Object

## Deep Investigation Report

**Date**: 2026-04-01
**Source files**: `compute/audit/real_complex/spectral_curve_investigation.py`, `spectral_curve_supplementary.py`, `verify_eo_discrepancy.py`
**Manuscript references**: `def:shadow-metric`, `thm:riccati-algebraicity`, `thm:shadow-connection`, `cor:spectral-curve`, `rem:gauss-manin-shadow`, `rem:hitchin-interpretation`, `cor:topological-recursion-mc-shadow`

---

## 0. Setup

The shadow metric on a primary line L of the Virasoro algebra is:
```
Q_L(t; c) = c^2 + 12ct + alpha(c) t^2
```
where `alpha(c) = (180c + 872)/(5c + 22) = 4(45c + 218)/(5c + 22)`.

The Gaussian decomposition: `Q_L = (c + 6t)^2 + [80/(5c+22)] t^2`.

The spectral curve of a single fiber: `Sigma_c := {(t, H) : H^2 = t^4 Q_L(t; c)}`, equivalently `y^2 = Q_L(t; c)` where `y = H/t^2`. Each Sigma_c has arithmetic genus 0.

The family: `S = {(c, t, y) : y^2 = Q_L(t; c)} subset C^3`, fibered over the c-line. After clearing the pole at `c = -22/5`:
```
(5c + 22) y^2 = P(c, t)
```
where `P(c, t) = 5c^3 + (60t + 22)c^2 + (180t^2 + 264t)c + 872t^2` is a polynomial of degree 3 in c and degree 2 in t. The surface S is rational (each fiber is genus 0).

---

## 1. Periods of the c-Family

**The period integral.** For fixed c, the branch points of `y^2 = Q_L(t)` are the zeros of Q_L in t. Since Q_L is quadratic in t with leading coefficient `alpha(c)`, the standard period integral around the branch cut gives:

```
omega(c) = oint dt/sqrt(Q_L) = 2 * int_{t_-}^{t_+} dt/sqrt(Q_L(t))
         = 2*pi / sqrt(alpha(c))
         = pi * sqrt((5c + 22)/(45c + 218))
```

This uses `int_0^1 du/sqrt(u(1-u)) = B(1/2, 1/2) = pi`.

**Key properties:**
- The period is ALGEBRAIC (degree 2) in c, living under a single square root.
- Branch points of the period as a function of c:
  - `c = -22/5` (Lee-Yang): `omega = 0` (the factor `5c+22` vanishes).
  - `c = -218/45`: `omega = infinity` (the factor `45c+218` vanishes).
- At `c = 13` (self-dual point): `omega(13)^2/omega(26-13)^2 = 1` (verified computationally).
- The Koszul dual singularities are:
  - `-22/5 <-> 152/5` (sum = 26)
  - `-218/45 <-> 1388/45` (sum = 26)

**The new singular value `c = -218/45`.** This value does NOT appear in the shadow connection or discriminant formulas. It emerges only in the c-family structure. At this value:
- `alpha(-218/45) = 0`: the t^2 coefficient of Q_L vanishes.
- Q_L degenerates from quadratic to LINEAR in t: `Q_L = c^2 + 12ct`.
- One branch point escapes to infinity.
- `Delta = -18 < 0`: the shadow metric has REAL zeros (phase transition).
- `kappa = -109/45`, `S_4 = 405/436`.
- The spectral curve degenerates to a fold `y^2 = 12c(t + c/12)`.

**Physical meaning:** `c = -218/45` is a phase boundary where the shadow metric loses its quadratic structure. Below this value, the shadow obstruction tower has qualitatively different analytic behavior (real branch points instead of complex conjugate). The Koszul dual `c = 1388/45 ~ 30.84` is the corresponding phase boundary for the dual algebra.

---

## 2. Picard-Fuchs Equation

### 2a. In the t-direction (fixed c)

The shadow connection `nabla^sh = d - Q'/(2Q) dt` has flat sections `f = sqrt(Q_L)`. These satisfy the Picard-Fuchs equation:

```
2 Q_L f'' + Q_L' f' - Q_L'' f = 0
```

This is verified by direct substitution (confirmed computationally). It is a second-order Fuchsian ODE on the t-line with regular singular points at the zeros of Q_L and at `t = infinity`.

The connection form `omega = Q_L'/(2Q_L)` has:
- Residue `1/2` at each simple zero of Q_L (universal, algebra-independent).
- Monodromy `-1` (= `exp(2*pi*i * 1/2)`) around each zero.

### 2b. In the c-direction (fixed t)

The period `f(c) = sqrt((5c+22)/(45c+218))` satisfies the first-order ODE for f':

```
(5c+22)(45c+218) f'' + 10(45c+203) f' = 0
```

This is a Fuchsian equation with regular singular points at:
- `c = -22/5` (Lee-Yang): local exponent 1/2 (square root zero).
- `c = -218/45`: local exponent -1/2 (square root pole).

The equation is first-order for f' because `f = sqrt(g)` is uniquely determined (up to sign) by the rational function `g(c) = (5c+22)/(45c+218)`.

**Note on 45c+203:** The coefficient `45c + 203` factors into `45(c + 203/45)`. The value `c = -203/45 ~ -4.511` lies between `-22/5 = -4.400` and `-218/45 = -4.844`. This is the zero of the derivative `g''/g'`, i.e., the inflection point of the period function.

---

## 3. Hodge Bundle and Gauss-Manin Connection

### The classical Hodge bundle is trivial

The family `{Sigma_c}_c` is a family of genus-0 curves over the c-line. The classical Hodge bundle `H^0(Sigma_c, omega_{Sigma_c})` is zero-dimensional (since `h^{0,1} = g = 0` for genus 0). There is no non-trivial Hodge variation in the classical sense.

### The shadow connection IS Gauss-Manin, but for the sqrt local system

The shadow connection `nabla^sh = d - Q'/(2Q) dt` is the Gauss-Manin connection of the DOUBLE COVER `y^2 = Q_L(t)` viewed as a family of sets `{+sqrt(Q_L(t)), -sqrt(Q_L(t))}` parametrized by t. More precisely:

- The multi-valued function `sqrt(Q_L(t))` defines a rank-1 local system on `L \ {Q_L = 0}`.
- `nabla^sh` is the unique flat connection for which `sqrt(Q_L(t)/Q_L(0))` is a horizontal section.
- The connection form `omega = d(log sqrt(Q_L))` is exact, confirming flatness.

This is correctly stated in `rem:gauss-manin-shadow`.

### The two-parameter Gauss-Manin

On the full (c, t)-base, the connection:
```
nabla = d - (1/2) d(log Q_L) = d - omega_t dt - omega_c dc
```
where `omega_t = (partial_t Q_L)/(2Q_L)` and `omega_c = (partial_c Q_L)/(2Q_L)`, is:
- FLAT (since `omega = d(log sqrt(Q_L))` is exact).
- Has monodromy `-1` around each irreducible component of the discriminant locus `D = {Q_L = 0}` in the (c,t)-plane.

The shadow connection is the RESTRICTION of this 2D connection to the t-direction. The c-period `omega(c)` is a horizontal section of the c-direction restriction.

### The Picard-Fuchs IS the shadow connection

The Picard-Fuchs equation `2Q f'' + Q' f' - Q'' f = 0` in the t-direction IS the equation defining flat sections of `nabla^sh`. These are the same object, confirming the manuscript's identification.

However, the shadow connection `nabla^sh` (in the t-direction, for the shadow obstruction tower) must NOT be confused with the modular connection `nabla^mod` on `M-bar_g`. These are different connections on different base spaces:

| Property | `nabla^sh` (shadow) | `nabla^mod` (modular) |
|---|---|---|
| Base | Shadow line L (1D, parameter t) | M-bar_g (moduli of curves) |
| Curvature | 0 (flat) | kappa * omega_g (Hodge class) |
| Monodromy | Z/2 (Koszul sign) | Sp(2g, Z) |
| PF equation | 2Q f'' + Q' f' - Q'' f = 0 | Tautological relations |

The MC equation INTERTWINES them: it projects the tautological relations on M-bar_g to the PF equation on L.

---

## 4. Special Fibers

### c = 0 (ramified, cusp)
- `Q_L(t; 0) = (436/11) t^2 = (872/22) t^2`.
- Double zero at `t = 0`: the spectral curve acquires a CUSP.
- `kappa = 0`: the algebra is uncurved.
- The shadow obstruction tower is trivially zero (kappa = 0 implies F_g = 0 for the scalar sector; but higher-arity contributions survive per AP31).

### c = -22/5 (Lee-Yang pole)
- `alpha(c) -> infinity`: the t^2 coefficient of Q_L diverges.
- Q_L has a pole in c. The spectral curve degenerates.
- `5c + 22 = 0`: this is the denominator of all W-algebra OPE structures.
- The period `omega(-22/5) = 0`.

### c = -218/45 (period pole, NEW)
- `alpha(c) = 0`: the t^2 coefficient vanishes. Q_L becomes linear in t.
- One branch point escapes to infinity.
- `Delta = -18 < 0`: real (not complex conjugate) zeros.
- The period `omega -> infinity`.
- Koszul dual: `c = 1388/45 ~ 30.84`.

### c = 13 (self-dual)
- `Q_L(t; 13) = 169 + 156t + (3212/87)t^2`.
- Koszul involution fixed point: `Vir_13^! = Vir_{26-13} = Vir_13`.
- Period ratio `omega(13)/omega(13) = 1` (self-dual).
- `alpha(13) = 3212/87 ~ 36.92`, `Delta(13) = 40/87 ~ 0.46`.
- The spectral curve is NOT symmetric under `t -> -t` (the linear term breaks symmetry), but IS invariant under the Koszul involution `c -> 26-c`.

### c = 26 (critical string)
- `kappa = 13`, `alpha(26) = 694/19 ~ 36.53`, `Delta(26) = 5/19 ~ 0.26`.
- Koszul dual: `c' = 0` (the degenerate cusp fiber).
- Koszul duality pairs the critical string (smooth, large kappa) with the degenerate fiber (cusp, kappa = 0).
- Shadow growth rate `rho(26) ~ 0.232` (convergent tower).
- `kappa_eff = kappa(matter) + kappa(ghost) = 13 + (-13) = 0` at critical dimension, but this is the EFFECTIVE curvature (AP29), not `kappa(Vir_{26}) = 13`.

### Discriminant curve D in the (c,t)-plane
The discriminant locus `D = {Q_L(t;c) = 0}` is a degree-(3,2) curve:
```
P(c,t) = 5c^3 + (60t+22)c^2 + (180t^2+264t)c + 872t^2 = 0.
```
- Passes through `(0, 0)` with multiplicity 2.
- Tangent cone at `(0,0)`: `872v^2 + 264uv + 22u^2 = 0`, discriminant = -1760 < 0.
- This is a NODE over C (two complex conjugate tangent directions) but an isolated point over R.

---

## 5. EO Recursion vs Shadow Tower

### The critical discrepancy (two levels)

**Level 1: EO F_1 vs shadow F_1.** The Eynard-Orantin genus-1 free energy on the spectral curve `y^2 = Q_L(t)` is `F_1^EO = -(1/24) log(320c^2/(5c+22))` (from the Bergman tau function), which has LOGARITHMIC dependence on c. The shadow F_1 = kappa/24 = c/48 is LINEAR in c. These are fundamentally different functions.

**Level 2: F_g^Airy != lambda_g^FP for g >= 2.** The EO recursion on the AIRY CURVE `y^2 = x` produces the orbifold Euler characteristics `F_g^Airy = B_{2g}/(4g(g-1))`. The shadow obstruction tower's `lambda_g^FP` are the A-hat coefficients:
```
lambda_g^FP = (1 - 2^{2g-1}) * B_{2g} * (-1)^g / (2^{2g-1} * (2g)!)
```
These are DIFFERENT numbers for g >= 2 (verified computationally in `verify_eo_discrepancy.py`):

| g | lambda_g^FP (A-hat) | F_g^Airy (chi(M_g)) |
|---|---|---|
| 1 | 1/24 | 1/24 |
| 2 | 7/5760 = 1.22e-3 | -1/240 = -4.17e-3 |
| 3 | 31/967680 = 3.20e-5 | 1/1008 = 9.92e-4 |
| 4 | 127/154828800 = 8.20e-7 | -1/1440 = -6.94e-4 |

Agreement at g = 1 is coincidental (both formulas give 1/24). At g >= 2, the A-hat coefficients are much smaller and always positive, while chi(M_g) alternates in sign and does not decay.

### Consequences

The shadow obstruction tower is NOT the EO recursion on any spectral curve, not even the Airy curve. The MC recursion (which uses the full modular operad structure) produces a fundamentally different sequence of invariants than EO.

The existing code in `topological_recursion_engine.py` has a function `airy_free_energy` that correctly computes `B_{2g}/(4g(g-1))` (the EO/Airy value), but this is NOT `lambda_g^FP`. The main engine's `lambda_fp` function in `higher_genus_graph_sum_engine.py` uses the correct formula `(2^{2g-1}-1) |B_{2g}| / (2^{2g-1} (2g)!)`.

### The genus-0 agreement

The tree-level (genus-0) data DOES match. The shadow coefficients S_n are exactly the Taylor coefficients of `sqrt(Q_L(t))`:
```
sqrt(Q_L(t)) = sum_{n>=0} a_n t^n,    a_n = (n+2) S_{n+2}
```
- `a_0 = 2*kappa = c` (verified)
- `a_1 = 3*S_3 = 6` (verified)
- `a_2 = 4*S_4 = 40/(c(5c+22))` (verified)
- All higher a_n match the MC recursion (verified to arity 11).

The tree-level EO data IS the shadow obstruction tower at genus 0. The spectral curve `y^2 = Q_L` is the correct encoding of the genus-0 shadow data.

### The correct relationship (cor:topological-recursion-mc-shadow)

The manuscript's statement is:

> The proved Koszul case of the EO recursion is the SCALAR SHADOW of the MC recursion.

This means: the MC recursion operates on the full modular cyclic deformation complex `Def_cyc^mod(A)`. The EO recursion is a PROJECTION of the MC recursion to a specific sector. The EO kernel is the scalar projection of the MC propagator `P_A`. The EO spectral curve encodes the genus-0 shadow CohFT data.

But the EO free energies `F_g^EO` (symplectic invariants of the spectral curve) are NOT the same as the shadow obstruction tower free energies `F_g = kappa * lambda_g^FP`. The MC recursion produces the A-hat genus; the EO recursion produces the orbifold Euler characteristic. These coincide at g = 1 but diverge at g >= 2.

The relationship between the two recursions at higher genus remains an open question (connected to `conj:EO-recursion` in the manuscript). The current proof of `cor:topological-recursion-mc-shadow` captures only the genus-0 content.

---

## 6. Summary of Singularity Structure

The c-family of spectral curves has the following singular c-values, organized by Koszul duality:

| c-value | Koszul dual | Type | Period | Q_L behavior |
|---|---|---|---|---|
| -218/45 | 1388/45 | Period pole | infinity | alpha = 0, linear in t |
| -22/5 | 152/5 | Lee-Yang | 0 | Pole (alpha -> infinity) |
| 0 | 26 | Cusp | finite | Q_L = alpha(0) t^2 |
| 13 | 13 | Self-dual | finite | Palindromic Q_L |
| 26 | 0 | Smooth | finite | Smooth, kappa_eff = 0 |
| 152/5 | -22/5 | Dual Lee-Yang | finite | Smooth |
| 1388/45 | -218/45 | Dual period pole | finite | Smooth |

The four pairs under Koszul duality `c <-> 26-c`:
1. `{-218/45, 1388/45}`: period singularity / smooth
2. `{-22/5, 152/5}`: Lee-Yang / dual Lee-Yang
3. `{0, 26}`: cusp / critical string
4. `{13, 13}`: self-dual fixed point

---

## 7. Open Questions

**Q1. A-hat vs chi(M_g) gap.** The shadow obstruction tower produces F_g = kappa * lambda_g^FP where lambda_g^FP are A-hat coefficients. The EO recursion on the Airy curve produces chi(M_g) = B_{2g}/(4g(g-1)). These agree at g = 1 and diverge dramatically at g >= 2. What is the precise relationship between the MC recursion (which produces A-hat) and the EO recursion (which produces chi)? Is there a MODIFIED topological recursion that produces A-hat coefficients?

**Q2. The 45c+218 singularity.** The period `omega(c) = pi * sqrt((5c+22)/(45c+218))` has a new singularity at `c = -218/45` that does not appear in the shadow connection or discriminant formulas. At this value, `alpha(c) = 0`, `Delta = -18 < 0`, and one branch point of Q_L escapes to infinity. Does this value have physical or representation-theoretic significance for the Virasoro algebra? (It lies at `kappa = -109/45`, which is not a known special level.)

**Q3. Picard-Lefschetz at the degeneration.** As c passes through `c = -218/45`, the spectral curve degenerates (Q_L becomes linear in t). The two complex conjugate branch points merge into a single real branch point plus a point at infinity. Is there a Picard-Lefschetz monodromy computation that captures this transition?

**Q4. Multi-family spectral surface.** The surface `S = {y^2 = Q_L(t;c)}` is rational. Can it be embedded in a LARGER family (e.g., parametrized by `(g, k)` for a general Lie algebra g at level k) where the total space has non-trivial Hodge structure? The affine KM fiber `Q_L = (2kappa + 3*alpha*t)^2` (perfect square, class L) would be a degenerate locus of such a family.

**Q5. EO as arity decomposition.** The EO recursion on `y^2 = Q_L(t)` produces symplectic invariants F_g^EO that involve all arities. Can these be decomposed into an arity-graded sum where different pieces are controlled by different shadow data? The arity-2 piece should be related to kappa, the arity-3 piece to alpha, etc.

**Q6. Quantization of the spectral curve.** In the theory of quantum curves (Gukov-Sulkowski), the spectral curve `y^2 = Q_L(t)` should be quantized to a differential operator `(hbar d/dt)^2 - Q_L(t) = 0`. Is the quantized operator related to the Picard-Fuchs equation `2Q f'' + Q' f' - Q'' f = 0`? The latter has the SAME singular points but different structure (first-order for f', versus second-order for f).
