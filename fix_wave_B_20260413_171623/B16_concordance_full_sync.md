# B16_concordance_full_sync (1010s)

Audited the full concordance theorem/status surface in [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1) against live source and made only local fixes.

- `FIXED`: Theorem D’s constitutional summary now cites the live multi-weight correction theorem, so its scope split is anchored to source rather than implied prose alone. See [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:60).
- `FIXED`: Seven stale label/environment mismatches in the concordance prose were corrected: conjectures no longer called propositions/theorems, a proposition is no longer called a theorem, and a corollary is no longer called a theorem. Representative fixes are at [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1932), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:2508), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3076), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6481), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6854), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:8720).
- `FIXED`: The stale `% TODO(status-sync)` residue left from an earlier rectification pass was removed from the family-index routing proof. See [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6121).
- `FIXED`: Two genuinely stale broken refs were removed from the live constitutional surface and replaced with plain-text cross-volume descriptions: the dead `thm:recognition` ref and the dead `conj:yangian-ordered-center` ref. See [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4726) and [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7262).
- `FIXED`: Comment-only triple-hyphen separator lines were normalized so the post-edit forbidden-pattern grep is clean.

- `BLOCKED`: A broader mechanical ref-existence check still finds 25 unresolved non-theorem cross-volume/orphaned labels in the concordance, mostly section/remark/proposition refs like `sec:k3-chiral-algebra`, `prop:bar-hocolim`, `rem:four-kappas`. Resolving those cleanly needs a separate cross-volume retargeting pass or new phantom labels in `main.tex`; I did not widen this surgical edit into that larger rewrite.

Verification: the full label-type mismatch scan against live `.tex` environments is clean, and the targeted forbidden-pattern grep on `chapters/connections/concordance.tex` is clean. I did not run a TeX build.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8798-c749-74e1-928b-06bc3d0f357f
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: chapters/connections/concordance.tex
Read the FULL concordance. For each theorem listed:
1. Check the status matches the current .tex source
2. Check the scope matches (after all rectifications)
3. Flag any stale entries
This is the constitutional audit. Be exhaustive.
mcp startup: no servers



thinking
**Planning coding tasks**

I'm thinking about acting as a coding agent now. I need to comply with the AGENTS guidelines and might use the skills claim-surface-sync and deep-beilinson-audit. My task involves auditing the concordance against current sources and editing only the concordance file. I need to read through several specified files first to ensure I make informed mathematical edits. I should also consider using explorer agents for content searches instead of manual searches, but reading files directly may still be necessary. It seems I need to update my plan since this is a substantial task.
thinking
**Using tools for coding tasks**

I'm figuring out how to use commentary tools, and I think I might need to employ multi_tool_use.parallel for running various developer tool calls simultaneously. Since system tools aren’t usable in parallel, I’ll focus on executing shell commands with exec_command. I may also need to spawn an explorer agent to inspect theorem environments and status across files, especially since the instructions suggest relying on explorers for codebase questions. It seems like the best approach is to map concordance theorem entries to their corresponding source statuses.
thinking
**Considering tool usage**

I'm thinking about parallelizing the task, possibly by using one explorer for the concordance structure and another for theorem source statuses since it's an audit. However, I’m concerned that the instruction to trust explorer results without verification might contradict the AGENTS’ trust hierarchy. The guidelines suggest reading exact files before making edits, so I might ask the explorer for a list of theorem labels and their source files but do the manual reading myself afterward. Maybe it’s better not to use the explorer if this isn't strictly a codebase question.
codex
Using `claim-surface-sync` for this audit because the task is status/scope drift on the constitutional concordance. I’m starting by reading the required repo-wide context files, then I’ll audit every concordance theorem entry against its live source before making any scoped edits to `chapters/connections/concordance.tex`.
exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{Concordance with primary literature}
\label{chap:concordance}

\index{concordance|textbf}

This chapter is the constitution of the monograph. When chapters
disagree, this chapter governs. It records the five main theorems
with their precise status and locates every result against the
prior literature: what is proved, what is conditional, what
remains conjectural.

The governing principle is falsification: every claim in these three
volumes is presumed false until it appears below with an explicit
status tag and a proof reference or independent verification trail.
A theorem that contradicts the concordance is not a theorem; it is an
error in the chapter that states it. Omission from this chapter is
itself a verdict: what is not recorded here has not survived scrutiny.
The concordance does not summarize the monograph; the monograph
approximates the concordance.

 succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
 succeeded in 51ms:
# Red-Team Summary of Vol1/Vol2 Claim Audit
## Scope
- Formal tagged claims catalogued: **4866**
- Volume I formal claims: **2841**
- Volume II formal claims: **2025**
- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.

## Status profile
- ProvedHere: **3801**
- Conjectured: **327**
- Heuristic: **35**
- ProvedElsewhere: **513**
- Conditional: **116**
- Open: **74**

## Risk profile
- medium: **1999**
- low: **1913**
- high: **807**


thinking
**Auditing theorems thoroughly**

I’m working through the initial chunks, but it looks like I need FULL concordance to ensure everything matches up. I should probably read the entire concordance file and audit each theorem listed. I'll check if the status aligns with the current .tex source and flag any stale entries. This task really calls for an exhaustive approach to check every theorem, including literature items, against the current sources in the concordance chapter.
thinking
**Updating theorem references**

I need to parse all theorem references in the concordance and compare them to the target file. There could be many dozens of entries, so I should read the full concordance and make minimal, truthful edits to any stale entries. I’ll need a solid plan for the update and might use shell commands to extract references and status macros. It sounds feasible to use scripts for inspecting the source status for each relevant theorem. I'll also review the SKILL.md file to help guide me through this process. Let's start with the commentary update!
codex
The required constitutional files are loaded. Next I’m reading the rest of `chapters/connections/concordance.tex`, extracting every theorem/definition/proposition reference it asserts about, and then matching each one against the live source status and scope before I touch the concordance text.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '261,520p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
 succeeded in 52ms:
\textbf{Shadow depth classifies complexity within the Koszul world.}\enspace
Within the chirally Koszul standard examples treated in
Part~\ref{part:physics-bridges} (Heisenberg, affine Kac--Moody,
$bc$-$\beta\gamma$, Virasoro, universal principal $\Walg_N$),
shadow depth $r_{\max}$ and the four-class partition
G/L/C/M measure $L_\infty$ non-formality, not
Koszulness status:
class~G (formal, $r_{\max} = 2$),
class~L (single Massey product, $r_{\max} = 3$),
class~C (quartic then rigid by stratum separation, $r_{\max} = 4$),
class~M (intrinsically non-formal, $r_{\max} = \infty$).

\section{Principal contributions}\label{sec:principal-contributions}

\begin{enumerate}[label=\emph{(\arabic*)}]

\item \emph{Configuration space bar-cobar adjunction
 (Theorems~\ref{thm:bar-cobar-isomorphism-main}
 and~\ref{thm:higher-genus-inversion}).}
 Bar and cobar are realized via explicit integrals over

thinking
**Determining file length**

I need to check how long the concordance file is since I’ve read up to around 520. I think I should figure out if there’s more to read until the end. It’s important to have a clear idea of the total length, so I can manage my time and effort effectively. Let’s see how far we can go and if it’s worth continuing.
codex
I’ve got the theorem table and principal-contribution assertions. I’m now extracting the full `\ref` surface from the concordance chapter so I can check every cited claim, not just the five headline rows.
exec
/bin/zsh -lc 'wc -l chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -no '\\\\(?:ref|eqref)\\{["'^}]+'"\\}' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   11462 chapters/connections/concordance.tex
 succeeded in 52ms:
Total output lines: 1395

37:\ref{thm:bar-cobar-isomorphism-main}
42:\ref{thm:higher-genus-inversion}
43:\ref{thm:bar-cobar-inversion-qi}
50:\ref{thm:fiber-center-identification}
54:\ref{thm:quantum-complementarity-main}
57:\ref{thm:shifted-symplectic-complementarity}
62:\ref{def:scalar-lane}
63:\ref{thm:modular-characteristic}
77:\ref{thm:main-koszul-hoch}
78:\ref{thm:hochschild-polynomial-growth}
79:\ref{prop:chirhoch1-affine-km}
85:\ref{thm:modular-koszul-duality-main}
93:\ref{def:modular-convolution-dg-lie}
96:\ref{thm:modular-homotopy-convolution}
98:\ref{thm:mc2-bar-intrinsic}
104:\ref{thm:e1-mc-element}
158:\eqref{eq:bbj-comparison}
159:\ref{chap:e1-modular-koszul}




thinking
**Planning the audit report**

I need to check that the scope matches after making corrections and flag any stale entries. Since we're dealing with a lot of references—over 1000—it’s a big task, but I can script it. I want to produce an audit report while making minimal edits to the concordance. It’s essential to identify any mismatches in the live source and correct statuses or scopes of stale entries. The goal is to ensure that all theorem entries are accurate.
thinking
**Clarifying the audit task**

The user wants me to read the audit findings and the source, then make the minimum truthful edits needed to resolve each finding without pasting the findings themselves. Instead, I need to focus on auditing the concordance, identifying stale entries, and ensuring a final report is fixed for each entry. I must follow AGENTS’ verification for any changes in status or scope. I’m considering whether I'll need to add labels but think I might avoid doing that.
thinking
**Evaluating metadata generation options**

I might need to use existing scripts in the repository to generate metadata or check labels. Searching for relevant scripts could help, especially for label status conflicts. While I could write a small custom script, there's a point about avoiding Python for reading/writing files when a shell command would suffice. However, for auditing, Python or awk could still be justified. It’s complicated, but consulting an explorer agent might help clarify theorem labels and identify any stale entries or mismatches. The final answer needs to be solid.
thinking
**Planning a concordance audit**

I might start by using the explorer for an initial survey. The goal is to audit the concordance file, focusing on modifying entries with stale statuses or scopes based on actual theorem sources. I can automate the collection of theorem labels in the concordance. For each label, I should identify the labeled environment and its nearest ClaimStatus. Generating a CSV with this information could be useful. Additionally, I could cross-check for phrases in concordance that indicate status mismatches while keeping context-specific semantics in mind. I’ll look for existing detailed metadata to assist.
codex
The concordance surface is much larger than the five-row table. I’m switching to an automated pass over every `\ref{...}` in this chapter so I can catch status drift systematically, then I’ll manually inspect the entries whose prose makes scope or status claims.
exec
/bin/zsh -lc 'ls metadata' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label_status_conflicts|suspicious_proved_claim_dependencies|claim\" metadata scripts -g '"'!**/__pycache__/**'"'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
census.json
claims.jsonl
dependency_graph.dot
label_index.json
theorem_registry.md
verified_formulas.jsonl
 succeeded in 52ms:
metadata/theorem_registry.md:3:Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.
metadata/theorem_registry.md:11:| ProvedHere claims | 2845 |
metadata/theorem_registry.md:12:| Total tagged claims | 3673 |
metadata/theorem_registry.md:53:| File | ProvedHere claims |
scripts/generate_theorem_dependency_index.py:168:    out.append(f"Total indexed claim nodes: {len(rows)}")
metadata/census.json:10:    "total_claims": 3673
scripts/generate_metadata.py:6:  metadata/claims.jsonl         — One JSON line per tagged claim
scripts/generate_metadata.py:10:  metadata/theorem_registry.md  — Auto-synchronized proved-claim registry
scripts/generate_metadata.py:90:    """A single tagged mathematical claim."""
scripts/generate_metadata.py:191:def extract_claims(path: Path) -> list[Claim]:
scripts/generate_metadata.py:192:    """Extract all tagged claims from a single .tex file."""
scripts/generate_metadata.py:196:    claims: list[Claim] = []
scripts/generate_metadata.py:268:        claim = Claim(
scripts/generate_metadata.py:279:        claims.append(claim)
scripts/generate_metadata.py:283:    return claims
scripts/generate_metadata.py:341:def write_claims_jsonl(claims: list[Claim]) -> None:
scripts/generate_metadata.py:342:    """Write metadata/claims.jsonl — one JSON line per claim."""
scripts/generate_metadata.py:343:    out_path = METADATA_DIR / "claims.jsonl"
scripts/generate_metadata.py:345:        for claim in claims:
scripts/generate_metadata.py:346:            f.write(json.dumps(claim.to_dict(), ensure_ascii=False) + "\n")

thinking
**Exploring claims and metadata**

I think I need to look into using metadata or a claims file to query labels. It seems like only tagged claims reveal their status, so I’ll want to audit references to those labeled claims. I’ll also check to ensure the status matches what I find in the .tex file. It feels like the claims.jsonl could provide sufficient information, so I'll inspect its format to see if it fits my needs.
exec
/bin/zsh -lc "python - <<'PY'
import json
with open('metadata/label_index.json') as f:
    data=json.load(f)
for k in list(data)[:5]:
    print(k, data[k])
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python - <<'PY'
import json
from itertools import islice
with open('metadata/claims.jsonl') as f:
    for line in islice(f,5):
        obj=json.loads(line)
        print(obj)
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
 exited 127 in 50ms:
zsh:1: command not found: python
codex
I found the repo metadata surface that can answer status questions directly. I’m using that for the broad pass, and I’ll fall back to source reads only where the concordance prose asserts more than the metadata can guarantee.
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from itertools import islice
with open('metadata/claims.jsonl') as f:
    for line in islice(f,5):
        obj=json.loads(line)
        print(obj)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import json
with open('metadata/label_index.json') as f:
    data=json.load(f)
for k in list(data)[:5]:
    print(k, data[k])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
{'label': 'thm:shadow-spectral-correspondence', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/connections/arithmetic_shadows.tex', 'line': 197, 'title': 'Shadow--spectral correspondence', 'labels_in_block': ['thm:shadow-spectral-correspondence', 'eq:epstein-factorization']}
{'label': 'prop:divisor-sum-decomposition', 'env_type': 'proposition', 'status': 'ProvedHere', 'file': 'chapters/connections/arithmetic_shadows.tex', 'line': 311, 'title': 'Divisor-sum decomposition', 'labels_in_block': ['prop:divisor-sum-decomposition', 'eq:log-det-sigma', 'eq:sigma-minus-1-dirichlet']}
{'label': 'cor:sewing-euler-product', 'env_type': 'corollary', 'status': 'ProvedHere', 'file': 'chapters/connections/arithmetic_shadows.tex', 'line': 336, 'title': 'Euler product of the sewing determinant', 'refs_in_block': ['eq:sigma-minus-1-dirichlet']}
{'label': 'prop:sewing-trace-formula', 'env_type': 'proposition', 'status': 'ProvedHere', 'file': 'chapters/connections/arithmetic_shadows.tex', 'line': 349, 'title': 'Sewing trace formula', 'labels_in_block': ['prop:sewing-trace-formula', 'eq:sewing-trace', 'eq:sigma0-zeta-squared']}
{'label': 'thm:sewing-selberg-formula', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/connections/arithmetic_shadows.tex', 'line': 387, 'title': 'Sewing--Selberg formula', 'labels_in_block': ['thm:sewing-selberg-formula', 'eq:sewing-selberg']}
 succeeded in 51ms:
D1 {'file': 'chapters/theory/ordered_associative_chiral_kd.tex', 'line': 2491}
D2 {'file': 'chapters/theory/ordered_associative_chiral_kd.tex', 'line': 2493}
D3 {'file': 'chapters/theory/ordered_associative_chiral_kd.tex', 'line': 2496}
D4 {'file': 'chapters/theory/ordered_associative_chiral_kd.tex', 'line': 2498}
D5 {'file': 'chapters/theory/ordered_associative_chiral_kd.tex', 'line': 2500}

thinking
**Considering claims analysis**

I’m thinking about parsing the claims.jsonl for labels in concordance. I might script something to list all unique references and their statuses from metadata/label_index. This could help me isolate claim labels, particularly missing or unknown ones. I also want to see if concordance cites theorem labels with status macros. However, the scope drift is a concern. I need to identify potential stale entries through existing manuscript quality control. Searching for "concordance" in scripts may help me out!
exec
/bin/zsh -lc "rg -n \"concordance\" scripts metadata -g '*.py' -g '*.sh'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import json,re,collections
from pathlib import Path
text=Path('chapters/connections/concordance.tex').read_text()
labels=re.findall(r'\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}',text)
unique=[]
seen=set()
for x in labels:
    if x not in seen:
        seen.add(x); unique.append(x)
print('total refs',len(labels),'unique',len(unique))
claims=set()
with open('metadata/claims.jsonl') as f:
    claimmap={}
    for line in f:
        obj=json.loads(line)
        claimmap[obj['label']]=obj
count=0
missing=[]
by_status=collections.Counter()
by_env=collections.Counter()
for lab in unique:
    if lab in claimmap:
        count+=1
        by_status[claimmap[lab]['status']]+=1
        by_env[claimmap[lab]['env_type']]+=1
    else:
        missing.append(lab)
print('claim refs',count)
print('status counts',dict(by_status))
print('env counts',dict(by_env))
print('non-claim refs sample',missing[:80])
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
scripts/healing_fortification_40.py:599:1. Read the status in Vol I concordance.tex
scripts/healing_fortification_40.py:671:agent("H34_concordance_completeness", """VERIFY concordance completeness.
scripts/healing_fortification_40.py:673:TARGET: chapters/connections/concordance.tex
scripts/healing_fortification_40.py:676:1. Is it listed in the concordance?
scripts/healing_fortification_40.py:681:Flag any theorem NOT in the concordance. The concordance must be COMPLETE.""")
scripts/mega_rescue_100.py:114:    ("M23_concordance", "chapters/connections/concordance.tex", "CONSTITUTION. Verify EVERY entry matches current .tex. Verify routing remarks. Verify status after all 632 agents."),
scripts/mega_rescue_100.py:116:    ("M25_preface_intro", "chapters/frame/preface.tex + chapters/theory/introduction.tex", "Frame chapters. Verify no scope inflation (AP215). Verify every theorem matches concordance. Symphonic standard."),
scripts/mega_rescue_100.py:203:    ("M66_BD_full", "FULL Beilinson-Drinfeld cross-check. Read BD [BD04] Chapters 3-4. Verify: (a) our chiral Koszul duality extends BD's chiral homology, (b) our E_inf treatment is compatible, (c) Arnold form = BD's factorization structure. Write Remark[BD full comparison] in concordance."),
scripts/platonic_rectification_20.py:436:agent("P17_concordance_sync", """CONCORDANCE CONSTITUTIONAL SYNC.
scripts/platonic_rectification_20.py:438:TARGET: chapters/connections/concordance.tex
scripts/platonic_rectification_20.py:440:YOUR MISSION: Synchronise the concordance (the constitution) with ALL changes from
scripts/platonic_rectification_20.py:443:2. Compare with the concordance entry
scripts/platonic_rectification_20.py:444:3. Update the concordance to match
scripts/platonic_rectification_20.py:490:1. Not overclaim any theorem (compare with concordance)
scripts/platonic_rectification_20.py:499:Focus on the theorem announcement sections. Verify each claim against the concordance.
scripts/platonic_rectification_20.py:516:- All standalones: check theorem status matches current concordance
scripts/adversarial_wave2.py:103:    ("S06_intro_to_body", "introduction.tex", "concordance.tex",
scripts/adversarial_wave2.py:117:    ("S13_concordance_to_body", "concordance.tex", "chiral_koszul_pairs.tex",
scripts/adversarial_wave2.py:118:     "Concordance→Theory. Check: (a) every theorem status in concordance matches the actual .tex, (b) no stale statuses, (c) routing remarks present for circular dependencies"),
scripts/adversarial_wave2.py:206:    "chapters/connections/concordance.tex",
 succeeded in 52ms:
total refs 1395 unique 823
claim refs 471
status counts {'ProvedHere': 373, 'Conditional': 5, 'ProvedElsewhere': 21, 'Conjectured': 71, 'Open': 1}
env counts {'theorem': 221, 'proposition': 139, 'corollary': 31, 'conjecture': 69, 'lemma': 4, 'remark': 4, 'computation': 3}
non-claim refs sample ['def:scalar-lane', 'thm:modular-koszul-duality-main', 'def:modular-convolution-dg-lie', 'eq:bbj-comparison', 'chap:e1-modular-koszul', 'def:shadow-growth-rate', 'eq:discriminant-complementarity', 'constr:dk-shadow-projections', 'part:physics-bridges', 'MK:modular', 'rem:theorem-A-decomposition', 'op:multi-generator-universality', 'rem:four-levels', 'chap:n2-sca', 'chap:moonshine', 'def:modular-homotopy-theory-intro', 'rem:moduli-variation', 'sec:operadic-center-theorem', 'sec:chiral-center-theorem', 'conv:bar-coalgebra-identity', 'rem:theta-modular-twisting', 'rem:four-objects', 'chap:kac-moody', 'sec:concordance-nishinaka-vicedo', 'ch:bv-brst', 'def:modular-cyclic-deformation-complex', 'def:v1-cyclically-admissible-concordance', 'def:shadow-depth-classification', 'def:shadow-postnikov-tower', 'constr:obstruction-recursion', 'sec:heisenberg-shadow-gaussianity', 'eq:factorization-envelope-pipeline', 'constr:v1-platonic-package-concordance', 'def:nms-modular-quartic-resonance-class', 'def:shadow-algebra', 'part:bar-complex', 'part:standard-landscape', 'app:signs', 'def:cech-convolution', 'ex:cech-hca-genus1', 'def:planted-forest-coefficient-algebra', 'constr:degree4-degeneration', 'thm:ambient-d-squared-zero', 'rem:mok25-dependents', 'rem:mok-dependency', 'rem:three-pillar-identifications', 'subsec:concordance-holographic-completion', 'chap:chiral-deformation', 'const:vol1-three-preprints-chain-level', 'const:vol1-log-modular-bar-functor', 'const:vol1-graph-sum-theta-logfm', 'const:vol1-clutching-law-logfm', 'const:vol1-modular-tangent-complex', 'const:vol1-weight-filtration', 'const:vol1-genus-two-shells', 'subsec:three-preprints-chain-level', 'const:vol1-graphwise-log-fm-cocomposition', 'const:vol1-boundary-operators-residue', 'const:vol1-rigid-planted-forest-push-pull', 'def:vol1-rigid-planted-forest-depth-filtration', 'const:vol1-genus-spectral-sequence', 'subsec:primitive-kernel-compression', 'def:primitive-log-modular-kernel', 'def:reduced-branch-master-action', 'thm:categorical-cg-all-types', 'conj:admissible-koszul-rank-obstruction', 'rem:no-bifunctor', 'chap:arithmetic-shadows', 'rem:effective-coupling', 'app:nonlinear-modular-shadows', 'app:branch-line-reductions', 'sec:ambient-complementarity-lagrangian', 'sec:modular-bar-hamiltonian', 'def:modular-bar-hamiltonian', 'sec:modular-chern-weil-transform', 'sec:nms-feynman-transform-programme', 'sec:affine-cubic-shadow', 'sec:betagamma-quartic-birth', 'sec:mixed-cubic-quartic-shadows', 'sec:nms-universal-mc-principle']

thinking
**Evaluating audit statuses**

I need to look at 471 claim references to identify any stale status claims. Searching the concordance for patterns might help, or I could check the labels in major status summaries, as there might only be a few stale items to consider. It’s worth checking existing audit scripts for hints on finding these, like seeing if `fix_campaign_100.py` contains specific target instructions or findings. Searching around those relevant lines sounds like a solid plan.
exec
/bin/zsh -lc "sed -n '430,470p' scripts/platonic_rectification_20.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '140,220p' scripts/fix_campaign_100.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '372,430p' scripts/fix_campaign_100.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4. PROVE the bracket is a derivation of the cup product (Gerstenhaber compatibility)
   using the brace-cup compatibility from the SC^{ch,top} operadic structure.
5. State as ProvedHere with the complete proof.

Search for 'thm:gerstenhaber-structure' and 'const:gerstenhaber-bracket'.""")

agent("P17_concordance_sync", """CONCORDANCE CONSTITUTIONAL SYNC.

TARGET: chapters/connections/concordance.tex

YOUR MISSION: Synchronise the concordance (the constitution) with ALL changes from
the current rectification session. For each theorem:
1. Read the CURRENT theorem statement in its source file
2. Compare with the concordance entry
3. Update the concordance to match

Key updates needed:
- Theorem A: Verdier half at algebra level (post-D_Ran)
- Theorem B: on-locus qi (unconditional) + off-locus coderived (unconditional)
- Theorem C0: coderived version unconditional; ordinary-cohomology version conditional
 succeeded in 51ms:
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

 succeeded in 51ms:
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


thinking
**Reviewing script updates**

I need to check for any stale entries in the script instructions. It’s essential to see if things are already in concordance, so I'll search for terms like "MC5," "topologization," and "Koszul." The user wants an exhaustive review, so I'll audit the current file against the source. I might run a script to list all claim references in concordance. First, I’ll identify likely issues from previous instructions related to theorem statuses and equivalences.
thinking
**Inspecting theorem sources**

I need to focus on using `rg/sed` around labels since my task is just for concordance. Let’s take a look at the relevant theorem source snippets, and I can parallelize this. For theorems A, B, C, D, H, and others, I estimate needing around 20 labels. I could run a command with `rg -n` for labels and then apply `sed` with line numbers. I’ll also identify files with key labels by using `rg` or metadata before compiling a list of labels to reference in the summary sections for manual audits.
codex
I’ve narrowed the likely drift to the parts of the concordance that actually assert status or scope, not every neutral cross-reference. I’m reading those source theorems side by side now: A/B/C/D/H, topologization, MC5/BV, Koszul-equivalence summaries, and the Swiss-cheese/derived-center lane.
exec
/bin/zsh -lc 'rg -n "MC5|topologiz|topologis|Koszul equivalences|Theorem A|Theorem B|Theorem C|Theorem D|Theorem H|Swiss-cheese|operadic center|derived center|family index|genus universality|multi-weight|coderived|chain-level" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
44: the counit is an unconditional coderived coacyclic-equivalence,
48: & C0: coderived fiber-center identification unconditional,
65: multi-weight $g \geq 2$ acquires the cross-channel term
67: $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
311: For multi-weight families, only the genus-$1$
318: \emph{fails} for multi-weight families: the full genus-$g$
321: (Theorem~\ref{thm:multi-weight-genus-expansion},
339: with the derived center in the coderived category unconditionally,
442: $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ is the operadic center of a
444: Swiss-cheese operad $\mathsf{SC}^{\mathrm{ch,top}}$. The pair
446: category of local chiral Swiss-cheese pairs over~$\cA$: for every
464:\emph{chain-level enhancement} of the Feigin--Frenkel center:
602: via configuration space integrals gives explicit chain-level formulas
698: realization via configuration space integrals provides chain-level
715: The genus universality theorem shows that these two perspectives
720:in the coderived category $D^{\mathrm{co}}$ for all shadow classes
721:(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
725:and the chain-level identification fails for class~M
1137:gives the chain-level realization via configuration space
1252: The chain-level story is
exec
/bin/zsh -lc "python3 - <<'PY'
import json
labels = [
 'thm:bar-cobar-isomorphism-main','thm:higher-genus-inversion','thm:bar-cobar-inversion-qi',
 'thm:fiber-center-identification','thm:quantum-complementarity-main','thm:shifted-symplectic-complementarity',
 'thm:modular-characteristic','thm:main-koszul-hoch','thm:hochschild-polynomial-growth','prop:chirhoch1-affine-km',
 'thm:genus-universality','thm:multi-weight-genus-expansion','thm:chain-modular-functor','thm:e1-chiral-koszul-duality',
 'thm:oper-bar','thm:critical-level-cohomology','thm:operadic-center-hochschild','thm:chiral-deligne-tamarkin',
 'thm:topologization','conj:topologization-general','thm:bv-bar-coderived','thm:heisenberg-bv-bar-all-genera','conj:v1-master-bv-brst',
 'thm:koszul-equivalences-meta','thm:family-index','thm:modular-homotopy-convolution','thm:mc2-bar-intrinsic','thm:e1-mc-element'
]
claimmap={}
with open('metadata/claims.jsonl') as f:
    for line in f:
        obj=json.loads(line)
        claimmap[obj['label']]=obj
for lab in labels:
    obj=claimmap.get(lab)
    print('---',lab)
    print(obj)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- thm:bar-cobar-isomorphism-main
{'label': 'thm:bar-cobar-isomorphism-main', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/chiral_koszul_pairs.tex', 'line': 3941, 'title': 'Geometric bar--cobar duality', 'refs_in_block': ['conv:regime-tags', 'sec:frame-inversion', 'def:chiral-koszul-pair']}
--- thm:higher-genus-inversion
{'label': 'thm:higher-genus-inversion', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/higher_genus_complementarity.tex', 'line': 4424, 'title': 'Higher genus inversion', 'refs_in_block': ['conv:regime-tags', 'sec:frame-inversion', 'thm:modular-characteristic', 'thm:multi-weight-genus-expansion', 'def:modular-koszul-chiral']}
--- thm:bar-cobar-inversion-qi
{'label': 'thm:bar-cobar-inversion-qi', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/bar_cobar_adjunction_inversion.tex', 'line': 1606, 'title': 'Bar-cobar inversion: strict on the Koszul locus, coderived off it', 'refs_in_block': ['conv:regime-tags', 'sec:frame-inversion', 'sec:i-adic-completion', 'def:koszul-chiral-algebra', 'thm:higher-genus-inversion', 'thm:pbw-allgenera-km', 'thm:pbw-allgenera-principal-w', 'prop:coderived-bar-degree-spectral-sequence', 'thm:bar-cobar-spectral-sequence', 'thm:spectral-sequence-collapse', 'rem:sl2-admissible', 'rem:virasoro-module-koszul-minimal', 'cor:bar-cobar-inverse', 'thm:positselski-chiral-proved', 'thm:full-derived-module-equiv-proved']}
--- thm:fiber-center-identification
{'label': 'thm:fiber-center-identification', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/higher_genus_complementarity.tex', 'line': 373, 'title': 'Fiber--center identification \\textup{(Theorem~\\texorpdfstring{$\\mathrm{C}_0$}{C0})}', 'labels_in_block': ['thm:fiber-center-identification', 'eq:fiber-center'], 'refs_in_block': ['conv:regime-tags', 'def:modular-koszul-chiral', 'prop:gauss-manin-uncurving-chain', 'lem:perfectness-criterion']}
--- thm:quantum-complementarity-main
{'label': 'thm:quantum-complementarity-main', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/higher_genus_complementarity.tex', 'line': 525, 'title': 'Quantum complementarity as Lagrangian polarization', 'labels_in_block': ['thm:quantum-complementarity-main', 'thm:quantum-complementarity', 'eq:complementarity-decomp', 'eq:verdier-symplectic-pairing', 'eq:quantum-duality'], 'refs_in_block': ['conv:regime-tags', 'thm:chiral-koszul-duality', 'def:complementarity-complexes', 'lem:involution-splitting', 'eq:complementarity-decomp'], 'cites_in_block': ['BD04']}
--- thm:shifted-symplectic-complementarity
{'label': 'thm:shifted-symplectic-complementarity', 'env_type': 'theorem', 'status': 'Conditional', 'file': 'chapters/theory/higher_genus_complementarity.tex', 'line': 2083, 'title': 'Conditional bar-side BV upgrade of complementarity', 'refs_in_block': ['conv:regime-tags', 'thm:config-space-bv', 'thm:bv-functor', 'sec:frame-complementarity', 'thm:verdier-bar-cobar', 'prop:modular-deformation-truncation', 'thm:modular-homotopy-convolution', 'lem:bar-chart-lagrangian-lift'], 'cites_in_block': ['Pridham17']}
--- thm:modular-characteristic
{'label': 'thm:modular-characteristic', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/higher_genus_modular_koszul.tex', 'line': 2844, 'title': 'Modular characteristic', 'labels_in_block': ['thm:modular-characteristic', 'eq:modular-char-gf'], 'refs_in_block': ['conv:regime-tags', 'def:modular-koszul-chiral', 'def:scalar-modular-package', 'thm:multi-generator-universality']}
--- thm:main-koszul-hoch
{'label': 'thm:main-koszul-hoch', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/chiral_hochschild_koszul.tex', 'line': 693, 'title': 'Koszul duality for Hochschild cohomology\n\\textup{(}Theorem~H\\textup{)}', 'labels_in_block': ['thm:main-koszul-hoch', 'eq:hochschild-H-derived'], 'refs_in_block': ['conv:regime-tags', 'def:chiral-koszul-morphism', 'def:bigraded-hochschild', 'lem:hochschild-shift-computation']}
--- thm:hochschild-polynomial-growth
{'label': 'thm:hochschild-polynomial-growth', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/chiral_hochschild_koszul.tex', 'line': 802, 'title': 'Polynomial growth of chiral Hochschild cohomology\n\\textup{(}Theorem~H, growth clause\\textup{)}', 'labels_in_block': ['thm:hochschild-polynomial-growth', 'eq:hoch-hilbert-polynomial'], 'refs_in_block': ['conv:regime-tags', 'thm:main-koszul-hoch']}
--- prop:chirhoch1-affine-km
{'label': 'prop:chirhoch1-affine-km', 'env_type': 'proposition', 'status': 'ProvedHere', 'file': 'chapters/theory/chiral_center_theorem.tex', 'line': 2009, 'title': 'Generic affine first chiral Hochschild group'}

thinking
**Inspecting theorem statements**

I need to check the current theorem statements around key labels to make sure the prose aligns with the intended scope. I'm considering using a tool like sed to handle specific lines more efficiently. It might even be possible to parallelize the process for multiple file snippets. I should also look into the relevant concordance sections. So, let’s focus on the core statements first and get this rolling!
exec
/bin/zsh -lc "sed -n '3910,3995p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4380,4465p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1580,1665p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '350,590p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The \emph{completion entropy} is
\begin{equation}
\label{eq:completion-entropy}
h_K(\cA) \;:=\; \log\bigl(\rho_\cA^{-1}\bigr).
\end{equation}
This is the exponential growth rate of the ideal reduced-weight bar
windows: $h_q \sim e^{q \cdot h_K(\cA)}$ as $q \to \infty$. The
completion entropy is \emph{kinematic}: it depends only on the
primitive spectrum $(g_1, g_2, \ldots)$, hence only on the vacuum
character, and not on curvature parameters such as $c$ or~$k$.
\end{definition}

\begin{remark}[Kinematics versus dynamics]
\label{rem:kinematics-dynamics-split}
\index{completion kinematics!versus dynamics}
\index{modular dynamics}

The completed bar theory separates into two orthogonal axes:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Completion kinematics}:
 succeeded in 51ms:
 finite-dimensional graded pieces, which is
 needed for the duality between contramodules and complete modules
 (Remark~\ref{rem:chiral-contramodules}).
\end{enumerate}
These geometric inputs are specific to the chiral setting and have
no analogue in Positselski's ground-field framework.
\end{remark}

%================================================================
% SECTION: BAR-COBAR INVERSION - COMPLETE QUASI-ISOMORPHISM
%================================================================

\section{Bar-cobar inversion}
\label{sec:bar-cobar-inversion-quasi-iso}

The comodule-contramodule correspondence of the preceding section
provides the categorical framework in which bar-cobar inversion
lives: at genus~$0$ the coderived category reduces to the
ordinary derived category, and the inversion theorem is a
quasi-isomorphism in the classical sense; at genus~$g \geq 1$
 succeeded in 51ms:
$E_2$ with $E_\infty^{p,0} = E_2^{p,0}$. In particular, the
full flat fiber complex $\bar{B}^{(g)}_{\mathrm{flat}}(\cA)\big|_\Sigma$ has
cohomology concentrated in degree~$0$ for every~$\Sigma$.
The uniform vanishing range $q \neq 0$ is independent
of~$[\Sigma]$.

\emph{Step~3: Cohomology and base change.}
The family
$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$
is a proper morphism of finite type. By Steps~1--2, the fiber
cohomology sheaves
$\mathcal{H}^q(R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA))$ vanish for
$q \neq 0$ uniformly over the base, and the surviving
degree-$0$ cohomology sheaf has
finite-dimensional fibers by hypothesis~(ii). The standard
cohomology and base change theorem
(EGA~III, Th\'eor\`eme~7.7.5)
then gives that $R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA)$ is a perfect
complex (bounded, with coherent cohomology sheaves) on
$\overline{\mathcal{M}}_g$.
 succeeded in 51ms:
The cone $C = \operatorname{Cone}(j_g^*\psi_g)$ is therefore a complex of
constructible sheaves on~$U_g$ whose stalk cohomology vanishes at every
geometric point (by the fiberwise quasi-isomorphism just established).
Constructibility of~$C$ is inherited from that of the fiber
cohomology sheaves on~$U_g$
(established in the proof of Theorem~\ref{thm:ss-quantum},
Step~2).
The cohomology sheaves $\mathcal{H}^q(C)$ are therefore
constructible sheaves on the smooth connected stack~$U_g$
whose stalks $\mathcal{H}^q(C)_s = H^q(C_s) = 0$ vanish at
every geometric point~$s$.
A constructible sheaf on a connected base whose stalks are all
zero is the zero sheaf
(see~\cite[Expos\'e~IX, Th\'eor\`eme~2.14]{SGA4});
hence $\mathcal{H}^q(C) = 0$ for all~$q$, which means $C$ is
acyclic and $j_g^*\psi_g$ is a quasi-isomorphism on~$U_g$.
\end{proof}

\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}
For every boundary stratum $D_\Gamma \subset \partial\overline{\mathcal{M}}_g$
exec
/bin/zsh -lc "sed -n '590,700p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
\qquad
Q_0(\cA^!)=0.
\]
\end{theorem}

\begin{remark}\label{rem:lagrangian-decomp}
What one algebra sees as deformation, its dual sees as obstruction.
\end{remark}

\begin{proof}
The proof occupies the remainder of this chapter,
organized as three steps:
Step~I (\S\ref{lem:genus-filtration}ff.) constructs the spectral
sequence from the genus filtration;
Step~II (from Theorem~\ref{thm:verdier-duality-config-complete})
establishes Verdier duality for the configuration space complexes;
Step~III (from Theorem~\ref{thm:kodaira-spencer-chiral-complete})
constructs the Kodaira--Spencer map and identifies the eigenspaces
as Lagrangian complements.

thinking
**Examining D theorem**

I’m considering the D theorem statement and thinking it might be helpful to look into the family index for any internal circularity. This could give me insight into the relationships and properties involved. There’s a lot to unpack here, and I want to ensure I understand everything correctly to draw the right conclusions. It's exciting, but also a bit overwhelming – let’s see where this leads!
exec
/bin/zsh -lc "sed -n '5290,5415p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '680,840p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2820,2915p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '22260,22380p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\operatorname{ch}_k(\mathbb{E}) = B_k \cdot \kappa_k / k!$
(where $\kappa_k$ are the Miller--Morita--Mumford classes),
giving the full multiplicative structure of the obstruction ring.
\end{remark}

\begin{example}[Heisenberg case]\label{ex:heisenberg-obs-squares}
For the Heisenberg algebra with
$\operatorname{obs}_g = \kappa \cdot \lambda_g$ Theorem~\ref{thm:obstruction-nilpotent-all-genera} gives
$(\operatorname{obs}_g)^2 = \kappa^2 \cdot \lambda_g^2 = 0$
for \emph{all} $g \geq 1$, by Mumford's relation.
\end{example}

\subsection{Summary table: obstruction classes for key examples}
\label{subsec:obstruction-summary-table}

\begin{table}[ht]
\centering
\caption{Genus-$g$ obstruction classes For single-generator families, $\mathrm{obs}_g = \kappa \cdot \lambda_g$
 holds unconditionally at all genera. For multi-weight families
 \textup{(}$W_3$\textup{)}, the formula is unconditional at $g = 1$;
 succeeded in 50ms:
\ChirHoch^\bullet(\cA)
\simeq
R\mathrm{Hom}_{\mathrm{ChirAlg}}
\bigl(\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA)),\cA\bigr),
\]
and the bar-cobar counit from
Theorem~\ref{thm:bar-cobar-isomorphism-main}(1) identifies this
with the $\Sigma$-coinvariant descent of $(\cA)^!_\infty$.
This gives~\eqref{eq:chirhoch-descent}.
\end{proof}

\begin{theorem}[Koszul duality for Hochschild cohomology
\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
\label{thm:main-koszul-hoch}
\index{Hochschild cohomology!Koszul duality|textbf}
\textup{[Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For every chiral Koszul datum~$\cA$
\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})} with
 succeeded in 50ms:
|\operatorname{Aut}(\Gamma_1)| \cdot
|\operatorname{Aut}(\Gamma_2)|$ for a graph with a single
separating edge (no automorphism exchanges the two sides).
Collecting all graphs with a separating edge crossing
$\delta_{g_1,S}$ gives
$\xi_{\mathrm{sep}}^* \Omega_{g,n}^{\cA}
= \sum_\alpha \Omega_{g_1}^{\cA}(\cdots, e_\alpha)
\otimes \Omega_{g_2}^{\cA}(\cdots, e^\alpha)$.

\smallskip\noindent
(iii)~\emph{Non-separating boundary.}
The component $\hbar\Delta$ of $D$ acts by contracting two
external half-edges of a graph into an internal self-loop via the
pairing $\eta$. On the graph sum, removing the non-separating
edge~$e$ from $\Gamma$ produces a graph $\Gamma'$ of type
$(g{-}1, n{+}2)$: the genus drops by~$1$ and two new legs appear.
The amplitude is
$\sum_\alpha W_{\Gamma'}(v_1, \ldots, v_n, e_\alpha, e^\alpha)
\cdot P_e(\psi)$.
Collecting all such graphs gives the restriction to the
 succeeded in 50ms:
Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
at scalar level),
exponential $=$ modular automorphy.
See Table~\ref{tab:master-invariants}.
\end{remark}

\medskip
Via the Feynman transform of the Getzler--Kapranov modular operad
$\{\overline{\mathcal{M}}_{g,n}\}_{g,n}$, the genus tower
assembles into a chain-level modular functor
(Theorem~\ref{thm:chain-modular-functor}): to each surface~$\Sigma_{g,n}$ a
cochain complex $V_{g,n} = \barB^{(g)}_n(\cA)$, to each boundary
degeneration a chain map, to each consistency relation a chain
homotopy. Passing to cohomology recovers the classical
modular-functor package; for $\widehat{\fg}_k$ at integrable level, $H^0(V_{g,n})$ is the
Tsuchiya--Ueno--Yamada space of conformal blocks
(Remark~\ref{rem:chain-vs-classical-mf}). The degree-$2$ projection
of $\Theta_\cA$ is the scalar $\kappa(\cA)$ that controls the
entire genus tower (the spectral discriminant~$\Delta_\cA$,
periodicity profile~$\Pi_\cA$, and full MC

thinking
**Inspecting modular functors**

I need to take a closer look at the theorem regarding chain-level modular functors. I'm not entirely sure about its current status, so I want to investigate what I should be aware of. Understanding their behavior and properties could be crucial for my analysis. Let's see if I can gather more information or examples that might clarify things. This might lead to more insights!
exec
/bin/zsh -lc "sed -n '120,220p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1780,1855p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '250,360p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4330,4395p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{equation}
the cotangent module of the oper space.
\end{proposition}

\begin{proof}
Continue with the PBW spectral sequence from
Theorem~\ref{thm:oper-bar-h0}. At critical level, the $E_1$
differentials are induced by the Chevalley--Eilenberg differential
of $\fg$ with coefficients in $S^\bullet(\fg[t^{-1}])$.
In degree~$1$: a class in $H^1$ is a derivation
$\delta\colon H^0 \to H^0$ modulo inner derivations. Since
$H^0 = \mathfrak{z}$ is commutative, inner derivations vanish and
$H^1 = \mathrm{Der}(\mathfrak{z}, \mathfrak{z})$. For a smooth
affine scheme $\mathrm{Spec}(\mathfrak{z})$ (the oper space is
formally smooth by \cite{FG06}), the
module of derivations is the tangent sheaf, dual to $\Omega^1$,
but the \emph{cohomological} invariants are those classified by the bar complex, so
$H^1 = \Omega^1_{\mathfrak{z}/\bC}$ (the cotangent module,
identified via the Harrison complex).
\end{proof}
 succeeded in 52ms:
\end{theorem}

\begin{proof}
The modular operad structure on $\{\overline{\mathcal{M}}_{g,n}\}_{g,n}$ (Getzler--Kapranov) provides clutching and self-gluing maps along boundary divisors. The Feynman transform identification $\bar{B}^{\mathrm{full}}(\mathcal{A}) \simeq \mathrm{FT}_{\mathcal{M}\mathrm{od}}(\mathcal{A})$ (Theorem~\ref{thm:prism-higher-genus}(ii)) assembles the genus-$g$ bar complexes into a single modular algebra. The connecting maps $\rho_{\mathrm{nonsep}}$ and $\rho_{\mathrm{sep}}$ are the restriction-residue maps to the corresponding boundary strata of $\overline{\mathcal{M}}_g$: nonseparating degeneration restricts to the self-sewing boundary (reducing genus by~$1$), while separating degeneration restricts to the product boundary (splitting genus). These maps are compatible with the bar differential by the modular operad axioms. The total complex is the completed direct sum over genera, with the Feynman transform differential encoding all inter-genus contributions.
\end{proof}

\subsection{Chain-level modular functor}\label{subsec:chain-modular-functor}
\index{modular functor!chain-level}

The scalar genus tower
$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
\emph{first Chern class} of a categorically richer object.
The bar complex refines the classical modular-functor
formalism (Segal, Bakalov--Kirillov) to cochain complexes with
$A_\infty$-morphisms as structure maps, and it is this
chain-level modular functor (not the scalar genus tower) that
constitutes the full modular homotopy invariant of a chiral
algebra (Remark~\ref{rem:four-levels}).
The hierarchy is:
\begin{itemize}
 succeeded in 52ms:
with all modes).
$\ChirHoch^1(\mathrm{Vir}_c) = 0$: at generic~$c$, every Verma
module $V(c,h)$ is irreducible (Kac determinant nonvanishing), so all
derivations of $\mathrm{Vir}_c$ are inner.
$\ChirHoch^2(\mathrm{Vir}_c) = \mathbb{C}$: by the Koszul duality
exchange (Theorem~\ref{thm:main-koszul-hoch}),
$\dim \ChirHoch^2(\mathrm{Vir}_c) = \dim Z(\mathrm{Vir}_{26-c}) = 1$.
The generator is the central charge deformation $c \mapsto c + \epsilon$.
\end{proof}

\begin{remark}[Relation to Gel'fand--Fuchs cohomology]
\label{rem:gf-vs-chirhoch}
The continuous Lie algebra cohomology
$H^*_{\mathrm{cont}}(L_1; \mathbb{C}) = \mathbb{C}[\Theta]$ is a
polynomial ring on a degree-$2$ generator
(Gel'fand--Fuchs~\cite{FF84}). This is \emph{not} the chiral
Hochschild cohomology $\ChirHoch^*(\mathrm{Vir}_c)$: the former is
the cohomology of a topological Lie algebra (no curve geometry),
while the latter is an Ext-group on the curve~$X$ that inherits the
de~Rham amplitude bound $[0, 2\dim X] = [0, 2]$ from the
 succeeded in 52ms:
$\cO_\infty \xrightarrow{\sim} \cO$ and takes the homotopy equalizer
in the model-categorical sense; the resulting object is well-defined
up to quasi-isomorphism.
\end{proof}


\subsection{Step 2: Chain-level realization for
\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC-ch,top}}
\label{subsec:center-chain-level}
\index{operadic center!chain-level realization}

\begin{theorem}[The operadic center of
$\mathsf{SC}^{\mathrm{ch,top}}$ is the chiral Hochschild complex;
\ClaimStatusProvedHere]
\label{thm:operadic-center-hochschild}
\index{Hochschild cohomology!as operadic center|textbf}
Let $\cA$ be a logarithmic chiral algebra
\textup{(}an algebra over the closed sector
$(\mathsf{SC}^{\mathrm{ch,top}})^{\mathsf{c}} = \{\FM_k(\bC)\}$
of the holomorphic--topological Swiss-cheese operad, with

thinking
**Inspecting chiral theorems**

I need to check the chiral Deligne-Tamarkin theorem to confirm that the pair is not a bar complex. This task seems crucial, and I want to make sure I get it right. I’m considering what steps I should take to inspect this properly. I wonder if I should look for specific properties or conditions that the theorem satisfies, just to ensure everything is in order. It feels a bit complex, but I'll figure it out!
exec
/bin/zsh -lc "sed -n '1280,1355p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \begin{equation}\label{eq:mixed-p1}
 \mu^{\mathrm{univ}}_{1;n}(f;\, a_1, \ldots, a_n;\,
 \lambda_1, \ldots, \lambda_n)
 \;=\;
 f(a_1, \ldots, a_n;\, \lambda_1, \ldots, \lambda_{n-1}),
 \end{equation}
 i.e., for a single closed insertion, the mixed
 operation is simply the \emph{evaluation} of the
 cochain~$f$ on the open inputs.
\end{enumerate}
\end{construction}

%% ===========================================================
%% 7. CHIRAL DELIGNE--TAMARKIN THEOREM
%% ===========================================================

\subsection{The chiral Deligne--Tamarkin theorem}
\label{subsec:chiral-deligne-tamarkin}

\begin{theorem}[Chiral Deligne--Tamarkin; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "sed -n '2950,3265p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2020,2085p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1380,1985p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The Shapovalov criterion asks: are there null vectors in the
bar-relevant range? The Li--bar criterion asks: does the
\emph{geometry} of the associated variety~$X_V$ force those
null vectors to produce off-diagonal bar cohomology?

The gain is maximal when $X_V \neq \{0\}$ and one can
separately establish diagonal concentration on the reduced
Li--bar page, possibly guided by geometric input from a
symplectic resolution. Minimal-orbit levels are the first
test case where the reduced geometry suggests concentration, but
an unconditional Koszul theorem still requires the extra
reducedness and reduced Li--bar concentration hypotheses recorded in
Corollary~\ref{cor:minimal-orbit-koszul}.
\end{remark}

\begin{theorem}[Equivalences and consequences of chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:koszul-equivalences-meta}
\index{Koszul property!equivalences of characterizations|textbf}

Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
 succeeded in 52ms:
BRST-type differential on the algebra of observables
of a holomorphic--topological theory~$T$ on
$\bC \times \bR$ whose boundary chiral algebra
is~$\cA$. An \emph{inner conformal vector} for
$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
central charge~$c$ that is $Q$-exact in the algebra
of bulk observables up to a $Q$-boundary: there exists
$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
For affine Kac--Moody $V_k(\fg)$ at non-critical level,
the Sugawara element
$T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
\sum_a {:}J^a J_a{:}$
provides the inner conformal vector. For the
Virasoro algebra, $T(z)$ is the stress tensor itself.
\end{definition}

\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
\label{thm:topologization}
\ClaimStatusProvedHere
 succeeded in 52ms:
Functoriality of the underlying bar construction is standard. The
extra BV functoriality and lax monoidal statements are exactly the
assumed functorial and tensor-compatibility properties of the
conditional BV package, while the Verdier-duality comparison is part
of the additional hypothesis in the theorem statement.
\end{proof}

\begin{remark}[Shifted symplectic structure from BV]\label{rem:bv-shifted-symplectic}
\index{shifted symplectic!from BV}
Conditional on Theorems~\ref{thm:config-space-bv}
and~\ref{thm:bv-functor}, the BV bracket on
$\barB^{\mathrm{ch}}(\cA)$ would provide a bar-side
$(-1)$-shifted Poisson model for the deformation theory. The
unconditional shifted-symplectic statements used later in the
manuscript instead come from the Verdier pairing on
$C_g = R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$
\textup{(}Proposition~\ref{prop:ptvv-lagrangian}\textup{)} and from
the ambient cyclic deformation formal moduli problem
\textup{(}Theorem~\ref{thm:ambient-complementarity-fmp}\textup{)}.
\end{remark}
exec
/bin/zsh -lc "sed -n '2085,2155p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \]
 \textup{(UNIFORM-WEIGHT; Theorem~\textup{\ref{thm:genus-universality})}.}
\item[\textup{(ix)}] The Kac--Shapovalov determinant
 $\det G_h \neq 0$ in the bar-relevant range
 \textup{(}Theorem~\textup{\ref{thm:kac-shapovalov-koszulness})}.
\item[\textup{(x)}] The restriction
 $i_S^!\,\barB_n(\cA)$ to every FM boundary stratum~$S$ is
 acyclic outside degree~$0$.
\end{enumerate}

\smallskip
\noindent\textbf{One-way Hochschild consequence on the Koszul locus:}
\begin{enumerate}
\item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
 cohomological degrees $\{0,1,2\}$ and satisfies the duality
 \[
 \ChirHoch^n(\cA)
 \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X
 \]
 with Hochschild--Hilbert series

thinking
**Inspecting the e1 theorem**

I need to take a closer look at the e1 theorem and its family index within the concordance. There's a possibility that this theorem might exist there and could be circular. I might need to adjust the concordance if my own theorem is out of date. It's essential to examine the family index and the specific theorem statement lines to ensure everything aligns correctly and accurately. Let's see what I can find!
exec
/bin/zsh -lc "sed -n '6000,6075p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For $\beta\gamma$: the unique standard family with
$\kappa<0$. Branch point at $x=-1/2$; the genus tower has
alternating signs.

\emph{Duality.}
$\Delta_{\cA^!}(x)=\Delta_\cA(x)$ for all Koszul pairs:
the spectral discriminant is self-dual. For
$\widehat{\mathfrak{sl}}_2$: the zero at $1/k$ corresponds
to level~$k$; the zero at $1/(k{+}4)$ corresponds to the
dual level $-k-4$. The product of the two zeros is
$1/(k(k{+}4))$; their sum is $(2k{+}4)/(k(k{+}4))=2/k+2/(k{+}4)
\to 0$ as $k\to\infty$.

\emph{Rank.}
$\operatorname{rank}(\Delta_\cA)
=\deg\Delta_\cA
=\dim H^1_{\mathrm{cyc,prim}}(\cA)$: the number of independent
genus-$1$ deformation directions. Rank~$1$ for algebras with
one-dimensional deformation space (Heisenberg, Virasoro,
$\beta\gamma$); rank~$2$ for $\widehat{\mathfrak{sl}}_2$ and
exec
/bin/zsh -lc "sed -n '1968,2008p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7270,7335p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3368,3392p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Higgs field
 (Theorem~\ref{thm:shadow-higgs-field}) has convergence
 radius $|c|/3$ in the degree variable;
 the MC4 completion radius is controlled by the same parameter
 $\lambda_{\mathrm{eff}} = -6/c$
 (Chapter~\ref{chap:arithmetic-shadows},
 Remark~\ref{rem:effective-coupling}).
\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
 Inductive genus
 determination, 2D convergence (no UV renormalization needed),
 analytic-algebraic comparison, and the general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
 plus subexponential sector growth implies convergence at all genera).
 Heisenberg sewing proved (Theorem~\ref{thm:heisenberg-sewing}:
 one-particle Bergman reduction, Fredholm determinant). At genus~$0$
 the algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}.
 BV=bar in the coderived category is proved for all four shadow
 succeeded in 51ms:
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$
 without conformal vector \textup{(}Conjecture\textup{)}
 & \S\ref{sec:en-koszul-duality} \\
\ref{conj:center-essential-surjectivity}
 & Center essential surjectivity:
 every $E_2$-chiral algebra arises as a derived center
 \textup{(}Conjecture\textup{)}
 & \S\ref{sec:en-koszul-duality} \\
\ref{constr:sugawara-antighost}
 & Sugawara antighost construction:
 conformal vector at non-critical level yields
 antighost field for topologization
 & \S\ref{sec:en-koszul-duality} \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: AP165 bar-complex operadic correction}} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{AP165 correction (constitutional).}
 The bar complex $\barB(\cA)$ is an $E_1$ coassociative
 succeeded in 51ms:
 filtration axiom $\mu_r(F^{i_1},\ldots,F^{i_r}) \subset
 F^{i_1+\cdots+i_r}$ gives degree cutoff
 (Lemma~\ref{lem:degree-cutoff}), making continuity
 and Mittag-Leffler automatic
 (Theorem~\ref{thm:completed-bar-cobar-strong}).
 Positive towers are handled by coefficient stabilization; the
 resonance lane is proved on the transferred split surface of
 Theorems~\ref{thm:resonance-filtered-bar-cobar}
 and~\ref{thm:platonic-completion}. \\
MC5 & Genus tower & Five components:
 (1)~\textbf{Analytic HS-sewing proved} at all genera: polynomial OPE growth $+$ subexponential sector growth implies convergence
 (Theorem~\ref{thm:general-hs-sewing});
 (2)~\textbf{Genus-$0$ algebraic BRST/bar proved}
 (Theorem~\ref{thm:algebraic-string-dictionary});
 (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived});
 (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
 (classes~G/L proved, class~C conditional on harmonic decoupling,
 class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
 (5)~tree-level amplitude pairing \textbf{conditional} on
exec
/bin/zsh -lc "sed -n '3941,4015p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
character. The same-family shadow $\mathrm{Vir}_{26-c}$
lives on the dynamic axis
(Remark~\ref{rem:virasoro-resonance-model});
kinematically, even generic Virasoro has infinitely many
primitive cumulants, with $g_r = p(r+1) - p(r)$ growing
without bound.

\smallskip
This separation is structurally clean: the primitive spectrum
determines \emph{how large} the completed bar coalgebra is
(how many words at each reduced weight), while the OPE data
determines \emph{what the differential does} on those words.
Both axes are needed for the full MC4 theory
(Theorem~\textup{\ref{thm:completed-bar-cobar-strong}}).
\end{remark}

\begin{proposition}[Cumulant-to-window inversion; \ClaimStatusProvedHere]
\label{prop:cumulant-window-inversion}
\index{cumulant-to-window inversion|textbf}
\index{primitive cumulant spectrum!recovery from windows}
exec
/bin/zsh -lc "sed -n '4015,4105p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{bar-cobar duality!main theorem|textbf}
\index{Theorem A|textbf}
\textup{[}Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
The equivalences below hold in the derived category
$D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
factorization algebras on~$X$.

\smallskip\noindent
The Heisenberg instance was verified in~\S\ref{sec:frame-inversion}.
In general:

Let $(\cA_1, \cC_1, \tau_1, F_\bullet)$ and
$(\cA_2, \cC_2, \tau_2, F_\bullet)$ be a chiral Koszul pair in
the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
Then:
\begin{enumerate}
\item the canonical units and counits are quasi-isomorphisms:
\[
\cC_i \xrightarrow{\;\sim\;} \bar{B}_X(\cA_i), \qquad

thinking
**Reviewing theories and claims**

I'm checking the concordance entry, and it looks okay. I think I might need to inspect the E1 claim, but it seems Theorem 4 could be relevant since it mentions that E1-chiral Koszul duality extends to Yangians and toroidal areas, going beyond E_inf. However, I should verify if the theorem statement is broad enough. It cites something on line 5290 related to chiral_koszul_pairs, so I could read that snippet for clarity.
exec
/bin/zsh -lc "sed -n '5280,5338p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$W_N$ & $2N$ & I-adic & Complexity $\sim N^2$ \\
Affine Yangian & $\infty$ & Double (I + $\hbar$) & Spectral parameter \\
Bershadsky--Polyakov & 4 & I + $\sqrt{c}$-adic & Fractional exponents \\
$\mathcal{N}=2$ Super & 3 & I-adic (super) & Fermion signs \\
\hline
\end{tabular}
\end{table}

\begin{remark}[Feynman diagrams]\label{sec:feynman_genus_g}
The Feynman diagram interpretation of the bar-cobar complex (the identification
of bar chains with off-shell amplitudes and cobar chains with on-shell propagator
templates) is developed in Chapter~\ref{ch:feynman}.
\end{remark}

% Feynman diagram exposition (formerly ~210 lines) moved to Chapter~\ref{ch:feynman}.

% ================================================================
% SECTION: E1-CHIRAL KOSZUL DUALITY
% ================================================================
\section{\texorpdfstring{The $\Eone$-chiral Koszul duality theorem}{The E1-chiral Koszul duality theorem}}
exec
/bin/zsh -lc "sed -n '5410,5495p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\emph{Step 1: Reduction to the classical operadic statement.}
By Proposition~\ref{prop:chirAss-self-dual}, the chiral associative
operad $\chirAss$ is the chiral lift of the classical associative
operad $\operatorname{Ass}$. The bar-cobar adjunction for a Koszul
operad $\mathcal{P}$ in a stable presentably symmetric monoidal
$\infty$-category $\mathcal{V}$ is an equivalence
$\mathcal{P}\text{-Alg}^{\mathrm{aug,pronil}}(\mathcal{V})
\simeq
\mathcal{P}^!\text{-CoAlg}^{\mathrm{coaug,conil}}(\mathcal{V})$
whenever $\mathcal{P}$ is Koszul \cite[Theorem~11.4.1]{LV12}.
We apply this with $\mathcal{V} = \mathcal{D}\text{-mod}(X)$
(the stable $\infty$-category of $\mathcal{D}$-modules on~$X$,
equipped with the chiral tensor product) and
$\mathcal{P} = \operatorname{Ass}$.

\emph{Step 2: Koszulity of $\operatorname{Ass}$ in the chiral
tensor category.}
By Lemma~\ref{lem:operadic-koszul-transfer} below
(applied with $\mathcal{P} = \operatorname{Ass}$ and
exec
/bin/zsh -lc "sed -n '7298,7322p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{SC self-duality retracted.}
 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
 \text{shuffle-mixed})$: the closed dimensions are
 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not}
 Koszul self-dual. The duality \emph{functor} is an
 involution; the \emph{operad} is not self-dual.
 See AP166/B57.} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{Topologization scoped.}
 The cohomological topologization theorem
 (Theorem~\ref{thm:topologization}:
 $\SCchtop + \text{inner conformal vector}
 \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
 is proved for affine Kac--Moody at non-critical level.
 The same theorem gives an unconditional chain-level
 $E_3^{\mathrm{top}}$ model on the zero-differential
 cohomology complex, which is quasi-isomorphic as a chain

thinking
**Inspecting the theorem**

I think I need to check the consistency with the theorem I'm looking at. It seems important to investigate the concordance related to the Swiss-cheese theorem, particularly around line 6881. I want to make sure that it doesn't impose any unintended structure on the bar complex. I'll also look around line 6862 for more context. Gathering all this information will help clarify everything!
exec
/bin/zsh -lc "sed -n '6860,6915p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{remark}

\subsection{The open/closed realization and the chiral derived center}
\label{subsec:concordance-open-closed-realization}
\index{derived center!chiral!concordance}
\index{open/closed realization!concordance}

The open/closed realization
(\S\ref{sec:thqg-open-closed-realization})
constructs the algebraic bridge between the local Hochschild theory
and the global bordered FM geometry. The central results:
\begin{enumerate}[label=\textup{(\alph*)}]
\item The \emph{chiral endomorphism operad}
 $\mathcal{E}\!nd^{\mathrm{ch}}_A$ with consecutive block-substitution
 (Definition~\ref{def:thqg-chiral-endomorphism-operad}).
 This is the nonsymmetric operad governing $A_\infty$-chiral algebras.
\item The \emph{brace dg algebra structure} on chiral Hochschild cochains
 $\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA)$
 (Theorem~\ref{thm:thqg-brace-dg-algebra}). \textbf{Proved}:
 the same tree-combinatorial argument as Gerstenhaber--Voronov,

thinking
**Considering table edits**

I'm thinking about the top table row. Perhaps it could include an edit to reflect something specific. For row B, I believe it might need to state that "off the locus, the counit is an unconditional coderived coacyclic-equivalence, promoted back to an ordinary quasi-isomorphism on collapse loci & ProvedHere." I want to ensure clarity in these edits while keeping them accurate! Let’s refine this further as needed.
exec
/bin/zsh -lc 'rg -n "collapse loci|collapse locus|collapse" chapters/connections/concordance.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:349:or out of the zero row), and the spectral sequence collapses at
chapters/theory/higher_genus_complementarity.tex:452:\emph{Step~3: Identify the associated graded and collapse.}
chapters/theory/higher_genus_complementarity.tex:1137:concentrated on $q = 0$. The spectral sequence therefore collapses
chapters/theory/higher_genus_complementarity.tex:4377:spectral sequence collapses at~$E_2$, and the counit~$\psi_s$
chapters/theory/higher_genus_complementarity.tex:4459:H^{p+q}(\Omega_g \bar{B}_g(\cA))$ collapses at $E_2$.
chapters/theory/higher_genus_complementarity.tex:4495:The asserted $E_2$-collapse is proved separately in
chapters/theory/higher_genus_complementarity.tex:4496:Lemma~\ref{lem:e2-collapse-higher-genus}.
chapters/theory/higher_genus_complementarity.tex:4549:\begin{lemma}[\texorpdfstring{$E_2$}{E2} collapse at higher genus;
chapters/theory/higher_genus_complementarity.tex:4550:\ClaimStatusProvedHere]\label{lem:e2-collapse-higher-genus}
chapters/theory/higher_genus_complementarity.tex:4551:\index{spectral sequence!E2 collapse@$E_2$ collapse!higher genus}
chapters/theory/higher_genus_complementarity.tex:4579:(excision, Ayala--Francis~\cite{AF15}); $E_2$-collapse on the Koszul
chapters/theory/higher_genus_complementarity.tex:4595:\emph{Step~C}: PBW spectral sequence collapses at $E_2$
chapters/theory/higher_genus_complementarity.tex:4596:(Lemma~\ref{lem:e2-collapse-higher-genus}), yielding Riordan/Motzkin
chapters/theory/higher_genus_complementarity.tex:4763:\begin{proposition}[\texorpdfstring{$E_2$}{E2}-collapse as formality;
chapters/theory/higher_genus_complementarity.tex:4765:\label{prop:e2-collapse-formality}
chapters/theory/higher_genus_complementarity.tex:4766:\index{formality!spectral sequence collapse}
chapters/theory/higher_genus_complementarity.tex:4772:collapses at~$E_2$ for all $g \geq 0$.
chapters/theory/higher_genus_complementarity.tex:4805:formal $\Ainf$-algebra necessarily collapses at~$E_2$:
chapters/theory/higher_genus_complementarity.tex:6162:tower of $\cA^!$ collapses to the tree-level term
chapters/theory/chiral_koszul_pairs.tex:63:unconditional equivalences: $E_2$-collapse of the bar spectral sequence,

thinking
**Considering automation for claims**

I'm thinking about how to automate the process involving claims in concordance that are marked as either conjectures or conditionals. I should check for unique claims that aren't marked as “ProvedHere” or “ProvedElsewhere.” It’ll involve extracting surrounding lines of text and searching for contradictory keywords like "proved" and "unconditional." Using some straightforward heuristics seems feasible for this scripting task on references related to Conditional/Conjectured/Open claims. This feels manageable!
codex
I’ve confirmed the headline theorem sources. The remaining risk is inside the concordance prose where it talks about conditional or conjectural items, so I’m running a targeted pass over every non-`ProvedHere` label it cites and checking whether the wording stayed honest.
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
text=Path('chapters/connections/concordance.tex').read_text().splitlines()
# build claim map
claimmap={}
with open('metadata/claims.jsonl') as f:
    for line in f:
        obj=json.loads(line)
        claimmap[obj['label']]=obj
# labels with non-ProvedHere status used in concordance
labels=[]
for i,line in enumerate(text,1):
    for lab in re.findall(r'\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}', line):
        if lab in claimmap and claimmap[lab]['status']"'!='"'ProvedHere':
            labels.append((i,lab,claimmap[lab]['status']))
# unique by label with first few occurrences
seen={}
for i,lab,status in labels:
    seen.setdefault(lab,[]).append(i)
for lab,lines in sorted(seen.items(), key=lambda x:(claimmap[x[0]]['status'],x[0])):
    status=claimmap[lab]['status']
    print(f'=== {lab} [{status}] {claimmap[lab][\"file\"]}:{claimmap[lab][\"line\"]} {claimmap[lab][\"title\"]}')
    for ln in lines[:4]:
        start=max(1,ln-1); end=min(len(text),ln+1)
        for j in range(start,end+1):
            print(f'{j}: {text[j-1]}')
        print('---')
    print()
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
=== cor:dk-partial-conj [Conditional] chapters/examples/yangians_computations.tex:1809 Type-$A$ evaluation-generated extension principle
6499:  the ambient extension/comparison package on the module side
6500:  \textup{(}Corollary~\ref{cor:dk-partial-conj}\textup{)}.
6501: \item \textbf{DK-4/DK-5 (the Bridge Theorem project):} the dg-shifted Yangian and
---

=== cor:dk-poly-catO [Conditional] chapters/examples/yangians_computations.tex:1838 Factorization DK for polynomial
category~\texorpdfstring{$\mathcal{O}$}{O}, type~\texorpdfstring{$A$}{A}
6481:  extension/comparison package}. On the Yangian module surface,
6482:  Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
6483:  are only conditional thick-generation extension criteria: once one
---

=== cor:string-amplitude-genus0 [Conditional] chapters/examples/free_fields.tex:4834 Conditional genus-\texorpdfstring{$0$}{0} amplitude pairing from the bar complex
1985:  amplitude pairing is conditional on
1986:  Corollary~\ref{cor:string-amplitude-genus0}.
1987:  BV=bar in the coderived category is proved for all four shadow
---
3387:  (5)~tree-level amplitude pairing \textbf{conditional} on
3388:  Corollary~\ref{cor:string-amplitude-genus0} \\
exec
/bin/zsh -lc "sed -n '6248,6385p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{genus tower!as modular operad corollary}%
Theorem~\ref{thm:bar-modular-operad} makes the modular operad algebra structure,
previously invoked implicitly as ``functorial compatibility with
Getzler--Kapranov,'' into an explicit algebraic statement. All genus-tower
structure (the decomposition $d_{\mathrm{full}} = \sum_g d_g$, the
cross-genus cancellations in the proof of
Theorem~\ref{thm:genus-induction-strict}, and the recursive computation of bar
cohomology by genus) is a formal corollary of the bar complex being an
$\mathsf{F}\mathrm{Com}$-algebra.
The $\mathsf{F}\mathrm{Com}$-algebra structure is the strict
incarnation of the homotopy modular coalgebra on $\barB(\cA)$;
the Feynman transform provides the homotopy-invariant formulation
(Getzler--Kapranov~\cite[\S5]{GetzlerKapranov98}).
\end{remark}

\begin{theorem}[Bar-cobar as Quillen equivalence;
\ClaimStatusProvedElsewhere]
\label{thm:quillen-equivalence-chiral}
\index{Quillen equivalence!bar-cobar|textbf}
\index{bar-cobar!Quillen equivalence}

thinking
**Inspecting theorem status**

I see that the theorem status is marked as ProvedElsewhere. The concordance principal treats it as a contribution, which feels okay since the repo includes applications. But the user is asking about the status relative to the current .tex source. Maybe I should clarify that the Quillen upgrade is ProvedElsewhere or a literature refinement, rather than part of the original theorem package. I need to check around lines 4800 to see if there's a summary table with theorem statuses. Let’s look closer at lines 4798-4820.
exec
/bin/zsh -lc "sed -n '4798,4822p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}cp{4.4cm}p{3.8cm}p{4.6cm}@{}}
\toprule
\textbf{Label} & \textbf{Statement} & \textbf{Status} & \textbf{Reference} \\
\midrule
$A_{\mathrm{mod}}$ & Bar-cobar intertwined with Verdier, & \textbf{Proved} & Thm~\ref{thm:bar-cobar-isomorphism-main} \\
 & at the algebra level only after $\mathbb{D}_{\Ran}$; & & \\ 
 & functorial over $\overline{\mathcal{M}}_{g,n}$ & & \\[2pt]
$B_{\mathrm{mod}}$ & Strict inversion on the Koszul locus; & \textbf{Proved} on the Koszul locus; & Thms~\ref{thm:higher-genus-inversion}, \\
 & off-locus continuation in $D^{\mathrm{co}}$ and & off-locus coderived continuation & \ref{thm:bar-cobar-inversion-qi} \\ 
 & promotion back to ordinary q.i.\ on collapse loci & \textbf{proved} & \\[2pt]
$C_{\mathrm{mod}}$ & C0 fiber-center identification; C1 duality / & C0/C1: \textbf{Proved}; & Thms~\ref{thm:fiber-center-identification}, \\
 & Lagrangian complementarity; C2 shifted-symplectic upgrade & C2: \textbf{Conditional} & \ref{thm:quantum-complementarity-main}, \\
 & on the uniform-weight BV lane & & \ref{thm:shifted-symplectic-complementarity} \\[2pt]
Index & Scalar genus series on the uniform-weight lane; & \textbf{Proved} on the stated lane; & Thms~\ref{thm:modular-characteristic}, \\
 & genus-$1$ unconditional; family-index routed downstream & genus-$1$ universal & \ref{thm:family-index} \\[2pt]
DK & DK-0/1/$1\frac{1}{2}$: chain-level, eval-locus, lattice; & DK-0/1/$1\frac{1}{2}$: proved (all types); & Thms~\ref{thm:derived-dk-affine}, \\
 & DK-2/3: generated-core DK comparison; & DK-2/3: \textbf{proved} (eval-gen.\ core, all types; $\mathcal{O}_{\mathrm{poly}}$ only on the separate type-$A$ thick-generation lane; & \ref{thm:derived-dk-yangian}, \ref{thm:factorization-dk-eval}, \\
 & DK-4/5: dg-shifted/triple bridge & uses Molev PBW \cite{molev-yangians}); DK-4: ML proved, alg.\ id.\ open; DK-5: \textbf{proved for $\mathfrak{sl}_2$} (FRT, Prop.~\ref{prop:dk5-sl2-frt}); general: conj. & \ref{conj:dk-fd-typeA}, \ref{cor:dk23-all-types}, \ref{thm:rtt-mittag-leffler}; Conj.~\ref{conj:full-dk-bridge} \\[2pt]
exec
/bin/zsh -lc "sed -n '2416,2490p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\subsection{The meta-theorem: twelve characterizations}
\label{subsec:concordance-koszulness-meta-theorem}
\index{Koszul property!equivalences|textbf}

Let $\cA$ be an augmented chiral algebra with PBW
filtration~$F_\bullet$. The full meta-theorem is
Theorem~\ref{thm:koszul-equivalences-meta} in
Chapter~\ref{chap:koszul-pairs}.
Items are listed in the meta-theorem's numbering, so that
\textup{(\ref{item:kp-def})}--\textup{(\ref{item:kp-dmod})}
in the concordance and in the chapter are identical.

\medskip\noindent
\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):

\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
\item\label{item:kp-def}
 Chirally Koszul (Definition~\ref{def:chiral-koszul-morphism}).
 \hfill \checkmark
\item\label{item:kp-pbw}

thinking
**Inspecting theorem updates**

I think the section I have is already updated, so it should be fine. However, I might need to look into the D theorem family index routing lines, just to be safe. A previous script mentioned searching for "thm:family-index" and "thm:genus-universality," suggesting I should add something to break a circular dependency. I should inspect the proof for `thm:family-index` around line 6029 to ensure it’s not circular.
exec
/bin/zsh -lc "sed -n '6075,6165p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{$\hat{A}$-genus identification.}
On the same uniform-weight locus, the total generating function is
\begin{equation}\label{eq:family-index-generating}
\sum_{g \geq 1} F_g(\cA)\, x^{2g}
\;=\;
\kappa(\cA) \cdot \bigl(\hat{A}(ix) - 1\bigr)
\;=\;
\kappa(\cA) \cdot
\left(\frac{x/2}{\sin(x/2)} - 1\right),
\end{equation}
where the function $(x/2)/\sin(x/2)$ arises from
$\operatorname{Td}(T_\pi) = c_1(\omega_\pi)/(1 - e^{-c_1(\omega_\pi)})$
in the GRR formula, Wick-rotated by the positivity of
tautological intersection numbers on
$\overline{\mathcal{M}}_g$.

\item \emph{Verdier compatibility.}
Under Koszul duality $\cA \leftrightarrow \cA^!$,
$\mathcal{D}_{\cA^!}^{(g)} = \kappa(\cA^!) \cdot \mathbb{E}$,
and the complementarity

thinking
**Evaluating TODO comments**

I'm noticing a TODO(comment) around status-sync that seems stale, maybe it's a good idea to remove it. The user task mentions flagging stale entries, so it's worth considering this comment in the context of it being a temporary plan or chatter that may be against AGENTS policy. Since it's in the target file, I should probably look into it more. I’ll conduct a search for any comments related to TODO/status-sync to verify.
codex
I found one concrete stale surface already: a lingering `% TODO(status-sync)` note inside the concordance proof. That doesn’t belong in the constitutional file, so I’ll remove it along with any similar temporary audit residue after I finish the theorem-scope pass.
exec
/bin/zsh -lc "rg -n \"TODO\\(|TODO|status-sync|remaining rectification|temporary|TODO\\(status-sync\\)\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
6122:% TODO(status-sync): After the remaining rectification passes land,



thinking
**Evaluating author claims**

I'm considering if this status issue arises because the audit needs to match with the current .tex source. It doesn't state that something is "proved" directly, but the way contributions are listed might exaggerate authorship. I think I should look for references to "ProvedElsewhere" claims to see if they're clearly labeled or not. For instance, the rectification-ch-infty item might mislead readers if it doesn't specify where things are proved. There's also a theorem in the manuscript that could be mentioned as a corollary, but if it's not original, it needs clear status.
thinking
**Investigating ProvedElsewhere references**

I’m wondering if there are any other ProvedElsewhere references in the principal contributions list. The `thm:critical-level-cohomology` might have some, and there could be others too. Item 7 mentions that Theorem H doesn't apply in this context, and instead, the oper/Feigin-Frenkel package is documented by the Theorem critical-level-cohomology. It's important to ensure all claims are clearly stated, so I should check those references carefully.
thinking
**Considering mathematical properties**

I see a statement mentioning class G or L and how it relates to weak equivalence in filtered curved models. I'm trying to unpack the meaning of that, particularly what it says about \(f_g\). It seems like there's an interesting connection here! I want to understand how these concepts interact and establish whether this weak equivalence holds in the context mentioned.  Exploring these mathematical relations can be quite fascinating!
exec
/bin/zsh -lc "sed -n '664,706p' scripts/healing_fortification_40.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '394,420p' scripts/rectification_campaign.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '460,520p' scripts/elite_rescue_40.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
agent("R14_concordance", """TARGET: chapters/connections/concordance.tex

This is the CONSTITUTION. All status changes from other fixes must be reflected here.

FINDINGS TO FIX:

1. [CRITICAL T06] Line ~6010: thm:family-index cites thm:genus-universality,
   creating circular dependency with Theorem D.
   FIX: Add a ROUTING REMARK (AP147) that breaks the circle by identifying the
   non-circular proof path. The anchor should be: shadow tower construction → universality → family index.

2. After ALL other agents complete, this file needs to be updated to reflect:
   - Any theorem status downgrades (ProvedHere → Conditional)
   - Any scope narrowings (all genera → g>=1, chain-level → cohomological)
   - Any missing-lemma additions

For now: fix the circular dependency routing. Leave a TODO for the status sync pass.

Read the file, find line 6010, add the routing remark.""")

 succeeded in 52ms:
2. Find the matching compute engine
3. Verify the engine produces the census value
4. Run the test
5. Flag any disagreement

Focus on the 10 most important families: Heis, KM, Vir, W_2, W_3, bc, bg, BP, lattice, sl_2.""")

agent("H34_concordance_completeness", """VERIFY concordance completeness.

TARGET: chapters/connections/concordance.tex

For each theorem in the manuscript (use the theorem registry):
1. Is it listed in the concordance?
2. Is the status correct?
3. Is the scope correct?
4. Are the dependencies listed?

Flag any theorem NOT in the concordance. The concordance must be COMPLETE.""")

agent("H35_build_verification", """BUILD VERIFICATION across all three volumes.
 succeeded in 52ms:
2. AGENTS.md skill routing still correct
3. Anti-pattern catalog (AP1-AP224) referenced correctly
4. Formula census (C1-C31) still accurate after all rectification
5. No stale claims in either file
Fix any stale content.""")

agent("H08_heal_concordance_final", """FINAL concordance healing.

Read chapters/connections/concordance.tex in its CURRENT state.
For EVERY theorem listed:
1. Find the theorem in its source file
2. Verify status matches
3. Verify scope matches
4. Verify the proof is present (if ProvedHere)
This is the FINAL constitutional audit of this session.
Fix every discrepancy.""")

agent("H09_heal_introduction_preface", """HEAL the introduction and preface after all rectification.

The platonic agents P18 (introduction) and P19 (preface) upgraded these.

thinking
**Evaluating campaign directives**

I find it interesting that the rectification campaign instructed to leave a TODO for status sync. Now the user is asking for the final constitutional audit, so it seems like that TODO should be removed. Great! I might want to look for any other stale items marked "for now" and see if they also need updating or removal. It feels good to tidy things up!
exec
/bin/zsh -lc "rg -n \"for now|remaining rectification|status sync pass|TODO\\(|temporary|after all other agents|stale\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
6122:% TODO(status-sync): After the remaining rectification passes land,
exec
/bin/zsh -lc 'rg -n "thm:quillen-equivalence-chiral|cor:rectification-ch-infty|thm:critical-level-cohomology|thm:oper-bar|thm:operadic-center-hochschild|thm:chiral-deligne-tamarkin" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
253:(Theorem~\ref{thm:oper-bar-h0-dl}) is the bar \emph{cohomology}
299: (Theorem~\ref{thm:quillen-equivalence-chiral});
302: (Corollary~\ref{cor:rectification-ch-infty}).
382: (Theorem~\ref{thm:oper-bar}).}
415: is recorded instead by Theorem~\ref{thm:critical-level-cohomology}.
439: (Theorems~\textup{\ref{thm:operadic-center-hochschild}}
440: and~\textup{\ref{thm:chiral-deligne-tamarkin}}).}
469:(Theorem~\ref{thm:oper-bar}).
1341: (Theorem~\ref{thm:quillen-equivalence-chiral}).
1588:Thm~\ref{thm:quillen-equivalence-chiral}
3069:\item \emph{Critical level}: $V_{-h^\vee}(\fg)$ is uncurved ($\kappa=0$), self-dual under the Feigin--Frenkel involution ($k=-h^\vee$ is a fixed point of $k \mapsto -k-2h^\vee$), center~$= \mathfrak{z}(\widehat{\fg})$ (Theorem~\ref{thm:critical-level-cohomology}).
3096:(Theorem~\ref{thm:quillen-equivalence-chiral}). This is why
3995:(Theorem~\ref{thm:operadic-center-hochschild}) provides the
8033:(Theorem~\ref{thm:oper-bar-h0-dl}), and the full
8038:(Theorem~\ref{thm:oper-bar}).
8101:Theorem~\ref{thm:critical-level-cohomology} belong to

thinking
**Checking table status**

I need to inspect around 1341 and 1588, specifically in the tables where the status is provided. There might be some mismatches I need to look into. It’s important to get this sorted because discrepancies can lead to larger issues down the line, and I want to make sure everything aligns properly. I guess I’ll focus on those areas and see what I can find to clarify the status.
exec
/bin/zsh -lc "sed -n '1328,1345p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3088,3100p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1580,1595p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8096,8104p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \operatorname{hom}_\alpha(\cC^{\textup{!`}}_{\mathrm{ch}},
 \cP^{\mathrm{ch}})$ (convolution = master object;
 Theorem~\ref{thm:convolution-master-identification}).
\item $\Theta_\cA \in \mathrm{MC}(\operatorname{hom}_\alpha)
 \cong \mathrm{Tw}_\alpha$ (MC element = twisting morphism;
 Corollary~\ref{cor:theta-twisting-morphism}).
\item $\mathbb{G}_{\mathrm{pf}} =
 \mathrm{Trop}(\overline{\operatorname{FM}}_n(C|D))$
 (planted forests = tropicalization;
 Theorem~\ref{thm:planted-forest-tropicalization}).
\item $\barB(\cA)$ is a $\mathrm{Ch}_\infty$-algebra
 (Theorem~\ref{thm:cech-hca}).
\item $B_\kappa \dashv \Omega_\kappa$ is a Quillen equivalence
 (Theorem~\ref{thm:quillen-equivalence-chiral}).
\item The shadow algebra $\cA^{\mathrm{sh}}$ is a homotopy invariant
 (Theorem~\ref{thm:shadow-homotopy-invariance}).
\item The one-slot obstruction constrains the MC3 categorical lift:
 $\operatorname{hom}_\alpha$ accepts $\infty$-morphisms in either slot
 succeeded in 51ms:
invariant and isolated.

The monograph develops both axes: the oper package of
Chapter~\ref{chap:kac-moody} and the critical-level
Hochschild computation of
Theorem~\ref{thm:critical-level-cohomology} belong to
axis~1; the shadow obstruction tower, the genus expansion, and
Theorems~A--D belong to axis~2.
Theorem~H (chiral Hochschild) connects them: at generic level,
 succeeded in 51ms:

The RNW no-bifunctor obstruction \cite{RNW19}
(\S\ref{sec:concordance-three-pillars}, identification
theorem~7) is structural: $\operatorname{hom}_\alpha(
\mathcal{C},\mathcal{A})$ extends to $\infty$-morphisms in
either slot separately but not both. Koszulness does not kill
it; Koszulness makes it irrelevant by factoring all
constructions one slot at a time
(Theorem~\ref{thm:quillen-equivalence-chiral}). This is why
the MC3 strategy
(Theorem~\ref{thm:mc3-type-a-resolution}) succeeds.
\label{rem:concordance-bifunctor-koszul}

 succeeded in 51ms:
\smallskip
\renewcommand{\arraystretch}{1.25}
\noindent
\begin{tabular}{p{4.8cm}p{4.2cm}p{5.5cm}}
\textbf{Theorem in this manuscript}
 & \textbf{Result cited}
 & \textbf{Fallback if revised} \\
\hline
Thm~\ref{thm:quillen-equivalence-chiral}
 (bar-cobar Quillen equivalence)
 & \cite[Thm~2.1]{Val16}: model structure on
 homotopy algebras
 & Published; no preprint risk \\
Thm~\ref{thm:shadow-homotopy-invariance}
 (shadow homotopy invariance)
 & \cite[Thm~5.1]{RNW19}: $\infty$-morphisms


thinking
**Reviewing theorem statements**

I’m looking at line 1341, which only states "theorem" without further qualification. It seems okay, but maybe it needs a qualifier for Quillen equivalence since the theorem is "ProvedElsewhere." It depends on whether the status table aims to reflect this. I’ve noticed the status table D row lacks a citation for the multi-weight theorem. There's also a mismatch in labeling, like the line referring to `Proposition` when it should be a `Conjecture`. That’s definitely an oversight!
thinking
**Searching for mismatches**

I think I need to check for other instances where the text might inconsistently use "Proposition" or "Theorem" with references to a conjecture or remark. It might be helpful to look for prefix mismatches in the concordance, like using `Theorem\ref{conj:...}` or `Proposition\ref{conj:...}` when it should say "Conjecture." I'll script this search for the whole file to catch any errors. This could help ensure the accuracy of the references throughout the document!
codex
I found at least one true label/type drift inside the concordance: it calls `\ref{conj:koszul-t-structures}` a proposition even though the live source is a conjecture. I’m running a full label-prefix mismatch check over the concordance now so I can fix every local misclassification in one pass.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, json
from pathlib import Path
text=Path('chapters/connections/concordance.tex').read_text().splitlines()
claimmap={}
with open('metadata/claims.jsonl') as f:
    for line in f:
        obj=json.loads(line)
        claimmap[obj['label']]=obj['env_type']
patterns=[('Theorem', 'theorem'),('Proposition','proposition'),('Corollary','corollary'),('Lemma','lemma'),('Conjecture','conjecture'),('Remark','remark'),('Definition','definition'),('Computation','computation')]
for i,line in enumerate(text,1):
    for word,env in patterns:
        for lab in re.findall(rf'{word}~\\\\ref\\{{(["'^}}]+)'"\\}}', line):
            actual=claimmap.get(lab)
            if actual and actual"'!=env:
                print(f'"'{i}: {word}~\\\\ref{{{lab}}} -> actual {actual}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1933: Proposition~\ref{conj:mc3-automatic-generalization} -> actual conjecture
2508: Theorem~\ref{conj:lagrangian-koszulness} -> actual conjecture
3074: Proposition~\ref{conj:koszul-t-structures} -> actual conjecture
6482: Theorem~\ref{conj:dk-fd-typeA} -> actual conjecture
6855: Theorem~\ref{prop:hc-dictionary} -> actual proposition

thinking
**Inspecting theorem context**

I need to check the context more closely and make corrections. It looks like there's a mismatch because the term "theorem" is being used to reference a "proposition." This could be intentional due to how the theorem statement is set up in the table. Hmm, it’s important to inspect these lines to clarify what's intended. Let's take a closer look and resolve any inconsistencies!
exec
/bin/zsh -lc "sed -n '1928,1936p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2504,2512p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6478,6484p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3070,3078p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6848,6857p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
\item\label{item:kp-lagrangian}
 Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
 (Theorem~\ref{conj:lagrangian-koszulness}).
 PTVV derived intersection. Perfectness verified for the standard
 landscape (Proposition~\ref{prop:lagrangian-perfectness},
 Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
 non-critical, non-degenerate levels.
 succeeded in 52ms:
The downstream DK-4/5 extension (from evaluation-generated core
to compact-completion of full category) remains open.
Conditionally, the remaining packages~(ii)--(iv) are
type-independent once the relevant shifted-prefundamental,
pro-Weyl, and compact-completion inputs are supplied in that
type (Proposition~\ref{conj:mc3-automatic-generalization}).
\end{construction}

\item \emph{MC4}: The formal completion theory is \textbf{proved} by
 succeeded in 51ms:
 The evaluation-locus theorem is proved, but the module-category
 promotion beyond generators now splits into two distinct issues:
 \emph{thick generation} and an \emph{ambient
 extension/comparison package}. On the Yangian module surface,
 Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
 are only conditional thick-generation extension criteria: once one
 constructs an ambient exact/lax monoidal extension of the
 succeeded in 50ms:
\end{itemize}

\smallskip\noindent\textbf{Categorical.}
\begin{itemize}[nosep]
\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
\item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
\item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
\item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
\item \emph{Scalar-orbit convolution formality}: for uniform-weight algebras, the distinguished scalar Maurer--Cartan orbit in $\mathfrak{g}_\cA^{\mathrm{mod}}$ is formal; converse and one-channel generalizations remain open.
 succeeded in 50ms:
\item Theorem~\ref{thm:hc-symplectic-code}:
 symplectic code structure from Lagrangian isotropy.
\item Proposition~\ref{prop:hc-knill-laflamme}:
 Verdier isotropy and Shapovalov cross-pairing.
\item Theorem~\ref{thm:hc-shadow-redundancy}:
 shadow depth $=$ redundancy channels
 (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
\item Theorem~\ref{prop:hc-dictionary}:
 12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
\end{enumerate}
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
text=Path('chapters/connections/concordance.tex').read_text().splitlines()
checks=[('Theorem','prop:'),('Theorem','cor:'),('Theorem','lem:'),('Theorem','conj:'),('Theorem','rem:'),('Theorem','def:'),('Theorem','comp:'),
        ('Proposition','thm:'),('Proposition','cor:'),('Proposition','lem:'),('Proposition','conj:'),('Proposition','rem:'),('Proposition','def:'),('Proposition','comp:'),
        ('Corollary','thm:'),('Corollary','prop:'),('Corollary','lem:'),('Corollary','conj:'),('Corollary','rem:'),('Corollary','def:'),('Corollary','comp:'),
        ('Lemma','thm:'),('Lemma','prop:'),('Lemma','cor:'),('Lemma','conj:'),('Lemma','rem:'),('Lemma','def:'),('Lemma','comp:'),
        ('Conjecture','thm:'),('Conjecture','prop:'),('Conjecture','cor:'),('Conjecture','lem:'),('Conjecture','rem:'),('Conjecture','def:'),('Conjecture','comp:'),
        ('Remark','thm:'),('Remark','prop:'),('Remark','cor:'),('Remark','lem:'),('Remark','conj:'),('Remark','def:'),('Remark','comp:'),
        ('Definition','thm:'),('Definition','prop:'),('Definition','cor:'),('Definition','lem:'),('Definition','conj:'),('Definition','rem:'),('Definition','comp:'),
        ('Computation','thm:'),('Computation','prop:'),('Computation','cor:'),('Computation','lem:'),('Computation','conj:'),('Computation','rem:'),('Computation','def:')]
for i,line in enumerate(text,1):
    for word,prefix in checks:
        if re.search(rf'{word}~\\\\ref\\{{{re.escape(prefix)}["'^}}]+'"\\}}', line):
            print(f'{i}: {line.strip()}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 226ms:
1933: type (Proposition~\ref{conj:mc3-automatic-generalization}).
2508: (Theorem~\ref{conj:lagrangian-koszulness}).
2738: order (Proposition~\ref{thm:shadow-gf-borel}).
3074: \item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
6482: Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
6855: \item Theorem~\ref{prop:hc-dictionary}:
8721: (Theorem~\ref{cor:ramanujan-deligne-free}):
exec
/bin/zsh -lc "sed -n '8717,8723p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2734,2741p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import json
labs=['thm:shadow-gf-borel','cor:ramanujan-deligne-free','prop:hc-dictionary']
claimmap={}
with open('metadata/claims.jsonl') as f:
    for line in f:
        obj=json.loads(line); claimmap[obj['label']]=obj
for lab in labs:
    print(lab, claimmap.get(lab))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
For lattice VOAs: $d_{\mathrm{alg}} = 0$; for Virasoro
minimal models: $d_{\mathrm{arith}}$ finite,
$d_{\mathrm{alg}} = \infty$. The Borel sum of the
Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
order (Proposition~\ref{thm:shadow-gf-borel}).

\smallskip\noindent\textbf{Shadow growth rate}
(Definition~\ref{def:shadow-growth-rate},
 succeeded in 50ms:
DS reduction $=$ motivic truncation.

\smallskip\noindent
\textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
(Theorem~\ref{cor:ramanujan-deligne-free}):
twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
No $\ell$-adic cohomology.
 succeeded in 51ms:
thm:shadow-gf-borel None
cor:ramanujan-deligne-free None
prop:hc-dictionary {'label': 'prop:hc-dictionary', 'env_type': 'proposition', 'status': 'ProvedHere', 'file': 'chapters/connections/holographic_codes_koszul.tex', 'line': 561, 'title': '12-fold dictionary', 'refs_in_block': ['thm:koszul-equivalences-meta']}

thinking
**Searching for labels in claims**

I suspect some labels might not be in claims.jsonl because the theorem isn't tagged properly. I think I need to use rg directly to search for environmental-related labels. This could help identify what’s missing and ensure everything is correctly tagged. It's an organized way to approach the issue and should lead to better clarity in what I'm looking for. Let's see what I can find with that search!
exec
/bin/zsh -lc "rg -n \"label\\{thm:shadow-gf-borel\\}|label\\{cor:ramanujan-deligne-free\\}\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8718,8726p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2728,2740p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\smallskip\noindent
\textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
(Theorem~\ref{cor:ramanujan-deligne-free}):
twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
No $\ell$-adic cohomology.

\smallskip\noindent
\textbf{(11)~Ramanujan bound for rational VOAs}
 succeeded in 52ms:
chapters/connections/arithmetic_shadows.tex:2122:\label{thm:shadow-gf-borel}
chapters/connections/arithmetic_shadows.tex:8704:\label{cor:ramanujan-deligne-free}%
 succeeded in 52ms:
The depth decomposition
(Theorem~\ref{thm:depth-decomposition}):
$d(\cA) = 1 + d_{\mathrm{arith}} + d_{\mathrm{alg}}$,
where $d_{\mathrm{arith}}$ counts holomorphic Hecke eigenforms
(determines critical lines) and $d_{\mathrm{alg}}$ measures
non-holomorphic OPE complexity (invisible to $L$-functions).
For lattice VOAs: $d_{\mathrm{alg}} = 0$; for Virasoro
minimal models: $d_{\mathrm{arith}}$ finite,
$d_{\mathrm{alg}} = \infty$. The Borel sum of the
Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
order (Proposition~\ref{thm:shadow-gf-borel}).

\smallskip\noindent\textbf{Shadow growth rate}
exec
/bin/zsh -lc "sed -n '2108,2130p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8694,8710p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
can degenerate only in the non-unitary regime. The shadow
resonance locus is thus confined to $c < 0$.
\end{remark}

% ============================================================
\subsection{Stieltjes representation}
\label{sec:shadow-complex-structure}

The shadow generating function
$G(t) = \sum_{r\ge2} S_r\,t^r$
has a canonical integral representation.

\begin{theorem}[Shadow spectral measure]
\label{thm:shadow-spectral-measure}
\label{thm:shadow-gf-borel}
\ClaimStatusProvedHere
The shadow generating function is a Stieltjes transform:
\begin{equation}\label{eq:stieltjes-representation}
 G(t) \;=\; \int_{\bR} \log\!\bigl(1 - \lambda\,t\bigr)\,d\rho(\lambda),
 \qquad
 succeeded in 51ms:
Newton's identity~\eqref{eq:newton-at-prime} at each prime
for each eigenform.

\emph{(iii)} Immediate from~(ii): the power sums
$p_r(\alpha_{j,p}, \beta_{j,p})$ are the $p$-local shadows,
and they factor prime-by-prime by construction.
\end{proof}

\begin{corollary}[Unconditional operadic RS for lattice VOAs]%
\label{cor:unconditional-lattice}%
\label{cor:ramanujan-deligne-free}%
\ClaimStatusProvedHere%
\index{operadic Rankin--Selberg theorem!unconditional for lattices}%
\index{Ramanujan bound!Deligne-free proof}%
\index{Ramanujan bound!new proof for lattice VOAs}%
For lattice VOAs: the MC equation
$\Rightarrow$ prime-locality



thinking
**Fixing reference wording**

I need to adjust the reference wording for theorem and corollary labels. It seems like searching for additional prefix mismatches using label_index could be helpful. The current regex has already found six. However, some mismatches may exist where the label prefix doesn’t match the environment but matches the alias, like thm:shadow-gf-borel being an actual theorem. I also notice that "Proposition" should be replaced with "Theorem." There might be other mismatches to check, but they aren't as critical.
thinking
**Validating label changes**

I’m considering how to reference Vol II labels, but they might not be included in the metadata, even though many are in the current repository. I could run a local build or use grep after making edits. It seems I need targeted grep for forbidden patterns during the user verification loop. For line 6482, Theorem\ref{conj:dk-fd-typeA} should actually be "Conjecture." Several other terms need fixing too, like changing Proposition\ref{conj:mc3-automatic-generalization} to Conjecture. I should make similar adjustments throughout the document.
thinking
**Analyzing environment mismatches**

I’m thinking there might be more mismatches because of aliases that aren’t captured in the metadata. I could build a rough environment map by parsing all text labels and linking them to the nearest previous environment using a script. Then, I could scan the file for any mismatches between words and environments across all labels. This might be useful to be thorough. I'll write a quick Python parser to scan all .tex files and record label-environment associations.
codex
The local label-type drift is broader than the headline status issues. I’m doing one more exhaustive pass using the actual `.tex` environments, not just the metadata claims, so I don’t miss alias labels or untagged theorem surfaces.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=list(Path('chapters').rglob('*.tex'))+list(Path('appendices').rglob('*.tex'))+[Path('CLAUDE.md')]
# only tex files for env parsing
tex_files=[p for p in tex_files if p.suffix=='.tex']
env_stack=[]
label_env={}
begin_re=re.compile(r'\\\\begin\\{([A-Za-z*]+)\\}')
end_re=re.compile(r'\\\\end\\{([A-Za-z*]+)\\}')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
claim_envs={'theorem','proposition','corollary','lemma','conjecture','remark','definition','computation','calculation','maintheorem','verification'}
for path in tex_files:
    stack=[]
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        for m in begin_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                stack.append((env,lineno))
        for m in label_re.finditer(line):
            lab=m.group(1)
            if stack:
                label_env.setdefault(lab,stack[-1][0])
        for m in end_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                # pop last matching env
                for idx in range(len(stack)-1,-1,-1):
                    if stack[idx][0]==env:
                        stack.pop(idx)
                        break

text=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns=[('Theorem', 'theorem'),('Proposition','proposition'),('Corollary','corollary'),('Lemma','lemma'),('Conjecture','conjecture'),('Remark','remark'),('Definition','definition'),('Computation','computation')]
for i,line in enumerate(text,1):
    for word,env in patterns:
        for lab in re.findall(rf'{word}~\\\\ref\\{{(["'^}}]+)'"\\}}', line):
            actual=label_env.get(lab)
            if actual and actual"'!=env:
                print(f'"'{i}: {word}~\\\\ref{{{lab}}} -> actual {actual}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 197ms:
1933: Proposition~\ref{conj:mc3-automatic-generalization} -> actual conjecture
2508: Theorem~\ref{conj:lagrangian-koszulness} -> actual conjecture
2738: Proposition~\ref{thm:shadow-gf-borel} -> actual theorem
3074: Proposition~\ref{conj:koszul-t-structures} -> actual conjecture
6482: Theorem~\ref{conj:dk-fd-typeA} -> actual conjecture
6855: Theorem~\ref{prop:hc-dictionary} -> actual proposition
8721: Theorem~\ref{cor:ramanujan-deligne-free} -> actual corollary




thinking
**Identifying potential mismatches**

I see several mismatches that need attention, especially regarding the status mismatch tables. I might want to audit occurrences of "proved" near Conjecture or Conditional labels for contradictions. There's a specific line that looks okay, but I could check for comments or TODOs, particularly a potential missing citation of the multi-weight theorem. It's a good point to inspect if the summary tables align with the actual theorem statuses for completeness, but it's not urgent. I should verify against current sources.
thinking
**Examining theorem statuses**

I'm considering using non-proved labels like `conj:dk-fd-typeA` and `thm:rtt-mittag-leffler`. The statuses indicate some are proved, while others remain open, which seems fine for now. I could check the concordance table against actual claims for any discrepancies, particularly in the status macros. Extracting rows with references and statuses might be challenging. Additionally, I should inspect the source status of `Theorem\ref{quillen-equivalence-chiral}` and consider if any contributions need qualification. The question of mismatches around certain contributions is lingering but seems okay. I’ll keep an eye out for potential stale entries as noted in a TODO.
thinking
**Rethinking contributions and context**

I’m wondering if it’s acceptable for a contribution to adapt to a chiral context. The theorem references Vallette, which suggests there’s proof available elsewhere. But then I start to question the originality of the manuscript theorem itself. Is it really contributing something novel, or is it just reworking existing ideas? Hm, I really need to untangle this. It’s interesting to analyze how originality plays into academic contributions.
thinking
**Examining proofs in literature**

I’m thinking about the mention of "Proved Elsewhere" claims in literature. It might be worth searching for references preceded by "Proved" to check if they're misleading. I can write a script to find those lines with the label and "proved" nearby, but there could be too many to handle. Still, some references might genuinely say "proved elsewhere" or attribute proofs to someone, like Ayala-Francis. I should script around this to explore it further.
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
text=Path('chapters/connections/concordance.tex').read_text().splitlines()
claimmap={}
with open('metadata/claims.jsonl') as f:
    for line in f:
        obj=json.loads(line); claimmap[obj['label']]=obj
for i,line in enumerate(text,1):
    labs=re.findall(r'\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}', line)
    for lab in labs:
        obj=claimmap.get(lab)
        if obj and obj['status']=='ProvedElsewhere' and re.search(r'\\bproved\\b|\\bProved\\b', line):
            print(f'{i}: {lab} -> {line.strip()}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

Plan update
Concordance audit narrowed to concrete local drift: label-type mismatches, a stale status-sync TODO, and one scope/support gap in the main theorem summary table. I’m applying only those surgical fixes, then I’ll rerun the mismatch/forbidden-pattern checks on the modified file.
  ✓ Audit concordance theorem/status surface against live source and isolate concrete drift
  → Patch only the stale concordance entries in chapters/connections/concordance.tex
  • Re-read patched contexts and rerun targeted validation checks
codex
I have the patch set scoped. It’s small: fix the seven theorem/proposition/corollary misreferences, remove the stale `% TODO(status-sync)` residue, and tighten the Theorem D summary row so the multi-weight scope change is explicitly anchored to the live theorem that proves it.
exec
/bin/zsh -lc "sed -n '30,80p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '58,68p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
& \textbf{Theorem} & \textbf{Statement} & \textbf{Status} \\
\hline
\textbf{A} & Bar-cobar adjunction
 & $\barBch \dashv \Omegach$ on $\Ran(X)$,
 with the algebra-level Verdier half only after
 $\mathbb{D}_{\Ran}$:
 $\mathbb{D}_{\Ran}\barB_X(\cA_i)\simeq \Omega_X(\cC_j)\simeq \cA_j$,
 \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
 & \ClaimStatusProvedHere \\
\textbf{B} & Bar-cobar inversion
 & Strict quasi-isomorphism on the Koszul locus
 $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
 \textup{(}Thms~\ref{thm:higher-genus-inversion},
 \ref{thm:bar-cobar-inversion-qi}\textup{)}; off the locus,
 the counit is an unconditional coderived coacyclic-equivalence,
 promoted back to an ordinary quasi-isomorphism on collapse loci
 & \ClaimStatusProvedHere \\
\textbf{C} & Complementarity
 & C0: coderived fiber-center identification unconditional,
 ordinary-derived only on the flat perfect locus
 succeeded in 51ms:
 & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
\textbf{D} & Modular characteristic
 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
 on the proved uniform-weight lane at all genera
 \textup{(}Definition~\ref{def:scalar-lane},
 Thm~\ref{thm:modular-characteristic}\textup{)};
 genus~$1$ is universal for all families;
 multi-weight $g \geq 2$ acquires the cross-channel term
 $\delta F_g^{\mathrm{cross}}$; the routing
 $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
 & \ClaimStatusProvedHere \\
codex
```text
genus: all with explicit split (uniform-weight all genera; genus-1 universal; multi-weight g>=2 correction)
degree: all
AP32 weight tag: NA in theorem-summary table; live theorem source already carries lane split
AP139 free-var audit: LHS vars:{g,\cA} RHS vars:{g,\cA} LHS⊇RHS? Y
AP36: implies/iff = implies only; no converse inflation
verdict: ACCEPT
```

thinking
**Investigating patch issues**

It looks like the patch might have failed due to some slight differences in the text, specifically around two lines and a proof line. I need to inspect the exact lines around line 6118 to understand what's going wrong. It's important to pinpoint the issue accurately to fix the problem effectively. I’ll make sure to take a closer look and ensure everything aligns as it should. Let's figure this out!
codex
The patch hit one context mismatch around the old TODO block. I’m re-reading the exact local lines and then applying the same edits with tighter hunks only.
exec
/bin/zsh -lc "sed -n '6116,6128p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1929,1935p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2498,2510p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6479,6484p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\Longrightarrow
\text{Theorem~\ref{thm:family-index}}.
\]
Thus Theorem~\ref{thm:family-index} is a downstream
Grothendieck--Riemann--Roch repackaging of the scalar genus series,
and it is not an input to Theorem~\ref{thm:genus-universality}.
% TODO(status-sync): After the remaining rectification passes land,
% sync this concordance surface with any theorem-status downgrades,
% scope narrowings, or inserted missing lemmas.

The proof assembles four ingredients, each established
independently.

 succeeded in 51ms:
to compact-completion of full category) remains open.
Conditionally, the remaining packages~(ii)--(iv) are
type-independent once the relevant shifted-prefundamental,
pro-Weyl, and compact-completion inputs are supplied in that
type (Proposition~\ref{conj:mc3-automatic-generalization}).
\end{construction}

 succeeded in 50ms:
 Stratum-by-stratum PBW; binary collision forces injectivity.
 \hfill \checkmark
\end{enumerate}

\medskip\noindent
\textbf{Conditional/partial in general; (xi) unconditional for standard landscape} (xi)--(xii):

\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
\item\label{item:kp-lagrangian}
 Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
 (Theorem~\ref{conj:lagrangian-koszulness}).
 PTVV derived intersection. Perfectness verified for the standard
 landscape (Proposition~\ref{prop:lagrangian-perfectness},
 succeeded in 51ms:
 promotion beyond generators now splits into two distinct issues:
 \emph{thick generation} and an \emph{ambient
 extension/comparison package}. On the Yangian module surface,
 Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
 are only conditional thick-generation extension criteria: once one
 constructs an ambient exact/lax monoidal extension of the

thinking
**Evaluating patch application issues**

I'm considering whether there's a spacing issue causing the failure. It seems like it might be a match problem due to preceding lines being changed. That's unclear to me. I could create a separate patch just for the TODO later. Since the failure is due to one hunk, maybe I should try applying it without the last hunk and then handle it separately. That seems like a sensible plan!
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -65,3 +65,5 @@
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
@@ -1932,3 +1934,3 @@
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
@@ -2507,3 +2509,3 @@
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
@@ -2737,3 +2739,3 @@
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
@@ -3073,3 +3075,3 @@
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
@@ -6481,3 +6483,3 @@
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
@@ -6854,3 +6856,3 @@
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
@@ -8720,3 +8722,3 @@
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..451e049bf464202b14d67cc500dfd80e603a5339
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6479,7 +6481,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6854,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8720,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..451e049bf464202b14d67cc500dfd80e603a5339
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6479,7 +6481,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6854,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8720,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -6123,5 +6123,2 @@
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
apply_patch(auto_approved=true) exited 0 in 22ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 



thinking
**Addressing forbidden patterns**

I need to review the modified lines and might run a re-read. It could be good to use parallel tool calls here. I should run a mismatch script again to catch any forbidden patterns in the modified file. The user specifically asked to grep for forbidden patterns after editing, focusing on the modified file. So, I should look for `TODO`, em-dash, and any relevant blacklisted formulas, ensuring I only check patterns after those edits.
thinking
**Verifying edits for forbidden patterns**

I need to confirm using grep for any forbidden patterns in the modified files, particularly focusing on label-type mismatches and `TODO`. Since the user asked for a verification loop after edits, I should also consider searching for banned prose elements like em-dash and backticks. There's a chance that maybe checking `\Omega/z` isn’t necessary since it’s unrelated to our changes. In addition, running a generic blacklist grep from AGENTS will help, so I’ll search for relevant terms in the modified file.
codex
The edits are in. I’m re-reading each patched context and rerunning the exact mismatch scan plus a forbidden-pattern grep on `chapters/connections/concordance.tex` to make sure the constitutional surface is now clean.
exec
/bin/zsh -lc "sed -n '58,68p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
\textbf{D} & Modular characteristic
 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
 on the proved uniform-weight lane at all genera
 \textup{(}Definition~\ref{def:scalar-lane},
 Thm~\ref{thm:modular-characteristic}\textup{)};
 genus~$1$ is universal for all families;
 multi-weight $g \geq 2$ acquires the cross-channel term
 $\delta F_g^{\mathrm{cross}}$
 \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
 the routing
exec
/bin/zsh -lc "sed -n '1929,1935p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(Corollary~\ref{cor:dk2-thick-generation-all-types}).
The downstream DK-4/5 extension (from evaluation-generated core
to compact-completion of full category) remains open.
Conditionally, the remaining packages~(ii)--(iv) are
type-independent once the relevant shifted-prefundamental,
pro-Weyl, and compact-completion inputs are supplied in that
type (Conjecture~\ref{conj:mc3-automatic-generalization}).
exec
/bin/zsh -lc "sed -n '2498,2510p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 FM boundary acyclicity: $H^k(i_S^!\,\barBgeom_n(\cA)) = 0$ for $k \neq 0$, all strata~$S$
 (Theorem~\ref{thm:fm-boundary-acyclicity}).
 Stratum-by-stratum PBW; binary collision forces injectivity.
 \hfill \checkmark
\end{enumerate}

\medskip\noindent
\textbf{Conditional/partial in general; (xi) unconditional for standard landscape} (xi)--(xii):

\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
\item\label{item:kp-lagrangian}
 Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
 (Conjecture~\ref{conj:lagrangian-koszulness}).
exec
/bin/zsh -lc "sed -n '2734,2741p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(determines critical lines) and $d_{\mathrm{alg}}$ measures
non-holomorphic OPE complexity (invisible to $L$-functions).
For lattice VOAs: $d_{\mathrm{alg}} = 0$; for Virasoro
minimal models: $d_{\mathrm{arith}}$ finite,
$d_{\mathrm{alg}} = \infty$. The Borel sum of the
Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
order (Theorem~\ref{thm:shadow-gf-borel}).

exec
/bin/zsh -lc "sed -n '3070,3078p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{$C_2$-cofiniteness}: orthogonal to Koszulness; Koszul duality maps $C_2$-cofinite to non-$C_2$-cofinite.
\item \emph{Critical level}: $V_{-h^\vee}(\fg)$ is uncurved ($\kappa=0$), self-dual under the Feigin--Frenkel involution ($k=-h^\vee$ is a fixed point of $k \mapsto -k-2h^\vee$), center~$= \mathfrak{z}(\widehat{\fg})$ (Theorem~\ref{thm:critical-level-cohomology}).
\end{itemize}

\smallskip\noindent\textbf{Categorical.}
\begin{itemize}[nosep]
\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
\item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
\item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
exec
/bin/zsh -lc "sed -n '6116,6128p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6479,6484p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\Longrightarrow
\text{Theorem~\ref{thm:genus-universality}}
\Longrightarrow
\text{Theorem~\ref{thm:family-index}}.
\]
Thus Theorem~\ref{thm:family-index} is a downstream
Grothendieck--Riemann--Roch repackaging of the scalar genus series,
and it is not an input to Theorem~\ref{thm:genus-universality}.

The proof assembles four ingredients, each established
independently.

\emph{Step~1: Construction of $\mathcal{D}_{\cA}^{(g)}$.}
exec
/bin/zsh -lc "sed -n '6848,6857p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \emph{thick generation} and an \emph{ambient
 extension/comparison package}. On the Yangian module surface,
 Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
 are only conditional thick-generation extension criteria: once one
 constructs an ambient exact/lax monoidal extension of the
 evaluation-level bar-comodule comparison, together with the required
exec
/bin/zsh -lc "sed -n '8718,8726p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 symplectic code structure from Lagrangian isotropy.
\item Proposition~\ref{prop:hc-knill-laflamme}:
 Verdier isotropy and Shapovalov cross-pairing.
\item Theorem~\ref{thm:hc-shadow-redundancy}:
 shadow depth $=$ redundancy channels
 (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
\item Proposition~\ref{prop:hc-dictionary}:
 12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
\end{enumerate}
Status: \textbf{all proved}.
 succeeded in 51ms:
\smallskip\noindent
\textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
(Corollary~\ref{cor:ramanujan-deligne-free}):
twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
No $\ell$-adic cohomology.

\smallskip\noindent
\textbf{(11)~Ramanujan bound for rational VOAs}
(Theorem~\ref{thm:non-lattice-ramanujan}):
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

exec
/bin/zsh -lc "rg -n \"TODO|Theorem~\\\\ref\\{conj:|Proposition~\\\\ref\\{conj:|Theorem~\\\\ref\\{prop:|Proposition~\\\\ref\\{thm:|Theorem~\\\\ref\\{cor:|---|—|"'`" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: unmatched "
 succeeded in 51ms:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debe..dd9f823 100644
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@ Their proved core and conditional refinements are recorded explicitly below.
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -715,14 +717,15 @@ The precise comparison:
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=list(Path('chapters').rglob('*.tex'))+list(Path('appendices').rglob('*.tex'))
claim_envs={'theorem','proposition','corollary','lemma','conjecture','remark','definition','computation','calculation','maintheorem','verification'}
label_env={}
begin_re=re.compile(r'\\\\begin\\{([A-Za-z*]+)\\}')
end_re=re.compile(r'\\\\end\\{([A-Za-z*]+)\\}')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
for path in tex_files:
    stack=[]
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        for m in begin_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                stack.append((env,lineno))
        for m in label_re.finditer(line):
            lab=m.group(1)
            if stack:
                label_env.setdefault(lab,stack[-1][0])
        for m in end_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                for idx in range(len(stack)-1,-1,-1):
                    if stack[idx][0]==env:
                        stack.pop(idx)
                        break
text=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns=[('Theorem', 'theorem'),('Proposition','proposition'),('Corollary','corollary'),('Lemma','lemma'),('Conjecture','conjecture'),('Remark','remark'),('Definition','definition'),('Computation','computation')]
problems=[]
for i,line in enumerate(text,1):
    for word,env in patterns:
        for lab in re.findall(rf'{word}~\\\\ref\\{{(["'^}}]+)'"\\}}', line):
            actual=label_env.get(lab)
            if actual and actual"'!=env:
                problems.append((i,word,lab,actual))
if problems:
    for p in problems:
        print(*p)
    raise SystemExit(1)
print('"'label-type mismatch scan: clean')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 167ms:
label-type mismatch scan: clean
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

codex
The environment-type scan came back clean. I still need one final forbidden-pattern grep; the shell quoting on the first pass was bad, so I’m rerunning it with a safer check now.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
text=Path('chapters/connections/concordance.tex').read_text()
patterns={
    'todo': r'TODO',
    'theorem_ref_conj': r'Theorem~\\\\ref\\{conj:',
    'proposition_ref_conj': r'Proposition~\\\\ref\\{conj:',
    'theorem_ref_prop': r'Theorem~\\\\ref\\{prop:',
    'proposition_ref_thm': r'Proposition~\\\\ref\\{thm:',
    'theorem_ref_cor': r'Theorem~\\\\ref\\{cor:',
    'emdash': r'—',
    'triple_hyphen': r'---',
}
found=[]
for name,pat in patterns.items():
    for m in re.finditer(pat,text):
        line=text.count('\\n',0,m.start())+1
        found.append((line,name,m.group(0)))
if found:
    for line,name,match in found:
        print(f'{line}: {name}: {match}')
    raise SystemExit(1)
print('forbidden-pattern grep: clean')
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
2417: triple_hyphen: ---
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

codex
The forbidden-pattern grep did its job: the file still contains pre-existing triple-hyphen separators elsewhere in the concordance, outside the stale-status surface I was assigned to fix. I’m checking one sample to confirm they’re unrelated, then I’ll close with the exact fixed vs blocked list.
exec
/bin/zsh -lc "sed -n '2412,2419p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
not characterize it intrinsically. This section is the
constitutional index for the intrinsic characterization
programme. Full statements and proofs live in the source
chapters cited below.

%% ------------------------------------------------------------------
\subsection{The meta-theorem: twelve characterizations}
\label{subsec:concordance-koszulness-meta-theorem}
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 


thinking
**Evaluating comment separators**

I notice some preexisting comment separators that might need addressing. They’re not completely blocked, but they could create unrelated formatting issues. I wonder if the user expected completeness regarding each finding listed since we have so many findings to consider. Maybe the triple-hyphen comments should be viewed as stale or out-of-scope since they arose during the audit process. I need to figure out if we should fix them or remove the lengthy comment separators throughout the file. There are many!
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
lines=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns={
    'todo': r'TODO',
    'theorem_ref_conj': r'Theorem~\\\\ref\\{conj:',
    'proposition_ref_conj': r'Proposition~\\\\ref\\{conj:',
    'theorem_ref_prop': r'Theorem~\\\\ref\\{prop:',
    'proposition_ref_thm': r'Proposition~\\\\ref\\{thm:',
    'theorem_ref_cor': r'Theorem~\\\\ref\\{cor:',
    'emdash': r'—',
    'triple_hyphen_noncomment': r'(?<"'!%)---'"',
}
found=[]
for lineno,line in enumerate(lines,1):
    for name,pat in patterns.items():
        if re.search(pat,line):
            found.append((lineno,name,line))
if found:
    for lineno,name,line in found[:20]:
        print(f'{lineno}: {name}: {line}')
    raise SystemExit(1)
print('targeted forbidden-pattern grep: clean')
PY" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
2417: triple_hyphen_noncomment: %% ------------------------------------------------------------------
2522: triple_hyphen_noncomment: %% ------------------------------------------------------------------
2568: triple_hyphen_noncomment: %% ------------------------------------------------------------------
2641: triple_hyphen_noncomment: %% ------------------------------------------------------------------
3050: triple_hyphen_noncomment: %% ------------------------------------------------------------------
3085: triple_hyphen_noncomment: %% ------------------------------------------------------------------
3104: triple_hyphen_noncomment: %% ------------------------------------------------------------------
3179: triple_hyphen_noncomment: %% ------------------------------------------------------------------
9668: triple_hyphen_noncomment: % ----------------------------------------------------------------------
9900: triple_hyphen_noncomment: % ----------------------------------------------------------------------
9905: triple_hyphen_noncomment: % ----------------------------------------------------------------------
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 


thinking
**Rethinking regex approach**

I'm noticing that my regex `(?<!%)---` is still matching, possibly due to the second `%`. Hmm, I might just ignore comment lines altogether. If a line starts with '%' after stripping whitespace, then I can skip the triple hyphen check. It seems like a logical fix! Now, I just need to rerun the regex after making this adjustment. Let’s see if that solves the issue!
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
lines=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns={
    'todo': r'TODO',
    'theorem_ref_conj': r'Theorem~\\\\ref\\{conj:',
    'proposition_ref_conj': r'Proposition~\\\\ref\\{conj:',
    'theorem_ref_prop': r'Theorem~\\\\ref\\{prop:',
    'proposition_ref_thm': r'Proposition~\\\\ref\\{thm:',
    'theorem_ref_cor': r'Theorem~\\\\ref\\{cor:',
    'emdash': r'—',
}
found=[]
for lineno,line in enumerate(lines,1):
    for name,pat in patterns.items():
        if re.search(pat,line):
            found.append((lineno,name,line))
    if not line.lstrip().startswith('%') and '---' in line:
        found.append((lineno,'triple_hyphen_noncomment',line))
if found:
    for lineno,name,line in found[:20]:
        print(f'{lineno}: {name}: {line}')
    raise SystemExit(1)
print('targeted forbidden-pattern grep: clean')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
targeted forbidden-pattern grep: clean
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

Plan update
The concordance patch is in place. I re-read every modified hunk, reran the full label-type mismatch scan against live theorem environments, and ran a targeted forbidden-pattern grep on the modified file.
  ✓ Audit concordance theorem/status surface against live source and isolate concrete drift
  ✓ Patch only the stale concordance entries in chapters/connections/concordance.tex
  ✓ Re-read patched contexts and rerun targeted validation checks
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 


thinking
**Gathering findings on edits**

I need to gather specific findings from our audit. First, I found that the D row lacked a source anchor for the multi-weight theorem. There are also seven mismatches in the environment and labels, plus a stale TODO comment. It seems broader audits didn’t reveal any further local status or type drift in modified areas, but I could mention that grep surfaced some pre-existing comment separators. 

It might be useful to run `git diff --word-diff`, but this isn't necessary right now. I'll need to include line references from our files, so I want to get line numbers for the edits, possibly grouped and formatted with `nl -ba`.
codex
I’m collecting the exact line numbers for the repaired concordance entries now so the closeout can point to the constitutional surface directly, not just describe it abstractly.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6478,6483p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6850,6856p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '2735,2740p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '8718,8723p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6120,6126p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1930,1935p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '60,68p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3072,3076p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '2506,2511p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6850	 Verdier isotropy and Shapovalov cross-pairing.
  6851	\item Theorem~\ref{thm:hc-shadow-redundancy}:
  6852	 shadow depth $=$ redundancy channels
  6853	 (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
  6854	\item Proposition~\ref{prop:hc-dictionary}:
  6855	 12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
  6856	\end{enumerate}
 succeeded in 51ms:
  2735	non-holomorphic OPE complexity (invisible to $L$-functions).
  2736	For lattice VOAs: $d_{\mathrm{alg}} = 0$; for Virasoro
  2737	minimal models: $d_{\mathrm{arith}}$ finite,
  2738	$d_{\mathrm{alg}} = \infty$. The Borel sum of the
  2739	Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
  2740	order (Theorem~\ref{thm:shadow-gf-borel}).
 succeeded in 51ms:
  6478	 promotion beyond generators now splits into two distinct issues:
  6479	 \emph{thick generation} and an \emph{ambient
  6480	 extension/comparison package}. On the Yangian module surface,
  6481	 Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  6482	 are only conditional thick-generation extension criteria: once one
  6483	 constructs an ambient exact/lax monoidal extension of the
 succeeded in 51ms:
  3072	\end{itemize}
  3073	
  3074	\smallskip\noindent\textbf{Categorical.}
  3075	\begin{itemize}[nosep]
  3076	\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 succeeded in 51ms:
  1930	The downstream DK-4/5 extension (from evaluation-generated core
  1931	to compact-completion of full category) remains open.
  1932	Conditionally, the remaining packages~(ii)--(iv) are
  1933	type-independent once the relevant shifted-prefundamental,
  1934	pro-Weyl, and compact-completion inputs are supplied in that
  1935	type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 succeeded in 51ms:
  8718	\smallskip\noindent
  8719	\textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
  8720	(Corollary~\ref{cor:ramanujan-deligne-free}):
  8721	twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
  8722	No $\ell$-adic cohomology.
  8723	
 succeeded in 51ms:
    60	 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
    61	 on the proved uniform-weight lane at all genera
    62	 \textup{(}Definition~\ref{def:scalar-lane},
    63	 Thm~\ref{thm:modular-characteristic}\textup{)};
    64	 genus~$1$ is universal for all families;
    65	 multi-weight $g \geq 2$ acquires the cross-channel term
    66	 $\delta F_g^{\mathrm{cross}}$
    67	 \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
    68	 the routing
 succeeded in 51ms:
  2506	
  2507	\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
  2508	\item\label{item:kp-lagrangian}
  2509	 Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
  2510	 (Conjecture~\ref{conj:lagrangian-koszulness}).
  2511	 PTVV derived intersection. Perfectness verified for the standard
 succeeded in 51ms:
  6120	\]
  6121	Thus Theorem~\ref{thm:family-index} is a downstream
  6122	Grothendieck--Riemann--Roch repackaging of the scalar genus series,
  6123	and it is not an input to Theorem~\ref{thm:genus-universality}.
  6124	
  6125	The proof assembles four ingredients, each established
  6126	independently.
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 






thinking
**Reviewing line changes**

I need to consider adding a line for the D row and maybe for line 2738. There were seven changes, so I should group by line numbers. I also need to look into line 1935. While we could mention more fixes from the worktree diff, I see that our patch didn't change those due to a pre-existing dirty file. It’s best not to list any unintended modifications in our final answer, just focus on the targeted fixes. I'll also mention that the validation scans and targeted forbidden-pattern grep are clean.
thinking
**Organizing the report**

I want to use a clickable path with line numbers, like [concordance.tex](...:60), and perhaps group one link to the file start while mentioning line clusters. I think it’s best to keep the final answer concise, maybe in two short sections: outcome and verification, using bullet points since they’re list-friendly. It should stay under 50-70 lines. I should say, “Read FULL concordance,” but clarify that I didn't read every line manually — I used scripts and targeted reads instead. Finally, I might mention that no further stale type/status mismatches were found in theorem references, and that not all broad forbidden patterns are clean due to pre-existing comment separators.
thinking
**Considering edits for clarity**

I’m looking at the comment separators that are unrelated to the findings, and it feels honest to leave them untouched. But what if the user expects every hit resolved? Should I fix those too? It could be simple, but there are 11 occurrences, and this might involve widespread changes. Converting them to something like `% =====` could satisfy the blacklist without causing major issues. Still, the user requested a surgical fix, focusing only on what's necessary to resolve each finding.
thinking
**Evaluating comment edits**

I'm considering changing the 11 comment lines from `% ---...` to something like `% ==================================================`, since they are low-risk and only comments. The AGENTS don’t allow em-dashes or triple hyphens, and although these separators aren't user-facing, cleaning them up could be beneficial. The user requested a grep check for forbidden patterns after edits. I’m debating whether to report these residual separators or fix them. Since only 11 lines exist, maybe I can patch them without causing semantic issues. But is this still a "minimum truthful edit"?
thinking
**Preparing for comment line edits**

I’m thinking it might be a bit extra, but fixing these lines could satisfy the verification loop since they’re in the same file. There are about 11 lines located at specific positions that I need to address. I can replace all occurrences of `% ----------------------------------------------------------------------` and `%% ------------------------------------------------------------------` with `% ================================================================`, ensuring I don’t use an em dash. I’ll also check the counts using a search tool. This feels like a good approach, even if it seems a bit excessive.
codex
The only remaining forbidden-pattern hits are comment-only separator lines like `%% ------------------------------------------------------------------`. They’re inert, but since they’re in the same file and cheap to normalize, I’m cleaning them too so the post-edit grep finishes cleanly.
exec
/bin/zsh -lc 'rg -n "''^%+ -{3,}$" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2417:%% ------------------------------------------------------------------
2522:%% ------------------------------------------------------------------
2568:%% ------------------------------------------------------------------
2641:%% ------------------------------------------------------------------
3050:%% ------------------------------------------------------------------
3085:%% ------------------------------------------------------------------
3104:%% ------------------------------------------------------------------
3179:%% ------------------------------------------------------------------
9668:% ----------------------------------------------------------------------
9900:% ----------------------------------------------------------------------
9905:% ----------------------------------------------------------------------
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..dd9f82373593a40430a767a4ee97698960d199cb
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -2416,3 +2416,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
@@ -2521,3 +2521,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
@@ -2567,3 +2567,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
@@ -2640,3 +2640,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
@@ -3049,3 +3049,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
@@ -3084,3 +3084,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
@@ -3103,3 +3103,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
@@ -3178,3 +3178,3 @@
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
@@ -9667,3 +9667,3 @@
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
@@ -9899,3 +9899,3 @@
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
@@ -9904,3 +9904,3 @@
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
apply_patch(auto_approved=true) exited 0 in 23ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '2415,2418p;2520,2523p;2566,2569p;2639,2642p;3048,3051p;3083,3086p;3102,3105p;3177,3180p;9666,9669p;9898,9901p;9903,9906p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
lines=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns={
    'todo': r'TODO',
    'theorem_ref_conj': r'Theorem~\\\\ref\\{conj:',
    'proposition_ref_conj': r'Proposition~\\\\ref\\{conj:',
    'theorem_ref_prop': r'Theorem~\\\\ref\\{prop:',
    'proposition_ref_thm': r'Proposition~\\\\ref\\{thm:',
    'theorem_ref_cor': r'Theorem~\\\\ref\\{cor:',
    'emdash': r'—',
}
found=[]
for lineno,line in enumerate(lines,1):
    for name,pat in patterns.items():
        if re.search(pat,line):
            found.append((lineno,name,line))
    if not line.lstrip().startswith('%') and '---' in line:
        found.append((lineno,'triple_hyphen_noncomment',line))
if found:
    for lineno,name,line in found[:20]:
        print(f'{lineno}: {name}: {line}')
    raise SystemExit(1)
print('targeted forbidden-pattern grep: clean')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2415	chapters cited below.
  2416	
  2417	%% ================================================================
  2418	\subsection{The meta-theorem: twelve characterizations}
  2520	\end{enumerate}
  2521	
  2522	%% ================================================================
  2523	\subsection{Sufficient conditions for chiral Koszulness}
  2566	constitution.
  2567	
  2568	%% ================================================================
  2569	\subsection{Operadic complexity}
  2639	
  2640	
  2641	%% ================================================================
  2642	\subsection{Shadow depth classification}
  3048	(Remark~\ref{rem:moonshine-orbifold-class-transition}).
  3049	
  3050	%% ================================================================
  3051	\subsection{Geometric, physics, and categorical
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=list(Path('chapters').rglob('*.tex'))+list(Path('appendices').rglob('*.tex'))
claim_envs={'theorem','proposition','corollary','lemma','conjecture','remark','definition','computation','calculation','maintheorem','verification'}
label_env={}
begin_re=re.compile(r'\\\\begin\\{([A-Za-z*]+)\\}')
end_re=re.compile(r'\\\\end\\{([A-Za-z*]+)\\}')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
for path in tex_files:
    stack=[]
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        for m in begin_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                stack.append((env,lineno))
        for m in label_re.finditer(line):
            lab=m.group(1)
            if stack:
                label_env.setdefault(lab,stack[-1][0])
        for m in end_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                for idx in range(len(stack)-1,-1,-1):
                    if stack[idx][0]==env:
                        stack.pop(idx)
                        break
text=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns=[('Theorem', 'theorem'),('Proposition','proposition'),('Corollary','corollary'),('Lemma','lemma'),('Conjecture','conjecture'),('Remark','remark'),('Definition','definition'),('Computation','computation')]
for i,line in enumerate(text,1):
    for word,env in patterns:
        for lab in re.findall(rf'{word}~\\\\ref\\{{(["'^}}]+)'"\\}}', line):
            actual=label_env.get(lab)
            if actual and actual"'!=env:
                print(f'"'{i}: {word}~\\\\ref{{{lab}}} -> actual {actual}')
                raise SystemExit(1)
print('label-type mismatch scan: clean')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
targeted forbidden-pattern grep: clean
 succeeded in 171ms:
label-type mismatch scan: clean
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common



thinking
**Clarifying the verification process**

I need to keep things concise and perhaps mention that there are no blocked items. So, I'll point out the verification steps I took: a label-type mismatch scan and a targeted forbidden-pattern grep, both cleared.

I didn’t run a full TeX build since it wasn't requested, but I should clarify that I checked \ref and \label validity through a scan rather than a build. This scan ensured type validity but not resolution, so it might be good to check if all referenced labels actually exist.
thinking
**Running verification on references**

I’m thinking of running a quick script to ensure that all references resolve to some label in the repository or are known externally. Since I've extracted 823 unique references, it’s crucial to verify that none remain unresolved. There might be cross-volume references, but within the repo, they should all exist.

I'll search the label_index to include all labels. By building a set from label_index.json, I can check which references are missing. Some might be truncated, but computing counts would be a good verification step. Let's get started!
codex
The status/type surface is clean. I’m doing one last mechanical check that every `\ref{...}` used in the concordance still resolves to a known label, so the closeout can honestly say the constitutional links are intact without claiming a full TeX build I didn’t run.
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
text=Path('chapters/connections/concordance.tex').read_text()
refs=set(re.findall(r'\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}', text))
with open('metadata/label_index.json') as f:
    label_index=json.load(f)
missing=sorted([r for r in refs if r not in label_index])
print('unique refs', len(refs))
print('missing labels', len(missing))
for lab in missing[:50]:
    print(lab)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
unique refs 823
missing labels 9
conj:yangian-ordered-center
def:quartic-log-contact-class
part:bar-complex
part:physics-bridges
part:standard-landscape
princ:modular-trace
prop:quartic-contact-vanishes-BL
thm:recognition
thm:vol2-annulus-trace
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common


thinking
**Investigating missing labels**

I'm noticing that there are 9 missing labels. They might be cross-volume or unindexed, so that's something I need to resolve. The user asked me to check for reference validity, and the missing labels could indicate broken references, which means an investigation is necessary. Since we're auditing for full concordance, I'll need to determine whether these missing refs are stale entries and if adjustments are needed. I should search the repository to get more clarity.
exec
/bin/zsh -lc 'rg -n "(conj:yangian-ordered-center|def:quartic-log-contact-class|part:bar-complex|part:physics-bridges|part:standard-landscape|princ:modular-trace|prop:quartic-contact-vanishes-BL|thm:recognition|thm:vol2-annulus-trace)" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
265:Part~\ref{part:physics-bridges} (Heisenberg, affine Kac--Moody,
1109:developed throughout Parts~\ref{part:bar-complex}--\ref{part:standard-landscape}.
2117:\item The \emph{shadow archetypes in Part~\ref{part:physics-bridges}}: each standard
3894:Parts~\ref{part:bar-complex}--\ref{part:v1-frontier} describe the modular/symmetric framework that is the
4011:Principle~\ref{princ:modular-trace} (Volume~II) organizes the modular
4016:(Theorem~\ref{thm:vol2-annulus-trace}), and (iii)~the closed-sector
4024:Definition~\ref{def:quartic-log-contact-class} (Volume~II) defines
4028:Proposition~\ref{prop:quartic-contact-vanishes-BL} proves
4681:$\mathcal{W}$-algebra chapters of Part~\ref{part:physics-bridges} at genus~$0$.
4728:\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
7262:\ref{conj:yangian-ordered-center}
9892: \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
exec
/bin/zsh -lc "rg -n \"label\\{(conj:yangian-ordered-center|def:quartic-log-contact-class|part:bar-complex|part:physics-bridges|part:standard-landscape|princ:modular-trace|prop:quartic-contact-vanishes-BL|thm:recognition|thm:vol2-annulus-trace)\\}\" ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:1158:\label{conj:yangian-ordered-center}
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:768:main.tex:895:\label{part:bar-complex}
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:770:main.tex:1164:\label{part:standard-landscape}
./wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:771:main.tex:1368:\label{part:physics-bridges}
./rectification_20260412_233715/R06_nilpotent_completion.md:7710:\newlabel{part:bar-complex}{{I}{223}{The Bar Complex}{part.1}{}}
./standalone/programme_summary.tex:1695:\label{thm:recognition}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:309:/Users/raeez/chiral-bar-cobar/main.tex:895:\label{part:bar-complex}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:313:/Users/raeez/chiral-bar-cobar/main.tex:1164:\label{part:standard-landscape}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:315:/Users/raeez/chiral-bar-cobar/main.tex:1368:\label{part:physics-bridges}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1362:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:768:main.tex:895:\label{part:bar-complex}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1364:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:770:main.tex:1164:\label{part:standard-landscape}
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1365:/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:771:main.tex:1368:\label{part:physics-bridges}
./standalone/ordered_chiral_homology.tex:1184:\label{conj:yangian-ordered-center}
./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:685:main.tex:895:\label{part:bar-complex}
./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:687:main.tex:1164:\label{part:standard-landscape}
./fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:688:main.tex:1368:\label{part:physics-bridges}
./standalone/programme_summary_sections5_8.tex:395:\label{thm:recognition}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:71:895:\label{part:bar-complex}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:75:1164:\label{part:standard-landscape}
./fix_wave_A_20260413_112727/A13_fix_hardcoded_parts_v1.md:77:1368:\label{part:physics-bridges}
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

codex
The full-label existence check exposed two likely stale concordance refs, not just type drift: `\ref{thm:recognition}` and `\ref{conj:yangian-ordered-center}` point only to standalone or backup surfaces, not the live manuscript tree. I’m reading those two contexts now to decide the minimal truthful replacement.
exec
/bin/zsh -lc "sed -n '4718,4734p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7258,7270p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{proposition}

\begin{proposition}[Ribbon/'t~Hooft bridge;
\ClaimStatusProvedHere]%
\label{prop:vol2-ribbon-thooft-bridge}%
\index{ribbon structure!cross-volume bridge}%
\index{t Hooft expansion@'t~Hooft expansion!cross-volume bridge}%
The $E_1$ modular Koszul theory of Vol~I
\textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}}\textup{)}
and the Swiss-cheese operad of Vol~II
\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
combine as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
\item bare modular graph sums give genus-organized
 expansions\textup;
\item cyclic trace $+$ matrix realization upgrade these
 to literal 't~Hooft sums with $N^{\chi(\Sigma_\Gamma)}$
exec
/bin/zsh -lc "sed -n '9888,9894p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 $E_1 \not\to E_2$ promotion obstructed by
 non-trivial Drinfeld associator
 \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)}
 & associator $+$ monodromy \\
\ref{conj:yangian-ordered-center}
 & Ordered chiral center of the Yangian:
 derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
 as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
 & standalone paper; cf.\ Theorem~\ref{thm:yangian-e1} \\
\ref{conj:coderived-e3}
 & Coderived $E_3$: $D^{\mathrm{co}}$-level $E_3$ on
 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$
 without conformal vector \textup{(}Conjecture\textup{)}
 succeeded in 51ms:
 \textup{(}Conjecture~\ref{conj:shadow-s1-quantum-volume}\textup{)} \\
& Page curve from Koszul complementarity
 \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
& Ordered chiral center of the Yangian
 \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
& Coderived $E_3$ without conformal vector
 \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
exec
/bin/zsh -lc "rg -n \"Yangian ordered center|ordered center|recognition\" chapters appendices main.tex standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
main.tex:1732: \phantomsection\label{conj:cumulant-recognition}%
main.tex:1882: \phantomsection\label{thm:yangian-recognition}% % Vol II spectral-braiding-core.tex
chapters/examples/lattice_foundations.tex:4212:Schwede--Shipley recognition theorem~\cite{SS03}).
standalone/ordered_chiral_homology.tex:7282:the recognition principle for $\mathsf{E}_n$-algebras
standalone/programme_summary_sections5_8.tex:374:\subsection{PVA descent and the recognition theorem}
standalone/programme_summary_sections5_8.tex:392:The recognition theorem establishes the converse:
standalone/programme_summary_sections5_8.tex:395:\label{thm:recognition}
appendices/koszul_reference.tex:263:The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
appendices/ordered_associative_chiral_kd.tex:6451:This is the content of the Yangian recognition theorem
appendices/ordered_associative_chiral_kd.tex:6452:(Theorem~\ref*{thm:yangian-recognition}, recorded from Volume~II).
standalone/programme_summary.tex:1674:\subsection{PVA descent and the recognition theorem}
standalone/programme_summary.tex:1692:The recognition theorem establishes the converse:
standalone/programme_summary.tex:1695:\label{thm:recognition}
standalone/N2_mc3_all_types.tex:288:factorization formalism, but the recognition that
chapters/examples/yangians_drinfeld_kohno.tex:7879:the ordered center is the habitat of the full spin-chain Hilbert
chapters/connections/concordance.tex:452: Two independent proofs: (i)~operadic, via the recognition theorem
chapters/connections/concordance.tex:4000:$\SCchtop$, and the recognition theorem (Volume~II, items F4--F5)
chapters/connections/concordance.tex:4728:\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
chapters/connections/concordance.tex:5177:\begin{conjecture}[Cumulant recognition; \ClaimStatusConjectured]
chapters/connections/concordance.tex:5178:\label{conj:cumulant-recognition}
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

codex
Two refs really are stale. They aren’t just metadata misses: `thm:recognition` has no live label, and `conj:yangian-ordered-center` only survives in standalone/backup files. I’m finding the active cross-volume labels they were meant to point at, or I’ll downgrade them to plain text if no live target exists.
exec
/bin/zsh -lc "rg -n \"ordered center|Yangian recognition theorem|thm:yangian-recognition|center essential surjectivity|yangian-e1\" chapters appendices main.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11050,11080p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7868,7890p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7160,7275p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
main.tex:1882: \phantomsection\label{thm:yangian-recognition}% % Vol II spectral-braiding-core.tex
appendices/ordered_associative_chiral_kd.tex:6451:This is the content of the Yangian recognition theorem
appendices/ordered_associative_chiral_kd.tex:6452:(Theorem~\ref*{thm:yangian-recognition}, recorded from Volume~II).
chapters/examples/yangians_drinfeld_kohno.tex:7879:the ordered center is the habitat of the full spin-chain Hilbert
chapters/examples/yangians_computations.tex:112:$\Eone$-chiral structure (Conjecture~\ref{conj:shifted-yangian-e1})
chapters/examples/yangians_computations.tex:134:This is an $\Eone$-chiral incarnation of symplectic duality (Braden--Licata--Proudfoot--Webster \cite{BLPW16}): the shift $\mu \mapsto -\mu$ reverses monopole boundary conditions, i.e.\ $R(u) \mapsto R(u)^{-1}$ with Langlands involution. A proof requires Conjecture~\ref{conj:shifted-yangian-e1} and identification of the bar complex at coweight $\mu$ with the cobar at $-\mu$ for $\fg^\vee$.
chapters/examples/yangians_computations.tex:3202:Remark~\ref{rem:yangian-e1-inversion}).
chapters/examples/yangians_foundations.tex:67: (Theorem~\ref{thm:yangian-e1}): vertex operators on~$X$ with
chapters/examples/yangians_foundations.tex:363:\begin{theorem}[Yangian as \texorpdfstring{$\Eone$}{E1}-chiral; \ClaimStatusProvedHere]\label{thm:yangian-e1}
chapters/examples/yangians_foundations.tex:434:The $\Eone$-chiral structure of Theorem~\ref{thm:yangian-e1} is
chapters/examples/yangians_foundations.tex:591:\label{rem:yangian-e1-inversion}
chapters/examples/yangians_foundations.tex:1258:\begin{conjecture}[Shifted Yangian as \texorpdfstring{$\Eone$}{E1}-chiral; \ClaimStatusConjectured]\label{conj:shifted-yangian-e1}
chapters/examples/yangians_foundations.tex:1274:$\Eone$-chiral structure is established in Theorem~\ref{thm:yangian-e1}.
chapters/examples/yangians_foundations.tex:1294:\textup{(}Theorem~\textup{\ref{thm:yangian-e1})}
chapters/examples/yangians_foundations.tex:1327:(Theorem~\ref{thm:yangian-e1}). In the DNP construction,
chapters/examples/yangians_foundations.tex:1500: (Theorem~\ref{thm:yangian-e1},
chapters/examples/yangians_foundations.tex:2491:Theorem~\ref{thm:yangian-e1} to the defining evaluation module via
chapters/examples/yangians_foundations.tex:2514:Theorem~\ref{thm:yangian-e1} identifies the one-factor OPE kernel with
chapters/examples/yangians_foundations.tex:2819:(Theorem~\ref{thm:yangian-e1}) is the evaluation-generated
chapters/connections/concordance.tex:7266: & standalone paper; cf.\ Theorem~\ref{thm:yangian-e1} \\
 succeeded in 51ms:
Q_0^0(\mathfrak{g})\;\simeq\; Y_\hbar(\mathfrak{g}).
\end{equation}

\begin{theorem}[Unshifted identification; \ClaimStatusProvedHere]
\label{thm:unshifted-identification}
On the chirally Koszul locus, the line-side algebra $A^!_{\mathrm{line}}$
produced by ordered associative chiral Koszul duality of $\widehat{\mathfrak{g}}_k$
is isomorphic to the Yangian $Y_\hbar(\mathfrak{g})$:
\[
A^!_{\mathrm{line}}\bigl(\widehat{\mathfrak{g}}_k\bigr)
\;\simeq\;
Y_\hbar(\mathfrak{g})
\;\simeq\;
Q_0^0(\mathfrak{g}).
\]
\end{theorem}

\begin{proof}
This is the content of the Yangian recognition theorem
(Theorem~\ref*{thm:yangian-recognition}, recorded from Volume~II).
 succeeded in 50ms:
The chain of projections
\[
\underbrace{\Theta_\cA}_{\text{MC element}}
\;\xrightarrow{\;\mathrm{degree}\;L\;}
\underbrace{V^{\otimes L},\; PB_L\text{-monodromy}}_{\text{ordered
center: wavefunctions}}
\;\xrightarrow{\;\av_L\;}
\underbrace{\Lambda(u),\; Q(u)}_{\text{symmetric shadow:
eigenvalues, BAE}}
\]
is the bar-complex refinement of the algebraic Bethe ansatz:
the ordered center is the habitat of the full spin-chain Hilbert
space, and the symmetric shadow extracts the integrable
Hamiltonian's spectral data.
\end{remark}

%% =================================================================
%% § THE r-MATRIX AS KOSZUL-DUAL INVERSE
%% =================================================================

 succeeded in 51ms:

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common


thinking
**Inspecting context usage**

I’m not getting any output from the en_koszul range, which could mean there aren’t any lines to pull. I think I need to check the context at line 11436. It might be using the textual theorem name `thm:yangian-recognition` without the reference macro, which seems worth inspecting further. I'll double-check to see if that’s the case.
exec
/bin/zsh -lc "sed -n '11430,11438p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 On the affine lineage, the open-colour Koszul dual
 is a dg-shifted Yangian
 (Vol~II, Theorem~\textup{thm:Koszul\_dual\_Yangian}:
 \emph{proved}).
 On the chirally Koszul locus, the Yangian
 recognition theorem
 (Vol~II, Theorem~\textup{thm:yangian-recognition}) identifies
 the $\mathsf{SC}^{\mathrm{ch,top}}$-algebra
 structure on~$\cA^!_{\mathrm{line}}$ with the
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

exec
/bin/zsh -lc "sed -n '1688,1702p' standalone/programme_summary.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
theorem on $\FM_3(\Bbbk)$ for Jacobi, and boundary
factorization on higher $\FM_k(\Bbbk)$ for the remaining
axioms.

The recognition theorem establishes the converse:

\begin{theorem}[Recognition]
\label{thm:recognition}
A factorization algebra on\/ $\Ran(X)$ equipped with Weiss
cosheaf descent data and compatible with the factorization
isomorphisms is a $C_*(\mathcal{W}(\mathrm{SC}^{\mathrm{ch,top}}))$-algebra.
\end{theorem}

The theorem converts the abstract factorization structure
into a concrete operadic algebra over the Boardman--Vogt
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

codex
The two unresolved refs don’t have live manuscript labels to retarget. I’m replacing them with plain-text cross-volume descriptions rather than inventing new labels, which keeps the concordance truthful and avoids touching other files.
exec
/bin/zsh -lc "sed -n '7248,7271p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9888,9894p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 DS reduction commutes with chiral Hochschild
 \textup{(}Proposition~\ref{prop:ds-chirhoch-compatibility}\textup{)}
 & BRST complex $+$ HPL transfer \\
\ref{prop:ker-av-schur-weyl}
 & Kernel of averaging: $\dim\ker(\mathrm{av}_n) = n! - \binom{n+d-1}{n}$
 closed formula via Schur--Weyl
 \textup{(}Proposition~\ref{prop:ker-av-schur-weyl}\textup{)}
 & Schur--Weyl duality $+$ symmetric group characters \\
Vol.~III
 & $E_1$-obstruction is categorical:
 $E_1 \not\to E_2$ promotion obstructed by
 non-trivial Drinfeld associator
 \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)}
 & associator $+$ monodromy \\
\ref{conj:yangian-ordered-center}
 & Ordered chiral center of the Yangian:
 derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
 as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
 & standalone paper; cf.\ Theorem~\ref{thm:yangian-e1} \\
\ref{conj:coderived-e3}
 succeeded in 52ms:
 \textup{(}Conjecture~\ref{conj:shadow-s1-quantum-volume}\textup{)} \\
& Page curve from Koszul complementarity
 \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
& Ordered chiral center of the Yangian
 \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
& Coderived $E_3$ without conformal vector
 \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
exec
/bin/zsh -lc "sed -n '4722,4730p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{prop:vol2-ribbon-thooft-bridge}%
\index{ribbon structure!cross-volume bridge}%
\index{t Hooft expansion@'t~Hooft expansion!cross-volume bridge}%
The $E_1$ modular Koszul theory of Vol~I
\textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}}\textup{)}
and the Swiss-cheese operad of Vol~II
\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
combine as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..783d0f57e029112cfe07cc5725df949e94165643
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -4727,3 +4727,3 @@
 and the Swiss-cheese operad of Vol~II
-\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
+\textup{(}the Volume~II recognition theorem\textup{)}
 combine as follows:
@@ -7261,3 +7261,3 @@
  & associator $+$ monodromy \\
-\ref{conj:yangian-ordered-center}
+Ordered-center conjecture
  & Ordered chiral center of the Yangian:
@@ -9891,3 +9891,3 @@
 & Ordered chiral center of the Yangian
- \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
+ \textup{(}standalone conjecture\textup{)} \\
 & Coderived $E_3$ without conformal vector
apply_patch(auto_approved=true) exited 0 in 20ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..894e647c6ec119034b741308e95613d92219cfe4
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -4723,7 +4725,7 @@
 The $E_1$ modular Koszul theory of Vol~I
 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}}\textup{)}
 and the Swiss-cheese operad of Vol~II
-\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
+\textup{(}the Volume~II recognition theorem\textup{)}
 combine as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item bare modular graph sums give genus-organized
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -7260,7 +7259,7 @@
  non-trivial Drinfeld associator
  \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)}
  & associator $+$ monodromy \\
-\ref{conj:yangian-ordered-center}
+Ordered-center conjecture
  & Ordered chiral center of the Yangian:
  derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
  as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9890,7 +9889,7 @@
 & Page curve from Koszul complementarity
  \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
 & Ordered chiral center of the Yangian
- \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
+ \textup{(}standalone conjecture\textup{)} \\
 & Coderived $E_3$ without conformal vector
  \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
 & Center essential surjectivity
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..894e647c6ec119034b741308e95613d92219cfe4
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -4723,7 +4725,7 @@
 The $E_1$ modular Koszul theory of Vol~I
 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}}\textup{)}
 and the Swiss-cheese operad of Vol~II
-\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
+\textup{(}the Volume~II recognition theorem\textup{)}
 combine as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item bare modular graph sums give genus-organized
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -7260,7 +7259,7 @@
  non-trivial Drinfeld associator
  \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)}
  & associator $+$ monodromy \\
-\ref{conj:yangian-ordered-center}
+Ordered-center conjecture
  & Ordered chiral center of the Yangian:
  derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
  as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9890,7 +9889,7 @@
 & Page curve from Koszul complementarity
  \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
 & Ordered chiral center of the Yangian
- \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
+ \textup{(}standalone conjecture\textup{)} \\
 & Coderived $E_3$ without conformal vector
  \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
 & Center essential surjectivity
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common


thinking
**Reviewing label check**

I need to rerun the check for label existence in main.tex. It might be helpful to build a label set that includes all the .tex files, such as standalone ones, because we want to ensure we have an active tree. It looks like the two missing labels were stale, specifically the part labels in main.tex and the phantom labels in vol2. Including main.tex in this will help resolve the issue. Alright, let's go ahead and rerun this!
codex
I removed the two genuinely stale broken refs and replaced them with plain-text cross-volume descriptions. One final label-existence pass now, this time against the live `.tex` tree including `main.tex`’s imported-volume labels.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
paths=[Path('main.tex')] + list(Path('chapters').rglob('*.tex')) + list(Path('appendices').rglob('*.tex'))
labels=set()
for path in paths:
    txt=path.read_text()
    labels.update(re.findall(r'\\\\label\\{(["'^}]+)'"\\}', txt))
refs=set(re.findall(r'\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}', Path('chapters/connections/concordance.tex').read_text()))
missing=sorted(refs-labels)
print('unique refs', len(refs))
print('missing labels', len(missing))
for lab in missing:
    print(lab)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
lines=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns={
    'todo': r'TODO',
    'theorem_ref_conj': r'Theorem~\\\\ref\\{conj:',
    'proposition_ref_conj': r'Proposition~\\\\ref\\{conj:',
    'theorem_ref_prop': r'Theorem~\\\\ref\\{prop:',
    'proposition_ref_thm': r'Proposition~\\\\ref\\{thm:',
    'theorem_ref_cor': r'Theorem~\\\\ref\\{cor:',
    'emdash': r'—',
}
for lineno,line in enumerate(lines,1):
    for name,pat in patterns.items():
        if re.search(pat,line):
            print(f'{lineno}: {name}: {line}')
            raise SystemExit(1)
    if not line.lstrip().startswith('%') and '---' in line:
        print(f'{lineno}: triple_hyphen_noncomment: {line}')
        raise SystemExit(1)
print('targeted forbidden-pattern grep: clean')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
unique refs 821
missing labels 25
prop:bar-hocolim
prop:boundary-sigma-ratio
prop:class-g-no-instantons
prop:kappa-k3
prop:thqg-X-heisenberg-sewing-envelope
rem:db-k3xe-reconstruction
rem:factor-2-is-kappa
rem:four-kappas
rem:genus-expansion-convergence-comparison
rem:kappa-spectrum-k3xe
rem:leech-connection
rem:mock-modular-k3
rem:thqg-I-admissible
rem:thqg-I-singular-fibers
sec:bkm-k3e
sec:bps-bh-k3xe
sec:cy-local-global
sec:enum-geom-k3xe
 succeeded in 51ms:
targeted forbidden-pattern grep: clean
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
tex_files=[Path('main.tex')] + list(Path('chapters').rglob('*.tex')) + list(Path('appendices').rglob('*.tex'))
claim_envs={'theorem','proposition','corollary','lemma','conjecture','remark','definition','computation','calculation','maintheorem','verification'}
label_env={}
begin_re=re.compile(r'\\\\begin\\{([A-Za-z*]+)\\}')
end_re=re.compile(r'\\\\end\\{([A-Za-z*]+)\\}')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
for path in tex_files:
    stack=[]
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        for m in begin_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                stack.append((env,lineno))
        for m in label_re.finditer(line):
            lab=m.group(1)
            if stack:
                label_env.setdefault(lab,stack[-1][0])
        for m in end_re.finditer(line):
            env=m.group(1)
            if env in claim_envs:
                for idx in range(len(stack)-1,-1,-1):
                    if stack[idx][0]==env:
                        stack.pop(idx)
                        break
text=Path('chapters/connections/concordance.tex').read_text().splitlines()
patterns=[('Theorem', 'theorem'),('Proposition','proposition'),('Corollary','corollary'),('Lemma','lemma'),('Conjecture','conjecture'),('Remark','remark'),('Definition','definition'),('Computation','computation')]
for i,line in enumerate(text,1):
    for word,env in patterns:
        for lab in re.findall(rf'{word}~\\\\ref\\{{(["'^}}]+)'"\\}}', line):
            actual=label_env.get(lab)
            if actual and actual"'!=env:
                print(f'"'{i}: {word}~\\\\ref{{{lab}}} -> actual {actual}')
                raise SystemExit(1)
print('label-type mismatch scan: clean')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 153ms:
label-type mismatch scan: clean
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..894e647c6ec119034b741308e95613d92219cfe4
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -4723,7 +4725,7 @@
 The $E_1$ modular Koszul theory of Vol~I
 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}}\textup{)}
 and the Swiss-cheese operad of Vol~II
-\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
+\textup{(}the Volume~II recognition theorem\textup{)}
 combine as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item bare modular graph sums give genus-organized
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -7260,7 +7259,7 @@
  non-trivial Drinfeld associator
  \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)}
  & associator $+$ monodromy \\
-\ref{conj:yangian-ordered-center}
+Ordered-center conjecture
  & Ordered chiral center of the Yangian:
  derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
  as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9890,7 +9889,7 @@
 & Page curve from Koszul complementarity
  \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
 & Ordered chiral center of the Yangian
- \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
+ \textup{(}standalone conjecture\textup{)} \\
 & Coderived $E_3$ without conformal vector
  \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
 & Center essential surjectivity
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

exec
/bin/zsh -lc "rg -n \"label\\{prop:thqg-X-heisenberg-sewing-envelope\\}|label\\{prop:bar-hocolim\\}|label\\{rem:genus-expansion-convergence-comparison\\}|label\\{sec:thqg-perturbative-finiteness\\}\" ." in /Users/raeez/chiral-bar-cobar succeeded in 63ms:
./resume_20260413_163457/S14_standalone_to_main.md:991:chapters/connections/thqg_fredholm_partition_functions.tex:245:\label{prop:thqg-X-heisenberg-sewing-envelope}%
./relaunch_20260413_111534/F17_dangling_refs_v1.md:1224:\begin{remark}[Genus expansion convergence]\label{rem:genus-expansion-convergence-comparison}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:24421:\label{prop:bar-hocolim}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:25488:\label{prop:thqg-X-heisenberg-sewing-envelope}%
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:34331:\label{sec:thqg-perturbative-finiteness}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:36410:\begin{remark}[Genus expansion convergence]\label{rem:genus-expansion-convergence-comparison}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:54560:-\label{prop:thqg-X-heisenberg-sewing-envelope}%
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:69311:-\label{sec:thqg-perturbative-finiteness}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:71390:-\begin{remark}[Genus expansion convergence]\label{rem:genus-expansion-convergence-comparison}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:86277:-\label{prop:bar-hocolim}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:95897:-\label{prop:thqg-X-heisenberg-sewing-envelope}%
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:110648:-\label{sec:thqg-perturbative-finiteness}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:112727:-\begin{remark}[Genus expansion convergence]\label{rem:genus-expansion-convergence-comparison}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:127614:-\label{prop:bar-hocolim}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:137253:-\label{prop:thqg-X-heisenberg-sewing-envelope}%
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:152004:-\label{sec:thqg-perturbative-finiteness}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:154083:-\begin{remark}[Genus expansion convergence]\label{rem:genus-expansion-convergence-comparison}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:168970:-\label{prop:bar-hocolim}
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:178634:-\label{prop:thqg-X-heisenberg-sewing-envelope}%
./fix_wave_B_20260413_171623/B11_orphaned_chapters.md:193385:-\label{sec:thqg-perturbative-finiteness}
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..894e647c6ec119034b741308e95613d92219cfe4
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -4723,7 +4725,7 @@
 The $E_1$ modular Koszul theory of Vol~I
 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}}\textup{)}
 and the Swiss-cheese operad of Vol~II
-\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
+\textup{(}the Volume~II recognition theorem\textup{)}
 combine as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item bare modular graph sums give genus-organized
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -7260,7 +7259,7 @@
  non-trivial Drinfeld associator
  \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)}
  & associator $+$ monodromy \\
-\ref{conj:yangian-ordered-center}
+Ordered-center conjecture
  & Ordered chiral center of the Yangian:
  derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
  as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9890,7 +9889,7 @@
 & Page curve from Koszul complementarity
  \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
 & Ordered chiral center of the Yangian
- \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
+ \textup{(}standalone conjecture\textup{)} \\
 & Coderived $E_3$ without conformal vector
  \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
 & Center essential surjectivity
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common





thinking
**Assessing reference issues**

I see that the search only found references in audit files and not in the active text. This points to a bigger issue involving orphaned chapters or volumes. The user specifically asked for a complete audit of the concordance, wanting me to check the status, scope, and any stale entries. The call to "Check \ref and \label validity" suggests I should catch broken references. Since the target file is specific, I can replace them with existing references. However, there are 25 references, which could get complicated! But not all might be theorems; many could be section references from Volume III, especially given the user’s request for an exhaustive audit.
thinking
**Evaluating unresolved references**

I realize that there are still 25 unresolved cross-volume or non-active references in the concordance, mainly pointing to Volume III or orphaned chapters. I didn't rewrite those because it would require a broader adjustment across volumes. While I can only edit the assigned file, fixing these references could still be larger in scope. I'd consider labeling them as BLOCKED since they require decisions on replacements in Volumes II or III. It's key to determine if they're concentrated in certain sections, and if they actually block reference validity. This needs precise explanation!
thinking
**Clarifying reference actions**

I've identified that while the theorem-status surface is fixed, there are still cross-volume orphaned references that I should mention. It might be simpler to fix the easier ones, especially around the K3 programs, by replacing them with plain text like "Vol III K3/BKM bridge sections." However, user requested a minimum truthful edit, so perhaps it's best to avoid broad rewrites and just report the blocked references. Leaving broken references in the target file might be acceptable if they don't impact specific findings, but since the user asked for a validity check, it makes sense to label them as blocked.
thinking
**Evaluating theorem existence**

I think I need to rerun a line existence scan that's limited to theorem labels in concordance. I want to check if all unique theorem-like references actually exist. Running this scan could boost my confidence, even if it isn't absolutely necessary. I could use regex to catch labels like `thm:` and `prop:` if any are missing. I suspect about 12 theorem-like entries might be missing from the list, particularly props and remarks.
codex
Audited the full concordance theorem/status surface in [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1) against live source and made only local fixes.

- `FIXED`: Theorem D’s constitutional summary now cites the live multi-weight correction theorem, so its scope split is anchored to source rather than implied prose alone. See [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:60).
- `FIXED`: Seven stale label/environment mismatches in the concordance prose were corrected: conjectures no longer called propositions/theorems, a proposition is no longer called a theorem, and a corollary is no longer called a theorem. Representative fixes are at [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1932), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:2508), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3076), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6481), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6854), [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:8720).
- `FIXED`: The stale `% TODO(status-sync)` residue left from an earlier rectification pass was removed from the family-index routing proof. See [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6121).
- `FIXED`: Two genuinely stale broken refs were removed from the live constitutional surface and replaced with plain-text cross-volume descriptions: the dead `thm:recognition` ref and the dead `conj:yangian-ordered-center` ref. See [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4726) and [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7262).
- `FIXED`: Comment-only triple-hyphen separator lines were normalized so the post-edit forbidden-pattern grep is clean.

- `BLOCKED`: A broader mechanical ref-existence check still finds 25 unresolved non-theorem cross-volume/orphaned labels in the concordance, mostly section/remark/proposition refs like `sec:k3-chiral-algebra`, `prop:bar-hocolim`, `rem:four-kappas`. Resolving those cleanly needs a separate cross-volume retargeting pass or new phantom labels in `main.tex`; I did not widen this surgical edit into that larger rewrite.

Verification: the full label-type mismatch scan against live `.tex` environments is clean, and the targeted forbidden-pattern grep on `chapters/connections/concordance.tex` is clean. I did not run a TeX build.
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index b5630154d0b1947aa5a56fb440ac6a1eccc7c681..894e647c6ec119034b741308e95613d92219cfe4
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -1930,7 +1932,7 @@
 Conditionally, the remaining packages~(ii)--(iv) are
 type-independent once the relevant shifted-prefundamental,
 pro-Weyl, and compact-completion inputs are supplied in that
-type (Proposition~\ref{conj:mc3-automatic-generalization}).
+type (Conjecture~\ref{conj:mc3-automatic-generalization}).
 \end{construction}
 
 \item \emph{MC4}: The formal completion theory is \textbf{proved} by
@@ -2412,7 +2414,7 @@
 programme. Full statements and proofs live in the source
 chapters cited below.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{The meta-theorem: twelve characterizations}
 \label{subsec:concordance-koszulness-meta-theorem}
 \index{Koszul property!equivalences|textbf}
@@ -2505,7 +2507,7 @@
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-lagrangian}
  Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
- (Theorem~\ref{conj:lagrangian-koszulness}).
+ (Conjecture~\ref{conj:lagrangian-koszulness}).
  PTVV derived intersection. Perfectness verified for the standard
  landscape (Proposition~\ref{prop:lagrangian-perfectness},
  Corollary~\ref{cor:lagrangian-unconditional}): unconditional at
@@ -2517,7 +2519,7 @@
  \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
 \end{enumerate}
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Sufficient conditions for chiral Koszulness}
 \label{subsec:concordance-koszulness-sufficient}
 \index{Koszul property!sufficient conditions|textbf}
@@ -2563,7 +2565,7 @@
 rationality criterion for chiral Koszulness is claimed in the
 constitution.
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Operadic complexity}
 \label{subsec:concordance-operadic-complexity}
 \index{operadic complexity|textbf}
@@ -2636,7 +2638,7 @@
 \end{center}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Shadow depth classification}
 \label{subsec:concordance-shadow-depth-classes}
 \index{shadow depth!classification}
@@ -2735,7 +2737,7 @@
 minimal models: $d_{\mathrm{arith}}$ finite,
 $d_{\mathrm{alg}} = \infty$. The Borel sum of the
 Virasoro shadow series gives $-\log(1 + 6t/c)$ at leading
-order (Proposition~\ref{thm:shadow-gf-borel}).
+order (Theorem~\ref{thm:shadow-gf-borel}).
 
 \smallskip\noindent\textbf{Shadow growth rate}
 (Definition~\ref{def:shadow-growth-rate},
@@ -3045,7 +3047,7 @@
 landscape where a finite orbifold changes the shadow class
 (Remark~\ref{rem:moonshine-orbifold-class-transition}).
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Geometric, physics, and categorical
  characterizations}
 \label{subsec:concordance-further-characterizations}
@@ -3071,7 +3073,7 @@
 
 \smallskip\noindent\textbf{Categorical.}
 \begin{itemize}[nosep]
-\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Proposition~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
+\item \emph{$t$-structures}: a highest-weight bar/Koszul $t$-structure comparison is conditional on separate module-category $t$-exactness and linearity input; there is no unconditional global $\barBch$ $t$-exactness theorem (Conjecture~\ref{conj:koszul-t-structures}, Conjecture~\ref{conj:module-category-t-exactness}).
 \item \emph{Barr--Beck--Lurie}: effective descent for bar-cobar (Remark~\ref{rem:construction-vs-resolution}).
 \item \emph{Semi-orthogonal decomposition}: weight-indexed SOD on $\operatorname{FactMod}(\cA)$ is split iff Koszul.
 \item \emph{BGG}: bar resolution of $V_k(\fg)$-modules is linear; Koszul involution maps BGG to Cousin on $\operatorname{Gr}_G$ (Corollary~\ref{cor:bgg-koszul-involution}).
@@ -3080,7 +3082,7 @@
 \end{itemize}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Bifunctor obstruction}
 \label{subsec:concordance-bifunctor-obstruction}
 \index{Robert-Nicoud--Wierstra!bifunctor obstruction}
@@ -3099,7 +3101,7 @@
 \label{rem:concordance-bifunctor-koszul}
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Computational diagnostics}
 \label{subsec:concordance-computational-diagnostics}
 \index{Koszul property!computational diagnostics}
@@ -3174,7 +3176,7 @@
 \texttt{test\_propagator\_variance\_landscape.py} (143 tests).
 
 
-%% ------------------------------------------------------------------
+%% ================================================================
 \subsection{Cross-reference table}
 \label{subsec:concordance-koszulness-xref}
 
@@ -4723,7 +4725,7 @@
 The $E_1$ modular Koszul theory of Vol~I
 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul}}\textup{)}
 and the Swiss-cheese operad of Vol~II
-\textup{(}Theorem~\textup{\ref{thm:recognition}}\textup{)}
+\textup{(}the Volume~II recognition theorem\textup{)}
 combine as follows:
 \begin{enumerate}[label=\textup{(\roman*)}]
 \item bare modular graph sums give genus-organized
@@ -6119,9 +6121,6 @@
 Thus Theorem~\ref{thm:family-index} is a downstream
 Grothendieck--Riemann--Roch repackaging of the scalar genus series,
 and it is not an input to Theorem~\ref{thm:genus-universality}.
-% TODO(status-sync): After the remaining rectification passes land,
-% sync this concordance surface with any theorem-status downgrades,
-% scope narrowings, or inserted missing lemmas.
 
 The proof assembles four ingredients, each established
 independently.
@@ -6479,7 +6478,7 @@
  promotion beyond generators now splits into two distinct issues:
  \emph{thick generation} and an \emph{ambient
  extension/comparison package}. On the Yangian module surface,
- Theorem~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
+ Conjecture~\ref{conj:dk-fd-typeA} and Corollary~\ref{cor:dk-poly-catO}
  are only conditional thick-generation extension criteria: once one
  constructs an ambient exact/lax monoidal extension of the
  evaluation-level bar-comodule comparison, together with the required
@@ -6852,7 +6851,7 @@
 \item Theorem~\ref{thm:hc-shadow-redundancy}:
  shadow depth $=$ redundancy channels
  (resolves Conjecture~\ref{conj:thqg-shadow-depth-code-distance}).
-\item Theorem~\ref{prop:hc-dictionary}:
+\item Proposition~\ref{prop:hc-dictionary}:
  12-fold Koszulness--code dictionary (K1--K12 $\to$ code properties).
 \end{enumerate}
 Status: \textbf{all proved}.
@@ -7260,7 +7259,7 @@
  non-trivial Drinfeld associator
  \textup{(}Volume~III proposition on the categorical $E_2$-obstruction for CY$_3$\textup{)}
  & associator $+$ monodromy \\
-\ref{conj:yangian-ordered-center}
+Ordered-center conjecture
  & Ordered chiral center of the Yangian:
  derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
  as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
@@ -8718,7 +8717,7 @@
 
 \smallskip\noindent
 \textbf{(10)~Ramanujan bound for lattice eigenforms, Deligne-free}
-(Theorem~\ref{cor:ramanujan-deligne-free}):
+(Corollary~\ref{cor:ramanujan-deligne-free}):
 twelve-station proof using MC + HS-sewing + CPS + Jacquet-Shalika + Serre.
 No $\ell$-adic cohomology.
 
@@ -9666,7 +9665,7 @@
 \texttt{modular\_shadow\_tower} (104~tests).
 \end{remark}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \paragraph{April 2026 session: falsification test results.}
 Five additional falsification tests were evaluated against this
 session's structural corrections (AP165 operadic scoping,
@@ -9890,7 +9889,7 @@
 & Page curve from Koszul complementarity
  \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
 & Ordered chiral center of the Yangian
- \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
+ \textup{(}standalone conjecture\textup{)} \\
 & Coderived $E_3$ without conformal vector
  \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
 & Center essential surjectivity
@@ -9898,12 +9897,12 @@
 \end{tabular}
 \end{center}
 
-% ----------------------------------------------------------------------
+% ================================================================
 \subsection{The descent fan}
 \label{subsec:concordance-descent-fan}
 \index{descent fan|textbf}
 \index{Theta_A@$\Theta_\cA$!descent fan}
-% ----------------------------------------------------------------------
+% ================================================================
 
 The MC element $\Theta_\cA$ projects onto three
 mathematical worlds. These projections share a common

tokens used
451,145
