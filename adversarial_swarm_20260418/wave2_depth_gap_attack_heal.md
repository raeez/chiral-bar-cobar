# Wave-2 Attack-and-Heal: Depth gap trichotomy `d_alg ∈ {0,1,2,∞}`

Target: CLAUDE.md Depth gap row + §Key Constants + AP131 + FM18. Anchor:
`prop:depth-gap-trichotomy` at
`chapters/theory/higher_genus_modular_koszul.tex:18208` (with
`lem:depth-three-impossible` at :18127, `rem:contact-stratum-separation`
at :19804). Status claim: PROVED — `d_alg ∈ {0,1,2,∞}`, d_alg = 3 impossible
via MC relation + shadow Lie Jacobi, βγ_λ witness at d_alg = 2, Vir/W_N at
d_alg = ∞.

## Attack ledger

Seven adversarial probes, verdicts against Vol~I source:

**A1 (Gelfand / environment-vs-content).** Is `prop:depth-gap-trichotomy`
inscribed as a proposition with a proof body, or a remark-level corollary
of the per-family census? **Verdict: PROPER PROPOSITION.** Environment
`\begin{proposition}` with `\ClaimStatusProvedHere`; 114-line proof body
(:18242–:18356); three enumerated clauses (i)–(iii) matching the four
classes G/L/C/M. Not a remark.

**A2 (Beilinson / rigorous-vs-pattern-match).** Is "d_alg = 3 impossible
via MC relation + shadow Lie Jacobi" a RIGOROUS obstruction with a named
cohomology class and Jacobi-contradiction structure, or a pattern-match
"no known algebra has d_alg = 3"? **Verdict: TWO INDEPENDENT PROOFS, both
computational, not pattern-match.** `lem:depth-three-impossible`
(:18127–:18206) has two proof passes on every κ ≠ 0 primary line L:
(a) MC recursion at r = 5, 6: if S_4 ≠ 0 and α = S_3 = 0 then S_5 = 0 but
S_6 = −(2 S_4²)/(3κ) ≠ 0; if α ≠ 0 and S_4 ≠ 0 then S_5 = −(6/5) P α S_4
≠ 0 directly; (b) shadow Lie algebra raising operator: D_𝔔(x^{2m}) =
(8m P S_4) x^{2m+2} ≠ 0 for all m ≥ 2, so S_4 ≠ 0 forces nonzero shadows
at all even r ≥ 6. Neither is pattern-match: both are explicit recursion
identities on the Gaussian decomposition Q_L(t) = (2κ + 3α t)² + 2Δ t²
with Δ = 8κ S_4.

**A3 (Drinfeld / closed-form collapse).** Does the closed form
H(t) = t² √(Q_L(t)) (Theorem riccati-algebraicity, same file :17965)
make infinite extent manifest when Δ ≠ 0? **Verdict: YES.** Q_L is a
polynomial in t of degree 2 in k(c)[t]. When Δ ≠ 0 it is not a perfect
square (the interaction correction 2Δ t² prevents it), so the binomial
series (1 + u)^{1/2} does not terminate. Finite d_alg ≥ 3 requires
√(Q_L) to be polynomial of degree exactly d_alg − 2, which is impossible
for a non-square irreducible quadratic.

**A4 (Kazhdan / d_alg = 2 witness).** Is the βγ_λ proof of d_alg = 2
inscribed as a proposition with explicit OPE-level derivation, or
"observed from OPE analysis"? **Verdict: INSCRIBED.** Dependencies
resolve: `thm:betagamma-global-depth` at
`chapters/examples/free_fields.tex:1192`; `thm:betagamma-rank-one-rigidity`
at `chapters/examples/beta_gamma.tex:2560`;
`cor:nms-betagamma-mu-vanishing` and `prop:betagamma-T-line-shadows` all
inscribed. The proof gives the full shadow tuple: S_2 = 6λ² − 6λ + 1,
S_3 = 0, S_4 = −5/12, S_r = 0 (r ≥ 5). The value d_alg = 2 is a
global-stratum witness (not single-line): on the T-line S_4 ≠ 0 gives a
tail, but the charged quartic μ_βγ = 0 by rank-one abelian rigidity on
the weight-changing stratum, and assembly over the full λ-family gives
r_max = 4.

**A5 (Nekrasov / multi-generator closure).** The "decouple-or-cubic-pump"
dichotomy extending single-line Riccati to multi-generator algebras
routes through `rem:contact-stratum-separation` at :19804. This is a
REMARK, load-bearing inside the proposition proof (cited 4× between
:18317 and :18657). **Verdict: ENVIRONMENT-vs-CONTENT MISMATCH
(AP40-adjacent).** The remark contains substantive mathematical content
(charge-graded master equation, non-nilpotent cubic pump, rank-n abelian
cross-sector obstruction), but it carries no ClaimStatus tag and is
cited as if a lemma. Content is correct and verifiable; environment is
understated. This is not a falsification — the remark is demonstrably
consistent with the single-line Riccati machinery — but a reader auditing
the proof chain must cross to a Remark to find the load-bearing rigidity.

**A6 (Kapranov / class M per-family).** Is class M d_alg = ∞ proved
uniformly or per-family (Vir via Li filtration; W_N via DS reduction)?
**Verdict: UNIFORMLY via Riccati with Δ ≠ 0 plus per-family S_4
verification.** The proposition gives the uniform mechanism: Δ ≠ 0 ⇒
d_alg = ∞. Per-family S_4 ≠ 0 is inscribed independently: Virasoro
S_4 = 10/[c(5c+22)] verified across 15+ chapter sites (e.g.
`preface.tex:1585`, `bv_brst.tex:2178`, `w_algebras.tex:4510`); W_N
inherits via the W_2 = Vir base case plus screening construction.

**A7 (Costello / gap-at-3 scope: empty-vs-conjecturally-empty-vs-proved-empty).**
Is d_alg = 3 (a) empty in the census, (b) conjecturally empty, or (c)
proved empty? **Verdict: (c) PROVED EMPTY on the standard landscape.**
The proposition proves d_alg = 3 (and any finite d_alg ≥ 3) is
unrealizable under the hypotheses "chirally Koszul algebra in the
standard landscape." The scope is explicit: standard landscape. This is
not universal across all chiral algebras — logarithmic families and
non-standard generator sets are outside hypothesis. The CLAUDE.md
"d_alg ∈ {0,1,2,∞}; gap at 3 impossible" is accurate on the standard
landscape; a scope qualifier is advisable.

## Surviving core (Drinfeld voice, 3 sentences)

On every chirally Koszul algebra in the standard landscape, the shadow
tower's Riccati generating function H(t) = t² √(Q_L(t)) forces the
algebraic depth d_alg to lie in {0, 1, 2, ∞}: the Gaussian decomposition
Q_L = (2κ + 3α t)² + 2Δ t² is either a perfect square (Δ = 0, finite
tower of degree ≤ 3) or an irreducible non-square quadratic (Δ ≠ 0,
√Q_L non-polynomial, infinitely many shadow coefficients), with no
intermediate finite depth ≥ 3 admissible. The boundary value d_alg = 2
is the unique contact class accessible only by assembling multiple
primary lines (βγ_λ / bc_λ), where the charged quartic μ = −5/12 survives
but rank-one abelian rigidity kills r ≥ 5. The dichotomy between
single-line Riccati and multi-line stratum separation is proved in the
proposition proof, with the multi-generator closure (decouple-or-cubic-pump)
routing through the charge-graded master equation.

## Heal plan

No structural downgrade required. Three minor scope/environment
improvements:

**H1 (scope qualifier on CLAUDE.md Key Constants).** The statement
"d_alg ∈ {0,1,2,∞} (depth gap: 3 impossible, prop:depth-gap-trichotomy)"
should read: "d_alg ∈ {0,1,2,∞} on the chirally Koszul standard
landscape (depth gap: 3 impossible, prop:depth-gap-trichotomy)." Adds
one scope qualifier; no mathematical change.

**H2 (environment upgrade for `rem:contact-stratum-separation`).**
The remark carries load-bearing content for the multi-generator half of
the depth-gap proof. Two options: (a) upgrade to `\begin{proposition}`
with `\ClaimStatusProvedHere` and the title "Multi-generator depth-gap
extension via stratum separation"; (b) inline the remark's content into
the proposition proof body (currently it is cited back as a forward
reference within the proof, :18317; the content is already partially
inlined). Option (a) cleanest — yields an explicit labelled proposition
that the main theorem calls. Recommended as a future edit, not a
blocking frontier item.

**H3 (AP131 / FM18 consistency).** AP131 and FM18 both note "d_gen(Vir)=3,
d_alg(Vir)=∞." This is consistent with the proof: d_gen is the finite
generator count; d_alg is shadow-tower depth; they decouple for Vir (3
strong generators do not bound the bar-level obstruction tower).
Retain AP131/FM18 verbatim.

## Commit plan

No commits. Note-only deliverable. If H1 or H2 are executed in a later
pass, batch them with the AP131/FM18 CLAUDE.md touchup in one commit
authored by Raeez Lorgat.

## Residual frontier

None of Beilinson-audit severity. The proposition is rigorously inscribed
with two independent proof passes (MC recursion and shadow-Lie raising
operator), a verified d_alg = 2 witness, a uniformly-argued class M, and
a closed-form Riccati discriminant obstruction ruling out finite d_alg ≥ 3
on any κ ≠ 0 line. The gap-at-3 impossibility is PROVED on the stated
scope, not pattern-matched. The only open-texture items are (a) the
stratum-separation remark's load-bearing use inside the proof (H2) and
(b) an optional scope qualifier on CLAUDE.md (H1).
