# Compute Engine: Complete Next Steps Registry

**Generated**: 2026-03-06, Session 117
**Baseline**: 1080 tests, 32 live lib files (11K lines), 34 test files (6.3K lines), 59 scripts (22K lines)
**Architecture**: Python 3.14, sympy 1.14.0, numpy 2.4.2, pytest 9.0.2, venv at `compute/.venv/`

---

## How to Use This Document

Each item below is a self-contained work unit. Items are grouped by dependency, not priority. Every item specifies:

- **What**: precise mathematical or engineering goal
- **Where**: exact file paths, function signatures, line numbers
- **How**: algorithmic specification detailed enough to implement without re-derivation
- **Verify**: executable command or assertion to confirm correctness
- **Pitfalls**: specific failure modes to avoid (informed by prior failures in this codebase)

**Dependency graph** (read downward):

```
[E1] Script cleanup ─────────────────────────────────────────────────────────
[E2] Name normalization ─────────────────────────────────────────────────────
[M1] Adjoint invariants ──┬── [M3] sl₂ bar from E₁ ──┬── [M5] sl₃ bar from E₁
[M2] CE with coefficients ┘                          │
                                                     └── [M6] Virasoro d₁
[M4] Full bar differential ── [M7] sl₃ H⁴ ── [M8] W₃ H⁵
[M9] Koszul relation engine ─────────────────────────────────────────────────
[M10] βγ Koszul inversion ──────────────────────────────────────────────────
[M11] W₃ H⁴ provenance ─────────────────────────────────────────────────────
[T1] Deeper property tests ──────────────────────────────────────────────────
[T2] Regression harness ────────────────────────────────────────────────────
```

---

## TIER 1: Engineering (no mathematical difficulty)

### E1. Script Audit and Cleanup

**What**: The `compute/scripts/` directory has 59 files (22K lines), many of which are one-off explorations from prior sessions. Classify each as KEEP (useful diagnostic), ARCHIVE (historical, move to `scripts/_archive/`), or DELETE (duplicates archived lib code).

**Where**: `compute/scripts/*.py` (59 files)

**How**:
1. Read the docstring and first 20 lines of each script
2. Check if it imports from `compute.lib._archive` (dead dependency) or from live `compute.lib`
3. Classify:
   - KEEP if it runs against live lib and produces useful output (e.g., `verify_master_table.py`, `compute_genus.py`)
   - ARCHIVE if it was an exploration that produced results now captured in lib (e.g., the 15+ `sl3_*.py` GF search scripts)
   - DELETE only if it's an exact duplicate of another script

**Verify**: `ls compute/scripts/ | wc -l` should decrease; `python -m pytest compute/tests/ -q` still 1080 passing

**Pitfalls**:
- Do NOT delete scripts that document the "wrong tree" investigation (d²≠0 sign search). These are historically valuable as evidence.
- Some scripts (e.g., `sl3_modular_rank.py`) contain working code that should be promoted to lib, not archived.

**Candidates for promotion to lib**:
- `sl3_modular_rank.py` → has working weight-decomposed bracket differential for sl₃ (lines 207-286)
- `verify_master_table.py` → already referenced by `make verify`

**Estimated script classification** (from headers read this session):
- KEEP: `verify_master_table.py`, `compute_genus.py`, `compute_bar_complex.py`, `sl3_modular_rank.py`
- ARCHIVE (sl₃ GF search, ~15 files): `sl3_algebraic_eq.py`, `sl3_algebraic_fit.py`, `sl3_bar_cohomology.py`, `sl3_bar_correct.py`, `sl3_bar_direct.py`, `sl3_bar_from_riordan.py`, `sl3_gf_analysis.py`, `sl3_gf_search.py`, `sl3_growth_rate.py`, `sl3_h4_search.py`, `sl3_koszul_constraint.py`, `sl3_phi_ansatz.py`, `sl3_phi_extended.py`, `sl3_psi_search.py`
- ARCHIVE (d²≠0 investigation, ~8 files): `debug_d2.py`, `debug_d2_trace.py`, `find_d2_sign.py`, `find_sign_convention.py`, `sl2_bar_debug.py`, `sl2_bar_validate.py`, `sl3_bar_sign_test.py`, `sl3_sign_search.py`
- ARCHIVE (W₃ search, ~4 files): `w3_algebraic_gf.py`, `w3_gf_systematic.py`, `w3_lie_cohomology.py`, `w3_recurrence.py`
- Needs inspection: remaining ~28 scripts

---

### E2. Name Normalization Across Registries

**What**: The engine uses inconsistent names for the same algebras across modules:
- `"beta_gamma"` in `KNOWN_BAR_DIMS` vs `"betagamma"` in `ALGEBRA_REGISTRY`
- `"Yangian_sl2"` in `KNOWN_BAR_DIMS` but absent from `ALGEBRA_REGISTRY`
- `"Heisenberg"` (capital H) everywhere except some test parameterizations

**Where**:
- `compute/lib/bar_complex.py:379-400` — `KNOWN_BAR_DIMS` keys
- `compute/lib/cross_algebra.py:33-166` — `ALGEBRA_REGISTRY` keys
- `compute/lib/koszul_pairs.py:32-65` — `KOSZUL_PAIRS` keys
- `compute/lib/cross_algebra.py:341-348` — `bar_to_reg` name mapping (current workaround)

**How**:
1. Pick canonical names: `heisenberg`, `free_fermion`, `beta_gamma`, `bc`, `sl2`, `sl3`, `virasoro`, `w3`, `e8`, `b2`, `g2`, `yangian_sl2`
2. Update all 4 registries to use canonical names
3. Update all tests that reference these names
4. Remove the `bar_to_reg` mapping hack in `verify_registry_consistency()`

**Verify**: `python -m pytest compute/tests/ -q` still 1080 passing; `grep -r '"Heisenberg"' compute/lib/ | wc -l` matches `grep -r '"heisenberg"' compute/lib/ | wc -l` (one or the other, not both)

**Pitfalls**:
- Many tests hardcode the current names. A find-and-replace must be thorough.
- `ALGEBRA_REGISTRY` keys are used by `spectral_sequence_collapse()` — the key must match.
- The name "Heisenberg" with capital H appears in user-facing output strings, not just dict keys. Distinguish between internal keys (normalize) and display names (keep capitalized).

---

### E3. Conftest and Import Hygiene

**What**: Tests currently rely on `conftest.py` adding the repo root to `sys.path`. This is fragile. Ensure `compute/` is a proper installable package.

**Where**: `compute/conftest.py`, `compute/lib/__init__.py`, `compute/tests/conftest.py`

**How**:
1. Check if a `pyproject.toml` or `setup.py` exists — if not, create minimal `pyproject.toml` with `[project]` and `[tool.pytest.ini_options]`
2. Install in editable mode: `pip install -e .` from the repo root
3. Remove `sys.path` hacks from conftest

**Verify**: `cd /tmp && python -c "from compute.lib import OPEAlgebra"` should work after install

**Pitfalls**:
- Do NOT create a full package with versioning, CI, etc. — this is a research codebase, not a distributable library. Minimal `pyproject.toml` only.
- The venv is at `compute/.venv/`, not the repo root. The editable install must target this venv.

---

## TIER 2: Mathematical Computation (feasible, well-specified)

### M1. Adjoint Invariant Dimensions (Molien Series)

**What**: Compute dim(Sym^n(g)^g) — the dimension of g-invariants in symmetric powers of the adjoint representation. This is the missing piece for the E₁ page computation at CE degree 0.

**Where**: New function in `compute/lib/spectral_sequence.py`, after `_sym_module_dim()`

**How**: For a semisimple g with Weyl group W and exponents m₁, ..., m_r:

```
Molien series: sum_{n>=0} dim(Sym^n(g)^g) t^n = 1 / prod_{i=1}^{r} (1 - t^{m_i + 1})
```

For sl₂: exponents = [1], so Molien = 1/(1-t²). Invariants: 1, 0, 1, 0, 1, ...
For sl₃: exponents = [1, 2], so Molien = 1/((1-t²)(1-t³)). Invariants: 1, 0, 1, 1, 1, 2, 2, ...

But we need invariants in `Sym(g ⊗ t⁻¹k[t⁻¹])`, not just `Sym(g)`. This decomposes by conformal weight h. At weight h, the coefficient module M_h has a g-action via the adjoint on each tensor factor.

For weight h=1: M₁ = g (adjoint), dim(g^g) = rank(g) (Cartan elements)
For weight h=2: M₂ = g⊕Sym²(g), the invariant computation involves the Casimir.

**Algorithm**:
1. For sl₂: build the 3-dim adjoint representation matrices ρ(e), ρ(f), ρ(h)
2. For weight h, build M_h as a g-module (tensor product of adjoint copies at various modes)
3. Compute dim(ker(ρ(e)) ∩ ker(ρ(f)) ∩ ker(ρ(h))) = dim(M_h^g)

For sl₂ this is tractable: adjoint = V₂ (spin-1 rep, 3-dim), Sym²(ad) = V₀ ⊕ V₂ ⊕ V₄ (dims 1+3+5=9), invariants in Sym²(ad) = dim(V₀) = 1.

```python
def adjoint_invariant_dim(dim_g: int, structure_constants: Dict, weight: int) -> int:
    """Dimension of g-invariants in the weight-h part of Sym(g[t^{-1}])."""
```

**Verify**: For sl₂:
- Weight 0: dim = 1 (scalars)
- Weight 1: dim = 0 (adjoint has no invariants for simple g)
- Weight 2: dim = 1 (Casimir)
- Weight 3: dim = 0 (odd weight, Molien 1/(1-t²) has no t³ term)

Check: `assert adjoint_invariant_dim(3, sl2_sc, 0) == 1`
Check: `assert adjoint_invariant_dim(3, sl2_sc, 1) == 0`
Check: `assert adjoint_invariant_dim(3, sl2_sc, 2) == 1`

**Pitfalls**:
- The M_h module at weight h is NOT simply Sym^h(g). It is the weight-h part of Sym(⊕_{m≥1} g_m) where g_m = g at mode -m has conformal weight m. At weight 2, this includes Sym²(g₁) ⊕ g₂, where g₂ is another copy of g at mode -2.
- The g-action is diagonal (acts on each tensor factor independently via adjoint). Do NOT conflate the adjoint action on mode -1 generators with the action on mode -2 generators — they are the same representation but on different copies.
- For sl₂ the invariant ring of Sym(g) has generators at degrees 2, not 1 (the Casimir is quadratic). So dim(Sym^1(g)^g) = 0, not rank(g). This is correct — the Cartan subalgebra is NOT g-invariant (h is NOT killed by ad(e), ad(f)).

---

### M2. CE Cohomology with Nontrivial Coefficients

**What**: Compute H^p(g, M) where M is a finite-dimensional g-module (not just trivial coefficients). This generalizes `ce_cohomology_dims()` which currently only handles M = k.

**Where**: New function in `compute/lib/spectral_sequence.py`

**How**: The CE complex with coefficients is:
```
C^p(g, M) = Hom(Λ^p(g), M) ≅ Λ^p(g*) ⊗ M
```
with differential:
```
(dω)(x₀,...,x_p) = Σᵢ (-1)^i xᵢ · ω(x₀,...,x̂ᵢ,...,x_p)
                  + Σᵢ<ⱼ (-1)^{i+j} ω([xᵢ,xⱼ], x₀,...,x̂ᵢ,...,x̂ⱼ,...,x_p)
```

The first term involves the g-action on M (absent for trivial coefficients).

```python
def ce_differential_with_coefficients(
    dim_g: int,
    structure_constants: Dict,
    module_dim: int,
    module_action: Dict[int, Matrix],  # g_i -> dim_M x dim_M matrix
    degree: int,
) -> Matrix:
    """CE differential d: Λ^degree(g*) ⊗ M -> Λ^{degree+1}(g*) ⊗ M."""
```

**Matrix structure**: The source space has dimension C(dim_g, degree) * module_dim. The target has dimension C(dim_g, degree+1) * module_dim. The matrix is block-structured: each block corresponds to a pair of Λ-basis elements, and within each block the module action appears.

**Verify**: For g = sl₂, M = adjoint (3-dim):
- C^0 = M (3-dim), C^1 = g* ⊗ M (9-dim), C^2 = Λ²(g*) ⊗ M (9-dim), C^3 = Λ³(g*) ⊗ M (3-dim)
- H^0(sl₂, ad) = 0 (no invariants for simple g in adjoint)
- H^1(sl₂, ad) = 0 (Whitehead)
- H^2(sl₂, ad) = 0 (Whitehead)
- H^3(sl₂, ad) = 0 (Whitehead + Poincaré duality)

Check: `assert all(d == 0 for d in ce_cohomology_with_coefficients_dims(3, sl2_sc, ad_matrices))`

**Pitfalls**:
- The differential has TWO terms: the Lie bracket term (already implemented in `ce_differential_matrix`) and the module action term (new). Do not forget the module action term — it is what distinguishes trivial from nontrivial coefficients.
- Signs: the module action term has sign (-1)^i for position i in the exterior product. Get this exactly right or d²≠0.
- Test d²=0 FIRST, before computing cohomology. If d²≠0, the signs are wrong.

---

### M3. sl₂ Bar Cohomology from E₁ Page

**What**: Derive the Riordan numbers R(n+3) from the PBW spectral sequence E₁ page, using M1 and M2 above. This would be the first computation of sl₂ bar cohomology from first principles in the engine.

**Where**: New function in `compute/lib/spectral_sequence.py`

**How**: For sl₂ at generic level, E₁ collapses (Whitehead). The bar cohomology at degree n is:
```
H^n(B̄(ŝl₂)) = Σ_h E₁^{n,h} = Σ_h dim H^n(sl₂, M_h)
```

Wait — this is more subtle. The bar degree n involves ALL CE degrees p with appropriate weight shifts. The PBW spectral sequence has E₁^{p,q} where:
- p = PBW filtration degree (conformal weight)
- q = complementary degree
- Total bar degree = some function of p,q

For KM at E₁ collapse: bar cohomology H^n = H^n(g, Sym(g[t⁻¹])) where the CE cohomology uses the FULL coefficient module (not decomposed by weight).

**Key insight**: For simple g, only H^0 and H^{dim_g} survive (Whitehead). So:
```
H^0(g, Sym(g[t⁻¹]])) = [Sym(g[t⁻¹]])]^g = invariant ring
H^3(g, Sym(g[t⁻¹]])) = [Sym(g[t⁻¹]]) ⊗ Λ^3(g)]^g  (Poincaré duality)
```

For sl₂: the invariant ring of Sym(ad ⊗ t⁻¹k[t⁻¹]) has Hilbert series:
```
1/((1-q²)(1-q⁴)(1-q⁶)·...)  [invariants at each even weight, from Molien]
```

This gives the generating function for H^0 contributions. The H^3 contributions are related by Poincaré duality.

**But wait**: the bar complex is NOT simply CE(g, Sym(g[t⁻¹])). The bar complex has its OWN grading (bar degree = number of tensor factors). The PBW spectral sequence relates bar degree to CE degree + weight, but the relationship is:
- Bar degree n elements at weight h contribute to E₁^{p,q} where p + q = n
- The CE degree p ranges from 0 to dim(g) = 3

So bar cohomology at degree n receives contributions from:
- CE degree 0 at bar degree n: H^0(g, M_{n,0}) where M_{n,0} is a specific coefficient module
- CE degree 3 at bar degree n: H^3(g, M_{n,3}) by Poincaré duality

**Correct approach**: The bar complex of the loop algebra g((t)) has:
```
B^n = (g[t⁻¹]t⁻¹)^⊗n / (shuffle relations from OS)
```

The PBW filtration by total t-degree gives:
```
gr B^n = ⊕_h (weight-h part of (g[t⁻¹]t⁻¹)^⊗n / shuffles)
```

The d₀ differential is the CE part, acting on the g-indices while preserving mode structure.

**Implementation strategy**:
1. At weight h, enumerate the mode assignments: partitions of h into n parts ≥ 1, each colored by dim(g)
2. For each mode assignment, the CE differential acts on the g-indices
3. Compute kernel/image decomposition
4. Sum over weights to get total bar cohomology at degree n

This is computationally expensive but feasible for sl₂ (dim=3) at low degrees and weights.

**Verify**: Result should match Riordan numbers: H¹=3, H²=6, H³=15, H⁴=36

**Pitfalls**:
- DO NOT conflate bar degree with CE degree. They are different gradings.
- The coefficient module at each weight depends on the bar degree (different for B² vs B³).
- The OS shuffle relations reduce the chain group dimension from d^n to d^n·(n-1)!/n! — careful with the quotient.
- This is computationally the HARDEST item in the document. Start with n=1 (trivial: H¹=dim(g)=3) and n=2 before attempting n=3.

---

### M4. Full Bar Differential (Bracket + Curvature)

**What**: Build the complete bar differential d = d_bracket + d_curvature for KM algebras, where d_bracket uses the Lie bracket (simple pole) and d_curvature uses the Killing form (double pole). The sum satisfies d²=0.

**Where**: New module `compute/lib/km_bar_differential.py` or addition to existing `compute/lib/sl3_bar.py`

**How**: For a KM algebra ĝ_k with generators {Jᵃ} and OPE:
```
Jᵃ(z) Jᵇ(w) ~ kκ(a,b)/(z-w)² + f^{ab}_c Jᶜ(w)/(z-w)
```

The bar differential at degree n acts on B̄^n = g^⊗n ⊗ OS^{n-1}(C_n):

**d_bracket** (simple pole residue):
```
d_bracket([a₁|...|aₙ] ⊗ ω) = Σᵢ<ⱼ (-1)^{sign} [a₁|...|[aᵢ,aⱼ]|...|â_ⱼ|...|aₙ] ⊗ Res_{z_i=z_j}(ω)
```

**d_curvature** (double pole residue):
```
d_curvature([a₁|...|aₙ] ⊗ ω) = Σᵢ<ⱼ (-1)^{sign} k·κ(aᵢ,aⱼ) [a₁|...|â_ᵢ|...|â_ⱼ|...|aₙ] ⊗ Res²_{z_i=z_j}(ω)
```

where Res² is the double-pole residue on the OS form.

**Key mathematical fact** (prop:pole-decomposition in bar_cobar_construction.tex):
```
d² = d_bracket² + {d_bracket, d_curvature} + d_curvature² = 0
```
with d_curvature² = 0 (curvature produces scalars, no further residue), and the cross term compensates d_bracket² ≠ 0.

**For the ASSOCIATIVE bar complex** (no OS forms, adjacent pairs only):
```
d_bracket([a₁|...|aₙ]) = Σᵢ (-1)^i [a₁|...|[aᵢ,aᵢ₊₁]|...|aₙ]
d_curvature([a₁|...|aₙ]) = Σᵢ (-1)^i k·κ(aᵢ,aᵢ₊₁) [a₁|...|â_ᵢ|â_{ᵢ₊₁}|...|aₙ]
```

This is simpler (adjacent pairs only, no OS forms) and d²=0 follows from Jacobi + κ-invariance.

**Implementation plan**:
1. Start with the ASSOCIATIVE bar complex (adjacent pairs, no OS). Build d = d_bracket + d_curvature.
2. Verify d²=0 for sl₂ at degrees 2,3,4.
3. Compute rank and cohomology.
4. If this works, extend to the CHIRAL bar complex (all pairs, with OS forms).

**Verify**:
- d²=0 at each degree (CRITICAL — if this fails, signs are wrong)
- For sl₂ degree 2→1: d maps 9-dim → 3-dim. The curvature term maps to scalars (1-dim).
- Already have explicit bar differential matrices in `chiral_bar.py` (CEComplex class handles the CE part; `sl2_assoc_bar_diff_2to1` handles degree 2→1 of the associative bar)

**Pitfalls**:
- **THIS IS THE ITEM THAT BROKE THE ARCHIVED CODE**. The archived `bar_differential.py` and `bar_differential_v2.py` both failed because they implemented ONLY d_bracket without d_curvature. Do NOT repeat this mistake.
- d_curvature maps B̄^n → B̄^{n-1} (removes 2 generators, inserts scalar) which changes the tensor product structure. The target space at degree n-1 is NOT the same as the source space minus two slots — the OS form changes too.
- For the associative bar (adjacent pairs), d_curvature removes two ADJACENT generators and shortens the chain. This is well-defined. For the chiral bar (all pairs), d_curvature removes ANY pair, which interacts with the OS form in a more complex way.
- The level k appears as a PARAMETER in d_curvature. Bar cohomology should be level-independent at generic k (proved in manuscript). Verify this computationally by checking rank is constant in k.
- Use sympy exact arithmetic, NOT numpy. The archived numpy code had floating-point rank issues.

---

### M5. sl₃ Bar Cohomology from E₁ Page

**What**: Compute H^n(B̄(ŝl₃)) for n=1,2,3,4 using the PBW spectral sequence (building on M1-M3).

**Where**: Extension of M3's approach to dim_g = 8.

**How**: Same algorithm as M3 but with sl₃ (8 generators). Computationally more expensive:
- Weight 1: M₁ = g = 8-dim, CE(sl₃, ad) is C^0=8, C^1=56, ..., C^8=1
- Weight 2: M₂ = 8+36=44 dim (8 at mode -2, Sym²(8) at modes -1,-1)

**Verify**: Should match known values: H¹=8, H²=36, H³=204. Would compute H⁴ (currently unknown — conjectured 1352 from GF).

**Pitfalls**:
- The chain group at degree 4 has dim 24,576. The CE complex at each weight will be smaller (weight decomposition helps), but individual blocks can still be large.
- sl₃ has exponents [1,2], so H*(sl₃,k) = Λ(x₃,x₅) with dims [1,0,0,1,0,1,0,0,1,...]. The CE complex is 8-dimensional (not 3 like sl₂).
- Use the weight decomposition from `compute/scripts/sl3_modular_rank.py` (lines 43-63, WEIGHTS dict) to decompose into smaller blocks.

---

### M6. Virasoro d₁ Differential

**What**: For Virasoro (non-KM), the PBW spectral sequence collapses at E₂, not E₁. Computing E₂ requires building the d₁ differential on the E₁ page and taking its cohomology.

**Where**: New function in `compute/lib/spectral_sequence.py`

**How**: The Virasoro algebra has one generator T of weight 2. The bar complex has:
```
B̄^n: elements [T_{-m₁}|...|T_{-mₙ}] with mᵢ ≥ 2 (weight of T is 2)
```

The PBW-associated graded has d₀ = 0 (Virasoro is not KM, the "bracket" part is the Lie bracket of Witt algebra which is already filtered). The E₁ page is the chain complex itself, and d₁ is the first nontrivial differential.

For Virasoro, the spectral sequence is:
- E₀ = gr B̄(Vir)
- d₀ comes from the Witt bracket [Lₘ, Lₙ] = (m-n)L_{m+n}
- E₁ = H(E₀, d₀) = Lie algebra cohomology of Witt with coefficients
- d₁ comes from the central extension (the c-dependent term)
- E₂ = H(E₁, d₁) = bar cohomology

**Key**: The central extension contributes at d₁ level. This is why Virasoro collapses at E₂ (one step later than KM).

**Verify**: E₂ should give Motzkin differences: 1, 2, 5, 12, 30, ...

**Pitfalls**:
- The Witt algebra is infinite-dimensional. Must truncate by conformal weight.
- CE cohomology of Witt is NOT the same as CE of a finite-dimensional Lie algebra — Witt has infinitely many generators. At fixed weight, the contribution is finite.
- The central extension piece (the c/12 · m(m²-1) term in [Lₘ, L₋ₘ]) is what generates d₁. Missing this gives E₁ collapse (wrong).

---

### M7. sl₃ H⁴ via Modular Rank (Full Differential)

**What**: Use M4's full bar differential (bracket + curvature) to compute H⁴(B̄(ŝl₃)) directly. This is the Programme IX target.

**Where**: Extension of `compute/scripts/sl3_modular_rank.py` with curvature terms added.

**How**:
1. Build d₃→₂: B̄³ → B̄² using bracket + curvature (matrix: 64 × 512 for associative bar, or 384 × 3072 with OS)
2. Build d₄→₃: B̄⁴ → B̄³ similarly
3. H⁴ = ker(d₄→₃) / im(d₃→₂... wait, wrong direction)

Actually in cohomological grading (|d|=+1): d: B̄ⁿ → B̄ⁿ⁺¹. So:
- d₃: B̄³ → B̄⁴ and d₂: B̄² → B̄³
- H³ = ker(d₃)/im(d₂)
- H⁴ = ker(d₄)/im(d₃)

Wait — the bar complex has the DESUSPENSION grading. Need to be precise:
- B̄ⁿ has bar degree n (n tensor factors)
- The differential d: B̄ⁿ → B̄ⁿ⁻¹ (reduces number of factors)
- In homological grading: |d| = -1
- In the monograph's cohomological convention: reindex as B̄ₙ = B̄^{-n}, so |d| = +1

For computing H^n: need d_{n+1}: B̄^{n+1} → B̄^n and d_n: B̄^n → B̄^{n-1}
Then H^n = ker(d_n) / im(d_{n+1}).

**Weight decomposition**: Decompose by root weight (as in `sl3_modular_rank.py`). Compute rank of each block. Sum ranks over blocks to get total rank. Cohomology dim = chain dim - rank(d_n) - rank(d_{n+1}).

**Verify**: H¹=8, H²=36, H³=204 must match known values. H⁴ is the unknown target (conjectured 1352).

**Pitfalls**:
- The sl₃ chain group at degree 4 is 8⁴·3! = 24,576 for the chiral bar, or 8⁴ = 4096 for the associative bar. Even with weight decomposition, some blocks are large.
- Use modular arithmetic (rank over F_p) for speed, then verify p-independence.
- The curvature term has level k as parameter. Must verify k-independence of cohomology rank.
- M4 must succeed first (d²=0 verified). Do NOT attempt M7 without M4.

---

### M8. W₃ H⁵ Verification

**What**: The W₃ bar cohomology has values [2, 5, 16, 52, 171?, ...]. H⁵=171 comes from the conjectured rational GF recurrence a(n) = 3a(n-1) + a(n-2) - 1. Verify or refute this value.

**Where**: `compute/lib/bar_complex.py:313-315` (current H⁴=52 lookup), `compute/lib/bar_gf_solver.py`

**How**: W₃ has 2 generators (T of weight 2, W of weight 3). The bar complex is more complex than KM because:
- Multiple pole orders: T×T has pole 4, T×W has pole 3, W×W has pole 6
- Composite fields: Λ = :TT: - (3/10)∂²T appears
- The PBW filtration is by conformal weight but the OPE structure is non-linear

Two approaches:
1. **Direct computation** (requires M4 generalized to non-KM): Build the full bar differential including all pole orders. Extremely difficult.
2. **GF analysis**: Use the 4 known values to constrain the generating function more tightly. The current depth-2 recurrence with constant is the unique such fit, but depth-3 or algebraic degree-2 GFs are also possible. Getting a 5th data point from any source would distinguish.

**Verify**: Any independently computed H⁵ value that differs from 171 refutes the rational GF conjecture. Agreement would be evidence (but not proof).

**Pitfalls**:
- H⁴(W₃)=52 itself has no documented derivation (see M11). If 52 is wrong, everything downstream is wrong.
- W₃ composite fields break PBW enumeration — the chain group dimension formula from `w3_bar.py` must account for Λ as a composite, not an independent generator.
- The W₃ generating function may NOT be rational (could be algebraic or transcendental). The recurrence ansatz assumes rationality.

---

### M9. Koszul Relation Verification Engine

**What**: Build an automated checker for the Koszul relation H_A(t) · H_{A!}(-t) = 1 using known bar cohomology data for all algebras in the registry.

**Where**: Extension of `compute/lib/koszul_hilbert.py:verify_koszul()`

**How**: For each algebra A with known bar cohomology and known Koszul dual A!:
1. Look up H^n(B̄(A)) = bar cohomology dims
2. Look up H^n(B̄(A!)) = Koszul dual bar cohomology dims
3. Check the product H_A(t) · H_{A!}(-t) = 1 + O(t^{N+1}) where N is the number of known terms

For self-dual algebras (sl₂, sl₃): A! = A at dual level, same bar cohomology sequence. So check H(t) · H(-t) = 1.

```python
def verify_koszul_for_algebra(algebra: str) -> Dict[str, object]:
    """Check Koszul relation using all known bar cohomology data."""
```

**Verify**: sl₂ Riordan GF satisfies P(x)·P(-x) ≠ 1 because sl₂ is NOT self-Koszul in the usual sense — it's self-dual with a level shift. The Koszul relation is between H_{ŝl₂_k}(t) and H_{ŝl₂_{-k-4}}(t), which have the SAME graded structure (level-independent at generic k). So the check is H(t)·H(-t) = 1 where H is the Riordan GF. Actually verify this identity:
```
R(x)·R(-x) where R(x) = Σ R(n+3) x^n
```

**Pitfalls**:
- The Koszul relation is between the ALGEBRA and its DUAL, not the algebra with itself. For self-dual algebras, A! ≅ A (up to regrading), but the isomorphism may involve a sign change.
- For βγ/bc pair: H_{βγ}(t) · H_{bc}(-t) should equal 1. This is a nontrivial cross-check between two different bar cohomology sequences.
- Truncation: with only N known terms, can only verify the first N coefficients of the product.

---

### M10. βγ Koszul Inversion Check

**What**: Verify that the βγ and bc bar cohomology sequences satisfy the Koszul inversion formula. This is a nontrivial cross-check: βγ has GF sqrt((1+x)/(1-3x)), bc has 2^n - n + 1.

**Where**: `compute/lib/bar_complex.py` (KNOWN_BAR_DIMS for both), `compute/lib/koszul_hilbert.py`

**How**:
```python
h_bg = [KNOWN_BAR_DIMS["beta_gamma"][n] for n in range(1, 11)]
h_bc = [KNOWN_BAR_DIMS["bc"][n] for n in range(1, 11)]
# Prepend h_0 = 1 for both
h_bg = [1] + h_bg
h_bc = [1] + h_bc
assert verify_koszul(h_bg, h_bc)
```

**Verify**: Product coefficients should be [1, 0, 0, 0, ...] through 10 terms.

**Pitfalls**:
- The bar cohomology at degree 0 is 1 (the ground field), which must be prepended.
- βγ is Com-type (bosonic), bc is Lie-type (fermionic). The Koszul relation involves (-1)^j factors that account for the sign change.

---

### M11. W₃ H⁴=52 Provenance Investigation

**What**: The value H⁴(B̄(W₃))=52 appears in the Master Table but has no documented derivation. Find or reconstruct the source computation.

**Where**: `compute/lib/bar_complex.py:396`, `chapters/examples/examples_summary.tex` (line ~329), `chapters/examples/w_algebras_deep.tex`

**How**:
1. Search session transcripts for when H⁴=52 was first introduced: `grep -r "52" compute/ --include="*.jsonl" | grep -i "w3\|W_3"`
2. Search the monograph for any computation yielding 52: `grep -rn "52" chapters/examples/w_algebras_deep.tex`
3. Check if 52 follows from any structural argument (e.g., Euler characteristic, generating function constraint)
4. Check the 4-point recurrence fit: is 52 the UNIQUE value making the depth-2 recurrence a(n)=3a(n-1)+a(n-2)-1 work? (Answer: yes, but this is circular — the recurrence was FIT to the 4 values including 52.)

**Verify**: Either find the derivation (promoting 52 from CONJECTURAL to PROVED) or explicitly document it as unverifiable (and add a warning to the Master Table).

**Pitfalls**:
- Do NOT assume 52 is correct just because it's in the table. The table was populated incrementally and some values may have been transcription errors.
- The session transcript search will be slow (large .jsonl files). Use narrow patterns.
- If 52 turns out to be wrong, the W₃ GF conjecture (and H⁵=171 prediction) are also wrong.

---

## TIER 3: Testing and Verification

### T1. Deeper Property-Based Tests

**What**: Extend `test_koszul_properties.py` with additional mathematical properties that should hold universally.

**Where**: `compute/tests/test_koszul_properties.py` (currently 95 tests)

**Properties to add**:
1. **Sugawara central charge symmetry**: c(k) · c(k') is level-independent for each Lie type (actually it's NOT constant — c(k)+c(k') is the complementarity sum, but c(k)·c(k') varies). Check the correct identity.
2. **Bar chain group factorial growth**: dim B̄ⁿ(g) = dim(g)ⁿ · (n-1)! for all KM, for n=1,...,5
3. **OS dimension identity**: dim OS^{n-1}(Cₙ) = (n-1)! for all n=2,...,8
4. **Partition function monotonicity**: p(n) ≤ p(n+1) for all n
5. **Catalan convolution**: C_n = Σ_{k=0}^{n-1} C_k · C_{n-1-k} (already in test_mathematical_identities.py but parametrize over wider range)
6. **Discriminant identity**: (1-3x)(1+x) = 1-2x-3x² for all x (trivial but documents the shared discriminant)
7. **Associahedron h-vector = Narayana**: h_k(K_n) = N(n-1, k+1) for all k,n

**Verify**: Each new test should pass on first run.

**Pitfalls**:
- Property 1 (Sugawara symmetry) needs careful formulation. The correct identity is κ(A)+κ(A!)=0, which is already tested. The c+c'=const identity involves central charges, not kappa.
- Do not add tests that duplicate existing ones in `test_mathematical_identities.py`.

---

### T2. Regression Test Harness for Conjectural Values

**What**: Create a clearly separated test suite for CONJECTURAL values (currently mixed with proved values). When a conjectural value is promoted to proved, move the test.

**Where**: New file `compute/tests/test_conjectural.py`

**Tests to include**:
```python
# W₃ bar cohomology degree 4 (CONJECTURAL)
def test_w3_h4_conjectural():
    assert KNOWN_BAR_DIMS["W3"][4] == 52  # Provenance: unknown

# W₃ GF recurrence prediction (CONJECTURAL)
def test_w3_h5_prediction():
    # a(n) = 3a(n-1) + a(n-2) - 1
    assert bar_dim_w3_conjectured(5) == 171

# sl₃ bar cohomology degree 4 (CONJECTURAL via GF)
def test_sl3_h4_conjectural():
    assert bar_dim_sl3_conjectured(4) == 1352

# Yangian bar cohomology (CONJECTURAL: 3^n + 1)
def test_yangian_h4_conjectural():
    assert yangian_bar_cohomology_conjectured(4) == 82
```

**Verify**: All conjectural tests pass. They are marked with `@pytest.mark.conjectural` so they can be run or skipped separately.

**Pitfalls**:
- Do NOT put conjectural tests in the main test suite without clear markers. A failing conjectural test should not break CI.
- The conjectural marker requires `conftest.py` to register the mark: `def pytest_configure(config): config.addinivalue_line("markers", "conjectural: conjectural values")`

---

### T3. Cross-Module Smoke Tests

**What**: Verify that every public function in `compute/lib/__init__.py` can be called without error with minimal inputs. Currently `__init__.py` exports 19 symbols but only some are exercised by tests.

**Where**: New file `compute/tests/test_smoke.py` or extend existing tests

**How**: For each exported function, call it with the simplest valid arguments and assert the result is not None / not empty.

```python
def test_smoke_all_exports():
    from compute.lib import (
        GradedVectorSpace, ChainComplex, OPEAlgebra, Generator,
        heisenberg_algebra, sl2_algebra, virasoro_algebra, free_fermion_algebra,
        cartan_data, sugawara_c, ff_dual_level, kappa_km,
        ALGEBRA_REGISTRY, KNOWN_BAR_DIMS, verify_bar_dim,
        quadratic_dual_dims, verify_koszul, riordan, motzkin,
        os_dimension, os_basis, residue_map,
        partition_number, lambda_fp, F_g,
    )
    # Each function produces a non-trivial result
    assert cartan_data("A", 1).dim == 3
    assert riordan(5) == 6
    assert motzkin(4) == 9
    assert os_dimension(3, 2) == 2
    assert partition_number(5) == 7
    # ...etc
```

**Verify**: `python -m pytest compute/tests/test_smoke.py -v` all pass

---

## TIER 4: Deep Mathematical Research (open problems)

### R1. Virasoro Koszul Dual Identification

**What**: Identify the Koszul dual of the Virasoro algebra. Currently listed as "conjectured W_infinity-related" in `ALGEBRA_REGISTRY`. This is a genuinely open mathematical problem.

**Status**: The monograph lists this as one of 7 genuinely open problems (CLAUDE.md: "Virasoro/W_infinity Koszul dual (3)").

**What the engine can contribute**: If the dual were identified, its bar cohomology generating function H!(t) would satisfy H(t)·H!(-t) = 1 where H(t) is the Motzkin difference GF. This gives a constraint on the dual's Hilbert series. The Motzkin difference GF is:
```
H(t) = (1 - t - √((1-3t)(1+t))) / (2t²)
```
So H!(t) = 1/(H(-t)) which can be computed to arbitrary order and examined for patterns.

---

### R2. Chiral Bar Differential Sign Resolution

**What**: Resolve the sign conventions for the chiral bar differential with OS forms such that d²=0 for the full differential (bracket + curvature + all pole orders).

**Status**: The archived code (`bar_differential.py`, `bar_differential_v2.py`, `chiral_bar_differential.py`) all have d²≠0. The problem is NOT that d²≠0 is a mathematical fact — it's that the sign conventions for the OS form residues have not been correctly implemented.

**What the engine can contribute**: The OS algebra module (`os_algebra.py`) correctly computes OS dimensions and Arnold relations. The CE complex (`chiral_bar.py`, CEComplex class) correctly implements the Lie bracket part with d²=0. What's missing is the correct sign rule for composing residues on OS forms when applying the bar differential.

**Approach**: Study the `chiral_bar_differential.py` (archived, 1603 lines) to understand exactly where d²≠0 appears, then compare with the manuscript's Proposition prop:pole-decomposition to identify the sign error.

---

### R3. Reflected Modular Periodicity

**What**: The KM bar cohomology at rank 1 (sl₂) shows 4-periodicity (period = 2h = 4). At higher rank, the periodicity structure is more complex. The manuscript conjectures "reflected modular periodicity" — a duality between bar cohomology at weights h and 2h-h for each Coxeter orbit.

**Status**: Listed as genuinely open (2 conjectures in koszul_pair_structure.tex).

**What the engine can contribute**: If M5 succeeds (sl₃ bar from E₁), the weight-decomposed bar cohomology data would directly test the periodicity conjecture.

---

## Execution Notes

### Session Strategy

Each session should pick ONE item from TIER 1-2 and drive it to completion (all tests passing). The items are ordered by dependency within each tier. Recommended sequence:

1. **E1** (script cleanup) — fast, reduces cognitive load for future sessions
2. **E2** (name normalization) — fast, eliminates a recurring source of bugs
3. **M1** (adjoint invariants) — unlocks M3 and M5
4. **M4** (full bar differential) — unlocks M7 and (potentially) R2
5. **M2** (CE with coefficients) — unlocks M3
6. **M3** (sl₂ bar from E₁) — the first genuine derivation of Riordan numbers from the PBW approach
7. **M9 + M10** (Koszul relation checks) — purely computational, uses existing data

### Verification Protocol

After each item:
1. Run `python -m pytest compute/tests/ -q` — all tests must pass
2. Run `python -m pytest compute/tests/ -q --co | tail -1` — count should only increase
3. If new functions added to lib, add them to `__init__.py` and verify import: `python -c "from compute.lib import new_function"`

### Known Cognitive Pitfalls

1. **The Wrong Tree**: Do NOT attempt to build the chiral bar differential using bracket-only d. This has been tried (2048 sign conventions, all fail). The full differential needs bracket + curvature.
2. **Coalgebra vs Algebra**: `quadratic_dual_dims()` computes the Koszul dual COALGEBRA (subcoalgebra of cofree), not the dual ALGEBRA (quotient of free). Their dimensions differ. The coalgebra is what appears in the bar construction.
3. **Bar Degree vs CE Degree**: In the PBW spectral sequence, bar degree n involves CE degrees 0 through dim(g). They are NOT the same grading. Each bar degree n element contributes to multiple CE degrees.
4. **Chain vs Cohomology**: KNOWN_BAR_DIMS stores bar COHOMOLOGY H^n(B̄). Chain group dimensions are much larger: dim(g)^n · (n-1)!. Do not confuse them.
5. **Name Collisions**: "beta_gamma" vs "betagamma", "Heisenberg" vs "heisenberg". Always check which convention a module uses before writing cross-module code.
6. **Level Independence**: Bar cohomology dims are level-independent at generic k (proved). If a computation gives k-dependent results, something is wrong.
7. **Circular Koszulness**: Do not assume Koszulness to prove bar cohomology formulas that are then used to verify Koszulness. The standalone proof chain is: PBW flatness (thm:pbw-koszulness-criterion) + classical Koszulness of associated graded (Priddy) → chiral Koszulness.
