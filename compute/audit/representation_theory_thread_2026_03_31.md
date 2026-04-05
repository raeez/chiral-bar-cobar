# Full Thread Dump: Representation Theory and the Shadow Tower
## Date: 2026-03-31
## Participants: Raeez Lorgat

---

# PART I: INITIAL PROMPT AND FIRST RESPONSE

## User Prompt

what are some of the deepest questions in representation theory and how do they intersect our research programme?

[User included a detailed sketch covering:]

1. Geometric Langlands and the critical-level formula:
   Q_g(g_{-h^v}) + Q_g(g_{-h^v}^!) = H*(M_g, Fun(Op_{g^v}))
   Claimed as a factorization algebra decomposition of the space geometric Langlands lives on.

2. Arithmetic shadows: the packet connection nabla^arith_A and frontier defect form Omega_A connecting shadow obstruction tower data to L-functions. Hecke-Newton closure for lattice VOAs giving unconditional Ramanujan.

3. Categorification (Crane-Frenkel vision, KLR). MC3 (proved all simple types) as the derived-level answer. Prefundamental modules L^+/- generate Grothendieck ring (Hernandez-Jimbo). K_0-generation proved, categorical thick generation remaining gap. DK bridge: R-matrix as genus-0 binary shadow of Theta_A.

4. Wild/irregular frontier: analytic sewing (MC5, HS-sewing theorem), sewing envelope A^sew, coderived passage at genus >= 1. Shadow growth rate rho(A) and critical cubic at c* ~ 6.125 as phase boundary.

5. Quantum groups at roots of unity / logarithmic CFT: admissible-level frontier, universal W^k(g) Koszul at all levels, simple quotient W_k(g) may fail. Annulus trace Tr_A ~ HH_*(A) as modular shadow of non-semisimple trace.

6. Modular representation theory: shadow obstruction tower as continuous analogue of decomposition matrix, G/L/C/M as shadow-tower analogue of tame/wild dichotomy.

User's unifying thread: every deep question has the same structural skeleton — duality between object and dual mediated by deformation/obstruction tower. All are projections of Theta_A in MC(g^mod_A). The shadow obstruction tower is to representation theory what the Postnikov tower is to homotopy theory.

User then asked: "let's develop this systematically, from first-principles, to realize the deepest possible understanding"

---

## First Response: Agent Explorations

Three exploration agents were launched to read source files:

### Agent 1: Representation Theory Sources
Read entanglement_modular_koszul.tex, arithmetic_shadows.tex, yangians_drinfeld_kohno.tex, higher_genus_complementarity.tex, chiral_koszul_pairs.tex, e1_modular_koszul.tex.

Key findings:
- Theorem 137 (entanglement): S_n^sc = (c/6)(1+1/n)log(L/eps), S_EE = (c/3)log(L/eps)
- Theorem 212 (entanglement complementarity): S_EE(A) + S_EE(A!) = (c+c')/3 log(L/eps)
- Four entanglement complexity classes G/L/C/M
- Shadow-spectral correspondence for lattice VOAs
- Arithmetic packet connection: nabla^arith = d - direct_sum Lambda'_chi/Lambda_chi ds
- DK levels as shadow projections (table DK-0 through DK-5)
- Derived DK for affine algebras (commutative square with braided monoidal functors)
- Yangian Koszul duality: Phi: D^b(Rep(Y_hbar)) -> D^b(Rep(Y_{-hbar}))
- Theorem C: Q_g(A) + Q_g(A!) = H*(M_g, Z(A)), Lagrangian decomposition
- 12 characterizations of chiral Koszulness (10 unconditional, 1 conditional, 1 one-directional)
- Conformal block reconstruction: F_g = kappa * lambda_g^FP, A-hat generating function

### Agent 2: Shadow Tower and MC Structure
Read higher_genus_modular_koszul.tex extensively.

Key findings:
- thm:mc2-bar-intrinsic: Theta_A := D_A - d_0, four properties (MC, scalar trace, clutching, Verdier)
- def:modular-convolution-dg-lie: g^mod_A with five-component differential D = d_int + [tau,-] + d_sew + d_pf + hbar*Delta
- Three-tier architecture (Tier 0 from D^2=0, no Koszulity needed)
- Shadow depth classification G/L/C/M (def, lines 13690-13740)
- thm:riccati-algebraicity: H(t)^2 = t^4 Q_L(t)
- thm:single-line-dichotomy: r_max|_L in {2, 3, infinity}
- Universal factorization: S_r = Delta * R_r for r >= 4
- thm:recursive-existence: inverse limit converges by Mittag-Leffler
- thm:shadow-connection: nabla^sh = d - Q_L'/(2Q_L)dt, logarithmic, residue 1/2, monodromy -1
- Complementarity of discriminants: Delta(A) + Delta(A!) = 6960/[(5c+22)(152-5c)]
- thm:cubic-gauge-triviality: cubic is gauge-trivial, quartic is canonical
- prop:independent-sum-factorization: kappa additive, Delta multiplicative

### Agent 3: Concordance and Physical Origins
Read concordance.tex, physical_origins.tex, introduction.tex, kac_moody.tex, koszul_pair_structure.tex.

Key findings:
- Koszulness programme: chiral extension of classical Koszul duality via FM compactifications
- Arnold relation = Jacobi identity in disguise
- All five MC1-5 proved
- Three-pillar architecture: Pillar A (Ch_infty), Pillar B (sL_infty), Pillar C (log FM)
- Feigin-Frenkel center: H^0(B(g_{-h^v})) = Fun(Op_{g^v}(D))
- FF shift k <-> -k-2h^v as Verdier duality on FM compactifications
- Factorization-level geometric Satake (conjectural target)
- Chiral Steinberg correspondence: FM_k(C) plays role of Springer resolution
- Swiss-cheese convolution algebra extracts six structures from single MC element

---

## First Response: Mathematical Essay

### The Shadow Tower as Universal Representation-Theoretic Object

### I. The Organizing Question
Every deep question in representation theory: "What controls the decomposition of a structured object into irreducible pieces, and what obstructs this decomposition at successive levels of complexity?"

### II. Level 0 — The Seed: Koszul Duality Over a Point
Classical Koszul duality (Priddy, BGS). Bar construction, BGG correspondence. Key observation: Koszul duality over a point = Koszul duality over P^1 at genus 0.

### III. Level 1 — The Curve: What Changes at Genus g >= 1
Three new phenomena:
(a) Curvature: kappa, A-hat generating function, Theorem D
(b) Complementarity: Theorem C, Lagrangian decomposition
(c) Critical-level collapse: Feigin-Frenkel center, oper space

### IV. Level 2 — The Shadow Tower: Obstruction-Theoretic Complexity
MC element, weight filtration, single-line dichotomy H^2 = t^4 Q_L.
Four-class partition G/L/C/M.
Growth rate rho, complementarity of discriminants.

### V. Level 3 — The Six Projections
1. pi_{2,0}(Theta^{E1}) = classical r-matrix
2. pi_{*,0}(Theta^{E1}) = full genus-0 tower / A_infty structure
3. pi_sc(Theta) = scalar trace / genus expansion
4. sigma-eigenspaces = Koszul/Langlands duality
5. pi_{2,1}(Theta^{E1}) = KZ associator at genus 1
6. All genera, all arities = full modular envelope

### VI. Level 4 — Arithmetic
Packet connection, depth decomposition, Hecke-Newton closure, unconditional Ramanujan.

### VII. Level 5 — What Is Theta_A?
Three identifications: (a) universal twisting morphism, (b) Postnikov tower analogue, (c) motivic decomposition.

### VIII. Synthesis Table
| Duality | Shadow projection | Arity | Genus |
|---------|-------------------|-------|-------|
| BGG/Koszul | Theta^{<=2} | 2 | 0 |
| Yang-Baxter | pi_{2,0} | 2 | 0 |
| Drinfeld-Kohno | pi_{*,0} | all | 0 |
| KZ-elliptic | pi_{2,1} | 2 | 1 |
| FF/Langlands | Theta|_{k=-h^v} | all | all |
| Complementarity | sigma-eigenspaces | all | g |
| Shadow depth | Full tower | <=r | 0 |
| Arithmetic | nabla^arith | all | all |

---

# PART II: ADVERSARIAL ATTACK

## User Prompt
"adversarially attack all the ideas in this thread. tear them to pieces. realize the strongest most platonic ideal form"

## Response: The Adversarial Audit

### Attack 1: "Every deep question is a projection of Theta_A" — SCOPE INFLATION

- Kazhdan-Lusztig: Saying "Koszul duality = arity 2" is circular. KL proved by D-modules (BB, BK), not bar-cobar. Framework restates Koszulness, doesn't prove KL.
- Geometric Langlands: Shadow obstruction tower COLLAPSES at critical level (kappa=0). Langlands content in bar COHOMOLOGY, not MC element. Shadow obstruction tower is wrong object — degenerates where Langlands lives.
- Categorification: MC3 is thick generation, not 2-category construction. Does not produce KLR algebras.
- Modular rep theory: G/L/C/M classifies ALGEBRAS (shadow depth), tame/wild classifies REPRESENTATION CATEGORIES (indecomposable count). Different things classified.

Verdict: 2/8 genuine (FF, DK), 3/8 tautological, 3/8 false/misleading.

### Attack 2: "Theta_A is a genuinely new object" — PACKAGING vs. DISCOVERY

Theta := D - d_0 repackages bar differential. D^2=0 is tautological. MC packaging is language, not discovery. Content is in structure theorems (algebraicity, formality, complementarity), not in formalism.

### Attack 3: "Shadow obstruction tower = Postnikov tower" — ANALOGY FAILURE

Postnikov: k-invariants arbitrary in cohomology group (maximal expressiveness).
Shadow: H^2 = t^4 Q_L (algebraic of degree 2, determined by 3 numbers).
Shadow obstruction tower much MORE RIGID than Postnikov. Analogy misleading in both directions.

### Attack 4: "6960 is universal" — AP7 + AP9

Computation: 6960 = 40 * 174 = (Virasoro quartic normalization) * (sum of Lee-Yang denominators). Virasoro-specific. For KM, W_N: different numerators.

### Attack 5: Entanglement — RESTATING KNOWN RESULTS

[Later RETRACTED — see Part IV]
Claimed S_EE = (c/3)log(L/eps) just restates Calabrese-Cardy.

### Attack 6: Arithmetic — NARRATIVE OUTRUNNING PROOF

Claimed depth-1 = critical lines is trivially true for class G. Extension to class M conjectural. "Unconditional Ramanujan" just Deligne's theorem.
[Later PARTIALLY RETRACTED — see Part IV]

### Attack 7: "Complete invariant" — ALMOST CERTAINLY FALSE

Ext algebra not complete classically. Shadow obstruction tower misses module information.

## Reconstruction: What Survives

### Genuine Theorem 1: Bar-Cobar on Curves Is Non-Trivial Extension
Curvature, complementarity, shadow depth — genuinely new at genus >= 1.

### Genuine Theorem 2: The Single-Line Dichotomy
H^2 = t^4 Q_L. Shadow generating function algebraic of degree 2. Determined by 3 invariants. Discriminant Delta controls termination.

### Genuine Theorem 3: The DK Bridge
R-matrix as shadow projection. Predicts DK-3 through DK-5.

### Genuine Theorem 4: Complementarity as Lagrangian Geometry
Q_g(A) + Q_g(A!) = H*(M_g, Z(A)). New duality phenomenon. Lagrangian condition.

### Genuine Connection 5: Feigin-Frenkel as Bar Cohomology
H*(B(g_{-h^v})) = Omega*(Op). On orthogonal axis from shadow obstruction tower.

## The Platonic Form

"The Shadow Structure Theorem" (informal):
(1) Bar differential defines convergent tower governed by H^2 = t^4 Q_L
(2) Discriminant Delta classifies into G/L/C/M
(3) Koszul duality acts by Verdier involution, Lagrangian complementarity
(4) Genus-0 arity-2 recovers R-matrix via DK
(5) Critical level: tower collapses, bar cohomology = FF center

Honest relationship: shadow obstruction tower simultaneously generalizes Ext algebra (genus 0), R-matrix (arity 2), partition function (scalar trace), while producing genuinely new information (discriminant, four-class classification, Lagrangian complementarity).

---

# PART III: REIMAGINED PLATONIC FORM

## User Prompt
"reimagine, from first-principles, the platonic ideal treatment of representation theory in the context of this research programme, drawing from the ideas we have discussed here"

## Response: Three Agents + Mathematical Essay

### Agent Explorations (3 parallel)
Read shadow metric/discriminant details, DK bridge/complementarity/Koszulness details, bar-intrinsic/convolution/formality details. All key theorem statements extracted with line numbers.

### Essay: Representation Theory on Curves — The Platonic Form

### 0. Intellectual Honesty
Three things from adversarial attack that govern:
1. Most claimed intersections tautological or misleading
2. MC packaging is language, not discovery
3. Three results survive as genuinely new

### I. The Seed: A Tautology with Consequences
D^2=0, Theta_A := D-d_0, weight filtration w(g,r,d) = 2g-2+r+d.

### II. The Three Theorems

**Theorem A (Algebraicity):**
H(t)^2 = t^4 Q_L(t) where Q_L = 4kappa^2 + 12kappa*alpha*t + (9alpha^2+16kappa*S_4)t^2
Delta := 8kappa*S_4 forces r_max in {2,3,infty}
Growth rate rho, asymptotics S_r ~ A*rho^r*r^{-5/2}

**Theorem B (Formality Identification):**
Shadow obstruction tower = L_infty formality obstruction tower
- Arity 2: kappa = ell_2^(0)(Theta,Theta)
- Arity 3: C = -h(ell_3^(0)(Theta^{<=2})^{otimes 3})
- Arity 4: Q = [ell_4^{(0),tr}(Theta^{<=3})^{otimes 4}]
G/L/C/M = formality classification

**Theorem C (Complementarity):**
C_g(A) ~ Q_g(A) + Q_g(A!), Lagrangian decomposition
(C1) unconditional, (C2) shifted-symplectic conditional

### III. The Triangle
Algebraicity + Formality + Complementarity form closed triangle.

### IV. What Classical Representation Theory Is
- Classical Koszul duality = genus 0, arity 2, Delta=0 (class G, formal case)
- DK bridge: R-matrix = pi_{2,0}(Theta^{E1}), genuine
- Feigin-Frenkel: bar cohomology at critical level, orthogonal axis

### V. What Is Genuinely New: The Discriminant
Delta = 8kappa*S_4. No classical invariant sees this.
(a) Formality classification
(b) Growth rate and phase boundary
(c) Duality constraint
(d) Connection topology (nabla^sh = Gauss-Manin, monodromy = Koszul sign)

### VI. Architecture
Classification table. Projections table. Connection structure.

### VII. Deepest Questions, Stated Honestly
(Q1) Operadic complexity conjecture
(Q2) Class C: structural or accidental?
(Q3) DK-5: full categorical equivalence
(Q4) Arithmetic axis
(Q5) Complementarity beyond Koszulness
(Q6) Picard-Fuchs monodromy

### VIII. The Platonic Sentence
"The genus expansion of a chirally Koszul algebra is algebraic of degree 2, classified by a computable quadratic discriminant that measures L_infty non-formality and is constrained by Koszul duality to satisfy Lagrangian complementarity."

---

# PART IV: DEEP BEILINSON PASS + STANDALONE TREATMENT

## User Prompt
"perform another deep beilinson pass on ALL the ideas discussed throughout this entire thread. Then, of what survives, write up all these ideas in a standalone treatment, first-principles fortified, platonic ideal realization, without any reference to previous versions or audits. i.e. completely standalone."

## User Follow-up
"adversarially attack all these ideas to ensure the false ones get killed"

## Response: Four Verification Agents

### Agent 1: Verify Algebraicity Chain (COMPLETED)

**Chain verified: D^2=0 -> Theta MC -> master eq -> Riccati algebraicity -> H^2=t^4*Q_L**

- thm:riccati-algebraicity (line 14088): ASSUMES master equation (from prop:master-equation-from-mc), shows EQUIVALENT to H^2=t^4*Q_L. Chain: partial^2=0 on M_bar -> D^2=0 (thm:convolution-d-squared-zero, line 20912) -> Theta MC (thm:mc2-bar-intrinsic, line 2860) -> master eq (prop:master-equation-from-mc, line 11056) -> algebraicity.
- Hostile spot-check at arity 5 (m=3): a_0*a_3 = -12*alpha*S_4, a_1*a_2 = 12*alpha*S_4, sum = 0. PASSES.
- thm:single-line-dichotomy (line 14277): correctly says r_max|_L in {2,3,infty}. Class C from stratum separation (rem:contact-stratum-separation, lines 14596-14611).
- S_r = Delta*R_r for r>=4: PROVED by binomial expansion (lines 14357-14365).
- Complementarity of discriminants (line 14468): Virasoro-specific. Proof uses c->26-c. "Universal constant" means c-independent numerator within Virasoro family.
- Shadow connection: flat on 1D (automatic), curvature delta_mix on multi-channel (item (vii)).
- thm:shadow-formality-identification (line 13481): ProvedHere, inductive proof. Genus-0 trees = genus-0 stable graphs, same combinatorial data.

**VERDICT: Zero gaps in logical chain. Every link proved. No circular dependencies.**

### Agent 2: Verify Complementarity + Koszulness (COMPLETED)

**Finding 1**: (C1) unconditional on Koszul locus (line 73 explicit). (C2) conditional on perfectness + nondegeneracy (line 50). CORRECT.

**Finding 2 (MODERATE, AP7)**: rem:homotopy-native-c (line 512) cites prop:ptvv-lagrangian without the g>=2 restriction the proposition carries. Shifted-symplectic proved for g>=2 only.

**Finding 3 (SERIOUS, AP2)**: CLAUDE.md lists:
- (ix) = FM boundary acyclicity
- (x) = shadow-formality at arities 2,3,4

Actual source has:
- (ix) = Kac-Shapovalov determinant
- (x) = FM boundary acyclicity

Shadow-formality is NOT a numbered item in thm:koszul-equivalences-meta. It appears as separate prop:koszulness-formality-equivalence (line 2060).

**Finding 4**: Involution-splitting lemma requires char != 2 (line 161). Satisfied over C. Key step for (C1).

### Agent 3: Verify DK Bridge + Feigin-Frenkel (COMPLETED)

**DK status tags verified:**
- DK-0: PROVED (thm:derived-dk-affine, line 127)
- DK-1: PROVED (thm:factorization-dk-eval, line 391)
- DK-2/3: PROVED on eval-generated core (cor:dk23-all-types, line 806). Full category O: CONJECTURAL (conj:full-derived-dk, line 468).
- DK-4: CONJECTURAL (conj:dk4-formal-moduli, line 1080)
- DK-5: CONJECTURAL (conj:dk5-infty-pbw, line 1140)

**DK-1 shadow projection**: constr:dk-shadow-projections (line 104) is a Construction (organizing table), NOT a theorem. The shadow-projection identification "DK-1 = pi_{2,0}(Theta^{E1})" is a conceptual framing. The proved content (thm:factorization-dk-eval) shows bar-cobar inverts R-matrix on evaluation modules — consistent but not identical.

**Feigin-Frenkel**: H^0(B(g_{-h^v})) = center is ORIGINAL (thm:oper-bar-h0, line 3630, ProvedHere). Center = Fun(Op) CITED from Feigin-Frenkel (thm:critical-level-structure, line 224, ProvedElsewhere).

**S_4 at critical level**: Well-defined and ZERO for all levels of affine KM (Jacobi identity, level-independent). No singularity.

**Factorization-level geometric Satake**: conj:chiral-bgg (line 2390), CONJECTURAL. Honestly labeled.

### Agent 4: Verify Entanglement + Arithmetic (COMPLETED)

**Entanglement S_EE**: CC formula is CITED (lem:ent-twist-dimension, line 113, ProvedElsewhere from CC). thm:ent-scalar-entropy (line 137, ProvedHere) plugs CC twist dimension into replica trick — elementary algebra. Shadow obstruction tower contributes CORRECTIONS at arity >= 3. Chapter honest about this (section title: "Calabrese-Cardy from the modular characteristic").

**Four-class entanglement complexity** (prop:ent-complexity-classification, line 332, ProvedHere): delta S_r defined as "shadow obstruction tower evaluated on replica geometry." Physical identification with FLM/EW bulk entropy corrections is HEURISTIC (rem:ent-rt-interpretation, remark level, not theorem).

**G12 QEC**: ProvedHere in holographic_codes_koszul.tex (line 340). But (i)<=>(ii) is tautological. Knill-Laflamme requires unitarity (line 96). G12' in thqg file is separate conjecture.

**Depth decomposition** (thm:depth-decomposition, line 1282, ProvedHere): HYBRID. d_alg DEFINED as remainder. Theorem content: d_arith counts critical lines + d_alg >= 0.

**cor:unconditional-lattice** (line 5344, ProvedHere): GENUINE alternative route. MC => prime-locality => CPS => Sym^{r-1} => Ramanujan. Goes through Langlands (CPS, Jacquet-Shalika) rather than etale cohomology. NOT just Deligne restated. Manuscript admits Hecke eigenvalues are same Deligne eigenvalues (lines 4708-4714) but proof method is independent.

**conj:arithmetic-comparison** (line 7688): Correctly labeled ClaimStatusConjectured.

---

## RETRACTED CLAIMS FROM PREVIOUS ATTACK

**1. "Entanglement programme just restates CC" — RETRACTED.**
The programme proves CC exact for class G (new), gives computable corrections for other classes (new), convergence for rho < 1 (new). Scalar level IS CC; corrections beyond CC are genuine.

**2. "Unconditional Ramanujan is just Deligne" — RETRACTED.**
It's a genuinely new proof route via CPS/Langlands rather than etale cohomology.

## CONFIRMED FALSE/INFLATED

| Claim | Verdict |
|-------|---------|
| "Every deep rep theory question = projection of Theta" | AP7 scope inflation |
| "6960 is universal" | Virasoro-specific |
| "Shadow obstruction tower = Postnikov tower" | Misleading analogy |
| "Theta is complete invariant" | Almost certainly false |
| "G/L/C/M = tame/wild" | Different things classified |
| "(C2) is unconditional" | FALSE — ClaimStatusConditional |
| "Langlands lives in shadow obstruction tower" | Tower collapses at critical level |
| "DK-1 = pi_{2,0} is a theorem" | It's a Construction (organizing table) |

---

# PART V: THE STANDALONE TREATMENT

## Representation Theory on Algebraic Curves: The Shadow Tower

### 1. The Problem

Classical Koszul duality (Priddy; Beilinson-Ginzburg-Soergel) governs decomposition over a point: quadratic algebra A, dual A^!, bar construction B(A), BGG correspondence, derived equivalence D^b(mod-A) ~ D^b(mod-A^!).

On an algebraic curve X: chiral algebra A (D_X-module with chiral bracket), bar construction via FM compactifications, bar differential extracts residues at collision divisors weighted by eta_{ij} = dlog(z_i - z_j).

Three phenomena at genus >= 1 with no classical analogue:
- Curvature (A-hat genus)
- Complementarity (Lagrangian decomposition)
- Shadow depth (quadratic discriminant classification)

### 2. The Modular Convolution Algebra

#### 2.1. Definition
g^mod_A := prod Hom_{Sigma_n}(C*(M_bar_{g,n}), End_A(n))
Differential D = d_int + [tau,-] + d_sew + d_pf + hbar*Delta
D^2 = 0 from partial^2 = 0 on M_bar_{g,n}

#### 2.2. Weight filtration
Tridegree (g,r,d), weight w = 2g-2+r+d. Exhaustive, separated, complete, pronilpotent.

#### 2.3. Universal MC element
Theta_A := D_A - d_0 satisfies:
1. MC: Theta in MC(g^mod)
2. Scalar trace: tr(Theta) = sum kappa * lambda_g^FP
3. Clutching factorization
4. Verdier: D(Theta_A) = Theta_{A^!}

Finite-order truncations project: kappa (arity 2), C (arity 3), Q (arity 4).
Inverse limit converges by Mittag-Leffler.

### 3. The Three Structure Theorems

#### 3.1. Algebraicity
**Theorem (Riccati algebraicity).** On any 1D primary slice L:
H(t)^2 = t^4 Q_L(t)
where Q_L(t) = 4kappa^2 + 12kappa*alpha*t + (9alpha^2 + 16kappa*S_4)t^2.

**Corollary (Single-line dichotomy).** Delta := 8kappa*S_4 forces r_max|_L in {2, 3, infty}.

**Corollary (Universal factorization).** S_r = Delta * R_r for r >= 4.

#### 3.2. Formality identification
**Theorem (Shadow-formality identification).** Shadow obstruction tower = L_infty formality obstruction tower at all arities:
- kappa = ell_2^(0)(Theta, Theta)
- C = -h(ell_3^(0)(Theta^{<=2})^{otimes 3})
- Q = [ell_4^{(0),tr}(Theta^{<=3})^{otimes 4}]

Four classes:
| G | depth 2 | formal | Heisenberg |
| L | depth 3 | single Massey product | aff g_k |
| C | depth 4 | quartic then rigid (stratum separation) | beta-gamma |
| M | depth infty | intrinsically non-formal | Vir_c, W_N |

#### 3.3. Complementarity
**Theorem C.** For chiral Koszul pair (A, A^!):

(C1, unconditional): C_g(A) ~ Q_g(A) + Q_g(A!), Lagrangian.
H*(M_bar_g, Z(A)) = Q_g(A) + Q_g(A!).

(C2, conditional on perfectness/nondegeneracy): -(3g-3)-shifted symplectic, Lagrangian subspaces.

### 4. The Discriminant

#### 4.1. Definition and classification
Delta = 8kappa*S_4. Three numbers (kappa, alpha, S_4) determine entire tower via H = t^2*sqrt(Q_L).

#### 4.2. Growth rate and convergence
rho = sqrt(9alpha^2 + 2Delta)/(2|kappa|). Shadow PF converges for rho < 1. Critical cubic at c* ~ 6.125 for Virasoro.

#### 4.3. Separation and additivity
Direct sums: kappa additive, Delta multiplicative, R_4^mod additive.

#### 4.4. Cubic gauge principle
H^1(F^3/F^4, d_2) = 0 implies cubic gauge-trivial, quartic canonical.

### 5. The Shadow Connection

nabla^sh = d - Q_L'/(2Q_L) dt = d - d(log sqrt(Q_L))

- Flat on 1D (automatic). Curvature delta_mix on multi-channel.
- Regular singularities at zeros of Q_L, residue 1/2, monodromy -1 (Koszul sign).
- Gauss-Manin identification: nabla^sh = nabla^GM of family {sqrt(Q_L(t))}.
- Picard-Fuchs: Q_L f'' + (1/2)Q_L' f' = 0. Fuchsian, 3 regular singular points.
- Koszul duality: Verdier involution on Q_L. For Virasoro:
  Delta(Vir_c) + Delta(Vir_{26-c}) = 6960/[(5c+22)(152-5c)] (Virasoro-specific).

### 6. Projections to Classical Representation Theory

#### 6.1. Koszul duality (genus 0, arity 2)
Tautological by construction.

#### 6.2. Drinfeld-Kohno bridge
| DK-0 | pi_sc | Scalar kappa | Proved |
| DK-1 | pi_{2,0} | Classical r-matrix | Proved |
| DK-2 | pi_{3,0} | CYBE + cubic | Proved (eval core) |
| DK-3 | pi_{2,1} | KZ genus 1 | Proved (eval core) |
| DK-4 | pi_{4,0} | Quartic resonance | Conjectural |
| DK-5 | pi_{*,*} | Full categorical | Conjectural |

Note: shadow-projection identification (constr:dk-shadow-projections) is a conceptual organizing framework, not a separately proved extraction theorem.

#### 6.3. Feigin-Frenkel center
At critical level k=-h^v: kappa=0, tower collapses. Bar COHOMOLOGY (not MC element) recovers oper space. Shadow obstruction tower and Langlands on orthogonal axes.

#### 6.4. Entanglement entropy
Scalar level: CC formula (input from CC, not independently derived).
Shadow corrections delta S_r: determined by Theta^{<=r} on replica geometry.
- Class G: CC exact
- Class M: |delta S_r| <= C*rho^r*r^{-5/2}*log(L/eps), converges for rho < 1
Physical identification with FLM/EW bulk corrections: heuristic, not proved.

#### 6.5. Arithmetic shadows
Depth decomposition: d = 1 + d_arith + d_alg (d_alg defined as remainder; d_arith counts critical lines is theorem content).
Unconditional Ramanujan for lattice VOAs: genuine alternative proof via CPS/Langlands rather than etale cohomology.
Arithmetic comparison conjecture: OPEN.

### 7. Koszulness Characterization
10 unconditional equivalences (PBW collapse, A_infty formality, Ext diagonal vanishing, bar-cobar qi, Barr-Beck-Lurie, FH concentration, ChirHoch vanishing, Kac-Shapovalov nondeg, FM boundary acyclicity + chirally Koszul itself).
1 conditional (Lagrangian criterion).
1 one-directional (D-module purity).
Shadow depth classifies complexity WITHIN the Koszul world.

### 8. The Open Frontier
(1) DK-4/5
(2) Operadic complexity conjecture
(3) Class C: structural or accidental?
(4) Arithmetic comparison conjecture
(5) Complementarity beyond Koszulness
(6) Multi-channel shadow connection

---

## Final Platonic Sentence

The genus expansion of a chirally Koszul algebra is algebraic of degree 2 on primary slices, classified by a computable quadratic discriminant that measures L_infty non-formality and is constrained by Koszul duality to satisfy Lagrangian complementarity.

---

# APPENDIX: CLAUDE.md ERROR FOUND

SERIOUS (AP2): CLAUDE.md lists meta-theorem items incorrectly:
- CLAUDE.md says (ix) = FM boundary acyclicity, (x) = shadow-formality
- Source says (ix) = Kac-Shapovalov, (x) = FM boundary acyclicity
- Shadow-formality is NOT a numbered item in thm:koszul-equivalences-meta

This should be fixed in CLAUDE.md.

---

# END OF THREAD DUMP
