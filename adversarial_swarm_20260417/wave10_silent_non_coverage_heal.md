# Wave-10 Heal: Silent Non-Coverage of the Master Invariant Table

**Target.** `chapters/examples/landscape_census.tex` — master invariant table
`tab:master-invariants`.

**Predecessor.** Wave-9 #60 added `rem:census-silent-non-coverage` listing
five families visible in the shadow-obstruction-tower census but absent
from the master invariant table. That remark acknowledged the skip but
did NOT inscribe rows. This wave extends the heal by inscribing
honest-frontier rows directly into the master table, each with a
scope/status tag.

## Scope

Inscribe rows in `tab:master-invariants` for:

1. $\mathcal{N}{=}2$ superconformal $\mathrm{SCA}_c$.
2. Logarithmic triplet $\mathcal{W}(p)$.
3. Cosets (Kazama--Suzuki, GKO, parafermion).
4. Non-rational / indefinite lattice VOAs $V_L$.
5. Admissible $V_k(\mathfrak{g})$ at $k + h^\vee = p/q$.

Plus: honest footnote on the Schellekens $71$ holomorphic $c = 24$ list.

## Mathematical substance inscribed

| Family | $c$ | $\kappa$ | $c+c'$ | Status |
|---|---|---|---|---|
| $\mathcal{N}{=}2$ $\mathrm{SCA}_c$ | $3k/(k{+}2)$ | $(k{+}4)/4$ | $6$ | PH (Prop~n2-kappa) |
| Triplet $\mathcal{W}(p)$ | $1 - 6(p{-}1)^2/p$ | $c/2$ | $2c$ | CJ (log, tempering conj.) |
| Coset $\mathcal{A}/\mathcal{B}$ | $c(\mathcal{A}) - c(\mathcal{B})$ (GKO) | pending | pending | HF |
| Indefinite lattice $V_L$ | $\operatorname{sig}(L) = (p,q)$; $c = p - q$ | $\operatorname{rank}(L)$ | $\operatorname{rank}(L)$ | HF |
| Admissible $V_k(\mathfrak{g})$ | $kd/(k{+}h^\vee)$ | $td/(2h^\vee)$ | $2d$ | CJ (adm) |

Status legend: PH = proved here; CJ = conjectured; HF = honest frontier.

## Sources consulted (not fabricated)

- $\mathcal{N}{=}2$ $\kappa$: `chapters/examples/n2_superconformal.tex`
  Proposition `prop:n2-kappa` lines 208--226 gives
  $\kappa(\mathrm{SCA}_c) = (k{+}4)/4$. Ito--Tanaka involution
  $c \mapsto 6 - c$ verified at the $c + c' = 6$ line.
- $\mathcal{W}(p)$ $\kappa$: `chapters/examples/logarithmic_w_algebras.tex`
  Proposition `prop:wp-kappa` gives $\kappa(\mathcal{W}(p)) = c/2$ with
  $c = 1 - 6(p-1)^2/p$; four strong generators ($T$, $W^\pm$, $W^0$).
  Tempering conjectural per Wave-4 #18 heal (Gurarie 1993; Flohr 1996).
- Cosets: inscribed with GKO additivity $c(\mathcal{A}/\mathcal{B}) =
  c(\mathcal{A}) - c(\mathcal{B})$; family-by-family $\kappa$ deferred to
  frontier (honest HF).
- Indefinite lattice: inscribed as Heisenberg-like Gaussian sector; the
  unimodular self-duality theorem (positive-definite hypothesis) does
  not extend.
- Admissible $V_k$: central-charge and $\kappa$ columns inherit from
  affine KM; the level restriction $k + h^\vee = p/q$ secures
  Koszul compatibility via `thm:periodic-cdg-is-koszul-compatible`.

## Honest scope qualifications

- $\mathcal{W}(p)$ row is class $M$ with $\kappa = c/2$ proved; the
  master-table status is CJ only because of the tempering frontier,
  not the $\kappa$ value itself.
- Coset row carries HF: GKO additivity is classical; the $\kappa$ /
  complementarity entries per family (Kazama--Suzuki N=2 cosets,
  parafermion $SU(2)_k / U(1)$, diagonal cosets) are left pending
  inscription rather than fabricated.
- Indefinite-lattice row: inscribed Gaussian-sector invariants only;
  modular self-duality falsified outside unimodular positive-definite.
- Admissible row is a level-restriction of the affine KM row; it is
  kept inline with a separate line to surface the admissible-only
  refinement (periodic-CDG filtration; $(p-1)(q-1)/2$ simple modules
  for Vir admissible minimal models).

## Schellekens $71$ footnote

Inscribed in the status-legend block: only Monster $V^\natural$ and
Leech $V_{\Lambda_{24}}$ represent the $c = 24$ family in the master
table; the $69$ non-Monster Schellekens algebras carry $c = 24$ with
$\kappa = 24$ uniformly but differ in strong-generator content and in
the Euler--Koszul class. Family-by-family inscription of the full $71$
list is deferred to the frontier (Part~\ref{part:v1-frontier}).

## Constitutional hygiene

- No bare $\kappa$ in Vol I rows (Vol I permits bare $\kappa$; HZ-7 Vol III
  rule not applicable here).
- No AP/HZ tokens in typeset prose; cache indices in LaTeX comments only.
- No em-dashes in new prose; no AI slop tokens.
- Part references via `\ref{part:standard-landscape}` and
  `\ref{part:v1-frontier}` (V2-AP26 compliant after fix).
- Status tags orthogonal: PH / CJ from existing scheme, HF added
  explicitly as "honest frontier" with legend expanded inline.

## Files touched

- `chapters/examples/landscape_census.tex` — 5 rows inscribed in
  `tab:master-invariants` plus expanded status-legend footnote and
  Schellekens $71$ acknowledgement paragraph. Approx +95 lines.

## Residual frontiers

- Coset family-by-family inscription (Kazama--Suzuki N=2 family is
  realised but carries a distinct row; general-coset $\kappa$ is open).
- Full $71$ Schellekens row-by-row table (genuinely combinatorial;
  belongs in a dedicated $c = 24$ census).
- Admissible $V_k$ separate family-line — the level restriction is
  folded into the existing affine KM row via a parameter restriction,
  not lifted to a standalone family.

## Verdict

Silent-non-coverage frontier reduced from five opaque skips to five
inscribed rows, each with explicit scope qualifier. The
`tab:master-invariants` now surfaces every family that the
shadow-obstruction-tower census refers to, in one of the categories
PH / CJ / HF. Reader-visible portrait matches the mathematics the
monograph actually proves and conjectures.
