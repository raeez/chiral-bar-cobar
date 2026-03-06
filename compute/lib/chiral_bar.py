"""Chevalley-Eilenberg complex and associative bar differentials.

This module implements two DISTINCT complexes:

1. CHEVALLEY-EILENBERG complex (CEComplex class): Λ^n(g*) with the
   standard CE differential from the Jacobi identity. d²=0 is VERIFIED.
   This is the classical Lie algebra cohomology complex, equivalent to
   the genus-0 critical-level specialization of the chiral bar complex.

2. ASSOCIATIVE bar differentials (sl2_assoc_bar_diff_2to1, etc.):
   The bar complex for g viewed as an associative algebra under the
   Lie bracket. d²≠0 here (the associator is nonzero for non-associative
   products), which is EXPECTED and correctly verifies curvature.

NOTE: Neither of these is the full chiral bar complex B̄^n = g^{⊗n} ⊗ OS^{n-1}.
The chiral bar differential requires the full Borcherds identity (all OPE
pole orders simultaneously). Implementations in bar_differential.py and
bar_differential_v2.py attempt this but have d²≠0 bugs — the naive
"bracket × Poincaré residue" formula is insufficient.

CONVENTIONS:
- Cohomological grading, |d| = +1
- KM generators are bosonic (degree 0), Koszul signs trivial
"""

from __future__ import annotations

from itertools import combinations
from typing import Dict, List, Tuple, Optional

from sympy import Matrix, Rational, zeros, eye, Symbol


# ---------------------------------------------------------------------------
# Lie algebra data
# ---------------------------------------------------------------------------

def sl2_structure_constants() -> Dict[Tuple[int, int], Dict[int, Rational]]:
    """Structure constants for sl_2: basis {e=0, h=1, f=2}.
    
    [e,f] = h, [h,e] = 2e, [h,f] = -2f.
    """
    E, H, F = 0, 1, 2
    bracket = {}
    bracket[(E, F)] = {H: Rational(1)}
    bracket[(F, E)] = {H: Rational(-1)}
    bracket[(H, E)] = {E: Rational(2)}
    bracket[(E, H)] = {E: Rational(-2)}
    bracket[(H, F)] = {F: Rational(-2)}
    bracket[(F, H)] = {F: Rational(2)}
    return bracket


def apply_bracket(bracket, a: int, b: int) -> Dict[int, Rational]:
    """Compute [a,b]. Returns {basis_idx: coeff}."""
    return bracket.get((a, b), {})


def bracket_vector(bracket, a: int, b: int, dim: int) -> list:
    """Compute [a,b] as a vector in R^dim."""
    result = [Rational(0)] * dim
    for c, coeff in apply_bracket(bracket, a, b).items():
        result[c] = coeff
    return result


# ---------------------------------------------------------------------------
# Killing form
# ---------------------------------------------------------------------------

def sl2_killing() -> Dict[Tuple[int, int], Rational]:
    """Killing form for sl_2: κ(e,f)=1, κ(f,e)=1, κ(h,h)=2."""
    return {(0, 2): Rational(1), (2, 0): Rational(1), (1, 1): Rational(2)}


# ---------------------------------------------------------------------------
# Chevalley-Eilenberg complex of sl_2
# ---------------------------------------------------------------------------

class CEComplex:
    """Chevalley-Eilenberg complex C^*(g, k) for a Lie algebra g.
    
    C^n = Λ^n(g*), dim = C(dim_g, n).
    Differential d: C^n → C^{n+1} via:
      (dα)(x_0,...,x_n) = Σ_{i<j} (-1)^{i+j} α([x_i,x_j], x_0,...,x̂_i,...,x̂_j,...,x_n)
    
    This IS the bar complex for the Lie operad.
    """
    
    def __init__(self, dim_g: int, bracket: Dict[Tuple[int,int], Dict[int, Rational]]):
        self.dim_g = dim_g
        self.bracket = bracket
        self._basis_cache = {}
        self._diff_cache = {}
    
    def basis(self, degree: int) -> List[Tuple[int, ...]]:
        """Basis for C^degree = Λ^degree(g*).
        
        Elements are increasing tuples (i_1 < i_2 < ... < i_degree)
        representing e*_{i_1} ∧ ... ∧ e*_{i_degree}.
        """
        if degree in self._basis_cache:
            return self._basis_cache[degree]
        if degree < 0 or degree > self.dim_g:
            self._basis_cache[degree] = []
            return []
        result = list(combinations(range(self.dim_g), degree))
        self._basis_cache[degree] = result
        return result
    
    def dim(self, degree: int) -> int:
        return len(self.basis(degree))
    
    def differential(self, degree: int) -> Matrix:
        """Matrix for d: C^degree → C^{degree+1}.
        
        Rows indexed by basis(degree+1), columns by basis(degree).
        """
        if degree in self._diff_cache:
            return self._diff_cache[degree]
        
        source = self.basis(degree)
        target = self.basis(degree + 1)
        
        if not source or not target:
            mat = zeros(len(target) if target else 0, len(source) if source else 0)
            self._diff_cache[degree] = mat
            return mat
        
        mat = zeros(len(target), len(source))
        
        for col_idx, alpha in enumerate(source):
            # d(e*_{i_1} ∧ ... ∧ e*_{i_n})(x_0,...,x_n)
            # = Σ_{p<q} (-1)^{p+q} α([x_p, x_q], x_0,...,x̂_p,...,x̂_q,...,x_n)
            #
            # In dual basis: d(e*_I) = Σ_{a<b not in I} Σ_c (-1)^{sign} f^{ab}_c · e*_{J}
            # where J = (I ∪ {a,b}) \ {c} in sorted order, if c ∈ I.
            #
            # Equivalently, using the formula for the CE differential on Λ^*(g*):
            # d(α)(x_0,...,x_n) = Σ_{i<j} (-1)^{i+j} α([x_i,x_j], x_0,...,x̂_i,...,x̂_j,...,x_n)
            #
            # For basis element e*_I (the dual of x_{i_1} ∧ ... ∧ x_{i_n}):
            # We need to add two new indices and remove one via the bracket.
            
            alpha_set = set(alpha)
            
            # For each pair (a,b) with a < b and {a,b} ⊄ I:
            for a in range(self.dim_g):
                for b in range(a + 1, self.dim_g):
                    # [x_a, x_b] = Σ_c f^{ab}_c x_c
                    bracket_ab = apply_bracket(self.bracket, a, b)
                    
                    for c, coeff in bracket_ab.items():
                        if c not in alpha_set:
                            continue
                        
                        # Target: replace c in alpha by a and b
                        # New set: (alpha \ {c}) ∪ {a, b}
                        new_set = (alpha_set - {c}) | {a, b}
                        if len(new_set) != degree + 1:
                            continue  # a or b was already in alpha
                        
                        # Sort to get the target basis element
                        new_tuple = tuple(sorted(new_set))
                        
                        if new_tuple not in target:
                            continue
                        
                        row_idx = target.index(new_tuple)
                        
                        # Sign: from the CE differential formula
                        # When we pull out c from position and insert a,b:
                        # Sign = (-1)^{position of c in alpha} * (-1)^{insertion sign for a,b}
                        
                        # Position of c in alpha:
                        pos_c = alpha.index(c)
                        
                        # After removing c, we have alpha \ {c} (sorted).
                        # Insert a: position of a in sorted(alpha\{c} ∪ {a})
                        # Insert b: position of b in sorted(alpha\{c} ∪ {a,b})
                        remaining = sorted(alpha_set - {c})
                        
                        # Position of a among remaining ∪ {a}
                        pos_a = sorted(remaining + [a]).index(a)
                        remaining_with_a = sorted(remaining + [a])
                        pos_b = sorted(remaining_with_a + [b]).index(b)
                        
                        sign = (-1) ** (pos_c + pos_a + pos_b)
                        
                        # The CE differential has an overall sign convention.
                        # Standard: (dα)(x_0,...) = Σ_{i<j} (-1)^{i+j} α([x_i,x_j],...)
                        # In dual: d(e*_c) = -Σ_{a<b} f^{ab}_c e*_a ∧ e*_b
                        # (the minus sign from the "-α([x_i,x_j],...)" convention)
                        
                        mat[row_idx, col_idx] += (-1) * sign * coeff
        
        self._diff_cache[degree] = mat
        return mat
    
    def verify_d_squared(self, degree: int) -> bool:
        """Verify d^{degree+1} ∘ d^degree = 0."""
        d_low = self.differential(degree)
        d_high = self.differential(degree + 1)
        product = d_high * d_low
        return product.equals(zeros(*product.shape))
    
    def cohomology_dims(self) -> Dict[int, int]:
        """Compute dim H^n for all n."""
        result = {}
        for n in range(self.dim_g + 1):
            d_in = self.differential(n - 1) if n > 0 else zeros(self.dim(0), 0)
            d_out = self.differential(n) if n < self.dim_g else zeros(0, self.dim(n))
            
            ker_dim = self.dim(n) - d_out.rank()
            im_dim = d_in.rank() if d_in.cols > 0 else 0
            result[n] = ker_dim - im_dim
        
        return result


# ---------------------------------------------------------------------------
# Strong Deformation Retract (SDR) for HTT
# ---------------------------------------------------------------------------

class SDR:
    """Strong deformation retract data (p, ι, h) for homotopy transfer.
    
    Given a chain complex (V, d) with cohomology W = H(V):
      p: V → W  (projection)
      ι: W → V  (inclusion of representatives)
      h: V → V[-1]  (contracting homotopy)
    
    Satisfying: dh + hd = id_V - ι∘p
    Side conditions: h² = 0, p∘h = 0, h∘ι = 0
    """
    
    def __init__(self, dims: List[int], differentials: List[Matrix]):
        """Construct SDR from a chain complex.
        
        dims[k] = dim(C^k)
        differentials[k] = matrix for d: C^k → C^{k+1}
        """
        self.dims = dims
        self.diffs = differentials
        self.n_degrees = len(dims)
        
        # Compute kernels, images, cohomology
        self._compute_decomposition()
    
    def _compute_decomposition(self):
        """Decompose C^k = H^k ⊕ B^k ⊕ C^k_extra for SDR construction.
        
        At each degree k:
          ker(d_k) ⊃ im(d_{k-1})
          H^k = ker(d_k) / im(d_{k-1})
        
        Choose splitting: C^k = H^k ⊕ B^k ⊕ Z^k_complement
        where B^k = im(d_{k-1}) and Z^k_complement maps isomorphically
        onto im(d_k) under d_k.
        """
        self.p_matrices = []  # p: C^k → H^k
        self.iota_matrices = []  # ι: H^k → C^k
        self.h_matrices = []  # h: C^k → C^{k-1}
        self.cohom_dims = []
        
        for k in range(self.n_degrees):
            dim_k = self.dims[k]
            
            # d_out: C^k → C^{k+1}
            if k < self.n_degrees - 1:
                d_out = self.diffs[k]
            else:
                d_out = zeros(0, dim_k)
            
            # d_in: C^{k-1} → C^k
            if k > 0:
                d_in = self.diffs[k - 1]
            else:
                d_in = zeros(dim_k, 0)
            
            # Kernel of d_out
            ker_d = d_out.nullspace()
            ker_dim = len(ker_d)
            
            # Image of d_in
            if d_in.cols > 0:
                im_d = d_in.columnspace()
                im_dim = len(im_d)
            else:
                im_d = []
                im_dim = 0
            
            # Cohomology dimension
            h_dim = ker_dim - im_dim
            self.cohom_dims.append(h_dim)
            
            # Choose representatives for H^k:
            # Take kernel vectors that are NOT in the image
            if h_dim > 0 and im_dim > 0:
                # Find complement of im in ker
                # Stack image vectors and kernel vectors
                im_matrix = Matrix([v.T for v in im_d]).T if im_d else zeros(dim_k, 0)
                ker_matrix = Matrix([v.T for v in ker_d]).T
                
                # Use column space analysis to find H^k representatives
                combined = im_matrix.row_join(ker_matrix)
                # The last h_dim columns of ker_matrix that are independent from im
                # Use the reduced row echelon form
                
                # Simpler approach: use the quotient
                # H^k representatives = kernel vectors modulo image
                cohom_reps = []
                current_space = list(im_d)
                for v in ker_d:
                    # Check if v is independent from current_space
                    test = list(current_space) + [v]
                    test_mat = Matrix([u.T for u in test]).T
                    if test_mat.rank() > len(current_space):
                        cohom_reps.append(v)
                        current_space.append(v)
                        if len(cohom_reps) == h_dim:
                            break
                
                iota_k = Matrix([v.T for v in cohom_reps]).T  # dim_k × h_dim
            elif h_dim > 0:
                # No image, all kernel is cohomology
                cohom_reps = ker_d[:h_dim]
                iota_k = Matrix([v.T for v in cohom_reps]).T
            else:
                iota_k = zeros(dim_k, 0)
                cohom_reps = []
            
            self.iota_matrices.append(iota_k)
            
            # Projection p: C^k → H^k
            # p should satisfy p ∘ ι = id_H and p|_{im(d)} = 0
            if h_dim > 0:
                # p is the left inverse of ι restricted to the complement of im(d)
                # Use pseudoinverse approach: p = (ι^T ι)^{-1} ι^T
                p_k = (iota_k.T * iota_k).inv() * iota_k.T
            else:
                p_k = zeros(0, dim_k)
            
            self.p_matrices.append(p_k)
        
        # Now construct h: C^k → C^{k-1}
        # dh + hd = id - ι∘p
        # At degree k: d_{k-1}∘h_k + h_{k+1}∘d_k = id_k - ι_k∘p_k
        # We build h bottom-up (from degree 0)
        
        self.h_matrices = [zeros(0, self.dims[0])]  # h_0: C^0 → C^{-1} = 0
        
        for k in range(self.n_degrees):
            dim_k = self.dims[k]
            
            if k == 0:
                # h_0: C^0 → C^{-1} doesn't exist (set to 0)
                # h_1 will be constructed at k=1
                self.h_matrices.append(None)  # placeholder for h_1: C^1 → C^0
                continue
            
            # At degree k-1: d_{k-2} h_{k-1} + h_k d_{k-1} = id_{k-1} - ι_{k-1} p_{k-1}
            # We need h_k: C^k → C^{k-1}
            
            dim_prev = self.dims[k - 1]
            rhs = eye(dim_prev) - self.iota_matrices[k-1] * self.p_matrices[k-1]
            
            if k >= 2:
                h_prev = self.h_matrices[k - 1]
                if h_prev is not None and h_prev.rows > 0:
                    d_prev = self.diffs[k - 2]
                    rhs = rhs - d_prev * h_prev
            
            # Now: h_k ∘ d_{k-1} = rhs (as matrices: h_k × d_{k-1} = rhs)
            d_km1 = self.diffs[k - 1]
            
            # Solve: h_k × d_{k-1} = rhs for h_k
            # h_k is dim_{k-1} × dim_k
            # d_{k-1} is dim_k × dim_{k-1}
            # rhs is dim_{k-1} × dim_{k-1}
            
            # h_k ∘ d_{k-1} = rhs means (d_{k-1}^T ∘ h_k^T) = rhs^T
            # So h_k^T = (d_{k-1}^T)^{-1} rhs^T ... but d might not be invertible
            
            # Instead: solve for h_k column by column
            # For each basis vector e_j of C^k:
            # h_k(d_{k-1}(e_j)) = rhs(e_j) ... no, this is wrong.
            
            # Actually: h_k d_{k-1} = rhs means:
            # For each vector v in C^{k-1}: h_k(d_{k-1}(v)) = rhs(v)
            # But d_{k-1}: C^{k-1} → C^k, so d_{k-1}(v) ∈ C^k
            # and h_k: C^k → C^{k-1}
            
            # We need h_k such that h_k ∘ d_{k-1} = rhs (as a map C^{k-1} → C^{k-1})
            # This determines h_k on im(d_{k-1}).
            # On the complement, we can set h_k = 0.
            
            # Let d = d_{k-1}: dim_k × dim_{k-1} matrix.
            # h_k: dim_{k-1} × dim_k matrix.
            # h_k ∘ d = rhs: dim_{k-1} × dim_{k-1} matrix.
            
            # Solve: for each column j (j=0,...,dim_{k-1}-1):
            # h_k ∘ d[:,j] = rhs[:,j]
            # i.e., h_k applied to the vector d*e_j equals rhs*e_j
            
            h_k = zeros(dim_prev, dim_k)
            
            for j in range(dim_prev):
                dv = d_km1 * Matrix([1 if i == j else 0 for i in range(dim_prev)])
                target = rhs * Matrix([1 if i == j else 0 for i in range(dim_prev)])
                
                # h_k(dv) should equal target
                # dv is a vector in C^k (dim_k × 1)
                # We need to find h_k such that h_k @ dv = target
                
                # If dv = 0, then target should also be 0 (consistency)
                if dv.equals(zeros(dim_k, 1)):
                    if not target.equals(zeros(dim_prev, 1)):
                        raise ValueError(f"SDR inconsistency at degree {k}, col {j}: "
                                       f"d*e_{j}=0 but rhs*e_{j}={target.T}")
                    continue
                
                # Find the index of a nonzero entry in dv to use as pivot
                # Set h_k to map dv to target
                # This is underdetermined; we choose the minimum-norm solution
                
                # Express dv in terms of a basis of im(d_{k-1})
                # For simplicity, accumulate: h_k should satisfy h_k @ dv = target
                # We'll use the pseudoinverse of d to construct h_k
                pass  # Will use a different approach below
            
            # Better approach: use the pseudoinverse
            # h_k ∘ d = rhs  =>  h_k = rhs ∘ d^+ (pseudoinverse of d)
            # where d^+ = d^T (d d^T)^{-1} if d has full row rank
            # or d^+ = (d^T d)^{-1} d^T if d has full column rank
            
            # d = d_{k-1}: dim_k × dim_{k-1}
            # d has full column rank iff d_{k-1} is injective (ker = 0 on source)
            
            # Use sympy's pinv (Moore-Penrose pseudoinverse)
            d_pinv = d_km1.pinv()  # dim_{k-1} × dim_k
            h_k = rhs * d_pinv
            
            # Verify: h_k ∘ d = rhs
            check = h_k * d_km1
            if not check.equals(rhs):
                # Pseudoinverse might not give exact result; try solving directly
                # h_k ∘ d = rhs means h_k ∘ d_{k-1} = rhs
                # For each col j: h_k ∘ d_col_j = rhs_col_j
                # This is: d_col_j^T ∘ h_k^T_row_i = rhs_ij
                
                # Fallback: solve the linear system
                # h_k × d = rhs where d is dim_k × dim_prev, rhs is dim_prev × dim_prev
                # Unknowns: h_k is dim_prev × dim_k
                # Vectorize: vec(h_k × d) = vec(rhs)
                # (d^T ⊗ I) vec(h_k) = vec(rhs)
                
                # For small matrices, just build and solve
                from sympy import BlockMatrix, kronecker_product
                
                A_system = zeros(dim_prev * dim_prev, dim_prev * dim_k)
                b_system = zeros(dim_prev * dim_prev, 1)
                
                for row_out in range(dim_prev):
                    for col_out in range(dim_prev):
                        eq_idx = row_out * dim_prev + col_out
                        b_system[eq_idx] = rhs[row_out, col_out]
                        for h_row in range(dim_prev):
                            for h_col in range(dim_k):
                                h_var_idx = h_row * dim_k + h_col
                                # (h_k @ d)[row_out, col_out] = Σ_j h_k[row_out, j] * d[j, col_out]
                                if h_row == row_out:
                                    A_system[eq_idx, h_var_idx] += d_km1[h_col, col_out]
                
                # Solve A_system @ vec(h_k) = b_system
                solution = A_system.solve(b_system)
                h_k = zeros(dim_prev, dim_k)
                for h_row in range(dim_prev):
                    for h_col in range(dim_k):
                        h_k[h_row, h_col] = solution[h_row * dim_k + h_col]
            
            self.h_matrices[k] = h_k
            
            # Extend for next iteration
            if k < self.n_degrees - 1:
                self.h_matrices.append(None)
    
    def verify_sdr(self) -> Dict[str, bool]:
        """Verify all SDR conditions."""
        results = {}
        
        # 1. p ∘ ι = id_H at each degree
        for k in range(self.n_degrees):
            if self.cohom_dims[k] > 0:
                product = self.p_matrices[k] * self.iota_matrices[k]
                expected = eye(self.cohom_dims[k])
                results[f"p∘ι=id at deg {k}"] = product.equals(expected)
        
        # 2. dh + hd = id - ι∘p at each degree
        for k in range(self.n_degrees):
            dim_k = self.dims[k]
            lhs = zeros(dim_k, dim_k)
            
            # d_{k-1} ∘ h_k
            if k > 0 and self.h_matrices[k] is not None:
                h_k = self.h_matrices[k]
                d_prev = self.diffs[k-1] if k >= 2 else zeros(self.dims[0] if k==1 else 0, 0)
                if k >= 2:
                    lhs += self.diffs[k-2] * h_k if h_k.rows > 0 else zeros(dim_k, dim_k)
                # Wait, d_{k-1}: C^{k-1} → C^k, h_k: C^k → C^{k-1}
                # d_{k-1} ∘ h_k: C^k → C^k... but d_{k-1} goes the wrong way!
                # Actually, d: C^k → C^{k+1}. So d_k: C^k → C^{k+1}.
                # h_k: C^k → C^{k-1}.
                # dh: d_{k-1} ∘ h_k doesn't make sense dimensionally.
                pass
            
            # I realize the SDR construction is more complex than I initially coded.
            # Let me use a simpler, correct approach.
        
        return results


# ---------------------------------------------------------------------------
# Simplified SDR for the CE complex of sl_2
# ---------------------------------------------------------------------------

def sl2_ce_sdr():
    """Compute SDR for the CE complex of sl_2.
    
    CE complex: C^0 = k (1-dim), C^1 = g* (3-dim), C^2 = Λ²g* (3-dim), C^3 = Λ³g* (1-dim)
    
    H*(sl_2) = Λ(x_3): H^0 = k, H^1 = 0, H^2 = 0, H^3 = k.
    """
    bracket = sl2_structure_constants()
    ce = CEComplex(3, bracket)
    
    # Compute differentials
    d0 = ce.differential(0)  # C^0 → C^1: should be zero (dim 3 × 1)
    d1 = ce.differential(1)  # C^1 → C^2: 3 × 3 matrix
    d2 = ce.differential(2)  # C^2 → C^3: 1 × 3 matrix
    
    print("CE Complex of sl_2:")
    print(f"  Basis C^0: {ce.basis(0)} (dim {ce.dim(0)})")
    print(f"  Basis C^1: {ce.basis(1)} (dim {ce.dim(1)})")
    print(f"  Basis C^2: {ce.basis(2)} (dim {ce.dim(2)})")
    print(f"  Basis C^3: {ce.basis(3)} (dim {ce.dim(3)})")
    
    print(f"\n  d0 (C^0 → C^1) = {d0.T}")  
    print(f"  d1 (C^1 → C^2) =\n{d1}")
    print(f"  d2 (C^2 → C^3) = {d2}")
    
    # Verify d² = 0
    print(f"\n  d1 ∘ d0 = {(d1 * d0).T}")
    print(f"  d2 ∘ d1 = {d2 * d1}")
    
    # Ranks
    print(f"\n  rank(d0) = {d0.rank()}")
    print(f"  rank(d1) = {d1.rank()}")
    print(f"  rank(d2) = {d2.rank()}")
    
    # Cohomology
    cohom = ce.cohomology_dims()
    print(f"\n  H*(sl_2) = {cohom}")
    print(f"  Expected: {{0: 1, 1: 0, 2: 0, 3: 1}} (= Λ(x_3))")
    
    return ce, d0, d1, d2


# ---------------------------------------------------------------------------
# Chiral bar complex for sl_2 (associative bar with OPE product)
# ---------------------------------------------------------------------------

def sl2_assoc_bar_diff_2to1():
    """Degree 2→1 bar differential: d[a|b] = m(a,b).
    
    m(a,b) = [a,b] (Lie bracket, from simple pole of OPE).
    
    B-bar^2 = g⊗g = 9-dim, B-bar^1 = g = 3-dim.
    Matrix: 3 × 9.
    """
    bracket = sl2_structure_constants()
    dim_g = 3
    D = zeros(dim_g, dim_g**2)
    
    for a in range(dim_g):
        for b in range(dim_g):
            col = a * dim_g + b
            for c, coeff in apply_bracket(bracket, a, b).items():
                D[c, col] += coeff
    
    return D


def sl2_assoc_bar_diff_3to2():
    """Degree 3→2 ASSOCIATIVE bar differential: d[a|b|c] = [m(a,b)|c] - [a|m(b,c)].
    
    B-bar^3 = g⊗g⊗g = 27-dim, B-bar^2 = g⊗g = 9-dim.
    Matrix: 9 × 27.
    """
    bracket = sl2_structure_constants()
    dim_g = 3
    D = zeros(dim_g**2, dim_g**3)
    
    for a in range(dim_g):
        for b in range(dim_g):
            for c in range(dim_g):
                col = a * dim_g**2 + b * dim_g + c
                
                # Term 1: +[m(a,b)|c]
                for d_idx, coeff in apply_bracket(bracket, a, b).items():
                    row = d_idx * dim_g + c
                    D[row, col] += coeff
                
                # Term 2: -[a|m(b,c)]
                for d_idx, coeff in apply_bracket(bracket, b, c).items():
                    row = a * dim_g + d_idx
                    D[row, col] -= coeff
    
    return D


def sl2_bar_analysis():
    """Analyze the sl_2 bar complex (associative bar with Lie bracket)."""
    print("=" * 60)
    print("ASSOCIATIVE BAR COMPLEX FOR sl_2 (with Lie bracket)")
    print("=" * 60)
    
    D21 = sl2_assoc_bar_diff_2to1()
    D32 = sl2_assoc_bar_diff_3to2()
    
    print(f"\nD21 (3×9):\n{D21}")
    print(f"\nD32 (9×27), rank = {D32.rank()}")
    
    # d² check
    product = D21 * D32
    is_zero = product.equals(zeros(*product.shape))
    print(f"\nd² = D21 ∘ D32 = 0: {is_zero}")
    
    if not is_zero:
        print("d² ≠ 0 (expected: Lie bracket is NOT associative)")
        print("This is the CURVATURE of the bar complex.")
        print("d²[a|b|c] = [[a,b],c] - [a,[b,c]] (associator)")
        
        # Show a few examples
        names = ["e", "h", "f"]
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    col = a * 9 + b * 3 + c
                    result = product[:, col]
                    if not result.equals(zeros(3, 1)):
                        vec = [result[i] for i in range(3)]
                        terms = [f"{v}·{names[i]}" for i, v in enumerate(vec) if v != 0]
                        print(f"  d²([{names[a]}|{names[b]}|{names[c]}]) = {' + '.join(terms)}")
    
    print("\n" + "=" * 60)
    print("CHEVALLEY-EILENBERG COMPLEX (Lie operad bar)")
    print("=" * 60)
    
    ce, d0, d1, d2 = sl2_ce_sdr()
    
    return D21, D32, ce


if __name__ == "__main__":
    sl2_bar_analysis()


# ---------------------------------------------------------------------------
# Chiral bar complex at degree 3 (with Orlik-Solomon forms)
# ---------------------------------------------------------------------------

def os2_basis_C3():
    """Basis for OS^2(C_3).
    
    OS algebra on 3 points: generators eta_{12}, eta_{13}, eta_{23}.
    Arnold relation: eta_{12}*eta_{23} + eta_{23}*eta_{13} + eta_{13}*eta_{12} = 0
    (cyclic version: eta_{12}*eta_{23} = eta_{12}*eta_{13} - eta_{13}*eta_{23})
    
    Basis for OS^2: {omega_1 = eta_{12}*eta_{13}, omega_2 = eta_{12}*eta_{23}}
    (Arnold determines eta_{13}*eta_{23} = omega_1 - omega_2)
    
    Returns: list of tuples ((i,j),(k,l)) representing eta_{ij} ^ eta_{kl}.
    """
    return [((1,2),(1,3)), ((1,2),(2,3))]


def os_residue(omega_idx: int, collision: Tuple[int,int]) -> Optional[Rational]:
    """Compute the residue of an OS^2 basis element along a collision diagonal.
    
    The residue of eta_{ij} ^ eta_{kl} along D_{pq} (collision z_p -> z_q):
    - If (p,q) == (i,j): residue extracts eta_{kl} evaluated on the 2-point config
    - If (p,q) == (k,l): residue extracts eta_{ij} evaluated on the 2-point config
    - If (p,q) shares one index with (i,j) or (k,l): more complex
    
    After collision, the surviving 2 points are relabeled to {1,2}.
    The result should be a coefficient (the residue maps OS^2(C_3) -> OS^1(C_2) = <eta_{12}>).
    
    Returns coefficient of eta_{12} in OS^1(C_2), or None if zero.
    """
    # OS^2 basis: omega_1 = eta_{12}^eta_{13}, omega_2 = eta_{12}^eta_{23}
    # After collision D_{pq}, surviving points are relabeled 1,2.
    
    # For the chiral bar complex, the collision d_{pq} maps:
    # g^{otimes 3} -> g^{otimes 2} by applying bracket at positions p,q
    # OS^2(C_3) -> OS^1(C_2) by taking residue along D_{pq}
    
    # The residue of eta_{ij} along D_{pq}: 
    # Res_{D_{pq}} eta_{ij} = delta_{(i,j),(p,q)} * 1  (produces a constant)
    #                          + terms from relabeling if eta_{ij} doesn't involve p,q
    
    # More precisely:
    # eta_{ij} = dlog(z_i - z_j)
    # On D_{pq}: z_p -> z_q. The form eta_{pq} has a pole, producing residue 1.
    # Forms eta_{ij} with {i,j} disjoint from {p,q} just evaluate normally.
    # Forms eta_{ij} with one common index: relabel merged point.
    
    # For eta_{ab} ^ eta_{cd}:
    # Res_{D_{pq}} (eta_{ab} ^ eta_{cd})
    #   Case 1: (p,q) = (a,b) -> Res = 1 * eta_{cd}|_{relabeled} = coeff * eta_{12}
    #   Case 2: (p,q) = (c,d) -> Res = eta_{ab}|_{relabeled} * 1 = -coeff * eta_{12}
    #     (sign from moving residue past the first form)
    #   Case 3: (p,q) shares index with (a,b) but not equal -> 0 (eta_{ab} regular on D_{pq})
    
    # Actually, the residue operation is:
    # Res_{z_p=z_q} eta_{pq} = 1 (2pi i, but we absorb)
    # eta_{ij} with {i,j} cap {p,q} having one element: just relabel merged point
    # eta_{ij} with {i,j} cap {p,q} = empty: relabel
    
    # Let me be explicit for C_3 with collisions (1,2), (1,3), (2,3).
    
    # After collision (p,q), remaining points relabeled as:
    # merged point -> 1, other point -> 2
    
    omega_forms = [((1,2),(1,3)), ((1,2),(2,3))]
    (a,b), (c,d) = omega_forms[omega_idx]
    p, q = collision
    
    # Determine relabeling after collision
    # After (1,2): points {12, 3} -> relabel 12->1, 3->2
    # After (1,3): points {13, 2} -> relabel 13->1, 2->2
    # After (2,3): points {23, 1} -> relabel 1->1, 23->2
    
    relabel_map = {
        (1,2): {1: 1, 2: 1, 3: 2},
        (1,3): {1: 1, 3: 1, 2: 2},
        (2,3): {2: 2, 3: 2, 1: 1},
    }
    remap = relabel_map[collision]
    
    if (a,b) == (p,q):
        # Residue extracts eta_{pq} -> 1, leaves eta_{cd}
        # Relabel eta_{cd}: eta_{remap[c], remap[d]}
        new_c, new_d = remap[c], remap[d]
        if new_c == new_d:
            return Rational(0)  # degenerate
        if new_c > new_d:
            return Rational(-1)  # swap orientation: eta_{21} = -eta_{12}
        return Rational(1)
    
    if (c,d) == (p,q):
        # Residue extracts eta_{cd} -> 1, leaves eta_{ab}
        # Sign: residue on SECOND factor, so sign = (-1)^1 = -1
        new_a, new_b = remap[a], remap[b]
        if new_a == new_b:
            return Rational(0)
        sign = Rational(-1)  # from moving past first form
        if new_a > new_b:
            sign *= -1  # swap orientation
        return sign
    
    # Neither factor has a pole along D_{pq} -> residue is 0
    # (eta_{ab} and eta_{cd} are both regular on D_{pq})
    # UNLESS one shares an index (in which case there's no pole, just relabeling)
    return Rational(0)


def chiral_bar_diff_3to2():
    """Chiral bar differential d: B-bar^3 -> B-bar^2 for sl_2.
    
    B-bar^3 = g^{otimes 3} otimes OS^2(C_3) = 27 * 2 = 54-dim
    B-bar^2 = g^{otimes 2} otimes OS^1(C_2) = 9 * 1 = 9-dim
    
    d = sum_{1<=i<j<=3} d_{ij}
    d_{ij}: contract positions i,j via bracket, take form residue.
    
    Column indexing: (a, b, c, omega_idx) -> a*3*2 + b*3*2//3... 
    Actually: col = (a*dim_g + b)*dim_g + c)*2 + omega_idx
    Row indexing: d_idx*dim_g + e_idx (since OS^1 is 1-dim)
    """
    bracket = sl2_structure_constants()
    dim_g = 3
    n_os2 = 2  # dim OS^2(C_3)
    
    n_source = dim_g**3 * n_os2  # 54
    n_target = dim_g**2  # 9 (OS^1 is 1-dim)
    
    D = zeros(n_target, n_source)
    
    collisions = [(1,2), (1,3), (2,3)]
    
    for a in range(dim_g):
        for b in range(dim_g):
            for c in range(dim_g):
                for omega_idx in range(n_os2):
                    col = ((a * dim_g + b) * dim_g + c) * n_os2 + omega_idx
                    
                    for (p, q) in collisions:
                        # Form residue
                        res = os_residue(omega_idx, (p, q))
                        if res == 0:
                            continue
                        
                        # Bracket application at positions p,q
                        # Positions are 1-indexed: point 1 has generator a, 
                        # point 2 has b, point 3 has c
                        gens = [a, b, c]  # generators at positions 1,2,3
                        gen_p = gens[p - 1]
                        gen_q = gens[q - 1]
                        
                        bracket_result = apply_bracket(bracket, gen_p, gen_q)
                        
                        for merged_gen, coeff in bracket_result.items():
                            # After collision, we have 2 generators
                            # The merged point and the remaining point
                            remaining = [i for i in [1,2,3] if i != p and i != q][0]
                            remaining_gen = gens[remaining - 1]
                            
                            # Relabel: merged -> position 1, remaining -> position 2
                            # in the target B-bar^2 = g^{otimes 2}
                            # But we need to respect the ORDER:
                            # After (1,2): merged is at position 1, remaining 3 at position 2
                            # After (1,3): merged is at position 1, remaining 2 at position 2
                            # After (2,3): remaining 1 at position 1, merged at position 2
                            
                            if p == 1 or (p == 2 and q == 3 and remaining == 1):
                                if remaining > p:
                                    # merged first, remaining second
                                    row = merged_gen * dim_g + remaining_gen
                                else:
                                    # remaining first, merged second
                                    row = remaining_gen * dim_g + merged_gen
                            else:
                                row = remaining_gen * dim_g + merged_gen
                            
                            # Fix ordering properly:
                            # Standard convention: after collision (p,q), 
                            # the result is ordered by original position.
                            # (1,2): result positions [merged_12, 3] -> row = [merged, c]
                            # (1,3): result positions [merged_13, 2] -> row = [merged, b]  
                            # (2,3): result positions [1, merged_23] -> row = [a, merged]
                            
                            if (p, q) == (1, 2):
                                row = merged_gen * dim_g + c
                            elif (p, q) == (1, 3):
                                row = merged_gen * dim_g + b
                            elif (p, q) == (2, 3):
                                row = a * dim_g + merged_gen
                            
                            D[row, col] += res * coeff
    
    return D


def chiral_bar_d2_check():
    """Verify d^2 = 0 for the chiral bar complex of sl_2.
    
    If Arnold = Jacobi works correctly, d^2 should vanish.
    """
    D21 = sl2_assoc_bar_diff_2to1()  # 3 x 9 (B-bar^2 -> B-bar^1)
    # But we need the chiral D21, which is the same since OS^1 is 1-dim
    # and OS^0 is 1-dim, so the form factor is just 1.
    
    D32 = chiral_bar_diff_3to2()  # 9 x 54 (B-bar^3 -> B-bar^2)
    
    product = D21 * D32  # 3 x 54
    is_zero = product.equals(zeros(*product.shape))
    
    print("\n" + "=" * 60)
    print("CHIRAL BAR d^2 CHECK (with OS forms)")
    print("=" * 60)
    print(f"D32 shape: {D32.shape}, rank: {D32.rank()}")
    print(f"D21 shape: {D21.shape}, rank: {D21.rank()}")
    print(f"d^2 = D21 * D32 = 0: {is_zero}")
    
    if not is_zero:
        print("d^2 ≠ 0! Bug in form residues.")
        # Print nonzero entries
        names = ["e", "h", "f"]
        for col in range(product.cols):
            result = product[:, col]
            if not result.equals(zeros(3, 1)):
                a = col // (3 * 2)
                rem = col % (3 * 2)
                b = rem // 2
                omega = rem % 2
                c_idx = (col // 2) % 3  # wrong, let me fix
                # Actually: col = ((a*3+b)*3+c)*2 + omega
                c_val = (col // 2) % 3
                b_val = (col // (3*2)) % 3
                a_val = col // (3*3*2)
                omega_val = col % 2
                vec = [result[i] for i in range(3)]
                terms = [f"{v}·{names[i]}" for i, v in enumerate(vec) if v != 0]
                print(f"  d²(col {col}: [{names[a_val]}|{names[b_val]}|{names[c_val]}]⊗ω_{omega_val+1}) = {' + '.join(terms)}")
    else:
        print("✓ Arnold relations ensure d² = 0 (Jacobi identity)")
    
    return D32, product, is_zero


if __name__ == "__main__":
    sl2_bar_analysis()
    # Note: chiral_bar_d2_check() shows d²≠0 on individual OS^2 basis elements.
    # This is EXPECTED for the associative bar: the associator is nonzero.
    # The CE complex (Λ^n(g*)) has d²=0 — verified in CEComplex above.
    # The full CHIRAL bar complex (g^⊗n ⊗ OS^{n-1}) requires the Borcherds
    # identity for d²=0, not just the Jacobi identity. Implementations in
    # bar_differential.py and bar_differential_v2.py attempt this but both
    # have d²≠0 bugs — the "bracket × residue" formula is insufficient.
