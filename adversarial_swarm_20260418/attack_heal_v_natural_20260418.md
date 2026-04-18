# Adversarial Attack-and-Heal: thm:v-natural-e3-topological

**Target:** `chapters/examples/chiral_moonshine_unified.tex:374-451` (theorem + proof).
**Date:** 2026-04-18.
**Author:** Raeez Lorgat.
**Prior flag:** AP287 in CLAUDE.md (cross-volume theorem existence without HZ-11 attribution).
**AP block consumed:** AP581-AP584 (four new anti-patterns surfaced this wave).

---

## PHASE 1 — ATTACK

### A1. HZ-11 scope-inheritance violation (AP287 primary).

The theorem is tagged `\ClaimStatusProvedHere`. Its proof clauses (ii) and (iii)
cite Vol~II material:

- Clause (ii): Vol~II `thm:uhf-monster-orbifold-bv-anomaly-vanishes`
  (universal_holography_functor.tex:497).
- Clause (iii): Vol~II Section `uhf-monster` (same file, :483--574), passed
  through the "universal holography functor $\Phi_{\mathrm{hol}}$".

Both Vol~II theorems are inscribed with proof bodies (verified). But a
Vol~I `ProvedHere` theorem whose load-bearing lemmas live only in Vol~II
violates HZ-11: the correct tag is `\ClaimStatusProvedElsewhere` with a
Remark[Attribution], OR the Vol~II theorems must be inscribed locally.
Currently neither discipline is applied.

### A2. Phantom file / phantomsection mask for thm:topologization-tower (AP255).

`def:e3-topological` at :359--372 names the canonical form of its
working definition as "the topologization tower theorem
`thm:topologization-tower` of Vol I (`en_koszul_duality`)". Grep:

- `\label{thm:topologization-tower}` inscribed: zero hits in Vol I chapters.
- `\phantomsection\label{thm:topologization-tower}` alias: `preface.tex:5146`,
  aliased to Vol II `thm:iterated-sugawara-construction` +
  `thm:e-infinity-topologization-ladder` (`e_infinity_topologization.tex`).
- `standalone/theorem_index.tex:2382` explicitly flags:
  "PHANTOM FILE: chapter does not exist on disk; AP255".

The `def:e3-topological` citation thus points at a phantom-masked alias.
The definition itself is correct structurally, but its canonical-reference
claim is textbook AP255.

### A3. Iterated-Sugawara scope mismatch (AP581).

Clause (i) claims "the iterated Sugawara construction of Vol II
`e_infinity_topologization` applies" at rung $n=2$. Vol II
`thm:iterated-sugawara-construction` (Vol II CLAUDE.md Topologization row
+ `e_infinity_topologization.tex:229`) proves inner higher-spin Casimirs
$\{T^{(n)}\}$ for principal $\cW_N$ obtained via DS reduction of affine
Kac-Moody at non-critical level. The machinery is Feigin--Frenkel
screening plus BRST primitive constructions on affine KM V_k(\fg).

V^natural is **not** affine KM; it is the $\Z/2$-orbifold of the
Leech-lattice vertex operator algebra $V_{\Lambda_{24}}$. Its
stress tensor is the FLM/Griess Sugawara (sum over 196884 weight-2
Griess primaries), not the Sugawara composite of an affine Kac-Moody
current algebra. The iterated-Sugawara machinery at rung $n \geq 2$
requires an input tower of inner higher-spin Casimirs inside an affine
KM parent; V^natural has neither an affine KM parent nor an
explicitly inscribed higher-spin Casimir tower inside the Griess
algebra. Clause (i) as written invokes the wrong machinery for the
object under study.

The *correct* route to E_3-topological for V^natural is the one
inscribed in Vol II `thm:monster-chain-level-e3-top`
(`chapters/connections/monster_chain_level_e3_top_platonic.tex:41`):

1. Leech-lattice parent $V_{\Lambda_{24}}$ is class G (abelian).
   It is E_3-topological via **abelian holomorphic Chern--Simons**
   (Costello--Li), not via iterated Sugawara.
2. $\Z/2$-orbifold (lattice-involution $\sigma = -1$ on $\Lambda_{24}$)
   descends the chain-level E_3-topological structure to the invariant
   algebra when the Dijkgraaf--Witten anomaly class vanishes.
3. V^natural is the $\sigma$-invariant part plus the twisted sector
   with half-spinor ground state; the twisted-sector Jacobi identity
   (FLM \S 8--10) is chain-level associative.

This replaces clause (i)'s iterated-Sugawara story with the genuine
abelian-CS-plus-orbifold story. The proof then routes through Vol II
`thm:monster-chain-level-e3-top` with explicit attribution, not
through the inapplicable iterated-Sugawara machinery.

### A4. "c=24 non-critical for every Virasoro factor" category error (AP582).

Clause (i) writes: "the effective level is $c = 24$, non-critical for
every Virasoro factor". Inside the proof: "the critical level for a
rank-24 lattice VOA is $k = -h^\vee$, which for the abelian lattice
limit is $k = 0$; $k = 24$ is far from critical."

This conflates three different critical-level conventions:

- **Affine KM critical level:** $k = -h^\vee$ for the Sugawara
  construction of $V_k(\mathfrak{g})$.
- **Heisenberg / lattice VOA critical behaviour:** the level parameter
  $k$ in the abelian Heisenberg $H_k$ (OPE $J(z)J(w) \sim k/(z-w)^2$)
  becomes degenerate at $k=0$ where Sugawara $T = (1/(2k)){:}JJ{:}$
  is ill-defined. Lattice VOAs normalise $k=1$ by construction.
- **Virasoro central charge $c$:** Virasoro at $c$ is its own family
  with its own structural invariants ($\kappa^{\mathrm{Vir}} = c/2$);
  there is no "critical $c$" in the affine-KM sense. Self-duality
  hits at $c = 13$; $c = 24$ is an ordinary value.

V^natural at $c = 24$ is not "non-critical in an affine-KM sense"
because V^natural is not an affine KM algebra. The statement as written
is a category error. The correct substance (V^natural has a
well-defined Virasoro stress tensor at $c = 24$) survives; the
mechanism wording must change.

### A5. Clause (iii) wrong cross-reference.

Clause (iii) claims chain-level E_3-topological via "the universal
holography functor $\Phi_{\mathrm{hol}}$ of Vol II Section
`uhf-monster`". Section `uhf-monster` inside
`universal_holography_functor.tex:483--574` proves the BV anomaly
vanishing (which is clause (ii) already). It does not, by itself,
prove chain-level E_3-topological descent.

The load-bearing chain-level E_3 statement is Vol II
`thm:monster-chain-level-e3-top` (`monster_chain_level_e3_top_platonic.tex:41`),
which is a separate chapter. Its Step 5 is the explicit
chain-level descent:

> "By Theorem thm:uhf-leech-class-M-chain-level, $V_\Lambda$ admits
> a chain-level $E_3$-topological structure as the boundary of abelian
> holomorphic Chern-Simons with charge lattice $\Lambda$... Chain-level
> $E_3$-topological structure passes to $\Z/2$-invariants when the
> orbifold BV anomaly vanishes..."

Clause (iii)'s citation is under-informed: the reader pointed at
Section `uhf-monster` cannot close the chain-level descent from what
that section contains alone.

### A6. "c_N(0)/2" / "class-M chain-level" propagation probe.

Vol II `thm:monster-chain-level-e3-top` uses **abelian holomorphic CS**
for the parent + orbifold BV anomaly vanishing for the descent.
Neither step invokes `thm:chd-ds-hochschild` (the DS-Hochschild
bridge). Good: the V^natural chain-level claim does NOT depend on
the DS route that scopes to $V_k(\mathfrak{g}) \rightsquigarrow
\cW_k(\mathfrak{g},f)$ principal/hook nilpotents. The class-M chain-level
status for V^natural is independent of `thm:chd-ds-hochschild` and
of Vol~I class-M MC5 direct-sum scope; the mechanism is lattice-orbifold
BV, which bypasses the direct-sum chain-level issue flagged in
CLAUDE.md MC5 row. This is a relief on first reading and the healed
theorem should SAY SO explicitly (the reader otherwise inherits the
class-M chain-level anxiety from adjacent rows).

### A7. Tautology test in compute/tests/test_chiral_moonshine_unified.py.

Nothing load-bearing attached to V^natural E_3 status in the current
test file; the engine tests target bar-Euler coefficient counts
($c(1) = 196884$ etc.) and shadow-class transitions. No HZ-IV decorator
on the E_3 claim.

### A8. "Chiral moonshine unified" — genuinely unified or portmanteau?

The chapter inscribes four SECTOR-SPECIFIC theorems
(`thm:moonshine-bar-euler-master` + sector theorems for Monster,
Conway, Thompson, Mathieu) plus the master bar-Euler identity. The
unity claim is legitimate at the level of the bar-Euler identity
framework (one identity, four specialisations). The title is
substantively earned. (The Monster sector's E_3-topological status is
independent of the master bar-Euler identity; fixing it does not
affect the title.)

---

## PHASE 2 — SURVIVING CORE

After attacks A1--A5, the following STRUCTURAL SUBSTANCE survives:

**Leech parent is class G + E_3-topological.** Costello--Li abelian
holomorphic Chern-Simons on $X \times \mathbb{R}$ with charge lattice
$\Lambda_{24}$ constructs a chain-level E_3-topological bulk
factorisation algebra whose boundary is $V_{\Lambda_{24}}$. This is
a *theorem* of Vol II (`thm:uhf-leech-class-M-chain-level` referenced
in `monster_chain_level_e3_top_platonic.tex:144`, routing through
`thm:E3-topological-km`).

**$\Z/2$ orbifold BV anomaly vanishes at chain level.** Vol II
`thm:monster-chain-level-e3-top` clauses (i) + Step 1-2 prove
explicitly (not merely cohomologically):

- $\sigma$-equivariance of the FLM cocycle $\epsilon$ on the nose
  (even bilinearity of $\langle \cdot,\cdot \rangle$ on $\Lambda$);
- $\Lambda^\sigma = 0$ (lattice is torsion-free), so
  $\epsilon|_{\Lambda^\sigma} \equiv 1$ literally;
- Kapustin--Saulina (2011) lattice-involution DW formula:
  $\alpha_{\mathrm{DW}}(\sigma) = \mathrm{sign}(\det(1-\sigma)) \cdot
  [\epsilon|_{\Lambda^\sigma}]_{H^3} = (+1) \cdot 1 = 1$,
  so $\alpha_{\mathrm{orb}} = 0$ in $H^3(B\Z/2;\mathrm{U}(1)) \cong \Z/2$.
- Borcherds cross-check (independent, number-theoretic): modular
  invariance of $j(\tau) - 744$ rules out an obstructing U(1) phase.

**Chain-level descent to V^natural.** Vol II
`thm:monster-chain-level-e3-top` Steps 3--5 finish: the FLM
twisted-sector Jacobi is chain-level associative on the nose; the
orbifold differential $Q^{\mathrm{orb}} = Q|_{\mathrm{inv}} \oplus
Q^{\mathrm{tw}}|_+$ squares to zero strictly; chain-level E_3-topological
passes to invariants when $\alpha_{\mathrm{orb}} = 0$.

**Class-G-to-class-M transition.** The Leech parent is class G, shadow
finite. V^natural is class M, shadow infinite. The transition is
real (the Griess algebra has 196884 independent weight-2 primaries,
not just the abelian Cartan), and it happens *across the $\Z/2$
orbifold step*. But the E_3-topological status is preserved across
this class transition because the orbifold BV anomaly vanishes.
Shadow class and E_n-topological status are orthogonal invariants
(class G, L, C, M can each be E_3-topological on its own terms).
This is the correct substance of the existing `rem:vnat-class-transition-clarified`.

The surviving core is: **V^natural is chain-level E_3-topological
because (a) its Leech parent is chain-level E_3-topological via
abelian holomorphic Chern-Simons, and (b) the $\Z/2$ orbifold BV
anomaly vanishes by three independent routes (lattice-cohomological,
FLM Jacobi, Borcherds modular).** The iterated-Sugawara machinery is
not invoked; the "non-critical $c$" phrase is retracted.

---

## PHASE 3 — HEAL

### H1. Retag `\ClaimStatusProvedHere` → `\ClaimStatusProvedElsewhere`.

Per HZ-11: the chain-level E_3-topological refinement is proved in
Vol~II `thm:monster-chain-level-e3-top`; the BV-anomaly-vanishing is
proved in Vol~II `thm:uhf-monster-orbifold-bv-anomaly-vanishes`;
both theorems have their own `\ClaimStatusProvedHere` tags in their
Vol~II homes with full proof bodies. The Vol~I theorem PACKAGES
those two Vol~II theorems together and adds a Vol~I-specific clause
about the Griess Sugawara's Virasoro presentation. The correct Vol~I
tag is `\ClaimStatusProvedElsewhere`, with a local
`\begin{remark}[Attribution]` naming both Vol~II theorems.

### H2. Rewrite clause (i).

Retire the "iterated Sugawara / rung $n=2$" wording. Clause (i)
becomes: *The Leech-lattice parent $V_{\Lambda_{24}}$ is
E_3-topological via abelian holomorphic Chern--Simons (Costello--Li;
Vol II thm:E3-topological-km applied to the abelian lattice case).
V^natural inherits a conformal vector (the FLM/Griess Sugawara of the
196884 weight-2 Griess primaries) of central charge $c = 24$; no
affine-KM critical-level condition enters because V^natural is not
affine KM.*

### H3. Rewrite clause (iii).

Retarget to `thm:monster-chain-level-e3-top`. Clause (iii) becomes:
*At chain level, V^natural is E_3-topological; this is Vol II
thm:monster-chain-level-e3-top via abelian holomorphic CS for the
Leech parent + chain-level orbifold BV anomaly vanishing by three
independent routes.*

### H4. Retire the phantom `thm:topologization-tower` from def:e3-topological.

`def:e3-topological` currently cites `thm:topologization-tower` of
Vol~I as the canonical form. Replace with direct citation of Vol II
`thm:iterated-sugawara-construction` + `thm:e-infinity-topologization-ladder`
(the two theorems the phantomsection alias points at). Note that for
V^natural, the topologization route is NOT iterated-Sugawara (clause
(i) attack) but abelian CS + orbifold descent (Vol II
`thm:monster-chain-level-e3-top`); the definition is retained as a
working local form, but its mechanism-invocation is broadened to
include both routes.

### H5. Category-error fix on "non-critical level".

"The effective level is $c = 24$, non-critical for every Virasoro
factor" → "The central charge is $c = 24$, at which the
FLM/Griess Sugawara is well-defined (Virasoro has no affine-KM
critical level; the $c = 24$ Virasoro stress tensor is a weight-2
Sugawara composite of the 196884 Griess primaries, not the Casimir
of an affine Kac-Moody current)."

### H6. Remark (Attribution) block naming Vol II theorems explicitly.

Add immediately after the proof:

```latex
\begin{remark}[Attribution and cross-volume routing]
\label{rem:v-natural-e3-attribution}
Theorem~\ref{thm:v-natural-e3-topological} is proved in Volume~II:
clause~(ii) is Vol~II~\ref*{thm:uhf-monster-orbifold-bv-anomaly-vanishes}
(universal_holography_functor.tex); clause~(iii) is Vol~II~\ref*{thm:monster-chain-level-e3-top}
(monster_chain_level_e3_top_platonic.tex), whose Steps~1--5 furnish
the chain-level E_3-topological descent via abelian holomorphic
Chern--Simons for the Leech parent plus Dong--Mason quantum Galois
uniqueness for the orbifold. The Vol~I content is the packaging of
those two Vol~II theorems together with the FLM/Griess Virasoro
presentation internal to $V^\natural$ (clause~(i)). The status tag
is \texttt{ProvedElsewhere} per HZ-11 cross-volume discipline.
\end{remark>
```

(LaTeX: `\end{remark}` typed correctly — the `>` is a typo exemplar
from FM7 and is NOT to be propagated into the file.)

### H7. Propagation pass.

Grep three volumes for `\ref{thm:v-natural-e3-topological}` and
update any consumer that relied on `ProvedHere` semantics.

---

## PHASE 4 — INSCRIBE

Edits to `chapters/examples/chiral_moonshine_unified.tex`:

1. def:e3-topological at :359--372: rewrite canonical-form citation.
2. thm:v-natural-e3-topological header at :374: downgrade tag.
3. Clause (i) at :381--387: abelian-CS-first, Griess-Sugawara as
   conformal vector, no "non-critical level" phrase.
4. Clause (iii) at :393--399: retarget to `thm:monster-chain-level-e3-top`.
5. Proof body at :402--451: drop iterated-Sugawara paragraph from
   (i) and the "non-critical level" gloss; (iii) routes via
   `thm:monster-chain-level-e3-top` Steps 3--5.
6. Append `rem:v-natural-e3-attribution`.

## PHASE 5 — PROPAGATE

Consumer map:

- `chapters/frame/part_ii_platonic_introduction.tex` — mentions
  `thm:v-natural-e3-topological`. Audit for ProvedHere inheritance;
  downgrade if needed.
- `notes/first_principles_cache_comprehensive.md` and `CLAUDE.md` —
  reference only; no `.tex` propagation.
- `compute/tests/test_chiral_moonshine_unified.py` — no HZ-IV block
  for E_3 claim; no code change from this heal.
- Vol II `part_vi_platonic_introduction.tex` — references
  `V1-thm:v-natural-e3-topological`. Update cross-ref comment if the
  Vol I tag change affects downstream prose.

---

## NEW ANTI-PATTERNS REGISTERED (AP581--AP584)

**AP581 (Iterated-Sugawara invoked outside affine-KM scope).** The
Vol II `thm:iterated-sugawara-construction` /
`thm:e-infinity-topologization-ladder` machinery scopes to principal
$\cW_N$ obtained via DS reduction of affine Kac-Moody $V_k(\fg)$ at
non-critical level. Invoking it as the mechanism by which a
non-affine-KM chiral algebra (lattice orbifold, Griess-Sugawara
Virasoro, $\cN{=}4$ superconformal on K3, Borcherds generalized KM
at rank $\geq 2$) becomes E_3-topological is a scope error. For
lattice VOAs and their finite-group orbifolds, the correct route is
abelian holomorphic Chern--Simons (Costello--Li) plus BV-anomaly
vanishing. Counter: before invoking "iterated Sugawara" as the
E_3 mechanism, verify the object is affine KM or is obtained from
one by DS reduction; if not, identify the actual topologization
route (abelian CS, non-abelian CS, boundary of a higher-dim HT QFT,
factorisation-homology pushforward, etc.) explicitly in the proof
body.

**AP582 (Virasoro central charge conflated with affine-KM critical
level).** Writing "$c = N$ is non-critical for every Virasoro
factor" is a category error. Affine-KM critical level is
$k = -h^\vee$ applied to the Sugawara construction of
$V_k(\mathfrak{g})$; it is a condition on the level parameter $k$,
not on the central charge $c$. Virasoro at $c$ has its own
structural invariants ($\kappa^{\mathrm{Vir}} = c/2$, self-duality
at $c = 13$); it has no "critical $c$" in the affine-KM sense.
Counter: state which family the object belongs to (affine KM,
lattice, Virasoro, W, N=2, etc.) and which critical-level
convention is invoked. If the object is not affine KM, the phrase
"non-critical level" is wrong; the correct substance is either
"well-defined Sugawara" or "not at the family-specific degeneration".

**AP583 (Cross-volume clause citing section instead of theorem).** A
clause of a Vol I theorem routes through "Vol II Section X" where
the section contains the *ingredient* lemma rather than the
statement equivalent to the clause. The clause reader cannot close
the argument from the cited section alone. Counter: for every
cross-volume `\ref`, verify the cited label is a theorem whose
statement directly implies the clause, not a section containing
a stepping-stone lemma. If only a section fits, the clause must
name the specific lemma within the section.

**AP584 (Tag `ProvedHere` on a Vol~I theorem that packages two
Vol~II theorems).** When a Vol~I theorem has clauses each proved in
a separately-inscribed Vol~II theorem and the Vol~I content is only
packaging, the correct tag is `ProvedElsewhere` with a Remark
[Attribution] naming both Vol~II theorems. Tagging `ProvedHere`
inflates Vol~I's inscription count (AP60) and violates HZ-11.
Counter: for every Vol~I `ProvedHere` theorem, audit every clause
to verify the proof body *derives* the clause from local Vol~I
material or from classical citations, NOT from cross-volume
theorems cited at label level.

---

## STATUS AFTER HEAL

- `thm:v-natural-e3-topological`: `\ClaimStatusProvedElsewhere`,
  clauses (i)+(ii)+(iii) attributed to Vol II
  `thm:monster-chain-level-e3-top` + `thm:uhf-monster-orbifold-bv-anomaly-vanishes`
  + Vol I FLM/Griess Virasoro presentation.
- Chain-level E_3-topological status for V^natural: unconditional
  (Vol II chain-level inscription), independent of
  `thm:chd-ds-hochschild` DS-reduction route.
- AP287 heal: applied Option (b) in HZ-11 vocabulary (downgrade to
  `ProvedElsewhere` + Attribution remark, rather than inscribing the
  Vol II theorems locally in Vol I).
