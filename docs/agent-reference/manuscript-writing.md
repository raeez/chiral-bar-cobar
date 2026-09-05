# Manuscript writing

Read for changes to reader-facing mathematics or physics.

## Writing standard: Chriss–Ginzburg north star

Manuscript prose channels the Russian elite school (Gelfand, Manin,
Drinfeld, Arnold, Beilinson, Bernstein, Kapranov, Etingof, Kazhdan,
Kontsevich, Soibelman, Bezrukavnikov) and the mathematical-physics
elite (Polyakov, Nekrasov, Witten, Costello, Gaiotto, Moore, Segal).
**Show don't tell.** Construct mathematics directly; the synthesis of
disparate technical domains brings out the unified structure.

**Forbidden in manuscript prose** (`chapters/`, `frame/`, `examples/`,
`theory/`, `connections/`, `bibliography/`, `appendices/`):

- *Bookkeeping vocabulary* — "Wave N", "round M", "batch K", "DNA
  strand", "AP$n$", "Pattern $n$", "cache entry $n$",
  "CG-rectify pass $k$", "$\mathsf{HZ}$-$n$ inscription". These
  belong in `notes/`, `FRONTIER.md`, commit messages, local
  `memory/` — never in the manuscript.
- *Meta-narration* — "we now turn to", "having established", "let us
  now", "this brings us to", "it is worth noting", "notably",
  "crucially", "remarkably", "furthermore", "moreover", "in the
  present work". Delete every instance; replace with direct
  mathematical statement.
- *Hedging the mathematics earns.* If $X = Y$ is proved, write
  $X = Y$; never "$X$ is closely related to $Y$". Courage, after
  Drinfeld and Polyakov: the equals sign is a theorem.

**Required**:

- Every section title names a mathematical object, construction,
  theorem, or question — never a process or meta-organising device.
- Introduce the mathematical question before its definition.
- Every symbol defined at or before first use, with parenthetical
  first-principles for standard concepts.
- Every physical claim labelled: theorem, heuristic, or metaphor.
  When a physical identification can be a theorem, state it as one;
  do not hide content as an "analogy".
- Economy. A paragraph that can be one sentence is one sentence.
- At a section boundary, state the mathematical dependency when the transition requires explanation.

The reader is an equal who sees the force of the argument when stated
with sufficient precision. The prose **is** mathematics, not
commentary on mathematics. Existing prose with bookkeeping vocabulary
is rectified through `/chriss-ginzburg-rectify`; new prose is in the
CG voice from the first keystroke.

## The manuscript is self-complete, self-coherent, self-consistent

Current version stands for itself. No references to previous versions,
intermediate ansätze, retracted values, superseded formulas, or
drafting-history commentary. If a formula was $X$ and is now $Y$, the
manuscript says $Y$; not "$Y$ (previously $X$)".

When a retraction is genuinely informative — a proof attempt whose
failure illuminates why the successful proof is forced — state the
failed argument and its flaw as mathematics: *"$[m_k, B^{(2)}] = 0$
fails per-$k$ because cyclic invariance controls adjacent contractions
but not non-adjacent terms (Proposition X)"*. Not "the author
initially attempted X". The mathematics is the Gap / Flaw, not the
drafting record.
