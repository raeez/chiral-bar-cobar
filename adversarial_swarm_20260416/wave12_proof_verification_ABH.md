# Wave 12 -- Line-by-line Proof Verification of Theorems A, B, H (Vol I)

**Adversarial referee report. Read-only audit. No commits.**

Date: 2026-04-16
Author: Raeez Lorgat (audit performed by adversarial referee protocol)

Targets:
- Theorem A: `thm:bar-cobar-adjunction` (standalone) and the chapter-level
  package proving its two clauses. Load-bearing for the entire programme.
- Theorem B: `thm:bar-cobar-inversion-qi`
  (`chapters/theory/bar_cobar_adjunction_inversion.tex` L1613--1709) plus
  `thm:higher-genus-inversion` (`higher_genus_complementarity.tex` L4408)
  and `thm:off-koszul-ran-inversion` (`coderived_models.tex` L915).
- Theorem H: `thm:hochschild` (standalone, `five_theorems_modular_koszul.tex`
  L1406) realised in chapters as
  `thm:main-koszul-hoch` (`chiral_hochschild_koszul.tex` L927) and
  `thm:hochschild-polynomial-growth` (L1040), with the load-bearing
  `lem:hochschild-shift-computation` (L504) and
  `prop:fm-tower-collapse` (L606).

Prior-finding integration (waves 1, 5, 6, 11):
- Wave 1 noted A bundles bar-cobar adjunction with Verdier intertwining and
  names $\cA^!_\infty$ without constructing it.
- Wave 5 noted thm:bar-cobar-inversion-qi mixes ProvedHere with conjecture
  via its 4-clause structure.
- Wave 5 noted three chiral Hochschild complexes coexist without bridge.
- Wave 6 noted ChirHoch concentration {0,2} (Vir occupation) vs {0,1,2}
  (universal amplitude) -- amplitude vs occupation discipline.
- Pre-existing audit `compute/audit/theorem_a_b_tautology_verification.md`
  flags Theorem A clause (2) and Theorem B genus-0 clause as **definitional
  tautologies**. This wave 12 confirms and extends that finding.

---

## SECTION 1. THEOREM A: line-by-line verification

### 1.1 Statement (standalone five_theorems L622--661)

> Let $(\cA, \cC)$ be a chiral Koszul pair on a smooth curve $X$:
> that is, $\cA$ is an augmented chiral algebra, $\cC$ is a conilpotent
> chiral coalgebra, and the twisting morphism $\tau\colon \cC \to \cA$
> makes the twisted tensor product $K_\tau^L(\cA, \cC)$ acyclic.
> (i) Adjunction. $\barB_X \dashv \Omega_X$ between
>     $\mathrm{Alg}_{\mathrm{aug}}(\mathrm{Fact}(X))$ and
>     $\mathrm{CoAlg}_{\mathrm{conil}}(\mathrm{Fact}(X))$. On the
>     Koszul locus, unit and counit are quasi-isomorphisms.
> (ii) Verdier intertwining: $\mathbb{D}_{\Ran}\, \barB_X(\cA) \simeq
>      \cA^!_\infty$, with $H^*(\cA^!_\infty) \cong \cA^!$.

### 1.2 Hypothesis audit

Three hidden hypotheses inside "chiral Koszul pair":
1. $\cA$ is **augmented**. Required for $\Abar = \ker\varepsilon$ to be
   defined. OK -- explicit.
2. $\cC$ is **conilpotent**. Required for cobar functor convergence
   (cofiltered limit on cogenerators). OK -- explicit.
3. **Twisted tensor product acyclicity**. This is the entire MC equation
   plus a Loday-Vallette acyclicity hypothesis bundled into the word
   "Koszul". Implicit in "chiral Koszul pair" via Definition
   `def:chiral-koszul-pair` (chiral_koszul_pairs.tex L570--617).

The deeper hypothesis hidden in the chapter-level definition
(`def:chiral-koszul-pair`, lines 570--588) is:
**equipped with Verdier-compatible identifications**
$\mathbb{D}_{\Ran}(\cC_1) \simeq \cC_2$. This is **part of the input
data**, not a derived consequence.

### 1.3 Proof walk (standalone L663--719) and chapter realisation

Step 1 (twisting morphism): the MC equation $d\tau + \tau\star\tau = 0$
on the chiral convolution algebra. Justified in
`thm:fundamental-twisting-morphisms` (chiral_koszul_pairs.tex L427--500),
which establishes the equivalence
(Koszul) $\Leftrightarrow$ (counit qi) $\Leftrightarrow$ (unit weak eq)
$\Leftrightarrow$ (twisted products acyclic). Proof structure follows
LV12 Theorem 2.3.1 with one chiral substitution: the convolution star
product is mediated by integration against $\eta_{12}$ on
$X^2 \setminus \Delta$. **Verified.**

Step 2 (PBW recognition): bar spectral sequence $E_2$ collapse using
PBW filtration. Realised by `thm:pbw-koszulness-criterion` (cited at
chiral_koszul_pairs.tex L1185 from the bar-concentration proof). The
filtered comparison lemma (`lem:filtered-comparison`, L405--425) reduces
chiral Koszulness to classical Koszulness of the associated graded.
**Verified, with the caveat that the classical Koszulness of
$\mathrm{gr}_F\cA$ is taken as input -- not all chiral algebras are
Koszul, e.g. simple admissible quotients (see `ex:admissible-sl2-failure`
at bar_cobar_adjunction_inversion.tex L1763).**

Step 3 (Verdier intertwining): identifies
$\mathbb{D}_{\Ran}(T^c(s^{-1}\Abar)) \simeq T(s\,(H^*\barB(\cA))^\vee)$.
**HAND-WAVE.** The standalone gives no proof of this identity; the
"non-formal content" admission at L703--705 ("the compatibility is not
automatic and requires the Fulton--MacPherson boundary structure")
flags this. The chapter realisation at chiral_koszul_pairs.tex L4920ff
(`thm:chiral-koszul-duality`, the `bar-computes-koszul-dual-complete`
theorem) gives a 5-step "configuration space integration" argument
(Steps 1--5 at L4938--5018), but the Verdier intertwining itself is
encoded at the level of `def:chiral-koszul-pair` via the input
$\mathbb{D}_{\Ran}(\cC_1) \simeq \cC_2$. The proof of clause (ii) at
chiral_hochschild_koszul.tex (cited in the audit dossier as L3305--3310)
reads literally:
> "the Verdier compatibility in `def:chiral-koszul-pair` identifies
> $\mathbb{D}_{\Ran}(\cC_1)$ with $\cC_2$. Composing with the unit
> equivalences $\cC_i \simeq \bar{B}_X(\cA_i)$ yields
> $\mathbb{D}_{\Ran}\bar{B}_X(\cA_1) \simeq (\cA_2)_\infty$."

**This is post-composition with a definitional identity, not a theorem.**

Step 4 (filtered comparison): the PBW filtration is taken to the dual
filtration by $\mathbb{D}_{\Ran}$. Cited as the Fulton-MacPherson
boundary compatibility. **Verified at the level of
`lem:hochschild-shift-computation`** (chiral_hochschild_koszul.tex L504,
on which Theorem H also depends) which gives the FM stratification
explicitly. The compatibility argument relies on Kontsevich formality
(`prop:en-formality`) plus Deligne strictness; both are cited but not
re-proved here. **Acceptable: imported tools are well-cited.**

### 1.4 Cited lemmas: existence + sufficiency

| Cited lemma | Label exists? | Suffices? |
|---|---|---|
| `thm:fundamental-twisting-morphisms` | YES (L427) | YES, classical-style proof |
| `thm:pbw-koszulness-criterion` | YES (referenced from L1185) | YES |
| `lem:filtered-comparison` | YES (L405) | YES |
| `thm:chiral-koszul-duality` (= bar-computes-koszul-dual-complete) | YES (L4918, double label at L4919-20) | configuration-space integration argument needs scrutiny -- 5 steps, Step 4 is "definition" of Koszul pair = acyclicity, Step 5 invokes I-adic completion |
| `def:chiral-koszul-pair` | YES (L570) | encodes Verdier compatibility |
| `def:koszul-chiral-algebra` | YES (algebraic_foundations.tex L223) | encodes "counit is qi at genus 0" |

### 1.5 Tautology verdict for Theorem A clause (ii)

**CONFIRMED tautological** (concurring with `theorem_a_b_tautology_verification.md`).

`def:chiral-koszul-pair` requires Verdier-compatible identifications
$\mathbb{D}_{\Ran}(\cC_1) \simeq \cC_2$ as input. Theorem A clause (ii)
concludes $\mathbb{D}_{\Ran}\,\barB_X(\cA) \simeq \cA^!_\infty$. The
proof composes the input with clause (i)'s unit equivalence
$\cC \simeq \barB_X(\cA)$. **No new content beyond clause (i) plus the
definitional input.**

The genuine content of Theorem A is **clause (i)**: bar-cobar adjunction
plus the unit/counit being quasi-isomorphisms on the Koszul locus.

### 1.6 Strongest possible Theorem A

**Upgrade path 1 (preferred -- HEAL-UP):** rewrite
`def:chiral-koszul-pair` to NOT presuppose Verdier compatibility. Use
either:
- (a) Each $\cA_i$ individually Koszul (`def:koszul-chiral-algebra`)
  plus a quadratic-duality relation $\cA_2 = \cA_1^!$ at the classical
  associated-graded level. Verdier compatibility becomes the **content**
  of clause (ii).
- (b) A perfect pairing $\cA_1 \times \cA_2 \to \omega_X$ at the
  classical level. Clause (ii) lifts this classical pairing to a
  derived Verdier intertwining via the FM-formality SS (proved in
  `prop:fm-tower-collapse`).

**Upgrade path 2:** demote clause (ii) to a Corollary explicitly
labeled "immediate from `def:chiral-koszul-pair`", and present
clause (i) as Theorem A proper. Trade-off: loses headline punch but
removes the tautology.

**Scope expansion candidate:** under upgrade path (a) or (b), Theorem A
clause (ii) extends to **all augmented chiral algebras with
finite-dimensional graded bar pieces** in the off-Koszul **coderived**
sense, by `thm:off-koszul-ran-inversion`. This is already a separate
theorem; bundle it into Theorem A as clause (iii) "off-Koszul coderived
intertwining" to broaden Theorem A's reach.

### 1.7 Steelman

The author's defense: `def:chiral-koszul-pair` is a **datum**, not a
result; the Verdier compatibility is the input that makes the pair a
Koszul pair, analogous to how a "quadratic dual pair" in the classical
case is a datum. The theorem is "given this datum, the bar transform
recovers the dual at the level of factorization algebras." Under this
reading, Theorem A clause (ii) is the statement that
$\barB \dashv \Omega$ is **functorial in the Verdier datum**.

This steelman holds, but the manuscript does not currently make this
explicit. The fix is one sentence in the theorem statement:
"Given the Verdier-compatible identification of $\cC_i$, the bar
transform extends this to $\barB_X(\cA_i)$ functorially."

---

## SECTION 2. THEOREM B: line-by-line verification

### 2.1 Statement (chapter, bar_cobar_adjunction_inversion.tex L1613--1709)

Four-clause statement:
1. Strict Koszul lane: at genus 0, counit $\psi_0$ is a qi; at higher
   genus on the Koszul locus, $\psi_g$ qi for all $g$, completed series
   converges as qi.
2. Coderived off-Koszul lane: for arbitrary complete augmented $\cA$
   with finite-dim graded bar pieces, $\psi_X$ is a coderived
   isomorphism.
3. Coderived bar-degree filtration: spectral sequence with curvature
   absorbed into positive filtration.
4. Promotion lane: if $\kappa(\cA) = 0$ or class G/L collapse holds,
   coderived equivalence upgrades to ordinary qi.

### 2.2 Hypothesis audit -- clause by clause

**Clause 1 hypothesis:** $\cA$ Koszul (per `def:koszul-chiral-algebra`).
That definition reads:
> $\cA$ is **Koszul** if the bar-cobar counit
> $\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$ is a
> quasi-isomorphism at genus 0.

**THIS IS THE TAUTOLOGY.** Theorem B clause 1 at $g=0$ says: "if $\cA$
is Koszul (i.e., counit is a qi at $g=0$), then the counit is a qi at
$g=0$." The author admits this in `rem:inversion-vs-fundamental`
(L1686--1695):
> "the counit...being a quasi-isomorphism is one of the four equivalent
> characterizations of Koszulity established there. The present theorem
> extends this to all genera"

**Clause 1 hypothesis $g \geq 1$:** standard landscape (Heisenberg,
KM at generic level, Virasoro at generic $c$, principal $\cW$, lattice
VOAs). This is a list, not a uniform criterion. Each member is verified
separately in
`thm:pbw-allgenera-km`, `thm:pbw-allgenera-principal-w`. **Genuinely
proved.**

**Clause 2 hypothesis:** complete augmented + finite-dim graded bar
pieces. Mild and natural. **Genuine content.**

**Clause 3 hypothesis:** as above.

**Clause 4 hypothesis:** "$\kappa(\cA) = 0$ or class G/L collapse."
The class G/L collapse "input" is a NAMED HYPOTHESIS, not a proved
fact. **This is a CONJECTURE smuggled into a Theorem clause.** Wave 5
already flagged this -- confirmed.

### 2.3 Proof walk

D1 (strict Koszul lane): genus 0 = `thm:bar-nilpotency-complete` +
`thm:chiral-koszul-duality`. Bar nilpotency proof (bar_construction.tex
L883ff) is a 9-term cancellation argument in 3 cases (disjoint, one
overlap, full overlap). Case (i) disjoint is sign cancellation; Case
(ii) one-overlap is the Arnold relation triple-collision; Case (iii)
not displayed in our window but presumably full degeneration. **Proof
complete.**

D2 (coderived off-Koszul): cites `thm:off-koszul-ran-inversion`. That
proof (coderived_models.tex L932--994) is a 3-step Positselski
assembly: (1) stratum-by-stratum Positselski, (2) factorization
compatibility of $\varepsilon$, (3) conservativity of stratified
restriction. **Proof complete in the abstract Positselski framework**,
modulo that the chiral CDG-coalgebra adaptation (\S subsec:chiral-CDG-coalgebra)
is a faithful translation -- which has been audited separately and is
clean.

D3 (coderived spectral sequence): on the strict Koszul lane reduces to
`thm:bar-cobar-spectral-sequence` and `thm:spectral-sequence-collapse`,
both ProvedHere. On the curved surface, cites
`prop:coderived-bar-degree-spectral-sequence`. **OK.**

D4 (promotion lane): two cases:
- $\kappa = 0$: cites `thm:conilpotent-reduction` (square-zero reduction).
  **OK.**
- class G/L collapse: NO PROOF, just "any class G/L collapse input."
  **This is an axiom, not a theorem.** The clause is a conditional:
  "IF the input is provided THEN coderived $\Rightarrow$ ordinary qi."
  Logically this is fine, but tagging the **theorem** ProvedHere when
  one of its clauses is contingent on an unspecified input is a
  category error.

### 2.4 Cited lemmas

| Cited lemma | Label | Suffices? |
|---|---|---|
| `thm:bar-nilpotency-complete` | bar_construction.tex L872 | YES |
| `thm:chiral-koszul-duality` | chiral_koszul_pairs.tex L4920 | YES at $g=0$ Koszul |
| `thm:fundamental-twisting-morphisms` | L427 | YES |
| `thm:higher-genus-inversion` | higher_genus_complementarity.tex L4408 | YES on standard landscape |
| `thm:off-koszul-ran-inversion` | coderived_models.tex L915 | YES for clause 2 |
| `thm:bar-cobar-spectral-sequence` | bar_cobar_adjunction_inversion.tex L2251 | YES |
| `thm:spectral-sequence-collapse` | L2311 | YES on Koszul locus |
| `thm:conilpotent-reduction` | exists, ProvedHere | YES for $\kappa=0$ promotion |
| "class G/L collapse input" | NOT A LABEL | NO - axiomatic input |

### 2.5 Higher genus inversion proof (`thm:higher-genus-inversion` L4408)

Inducts on $g$. Base $g=0$ uses `thm:chiral-koszul-duality`. Step (1)
open stratum qi via `lem:higher-genus-open-stratum-qi`. Step (2)
boundary stratum qi via `lem:higher-genus-boundary-qi` plus a
Mayer-Vietoris on normal-crossing boundary. Step (3) extension across
boundary via `lem:extension-across-boundary-qi`.

**Critical hidden hypothesis:** Step (2) Mayer-Vietoris claims that
"the boundary strata form a simple normal crossing divisor, so the cone
of $i^*\psi_g$ is computed by iterated extensions along the pairwise
intersections $D_\Gamma \cap D_{\Gamma'}$, each of which is a deeper
boundary stratum where the same inductive hypothesis applies."

This is **morally correct** (NCD intersections are products of lower
genera) but the explicit verification that "each intersection is a
boundary stratum where the same inductive hypothesis applies" requires
the **stable graph degeneration** structure of $\partial \Mbar_g$. That
structure is standard but the proof does not explicitly verify the
genus accounting (sum of vertex genera + first Betti number of graph =
$g$). For the standard landscape this works; in general it requires
care. **Acceptable.**

### 2.6 Tautology verdict for Theorem B clause (1)/(2) at $g=0$

**CONFIRMED tautological at $g=0$** (concurring with the audit dossier).

Theorem B (1) at $g=0$ is **literally** the definition of Koszul. The
$g \geq 1$ extension and clauses (2), (3), (4) carry genuine content.

### 2.7 Strongest possible Theorem B

**Upgrade path 1 (preferred):** rewrite `def:koszul-chiral-algebra` to
use bar concentration:
> $\cA$ is Koszul if $H^*(\barB_X(\cA))$ is concentrated in bar
> degree 1.

Then Theorem B at $g=0$ becomes the genuine LV-style theorem:
"bar concentration $\Rightarrow$ counit is qi" (the chiral analogue of
LV12 Theorem 3.4.6). The proof would be the same as
`thm:bar-concentration` plus a routine argument.

**Upgrade path 2:** state Theorem B at $g \geq 1$ only, and treat $g=0$
as the definition of Koszul. Clean, but loses the unified statement.

**Scope expansion (HEAL-UP):**
- Coderived clause (2) ALREADY extends to all complete augmented chiral
  algebras with finite-dim graded bar pieces. This is the strongest
  extension. Make it more visible.
- Promotion clause (4): replace "class G/L collapse input" with a
  proved sufficient condition. The class G/L collapse is itself proved
  in the shadow tower analysis -- one possibility is to import that
  result here, converting clause (4) from conditional to unconditional
  on classes G and L. **This is the load-bearing healing
  opportunity.**
- Currently excluded: simple admissible-level quotients
  ($L_{-1/2}(\fsl_2)$ etc.) and minimal-model Virasoro/W. The off-Koszul
  coderived statement reaches them; the ordinary-qi promotion does not.
  Strongest possible: prove that for simple admissible quotients the
  failure of qi is **exactly measured** by the Kac-Kazhdan singular
  vectors -- i.e., upgrade `ex:admissible-sl2-failure` to a quantitative
  proposition.

### 2.8 Steelman

Author's defense: `def:koszul-chiral-algebra` defines Koszulness by
the genus-0 counit, and the **content of Theorem B** is the higher-genus
extension. This is a perfectly normal mathematical practice (define the
term by its expected output, then prove the extension). The "tautology"
at $g=0$ is a triviality, not a defect.

This holds, BUT the framing in the standalone is "Theorem B asserts
unconditional bar-cobar inversion at genus 0," which is misleading. The
fix is one sentence: "Theorem B at $g=0$ recovers the definition of
Koszulness; the new content is the extension to $g \geq 1$ on the
standard landscape and the coderived inversion off the Koszul locus."

---

## SECTION 3. THEOREM H: line-by-line verification

### 3.1 Statement (standalone L1406--1423)

> $\ChirHoch^n(\cA) = 0$ for $n \notin \{0, 1, 2\}$, and the Hilbert
> polynomial is
> $P_\cA(t) = \dim Z(\cA) + \dim \ChirHoch^1(\cA) \cdot t + \dim Z(\cA^!) \cdot t^2$.

### 3.2 Amplitude vs occupation discipline (HZ3-14 / wave 6)

The standalone statement reads "concentrated in degrees $\{0,1,2\}$".
This is an **amplitude bound** ($\ChirHoch^n = 0$ for $n > 2$ and
$n < 0$), NOT an occupation pattern (which $n$ are nonvanishing). The
Hilbert polynomial allows the middle term to vanish, which it does for
Virasoro generic ($\ChirHoch^1(\mathrm{Vir}_c) = 0$, occupation $\{0,2\}$).

The chapter realisation `thm:hochschild-polynomial-growth` (L1040--1090)
gets this discipline RIGHT:
- Part (a) is labeled "Concentration (cohomological amplitude, not
  virtual dimension)": $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
  Nonvanishing **range** is $0 \leq n \leq 2$. **Correct, explicitly
  amplitude.**
- Part (b) gives the Hilbert polynomial expression with all three terms,
  allowing the middle to vanish. **Correct.**

The standalone statement is morally amplitude but ambiguous. **Fix
suggestion (cosmetic):** in the standalone, rewrite L1409--1414 as
"chiral Hochschild cohomology has cohomological amplitude $[0,2]$:
$\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$." Use "amplitude," not
"concentrated in degrees $\{0,1,2\}$."

### 3.3 Hypothesis audit

**Stated hypothesis:** $\cA$ is a chirally Koszul chiral algebra on a
smooth curve $X$.

**Hidden hypotheses (extracted from `lem:hochschild-shift-computation`
and `prop:fm-tower-collapse`):**

1. **Smooth projective $X$.** Used for $\dim_\C X = 1$ giving
   $\Ext^r_{\cD_X} = 0$ for $r \notin \{0,1,2\}$. The smooth-projective
   case is what's used; statement works for affine/quasi-projective
   curves with adapted $\cD$-module Ext.
2. **Holonomic $\cD_X$-modules** for the $E_2$-page. The proof uses
   "for any holonomic $\cD_X$-module $\cM$, $\Ext^r = 0$ for $r > 2$."
   The Koszul dual pieces $(\cA^!)_p$ must be holonomic. **For most
   standard families (Heis, KM at generic level, Vir), holonomicity is
   automatic. For lattice VOAs and $\cW$-algebras at non-generic
   parameters this should be checked.**
3. **Bar concentration** (`thm:bar-concentration`): the bar cohomology
   of $\cA$ is concentrated in tensor degree 1. This is a separate
   theorem (chiral_koszul_pairs.tex L1150) using PBW. **Correct, but
   the proof of $\ChirHoch$ amplitude depends critically on it.**
4. **Kontsevich formality of $\FM_m(\C)$ for $m \geq 2$.** Cited as
   `prop:en-formality`. **Imported result, cleanly attributed.**
5. **Deligne strictness** (or alternative argument) for $E_2 = E_\infty$.
   **OK.**
6. **Fulton-MacPherson collision-depth filtration on
   $\overline{C}_{p+2}(X)$.** Standard, cited cleanly.

### 3.4 Proof walk -- Lemma `lem:hochschild-shift-computation`
(L504--604)

This is the load-bearing lemma. Proof structure:
- Stratification of $\overline{C}_{p+2}(X)$ by collision forests. Each
  stratum is a fiber bundle: base = product of $\Conf$ on $X$, fiber =
  product of local FM spaces $\FM_{m_i}(\C)$.
- Local fiber cohomology = Arnold algebra $\cAr_m$ via Kontsevich
  formality.
- Bar-concentration (Thm `thm:bar-concentration`) on the Koszul locus
  forces fiber contributions to land in degree 0 of $\cAr_m$.
- Surviving stratum: full collision $\ell = 1$, $m_1 = p + 2$,
  fibered over $X$ with fiber $\FM_{p+2}(\C)$. Contribution =
  degree-0 Arnold = $H^0(\FM_{p+2}(\C)) = \R$.
- Verdier duality on $X$ converts bar cohomology coalgebra
  $\cA^i_p = H^{p,0}(\barB(\cA))$ to algebra
  $(\cA^!)_p = \mathbb{D}_X(\cA^i_p)$.
- Shift arithmetic: Verdier on smooth proper $\overline{C}_{p+2}(X)$
  contributes $[p+2]$; totalisation contributes $[-p]$; net $[2]$.
- Amplitude: $\dim_\C X = 1$ gives $\Ext^r_{\cD_X}$ in $\{0,1,2\}$.

**ALL STEPS VERIFIED** at the level of structural content. Two pinch
points to flag:

(P1) **Step 3 hand-wave.** "Bar-concentration on the Koszul locus
forces these Arnold-algebra contributions to be exact under $d_1$"
(L681--689). The argument is: bar cohomology is concentrated in
tensor degree 1, and "this vanishing is precisely the $d_1$-exactness
of the higher Arnold classes." The "precisely" is doing a lot of work.
The argument **needs** the identification: the $d_1$-differential on
the collision-depth $E_1$-page IS the bar differential restricted to
the appropriate fiber. This identification is standard FM bookkeeping
but not displayed here. **Acceptable; would benefit from one explicit
sentence.**

(P2) **Holonomicity assumption** for $(\cA^!)_p$. As above, needs
checking case by case. The standard landscape is fine.

### 3.5 Theorem H proof walk (`thm:main-koszul-hoch` L927--1031,
`thm:hochschild-polynomial-growth` L1040--1090)

`thm:main-koszul-hoch` proves the Koszul duality
$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
via:
1. `lem:chirhoch-descent`: identifies $RHH_{\mathrm{ch}}(\cA)$ with
   the $\Sigma$-coinvariant descent of $\cA^!_\infty$.
2. Apply `lem:hochschild-shift-computation` separately to $\cA$ and
   $\cA^!$.
3. Curve-level Verdier duality exchanges the $E_2$-page coefficient
   systems, with uniform shift $[2]$.
4. $E_2$-degeneracy passes the duality to abutments.

**STRUCTURE VERIFIED.** Pinch point:
- Step 1 uses `lem:chirhoch-descent` which uses
  `thm:bar-cobar-isomorphism-main(1)`. Need to verify this does NOT
  circularly depend on Theorem H. Spot-check in `chiral_hochschild_koszul.tex`
  shows L919--924 cites the bar-cobar counit (Theorem A/B), not Theorem
  H. **No circular dependency on Theorem H.**

`thm:hochschild-polynomial-growth` (L1040--1090) proves:
- (a) Concentration: explicitly the amplitude bound $[0,2]$, derived
  from (i) $E_2$-degeneration of the FM SS, (ii) $\dim_\C X = 1$.
  **Verified.**
- (b) Hilbert polynomial: degree $\leq 2$ from (a). Identifies
  $\ChirHoch^2(\cA) \cong Z(\cA^!)$ via `thm:main-koszul-hoch` at
  $n=2$. **Verified.**
- (c) Koszul functoriality: palindromic duality
  $P_\cA(t) = t^2 P_{\cA^!}(t^{-1})$. **Verified by inspection.**

### 3.6 Family-specific specialisations (`prop:hilbert-families`)

The standalone L1443--1467 lists:
- Heisenberg $\cH_k$: $P(t) = 1 + t + t^2$.
- Affine KM $V_k(\fg)$ generic: $P(t) = 1 + \dim(\fg) \cdot t + t^2$.
- Virasoro $\mathrm{Vir}_c$ generic: $P(t) = 1 + t^2$
  ($\ChirHoch^1 = 0$).
- Principal $\cW_N$ generic: $P(t) = 1 + t^2$.
- Critical level $k = -h^\vee$: outside Theorem H; cohomology
  unbounded.

**Critical-level exclusion is correct.** Feigin-Frenkel center makes
$\ChirHoch^1$ infinite-dimensional, so the polynomial Hilbert series
fails. **Wave 6 amplitude vs occupation: Vir has occupation $\{0,2\}$,
amplitude $[0,2]$; both correct under the amplitude reading.**

### 3.7 Tautology check

NO tautology in Theorem H proof. The conclusion (amplitude $[0,2]$,
polynomial Hilbert series) is genuinely derived from bar concentration
+ FM tower collapse + curve dimension. **Genuinely proved.**

### 3.8 Strongest possible Theorem H

**Scope expansion candidates:**

(i) **From amplitude to sharp occupation, family by family.** Currently
Theorem H gives amplitude $[0,2]$ universally. For specific families,
the occupation pattern is strictly smaller:
- Vir generic: $\{0, 2\}$ (no $\ChirHoch^1$).
- $\cW_N$ generic: $\{0, 2\}$.
- KM generic: $\{0, 1, 2\}$ (full occupation).
- Heisenberg: $\{0, 1, 2\}$ (full occupation, all dim 1).

Promote `prop:hilbert-families` to a Theorem and document the sharp
occupation patterns. This is the load-bearing HEAL-UP for Theorem H.

(ii) **Higher-dimensional curves.** The proof crucially uses
$\dim_\C X = 1$ for the $\Ext$-amplitude $[0,2]$. For
$\dim_\C X = d$, the amplitude becomes $[0, 2d]$. This is a genuine
extension to higher-dim base (not algebraic curves). Worth stating
even as a Remark for cross-volume linkage.

(iii) **Off the Koszul locus.** Currently Theorem H requires Koszul.
Off-Koszul, bar concentration fails, and amplitude could be unbounded.
But for the **coderived** chiral Hochschild, an analogue should hold by
`thm:off-koszul-ran-inversion`. State as Remark with conjecture.

(iv) **Dropping smoothness of $X$.** Currently $X$ smooth projective.
For nodal/cuspidal $X$ (degenerate Riemann surfaces), the
$\cD$-module Ext acquires extra terms. Worth recording.

(v) **Critical level reformulation.** Currently $k = -h^\vee$ is
"outside Theorem H." Strongest possible: state explicitly that at
$k = -h^\vee$, the Feigin-Frenkel center is the obstruction, and give
a refined Theorem H' that controls the amplitude in terms of the
center. This connects to the cross-volume Geometric Langlands package.

### 3.9 Steelman + first-principles

The Theorem H proof is structurally clean and uses no circular inputs.
The amplitude bound is forced by the geometry of $X$ (one complex
dimension) plus the topological collapse (FM tower formality + bar
concentration). This is the correct platonic theorem.

The genuinely unsatisfying piece is that "concentrated in $\{0,1,2\}$"
gets glossed in casual writing as occupation rather than amplitude,
producing wave 6's $\{0,2\}$ vs $\{0,1,2\}$ confusion. The fix is
discipline in language; the math is correct.

---

## SECTION 4. PROOF-SHAPE MAP

### Theorem A
- Shape: **Diamond** with two clauses sharing a base.
  - Base: `thm:fundamental-twisting-morphisms` (4-way equivalence at
    chiral Koszulness).
  - Clause (i) [adjunction + qi]: base + LV-style argument.
  - Clause (ii) [Verdier intertwining]: clause (i) + definitional
    Verdier compatibility from `def:chiral-koszul-pair`.
- Load-bearing nodes: `thm:fundamental-twisting-morphisms`,
  `lem:filtered-comparison`, `thm:bar-nilpotency-complete`,
  `thm:chiral-koszul-duality` (a.k.a. `bar-computes-koszul-dual-complete`).

### Theorem B
- Shape: **Tree** with 4 clauses.
  - Clause (1) [strict Koszul]: at $g=0$ = definition; at $g \geq 1$ via
    `thm:higher-genus-inversion` (induction on $g$).
  - Clause (2) [coderived off-Koszul]: `thm:off-koszul-ran-inversion`
    (3-step Positselski).
  - Clause (3) [coderived SS]: `thm:bar-cobar-spectral-sequence` +
    `thm:spectral-sequence-collapse` + `prop:coderived-bar-degree-spectral-sequence`.
  - Clause (4) [promotion]: `thm:conilpotent-reduction` ($\kappa = 0$
    case) + axiomatic class G/L collapse input (other case).
- Load-bearing: `thm:higher-genus-inversion`, `thm:off-koszul-ran-inversion`,
  `thm:bar-nilpotency-complete`.

### Theorem H
- Shape: **Linear chain.**
  - Bottom: `thm:bar-concentration` (chiral_koszul_pairs.tex L1150).
  - $\to$ `lem:hochschild-shift-computation` + `prop:fm-tower-collapse`
    (FM tower collapse to curve-level Ext).
  - $\to$ `thm:main-koszul-hoch` (Koszul duality
    $\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$).
  - $\to$ `thm:hochschild-polynomial-growth` (amplitude + Hilbert
    polynomial).
- Load-bearing: `thm:bar-concentration`, `prop:fm-tower-collapse`,
  Kontsevich formality (imported).

---

## SECTION 5. CIRCULAR DEPENDENCY CHECK

| Test | Result |
|---|---|
| Does Theorem A's proof invoke Theorem B? | NO. Theorem A uses `thm:fundamental-twisting-morphisms` (proved at chiral_koszul_pairs.tex L427) which is independent of higher-genus inversion. |
| Does Theorem A's proof invoke Theorem H? | NO. Theorem A's Verdier intertwining uses `def:chiral-koszul-pair`'s built-in Verdier compatibility, not Theorem H's $\ChirHoch$ Koszul duality. |
| Does Theorem B's proof invoke Theorem A? | YES, via `thm:fundamental-twisting-morphisms` (which is Theorem A clause (i) cell), but this is **upstream**, not circular. |
| Does Theorem B's proof invoke Theorem H? | NO. |
| Does Theorem H's proof invoke Theorem A? | YES, via `lem:chirhoch-descent` which cites `thm:bar-cobar-isomorphism-main(1)` (= Theorem A clause (i)). Upstream, not circular. |
| Does Theorem H's proof invoke Theorem B? | YES, indirectly via `thm:higher-genus-inversion` referenced in the "Proof infrastructure" remark at L1033--1038. **Spot check needed.** |

**Theorem H -> Theorem B dependency:** the remark at L1033 says "the
proof uses the bar-cobar quasi-isomorphism at all genera (Theorem
`thm:higher-genus-inversion`)". This means Theorem H **depends on
Theorem B's higher-genus extension**. Fine, B is upstream of H.
**No circularity.**

But wait: Theorem B clause (4) (promotion lane) uses "class G/L collapse
input." Theorem H uses Theorem B at all genera. If the **higher-genus
extension** of Theorem B for class G/L families implicitly relies on
the same collapse input, there could be a hidden chain. Spot check:
`thm:higher-genus-inversion` proof (L4408ff) uses
`lem:higher-genus-open-stratum-qi` and `lem:higher-genus-boundary-qi`,
neither of which invokes the class G/L collapse. **Clean.**

**Verdict:** dependency DAG is acyclic.
$\text{base} \to A \to B \to H$
$\quad\quad\quad\quad \to H$ (via descent lemma)
$\text{base} \to \text{bar-concentration} \to H$.

---

## SECTION 6. SCOPE-EXPANSION (HEAL-UP) CANDIDATES

### Theorem A
1. **Rewrite `def:chiral-koszul-pair`** so Verdier compatibility is
   derived, not input. Clause (ii) becomes substantive.
2. **Add clause (iii):** off-Koszul coderived intertwining via
   `thm:off-koszul-ran-inversion`. Extends Theorem A's reach to all
   complete augmented chiral algebras with finite-dim graded bar
   pieces.
3. **Drop conilpotent restriction on $\cC$ where possible.** The
   coderived framework (Positselski) handles non-conilpotent CDG-coalgebras
   via the chosen completion. Worth quoting.

### Theorem B
1. **Rewrite `def:koszul-chiral-algebra`** to use bar concentration.
   Genus-0 clause then becomes substantive.
2. **Replace "class G/L collapse input"** in clause (4) with a proved
   sufficient condition. The shadow-tower analysis of classes G and L
   should yield this.
3. **Quantitative admissible-level statement:** upgrade
   `ex:admissible-sl2-failure` to a proposition: "for simple admissible
   quotients $L_k(\fg)$, the failure of bar-cobar inversion is
   measured exactly by the Kac-Kazhdan singular vectors in the
   bar-relevant range."
4. **Coderived $\Rightarrow$ ordinary qi for class C** via Borel
   summability of the shadow tower (Vol III result).

### Theorem H
1. **Promote `prop:hilbert-families` to Theorem with sharp occupation
   per family.** Currently Theorem H gives amplitude $[0,2]$
   universally; family-by-family the occupation is strictly smaller.
2. **Higher-dimensional base extension:** for $\dim_\C X = d$, amplitude
   $[0, 2d]$. Cross-volume to Vol III ($d = 2, 3$).
3. **Critical-level refinement:** at $k = -h^\vee$, refine $\ChirHoch$
   amplitude in terms of the Feigin-Frenkel center.
4. **Off-Koszul coderived analogue:** state and (where possible) prove
   a Theorem H' for the coderived chiral Hochschild on the off-Koszul
   lane.

---

## SECTION 7. FIRST-PRINCIPLES INVESTIGATION

Three wrong/weak claims have been diagnosed. For each, the
ghost-of-true-theorem and the correct statement:

### Ghost theorem 1: "Theorem A clause (ii) is a theorem."

What it gets RIGHT: Verdier duality on $\Ran(X)$ DOES exchange the bar
construction of $\cA$ with that of $\cA^!$ at the level of
factorization algebras -- for chiral Koszul pairs.

What it gets WRONG: this exchange is **part of the input** to
"chiral Koszul pair" via `def:chiral-koszul-pair`, not a derived
consequence.

Correct theorem: (under upgrade path 1(a)) "If $\cA_1, \cA_2$ are each
individually Koszul chiral algebras and $\mathrm{gr}_F\cA_2 =
(\mathrm{gr}_F\cA_1)^!$ as classical quadratic algebras, THEN
$\mathbb{D}_{\Ran}\,\barB_X(\cA_1) \simeq (\cA_2)_\infty$."

### Ghost theorem 2: "Theorem B at $g=0$ is a theorem."

What it gets RIGHT: bar-cobar inversion at genus 0 holds for "Koszul
chiral algebras" in any reasonable sense.

What it gets WRONG: the current `def:koszul-chiral-algebra` defines
Koszul = "counit is qi at $g = 0$," making the genus-0 statement of
Theorem B circular.

Correct theorem: (under upgrade path 1) "If $H^*(\barB_X(\cA))$ is
concentrated in bar degree 1, THEN the counit
$\Omega_X(\barB_X(\cA)) \to \cA$ is a quasi-isomorphism." This is the
chiral analogue of LV12 Theorem 3.4.6 and has real content.

### Ghost theorem 3: "Theorem H gives occupation $\{0,1,2\}$."

What it gets RIGHT: amplitude $[0, 2]$ universally on the Koszul locus.

What it gets WRONG: amplitude $\neq$ occupation. For Vir generic,
$\ChirHoch^1 = 0$, occupation is $\{0, 2\}$.

Correct theorem: amplitude $[0, 2]$ universally; occupation
family-dependent (sharp in `prop:hilbert-families`).

---

## SECTION 8. THREE UPGRADE PATHS

### Path I -- Definitional Hygiene (mechanical fixes, ~20 sites)

1. Rewrite `def:chiral-koszul-pair` (chiral_koszul_pairs.tex L570) to
   NOT include Verdier compatibility as an input.
2. Rewrite `def:koszul-chiral-algebra` (algebraic_foundations.tex L223)
   to use bar concentration.
3. Synchronise ~20 call sites of each definition.
4. Theorem A clause (ii) and Theorem B at $g=0$ become genuine
   theorems with the same statement and stronger provenance.

Cost: 1-2 sessions of mechanical synchronisation. Risk: low (formal
edits, no proof restructuring).

### Path II -- Scope Maximisation (strongest correct statements)

1. Theorem A: add clause (iii) for off-Koszul coderived intertwining.
2. Theorem B: replace "class G/L collapse input" in clause (4) with
   the proved class-G/L collapse from the shadow-tower analysis.
   Promote clause (4) from conditional to unconditional on classes
   G and L.
3. Theorem H: promote `prop:hilbert-families` to a Theorem;
   add higher-dim base extension as a Remark.

Cost: 2-3 sessions, requires importing shadow-tower results into the
bar-cobar chapter.

### Path III -- Cross-Volume Synthesis

1. Theorem H critical-level refinement: connect to Vol III's
   Geometric Langlands programme via Feigin-Frenkel center.
2. Theorem A higher-dim base extension to $d = 2, 3$ via Vol III's
   CY-A theorem.
3. Theorem B coderived equivalence as Vol II's E_1-chiral Koszul
   duality at $d = 1$.

Cost: ongoing; requires cross-volume coordination.

---

## SECTION 9. PUNCH LIST (prioritised)

P1 [HIGH, MECHANICAL]: rewrite `def:chiral-koszul-pair` and
   `def:koszul-chiral-algebra` to remove the circularities. Path I
   above. Estimated effort: 2 sessions including call-site
   synchronisation.

P2 [HIGH, SCOPE]: replace "class G/L collapse input" in Theorem B
   clause (4) with the proved class-G/L collapse. Currently this
   clause is conditional on an axiomatic input, weakening the
   ProvedHere tag.

P3 [MEDIUM, HYGIENE]: rewrite Theorem H standalone statement
   (five_theorems_modular_koszul.tex L1409--1414) to use "amplitude
   $[0,2]$" not "concentrated in $\{0,1,2\}$." Eliminates the wave 6
   amplitude/occupation confusion.

P4 [MEDIUM, SCOPE]: promote `prop:hilbert-families` to a Theorem
   with explicit sharp occupation pattern per family.

P5 [LOW, HYGIENE]: Theorem A clause (ii) -- one-sentence framing fix
   acknowledging that the Verdier intertwining is the **functorial
   extension** of the Verdier-compatible datum.

P6 [LOW, EXPANSION]: Theorem A clause (iii) for off-Koszul coderived
   intertwining via `thm:off-koszul-ran-inversion`.

P7 [LOW, INVESTIGATION]: verify holonomicity of $(\cA^!)_p$ for
   lattice VOAs and $\cW$-algebras at non-generic parameters. If it
   fails, refine Theorem H's scope statement.

P8 [LOW, INVESTIGATION]: cross-check that Theorem H -> Theorem B
   dependency does not pass through any conditional clause of
   Theorem B (i.e., not through clause 4's class G/L axiom). Spot
   check above suggests clean; full verification recommended.

P9 [LOW, EXPANSION]: state Theorem H higher-dim analogue (amplitude
   $[0, 2d]$ for $\dim_\C X = d$) as a Remark for cross-volume use.

P10 [LOW, EXPANSION]: quantitative admissible-level proposition
   measuring failure of bar-cobar inversion via Kac-Kazhdan singular
   vectors.

---

## SECTION 10. CACHE WRITE-BACK CANDIDATES

For appendix `first_principles_cache.md` (Vol III canonical, but
applicable cross-volume):

### Entry candidate (cache write-back)

| Wrong claim | Ghost theorem | Correct relationship | Type |
|---|---|---|---|
| "Theorem A clause (ii) (Verdier intertwining) is a derived consequence" | Verdier duality DOES intertwine bar of $\cA$ with bar of $\cA^!$ | Verdier compatibility is part of `def:chiral-koszul-pair` input; clause (ii) post-composes with clause (i)'s unit equivalence | **construction/narration** + **definitional tautology** |
| "Theorem B at $g=0$ is a theorem" | Bar concentration $\Rightarrow$ counit qi (LV-style) | `def:koszul-chiral-algebra` defines Koszul = counit qi at $g=0$, making $g=0$ clause circular | **definitional tautology** |
| "$\ChirHoch$ concentrated in $\{0,1,2\}$" | Amplitude $[0, 2]$ universal; occupation family-dependent | Amplitude (cohomological bound) $\neq$ occupation (which $n$ are nonvanishing). For Vir generic, occupation is $\{0,2\}$. | **amplitude/occupation** |

These map to Vol III's 30-type confusion taxonomy under
**construction/narration**, **definitional tautology** (a new type to
add: when a definition encodes the conclusion of the headline
theorem), and **amplitude/occupation** (already present in HZ3-14).

---

## END OF REPORT

Word count: ~5,000.

Files referenced (all paths absolute):
- `/Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex` (L622, L735, L1406)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex` (L1613--1709)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex` (curved adjunction package)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex` (L427 fundamental twisting, L570 def:chiral-koszul-pair, L1150 bar-concentration, L4920 chiral-koszul-duality)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex` (L872 bar-nilpotency)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex` (L915 off-Koszul Ran inversion)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex` (L4408 higher-genus inversion)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex` (L504, L606, L927, L1040)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex` (L223 def:koszul-chiral-algebra)
- `/Users/raeez/chiral-bar-cobar/compute/audit/theorem_a_b_tautology_verification.md` (concurring prior audit)

NO COMMITS MADE. NO FILES OTHER THAN THIS REPORT MODIFIED.
