## 1. Generators and relations (explicit presentation).
Let \(E=\Omega^{0,\bullet}(\mathbb C^3,\mathfrak g)[1]\) and
\(\mathcal A=c+A_{0,1}+A^*_{0,2}+c^*_{0,3}\). These four entries are
the complete Dolbeault-field components on a CY\(_3\): \(Q=\bar\partial+
[\mathcal A,-]\) stays inside bidegrees \(0,\ldots,3\). They are not,
by themselves, a point-generator presentation of local observables:
one must add holomorphic jets \(\partial^I\mathcal A\). Anchor:
Costello--Gwilliam Vol. I Prop. 6.1.3 / Thm. 6.5.4 and
plat-hCS-quantum.

The fused relation is Wick/BV, not an OPE quotient:
\[
\mu(F,G)=m\circ \exp\!\bigl(\hbar\langle P_{\rm BM},
\delta_F\otimes\delta_G\rangle\bigr)(F\otimes G),\qquad
(Q+\hbar\Delta)^2=0,
\]
with graded-commutative \(\Sym(E^\vee[-1])[[\hbar]]\). The kernel has
\(\|z-w\|^{-6}\) denominator and scalar size \(r^{-5}\), matching the
Bochner--Martinelli formula in plat-hCS-quantum.

## 2. Koszul dual + L_infty structure.
Classically,
\[
\Obs^{\rm cl}_{\rm hCS}(\mathbb C^3)\simeq \CE^\bullet(L),\qquad
L=E[-1]=\Omega^{0,\bullet}(\mathbb C^3,\mathfrak g),
\]
with \(\ell_1=\bar\partial\), \(\ell_2(\alpha,\beta)=
[\alpha\wedge\beta]_{\mathfrak g}\) with Dolbeault/Koszul signs, and
\(\ell_{n\ge3}=0\) before homotopy transfer. The \((-1)\)-shifted
pairing pairs \(c\) with \(c^*_{0,3}\) and \(A_{0,1}\) with \(A^*_{0,2}\).
Quantum observables are a BV/BD deformation; calling the \(\hbar\ne0\)
object plain CE suppresses \(\Delta\). Anchor: plat-hCS-classical /
plat-hCS-quantum.

## 3. pi_1 and E_3 commutativity.
\(\pi_1(\Conf_2(\mathbb C^3))=\pi_1(S^5)=0\) kills binary braid
monodromy only. It does not imply \(E_\infty\) or strict commutativity.
All arities are governed by chains on the relevant little-disk /
Fulton--MacPherson operad; \(H_\*(E_3)=\mathrm{Pois}_3\), with a
degree \(1-3=-2\) bracket (textbook operad fact). Thus the settled
statement is coherent
\(E_3\)-commutativity, not full commutativity. Anchor: CG Vol. II
Thm. 7.5.1; 6d audit E8.

## 4. Cech-Dolbeault MV + associativity.
Cech--Dolbeault Mayer--Vietoris on
\(\overline{\Conf}_n(\mathbb C^3)\) proves descent/locality, not by
itself the shuffle associativity. The missing check is boundary-stratum
compatibility: restrictions of \(P_{\rm BM}\), orientations, and Koszul
signs must match the operadic composition maps. With that check,
CG Vol. I Thm. 6.5.4 and Vol. II Thm. 7.5.1 supply the machine.

## 5. Frontier: E_3-trace via S^5.
For abelian \(\mathfrak g\), the \(S^5=\partial B^6\) trace is the
Bochner--Martinelli residue pairing
\[
\langle a,b\rangle_{S^5}=\int_{S^5}a\,P_{\rm BM}\,b,
\]
nondegenerate on compactly supported / finite-mode duals. On flat
\(\mathbb C^3\), non-abelian 3-dualizability fails by infinite
\(E_3\)-Hochschild size (plat-dualizability). Compact CY\(_3\)
recovery is conditional on elliptic finiteness, Serre duality, and
anomaly cancellation; 6d audit E12 forbids automatic compactness.

## 6. Frontier push: K3 x E and conifold explicit construction attempt.
For \(X=K3\times E\), the honest attempt is
\(\Obs_X=\CE^\bullet(\Omega^{0,\bullet}(X,\mathfrak g))[[\hbar]]\)
with pairing \(\int_X\Omega_X\wedge\langle-,-\rangle\) and a compactly
supported CG propagator. CONJ: \(\ell^{\min}_{n\ge3}=0\). The cited
\(\mathrm{At}(TE)=0\) does not kill \(\mathrm{At}(TK3)\), so formality
does not follow (textbook Atiyah-class obstruction; plat-Linf-minimal).
For the resolved conifold, the same construction is
CONJ until boundary conditions, compact support, and a renormalised
propagator are specified.

## 7. Brutal audit of wave-11-16 / 6d-hCS-audit claims (bullet list, severity HIGH/MED/LOW + one-line fix).
- HIGH: plat-hCS-anomaly conflicts with the 6d audit's quartic-wheel
  obstruction. Fix: separate quartic BV anomaly from cubic inflow data.
- HIGH: finite four-generator OPE presentation omits holomorphic jets.
  Fix: say sheaf-level fields or add all \(\partial^I\)-jets.
- HIGH: \(E_3\) from \(\pi_1=0\) overclaims. Fix: use operadic
  \(E_3\)-coherence for every arity.
- HIGH: K3\(\times E\) formality is unproved. Fix: include the \(TK3\)
  Atiyah obstruction or mark CONJ.
- MED: MV is not associativity. Fix: add boundary-stratum/sign proof.
- MED: flat-to-compact CY transfer ignores compact support. Fix: cite
  CG locality plus compactly supported propagator hypotheses.
- LOW: BM pole wording is ambiguous. Fix: denominator order \(6\),
  scalar size \(r^{-5}\).
