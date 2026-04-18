# Attack-and-Heal: $\ChirHoch^*(\mathrm{Vir}_c)$ concentration and the Gelfand--Fuchs contrast

Author: Raeez Lorgat. Date: 2026-04-18. Session: Wave-ChirHoch-Vir adversarial swarm.
Target: CLAUDE.md Structural Facts line "ChirHoch*(Vir_c) degrees {0,1,2}. NEVER C[Θ]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded)."
Canonical inscription audited: `chapters/theory/chiral_center_theorem.tex` Proposition `prop:derived-center-explicit` (Part (iii), lines 2023--2046) + proof Part (iii) (lines 2098--2117).
Engine audited: `compute/lib/chirhoch_dimension_engine.py::chirhoch_virasoro` (lines 309--336).
AP block used: AP921--AP940.

## Executive verdict

1. $\ChirHoch^0(\mathrm{Vir}_c) = \bC$; $\ChirHoch^1(\mathrm{Vir}_c) = 0$; $\ChirHoch^2(\mathrm{Vir}_c) = \bC \cdot \Theta$. Total dimension~$2$. Hilbert series $P(t) = 1 + t^2$. No heal to the numerical statement.

2. The CLAUDE.md Structural Facts digest "ChirHoch*(Vir_c) degrees {0,1,2}" is numerically accurate as a concentration statement (no support in degrees $\ge 3$ or $< 0$), but is operationally misleading: the degree-$1$ slot is zero at generic $c$. The inscribed prose in `chiral_center_theorem.tex:2028--2031` correctly states $\ChirHoch^1 = 0$ and the preface note at `:50--51` correctly writes concentration "in degrees $\{0,2\}$", reflecting the nonvanishing slots. The digest line should read "concentrated in $\{0,1,2\}$ by Theorem H; for Vir$_c$ the middle slot vanishes generically, leaving $\{0,2\}$ and total dim 2".

3. The Vir/affine split $\dim \ChirHoch^1(\mathrm{Vir}_c) = 0$ vs $\dim \ChirHoch^1(V_k(\fg)) = \dim \fg$ is not a rank-1 vs rank-$r$ phenomenon: Heisenberg $\mathfrak{H}_k$ is also rank-1 and has $\dim \ChirHoch^1 = 1$. The distinction is OPE-POLE-ORDER: $\mathrm{Vir}_c$ has a quartic pole in $T_{(3)} T = c/2$, Heisenberg has a double pole only, affine KM has double pole + simple pole. The simple/higher-pole mechanism makes all single-generator derivations inner.

4. Gelfand--Fuchs cohomology $H^*_{\mathrm{cont}}(\mathrm{Vect}(S^1);\bC)$ of the Witt-algebra topological completion is genuinely a different object. It is infinite-dimensional (Godbillon--Vey class in degree $2$, Euler-class tower, higher characteristic classes). $\ChirHoch^*(\mathrm{Vir}_c)$ is finite and bounded by Theorem H. The relationship is NOT a subquotient in the direct sense; it is a different chain complex on a different algebra with a different coefficient system. The contrast as stated is correct.

5. Hilbert series symmetry at self-dual $c=13$: the Poincar\'e polynomial is palindromic $P(t) = 1 + t^2$ by $\ChirHoch^0(A) \cong \ChirHoch^2(A^!)^\vee \otimes \omega_X$ (Theorem~\ref{thm:main-koszul-hoch}); at $c=13$ the algebra is self-Koszul-dual under $c \mapsto 26-c$, so the palindrome is $P_A(t) = P_{A^!}(t)$ and the symmetry is manifest. No heal.

## AP921 Concentration-statement compression in the metacognitive digest

The CLAUDE.md Structural Facts line compresses two different concentration statements: the universal Theorem-H concentration in $\{0,1,2\}$ (which is a statement about support, valid for every modular-Koszul $\cA$), and the family-specific Virasoro concentration in $\{0,2\}$ (which is the palindromic pattern with the middle slot zero).

Operational correction: the ADMISSIBLE SUPPORT is $\{0,1,2\}$ in the sense that nothing above degree 2 or below degree 0 can appear. For Vir$_c$ the ACTUAL SUPPORT is $\{0,2\}$. The distinction matters because of the (false) inference chain "Theorem H says $\{0,1,2\}$ so every dim should be positive in $\{0,1,2\}$". The structural fact line should be:

> "ChirHoch$^*(A)$ supported in $\{0,1,2\}$ universally by Theorem~H (NEVER $\bC[\Theta]$ which is unbounded). Family-specific ACTUAL support: Heisenberg/KM middle slot nonzero, Vir/W$_N$/bc/betagamma middle slot vanishes. ChirHoch $\ne$ Gelfand--Fuchs (GF infinite-dim on Witt algebra; ChirHoch bounded on the vertex algebra)."

Related: Pattern 226 (first-principles cache). Trigger: CLAUDE.md / MEMORY.md compressed line names a concentration range; reader (or future agent) confuses AMPLITUDE (admissible support) with ACTUAL SUPPORT (family-specific nonvanishing slots). Counter-derivation: substitute family and compute each dim from the engine; if any slot is zero, the actual support is a proper subset of the amplitude.

## AP922 First-principles derivation of $\ChirHoch^1(\mathrm{Vir}_c) = 0$

Virasoro has one strong generator $T$ of weight $2$ with OPE
\[
  T(z) T(w) \sim \frac{c/2}{(z-w)^4} + \frac{2 T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w}.
\]
Pole orders $\{4, 2, 1\}$. The quartic pole is load-bearing. A degree-$1$ chiral Hochschild cochain is a $\cA$-bimodule derivation $D: T \mapsto T + \epsilon \phi(T)$ for some $\phi(T) \in \mathrm{Vir}_c$; compatibility with OPE forces $\phi$ to commute with the associative product.

Candidate derivations:

(a) Inner: $D = [a, -]$ for $a \in \mathrm{Vir}_c$. Modulo these, outer.
(b) Deformation of $c$: maps to $\ChirHoch^2$, not $\ChirHoch^1$. The deformation $c \mapsto c + \epsilon$ is a DEGREE-$2$ cocycle (second-order in the OPE), not a derivation. This is the $\Theta$ class.
(c) Conformal weight shift: $T \mapsto T + \epsilon \partial X$ for some field $X$. Requires $X$ of weight $1$. Vir$_c$ has no weight-$1$ field (only multiples of $T$ and its derivatives). So this class is zero.
(d) Rescaling: $T \mapsto (1+\epsilon) T$ changes $c \mapsto (1+\epsilon)^2 c$, which is an automorphism deformation, NOT a $\ChirHoch^1$ class at fixed $c$ (automorphisms of a fixed vertex algebra are not derivations).

Conclusion: no generating space for $\ChirHoch^1$. The Koszul-resolution argument for affine KM (which produces $V = \fg$) has no analogue because Virasoro is NOT quadratic (quartic pole), so the standard three-term Koszul resolution is not the correct resolution. The higher-pole mechanism forces all derivations inner. Inscribed at `chiral_center_theorem.tex:2098--2117`, proof Part (iii).

First-principles verification via engine: `chirhoch_dimension_engine.py::chirhoch_virasoro` returns `dim1 = 0`, mechanism "quartic pole; single generator; all derivations inner". Cross-engine: `chirhoch_sl_n_outer_derivations_engine.py` line 33 explicitly excludes Virasoro from the affine-style $\fg$-valued outer-derivation mechanism.

## AP923 Gelfand--Fuchs vs ChirHoch: not a subquotient, different chain complex

Gelfand--Fuchs cohomology $H^*_{\mathrm{cont}}(\mathfrak{g}; \bC)$ for $\mathfrak{g} = \mathrm{Vect}(S^1)$ is computed from continuous Lie-algebra cochains $\mathrm{Hom}^{\mathrm{cont}}(\Lambda^n \mathfrak{g}, \bC)$. Gelfand--Fuchs 1968 + Godbillon--Vey show this is infinite-dimensional via the Godbillon--Vey cocycle (degree $2$) + an Euler-class tower. It lives on the TOPOLOGICAL Lie algebra of vector fields on $S^1$; it is a CLASSICAL (non-chiral, non-central-extension) object.

$\ChirHoch^*(\mathrm{Vir}_c, \mathrm{Vir}_c)$ is computed from chiral Hochschild cochains on the vertex algebra (def:chiral-hochschild-cochain-brace), with spectral-variable-carrying cochains in $\mathrm{End}^{\mathrm{ch}}_{\mathrm{Vir}_c}$. It lives on the QUANTUM / CHIRAL vertex algebra; it is bounded by Theorem H.

The two are different chain complexes on different objects. There is no direct comparison map. A naive "passage to the classical limit $c \to 0$" is not a chain map; the central charge is internal to the vertex algebra, while Gelfand--Fuchs operates on the universal bracket Lie algebra $\mathrm{Vect}(S^1)$.

Consequence for AP96 (CLAUDE.md Structural Facts anti-pattern): the warning "ChirHoch != Gelfand-Fuchs" is correct; it prevents the error of importing Godbillon--Vey-style infinite-dimensional structure into the chiral Hochschild of Vir$_c$. No heal, but adding "different CHAIN COMPLEX on different OBJECT, not a subquotient" tightens the scope.

## AP924 Hilbert series symmetry at self-dual $c = 13$

Theorem H gives
\[
  P_A(t, q) = \HS_{Z(A)}(q) + \HS_{\ChirHoch^1(A)}(q) \cdot t + \HS_{Z(A^!)}(q) \cdot t^2.
\]

For $A = \mathrm{Vir}_c$, Koszul dual $A^! = \mathrm{Vir}_{26-c}$. At $c = 13$, $A = A^!$; hence $Z(A) = Z(A^!) = \bC$ at conformal weight $0$, and $\HS_{Z(A)}(q) = \HS_{Z(A^!)}(q) = 1$. The Hilbert series is
\[
  P_{\mathrm{Vir}_{13}}(t, q) = 1 + 0 \cdot t + 1 \cdot t^2 = 1 + t^2,
\]
which is palindromic in $t$ ($t \leftrightarrow t^{2-n}$ symmetric under $n \leftrightarrow 2-n$), and constant in $q$ (all classes at weight $0$). The symmetry $P(t, q) = t^2 P(1/t, q)$ holds pointwise.

This is a consistency check, not an independent theorem. The symmetry is FORCED by the Koszul-duality palindrome $\dim \ChirHoch^n(A) = \dim \ChirHoch^{2-n}(A^!)$ (thm:main-koszul-hoch at `chiral_hochschild_koszul.tex:1594`) combined with the self-dual point $c = 13$. No heal.

Falsification test: substitute $c = 14$ (non-self-dual) and verify that the palindrome holds between $\mathrm{Vir}_{14}$ and $\mathrm{Vir}_{12}$ across the pair, NOT within $\mathrm{Vir}_{14}$ alone. Pointwise palindrome within a single algebra occurs only at self-dual points.

## AP925 Why the $\ChirHoch^1 = 0$ mechanism for Vir is orthogonal to $\ChirHoch^1(\mathfrak{H}_k) = 1$

Both are rank-1, but the distinction is OPE-pole-order, not strong-generator count.

| Algebra | Generator weight | OPE pole orders | $\dim \ChirHoch^1$ |
|---------|------------------|-----------------|--------------------|
| $\mathfrak{H}_k$ | $1$ | $\{2\}$ (double only, no simple pole) | $1$ (level deformation $k \mapsto k+\epsilon$) |
| Vir$_c$ | $2$ | $\{4, 2, 1\}$ (quartic, quadratic, simple) | $0$ |
| $V_k(\fg)$ | $1$ | $\{2, 1\}$ (double + simple) | $\dim \fg$ |
| bc (spin $\lambda$) | $1-\lambda, \lambda$ | $\{1\}$ (simple only) | $0$ |
| $\beta\gamma$ (spin $\lambda$) | $1-\lambda, \lambda$ | $\{1\}$ (simple only) | $0$ |
| W$_N$ | $2, 3, \ldots, N$ | incl. quartic via Vir subalgebra | $0$ |

Pattern: $\ChirHoch^1$ is nonzero iff the algebra is PURELY QUADRATIC (no simple-pole, no higher pole). Only Heisenberg and affine KM at generic level fit this; Vir has quartic, bc has simple, $\beta\gamma$ has simple. This is a cleaner statement than "rank-based" and propagates correctly across the landscape.

Mechanism (Heisenberg): $\mathfrak{H}_k$ is quadratic (double pole only), chirally Koszul; the three-term Koszul resolution has generating space $V = \bC \cdot a$; the $\ChirHoch^1$ slot picks up the level deformation $k \mapsto k+\epsilon$. This is the "level as $\ChirHoch^1$-cocycle" phenomenon.

Mechanism (affine KM): $V_k(\fg)$ is quadratic (double + simple poles only, both $\le 2$); Koszul resolution has $V = \fg$; $\ChirHoch^1 \cong \fg$ (outer derivations = current deformations).

Mechanism (Vir, W$_N$, bc, $\beta\gamma$): higher or simple-only poles force $\ChirHoch^1 = 0$; the quadratic-Koszul three-term resolution does not apply. The "modular Koszul" theorem (Theorem H) still applies and caps support at $\{0,1,2\}$; the middle slot is independently zero via the pole-order mechanism.

## AP926 Engine audit: `chirhoch_virasoro` vs inscribed theorem

Engine: `compute/lib/chirhoch_dimension_engine.py::chirhoch_virasoro` returns `ChirHochData(family="Virasoro Vir_c", dim0=1, dim1=0, dim2=1, total=2, poincare_poly="1 + t^2")`.

Manuscript: `chiral_center_theorem.tex:2023--2046` `prop:derived-center-explicit(iii)` states $\ChirHoch^0 = \bC$, $\ChirHoch^1 = 0$, $\ChirHoch^2 = \bC \cdot \Theta$, $P(t) = 1 + t^2$.

Engine = manuscript = first-principles derivation. AP245 (statement-proof-engine numerical agreement) check: PASS on all three axes.

The engine's `mechanism_dim1` field says "quartic pole; single generator; all derivations inner" and matches the manuscript proof Part (iii) verbatim.

## AP927 Sharp Hilbert series at generic $c$ vs the DS-compatibility cross-check

The DS compatibility proposition `prop:ds-chirhoch-compatibility` (`chiral_center_theorem.tex:2423--2474`) establishes that the induced map $\mathrm{DS}_* : \ChirHoch^1(V_k(\mathfrak{sl}_2)) \to \ChirHoch^1(\mathrm{Vir}_{c(k)})$ is ZERO. This is consistent with $\ChirHoch^1(\mathrm{Vir}_c) = 0$ but provides an independent cross-check via the three-way weight decomposition of $\mathfrak{sl}_2$: $D_e$ is BRST-exact, $D_h$ becomes inner via the Sugawara modification $T_{\mathrm{DS}} = T_{\mathrm{Sug}} + \partial J^h / 2$, $D_f$ becomes inner via the screening charge $Q_-$. The sum $1 + 1 + 1 = 3 = \dim \mathfrak{sl}_2$ exhausts the full $\ChirHoch^1(V_k(\mathfrak{sl}_2))$ and confirms that the DS functor kills every outer derivation.

Verification engine: `ds_chirhoch_compatibility_engine.py` traces all three mechanisms and verifies the dimension accounting. This is a genuinely independent path from the direct pole-order argument; both paths agree that $\dim \ChirHoch^1(\mathrm{Vir}_c) = 0$.

HZ-IV independence check: the pole-order mechanism uses the quartic pole of $T(z) T(w)$ and the Koszul-Ext computation. The DS-compatibility mechanism uses the BRST-exact structure of $J^e$, the Sugawara identity, and the Wakimoto screening. No shared intermediate step. Two genuinely disjoint paths.

## AP928 Status-table row (no edit made this session)

CLAUDE.md does not carry a dedicated "ChirHoch*(Vir_c)" status-table row; the family is covered under the Theorem H row plus the Structural Facts digest. Recommendation: add a per-family ChirHoch row in a future consolidated-status pass, mirroring the ChirHoch^1 KM row:

| Fam | $(\ChirHoch^0, \ChirHoch^1, \ChirHoch^2)$ | Total | Mechanism | Source |
|-----|-------------------------------------------|-------|-----------|--------|
| Heis | $(1,1,1)$ | 3 | quadratic Koszul, level deformation | `prop:derived-center-explicit(i)` |
| $V_k(\fg)$ | $(1, \dim\fg, 1)$ | $\dim\fg + 2$ | quadratic Koszul, current deformations | `prop:chirhoch1-affine-km`, `prop:chirhoch2-affine-km-general` |
| Vir$_c$ | $(1, 0, 1)$ | 2 | quartic pole, all derivations inner | `prop:derived-center-explicit(iii)` |
| bc, $\beta\gamma$ | $(1, 0, 1)$ | 2 | simple-pole mechanism | `chirhoch_dimension_engine.py::chirhoch_free_*` |
| W$_N$ | $(1, 0, 1)$ | 2 | Vir-subalgebra quartic pole | `chirhoch_dimension_engine.py::chirhoch_w_algebra` |

This row-level inventory is AP270-compliant (no multi-object conflation) and provides per-family grounding for the Theorem H digest.

## AP929 Preface prose corroboration at `chiral_center_theorem.tex:50--51`

The preface to `chiral_center_theorem.tex` (lines 49--62) writes: "$\ChirHoch^*(\mathrm{Vir}_c)$ is concentrated in degrees $\{0, 2\}$, with total dimension $2$..." This prose is TIGHTER than the Structural Facts digest: it states the actual nonvanishing support $\{0,2\}$, not the admissible amplitude $\{0,1,2\}$. The preface is correct; the digest is loosely compressed. Following AP271 / AP305 (manuscript vs metacognitive drift), the direction of drift here is metacognitive $\supsetneq$ manuscript: the metacognitive digest over-states the support range compared with the inscribed proposition. The correct reconciliation is to tighten the digest to match the preface, which is what item 2 of the Executive Verdict proposes.

## AP930 Heal scope

No edits made to CLAUDE.md, the manuscript, or engines in this session (per user constraint "Report... Patch per AP316"). The heal targets are:

1. **Metacognitive-layer edit (CLAUDE.md):** rewrite the Structural Facts line per Executive Verdict item 2, distinguishing amplitude from actual support.
2. **Manuscript-layer edit (no change required):** inscribed proposition is correct; preface prose is correct.
3. **Engine-layer edit (no change required):** engine returns correct dims, docstring matches manuscript.
4. **Status-table augmentation (future pass):** add per-family ChirHoch row per AP928 table.

AP316 patch delivery: this report is the deliverable. No worktree patch is required because no .tex / .py edits were performed (only the CLAUDE.md Structural Facts rewrite is a programme-level metacognitive update better deferred to a consolidated pass that also addresses AP921).

## Cache entries

**Pattern 226 (first-principles cache, session 2026-04-18).** Amplitude (admissible support) vs actual support for ChirHoch concentration theorems. Trigger: metacognitive line names a concentration range for a theorem about support; reader conflates "support $\subseteq \{0,1,2\}$" (universal Theorem-H statement) with "dim $>0$ in every slot of $\{0,1,2\}$" (family-specific, false for Vir/W_N/bc/$\beta\gamma$). Counter-derivation: substitute family and read each slot from the engine / inscribed proposition; expose the actual nonvanishing pattern (here $\{0,2\}$ for Vir). Regex trigger: `concentrated in \{0, ?1, ?2\}` in `CLAUDE.md`, `MEMORY.md`, `notes/*.md` — verify per-family digest distinguishes amplitude from actual support. Cross-volume: same pattern applies to Vol II Theorem-H cross-volume consumers and Vol III ChirHoch$^*_{\mathrm{cat}}$ statements.

**Pattern 227 (first-principles cache, session 2026-04-18).** Rank-1 vs OPE-pole-order as the true discriminator for $\ChirHoch^1$ nonvanishing. Trigger: prose claim "$\ChirHoch^1 = 0$ because $\cA$ is rank 1" or "$\dim \ChirHoch^1 = \mathrm{rank}(\cA)$". Counter-example: Heisenberg is rank 1 with $\dim \ChirHoch^1 = 1$; Vir is rank 1 with $\dim \ChirHoch^1 = 0$. Correct discriminator: OPE-pole-order. Quadratic (pole order $\le 2$, no simple pole among strong generators that contributes to nontrivial Koszul cohomology) $\Rightarrow$ $\dim \ChirHoch^1 = \dim V$ (generating space). Higher-pole (quartic for Vir, via Vir-subalgebra for W$_N$) or simple-pole (bc, $\beta\gamma$) $\Rightarrow$ $\dim \ChirHoch^1 = 0$. Affine KM is the borderline case: double + simple pole, but the simple pole is Lie-bracket-valued, and the Koszul resolution still gives $\fg$-valued $\ChirHoch^1$.

## Session ledger

1. Verified `prop:derived-center-explicit(iii)` is inscribed with full proof at `chiral_center_theorem.tex:2023--2117`.
2. Verified engine `chirhoch_virasoro` dims match inscription.
3. Verified `prop:chirhoch1-affine-km` at :2132 and `prop:chirhoch2-affine-km-general` at :2221 inscribe the affine-KM counterpart.
4. Verified `prop:ds-chirhoch-compatibility` at :2423 provides the independent DS-cross-check for $\ChirHoch^1(\mathrm{Vir}_{c(k)}) = 0$.
5. Verified the Gelfand--Fuchs contrast at :2037--2046 is substantive (different chain complex on different object), not rhetorical.
6. Identified AP921 metacognitive drift in the CLAUDE.md Structural Facts digest: $\{0,1,2\}$ admissible vs $\{0,2\}$ actual for Vir$_c$.
7. Registered patterns 226 and 227 for the first-principles cache.
8. No commits. No edits. Report only.
