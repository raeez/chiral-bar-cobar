# HITLIST: Platonic Ideal Mathematical Form
# Monograph: Modular Homotopy Theory for Factorization Algebras on Curves
# Generated: 2026-03-14 (Session 8)
# Scope: EVERYTHING. Trust nothing. Verify everything. Build what is missing.
#
# CURRENT STATE:
#   1700 tagged claims (1142 PH, 353 PE, 181 CJ, 27 HE, 0 OP)
#   125K lines of .tex across ~55 files
#   5100 test functions across 109 test files, 102 lib files
#   ~1516 pages compiled
#
# STRUCTURE:
#   PHASE A: VERIFY (audit every proved claim for correctness)
#   PHASE B: RESOLVE (promote conjectures / fill construction gaps)
#   PHASE C: COMPUTE (build computational evidence)
#   PHASE D: PERFECT (Chriss-Ginzburg-grade exposition)
#
# EXECUTION PROTOCOL FOR EACH ITEM:
#   1. Read the EXACT source (file:line). Never rely on memory.
#   2. Check conventions BEFORE reasoning (CLAUDE.md grading/sign section).
#   3. Verify formulas computationally when possible (sympy/sage).
#   4. If item is a proof: trace EVERY dependency. Read each cited result.
#   5. If item is a formula: derive independently OR verify numerically at 3+ points.
#   6. Record findings as PASS / ISSUE(description) / GAP(what's missing).
#   7. Do NOT fix anything until the full audit of that tier is complete.
#
# ANTI-FAILURE-MODE GUARDS:
#   - COHOMOLOGICAL convention: |d| = +1. Bar uses DESUSPENSION s^{-1}.
#   - Com^! = Lie (NOT coLie). Koszul dual coalgebra is SUB-coalgebra of cofree.
#   - Heisenberg NOT self-dual. Free fermion dual is beta-gamma.
#   - B_4 = B_8 = -1/30 (not an error).
#   - BV bracket degree +1 in cohomological convention (correct for this monograph).
#   - Sugawara UNDEFINED at k = -h^vee (not "c diverges").
#   - ~80% of findings will be false alarms. Triple-check before declaring error.
#   - NEVER change a verified formula. Compute or cite before touching.

---

## PHASE A: VERIFICATION

### A.0 CONVENTIONS AND FOUNDATIONS

A.0.1  [SIGN] Verify cohomological grading |d|=+1 is used consistently in ALL
       chapter files. Search for homological-convention artifacts: d of degree -1,
       bar using suspension instead of desuspension, shifted complexes V[n] with
       wrong sign convention.
       FILES: all chapters/*.tex
       METHOD: grep for 'degree.*-1', 'suspension', 's\^{1}', check each instance

A.0.2  [SIGN] Verify the bar differential sign convention
       d_bar = sum (-1)^{rs+t} m_{r+1+t}(id^r tensor m_s tensor id^t)
       is used consistently. Check that the specific sign (-1)^{rs+t} matches
       Loday-Vallette converted to cohomological convention.
       FILES: algebraic_foundations.tex, bar_cobar_construction.tex
       METHOD: read the definition, trace through one example (Heisenberg bar)

A.0.3  [SIGN] Verify curved A-infinity sign: m_1^2(a) = m_2(m_0,a) - m_2(a,m_0)
       (MINUS sign = commutator, not anticommutator). Check every appearance.
       FILES: higher_genus.tex, bar_cobar_construction.tex, algebraic_foundations.tex

A.0.4  [CONV] Verify Koszul dual identification Com^! = Lie throughout.
       Search for any instance of Com^! = coLie or other error.
       FILES: all theory/*.tex, chiral_koszul_pairs.tex

A.0.5  [CONV] Verify bar complex desuspension convention B(A) = T^c(s^{-1}A-bar)
       throughout. Check that s^{-1} (not s) is used.
       FILES: bar_cobar_construction.tex, algebraic_foundations.tex

A.0.6  [CONV] Verify H/M/S semantic level labels are correctly applied.
       Check that "H-level" is never used for model-level constructions, etc.
       FILES: concordance.tex, bar_cobar_construction.tex, higher_genus.tex

A.0.7  [CONV] Verify differential notation: \dfib, \Dg{g}, \dzero are used
       correctly and consistently. Check d_fib^2 = kappa * omega_g (not =0).
       FILES: higher_genus.tex, bar_cobar_construction.tex

A.0.8  [CONV] Verify Feigin-Frenkel level shift is k <-> -k-2h^vee throughout
       (NOT -k-h^vee). Search for every occurrence.
       FILES: kac_moody_framework.tex, w_algebras_framework.tex, w_algebras_deep.tex,
              chiral_koszul_pairs.tex

A.0.9  [CONV] Verify Sugawara formula: T = 1/(2(k+h^vee)) sum :J^a J^a:
       and c = k*dim(g)/(k+h^vee). Check every occurrence.
       FILES: kac_moody_framework.tex, free_fields.tex

A.0.10 [CONV] Verify DS central charge formulas:
       Virasoro: c = 1 - 6(k+1)^2/(k+2)
       W_3: c = 2 - 24(k+2)^2/(k+3)
       General W_N: use the correct general formula
       FILES: w_algebras_framework.tex, w_algebras_deep.tex
       METHOD: verify with compute/lib sympy at 5 values of k each

A.0.11 [CONV] Verify c+c' complementarity sums:
       Virasoro: 26. KM: 2*dim(g). W_3: 100. W_4: 246.
       FILES: examples_summary.tex, w_algebras_deep.tex, kac_moody_framework.tex
       METHOD: verify with compute/ at 3 values of k each

A.0.12 [CONV] Verify kappa formulas:
       kappa(Vir) = c/2. kappa(g-hat_k) = (k+h^vee)d/(2h^vee).
       kappa(W_N) = c*(H_N - 1). kappa(bc) = c/2. kappa(betagamma) = -c/2.
       FILES: higher_genus.tex, genus_expansions.tex, free_fields.tex
       METHOD: cross-check each with compute/lib invariant_machine

A.0.13 [INDEX] Verify notation index (appendices/notation_index.tex) is complete
       and consistent with actual usage. Check 20 randomly selected macros.

A.0.14 [XREF] Run LaTeX and check for undefined references. Count them.
       METHOD: grep for '??' in .log file after make fast

---

### A.1 CORE THEOREM A: BAR-COBAR ADJUNCTION

A.1.1  [PROOF] Read thm:bar-cobar-isomorphism-main in full. Trace every
       \ref{} in the proof. Verify each cited result exists and says what
       the proof claims it says.
       FILE: bar_cobar_construction.tex
       DEPENDENCIES: must read every cited proposition/lemma

A.1.2  [PROOF] Verify the geometric bar construction on FM compactifications
       is correctly defined. Check: FM_n(X) = blowup (NOT X^n \ Delta).
       Check: the bar differential is the Poincare residue on boundary divisors.
       FILE: configuration_spaces.tex, bar_cobar_construction.tex

A.1.3  [PROOF] Verify the cobar construction. Check: Omega(C) = free algebra
       on s*C-bar with twisted differential. Check: desuspension/suspension
       conventions match.
       FILE: bar_cobar_construction.tex

A.1.4  [PROOF] Verify the adjunction: bar is left adjoint to cobar (or right
       adjoint, depending on convention). Check that the unit/counit are
       correctly defined.
       FILE: bar_cobar_construction.tex

A.1.5  [PROOF] Verify the Koszul equivalence criterion: bar-cobar counit is
       a QI iff A is Koszul. Check this is proved, not just stated.
       FILE: bar_cobar_construction.tex

A.1.6  [COMP] Run all bar-cobar tests:
       cd compute && .venv/bin/python -m pytest tests/test_bar_*.py -v

A.1.7  [COMP] Verify the bar complex of the Heisenberg algebra explicitly.
       Compute B_1, B_2, B_3 and check dimensions match the text.
       FILE: heisenberg_frame.tex, compute/lib/

---

### A.2 CORE THEOREM B: BAR-COBAR INVERSION

A.2.1  [PROOF] Read thm:higher-genus-inversion in full. Trace every \ref{}.
       FILE: higher_genus.tex (or bar_cobar_construction.tex -- locate it)

A.2.2  [PROOF] Verify the E_2 spectral sequence collapse. What filtration
       is used? Is the degeneration proved or assumed? Check the E_2 page
       computation.

A.2.3  [PROOF] Verify the genus-g correction: the bar-cobar QI at genus g
       involves the corrected differential D_g. Check d_fib^2 = kappa*omega_g
       is proved.
       FILE: higher_genus.tex

A.2.4  [COMP] Run genus-related tests:
       cd compute && .venv/bin/python -m pytest tests/test_genus*.py -v

---

### A.3 CORE THEOREM C: QUANTUM COMPLEMENTARITY

A.3.1  [PROOF] Read thm:quantum-complementarity-main in full.
       Statement: Q_g(A) + Q_g(A!) = H*(M_g, Z(A)).
       Verify each term is correctly defined. Verify the proof.
       FILE: higher_genus.tex (or poincare_duality_quantum.tex)

A.3.2  [PROOF] Verify the Verdier duality argument. Check:
       Verdier duality on FM compactification, NOT Stokes.
       D-module adjointness, NOT integration by parts.
       FILE: poincare_duality.tex, poincare_duality_quantum.tex

A.3.3  [PROOF] Verify the center local system Z(A) is correctly defined
       and the pushforward R^0 pi_* B-bar^(g)(A) = Z(A) is proved.
       FILE: higher_genus.tex

A.3.4  [COMP] Verify complementarity for Heisenberg, KM (sl_2), W_3:
       Q_g + Q_g^! = expected value
       METHOD: compute/tests/test_complementarity or test_cross_algebra

A.3.5  [FORMULA] Verify the FP formula:
       integral_{M-bar_{g,1}} psi_1^{2g-2} lambda_g = (2^{2g-1}-1)/(2^{2g-1}) * |B_{2g}|/(2g)!
       at g=1,2,3 numerically.

---

### A.4 CORE THEOREM D: MODULAR CHARACTERISTIC

A.4.1  [PROOF] Read thm:modular-characteristic (D_scal) in full.
       Statement: kappa(A) is universal, additive, anti-symmetric, A-hat GF.
       FILE: higher_genus.tex

A.4.2  [PROOF] Verify universality: kappa depends only on the chiral algebra,
       not on the curve. Check the proof uses only deformation-theoretic data.

A.4.3  [PROOF] Verify additivity: kappa(A tensor B) = kappa(A) + kappa(B).
       Check the proof, check examples.

A.4.4  [PROOF] Verify anti-symmetry: kappa(A) + kappa(A!) = c+c'/2 or
       whatever the correct formula is. Check against known values.

A.4.5  [PROOF] Verify the A-hat generating function identification.
       FILE: higher_genus.tex, genus_expansions.tex

A.4.6  [PROOF] Read the spectral characteristic D_Delta. Verify the
       spectral discriminant Delta_A(x) is correctly defined and computed
       for Heisenberg, KM, W_3.
       FILE: higher_genus.tex, examples_summary.tex

A.4.7  [COMP] Verify kappa values computationally for ALL families:
       Heisenberg, bc, betagamma, free fermion, KM (sl_2 through sl_5),
       W_3, W_4, W_5.
       METHOD: compute/tests/test_genus.py, test_chiral_invariant_machine.py

---

### A.5 MC1: PBW CONCENTRATION (thm:master-pbw)

A.5.1  [PROOF] Read thm:master-pbw in full. Statement: PBW spectral sequence
       degenerates for KM, Virasoro, principal W_N at generic level.
       Verify the E_2 page identification. Verify degeneration.
       FILE: bar_cobar_construction.tex (locate it)

A.5.2  [PROOF] Trace the dependency on the PBW filtration definition.
       Check that the filtration is compatible with the bar differential.
       Check that gr(B(A)) has the correct Hilbert series.

A.5.3  [PROOF] Verify the Hilbert series comparison: the bar Hilbert series
       matches the Koszul dual Hilbert series. Check for KM (sl_2).
       METHOD: compute/lib bar_gf or hilbert_series

A.5.4  [CAVEAT] Check the caveat: PBW SS does NOT automatically degenerate
       at E_3 for "quadratic OPE" -- composites have higher poles from
       double Wick contractions. Verify this caveat is correctly stated
       and does not affect the proved cases.

---

### A.6 MC2: CYCLIC L-INFINITY AND THETA_A (thm:mc2-full-resolution)

A.6.1  [PROOF] Read thm:mc2-full-resolution in full. What are the three
       packages resolved? Read each sub-theorem.
       FILE: higher_genus.tex (or deformation_theory.tex)

A.6.2  [PROOF] Read thm:universal-theta. Verify the universal MC class
       Theta_A is correctly constructed via cyclic L-infinity homotopy
       transfer.
       FILE: higher_genus.tex

A.6.3  [PROOF] Verify the scalar saturation theorem: when dim H^2_cyc = 1,
       Theta = kappa * eta tensor Lambda. Check the proof.
       FILE: higher_genus.tex:14760-14794

A.6.4  [PROOF] Verify the obstruction nilpotence result. Check that it uses
       Mumford's relation c(E)c(E^v) = 1. Check it works for ALL genera
       (was previously only conjecture for g >= 3).
       FILE: higher_genus.tex

---

### A.7 DS-KD INTERTWINING (thm:ds-koszul-intertwine)

A.7.1  [PROOF] Read thm:ds-koszul-intertwine proof at chiral_modules.tex:4223-4266.
       Verify: (a) Q_DS commutes with d_bar -- this requires n_+ action commuting
       with OPE-residue operations. Is this proved or just stated?
       (b) DS vanishing theorem -- is this proved or cited? If cited, verify the
       citation is correct.
       (c) Spectral sequence degeneration -- is the E_1 differential correctly
       identified as Q_DS? Is the vanishing of higher cohomology correctly used?

A.7.2  [PROOF] Verify cor:ds-bar-level-shift (chiral_modules.tex:4311).
       The composition of DS intertwining with level-shifting duality.
       Check: k' = -k - 2h^vee (NOT -k - h^vee).

A.7.3  [PROOF] Verify the character formula cor:ds-character-compatibility.
       Check the ghost Euler characteristic formula. Verify at sl_2, k=1.

A.7.4  [GAP] The proof of A.7.1(a) says "the BRST operator involves the n_+
       action, which commutes with the OPE-residue operations defining d_bar."
       This is a non-trivial claim. Verify it: the BRST differential Q_DS
       = sum e_alpha * J^alpha + ... involves the nilpotent n_+ currents.
       The bar differential involves OPE residues on configuration spaces.
       Their commutativity should follow from the fact that the n_+ action
       is an algebra action (not an OPE action), but this deserves a careful
       argument. Check if one exists.

---

### A.8 W-INFINITY FACTORIZATION KOSZUL DUAL (thm:winfty-factorization-kd)

A.8.1  [PROOF] Part (i): Sectorwise finiteness. The argument at
       w_algebras_deep.tex:870-882 says compositions of h into parts from
       {2,...,N} are bounded by p(h). Verify this counting argument.
       Is the bound sharp? Is it independent of n for n > h/2?

A.8.2  [PROOF] Part (i): Factorization descent from Ran_1 to Ran(X).
       The argument at w_algebras_deep.tex:910-932 uses Kunneth on disjoint
       opens + cosheaf descent. Verify: does Kunneth preserve QI over a field
       for completed objects? Is cosheaf descent proved or cited?

A.8.3  [PROOF] Part (ii): DS-KD identification (W_N^k)^! = sl_{N,-k-2N}-hat.
       Verify the partition transpose argument: (N)^t = (1^N), DS at zero
       nilpotent = identity. Composed with FF level shift.
       Check for N=3,4 explicitly.

A.8.4  [PROOF] Part (iii): Completed inverse limit. Verify Mittag-Leffler.
       The proof at w_algebras_deep.tex:934-955 cites cor:winfty-standard-mc4-package.
       Trace the dependency chain: cor:winfty-weight-cutoff -> prop:mc4-weight-cutoff.
       Verify each step.

A.8.5  [PROOF] Part (iii): "surjectivity is preserved by tensor products over
       a field" -- verify this is correct for the factorization-level application.
       The tensor products are over disjoint opens in Ran(X); verify that the
       relevant topological tensor product preserves surjectivity.

A.8.6  [PROOF] Part (iv): C^res = C^DS. Verify the chain:
       thm:ds-koszul-intertwine -> chain-level iso B_W(W_N) = H^0_DS(B(sl_N))
       -> residue coefficients are entries of the same complex.
       Check: is "chain-level isomorphism" the correct term? Is it a QI or
       a strict isomorphism? If only a QI, does the coefficient identification
       still hold?

A.8.7  [COMP] Verify thm:winfty-factorization-kd computationally:
       - Stage-3 packet: DONE (verified in audit)
       - Stage-4 six-entry packet: verify DS-side values
       - c334^2, c444^2: verified symbolically (audit)
       - C_{4,4;2;0,6} = 2, C_{3,4;2;0,5} = 0: verify

---

### A.9 M-LEVEL MC4 MACHINERY (bar_cobar_construction.tex:5400-5900)

A.9.1  [PROOF] prop:mc4-reduction-principle (line 5414). Verify the general
       inverse-limit bar-cobar reduction. Check Milnor exact sequence usage.

A.9.2  [PROOF] cor:mc4-degreewise-stabilization (line 5498). Verify that
       degreewise stabilization of bar cohomology implies completed QI.

A.9.3  [PROOF] cor:mc4-surjective-criterion (line 5535). Verify that
       eventual surjectivity on finite-dimensional weight slices suffices.

A.9.4  [PROOF] prop:mc4-weight-cutoff (line 5573). Verify the stabilization
       N >= w for weight-cutoff towers.

A.9.5  [PROOF] prop:winfty-mc4-criterion (line 5622). Verify all three
       hypotheses are satisfied by the standard principal tower.

A.9.6  [PROOF] cor:winfty-weight-cutoff (line 5673). Verify the explicit
       weight-cutoff stabilization for the W_N tower.

A.9.7  [PROOF] cor:winfty-standard-mc4-package (line 5770). Verify the
       assembly: all hypotheses -> completed QI.

A.9.8  [PROOF] prop:completed-target-comparison (line 5804). Verify the
       general comparison theorem for completed targets.

A.9.9  [PROOF] cor:winfty-hlevel-comparison-criterion (line 5882). Verify
       the criterion: what exactly must W^{ht} satisfy?

---

### A.10 STAGE-4 PACKET ANALYSIS (bar_cobar_construction.tex:6100-8700)

A.10.1  [PROOF] Read and verify ALL ~40 propositions/corollaries in this range.
        For each: check the proof cites valid results, check the logic,
        check the combinatorial counting.
        This is the most technically dense section of the monograph.
        Do it item by item, recording PASS/ISSUE for each.

A.10.2  [PROOF] prop:winfty-ds-generator-seed (line 6381). Verify the
        generator seed reduction: comparison reduces to primary coefficients.

A.10.3  [PROOF] cor:winfty-ds-finite-seed-set (line 6434). Verify the
        seed set enumeration. Cross-check with compute/lib/w4_stage4_coefficients.py.

A.10.4  [PROOF] prop:winfty-ds-stage3-explicit-packet (line 6856). Verify
        the 15-entry packet, 3 nonzero, 12 zero. DONE in audit.

A.10.5  [PROOF] prop:winfty-ds-stage4-residual-packet (line 6952). Verify
        the residual packet after removing Virasoro/W3 sectors.

A.10.6  [PROOF] cor:winfty-ds-stage4-five-plus-zero (line 7726). Verify
        the five-plus-zero decomposition.

A.10.7  [PROOF] prop:winfty-mc4-frontier-package (line 7793). Verify the
        exact six-entry identity packet.

A.10.8  [PROOF] cor:winfty-stage4-residue-four-channel (line 7952). Verify
        the Ward-normalized contraction from 6 to 4 channels.

A.10.9  [PROOF] All visible pairing propositions (lines 8011-8700).
        Verify the orthogonality, W3 normalization, pairing reduction,
        primitive-transport-square-triple, Borcherds two-primitive results.

---

### A.11 STAGE-5 PACKET ANALYSIS (bar_cobar_construction.tex:8700-11100)

A.11.1  [PROOF] Verify ALL ~60 propositions/corollaries/conjectures in
        this range. The stage-5 analysis is even more technically dense.
        Focus on: are the packet decompositions correct? Do the target
        corridors correctly exhaust the packet? Is the single-effective-
        coefficient reduction valid?

A.11.2  [PROOF] prop:winfty-stage5-one-coefficient-reduction (line 10561).
        This is the key result: the full visible-pairing stage-5 comparison
        reduces to C^res_{3,5;4;0,4}(5) = C^DS_{3,5;4;0,4}(5).
        Verify the entire reduction chain leading to this.

A.11.3  [STATUS] Count and catalog all 18 stage-5 conjectures. For each,
        determine: is it purely structural (about the principal DS side)?
        Or does it require the missing H-level target? Or is it an
        independent W-algebra identity that could be proved by OPE methods?

---

### A.12 HEISENBERG FRAME (chapters/frame/heisenberg_frame.tex)

A.12.1  [PROOF] Verify the Heisenberg frame atom is correctly constructed.
        Check: H is NOT self-dual (H^! = Sym^ch(V*) with curvature).
        Check the curvature computation.

A.12.2  [PROOF] Verify the bar complex of H explicitly at low degrees.
        Check: B_1(H), B_2(H), B_3(H) dimensions and differentials.

A.12.3  [COMP] Run Heisenberg tests:
        cd compute && .venv/bin/python -m pytest tests/ -k 'heisenberg' -v

---

### A.13 KAC-MOODY EXAMPLES

A.13.1  [PROOF] Verify the Kac-Moody bar complex construction. Check:
        the bar differential involves ALL OPE poles (Borcherds), not just
        the Lie bracket.

A.13.2  [PROOF] Verify the 2048-sign computation: d_bracket^2 != 0 but
        d_bracket + d_curvature has d^2 = 0.
        FILE: kac_moody_framework.tex

A.13.3  [PROOF] Verify the KM Koszul duality:
        (g-hat_k)^! = g-hat_{-k-2h^vee} at the M-level.
        Check the level shift formula.
        FILE: chiral_koszul_pairs.tex

A.13.4  [PROOF] Verify the KM PBW (MC1): PBW spectral sequence degenerates.
        Check: is the associated graded identified with the symmetric algebra?

A.13.5  [COMP] Run KM tests:
        cd compute && .venv/bin/python -m pytest tests/ -k 'km or kac_moody or sl2 or sl3' -v

---

### A.14 W-ALGEBRA EXAMPLES

A.14.1  [PROOF] Verify the DS construction of W_3 from sl_3-hat. Check:
        the BRST complex, the ghost system, the strong generators T, W.
        FILE: w_algebras_framework.tex

A.14.2  [PROOF] Verify the explicit W_3 OPE: all pole orders and coefficients.
        Check: W(z)W(w) OPE has Lambda = :TT: - (3/10)d^2T with MINUS sign.
        FILE: w3_composite_fields.tex, w_algebras_deep.tex

A.14.3  [PROOF] Verify the W_3 central charge formula:
        c = 2 - 24(k+2)^2/(k+3).
        Check at k = 0, 1, -1, -5/2.
        FILE: w_algebras_framework.tex

A.14.4  [PROOF] Verify the W_3 Koszul duality:
        (W_3^k)^! = sl_{3,-k-6}-hat.
        Check the level shift.
        FILE: w_algebras_deep.tex

A.14.5  [PROOF] Verify the W_4 construction and OPE (as much as exists).
        FILE: w_algebras_deep.tex, w4_stage4_coefficients.py

A.14.6  [COMP] Run W_3/W_4 tests:
        cd compute && .venv/bin/python -m pytest tests/ -k 'w3 or w4' -v

---

### A.15 YANGIAN EXAMPLES

A.15.1  [PROOF] Verify thm:yangian-koszul-dual. The Yangian Koszul duality
        Y(g) <-> Y_{R^{-1}}(g). Check the R-matrix duality.
        FILE: yangians.tex

A.15.2  [PROOF] Verify the DK ladder: DK-0/1 proved, DK-1.5 lattice proved,
        DK-2/3 proved on evaluation-generated core.
        FILE: yangians.tex

A.15.3  [PROOF] Verify the RTT realization and boundary strip identities.
        FILE: yangians.tex

A.15.4  [PROOF] Verify the completed Yangian bar-cobar QI
        (cor:completed-bar-cobar-yangian). Same ML argument as W-infinity.
        FILE: yangians.tex

A.15.5  [COMP] Run Yangian tests:
        cd compute && .venv/bin/python -m pytest tests/ -k 'yangian' -v

---

### A.16 FREE FIELD EXAMPLES

A.16.1  [PROOF] Verify bc system: F^! = beta-gamma (Lie<->Com duality).
        NOT Heisenberg. Check the duality table.
        FILE: free_fields.tex, chiral_koszul_pairs.tex

A.16.2  [PROOF] Verify free fermion: check that bc-betagamma is a
        2-generator duality (dim V = 2). Bosonization != Koszul duality.
        FILE: free_fields.tex

A.16.3  [PROOF] Verify lattice VOA constructions.
        FILE: lattice_foundations.tex

A.16.4  [COMP] Run free field tests:
        cd compute && .venv/bin/python -m pytest tests/ -k 'free_field or bc or beta_gamma or fermion' -v

---

### A.17 CONFIGURATION SPACES AND GEOMETRY

A.17.1  [PROOF] Verify FM compactification: C-bar_n(X) = blowup.
        Check: it is NOT X^n \ Delta.
        FILE: configuration_spaces.tex

A.17.2  [PROOF] Verify Arnold relations and their role in the bar complex.
        FILE: configuration_spaces.tex, appendices/arnold_relations.tex

A.17.3  [PROOF] Verify normal bundle: N_{Delta_S/X^n} = direct-sum T_X
        (tangent, NOT cotangent).
        FILE: configuration_spaces.tex

A.17.4  [PROOF] Verify the prime form E(z,w) section:
        K^{-1/2} boxtimes K^{-1/2} (NOT K^{+1/2}).
        FILE: configuration_spaces.tex or higher_genus.tex

A.17.5  [PROOF] Verify boundary divisor classes: [Delta_I] in H^2
        (codimension 1, NOT H^{2|I|-2}).
        FILE: configuration_spaces.tex

---

### A.18 CONNECTIONS (Part 3)

A.18.1  [PROOF] Verify BV/BRST = bar at genus 0.
        FILE: bv_brst.tex

A.18.2  [PROOF] Verify BV antibracket degree: +1 in cohomological convention.
        FILE: bv_brst.tex

A.18.3  [PROOF] Verify QME: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2).
        FILE: bv_brst.tex, physical_origins.tex

A.18.4  [PROOF] Verify HCS action coefficient: 2/3 (not 1/3).
        FILE: holomorphic_topological.tex

A.18.5  [PROOF] Verify Feynman diagram identification with bar complex.
        FILE: feynman_diagrams.tex, feynman_connection.tex

A.18.6  [PROOF] Verify the concordance (constitution) is consistent with
        all chapter-level statements. Read concordance.tex in full and
        cross-check 20 key claims against their source locations.
        FILE: concordance.tex

---

### A.19 APPENDICES

A.19.1  [PROOF] Verify all sign conventions in appendices/sign_conventions.tex
        and appendices/signs_and_shifts.tex. Cross-check with CLAUDE.md.

A.19.2  [PROOF] Verify spectral sequence appendix.
        FILE: appendices/spectral_sequences.tex

A.19.3  [PROOF] Verify homotopy transfer appendix.
        FILE: appendices/homotopy_transfer.tex

A.19.4  [PROOF] Verify nilpotent completion appendix.
        FILE: appendices/nilpotent_completion.tex

A.19.5  [PROOF] Verify computational tables appendix against compute/ output.
        FILE: appendices/computational_tables.tex

---

## PHASE B: RESOLVE (promote conjectures, fill gaps)

### B.1 H-LEVEL TARGET CONSTRUCTION

B.1.1  [CONSTRUCT] Build W^{ht} explicitly via the Miura map.
       Approach: the Miura map at stage N embeds W_N -> Heis^{N-1}.
       The completed product Heis^{infinity} gives a separated complete target.
       Equip with the conformal weight filtration.
       Verify: finite quotients recover W_N.
       FILE TARGET: w_algebras_deep.tex (new section)

B.1.2  [CONSTRUCT] Alternative: build W^{ht} as the factorization algebra
       on Ran(X) associated to the pro-nilpotent completed bar complex.
       This reverses the logic: define W^{ht} := Omega(B-hat(W_infinity))
       and prove it has the required properties.
       Advantage: the M-level package is already proved.
       Disadvantage: circularity risk.

B.1.3  [CONSTRUCT] Verify that the quotient system hypothesis
       (def:winfty-quotient-system, bar_cobar_construction.tex:5953)
       is satisfied by the Miura realization.

B.1.4  [PROVE] Promote conj:winfty-stage4-ward-inheritance
       (bar_cobar_construction.tex:8281) to a theorem. This is the key
       missing lemma for the 6-to-4 channel contraction.
       Approach: the Ward identities are constraints from the Virasoro
       subalgebra action on the higher-spin generators. They should follow
       from the standard Virasoro representation theory.

---

### B.2 H^2_CYC COMPUTATION

B.2.1  [COMPUTE] Compute dim H^2_cyc(W_infinity) in the inverse limit.
       Step 1: The BRST pullback map H^2_cyc(W_N) -> H^2_cyc(sl_N) is
       an injection for each N (proved in higher_genus.tex:15340-15366).
       Step 2: By stability of Lie algebra cohomology, H^3(sl_N) = C
       for all N >= 2. Hence H^2_cyc(sl_N, sl_N) = C for all N.
       Step 3: The transition maps W_{N+1} -> W_N induce maps on H^2_cyc.
       Since dim = 1 at each stage, these maps are either 0 or isomorphisms.
       Step 4: They are isomorphisms (the central charge deformation
       direction is compatible with truncation).
       Conclusion: dim H^2_cyc(W_infinity) = lim dim H^2_cyc(W_N) = 1.

B.2.2  [CONSEQUENCE] If B.2.1 gives dim = 1, then:
       W_infinity is scalar-saturated.
       The non-scalar Theta_A programme cannot be realized via W_infinity.
       The monograph must honestly record this.
       Update raeeznotes34.md with the result.

B.2.3  [ALTERNATIVE] If the non-scalar programme is to survive, identify
       alternative sources:
       (a) Non-type-A W-algebras (e.g., W(so_N, f) with non-principal f)
       (b) Tensor products (Kunneth gives dim = r for r-fold products)
       (c) Non-DS constructions (e.g., lattice VOAs at higher rank)
       (d) The W_infinity TOWER as an E_1-algebra (not individual W_N)
       For each, compute or estimate dim H^2_cyc.

---

### B.3 BAR-SIDE RESIDUE EXTRACTION

B.3.1  [BUILD] Extend compute/lib/km_chiral_bar.py to handle W_3.
       The W_3 bar complex at degree 2 has chains:
       B_2(W_3) = span{T* tensor T*, T* tensor W*, W* tensor T*, W* tensor W*}
       graded by conformal weight.
       The bar differential d: B_2 -> B_1 is the Poincare residue of the OPE.
       Compute d explicitly and extract C^res coefficients.

B.3.2  [BUILD] Extend to W_4 at degree 2. This is more involved:
       generators T, W^3, W^4 give 6 types of degree-2 chains.
       Compute d from the W_4 OPE.

B.3.3  [VERIFY] Compare C^res (from bar-side extraction) with C^DS (from
       DS-side extraction) for the stage-3 packet (15 entries).
       This is the first independent verification of thm:ds-koszul-intertwine.

B.3.4  [VERIFY] Compare for the stage-4 six-entry packet.

---

### B.4 DS DERIVATION OF STRUCTURE CONSTANTS

B.4.1  [DERIVE] Derive c334^2 from the explicit DS BRST complex for sl_4.
       Method: construct the W_4 BRST complex explicitly, normal-order the
       ghost currents, extract the W^3 x W^3 OPE, isolate the W^4 channel
       at pole 2, compute the coefficient as a function of k (hence c).
       This is a substantial computation but well-defined.

B.4.2  [DERIVE] Similarly derive c444^2 (W^4 x W^4 -> W^4 self-coupling).

B.4.3  [DERIVE] Derive C_{3,4;3;0,4} and C_{3,4;4;0,3} from the DS complex.

B.4.4  [VERIFY] Cross-check all derived values against the Hornfeck formulas.

---

### B.5 PROMOTE STAGE-4 CONJECTURES

B.5.1  [PROVE] conj:winfty-stage4-visible-diagonal-normalization
       (bar_cobar_construction.tex:8253)

B.5.2  [PROVE] conj:winfty-stage4-ward-inheritance
       (bar_cobar_construction.tex:8281)

B.5.3  [PROVE] conj:winfty-stage4-visible-borcherds-transport
       (bar_cobar_construction.tex:8591)

For each: read the conjecture statement, identify what would constitute a proof
(OPE bootstrap? Jacobi identity? Direct computation?), and attempt it.

---

### B.6 PROMOTE STAGE-5 CONJECTURES

B.6.1  [PROVE] The 18 stage-5 conjectures at bar_cobar_construction.tex:10329-10932.
       Prioritize:
       - conj:winfty-stage5-principal-one-coefficient-normal-form (10496)
       - conj:winfty-stage5-one-coefficient-comparison (10590)
       These are the two that, if proved, would resolve stage-5.

B.6.2  [COMPUTE] Verify C^DS_{3,5;4;0,4}(5) computationally. This requires
       the explicit W_5 OPE at spin 5, which is not yet in compute/.
       Building the W_5 OPE module would be a major computational task.

---

### B.7 FACTORIZATION DESCENT EXPANSION

B.7.1  [EXPAND] Expand the proof of Part (iii) of thm:winfty-factorization-kd.
       Spell out: the Milnor exact sequence at the Ran-stratum level,
       the tensor product decomposition at each stratum, the compatibility
       with the inverse system, and the resulting lim^1 vanishing.
       This should be ~1 page of additional argument.

---

### B.8 YANGIAN-W_INFINITY BRIDGE

B.8.1  [CONSTRUCT] Build a functorial connection between the W_infinity and
       Yangian MC4 towers. The natural candidate: the Schur-Weyl functor
       that relates W-algebras (vertex algebra side) to Yangians (quantum
       group side). At the level of categories, this is the Arakawa-Frenkel
       functor. Formalize this as a commutative diagram of MC4 reductions.

B.8.2  [PROVE] Show that the Schur-Weyl functor intertwines the finite-detection
       packets: I_N on the W-infinity side and Delta_{a,0}(N) on the Yangian side.

---

### B.9 PERIODICITY

B.9.1  [VERIFY] The periodicity profile Pi_A is correctly defined and computed
       for all families. Check that the statement "KM periodicity is 2h (Coxeter),
       NOT 2h^vee" is correctly applied.
       FILE: higher_genus.tex, modular_periodicity tests

B.9.2  [VERIFY] "Rank>1: period 2h for all g is WRONG" -- check this caveat
       is correctly handled in the text.

---

## PHASE C: COMPUTE (build computational evidence)

### C.1 NEW COMPUTE MODULES

C.1.1  [BUILD] compute/lib/w3_bar_complex.py: explicit bar complex of W_3
       at degree 2, with bar differential from OPE residues. Extract C^res.

C.1.2  [BUILD] compute/lib/w4_bar_complex.py: same for W_4.

C.1.3  [BUILD] compute/lib/w5_ope.py: W_5 OPE algebra (at least the
       primary coefficients needed for stage-5 verification).

C.1.4  [BUILD] compute/lib/w_algebra_ds_brst.py: explicit DS BRST complex
       for sl_N at general N, extracting W-algebra OPE coefficients from
       the BRST construction.

C.1.5  [BUILD] compute/lib/cyclic_cohomology.py: compute H^2_cyc(W_N, W_N)
       explicitly for N = 2, 3, 4, 5 and verify dim = 1.

C.1.6  [BUILD] compute/lib/miura_map.py: the Miura embedding W_N -> Heis^{N-1}
       at each stage. Verify compatibility with truncation.

---

### C.2 NEW TESTS

C.2.1  [TEST] test_w3_bar_complex.py: bar-side C^res extraction at stage 3.
       Compare with stage3_ds_coefficients() from w4_stage4_coefficients.py.

C.2.2  [TEST] test_w4_bar_complex.py: bar-side C^res at stage 4.
       Compare with DS-side extraction.

C.2.3  [TEST] test_ds_brst_ope.py: derive c334^2, c444^2 from the
       BRST complex. Compare with Hornfeck values.

C.2.4  [TEST] test_cyclic_cohomology.py: verify dim H^2_cyc = 1 for
       W_3, W_4, W_5 by explicit BRST pullback.

C.2.5  [TEST] test_miura_map.py: verify Miura embedding properties.

C.2.6  [TEST] test_factorization_descent.py: verify Kunneth and lim^1 = 0
       for a toy model (e.g., a 2-generator tower).

---

### C.3 EXISTING TEST AUDIT

C.3.1  [AUDIT] Review every test file in compute/tests/. For each:
       - Is it testing the correct mathematical statement?
       - Is the test meaningful (not tautological)?
       - Does it verify a manuscript claim, and if so which one?
       - Are there edge cases that should be tested?
       This produces a test-to-claim coverage matrix.

C.3.2  [AUDIT] Identify manuscript claims with NO computational verification.
       Prioritize building tests for these.

---

### C.4 FORMULA VERIFICATION SWEEP

C.4.1  [VERIFY] Every formula in CLAUDE.md "Critical Pitfalls" section.
       Verify each formula computationally at 3+ values.

C.4.2  [VERIFY] Every formula in the "Known Verified Formulas" memory.
       Re-derive or verify each.

C.4.3  [VERIFY] The Mumford isomorphism formula:
       c_1(pi_* omega^{tensor h}) = (6h^2 - 6h + 1) lambda on M-bar_{1,1}.
       lambda_1^{(2)} = 13/24, lambda_1^{(3)} = 37/24.
       Verify at h = 1, 2, 3.

C.4.4  [VERIFY] K_N = 4N^3 - 2N - 2 for N = 2, 3, 4, 5.
       Check: K_2 = 26 (Virasoro), K_3 = 100 (W_3), K_4 = 246 (W_4).

C.4.5  [VERIFY] sigma(E_8) = 121/126 (NOT 31/15).
       Verify: sigma = sum 1/(m_i + 1) where m_i are exponents of E_8.

---

## PHASE D: PERFECT (Chriss-Ginzburg-grade exposition)

### D.1 COMPUTATION-FIRST EXPOSITION

D.1.1  [REWRITE] The W-infinity chapter should lead with the explicit W_3
       computation, not with abstract definitions. The current structure
       (def:w-infty at line 484, then conj:w-infty-bar at 502, then the
       general theorem at 795) buries the computation. Chriss-Ginzburg
       style: put the W_3 computation first, then W_4, then generalize.
       The current text partially does this (the "warm-up" at lines 600-760)
       but the transition to the general theorem could be smoother.

D.1.2  [REWRITE] The DS-KD intertwining theorem should include an explicit
       worked example (sl_2 -> Virasoro) before the general statement.
       Show the double complex, the spectral sequence, and the degeneration
       concretely for the simplest case.

D.1.3  [REWRITE] The stage-4 packet analysis should include a summary table
       at the beginning, not just the detailed decomposition. The reader
       needs a roadmap before the 40-proposition deep dive.

---

### D.2 GEOMETRIC REALIZATION

D.2.1  [WRITE] A new section: "Geometric home for the W-algebra bar complex."
       Connect the bar complex to perverse sheaves on the Slodowy slice
       inside the affine Grassmannian. The DS functor provides the bridge:
       DS(perverse sheaf on Gr_G) = perverse sheaf on Slodowy slice.
       The bar complex coefficients should correspond to intersection
       numbers or Ext groups on this geometric space.
       This is the Chriss-Ginzburg perspective that is currently absent.

D.2.2  [WRITE] Geometric interpretation of the stage-4 channels.
       The six channels should correspond to specific geometric data
       on the Slodowy slice for sl_4.

---

### D.3 NON-SCALAR PROGRAMME HONESTY

D.3.1  [WRITE] If B.2.1 confirms dim H^2_cyc(W_infinity) = 1:
       Write an honest assessment in the monograph. The W-infinity
       construction is the crowning finite-type example and the M-level
       completed package, but it does NOT provide a non-scalar Theta_A.
       The non-scalar programme requires a different source.

D.3.2  [WRITE] If alternatives are found (B.2.3): write the non-scalar
       construction using the correct source.

---

### D.4 MISSING PROOFS

D.4.1  [COMPLETE] Every instance of "the proof is similar" or "one verifies"
       in the monograph. Search and replace each with a complete argument.
       METHOD: grep -rn 'proof is similar\|one verifies\|straightforward\|is clear' chapters/ --include='*.tex'

D.4.2  [COMPLETE] Every proof that cites a result without verifying the
       hypotheses are satisfied. For each cited result, check that its
       hypotheses are verified in the citing proof.

---

### D.5 CROSS-REFERENCE INTEGRITY

D.5.1  [VERIFY] Every \ref{} in the monograph resolves. Run LaTeX and
       check for undefined references.

D.5.2  [VERIFY] Every \eqref{} points to the correct equation.

D.5.3  [VERIFY] The concordance (concordance.tex) is consistent with
       all chapter-level statements. Any disagreement: concordance wins.

---

### D.6 BIBLIOGRAPHY

D.6.1  [VERIFY] Every \cite{} resolves.

D.6.2  [VERIFY] Key citations are correct: Hornfeck 1993, Blumenhagen et al.
       1996, Fateev-Lukyanov, Arakawa, Beilinson-Drinfeld, etc.

D.6.3  [ADD] Any missing references identified during the audit.

---

## PRIORITY ORDER FOR EXECUTION

### IMMEDIATE (do first, highest impact)
1. A.7.1-A.7.4 (DS-KD intertwining -- foundational)
2. A.8.1-A.8.7 (W-infinity theorem -- the audit target)
3. B.2.1-B.2.2 (H^2_cyc computation -- existential for the programme)
4. B.3.1-B.3.3 (bar-side residue extraction -- independent verification)
5. A.0.8-A.0.12 (convention/formula checks -- guards against corruption)

### HIGH (do second)
6. A.1.1-A.1.7 (Theorem A)
7. A.2.1-A.2.4 (Theorem B)
8. A.3.1-A.3.5 (Theorem C)
9. A.4.1-A.4.7 (Theorem D)
10. A.5.1-A.5.4 (MC1)
11. A.6.1-A.6.4 (MC2)

### MEDIUM (do third)
12. A.9.1-A.9.9 (M-level MC4 machinery)
13. A.10.1-A.10.9 (stage-4 packet)
14. A.11.1-A.11.3 (stage-5 packet)
15. B.1.1-B.1.4 (H-level target construction)
16. B.4.1-B.4.4 (DS derivation of structure constants)

### ONGOING (throughout)
17. C.1.1-C.1.6 (new compute modules)
18. C.2.1-C.2.6 (new tests)
19. C.3.1-C.3.2 (test audit)
20. C.4.1-C.4.5 (formula verification sweep)

### FINAL (after everything else)
21. D.1.1-D.1.3 (exposition rewrite)
22. D.2.1-D.2.2 (geometric realization)
23. D.3.1-D.3.2 (non-scalar honesty)
24. D.4.1-D.4.2 (complete missing proofs)
25. D.5.1-D.5.3 (cross-reference integrity)
26. D.6.1-D.6.3 (bibliography)

---

## EXECUTION NOTES FOR OPUS 4.6

### Strengths to leverage
- Deep mathematical reasoning: use for proof verification, gap analysis
- Long context: read entire proofs before judging, don't skip steps
- Code generation: build compute modules that verify formulas
- Systematic analysis: process items sequentially, don't jump around

### Failure modes to avoid
- Formula hallucination: NEVER write a formula without sourcing it from a file
- Sycophantic convergence: if a proof looks wrong, say so. Don't soften.
- Convention drift: re-read CLAUDE.md conventions section before each phase
- False confidence: "obvious" steps in proofs are where errors hide
- Context loss: checkpoint after each sub-phase, summarize findings

### Session management
- Each session should tackle one sub-phase (e.g., A.7 or A.8)
- Begin each session by re-reading CLAUDE.md and the relevant source files
- End each session by recording findings in notes/
- Never fix anything during a verification phase -- just record
- Fix phase comes only after full audit of a tier is complete
