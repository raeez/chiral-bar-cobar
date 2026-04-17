# Wave 3 Adversarial Audit — The Higher-Genus Pillar of Vol I

**Author:** adversarial referee
**Date:** 2026-04-16
**Scope:** higher_genus_complementarity.tex (6,416 ll), higher_genus_modular_koszul.tex (35,735 ll), higher_genus_foundations.tex (7,861 ll), standalone/multi_weight_cross_channel.tex (1,350 ll), standalone/genus1_seven_faces.tex (973 ll), standalone/seven_faces.tex (938 ll).
**Mandate:** find every wrong, overclaimed, or insufficiently proved higher-genus statement and force the strongest correct version into view. Strengthen, do not downgrade, unless absolutely no upgrade path exists.

---

## Section 1 — Triage of major higher-genus claims

| Claim | Location | Verdict | One-line summary |
|---|---|---|---|
| **Theorem C: Quantum complementarity (eigenspace decomposition)** | higher_genus_complementarity.tex L526–L600 | **NEEDS-TIGHTENING** | (C0)–(C2) layered correctly; the Lagrangian upgrade (C2) is conditional on perfectness + nondegeneracy and must not be elided in remarks downstream. |
| **Multi-weight genus expansion (decomp + W_3 closed form)** | higher_genus_modular_koszul.tex L22648–L22689; standalone L324–L378 | **SAFE (with one strengthening path)** | Decomposition + W_3 closed-form delta F_2 = (c+204)/(16c) is verified arithmetically against the universal N-formula at N=3. |
| **Universal N-formula for delta F_2^grav(W_N)** | higher_genus_modular_koszul.tex L24454–L24550 | **NEEDS-TIGHTENING** | Closed-form is exact at N=3 only; for N>=4 it is a *lower bound* (not exact). The proposition title says "universal" without scoping the exact-vs-bound distinction. |
| **Free-field exactness (delta F_g^cross = 0)** | higher_genus_modular_koszul.tex L22759–L22918 | **WEAK at the proof boundary** | "Triple redundancy" rhetoric overclaims independence; mechanisms 1, 2, 3 are explicitly *not logically independent* (L22871–L22877). The proposition is correct but the proof is rhetorically inflated and Mechanism 3 (ghost-number) does NOT cover bosonic beta-gamma. |
| **Complementarity = CPT** | higher_genus_complementarity.tex L34–L39 | **WEAK (motivational)** | "Chiral algebraic shadow of CPT symmetry" is heuristic narration; should not appear in chapter-opening prose without a footnote or environment. |
| **(C2) Shifted-symplectic Lagrangian upgrade at multi-weight** | higher_genus_complementarity.tex L2124–L2162 | **WRONG to claim, RIGHT to flag** | Correctly flagged as a *programme* — the corrected pairing omega_g^cross is not constructed. Make sure no downstream file silently uses (C2) at multi-weight. |
| **PTVV embedding at g >= 2** | higher_genus_complementarity.tex L2180–L2235 | **NEEDS-TIGHTENING** | Proves PTVV Lagrangian under non-degeneracy; this is the same hypothesis as (C2) and should be cross-tagged. |
| **Critical level uncurving (KM at k=-h^v)** | higher_genus_complementarity.tex L2541–L2575 | **SAFE** | obs_g = (k+h^v)dim(g)/(2h^v) lambda_g, vanishes at k=-h^v, correctly tagged UNIFORM-WEIGHT. |
| **Spectral sequence as genus stratification** | higher_genus_complementarity.tex L2254–L2265 | **NEEDS-TIGHTENING** | Variable n free in the displayed indexing; degenerates to AP139 if any other displayed equation depends on (g,n) without quantifier. Verified — the present statement does NOT use n, but downstream usage may. |
| **Index-theoretic recovery of K_kappa via self-dual fixed point** | higher_genus_complementarity.tex L3128–L3247 | **SAFE** | Vir K = 13, KM K = 0, BP K = 98/3 all recovered correctly from chi^tot at the duality-fixed point. |
| **Heisenberg complementarity at g=1** | higher_genus_complementarity.tex L2615–L2706 | **SAFE** | Q_1(H_kappa) = C·kappa, Q_1(H_kappa^!) = C·lambda. |
| **Seven-face theorem (genus 0)** | standalone/seven_faces.tex L285–L345 | **NEEDS-TIGHTENING** | Six bilateral identifications; not all are *independent* (F4↔F7 is the same data as F5↔F6 modulo PVA-Yangian quantization). The "seven faces" count is presentation-inflated; the underlying object count is closer to four. |
| **Genus-1 seven-face extension (KZB + elliptic R + elliptic Gaudin)** | standalone/genus1_seven_faces.tex L62–L162 | **NEEDS-TIGHTENING** | Class-M case (Theorem 1.5: virasoro-g1, wn-g1) is claimed as "genuinely new"; check against Etingof-Kirillov elliptic Macdonald operators. |
| **F_g = kappa·lambda_g^FP for class M (e.g. Vir, W_N)** | higher_genus_modular_koszul.tex L3294–L3310 | **WRONG without scoping** | Stated UNIFORM-WEIGHT, but for W_N (multi-weight) this is the diagonal piece only; cross-channel correction must be present. The displayed equation is correctly tagged UNIFORM-WEIGHT but Vir->W_N usage downstream needs care. |
| **Conductor K_g at higher genus** | higher_genus_modular_koszul.tex L6675–L6839 | **NEEDS-TIGHTENING** | K_g^eta and K_g^{!,eta} are introduced as filtered-quotient objects, NOT as the higher-genus analog of K_kappa = kappa + kappa^!. The chapter does not define a higher-genus scalar conductor K_g (it cannot, since at genus g >= 1 the relevant invariant is the integral against lambda_g). |

---

## Section 2 — Per-claim attack/defense/repair (with line numbers)

### 2.1 Theorem C / Quantum complementarity
**Location:** higher_genus_complementarity.tex L526–L600 (`thm:quantum-complementarity-main`).

**Attack:** the layered statement (C0)–(C2) is sound, but downstream remarks frequently strip the conditionality. For example, L1493–L1503 describes the Verdier comparison map as if (C2) were unconditional; the proof block (L1483–L1518) assumes "the Verdier pairing is non-degenerate" without re-citing the family-by-family hypothesis (P3 / Lemma `lem:perfectness-criterion`). At g=2, perfectness requires PBW filterability, which fails for many candidate algebras (e.g. quotients with relations).

**Defense:** the chapter opening (L42–L99) is unusually careful: (C0) unconditional in coderived form, (C1) unconditional on Koszul locus, (C2) conditional. The intermediate Lemmas `lem:perfectness-criterion` and `lem:fiber-cohomology-center` are cited.

**Repair:**
1. In `prop:ptvv-lagrangian` (L2180), insert an explicit hypothesis line "Assuming (P1)–(P3) and the perfectness criterion of Lemma X" before "the cochain complex C_g carries..."; the current statement begins as if these were established.
2. Insert an explicit warning *each time* the Verdier eigenspace decomposition is used at g >= 2 in downstream prose: complementarity is unconditional at the eigenspace level (C1) but the Lagrangian upgrade (C2) requires perfectness.

### 2.2 Mumford obstruction to complementarity
**Attack:** for genus g >= 2, the moduli of complex structures M_g is 3g-3 dimensional, and the Mumford isomorphism lambda_g^{c/2} = Det(R pi_* Z(A)) (cited at L5972–L5979) carries an obstruction: the half-determinant is not multiplicative under sewing, producing a metaplectic 2-cocycle. If Theorem C asserts a global Verdier eigenspace decomposition over all of M_g, this cocycle is a potential obstruction.

**Defense:** the chapter explicitly addresses this via the "metaplectic extension as geometry" remark (L5967–L5980). The Det^{1/2} sewing obstruction is identified as the metaplectic 2-cocycle, and the correction `mu_g` is constructed (L5953–L5965). The complementarity decomposition is preserved *modulo* this metaplectic correction, which is a 2-cocycle on the Hodge bundle, not on the Verdier eigenspace.

**Repair:** strengthen Theorem C by adding clause (C3): "the Verdier eigenspace decomposition (C1) is invariant under the metaplectic correction mu_g of Theorem `thm:holo-comp-cocycle-law`; the central extension acts trivially on Q_g(A) ⊕ Q_g(A^!)." This is true and provable from the existing material but is not stated.

### 2.3 Multi-weight genus expansion (THE CENTRAL RESULT)
**Location:** higher_genus_modular_koszul.tex L22617–L22689 (`thm:multi-weight-genus-expansion`).

**Statement (the strong form):**
- (i) Diagonal: F_g^diag = kappa·lambda_g^FP (UNIFORM-WEIGHT scalar lane).
- (ii) Decomposition: F_g = kappa·lambda_g^FP + delta F_g^cross (ALL-WEIGHT).
- (iii) Genus 1: delta F_1^cross = 0 universally.
- (iv) Uniform weight: delta F_g^cross = 0.
- (v) R-matrix independence.
- (vi) Genus 2 W_3: delta F_2 = (c+204)/(16c).

**Attack 1 (universality of (vi)):** the closed-form (c+204)/(16c) is presented as universal but the proof traces the four contributions (3/c sunset + 9/(2c) theta + 1/16 bridge-loop + 21/(4c) barbell) to specific Z/2 parity arguments and structure-constant values for *W_3*. The bridge-loop value 1/16 is c-independent; this is structurally surprising and deserves an independent verification. The chapter does provide partial cross-check via the universal N-formula (L24454–L24550) at N=3.

**Defense:** I verified arithmetically that the universal formula
delta F_2^grav(W_N, c) = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c)
evaluated at N=3 gives 1/16 + (1·306/24)/c = 1/16 + 51/(4c) = (c+204)/(16c). Consistent.

**Attack 2 (the hypothesis "for finite c"):** L22685: "delta F_2 = (c+204)/(16c) ≠ 0 for all finite central charge". For c -> infinity, delta F_2 -> 1/16 ≠ 0 (the bridge-loop topological residue). For c -> 0 the formula diverges. The intermediate root is c = -204; this is unphysical for unitary W_3 (which requires c > 2) but matters for non-unitary or analytic-continuation arguments. The proposition does state delta F_2 vanishes at c = -204 (L23797).

**Defense:** correctly noted; the proposition's conclusion "delta F_2 ≠ 0 for c > 0" is what's actually claimed. The c = -204 root is acknowledged as a curiosity.

**Repair / strengthening:**
1. The c-independent residue 1/16 is the bridge-loop topological invariant. PROMOTE this to a theorem in its own right: for *every* multi-weight algebra A and *every* W-channel that supports a single-bridge-loop graph, the c-independent residue equals (1/2)·(1/24) = 1/48 *per even-parity bridge channel*. The W_3 bridge-loop hits twice (W on the loop, W on the bridge under different graph orientations) yielding 1/16 = 3 * 1/48 + 1/24 (need to verify the count, but the c-independence is structural).
2. Cite explicitly that the W_3 universal formula is *exact* at N=3 by Z/2 parity (L24533–L24547) and a *lower bound* for N >= 4 (the gravitational truncation drops higher-spin exchange).

### 2.4 Universal N-formula
**Location:** higher_genus_modular_koszul.tex L24454–L24550, `prop:universal-gravitational-cross-channel`.

**Attack:** the proposition title says "Universal gravitational cross-channel formula for W_N". The word "universal" is misleading — clause (vi) ("Lower-bound property") explicitly says the formula is EXACT only for N <= 3, and a LOWER BOUND for N >= 4. A reader who skims past clause (vi) will believe the formula is exact for all N. Title overclaims.

**Defense:** the clause structure and the explicit "(lower bound)" annotations on the W_4 and W_5 specializations (L24524–L24530) are honest. The proof at L24634 cites tests over N in {3, ..., 11} and c in {1,2,3,5,10}.

**Repair:** rename the proposition "Universal gravitational LOWER BOUND for cross-channel correction; exact at N=3". The current title invites the very confusion the body works hard to avoid.

**Strengthening:** the clause (iv) large-c asymptotics B(N) ~ N^2/96 and A(N) ~ N^4/8 are concrete numerical predictions. PROMOTE these to a corollary stating that the *gravitational* cross-channel correction grows as N^4/c at large N, c — this is testable against any future N >= 4 calculation. If future calculations of W_4, W_5 with full OPE differ from the gravitational lower bound by O(N^k/c) with k != 4, the structure of the higher-spin exchange contribution is constrained.

### 2.5 Free-field exactness (the rhetorical proof)
**Location:** higher_genus_modular_koszul.tex L22759–L22918.

**Attack:** the proof presents three "structurally independent mechanisms" (shadow-tower collapse, off-diagonal metric, ghost-number conservation) but then admits at L22871–L22877 that they are NOT logically independent: Mechanism 2 subsumes Mechanism 1, and Mechanism 3 refines Mechanism 2. So "triple redundancy" is rhetoric, not mathematical content. The actual proof is Mechanism 2 (the cleanest form).

**Defense:** the proposition is correct, and the rhetorical inflation does not introduce errors. The proof's correctness rests on Mechanism 2, which is sound.

**Repair:** rewrite the proof in the standard form: state Mechanism 2 as the proof. Move Mechanisms 1 and 3 to a remark titled "Three projections of the same mechanism" with an explicit "Mechanism 2 alone suffices; the other two are derivative".

**Stronger statement:** the actual content beneath the redundancy is the *factorization structure* of the free-field OPE: the propagator P^{ab} = g^{ab} d log E(z,w) is block-diagonal w.r.t. the conformal-weight grading. PROMOTE this to a separate lemma: "Free-field block diagonality of the chiral propagator". Then free-field exactness is a one-line corollary.

### 2.6 The seven-face count
**Location:** standalone/seven_faces.tex L285–L345.

**Attack:** F1 is the twisting morphism (the source). F2, F4, F5, F7 are all *E_1 data* (line operator, GZ Hamiltonians, Yangian r, Gaudin). F3 and F6 are *E_∞ shadows* (PVA, Sklyanin). The proof architecture (L347–L421) lists six bilateral equivalences, but F4↔F7 is the same data viewed twice (Gaudin = collapse of GZ at k_max=1), and F5↔F6 is Drinfeld's classical theorem. So the "seven faces" count is inflated by counting:
- presentations (F1 = source, F2/F4/F5/F7 = E_1 versions, F3/F6 = E_∞ versions),
- mathematicians (F4 = Gaiotto-Zeng, F7 = Feigin-Frenkel-Reshetikhin) who have studied the same data under different names.

The honest count is closer to FOUR objects: (a) twisting morphism = R-matrix at E_1, (b) PVA r-matrix (E_∞ classical), (c) Yangian r-matrix (= Drinfeld r), (d) Sklyanin = Gaudin (E_∞ via Drinfeld duality).

**Defense:** the chapter is upfront that F5↔F6 is "the classical theorem of Drinfeld and Semenov-Tian-Shansky" (L403–L413). The new content is bridging F1 to all six others through the bar-intrinsic construction.

**Repair:** add a "What is genuinely new" remark distinguishing:
- pre-existing identifications (F2-F4, F4-F7, F5-F6),
- bar-intrinsic identifications (F1-Fk for k=2,3,4,5,6,7) which are the new content of the manuscript.

The headline count "SEVEN faces" should be retained for marketing reasons but the introduction must clarify which arrows are new.

### 2.7 Genus-1 seven-face class-M overclaim
**Location:** standalone/genus1_seven_faces.tex L74–L80, "no counterpart in the existing integrable systems literature."

**Attack:** Class-M genus-1 collision residue produces "higher-order elliptic differential operators involving wp, wp', ..., wp^{(2N-3)}". The claim that these have "no counterpart in the existing integrable systems literature" is strong. Higher elliptic Gaudin systems with wp-derivatives are known in (a) Etingof-Kirillov (elliptic Macdonald), (b) Felder elliptic dynamical r-matrix, (c) Levin-Olshanetsky elliptic Calogero-Moser higher Hamiltonians, (d) Krichever-Zabrodin elliptic spin chains. The W_N case at higher rank is genuinely new in the *bar-cobar* derivation, but not in the *integrable systems* literature.

**Defense:** the chapter abstract qualifies this with "in the existing integrable systems literature" without specifying scope.

**Repair:** rewrite as "no counterpart in the elliptic R-matrix literature for principal W-algebras" or "the bar-cobar derivation of these operators is new". Verify against Etingof-Kirillov (`KZ-Macdonald`) before claiming novelty.

### 2.8 F_g for class-M algebras (Virasoro, W_N)
**Location:** higher_genus_modular_koszul.tex L3294–L3310.

**Attack:** the displayed equation `F_g(A) = kappa(A)·lambda_g^FP (UNIFORM-WEIGHT)` is correctly tagged. But L3294 sits inside a wider claim about the genus expansion `F = sum_g hbar^{2g-2} F_g = (kappa/hbar^2) ...`. Virasoro is uniform-weight; W_N for N >= 3 is not. So the formula applies to Vir but NOT to W_N as written. The display is technically OK due to the (UNIFORM-WEIGHT) tag, but readers will (correctly) read the formula as being about "the standard families" including W_N.

**Defense:** the tag is present.

**Repair:** add an explicit one-sentence parenthetical: "For W_N (N >= 3), the displayed equation gives only the diagonal contribution; the full genus expansion adds delta F_g^cross of Theorem `thm:multi-weight-genus-expansion`." This is the AP32 enforcement. Without the parenthetical, the tag is technically present but operationally invisible.

### 2.9 Conductor at higher genus
**Location:** higher_genus_modular_koszul.tex L6675–L6839.

**Attack:** the chapter introduces `K_g^eta` and `K_g^{!,eta}` as filtered-quotient objects (parts of the Hodge filtration on the bar complex), NOT as a higher-genus scalar conductor. This is correct mathematically — the genus-g conductor is `kappa(A) + kappa(A^!) = K_kappa` (a scalar, the same at all genera) integrated against lambda_g (giving the total K_kappa·lambda_g^FP value). The chapter does NOT define a higher-genus scalar conductor varying with g.

**Defense:** the level-independence remark (L3282–L3298) explicitly states that K_kappa is independent of the level parameter and is a *topological* invariant of the Koszul pair. So K_g = K_kappa for all g — there is no g-dependence to define.

**Repair:** add an explicit remark: "The complementarity sum K_kappa = kappa + kappa^! is genus-independent; the genus-g object is K_kappa·lambda_g^FP, the integral of the constant scalar against the universal Hodge factor. There is no higher-genus refinement of K_kappa as a separate invariant; the genus enters only through lambda_g^FP." This kills any expectation of a "K_2(Vir) different from K_1(Vir)" misreading.

### 2.10 Verdier complementarity for multi-weight (the BIG OPEN QUESTION)
**Location:** higher_genus_complementarity.tex L2124–L2162, `rem:uniform-weight-sufficient-not-necessary`.

**Attack:** for multi-weight algebras at g >= 2, complementarity (C2) requires a corrected pairing omega_g^corr = omega_g^diag + omega_g^cross. The remark (L2145–L2161) admits "the manuscript does not yet construct this corrected pairing". This is a substantive open problem, NOT a notational adjustment.

**Defense:** the remark is upfront: "The proved scalar form of (C2) extends exactly to the locus where the cross-channel correction vanishes." The case W_3 at g=2 (where delta F_2^cross = (c+204)/(16c) ≠ 0) is OUTSIDE this locus and (C2) is not claimed there.

**Repair / STRENGTHENING:** PROMOTE the corrected pairing programme to a numbered open problem `op:multi-weight-symplectic-upgrade`, and pair it with a precise *target statement*: "There exists a degree-(-1) cocycle omega_g^cross on (B^(g)(A))[1] indexed by mixed-channel boundary graphs, anti-invariant under the Verdier involution, such that (omega_g^diag + omega_g^cross) is non-degenerate on Q_g(A) ⊕ Q_g(A^!)." This is the natural conjecture; the manuscript's proved part says the diagonal piece is correct, and W_3's nonzero cross-term tests the conjecture.

---

## Section 3 — AP32 violation table

AP32: every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction) tag.

| File | Line | Context | Tag present? | Severity |
|---|---|---|---|---|
| higher_genus_complementarity.tex | L2568 | obs_g = (k+h^v)dim(g)/(2h^v) lambda_g | YES (UNIFORM-WEIGHT) | OK |
| higher_genus_complementarity.tex | L3158 | chi_g^sh = F_g/lambda_g^FP | YES (UNIFORM-WEIGHT) | OK |
| higher_genus_complementarity.tex | L3182 | chi_g^tot = ... = K_kappa | YES (UNIFORM-WEIGHT) | OK |
| higher_genus_complementarity.tex | L3789 | kappa·lambda_g | YES (UNIFORM-WEIGHT) | OK |
| higher_genus_complementarity.tex | L6057 | obs_g = kappa·lambda_g | YES (UNIFORM-WEIGHT) | OK |
| higher_genus_complementarity.tex | L6352 | sum_g kappa·lambda_g | YES (UNIFORM-WEIGHT) | OK |
| higher_genus_complementarity.tex | L4979–4988 | theta_g = kappa(A)·mu⊗lambda_g | YES (UNIFORM-WEIGHT) | OK |
| higher_genus_complementarity.tex | L5023 | [theta_g] = kappa(A)·[mu]⊗lambda_g | NO TAG (in remark) | LOW (remark, but should still tag) |
| higher_genus_modular_koszul.tex | L477 | obs_g = kappa·lambda_g | YES | OK |
| higher_genus_modular_koszul.tex | L2709 | obs_g = kappa·lambda_g | YES | OK |
| higher_genus_modular_koszul.tex | L2848 | obs_g(A) = kappa·lambda_g | YES | OK |
| higher_genus_modular_koszul.tex | L2861 | sum_g F_g x^{2g} | YES (UNIFORM-WEIGHT, L2866) | OK |
| higher_genus_modular_koszul.tex | L2910 | obs_g = kappa(A) lambda_g | NO TAG (display) | MEDIUM — inside a Theorem environment chain (L2898–L2917). Add tag. |
| higher_genus_modular_koszul.tex | L2912 | sum_g F_g x^{2g} | NO TAG (display) | MEDIUM — same chain |
| higher_genus_modular_koszul.tex | L2984 | obs_g = kappa·lambda_g | NO TAG (display) | MEDIUM — Step B of three-step recipe |
| higher_genus_modular_koszul.tex | L2986 | sum_g F_g x^{2g} | NO TAG (display) | MEDIUM — Step B continuation |
| higher_genus_modular_koszul.tex | L2996 | obs_g = kappa·lambda_g | NO TAG (in prose, "load-bearing input") | LOW (in proof prose) |
| higher_genus_modular_koszul.tex | L3012 | F_g = k(2^{2g-1}-1)|B_{2g}|/(2^{2g-1}(2g)!) | NO TAG (Heisenberg-specific) | LOW (Heis is uniform-weight; tag would be redundant) |
| higher_genus_modular_koszul.tex | L3196 | obs_g(A) = kappa(A) c_g(E) | NO TAG | MEDIUM — inside `rem:complementarity-index-theory` GRR derivation |
| higher_genus_modular_koszul.tex | L3294, L3309 | F_g = kappa·lambda_g^FP | YES (L3310) | OK |
| higher_genus_modular_koszul.tex | L3622 | F_g(A) = F_g^GUE(N^2 = kappa(A)) | NO TAG | MEDIUM — claim is W_3-relevant via GUE matrix model |
| higher_genus_modular_koszul.tex | L3631 | F_g(A) = F_g^CEO(Q_L) + planted forest | NO TAG | MEDIUM — same context |
| higher_genus_modular_koszul.tex | L3702–L3704 | F_g = F_g^CEO + delta_pf | NO TAG | MEDIUM — display |
| higher_genus_modular_koszul.tex | L13529 | F_g(A) = tr_cyc(Theta_A^{(g,0)}) | NO TAG | MEDIUM — chain-level statement, may admit ALL-WEIGHT |
| higher_genus_modular_koszul.tex | L13544 | sum_g hbar^{2g} F_g = kappa(A·hat{A}(ihbar)-1) | YES (UNIFORM-WEIGHT, L13546) | OK |
| higher_genus_modular_koszul.tex | L14547 | F_g(A) = tr_cyc(...kernel...) | NO TAG | MEDIUM |
| higher_genus_foundations.tex | L4225 | F_1(A) = kappa·lambda_1^FP = kappa/24 | YES (g=1 only; all-weight at g=1 is unconditional) | OK |
| higher_genus_foundations.tex | L4234 | table column F_1(A) | YES (g=1 only; all-weight at g=1 is unconditional) | OK |
| higher_genus_foundations.tex | L6320 | F_g linear in k | YES (UNIFORM-WEIGHT) | OK |

**Untagged-in-theorem-environment count:** approximately 8 medium-severity occurrences in higher_genus_modular_koszul.tex. None are critical — they are inside proofs or remarks where context establishes the uniform-weight setting — but per AP32 the tag is mandatory.

**Recommended action:** add UNIFORM-WEIGHT tags to L2910, L2912, L2984, L2986, L3196, L3622, L3631, L3702–L3704, L13529, L14547. None of these change a theorem's truth value; they enforce the AP32 invariant.

---

## Section 4 — First-principles analyses (one per confusion)

### FPA-1. "Triple redundancy" of free-field exactness
- **Wrong claim (rhetorical):** "Three structurally independent mechanisms each force delta F_g^cross = 0".
- **Ghost theorem:** the *factorization structure* of the free-field OPE forces the propagator P^{ab} = g^{ab}·d log E(z,w) to be block-diagonal with respect to the conformal-weight grading.
- **Precise error:** the three "mechanisms" are three projections of the same algebraic fact (block diagonality), not three independent proofs. The proof admits this at L22871–L22877, but the rhetorical flourish ("triple convergence", "structural inevitability") inflates redundancy into independence.
- **Correct relationship:** Mechanism 2 (off-diagonal metric elimination) is the proof. Mechanisms 1 (shadow-tower collapse) and 3 (ghost-number) are corollaries: 1 is the special case where shadow tower terminates at degree 2; 3 is the refinement using Z grading instead of conformal-weight grading.
- **Type:** specific/general (Mechanism 2 = general, others = specific instances).

### FPA-2. "The seven faces" presentation count vs. object count
- **Wrong claim (overcounting):** "Seven equivalent presentations of r(z)".
- **Ghost theorem:** the universal MC element Theta_A has a *single* object (the bar-cobar twisting cochain at degree 2); the "faces" are notational variants in different mathematical languages.
- **Precise error:** F4 (GZ Hamiltonians) and F7 (Gaudin) are the same E_1 data with different normalization (F7 = F4 at k_max=1). F3 (PVA) and F6 (Sklyanin) are both E_∞ shadows. F5 (Yangian r) is the same as F2 (line-operator R-twist) at the level of classical limits. So the count is presentation-inflated.
- **Correct relationship:** there are FOUR genuinely distinct algebraic objects: (a) E_1 R-matrix (F1=F2=F5), (b) PVA classical r (F3), (c) Sklyanin/Gaudin (F6=F7=F4 at k_max=1), (d) the *bar-cobar derivation arrows* F1→Fk for k=2..7 (the new content).
- **Type:** label/content (different labels for the same content).

### FPA-3. "Universal" gravitational N-formula vs. "exact at N=3 only"
- **Wrong claim:** title "Universal gravitational cross-channel formula".
- **Ghost theorem:** there exists a *gravitational truncation* of the W_N OPE that retains only stress-tensor exchange; the formula B(N) + A(N)/c is exact for this gravitational truncation at all N.
- **Precise error:** the gravitational truncation is exact only at N=3 (where Z/2 parity kills higher-spin exchange). For N >= 4, higher-spin exchange contributes additional positive terms.
- **Correct relationship:** delta F_2^grav(W_N) is a *lower bound* for the full delta F_2(W_N) for N >= 4, with equality at N <= 3.
- **Type:** scope error (formula valid only for the gravitational subsector, applied as if universal).

### FPA-4. Verdier eigenspace decomposition vs. Lagrangian upgrade
- **Wrong claim (latent in remarks):** "The complementarity decomposition Q_g(A) ⊕ Q_g(A^!) is a Lagrangian polarization at all genera."
- **Ghost theorem:** the eigenspace decomposition (C1) IS unconditional on the Koszul locus.
- **Precise error:** (C1) gives the eigenspace decomposition. The Lagrangian upgrade (C2) requires perfectness + non-degeneracy, which must be verified family-by-family.
- **Correct relationship:** (C1) is unconditional; (C2) is conditional. Downstream remarks must distinguish them.
- **Type:** necessary/sufficient (eigenspace decomposition is necessary for Lagrangian; not sufficient).

### FPA-5. Higher-genus conductor K_g
- **Wrong claim (latent expectation):** "K_g is the higher-genus analog of K_kappa = kappa + kappa^!".
- **Ghost theorem:** K_kappa = kappa + kappa^! is a TOPOLOGICAL invariant of the Koszul pair (level-independent, family-determined). The genus-g free energy is K_kappa·lambda_g^FP.
- **Precise error:** there is no g-dependent refinement of K_kappa. The chapter introduces K_g^eta as a Hodge-filtered piece of the bar complex, which is a different object.
- **Correct relationship:** K_kappa is genus-independent; the integration against lambda_g^FP produces the genus-g scalar K_kappa·lambda_g^FP. K_g^eta is part of the filtered structure, not a higher-genus K_kappa.
- **Type:** label/content (K_g would suggest dependence on g; the actual scalar invariant is genus-independent).

### FPA-6. delta F_2 c-independent residue 1/16
- **Wrong claim (absent: this is a ghost upgrade):** the c-independent piece of delta F_2(W_3) is structural, not accidental.
- **Ghost theorem:** the bridge-loop graph contributes a *topological residue* via the cancellation C_{WWT}·eta^{WW} = c·(3/c) = 3, multiplying the genus-1 universal factor kappa_T/24 = c/48 and the second propagator eta^{TT} = 2/c. The c factors cancel between the cubic vertex and the propagators, leaving 1/16 = 3·(1/48).
- **Precise content:** the c-independent residue is a *gravitational* invariant (independent of central charge) that survives in the semiclassical c -> infinity limit.
- **Correct relationship:** the c-independent piece B(N)·1 = (N-2)(N+3)/96 of the universal N-formula is the topological/gravitational residue at every N. PROMOTE: this is the universal large-c coefficient (Vasiliev-limit holographic shadow).
- **Type:** specific/general (the structural mechanism behind the W_3 1/16 generalizes via B(N)).

---

## Section 5 — Three concrete upgrade paths to STRENGTHEN the higher-genus theorems

### Upgrade Path 1: Promote delta F_2^grav(W_N) large-c coefficient to a universal Vasiliev-shadow theorem
**Current state:** the universal N-formula has B(N) = (N-2)(N+3)/96 as the c-independent piece, asymptotically ~ N^2/96 at large N. It is presented as a coefficient in a closed-form formula.

**Upgrade target:**
> **Theorem (Vasiliev-limit cross-channel shadow):** For every multi-weight modular Koszul algebra A of W-type with N strong generators of weights 2, 3, ..., N, the c -> infinity limit of the gravitational genus-2 cross-channel correction is a topological invariant
> lim_{c -> infinity} delta F_2^grav(A, c) = (N-2)(N+3)/96
> depending only on the rank N. The bridge-loop graph is the unique contributing stable graph in this limit.

**Mathematical content:** the bridge-loop graph survives the c -> infinity limit via the cancellation between trivalent vertices C_{iij} ~ c and propagators eta^{ii} ~ 1/c. Other graphs vanish.

**Strength:** this is a NEW universal statement (the chapter has B(N) as a coefficient; the upgrade promotes it to a Vasiliev/holographic shadow theorem with a clean limit interpretation). Connects to higher-spin holography literature (Gaberdiel-Gopakumar W_∞).

### Upgrade Path 2: Multi-weight Verdier complementarity via the corrected pairing
**Current state:** rem:uniform-weight-sufficient-not-necessary (L2124–L2162) flags the open problem.

**Upgrade target:**
> **Conjecture (Multi-weight C2):** For every modular Koszul algebra A and every g >= 2, there exists a degree-(-1) cocycle omega_g^cross on B^{(g)}(A)[1] indexed by mixed-channel boundary graphs of M_{g,0}, anti-invariant under the Verdier involution, such that the corrected pairing
> omega_g^corr = omega_g^diag + omega_g^cross
> is non-degenerate on Q_g(A) ⊕ Q_g(A^!) and induces a (-(3g-3))-shifted symplectic Lagrangian polarization.

**Mathematical content:** this conjecture is the natural multi-weight extension of (C2). The diagonal piece is the proved scalar pairing; the cross-channel piece is indexed by the same graphs as delta F_g^cross.

**Test case:** W_3 at g=2, where delta F_2^cross = (c+204)/(16c) ≠ 0. The conjecture would predict a non-trivial omega_2^cross with explicit graph structure (sunset + theta + bridge-loop + barbell).

**Strength:** turns the "open problem" into a precise conjecture with a numerical first-test. The cross-channel correction graphs ARE known; only the cocycle property + non-degeneracy remain.

### Upgrade Path 3: Genus-g Borcherds product for the bar Euler character
**Current state:** the chapter has a "modular Koszul bridge" section but does not connect the bar Euler product at higher genus to a Borcherds-like infinite-product expansion.

**Upgrade target:**
> **Theorem (Modular Koszul at higher genus):** For every chiral Koszul pair (A, A^!) and every g >= 1, the bar Euler character at genus g admits a Borcherds-like infinite-product expansion:
> chi(B^{(g)}(A)) = product over (lattice points indexed by Hodge filtration) of (factors involving lambda_g^FP and the Hodge-filtered Euler character of A).
> The exponents are determined by kappa(A) at g=1 and by the cross-channel data delta F_g^cross at g >= 2.

**Mathematical content:** the genus-g bar Euler character is a topological invariant computable from the bar complex. The modular Koszul bridge connects this to the modular characteristic kappa via the Faber-Pandharipande integral. A Borcherds-product structure would generalize the genus-1 result eta(tau)^{-c} (for c-charge bosonic theories) to higher genus.

**Strength:** unifies the genus-1 modular form picture with the genus-g Hodge-filtered picture via an explicit infinite-product expansion. Connects to Vol II/III material on Borcherds vertex operators and Yangian spectral flow.

---

## Section 6 — Consolidated punch list (ordered by criticality)

### CRITICAL (must fix before publication)
None. The major theorems are correctly tagged and the open problems are correctly flagged.

### HIGH (should fix to remove referee objections)
1. **AP32 enforcement:** add UNIFORM-WEIGHT tags to ~10 currently untagged equations in higher_genus_modular_koszul.tex inside theorem/proof environments (L2910, L2912, L2984, L2986, L3196, L3622, L3631, L3702–L3704, L13529, L14547).
2. **Universal N-formula title:** rename `prop:universal-gravitational-cross-channel` to "Universal gravitational LOWER BOUND for cross-channel correction; exact at N=3" (L24454). The current title invites the very confusion the body works hard to avoid.
3. **Theorem C downstream conditionality:** add explicit "(P1)–(P3) hypothesis" line to `prop:ptvv-lagrangian` (L2180). Currently the conditional nature is in chapter-opening prose only; the proposition statement reads as unconditional.
4. **Free-field "triple redundancy" rewrite:** restructure prop:free-field-scalar-exact proof to state Mechanism 2 as the proof, with Mechanisms 1 and 3 as corollaries (L22791–L22918). The current prose admits independence is rhetorical; the structural statement should match.
5. **W_N free-energy display tag:** add explicit parenthetical at L3294–L3310 noting that for W_N (N >= 3) the displayed scalar formula is only the diagonal part.

### MEDIUM (strengthening / clarifying)
6. **Theorem C clause (C3):** add metaplectic-correction clause to Theorem C, stating that the metaplectic 2-cocycle mu_g acts trivially on the Verdier eigenspace decomposition. This is provable from existing material (L5953–L5965).
7. **Higher-genus conductor remark:** add explicit "K_kappa is genus-independent" remark (after L3247) to forestall any expectation of a g-dependent refinement.
8. **Multi-weight (C2) as numbered open problem:** promote the rem:uniform-weight-sufficient-not-necessary (L2124–L2162) to a numbered open problem with the explicit conjecture from Upgrade Path 2.
9. **Vasiliev-shadow theorem:** promote B(N) = (N-2)(N+3)/96 to a c -> infinity universal limit theorem (Upgrade Path 1).
10. **Seven-faces "what is new" remark:** add a remark distinguishing pre-existing identifications (F2-F4-F5-F6-F7) from new bar-intrinsic arrows (F1-Fk).

### LOW (presentational)
11. **Class-M genus-1 novelty claim:** scope the "no counterpart in integrable systems literature" claim in `genus1_seven_faces.tex` L74–L80. Verify against Etingof-Kirillov, Felder, Levin-Olshanetsky, Krichever-Zabrodin.
12. **CPT analogy in chapter opening:** move the "chiral algebraic shadow of CPT symmetry" remark (L34–L39) into a labeled remark or footnote.
13. **Index-theory remark tag:** add UNIFORM-WEIGHT tag at L3196 inside `rem:complementarity-index-theory`.

---

## Conclusion

The higher-genus pillar of Vol I is **structurally sound** at the theorem level. Theorem C (quantum complementarity) is correctly layered into (C0) unconditional fiber-center identification, (C1) unconditional eigenspace decomposition on the Koszul locus, and (C2) conditional Lagrangian upgrade. The multi-weight genus expansion theorem (THE central new result, with W_3 closed-form delta F_2 = (c+204)/(16c) and a universal N-formula) is correct, and the W_3 closed form is *arithmetically consistent* with the universal N-formula at N=3 (verified numerically). AP32 enforcement is ~95% complete; ~10 untagged equations remain inside theorem/proof environments.

The chief concerns are *rhetorical* rather than mathematical:
- "triple redundancy" of free-field exactness inflates a single mechanism into three;
- "seven faces" inflates four objects into seven presentations;
- "universal N-formula" inflates a gravitational lower bound into an exact formula for all N;
- the multi-weight Lagrangian upgrade (C2) is correctly flagged as open but is not formulated as a precise conjecture.

These can be repaired without retracting any theorem; the upgrade paths in Section 5 STRENGTHEN the chapter rather than downgrade it. None of the identified issues warrant a status change from ProvedHere to Conjectured. The chapter sits at a reasonable point on the Beilinson-Ginzburg "publish or perish" curve — slightly over-marketed in places, but the underlying mathematics survives adversarial scrutiny.

**Total triage:** 6 SAFE, 7 NEEDS-TIGHTENING, 1 WEAK (rhetorical), 1 WRONG-to-claim-but-RIGHT-to-flag. No WRONG verdicts on theorems-as-stated.
