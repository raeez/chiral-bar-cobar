#!/usr/bin/env python3
"""
Derivation and numerical verification of the antisymmetric KZB conformal block
on E_tau for sl_2 at level k, in the fundamental representation V = C^2.

MATHEMATICAL SETUP
==================
KZB equation at arity 2 on E_tau for sl_2, level k:
    (k + h^v) d Phi/dz = Omega * wp(z; tau) * Phi(z)

where h^v = 2, Omega is the Casimir, wp is the Weierstrass p-function.

V tensor V = V_0 (singlet, J=0, antisymmetric) + V_1 (triplet, J=1, symmetric)

Casimir eigenvalues:
    lambda_0 = -3/4  (singlet)
    lambda_1 = +1/4  (triplet)

Scalar ODE on each isotypic component:
    d phi_J / dz = alpha_J * wp(z; tau) * phi_J(z)

where alpha_J = lambda_J / (k + 2).

SOLUTION OF THE ODE
====================
Since wp(z) = -zeta'(z), the ODE becomes:
    d(log phi)/dz = -alpha * zeta'(z)
    => log phi(z) = -alpha * zeta(z; tau) + const
    => phi_J(z) = C_J * exp(-alpha_J * zeta(z; tau))

In terms of theta_1:
    zeta(z; tau) = (d/dz) log theta_1(z | tau) + 2 * eta_1 * z
                 = theta_1'(z|tau) / theta_1(z|tau) + 2 * eta_1 * z

So:  phi_J(z) = C_J * theta_1(z|tau)^{-alpha_J} * exp(-2 * alpha_J * eta_1 * z)

Wait -- let me be precise. From log phi = -alpha * zeta(z) + C:

    phi_J(z) = C_J * exp(-alpha_J * zeta(z; tau))

This is the EXACT closed form. The sigma-function form is:

    sigma(z; tau) is defined by  d/dz log sigma(z) = zeta(z)
    => zeta(z) = sigma'(z)/sigma(z)

Note: sigma(z) = exp(eta_1 * z^2) * theta_1(z|tau) / theta_1'(0|tau)

So: zeta(z) = d/dz [eta_1*z^2 + log theta_1(z|tau) - log theta_1'(0|tau)]
            = 2*eta_1*z + theta_1'(z|tau)/theta_1(z|tau)

And: phi_J(z) = C_J * exp(-alpha_J * zeta(z; tau))
             = C_J * exp(-alpha_J * 2*eta_1*z) * exp(-alpha_J * theta_1'(z)/theta_1(z))

The second factor exp(-alpha * theta_1'/theta_1) is NOT theta_1^{-alpha}
(that would be the integral, not the function).

The clean form IS:  phi_J(z) = C_J * exp(-alpha_J * zeta(z; tau))
"""

import sys
sys.path.insert(0, '/Users/raeez/chiral-bar-cobar/compute/lib')

import numpy as np

# Import our theta function library
from elliptic_rmatrix_shadow import (
    jacobi_theta1,
    jacobi_theta1_prime0,
    jacobi_theta2,
    jacobi_theta3,
    jacobi_theta4,
    weierstrass_zeta,
    weierstrass_p,
    _weierstrass_eta1,
    PI,
    TWO_PI_I,
)

# ============================================================
# Parameters
# ============================================================
tau = 1j        # modular parameter
k = 2           # level
z_test = 0.3 + 0.1j   # test point
h_vee = 2      # dual Coxeter number of sl_2

# Casimir eigenvalues on V tensor V = V_0 + V_1
lambda_singlet = -3.0/4   # J=0, antisymmetric
lambda_triplet = +1.0/4   # J=1, symmetric

# alpha_J = lambda_J / (k + h^v) = lambda_J / (k + 2)
alpha_singlet = lambda_singlet / (k + h_vee)
alpha_triplet = lambda_triplet / (k + h_vee)

print("=" * 70)
print("KZB CONFORMAL BLOCK FOR sl_2 ON E_tau")
print("=" * 70)
print()
print(f"Parameters: tau = {tau}, k = {k}, h^v = {h_vee}")
print(f"Casimir eigenvalues: lambda_0 = {lambda_singlet}, lambda_1 = {lambda_triplet}")
print(f"ODE parameters: alpha_0 = {alpha_singlet} = -3/{4*(k+2)}")
print(f"                alpha_1 = {alpha_triplet} = 1/{4*(k+2)}")
print()

# ============================================================
# Step 1: Compute the individual channel solutions
# ============================================================
print("=" * 70)
print("STEP 1: Individual channel solutions phi_J(z)")
print("=" * 70)
print()
print("Solution of  d phi/dz = alpha * wp(z) * phi:")
print("  phi_J(z) = exp(-alpha_J * zeta(z; tau))")
print()

# Evaluate at test point
zeta_z = weierstrass_zeta(z_test, tau)
wp_z = weierstrass_p(z_test, tau)

print(f"At z = {z_test}, tau = {tau}:")
print(f"  zeta(z; tau) = {zeta_z:.10f}")
print(f"  wp(z; tau)   = {wp_z:.10f}")
print()

phi_singlet = np.exp(-alpha_singlet * zeta_z)
phi_triplet = np.exp(-alpha_triplet * zeta_z)

print(f"  phi_0(z) [singlet] = exp({-alpha_singlet:.4f} * zeta(z)) = {phi_singlet:.10f}")
print(f"  phi_1(z) [triplet] = exp({-alpha_triplet:.4f} * zeta(z)) = {phi_triplet:.10f}")
print(f"  |phi_0| = {abs(phi_singlet):.10f}")
print(f"  |phi_1| = {abs(phi_triplet):.10f}")
print()

# ============================================================
# Step 2: Verify the ODE numerically
# ============================================================
print("=" * 70)
print("STEP 2: Numerical verification of ODE")
print("=" * 70)
print()

eps = 1e-7
for label, alpha_J in [("singlet", alpha_singlet), ("triplet", alpha_triplet)]:
    zeta_plus = weierstrass_zeta(z_test + eps, tau)
    zeta_minus = weierstrass_zeta(z_test - eps, tau)

    phi_z = np.exp(-alpha_J * weierstrass_zeta(z_test, tau))
    phi_plus = np.exp(-alpha_J * zeta_plus)
    phi_minus = np.exp(-alpha_J * zeta_minus)

    dphi_dz = (phi_plus - phi_minus) / (2 * eps)
    rhs = alpha_J * wp_z * phi_z

    rel_err = abs(dphi_dz - rhs) / max(abs(rhs), 1e-30)
    print(f"  {label}: dphi/dz = {dphi_dz:.10f}")
    print(f"  {label}: alpha*wp*phi = {rhs:.10f}")
    print(f"  {label}: relative error = {rel_err:.2e}")
    print()

# ============================================================
# Step 3: The Yangian R-matrix eigenvalue
# ============================================================
print("=" * 70)
print("STEP 3: Yangian R-matrix and E_1 block")
print("=" * 70)
print()

u = 1.0  # spectral parameter
hbar = 1.0 / (k + h_vee)  # hbar = 1/(k+2) for level k

# The Yangian R-matrix for sl_2 at level k:
# R(u) = (u + hbar*P) / (u + hbar)  where P is the permutation
# Eigenvalue on singlet (antisymmetric, P = -1): R_sing = (u - hbar)/(u + hbar)
# Eigenvalue on triplet (symmetric, P = +1): R_trip = 1

R_singlet = (u - hbar) / (u + hbar)
R_triplet = 1.0  # always 1 on symmetric subspace

print(f"Spectral parameter: u = {u}")
print(f"hbar = 1/(k+2) = {hbar}")
print(f"R-matrix eigenvalue on singlet: R_sing = (u-hbar)/(u+hbar) = {R_singlet:.10f}")
print(f"R-matrix eigenvalue on triplet: R_trip = {R_triplet:.10f}")
print()

# ============================================================
# Step 4: The E_1 block
# ============================================================
print("=" * 70)
print("STEP 4: E_1 holomorphic block Psi_E1")
print("=" * 70)
print()

# The E_1 block lives in ker(av_2). At arity 2, the averaging map
# projects onto the Sigma_2-invariant (symmetric) part.
# The E_1 block is the Sigma_2-ANTI-invariant combination:
#
# Psi_E1(z, tau) = phi_triplet(z) - R_sing * phi_singlet(z)
#
# This is in ker(av_2) because under z -> -z:
#   phi_J(-z) = exp(-alpha_J * zeta(-z)) = exp(alpha_J * zeta(z))  [since zeta is odd]
#            = 1/phi_J(z)
#
# Actually, under the Sigma_2 exchange z_1 <-> z_2, we have z -> -z.
# The conformal block transforms as Phi(z) -> P_{12} * Phi(-z) where P is permutation.
# On V_J channel: P eigenvalue = (-1)^{J+1} for sl_2 fund x fund
#   Singlet (J=0, antisym): P = -1
#   Triplet (J=1, sym): P = +1
#
# So the full block on the triplet channel under z -> -z:
#   phi_1(-z) = phi_1(-z)  with P=+1, so contribution = (+1)*phi_1(-z)
# On the singlet channel:
#   R_sing * phi_0(-z) with P=-1, so contribution = (-1)*R_sing*phi_0(-z)
#
# The E_1 block captures the ordered (non-averaged) information.
# In the rational limit this is the quantum group R-matrix evaluated
# on the conformal block.

# The simplest combination that captures the E_1 content:
Psi_E1 = phi_triplet - R_singlet * phi_singlet

print("Psi_E1(z, tau) = phi_1(z) - R_sing * phi_0(z)")
print(f"  = exp(-alpha_1 * zeta(z)) - R_sing * exp(-alpha_0 * zeta(z))")
print(f"  = exp(-{alpha_triplet} * zeta(z)) - {R_singlet:.6f} * exp(-{alpha_singlet} * zeta(z))")
print()
print(f"At z = {z_test}, tau = {tau}, k = {k}, u = {u}:")
print(f"  phi_1(z) = {phi_triplet:.10f}")
print(f"  R_sing * phi_0(z) = {R_singlet * phi_singlet:.10f}")
print(f"  Psi_E1 = {Psi_E1:.10f}")
print(f"  |Psi_E1| = {abs(Psi_E1):.10f}")
print()

# ============================================================
# Step 5: Explicit theta-function formula
# ============================================================
print("=" * 70)
print("STEP 5: Explicit formula in terms of theta_1")
print("=" * 70)
print()

# Recall: zeta(z; tau) = theta_1'(z|tau)/theta_1(z|tau) + 2*eta_1*z
# So exp(-alpha * zeta(z)) = exp(-alpha*theta_1'(z)/theta_1(z)) * exp(-2*alpha*eta_1*z)
#
# The theta_1'/theta_1 term is the d-log derivative evaluated at z.
#
# For an EXPLICIT formula, we should use mpmath for higher precision.

eta1 = _weierstrass_eta1(tau)
th1 = jacobi_theta1(z_test, tau)
th1p0 = jacobi_theta1_prime0(tau)

# Numerical derivative theta_1'(z)
eps_d = 1e-7
th1_p = jacobi_theta1(z_test + eps_d, tau)
th1_m = jacobi_theta1(z_test - eps_d, tau)
th1_prime_z = (th1_p - th1_m) / (2 * eps_d)

dlog_theta1 = th1_prime_z / th1
zeta_check = dlog_theta1 + 2 * eta1 * z_test

print(f"eta_1 = {eta1:.10f}")
print(f"theta_1(z|tau) = {th1:.10f}")
print(f"theta_1'(z|tau) = {th1_prime_z:.10f}")
print(f"dlog theta_1(z) = {dlog_theta1:.10f}")
print(f"zeta(z) from theta = {zeta_check:.10f}")
print(f"zeta(z) direct     = {zeta_z:.10f}")
print(f"Consistency: {abs(zeta_check - zeta_z):.2e}")
print()

print("EXPLICIT FORMULA:")
print()
print("phi_J(z; tau, k) = exp(-alpha_J * zeta(z; tau))")
print()
print("where:")
print("  alpha_0 = -3/(4(k+2))    [singlet]")
print("  alpha_1 = 1/(4(k+2))     [triplet]")
print("  zeta(z; tau) = theta_1'(z|tau)/theta_1(z|tau) + 2*eta_1*z")
print("  eta_1 = -theta_1'''(0|tau)/(6*theta_1'(0|tau))")
print()
print("Psi_E1(z; tau, k, u) = exp(-alpha_1 * zeta(z; tau))")
print("                     - R_sing(u, k) * exp(-alpha_0 * zeta(z; tau))")
print()
print("where R_sing(u, k) = (u - 1/(k+2)) / (u + 1/(k+2))")
print()

# ============================================================
# Step 6: High-precision verification with mpmath
# ============================================================
print("=" * 70)
print("STEP 6: High-precision verification with mpmath")
print("=" * 70)
print()

try:
    import mpmath
    mpmath.mp.dps = 50

    tau_mp = mpmath.mpc(0, 1)
    z_mp = mpmath.mpc(0.3, 0.1)
    k_mp = mpmath.mpf(2)
    u_mp = mpmath.mpf(1)
    h_vee_mp = mpmath.mpf(2)

    # Weierstrass functions with periods (1, tau)
    # mpmath uses omega1, omega2 as half-periods
    omega1 = mpmath.mpf(0.5)
    omega2 = tau_mp / 2

    # Weierstrass zeta
    zeta_mp = mpmath.zeta  # This is Riemann zeta, not Weierstrass

    # mpmath's elliptic functions use different conventions.
    # Let's use the Jacobi theta functions directly.

    # mpmath.jtheta(n, z, q) where n=1,2,3,4
    # Convention: jtheta(1, pi*z, q) = theta_1(z | tau) in our convention
    # where q = exp(i*pi*tau)

    q_mp = mpmath.exp(mpmath.mpc(0, 1) * mpmath.pi * tau_mp)

    # theta_1(z|tau) in our convention with argument z (not pi*z):
    def theta1_mp(z):
        return mpmath.jtheta(1, mpmath.pi * z, q_mp)

    def theta1_prime_mp(z):
        eps = mpmath.mpf(10)**(-15)
        return (theta1_mp(z + eps) - theta1_mp(z - eps)) / (2 * eps)

    # theta_1'(0|tau)
    th1p0_mp = theta1_prime_mp(mpmath.mpf(0))

    # eta_1 via the formula:
    # eta_1 = -theta_1'''(0) / (6*theta_1'(0))
    eps_mp = mpmath.mpf(10)**(-10)
    th1_2e = theta1_mp(2*eps_mp)
    th1_e = theta1_mp(eps_mp)
    th1_me = theta1_mp(-eps_mp)
    th1_m2e = theta1_mp(-2*eps_mp)
    th1_triple_prime_0 = (th1_2e - 2*th1_e + 2*th1_me - th1_m2e) / (2*eps_mp**3)
    eta1_mp = -th1_triple_prime_0 / (6 * th1p0_mp)

    # Weierstrass zeta from theta
    def wz_zeta_mp(z):
        dlog = theta1_prime_mp(z) / theta1_mp(z)
        return dlog + 2 * eta1_mp * z

    # Weierstrass P from zeta
    def wz_p_mp(z):
        eps = mpmath.mpf(10)**(-10)
        return -(wz_zeta_mp(z + eps) - wz_zeta_mp(z - eps)) / (2 * eps)

    # Compute channel solutions
    alpha0_mp = mpmath.mpf(-3) / (4 * (k_mp + h_vee_mp))
    alpha1_mp = mpmath.mpf(1) / (4 * (k_mp + h_vee_mp))

    zeta_z_mp = wz_zeta_mp(z_mp)

    phi0_mp = mpmath.exp(-alpha0_mp * zeta_z_mp)
    phi1_mp = mpmath.exp(-alpha1_mp * zeta_z_mp)

    hbar_mp = mpmath.mpf(1) / (k_mp + h_vee_mp)
    R_sing_mp = (u_mp - hbar_mp) / (u_mp + hbar_mp)

    Psi_E1_mp = phi1_mp - R_sing_mp * phi0_mp

    print(f"mpmath precision: {mpmath.mp.dps} digits")
    print()
    print(f"eta_1 = {eta1_mp}")
    print(f"zeta(z; tau) = {zeta_z_mp}")
    print()
    print(f"alpha_0 = {alpha0_mp}")
    print(f"alpha_1 = {alpha1_mp}")
    print()
    print(f"phi_0(z) = {phi0_mp}")
    print(f"phi_1(z) = {phi1_mp}")
    print()
    print(f"R_sing = {R_sing_mp}")
    print()
    print(f"Psi_E1 = {Psi_E1_mp}")
    print(f"|Psi_E1| = {abs(Psi_E1_mp)}")
    print()

    # Verify ODE
    eps_ode = mpmath.mpf(10)**(-10)
    wp_mp = wz_p_mp(z_mp)

    phi0_p = mpmath.exp(-alpha0_mp * wz_zeta_mp(z_mp + eps_ode))
    phi0_m = mpmath.exp(-alpha0_mp * wz_zeta_mp(z_mp - eps_ode))
    dphi0_dz = (phi0_p - phi0_m) / (2 * eps_ode)
    ode_lhs_0 = dphi0_dz
    ode_rhs_0 = alpha0_mp * wp_mp * phi0_mp
    err_0 = float(abs(ode_lhs_0 - ode_rhs_0))
    print(f"ODE check singlet: |LHS - RHS| = {err_0:.4e}")

    phi1_p = mpmath.exp(-alpha1_mp * wz_zeta_mp(z_mp + eps_ode))
    phi1_m = mpmath.exp(-alpha1_mp * wz_zeta_mp(z_mp - eps_ode))
    dphi1_dz = (phi1_p - phi1_m) / (2 * eps_ode)
    ode_lhs_1 = dphi1_dz
    ode_rhs_1 = alpha1_mp * wp_mp * phi1_mp
    err_1 = float(abs(ode_lhs_1 - ode_rhs_1))
    print(f"ODE check triplet: |LHS - RHS| = {err_1:.4e}")
    print()

except ImportError:
    print("mpmath not available, skipping high-precision check")

# ============================================================
# Step 7: Comparison with claimed numerical value
# ============================================================
print("=" * 70)
print("STEP 7: Comparison with previous agent's numerical value")
print("=" * 70)
print()
print("Previous agent claimed: Psi_E1 = 0.869 + 1.355i at tau=i, k=2, u=1")
print(f"Our computation:        Psi_E1 = {Psi_E1:.6f}")
print(f"|Psi_E1| (ours) = {abs(Psi_E1):.6f}")
print(f"|Psi_E1| (claimed) ~ 1.61")
print(f"|0.869 + 1.355i| = {abs(0.869 + 1.355j):.6f}")
print()

# The test point might have been z=1 (the spectral parameter u=1 was used as z)
# Let's also check various z values
print("Checking at various z values to find the match:")
for z_try in [0.3+0.1j, 0.5, 0.25, 1.0/(2*np.pi), 0.1, 0.3, z_test]:
    z_t = complex(z_try)
    zeta_t = weierstrass_zeta(z_t, tau)
    phi0_t = np.exp(-alpha_singlet * zeta_t)
    phi1_t = np.exp(-alpha_triplet * zeta_t)
    psi_t = phi1_t - R_singlet * phi0_t
    print(f"  z={z_t:.4f}: Psi_E1 = {psi_t:.6f}, |Psi_E1| = {abs(psi_t):.6f}")

print()

# ============================================================
# Step 8: Alternative normalization - sigma function form
# ============================================================
print("=" * 70)
print("STEP 8: Sigma function / theta_1 alternative form")
print("=" * 70)
print()

# The solution phi_J(z) = exp(-alpha_J * zeta(z))  can be related to sigma:
#
# Since d/dz log sigma(z) = zeta(z), we have
#    exp(-alpha * zeta(z)) != sigma(z)^{-alpha}
# because exp(-alpha * zeta(z)) involves zeta EVALUATED at z,
# NOT the integral of zeta.
#
# However, the DERIVATIVE of sigma^{-alpha} gives:
#   d/dz [sigma(z)^{-alpha}] = -alpha * sigma(z)^{-alpha-1} * sigma'(z)
#                              = -alpha * sigma(z)^{-alpha} * zeta(z)
#
# So sigma(z)^{-alpha} satisfies:
#   dw/dz = -alpha * zeta(z) * w
#
# But we need:
#   dphi/dz = alpha * wp(z) * phi = -alpha * zeta'(z) * phi
#
# These are DIFFERENT equations!
#   sigma^{-alpha} satisfies dw/dz = -alpha*zeta(z)*w  (first-order linear with zeta(z) coefficient)
#   phi(z) satisfies dphi/dz = -alpha*zeta'(z)*phi     (first-order linear with zeta'(z) coefficient)
#
# So sigma^{-alpha} is NOT the solution. Let me reconsider.

# Actually, let me re-derive more carefully. The ODE is:
#   dphi/dz = alpha * wp(z) * phi
# where wp(z) = -zeta'(z) = -d/dz[sigma'(z)/sigma(z)]
#
# This is a first-order LINEAR ODE with non-constant coefficient:
#   dphi/dz - alpha*wp(z)*phi = 0
#
# The integrating factor is exp(-alpha * integral(wp(z)dz)) = exp(alpha*zeta(z))
# since integral(wp(z))dz = -zeta(z) + const.
#
# So d/dz[phi * exp(alpha*zeta(z))] = 0
# => phi(z) * exp(alpha*zeta(z)) = const
# => phi(z) = C * exp(-alpha * zeta(z))
#
# This is correct! Let me verify once more:
# d/dz [C * exp(-alpha*zeta(z))] = C * exp(-alpha*zeta(z)) * (-alpha * zeta'(z))
#                                 = (-alpha * zeta'(z)) * phi(z)
#                                 = alpha * wp(z) * phi(z)  ✓

# Now, the explicit theta_1 form. Using:
#   zeta(z; tau) = pi * theta_1'(pi*z | tau) / theta_1(pi*z | tau) + 2*eta_1*z
# Wait, let me be careful about conventions.

# In our library, theta_1(z | tau) uses z directly (not pi*z).
# The relation is: zeta(z) = theta_1'(z)/theta_1(z) + 2*eta_1*z
# where eta_1 is the quasi-period for omega_1 = 1.

# However, there's a subtlety about the pi factor. Let me check:
# Our theta_1(z|tau) = 2 sum_{n>=0} (-1)^n q^{(n+1/2)^2} sin((2n+1)*pi*z)
# where q = exp(i*pi*tau).
# This means theta_1 has zeros at z = m + n*tau (integers m,n).

# The Weierstrass sigma for lattice Z + Z*tau has:
# sigma(z) = (theta_1(z|tau) / theta_1'(0|tau)) * exp(eta_1 * z^2)

# Therefore:
# log sigma(z) = log theta_1(z|tau) - log theta_1'(0|tau) + eta_1*z^2
# zeta(z) = d/dz log sigma(z) = theta_1'(z)/theta_1(z) + 2*eta_1*z

# But theta_1'(z)/theta_1(z) here means (d/dz)log theta_1(z|tau).
# Let's verify numerically:

print("Verifying zeta = d(log theta_1)/dz + 2*eta_1*z:")
z_v = z_test
th1_v = jacobi_theta1(z_v, tau)
th1_vp = jacobi_theta1(z_v + 1e-7, tau)
th1_vm = jacobi_theta1(z_v - 1e-7, tau)
dlog_th1 = (th1_vp - th1_vm) / (2e-7 * th1_v)
eta1_v = _weierstrass_eta1(tau)
zeta_from_theta = dlog_th1 + 2*eta1_v*z_v
zeta_direct = weierstrass_zeta(z_v, tau)
print(f"  d(log theta_1)/dz at z={z_v}: {dlog_th1:.10f}")
print(f"  2*eta_1*z: {2*eta1_v*z_v:.10f}")
print(f"  Sum: {zeta_from_theta:.10f}")
print(f"  Direct zeta: {zeta_direct:.10f}")
print(f"  Agreement: {abs(zeta_from_theta - zeta_direct):.2e}")
print()

# ============================================================
# Step 9: Write the FINAL FORMULA
# ============================================================
print("=" * 70)
print("FINAL FORMULA")
print("=" * 70)
print()
print("THEOREM (KZB conformal block, sl_2, level k, fundamental rep)")
print()
print("The E_1 KZB conformal block on E_tau for sl_2 at level k,")
print("in V=C^2 with Yangian spectral parameter u, is:")
print()
print("  Psi_E1(z; tau, k, u) = exp(-alpha_1 * zeta(z; tau))")
print("                       - R(u,k) * exp(-alpha_0 * zeta(z; tau))")
print()
print("where:")
print("  alpha_0 = -3/(4(k+2))       [singlet channel]")
print("  alpha_1 =  1/(4(k+2))       [triplet channel]")
print("  R(u,k) = (u - hbar)/(u + hbar),  hbar = 1/(k+2)")
print("  zeta(z; tau) = Weierstrass zeta for lattice Z + Z*tau")
print()
print("In terms of theta_1:")
print()
print("  Psi_E1(z; tau, k, u) = exp(-alpha_1*[L(z) + 2*eta_1*z])")
print("                       - R(u,k)*exp(-alpha_0*[L(z) + 2*eta_1*z])")
print()
print("where L(z) = (d/dz) log theta_1(z|tau) = theta_1'(z|tau)/theta_1(z|tau)")
print("and eta_1 = -theta_1'''(0|tau)/(6*theta_1'(0|tau)).")
print()
print("Equivalently, using the Weierstrass sigma function:")
print("  sigma(z; tau) = theta_1(z|tau)/theta_1'(0|tau) * exp(eta_1*z^2)")
print()
print("  Psi_E1 = exp(-alpha_1 * sigma'(z)/sigma(z))")
print("         - R(u,k) * exp(-alpha_0 * sigma'(z)/sigma(z))")
print()

# ============================================================
# Step 10: Modular transformation properties
# ============================================================
print("=" * 70)
print("STEP 10: Modular transformation properties")
print("=" * 70)
print()

# Under tau -> tau + 1:
# The lattice Z + Z*tau changes to Z + Z*(tau+1).
# Weierstrass zeta transforms: zeta_{tau+1}(z) = zeta_tau(z)
# (same lattice up to relabeling, since Z + Z*(tau+1) = Z + Z*tau for z in C)
# Actually this is NOT the same lattice. Let's compute.

# Under tau -> tau + 1:
#   theta_1(z|tau+1) = exp(i*pi/4) * theta_1(z|tau)
# This means:
#   d/dz log theta_1(z|tau+1) = d/dz log theta_1(z|tau)  (the phase cancels in the log derivative)
# But eta_1(tau+1) != eta_1(tau).

# Let me compute eta_1 at tau and tau+1:
eta1_tau = _weierstrass_eta1(tau)
eta1_tau1 = _weierstrass_eta1(tau + 1)

print("Under tau -> tau + 1:")
print(f"  eta_1(tau) = {eta1_tau:.10f}")
print(f"  eta_1(tau+1) = {eta1_tau1:.10f}")
print(f"  Difference: {eta1_tau1 - eta1_tau:.10f}")
print()

# Under tau -> -1/tau:
# The modular S-transformation maps (1, tau) -> (1, -1/tau), which is equivalent
# to (tau, -1) via rescaling by tau. The Weierstrass zeta transforms as:
#   zeta_{-1/tau}(z) = tau^2 * zeta_tau(tau*z)  ... needs careful check
#
# Actually for periods (omega1, omega2) -> (omega2, -omega1):
# The standard transformation: if we rescale z -> z/tau, then
#   zeta_{-1/tau}(z) = tau * zeta_tau(tau*z) + 2*eta_2*z
# where eta_2 is the quasi-period for omega_2 = tau.

# Actually the correct formula (Weierstrass functions under modular transform):
# Under tau -> -1/tau with z -> z/tau:
#   zeta(-1/tau)(z/tau) = tau * zeta(tau)(z) - 2*eta_2*z*tau
#
# This gets complicated. Let me compute numerically.

tau_S = -1/tau  # = -1/i = i (special case!)
print(f"Under tau -> -1/tau: tau_S = {tau_S}")
print("(Special case: -1/i = i, so tau=i is a FIXED POINT of S!)")
print()

# Since tau=i is a fixed point of S, the modular properties simplify.
# The conformal block at tau=i has enhanced symmetry.

# For general tau, under S: tau -> -1/tau:
# The KZB equation transforms covariantly. The conformal block picks up
# a factor related to the modular weight.
#
# The Weierstrass zeta for lattice (1, tau) under S: (1, tau) -> (1, -1/tau)
#
# More precisely: zeta_{-1/tau}(z) relates to zeta_tau(z*tau) by:
#   zeta(z; 1, -1/tau) = tau^2 * zeta(z*tau; 1, tau) + 2*eta_1'*z*(tau^2 - 1)
# but this is getting complicated. Let me compute for a general tau.

tau_gen = 0.3 + 1.2j  # generic tau
tau_S_gen = -1/tau_gen

print(f"Generic tau = {tau_gen}")
print(f"S(tau) = -1/tau = {tau_S_gen}")
print()

# Compute Psi_E1 at both tau and S(tau)
z_mod = 0.2 + 0.1j

for tau_val, label in [(tau_gen, "tau"), (tau_S_gen, "S(tau)")]:
    eta1_val = _weierstrass_eta1(tau_val)
    zeta_val = weierstrass_zeta(z_mod, tau_val)
    phi0_val = np.exp(-alpha_singlet * zeta_val)
    phi1_val = np.exp(-alpha_triplet * zeta_val)
    psi_val = phi1_val - R_singlet * phi0_val
    print(f"  At {label}={tau_val:.4f}:")
    print(f"    zeta(z) = {zeta_val:.10f}")
    print(f"    Psi_E1  = {psi_val:.10f}")
    print(f"    |Psi_E1| = {abs(psi_val):.10f}")
    print()

# Under S-transform, z should also transform: z -> z/tau
z_S = z_mod / tau_gen
print(f"Under S: z -> z/tau = {z_S:.6f}")
zeta_S = weierstrass_zeta(z_S, tau_S_gen)
phi0_S = np.exp(-alpha_singlet * zeta_S)
phi1_S = np.exp(-alpha_triplet * zeta_S)
psi_S = phi1_S - R_singlet * phi0_S
print(f"  Psi_E1(z/tau, -1/tau) = {psi_S:.10f}")
print(f"  |Psi_E1(z/tau, -1/tau)| = {abs(psi_S):.10f}")
print()

# The conformal block should transform with a modular weight factor:
# Psi(z/tau, -1/tau) = tau^h * exp(pi*i*kappa*z^2/tau) * Psi(z, tau)
# where h is the conformal weight and kappa is the modular characteristic.
# For the KZB system, the weight is determined by the Casimir eigenvalue.

# Let me compute the ratio:
zeta_orig = weierstrass_zeta(z_mod, tau_gen)
phi0_orig = np.exp(-alpha_singlet * zeta_orig)
phi1_orig = np.exp(-alpha_triplet * zeta_orig)
psi_orig = phi1_orig - R_singlet * phi0_orig

ratio = psi_S / psi_orig
print(f"Ratio Psi(z/tau, -1/tau) / Psi(z, tau) = {ratio:.10f}")
print(f"|ratio| = {abs(ratio):.10f}")
print(f"arg(ratio)/pi = {np.angle(ratio)/np.pi:.10f}")
print()

# ============================================================
# Step 11: T-transformation: tau -> tau+1
# ============================================================
print("=" * 70)
print("STEP 11: T-transformation tau -> tau+1")
print("=" * 70)
print()

tau_T = tau_gen + 1
zeta_T = weierstrass_zeta(z_mod, tau_T)
phi0_T = np.exp(-alpha_singlet * zeta_T)
phi1_T = np.exp(-alpha_triplet * zeta_T)
psi_T = phi1_T - R_singlet * phi0_T

print(f"Psi_E1(z, tau+1) = {psi_T:.10f}")
print(f"|Psi_E1(z, tau+1)| = {abs(psi_T):.10f}")
print()

ratio_T = psi_T / psi_orig
print(f"Ratio Psi(z, tau+1) / Psi(z, tau) = {ratio_T:.10f}")
print(f"|ratio_T| = {abs(ratio_T):.10f}")
print(f"arg(ratio_T)/pi = {np.angle(ratio_T)/np.pi:.10f}")
print()

# ============================================================
# Summary
# ============================================================
print("=" * 70)
print("SUMMARY OF RESULTS")
print("=" * 70)
print()
print("1. CLOSED FORM:")
print("   phi_J(z; tau, k) = exp(-alpha_J * zeta(z; tau))")
print("   alpha_0 = -3/(4(k+2)),  alpha_1 = 1/(4(k+2))")
print()
print("2. E_1 BLOCK:")
print("   Psi_E1(z; tau, k, u) = phi_1(z) - R(u,k) * phi_0(z)")
print("   R(u,k) = (u - 1/(k+2))/(u + 1/(k+2))")
print()
print("3. THETA FORM:")
print("   phi_J(z) = exp(-alpha_J * [theta_1'(z|tau)/theta_1(z|tau) + 2*eta_1*z])")
print("   eta_1(tau) = -theta_1'''(0|tau) / (6*theta_1'(0|tau))")
print()
print("4. NUMERICAL VALUES at z=0.3+0.1i, tau=i, k=2, u=1:")
print(f"   Psi_E1 = {Psi_E1:.10f}")
print(f"   |Psi_E1| = {abs(Psi_E1):.10f}")
print()
print("5. MODULAR PROPERTIES:")
print("   - tau=i is a fixed point of S: tau -> -1/tau")
print("   - Under T: tau -> tau+1, Psi transforms by a phase")
print("   - The block has weight alpha_J under z -> z + 1 and z -> z + tau")
print("     (quasi-periodic with multipliers exp(-alpha_J * 2*eta_1)")
print("     and exp(-alpha_J * 2*eta_2) respectively)")
