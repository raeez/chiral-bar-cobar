# Wave 5 adversarial audit: depth-gap trichotomy and Theta_A recursive existence

**Targets**
- `prop:depth-gap-trichotomy` at `chapters/theory/higher_genus_modular_koszul.tex:18204`
- `thm:recursive-existence` at `chapters/theory/higher_genus_modular_koszul.tex:13509`
- `lem:depth-three-impossible` at `chapters/theory/higher_genus_modular_koszul.tex:18123`
- `thm:mc2-bar-intrinsic` at `chapters/theory/higher_genus_modular_koszul.tex:4032` (input for Theta_A)
- `thm:betagamma-global-depth` at `chapters/examples/free_fields.tex:1191` (d_alg=2 witness)
- `prop:independent-sum-factorization` at `chapters/theory/higher_genus_modular_koszul.tex:29428`

## Verdicts per sub-attack

### (i) Riccati / Delta = 8 kappa S_4 discriminant argument
**ACCEPT.** The Gaussian decomposition Q_L(t) = (2 kappa + 3 alpha t)^2 + 2 Delta t^2 (`cor:gaussian-decomposition:18072`) is algebraically immediate. Q_L is a perfect square iff Delta = 0 iff S_4 = 0 (since kappa != 0 on the assumed line). When Delta != 0, the binomial series for sqrt(Q_L) has infinitely many nonzero coefficients (the coefficient of t^2 inside u is nonzero, so the binomial series for (1+u)^{1/2} does not terminate). The Taylor inversion at degree r is the MC recursion itself (`eq:single-line-inversion`). No step is skipped; the argument is first-principles in k(c)[t].

### (ii) beta-gamma witness at d_alg = 2
**ACCEPT with caveat on AP219.** The d_alg = 2 witness is the *full two-channel deformation* of beta-gamma_lambda, not the T-line slice (which is class M, d_alg = infinity) and not the weight-changing line slice (which has all shadows vanishing). Stratum separation (mu_{beta-gamma} = 0 via rank-one abelian rigidity, `cor:nms-betagamma-mu-vanishing`) kills the self-bracket of the charged quartic, giving S_r = 0 for r >= 5 globally despite S_5 != 0 on the T-line slice. AP219 warns "wrong line": the T-line slice IS the wrong line if one wants d_alg = 2. `prop:depth-gap-trichotomy` correctly cites the global depth theorem.

### (iii) Virasoro d_alg = infinity
**ACCEPT.** For Vir_c, kappa = c/2 != 0 (generic c), alpha = S_3 = 2 != 0, S_4 = 10/(c(5c+22)) != 0. Hence Delta = 80 kappa/(c(5c+22)) = 40/(5c+22) != 0, and Q_L is not a perfect square in k(c)[t]. Single-line Riccati gives d_alg = infinity immediately, with no further input.

### (iv) Heisenberg d_alg = 0 vs affine KM d_alg = 1
**ACCEPT.** Heisenberg: alpha = 0, S_4 = 0, Q_L = (2 kappa)^2, so H(t) = 2 kappa t^2 (degree 2 only). Affine KM: alpha != 0 (Jacobi contribution), S_4 = 0 (Jacobi-forced cancellation of intrinsic against free quartic, verified numerically in Hankel table `ex:hankel-standard`), Q_L = (2 kappa + 3 alpha t)^2, so H is degree 3. Class assignment G and L respectively, each witnessed by the Gaussian envelope's degree.

### (v) Impossibility of d_alg = 3
**ACCEPT as PROOF, not check-of-known-families.** `lem:depth-three-impossible` gives two independent arguments:
- *MC-recursion argument (degrees 5 and 6).* If S_4 != 0 and alpha != 0, then S_5 = -6 P alpha S_4 / 5 != 0. If S_4 != 0 and alpha = 0, then S_5 = 0 but S_6 = -2 S_4^2/(3 kappa) != 0. So the tower does not terminate at degree 4 on any kappa != 0 line.
- *Shadow Lie / weight-raising operator argument.* D_{Q-frak} is a degree-2 raising operator on the Hamiltonian model of the primary line; S_4 != 0 makes its action on x^{2m} nonzero for all m >= 2, populating every even degree beyond 4.
These are first-principles and do not rely on family-by-family inspection. The multi-generator closure paragraph then closes off cross-sector assembly via `prop:independent-sum-factorization` (decouple) OR cubic-pump-reactivation (couple); the dichotomy is sharp and rules out finite d_alg >= 3 from any source.

### (vi) Theta_A inverse limit
**ACCEPT, non-circular.** The apparent circularity concern (Step 2 cites the bar-intrinsic Theta_A before Step 4 constructs it) is resolved by reading carefully: Step 2 invokes `thm:mc2-bar-intrinsic` (already proved, `:4032`), whose construction is operadic (D_A = genus-completed bar differential, D_A^2 = 0 from prism/`thm:bar-modular-operad`). The inverse-limit argument of Steps 1,3,4 establishes that the pronilpotent weight filtration F^N (indexed by 2g-2+r+d) is exhaustive, separated, complete, with finite-dim quotients, giving Mittag-Leffler in the strongest form (every transition surjective). Step 5 identifies the limit with D_A - d_0, which is the Theta_A defined unconditionally in thm:mc2-bar-intrinsic. `rem:recursive-existence-clarification` already states this transparently.

### (vii) MC relation at degree 4
**ACCEPT.** The quadratic master equation (`eq:single-line-inversion`) at r = 4 reads S_4^free = -9 alpha^2/(16 kappa), derived from the j = k = 3 term of the charge-graded recursion. The Hankel Schur complement `eq:intrinsic-quartic-schur` separates inherited (alpha^2-driven) from intrinsic (S_4 - S_4^free) content. Affine KM has S_4^intrinsic = -S_4^free so S_4 = 0, enforcing d_alg = 1. Virasoro has S_4^intrinsic != -S_4^free, so S_4 != 0 and Delta != 0, enforcing d_alg = infinity.

### (viii) Shadow Lie Jacobi
**ACCEPT.** The second proof of `lem:depth-three-impossible` uses the shadow Hamiltonian bracket {x^j, x^k}_H = jk P x^{j+k-2} on the primary line (`:18169`). This is the graded Lie structure (AP94) on the shadow algebra restricted to the line. Jacobi is built into the bracket by construction (it is the classical Poisson algebra of x in one variable with Poisson weight P). The weight-raising operator D_{Q-frak} is then well-defined and first-principles.

### (ix) d_alg vs d_gen coincidence
**ACCEPT with clarification.** Both invariants coincide on classes G (= 0), L (= 1). On class C (beta-gamma), d_alg = 2 (from global shadow depth) and d_gen >= 2 (two generators beta, gamma); these are equal. On class M (Vir), d_alg = infinity but d_gen = 3 (T generates through m_3 Jacobiator; further generators not produced). The distinction is substantive only in class M and is properly handled by `rem:depth-gap-fine-structure:18380`.

## Findings summary

No MODERATE or worse findings. The proofs are first-principles and complete. One MINOR finding: the multi-generator closure paragraph in `prop:depth-gap-trichotomy` (`:18306`-`:18347`) relies on the non-nilpotence of `ad_{S_3^{(q_0)}}` (cubic pump) but the proof of non-nilpotence is located in `rem:contact-stratum-separation:19795`, several thousand lines downstream in the file. A forward reference belongs in the closure paragraph itself for chain-of-proof clarity. Similarly, `lem:depth-three-impossible:18123` is called from `prop:depth-gap-trichotomy` but covers only the single-line kappa != 0 case; the proof of the gap on the residual kappa = 0 locus is structurally different (rank-one rigidity + charge decomposition) and deserves its own explicit cross-reference in the proof. Healing edits below.

## Heal edits (surgical)

- Insert forward cross-reference from the multi-generator closure paragraph of `prop:depth-gap-trichotomy` to `rem:contact-stratum-separation` where the non-nilpotence of the cubic pump is actually justified.
- Insert explicit cross-reference to the single-line Riccati scope (kappa != 0) in the proof prologue and to `thm:betagamma-rank-one-rigidity` for the kappa = 0 residual locus.
- In `thm:recursive-existence` Step 2, tighten the sentence "Since the MC equation [..] holds in completed algebra" to include an explicit parenthetical pointer to `thm:mc2-bar-intrinsic`(i), preventing a reader from parsing Step 2 as assuming its conclusion.

All edits are internal-reference tightening; no theorem statements or proofs change semantically.

Output: attack-and-heal report (this file) + two surgical Edit insertions. No commits.
