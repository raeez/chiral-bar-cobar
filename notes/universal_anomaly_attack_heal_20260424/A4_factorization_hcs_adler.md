# A4 factorization / hCS / KT-formality / Adler-Bardeen audit

Scope: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
and its two explicit inputs `universal_anomaly_voa_explicit_supplement.tex`,
`universal_anomaly_local_global_arithmetic_supplement.tex`.

Verdict: the factorization-algebra and hCS edge is not theorem-level in
the present paper. The safe repair is a conditional anomaly bridge. The
paper has theorem-level ingredients, but the current text turns them into
strict canonicity, strict `E_3` formality, and an Adler-Bardeen theorem
without the needed comparison theorems.

## 1. Status split

Theorem-level:

- Operad-level rational formality of little-disks `E_n` for `n >= 3`,
  in the Fresse-Willwacher sense. This is operad-level formality, not
  a canonical strictification of a concrete CY3 Hochschild cochain model.
- Costello-Gwilliam factorization algebra formalism: prefactorization
  plus Weiss/cosheaf descent is the correct structure. Ayala-Francis
  pushforward/Fubini applies to topological factorization homology with
  the correct framed/topological coefficient data.
- Local hCS/BCOV perturbative statements in the Costello-Li scope:
  flat affine models, BCOV/hCS couplings, and perturbative quantization
  in the stated gauge/supergroup settings.
- Adler-Bardeen 1969 in its original scope: one-loop exactness of the
  axial anomaly for the models treated there; Bardeen-Zumino/Wess-Zumino
  give the general descent/consistency language.

Conditional:

- `Phi^{FA}_3(X)` as a canonical holomorphic `E_3` factorization algebra
  on an arbitrary smooth projective CY3, especially as a colimit-preserving
  functor out of `D^b_dg(X)`.
- Identification of compact Costello-Li heat-kernel/Feynman weights with
  a chosen `E_3` formality morphism.
- `U^3_{2,X} = [m_3,B^{(2)}]_X` and any strictification of the `L_infty`
  formality morphism from vanishing of `U_2`.
- The hCS anomaly class equals the Dolbeault class `[m_3,B^{(2)}]_X` and
  satisfies an Adler-Bardeen-type all-loop non-renormalization theorem.
- Clemens/H-twisted replacement, unless a closed `H`, a square-zero
  twisted differential, Courant/CDO existence, and a twisted cyclic
  comparison are supplied.

Heuristic:

- "The cocycle is precisely the Adler-Bardeen condition" as currently
  written.
- "Each Clemens climax lifts verbatim" after replacing `\bar\partial`
  by `d^H`.
- RG/anomaly-matching prose that uses `hbar^2 K=-1` as a physical
  non-renormalization principle.

## 2. Fatal findings

CRITICAL: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:223`
states that locally constant factorization algebras on a chart
`U \cong \mathbb R^6` are equivalent to `E_3`-algebras. As stated this is
dimensionally wrong: locally constant factorization algebras on real
6-manifolds give `E_6` data. A holomorphic `\mathbb C^3` theory can have
a holomorphic/3-complex-dimensional structure, but that is not the
statement written. The repair must distinguish real locally constant
`E_6` from holomorphic factorization in complex dimension 3.

CRITICAL: `...tex:225` and `...tex:752` use `K3 \times \mathbb C^2` as a
noncompact target for "six-dimensional hCS". This target is complex
dimension 4, real dimension 8. Six-real-dimensional hCS requires complex
dimension 3, e.g. `K3 \times \mathbb C` if that geometry is intended.

CRITICAL: `...tex:531-551` marks `thm:formality-atiyah` and
`cor:strict-formality` proved here. The proof imports operad-level
formality and then concludes a strict `E_3` isomorphism from vanishing of
the second Taylor coefficient. This is not valid. Higher Taylor
coefficients of an `L_infty` morphism are not generally iterated
Massey brackets of `U_2`, and vanishing `U_2=0` does not strictify the
whole morphism. The cited Markl-Shnider-Stasheff reference cannot carry
that conclusion without an explicit obstruction-complex theorem.

CRITICAL: `...tex:702` and `...tex:713` assert
`\at_X^{\cup 3}=0 <=> a_3=0` and use this as strand `(ii)=>(iii)`.
This is not proved by Gilkey. Heat-kernel coefficients are universal
local curvature polynomials; the expansion does not "terminate at
coefficient `a_3`" on a CY3, and `a_3` is not automatically
`\int_X \at_X^{\cup 3}`. Also, closedness of a cyclic-skew square
`\at_X \wedge \at_X` does not force the cubic `\at_X^{\cup 3}` to vanish.

CRITICAL: `...tex:713` says Costello-Li 2016 Proposition 5.2 identifies
the hCS parametrix with the bar-cobar contracting homotopy. The
Costello-Li source is about twisted supergravity/BCOV and hCS twists; the
available primary text treats BCOV fields, local cyclic cohomology, and
perturbative quantization in specific settings. It is not a theorem that
the hCS parametrix is inverse to the Vol I chiral bar-cobar counit.

CRITICAL: `...tex:730-742` marks `thm:adler-bardeen` proved here. The
Adler-Bardeen theorem is a non-renormalization theorem for axial-vector
anomalies in the original four-dimensional QFT setting. The manuscript
needs a separate local BRST-cohomology computation for six-real-dimensional
holomorphic Chern-Simons with gauge algebra `End(T_X)`, plus a
non-renormalization theorem in that holomorphic theory, before the class
can be called the Adler-Bardeen anomaly. Bardeen-Zumino descent supplies
language, not this identification.

SERIOUS: `...tex:228` promotes Stage 1 to a morphism
`D^b_dg(X) -> Fact^{E_3}_X` in `Pr^L_{k,st}` and says
Costello-Gwilliam-Li locality pins compact generators. This is not
constructed. Lurie extension theorems apply after a functor on compact
objects is already defined; they do not manufacture the hCS/FA functor.

SERIOUS: `...tex:868-878` and `...tex:883-895` overstate the
Clemens replacement. The later `q:H-twisted cocycle on Clemens`
(`...tex:1037-1044`) correctly says this is open. The current theorem
surface contradicts that open status.

SERIOUS: `...tex:874` says `d^H=d+H\wedge(-)` satisfies `(d^H)^2=0`
on a balanced `SU(3)` structure. In general `(d+H\wedge)^2=dH\wedge(-)`
for odd closed `H` up to the usual sign simplification; in the Strominger
system one often has `dH=tr(R\wedge R)-tr(F\wedge F)`, not zero before
anomaly cancellation. Square-zero is an extra hypothesis, not a consequence
of balancedness.

SERIOUS: `...tex:889-900` says every `H`-flux has a Courant avatar and
every Courant algebroid has a CDO. Exact Courant algebroids require a
closed Severa class, and CDO existence carries characteristic-class
conditions/choices. The theorem should be conditional on those data.

MODERATE: `...tex:876` marks the Strominger reformulation
`ProvedElsewhere`, while `...tex:1037-1044` says the `H`-twisted cocycle
construction remains open. This is status drift inside the same file.

## 3. Repaired conditional bridge statement

```tex
\begin{theorem}[Conditional factorisation--hCS anomaly bridge;
\ClaimStatusConditional]
\label{thm:conditional-factorisation-hcs-adler}
Let $X$ be a smooth projective Calabi--Yau threefold and fix a
holomorphic BV model of six-real-dimensional holomorphic
Chern--Simons theory on $X$ with fields
$\Omega^{0,\bullet}(X,\mathfrak g)[1]$, $\mathfrak g=\End(T_X)$.
Assume the following data and comparison theorems.
\begin{enumerate}[label=\textup{(F\arabic*)}]
\item The Costello--Gwilliam observables of this BV theory form a
holomorphic factorisation algebra satisfying Weiss descent; on
noncompact targets a cylindrical-end/compact-support hypothesis kills
boundary terms.
\item A rational $E_3$-formality datum
$\alpha\in\operatorname{Form}_3(\mathbb Q)$ has been chosen, and the
heat-kernel/Feynman graph weights of the BV model are compared
graph-by-graph with the $\alpha$-transported $E_3$ operations.
\item The HKR--Tsygan--Shoikhet cyclic comparison identifies the
one-loop local BRST anomaly class of the hCS theory with the cyclic
Hochschild class
\[
  [m_3,B^{(2)}]_X\in HC^{-,2}(\End(T_X),
  \End(T_X)\otimes\Omega^1_X)\xrightarrow{\mathrm{HKR}}
  H^2(X,\Omega^1_X).
\]
\item Local BRST cohomology in ghost number $1$ and form degree $6$
is generated, in this theory and with this gauge algebra, by the class
in \textup{(F3)}.
\item An Adler--Bardeen-type non-renormalisation theorem holds for this
holomorphic BV theory: after \textup{(F4)}, the all-loop anomaly is the
one-loop class.
\end{enumerate}
Then vanishing of $[m_3,B^{(2)}]_X$ trivialises the hCS anomaly and
gives a canonical stage-one factorisation algebra relative to the
chosen formality/locality data. Without \textup{(F3)--(F5)}, the
identification with Adler--Bardeen is an anomaly-matching conjecture,
not a theorem.
\end{theorem}
```

For Clemens-type non-Kahler small resolutions, append:

```tex
\begin{question}[H-twisted Clemens bridge; \ClaimStatusOpen]
For a Clemens small resolution $\tilde Y$, suppose one has a closed
Severa class $[H]\in H^3(\tilde Y,\mathbb R)$ with a square-zero
twisted differential on the chosen complex, an $H$-twisted Courant
algebroid satisfying the characteristic-class condition for a CDO, and
a cyclic comparison identifying its BRST anomaly with an
$H$-twisted class $[m_3,B^{(2)}]^H_{\tilde Y}$. Does the vanishing of
this class gate the four H-twisted analogues of the climaxes?
\end{question}
```

## 4. Primary-source / proof obligations

1. Costello-Li scope: cite the exact theorem in Costello-Li/BCOV giving
   perturbative quantization for the precise hCS model used here, and
   prove the extension from flat or supergroup settings to compact
   projective CY3 with gauge algebra `End(T_X)`.

2. Factorization algebra descent: cite the exact Costello-Gwilliam
   theorem establishing Weiss descent for these observables. If only a
   prefactorization algebra is constructed, state that.

3. Real/holomorphic operadic level: prove why the local structure is
   `E_3` rather than real `E_6`, or rewrite the statement as holomorphic
   factorization in complex dimension 3 with no real-locally-constant
   `E_3` assertion.

4. Formality datum: separate Fresse-Willwacher operad-level rational
   intrinsic formality from the chosen formality datum used by the CY3
   Hochschild cochain/factorization model. State the `GRT_1(Q)` torsor
   if noncanonical choices remain.

5. Strictification: replace the Markl-Shnider-Stasheff strictness claim
   with an explicit obstruction theory proving all higher Taylor
   coefficients vanish or are gauge-removable. Vanishing of `U_2` alone
   is not enough.

6. Heat-kernel coefficient: compute the exact Seeley-DeWitt coefficient
   relevant to six real dimensions, including normalisation, signs,
   boundary terms, and the map from curvature polynomials to Atiyah
   classes. Do not write `a_3 = int at^3` without this computation.

7. Bar-cobar to parametrix: prove a chain map from the Positselski
   contracting homotopy to the hCS propagator/parametrix, including
   choices and homotopies. Current citations do not supply it.

8. Adler-Bardeen: prove local BRST cohomology and one-loop exactness
   for six-dimensional holomorphic Chern-Simons with the actual gauge
   algebra. The 1969 Adler-Bardeen theorem and Bardeen-Zumino descent
   are provenance for the analogy, not the theorem.

9. Noncompact geometry: correct `K3 x C^2` to a complex-threefold target
   if six-dimensional hCS is intended, and prove cylindrical-end
   compatibility for that corrected target.

10. Clemens/H-twist: supply closed `H`, square-zero differential,
    Courant/CDO existence conditions, and a twisted cyclic comparison.
    Until then the later open question is the correct status.

## 5. Downgrades recommended

- `thm:formality-atiyah`: downgrade from `ProvedHere` to `Conditional`.
  Its theorem title should say "second-obstruction comparison" rather
  than "Atiyah class as E3-formality obstruction" unless all higher
  obstructions are handled.

- `cor:strict-formality`: downgrade to `Conjectured` or remove. A safe
  corollary can say only that a chosen second obstruction vanishes.

- `thm:main`: keep the pentagon only as conditional on (H1)--(H2) plus
  the new factorization/hCS bridge hypotheses (F1)--(F5). The edge
  `(ii)=>(iii)` is not theorem-level.

- `thm:adler-bardeen`: downgrade to `Conditional` or `Heuristic`.
  The repaired title should be "Conditional hCS anomaly bridge" rather
  than "Universal anomaly = Adler-Bardeen condition".

- `rem:hcs-compactness`: correct the dimension of the noncompact target
  and replace "where the two forms agree" by an explicit hypothesis.

- `cor:strominger` and `thm:strominger-native`: downgrade to
  `Conditional`/`Open` in line with `q:H-twisted cocycle on Clemens`.
  Remove "lifts verbatim".

- Abstract/introduction lines claiming "each edge is a single
  chain-level equality" should be changed to "each edge is conditional
  on the named bridge data" until the obligations above are discharged.

## 6. Files changed

- `notes/universal_anomaly_attack_heal_20260424/A4_factorization_hcs_adler.md`

No target TeX files were edited.

## 7. Commands run

- `sed -n '1,220p' repo-local instructions file`
- `sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md`
- `rg` over the target standalone, supplements, metadata, and selected
  Vol III notes for `thm:formality-atiyah`, `thm:adler-bardeen`,
  `Costello--Li`, `E_3`, `Adler--Bardeen`, `Clemens`, and `H`-twisted
  surfaces.
- Targeted `sed` reads around lines `207-235`, `527-555`, `650-760`,
  `848-905`, `996-1045`, and bibliography blocks of the standalone.
- `sed` reads of `chapters/connections/concordance.tex`,
  `metadata/theorem_registry.md`,
  `archive/raeeznotes/raeeznotes100/red_team_summary.md`.
- `sed` reads of
  `/Users/raeez/calabi-yau-quantum-groups/notes/adversarial_architecture_swarm_20260424/agent_10_hcs_factorization.md`
  and related Vol III working notes for cross-volume consistency.
- Web/primary-source checks:
  `arxiv.org/abs/1606.00365` (Costello-Li),
  `arxiv.org/abs/1503.08699` (Fresse-Willwacher),
  `arxiv.org/abs/1206.5522` (Ayala-Francis),
  `arxiv.org/abs/0901.0069` (Dolgushev-Tamarkin-Tsygan),
  APS DOI page for Adler-Bardeen 1969,
  ScienceDirect/eScholarship page for Bardeen-Zumino 1984.
- `curl`/`tar -xO`/`zcat` source inspections of the arXiv TeX where
  available.

No build or test command was run.
