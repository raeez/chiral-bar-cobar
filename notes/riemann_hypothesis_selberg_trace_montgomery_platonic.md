# Riemann Hypothesis via Selberg Trace Formula: Selberg Zeta / Montgomery / Connes-Marcolli

Second-wave attempt on RH through hyperbolic-spectral machinery. Prior
wave's motivic-shadow routes (A, B, C) documented in
[riemann_hypothesis_motivic_shadow_platonic.md](riemann_hypothesis_motivic_shadow_platonic.md):
Route A blocked (non-Euler-product shadow L), Route B yields Rankin
$1/4$-subconvexity independent of Weil, Route C is a category error.
This wave attacks three new angles built on the Selberg trace formula,
Montgomery pair correlation, and Connes-Marcolli spectral realisation.

## What the programme already owns on this side

Three items of existing infrastructure matter.

1. **Heisenberg-Selberg factorisation.** `chapters/connections/bv_brst.tex:1545-1581`
   proves that the genus-$g$ Heisenberg partition function factors
   through the Selberg zeta function via the D'Hoker-Phong determinant
   formula:
   $Z_g(\mathcal{H}_\kappa;\Sigma_g) = (\det\operatorname{Im}\Omega)^{-\kappa/2}
   \cdot Z_{\mathrm{Sel}}(1;\Sigma_g)^{-\kappa/2} \cdot e^{-\kappa c_g/2}$.
   Extraction of the top Chern class confirms
   $F_g^{\mathrm{BV}}(\mathcal{H}_\kappa) = \kappa \cdot \lambda_g^{\mathrm{FP}}$.
   This is a SECOND proof of Thm D via Selberg.

2. **GUE universality of the shadow tower.** `higher_genus_modular_koszul.tex:3612-3644`
   ($\ClaimStatusProvedHere$ `prop:gue-universality`) proves
   $F_g(\mathcal{A}) = F_g^{\mathrm{GUE}}(N^2 = \kappa(\mathcal{A}))$
   for all chirally Koszul $\mathcal{A}$ on the uniform-weight locus.
   The shadow-tower free energies literally ARE the GUE free energies
   at matrix size $N^2 = \kappa$. Class G is Gaussian, class L is cubic
   critical, class C is quartic critical, class M is infinite-potential
   (complex conjugate branch points).

3. **Sewing-Selberg two-variable L-function.** `genus_complete.tex:2725-2807`
   provides $L_{\mathcal{A}}(s, u)$ with the zeta-zero locus explicitly:
   the factor $\zeta(v+1)$ in $S_{\mathcal{A}}(v)$ (where $v = s+u-1$)
   has zeros at $v = \rho - 1$. These are ZEROS of $L_{\mathcal{A}}$,
   not poles; the scattering poles at $s = \rho/2$ are HOLOMORPHIC
   points of the Rankin-Selberg integral (`prop:scattering-residue`).

## Route I: Selberg zeta via the Virasoro shadow tower

**Claim to test.** Is there a map from the Virasoro shadow tower
$\{S_r(\mathrm{Vir}_c)\}$ to the zero set of the Selberg zeta function
$Z_\Gamma(s)$ for $\Gamma = \mathrm{SL}_2(\mathbb{Z})$?

**Setup.** $Z_\Gamma(s) = \prod_{\gamma \text{ prim.}} \prod_{k=0}^\infty
(1 - e^{-(s+k)\ell(\gamma)})$ with non-trivial zeros at $s = 1/2 + i r_n$
where $r_n^2 = \lambda_n - 1/4$ and $\{\lambda_n\}$ are Laplace
eigenvalues on $\mathrm{SL}_2(\mathbb{Z}) \backslash \mathbb{H}$.
The Selberg trace formula is
$\sum h(r_n) + (\text{Eisenstein}) = (\text{vol term}) + \sum_{\gamma \text{ prim}} \sum_{k \ge 1} \frac{\ell(\gamma)}{2\sinh(k\ell(\gamma)/2)} g(k\ell(\gamma))$.

**What the programme supplies.** For Heisenberg, the bar-side partition
function factors literally through $Z_\Gamma(1)$ via Item 1. For
Virasoro $\mathrm{Vir}_c$, the $c/48$ genus-$1$ free energy equals the
Selberg zeta contribution to the BTZ one-loop determinant
(entanglement_modular_koszul.tex:829-834, `Patterson-Perry01`).

**Obstruction.** The Selberg zeta has an $\mathrm{RH}$-analogue that
is PROVED unconditionally: all non-trivial zeros of $Z_\Gamma$ lie on
$\mathrm{Re}(s) = 1/2$ because the Laplace spectrum is real and
positive. The bijection with shadow tower would need to either
(a) transport this unconditional Selberg-RH to the Riemann $\zeta$,
or (b) reproduce the Laplace spectrum from shadow data.

Direction (a) fails because the bridge from $Z_\Gamma$ to $\zeta$ runs
through the scattering matrix $\varphi(s) = \Lambda(1-s)/\Lambda(s)$
of the Eisenstein series: $Z_\Gamma$ zeros come in TWO kinds — Maass
(cuspidal) and scattering (Eisenstein, controlled by $\varphi$). The
Maass zeros give genuine Laplace eigenvalues; the Eisenstein zeros are
at $s = \rho/2$ where $\rho$ ranges over $\zeta$-zeros. RH for $\zeta$
is equivalent to the statement that ALL Eisenstein zeros of $Z_\Gamma$
(in the Selberg-RH sense) sit on $\mathrm{Re}(s) = 1/4$, a fact that is
NOT part of Selberg-RH and is exactly the content of classical RH.

Direction (b) fails because the shadow tower is real-analytic on the
family parameter $c$, not on $s$. Laplace eigenvalues $\lambda_n$ come
from the QUOTIENT surface $\Gamma \backslash \mathbb{H}$; the shadow
tower comes from the CHIRAL algebra (the bulk theory living on
$\Sigma_g$, not on the arithmetic surface). The programme's Heisenberg
factorisation uses $\Sigma_g = $ hyperbolic surface of GENUS $g$, not
the modular curve.

**Verdict on Route I.** Negative. The Heisenberg-Selberg factorisation
and the BTZ Selberg identity confirm the SHADOW-TOWER-LEVEL consistency
with Selberg zeta on hyperbolic geometry, but the arithmetic bridge
from $Z_\Gamma$ to $\zeta$ passes through the Eisenstein scattering
matrix, which sits at $s = \rho/2$ rather than on the critical line.
Selberg-RH does NOT imply Riemann-RH. The programme's Heisenberg-Selberg
result is a REFORMULATION of $\kappa(\mathcal{H}) = 1$ via D'Hoker-Phong,
not a new path to RH. The Heisenberg spectrum is KNOWN unconditionally
(Laplacian eigenvalues on $\mathrm{SL}_2(\mathbb{Z})\backslash\mathbb{H}$
are positive); connecting to $\zeta$-zeros goes through Eisenstein
scattering, which is external.

## Route II: Montgomery pair correlation via R(z) eigenvalue spectrum

**Claim to test.** For $\widehat{\mathfrak{sl}}_2$ at level $k$, compute
the eigenvalue spacing statistics of $R(z)$ on $V \otimes V$ as $k \to \infty$.
Does this match GUE pair correlation?

**Structure available.** The universal R-matrix of the Yangian
$Y_\hbar(\mathfrak{sl}_2)$ on the evaluation module $V = V(\lambda)
\otimes V(\mu)$ has spectrum that depends rationally on $z$. For
$\mathfrak{sl}_2$ in the fundamental rep $V = \mathbb{C}^2$, the
$R$-matrix on $V \otimes V$ has two eigenvalues:
$\lambda_\pm(z) = 1$ on symmetric / antisymmetric subspaces,
with the explicit expansion $R(z) = 1 + \hbar P/(z) + O(\hbar^2)$
giving eigenvalues $1 + \hbar/(z \pm \hbar)$.

**Prop:gue-universality already proves the GUE match at the FREE ENERGY
level.** The shadow-tower free energies $F_g$ equal the GUE free
energies at $N^2 = \kappa$. This is a STATEMENT ABOUT GENUS EXPANSION,
not about eigenvalue spacing of a specific R-matrix. It is the double
scaling limit statement, not the pair correlation statement.

**The pair-correlation question.** Montgomery's conjecture is about
normalized zero spacings of $\zeta$, matching GUE pair correlation
density $1 - (\sin\pi x /\pi x)^2$. Translating to the programme:
does the $R(z)$ eigenvalue spacing on $V^{\otimes N}$ (viewed as $N$
spectral parameters with eigenvalues at poles $z_{ij} = z_i - z_j$)
exhibit this statistic as $N \to \infty$?

**Computation sketch for $\widehat{\mathfrak{sl}}_2$ at level $k$.**
On a tensor product $V_{u_1} \otimes \cdots \otimes V_{u_N}$ of
evaluation modules with spectral parameters $\{u_i\}$, the Yangian
transfer matrix $T(z)$ has eigenvalues determined by the Bethe ansatz:
$\Lambda(z) = \prod_i \frac{z - u_i + \hbar}{z - u_i} \cdot Q(z-\hbar)/Q(z) + \prod_i \frac{z - u_i}{z - u_i + \hbar} \cdot Q(z+\hbar)/Q(z)$
where $Q(z) = \prod_j (z - v_j)$ are Bethe roots. The NORMALISED zero
spacings of $\Lambda(z)$ (that is, spacings between Bethe roots $v_j$)
as $N \to \infty$ at fixed filling ratio $M/N \to \alpha \in (0,1)$
are KNOWN to match GUE for generic irrational $\alpha$ (KKMM97,
Korepin-Slavnov, Bethe-ansatz free-fermion limit). This is NOT a
programme-internal result; it is classical integrable-systems / random
matrix theory.

**What the programme adds.** The factorisation
$F_g(\mathcal{A}) = F_g^{\mathrm{GUE}}(\kappa(\mathcal{A}))$
says that the shadow-tower generating function IS the GUE partition
function at $N^2 = \kappa$. This is a STRONGER statement than generic
GUE pair correlation at the free-energy level: it gives equality of
GENUS EXPANSIONS, not just leading pair correlation. However, the
bridge to $\zeta$-zero pair correlation would require:

(i) The Bethe roots of the shadow-Yangian to be identified with the
Riemann zeros. No such identification exists. The Bethe roots of the
shadow-Yangian sit on the shadow metric's spectral curve
$\Sigma_L: y^2 = Q_L(t)$, whose branch points for lattice VOAs are
quadratic irrationalities from the Gram matrix. These are not
transcendental like $\zeta$-zeros.

(ii) The large-$N$ limit to reach Montgomery. The GUE universality
`prop:gue-universality` is at $N^2 = \kappa$, which is typically small
and rational (Heisenberg: $N^2 = 1$; KM level $k$: $N^2 = \dim(g)(k+h^v)/(2h^v)$).
Montgomery requires $N \to \infty$ (infinite matrix). The programme's
$\kappa$ is bounded by the algebra, not by a limit parameter.

**Verdict on Route II.** The programme has GUE universality at the
FREE-ENERGY level (the shadow tower IS a GUE matrix model), but this
does NOT transport to Montgomery pair correlation of $\zeta$-zeros
because (i) shadow-Bethe roots are algebraic, not transcendental, and
(ii) $\kappa$ is bounded per algebra, not a limit parameter. The
Montgomery-GUE correspondence for $\zeta$ requires the full
automorphic spectrum of $\mathrm{GL}(2)/\mathbb{Q}$, which is external
to the chiral algebra. The programme's R-matrix spectrum gives a
Bethe-ansatz analogue that DOES match GUE on its own terms (classical
result), but does not connect to $\zeta$.

## Route III: Connes-Marcolli spectral realisation of zeros

**Claim to test.** Is there an isomorphism between the programme's
derived chiral centre $Z^{\mathrm{der}}_{ch}(\mathcal{A})$ and the
Connes-Marcolli operator $H_{\mathrm{CM}}$ whose spectrum realises
$\{\mathrm{Im}(\rho) : \zeta(\rho) = 0\}$?

**Connes-Marcolli setup.** The noncommutative adele class space
$\mathbb{A}_{\mathbb{Q}} / \mathbb{Q}^*$ carries a Bost-Connes
quantum statistical mechanical system with partition function $\zeta(s)$
and KMS states at inverse temperature $\beta = s$. The "Hamiltonian"
$H$ is unbounded positive self-adjoint on a specific $L^2$ space of
adele classes; its spectrum is conjecturally $\{\log p : p \text{ prime}\}$
for the position operator and $\{\mathrm{Im}(\rho)\}$ for the dual
(Connes' formulation of RH as a Weil positivity on this space).

**Candidate comparison.** The programme's $Z^{\mathrm{der}}_{ch}(\mathcal{A})$
acts on $\mathrm{Rep}(\mathcal{A})$ as an $E_2$-chiral Gerstenhaber
algebra. For the self-dual Virasoro at $c = 13$
(`prop:two-fixed-points`), $\mathrm{Vir}_{13}$ has a Koszul involution
making the derived centre self-dual. For the Bost-Connes side, the
"self-dual point" is $\beta = 1/2$ (the critical line).

**Obstruction.** The Bost-Connes system is defined over $\mathbb{Q}$
(function-field analogue replaced by number field); the programme's
chiral algebra is defined over $\mathbb{C}$ (complex algebraic curves).
The arithmetic descent from function fields to number fields is the
ARCHETYPAL gap in the Weil-conjectures-to-RH programme and remains open.
`working_notes.tex:6095-6125` already records this: "The Bost-Connes
system is defined over $\mathbb{Q}$; the bar complex is defined over
$\mathbb{C}$... the arithmetic descent is the fundamental obstruction."

**What would need to be added.** A chiral algebra over $\mathbb{F}_p$
or $\mathbb{Z}_p$ with a bar-cobar structure whose derived centre maps
to the local Bost-Connes algebra. Nothing in the programme supplies
this. The bar-cobar adjunction is characteristic-0 (Francis-Gaitsgory
factorisation on Ran(X) requires $\mathrm{char} = 0$ for the infinity-
categorical machinery).

**Verdict on Route III.** The most structurally compatible route
(derived centre $\leftrightarrow$ Bost-Connes Hamiltonian as E_2-chiral
Gerstenhaber algebras) is blocked by the characteristic-0 vs
arithmetic-$\mathbb{Q}$ gap. `working_notes.tex:6103` identifies this
as "the most structurally compatible approach, but no bridge has been
constructed." Second wave confirms: no additional structure in the
programme supplies the $\mathbb{Z}/\mathbb{F}_p$ arithmetic descent
that Connes-Marcolli requires.

## Synthesis: where the programme DOES connect to Selberg

The three Selberg-side routes each run into the same structural
barrier that blocked Routes A-C in the prior wave: the programme's
algebra-geometry-arithmetic trichotomy (`working_notes.tex:3827-3876`)
places the bar complex on the ALGEBRA axis, the hyperbolic Laplacian
on the GEOMETRY axis, and $\zeta$ on the ARITHMETIC axis. Selberg
trace formula connects GEOMETRY $\leftrightarrow$ ARITHMETIC (closed
geodesics = primes); the programme's bar complex only reaches the
GEOMETRY axis via partition-function evaluation.

**Where real traction lives:** `prop:gue-universality` is a GENUINE
non-trivial structural result — the shadow-tower generating function
IS the GUE matrix-model partition function at $N^2 = \kappa$. This
places the chiral algebra's genus expansion in the random-matrix
universality class. For $\zeta$, Montgomery-GUE is EMPIRICALLY
verified (Odlyzko) but NOT proved; the programme's GUE universality
is PROVED for chirally Koszul algebras. The programme's content
therefore is a PROVEN matrix-model statement at the chiral-algebra
level; Montgomery-GUE for $\zeta$ remains conjectural and external.

**The one new observation from this wave.** The Sewing-Selberg
two-variable L-function $L_{\mathcal{A}}(s, u) = \Gamma(v) (2\pi)^{-v}
\zeta(v+1)(\zeta(v) - 1)$ for Virasoro has zeros at $v = \rho - 1$
for each non-trivial $\zeta$-zero $\rho$. These are EMBEDDED in the
programme's L-function; the programme does NOT constrain their
location. The embedding gives a shadow-tower-level STATEMENT of RH:
RH $\Leftrightarrow$ $L_{\mathrm{Vir}}(s, u)$ has all non-trivial
zeros along the diagonal $s + u = 3/2$ (since $v = s+u-1$ and
$\mathrm{Re}(\rho) = 1/2 \Leftrightarrow \mathrm{Re}(v) = -1/2$, so
$s + u = 1/2$). This is a REFORMULATION of RH inside the programme's
$L$-function, not a proof. It does record that the programme's
natural two-variable L-function IS a candidate target if a chiral-side
functional equation ever becomes available; currently none is.

## Status

Of the three Selberg-side routes attacked:

- **Route I (Selberg zeta)**: Negative. Selberg-RH is unconditional;
  does NOT imply $\zeta$-RH; bridge to $\zeta$ runs through Eisenstein
  scattering matrix, external.
- **Route II (Montgomery-GUE)**: Programme HAS GUE universality at
  free-energy level (`prop:gue-universality`) but this is a statement
  about matrix-model partition functions, not $\zeta$-zero statistics.
  Shadow-Bethe roots are algebraic, $\zeta$-zeros are transcendental;
  no identification.
- **Route III (Connes-Marcolli)**: Most structurally compatible;
  blocked by characteristic-0 vs arithmetic-$\mathbb{Q}$ gap (the
  archetypal Weil-to-RH obstruction).

**Combined verdict with prior wave.** Six routes attacked (A-C
motivic/Koszul + I-III Selberg). All six blocked by the same
structural trichotomy: the programme sits on algebra $\leftrightarrow$
geometry, not geometry $\leftrightarrow$ arithmetic. The programme's
new RH-adjacent contributions confirmed by this wave:

1. `prop:gue-universality` — shadow tower IS GUE at matrix size
   $N^2 = \kappa$. Proved for all chirally Koszul $\mathcal{A}$;
   stronger than Montgomery (which is empirical for $\zeta$).
2. `thm:shadow-spectral-correspondence` — shadow depth equals L-factor
   count in Hecke decomposition of lattice theta functions.
3. Heisenberg-Selberg factorisation — $Z_g(\mathcal{H})$ literally
   factors through Selberg zeta.

These are genuine programme results; they are ABOUT chiral algebras,
not about $\zeta$. The programme does not supply a proof of RH, and
the obstruction identified by the prior wave (`rem:structural-obstruction`)
— real spectral line vs complex critical line — is CONFIRMED across
all six routes. RH remains external. Honest position: the programme
has GUE universality and Heisenberg-Selberg at theorem level, a
reformulation of RH inside $L_{\mathcal{A}}(s, u)$ at remark level,
and no new proof path.
