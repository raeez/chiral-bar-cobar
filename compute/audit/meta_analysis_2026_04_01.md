# Meta-Analysis: Taking the Programme to the Next Level

## The Beilinsonian Verdict in One Paragraph

The programme has built an impressive algebraic engine with 2,200+ pages of proved theorems, 468 test files, and five main theorems all established. But it has a critical imbalance: **the proofs are almost entirely structural (existence, adjunction, characterization), while the computations are almost entirely tautological above genus 0.** The genus-0 bar complex is computed from first principles. At genus 1 and above, every numerical verification takes its answer as input. The Feynman agent's finding is the single most important diagnostic: "The programme has teeth at genus 0. At genus >= 1, it has only formulas that verify formulas." Until this changes, the programme is a machine that has been built but never turned on.

---

## 1. The Five Most Impactful Things to Prove Next

### 1.1 Multi-generator universality at genus >= 2 (op:multi-generator-universality)

**What it is.** For multi-weight algebras (W_3, W_N, etc.) at genus g >= 2, prove that obs_g = kappa * lambda_g.

**Why it matters.** This is the single remaining gap in Theorem D. The uniform-weight lane is proved. The genus-1 statement is proved unconditionally. But W_N algebras are the physically interesting ones (higher-spin gravity), and the programme cannot make genus >= 2 predictions for them. Every attempt so far has been falsified (three proof attempts in the memory files, all three caught by the Beilinson principle). The gap is real: cyclic rigidity gives Theta^min = eta tensor Gamma_A but does NOT identify Gamma_A with kappa * Lambda.

**What would close it.** A direct genus-2 computation for W_3: enumerate the stable graphs, compute the graph amplitudes using the multi-channel propagator with R-dressed vertices, sum, and verify the answer equals kappa(W_3) * 7/5760. This is the "decisive path" identified in the multi-generator audit: compute first, then prove.

**Impact rating: 10/10.** Closes the last gap in the main theorem suite.

### 1.2 First-principles F_2 from stable graph sums

**What it is.** Compute the genus-2 free energy F_2 for sl_2 affine KM (or Heisenberg, or Virasoro) by enumerating all genus-2 stable graphs, computing the amplitude of each graph from OPE structure constants and propagators, summing over graphs, and verifying the result equals kappa * 7/5760.

**Why it matters.** This is the computation the programme has never done. F_1 = kappa/24 is proved abstractly but never derived from the genus-1 bar complex. F_2 has six contributing graph topologies at genus 2. Computing even one of them from first principles would be the first genuine higher-genus verification. Computing all six and getting the right answer would be devastating evidence for the programme.

**What would close it.** A compute module that: (a) enumerates genus-2 stable graphs with the correct symmetry factors, (b) assigns edge propagators (d log E(z,w)), (c) assigns vertex weights from OPE structure constants, (d) performs the graph integrals (which reduce to intersection numbers on M-bar_{2,n} by Mumford's formula), (e) sums and compares with kappa * B_4 / (4 * 4!). The key intermediate step is Faber's algorithm for tautological intersection numbers on M-bar_2.

**Impact rating: 10/10.** Transforms the programme from "proved existence" to "computed answer."

### 1.3 Explicit collision-residue R-matrix for sl_2

**What it is.** Construct Theta_A at genus 0, arity 2 from the bar-intrinsic definition (Theta_A := D_A - d_0), take the collision residue Res^coll_{0,2}(Theta_A), and verify the result equals Omega/z (the Casimir over z) for sl_2 affine Kac-Moody.

**Why it matters.** The identification r(z) = Res^coll_{0,2}(Theta_A) is stated as a theorem (the Yangian-shadow identification), but it has never been instantiated for any specific algebra. This single computation would verify that the abstract MC element, when you actually compute it, produces the known R-matrix. It would also give the DK-0 bridge concrete content.

**What would close it.** The computation is genuinely doable: at genus 0 and arity 2, the bar complex of V_k(sl_2) is small enough to write down explicitly. The differential D_A - d_0 at arity 2 involves only the quadratic bar component. The collision residue is a contour integral. The expected answer Omega/z = (sum e_a tensor e^a) / z is known.

**Impact rating: 9/10.** First instantiation of the central abstract identification.

### 1.4 Derived center computation for CS at integrable level

**What it is.** Compute C^bullet_ch(V_k(sl_2), V_k(sl_2)) (the chiral derived center / chiral Hochschild cochains) explicitly at an integrable level (say k=1), and verify the result matches the known center of the modular tensor category of V_1(sl_2)-modules.

**Why it matters.** The Swiss-cheese theorem (thm:thqg-swiss-cheese) proves abstractly that the chiral derived center is the universal bulk. But for CS gauge theory, the bulk is KNOWN independently (it is the center of the category of Wilson lines = the modular tensor category). Verifying agreement would give the derived-center-as-bulk identification its first concrete test. The raeeznotes113 audit identified this as "the key checkable computation the programme should perform."

**What would close it.** At k=1 for sl_2, the modular tensor category has k+1 = 2 simple objects (trivial and spin-1/2). The center has dimension 2. Computing C^bullet_ch(V_1(sl_2), V_1(sl_2)) requires understanding the chiral Hochschild complex, which is controlled by bar data. This is a hard but finite computation.

**Impact rating: 8/10.** First concrete verification of the bulk-boundary dictionary.

### 1.5 MCG-equivariance as a theorem (not a remark)

**What it is.** Prove that the genus-g amplitudes Z_g are invariant under the mapping class group action, as a theorem with a complete proof.

**Why it matters.** Currently this rests on a 3-line remark (rem:modular-invariance-tower). For a programme called "Modular Koszul Duality," the word "modular" should be backed by a theorem. The Segal agent found this as a SERIOUS gap: the construction defines Z_g by clutching, but never proves MCG-equivariance or compares with Segal's sewing axioms.

**What would close it.** The argument exists in outline: the bar-intrinsic construction uses D^2 = 0 on M-bar_{g,n}, which is MCG-invariant by construction. The formalization requires showing that the projection from D^2 = 0 to the amplitude Z_g preserves MCG-equivariance. This is a 2-page proof, not a research problem.

**Impact rating: 7/10.** Transforms the programme's central adjective from a slogan to a theorem.

---

## 2. The Three Biggest Computational Gaps

### 2.1 Zero first-principles verification at genus >= 1

**The gap.** Every numerical formula above genus 0 takes its answer as input. The compute layer has 468 test files, but at genus >= 1, they verify formulas against hardcoded expected values that were computed from the same formulas. The Feynman agent's three specific computations remain undone:

1. Compute kappa from d^2 on the torus (build genus-1 bar differential with Weierstrass zeta propagator, extract coefficient of Arnold defect, verify = c/2 * E_2(tau))
2. Compute the R-matrix from collision residue (construct Theta_A at genus 0 arity 2, take Res^coll, verify = Omega/z for sl_2)
3. Compute F_2 from the stable graph sum (enumerate 6 genus-2 graphs, compute amplitudes, sum, verify = kappa * 7/5760)

**How to fill it.** Write three new compute modules, each building the answer from OPE structure constants alone (not from the final formula). The key technical ingredient for #1 is the Weierstrass zeta function as genus-1 propagator. For #3, Faber's intersection-number algorithm on M-bar_2.

### 2.2 No explicit Theta_A ever constructed

**The gap.** The MC element Theta_A := D_A - d_0 is proved to exist (thm:mc2-bar-intrinsic) and is the protagonist of the entire monograph. But it has never been written down explicitly for any specific algebra, at any genus, at any arity. Not for Heisenberg. Not for sl_2 KM. Not for Virasoro. The object that "encodes the entire genus expansion" has never been instantiated.

**How to fill it.** Start with Heisenberg (the simplest case: class G, tower terminates at arity 2). At arity 2 and genus 0, Theta_A is a single tensor kappa tensor omega in Def_cyc. Write it down. Then do genus 0, arity 3 for sl_2 KM (class L, tower terminates at arity 3). Write down the cubic component. Then do genus 1, arity 2 for Heisenberg: verify the genus-1 obstruction is kappa * lambda_1. This chain of explicit instantiations would give the abstract theory concrete content.

### 2.3 Shadow tower coefficients S_r never computed from bar complex

**The gap.** The shadow tower coefficients S_3, S_4, S_5, ... are computed from the Riccati recursion (a genuine algebraic computation), which is correct. But they have never been independently verified by computing them from the bar complex definition: S_r should be extractable from Theta_A at arity r. The two computation paths (Riccati vs bar extraction) have never been compared.

**How to fill it.** For Virasoro at arity 3: compute the cubic shadow C from the bar complex (arity-3 bar cochains with structure constants, modulo gauge), and verify it matches S_3 = -24/(c(5c+22)) from the Riccati recursion. This would be the first cross-validation between the "shadow tower as recursion" and "shadow tower as bar projection" perspectives.

---

## 3. The Three Most Important Conjectures That Could Be Upgraded

### 3.1 conj:master-bv-brst (BV/BRST = bar at higher genus)

**Current status.** The identification BV/BRST = bar is proved at genus 0 (the original Swiss-cheese theorem) and at genus 1 (the curvature identification). At genus >= 2, it is conjectural.

**Why it could be upgraded.** The ingredients exist: the bar complex is a factorization coalgebra over the Feynman transform of the commutative modular operad (thm:bar-modular-operad). The BV/BRST differential is built from the same OPE data. The identification at genus 0 shows they agree on the generators. A general argument by induction on genus (using the clutching maps) should close this.

**What's needed.** A careful proof that the bar differential, expressed as a graph sum over stable graphs at genus g, matches the Feynman-diagrammatic BV differential at genus g. The key subtlety is the planted-forest corrections (delta_pf) at genus >= 2.

### 3.2 conj:operadic-complexity (shadow depth = A-infinity depth = L-infinity formality level)

**Current status.** Proved at arities 2, 3, 4 (prop:shadow-formality-low-arity). The full conjecture: r_max(A) equals the A-infinity depth (the smallest r such that all transferred A-infinity operations m_k for k > r vanish) equals the L-infinity formality level of the convolution algebra.

**Why it could be upgraded.** The low-arity proof works by explicit matching of the shadow tower obstruction classes with the formality obstruction classes. The pattern is clear. What's needed is a general argument that the arity-r shadow class o_r(A) in the cyclic deformation complex corresponds exactly to the A-infinity operation m_r under the homotopy transfer theorem. This is essentially an operadic comparison theorem.

**What's needed.** An explicit identification of the HTT-transferred m_r with the arity-r projection of Theta_A, at all arities. The low-arity proofs suggest the right framework; what's missing is the general inductive step.

### 3.3 conj:pixton-from-shadows (class-M algebras generate the Pixton ideal)

**Current status.** Computationally supported at genus 2-3. The conjecture: the infinite MC tower of a class-M algebra (Virasoro, W_N) produces tautological relations in the Chow ring of M-bar_g that generate the Pixton ideal (Pixton's relations, proved by Janda-Pandharipande-Pixton-Zvonkine to generate all relations among tautological classes).

**Why it could be upgraded.** At genus 2, the planted-forest correction delta_pf^{(2,0)} = S_3(10S_3 - kappa)/48 is proved. For Virasoro, this gives -(c-40)/48, which is a specific tautological relation. The question is whether the infinite tower of such relations (one at each genus, one at each arity) generates the Pixton ideal. The computational evidence (pixton_shadow_bridge.py, 75 tests) is positive.

**What's needed.** An explicit comparison between the genus-2 shadow relation and the genus-2 Pixton relation using the admcycles/sage framework. If they match, the conjecture gains strong evidence. If the shadow tower at genus 3 also matches, the pattern would be very compelling.

---

## 4. Structural Changes for Maximum Impact

### 4.1 Separate the proved core from the programme

**The problem.** The manuscript mixes 1,400 pages of proved theorems with programmatic assertions, frontier conjectures, and physical interpretations. A hostile referee cannot tell where the proofs end and the programme begins. The Beilinson agent's verdict: "The four-stage architecture creates an illusion of 75% completion."

**The fix.** The proved core (Theorems A-D+H, the Koszulness characterization programme, the shadow tower at finite order, the MC element existence) should be separated into a self-contained mathematical monograph that could stand alone as a submission to Asterisque. The frontier (holographic interpretations, non-perturbative completion, full modularity programme) should be in a separate volume or clearly demarcated final part. The current structure (interleaving proved and conjectural across 80+ files) makes the programme look less proved than it is.

### 4.2 Write a short paper (Inventiones-length) proving ONE thing

**The problem.** The monograph is 2,200+ pages. No referee will read it. The programme's strongest results (Theorem A + Theorem B + shadow tower at finite order, say) could be extracted into a 50-page paper that proves a single clean theorem. This paper would get the programme into the literature and force engagement.

**The candidate theorem.** "For any chirally Koszul chiral algebra A on a smooth projective curve X, the bar construction B(A) carries a natural modular Maurer-Cartan element Theta_A in the convolution dg Lie algebra, whose leading coefficient is kappa(A) * lambda_g at all genera (for uniform-weight A). The shadow Postnikov tower of Theta_A is algebraic of degree 2, with critical discriminant classifying shadow depth into four structural classes."

This is a complete theorem with a complete proof (all ingredients are proved in the current manuscript). It is new (no one has constructed the modular MC element for chiral algebras). It is checkable (the shadow tower has explicit formulas). It would be devastating.

### 4.3 Cut the scaffolding

**The problem.** The Dirac agent found that in foundations.tex alone, remarks outnumber theorems by 2.6:1. Across both volumes, there are hundreds of remarks restating the same insights, roadmap paragraphs that add no content, and "motivational" passages that a strong reader would find patronizing. The Chriss-Ginzburg principle demands that every object earn its place by solving a specific problem.

**The fix.** Every remark should either (a) state a mathematical fact that is not a theorem/proposition/lemma, (b) give a counterexample or edge case, or (c) connect the current construction to something specific in the literature. Remarks that restate the thesis ("this is the single organizing principle") should be deleted. The estimate: 20-30% of the current page count is scaffolding.

### 4.4 Reorganize examples around computations, not narratives

**The problem.** The example chapters are organized as narratives ("The Heisenberg Algebra," "Kac-Moody Algebras") that introduce background, state the classification, and then compute. A reader who wants to see a specific computation (e.g., kappa for W_3) has to navigate through 50+ pages of background.

**The fix.** Add a computational appendix or table that, for each algebra family, gives: (1) generators and OPE, (2) kappa and shadow depth, (3) Koszul dual, (4) shadow tower coefficients through arity 4, (5) complementarity data, (6) R-matrix at genus 0. The current landscape_census.tex partially does this, but it should be expanded into a definitive reference table with all computed invariants.

---

## 5. The Single Biggest Weakness

**The programme has never computed its central object from first principles at genus >= 1.**

The modular MC element Theta_A is the protagonist of 3,000+ pages across two volumes. It is proved to exist. Its projections (kappa, shadow tower, genus expansion) are named, classified, and discussed in exhaustive detail. But Theta_A has never been explicitly constructed for any specific algebra. The genus-1 free energy F_1 = kappa/24 is stated as a theorem, but the compute layer literally returns the input parameter. The genus-2 free energy F_2 = kappa * 7/5760 has never been derived from a graph sum.

This is not a weakness of the theory -- it is a weakness of the PRESENTATION. The theory predicts specific numbers. Those numbers can be computed from first principles (OPE structure constants + stable graph sums + intersection numbers). The computation has not been done. Until it is done, the programme is a machine that has been built but never turned on.

**What would fix it.** Three computations, in order of difficulty:

1. **Heisenberg F_1 from the genus-1 bar complex.** The simplest case. The genus-1 bar complex for Heisenberg has a single generator. The d^2 computation on the torus should produce k * E_2(tau), where k is the level. This is a 1-page computation that would take an afternoon.

2. **sl_2 R-matrix from collision residue.** Construct Theta_A at genus 0, arity 2 for V_k(sl_2). Take the collision residue. Get Omega/z. This is a 2-page computation.

3. **Heisenberg or sl_2 F_2 from stable graph sums.** Enumerate the genus-2 stable graphs. Compute each amplitude. Sum. Get kappa * 7/5760. This is a 5-page computation that would use Faber's intersection numbers.

These three computations, implemented as compute modules with tests, would transform the programme from "existence theorem" to "computational machine." They should be done before any further structural rewriting.

---

## 6. New Connections to Other Areas

### 6.1 Topological recursion (Eynard-Orantin)

**The connection.** The shadow tower recursion (the Riccati equation for the shadow generating function) should be a specialization of topological recursion. The cor:topological-recursion-mc-shadow already identifies EO recursion with the MC shadow, but this identification has not been worked out explicitly. A precise comparison with Eynard-Orantin's spectral curve formalism would connect the programme to a large body of literature in mathematical physics and enumerative geometry.

**What's needed.** Identify the spectral curve (y^2 = Q_L(t)) for each algebra family. Verify that the recursion kernel matches the shadow connection. Check that the Bergman kernel on the spectral curve reproduces the shadow propagator.

### 6.2 Geometric Langlands (at the factorization level)

**The connection.** The bar complex of V_k(g) is a factorization coalgebra on Ran(X). The factorization algebra of Beilinson-Drinfeld, at the critical level k = -h^v, produces the Feigin-Frenkel center Z(g-hat). The Langlands dual g^L appears because B(V_k(g)) should have Verdier dual B(V_{k^L}(g^L)) (a factorization-level Langlands duality). This is touched on in the derived_langlands.tex chapter but remains largely programmatic. A clean theorem identifying the Verdier dual of the bar complex with the Langlands-dual bar complex would be a major result.

**What's needed.** A precise statement and proof at the critical level. The critical-level Feigin-Frenkel center is well-understood. The bar complex at the critical level should degenerate in a way that makes the Langlands duality manifest.

### 6.3 Motivic periods and mixed Tate motives

**The connection.** The arithmetic_shadows.tex chapter develops an "arithmetic packet connection" but the motivic content remains underdeveloped. The shadow tower coefficients S_r for specific algebras are rational numbers with specific prime factorizations. These numbers should have motivic interpretations: the genus-1 amplitude involves periods of mixed Tate motives (E_2 is not a period of a pure motive, but E_2* is quasi-modular with mixed-Tate structure). The connection to Brown's work on mixed Tate motives and multiple zeta values is natural but unexplored.

**What's needed.** Compute the motivic weight of the shadow tower coefficients at genus 2 and 3. Verify against Brown's tables of motivic periods. This would connect the programme to arithmetic geometry in a concrete way.

### 6.4 Quantum error correction and holographic codes

**The connection.** The memory files mention a holographic-codes-from-Koszul-duality connection (G12: Koszulness = exact QEC). This is potentially very impactful given current interest in quantum information. The Knill-Laflamme conditions from Lagrangian isotropy, and shadow depth = redundancy channels, would connect modular Koszul duality to a hot area of mathematical physics.

**What's needed.** A short paper (not a chapter) extracting this connection. State it as: "The Koszulness characterization programme provides 10 equivalent conditions for exact quantum error correction in the holographic code associated to a chiral algebra."

### 6.5 Derived algebraic geometry and shifted symplectic structures

**The connection.** Theorem C (complementarity) says the genus-g obstructions decompose as complementary Lagrangians. This is naturally a statement about (-1)-shifted symplectic geometry in the sense of Pantev-Toen-Vaquie-Vezzosi. The shifted-symplectic upgrade is mentioned in the manuscript but not fully developed. A clean theorem identifying the complementarity decomposition with a Lagrangian intersection in a shifted-symplectic derived stack would connect the programme to the PTVV programme.

**What's needed.** Identify the shifted-symplectic structure on the derived moduli of A-modules. Show that the complementarity decomposition is a Lagrangian splitting in this structure. This would require checking the PTVV axioms against the bar complex data.

---

## 7. What Would Make This Programme Undeniable

### To a referee at Inventiones/JAMS:

**One thing:** A 50-page paper extracting the cleanest proved theorem (the modular MC element for chirally Koszul algebras, with explicit shadow tower, verified by independent computation at genus 2). The 2,200-page monograph is unpublishable as-is; the extracted paper would be.

### To a referee at Annals:

**Two things:** (1) The extracted paper, plus (2) a genuinely new mathematical consequence. The strongest candidate: the Pixton ideal generation (if conj:pixton-from-shadows can be upgraded). Showing that the MC tower of a Virasoro algebra generates all tautological relations on M-bar_g would be a major result in algebraic geometry that uses the chiral-algebraic machinery in an essential way.

### To Beilinson himself:

**Three things that are currently missing:**

1. **Functoriality.** The construction A --> Theta_A should be proved to be a functor from chirally Koszul algebras to MC elements in modular convolution algebras. The functorial properties are discussed but not packaged as a single clean theorem. A functor is stronger than a construction.

2. **Comparison.** The modular MC element should be compared with existing constructions: Costello-Gwilliam's factorization algebra quantization, Beilinson-Drinfeld's chiral algebras, Kontsevich's deformation quantization. The comparison would show that Theta_A is the SAME object seen from a different angle, not a new invention. The strongest comparison: at the critical level, the bar complex of V_{-h^v}(g) should recover the Feigin-Frenkel center via the Verdier dual -- this would connect the programme to geometric Langlands through a single computation.

3. **A computation that nobody else can do.** The programme claims to be a computational machine. What computation does it enable that cannot be done by other methods? The candidate: the genus-2 free energy F_2 for W_3, computed from the shadow tower with its multi-channel structure. No other framework can compute this (the string theory approach requires a 6-dimensional compactification; the direct CFT approach requires enumerating all states at weight 2 * (c/24 - 1) which is enormous). If the shadow tower gives F_2(W_3) as a closed-form rational function of c, that would be a prediction that nobody else can make.

### The honest summary:

The programme has built an extraordinarily powerful algebraic machine. The machine works (the proofs are correct). The machine is well-designed (the MC element is the right organizing principle). But the machine has never been turned on. It has never computed a number that was not already known. It has never made a prediction. It has never been compared with a competing framework. Until it does at least one of these things, the strongest possible referee will say: "This is an impressive construction. But what does it compute?"

The answer to "what does it compute?" exists -- it computes F_g for all standard families, it computes shadow tower coefficients, it computes R-matrices. But these computations have only been done at the FORMULA level (deriving formulas from the theory) and never at the NUMBER level (evaluating the formulas by an independent method and checking). The gap between "the theory predicts F_2 = kappa * 7/5760" and "we have computed F_2 = kappa * 7/5760 from a graph sum" is the gap between a blueprint and a building.

**The single action item that dominates all others: write the genus-2 graph sum compute module. Enumerate the six stable graph topologies. Assign propagators and vertices. Integrate. Sum. Get 7/5760. Then publish.**
