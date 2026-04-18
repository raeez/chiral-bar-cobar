# Wave 3 Attack-and-Heal — 6d hCS codim-2 defect = W_{1+∞} at Ψ = −σ_2

Target row (Vol I CLAUDE.md:624):
  "6d hCS defect | PROVED | Codim-2 defect on C⊂C³: boundary algebra
   = W_{1+inf} with Psi=-sigma_2. c=1 (Sugawara). N_{C/Y}=C² gives
   spectral params. 49 tests."

Inscription locus:
  Vol III `chapters/theory/quantum_chiral_algebras.tex:397-471` —
  `prop:codim2-defect-ope`, ClaimStatusProvedHere, tagged 48 tests.
  Vol III `standalone/cy3_6d_hcs_w1inf_vol3.tex` (SCAFFOLD stub only:
  lines 1-81; one-paragraph abstract + \input pointers to other
  chapters — no theorem body; scaffold-only at 2026-04-17).
  Vol III `chapters/theory/en_factorization.tex:1200-1320` — AGT
  factorization descent picture.
  Vol III `compute/lib/hcs_codim2_defect_ope.py` (666 lines).
  Vol III `compute/tests/test_hcs_codim2_defect_ope.py` (681 lines,
  ≈48 test methods + 1 HZ-IV-decorated class).

## Attack ledger (seven lines of adversarial fire)

A1 (AP272 folklore-citation pillar). The whole identification of the
6d hCS codim-2 defect algebra with W_{1+∞} rests on Costello 2013
"Supersymmetric gauge theory and the Yangian" at 5d (one dimension
down) plus Costello-Gwilliam factorisation algebras as the global
framework. Neither is inscribed as a theorem inside Vol III. The
5d → 6d-on-codim-2 bridge is the load-bearing move; it is not
independently derived. (This is exactly the AP272 "unstated
cross-lemma via folklore citation" pattern — single-citation
mechanism.)

A2 (Derivation gap — Step 3 "integration over the normal fiber").
`prop:codim2-defect-ope` proof Step 3 (line 426-436) writes the
propagator ⟨A^{(m,n)}(z) A^{(p,q)}(w)⟩ = δ_{m+p,0}δ_{n+q,0}/(z−w)²
and then ASSERTS "the Omega-background twists the inner product on
gl_1 by −σ_2 (which is the Kac–Moody level of the 5d theory on
C² × R, as in Costello 2013)." The TWIST is not derived; it is
imported. Specifically, where does the coefficient −σ_2 come from
if the propagator delta-conditions force m+p=n+q=0? The mode (0,0)
has zero equivariant weight; the level −σ_2 should arise from
integrating the quadratic form in `dz_2 ∧ dz_3 ∧ (normal coupling
to Ω-background)` over the formal bidisk. This one-loop equivariant
determinant on D² is not computed — it is quoted from Costello.
That is the specific Beilinson-falsification target.

A3 (Sign of σ_2 convention). The engine (`hcs_codim2_defect_ope.py`
line 180-199) fixes Ψ = −σ_2 with σ_2 = h_1 h_2 + h_1 h_3 + h_2 h_3.
Under the CY constraint h_1+h_2+h_3=0 we have σ_2 = −½(h_1²+h_2²+h_3²)
≤ 0, hence Ψ = −σ_2 ≥ 0. Good: at the self-dual point (1,0,−1),
σ_2 = 1·0 + 1·(−1) + 0·(−1) = −1, so Ψ = 1, matching the self-dual
level and producing c=1 Heisenberg (the free boson). Sign check
PASSES. The engine also correctly implements permutation
invariance under S_3 on (h_1,h_2,h_3) — good (matches Miki
triality).

A4 (c=1 Sugawara). The Sugawara formula c = Ψ·dim(gl_1)/(Ψ+h^∨)
= Ψ/Ψ = 1 (because h^∨=0 for the abelian gl_1). This is correct
and Ψ-INDEPENDENT, matching the test-file claim. But CLAUDE.md
writes "c=1 (Sugawara)" without the critical qualifier "for N=1
only"; for general N=rank of W_{1+∞} restricted to gl_N modes
(as in toroidal sectors), c=N. The row is correct for the
codim-2 defect on C ⊂ C³ with gl_1 gauge, which IS the scope
of `prop:codim2-defect-ope` — but the row invites reader confusion
against the W_N family. Mild scope-tag issue.

A5 (49 vs 48 test count mismatch). CLAUDE.md advertises "49 tests";
the chapter-level Remark (`quantum_chiral_algebras.tex:484`) says
"48 tests" and enumerates 15+6+13+4+3+3+4 = 48. The 49th is the
HZ-IV decorated test `test_codim2_defect_OPE_at_SV_N2_and_self_dual`
in class `TestCodim2DefectOPEIV` (lines 571-681 of the test file).
Minor: status row and chapter remark drifted by one — AP256
aspirational-heal drift in the small.

A6 (AP277 vacuous HZ-IV body? — PARTIAL). The single HZ-IV
decorator (test 49) carries a prose decorator with FOUR declared
disjoint sources:
  (i) 5d cross-check via `prop:5d-spin12-ope`
  (ii) Prochazka-Rapcak 2018 (arXiv:1711.06888) Miura transform
  (iii) Arbesfeld-Schiffmann-Vasserot 2015 (arXiv:1506.00246)
       explicit level formula
  (iv) classical Sugawara c = dim(g)·k/(k+h^∨) for gl_1
The test body checks: (a) σ_2 = −3 at (1,−2,1) via direct arithmetic
(Path DC); (b) CY constraint sum h_i = 0; (c) `five_d_Psi_matches
= True` (HARD-CODED True — AP287 structural primitive, NOT a
numerical cross-check); (d) Sugawara c = 1 at Ψ ∈ {3,1,2,5} via
`dim_gl1 * Psi_val / (Psi_val + h_v_gl1)` (real arithmetic); (e)
`pr_w_inf_match = True` (HARD-CODED — AP287); (f) `asv_miura
= True` (HARD-CODED — AP287); (g) σ_2 = −1 at (1,0,−1).
Two of four declared paths (PR and ASV) are AP287/AP277 vacuous
boolean truth-markers. The decorator PASSES `assert_sources_disjoint`
on the LABELS, but the COMPUTATION on paths (ii),(iii) is a
bibliographic-disjoint-shared-intermediate veneer (AP288/AP310
variant).

A7 (Cross-volume Khan-Zeng B84 scope). B84 states "Khan-Zeng 3d
Poisson sigma model covers ALL freely-generated PVAs with conformal
vector." W_{1+∞} at c=1 is freely-generated (the free boson as a
Heisenberg strong-generator plus Sugawara T) with conformal vector
— so the 6d hCS defect output IS in Khan-Zeng scope. But the
chapter makes no cross-reference. Opportunity, not a failure.

## Surviving core (Drinfeld-style, 2-3 sentences)

A 6d holomorphic Chern–Simons theory on Y = C³ with abelian gauge
algebra gl_1 and Omega-background (h_1,h_2,h_3) subject to the CY
constraint ∑h_i = 0, restricted to a tubular neighbourhood of the
holomorphic curve C = C_{z_1} ⊂ Y, produces on C a rank-one
Heisenberg algebra at level Ψ = −σ_2(h) with Sugawara stress tensor
of central charge c = 1; the level Ψ = −σ_2 is the coefficient of the
propagator twist induced by integrating the quadratic action over
the normal formal bidisk D² ⊂ N_{C/Y} = C². The identification of
the full higher-spin tower on C with W_{1+∞} at parameter Ψ is
imported from the Costello 5d result and from the independent
Procházka–Rapčák affine-Yangian / W_{1+∞} isomorphism; the
spins-1-and-2 fragment of that identification (the c = 1 Sugawara +
level Ψ Heisenberg) is inscribed with derivation. Beilinson-
falsification target: Step 3 of `prop:codim2-defect-ope` asserts the
−σ_2 twist without computing the equivariant 1-loop determinant on
D².

## Heal plan (four options, all non-destructive)

H1 (AP272 — strengthen the 5d → 6d-on-codim-2 bridge). Add a new
`lemma:5d-to-6d-codim2-bridge` in `quantum_chiral_algebras.tex` §5,
stating explicitly: "The 6d hCS action restricted to U = C × D² and
integrated over D² with Omega-background parameters (h_2, h_3) on
the normal fiber produces the 5d hCS action on C × R with KM level
k_eff = −σ_2(h)." The proof is a one-line equivariant-determinant
computation on D² (the 1-loop determinant of the ∂̄-operator in the
Omega-background), bibkey Costello 2013 + Costello-Gwilliam Vol II
§5, with honest `\ClaimStatusProvedElsewhere` tag. This converts the
AP272 single-citation pillar into a cited bridge-lemma with internal
derivation sketch.

H2 (Scope-qualify CLAUDE.md row). Rewrite the row to:
  "6d hCS defect | PROVED spins 1+2 on C ⊂ C³ with gl_1 gauge
   (`prop:codim2-defect-ope`, 48 tests + 1 HZ-IV); full higher-
   spin W_{1+∞} identification ProvedElsewhere via Procházka–Rapčák
   (arXiv:1711.06888) | Codim-2 defect: spin-1 Heisenberg at level
   Ψ = −σ_2(h), Sugawara c = 1 (gl_1 only; h^∨=0). N_{C/Y} = C²
   gives two spectral parameters (z_2,z_3) with Yangian projection
   C³ → C² → C reducing to single-parameter R(u)."

H3 (HZ-IV decorator upgrade — AP277 heal). Replace `pr_w_inf_match
= True` and `asv_miura = True` with genuine numerical checks:
  (a) Procházka-Rapčák Miura-transform path: compute the Ψ →
      U_Ψ(W_{1+∞}) structure function g(u) = ∏(u−h_i)/∏(u+h_i)
      expanded to O(u^{-2}); residue = −2σ_2 = 2Ψ. Assert
      `residue_at_infty == 2 * Psi_SV_N2` (→ 6 at SV N=2).
  (b) Arbesfeld-Schiffmann-Vasserot path: compute the Miura
      factorisation of the Heisenberg at Ψ=3 and check that the
      bosonisation reproduces the J(z)J(w) = 3/(z−w)² OPE. This
      makes the HZ-IV block honest at all four declared paths
      rather than two hard-coded booleans. No decorator
      re-wiring; just replace the two booleans with live
      computations that actually touch the engine.

H4 (Test count rectification — AP256). Change CLAUDE.md "49 tests"
→ "48 tests + 1 HZ-IV-decorated independent-verification test"
(which is the honest count the chapter-level Remark carries).
Alternatively: bump the chapter Remark to "49 tests" if the HZ-IV
test is to be counted. Either direction — make the two numbers
agree in a single atomic edit. Recommend keeping "48 + 1 HZ-IV"
because the HZ-IV test is qualitatively distinct.

## Commit plan

NONE. This note is analytical. All four heal options are drafted
but no .tex, engine, test file, or CLAUDE.md is edited in this
wave. When a user invokes a follow-up heal-implementation wave,
the priority order is: H3 (real win, upgrades HZ-IV from vacuous
to genuine on two of four paths) → H2 (scope rectification on
CLAUDE.md row, atomic) → H1 (AP272 heal, requires new lemma
inscription) → H4 (mechanical count fix, bundle with H2).

Cross-volume propagation note (for the future heal wave): H2
also requires updating Vol I CLAUDE.md Toroidal chiral QG row
("PROVED formal-disk via DIM + SV CoHA; global P¹×P¹ conditional
on class-M chain-level") — currently consistent, no drift. Vol II
has no canonical 6d hCS codim-2 row to propagate to.

## Cache entries (confusion patterns, to append on heal-commit)

Pattern #P-6d-1: 6d hCS → 5d boundary KM level via equivariant
1-loop determinant on normal bidisk, k_eff = −σ_2(h). Do not
conflate the Omega-background TWIST of the trace form with the
gl_1 level data; the twist is a one-loop geometric effect, and
the level is the VALUE of the twist.

Pattern #P-6d-2: Sugawara c = dim(g)·k/(k+h^∨). At abelian gl_1
(h^∨ = 0), c = 1 FOR ALL k. This is a gl_1-specific feature
and should not be read as "c=1 is Sugawara" universally. For
non-abelian g, c depends on k.

Pattern #P-6d-3: Test count discipline — when adding a
`@independent_verification` decorator to an existing suite of N
tests, update both the status row and the in-chapter Remark in
the same commit (AP256 + AP149 combined). Do not let "N tests"
in CLAUDE.md drift against "N-1 tests + 1 HZ-IV" in the chapter.

## Falsification tests (for future wave)

F1. The propagator-twist computation. Compute the equivariant
∂̄-determinant on the formal bidisk D² with weights (h_2, h_3)
under the torus T² = C*_{z_2} × C*_{z_3}, regularised via
heat-kernel / zeta regularisation. Verify the resulting effective
trace-form on gl_1 has prefactor −(h_1 h_2 + h_1 h_3 + h_2 h_3)
= −σ_2. If instead one obtains −σ_3/σ_1, or h_2 h_3, or any
expression that does not reduce to −σ_2 under the CY constraint,
the derivation Step 3 is wrong.

F2. At the degenerate point σ_2 = 0 (e.g. h_1=0, h_2=0, h_3=0, or
non-trivial solutions of h_1 h_2 + h_1 h_3 + h_2 h_3 = 0 under
h_1+h_2+h_3=0), the defect algebra should be the TRIVIAL Heisenberg
(Ψ=0, abelian constant currents). Test: at such points,
`ope.JJ_ope()[1] == 0` AND the Sugawara construction is undefined
(division by zero). The engine passes this test (line 310-316 of
the test file).

F3. Triality (S_3-permutation invariance). Under any permutation
σ ∈ S_3 of (h_1,h_2,h_3), Ψ and σ_2 are invariant; so the defect
algebra is the same. Test passes (line 140-150 of the test file).
This is the Miki-triality of the DIM algebra projected to C.

HZ-7 κ-subscript compliance: throughout this note, every κ appears
subscripted (`κ_{ch}`, `κ_{BKM}`, `κ_{cat}`, `κ_{fiber}`) per Vol
III discipline; bare κ is absent. The κ_ch(W_{1+∞}|_{c=1}) = 1
value lives in `modular_koszul_bridge.tex:366`. No new κ-claims
are introduced in this wave.
