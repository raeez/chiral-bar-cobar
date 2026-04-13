#!/usr/bin/env python3
"""
Mega Rescue Campaign — 100 Codex Agents
Scope: last 200 commits from EACH volume (~600 commits total).
HEAL, REPAIR, UPGRADE, ALTERNATIVE PROOFS, CROSS-CONSISTENCY, LITERATURE.

Usage:
    python3 scripts/mega_rescue_100.py --batch-size 5 --timeout 1800 --delay 45
"""

import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"mega_rescue_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

PREAMBLE = """\
<task>
You are a MEGA RESCUE agent operating on the FULL scope of the last 200 commits from
each volume of a 3-volume, 4,700-page mathematical manuscript. This session has already
deployed 632 Codex agents. You operate on the CURRENT disk state which reflects ALL prior work.

Run `git log --oneline -200` to see the full commit history in your assigned repo.
Read AGENTS.md and CLAUDE.md for the constitutional framework (AP1-AP224, B1-B78, FM1-FM38).

Your mission:
1. HEAL: find remaining wounds across the FULL 200-commit surface
2. ALTERNATIVE PROOFS: provide independent proof routes for redundancy
3. LITERATURE: cross-check against published sources with explicit convention bridges
4. UPGRADE: strengthen conditional results; seek condition removal
5. CROSS-CONSISTENCY: verify coherence across all three volumes and with external theories

CRITICAL: read the ACTUAL files on disk. Do NOT rely on commit messages or memory.
</task>

<grounding_rules>
Every claim grounded in file contents or tool outputs. Label hypotheses.
Literature citations: paper, theorem/equation number, convention bridge.
</grounding_rules>

<completeness_contract>
For each result in scope: PRIMARY PROOF [sound/gap], ALTERNATIVE [written/sketched/identified],
LITERATURE [confirmed/discrepant/unchecked], CONFIDENCE [high/medium/low].
</completeness_contract>

<verification_loop>
After edits: re-read, grep AP126/AP132/AP29/AP165/AP113. Run relevant tests.
</verification_loop>
"""


def agent(aid, prompt, cwd=VOL1):
    AGENTS.append({"id": aid, "prompt": PREAMBLE + "\n\n" + prompt, "cwd": cwd, "model": "gpt-5.4"})


def run_agent(a, timeout=1800):
    out_file = OUT / f"{a['id']}.md"
    t0 = time.time()
    try:
        r = subprocess.run(
            ["codex", "exec", "-", "-m", "gpt-5.4", "-C", a["cwd"], "--full-auto"],
            input=a["prompt"], capture_output=True, text=True, timeout=timeout,
        )
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} ({dt:.0f}s)\n\n{r.stdout}\n\n---\nSTDERR:\n{r.stderr}")
        return a["id"], r.returncode == 0, dt
    except subprocess.TimeoutExpired:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — TIMEOUT ({dt:.0f}s)\n")
        return a["id"], False, dt
    except Exception as e:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — ERROR: {e}\n")
        return a["id"], False, dt


# ═══════════════════════════════════════════════════════════════════
# TIER 1: VOL I DEEP CHAPTER HEALING (25 agents)
# One agent per key chapter — full 200-commit scope.
# ═══════════════════════════════════════════════════════════════════

V1_TARGETS = [
    ("M01_bar_construction", "chapters/theory/bar_construction.tex", "Bar construction: augmentation, desuspension, deconcatenation. Cross-check with BD [BD04] Ch 3. Alternative: Lurie HA nerve construction. Verify AP132, AP22."),
    ("M02_cobar_construction", "chapters/theory/cobar_construction.tex", "Cobar construction + Verdier. Cross-check with Positselski [Pos11] coderived. Alternative: operadic bar-cobar from LV [LV12]. Verify Verdier convention (AP208)."),
    ("M03_bar_cobar_inversion", "chapters/theory/bar_cobar_adjunction_inversion.tex", "Theorem B inversion. Cross-check with Keller [Kel94] derived equivalence. Alternative: deformation-retract approach. Verify non-circularity (AP191)."),
    ("M04_bar_cobar_curved", "chapters/theory/bar_cobar_adjunction_curved.tex", "MC4 curved bar-cobar. Cross-check with Positselski curved Koszul [Pos11]. Verify filtration (AP199). Alternative: weight-completion via Beilinson."),
    ("M05_chiral_koszul_pairs", "chapters/theory/chiral_koszul_pairs.tex", "Theorem A + Koszul equivs. Verify filtered-comparison lemma (AP209). Verify (vii)/(viii) scope (AP216/AP217). SC-formality (AP218). Cross-check with FG [FG04]."),
    ("M06_higher_genus_foundations", "chapters/theory/higher_genus_foundations.tex", "C0 fiber-center. Verify curved well-typedness (AP194). Cross-check with Tsuchimura [Tsu04] genus-g propagator. Alternative: coderived fiber-center."),
    ("M07_higher_genus_modular", "chapters/theory/higher_genus_modular_koszul.tex", "Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g."),
    ("M08_higher_genus_complementarity", "chapters/theory/higher_genus_complementarity.tex", "Theorems C1/C2. Verify genus-0 (AP204), reflexivity (AP205), object identity (AP206/AP207). Cross-check with PTVV shifted symplectic."),
    ("M09_en_koszul_duality", "chapters/theory/en_koszul_duality.tex", "Topologization + E_n. Verify chain-level split (AP210). Cross-check with CFG [arXiv:2602.12412] E_3. SC five presentations. Alternative: 3d CS factorization."),
    ("M10_chiral_hochschild", "chapters/theory/chiral_hochschild_koszul.tex", "Theorem H + Gerstenhaber. Verify coalgebra chain (AP223), FM collapse (AP222), bracket (AP221). Cross-check with Tamarkin [Tam03] formality. Alternative: deformation-theoretic."),
    ("M11_e1_modular", "chapters/theory/e1_modular_koszul.tex", "E1 ordered theory. Verify MC2 carrier (g^{E1} vs g^{mod}). Cross-check with Stasheff [Sta63]. Alternative: operadic E_1 via LV."),
    ("M12_nilpotent_completion", "chapters/theory/nilpotent_completion.tex", "MC4 resonance. Verify transfer theorem (AP200). Cross-check with Positselski completion. Alternative: pro-completion via Lurie."),
    ("M13_ordered_chiral_kd", "chapters/theory/ordered_associative_chiral_kd.tex", "Ordered chiral KD — newest content. Verify E1-first. Cross-check with Kazhdan-Lusztig category O. Alternative: Drinfeld strictification."),
    ("M14_coderived_models", "chapters/theory/coderived_models.tex", "Coderived category. Verify non-circularity with Thm B (AP191). Cross-check with Positselski [Pos11]. Verify coacyclic characterization (AP202)."),
    ("M15_heisenberg", "chapters/examples/heisenberg.tex", "Heisenberg: kappa=k, r=k/z, class G. Verify all formulas against census. Cross-check with FLM [FLM88]. Verify k=0 abelian limit."),
    ("M16_kac_moody", "chapters/examples/kac_moody.tex", "Affine KM: kappa=dim(g)(k+h^v)/(2h^v), r=k*Omega/z. Verify Sugawara shift. Cross-check with Kac [Kac90]. Verify critical level k=-h^v."),
    ("M17_virasoro", "chapters/examples/virasoro.tex", "Virasoro: kappa=c/2, self-dual c=13. Verify r-matrix (c/2)/z^3+2T/z. Cross-check with BPZ [BPZ84]. Verify class M, d_alg=inf."),
    ("M18_w_algebras", "chapters/examples/w_algebras.tex", "W_N: kappa=c*(H_N-1). Verify H_N convention (AP136). Verify W_2=Vir specialization. Cross-check with Fateev-Lukyanov."),
    ("M19_free_fields", "chapters/examples/free_fields.tex", "bc/bg: c_bc+c_bg=0. Verify signs (AP137). Verify betagamma depth gap witness (AP219). Cross-check with Friedan-Martinec-Shenker."),
    ("M20_bershadsky_polyakov", "chapters/examples/bershadsky_polyakov.tex", "BP: K=196, self-dual k=-3. Verify kappa+kappa'=98/3. Cross-check with Bershadsky [Ber91], Polyakov [Pol90]."),
    ("M21_landscape_census", "chapters/examples/landscape_census.tex", "The CENSUS. For EVERY family: verify kappa, r-matrix, class, depth, K against compute engines. This is the CANONICAL source. Any error here propagates everywhere."),
    ("M22_yangians", "chapters/examples/yangians_computations.tex", "MC3 Baxter + Yangian. Verify constraint b=a-1/2 (AP201). Cross-check with Drinfeld [Dri85], Chari-Pressley [CP95]."),
    ("M23_concordance", "chapters/connections/concordance.tex", "CONSTITUTION. Verify EVERY entry matches current .tex. Verify routing remarks. Verify status after all 632 agents."),
    ("M24_bv_brst", "chapters/connections/bv_brst.tex", "MC5 BV/bar. Verify harmonic mechanism (AP203). Verify coderived argument (AP202). Cross-check with Costello-Gwilliam BV [CG17]."),
    ("M25_preface_intro", "chapters/frame/preface.tex + chapters/theory/introduction.tex", "Frame chapters. Verify no scope inflation (AP215). Verify every theorem matches concordance. Symphonic standard."),
]

for mid, target, desc in V1_TARGETS:
    agent(mid, f"""TARGET: {target}
SCOPE: Last 200 commits. Run: git log --oneline -200 -- {target.split('+')[0].strip()} | head -20
{desc}
Read the file. Audit every theorem. Provide alternative proofs where possible.
Cross-check against cited literature with explicit convention bridges.
For each finding: PROBLEM + FIX. For each alternative proof: write or sketch it.""")


# ═══════════════════════════════════════════════════════════════════
# TIER 2: VOL II DEEP HEALING (20 agents)
# ═══════════════════════════════════════════════════════════════════

V2_TARGETS = [
    ("M26_v2_bar_cobar_review", "chapters/theory/bar-cobar-review.tex", "Vol I bridge. Verify ALL theorem citations match current Vol I after 200 commits of rectification. Fix stale claims."),
    ("M27_v2_factorisation_sc", "chapters/theory/factorisation_swiss_cheese.tex", "SC^{ch,top}. Verify AP165 (not on B(A)), AP166 (not self-dual), AP168 (E_3-topological). Five presentations."),
    ("M28_v2_foundations", "chapters/theory/foundations.tex", "Vol II foundations. Cross-check E_1/E_inf hierarchy (V2-AP1-AP24). Verify no 'VAs not E_inf'."),
    ("M29_v2_axioms", "chapters/theory/axioms.tex", "Vol II axioms. Verify E_N definitions (chiral vs topological at each level). Cross-check with our Vol I definitions."),
    ("M30_v2_3d_gravity", "chapters/connections/3d_gravity.tex", "CLIMAX. Verify topologization scope (affine KM only, NOT unconditional — fix line 6516). Cross-check with CFG E_3. Genus tower."),
    ("M31_v2_spectral_braiding", "chapters/connections/spectral-braiding-core.tex", "R-matrix/braiding. Verify chiral QG scope (AP174: sl_2+KM only). Cross-check with Drinfeld, Etingof-Varchenko."),
    ("M32_v2_ht_bulk_boundary", "chapters/connections/ht_bulk_boundary_line_core.tex", "HT bulk-boundary. Verify derived center = bulk (not bar complex = bulk). Cross-check with Costello-Li."),
    ("M33_v2_celestial", "chapters/connections/celestial_holography_core.tex", "Celestial holography. Verify shadow tower connections. Cross-check with Strominger soft theorems."),
    ("M34_v2_hochschild", "chapters/theory/hochschild.tex", "Vol II Hochschild. Verify THREE Hochschild theories distinguished (AP197). CHIRAL Hochschild only."),
    ("M35_v2_ordered_kd", "chapters/connections/ordered_associative_chiral_kd.tex", "Ordered KD bridge. Verify E1-first. Modular operad breakthroughs consistent with Vol I."),
    ("M36_v2_holographic", "chapters/connections/thqg_holographic_reconstruction.tex", "Holographic reconstruction. Verify boundary-linear bulk proved; global triangle conjectural."),
    ("M37_v2_soft_graviton", "chapters/connections/thqg_soft_graviton_theorems.tex", "Soft graviton. Cross-check with shadow tower. Verify scope."),
    ("M38_v2_perturbative_fin", "chapters/connections/thqg_perturbative_finiteness.tex", "Perturbative finiteness. Verify genus-2 graph count=7. Cross-check with Faber-Pandharipande."),
    ("M39_v2_modular_pva", "chapters/connections/thqg_modular_pva_extensions.tex", "Modular PVA. Verify V2-AP34 divided-power convention. Cross-check with Beilinson-Drinfeld PVA."),
    ("M40_v2_w_algebras", "chapters/examples/w-algebras-virasoro.tex + chapters/examples/w-algebras-w3.tex", "W-algebra examples. Verify lambda-bracket conventions. W_2=Vir specialization. Cross-check FZ [FZ92]."),
    ("M41_v2_rosetta", "chapters/examples/rosetta_stone.tex", "Rosetta stone. Verify all family translations. Cross-check convention bridges."),
    ("M42_v2_preface", "chapters/frame/preface.tex", "Vol II preface. Verify geometric escalation ladder. No scope inflation. Symphonic standard."),
    ("M43_v2_brace_signs", "appendices/brace-signs.tex", "Brace signs appendix. Verify sign conventions. Cross-check with Getzler-Jones [GJ94]."),
    ("M44_v2_conclusion", "chapters/connections/conclusion.tex", "Conclusion. Verify frontier directions match current state. No stale claims."),
    ("M45_v2_standalones", "standalone/", "Vol II standalones. Verify all match current manuscript. Macros via providecommand. No stale scope."),
]

for mid, target, desc in V2_TARGETS:
    agent(mid, f"""TARGET: {target}
SCOPE: Last 200 commits. Run: git log --oneline -200 -- {target.split('+')[0].strip()} | head -20
{desc}
Read the file. Audit. Cross-check literature. Provide alternative proofs.
For each finding: PROBLEM + FIX.""", cwd=VOL2)


# ═══════════════════════════════════════════════════════════════════
# TIER 3: VOL III DEEP HEALING (20 agents)
# ═══════════════════════════════════════════════════════════════════

V3_TARGETS = [
    ("M46_v3_cy_to_chiral", "chapters/theory/cy_to_chiral.tex", "CY-to-chiral functor. CY-A proved d=2 only. d=3 conditional. Cross-check with Costello [Cos11] CY categories. Verify kappa_ch domain (AP182)."),
    ("M47_v3_fukaya", "chapters/theory/fukaya_categories.tex", "Fukaya categories. Verify pi_3(BU)=0 (AP181). E_1 obstruction = antisymmetric Euler form. Cross-check with Kontsevich HMS."),
    ("M48_v3_en_factorization", "chapters/theory/e_n_factorization.tex", "E_n factorization. Verify Bott periodicity. E_1 for d>=3. Cross-check with Lurie HA E_n."),
    ("M49_v3_e1_chiral", "chapters/theory/e1_chiral_algebras.tex", "E_1-chiral algebras. Verify five notions distinguished (AP161). Cross-check with Etingof-Kazhdan."),
    ("M50_v3_e2_chiral", "chapters/theory/e2_chiral_algebras.tex", "E_2-chiral algebras. Verify braided ≠ symmetric. SC ≠ E_3 correction. Cross-check with Tamarkin formality."),
    ("M51_v3_quantum_chiral", "chapters/theory/quantum_chiral_algebras.tex", "Quantum chiral algebras. Verify QG equivalence scope (AP174). Cross-check with Etingof-Kazhdan quantization."),
    ("M52_v3_bar_cobar_bridge", "chapters/theory/bar_cobar_bridge.tex", "CY bar-cobar bridge. Bar Euler = Borcherds. Verify kappa_BKM=5 for K3xE. Cross-check with Gritsenko-Nikulin."),
    ("M53_v3_braided_fact", "chapters/theory/braided_factorization.tex", "Braided factorization. Verify E_2 claims. Cross-check with Fresse [Fre17] E_n operads."),
    ("M54_v3_introduction", "chapters/theory/introduction.tex", "Vol III introduction. Verify no scope inflation. CY-A d=2 only stated clearly."),
    ("M55_v3_k3_times_e", "chapters/examples/k3_times_e.tex", "K3xE. Verify kappa_ch=3, kappa_BKM=5 distinguished (AP113). Cross-check with Gritsenko-Nikulin-Sarti."),
    ("M56_v3_toric_cy3", "chapters/examples/toric_cy3_coha.tex", "Toric CY3 CoHA. Verify McKay quiver (AP183). Verify kappa_ch domain (AP182). Cross-check with Kontsevich-Soibelman CoHA."),
    ("M57_v3_toroidal", "chapters/examples/toroidal_elliptic.tex", "Toroidal/elliptic. Verify bc/bg signs fixed. Cross-check with Feigin-Odesskii, Miki."),
    ("M58_v3_holographic", "chapters/connections/cy_holographic_datum_master.tex", "CY holographic datum. Verify cross-volume bridges to Vol I/II. No stale claims."),
    ("M59_v3_compute_shadow", "compute/lib/*shadow* + compute/lib/*modular_cy*", "Shadow/modular CY engines. Run tests. Verify expected values. Cross-check with census."),
    ("M60_v3_compute_coproduct", "compute/lib/*coproduct* + compute/lib/*bialgebra*", "Coproduct engines. Run tests. Verify Hopf axioms. Create missing test files."),
    ("M61_v3_compute_e1_e2", "compute/lib/*e1* + compute/lib/*e2* + compute/lib/*e3*", "E_n engines. Run tests. Verify Koszul duality. Create missing test files."),
    ("M62_v3_compute_k3", "compute/lib/*k3* + compute/lib/*drinfeld*", "K3 + Drinfeld engines. Run tests. Verify kappa values match census."),
    ("M63_v3_compute_misc", "compute/lib/*tetrahedron* + compute/lib/*categorical* + compute/lib/*zamolodchikov*", "Frontier engines. Run tests. Verify axioms. These are the newest, least-verified engines."),
    ("M64_v3_CLAUDE_AGENTS", "CLAUDE.md + AGENTS.md", "Vol III constitutional files. Verify AP-CY1 through AP-CY19. Verify kappa subscripts. Verify CY-A scope."),
    ("M65_v3_readme_frontier", "README.md + FRONTIER.md", "Vol III documentation. Verify page counts, test counts, theorem status. No scope inflation."),
]

for mid, target, desc in V3_TARGETS:
    agent(mid, f"""TARGET: {target}
SCOPE: Last 200 commits. Run: git log --oneline -200 -- {target.split('*')[0].split('+')[0].strip()} | head -20
{desc}
Read the files. Audit. Cross-check literature. Provide alternative proofs.
For each finding: PROBLEM + FIX.""", cwd=VOL3)


# ═══════════════════════════════════════════════════════════════════
# TIER 4: CROSS-VOLUME LITERATURE + INDEPENDENT PROOFS (15 agents)
# ═══════════════════════════════════════════════════════════════════

XLIT = [
    ("M66_BD_full", "FULL Beilinson-Drinfeld cross-check. Read BD [BD04] Chapters 3-4. Verify: (a) our chiral Koszul duality extends BD's chiral homology, (b) our E_inf treatment is compatible, (c) Arnold form = BD's factorization structure. Write Remark[BD full comparison] in concordance."),
    ("M67_FG_full", "FULL Frenkel-Gaitsgory cross-check. Read FG [FG04/06]. Verify: (a) our critical level matches FG's center, (b) our Koszul at critical = FG's local Langlands, (c) Wakimoto consistency. Write Remark[FG full comparison]."),
    ("M68_CG_CFG_full", "FULL Costello-Gwilliam-Francis cross-check. CG [CG17/21] BV quantization + CFG [arXiv:2602.12412] E_3. Verify: (a) our MC5 = CG's BV, (b) our topologization = CFG's E_3, (c) our shadow tower = CFG's perturbative invariants."),
    ("M69_Lurie_full", "FULL Lurie cross-check. HA + DAG. Verify: (a) bar = Cech nerve, (b) cobar = totalization, (c) adjunction = nerve-realization, (d) E_n Koszul = Lurie's E_n duality. Write comparison."),
    ("M70_PTVV_Cal_full", "FULL PTVV + Calaque cross-check. Shifted symplectic. Verify: (a) our complementarity = shifted symplectic pairing, (b) our Lagrangian = PTVV Lagrangian intersection, (c) integration = Calaque-Scheimbauer."),
    ("M71_KS_full", "FULL Kontsevich-Soibelman. Wall-crossing, scattering, BPS. Verify: (a) Theta_A = KS scattering product, (b) shadow growth = KS stability, (c) G/L/C/M = KS BPS classes."),
    ("M72_Drinfeld_Yangian", "FULL Drinfeld Yangian cross-check. [Dri85/87]. Verify: (a) our Y(g)^{ch} extends classical Y_hbar(g), (b) R-matrix = Drinfeld's universal R, (c) coproduct = Drinfeld coproduct. Write comparison with explicit convention bridge."),
    ("M73_EV_elliptic", "Etingof-Varchenko elliptic cross-check. Verify: (a) our genus-1 R-matrix matches EV's elliptic R, (b) KZB connection consistent. Cross-check with Bernard [Ber88], Felder [Fel94], CEE [CEE09]."),
    ("M74_LV_operadic", "Loday-Vallette operadic cross-check. [LV12]. Verify: (a) our SC Koszulity matches LV colored operad theory, (b) SC^! dimension formulas, (c) homotopy transfer = LV transfer."),
    ("M75_GNS_BKM", "Gritsenko-Nikulin-Sarti BKM cross-check (Vol III). Verify: (a) our kappa_BKM = 5 for K3xE matches Phi_10 weight, (b) our Borcherds product matches GNS, (c) root multiplicities consistent."),
    ("M76_alt_thm_A_via_infinity_cat", "ALTERNATIVE PROOF of Theorem A via infinity-categorical methods. Use Lurie's bar-cobar for E_1-algebras in a presentable stable infinity-category. Specialize to D-mod on Ran(X)."),
    ("M77_alt_thm_D_via_GRR", "ALTERNATIVE PROOF of Theorem D via Grothendieck-Riemann-Roch. Direct: fiber bar complex = complex of vector bundles on M-bar_g. GRR on universal curve gives ch(R*pi_*(B_fib)) = kappa*ch(E)."),
    ("M78_alt_topol_via_factorization", "ALTERNATIVE PROOF of topologization via factorization homology. The 3d HT theory = E_3 factorization algebra. Boundary = A. Bulk observables = derived center. E_3 automatic from 3d structure."),
    ("M79_alt_complementarity_via_index", "ALTERNATIVE DERIVATION of complementarity K(A) via index theory. K = Euler characteristic of total bar complex = topological invariant of the operad. K(Com)=0, K(ChirAss)=family-dependent."),
    ("M80_session_summary_final", "DEFINITIVE SESSION SUMMARY. Total agents: 732. Write compute/audit/session_2026_04_13_mega_rescue.md. State: proved/conditional/conjectural/open for every theorem. List alternative proofs. List literature confirmations. List remaining gaps. Be exhaustive and honest."),
]

for mid, desc in XLIT:
    agent(mid, desc)


# ═══════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Mega Rescue Campaign — 100 agents")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--delay", type=int, default=45)
    args = parser.parse_args()

    print(f"Mega Rescue: {len(AGENTS)} agents -> {OUT}")
    print(f"Tiers: {sum(1 for a in AGENTS if a['id'].startswith('M') and int(a['id'][1:3])<=25)} V1, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('M') and 26<=int(a['id'][1:3])<=45)} V2, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('M') and 46<=int(a['id'][1:3])<=65)} V3, "
          f"{sum(1 for a in AGENTS if a['id'].startswith('M') and int(a['id'][1:3])>=66)} xlit")
    print(f"Batch: {args.batch_size}, Timeout: {args.timeout}s, Delay: {args.delay}s\n")

    ok, fail = 0, 0
    results = []
    for i in range(0, len(AGENTS), args.batch_size):
        batch = AGENTS[i:i + args.batch_size]
        bn = i // args.batch_size + 1
        tb = (len(AGENTS) + args.batch_size - 1) // args.batch_size
        print(f"=== Batch {bn}/{tb} ({len(batch)} agents) ===")
        with ThreadPoolExecutor(max_workers=args.batch_size) as ex:
            futs = {ex.submit(run_agent, a, args.timeout): a for a in batch}
            for f in as_completed(futs):
                aid, success, dt = f.result()
                ok += success; fail += (not success)
                results.append({"id": aid, "ok": success, "time": dt})
                print(f"  [{ok+fail}/{len(AGENTS)}] {'OK' if success else 'FAIL'} {aid} ({dt:.0f}s)")
        if i + args.batch_size < len(AGENTS):
            print(f"  (cooldown {args.delay}s)")
            time.sleep(args.delay)

    summary = [f"# Mega Rescue Summary — {TS}\n",
               f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
