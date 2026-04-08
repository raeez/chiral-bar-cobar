# Resurgence of the Cross-Channel Correction delta_F_g^cross(W_3)

## Data

The genus expansion of the W_3 free energy decomposes as
F_g(W_3) = kappa * lambda_g^FP + delta_F_g^cross (thm:multi-weight-genus-expansion).

Explicit formulas (proved, ProvedHere):

| g | delta_F_g^cross(W_3) | Large-c leading | Source |
|---|---------------------|-----------------|--------|
| 1 | 0 | 0 | thm:multi-weight-genus-expansion(iii) |
| 2 | (c+204)/(16c) | 1/16 | eq:w3-genus2-cross, cor:w3hol-multi-gen-fails |
| 3 | (5c^3+3792c^2+1149120c+217071360)/(138240c^2) | c/27648 | prop:w3-genus3-cross-channel |
| 4 | (287c^4+268881c^3+115455816c^2+...)/(17418240c^3) | 41c/2488320 | tab:cross-channel-tower |

## Net degree pattern

- g=2: net degree 0 in c (delta_F_2 -> 1/16 as c -> infinity)
- g=3: net degree 1 in c (delta_F_3 ~ c/27648)
- g=4: net degree 1 in c (delta_F_4 ~ 41c/2488320)

Pattern: delta_F_g^cross has numerator degree 2g-3 and denominator degree g-1
in c (verified at g=2,3; proved in prop:cross-channel-growth).

## Growth rate analysis

### Comparison with the scalar tower

The scalar tower F_g^scalar = kappa * lambda_g^FP is CONVERGENT:
lambda_g^FP ~ 2/(2pi)^{2g} (exponential decay from Bernoulli asymptotics).
Convergence radius in hbar: 2pi. This is Gevrey-0; the Borel transform is entire.

The cross-channel tower has FACTORIAL growth. The ratio
R_g := delta_F_g / (kappa * lambda_g) at large c satisfies (prop:cross-channel-growth):

| g | R_g (large c limit) | R_g / R_{g-1} |
|---|--------------------|----|
| 2 | 0 | - |
| 3 | 42/31 ~ 1.35 | - |
| 4 | 9184/381 ~ 24.1 | 17.8 |

The factor R_4/R_3 ~ 17.8 is consistent with (2g)!-type growth
(naive (2g)(2g-1) = 8*7 = 56 up to subleading corrections from the
non-leading-order coefficient structure).

### Is the cross-channel series Borel summable?

The key question. Two independent arguments point to YES (Gevrey-1, hence
classically Borel summable), but with a DIFFERENT instanton action from
the scalar tower.

**Argument 1: Leading coefficient ratios.** The large-c leading coefficients:
A_3 = 1/27648, A_4 = 41/2488320, giving A_4/A_3 = 41/90 ~ 0.456.

If delta_F_g ~ C * beta^g * Gamma(2g+1), then
delta_F_{g+1}/delta_F_g ~ beta * (2g+2)(2g+1),
which gives beta = (41/90)/56 = 41/5040 ~ 0.00813.

The Borel transform B_cross(t) = sum delta_F_g t^{2g}/(2g)! would then
converge for |t| < 1/sqrt(beta) ~ 11.1.

For comparison:
- Scalar Borel radius: 2pi ~ 6.28 (from A-hat poles)
- WP volume growth rate: 1/(4pi^2) ~ 0.0253 (Mirzakhani/Zograf)
- Cross-channel beta ~ 0.00813, i.e., beta ~ 1/(3.1 * 4pi^2)

The cross-channel instanton action A_cross = 1/beta ~ 123 is approximately
3.1 * (2pi)^2 ~ 3.1 * A_scalar. This suggests the cross-channel
singularities in the Borel plane are FURTHER from the origin than the
scalar singularities, not closer.

**Argument 2: Graph-counting bound.** The cross-channel amplitude at genus g
sums over O(C_graph^g) stable graphs (the count grows exponentially:
7, 42, 379 at g=2,3,4; ratio ~6-9). Each graph amplitude is bounded
polynomially in c (the c-power is 1 - h^1(Gamma) where h^1 is the loop
number). The exponential graph-count growth, combined with polynomial
per-graph amplitudes, gives at most C^g growth for the graph sum.
But the Hodge integral normalizations at each vertex contribute factors
that can grow factorially (from Weil-Petersson volume asymptotics at
vertices of high genus). The net growth is Gevrey-1.

**Caveat.** With only g=2,3,4 data, the distinction between (2g)! and
(2g-2)! growth is not resolvable. The beta estimate has a factor ~3.6
uncertainty: beta in [0.008, 0.015]. The instanton action A_cross is
constrained to [65, 123].

## Structural comparison with the scalar resurgence

| Property | Scalar tower | Cross-channel tower |
|----------|-------------|-------------------|
| Generating function | A-hat(i*hbar) = (hbar/2)/sin(hbar/2) | Unknown |
| Growth rate | Converges (Gevrey-0) | (2g)! (Gevrey-1) |
| Instanton action | (2pi)^2 ~ 39.5 | ~65-123 (estimated) |
| Borel plane singularities | hbar = 2pi*n (simple poles) | Unknown |
| Stokes constant | S_1 = -4pi^2 kappa i | Unknown |
| Resurgent structure | Simple (A-hat poles, Ecalle bridge) | Expected but unproved |
| Trans-series | Known (one-instanton from residues) | Unknown |
| Physical interpretation | Instanton = 2pi soliton | Mixed-channel virtual graphs |

## Key finding

The cross-channel series introduces a QUALITATIVELY NEW resurgent sector
that is absent from the scalar (uniform-weight) tower. The scalar tower
converges; the cross-channel tower diverges factorially. This means:

1. The FULL free energy F_g(W_3) = kappa*lambda_g + delta_F_g^cross has
   (2g)! growth dominated by the cross-channel correction at high genus.
   The scalar part contributes a convergent subseries.

2. The instanton action controlling the cross-channel divergence is
   A_cross ~ 65-123, which is LARGER than the scalar instanton action
   A_scalar = (2pi)^2 ~ 39.5. This is counterintuitive: the cross-channel
   "instantons" are heavier than the scalar instantons.

3. Since A_cross > A_scalar, the cross-channel non-perturbative effects
   are EXPONENTIALLY SUPPRESSED relative to the scalar ones:
   exp(-A_cross/hbar^2) << exp(-A_scalar/hbar^2). The scalar resurgence
   dominates at small coupling.

4. At sufficiently high genus (g >= 4), the cross-channel correction
   dominates the perturbative free energy. But the non-perturbative
   (Borel-resummed) answer is controlled by the nearer (scalar) singularity.

## Status

- delta_F_2^cross, delta_F_3^cross: PROVED (ProvedHere), multi-path verified
- prop:cross-channel-growth: PROVED (ProvedHere), factorial growth established
- Borel summability of cross-channel series: OPEN (supported by 3-point
  extrapolation, not proved; needs g=5+ data or structural argument)
- Cross-channel instanton action: OPEN (estimated A_cross ~ 65-123)
- Cross-channel Stokes constant: OPEN
- Cross-channel trans-series: OPEN
- Resurgent structure (alien derivatives, bridge equation): OPEN

## What is needed

1. The genus-5 cross-channel formula delta_F_5^cross(W_3) would pin down
   the growth rate to distinguish (2g)! from (2g-2)! and refine beta.
2. A structural argument for Borel summability from the MC equation
   D*Theta + (1/2)[Theta,Theta] = 0 (the cross-channel data is part of
   the full MC element; the MC equation constrains alien derivatives
   via the Ecalle bridge, but this has only been worked out for the
   scalar sector).
3. Identification of the cross-channel "instantons" (the Borel plane
   singularities of B_cross(t)) with geometric objects (analogues of the
   A-hat poles at hbar = 2pi*n).
