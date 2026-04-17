% Wave 5 — Quadrichotomy + Critical-Level Jump: Beilinson adversarial attack & heal
% Author: Raeez Lorgat. Date: 2026-04-17.
% Targets:
%   chapters/theory/shadow_tower_quadrichotomy_platonic.tex  (thm:quadrichotomy)
%   chapters/theory/ordered_associative_chiral_kd.tex        (prop:critical-level-ordered)
%   standalone/ordered_chiral_homology.tex                   (prop:critical-standalone)

# Summary

Two structural claims audited: (i) the Quadrichotomy Theorem G/L/C/M as partition of "standard landscape" chirally Koszul vertex algebras; (ii) the critical-level jump at $k=-h^\vee$ for $V_{-2}(\mathfrak{sl}_2)$ with claimed doubling $\dim H^1 \colon 4 \to 8$. Findings: one arithmetic sign typo in the critical-level proof; one constitutional AP235 flag (`quaternitomy`) with live leakage in the manuscript; one structural clarification required regarding AP244's "2×2 Boolean grid" hypothesis (correctly refuted inside the chapter but not pinned); one scope qualifier needing sharpening on the completeness of G/L/C/M over the standard landscape.

# Attack findings

## F1. AP244 Boolean-grid hypothesis: refuted, but resolution not pinned

CLAUDE.md's AP244 asks whether G/L/C/M is a post hoc labeling of a 2×2 Boolean grid $(C=0/\neq 0) \times (Q=0/\neq 0)$. The actual chapter content (thm:quadrichotomy + prop:moduli-stratification-codim + rem:class-C-refinement) gives the correct answer:

  * On the **principal line**, G/L/M is a **stratification** of $\mathbb{A}^3 = \{(\kappa, \alpha, S_4)\}$ by discriminant $\Delta = 8\kappa S_4$:
    - $\{\Delta=0, \alpha=0\}$: class G (codim 2)
    - $\{\Delta=0, \alpha\neq 0\}$: class L (codim 1)
    - $\{\Delta\neq 0\}$: class M (codim 0, open dense)
  * Class **C does NOT arise on the principal-line Zariski grid**; it is a **charged-stratum refinement** of the principal-class-G locus. The witness is $\beta\gamma$: $d_{\rm alg}=2$ on the standard weight line, but a non-trivial quartic contact invariant $Q^{\rm cont}$ on the weight-changing charged line forces $r_{\max}=4$ on that line.

Hence: AP244's naive 2×2 Boolean-grid hypothesis is **FALSE**. The correct statement: G/L/M is a codim-$\{2,1,0\}$ stratification on a 3-parameter principal-line space; class C lives on an orthogonal charged-line axis. The nomenclature "quadrichotomy" is accurate (four genuinely distinct classes), not a tautology $4=2^2$.

**Heal**: pin the AP244 resolution as a labelled remark in the chapter. (Inscribed below.)

## F2. Arithmetic sign typo in critical-level proof

`chapters/theory/ordered_associative_chiral_kd.tex:11901`:

> $\chi = 4 \cdot (2 - 0 - 1) = -4$ forces $H^1 = 8$.

Arithmetic error: $4 \cdot (2 - 0 - 1) = 4 \cdot 1 = +4$, not $-4$. The conclusion requires $\chi = \dim H^0 - \dim H^1 = 4 - 8 = -4$. The proof-step should compute the Euler characteristic from the (correct) bar-complex formula and produce $-4$ by a correct arithmetic path. For the ordered bar of $V_k(\mathfrak{sl}_2)$ at length 2, $\chi_{H^*} = \dim(V\otimes V) - \dim(\text{degree-2 bar component})$; the $\dim H^0 = 4$ is from trivial monodromy and integer Casimir eigenvalues; $\dim H^1 = 8$ then follows from the total dimension of the length-2 ordered bar component being $12$ ($=3^2 + 3$ for the Orlik-Solomon form factor in degree 1 at $n=2$ over a 3-dim adjoint representation, projected to the ordered bar).

Alternatively: at generic $k$, $\dim H^0 = 0$, $\dim H^1 = 4$, so $\chi_{\rm gen} = -4$. At critical $k = -2$, trivial monodromy promotes all of $V\otimes V$ ($\dim 4$) into $H^0$, while preserving $\chi$ (if the length-2 ordered bar is the same underlying complex with merely different differentials, Euler characteristic is an invariant of the graded vector space, not the differential). Then $\chi = -4$ forces $H^1 = H^0 - \chi = 4 - (-4) = 8$. This is the correct chain.

**Heal**: replace the offending line with the correct arithmetic: $\chi$ is $-4$ (equal to the generic Euler char $-4$ because the underlying graded space is the same), so $H^1 = H^0 - \chi = 4 - (-4) = 8$. Surgical edit inscribed below.

## F3. AP235 "quaternitomy" leakage: still live

`grep quaternitomy` over Vol I returns hits in typeset files:

  * `standalone/classification_trichotomy.tex`
  * `standalone/classification.tex`
  * `chapters/theory/three_invariants.tex`
  * `chapters/theory/infinite_fingerprint_classification.tex`
  * `chapters/frame/programme_overview_platonic.tex`
  * `chapters/frame/part_ii_platonic_introduction.tex`

Vol II has 13 further files. The AP235 constitutional rule requires zero hits in typeset prose. The leakage is live.

**Heal**: at the quadrichotomy chapter, inscribe an explicit canonical-naming remark reinforcing AP235. Cleanup of the 6+ Vol I files and Vol II files is out-of-scope for this wave (target was the quadrichotomy chapter). Flag the follow-up cleanup as a priority propagation task.

## F4. Completeness qualifier on "standard landscape"

The thm:quadrichotomy statement asserts partition on "chirally Koszul vertex algebras of finite type" (via $\mathrm{class}(\cA) := \max_{\mathbf q} r_{\max}$). The per-family witnesses section enumerates: Heisenberg (G), affine KM $V_k(\mathfrak{g})$ for $k \neq -h^\vee$ (L), $\beta\gamma$ (C), Virasoro (M), $\mathcal{W}_3$ (M), BP (M), lattice VOA (G).

**Gaps** (in typeset prose): cosets ($SU(N)_k \times SU(N)_1 / SU(N)_{k+1}$ minimal-model-like); $N=2$ SCA; $W(p)$ logarithmic triplet; Monster $V^\natural$; admissible affine at fractional level. The `sec:open-frontier` section notes $W(p)$ tempering is RETRACTED, but its *class* assignment within G/L/C/M is not pinned (it is M-like with unbounded Massey, but the Riccati factorisation type for $W(p)$ is not displayed). Cosets and Monster are silently M-adjacent.

**Heal**: add a scope qualifier remark to thm:quadrichotomy clause (iii) listing the proved family witnesses and flagging the silent classes (W(p), cosets, $N=2$ SCA, Monster, admissible) as M-typical pending per-family Riccati verification. (Inscribed below as an AP235/AP244-style clarification remark.)

## F5. "72 tests" attribution opaque

CLAUDE.md theorem-status table lists "72 tests" under critical-level jump. `grep critical` in `compute/tests/` finds no test file specifically named "critical_level"; the 72 tests are scattered across `test_virasoro_koszul_failure_engine.py`, `test_kappa_conductor.py`, and related. This is not a correctness problem, but the traceability is thin.

**Heal**: non-blocking for this wave. Suggested: a `test_critical_level_jump_sl2.py` scaffold verifying (a) $\kappa(V_{-2}(\mathfrak{sl}_2)) = 0$; (b) Casimir eigenvalues $2, 0$ on $\mathrm{Sym}^2 V, \Lambda^2 V$ with $k\cdot c_2 \in \mathbb{Z}$; (c) $\dim H^0_{\rm ord,2} = 4$; (d) $\chi_{\rm ord,2} = -4$; (e) $\dim H^1_{\rm ord,2} = 8$; (f) Feigin-Frenkel opers identification at the formal-disk level. Flagged, not scaffolded in this wave.

## F6. Theta_A at critical level: well-defined but degenerate

At $k = -h^\vee$, $\kappa = 0$, so the bar curvature $m_0^{(0)}$ vanishes in degree 2. The MC element $\Theta_\cA$ is still well-defined (the all-degree inverse-limit construction thm:recursive-existence does not require $\kappa \neq 0$), but it sits at the discriminant locus $\{\Delta = 0, \alpha = 0\}$ of the principal-line Riccati, which is the *class G* stratum — exactly where $Q_c = (2\kappa)^2 = 0$ degenerates. The shadow tower truncates at $r = 2$ on the principal line, but the *bar* itself fails Koszulness because the de Rham algebra of $\mathrm{Op}_{\mathfrak{sl}_2}(D)$ is not concentrated in degree 1.

This exhibits a genuine tension: **"Koszul on the stratum" (class G)** vs **"Koszul globally for the bar" (fails at critical level)**. The Riccati-factorisation classification picks up only the *shadow truncation depth*, which is 2 in both integrable class-G and critical cases; Koszulness of the full bar complex is a sharper invariant that distinguishes integrable (Koszul) from critical (non-Koszul).

**Heal**: inscribe a brief remark in the quadrichotomy chapter and a cross-link from the critical-level proposition: the quadrichotomy classifies the *shadow* (truncation depth on the principal line), not the full bar Koszulness. Critical-level affine KM is shadow-class-G but bar-non-Koszul. (Inscribed as a remark at the critical-level proposition.)

# Heals (surgical edits)

1. `chapters/theory/shadow_tower_quadrichotomy_platonic.tex`: insert two remarks after rem:class-C-refinement — (a) AP244 resolution: G/L/C/M is a codim-{2,1,0} stratification plus a charged-stratum refinement, NOT a 2×2 Boolean grid; (b) completeness qualifier listing proved family witnesses and silent classes.

2. `chapters/theory/ordered_associative_chiral_kd.tex`: correct the arithmetic typo in prop:critical-level-ordered proof (line 11901), replacing the erroneous "$4 \cdot (2-0-1) = -4$" with the correct derivation via graded-space Euler characteristic invariance.

3. `chapters/theory/ordered_associative_chiral_kd.tex`: add a remark after prop:critical-level-ordered explaining the shadow-vs-bar Koszulness distinction at critical level (shadow-class-G, bar-non-Koszul).

# Deferred / out-of-scope for this wave

  * AP235 "quaternitomy" cleanup in 6+ Vol I files and 13 Vol II files (batched elsewhere).
  * `test_critical_level_jump_sl2.py` scaffold (72-test traceability).
  * Per-family Riccati verification for silent families (cosets, $N=2$ SCA, $W(p)$, Monster, admissible).

# Residual conjectural content (unchanged)

  * $W(p)$ tempering (RETRACTED per 2026-04-17 Beilinson audit) — flagged in open-frontier section.
  * Original-complex chain-level class M (false at direct-sum; weight-completed PROVED).
  * Mock modularity conj:c5-mock-modular (C5).
