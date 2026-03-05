#!/usr/bin/env python3
"""
Generate machine-readable metadata from the chiral bar-cobar monograph.

Outputs:
  metadata/claims.jsonl         — One JSON line per tagged claim
  metadata/census.json          — Single source of truth for all counts
  metadata/dependency_graph.dot — Machine-traversable theorem DAG
  metadata/label_index.json     — All labels with file:line locations

Usage:
  python3 scripts/generate_metadata.py
  # or: make metadata
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
METADATA_DIR = ROOT / "metadata"

# All environments that can carry a ClaimStatus tag
CLAIM_ENVS = {
    "theorem", "lemma", "proposition", "corollary", "conjecture",
    "computation", "calculation", "maintheorem", "verification", "remark",
}

# All theorem-like environments (for label indexing, broader than CLAIM_ENVS)
THEOREM_LIKE_ENVS = CLAIM_ENVS | {
    "definition", "example", "construction", "convention",
    "notation", "framework", "principle", "observation",
    "question", "openproblem", "setup", "strategy",
}

# Claim status patterns
STATUS_RE = re.compile(
    r"\\ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Open|Heuristic)"
)

# Label patterns
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")

# Reference patterns (all \ref-family commands)
REF_RE = re.compile(
    r"\\(?:ref|autoref|Cref|cref|eqref|nameref|hyperref)\{([^}]+)\}"
)

# Citation pattern
CITE_RE = re.compile(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}")

# Include/input pattern
INCLUDE_RE = re.compile(r"\\(?:include|input)\{([^}]+)\}")

# Begin environment pattern
BEGIN_RE = re.compile(r"\\begin\{([a-zA-Z]+)\}")

# Environment with optional arg (captures the optional argument)
BEGIN_OPT_RE = re.compile(
    r"\\begin\{([a-zA-Z]+)\}\s*\[([^\]]*)\]", re.DOTALL
)

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class Claim:
    """A single tagged mathematical claim."""
    label: str
    env_type: str  # theorem, lemma, proposition, etc.
    status: str    # ProvedHere, ProvedElsewhere, Conjectured, Heuristic, Open
    file: str      # relative path
    line: int      # 1-indexed line number
    title: str     # optional title from [...] argument
    labels_in_block: list[str] = field(default_factory=list)
    refs_in_block: list[str] = field(default_factory=list)
    cites_in_block: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        # Remove empty lists for compactness
        if not d["labels_in_block"]:
            del d["labels_in_block"]
        if not d["refs_in_block"]:
            del d["refs_in_block"]
        if not d["cites_in_block"]:
            del d["cites_in_block"]
        return d


@dataclass
class LabelEntry:
    """A label with its location and context."""
    label: str
    file: str
    line: int
    env_type: Optional[str] = None  # if inside a theorem-like env


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def strip_comments(text: str) -> str:
    """Remove LaTeX comments (% to end of line), preserving \\%."""
    lines = []
    for line in text.splitlines():
        result = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                break
            result.append(line[i])
            i += 1
        lines.append("".join(result))
    return "\n".join(lines)


def get_active_files() -> list[Path]:
    """Get all .tex files included by main.tex, in order."""
    main_path = ROOT / "main.tex"
    if not main_path.exists():
        print("ERROR: main.tex not found", file=sys.stderr)
        sys.exit(1)

    main_text = strip_comments(main_path.read_text(encoding="utf-8", errors="ignore"))

    files: list[Path] = []
    seen: set[Path] = set()

    for match in INCLUDE_RE.finditer(main_text):
        rel = match.group(1)
        if not rel.endswith(".tex"):
            rel += ".tex"
        path = ROOT / rel
        if path.is_file() and path not in seen:
            seen.add(path)
            files.append(path)

    return files


def get_all_tex_files() -> list[Path]:
    """Get ALL .tex files in chapters/ and appendices/."""
    dirs = [ROOT / "chapters", ROOT / "appendices"]
    files = []
    for d in dirs:
        if d.exists():
            files.extend(sorted(d.rglob("*.tex")))
    return files


def find_env_end(lines: list[str], start_idx: int, env_name: str) -> int:
    """Find the line index of \\end{env_name} matching the \\begin at start_idx."""
    end_token = f"\\end{{{env_name}}}"
    depth = 1
    begin_token = f"\\begin{{{env_name}}}"
    for i in range(start_idx + 1, len(lines)):
        # Count nesting (rare but possible)
        if begin_token in lines[i]:
            depth += 1
        if end_token in lines[i]:
            depth -= 1
            if depth == 0:
                return i
    return len(lines) - 1


def extract_claims(path: Path) -> list[Claim]:
    """Extract all tagged claims from a single .tex file."""
    rel_path = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    claims: list[Claim] = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Look for \begin{env}
        begin_match = BEGIN_RE.search(line)
        if not begin_match or begin_match.group(1) not in CLAIM_ENVS:
            i += 1
            continue

        env_name = begin_match.group(1)
        env_start = i
        env_end = find_env_end(lines, i, env_name)

        # Get the full block text
        block_lines = lines[env_start:env_end + 1]
        block_text = "\n".join(block_lines)

        # Check for ClaimStatus
        status_match = STATUS_RE.search(block_text)
        if not status_match:
            i = env_end + 1
            continue

        status = status_match.group(1)

        # Extract optional title from \begin{env}[title; ClaimStatus...]
        title = ""
        opt_match = BEGIN_OPT_RE.search(block_text[:500])  # look in first 500 chars
        if opt_match:
            raw_title = opt_match.group(2)
            # Remove ClaimStatus from title
            raw_title = STATUS_RE.sub("", raw_title).strip()
            # Remove trailing/leading semicolons and whitespace
            raw_title = raw_title.strip("; \t\n")
            title = raw_title

        # Find all labels in this block
        block_labels = LABEL_RE.findall(block_text)

        # Find all refs in this block
        block_refs = []
        for ref_match in REF_RE.finditer(block_text):
            for raw in ref_match.group(1).split(","):
                key = raw.strip()
                if key:
                    block_refs.append(key)

        # Find all citations in this block
        block_cites = []
        for cite_match in CITE_RE.finditer(block_text):
            for raw in cite_match.group(1).split(","):
                key = raw.strip()
                if key:
                    block_cites.append(key)

        # Deduplicate refs and cites
        block_refs = list(dict.fromkeys(block_refs))
        block_cites = list(dict.fromkeys(block_cites))

        # Use the first label as the primary label; if no label, use a synthetic one
        primary_label = block_labels[0] if block_labels else f"__unlabeled_{rel_path}:{env_start + 1}"

        # Find the line of the primary label (for accurate location)
        label_line = env_start + 1  # default: the \begin line (1-indexed)
        for local_idx, local_line in enumerate(block_lines):
            if primary_label in local_line and "\\label{" in local_line:
                label_line = env_start + local_idx + 1
                break

        claim = Claim(
            label=primary_label,
            env_type=env_name,
            status=status,
            file=rel_path,
            line=label_line,
            title=title,
            labels_in_block=block_labels if len(block_labels) > 1 else [],
            refs_in_block=block_refs,
            cites_in_block=block_cites,
        )
        claims.append(claim)

        i = env_end + 1

    return claims


def extract_all_labels(path: Path) -> list[LabelEntry]:
    """Extract all \\label{} occurrences from a file."""
    rel_path = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    entries: list[LabelEntry] = []

    for i, line in enumerate(lines):
        for match in LABEL_RE.finditer(line):
            label = match.group(1)
            entries.append(LabelEntry(
                label=label,
                file=rel_path,
                line=i + 1,
            ))

    return entries


def extract_all_refs(path: Path) -> list[tuple[str, str, int]]:
    """Extract all \\ref{} occurrences: (label, file, line)."""
    rel_path = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    refs: list[tuple[str, str, int]] = []

    for i, line in enumerate(lines):
        for match in REF_RE.finditer(line):
            for raw in match.group(1).split(","):
                key = raw.strip()
                if key:
                    refs.append((key, rel_path, i + 1))

    return refs


# ---------------------------------------------------------------------------
# Output generation
# ---------------------------------------------------------------------------

def write_claims_jsonl(claims: list[Claim]) -> None:
    """Write metadata/claims.jsonl — one JSON line per claim."""
    out_path = METADATA_DIR / "claims.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for claim in claims:
            f.write(json.dumps(claim.to_dict(), ensure_ascii=False) + "\n")
    print(f"  claims.jsonl: {len(claims)} claims")


def raw_grep_counts(all_files: list[Path]) -> dict[str, int]:
    """Count raw occurrences of \\ClaimStatus* strings (matches legacy grep method)."""
    counts: dict[str, int] = defaultdict(int)
    for path in all_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in STATUS_RE.finditer(text):
            counts[match.group(1)] += 1
    return dict(counts)


def write_census_json(claims: list[Claim], all_files: list[Path]) -> None:
    """Write metadata/census.json — single source of truth for counts."""
    status_counts: Counter[str] = Counter()
    for claim in claims:
        status_counts[claim.status] += 1

    # Raw grep counts for comparison (matches the CLAUDE.md methodology)
    grep_counts = raw_grep_counts(all_files)

    # Line counts by part
    part_lines: dict[str, int] = {}
    for part_name, pattern in [
        ("theory", "chapters/theory/"),
        ("examples", "chapters/examples/"),
        ("connections", "chapters/connections/"),
        ("appendices", "appendices/"),
    ]:
        total = 0
        for f in all_files:
            rel = f.relative_to(ROOT).as_posix()
            if rel.startswith(pattern):
                total += sum(1 for _ in open(f, encoding="utf-8", errors="ignore"))
        part_lines[part_name] = total

    total_lines = sum(part_lines.values())

    # Claims by part
    claims_by_part: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for claim in claims:
        for part_name, pattern in [
            ("theory", "chapters/theory/"),
            ("examples", "chapters/examples/"),
            ("connections", "chapters/connections/"),
            ("appendices", "appendices/"),
        ]:
            if claim.file.startswith(pattern):
                claims_by_part[part_name][claim.status] += 1
                break

    # Claims by file
    claims_by_file: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for claim in claims:
        claims_by_file[claim.file][claim.status] += 1

    census = {
        "date": date.today().isoformat(),
        "totals": {
            "ProvedHere": status_counts.get("ProvedHere", 0),
            "ProvedElsewhere": status_counts.get("ProvedElsewhere", 0),
            "Conjectured": status_counts.get("Conjectured", 0),
            "Heuristic": status_counts.get("Heuristic", 0),
            "Open": status_counts.get("Open", 0),
            "total_claims": len(claims),
        },
        "raw_grep_counts": {
            "_note": "Raw string occurrences (includes inline mentions in remarks/proofs). Higher than structured count.",
            "ProvedHere": grep_counts.get("ProvedHere", 0),
            "ProvedElsewhere": grep_counts.get("ProvedElsewhere", 0),
            "Conjectured": grep_counts.get("Conjectured", 0),
            "Heuristic": grep_counts.get("Heuristic", 0),
            "Open": grep_counts.get("Open", 0),
            "total_occurrences": sum(grep_counts.values()),
        },
        "lines": {
            "total": total_lines,
            **part_lines,
        },
        "by_part": {k: dict(v) for k, v in claims_by_part.items()},
        "by_file": {k: dict(v) for k, v in sorted(claims_by_file.items())},
    }

    out_path = METADATA_DIR / "census.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(census, f, indent=2, ensure_ascii=False)
    print(f"  census.json: PH={census['totals']['ProvedHere']} "
          f"PE={census['totals']['ProvedElsewhere']} "
          f"CJ={census['totals']['Conjectured']} "
          f"H={census['totals']['Heuristic']} "
          f"O={census['totals']['Open']} "
          f"total={census['totals']['total_claims']}")


def write_dependency_graph(claims: list[Claim], all_labels: dict[str, LabelEntry]) -> None:
    """Write metadata/dependency_graph.dot — theorem dependency DAG."""
    # Build set of claim labels for filtering
    claim_labels = {c.label for c in claims}
    # Also include secondary labels from multi-label blocks
    for c in claims:
        for lab in c.labels_in_block:
            claim_labels.add(lab)

    # Map secondary labels to primary
    label_to_primary: dict[str, str] = {}
    for c in claims:
        label_to_primary[c.label] = c.label
        for lab in c.labels_in_block:
            label_to_primary[lab] = c.label

    out_path = METADATA_DIR / "dependency_graph.dot"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("digraph theorem_dependencies {\n")
        f.write("  rankdir=TB;\n")
        f.write("  node [shape=box, fontsize=9, fontname=\"Helvetica\"];\n")
        f.write("  edge [fontsize=7];\n\n")

        # Color nodes by status
        status_colors = {
            "ProvedHere": "#c8e6c9",      # green
            "ProvedElsewhere": "#bbdefb",  # blue
            "Conjectured": "#fff9c4",      # yellow
            "Heuristic": "#ffccbc",        # orange
            "Open": "#ef9a9a",             # red
        }

        # Color nodes by part
        part_colors = {
            "chapters/theory/": "#e8eaf6",
            "chapters/examples/": "#e0f2f1",
            "chapters/connections/": "#fce4ec",
            "appendices/": "#f3e5f5",
        }

        for claim in claims:
            color = status_colors.get(claim.status, "#ffffff")
            safe_label = claim.label.replace(":", "_").replace("-", "_")
            short_title = claim.title[:40] + "..." if len(claim.title) > 40 else claim.title
            display = f"{claim.label}\\n{claim.env_type} [{claim.status[:2]}]"
            if short_title:
                display += f"\\n{short_title}"
            f.write(f'  {safe_label} [label="{display}", style=filled, fillcolor="{color}"];\n')

        f.write("\n")

        # Edges: claim -> refs that are also claims
        for claim in claims:
            src = claim.label.replace(":", "_").replace("-", "_")
            for ref in claim.refs_in_block:
                primary = label_to_primary.get(ref)
                if primary and primary != claim.label:
                    dst = primary.replace(":", "_").replace("-", "_")
                    f.write(f"  {src} -> {dst};\n")

        f.write("}\n")

    # Count edges
    edge_count = sum(
        1 for c in claims
        for r in c.refs_in_block
        if label_to_primary.get(r) and label_to_primary.get(r) != c.label
    )
    print(f"  dependency_graph.dot: {len(claims)} nodes, {edge_count} edges")


def write_label_index(all_labels: dict[str, LabelEntry]) -> None:
    """Write metadata/label_index.json — all labels with locations."""
    index = {}
    for label, entry in sorted(all_labels.items()):
        index[label] = {
            "file": entry.file,
            "line": entry.line,
        }
        if entry.env_type:
            index[label]["env_type"] = entry.env_type

    out_path = METADATA_DIR / "label_index.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f"  label_index.json: {len(index)} labels")


def write_verified_formulas() -> None:
    """Write metadata/verified_formulas.jsonl from CLAUDE.md pitfalls.

    These are hand-curated facts that agents must not contradict.
    Generated once, then maintained manually.
    """
    formulas = [
        # Grading and Conventions
        {"id": "VF001", "domain": "grading", "correct": "Cohomological grading: |d| = +1",
         "wrong": "|d| = -1 (homological)", "source": "CLAUDE.md, LV12 convention diff", "violations": 2},
        {"id": "VF002", "domain": "grading", "correct": "Bar uses desuspension: B(A) = T^c(s^{-1}A-bar, d)",
         "wrong": "B(A) = T^c(sA-bar, d) (suspension)", "source": "CLAUDE.md", "violations": 2},
        {"id": "VF003", "domain": "grading", "correct": "Suspension: sV = V[-1] under V[n]^k = V^{k+n}",
         "wrong": "sV = V[+1]", "source": "CLAUDE.md", "violations": 1},

        # Koszul Duality
        {"id": "VF010", "domain": "koszul", "correct": "Com^! = Lie (NOT coLie)",
         "wrong": "Com^! = coLie", "source": "LV12 Thm 7.6.5", "violations": 5},
        {"id": "VF011", "domain": "koszul", "correct": "Sym^! = Lambda (exterior, NOT commutative again)",
         "wrong": "Sym^! = Sym", "source": "LV12", "violations": 1},
        {"id": "VF012", "domain": "koszul", "correct": "Koszul dual coalgebra = SUB-coalgebra of cofree (cogenerated by R^perp)",
         "wrong": "Quotient of cofree", "source": "LV12 Ch 7", "violations": 5},
        {"id": "VF013", "domain": "koszul", "correct": "Heisenberg: H^! = Sym^ch(V*) (commutative chiral)",
         "wrong": "H^! = H_{-kappa} (self-dual)", "source": "free_fields.tex:thm:heisenberg-koszul-dual", "violations": 3},
        {"id": "VF014", "domain": "koszul", "correct": "Free fermion: F^! = beta-gamma (Lie<->Com duality)",
         "wrong": "F^! = Heisenberg", "source": "free_fields.tex", "violations": 3},
        {"id": "VF015", "domain": "koszul", "correct": "bc-betagamma is a 2-generator duality (dim V=2)",
         "wrong": "bc dual is Heisenberg", "source": "free_fields.tex", "violations": 2},
        {"id": "VF016", "domain": "koszul", "correct": "Bosonization != Koszul duality (bc has 2 generators, H has 1)",
         "wrong": "Bosonization = Koszul duality", "source": "CLAUDE.md", "violations": 2},

        # P-infinity vs Coisson
        {"id": "VF020", "domain": "quantization", "correct": "P_infty-chiral != Coisson. Coisson has NO OPE.",
         "wrong": "P_infty-chiral = Coisson", "source": "CLAUDE.md", "violations": 2},
        {"id": "VF021", "domain": "quantization",
         "correct": "Coisson = PVA = commutative D_X-algebra + Lie* bracket. NOT a chiral algebra.",
         "wrong": "Coisson is a chiral algebra", "source": "CLAUDE.md", "violations": 2},

        # Central Charges and Levels
        {"id": "VF030", "domain": "levels", "correct": "Sugawara: c = k*dim(g)/(k+h^dual). UNDEFINED at k = -h^dual.",
         "wrong": "c diverges at k = -h^dual", "source": "Kac, CLAUDE.md", "violations": 1},
        {"id": "VF031", "domain": "levels", "correct": "Feigin-Frenkel involution: k <-> -k-2h^dual",
         "wrong": "k <-> -k-h^dual", "source": "CLAUDE.md", "violations": 2},
        {"id": "VF032", "domain": "levels", "correct": "Virasoro DS: c = 1 - 6(k+1)^2/(k+2)",
         "wrong": "Other parametrization", "source": "w_algebras_framework.tex", "violations": 0},
        {"id": "VF033", "domain": "levels", "correct": "W_3 DS: c = 2 - 24(k+2)^2/(k+3)",
         "wrong": "Other parametrization", "source": "w_algebras_framework.tex", "violations": 0},
        {"id": "VF034", "domain": "levels",
         "correct": "KM periodicity: 2h (Coxeter), NOT 2h^dual (dual Coxeter). Differ for non-simply-laced.",
         "wrong": "Period = 2h^dual", "source": "CLAUDE.md", "violations": 2},
        {"id": "VF035", "domain": "levels",
         "correct": "KM periodicity rank>1: NOT uniform. sl_2 is 4-periodic but sl_3 is NOT 6-periodic.",
         "wrong": "All KM algebras are 2h-periodic", "source": "CLAUDE.md", "violations": 1},
        {"id": "VF036", "domain": "levels",
         "correct": "FF dual of admissible level is NOT admissible. k'=-h^dual-p/q fails admissibility.",
         "wrong": "Admissible dual is admissible", "source": "CLAUDE.md", "violations": 2},

        # Curved A-infinity
        {"id": "VF040", "domain": "curved", "correct": "m_1^2(a) = m_2(m_0,a) - m_2(a,m_0) = [m_0,a] (COMMUTATOR, MINUS)",
         "wrong": "m_1^2(a) = m_2(m_0,a) + m_2(a,m_0)", "source": "CLAUDE.md, LV12", "violations": 1},
        {"id": "VF041", "domain": "curved", "correct": "Bar differential always d^2=0; curvature shows as m_1^2 != 0",
         "wrong": "d^2 != 0 for curved case", "source": "CLAUDE.md", "violations": 1},

        # Geometry
        {"id": "VF050", "domain": "geometry", "correct": "FM compactification: C-bar_n(X) = Bl (blowup along diags), NOT X^n \\ Delta",
         "wrong": "FM = complement of diagonals", "source": "BD04, CLAUDE.md", "violations": 1},
        {"id": "VF051", "domain": "geometry", "correct": "M-bar_{0,5} = Bl_4(P^2) (del Pezzo deg 5), dim H^2 = 5",
         "wrong": "M-bar_{0,5} = P^2", "source": "CLAUDE.md", "violations": 1},
        {"id": "VF052", "domain": "geometry", "correct": "Prime form E(z,w) is section of K^{-1/2} boxtimes K^{-1/2}",
         "wrong": "E(z,w) in K^{+1/2}", "source": "CLAUDE.md, Fay", "violations": 1},
        {"id": "VF053", "domain": "geometry", "correct": "Normal bundle N_{Delta_S/X^n} = direct-sum T_X (tangent, NOT cotangent)",
         "wrong": "N = T_X* (cotangent)", "source": "CLAUDE.md", "violations": 0},
        {"id": "VF054", "domain": "geometry", "correct": "Vol(M-bar_g) ~ (2g)! (Mirzakhani), NOT e^{Cg}",
         "wrong": "Vol ~ e^{Cg}", "source": "Mirzakhani", "violations": 0},

        # Physics
        {"id": "VF060", "domain": "physics", "correct": "QME: hbar*Delta*S + (1/2){S,S} = 0 (factor 1/2)",
         "wrong": "hbar*Delta*S + {S,S} = 0 (missing 1/2)", "source": "CG17", "violations": 0},
        {"id": "VF061", "domain": "physics", "correct": "Virasoro central extension is Lie algebra 2-COCYCLE (not 3-cocycle)",
         "wrong": "3-cocycle", "source": "Kac", "violations": 0},
        {"id": "VF062", "domain": "physics",
         "correct": "W_3 composite: Lambda = :TT: - (3/10)partial^2 T (MINUS sign)",
         "wrong": "Lambda = :TT: + (3/10)partial^2 T", "source": "w3_composite_fields.tex", "violations": 0},

        # Anti-patterns (higher level)
        {"id": "VF070", "domain": "anti-pattern",
         "correct": "Bar-cobar QI does NOT imply D^b(A-mod) ~ D^b(A!-mod). Need Positselski D^co/D^ctr.",
         "wrong": "D^b(A-mod) ~ D^b(A!-mod) from bar-cobar", "source": "Positselski", "violations": 2},
        {"id": "VF071", "domain": "anti-pattern",
         "correct": "Genus expansion F_g extracts ONE tautological intersection number, NOT physical partition function.",
         "wrong": "F_g = Z_g (partition function)", "source": "CLAUDE.md", "violations": 2},
        {"id": "VF072", "domain": "anti-pattern",
         "correct": "Ghost c=26 is a HYPOTHESIS (d^2=0 requires it), not a CONCLUSION of Koszul duality.",
         "wrong": "c=26 is a Koszul-theoretic conclusion", "source": "CLAUDE.md", "violations": 2},
        {"id": "VF073", "domain": "anti-pattern",
         "correct": "kappa(A) does NOT determine A up to isomorphism. Many algebras share same kappa.",
         "wrong": "kappa determines A", "source": "CLAUDE.md", "violations": 1},
        {"id": "VF074", "domain": "anti-pattern",
         "correct": "CH* periodicity of A does NOT imply periodicity of CH*(A!) via Koszul duality alone.",
         "wrong": "Periodicity transfers under Koszul duality", "source": "CLAUDE.md", "violations": 2},
    ]

    out_path = METADATA_DIR / "verified_formulas.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for formula in formulas:
            f.write(json.dumps(formula, ensure_ascii=False) + "\n")
    print(f"  verified_formulas.jsonl: {len(formulas)} formulas")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Generating metadata for chiral-bar-cobar monograph...")
    print(f"  Root: {ROOT}")

    # Ensure output directory exists
    METADATA_DIR.mkdir(exist_ok=True)

    # Get files
    active_files = get_active_files()
    all_tex_files = get_all_tex_files()
    print(f"  Active files (in main.tex): {len(active_files)}")
    print(f"  All .tex files: {len(all_tex_files)}")

    # Extract claims from all tex files
    all_claims: list[Claim] = []
    for path in all_tex_files:
        file_claims = extract_claims(path)
        all_claims.extend(file_claims)

    # Extract all labels
    all_labels: dict[str, LabelEntry] = {}
    for path in all_tex_files:
        for entry in extract_all_labels(path):
            if entry.label not in all_labels:  # first occurrence wins
                all_labels[entry.label] = entry

    print(f"\n  Extracted {len(all_claims)} tagged claims from {len(all_tex_files)} files")

    # Write outputs
    print(f"\nWriting metadata to {METADATA_DIR}/")
    write_claims_jsonl(all_claims)
    write_census_json(all_claims, all_tex_files)
    write_dependency_graph(all_claims, all_labels)
    write_label_index(all_labels)
    write_verified_formulas()

    print(f"\nDone. Run 'make metadata' to regenerate.")


if __name__ == "__main__":
    main()
