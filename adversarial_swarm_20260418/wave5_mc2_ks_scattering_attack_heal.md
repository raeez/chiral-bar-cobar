# Wave-5 MC2 + H06 (KS scattering) attack-and-heal (2026-04-18)

Author: Raeez Lorgat.

Target: CLAUDE.md MC2 row ("MC2 ALT H06 (KS scattering) conditional on support-property comparison (open)") and Alternative Proofs Secured table entry `| MC2 | Recursive inverse limit | KS scattering diagram (H06) |`.

Source under audit: Vol I `chapters/theory/higher_genus_modular_koszul.tex` — `thm:mc2-bar-intrinsic` (`:4033`), `rem:mc2-scattering-diagram` (`:4421`), `rem:v1-mc2-ks-comparison` (`:4507`), `rem:mc2-bar-intrinsic-perspective` (`:4568`), `thm:recursive-existence` (`:13510`).

Cross-reference: prior today's audit `adversarial_swarm_20260418/attack_heal_mc2_20260418.md` (122-line ledger) — consistent with source; its patch plan was not committed. This Wave-5 ledger adopts the prior ledger's verdicts, installs the two minimal CLAUDE.md scope qualifications, and appends one manuscript scope sentence.

## Attack ledger (six adversarial questions)

**(a) MC2 bar-intrinsic inscription status.** `\label{thm:mc2-bar-intrinsic}` is LIVE at `higher_genus_modular_koszul.tex:4034` with a full four-clause proof body (`:4033-4267`). Secondary all-degree convergence witness: `thm:recursive-existence` (`:13510-13677`), Step 4 constructs $\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ in the weight-filtration quotients $\gAmod/F^{N+1}\gAmod$. Graph-finiteness bound $|V(\Gamma)|\leq 2g-2+n$, $|E(\Gamma)|\leq 3g-3+n$ (`thm:stable-graph-pronilpotent-completion:14016`) gives finite-dimensional transitions; Mittag-Leffler is the strongest form (surjective transitions ⇒ $\varprojlim^1 = 0$). PROVED.

**(b) H06 inscription status.** H06 is a REMARK, not a theorem. `rem:mc2-scattering-diagram:4421-4505` is a proof sketch explicitly labelled "proof sketch for a second, conceptually independent construction." Its companion `rem:v1-mc2-ks-comparison:4507-4566` is honestly scoped: "The missing theorem is the construction, for an arbitrary modular Koszul chiral algebra $\cA$, of a KS support-property package whose ray data are exactly the primitive shadows extracted from $D_\cA$. Until that comparison is proved, `thm:mc2-bar-intrinsic` remains the primary proof of MC2 and `rem:mc2-scattering-diagram` is a redundant route only at the level of a sketched alternative." Not inscribed.

**(c) What is the "support-property comparison"?** Two uninscribed packages surface in the source itself:

1. **Central-charge canonicalisation.** `rem:mc2-scattering-diagram:4431-4434` introduces $Z : \bigoplus_{r\geq 2} \mathbb{Z} e_r \to \mathbb{C}$ as a CHOICE ("choose a central-charge map"). No canonicalisation is given for arbitrary $\cA$; $Z$ is a free variable in the current formulation.

2. **KS support-property comparison.** `rem:v1-mc2-ks-comparison:4528-4538` cites Kontsevich-Soibelman 2008 Def. 1 + Remark 1 (polynomial-density support in the central-charge plane). The shadow radius estimate $|S_r(L)|\sim A(L)\rho_L^r r^{-5/2}$ (`thm:shadow-radius`(ii)) supplies local finiteness on autonomous primary lines, but for a general modular Koszul chiral algebra without T-line restriction, whether the primitive shadows satisfy the KS support property is OPEN.

**(d) AP266 sharpened-obstruction check.** The source already names the obstructions (packages 1 and 2 above). The Kontsevich-Soibelman citation is specific (2008 Theorem 2; Def. 1 + Remark 1). `rem:v1-mc2-ks-comparison` supplies the convention-conversion note: KS use a lattice Lie algebra and its pronilpotent group, this chapter uses $\widehat{\gAmod}$, and "the match is structural, not an identification of Lie algebras." This satisfies AP266 (explicit named obstruction with falsification test): the falsification test is — construct $Z$ and verify polynomial density of active charges, compare $\log \Phi_{\mathfrak{D}}$ to $\Theta_\cA$. No AP272 folklore-citation violation (KS08, KS14 cited specifically).

**(e) Alternative-proof discipline.** The Alternative Proofs Secured table advertises H06 as the "KS scattering diagram" alternative. The word "alternative" suggests an inscribed parallel-primary. In source, H06 is a sketched redundant route WITH two named missing packages. This is AP742 (optimistic status-table drift: "sketched remark with two open packages" → "alternative proof secured"). The Beilinson dictum applies: prefer a smaller true admission to a larger false advertisement. H06 is a SKETCH waiting on a support-property package, not a secured alternative.

**(f) AP741 (pro-object vs chain-level ambient drift).** CLAUDE.md Structural Facts (line 1222) asserts "All-degree convergence PROVED" without naming the ambient category. The source reality (`rem:mc2-bar-intrinsic-perspective:4591-4605`): for class M, $\Theta_\cA$ exists as a pro-object limit in $\widehat{\gAmod} = \pro\text{-}\gAmod$; chain-level termination in $\gAmod$ happens only for classes G/L/C (at degrees 2/3/4 respectively). Class M is unbounded support. Bare "all-degree convergence" understates the class-dependence.

## Surviving core (three sentences)

MC2 bar-intrinsic is PROVED: $\Theta_\cA := D_\cA - d_0$ solves Maurer–Cartan in the completed modular convolution dg Lie algebra $\widehat{\gAmod}$, as the inverse limit along the weight filtration $w(g,r,d) = 2g-2+r+d$ with surjective-transitions Mittag-Leffler (`thm:mc2-bar-intrinsic` + `thm:recursive-existence`). "All-degree convergence" means pro-object convergence in $\pro\text{-}Ch(\Vect)$; chain-level termination in $Ch(\Vect)$ is a class property (G/L/C finite, M transfinite). H06 (Kontsevich–Soibelman scattering) is a SKETCH in `rem:mc2-scattering-diagram` + `rem:v1-mc2-ks-comparison` with two uninscribed packages — central-charge canonicalisation $Z$ and KS support-property comparison (KS08, Def. 1 + Remark 1) — and is not a secured alternative proof.

## Heals (three edits, one ledger)

**H1 — CLAUDE.md Structural Facts (line 1222).** Qualify "All-degree convergence PROVED" with pro-object scope and AP296 cross-check note.

*Before:* `All-degree convergence PROVED.`
*After:* `All-degree convergence PROVED as pro-object limit in $\widehat{\gAmod}$ (surjective-transitions Mittag-Leffler on the operadic weight filtration $w(g,r,d)=2g-2+r+d$); chain-level termination in $\gAmod$ is class-dependent (G/L/C finite, M transfinite).`

Status tag: `\ClaimStatusProvedHere` unchanged. This is SCOPE QUALIFICATION, not retraction.

**H2 — CLAUDE.md Alternative Proofs Secured table (line 1316).** Rename H06 from "KS scattering diagram" (secured) to "KS scattering diagram SKETCHED".

*Before:* `| MC2 | Recursive inverse limit | KS scattering diagram (H06) |`
*After:* `| MC2 | Recursive inverse limit | KS scattering diagram SKETCHED (H06; central-charge + support-property comparison uninscribed) |`

**H3 — Manuscript scope remark (`higher_genus_modular_koszul.tex:~4612`).** Append one sentence at the end of the chain-level-components paragraph of `rem:mc2-bar-intrinsic-perspective` before the multi-channel paragraph, naming the ambient category explicitly.

*Insertion after* `"…even though the parametrization is one-dimensional."` (`:4606`):

> "Equivalently, $\Theta_\cA$ exists as a pro-object limit in $\widehat{\gAmod} = \pro\text{-}\gAmod$ along the weight filtration $w(g,r,d)=2g-2+r+d$; chain-level termination in $\gAmod$ on the nose is a class property (Heisenberg at~$2$, affine at~$3$, $\beta\gamma$ at~$4$; Virasoro at~$\infty$), and the MC equation holds in $\widehat{\gAmod}$ rather than in $\gAmod$ for class~M."

This prevents AP271 reverse drift (CLAUDE.md lagging manuscript) and AP256 aspirational heal by making the ambient distinction explicit in the chapter itself.

**Ledger.** This file `adversarial_swarm_20260418/wave5_mc2_ks_scattering_attack_heal.md`. Prior ledger `attack_heal_mc2_20260418.md` (122 lines) subsumed.

## Anti-patterns surfaced (catalogued with prior ledger; not re-inscribed)

- **AP741** (Pro-object-limit-vs-chain-level ambient drift in MC status-table). Prior ledger §"New anti-patterns surfaced". Heals via H1.
- **AP742** (Alt-proof SKETCHED mislabelled as "conditional" / "secured"). Prior ledger §"New anti-patterns surfaced". Heals via H2.

## Commit plan (NOT EXECUTED)

Three files in one commit, authored Raeez Lorgat, no AI attribution:

1. `CLAUDE.md` — two scope qualifications (H1 line 1222, H2 line 1316).
2. `chapters/theory/higher_genus_modular_koszul.tex` — one-sentence scope remark insertion at `rem:mc2-bar-intrinsic-perspective:4606`.
3. `adversarial_swarm_20260418/wave5_mc2_ks_scattering_attack_heal.md` — this file.

Build gate: `pkill -9 -f pdflatex; sleep 2; make fast`; `make test`. No theorem downgrade, no status tag change, no label rename; edits are scope-language only.

## Verdict

MC2 core theorem is structurally sound at the inscribed scope. H06 is a SKETCHED redundant route, not a secured alternative proof. Two scope qualifications in CLAUDE.md + one-sentence manuscript clarification close the audit. No frontier added, no frontier closed — the support-property comparison remains OPEN, as honestly declared in `rem:v1-mc2-ks-comparison:4558-4564`.
