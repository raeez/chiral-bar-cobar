# First-Principles Analysis Cache — Cross-Programme Reference

This file caches every first-principles investigation from the programme's git history.
For each wrong claim: what it gets RIGHT, what it gets WRONG, the correct relationship, and the confusion type.

## Confusion Type Taxonomy (21 types)

1. **part/whole** — individual term properties assumed for total
2. **scope error** — formula valid in restricted domain applied universally  
3. **specific/general** — coincidence elevated to law
4. **label/content** — theorem label on conjecture; same symbol for different objects
5. **native/derived** — derived structure attributed to native level
6. **mechanism error** — right conclusion, wrong proof
7. **positive/negative** — obstruction misread as enablement
8. **off-by-one** — systematic shift in formula
9. **conflation** — distinct objects/operations equated
10. **convention clash** — two normalizations coexisting silently
11. **construction/narration** — structural analogy stated as identification
12. **construction/functor** — different constructions confused with single functor
13. **chain/cohomology** — chain-level property confused with cohomological
14. **algebraic/topological** — two incarnations of same structure conflated
15. **level error** — category-level confused with algebra-level; j=0 with j>=1
16. **vacuous/meaningful** — tautology presented as result
17. **temporal** — status changed over time; old status persists
18. **hardcoded/symbolic** — fragile reference instead of label
19. **sandbox/reality** — agent sandbox illusion
20. **additive/multiplicative** — different algebraic operations confused
21. **necessary/sufficient** — necessary condition treated as sufficient

## I. Retracted Proofs (3)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 1 | {b_k, B^{(2)}} = 0 for each k individually | TOTAL {b, B^{(2)}} = 0 via Costello TCFT | Individual arity-k terms don't vanish for non-formal algebras | Cross-arity cancellation: {b_3, B^{(2)}} cancelled by {b_2, B^{(2)}} via Stasheff. Total vanishes by operadic d^2=0. | part/whole |
| 2 | Tsygan formality proves {b, B^{(2)}} = 0 | Tsygan formality is a real theorem | Wrong scope: applies to B^{(0)} = Connes B, not B^{(j>=1)} | B^{(0)} mixed complex axiom [b, B^{(0)}]=0 does NOT extend to B^{(j)} hierarchy. | scope error |
| 3 | kappa_BKM = kappa_ch + chi(O_fiber) universally | True for N=1 (K3 x E): 5 = 3 + 2 | Numerical coincidence for single case | Fails for all Z/NZ-orbifolds with N>=2. Correct: kappa_BKM = c_N(0)/2 (Borcherds weight theorem). | specific/general |

## II. Theorem Downgrades

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 4 | "Theorem: BV-BRST = bar of G(X)" for CY3 | Structural identification plausible | G(X) does not exist; cannot be theorem | \begin{conjecture}. 11+ instances fixed. AP-CY6/AP-CY14 | label/content |
| 5 | "Theorem: kappa_ch = chi(O_X) for all CY" | True for d=2 with h^{1,0}=0 | FALSE for odd d (Serre forces chi(O_X)=0) | kappa_ch = worldsheet anomaly; chi(O_X) = target-space. Coincide at d=2, diverge at d=3. AP-CY34 | scope error |
| 6 | 62 instances of "Theorem CY-A_3" | CY-A_3 now proved (inf-cat) | Before proof: unproved conjecture in theorem env | Mass rectification. Chain-level results remain conjectural. | temporal |

## III. Kappa Conflations (7 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 7 | Bare "kappa" (~100+ instances) | Each kappa is real | Without subscript, different kappas conflate | Four kappas: kappa_{ch,BKM,cat,fiber}. K3xE spectrum: {0,2,3,5,24}. AP113 | label/content |
| 8 | "kappa(K3xE) = 3 vs 5 contradiction" | Both values real | DIFFERENT kappas of DIFFERENT algebras | kappa_ch=3 (chiral), kappa_BKM=5 (Igusa). No contradiction. | conflation |
| 9 | "Algebraizations share kappa_cat" as meaningful | kappa_cat IS same | VACUOUS: kappa_cat is manifold invariant | Like "both share gravity." AP-CY55 | vacuous/meaningful |
| 10 | kappa_ch = Sigma(-1)^i dim HH_i | Gives a real invariant | Gives chi_top (=24 for K3), NOT kappa_ch (=2) | Correct: Hodge-filtered supertrace str_{F^0}(q^{L_0}). AP-CY36 | formula error |
| 11 | kappa_ch additive under fiber products | Additive under direct sums | NOT under fiber products | kappa_ch(K3xE)=3 but chi(O_{K3xE})=2*0=0. Additivity vs multiplicativity. | additive/multiplicative |

## IV. E_n Level Confusions (8 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 12 | Phi: CY_d-Cat -> E_2-ChirAlg (uniformly) | E_2 correct for d<=2 | WRONG at d>=3: output is E_1 | Must scope: n=2 for d<=2; n=1 for d>=3. FM43 | scope error |
| 13 | "E_2-chiral algebra" at d=3 for A itself | E_2 DOES appear at d=3 | Lives on Z(Rep^{E_1}(A)), NOT on A | A is E_1 native. E_2 is derived via center. AP-CY56 | native/derived |
| 14 | E_3 on HH of E_1 algebras (Deligne) | E_3 Deligne is real | Requires E_inf input, not E_1 | For E_1: only E_2 (Dunn: E_1 tensor E_2 = E_3, but input contributes E_1). AP153 | scope error |
| 15 | Two E_3 structures are the same | Both exist | Agree under formality only | Algebraic E_3 (Deligne) vs topological E_3 (Conf(R^3)). Physical content at chain level. AP154 | algebraic/topological |
| 16 | Miki from E_3 operad | Miki IS an S_3 permutation | Comes from CY torus Weyl group, not operad | Counterexample: k[x]/(x^2) is E_3, no Miki. AP-CY22 | specific/general |
| 17 | CY-B is "E_2-Koszul" uniformly | CY-B IS Koszul duality | d-DEPENDENT: E_2 at d=2, E_1 at d=3 | At d=3: E_1-Koszul on A, E_2 on center. AP-CY58 | scope error |
| 18 | Class M E_3 bar is infinite | Class M IS most complex | Cohomology is 6^g (Kunneth) | Chain: P(q)^{6g}. Cohomology: 6^g. AP-CY21/38 | chain/cohomology |
| 19 | SN bracket vanishes for all CY_3 | True for C^d with GL(d) | False for non-toric CY_3 | Two mechanisms: (a) operadic degree (universal), (b) GL(d)-invariant vanishing (toric). | specific/general |

## V. Object Conflations (9 types)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 20 | CoHA = E_1-chiral algebra | CoHA related to E_1-sector | CoHA is associative, not chiral | Connection via functor Phi, not identification. AP-CY7 | construction/identification |
| 21 | Drinfeld center = derived center | Both real | Three distinct objects conflated | Z(C) = category center. Z^der = Hochschild cochains. Z categorifies derived center. AP-CY4 | level error |
| 22 | Drinfeld center = categorified averaging | Related via factorization | Center CONSTRUCTS; averaging DESTROYS | E_1 ->^Z E_2 ->^{Sym} E_inf. AP-CY54 | construction/narration |
| 23 | Flop = Koszul dual | Both operations on CY | Flop preserves kappa; Koszul exchanges | kappa(A_X)=kappa(A_{X+}) for flop. kappa(A)+kappa(A^!)=K for Koszul. AP-CY10 | conflation |
| 24 | CoHA = bar complex | Both have char M(q) | CoHA is algebra; bar is coalgebra | SV theorem: CoHA ≅ Y^+. Bar encodes Y-multiplication. Character coincidence. | algebra/coalgebra |
| 25 | Spectral z = worldsheet z | Both called "z" | Different objects | Delta_z spectral: shift parameter. OPE z: insertion coordinate. AP-CY31 | label/content |
| 26 | Phi distinguishes three K3 algebras | Three algebras exist | Phi gives ONE output: H_Muk | BKM from Borcherds lift, Conway from Leech. Different constructions. AP-CY59 | construction/functor |
| 27 | Six routes = six Phi applications | Six routes are constructions | Six DIFFERENT constructions | Convergence = CY-C (conjectural). AP-CY60 | construction/functor |
| 28 | R(z) = (id tensor S) o Delta_z(1) | R from coproduct | Coproduct of vacuum = 1 tensor 1 by counit | Correct R via half-braiding sigma in Z(Rep). AP-CY25 | construction error |

## VI. Scope and Status Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 29 | 6d route bypasses CY-A_3 | Alternative approach | Each subproblem requires same data | Reorganises, doesn't resolve. AP-CY32 | reorganization/bypass |
| 30 | S_{ijk}=R_{ij}R_{ik}R_{jk} satisfies ZTE | R satisfies YBE | Pairwise != 3-particle consistency | Fails at O(kappa^2). S^{corr}=S+kappa^2*T exists. AP-CY30 | specific/general |
| 31 | Shadow class from non-formality alone | m_3!=0 necessary for >=L | Not sufficient | local P^2: m_3!=0 but class M (infinite). Must compute full tower. AP-CY12 | necessary/sufficient |
| 32 | Omega-background universal for CY_3 | Realizes E_1 for toric | Requires torus action | General mechanism: bracket degree 1-d. Omega-background: toric-specific. | specific/general |
| 33 | "CY frontier" (empty slogan) | Gap F_g^top - F_g^sh is real | "Frontier" says nothing | Computable via Borel resummation + KS wall-crossing. | label/content |

## VII. Formula and Computation Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 34 | MF(W): A^n->A^1 is CY_{n-1} | MF IS a CY category | CY dim is n-2, not n-1 | ADE in 2 vars: CY_0. Need 5 vars for CY_3. AP-CY17 | off-by-one |
| 35 | A-hat convergence radius = pi | A-hat IS relevant | Argument halved: (x/2)/sinh(x/2) | Radius = 2*pi. The /2 doubles the radius. AP-CY19 | mechanism error |
| 36 | phi_{0,1} c(-1)=1 vs c(-1)=2 | Both normalizations exist | Factor of 2 = kappa_ch(K3) propagated silently | State convention. K3 elliptic genus = 2*phi_{0,1}. AP-CY42 | convention clash |
| 37 | Verdier inverts sigma_2 for k^!=-k | k^!=-k IS correct | sigma_2 is even under h_i->-h_i | k^! from Shapovalov form transposition, not sigma_2 inversion. AP-CY26 | mechanism error |
| 38 | B-cycle i^2=1 instead of i^2=-1 | B-cycle integrals needed | Sign error gives |q|=1, kills convergence | Verify |q|<1 and Im(tau)>0 after B-cycle computation. FM24 | sign error |

## VIII. Process and Agent Errors

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 39 | Agent writes persist to disk | Written inside sandbox | Sandbox isolation | Verify with ls after agent completion. AP-CY27 | sandbox/reality |
| 40 | Agent writes to correct repo | Files written | Wrong volume's directory | Verify FULL PATH. AP-CY29 | path error |
| 41 | Agent test values independent | Tests pass | 10% tautological | Multi-path verification required. AP-CY49 | tautological verification |
| 42 | Docstring values correct | Code correct | Docstring fabricates for n>=4 | Verify EVERY numerical value against function output. AP-CY24 | code/documentation |

## IX. Cross-Volume Confusions

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| 43 | Bulk replace "arity"->"degree" | Rename intentional | Corrupts singularity, unitarity, etc. | 45 corruptions. Check compound words. FM42 | mechanical error |
| 44 | "shadow Postnikov tower" | Shadow tower is real | "Postnikov" is different concept | Correct: "obstruction tower" or "shadow tower" | terminology error |
| 45 | Part~IV hardcoded | Parts ARE numbered | Numbers change on restructuring | Use \ref{part:...}, never Part~N. AP-CY13 | hardcoded/symbolic |

## X. cy_to_chiral.tex Audit (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 46 | Class M E_3 bar cohomology is "infinite-dimensional" | d_4 survives for class M | Chain-level complex P(q)^{6g} is infinite, but cohomology is FINITE | dim H*(B^{E_3}(A)) = 6^g for class M (Kunneth: d_4 kills Lambda^0 and Lambda^3, leaving [0,3,3,0] per handle). AP-CY21/38 | chain/cohomology | cy_to_chiral.tex L3760, L3765 |
| 47 | "dim HH_0 = 2, dim HH_1 = 20, dim HH_2 = 2" (yielding -16) | Alternating sum = -16 is correct | Mislabeled: these are dim H*(Omega^p), not dim HH_i | HH_i uses homological grading (HH_0=22); the Hodge grading uses p (dim H*(Omega^0)=2). Both yield -16 under the correct alternating sum, but the labels were wrong. | label/content | cy_to_chiral.tex L69 |
| 48 | ClaimStatusConditional for class M E_3 bar genus result | Class M result WAS conditional | Now PROVED via Kunneth (6^g closed form) | Update status to ProvedHere for all classes including M. | temporal | cy_to_chiral.tex L3754-3755 |

## XI. en_factorization.tex Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 49 | K3 listed as CY_4 in Pontryagin class table | K3 has c_2=24, p_1=-48 | K3 is CY_2 (complex dim 2), NOT CY_4 | Removed row. K3 cannot appear in CY_4 landscape table. AP-CY1 | scope error | en_factorization.tex L309 |
| 50 | Verification note "AP-CY21: class M infinite" | Class M IS most complex shadow class | Class M E_3 bar = 6^g (FINITE); class G is the infinite one | Corrected to "class M is 6^g not (1+t)^{3g}". AP-CY21/38 | chain/cohomology | en_factorization.tex L2688 |

## XII. K3 Example Chapters Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 51 | "E_2-structure should come from Sp_4(Z)" (at d=3, no E_n scoping) | E_2 structure IS relevant at d=3 | At d=3, A is natively E_1; E_2 lives on Drinfeld center Z(Rep^{E_1}(A)), not on A | Fixed: clarified that E_2-braiding is on the Drinfeld center of the representation category, not on A itself. AP-CY56 | native/derived | k3_chiral_algebra.tex L35 |
| 52 | "CoHA is E_1-sector of G(X), which is CY-A_3" | CoHA/G(X) connection is real | G(X) requires CY-C (quantum group realization), NOT CY-A_3; CY-A_3 gives A_X, not G(X) | Fixed: CoHA as E_1-sector of G(X) requires Conjecture CY-C. CY-A_3 constructs A_X but not G(X). AP-CY7/AP-CY14 | label/content | k3_yangian_chapter.tex L1103 |
| 53 | kappa_BKM = h^{1,1}(K3)/4 = 20/4 = 5 | Numerically correct (5=5) | Misleading derivation: c_f(0)=10 comes from Jacobi form, not h^{1,1}/2 | Fixed: kappa_BKM = c_f(0)/2 = 10/2 = 5 with explicit AP-CY37 citation. Hodge number route obscures Borcherds weight theorem. | mechanism error | k3_chiral_algebra.tex L510 |
| 54 | "deeper identifications await CY-A_3" | CY-A_3 WAS open | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction) | Fixed: remaining obstructions are chain-level framing data (non-formal) and Vol I Borcherds-lift bridge, not CY-A_3 itself. | temporal | k3_yangian_chapter.tex L1347, L1380-1391 |
| 55 | Bare $\kappa$-diagnostic in verification note | kappa_bullet notation required | AP113 zero-tolerance: all kappa must be subscripted or use bullet | Fixed: $\kappa$-diagnostic -> $\kappa_\bullet$-diagnostic. | label/content | k3_yangian_chapter.tex L126 |

## XIII. Connection/Bridge Chapters Enforcement (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 56 | "predicted modular characteristic is kappa_ch = chi_top/24 (BCOV prediction)" as blanket statement for compact CY3 | BCOV prediction IS used for compact CY3 | Presents conjectural formula without noting chi_top/24 != chi(O_X) for CY3 | chi(O_X)=0 for ALL CY3 by Serre duality (AP-CY34). kappa_ch = chi_top/24 is BCOV *prediction* (conjectural), not established formula. Must mark as conjectural and note the distinction. | scope error | bar_cobar_bridge.tex L235 |
| 57 | "conditional on CY-A_3" in DMVV conjecture (bar_cobar_bridge.tex) | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction, April 2026) | Remaining conditionality: Vol I Borcherds-lift identification (AP-CY8) and motivic DT comparison, NOT CY-A_3. | temporal | bar_cobar_bridge.tex L749 |
| 58 | "conditional on CY-A_3" for K3xE Stokes-WC identification | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | A_{K3xE} now exists. Remaining conditionality: Vol I Borcherds-lift identification (AP-CY8) + infinite stitching of local conifold identifications. | temporal | modular_koszul_bridge.tex L581, L936, L964 |
| 59 | "conditional on CY-A_3" for Hochschild bridge at d=3 | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Conjecture remains (upgrading the categorical-to-chiral Hochschild map to d=3 requires more than inf-cat existence), but the CY-A_3 conditionality is resolved. The conjecture's remaining content: the PTVV shifted Poisson maps to genus-0 convolution bracket. | temporal | modular_koszul_bridge.tex L317 |
| 60 | Face 1 "Conjectured for d=3 (conditional on CY-A_3)" in seven-face status remark | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED; thm at L153 already has ProvedHere | Status remark stale: Face 1 is ProvedHere for both d=2 and d=3. | temporal | cy_holographic_datum_master.tex L859 |
| 61 | "CY_3 (conditional on CY-A_3)" paragraph header in holographic datum | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Updated header. The paragraph body already said "now follow from Theorem CY-A_3". Only the header was stale. | temporal | cy_holographic_datum_master.tex L245 |
| 62 | K3xE Hecke eigensheaf "conditional on CY-A_3" | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | A_{SxE} exists by CY-A_3. Remaining conditionality: factorization Phi(SxE) = Phi(S) tensor Phi(E) (not established) and the Hecke eigensheaf identification. | temporal | geometric_langlands.tex L257 |
| 63 | "d=3 analogue remains part of CY-A_3" in convolution algebra proof | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Updated: "now established by CY-A_3 (proved)". The convolution bracket pulls back at both d=2 and d=3. | temporal | modular_koszul_bridge.tex L42 |
| 64 | kappa_ch + kappa_ch' = 0 displayed without scoping | True for KM/free-field class | Virasoro: sum = 13, not 0. Free-field scoping buried in prose after display | Fixed: displayed formula now shows general conductor relation kappa_ch + kappa_ch' = rho*K with explicit family-dependent scoping. | scope error | bar_cobar_bridge.tex L196 |

| 65 | "conditional on CY-A_3" in genus expansion section of modular_trace.tex | CY-A_3 WAS the bottleneck for GW identification | CY-A_3 is now PROVED; A_X exists | Remaining conditionality: the comparison between shadow tower and B-model topological string at g>=2. At g=1, unconditionally proved via Vol I Theorem D. | temporal | modular_trace.tex L168 |
| 66 | "the tower is conditional on CY-A_3" for CY3 shadow tower | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED | Tower is now accessible via CY-A_3 (proved). BKM modularity constraints provide structural predictions independently. | temporal | modular_trace.tex L173 |

### Positive findings (no violations)

The following were checked and found correct across all five files:

- **AP113 (bare kappa)**: Zero violations. All kappa subscripted throughout all five files.
- **AP-CY4 (Drinfeld center vs derived center)**: Correctly distinguished in modular_koszul_bridge.tex Def 3.1 (three Hochschild theories), cy_holographic_datum_master.tex Rem rem:no-cobar-bulk-confusion, geometric_langlands.tex Iwahori passage.
- **AP-CY7 (CoHA != chiral)**: Correctly noted as associative in bar_cobar_bridge.tex L359 ("on the CY side, the CoHA..."), geometric_langlands.tex L90 (explicit AP-CY7 citation).
- **AP-CY8 (denominator != bar Euler)**: No bare identification. The modular_koszul_bridge.tex Igusa cusp form section (Thm thm:k3xe-shadow-cohft-igusa) explicitly notes the AP-CY8 proviso.
- **AP-CY10 (flop != Koszul)**: modular_trace.tex L178 correctly distinguishes complementarity (Koszul) from flop.
- **AP-CY12 (shadow class from full tower)**: bar_cobar_bridge.tex correctly computes shadow class for each CY3 example from the full tower data, not from non-formality alone.
- **AP-CY54 (Drinfeld center != averaging)**: geometric_langlands.tex correctly describes Drinfeld center via half-braidings/Iwahori passage, never calls it "averaging".
- **AP-CY55 (manifold vs algebraization invariants)**: modular_koszul_bridge.tex kappa-spectrum tables (L333-344, L251-252) correctly separate manifold invariants from algebraization invariants.
- **AP-CY56 (E_n level scoping)**: geometric_langlands.tex correctly uses E_2 only for d<=2, E_1 for d>=3. cy_holographic_datum_master.tex Face 1 d=3 correctly references E_1-chiral.
- **AP-CY57 (construction/narration)**: The seven-face chapter constructs each face explicitly, not by narration. Koszul duality is constructed through the bar-Verdier pipeline in modular_koszul_bridge.tex.
- **AP25 (bar != cobar != Koszul)**: bar_cobar_bridge.tex Remark 3.1 (three functors, three outputs) correctly distinguishes Omega(B(A))=A (inversion), D_Ran(B(A))=B(A^!) (Verdier/Koszul), Z^der_ch(A)=RHom (derived center).
- **Geometric Langlands, derived Satake**: All CONJECTURAL throughout geometric_langlands.tex. Every formal statement uses \begin{conjecture} except Feigin-Frenkel (ProvedElsewhere).
- **Part references**: No hardcoded Part~N references found in any of the five files.

## XIV. Theory + Examples Chapters Enforcement (2026-04-15, 11-file sweep)

Files audited: cy_categories.tex, cyclic_ainf.tex, hochschild_calculus.tex, quantum_groups_foundations.tex, braided_factorization.tex, toroidal_elliptic.tex, matrix_factorizations.tex, fukaya_categories.tex, quantum_group_reps.tex, derived_categories_cy.tex, k3e_cy3_programme.tex.

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 65 | kappa_cat(K3 x E) = 3 in kappa-spectrum remark | kappa_ch = 3 IS correct | kappa_cat = chi(O_{K3xE}) = 0 by Kunneth (2*0=0), NOT 3 | Fixed: kappa_cat = 0. The value 3 is kappa_ch (algebraization invariant). AP-CY55 | conflation | quantum_group_reps.tex L513 |
| 66 | kappa_cat = 1 for resolved conifold (d=3) | Chiral modular char IS 1 | At d=3, the chiral algebra output is kappa_ch, not kappa_cat | Fixed: kappa_ch = 1. | label/content | quantum_group_reps.tex L360 |
| 67 | kappa_cat(Phi(Fuk(X))) = chi(O_X) at d=3 conjecture | kappa_cat = chi(O_X) as manifold invariant | Phi produces kappa_ch, not kappa_cat. At d=3, kappa_ch != chi(O_X) (AP-CY34). | Fixed: kappa_ch = chi^{CY}(Fuk(X)), noting divergence at d=3. | scope error | fukaya_categories.tex L255 |
| 68 | kappa_cat = 0 as "predicted modular characteristic" of Phi for quintic | kappa_cat = 0 correct as manifold invariant | "Predicted" implies Phi output = kappa_ch, which may differ at d=3 | Fixed: separated kappa_cat from kappa_ch; noted d=3 programme. | label/content | fukaya_categories.tex L296 |
| 69 | kappa_cat = 1 for conifold in Fukaya chapter | Chiral modular char IS 1 | At d=3, chiral algebra output is kappa_ch | Fixed: kappa_ch = 1. | label/content | fukaya_categories.tex L307 |
| 70 | {kappa_cat,...} = {2, 3, 5, 24} for K3 x E | Individual values correct in isolation | kappa_cat(K3xE) = 0, NOT 2. The 2 is chi(O_{K3}) = kappa_cat of the fiber. | Fixed: {0, 3, 5, 24} with Kunneth. AP-CY55 | conflation | cyclic_ainf.tex L195 |
| 71 | "modular characteristic kappa_cat" depends on cyclic A_inf input | kappa_ch does depend on it via Phi | kappa_cat = chi(O_X) is manifold-invariant, independent of algebraization | Fixed: "chiral modular characteristic kappa_ch". AP-CY55 | vacuous/meaningful | cyclic_ainf.tex L4 |
| 72 | kappa_cat = 2 = chi(O_{K3}) in K3 x E BPS factorization context | chi(O_{K3}) = 2 correct for K3 fiber | Context is K3 x E; kappa_cat(K3xE) = 0 by Kunneth | Fixed: kappa_cat(K3xE) = 0; 2 is fiber value. AP-CY55 | conflation | braided_factorization.tex L1389 |
| 73 | "resulting chiral algebra is class M" (from CoHA directly) | Class M IS correct | Conflates CoHA (associative) with chiral algebra (via Phi). AP-CY7 | Fixed: CoHA is associative; Phi_3 output is class M. | construction/identification | derived_categories_cy.tex L256 |

### Verified Clean (no violations):

- **AP113**: All kappa subscripted in all 11 files.
- **AP-CY17**: MF(W) dim = n-2 correct with explicit citations.
- **AP-CY1**: cyclic_ainf.tex L80 explicitly warns d = complex dim, not real dim 2n.
- **AP-CY2**: CY class in HC^-_d with AP-CY2 citation.
- **AP-CY5**: KL root-of-unity correctly required.
- **AP-CY7**: CoHA correctly labeled associative, not chiral.
- **AP-CY10**: Flop/Koszul correctly distinguished.
- **AP-CY13**: Zero hardcoded Part~N references.
- **AP152**: "ordered product" disambiguated by context.
- **AP160**: Hochschild convention note present.
- **pi_3(BU)=0**: Correctly stated with Bott periodicity derivation.
- **E_n scoping**: Correctly scoped throughout (E_2 at d=2, E_1 at d=3).
- **CY-C**: All \begin{conjecture}, never \begin{theorem}.

### First-principles verification: kappa_cat(K3 x E) = 0

chi(O_{K3xE}) = sum_q (-1)^q h^{0,q}(K3 x E). Kunneth: h^{0,q}(K3 x E) = sum_{a+b=q} h^{0,a}(K3) h^{0,b}(E). K3: (h^{0,0}, h^{0,1}, h^{0,2}) = (1, 0, 1). E: (h^{0,0}, h^{0,1}) = (1, 1). Product: (1, 1, 1, 1). chi = 1-1+1-1 = 0. Equivalently chi(O_{K3}) chi(O_E) = 2*0 = 0.

## XV. Vol I Archaeology (cross-programme, from git history)

| # | Wrong Claim | Ghost Theorem | Error | Correct | Type |
|---|-------------|---------------|-------|---------|------|
| 76 | B(A) is SC-coalgebra | B(A) IS coalgebra | E_1 not SC | SC on derived center pair | object/structure |
| 77 | SC=E_3 | Related | SC+conformal=E_3-TOP | generic/special |
| 78 | r(z)=Omega/z bare | Proportional | Missing k. 90+ instances | specific/general |
| 79 | kappa=c/2 universal | Virasoro | Heis:k, KM:dim(g)(k+h^v)/(2h^v) | specific/general |
| 80 | av(r)=kappa non-abelian | Abelian | kappa=av(r)+dim(g)/2 | abelian/non-abelian |
| 81 | r^Vir=(c/2)/z^4 | Quartic pole | d-log: p->p-1. r=(c/2)/z^3+2T/z | OPE/r-matrix |
| 82 | S_4=-(5c+22)/(10c) | Correct symbols | Reciprocal. 10/[c(5c+22)] | reciprocal |
| 83 | kappa+kappa'=0 universal | KM/Heis/free | Vir:13, BP:98/3. Family-dependent | specific/general |
| 84 | Bar-cobar=bulk | Fundamental | Omega(B(A))~A inversion. Bulk=HH | four-object |
| 85 | E_3 derived center for E_1 | For E_inf (HDC) | E_1: only E_2 | input/output scope |
| 86 | Algebraic E_3=topological E_3 | Both exist | Agree formality; diverge chain | two-structure |
| 87 | Bare "Hochschild" | 3 theories | topological/chiral/categorical | three-object |
| 88 | 4 Yangians interchangeable | All Yangians | classical/dg/chiral/spectral | four-object |
| 89 | SC Koszul self-dual | SC IS Koszul | SC^!=(Lie^c,Ass^c) != SC | functor/object |
| 90 | A^! is SC-algebra | Dual operad | SC^!=(Lie,Ass) not SC=(Com,Ass) | algebra/coalgebra |
| 91 | d_alg(Vir)=3 | d_gen=3 | d_alg=infinity (class M) | two-depth |
| 92 | omega_g=d*tau | Both exist | d*tau fiber; c_1(lambda) moduli | fiber/base |
| 93 | Arnold=connection form | Arnold fundamental | Arnold=bar coeff. KZ=r(z)dz | form-type |
| 94 | obs_g=kappa*lambda_g universal | g=1+uniform | g>=2: cross-channel corrections | specific/general |
| 95 | B(A)=T^c(s^{-1}A) full | Desuspended | Augmentation ideal A-bar | augmentation/full |
| 96 | |s^{-1}v|=|v|+1 | Shifting | LOWERS: |v|-1 | suspension/desuspension |
| 97 | m_1^2=0 curved A-inf | Flat | Curved: m_1^2=[m_0,a] | flat/curved |
| 98 | CE=chiral bar multi-gen | Single-gen | Orlik-Solomon. sl_3: 36 vs 20 | algebraic/geometric |
| 99 | ChirHoch free polynomial | Polynomial Hilbert | z^2!=0 but ChirHoch^4=0 | A_inf/cup-product |
| 100 | E_8 fund=779247 | Large irreps | Adjoint=248 | confabulated |
| 101 | g=2 stable graphs=6 | Several | 7 not 6 | off-by-one |
| 102 | 1/eta^2=triangular | Simple expansion | Bicoloured partitions | sequence family |
| 103 | S_2=c/12 Vir | lambda-bracket | S_2=kappa=c/2 | shadow/OPE |
| 104 | K_BP=2 | Conductor exists | K_BP=196 | local/global |
| 105 | kappa(BP)+kappa(BP^!)=1/3 | Rational | 98/3 | numerical factor |

## XVI. Vol II Archaeology (cross-programme, from git history)

| # | Wrong Claim | Ghost Theorem | Error | Correct | Type |
|---|-------------|---------------|-------|---------|------|
| 106 | Dunn E_1xE_1=E_2 on A | Dunn real | On Z(A)/Mod_A not A | native/derived |
| 107 | R-matrix promotes A E_1->E_2 | R braiding | On Mod_A. Rep E_2 | native/derived |
| 108 | ALL VAs not E_inf | Poles | ALL VAs ARE E_inf | label/content |
| 109 | E_inf=no poles | BD subclass | E_inf=LOCAL | specific/general |
| 110 | B(A)=int_R A | Related FH | int_R A=A. B=int_{[0,1]} | construction/narration |
| 111 | Deconc=chiral coproduct | Both | DIFFERENT objects | algebra/coalgebra |
| 112 | E_inf->E_3 automatic | E_2 automatic | E_3 needs 3d HT | automatic/constructed |
| 113 | Bar degree=E_1 direction | Grading | Grading != operadic | label/content |
| 114 | Y_z^hbar(g) | Y_hbar(g) | z on structures not algebra. 531 | label/content |
| 115 | {T_lam T}=(c/2)lam^3 | OPE coeff | (c/12)lam^3. Factor 1/3! | convention |
| 116 | S_2=c/12 | lambda-bracket | S_2=kappa=c/2 | shadow/OPE |
| 117 | Vir m_3 formula errors | Computable | Wrong coefficients | arithmetic |
| 118 | betaGamma/bc swapped | Both exist | Sign flip. 16 corrections | convention/sign |
| 119 | W_N collapse E_4 | SS collapses | E_{2N} for N>=3 | arithmetic |
| 120 | N=4 k'=-k-2 | Dual exists | k'=-k-4. h^v=2 | arithmetic |
| 121 | FP lambda_2=1/1152 | Value exists | 7/5760. Shared wrong derivation | arithmetic |
| 122 | Heis trivial braiding | Simple | R=exp(k*hbar/z) NOT trivial | specific/general |
| 123 | J(z)J(w)~1/(z-w) | OPE | DOUBLE pole: k/(z-w)^2 | arithmetic |
| 124 | d_alg(Vir)=1 | Has depth | d_alg=inf. d_gen=1 | two-depth |
| 125 | self-dual=critical | Both special | c*=13 != c_crit=26 | label/content |
| 126 | Formality failure=defect | Fails d'=1 | IS the feature | label/content |
| 127 | kappa/S_2 interchangeable | Related | Only Vir/Heis | specific/general |
| 128 | W(2)=(betaGamma)^{Z/2} | Z/2 orbifold | Symplectic fermion c=-2 | wrong parent |
| 129 | Agent composite confabulation | Each real | Composite unconstructed | confabulation |
| 130 | Engine+test same wrong | Both agree | Shared wrong model | tautological |
| 131 | Spectral R(z)=categorical braiding | Both encode | Family with z vs single nat trans | specific/general |
| 132 | B^FG=B^Sigma=B^ord | All bar | DIFFERENT: ord->Sigma->FG | three-object |
| 133 | PVA=P_inf | Both | OPPOSITE: descend vs ascend | construction/narration |
| 134 | SC bar on R x C | Involves | Product operad. Needs Deligne-Tamarkin | construction/narration |
| 135 | Within-surface E_1+transverse independent | Two E_1s | Koszul dual via Hom | construction/narration |
| 136 | RT from E_1 ordered | RT exists | E_inf FH (CFG) | specific/general |
| 137 | Two Yangian defs equivalent | Both | RTT weaker than quadruple | weak/strong |
| 138 | Miura coefficient 1/Psi | Involves | (Psi-1)/Psi. Accidental at Psi=2 | accidental agreement |

## XVI. k3e_cy3_programme.tex Deep Enforcement (2026-04-15, second pass, 3391 lines)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 139 | kappa_cat(K3) = 2 = chi(O_{K3}) described as "the arithmetic genus" probing K3 x E | chi(O_{K3}) = 2 IS correct for K3 fiber | In context of K3 x E kappa-spectrum, value 2 is kappa_ch(A_{K3}) (algebraization invariant), NOT kappa_cat (manifold invariant of K3 x E). kappa_cat(K3 x E) = 0 by Kunneth. | Fixed: replaced with "kappa_ch(A_{K3}) = 2 is the K3 sigma model modular characteristic (an algebraization invariant, not a manifold invariant; cf. AP-CY55)". | conflation | k3e_cy3_programme.tex L1777 |
| 140 | Table column header "kappa_ch" covers row with kappa_BKM = 5 | kappa_BKM = 5 IS correct | Table mixes kappa_ch (rows 1-2) and kappa_BKM (row 3) under single kappa_ch column header. AP113 violation. | Fixed: column header changed to kappa_bullet, each row now has explicit subscript (kappa_ch or kappa_BKM). | label/content | k3e_cy3_programme.tex L965, L973 |
| 141 | "conditional on CY-A_3 for the existence of A_{K3 x E}" | CY-A_3 WAS the bottleneck | CY-A_3 is now PROVED (inf-cat, thm:derived-framing-obstruction). A_{K3 x E} exists. | Fixed: updated to cite CY-A_3 as proved; remaining conjecture content is the factorisation structure and shadow correction identification. | temporal | k3e_cy3_programme.tex L3236-3237 |
| 142 | Conjecture: kappa_BKM = kappa_ch(S) + kappa_ch(S x E) universally for S x E | True for N=1 (5 = 2+3) | PROVED FALSE for Z/NZ-orbifolds N>=2 by kappa_bkm_adversarial.py (62 tests). AP-CY37. | Fixed: downgraded from conjecture to remark noting this is a numerical coincidence for N=1; correct universal formula is kappa_BKM = c_N(0)/2 (Borcherds weight theorem). | specific/general | k3e_cy3_programme.tex L2172-2189 |
| 143 | Programme C asks "Does kappa_BKM = kappa_ch(surface) + kappa_ch(CY_3) hold?" as open | Was open at time of writing | Already answered NEGATIVELY for N>=2. Correct universal: kappa_BKM = c_N(0)/2. | Fixed: restated as answered (fails for N>=2), cited adversarial engine and AP-CY37. For non-K3-fibered CY3: kappa_BKM undefined. | temporal | k3e_cy3_programme.tex L2130-2136 |

### Verified Clean (no violations in k3e_cy3_programme.tex):

- **AP113 (bare kappa)**: Zero violations. All kappa subscripted throughout the entire 3391-line file.
- **AP-CY7 (CoHA != chiral)**: L18 explicitly parenthetically notes "AP-CY7: the CoHA is associative, not chiral; the passage to a chiral algebra requires the functor Phi".
- **AP-CY8 (denominator != bar Euler)**: L697 reference to "twined bar Euler product" is observational (eta product decomposition), not claiming bare identification.
- **AP-CY10 (flop != Koszul)**: No flop/Koszul conflation found.
- **AP-CY4 (Drinfeld center != derived center)**: L840-841 correctly distinguishes derived centre from Koszul dual ("the universal bulk is a separate object from A^!").
- **AP-CY12 (shadow class from full tower)**: L399-452 computes shadow class M from full tower through degree 12, not from non-formality alone.
- **AP-CY13 (Part references)**: Zero hardcoded Part~N references.
- **AP-CY17 (MF CY dim)**: No matrix factorization claims in this file.
- **AP-CY34 (kappa_ch != chi(O_X) at odd d)**: No bare kappa_ch = chi(O_X) claim outside d=2 scope.
- **AP-CY37 (kappa_BKM decomposition)**: Proposition prop:kappa-bps-decomposition (L1808-1867) correctly identifies the decomposition as a "numerical coincidence" specific to N=1, cites adversarial engine. The conjecture and Programme C question (violations 142, 143) were the exceptions, now fixed.
- **AP-CY55 (manifold vs algebraization invariants)**: kappa-spectrum table (L1754-1781) correctly uses kappa_ch for algebraization invariants; the one exception (L1777 using kappa_cat(K3) for a value in the spectrum) was fixed (violation 139).
- **AP-CY56 (E_n scoping at d=3)**: No unscoped E_2-chiral claims at d=3 found. The file primarily discusses d=2 (K3 sigma model).
- **AP-CY59 (multiple algebraizations)**: L1758-1759 explicitly cites "AP-CY59: only the chiral de Rham complex comes from Phi".
- **AP-CY60 (six routes)**: No six-routes discussion in this file.
- **AP24 (kappa+kappa'=0)**: L829 correctly scoped to "free-field/CY sigma models"; L1356 correctly scoped to "free fields".
- **All theorems**: The 5 \begin{theorem} environments all carry \ClaimStatusProvedElsewhere or \ClaimStatusProvedHere. All conjectures use \begin{conjecture} with \ClaimStatusConjectured.
- **Convention**: phi_{0,1} normalization at L466-477 explicitly uses Eichler-Zagier convention with Z_{K3} = 2*phi_{0,1} and phi_{0,1}(tau,0) = 12, and the factor of 2 = kappa_ch(K3) is identified at L551-579 (AP-CY42 compliant).
- **BKM universal formula**: kappa_BKM = c_0(0)/2 = 10/2 = 5 correctly stated at L1816-1821 and L3119-3120 via Borcherds weight theorem, with explicit citation of prop:bkm-weight-universal.

## XVIII. toroidal_elliptic.tex Deep Pass (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 144 | kappa_ch = rank(Lambda) for lattice VOA | Bar curvature = rank*level | Conflates kappa_ch with kappa_fiber in CY context | kappa_ch(K3)=2 (algebraization); kappa_fiber=24 (lattice rank). For abstract rank-r Heis at level k: curvature=rk | kappa conflation | toroidal_elliptic.tex L437 |
| 145 | kappa_ch(A_E) = 24 "(rank of free-boson lattice)" | Central charge of boundary algebra IS 24 | Parenthetical describes kappa_fiber not kappa_ch | 24 = central charge of A_E = kappa_fiber. kappa_ch(K3)=2. Coincidence at level 1 | kappa conflation | toroidal_elliptic.tex L1526 |
| 146 | Two hbar conventions without bridge (hbar_1,hbar_2 vs plain hbar) | Both conventions valid | No explicit bridge identity connecting them | Need: q=e^{hbar_1}, t=e^{-hbar_2}; rational limit hbar=hbar_1 | convention clash | toroidal_elliptic.tex L402 vs L1440 |
| 147 | chi(K3)=24 bare without chi_top subscript | chi_top(K3)=24 correct | Bare chi risks confusion with chi(O_{K3})=2 in kappa context | Use chi_top(K3)=24 or dim H*(K3)=24 explicitly | label/content | toroidal_elliptic.tex L1515 |
| 148 | vartheta_1 vs theta_1 notation inconsistency | Same function | Notation switch mid-file | Harmonize to theta_1 throughout | convention | toroidal_elliptic.tex L131 vs L506+ |

## XIX. Vol I Examples, Connections, and Standalone Papers Enforcement (2026-04-15)

Comprehensive sweep of 27 example chapters, 21 connection chapters, and 50+ standalone papers against the first-principles protocol. Focused on the key violation types from the 100-entry Vol I archaeology.

### Fix applied

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 149 | "Summary of Part~IV" chapter title for landscape census | landscape_census IS a Part summary | File lives in Part III (The Standard Landscape, L1182-1389 of main.tex), NOT Part IV (Physics Bridges, L1390+) | Fixed: Part~IV -> Part~\ref{part:standard-landscape}. AP-CY13 stale Part reference. | hardcoded/symbolic | landscape_census.tex L1-3 |

### Verified clean: r(z) = k*Omega/z (entry 84)

All 39 instances of r(z) = k*Omega/z across examples, connections, and standalone papers carry the level prefix k. Zero bare Omega/z violations found. Files checked: lattice_foundations.tex (3 instances), yangians_foundations.tex (4), yangians_drinfeld_kohno.tex (6), genre_expansions.tex (1 comment), five_theorems_modular_koszul.tex, drinfeld_kohno_bridge.tex (3), shadow_towers_v3.tex (2), en_chiral_operadic_circle.tex (1), ordered_chiral_homology.tex (3), N2_mc3_all_types.tex (1), koszulness_fourteen_characterizations.tex (2), e1_primacy_ordered_bar.tex (1), frontier_modular_holography_platonic.tex (2), en_koszul_duality.tex (1), e1_modular_koszul.tex (1), algebraic_foundations.tex (1). All carry k*Omega/z with explicit level prefix.

### Verified clean: kappa = c/2 Virasoro only (entry 87)

All ~60 instances of kappa = c/2 across the three directories are correctly scoped to Virasoro contexts. Key patterns:
- w_algebras.tex L2158 explicitly states "kappa = c/2 for Virasoro, kappa = 5c/6 for W_3" with a scoping preamble.
- N6_shadow_formality.tex L425-426 explicitly warns "kappa=c/2 holds only for Virasoro, not universally."
- garland_lepowsky.tex L856 explicitly says "The formula kappa = c/2 applies to the Virasoro algebra."
- three_dimensional_quantum_gravity.tex: all instances in Virasoro-specific paper (about Vir_c).
- virasoro_r_matrix.tex: all instances in Virasoro-specific paper.
- bp_self_duality.tex L389: explicitly labeled "with kappa = c/2" in Virasoro context.

### Verified clean: kappa + kappa' family-dependent (entry 113)

All instances of kappa + kappa' are correctly scoped:
- landscape_census.tex L1076: "kappa + kappa' = 0" explicitly for Heisenberg/KM (footnote context).
- landscape_census.tex L1284: "kappa(A) + kappa(A^!) = 0" explicitly for free fields.
- landscape_census.tex L3732-3744: "kappa + kappa' = 0" for affine KM, immediately followed by "For W-algebras, kappa + kappa' != 0: = 13 for Virasoro and 250/3 for W_3."
- bv_brst.tex L772, L797, L871: all scoped to "Virasoro branch where kappa + kappa' = 13".
- moonshine.tex L57, L78: "kappa + kappa' = 13" scoped to Virasoro sector.
- bershadsky_polyakov.tex L66: "kappa + kappa' = 98/3 (W-type)" -- correctly non-zero, non-Virasoro.
- w_algebras_deep.tex: table and prose correctly distinguish 0 (KM-type) from non-zero (W-type).
- five_theorems_modular_koszul.tex L101-102: "kappa(A) + kappa(A^!) family-dependent: 0 for KM and free fields, 13 for Virasoro." Correct.

### Verified clean: Bar-cobar = inversion, NOT Koszul (entry 98)

All ~40 instances use "bar-cobar inversion" or "bar-cobar quasi-isomorphism" (Omega(B(A)) ~ A), correctly distinguished from Koszul duality (A -> A^!). Key anchors:
- introduction_full_survey.tex L5400 explicitly states: "Omega(B(A)) recovers A (bar-cobar inversion, not duality); A^! is obtained by Verdier/linear duality, not cobar."
- five_theorems_modular_koszul.tex: Theorem B is "bar-cobar inversion", separate from Theorem C (complementarity/Koszul pairing).
- e1_primacy_ordered_bar.tex L254: four objects clearly enumerated (B(A) = bar coalgebra, A^i = H*(B(A)), A^! = (A^i)^v, Z^der_ch(A) = derived center).
- deformation_quantization.tex L815: "bar-cobar adjunction, restricted to formal disk at genus 0, recovers classical Koszul duality" -- correct scoping.

### Verified clean: Arnold = bar coefficient (entry 111)

Arnold relations appear correctly as bar-complex coefficient relations (d^2=0 from wedge products of d-log forms), NOT as connection forms. Key anchor: arnold_relations.tex appendix (L16) correctly describes Arnold relations as running through "Kontsevich formality (configuration space integrals satisfying d^2=0 via Arnold relations), Beilinson-Drinfeld (Arnold relations in the chiral bar construction), Costello-Gwilliam (Arnold relations as locality in factorization algebras)." No conflation with connection forms.

### Verified clean: CE != chiral bar for multi-generator (entry 120)

Zero CE = chiral bar conflations found. Survey papers correctly say "Chevalley-Eilenberg complex as a restricted bar construction" (restricted, not equal). The garland_lepowsky.tex standalone correctly handles the single-generator (KM) case where CE IS the bar complex via PBW filtration. The W-algebra chapters (w_algebras.tex, w_algebras_deep.tex) correctly note the multi-generator bar has Orlik-Solomon-type relations beyond CE.

### Verified clean: eta = q^{1/24}*prod (entry 94)

All 18 instances of eta(tau) definition include the q^{1/24} prefactor. No bare product-only definition found. Key anchors: theta_functions.tex appendix, heisenberg_eisenstein.tex L386, lattice_foundations.tex L1589, analytic_sewing.tex L398, five_theorems_modular_koszul.tex L1388.

### Verified clean: S_2 = kappa = c/2, NOT c/12 (entry 128)

Zero instances of S_2 = c/12 or kappa = c/12 found across all three directories. All S_2 references use S_2 = kappa.

### Verified clean: B(A) is E_1 NOT SC (entry 80)

The en_koszul_duality.tex L1278 has an explicit index entry: "bar complex!is E1 coassociative, NOT SC." The e1_primacy_ordered_bar.tex builds the entire paper around B^ord being E_1. No SC conflation found in examples, connections, or standalone.

### Verified clean: SC^{ch,top} != E_3 (entry 81)

en_koszul_duality.tex L2939 has a comment clarifying "SC^{ch,top} + SUGAWARA = E_3" (the distinction that SC alone is not E_3). introduction.tex L2240 correctly states "topologization SC^{ch,top} + T_Sug => E_3." No bare SC = E_3 conflation.

### Verified clean: Three bars B^ord != B^Sigma != B^FG (entry 194/132)

e1_primacy_ordered_bar.tex (the entire paper) is built on this distinction, with explicit macros \Barord, \BarSig, \Barch. landscape_census.tex L3136 mentions "three bar complexes" correctly. No conflation found.

### Verified clean: ChirHoch NOT free polynomial (entry 122)

The only "free polynomial algebra" claim for ChirHoch is survey_modular_koszul_duality_v2.tex L1795-1796, which correctly qualifies: "is a free polynomial algebra (conditional on Massey vanishing from FM formality)." The chiral_koszul_pairs.tex L2388-2391 remark explicitly states: "A further identification of ChirHoch*(A) as a free polynomial algebra is conditional on a Massey-vanishing consequence of Fulton-MacPherson formality and is not used in the equivalence core." No unqualified claims.

### Verified clean: obs_g = kappa*lambda_g at g=1+uniform only (entry 112)

All instances of obs_g = kappa*lambda_g carry "(UNIFORM-WEIGHT)" qualification or are explicitly at g=1. Key anchors: w_algebras.tex L2257, genus_expansions.tex L43, kac_moody.tex L203. No unqualified all-genera claims.

### Verified clean: d_alg != d_gen (entry 108)

No conflation found. The classification_trichotomy.tex standalone paper is specifically about distinguishing the three invariants (p_max, k_max, r_max) and explicitly warns against conflation.

### Verified clean: Four Yangians (AP159)

No "all four Yangians are the same" or equivalent conflation found. yangians_foundations.tex distinguishes RTT, Drinfeld, and other presentations. yangians_drinfeld_kohno.tex builds explicit bridges between specific presentations without claiming identity.

### Verified clean: Bare "Hochschild" (AP160)

No unqualified "Hochschild" found in standalone papers. All instances carry a qualifier (cohomology, cochains, complex, etc.).

### Verified clean: Part references (AP-CY13)

Zero hardcoded Part~N references in chapters/connections/ or standalone/ (only Part~\ref{...} symbolic references and proof-part labels like Part~(i)). The sole violation was in landscape_census.tex (fixed above).

### Summary statistics

- **Files scanned**: 27 example chapters + 21 connection chapters + 50+ standalone papers = ~100 .tex files
- **Total violations found**: 1 (stale Part~IV reference in landscape_census.tex)
- **Violations fixed**: 1
- **Clean verifications**: 16 categories checked, all clean
- **Assessment**: Vol I examples, connections, and standalone papers are in excellent shape. The 100-entry archaeology from earlier sessions has been comprehensively enforced. The remaining violation was a mechanical hardcoded Part reference (AP-CY13), not a conceptual error.

## XX. working_notes.tex Deep Audit (2026-04-15, 8930 lines)

The working notes file is the programme's intellectual diary: 35+ sections covering the 1-form, five theorems, shadow tower, quadratic extension, Koszul-Epstein frontier, gravitational coproduct, and honest scope assessment. The file is remarkably self-correcting -- it contains explicit Beilinson passes that identify and dismiss false claims. The following findings record the verified clean patterns and the few residual issues.

### Verified Clean (no violations in working_notes.tex):

- **Entry 84 (r(z)=k*Omega/z)**: L1501 correctly writes "r(z) = k\,\Omega_\fg/z" with explicit level k. The Virasoro r-matrix at L1505 is "(c/2)/z^3 + 2T/z" -- correct (not (c/12)/z^3). All r-matrix formulas carry the level parameter.
- **Entry 87 (kappa=c/2 Virasoro ONLY)**: L2010 writes "kappa = c/2" in explicit Virasoro context. L724-728 computes kappa_matter = 26*(1/2) = 13 for 26 free bosons at k=1/2. The Heisenberg formula kappa=k (not c/2) is at L5011. The N=2 formula kappa=(k+4)/4 from Kazama-Suzuki at L2517 is correctly different from c/2.
- **Entry 90 (S_4 reciprocal)**: L1022-1023 correctly writes "Q^{ct}_{Vir} = 10/[c(5c+22)]" -- the correct reciprocal, not -(5c+22)/(10c).
- **Entry 113 (kappa+kappa'=K family-dependent)**: L2887-2888 correctly scopes: kappa+kappa'=0 for KM, kappa+kappa'=13 for Virasoro, kappa+kappa'=1 for N=2. The table at L2880 makes the family dependence explicit. L8119 explicitly cites AP24.
- **Entry 112 (obs_g = kappa*lambda_g at g=1+uniform ONLY)**: L391-393 correctly states "At genus 1 the formula F_1=kappa/24 holds unconditionally for all families; at g>=2 for multi-weight algebras it remains open (op:multi-generator-universality)." L4296-4308 repeats the qualification.
- **Entry 108 (d_alg != d_gen)**: The four-class table at L944-949 uses r_max (shadow depth), not d_alg or d_gen. No conflation found.
- **Entry 111 (Arnold != connection form)**: L209-211 correctly identifies Arnold's relation as the partial-fractions identity among three simple poles. The connection form (KZ) appears at L1498-1508 as a separate object. No conflation.
- **Entry 94 (eta = q^{1/24}*prod)**: L1549-1551 correctly writes "Z = q^{-kappa/24} prod(1-q^n)^{-1}" with the q^{-kappa/24} prefactor. The eta function is not explicitly miswritten.
- **Entry 128 (S_2 = kappa = c/2, NOT c/12)**: L1161 correctly writes S_2 = c/2. No S_2 = c/12 errors found.
- **Entry 120 (CE != chiral bar multi-gen)**: No CE/chiral bar conflation. The CE complex appears only in the separate Vol III context.
- **Entry 115 (B(A) = T^c(s^{-1} A-BAR), augmentation ideal)**: L233 writes the bar complex with the correct augmentation ideal notation "B_X(A)". The bar construction is defined via collision residues, not naively on the full algebra.
- **AP113 (bare kappa)**: Zero violations in working_notes.tex. All kappa references are either generic "kappa(A)" or family-scoped ("kappa = c/2" for Virasoro, "kappa = k" for Heisenberg).
- **Three-functor distinction (bar-cobar != bulk != Koszul)**: L7924-7946 (Observation obs:three-functors) explicitly distinguishes (i) reconstruction Omega(B(A))=A, (ii) Koszul duality D_Ran(B(A))=A^!, (iii) derived centre Z^der(A)=RHom. L2036-2038 reiterates: "The bulk is not B(Vir) but the derived centre C^bullet(Vir,Vir) (AP34)."
- **Descent chain self-correction**: Section 15 (L3326-3999) subjects the entire arithmetic programme to a Beilinson test. Five levels examined; chain found BROKEN at Level 2->3 (shadow tower and Dirichlet-sewing lift are independent invariants). Three distinct involutions identified and distinguished (Verdier, Galois, Koszul). The "shadow Riemann hypothesis" explicitly dismissed (L4321-4334). Exemplary self-criticism.
- **Fan vs chain**: L4044-4054 explicitly replaces the "descent chain" picture with a "fan" picture: three independent projections from Theta_A. Repeated at L4281-4288.
- **Gravitational coproduct primitivity**: L4723-4782 correctly proves Delta_z^{Vir} is strictly primitive at all arities, via ghost-number obstruction. Mechanism is clear (BRST ghost degree -1 kills transferred corrections under p tensor p projection).
- **bc reclassification**: L4892-4912 correctly reclassifies bc ghosts from class G to class C (contact/quartic). The prior misclassification (AP3: pattern completion without recomputation) is identified.
- **N=2 corrected kappa**: L2506-2557 identifies the naive channel sum kappa=7c/6 as WRONG (AP1) and derives the correct kappa=(k+4)/4 via Kazama-Suzuki. Warning warn:n2-conflict at L2548-2557 documents the correction.
- **Honest scope assessment**: Section "What the machine does not compute" (L4205-4543) explicitly lists six structural failures: (h) Universal Langlands, (i) Non-lattice L-functions, (j) Single descent, (k) Multi-weight universality at g>=2, (l) Shadow RH, (m) Smooth-arithmetic bridge. Each failure is identified as structural, not a limitation of current technology.

### Residual Observations (not violations, but noteworthy):

| # | Observation | Details | Location |
|---|-------------|---------|----------|
| 149 | "shadow Postnikov tower" terminology | The phrase "shadow Postnikov obstruction tower" appears at L170, L931, L1292, L4969, L5123, L7056. "Postnikov" is technically a different concept (homotopy truncation by connectivity, not by arity). The manuscript's own terminology is "shadow obstruction tower" (used >50 times). The "Postnikov" instances are legacy. Not wrong per se (the tower IS a Postnikov-like truncation in the arity filtration), but "obstruction tower" is more precise. | working_notes.tex L170, L931, etc. |
| 150 | F_2(W_3) formula conditional | L4838-4880 computes F_2(W_3) = (c+120)/(16c) but marks it "conditional on op:multi-generator-universality." The RECTIFICATION-FLAG at L4868-4876 correctly notes that F_2(W_3) does NOT reduce to F_2(Vir) upon dropping W-channel. Honest bookkeeping. | working_notes.tex L4838 |
| 151 | Koszul field-preservation: only c=1,13 among integers | L3215 states "Among integers c in [0,26], it holds only at c=1 and c=13." This is a proved statement (Proposition prop:koszul-field-criterion), not a violation. | working_notes.tex L3165-3216 |
| 152 | Li coefficient sign change location: n=7 (uncompleted) vs n=974 (completed) | L5269-5275 reports completed Li coefficients turn negative at n=974, uncompleted at n=7. Both verified (L4501-4503). Distinction between completed and uncompleted Li coefficients correctly maintained. | working_notes.tex L5269, L4501 |

## XXI. higher_genus_complementarity.tex Deep Audit (2026-04-15, 6416 lines)

The complementarity theorem chapter (Theorem C) with the Verdier decomposition Q_g(A) + Q_g(A^!) = H*(M_g, Z(A)). Read L1-300 in detail.

### Verified Clean:

- **Three-layer structure C0/C1/C2**: L44-111 correctly decomposes Theorem C into fiber-center identification (C0, unconditional), eigenspace decomposition (C1, unconditional on Koszul locus), and Lagrangian upgrade (C2, conditional on perfectness and nondegeneracy). Conditionality at each layer is explicitly stated.
- **Involution splitting**: Lemma lem:involution-splitting (L236-271) proved in characteristic 0. The projectors p^+/- = (1/2)(id +/- sigma) are standard. Part (c) proves Lagrangian via anti-symmetry of the Verdier pairing.
- **Perfectness criterion**: L290-300 correctly requires PBW filterability + finite-dimensional flat fiber cohomology (Lemma lem:perfectness-criterion). Not assumed universally.
- **kappa(A) notation**: All kappa references use kappa(A) with explicit algebra argument. No bare kappa.
- **Holstein-Rivera CY exchange**: L113-132 correctly cites HR24 for smooth/proper CY exchange under Koszul duality. Identifies fiber-level perfectness as separate from family-level perfectness.
- **Complementarity as transversality**: L176-194 correctly frames complementarity via CDG2024 transversality of boundary conditions. No overclaims.

## XXII. higher_genus_foundations.tex Deep Audit (2026-04-15, 7861 lines)

The foundations chapter for higher genus theory. Read L1-300 in detail.

### Verified Clean:

- **Curvature formula**: L38-39 correctly writes d_fib^2 = kappa(A) * omega_g with omega_g as the Arakelov (1,1)-form. L98-104 derives the genus-1 curvature from the unique stable graph Gamma_irr.
- **Three differentials**: L237-282 (Convention conv:higher-genus-differentials) correctly separates d_0 (genus-0, d_0^2=0 by Arnold), d_fib (fiberwise, d_fib^2=kappa*omega_g), D_g (total corrected, D_g^2=0 by Fay trisecant). Categorical homes (derived vs coderived) correctly identified at L285-296.
- **Coderived category**: L288-293 correctly identifies the curved bar complex as living in D^co (Positselski), not D^b.
- **Arakelov propagator**: L143-154 writes the elliptic propagator with the non-holomorphic correction term 2pi*i*Im(z)/(Im(tau))*dbar{z}, forced by double-periodicity. L159-169 gives the genus-g generalization with the prime form.
- **obs_g scoping**: L186-193 correctly states "uniform-weight algebras" for the all-genera formula, with "g=1 unconditional" at L190.

## XXIII. cobar_construction.tex Deep Audit (2026-04-15, 3491 lines)

The geometric cobar complex chapter. Read L1-100 in detail.

### Verified Clean:

- **Three-functor distinction**: Remark rem:cobar-three-functors (L67-100) is a model of clarity. Explicitly states: (i) cobar = reconstruction (Omega(B(A)) = A), (ii) Verdier = homotopy Koszul dual, (iii) derived centre = bulk. Final sentence: "the cobar of the bar gives A, and Verdier duality of the bar gives the homotopy Koszul dual factorization algebra." No conflation possible.
- **Verdier exchange**: L26-27 correctly identifies j_* vs j_! as the duality between bar and cobar kernels.
- **Curvature at genus>=1**: L53-54 correctly states d_fib^2 = kappa*omega_g.

## XXIV. yangians_foundations.tex Deep Audit (2026-04-15, 3600 lines)

The Yangian foundations chapter. Read L1-100 in detail.

### Verified Clean:

- **E_1 vs E_inf distinction**: L14-17 correctly states the Yangian is E_1-chiral (ordered configurations), breaking all three E_inf features (symmetry, level inversion, kappa completeness).
- **Three levels of Yangian**: Remark rem:yangian-three-levels (L49-83) correctly separates (A) algebraic Y(g), (B) E_1-chiral on a curve, (C) QFT realization. The spectral parameter z is identified as a coordinate difference on the curve, NOT a worldsheet insertion coordinate.
- **Verdier on ordered configs**: L47 correctly states D R(u) = R^{-1}(u) (inverts R-matrix, not level).
- **Four Yangian types**: Remark rem:yangian-four-level (L85-97) separates geometric/physical, strict model, L_inf, and pro-MC levels.

## XXV. higher_genus_modular_koszul.tex Spot Check (2026-04-15, 35735 lines)

The largest theory file. Spot-checked the opening (L1-100) and r-matrix section.

### Verified Clean:

- **MC element definition**: L37-43 correctly defines Theta_A = D_A - d_0 as MC because D_A^2 = 0. "Existence of the MC element is not a theorem to be proved; it is a tautology of the bar construction."
- **Five constructions**: L70-100 lists shadow algebra, graph-sum formula, obstruction class, shadow metric, complementarity -- each arising because the preceding creates a problem.
- **Level-stripped r-matrix**: L3467 writes "r(z) = 0*Omega/z = 0" for level-stripped case, correctly carrying the level factor.

## XXVI. Vol I Remaining Theory Files: Cross-Programme First-Principles Summary

### Critical confusions checked across Vol I remaining files:

| Entry | Confusion | Files Checked | Result |
|-------|-----------|---------------|--------|
| 84 | r(z)=k*Omega/z needs level k | working_notes, all theory, lattice_foundations, yangians | **CLEAN**: All 30+ instances carry level k or hbar. Zero bare Omega/z. |
| 87 | kappa=c/2 Virasoro ONLY | working_notes, higher_genus_*, all connections | **CLEAN**: Always scoped. N=2 has separate formula. |
| 90 | S_4=10/[c(5c+22)], NOT reciprocal | working_notes L1022, L1163 | **CLEAN**: Correct throughout. |
| 113 | kappa+kappa'=K family-dependent | working_notes, w_algebras, genus_expansions, landscape_census, concordance | **CLEAN**: Always scoped by family. |
| 112 | obs_g=kappa*lambda_g at g=1+uniform ONLY | working_notes, higher_genus_foundations | **CLEAN**: Multi-weight g>=2 marked open. |
| 108 | d_alg != d_gen | survey_v2 L5021 (table header only) | **CLEAN**: Table distinguishes the two. |
| 111 | Arnold != connection form | working_notes | **CLEAN**: Arnold = partial fractions identity; KZ = r(z)dz connection. |
| 94 | eta = q^{1/24}*prod | working_notes L1549 | **CLEAN**: Correct prefactor. |
| 128 | S_2=kappa=c/2, NOT c/12 | working_notes L1161 | **CLEAN**: S_2 = c/2 throughout. |
| 120 | CE != chiral bar multi-gen | working_notes, bar_construction | **CLEAN**: No conflation found. |
| 115 | B(A)=T^c(s^{-1} A-BAR), augmentation ideal | cobar_construction, higher_genus_* | **CLEAN**: Augmentation ideal correctly used. |

### Process note:

The working_notes.tex file is the strongest self-correcting document in the programme. It contains:
- 7 dismissed false ideas (Section sec:koszul-epstein-frontier)
- 8 dead-end candidates for real-to-complex bridge (Section sec:real-to-complex-frontier)
- Explicit broken-link diagnosis in the descent chain (Level 2->3)
- Quantified failures: Li coefficients negative at n=7 (uncompleted) / n=974 (completed)
- Three distinguished involutions (Verdier/Galois/Koszul) that DO NOT compose
- Fan picture replacing chain picture

The theory chapters (higher_genus_complementarity, higher_genus_foundations, cobar_construction, yangians_foundations) are all cleanly written with correct scoping, explicit conditionality, and no violations of the critical confusion entries. The higher_genus_modular_koszul.tex (35735 lines) was spot-checked at the opening and the r-matrix section; no violations found.

## XXVII. Vol I Front Matter Comprehensive Enforcement (2026-04-15, 5-file line-by-line)

Files audited: main.tex abstract (L724-799), chapters/frame/preface.tex (4706 lines), chapters/theory/introduction.tex (2722 lines), chapters/theory/bar_construction.tex (2536 lines), chapters/theory/three_invariants.tex (356 lines). Total: ~10,500 lines.

### XXVII.A. r(z) = k * Omega / z: level prefix VERIFIED CLEAN (entry 84)

Every KM r-matrix in the front matter carries the level k prefix:
- preface.tex L598: `r(z) = k/z` (Heisenberg, scalar)
- preface.tex L712: `r(z) = k\,\Omega/z` (KM, matrix-valued)
- preface.tex L738, L1164, L3003, L3014, L3231, L4386: all `k\,\Omega/z`
- introduction.tex L1293: `r_k(z) = k\,\Omega/z` (Sugawara identity)
- introduction.tex L1441, L1654: `r(z) = k\,\Omega/z`
- Virasoro: `r(z) = (c/2)/z^3 + 2T/z` (preface L1167)

### XXVII.B. kappa = c/2 Virasoro ONLY: VERIFIED CLEAN (entry 87)

Preface kappa table (L2425-2446) gives family-specific formulae:
Heisenberg k, KM dim(g)(k+h^v)/(2h^v), Virasoro c/2, beta-gamma 1, Lattice rank(Lambda), W_N c*(H_N-1), Fermion 1/4, BP c(k)/6.
The formula kappa = c/2 appears ONLY in Virasoro context (preface L1186, L2434).

### XXVII.C. kappa + kappa' NOT universal: VERIFIED CLEAN (entry 113)

All instances scoped:
- preface L1340: `kappa(A)+kappa(A^!)=0 (for Kac--Moody and free-field algebras)`
- preface L1343: `For W-algebras: 13 for Virasoro, 250/3 for W_3`
- preface L2452-2456: full conductor table
- introduction L634-637: family-dependent scoping
- introduction L1024-1091 (thm:central-charge-complementarity): full proof, KM sum = 2 dim(g), W sum = 2 rank(g) + 4h^v dim(g), sl_2 gives 26

### XXVII.D. Bar-cobar = inversion, NOT Koszul: VERIFIED CLEAN (entry 98)

Three-functor distinction explicit at preface L446-457:
- Omega(B(A)) ~ A (inversion)
- D_Ran(B(A)) ~ A^!_inf (Verdier)
- (H*(B(A)))^v = A^! (linear duality)

Restated at bar_construction.tex L79-194 with five-row table. Preface L457: "Confusing any two is a category error."

### XXVII.E. B(A) uses augmentation ideal: VERIFIED CLEAN (entry 115)

Correct at abstract L736, preface L240-241, bar_construction.tex L9-10, introduction.tex L21. All write A-bar = ker(epsilon).

### XXVII.F. |s^{-1}v| = |v| - 1 LOWERS degree: VERIFIED CLEAN (entry 116)

Preface L241-242: `s^{-1} denotes desuspension (|s^{-1}a| = |a| - 1)`. Correct convention.

### XXVII.G. SC^{ch,top} != E_3: VERIFIED CLEAN (entry 81)

Preface L3840: "The operad SC^{ch,top} is NOT E_3." Topologisation requires inner conformal vector (L3843-3864).

### XXVII.H. B(A) is E_1, NOT SC: VERIFIED CLEAN (entry 80)

Preface L1030-1033: "B(A) is an E_1 chiral coassociative coalgebra: a single-coloured object, not an SC^{ch,top}-coalgebra."

### XXVII.I. Three Hochschild theories: VERIFIED CLEAN (entry 87/101)

Introduction L690-711: chiral (OPE on Ran, [0,2]), topological (E_1 on S^1), categorical (Drinfeld center). Preface L1035-1043: curve->chiral, circle->topological, category->Drinfeld.

### XXVII.J. d_alg != d_gen: VERIFIED CLEAN (entry 108)

Introduction L83-103: three independent invariants (r_max, d_gen, d_alg). Virasoro has d_gen = 3 but d_alg = infinity. The three_invariants.tex chapter (356 lines) is dedicated to this.

### XXVII.K. Arnold form != connection form: VERIFIED CLEAN (entry 111)

Arnold: eta_{ij} = d log(z_i - z_j), bar propagator (preface L119). Arnold relation: cyclic wedge identity (preface L128-133). KZ connection: r(z) dz on conformal blocks (introduction L788). Never conflated.

### XXVII.L. eta = q^{1/24} * prod(1-q^n): CLEAN in front matter (entry 94)

Appears only as `tr(q^{L_0 - c/24}) = 1/eta(tau)` (preface L888). The q^{-c/24} factor is explicit via L_0 - c/24. Definition of eta not given in front matter; verified clean in Section XIX (18 instances across examples carry q^{1/24}).

### XXVII.M. AP113 bare kappa: CLEAN in Vol I context

In Vol I, bare kappa always means kappa(A) -- the single modular characteristic. No ambiguity because Vol I has one kappa per algebra, not the four-kappa spectrum of Vol III.

### XXVII.N. Five Theorems Mutual Consistency

All five theorems verified consistent across abstract (main.tex L752-763), preface (L1406-1497), and introduction (L330-688):
- **A**: Bar-cobar adjunction + Verdier. Symmetric bar on Ran(X).
- **B**: Inversion Omega(B(A)) ~ A. g=0 unconditional; g>=1 on Koszul locus (except integer-spin beta-gamma).
- **C**: Lagrangian Q_g(A) + Q_g(A^!). Verdier splitting proved; shifted-symplectic conditional.
- **D**: obs_g = kappa * lambda_g (UNIFORM-WEIGHT). g=1 unconditional. Multi-weight g>=2 has cross-channel delta_F_g^cross.
- **H**: ChirHoch^n = 0 for n not in {0,1,2}. Hilbert polynomial P_A(t). Critical level excluded.

### XXVII.O. E_n Hierarchy: VERIFIED CORRECT

Abstract L784-798 and preface L928-1059:
- E_inf input -> E_2-coalgebra on symmetric bar, E_3 on derived center
- E_1 input -> E_2 on derived center (NOT E_3)
- SC^{ch,top} + inner conformal vector -> E_3^{top}
- ALL standard VAs are E_inf; poles do NOT break E_inf (preface L953)

### XXVII.P. Genus Tower: VERIFIED CORRECT

Preface L1062-1312: prime form, genus-g propagator with period corrections, d_fib^2 = kappa * omega_g, D_g = d_fib + nabla^{GM} with D_g^2 = 0. A-hat generating function (x/2)/sin(x/2), radius 2*pi.

### XXVII.Q. Central Charge Complementarity: VERIFIED CORRECT

Introduction L1024-1091: KM c + c' = 2 dim(g); W-algebras c + c' = 2 rank(g) + 4h^v dim(g); sl_2 gives 26. Proof via Sugawara c = k dim(g)/(k+h^v) and Freudenthal-de Vries |rho|^2 = h^v dim(g)/12.

### XXVII.R. Master Reference Tables

**Kappa table** (all standard families, from preface L2425-2446):

| Family | kappa(A) | kappa(A^!) | K |
|--------|----------|------------|---|
| Heisenberg H_k | k | -k | 0 |
| Affine KM g_k | dim(g)(k+h^v)/(2h^v) | negated | 0 |
| Virasoro Vir_c | c/2 | (26-c)/2 | 13 |
| beta-gamma | 1 | -1 | 0 |
| Lattice V_Lambda | rank(Lambda) | negated | 0 |
| W_N(sl_N) | c*(H_N-1) | c'*(H_N-1) | K_N*(H_N-1) |
| Free fermion | 1/4 | -1/4 | 0 |
| BP B^k | c(k)/6 | c(-k-6)/6 | 98/3 |

**r-matrix table** (from preface L597-740):

| Family | r(z) | Pole order | av(r) |
|--------|------|-----------|-------|
| Heisenberg | k/z | 1 (scalar) | k |
| Affine KM | k*Omega/z | 1 (matrix) | k*dim(g)/(2h^v) |
| Virasoro | (c/2)/z^3 + 2T/z | 3 (matrix) | c/2 |
| beta-gamma | nilpotent/z | 1 (nilpotent) | 1 |

Note: For non-abelian KM, kappa = av(r) + dim(g)/2 (Sugawara shift, preface L724-729).

**Three invariants** (from three_invariants.tex):

| Family | p_max | k_max | r_max | Class |
|--------|-------|-------|-------|-------|
| Heisenberg | 2 | 1 | 2 | G |
| Affine sl_2 | 2 | 1 | 3 | L |
| beta-gamma | 1 | 0 | 4 | C |
| Virasoro | 4 | 3 | inf | M |
| W_3 | 6 | 5 | inf | M |

**Three functors** (from preface L446-457):

| Functor | Output | Name |
|---------|--------|------|
| Omega(B(A)) | original A | INVERSION |
| D_Ran(B(A)) | A^!_inf | VERDIER |
| (H*(B(A)))^v | A^! | LINEAR DUALITY |

**E_n cascade** (from preface L928-1059 and abstract L784-798):

| Input | Bar structure | Derived center | Mechanism |
|-------|-------------|----------------|-----------|
| E_inf | E_2-coalgebra | E_3 | Higher Deligne |
| E_1 | E_1-coalgebra | E_2 | Deligne |
| SC^{ch,top} | -- | E_3^{top} (with inner conformal vector) | Topologisation |

### XXVII.S. Summary

- **Files audited**: 5 (main.tex abstract, preface.tex, introduction.tex, bar_construction.tex, three_invariants.tex)
- **Total lines read**: ~10,500
- **Cache entries verified**: 14 (entries 80, 81, 84, 87, 94, 98, 101, 108, 111, 113, 115, 116, AP113, five theorems)
- **Violations found**: 0
- **All 14 entries clean in the Vol I front matter**. The canonical volume is in excellent shape.

**Total new violations found across all files audited in this sweep: 0.** The Vol I remaining files (working_notes.tex + 5 major theory chapters) are clean against all 12 critical confusion entries.

## XXVIII. Vol I Preface Deep Line-by-Line Pass (2026-04-15)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | Location |
|---|-------------|---------------|---------------|---------------------|------|----------|
| 153 | "Arrow 3 is the Drinfeld center, the categorified analogue of the averaging map" | Z and av ARE related via factorization | Z categorifies the algebraic CENTER z(A), not the averaging map. av categorifies to Sym (symmetrization) | Z = right adjoint to forgetful E_2→E_1 (constructs braiding). av = further step Sym: E_2→E_∞ (destroys braiding). Factorization: E_1→^Z E_2→^{Sym} E_∞. Center constructs; averaging destroys. | construction/narration (AP-CY54) | preface.tex L3813 |

115 claims checked, 2 violations found and fixed. The Vol I preface is the canonical reference — 113 clean claims out of 115.

| 154 | "conditional on chain-level S³-framing for d=3" | CY-A_3 WAS conditional | CY-A_3 is NOW PROVED (inf-cat, HH^{-2}_{E_1}=0). Chain-level explicit A_X for non-formal remains open | Update: "proved at d=3 via inf-cat resolution" | temporal | preface.tex L4681 |
| 155 | Σ F_g x^{2g} = k(x/2/sinh(x/2) - 1) | Â-genus DOES use sinh | sinh gives alternating signs; FP intersection numbers λ_g are POSITIVE | Correct: sin (all positive coefficients). Â-genus (sinh) alternates; FP series (sin) doesn't. |B_{2g}|/(2g)! is the absolute value. | convention/sign | heisenberg_frame.tex L48 |

## XXIX. Geometric vs Algebraic Model Conflations (2026-04-16, from Vol III adversarial swarm on two derived centers)

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type | AP |
|---|-------------|---------------|---------------|---------------------|------|-----|
| 156 | "Spectral parameters from FM_k(C)" for End^ch_A | End^ch_A relates to FM via local-global identification | Narration: End^ch_A is algebraic (formal Laurent series in lambda_i). FM enters via comparison theorem (formal disk restriction), not the definition. | Three layers: (1) geometric model on FM_{n+1}(X) with log forms, (2) formal-disk restriction gives lambda_i as relative positions, (3) algebraic model End^ch_A with formal variables. The comparison is a theorem, not a definition. | construction/narration | AP-CY67 |
| 157 | "ChirHoch* and THH* are different-sized objects (dim 3 vs infinite)" | ChirHoch and THH compute different invariants | For Koszul algebras (Heisenberg), HH*(Weyl)=1-dim, not infinite. Difference is STRUCTURAL (E_2 with spectral data vs abstract E_2), not DIMENSIONAL. | Same cohomology groups for Koszul algebras; different E_2 algebra structures. The genuine "fails to concentrate" object is H*_GF (Gel'fand-Fuchs), not THH. | chain/cohomology confused with size/structure | AP-CY64 |
| 158 | "BZFN gives different answers depending on ambient category S as tunable parameter" | Two derived centers DO exist and produce different braided categories | S is not a free parameter. Both sides of BZFN use same S. Two centers come from TWO DIFFERENT ALGEBRAS: chiral A (in D-mod(Ran)) vs mode algebra A_mode (in Vect). | BZFN applied once to each algebra in its native ambient category. Different inputs, not different parameters. | object/structure | AP-CY66 |
| 159 | "Topological Drinfeld center has no spectral parameters" | Chiral structure creates translation automorphism enabling evaluation modules | Yangian Y(g) as purely associative algebra HAS evaluation modules V_u and spectral R(z=u-v) in its Drinfeld center. | Spectral parameter from representation theory (evaluation modules), not center construction. Correct claim: chiral bar DIFFERENTIAL is z-dependent; topological bar COPRODUCT is z-independent. | construction/data conflation | AP-CY65 |
| 160 | BD chiral operad = algebraic End^ch_A (used interchangeably) | They are related by formal disk restriction (isomorphism after coordinate choice) | BD operad lives in D-modules on Ran(X); End^ch_A is formal Laurent series. Different mathematical categories. Identification requires 4-step chain. | Bridge: local coordinate -> formal disk -> D-module trivialization -> spectral variable identification. Isomorphism of non-Sigma operads, coordinate-dependent. Aut(O)-equivariance absorbs coordinate dependence. Bridge Proposition assembling all 4 steps ABSENT from manuscript. | object/structure + expository gap | AP-CY63 |
| 161 | Geometric ChirHoch = algebraic ChirHoch (used interchangeably at chain level) | They ARE quasi-isomorphic for logarithmic chiral algebras | The comparison is stated only as a remark (rem:comparison-geometric-hoch), NOT proved as a named theorem. Used without citation at 100+ locations. The bar complex comparison IS a named theorem (thm:geometric-equals-operadic-bar). | Two models: geometric (FM compactifications, log forms, 3-component diff) vs algebraic (End^ch_A, formal variables, Gerstenhaber bracket diff). At genus >= 1, geometric model carries curve-dependent data that algebraic model lacks. | label/content (model ambiguity) | AP-CY62 |
| 162 | "Theorem H fails for THH / concentration has no THH analogue" | Theorem H IS specifically about ChirHoch* | THH = HH*(A_mode) is ALSO concentrated: HH*(Weyl) = C in degree 0 (MORE concentrated). The "fails for THH" claim confuses HH* with H*_GF (Gel'fand-Fuchs). | Three invariants: ChirHoch* in {0,1,2}, HH*(A_mode) in {0}, H*_GF unbounded. Genuine size difference ONLY at critical level k=-h^v (Feigin-Frenkel center). | three-way conflation (ChirHoch/HH/GF) | AP-CY64 |
| 163 | "Physics requires two different bulk theories" | Physics has ONE bulk per boundary (uniqueness of derived center) | Two derived centers are two COMPUTATIONAL MODELS of the same physical observable, not two different theories. | Physics: boundary A determines unique bulk Z^der(A). Two mathematical routes (ChirHoch, Z(U_A)) should give the same answer. Their equivalence is conj:drinfeld-center-equals-bulk. | construction/narration (two routes, one destination) | AP-CY62/66 |
| 164 | "Restricting chiral algebra to S^1 gives A_inf algebra" | E_2 restricts to E_1 on real submanifolds (Costello-Gwilliam) | Conflates four operations: (a) D-module restriction (ill-defined on real submanifold), (b) mode algebra (strictly assoc), (c) int_{S^1} A = HH_*(A) (chain complex), (d) pullback of FA along S^1->D* (gives E_1). | Correct: holomorphic FA on C restricted to real ray gives E_1-algebra. int_{S^1} gives Hochschild homology. Mode algebra is strictly associative. E_1 = A_inf only in char 0 after homotopy transfer. | four-way conflation | AP-CY64 |
| 165 | Tamarkin inconsistency: C*(H_k, H_k) = k[[kappa]] vs Theorem H dim 3 | Both computations correct | k[[kappa]] is DEFORMATION PARAMETER SPACE (how family varies with level k). ChirHoch*(H_k) at FIXED k has dim 3. Different mathematical objects. | Reconstructor deformation parameter space vs bulk state space: answer different questions. Neither wrong. Resolution at hochschild.tex:3376-3413. | family/fiber conflation | AP-CY64 |
