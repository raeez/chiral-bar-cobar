# Wave 7 — Part V Seven Faces of r(z) adversarial attack + heal

Date: 2026-04-17. Target: Vol I Part V (`holographic_datum_master.tex`, `genus1_seven_faces.tex`, `main.tex:1780-1812`). Full-file linear read: both chapters (1300 + 1255 = 2555 lines total) read top-to-bottom with ~200-400 line chunks; bibliography entries for every face citation verified at primary-source anchor.

## Phase 1: reconnaissance

Part V consists of exactly two chapter files plus a one-page part divider in `main.tex`:

- `chapters/connections/holographic_datum_master.tex` — master chapter, genus-0 seven-face master theorem `thm:hdm-seven-way-master` (1300 lines).
- `chapters/connections/genus1_seven_faces.tex` — elliptic extension, genus-1 master theorem `thm:g1sf-master` (1255 lines).

Part V is flagged `\ifannalsedition\else` (archive-only in Annals edition).

## Phase 2: per-face attack

### Citation table (verified against `bibliography/references.tex`)

| Face | Slug | Citation | arXiv/journal | Status |
|------|------|----------|---------------|--------|
| F1 | bar-cobar twisting (Getzler-Jones / Loday-Vallette) | internal | n/a | Standard |
| F2 | DNP25 = **Dimofte, Niu, Py** | 2508.11749 (2025) | arXiv Aug 2025 | Verified |
| F3 | KhanZeng25 | 2502.13227 (2025) | arXiv Feb 2025 | Verified |
| F4 | GZ26 = Gaiotto, Zeng | 2603.08783 (2026) | arXiv Mar 2026 | Verified (no UNVERIFIED flag; current date 2026-04-17) |
| F5 | Drinfeld85 | Soviet Math. Dokl. 32 | 1985 | Verified |
| F6 | STS83 = Semenov-Tian-Shansky | Funct. Anal. Appl. 17 | 1983 | Verified |
| F7 | FFR94 = Feigin, Frenkel, Reshetikhin | hep-th/9402022 | CMP 166 (1994) | Verified |

**Prompt presupposition error corrected.** The prompt asked whether "DNP25" = "Dimofte-Niarchos-Park" or "Dimofte-Neitzke-Park". Neither. The manuscript consistently attributes DNP25 to **Dimofte, Niu, Py** (arXiv:2508.11749). Multiple bibitem entries (`DNP25`, `DNP2025`) redundantly pin the authorship.

### Face-by-face verdicts

**F1 (bar-cobar twisting).** `thm:hdm-face-1` ProvedHere: $r_\cA(z) = \pi_\cA \in \mathrm{Tw}(B^{\mathrm{ch}}(\cA), \cA)$. Body: propagator-extraction formula eq:hdm-twisting-propagator recovers Getzler-Jones / Loday-Vallette convolution-algebra universal twisting morphism. Self-contained. ACCEPT.

**F2 (DNP line operators).** `thm:hdm-face-2` previously `\ClaimStatusProvedHere`; proof body says "cross-volume identification is established in Vol.~II… documented in Vol.~II, line-operators chapter". This is AP60/AP227 (ProvedHere forwarding: the identification of $r^{\mathrm{DNP}}(z) = r_\cA(z)$ is proved in Vol II, not here). HEAL applied: split-status tag matching Faces 5/6 pattern — ProvedHere for the bar-side identification, ProvedElsewhere for the DNP line-operator package + Vol II cross-volume matching.

**F3 (Khan-Zeng PVA).** `thm:hdm-face-3` ProvedHere with explicit scope `(genus~0 only)` in theorem title and remark after. Scope qualifier present; avoids AP7/AP32 over-generalization. Khan-Zeng framework = 3d Poisson sigma model on PVAs in Barakat-De Sole-Kac sense. Identification $r_\cA(z) = \sum_n \mathrm{cl}(a_{(n)}b)/z^{n+1}$ = formal Laplace transform of $\lambda$-bracket. Classical YBE $\leftrightarrow$ $\lambda$-Jacobi. ACCEPT.

**F4 (Gaiotto-Zeng sphere Hamiltonians).** `thm:hdm-face-4` ProvedHere. $H_i^{\mathrm{GZ}} = \sum_{j \neq i} [r_\cA(z_i - z_j)]_{i,j}$, order $k_{\max}(\cA) - 1$ differential operator on $\mathrm{Conf}_n(\bP^1)$. Commutativity = flatness of $\nabla^{\mathrm{hol}}_{0,n}$ (thm:sphere-reconstruction, Vol I). ACCEPT.

**F5 (Drinfeld rational r-matrix).** `thm:hdm-face-5` split status ProvedHere (identification) + ProvedElsewhere (Drinfeld 1985). Trace-form $r^{\mathrm{Dr}}(z) = k\Omega_{\mathrm{tr}}/z$ and KZ form $\Omega/((k+h^\vee)z)$ bridged at generic $k$; level-sanity checks at $k=0$ and $k=-h^\vee$ correctly labelled. Consistent with HZ-1 / AP-RMATRIX and C9. ACCEPT.

**F6 (Sklyanin/STS83 Poisson bracket).** `thm:hdm-face-6` split status. Classical limit via Li filtration $\cA \to \mathrm{gr}^{\mathrm{Li}}(\cA)$; Sklyanin bracket on $\fg^*$ = Lie-Poisson twisted by symmetric Casimir $\Omega$. Drinfeld classical-limit theorem cited for $\hbar \to 0$ recovery. ACCEPT.

**F7 (FFR94 Gaudin).** `thm:hdm-face-7` ProvedHere. $H_i^{\mathrm{Gaudin}} = \sum_{j \neq i}\Omega_{ij}/(z_i - z_j) = (k+h^\vee)\, H_i^{\mathrm{GZ}}$ — explicit level rescaling makes F7 a normalization-rescaled F4 at $\cA = \widehat{\fg}_k$. Critical-level $k \to -h^\vee$ limit = FFR94 Wakimoto / Sugawara collapse. ACCEPT.

### AP244 overcounting check (are seven faces genuinely distinct?)

Home-category table:

| Face | Home category | Input data |
|------|---------------|------------|
| F1 | dg cat of twisting morphisms $\mathrm{Tw}(B^{\mathrm{ch}}(\cA), \cA)$ | bar coalgebra + algebra |
| F2 | factorization cat on 3d HT theory (DNP meromorphic tensor cat) | line operators |
| F3 | $\lambda$-brackets on PVA = $\mathrm{gr}^{\mathrm{Li}}(\cA)$ | Poisson vertex algebra |
| F4 | $\mathrm{Diff}^*(\mathrm{Conf}_n(\bP^1))$ | differential operators |
| F5 | $Y_\hbar(\fg)$-bimod | quantum group |
| F6 | Poisson $C^\infty(\fg^*)$ | Lie bialgebra cobracket |
| F7 | $\mathcal{U}(\fg)^{\otimes n}$ | universal enveloping |

Potential collapse: F4 vs F7 differ only by the scalar $(k+h^\vee)$, but they occupy DIFFERENT home categories (differential-operator ring on configuration space vs UEA). The master equation eq:hdm-master-equation records the factor-$(k+h^\vee)$ mismatch explicitly. This is legitimate distinctness. NO AP244 collapse.

### Unification claim (viii) — master theorem

`thm:hdm-seven-way-master` (line 730) is inscribed at theorem level with boxed master equation eq:hdm-master-equation and proof body (transitive closure of F1-F7). Scope remark `rem:hdm-master-scope` pins each face's applicability (F1/F3/F4 all modular Koszul $\cA$; F2 3d HT realization; F5-F7 $\cA = \widehat{\fg}_k$). Explicit inscription, NOT advertisement.

### Seven-face TFAE (ix)

The seven faces are not related by TFAE (equivalences of propositions); they are **equal elements** of $\mathrm{End}_\cA(2)[\![z^{-1}]\!]$. Equality is stronger than equivalence. Hence `thm:hdm-seven-way-master` is the correct formalism — no separate `thm:seven-faces-tfae` needed, and introducing one would weaken the claim.

### Genus-1 extension

`thm:g1sf-master` (genus-1 master theorem) ProvedHere for $\cA = \widehat{\fg}_k$. Conjecture `conj:g1sf-higher-genus` (genus $g \geq 2$) correctly tagged Conjectured. Face correspondences:

- F4 at g=1 → KZB connection (instead of KZ), with separate $dz$ and $d\tau$ components.
- F5 at g=1 → Belavin-Drinfeld elliptic r-matrix.
- F7 at g=1 → elliptic Gaudin Hamiltonians.

Class M (Virasoro, $\cW_N$) at genus 1 produces higher-order elliptic differential operators via Weierstrass derivatives $\wp, \wp', \ldots, \wp^{(2N-3)}$ — `thm:g1sf-virasoro`, `thm:g1sf-wn`. Scope remark `rem:g1sf-class-m-scope` correctly notes F5-F7 have no class-M analogue. The $B$-cycle monodromy → quantum group parameter $q = \exp(2\pi i/(k+h^\vee))$ in `thm:g1sf-b-cycle-monodromy` is a legitimate "face 0" at g=1 (no genus-0 counterpart) — inscribed as `rem:g1sf-b-cycle-face-0`.

## Phase 3: heals applied

**H1 (Face 2 status).** `thm:hdm-face-2` tag upgraded from solitary `\ClaimStatusProvedHere` to split `\ClaimStatusProvedHere` (identification with collision residue) + `\ClaimStatusProvedElsewhere` (DNP line-operator package: Dimofte-Niu-Py 2025; Vol II cross-volume matching). Matches Face 5 / Face 6 pattern. Resolves AP60/AP227 ProvedHere-forwarding.

No other surgical heals needed. No phantom citations. No AP244 collapse. Manuscript-metadata hygiene (AP236) clean for Part V (only `% AP148:` LaTeX comments, invisible in PDF, permitted per CLAUDE.md).

## Constitutional hygiene

- AAP1 (antml leakage): zero hits in both chapter files.
- Metadata leakage (AP in prose): zero hits outside `%` comments.
- All commits authored by Raeez Lorgat; no AI attribution.
- No commit performed per instruction.
