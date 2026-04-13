#!/usr/bin/env python3
"""
Fix Campaign — 100 Codex Agents in 5 waves of 20.
Launch wave by wave: python3 scripts/fix_campaign_100.py --wave A

Waves:
  A: Failed rectification relaunch + critical structural fixes
  B: Status/label/reference integrity
  C: Formula and convention fixes across all volumes
  D: Prose discipline (AP4, AP32, Hochschild, slop, arity)
  E: Missing content, test gaps, orphaned chapters
"""

import subprocess, os, sys, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")

AGENTS = {"A": [], "B": [], "C": [], "D": [], "E": []}

FIX_PREAMBLE = """\
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \\ref and \\label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>
"""

AUDIT_PREAMBLE = """\
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>
"""


def agent(wave, aid, prompt, cwd=VOL1, preamble=FIX_PREAMBLE):
    AGENTS[wave].append({
        "id": aid, "prompt": preamble + "\n\n" + prompt,
        "cwd": cwd, "model": "gpt-5.4",
    })


def run_agent(a, timeout=1500):
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
# WAVE A: Failed rectification relaunch + critical structural (20)
# ═══════════════════════════════════════════════════════════════════

agent("A", "A01_koszul_pairs_rect", """TARGET: chapters/theory/chiral_koszul_pairs.tex

This is the LARGEST theory file. The previous rectification agent timed out.
Focus on the THREE most critical fixes only (do not try to rewrite the whole file):

1. Koszul equivalence (vii): currently listed as unconditional but proof only covers g=0.
   FIX: Move (vii) to conditional equivalences OR add "at genus 0" qualifier.

2. Koszul equivalence (viii): claims ChirHoch is free polynomial algebra, but Hochschild
   theorems only prove duality + concentration. FIX: Weaken (viii) to match proved content.

3. SC-formality converse: uses bilinear form C(x,y,z)=kappa(x,[y,z]) but kappa is scalar.
   FIX: Restrict to families with invariant bilinear form (KM, not betagamma).

Read the relevant sections ONLY (search for 'equiv' and 'SC-formal'). Do not read the whole file.""")

agent("A", "A02_hg_modular_rect", """TARGET: chapters/theory/higher_genus_modular_koszul.tex

Previous rectification agent timed out. Focus on TWO critical fixes:

1. MC1 PBW: Whitehead lemma applied to truncated current algebra without justification.
   At lines ~1011, 1027, 1294, 1776. FIX: Add explicit reduction: the truncated current
   algebra has the finite-dimensional semisimple g acting on weight-graded pieces;
   Whitehead applies to g, not to the full current algebra. Add a remark.

2. Theorem D circular dependency routing: thm:genus-universality <-> thm:family-index.
   FIX: Add routing remark (AP147) at the Theorem D proof identifying the non-circular
   anchor: shadow tower construction (independent) -> genus universality -> family index.
   Search for 'thm:genus-universality' and add the routing remark nearby.

Read only the relevant sections. Do not try to process the whole file.""")

agent("A", "A03_symplectic_polar", """TARGET: chapters/connections/thqg_symplectic_polarization.tex

FINDINGS: C1 involution sigma uses ev: C_g(A)^{vv} -> C_g(A) without reflexivity.
At lines ~197, 220. The vv construction requires finite-dimensional fiber-cohomology.
Also: Q_g(A) ≅ Q_g(A^!)^v for all g>=0 contradicts Q_0(A^!)=0 at g=0 (lines ~476, 694).

FIXES:
1. Add reflexivity/perfectness hypothesis to the involution construction.
2. Add g>=1 hypothesis to the duality statement, or fix the genus-0 identifications.

Read lines 150-250 and 450-700. Make minimal fixes.""")

agent("A", "A04_introduction", """TARGET: chapters/theory/introduction.tex

FINDINGS:
1. Line ~368: incorrectly attributes E1 ordered MC2 to thm:mc2-bar-intrinsic.
   That theorem proves g^{mod} only. E1 version is in e1_modular_koszul.tex:290.
   FIX: Change cross-reference to cite the E1 theorem correctly.

2. Lines ~2091-2092: advertises MC4 for V_k(g), Vir_c, W-algebras, lattices.
   But prop:standard-strong-filtration has issues (corrected in bar_cobar_adjunction_curved.tex).
   FIX: Add weight-completion qualifier.

Search for 'mc2-bar-intrinsic' and 'completed-bar-cobar-strong'. Fix cross-references.""")

agent("A", "A05_concordance", """TARGET: chapters/connections/concordance.tex

This is the CONSTITUTION. Must reflect all rectification changes.

FIXES:
1. Search for thm:family-index and thm:genus-universality. Add routing remark (AP147)
   breaking the circular dependency. The non-circular path: shadow tower -> universality -> family index.

2. Search for 'topologization' or 'topologisation'. Update status to reflect the split:
   (a) cohomological E_3 = ProvedHere for affine KM at non-critical level
   (b) chain-level E_3 = Conjectured in general

3. Search for MC5. Update to reflect: analytic proved, coderived proved, chain-level conjectural.
   The coderived proof is now clean (bv_brst.tex fixed).

4. Search for Koszul equivalences. Note that (vii) is g=0 only, (viii) weakened.

Do NOT rewrite the concordance. Only update the specific status entries.""")

agent("A", "A06_toroidal_v1", """TARGET: chapters/examples/toroidal_elliptic.tex (Vol I)

FINDING: Line ~2085: K3 CDR remark has bc/bg signs swapped.
States c_betagamma = -2, c_bc = +2. Should be c_bc = -2, c_bg = +2.
Canonical: c_bc(lambda=1) = 1-3(1)^2 = -2. c_bg(lambda=1) = 2(1) = +2.

FIX: Find line ~2085 and swap the signs. Also grep the rest of the file for
any other bc/bg sign issues.""")

agent("A", "A07_free_fields", """TARGET: chapters/examples/free_fields.tex

FINDINGS:
1. Lines ~1148-1166: A proved proposition says betagamma shadow tower vanishes on some line.
   This potentially contradicts depth-gap claim that betagamma has d_alg=2 (r_max=4).
2. Line ~1171: Global-depth theorem contradicts T-line theorem.

FIX: Read both propositions. Determine WHICH parameter line each refers to.
If different lines: add clarification distinguishing them.
If same line: one of the propositions is wrong; narrow the incorrect one.""")

agent("A", "A08_cobar_construction", """TARGET: chapters/theory/cobar_construction.tex

FINDING: Lines ~1347-1348 and ~2207-2219: Verdier convention must be consistent with
Theorem A after the chiral_koszul_pairs.tex rectification. The Verdier identification
should be at the ALGEBRA level (post-D_Ran), not coalgebra.

FIX: Read the current statement of thm:verdier-bar-cobar. Verify it says
D_Ran(bar B(A)) = (A)^!_inf as factorization algebra. If it says coalgebra, fix it.""")

agent("A", "A09_coderived_models", """TARGET: chapters/theory/coderived_models.tex

FINDINGS:
1. Lines ~247-270: prop:coderived-adequacy(a) invokes thm:higher-genus-inversion,
   creating circular dependency (same issue as Theorem B).
   FIX: Reprove coderived-adequacy independently using the coderived characterization
   (Verdier quotient by coacyclic objects), not by importing thm:higher-genus-inversion.

2. Lines ~75, ~545: Verify the coderived category definition is consistent with how
   bv_brst.tex now uses it (after the MC5 rectification).

Read the relevant sections only.""")

agent("A", "A10_configuration_spaces", """TARGET: chapters/theory/configuration_spaces.tex

FINDING: Lines ~1251, ~1278: Log FM definition for fixed pair (X,D).
The D^2=0 proof in higher_genus_modular_koszul.tex:30863 claims curve-degeneration
strata, but log FM for a fixed curve only has FM collisions and puncture collisions.

FIX: Add a remark clarifying which strata exist in each space:
- Log FM for fixed (X,D): FM collisions + puncture collisions only
- Universal family over M-bar_{g,n}: additionally has curve degenerations
The D^2=0 proof needs the universal family, not fixed-curve log FM.""")

# Remaining 10 agents: highest-priority structural fixes from audit findings

agent("A", "A11_fix_broken_refs_v1_theory", """TARGET: chapters/theory/ (all files)

The audit found 159 CRITICAL+HIGH broken references in Vol I. Focus on theory/ chapters.

Run: grep -rn '\\\\ref{' chapters/theory/ | head -100
For each ref, check if the corresponding label exists:
  grep -rn 'label{LABELNAME}' chapters/

Fix broken refs by either: (a) correcting the label name, (b) adding the missing label,
or (c) removing the dangling reference if the target was deleted.

Focus on the FIRST 30 broken refs you find. Fix each one.""")

agent("A", "A12_fix_broken_refs_v1_rest", """TARGET: chapters/examples/ chapters/connections/ appendices/ (all files)

Fix broken references in example, connection, and appendix chapters.

Run: grep -rn '\\\\ref{' chapters/examples/ chapters/connections/ appendices/ | head -100
For each ref, check the label exists. Fix the first 30 broken refs.""")

agent("A", "A13_fix_hardcoded_parts_v1", """TARGET: chapters/ (all files in Vol I)

The audit found 52 hardcoded Part references (Part~I, Part~II, etc.) that should use \\ref{part:...}.

Run: grep -rn 'Part~[IVXL]' chapters/ | head -60
For each: replace Part~IV with Part~\\ref{part:LABEL} using the correct label.
You may need to check main.tex for the part labels.
Fix ALL instances you find.""")

agent("A", "A14_fix_hardcoded_parts_v2", """TARGET: chapters/ (all files in Vol II)

Fix hardcoded Part references in Vol II.
Run: grep -rn 'Part~[IVXL]' chapters/ | head -60
Replace with \\ref{part:...}. Check main.tex for part labels.""", cwd=VOL2)

agent("A", "A15_fix_duplicate_labels_v1", """TARGET: chapters/ (Vol I)

The audit found 49 duplicate labels across volumes. Find and fix Vol I duplicates.

Run: grep -roh '\\\\label{[^}]*}' chapters/ | sort | uniq -d | head -30
For each duplicate: rename with unique suffix and update all \\ref{} to match.
Prefer adding a v1- prefix to the Vol I copy if the same label exists in Vol II/III.""")

agent("A", "A16_fix_status_mismatch_v1", """TARGET: chapters/theory/ (Vol I)

The audit found 101 ClaimStatus/environment mismatches. Fix theory chapter mismatches.

Find: \\ClaimStatusConjectured inside \\begin{theorem} or \\begin{proposition} environments.
FIX: Change the environment to \\begin{conjecture} and rename the label prefix (thm: -> conj:).

Also find: \\ClaimStatusProvedHere inside \\begin{conjecture} environments.
FIX: Change to \\begin{theorem} and rename label prefix (conj: -> thm:).

Run: grep -B3 'ClaimStatusConjectured' chapters/theory/ | grep 'begin{theorem}' | head -20
Fix the first 20 mismatches you find.""")

agent("A", "A17_fix_status_mismatch_v2", """TARGET: chapters/ (Vol II)

Fix ClaimStatus/environment mismatches in Vol II.
Same pattern: Conjectured in theorem env -> change to conjecture env.
ProvedHere in conjecture env -> change to theorem env.
Fix all you find.""", cwd=VOL2)

agent("A", "A18_fix_proof_after_conj_v1", """TARGET: chapters/ (Vol I)

The audit found 70 proof-after-conjecture violations (AP4).

Find: \\begin{proof} that follows \\begin{conjecture} or \\begin{heuristic}.
FIX: Change \\begin{proof} to \\begin{remark}[Evidence] ... \\end{remark}.

Run: grep -B15 'begin{proof}' chapters/theory/ | grep -B1 'begin{conjecture}' | head -30
Fix the first 20 violations.""")

agent("A", "A19_fix_proof_after_conj_v2", """TARGET: chapters/ (Vol II)

Same AP4 fix for Vol II: proof-after-conjecture -> remark[Evidence].
Find and fix all violations.""", cwd=VOL2)

agent("A", "A20_fix_broken_refs_v2", """TARGET: chapters/ (Vol II)

Fix 84 broken references in Vol II.
Run: grep -rn '\\\\ref{' chapters/ | head -100
Check each ref resolves. Fix the first 30.""", cwd=VOL2)


# ═══════════════════════════════════════════════════════════════════
# WAVE B: Status/label/reference integrity (20)
# ═══════════════════════════════════════════════════════════════════

agent("B", "B01_fix_duplicate_labels_xvol", """Find ALL duplicate labels across all three volumes.
Run: (grep -roh '\\\\label{[^}]*}' ~/chiral-bar-cobar/chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null) | sort | uniq -d
For each duplicate: determine which volume should keep it, rename the others with v1-/v2-/v3- prefix,
and update all \\ref{} in the renamed volume. Fix the first 20 duplicates.""")

agent("B", "B02_status_audit_theory_1", """Fix ClaimStatus mismatches in: chapters/theory/bar_construction.tex, chapters/theory/cobar_construction.tex, chapters/theory/bar_cobar_adjunction_inversion.tex, chapters/theory/bar_cobar_adjunction_curved.tex.
For each file: verify every \\ClaimStatus tag matches its environment. Fix mismatches.""")

agent("B", "B03_status_audit_theory_2", """Fix ClaimStatus mismatches in: chapters/theory/chiral_koszul_pairs.tex, chapters/theory/higher_genus_foundations.tex, chapters/theory/higher_genus_complementarity.tex.
Verify every tag matches its environment. Fix mismatches.""")

agent("B", "B04_status_audit_theory_3", """Fix ClaimStatus mismatches in: chapters/theory/higher_genus_modular_koszul.tex, chapters/theory/en_koszul_duality.tex, chapters/theory/chiral_hochschild_koszul.tex.
Verify every tag matches its environment. Fix mismatches.""")

agent("B", "B05_status_audit_examples", """Fix ClaimStatus mismatches in ALL chapters/examples/*.tex files.
Verify every tag matches its environment. Conjectured claims in theorem envs -> conjecture envs.""")

agent("B", "B06_status_audit_connections", """Fix ClaimStatus mismatches in ALL chapters/connections/*.tex files.
Especially bv_brst.tex (MC5 status), concordance.tex (all statuses).""")

agent("B", "B07_missing_status_tags", """Find theorem/proposition/lemma environments WITHOUT any ClaimStatus tag.
Run: grep -A5 'begin{theorem}\\|begin{proposition}' chapters/theory/ | grep -L 'ClaimStatus'
For each untagged theorem: determine the correct status and add the tag.""")

agent("B", "B08_fix_broken_refs_v3", """Fix broken references in Vol III.
Run: grep -rn '\\\\ref{' chapters/ | head -80
Check each ref resolves. Fix all broken refs.""", cwd=VOL3)

agent("B", "B09_fix_hardcoded_parts_v3", """Fix hardcoded Part references in Vol III.
Run: grep -rn 'Part~[IVXL]\\|Chapter~[0-9]' chapters/ | head -30
Replace with \\ref{part:...}.""", cwd=VOL3)

agent("B", "B10_incomplete_proofs", """Find incomplete proofs in Vol I.
Search for: \\begin{proof} blocks that are <5 lines, or contain '...' or 'TO BE COMPLETED'.
Also find ProvedHere tags without a following proof block within 50 lines.
Run: grep -A50 'ClaimStatusProvedHere' chapters/theory/ | grep -B5 'end{theorem}\\|end{proposition}' | grep -v 'begin{proof}' | head -30
For each: either write the proof sketch or downgrade to Conjectured.""")

agent("B", "B11_orphaned_chapters", """Find chapter files NOT in the \\input graph.
Run: grep '\\\\input{' main.tex | sed 's/.*input{//' | sed 's/}.*//' > /tmp/inputted.txt
Then: ls chapters/theory/*.tex chapters/examples/*.tex chapters/connections/*.tex | while read f; do
  base=$(echo $f | sed 's/.tex//'); grep -q "$base" /tmp/inputted.txt || echo "ORPHANED: $f"
done
For each orphaned file: determine if it should be \\input'd or removed.""")

agent("B", "B12_undefined_citations", """Find undefined citations (\\cite{} without bibitem).
Run: grep -roh '\\\\cite{[^}]*}' chapters/ | sort -u | sed 's/\\\\cite{//' | sed 's/}//' > /tmp/cites.txt
Then: for c in $(cat /tmp/cites.txt); do grep -q "$c" bibliography.bib 2>/dev/null || echo "UNDEFINED: $c"; done | head -30
Fix by adding missing bibentries or correcting the cite key.""")

agent("B", "B13_empty_sections", """Find empty or near-empty sections in Vol I.
Run: grep -n 'section{' chapters/theory/ chapters/examples/ | while read line; do
  file=$(echo $line | cut -d: -f1); num=$(echo $line | cut -d: -f2)
  next=$(grep -n 'section{' "$file" | awk -F: -v n=$num '$1>n{print $1;exit}')
  if [ -n "$next" ]; then content=$((next-num)); [ $content -lt 5 ] && echo "EMPTY ($content lines): $line"; fi
done 2>/dev/null | head -20
For each empty section: add content or remove the section.""")

agent("B", "B14_stale_cross_vol_refs_v2", """Find stale cross-volume references in Vol II that point to Vol I.
Search for 'Volume~I' or 'Vol~I' or 'chiral-bar-cobar' in chapters/.
For each: verify the referenced theorem/formula is still accurate after the Vol I rectification.
Especially check: Theorem A, B, C, D, H status; topologization scope; MC5 status.""", cwd=VOL2)

agent("B", "B15_stale_cross_vol_refs_v3", """Find stale cross-volume references in Vol III that point to Vol I or Vol II.
Search for 'Volume~I', 'Volume~II', 'Vol~I', 'Vol~II' in chapters/.
Verify referenced theorems are accurate. Especially: CY-A scope (d=2 only), kappa subscripts.""", cwd=VOL3)

agent("B", "B16_concordance_full_sync", """TARGET: chapters/connections/concordance.tex
Read the FULL concordance. For each theorem listed:
1. Check the status matches the current .tex source
2. Check the scope matches (after all rectifications)
3. Flag any stale entries
This is the constitutional audit. Be exhaustive.""")

agent("B", "B17_metadata_sync", """TARGET: metadata/theorem_registry.md
Read the theorem registry. Cross-check against concordance.tex and the actual .tex files.
Flag any disagreements. Update the registry to match current state.""")

agent("B", "B18_readme_update_v1", """TARGET: README.md (Vol I)
Read the current README. Update:
1. Page count (check from last build)
2. Test count (run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ --co -q 2>&1 | tail -1)
3. Theorem status summary (from concordance)
4. Ensure no claims exceed what's proved
Do NOT inflate scope.""")

agent("B", "B19_readme_update_v2", """TARGET: README.md (Vol II)
Same: update page count, test count, theorem status. No scope inflation.""", cwd=VOL2)

agent("B", "B20_readme_update_v3", """TARGET: README.md (Vol III)
Same: update page count, test count, theorem status. No scope inflation.""", cwd=VOL3)


# ═══════════════════════════════════════════════════════════════════
# WAVE C: Formula and convention fixes (20)
# ═══════════════════════════════════════════════════════════════════

agent("C", "C01_bare_omega_v1", """Fix ALL bare \\Omega/z without level prefix in Vol I (AP126).
Run: grep -rn '\\\\Omega' chapters/ | grep -v 'k.*\\\\Omega\\|level\\|AP126' | head -40
For each: add the level prefix k. r(z) = k*\\Omega/z, NOT \\Omega/z.""", preamble=AUDIT_PREAMBLE)

agent("C", "C02_bare_omega_v2", """Same AP126 fix for Vol II.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("C", "C03_bare_omega_v3", """Same AP126 fix for Vol III.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)

agent("C", "C04_arnold_kz_fix", """Fix Arnold form vs KZ connection confusion (AP117).
Search ALL volumes for 'd\\\\log' near 'connection' or 'KZ' or '\\\\nabla'.
Connection is r(z)dz, NOT r(z) d log(z). Arnold d log(z_i-z_j) is bar coefficient only.
Fix each instance.""", preamble=AUDIT_PREAMBLE)

agent("C", "C05_cauchy_normalization", """Fix Cauchy integral normalization (AP120).
Search ALL volumes for '\\\\oint' or '\\\\frac{1}{2\\\\pi}'.
Must be 1/(2*pi*i), NOT 1/(2*pi). Fix each instance.""", preamble=AUDIT_PREAMBLE)

agent("C", "C06_averaging_sugawara", """Fix averaging identity Sugawara shift (C13/FM11).
Search for 'av(r' or 'averaging' in ALL volumes.
For non-abelian KM: av(r(z)) + dim(g)/2 = kappa, NOT av(r(z)) = kappa.
Fix each instance.""", preamble=AUDIT_PREAMBLE)

agent("C", "C07_e3_chiral_ban", """Fix 'E_3-chiral' -> 'E_3-topological' (AP168/B58).
Search ALL volumes for 'E_3.*chiral\\|E_{3}.*chiral\\|E_3-chiral'.
Must be E_3-TOPOLOGICAL when referring to the topologized derived center.
Fix each instance.""", preamble=AUDIT_PREAMBLE)

agent("C", "C08_sc_self_dual_fix", """Fix any remaining SC Koszul self-duality claims (AP166/B57).
Search ALL volumes for 'self-dual' near 'SC\\|Swiss-cheese'.
SC is NOT self-dual: SC^! = (Lie, Ass, shuffle). Fix each instance.""", preamble=AUDIT_PREAMBLE)

agent("C", "C09_sc_bar_coalgebra_fix", """Fix any remaining 'B(A) is SC coalgebra' claims (AP165/B54).
Search ALL volumes for 'bar.*SC\\|B(A).*SC\\|coalgebra.*SC'.
B(A) is E_1 coalgebra. SC lives on (C^bullet_ch(A,A), A). Fix each.""", preamble=AUDIT_PREAMBLE)

agent("C", "C10_rmatrix_xvol_consistency", """Cross-volume r-matrix convention consistency.
For each family (KM, Heis, Vir): grep all three volumes for r-matrix formulas.
Verify: (a) level prefix present, (b) same convention (trace-form or KZ) within each file,
(c) bridge identity stated when conventions switch. Fix inconsistencies.""", preamble=AUDIT_PREAMBLE)

agent("C", "C11_kappa_xvol_consistency", """Cross-volume kappa formula consistency.
For each family: grep all three volumes for kappa formulas.
Verify each matches the canonical census. Especially check:
kappa(KM) includes Sugawara shift, kappa(W_N) uses H_N-1 not H_{N-1},
Vol III has subscripts (AP113). Fix inconsistencies.""", preamble=AUDIT_PREAMBLE)

agent("C", "C12_desuspension_fix", """Fix desuspension direction errors (AP22/B15-B16).
Search ALL volumes for 's\\^{-1}' and '|s\\^{-1}'.
Must be |s^{-1}v| = |v| - 1 (LOWERS). Fix any +1 instances.
Also check for bare 's' (not s^{-1}) in bar complex formulas.""", preamble=AUDIT_PREAMBLE)

agent("C", "C13_augmentation_fix", """Fix augmentation ideal omissions (AP132/B14).
Search ALL volumes for 'T\\^c' and 'B(A)'.
Must use A-bar = ker(epsilon), NOT bare A. Fix T^c(s^{-1} A) -> T^c(s^{-1} A-bar).""", preamble=AUDIT_PREAMBLE)

agent("C", "C14_curved_vs_flat_fix", """Fix curved-vs-flat confusion (D08 findings).
Search Vol I theory chapters for 'd\\^2' and 'spectral sequence' and 'cohomology'.
Where ordinary cohomology is applied to curved complexes (d^2=kappa*omega_g), add
explicit flat-side comparison or coderived qualifier. Fix each instance.""", preamble=AUDIT_PREAMBLE)

agent("C", "C15_five_objects_fix", """Fix five-object conflation (D09 findings).
Search Vol I for paragraphs mentioning both 'bar' and 'Koszul dual' or 'derived center'.
Verify all five objects (A, B(A), A^i, A^!, Z^der) correctly distinguished.
Fix any conflation language.""", preamble=AUDIT_PREAMBLE)

agent("C", "C16_lambda_bracket_v2", """Fix lambda-bracket divided-power convention in Vol II (V2-AP34).
Search for lambda-bracket formulas. Must use divided powers: c/12 (not c/2) for Virasoro.
{T_lambda T} = (c/12)*lambda^3. Fix any incorrect conventions.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("C", "C17_bare_kappa_v3", """Fix ALL remaining bare kappa in Vol III (AP113).
Run: grep -rn '\\\\kappa[^_{}]\\|\\\\kappa$' chapters/ | head -50
Must be kappa_ch, kappa_cat, kappa_BKM, or kappa_fiber. Fix each.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)

agent("C", "C18_eta_prefactor", """Fix missing eta prefactor q^{1/24} (B17).
Search ALL volumes for 'eta' and 'prod.*1-q'.
eta(tau) = q^{1/24} * prod(1-q^n). Fix any missing prefactors.""", preamble=AUDIT_PREAMBLE)

agent("C", "C19_bc_bg_swap_check", """Comprehensive bc/bg central charge audit across ALL volumes (AP137).
For every occurrence of c_bc or c_betagamma: verify the formula is correct.
c_bc(lambda) = 1 - 3(2lambda-1)^2 (fermionic).
c_bg(lambda) = 2(6lambda^2-6lambda+1) (bosonic).
c_bc + c_bg = 0. Fix any swaps.""", preamble=AUDIT_PREAMBLE)

agent("C", "C20_WN_harmonic_fix", """Fix W_N harmonic number issues (AP136/B7).
Search ALL volumes for 'H_{N-1}' and 'kappa.*W_N'.
kappa(W_N) = c*(H_N - 1), NOT c*H_{N-1}. H_{N-1} != H_N - 1.
At N=2: H_1=1, H_2-1=1/2. Fix each instance.""", preamble=AUDIT_PREAMBLE)


# ═══════════════════════════════════════════════════════════════════
# WAVE D: Prose discipline (20)
# ═══════════════════════════════════════════════════════════════════

agent("D", "D01_slop_v1_theory", """Remove AI slop vocabulary from chapters/theory/*.tex.
Banned: moreover, additionally, notably, crucially, remarkably, interestingly, furthermore,
delve, leverage, tapestry, cornerstone, "it is worth noting", "worth mentioning".
grep -rni these words in chapters/theory/. Rewrite each without the slop word.""", preamble=AUDIT_PREAMBLE)

agent("D", "D02_slop_v1_examples", """Same slop removal for chapters/examples/*.tex.""", preamble=AUDIT_PREAMBLE)

agent("D", "D03_slop_v1_connections", """Same slop removal for chapters/connections/*.tex.""", preamble=AUDIT_PREAMBLE)

agent("D", "D04_slop_v2", """Same slop removal for ALL Vol II chapters/.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("D", "D05_slop_v3", """Same slop removal for ALL Vol III chapters/.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)

agent("D", "D06_em_dash_v1", """Remove ALL em dashes from Vol I chapters/.
grep -rn '---\\|—' chapters/. Replace with colon, semicolon, or separate sentence.""", preamble=AUDIT_PREAMBLE)

agent("D", "D07_em_dash_v2", """Same em dash removal for Vol II.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("D", "D08_em_dash_v3", """Same em dash removal for Vol III.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)

agent("D", "D09_markdown_in_latex", """Fix markdown in LaTeX across ALL volumes (AP121/B40).
Search for: backtick numerals (`29`), **bold**, _italic_ in .tex files.
Replace with $29$, \\textbf{}, \\emph{}.""", preamble=AUDIT_PREAMBLE)

agent("D", "D10_arity_ban_v1", """Remove ALL remaining 'arity' from Vol I (AP176).
grep -rni '\\barity\\b' chapters/ appendices/ standalone/
Must return ZERO hits. Replace with 'degree'. Fix article: 'an degree' -> 'a degree'.""", preamble=AUDIT_PREAMBLE)

agent("D", "D11_arity_ban_v2", """Same for Vol II.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("D", "D12_arity_ban_v3", """Same for Vol III.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)

agent("D", "D13_uniform_weight_tags", """Fix missing uniform-weight tags on obs_g/F_g formulas (AP32/D13).
Search Vol I for 'obs_g\\|F_g\\|lambda_g' in theorem environments.
Each must carry: (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta F_g^cross).
Add the tag to each untagged formula.""", preamble=AUDIT_PREAMBLE)

agent("D", "D14_hochschild_disambiguation", """Fix bare 'Hochschild' without qualifier (D12).
Search ALL volumes for 'Hochschild' not preceded by 'chiral' or 'topological' or 'categorical'.
In mathematical contexts: must specify WHICH Hochschild theory.
Add 'chiral' qualifier where the chiral Hochschild complex is meant.""", preamble=AUDIT_PREAMBLE)

agent("D", "D15_e1_einf_v2", """Fix E_1/E_inf terminology violations in Vol II (V2-AP1-AP24).
Search for 'E_inf' near 'no poles' or 'not E_inf' near 'vertex algebra'.
All VAs are E_inf. OPE poles don't break E_inf. Fix violations.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("D", "D16_chapter_openings_v1", """Audit chapter openings in Vol I theory chapters.
For each chapter: does it open with the PROBLEM (deficiency opening)?
Or with 'In this chapter we...' (AP106)?
Rewrite the first 3-5 lines of any chapter that opens with a signpost instead of a problem.""", preamble=AUDIT_PREAMBLE)

agent("D", "D17_chapter_openings_v2", """Same for Vol II.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("D", "D18_todos_v1", """Find and resolve ALL TODO/FIXME/HACK/RECTIFICATION-FLAG markers in Vol I.
grep -rn 'TODO\\|FIXME\\|HACK\\|RECTIFICATION-FLAG\\|XXX' chapters/ | head -40
For each: either resolve the TODO or convert to an explicit remark.""", preamble=AUDIT_PREAMBLE)

agent("D", "D19_todos_v2", """Same for Vol II.""", cwd=VOL2, preamble=AUDIT_PREAMBLE)

agent("D", "D20_todos_v3", """Same for Vol III.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)


# ═══════════════════════════════════════════════════════════════════
# WAVE E: Missing content and test gaps (20)
# ═══════════════════════════════════════════════════════════════════

agent("E", "E01_test_gaps_shadow", """Find and create missing test files for shadow tower engines.
ls compute/lib/*shadow*.py | while read f; do test=compute/tests/test_$(basename $f); [ ! -f "$test" ] && echo "MISSING: $test"; done
For each missing test: create a basic test file that imports the engine and runs at least
3 smoke tests with verified expected values.""", preamble=AUDIT_PREAMBLE)

agent("E", "E02_test_gaps_koszul", """Same for koszul/complementarity engines.""", preamble=AUDIT_PREAMBLE)

agent("E", "E03_test_gaps_central", """Same for central_charge/ghost engines.""", preamble=AUDIT_PREAMBLE)

agent("E", "E04_test_gaps_rmatrix", """Same for r_matrix engines.""", preamble=AUDIT_PREAMBLE)

agent("E", "E05_test_gaps_misc", """Find ALL engines without tests in Vol I.
ls compute/lib/*.py | while read f; do base=$(basename $f .py); [ ! -f "compute/tests/test_${base}.py" ] && echo $f; done
Create basic test files for the first 10 untested engines.""", preamble=AUDIT_PREAMBLE)

agent("E", "E06_test_gaps_v3", """Find and create missing test files in Vol III.
Same pattern: check compute/lib/ vs compute/tests/.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)

agent("E", "E07_test_verification", """Verify hardcoded expected values in Vol I tests (AP10/AP128).
Read compute/tests/test_shadow*.py and check: does each expected value have a '# VERIFIED'
comment citing 2+ independent sources? Add missing verification comments.""", preamble=AUDIT_PREAMBLE)

agent("E", "E08_stub_chapters_v1", """Find stub chapters (<100 lines or no theorems) in Vol I.
For each: either develop into substantive content or comment out from main.tex.""", preamble=AUDIT_PREAMBLE)

agent("E", "E09_stub_chapters_v3", """Same for Vol III.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)

agent("E", "E10_missing_examples_thms", """For Theorems A-D, H: find worked examples.
Search chapters/examples/ for explicit verification of each theorem for a specific family.
If a theorem lacks a worked example: write one for Heisenberg (simplest).""", preamble=AUDIT_PREAMBLE)

agent("E", "E11_missing_genus2", """Search for genus-2 content.
Is there explicit genus-2 computation? 7 stable graphs enumerated? Period matrix 2x2?
If missing: add a remark in higher_genus_foundations.tex or higher_genus_modular_koszul.tex.""", preamble=AUDIT_PREAMBLE)

agent("E", "E12_missing_SC_presentation", """Search for SC^{ch,top} generators-and-relations.
Is the operadic presentation explicit? With generators (codim-1 boundary strata) and
relations (codim-2)? If missing: add at least a remark listing the generators.""", preamble=AUDIT_PREAMBLE)

agent("E", "E13_dead_labels_v1", """Find labels that are never referenced.
grep -roh '\\\\label{[^}]*}' chapters/ | sort > /tmp/labels.txt
grep -roh '\\\\ref{[^}]*}' chapters/ | sort > /tmp/refs.txt
comm -23 /tmp/labels.txt /tmp/refs.txt > /tmp/dead.txt
Report the dead labels. Do NOT delete them (they may be referenced from other volumes).""", preamble=AUDIT_PREAMBLE)

agent("E", "E14_forward_refs_v1", """Find forward references that don't resolve.
For each \\ref{X}: is \\label{X} defined BEFORE or AFTER in the input order?
If after: flag as forward reference. If never: flag as broken.
Focus on chapters/theory/.""", preamble=AUDIT_PREAMBLE)

agent("E", "E15_build_warnings", """Read main.log for LaTeX warnings.
grep -i 'warning\\|undefined\\|multiply' main.log | grep -v 'rerunfilecheck' | head -40
For each warning: diagnose the cause and suggest the fix.""", preamble=AUDIT_PREAMBLE)

agent("E", "E16_compute_manuscript_sync", """Verify computed values match manuscript claims.
Pick 10 key formulas from landscape_census.tex. For each:
1. Read the census value
2. Find the formula in the manuscript
3. Find the compute engine
4. Run the test
Report any disagreements.""", preamble=AUDIT_PREAMBLE)

agent("E", "E17_missing_definitions", """Find objects used before definition in Vol I theory chapters.
Read chapters/theory/bar_construction.tex, cobar_construction.tex, chiral_koszul_pairs.tex.
For each \\ macro or symbol: is it defined before first use? Flag define-before-use violations.""", preamble=AUDIT_PREAMBLE)

agent("E", "E18_hidden_imports", """Find hidden imports in Vol I theory chapters.
Search for 'by Theorem', 'by Proposition', 'by Lemma', 'follows from'.
For each: does the cited result exist and prove what's needed?
Focus on higher_genus_modular_koszul.tex (the largest file).""", preamble=AUDIT_PREAMBLE)

agent("E", "E19_notation_index", """Create a notation index for Vol I.
Scan main.tex and chapters/theory/ for key macros: \\kappa, \\Theta, B(A), A^!, Z^{der}, r(z), etc.
Produce a list of: symbol, meaning, first defined at file:line.
Write to standalone/notation_index.tex.""", preamble=AUDIT_PREAMBLE)

agent("E", "E20_theorem_index", """Create a theorem index for Vol I.
Scan all chapters for \\begin{theorem}, \\begin{proposition}, \\begin{conjecture}.
For each: label, name, status, file:line.
Write to standalone/theorem_index.tex.""", preamble=AUDIT_PREAMBLE)


# ═══════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Fix Campaign — 100 agents, 5 waves")
    parser.add_argument("--wave", required=True, choices=["A", "B", "C", "D", "E"],
                        help="Which wave to launch")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1500)
    parser.add_argument("--delay", type=int, default=30, help="Seconds between batches")
    args = parser.parse_args()

    global OUT
    OUT = Path(VOL1) / f"fix_wave_{args.wave}_{TS}"
    OUT.mkdir(parents=True, exist_ok=True)

    agents = AGENTS[args.wave]
    print(f"Wave {args.wave}: {len(agents)} agents → {OUT}")
    print(f"Batch: {args.batch_size}, Timeout: {args.timeout}s, Delay: {args.delay}s\n")

    ok, fail = 0, 0
    results = []
    for i in range(0, len(agents), args.batch_size):
        batch = agents[i:i + args.batch_size]
        bn = i // args.batch_size + 1
        tb = (len(agents) + args.batch_size - 1) // args.batch_size
        print(f"=== Batch {bn}/{tb} ({len(batch)} agents) ===")
        with ThreadPoolExecutor(max_workers=args.batch_size) as ex:
            futs = {ex.submit(run_agent, a, args.timeout): a for a in batch}
            for f in as_completed(futs):
                aid, success, dt = f.result()
                ok += success; fail += (not success)
                results.append({"id": aid, "ok": success, "time": dt})
                print(f"  [{ok+fail}/{len(agents)}] {'OK' if success else 'FAIL'} {aid} ({dt:.0f}s)")
        if i + args.batch_size < len(agents):
            print(f"  (cooldown {args.delay}s)")
            time.sleep(args.delay)

    summary = [f"# Wave {args.wave} Summary — {TS}\n",
               f"Total: {len(agents)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
