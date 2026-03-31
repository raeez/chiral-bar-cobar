# Common Mathematical Errors Agents Make

**Repository**: Vol I — Modular Koszul Duality
**Derived from**: Deep audit of 300+ commits, 6 adversarial audit sessions, plus full analysis of the uncommitted dirty working state (~60 files of in-flight corrections). **215+ distinct error instances** catalogued (2026-03-16 through 2026-03-24).
**Purpose**: Mandatory pre-flight checklist for any agent session touching this codebase.

---

## Error Class 1: FORMULA ERRORS (most frequent, 31+ instances)

### 1A. Kappa formula confusion — THE #1 RECURRING ERROR

**What happens**: The modular characteristic kappa is confused with the Sugawara central charge c, or with c/2, or with other algebra-specific quantities. One wrong formula propagates to 47+ files via copy-paste.

**Specific instances from git history**:
- kappa(V_k(g)) written as `k*dim(g)/(k+h^v)` (= c, the Sugawara formula) or `k*dim(g)/(2(k+h^v))` (= c/2). **Correct**: `dim(g)*(k+h^v)/(2h^v)`. Commits: `05d6eb2`, `6526706`, `5629ee7`, `eb1b70d`, `c28bd2e`, `c0f0e4c`, `43e5ac2`, `6cc99c6`. Blast radius: **47 files**.
- kappa(Vir_c) written as `(26-c)/12`. **Correct**: `c/2`. Commit: `f78bec1`.
- kappa(W_3_c) written as `(c-50)/2`. **Correct**: `5c/6`. Commit: `6cc99c6`.
- kappa(E8) off by factor 8. Commit: from mathematical audit 2026-03-17.
- Legendre dual cubic coefficient `128/3` instead of `64/3`. Same audit.

**Additional instances from dirty working state (currently being corrected)**:
- kappa(KM) in `higher_genus_foundations.tex`: `k*dim(g)/(2h^v)` -> `(k+h^v)*dim(g)/(2h^v)` (the Sugawara normal-ordering shift k -> k+h^v was missing)
- kappa(KM) in `fourier_seed.tex`: table entry `k*dim(g)/(k+h^v)` corrected
- kappa(KM) in `holomorphic_topological.tex`: same correction
- kappa(sl_2) in `preface.tex`: `3k/(k+2)` -> `3(k+2)/4`
- kappa(sl_3) in `preface.tex`: `8k/(k+3)` -> `4(k+3)/3`
- kappa(betagamma) in `thqg_preface_supplement.tex`: `kappa = -1` -> `kappa = c_{bg}/2 = 6lambda^2 - 6lambda + 1`
- kappa(betagamma) in `branch_line_reductions.tex`: `kappa = -2` -> `kappa = 1`
- kappa(W_N) harmonic sum: `H_N = sum_{j=1}^{N-1} 1/j` -> `H_N = sum_{j=1}^{N} 1/j` (N-th harmonic, not (N-1)-st)
- kappa(sl_2 module) in `chiral_modules.tex`: `kappa = k(k+4)/(2(k+2))` -> `kappa = 3(k+2)/4`
- kappa(G_2 Casimir) in `genus_expansions.tex`: `7k/4 + 7/2` -> `7k/4 + 7` (Casimir = dim(g)/2 = 7, not 7/2)

**Diagnostic**: The wrong affine kappa diverges at the critical level k = -h^v; the correct formula vanishes there (uncurved bar complex). If your formula diverges at criticality, it is wrong.

**Prevention rules**:
1. Before writing ANY kappa formula, check `landscape_census.tex` master table.
2. NEVER copy a kappa formula between algebra families without recomputing from first principles.
3. Use the family-qualified notation: kappa^{KM}, kappa^{Vir}, kappa^{W_N}.
4. After writing a kappa formula, verify: does it vanish at the uncurved point? Does kappa + kappa' satisfy the correct complementarity relation for this family?

### 1B. Kappa anti-symmetry overclaim — THE #2 RECURRING ERROR (25+ instances)

**What happens**: "kappa(A) + kappa(A!) = 0 for all Koszul pairs" is stated as universal. This is **FALSE**. It holds only for Kac-Moody and free fields. For W-algebras: kappa + kappa' = K(g) (a nonzero family-dependent constant, e.g., 13 for Virasoro, 250/3 for W_3).

**Git evidence**: 16+ files corrected in the Beilinson mathematical audit (2026-03-23).

**Dirty working state**: The single most pervasive correction currently in flight — **25+ instances across 15+ files** being corrected simultaneously:
- `introduction.tex`: "anti-symmetric under Koszul duality" -> "duality-constrained (kappa + kappa' = 0 for KM/free fields)"
- `higher_genus_modular_koszul.tex`: multiple occurrences; "sign reversal" -> "complementarity relation kappa(A) + kappa(A!) = K(g)"
- `bar_cobar_adjunction_inversion.tex`: same correction
- `preface.tex`: kappa + kappa' = 0 qualified with "(for Kac-Moody and free-field algebras)"
- `concordance.tex`, `outlook.tex`, `editorial_constitution.tex`: Theorem D description updated
- `thqg_introduction_supplement_body.tex`: 5+ instances
- `thqg_preface_supplement.tex`: 5+ instances
- `thqg_symplectic_polarization.tex`: 3+ instances
- `twisted_holography_quantum_gravity.tex`: S-duality theorem reframed
- `free_fields.tex`, `quantum_corrections.tex`, `guide_to_main_results.tex`, `main.tex`: further instances

**Prevention rules**:
1. The complementarity relation is family-dependent. Always specify which family.
2. Check the formula in `landscape_census.tex` before writing any kappa complementarity statement.
3. The correct universal statement is: "kappa is duality-constrained: kappa + kappa' = 0 for KM/free fields; kappa + kappa' = rho*K for W-algebras."

### 1C. Sign errors

**Instances**:
- Spectral zeta: `e^{+pi*y/3}` (growing) should be `e^{-pi*y/3}` (decaying). Commit: `9248c37`.
- Genus-1 Green function: `G_tau(z) = zeta(z) + ...` should have minus sign: `zeta(z) - pi^2*E_2/3 * z`. Propagated across 5 files.
- Curved A-infinity: `m_1^2(a) = [m_0, a]` — the COMMUTATOR sign is essential. Missing minus signs turn cohomological differentials into homological ones.

**Prevention rule**: Sign errors cluster in BV/Koszul sign conventions. For any formula with signs, verify by expanding the simplest nontrivial example (e.g., arity 2 for A-infinity identities).

### 1D. QME factor 1/2

**What happens**: The quantum master equation is written as `{S,S}_BV + hbar*Delta*S = 0`, missing the factor of 1/2.

**Correct**: `(1/2){S,S}_BV + hbar*Delta*S = 0`.

**Git evidence**: 2 instances in Vol II (`67bcd3b`), flagged in mathematical audit.

**Prevention rule**: Always write the QME with the 1/2. Without it, arity expansions produce doubled terms.

### 1E. Off-by-one and indexing errors

**Instances**:
- Pro-Weyl kernel dimension indexed from level 0 instead of level 1. Commit: `21524a5`.
- grt_1 dimension sequence: claimed 1,0,1,0,0,0,1,... **Correct**: 1,0,1,0,1,0,1,0,1,1,... (nonzero at all odd weights; first even-weight at weight 12 from cusp form Delta_12). Commit: `59ff49c`.
- W-algebra dimension table for N=4,5: (2,1^2) at dim 8 (correct: 6), (3,1) at dim 12 (correct: 10). Commit: `e288a86`.

**Prevention rule**: Verify dimension/index formulas against at least two independent sources. For combinatorial sequences, compute the first 5+ terms explicitly.

### 1F. W_3 OPE coefficient — 12+ instances (NEW from dirty state)

**What happens**: The W_3 quartic contact coupling is written as `16/(22+5c)` when the correct value is `32/(22+5c)`. This propagates to all quartic shadow coefficients.

**Dirty working state**: Currently being corrected in 3 files with 12+ instances:
- `w_algebras.tex`: W_3 OPE (2 instances); quartic channel coefficients Q_TTWW 160->320, Q_WWWW 2560->10240; coupling alpha 16/(5c+22)->32/(5c+22); 5 more
- `nonlinear_modular_shadows.tex`: 4 instances
- `deformation_quantization_examples.tex`: Lambda quantum correction coefficient
- Compute modules: shadow_tower_atlas, modular_deformation_package, etc.

**Root cause**: The WW->Lambda OPE coefficient was off by a factor of 2 from the start. Because W_3 formulas are less commonly checked than Virasoro ones, the error persisted longer.

**Prevention rule**: For W_3, the normalization-independent quantity is 32/(22+5c). Check against the Fateev-Lukyanov standard. If you see 16/(22+5c), it is wrong.

### 1G. Elliptic propagator sign — 7 instances across 5 files (NEW from dirty state)

**What happens**: The regularized elliptic Green function has a + sign where - is correct.

**Dirty working state**: `G_tau(z) = zeta_tau(z) + pi^2 E_2(tau)/3 * z` corrected to `G_tau(z) = zeta_tau(z) - pi^2 E_2(tau)/3 * z` in:
- `heisenberg_eisenstein.tex` (3 instances)
- `free_fields.tex` (1 instance)
- `toroidal_elliptic.tex` (2 instances)
- `heisenberg_frame.tex` (1 instance)

**Root cause**: The minus sign comes from the regularization: G = zeta - (pi^2 E_2/3)z ensures quasi-periodicity G(z+1) = G(z), G(z+tau) = G(z) - 2pi*i. The + sign would give the wrong quasi-periodicity.

### 1H. Faber-Pandharipande tautological constants (NEW from dirty state)

**What happens**: The A-hat genus coefficients for genus-g free energy are wrong.

**Dirty working state** in `heisenberg_eisenstein.tex`:
- Old: `lambda_g^FP = |B_{2g}| / (2g * (2g-2)!)` with F_1 = kappa/12, F_2 = kappa/240, F_3 = kappa/6048
- New: `lambda_g^FP = (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!` with F_1 = kappa/24, F_2 = 7*kappa/5760, F_3 = 31*kappa/967680

**Root cause**: The A-hat genus (not Todd genus) governs the Faber-Pandharipande formula. The (2^{2g-1}-1)/2^{2g-1} prefactor was missing.

### 1I. Virasoro shadow recursion: exact -> cubic-source approximation (NEW from dirty state)

**What happens**: The recursion S_{r+1} = -6r/(c(r+1)) * S_r is presented as exact for all r. Actually, for r >= 6, cross-terms from {Sh_j, Sh_k} brackets enter the full recursion.

**Dirty working state** in `thqg_holographic_reconstruction.tex`:
- Entire proposition, corollary, and computation requalified as "cubic-source approximation"
- All S_r for r >= 6 relabeled S_r^{cub} with dagger marks in table
- Caveat added: "For r >= 6, additional contributions from {Sh_j, Sh_k} bracket terms with j,k >= 4 enter"

**Root cause**: The full shadow master equation involves all {Sh_j, Sh_k} brackets with j+k = r+1. The cubic-only recursion only includes {Sh_3, Sh_{r-2}}. Starting at r = 6, the {Sh_4, Sh_4} term enters.

**Prevention rule**: When presenting a recursion, always state which terms are included and which are truncated. If a recursion is a truncation of a larger system, call it an "approximation," not a "recursion."

### 1J. Additional formula corrections from dirty state

- **Jacobi triple product q-power** (`fourier_seed.tex`): `2q^{1/4} sin(pi z)` -> `2q^{1/8} sin(pi z)`
- **Quantum MC hbar power** (`chiral_hochschild_koszul.tex`): `hbar^{2g}` -> `hbar^g` in the MC expansion
- **Virasoro pump coefficient** (`higher_genus_modular_koszul.tex`): R_5 = -6/(5c^2) -> R_5 = -12/(5c^2)
- **Genus loop operator** (`nonlinear_modular_shadows.tex`): Lambda_P now sums over all binom(r,2) pairs (was single pair); fixes delta_H^(1) from 20/[c^2(5c+22)] to 120/[c^2(5c+22)]
- **Affine cubic loop** (`nonlinear_modular_shadows.tex`): Lambda_P(C_aff) was nonzero involving Weyl vector; correct: Lambda_P(C_aff) = 0 (symmetric propagator x antisymmetric structure constants)
- **Tree identity** (`semistrict_modular_higher_spin_w3.tex`): `2v_3 + 3v_4 = n-2` -> `v_3 + 2v_4 = n-2`
- **PTVV shifted-symplectic degree** (`higher_genus_complementarity.tex`): "(n+1)-shifted" -> "n-shifted"
- **W_3 complementarity sum** (`preface.tex`): W_3 Koszul dual `W_3_{50-c}` -> `W_3_{100-c}` (K = 100 for rank-2)
- **W_N central charge sum** (`preface.tex`): `c + c' = 2(N-1)(1 + N(N+1))` -> `c + c' = 2(N-1)(1 + 2N(N+1))`
- **Spectral sequence collapse page** (`higher_genus_complementarity.tex`): "collapses at E_1" -> "collapses at E_2"
- **FM/associahedron** (`configuration_spaces.tex`): "C_n(P^1) isomorphic to Stasheff associahedron K_n" -> correct identification

---

## Error Class 1.5: V_k(g) vs L_k(g) CONFLATION — 12+ instances (NEW from dirty state)

**What happens**: V_k(g) (universal affine vertex algebra) is written where L_k(g) (simple quotient) is meant. This matters because Arakawa's rationality theorem and associated variety results apply to simple quotients, not universal algebras.

**Dirty working state**: 12+ instances across 3 files:
- `chiral_modules.tex`: Arakawa rationality references changed from V_k to L_k (4 instances); orbit duality uses L_k consistently (6+ instances)
- `kac_moody.tex`: admissible level examples use L_k
- `higher_genus_modular_koszul.tex`: "all admissible levels" -> "admissible parameter values on the universal family" with disclaimer about simple quotients

**Prevention rules**:
1. V_k(g) is Koszul for ALL k (prop:pbw-universality). L_k(g) may fail at admissible levels.
2. Associated variety statements (Arakawa) apply to L_k, not V_k.
3. When discussing admissible levels, always specify whether the claim is about V_k or L_k.
4. The PBW criterion applies to the UNIVERSAL algebra; failure for simple quotients comes from vacuum null vectors.

---

## Error Class 2: STATUS INFLATION (19+ instances)

### 2A. ProvedHere on incomplete proofs

**What happens**: A claim is tagged `\ClaimStatusProvedHere` but the proof has gaps, cites conjectural inputs, or proves something weaker than stated.

**Specific instances from commits**:
- D^2=0 simultaneously tagged ProvedHere and Conjectured in different files of the same manuscript.
- Koszulness equivalence count: "all 12 proved" when actually 10 unconditional + 1 conditional + 1 one-directional. Commit: `5753248`.
- WKB metaphor presented as theorem: "the genus expansion is the WKB correction" stated as proved, but no quantised Hamiltonian constructed. Commit: `c0f0e4c`.
- DS shadow commutation presented as "verification" when it is an OPEN CONJECTURE. Commits: `75dcae1`, `0ca622c`.
- prop:polyakov-arity-two-projection tagged ProvedHere but cites external propositions. Commit: `11aad21`.

**Additional instances from dirty working state**:
- **Orbit duality demoted**: prop:orbit-duality changed from Proposition (ProvedHere) to Conjecture across 4 files. The "proof" relied on identifying the associated variety of V_{k'} at the non-admissible dual level, which is not established. 10+ instances across chiral_modules.tex, kac_moody.tex, w_algebras.tex, koszul_pair_structure.tex.
- **Multiple status downgrades**: prop:standard-tower-mc5-reduction (ProvedHere -> Conditional), cor:standard-tower-mc5-closure (ProvedHere -> Conditional), thm:grand-synthesis-principle (ProvedHere -> Conditional), prop:constitution-status-updates (Proposition -> Remark), thm:fourier-four-properties (ProvedHere -> ProvedElsewhere), MC3 for types B_n/C_n ("expected" -> "remains conjectural").
- **Label type corrections**: 5 conjectural items had wrong label prefixes (lem/thm instead of conj): lem:ambient-self-duality, lem:one-sided-isotropy, thm:ambient-complementarity, prop:formal-legendre all corrected to conj: prefix. Derived critical locus ProvedHere -> Conditional.

**Prevention rules**:
1. Before tagging ProvedHere, verify that the proof text actually proves the stated claim at the stated level of generality.
2. Check that all cited results are themselves proved (not conjectural).
3. Distinguish "consistency check" from "proof" in code and prose.
4. Each audit cycle finds 8-12 status boundary violations. Budget for this.

### 2B. Stale conjecture labels after promotion

**What happens**: A conjecture is promoted to a theorem but the `conj:` label prefix is not updated everywhere. Readers see conflicting signals.

**Git evidence**: 5 theorems retained stale `conj:` labels across 7 files. Commit: `21c9cee`.

**Prevention rule**: When promoting conj → thm, grep for ALL occurrences of the old label across both volumes. Update every `\ref{conj:...}` to `\ref{thm:...}`.

---

## Error Class 3: SCOPE INFLATION (8+ instances)

### 3A. Universal claim, special-case proof

**Instances**:
- "Koszulness holds for all..." when proved only for type A.
- "MC3 proved" when proved in type A only. Prior audits found 3+ instances.
- Shadow depth classification G/L/C/M presented as exhaustive (4 classes covering all possibilities). Actually: r_max takes values in {2,3,4,...} union {infinity}; classes F_5, F_6,... are permitted. Commit: `884be20`. Blast radius: **14 files**.
- Saddle-point MC Fredholm identification stated without caveat: precise only for Heisenberg; interacting algebras require HS-sewing hypothesis. Commit: `11aad21`.

**Prevention rules**:
1. Before writing a universal quantifier, verify the proof has no implicit type/genus/level restriction.
2. If a classification is derived from examples, state "for the standard landscape" not "for all chiral algebras."
3. When a claim is proved for a special case, fence it explicitly at every cross-reference site.

### 3B. One-directional implication claimed as equivalence

**Instance**: "Koszulness (ii) iff (iii)" where only (ii) => (iii) was proved. Commit: `8df1fcf`.

**Prevention rule**: Mark the direction of every implication. "A implies B" and "A iff B" are categorically different claims.

---

## Error Class 4: COPY-PASTE PROPAGATION (the amplifier)

### 4A. Formula copied between families without recomputation

This is the ROOT CAUSE of the 47-file kappa disaster. The Sugawara central charge c = k*dim(g)/(k+h^v) was confused with kappa. Once wrong in one file, it was copied to 46 more.

**Prevention rule**: After EVERY formula correction, grep for all variant forms across BOTH `~/chiral-bar-cobar` AND `~/chiral-bar-cobar-vol2`. Fix all instances in the same session. This is AP5 — the #1 systematic failure mode, requiring 3-4 commits per full correction.

### 4B. Tests encoding the same errors

**What happens**: When a formula is wrong in both code AND test expected values, the test passes. This creates a false sense of security.

**Git evidence**: 16 hardcoded `True` assertions in compute tests — tests that always pass regardless of computation. Commit: `ff4c00e`.

**Prevention rules**:
1. Cross-family consistency checks (additivity, complementarity, anti-symmetry) are the real verification.
2. Single-family hardcoded tests are necessary but NOT sufficient.
3. Never write `assert True` as a placeholder — write the actual mathematical assertion.
4. When fixing a formula in code, ALWAYS check whether the test expected values also encode the wrong formula.

### 4C. Placeholder text left behind

LLM-generated text with "[Omitted long context line]" truncation artifacts left in production files. Commit: `11aad21`.

**Prevention rule**: After any bulk edit, grep for placeholder patterns: `[Omitted`, `[TODO`, `[PLACEHOLDER`, `...`, `XXX`.

---

## Error Class 5: OBJECT CONFLATION (10+ instances)

### 5A. The four fundamental objects

These are DISTINCT and must never be conflated:
- **B(A)**: the bar coalgebra
- **Omega(B(A))**: the cobar construction (recovers A itself — Theorem B inversion)
- **D_Ran(B(A))**: the Verdier dual (a factorization ALGEBRA, gives A^!)
- **A^! = H*(B(A))^v**: the Koszul dual algebra

**Git evidence**: 16 files conflated Verdier dual with cobar. Commit: `2273421`. Vol II defined A^! as Omega(B(A)). Commit: `1d8a5f5`.

**Prevention rule**: Never write "the bar-cobar dual" — specify which operation. Cobar recovers A. Verdier produces A^!. These are different functors with different outputs.

### 5B. MC target algebra wrong

The Swiss-cheese twisting morphism alpha_T lives in the two-coloured Swiss-cheese convolution algebra g^{SC}_T, NOT in Hom(B^ch(A), End_A). Commits: `573b417`, `a3c3ec9`.

**Prevention rule**: Always specify the full convolution algebra, not a projection of it.

### 5C. Virasoro self-duality ambiguity — 7+ corrections

Three DISTINCT self-dual points: c=0 (uncurved quadratic), c=13 (FF involution: Vir_c^! = Vir_{26-c}), c=26 (complementarity sum). Commit: `f78bec1`, 6 propagation corrections.

**From dirty working state**: Virasoro complementarity halving formula was applied at c=0 (uncurved point) instead of c=13 (self-dual point). Corrected in `higher_genus_complementarity.tex`: "Vir at c=0 is Koszul self-dual" -> "Vir at c=13 is Koszul self-dual." Note: kappa(Vir_13) = 13/2 != 0, so the self-dual algebra is NOT uncurved.

**Prevention rule**: NEVER write "self-dual" for Virasoro unqualified. Always specify which duality and which central charge.

### 5D. Heisenberg NOT self-dual (NEW from dirty state)

**What happened**: `introduction.tex` described "H_k^! = Sym^ch(V*) = H_{-k} (with the sign flip k -> -k)" — claiming Heisenberg is Koszul self-dual.

**Correction**: "H_k^! = Sym^ch(V*), a curved chiral coalgebra with curvature -k*omega_g... Note: H_k^! != H_{-k} as chiral algebras—the Heisenberg algebra is NOT Koszul self-dual."

**Root cause**: The sign flip k -> -k does NOT make H_{-k} isomorphic to H_k. The Koszul dual is a different categorical object (curved coalgebra).

### 5E. Cobar construction formula (NEW from dirty state)

**What happened**: `cobar_construction.tex` defined Omega(C) = (A tensor_tau C, d_tau). **Correct**: Omega(C) = (Free(s^{-1}bar{C}), d_tau) — the cobar is the FREE algebra on the desuspended augmentation ideal, not a twisted tensor product.

### 5F. Bar-cobar spectral sequence differential swap (NEW from dirty state)

**What happened**: In `bar_cobar_adjunction_inversion.tex`, the E_0 differential was identified as d_internal. **Correct**: E_0 = d_bar = d_internal + d_bar (the full bar complex differential). The E_1 -> E_2 differential was also swapped.

**Root cause**: Spectral sequence page identification is notoriously error-prone. The filtration determines which part of the differential appears at which page.

### 5D. Tor conflation

Tor^A(k,k) (bar cohomology) confused with Tor^{O(M)}(O(L),O(L)) (derived self-intersection). Commit: `786505a`.

### 5E. Conv_str vs Conv_infinity

The dg Lie algebra Conv_str(C,P) is a STRICT MODEL of Conv_infinity(C,P). MC moduli coincide, but the full L_infinity structure is needed for transfer, formality, gauge equivalence.

### 5F. m_0 vs kappa

m_0 = genus-0 curvature (makes m_1^2 != 0). kappa = genus-1 obstruction coefficient. Different genera, different objects.

---

## Error Class 6: LEVEL/GENUS CONFUSION (6+ instances)

### 6A. D^2=0 at which level?

D^2=0 holds at TWO different levels:
- **Convolution level**: from partial^2=0 on M-bar_{g,n}. A THEOREM.
- **Ambient level**: with planted-forest corrections. Also PROVED (via Mok's log FM).

These are structurally different results at different levels of the complex. Conflating them passes review because both are true.

**Prevention rule**: Every use of D^2=0 MUST specify: convolution or ambient.

### 6B. Genus-0 vs genus-1

kappa is a genus-1 obstruction. The genus-0 story (PBW, formality) is different from the genus-1 story (curvature, modular characteristic). Claims like "D^2=0 is proved" or "Theta_A is proved" must specify genus.

### 6C. Chain-level vs cohomological

Sesquilinearity at the chain level (def:sesquilinearity) is different from the PVA definition on cohomology (def:PVA). Citing the wrong one in a proof creates a gap.

---

## Error Class 6.5: FALSE PERIODICITY / WRONG EXAMPLE (NEW from dirty state)

### 6.5A. ChirHoch periodicity claim

**What happened**: `chiral_hochschild_koszul.tex` claimed "ChirHoch^{n+24} = ChirHoch^n" — a periodicity with period M=24. **This is false**: ChirHoch vanishes for n > 2 by Theorem H. The periodicity M=24 lives in the weight-graded bar complex, not in ChirHoch degree.

**Root cause**: Conflating a grading on the bar complex with a grading on ChirHoch. The bar complex has rich structure in high weight; ChirHoch collapses.

### 6.5B. Wrong bar element in Virasoro completion proof

**What happened**: `bar_cobar_adjunction_curved.tex` used L_0 tensor L_0 as the example bar element to demonstrate completion necessity. But [L_0, L_0] = 0, so the example is trivial. Corrected to L_{-2} tensor L_2, which gives d(omega) = [L_{-2}, L_2] = -4L_0 - c/2.

**Root cause**: Picking the simplest-looking element without checking it gives a nontrivial computation.

---

## Error Class 7: CIRCULAR REASONING (6+ instances)

### 7A. Theorem B circularity at genus >= 1

The proof of bar-cobar inversion at g >= 1 appeared to invoke bar-cobar inversion at the genus under consideration. Fixed by explicit inductive separation. Commit: `8d8c8b2`.

### 7B. Euler-Koszul circular classification

12 lines of circular reasoning where the classification used its own output as input. Commit: `f2ed094`.

### 7C. LG Q^2=0 wrong proof

Q^2(phi) claimed to vanish "by direct computation" but the computation is incomplete. The correct argument uses the classical master equation and Jacobi identity. Commit: `1d8a5f5`.

### 7D. Forward references hiding gaps

A claim in the introduction is tagged ProvedHere, but the proof at genus g >= 1 assumes the very thing it claims to prove. Forward references must be transparent about genus/level/type restrictions.

**Prevention rules**:
1. For any inductive proof, verify the induction hypothesis is strictly weaker than the induction step.
2. For any "direct computation" proof, carry the computation to completion — don't stop at "the remaining terms cancel."
3. Forward references across chapters must state the exact level of generality proved.

---

## Error Class 8: STRUCTURAL/LABEL ERRORS (14+ instances)

### 8A. Broken cross-references after renames

File renames and label promotions (conj: -> thm:) break cross-references. Two instances: ~35 broken refs (commit `e8b38dc`, 24 files) and 10+ stale refs (commit `d1d9296`, 10 files).

### 8B. Undefined macros

\gmod, \Sh, \cW used in chapter files but not defined in preamble. Commit: `b79534e`.

### 8C. Label collisions between volumes

11+ labels in nonlinear_modular_shadows.tex and 8 in yangians_drinfeld_kohno.tex clashed between Vol I and Vol II. Commit: `f78bec1`.

### 8D. Phantom bibliography entries

3 citations had placeholder arXiv IDs (2602.12345, 2603.12345, 2412.12345). Commit: `3352966`.

### 8E. Build hygiene

363 undefined refs, 3 multiply-defined labels, 5 undefined citations cleaned in foundational audit. Commit: from 2026-03-22 foundational audit.

**Prevention rules**:
1. After any rename: grep for ALL old names/labels across both volumes.
2. After any commit: `make fast` must complete with 0 errors.
3. New macros go in main.tex preamble, never in chapter files.

---

## Error Class 9: EDITORIAL/FRAMING ERRORS (8+ instances)

### 9A. Physics analogy inflated to mathematical claim

"The genus expansion is the WKB correction" — no Hamiltonian constructed, no operator ordering, no Schrodinger equation. Commit: `c0f0e4c`.

### 9B. LLM vocabulary in monograph prose

"Adversarial assessment" in concordance section title. "This is the fundamental link..." — the mathematics should speak for itself. Commits: `59ff49c`, `85c08d2`.

### 9C. "Dyson-Schwinger equation" misnomer

The Kadeishvili-Merkulov tree-level transfer recursion is NOT the Dyson-Schwinger equation. Commit: `786505a`.

**Prevention rules**:
1. Physics analogies must be explicitly labeled as analogies, not stated as theorems.
2. Grep for LLM-characteristic phrases: "fundamental", "key insight", "crucially", "the selection principle".
3. Attribution: use the correct mathematical name, not the physics name, for algebraic constructions.

---

## Error Class 10: SINGLE-POINT EXTERNAL DEPENDENCY (1 critical)

thm:ambient-d-squared-zero depends entirely on [Mok25, Thm 3.3.1], a 2025 preprint. If retracted, 37+ downstream citations fall.

**Prevention rule**: Any theorem resting on a single external source gets flagged in concordance.tex with source, publication status, and fallback strategy.

---

## Statistical Summary

| Error Class | Committed | Dirty State | Key Blast Radius |
|---|---|---|---|
| Formula errors (kappa families) | 18 | 10+ new | 47 files (kappa alone) |
| Kappa anti-symmetry overclaim | 20+ | 25+ instances | 15+ files |
| W_3 OPE coefficient (16->32) | — | 12+ instances | 3 files + compute |
| Elliptic propagator sign | — | 7 instances | 5 files |
| V_k vs L_k conflation | — | 12+ instances | 3 files |
| Status inflation/downgrades | 7 | 8+ downgrades | 10+ files |
| Orbit duality Proved->Conjectured | — | 10 instances | 4 files |
| Scope inflation | 4 | shadow recursion | 14 files |
| Copy-paste propagation | 3 | same amplifier | 47+ files (compound) |
| Object conflation | 5 | 3 new (Heis, cobar, SS) | 16 files (Verdier/cobar) |
| Level/genus confusion | 3 | — | systemic |
| Circular reasoning | 3 | — | 5 files |
| Structural/label errors | 8 | — | 24 files (post-rename) |
| Editorial/framing | 5 | — | 10+ files |
| False periodicity/wrong example | — | 2 | 2 files |
| Single-point dependency | 1 | — | 37 downstream |
| Stale status tags | 2 | 5 label-type | systemic |
| **TOTAL** | **79+** | **90+** | **~60 dirty files** |

**Combined total**: 215+ distinct error instances catalogued across committed history and dirty working state.

## The Seven Deadliest Patterns

1. **Kappa formula confusion** — 7-8 commits + 10 new dirty instances, 47+ files. The same error keeps being rediscovered in new locations. Root cause: Sugawara c confused with modular characteristic kappa.
2. **Kappa anti-symmetry overclaim** — 25+ instances across 15+ files currently being corrected. "kappa + kappa' = 0 for all" is false; it is family-dependent. This is the error with the largest CURRENT blast radius.
3. **Corrections require 3-4 commits each** — a formula fix in one file is followed by 1-3 propagation commits finding the same error elsewhere (AP5). The W_3 coefficient correction hit 12+ instances in 3 files + compute.
4. **Tests encode the errors** — when code AND test expected values are both wrong, tests pass (AP10).
5. **Object conflation is the deepest** — Verdier/cobar (16 files), V_k/L_k (12+ instances), Heisenberg self-duality (introduction), cobar definition (cobar_construction).
6. **Status inflation follows a predictable pattern** — claims start as conjectures, get partially proved, the partial proof is tagged ProvedHere, and the caveats are lost. The orbit duality demotion (10 instances) is the latest case.
7. **Truncated recursions presented as exact** — the shadow recursion was cubic-source-only but presented as the full answer. Prevention: always state which terms are included.

## The Golden Rules (distilled from 215+ errors)

1. **Never copy a formula between families without recomputing from first principles.** (AP1 — 47+ file kappa disaster, 12+ W_3 instances)
2. **After every correction, grep both volumes for all variant forms.** (AP5 — corrections need 3-4 commits each)
3. **ProvedHere is a LaTeX macro, not a proof.** Verify the proof text. (AP4 — orbit duality, 8+ status downgrades)
4. **Specify the level**: convolution vs ambient, genus-0 vs genus-1, strict vs homotopy. (AP6)
5. **Cross-family consistency checks are the real tests**, not hardcoded expected values. (AP10)
6. **The four fundamental objects (B, Omega B, D_Ran B, A^!) are distinct.** Name which one. (16 files)
7. **V_k(g) != L_k(g).** Universal affine VA vs simple quotient. (12+ dirty instances)
8. **A truncated recursion is an approximation, not a formula.** State which terms are included. (shadow recursion)
9. **A physics analogy is not a theorem.** Label it accordingly.
10. **Universal claims need universal proofs.** If proved in type A, say "type A." (AP7)
11. **kappa + kappa' = 0 is NOT universal.** It is family-dependent. (25+ dirty instances)
12. **After any rename, grep everything.** The blast radius is always larger than you think.
13. **Your correction might also be wrong.** Mark uncertain corrections with RECTIFICATION-FLAG.

---

## Error Class 11: BETAGAMMA/BC SIGN CONFUSION — 18 instances (NEW: 2026-03-24 audit)

**What happens**: c(betagamma) = +2(6lambda^2 - 6lambda + 1) is confused with c(bc) = -2(6lambda^2 - 6lambda + 1). At lambda=1: c(bg) = +2 and kappa(bg) = +1, but 18 locations had c = -2 and kappa = -1 (the bc values).

**Root cause**: The betagamma and bc systems are Koszul dual. Their central charges differ by sign. Because bc ghosts (c=-26 at lambda=2) appear more often in physical formulas (string theory ghost system), the negative-sign convention was unconsciously applied to betagamma.

**Blast radius**: 5 tex files + 14 compute lib files + 12 test files. Tests PASSED because they asserted the wrong expected values (Error Class 4B amplifier).

**Prevention rules**:
1. betagamma has c > 0 at lambda = 0,1. bc has c < 0. If your "betagamma" c is negative, you have the bc system.
2. The Koszul dual pair is: kappa(bg) + kappa(bc) = 0. If both are negative, something is wrong.
3. After fixing a kappa sign in code, ALWAYS check the corresponding test assertions.

## Error Class 12: F_1 = c/24 vs c/48 CONFUSION — 3 instances (NEW: 2026-03-24 audit)

**What happens**: F_1 = kappa/24 (the shadow free energy). For Virasoro, kappa = c/2, so F_1 = c/48. But 3 locations wrote c/24.

**Root cause**: The PHYSICAL conformal anomaly coefficient is c/24 (in the partition function Z = q^{-c/24}/eta). The SHADOW free energy is kappa/24 = c/48. For the Heisenberg, kappa = c, so the two coincide; for all other families they differ. The error comes from incorrectly generalizing the Heisenberg identity F_1 = c/24 to Virasoro.

**Specific diagnostic**: If (c/2)*(1/12) appears, the 1/12 should be 1/24 (the Faber-Pandharipande evaluation of lambda_1). The factor 1/12 comes from confusing lambda_1 with kappa_1/12 (Mumford's relation), but int(lambda_1) = 1/24, not 1/12.

**Prevention rule**: For Virasoro, F_1 = c/48. For Heisenberg, F_1 = c/24. For W_N, F_1 = c*(H_N-1)/24. ALWAYS use F_1 = kappa/24 as the universal formula, never F_1 = c/24.

## Error Class 13: STATE-FIELD MAP FACTOR — 1 instance (NEW: 2026-03-24 audit)

**What happens**: The quasi-primary composite Lambda = :TT: - (3/10) d^2 T has coefficient 3/10 in FIELD language. In STATE language: |Lambda> = L_{-2}^2|0> - (3/5) L_{-4}|0>, because d^2 T corresponds to 2*L_{-4}|0> under the state-field map. The proof at NMS:1266 used the field coefficient (3/10) in the state formula, producing wrong intermediate steps.

**Root cause**: The state-field correspondence Y(L_{-n}|0>, z) = (1/(n-2)!) partial^{n-2} T(z) introduces factorial factors. For L_{-4}|0>: Y gives (1/2!) partial^2 T = (1/2) partial^2 T. So partial^2 T = 2*Y(L_{-4}|0>).

**Prevention rule**: When translating between field and state language, always apply the state-field map explicitly. The coefficient in the field formula differs from the coefficient in the state formula by the appropriate factorial.

## Error Class 14: TWO DIFFERENT LISTS WITH THE SAME NUMBER — the Koszulness 12 (NEW: 2026-03-24 audit)

**What happens**: Two different lists of 12 Koszulness characterizations exist:
- Meta-theorem (i)-(xii): items (xi) = Lagrangian (conditional), (xii) = D-mod purity (one-directional)
- Preface K1-K12: K12 = bifunctor decomposition (proved), D-mod purity is "13th"

6+ files said "all 12 proved" using one list's numbering while the other list's item (xi) is conditional.

**Root cause**: Two different authors (or two different sessions) created two different enumerations of "the 12 characterizations" with different items in positions 11 and 12.

**Prevention rule**: Always cite the specific theorem number (thm:koszul-equivalences-meta) and item number ((i)-(xii)), not "the 12 conditions." When discussing the count, specify: "10 unconditional in the meta-theorem + tropical Koszulness proved separately = 11 unconditional total; Lagrangian criterion conditional; D-module purity one-directional."

---

## Updated Statistical Summary (2026-03-24)

| Error Class | Total Known | Fixed This Session |
|---|---|---|
| 1A. Kappa formula confusion | 28+ | 0 (prior) |
| 1B. Kappa anti-symmetry overclaim | 37+ | 12 new |
| 1F. W_3 OPE coefficient | 12+ | 0 (prior) |
| 1I. Shadow recursion cubic-source | 18 | 18 (both volumes) |
| 11. betagamma/bc sign | 18 | 18 (all) |
| 12. F_1 c/24 vs c/48 | 3 | 3 (all) |
| 13. State-field map factor | 1 | 1 |
| 14. Two Koszulness lists | 6+ | 6 |
| Status inflation (various) | 25+ | 21 W-infty + 5 Koszulness |
| Structural/label | 30+ | 10+ phantom/ref fixes |
| **TOTAL THIS SESSION** | **~95** | **~95 fixes applied** |

**Combined all-time total**: 310+ distinct error instances catalogued.

---

## Addendum: Deep Beilinson Audit (2026-03-24) — New Patterns

24 parallel audit agents read every argument in Vol I (~180K lines), 7 agents read Vol II (~53K lines). 65+ fixes applied across both volumes. Agent false positive rate: ~25-30%.

### NEW PATTERN: κ vs κ_eff Conflation (Vol II, 5+ instances)

**Error form**: Writing κ(Vir_26) = 0 when the intrinsic κ = c/2 = 13. The EFFECTIVE κ_eff = (c-26)/2 = 0 (after ghost subtraction). Multiple files drop the "eff" subscript, creating the false claim that the modular characteristic itself vanishes at c=26.

**Locations**: anomaly_completed_core.tex, thqg_anomaly_extensions.tex, ht_bulk_boundary_line_frontier.tex, thqg_spectral_braiding_extensions.tex.

**Prevention**: Always distinguish κ (intrinsic) from κ_eff (after ghost subtraction). At c=26: κ=13, κ_eff=0.

### NEW PATTERN: Class M "Not Koszul" Conflation (Vol II, 3 instances)

**Error form**: Claiming Virasoro/W_N is "not chirally Koszul" because it has infinite shadow depth. WRONG: shadow depth does NOT characterize Koszulness. Both finite and infinite shadow depth algebras are Koszul. Shadow depth classifies COMPLEXITY (G/L/C/M), not Koszulness.

**Locations**: Vol II rosetta_stone.tex (×2), examples-worked.tex (×1). The rosetta_stone.tex had an internal self-contradiction: theorem statement said "all four classes are Koszul" but proof said "class M is not."

**Prevention**: Koszulness = PBW concentration. Non-formality (m_k ≠ 0 for k ≥ 3) ≠ non-Koszulness.

### NEW PATTERN: Convention Contradictions from Duplicate Sections (Vol I, 1 instance)

**Error form**: nonlinear_modular_shadows.tex had ~435 lines of "restated" material using a different convention (binom(r,2) all-pairs vs single-pair genus loop), creating contradictory values for the affine cubic loop (0 vs nonzero), Virasoro cubic loop (4x/c vs 12x/c), and Hessian correction (20 vs 120).

**Root cause**: Two-phase development without convention reconciliation. The restated sections used the geometrically correct binom(r,2) convention but incorrectly computed the affine cubic loop.

### NEW PATTERN: Virasoro Bracket Sign Error (Vol I, 1 instance)

**Error form**: [L_{-2}, L_2] = -4L_0 + c/2 (sign error in central term). Correct: -4L_0 - c/2.

**Derivation**: c/12 · m(m²-1) with m=-2 gives c/12·(-2)(3) = -c/2.

### NEW PATTERN: R-Matrix Inverse Formula (Vol I, 1 instance)

**Error form**: R(u)^{-1} = 1 + P/(u-1) for R(u) = 1-P/u. WRONG on antisymmetric subspace.

**Correct**: R^{-1} = u(u+P)/(u²-1), or equivalently: eigenvalue (u-1)/u on symmetric, u/(u+1) on antisymmetric.

### NEW PATTERN: FM-Associahedron Dimension Error (Vol I, 1 instance)

**Error form**: C̄_n(P¹) ≅ K_n as stratified space. Dimensionally impossible: C̄_n(P¹) has complex dimension n, K_n has dimension n-2.

**Correct**: The real FM moduli M̄_{0,n+1}(R) has face poset isomorphic to K_{n-1}.

### NEW PATTERN: Proof Sketches Tagged ProvedHere (Vol II, 3 instances)

**Error form**: log_ht_monodromy_core.tex has three theorems (BPHZ existence, analytic flatness, family version) tagged ProvedHere but with only "Proof sketch" arguments.

### Vol II Structural Crisis (RESOLVED)

1018 duplicate labels from 42 superseded files → 0 after label stripping. 36 internal undefined refs → 0 after 6 label renames + 7 relocations. 27 undefined citations → 0 after 17 bibliography additions.

### Updated Totals

| Pattern | Vol I instances | Vol II instances |
|---------|----------------|-----------------|
| κ formula (AP1) | 10+ fixed | 4 fixed (κ_eff conflation) |
| WW OPE 16→32 | 8 fixed | 8 fixed |
| Class M Koszulness | 0 | 3 fixed |
| F₁ = c/24→c/48 | 2 fixed | 1 fixed |
| K_{sl_N} factor | 1 fixed | 0 |
| R₅ factor | 1 fixed | 0 |
| Virasoro self-duality | 2 fixed | 0 (clean) |
| Ω(B(A))=A^! conflation | 1 fixed | 0 (clean) |
| Status inflation | 10+ fixed | 4 flagged |
| Structural/label | 5+ fixed | 1018→0 duplicates |
| **TOTAL** | **45+** | **20+** |

**Combined all-time total**: 375+ distinct error instances catalogued.

---

## Error Class 15: CROSS-VOLUME — CATEGORICAL CONFLATION FROM VOL II (2026-03-24)

The following error patterns were discovered in Vol II and have cross-volume relevance. See Vol II `common_agent_errors.md`, Error Classes 10-11, for full details.

### 15A. Operations vs co-operations (cross-volume principle)

**The error**: Claiming an operad-algebra structure determines a bialgebra structure. Operads give operations (many inputs → one output). A Yangian coproduct (one input → many outputs) is a co-operation that CANNOT come from any operad. The coproduct on A^! comes from the module tensor product on C_line ≃ A^!-mod, not from the SC^{ch,top}-algebra structure.

**Vol I relevance**: Vol I's Theorem A (bar-cobar adjunction) produces a COALGEBRA B(A), and the Koszul dual A^! gets an ALGEBRA structure. The bialgebra structure on A^! (if it exists) requires additional input beyond the bar-cobar adjunction. Any passage in Vol I that conflates "Koszul dual is an algebra" with "Koszul dual is a bialgebra" is wrong.

### 15B. Bar-cobar inversion ≠ Koszul involution

**The error**: Using Ω(B(X)) ≃ X (bar-cobar inversion, LV 10.1.13) to prove (X^!)^! ≃ X (Koszul involution, LV 7.4.5). These are different theorems. The involution requires X^! to also be Koszul.

### 15C. Correction propagation in a multi-volume work

**The error**: Correcting a theorem in one file but leaving dozens of references to the old version in other files. In a 2700-page two-volume work, the blast radius of a conceptual correction is enormous. After ANY correction: grep BOTH volumes for the old language.

### Golden Rules Addendum (from Vol II thread)

23. **Operads give operations (many→one). Co-operations (one→many) are NOT operadic.**
24. **An element of Y⊗Y is NOT a bilinear map Y⊗Y → Y.** Check types.
25. **Bar-cobar inversion ≠ Koszul involution.** Different theorems, different hypotheses.
26. **Verify algebraic identities in the simplest example first.**
27. **When citing a proposition, verify it exists in the cited paper.**
28. **After correcting a theorem, grep EVERYTHING for the old language.**
29. **When claiming X = Y, check both directions separately.**
30. **When dualizing, check finiteness.** Koszulness or concentration is needed.
