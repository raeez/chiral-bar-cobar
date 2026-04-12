#!/usr/bin/env python3
"""
Investigate the discrepancy with the claimed Psi_E1 = 0.869 + 1.355i.

The previous agent computed a "Y_hbar(sl_2) E_1 holomorphic invariant"
at tau=i, k=2, u=1. The value 0.869 + 1.355i with |.| = 1.61 could
correspond to a different convention for:
  (a) The KZB equation normalization
  (b) The R-matrix (quantum vs classical, with spectral shift)
  (c) The overall conformal block normalization (prime form, theta, eta factors)
  (d) A different notion of "E_1 invariant" (trace vs component)

We systematically explore these possibilities.
"""

import mpmath
mpmath.mp.dps = 30

# ============================================================
# Theta functions and Weierstrass functions
# ============================================================

def theta1(z, tau, n=80):
    q = mpmath.exp(mpmath.pi * 1j * tau)
    s = mpmath.mpf(0)
    for m in range(n):
        s += (-1)**m * q**((m + mpmath.mpf(1)/2)**2) * mpmath.sin((2*m+1)*mpmath.pi*z)
    return 2*s

def theta1_dz(z, tau, n=80):
    q = mpmath.exp(mpmath.pi * 1j * tau)
    s = mpmath.mpf(0)
    for m in range(n):
        s += (-1)**m * q**((m + mpmath.mpf(1)/2)**2) * (2*m+1)*mpmath.pi * mpmath.cos((2*m+1)*mpmath.pi*z)
    return 2*s

def theta1_d3z(z, tau, n=80):
    q = mpmath.exp(mpmath.pi * 1j * tau)
    s = mpmath.mpf(0)
    for m in range(n):
        s += (-1)**m * q**((m + mpmath.mpf(1)/2)**2) * (-(2*m+1)*mpmath.pi)**3 * mpmath.cos((2*m+1)*mpmath.pi*z)
    return 2*s

def eta1_qp(tau):
    return -theta1_d3z(0, tau) / (6 * theta1_dz(0, tau))

def wz_zeta(z, tau):
    return theta1_dz(z, tau)/theta1(z, tau) + 2*eta1_qp(tau)*z

# ============================================================
# Parameters
# ============================================================

tau = mpmath.mpc(0, 1)
k = mpmath.mpf(2)
hv = mpmath.mpf(2)
u = mpmath.mpf(1)
z = mpmath.mpc(0.3, 0.1)

alpha0 = mpmath.mpf(-3)/(4*(k+hv))  # -3/16
alpha1 = mpmath.mpf(1)/(4*(k+hv))   # 1/16
hbar = 1/(k+hv)                      # 1/4
R_sing = (u - hbar)/(u + hbar)       # 3/5

zeta_z = wz_zeta(z, tau)
phi0 = mpmath.exp(-alpha0 * zeta_z)
phi1 = mpmath.exp(-alpha1 * zeta_z)

target = mpmath.mpc(0.869, 1.355)

print("=" * 70)
print("SYSTEMATIC EXPLORATION OF NORMALIZATIONS")
print("=" * 70)
print()
print(f"Basic quantities at z={z}, tau={tau}, k={k}, u={u}:")
print(f"  zeta(z) = {zeta_z}")
print(f"  phi_0 = {phi0},  |phi_0| = {float(abs(phi0)):.6f}")
print(f"  phi_1 = {phi1},  |phi_1| = {float(abs(phi1)):.6f}")
print(f"  R_sing = {R_sing}")
print()
print(f"  Target: {target}, |target| = {float(abs(target)):.6f}")
print()

# ============================================================
# Convention A: Bernard's KZB with different normalization
# ============================================================
# Bernard (1988) writes the KZB equation as:
#   d/dz F(z) = (1/(k+h^v)) * Omega * wp(z) * F(z)
# so the coefficient is 1/(k+2), not lambda_J/(k+2).
#
# In this convention:
#   alpha_J^{Bernard} = lambda_J   (no division by k+2)
# Let's compute with this.

print("--- Convention A: Bernard (alpha = lambda, no 1/(k+2) factor) ---")
a0_B = mpmath.mpf(-3)/4
a1_B = mpmath.mpf(1)/4
phi0_B = mpmath.exp(-a0_B * zeta_z)
phi1_B = mpmath.exp(-a1_B * zeta_z)

# Simple difference
psi_B_simple = phi1_B - R_sing * phi0_B
# Full anti-invariant
psi_B_anti = (phi1_B - 1/phi1_B) + R_sing*(phi0_B + 1/phi0_B)

print(f"  phi_0 = {phi0_B}, |.| = {float(abs(phi0_B)):.6f}")
print(f"  phi_1 = {phi1_B}, |.| = {float(abs(phi1_B)):.6f}")
print(f"  Simple: phi_1 - R*phi_0 = {psi_B_simple}, |.| = {float(abs(psi_B_simple)):.6f}")
print(f"  Anti-inv: {psi_B_anti}, |.| = {float(abs(psi_B_anti)):.6f}")
print()

# ============================================================
# Convention B: Different Casimir normalization
# ============================================================
# Some references use Omega = (1/2)(E*F + F*E + H*H/2) with an
# overall factor, or the quadratic Casimir C_2 = 2*Omega.
# The eigenvalue on V_0 would then be -3/2, on V_1 would be +1/2.

print("--- Convention B: Casimir = 2*Omega (eigenvalues doubled) ---")
a0_C2 = mpmath.mpf(-3)/(2*(k+hv))
a1_C2 = mpmath.mpf(1)/(2*(k+hv))
phi0_C2 = mpmath.exp(-a0_C2 * zeta_z)
phi1_C2 = mpmath.exp(-a1_C2 * zeta_z)

psi_C2_simple = phi1_C2 - R_sing * phi0_C2
psi_C2_anti = (phi1_C2 - 1/phi1_C2) + R_sing*(phi0_C2 + 1/phi0_C2)

print(f"  alpha_0 = {a0_C2}, alpha_1 = {a1_C2}")
print(f"  Simple: {psi_C2_simple}, |.| = {float(abs(psi_C2_simple)):.6f}")
print(f"  Anti-inv: {psi_C2_anti}, |.| = {float(abs(psi_C2_anti)):.6f}")
print()

# ============================================================
# Convention C: KZ normalization (Omega/((k+h^v)*z) convention)
# ============================================================
# In the KZ convention, the equation is:
#   (k+h^v) d/dz F = wp(z) * Omega * F
# so alpha_J = lambda_J/(k+h^v)  -- same as ours.
# But with KZ r-matrix R = Omega/((k+h^v)*z), not k*Omega/z.
# This shouldn't change the conformal block.

# ============================================================
# Convention D: Conformal weight normalization
# ============================================================
# The conformal block is often written with a prefactor z^{-h}
# where h is the conformal weight. For V=C^2 (j=1/2):
#   h = j(j+1)/(k+2) = 3/(4(k+2)) = 3/16 for k=2
# Maybe the "E_1 invariant" includes this weight factor.

h_conf = mpmath.mpf(3)/(4*(k+hv))  # = 3/16

# Also, the block might be normalized to have specific behavior at z -> 0.
# phi_J(z) = exp(-alpha_J * zeta(z)) ~ exp(-alpha_J/z) * exp(-alpha_J * O(z))
# as z -> 0, zeta(z) ~ 1/z + regular.

# What if we normalize by the leading singularity?
# At z small: zeta(z) ~ 1/z + 2*eta_1*z + O(z^3)
# phi_J(z) ~ exp(-alpha_J/z) * exp(-2*alpha_J*eta_1*z)
# The first factor is the "connection factor" and the second is finite.
# The "regular" part at z=0 is exp(-2*alpha_J*eta_1*z) * exp(-alpha_J * (zeta - 1/z))

# ============================================================
# Convention E: Different R-matrix
# ============================================================
# The quantum R-matrix for U_q(sl_2) is:
#   R(u) = f(u) * (u*q - u^{-1}*q^{-1}) / (u - u^{-1}) * P + ...
# Various normalizations exist.

# Let's try R_sing = (q*u - 1/(q*u)) / (u - 1/u) where q = exp(pi*i/(k+2))
q_param = mpmath.exp(mpmath.pi*1j/(k+hv))  # q = exp(pi*i/4) for k=2
# At u=1: (u - 1/u) = 0, use L'Hopital or evaluate at nearby u
u_reg = mpmath.mpf(1.01)
R_q_sing = (q_param*u_reg - 1/(q_param*u_reg)) / (u_reg - 1/u_reg)
print(f"--- Convention E: Quantum R-matrix with q = exp(pi*i/(k+2)) ---")
print(f"  q = {q_param}")
print(f"  R_sing^q (at u=1.01) = {R_q_sing}, |.| = {float(abs(R_q_sing)):.6f}")
# At u=1 exactly, by L'Hopital: limit = q + 1/q (for the ratio)
R_q_sing_exact = q_param + 1/q_param  # = 2*cos(pi/(k+2))
print(f"  R_sing^q (u=1 limit) = {R_q_sing_exact}, |.| = {float(abs(R_q_sing_exact)):.6f}")
psi_Eq = phi1 - R_q_sing_exact * phi0
print(f"  Simple: {psi_Eq}, |.| = {float(abs(psi_Eq)):.6f}")
psi_Eq_anti = (phi1 - 1/phi1) + R_q_sing_exact*(phi0 + 1/phi0)
print(f"  Anti-inv: {psi_Eq_anti}, |.| = {float(abs(psi_Eq_anti)):.6f}")
print()

# ============================================================
# Convention F: Etingof-Schiffmann elliptic quantum group R-matrix
# ============================================================
# The Etingof-Varchenko / Felder elliptic R-matrix for sl_2 involves
# theta functions:
#   R^{ell}(z, lambda, tau, eta) = ...
# where lambda is the dynamical parameter and eta = 1/(2(k+2)).
# The E_1 invariant might USE the elliptic R-matrix eigenvalue.

eta_param = 1/(2*(k+hv))  # = 1/8

# For sl_2 in the fundamental, the Felder R-matrix eigenvalues on
# singlet/triplet are:
#   R_trip^{ell}(z) = theta_1(z|tau)*theta_1(eta|tau) / (theta_1(z+eta|tau)*theta_1(-eta|tau))  ??
# Actually the Baxter-Belavin R-matrix for sl_2 at eta=1/(2(k+2)):
#   R^{BB}(z, eta, tau) has eigenvalues involving theta-function ratios.

# Let me try the standard Baxter parameterization:
# a(z) = theta_1(z+eta|tau) / theta_1(z|tau)  (on triplet)
# b(z) = theta_1(eta|tau) / theta_1(z|tau)    (coupling)
# c(z) = ...
# The R-matrix eigenvalue on the singlet is related to:
#   R_sing = theta_1(z-eta|tau) / theta_1(z+eta|tau)

eta_ell = 1/(2*(k+hv))  # = 1/8
th_z = theta1(z, tau)
th_z_plus_eta = theta1(z + eta_ell, tau)
th_z_minus_eta = theta1(z - eta_ell, tau)
th_eta = theta1(eta_ell, tau)

R_ell_sing = th_z_minus_eta / th_z_plus_eta

print(f"--- Convention F: Elliptic R-matrix eigenvalue ---")
print(f"  eta_ell = 1/(2(k+2)) = {eta_ell}")
print(f"  theta_1(z-eta) / theta_1(z+eta) = {R_ell_sing}")
print(f"  |R_ell_sing| = {float(abs(R_ell_sing)):.6f}")
print()

# E_1 block with elliptic R-matrix:
psi_F_simple = phi1 - R_ell_sing * phi0
print(f"  Simple: phi_1 - R^ell*phi_0 = {psi_F_simple}, |.| = {float(abs(psi_F_simple)):.6f}")
psi_F_anti = (phi1 - 1/phi1) + R_ell_sing*(phi0 + 1/phi0)
print(f"  Anti-inv: {psi_F_anti}, |.| = {float(abs(psi_F_anti)):.6f}")
print()

# ============================================================
# Convention G: The "transfer matrix" / "partition function" formulation
# ============================================================
# In the Yangian/quantum group formulation, the E_1 invariant is often
# the TRACE of the R-matrix in the auxiliary space times the conformal block:
#   Psi = Tr_V (R(u) * Phi(z))
# For V = C^2:
#   Tr_V R(u) * Phi = R_trip * dim(V_1)/dim(V) * phi_1 + R_sing * dim(V_0)/dim(V) * phi_0
# with dim(V_1)=3, dim(V_0)=1, dim(V)=4 (in the V tensor V decomposition)
# Hmm, this is more involved. Let me try a simpler version:
# Psi = phi_1 + R_sing * phi_0 (sum, not difference)

psi_G_sum = phi1 + R_sing * phi0
print(f"--- Convention G: Sum phi_1 + R*phi_0 ---")
print(f"  {psi_G_sum}, |.| = {float(abs(psi_G_sum)):.6f}")
print()

# ============================================================
# Convention H: Include theta_1 / eta^3 prime form normalization
# ============================================================
# The "prime form" E(z) = theta_1(z|tau) / theta_1'(0|tau)
# The conformal block might be normalized by E(z)^h or 1/E(z)^h.

th1_z = theta1(z, tau)
th1p0 = theta1_dz(0, tau)
E_z = th1_z / th1p0  # prime form

print(f"--- Convention H: Prime form factors ---")
print(f"  E(z) = theta_1(z)/theta_1'(0) = {E_z}")
print(f"  |E(z)| = {float(abs(E_z)):.6f}")

for h_try in [h_conf, 2*h_conf, -h_conf, mpmath.mpf(1)/2, mpmath.mpf(1)]:
    factor = E_z**(-h_try)
    psi_H = psi_B_simple * factor
    psi_H2 = (phi1 - R_sing*phi0) * factor
    if abs(float(abs(psi_H)) - 1.61) < 0.1 or abs(float(abs(psi_H2)) - 1.61) < 0.1:
        print(f"  *** POSSIBLE MATCH at h={float(h_try):.4f}: |Psi| = {float(abs(psi_H)):.6f} (Bernard), {float(abs(psi_H2)):.6f} (ours)")
    else:
        print(f"  h={float(h_try):.4f}: |Psi| = {float(abs(psi_H)):.6f} (Bernard), {float(abs(psi_H2)):.6f} (ours)")

print()

# ============================================================
# Convention I: Felder's conformal block normalization
# ============================================================
# Felder (1994) normalizes the KZB conformal block by:
#   Phi(z) = theta_1(z|tau)^{-lambda_J/(k+h^v)} * (smooth factor)
# This removes the essential singularity at z=0.
# The "smooth factor" is what's computed as the holonomy.

# With the theta_1 prefactor:
# phi_J^{Felder} = theta_1(z)^{-alpha_J} * (holonomy part)
# where holonomy = exp(-alpha_J * 2*eta_1*z)
# Actually: phi_J = exp(-alpha_J * zeta) = exp(-alpha_J * [dlog theta_1 + 2*eta_1*z])

# The "holonomy" (smooth) part is extracted by dividing by the theta_1 singularity:
# phi_J / theta_1(z)^{-alpha_J} = exp(-alpha_J * zeta) / theta_1(z)^{-alpha_J}
#                                = exp(-alpha_J * zeta + alpha_J * log theta_1)
#                                = exp(-alpha_J * 2*eta_1*z)   (just the eta correction!)

# Hmm, that's too simple. Let me reconsider.
# zeta(z) = dlog theta_1(z) + 2*eta_1*z
# So: -alpha_J * zeta(z) = -alpha_J * dlog theta_1(z) - 2*alpha_J*eta_1*z
# But exp(-alpha_J * dlog theta_1) is NOT theta_1^{-alpha_J} !!!
# Because dlog theta_1 = theta_1'/theta_1 is evaluated at z, not integrated.
# The integral of dlog theta_1 FROM 0 to z is log(theta_1(z)/theta_1(0)),
# but theta_1(0) = 0, so this requires regularization.

# Actually, let me think about this differently.
# The SIGMA FUNCTION is: sigma(z) = (theta_1(z)/theta_1'(0)) * exp(eta_1*z^2)
# So log sigma(z) = log theta_1(z) - log theta_1'(0) + eta_1*z^2
# And zeta(z) = d/dz log sigma = theta_1'(z)/theta_1(z) + 2*eta_1*z
# The integral of zeta from z_0 to z is:
# int zeta dz = log sigma(z) - log sigma(z_0)
#             = log theta_1(z) + eta_1*z^2 - log theta_1(z_0) - eta_1*z_0^2

# But we have phi(z) = exp(-alpha * zeta(z)), not exp(-alpha * int zeta dz).
# These are COMPLETELY DIFFERENT things.
# exp(-alpha * zeta(z)) involves zeta EVALUATED at z (a function value).
# exp(-alpha * int zeta) = sigma(z)^{-alpha} (up to const).

# So there's no clean "theta_1^{-alpha}" form for our solution.

# ============================================================
# Convention J: The SIGMA FUNCTION solution
# ============================================================
# Wait - let me reconsider the ODE. Maybe I made an error.
# ODE: (k+2) phi' = lambda * wp * phi
# phi' = alpha * wp * phi, alpha = lambda/(k+2)
#
# wp(z) = -zeta'(z)
# phi' = -alpha * zeta'(z) * phi
# d(log phi) = -alpha * zeta'(z) dz
# INTEGRAL: log phi(z) - log phi(z0) = -alpha * [zeta(z) - zeta(z0)]
# phi(z) = phi(z0) * exp(-alpha * [zeta(z) - zeta(z0)])
#
# So phi(z) = C * exp(-alpha * zeta(z)).  Confirmed: this involves
# zeta(z) EVALUATED, not integrated.

# But wait, what if the ODE should use a different elliptic function?
# Some references write the KZB equation with the Weierstrass P-function
# but defined differently (e.g., for periods (2*omega_1, 2*omega_2)
# instead of (1, tau)).

# In our convention: periods = (1, tau), half-periods = (1/2, tau/2).
# The standard convention in much of the literature: periods = (2*omega_1, 2*omega_2)
# with the modular parameter tau = omega_2/omega_1.
# If omega_1 = 1/2, omega_2 = tau/2, then periods = (1, tau). Same.
#
# But some references use omega_1 = 1, omega_2 = tau (periods (2, 2*tau)).
# The Weierstrass functions for lattice (2, 2*tau) differ from (1, tau) by scaling:
#   wp_{(2,2tau)}(z) = (1/4) * wp_{(1,tau)}(z/2)
# This could introduce factors of 2 or 4.

# ============================================================
# Convention K: Bernard's exact normalization
# ============================================================
# Bernard (1988) equation (2.12):
# partial_z Phi = (1/(k+h^v)) * sum_{a} (t_a (x) t_a) * wp(z) * Phi
# where t_a are generators in a specific normalization.
# For sl_2 fund: t_a = sigma_a / 2 (Pauli/2)
# Omega = sum t_a (x) t_a = (1/4)(sigma_1 x sigma_1 + sigma_2 x sigma_2 + sigma_3 x sigma_3)
# In the {singlet, triplet} basis:
#   Omega|_singlet = -3/4, Omega|_triplet = 1/4
# This matches our convention.

# Bernard's equation: phi'_J = lambda_J/(k+h^v) * wp(z) * phi_J
# alpha_J = lambda_J/(k+h^v) = lambda_J/(k+2)
# This confirms our alpha_0 = -3/16, alpha_1 = 1/16 for k=2.

# ============================================================
# KEY INSIGHT: The previous agent's computation might have used
# a DIFFERENT test point or a different meaning of "u=1"
# ============================================================

print("=" * 70)
print("EXPLORING: Different meanings of u=1")
print("=" * 70)
print()

# In the Yangian Y_hbar(sl_2), the spectral parameter u and hbar
# can be related to the KZB data in multiple ways:
# (a) u = additive spectral parameter, hbar = 1/(k+2)
# (b) u = z (the KZB coordinate IS the spectral parameter)
# (c) u = exp(2*pi*i*z) (multiplicative spectral parameter)
# (d) u = theta_1(z)/theta_1'(0) (elliptic spectral parameter)

# Let's try (c): u = exp(2*pi*i*z), then z = log(u)/(2*pi*i)
z_from_u = mpmath.log(u)/(2*mpmath.pi*1j)
print(f"If u = exp(2*pi*i*z), z = {z_from_u}")
print("  (z = 0, which is a lattice point - singular!)")
print()

# Let's try u as the ELLIPTIC spectral parameter
# u = theta_1(z|tau)/theta_1'(0|tau), then we need to solve for z.
# At tau=i, theta_1'(0|i) ~ 2.849.
# We want theta_1(z|i)/2.849 = 1, so theta_1(z|i) = 2.849
# This is close to z where theta_1 achieves its maximum.

# Actually the Yangian parameter might be:
# u = e^{2*pi*i*z*hbar} or u = z itself.

# Let me try z = u = 1 (the previous agent might have used z=1 directly,
# but z=1 is a period!). Let me try z near 0:

# What if the "E_1 invariant" is the VALUE of the R-matrix eigenvalue itself
# evaluated at a specific point, not a conformal block?

# Actually, let me reconsider completely. The "E_1 holomorphic invariant
# living in ker(av_2)" is the E_1 content of the genus-1 shadow tower.
# In the manuscript, this is related to Theta_A restricted to M_{1,2}.
# The VALUE Psi_E1 = 0.869 + 1.355i might be computed from a DIFFERENT
# formula entirely.

# Let me try: maybe the computation used the ELLIPTIC r-matrix directly
# (not the conformal block), evaluated at z with specific normalization.

# The Belavin r-matrix for sl_2: r(z,tau) = zeta(z)*H(x)H/2 + phi_+(z)E(x)F + ...
# The eigenvalue on the singlet (antisymmetric) subspace involves the
# Weierstrass functions in a specific combination.

# On the singlet e(x)f - f(x)e (normalized):
# r|_singlet = zeta(z)/2 * (1/2 - 1/2 - 1/2) + ...

# Actually for the full Casimir Omega = E(x)F + F(x)E + (1/2)H(x)H:
# On singlet: Omega = 1*(-1) + 1*(-1) + (1/2)*(1*(-1)+(-1)*1)/2 = wait,
# let me compute properly.

# V = C^2 with basis e_1, e_2.
# e_1 (x) e_2 - e_2 (x) e_1 is the singlet (up to normalization).
# H(x)H acting on e_1(x)e_2: H*e_1 = e_1, H*e_2 = -e_2
# So (H(x)H)(e_1(x)e_2) = e_1 (x) (-e_2) = -(e_1(x)e_2)
# (1/2)(H(x)H)|_singlet eigenvalue = -1/2
# E(x)F acting: E*e_1=0, F*e_2=e_1, so (E(x)F)(e_1(x)e_2) = 0
# F(x)E acting: F*e_1=e_2, E*e_2=0, so (F(x)E)(e_1(x)e_2) = e_2(x)0 = 0
# Wait that's wrong. Let me redo:
# E(x)F: left=E, right=F
# (E(x)F)(e_1(x)e_2) = E(e_1) (x) F(e_2) = 0 (x) e_1 = 0
# (E(x)F)(e_2(x)e_1) = E(e_2) (x) F(e_1) = 0 (x) e_2 = 0
# Hmm, E(e_1) = 0 (e_1 is highest weight), E(e_2) = e_1, F(e_1) = e_2, F(e_2) = 0.
# (E(x)F)(e_1(x)e_2) = 0 * e_1 = 0
# (E(x)F)(e_2(x)e_1) = e_1 * 0 = 0
# Wait no. E*e_1=0, E*e_2=e_1. F*e_1=e_2, F*e_2=0.
# (E(x)F) acts as: v(x)w -> E(v)(x)F(w).
# (E(x)F)(e_1(x)e_2) = E(e_1)(x)F(e_2) = 0(x)0 = 0
# (E(x)F)(e_2(x)e_1) = E(e_2)(x)F(e_1) = e_1(x)e_2
# So E(x)F on singlet (e_1(x)e_2 - e_2(x)e_1):
#   = 0 - e_1(x)e_2 = -e_1(x)e_2 = -(1/2)(singlet + triplet_0)
# Hmm, this mixes. Actually on the SINGLET subspace:
# P_0 * (E(x)F) * P_0 where P_0 projects onto singlet.

# The singlet is (1/sqrt(2))(e_1(x)e_2 - e_2(x)e_1).
# Similarly (F(x)E)(e_1(x)e_2) = F(e_1)(x)E(e_2) = e_2(x)e_1
# (F(x)E)(e_2(x)e_1) = F(e_2)(x)E(e_1) = 0(x)0 = 0
# F(x)E on singlet: e_2(x)e_1 - 0 = e_2(x)e_1 = -(1/2)(singlet - triplet_0)

# So (E(x)F + F(x)E)|_singlet = -e_1(x)e_2 + e_2(x)e_1 = -(e_1(x)e_2 - e_2(x)e_1) = -singlet * sqrt(2) * ...
# Actually: on singlet s = (e_1(x)e_2 - e_2(x)e_1)/sqrt(2):
# (E(x)F)(s) = (1/sqrt(2))[-e_1(x)e_2] (from calculation above... let me be more careful)
# (E(x)F)(e_1(x)e_2 - e_2(x)e_1) = 0 - e_1(x)e_2 = -e_1(x)e_2
# (F(x)E)(e_1(x)e_2 - e_2(x)e_1) = e_2(x)e_1 - 0 = e_2(x)e_1
# Sum: (E(x)F + F(x)E)(s_unnorm) = -e_1(x)e_2 + e_2(x)e_1 = -(e_1(x)e_2 - e_2(x)e_1) = -s_unnorm
# And (1/2)(H(x)H)(s_unnorm): H(x)H(e_1(x)e_2) = e_1(x)(-e_2) = -e_1(x)e_2
#                               H(x)H(e_2(x)e_1) = (-e_2)(x)e_1 = -e_2(x)e_1
# So (1/2)H(x)H(s_unnorm) = (1/2)(-e_1(x)e_2 - (-e_2(x)e_1)) = (1/2)(-e_1(x)e_2 + e_2(x)e_1)
# Wait: H(x)H(e_1(x)e_2 - e_2(x)e_1) = (H*e_1)(x)(H*e_2) - (H*e_2)(x)(H*e_1)
#   = e_1(x)(-e_2) - (-e_2)(x)e_1 = -e_1(x)e_2 + e_2(x)e_1 = -(e_1(x)e_2 - e_2(x)e_1) = -s_unnorm
# So (1/2)H(x)H|_singlet = -1/2

# Total: Omega|_singlet = (E(x)F + F(x)E + (1/2)H(x)H)|_singlet = -1 + (-1/2) = -3/2
# Hmm wait, that gives -3/2, not -3/4!

# Let me double-check. The Casimir C_2 = sum_a t_a (x) t_a where {t_a} is an
# orthonormal basis of g with respect to the Killing form.
# For sl_2 with Killing form (X,Y) = 4*Tr(XY):
#   ON basis: E, F, H with (E,F) = 4, (H,H) = 8
#   t_a: e = E/2, f = F/2, h = H/(2*sqrt(2))
# Then Omega = e(x)f + f(x)e + h(x)h = (1/4)(E(x)F + F(x)E) + (1/8)H(x)H
# Omega|_singlet = (1/4)*(-2) + (1/8)*(-2) = -1/2 - 1/4 = -3/4. Yes!

# OK so different normalization of the Casimir gives different eigenvalues.
# With Omega = E(x)F + F(x)E + (1/2)H(x)H:
#   lambda_0 = -3/2, lambda_1 = 1/2
# With Omega = (1/4)(E(x)F + F(x)E) + (1/8)H(x)H:  [trace form]
#   lambda_0 = -3/4, lambda_1 = 1/4

# The TRACE FORM normalization gives -3/4, 1/4 (what we used).
# The MATRIX normalization gives -3/2, 1/2.

# Let me compute with the matrix normalization:
print("--- Convention: Matrix Casimir (double eigenvalues) ---")
a0_mat = mpmath.mpf(-3)/(2*(k+hv))   # = -3/8
a1_mat = mpmath.mpf(1)/(2*(k+hv))    # = 1/8
phi0_mat = mpmath.exp(-a0_mat * zeta_z)
phi1_mat = mpmath.exp(-a1_mat * zeta_z)

psi_mat_simple = phi1_mat - R_sing * phi0_mat
psi_mat_anti = (phi1_mat - 1/phi1_mat) + R_sing*(phi0_mat + 1/phi0_mat)
psi_mat_anti_half = psi_mat_anti / 2

print(f"  alpha_0 = -3/8, alpha_1 = 1/8")
print(f"  phi_0 = {phi0_mat}, |.| = {float(abs(phi0_mat)):.6f}")
print(f"  phi_1 = {phi1_mat}, |.| = {float(abs(phi1_mat)):.6f}")
print(f"  Simple: {psi_mat_simple}, |.| = {float(abs(psi_mat_simple)):.6f}")
print(f"  Anti-inv (no 1/2): {psi_mat_anti}, |.| = {float(abs(psi_mat_anti)):.6f}")
print(f"  Anti-inv (with 1/2): {psi_mat_anti_half}, |.| = {float(abs(psi_mat_anti_half)):.6f}")
print()

# Sinh/cosh form for matrix convention
psi_mat_sc = R_sing * mpmath.cosh(a0_mat * zeta_z) - mpmath.sinh(a1_mat * zeta_z)
print(f"  Sinh/cosh: {psi_mat_sc}, |.| = {float(abs(psi_mat_sc)):.6f}")
print()

# ============================================================
# What if the formula used exp(alpha * integral of wp(z)dz)?
# ============================================================
# Some references write the KZB solution as:
#   Phi(z) ~ [sigma(z)]^{-h_V/(k+h^v)} * (holonomy)
# where h_V = j(j+1) is the spin Casimir.
# For j=1/2: h_V = 3/4.
# So the exponent is -3/(4*(k+2)).
# sigma(z) = (theta_1(z)/theta_1'(0)) * exp(eta_1*z^2)

sigma_z = (theta1(z, tau) / theta1_dz(0, tau)) * mpmath.exp(eta1_qp(tau)*z**2)
print(f"sigma(z) = {sigma_z}")
print(f"|sigma(z)| = {float(abs(sigma_z)):.6f}")
print()

# Phi = sigma(z)^{-alpha} where alpha = 3/(4(k+2)) = 3/16
alpha_sigma = mpmath.mpf(3)/(4*(k+hv))
phi_sigma = sigma_z**(-alpha_sigma)
print(f"sigma(z)^{{-3/16}} = {phi_sigma}")
print(f"|.| = {float(abs(phi_sigma)):.6f}")
print()

# Or with the "full" Casimir eigenvalue
phi_sigma2 = sigma_z**(mpmath.mpf(3)/4)  # exponent = +3/4
print(f"sigma(z)^{{+3/4}} = {phi_sigma2}")
print(f"|.| = {float(abs(phi_sigma2)):.6f}")
print()

# Actually, let me try the RATIO of sigma functions as a candidate
# for the E_1 block. In the KZB theory, the conformal block is often
# proportional to a product of sigma (or theta_1) functions.

# For sl_2, fund x fund on E_tau:
# Phi(z) = theta_1(z|tau)^{Omega/(k+2)} (symbolically)
# On singlet: theta_1(z)^{-3/(4(k+2))}
# On triplet: theta_1(z)^{1/(4(k+2))}
# These involve fractional powers of theta_1, which are multi-valued.

# The E_1 invariant in the Yangian sense might be:
# Psi = theta_1(z + eta|tau) / theta_1(z|tau)  (shift by spectral parameter)
# This is the TRANSFER MATRIX eigenvalue in the elliptic quantum group.

th_z_shifted = theta1(z + hbar, tau)
transfer_ratio = th_z_shifted / theta1(z, tau)
print(f"theta_1(z+hbar|tau)/theta_1(z|tau) = {transfer_ratio}")
print(f"|.| = {float(abs(transfer_ratio)):.6f}")
print()

# Or the full transfer matrix trace:
# T(z) = theta_1(z+hbar|tau)/theta_1(z|tau) * R_trip + theta_1(z-hbar|tau)/theta_1(z|tau) * R_sing
th_z_minus = theta1(z - hbar, tau)
T_z = th_z_shifted/theta1(z,tau) * 1 + th_z_minus/theta1(z,tau) * R_sing
print(f"Transfer matrix trace T(z) = {T_z}")
print(f"|T(z)| = {float(abs(T_z)):.6f}")
print()

# ============================================================
# Direct match search over a wide grid of conventions
# ============================================================
print("=" * 70)
print("BRUTE-FORCE: Which combination has |.| ~ 1.61?")
print("=" * 70)
print()

candidates = {
    "phi0": phi0,
    "phi1": phi1,
    "1/phi0": 1/phi0,
    "1/phi1": 1/phi1,
    "phi0*phi1": phi0*phi1,
    "phi0/phi1": phi0/phi1,
    "phi1/phi0": phi1/phi0,
    "phi0-phi1": phi0-phi1,
    "phi0+phi1": phi0+phi1,
    "phi0-R*phi1": phi0-R_sing*phi1,
    "phi1-R*phi0": phi1-R_sing*phi0,
    "phi1+R*phi0": phi1+R_sing*phi0,
    "anti_no_half": psi_mat_anti,  # reuse the one already computed
    "anti_w_half": psi_mat_anti/2,
    "mat_simple": psi_mat_simple,
    "mat_anti": psi_mat_anti,
    "mat_anti/2": psi_mat_anti_half,
    "B_simple": psi_B_simple,
    "B_anti": psi_B_anti,
    "sigma_neg": phi_sigma,
    "sigma_pos": phi_sigma2,
    "transfer_ratio": transfer_ratio,
    "T_z": T_z,
    "R_ell_sing": R_ell_sing,
    "psi_F_simple": psi_F_simple,
    "psi_F_anti": psi_F_anti,
}

# Also try with normalization factors
th1p0_val = theta1_dz(0, tau)
eta_ded = mpmath.mpf(0.768225422326056659)  # eta(i)

norm_factors = {
    "1": mpmath.mpf(1),
    "th1p0": th1p0_val,
    "1/th1": 1/theta1(z, tau),
    "th1p0/th1": th1p0_val/theta1(z, tau),
    "1/eta^2": 1/eta_ded**2,
    "2*pi*i": 2*mpmath.pi*1j,
    "pi": mpmath.pi,
    "2*pi": 2*mpmath.pi,
    "k+2": k+hv,
    "1/(k+2)": 1/(k+hv),
    "sqrt(k+2)": mpmath.sqrt(k+hv),
}

psi_E1_no_half = (phi1 - 1/phi1) + R_sing*(phi0 + 1/phi0)

matches = []
for cname, cval in candidates.items():
    for nname, nval in norm_factors.items():
        val = cval * nval
        mag = float(abs(val))
        if abs(mag - 1.61) < 0.05:
            matches.append((cname, nname, val, mag))

if matches:
    print("MATCHES found (|.| within 0.05 of 1.61):")
    for cname, nname, val, mag in matches:
        print(f"  {cname} * {nname} = {val}")
        print(f"    |.| = {mag:.6f}")
        # Check complex value match
        target_diff = float(abs(val - target))
        print(f"    |val - target| = {target_diff:.6f}")
        print()
else:
    print("No exact matches found. The previous agent likely used a")
    print("different computational approach or different evaluation point.")
    print()

# ============================================================
# FINAL: The correct formula regardless of the claimed value
# ============================================================
print("=" * 70)
print("DEFINITIVE FORMULA (independent of claimed value)")
print("=" * 70)
print()
print("The antisymmetric KZB conformal block on E_tau for sl_2")
print("at level k, fundamental representation V = C^2:")
print()
print("Individual channel solutions of (k+2)*phi'_J = lambda_J*wp(z)*phi_J:")
print()
print("  phi_J(z; tau) = exp(-alpha_J * zeta(z; tau))")
print()
print("  alpha_0 = -3/(4(k+2))  (singlet, J=0)")
print("  alpha_1 =  1/(4(k+2))  (triplet, J=1)")
print()
print("The E_1 KZB block (Sigma_2-anti-invariant of the R-matrix-")
print("twisted ordered block):")
print()
print("  Psi_{E_1}(z; tau, k, u)")
print("    = R(u,k)*cosh(3*zeta(z;tau)/(4(k+2)))")
print("      - sinh(zeta(z;tau)/(4(k+2)))")
print()
print("where:")
print("  R(u,k)      = (u - 1/(k+2))/(u + 1/(k+2))")
print("  zeta(z;tau)  = theta_1'(z|tau)/theta_1(z|tau) + (pi^2/3)*E_2(tau)*z")
print("  (using eta_1 = pi^2/6 * E_2(tau))")
print()
print("Quasi-periodicity multipliers:")
print("  phi_J(z+1) = phi_J(z) * exp(-2*alpha_J*eta_1)")
print("  phi_J(z+tau) = phi_J(z) * exp(-2*alpha_J*eta_2)")
print("  eta_2 = eta_1*tau - pi*i  (Legendre relation)")
print()
print("Modular: T-invariant. S mixes channels (flat bundle section).")
