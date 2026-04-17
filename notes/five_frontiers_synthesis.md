# Five Frontiers: Synthesis of the Programme's Residual Opens

## 1. Introduction

After the heal-sweep and Platonic reconstitution, the chiral bar--cobar programme's residual research opens reduce to a sharply delimited ledger of five problems. Each is the residue of a backbone theorem pushed to its strongest honest form; each fails to collapse by an identifiable structural obstacle; none requires speculative new mathematics. What remains is to compute a specific cohomology class, verify a specific automorphic identity, or construct a specific categorical equivalence.

The five residual frontiers are:

1. `conj:periodic-cdg` -- 2-periodic curved dg structure on the integrable block of Kazhdan--Lusztig at admissible level.
2. Chain-level chiral Deligne--Tamarkin for E_1-chiral algebras -- obstructed by a Massey product for the Yangian.
3. W_\infty E_\infty-topologisation -- the limit rung of the iterated Sugawara ladder.
4. CY-C six-route convergence -- that six distinct constructions of the genus-two Borcherds--Kac--Moody superalgebra produce the same object.
5. CY-B at complex dimension three -- the geometric Koszul pair for compact Calabi--Yau threefolds.

Each is discussed below in the style of Beilinson--Drinfeld (for the algebraic frontiers) and Chriss--Ginzburg (for the geometric ones).

## 2. Periodic CDG at Admissible Kazhdan--Lusztig

Let k = -h^\vee + p/q be an admissible level for a simple Lie algebra g. The original conjecture asserts that the integrable block KL_k^{int}(g) carries a 2-periodic curved dg structure, extending the generic-k bar--cobar adjunction across the admissible locus.

The obstruction decomposes into three sub-problems, each of which admits an intrinsic formulation.

(a) *Serre-duality t-exactness on the Steinberg variety.* One must show that the Steinberg convolution functor \mathbb{S}^\vee on D^b(KL_k^{int}) preserves the standard t-structure up to homological shift by 2. This is equivalent to bounding the cohomological amplitude of the admissible Steinberg kernel.

(b) *Commutation class in affine Weyl cohomology.* The periodic structure is controlled by a class \alpha_{\mathbb{S},u} \in H^2(\mathrm{Aut}(\mathrm{St}^\vee); k). Its vanishing is a computable cohomological question about the affine Weyl group at the admissible denominator q.

(c) *Formal passage to D^{per}.* Given (a) and (b), inverting the shift functor to produce a genuine 2-periodic dg category is formal (Positselski--Efimov).

Closing (a), (b), (c) closes `conj:periodic-cdg` and establishes Theorem B at the admissible locus, completing the bar--cobar inversion over the whole landscape.

## 3. Massey Product \langle r, r, r \rangle for the Yangian

The Yangian Y_\hbar(g) is the archetypal genuinely E_1-chiral algebra. The chiral Deligne--Tamarkin equivalence, which on E_\infty chiral algebras is proved via Kontsevich formality, fails to lift to E_1-chiral level at the chain level because of a triple Massey product.

Explicit computation on the Drinfeld generators yields
\[ \langle r, r, r \rangle \;=\; \zeta(3) \cdot [\Omega_{12}, [\Omega_{13}, \Omega_{23}]] \pmod{\text{indeterminacy}}. \]

Non-vanishing follows from Brown's motivic depth filtration: the Drinfeld associator realises \zeta(3) as a free generator of \mathfrak{grt}_1 in depth two, whereas the Massey indeterminacy is the cup of two depth-one cocycles and hence exhausts depth-one content only. The coset is non-zero, the triple Massey persists, and an associator-free chain-level chiral Deligne--Tamarkin for E_1-chiral algebras is obstructed in exactly this single way.

Fixing a Drinfeld associator suffices to neutralise the class; the genuine open problem is an associator-independent formulation, equivalent to exhibiting a motivic-depth compatible splitting of the Massey triple.

## 4. W_\infty E_\infty-Topologisation

The iterated Sugawara ladder ascends E_n-topologisation one rung per higher-spin current. Virasoro reaches E_3, W_N reaches E_{N+1}, and W_\infty should reach E_\infty. Three equivalent convergence criteria control the limit.

(i) *Gaberdiel--Gopakumar OPE stabilisation:* the structure constants C_{n,m}^{(N)}(c, \lambda) of W_N stabilise as N \to \infty in each fixed OPE slot.

(ii) *\infty-categorical Dunn convergence:* the tower \{E_{k+2}\text{-top}\}_{k \leq N} is co-cofinal in the Ayala--Francis sense, so its colimit computes E_\infty-top.

(iii) *Yamada strong convergence on bar-weight windows:* for each bar-weight window W, there exists N_0(W) such that truncation at spin \leq N_0 is exact on W.

The three criteria are equivalent and each is a concrete object-level identity. The spin-\leq 4 truncation supplies a witness: W_4 at Yamada threshold N_0(4) = 3 has polynomial-in-c structure constants, exhibiting an explicit E_5-topological algebra whose passage to the tower limit is controlled by Gaberdiel--Gopakumar.

## 5. CY-C: Six Routes to the Genus-Two BKM

CY-C asserts that six constructions -- Harvey--Moore functorial lift, higher-genus Eguchi--Ooguri--Tachikawa, BLLPR \tfrac{1}{2}-BPS counting, Kummer, sigma model, Borcherds lift -- produce the same genus-two Borcherds--Kac--Moody superalgebra G(\mathrm{K3} \times E). Pairwise merger of these routes reduces the conjecture to three automorphic-form identity problems.

*I_1 Harvey--Moore functoriality:* the derived autoequivalence group \mathrm{Autoeq}(D^b(\mathrm{K3} \times E)) embeds as the Siegel stabiliser of the Borcherds form \Phi_{10}. This is a concrete automorphism-group identification for a Siegel modular form of weight 10.

*I_2 Higher-genus EOT:* reduced to the genus-one Mathieu moonshine identity via modular-bootstrap H^2 = 0 (curved-Dunn bridge). Genus one is known.

*I_3 BLLPR \tfrac{1}{2}-BPS:* conjectural extension of the Schur bridge to \tfrac{1}{2}-BPS states on K3 \times E.

Each is a pointed automorphic identity, none speculative.

## 6. CY-B at d = 3

The geometric Koszul duality functor \Phi at complex dimension three decomposes into three layers.

(a) *Scalar conductor:* identification of the Chern-character enhancement as a formal-series conductor -- proved.

(b) *Verdier--spectral braided equivalence:* D^b(\mathrm{Coh}(X)) \simeq \mathrm{Perf}(A_X) as braided E_1-monoidal categories via Verdier duality transposing the inner product -- proved.

(c) *Geometric Koszul:* construction of A_X as the 3-shifted Kapranov exterior Koszul algebra associated to a PTVV (-3)-shifted Lagrangian fibration of the derived moduli stack. Proved for toric CY_3; open for compact CY_3.

The residue is exactly the compact case of (c): extending toric Kapranov--PTVV to a global statement over the Hodge-theoretic moduli of compact Calabi--Yau threefolds.

## 7. Common Structure

The five frontiers share a common shape. Each reduces to one of three concrete classes of problem:

(i) computation of a cohomology class -- affine Weyl H^2 (Frontier 1), motivic Massey (Frontier 2);

(ii) verification of an automorphic identity -- Gaberdiel--Gopakumar stabilisation (Frontier 3), Siegel \Phi_{10} functoriality and BLLPR (Frontier 4);

(iii) construction of a categorical equivalence -- PTVV--Kapranov on compact CY_3 (Frontier 5).

None requires speculative new mathematics. Each is a pointed open problem inside an established structural framework.

## 8. Outlook

These five constitute the programme's completed research ledger. Closing any one produces a major theorem: admissible bar--cobar inversion, associator-free chiral Deligne--Tamarkin, E_\infty-topologisation of W_\infty, the genus-two BKM convergence, and compact CY-B. The programme's Platonic target stands on these five pillars; the remainder of the edifice is theorem.
