# Theorematic Volume I Strike List

This report audits the live manuscript source in `main.tex` and its active included files, with the sole criterion: **what must change for the book to read as a theorematic Volume I rather than as a mixed theorem-book and constitutional history of the programme**.

Each strike item gives a pinpoint source coordinate (`file:line`), current chapter page span (from `main.toc` when available), issue class, and a rewrite algorithm.
When a local heading could be matched to the table of contents, the accompanying CSV also records the exact section-start page.

## Global diagnosis

- Active main-matter counts from automated scan:

  - **Core Theory**: 164 strike items in this ledger (narrative-meta=114, status-heuristic=9, status-conjectured=33, meta-heading=7, architecture=1).
  - **Complete Portraits**: 206 strike items in this ledger (status-conjectured=72, narrative-meta=123, meta-heading=7, architecture=3, status-heuristic=1).
  - **Synthesis and Programmes**: 199 strike items in this ledger (status-conjectured=53, meta-heading=9, status-heuristic=19, architecture=2, narrative-meta=116).


## Rewrite algorithms

- **ALG-A** — Retitle or relocate meta-heading: replace programme/frontier/future headings by mathematical-question headings; if unresolved material remains, move to Part III outlook or external notes.
- **ALG-B** — Conjecture containment: split statement into theorematic proved core + explicitly fenced conjectural remainder; if core chapter is affected, move conjectural remainder to synthesis/outlook.
- **ALG-C** — Part-opener compression: replace constitutional/programmatic paratext by a one-paragraph mathematical contract (question, inputs, outputs, theorem map).
- **ALG-D** — Portrait cleanup: remove research-programme sections from example chapters; end with theorematic summary/corollary instead.
- **ALG-E** — Concordance quarantine: compress constitutional/status-ledger material to an afterword or editorial appendix; retain only literature concordance needed for reading the theorems.
- **ALG-F** — Legacy stub purge: remove or archive six-line snapshot files from live tree and delete commented include scaffolding once archival path is documented in README.
- **ALG-G** — Appendix theoremization: convert frontier appendices into theorem-support appendices, or move frontier material to external notes.
- **ALG-H** — Generic title normalization: rename placeholder or generic chapter titles to mathematical object names; ensure TOC reads like a theorematic monograph.
- **ALG-I** — Narrative meta-pruning: excise internal project-management nouns (frontier, programme, status, stratum, ledger) from running prose unless they designate a formal theorem or appendix title.

## Non-negotiable architectural strikes

- **I0569** `chapters/frame/heisenberg_frame.tex:2268` — Excise programme section from frame chapter or collapse to one terminal paragraph (ALG-A).
- **I0566** `main.tex:774` — Replace part opener with mathematical contract; remove status/frontier diction (ALG-C).
- **I0571** `chapters/examples/examples_summary.tex:1` — Normalize title and numbering to current volume architecture (ALG-I).
- **I0570** `chapters/examples/free_fields.tex:2` — Rename chapter to mathematical subject (e.g. Free field atoms or Free fields) (ALG-H).
- **I0567** `main.tex:911` — Replace part opener with one-paragraph portrait contract; remove programme bleed (ALG-C).
- **I0572** `chapters/connections/concordance.tex:1` — Split literature concordance from status ledger; keep only reader-facing concordance in book (ALG-E).
- **I0568** `main.tex:1065` — Compress to a short synthesis preface and push editorial meta to afterword/notes (ALG-C).

## Exhaustive ledger

### None — `chapters/frame/heisenberg_frame.tex`
Current chapter pages: 45-78
- **I0001** `line 2268` | **meta-heading** | **critical** | heading/context: `\section{Synthesis: the modular Koszul programme}`\
  Snippet: \section{Synthesis: the modular Koszul programme}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### None — `chapters/frame/heisenberg_frame.tex`
- **I0569** `line 2268` | **architecture** | **critical** | heading/context: `Frame synthesis section`\
  Snippet: Frame synthesis section\
  Action: Excise programme section from frame chapter or collapse to one terminal paragraph\
  Algorithm: ALG-A

### None — `chapters/frame/heisenberg_frame.tex`
Current chapter pages: 45-78
- **I0002** `line 2340` | **meta-heading** | **critical** | heading/context: `\subsection{The modular Koszul programme}`\
  Snippet: \subsection{The modular Koszul programme}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Core Theory — `chapters/theory/algebraic_foundations.tex`
Current chapter pages: 97-100
- **I0005** `line 249` | **narrative-meta** | **high** | heading/context: `\subsection{The Gui--Li--Zeng quadratic duality framework}`\
  Snippet: and~(iv) are descriptions of the respective frameworks' scopes.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/bar_cobar_construction.tex`
Current chapter pages: 177-346
- **I0007** `line 1980` | **narrative-meta** | **high** | heading/context: `\subsection{Motivation: reversing the prism}`\
  Snippet: If the bar construction acts as a prism decomposing chiral algebras into their spectrum, the cobar construction acts as the \emph{inverse prism}, reconstructing the algebra from its spectral components. Geometrically: th\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0008** `line 2903` | **status-heuristic** | **high** | heading/context: `\subsection{Physical interpretation: on-shell propagator and Feynman-rule templates}`\
  Snippet: \begin{conjecture}[Cobar elements as on-shell propagator templates; \ClaimStatusHeuristic]\label{conj:cobar-physical}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0009** `line 2959` | **narrative-meta** | **high** | heading/context: `\subsection{Physical interpretation: on-shell propagator and Feynman-rule templates}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0010** `line 2960` | **status-heuristic** | **high** | heading/context: `\subsection{Physical interpretation: on-shell propagator and Feynman-rule templates}`\
  Snippet: Conjecture~\ref{conj:cobar-physical} is tagged \ClaimStatusHeuristic{} because the identification of cobar elements with on-shell propagators requires external physics input (equations of motion, path integral measure) that lies outside the algebraic framework of this monograph.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0011** `line 3628` | **narrative-meta** | **high** | heading/context: `\subsection{Poincaré--Verdier duality realization}`\
  Snippet: \item The duality exchanges extraction (analysis) with reconstruction (synthesis)\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0012** `line 4287` | **status-heuristic** | **high** | heading/context: `\subsection{BRST cohomology and string theory connection}`\
  Snippet: \begin{conjecture}[BRST cohomology realization; \ClaimStatusHeuristic]\label{conj:brst-cohomology}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0013** `line 4354` | **status-heuristic** | **high** | heading/context: `\subsection{BRST cohomology and string theory connection}`\
  Snippet: \begin{conjecture}[Anomaly cancellation for matter-ghost systems; \ClaimStatusHeuristic]\label{conj:anomaly-cancellation}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0014** `line 4943` | **narrative-meta** | **high** | heading/context: `\subsection{I-adic completion: topology and convergence}`\
  Snippet: throughout Parts~II--III, whereas $W_\infty$ marks the frontier where a\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0015** `line 5250` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \emph{Scope.} This is the current M/S-level shadow inside the manuscript's\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0016** `line 5253` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: that frontier is recorded under MC4, where $W_\infty$ is the conjectural\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0017** `line 5259` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \begin{example}[$W_\infty$: exact MC4 frontier]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0018** `line 5267` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: not the stronger H-level realization expected in the modular programme.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0019** `line 5269` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \emph{The precise frontier statement} is no longer a first inverse-limit\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0020** `line 5309` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: finite-type theory.  It should be read as an exact MC4 frontier, not as\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0021** `line 5313` | **status-conjectured** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \begin{conjecture}[Inverse-limit completed bar-cobar package; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0022** `line 5335` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \emph{This is the theorem-shaped local form of the MC4 frontier:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0023** `line 5578` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: realization problems remain on the MC4/MC5 frontier.  By\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0024** `line 5711` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: remaining frontier is\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0025** `line 5830` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: completion.  Thus the live $\mathcal{W}_\infty$ frontier is to\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0026** `line 5857` | **status-conjectured** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \texorpdfstring{$W_\infty$}{W_infty} target; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0027** `line 5879` | **status-conjectured** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \texorpdfstring{$W_\infty$}{W_infty} completion; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0028** `line 5976` | **status-conjectured** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \texorpdfstring{$W_\infty$}{W_infty}; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0029** `line 5997` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: Thus the live $\mathcal{W}_\infty$ frontier is not further stabilization\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0030** `line 6180` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: the remaining $\mathcal{W}_\infty$ frontier is reduced to matching the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0031** `line 6233` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: $\mathcal{W}_\infty$ frontier is reduced to exact equality of the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0032** `line 6888` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: live stage-$4$ frontier is one new coefficient in the $(3,3)$ block,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0033** `line 6909` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \begin{corollary}[Stage-$4$ frontier as one mixed block and three\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0034** `line 7026` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: Equivalently, the live mixed stage-$4$ frontier splits into one\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0035** `line 7228` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \begin{corollary}[Stage-$4$ frontier after theorematic mixed\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0036** `line 7289` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: \begin{proposition}[Exact MC4 frontier packet for the standard\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0037** `line 7355` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: $\mathcal{J}_4$ to the frontier of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0038** `line 7356` | **narrative-meta** | **high** | heading/context: `\subsection{Examples: computing Koszul duals with completion}`\
  Snippet: Proposition~\ref{prop:winfty-mc4-frontier-package} has been\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0039** `line 7551` | **narrative-meta** | **high** | heading/context: `\subsection{Mathematical foundations: three regimes}`\
  Snippet: scope of the present chapter.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0040** `line 7811` | **narrative-meta** | **high** | heading/context: `\subsubsection{\texorpdfstring{Regime II: curved differential ($m_1^2 = [\mu_0, -]$, central curvature)}{Regime II: curved differential (m1 squared = commutator with mu0, central curvature)}}`\
  Snippet: fall outside the scope of Theorem~\ref{thm:central-implies-strict}.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0041** `line 8385` | **narrative-meta** | **high** | heading/context: `\section{Non-quadratic chiral algebras}`\
  Snippet: whose standard tower is theorematic while the remaining frontier is the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0042** `line 8549` | **meta-heading** | **critical** | heading/context: `\subsubsection{Class IV: general (exact MC4 frontier)}`\
  Snippet: \subsubsection{Class IV: general (exact MC4 frontier)}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0043** `line 8565` | **narrative-meta** | **high** | heading/context: `\subsubsection{Class IV: general (exact MC4 frontier)}`\
  Snippet: The frontier is now narrower.  For the standard principal-stage tower,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0044** `line 8619` | **narrative-meta** | **high** | heading/context: `\subsection{Comparison of the four classes}`\
  Snippet: \textbf{General / frontier} &\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0045** `line 8622` | **narrative-meta** | **high** | heading/context: `\subsection{Comparison of the four classes}`\
  Snippet: OPEN / frontier &\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0046** `line 8981` | **narrative-meta** | **high** | heading/context: `\subsection{Summary and decision tree}`\
  Snippet: \item Is the generating space infinite-dimensional? $\Rightarrow$ treat as an exact MC4 frontier: first construct the filtered H-level target, then identify its finite quotients by explicit coefficient identities and fin\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0047** `line 9935` | **narrative-meta** | **high** | heading/context: `\subsection{Statement of the main result}`\
  Snippet: \smallskip\noindent\emph{Scope.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0048** `line 10899` | **narrative-meta** | **high** | heading/context: `\subsection{The Taylor expansion of the logarithm}`\
  Snippet: logarithm is a natural target for future work.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0049** `line 11104` | **status-conjectured** | **high** | heading/context: `\subsection{Visible theorems}`\
  Snippet: \ClaimStatusConjectured]\label{conj:factorization-finiteness-criterion}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0050** `line 11173` | **narrative-meta** | **high** | heading/context: `\subsection{The monograph as construction of a categorical logarithm}`\
  Snippet: These are not five separate programmes.  They are five windows onto a\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/chiral_koszul_pairs.tex`
Current chapter pages: 557-606
- **I0085** `line 839` | **narrative-meta** | **high** | heading/context: `\subsection{Koszulness verification: the PBW deformation method}`\
  Snippet: (Appendix~\ref{app:combinatorial-frontier}) requires\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0086** `line 1627` | **narrative-meta** | **high** | heading/context: `\subsection{\texorpdfstring{Stage 3: bar construction computes $\mathcal{A}_2^!$}{Stage 3: bar construction computes A-2!}}`\
  Snippet: \begin{remark}[Frontier completion package]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0087** `line 1634` | **narrative-meta** | **high** | heading/context: `\subsection{\texorpdfstring{Stage 3: bar construction computes $\mathcal{A}_2^!$}{Stage 3: bar construction computes A-2!}}`\
  Snippet: infinite-type algebras, belongs to the frontier package of that\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0088** `line 1636` | **narrative-meta** | **high** | heading/context: `\subsection{\texorpdfstring{Stage 3: bar construction computes $\mathcal{A}_2^!$}{Stage 3: bar construction computes A-2!}}`\
  Snippet: the frontier hypotheses of Appendix~\ref{app:nilpotent-completion}.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0089** `line 3051` | **status-conjectured** | **high** | heading/context: `\subsection{Motivation: ghost systems}`\
  Snippet: \begin{conjecture}[Derived bc-$\beta\gamma$ Koszul duality; \ClaimStatusConjectured]\label{conj:derived-bc-betagamma}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0090** `line 3078` | **status-conjectured** | **high** | heading/context: `\subsection{Motivation: ghost systems}`\
  Snippet: \ClaimStatusConjectured{} for two independent reasons:\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0091** `line 3131` | **narrative-meta** | **high** | heading/context: `\subsection{Virasoro algebra: beyond the quadratic setting}`\
  Snippet: local OPE blocks, with the genuinely mixed stage-$4$ frontier reduced\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/chiral_modules.tex`
Current chapter pages: 681-752
- **I0126** `line 712` | **narrative-meta** | **high** | heading/context: `\subsection{Conformal blocks and the bar complex}`\
  Snippet: = \delta_{\sigma,\tau}$, the sum telescopes to the claimed\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0127** `line 3659` | **narrative-meta** | **high** | heading/context: `\subsection{When homology is non-trivial}`\
  Snippet: The failure of acyclicity means the alternating sum does not telescope completely.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0128** `line 4779` | **narrative-meta** | **high** | heading/context: `\subsection{Fusion product preservation under bar-cobar}`\
  Snippet: Kazhdan--Lusztig programme~\cite{KL93}.  The configuration space\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/configuration_spaces.tex`
Current chapter pages: 113-176
- **I0006** `line 600` | **narrative-meta** | **high** | heading/context: `\subsection{Logarithmic differential forms}`\
  Snippet: This is the main theorem of \cite{Arnold69, FM94}. The proof uses intersection theory on $\overline{C}_n(\Sigma_g)$ and is beyond our scope here.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/deformation_theory.tex`
Current chapter pages: 635-680
- **I0106** `line 1337` | **narrative-meta** | **high** | heading/context: `\subsection{The cyclic deformation complex}`\
  Snippet: \begin{remark}[Scope of Theorem~\ref{thm:mc2-1-km}]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0107** `line 1375` | **narrative-meta** | **high** | heading/context: `\subsection{The cyclic deformation complex}`\
  Snippet: packages the remaining MC2 frontier into three tasks: the intrinsic\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0108** `line 1941` | **status-conjectured** | **high** | heading/context: `\subsubsection{The mechanism}`\
  Snippet: \begin{conjecture}[Modular periodicity for minimal models; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0109** `line 2118` | **status-conjectured** | **high** | heading/context: `\subsubsection{The mechanism}`\
  Snippet: \begin{conjecture}[Modular periodicity for general rational chiral algebras; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0110** `line 2153` | **status-conjectured** | **high** | heading/context: `\subsubsection{The mechanism}`\
  Snippet: rational vertex algebras (\ClaimStatusConjectured), where Zhu's finiteness theorem and Huang's\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0111** `line 2202` | **status-conjectured** | **high** | heading/context: `\subsubsection{Examples}`\
  Snippet: \begin{conjecture}[Modular periodicity for WZW models; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0112** `line 2322` | **status-conjectured** | **high** | heading/context: `\subsubsection{Koszul dual behavior}`\
  Snippet: \begin{conjecture}[Reflected modular periodicity; \ClaimStatusConjectured]\label{conj:reflected-modular-periodicity}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0113** `line 2346` | **narrative-meta** | **high** | heading/context: `\subsubsection{Koszul dual behavior}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0114** `line 2347` | **status-conjectured** | **high** | heading/context: `\subsubsection{Koszul dual behavior}`\
  Snippet: This conjecture is labeled \ClaimStatusConjectured{} because the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0115** `line 2385` | **narrative-meta** | **high** | heading/context: `\subsubsection{The quantum group structure}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0116** `line 2609` | **status-conjectured** | **high** | heading/context: `\subsubsection{Genus dependence and nilpotent depth}`\
  Snippet: \begin{conjecture}[Geometric amplitude on compactified moduli; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0117** `line 2704` | **status-conjectured** | **high** | heading/context: `\subsection{Stratified periodicity}`\
  Snippet: \begin{conjecture}[Stratified periodicity package (partial); \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0118** `line 2810` | **status-conjectured** | **high** | heading/context: `\subsection{Stratified periodicity}`\
  Snippet: The conjecture is tagged \ClaimStatusConjectured{} because the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0119** `line 2883` | **narrative-meta** | **high** | heading/context: `\subsection{Stratified periodicity}`\
  Snippet: \item \emph{Principal rational frontier.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0120** `line 2890` | **narrative-meta** | **high** | heading/context: `\subsection{Stratified periodicity}`\
  Snippet: \item \emph{Outer rational frontier.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0121** `line 2914` | **narrative-meta** | **high** | heading/context: `\subsection{Stratified periodicity}`\
  Snippet: See \S\ref{subsec:nine-futures}, Future~7 for the programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0122** `line 3016` | **status-conjectured** | **high** | heading/context: `\subsection{Holographic duality}`\
  Snippet: \begin{conjecture}[Holographic Koszul duality; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0123** `line 3028` | **narrative-meta** | **high** | heading/context: `\subsection{Holographic duality}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0124** `line 3029` | **narrative-meta** | **high** | heading/context: `\subsection{Holographic duality}`\
  Snippet: This conjecture lies outside the scope of the present monograph: it is a\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0125** `line 3039` | **narrative-meta** | **high** | heading/context: `\subsection{Holographic duality}`\
  Snippet: duality framework alone.  In the monograph's frontier order, the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/derived_langlands.tex`
- **I0149** `line 16` | **narrative-meta** | **high** | heading/context: `\chapter{Derived structures and the geometric Langlands correspondence}`\
  Snippet: point of the geometric Langlands programme into bar-cobar duality.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0150** `line 29` | **narrative-meta** | **high** | heading/context: `\chapter{Derived structures and the geometric Langlands correspondence}`\
  Snippet: \begin{remark}[Periodicity frontier]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0151** `line 37` | **narrative-meta** | **high** | heading/context: `\chapter{Derived structures and the geometric Langlands correspondence}`\
  Snippet: frontier.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0152** `line 704` | **status-conjectured** | **high** | heading/context: `\subsection{The periodic CDG structure}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0153** `line 798` | **narrative-meta** | **high** | heading/context: `\subsection{Evidence for periodicity}`\
  Snippet: \begin{remark}[Scope boundary for periodicity]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0154** `line 815` | **meta-heading** | **critical** | heading/context: `\section{Kazhdan--Lusztig from bar-cobar: chain-level adjunction and periodic frontier}`\
  Snippet: \section{Kazhdan--Lusztig from bar-cobar: chain-level adjunction and periodic frontier}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0155** `line 933` | **status-conjectured** | **high** | heading/context: `\section{Kazhdan--Lusztig from bar-cobar: chain-level adjunction and periodic frontier}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0156** `line 938` | **narrative-meta** | **high** | heading/context: `\section{Kazhdan--Lusztig from bar-cobar: chain-level adjunction and periodic frontier}`\
  Snippet: programme-level Kazhdan--Lusztig recovery on the semisimplified target\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0157** `line 951` | **narrative-meta** | **high** | heading/context: `\section{Kazhdan--Lusztig from bar-cobar: chain-level adjunction and periodic frontier}`\
  Snippet: $\mathrm{Rep}^{\mathrm{fd}}(U_q(\fg))$ is an additional frontier,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0158** `line 1044` | **narrative-meta** | **high** | heading/context: `\subsection{Roadmap: from critical level to KL}`\
  Snippet: programme (critical level, opers) to the representation-theoretic\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0159** `line 1045` | **narrative-meta** | **high** | heading/context: `\subsection{Roadmap: from critical level to KL}`\
  Snippet: Langlands programme (admissible level, quantum groups) through\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0160** `line 1055` | **meta-heading** | **critical** | heading/context: `\section{Connections to the geometric Langlands programme}`\
  Snippet: \section{Connections to the geometric Langlands programme}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0161** `line 1059` | **meta-heading** | **critical** | heading/context: `\subsection{The Frenkel--Gaitsgory programme}`\
  Snippet: \subsection{The Frenkel--Gaitsgory programme}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0162** `line 1109` | **narrative-meta** | **high** | heading/context: `\subsection{From opers to Hecke eigensheaves}`\
  Snippet: $G^\vee$-local systems on~$X$.  The Frenkel--Gaitsgory programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0163** `line 1184` | **narrative-meta** | **high** | heading/context: `\section{Summary}`\
  Snippet: programmes: geometric Langlands (Programme~I), the KL equivalence\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0164** `line 1185` | **narrative-meta** | **high** | heading/context: `\section{Summary}`\
  Snippet: (Programme~II), and fusion product preservation (Programme~III).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0165** `line 1187` | **narrative-meta** | **high** | heading/context: `\section{Summary}`\
  Snippet: complex---that unifies these apparently disparate research\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/en_koszul_duality.tex`
- **I0146** `line 840` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{The $n = 3$ case: Chern--Simons theory}{The n = 3 case: Chern--Simons theory}}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0147** `line 861` | **narrative-meta** | **high** | heading/context: `\section{\texorpdfstring{The $n = 3$ case: Chern--Simons theory}{The n = 3 case: Chern--Simons theory}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0148** `line 920` | **narrative-meta** | **high** | heading/context: `\section{Summary and the dimensional ladder}`\
  Snippet: Remark~\ref{rem:en-scope}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/filtered_curved.tex`
Current chapter pages: 753-764
- **I0142** `line 154` | **narrative-meta** | **high** | heading/context: `\subsection{When does filtering degenerate to curved?}`\
  Snippet: infinite-generator programme.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0143** `line 157` | **narrative-meta** | **high** | heading/context: `\subsection{When does filtering degenerate to curved?}`\
  Snippet: $W_N$ algebras to the $W_\infty$/Yangian frontier recorded in\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/higher_genus.tex`
Current chapter pages: 361-556
- **I0051** `line 76` | **narrative-meta** | **high** | heading/context: `\chapter{Higher genus}`\
  Snippet: extension of~\S\ref{sec:modular-koszul-programme} articulates\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0052** `line 77` | **narrative-meta** | **high** | heading/context: `\chapter{Higher genus}`\
  Snippet: the higher-genus programme.  The condition $\kappa = 0$ is simultaneously the mathematical condition for the bar complex to be uncurved and the physical condition for anomaly cancellation.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0053** `line 5109` | **narrative-meta** | **high** | heading/context: `\subsection{Strategy of proof: overview}`\
  Snippet: While each ingredient is classical, their synthesis to prove\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0054** `line 6484` | **status-heuristic** | **high** | heading/context: `\subsection{Corollaries and physical interpretation}`\
  Snippet: \begin{conjecture}[Physical interpretation; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0055** `line 6509` | **narrative-meta** | **high** | heading/context: `\subsection{Corollaries and physical interpretation}`\
  Snippet: \begin{remark}[Scope of Conjecture~\ref{conj:physical-complementarity}]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0056** `line 6510` | **status-heuristic** | **high** | heading/context: `\subsection{Corollaries and physical interpretation}`\
  Snippet: This corollary is labeled \ClaimStatusHeuristic{} because a complete proof requires:\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0057** `line 6516` | **narrative-meta** | **high** | heading/context: `\subsection{Corollaries and physical interpretation}`\
  Snippet: as a chiral Koszul pair, which is beyond the scope of this monograph.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0058** `line 6776` | **status-heuristic** | **high** | heading/context: `\subsection{Self-dual algebras and critical level}`\
  Snippet: \begin{conjecture}[String theory interpretation; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0059** `line 6793` | **narrative-meta** | **high** | heading/context: `\subsection{Self-dual algebras and critical level}`\
  Snippet: \begin{remark}[Scope of Conjecture~\ref{conj:string-theory-complementarity-explicit}]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0060** `line 6794` | **status-heuristic** | **high** | heading/context: `\subsection{Self-dual algebras and critical level}`\
  Snippet: This corollary is labeled \ClaimStatusHeuristic{} because:\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0061** `line 8886` | **status-conjectured** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \begin{remark}[Extended axioms; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0062** `line 8919` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: the Stratum~II programme (Remark~\ref{rem:two-strata}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0063** `line 9161` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: and the distinct three-packet non-principal orbit frontier\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0064** `line 9421` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: $n=3,4,5,6$ and remain zero in the staged $n=7$ frontier run.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0065** `line 9993` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \begin{remark}[Scope of the universal PBW theorem]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0066** `line 10027` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: of the non-principal orbit programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0067** `line 10044` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: completion scaffold of \S\ref{sec:modular-koszul-programme} is the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0068** `line 10593` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \begin{remark}[Scope of Theorem~\ref{thm:explicit-theta}]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0069** `line 10882` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: of the MC2 programme at Step~1.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0070** `line 11082` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: Proposition~\ref{prop:mc2-reduction-principle}, the live MC2 frontier\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0071** `line 11303` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: (\S\ref{sec:modular-koszul-programme}, axiom~\ref{MK:clutching-verdier}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0072** `line 14084` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \begin{remark}[Frontier consequence for MC2]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0073** `line 14087` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: three-package frontier:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0074** `line 14578` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: (Future~7) have not been computed explicitly for any\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0075** `line 14626` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \begin{remark}[Scope of scalar saturation and its frontier]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0076** `line 14661` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \emph{The genuine frontier: coupled multi-parameter families.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0077** `line 14691` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: programme~\cite{ACL19}, reducing to a one-parameter family.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0078** `line 14791` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: A careful analysis of this frontier reveals a three-stratum\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0079** `line 14815` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: these are the genuine frontier.  Such algebras have primary\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0080** `line 14826` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: Thus the frontier of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0081** `line 15384` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \begin{remark}[Scope and significance of cyclic rigidity]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0082** `line 15430` | **status-conjectured** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \ClaimStatusConjectured\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0083** `line 15471` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \begin{remark}[Evidence and frontier of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0084** `line 15929` | **narrative-meta** | **high** | heading/context: `\subsection{Modular Koszul chiral algebras: the definition}`\
  Snippet: \S\ref{sec:modular-koszul-programme}.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/hochschild_cohomology.tex`
Current chapter pages: 765-778
- **I0144** `line 208` | **narrative-meta** | **high** | heading/context: `\subsection{$\mathcal{W}$-algebra periodicity}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0145** `line 768` | **meta-heading** | **critical** | heading/context: `\subsection{Summary and future directions}`\
  Snippet: \subsection{Summary and future directions}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Core Theory — `chapters/theory/introduction.tex`
Current chapter pages: 45-78
- **I0003** `line 328` | **narrative-meta** | **high** | heading/context: `\section{The four theorems}`\
  Snippet: The frontier is recorded in Chapter~\ref{chap:concordance}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0004** `line 329` | **narrative-meta** | **high** | heading/context: `\section{The four theorems}`\
  Snippet: and~\S\ref{sec:modular-koszul-programme}.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `chapters/theory/koszul_pair_structure.tex`
Current chapter pages: 607-634
- **I0092** `line 512` | **narrative-meta** | **high** | heading/context: `\subsection{Statement and first properties}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0093** `line 649` | **narrative-meta** | **high** | heading/context: `\subsection{Periodicity for other chiral algebras}`\
  Snippet: The synthesis for general simple~$\mathfrak{g}$ is new to this work.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0094** `line 819` | **status-conjectured** | **high** | heading/context: `\subsection{Periodicity for other chiral algebras}`\
  Snippet: \begin{definition}[Derived scalar period; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0095** `line 1285` | **status-conjectured** | **high** | heading/context: `\subsection{S-duality and Koszul duality}`\
  Snippet: \begin{conjecture}[Gaiotto-Witten S-duality, general case; \ClaimStatusConjectured]\label{conj:gw-s-duality}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0096** `line 1297` | **narrative-meta** | **high** | heading/context: `\subsection{S-duality and Koszul duality}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0097** `line 1305` | **narrative-meta** | **high** | heading/context: `\subsection{S-duality and Koszul duality}`\
  Snippet: \cite{GW09}) that is beyond the scope of this monograph.  On the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0098** `line 1762` | **narrative-meta** | **high** | heading/context: `\subsection{The precise connection}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0099** `line 1785` | **status-conjectured** | **high** | heading/context: `\subsection{Physical interpretation: quantum groups and Chern--Simons}`\
  Snippet: \begin{conjecture}[Witten--Reshetikhin--Turaev; \ClaimStatusConjectured]\label{conj:wrt-conjecture}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0100** `line 1789` | **narrative-meta** | **high** | heading/context: `\subsection{Physical interpretation: quantum groups and Chern--Simons}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0101** `line 1844` | **status-conjectured** | **high** | heading/context: `\subsection{The holographic interpretation}`\
  Snippet: \begin{conjecture}[AdS/CFT as Chern--Simons/Koszul duality; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0102** `line 1852` | **narrative-meta** | **high** | heading/context: `\subsection{The holographic interpretation}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0103** `line 1866` | **narrative-meta** | **high** | heading/context: `\subsection{The holographic interpretation}`\
  Snippet: frontier order, the theorematic input here is the boundary-side\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0104** `line 1928` | **status-heuristic** | **high** | heading/context: `\subsection{BV formalism}`\
  Snippet: \begin{remark}[Chern--Simons interpretation; \ClaimStatusHeuristic]\label{rem:cs-interp}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0105** `line 1950` | **meta-heading** | **critical** | heading/context: `\section{Open questions}`\
  Snippet: \section{Open questions}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Core Theory — `chapters/theory/poincare_duality_quantum.tex`
Current chapter pages: 681-752
- **I0129** `line 209` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{The AdS$_3$/CFT$_2$ example: twisted supergravity}{The AdS 3/CFT 2 example: twisted supergravity}}`\
  Snippet: \begin{conjecture}[Gravitational backreaction and deformation; \ClaimStatusConjectured]\label{conj:backreaction}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0130** `line 232` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{The AdS$_3$/CFT$_2$ example: twisted supergravity}{The AdS 3/CFT 2 example: twisted supergravity}}`\
  Snippet: This theorem is tagged \ClaimStatusConjectured: the $1/N$ expansion of\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0131** `line 239` | **narrative-meta** | **high** | heading/context: `\subsection{\texorpdfstring{The AdS$_3$/CFT$_2$ example: twisted supergravity}{The AdS 3/CFT 2 example: twisted supergravity}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0132** `line 240` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{The AdS$_3$/CFT$_2$ example: twisted supergravity}{The AdS 3/CFT 2 example: twisted supergravity}}`\
  Snippet: Conjecture~\ref{conj:backreaction} is tagged \ClaimStatusConjectured{} because\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0133** `line 291` | **narrative-meta** | **high** | heading/context: `\subsection{Physical interpretation: defects and open-closed duality}`\
  Snippet: Within the frontier order of this monograph, the theorematic content is\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0134** `line 369` | **meta-heading** | **critical** | heading/context: `\subsection{Applications and future directions}`\
  Snippet: \subsection{Applications and future directions}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0135** `line 884` | **status-conjectured** | **high** | heading/context: `\subsubsection{Operadic Koszul duality and the prism}`\
  Snippet: \begin{definition}[Modular graph coefficient algebra; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0136** `line 1101` | **status-conjectured** | **high** | heading/context: `\subsection{Holographic interpretation}`\
  Snippet: \begin{conjecture}[Holographic Koszul duality; \ClaimStatusConjectured]\label{conj:holographic-koszul}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0137** `line 1136` | **narrative-meta** | **high** | heading/context: `\subsection{Holographic interpretation}`\
  Snippet: \begin{remark}[Physical evidence and scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0138** `line 1140` | **status-conjectured** | **high** | heading/context: `\subsection{Holographic interpretation}`\
  Snippet: \ClaimStatusConjectured{} because the holographic identification of the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0139** `line 1148` | **narrative-meta** | **high** | heading/context: `\subsection{Holographic interpretation}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0140** `line 1149` | **status-conjectured** | **high** | heading/context: `\subsection{Holographic interpretation}`\
  Snippet: Conjecture~\ref{conj:holographic-koszul} is tagged \ClaimStatusConjectured{}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0141** `line 1161` | **narrative-meta** | **high** | heading/context: `\subsection{Holographic interpretation}`\
  Snippet: physical input that we do not attempt to supply.  In the repo's frontier\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Core Theory — `main.tex`
- **I0566** `line 774` | **architecture** | **critical** | heading/context: `Part I opener`\
  Snippet: Part I opener\
  Action: Replace part opener with mathematical contract; remove status/frontier diction\
  Algorithm: ALG-C

### Complete Portraits — `chapters/examples/deformation_quantization.tex`
- **I0248** `line 110` | **status-conjectured** | **high** | heading/context: `\subsection{Operator product expansion as star product}`\
  Snippet: The higher-genus extension is conjectural (\ClaimStatusConjectured): it requires controlling the global obstructions in $H^2$ of the chiral Hochschild complex on $\overline{\mathcal{M}}_{g,n}$.  This remains open.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0249** `line 670` | **status-conjectured** | **high** | heading/context: `\subsection{AdS/CFT and holography}`\
  Snippet: \begin{conjecture}[Holographic duality; \ClaimStatusConjectured]\label{conj:deformation-holographic}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0250** `line 679` | **narrative-meta** | **medium** | heading/context: `\subsection{AdS/CFT and holography}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0251** `line 680` | **narrative-meta** | **medium** | heading/context: `\subsection{AdS/CFT and holography}`\
  Snippet: The mathematical content --- that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed by the bar complex via configuration space integrals --- is established in the preceding sections.  The interpretation as a bulk\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0252** `line 681` | **narrative-meta** | **medium** | heading/context: `\subsection{AdS/CFT and holography}`\
  Snippet: In the monograph's frontier order, the theorematic input here is the boundary genus expansion itself; the open task is the downstream MC5 identification of that series with a bulk path integral, not any missing finite-ty\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0253** `line 1131` | **meta-heading** | **critical** | heading/context: `\section{Open questions}\label{sec:open-questions}`\
  Snippet: \section{Open questions}\label{sec:open-questions}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Complete Portraits — `chapters/examples/detailed_computations.tex`
- **I0344** `line 873` | **status-conjectured** | **high** | heading/context: `\subsection{Weight-decomposed modular rank}`\
  Snippet: (\ClaimStatusConjectured).\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Complete Portraits — `chapters/examples/examples_summary.tex`
- **I0571** `line 1` | **architecture** | **high** | heading/context: `Summary chapter title "Summary of Part XI"`\
  Snippet: Summary chapter title "Summary of Part XI"\
  Action: Normalize title and numbering to current volume architecture\
  Algorithm: ALG-I
- **I0345** `line 107` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: (\ClaimStatusProvedHere); CJ = conjectured (\ClaimStatusConjectured).\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0346** `line 145` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: Proposition~\ref{prop:winfty-mc4-frontier-package} packages this\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0347** `line 157` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: The remaining Yangian frontier is the staged DK-2--DK-5 ladder.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0348** `line 172` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: tower, Proposition~\ref{prop:yangian-dk4-typea-frontier} reduces that\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0349** `line 407` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: The individual synthesis remarks---Remark~\ref{rem:sl2-three-theorems}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0350** `line 618` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: setting --- would upgrade the value from \ClaimStatusConjectured{} to\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0351** `line 857` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: (\ClaimStatusConjectured): for any simple $\mathfrak{g}$, the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0352** `line 875` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: \ClaimStatusConjectured]\label{conj:ds-spectral-branch-preservation}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0353** `line 920` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: \begin{conjecture}[Kodaira--Spencer operator on reduced bar cohomology; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0354** `line 981` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0355** `line 1094` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: \begin{conjecture}[$\widehat{\mathfrak{sl}}_3$ bar generating function; \ClaimStatusConjectured]\label{conj:sl3-bar-gf}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0356** `line 1142` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: \emph{Scope.}  Independent verification requires computing $\dim H^4(\barBgeom(\widehat{\mathfrak{sl}}_{3,k}))$ directly from the chiral bar differential.  The value $1352$ would confirm the recurrence~\eqref{eq:sl3-bar-\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0357** `line 1147` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0358** `line 1243` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: following conjectural interpretation (\ClaimStatusConjectured): the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0359** `line 1246` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: (\S\ref{sec:modular-koszul-programme}).  The precise relationship\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0360** `line 2181` | **status-conjectured** | **high** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: \ClaimStatusConjectured\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0361** `line 2192` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: The scope of this extension is discussed in\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0362** `line 2210` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: three-theorem synthesis\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0363** `line 2229` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: three-theorem synthesis (Remark~\ref{rem:sl2-three-theorems}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0364** `line 2248` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: three-theorem synthesis\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0365** `line 2254` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: three-theorem synthesis\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0366** `line 2261` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: three-theorem synthesis\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0367** `line 2268` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: three-theorem synthesis\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0368** `line 2281` | **narrative-meta** | **medium** | heading/context: `\chapter*{Summary of Part XI}`\
  Snippet: The computations of Part~II are complete.  Part~III connects the bar-cobar framework to adjacent programs --- Feynman diagrams, BV-BRST, holomorphic-topological field theories, the 4d/2d correspondence --- and concludes \
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/free_fields.tex`
- **I0570** `line 2` | **architecture** | **high** | heading/context: `Generic chapter title "Examples"`\
  Snippet: Generic chapter title "Examples"\
  Action: Rename chapter to mathematical subject (e.g. Free field atoms or Free fields)\
  Algorithm: ALG-H
- **I0183** `line 327` | **status-conjectured** | **high** | heading/context: `\subsection{Derived completion and extended duality}`\
  Snippet: \begin{conjecture}[Extended fermion-ghost duality; \ClaimStatusConjectured]\label{conj:extended-ferm-ghost}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0184** `line 1582` | **status-conjectured** | **high** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: Virasoro & $W_\infty$ & Curved & AdS$_3$/CFT$_2$ & \ClaimStatusConjectured \\\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0185** `line 1583` | **status-conjectured** | **high** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: $\mathcal{W}_N$ & Yangian $Y(\mathfrak{gl}_N)$ & Curved & Higher spin & \ClaimStatusConjectured \\\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0186** `line 1584` | **status-conjectured** | **high** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: Super-Virasoro & Super-$W_\infty$ & Curved & AdS$_3$ sugra & \ClaimStatusConjectured \\\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0187** `line 1619` | **status-conjectured** | **high** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: \item \emph{Conjectural} (\ClaimStatusConjectured): The H-level realizations Virasoro $\rightsquigarrow W_\infty$, $\mathcal{W}_N \rightsquigarrow Y(\mathfrak{gl}_N)$, and Super-Virasoro $\rightsquigarrow$ Super-$W_\infty$ remain conjectures motivated by physical considerations (higher-spin holography, integrable systems) and by the structure of the bar complex computations in this manuscript.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0188** `line 1621` | **narrative-meta** | **medium** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: For the Virasoro and principal $\mathcal{W}_N$ rows, the live frontier is no longer a vague infinite-generator existence problem: the standard principal-stage completed M-level packages are theorematic, and the remaining\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0189** `line 1641` | **narrative-meta** | **medium** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: Significant partial progress exists: the bar--semi-infinite identifications (Theorems~\ref{thm:bar-semi-infinite-km} and~\ref{thm:bar-semi-infinite-w}) establish that the bar complex of any Kac--Moody or W-algebra comput\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0190** `line 1645` | **narrative-meta** | **medium** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: \begin{remark}[Scope: conjectural table entries]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0191** `line 1646` | **narrative-meta** | **medium** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: The three conjectural Koszul duality identifications in the table above --- Virasoro $\leftrightarrow$ $W_\infty$, $\mathcal{W}_N \leftrightarrow Y(\mathfrak{gl}_N)$, and Super-Virasoro $\leftrightarrow$ Super-$W_\infty$\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0192** `line 1663` | **narrative-meta** | **medium** | heading/context: `\subsection{Koszul duality table}`\
  Snippet: This constrains the frontier in two layers.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0193** `line 2278` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{Explicit $A_\infty$ structure for $\mathcal{W}$-algebras}{Explicit A- structure for $\mathcal{W}$-algebras}}`\
  Snippet: cohomology; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0194** `line 2287` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{Explicit $A_\infty$ structure for $\mathcal{W}$-algebras}{Explicit A- structure for $\mathcal{W}$-algebras}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0195** `line 3867` | **status-conjectured** | **high** | heading/context: `\subsection{Worldsheet perspective: higher genus}`\
  Snippet: $g \geq 1$; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0196** `line 3882` | **narrative-meta** | **medium** | heading/context: `\subsection{Worldsheet perspective: higher genus}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0197** `line 3896` | **status-conjectured** | **high** | heading/context: `\subsection{Holographic duality via bar-cobar}`\
  Snippet: \begin{conjecture}[Bulk-boundary correspondence; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0198** `line 3948` | **status-conjectured** | **high** | heading/context: `\section{Holographic reconstruction via Koszul duality}`\
  Snippet: \begin{conjecture}[Bulk package from boundary shadow; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0199** `line 3966` | **status-conjectured** | **high** | heading/context: `\section{Holographic reconstruction via Koszul duality}`\
  Snippet: \begin{conjecture}[Holographic dictionary; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0200** `line 3985` | **narrative-meta** | **medium** | heading/context: `\section{Holographic reconstruction via Koszul duality}`\
  Snippet: \begin{remark}[Scope of holographic statements]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0201** `line 3987` | **status-conjectured** | **high** | heading/context: `\section{Holographic reconstruction via Koszul duality}`\
  Snippet: The holographic conjectures remain \ClaimStatusConjectured{} because they\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0202** `line 4040` | **status-conjectured** | **high** | heading/context: `\section{Quantum corrections and deformed Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0203** `line 4064` | **narrative-meta** | **medium** | heading/context: `\section{Quantum corrections and deformed Koszul duality}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0204** `line 4077` | **status-heuristic** | **high** | heading/context: `\section{Entanglement and Koszul duality}`\
  Snippet: \ClaimStatusHeuristic\\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0205** `line 4136` | **status-conjectured** | **high** | heading/context: `\section{String amplitudes via bar complex}`\
  Snippet: \ClaimStatusConjectured]\label{conj:string-amplitude}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0206** `line 4152` | **narrative-meta** | **medium** | heading/context: `\section{String amplitudes via bar complex}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0207** `line 4349` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{Modular invariance under $SL_2(\mathbb{Z})$}{Modular invariance under SL-2(Z)}}`\
  Snippet: algebras; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0208** `line 4375` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{Modular invariance under $SL_2(\mathbb{Z})$}{Modular invariance under SL-2(Z)}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/genus_expansions.tex`
- **I0332** `line 285` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \textup{(\ClaimStatusConjectured; physics;\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0333** `line 304` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \begin{conjecture}[$\mathcal{W}_3$ bar cohomology algebraicity; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0334** `line 324` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \emph{Scope.}  Verification requires computing $\dim H^5(\barBgeom(\mathcal{W}_3^k))$: the value $171$ would confirm the recurrence~\eqref{eq:w3-bar-recurrence}, while any other value would rule it out and point to a non\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0335** `line 327` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0336** `line 332` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \begin{conjecture}[Non-simply-laced discriminant; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0337** `line 342` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \emph{Scope.}  Even for $G_2$, only three data points are available.  The chain-group dimensions are $\dim(\mathfrak{g})^n \cdot (n{-}1)! = 14, 392, 5488$ for $n = 1, 2, 3$; the \emph{bar cohomology} dimensions are not y\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0338** `line 345` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0339** `line 350` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \begin{conjecture}[Yangian bar generating function; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0340** `line 366` | **status-conjectured** | **high** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: (\ClaimStatusConjectured): a ``constant'' contribution (from the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0341** `line 378` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \emph{Scope.}  Three data points do not uniquely determine the generating\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0342** `line 386` | **narrative-meta** | **medium** | heading/context: `\section{\texorpdfstring{$\mathcal{W}$-algebra free energy and Higgs bundles}{$\mathcal{W}$-algebra free energy and Higgs bundles}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0343** `line 2854` | **narrative-meta** | **medium** | heading/context: `\subsection{Koszul duality as duality of genera}\label{subsec:koszul-genera-duality}`\
  Snippet: (\S\ref{sec:modular-koszul-programme}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/heisenberg_eisenstein.tex`
- **I0209** `line 431` | **narrative-meta** | **medium** | heading/context: `\subsection{Modular weight computations for each genus}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/kac_moody_framework.tex`
- **I0210** `line 86` | **narrative-meta** | **medium** | heading/context: `\subsection{Strategy for explicit computation}`\
  Snippet: The computation proceeds through four stages: identify generators and conformal weights, compute OPEs via multi-residues on configuration spaces, extract quadratic relations from OPE associativity, and verify bar-cobar q\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0211** `line 987` | **status-conjectured** | **high** | heading/context: `\subsection{Drinfeld--Sokolov reduction}`\
  Snippet: (\ClaimStatusConjectured): geometric Langlands considerations indicate this\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0212** `line 1000` | **status-conjectured** | **high** | heading/context: `\subsection{Drinfeld--Sokolov reduction}`\
  Snippet: The principal case of Theorem~\ref{thm:w-algebra-koszul} is a manifestation of geometric Langlands duality: the exchange $\mathfrak{g} \leftrightarrow \mathfrak{g}^\vee$ of Langlands dual Lie algebras carries the principal nilpotent $f_{\mathrm{prin}}$ to its dual $f^\vee_{\mathrm{prin}}$, and the corresponding W-algebras --- quantum deformations of the Slodowy slices $\mathcal{S}_f$ and $\mathcal{S}_{f^\vee}$ --- are interchanged by Koszul duality.  That the bar-cobar adjunction produces the Langlands dual at critical level motivates a programme-level conjectural direction (\ClaimStatusConjectured): the chiral bar complex could provide a constructive approach to the geometric Langlands correspondence, building the dual D-modules on $\mathrm{Bun}_G$ from configuration space data on the curve (see \S\ref{sec:km-conformal-blocks} for the conformal block interpretation).\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0213** `line 1134` | **status-conjectured** | **high** | heading/context: `\subsection{Holographic duality}`\
  Snippet: \begin{conjecture}[Kac--Moody in holography; \ClaimStatusConjectured]\label{conj:km-holography}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0214** `line 1152` | **narrative-meta** | **medium** | heading/context: `\subsection{Holographic duality}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0215** `line 1162` | **narrative-meta** | **medium** | heading/context: `\subsection{Holographic duality}`\
  Snippet: string-theoretic input beyond the scope of this monograph.  The\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0216** `line 2673` | **meta-heading** | **critical** | heading/context: `\section{Research programmes}`\
  Snippet: \section{Research programmes}\
  Action: Remove research-programme block from example chapter\
  Algorithm: ALG-D
- **I0217** `line 2675` | **meta-heading** | **critical** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: \subsection{Kazhdan--Lusztig programme from bar-cobar duality}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0218** `line 2682` | **status-conjectured** | **high** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: (\ClaimStatusConjectured) to the Kazhdan--Lusztig\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0219** `line 2685` | **narrative-meta** | **medium** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: \begin{remark}[Programme: KL equivalence from bar-cobar]%\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0220** `line 2693` | **status-conjectured** | **high** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: \ClaimStatusConjectured]\label{conj:kl-periodic-cdg}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0221** `line 2706` | **status-conjectured** | **high** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: \ClaimStatusConjectured]\label{conj:kl-coderived}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0222** `line 2736` | **status-conjectured** | **high** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: \ClaimStatusConjectured]\label{conj:kl-braided}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0223** `line 2796` | **narrative-meta** | **medium** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: This programme would give a \emph{geometric} proof of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0224** `line 2837` | **status-conjectured** | **high** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: (\ClaimStatusConjectured): the CDG periodicity\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0225** `line 2868` | **narrative-meta** | **medium** | heading/context: `\subsection{Kazhdan--Lusztig programme from bar-cobar duality}`\
  Snippet: constitutes the monoidal component of the KL programme.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0226** `line 3051` | **narrative-meta** | **medium** | heading/context: `\subsection{The oper space at critical level: summary}`\
  Snippet: structure, and the Kazhdan--Lusztig programme, is developed in\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0227** `line 3106` | **narrative-meta** | **medium** | heading/context: `\subsection{Fusion monoidality for Kac--Moody modules}`\
  Snippet: conjecture and its relation to the Kazhdan--Lusztig programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0228** `line 3109` | **meta-heading** | **critical** | heading/context: `\section{Open questions}`\
  Snippet: \section{Open questions}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Complete Portraits — `chapters/examples/lattice_foundations.tex`
- **I0166** `line 2387` | **narrative-meta** | **medium** | heading/context: `\subsection{Explicit specializations}`\
  Snippet: (cf.\ Remark~\ref{rem:lattice:qg-programme}, Route~A).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0167** `line 2696` | **status-conjectured** | **high** | heading/context: `\subsection{Deformed Frenkel--Kac--Segal and quantum groups}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0168** `line 2804` | **narrative-meta** | **medium** | heading/context: `\subsection{Deformed Frenkel--Kac--Segal and quantum groups}`\
  Snippet: \begin{remark}[Quantum group identification programme]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0169** `line 2868` | **narrative-meta** | **medium** | heading/context: `\subsection{Deformed Frenkel--Kac--Segal and quantum groups}`\
  Snippet: programme, while the $N$-periodic representation theory of the quantum\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0170** `line 2887` | **narrative-meta** | **medium** | heading/context: `\subsection{Deformed Frenkel--Kac--Segal and quantum groups}`\
  Snippet: Remark~\ref{rem:lattice:qg-programme}: match the logarithmic\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0171** `line 3015` | **narrative-meta** | **medium** | heading/context: `\subsection{Master table of $\Eone$ examples}`\
  Snippet: connected to the MC4 programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0172** `line 3357` | **narrative-meta** | **medium** | heading/context: `\subsection{Factorization DK for lattice algebras}`\
  Snippet: \begin{remark}[The factorization DK programme from lattices]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0173** `line 3367` | **narrative-meta** | **medium** | heading/context: `\subsection{Factorization DK for lattice algebras}`\
  Snippet: The relationship to the Yangian DK programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0174** `line 3878` | **meta-heading** | **critical** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: \subsection{Bridge to the Yangian DK programme}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0175** `line 3881` | **narrative-meta** | **medium** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: programme (MC3, Conjecture~\ref{conj:master-dk-kl}) through\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0176** `line 3935` | **status-conjectured** | **high** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0177** `line 3989` | **narrative-meta** | **medium** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: falls outside its direct scope, but the KL equivalence provides\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0178** `line 4008` | **narrative-meta** | **medium** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: The three-route programme for the identification is described in\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0179** `line 4009` | **narrative-meta** | **medium** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: Remark~\ref{rem:lattice:qg-programme}.  The conjectural status of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0180** `line 4010` | **narrative-meta** | **medium** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: (ii) is the sole obstacle between the lattice programme and the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0181** `line 4014` | **narrative-meta** | **medium** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: \begin{remark}[Summary: the lattice DK programme]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0182** `line 4035` | **narrative-meta** | **medium** | heading/context: `\subsection{Bridge to the Yangian DK programme}`\
  Snippet: The lattice route is the most complete factorization DK programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/minimal_model_fusion.tex`
- **I0242** `line 302` | **narrative-meta** | **medium** | heading/context: `\subsection{Quantum dimensions and Verlinde formula check}`\
  Snippet: \emph{Remark on the S-matrix.} The S-matrix above uses the Virasoro modular data (products of sines $\sin(\pi r s'/p)$). For a genuine $W_3$ minimal model, the modular data requires $A_2$ weight labeling with two-compone\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/toroidal_elliptic.tex`
- **I0321** `line 9` | **narrative-meta** | **medium** | heading/context: `\chapter{Toroidal and elliptic algebras}`\
  Snippet: elliptic frontier splits into two directions that must not be\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0322** `line 28` | **narrative-meta** | **medium** | heading/context: `\chapter{Toroidal and elliptic algebras}`\
  Snippet: \begin{remark}[Two programme tracks]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0323** `line 35` | **narrative-meta** | **medium** | heading/context: `\chapter{Toroidal and elliptic algebras}`\
  Snippet: track~(b) is a separate higher-dimensional programme target.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0324** `line 118` | **status-conjectured** | **high** | heading/context: `\subsection{Definition}`\
  Snippet: \begin{conjecture}[Elliptic-curve toroidal realization; \ClaimStatusConjectured]\label{conj:toroidal-e1}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0325** `line 125` | **status-conjectured** | **high** | heading/context: `\subsection{Definition}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0326** `line 136` | **narrative-meta** | **medium** | heading/context: `\subsection{Definition}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0327** `line 138` | **status-conjectured** | **high** | heading/context: `\subsection{Definition}`\
  Snippet: is conjectural (\ClaimStatusConjectured).  The RTT presentation of\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0328** `line 222` | **status-conjectured** | **high** | heading/context: `\subsection{Koszul dual of the toroidal algebra}`\
  Snippet: \begin{conjecture}[Toroidal Koszul dual; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0329** `line 271` | **narrative-meta** | **medium** | heading/context: `\subsection{Koszul dual of the toroidal algebra}`\
  Snippet: At the frontier, this should be read as an extension statement rather\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0330** `line 391` | **status-conjectured** | **high** | heading/context: `\subsection{Felder's elliptic quantum group}`\
  Snippet: (\ClaimStatusConjectured; the missing ingredient\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0331** `line 692` | **narrative-meta** | **medium** | heading/context: `\subsection{Bar complex with theta functions}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/w_algebras_deep.tex`
- **I0243** `line 164` | **narrative-meta** | **medium** | heading/context: `\subsection{Non-principal nilpotents and the DS hierarchy}`\
  Snippet: \begin{remark}[Frontier discipline]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0244** `line 170` | **narrative-meta** | **medium** | heading/context: `\subsection{Non-principal nilpotents and the DS hierarchy}`\
  Snippet: the section is to isolate the mechanism that a future theorem must\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0245** `line 171` | **narrative-meta** | **medium** | heading/context: `\subsection{Non-principal nilpotents and the DS hierarchy}`\
  Snippet: globalize, not to blur that frontier into a single slogan.  Concretely,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0246** `line 488` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{$\mathcal{W}_{1+\infty}$ and the large-$N$ limit}{W(1+infinity) and the large-N limit}}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0247** `line 538` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{$\mathcal{W}_{1+\infty}$ and the large-$N$ limit}{W(1+infinity) and the large-N limit}}`\
  Snippet: \begin{remark}[Scope: higher spin gravity and minimal model holography]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `chapters/examples/w_algebras_framework.tex`
- **I0229** `line 152` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{The solution: curved $A_\infty$ Koszul duality}{The solution: curved A infty Koszul duality}}`\
  Snippet: \begin{conjecture}[W-algebra Koszul duality for general nilpotent; \ClaimStatusConjectured]\label{conj:w-orbit-duality}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0230** `line 161` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{The solution: curved $A_\infty$ Koszul duality}{The solution: curved A infty Koszul duality}}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0231** `line 180` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{The solution: curved $A_\infty$ Koszul duality}{The solution: curved A infty Koszul duality}}`\
  Snippet: frontier.  This orbit-indexed transport problem is distinct from the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0232** `line 197` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{The solution: curved $A_\infty$ Koszul duality}{The solution: curved A infty Koszul duality}}`\
  Snippet: The conjecture packages the non-principal frontier into a Type~II\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0233** `line 203` | **meta-heading** | **critical** | heading/context: `\subsection{$\mathcal{W}$-algebras for general nilpotent data and the orbit-indexed frontier}`\
  Snippet: \subsection{$\mathcal{W}$-algebras for general nilpotent data and the orbit-indexed frontier}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0234** `line 243` | **narrative-meta** | **medium** | heading/context: `\subsection{$\mathcal{W}$-algebras for general nilpotent data and the orbit-indexed frontier}`\
  Snippet: first non-principal theorematic evidence, and the remaining frontier is\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0235** `line 342` | **narrative-meta** | **medium** | heading/context: `\subsection{$\mathcal{W}$-algebras for general nilpotent data and the orbit-indexed frontier}`\
  Snippet: orbit-indexed non-principal transport frontier, not as a finite-packet\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0236** `line 2052` | **status-conjectured** | **high** | heading/context: `\subsection{4d gauge theory and AGT correspondence}`\
  Snippet: \begin{conjecture}[AGT correspondence --- W-algebra version; \ClaimStatusConjectured]\label{conj:agt-w-algebra}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0237** `line 2080` | **narrative-meta** | **medium** | heading/context: `\subsection{4d gauge theory and AGT correspondence}`\
  Snippet: \begin{remark}[Scope: AGT correspondence]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0238** `line 2082` | **narrative-meta** | **medium** | heading/context: `\subsection{4d gauge theory and AGT correspondence}`\
  Snippet: Proving this equality requires: (a) localization on the instanton moduli space $\mathcal{M}_{G,C_g}$ using Nakajima's quiver variety techniques, (b) identification of the localization contributions with W-algebra matrix \
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0239** `line 2359` | **narrative-meta** | **medium** | heading/context: `\subsection{Highest weight modules via Drinfeld--Sokolov reduction}`\
  Snippet: isomorphism; Remark~\ref{rem:zhu-koszul-scope}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0240** `line 2469` | **status-conjectured** | **high** | heading/context: `\subsection{Logarithmic $\mathcal{W}$-algebra modules}`\
  Snippet: As a conjectural extension (\ClaimStatusConjectured) of the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0241** `line 2500` | **meta-heading** | **critical** | heading/context: `\section{Open questions}`\
  Snippet: \section{Open questions}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Complete Portraits — `chapters/examples/yangians.tex`
- **I0254** `line 525` | **status-conjectured** | **high** | heading/context: `\subsection{Yangian modules and Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\label{conj:e1-genus-theory}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0255** `line 621` | **status-conjectured** | **high** | heading/context: `\subsection{Definition}`\
  Snippet: \begin{conjecture}[Shifted Yangian as $\Eone$-chiral; \ClaimStatusConjectured]\label{conj:shifted-yangian-e1}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0256** `line 629` | **narrative-meta** | **medium** | heading/context: `\subsection{Definition}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0257** `line 636` | **status-conjectured** | **high** | heading/context: `\subsection{Definition}`\
  Snippet: A conjectural extension (\ClaimStatusConjectured) is that the shifted case follows by an analogous argument using the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0258** `line 755` | **status-conjectured** | **high** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: The bridge claim is \ClaimStatusConjectured: the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0259** `line 765` | **status-conjectured** | **high** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0260** `line 847` | **narrative-meta** | **medium** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: standard way, higher tensor lengths cease to be a separate frontier.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0261** `line 1477` | **narrative-meta** | **medium** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: satisfied, so the Yangian finite-detection frontier reduces to the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0262** `line 1541` | **narrative-meta** | **medium** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: pairwise frontier of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0263** `line 1602` | **narrative-meta** | **medium** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: Yangian frontier on the fundamental line is the residue extraction at\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0264** `line 1641` | **narrative-meta** | **medium** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: Yangian frontier on the fundamental line is a two-channel scalar\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0265** `line 1687` | **narrative-meta** | **medium** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: Yangian frontier on the fundamental line may be checked on one ordered\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0266** `line 1772` | **narrative-meta** | **medium** | heading/context: `\subsection{Comparison with dg-shifted Yangians}`\
  Snippet: Yangian MC4 frontier.  The remaining open frontier is the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0267** `line 1829` | **status-conjectured** | **high** | heading/context: `\subsection{Definition}`\
  Snippet: \begin{conjecture}[CoHA as $\Eone$-chiral; \ClaimStatusConjectured]\label{conj:coha-e1}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0268** `line 1842` | **narrative-meta** | **medium** | heading/context: `\subsection{Definition}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0269** `line 1882` | **status-conjectured** | **high** | heading/context: `\subsection{Shifted Yangians and Coulomb branch algebras}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0270** `line 1898` | **narrative-meta** | **medium** | heading/context: `\subsection{Shifted Yangians and Coulomb branch algebras}`\
  Snippet: \begin{remark}[Scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0271** `line 1956` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{Cohomological Hall algebras as $\Eone$-chiral algebras}{Cohomological Hall algebras as E1-chiral algebras}}`\
  Snippet: \begin{conjecture}[CoHA--Yangian Koszul duality; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0272** `line 1970` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Cohomological Hall algebras as $\Eone$-chiral algebras}{Cohomological Hall algebras as E1-chiral algebras}}`\
  Snippet: \begin{remark}[Scope and evidence]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0273** `line 2844` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \begin{remark}[Verification of hypotheses and scope]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0274** `line 3165` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: scope of DK\@.  The factorization DK equivalence in its natural form\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0275** `line 3207` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: The following lemma constrains the scope of what finite-dimensional\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0276** `line 3258` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: (matching the proved scope);\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0277** `line 3880` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \textbf{Strategy} & \textbf{Reduces to} & \textbf{Scope} \\\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0278** `line 3914` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \ClaimStatusConjectured]\label{conj:mc3-sectorwise-all-types}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0279** `line 4099` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \subsubsection*{Beyond finite dimensions: the shifted-prefundamental programme}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0280** `line 4107` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: $\mathcal{O}^{\mathrm{sh}}$; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0281** `line 4131` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \begin{conjecture}[Shifted-prefundamental generation; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0282** `line 4203` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \begin{conjecture}[Pro-Weyl recovery of ordinary standards; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0283** `line 4221` | **status-conjectured** | **high** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \begin{conjecture}[DK on compacts, extended by completion; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0284** `line 4291` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: \begin{remark}[Corrected MC3 frontier]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0285** `line 4307` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: The remaining MC3 frontier therefore splits into two layers.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0286** `line 4373` | **narrative-meta** | **medium** | heading/context: `\subsection{\texorpdfstring{Yangian category $\mathcal{O}$ from bar-cobar duality}{Yangian category O from bar-cobar duality}}`\
  Snippet: Option~(b) is the deeper programme, with the Yangian analogue\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0287** `line 4703` | **status-conjectured** | **high** | heading/context: `\subsection{The staged ladder beyond the evaluation locus}`\
  Snippet: \ClaimStatusConjectured]\label{conj:full-derived-dk}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0288** `line 4817` | **narrative-meta** | **medium** | heading/context: `\subsection{The staged ladder beyond the evaluation locus}`\
  Snippet: The frontier decomposes into a theorem ladder:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0289** `line 5066` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \begin{remark}[Scope of ``unconditional'']\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0290** `line 5117` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \begin{remark}[Two proofs in type~$A$; scope comparison]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0291** `line 5152` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: Remark~\ref{rem:corrected-mc3-frontier}(b) ---\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0292** `line 5164` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: The two programmes are complementary:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0293** `line 5173` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: home for both programmes: the evaluation-generated core is the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0294** `line 5219` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0295** `line 5262` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: Proposition~\ref{prop:yangian-dk4-typea-frontier} are\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0296** `line 5279` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0297** `line 5485` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \emph{correct categorical context} for the full MC3 programme:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0298** `line 5497` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: Remark~\ref{rem:corrected-mc3-frontier}(b)\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0299** `line 5585` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: Remark~\ref{rem:corrected-mc3-frontier}(b) concern modules\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0300** `line 5619` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0301** `line 5682` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \begin{remark}[Tangent Lie algebra controls the extension programme]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0302** `line 5972` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0303** `line 6022` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: Proposition~\ref{prop:yangian-dk4-typea-frontier} verifies\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0304** `line 6059` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0305** `line 6073` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0306** `line 6084` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \begin{definition}[dg-shifted Yangian; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0307** `line 6097` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0308** `line 6166` | **status-conjectured** | **high** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0309** `line 6290` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: Thus, after DK-3, the genuinely analytic Yangian frontier on the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0310** `line 6327` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: Proposition~\ref{prop:yangian-dk4-typea-frontier}.  Let\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0311** `line 6384` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: After Proposition~\ref{prop:yangian-dk4-typea-frontier}, the remaining\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0312** `line 6422` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: theorematic RTT stages.  Proposition~\ref{prop:yangian-dk4-typea-frontier}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0313** `line 6438` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: frontier breaks into four concrete checks rather than one undifferentiated\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0314** `line 6459` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: bar-cobar package.  The live Yangian frontier is the stronger H-level\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0315** `line 6466` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: type-A tower, Proposition~\ref{prop:yangian-dk4-typea-frontier} reduces\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0316** `line 6506` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: frontier.  As in the \(\mathcal{W}_\infty\) case, the eventual-constancy\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0317** `line 6669` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: remaining Yangian H-level frontier is to construct a filtered\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0318** `line 6726` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: The remaining frontier is\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0319** `line 6730` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: $\Eone$-chiral bridge to the modular Koszul programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0320** `line 6731` | **narrative-meta** | **medium** | heading/context: `\subsection{$\infty$-categorical factorization Koszul duality}`\
  Snippet: (\S\ref{sec:modular-koszul-programme}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Complete Portraits — `main.tex`
- **I0567** `line 911` | **architecture** | **critical** | heading/context: `Part II opener`\
  Snippet: Part II opener\
  Action: Replace part opener with one-paragraph portrait contract; remove programme bleed\
  Algorithm: ALG-C

### Synthesis and Programmes — `appendices/coderived_models.tex`
- **I0564** `line 291` | **status-conjectured** | **medium** | heading/context: `\subsection{Relative curved models}`\
  Snippet: (\ClaimStatusConjectured) to embed fully faithfully into the eventual coderived category of curved\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0565** `line 308` | **status-conjectured** | **medium** | heading/context: `\subsection{Completed ambient for factorization algebras}`\
  Snippet: \begin{definition}[Completed chiral ambient; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `appendices/combinatorial_frontier.tex`
- **I0559** `line 363` | **status-conjectured** | **medium** | heading/context: `\subsection{Conjectured rational ($\mathfrak{sl}_3$ family)}`\
  Snippet: \begin{conjecture}[$\mathcal{W}_3$ bar cohomology generating function; \ClaimStatusConjectured]\label{conj:w3-bar-gf}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0560** `line 526` | **meta-heading** | **high** | heading/context: `\section{Open problems and the computational frontier}`\
  Snippet: \section{Open problems and the computational frontier}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0561** `line 780` | **status-conjectured** | **medium** | heading/context: `\subsection{Near-rationality of the Virasoro bar sequence}`\
  Snippet: \begin{conjecture}[Period-$6$ Pad\'e structure; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0562** `line 851` | **meta-heading** | **high** | heading/context: `\subsection{Updated frontier targets}`\
  Snippet: \subsection{Updated frontier targets}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Synthesis and Programmes — `appendices/nilpotent_completion.tex`
- **I0563** `line 10` | **meta-heading** | **high** | heading/context: `\chapter{Nilpotent-completion frontier for non-quadratic Koszul duality}`\
  Snippet: \chapter{Nilpotent-completion frontier for non-quadratic Koszul duality}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Synthesis and Programmes — `appendices/spectral_higher_genus.tex`
- **I0558** `line 63` | **status-conjectured** | **medium** | heading/context: `\subsection{Convergence and degeneration}`\
  Snippet: \begin{conjecture}[Superstring degeneration; \ClaimStatusConjectured]\label{conj:superstring-degeneration}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `chapters/connections/bv_brst.tex`
- **I0381** `line 358` | **status-conjectured** | **medium** | heading/context: `\subsection{Coupling to topological gravity}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0382** `line 1299` | **status-heuristic** | **medium** | heading/context: `\subsection{The holomorphic-topological boundary condition}`\
  Snippet: \begin{conjecture}[Bar-cobar from HT boundary; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0383** `line 1326` | **status-heuristic** | **medium** | heading/context: `\subsection{The holomorphic-topological boundary condition}`\
  Snippet: This conjecture is labeled \ClaimStatusHeuristic{} because it proposes a geometric\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0384** `line 1337` | **status-conjectured** | **medium** | heading/context: `\section{$\mathcal{W}$-algebras from Higgs branches}`\
  Snippet: W-algebra package is \ClaimStatusConjectured, while central-charge\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0385** `line 1342` | **status-conjectured** | **medium** | heading/context: `\subsection{\texorpdfstring{4d gauge theory $\to$ 2d $\mathcal{W}$-algebra}{4d gauge theory -> 2d $\mathcal{W}$-algebra}}`\
  Snippet: \begin{conjecture}[Costello--Gaiotto AGT; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0386** `line 1382` | **status-conjectured** | **medium** | heading/context: `\subsection{\texorpdfstring{4d gauge theory $\to$ 2d $\mathcal{W}$-algebra}{4d gauge theory -> 2d $\mathcal{W}$-algebra}}`\
  Snippet: This conjecture is labeled \ClaimStatusConjectured{} because the derivation\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0387** `line 1420` | **status-heuristic** | **medium** | heading/context: `\section{Quantum observables and BV integration}`\
  Snippet: \textup{(}\ClaimStatusHeuristic\textup{)}.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0388** `line 1431` | **status-heuristic** | **medium** | heading/context: `\subsection{BV path integral}`\
  Snippet: \begin{conjecture}[BV integration = bar-cobar pairing; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0389** `line 1477` | **status-heuristic** | **medium** | heading/context: `\subsection{BV path integral}`\
  Snippet: This conjecture is labeled \ClaimStatusHeuristic{} because the identification of the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0390** `line 1612` | **status-heuristic** | **medium** | heading/context: `\subsection{Quantum master equation}`\
  Snippet: \begin{conjecture}[Quantum master equation; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0391** `line 1621` | **status-heuristic** | **medium** | heading/context: `\subsection{Quantum master equation}`\
  Snippet: This conjecture is labeled \ClaimStatusHeuristic{} because the solution $S$ of\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0392** `line 1630` | **status-heuristic** | **medium** | heading/context: `\subsection{Quantum master equation}`\
  Snippet: \begin{conjecture}[BV quantization = bar-cobar duality; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `chapters/connections/concordance.tex`
- **I0572** `line 1` | **architecture** | **critical** | heading/context: `Concordance chapter as constitutional dossier`\
  Snippet: Concordance chapter as constitutional dossier\
  Action: Split literature concordance from status ledger; keep only reader-facing concordance in book\
  Algorithm: ALG-E
- **I0428** `line 8` | **narrative-meta** | **high** | heading/context: `\chapter{Concordance with primary literature}`\
  Snippet: dependency-ordered frontier\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0429** `line 12` | **narrative-meta** | **high** | heading/context: `\chapter{Concordance with primary literature}`\
  Snippet: (\S\ref{subsec:homotopy-templates}), and the nine-futures assessment\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0430** `line 13` | **narrative-meta** | **high** | heading/context: `\chapter{Concordance with primary literature}`\
  Snippet: (\S\ref{subsec:nine-futures}).  The status classifications, proof tiers,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0431** `line 28` | **narrative-meta** | **high** | heading/context: `\chapter{Concordance with primary literature}`\
  Snippet: structural frontier.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0432** `line 38` | **narrative-meta** | **high** | heading/context: `\chapter{Concordance with primary literature}`\
  Snippet: \item \emph{Dependency-ordered frontier.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0433** `line 41` | **narrative-meta** | **high** | heading/context: `\chapter{Concordance with primary literature}`\
  Snippet: Theorem~\ref{thm:mc2-full-resolution}).  The remaining frontier:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0434** `line 50` | **narrative-meta** | **high** | heading/context: `\chapter{Concordance with primary literature}`\
  Snippet: interface used by all programme chapters.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0435** `line 110` | **narrative-meta** | **high** | heading/context: `\section{Principal contributions}\label{sec:principal-contributions}`\
  Snippet: $\mathcal{W}_\infty$ realization retained as programme\textup{)},\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0436** `line 447` | **meta-heading** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0437** `line 452` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: resolved entry theorem together with a dependency-ordered frontier:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0438** `line 503` | **status-conjectured** | **critical** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \ClaimStatusConjectured{}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0439** `line 520` | **status-conjectured** | **critical** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \ClaimStatusConjectured{}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0440** `line 544` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: programme.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0441** `line 546` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \emph{The live MC4 frontier is therefore filtered H-level realization,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0442** `line 553` | **status-conjectured** | **critical** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \ClaimStatusConjectured{}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0443** `line 588` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: The master package maps to the nine futures\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0444** `line 589` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: (\S\ref{subsec:nine-futures}) as follows:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0445** `line 590` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Theorem~\ref{conj:master-pbw} $\to$ Future~2;\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0446** `line 591` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Theorem~\ref{conj:master-theta} $\to$ Futures~3, 4;\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0447** `line 592` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Corollary~\ref{cor:effective-quadruple} $\to$ Future~4\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0448** `line 594` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Theorem~\ref{thm:cyclic-rigidity-generic} $\to$ Future~4\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0449** `line 598` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Conjecture~\ref{conj:master-dk-kl} $\to$ Future~6;\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0450** `line 599` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Conjecture~\ref{conj:master-infinite-generator} $\to$ Future~3;\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0451** `line 600` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Conjecture~\ref{conj:master-bv-brst} $\to$ Future~9.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0452** `line 601` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Futures~1, 5, 7, 8 are resolved or reformulated independently of the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0453** `line 605` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \begin{remark}[Completion frontier crystallization]\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0454** `line 607` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: The completion frontier (Appendix~\ref{app:nilpotent-completion})\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0455** `line 620` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: (Remarks~\ref{rem:completion-convergence-frontier},\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0456** `line 621` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \ref{rem:completed-bar-cobar-frontier},\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0457** `line 622` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: \ref{rem:koszul-dual-characterization-frontier}) identify the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0458** `line 625` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: frontier from full theorematic standing.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0459** `line 649` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Remaining scope: genus-$0$ Koszulness~(MK1) and\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0460** `line 685` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: (Remark~\ref{rem:corrected-mc3-frontier}(b)).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0461** `line 706` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: standard type-A Yangian tower, Proposition~\ref{prop:yangian-dk4-typea-frontier}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0462** `line 913` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: See Remark~\ref{rem:corrected-mc3-frontier} for the precise\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0463** `line 914` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: two-layer frontier.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0464** `line 919` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Proof route: three-stage programme---periodic CDG from admissible-level\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0465** `line 933` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: the Yangian programme at level~$1$.  The full MC3 via lattices\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0466** `line 941` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Three external programmes bear directly on the MC3 frontier:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0467** `line 975` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: The live MC4 frontier is therefore the H-level comparison between these\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0468** `line 987` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: frontier: Conjecture~\ref{conj:winfty-factorization-package} asks for a\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0469** `line 1009` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: The frontier has now been sharpened once again:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0470** `line 1045` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: The frontier can now be stated mode by mode.  On the Yangian side,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0471** `line 1064` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: The frontier is now finite at each stage $N$.  On the Yangian side,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0472** `line 1120` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: remains the live frontier.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0473** `line 1152` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: then isolates the exact mixed higher-spin frontier: the only genuinely\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0474** `line 1166` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: stage-$4$ frontier is therefore four free coefficient channels,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0475** `line 1177` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Proposition~\ref{prop:winfty-mc4-frontier-package} packages this\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0476** `line 1178` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: entire W-side dependency chain into one exact MC4 frontier statement:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0477** `line 1259` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: remain the sharp frontier for the $\mathcal{W}_\infty$ side of MC4.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0478** `line 1270` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: the common categorical framework for both programmes.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0479** `line 1293` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: Below we organize the full conjectural frontier into attack fronts,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0480** `line 1429` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: beyond this manuscript's scope.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0481** `line 1456` | **narrative-meta** | **high** | heading/context: `\subsection{Resolved Entry Theorem and Dependency-Ordered Frontier}`\
  Snippet: (Stratum~I) from the full programme (Stratum~II).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0482** `line 1624` | **narrative-meta** | **high** | heading/context: `\subsection{Homotopy templates for conjectures}`\
  Snippet: Each individual conjecture in the monograph carries a scope remark\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0483** `line 1633` | **meta-heading** | **high** | heading/context: `\section{Research programmes}`\
  Snippet: \section{Research programmes}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0484** `line 1779` | **narrative-meta** | **high** | heading/context: `\subsection{Higher-dimensional Koszul duality}`\
  Snippet: \emph{Step~4: Synthesis.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0485** `line 1799` | **status-conjectured** | **critical** | heading/context: `\subsection{Vassiliev invariants from Feynman transform}`\
  Snippet: \ClaimStatusConjectured]\label{conj:vassiliev-bar}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0486** `line 1970` | **status-conjectured** | **critical** | heading/context: `\subsection{Anomaly cancellation and Koszul structure}`\
  Snippet: \ClaimStatusConjectured]\label{conj:anomaly-physical}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0487** `line 2016` | **status-conjectured** | **critical** | heading/context: `\subsection{\texorpdfstring{AdS$_3$/CFT$_2$ as curved Koszul duality}{AdS3/CFT2 as curved Koszul duality}}`\
  Snippet: \ClaimStatusConjectured]\label{conj:ads-cft-bar}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0488** `line 2081` | **narrative-meta** | **high** | heading/context: `\subsection{\texorpdfstring{AdS$_3$/CFT$_2$ as curved Koszul duality}{AdS3/CFT2 as curved Koszul duality}}`\
  Snippet: This synthesis is now achieved for Kac--Moody and W-algebras:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0489** `line 2095` | **status-conjectured** | **critical** | heading/context: `\subsection{\texorpdfstring{3d mirror symmetry from $\Eone$-chiral Koszul duality}{3d mirror symmetry from E1-chiral Koszul duality}}`\
  Snippet: \ClaimStatusConjectured]\label{conj:3d-mirror}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0490** `line 2198` | **status-conjectured** | **critical** | heading/context: `\subsection{Noncommutative Hodge theory from genus tower}`\
  Snippet: \ClaimStatusConjectured]\label{conj:nc-hodge}\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0491** `line 2226` | **meta-heading** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: \subsection{The nine programmes: synthesis and interdependence}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0492** `line 2230` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: Programmes~I (higher-dimensional Koszul duality,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0493** `line 2233` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: as common foundation, but diverge in application: Programme~I\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0494** `line 2235` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: space integrals on $n$-manifolds, while Programme~II specializes\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0495** `line 2237` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: the Kontsevich integral.  At $n = 3$, the two programmes converge:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0496** `line 2241` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: Vassiliev weight systems of Programme~II\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0497** `line 2244` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: The anomaly cancellation programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0498** `line 2250` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: AdS$_3$/CFT$_2$ programme (\S\ref{subsec:ads-cft-koszul}), where\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0499** `line 2255` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: The $3$d mirror symmetry programme (\S\ref{subsec:3d-mirror})\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0500** `line 2262` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: The noncommutative Hodge programme (\S\ref{subsec:nc-hodge})\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0501** `line 2267` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: This programme depends on the complementarity theorem\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0502** `line 2274` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: All of the programmes above are facets of a single conjecture:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0503** `line 2313` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: \S\ref{sec:modular-koszul-programme} below.  For the status of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0504** `line 2314` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: each programme-level aspiration, see\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0505** `line 2315` | **narrative-meta** | **high** | heading/context: `\subsection{The nine programmes: synthesis and interdependence}`\
  Snippet: \S\ref{subsec:nine-futures}.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0506** `line 2391` | **narrative-meta** | **high** | heading/context: `\subsection{The coderived Ran-space formalism}`\
  Snippet: provides a working substitute within the scope of this monograph.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0507** `line 2791` | **narrative-meta** | **high** | heading/context: `\subsection{The discriminant as spectral invariant}`\
  Snippet: \emph{Synthesis.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0508** `line 2803` | **narrative-meta** | **high** | heading/context: `\subsection{The discriminant as spectral invariant}`\
  Snippet: \begin{remark}[Scope and verification]%\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0509** `line 2867` | **status-conjectured** | **critical** | heading/context: `\subsection{The discriminant as spectral invariant}`\
  Snippet: \begin{definition}[Spectral branch object; \ClaimStatusConjectured]\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0510** `line 3181` | **narrative-meta** | **high** | heading/context: `\subsection{The index theorem for genus expansions}`\
  Snippet: \S\ref{sec:modular-koszul-programme} and is the subject of\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0511** `line 3247` | **status-conjectured** | **critical** | heading/context: `\subsection{Chain-level / evaluation-locus derived Drinfeld--Kohno}`\
  Snippet: \ClaimStatusConjectured]\
  Action: Move constitutional conjectural status-tracking to editorial afterword/notes\
  Algorithm: ALG-E
- **I0512** `line 3265` | **narrative-meta** | **high** | heading/context: `\subsection{Chain-level / evaluation-locus derived Drinfeld--Kohno}`\
  Snippet: The Yangian frontier is best read as a DK ladder:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0513** `line 3328` | **narrative-meta** | **high** | heading/context: `\subsection{Summary}`\
  Snippet: The following subsection tracks the status of the nine programme-level\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0514** `line 3331` | **narrative-meta** | **high** | heading/context: `\subsection{Summary}`\
  Snippet: Remark~\ref{rem:nine-futures-summary}).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0515** `line 3333` | **meta-heading** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \subsection{Programme status: nine futures}\label{subsec:nine-futures}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0516** `line 3337` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: programme-level aspirations, each advertised in earlier stages of the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0517** `line 3346` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~1: All-genus $H^1(\mathcal{M}_g)$-parameterized\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0518** `line 3378` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~2: Modular Koszul programme.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0519** `line 3386` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: The status table on p.~\pageref{sec:modular-koszul-programme}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0520** `line 3394` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: (\S\ref{subsec:coderived-ran}), belonging to Future~3 below.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0521** `line 3398` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~3: Modular homotopy theory for factorization\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0522** `line 3407` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: This future is the mature endpoint of the project.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0523** `line 3465` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~4: Universal modular characteristic hierarchy.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0524** `line 3487` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: (Future~7).  Under the nilpotence-periodicity correspondence\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0525** `line 3565` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: conjectural (Future~7).  The boundary-extended depth on\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0526** `line 3661` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~5: Index-theoretic explanation of genus\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0527** `line 3678` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: class) remains open and requires Future~3.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0528** `line 3682` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~6: Derived Drinfeld--Kohno and quantum\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0529** `line 3696` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: frontier is ordered rather than undifferentiated:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0530** `line 3731` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \textup{(}Remark~\ref{rem:corrected-mc3-frontier}(b)\textup{)}.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0531** `line 3743` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: Proposition~\ref{prop:yangian-dk4-typea-frontier}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0532** `line 3764` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: Thus Future~6 is no longer one frontier theorem.  DK-0/DK-1 are proved,\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0533** `line 3923` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: The remaining MC3 frontier splits into two layers.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0534** `line 3932` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: (Remark~\ref{rem:corrected-mc3-frontier}(a)).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0535** `line 3937` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: modules (Remark~\ref{rem:corrected-mc3-frontier}(b)).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0536** `line 3950` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~7: Periodicity and tautological depth.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0537** `line 4012` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: packages remain frontier statements and should not be used as already\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0538** `line 4034` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: principal remaining programme-level target; the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0539** `line 4040` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~8: Spectral discriminant geometry.}\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0540** `line 4077` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: promote Future~8 from a spectral statement to a categorical one:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0541** `line 4084` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \noindent\textbf{Future~9: BV/BRST/path-integral/holography\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0542** `line 4105` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: four-clause synthesis: bar = BRST, curvature = anomaly, genus\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0543** `line 4108` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: The higher-genus programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0544** `line 4113` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: conjectural.  The holographic duality programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0545** `line 4117` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: Future~3's higher-dimensional shadow.\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0546** `line 4123` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: Of the nine programme-level aspirations:\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0547** `line 4128` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \textbf{\#} & \textbf{Future} & \textbf{Status} \\\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0548** `line 4131` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: 2 & Modular Koszul programme & \textbf{Largely realized} \\\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0549** `line 4161` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: (Future~5), a spectral characteristic package (Futures~4, 8), and a\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0550** `line 4163` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: (Future~6).  It is no longer becoming a single theorematic theory\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0551** `line 4165` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: parameters (Future~1, superseded) or a sharp global periodicity\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0552** `line 4166` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: theorem (Future~7, stratified).  These older self-images have been\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0553** `line 4180` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: programme-level aspirations of Futures~3, 6, and~9.  We tabulate\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0554** `line 4214` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: The MC4 W-infinity stabilization programme\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0555** `line 4255` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: \emph{Status:} conjectural (research).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0556** `line 4264` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: (Future~9).\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I
- **I0557** `line 4270` | **narrative-meta** | **high** | heading/context: `\subsection{Programme status: nine futures}\label{subsec:nine-futures}`\
  Snippet: (Remark~\ref{rem:completion-frontier-crystallization}(H3)) for the\
  Action: Prune internal-project vocabulary from running prose\
  Algorithm: ALG-I

### Synthesis and Programmes — `chapters/connections/feynman_connection.tex`
- **I0380** `line 362` | **status-conjectured** | **medium** | heading/context: `\subsection{Path integral interpretation}`\
  Snippet: \begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `chapters/connections/feynman_diagrams.tex`
- **I0371** `line 76` | **status-heuristic** | **medium** | heading/context: `\subsection{Tree vs.\ loop decomposition}`\
  Snippet: \begin{conjecture}[Configuration space interpretation; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0372** `line 112` | **status-heuristic** | **medium** | heading/context: `\subsection{Off-shell vs.\ on-shell}`\
  Snippet: \begin{conjecture}[Bar = off-shell amplitudes; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0373** `line 154` | **status-heuristic** | **medium** | heading/context: `\subsection{Distributional interpretation}`\
  Snippet: \begin{conjecture}[Cobar / on-shell propagator template; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0374** `line 198` | **status-heuristic** | **medium** | heading/context: `\subsection{The pairing: residue meets distribution}`\
  Snippet: \begin{conjecture}[Physical pairing; \ClaimStatusHeuristic]\label{conj:physical-pairing}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0375** `line 240` | **status-heuristic** | **medium** | heading/context: `\subsection{Feynman rules from bar-cobar}`\
  Snippet: \begin{conjecture}[Feynman rules dictionary; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0376** `line 289` | **status-heuristic** | **medium** | heading/context: `\subsection{\texorpdfstring{The $A_\infty$ structure as perturbative expansion}{The A infty structure as perturbative expansion}}`\
  Snippet: \begin{conjecture}[Loop expansion = $A_\infty$ operations; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0377** `line 410` | **status-heuristic** | **medium** | heading/context: `\subsection{The graph complex}`\
  Snippet: \begin{conjecture}[Bar complex and graph complex; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0378** `line 948` | **status-heuristic** | **medium** | heading/context: `\subsection{\texorpdfstring{The $A_\infty$ relations as recursion formula}{The A infty relations as recursion formula}}`\
  Snippet: \begin{conjecture}[BPHZ recursion = $A_\infty$ consistency; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0379** `line 1052` | **status-heuristic** | **medium** | heading/context: `\subsection{Worldline formalism: configuration spaces as Feynman graphs}`\
  Snippet: \begin{conjecture}[Bar complex and worldline integrals; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `chapters/connections/genus_complete.tex`
- **I0421** `line 378` | **status-conjectured** | **medium** | heading/context: `\subsection{Topological recursion and computational methods}\label{subsec:recursion}`\
  Snippet: \begin{conjecture}[Eynard--Orantin recursion for bar complex; \ClaimStatusConjectured]\label{conj:EO-recursion}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0422** `line 404` | **status-conjectured** | **medium** | heading/context: `\subsection{Topological recursion and computational methods}\label{subsec:recursion}`\
  Snippet: \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0423** `line 507` | **status-heuristic** | **medium** | heading/context: `\subsection{Topological recursion and computational methods}\label{subsec:recursion}`\
  Snippet: Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0424** `line 511` | **status-conjectured** | **medium** | heading/context: `\subsection{Topological recursion and computational methods}\label{subsec:recursion}`\
  Snippet: Part~(c) remains \ClaimStatusConjectured{}: for a non-Koszul chiral\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0425** `line 572` | **status-conjectured** | **medium** | heading/context: `\subsection{Physical interpretation: strings and holography}\label{subsec:physics}`\
  Snippet: \begin{conjecture}[String amplitude = bar complex cohomology; \ClaimStatusConjectured]\label{conj:string-amplitude-bar}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0426** `line 620` | **status-conjectured** | **medium** | heading/context: `\subsection{Physical interpretation: strings and holography}\label{subsec:physics}`\
  Snippet: \begin{conjecture}[Holographic duality via bar-cobar; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0427** `line 675` | **meta-heading** | **high** | heading/context: `\subsection{Synthesis}\label{subsec:synthesis}`\
  Snippet: \subsection{Synthesis}\label{subsec:synthesis}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A

### Synthesis and Programmes — `chapters/connections/holomorphic_topological.tex`
- **I0393** `line 11` | **status-conjectured** | **medium** | heading/context: `\section{Mathematical relationships between frameworks}`\
  Snippet: genuine chirality \textup{(}\ClaimStatusConjectured\textup{)}.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0394** `line 45` | **status-conjectured** | **medium** | heading/context: `\subsection{From 4D gauge theory to 2D chiral algebras}`\
  Snippet: \begin{conjecture}[When does CL produce chiral algebras?; \ClaimStatusConjectured]\label{conj:CL-produces-chiral}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0395** `line 78` | **status-conjectured** | **medium** | heading/context: `\subsection{From 4D gauge theory to 2D chiral algebras}`\
  Snippet: \ClaimStatusConjectured\ because the three conditions\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0396** `line 124` | **status-conjectured** | **medium** | heading/context: `\subsection{Costello--Li conditions: from factorization to chiral}`\
  Snippet: \begin{conjecture}[CL chirality conditions for general $R$; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0397** `line 387` | **status-conjectured** | **medium** | heading/context: `\subsection{Chiral operad action}`\
  Snippet: \begin{conjecture}[Chiral operad from HCS; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0398** `line 432` | **status-conjectured** | **medium** | heading/context: `\section{Open-closed correspondence as bar-cobar duality}`\
  Snippet: full open-closed equivalence remain \ClaimStatusConjectured.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0399** `line 477` | **status-conjectured** | **medium** | heading/context: `\subsection{Open and closed sectors}`\
  Snippet: \begin{conjecture}[Closed-string cobar identification; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0400** `line 531` | **status-conjectured** | **medium** | heading/context: `\subsection{Factorization and dimensional reduction}`\
  Snippet: \begin{conjecture}[Factorization along dimension tower; \ClaimStatusConjectured]\label{conj:factorization-dim-tower}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0401** `line 586` | **status-conjectured** | **medium** | heading/context: `\section{$\mathcal{W}$-algebras from Hitchin moduli}`\
  Snippet: \ClaimStatusConjectured.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0402** `line 608` | **status-conjectured** | **medium** | heading/context: `\subsection{The Higgs branch and Hitchin system}`\
  Snippet: \begin{conjecture}[W-algebra from Hitchin; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0403** `line 793` | **status-heuristic** | **medium** | heading/context: `\subsection{Classical vs.\ quantum chiral algebras}`\
  Snippet: \begin{remark}[Physics interpretation; \ClaimStatusHeuristic]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0404** `line 919` | **status-conjectured** | **medium** | heading/context: `\subsection{Bar-cobar duality for $\mathcal{W}$-algebras}`\
  Snippet: at admissible levels \textup{[\ClaimStatusConjectured]}:\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0405** `line 926` | **status-conjectured** | **medium** | heading/context: `\subsection{Bar-cobar duality for $\mathcal{W}$-algebras}`\
  Snippet: at admissible levels \textup{[\ClaimStatusConjectured]}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0406** `line 998` | **status-conjectured** | **medium** | heading/context: `\subsection{Bar-cobar duality for $\mathcal{W}$-algebras}`\
  Snippet: levels, the Koszul property remains \ClaimStatusConjectured{}: null\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0407** `line 1059` | **status-conjectured** | **medium** | heading/context: `\subsection{BV complex = geometric bar complex}`\
  Snippet: between the classical BV complex (Costello--Gwilliam~\cite{CG17}) and the geometric bar complex.  For non-free algebras, the precise equivalence remains conjectural (\ClaimStatusConjectured) and has not been fully established.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0408** `line 1148` | **status-conjectured** | **medium** | heading/context: `\subsection{AGT correspondence via bar-cobar}`\
  Snippet: \begin{conjecture}[AGT 4D--2D bridge via bar-cobar; \ClaimStatusConjectured]\label{conj:agt-bar-cobar}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0409** `line 1355` | **meta-heading** | **high** | heading/context: `\section{Open questions and future directions}`\
  Snippet: \section{Open questions and future directions}\
  Action: Retitle or relocate heading outside theorematic flow\
  Algorithm: ALG-A
- **I0410** `line 1418` | **status-conjectured** | **medium** | heading/context: `\section{Open questions and future directions}`\
  Snippet: conjectural bridge (\ClaimStatusConjectured): the bar complex\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `chapters/connections/kontsevich_integral.tex`
- **I0411** `line 376` | **status-conjectured** | **medium** | heading/context: `\section{Higher genus: from bar complex to loop expansion}`\
  Snippet: \ClaimStatusConjectured and is isolated as the only missing bridge.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0412** `line 401` | **status-conjectured** | **medium** | heading/context: `\section{Higher genus: from bar complex to loop expansion}`\
  Snippet: \item (\ClaimStatusConjectured) The passage from holomorphic propagators on complex curves\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0413** `line 450` | **status-conjectured** | **medium** | heading/context: `\section{Chern--Simons theory as the bridge}`\
  Snippet: \begin{conjecture}[CS factorization homology; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `chapters/connections/physical_origins.tex`
- **I0414** `line 46` | **status-conjectured** | **medium** | heading/context: `\section{Non-commutative Chern--Simons theory}`\
  Snippet: \ClaimStatusConjectured; the purpose is to state a precise target\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0415** `line 60` | **status-conjectured** | **medium** | heading/context: `\subsection{Chern--Simons as source of chiral algebras}`\
  Snippet: \begin{conjecture}[Non-commutative CS; \ClaimStatusConjectured]\label{conj:nc-cs}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0416** `line 128` | **status-conjectured** | **medium** | heading/context: `\subsection{\texorpdfstring{Noncommutative geometry and associative / topological $\mathsf{E}_1$ structures}{Noncommutative geometry and associative / topological E1 structures}}`\
  Snippet: \begin{conjecture}[Koszul duality as Morita equivalence; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0417** `line 179` | **status-conjectured** | **medium** | heading/context: `\subsection{D-brane vertex algebras}`\
  Snippet: \begin{conjecture}[D-brane algebras are $\Eone$; \ClaimStatusConjectured]\label{conj:dbrane-e1}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0418** `line 217` | **status-conjectured** | **medium** | heading/context: `\subsection{\texorpdfstring{D-brane categories from $\Eone$-module Koszul duality}{D-brane categories from E1-module Koszul duality}}`\
  Snippet: \begin{conjecture}[HMS from $\Eone$-module Koszul duality; \ClaimStatusConjectured]\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0419** `line 273` | **status-conjectured** | **medium** | heading/context: `\section{AGT correspondence connections}`\
  Snippet: nonlocal/associative remain \ClaimStatusConjectured.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0420** `line 296` | **status-conjectured** | **medium** | heading/context: `\section{AGT correspondence connections}`\
  Snippet: \begin{conjecture}[$q$-AGT; \ClaimStatusConjectured]\label{conj:q-agt}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `chapters/connections/poincare_computations.tex`
- **I0369** `line 13` | **status-conjectured** | **medium** | heading/context: `\section{Worked examples: standard Koszul pairs}`\
  Snippet: explicitly as \ClaimStatusConjectured.\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B
- **I0370** `line 93` | **status-conjectured** | **medium** | heading/context: `\subsection{Affine Kac--Moody at critical level}`\
  Snippet: \ClaimStatusConjectured]\label{conj:critical-affine-yangian}\
  Action: Fence, split, move, or prove conjectural/heuristic material\
  Algorithm: ALG-B

### Synthesis and Programmes — `main.tex`
- **I0568** `line 1065` | **architecture** | **critical** | heading/context: `Part III opener`\
  Snippet: Part III opener\
  Action: Compress to a short synthesis preface and push editorial meta to afterword/notes\
  Algorithm: ALG-C

### repo — `chapters/examples/deformation_quantization_complete.tex`
- **I0582** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/examples/heisenberg_higher_genus.tex`
- **I0580** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/examples/kac_moody_computations.tex`
- **I0578** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/examples/obstruction_classes.tex`
- **I0579** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/examples/w_algebras_computations.tex`
- **I0581** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/theory/bar_cobar_quasi_isomorphism.tex`
- **I0573** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/theory/classical_to_chiral.tex`
- **I0577** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % ARCHIVED: Content absorbed into introduction.tex (rem:three-level-dictionary). Not compiled.\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/theory/higher_genus_full.tex`
- **I0574** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/theory/higher_genus_quasi_isomorphism.tex`
- **I0575** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % Phase 0 overlap stub (2026-02-28).\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

### repo — `chapters/theory/koszul_across_genera.tex`
- **I0576** `line 1` | **legacy-stub** | **medium** | heading/context: `legacy snapshot`\
  Snippet: % ARCHIVED: Content absorbed into higher_genus.tex (§sec:koszul-across-genera). Not compiled.\
  Action: Remove from live tree or archive outside manuscript source root\
  Algorithm: ALG-F

## File-level counts

- `chapters/connections/concordance.tex` — 131 issues (architecture=1, narrative-meta=116, meta-heading=4, status-conjectured=10)
- `chapters/examples/yangians.tex` — 67 issues (status-conjectured=23, narrative-meta=44)
- `chapters/theory/bar_cobar_construction.tex` — 44 issues (narrative-meta=34, status-heuristic=4, status-conjectured=5, meta-heading=1)
- `chapters/theory/higher_genus.tex` — 34 issues (narrative-meta=28, status-heuristic=4, status-conjectured=2)
- `chapters/examples/free_fields.tex` — 27 issues (architecture=1, status-conjectured=14, narrative-meta=11, status-heuristic=1)
- `chapters/examples/examples_summary.tex` — 25 issues (architecture=1, status-conjectured=8, narrative-meta=16)
- `chapters/theory/deformation_theory.tex` — 20 issues (narrative-meta=10, status-conjectured=10)
- `chapters/examples/kac_moody_framework.tex` — 19 issues (narrative-meta=8, status-conjectured=8, meta-heading=3)
- `chapters/connections/holomorphic_topological.tex` — 18 issues (status-conjectured=16, status-heuristic=1, meta-heading=1)
- `chapters/theory/derived_langlands.tex` — 17 issues (narrative-meta=12, status-conjectured=2, meta-heading=3)
- `chapters/examples/lattice_foundations.tex` — 17 issues (narrative-meta=14, status-conjectured=2, meta-heading=1)
- `chapters/theory/koszul_pair_structure.tex` — 14 issues (narrative-meta=8, status-conjectured=4, status-heuristic=1, meta-heading=1)
- `chapters/theory/poincare_duality_quantum.tex` — 13 issues (status-conjectured=7, narrative-meta=5, meta-heading=1)
- `chapters/examples/w_algebras_framework.tex` — 13 issues (status-conjectured=3, narrative-meta=8, meta-heading=2)
- `chapters/examples/genus_expansions.tex` — 12 issues (status-conjectured=5, narrative-meta=7)
- `chapters/connections/bv_brst.tex` — 12 issues (status-conjectured=4, status-heuristic=8)
- `chapters/examples/toroidal_elliptic.tex` — 11 issues (narrative-meta=6, status-conjectured=5)
- `chapters/connections/feynman_diagrams.tex` — 9 issues (status-heuristic=9)
- `chapters/theory/chiral_koszul_pairs.tex` — 7 issues (narrative-meta=5, status-conjectured=2)
- `chapters/connections/physical_origins.tex` — 7 issues (status-conjectured=7)
- `chapters/connections/genus_complete.tex` — 7 issues (status-conjectured=5, status-heuristic=1, meta-heading=1)
- `chapters/examples/deformation_quantization.tex` — 6 issues (status-conjectured=2, narrative-meta=3, meta-heading=1)
- `chapters/examples/w_algebras_deep.tex` — 5 issues (narrative-meta=4, status-conjectured=1)
- `appendices/combinatorial_frontier.tex` — 4 issues (status-conjectured=2, meta-heading=2)
- `main.tex` — 3 issues (architecture=3)
- `chapters/theory/en_koszul_duality.tex` — 3 issues (status-conjectured=1, narrative-meta=2)
- `chapters/theory/chiral_modules.tex` — 3 issues (narrative-meta=3)
- `chapters/frame/heisenberg_frame.tex` — 3 issues (meta-heading=2, architecture=1)
- `chapters/connections/kontsevich_integral.tex` — 3 issues (status-conjectured=3)
- `chapters/theory/introduction.tex` — 2 issues (narrative-meta=2)
- `chapters/theory/hochschild_cohomology.tex` — 2 issues (narrative-meta=1, meta-heading=1)
- `chapters/theory/filtered_curved.tex` — 2 issues (narrative-meta=2)
- `chapters/connections/poincare_computations.tex` — 2 issues (status-conjectured=2)
- `appendices/coderived_models.tex` — 2 issues (status-conjectured=2)
- `chapters/theory/koszul_across_genera.tex` — 1 issues (legacy-stub=1)
- `chapters/theory/higher_genus_quasi_isomorphism.tex` — 1 issues (legacy-stub=1)
- `chapters/theory/higher_genus_full.tex` — 1 issues (legacy-stub=1)
- `chapters/theory/configuration_spaces.tex` — 1 issues (narrative-meta=1)
- `chapters/theory/classical_to_chiral.tex` — 1 issues (legacy-stub=1)
- `chapters/theory/bar_cobar_quasi_isomorphism.tex` — 1 issues (legacy-stub=1)
- `chapters/theory/algebraic_foundations.tex` — 1 issues (narrative-meta=1)
- `chapters/examples/w_algebras_computations.tex` — 1 issues (legacy-stub=1)
- `chapters/examples/obstruction_classes.tex` — 1 issues (legacy-stub=1)
- `chapters/examples/minimal_model_fusion.tex` — 1 issues (narrative-meta=1)
- `chapters/examples/kac_moody_computations.tex` — 1 issues (legacy-stub=1)
- `chapters/examples/heisenberg_higher_genus.tex` — 1 issues (legacy-stub=1)
- `chapters/examples/heisenberg_eisenstein.tex` — 1 issues (narrative-meta=1)
- `chapters/examples/detailed_computations.tex` — 1 issues (status-conjectured=1)
- `chapters/examples/deformation_quantization_complete.tex` — 1 issues (legacy-stub=1)
- `chapters/connections/feynman_connection.tex` — 1 issues (status-conjectured=1)
- `appendices/spectral_higher_genus.tex` — 1 issues (status-conjectured=1)
- `appendices/nilpotent_completion.tex` — 1 issues (meta-heading=1)