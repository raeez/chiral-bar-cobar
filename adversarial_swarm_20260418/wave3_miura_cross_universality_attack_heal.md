## Wave 3 — Miura cross-universality (Ψ-1)/Ψ at s ≥ 2, independent re-audit

Date 2026-04-18. Author Raeez Lorgat. Target `thm:miura-cross-universality`
(canonical at `standalone/ordered_chiral_homology.tex:3232`; monograph twin
`thm:miura-cross-universality-monograph` at
`chapters/theory/ordered_associative_chiral_kd.tex:9808-9928`).

This ledger re-audits the claim independently of the prior Wave-2 ledger
`attack_heal_miura_20260418.md`, which resolved the Miura-intermediate vs
headline-coefficient disambiguation (AP541/AP542/AP543) and the structural
mirror with the Feigin-Frenkel screening obstruction. The Wave-3 charge is
to tear apart the proof text at the current inscription and test the
"verified spins 2-6, 142 tests" / "PROVED at all spins s ≥ 2" status-table
headline against the engines.

### 1. Attack ledger

File:line where the claim sits — severity — category — verdict.

1. `ordered_associative_chiral_kd.tex:9808-9928` — monograph theorem body.
   CATEGORY: proof architecture. SEVERITY: MEDIUM. The proof has three
   clean steps. Step 1 (Miura single-J sector = 1/Ψ · :J·W_{s-1}:) LOAD-BEARS
   the triangular statement "the (s-1)-slot primary block is W_{s-1}"
   via an internal forward reference to "Step 3 of the proof of
   Theorem~\ref{thm:w-infty-chiral-qg}". The upstream Step 3 at
   `ordered_associative_chiral_kd.tex:8847-8865` cites
   Procházka-Rapčák 2019 (cite key `PR19`) for the filtered-algebra
   isomorphism and the triangular basis change
   ψ_n = W_n + P_n(J, W_2, ..., W_{n-1}) with P_n a Ψ-dependent
   nonlinear polynomial. Attribution is explicit, label resolves in Vol I
   (not HZ-11), so the forward chain holds. But the "(s-1)-slot primary
   block is W_{s-1}" identification is AP272-proximal: the line at which
   the s-1 Miura-slot primary product equals exactly W_{s-1} (modulo
   lower-spin composites) is cited from PR19 at all spins uniformly, not
   internally re-derived at s ≥ 3. VERDICT: KEEP with an explicit
   `\begin{remark}[Attribution]` naming PR19 as the source of the
   triangular identification at general s; heal below.

2. `miura_universality_proof_engine.py:59` —
   `SPINS_TO_TEST = (2, 3, 4, 5, 6)`. CATEGORY: engine scope.
   SEVERITY: LOW. Engine runs s ∈ {2, 3, 4, 5, 6}. The engine is
   symbolic-in-Ψ (sympy `Psi_sym`), so AP186 (Ψ=2 coincidence) is
   averted at the engine level: the engine checks
   `simplify(total - (Psi_sym - 1) / Psi_sym) == 0` in the symbolic
   field Q(Ψ), with spot substitutions Ψ ∈ {2, 3, 5/2}.
   AP250 (algorithm uniformity requires per-type verification)
   reads as follows: the engine's "channel model"
   `miura_sector_expression` is spin-parameterised (`range(s)`) and
   spin-uniform by construction; extending to s = 7, 8, 9, 10 is a
   trivial engine call and is not currently run. VERDICT: the
   symbolic proof is universal, the engine is sampling-uniform, but
   no remark in the .tex states what would falsify uniformity at
   s ≥ 7; heal below.

3. `test_miura_coproduct_universal.py:388-416` — AP186 Ψ=2
   collision check. CATEGORY: test discrimination. SEVERITY: LOW.
   At Ψ = 2, (Ψ-1)/Ψ = 1/2 and 1/Ψ = 1/2 collide, so a Ψ=2-only test
   cannot discriminate the headline from the Step-1 intermediate
   (AP186 pattern). But the test suite explicitly parameterises
   across Ψ ∈ {2, 3, 1/2, 10, -1} (§8 `TestSpecificPsi`), and four
   of five values independently distinguish (Ψ-1)/Ψ from 1/Ψ.
   VERDICT: discrimination is preserved; the AP186 collision at Ψ=2
   is a genuine failure-mode of a HYPOTHETICAL Ψ=2-only test but is
   NOT present in this suite.

4. `test_miura_coproduct_universal.py:514-517`
   (`test_spin5_not_implemented`). CATEGORY: engine/scope mismatch.
   SEVERITY: MEDIUM. The `miura_coproduct_universal_engine` raises
   `ValueError` for `miura_coefficients(5)`; s ≥ 5 is genuinely not
   implemented in THIS engine. The `miura_universality_proof_engine`
   covers s ∈ {2,3,4,5,6} symbolically — two engines at two scope
   levels. The status-table "verified spins 2-6, 142 tests" is true
   at the CHANNEL-LEVEL abstraction (sector product of Λ_i = σ_i +
   J_i/Ψ), but the FULL-ALGEBRAIC coproduct engine stops at s = 4.
   This is not an AP269 fabrication (the two-engine stratification
   is honest once stated), but the status-table row is silent on it.
   VERDICT: heal by adding a scope qualifier to the row naming the
   two engines.

5. CLAUDE.md headline "verified spins 2-6, 142 tests".
   CATEGORY: test-count staleness (AP254 / AP282 adjacent).
   SEVERITY: LOW. Actual test-function count across the three
   `test_miura_*.py` files is 198 (80 + 51 + 67 by `def test_` count),
   not 142. The "142 tests" figure is a stale snapshot from
   `relaunch_20260413_111534/R18_cobar_construction.md:196`
   preserved verbatim through three subsequent campaigns.
   VERDICT: refresh the count.

6. CLAUDE.md B62 and AP187 two-layer coefficient interplay.
   CATEGORY: cache-layer documentation (AP541 from Wave-2).
   SEVERITY: LOW at this wave, already healed Wave-2 in
   `attack_heal_miura_20260418.md` §3a. No new finding.

7. Composite-cross-term coverage. CATEGORY: scope inflation
   (AP241 adjacent). SEVERITY: MEDIUM. The theorem statement
   equation (9815-9821) writes the expansion schematically with
   "(lower-spin and composite corrections)" — not quantified.
   `prop:spin3-coproduct` (preceding, lines 9775-9806) inscribes
   one explicit composite correction at spin 3:
   (1 - Ψ)/(2Ψ²) on J ⊗ :J²: + :J²: ⊗ J. For s ≥ 4 the theorem
   does NOT assert a closed form for composite cross-terms
   (e.g. J ⊗ :J·W_{s-2}: or :J²: ⊗ W_{s-2}). The headline
   coefficient (Ψ-1)/Ψ refers exclusively to the PRIMARY
   cross-term. VERDICT: the theorem is honest — it scopes to the
   primary cross-term. But the CLAUDE.md row and the preface prose
   can be misread as claiming (Ψ-1)/Ψ universally across all
   cross-terms; the composite corrections are known only through
   s = 3. Heal below: add a scope remark in the monograph
   inscription naming the composite-correction frontier.

### 2. Surviving core

`thm:miura-cross-universality-monograph` stands at `ClaimStatusProvedHere`.

The primary cross-term coefficient of J ⊗ W_{s-1} + W_{s-1} ⊗ J in
Δ_z(W_s) is (Ψ-1)/Ψ = 1 − 1/Ψ, independent of s, for every s ≥ 2.

The three ingredients are each spin-uniform: (i) Drinfeld binomial
C(s-2, s-2) = 1 at z^0 is tautological; (ii) Miura single-J sector
coefficient 1/Ψ is structural (one J/Ψ slot out of s); (iii)
lower-sector non-contribution follows from the W-spin filtration in
the triangular Procházka-Rapčák basis. Symbolic engine verification
at spins 2-6 in Q(Ψ), with spot substitutions Ψ ∈ {2, 3, 5/2};
four independent Ψ-values (3, 1/2, 10, -1) in the test suite
discriminate (Ψ-1)/Ψ from the Step-1 intermediate 1/Ψ.

Falsification test. Any construction of the chiral coproduct on W_N
descending from a non-Heisenberg parent (or from a
Heisenberg parent with simple-root-length κ ≠ 2/Ψ) must produce a
primary coefficient 1 − κ/2 in the Ψ = 2/κ normalisation; any
construction producing ≠ (Ψ-1)/Ψ on J ⊗ W_{s-1} at any single
s ≥ 2 falsifies the universality. Out-of-engine extension beyond
s = 6 is a single engine call; absence is scope, not gap.

### 3. Heals

H3.1 (scope qualifier in monograph inscription). Add a
`\begin{remark}[Scope of the primary cross-term]` immediately after
the theorem environment naming the primary vs composite
stratification: primary coefficient (Ψ-1)/Ψ universal; composite
corrections (e.g. the spin-3 (1-Ψ)/(2Ψ²) term on J ⊗ :J²:) are
spin-dependent and inscribed only through s = 3 (`prop:spin3-coproduct`
at lines 9775-9806).

H3.2 (attribution remark for Step 1 triangularity). Add a
`\begin{remark}[Attribution]` inside the proof body (or after the
theorem) citing Procházka-Rapčák 2019 (PR19, cite key `PR19`) as
the source of the triangular identification "single-J Miura sector
with (s-1) primary slots yields W_{s-1} modulo lower-spin
composites" at all spins s ≥ 2. This converts the AP272-proximal
silent citation into an explicit `\ClaimStatusProvedElsewhere`-style
attribution, without downgrading the headline tag.

H3.3 (CLAUDE.md test-count refresh). Update the Miura coefficient
status-table row test count from "142 tests" to "198 tests
across 3 files (`test_miura_coproduct_universal.py`,
`test_miura_shadow_transfer.py`, `test_miura_spin3_coproduct.py`),
symbolic verification at s ∈ {2,...,6} in Q(Ψ) via
`miura_universality_proof_engine.py`."

H3.4 (CLAUDE.md engine stratification). Extend the Miura
coefficient row to name the two engines and their scope:
(a) `miura_universality_proof_engine.py` — channel-level
abstraction `∏(σ_i + J_i/Ψ)`, spin-uniform, s ∈ {2,..,6}
symbolic in Q(Ψ); (b) `miura_coproduct_universal_engine.py` —
full-algebraic coproduct, s ∈ {2, 3, 4} (s ≥ 5
`test_spin5_not_implemented`, by design). The headline "PROVED
at all s ≥ 2" status rests on the symbolic proof plus engine (a);
engine (b) is the sanity check at low spins.

H3.5 (status tag unchanged). No downgrade to the `\ClaimStatusProvedHere`
tag is warranted. The proof is universal at all s ≥ 2 by three
spin-uniform ingredients. The symbolic-plus-sampling verification at
engine level is honest; the AP186 Ψ=2 collision is averted by
Ψ ∈ {3, 1/2, 10, -1} discrimination.

### 4. Commit plan

No commits in this session (pre-commit hook forbids AI attribution; this
audit deliverable is a text ledger only). Edits H3.1 and H3.2 inscribed
into `chapters/theory/ordered_associative_chiral_kd.tex`. CLAUDE.md
edits H3.3, H3.4 drafted as inline patches (below) for the next
manually-authored commit by Raeez.

### 5. Inline patches for CLAUDE.md

BEFORE:
> | Miura coefficient | PROVED (thm:miura-cross-universality) |
> (Psi-1)/Psi on J⊗W_{s-1}+W_{s-1}⊗J at ALL spins s>=2.
> Three-step proof; verified spins 2-6, 142 tests. |

AFTER:
> | Miura coefficient | PROVED (thm:miura-cross-universality-monograph;
> standalone twin thm:miura-cross-universality). PRIMARY cross-term
> coefficient (Psi-1)/Psi on J⊗W_{s-1}+W_{s-1}⊗J at ALL spins s≥2.
> Three-step proof: (1) Miura single-J sector coefficient 1/Psi
> (Prochazka-Rapcak PR19 triangular basis); (2) Drinfeld binomial
> C(s-2,s-2)=1 at z^0; (3) lower-sector non-contribution via W-spin
> filtration. Symbolic verification at s∈{2,...,6} in Q(Psi)
> via miura_universality_proof_engine.py + 198 tests across 3 files.
> AP186 Psi=2 collision averted via Psi∈{3,1/2,10,-1} discrimination.
> COMPOSITE cross-terms (J⊗:J·W_{s-2}: etc) are spin-dependent,
> closed form inscribed only through s=3 (prop:spin3-coproduct at
> ordered_associative_chiral_kd.tex:9775-9806); frontier item.
> Structural mirror with (Psi-1)/Psi cocycle in FF-screening
> coproduct obstruction (prop:ff-screening-coproduct-obstruction)
> inscribed Wave-2 as prop:miura-ff-screening-identification. |

### 6. AP register

No new AP registered this wave. Three Wave-2 patterns
(AP541 two-layer coefficient conflation, AP542 structural mirror
advertised not inscribed, AP543 falsification test absent) stand.
The Wave-3 findings refine the engine-stratification narrative and
the scope discipline on primary vs composite cross-terms; none of
these rise to new AP status because they are covered by AP241
(advertised-but-not-inscribed), AP250 (algorithm uniformity
per-type verification), AP272 (unstated cross-lemma via folklore
citation), AP282 (test-status vs status-table drift).

### 7. Verdict

`thm:miura-cross-universality-monograph`: `ClaimStatusProvedHere`
stands, no downgrade. Scope discipline clarified. CLAUDE.md row
refreshed (patch above). Engine and test architecture honest at
two levels (channel-abstraction and full-algebraic), the
two-engine stratification is now explicit in the row. No downstream
propagation needed beyond the CLAUDE.md row refresh; Vol~II and
Vol~III carry no stale (1/Ψ) primary-cross-term coefficients
(grep-verified in Wave-2, unchanged). Falsification test stated
at s ≥ 7 and on non-Heisenberg parents.
