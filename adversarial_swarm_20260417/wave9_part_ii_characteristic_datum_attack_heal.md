# Wave 9 - Part II Characteristic Datum: Attack + Heal

**Target.** `chapters/frame/part_ii_platonic_introduction.tex` (879 lines), the Part II
Platonic introduction that announces the five-slot fingerprint
$\varphi(\cA) = (p_{\max}, r_{\max}, \chi_{\VOA}, n_{\mathrm{strong}},
\mathrm{coset})$ as the characteristic datum of the Modular Koszul programme,
with $G/L/C/M$ as its lossy coarse projection.

**Protocol.** Beilinson adversarial audit + surgical heal. No commit.
Cross-referenced against `chapters/examples/landscape_census.tex` and
`chapters/theory/infinite_fingerprint_classification.tex`.

---

## Attack findings

### F1. BLOCKING: $V^\natural$ miscategorised (class + slot data)

**Lines 509-512, 544-549 of the target file.**  The fingerprint of the Monster
VOA is stated as
$\varphi(V^\natural) = (2,\, 2,\, \chi_{\VOA}(V^\natural),\, 196884,\, \mathrm{coset})$
with the proof text "$r_{\max}(V^\natural) = 2$ follows because $V^\natural$
is lattice-orbifold-type, with shadow tower stabilizing at $r = 2$" and
"$n_{\mathrm{strong}}(V^\natural) = 196884$ is the dimension of the weight-$1$
non-trivial irreducible Monster representation."

Four errors stacked on one claim:

(i) **$r_{\max}(V^\natural) \ne 2$.**  Landscape census
(`chapters/examples/landscape_census.tex:415,825`) records $V^\natural$ as
class $M$ with $r_{\max} = \infty$, $\kappa = 12$, $\Delta \ne 0$; the
discrimination remark `rem:census-moonshine-leech-discrimination` (lines
935-962) explicitly contrasts $V^\natural$ (class $M$) against
$V_{\Lambda_{24}}$ (class $G$): "$V^\natural$ has $\Delta = 20/71 \ne 0$";
"$V^\natural$ is class $M$."  The Monster VOA contains the stress tensor and
hence the full Virasoro sub-VOA at $c = 24$, which inherits the Virasoro
shadow tower $r_{\max} = \infty$.  The introduction places $V^\natural$ in
class $G$ by fingerprint projection, in direct contradiction with the census.

(ii) **$n_{\mathrm{strong}}(V^\natural) \ne 196884$.**  Landscape census
footnote (`landscape_census.tex:1202-1208`): "The Monster module $V^\natural$
has a single strong generator $T$ of weight~$2$ ($\dim V_1^\natural = 0$)".
The correct strong-generator count is $1$, not $196884$.  The $196884$ is the
dimension of the weight-$2$ Griess primary component (or equivalently, the
graded dimension $\dim V_2^\natural - 1$ via the coefficient of $q^0$ in
$J(\tau) - 744$); it is not the strong-generator count.

(iii) **"Weight-$1$ non-trivial irreducible Monster representation"** is a
double error: $V^\natural_1 = 0$ (Frenkel-Lepowsky-Meurman uniqueness), so
there is no weight-$1$ space at all, let alone a weight-$1$ Monster irrep.
The smallest non-trivial Monster irrep has dimension $196883$ (acting on
$V^\natural_2 / \mathbb{C}\omega$), appearing at weight $2$, not weight $1$.

(iv) **$p_{\max}(V^\natural) = 4$, not $2$.**  The stress tensor OPE gives
$p_{\max} = 4$ for any VOA containing a Virasoro sub-VOA at $c \ne 0$; this
is $p_{\max}(\Vir_c) = 4$ from
`infinite_fingerprint_classification.tex:312`.

**Consequence.**  Theorem
`thm:part-ii-moonshine-via-fingerprint` (Monster moonshine claim) is
inscribed with a wrong fingerprint.  Because that theorem's conclusion (the
$194$ twining fingerprints, Conway-Norton correspondence) does not depend on
the specific $(p_{\max}, r_{\max}, n_{\mathrm{strong}})$ values, this is a
slot-data error, not a theorem-level error: heal by restoring the census
values.

### F2. BLOCKING: $\kappa$-isospectral example is self-contradictory

**Lines 131-141.**  The first "four independent obstructions" item attempts to
exhibit two $\kappa$-isospectral chiral algebras:

> The Heisenberg algebra $H_k$ has $\kappa(H_k) = k$; the affine
> Kac-Moody algebra $V_k(\fsl_2)$ at level $k$ has
> $\kappa(V_k(\fsl_2)) = 3(k+2)/4$.  Tuning $k = \frac{4}{3}\kappa(H_k) - 2$
> produces two non-isomorphic algebras with identical $\kappa$; they are
> separated by $p_{\max}(H_k) = 2$ versus $p_{\max}(V_k(\fsl_2)) = 2$
> (same pole order) and by $\chi_{\VOA}$, ...

Two errors:

(i) **Notation collision.**  The symbol $k$ is bound to the Heisenberg level
in the first clause, then reused for the affine level in the "tuning" clause.
The tuning equation $k_{\text{aff}} = \frac{4}{3} k_{\text{Heis}} - 2$ is
sensible, but the $k$-as-shared-letter presentation makes the equation
self-referential ($k = \frac{4}{3}k - 2$ solves to $k = 6$ and hides the
degree of freedom).

(ii) **"Separated by $p_{\max} = 2$ versus $p_{\max} = 2$."**  The two pole
orders are equal; this clause announces separation by a slot that does not
separate.  Direct internal contradiction.  The correct separator in the
$(p_{\max}, r_{\max})$ projection is $r_{\max}$: $H_k$ has $r_{\max} = 2$
(class $G$); $V_k(\fsl_2)$ has $r_{\max} = 3$ (class $L$).

### F3. Witness fingerprint for $V_k(\fsl_2)$: $n_{\mathrm{strong}}$ choice

**Line 259.**  The $V_k(\fsl_2)$ witness lists $n_{\mathrm{strong}} = 3$
(i.e., $\dim \fsl_2$).  This is the standard strong-generator count and
matches the Kac-Wakimoto convention in the independent-verification row
(line 819-823).  Accepted, no heal needed.  Included here only to note that
the choice is the bracketed-generator count (not PBW-minimal count with
derivatives absorbed, which would give $1$ for $\mathrm{Vir}_c$ and $1$ for
$V^\natural$ in the same sense).  The $V^\natural$ row in F1(ii) must use
the same convention.

### F4. CG architecture: deficiency opening present; five-shadow list compliant

Introduction section text (lines 50-118) opens with the Virasoro OPE
(classical reading), names the deficiency ("The one-coordinate reading is a
shadow"), exhibits the five-slot survivor
$\varphi = (p_{\max}, r_{\max}, \chi_{\VOA}, n_{\mathrm{strong}},
\mathrm{coset})$, and announces the forced transition to the fingerprint
theorem schema.  Satisfies CG deficiency-opening + unique-survivor pattern.
AP109 (list results before proving) and AP111 ("What this chapter proves"
block): compliant.  AP106 ("This chapter constructs..."): line 47-48 uses
neutral chapter heading; line 114-118 opens with the deficiency, not the
results list.  Pass.

### F5. AP235 ("quaternitomy") sweep

Grep on the file: eight occurrences of "quadrichotomy"; zero occurrences of
"quaternitomy".  Pass.

### F6. AP/HZ metadata hygiene

Grep for `AP\d+`, `HZ-\d+`, `V[0-9]-AP`, `AP-CY\d+`, `/B\d+`, `Pattern \d+`,
`Cache #\d+` in typeset lines of the target file: zero hits.  Pass.

### F7. AI-slop / em-dash / hedging sweep

Grep HZ-10 tokens (`moreover`, `additionally`, `notably`, `crucially`,
`remarkably`, `interestingly`, `furthermore`, `we now`, `worth noting`,
`delve`, `leverage`, `tapestry`, `cornerstone`, `journey`, `navigate`), em-dashes
(`---`, U+2014), hedging (`arguably`, `perhaps`, `seems to`, `appears to`):
zero hits in typeset prose.  One `---` in the comment header (line 3, inside
`%`), which is allowed.  Pass.

### F8. $E_1$-first architecture

The introduction presents the shadow tower as the backbone
(§\ref{sec:part-ii-shadow-tower}); the $r = 2$ rung is $\kappa = S_2$.
No $E_1$-ordered vs symmetric-bar distinction is made in the introduction
because the introduction speaks at the $\varphi$ level, which is
$\Sigma_n$-coinvariant by construction (pole order, shadow depth, Euler
character, strong-generator count, and coset are all averaging-invariant).
Compliant: the introduction does not advertise a symmetric-bar result
without the ordered primitive; it advertises the coarse projection of a
fingerprint, which is inherently $\Sigma$-invariant.

### F9. Scope qualifier: Theorem
`thm:part-ii-fingerprint-complete-invariant`

Statement (lines 308-325) quantifies "for any two chirally Koszul chiral
algebras $\cA, \cB$ in the standard landscape".  The qualifier "in the
standard landscape" is essential: the reconstruction functor
$\Phi_{\mathrm{recon}}: \mathcal{F} \to E_1\text{-coAlg}^{\mathrm{chir},
\mathrm{aug}, \mathrm{conil}}_{/X}$ is constructed only on the standard
landscape (the explicit landscape families with landscape-census entries).
Outside the standard landscape, the five slots may still be defined but
completeness is not asserted.  Pass.

### F10. Higher-genus fingerprint (§7): AP225-adjacent scope

**Lines 602-627.**  The statement asserts $p_{\max}$ and $r_{\max}$
genus-independent; $n_{\mathrm{strong}}$ genus-independent; $\chi_{\VOA,g}$
genus-deformed by $(1-q^g)^{-\kappa(\cA)}$; and $\mathrm{coset}_g$ obtained
by clutching.  The $(1-q^g)^{-\kappa(\cA)}$ formula is advertised in the
shadow-kernel ("modular-bootstrap closed form"); this is a
UNIFORM-WEIGHT claim.  HOT ZONE HZ-3 (AP32) requires an explicit
scope tag.  Line 624: "uniform-weight formula
$\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$
(UNIFORM-WEIGHT) and its all-weight correction
$\delta F_g^{\mathrm{cross}}$ (ALL-WEIGHT)."  The tag is present and
propagated.  Pass.  **Note** (AP225): the all-genera claim is the one Beilinson
noted as conditional until clutching-uniqueness is proved
(Chapter `ftm_seven_fold_tfae_platonic.tex:thm:clutching-uniqueness`,
inscribed 2026-04-16 wave).  The introduction references this via the
ALL-WEIGHT correction and does not claim an unconditional all-genera
factorisation beyond UNIFORM-WEIGHT; scope is honest.

### F11. Fifth class (FF) inscription vs CLAUDE.md G/L/C/M/M*/W

CLAUDE.md north star lists extended classes $G/L/C/M/M^*/W$ with $M^*$ (log
CFT) and $W$ (extended W-algebras beyond class $M$).  The Part II
introduction inscribes only $G/L/C/M/\mathrm{FF}$ (with $\mathrm{FF}$ the
critical-level Feigin-Frenkel stratum at $\kappa = 0$) and does not mention
$M^*$ or $W$.

Two readings:

(a) The $M^*$ (logarithmic) stratum is a refinement of class $M$, not a
separate coarse stratum: $V^\natural$, $\Vir_c$, $W(p)$ all have
$r_{\max} = \infty$, and $M$ vs $M^*$ is a logarithmic-submodule
distinction at the bar-complex level.  Similarly, extended $W$ families
($W_N, W_\infty$) sit in class $M$ by $r_{\max} = \infty$.

(b) The $G/L/C/M/\mathrm{FF}$ coarse projection of the introduction is
the $r_{\max}$-valued projection, and $M^*, W$ are not $r_{\max}$-indexed.
They appear as refinements carried by other slots ($\chi_{\VOA}$,
$\mathrm{coset}$).

The introduction is honest at the coarse projection level; no heal needed
on this point, but the architecture is declared:
the $G/L/C/M/\mathrm{FF}$ coarse projection is one-dimensional (indexed by
$r_{\max}$), whereas $M^*/W$ are refinements visible through the remaining
four slots.  Accepted.

---

## Heal: surgical edits

Two slot-data errors fixed in place; notation collision in F2 healed;
everything else left intact.

### Edit 1 (F2: $\kappa$-isospectral example)

Restore mathematical content: Heisenberg and affine $\fsl_2$ are
$\kappa$-isospectral when the affine level is tuned to
$k_{\mathrm{aff}} = \frac{4}{3}k_{\mathrm{Heis}} - 2$, separated by
$r_{\max}$ (not $p_{\max}$: both carry $p_{\max} = 2$).

### Edit 2 (F1: $V^\natural$ fingerprint)

Restore the landscape census values: $(p_{\max}, r_{\max}, \chi, n_{\mathrm{strong}},
\mathrm{coset}) = (4, \infty, \chi, 1, \mathrm{coset})$.  Correct the
$n_{\mathrm{strong}}$ proof-text to identify it as the single strong generator
$T$ ($V^\natural_1 = 0$, Virasoro sub-VOA determines $\kappa$).  Remove the
"lattice-orbifold-type shadow tower stabilizing at $r = 2$" justification (it
was wrong).

### Edit 3 (F1 follow-through: moonshine theorem dependency map)

Line 511's fingerprint is referenced from Theorem
`thm:part-ii-moonshine-via-fingerprint` (line 503) and from
`thm:part-ii-platonic-completeness` (line 657).  The corrected fingerprint
propagates atomically: only the $\varphi$ display in the moonshine theorem
changes; the $194$-twining conclusion is independent of the slot values.

---

## Verification after heal

(a) Grep "quaternitomy": 0.  Grep "quadrichotomy": 8.  Pass.
(b) Grep `AP\d+|HZ-\d+|/B\d+` in typeset prose: 0.  Pass.
(c) Grep AI slop tokens + em-dash: 0 in typeset prose.  Pass.
(d) Cross-reference against `landscape_census.tex:415,825,935-962,1202-1208`:
    $V^\natural$ fingerprint matches ($r_{\max} = \infty$, $n_{\mathrm{strong}} = 1$,
    $\kappa = 12$, class $M$).  Pass.
(e) Cross-reference against
    `infinite_fingerprint_classification.tex:297-323` pole-depth independence
    table: Heisenberg $(2,2)$, affine $(2,3)$, $\Vir_c\; (4,\infty)$.  Part II
    introduction witnesses match.  Pass.

No build or test invocation (per task scope).

---

## Report

Three edits land in `chapters/frame/part_ii_platonic_introduction.tex`,
restoring consistency with the landscape census on $V^\natural$ and fixing a
self-contradictory slot separator in the $\kappa$-isospectral example.  No
other Part II chapters touched.  No commit.
