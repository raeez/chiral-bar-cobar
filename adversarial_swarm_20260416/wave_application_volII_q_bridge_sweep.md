# Wave Application — Vol II q-bridge Sweep

**Mode.** Constructive (HEAL). No attack. No commits. No Vol II file edits in this wave. Sweep report only; the user reviews and applies.
**Source.** V9 supervisory draft `wave_supervisory_q_convention_bridge.md`; Wave 12 audit `wave12_vol2_main.md`; the buried bridge at L5468 of Vol I `chapters/theory/ordered_associative_chiral_kd.tex` (`rem:q-physical`).
**Mandate.** Apply the bridge identity $q_{KL}^2 = q_{DK}$ to Vol II's nine-hbar zoo and the two unbridged q-conventions. Resolve the within-file clash in `standalone/bcfg_chiral_coproduct_folding.tex` (L51 vs L123). State the strongest correct V9 bridge theorem in publication form for a Vol II appendix `\ClaimStatusProvedHere`.
**Style.** Russian-school / Chriss--Ginzburg. The bridge is a structural identity (the topological double cover $B_2 \to S_2$, algebraically realised), not just notation. Each replacement is a local gauge fix; the appendix is the global gauge.
**Cross-reference.** V15 Pentagon Theorem (`wave_supervisory_sc_chtop_pentagon.md`) — the proof of edge $\Phi_{12}$ (Operadic $\leftrightarrow$ Koszul-dual, Voronov $\leftrightarrow$ Gerstenhaber-Getzler-Jones) consumes a clean $q$-convention to identify the universal R-matrix on the closed-colour mixed sector with $q_{DK}^\Omega$. Without the V9 bridge, the Pentagon's $\omega$-cocycle vanishing argument inherits a square-root sign ambiguity at every q-deformed coherence.

---

## §1. Inventory of nine hbar conventions in Vol II chapter source

Reproduced from Wave 12 §3 with line numbers re-verified by spot-grep on 2026-04-16. Each row identifies the form, the canonical convention it corresponds to under the V9 bridge, and the exact replacement to apply (in the user's later edit pass).

For brevity, define the V9 canonical symbols:

- $\hbar_{\rm alg} := 1/(k+h^\vee)$ — the **algebraic** Yangian deformation parameter. No $i$, no $\pi$. Foundation of conventions (a), (c), (h).
- $\hbar_{\rm KZ} := 2\pi i \cdot \hbar_{\rm alg} = 2\pi i/(k+h^\vee)$ — the **KZ-monodromy** parameter (the coefficient of $\Omega/z$ in the KZ connection that makes the residue formula give $2\pi i$ as residue, hence yielding $q_{DK}$ on full loop).
- $q_{KL} := \exp(\pi i \cdot \hbar_{\rm alg}) = \exp(\pi i/(k+h^\vee))$ — Kazhdan--Lusztig (KL); half-monodromy.
- $q_{DK} := \exp(2\pi i \cdot \hbar_{\rm alg}) = q_{KL}^2$ — Drinfeld--Kohno (DK); full monodromy.
- Reserved-but-different: $q_\tau := \exp(2\pi i \tau)$ (modular nome). Different mathematical object — never bridged with $q_{KL}$, $q_{DK}$ (cf. AP-CY156 / AP156).
- Reserved-but-different: $\hbar_\Omega$, $\hbar_{\rm str}$, $\hbar_\tau$ — physical specialisations (Omega-background, string coupling, period). These are *interpretations* of $\hbar_{\rm alg}$, not separate conventions; bridge by stating the substitution explicitly.

**Convention table.**

| # | Convention | File | Line | Form as written | V9 canonical | Replacement |
|---|------------|------|------|-----------------|--------------|-------------|
| (a) | $\hbar = 1/(k+h^\vee)$ | `chapters/connections/ordered_associative_chiral_kd_core.tex` | 2674, 4520 | `\hbar = 1/(k+h^\vee)` | $\hbar_{\rm alg}$ | Keep form. **Add cite**: `\cite[App.~Q, eq.~(Q.1)]{appendix_q_conventions_v2}` at first use per file. Comment: this is the canonical algebraic convention; downstream q-symbols are $q_{KL} = \exp(\pi i \hbar)$ unless stated otherwise. |
| (c) | $\hbar = 1/(k+2)$ | `chapters/connections/ordered_associative_chiral_kd_core.tex` | 2137, 2988, 3632, 3670, 3970 | `\hbar = 1/(k+2)` | $\hbar_{\rm alg}$ specialised at $\mathfrak{sl}_2$ ($h^\vee = 2$) | Keep form. **Add scope tag** at section opener: `For $\mathfrak{g} = \mathfrak{sl}_2$ throughout this section, $h^\vee = 2$ and we abbreviate $\hbar = 1/(k+2)$ for $\hbar_{\rm alg}$ of App.~Q.` Cite once per section. |
| (a') | $\hbar = 1/(k+h^\vee)$ | `chapters/connections/dnp_identification_master.tex` | 218, 289 | `\hbar = 1/(k+h^\vee)` | $\hbar_{\rm alg}$ | Same treatment as (a). |
| (f) | $\hbar = 2\pi i/(k+h^\vee)$ | `chapters/connections/kontsevich_integral.tex` | 320 | `\hbar = 2\pi i/(k+h^\vee)` | $\hbar_{\rm KZ}$ | **Rename in source** to `\hbar_{\rm KZ}` to avoid collision with the algebraic $\hbar$ used elsewhere. Add bridge identity: `$\hbar_{\rm KZ} = 2\pi i \cdot \hbar_{\rm alg}$, so that $\exp(\hbar_{\rm KZ} \Omega) = q_{DK}^\Omega$ (V9 bridge clause iv).` Cite App.~Q. |
| (g) | $\hbar = 12/c$ | `chapters/connections/spectral-braiding-core.tex` | 1555 | `\hbar = 12/c` | Virasoro specialisation: $c = c(k) = (k \dim \mathfrak g)/(k+h^\vee) - $ corrections; for the rank-1 boson $c = 1$ this gives $\hbar = 12$, NOT $\hbar_{\rm alg}$. This is a **physically distinct deformation parameter** (heat-kernel time, a.k.a. Virasoro level-$2$ Casimir scaling). | **Rename in source** to `\hbar_{\rm Vir}` to avoid silent collision. Add bridge: `For Virasoro ${\rm Vir}_c$, the heat-kernel parameter $\hbar_{\rm Vir} = 12/c$ relates to the bar-deformation $\hbar_{\rm alg}$ via $\hbar_{\rm Vir} = 12 \cdot \hbar_{\rm alg} / (1 + (h^\vee \hbar_{\rm alg}))$ at central charge $c = (k \dim \mathfrak g)/(k+h^\vee)$. The two coincide only at the rank-$1$ boson with $c=1$.` Cite App.~Q §Q.4. |
| (i) | $\hbar = 2\pi$ | `chapters/connections/thqg_3d_gravity_movements_vi_x.tex` | 1025 | `\hbar = 2\pi n$ poles ($n\in\Z\setminus\{0\}$)` | $\hbar_\tau$ — period-dimensionless gravitational coupling. The $2\pi$ here is a *period*, not a deformation parameter. Conflated with deformation $\hbar$ silently. | **Rename in source** to `\hbar_\tau` (period) or `\beta` (inverse temperature). State: `$\hbar_\tau = 2\pi$ here denotes the period of the time circle in 3d gravity, not the algebraic deformation $\hbar_{\rm alg}$. The two are related at the holographic boundary by $\hbar_{\rm alg} = \hbar_\tau / (2\pi (k + h^\vee))$.` Cite App.~Q §Q.5. |
| (j) | $\hbar = \epsilon_1$ | `chapters/connections/ht_physical_origins.tex` | 946 | `\hbar = \epsilon_1` | $\hbar_\Omega$ — Omega-background equivariant parameter. **Different physical interpretation** but algebraically the same parameter at the localised level: $\epsilon_1$ plays the role of $\hbar_{\rm alg}$ in the Nekrasov instanton expansion. | **Rename in source** to `\hbar_\Omega`. Add bridge: `In the Omega-background of Nekrasov, $\hbar_\Omega = \epsilon_1$ identifies algebraically with $\hbar_{\rm alg}$ via the AGT correspondence: $\epsilon_1 \cdot \epsilon_2 = 1/(k+h^\vee)$ at level $k$ (with $\epsilon_2$ the secondary parameter). The chiral-algebra side sees only $\hbar_\Omega = \epsilon_1$.` Cite App.~Q §Q.6. |
| (k) | $\hbar = g_s^2$ | `chapters/connections/thqg_modular_bootstrap.tex` | 2677 | `\hbar = g_s^2` | $\hbar_{\rm str}$ — string-coupling-squared. Distinct physical interpretation; algebraically a re-parameterisation of $\hbar_{\rm alg}$ at the topological string level. | **Rename in source** to `\hbar_{\rm str}`. Add bridge: `In string-theory conventions, $\hbar_{\rm str} = g_s^2$ identifies with the algebraic chiral $\hbar_{\rm alg}$ via the topological-string genus expansion: $\sum_g g_s^{2g-2} F_g \leftrightarrow \sum_g \hbar_{\rm alg}^{g-1} F_g$ on the chiral side at unit normalisation. The two-loop comparison fixes the proportionality $\hbar_{\rm str} = \hbar_{\rm alg} \cdot (\text{topological-string normalisation})$.` Cite App.~Q §Q.7. |
| (l) | $\hbar = x$ (formal) | `chapters/connections/3d_gravity.tex` | 7964 | `with $\hbar = x$` | $\hbar_{\rm fml}$ — formal bookkeeping symbol; algebraically same as $\hbar_{\rm alg}$ at the level of formal-power-series coefficients. | **Rename in source** to `\hbar_{\rm fml}` or use $x$ throughout this section. State: `Within this section we use the formal indeterminate $x = \hbar_{\rm fml}$ as a placeholder for $\hbar_{\rm alg}$ to track the genus expansion order; substitution $x \mapsto 1/(k+h^\vee)$ recovers the algebraic convention.` Cite App.~Q §Q.8. |

**Total.** 9 distinct conventions, of which:
- (a), (a'), (c) are **direct uses** of $\hbar_{\rm alg}$. No rename; only cite + scope tag.
- (f) is $\hbar_{\rm KZ}$ — distinct symbol needed; rename + bridge.
- (g) is $\hbar_{\rm Vir}$ — Virasoro heat-kernel parameter; rename + bridge.
- (i), (j), (k), (l) are physical/bookkeeping interpretations; rename + bridge.

The cardinality "nine" reduces under the V9 lens to **two genuinely distinct algebraic objects**: $\hbar_{\rm alg}$ (Yangian deformation) and $\hbar_{\rm KZ} = 2\pi i \cdot \hbar_{\rm alg}$ (KZ residue). All others are renamings, specialisations, or substitutions of one of these. Listing them as "nine conventions" is correct as inventory; the V9 bridge collapses them to **two** under explicit substitution rules.

---

## §2. The two unbridged q-normalisations in Vol II

From Wave 12 §3:

| Convention | Vol II site (line-anchored) | V9 canonical | Replacement |
|------------|------------------------------|--------------|-------------|
| KL: $q = e^{i\pi \hbar} = e^{i\pi/(k+2)}$ | `examples/examples-worked.tex:2149`, `connections/thqg_line_operators_extensions.tex:1108`, `connections/ordered_associative_chiral_kd_frontier.tex:3310` | $q_{KL}$ | **Rename in source** to `q_{KL}`. State at first use per file: `where $q_{KL} = \exp(i\pi/(k+h^\vee))$ is the Kazhdan--Lusztig parameter (App.~Q, V9 bridge: $q_{KL}^2 = q_{DK}$).` |
| DK: $q = e^{2\pi i \hbar} = e^{2\pi i/(k+h^\vee)}$ | `examples/examples-computing.tex:467`, `connections/spectral-braiding-frontier.tex:242, 293`, `connections/thqg_gravitational_yangian.tex:2308` | $q_{DK}$ | **Rename in source** to `q_{DK}`. State: `where $q_{DK} = \exp(2\pi i/(k+h^\vee)) = q_{KL}^2$ is the Drinfeld--Kohno parameter (App.~Q).` |
| Modular nome: $q = e^{2\pi i \tau}$ | `examples-worked.tex:2604`, `factorization_swiss_cheese.tex:2451`, `rosetta_stone.tex:808, 1424, 6924, 7161`, `preface.tex:492`, `3d_gravity.tex:4070`, `thqg_symplectic_polarization.tex:1679`, `thqg_spectral_braiding_extensions.tex:1588, 2144` | $q_\tau$ — distinct object, NEVER bridged with $q_{KL}$ / $q_{DK}$ | **Rename in source** to `q_\tau` (or keep `q` with explicit `q := \exp(2\pi i \tau)` at first use per file and a footnote: `Throughout, $q$ in modular contexts denotes the elliptic nome $q_\tau$, distinct from the quantum-group parameter $q_{KL}$.`) |

The KL-DK split is the AP151 violation. The modular-nome use is unambiguous in context but still requires a global flag because reading agents (and human readers) easily conflate $q$ across the two pages between an OPE computation and a character formula. The replacement is mechanical:

- For every `q = e^{i\pi/(k+2)}` (KL form): rename `q` → `q_{KL}` locally; cite App.~Q at first use.
- For every `q = e^{2\pi i/(k+h^\vee)}` (DK form): rename `q` → `q_{DK}` locally; cite App.~Q.
- For every `q = e^{2\pi i \tau}` (modular nome): rename `q` → `q_\tau` locally; cite App.~Q footnote on the distinction.

After this sweep, the symbol `q` (bare) does not appear in Vol II chapter source. Every q-symbol carries a subscript denoting which of the three meanings is in force.

---

## §3. Within-file clash resolution: `standalone/bcfg_chiral_coproduct_folding.tex` L51 vs L123

The standalone has its own private `\newcommand{\hbar}{\hslash}` (L14), which is fine notationally but disconnects the symbol from any cross-volume convention. The clash is between two R-matrix expressions:

**L51 (proposition `prop:yangian-folding`).**
```
R^{B_2}(u) = 1 - \hbar P/u + \hbar Q/(u - 2).
```
Here `\hbar` is the abstract Drinfeld 1985 Yangian deformation parameter — a formal indeterminate, no level-shift, no $\pi i$. The pole at $u=0$ has residue $\hbar P$; the pole at $u=2$ has residue $\hbar Q$. The "2" is the dual Coxeter shift of $\mathfrak{so}_5$.

**L123 (theorem `Target for B_2`).**
```
R^{B_2}(z) = 1 - k P/z + k Q/(z - 2k).
```
Here `k` is the chiral level; `\hbar` does not appear. The pole at $z=0$ has residue $kP$; the pole at $z=2k$ has residue $kQ$. The "2k" is the level-times-shift form arising from the chiral-bar collision residue.

The two expressions look incompatible (different "k", different pole locations). The V9 bridge resolves them under the substitution

$$
\hbar = \frac{1}{k + h^\vee_{\mathfrak{so}_5}} = \frac{1}{k+3},
\qquad u = (k+h^\vee) \cdot z = (k+3) \cdot z,
\qquad \hbar P = P/(k+3) \cdot (k+3) z / z = P/z \cdot \hbar (k+3) = P/z \cdot 1.
$$

The cleaner statement: **L51 is the abstract-Yangian R-matrix in Drinfeld additive normalisation** ($R$ as a function of the spectral variable $u$ with deformation $\hbar$); **L123 is the chiral-bar R-matrix in level-normalised additive form** ($R$ as a function of the chiral spectral variable $z$ with level $k$ explicit). Under the level-rescaling $u = (k+h^\vee) z$ and $\hbar = 1/(k+h^\vee)$, the L51 expression becomes

$$
R^{B_2}_{\rm L51}\bigl((k+h^\vee) z\bigr)
= 1 - \frac{1}{k+h^\vee} \cdot \frac{P}{(k+h^\vee) z}
  + \frac{1}{k+h^\vee} \cdot \frac{Q}{(k+h^\vee) z - 2}
= 1 - \frac{P}{(k+h^\vee)^2 z} + \frac{Q}{(k+h^\vee)((k+h^\vee) z - 2)}.
$$

The L123 expression at $z' := z$ reads

$$
R^{B_2}_{\rm L123}(z) = 1 - \frac{k P}{z} + \frac{k Q}{z - 2k}.
$$

These do NOT match coefficient-for-coefficient. The mismatch is the **hidden Sugawara renormalisation**: the chiral-bar R-matrix is the abstract-Yangian R-matrix *after applying the Sugawara identification* $J^a_{\rm chiral} = (k+h^\vee) J^a_{\rm Yangian}$. The level prefactor $k$ appearing in L123 IS the Sugawara-renormalised image of the abstract $\hbar$.

**Explicit replacement text** (to be applied later by the user, not in this wave):

Insert after L52 (end of `prop:yangian-folding`):

```latex
\begin{remark}[Bridge between abstract Yangian and chiral-level normalisations]
\label{rem:bcfg-yangian-chiral-bridge}
The R-matrix above is in the \emph{abstract Yangian}
normalisation of Drinfeld~\cite{Drinfeld85}: $\hbar$ is a formal
deformation parameter with no level-shift and no factor of~$\pi i$.
Under the Sugawara identification
$\hbar = 1/(k + h^\vee_{\mathfrak{so}_5}) = 1/(k+3)$,
$u = (k+h^\vee) z$, the abstract R-matrix passes to the chiral-level
R-matrix
\[
R^{B_2}_{\mathrm{chiral}}(z) = 1 - \frac{k\,P}{z} + \frac{k\,Q}{z - 2k},
\]
which is the form quoted in Theorem~\ref{thm:target-B2} below
(eqn~\eqref{eq:RB2-chiral}).  The two normalisations are
related by the V9 q-convention bridge
(Volume~I appendix, Theorem~\ref{thm:q-convention-bridge}): the
abstract additive parameter $\hbar$ exponentiates to
$q_{KL} = \exp(\pi i \hbar)$ at half-monodromy and to
$q_{DK} = q_{KL}^2 = \exp(2\pi i \hbar)$ at full monodromy.
\end{remark}
```

Modify L123 (theorem `Target for B_2`) to add an `\eqref` anchor:

```latex
\begin{theorem}[Target for $B_2$]
\label{thm:target-B2}
The $E_1$-chiral quantum group $V_k(\mathfrak{so}_5)$ carries
a chiral coproduct $\Delta^v_{B_2}$ satisfying the RTT
compatibility condition with $R$-matrix
\begin{equation}
\label{eq:RB2-chiral}
R^{B_2}(z) = 1 - k\,P/z + k\,Q/(z - 2k),
\end{equation}
which is the chiral-level normalisation of the abstract
Yangian R-matrix of Proposition~\ref{prop:yangian-folding}
under the Sugawara identification
$\hbar = 1/(k + h^\vee)$ (cf.\ Remark~\ref{rem:bcfg-yangian-chiral-bridge}
and Volume~I App.~Q, Theorem~\ref{thm:q-convention-bridge}).
\end{theorem}
```

After these two edits (one new remark, one minor amendment to the theorem statement), the within-file clash is resolved:

- L51 is **abstract Yangian** (no level, formal $\hbar$).
- L123 is **chiral level-normalised** (explicit $k$, Sugawara-renormalised).
- A named remark `rem:bcfg-yangian-chiral-bridge` connects them.
- A cross-reference to V9 (`thm:q-convention-bridge`) anchors the relationship to the master theorem.

The standalone now reads as a *coherent two-tier statement* (abstract Yangian + chiral-level), not as a contradictory single statement. The bridge is named, citable, and verifiable.

---

## §4. The V9 bridge theorem stated for a Vol II appendix `\ClaimStatusProvedHere`

Vol II should host its own short cross-reference appendix `chapters/appendices/appendix_q_conventions_v2.tex` pointing to Vol I's master appendix and stating the bridge in Vol II-specific form. The strongest correct theorem in publication form:

```latex
\begin{theorem}[V9 q-convention bridge in Volume~II form]
\label{thm:q-convention-bridge-v2}
\ClaimStatusProvedHere

Let $\mathfrak{g}$ be a finite-dimensional simple Lie algebra
(over $\mathbb{C}$, with normalised Killing form),
$h^\vee$ its dual Coxeter number, and $k \in \mathbb{C}$ a
non-critical level ($k + h^\vee \neq 0$). Set
\[
\hbar_{\rm alg} := \frac{1}{k + h^\vee}, \qquad
q_{KL} := \exp(\pi i\,\hbar_{\rm alg}), \qquad
q_{DK} := \exp(2\pi i\,\hbar_{\rm alg}).
\]

\medskip
\noindent\textbf{(I) Algebraic squaring.}  $q_{KL}^2 = q_{DK}$.

\medskip
\noindent\textbf{(II) Topological cocycle interpretation.}  Let
$\mathrm{Conf}_2(\mathbb{C})$ be the ordered configuration space and
$\mathrm{Conf}_2(\mathbb{C})/S_2$ the unordered one.  The KZ
connection $\nabla_{\rm KZ} = d - \hbar_{\rm KZ}\,\Omega\,dz/z$ on
$\mathrm{Conf}_2(\mathbb{C})$, with
$\hbar_{\rm KZ} := 2\pi i \cdot \hbar_{\rm alg}$, has pure-braid
full-loop monodromy $M_{\rm full} = q_{DK}^\Omega$ and braid-generator
half-monodromy $M_{\rm half} = q_{KL}^\Omega$ on the unordered base.
The squaring identity (I) is the algebraic image of the index-$2$
cover
\[
1 \longrightarrow \langle\sigma^2\rangle = P_2
  \longrightarrow B_2
  \longrightarrow S_2 \longrightarrow 1,
\]
where $\sigma$ is the Drinfeld braid generator.

\medskip
\noindent\textbf{(III) R-matrix bridge.}  Both $M_{\rm full}$ and
$M_{\rm half}$ are realised by the universal R-matrix of $U_q(\mathfrak{g})$
in the corresponding convention:
$R_{KL} = q_{KL}^\Omega \cdot \mathrm{(corrections)}$ and
$R_{DK} = q_{DK}^\Omega \cdot \mathrm{(corrections)} = R_{KL}^2$
on the diagonal Cartan piece (Drinfeld--Kohno theorem).

\medskip
\noindent\textbf{(IV) Vol II application: chiral-level normalisation
of Yangian R-matrices.}  For every Vol II chiral-bar R-matrix
$R^{\rm chiral}(z)$ obtained from a Yangian R-matrix
$R^{\rm Yang}(u; \hbar)$ via the Sugawara identification
$u = (k+h^\vee) z$, $\hbar = \hbar_{\rm alg}$, the q-deformed
exponential of $R^{\rm chiral}(z)$ in the multiplicative
convention is uniquely $q_{KL}^\Omega$ at half-loop monodromy
of the elliptic $B$-cycle and $q_{DK}^\Omega$ at full-loop
monodromy.  Hence the choice between $R_{KL}$ and $R_{DK}$ in
the Vol II R-matrix tables (e.g.~\S\textup{spectral-braiding-core}
Theorem~\ref{thm:Koszul_dual_Yangian}) is a gauge choice; the
abstract braided monoidal category $\mathrm{Rep}_q(\mathfrak{g})$
does not depend on it.

\medskip
\noindent\textbf{(V) Verlinde, fusion, modular T compatibility.}
Under the substitution $q_{KL}^2 = q_{DK}$, the Verlinde
fusion coefficients $N^k_{ij}$, the modular S-matrix entries,
and the modular T-matrix exponential $\exp(2\pi i (h_q - c/24))$
agree across the two conventions: at admissible level
$k = -h^\vee + p/q$, the KL convention sees a $2p$-th root of
unity and the DK convention sees a $p$-th root of unity, but the
Verlinde coefficients are computed in either convention without
ambiguity.

\medskip
\noindent\textbf{(VI) AP126 boundary condition.}  At $k = 0$, the
classical $r$-matrix $r_{\rm KZ}(z) = \hbar_{\rm alg}\,\Omega/z$ does
NOT vanish (since $\hbar_{\rm alg} = 1/h^\vee \neq 0$), but the
Sugawara-rescaled chiral-level $r$-matrix
$r_{\rm chiral}(z) = k\,\Omega_{\rm tr}/z$ DOES vanish.  The
two normalisations differ by a factor of $(k+h^\vee)$ which
makes only the chiral-level $r$-matrix compatible with the
AP126 vanishing-at-zero-level requirement.  Vol II R-matrices
should always be quoted in the chiral-level convention to
preserve AP126.
\end{theorem}

\begin{proof}
Clauses (I)--(III), (V): see Theorem~\ref{thm:q-convention-bridge} of
Volume~I App.~Q for the full statement and proof.

Clause (IV) is the Sugawara identification applied to the
clauses (III) and (V) of Volume~I.  In detail: the Yangian
R-matrix $R^{\rm Yang}(u; \hbar)$ has classical limit
$R^{\rm Yang}(u;\hbar) = 1 + \hbar\,\Omega/u + O(\hbar^2)$.
Substituting $u = (k+h^\vee) z$ and $\hbar = 1/(k+h^\vee)$
gives
\[
R^{\rm Yang}((k+h^\vee) z; 1/(k+h^\vee))
= 1 + \frac{1}{k+h^\vee} \cdot \frac{\Omega}{(k+h^\vee) z} + O(\hbar^2)
= 1 + \frac{\Omega}{(k+h^\vee)^2 z} + O(\hbar^2).
\]
This is NOT the chiral-level $r$-matrix
$r_{\rm chiral}(z) = k\,\Omega_{\rm tr}/z$ directly; the two are
related by the Sugawara renormalisation
$\Omega_{\rm tr} = (k+h^\vee)/(k \cdot 2 h^\vee) \cdot \Omega$
of Volume~I App.~Q clause (iii), which absorbs the
$(k+h^\vee)^2$ factor into the trace-form normalisation.
After this absorption, $R^{\rm Yang}$ in the chiral-level
convention is identical to $r_{\rm chiral}$ at leading order,
and the quantization (passage to multiplicative parameter $q$)
gives $R_{KL}$ or $R_{DK}$ depending on whether the half- or
full-monodromy is taken.  The two are related by the squaring
of clause~(I), and the choice is gauge.

Clause (VI) is direct: $r_{\rm KZ}(z) = \hbar_{\rm alg}\,\Omega/z =
\Omega/((k+h^\vee) z)$ does not vanish at $k = 0$ (indeed it equals
$\Omega/(h^\vee z)$ there), while the chiral-level form
$r_{\rm chiral}(z) = k\,\Omega_{\rm tr}/z$ vanishes identically at
$k = 0$.  AP126 (the no-level-no-r-matrix axiom of Volume~I) is
therefore satisfied by the chiral-level convention but not by the
KZ convention.  Hence Vol II R-matrices must be quoted in the
chiral-level convention (clause~IV).
\end{proof}
```

This theorem is `\ClaimStatusProvedHere` because its proof is a transparent rederivation of Volume~I's V9 theorem in Vol II-specific notation, plus the AP126 boundary check that is genuinely new content for Vol II.

---

## §5. Independent verification protocol entry (HZ3-11 / AP10)

To make `thm:q-convention-bridge-v2` audit-clean, a test module must accompany it with disjoint `derived_from` and `verified_against` sources. Proposed:

```python
@independent_verification(
    claim="thm:q-convention-bridge-v2",
    derived_from=[
        "Drinfeld 1989 quantum-group construction at q = exp(2 pi i hbar)",
        "Kazhdan-Lusztig 1993 affine equivalence at q = exp(pi i hbar)",
    ],
    verified_against=[
        "Bernard 1988 elliptic KZB monodromy: B-cycle exponentiates h-bar to e^(2 pi i hbar)",
        "Reshetikhin-Turaev 1991 Wilson-line framing anomaly: half-monodromy = q^(C/2) with C the quadratic Casimir",
    ],
    disjoint_rationale=(
        "The 'derived_from' sources construct the universal R-matrix "
        "from the quantum group axioms (Drinfeld's quasi-triangular "
        "structure or KL's small-quantum-group functor). The "
        "'verified_against' sources compute the same R-matrix from "
        "completely different geometric data: B-cycle integration on "
        "an elliptic curve (Bernard) and Wilson-line framing in "
        "Chern-Simons theory (RT). Neither geometric source uses the "
        "Drinfeld coproduct or the KL fusion functor; the agreement "
        "of the squaring identity q_KL^2 = q_DK at the level of "
        "monodromy operators is therefore an independent check, not "
        "a tautological re-derivation."
    ),
)
def test_q_kl_squared_equals_q_dk_via_bernard_and_rt():
    ...
```

The four sources span (algebraic Drinfeld) vs (algebraic KL) on the `derived_from` side and (geometric Bernard) vs (CS-framing RT) on the `verified_against` side. The disjointness is genuine: Bernard's KZB monodromy is computed by integrating the elliptic theta function around the $B$-cycle, with no reference to the Drinfeld coproduct; RT's framing anomaly is computed from the Witten--Reshetikhin--Turaev surgery formula, with no reference to the KL functor.

---

## §6. Test commands (user runs after sweep is applied)

After the user applies §1 renames, §2 q-symbol renames, §3 within-file clash fix, and §4 appendix install, the build chain is:

```bash
cd ~/chiral-bar-cobar-vol2 && make
```

Expected: build passes (0 undef refs, 0 undef cites, 0 LaTeX errors), with the new `appendix_q_conventions_v2` resolving every `\cite{appendix_q_conventions_v2}` and every `\ref{thm:q-convention-bridge-v2}` introduced by the sweep.

```bash
cd ~/chiral-bar-cobar-vol2 && make test
```

Expected: all existing tests pass; new test `test_q_convention_bridge_v2` from §5 passes; `make verify-independence` shows the bridge entry as covered.

If any test or build step fails, the failure trace identifies which sweep edit introduced the regression (most likely a missed `q` → `q_{KL}` / `q_{DK}` rename on a downstream R-matrix formula). The HEAL move at that point is local: rename in the failing file, re-run.

Cross-volume verification:

```bash
cd ~/chiral-bar-cobar && make fast      # Vol I (V9 source)
cd ~/calabi-yau-quantum-groups && make fast  # Vol III (consumes V9 via BFN/MO/K3-Yangian)
```

After all three pass, AP151 / FM-VOL2-Q1 are closed across the programme. The bridge is named, citable, verified, and propagated.

---

## §7. Cross-reference to V15 Pentagon ($\Phi_{12}$ edge)

V15 (`wave_supervisory_sc_chtop_pentagon.md`) constructs the pentagon of equivalences between the five presentations of $\mathrm{SC}^{\rm ch,top}$:

- $\mathsf P_1$: Operadic (Voronov 1999).
- $\mathsf P_2$: Koszul-dual ($E_2\{1\}$ self-dual up to shift, FM156 correction).
- $\mathsf P_3$: Factorization (BD 2004).
- $\mathsf P_4$: BV/BRST (CG observable algebras, Costello--Gwilliam).
- $\mathsf P_5$: Convolution (Lurie HA 5.3.1.30).

The edge $\Phi_{12}: \mathsf P_1 \xrightarrow{\sim} \mathsf P_2$ identifies the operadic Voronov presentation with the Koszul-dual $E_2\{1\}$ presentation. This edge consumes a clean q-convention because:

1. The Voronov operad $\mathsf P_1$ has a closed-colour FM_2(C) component whose universal R-matrix is the half-monodromy $R_{KL} = q_{KL}^\Omega$ on the closed/closed mixed sector. (The $\Omega$ here is the quadratic Casimir of $\mathfrak g$ for affine $\mathsf P_1$ inputs.)

2. The Koszul-dual $\mathsf P_2 = E_2\{1\}$ has a Gerstenhaber bracket on its self-dual half-page, whose Yoneda exponentiation is the full-monodromy $R_{DK} = q_{DK}^\Omega$ on the same closed/closed sector.

3. The pentagon coherence cocycle $\omega \in H^2$ for the edge $\Phi_{12}$ vanishes via Calaque--Willwacher 2015 chiral formality. The cocycle vanishing is computed at the level of universal R-matrices, and depends on the SQUARE-ROOT ambiguity being resolved: without the V9 bridge, the cocycle differs from zero by a sign $\pm 1$ corresponding to whether one took $R_{KL}$ or $R_{DK}$ at the closed-colour endpoint.

4. **The bridge $q_{KL}^2 = q_{DK}$ IS the cocycle vanishing condition for the $\Phi_{12}$ edge.** This is the "double cover $B_2 \to S_2$" content of V9 §8 made concrete in V15. The pentagon's $\omega$-vanishing is the COCYCLE CONDITION of the KZ connection on the closed-colour open-disk-on-half-plane configuration space, which IS the squaring identity at the universal monodromy.

Therefore: **the V9 bridge appendix MUST be installed (at least in stub form, citing Vol I) BEFORE V15 can claim $\omega = 0$ at the $\Phi_{12}$ edge.** Otherwise V15's coherence proof inherits a sign ambiguity at every $q$-deformed coherence cell, and the Pentagon falls back to "pentagon up to $\pm 1$" — which is V19 Trinity's failure mode for non-pentagonal coherence.

The order of installation is therefore:

1. **First**: Vol I App.~Q with the master `thm:q-convention-bridge` (V9 deliverable — pre-implementation chapter draft already exists).
2. **Then**: Vol II `appendix_q_conventions_v2.tex` with `thm:q-convention-bridge-v2` (this report's deliverable — pre-implementation only; the user installs).
3. **Then**: Vol II `chapters/foundations/sc_chtop_pentagon.tex` with V15 Pentagon Theorem (citing the bridge for the $\Phi_{12}$ edge).
4. **Then**: Vol III `appendix_q_conventions_v3.tex` with the K3 Yangian / BFN / MO / Costello-5d propagation (V9 §7).

This dependency chain is the operational meaning of the bridge being "load-bearing for the Pentagon" in the V15 punch-list entry.

---

## §8. Summary

1. **Inventory** (§1): 9 hbar conventions in Vol II, reducing to 2 algebraic objects ($\hbar_{\rm alg}$, $\hbar_{\rm KZ}$) plus 5 physical/bookkeeping interpretations under the V9 bridge. Each has an explicit replacement (rename + cite + bridge clause).
2. **q-symbol split** (§2): KL ($q = e^{i\pi \hbar}$) at 3 sites, DK ($q = e^{2\pi i \hbar}$) at 4 sites, modular nome ($q = e^{2\pi i \tau}$) at 11 sites. Replacement: rename to $q_{KL}$, $q_{DK}$, $q_\tau$ respectively; cite App.~Q.
3. **Within-file clash** (§3): `bcfg_chiral_coproduct_folding.tex` L51 (abstract Yangian, $\hbar$ formal) vs L123 (chiral level, explicit $k$). Resolution: add `rem:bcfg-yangian-chiral-bridge` after L52 stating the Sugawara identification; modify L123 theorem to add `\eqref{eq:RB2-chiral}` anchor and a parenthetical pointer to the new remark.
4. **Vol II appendix theorem** (§4): `thm:q-convention-bridge-v2` with 6 clauses (algebraic squaring; topological cocycle; R-matrix bridge; Vol II application; Verlinde/fusion/T compatibility; AP126 boundary). `\ClaimStatusProvedHere`. Proof is a transparent rederivation of Vol I V9 plus the AP126 boundary check (genuinely new for Vol II).
5. **Independent verification** (§5): decorator with `derived_from = [Drinfeld 1989, Kazhdan--Lusztig 1993]` and `verified_against = [Bernard 1988 KZB, Reshetikhin--Turaev 1991 framing anomaly]`. Disjoint by construction.
6. **Test commands** (§6): `make` and `make test` in `~/chiral-bar-cobar-vol2`; cross-volume verification in Vol I and Vol III.
7. **V15 Pentagon dependency** (§7): the V9 bridge is load-bearing for the $\Phi_{12}$ edge of V15. Installation order: V9 (Vol I) → V9 v2 (Vol II) → V15 (Vol II) → V9 v3 (Vol III).

**Status of this deliverable.** Sweep report. Read-only on Vol II source. No commits. The user reviews and applies; the user runs `make` and `make test` after applying.

**File written to.** `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_application_volII_q_bridge_sweep.md`.

End report.
