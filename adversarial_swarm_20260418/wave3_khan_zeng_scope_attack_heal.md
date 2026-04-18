# Wave 3 Attack-and-Heal: Khan-Zeng PVA Scope (CLAUDE.md B84)

Date: 2026-04-18. Voice: Chriss-Ginzburg fortification + Beilinson audit.
Target: CLAUDE.md B84 — "3d Poisson sigma model covers ALL freely-generated
PVAs with conformal vector. Check gr_Li(A) first." Primary inscription:
Vol II `chapters/connections/3d_gravity.tex:7041-7070`
(`thm:E3-topological-free-PVA`, `\ClaimStatusProvedHere`).

## 1. Attack ledger

### F1 (HIGH; AP272 folklore single-citation). `3d_gravity.tex:7050-7054`.
The proof body of `thm:E3-topological-free-PVA` delegates the entire
holomorphic-topological-to-fully-topological upgrade to a single citation
`\cite[Theorem~4.1]{KZ25}`. No bridge step, no local lemma verifying that
KZ25's hypothesis matches the programme's freely-generated-PVA-with-conformal-vector
input on the nose. KZ25 Theorem 2.1 (quoted at `hochschild.tex:88`) gives
the gauge-invariance↔λ-Jacobi equivalence; the "Theorem 4.1" cited for the
conformal-to-topological upgrade has no quoted statement anywhere in the
three volumes. Single-mechanism pillar for a `ProvedHere` theorem covering
the entire G/L/C/M landscape.

### F2 (HIGH; AP255 phantomsection mask + AP287 attribution discipline).
The theorem is tagged `\ClaimStatusProvedHere` but its proof chain is
(i) `\cite[Thm 4.1]{KZ25}` (external), (ii) `thm:general-half-space-bv`
(local, ProvedHere), (iii) `constr:topologization` (local). Step (i) is the
LOAD-BEARING reduction. Per AP60 + HZ-11 discipline, a theorem whose
decisive step is a single external citation should be `ProvedElsewhere`
with `\begin{remark}[Attribution]`, OR the KZ25 Thm 4.1 statement should
be inscribed locally as a `\begin{lemma}[After Khan--Zeng Theorem 4.1]`
with a proof sketch or quoted statement.

### F3 (HIGH; AP250 algorithm-uniformity + AP244 scope collapse).
`rem:E3-top-free-PVA-scope` at `3d_gravity.tex:7062-7070` asserts the
hypothesis is satisfied by "Kac--Moody $V_k(\mathfrak g)$ (class G),
Virasoro and $\mathcal W$-algebras (classes L and C), and matter-coupled
systems (class M)." Three drifts:

  (a) **Class-label drift.** CLAUDE.md fixes G = Heisenberg,
      L = affine KM, C = $\beta\gamma/bc$, M = Vir/$\mathcal W_N$.
      The scope remark labels KM as G, swaps L and C, and calls matter M.
      This is not a minor rename: the CLAUDE.md taxonomy carries depth
      semantics (G r=2, L r=3, C r=4, M r=$\infty$) and the scope remark
      silently redraws the partition.

  (b) **M = "matter-coupled systems" is undefined.** Standard class M
      (Vir, $\mathcal W_N$) has infinite-depth shadows from quartic poles.
      The scope remark's wording suggests M = matter, which either
      duplicates C or is a fifth class.

  (c) **Non-simply-laced exceptional DS reductions.** "principal $\mathcal W$"
      includes $\mathcal W(F_4)$, $\mathcal W(G_2)$. Khan-Zeng's free-PVA
      classification via De Sole-Kac-Valeri covers these, but the scope
      remark does not verify per-type (AP250).

### F4 (MEDIUM; AP241 advertised-but-not-inscribed).
CLAUDE.md B84 says "Check gr_Li(A) first." The programme has NO inscribed
decision procedure `prop:kz-admissibility-test` taking a conformal VA and
returning KZ-applicable yes/no. `prop:class-M-free-PVA` at
`e_infinity_topologization.tex:1165-1201` verifies Vir_c case-by-case;
$\mathcal W_N$ at N≥3 is asserted analogously but no lemma spells out
that gr_Li($\mathcal W_N$) is freely generated on N generators with
polynomial λ-brackets. The CLAUDE.md advisory "check first" has no
executable checklist.

### F5 (MEDIUM; AP149 resolution propagation).
Vol II CLAUDE.md FM82 → FM215 history: FM82 flagged class M as
INCOMPATIBLE with KZ; FM215 inscribed the Li-filtration heal;
`notes/first_principles_cache_comprehensive.md:2593` marks FM82 CLOSED.
But `3d_gravity.tex:7067` uses the informal word "matter-coupled" for
class M rather than routing through `prop:class-M-free-PVA`
(separate file, same chapter directory). The heal did not propagate
the SEMANTIC into the scope remark of the theorem.

### F6 (LOW; bibkey duplication, AP281 variant).
`main.tex:1945/1947` defines `KZ25` and `KZ2025` as duplicate bibitems to
arXiv:2502.13227. This is harmless at build time but is exactly the alias
drift behind the Vol I 87% phantom-citation rate (AP281). Flag for
future canonicalisation.

### F7 (LOW; AP288 stale narrative).
`notes/part_VI_climax_platonic_reconstitution.md:25`, `part_VII_frontier_platonic_reconstitution.md:53`,
`ROADMAP_85_TO_100.md:60` propagate "all freely-generated PVAs with
conformal vector PROVED via Khan-Zeng" without the class-M Li-filtration
caveat. Future agents reading these notes inherit an oversimplified scope.

## 2. Surviving core (Drinfeld-style)

What Khan-Zeng (arXiv:2502.13227) actually delivers: given a freely
generated Poisson vertex algebra $P$ on finitely many generators with
polynomial $\lambda$-bracket, there exists a 3d holomorphic-topological
Poisson sigma model on $X \times \mathbb{R}_{\geq 0}$ whose boundary
observables recover $P$; gauge invariance is equivalent to the
$\lambda$-Jacobi identity (KZ25 Thm 2.1). When the input carries a
conformal vector whose quantisation exists at non-critical level, the
3d theory admits a fully topological deformation. The programme inherits
this: for a conformal vertex algebra $\mathcal A$ whose Li-filtration
associated graded $\mathrm{gr}_{\mathrm{Li}}(\mathcal A)$ is freely
generated — a hypothesis that IS verified (Vir$_c$ by direct computation
via $F_3$-filtering the quartic $\lambda^3$-term; affine KM and principal
$\mathcal W_N$ by classical Arakawa and De Sole-Kac-Valeri) — the
Khan-Zeng 3d theory supplies the bulk and the derived chiral centre
carries an $E_3$-topological structure. Class M lives in the image
precisely because the Li filtration REMOVES the non-polynomial part
of the $\lambda$-bracket; "quartic pole incompatibility" (FM82)
confused the pre-filtration and the associated-graded brackets.

## 3. Heal (per finding)

- **F1**: Inscribe a local lemma `lem:kz25-conformal-upgrade` in
  `3d_gravity.tex` quoting KZ25 Theorem 4.1 verbatim
  (scope: freely-generated PVA, conformal vector, non-critical level;
  conclusion: 3d holomorphic-topological theory admits fully topological
  deformation). Retag `thm:E3-topological-free-PVA` to
  `\ClaimStatusProvedElsewhere` with `\begin{remark}[Attribution]`
  explicitly naming KZ25 Thm 4.1 as the load-bearing reduction, OR
  keep `ProvedHere` and add a paragraph verifying the hypothesis-match
  bridge. Status tag: `ProvedElsewhere` is the honest option.

- **F2**: Companion to F1. HZ-11 cross-volume attribution discipline
  applies VERTICALLY here (external source). `ProvedElsewhere` + remark
  is the heal.

- **F3**: Rewrite `rem:E3-top-free-PVA-scope` to match CLAUDE.md G/L/C/M
  taxonomy exactly: "G = Heisenberg, L = affine KM non-critical,
  C = $\beta\gamma/bc$, M = Virasoro and $\mathcal W_N$." For each,
  point to the explicit verification that $\mathrm{gr}_{\mathrm{Li}}$ is
  freely generated: G trivially (Heis IS its own associated graded);
  L via Arakawa 2017 (gr_Li($V_k(\mathfrak g)$) = $\mathrm{Sym}(\mathfrak g((t))/\mathfrak g[[t]])$);
  C via Frenkel-Ben-Zvi 2004 §3;
  M via `prop:class-M-free-PVA` (Vir) + per-type verification for
  $\mathcal W_N$ (principal ADE via Fateev-Lukyanov-Arakawa;
  $G_2, F_4$ per-case via De Sole-Kac-Valeri 2013).

- **F4**: Inscribe `prop:kz-admissibility-test` giving an explicit
  decision procedure: input $(\mathcal A, T)$; compute $\mathrm{gr}_{\mathrm{Li}}(\mathcal A)$;
  check (i) finite generation as PVA, (ii) freeness (no non-trivial
  $\lambda$-bracket relations among generators), (iii) descent of conformal
  vector to gr. If all three, KZ25 applies. State that the check fails for
  non-freely-generated targets: logarithmic $\mathcal W(p)$, symplectic
  fermions, lattice VAs at non-positive-definite lattices, Monster VOA
  (which routes via orbifold, `thm:monster-orbifold-e3`).

- **F5**: Ensure the corrected `rem:E3-top-free-PVA-scope` explicitly
  cross-references `prop:class-M-free-PVA` in `e_infinity_topologization.tex`
  so the two files agree on class-M coverage semantics. Cite by label, not
  by re-stating.

- **F6**: Note in the attack-heal ledger. Defer canonicalisation to
  the programme-wide bibkey pass (AP281 heal).

- **F7**: Append a dated correction to the three session notes
  stating: "KZ scope covers freely-generated PVAs; class M inclusion
  requires Li-filtration descent verified per-family (Vir: `prop:class-M-free-PVA`;
  $\mathcal W_N$: per-type verification required). Non-freely-generated
  VOAs (logarithmic, symplectic fermion, Monster direct) NOT covered."

## 4. Updated CLAUDE.md B84 line (draft)

Replace current:

> B84. Khan-Zeng scope: 3d Poisson sigma model covers ALL freely-generated
> PVAs with conformal vector. Check gr_Li(A) first.

With:

> B84 (2026-04-18 sharpened). Khan-Zeng arXiv:2502.13227 (KZ25) attaches a
> 3d holomorphic-topological Poisson sigma model to any freely generated
> PVA with polynomial $\lambda$-bracket (KZ25 Thm 2.1); with a conformal
> vector at non-critical level, the 3d theory admits a fully topological
> deformation (KZ25 Thm 4.1). Programme application (Vol II
> `thm:E3-topological-free-PVA`): a conformal VA $\mathcal A$ inherits
> an $E_3$-topological structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal A)$
> iff $\mathrm{gr}_{\mathrm{Li}}(\mathcal A)$ is freely generated and the
> conformal vector descends. Verified per-family: G (Heis, trivial),
> L (affine KM non-critical, Arakawa 2017), C ($\beta\gamma/bc$, FBZ04 §3),
> M (Vir via `prop:class-M-free-PVA`; principal $\mathcal W_N$ ADE via
> Fateev-Lukyanov-Arakawa; $G_2, F_4$ per-case via De Sole-Kac-Valeri).
> NOT covered: logarithmic $\mathcal W(p)$, symplectic fermions, lattice
> VAs at indefinite lattices, Monster VOA direct (routes via orbifold
> `thm:monster-orbifold-e3`). Tag discipline: the Vol II theorem citing
> KZ25 Thm 4.1 as load-bearing reduction should be
> `\ClaimStatusProvedElsewhere` with Remark[Attribution], not `ProvedHere`.

## 5. Commit plan

No commit produced in this agent run. Inscription deliverables for a
later pass:

1. `3d_gravity.tex:7041-7070` — add `lem:kz25-conformal-upgrade`;
   retag `thm:E3-topological-free-PVA` to `\ClaimStatusProvedElsewhere`
   (or inscribe hypothesis-match bridge) + rewrite scope remark to match
   G/L/C/M taxonomy.
2. `e_infinity_topologization.tex` — add `prop:kz-admissibility-test`;
   ensure cross-reference to `prop:class-M-free-PVA` from the scope
   remark in `3d_gravity.tex`.
3. CLAUDE.md B84 — replace as above.
4. `ROADMAP_85_TO_100.md`, `notes/part_VI_climax_platonic_reconstitution.md`,
   `notes/part_VII_frontier_platonic_reconstitution.md` — append dated
   correction flagging the Li-filtration caveat.
5. `main.tex:1947-1948` — canonicalise to single `KZ25` bibkey
   (folded into AP281 programme-wide pass).

Manuscript hygiene (AP metadata): none of the above touches `.tex`
manuscript prose with AP/HZ/FM slugs; CLAUDE.md update is on-charter.
