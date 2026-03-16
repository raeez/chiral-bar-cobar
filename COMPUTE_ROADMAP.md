# COMPUTE ROADMAP — Volume II Verification Infrastructure

**Purpose**: Detailed specification of every compute module that needs to exist,
with test specifications, priority ordering, and dependency on the proof programme.

**Governing principle**: Every test must verify something MATHEMATICAL, not just
"code runs." The Virasoro `return S.Zero` and LG `pass` stubs are not tests.

**Test tiers** (from Vol I audit methodology):
- **Tier 1 (structural)**: d²=0, Jacobi, associativity — self-certifying identities
- **Tier 2 (published)**: known values from Kac, BPZ, DSK, etc.
- **Tier 3 (cross-check)**: two independent code paths agree
- **Tier 4 (regression)**: "whatever code produced" — AVOID

**Last updated**: March 13, 2026

---

## Current State (updated March 13, 2026)

### Module inventory

| Module | File | Status | Tests |
|--------|------|--------|-------|
| ainfty.py | lib/ainfty.py | **Complete** | 6 sesqui + sign/identity |
| pva.py | lib/pva.py | **Complete** | Jacobi + Leibniz + commutativity + skew |
| spectral.py | lib/spectral.py | **Complete** | Laurent arithmetic + symmetrize |
| free_multiplet.py | lib/examples/free_multiplet.py | **Complete** | 4 |
| lg_cubic.py | lib/examples/lg_cubic.py | **Complete** | 14 (Q^2, m_k, truncation) |
| virasoro.py | lib/examples/virasoro.py | **Complete** | 10 (real Jacobi, sesqui, components) |
| abelian_cs.py | lib/examples/abelian_cs.py | Complete (trivial) | 5 |
| nonabelian_cs.py | lib/examples/nonabelian_cs.py | **Complete** | 8 (all 27 Jacobi, Sugawara) |
| convention_check.py | lib/convention_check.py | **Complete** | 22 (LV=(-1)^{i-1}*Koszul) |
| laplace_bridge.py | lib/laplace_bridge.py | **Complete** | 9 (BR3 abelian/Vir/su2, roundtrip) |
| fm_boundary.py | lib/fm_boundary.py | **Complete** | 10 (strata, signs, corners) |
| arnold.py | lib/arnold.py | **Complete** | 12 (partial fractions, exterior, AOS) |

### Test suite
- **133 tests total**, all passing (up from 38 initial)
- **~80% genuine** (Tier 1-2): Real Jacobi, sesquilinearity, BR3, Arnold relations, sign conventions
- **~20% structural/trivial**: free theory, abelian CS, scaffolding
- **Zero stubs remaining**: no `pass`, no `return S.Zero` for Jacobi

### Resolved deficiencies
1. ~~No genuine Jacobi test~~ **RESOLVED**: Virasoro (symbolic), su(2) (all 27 triples), PVA checker
2. ~~LG cubic = zero computation~~ **RESOLVED**: m_1 Q^2=0, m_2 product, m_3 cubic vertex, m_{k>=4}=0
3. ~~No PVA axiom verification~~ **RESOLVED**: PVAChecker with Jacobi + Leibniz, tested on su(2)
4. ~~No FM calculus~~ **RESOLVED**: fm_boundary.py + arnold.py (strata, signs, AOS cancellations)
5. No brace/Hochschild computation (not yet needed for current claims)
6. ~~No R-matrix beyond abelian~~ **PARTIALLY RESOLVED**: su(2) r-matrix via Laplace bridge

### Remaining gaps (Phase 4-5)
- **W_3 module** (lib/examples/w3.py) — composite field Jacobi, highest-effort remaining item
- **Homotopy transfer** (lib/homotopy_transfer.py) — HPL for A-infinity transfer
- **Spectral substitution** (lib/spectral_substitution.py) — block fusion for compositions
- **Brace/Hochschild** — not yet scoped

---

## Phase 1: Critical Fixes (blocks paper credibility)

### 1.1 LG Cubic m₁ Implementation

**File**: `lib/examples/lg_cubic.py` → `m1_lg`

**Specification**:
```python
def m1_lg(field_value, field_type, g):
    """BV-BRST differential for LG model W = g*phi³/3.

    Q = dbar + g*phi²*(∂/∂psi)

    On the polynomial ring:
      Q(phi_n) = psi_n          (same as free theory)
      Q(psi_n) = g * (phi²)_n  (deformation by W'(phi) = g*phi²)

    Q² check:
      Q²(phi) = Q(psi) = g*phi²    (NOT zero!)
      Q²(psi) = Q(g*phi²) = 2g*phi*psi  (NOT zero!)

    WAIT — this means Q² ≠ 0, so Q is a CURVED differential.
    Actually: Q = dbar is the free differential. The interaction W
    enters through m₂, not m₁. So:
      m₁ = Q_free: Q(phi)=psi, Q(psi)=0, Q²=0.

    The superpotential deforms m₂ and creates m₃, not m₁.
    Reference: CLAUDE.md curved A∞ — m₁²(a) = [m₀, a], but here m₀ = 0
    (uncurved), so m₁² = 0.

    CRITICAL CHECK: Is the LG A∞ structure curved or uncurved?
    - On C×R with W = g*phi³/3, the BV-BRST differential IS Q_free.
    - The superpotential enters as a DEFORMATION of the propagator and vertices.
    - At the A∞ level: m₁ = Q_free, m₂ = free product + g-correction, m₃ ~ g.
    - NO curvature (m₀ = 0) because W is a polynomial (no vacuum energy).
    """
```

**Tests** (Tier 1):
- `test_lg_m1_Q_squared`: Q²(phi) = 0, Q²(psi) = 0
- `test_lg_m1_degree`: |m₁| = 0 (differential has degree 0 in our conventions)

### 1.2 LG Cubic m₂ Implementation

**File**: `lib/examples/lg_cubic.py` → `m2_lg`

**Specification**:
The binary operation has reg + sing parts:
- m₂^reg(phi,phi;λ) = phi·phi (commutative product, zeroth order in g)
  + g-correction (first order in g, from one propagator with W''-vertex)
- m₂^sing(phi,phi;λ) = 0 at zeroth order
  + g²-correction (from Feynman diagram with two W''-vertices and propagator)

**Physical origin**: The m₂ operation is the time-ordered product T₂(a₁,a₂).
For the free theory, this is the normal-ordered product (regular) plus the
propagator contraction (singular = simple pole). For LG, the propagator is
dressed by the interaction W, producing corrections at each order in g.

**Implementation strategy**:
Work to first order in g (linear deformation of the free m₂).
At O(g⁰): m₂ = free product (already implemented in free_multiplet.py).
At O(g¹): need one cubic vertex W''' = 2g connecting two of the three
lines (two inputs + one output). The Feynman diagram gives a correction
proportional to g.

**Tests** (Tiers 1-2):
- `test_lg_m2_reduces_to_free`: at g=0, m₂ = free product
- `test_lg_m2_reg_commutative`: m₂^reg(a,b;0) = m₂^reg(b,a;0)
- `test_lg_m2_sesquilinearity`: m₂(∂a,b;λ) = −λ·m₂(a,b;λ)

### 1.3 LG Cubic m₃ Implementation

**File**: `lib/examples/lg_cubic.py` → `m3_lg`

**Specification**:
m₃(a₁,a₂,a₃;λ₁,λ₂) arises from the cubic vertex W''' = 2g with one propagator.

**Feynman diagram**:
```
a₁ ──┐
      │── vertex (W'''=2g) ── propagator K ── output
a₂ ──┘                                    │
a₃ ────────────────────────────────────────┘
```
Wait — this isn't quite right. The tree diagram for m₃ with one cubic vertex has:
- 3 inputs (a₁, a₂, a₃)
- 1 vertex (trivalent)
- 0 internal edges (the vertex directly connects all 3)

So m₃ ~ W''' = 2g · (some integral over FM₃(C)).

**Tests** (Tier 1):
- `test_lg_m3_proportional_to_g`: m₃ at g=0 should be 0
- `test_lg_m3_koszul_sign`: verify the sign convention matches A∞ identity
- `test_lg_m3_ainfty_identity`: the n=3 A∞ identity should hold

### 1.4 LG Truncation Verification

**File**: `lib/examples/lg_cubic.py` → `check_truncation_degree_counting`

**Specification**:
Current implementation only returns vertex/edge counts. Need:
1. Complete the ghost number budget with holomorphic/topological split
2. Show that for k≥4, the total degree of the Feynman integral does not
   match |m_k| = 1−k
3. The argument should work for ANY cubic W, not just phi³

**Tests** (Tier 2):
- `test_lg_m4_zero_degree_counting`: ghost + form degree mismatch for k=4
- `test_lg_m5_zero`: similar for k=5

### 1.5 Real Virasoro Jacobi

**File**: `lib/examples/virasoro.py` → `check_virasoro_jacobi`

**Specification**:
Replace `return S.Zero` with actual computation.

**Method**: Use the Lie conformal algebra n-product formulation.
The n-products are: T₀T = ∂T, T₁T = 2T, T₃T = c/2.
The Jacobi identity for Lie conformal algebras (Kac, Thm 2.7) states:

[a_λ [b_μ c]] − [b_μ [a_λ c]] = [[a_λ b]_{λ+μ} c]

For a=b=c=T, expand each side using the n-product formulation:
{T_λ {T_μ T}} = {T_λ (∂T + 2Tμ + c/12·μ³)}

Use sesquilinearity:
{T_λ ∂T} = (λ+∂){T_λ T} = (λ+∂)(∂T + 2Tλ + c/12·λ³)
           = λ·∂T + ∂²T + 2∂T·λ + 2T·λ² + c/12·λ⁴

And {T_λ 2Tμ} = 2μ·{T_λ T} = 2μ(∂T + 2Tλ + c/12·λ³)

And {T_λ c/12·μ³} = 0 (constant)

So the full LHS term 1 involves:
- Quadratic terms in T (from {T_λ T} iterated)
- Quartic terms in λ,μ (from the c/12 pieces)
- ∂²T, ∂T·λ, T·λ², T·λμ, T·μ² terms

Similarly compute LHS term 2 and RHS, then verify cancellation.

**Implementation**:
```python
def check_virasoro_jacobi_real(lam, mu, c):
    """REAL Jacobi check for Virasoro, not `return S.Zero`."""
    T, dT, d2T, d3T = symbols('T dT d2T d3T')

    # {T_lam T} = dT + 2*T*lam + c/12*lam^3
    def bracket(l):
        return dT + 2*T*l + Rational(1,12)*c*l**3

    # {T_lam dT} = (lam + partial) {T_lam T}
    # partial acts: partial(dT)=d2T, partial(T)=dT, partial(const)=0
    def bracket_dT(l):
        # (l + partial)(dT + 2*T*l + c/12*l^3)
        # = l*dT + l*2*T*l + l*c/12*l^3 + d2T + 2*dT*l + 0
        return l*dT + 2*T*l**2 + Rational(1,12)*c*l**4 + d2T + 2*dT*l

    # LHS term 1: {T_lam {T_mu T}} = {T_lam (dT + 2*T*mu + c/12*mu^3)}
    # = {T_lam dT} + 2*mu*{T_lam T} + 0
    term1 = bracket_dT(lam) + 2*mu*bracket(lam)

    # LHS term 2: -{T_mu {T_lam T}} = -({T_mu dT} + 2*lam*{T_mu T})
    term2 = -(bracket_dT(mu) + 2*lam*bracket(mu))

    # RHS: {{T_lam T}_{lam+mu} T}
    # {T_lam T} = dT + 2*T*lam + c/12*lam^3
    # We need {(dT + 2*T*lam + c/12*lam^3)_{lam+mu} T}
    # By sesquilinearity: {dT_nu T} = -(nu) * {T_nu T} (LEFT sesquilinearity: partial on first arg)
    # Wait — actually {dT_nu T} uses skew-symmetry or direct computation.
    #
    # For the Virasoro LCA: {f(T)_nu T} requires the Leibniz/sesquilinearity rules.
    # {dT_nu T} = -(d+nu) {T_nu T}  ... no, this is the RIGHT sesquilinearity.
    #
    # Actually: LEFT sesquilinearity gives {partial(a)_nu b} = -nu {a_nu b}
    # So {dT_nu T} = -nu * {T_nu T} = -nu * (dT + 2*T*nu + c/12*nu^3)
    nu = lam + mu
    rhs_from_dT = -nu * bracket(nu)  # from {dT_{lam+mu} T} = -(lam+mu)*{T_{lam+mu} T}
    rhs_from_2Tlam = 2*lam * bracket(nu)  # from {2*T*lam_{lam+mu} T} = 2*lam*{T_{lam+mu} T}
    rhs_from_const = 0  # {const_{nu} T} = 0
    rhs = rhs_from_dT + rhs_from_2Tlam + rhs_from_const

    result = expand(term1 + term2 - rhs)
    return result  # Should be 0
```

**Tests** (Tier 1 — self-certifying):
- `test_virasoro_jacobi_real`: result == 0 for symbolic c
- `test_virasoro_jacobi_c1`: result == 0 for c=1 (free boson)
- `test_virasoro_jacobi_c26`: result == 0 for c=26 (bosonic string)

This is the **single highest-value test to implement**.

---

## Phase 2: PVA Axiom Verification Framework

### 2.1 Enhanced PVA Checker

**File**: `lib/pva.py` → extend `PVAChecker`

**What's missing**:
- `check_all()` only checks commutativity and skew-symmetry, not Jacobi or Leibniz
- `verify_jacobi()` exists as a standalone function but isn't integrated
- `verify_leibniz()` exists but isn't integrated
- No test calls these on any nontrivial example

**Enhancement**:
```python
class PVAChecker:
    def check_all(self, lam=None, mu=None):
        # ... existing commutativity and skew_symmetry ...

        # Jacobi (on generators)
        jacobi_results = []
        for a in self.generators:
            for b in self.generators:
                for c in self.generators:
                    diff = self._check_jacobi(a, b, c, lam, mu)
                    jacobi_results.append((a, b, c, diff))
        results['jacobi'] = jacobi_results

        # Leibniz (on generators)
        leibniz_results = []
        for a in self.generators:
            for b in self.generators:
                for c in self.generators:
                    diff = self._check_leibniz(a, b, c, lam)
                    leibniz_results.append((a, b, c, diff))
        results['leibniz'] = leibniz_results

        return results
```

**Tests** (Tier 1):
- `test_pva_checker_virasoro_all_axioms`: run full PVA check on Virasoro
- `test_pva_checker_abelian_cs_all_axioms`: run full PVA check on abelian CS
- `test_pva_checker_free_multiplet_all_axioms`: trivial (bracket = 0)

### 2.2 Sesquilinearity Verification

**File**: `lib/ainfty.py` → implement `verify_sesquilinearity_left/right`

**Current state**: Both functions are `pass` stubs.

**Specification**:
```python
def verify_sesquilinearity_left(m_k, elements, i, lambda_i):
    """Verify: m_k(..., partial(a_i), ...) = -lambda_i * m_k(..., a_i, ...)"""
    # For each element, apply partial to the i-th slot and compare with -lambda_i * original
    ...

def verify_sesquilinearity_right(m_k, elements, lambdas):
    """Verify: m_k(..., partial(a_k)) = (sum(lambdas) + partial) * m_k(...)"""
    ...
```

**Tests** (Tier 1-2):
- `test_sesquilinearity_left_virasoro`: {∂T_λ T} = −λ{T_λ T}
- `test_sesquilinearity_right_virasoro`: {T_λ ∂T} = (λ+∂){T_λ T}
- `test_sesquilinearity_left_abelian_cs`: {∂J_λ J} = −λ{J_λ J} = −kλ²
- `test_sesquilinearity_right_abelian_cs`: {J_λ ∂J} = (λ+∂){J_λ J} = kλ + k∂

### 2.3 LaurentSeries Enhancement

**File**: `lib/spectral.py` → complete `symmetrize`

**Current state**: `symmetrize` method is a `pass` stub.

**Specification**:
```python
def symmetrize(self, partial_symbol):
    """Compute (f(λ) + f(−λ−∂)) / 2 for extracting commutative product.

    For m₂(a,b;λ), the commutative product on cohomology is:
    a·b = (m₂(a,b;λ) + m₂(b,a;−λ−∂)) evaluated at λ=0.

    The ∂ acts as the translation operator on the second argument.
    """
```

---

## Phase 3: A∞ Identity Verification

### 3.1 Full A∞ Identity at Arity 3

**File**: `lib/ainfty.py` → extend `verify_ainfty_identity`

**Current state**: The function exists and works for scalar operations, but does
not handle spectral parameters (Laurent series valued operations).

**Enhancement needed**: Support m_k returning LaurentSeries objects, with spectral
substitution (block fusion) for nested compositions.

**The arity-3 identity** (n=3):
```
Σ_{i+j=4} Σ_s (−1)^ε m_i(..., m_j(...), ...) = 0
```
Expanding: m₁(m₃(a,b,c)) + m₃(m₁(a),b,c) + m₃(a,m₁(b),c) + m₃(a,b,m₁(c))
         + m₂(m₂(a,b),c) − m₂(a,m₂(b,c)) = 0

(The last two terms have spectral substitution for the spectral parameters.)

**Tests** (Tier 1):
- `test_ainfty_n3_free`: all m_{≥3}=0, reduces to m₂(m₂(a,b),c) = m₂(a,m₂(b,c)) (associativity)
- `test_ainfty_n3_lg_order_g0`: at g=0, LG = free, identity holds
- `test_ainfty_n3_lg_order_g1`: at O(g), m₃ term enters, verify cancellation

### 3.2 Spectral Substitution

**New file**: `lib/spectral_substitution.py`

**Purpose**: Implement the spectral substitution (block fusion) rule:
when m_j appears inside m_i, the spectral parameters of the inner block
are replaced by their sum.

**Specification**:
```python
def substitute_block(outer_series, inner_series, block_indices):
    """Apply spectral substitution for A∞ composition.

    When m_i(..., m_j(a_{s+1},...,a_{s+j}; inner_lambdas), ...; outer_lambdas),
    the inner spectral parameters are summed and replaced in the outer series.

    This is the "block fusion" rule from axioms.tex.
    """
```

---

## Phase 4: New Modules

### 4.1 FM Boundary Calculator

**New file**: `lib/fm_boundary.py`

**Purpose**: Compute boundary contributions from FM_k(C) for the Stokes
derivation of A∞ identities.

**Core functions**:
```python
def fm_boundary_strata(k):
    """Return all codimension-1 boundary strata of FM_k(C).

    Each stratum corresponds to a subset S ⊂ {1,...,k} with |S| ≥ 2
    colliding to a point. The stratum is FM_{|S|}(C) × FM_{k-|S|+1}(C).
    """

def boundary_integral_sign(k, S):
    """Compute the orientation sign for the boundary stratum D_S.

    The sign comes from the orientation of the normal bundle to D_S in FM_k(C).
    """

def stokes_identity(k, amplitude_fn):
    """Apply Stokes' theorem: ∫_{FM_k} dω = Σ_S ±∫_{D_S} Res_S(ω).

    For k=3: D_{12}, D_{23}, D_{13} give the three terms of the n=3 identity.
    """
```

**Tests** (Tier 1):
- `test_fm3_boundary_gives_3_strata`: |boundary_strata(3)| = 3
- `test_fm3_stokes_signs`: boundary signs compatible with A∞ signs
- `test_fm4_boundary_gives_7_strata`: C(4,2)−1 = 5... actually need to count correctly

### 4.2 Arnold Relations

**New file**: `lib/arnold.py`

**Purpose**: Verify Arnold-Orlik-Solomon cancellations at codimension-2 corners.

**Core functions**:
```python
def arnold_relation(i, j, k):
    """The Arnold relation: ω_{ij} ∧ ω_{jk} + ω_{jk} ∧ ω_{ki} + ω_{ki} ∧ ω_{ij} = 0.

    This is the fundamental relation in H*(Conf_n(C), Z).
    """

def aos_cancellation(k, S1, S2):
    """Verify that at the corner D_{S1} ∩ D_{S2}, the boundary contributions cancel.

    The cancellation follows from the Arnold relation applied to the
    three logarithmic forms ω_{ij} = d log(z_i - z_j).
    """
```

**Tests** (Tier 2 — published result):
- `test_arnold_3_points`: ω₁₂∧ω₂₃ + ω₂₃∧ω₃₁ + ω₃₁∧ω₁₂ = 0
- `test_aos_fm3_corners`: all codim-2 contributions cancel

### 4.3 Nonabelian Current Algebra

**New file**: `lib/examples/nonabelian_cs.py`

**Purpose**: SU(2) (and eventually general g) current algebra from nonabelian CS.

**Specification**:
```python
def su2_lambda_bracket(a, b, lam, k):
    """Lambda-bracket for su(2) current algebra at level k.

    {J^a_λ J^b} = f^{ab}_c J^c + k * κ^{ab} * λ

    where f^{ab}_c = structure constants and κ^{ab} = Killing form.
    """

def check_jacobi_su2(lam, mu, k):
    """Verify Jacobi for su(2)_k.

    This is the FIRST genuinely nontrivial Jacobi check.
    The abelian case is 0=0=0. The Virasoro case is classically known.
    The su(2) case involves structure constants and is a real computation.
    """
```

**Tests** (Tier 2 — published values):
- `test_su2_bracket_structure_constants`: f^{ab}_c = ε^{abc}
- `test_su2_jacobi`: full Jacobi identity (Tier 1)
- `test_su2_sugawara`: T = (1/2(k+2)) Σ :J^a J^a: gives correct c = 3k/(k+2)
- `test_su2_r_matrix_classical`: r(z) = Ω/z where Ω = Σ J^a ⊗ J^a

### 4.4 W₃ Operations

**New file**: `lib/examples/w3.py`

**Purpose**: W₃ algebra with generators T (weight 2) and W (weight 3).

**The OPE data** (published, Zamolodchikov):
- {T_λ T} = ∂T + 2Tλ + c/12·λ³
- {T_λ W} = ∂W + 3Wλ
- {W_λ W} = ∂Λ + 2Λλ + (c/3·5!)λ⁵ + (16/(22+5c))(∂³T/6 + T∂T·λ + T²λ² + ∂²T·λ²/2 + ∂T·λ³/2 + T·λ⁴/3)
  where Λ = :TT: − (3/10)∂²T (the composite field)

**Note on Λ**: CLAUDE.md says Λ = :TT: − (3/10)∂²T (MINUS sign). Verify this
matches the Vol I convention. Getting this sign wrong corrupts the entire W₃ computation.

**Tests** (Tiers 1-2):
- `test_w3_virasoro_subalgebra`: {T_λ T} = Virasoro (consistency)
- `test_w3_primary_W`: {T_λ W} = ∂W + 3Wλ (W is primary of weight 3)
- `test_w3_jacobi_TTT`: Virasoro sub-Jacobi (known)
- `test_w3_jacobi_TTW`: involves both Virasoro and primary field
- `test_w3_jacobi_TWW`: the first test using the composite Λ
- `test_w3_jacobi_WWW`: the hardest test — involves Λ explicitly
- `test_w3_lambda_sign`: Λ = :TT: − (3/10)∂²T (verify minus sign)

### 4.5 Homotopy Transfer

**New file**: `lib/homotopy_transfer.py`

**Purpose**: Implement the homological perturbation lemma (HPL) for A∞ algebras.

**Specification**:
Given an A∞ algebra (A, {m_k}) with a deformation retract (ι: H → A, π: A → H, h: A → A)
satisfying π∘ι = id, ι∘π − id = m₁∘h + h∘m₁, the HPL produces transferred operations
m_k^{tr} on H.

The formulas (Loday-Vallette §10.3):
- m₂^{tr}(a,b) = π ∘ m₂(ι(a), ι(b))
- m₃^{tr}(a,b,c) = π ∘ m₂(ι(a), h∘m₂(ι(b),ι(c))) ± π ∘ m₂(h∘m₂(ι(a),ι(b)), ι(c)) ± π ∘ m₃(ι(a),ι(b),ι(c))

**Tests** (Tier 1):
- `test_hpl_free_multiplet`: all m_k^{tr} = 0 for k≥3 (free theory = formal)
- `test_hpl_virasoro_m3`: m₃^{tr} on H•(Vir) — should be 0 if PVA descent is correct
- `test_hpl_preserves_ainfty`: transferred operations satisfy A∞ identity

---

## Phase 5: Cross-Volume Verification

### 5.1 Convention Comparison

**New file**: `lib/convention_check.py`

**Purpose**: Verify that Vol I and Vol II sign conventions are genuinely equivalent.

**Specification**:
```python
def lv_sign(r, s, t):
    """Loday-Vallette sign: (-1)^{rs+t}"""
    return (-1)**(r*s + t)

def koszul_sign(degrees_before, arity_inner):
    """Koszul sign: (-1)^{(j-1)(|a_1|+...+|a_s|)}"""
    return (-1)**((arity_inner - 1) * sum(degrees_before))

def compare_conventions(n, degrees):
    """For each term in the n-th A∞ identity, compare LV and Koszul signs.

    Returns True if they agree on all terms.
    """
```

**Tests** (Tier 1):
- `test_conventions_agree_n2`: n=2 identity (d²=0)
- `test_conventions_agree_n3`: n=3 identity (homotopy associativity)
- `test_conventions_agree_n4`: n=4 identity (where signs get interesting)
- `test_conventions_agree_n5`: n=5 (thorough)

### 5.2 Laplace Transform Bridge

**New file**: `lib/laplace_bridge.py`

**Purpose**: Verify BR3 (r(z) = Laplace of λ-bracket) for worked examples.

**Specification**:
```python
def laplace_of_bracket(bracket_fn, z):
    """Compute r(z) = Res_{λ=0} e^{-λz} {a_λ b}.

    For polynomial λ-brackets (Virasoro, abelian CS), this is finite.
    """

def verify_br3_abelian(k, z):
    """Check: Laplace({J_λ J}) = k/z² (up to normalization)."""

def verify_br3_virasoro(c, z):
    """Check: Laplace({T_λ T}) = ∂T/z + 2T/z² + c/(12z⁴)."""
```

**Tests** (Tier 3 — cross-check):
- `test_laplace_abelian_cs`: r(z) = k/z²
- `test_laplace_virasoro`: r(z) matches known classical r-matrix

---

## Priority Ordering

| Priority | Module | Tests | Effort | Value |
|----------|--------|-------|--------|-------|
| **P0** | LG m₁ implementation | 2 | 1 hour | Credibility |
| **P0** | LG m₂ implementation | 3 | 2 hours | Credibility |
| **P0** | LG m₃ implementation | 3 | 3 hours | Credibility |
| **P0** | Virasoro REAL Jacobi | 3 | 2 hours | **Highest value** |
| P1 | PVA checker enhancement | 3 | 2 hours | Infrastructure |
| P1 | Sesquilinearity verification | 4 | 2 hours | Infrastructure |
| P1 | LaurentSeries symmetrize | 1 | 30 min | Bug fix |
| P2 | A∞ arity-3 with spectral params | 3 | 4 hours | PVA descent support |
| P2 | FM boundary calculator | 3 | 4 hours | D5 (Jacobi) support |
| P2 | Arnold relations | 2 | 2 hours | D5 support |
| P3 | Convention comparison | 4 | 3 hours | Bridge support |
| P3 | Laplace bridge | 2 | 2 hours | BR3 support |
| P3 | Nonabelian CS (su₂) | 4 | 6 hours | First nontrivial example |
| P4 | W₃ operations | 7 | 8 hours | Ambitious |
| P4 | Homotopy transfer | 3 | 6 hours | D6 support |

**Total estimated effort**: ~45 hours of implementation + testing

### Test count targets

| Current | After Phase 1 | After Phase 2 | After Phase 3 | After all |
|---------|--------------|---------------|---------------|-----------|
| 38 | ~50 | ~60 | ~68 | ~90+ |
| 30% genuine | ~55% genuine | ~65% genuine | ~70% genuine | ~80% genuine |

---

## Module Dependency Graph

```
spectral.py (core) ──── LaurentSeries, reg_sing_decompose
  │
  ├── ainfty.py ──── koszul_sign, verify_ainfty_identity, sesquilinearity
  │     │
  │     └── spectral_substitution.py (new) ──── block fusion
  │
  ├── pva.py ──── PVAChecker with all 5 axioms
  │
  ├── fm_boundary.py (new) ──── strata, signs, Stokes
  │     │
  │     └── arnold.py (new) ──── AOS cancellations
  │
  └── examples/
        ├── free_multiplet.py ✓
        ├── lg_cubic.py ← IMPLEMENT
        ├── abelian_cs.py ✓ (but trivial)
        ├── virasoro.py ← FIX JACOBI
        ├── nonabelian_cs.py (new)
        └── w3.py (new)

Cross-volume:
  convention_check.py (new) ──── Vol I ↔ Vol II sign comparison
  laplace_bridge.py (new) ──── BR3 verification
  homotopy_transfer.py (new) ──── HPL for D6
```

---

## What Success Looks Like

After full implementation:
- **Every worked example has genuine computation behind it** (no stubs, no `pass`, no `return S.Zero`)
- **The PVA axioms are verified computationally** for Virasoro and su(2)
- **The A∞ identities are verified** with spectral parameters for LG cubic
- **The convention comparison** proves Vol I and Vol II signs agree
- **The Laplace bridge** provides computational evidence for BR3
- **~90+ tests**, **~80% genuine verification** (up from 38 tests, 30% genuine)

This transforms the compute infrastructure from "scaffolding with stubs" to
"genuine computational support for the paper's claims."
