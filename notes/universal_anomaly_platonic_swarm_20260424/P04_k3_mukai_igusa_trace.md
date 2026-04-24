# P04: K3 / Mukai / Igusa / trace attack-heal report

Scope: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`, its two supplements, and the minimal Vol III / Igusa anchors needed for B3/B4. Target TeX files were not edited.

## Verdict

The K3/Mukai/Igusa/trace side has a real theorem-shaped core, but it is not the theorem "the K3 product kills the universal anomaly."

The constants survive:

\[
\operatorname{Muk}(K3)=H^{\mathrm{even}}(K3,\mathbb Z),\qquad
\operatorname{sig}(\operatorname{Muk}(K3))=(4,20),
\]
\[
c_+(\operatorname{Muk}(K3))=4,\qquad
K=2c_+(\operatorname{Muk}(K3))=8,\qquad
\hbar^2=-1/8,\qquad
\hbar^2K=-1.
\]

They survive only as a normalized Mukai--Bruinier conductor package. They are not consequences of Bruinier Proposition 5.1 alone, not the BKM weight, not the total-space Hodge supertrace, and not a proof that
\[
[m_3,B^{(2)}]_{K3\times E}=0.
\]

The K3 product calculation is now correctly scoped in the standalone: the target
\[
H^2(K3\times E,\Omega^1)
\]
is 21-dimensional, so vanishing is a cyclic-projection computation in a nonzero group.

## Anchors read

- Main standalone: title/abstract and corrected target at `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:78`, `:86--109`; conditional theorem at `:744--765`; K3 product target at `:908--984`; Heegner discriminants at `:1097--1114`; five K3 strands at `:1313--1327`.
- VOA supplement: `standalones/universal_anomaly_voa_explicit_supplement.tex:223--315`.
- Vol III constants: `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:40--50`, `:221--231`.
- Vol III denominator and BKM weight: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex:2670--2702`, `:4380--4391`.
- Vol III Bruinier/Mukai conductor: `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_chiral_bialgebra_platonic.tex:2823--2885`.
- Igusa boundary: `/Users/raeez/igusa-cusp-form/agent_material/07_chiral_koszul_factorization_boundary.tex:45--64`, `:107--118`, `:185--210`, `:245--257`.

## Findings

### CRITICAL: B3 cannot be the raw assertion \(\Phi_3(K3\times E)=\mathbf H_{\Delta_5}\)

The Igusa current envelope is theorem-grade only as a current construction from the already constructed BKM superalgebra:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z).
\]
The Igusa-side anchor explicitly says that the compact \(K3\times E\) realization still needs a microscopic factorization object, a conilpotent coalgebra, and primitive-bracket comparison. Thus B3 must be:

> Conditional on a compact \(K3\times E\) Hall/factorization object \(C_{K3\times E}\), a chiral Koszul realization
> \[
> \Omega_E^{\mathrm{ch}}C_{K3\times E}\simeq \mathsf A_{\Delta,E},
> \]
> and a primitive compatibility identifying protected primitives with \(\mathfrak g_{\Delta_5}\), the stage-two K3 vertex is \(\mathbf H_{\Delta_5}\).

Without those hypotheses, \(\Delta_5\) gives the target denominator, not the compact CY3 chiral algebra.

### SERIOUS: \(K=8\) is a Mukai conductor, not \(\kappa_{\mathrm{BKM}}\)

Vol III separates four \(K3\times E\) numbers:
\[
\kappa_{\mathrm{cat}}(K3\times E)=0,\quad
\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3,\quad
\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=5,\quad
\kappa_{\mathrm{fiber}}=24.
\]
The \(\mathsf B\)-row value
\[
K^\kappa=8
\]
is a fifth conductor/complementarity value:
\[
K^\kappa=2c_+(\operatorname{Muk}(K3))=8.
\]
It must not be identified with the BKM weight \(5\), the total-space categorical trace \(0\), or the K3 Euler number \(24\).

### SERIOUS: Bruinier Proposition 5.1 does not by itself force \(K=2c_+=8\)

The local Vol III specialization records Bruinier 2002 Prop. 5.1 as a Heegner-divisor Chern-class statement. The jump to the conductor identity uses extra ingredients:

1. the Mukai lattice signature \((4,20)\), hence \(c_+=4\);
2. the CY2 Mukai-doubling convention \(K=2c_+\);
3. the effective monodromy-order calculation on \(H_1\), including the Gritsenko additive-lift coefficient and the \(\mathcal D\)-module/Riemann--Hilbert translation.

Thus the correct citation is not "Bruinier implies \(K=8\)." It is "Bruinier supplies the Heegner Chern-class input; Mukai signature plus the conductor normalization identify the value \(8\)."

### SERIOUS: \(\hbar^2=-1/8\) is a normalization, not a Todd trace computation

The supplement now correctly says the Todd integral on \(K3\times E\) gives \(\chi(\mathcal O_{K3\times E})=0\), not \(-1\). Therefore
\[
\operatorname{tr}(1_A)=\hbar^2K
\]
is a normalized conductor identity. The theorem-grade B4 statement must include the normalization as a hypothesis:

> The derived-centre trace is normalized so that the Mukai--Bruinier conductor \(K=8\) pairs with the deformation parameter by \(\hbar^2K=-1\).

### SERIOUS: \(\Delta_5\) and \(\Phi_{10}\) must stay separated

The primitive BKM denominator side is:
\[
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)
\]
in the Igusa normalization.

The scalar square / protected Euler series side is:
\[
Z^X_\square=C_\square\Delta_5^{-2}.
\]
In the standalone convention:
\[
\Phi_{10}=\Delta_5^2,\qquad \Phi_{10}^{-1}=\Delta_5^{-2}.
\]
Therefore:

- \(\mathbf H_{\Delta_5}\) / BKM denominator belongs to \(\Delta_5\), weight \(5\).
- DVV / reduced DT / scalar BPS partition belongs to \(\Phi_{10}^{-1}=\Delta_5^{-2}\), weight \(-10\) after inversion.
- A statement \(\operatorname{ch}\mathbf H_{\Delta_5}=1/\Phi_{10}\) requires a square/double/pairing construction. It is not the primitive denominator identity.

### CRITICAL: \(K3\times E\) does not prove obstruction vanishing

For \(Y=S\times E\):
\[
\at_Y=\pi_S^*\at_S,\qquad \at_S\neq0,\qquad \at_E=0.
\]
The corrected coherent target is
\[
H^2(Y,\Omega_Y^1)\cong
H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E)
\oplus
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1),
\]
of dimension \(20+1=21\). Also
\[
H^3(Y,\Omega_Y^3)\cong
H^2(S,\mathcal O_S)\otimes H^1(E,\mathcal O_E)\cong\mathbb C.
\]
Thus \([m_3,B^{(2)}]_Y=0\) is equivalent to an extra statement:
\[
\operatorname{Cyc}_3(\pi_S^*\at_S^{\cup2})=0
\quad\text{in the two Kunneth summands above.}
\]
This is the main local blocker.

### MODERATE: a K3-only vanishing theorem exists, but it is not a CY3 theorem

There is a true small theorem:

> If the cyclic-HKR construction is replaced by a K3-reduced construction whose output lands in \(H^2(S,\Omega^1_S)\), then the output vanishes for dimensional reasons, since \(H^2(S,\Omega^1_S)=H^{1,2}(S)=0\).

This cannot be silently inserted into \(K3\times E\). The elliptic factor creates the extra nonzero target
\[
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1)
\]
and also the \(20\)-dimensional
\[
H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E).
\]
The only way to make the K3-derived vanishing a theorem on a CY3 locus is to define a quotient/projection functor whose kernel contains both product summands, then prove the trace and B3/B4 comparisons factor through that quotient. That is a different theorem.

## Platonic theorem statement

```tex
\begin{theorem}[K3--Mukai conductor and the Igusa trace bridge]
Let \(S\) be a projective K3 surface and let
\[
  L_{\mathrm{Muk}}=H^{\mathrm{even}}(S,\mathbb Z)
\]
with the Mukai pairing. Then \(L_{\mathrm{Muk}}\) has signature
\((4,20)\), hence \(c_+(L_{\mathrm{Muk}})=4\). The Mukai conductor is
\[
  K_{\mathrm{Muk}}:=2c_+(L_{\mathrm{Muk}})=8.
\]

Let \(\mathfrak g_{\Delta_5}\) be the Gritsenko--Nikulin
Borcherds--Kac--Moody superalgebra. Its primitive denominator is
\[
  \operatorname{den}(\mathfrak g_{\Delta_5})
  =64^{-1}\Delta_5(2Z),
\]
and, in the scalar BPS convention,
\[
  \Phi_{10}=\Delta_5^2,\qquad
  Z_{\mathrm{BPS}}=C\Delta_5^{-2}=C\Phi_{10}^{-1}.
\]

Assume:
\begin{enumerate}[label=\textup{(B3.\arabic*)}]
\item there exists a compact \(K3\times E\) Hall/factorization object
      \(C_{K3\times E}\) on the reference elliptic curve;
\item the chiral cobar comparison
      \(\Omega_E^{\mathrm{ch}}C_{K3\times E}\simeq\mathsf A_{\Delta,E}\)
      is a quasi-isomorphism;
\item the protected primitive bracket of \(C_{K3\times E}\) is
      \(\mathfrak g_{\Delta_5}\);
\item the derived-centre trace is normalized by the Mukai--Bruinier
      conductor \(K_{\mathrm{Muk}}=8\).
\end{enumerate}
Then the K3 vertex of the four-climax diagram is the
\(\Delta_5\)-current envelope, and the normalized trace satisfies
\[
  \hbar^2K_{\mathrm{Muk}}=-1,\qquad \hbar^2=-1/8.
\]

For \(Y=S\times E\), the Atiyah--Connes obstruction lives in the
nonzero group
\[
H^2(Y,\Omega_Y^1)\cong
H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E)
\oplus
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1).
\]
The K3--Mukai trace bridge closes the obstruction edge only under the
additional cyclic-projection identity
\[
  \operatorname{Cyc}_3(\pi_S^*\at_S^{\cup2})=0.
\]
\end{theorem}
```

This is the statement the side wants. It has a proved constant core and explicit bridge hypotheses.

## Exact blockers

1. Define the cochain operator \(B^{(2)}\) and the projection
   \[
   \operatorname{Cyc}_3:
   \pi_S^*(\at_S^{\cup2})\mapsto H^2(S\times E,\Omega^1)
   \]
   with signs, trace, and contraction fixed.
2. Compute its two Kunneth components. The target dimensions are \(20\) and \(1\); a proof must show both components vanish.
3. Prove the compact \(K3\times E\) Hall/factorization object exists and has protected primitives \(\mathfrak g_{\Delta_5}\).
4. Prove the chiral Koszul comparison
   \[
   \Omega_E^{\mathrm{ch}}C_{K3\times E}\simeq\mathsf A_{\Delta,E}.
   \]
5. Separate the denominator identity from scalar partition identities:
   \[
   \operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z),
   \qquad
   Z^X_\square=C_\square\Delta_5^{-2}.
   \]
6. Recheck the Vol III monodromy proof of order \(8\): the vulnerable step is the effective denominator \(1/4\) for the \(H_1\) Fourier coefficient and its conversion to local \(\mathcal D\)-module monodromy.
7. If a Borcea--Voisin twist is used to remove the product's strict-Hodge failure, recompute \(h^{p,q}\), \(\pi_1\), the product Kunneth target, and the period/Humbert locus. The raw product's 21-dimensional count cannot be carried across unchanged.

## Proved / conditional / conjectural split

**Proved or primary-source-backed.**

- \(\operatorname{sig}(\operatorname{Muk}(K3))=(4,20)\).
- \(c_+=4\), hence \(K_{\mathrm{Muk}}=2c_+=8\) once the Mukai-doubling convention is adopted.
- \(\kappa_{\mathrm{BKM}}(\Delta_5)=5\), because \(\phi_{0,1}\) has \(c_1(0)=10\) and the Borcherds weight is \(c_1(0)/2\).
- \(\Phi_{10}=\Delta_5^2\) in the scalar square convention.
- \(H^2(K3\times E,\Omega^1)\) has dimension \(21\); \(H^3(K3\times E,\Omega^3)\cong\mathbb C\).

**Conditional.**

- \(\hbar^2=-1/8\) as a derived-centre trace identity; it is true under the conductor normalization, not as a Todd integral.
- The K3 vertex \(\mathbf H_{\Delta_5}\) as output of compact \(K3\times E\) stage-two specialization.
- The equality of the trace anomaly with the Serre-dual functional of \([m_3,B^{(2)}]\).
- The full \(K3\times E\) obstruction vanishing.

**Conjectural / open.**

- The cyclic-projection vanishing in the full CY3 product target.
- The compact Hall/factorization realization of \(\mathfrak g_{\Delta_5}\) from \(K3\times E\).
- The Bruinier--Chenevier replacement
  \[
  \{43,67,163\}\rightsquigarrow\{15,20,24\}
  \]
  in the nine-discriminant list. The classical list remains
  \[
  \{3,4,7,8,11,19,43,67,163\}.
  \]

## Next proof step

Compute
\[
\operatorname{Cyc}_3(\pi_S^*\at_S^{\cup2})
\]
in the two Kunneth summands of \(H^2(K3\times E,\Omega^1)\). This is the decisive falsifier. If both components vanish, the K3 side becomes a genuine theorem under B3/B4. If either component is nonzero, the four-climax bridge holds only on a stricter derived zero locus, not on the raw \(K3\times E\) Mukai/Humbert locus.

## Files changed

- `notes/universal_anomaly_platonic_swarm_20260424/P04_k3_mukai_igusa_trace.md`

No target TeX files were edited. No build was run.
