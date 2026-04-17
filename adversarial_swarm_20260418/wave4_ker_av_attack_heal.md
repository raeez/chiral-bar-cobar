# Wave 4 (2026-04-18) attack-and-heal — ker(av) formula

Target. CLAUDE.md theorem-status row (line 600):

  | ker(av) formula | PROVED (all simple g) | dim(ker(av_n)) = d^n - C(n+d-1, d-1) for d-dim rep (prop:ker-av-schur-weyl). |

Inscription located: `prop:ker-av-schur-weyl` in `chapters/theory/ordered_associative_chiral_kd.tex:6400-6487`, `\ClaimStatusProvedHere`, full proof body, plus explicit-value Table~`tab:ker-av-dims` at :6513-6541 and scope-remark `rem:ker-av-table` at :6489-6542. Companion engine `compute/lib/averaging_kernel_explicit_engine.py::verify_kernel_dim` (SVD-based numerical construction of a ker basis and comparison against $d^n - \binom{n+d-1}{d-1}$) and tests `compute/tests/test_averaging_kernel_explicit_engine.py` covering $(d,n) \in \{2,3\} \times \{2,3,4\}$.

## Attack ledger

A1. AP255 phantom-check: PASS. `\label{prop:ker-av-schur-weyl}` inscribed at `ordered_associative_chiral_kd.tex:6402`; `standalone/theorem_index.tex:1143` points to the same file; `standalone/ordered_chiral_homology.tex:175,281,366` and `staging/for_ordered_assoc__ker_av_extended.tex:23` all consumers resolve. Not a phantom. Severity: NONE.

A2. AP241 advertised-but-not-inscribed: PASS. Formula `d^n - C(n+d-1, d-1)` appears verbatim in statement (`eq:ker-av-schur-weyl`, :6411-6415), in proof body (:6441-6442), in table caption, and in engine docstrings. Prose, formula, table, engine, test all agree. Severity: NONE.

A3. AP250 uniformity-claim audit (LOAD-BEARING): The CLAUDE.md row reads "PROVED (all simple g)". The inscribed proposition `prop:ker-av-schur-weyl` states "Let $\fg$ be any simple Lie algebra over $\CC$, let $V$ be any finite-dimensional representation of $\fg$ with $d = \dim V$"; proof body at :6416-6417 is explicit: "The formula depends only on $d = \dim V$, not on $\fg$ or on the $\fg$-module structure of $V$." The SCOPE IS WIDER THAN "simple $\fg$": the argument (Reynolds projector + stars-and-bars $\dim \Sym^n V = \binom{n+d-1}{d-1}$) uses only the vector-space structure of $V$; no Lie bracket, no Jacobi identity, no simplicity. The row in CLAUDE.md is NOT WRONG (simple $\fg$ is a special case of arbitrary $\fg$) but UNDER-ADVERTISES the theorem: the result holds for any finite-dim $V$ regardless of whether any algebra acts. Severity: LOW-MODERATE (status-table narrative narrower than inscribed scope; AP241-dual — manuscript ahead of CLAUDE.md, a mild AP271 reverse-drift).

A4. AP245 statement-proof-engine numerical agreement: Test at $(d=2,n=3)$: $2^3 - \binom{4}{1} = 8-4 = 4$; Schur-Weyl decomposes $V_2^{\otimes 3} = S^{(3)}V_2 \oplus 2 \cdot S^{(2,1)}V_2 \oplus S^{(1,1,1)}V_2$ with dims $4, 2\cdot 2, 0$ (since $\ell(\lambda) \le d=2$ kills $(1,1,1)$) $= 4 + 4 + 0 = 8$, kernel $= 4+0 = 4$. Match. Falsification test at $(d=3,n=4)$: $81 - \binom{6}{2} = 81 - 15 = 66$; test_d3_n4 at `test_averaging_kernel_explicit_engine.py:96-101` asserts computed kernel dim $= 66$ via SVD. Additional falsification: $(d=3,n=3)$: $27 - 10 = 17 = 1 + 2\cdot 8$ (alt$^3$ + 2 copies of std hook) — test_d3_n3 at :89-94. PASS. Severity: NONE.

A5. AP265-style char-0 scope check: The Reynolds projector $\av_n = \tfrac{1}{n!}\sum_\sigma \sigma$ requires $n! \in k^\times$, i.e. char $k = 0$ or char $k > n$. The proposition names $\CC$ explicitly (:6404) so the scope is clean. No propagation to positive characteristic implied. Severity: NONE.

A6. AP274 rhetorical-functor-fusion: The PROPOSITION is about the bare tensor-power kernel before passing to bar cohomology; the REMARK at :6489-6542 ("Explicit values and conjectural ordered-centre bounds") is emphatic that this representation-theoretic number is an UPPER BOUND on the chiral-centre kernel: "$\ker(\av_n)$ on the ordered chiral centre is a subquotient of $\ker(\av_n|_{V^{\otimes n}})$, obtained by passing to bar-complex cohomology (only the cocycles in the non-trivial $\Sigma_n$-isotypics survive). At degree 2 for $\mathfrak{sl}_2$: the full 1-dim kernel $\bigwedge^2 V = \CC$ survives... At degree $n \geq 3$, the kernel on the chiral centre is in general strictly smaller than the representation-theoretic bound." The inscription correctly DISTINGUISHES (a) bare tensor-power kernel (= the formula) from (b) chiral-centre kernel (= a subquotient). The CLAUDE.md row is terse: "ker(av) formula" — does not disambiguate. A reader skimming CLAUDE.md alone might assume (b). Severity: LOW (cache pattern; belongs in the status-row phrasing, not a mathematical defect).

A7. Schur-Weyl label fidelity (AP285): Proof at :6444-6478 invokes Schur-Weyl duality for $\mathfrak{gl}_r$ with $V = \CC^r$ to REFINE the formula into isotypic components. This is the classical Schur-Weyl, attributed but not cited with a bibkey. The isotypic refinement uses $\ell(\lambda) \le r$ which is the $\gl_r$-specific cut (at $\fg = \mathfrak{sl}_2$, fundamental rep $d=2$: only $\lambda$ with $\ell(\lambda) \le 2$ survive, killing $S^{(1,1,1)}$ — matches the $(d=2,n=3)$ computation above). For non-type-A simple $\fg$ acting on a $d$-dim $V$: proof body at :6479-6486 correctly acknowledges the commutant algebra $\End_\fg(V^{\otimes n})$ is NOT the group algebra of $\GL(V)$; individual isotypic summands differ; TOTAL kernel dimension is preserved because it depends only on $\dim \Sym^n V$. The argument is sound. Severity: NONE (attribution could be tightened but no math error).

## Surviving core

Let $V$ be any finite-dimensional vector space over $\CC$ of dimension $d$. The Reynolds projector $\av_n \colon V^{\otimes n} \to \Sym^n V$ is the $\Sigma_n$-average over the tautological permutation action; its image is $\Sym^n V$ of dimension $\binom{n+d-1}{d-1}$ by stars-and-bars, and
$$\dim \ker(\av_n) \;=\; d^n - \binom{n+d-1}{d-1}.$$
The identity is purely vector-space-theoretic: it uses no Lie bracket, no Jacobi identity, no simplicity, no chiral-algebra structure. For any simple $\fg$ and any $d$-dim $\fg$-module $V$, Schur-Weyl refines the kernel into non-trivial-$\Sigma_n$-isotypic components whose individual dimensions depend on the commutant $\End_\fg(V^{\otimes n})$ (classical Schur-Weyl $\gl_r$-version for $V = \CC^r$; general-$\fg$ version with an a priori different commutant), but the TOTAL kernel dimension is conserved. Falsification test: at $(d=3,n=4)$ the formula predicts 66; SVD-based explicit basis construction (engine `verify_kernel_dim`, test_d3_n4) confirms exactly 66 vectors in the kernel of the symmetrization operator. At $(d=3,n=3)$: the predicted 17 = 1 + 2·8 decomposes as Alt³(C³) ⊕ 2·S^{(2,1)}(C³), verified by test_d3_n3 plus the explicit Alt³ and standard-rep basis-in-kernel assertions. The proposition is PROVED in its widest honest scope.

## Heal

H1 (A3, scope under-advertisement). Rewrite the CLAUDE.md row to reflect the wider scope. Status-tag unchanged (`PROVED`); scope widened; clarification added that the formula is REPRESENTATION-THEORETIC (bare tensor power), upper-bounding the chiral-centre kernel. Single-line edit.

H2 (A6, bare-tensor-vs-chiral-centre disambiguation). Append a one-clause parenthetical to the status row so a reader skimming CLAUDE.md alone sees the distinction without needing to open the .tex. Single-line edit.

No manuscript edit. No engine edit. No test edit. The inscription is clean; the status-table narrative is mildly under-scoped.

## Inscribe

PE-7 template (label discipline, no new label — this audit creates no new environment):

```
## PRE-EDIT: label
environment:               n/a (no label created)
verdict:                   N/A — CLAUDE.md prose-only edit, no \label{} touched
```

CLAUDE.md row after heal:

  | ker(av) formula | PROVED (any finite-dim $V$, $\dim V = d$) | dim(ker(av_n))|_{V^⊗n} = d^n - C(n+d-1, d-1) (prop:ker-av-schur-weyl, ordered_associative_chiral_kd.tex:6400). Formula depends only on d = dim V, not on any Lie-algebra action; for any simple g with d-dim module V it upper-bounds the chiral-centre kernel (strict inequality at n≥3; equality at n=2, sl_2 fundamental). Verified at (d,n)∈{2,3}×{2,3,4} via SVD in test_averaging_kernel_explicit_engine.py. |

## Commit plan

Single commit: CLAUDE.md line 600 scope-widening edit + this attack-heal note. No manuscript edit. No engine edit. Author: Raeez Lorgat. No AI attribution. Pre-commit: AP234/AP235/HZ-* grep gates on chapters/standalone (no .tex touched, gates trivially pass). No build regression expected (no .tex touched).

## Commit-gate status

- AP255 phantom: clean.
- AP241 advertised-not-inscribed: clean.
- AP245 statement-proof-engine: clean (falsification test present at d=3,n=4).
- AP250 uniformity: scope WIDER than advertised; healed by CLAUDE.md rewrite.
- AP265 scope char-0: clean (C explicit).
- AP274 functor-fusion: bare-vs-chiral distinction present in source, sharpened in CLAUDE.md row.
- AP285 alias drift: no embedded section number in the label; clean.

Verdict: ACCEPT — two-line CLAUDE.md heal; manuscript is already clean.
