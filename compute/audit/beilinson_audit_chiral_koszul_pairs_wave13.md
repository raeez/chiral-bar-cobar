# Beilinson Audit: chiral_koszul_pairs.tex (Wave 13)

Target: /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex (5446 lines)
Mode: read-only, six-hostile-examiner adversarial pass.
Focus: thm:koszul-equivalences-meta (L1900-1959), Wave 5-5 insertions (L2429-2589), and AP compliance on load-bearing material.

## Per-examiner finding counts

| Examiner          | Findings | Severity distribution             |
|-------------------|----------|-----------------------------------|
| Formalist         | 4        | 1 MAJOR, 2 MODERATE, 1 MINOR      |
| Topologist        | 2        | 1 MODERATE, 1 MINOR               |
| Physicist         | 2        | 2 MINOR                           |
| Number Theorist   | 1        | 1 MODERATE                        |
| Adversarial Chef  | 4        | 2 MAJOR, 1 MODERATE, 1 MINOR      |
| Editor            | 3        | 1 MODERATE, 2 MINOR               |
| **Total**         | **16**   | **3 MAJOR, 6 MODERATE, 7 MINOR**  |

## 12-equivalences verification (L1900-1959)

Statement layout audit of thm:koszul-equivalences-meta:

- (i) chirally Koszul. Precise, refs def:chiral-koszul-morphism. OK.
- (ii) PBW SS collapses at E_2. Precise. OK.
- (iii) Minimal A_inf-model of barBgeom(A) is formal: m_n=0 for n>=3. Precise. OK.
- (iv) Ext diagonal vanishing: Ext^{p,q}_A(omega_X,omega_X)=0 for p != q. Precise. OK.
- (v) bar-cobar counit Omega(barBgeom(A))->A is qi. Precise. OK.
- (vi) Barr-Beck-Lurie comparison is equivalence "on the fiber over barBgeom(A)". **MODERATE (Formalist):** "on the fiber over barBgeom(A)" is never defined in this chapter; the BBL section (L2086-2114) phrases it as "Phi is an equivalence" tout court. The scoping qualifier in the theorem statement and the proof do not match.
- (vii) Factorization homology int_{Sigma_g} A concentrated in degree 0 "for all g". **MAJOR (Adversarial Chef + Topologist):** This is untenable as stated. At genus g>=1 with non-trivial kappa, factorization homology of a Koszul algebra is NOT uniformly concentrated in degree 0 (Virasoro is Koszul but has kappa=c/2 obstructing higher-genus vanishing; cf AP32). The proof only treats g=0 in the (vii)=>(i) direction (L2054-2060 explicitly reduces to Sigma_0=P^1), leaving "for all g" unproved and likely FALSE. Should be restricted to g=0, or accept condition as a strictly stronger refinement that pulls in the kappa=0 locus only.
- (viii) ChirHoch^*(A) polynomial in {0,1,2}. OK but see AP134 note below.
- (ix) Kac-Shapovalov det G_h != 0 in bar-relevant range. Precise. OK.
- (x) i_S^!barB_n(A) acyclic outside degree 0 at every FM boundary stratum S. OK.
- (xi) Lagrangian criterion (transverse Lagrangians in (-1)-shifted symplectic M_comp). Scoped conditional on perfectness. AP99 compliant.
- (xii) D-module purity: each barBgeom_n(A) pure of weight n. Scoped as (xii)=>(x) one-way, with KM converse (prop:d-module-purity-km-equivalence). AP99 compliant.

**Proof circuit arrow inventory:**
- (i)<=>(ii) proved directly; (ii)=>(v) via bar concentration; (v)=>(i) via Lemma-cone; (v)<=>(viii) proved both directions; (ii)<=>(iii) proved both directions; (i)<=>(vii) proved but with the (vii)=>(i) direction silently restricted to g=0 [MAJOR: quantifier mismatch with theorem statement]; (i)<=>(x) proved via FM strata; (i)<=>(vi) proved via BBL; (i)<=>(ix) proved via Kac-Shapovalov; (i)<=>(iv) proved; (i)<=>(xi) proved conditional on perfectness; (xii)=>(x) via Saito, converse open (KM converse proved in prop:d-module-purity-km-equivalence).

**MODERATE (Formalist):** (iv)=>(i) on L2155-2169 invokes "in characteristic zero with a split filtration... the extension problem is trivial: E_infty=E_2 as bigraded objects". The PBW filtration is stated to "split by conformal weight", but this split is not defined nor cited; it is used as if free. The argument requires more care: bigraded collapse modulo extensions needs invoking concreteness of the PBW splitting, not just "characteristic zero".

## Top 5 findings

1. **MAJOR (Chef + Topologist) — Factorization homology equivalence over-claimed at all genera.** Condition (vii) and its "(vii)=>(i)" proof are mismatched on the quantifier. As proved only (g=0 case), either restrict the statement to "int_{P^1} A in deg 0" (proper fix) or add an AP32 UNIFORM-WEIGHT / KAPPA=0 scope tag. As stated, it suggests Virasoro fails Koszulness (since its higher-genus FH has kappa obstructions), contradicting thm:virasoro-chiral-koszul. This is an internal contradiction on a load-bearing theorem.

2. **MAJOR (Chef) — Prop 4904/Prop bar-neq-quasiprimary contradicts Remark 1010/1028.** L1029 asserts "dim H^1(barBgeom(Vir))=1 (a single generator T of conformal weight 2)", but L4922-4925 asserts the sequence (0,1,2,5,12,30,76,...) with dim H^1_4(Vir) = 12 via M(5)-M(4) = 21-9. These cannot both be right without extra scoping (the remark likely means "weight 2 quasi-primary generator count = 1", but the phrasing "dim H^1(barBgeom(Vir)) = 1" is unqualified). Either clarify the remark (weight-2 restriction explicit) or resolve which is correct. The Motzkin-number identification at L4923 is also uncited and not obviously verified against a generating function — potential AP10 / AP123 (enumeration without cross-check).

3. **MAJOR (Formalist) — BBL condition (vi) scoping "on the fiber over barBgeom(A)" undefined.** The phrase is never defined, and the proof drops it entirely, reducing BBL to "Phi is an equivalence" which then appeals to Quillen equivalence "restricted to the Koszul locus". The circuit closes, but the condition as written in the theorem statement does not match what the proof proves. Either remove the fiber qualifier, or define it via the Koszul locus Quillen equivalence explicitly.

4. **MODERATE (Chef) — Kac-Shapovalov proof (ix)=>(ii) uses injectivity of iota without justifying it at ALL bar-relevant weights.** L2127-2142 says "det G_h != 0 means the PBW-to-bar comparison map iota is injective at every bar-relevant weight". The equivalence "nondegeneracy of Shapovalov form <=> injectivity of PBW-to-bar map" is substantive and not cited. Classical Poincare-Birkhoff-Witt injectivity is distinct from the bar-complex-level injectivity needed here. A lemma or explicit reference is missing.

5. **MODERATE (Formalist + Editor) — Iff claimed in (iv)<=>(i) without recording the split-filtration hypothesis in the theorem statement.** The proof at L2155-2169 introduces ad hoc split-filtration hypotheses ("characteristic zero with split filtration") to upgrade E_infty = E_2 from filtered to bigraded. The theorem statement says conditions (i)-(x) are equivalent unconditionally; the split-filtration hypothesis is actually used. AP36 risk: "iff" written but a converse hypothesis is implicit. Either record the hypothesis in the theorem, or strengthen the proof.

## AP compliance on load-bearing material

- **AP1 (kappa operational mandate):** kappa appears in prop:swiss-cheese-nonformality-by-class (L2250+) and in the "class M" computations. At L2334-2337: S_3 = 2kappa/kappa = 2 (c-independent), S_4 = 10/[c(5c+22)], Delta = 8kappa S_4 = 40/(5c+22). The cross-reference to family-specific kappa (kappa^Vir = c/2) is implicit. Acceptable but nit: the class-L entry says "S_3 = 2h^v/(k+h^v)" which is structure constant ratio; fine. **AP1 PASS with nit.**
- **AP14 (Koszul != SC formality):** Explicitly enforced in rem:loop-exactness-ordering (L2237-2248) and prop:swiss-cheese-nonformality-by-class (L2250+), which sharply distinguishes A_inf formality of bar cohomology (always for Koszul) from SC formality of A itself (differs by class). **AP14 PASS.**
- **AP33 (Koszul dual != level-dual):** L5252-5264 AP33 caution remark explicitly records the distinction: widehat{g}_k^! is the linear dual of the bar cohomology, NOT widehat{g}_{-k-2h^v}. **AP33 PASS.**
- **AP75 (Koszulness = PBW degree concentration, NOT conformal weight):** Correct throughout. **AP75 PASS.**
- **AP126 (level-stripped r-matrix):** Only two r-matrix occurrences at L2840 and L2857, both written r^cl(z) = k Omega/z. k=0 vanishing automatic. **AP126 PASS.**
- **AP132 (augmentation ideal in bar complex):** L51, L528, L3374 all correctly use T^c(s^{-1}\bar{A}). The intrinsic Koszul dual at L3581 uses T^c(V^vee) (generator dual, not bar), which is a different construction — acceptable but see AP44 nit below. **AP132 PASS.**
- **AP125 (label prefix matches environment):** All thm: and conj: labels match their environments. **AP125 PASS.**
- **AP136 (H_N harmonic notation):** L4258 kappa(W_N) = c*(H_N - 1) with H_N = sum_{j=1}^N 1/j. Correct. **AP136 PASS.**
- **AP32 (genus-1 != all-genera):** **PARTIAL FAIL** due to finding #1: condition (vii) claims concentration "for all g" without a (UNIFORM-WEIGHT) scope tag; proof only treats g=0. Should be scoped.
- **AP44/45 (desuspension s^{-1}):** L3581 writes A_2^! = T^c(V^vee) without desuspension; the shift is implicit since this is the intrinsic construction from generator dual, but a reader coming from L51 would expect explicit s^{-1}. **MINOR nit.**
- **AP14 enforcement in prop:swiss-cheese-nonformality-by-class:** Proposition header explicitly says "not on bar cohomology H^*(barB(A)), which is always A_inf-formal for Koszul algebras" — exemplary AP14 guarding.

## Additional findings

- **MINOR (Topologist) — Remark "Bar concentration implies H^0 cong A_2^!" (L1080-1106):** The upgrade from "bar cohomology dim = dim A_2^! as vector space" to "as coalgebra" argues by noting twisted tensor product acyclicity upgrades the map. The argument invokes "the identical argument applies because acyclicity of Koszul complexes is the only input beyond the MC equation" — slightly hand-wavy; a stricter attribution to lem:bar-holonomicity + thm:fundamental-twisting-morphisms was added but the reduction is not trivially clear.

- **MINOR (Physicist) — Curvature claim on Vir^! at L4101:** `d_!(T^*) = -c/2 (quartic curvature term)` is intuitive but the actual coalgebra-level curvature assignment is not fully made precise. The example frames this as a "curved coalgebra, a consequence of the central extension" without saying that the curvature lives in the m_0 slot and satisfies the MC equation.

- **MINOR (Physicist) — Sklyanin STS bracket proof (L2869-2889):** The Whitehead Lemma application is sound for semisimple g, but the decomposition pi_{STS} = pi_LP + pi_r "the constant correction pi_r contributes only at the E_0 level" deserves a one-line justification. pi_r is constant in polynomial degree, so its Schouten bracket with itself vanishes, but this is not spelled out.

- **MINOR (Editor) — "One-loop exactness" (rem L1132-1149):** Physically suggestive prose; rather than flagging, this passes but grazes the "RS-1 physics IS the math, not a bridge" constraint. OK as stated.

- **MINOR (Editor) — "AI slop" pass:** Single em dash at L1068 "$\bar{B}^{\mathrm{ch}}(\cA_1) \to \cA_2^!$ is a" (narrative dash, not en/em). Grep confirms no em-dash issues on prose lines. Word-level check: no "notably", "remarkably", "cornerstone", "tapestry", "delve", "leverage". **Editor PASS for prose hygiene.**

- **MINOR (Editor) — Number Theorist concern on AP134:** Condition (viii) states "ChirHoch^* is polynomial with generators concentrated in degrees {0,1,2}". The phrase "polynomial algebra" is compatible with cohomological amplitude [0,2] but only if the generators are specified as a fixed finite set at each degree. CLAUDE.md AP134 warns against conflating cohomological amplitude with virtual dimension — here the amplitude is the claim and that is correct. **Pass with AP134 note in mind.**

## Health grade

**B+** (load-bearing meta-theorem sound in core circuit, but scoping mismatch on condition (vii) is a MAJOR hazard; an internal contradiction between L1029 and Prop bar-neq-quasiprimary must be reconciled; BBL (vi) needs definitional precision.)

### Breakdown
- Formalism / rigor: B+  (Lagrangian + D-module scoping precise; BBL fiber qualifier undefined; Ext diagonal split-filtration ad hoc)
- Proof circuit soundness: A-  (10 unconditional arrows all present; (vii) quantifier mismatch is the one gap)
- AP compliance (126, 132, 125, 136, 14, 33, 75): PASS
- AP32 scoping on (vii): PARTIAL FAIL (needs fix)
- Internal consistency (Motzkin vs "dim H^1 = 1"): FAIL — needs reconciliation
- Prose / editorial: B+ (dependency digest helpful; some phrasings hand-wavy)

## Recommended actions (priority-ordered)

1. Reconcile L1029 ("dim H^1(barBgeom(Vir)) = 1") with L4922-4925 (Motzkin sequence). Either add weight-2 scoping to L1029 or correct one of them. Verify the Motzkin identification against an independent computation or cite a source.
2. Restrict condition (vii) to g=0 (Sigma_0 = P^1) OR tag it (UNIFORM-WEIGHT, g=0) and note that the all-genera version is a Koszulness + trivial-kappa refinement. Either way, remove "for all g" from the unconditional equivalences.
3. Define or delete the "on the fiber over barBgeom(A)" qualifier in condition (vi). Simplify to "the Barr-Beck-Lurie comparison for the bar-cobar adjunction is an equivalence" and let the proof's Koszul-locus reduction stand.
4. Add explicit hypotheses to thm:koszul-equivalences-meta for the split-filtration argument in (iv)=>(i), or cite a reference (LV12 + Boardman) covering the bigraded E_infty=E_2 statement without ad hoc splitting.
5. Minor: add s^{-1} desuspension to the intrinsic Koszul dual definition (L3581), or note that V^vee already carries the shift, to keep AP44/45 bookkeeping uniform across the chapter.
6. Minor: one-line justification in Sklyanin proof (L2869) that pi_r is Schouten-flat because it is constant in polynomial degree.
