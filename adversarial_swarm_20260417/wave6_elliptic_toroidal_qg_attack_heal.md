# Wave 6 — Elliptic + Toroidal Chiral QG Attack/Heal (Vol I)

Date: 2026-04-17. Operator: adversarial-mathematician agent.
Targets: `chapters/examples/yangians_drinfeld_kohno.tex` §7251–7389
(elliptic r-matrix from genus-1 shadow) and `chapters/examples/yangians_foundations.tex`
§3778–3905 (KZB, Felder, Fay, toroidal scope remark).

## Phase 1 findings.

1. **Belavin vs Felder presentation is HONEST in Vol I.**
   `prop:elliptic-rmatrix-shadow` (line 7251) inscribes the **Belavin**
   non-dynamical r-matrix (algebraic, uses full Weierstrass
   $\zeta_\tau = \theta_1'/\theta_1 + 2\eta_1 z$ per FM30). A separate
   definition `def:elliptic-yangian-felder` (line 3766) carries the
   **Felder dynamical** r-matrix with propagator $\theta_1'/\theta_1$
   alone and **explicit FM30 warning** that adding $2\eta_1 z$ to the
   dynamical form breaks dynamical YBE. Wave-2 scope remark
   `rem:elliptic-rmatrix-scope` (line 7364) correctly disambiguates:
   the chapter statement is Belavin at $\mathfrak{sl}_2$ leading-$\hbar$;
   Felder is distinct. CYBE verification upgraded to 3 independent
   non-degenerate sample points (line 7357–7361).

2. **Heat prefactor CORRECT per FM34a.** Line 3793–3796:
   "$1/(4\pi i)$ on the diagonal $a=b$ and $1/(2\pi i)$ off-diagonal;
   both arise from the symmetric-matrix chain rule on
   $\partial_{\Omega_{ab}}$." Matches AP/FM34a.

3. **Fay trisecant CORRECT at $g=1$** as three-theta relation (line
   3829–3833: $\theta_1(u+v)\theta_1(u-v)\theta_1(w)^2+\mathrm{cyc}=0$).
   Not confused with Szegő three-term. Fay also properly cited in
   `chiral_hochschild_koszul.tex:3315` at all genera via Szegő kernel.

4. **Toroidal Vol I chapter-level inscription: ABSENT, and the
   labels referenced were PHANTOM.** Two concrete phantoms:
   - `rem:toroidal-three-theorems` (referenced in `yangians_foundations.tex:1120`)
     is defined ONLY in Vol III
     (`~/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:395`),
     not in Vol I.
   - `conj:toroidal-two-param-coprod` (referenced in bare form at
     `yangians_foundations.tex:3901`) is NOWHERE defined, in any volume.
     `grep '\label{conj:toroidal-two-param-coprod}'` returns zero hits.
     The CLAUDE.md status table line "Toroidal coproduct | CONJECTURED |
     conj:toroidal-two-param-coprod" advertises a label that does not
     exist as an inscription.

   The chapter-level toroidal claim in Vol I was a **status-table
   promise with no target**: `thm:chiral-qg-equiv-toroidal-sf` lives
   in `standalone/seven_faces.tex:1020` (ClaimStatusProvedElsewhere)
   and in `standalone/N3_e1_primacy.tex:1160`; neither is a Vol I
   chapter inscription.

5. **SV CoHA = Miki DIM bridge** is not inscribed at chapter level;
   the standalone seven-faces theorem cites "Schiffmann–Vasserot
   cohomological Hall algebra on the instanton moduli space" without
   the Tsymbaliuk–Garbali transport citation. Not a Vol I blocker
   (toroidal is Vol III territory) but the Vol I cross-reference was
   broken.

6. **Global $\mathbb{P}^1 \times \mathbb{P}^1$ conditional on class-M
   chain-level** is stated correctly in `seven_faces.tex:1027–1029`
   and consistent with Wave-5 finding that class-M chain-level on the
   ORIGINAL complex is open; the weight-completed / J-adic / pro-object
   ambients are now proved (Wave-5), but the original-complex variant
   that the toroidal global extension would require remains open.

7. **Miki $S_3$ = Weyl of $\Omega$-background** not inscribed at
   chapter level in Vol I; Vol III chapter
   `k3_quantum_toroidal_chapter.tex` is the correct home.

## Phase 2 heals (surgical, in Vol I only).

Heal A — `chapters/examples/yangians_foundations.tex:1118–1122`
(was phantom `\ref{rem:toroidal-three-theorems}`):

    The toroidal algebra (the two-parameter double-loop
    extension $U_{q,t}(\ddot{\mathfrak{sl}}_N)$, treated in Vol III)
    faces the same obstruction.

Heal B — `chapters/examples/yangians_foundations.tex:3900–3905`
(was phantom bare-text `conj:toroidal-two-param-coprod`): replaced
the one-line stub with a full-paragraph scope statement naming the
toroidal datum (Ding–Iohara–Miki presentation, SV CoHA on instanton
moduli, Miki $S_3$ = Weyl($\Omega$-background) with
$q_1 q_2 q_3 = 1$), pointing the inscription at
`thm:chiral-qg-equiv-toroidal-sf` of `standalone/seven_faces.tex`,
and reaffirming that global $\mathbb{P}^1\times\mathbb{P}^1$ is
conditional on class-M chain-level on the ORIGINAL complex.

No other edits made. No new chapter file created: the toroidal
theorem's honest home is Vol III; creating a Vol I chapter-level
`toroidal_chiral_qg_formal_disk_platonic.tex` would duplicate Vol III
and inflate Vol I scope (AP-CY63/AP-CY64 territory).

## Residual open frontiers.

- OF6.a (Felder dynamical half of elliptic chiral QG): the chapter
  inscription is Belavin algebraic; Felder dynamical is a standalone
  statement leading-$\hbar$ only. Higher-order coherence and
  $E_3$-identification remain conjectural (`conj:elliptic-E3-identification`).
- OF6.b (Toroidal Vol I chapter inscription): Vol I deliberately
  does NOT carry a chapter-level toroidal theorem; it is Vol III
  content. The Vol I status-table line should be rewritten to cite
  the standalone label and the Vol III chapter, not a phantom
  Vol I label. (CLAUDE.md entry is informational, not inscribed.)
- OF6.c (SV CoHA = DIM bridge citation): Tsymbaliuk–Garbali transport
  not yet stated in standalone; Vol III `k3_quantum_toroidal_chapter.tex`
  is the correct locus.

## Voice audit.

Heal B now reads in Russian-school register (Etingof–Varchenko dynamical
YBE at g=1; Schiffmann–Vasserot CoHA; Miki–Tsymbaliuk DIM; Nekrasov
Ω-background). No AI slop, no em-dash (uses `---`), no hedging.

## Constitutional hygiene.

Post-write grep confirmed:
- Zero bare $\zeta(z) = \theta_1'/\theta_1 + 2\eta_1 z$ without
  FM30 context in the elliptic inscription: the Weierstrass form
  appears only in `prop:elliptic-rmatrix-shadow` (Belavin, correct)
  and `def:elliptic-yangian-felder` carries explicit "Weierstrass
  presentation forbidden here" warning.
- Zero AP references in manuscript typeset prose in my edits.
- No new AP24 violations introduced (hook-flagged pre-existing
  lines 72/118/1159 are properly scoped super-Yangian / Yangian-family
  contexts where $\kappa+\kappa^!=0$ is correct).
- No em-dash, no banned tokens, no Markdown.
