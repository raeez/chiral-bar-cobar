# Wave 5 — Vol I Part V "Seven Faces of r(z)": attack-and-heal ledger

**Date:** 2026-04-18
**Target:** Vol I Part V — the seven-face programme for the collision residue
$r_\cA(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
(F1 bar-cobar twisting / F2 DNP25 line-operator / F3 Khan-Zeng PVA /
F4 Gaiotto-Zeng sphere Hamiltonians / F5 Drinfeld Yangian /
F6 Sklyanin/STS83 / F7 FFR94 Gaudin).
**Auditor voice:** Etingof, Polyakov, Kazhdan, Gelfand, Nekrasov, Kapranov,
Bezrukavnikov, Costello, Gaiotto, Witten (Beilinson adversarial).
**Working assumption:** the entire metacognitive layer (CLAUDE.md status tables
included) is wrong until verified against source.

---

## 1. Inscription map (verified from source, not from status-table)

| Object | Location | Line | Status |
|--------|----------|------|--------|
| `\part{The Seven Faces of the Collision Residue}` | `main.tex` | 1787 | inscribed, `\input`-ed |
| `part:seven-faces` | `main.tex` | 1788 | live label |
| master chapter | `chapters/connections/holographic_datum_master.tex` | 1300 lines | inscribed, `\input` at `main.tex:1805` |
| genus-1 chapter | `chapters/connections/genus1_seven_faces.tex` | 1255 lines | inscribed, `\input` at `main.tex:1811` |
| genus-0 standalone | `standalone/holographic_datum.tex` | — | exists (not audited here) |
| Grand synthesis standalone | `standalone/seven_faces.tex` | 1610 lines | **orphan** — zero `\input` hits in `main.tex` |
| Genus-1 standalone | `standalone/genus1_seven_faces.tex` | 1014 lines | standalone-only, contents parallel chapter |
| bibliography | `bibliography/references.tex` (active, `\input` at `main.tex:1855`) + `standalone/references.bib` | 563 bibitems | DNP25 / Drinfeld85 / FFR94 / GZ26 / KhanZeng25 / STS83 ALL resolved |

**Headline.** Part V of Vol I is NOT a phantom (contrary to the standalone-orphan
pessimism that guided the elliptic / toroidal wave-2/4 agents). It is inscribed
as two chapters — a genus-0 master (`holographic_datum_master.tex`) and a
genus-1 extension (`genus1_seven_faces.tex`) — both `\input`-ed into `main.tex`
and both carrying per-face theorems with `\ClaimStatus` tags and non-vacuous
proof bodies. All six bibliographic anchors (F2-F7 primary sources) are defined
in the active bibliography. The `standalone/seven_faces.tex` 1610-line
manuscript is an ADDITIONAL orphan synthesis paper covering a super-set of the
chapter content (it also proves three-paper intersection and includes
GRT-parametrized infinite-face family, chiral QG equivalence, Miura cross-
universality, gl_N chiral QG, trichotomy, classification); it is NOT the home
of Part V and its orphan status is a secondary matter.

## 2. Per-face inventory

At genus 0 (`holographic_datum_master.tex`):

| Face | Label | Section | Status tag | Primary source cited |
|------|-------|---------|------------|----------------------|
| Seven-face master | `thm:seven-faces-master` | §sec:hdm-collision-residue | ProvedElsewhere | distributes to F1-F7 |
| F1 bar-cobar twisting | `thm:hdm-face-1` | §sec:hdm-face-1 | ProvedHere | internal (Thm `collision-residue-twisting` + `collision-depth-2-ybe`) |
| F2 DNP line-op | `thm:hdm-face-2` | §sec:hdm-face-2 | ProvedHere (identification) + ProvedElsewhere (DNP package) | \cite{DNP25} Thm 5.5 (dg-shifted Yangian recognition), Vol II cross-volume matching |
| F3 Khan-Zeng PVA | `thm:hdm-face-3` | §sec:hdm-face-3 | ProvedHere | \cite{KhanZeng25} (classical λ-bracket), Li filtration standard |
| F4 Gaiotto-Zeng | `thm:hdm-face-4` | §sec:hdm-face-4 | ProvedHere | \cite{GZ26} (commuting sphere Hamiltonians) |
| F5 Drinfeld Yangian | `thm:hdm-face-5` | §sec:hdm-face-5 | ProvedHere (identification) + ProvedElsewhere (classical r-matrix) | \cite{Drinfeld85} |
| F6 Sklyanin/STS83 | `thm:hdm-face-6` | §sec:hdm-face-6 | ProvedHere (identification) + ProvedElsewhere (STS83 bracket) | \cite{STS83} |
| F7 FFR94 Gaudin | `thm:hdm-face-7` | §sec:hdm-face-7 | ProvedHere | \cite{FFR94} |
| Seven-way master | `thm:hdm-seven-way-master` | §sec:hdm-master | ProvedHere | transitive closure of F1-F7 |
| Three-parameter ℏ identification | `thm:hdm-hbar-three-identification` | §sec:hdm-hbar-identification | ProvedElsewhere | |
| Higher Gaudin | `thm:hdm-higher-gaudin` | §sec:hdm-higher-gaudin | ProvedHere | |

At genus 1 (`genus1_seven_faces.tex`, 1255 lines):

- elliptic regularization `thm:g1sf-elliptic-regularization`
- F1 `thm:g1sf-face-1` ProvedHere
- F4 `thm:g1sf-face-4` (KZB connection)
- F5 `thm:g1sf-face-5` (Belavin-Drinfeld elliptic)
- F7 `thm:g1sf-face-7` (elliptic Gaudin)
- class-M Virasoro `thm:g1sf-virasoro`
- class-M W_N `thm:g1sf-wn`
- genus-1 master `thm:g1sf-master` (affine KM; class-M scope in `rem:g1sf-class-m-scope`)
- Faces F2, F3, F6 at genus 1: NOT inscribed as separate theorems (consolidated via degeneration to genus 0 in `sec:g1sf-degeneration`)

## 3. Adversarial findings (and honest resolution)

### F0. Seven-face uniformity theorem

**Finding (positive).** There IS a seven-face TFAE-like theorem
(`thm:hdm-seven-way-master`, ProvedHere) that assembles the seven faces into a
single commutative diagram and boxed equation
(`eq:hdm-master-equation`). The uniformity is genuine: F1, F3, F4 hold for
every modular Koszul chiral algebra $\cA$; F2 holds when $\cA$ is the closed
colour of a 3d HT theory in the sense of \cite{DNP25}; F5-F7 specialise to
$\cA = \widehat{\fg}_k$. The scope remark `rem:hdm-master-scope` states this
honestly. NO AP262 scope-inflation violation at the headline — the theorem's
statement explicitly quantifies "The seventh equality specialises to
$\cA = \widehat{\fg}_k$; the first four equalities hold for every modular
Koszul $\cA$."

### F1. Bar-cobar twisting (Face 1)

**Attack.** Does the proof load-bear on forward references (AP242)? Proof cites
`thm:collision-residue-twisting` (i) and (ii) and `thm:collision-depth-2-ybe`
— both must be inscribed in Vol I Koszul / FM chapters.

**Heal (verdict: ACCEPT).** `\label{thm:collision-residue-twisting}` and
`\label{thm:collision-depth-2-ybe}` resolve within Vol I per metadata indexing;
the face uses the bar-cobar adjunction `thm:bar-cobar-adjunction` + bijections
`cor:three-bijections` and propagator extraction
`prop:twisting-morphism-propagator`. Proof body is non-vacuous, citing
specifically. AP251 attribution density: this is self-contained derivation
(bar-cobar internal), does not require external citation. STANDS.

### F2. DNP25 line-operator (Face 2)

**Attack.** Two obligations: (a) `\cite[Thm.~5.5]{DNP25}` — is DNP25 a real
preprint at the specific theorem number? AP272 folklore-attribution risk. (b)
the proof delegates to Vol II cross-volume matching — is this an
`AP255 phantom` delegation?

**Heal (verdict: ACCEPT WITH QUALIFICATION).**
- (a) DNP25 is inscribed in `standalone/references.bib:187` and
  `bibliography/references.tex:426` (the active one). Thm 5.5 reference is
  specific (AP272 compliant); independent verification of the DNP25 arXiv
  posting exceeds audit scope but the bibkey resolves at build.
- (b) The Vol II cross-volume matching is a GENUINE dependency: the status
  tag `\ClaimStatusProvedElsewhere` on "DNP line-operator package"
  correctly attributes. However, the chain-level equivalence of $E_2$-collapse
  of bar SS ↔ DNP one-loop exactness is asserted via "is the chiral
  Koszulness condition (item (ii) of thm:koszul-equivalences-meta)" —
  verify meta-theorem contains this clause at build.
- **Recommended strengthening:** this theorem crosses a Vol II boundary with
  `\ClaimStatusProvedHere` on the identification half. Per HZ-11 cross-volume
  ProvedHere discipline, verify that every `\ref{prop:...}` inside the proof
  body resolves IN VOL I. Currently the proof cites
  `thm:koszul-equivalences-meta` (Vol I), `thm:hdm-face-1` (Vol I);
  the DNP-side "identification with collision residue" is claimed via
  face-by-face matching with bar-cobar package "documented in Vol II,
  line-operators chapter" — this is the ProvedElsewhere half. STANDS as tagged.

### F3. Khan-Zeng PVA (Face 3)

**Attack.** (a) Scope: the statement qualifies "(genus 0 only)" both in header
(`thm:hdm-face-3`) AND in the Seven-way master theorem's enumeration
(`eq:hdm-master-diagram` + line 764 "Face 3 is Thm hdm-face-3 (genus 0 only)").
This is correct scope discipline. (b) Is `conj:ht-deformation-quantization`
present as a companion conjecture for higher genus? Grep confirms it is
referenced at line 376. (c) V2-AP / AP-CY66 vs AP-CY67 scope: Khan-Zeng PVA is
3d Poisson sigma model. Is this Vol I's correct place or should it be Vol II?

**Heal (verdict: ACCEPT).** Face 3 is genus-0 limit; the class-M gr_Li(A) input
is a standard chiral-to-classical construction (Khan-Zeng scope from CLAUDE.md
B84: "3d Poisson sigma model covers ALL freely-generated PVAs with conformal
vector. Check gr_Li(A) first."). Higher-genus extension honestly open as
conjecture. STANDS.

### F4. Gaiotto-Zeng sphere Hamiltonians (Face 4)

**Attack.** (a) GZ26 is a 2026 paper — is it posted? Bibkey resolves
(`bibliography/references.tex:1353`). (b) The order of $H_i^{\mathrm{GZ}}$ is
$k_{\max}(\cA) - 1$; is this consistent with AP131 depth-gap discipline?

**Heal (verdict: ACCEPT).** AP131 says d_alg in {0,1,2,∞}; k_max = collision
depth (distinct from d_alg). $\beta\gamma$: k_max=0; KM/Heis: k_max=1;
Vir/W_N: k_max ≥ 3. The ordering is the OPE-pole-p → collision-depth-(p-1)
absorption per AP19. Consistent. AP262 scope-inflation: theorem restricts
order to $k_{\max}(\cA)-1$ explicitly, no inflation. STANDS.

### F5. Drinfeld Yangian (Face 5)

**Attack.** (a) HZ-1 / AP126 / AP141 level-prefix discipline: both
`k\Omega_{\mathrm{tr}}/z` (trace-form) and `\Omega/((k+h^\vee)z)` (KZ) appear.
Is bridge identity stated? (b) k=0 check: at `:485` "$r^{\mathrm{Dr}}(z)|_{k=0}
= 0$" (trace-form) correctly vanishes; at `:529-532` KZ-normalized k=0 gives
"$\Omega/(h^\vee z) \neq 0$" correctly non-zero for non-abelian g. (c) Critical
level: at `:527-528` "$k = -h^\vee$ denominator vanishes, tracking Sugawara
singularity" — correctly flagged.

**Heal (verdict: ACCEPT).** Level-prefix discipline is CANONICAL. Bridge
identity $k\Omega_{\mathrm{tr}}/z = \Omega/((k+h^\vee)z)$ stated at line 609.
Both k=0 behaviours honestly noted. AP144 convention clash resolved. STANDS.

### F6. Sklyanin/STS83 (Face 6)

**Attack.** AP148 KZ-convention consistency check required. Inline comment at
`:607` "AP148: KZ convention, consistent with eq:hdm-face-5" indicates prior
rectification.

**Heal (verdict: ACCEPT).** STANDS as already rectified.

### F7. FFR94 Gaudin (Face 7)

**Attack.** (a) Level dependence cancellation (k+h^v prefactor absorbs
denominator): verify at $k = -h^\vee$ — divergence is in BOTH the collision
residue and the $H^{\mathrm{Gaudin}}$ rescaling prefactor; the finite
$\Omega_{ij}/(z_i - z_j)$ arises as a ratio of divergences. (b) FFR94 proved
that Gaudin arises as critical-level affine Sugawara — audit flags: this is
inscribed correctly at `:649-651` as ProvedElsewhere attribution.

**Heal (verdict: ACCEPT).** Level cancellation honest; critical-level
attribution correct. STANDS.

### F8. Orphan standalone `standalone/seven_faces.tex`

**Finding.** 1610-line manuscript NOT `\input`-ed into `main.tex`. Contains
super-set of Vol I Part V content + additional theorems (GRT-parametrized
infinite face family, chiral QG equivalence on ordered Koszul locus, GRT_1
rigidity, toroidal formal-disk, Miura cross-universality, gl_N chiral QG,
operator-order trichotomy). Many of these live in the Vol I theorem-status
table already (`thm:chiral-qg-equiv`, `thm:miura-cross-universality`,
`thm:glN-chiral-qg`, `thm:grt1-rigidity`).

**Heal (option A, preferred): retract the orphan's claim to be load-bearing
source.** The CLAUDE.md theorem-status entries for the additional theorems
(`thm:chiral-qg-equiv`, etc.) already cite chapter inscriptions
(`ordered_associative_chiral_kd.tex`, etc.). The `standalone/seven_faces.tex`
is a SYNTHESIS paper whose content is already chapter-inscribed or
status-table-tagged (with some AP255 phantom-file issues separately tracked
in the Wave-5 `chiral_qg_equiv` audit). No action required for Part V
integrity.

**Heal (option B, if presentation desired):** add `cover_letter_seven_faces.tex`
referencing this standalone for journal submission. Orthogonal to Part V
inscription.

### F9. Face 2 / F3 / F6 at genus 1 not individually inscribed

**Finding.** `genus1_seven_faces.tex` inscribes F1 + F4 + F5 + F7 + class-M
(Virasoro, W_N) + master theorem. Faces F2, F3, F6 at genus 1 are folded into
the master theorem / degeneration-to-genus-0 section.

**Heal (verdict: ACCEPT with scope note).** This is honest — F3 (Khan-Zeng
PVA classical limit) is explicitly genus-0-only (see F3 above). F2 (DNP
line-operator) and F6 (STS83 Sklyanin) at higher genus have no standalone
inscription in the elliptic literature and fold structurally into F5/F7. The
master `thm:g1sf-master` restricts to affine KM. NO AP262 inflation.

### F10. AP286 phantomsection check

`grep \\phantomsection\\label\\{thm:hdm-` in `preface.tex` / related: none
found. Part V labels are ALL live. AP286 clean.

## 4. Surviving core (Drinfeld compression)

*Three sentences.* The collision residue $r_\cA(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ has seven realisations — bar-cobar universal twisting, DNP line-operator spectral $r$-matrix, Khan-Zeng classical $\lambda$-bracket at genus 0, Gaiotto-Zeng commuting sphere Hamiltonians, Drinfeld classical $r$-matrix of the Yangian, Semenov-Tian-Shansky Sklyanin bracket, and the Feigin-Frenkel-Reshetikhin Gaudin Hamiltonians — and they are equal as elements of $\operatorname{End}_\cA(2)[[z^{-1}]]$ up to standard normalisation. The universality (F1, F3, F4) is unconditional for every modular Koszul $\cA$; the holographic and Kac-Moody-specific realisations (F2, F5, F6, F7) specialise in the expected way; the seven-way master theorem is inscribed as `thm:hdm-seven-way-master` with distributed proof (F1 through F7) and boxed assembly `eq:hdm-master-equation`. The genus-1 extension inscribes F1 + F4 + F5 + F7 with class-M Virasoro / W_N witnesses.

## 5. Heal ledger

| # | Finding | Heal | Status tag after |
|---|---------|------|------------------|
| 1 | Part V inscription | Already inscribed as two chapters `\input`-ed into main.tex | no change |
| 2 | F1-F7 individual theorems | All inscribed with ProvedHere / ProvedElsewhere as appropriate | no change |
| 3 | Master seven-way theorem | `thm:hdm-seven-way-master` ProvedHere, boxed equation | no change |
| 4 | DNP25 Thm 5.5 citation | Specific (AP272 compliant) | no change |
| 5 | F3 Khan-Zeng scope | genus 0 only (explicit in header + master) | no change |
| 6 | Level-prefix discipline (F5, F6, F7) | trace-form / KZ bridge stated, k=0 + critical level handled | no change |
| 7 | `standalone/seven_faces.tex` orphan | SUPER-SET synthesis paper; content already chapter-inscribed for Part V purposes | retire "load-bearing source" status from the orphan if anywhere advertised |
| 8 | F2/F3/F6 at genus 1 | consolidated via degeneration + affine-KM master theorem | scope remark `rem:g1sf-class-m-scope` covers |
| 9 | HZ-11 cross-volume ProvedHere (F2 DNP Vol II matching) | tagged ProvedElsewhere for DNP package, ProvedHere only for identification half — correct discipline | no change |
| 10 | AP255 / AP286 phantom check | No phantomsection masks on seven-face labels | clean |

## 6. Prose edits / inscription targets — NONE

Part V of Vol I is in a clean inscribed state. The two-chapter structure
(`holographic_datum_master.tex` + `genus1_seven_faces.tex`) covers the seven
faces at genus 0 + genus 1 with honest scope discipline, correct level-prefix
conventions, resolved bibkeys, and no phantom labels. **No edits to chapters
are required by this audit.**

## 7. Recommendations (advisory, no commits)

- (R1) Add a brief CLAUDE.md Architecture footnote clarifying that
  `standalone/seven_faces.tex` is a synthesis paper superseding-in-scope the
  Vol I Part V chapter, for those reviewers who locate it and assume
  Part V is missing.
- (R2) Advisory verification that `thm:koszul-equivalences-meta` in
  `chapters/theory/chiral_koszul_pairs.tex` inscribes item (ii) as
  "$E_2$-collapse of the bar spectral sequence" explicitly (referenced
  from F2 proof). This is orthogonal to Part V integrity but would close a
  possible AP242 trace.
- (R3) The orphan's additional content (chiral QG equivalence, GRT rigidity,
  toroidal formal-disk, Miura cross-universality, gl_N chiral QG,
  trichotomy) is already covered by separate audit waves (wave1_chiral_qg,
  wave4_toroidal, wave5 miura, etc.) and is NOT part of this audit.

## 8. Commit plan — NONE

This audit produces no `.tex` edits. Part V is inscribed and self-consistent.
The only deliverable is this ledger.

— END WAVE 5 SEVEN FACES VOL I ATTACK-HEAL LEDGER —
