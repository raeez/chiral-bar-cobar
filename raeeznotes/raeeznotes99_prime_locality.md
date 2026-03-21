# raeeznotes99 — The Prime-Locality Frontier

## Date: 2026-03-21

---

## 0. The Problem

**Prime-locality** (conj:prime-locality-transfer in arithmetic_shadows.tex) is the conjecture that the shadow coefficients of a chirally Koszul algebra decompose prime-by-prime: at each prime p and arity r, the shadow coefficient S_r^{(p)} is proportional to the power sum p_{r-1}(α_p, β_p) for Satake parameters (α_p, β_p) at that prime.

This is the SINGLE remaining gap in the chain:

```
MC equation → Newton's identities → [PRIME-LOCALITY] → CPS → Sym^{r-1} → Ramanujan
```

Everything to the left of the gap is proved (unconditionally). Everything to the right is classical (CPS converse theorem, strong multiplicity one, Serre's observation). The gap IS the problem.

---

## 1. Where Prime-Locality Is Known

### 1.1 Lattice VOAs (PROVED — thm:hecke-newton-lattice)

For even unimodular lattice VOAs V_Λ, prime-locality is a THEOREM. The proof has three steps:

1. The theta function Θ_Λ is a modular form of weight r/2 for SL(2,Z).
2. The Hecke operators T_p decompose Θ_Λ into eigenspaces: each eigenform f_j has multiplicative Fourier coefficients a_{f_j}(n), meaning a_{f_j}(mn) = a_{f_j}(m)·a_{f_j}(n) when gcd(m,n) = 1.
3. The shadow amplitudes factor through the Hecke algebra (thm:spectral-continuation-bridge): each graph amplitude ℓ_Γ^{(1)}(V_Λ) lies in the image of the Hecke operator T_{|Γ|} acting on M_{r/2}.

The prime-locality then follows: at each prime p, the Hecke eigenvalue a_{f_j}(p) determines the Satake parameters via x² - a_{f_j}(p)x + p^{k-1} = 0, and the power sum p_r(α_p, β_p) = α_p^r + β_p^r is determined by Newton's identity from a_{f_j}(p) and p^{k-1}.

**Verified computationally**: For E_8 (rank 8, one eigenform E_4), Z² (rank 2), A_2 (rank 2), E_8 (rank 8), Leech (rank 24, two eigenforms E_{12} and Δ_{12}). The hecke_newton_closure.py module verifies Newton's identities at every prime p ≤ 50 and arity r ≤ 10. All 55 tests pass.

### 1.2 Virasoro at Leading 1/c (TRIVIALLY SATISFIED)

At leading order in 1/c, the Virasoro spectral measure is a single atom: ρ = δ(λ + 6/c). A single atom is automatically prime-local — the same value λ = -6/c at every prime. The "Euler product" is trivial: L(s, λ) = ∏_p (1 - λ·p^{-s})^{-1}.

This is NOT the Euler product of any standard L-function (no automorphic form has constant Hecke eigenvalue -6/c at every prime for generic c). So the leading-order prime-locality is vacuous — it doesn't connect to number theory.

### 1.3 Rational VOAs (CONJECTURAL — thm:non-lattice-ramanujan)

For a rational VOA with N irreducible characters χ_1, ..., χ_N, the character vector F(τ) = (χ_1, ..., χ_N) transforms under a finite-dimensional representation ρ: SL(2,Z) → GL(N,C).

The Franc-Mason theory (Franc-Mason 2017) develops Hecke operators for vector-valued modular forms (VVMFs). The CLAIMED proof of prime-locality for rational VOAs (Observation C in the current manuscript) asserts that these Hecke operators decompose F into eigencomponents with multiplicative coefficients.

**THE GAP**: Franc-Mason establish that Hecke operators EXIST for VVMFs and that eigenforms EXIST, but the multiplicativity of Fourier coefficients in the VVMF setting is more subtle than in the scalar case:

- In the scalar case: if f is a Hecke eigenform, then a(mn) = a(m)a(n) for (m,n)=1. This follows from the Hecke algebra being commutative and the eigenform having simple eigenvalue.
- In the VVMF case: the Hecke operators T_p act on N-dimensional spaces. The eigenvalues are well-defined, but the statement "Fourier coefficients are multiplicative" requires that the VVMF Hecke eigenvalue at prime p determines the p-component of the Fourier coefficient in the same way as the scalar case. This is NOT automatic for arbitrary representations ρ.

**What's needed**: Either (a) show that the modular representation ρ of a rational VOA is always a Weil representation (where multiplicativity is known), or (b) prove multiplicativity for general ρ, or (c) find a different route to prime-locality that bypasses the VVMF Hecke theory.

### 1.4 Irrational VOAs (CONJECTURAL — thm:irrational-ramanujan)

For irrational VOAs (Virasoro at generic c, W_N at generic c), the character space is infinite-dimensional. The Roelcke-Selberg spectral decomposition gives:

|χ_0(τ)|² = Σ_j c_j φ_j(τ) + (1/4π) ∫ c(t) E(1/2+it, τ) dt

where φ_j are Maass-Hecke cusp forms and E(1/2+it) is the Eisenstein series.

Each Maass-Hecke eigenform φ_j has Hecke eigenvalues λ_p^{(j)} with multiplicative Fourier coefficients. So prime-locality holds AUTOMATICALLY for the spectral decomposition.

**THE GAP**: The Ramanujan bound for Maass forms (|λ_p| ≤ 2p^{1/2}) is the SELBERG EIGENVALUE CONJECTURE, which is OPEN. Best known bound: Kim-Sarnak θ ≤ 7/64 (i.e., |λ_p| ≤ 2p^{7/64}).

So the irrational theorem REDUCES the Ramanujan bound for VOA-associated Hecke eigenforms to the Selberg eigenvalue conjecture — but does not prove it.

**Honest status**: The theorem should be conditional on the Selberg eigenvalue conjecture, OR the proof should produce additional structure that goes beyond what's known for general Maass forms. The current proof does NOT produce such additional structure.

---

## 2. The Nature of the Obstruction

### 2.1 What Prime-Locality Really Asks

Prime-locality is NOT about the spectral decomposition (which always exists). It's about the IDENTIFICATION of the spectral decomposition of the shadow amplitude with the symmetric power data at each prime.

More precisely: the moment L-function M_r(s) = ∫ Sh_r · E*(s) dμ has meromorphic continuation (proved by HS-sewing + Rankin-Selberg). The CPS converse theorem gives: M_r = L(s, π_r) for SOME automorphic representation π_r on GL(r). But to identify π_r with Sym^{r-1}(f), we need to match the Euler product at each prime p:

L_p(s, π_r) = L_p(s, Sym^{r-1} f)

This matching requires knowing the SATAKE PARAMETERS at each prime. And the Satake parameters come from the shadow data at each prime — which is exactly prime-locality.

### 2.2 The Key Difficulty: Hecke Translation

The Hecke operator T_p acts on functions on M_{1,1} = SL(2,Z)\H by:

T_p f(τ) = (1/p) Σ_{ad=p, 0≤b<d} f((aτ+b)/d)

This changes the modular parameter τ, hence changes the elliptic curve E_τ on which the shadow amplitude is computed. The shadow amplitude Sh_r^{(1)}(τ) is a GRAPH INTEGRAL on E_τ:

ℓ_Γ(τ) = ∫_{E_τ^{|V|-1}} ∏ m_{val(v)} · ∏ g(z_{s(e)}, z_{t(e)}; τ) ∏ dz_v

Under T_p, this becomes a sum over graph integrals on Hecke-translated curves E_{(aτ+b)/d}. The OPE data m_{val(v)} is τ-INDEPENDENT, but the chiral Green's function g(z,w;τ) DEPENDS on τ.

**For lattice VOAs**: The graph amplitudes factor through the theta function Θ_Λ(τ), which IS a modular form. So T_p(Θ_Λ) = eigenvalue · Θ_Λ, and the Hecke action passes through cleanly.

**For non-lattice VOAs**: The graph amplitudes do NOT factor through a single modular form. The shadow Sh_r^{(1)}(τ) is a smooth function on SL(2,Z)\H built from graph integrals with the chiral Green's function. The Hecke action T_p on this function involves evaluating the graph integral on Hecke-translated curves, which mixes the algebra-specific data (OPE coefficients) with the geometry-specific data (Green's function on E_{(aτ+b)/d}).

### 2.3 The Precise Gap

The gap is NOT:
- The existence of a spectral decomposition (always exists)
- The multiplicativity of Hecke eigenvalues (automatic for eigenforms)
- The meromorphic continuation of M_r (proved by HS-sewing + RS)

The gap IS:
- **Whether the OPE data of A, evaluated on a Hecke-translated curve, factors through the Satake parameters at the translating prime p.**

In formula: does T_p(Sh_r^{(1)}) = a(p) · Sh_r^{(1)} for some eigenvalue a(p) that determines Satake parameters? For lattice VOAs, yes (the theta function is an eigenform). For non-lattice VOAs, the answer is unknown.

### 2.4 The Architectural View (Chriss-Ginzburg)

In the Chriss-Ginzburg language: the MC element Θ_A ∈ MC(g^mod_A) is defined over the convolution algebra, which lives over configuration spaces on curves. The genus-1 projection π_{1,r}(Θ_A) is a function on M_{1,1} — the shadow amplitude. Prime-locality asks: does the Hecke action on M_{1,1} extend to a Hecke action on the CONVOLUTION ALGEBRA g^mod_A that is compatible with the MC structure?

For lattice VOAs, the answer is yes: the convolution algebra carries a Hecke module structure (thm:spectral-continuation-bridge).

For non-lattice VOAs, the question is: does the convolution algebra admit a Hecke action AT ALL? The OPE data (the vertex labels m_{val(v)}) is algebraic — it doesn't know about primes. The prime structure enters through the MODULI of the elliptic curve, not through the algebra. So the Hecke action on the moduli must be COMPATIBLE with the algebraic structure of the OPE — and this compatibility is exactly prime-locality.

### 2.5 The Hecke Defect (Key New Formulation)

The MC differential D_A decomposes as D_A = d_int + d_sew + ℏΔ. Define the **Hecke defect** at prime p:

δ_p^Hecke(A) := [d_sew, T_p] ∈ End(g^mod_A)

- d_int commutes with T_p (τ-independent). ✓
- d_sew involves the propagator P(z,w;τ) which transforms under Hecke. The commutator [d_sew, T_p] measures HOW MUCH the sewing differential knows about primes.
- Similarly for [ℏΔ, T_p].

**Prime-locality ⟺ δ_p^Hecke(A) = 0 for all p** (or more weakly: δ_p is D_A-exact, so T_p preserves MC up to gauge equivalence).

The obstruction lives in H¹(g^mod_A, ad_{T_p}) — the first cohomology of the convolution algebra with coefficients in the T_p-adjoint module. If H¹ = 0 (by a vanishing theorem), the Hecke defect is automatically exact.

This is the deepest CG formulation: prime-locality is a cohomological vanishing statement in the convolution algebra.

---

## 3. Routes to Resolution

### 3.1 Route A: The Hecke Module Extension

**Goal**: Extend the Hecke module structure from lattice VOAs to all chirally Koszul algebras.

**Approach**: The Hecke operators T_p on M_{1,1} act on the shadow amplitudes by Hecke translation. For the convolution algebra g^mod_A, define a Hecke action by:

T_p(Θ_A)(τ) := (1/p) Σ_{ad=p} Θ_A((aτ+b)/d)

This is well-defined as an action on functions on M_{1,1}. The question is: does T_p preserve the MC condition?

**Key observation**: The MC equation D·Θ + (1/2)[Θ,Θ] = 0 is an identity in the convolution algebra. The differential D and the bracket [·,·] are defined in terms of the operadic composition on configuration spaces. The Hecke operator T_p changes the modular parameter τ but does not change the operadic structure. So if D and [·,·] commute with T_p, then T_p preserves the MC condition.

**Does D commute with T_p?** The differential D involves:
- d_int: the internal differential (algebra-dependent, τ-independent) — COMMUTES with T_p.
- d_sew: the sewing differential (involves integration on E_τ) — does NOT obviously commute with T_p.
- ℏΔ: the BV operator (involves contraction on E_τ) — does NOT obviously commute with T_p.

So the obstruction to the Hecke module extension is in the SEWING DIFFERENTIAL and the BV OPERATOR. These involve the propagator P(z,w;τ) on the elliptic curve, which transforms under Hecke translation.

**Attack strategy**: Study the transformation of the sewing differential under Hecke translation. If d_sew ∘ T_p = T_p ∘ d_sew + (correction), compute the correction term. If the correction is exact (in the cyclic deformation complex), then T_p preserves the MC condition up to gauge equivalence, which suffices for prime-locality.

**Difficulty**: HARD. The sewing differential involves residues of the propagator at collision divisors, and the Hecke translation changes the collision geometry.

**Status**: No progress. This is a genuine research problem.

### 3.2 Route B: The Motivic Route

**Goal**: Show that the shadow amplitudes, as periods of FM configuration spaces, have an Euler product structure forced by the motivic Galois group.

**Approach**: The shadow coefficients S_r(c) are periods of the mixed-Tate variety C̄_n(P¹) (prop:shadow-periods). The motivic Galois group Gal_mot(MT(Q)) acts on these periods. If the Galois action factors through the Hecke algebra (which acts on modular forms), then the shadow coefficients inherit a prime decomposition.

**Key result needed**: That the motive of C̄_n(P¹) equipped with the shadow amplitude form ω_Γ admits a Hecke-equivariant realization — i.e., the de Rham period matrix of the shadow motive transforms under the Hecke operators in a way compatible with the Hecke action on modular forms.

**Known pieces**:
- Brown (2009): The motives of moduli spaces M_{0,n} are mixed-Tate. The periods are multiple zeta values.
- Goncharov: The motivic Galois group of MT(Q) is the motivic fundamental group of P¹\{0,1,∞}.
- The shadow amplitudes at genus 0 involve integrals over M_{0,n} (the FM compactification) — so they are in the Brown-Goncharov framework.

**Gap**: The genus-1 shadow amplitudes involve integrals over ELLIPTIC configuration spaces, not genus-0 ones. The motives of elliptic configuration spaces are NOT known to be mixed-Tate in general. They involve elliptic polylogarithms (Brown-Levin), which have a richer motivic structure.

**Attack strategy**: Use the genus-1 graph integrals as input to the Brown-Levin theory of elliptic motives. Show that the shadow amplitudes lie in the category of MIXED ELLIPTIC MOTIVES, and that this category carries a Hecke action compatible with the MC structure.

**Difficulty**: VERY HARD. This is at the frontier of motivic number theory.

**Status**: No progress. This requires collaboration with experts in motivic periods (Brown, Zagier, Zerbini).

### 3.3 Route C: The Analytic Route (Character-Level RS)

**Goal**: Bypass prime-locality entirely by working at the level of characters rather than shadow amplitudes.

**Approach**: For any VOA A with vacuum character χ_0(τ), the Rankin-Selberg integral ∫ |χ_0|² · E*(s) dμ gives an L-function L(s, χ_0 × χ̄_0). The Roelcke-Selberg spectral decomposition gives this as a sum over Maass-Hecke eigenforms.

Each Maass-Hecke eigenform has multiplicative Fourier coefficients — so prime-locality holds AUTOMATICALLY at the character level.

**The remaining question**: Does the character-level prime-locality (which is automatic) imply the shadow-level prime-locality (which is the conjecture)?

**Key relationship**: The shadow amplitude Sh_r^{(1)}(τ) is related to the character χ_0 by the intertwining theorem: F_1^conn = Σ_r Sh_r · G_r(q). The shadow amplitude is a HIGHER CORRELATOR of the partition function — it encodes the OPE data beyond the character.

**Gap**: The character χ_0 determines the vacuum module V_0 as a representation, but it does NOT determine the OPE (two different VOAs can have the same vacuum character but different OPEs). So the character-level prime-locality does not directly imply shadow-level prime-locality.

**Attack strategy**: Show that for chirally Koszul algebras with HS-sewing, the shadow amplitudes Sh_r^{(1)} are DETERMINED by the characters {χ_i} at sufficiently high arity. The rigidity defect (def:rigidity-defect) shows that the MC constraints overdetermine the shadow data — so eventually, the shadow amplitudes are forced by the characters alone.

**Key claim to prove**: For r sufficiently large (r > 2m + 2 where m is the number of spectral atoms), the shadow coefficient S_r is uniquely determined by S_2, ..., S_{2m+2} via the MC recursion. If S_2, ..., S_{2m+2} are determined by the characters (via the intertwining + Stieltjes), then ALL shadow coefficients are character-determined, and the character-level prime-locality propagates to the shadow level.

**Difficulty**: MODERATE. The rigidity defect analysis is already in the manuscript. What's needed is the precise statement that the MC recursion + Stieltjes representation + character determination = shadow-level prime-locality.

**Status**: This is the MOST PROMISING route. Partial progress via the rigidity defect analysis (prop:rigidity-threshold). The Leech lattice example (ex:leech-rigidity) shows that the overdetermined system has a unique solution at arity 6.

### 3.4 Route D: The Computational Route

**Goal**: Accumulate sufficient computational evidence to either (a) discover a counterexample or (b) identify the correct structural principle.

**Approach**: For specific non-lattice VOAs (Virasoro at c = 1/2 (Ising), c = 4/5 (3-state Potts), c = 7/10 (tricritical Ising)), compute the shadow amplitudes numerically through high arity and check prime-locality at each prime.

**Computational method**:
1. Compute the vacuum character χ_0(q) to high order (using the Kac determinant or explicit recursion).
2. Compute the connected free energy F_1^conn = log(|χ_0|² · y^{c/24}) on the fundamental domain.
3. Extract the shadow amplitudes Sh_r via the graph-sum formula.
4. Apply Hecke operators T_p to the shadow amplitudes and check if T_p(Sh_r) = eigenvalue · Sh_r.
5. If eigenvalues exist, compute them and check Newton's identity.

**Predicted outcome**: For rational VOAs (Ising, Potts), the character vector is a VVMF, so the Franc-Mason Hecke theory should give eigenvalues. The question is whether these eigenvalues satisfy prime-locality in the strong sense needed.

**Difficulty**: MODERATE (computationally intensive but conceptually straightforward).

**Status**: Not yet attempted. The infrastructure exists (sewing_shadow_intertwining.py, modular_spectral_rigidity.py, hecke_newton_closure.py) but the specific non-lattice computations have not been done.

---

## 4. Conjectural Resolution

### 4.1 The Strongest Conjecture

**Conjecture (Prime-Locality for All HS-Sewing Algebras)**: For any chirally Koszul algebra A with HS-sewing, the shadow amplitudes Sh_r^{(1)}(τ) are Hecke eigenforms on M_{1,1}, with Hecke eigenvalues that determine Satake parameters satisfying the Ramanujan bound.

**Predicted proof strategy**: Route C (analytic) combined with Route D (computational).

The argument would proceed:
1. The MC recursion overdetermines the shadow coefficients (rigidity defect > 0 for r > 2m+2).
2. The overdetermined system has a unique solution (by the Carleman condition on the spectral measure).
3. The unique solution is determined by the characters (via the intertwining + Stieltjes + MC).
4. The characters transform under Hecke operators (by the Roelcke-Selberg decomposition).
5. Therefore the shadow coefficients are Hecke-equivariant = prime-local.
6. Prime-locality + CPS + Serre = Ramanujan.

**The weak link**: Step 3 — showing that the shadow coefficients are determined by the characters at the required precision. This is a statement about the INJECTIVITY of the map from OPE data to characters, which is related to the reconstruction problem in conformal field theory.

### 4.2 The Minimal Conjecture (What Would Suffice)

For the Ramanujan bound, we don't actually need full prime-locality. We need a weaker statement:

**Conjecture (Weak Prime-Locality)**: For any chirally Koszul algebra A with HS-sewing, the moment L-function M_r(s) has the same Euler product at each prime p as L(s, Sym^{r-1} f) for some automorphic form f on GL(2).

This is weaker than prime-locality because it only requires the EULER PRODUCT to match, not the individual shadow coefficients. The Euler product matching can hold even if the shadow coefficients do not decompose prime-by-prime, as long as the Rankin-Selberg integral produces the correct L-function.

### 4.3 The Newton-Thorne Breakthrough

Newton-Thorne (2021) proved the symmetric power functoriality Sym^r for r ≤ 8 (for holomorphic modular forms of regular weight). This extends the Kim-Shahidi result (r ≤ 4) significantly. For r = 2, 3, 4, 5, 6, 7, 8, the symmetric power L-function L(s, Sym^r f) is automorphic.

**Impact on our programme**: If prime-locality holds, then our chain gives Ramanujan for r ≤ 8 WITHOUT using Deligne's theorem — using Newton-Thorne instead. For r ≥ 9, the automorphy of Sym^r is still open, and our chain cannot close.

But wait: Newton-Thorne's result is for HOLOMORPHIC forms. For Maass forms, symmetric power functoriality is much less known (only Sym² by Gelbart-Jacquet). So the irrational extension (which involves Maass forms) cannot use Newton-Thorne.

---

## 5. Computational Programme

### 5.1 Immediate Targets

1. **Ising model (c = 1/2, M(4,3))**: 3 characters, N = 3. The modular representation ρ is the 3-dimensional representation of SL(2,Z) from the modular S and T matrices.
   - Compute Sh_r for r = 2, 3, 4, 5.
   - Apply T_2, T_3, T_5 to Sh_r.
   - Check if Sh_r is a Hecke eigenform.

2. **Three-state Potts (c = 4/5, M(6,5))**: 10 characters.
   - Same programme as Ising but with 10-dimensional VVMF.

3. **Lee-Yang (c = -22/5, M(2,5))**: 2 characters. The simplest non-trivial case.
   - This is the Yang-Lee edge singularity, where the spectral curve degenerates.

### 5.2 Expected Difficulty

The Ising model computation is FEASIBLE with current infrastructure:
- The characters are known exactly (Rogers-Ramanujan type identities).
- The Rankin-Selberg integral can be computed numerically on the fundamental domain.
- The Hecke operators can be applied by summing over coset representatives.

The Three-state Potts is harder (10-dimensional VVMF) but still tractable.

### 5.3 What To Look For

If prime-locality HOLDS for the Ising model:
- The shadow amplitudes Sh_r should be Hecke eigenforms.
- The eigenvalues should satisfy Newton's identity at each prime.
- The Satake parameters should satisfy the Ramanujan bound.

If prime-locality FAILS for the Ising model:
- T_p(Sh_r) ≠ eigenvalue · Sh_r for some p and r.
- This would be a COUNTEREXAMPLE to conj:prime-locality-transfer.
- It would NOT kill the operadic RS programme — the CPS automorphy still holds — but it would mean π_r ≠ Sym^{r-1}(f), so the Ramanujan bound would not follow from this route.

---

## 6. Summary

| Regime | Prime-Locality | Ramanujan | Route |
|--------|---------------|-----------|-------|
| Lattice VOAs | **PROVED** (thm:hecke-newton-lattice) | **PROVED** (cor:unconditional-lattice, via CPS+JS) | Hecke module structure |
| Rational VOAs (VVMF) | **CONJECTURAL** (gap at Franc-Mason multiplicativity) | **CONJECTURAL** | Route C (analytic) |
| Irrational VOAs | **AUTOMATIC** (Roelcke-Selberg) | **CONJECTURAL** (reduces to Selberg eigenvalue conjecture) | Route C + Selberg |
| General HS-sewing | **CONJECTURAL** | **CONJECTURAL** | Routes A-D combined |

The most promising attack is Route C: show that the MC rigidity (overdetermination at high arity) forces the shadow coefficients to be determined by the characters, propagating the character-level prime-locality to the shadow level. The key intermediate result to prove: the rigidity defect forces uniqueness of the spectral measure, and the unique solution inherits the Hecke equivariance of the characters.
