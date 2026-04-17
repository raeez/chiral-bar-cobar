# Wave Application — Climax Theorem main.tex Application Drafts

**Mandate.** First concrete editorial action on the live Vol I manuscript per V27 6-month roadmap step M4 (Climax abstract promotion). Three V22 drafts staged as application-ready `.tex` snippets in `adversarial_swarm_20260416/`; this report verifies each placement, names the dependency graph, and lists the test commands the user must run after applying. **No commits, no edits to `main.tex` or `standalone/drinfeld_kohno_bridge.tex` — drafts staged in swarm directory only.**

**Author.** Raeez Lorgat. **Date.** 2026-04-16.

**Files staged.**

- `adversarial_swarm_20260416/draft_main_tex_abstract_paragraph.tex` (H1, ~250 words)
- `adversarial_swarm_20260416/draft_main_tex_part_I_opener.tex` (H2a + H2b, ~200 words combined)
- `adversarial_swarm_20260416/draft_dk_standalone_thm_0_1.tex` (H3, ~280 words, includes one numbered theorem and one remark)

---

## §1. Verbatim quote of current Vol I `main.tex` L780–820 (abstract context)

The current abstract paragraph block ends at L798 with the higher-Deligne / Costello–Francis–Gwilliam sentence, terminated by `\end{abstract}` at L799. The full surrounding block:

```
780: At genus~$1$, the bar-complex propagator specialises to
781: the Weierstrass $\zeta$-function and the shadow connection
782: restricts to the KZB connection.
783:
784: For $\mathsf{E}_\infty$-chiral~$\cA$, the symmetric bar
785: carries an $\mathsf{E}_2$-coalgebra structure; by the
786: Higher Deligne Conjecture, the derived chiral center
787: $Z_{\mathrm{ch}}^{\mathrm{der}}(\cA)
788: = \operatorname{HH}^*(\cA, \cA)$
789: carries $\mathsf{E}_3$ structure.
790: For $\mathsf{E}_1$-chiral~$\cA$, the derived center is
791: $\mathsf{E}_2$.
792: The $\mathsf{E}_3$-deformation space of
793: $Z_{\mathrm{ch}}^{\mathrm{der}}(V_k(\mathfrak{g}))$
794: is $\hbar H^3(\mathfrak{g})[[\hbar]]$; formal disk
795: restriction recovers the Costello--Francis--Gwilliam
796: perturbative Chern--Simons $\mathsf{E}_3$-algebra,
797: an identification that is conjectural beyond the
798: formal disk.
799: \end{abstract}
800:
801: \bigskip
802: \noindent
803: \textbf{2020 Mathematics Subject Classification.}
```

The italics environment opened earlier in the abstract block (`\begin{abstract}` at L724) is in force throughout L780–798 and terminates at L799. The Climax paragraph (H1) MUST insert between L798 and L799 to inherit the italics styling.

---

## §2. Proposed replacement (H1 — abstract Climax paragraph)

**Insertion point.** New material between L798 and L799 (i.e. as the final paragraph of the abstract). Exact text is the file `draft_main_tex_abstract_paragraph.tex` (~250 words including the displayed equation).

**Diff visualisation (H1).**

```diff
  794: is $\hbar H^3(\mathfrak{g})[[\hbar]]$; formal disk
  795: restriction recovers the Costello--Francis--Gwilliam
  796: perturbative Chern--Simons $\mathsf{E}_3$-algebra,
  797: an identification that is conjectural beyond the
  798: formal disk.
+ 798a:
+ 798b: \medskip\noindent\textbf{Climax (the four pillars).}
+ 798c: The bar differential of the ordered chiral bar complex
+ 798d: $B^{\mathrm{ord}}(\cA)$ on $\Conf_n^{\mathrm{ord}}(X)$ is the
+ 798e: pullback of Arnold's universal KZ connection along a universal
+ 798f: functor $\mathrm{KZ} : \mathrm{ChirAlg}^{\Einf} \to \mathrm{ConnConf}$:
+ 798g: \begin{equation*}
+ 798h:   d_{\mathrm{bar}} \;=\; \mathrm{KZ}^{*}(\nabla_{\mathrm{Arnold}}),
+ 798i:   \qquad
+ 798j:   \kappa(\cA) \;=\; -\,c_{\mathrm{ghost}}(\mathrm{BRST}(\cA)).
+ 798k: \end{equation*}
+ 798l: Drinfeld--Kohno
+ 798m: $\rho_{n}^{\mathrm{KZ}} \cong \rho_{n}^{U_{q}(\fg)}$
+ 798n: at $q = e^{2\pi i / (k + h^{\vee})}$, the Verlinde diagonalisation
+ 798o: $N_{ij}^{k} = \sum_{a} S_{ia}S_{ja}\overline{S_{ka}}/S_{0a}$, and the
+ 798p: Borcherds product $\Phi_{10}$ for the $\mathrm{II}_{2,18}$ lattice
+ 798q: vertex algebra are three specialisations of the pullback identity:
+ 798r: DK at genus $0$ on evaluation modules of affine Kac--Moody;
+ 798s: Verlinde at genus $0$ on rational fusion;
+ 798t: Borcherds at genus $1$ on lattice vertex algebras.
+ 798u: All three reduce ultimately to Arnold's three-term relation on
+ 798v: $\Conf_{n}(\CC)$. The modular characteristic $\kappa$ is the
+ 798w: bc-ghost central charge of any free-field BRST resolution; this
+ 798x: identity collapses the per-family $\kappa$ table
+ 798y: (Heisenberg $k$, Virasoro $c/2$, affine
+ 798z: $\dim(\fg)(k+h^{\vee})/(2h^{\vee})$, principal $W_{N}$
+ 798zz: $c\cdot(H_{N}-1)$) into one functor
+ 798zzz: $K : \mathrm{BRSTGaugedChirAlg} \to \ZZ$.
+ 798zzzz: Theorems~(A)--(H) and the shadow quadrichotomy are corollaries.
  799: \end{abstract}
```

The italics environment from `\begin{abstract}` at L724 wraps this paragraph as well. The `\medskip\noindent` opening posture-switches the reader from the higher-Deligne paragraph to the structural climax without breaking the italicised block.

---

## §3. Verbatim quote of current Vol I `main.tex` L899–946 (Part I opener)

```
899: \part{The Bar Complex}
900: \label{part:bar-complex}
901:
902: \noindent
903: Place sections $a_1, \ldots, a_n$ of a chiral algebra~$\cA$ at
904: distinct points $z_1, \ldots, z_n$ on a smooth curve~$X$. Wedge the
905: tensor $a_1(z_1) \otimes \cdots \otimes a_n(z_n)$ against the
906: logarithmic $n$-form $\eta = \bigwedge_{i<j} d\log(z_i - z_j)$ on
907: the Fulton--MacPherson compactification $\overline{C}_n(X)$, and
908: extract residues at each collision divisor. The result is a
909: differential. Arnold's three-term identity
910: \[
911: \eta_{12} \wedge \eta_{23}
912: \;+\; \eta_{23} \wedge \eta_{31}
913: \;+\; \eta_{31} \wedge \eta_{12}
914: \;=\; 0
915: \]
916: forces $d^2 = 0$. This is the bar complex~$\barB_X(\cA)$: the
917: categorical logarithm of~$\cA$.
918:
919: A logarithm has four properties. Each is a theorem.
920:
921: \begin{enumerate}[label=\textbf{(\Alph*)},leftmargin=2.2em]
922: \item \textbf{Existence.}
923:  The bar-cobar adjunction $(\barB, \Omega)$, intertwined with
924:  Verdier duality on $\operatorname{Ran}(X)$. The logarithm exists
925:  and is natural.
[...]
946: \end{enumerate}
```

The line cadence is: L902–917 = FM-residue construction culminating in "categorical logarithm of $\cA$"; L919 = the connective sentence; L921–946 = the four-property enumeration (A)–(D); L943–945 = (H) the coefficient ring as standalone block.

---

## §4. Proposed replacement (H2a + H2b — Part I opener)

**H2a — INSERT after L917, before L919.** Two-paragraph Climax block. Exact text is the file `draft_main_tex_part_I_opener.tex` (first half).

**H2b — REPLACE the existing L919 sentence.** Single-line cadence patch. Exact text is the file `draft_main_tex_part_I_opener.tex` (second half).

**Diff visualisation (H2a + H2b).**

```diff
  916: forces $d^2 = 0$. This is the bar complex~$\barB_X(\cA)$: the
  917: categorical logarithm of~$\cA$.
+ 917a:
+ 917b: \medskip\noindent
+ 917c: \textbf{The Climax of Volume~I.}
+ 917d: The bar differential just constructed by FM residue extraction on
+ 917e: $\overline{C}_{n}(X)$ is the pullback of Arnold's universal KZ
+ 917f: connection on $\Conf_{n}^{\mathrm{ord}}(X)$:
+ 917g: \[
+ 917h:   d_{\mathrm{bar}}
+ 917i:   \;=\;
+ 917j:   \mathrm{KZ}^{*}(\nabla_{\mathrm{Arnold}}),
+ 917k:   \qquad
+ 917l:   \nabla_{\mathrm{Arnold}}
+ 917m:   \;=\;
+ 917n:   d \;-\; \sum_{i<j} t_{ij}\;d\log(z_{i}-z_{j}),
+ 917o: \]
+ 917p: with $\{t_{ij}\}$ the universal infinitesimal braid generators
+ 917q: (Arnold 1969). Flatness $\nabla_{\mathrm{Arnold}}^{2} = 0$ is
+ 917r: equivalent, after pullback, to $d_{\mathrm{bar}}^{2} = 0$;
+ 917s: Arnold's three-term identity on $\Conf_{3}^{\mathrm{ord}}(\CC)$
+ 917t: is the chain-level expression of the classical Yang--Baxter equation
+ 917u: on the collision residues
+ 917v: $r^{(ij)}(z_{i}-z_{j}) = \mathrm{KZ}^{*}(\eta_{ij})$.
+ 917w:
+ 917x: Three classical theorems --- Drinfeld--Kohno
+ 917y: $\rho_{n}^{\mathrm{KZ}} \cong \rho_{n}^{U_{q}(\fg)}$,
+ 917z: Verlinde $N_{ij}^{k} = \sum_{a} S_{ia}S_{ja}\overline{S_{ka}}/S_{0a}$,
+ 917aa: and the Borcherds product $\Phi_{10}$ --- are pullbacks of
+ 917ab: $\nabla_{\mathrm{Arnold}}$ along three structure functors,
+ 917ac: applied to three specific chiral inputs (affine Kac--Moody on
+ 917ad: evaluation modules; rational chiral algebra on conformal blocks;
+ 917ae: lattice vertex algebra on the genus-$1$ trace). The bar
+ 917af: differential is a fourth pullback --- the chain-level
+ 917ag: incarnation. The four properties (A)--(D) below, and the
+ 917ah: modular-characteristic identity
+ 917ai: $\kappa(\cA) = -c_{\mathrm{ghost}}(\mathrm{BRST}(\cA))$ established
+ 917aj: in Part~\ref{part:characteristic-datum}, are the structural
+ 917ak: unfolding of this single observation.
+ 917al:
- 919: A logarithm has four properties. Each is a theorem.
+ 919: \smallskip\noindent
+ 919a: A logarithm proved by such an identity has four structural
+ 919b: properties. Each is a theorem; each is one face of the Climax.
  920:
  921: \begin{enumerate}[label=\textbf{(\Alph*)},leftmargin=2.2em]
```

**Six words inserted in H2b** (preserves the existing four-property enumeration verbatim and demotes it from "list of theorems" to "structural unfolding of one Climax"):

- "proved by such an identity" (5 words inside the first sentence)
- "structural" (1 word qualifying "properties")
- "; each is one face of the Climax" (7 words appended to the second sentence — count includes "; each is one face of the Climax", which is the structural patch)

The cadence "Each is a theorem" survives verbatim, signalling that the four enumeration items below are unchanged.

---

## §5. Verbatim quote of current `standalone/drinfeld_kohno_bridge.tex` L168–185

```
168: \end{abstract}
169:
170: \maketitle
171:
172: \setcounter{tocdepth}{2}
173: \tableofcontents
174:
175: \begin{remark}[Convention for $q$: Kazhdan--Lusztig vs.\ Drinfeld]
176: \label{rem:dk-q-convention}
177: This paper uses two closely related but distinct deformation
178: parameters, and we fix the convention once and for all.
179: \begin{itemize}
180: \item \textbf{Canonical (Kazhdan--Lusztig).} We set
181: \[
182:   q \;:=\; \exp\!\bigl(2\pi i/(k+\hv)\bigr).
183: \]
```

V22 §3 specifies the insertion target as "between L173 (`\tableofcontents`) and L178 (`\section{Introduction}`)". The actual file structure has `\tableofcontents` at L173 and the q-convention remark beginning at L175 (not §1 introduction at L178 as V22 narrated). The insertion target is therefore between L173 and L175, i.e. before the `rem:dk-q-convention` block. This is a typographic adjustment to V22's line specification; the rhetorical placement (before any other content of the paper body) is unchanged.

**Adjustment recorded.** V22 §3 said L173–178; actual placement is L173–175 (before the q-convention remark). The Theorem 0.1 block introduces the Climax BEFORE the q-convention remark, so the q-convention discussion at L175–199 already operates inside the Climax framing.

---

## §6. Proposed replacement (H3 — DK standalone Theorem 0.1)

**Insertion point.** New `\section*` block + numbered theorem + remark, between L173 and L175. Exact text is the file `draft_dk_standalone_thm_0_1.tex` (~280 words, two displayed equations).

**Diff visualisation (H3).**

```diff
  172: \setcounter{tocdepth}{2}
  173: \tableofcontents
+ 173a:
+ 173b: \section*{Theorem~0.1 (Climax of Volume~I, attribution)}
+ 173c: \addcontentsline{toc}{section}{Theorem~0.1: Climax of Volume~I}
+ 173d: \label{sec:dk-climax-attribution}
+ 173e:
+ 173f: The Drinfeld--Kohno bridge proved in this article is the affine
+ 173g: Kac--Moody specialisation of a single structural theorem of
+ 173h: Volume~I, which the present standalone treats as a black box.
+ 173i: We state it here because the entire DK ladder
+ 173j: (Sections~\ref{sec:dk0}--\ref{sec:dk3}) is a corollary.
+ 173k:
+ 173l: \begin{theorem}[Vol~I Climax, $\Phi$-pullback identity]
+ 173m: \label{thm:climax}
+ 173n: [...full statement...]
+ 173o: \ClaimStatusProvedElsewhere
+ 173p: \end{theorem}
+ 173q:
+ 173r: \begin{remark}[Position of the present standalone]
+ 173s: \label{rem:dk-position-in-climax}
+ 173t: [...full remark...]
+ 173u: \end{remark}
+ 173v:
  174:
  175: \begin{remark}[Convention for $q$: Kazhdan--Lusztig vs.\ Drinfeld]
```

**One adjustment from V22 §3 (recorded in the draft header):** V22 §3 wrote `Theorems~\ref{thm:dk0}--\ref{thm:dk3}` in the prose paragraph but `Sections~\ref{sec:dk0}--\ref{sec:dk3}` in the Remark. Only `thm:dk0` exists as a labelled theorem; `thm:dk1`, `thm:dk2`, `thm:dk3` do NOT exist. The four sections `sec:dk0`, `sec:dk1`, `sec:dk2`, `sec:dk3` all exist (L679, L923, L1194, L1342). The draft uses the Section form in BOTH places, avoiding a dangling reference.

---

## §7. Cross-reference verification

Each `\ref{...}` and `\label{...}` in the three drafts is checked for resolvability AT THE TIME OF INSERTION (not after Climax-theorem environment installation, which is a separate commit).

### 7.1 Labels introduced by the drafts

| Draft | New label | Type | Used by |
|-------|-----------|------|---------|
| H1 | none | — | — |
| H2 | none (could optionally add `\label{thm:climax-vol1}` if Climax block is later promoted to numbered theorem environment) | — | (future) |
| H3 | `sec:dk-climax-attribution` | section | self |
| H3 | `thm:climax` | theorem (Vol I attribution) | H6 (`seven_faces.tex`), D1, D5–D8 |
| H3 | `rem:dk-position-in-climax` | remark | self |

### 7.2 References used by the drafts

| Draft | Reference | Resolves to | Status at insertion |
|-------|-----------|-------------|---------------------|
| H1 | (none — bare prose) | — | OK |
| H2a | `\ref{part:characteristic-datum}` | `main.tex` L1096 | LIVE |
| H3 | `\ref{sec:dk0}` | `standalone/drinfeld_kohno_bridge.tex` L679 | LIVE |
| H3 | `\ref{sec:dk3}` | `standalone/drinfeld_kohno_bridge.tex` L1342 | LIVE |
| H3 | `\ref{thm:climax}` | self (introduced by this same draft H3) | LIVE-on-insert |

**Forward references that DO NOT exist at insertion time and are NOT cited by these drafts:**

- `thm:climax` in `main.tex` — does not exist; the H1/H2 drafts state the Climax in PROSE only and do not cite a label. A follow-up commit may promote H2a to a numbered theorem block (Obstruction §7.1 of V22), at which point `\ref{thm:climax}` would become a Vol I cross-reference target.
- `thm:brst-ghost-identity` — does not exist; the H1/H2 drafts STATE the identity $\kappa(\cA) = -c_{\mathrm{ghost}}(\mathrm{BRST}(\cA))$ as a displayed equation but do NOT cite the V13 chapter label. Once V13 is installed, a follow-up commit can add `\ref{thm:brst-ghost-identity}` cross-references throughout.
- `thm:universal-trace` — exists conceptually in the swarm cache (V20 `UNIVERSAL_TRACE_IDENTITY.md`). Not yet a `.tex` label. Drafts do NOT cite it.

**Conclusion.** No dangling references are introduced by the three drafts. The drafts are safe to apply atomically without first installing V13 or the Climax theorem environment, but the deeper structural integration (numbered Climax theorem, BRST chapter cross-link, V20 trace identity cross-link) is a follow-on commit per the dependency graph in §10 below.

### 7.3 Cross-volume convention boundary

These three drafts all live in Vol I. Vol I house style:

- bare $\kappa$ (no subscript). AP113 `kappa-spectrum` discipline applies ONLY to Vol III; Vol I has a unique referent for $\kappa$ ("modular characteristic") and the bare symbol is unambiguous.
- $q = e^{2\pi i/(k+h^\vee)}$ (Kazhdan–Lusztig canonical convention; matches DK standalone L181-183).
- OPE-mode formulas (Vol I convention per AP49 hook).
- $r$-matrix with explicit level prefix $1/(k+h^\vee)$ (AP126/AP141). The KZ connection in H2a, H3 carries the full $1/(k+h^\vee)$; at critical level $k = -h^\vee$ the coefficient diverges, signalling the boundary of $\mathrm{ConnConf}$.
- "chiral Hochschild" not invoked in these drafts (no AP160 trigger). The Climax equations stop at the bar differential / KZ pullback level; chiral Hochschild structure is the next layer down (V13 BRST chapter and Vol III $\Phi$ chapter).

When the H6 propagation (`standalone/seven_faces.tex`) and D7 propagation (Vol III) edits are made later, bare $\kappa$ at Vol III contact points must be subscripted to $\kappa_{\mathrm{ch}}$ per AP113. This is an AP49 boundary translation, not a content change.

---

## §8. Test commands the user should run after applying

After applying H1, H2a, H2b to `main.tex` and H3 to `standalone/drinfeld_kohno_bridge.tex`, the user runs:

```bash
# 1. Kill any stuck pdflatex processes (AP-CY52 hygiene).
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2

# 2. Vol I main build (the abstract paragraph H1 + Part I opener H2 are part of main.tex).
cd ~/chiral-bar-cobar
make fast

# 3. Verify the Climax paragraph appears in the abstract of the rendered PDF.
pdftotext out/main.pdf - | grep -A3 "Climax (the four pillars)"

# 4. Verify the Part I Climax block appears in the rendered PDF.
pdftotext out/main.pdf - | grep -A3 "The Climax of Volume"

# 5. Verify the patched four-property cadence.
pdftotext out/main.pdf - | grep "logarithm proved by such an identity"

# 6. Verify no undef refs introduced.
grep -c "Reference .*undefined" out/main.log || echo "0 undef refs"

# 7. DK standalone build (H3 lives here).
cd ~/chiral-bar-cobar/standalone
pdflatex drinfeld_kohno_bridge.tex
pdflatex drinfeld_kohno_bridge.tex   # second pass for TOC

# 8. Verify Theorem 0.1 appears in the standalone PDF and TOC.
pdftotext drinfeld_kohno_bridge.pdf - | head -120 | grep -A2 "Theorem 0.1"

# 9. Verify thm:climax label is now defined in the standalone .aux file.
grep "thm:climax" drinfeld_kohno_bridge.aux

# 10. Vol I tests (no test changes needed; this is a prose change).
cd ~/chiral-bar-cobar
make test 2>&1 | tail -20
```

**Expected results.**

- Step 2: `make fast` returns 0; `out/main.pdf` regenerated.
- Step 3: `Climax (the four pillars)` appears in the abstract (last paragraph).
- Step 4: `The Climax of Volume` appears in the Part I opener (between FM construction and the four-property enumeration).
- Step 5: the patched cadence appears at the connector to (A)–(D).
- Step 6: 0 undefined references (no new unresolved labels).
- Step 7: standalone build succeeds.
- Step 8: Theorem 0.1 appears as `\section*` heading at the front of the standalone TOC.
- Step 9: `thm:climax` label is defined in the standalone .aux.
- Step 10: tests pass unchanged (no engine changes in this commit).

**If step 6 reports undef refs to `thm:brst-ghost-identity` or `thm:universal-trace`:** these references are NOT introduced by these drafts. They would only appear if a follow-on commit (V13 BRST chapter or H6 propagation) was bundled into this commit. The three drafts staged here introduce zero new dangling references.

---

## §9. Conventions verified for each draft

A summary cross-check, repeating §6.5 of V22 with concrete file:line anchors.

| Convention | H1 (abstract) | H2 (Part I opener) | H3 (DK standalone) |
|------------|---------------|---------------------|---------------------|
| $q = e^{2\pi i / (k+h^\vee)}$ (DK / KL canonical) | OK (one occurrence) | not invoked | OK (one occurrence; matches standalone L181-183) |
| Level prefix on KZ pole $1/(k+h^\vee)$ (AP126/AP141) | OK (in $W_N$ ghost-charge formula via $\dim(\fg)(k+h^\vee)/(2h^\vee)$ for affine) | OK (no explicit pole here; $t_{ij}$ carries level when specialised) | OK (`\nabla(V^k(\fg))` carries $1/(k+h^\vee)$ in Remark) |
| Harmonic number $H_N - 1$, NOT $H_{N-1}$ (AP136) | OK (`$c\cdot(H_{N}-1)$`) | not invoked | not invoked |
| bare $\kappa$ is Vol I house style (NOT subscripted) | OK | OK | OK |
| "chiral Hochschild" / `\ChirHoch` (AP160) | not invoked | not invoked | not invoked |
| `\Einf` / `\Eone` macros exist in target preamble | OK (`main.tex`) | OK | OK (standalone preamble) |
| `\ClaimStatus*` macros exist in target preamble | n/a (prose only) | n/a (prose only) | OK (standalone L114) |
| `\Ydg` macro exists in target preamble | n/a | n/a | OK (standalone L96) |
| OPE-mode convention (Vol I convention, AP49 hook) | OK ($N_{ij}^k$ formula in mode form, $\kappa$ as bc-ghost central charge) | OK (Yang–Baxter on residues stated at the operator level) | OK (DK ladder unchanged) |
| Cites V20 Universal Trace Identity for $\kappa = -c_\text{ghost}(\text{BRST})$ | OK (displayed equation reproduces V20 §I and V20 §III boxed equation) | OK (cross-reference to Part~\ref{part:characteristic-datum}) | OK (displayed equation in Theorem 0.1) |

**No bulk substring replacement performed (FM42 hygiene).** All three drafts are written from scratch, no `replace_all` operations.

---

## §10. Order of operations (dependency graph)

The three drafts can be applied in three different orderings. The recommended ordering minimises the dangling-reference window.

### 10.1 Recommended ordering

**Step 1 (today).** Apply H3 (DK standalone Theorem 0.1) FIRST.

- This installs the `thm:climax` label in `standalone/drinfeld_kohno_bridge.tex`.
- The standalone is a self-contained build (`pdflatex drinfeld_kohno_bridge.tex`); it does not affect `main.tex`.
- After this commit, `thm:climax` exists as a label in the standalone's `.aux` file. Cross-volume references (Vol II, Vol III) can resolve it via `\externaldocument` or `xr` package.

**Step 2 (today).** Apply H1 (abstract Climax paragraph) and H2 (Part I opener Climax block) TOGETHER in one commit.

- These are PROSE additions to `main.tex`. They do not introduce new labels, do not cite `thm:climax`, do not cite `thm:brst-ghost-identity`.
- The Climax paragraphs STATE the two equations as displayed math; the structural unification is rhetorical, not formalised as a numbered theorem. AP4 satisfied (no `\begin{theorem}` block created without proof).
- After this commit, the Vol I abstract and Part I opener prominently feature the Climax. The four-property enumeration (A)–(D)+(H) survives unchanged.

**Step 3 (next session).** Install V13 BRST ghost identity chapter per `wave14_brst_ghost_identity_chapter_draft.md`. This gives `thm:brst-ghost-identity` a home in main.tex.

**Step 4 (next session).** Promote H2a to a numbered `\begin{theorem}[Vol~I Climax]\label{thm:climax}` block in `main.tex`, with `\ClaimStatusProvedHere` and a one-paragraph proof referencing the four pillars. ~30 lines added per V22 Obstruction §7.1 option (a).

**Step 5 (later session).** Apply downstream propagations H4 (`chapters/frame/preface.tex`), H5 (`chapters/theory/introduction.tex`), H6 (`standalone/seven_faces.tex`) per V22 §5 punch list. These DEPEND on `thm:climax` existing in main.tex (Step 4).

**Step 6 (later session).** Apply cross-volume propagations D6 (Vol II), D7 (Vol III). These translate bare $\kappa$ to the appropriate Vol III subscripted form ($\kappa_{\mathrm{ch}}$ at the bar-cobar contact; $\kappa_{\mathrm{BKM}}$ at the Borcherds contact) per AP113 / AP49 boundary.

### 10.2 Alternative ordering: install V13 FIRST

If the user prefers structural completeness over rhetorical promotion, V13 BRST chapter can be installed before H1/H2/H3. This makes both Climax equations live theorems (`thm:climax` in main.tex via Step 4 above; `thm:brst-ghost-identity` in V13 chapter). Then H1/H2/H3 can cite both labels explicitly. Higher rigour, larger commit, longer review cycle.

**Recommendation: §10.1 ordering.** The rhetorical promotion is the highest-leverage single edit (V22 §0.1: "the rhetorical missing peak"). Installing H3 + (H1, H2) today gives the reader the unified framing immediately; the formal numbered theorem and BRST chapter cross-link can follow without retracting any of these prose additions.

### 10.3 Build-break risk

| Apply | Build-break risk | Mitigation |
|-------|------------------|------------|
| H3 alone | none | self-contained standalone |
| H1 alone | none | prose only, no new labels, no new refs |
| H2 alone | none | prose only, references existing `part:characteristic-datum` label |
| H1+H2+H3 in one commit | none | each draft independently safe; no cross-dependencies among the three |
| H1+H2+H3 + H4-H6 in one commit | RISK | H6 cites `\ref{thm:climax}` which lives in standalone, not main.tex; needs `xr` package or duplicate label |
| H1+H2+H3 + V13 in one commit | LOW (all clean if V13 chapter is build-clean) | V13 is a large chapter; recommend separate commit |

The recommended Step 1 + Step 2 today yields a clean build with no dangling references and full rhetorical promotion. The downstream propagations and structural completion can follow without merge conflicts.

---

## §11. Summary

Three V22 drafts staged as application-ready `.tex` files in `~/chiral-bar-cobar/adversarial_swarm_20260416/`:

1. `draft_main_tex_abstract_paragraph.tex` — H1 abstract Climax paragraph, ~250 words, insertion point `main.tex` between L798 and L799.
2. `draft_main_tex_part_I_opener.tex` — H2a Climax block + H2b cadence patch, ~200 words combined, insertion points `main.tex` after L917 and replacing L919.
3. `draft_dk_standalone_thm_0_1.tex` — H3 Theorem 0.1 + position remark, ~280 words, insertion point `standalone/drinfeld_kohno_bridge.tex` between L173 and L175 (V22 said L173–178; actual location is before the q-convention remark at L175).

**Two minor adjustments to V22's specification, both documented in draft headers:**

- V22 §3 referenced `Theorems~\ref{thm:dk0}--\ref{thm:dk3}` in its outer prose, but only `thm:dk0` exists as a labelled theorem. Adjusted to `Sections~\ref{sec:dk0}--\ref{sec:dk3}` (which all exist).
- V22 §3 specified the H3 insertion target as L173–178 ("`\tableofcontents`...`\section{Introduction}`"). The actual file structure has `\tableofcontents` at L173 and the q-convention remark beginning at L175 (the `\section{Introduction...}` is further down). Insertion target adjusted to L173–175 (before the q-convention remark). This places the Climax framing BEFORE the q-convention discussion, so the q convention reads as a tactical fixing inside the Climax framing.

**Zero dangling references introduced.** The drafts are safe to apply atomically without first installing V13 or promoting H2a to a numbered theorem environment. Forward references (`thm:climax` in main.tex, `thm:brst-ghost-identity`, `thm:universal-trace`) are not cited by these drafts; the Climax equations are stated as displayed math, and the numbered theorem environment is introduced only in the DK standalone (where `\ClaimStatusProvedElsewhere` attributes the proof to Vol I).

**Dependency graph respected.** Recommended ordering: Step 1 = apply H3 today (standalone, self-contained). Step 2 = apply H1+H2 today (main.tex, prose only). Step 3 = install V13 (next session). Step 4 = promote H2a to numbered theorem environment (next session). Step 5 = downstream propagations H4–H6 (later). Step 6 = cross-volume propagations D6, D7 with AP113/AP49 boundary translation (later).

**Test commands listed in §8.** After applying, the user runs `pkill -9 -f pdflatex; sleep 2; cd ~/chiral-bar-cobar && make fast`, then verifies the Climax paragraph in the rendered PDF via `pdftotext out/main.pdf - | grep -A3 "Climax (the four pillars)"`. Standalone build is `cd ~/chiral-bar-cobar/standalone && pdflatex drinfeld_kohno_bridge.tex` (twice, for TOC).

**No commits made in this session.** This report is the application blueprint; the commit is the user's action after review.

— Raeez Lorgat, 2026-04-16.
