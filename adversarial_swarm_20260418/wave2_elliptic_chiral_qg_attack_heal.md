# Wave 2 (2026-04-18) — Elliptic chiral QG: AP275 propagator convention + AP255 orphan standalone

Adversarial channel: Etingof (theta vs zeta), Polyakov (CYBE as physics), Nekrasov (modular
correction), Kapranov (structure lives on the curve), Bezrukavnikov (universal objects),
Costello (factorization).

## ATTACK LEDGER

### (a) What the manuscript actually inscribes

Vol~I carries three elliptic propagator inscriptions. All three write the FULL Weierstrass
zeta, not the bare theta-derivative:

- `chapters/examples/yangians_drinfeld_kohno.tex:7310-7389` —
  `prop:elliptic-rmatrix-shadow` (ClaimStatusProvedHere). Proof derives
  $d\log E(z) = (\theta_1'(z|\tau)/\theta_1(z|\tau))\,dz$ at :7314, then
  explicitly adds the quasi-period correction at :7315-7318:
  "Adding the quasi-period correction $2\eta_1 z$ ... gives the Weierstrass zeta function
  $\zeta_\tau(z) = \theta_1'(z|\tau)/\theta_1(z|\tau) + 2\eta_1 z$." The
  r-matrix :7270-7278 uses $\zeta_\tau(z) \cdot H\otimes H/2$ in the Cartan channel.
  `rem:elliptic-rmatrix-scope` at :7364-7389 explicitly warns: "A common pitfall is to drop
  the quasi-period correction and write only the theta derivative $\theta_1'/\theta_1$: this
  form breaks the classical Yang--Baxter equation off the diagonal and is not the Belavin
  $r$-matrix."

- `chapters/examples/lattice_foundations.tex:4689-4715` — `prop:lattice:genus1-simple-pole`
  uses $\zeta_\tau(z_{ij}) + \frac{\pi}{\operatorname{Im}\tau}\operatorname{Im}(z_{ij})$
  (the Arakelov Green form, real-analytic globally well-defined on $E_\tau$). Residue
  structure inherits simple pole of $\zeta_\tau$ (not $\theta_1'/\theta_1$).

- `chapters/examples/heisenberg_eisenstein.tex:458-503` —
  `thm:heisenberg-genus-one-complete` uses
  $G_\tau(z) = \zeta_\tau(z) - (\pi^2 E_2(\tau)/3)\,z$, i.e. the Weierstrass zeta minus
  $2\eta_1 z$ (where $2\eta_1 = \pi^2 E_2(\tau)/3$). This is the torus-periodic repackaging;
  the underlying object is Weierstrass $\zeta_\tau$.

- `chapters/connections/genus1_seven_faces.tex:470-546` — Belavin elliptic r-matrix for
  $\fsl_2$ at :480-485 uses $\zeta_\tau(z)$ (not bare $\theta_1'/\theta_1$).

Conclusion: the manuscript is CONSISTENT with the convention
$\zeta_\tau(z) = \theta_1'(z|\tau)/\theta_1(z|\tau) + 2\eta_1 z$. The bare
$\theta_1'/\theta_1$ form does NOT appear as the propagator in ANY Vol~I chapter.

### (b) The AP275-inverted site: CLAUDE.md

CLAUDE.md theorem-status Elliptic chiral QG row line 629:
"θ_1'/θ_1 propagator (NOT Weierstrass ζ)."

This inverts the actual inscribed convention. A reader editing the manuscript to match this
CLAUDE.md line would INTRODUCE a Yang-Baxter bug (AP275/FM30): bare $\theta_1'/\theta_1$
is quasi-periodic, not periodic; the root-channel factors $\phi_\pm(z,\tau)$ and the
Cartan-channel $\zeta_\tau$ both rely on the $2\eta_1 z$ correction for CYBE off-diagonal.

### (c) The AP255-orphan site: standalone/seven_faces.tex

`standalone/seven_faces.tex:1005-1017` contains `thm:chiral-qg-equiv-elliptic-sf`,
`ClaimStatusProvedElsewhere`, with the SAME inverted prose: "the Felder dynamical
$R$-matrix ... built from the Jacobi theta derivative $\theta_1'/\theta_1$, not the
Weierstrass zeta; FM30". This is BACKWARD: FM30 is precisely the warning that the Belavin
form uses the FULL Weierstrass $\zeta_\tau = \theta_1'/\theta_1 + 2\eta_1 z$; dropping
$2\eta_1 z$ BREAKS CYBE. The current prose cites FM30 while REPRODUCING the bug FM30 warns
against.

File status:
- `grep -n seven_faces /Users/raeez/chiral-bar-cobar/main.tex` → zero hits for
  `standalone/seven_faces.tex` (only `chapters/connections/genus1_seven_faces.tex` at line
  1811).
- `thm:chiral-qg-equiv-elliptic-sf` / `thm:chiral-qg-equiv-toroidal-sf` are only in the
  orphan standalone. The unsuffixed labels `thm:chiral-qg-equiv-elliptic` and
  `thm:chiral-qg-equiv-toroidal-formal-disk` advertised by CLAUDE.md do NOT exist anywhere
  in Vol~I.
- `grep -rn 'ref\{thm:chiral-qg-equiv-elliptic\}\|ref\{thm:chiral-qg-equiv-toroidal-formal-disk\}' chapters/ standalone/ appendices/` →
  zero matches. There are no `\ref` consumers of either phantom label, so the orphan does
  NOT cause `[?]` rendering at build time; the phantoms are advertised only in CLAUDE.md
  and in session notes. Two secondary prose mentions (`standalone/genus1_seven_faces.tex:105`
  and `standalone/N3_e1_primacy.tex:1153`) typeset the label name in `\textup{\textsf{...}}`
  font, not as a cross-reference; they are bibliographic annotations, not ref consumers.

### (d) AP305 pessimistic-drift status

CLAUDE.md advertises "PROVED leading-order ℏ for sl_2 via Felder R + KZB + Fay trisecant".
What is ACTUALLY inscribed:
- Belavin elliptic r-matrix for $\fsl_2$: PROVED (ClaimStatusProvedHere) in both
  `yangians_drinfeld_kohno.tex` `prop:elliptic-rmatrix-shadow` and
  `chapters/connections/genus1_seven_faces.tex` `thm:g1sf-elliptic-rmatrix` at :470.
- Felder DYNAMICAL R-matrix equivalence to KZB at leading-order $\hbar$: NOT INSCRIBED in
  any chapter. `rem:elliptic-rmatrix-scope` at :7379-7388 explicitly labels Felder as "an
  open frontier addressed in the genus-one seven-faces standalone". The Felder R
  presentation only appears in the orphan `standalone/seven_faces.tex` with the inverted
  convention and in `chapters/connections/genus1_seven_faces.tex` as a SEVEN-FACE ITEM
  without the chiral-QG-equivalence theorem attached.
- Fay trisecant: Szegő three-term at $g \le 1$ is universal, mentioned in orphan only.
- Heat prefactor 1/(4πi) diag / 1/(2πi) off-diag: verified only in orphan
  `standalone/seven_faces.tex` + FM34a; no chapter-level theorem.

Conclusion: CLAUDE.md "PROVED" conflates TWO distinct claims: (i) Belavin elliptic r-matrix
— PROVED in chapters; (ii) Felder dynamical R ↔ KZB leading-order — INSCRIBED only in the
orphan standalone. The chiral-QG-equivalence label (Felder-with-KZB) is standalone-only and
the standalone itself carries the AP275 convention bug.

## SURVIVING CORE

At $\fsl_2$, on a smooth elliptic curve $E_\tau$ with $\operatorname{Im}\tau > 0$:
- The Belavin non-dynamical elliptic r-matrix $r^{\mathrm{ell}}_{\fsl_2}(z,\tau)$ PROVED
  as the collision residue of $\Theta_\cA$ on the genus-$1$ ordered bar, Cartan channel
  built from the FULL Weierstrass $\zeta_\tau(z) = \theta_1'/\theta_1 + 2\eta_1 z$, root
  channels from theta-function ratios $\phi_\pm(z,\tau)$, classical YBE verified at three
  parameter samples. This survives as Vol~I chapter-level ProvedHere. Dropping
  $2\eta_1 z$ breaks CYBE off-diagonal; the convention is not optional.
- Felder dynamical R-matrix $R(z,\lambda,\tau)$ and its ↔ KZB equivalence at leading-order
  $\hbar$ are INSCRIBED only in the orphan `standalone/seven_faces.tex` (non-input-ed).
  The chapter-level status is CONJECTURAL/FRONTIER, not PROVED.

## HEAL PLAN

1. CLAUDE.md Elliptic chiral QG row (line 629): rewrite from
   "θ_1'/θ_1 propagator (NOT Weierstrass ζ)" to
   "$\zeta_\tau(z) = \theta_1'/\theta_1 + 2\eta_1 z$ (full Weierstrass zeta;
   dropping $2\eta_1 z$ breaks CYBE off-diagonal, see FM30)."
   Demote "PROVED" to "BELAVIN r-matrix PROVED sl_2 chapter-level
   (`prop:elliptic-rmatrix-shadow`, `thm:g1sf-elliptic-rmatrix`); Felder↔KZB leading-order
   inscribed only in orphan `standalone/seven_faces.tex` (not `\input`-ed; phantom-in-chapters
   per AP255)".

2. CLAUDE.md Chiral QG equiv row: leave the Wave-5 language
   ("ELLIPTIC: NOT INSCRIBED") as the honest status; cross-reference the Belavin r-matrix
   (which IS chapter-inscribed) as the surviving core.

3. `standalone/seven_faces.tex:1005-1017`: rewrite `thm:chiral-qg-equiv-elliptic-sf` so
   that (a) the propagator convention is the FULL Weierstrass
   $\zeta_\tau = \theta_1'/\theta_1 + 2\eta_1 z$; (b) Belavin non-dynamical vs Felder
   dynamical is clearly separated (Belavin is the chapter-inscribed object; Felder is the
   dynamical face-model cousin obtained via vertex-IRF at $\fsl_2$); (c) FM30 citation
   warns against bare $\theta_1'/\theta_1$ rather than endorsing it; (d) the environment
   is downgraded from `\begin{theorem}` + `\ClaimStatusProvedElsewhere` to
   `\begin{conjecture}` + `\ClaimStatusConjectured` per AP40, with label renamed from
   `thm:chiral-qg-equiv-elliptic-sf` to `conj:chiral-qg-equiv-elliptic-sf` per AP125. Zero
   `\ref` consumers verified before rename.

4. No `\input` of `standalone/seven_faces.tex` into `main.tex` yet (AP305 honesty: the
   elliptic chiral-QG equivalence is not at ProvedHere publication standard; it is
   standalone-draft material). Update CLAUDE.md status row to reflect this rather than
   advertising a PROVED label.

No commit. Attack-and-heal ledger only.

## COMMIT PLAN

No commit. Edits applied in-session:
- `CLAUDE.md` lines near 629 (Elliptic chiral QG row).
- `standalone/seven_faces.tex:1005-1017` (elliptic chiral QG equivalence theorem prose).
- This note file.

Grep gate after edits:
- `grep -rn 'θ_1./θ_1.*NOT Weierstrass\|theta_1.*not the Weierstrass\|built from the Jacobi theta derivative' /Users/raeez/chiral-bar-cobar/ --include='*.md' --include='*.tex'` → zero hits required.
