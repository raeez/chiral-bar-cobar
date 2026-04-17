# True Formula Census (C1-C31)

Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).

The 5 most-violated entries (C3, C4, C9, C14, C19) are kept inline in CLAUDE.md; all 31 are listed here for reference.

**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).

**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).

**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).

**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.

**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).

**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).

**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).

**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).

**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).

**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).

**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).

**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.

**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).

**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).

**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).

**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.

**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).

**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).

**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).

**C20. Bershadsky-Polyakov Koszul conductor.** `K_BP = c(k) + c(-k-6) = 196`. Self-dual level k=-3. Wrong: K_BP=76 (corrected in Wave 7); K_BP=2 (AP140, confusing with ghost constant C_{(2,1)}=2).

**C21. Igusa cusp form / BKM kappa.** `wt(Phi_10) = 10 = 2*kappa_BKM(K3xE)`, so `kappa_BKM(K3xE) = 5`. Phi_10 = Delta_5^2. Wrong: kappa_BKM = 10 (identifies kappa with full weight); kappa_BKM = 2.

**C22. Dedekind eta.** `eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)`. Prefactor q^{1/24} ESSENTIAL for modular weight 1/2 transformation. Wrong: dropping q^{1/24}; q^{1/12} prefactor.

**C23. Bicoloured partitions.** `1/eta^2 = q^{-1/12} sum p_{-2}(n) q^n`, coefficients `(1, 2, 5, 10, 20, ...)` (OEIS A002513). Wrong: triangular (1,3,6,10,...) (AP135); ordinary partitions (1,1,2,3,5,...).

**C24. Cauchy integral normalization.** `[z^{n-1}] f(z) = (1/(2*pi*i)) * contour_integral f(z) dz/z^n`. Wrong: 1/(2*pi) (missing i gives zero for real integrands, AP120). Sanity: F_1 = kappa/24.

**C25. MC equation.** `d*Theta + (1/2)[Theta, Theta] = 0`. QME: `hbar*Delta*S + (1/2){S,S} = 0`. Wrong: drop the 1/2 (except odd parity); sign flip.

**C26. G/L/C/M classification.** G (r=2, Heis), L (r=3, aff KM), C (r=4, betagamma), M (r=inf, Vir/W_N). Shadow depth != Koszulness.

**C27. Chiral Hochschild of Vir.** `ChirHoch^*(Vir_c)` concentrated in degrees {0,1,2}; polynomial Hilbert series. This is AMPLITUDE (topological), NOT virtual dimension (arithmetic) (AP134). NOT C[Theta] (AP94). NOT Gelfand-Fuchs (GF infinite, AP95).

**C28. Arnold form vs KZ connection.** KZ: `nabla_KZ = d + sum r_{ij} dz_{ij}` with `dz_{ij}`, NOT `d log z_{ij}`. Arnold form `omega_{ij} = d log(z_i - z_j)` is a bar-construction coefficient, NOT the connection form (AP117). For affine KM: `r_{ij}(z) = k*Omega_{ij}/z`.

**C29. Genus-1 period matrix collapse.** `(Im Omega)^{-1}` is a gxg MATRIX at g>=2; degenerates to scalar 1/Im(tau) at g=1. Write formulas in full matrix form; verify at g=2 (AP118).

**C30. Delta discriminant.** `Delta = 8*kappa*S_4`. Finite tower iff Delta=0; for kappa!=0 iff S_4=0. LINEAR in kappa (NOT quadratic, AP21). Heis: S_4=0, Delta=0, class G. Vir: S_4!=0, Delta!=0, class M.

**C31. Bershadsky-Polyakov complementarity conductor.** `kappa(BP) + kappa(BP^!) = 98/3` (NOT 1/3). `varrho_BP = 1/6`. Checks: K_BP = c(k) + c(-k-6) = 196 (cross-check C20); at self-dual level k=-3, kappa(BP) = 49/3. Wrong: kappa(BP)+kappa(BP^!)=1/3 (off by factor 98); varrho_BP=1/2 (confusing with rank-1 value).
