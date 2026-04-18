# Attack-and-heal: Seven Faces F6 (Sklyanin / STS83) — 2026-04-18

Author: Raeez Lorgat.

## Mission

Adversarial audit on Face 6 (Sklyanin / STS83 Poisson-Lie Yangian) of the
Seven Faces of r(z) programme. Locate the F6 standalone, verify inscription
depth, check main.tex `\input` wiring, check independence from F5 (Drinfeld).

## TL;DR verdict

No action on the manuscript. F6 is structurally sound. One prior wave
already covered this face (Wave 5, 2026-04-18, `wave5_seven_faces_vol_i_attack_heal.md`
row F6; also Wave 7, 2026-04-17, `wave7_seven_faces_attack_heal.md`). The only
residual drift is cosmetic: the dedicated F6 standalone file does NOT exist —
F6 content is consolidated in three loci. This is not a defect; it reflects
a deliberate programme choice to treat the seven faces as facets of a single
master theorem rather than seven separately-packaged standalones.

## 1. Inventory: where F6 actually lives

There is NO dedicated `standalone/seven_faces_F6_*.tex` file. Search for
`Sklyanin|STS83|Semenov-Tian-Shansky|Poisson-Lie` across the repo locates
F6 content at the following inscribed sites.

### Canonical chapter-level inscription (in build)

- `chapters/connections/holographic_datum_master.tex:549-625`
  - `§sec:hdm-face-6` titled "Face 6: the Sklyanin Poisson bracket of
    Semenov-Tian-Shansky".
  - `\begin{theorem}\label{thm:hdm-face-6}` at line 576, carrying split status
    `\ClaimStatusProvedHere` (identification of Sklyanin bracket with classical
    limit of the collision residue) + `\ClaimStatusProvedElsewhere`
    (the STS83 bracket construction itself).
  - Proof body at :593-619: four-step derivation. Step 1 constructs the
    antisymmetric part $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$ from
    $r^{\mathrm{Dr}} = k \Omega_{\mathrm{tr}}/z$ and identifies it with the
    residue at $z=0$. Step 2 takes the classical limit via Face 3 (Li
    filtration $\cA \to \mathrm{gr}^{\mathrm{Li}}(\cA)$). Step 3 matches
    the KZ-normalised collision residue $\Omega/((k+h^\vee)z)$ to the
    trace-form $k\Omega_{\mathrm{tr}}/z$ via the bridge identity. Step 4
    invokes Drinfeld's $\hbar \to 0$ theorem for the Yangian.
  - Sklyanin bracket equation `\label{eq:hdm-sklyanin-bracket}` at :557 with
    the full formula
    $\{f,g\}_{\mathrm{STS}}(\xi) = \langle \xi, [df, dg]_{r^{\mathrm{cl}}}\rangle$
    and the twisted-bracket definition
    $[X,Y]_{r^{\mathrm{cl}}} := [r^{\mathrm{cl}}(X), Y] + [X, r^{\mathrm{cl}}(Y)]$.
  - `\cite{STS83}` and `\cite{Drinfeld85}` both present.

- `chapters/connections/genus1_seven_faces.tex:868-899`
  - Elliptic Sklyanin bracket clause in the genus-1 master theorem.
  - F6 at genus 1 is NOT a separate theorem — `rem:g1sf-class-m-scope`
    at :916-930 explicitly acknowledges that F5-F7 specialize to affine
    Kac-Moody and do not have class-M analogues, and the class-M genus-1
    object is a genuinely new elliptic structure (`thm:g1sf-virasoro`,
    `thm:g1sf-wn`).
  - F2$^{(1)}$, F3$^{(1)}$, F6$^{(1)}$ are proved by elliptic regularization
    lifting from the genus-0 `thm:hdm-face-6` (:906-911).
  - This chapter IS `\input`-ed into main.tex at line 1811.

- `chapters/connections/frontier_modular_holography_platonic.tex:1672-1726`
  - `\begin{theorem}\label{thm:yangian-sklyanin-quantization}` at :1675,
    carrying mixed status: `\ClaimStatusProvedHere` on the new three-parameter
    identification + `\ClaimStatusProvedElsewhere` on classical STS83/Drinfeld
    content. This theorem is a SEPARATE Vol I result about the
    three-parameter identification of $\hbar = 1/(k+h^\vee)$ across KZ25
    sigma-model coupling, DNP25 loop parameter, and collision-residue
    prefactor. Proof body at :1703-1726 is non-vacuous, citing
    `\cite[\S 2.2]{KhanZeng25}`, `\cite[\S 3]{DNP25}`,
    `thm:collision-residue-twisting`, and the two classical papers. This is
    a genuinely new Vol I contribution that touches F6 without being a
    repackaging.

### Standalone-level inscription (orphan)

- `standalone/seven_faces.tex:341-347` (Sklyanin bracket as $E_\infty$
  shadow, prose framing); :421-431 (F5 $\Leftrightarrow$ F6 argument;
  references `thm:yangian-sklyanin-quantization` at :429); :1448 (status
  table row "F6 (Sklyanin bracket) | proved | cited | specialized | STS 1983");
  :1587 (STS83 bibliography entry).
  - This standalone is NOT `\input`-ed into main.tex (grep returns zero
    hits for `\input{standalone/seven_faces}`). Orphan. AP255 (phantom-file
    in terms of main-manuscript `\input` wiring) holds weakly — but the
    chapter-level inscription at `thm:hdm-face-6` is the canonical home,
    so cross-volume `\ref{thm:yangian-sklyanin-quantization}` consumers
    still resolve via the frontier-chapter inscription (which IS in build).

- `standalone/genus1_seven_faces.tex:868-871` (elliptic Sklyanin bracket,
  prose); also orphan; the corresponding chapter file
  `chapters/connections/genus1_seven_faces.tex` carries the same content
  and IS in build.

## 2. Per-question verdicts

### (i) Locate F6 standalone

VERDICT: no dedicated F6 standalone file exists. F6 lives in the
multi-face standalone `standalone/seven_faces.tex` (orphan) and the
multi-face chapter `chapters/connections/holographic_datum_master.tex`
(in build). The programme never allocated a per-face standalone at the
level of granularity the mission presupposes; all seven faces ship
together as a single paper.

### (ii) Verify F6 content

VERDICT: `thm:hdm-face-6` is inscribed with a genuine proof body (four
steps, non-prose, citing `eq:hdm-sklyanin-bracket`, `thm:hdm-face-3` for
the Li filtration, the $k\Omega_{\mathrm{tr}}/z = \Omega/((k+h^\vee)z)$
bridge identity, and `\cite{Drinfeld85}` for the $\hbar \to 0$ Yangian
classical limit). Status tag correctly split: the identification is
`\ClaimStatusProvedHere`; the STS83 Sklyanin bracket construction is
`\ClaimStatusProvedElsewhere`. AP60 respected.

### (iii) Main.tex `\input` wiring

VERDICT: `chapters/connections/holographic_datum_master.tex` is
`\input`-ed into main.tex indirectly via the Part-IV assembly chain;
`chapters/connections/genus1_seven_faces.tex` is directly `\input`-ed at
main.tex:1811; `chapters/connections/frontier_modular_holography_platonic.tex`
(housing `thm:yangian-sklyanin-quantization`) is also in build per
metadata. The standalones `standalone/seven_faces.tex` and
`standalone/genus1_seven_faces.tex` are both orphan (not `\input` into
main.tex). This is acceptable: standalones are submission-format
extracts, not chapters. AP255 applies to the orphan standalones only in
the sense that a reader opening a standalone pdf sees scope labels that
are compiled against main.tex labels; zero live-consumer `\ref{}` hits
to either standalone file from the chapters, so no `[?]` cascade at
build.

### (iv) Independence vs Drinfeld F5

VERDICT: genuinely independent framings, not repackaging.

- F5 (`thm:hdm-face-5`, :488-510) proves: the collision residue of
  $\Theta_{\widehat{\fg}_k}$ equals the Drinfeld $r$-matrix
  $r^{\mathrm{Dr}}(z) = k \Omega_{\mathrm{tr}}/z = \Omega/((k+h^\vee)z)$
  (bridge identity) as an element of $\fg \otimes \fg [\![z^{-1}]\!]$,
  and satisfies CYBE. Proof route: chiral-bar-complex derivation from
  $J^a J^b$ OPE; Casimir extraction via simple-pole coefficient; level
  Sugawara shift; Yang-Baxter inherited from the infinitesimal braid
  relation (`thm:collision-depth-2-ybe`).

- F6 (`thm:hdm-face-6`, :575-619) proves: the same Drinfeld $r$-matrix
  $r^{\mathrm{Dr}}$, viewed as a CLASSICAL $r$-matrix on $\fg$, defines
  a Poisson bracket on $\fg^*$ (the Sklyanin bracket) via the Lie-Poisson
  construction twisted by $\Omega$. Proof route: the STS83
  Poisson-geometric face — $r^{\mathrm{cl}}$ is a TENSOR generating a
  Poisson bracket, not a symbol in an OPE; the $\hbar \to 0$ limit of
  the Yangian coproduct commutator $[\Delta_\hbar(x), y \otimes 1]/\hbar$
  recovers the Sklyanin bracket.

The two faces are orthogonal framings of the SAME $r$-matrix: F5 is the
algebraic-CYBE face (operator-valued spectral function satisfying a
cohomological identity), F6 is the Poisson-geometric face (tensor
generating a Poisson structure on a phase space). Analogous distinction
to F1 (twisting-morphism face, categorical) vs F3 (PVA face, semiclassical
limit). The standalone seven-face master theorem at
`standalone/seven_faces.tex:363` states "the identification
$\mathrm{F5} \Leftrightarrow \mathrm{F6}$ is Drinfeld's and
Semenov-Tian-Shansky's classical result" — the equivalence between the
two faces is the substantive content that makes the seven-face assembly
a theorem rather than a taxonomy. F5 is the quantum/OPE face; F6 is the
classical/Poisson face; their equivalence is Drinfeld's quantisation
theorem.

## 3. Residuals

No APs fire at the new tier (AP1601-AP1620 block). Prior APs that
apply and were already addressed:

- AP255 (orphan standalone): `standalone/seven_faces.tex` and
  `standalone/genus1_seven_faces.tex` are orphans, previously catalogued
  under the Chiral QG equiv row and the genus1_seven_faces row. No
  `[?]` cascade because chapter-level inscription carries the live labels.

- AP60 (tag only genuinely new content ProvedHere): correctly respected
  at `thm:hdm-face-6` and `thm:yangian-sklyanin-quantization` via split
  status tags.

- Prior wave coverage: `adversarial_swarm_20260417/wave7_seven_faces_attack_heal.md`
  row at :42 already gave F6 an ACCEPT verdict; `adversarial_swarm_20260418/wave5_seven_faces_vol_i_attack_heal.md`
  row at :54 inventoried F6 with honest split-status accounting and zero
  open items. The present audit reproduces and confirms those verdicts.

## 4. Heal applied

None. No manuscript edit, no CLAUDE.md edit. This report is the audit
deliverable.

## 5. Mission coda

Mission presupposed a per-face standalone architecture that the programme
does not implement. The actual architecture: one multi-face standalone
paper (`seven_faces.tex`), one canonical chapter
(`holographic_datum_master.tex`), one companion chapter
(`frontier_modular_holography_platonic.tex`) housing the new
three-parameter $\hbar$ identification, and one genus-1 lift
(`genus1_seven_faces.tex`). Each face gets a named theorem and a section
header; F6 is fully inscribed at `thm:hdm-face-6` with non-vacuous proof
body, genuine split-status attribution to STS83 + Drinfeld85, and no
independence issue relative to F5.
