## G1 Koszul Reflection — Adversarial Audit

### Attack 1: Adjoint equivalence vs adjunction
Claim attacked: "`(Omega_X, B-bar_X) ... is a symmetric-monoidal adjoint equivalence`" (memory:236; theorem_A:34-49, 175-183). Proved: a twisting-morphism adjunction is cited (LV12 Thm. 2.2.9/11.4.1; theorem_A:203-218). Asserted: unit/counit equivalences; theorem_A:233-238 even swaps terminology ("counit" for `K^{-1}K(A)`). Missing: chain-level triangle identities. CLAUDE demands named homotopies when chain-level (310-335); none appear.

### Attack 2: conil+comp convention ambiguity
Claim attacked: "`Coalg_X^{conil,comp}`" (memory:236) / "conilpotent-complete locus" (theorem_A:947-953). The precise axiom appears only later: exhaustive coradical filtration plus equivalent completion (theorem_A:949-953, 1100-1101), while H2 is augmentation-adic algebra completion (73-77). Positselski's conventions are CDG/coderived and filtered by internal grading (Positselski 2011 App. A, Thms. 1-2; Positselski 2018 §§6.3-6.4), not automatically the same as Francis-Gaitsgory factorization coalgebras (FG §§3.3-5.2; GR IV.5).

### Attack 3: K² ≃ id explicit homotopy
Claim attacked: "`K^2 ~ id`" (memory:236; theorem_A:45-49, 190-192). What is proved is spectral-sequence collapse plus imported acyclicity (theorem_A:226-238, 507-535). No explicit contraction `h` is written for Heisenberg, Virasoro, or affine KM. The "five collapse statements ... constitute chain-level verification" sentence (533-534) is aspirational unless those homotopies are displayed.

### Attack 4: H3 finite-dim vs bounded-per-grade
Claim attacked: "finite-dimensional graded bar pieces" (memory:238). theorem_A correctly narrows H3 to conformal-weight spaces, "not by bar-tensor depth" (78-83), and says bar-depth slices are infinite-dimensional (456-474). Lattice/Heisenberg `p(n)` entries (359-382, 386-405) support finite per weight, not polynomial or uniformly bounded multiplicity. H3 should read finite-dimensional per conformal weight plus Mittag-Leffler surjectivity (1135-1160).

### Attack 5: Fibred (∞,1)-category existence
Claim attacked: "`Kosz^{rel}/M_{g,n}` ... fibred (infinity,1)-category" and global autoequivalence (memory:29-30, 169-175, 939-944). theorem_A explicitly retracts this to fixed smooth `X`; relative Ran base-change and nodal gluing are "cited but not established" (1163-1196), with obstruction classes `[alpha_BC]`, `[beta_nodal]` (1198-1285). Global form is conditional/aspirational.

### Attack 6: Francis-Gaitsgory (∞,2) properad 2-morphism
Claim attacked: "explicit ... properad level" (theorem_A:137-139, 947-999). The proof is abstract transfer: "applying the left adjoint" and "extended graph-wise" (1091-1107). Extra structure is multi-output graph composition (873-917), but no concrete 2-morphism/modification is exhibited. This is a formal lift, not an explicit FG 2-cell (compare FG §§3.3-5.2; Lurie HA §§5.2, 5.5).

### Retraction Candidates
- Retract "symmetric-monoidal adjoint equivalence" to "adjunction, equivalence after stated unit/counit qi hypotheses."
- Retract global `K^{univ}` autoequivalence pending `[alpha_BC]=[\beta_nodal]=0`.
- Retract "chain-level verification" for archetypes until explicit homotopies are inscribed.
- Retract "explicit properad-level" to "abstract properad-level transfer."

### Over-Strong Language Flags
- "\ClaimStatusProvedHere" for theorem_A:158-160 and 955-958.
- "at full strength" (801-804).
- "One symmetry, one diagram, one theorem/equation" (270-282, 2102-2111).
- "sole genuinely open frontier" (95-98, 1979-1984).
