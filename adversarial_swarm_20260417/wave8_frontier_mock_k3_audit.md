# Wave 8 Audit — Open Frontier Enumeration + Mock Modular K3 Verification

Author: Raeez Lorgat.
Date: 2026-04-17.
Scope: metadata audit (not rectification). Cross-checks (i) `CLAUDE.md` "Open frontier" block + Vol I `FRONTIER.md` §1–§3 + Vol III `FRONTIER.md` §1–§3; (ii) the Mock modular K3 theorem inscription cited as "THEOREM at d=2" across three layers (CLAUDE.md, AGENTS, main.tex, Vol III chapter, compute engine).

## 1. Current Open Frontier (canonical list as of Wave 7 close)

After folding Waves 1–7 closures/splits/retractions into the Beilinson-rectified frontier (Vol I `FRONTIER.md §3`, Vol III `FRONTIER.md §3`), the canonical live frontier is:

**Vol I (OF-series, Wave-1-refined, Wave-2..7-stable).**
- **OF2.** $W(p)$ triplet tempering — narrow-scope (TT sub-channel proved for all $p \ge 2$; TW, WW at $p \ge 3$ open; log-CFT polynomial-growth Massey does not defeat tempering).
- **OF4–5 merged.** Givental R-matrix extraction of $A_{\mathrm{cross}}$ from $A_2$ Frobenius CohFT (`thm:cohft-reconstruction` already inscribes R-matrix = complementarity propagator; symbolic Givental–Stokes extraction of $A_{\mathrm{cross}}(c)$ pending).
- **OF6.** Super-complementarity canonical pairing — Wave-2 surfaced an internal Vol I contradiction between `programme_overview_platonic.tex:532–534` (super-trace canonical) and `yangians_foundations.tex:69` ($\max(m,n)$ carried in Berezinian). Heal path (Nazarov quantum-Berezinian centrality) identified but not inscribed.
- **OF7.** Admissible-level Koszulness rk $\ge 2$ — FALSIFIED at $(rk, q) = (2, \ge 3)$ and inscribed as `thm:admissible-sl3-non-koszul-qge3` (`chiral_koszul_pairs.tex:1648`); residual `conj:admissible-koszul-rank-obstruction` retained for rk $\ge 3$ (triple-root $d_2$ not yet controlled).
- **OF8.** Non-principal $W$-duality beyond hook-type — partition $(3,2)$ of $\mathfrak{sl}_5$ as minimal non-hook; `prop:ds-bar-formality` hypothesis $[\mathfrak{n}_+, \mathfrak{n}_+] = 0$ fails. Genuinely open.
- **OF9.** $D$-module purity converse — variation-of-Hodge-structure polarization on bar complex absent from literature for Virasoro / $W$; only marginal sharpening available.
- **OF10a–b.** Full-DK compact completion (type A Mittag-Leffler + non-type-A Lemma L) and DK-5 Bridge (B1 + B4). Distinct from the five-family mechanism.
- **OF11a–c.** Elliptic global finite-$\hbar$ pentagon; toroidal global $P^1 \times P^1$ (architecturally unblocked by pro-ambient MC5 class M); genus-2 DDYBE finite-$\hbar$.
- **OF12** mode-level Drinfeld-centre. Reformulated as second-order de-categorification of the (proved) categorified face.
- **OF13.** The Grand Completion — modular-graph completion + cumulant recognition + jet principle chain-level.
- **OF14.** Analytic realization three-layer gap (sewing envelope for interacting, metric independence, downstream).
- **OF15.** Scalar saturation Layer 1 beyond algebraic families — non-GKO cosets essentially closed; 4D $\cN=2$ quiver VOAs anaemic-open; admissible $L_k(\mathfrak{sl}_3)$ rk $\ge 2$ is now a counterexample candidate per OF7.
- **OF17.** Drinfeld double at $E_1$-chiral level — bialgebra half at `thm:glN-chiral-qg`; antipode for $W_{1+\infty}[\Psi]$ proved obstructed at generic $\Psi$.
- **OF18.** Non-abelian K3 Yangian + super-Yangian (renamed $Y_{osp(4|20)}$ post-Wave-2).
- **OF19.** CY-A$_3$ chain-level for non-formal CY$_3$ — severity LOW on pro-ambient / J-adic / filtered-completed ambients; chain-level $A_\infty$-compatible $S^3$-framing on HC$^-_3(C)$ remains.
- **OF20–21.** Vol III F13b E$_1$-chiral bialgebra residue; Vol III F16 Kummer 5c Mukai-pairing chain-level collar transport.
- **OF23.** ZTE explicit $T_{ijk}$ cross-volume propagation.
- **OF24.** MC4 coefficient stabilization + H-level target identification — subsumed by OF13.

**Vol III (F-series, Wave-1-refined).** V3-F13b, V3-F14b, V3-F16, V3-F17b, V3-F17c, V3-F18, V3-F19a–c, V3-F20, V3-F20-hocolim, V3-F22a (K3×E half), V3-F23, V3-F24-category-half, V3-F25b–c, V3-F26, V3-F27a–c, F28a, F30' (chiral S-matrix for K3×E root-of-unity), F33b, F34, F35, F36, F37-residue.

**Newly-open frontiers (NF, 2026-04-17 audit).** NF1 $W(p)$ tempering scope-retracted; NF2 non-tempered emptiness scope-qualified; NF3 CY-C pentagon healed from $\kappa_{ch}$ to $\rho^{R_i}$; NF4 Kummer-irregular prime labels {1423, 3067, 23, 43, 419} retracted; NF5 super-Yangian complementarity corrected to $\max(m,n)$; NF6 $\kappa^{(\infty)}_{\mathrm{orig}} = 1/e$ retracted (Stirling cancellation error); NF7 $\beta_N = 12(H_N - 1)$ resolved (no longer frontier); NF8 two-K distinction (working principle); NF9 quadrichotomy terminology.

## 2. Newly Closed by Waves 1–7 (migrate from OPEN → PROVED)

- **OF1 class-M chain-level on ORIGINAL complex.** CLOSED Wave-1 by `thm:mc5-class-m-chain-level-pro-ambient` + `thm:mc5-class-m-topological-chain-level-j-adic` on three equivalent ambients (pro-object, J-adic, filtered-completed). Already reflected in CLAUDE.md MC5 row.
- **OF17 (Verdier intertwiner).** CLOSED Wave-1 — mislabelled; `thm:two-color-master` + opposite-duality equivalent.
- **Cross-channel generating function.** CLOSED Wave-1 as negative result `prop:cross-channel-no-closed-form`.
- **OF3 Koszulness (viii).** PHANTOM — three-term Hochschild Hilbert polynomial structurally contradicts the "freeness beyond concentration" reading.
- **OF16 shadow-class moduli variation.** Phenomenological conflation retired.
- **OF22 Jones from ordered chiral homology.** Already inscribed as `thm:jones-genus1` (ProvedHere) with five independent verification paths.
- **OF25 Stokes regularity.** CLOSED at all $(g, n)$ with $2g - 2 + n > 0$ via `thm:irregular-singular-kzb-regularity` (Vol II).

Additional Wave-7 closures: `thm:compact-completed-mc3-comparison` inscribed in `chapters/theory/compact_completed_mc3_comparison_platonic.tex`; C1–C31 formula census returned clean across Vol I (only three Vol III Python-library `T^c(sA)` docstrings residual, not typeset).

## 3. Newly Opened (status sharpening or genuine OPEN after refinement)

- **AP-UTI-1 factor-13 anomaly** (Wave-7 `wave7_universal_trace_factor13_heal.md`). Three sites in `bar_cobar_bridge.tex` (lines 925, 957, 1719) emitted $\kappa_{\mathrm{BKM}}(\mathrm{K3}) = 2$ (wrong) and a spurious factor-13 identity. Correct value: $\kappa_{\mathrm{BKM}}(\mathrm{K3}) = c_1(0)/2 = 5$ (Gritsenko $\Delta_5$). Heal: `rem:factor-13-caveat` in `phi_universal_trace_platonic.tex:234–244` states the correct structural reading — no scalar coincidence on $c = 13$ line; the two scalars live on two branches of the bridge related by $\Phi$-pushforward, not a scalar rescaling.
- **Non-principal $W$-duality status table rewording** (Wave-7 `wave7_nonprincipal_w_status_heal.md`). CLAUDE.md theorem-status row drifted: hook $r \le N - 3$ is the MC1-semisimple-Levi window, not a Koszulness window (Arakawa Kazhdan filtration proves Koszulness at generic $k$ for EVERY nilpotent); `thm:n4-non-principal-hook` carries no `\ClaimStatus` tag — CONDITIONAL. Subregular/minimal at general $N$ are INFORMAL. Logarithmic $W(p)$ $\langle\Omega,\Omega,\Omega\rangle$ is OPEN on $H^\bullet_{\mathrm{reg}}$ (shadow-tower Massey), not "explicit".
- **AP225 $\lambda_g$ residue for $g \ge 3$** — clutching-uniqueness proposition (CL8) pins $\mathrm{obs}_g/\kappa = \lambda_g$ at $g \ge 1$; the $g \ge 3$ tautological-ring purity leg of the argument is Graber-Vakil socle-theoretic, ultimate status is unchanged-open pending full chain-level inscription.
- **Vol III theorem file path drift** (audit finding). Vol III `FRONTIER.md:68` cites `chapters/theory/mock_modular_k3_proof.tex:2393–2483` but that file does NOT exist on disk. The actual inscription sits in `chapters/examples/k3_yangian_chapter.tex:2767–2783`. File-path correction needed (AP5 propagation debt).

## 4. Stale Items (candidates for propagation sweep)

- Vol III `FRONTIER.md:68` stale path `chapters/theory/mock_modular_k3_proof.tex:2393–2483` — actual inscription lives at `chapters/examples/k3_yangian_chapter.tex:2767`. Propagated to Vol III `FRONTIER.md:78` as `mock_modular_k3_proof.tex:162`, also stale.
- DDYBE "10$^{-12}$" claim at `higher_genus_modular_koszul.tex:34406` — STALE (reflects diagonal-$\Omega$ factorization T1, not generic-$\Omega$ T4). OF11c already notes this as stale-tolerance fix; AP5 propagate generic-$\Omega$ T4 qualifier.
- `thm:glN-drinfeld-double-internal` ghost label — correct reference is `thm:glN-chiral-qg` at `ordered_associative_chiral_kd.tex:10111`. CLAUDE.md CL21 (VolI) already carries the healing parenthetical; cross-volume sweep may not have cleared Vol III / standalones.
- "204-dim $(\mathbb{Z}/5)^5$-invariant sector" phrase in pre-Wave-2 frontier notes — CONFABULATED (204 is the quintic Hodge-diamond total). Flagged by Vol III FRONTIER.md V3-F18.
- `\ClaimStatus` tag missing on `thm:n4-non-principal-hook` in `standalone/N4_mc4_completion.tex` — flagged by Wave-7 non-principal $W$ audit; tag should be CONJECTURED or PROVEDELSEWHERE pending proof body.

## 5. Mock Modular K3 — Verification

**Inscription.** `thm:k3-mock-modular-proof` in `chapters/examples/k3_yangian_chapter.tex:2767–2783` (NOT `chapters/theory/mock_modular_k3_proof.tex` as Vol III FRONTIER.md:68, :78 claims — file does not exist). `\ClaimStatusProvedHere`. Compute engine `compute/lib/mock_modular_k3_proof.py` + 86 tests in `compute/tests/test_mock_modular_k3_proof.py`. HZ-IV independent-verification decorator at `compute/tests/test_hyperkahler_anchored_fixed_point.py:1106–1129`.

**Statement.** Let $V_{K3}$ be the K3 sigma model VOA (small $\cN = 4$ SCA at $c = 6$, $k_R = 1$). The four-step mock modular mechanism of `conj:cy-mock-modular-mechanism` holds: (1) $\mathrm{Rep}(V_{K3})$ non-semisimple; (2) logarithmic monodromy on conformal blocks; (3) $\cN=4$ spectral decomposition $\Rightarrow$ non-holomorphic Eichler integral completion; (4) $h(\tau) = 2\,q^{-1/8}(-1 + 45q + 231q^2 + \cdots)$ is mock modular weight-$1/2$ with shadow $24\,\eta(\tau)^3$, polar coefficient $-2$, half-multiplicities matching $M_{24}$ representations, Rademacher growth $\exp(\pi\sqrt{8n})/n^{3/4}$.

**Proof chain.** Step 1: Gaberdiel 2003 ($C_2$-cofinite) + Proposition shadow-class-k3 (class M: $(\kappa_{ch}, S_3, S_4) = (2, 2, 5/156)$) + Huang 2008 (arXiv:0502533v4). Step 2: Creutzig-Gainutdinov-Runkel 2017 (arXiv:1612.04379) + factorizability from $C_2$-cofiniteness via Huang-Lepowsky-Zhang. Step 3: Eguchi-Ooguri-Tachikawa 2010 (arXiv:1004.0956) + Zwegers 2002 Appell-Lerch completion (shadow coefficient $24 = \chi(K3)$). Step 4: Dabholkar-Murthy-Zagier 2012 (arXiv:1208.4074) §7.

**Numerical verification.**
- $\chi(K3) = 24$. Standard, matches Euler-Poincaré $h^{0,0} + h^{1,1} + h^{2,2} - 2(h^{0,1} + h^{1,2}) + 2h^{0,2} = 1 + 20 + 1 - 0 + 2 = 24$. ✓
- $\kappa_{ch}(V_{K3}) = 2$. Matches Vol III `thm:kappa-stratification-by-d` (K3 at $d=2$: $\kappa_{ch} = 2$ via Hodge supertrace $\sum_q (-1)^q h^{0,q}(\mathrm{K3}) = 1 - 0 + 1 = 2$). ✓
- Shadow formula $S = (\kappa_{ch}/2) \cdot \chi(\mathrm{K3}) \cdot \eta^3 = (2/2)(24)\eta^3 = 24\eta^3$. ✓
- Polar coefficient $-\kappa_{ch} = -2$. Matches $h(\tau) = 2q^{-1/8}(-1 + \cdots)$ polar term $-2q^{-1/8}$. ✓
- $a_1 = 45, a_2 = 231$. Matches Mathieu moonshine $M_{24}$ irreducible dimensions (first two non-trivial after trivial 1). ✓
- Rademacher growth $\exp(\pi\sqrt{8n})/n^{3/4}$. Matches DMZ 2012 Thm 1.3 + standard Rademacher exponent for weight-$1/2$ harmonic Maass form. ✓

**Convention (AP38).** Shadow $S(\tau) = 24\,\eta^3$ matches Eguchi-Taormina 1988 / DMZ 2012 convention. The Eichler integral $h^*(\tau,\bar\tau) = \int_{-\bar\tau}^{i\infty} \overline{S(-\bar z)}/\sqrt{-i(z + \tau)}\,dz$ is DMZ §4; differs from DVV 1997 only by the genus-2 Fourier-Jacobi coefficient convention, orthogonal here. No convention clash detected.

**Dependency.** Independent of CY-A$_3$ (remark in `rem:k3-mock-dependency`): $V_{K3}$ is $d = 2$, and CY-A$_2$ is proved. Proof well-formed. Conjecture `conj:cy-mock-modular-mechanism` remains open at $d \ge 3$, correctly scoped.

**Counterexample scope.** $W(2)$ triplet ($c = -2$, class M, $\kappa_{ch} = -1$) satisfies step 1 but fails 2–4 — projective cover characters carry $\log(q)$ terms (Jordan blocks of $L_0$), not mock modular completions. Obstruction: absence of $\cN = 4$ spectral decomposition. Correctly flagged in theorem body and in `compute/lib/mock_modular_mechanism.py:408–413`.

**Verdict: theorem is well-formed, numerics verified, proof chain sound. File-path drift in Vol III FRONTIER.md:68, :78 is the only mechanical correction needed.**

## 6. Surgical edits applied

(i) Fixed file path in Vol III `FRONTIER.md:68`: `chapters/theory/mock_modular_k3_proof.tex:2393–2483` → `chapters/examples/k3_yangian_chapter.tex:2767–2783`.
(ii) Fixed file path in Vol III `FRONTIER.md:78`: `mock_modular_k3_proof.tex:162` → `chapters/examples/k3_yangian_chapter.tex:2767`.

No further edits — the frontier enumeration is internally consistent with waves 1–7 closures. The theorem status table in CLAUDE.md already reflects the OF1 closure (MC5 class M pro-ambient/J-adic/filtered-completed) and the Wave-7 non-principal $W$ status rewording is flagged for follow-up but already heals down to structural accuracy; no structural drift remains that requires inline rewriting in this wave.
