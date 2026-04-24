# kappa Stratification - Adversarial Attack Report

## 1. Serre-duality forced vanishing at odd d
PROVEN: For a proper smooth d-fold with trivial canonical bundle, Serre duality gives H^q(O_X)^vee = H^{d-q}(O_X), hence h^{0,q}=h^{0,d-q}; at odd d the signs (-1)^q and (-1)^{d-q} cancel. Serre alone is not enough: without omega_X = O_X it pairs O_X with omega_X, not the same Hodge column (Hartshorne III.7; cy_d_kappa_stratification, Serre lemma).

## 2. UTI scope vs kappa_ch(K3xE) = 0
PROVEN: The target definition gives kappa_ch(K3 x E)=0 by Kunneth: (1,1,1,1) has supertrace 1-1+1-1. PROVEN: the same source gives kappa_BKM(Phi_1)=5, so 2*kappa_BKM=10. Therefore UTI-3, read literally as kappa_ch = 2*kappa_BKM on K3-fibered Class A, is false. SCOPED: UTI-2 can survive only as K o Phi = 2*kappa_BKM with K not identified with raw odd-d Hodge supertrace. The sources are not clean: platonic section 4 still calls the numerical UTI-3 per-family verifiable, while cy_d_kappa_stratification explicitly separates kappa_ch from Borcherds specialization weight.

## 3. d=2 values (K3, STU, bielliptic)
PROVEN: K3 has column (1,0,1), so kappa_ch=2. PROVEN: bielliptic has (1,1,0), so kappa_ch=0. SCOPED GAP: none of the four requested sources defines an "STU surface"; they mention only an STU model inside K3-fibered Class A. If STU means the K3-fibered CY3 model, raw kappa_ch is 0 by odd-d Serre; if it means the K3 fibre, the value is 2. The report cannot honestly compute a missing surface.

## 4. Class A vs Class B precise criterion
SCOPED: Class A is operationally the K3-fibered CHL/Borcherds-denominator locus: diagonal K3 x E orbifolds plus STU, N in {1,2,3,4,6}, with kappa_BKM=c_N(0)/2 (Borcherds 1995/1998; Gritsenko 1999). PROVEN/SCOPED: Class B examples - quintic, C^3, conifold, local P^2 - have no such Borcherds product in the sources, so kappa_BKM is undefined and replacements are kappa_BCOV=chi/24 and shadow depth. HEURISTIC: as a CY3 classification this is still an automorphic-admissibility cut, not an intrinsic geometric taxonomy.

## 5. Six routes and the rho^{R_i} pentagon healing
SCOPED: The sources assert that the six routes are different constructions witnessing the same Phi_3(K3 x E) output, not six Phi applications. HEURISTIC: no route-by-route isomorphism proof or definition of rho^{R_i} is present in the four sources. Thus rho^{R_i} can only stratify generator-rank of constructions; it cannot rescue kappa_ch, which is route-independent and zero.

## Verdict
UTI is broken if it equates raw odd-d kappa_ch with 2*kappa_BKM; scoped only after renaming the invariant. Class A/B is principled automorphically but ad hoc geometrically. The pentagon healing is plausible bookkeeping until rho^{R_i} and the six isomorphisms are proved.
