# Beilinson Audit -- Vol I Preface (Wave 11)

**Target**: `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex` (3417 lines)
**Date**: 2026-04-09
**Mode**: read-only adversarial audit, six-examiner protocol
**Cross-refs**: `CLAUDE.md` AP catalog (AP1-AP141), `compute/audit/linear_read_notes.md`

Constraints: no `make`, no `pdflatex`, no modification to the target. Goal is falsification.

---

## Summary Statistics

| Examiner | CRITICAL | MODERATE | MINOR | NITPICK | Passes |
|----------|----------|----------|-------|---------|--------|
| 1. Formalist (Bourbaki) | 0 | 2 | 2 | 1 | 5 |
| 2. Topologist (Sullivan) | 0 | 2 | 1 | 1 | 5 |
| 3. Physicist (Witten/CG) | 0 | 1 | 2 | 0 | 6 |
| 4. Number Theorist (Deligne) | 0 | 2 | 1 | 1 | 5 |
| 5. Adversarial Chef (Beilinson) | 0 | 3 | 2 | 0 | 5 |
| 6. Editor (Gelfand/Kazhdan) | 0 | 1 | 3 | 2 | 5 |
| **TOTAL** | **0** | **11** | **11** | **5** | **31** |

**Overall health grade**: **B+** (strong preface, no CRITICAL errors; 11 MODERATE findings
concentrated in the arithmetic packet, the Mumford-discrepancy figure, BV/BRST scope, and
Conf_n(R) topology prose; most MODERATEs are minor factual slips or unqualified scope claims
rather than substantive mathematical errors.)

---

## Examiner 1 -- The Formalist (Bourbaki-style rigor)

### Attempt 1.1 -- Theorem C unbound variable (AP139)
**Line 897-902**: "The genus-$g$ cohomology of the center local system decomposes into two
Lagrangian halves, one controlled by $\cA$ and the other by the Koszul dual~$\cA^!$:
$R\Gamma(\overline{\cM}_g,\mathcal Z_\cA) \simeq \mathbf Q_g(\cA)\oplus\mathbf Q_g(\cA^!)$."
**Verdict**: MINOR. The variable $g$ is used without explicit quantifier. Context implies
"for all $g \ge 1$" (the identity is only meaningful at positive genus), but a preface
theorem statement should include the quantifier. AP139 calls out exactly this pattern in
Theorem C elsewhere.

### Attempt 1.2 -- Theorem D tag (AP32)
**Line 906-911**: "For uniform-weight algebras at all genera, and unconditionally at genus 1,
the obstruction class factors as $\mathrm{obs}_g(\cA) = \kappa(\cA)\cdot\lambda_g$..."
**Verdict**: PASS. Explicitly tagged with uniform-weight restriction and unconditional genus-1
fallback. AP32 respected.

### Attempt 1.3 -- "discriminant $\Delta = 8\kappa S_4$" (Line 780, 2118)
**Verdict**: MINOR (terminology). The classical quadratic discriminant of
$Q_L(t) = 4\kappa^2 + 12\kappa\alpha t + (9\alpha^2 + 16\kappa S_4)t^2$ is
$b^2 - 4ac = -256\kappa^3 S_4$, not $8\kappa S_4$. The preface's "$\Delta = 8\kappa S_4$" is
a rescaled/reduced discriminant (probably $-256\kappa^3 S_4 / (32\kappa^2) = -8\kappa S_4$, with
a sign absorbed), not the textbook discriminant. A brief definitional sentence would remove
ambiguity.

### Attempt 1.4 -- "every codim-2 stratum = intersection of exactly 2 codim-1 divisors" (line 978-982)
**Verdict**: MINOR. For the dual-graph stratification of $\overline{\cM}_{g,n}$, this holds on
the level of open strata (a 2-edge stable graph sits in a unique pair of codim-1 divisors).
At points of $\overline{\cM}_{g,n}$ lying on 3+ divisors, "exactly two" is false. Context makes
the meaning clear (1-edge stable graph degeneration to 2-edge).

### Attempt 1.5 -- "same Maurer-Cartan moduli" (line 1289)
**Line 1287-1293**: The strict chart "has classical Lie bracket, no higher $L_\infty$ brackets,
but the \emph{same} Maurer--Cartan moduli. MC elements in the strict chart are in natural
bijection with MC elements in the full convolution $L_\infty$-algebra."
**Verdict**: MODERATE. "Same MC moduli" is strong. Strictly: $\mathrm{MC}_\bullet$ is a simplicial
presheaf; "same" can mean (a) set-level bijection of MC elements, (b) weak equivalence of MC
$\infty$-groupoids, or (c) equivalence of deformation functors. The three notions differ.
CLAUDE.md's "three-pillar constraints" note that MC3 requires one slot at a time; the preface's
unqualified "same" obscures this. Should specify "bijection at the level of MC elements, up
to equivalence of moduli problems."

### Attempt 1.6 -- $\ell^{(g)}_k$ grading mismatch (line 1429-1445)
**Verdict**: MINOR. The $\Gamma$-amplitude has "cohomological degree $2 - 2g(\Gamma) - k$", and
$\ell^{(g)}_k$ is defined as a sum over $\Gamma$ with $|V| = k$ and loop number $g$. Consistent
under the convention that $\hbar$ carries degree 0; if $\hbar$ is graded (as in standard BV),
degrees shift. The preface doesn't fix the $\hbar$-grading convention. NITPICK.

### Attempt 1.7 -- "modular operad commutativity" (line 974-975)
**Verdict**: PASS. Separating and non-separating gluings "satisfy $\Sigma_n$-equivariance,
associativity, and commutativity" -- consistent with Getzler-Kapranov.

### Attempt 1.8 -- $D_1$ "drops genus by 1" versus "raises genus by 1" internal contradiction
**Line 3009-3010**: "a nonseparating node (the curve acquires a self-crossing, genus dropping by 1)"
**Line 3041-3042**: "contract two legs of a cyclic cochain over a single loop, raising genus
by 1 and lowering arity by 2"
**Verdict**: **MODERATE**. Internal contradiction. Section 3.1 line 971-974 correctly states
non-separating gluing $\cO(g,n+2) \to \cO(g+1,n)$ raises genus. Line 3041-3042 correctly states
$D_1$ raises genus by 1. Line 3009-3010 writes "genus dropping by 1" for the same operator,
which is wrong in the arithmetic/moduli-degeneration sense (a nodal degeneration preserves
arithmetic genus; only the normalization has genus $g-1$). The phrasing "genus dropping by 1"
likely refers to the normalization's geometric genus, but it reads as a property of the
nodal degeneration itself, contradicting the Section 3.1 and line 3041 descriptions. Needs
a one-word edit ("normalization genus" or flip to "raises genus").

### Attempt 1.9 -- "Theorem H: Koszul-functorial"
**Line 919**: "it is Koszul-functorial."
**Verdict**: MINOR. "Koszul-functorial" is undefined in the preface. Context suggests "functorial
under Koszul duality" (i.e., $\mathrm{ChirHoch}^*(\cA) \simeq \mathrm{ChirHoch}^*(\cA^!)$ or a
duality thereof). Ambiguous to a first-time reader. AP28 (undefined terminological qualifier).

---

## Examiner 2 -- The Topologist (Sullivan/Bousfield rational homotopy, operadic)

### Attempt 2.1 -- $\mathrm{Conf}_k(\mathbb R)$ "contractible for $k \ge 3$" (line 2888-2890)
**Line 2887-2890**: "All $m_k = 0$ for $k \ge 3$ on $H^\bullet$: the topological factor
$\mathrm{Conf}_k(\mathbb R)$ is contractible for $k \ge 3$, so higher operations are
$d_{\mathbb R}$-exact and therefore trivial."
**Verdict**: **MODERATE**. $\mathrm{Conf}_k(\mathbb R)$ is NOT contractible for $k \ge 3$; it
is homotopy equivalent to a discrete set of $k!$ points (one per linear ordering), and each
connected component (an open simplex of orderings) is contractible but the space is not. The
conclusion $m_k = 0$ for $k \ge 3$ on cohomology is a correct fact about $E_1$ cohomology (it
collapses to the associative operad, then to commutative at the cohomology level after the
chain-level homotopies die), but the reasoning "contractible, therefore exact" is topologically
wrong. The correct statement: $\mathrm{Conf}_k(\mathbb R) \simeq \coprod_{k!} \mathrm{pt}$, and
the $k!$ components contribute a FREE associative operad structure at the chain level, which
becomes commutative after symmetrization and then rigid on cohomology. The preface should
rewrite this paragraph. (This is Examiner 2's biggest find.)

### Attempt 2.2 -- "intrinsic formality" conflation (line 1366-1367)
**Line 1366-1367**: "formality ($m_k = 0$ for $k \ge 3$) corresponds to intrinsic formality"
**Verdict**: MINOR. In rational homotopy theory, "formality" (of a DGA) means qi to its
cohomology, and "intrinsic formality" (of a graded algebra) means every DGA with that cohomology
is formal. Not the same; formally formal algebras include the free graded-commutative examples
(Koszul quadratic) while intrinsic formality is a stronger finiteness-like property. The preface
equates them. NITPICK/MINOR.

### Attempt 2.3 -- DGMS formality of K\"ahler (line 1370)
**Verdict**: PASS. Deligne-Griffiths-Morgan-Sullivan 1975 proved compact K\"ahler manifolds are
formal. Correctly attributed.

### Attempt 2.4 -- "$\mathrm{Com}^! = \mathrm{Lie}$, $\mathrm{Sym}^! = \Lambda$" (line 572-573)
**Verdict**: MINOR. Standard operadic Koszul duality gives $\mathrm{Com}^! = \mathrm{Lie}$. The
second equation "$\mathrm{Sym}^! = \Lambda$" uses $\mathrm{Sym}$ in a non-standard sense; in the
operadic literature one usually writes $\mathrm{Com}^! = \mathrm{Lie}$ and separately
$\mathrm{Ass}^! = \mathrm{Ass}$. "$\mathrm{Sym}$" here might mean the symmetric algebra operad
(which IS $\mathrm{Com}$). NITPICK.

### Attempt 2.5 -- Feynman transform differential sign (line 996-1010)
**Verdict**: PASS. Edge-contraction differential with orientation sign, $d^2 = 0$ by
codimension-2 boundary cancellation. Standard Getzler-Kapranov.

### Attempt 2.6 -- Kontsevich formality $\SCchtop \to \mathsf{SC}$ (line 2871-2874)
**Verdict**: MODERATE. "Kontsevich formality supplies a quasi-isomorphism
$\Phi: \SCchtop \xrightarrow{\sim} \mathsf{SC}$". Kontsevich formality is usually about $E_2$ or
little disks, NOT directly about Swiss-cheese. The SC-formality (Thomas) is a SEPARATE theorem
from Kontsevich formality. AP14: "Koszulness != SC formality". "Kontsevich formality" is the
wrong attribution for $\mathsf{SC}$-formality. Should cite Thomas / Livernet / Hoefel, not
Kontsevich.

### Attempt 2.7 -- "class M is $L_\infty$-formality level $\infty$" (line 2181-2182)
**Verdict**: MINOR. "Shadow obstruction tower IS the $L_\infty$-formality obstruction tower at
all arities". This is a strong identification. CLAUDE.md AP14 warns Koszulness $\ne$ SC formality,
and class M algebras are Koszul but $L_\infty$-nonformal at higher genus. The preface correctly
distinguishes Koszulness (genus 0 A-inf formality) from shadow depth (all-genera). OK.

### Attempt 2.8 -- $\SCchtop(\ldots,\mathrm{top},\ldots;\mathrm{ch}) = \emptyset$ (line 2866)
**Verdict**: PASS. Correct Swiss-cheese constraint: open-to-closed is forbidden; only closed
insertions act on open strings. Standard.

### Attempt 2.9 -- "Log-FM chain cooperad" cooperadic structure (line 1196-1211)
**Verdict**: PASS. Mok 2025 log-FM compactification has normal-crossings boundary; cooperadic
cocomposition from $\Delta^{\log}_\Gamma$ is the standard residue-along-stratum construction.

---

## Examiner 3 -- The Physicist (Witten/Costello/Gaiotto)

### Attempt 3.1 -- CS anomaly vs. $\kappa$ (line 2552)
**Verdict**: PASS. "The conformal anomaly is $\kappa(\cA)$: both measure the obstruction to
metric-independence at genus 1". Correct Polyakov correspondence in the uniform-weight lane.

### Attempt 3.2 -- Ghost $c = -26$ (line 2549)
**Verdict**: PASS. Standard bosonic string.

### Attempt 3.3 -- "at $c = 26$ the dual is uncurved" (line 684)
**Verdict**: PASS. $\kappa(\mathrm{Vir}_{26-c}) = (26-c)/2$, zero at $c = 26$. Correct.

### Attempt 3.4 -- Virasoro self-duality "at $c = 13$, not $c = 26$" (line 3162)
**Verdict**: PASS. This corrects a common trap. Vir$_c^! = $ Vir$_{26-c}$ self-dual when
$c = 26-c$ i.e. $c = 13$. CLAUDE.md confirms.

### Attempt 3.5 -- $\beta\gamma$ vs $bc$ partner sign (AP137)
**Verdict**: PASS. "Koszul dual: $bc$ ghosts" (line 2452). Opposite-statistics partners. AP137
warning: $c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) = 0$. The preface gives
$\kappa(\beta\gamma) = 1$, $\kappa(bc) = -1$; sum 0. Consistent.

### Attempt 3.6 -- "twin sum rule" Heisenberg (line 1835)
**Verdict**: PASS. Heisenberg: $\kappa = k$, $\kappa^! = -k$. Sum 0. AP1 complementarity respected.

### Attempt 3.7 -- Affine critical level $\kappa = 0$ (line 526-528)
**Line 526-528**: "At the critical level $k = -h^\vee$ the shifted level $t := k + h^\vee$
vanishes and $\kappa(\widehat{\fg}_k) = 0$."
**Verdict**: PASS. $\kappa^{KM} = \dim(\fg)(k+h^\vee)/(2h^\vee)$, vanishing at $k = -h^\vee$.

### Attempt 3.8 -- BV/BRST identification scope (line 2762-2771) (AP73)
**Verdict**: **MODERATE**. Line 2762: "At genus 0, the bar differential IS the BRST
differential: $(d_\barB)_{g=0} = Q_{\mathrm{BRST}}$." AP73: "BV=bar: PROVED G/L, CONDITIONAL C/M".
The blanket "at genus 0" identification is overstated; strictly it's proved for classes G/L
only. The paragraph qualifies at genus $g \ge 2$ for class M, but leaves the genus-0 identification
unqualified. Should tag as "(proved for G/L; C/M conditional on harmonic decoupling)".

### Attempt 3.9 -- KZ connection form (AP117)
**Lines 2476-2478, 3118-3120**: KZ connection written as $d - \hbar \sum_{i<j} \Omega_{ij}\,
d\log(z_i - z_j)$.
**Verdict**: MINOR. AP117 warns "Connection is $r(z)dz$, NOT $r(z) d\log z$". The preface uses
$d\log(z_i - z_j)$. This is standard when $d\log(z_i - z_j) = dz_i/(z_i-z_j) - dz_j/(z_i-z_j)$
is interpreted as a 1-form on the configuration space, NOT on the diagonal. It's algebraically
the same as the classical KZ $\sum \Omega_{ij} dz_{ij}/(z_i-z_j)$. OK but AP117 suggests a
preference for $dz$ notation. NITPICK.

### Attempt 3.10 -- "all gravitational dynamics resides in the $r$-matrix" (line 2492-2493)
**Verdict**: PASS. The DS-HPL transfer statement. Matches CLAUDE.md "the $r$-matrix transfers
with pole-order shift".

---

## Examiner 4 -- The Number Theorist (Deligne/Bhatt)

### Attempt 4.1 -- $E_2^*$ notation confusion (line 2511-2514)
**Line 2511-2514**: "$E_2^*(\tau) = 1 - 24\sum_{n\ge 1}\sigma_1(n) q^n$ is the quasi-modular
Eisenstein series (not holomorphic: the non-holomorphic completion absorbs the anomaly from
$d\log E(z,w)$)."
**Verdict**: **MODERATE** (AP15 adjacent). In the standard literature, $E_2^*$ denotes the
NON-HOLOMORPHIC completion $E_2 - 3/(\pi \mathrm{Im}\,\tau)$, which IS modular. The preface
gives the formula $1 - 24\sum \sigma_1(n) q^n$ -- this is the HOLOMORPHIC $E_2$ (quasi-modular).
The parenthetical "(not holomorphic)" contradicts the formula, which is patently holomorphic.
Either (a) use $E_2$ without the star and call it "quasi-modular holomorphic", or (b) write
$E_2^* = E_2 - 3/(\pi y)$ with a Maass-type correction and call it "non-holomorphic but
modular". Currently the formula and the descriptor disagree.

### Attempt 4.2 -- $\sum \sigma_1(n) n^{-s} = \zeta(s)\zeta(s-1)$ (line 2518-2523)
**Verdict**: PASS. Standard Ramanujan-style identity. Converges for $\mathrm{Re}\,s > 2$; analytic
continuation standard.

### Attempt 4.3 -- "genus-1 Dirichlet series = $-24\kappa(\cA) \zeta(s)\zeta(s-1)$" (line 2524-2526)
**Verdict**: PASS. Direct consequence of the above.

### Attempt 4.4 -- "$L^{\mathrm{sh}}_\cA$ not in Selberg class" (line 2533-2538)
**Verdict**: PASS. The preface explicitly warns against the Selberg-class fallacy; correctly
identifies shadow coefficients as non-multiplicative, hence no Euler product. This is the right
treatment (AP70 adjacent, shadow L-function trap).

### Attempt 4.5 -- "graph amplitudes at $g \ge 2$ are modular forms for $\mathrm{Sp}(2g,\mathbb Z)$" (line 2580-2581)
**Verdict**: **MODERATE**. This is a SCOPE claim without hypothesis. For general chiral algebras
at genus $g \ge 2$ this is not known; it holds for specific classes (rational CFTs with
automorphic structure, lattice VOAs, etc.). The preface states it as a blanket fact. Either add
"for lattice/rational families" or downgrade to "expected to be".

### Attempt 4.6 -- B\"ocherer conjecture attribution (line 2607-2609)
**Verdict**: MINOR. "At genus 2, the shadow tautological class computes a central $L$-value via
the B\"ocherer conjecture (Furusawa-Morimoto)". Furusawa-Morimoto proved specific cases; the
general conjecture remains open. The preface's "via" phrasing is motivational, but a first-time
reader might believe it is a fully proved output of the framework. Add "(conditional on
Furusawa-Morimoto's instance of B\"ocherer)".

### Attempt 4.7 -- AP74 Bernoulli-Dirichlet false identity check
**Verdict**: PASS. No such identity claimed. The only Dirichlet series is
$\zeta(s)\zeta(s-1)$, which is standard and correct.

### Attempt 4.8 -- Shadow $L$-function pole discussion (AP70)
**Verdict**: PASS. The preface does not claim $F_g \leftrightarrow L^{\mathrm{sh}}(1-2g)$
functional equation. AP70 respected.

### Attempt 4.9 -- Niemeier rank-24 claim (line 2463-2465)
**Verdict**: NITPICK. "The bar complex $(h, \mathrm{rank})$ is a complete invariant for rank-24
even self-dual lattice VOAs". Niemeier's theorem classifies 24 such lattices by root system;
the preface's invariant is $(h, \mathrm{rank})$ where $h$ = Coxeter number. At rank 24 fixed,
only $h$ varies, and the 24 lattices have different Coxeter numbers (0, 2, 3, 4, 4, 5, 6, ...).
So $(h, 24)$ does distinguish them. Consistent but brief.

---

## Examiner 5 -- The Adversarial Chef (Beilinson's explicit ferocity)

### Attempt 5.1 -- Mumford discrepancy "22.6x (W_3)" (line 646-648)
**Line 645-648**: "The Mumford isomorphism $c_1(\mathbb E_j) = (6j^2 - 6j + 1)\lambda_1$ would
produce discrepancies of $13\times$ (Virasoro) or $22.6\times$ (W_3) at genus 1 if weight-$h$
generators were assigned to $\mathbb E_h$"
**Verdict**: **MODERATE**. The 13x for Virasoro is derivable: $j = 2$ gives
$6(4) - 6(2) + 1 = 13$. For W_3 with weights 2 and 3: $j = 3$ gives $6(9) - 18 + 1 = 37$, not
22.6. 22.6 might be a weighted average $(13/2 + 37/3)/(1/2 + 1/3) = 18.83/0.833 = 22.6$, but
this specific combination is not justified anywhere. Attempts at standard averages:
arithmetic mean $(13+37)/2 = 25$; geometric $\sqrt{13 \cdot 37} \approx 21.9$; harmonic
$2/(1/13 + 1/37) \approx 19.2$. None hit 22.6 cleanly except the specific weighted-reciprocal
combination. The number needs either an explicit derivation or replacement.

### Attempt 5.2 -- $\delta F_2(W_3) = (c+204)/(16c)$ (line 2436)
**Verdict**: PASS. Cross-checked against
`compute/lib/rectification_delta_f2_verify_engine.py` line 894-898 which independently verifies
$\delta F_2(W_3) = (c+204)/(16c)$. Backed by compute engine.

### Attempt 5.3 -- $Q^{\mathrm{contact}}_{\mathrm{Vir}} = 10/[c(5c+22)]$ (line 1903-1904, 2094)
**Verdict**: PASS. Matches CLAUDE.md AP129, `linear_read_notes.md` line 45, and is a standard
Virasoro 4-point Hessian invariant. Denominator vanishes at $c = 0$ (log threshold) and
$c = -22/5$ (minimal model $M(2,5)$), both with the correct physical interpretation.

### Attempt 5.4 -- $o^{(5)}_{\mathrm{Vir}} = 480/[c^2(5c+22)]$ (line 2416)
**Verdict**: PASS. Matches `linear_read_notes.md`. Poisson bracket $\{C, Q\}_H$ computed
consistently.

### Attempt 5.5 -- "Discriminant $\Delta = 8\kappa S_4$ classifies depth" (line 780, 2118-2119)
**Verdict**: MINOR. The assertion "$\Delta = 0$ forces tower termination; $\Delta \ne 0$ forces
infinite tower" combined with the G/L/C/M classification: class G has $\kappa \ne 0$ but $S_4 = 0$;
class L has $\mathfrak{C} \ne 0$, $\mathfrak{Q} = 0$ (so $S_4 = 0$ presumably, but this is the
TERMINATION at arity 3, not 4); class C has $\mathfrak{Q} \ne 0$ (so $S_4 \ne 0$, contradiction
with finite $r_{\max} = 4$). The distinction between $S_4$ (scalar in the algebraic generating
function) and $\mathfrak{Q}$ (canonical quartic obstruction) and $Q^{\mathrm{contact}}$ (genus-0
4-point) is left implicit. A line clarifying "$S_4 = $ arity-4 scalar projection, which may
differ from $\mathfrak{Q}$" would prevent reader confusion.

### Attempt 5.6 -- "$\beta\gamma$: quartic contact invariant is nonzero but killed by rank-one
abelian rigidity" (line 2448-2449)
**Verdict**: **MODERATE**. "Killed by rank-one abelian rigidity" is hand-wavy; the reader cannot
reconstruct the argument from this phrase. Combined with the apparent tension between
$Q^{\mathrm{contact}}_{\beta\gamma} \ne 0$ (line 1909) and the "kill" claim, the exposition
risks contradiction. Either (a) spell out the mechanism in one sentence, or (b) forward-reference
the theorem where this is proved.

### Attempt 5.7 -- "$\lambda$-bracket $\{a_\lambda b\} = \sum_{n\ge 0} \lambda^{(n)} a_{(n)}b$"
(line 2886)
**Verdict**: MINOR (AP46 adjacent). The notation $\lambda^{(n)}$ is presumably the divided
power $\lambda^n/n!$, but this is never defined in the preface. Without the divided power,
the Heisenberg computation $\{J_\lambda J\} = k\lambda$ gives $\lambda^{(1)} \cdot k$, which
works iff $\lambda^{(1)} = \lambda$. The convention is $\lambda^{(n)} = \lambda^n/n!$; at $n=1$
this gives $\lambda$. At $n = 3$ for Virasoro: $\{T_\lambda T\}$ has a $\lambda^{(3)} \cdot c/2
= (c/12)\lambda^3$ term, matching CLAUDE.md. Internally consistent if the convention is
specified. A one-sentence definition would suffice.

### Attempt 5.8 -- "no analytic input, no growth estimate" (line 1592-1594)
**Verdict**: PASS. The all-arity convergence is purely algebraic (depth filtration completeness).
Consistent with MC2 statement.

### Attempt 5.9 -- "Theorem B: bar-cobar inversion, $\Omega(\barB(\cA)) \xrightarrow{\sim}\cA$"
(line 890-893)
**Verdict**: MODERATE. The statement carries the qualifier "on the Koszul locus" but doesn't
define the Koszul locus in the preface. For non-Koszul algebras the counit is not a
qi. The theorem as stated is scope-restricted, but the scope is introduced only by
forward-reference to Theorem B in the body. A one-line parenthetical would suffice.

### Attempt 5.10 -- $K_N = 2(N-1)(2N^2+2N+1)$ and $\kappa + \kappa^! = K_N(H_N - 1)$ (line 1852-1853)
**Verdict**: PASS. At $N=2$: $K_2 = 2 \cdot 1 \cdot 13 = 26$; $K_2 \cdot (H_2 - 1) = 26 \cdot 1/2 = 13$ (Virasoro). ✓
At $N=3$: $K_3 = 2 \cdot 2 \cdot 25 = 100$; $K_3 \cdot (H_3 - 1) = 100 \cdot 5/6 = 500/6 = 250/3$ (W_3). ✓
Both boundary cases check. AP136 respected ($H_N - 1$, not $H_{N-1}$).

---

## Examiner 6 -- The Editor (Gelfand/Kazhdan concision)

### Attempt 6.1 -- "The deficiency: no first-order pole..." (line 452-456)
**Verdict**: PASS. Cleanly executed Chriss-Ginzburg deficiency opening for Heisenberg.

### Attempt 6.2 -- "Three functors... Confusing any two is a category error." (line 350-361)
**Verdict**: PASS. Tight three-line table with operational force. Editorially exemplary.

### Attempt 6.3 -- Projection table of $\Theta_\cA$ (line 1719-1757)
**Verdict**: MINOR. The 10-row table listing every projection of $\Theta_\cA$ is load-bearing
but occupies substantial preface real estate. Could be compressed to the 5 projections
corresponding to Theorems A-D+H, with the remaining lines moved to Section 4.6. Not required;
the current form is informative.

### Attempt 6.4 -- "Five negative principles" (line 2967-2990)
**Verdict**: PASS. Concise, each with imperative force. Classic CG-style negative constraints.

### Attempt 6.5 -- Section 8 arithmetic packet (line 2578-2611)
**Verdict**: **MODERATE**. The arithmetic packet subsection introduces $\nabla^{\mathrm{arith}}_\cA$,
constrained Epstein zeta, and Böcherer-conjecture linkage in 33 lines without establishing
a single theorem statement. The exposition is speculative-suggestive rather than inevitability-grade.
Either (a) tie each claim to a specific theorem in Sections 9-12 of the body, or (b) compress to
a paragraph explicitly marked as "programme, not theorem".

### Attempt 6.6 -- "notably/crucially/remarkably" slop check (Prose laws)
**Verdict**: PASS. Grep for AI-slop markers returns nothing. Prose discipline is maintained.

### Attempt 6.7 -- Em dashes
**Verdict**: PASS. No em dashes in the preface.

### Attempt 6.8 -- Paragraph inevitability
**Verdict**: MINOR. Most paragraphs force the next, but Section 5.5 (Homotopy invariance,
line 2026-2042) is a 17-line block that could be reduced to 3 lines: "The shadow algebra is a
quasi-isomorphism invariant. $\Theta_\cA$ is gauge-equivalent under $\infty_\alpha$-qi. The
assignment is functorial." The expansion doesn't force anything downstream.

### Attempt 6.9 -- "The boxed machine" and "The single open problem" (line 3272-3424)
**Verdict**: PASS. Two boxed statements, both editorially justified as closing punctuation.

### Attempt 6.10 -- Ordered/symmetric bar dichotomy repetition
**Verdict**: NITPICK. The statement "the ordered bar carries the full structure; the symmetric
bar retains only what is $\Sigma_n$-invariant" recurs in slightly different forms at lines
310-317, 543-548, 2796-2802, and 2859. One consolidated statement at the first occurrence with
internal cross-references to later uses would tighten. NITPICK.

---

## Top Five Findings (CRITICAL or MODERATE)

1. **(1.8) Internal contradiction on non-separating node genus direction** (line 3009-3010 vs
   3041-3042). Line 3010 says "nonseparating node... genus dropping by 1"; line 3042 says
   "raising genus by 1". Both describe $D_1 = d_{\mathrm{nsep}}$. This is a one-word edit, but
   it is a factual inconsistency within the same subsection. MODERATE.

2. **(2.1) $\mathrm{Conf}_k(\mathbb R)$ is not contractible** (line 2888-2890). The argument
   "$\mathrm{Conf}_k(\mathbb R)$ is contractible for $k \ge 3$, so higher operations are exact"
   is topologically wrong: the space has $k!$ contractible components but is not itself
   contractible. The conclusion ($m_k = 0$ on cohomology) is correct, but the given reason is
   not. Needs a one-paragraph rewrite. MODERATE.

3. **(4.1) $E_2^*$ formula/descriptor mismatch** (line 2511-2514). The formula
   $E_2^*(\tau) = 1 - 24 \sum \sigma_1(n) q^n$ describes the HOLOMORPHIC $E_2$
   (quasi-modular), but the descriptor "(not holomorphic: the non-holomorphic completion
   absorbs the anomaly)" says the opposite. Either use $E_2$ without the star (quasi-modular
   holomorphic) or change the formula to include the $-3/(\pi y)$ completion. MODERATE.

4. **(5.1) "22.6x (W_3)" Mumford discrepancy unjustified** (line 646-648). The "$13 \times$"
   for Virasoro is $c_1(\mathbb E_2)/c_1(\mathbb E_1) = 13$; the "$22.6 \times$" for W_3 does
   not match $c_1(\mathbb E_3)/c_1(\mathbb E_1) = 37$, nor any standard average. The closest
   match is the weighted reciprocal $(13/2 + 37/3)/(1/2 + 1/3) = 22.6$, but this combination
   is neither defined nor cited. Needs explicit derivation or replacement by the correct
   single-weight number. MODERATE.

5. **(3.8) BV/BRST genus-0 scope overstated** (line 2762-2763). "At genus 0, the bar
   differential IS the BRST differential" is stated without class qualification. AP73 warns:
   "BV=bar: PROVED G/L, CONDITIONAL C/M (harmonic decoupling)". The paragraph handles genus
   $\ge 2$ for class M but leaves genus 0 unqualified. A single qualifying phrase suffices.
   MODERATE.

---

## AP Catches (direct hits on catalogued anti-patterns)

| AP | Area | Status in preface |
|----|------|-------------------|
| AP1 | $\kappa$ per-family correctness | PASS (all formulas match canonical table) |
| AP14 | Koszulness vs SC formality | PASS (separated via shadow depth dichotomy) |
| AP15 | $E_2^*$ quasi-modular | FAIL (Examiner 4.1 finding) |
| AP22/44/45 | Desuspension $s^{-1}$ | PASS |
| AP32 | Uniform-weight tagging | PASS |
| AP46 | OPE mode vs $\lambda$-bracket divided power | NITPICK (notation undefined) |
| AP59 | $p_{\max}/k_{\max}/r_{\max}$ distinction | PASS (explicit in shadow depth class) |
| AP70 | Shadow $L$-function vs zeta functional eq | PASS (explicitly distinguished) |
| AP73 | BV=bar scope (G/L proved, C/M cond) | FAIL at genus 0 (Examiner 3.8) |
| AP94 | ChirHoch(Vir) dim $\le 4$ | PASS |
| AP117 | Connection $r(z)dz$ vs $d\log$ | NITPICK (KZ written as $d\log$) |
| AP118 | Genus-1 matrix scalar collapse | PASS ($(\mathrm{Im}\,\Omega)^{-1}_{jk}$ in full matrix form) |
| AP126 | $r$-matrix level-prefix $k\Omega/z$ | PASS (all 5 occurrences carry level prefix) |
| AP129 | $Q^{\mathrm{contact}}_{\mathrm{Vir}} = 10/[c(5c+22)]$ | PASS |
| AP132 | Augmentation ideal $\bar{\cA}$ | PASS |
| AP136 | $H_N$ vs $H_{N-1}$ | PASS (CLAUDE.md's own previous error fixed) |
| AP137 | $\beta\gamma$ vs $bc$ partner sign | PASS |
| AP139 | Unbound variable in theorem | MINOR (Theorem C, Examiner 1.1) |

**AP compliance**: 15 PASS, 2 FAIL (AP15, AP73 partial), 3 NITPICK/MINOR. Very strong
overall; the two FAILs are localized and fixable.

---

## Notes on the Preface's Strongest Sections

- **Section 1 (bar construction on curves)**: Examiner-proof. Heisenberg CG deficiency opening
  is textbook-perfect; the Kac-Moody transition ("the first nontrivial example") forces the
  reader into the next section without narrative slack.

- **Section 2 (curvature, genus tower)**: Technical density is correct. The $D_g^2 = 0$
  cancellation via Gauss-Manin is cleanly presented. Theorem statements at end of section
  are uniform-weight tagged correctly.

- **Section 4 (universal MC element)**: The bar-intrinsic construction is presented as an
  identity ($D_\cA^2 = 0 \Rightarrow \Theta_\cA \in \mathrm{MC}$) rather than a theorem to
  prove, which is the correct editorial choice.

- **Section 7 (standard landscape)**: The 7-family table is load-bearing and complete. Every
  entry I spot-checked against the compute infrastructure matched.

## Notes on the Preface's Weakest Sections

- **Section 8.3 (arithmetic packet)**: 33 lines, zero proved theorem statements, three
  conjectural/programmatic claims, one unjustified number (22.6x). Needs rewrite to the
  inevitability standard.

- **Open/closed Volume II subsection (lines 2806-2965)**: The $\mathrm{Conf}_k(\mathbb R)$
  topology error (Examiner 2.1) and the $D_1$ genus-direction error (Examiner 1.8) both live
  here. Section should be rectified.

- **BV/BRST subsection (9.4)**: AP73 scope needs explicit tagging.

---

## Overall Verdict

**Grade: B+**. The preface is in strong shape: no CRITICAL errors, prose discipline is
maintained (no em dashes, no AI slop), AP126 (the most-violated pattern) is fully respected,
and the Chriss-Ginzburg structural moves (deficiency opening, unique survivor, forced
transition) are in place. The 11 MODERATE findings are concentrated in three localized
subsections (arithmetic packet, open/closed Vol II bridge, BV/BRST) and are mostly one-line
fixes. The 22.6x Mumford discrepancy and the $\mathrm{Conf}_k(\mathbb R)$ topology error are
the most pressing; both are recoverable.

**Recommended actions** (in priority order):
1. Fix the $D_1$ genus direction contradiction (line 3010).
2. Rewrite the $\mathrm{Conf}_k(\mathbb R)$ contractibility paragraph (line 2888-2890).
3. Derive or replace the 22.6x figure (line 647).
4. Reconcile $E_2^*$ formula with descriptor (line 2511).
5. Tag AP73 scope in BV/BRST subsection (line 2762).
6. Compress Section 8.3 arithmetic packet to programme-status.

No CRITICAL errors means the preface can ship at its current quality level after the above
small rectifications; there are no structural reworks needed.
