# Admissible sl_3 Koszulness: Frontier Assessment

## Status

**sl_2**: PROVED at all admissible levels (rem:admissible-koszul-status).
**sl_3 and higher rank**: OPEN.

## The Precise Obstruction

The obstruction is **not** the bar-Ext vs ordinary-Ext gap in the abstract
sense. The obstruction is concrete and structural:

### Why sl_2 works

For sl_2 at admissible level k = p/q - 2:
- dim(sl_2) = 3, so max bar arity = 3.
- The null-vector ideal I_k is generated in a **single conformal weight**
  h_null = (p-1)*q.
- For most admissible levels, h_null > 3, so nulls never enter the bar range.
  The quotient bar complex equals the universal bar complex, which is Koszul.
- Even when h_null <= 3 (possible for small p, q), the quotient bar spectral
  sequence degenerates at E_2 by the Kac-Wakimoto character formula because
  there is only one null-vector generator.

### Why sl_3 fails

For sl_3 at admissible level k = p/q - 3:
- dim(sl_3) = 8, so max bar arity = 8.
- The null-vector ideal has generators at **multiple conformal weights**:
  - From the highest root theta: grade (p-2)*q.
  - From simple roots alpha_1, alpha_2: grade (p-1)*q.
- These are at DIFFERENT weights, so the quotient bar complex is affected
  at multiple points simultaneously.
- For q = 2, p = 3 (k = -3/2): h_null(theta) = 2, h_null(alpha_i) = 4.
  Both are <= 8 (max bar arity). Multiple null grades in the bar range.

The core difficulty: with null vectors at multiple weights, the quotient
bar spectral sequence may have nontrivial differentials coupling the
different null-vector contributions. The single-generator argument that
works for sl_2 breaks down.

## The Li-bar Spectral Sequence Route

The most promising attack uses the Li filtration (constr:li-bar-spectral-sequence):

    E_0 = bar(R_{L_k})     (bar complex of C_2 algebra)
    E_1 = Tor^R_*(k, k)    (bar homology of C_2 algebra)
    E_2 = H(E_1, d_1)      (Poisson differential)

**Koszulness criterion**: E_2 concentrated on the diagonal => chirally Koszul.

Key structural input (Arakawa 2015, 2017): ALL admissible L_k(sl_N) are
rational, hence C_2-cofinite. So X_{L_k} = {0} (the associated variety
is the zero orbit), and R_{L_k} is an **Artinian local algebra**. This
makes the E_1 page finite-dimensional and computable.

### What the existing engine computes

The theorem_admissible_sl3_libar_engine.py implements:

1. **C_2 algebra structure**: R_{L_k} = tensor product of truncated
   polynomial rings (one per sl_3 generator, truncated at the null grade).

2. **E_1 via Kunneth**: Since R is a tensor product of truncated polynomials,
   Tor^R = tensor product of Tor for each factor. Each truncated polynomial
   k[x]/(x^d) has known Tor: periodic resolution, Tor_n at specific weights.

3. **Diagonal concentration analysis**: For d = 2 (null at grade 2), the
   Tor is diagonal. For d >= 3, off-diagonal classes appear in E_1.

4. **Poisson d_1 differential**: The Lie-Poisson bracket on sl_3* couples
   Cartan and root sectors. The structural argument: semisimplicity of the
   adjoint action provides a contracting homotopy that kills off-diagonal
   E_1 classes.

### The gap in the structural argument

The engine's structural d_1 argument (lines 59-73 of the docstring) claims
that Lie bracket coupling kills all off-diagonal E_1 classes. This is
**verified computationally** for the cases h_theta = 2 (Kunneth
decomposition is explicit and small), but the extension to h_theta >= 3
relies on:

- Surjectivity of the Lie bracket map [E_alpha, -]: off-diagonal classes
  in the Cartan sector are mapped to diagonal classes in the root sector.
- Nondegeneracy of the Cartan action on root generators.

These are properties of the **quotient** Poisson algebra, not just the
universal one. For the universal algebra sl_3*, they hold by Whitehead's
lemma. For the truncated quotient, the argument needs verification at each
truncation level.

## Can the Three-Bar-Complex Picture Help?

The three bar complexes are:
1. B(V_k) -- bar of the universal algebra (always Koszul)
2. B(L_k) -- bar of the simple quotient (target)
3. B(I_k) -- bar complex of the null ideal

The relationship: B(L_k) = B(V_k) / B(I_k) as a quotient bar complex
(not exact, but there is a filtration spectral sequence).

### Potential leverage

The three-bar picture provides one additional verification path:

- **Quotient bar SS**: The short exact sequence 0 -> I_k -> V_k -> L_k -> 0
  gives a long exact sequence in bar homology. If B(I_k) has cohomology
  concentrated on the diagonal (which it does when I_k is generated in a
  single degree), then L_k inherits diagonal concentration from V_k.

- **For sl_3**: I_k has generators at MULTIPLE degrees (the theta-null
  and the alpha-nulls). So the quotient bar SS has potentially nontrivial
  connecting maps between different null-vector contributions. The
  three-bar picture does NOT simplify the multi-weight difficulty; it
  restates it in a different language.

### Where it does help

The three-bar picture helps for ONE specific case: if the null-vector
ideal I_k happens to be generated by a **regular sequence** in the bar
complex. Then the quotient bar complex has a Koszul resolution, and
diagonal concentration follows. For sl_2, the single null vector is
automatically a regular element. For sl_3, checking regularity of the
multi-generator null ideal requires explicit computation at each level.

## Assessment

### Feasibility: MEDIUM (not easy, not blocked)

The problem is well-posed and has concrete computational content:

1. **Finite computation**: For each admissible level (p, q) with q <= 6,
   the C_2 algebra R_{L_k} is a finite-dimensional Artinian algebra.
   Its bar complex, E_1 page, and E_2 page are all finite-dimensional
   and computable by linear algebra.

2. **Existing infrastructure**: Two engines already built:
   - admissible_koszul_rank2_engine.py (null vectors, C_2 algebra dims,
     Li-bar E_1/E_2 estimates, associated variety)
   - theorem_admissible_sl3_libar_engine.py (Kunneth decomposition,
     structural d_1 analysis, character comparisons)

3. **Critical test cases**:
   - k = -3/2 (p=3, q=2): h_theta = 2, h_alpha = 4. Both in bar range.
     This is the FIRST case where the multi-weight difficulty appears.
   - k = -5/3 (p=4, q=3): h_theta = 6, h_alpha = 9. h_theta in bar range.
   - k = 0 (p=3, q=1): integrable. Koszul (known).

4. **Bottleneck**: The Poisson d_1 differential on the quotient C_2
   algebra is a finite-dimensional linear algebra problem, but its
   matrix depends on the FULL sl_3 structure constants restricted to
   the truncated polynomial ring. Computing this matrix explicitly for
   the critical levels (especially k = -3/2) is the key step.

### Most productive next step

Explicit computation of the E_2 page for k = -3/2 (p=3, q=2):
- R_{L_k} is Artinian with dim < 100 (8 generators, truncation at grade 2-4).
- The bar complex has at most 8 terms (max arity = 8).
- The d_1 matrix is a finite matrix over Q.
- If E_2 is diagonal: Koszulness at this level is PROVED.
- If E_2 has off-diagonal classes: either find a d_2 that kills them, or
  exhibit a genuine obstruction to Koszulness.

This is a concrete, bounded computation. The existing engine infrastructure
supports it. The result would be the FIRST data point for admissible sl_3
Koszulness at a level where nulls enter the bar range.
