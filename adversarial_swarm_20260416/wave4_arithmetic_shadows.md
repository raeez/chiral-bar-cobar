# Wave 4 Adversarial Audit — Arithmetic Shadows, Shadow Formality, and the Modular/Arithmetic Pillar of Vol I

**Author:** adversarial referee
**Date:** 2026-04-16
**Scope:** standalone/arithmetic_shadows.tex (1,221 ll), chapters/connections/arithmetic_shadows.tex (13,027 ll), standalone/N6_shadow_formality.tex (705 ll), standalone/seven_faces.tex (939 ll), standalone/genus1_seven_faces.tex (974 ll), chapters/connections/genus1_seven_faces.tex (1,203 ll).
**Mandate:** find every wrong, overclaimed, or insufficiently proved arithmetic / modular / formality statement and force the strongest correct version into view. Strengthen, do not downgrade, unless absolutely no upgrade path exists.

---

## Section 1 — Triage of arithmetic / modular / formality / seven-faces claims

| Claim | Location | Verdict | One-line summary |
|---|---|---|---|
| **Shadow Eisenstein theorem (D₂ = −24κ·ζ(s)ζ(s−1))** | standalone/arithmetic_shadows.tex L348–L383; chapter L3412–L3456 | **SAFE (strong, non-trivial)** | The proof is the classical Ramanujan divisor identity σ₁ = id ∗ 𝟏. Modular structure clean. The chapter version explicitly disclaims the *false* identification with the shadow L-function (good). |
| **Sewing–Selberg formula (Rankin–Selberg)** | chapter L386–L408; standalone L1077–L1095 | **SAFE WITH SCOPE FLAG** | Identity correct; but written as if for "every" κ-bearing algebra without naming the regularization scheme for the divergent integral over 𝓜₁,₁ (the *constant term* a₀(y) is what is integrated; this should be stated). |
| **Narain universality (rank-1 Epstein)** | standalone L443–L470 | **SAFE** | T-duality manifest; (i)–(iii) tight. |
| **E₈ Epstein factorization (240·2⁻ˢ·ζ(s)·ζ(s−3))** | standalone L474–L495 | **SAFE** | Theta of E₈ = E₄, σ₃ identity, clean. |
| **Leech: Θ_Leech = E₁₂ − (65520/691)·Δ₁₂** | standalone L522–L546 | **SAFE** | Standard, with cusp form Δ₁₂ properly named. |
| **Shadow L-function L^sh(s) = Σ S_r r⁻ˢ analytic properties** | standalone L639–L663 | **NEEDS-TIGHTENING** | (ii) "poles at s=1 and s=2 arising from S₂=κ and S₃" is a category error: a Dirichlet series Σ a_r r⁻ˢ with isolated coefficients (not multiplicative, no functional equation) cannot have arithmetic poles at integer s without a special structural mechanism; for class G it is finite (no poles at all). The "trivial zeros at negative integers" claim (iii) is *vacuous*: Σ a_r r⁻ˢ does not analytically continue to negative integers without a regularization that the text does not provide. The Ramanujan-bound violation note is correct. |
| **κ_BKM = c_N(0)/2** parallels via shadow Eisenstein | does not occur in Vol I; Vol III only | n/a | — |
| **Seven-faces master theorem** | standalone/seven_faces.tex L285–L345 | **WRONG without deduplication** | Seven presentations inflate four genuine objects: see Section 4. The chain F1↔F4↔F7 collapses to one object via Drinfeld–Sklyanin. |
| **Trichotomy k_max ∈ {0,1,≥3}** | standalone/seven_faces.tex L581–L638 | **NEEDS-TIGHTENING** | The "absence of k_max=2" proof (Prop 4.4, L624–L638) over-ranges: it asserts p_max ∈ {1,2}∪{4,5,…} for *all* bosonic chiral algebras in the standard landscape, but supersymmetric or mixed-parity examples (b–c systems with mixed weight) can have p_max=3. The proof should restrict to the bosonic, half-integer-excluded landscape explicitly. |
| **β γ exceptional class C** | seven_faces.tex L640–L678 | **SAFE** | The witness is correctly identified; the stratum-separation explanation is honest. |
| **Genus-1 elliptic regularization theorem** | genus1_seven_faces.tex L261–L310 | **SAFE WITH OPE COEFFICIENT FLAG** | Replacement 1/zⁿ⁺¹ → (−1)ⁿ⁻¹·℘⁽ⁿ⁻¹⁾(z)/n! is correct (matches Laurent at z=0 to leading order). The OPE-mode coefficients c_n = a_(n)b are stated but the Wick-product correction (normal ordering shifts) is not addressed for composite generators (relevant for ℳ_class). |
| **KZB identification (Theorem 3.1)** | genus1_seven_faces.tex L344–L406 | **SAFE** | OPE c₀ = Ω/(k+h^v) gives r^(1) = Ω·ζ_τ(z)/(k+h^v); part (ii) uses ℘ = −ζ_τ′ correctly. The level prefix is present (AP126 satisfied). |
| **Belavin–Drinfeld elliptic r-matrix identification** | genus1_seven_faces.tex L428–L491 | **NEEDS-TIGHTENING** | Theorem L428 claims the elliptic r-matrix for arbitrary simple 𝔤; proof L469–L491 only covers 𝔰𝔩₂ explicitly (Cartan + two roots). For higher rank (Remark L493–L501) the existence is asserted by "uniqueness of Belavin–Drinfeld" but the proof provides no construction beyond rank 1. Strengthen: state explicitly "for 𝔤 = 𝔰𝔩₂; higher rank conjectural pending matching of root-channel theta ratios." |
| **Class M elliptic operators "genuinely new"** | genus1_seven_faces.tex L646–L685 | **WRONG without literature check** | The remark "no counterpart in the existing integrable systems literature" L674–L685 is an overclaim. Etingof–Kirillov elliptic Macdonald operators and the Etingof–Latour–Rains higher-genus elliptic Calogero–Moser systems involve precisely the higher-derivative ℘^(m) operators. Strengthen by *citing* Etingof–Kirillov and stating the precise novelty (e.g., the appearance from the bar-cobar Maurer–Cartan rather than Hamiltonian reduction). |
| **B-cycle monodromy = quantum group parameter** | genus1_seven_faces.tex L811–L853 | **SAFE WITH AP156 RISK** | The identification q = exp(2πi/(k+h^v)) is correct; the appeal to ζ_τ quasi-periodicity is the right mechanism. Verify that ζ_τ here is the Weierstrass zeta, not θ₁′/θ₁ (AP156). At L207 the standalone uses Weierstrass zeta — consistent. |
| **Critical level jump theorem** | genus1_seven_faces.tex L867–L913 | **SAFE WITH SPECIFIC NUMBER FLAG** | Item (ii) claims dim H¹ jumps from 4 to 8 for 𝔰𝔩₂ at critical level; this number should be cited or derived (not asserted). The Feigin–Frenkel center identification is standard. |
| **Shadow ↔ formality identification (N6 main theorem)** | N6_shadow_formality.tex L157–L169, L434–L502 | **NEEDS-TIGHTENING (chain vs cohomology)** | The theorem identifies shadow tower with the Linf-formality obstruction tower of 𝔤^{mod,(0)}. The induction proof (L449–L502) is at the *cohomology* level (Step 2 chooses a deformation retract; both sides are computed in cohomology). For class M (Virasoro) the "intrinsically non-formal" assertion (Cor 5.3, L568–L572) is correct at *cohomology* but the chain-level statement requires an additional argument: the chain-level differential could in principle be formalisable while the *transferred* brackets fail. The proof does not distinguish. |
| **κ formula list (Heis k, KM dim(g)(k+h^v)/(2h^v), Vir c/2, W_N c·(H_N−1))** | standalone/arithmetic_shadows.tex L246–L262 | **SAFE** | All four formulas correct; AP136 (H_{N−1} vs H_N − 1) correctly handled — the formula uses (H_N − 1), not H_{N−1}. |
| **ε^c_s rank-1 recovery (Theorem 3.2)** | standalone L499–L531 | **SAFE WITH NORMALIZATION FLAG** | Two normalizations stated (Q(m)=m² vs Q(m)=2m²); the choice is documented. The "alternate convention with ε^1_s(R=1) = 4ζ(2s)" needs an explicit citation to which engine uses which. |
| **Hecke decomposition at higher rank (Prop 3.4)** | standalone L554–L567 | **WEAK as theorem; should be PROPOSITION-with-conditions** | The decomposition Σ_j c_j L(s, χ_j) is asserted with "c_j ∈ ℚ are algebraic coefficients determined by the lattice geometry" — no proof, no construction, no examples beyond E₈/Leech. This is a *programme*, not a proposition. Strengthen by either restricting to lattices with class number 1 (where the proof goes through) or downgrading to remark/conjecture. |
| **Verlinde polynomial family Theorem 5.2 (i)** | standalone L786–L830 | **SAFE FOR g≤6, NEEDS SCOPE for g>6** | Explicit formulas P₂…P₆ verified by polynomial interpolation; the universal factor n^(g-1)(n²-1)·R_{g-2}(n²) is asserted "for g ≥ 2" without proof for g > 6. The cosecant power-sum argument (proof L832–L847) does establish this universally, so the scope is fine — but the wording "Verified by direct S-matrix summation" should be cited to a specific computation. |
| **Verlinde leading asymptotic ζ(2g−2)/(2^{g−2}π^{2g−2})** | standalone L815–L820 | **SAFE** | This is the classical Euler asymptotic for cosecant power sums. Identification with zeta values clean. |
| **Bocherer bridge conjecture** | standalone L934–L962 | **SAFE AS CONJECTURE** | Properly tagged conjecture; cites Furusawa–Morimoto. |
| **Two-variable L-object L(s,u) sewing-Hecke reciprocity** | standalone L1077–L1095 | **NEEDS-TIGHTENING** | Equation L1086–L1091 claims L(s,u) = Γ(v)/(2π)^v · S(v) with v = s+u-1; this is asserted without proof. The "scattering poles of E* at s = ρ/2 are not poles of L_𝒜" is asserted as a structural observation; needs a reference or proof. |
| **p-adic convergence radius proposition** | chapter L2623–L2647 | **SAFE WITH AP-CY19 SATISFIED** | The Â-genus generating function is correctly written (x/2)/sinh(x/2); AP-CY19 (don't drop the /2) is observed. The von Staudt–Clausen estimate is correctly applied. |
| **Kummer congruences ↔ Kubota–Leopoldt** | chapter L2649–L2671 | **NEEDS-TIGHTENING (specific/general)** | Statement (L2660–L2667) asserts "the shadow tower inherits this structure": valid for Heisenberg and the leading-order Virasoro geometric series, but extending the analogy to all class M is an inductive leap not supported. |
| **Ferrero–Washington failure remark** | chapter L2695–L2738 | **WEAK: ClaimStatusProvedHere?** | This is a lengthy remark with five sub-claims (μ-invariant nonvanishing, Mazur inequality at p≤37, arithmetic vs algebraic depth independence, Nahm eigenvalue, conductor non-symmetric) that *together* would be substantial original arithmetic. None has a proof in the file. Each should be restricted to a verifiable scope or downgraded. The remark environment shields it from the audit, but the claims are asserted as facts. |
| **Hilbert reciprocity for shadow field** | chapter L2673–L2693 | **SAFE AS CHECK, WEAK as STATEMENT** | The Hilbert reciprocity Π_p (κ,Δ)_p = 1 is automatic for any field and any pair (κ, Δ); claiming it "holds for all standard families" is vacuously true (it holds for any choice of (κ, Δ) ∈ ℚ× × ℚ×). The result is the *sign-change correspondence*, not the reciprocity itself. |
| **Shadow s=1 quantum modularity volume conjecture** | chapter L3724–L3749 | **SAFE AS CONJECTURE** | Properly tagged. Falsification criteria are explicit and testable. |
| **Shadow–MZV dictionary** | chapter L2754–L2779 | **NEEDS-TIGHTENING** | Items (i) and (ii) (κ controls ζ(2) coefficient of 4-point amplitude; S₃ controls ζ(3) coefficient) need explicit normalization. The genus-0 4-point amplitude depends on which channel (s/t/u) is chosen; the symmetric average eliminates the parity issue but only via a calculation not in the file. |
| **Shadow Higgs field theorem** | chapter L3922 onward | (out of wave-4 scope; mentioned for context) | The "nonabelian Hodge correspondence" framing (flat/Higgs/harmonic) for the shadow tower is a *structural analogy*, not a theorem. Should be downgraded to construction/programme. |
| **Categorical zeta of 𝔰𝔩₂ = ζ(s) − 1** | chapter L3843–L3888 | **SAFE** | Correct calculation; explicitly notes the rank-1 accident (no multiplicativity for N≥3). |

---

## Section 2 — Per-claim attack/defense/repair (with line numbers)

### 2.1 Shadow Eisenstein theorem (D₂(s) = −24κ ζ(s) ζ(s−1))

**Locations:** standalone/arithmetic_shadows.tex L348–L383; chapter/arithmetic_shadows.tex L3412–L3456.

**Attack:** the result *looks* like a theorem about chiral algebras, but it is a triviality dressed up: D₂ is *defined* (L353) as Σ σ₁(n) n⁻ˢ, which is an arithmetic Dirichlet series independent of 𝒜. The factorization D₂ = ζ(s)ζ(s−1) is the classical Ramanujan identity (proved via Dirichlet convolution σ₁ = id ∗ 𝟏). The chiral algebra contributes only the prefactor −24κ, *which appears in the definition itself* (L382: "the Fourier coefficient of −24κσ₁(n) at q^n"). The identity proves nothing about chiral algebras that wasn't already in the definition.

**Defense:** the *content* is the chain
  (i) shadow amplitude Sh₂^(1) = κ·E₂* (proved upstream via bar-complex computation),
  (ii) Fourier coefficients of E₂* are −24σ₁(n) (classical),
  (iii) σ₁ Dirichlet series factors as ζ(s)ζ(s−1) (Ramanujan).
The non-trivial step is (i); the Eisenstein identification is a *consequence* of (i), not new content. The chapter version (L3458–L3495) explicitly disclaims the *false* identification of D₂ with the shadow L-function L^sh(s) = Σ S_r r⁻ˢ — this disclaimer is *important* and shows awareness of the failure mode.

**Strongest correct version:** "Theorem (Shadow–Eisenstein dictionary)." For every chirally Koszul 𝒜 with κ = κ(𝒜), the genus-1 degree-2 shadow amplitude is Sh₂^(1)(τ) = κ·E₂*(τ), and its Fourier-coefficient Dirichlet series is the Eisenstein L-function D₂(𝒜, s) = −24κ·ζ(s)ζ(s−1). The single algebraic input is κ; the rest is classical analytic number theory.

**Repair:** add an explicit "Content versus consequence" note immediately after the proof. The content is Sh₂^(1) = κ·E₂* (proved via bar-complex Bergman kernel); the Eisenstein factorization is its immediate arithmetic consequence.

---

### 2.2 Shadow L-function L^sh(s) = Σ S_r r⁻ˢ poles and trivial zeros

**Location:** standalone/arithmetic_shadows.tex L639–L663 (Prop. 4.3).

**Attack:** Item (ii) "Poles at s=1 and s=2 arising from S₂=κ and S₃" is *categorically wrong*. A Dirichlet series with isolated, non-multiplicative coefficients does not have arithmetic poles at integer s. For class G (Heisenberg), L^sh(s) = k·2⁻ˢ has no poles anywhere; for class L (KM), L^sh(s) = κ·2⁻ˢ + S₃·3⁻ˢ has no poles. The author conflates the *Eisenstein* poles of D₂(s) (Theorem 2.1, which does have such poles via ζ(s)ζ(s−1)) with the *shadow* L-function L^sh, which is a *different object* (the chapter remark L3458–L3495 says exactly this).

Item (iii) "Trivial zeros at negative integers s = −n arising from polynomial vanishing" is similarly mistaken: a Dirichlet series Σ S_r r⁻ˢ with finitely many or growing-rationally-many terms does not analytically continue to negative integers without a regularization (e.g., zeta regularization), and even then, "trivial zeros" require ζ-like functional equation symmetry.

**Defense:** there may be a generating-function reading (Σ r^n S_r evaluated at finite truncations) where polynomial vanishing happens at exceptional c. But this is *not* the meaning of L^sh(−n) for a Dirichlet series.

**Strongest correct version:** "Proposition (Convergence of L^sh)." For class M algebras with shadow coefficients S_r = O(r^α) (some α), L^sh(s) converges absolutely for Re(s) > α + 1. For class G (S_r = 0 for r≥3), L^sh(s) = κ·2⁻ˢ is entire. For class L (S_r = 0 for r≥4), L^sh is entire of two terms. For class C (one extra term), entire of three terms. *No poles for classes G, L, C.* For class M, the analytic continuation question requires substantive arithmetic input that is not provided.

**Repair:** delete (ii) and (iii); replace with a convergence-only statement. Reserve "Eisenstein poles" for D₂.

---

### 2.3 Seven-faces master theorem

**Location:** standalone/seven_faces.tex L285–L345 (Theorem 3.1).

**Attack (deduplication):** of the seven presentations, only **four** are genuinely distinct objects:

  - **Object A** (E_1 algebraic): the universal twisting morphism / r(z) ∈ 𝒜^! ⊗ 𝒜^![[z⁻¹]]. This is F1.
  - **Object B** (semiclassical shadow): the classical r-matrix / Sklyanin tensor / Gaudin generator. F3, F5, F6, F7 are the *same* element under different names. The differential between them is purely *normalization*: F5 is F6 by Drinfeld–STS (1985-1983); F7 is F4 (sphere Hamiltonians) when the spectral parameter is a worldsheet position rather than a Hopf-algebra parameter; F3 (PVA r-matrix) is the classical limit of F5 (Yangian r-matrix). All four are projections of Object A under av: E_1 → E_∞.
  - **Object C** (gauge-theoretic): the line operator R-matrix in DNP. This is F2. It equals Object A by the Vol II identification thm:dnp-bar-cobar-identification.
  - **Object D** (holographic): the Gaiotto–Zeng commuting differentials. This is F4. It equals the *image of* Object A under the sphere Hamiltonian map; the equivalence with Object B is part of GZ26.

The presentation chain F1 ⇔ F2 ⇔ F3 ⇔ F4 ⇔ F5 ⇔ F6 ⇔ F7 has 6 bilateral equivalences but only **3 mathematically substantive arrows**:
  1. Object A ↔ Object B (av map: chiral E_1 datum to its E_∞ shadow). This is F1 ↔ {F3, F5, F6, F7}.
  2. Object A ↔ Object C (the DNP gauge-theoretic dual). This is F1 ↔ F2.
  3. Object A ↔ Object D (the GZ26 holographic Hamiltonians). This is F1 ↔ F4.

The chain F5 ⇔ F6 (Drinfeld 1985 ⇔ STS 1983) and F4 ⇔ F7 (Gaudin = sphere Hamiltonians) are *internal* to Object B / D respectively and pre-date this work.

**Defense:** the seven presentations matter for *audit*: each comes with its own compute engine (929 tests total per the table at L691–L730), and verifying agreement face-by-face provides an independent witness. The seven count is a *presentation* count, not an *object* count.

**Strongest correct version:** "Theorem (Four-face identification)." The collision residue r(z) admits four distinct categorical realizations:
  (A) the genus-zero binary projection of the universal twisting morphism π_𝒜: B(𝒜) → 𝒜 (E_1 algebraic);
  (B) the semiclassical r-matrix family (PVA, Drinfeld, Sklyanin, Gaudin) — equivalent under classical-limit and Drinfeld–STS identifications;
  (C) the line operator R-matrix in 3d holomorphic-topological gauge theory (DNP);
  (D) the generating function of Gaiotto–Zeng commuting sphere Hamiltonians.
The three substantive arrows A↔B, A↔C, A↔D are each new theorems of the monograph; the four pairwise identifications within (B) and (A,B,D) are pre-existing classical results.

**Repair:** rename "Seven-face identification" to "Four-face identification" with a remark cataloguing the seven *presentations* of the four objects (split as A=1, B=4, C=1, D=1). State the three substantive arrows separately and credit the classical pre-existing identifications.

This deduplication does not weaken the result. It strengthens it by separating the *new theorems* from the *bookkeeping*.

---

### 2.4 Trichotomy k_max ∈ {0,1,≥3} (absence of k=2)

**Location:** standalone/seven_faces.tex L581–L638; Prop. 4.4 L624–L638.

**Attack:** Prop. 4.4 proves that p_max ∈ {1,2}∪{4,5,…} for "bosonic chiral algebras in the standard landscape." But:
  - the b–c ghost system (which the standalone text treats as part of class G via "lattice VOAs, free fermion, bc ghosts" L524) is a *fermionic* system with p_max = 1, half-integer weight (b is weight 2, c is weight −1; OPE pole order ≤ 1).
  - mixed-parity systems (e.g., supersymmetric matter coupled to ghost) can in principle realize p_max = 3.

The proof appeals to "bosonic locality and half-integer weight constraints" (L599) — but the trichotomy theorem (Theorem 4.3, L581) asserts the conclusion *for every 𝒜 in the standard landscape*, including fermionic systems. Either the theorem must be restricted to bosonic algebras, or the argument must be extended.

**Defense:** the bc ghost system has p_max = 1 (b·c OPE simple pole), so k_max = 0, falling in case (i) "Trivial." This is *consistent* with the trichotomy (no k_max = 2 appears). The exclusion of k_max = 2 in the bosonic case is the real content.

**Strongest correct version:** "Theorem (Trichotomy on bosonic chiral algebras of integer weight)." For every 𝒜 in the standard landscape with integer-weight bosonic generators, k_max(𝒜) ∈ {0, 1} ∪ {3, 4, 5, …}. Half-integer weight or fermionic generators may extend the value set; the trichotomy is the bosonic statement.

**Repair:** restrict the theorem to "bosonic, integer-weight" and add a remark on the fermionic/half-integer extension.

---

### 2.5 Class-M elliptic operators "genuinely new"

**Location:** genus1_seven_faces.tex L674–L685 (Remark 5.4).

**Attack:** the assertion "no counterpart in the existing integrable systems literature" (L675) is an overclaim. Etingof–Kirillov elliptic Macdonald operators (Etingof–Kirillov 1996, "Macdonald's polynomials and representations of quantum groups") and the Etingof–Latour–Rains elliptic Calogero–Moser–Sutherland systems both involve precisely the higher-derivative ℘^(m) operators on the elliptic curve. The Felder elliptic Knizhnik–Zamolodchikov equation involves ℘ and is the K-M analog of KZB.

**Defense:** the *mechanism* is new — extracted from the bar-complex Maurer–Cartan element rather than from Hamiltonian reduction or Hecke–Macdonald theory. The class-M algebra (Vir, W_N) inputs are not the standard inputs to elliptic Calogero.

**Strongest correct version:** "Remark (Class-M elliptic operators are familiar but new in provenance)." The higher-derivative elliptic operators ℘^(m) appearing in the class-M collision residue are well-known objects in the elliptic Calogero–Moser–Sutherland and Macdonald–Ruijsenaars literature (Etingof–Kirillov, Etingof–Latour–Rains, Felder). The novelty here is their *provenance* from the chiral bar-cobar Maurer–Cartan element, providing a unified derivation that connects W-algebra collision data to elliptic Hamiltonian systems.

**Repair:** cite Etingof–Kirillov, Felder, Etingof–Latour–Rains; rephrase "no counterpart" as "previously appeared in different categorical contexts; new derivation via bar-cobar."

---

### 2.6 Shadow–formality identification (N6 main theorem)

**Location:** standalone/N6_shadow_formality.tex L157–L169 (Theorem 1.1); L434–L502 (proof).

**Attack:** the theorem identifies Sh_r(𝒜) with the transferred Linf bracket ℓ_r^(0),tr evaluated on the truncated Maurer–Cartan element. The proof Step 2 (L466–L471) chooses a deformation retract (𝔤^{mod,(0)}, h, A^{sh}_{*,0}) and constructs the transferred Linf structure on cohomology. Step 3 then asserts that the genus-zero graph sum (defining Sh_r) and the tree formula (defining ℓ_r^tr) "range over identical planar rooted trees with identical internal-vertex decorations, propagators, and signs." The proof is at the level of *cohomology classes* (Step 1: A^{sh}_{*,0} is the shadow algebra, the cohomology of the genus-zero convolution).

For class M (Virasoro), Corollary 5.3 (L568–L572) asserts intrinsic non-formality "in the sense that no finite truncation of their minimal Linf model is quasi-isomorphic to a dg Lie algebra." This is *correct at the cohomology level* but the chain-level statement is *not proved*. The transferred Linf structure on cohomology can fail to be quasi-isomorphic to a dg Lie algebra even when the chain-level dg Lie algebra is formalisable: formality is a *quasi-isomorphism question*, and the obstruction tower might admit a chain-level formalisation that the *transferred* (cohomology-level) tower cannot see.

**Defense:** the standard convention in Linf-formality is precisely the cohomology-level statement (Kontsevich's theorem is at the cohomology level). The "transferred brackets vanish" criterion is the operative one. Class-M non-formality at cohomology is the substantive content.

**Strongest correct version:** "Theorem (Shadow–formality cohomological identification)." For every chiral algebra 𝒜 and every degree r ≥ 2, the shadow obstruction Sh_r(𝒜) coincides at the level of cohomology classes in A^{sh}_{r,0} with the transferred genus-zero Linf bracket ℓ_r^(0),tr evaluated on the truncated Maurer–Cartan element. As a consequence (Corollary): the shadow termination degree, the transferred A∞-depth, and the Linf-formality level of 𝔤^{mod,(0)} are a single cohomological invariant. Class M is intrinsically non-formal at cohomology; the chain-level statement is left open for non-formal algebras.

**Repair:** make the cohomology level explicit throughout; do not assert the chain-level non-formality without further argument.

---

### 2.7 Hecke decomposition at higher rank (Prop 3.4)

**Location:** standalone/arithmetic_shadows.tex L554–L567.

**Attack:** the proposition asserts ε^c_s(V_Λ) = Σ_j c_j L(s, χ_j) for "L-functions attached to Hecke characters χ_j of the adelic group of the lattice" with "c_j ∈ ℚ algebraic coefficients determined by the lattice geometry." No proof, no construction, no examples beyond what's already in §4 (E₈, ℤ², Leech). The object "adelic group of the lattice" is not defined.

**Defense:** for class-number-1 lattices (E₈, Leech), the Hecke decomposition is a theorem; the assertion is genuinely true on those examples.

**Strongest correct version:** "Proposition (Hecke decomposition for lattices of class number 1)." For an even unimodular lattice Λ of rank r and class number 1, the constrained Epstein zeta admits a Hecke decomposition ε^c_s(V_Λ) = Σ_j c_j L(s, χ_j) where the L-functions are attached to ideal-class characters χ_j of Λ ⊗ ℝ and c_j ∈ ℚ are explicit. For lattices of class number ≥ 2, the decomposition extends with additional L-function summands corresponding to non-trivial ideal classes.

**Repair:** restrict to class number 1 explicitly; cite the classical reference (Siegel 1951, or Schoeneberg).

---

### 2.8 Two-variable L-object L(s, u) sewing-Hecke reciprocity

**Location:** standalone/arithmetic_shadows.tex L1077–L1095.

**Attack:** the equation L(s, u) = Γ(v)/(2π)^v · S(v) (with v = s+u−1) is asserted with no proof and no citation. The "scattering poles of E* at s = ρ/2 are not poles of L_𝒜" is asserted as a structural observation; the *mechanism* (where do the scattering poles go?) is not given.

**Defense:** the Rankin–Selberg unfolding does collapse two variables into one for the Eisenstein integral against a fixed automorphic function. The specific identity is plausible.

**Strongest correct version:** state as a conjecture or proposition with hypothesis "for 𝒜 such that F^conn_𝒜 has rapid decay in y." Provide either a proof sketch (Mellin transform of the Eisenstein integral) or a citation.

**Repair:** convert to remark; cite Iwaniec–Kowalski for the Rankin–Selberg method; add "subject to convergence conditions on F^conn".

---

### 2.9 Ferrero–Washington failure remark

**Location:** chapter/arithmetic_shadows.tex L2695–L2738.

**Attack:** five sub-claims with no proof each (μ-invariant nonvanishing at p=2,5; Mazur inequality at p≤37; arithmetic vs algebraic depth independence; Nahm eigenvalue formula; conductor non-symmetric). The remark environment is not a license to assert.

**Defense:** several of the sub-claims may be true and verifiable; the *Mazur inequality at p ≤ 37* is a finite computation that should have a compute engine.

**Strongest correct version:** split into separate propositions, each properly tagged. Sub-claim (ii) Mazur inequality at p ≤ 37: ProvedHere if a compute engine verifies it. Sub-claim (i) μ ≠ 0: ProvedHere if specific c-values are verified. Sub-claims (iii)–(vi): require either reference or proof or downgrade.

**Repair:** lift each sub-claim to a proper proposition; verify with compute engine; tag accordingly.

---

## Section 3 — Jacobi discriminant and φ_{0,1} normalization audit

### 3.1 Jacobi forms in arithmetic_shadows.tex

**Search results:**

- standalone/arithmetic_shadows.tex L1158: "\"Uber die Fourier-Jacobi-Entwicklung Siegelscher Eisensteinreihen II" — Bocherer 1985 reference, properly cited.
- chapter/arithmetic_shadows.tex L1489: "Jacobi identity cancels the amplitudes at degree ≥ 4" — Lie algebra Jacobi, not Jacobi form. No discriminant claim.
- chapter L3070, L4078, L4091: "Jacobi" refers to Lie algebra Jacobi or theta function identities, not Jacobi forms.

**AP-CY9 verdict (Jacobi discriminant constraint):** Vol I arithmetic_shadows.tex does **not** contain any Jacobi-form coefficient table that would trigger AP-CY9. The Vol III k3_elliptic_genus_bkm_bar machinery is the relevant one for AP-CY9. The Vol I discussion is purely modular (E₂*, E₄, E₈, E₁₂, Δ₁₂); no Jacobi index appears.

**Conclusion:** AP-CY9 not triggered in Vol I scope.

### 3.2 φ_{0,1} normalization (AP-CY42)

**Search results:**

- φ_{0,1} normalization: **not present** in either standalone/arithmetic_shadows.tex or chapter/arithmetic_shadows.tex.
- The K3 elliptic genus appears in *Vol III* k3_elliptic_genus_bkm_bar engine, not in Vol I arithmetic_shadows.

**AP-CY42 verdict:** not triggered in Vol I scope. The chapter's modular machinery is exclusively about (i) lattice theta series (E₈, ℤ², Leech), (ii) holomorphic Eisenstein E_k, (iii) the Ramanujan cusp form Δ₁₂ — all weight-pure objects with no Jacobi index.

### 3.3 AP-CY18 (lattice theta q-power divergence)

**Audit:** the chapter identifies Θ_E₈ = E₄ = 1 + 240·Σ σ₃(n)q^n (L488–L489). At q^1: the coefficient is 240·σ₃(1) = 240. The minimum norm² of E₈ is 2; E₈ has 240 vectors of norm² 2. So r₈(2) = 240 (representation count for n = 1 in 2n indexing). Match.

For Leech: Θ_Leech = E₄³ − 720·Δ has q^0 coefficient 1 and q^1 coefficient 1·240·3 − 720·1 = 720 − 720 = 0 (Leech has *no* vectors of norm² 2 by construction; first nonzero is at norm² 4). Standalone L530–L532: Θ_Leech = E₁₂ − (65520/691)·Δ₁₂. E₁₂ has q^0 = 1, q^1 = (65520/691)·1 (so the cancellation gives q^1 = 0). Cross-check: E₁₂(τ) = 1 + (65520/691)·Σ σ₁₁(n)q^n; Δ₁₂(τ) = q + O(q²); so Θ_Leech = 1 + (65520/691)·1·q − (65520/691)·1·q + O(q²) = 1 + O(q²). q^1 coefficient is *zero*, consistent with Leech minimum norm² = 4. ✓

**AP-CY18 verdict:** the Leech and E₈ identifications correctly handle the q-power matching. AP-CY18 is satisfied.

### 3.4 AP-CY19 (A-hat halving)

**Audit:** chapter/arithmetic_shadows.tex L2636: Â(x) = (x/2)/sinh(x/2). The /2 is *present*. Convergence radius: first pole of sinh(x/2) is at x = 2πi (since sinh(z) = 0 at z = nπi), so convergence radius is |2πi|/|1| = 2π. ✓

**AP-CY19 verdict:** satisfied. The (x/2)/sinh(x/2) form preserves the correct radius.

---

## Section 4 — Seven faces deduplication

The seven presentations of r(z) reduce to **four distinct mathematical objects**:

| Object | Faces collapsed | Categorical home | New theorem? |
|---|---|---|---|
| **A. Twisting morphism** | F1 | E_1 algebraic; B(𝒜) coalgebra | Yes (the bar-intrinsic theorem) |
| **B. Semiclassical r-matrix** | F3 (PVA), F5 (Yangian), F6 (Sklyanin), F7 (Gaudin) | E_∞ shadow; classical limit | No within (B); the av: A → B map is the new theorem |
| **C. Line operator R-twist** | F2 | 3d hol-top gauge theory | Yes (DNP equivalence) |
| **D. Sphere Hamiltonians** | F4 | Holographic / GZ26 | Yes (GZ26) |

The internal identifications inside (B) — Drinfeld 1985 ↔ STS 1983, FFR 1994 — are *classical pre-existing theorems*, not new. The four-object structure exposes:

- One genuinely new categorical object: the universal twisting morphism (Object A).
- Three new functorial arrows from A: A → B (av map), A → C (DNP), A → D (GZ26).
- One classical equivalence class internal to B (Drinfeld–STS–FFR).

**The seven presentations matter for compute audit (929 tests, 14 engines per Section 5 of seven_faces.tex), but the mathematical content is four objects + three arrows.** The "seven-face" branding is presentation-inflated by a factor of ~7/4 ≈ 1.75x.

The strongest correct headline is: **"The four faces of the collision residue: one E_1 datum, three projections."** The four projections are: classical r-matrix family (B), gauge-theoretic R-twist (C), holographic Hamiltonians (D), and the trivial identity F1 = A. The substantive content is the three projection theorems A → B, A → C, A → D.

---

## Section 5 — First-principles analyses

### 5.1 Wrong claim: "The shadow L-function L^sh has poles at s=1 and s=2."

- **Ghost theorem.** D₂(s) = Σ a_n(𝒜) n⁻ˢ with a_n = −24κ·σ₁(n) is an Eisenstein L-function with poles at s=1, 2 from ζ(s)·ζ(s−1). The Eisenstein structure is real.
- **Precise error.** Conflating the Fourier-coefficient Dirichlet series D₂ (which has poles) with the shadow L-function L^sh (which is a *different object*, summing constant terms at degree r). The chapter remark L3458–L3495 explicitly disclaims this *exact* error, but the standalone Prop 4.3 (L639–L663) commits it. *Within-volume contradiction.*
- **Correct relationship.** D₂ has Eisenstein poles; L^sh is convergent in a half-plane and has no Eisenstein poles. The chapter is correct; the standalone has the bug.
- **Confusion type.** Object conflation (D₂ ≠ L^sh). Sub-type: **label/content** (same word "shadow L-function" applied to two different objects).

### 5.2 Wrong claim: "Seven distinct mathematical traditions describe the same r(z)."

- **Ghost theorem.** Object A (twisting morphism) maps to multiple presentations under av and gauge dualities. The functor F1 → {F2, F3, F4, F5, F6, F7} is real.
- **Precise error.** Counting *presentations* (7) as *objects* (claimed 7, actual 4). The Drinfeld–Sklyanin classical equivalence (F5 = F6) and the FFR identification (F4 = F7) reduce to internal classical identifications. F3 is the classical limit of F5.
- **Correct relationship.** Four objects, three new arrows (A → B, A → C, A → D), one classical equivalence class internal to B.
- **Confusion type.** **Presentation/object** (a new sub-type to add to the cache: presentation-counting elevated to object-counting).

### 5.3 Wrong claim: "Class M is intrinsically non-formal (chain-level)."

- **Ghost theorem.** The transferred Linf brackets on cohomology fail to vanish for Virasoro at every degree r ≥ 3.
- **Precise error.** Conflating cohomology-level non-formality (which is what the proof establishes) with chain-level non-formality (which is not addressed). The latter is a stronger statement requiring an obstruction-theoretic argument (see, e.g., Halperin-Stasheff for the rational case).
- **Correct relationship.** Cohomology-level non-formality of class M is proved (Theorem 5 in N6_shadow_formality.tex). Chain-level non-formality is plausible but not addressed.
- **Confusion type.** **chain/cohomology** (#13 in cache taxonomy).

### 5.4 Wrong claim: "Class M elliptic operators have no counterpart in the literature."

- **Ghost theorem.** The class-M collision residue at depth ≥ 3 produces ℘^(m) operators that are genuinely new outputs of the bar-cobar machinery.
- **Precise error.** The *operators* themselves (℘, ℘′, ℘′′, …) appear in Etingof–Kirillov elliptic Macdonald operators, Felder elliptic KZ, and Etingof–Latour–Rains elliptic CMS; they are *not* new operators. What is new is their *derivation via the bar-cobar Maurer–Cartan element from a vertex-algebra OPE*.
- **Correct relationship.** Same operators, new categorical provenance. The novelty is architectural, not computational.
- **Confusion type.** **construction/identification** (#11 + #20 in cache; new construction recovers known invariants).

### 5.5 Wrong claim: "Hilbert reciprocity holds for the shadow field."

- **Ghost theorem.** The Hilbert symbols (κ, Δ)_p and their product formula Π_p (κ, Δ)_p = 1 are real arithmetic invariants of the shadow data.
- **Precise error.** Hilbert reciprocity Π_p (a, b)_p = 1 holds *for all* a, b ∈ ℚ× — it is a *theorem of class field theory*, not a property of "standard families." Asserting it "holds for all standard families" is vacuously true.
- **Correct relationship.** The non-trivial content is the *sign-change correspondence*: (κ, Δ)_p changes sign across consecutive shadow zeros, implying the Hilbert symbol *detects* the shadow-spectral locus crossings. This is the substantive arithmetic content; reciprocity is a structural automatism.
- **Confusion type.** **vacuous/meaningful** (#16 in cache).

### 5.6 Pattern: Dirichlet-series category errors

Both errors 5.1 ("shadow L^sh has Eisenstein poles") and the Hecke-decomposition Prop 3.4 (vague existence claim) share a **Dirichlet-series category error pattern**:

- A Dirichlet series Σ a_n n⁻ˢ has analytic structure (poles, functional equation, Euler product) only if the coefficients a_n have arithmetic structure (multiplicativity, Hecke relations, modular origin).
- The shadow coefficients S_r are *not* multiplicative, *not* in the Selberg class (this is correctly noted at L658–L661), and have *no* known modular origin.
- Treating L^sh as "an L-function" with the *automatic structural properties* of L-functions is the error. L^sh is a Dirichlet series of arbitrary rationals; without an additional structural input (e.g., motivic origin, automorphic origin), it has no analytic continuation, no functional equation, no Euler product.

This is a recurrent pattern. **Defense:** the chapter remark L3458–L3495 explicitly recognizes this. The standalone version regresses to the error.

### 5.7 Pattern: Presentation-inflation

The "seven faces" is an instance of a more general pattern: **counting presentations as objects**. The same pattern appears in:
- "Three CY-A_3 proofs" (when only one inf-categorical proof exists; the other two are restatements).
- "Five Routes to G(K3 × E)" (six routes per CLAUDE.md, but several are equivalent under Verdier or Saito–Kurokawa).
- "Seven Faces of r_CY(z)" (Vol III: same phenomenon, four objects in seven dressings).

**Cache-worthy pattern (new):** *presentation/object* — counting different *names* or *categorical languages* for the same mathematical object as if they were distinct objects.

---

## Section 6 — Three upgrade paths

### 6.1 Upgrade 1: Strongest correct shadow Eisenstein theorem (publication-grade)

**Statement.** For every chirally Koszul chiral algebra 𝒜 with modular characteristic κ = κ(𝒜):
  (i) The genus-1 degree-2 shadow amplitude on 𝓜₁,₁ is Sh₂^(1)(𝒜, τ) = κ · E₂*(τ), where E₂* is the quasi-modular Eisenstein series of weight 2.
  (ii) The Fourier-coefficient Dirichlet series D₂(𝒜, s) = Σ_{n≥1} a_n(𝒜) n⁻ˢ with a_n = −24κ·σ₁(n) factors as D₂(𝒜, s) = −24κ·ζ(s)·ζ(s−1).
  (iii) D₂(𝒜, s) has poles at s=1 (residue −24κ·ζ(0) = 12κ) and s=2 (regularized residue 24κ·ζ(2) = 4κπ²); zeros at the nontrivial ζ-zeros and their +1 shifts.
  (iv) The single algebraic input from 𝒜 is κ; the rest is classical analytic number theory.

**Upgrade content:** explicit residue values (κ-dependent, so genuinely chiral-algebra information); explicit zero locations; D₂-versus-L^sh disclaimer in the theorem itself (not as a downstream remark).

### 6.2 Upgrade 2: Strongest correct four-face theorem (the seven-faces deduplication)

**Statement.** "Theorem (Four-face identification of the collision residue)." Let 𝒜 be a chirally Koszul chiral algebra in the standard landscape. The collision residue r(z) = Res^coll_{0,2}(Θ_𝒜) admits four distinct categorical realizations:
  (A) **E_1 algebraic.** r(z) is the genus-zero binary projection of the universal twisting morphism π_𝒜: B(𝒜) → 𝒜. (F1.)
  (B) **Semiclassical r-matrix.** r(z) is the classical r-matrix of the Yangian Y_ℏ(𝒜^!) (Drinfeld 1985), equivalently the Sklyanin tensor (STS 1983), equivalently the PVA classical r-matrix (Khan–Zeng 2025), equivalently the Gaudin generator (FFR 1994). The internal identifications within (B) are classical. (F3, F5, F6, F7.)
  (C) **3d holographic-topological R-twist.** r(z) is the line operator R-matrix in DNP. (F2.)
  (D) **Holographic sphere Hamiltonians.** r(z) generates the GZ26 commuting differentials. (F4.)

The substantive new theorems are three: A ↔ B (av-map identification), A ↔ C (DNP equivalence), A ↔ D (GZ26 holographic Hamiltonians). The trichotomy of operator orders {0, 0, ≥2} for {C, B∪D∪G-classes, M-class} is genuinely new.

**Upgrade content:** clean separation of new content (3 arrows + 1 trichotomy) from classical (4 internal equivalences within B). Honest credit attribution.

### 6.3 Upgrade 3: Strongest correct shadow–formality identification (cohomology-level)

**Statement.** "Theorem (Shadow–formality cohomological identification)." For every chirally Koszul chiral algebra 𝒜 and every degree r ≥ 2,
  Sh_r(𝒜) = ℓ_r^(0),tr(Θ^{≤r−1}_𝒜, …, Θ^{≤r−1}_𝒜)  in A^{sh}_{r,0}.
The identification is at the level of cohomology classes in the shadow algebra A^{sh}_{*,0} = H^*(𝔤^{mod,(0)}). As a corollary, the shadow termination degree r_max(𝒜), the transferred A∞-depth d_∞(𝒜), and the Linf-formality level f_∞(𝒜) of 𝔤^{mod,(0)} coincide as a single cohomological invariant, classified into four classes G/L/C/M with cohomology-level non-formality of class M.

**Upgrade content:** explicit cohomology-level statement; chain-level extension flagged as open. The class-M cohomological non-formality is the correct, verifiable statement; chain-level non-formality remains a separate question.

---

## Section 7 — Consolidated punch list

### 7.1 Critical (must-fix before any release)

1. **Standalone Prop 4.3 (L639–L663)** has the within-volume contradicted Eisenstein-poles claim for L^sh. *Delete or rewrite as a convergence-only proposition matching the chapter remark L3458–L3495.*

2. **Seven-faces master theorem** (standalone/seven_faces.tex L285–L345): rename to "Four-face identification" and isolate the three substantive new arrows from the four pre-existing classical identifications inside (B). *Restructure §3.1; add deduplication remark.*

3. **Trichotomy theorem** (seven_faces.tex L581–L638): restrict explicitly to "bosonic, integer-weight" landscape; flag the fermionic / half-integer extension as open.

### 7.2 High (should-fix)

4. **Class M elliptic operators "genuinely new"** (genus1_seven_faces.tex L674–L685): add citations to Etingof–Kirillov, Felder, Etingof–Latour–Rains; restate "novelty is provenance, not invention."

5. **Shadow-formality theorem** (N6_shadow_formality.tex L157–L169): add explicit "at the cohomology level" qualifier in the statement; flag chain-level extension as open in Cor 5.3.

6. **Hecke decomposition at higher rank** (Prop 3.4, L554–L567): restrict to class-number-1 lattices; cite Siegel 1951 or Schoeneberg.

7. **Two-variable L(s, u) reciprocity** (L1077–L1095): convert to remark with convergence hypothesis; provide proof sketch or citation.

### 7.3 Medium (worth tightening)

8. **Belavin–Drinfeld for higher rank** (genus1_seven_faces.tex L493–L501): explicitly state proof covers 𝔰𝔩₂ only; higher rank by uniqueness theorem with citation.

9. **Sewing–Selberg formula** (L386–L408): name the regularization of the divergent integral; the constant-term a₀(y) is what gets integrated.

10. **Hilbert reciprocity remark** (chapter L2673–L2693): clarify that reciprocity is automatic; the substance is the *sign-change correspondence*.

11. **Ferrero–Washington failure remark** (chapter L2695–L2738): split into separate propositions, each with proper status tag and (where applicable) compute-engine verification.

12. **Critical-level dim H¹ jump 4 → 8** (genus1_seven_faces.tex L876–L877): cite or derive the specific numbers.

### 7.4 Low (presentation polish)

13. **MZV dictionary** (chapter L2754–L2779): name the channel choice for the genus-0 4-point amplitude; otherwise the κ ↔ ζ(2) coefficient is ambiguous.

14. **κ formula list** (standalone L246–L262): add "AP136 verified: H_N − 1 not H_{N−1}" as a comment (already done in code, missing in tex).

15. **Verlinde polynomial verification** (standalone L832–L847): cite the polynomial-interpolation engine that verifies P₂…P₆.

16. **Norm convention for ε^c_s rank-1** (standalone L499–L531): cite which Vol III engine uses Q(m) = m² and which uses Q(m) = 2m².

### 7.5 Cache write-back

The **presentation/object** confusion type — counting different categorical names or presentations for the same mathematical object as if they were distinct objects — appears in:
- Vol I "Seven Faces of r(z)" (4 objects in 7 dressings, this wave).
- Vol III "Seven Faces of r_CY(z)" (same pattern).
- Vol III "Six Routes to G(K3 × E)" (per CLAUDE.md AP-CY60: "six DIFFERENT mathematical constructions, NOT six applications of the same functor").

**Cache entry to add to first_principles_cache.md (Section IX or new "Presentation Inflation"):**

| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |
|---|-------------|---------------|---------------|---------------------|------|
| N1 | "Seven faces of r(z)" / "seven mathematical traditions describe the same object" | Multiple presentations of one E_1 datum exist | Counting *presentations* (7) as *objects* (claimed 7, actual 4) | Four objects: A=twisting morphism (F1), B=semiclassical r-matrix family {F3,F5,F6,F7} unified by classical Drinfeld–STS, C=DNP gauge R-twist (F2), D=GZ26 holographic (F4). Three new arrows A↔B, A↔C, A↔D | presentation/object (new type) |

---

**Total wave-4 punch list: 16 items** (3 critical + 4 high + 5 medium + 4 low). One new cache entry recommended.

**Bottom-line verdict.** The arithmetic shadows / shadow formality / seven-faces pillar is *mostly sound*. The standalone-versus-chapter D₂/L^sh confusion is the single critical bug that contradicts the chapter's own disclaimer. The seven-faces deduplication is a *strengthening* opportunity, not a downgrade. The class-M elliptic operators are real but not new operators — only new in derivation. The shadow–formality theorem is a cohomology-level result, correctly proved at that level; chain-level extension is open and should be flagged.

The strongest correct version of each load-bearing claim sits one careful rewrite away. None of the 16 punch-list items requires retraction; all admit upgrade paths.
