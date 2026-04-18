# Attack-and-heal: Seven Faces F7 (FFR94 Gaudin)

Session: 2026-04-18. Auditor: adversarial audit (Vol I Part V Face 7).
Scope: CLAUDE.md Part V reference "F7 FFR94 Gaudin" (Feigin--Frenkel--Reshetikhin 1994, "Gaudin model, Bethe ansatz and critical level", Comm. Math. Phys. 166 (1994), 27--62).

Target files:
- `standalone/seven_faces.tex` (1610 lines) -- canonical seven-faces survey.
- `standalone/gaudin_from_collision.tex` (850 lines).
- `chapters/connections/frontier_modular_holography_platonic.tex:1632-1670` -- theorem home of `thm:gaudin-yangian-identification`.
- `main.tex:1199,1811` -- only `ftm_seven_fold_tfae_platonic` and `genus1_seven_faces` are `\input`.

No edits were performed this session. Findings recorded per AP314 discipline (minimal new APs; reuse the existing catalogue).

---

## (i) Location

Face 7 is inscribed at three sites:

1. **Standalone survey** `standalone/seven_faces.tex:1451` (status table row "F7 (Gaudin generator) proved / cited / specialized, FFR 1994"), with the F4 $\Leftrightarrow$ F7 bridge at lines 408--419 and the F7 generating-function identity at 348--354.
2. **Chapter theorem** `thm:gaudin-yangian-identification` in `chapters/connections/frontier_modular_holography_platonic.tex:1632` (`\ClaimStatusProvedHere`), three clauses: (i) affine KM $k_{\max}=1$ recovery of Gaudin Hamiltonians; (ii) higher Gaudin system from collision residues; (iii) quantization parameter $\hbar = 1/(k+h^\vee)$.
3. **Companion standalone** `standalone/gaudin_from_collision.tex` (850 lines), author-level companion paper to F4/F7.

CLAUDE.md prose references "F7 FFR94 Gaudin" in Architecture block line 1080 only; no theorem-status row is dedicated to F7 (the Gaudin identification lives as downstream content of the `chiral QG equiv` and `thm:gaudin-yangian-identification` rows).

## (ii) Content verification

The F7 content IS inscribed with a proof body, not pure prose framing. Proof body at `frontier_modular_holography_platonic.tex:1655-1670`:

- Part (i) substitutes the collision residue $r(z) = \Omega/((k+h^\vee)z)$ (KZ convention, the programme's canonical form for this inscription) into the depth-1 Hamiltonian formula and recovers $H_i^{\mathrm{GZ}} = (k+h^\vee)^{-1} H_i^{\mathrm{Gaudin}}$ with $H_i^{\mathrm{Gaudin}} = \sum_{j \neq i} \Omega_{ij}/(z_i - z_j)$. The substitution cites `thm:yangian-shadow-theorem` for the collision-residue identity. Computation is one-line; rests on the prior shadow-theorem inscription.
- Part (ii) interprets depth-$k$ residues as $A_\infty$ operations $m_k$ on $\cA^!_{\mathrm{line}}$ via the Homological Perturbation Lemma, at spectral separation $z_{ij}$.
- Part (iii) cites Drinfeld 1985 for $\hbar = 1/(k+h^\vee)$.

The theorem is **not pure prose framing**, but its load-bearing content is the substitution in part (i); parts (ii)--(iii) inherit structure from prior inscriptions (`thm:gz26-commuting-differentials`, `thm:yangian-shadow-theorem`, Drinfeld 1985).

## (iii) `\input` status

- `standalone/seven_faces.tex` is NOT `\input` into `main.tex`. Confirmed by Grep (single match at `main.tex:1811` for `\input{chapters/connections/genus1_seven_faces}`; zero matches for `seven_faces.tex`). This is the **AP255 orphan standalone** noted in the existing CLAUDE.md Elliptic + Toroidal rows; it equally applies to F7, F5 and F6.
- `standalone/gaudin_from_collision.tex` is also NOT `\input` into `main.tex`. Confirmed by Grep (zero matches). Second orphan.
- The chapter `chapters/connections/frontier_modular_holography_platonic.tex` IS inscribed via build (`main.tex` includes Part IV chapters). The load-bearing theorem `thm:gaudin-yangian-identification` therefore lives in the compiled monograph; only the STANDALONE companion surveys are orphans.

Consequence: 19 `\ref{thm:gaudin-yangian-identification}` consumers across Vol I (working_notes, chapters/connections/*, standalone/garland_lepowsky, etc.) resolve to the live chapter inscription. No `[?]` emissions expected at build for this label.

## (iv) Critical-level consistency (k = -h^v)

**THIS IS THE FINDING OF SUBSTANCE.** The F7 inscription uses the KZ-convention r-matrix `r(z) = Omega/((k+h^v)z)` (HOT-ZONE HZ-1 + C9). At $k = -h^\vee$ this form DIVERGES; the Gaudin Hamiltonian inherits the divergence via the $(k+h^\vee)^{-1}$ prefactor.

The PROGRAMME-LEVEL critical-level-jump theorem is separately proved in Vol I (CLAUDE.md status table, row "Critical level jump, PROVED"): at $k=-h^\vee$, $\kappa=0$, monodromy trivial, $H^1$ doubles ($4 \to 8$), Koszulness fails, $H^\bullet_{\mathrm{bar}} = \Omega^\bullet(\mathrm{Op}_\fg^\vee(D))$.

F7 consistency audit:

- **seven_faces.tex, F4$\Leftrightarrow$F7 bridge (lines 408-419):** uses `r(z) = Omega/((k+h^v)z)` WITHOUT explicit exclusion of the critical level. The identity $H_i^{\mathrm{GZ}} = (1/(k+h^\vee)) H_i^{\mathrm{Gaudin}}$ breaks at $k=-h^\vee$. No critical-level scope remark in seven_faces.tex. No `k \ne -h^\vee` qualifier in the bridge paragraph. This is a scope discipline violation at the STANDALONE-level (AP256-adjacent: aspirational bridge text without k-scope qualifier).
- **thm:gaudin-yangian-identification (frontier_modular_holography_platonic.tex:1632-1670):** clause (i) does NOT state "$k \ne -h^\vee$" explicitly in the hypothesis. The theorem statement says "Let $\cA$ be a modular Koszul chiral algebra with dg-shifted Yangian $Y^{\mathrm{dg}}_\cA$"; at $k=-h^\vee$ the algebra $\widehat{\fg}_{-h^\vee}$ FAILS Koszulness (critical-level jump theorem), so the Koszul-locus hypothesis technically excludes $k=-h^\vee$. But the exclusion is implicit, not explicit in the theorem statement, and part (iii) "$\hbar = 1/(k+h^\vee)$" diverges at $k=-h^\vee$ without comment.
- **Consistency with "critical level jump" theorem:** at $k=-h^\vee$ the Feigin--Frenkel centre of $\widehat{\fg}_{-h^\vee}$ is the algebra of functions on opers $\mathrm{Op}_\fg^\vee(D)$; the Gaudin Hamiltonians of FFR94 are, in the ORIGINAL FFR94 paper, DEFINED precisely by lifting central elements from this centre. That is, FFR94 IS the critical-level construction in its primary-source form. The Vol I F7 inscription, however, presents the Gaudin identification as a NON-CRITICAL fact via the $1/(k+h^\vee)$ prefactor. The two are opposite sides of the same object: at $k \ne -h^\vee$ Gaudin emerges as a classical Yangian shadow (Vol I inscription); at $k = -h^\vee$ Gaudin emerges as the spectrum of the centre (FFR94 primary source). Vol I F7 inscribes only the NON-CRITICAL face.
- **Silent scope gap:** the Vol I F7 inscription does not name this split. A reader who sees "Gaudin via FFR94" in the Architecture list may assume the FFR94 critical-level construction is covered by Vol I F7, when it is NOT.

## Diagnosis (no edits this session, per /loop discipline + AP314)

**Pre-existing APs that fire; no new AP numbers needed:**

1. **AP255 (orphan standalone)**: `standalone/seven_faces.tex` and `standalone/gaudin_from_collision.tex` are orphan standalones, same pattern as the Elliptic/Toroidal rows. Build-neutral (no `\ref` consumers point to them uniquely); typeset-phantom at the programme-integration level. Already catalogued across CLAUDE.md.
2. **AP256 (aspirational-heal drift)**: seven_faces.tex F4$\Leftrightarrow$F7 bridge text asserts the identification without the $k \ne -h^\vee$ scope qualifier. Chapter body inherits the same implicit exclusion via Koszulness hypothesis but without explicit statement.
3. **AP271 (reverse drift)**: CLAUDE.md Architecture line 1080 advertises "F7 FFR94 Gaudin" as a face of the programme, presenting FFR94 as the namesake; primary-source FFR94 is the CRITICAL-level construction, whereas Vol I inscribes only the non-critical face. A cleaner statement in CLAUDE.md would read "F7 Gaudin shadow (non-critical face; FFR94 critical-level face covered separately by `Critical level jump` theorem)".
4. **AP280-adjacent (three-step inflation)**: F7 row in seven_faces.tex status table is "proved / cited / specialized" -- one-line claim without scope qualifier, propagating the non-critical face as if it covered the full FFR94 mechanism.

## Heal recommendations (for future session with commit authority)

H1. **seven_faces.tex**: in the F4$\Leftrightarrow$F7 bridge paragraph (lines 408-419), add "$k \ne -h^\vee$" scope qualifier to the statement $H_i^{\mathrm{GZ}} = (1/(k+h^\vee)) H_i^{\mathrm{Gaudin}}$; inscribe a one-line remark noting that the critical-level ($k=-h^\vee$) face of FFR94, where the Gaudin Hamiltonians lift from the Feigin--Frenkel centre on opers, is covered by the Vol I "Critical level jump" theorem as a separate inscription. Minimal scaffolding: 2-3 sentences.

H2. **thm:gaudin-yangian-identification**: strengthen the hypothesis to state "$\cA$ Koszul (implying $k \ne -h^\vee$ when $\cA = \widehat{\fg}_k$)" explicitly, and add in a companion remark `rem:gaudin-critical-face` noting the Feigin--Frenkel opers-centre description of the Gaudin Hamiltonians at $k=-h^\vee$ as the complementary face. The bar-complex perspective covers the non-critical face; opers-centre covers the critical face. Both are FFR94.

H3. **CLAUDE.md Architecture line** (line 1080 of the full CLAUDE.md): no edit required; the existing wording "F7 FFR94 Gaudin" is accurate as the NAMESAKE reference. But if a dedicated F7 status-table row is ever added, it must split the scope as "Non-critical face: PROVED via `thm:gaudin-yangian-identification`. Critical face ($k=-h^\vee$): covered by `Critical level jump` theorem via FF opers-centre."

H4. **main.tex \input of standalone/seven_faces.tex + standalone/gaudin_from_collision.tex**: consistent with the elliptic/toroidal row treatment, these remain AP255 orphans by design (standalone survey papers, not chapters). No heal action required provided CLAUDE.md continues to note the orphan status; no theorem-level inscription is lost by the non-inclusion, since the load-bearing `thm:gaudin-yangian-identification` is in the live chapter.

## Summary

F7 FFR94 Gaudin IS inscribed with proof body at `thm:gaudin-yangian-identification` (chapter, in-build). Two companion standalones are AP255 orphans. The inscription covers the NON-CRITICAL face of FFR94 only; the CRITICAL-level face (Gaudin from Feigin--Frenkel opers-centre, which is the primary-source FFR94 content) is covered separately by the "Critical level jump" theorem but not named as "F7" anywhere. The silent scope split is the programme's largest latent scope discipline issue on Face 7: "F7 = FFR94" reads as covering the full FFR94 paper, while only the non-critical shadow is inscribed under the F7 label.

No edits executed this session per /loop + AP314 discipline. Heal recommendations H1-H3 above; H4 status-quo.
