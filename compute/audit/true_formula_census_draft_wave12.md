## The True Formula Census

The following entries enumerate canonical formulas that must never be written from memory. Every entry provides (1) the canonical form, (2) two independent sanity checks at boundary values, (3) blacklisted wrong variants with the cognitive error that produces them, and (4) the diagnostic condition under which Opus writes the wrong form. Before writing any formula in this list, stop and verify against this census; do not trust memory or surface pattern-matching.

### C1. Heisenberg kappa

**Canonical form.** For the rank-one Heisenberg VOA $\cH_k$ at level $k$:
$$\kappa(\cH_k) \;=\; k.$$
**Sanity check 1 ($k=0$).** $\kappa(\cH_0)=0$; Heisenberg at level zero is the commutative polynomial algebra on one generator, which has vanishing kappa. Consistent.
**Sanity check 2 ($k=1$).** $\kappa(\cH_1)=1$; matches $c_{\mathrm{Heis}}(1)=1$ and coincides with the rank-one case where $\kappa=c$ accidentally.
**Wrong variants.** (a) $\kappa(\cH_k)=k/2$: produced by pattern-matching to $\kappa^{\mathrm{Vir}}=c/2$. (b) $\kappa(\cH_k)=k\cdot\dim/(2h^\vee)$: produced by copying the affine KM formula and setting $h^\vee=1$.
**Diagnostic.** Writing $\kappa^{\mathrm{Heis}}$ from memory inside a formula where a $1/2$ appears nearby, or inside a passage that has just stated the Virasoro or KM case.

### C2. Virasoro kappa

**Canonical form.** For Virasoro at central charge $c$:
$$\kappa(\mathrm{Vir}_c) \;=\; \tfrac{c}{2}.$$
This is the UNIQUE family in the standard landscape for which $\kappa=c/2$.
**Sanity check 1 ($c=0$).** $\kappa=0$: Virasoro at $c=0$ is abelian as a chiral algebra (no central extension), consistent with vanishing kappa.
**Sanity check 2 ($c=13$).** $\kappa=13/2$, and $\kappa+\kappa'=13$ under Feigin-Frenkel $c\leftrightarrow 26-c$: self-dual point at $c=13$.
**Wrong variants.** (a) $\kappa^{\mathrm{Vir}}=c$: produced by dropping the $1/2$ during a copy-paste. (b) $\kappa^{\mathrm{Vir}}=c/24$: produced by confusing with the Eisenberg modular anomaly $c/24$.
**Diagnostic.** Writing Virasoro kappa next to a modular anomaly expression that involves $c/24$, or writing it during a passage about conformal anomaly.

### C3. Affine Kac-Moody kappa

**Canonical form.** For the affine Kac-Moody VOA $V_k(\fg)$ at level $k$, with dual Coxeter number $h^\vee$:
$$\kappa(V_k(\fg)) \;=\; \frac{\dim(\fg)\,(k+h^\vee)}{2h^\vee}.$$
**Sanity check 1 ($k=0$).** $\kappa=\dim(\fg)/2$. This is NOT zero. $V_0(\fg)$ is the SELF-DUAL level for the Feigin-Frenkel pairing; $\kappa+\kappa'$ vanishes here only after adding the dual.
**Sanity check 2 ($k=-h^\vee$, critical level).** $\kappa=0$. At critical level the Sugawara construction degenerates, the leading arity-$2$ shadow vanishes, and the bar complex is uncurved; this does not by itself force the full shadow tower to collapse.
**Wrong variants.** (a) $\kappa=\dim(\fg)\,k/(2h^\vee)$: produced by forgetting the $+h^\vee$ shift (Sugawara shift dropped). (b) $\kappa=k/2$: produced by copying the Heisenberg formula. (c) $\kappa=c/2$ where $c=k\dim(\fg)/(k+h^\vee)$: produced by copying the Virasoro formula; these are DIFFERENT functions of $k$ except at rank one.
**Diagnostic.** Writing kappa for affine KM immediately after writing it for Heisenberg or Virasoro; or from memory during a Sugawara passage where the shift is already implicit elsewhere.

### C4. Principal W_N kappa

**Canonical form.** For the principal $\cW_N$ algebra $\cW^k(\fsl_N, f_{\mathrm{prin}})$:
$$\kappa(\cW_N) \;=\; c\cdot(H_N-1), \qquad H_N \;=\; \sum_{j=1}^{N}\frac{1}{j}.$$
**Sanity check 1 ($N=2$).** $H_2=3/2$, so $H_2-1=1/2$, giving $\kappa(\cW_2)=c/2=\kappa^{\mathrm{Vir}}$. Consistent: $\cW_2=\mathrm{Vir}$.
**Sanity check 2 ($N=3$).** $H_3=1+1/2+1/3=11/6$, so $H_3-1=5/6$, giving $\kappa(\cW_3)=5c/6$. At the self-dual level this produces the census entry $\kappa+\kappa'=250/3$ recorded in the landscape census.
**Wrong variants.** (a) $\kappa=c\cdot H_{N-1}$: the off-by-one (AP136). At $N=2$, $H_{N-1}=H_1=1$, giving $\kappa=c$, wrong by factor 2. (b) $\kappa=c\cdot H_N - 1$: parenthesization error. At $N=2$, gives $3c/2-1$, wrong. (c) $\kappa=(c/2)\cdot H_N$: copying Virasoro and multiplying by harmonic number.
**Diagnostic.** Writing $\kappa^{\cW_N}$ from memory without substituting $N=2$ and checking that the result reduces to $c/2$.

### C5. Fermionic bc central charge

**Canonical form.** For the fermionic bc-system of conformal weight $(\lambda, 1-\lambda)$:
$$c_{bc}(\lambda) \;=\; 1 - 3(2\lambda-1)^2.$$
**Sanity check 1 ($\lambda=1/2$).** $c_{bc}(1/2) = 1-0 = 1$: the single complex fermion (free Dirac fermion), consistent with the standard $c=1$ of a free Majorana pair.
**Sanity check 2 ($\lambda=2$).** $c_{bc}(2) = 1-3\cdot 9 = -26$: the reparametrization ghosts, consistent with bosonic string critical dimension.
**Wrong variants.** (a) $c_{bc}(\lambda) = -1+3(2\lambda-1)^2$: sign flip (copies the bosonic partner with wrong sign). (b) $c_{bc}(\lambda) = 1-3(2\lambda+1)^2$: sign inside parenthesis; at $\lambda=1/2$ gives $1-12=-11$, wrong.
**Diagnostic.** Writing $c_{bc}$ inside a passage that has just discussed the bosonic $\beta\gamma$ system; the parallelism triggers miscopy.

### C6. Bosonic βγ central charge

**Canonical form.** For the bosonic $\beta\gamma$-system of conformal weight $(\lambda, 1-\lambda)$:
$$c_{\beta\gamma}(\lambda) \;=\; 2(6\lambda^2 - 6\lambda + 1).$$
**Sanity check 1 ($\lambda=1/2$).** $c_{\beta\gamma}(1/2) = 2(6/4-3+1) = 2(-1/2)=-1$: single complex boson with weight $(1/2,1/2)$, consistent with the $c=-1$ symplectic boson.
**Sanity check 2 ($\lambda=2$).** $c_{\beta\gamma}(2) = 2(24-12+1) = 26$: the superstring matter ghost, consistent with $c_{\beta\gamma}+c_{bc} = 26-26 = 0$ (AP137 total-zero check).
**Wrong variants.** (a) $c_{\beta\gamma}(\lambda) = 12\lambda^2-12\lambda+2$: correct value but a survey paper had $3(2\lambda-1)^2-1 = 12\lambda^2-12\lambda+2$; both algebraically equal; but $2(6\lambda^2-6\lambda+1)$ is the canonical factored form. Prefer the canonical form. (b) $c_{\beta\gamma}(\lambda)=2(6\lambda^2+6\lambda+1)$: wrong middle sign.
**Diagnostic.** Writing $c_{\beta\gamma}$ without the companion $c_{bc}$ sanity check $c_{\beta\gamma}+c_{bc}=0$.

### C7. bc/βγ complementarity

**Canonical form.** The bosonic and fermionic partners with the same weight $\lambda$ satisfy
$$c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) \;=\; 0.$$
**Sanity check 1 ($\lambda=1$).** $c_{\beta\gamma}(1)=2$, $c_{bc}(1)=-2$. Sum zero.
**Sanity check 2 ($\lambda=2$).** $c_{\beta\gamma}(2)=26$, $c_{bc}(2)=-26$. Sum zero; the string ghost cancellation.
**Wrong variants.** (a) $c_{\beta\gamma}+c_{bc}=c$: confusing the partner cancellation with the Koszul conductor. (b) $c_{\beta\gamma}-c_{bc}=0$: sign error, implying $c_{\beta\gamma}=c_{bc}$.
**Diagnostic.** Writing the complementarity without a numerical sanity check.

### C8. Virasoro self-dual point

**Canonical form.** Under the Feigin-Frenkel involution $c\mapsto 26-c$:
$$\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c}) \;=\; \frac{c}{2}+\frac{26-c}{2} \;=\; 13.$$
The self-dual point is $c=13$ (NOT $c=26$, NOT $c=0$).
**Sanity check 1 ($c=13$).** $\kappa=13/2$, and the dual is also at $c'=13$: self-duality.
**Sanity check 2 ($c=25$).** $\kappa=25/2$, dual at $c'=1$ has $\kappa'=1/2$; sum $=13$.
**Wrong variants.** (a) "Virasoro self-dual at $c=26$" (confusing $c+c'=26$ with the self-dual point). (b) "Virasoro self-dual at $c=0$" (confusing with trivial representation).
**Diagnostic.** Writing "self-dual" without specifying the duality (c vs. $\kappa$) and the fixed point.

### C9. Affine Kac-Moody classical r-matrix

**Canonical form.** For affine $\widehat{\fg}_k$ at level $k$, with Casimir $\Omega=\sum_a J^a\otimes J_a$:
$$r^{\mathrm{KM}}(z) \;=\; k\cdot\frac{\Omega}{z}.$$
The level prefix $k$ is MANDATORY; it survives $d\log$ absorption (AP126, AP141).
**Sanity check 1 ($k=0$).** $r^{\mathrm{KM}}(z)=0$. At level zero the chiral algebra is cocommutative; r-matrix vanishes. (AP141 enforcement: after writing ANY r-matrix, verify $k=0\Rightarrow r=0$.)
**Sanity check 2 (averaging).** $\mathrm{av}(k\Omega/z) = (k+h^\vee)\dim(\fg)/(2h^\vee) = \kappa(V_k(\fg))$. At $k=-h^\vee$ this gives $0$: critical level, consistent with $\kappa=0$.
**Wrong variants.** (a) $r^{\mathrm{KM}}(z)=\Omega/z$: bare, no level prefix (AP126 — THE MOST VIOLATED AP; 42+ instances). (b) $r^{\mathrm{KM}}(z)=(k+h^\vee)\Omega/z$: absorbing the Sugawara shift into the r-matrix. (c) $r^{\mathrm{KM}}(z)=k\Omega/z^2$: double pole (confusing with Heisenberg double pole in the OPE).
**Diagnostic.** Writing any affine r-matrix from memory; parallel-writing with a Heisenberg r-matrix that uses $k/z$ and dropping the $\Omega$; writing inside a Gaudin or KZ passage where the level is already "understood."

### C10. Heisenberg classical r-matrix

**Canonical form.** For the rank-one Heisenberg at level $k$:
$$r^{\mathrm{Heis}}(z) \;=\; \frac{k}{z}.$$
This is the $\fg=\fu(1)$ specialization of the affine KM r-matrix: $\dim(\fg)=1$, $h^\vee=0$ (degenerate), and $\Omega=1\otimes 1$.
**Sanity check 1 ($k=0$).** $r=0$. Vanishes as required.
**Sanity check 2 (averaging).** $\mathrm{av}(k/z)=k=\kappa(\cH_k)$; matches C1.
**Wrong variants.** (a) $r^{\mathrm{Heis}}(z)=k/z^2$: double-pole (confusing with the OPE pole order; the r-matrix absorbs one pole via $d\log$). (b) $r^{\mathrm{Heis}}(z)=1/z$: level stripped (AP126).
**Diagnostic.** Writing the Heisenberg r-matrix next to the OPE $J(z)J(w)\sim k/(z-w)^2$ and copying the double pole.

### C11. Virasoro classical r-matrix

**Canonical form.** For Virasoro at central charge $c$, with stress tensor $T$:
$$r^{\mathrm{Vir}}(z) \;=\; \frac{c/2}{z^3} + \frac{2T}{z}.$$
Pole structure: CUBIC (order 3) plus simple, NOT quartic.
**Sanity check 1 (OPE absorption).** The OPE $T(z)T(w)\sim (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + \partial T(w)/(z-w)$ has a quartic pole; the $d\log$ absorption rule (AP19) gives r-matrix poles = OPE poles $-1$, yielding cubic.
**Sanity check 2 ($c=0$).** $r^{\mathrm{Vir}}(z) = 2T/z$; only the stress tensor survives, consistent with the trivial central extension.
**Wrong variants.** (a) $r^{\mathrm{Vir}}(z)=(c/2)/z^4 + \ldots$: quartic pole, forgetting $d\log$ absorption (AP19/AP21). (b) $r^{\mathrm{Vir}}(z)=c/z^3$: dropping the $1/2$ and the $2T/z$ term. (c) Using $\lambda$-bracket form $\{T_\lambda T\}=(c/12)\lambda^3$ in an OPE passage (cross-volume convention confusion AP46).
**Diagnostic.** Writing the Virasoro r-matrix while looking at the OPE formula; the quartic pole of the OPE contaminates the r-matrix writing.

### C12. r-matrix / OPE pole absorption

**Canonical form.** For any chiral algebra, the classical r-matrix pole order is exactly one less than the OPE pole order:
$$\text{pole}_r \;=\; \text{pole}_{\mathrm{OPE}} - 1.$$
This is because the r-matrix is obtained by integrating the OPE against $d\log(z-w) = dz/(z-w)$, which absorbs one pole.
**Sanity check 1 (Heisenberg).** OPE $\sim k/z^2$ (double pole) $\Rightarrow$ r-matrix $\sim k/z$ (simple pole). Consistent with C10.
**Sanity check 2 (Virasoro).** OPE $\sim (c/2)/z^4$ (quartic pole) $\Rightarrow$ r-matrix $\sim (c/2)/z^3$ (cubic pole). Consistent with C11.
**Wrong variants.** (a) "r-matrix has the same pole structure as the OPE": forgetting $d\log$ absorption. (b) "r-matrix has pole $p+1$ where OPE has pole $p$": sign error.
**Diagnostic.** Writing r-matrix pole orders in a passage that discusses OPEs without explicit $d\log$ notation.

### C13. Averaging map identity

**Canonical form.** The coinvariant projection $\mathrm{av}: \fg^{E_1}\to \fg^{\mathrm{mod}}$ at arity 2 satisfies
$$\mathrm{av}(r(z)) \;=\; \kappa(A)$$
where $\kappa(A)$ is the family-specific kappa from C1-C4.
**Sanity check 1 (Heisenberg).** $\mathrm{av}(k/z)=k=\kappa(\cH_k)$. Direct.
**Sanity check 2 (affine KM).** $\mathrm{av}(k\Omega/z)=(k+h^\vee)\dim(\fg)/(2h^\vee)=\kappa(V_k(\fg))$. The Sugawara shift is ALREADY ENCODED in the averaging projection; no extra shift is required. At $k=-h^\vee$ both sides vanish.
**Wrong variants.** (a) $\mathrm{av}(r(z))=\kappa(A)-\dim(\fg)/2$: subtracting a spurious constant; the shift is already inside $\kappa$. (b) $\mathrm{av}(r(z))=k$ for affine KM: this is the bare level, not $\kappa$; forgets the trace over $\Omega$.
**Diagnostic.** Writing the averaging identity while switching between Heisenberg and affine KM in the same passage; the reader mixes up the scalar identity with the matrix trace.

### C14. Bar complex uses augmentation ideal

**Canonical form.** For an augmented (possibly non-unital) associative algebra $A$ with augmentation $\varepsilon:A\to k$:
$$B(A) \;=\; T^c\bigl(s^{-1}\bar A\bigr), \qquad \bar A \;=\; \ker(\varepsilon).$$
The augmentation ideal $\bar A$, NOT the full algebra $A$. Deconcatenation coproduct; desuspension $s^{-1}$; tensor coalgebra $T^c$.
**Sanity check 1 (unit absent).** The bar complex excludes the identity: $B(A)^1 = s^{-1}\bar A$ has no copy of $1\in A$. Writing $T^c(s^{-1}A)$ incorrectly includes the unit and breaks exactness at the vacuum.
**Sanity check 2 (abelian case).** For $A=k[x]/(x^2)$ with $\bar A=(x)$, $B(A)=T^c(s^{-1}\langle x\rangle)$ is the Koszul dual of polynomial: one generator in degree $-1$. Matches $H^*(B(k[x]/(x^2))) = k[y]$, $|y|=1$.
**Wrong variants.** (a) $B(A) = T^c(s^{-1}A)$: uses full $A$ (AP132). (b) $B(A) = T^c(sA)$: wrong suspension direction (AP22). (c) $B(A) = T(s^{-1}\bar A)$: uses tensor ALGEBRA, not coalgebra, losing the deconcatenation.
**Diagnostic.** Writing the bar complex from memory without explicitly inserting $\bar A$ and $s^{-1}$.

### C15. Desuspension grading

**Canonical form.** The desuspension operator $s^{-1}$ LOWERS cohomological degree by 1:
$$|s^{-1} v| \;=\; |v| - 1.$$
Mnemonic: bar = down = desuspension = $s^{-1}$.
**Sanity check 1 (generator).** If $v\in A$ sits in degree $0$, then $s^{-1}v$ sits in degree $-1$; bar cohomology of an ordinary algebra is concentrated in non-positive degrees (before regrading).
**Sanity check 2 (Koszul sign).** The bar differential $d_B(s^{-1}a\otimes s^{-1}b) = -(-1)^{|a|}s^{-1}(ab)$; the sign comes from moving $s^{-1}$ past $a$, consistent with $|s^{-1}|=-1$.
**Wrong variants.** (a) $|s^{-1}v|=|v|+1$: sign error; writing desuspension as suspension. (b) $|s v|=|v|-1$: reversing the suspension convention.
**Diagnostic.** Writing degree shifts for bar constructions while the adjacent passage uses homological (not cohomological) grading; always state "cohomological" explicitly.

### C16. E_8 fundamental representation dimensions

**Canonical form.** The eight fundamental representations of $E_8$ have dimensions
$$\{248,\; 3875,\; 30380,\; 147250,\; 2450240,\; 6696000,\; 146325270,\; 6899079264\}$$
(listed in order $\omega_1,\ldots,\omega_8$ with $\omega_1$ the adjoint). For $E_8$ uniquely among simple Lie algebras, the adjoint IS the first fundamental ($\dim=248$).
**Sanity check 1 (adjoint = fundamental).** $\dim\omega_1=248=\dim\fg$: consistent with the fact that $E_8$ has no smaller nontrivial representation than its adjoint.
**Sanity check 2 (total).** Sum of fundamentals = $7056003287$; matches the independent computation in `compute/lib/bc_exceptional_categorical_zeta_engine.py`.
**Wrong variants.** (a) Writing $779247$ as a fundamental dimension (Wave 10-8 error; this number is not a fundamental of $E_8$). (b) Writing $3875$ as the adjoint (confusing $\omega_2$ with $\omega_1$). (c) Writing $2450$ or $245024$ (truncation of $2450240$).
**Diagnostic.** Writing $E_8$ dimensions from memory instead of copying from `FUNDAMENTAL_DIMS['E8']` in `bc_exceptional_categorical_zeta_engine.py`.

### C17. W_N conformal weight range

**Canonical form.** The principal $\cW_N$ algebra has generators $W^{(s)}$ at conformal weights
$$s \;\in\; \{2,3,\ldots,N\}.$$
Exactly $N-1$ generators; highest weight $N$, NOT $N+1$.
**Sanity check 1 ($N=2$).** $\cW_2$ has generators at $\{2\}$: the stress tensor $T$ only; this is Virasoro. Consistent.
**Sanity check 2 ($N=3$).** $\cW_3$ has generators at $\{2,3\}$: stress tensor $T$ and spin-3 primary $W$; matches Zamolodchikov's original $\cW_3$.
**Wrong variants.** (a) Weights $\{2,3,\ldots,N+1\}$ (Wave 11-2 error): extra weight-$(N+1)$ field that does not exist. At $N=2$ this gives $\{2,3\}$, wrong. (b) Weights $\{1,2,\ldots,N\}$: includes a weight-1 field (absent in the principal DS reduction). (c) Weights $\{2,4,6,\ldots,2N\}$: confuses with non-principal or even-spin truncation.
**Diagnostic.** Writing the $\cW_N$ weight range while the passage has just discussed affine currents (weight 1) or dimensions.

### C18. Koszul complementarity per family

**Canonical form.** The Koszul conductor $K(A) = \kappa(A)+\kappa(A^!)$ takes family-specific values:
$$K(A) \;=\;
\begin{cases}
0 & \text{Kac-Moody, Heisenberg, lattice, free field};\\
13 & \text{Virasoro};\\
250/3 & \cW_3;\\
K_N\cdot(H_N-1) & \cW_N \text{ (family-specific }K_N\text{)};\\
196 & \text{Bershadsky-Polyakov}.
\end{cases}$$
**Sanity check 1 (Virasoro).** $c+(26-c)=26$, so $\kappa+\kappa'=13$. Matches C8.
**Sanity check 2 (affine KM).** $\kappa+\kappa'=0$ because the Feigin-Frenkel pairing maps $k\mapsto -k-2h^\vee$ and $(k+h^\vee)+(-k-2h^\vee+h^\vee)=0$. Consistent with KM line of the table.
**Wrong variants.** (a) Universal $\kappa+\kappa'=0$ (AP24): wrong for Virasoro and beyond. (b) Universal $\kappa+\kappa'=13$: wrong for KM. (c) $K_{\mathrm{BP}}=2$: confusing the global Koszul conductor with a local ghost constant $C_{(2,1)}=2$ (AP140).
**Diagnostic.** Writing "$\kappa+\kappa'=$[constant]" without first specifying which family; writing $K_{\mathrm{BP}}$ from memory in a ghost-number passage.

### C19. Harmonic number definition

**Canonical form.** The harmonic number is
$$H_N \;=\; \sum_{j=1}^{N}\frac{1}{j}.$$
Upper limit $N$, lower limit $1$.
**Sanity check 1 ($N=1$).** $H_1=1$.
**Sanity check 2 ($N=2$).** $H_2=1+1/2=3/2$; $H_1 = H_2 - 1/2$ (NOT $H_2-1$).
**Wrong variants.** (a) $H_N = \sum_{j=1}^{N-1}1/j$ (AP116, AP136): off-by-one, gives $H_1=0$. (b) $H_{N-1}=H_N-1$: wrong recursion; the correct one is $H_N-H_{N-1}=1/N$, so $H_{N-1}=H_N-1/N$. At $N=2$: $H_1=1$ vs. $H_2-1=1/2$. (c) $H_N = \sum_{j=0}^{N}1/j$: divergent term at $j=0$.
**Diagnostic.** Writing a harmonic-number recursion without checking the smallest $N$; writing $H_{N-1}$ inside a $\cW_N$ kappa formula.

### C20. Koszul conductor for Bershadsky-Polyakov

**Canonical form.** For Bershadsky-Polyakov $\cW^k(\fsl_3, f_{\mathrm{sub}})$:
$$K_{\mathrm{BP}} \;=\; c(k) + c(-k-6) \;=\; 196.$$
The Koszul duality is $k\mapsto -k-6$ (Feigin-Frenkel for the subregular $\fsl_3$ reduction).
**Sanity check 1 (explicit).** At $k=0$: $c(0) = -23/3$ (nontrivial) and $c(-6) = 196+23/3 = 611/3$; sum $=196$. (Verified in `theorem_gz_frontier_engine.py`.)
**Sanity check 2 (duality fixed point).** The self-dual level is $k=-3$; at $k=-3$, $c(-3)=c(-3)=98$, so $\kappa+\kappa'=196$. Consistent with both computations.
**Wrong variants.** (a) $K_{\mathrm{BP}}=76$: a prior incorrect value corrected in Wave 7 (see `thread_final_beilinson_rectification_2026_04_07.md`). (b) $K_{\mathrm{BP}}=2$ (AP140): confusing the global Koszul conductor with the local ghost constant $C_{(2,1)}=2$.
**Diagnostic.** Writing $K_{\mathrm{BP}}$ from memory; writing it in a ghost-number passage where small constants dominate attention.

### C21. Igusa cusp form weight and BKM kappa

**Canonical form.** The Igusa cusp form $\Phi_{10}$ on $\mathrm{Sp}(4,\bZ)$ has Siegel modular weight
$$\mathrm{wt}(\Phi_{10}) \;=\; 10 \;=\; 2\,\kappa_{\mathrm{BKM}}(K3\times E),$$
so that
$$\kappa_{\mathrm{BKM}}(K3\times E) \;=\; 5.$$
**Sanity check 1 ($\Phi_{10}=\Delta_5^2$).** The Igusa cusp form is the square of the Borcherds product $\Delta_5$ of weight $5$; this directly gives the factor of 2.
**Sanity check 2 (DT partition function).** The generating function of BPS/DT invariants for $K3\times E$ is $1/\Phi_{10}$, and the kappa-anomaly at genus $g$ extracts weight $2\kappa_{\mathrm{BKM}}\cdot(g-1)$; the $g=2$ coefficient matches $\kappa_{\mathrm{BKM}}=5$.
**Wrong variants.** (a) $\kappa_{\mathrm{BKM}}(K3\times E)=10$: identifying kappa with the full weight rather than half. (b) $\kappa_{\mathrm{BKM}}=2$: confusing with some small ghost constant. (c) $\mathrm{wt}(\Phi_{10})=5$: confusing with the base Borcherds product $\Delta_5$.
**Diagnostic.** Writing a BKM kappa without explicitly invoking the factor of 2 in the Siegel-weight-to-kappa translation.

### C22. Eta function q-expansion

**Canonical form.** The Dedekind eta function has the expansion
$$\eta(\tau) \;=\; q^{1/24}\prod_{n=1}^{\infty}(1-q^n),\qquad q=e^{2\pi i\tau}.$$
The prefactor $q^{1/24}$ is essential.
**Sanity check 1 (modular weight).** $\eta(\tau)$ has modular weight $1/2$; $\eta(-1/\tau)=\sqrt{-i\tau}\,\eta(\tau)$. Without the $q^{1/24}$ prefactor the transformation fails.
**Sanity check 2 ($c=1$ partition).** The Heisenberg partition function is $1/\eta(\tau)$ (after stripping the $q^{c/24}$ prefactor), giving $c=1$: matches $c_{\mathrm{Heis}}(k=1)=1$.
**Wrong variants.** (a) $\eta(\tau)=\prod(1-q^n)$: drops the $q^{1/24}$ prefactor; fails modular transformation. (b) $\eta(\tau)=q^{1/12}\prod(1-q^n)$: wrong prefactor exponent. (c) $\eta(\tau)=q^{1/24}\prod(1-q^{2n})$: confusing with theta functions.
**Diagnostic.** Writing $\eta$ expansions in a passage that compares conformal characters without the $c/24$ vacuum shift.

### C23. Bicoloured partition q-expansion

**Canonical form.** The expansion $1/\eta(\tau)^2 = q^{-1/12}\sum_{n\ge 0} p_{-2}(n) q^n$ where $p_{-2}(n)$ are bicoloured partition numbers:
$$(p_{-2}(0), p_{-2}(1), p_{-2}(2), p_{-2}(3), p_{-2}(4), \ldots) \;=\; (1, 2, 5, 10, 20, \ldots).$$
These are OEIS A002513 (number of partitions of $n$ into parts of two kinds).
**Sanity check 1 ($n=1$).** Two colourings of the single-part partition: $p_{-2}(1)=2$.
**Sanity check 2 ($n=2$).** $1+1$ with two colours = $\binom{2+1}{2}=3$ multisets, plus $2$ with two colours = $2$, total $5$: $p_{-2}(2)=5$.
**Wrong variants.** (a) Triangular numbers $(1,3,6,10,\ldots)$: confusing with $T_n=n(n+1)/2$ (AP135). (b) Powers of 2 $(1,2,4,8,\ldots)$: wrong generating function. (c) Ordinary partitions $(1,1,2,3,5,\ldots)$: dropping the bicolouring (this is $p(n)$, not $p_{-2}(n)$).
**Diagnostic.** Writing $q$-expansion coefficients of $1/\eta^r$ for $r\ge 2$ without OEIS lookup; pattern-matching to the nearest low-entropy sequence.

### C24. Cauchy integral normalization

**Canonical form.** The Cauchy integral formula for the coefficient of $z^{n-1}$ in a holomorphic function $f$:
$$[z^{n-1}]f(z) \;=\; \frac{1}{2\pi i}\oint f(z)\frac{dz}{z^n}.$$
The normalization is $1/(2\pi i)$ with the imaginary unit in the denominator.
**Sanity check 1 ($f=z$).** $[z^0]z=0$ and $[z^{-1}] z = 0$; $[z^0]1 = 1$ via $\oint dz/(2\pi i z)=1$. Consistent.
**Sanity check 2 (genus-one $F_1$).** The standard identity $F_1 = \kappa/24$ for Heisenberg follows from a Cauchy integral with $1/(2\pi i)$; missing the $i$ yields zero for real integrands. (AP120 caught this.)
**Wrong variants.** (a) $1/(2\pi)$: missing the $i$, gives real coefficients zero. (b) $1/(\pi i)$: factor of 2 error. (c) $1/(2\pi i)^n$: wrong power for a single residue extraction.
**Diagnostic.** Writing residue formulas in a passage that has just computed a real integral; the real-analysis normalization contaminates the complex-analysis writing.

### C25. MC equation

**Canonical form.** The Maurer-Cartan equation for an element $\Theta\in L$ in a dg Lie (or $L_\infty$) algebra is
$$d\Theta + \frac{1}{2}[\Theta,\Theta] \;=\; 0,$$
and, in the quantum / BV / curved case,
$$\hbar\,\Delta\,S + \frac{1}{2}\{S,S\} \;=\; 0 \qquad (\text{QME}).$$
**Sanity check 1 (abelian limit).** If $[-,-]=0$ the equation reduces to $d\Theta=0$: closed elements, consistent with the flat connection interpretation.
**Sanity check 2 (grading).** In cohomological grading with $|d|=+1$, the MC element sits in degree $1$; the bracket $[\Theta,\Theta]$ sits in degree $2$; both sides of the equation have degree $2$.
**Wrong variants.** (a) $d\Theta + [\Theta,\Theta]=0$: dropping the $1/2$ (only correct in the odd parity case where $[\Theta,\Theta]=0$ automatically). (b) $d\Theta - (1/2)[\Theta,\Theta]=0$: sign error. (c) $d\Theta + (1/2)\{\Theta,\Theta\}=0$: mixing antibracket and bracket notation.
**Diagnostic.** Writing MC in a BV passage and importing the antibracket notation incorrectly into a dg Lie setting.

### C26. G/L/C/M shadow depth classification

**Canonical form.** The depth class of a standard chiral algebra is determined by the highest nonvanishing shadow arity:
$$
\text{G (Gaussian): } r=2 \text{ (Heisenberg)};\quad
\text{L (Lie/tree): } r=3 \text{ (affine KM)};
$$
$$
\text{C (cubic): } r=4 \text{ (}\beta\gamma\text{-system)};\quad
\text{M (modular): } r=\infty \text{ (Virasoro, }\cW_N\text{)}.
$$
**Sanity check 1 (Heisenberg).** Gaussian path integral has only two-point function; $r=2$. Consistent.
**Sanity check 2 ($\cW_2=$Vir).** Virasoro is class M with $r=\infty$: the shadow tower never terminates. Matches class-M prediction.
**Wrong variants.** (a) Heisenberg $\in$ L: confusing with affine KM. (b) $\beta\gamma\in$ L: missing that $\beta\gamma$ has a genuine quartic (cubic-shadow-arity $r=4$) obstruction. (c) Virasoro $\in$ L with finite depth 1: confusing generating depth $d_{\mathrm{gen}}$ with algebraic depth $d_{\mathrm{alg}}$ (AP131).
**Diagnostic.** Writing depth classifications without first specifying whether the measure is generating or algebraic depth.

### C27. Chiral Hochschild of Virasoro amplitude

**Canonical form.** The chiral Hochschild complex of Virasoro satisfies
$$\mathrm{ChirHoch}^*(\mathrm{Vir}_c) \text{ is concentrated in degrees }\{0,1,2\}, \qquad \dim_{\mathrm{total}} \le 4.$$
This is cohomological AMPLITUDE, not virtual dimension (AP134).
**Sanity check 1 (polynomial).** The dimensions in degrees $0,1,2$ sum to at most $4$, strictly bounded; matches Theorem H.
**Sanity check 2 (contrast with Gelfand-Fuchs).** Gelfand-Fuchs cohomology of Witt/Virasoro Lie algebra is infinite-dimensional; ChirHoch is bounded (AP94). These are different theories.
**Wrong variants.** (a) $\mathrm{ChirHoch}^*=\bC[\Theta]$: infinite polynomial ring (AP94). (b) $\mathrm{ChirHoch}$ has virtual dimension 2 (AP134): conflating amplitude with vdim. (c) $\mathrm{ChirHoch}=\mathrm{GF}^*(\mathrm{Vir})$: confusing with Gelfand-Fuchs (AP95).
**Diagnostic.** Writing about chiral Hochschild in a passage that discusses Gelfand-Fuchs or Lie-algebra cohomology.

### C28. Arnold form vs KZ connection

**Canonical form.** The Knizhnik-Zamolodchikov connection is
$$\nabla_{\mathrm{KZ}} \;=\; d \;+\; \sum_{i<j} r_{ij}(z_i-z_j)\,d(z_i-z_j) \;=\; d + \sum_{i<j} r_{ij}\,dz_{ij},$$
with the differential form $dz_{ij}$ (NOT $d\log z_{ij}$). The Arnold form $\omega_{ij}=d\log(z_i-z_j)$ is a bar-construction COEFFICIENT, not the KZ connection form.
**Sanity check 1 (level).** For affine KM at level $k$, the KZ connection uses $r_{ij}(z) = k\Omega_{ij}/z$ so that $r_{ij}\cdot dz$ produces the standard $\Omega_{ij}\,dz_{ij}/(z_i-z_j)$, matching AP117.
**Sanity check 2 (bar construction).** In the bar complex $B^{\mathrm{ord}}(A)$, the Arnold forms $\omega_{ij}=d\log z_{ij}$ serve as the structure coefficients of the cobar differential; they are NOT the connection on a moduli space.
**Wrong variants.** (a) $\nabla_{\mathrm{KZ}} = d + \sum r_{ij}\,d\log z_{ij}$: confusing the bar coefficient with the connection form (AP117). (b) $\nabla_{\mathrm{KZ}} = d + \sum \Omega_{ij}\,dz_{ij}$: dropping the level $k$ from the r-matrix (AP126).
**Diagnostic.** Writing the KZ connection next to an Arnold-form passage about the bar complex; the $d\log$ contaminates the writing.

### C29. Genus-1 period matrix collapse

**Canonical form.** At genus $g\ge 2$, the inverse period matrix $(\mathrm{Im}\,\Omega)^{-1}$ is a $g\times g$ MATRIX; at genus 1 it degenerates to the scalar $1/\mathrm{Im}(\tau)$. Formulas must be written in the full multi-dimensional form:
$$\omega_g \;=\; c_1(\lambda_g) \;\in\; H^2(\bar M_g,\bQ), \qquad \text{use }(\mathrm{Im}\,\Omega)^{-1} \text{ as a matrix.}$$
**Sanity check 1 (g=2).** $(\mathrm{Im}\,\Omega)^{-1}$ is a $2\times 2$ matrix; formulas involving traces, determinants, and quadratic forms must be checked at $g=2$ (AP118).
**Sanity check 2 (g=1 specialization).** The genus-1 formula is recovered by setting $g=1$, but this must be the SPECIALIZATION of the matrix formula, not the starting point.
**Wrong variants.** (a) Writing $1/\mathrm{Im}(\tau)$ at all genera (AP118): degenerates to a scalar that only exists at $g=1$. (b) Writing $(\mathrm{Im}\,\Omega)^{-1}$ as a scalar divisor: forgets matrix structure.
**Diagnostic.** Writing a higher-genus formula by starting from the genus-1 version and "promoting" scalars; the matrix structure is lost.

### C30. Delta discriminant for finite shadow tower

**Canonical form.** The shadow-tower finite-depth discriminant is
$$\Delta \;=\; 8\,\kappa\,S_4.$$
The shadow tower terminates at finite depth iff $\Delta=0$, which for fixed $\kappa\ne 0$ means $S_4=0$.
**Sanity check 1 (Heisenberg).** $\kappa=k$, $S_4=0$ (Gaussian), so $\Delta=0$: finite tower (depth 2). Class G.
**Sanity check 2 (Virasoro).** $\kappa=c/2$, $S_4\ne 0$ generically, so $\Delta\ne 0$: infinite tower. Class M.
**Wrong variants.** (a) $\Delta = 4\kappa S_4$: wrong factor. (b) $\Delta = \kappa^2 S_4$: wrong power (the $u=\eta^2=\kappa\cdot\omega_g$ relation is LINEAR in $\kappa$, not quadratic, AP21). (c) $\Delta = 0 \iff \kappa=0$: ignores the $S_4$ factor.
**Diagnostic.** Writing the discriminant while thinking about quadratic forms in $\kappa$; the physical linearity is forgotten.
