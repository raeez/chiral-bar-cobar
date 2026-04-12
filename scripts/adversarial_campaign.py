#!/usr/bin/env python3
"""
Adversarial Beilinson Audit Campaign — 105 Codex Agents
First-principles reconstitution of all recent work across 3 volumes.

Launches via `codex exec` with GPT-5.4 at xhigh reasoning effort.
Each agent reads files, greps, runs tests, and reports findings.
No agent modifies any file — pure adversarial audit.

Usage:
    python3 scripts/adversarial_campaign.py [--batch-size 15] [--timeout 900]
"""

import subprocess
import os
import sys
import time
import json
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"audit_campaign_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Agent infrastructure
# ---------------------------------------------------------------------------

AGENTS = []

PREAMBLE = """\
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics \
manuscript on operadic Koszul duality in the chiral realm (3 volumes). \
Your mission is FALSIFICATION — assume everything is WRONG until independently verified \
from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. \
If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. \
Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. \
Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>
"""


def agent(aid, prompt, cwd=VOL1, model="gpt-5.4"):
    """Register an agent. All agents use gpt-5.4 (ChatGPT account constraint)."""
    AGENTS.append({
        "id": aid,
        "prompt": PREAMBLE + "\n\n" + prompt,
        "cwd": cwd,
        "model": model,
    })


def run_agent(a, timeout=900):
    """Execute a single Codex agent via `codex exec`."""
    out_file = OUT / f"{a['id']}.md"
    t0 = time.time()
    try:
        r = subprocess.run(
            ["codex", "exec", "-",
             "-m", a["model"],
             "-C", a["cwd"],
             "--full-auto"],
            input=a["prompt"],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        dt = time.time() - t0
        out_file.write_text(
            f"# {a['id']} ({dt:.0f}s, {a['model']})\n\n"
            f"{r.stdout}\n\n---\nSTDERR:\n{r.stderr}"
        )
        return a["id"], r.returncode == 0, dt
    except subprocess.TimeoutExpired:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — TIMEOUT after {dt:.0f}s\n")
        return a["id"], False, dt
    except Exception as e:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — ERROR: {e}\n")
        return a["id"], False, dt


# ═══════════════════════════════════════════════════════════════════════════
# TIER 1: THEOREM FALSIFICATION (20 agents, o3)
# Try to BREAK each main theorem's proof.
# ═══════════════════════════════════════════════════════════════════════════

THEOREMS = [
    ("T01_thm_A", "Theorem A: bar-cobar adjunction + Verdier intertwining on Ran(X). Find the proof. Check: (a) does each step follow? (b) are all cited lemmas proved? (c) is scope correct (genus, level, Koszul locus)? (d) any four-functor confusion (AP25/AP34/AP50)? (e) does B^ord vs B^Sigma matter?"),
    ("T02_thm_B", "Theorem B: bar-cobar inversion Omega(B(A))→A qi on Koszul locus. Check: (a) is Koszul locus correctly defined? (b) does the qi actually induce iso on cohomology? (c) is the model structure correct? (d) what happens OFF the Koszul locus?"),
    ("T03_thm_C0", "Theorem C0: fiber-center identification (unconditional). Check: (a) what exactly is identified? (b) is it really unconditional or are there hidden hypotheses? (c) does it work for ALL families or only specific ones?"),
    ("T04_thm_C1", "Theorem C1: Lagrangian eigenspace decomposition (unconditional). Check: (a) what is the eigenspace decomposition? (b) why is it Lagrangian? (c) what pairing? (d) is it really unconditional?"),
    ("T05_thm_C2", "Theorem C2: scalar BV pairing (conditional on uniform-weight). Check: (a) what is the condition? (b) does uniform-weight actually suffice? (c) what fails at multi-weight? (d) is the delta_F_g^cross correction properly scoped?"),
    ("T06_thm_D", "Theorem D: obs_g = kappa*lambda_g at uniform weight. Check: (a) is the formula correct? (b) what is the scope (genus, weight)? (c) is the proof complete? (d) does multi-weight really need delta_F_g^cross? (e) is F_1=kappa/24 a sanity check?"),
    ("T07_thm_H", "Theorem H: ChirHoch*(A) polynomial Hilbert series, concentrated in {0,1,2}. Check: (a) is this really for ALL families? (b) what is the Hilbert series? (c) is concentration in {0,1,2} proved or just computed? (d) is this amplitude or vdim (AP134)?"),
    ("T08_MC1_PBW", "MC1: PBW theorem. Find the proof. Check completeness and correctness of the PBW filtration."),
    ("T09_MC2_theta", "MC2: MC element Theta_A existence (bar-intrinsic). Check: (a) is the construction truly bar-intrinsic? (b) all-degree convergence? (c) is it in g^{E1} or g^mod?"),
    ("T10_MC3_thickgen", "MC3: thick generation. Check: (a) type A unconditional, outside type A conditional—is this correctly stated? (b) what is the condition? (c) layer 3 shifted prefundamental generation?"),
    ("T11_MC4_completion", "MC4: completion tower. Check: (a) is the tower convergent? (b) MC4+ SOLVED, MC4-0 finite resonance—verify."),
    ("T12_MC5_BV_bar", "MC5: BV/bar identification. Status: analytic proved, coderived proved, chain conjectural. Check: (a) what exactly is proved at each level? (b) is class M chain-level really false? (c) is the coderived result correct?"),
    ("T13_koszul_equivs", "10+1+1 Koszul equivalences. Find and audit each. Are there really 10 unconditional? What are the +1+1?"),
    ("T14_topologization", "Topologization theorem: SC+Sugawara=E_3. Check: (a) proved ONLY for affine KM—is this correctly scoped? (b) non-critical level required? (c) is the proof cohomological? (d) class M chain-level status?"),
    ("T15_SC_formality", "SC-formality: A is SC-formal iff class G. Check: (a) is this an iff? (b) is the proof complete in both directions? (c) what exactly is SC-formality?"),
    ("T16_depth_gap", "Depth gap: d_alg in {0,1,2,inf}, gap at 3. Check: (a) why is 3 impossible? (b) are the four values realized? (c) is there confusion between d_gen and d_alg (AP131)?"),
    ("T17_chirhoch1_KM", "ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?"),
    ("T18_D2_moduli", "D^2=0 on moduli: convolution + ambient. Check: (a) convolution on M-bar_{g,n}—is this the right space? (b) ambient from Mok25—is the citation correct? (c) log FM vs classical?"),
    ("T19_theta_existence", "Theta_A existence: bar-intrinsic, all-degree inverse limit. Check: (a) is the inverse limit well-defined? (b) convergence? (c) is it in the correct convolution algebra?"),
    ("T20_gerstenhaber", "Gerstenhaber bracket on derived center. Check: (a) is this chiral or topological (AP164)? (b) is it on Z^{der}_{ch}(A)? (c) is the bracket correctly defined via OPE residues on FM_k(C)?"),
]

for tid, desc in THEOREMS:
    agent(tid, f"""MISSION: FALSIFY the proof of {desc}

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.""", model="gpt-5.4")


# ═══════════════════════════════════════════════════════════════════════════
# TIER 2: FORMULA CENSUS FALSIFICATION (20 agents, o4-mini)
# Verify every instance of each formula family.
# ═══════════════════════════════════════════════════════════════════════════

FORMULAS = [
    ("F01_kappa_KM", "kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)", "Affine KM kappa", "grep -rn 'kappa.*dim.*h' chapters/ appendices/ standalone/ | head -50", "k=0→dim(g)/2 (NOT 0); k=-h^v→0. WRONG: dim(g)*k/(2h^v), k/2, c/2"),
    ("F02_kappa_Vir", "kappa(Vir_c) = c/2", "Virasoro kappa", "grep -rn 'kappa.*Vir\\|kappa.*c/2' chapters/ | head -50", "c=0→0; c=13→13/2. WRONG: c, c/24, c/12"),
    ("F03_kappa_Heis", "kappa(H_k) = k", "Heisenberg kappa", "grep -rn 'kappa.*Heis\\|kappa.*H_k' chapters/ | head -50", "k=0→0; k=1→1. WRONG: k/2"),
    ("F04_kappa_WN", "kappa(W_N) = c*(H_N - 1)", "W_N kappa", "grep -rn 'kappa.*W_N\\|H_N.*-.*1\\|H_{N-1}' chapters/ | head -50", "N=2→c/2=Vir. WRONG: c*H_{N-1} (AP136)"),
    ("F05_r_KM", "r^KM(z) = k*Omega/z [trace-form]", "KM r-matrix", "grep -rn 'Omega.*z\\|r(z).*Omega' chapters/ | head -50", "k=0→0. WRONG: Omega/z (bare, AP126)"),
    ("F06_r_Heis", "r^Heis(z) = k/z", "Heis r-matrix", "grep -rn 'r.*Heis\\|r(z).*k/z' chapters/ | head -30", "k=0→0. WRONG: 1/z"),
    ("F07_r_Vir", "r^Vir(z) = (c/2)/z^3 + 2T/z", "Vir r-matrix", "grep -rn 'r.*Vir\\|c/2.*z.*3' chapters/ | head -30", "Cubic+simple. WRONG: (c/2)/z^4"),
    ("F08_c_bc", "c_bc(lambda) = 1 - 3(2*lambda-1)^2", "bc central charge", "grep -rn 'c_bc\\|c_{bc}\\|1.*3.*2.*lambda' chapters/ | head -30", "lambda=2→-26. WRONG: 2(6L^2-6L+1)"),
    ("F09_c_bg", "c_bg(lambda) = 2(6*lambda^2-6*lambda+1)", "bg central charge", "grep -rn 'c_bg\\|c_{beta.*gamma}\\|6.*lambda.*2' chapters/ | head -30", "lambda=2→+26. WRONG: 1-3(2L-1)^2"),
    ("F10_bar_complex", "B(A) = T^c(s^{-1} A-bar)", "Bar complex definition", "grep -rn 'T\\^c\\|bar.*complex\\|B(A)' chapters/ | head -50", "Uses A-bar=ker(epsilon). WRONG: T^c(s^{-1} A), T^c(s A-bar)"),
    ("F11_desuspension", "|s^{-1}v| = |v| - 1", "Desuspension grading", "grep -rn 's\\^{-1}\\|desuspension\\|suspension' chapters/ | head -30", "LOWERS degree. WRONG: +1"),
    ("F12_MC_equation", "d*Theta + (1/2)[Theta,Theta] = 0", "MC equation", "grep -rn 'Maurer.*Cartan\\|Theta.*Theta\\|MC.*equation' chapters/ | head -30", "Has 1/2 coefficient. WRONG: drop 1/2"),
    ("F13_eta", "eta(tau) = q^{1/24} * prod(1-q^n)", "Dedekind eta", "grep -rn 'eta.*tau\\|eta.*q\\|q\\^{1/24}' chapters/ | head -30", "q^{1/24} ESSENTIAL. WRONG: missing prefactor"),
    ("F14_averaging", "av(r(z)) + dim(g)/2 = kappa for non-abelian KM", "Averaging identity", "grep -rn 'av.*r.*kappa\\|averaging.*map' chapters/ | head -30", "Sugawara shift for non-abelian. WRONG: av(r)=kappa universally"),
    ("F15_S2", "S_2 = kappa for ALL families", "Shadow invariant S_2", "grep -rn 'S_2\\|S_{2}' chapters/ standalone/ | head -50", "S_2=kappa=c/2 for Vir. WRONG: c/12 (AP177)"),
    ("F16_cauchy", "Cauchy: 1/(2*pi*i)", "Cauchy integral normalization", "grep -rn '2.*pi.*oint\\|1.*2.*pi' chapters/ | head -30", "WRONG: 1/(2*pi) missing i (AP120)"),
    ("F17_K_BP", "K(BP) = 196", "BP Koszul conductor", "grep -rn 'K.*BP\\|Bershadsky.*Polyakov.*196\\|Bershadsky.*Polyakov.*K' chapters/ | head -30", "WRONG: K_BP=2 (AP140)"),
    ("F18_complementarity", "K(Vir)=13, K(KM)=0", "Complementarity", "grep -rn 'complementarity\\|self-dual.*c.*13\\|kappa.*kappa.*prime' chapters/ | head -30", "Self-dual c=13. WRONG: c=26, universal 0"),
    ("F19_arnold_KZ", "KZ: sum r_{ij} dz_{ij}, NOT d log", "Arnold vs KZ", "grep -rn 'd.*log.*z\\|nabla.*KZ\\|Arnold' chapters/ | head -30", "Arnold form is bar coeff, NOT connection (AP117)"),
    ("F20_WN_weights", "W_N generators at {2,...,N}", "W_N weight range", "grep -rn 'W_N.*generator\\|weight.*range\\|{2.*N}' chapters/ | head -20", "N-1 generators. WRONG: {2,...,N+1}"),
]

for fid, canonical, name, grep_cmd, checks in FORMULAS:
    agent(fid, f"""MISSION: Verify every instance of {name} across all .tex files.

CANONICAL: {canonical}
CHECKS: {checks}

STEPS:
1. Run: {grep_cmd}
2. Also search in Vol II: grep -rn similar patterns ~/chiral-bar-cobar-vol2/chapters/ | head -30
3. Also search in Vol III: grep -rn similar patterns ~/calabi-yau-quantum-groups/chapters/ | head -30
4. For EACH hit, verify the formula matches the canonical form
5. Check boundary values
6. Flag ANY discrepancy, even minor notation differences
7. Also check landscape_census.tex for the canonical source""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER 3: ANTI-PATTERN DRAGNET (25 agents, o4-mini)
# Each agent sweeps for specific banned patterns across all 3 volumes.
# ═══════════════════════════════════════════════════════════════════════════

AP_SWEEPS = [
    ("AP01_bare_omega", "AP126: bare Omega/z without level prefix", r"grep -rn '\\\\Omega.*z\b' chapters/ standalone/ | grep -v 'k.*Omega' | grep -v 'level' | head -50", "Every Omega/z MUST have k prefix"),
    ("AP02_quartic_vir", "B2: quartic Virasoro r-matrix (c/2)/z^4", r"grep -rn 'z\^4\\|z\^\{4\}' chapters/ | grep -i 'vir\|r(z)' | head -20", "Vir r-matrix is CUBIC z^3, NOT quartic"),
    ("AP03_wrong_WN_kappa", "AP136/B7: kappa(W_N) = c*H_{N-1}", r"grep -rn 'H_{N-1}' chapters/ | head -30", "MUST be c*(H_N - 1), NOT c*H_{N-1}"),
    ("AP04_bare_A_bar", "AP132/B14: T^c(s^{-1} A) without augmentation", r"grep -rn 'T\^c.*s\^{-1}.*A[^-]' chapters/ | head -30", "MUST use A-bar = ker(epsilon)"),
    ("AP05_wrong_suspension", "AP22/B15-B16: wrong suspension direction", r"grep -rn 's\^{-1}.*|v|.*\+.*1\|T\^c(s\s' chapters/ | head -20", "Must be |v|-1, not +1; s^{-1} not bare s"),
    ("AP06_missing_eta_prefix", "B17: eta missing q^{1/24}", r"grep -rn 'eta.*prod.*1-q\|eta.*=.*\\prod' chapters/ | head -20", "MUST include q^{1/24} prefactor"),
    ("AP07_env_mismatch", "AP40: environment/tag mismatch", r"grep -B2 'ClaimStatusConjectured' chapters/ | grep 'begin{theorem}\|begin{proposition}\|begin{corollary}' | head -30", "Conjectured → conjecture env"),
    ("AP08_proof_after_conj", "AP4: proof after conjecture", r"grep -B10 'begin{proof}' chapters/ | grep 'begin{conjecture}\|begin{heuristic}' | head -20", "Use Remark[Evidence] not proof"),
    ("AP09_label_prefix", "AP125: label prefix mismatch", r"grep -n 'begin{conjecture}' chapters/ | while read line; do file=$(echo $line | cut -d: -f1); num=$(echo $line | cut -d: -f2); grep -A5 \"^\" $file | head -6 | grep 'label{thm:'; done 2>/dev/null | head -20", "conj env needs conj: prefix"),
    ("AP10_AI_slop", "AP29: AI slop vocabulary", r"grep -rni 'moreover\|additionally\|notably\|crucially\|remarkably\|interestingly\|furthermore\|delve\|leverage\|tapestry\|cornerstone' chapters/ | head -50", "Banned vocabulary"),
    ("AP11_em_dash", "B41: em dashes", r"grep -rn '---\|—' chapters/ | head -30", "FORBIDDEN: use colon/semicolon/separate sentence"),
    ("AP12_markdown_latex", "AP121/B40: markdown in LaTeX", r"grep -rn '`[0-9]\|\\*\\*\|_[a-z]' chapters/ | head -20", "Use $...$, textbf, emph"),
    ("AP13_hardcoded_part", "FM10/B33: hardcoded Part numbers", r"grep -rn 'Part~[IVXL]\|Chapter~[0-9]' chapters/ | head -30", "Use \\ref{part:...}"),
    ("AP14_bare_kappa_v3", "AP113: bare kappa in Vol III", r"grep -rn '\\kappa[^_]' ~/calabi-yau-quantum-groups/chapters/ | grep -v 'kappa_' | head -50", "MUST be subscripted"),
    ("AP15_duplicate_labels", "AP124: duplicate labels across volumes", r"grep -roh '\\label{[^}]*}' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -d | head -30", "Labels must be unique across volumes"),
    ("AP16_arity_banned", "AP176: arity is BANNED", r"grep -rni '\\barity\\b' chapters/ appendices/ standalone/ | head -20", "Must return ZERO hits"),
    ("AP17_E3_chiral", "AP168/B58: E_3-chiral for topologized", r"grep -rni 'E_3.*chiral\|E_3-chiral\|E_{3}.*chiral' chapters/ | head -20", "MUST be E_3-TOPOLOGICAL"),
    ("AP18_SC_self_dual", "AP166/B57: SC Koszul self-dual claim", r"grep -rni 'self-dual\|self.*dual' chapters/ | grep -i 'SC\|Swiss.*cheese' | head -20", "SC is NOT self-dual"),
    ("AP19_B_SC_coalgebra", "AP165/B54: B(A) is SC-coalgebra claim", r"grep -rni 'bar.*SC\|B(A).*SC\|coalgebra.*SC\|SC.*coalgebra' chapters/ | head -20", "B(A) is E_1 coalgebra, NOT SC"),
    ("AP20_over_point_P1", "AP142/B53: over a point is over P^1", r"grep -rni 'over a point\|over.*P.*1' chapters/ | head -20", "FALSE: retract is DATA, disk!=point"),
    ("AP21_topologization_scope", "AP167/B59: topologization scope inflation", r"grep -rni 'topologization\|topologisation' chapters/ | grep -i 'proved\|general\|all' | head -20", "ONLY proved for affine KM at non-critical level"),
    ("AP22_S2_c12", "AP177/B62: S_2 = c/12", r"grep -rn 'S_2.*c/12\|S_2.*=.*c.*12\|S_{2}.*c/12' chapters/ standalone/ ~/chiral-bar-cobar-vol2/chapters/ | head -20", "WRONG: S_2 = kappa = c/2"),
    ("AP23_pi3_BU", "AP181/B69: pi_3(BU) = Z", r"grep -rn 'pi_3.*BU\|pi_{3}.*BU' chapters/ ~/calabi-yau-quantum-groups/chapters/ | head -20", "WRONG: pi_3(BU) = 0 by Bott"),
    ("AP24_undefined_macros", "FM6: undefined macros in standalone", r"grep -rn '\\\\cW\|\\\\hol\|\\\\Ran\|\\\\FM\|\\\\chHoch' standalone/ | head -20", "Must be defined via providecommand"),
    ("AP25_slop_v2_v3", "AP29 across Vol II and Vol III", r"grep -rni 'moreover\|additionally\|notably\|crucially\|remarkably\|furthermore\|delve\|leverage' ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ | head -50", "Banned in all volumes"),
]

for apid, name, cmd, expected in AP_SWEEPS:
    agent(apid, f"""MISSION: Sweep for {name} across all three volumes.

Run: {cmd}

Expected: {expected}

For EACH hit:
1. Read surrounding context to determine if it's a genuine violation
2. Distinguish false positives from real violations
3. Report file:line and the exact violating text
4. Assess severity (CRITICAL if mathematical, HIGH if structural, MEDIUM if prose)""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER 4: CROSS-VOLUME CONSISTENCY (15 agents, o4-mini)
# ═══════════════════════════════════════════════════════════════════════════

XV_CHECKS = [
    ("XV01_kappa_xvol", "Kappa formulas", "kappa", "Are kappa formulas consistent across volumes? Check kappa(KM), kappa(Vir), kappa(Heis), kappa(W_N) in all .tex files across all 3 repos."),
    ("XV02_rmatrix_xvol", "r-matrix conventions", "r-matrix", "Are r-matrix conventions consistent? Check trace-form vs KZ, level prefix presence, across all 3 repos."),
    ("XV03_bar_def_xvol", "Bar complex B(A) definition", "bar complex", "Is B(A)=T^c(s^{-1}A-bar) consistent? Check augmentation ideal, desuspension direction, across all 3 repos."),
    ("XV04_SC_claims_xvol", "SC^{ch,top} claims", "SC", "Are SC^{ch,top} claims consistent? Check: (a) no B(A)=SC coalgebra claims, (b) SC emerges on derived center pair, (c) SC not self-dual, across all 3 repos."),
    ("XV05_topologization_xvol", "Topologization scope", "topologization", "Is topologization scope consistent? Check: proved for affine KM only, conjectural general, across all 3 repos."),
    ("XV06_hochschild_xvol", "Hochschild disambiguation", "Hochschild", "Are the three Hochschild theories correctly distinguished? Check: chiral/topological/categorical never conflated, across all 3 repos."),
    ("XV07_yangian_xvol", "Yangian type distinctions", "Yangian", "Are the four Yangian types distinguished? Classical/dg-shifted/chiral/spectral. Check for conflation across all 3 repos."),
    ("XV08_thm_status_xvol", "Theorem status vs proofs", "theorem status", "Do theorem status claims in concordance.tex, metadata, and README match what's actually proved in the .tex files? Check all five theorems A-D+H."),
    ("XV09_label_unique_xvol", "Label uniqueness", "labels", "Are there any duplicate \\label{} across all 3 repos? Run: grep -roh '\\\\label{[^}]*}' across all volumes, find duplicates."),
    ("XV10_convention_bridge", "Convention bridges (OPE/lambda/motivic)", "conventions", "When formulas appear in both Vol I (OPE modes) and Vol II (lambda-brackets), is the conversion correct? Check c/2 vs c/12 divided-power, etc."),
    ("XV11_claim_status_sync", "ClaimStatus consistency", "status", "Do ClaimStatus macros match theorem environments? Check for Conjectured in theorem env, ProvedHere in conjecture env, across all 3 repos."),
    ("XV12_part_refs", "Part/Chapter references", "references", "Are there hardcoded Part~/Chapter~ references that should be \\ref{part:...}? Check all 3 repos."),
    ("XV13_biblio_xvol", "Bibliography consistency", "bibliography", "Are cited references defined in bibliography? Check for [?] in compile logs or undefined citations across all 3 repos."),
    ("XV14_five_objects_xvol", "Five objects discipline", "objects", "Is the five-object distinction (A, B(A), A^i, A^!, Z^{der}) maintained everywhere? Check for conflation language across all 3 repos."),
    ("XV15_E1_first_xvol", "E1-first architecture", "E1-first", "Does every chapter construct the E1 ordered story first? Check for symmetric-bar results stated without E1 source, across all 3 repos."),
]

for xvid, name, keyword, desc in XV_CHECKS:
    agent(xvid, f"""MISSION: Cross-volume consistency check for {name}.

{desc}

Search across ALL three repos:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding, note: which volume, file:line, the inconsistency, and severity.""")


# ═══════════════════════════════════════════════════════════════════════════
# TIER 5: COMPUTE ENGINE VERIFICATION (10 agents, o4-mini)
# ═══════════════════════════════════════════════════════════════════════════

COMPUTE_CHECKS = [
    ("CE01_shadow_engines", "Shadow tower engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'shadow' --tb=short -q 2>&1 | tail -30. Check: do ALL shadow tower tests pass? Are expected values independently verified?"),
    ("CE02_central_charge", "Central charge engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'central_charge or ghost' --tb=short -q 2>&1 | tail -30. Check: bc/bg complementarity c_bc+c_bg=0?"),
    ("CE03_koszul_conductor", "Koszul conductor engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'koszul_conductor or complementarity' --tb=short -q 2>&1 | tail -30. Check: K(BP)=196? K(Vir)=13?"),
    ("CE04_rmatrix", "R-matrix engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'r_matrix or rmatrix' --tb=short -q 2>&1 | tail -30. Check: level prefix present? k=0→0?"),
    ("CE05_E8_dims", "E_8 dimensional engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'E8 or exceptional' --tb=short -q 2>&1 | tail -30. Check: adjoint=248?"),
    ("CE06_bar_cohom", "Bar cohomology engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'bar_cohom or sl_2' --tb=short -q 2>&1 | tail -30. Check: sl_2 H^2=5?"),
    ("CE07_DS_ghost", "DS ghost charge engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'ds_ghost or ghost_charge' --tb=short -q 2>&1 | tail -30. Check: W6/W7 ghost charges correct?"),
    ("CE08_stokes", "Stokes/asymptotic engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'stokes or asymptotic' --tb=short -q 2>&1 | tail -30. Check: Gevrey type correct?"),
    ("CE09_cy3_engines", "CY3 engines (Vol III)", "Run: cd ~/calabi-yau-quantum-groups && python3 -m pytest compute/tests/ --tb=short -q 2>&1 | tail -30. Check: all Vol III tests pass?"),
    ("CE10_gerstenhaber", "Gerstenhaber bracket engines", "Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'gerstenhaber' --tb=short -q 2>&1 | tail -30. Check: bracket computations correct?"),
]

for ceid, name, desc in COMPUTE_CHECKS:
    agent(ceid, desc + f"\n\nAlso check: are hardcoded expected values in test files cited with 2+ independent sources (AP10/AP128)? Read the test file and verify.", model="gpt-5.4")


# ═══════════════════════════════════════════════════════════════════════════
# TIER 6: BOUNDARY/DEGENERATE CASE ASSAULT (10 agents, o3)
# ═══════════════════════════════════════════════════════════════════════════

BOUNDARY_CHECKS = [
    ("BC01_k_zero", "k=0 (abelian limit)", "Find ALL formulas that depend on parameter k. Evaluate at k=0. Check: r-matrix→0 (AP126)? kappa(KM)→dim(g)/2 (NOT 0)? kappa(Heis)→0? Algebra becomes abelian but is still Koszul. k=0 is NOT the critical level."),
    ("BC02_k_critical", "k=-h^v (critical level)", "Find ALL formulas involving h^v or critical level. At k=-h^v: kappa→0, center jumps (Feigin-Frenkel), Sugawara undefined, topologization FAILS. Check all claims are properly scoped."),
    ("BC03_c_zero", "c=0", "Find ALL formulas involving central charge c. At c=0: kappa(Vir)→0, kappa(Heis at k=0)→0. Check: does the theory degenerate gracefully?"),
    ("BC04_c_13", "c=13 (Virasoro self-dual)", "At c=13: kappa=13/2, K(Vir)=13. The Virasoro algebra is Koszul self-dual. Check all c=13 claims."),
    ("BC05_c_26", "c=26 (string critical)", "At c=26: matter-ghost cancellation. This is NOT the self-dual point (that's c=13). Check for c=26 confused with self-duality."),
    ("BC06_genus_0", "g=0", "Check all genus-0 claims. At g=0: no curvature (d^2=0), the bar complex is uncurved. FM_n(C) configuration spaces. Is everything correct?"),
    ("BC07_genus_1", "g=1", "Check all genus-1 claims. At g=1: obs_1=kappa*lambda_1 unconditional (all-weight). Period matrix is scalar 1/Im(tau). E_2* quasi-modular forms appear. Check proper scoping."),
    ("BC08_genus_2", "g=2", "Check all genus-2 claims. At g=2: period matrix is 2x2 (AP118). Multi-weight correction delta_F_g^cross appears. Stable graph count=7 (AP123). Verify."),
    ("BC09_N_2", "N=2 (W_2 = Virasoro)", "At N=2: W_2 must reduce to Virasoro. kappa(W_2)=c*(H_2-1)=c/2. Check all W_N formulas specialize correctly."),
    ("BC10_sl2", "sl_2 (smallest non-abelian)", "sl_2 is the smallest non-abelian case. dim(sl_2)=3, h^v=2. kappa=3(k+2)/4. bar H^2=5 (NOT 6). Check all sl_2 computations."),
]

for bcid, name, desc in BOUNDARY_CHECKS:
    agent(bcid, f"""MISSION: Boundary/degenerate case assault at {name}.

{desc}

Search ALL .tex files in chapters/ for formulas involving the relevant parameter.
For EACH formula found:
1. Substitute the boundary value
2. Verify the result is correct
3. Check the manuscript states the correct boundary behavior
4. Flag any discrepancy""", model="gpt-5.4")


# ═══════════════════════════════════════════════════════════════════════════
# TIER 7: STRUCTURAL INTEGRITY (5 agents, o4-mini)
# ═══════════════════════════════════════════════════════════════════════════

STRUCT_CHECKS = [
    ("SI01_broken_refs_v1", "Find broken \\ref in Vol I. Run: grep -rn '\\\\ref{' chapters/ | head -100. For each ref, check the corresponding \\label exists. Also check compile log for undefined references."),
    ("SI02_broken_refs_v2", "Find broken \\ref in Vol II. Run: grep -rn '\\\\ref{' ~/chiral-bar-cobar-vol2/chapters/ | head -100. Check labels exist. Check compile log."),
    ("SI03_missing_provedhere", "Find theorems tagged ProvedHere that lack a \\begin{proof}. Run: grep -B5 'ClaimStatusProvedHere' chapters/ | grep 'begin{theorem}\\|begin{proposition}' | head -30. For each, check a proof block follows."),
    ("SI04_missing_tags", "Find theorem/proposition environments without ANY ClaimStatus tag. These are untagged claims. Run: grep -A3 'begin{theorem}\\|begin{proposition}' chapters/ | grep -v 'ClaimStatus' | head -50."),
    ("SI05_test_coverage", "Find compute engines without matching test files. Run: ls compute/lib/*.py | while read f; do base=$(basename $f .py); if [ ! -f compute/tests/test_${base}.py ]; then echo MISSING: $f; fi; done | head -30."),
]

for siid, desc in STRUCT_CHECKS:
    agent(siid, desc + "\n\nReport every finding with file:line.")


# ═══════════════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Adversarial Beilinson Audit Campaign")
    parser.add_argument("--batch-size", type=int, default=15,
                        help="Number of concurrent agents per batch")
    parser.add_argument("--timeout", type=int, default=900,
                        help="Timeout per agent in seconds")
    parser.add_argument("--tier", type=str, default="all",
                        help="Run specific tier: T,F,AP,XV,CE,BC,SI or 'all'")
    args = parser.parse_args()

    # Filter agents by tier if specified
    agents = AGENTS
    if args.tier != "all":
        prefix_map = {
            "T": "T", "F": "F", "AP": "AP", "XV": "XV",
            "CE": "CE", "BC": "BC", "SI": "SI"
        }
        prefix = prefix_map.get(args.tier, args.tier)
        agents = [a for a in AGENTS if a["id"].startswith(prefix)]

    print(f"Campaign: {len(agents)} agents → {OUT}")
    print(f"Models: {sum(1 for a in agents if a['model']=='gpt-5.4')} gpt-5.4")
    print(f"Batch size: {args.batch_size}, Timeout: {args.timeout}s")
    print()

    ok, fail = 0, 0
    results = []

    for i in range(0, len(agents), args.batch_size):
        batch = agents[i:i + args.batch_size]
        batch_num = i // args.batch_size + 1
        total_batches = (len(agents) + args.batch_size - 1) // args.batch_size
        print(f"=== Batch {batch_num}/{total_batches} ({len(batch)} agents) ===")

        with ThreadPoolExecutor(max_workers=args.batch_size) as executor:
            futures = {executor.submit(run_agent, a, args.timeout): a for a in batch}
            for future in as_completed(futures):
                aid, success, dt = future.result()
                status = "OK" if success else "FAIL"
                ok += success
                fail += (not success)
                results.append({"id": aid, "ok": success, "time": dt})
                print(f"  [{ok + fail}/{len(agents)}] {status} {aid} ({dt:.0f}s)")

    # Write summary
    summary_lines = [
        f"# Adversarial Campaign Summary — {TS}",
        f"",
        f"Total: {len(agents)} | OK: {ok} | Failed: {fail}",
        f"",
        f"## Results",
        f"",
    ]
    for r in sorted(results, key=lambda x: x["id"]):
        status = "OK" if r["ok"] else "FAIL"
        summary_lines.append(f"- [{status}] {r['id']} ({r['time']:.0f}s)")

    (OUT / "SUMMARY.md").write_text("\n".join(summary_lines))

    print(f"\n{'=' * 60}")
    print(f"DONE. OK={ok} Failed={fail}")
    print(f"Results: {OUT}")
    print(f"Summary: {OUT / 'SUMMARY.md'}")


if __name__ == "__main__":
    main()
