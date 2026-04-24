# P15: Vol III K3 chiral bialgebra / H_Delta5 / Mukai / kappa lane

Owned file:
`notes/universal_anomaly_platonic_swarm_20260424/P15_vol3_k3_chiral_bialgebra.md`

Target TeX files were read only. No target TeX files were edited.

## Verdict

The standalone may cite Vol III for a real K3/Igusa/Mukai theorem, but
only in its precise Vol III scope.

The theorem-grade Vol III surface is not:

\[
\Phi_3(K3)=\mathbf H_{\Delta_5}
\]

and not:

\[
[m_3,B^{(2)}]_{K3\times E}=0.
\]

The theorem-grade surface is:

\[
\SpCh_{K3,E}\!\left(\PhiFA_3(\Perf(K3\times E))\right)
\simeq \mathbf H_{\Delta_5}
\]

as an \(E_1\)-chiral bialgebra on the elliptic curve \(E\), on the
principal \(K3\times E\) locus, with the BL-2/4/6 comparison witnesses
and the BL-7 Borcherds-weight identity installed. Away from that
principal locus, Vol III itself marks the chiral-bialgebra extension as
conditional.

Thus B3/B4 in the standalone should read:

1. B3: principal-locus stage-two specialisation through
   \(\SpCh_{K3,E}\), not a bare \(K3\) or Hilbert-scheme statement.
2. B4: Mukai-Bruinier conductor normalisation
   \(K^{\kappa_{\mathrm{ch}}}=2c_+(\mathrm{Mukai}(K3))=8\) and
   \(\hbar^2K^{\kappa_{\mathrm{ch}}}=-1\), not a Todd integral,
   not \(\kappa_{\mathrm{BKM}}\), and not the total-space
   Hodge supertrace.
3. K3xE obstruction vanishing remains independent and conditional on
   the cyclic-HKR projection scalar computed in P08.

## Anchors read

- Standalone K3/Mukai surface:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:352-383`,
  `:777-779`, `:905-984`, `:1099-1114`, `:1310-1327`.
- VOA supplement:
  `standalones/universal_anomaly_voa_explicit_supplement.tex:198-219`,
  `:223-303`, `:584-706`.
- Local-global supplement:
  `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:49-80`.
- Vol III doctrine:
  `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:26-50`,
  `:211-231`, `:267-276`, `:304-310`.
- Vol III K3 bialgebra:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1518-1628`;
  `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_chiral_bialgebra_platonic.tex:1-230`,
  `:1456-1565`, `:2230-2425`, `:2840-2890`, `:7360-7468`.
- Vol III kappa stratification:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/cy_d_kappa_stratification.tex:135-220`,
  `:3184-3228`, `:4376-4412`.
- Vol III K3xE obstruction warnings:
  `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex:1500-1525`;
  `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex:13752-13766`.

## Findings

### CRITICAL: the standalone's "Phi_3(K3)" formulation is wrong for the Vol III theorem

The standalone currently says, in the Volume III subsection, that one
lets \(X=K3\) and considers the two-stage factorisation at \(d=3\),
then writes

\[
\Phi_3(K3)=\Sp^{\mathrm{ch}}_{\Sigma_2,C}\circ\Phi^{\mathrm{FA}}_3(K3).
\]

Vol III's theorem is different. The input is the CY3

\[
X=K3\times E,
\]

and the specialisation is along the \(K3\)-fibre to the elliptic base:

\[
\SpCh_{K3,E}\!\left(\PhiFA_3(\Perf(K3\times E))\right)
\simeq U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})
\]

at the chiral-algebra level, and

\[
\SpCh_{K3,E}\!\left(\PhiFA_3(\Perf(K3\times E))\right)
\simeq \mathbf H_{\Delta_5}
\]

as \(E_1\)-chiral bialgebras on the principal locus. The standalone
should not write \(\Phi_3(K3)\) in this lane. \(K3\) alone is CY2 and
has a CY2 shift; the \(d=3\) object is \(K3\times E\).

### CRITICAL: Vol III does not prove K3xE obstruction vanishing

Vol III explicitly separates the \(K3\times E\) BKM/chiral-bialgebra
specialisation from product-geometry vanishing. It also records that
global NCCR fails on \(K3\times E\), including:

\[
\Ext^1_{K3\times E}(\mathcal F\boxtimes\mathcal O_E,
\mathcal F\boxtimes\mathcal O_E)
\supset H^1(E,\mathcal O_E)\neq0.
\]

This is the same structural reason P08 found a nonzero obstruction
target:

\[
H^2(K3\times E,\Omega^1)
=
H^1(K3,\Omega^1_{K3})\otimes H^1(E,\mathcal O_E)
\oplus
H^2(K3,\mathcal O_{K3})\otimes H^0(E,\Omega^1_E).
\]

Vol III may be cited for the principal-locus K3 bialgebra comparison
and for the Mukai/Borcherds constants. It may not be cited for
\(\alpha_{K3\times E}=0\). That remains exactly the cyclic-projection
condition:

\[
\operatorname{Cyc}_3(\pi_{K3}^*\operatorname{at}_{K3}^{\cup2})=0.
\]

P08 sharpens this: product naturality kills the \(20\)-dimensional
mixed summand, but a one-dimensional scalar line remains. Under the
standard Atiyah/Chern-Weil/Rozansky-Witten normalisation that scalar is
expected to be proportional to \(\int_{K3}c_2(T_{K3})=24\), hence not
zero unless the final cyclic-HKR convention forces a trace-free
projection.

### SERIOUS: "canonical non-abelian chiral bialgebra" needs Vol III's abelian-at-Lie discipline

Vol III's own statement is subtle:

- \(\mathbf H_{\Delta_5}\) is a super-quasi-Hopf / \(E_1\)-chiral
  bialgebra.
- Its primitive/vertex closure sees
  \(\mathfrak g_{\Delta_5}\).
- At the Lie-algebra / Hopf-algebra level, Vol III states
  \(\mathbf H_{\Delta_5}\) is abelian: \(24\) Heisenberg/Miki copies.
- The BKM non-abelianity emerges under vertex-operator closure on the
  K3 Fock module.

So the standalone should not say simply "canonical non-abelian chiral
bialgebra" unless it adds the scope:

> the \(E_1\)-chiral bialgebra whose primitive/vertex-operator closure is
> the Borcherds-Kac-Moody algebra \(\mathfrak g_{\Delta_5}\); abelian at
> the raw Lie/Hopf level, non-abelian after BKM vertex closure.

### SERIOUS: the kappa lane must be subscripted and split into four values plus the conductor

Vol III forbids bare \(\kappa\). For \(K3\times E\) the theorem-grade
split is:

\[
\{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}}\}(K3\times E)
=\{0,3,5,24\}.
\]

The values mean:

- \(\kappa_{\mathrm{cat}}(K3\times E)=\chi(\mathcal O_{K3})\chi(\mathcal O_E)=2\cdot0=0\).
- \(\kappa_{\mathrm{ch}}^{\mathrm{Heis}}=3\), the Stage-2 Heisenberg-Cartan rank.
- \(\kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=c_1(0)/2=10/2=5\), the Borcherds weight.
- \(\kappa_{\mathrm{fiber}}=24\), the Mukai-lattice rank / K3 Euler count.

The number \(8\) is not any of these four \(\kappa_\bullet\) values. It is the
Mukai complementarity/conductor value

\[
K^{\kappa_{\mathrm{ch}}}
=\kappa_{\mathrm{ch}}+\kappa_{\mathrm{ch}}^!
=2c_+(\mathrm{Mukai}(K3))
=8.
\]

The standalone should therefore write \(K^{\kappa_{\mathrm{ch}}}\) or
\(K_{\mathrm{Muk}}\) when it means the conductor. It should not call this
\(\kappa_{\mathrm{BKM}}\), the central charge of \(\Delta_5\), or the
total-space Hodge supertrace.

### SERIOUS: Bruinier is one input, not the whole proof of \(K=8\)

Vol III's `thm:humbert-order-K-kappa` proves the monodromy/conductor
identity by combining:

1. Mukai signature \((4,20)\), hence \(c_+=4\);
2. CY2/Mukai doubling, \(K^{\kappa_{\mathrm{ch}}}=2c_+=8\);
3. Bruinier Heegner Chern-class reciprocity for \(\Delta_5\);
4. Riemann-Hilbert translation to monodromy around \(H_1\);
5. the Lusztig/root-of-unity normalisation.

The standalone should cite this package, not say "Bruinier forces
\(K=8\)" or "Bruinier implies \(\hbar^2=-1/8\)".

Safe citation language:

> Vol III, Theorem `thm:humbert-order-K-kappa`, identifies the
> Humbert-\(H_1\) monodromy order, the Mukai doubled conductor
> \(2c_+(\mathrm{Mukai}(K3))\), and the Lusztig level. Bruinier's
> Heegner Chern-class reciprocity supplies the automorphic Chern-class
> input; the value \(8\) uses the Mukai signature and the conductor
> normalisation.

### SERIOUS: Delta_5 and Phi_10 must not be collapsed

Vol III keeps two levels:

\[
\kappa_{\mathrm{BKM}}(\Delta_5)=5,\qquad \Phi_{10}=\Delta_5^2.
\]

The primitive denominator / BKM side belongs to \(\Delta_5\). The DVV,
reduced-DT, and scalar BPS partition side belongs to

\[
\Phi_{10}^{-1}=\Delta_5^{-2}.
\]

The standalone's bridge to DVV should therefore say:

- \(\mathbf H_{\Delta_5}\) and \(\mathfrak g_{\Delta_5}\) are pinned by
  \(\Delta_5\), weight \(5\).
- The protected index / reduced DT / DVV scalar partition is the square
  or doubled character, \(1/\Phi_{10}=\Delta_5^{-2}\).
- A statement such as
  \(\operatorname{ch}\mathbf H_{\Delta_5}=1/\Phi_{10}\) requires a
  square, Fock-pairing, or quasi-NCCR character construction; it is not
  the primitive denominator identity.

### MODERATE: the standalone's arithmetic-VOA lane is still too strong

The main standalone has already made the nine-discriminant list
conditional. The VOA supplement still phrases the nine
\(V^{\mathrm{arith}}_{K3,d_K}\) as canonical arithmetic VOAs with
central charge \(8\). Vol III does not supply that as a simple theorem
of the principal \(K3\times E\) bialgebra. The safer statement is:

> The classical singular-K3 CM discriminants are the
> Shioda-Inose / class-number-one list. The replacement list
> \(\{3,4,7,8,11,15,19,20,24\}\) is conditional on the Bruinier/Chenevier
> coefficient-sign calculation. The attached arithmetic VOA
> \(V^{\mathrm{arith}}_{K3,d_K}\) is a proposed construction unless the
> Scheithauer twist, class-group action, and Mukai-conductor central
> charge are built explicitly for that \(d_K\).

The supplement's phrase "canonical arithmetic VOA" should be read as
conditional, not proved.

## What Vol III proves

### Proved / proved-here in Vol III, as cited

1. Principal-locus specialisation:

\[
\SpCh_{K3,E}\!\left(\PhiFA_3(\Perf(K3\times E))\right)
\simeq U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})
\]

and, with coproduct/associator/R-matrix comparison data, as
\(E_1\)-chiral bialgebras:

\[
\SpCh_{K3,E}\!\left(\PhiFA_3(\Perf(K3\times E))\right)
\simeq \mathbf H_{\Delta_5}.
\]

Scope: principal \(K3\times E\) locus; BL-2/4/6 and BL-7 comparison
witnesses; not a general CY3 theorem.

2. BKM weight:

\[
\kappa_{\mathrm{BKM}}(\Delta_5)=c_{\phi_{0,1}}(0,0)/2=10/2=5.
\]

3. Mukai conductor:

\[
\operatorname{sig}(\widetilde H(K3,\mathbb Z))=(4,20),\quad c_+=4,\quad
K^{\kappa_{\mathrm{ch}}}=2c_+=8.
\]

4. Normalised trace/conductor relation on the \(B\)-family:

\[
\hbar^2K^{\kappa_{\mathrm{ch}}}=-1,\qquad \hbar^2=-1/8.
\]

This is a conductor normalisation, not a Todd integral.

5. Four \(K3\times E\) kappa invariants:

\[
\{\kappa_{\mathrm{cat}},\kappa_{\mathrm{ch}}^{\mathrm{Heis}},
\kappa_{\mathrm{BKM}},\kappa_{\mathrm{fiber}}\}
=\{0,3,5,24\}.
\]

6. Character-level K3xE quasi-NCCR / reduced-DT identity:

\[
\chi(\mathcal A^{\mathrm{qNCCR}}(K3\times E))
=-\Phi_{10}^{-1}=-\Delta_5^{-2}
\]

on the stated quasi-NCCR / character-level surface.

### Conditional / frontier in Vol III

1. General CY3 extension of the \(K3\times E\) hCS-to-Hall/Borcherds
specialisation.
2. Equivariant CHL sibling \(E_1\)-chiral bialgebras at \(N=2,3,4,6\)
as bialgebras, beyond the automorphic and reduced-DT inputs.
3. Full M-theory parent as a bialgebra. Vol III explicitly stratifies:
theorem at character level, heuristic at 5D SCFT reduction, metaphor at
the M5 sigma-model step, conjectural at full bialgebra.
4. Any use of \(K3\times E\) as a vanishing witness for the
Atiyah-Connes class.
5. The nine arithmetic VOA construction unless the Bruinier/Chenevier
coefficient-sign calculation and the Scheithauer/class-group VOA data
are supplied.

## How the standalone should cite Vol III

### Replacement for `thm:climax-III`

Use:

```tex
\begin{theorem}[Principal K3-fibre specialisation, Vol III; \ClaimStatusProvedElsewhere]
On the principal \(K3\times E\) locus, with the BL-2/4/6 comparison
witnesses and the BL-7 Borcherds-weight normalisation, Vol III proves
\[
  \SpCh_{K3,E}\!\left(\PhiFA_3(\Perf(K3\times E))\right)
  \simeq \mathbf H_{\Delta_5}
\]
as an \(E_1\)-chiral bialgebra on \(E\). The primitive/vertex-closure
Lie super-bialgebra is \(\mathfrak g_{\Delta_5}\), and
\(\kappa_{\mathrm{BKM}}(\Delta_5)=5\).
\end{theorem}
```

Do not write \(X=K3\) in this theorem. Do not write
\(\Phi_3(K3)\). Do not say this holds for arbitrary \(X\).

### Replacement for the trace bridge

Use:

```tex
\begin{theorem}[Mukai conductor and trace normalisation, Vol III;
\ClaimStatusProvedElsewhere]
For the Mukai lattice \(\widetilde H(K3,\mathbb Z)\) of signature
\((4,20)\),
\[
  K^{\kappa_{\mathrm{ch}}}_{\mathrm{Muk}}
  =2c_+(\widetilde H(K3,\mathbb Z))=8.
\]
Vol III identifies this value with the Humbert-\(H_1\) monodromy order
of the \(\Delta_5\)-automorphic \(\mathcal D\)-module and with the
Lusztig level on the \(B\)-family. With the derived-centre trace
normalised by this conductor,
\[
  \hbar^2K^{\kappa_{\mathrm{ch}}}_{\mathrm{Muk}}=-1.
\]
\end{theorem}
```

Then add:

> This theorem supplies B4. It does not imply
> \([m_3,B^{(2)}]_{K3\times E}=0\).

### B3/B4 in the main theorem

Current B3/B4 should be sharpened to:

\[
\text{(B3)}\quad
\SpCh_{K3,E}(\PhiFA_3(\Perf(K3\times E)))\simeq\mathbf H_{\Delta_5}
\]

on the principal locus, with BL-2/4/6/7 comparison data, and with any
chosen \(X\) mapped to that locus by an explicitly defined
specialisation.

\[
\text{(B4)}\quad
\operatorname{tr}_{Z^{\mathrm{der}}_{\mathrm{ch}}}
\text{ is normalised by }
K^{\kappa_{\mathrm{ch}}}_{\mathrm{Muk}}=2c_+=8.
\]

If \(X\neq K3\times E\) on the principal locus, B3 is not available
without the Vol III general-extension conjecture.

## Exact blockers

1. Replace every bare or ambiguous \(K=8\) sentence by
   \(K^{\kappa_{\mathrm{ch}}}_{\mathrm{Muk}}=8\) or
   \(K_{\mathrm{Muk}}=8\), depending on whether the conductor or the
   shorthand central conductor is meant.
2. Replace every sentence identifying \(K=8\) with
   \(\kappa_{\mathrm{BKM}}\). The BKM value is \(5\).
3. Replace the standalone's `Phi_3(K3)` theorem by the principal
   \(K3\times E\) `SpCh_{K3,E}` theorem.
4. Separate:
   \[
   \Delta_5,\quad \Phi_{10}=\Delta_5^2,\quad
   \Delta_5^{-1},\quad \Phi_{10}^{-1}=\Delta_5^{-2}.
   \]
5. Add the sentence: "Vol III does not prove the Atiyah-Connes class
   vanishes on \(K3\times E\); the obstruction edge is exactly the
   cyclic-projection calculation of Proposition `prop:k3e-vanish`."
6. Demote the arithmetic-VOA nine-discriminant construction to
   conditional unless the Bruinier/Chenevier coefficient-sign and
   class-group VOA construction are supplied.
7. In the five-strand example, do not say the elliptic factor collapses
   after Koszul-cofibrant replacement unless the replacement functor is
   defined and shown to preserve the B3/B4 comparison. Vol III says the
   \(E\)-direction is the reference curve and parameter base, not a
   disposable tensor factor.

## Proved / conditional / conjectural split for the standalone

### Proved from Vol III

- Principal-locus \(K3\times E\) stage-two specialisation to
  \(\mathbf H_{\Delta_5}\), in the stated Vol III ambient.
- \(\kappa_{\mathrm{BKM}}(\Delta_5)=5\).
- \(\Phi_{10}=\Delta_5^2\) in the scalar BPS convention.
- Mukai signature \((4,20)\), \(c_+=4\), conductor
  \(K^{\kappa_{\mathrm{ch}}}=8\).
- Four \(K3\times E\) \(\kappa_\bullet\)-values
  \(\{0,3,5,24\}\), from four distinct constructions.

### Conditional

- The standalone's B3 bridge from a general Atiyah-Connes admissible
  locus to \(\mathbf H_{\Delta_5}\).
- The B4 bridge unless the derived-centre trace normalisation is
  imported exactly as a hypothesis.
- The \(K3\times E\) obstruction vanishing.
- Arithmetic VOAs at the proposed nine discriminants.
- CHL sibling bialgebras and all general CY3 bialgebra extensions.

### Conjectural / frontier

- Full M-theory parent of \(\mathbf H_{\Delta_5}\) as a bialgebra.
- Any universal pentagon statement making the K3 vertex force
  \(\alpha_X=0\) without a computed cyclic-HKR return map.
- Any claim that the K3/Igusa vertex is canonical for all CY3 targets.

## Next proof step

The decisive computation is not another K3/Iguasa citation. It is the
one-dimensional scalar from P08:

\[
\alpha_{K3\times E}
=
\lambda_{\mathrm{Cyc}}\,
[\bar\sigma_{K3}]\otimes\eta_E
\quad\in\quad
H^2(K3,\mathcal O_{K3})\otimes H^0(E,\Omega^1_E).
\]

Compute \(\lambda_{\mathrm{Cyc}}\) in the same cyclic-HKR convention as
P01. If \(\lambda_{\mathrm{Cyc}}=0\), \(K3\times E\) becomes the first
geometric zero witness. If \(\lambda_{\mathrm{Cyc}}\neq0\), the paper
has a stronger result: the K3/Igusa vertex is not an admissible point
of the raw Atiyah-Connes locus and must enter only after quotient,
twist, or trace-free projection.
