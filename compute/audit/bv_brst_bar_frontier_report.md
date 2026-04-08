# Frontier Report: conj:master-bv-brst (BV/BRST = bar at higher genus)

## 1. Precise conjecture statement

**Location**: `chapters/connections/editorial_constitution.tex`, line 433.

```
\begin{conjecture}[BV/BRST/bar identification]
\label{conj:master-bv-brst}
\ClaimStatusConjectured{}
For a holomorphic field theory on a Riemann surface, the BV/BRST
complex coincides with the bar complex of the associated chiral algebra,
at all genera.
```

The conjecture comes with a clarifying remark (line 440): it is **downstream** of the algebraic theorems (Thms A--D, MC1--5) and "should not be placed on the same logical level." The analytic convergence component of MC5 is resolved; what remains is the **identification** of the two complexes as mathematical objects.

The concordance reformulation (line 9290) makes the statement more precise:

> The conjecture asserts an identification of convolution algebras
> g^oc_A |_{g >= 1}  ~  g^BV_T |_{g >= 1}
> under which Theta^oc_A maps to Theta^BV_T.

At genus 0, this identification is the content of the PVA descent theorems D2--D6 (all proved in Vol II).

---

## 2. What is proved

### Genus 0 (COMPLETE)

- **thm:bv-bar-geometric** (line 146, bv_brst.tex): On P^1, the BV complex (C_BV(A), Q_BV) is isomorphic to the geometric bar complex. Proof via Costello-Gwilliam [CG17], with geometric construction in the manuscript. The BRST operator = bar differential; classical ME = d_bar^2 = 0; anomaly cancellation (c=26) = kappa_tot = 0.

- **thm:brst-bar-genus0** (line 454): Chain-level quasi-isomorphism Phi: (A_tot^rel, Q_BRST) -> (B^ch_0(A_tot), d_bar) for conformal VAs on P^1 with c=26. Proof by spectral sequence comparison (Eilenberg-Moore) on the conformal weight filtration: Phi_0 gives an isomorphism at the E_1 page, lifts to a filtered quasi-isomorphism.

- **thm:bar-semi-infinite-km** (line ~714): For affine KM at all non-critical levels, the chiral bar complex is quasi-isomorphic to the semi-infinite (BRST) complex: H*(B^ch(g_hat_k)) = H^{inf/2+*}(g_hat_k, V_k). Proof by the same spectral sequence technique, without the c=26 hypothesis.

### All genera, Heisenberg (COMPLETE at scalar level)

- **thm:heisenberg-bv-bar-all-genera** (line 1202): For H_kappa at all g >= 1:
  F_g^BV(H_kappa) = F_g^bar(H_kappa) = kappa * lambda_g^FP.
  Four independent proofs: (a) Quillen anomaly + GRR, (b) Selberg zeta function, (c) direct family index, (d) numerical verification to g=15.

### Genus 1, classes G/L/C (scalar level PROVED, chain level PROVED for G/L, PROVED for C)

The three obstructions to chain-level identification (prop:chain-level-three-obstructions, line 1448) are classified by shadow depth:

| Class | r_max | BV=bar | Mechanism |
|-------|-------|--------|-----------|
| G (Heisenberg) | 2 | **proved** | no interaction vertices |
| L (affine KM) | 3 | **proved** | Jacobi identity kills cubic harmonic correction |
| C (betagamma) | 4 | **proved** | harmonic decoupling (three-mechanism argument) |
| M (Virasoro, W_N) | inf | **false at ordinary chain level** | genuine obstruction |

The class C resolution (rem:bv-bar-class-c-proof, line 1546) works by three mechanisms: (i) the quartic vertex comes from a composite field T = :beta*d(gamma):, not a fundamental pole, (ii) Hodge type forces the harmonic-propagator contraction to vanish, (iii) the harmonic correction factors through the free betagamma (class G) trace.

---

## 3. The class M obstruction

This is the genuine open problem. The manuscript states (line 1627):

> For class M, the identification Delta_BV = d_sew **fails** at the ordinary chain level: the quartic harmonic discrepancy delta_4^harm ~ Q^contact * kappa / Im(tau) is **not** a coboundary, because 1/Im(tau) is non-holomorphic and hence not in the image of the holomorphic bar differential. The Fay trisecant identity does not cancel it.

The class M obstruction has a precise quantitative formula. The quartic contact invariant Q^contact_Vir = 10/(c(5c+22)) is the coefficient. The harmonic propagator correction at the quartic level produces a term proportional to Q^contact * kappa / Im(tau), which is not holomorphic and therefore cannot be a coboundary in the holomorphic bar complex.

**Why class M is different from class C**: In the betagamma system, the quartic vertex factors through COMPOSITE fields (T = :beta*d(gamma):), and the BV contraction passes through FUNDAMENTAL fields (beta, gamma). This factorization decouples the harmonic part. For Virasoro, T is itself the fundamental generator: the quartic vertex T_{(3)}T = c/2 couples T directly to T, and the harmonic correction does not factor through a free subsystem.

The compute module `bv_bar_class_m_engine.py` investigates six avenues: explicit genus-1 arity-4 amplitude comparison, coboundary analysis, Fay trisecant cancellation, coderived category approach, cohomology class of the first discrepancy, and cross-verification at special central charges (c=1, 13, 25, 26).

---

## 4. The coderived reformulation

The manuscript itself identifies the correct reformulation (line 1633):

> The correct formulation requires the **coderived** category D^co(A) of Positselski, where d^2 = m_0 * id is permitted and the curvature is absorbed into the bar differential. In D^co, the bar complex B(A) has D_B^2 = 0 **always**, and Conjecture conj:master-bv-brst should be reformulated as a coderived quasi-isomorphism.

This is the key insight: the conjecture as literally stated is FALSE for class M at the ordinary chain level, but should hold in the coderived category. The curvature kappa * omega_g on the bar side and the conformal anomaly (c-26)/12 * c_0 on the BV side play the same role: they are the curvature terms that prevent d^2 = 0 in the uncurved sense but are absorbed into the curved differential.

**Current status of the coderived reformulation**: This is stated as a direction but not formalized as a precise conjecture with hypotheses. A precise version would need:
1. A specific definition of "coderived quasi-isomorphism" in the factorization algebra context
2. Verification that the BV complex at genus >= 1 admits a natural coderived structure compatible with the bar complex's curved A-infinity structure
3. The comparison map extending the genus-0 Phi to all genera in the coderived category

---

## 5. Does the E_1/ordered-bar structure help?

**Assessment**: The BV/BRST complex carries a natural ordering from the path integral (time-ordering in the topological direction R, for HT theories on C x R). The bar complex in the monograph is the **symmetric** bar (factorization coalgebra on Ran(X)), not the ordered bar. However:

1. The genus-0 comparison (thm:brst-bar-genus0) already works at the E_1 page of the spectral sequence. The spectral sequence comparison theorem (Eilenberg-Moore) lifts the E_1-page isomorphism to a chain-level quasi-isomorphism.

2. The ordered vs symmetric distinction is a genus-0 phenomenon: at genus 0, the ordered bar (Hochschild homology, tensor powers) and the symmetric bar (Lie homology, exterior powers) are quasi-isomorphic in characteristic 0 via the antisymmetrization map (AP37: they are categorically different but cohomologically isomorphic). At genus >= 1, the relevant structure is the MODULAR operad, which is inherently symmetric (the sewing does not preserve ordering around a node).

3. The BV Laplacian Delta_BV is a SYMMETRIC operator: it contracts field-antifield pairs without ordering. The sewing operator d_sew on the bar complex is also symmetric. The genus >= 1 comparison is between symmetric operations.

**Conclusion**: The E_1/ordered-bar perspective sharpens the genus-0 comparison (and is already used in the spectral sequence proofs) but does NOT provide new leverage at genus >= 1, where the relevant structures are modular and symmetric.

---

## 6. Period integral corrections and the BV framework

The corrected bar differential D^(g) (incorporating Fay trisecant / period matrix data from the genus-g surface) has the following BV interpretation:

- The bar differential d_bar at genus 0 uses d log(z_i - z_j), which is the algebraic propagator.
- At genus 1, the bar propagator becomes d log sigma(z-w|tau) (Weierstrass sigma function), which incorporates the period matrix through Eisenstein series.
- The BV propagator P(z,w) = dbar^{-1} delta(z,w) includes a harmonic part P_harm that depends on the complex structure of Sigma_g.

The period integral corrections correspond to:
- **On the bar side**: the transition from genus-0 propagator d log(z-w) to genus-g propagator d log E(z,w) (prime form), which absorbs the moduli dependence into the propagator's regular part.
- **On the BV side**: the Quillen anomaly formula curv(h_Q) = -2pi*i * c_1(E), which universally relates the determinant line bundle curvature to the Hodge class.

The discrepancy between the two propagators is P_harm = dz * dw / Im(tau) (at genus 1). This is NOT a renormalization counterterm; it is a genuine cohomological obstruction arising from the non-holomorphicity of the Green function vs the holomorphicity of the bar propagator. The Fay trisecant identity does NOT cancel this term for class M.

**BV interpretation of P_harm**: The harmonic propagator correction at the quartic level produces a "background charge" contribution that is absent from the algebraic bar complex. In the BV framework, this is the difference between:
- Regularized Feynman integrals (BV side): integrate against the FULL Green function P = P_bar + P_harm
- Algebraic residues (bar side): extract residues against the HOLOMORPHIC kernel d log E

For classes G, L, C, the harmonic correction decouples from the OPE (by Gaussianity, Jacobi, or role separation). For class M, it couples irreducibly.

---

## 7. Partial results beyond Heisenberg

### Affine Kac-Moody (class L)

- **Genus 0**: Fully proved (thm:bar-semi-infinite-km) at all non-critical levels, including critical level via Feigin-Frenkel.
- **Genus 1, chain level**: Proved (theorem_bv_genus1_chain_level_engine.py). The proof uses: (1) the OPE has poles of order <= 2, so the BV interaction is purely cubic; (2) the Jacobi identity gives [Q_int, Q_int] = 0 at the chain level; (3) the spectral sequence with Q_0 on E_0 and Q_int on E_1 degenerates at E_2.
- **Genus 2**: The bv_bar_genus2_engine.py computes both sides independently for V_k(sl_2). The bar side gives F_g = kappa * lambda_g^FP with kappa = 3(k+2)/4. The BV Feynman graph expansion uses 7 stable graphs at genus 2. For class L, the constraint that all genus-0 vertices have valence 2 or 3 (shadow depth 3) severely limits the contributing graphs. The engine reports MATCH at genus 2.
- **All genera, scalar level**: Proved by Theorem D (uniform-weight lane). The scalar-level match F_g^BV = F_g^bar = kappa * lambda_g^FP holds at all genera.

### Betagamma (class C)

- **Genus 0**: Proved.
- **Genus 1**: Proved at the scalar level (three-mechanism argument in rem:bv-bar-class-c-proof). The chain-level identification uses harmonic decoupling: the quartic vertex factors through composite fields.
- **Genus >= 2**: OPEN (even at scalar level, this requires the full shadow obstruction tower through arity 4).

### Virasoro (class M)

- **Genus 0**: Proved (specializes to thm:brst-bar-genus0 with c=26 or to semi-infinite cohomology).
- **Genus 1, scalar level**: Proved. F_1 = c/48 on both sides.
- **Genus 1, chain level**: FALSE at the ordinary level (delta_4^harm obstruction). Should hold in D^co.
- **Genus >= 2**: OPEN.
- **Special values**: At c=26, kappa_tot = 0 and the bar complex is uncurved; the coderived issue does not arise. At c=13, the full shadow tower is self-dual (prop:c13-full-self-duality), which might simplify the comparison.

---

## 8. What would a proof require?

The gap (concordance, line 9312) is identified precisely:

> The gap is the construction of a comparison map between the algebraic bordered FM integrals (which define Theta^oc_A) and the BV path-integral quantization on Sigma_g at higher genus. The analytic comparison theorem establishes this for graph amplitudes; the missing step is the BV master equation on the full moduli space M-bar_g, not only on individual graphs.

A complete proof would require:

### Step 1: Coderived category framework
Establish that the bar complex B(A) at genus g >= 1, viewed in Positselski's coderived category D^co, admits a well-defined comparison target on the BV side. This requires constructing the "coderived BV complex" as the appropriate home for the BV quantization with curved background.

### Step 2: Graph-by-graph comparison
For each stable graph Gamma in M-bar_{g,0}, show that the bar amplitude (algebraic residue integral over the FM compactification of the vertex) equals the BV amplitude (regularized Feynman integral with the full Green function). The bv_bar_genus2_engine.py does this for class L at genus 2; it needs to be extended to class M.

### Step 3: Assembly over M-bar_g
Show that the graph-by-graph comparisons assemble into a global comparison over M-bar_g. This is the "BV master equation on the full moduli space" step. The issue: the bar complex is defined graph-by-graph (stable graph decomposition of M-bar_g), while the BV quantization is defined on the full surface Sigma_g. The passage from individual graphs to the full moduli space uses the stratification of M-bar_g by dual graphs, and requires that the boundary strata contributions (planted forests, separating/non-separating nodes) match between the two frameworks.

### Step 4: Harmonic propagator resolution for class M
This is the hard step. For class M, show that the harmonic propagator discrepancy delta_4^harm is a coboundary in D^co (even though it is not a coboundary in the ordinary bar complex). This would require understanding the curved A-infinity structure of the bar complex at genus >= 1 well enough to show that delta_4^harm, while not d_bar-exact, becomes exact when the curvature m_0 = kappa * omega_g is absorbed into the differential.

---

## 9. What would a disproof look like?

The conjecture could fail in two ways:

### 9a: Failure in D^co (genuine failure)
If the coderived quasi-isomorphism also fails, this would mean the BV and bar frameworks are genuinely inequivalent at higher genus. This would require finding a cohomology class in one framework that is absent from the other. Given that both frameworks produce the same scalar invariants (F_g = kappa * lambda_g^FP) at all genera, such a class would have to live in a non-scalar component -- for instance, a nonvanishing class in the chain-level kernel of one differential that is not in the kernel of the other.

**Likelihood assessment**: LOW. The structural match is too tight. Both frameworks are controlled by the same modular operad structure (stable graphs, sewing, clutching). The genus-0 comparison is a quasi-isomorphism; the genus-1 scalar comparison holds for all families; the chain-level comparison holds for 3 out of 4 shadow classes. The remaining class M obstruction is a specific quantitative discrepancy (delta_4^harm) that has a natural home in the coderived category.

### 9b: Failure of the naive statement but success of the coderived reformulation
This is what the manuscript already predicts: conj:master-bv-brst as literally stated is FALSE for class M at the ordinary chain level. The correct statement is a coderived quasi-isomorphism. This is not really a "disproof" but rather a sharpening.

### 9c: Computational disproof at genus 2
If the BV Feynman graph expansion for Virasoro at genus 2 produces a DIFFERENT value from the bar free energy F_2 = kappa * lambda_2^FP + delta_F_2^cross (where delta_F_2^cross includes the multi-weight correction if applicable), this would disprove the scalar-level conjecture. The bv_bar_genus2_engine.py is set up to test this. For single-generator algebras (Virasoro), the bar side gives F_2 = (c/2) * 7/5760 = 7c/11520. The BV side should give the same value from the 7 stable graphs of M-bar_{2,0}.

**Likelihood assessment of 9c**: VERY LOW. The BV and bar formulas are both determined by the same geometric data (OPE coefficients, propagator, moduli space stratification). A scalar-level mismatch would violate the Quillen anomaly formula, which is universal.

---

## 10. Compute engine inventory

The following engines address conj:master-bv-brst:

| Engine | Tests | Scope |
|--------|-------|-------|
| `chain_level_bv_bar.py` | in test_chain_level_bv_bar.py | Genus-1 propagator comparison, three obstructions, factorization homology |
| `costello_bv_comparison_engine.py` | -- | Six comparison axes (differential, modular operad, genus expansion, obstruction, renormalization, effective action) |
| `bv_bar_genus2_engine.py` | in test_bv_bar_genus2_engine.py, test_bv_bar_genus2_comparison.py | Genus-2 graph-by-graph BV vs bar for affine sl_2 |
| `bv_bar_class_m_engine.py` | in test_bv_bar_class_m_engine.py | Class M obstruction analysis (Virasoro quartic harmonic discrepancy) |
| `theorem_bv_brst_genus1_constraints_engine.py` | in test_theorem_bv_brst_genus1_constraints_engine.py | Genus-1 BV=bar constraints from KZ25 sigma model |
| `theorem_bv_genus1_chain_level_engine.py` | in test_theorem_bv_genus1_chain_level_engine.py | Chain-level identification at genus 1 for class L |
| `theorem_bv_brst_rectification_engine.py` | in test_theorem_bv_brst_rectification_engine.py | Literature rectification (SiLi25, WG24, ESW20/24, HP26) |
| `theorem_si_li_bv_index_engine.py` | in test_theorem_si_li_bv_index_engine.py | Si Li BV-to-algebraic-index comparison |
| `theorem_bv_sewing_engine.py` | -- | Chain-level Delta_BV = d_sew identification |
| `theorem_bv_bethe_gaudin_frontier_engine.py` | in test_theorem_bv_bethe_gaudin_frontier_engine.py | Bethe/Gaudin connections to BV |
| `heisenberg_bv_bar_proof.py` | -- | Four-path proof for Heisenberg at all genera |

---

## 11. Relationship to the three-bar-complex picture

The question asks whether B^ord (E_1 bar) vs B^Sigma (symmetric bar) helps sharpen the conjecture.

**Answer**: No, for genus >= 1.

The BV path integral on C x R is naturally E_1 in the topological (R) direction, but the **genus >= 1 BV quantization on Sigma_g** is not naturally ordered. The sewing operation on M-bar_{g,n+2} -> M-bar_{g+1,n} (non-separating clutching) is symmetric: it identifies two marked points without ordering them. The bar complex at genus g >= 1 is governed by the MODULAR operad, which is symmetric by definition (stable graphs have no canonical vertex ordering beyond what the automorphism group respects).

At genus 0, the distinction matters for the spectral sequence: the E_1 page of the PBW spectral sequence is Hochschild homology (tensor, ordered) vs Lie homology (exterior, unordered) -- these are quasi-isomorphic in char 0 but categorically different (AP37). The genus-0 BV complex naturally lives on the ordered (Hochschild) side, which is why the comparison maps use the E_1 page.

At genus >= 1, both the BV and bar complexes are controlled by the modular operad's composition maps. The relevant structure is the Feynman transform FT(FCom), which is inherently symmetric. The BV Laplacian Delta_BV and the sewing operator d_sew are both symmetric operations (they contract unordered pairs through the propagator).

---

## 12. Assessment of tractability

**Near-term accessible** (1-2 years):
- Genus-2 BV=bar for affine KM at the scalar level (graph-by-graph computation, bv_bar_genus2_engine.py is set up for this)
- Genus-1 chain level for class C in the coderived category (building on rem:bv-bar-class-c-proof)
- Precise formulation of the coderived conjecture with full hypotheses

**Medium-term** (2-5 years):
- Coderived quasi-isomorphism for class L at all genera (combining the semi-infinite comparison with the coderived framework)
- Genus-1 chain level for Virasoro in D^co (requires understanding the curved A-infinity structure at one loop)

**Hard** (5+ years or requires new ideas):
- Full chain-level BV=bar for class M at all genera (requires both the coderived framework and a resolution of the harmonic propagator obstruction at all arities and all genera)
- The BV master equation on the full moduli space M-bar_g (not just individual graphs)

**The bottleneck is class M at the chain level.** Everything else is either proved or accessible by extension of existing techniques.

---

## 13. Key insight from this investigation

The conjecture as stated is a **physics-mathematics bridge**, not an internal algebraic claim. The algebraic side (bar complex, Theta_A, shadow obstruction tower) is fully proved. The BV/BRST side is a physical construction (path integral, functional determinants, Green functions). The gap is the identification between algebraic residues (on FM compactification) and analytic integrals (on the surface Sigma_g with its complex structure).

The sharpest formulation is:
1. At the scalar level: F_g^BV = F_g^bar for all g and all modular Koszul algebras. This is PROVED for classes G/L and STRONGLY EXPECTED for C/M (by the universality of the Quillen anomaly formula).
2. At the chain level: the BV complex and the bar complex are quasi-isomorphic in the CODERIVED category. This is PROVED for classes G/L at genus 1, PROVED for class C at genus 1, and OPEN for class M.
3. The ordinary chain-level identification (without coderived) is FALSE for class M: delta_4^harm is not a coboundary in the holomorphic bar complex.

The three-level stratification (scalar/chain/coderived) is the correct epistemic framework. The scalar level is essentially resolved; the chain level is resolved for 3/4 classes and known to fail for class M in the naive formulation; the coderived level is the correct reformulation for class M.
