# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} = shadow depth, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,500pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,500pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~200pp). Total ~4,200pp, 119K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

## The Beilinson Principle

"What limits forward progress is not the lack of genius but the inability to dismiss false ideas." Every claim is false until independently verified from primary source. Prefer a smaller true theorem to a larger false one. Every numerical claim requires 3+ genuinely independent verification paths (direct computation, alternative formula, limiting case, symmetry/duality, cross-family, literature+convention, dimensional analysis, numerical evaluation).

**Epistemic hierarchy** (higher wins): (1) Direct computation > (2) .tex source +/-100 lines > (3) Build system > (4) Published literature > (5) concordance.tex > (6) This file > (7) Memory. Before every assertion: "How do I know this? Read the source, computed it, or assumed it?" If assumed, stop and verify.

## The Five Objects (NEVER CONFLATE)

A (algebra) -- B(A) (bar coalgebra) -- A^i=H*(B(A)) (dual coalgebra) -- A^!=((A^i)^v) (dual algebra) -- Z^der_ch(A) (derived center = bulk). Omega(B(A))=A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.

## Key Constants

kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(Heis)=k. kappa(W_N)=c*H_{N-1}. Vir^!=Vir_{26-c}. Self-dual at c=13. kappa+kappa'=0 (KM/free), 13 (Vir). QME: hbar*Delta*S+(1/2){S,S}=0. sl_2 bar H^2=5 (not 6). Desuspension: |s^{-1}v|=|v|-1, NOT +1. eta(q)=q^{1/24}*prod(1-q^n). Bar propagator d log E(z,w): ALWAYS weight 1. Prime form: section of K^{-1/2} boxtimes K^{-1/2}. FM_n(X): blowup along diagonals, NOT complement. Grading: COHOMOLOGICAL (|d|=+1). Curved A-inf: m_1^2(a)=[m_0,a]. Bar d^2=0 always; curvature appears as m_1^2 != 0.

## Theorem Status

| Thm | Status | Key result |
|-----|--------|------------|
| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
| B | PROVED | Bar-cobar inversion: Omega(B(A)) -> A qi on Koszul locus |
| C | PROVED | Complementarity; C1 (eigenspace) unconditional, C2 (scalar) uniform-weight |
| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
| H | PROVED | ChirHoch*(A) polynomial in {0,1,2}, dim<=4 |
| MC1-5 | ALL PROVED | PBW, MC element, thick gen (all types), completion tower, analytic sewing |
| Koszul | 10+1+1 | 10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir) |
| D^2=0 | PROVED | Convolution (M-bar_{g,n}) + ambient (Mok25 log FM) |
| Theta_A | PROVED | Bar-intrinsic; all-arity inverse limit (thm:recursive-existence) |

## Anti-Patterns by Cognitive Trigger

### BEFORE WRITING A FORMULA

**kappa** (AP1,9,20,24,48): DISTINCT per family, NEVER copy. KM=dim(g)(k+h^v)/2h^v, Vir=c/2, W_N=c*H_{N-1}, Heis=k. Always qualify: kappa^{KM}, kappa^{Vir}. Complementarity: kappa+kappa'=0 (KM/free), 13 (Vir), NOT universal. State WHICH algebra: intrinsic vs kappa_eff=kappa(matter)+kappa(ghost) vs kappa(B) where B=A^!.

**pole/weight** (AP19,21,27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.

**grading/signs** (AP22,23,44,45,46,49): Desuspension LOWERS: |s^{-1}v|=|v|-1. eta(q) includes q^{1/24}. OPE mode vs lambda-bracket: T_{(3)}T=c/2 becomes {T_lambda T}=(c/12)*lambda^3 (divided power 1/n!). A-hat(ix)-1 starts at x^2; verify F_1 matches leading order. sqrt(Q_L) is flat section; H(t)=t^2*sqrt(Q_L) NOT horizontal. Cross-volume conventions: Vol I=OPE modes, Vol II=lambda-brackets, Vol III=motivic. NEVER paste without conversion.

**duality** (AP33,29,31): H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-arity components independent. F_1=0 does NOT imply F_g=0.

**computation discipline** (AP3,10,61): Compute independently. NEVER pattern-match across occurrences. Cross-family consistency checks are real verification; single-family hardcoded tests insufficient. Verify against OPE table, landscape_census.tex, cross-engine comparison.

### BEFORE WRITING A SCOPE CLAIM

AP6: Specify genus, arity, level (convolution vs ambient) for D^2=0, kappa, Theta_A.
AP7: Before writing universal quantifier, verify proof has no implicit type/genus/level restriction.
AP8: NEVER "self-dual" unqualified. Specify which duality, which c. Virasoro self-dual at c=13.
AP14: Koszulness != SC formality. Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k>=3. All standard families Koszul; only class G SC-formal.
AP18: "Entire standard landscape" -> list every family, check each against hypotheses.
AP30: CohFT flat identity requires vacuum in V. ALWAYS list conditional axioms at cross-reference.
AP32: Genus-1 != all-genera. obs_1=kappa*lambda_1 unconditional. Multi-weight g>=2: scalar formula FAILS.
AP36: "implies" proved, "iff" claimed -> write "implies" until converse has independent proof.
AP67: Strong gen != FREE strong gen. W(p) has 4 strong generators but FREE strong gen OPEN.

### BEFORE WRITING ABOUT OBJECTS

**four functors** (AP25,34,50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."

**operadic** (AP81,82,83,84,85,88,103,104): B_P(A)=P^!-coalgebra != BP=cooperad (different levels). Three coalgebra structures: Lie^c (Harrison, coLie), Sym^c (coshuffle, 2^n terms), T^c (deconcatenation, n+1 terms). Coshuffle != deconcatenation. Factorization coproduct (Sym^c on Ran) != deconcatenation (T^c on ordered configs); R-matrix descent relates. B_{Com}(A) is coLie, NOT cocommutative. P^i=cooperad != P^!=(P^i)^v=operad. Cotriple bar != operadic bar. E_1 is PRIMITIVE; modular/symmetric is av-image.

**SC/promotion** (AP89,90,87,86,91,92,93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).

**shadow/Hochschild** (AP94,95,96,97,98,100,102): ChirHoch*(Vir_c) total dim <= 4. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C1 unconditional, C2 uniform-weight only. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.

### BEFORE WRITING PROSE

AP105: Heisenberg = abelian KM at level k = abelian CS boundary. SAME OPE J(z)J(w) ~ k/(z-w)^2. Simple-pole requires ODD generator (symplectic fermion).
AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
AP108: Heisenberg = CG opening, NOT the atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
AP111: No "What this chapter proves" blocks. Restructure instead.
AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
**Prose laws**: (1) No AI slop (notably/crucially/remarkably/interestingly/furthermore/moreover/delve/leverage/tapestry/cornerstone). (2) No hedging where math is clear. (3) No em dashes; use colons, semicolons, or separate sentences. (4) No passive voice hedging. (5) Every paragraph forces the next. (6) State once, prove once. (7) Scope always explicit. (8) Comparison with prior work: one sentence per paper.

### AFTER EVERY EDIT

AP2: Read actual .tex proof, not CLAUDE.md description. Descriptions are claims ABOUT source.
AP5: Grep ALL THREE volumes for variant forms: ~/chiral-bar-cobar, ~/chiral-bar-cobar-vol2, ~/calabi-yau-quantum-groups. After EVERY correction.
AP12: When proving a claim, search entire manuscript for variants. Update all instances same commit.
AP17: After writing ANY new theorem, IMMEDIATELY audit before building next result.
AAP1: Grep for `antml` or `</invoke>` in .tex after every write.
AAP7: Grep current file before writing formula that appears elsewhere in same file.

### BEFORE COMMITTING STATUS

AP4: ClaimStatusProvedHere = verify proof proves stated claim. Status tag != ground truth.
AP40: Environment MUST match tag. Conjectured -> \begin{conjecture}. ProvedElsewhere -> theorem + Remark attribution.
AP60: Tag only genuinely new content ProvedHere. Classical parts ProvedElsewhere with attribution.
AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.

## Additional Anti-Patterns (Reference)

### Epistemic
AP11: Single-point external dependency -> flag in concordance with source, status, fallback.
AP13: Forward references must be transparent about genus/level/type restrictions.
AP15: E_2* is quasi-modular. Genus-1 propagator IS E_2*. Graph sums produce quasi-modular {E_2*,E_4,E_6}, NOT {E_4,E_6}.
AP26: Fock inner product != BPZ for weight>=4, rank>=3 W-algebras.
AP28: NEVER use undefined terminological qualifier in 3+ locations.
AP35: False proof, true conclusion -> two cancelling errors. Fix BOTH.
AP37: SS page from FULL differential, not pole order heuristics. Lie homology != Hochschild homology.
AP38: Literature values: record source paper AND convention. DVV != Eichler-Zagier. Derive independently.
AP39: kappa != S_2 for non-Virasoro. Coincide only rank-1.
AP41: Prose mechanism != mathematical mechanism. "Residue extracts simple-pole coefficient" WRONG.
AP42: State level of validity explicitly for sophisticated identifications.
AP43: Central object without \begin{definition} -> property list is conjecture, not definition.

### Computational
AP59: Three invariants: p_max(OPE pole) != k_max(collision depth=p-1) != r_max(shadow depth, independent). betagamma: p=1,k=0,r=4.
AP62: "depends only on dim(g)" = Euler char only. Individual bar cohom dims need full bracket.
AP63: CE(g_-) != chiral bar for multi-gen. Orlik-Solomon form factor differs. sl_3 chiral H^2=36 vs CE H^2=20.
AP64: CE weight vs PBW degree produce different sequences. Always specify grading.
AP66: Free-field GFs NOT D-finite (Lipshitz/Stanley). Interacting algebras ARE.
AP68: PVA slab ghost c != kappa. SVir: kappa=(3c-2)/4. Hierarchy: Sigma_0=13 > Sigma_1=41/4 > Sigma_2=1 > Sigma_4=0.
AP69: tau_shadow = kappa-deformed KdV. Obstruction kappa(kappa-1). Standard KdV only at kappa=1.
AP70: Shadow L^sh has POLES at s=1,2. Negative integers are trivial zeros. F_g <-> L^sh(1-2g) FAILS.
AP71: Shadow kappa != Dyson beta. At c=13, kappa=6.5, not 13.
AP72: W-algebra NOP bar has d^2 != 0. Needs full singular OPE + Orlik-Solomon.
AP73: BV=bar: PROVED G/L, CONDITIONAL C/M (harmonic decoupling).
AP74: False Bernoulli-Dirichlet identity. LHS entire, RHS has poles s=1,2. Verify numerically at s=0.
AP75: Koszulness = PBW degree concentration, NOT conformal weight grading.
AP76: Y_{1,1,1} has c=0, kappa=Psi, NOT c=3.
AP77: Stokes ratio on convergent series spurious. Use direct Pade, not Borel.
AP78: Never conjecture from isolated number-theoretic coincidences.
AP79: W(p) has 4 generators (T + sl_2 triplet), not 2. Count fields, not isotypic components.
AP80: Engine without test file -> verify BOTH exist after every agent completion.

### Operadic-Structural
AP99: K11 Lagrangian CONDITIONAL (perfectness + bar-cobar normal-complex).
AP101: "qi not merely iso on cohomology" is tautological. Use "qi of A-inf-algebras" vs "chain qi."
AP110: Each volume's preface tells its OWN story. Cross-volume in delineated subsections.
AP112: Never trust stale page counts. Verify against fresh builds.
AP113: kappa without subscripts FORBIDDEN in Vol III. Always kappa_ch, kappa_BKM, kappa_cat, kappa_fiber.
AP114: Stub chapters (<50 lines, no theorems) create false coverage -> develop or comment out.
AP115: Architectural CLAUDE.md claims must be enacted in .tex. Metadata-source gap is the most dangerous anti-pattern.

## Regression Safeguards (non-AP)

RS-3: Physics IS the homotopy type, not a "bridge." Costello-Gaiotto-Dimofte are substance, not applications.
RS-4: Costello/Dimofte/Gaiotto content belongs in mathematical core, not "connections" chapters.
RS-9: The slab is a bimodule, NOT a Swiss-cheese disk. Two boundary components.
RS-10: Single-pass agent work without audit FORBIDDEN. Beilinson loop mandatory for chapters.
RS-12: The programme is THREE volumes, not two.
RS-13: In Vol II, gravity is the CLIMAX (Part VI), not middle content.
RS-14: Introduction orients, Overture instantiates. Introduction first, Overture second.
RS-15: Koszul programme before higher_genus in the dependency DAG.
RS-19: The preface is a complete survey, not a compressed summary. Save before compressing.

## Agent Anti-Patterns

AAP2: Terminology rename MUST be atomic across all three volumes in single session.
AAP3: Formula implemented ONCE in canonical module, import everywhere.
AAP4: \begin{proof} only after theorem/prop/lemma with ProvedHere. Use Remark[Evidence] for conjectures.
AAP5: Build-artifact commits batched with content. Never standalone artifact commits.
AAP6: Search ALL THREE volumes before downgrading a status tag.
AAP8: README claims independently verifiable by test suite.
AAP9: Wait for ALL agents to finish before launching new batch.
AAP10: After agent completion, verify BOTH engine AND test files exist.
AAP11: Every hardcoded expected value derivable by 2+ independent paths.
AAP12: Asymptotic tolerance proportional to 1/log(N) or verified by two methods.
AAP13: NEVER downgrade model without user permission. Wait and retry on rate limit.
AAP14: Unique branch name per agent.
AAP15: Serialize builds or use isolated worktrees. Parallel pdflatex kills.
AAP16: git stash FORBIDDEN. Use git diff > patch.diff + git apply instead.
AAP17: Verify edits via git diff, not agent narrative.
AAP18: Confabulating operadic theory -> compute or cite (Loday-Vallette, Vallette, Livernet). NEVER analogize.

## Structural Facts

**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-arity convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower.

**Convolution**: dg Lie Conv_str is strict model of L-inf Conv_inf. MC moduli coincide. Full L-inf needed for transfer/formality/gauge equivalence.

**E_1 primacy**: B^ord is the primitive (Stasheff). av: g^{E_1} -> g^mod lossy Sigma_n-coinvariant projection. av(r(z))=kappa at arity 2. All standard chiral algebras are E_inf (local); E_1=nonlocal (Yangian, EK quantum VA). NEVER "E_inf means no OPE poles."

**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).

## Architecture

**Vol I**: Introduction + Overture (Heisenberg CG opening, unnumbered) + Part I (Bar Complex: Thms A-D+H, 12 Koszul equivs) + Part II (Characteristic Datum: shadow tower, G/L/C/M, higher-genus, E_1 modular) + Part III (Standard Landscape: all families, census) + Part IV (Physics Bridges: E_n, factorization envelopes, derived Langlands) + Part V (Seven Faces of r(z): R-matrix, Yangian, Sklyanin, DK, celestial, holographic) + Part VI (Frontier) + Appendices.

**Vol II** (~1,500pp, ~/chiral-bar-cobar-vol2): SC^{ch,top} bar differential = holomorphic factorization on C, coproduct = topological factorization on R. Seven parts: I(Open Primitive) II(E_1 Core) III(Seven Faces) IV(Char Datum) V(HT Landscape) VI(3D Quantum Gravity = CLIMAX) VII(Frontier). See Vol II CLAUDE.md for V2-AP1-24 (E_1/E_inf hierarchy).

**Vol III** (~200pp, ~/calabi-yau-quantum-groups): CY -> chiral functor Phi. Five parts: I(CY Engine) II(CY Char Datum) III(CY Landscape) IV(Seven Faces r_CY) V(CY Frontier). 12 stub chapters. kappa subscripts MANDATORY. See Vol III CLAUDE.md for AP-CY1-8 (kappa-spectrum).

## Writing Standard

Channel: Gelfand (inevitability), Beilinson (falsification), Drinfeld (unifying principle), Kazhdan (compression), Etingof (clarity), Polyakov (physics=theorem), Nekrasov (seamless passage), Kapranov (higher structure IS math), Ginzburg (every object solves a problem), Costello (factorization), Gaiotto (dualities compute), Witten (physical insight precedes proof). **Convergent loop mandatory**: WRITE -> REIMAGINE (Gelfand/Beilinson/Drinfeld) -> REWRITE from scratch -> BEILINSON AUDIT (adversarial) -> REIMAGINE AGAIN -> REWRITE AGAIN -> CONVERGE (zero findings >= MODERATE). Preface/intro: 3+ iterations. Chapter openings: 2+. **CG structural moves**: deficiency opening, unique survivor, instant computation, forced transition, decomposition table, dichotomy, sentence-as-theorem.

## Skills

```
/build                      Build all three volumes, tests, census
/audit [target]             Deep Beilinson audit (6 hostile examiners)
/chriss-ginzburg-rectify [file]  Full 5-phase CG + Beilinson rectification (canonical)
/rectify-all                Rectification across all chapters, all volumes, parallel tiers
/research-swarm [topic]     Launch 30+ research agents on frontier
/verify [claim]             Multi-path verification (3+ independent paths)
/propagate [pattern]        Cross-volume AP5 propagation check
/compute-engine [name]      Scaffold compute engine with multi-path tests
/beilinson-swarm            Beilinson rectification swarm across all chapters
/rectify [file]             Beilinson rectification loop (lighter than CG)
```

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
cd ~/calabi-yau-quantum-groups && make fast                       # Vol III
make test                                                         # Fast tests
make test-full                                                    # All tests (~119K)
python3 scripts/generate_metadata.py                              # Census
```

CAUTION: Watcher spawns competing pdflatex; always kill before builds.

## Session Protocol

1. Read this file. 2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. 3. Tests: `make test`. 4. `git log --oneline -10`. 5. Read .tex source before any edit (never from memory). 6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5). 7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1). 8. Apply convergent writing loop to all prose. 9. Session end: build all three volumes, run tests, summarize errors by class.

Details: FRONTIER.md (research programme status), MEMORY.md (session history), concordance.tex (constitution).

## LaTeX

All macros in main.tex preamble. NEVER \newcommand in chapters (use \providecommand). Memoir class, EB Garamond (newtxmath + ebgaramond). Tags: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic. Label everything with \label{def:}, \label{thm:}. Cross-reference with \ref. Do not add packages without checking compatibility. Do not create new .tex files when content belongs in existing chapters.

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. No co-authored-by, no generated-by, no AI attribution anywhere. Constitution: concordance.tex. git stash FORBIDDEN (AAP16).
