#!/usr/bin/env python3
"""Generate a full Volume I mathematical fault catalogue.

This exporter focuses on mathematical / claim-surface integrity, not prose.
It aggregates:
  - current claim metadata
  - the Beilinson proof-chain auditor
  - archived red-team ledgers (Volume I filtered)
  - current doctrine/QC drift surfaces relevant to mathematics
  - source-validated manual findings from a direct read of high-risk claims

Outputs:
  compute/audit/vol1_full_audit_<date>/
    CATALOGUE.md
    counts.json
    manual_findings.json
    auditor_findings.csv
    auditor_bottlenecks.csv
    auditor_uncovered_provedhere.csv
    archive_v1_high_critical_claims.csv
    archive_v1_frontier_claims.csv
    archive_v1_suspicious_proved_dependencies.csv
    archive_label_status_conflicts_touching_v1.csv
    local_duplicate_labels.csv
    duplicate_title_clusters.csv
    qc_math_surfaces.json
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, is_dataclass
from datetime import date
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_DIR = REPO_ROOT / "archive" / "raeeznotes" / "raeeznotes100"
DEFAULT_OUT_DIR = REPO_ROOT / "compute" / "audit" / f"vol1_full_audit_{date.today().isoformat().replace('-', '_')}"

if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compute.lib.beilinson_auditor import BeilinsonAuditor, STATUS_NAME, SEVERITY_ORDER


def load_manuscript_qc_module():
    path = REPO_ROOT / "scripts" / "manuscript_qc.py"
    spec = importlib.util.spec_from_file_location("manuscript_qc", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def mkdirp(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", (title or "").strip().lower())


def read_claims() -> list[dict[str, Any]]:
    claims: list[dict[str, Any]] = []
    with (REPO_ROOT / "metadata" / "claims.jsonl").open() as fh:
        for line in fh:
            if line.strip():
                claims.append(json.loads(line))
    return claims


def write_json(path: Path, data: Any) -> None:
    with path.open("w") as fh:
        json.dump(data, fh, indent=2, sort_keys=True)


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if fieldnames is None:
        keys: set[str] = set()
        for row in rows:
            keys.update(row.keys())
        fieldnames = sorted(keys)
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def serialize_obj(obj: Any) -> Any:
    if is_dataclass(obj):
        data = asdict(obj)
        for key, value in list(data.items()):
            if isinstance(value, Path):
                data[key] = str(value)
        return data
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, tuple):
        return [serialize_obj(x) for x in obj]
    if isinstance(obj, list):
        return [serialize_obj(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): serialize_obj(v) for k, v in obj.items()}
    return obj


def extract_claim_index(claims: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {claim["label"]: claim for claim in claims if claim.get("label")}


def build_archive_exports() -> dict[str, list[dict[str, Any]]]:
    exports: dict[str, list[dict[str, Any]]] = {}

    with (ARCHIVE_DIR / "master_claim_ledger_filtered.csv").open() as fh:
        rows = list(csv.DictReader(fh))
    exports["archive_v1_high_critical_claims"] = [
        row for row in rows
        if row.get("volume") == "V1" and row.get("risk") in {"high", "critical"}
    ]
    exports["archive_v1_frontier_claims"] = [
        row for row in rows
        if row.get("volume") == "V1" and row.get("status") in {"Conjectured", "Conditional", "Heuristic", "Open"}
    ]

    with (ARCHIVE_DIR / "suspicious_proved_claim_dependencies.csv").open() as fh:
        exports["archive_v1_suspicious_proved_dependencies"] = [
            row for row in csv.DictReader(fh) if row.get("volume") == "V1"
        ]

    with (ARCHIVE_DIR / "label_status_conflicts.csv").open() as fh:
        rows = []
        for row in csv.DictReader(fh):
            instances = row.get("instances", "")
            if "V1:" in instances:
                rows.append(row)
        exports["archive_label_status_conflicts_touching_v1"] = rows

    return exports


def build_local_duplicate_exports(claims: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    by_label: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_title: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for claim in claims:
        by_label[claim["label"]].append(claim)
        norm_title = normalize_title(claim.get("title", ""))
        if norm_title:
            by_title[norm_title].append(claim)

    duplicate_labels: list[dict[str, Any]] = []
    for label, rows in sorted(by_label.items()):
        if len(rows) <= 1:
            continue
        statuses = sorted({row["status"] for row in rows})
        duplicate_labels.append(
            {
                "label": label,
                "count": len(rows),
                "statuses": ";".join(statuses),
                "instances": " || ".join(
                    f"{row['file']}:{row['line']}:{row['status']}:{row.get('title','')}"
                    for row in rows
                ),
            }
        )

    duplicate_titles: list[dict[str, Any]] = []
    for norm_title, rows in sorted(by_title.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        files = {row["file"] for row in rows}
        if len(rows) <= 1 or len(files) <= 1:
            continue
        duplicate_titles.append(
            {
                "normalized_title": norm_title,
                "count": len(rows),
                "labels": ";".join(sorted({row["label"] for row in rows})),
                "statuses": ";".join(sorted({row["status"] for row in rows})),
                "instances": " || ".join(
                    f"{row['label']}@{row['file']}:{row['line']}:{row['status']}"
                    for row in rows
                ),
            }
        )

    return {
        "local_duplicate_labels": duplicate_labels,
        "duplicate_title_clusters": duplicate_titles,
    }


def build_manual_findings() -> list[dict[str, Any]]:
    return [
        {
            "severity": "CRITICAL",
            "title": "Principal W-duality surface is internally contradictory",
            "summary": (
                "The main principal-duality theorem states an actual equivalence "
                "(W^k)^! ≃ W^{k'}, while the later 'precise statement' says the "
                "dual is not W^{k'} itself, only a chiral CE algebra with the same kappa. "
                "This is a foundational inversion-vs-dual conflation."
            ),
            "evidence": [
                {"file": "chapters/examples/w_algebras.tex", "line": 316, "label": "thm:w-algebra-koszul-main"},
                {"file": "chapters/examples/w_algebras.tex", "line": 1201, "label": "thm:w-koszul-precise"},
                {"file": "chapters/examples/w_algebras.tex", "line": 1218, "label": "thm:w-koszul-precise"},
                {"file": "chapters/connections/concordance.tex", "line": 28, "label": "thm:higher-genus-inversion"},
            ],
        },
        {
            "severity": "CRITICAL",
            "title": "W precise statement leaves its general-level claim unproved",
            "summary": (
                "The proof of thm:w-koszul-precise proves the critical-level package "
                "and skips Part B. The theorem still asserts a general-level statement, "
                "so the claim surface currently outruns the written proof."
            ),
            "evidence": [
                {"file": "chapters/examples/w_algebras.tex", "line": 1214, "label": "thm:w-koszul-precise"},
                {"file": "chapters/examples/w_algebras.tex", "line": 1228, "label": "thm:w-koszul-precise"},
            ],
        },
        {
            "severity": "CRITICAL",
            "title": "Explicit theta theorem overclaims beyond the proved scalar lane",
            "summary": (
                "thm:explicit-theta asserts the full kappa·eta⊗Lambda formula under "
                "a one-channel hypothesis, but later results and concordance explicitly "
                "restrict that formula to the proved uniform-weight lane and record "
                "failure of tautological purity in multi-weight settings."
            ),
            "evidence": [
                {"file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 3777, "label": "thm:explicit-theta"},
                {"file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 7404, "label": "cor:scalar-saturation"},
                {"file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 13735, "label": "thm:theta-direct-derivation"},
                {"file": "chapters/connections/concordance.tex", "line": 9394, "label": "concordance-multi-weight-diagnosis"},
            ],
        },
        {
            "severity": "SERIOUS",
            "title": "Sub-exponential growth is not automatic from positive energy alone",
            "summary": (
                "prop:subexponential-growth-automatic assumes only positive energy and "
                "finite-dimensional graded pieces, then imports Hardy-Ramanujan-Rademacher/"
                "effective-central-charge asymptotics. Those asymptotics need much stronger "
                "modularity/character-control input, so the proposition is overstated."
            ),
            "evidence": [
                {"file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 3781, "label": "prop:subexponential-growth-automatic"},
                {"file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 3811, "label": "prop:subexponential-growth-automatic"},
                {"file": "chapters/connections/concordance.tex", "line": 6702, "label": "concordance-factorization-finiteness-reduction"},
            ],
        },
        {
            "severity": "SERIOUS",
            "title": "Yangian duality proof only controls leading-order / low-rank data",
            "summary": (
                "thm:yangian-koszul-dual is stated as an exact RTT duality theorem, but the proof "
                "leans on a 16x16 sl2 orthogonal-complement computation and then declares higher "
                "R^{-1} coefficients irrelevant because the mode expansion sees only leading-order data. "
                "That does not justify the full algebra-level identification."
            ),
            "evidence": [
                {"file": "chapters/examples/yangians_foundations.tex", "line": 501, "label": "thm:yangian-koszul-dual"},
                {"file": "chapters/examples/yangians_foundations.tex", "line": 545, "label": "thm:yangian-koszul-dual"},
                {"file": "chapters/examples/yangians_foundations.tex", "line": 557, "label": "thm:yangian-koszul-dual"},
            ],
        },
        {
            "severity": "SERIOUS",
            "title": "Derived W3 duality theorem inherits the contradictory W-duality surface",
            "summary": (
                "thm:w3-koszul-dual imports the principal W-duality theorem as if it proved "
                "(W_3^k)^! ≃ W_3^{k'}. Since the parent theorem surface is internally contradictory, "
                "the specialized W3 theorem is downstream-fragile as written."
            ),
            "evidence": [
                {"file": "chapters/examples/w_algebras.tex", "line": 1869, "label": "thm:w3-koszul-dual"},
                {"file": "chapters/examples/w_algebras.tex", "line": 1897, "label": "thm:w3-koszul-dual"},
                {"file": "chapters/examples/w_algebras.tex", "line": 1218, "label": "thm:w-koszul-precise"},
            ],
        },
    ]


def claims_rows_for_labels(labels: list[str], claim_index: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for label in labels:
        claim = claim_index.get(label)
        if not claim:
            rows.append({"label": label})
            continue
        rows.append(
            {
                "label": label,
                "file": claim.get("file", ""),
                "line": claim.get("line", ""),
                "status": claim.get("status", ""),
                "env_type": claim.get("env_type", ""),
                "title": claim.get("title", ""),
            }
        )
    return rows


def collect_qc_math_surfaces() -> tuple[dict[str, list[dict[str, Any]]], dict[str, int]]:
    qc_mod = load_manuscript_qc_module()
    data = qc_mod.scan()

    math_keys = [
        "untagged",
        "prior_version",
        "ambiguous_status",
        "virasoro_shadow_drift",
        "infinite_generator_drift",
        "dk_scope_drift",
        "periodicity_profile_drift",
        "kl_scope_drift",
        "periodicity_overclaim_drift",
        "package_scope_drift",
        "mc2_frontier_drift",
        "mc2_verdier_drift",
        "mc2_ptvv_lift_drift",
        "mc2_chain_model_drift",
        "mc2_seed_drift",
        "mc2_seed_packet_drift",
        "mc2_visible_lowarity_drift",
        "mc2_transfer_package_drift",
        "mc2_transfer_law_drift",
        "mc2_chart_drift",
        "mc2_line_detection_drift",
        "mc2_automorphism_rigidity_drift",
        "mc2_stabilizer_drift",
        "mc2_incidence_orbit_drift",
        "mc2_orbit_table_drift",
        "mc2_universal_table_drift",
        "mc2_invariant_signature_drift",
        "mc2_seed_character_drift",
        "mc2_twosign_scalar_drift",
        "mc2_parity_scalar_drift",
        "mc2_parity_forcing_drift",
        "nonprincipal_packet_drift",
        "en_axis_drift",
        "mc3_wording_drift",
        "mc4_wording_drift",
    ]
    result: dict[str, list[dict[str, Any]]] = {}
    counts: dict[str, int] = {}
    for key in math_keys:
        value = data[key]
        rows = [serialize_obj(item) for item in value]
        result[key] = rows
        counts[key] = len(rows)

    # Duplicate paragraphs and long paragraphs are exposition-adjacent, but
    # duplicate blocks are a real theorem-surface drift vector, so keep only duplicates.
    duplicate_rows: list[dict[str, Any]] = []
    for normalized, paras in data["duplicates"]:
        duplicate_rows.append(
            {
                "normalized_prefix": normalized[:120],
                "count": len(paras),
                "instances": " || ".join(f"{p.path}:{p.line}" for p in paras),
            }
        )
    result["duplicate_paragraph_clusters"] = duplicate_rows
    counts["duplicate_paragraph_clusters"] = len(duplicate_rows)
    return result, counts


def build_auditor_exports(claim_index: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
    auditor = BeilinsonAuditor(str(REPO_ROOT))
    report = auditor.run_audit()

    findings_rows: list[dict[str, Any]] = []
    for finding in report.findings:
        row = serialize_obj(finding)
        claim = claim_index.get(finding.claim_label, {})
        row["title"] = claim.get("title", "")
        row["status"] = claim.get("status", "")
        row["env_type"] = claim.get("env_type", "")
        findings_rows.append(row)

    bottleneck_rows: list[dict[str, Any]] = []
    for label, count in report.bottlenecks:
        claim = claim_index.get(label, {})
        eff = report.effective_strength.get(label, claim.get("strength", -1))
        bottleneck_rows.append(
            {
                "label": label,
                "downstream_dependents": count,
                "file": claim.get("file", ""),
                "line": claim.get("line", ""),
                "status": claim.get("status", ""),
                "title": claim.get("title", ""),
                "tested": label in report.test_coverage,
                "effective_strength": STATUS_NAME.get(eff, eff),
                "weakest_link": report.weakest_links.get(label, ""),
            }
        )

    summary = {
        "total_claims": report.total_claims,
        "statement_edges": report.statement_edges,
        "proof_edges": report.proof_edges,
        "proof_claims_found": report.proof_claims_found,
        "root_count": report.root_count,
        "layer_count": report.layer_count,
        "genuine_cycles": len(report.genuine_cycles),
        "forward_ref_cycles": len(report.forward_ref_cycles),
        "bottleneck_count": len(report.bottlenecks),
        "coverage_count": len(report.test_coverage),
        "uncovered_provedhere_count": len(report.uncovered_proved),
        "findings_by_severity": dict(Counter(f.severity for f in report.findings)),
        "findings_by_anti_pattern": dict(Counter(f.anti_pattern for f in report.findings)),
    }

    exports = {
        "auditor_findings": findings_rows,
        "auditor_bottlenecks": bottleneck_rows,
        "auditor_uncovered_provedhere": claims_rows_for_labels(report.uncovered_proved, claim_index),
    }
    return summary, exports


def build_counts(
    claims: list[dict[str, Any]],
    archive_exports: dict[str, list[dict[str, Any]]],
    duplicate_exports: dict[str, list[dict[str, Any]]],
    qc_counts: dict[str, int],
    auditor_summary: dict[str, Any],
) -> dict[str, Any]:
    statuses = Counter(claim["status"] for claim in claims)
    envs = Counter(claim["env_type"] for claim in claims)
    top_files = Counter(claim["file"] for claim in claims)

    return {
        "claims": {
            "total": len(claims),
            "statuses": dict(statuses),
            "env_types": dict(envs),
            "top_files": dict(top_files.most_common(25)),
        },
        "archive": {
            "v1_high_critical_count": len(archive_exports["archive_v1_high_critical_claims"]),
            "v1_frontier_count": len(archive_exports["archive_v1_frontier_claims"]),
            "v1_suspicious_proved_dependencies_count": len(archive_exports["archive_v1_suspicious_proved_dependencies"]),
            "label_status_conflicts_touching_v1_count": len(archive_exports["archive_label_status_conflicts_touching_v1"]),
        },
        "duplication": {
            "local_duplicate_labels": len(duplicate_exports["local_duplicate_labels"]),
            "duplicate_title_clusters": len(duplicate_exports["duplicate_title_clusters"]),
        },
        "qc_math": qc_counts,
        "auditor": auditor_summary,
    }


def write_markdown_catalogue(
    out_dir: Path,
    counts: dict[str, Any],
    manual_findings: list[dict[str, Any]],
    archive_exports: dict[str, list[dict[str, Any]]],
    qc_counts: dict[str, int],
    auditor_summary: dict[str, Any],
) -> None:
    def rel(name: str) -> str:
        return f"./{name}"

    lines: list[str] = []
    lines.append("# Volume I Full Mathematical Fault Catalogue")
    lines.append("")
    lines.append(f"Generated on {date.today().isoformat()} from the live Volume I repo plus the archived red-team ledgers.")
    lines.append("")
    lines.append("This catalogue excludes pure exposition/style backlog and focuses on rigor, correctness, claim-surface integrity, proof dependencies, hypothesis discipline, and duplication/drift risks.")
    lines.append("")
    lines.append("## Snapshot")
    lines.append("")
    lines.append(f"- Tagged claims in current Volume I metadata: **{counts['claims']['total']}**")
    lines.append(f"- Current `ProvedHere` claims: **{counts['claims']['statuses'].get('ProvedHere', 0)}**")
    lines.append(f"- Current proof-auditor findings: **{sum(auditor_summary['findings_by_severity'].values())}**")
    lines.append(f"- Current proof-level critical findings: **{auditor_summary['findings_by_severity'].get('CRITICAL', 0)}**")
    lines.append(f"- Current proof-level serious findings: **{auditor_summary['findings_by_severity'].get('SERIOUS', 0)}**")
    lines.append(f"- Current `ProvedHere` claims without compute-test references: **{auditor_summary['uncovered_provedhere_count']}**")
    lines.append(f"- Archived red-team V1 high/critical-risk claims: **{counts['archive']['v1_high_critical_count']}**")
    lines.append(f"- Archived red-team V1 frontier claims: **{counts['archive']['v1_frontier_count']}**")
    lines.append(f"- Archived suspicious proved-here local dependency violations in V1: **{counts['archive']['v1_suspicious_proved_dependencies_count']}**")
    lines.append(f"- Cross-volume label-status conflicts touching V1: **{counts['archive']['label_status_conflicts_touching_v1_count']}**")
    lines.append(f"- Local duplicate labels inside Volume I: **{counts['duplication']['local_duplicate_labels']}**")
    lines.append(f"- Duplicate title clusters across files: **{counts['duplication']['duplicate_title_clusters']}**")
    lines.append("")
    lines.append("## Source-Validated Critical / Serious Findings")
    lines.append("")
    for idx, finding in enumerate(manual_findings, start=1):
        lines.append(f"{idx}. **[{finding['severity']}] {finding['title']}**")
        lines.append(f"   {finding['summary']}")
        lines.append("   Evidence:")
        for ev in finding["evidence"]:
            lines.append(f"   - `{ev['file']}:{ev['line']}` `{ev['label']}`")
        lines.append("")
    lines.append("## Raw Exports")
    lines.append("")
    lines.append(f"- Full proof-auditor findings: [{Path(rel('auditor_findings.csv')).name}]({rel('auditor_findings.csv')})")
    lines.append(f"- Bottleneck claims and test coverage gaps: [{Path(rel('auditor_bottlenecks.csv')).name}]({rel('auditor_bottlenecks.csv')})")
    lines.append(f"- All `ProvedHere` claims without compute-test references: [{Path(rel('auditor_uncovered_provedhere.csv')).name}]({rel('auditor_uncovered_provedhere.csv')})")
    lines.append(f"- Archived V1 high/critical-risk claims: [{Path(rel('archive_v1_high_critical_claims.csv')).name}]({rel('archive_v1_high_critical_claims.csv')})")
    lines.append(f"- Archived V1 frontier claims: [{Path(rel('archive_v1_frontier_claims.csv')).name}]({rel('archive_v1_frontier_claims.csv')})")
    lines.append(f"- Archived suspicious proved-here dependencies: [{Path(rel('archive_v1_suspicious_proved_dependencies.csv')).name}]({rel('archive_v1_suspicious_proved_dependencies.csv')})")
    lines.append(f"- Cross-volume label-status conflicts touching V1: [{Path(rel('archive_label_status_conflicts_touching_v1.csv')).name}]({rel('archive_label_status_conflicts_touching_v1.csv')})")
    lines.append(f"- Local duplicate labels: [{Path(rel('local_duplicate_labels.csv')).name}]({rel('local_duplicate_labels.csv')})")
    lines.append(f"- Duplicate title clusters: [{Path(rel('duplicate_title_clusters.csv')).name}]({rel('duplicate_title_clusters.csv')})")
    lines.append(f"- QC math-surface drift export: [{Path(rel('qc_math_surfaces.json')).name}]({rel('qc_math_surfaces.json')})")
    lines.append(f"- Manual validated findings as JSON: [{Path(rel('manual_findings.json')).name}]({rel('manual_findings.json')})")
    lines.append(f"- Aggregate counts: [{Path(rel('counts.json')).name}]({rel('counts.json')})")
    lines.append("")
    lines.append("## Current Machine-Detected Math Surfaces")
    lines.append("")
    lines.append("### Auditor")
    lines.append("")
    for key in sorted(auditor_summary["findings_by_severity"], key=lambda sev: SEVERITY_ORDER.get(sev, 99)):
        lines.append(f"- `{key}`: {auditor_summary['findings_by_severity'][key]}")
    lines.append("")
    for ap, count in sorted(auditor_summary["findings_by_anti_pattern"].items()):
        lines.append(f"- `{ap}`: {count}")
    lines.append("")
    lines.append("### QC / Doctrine Drift")
    lines.append("")
    nonzero_qc = [(k, v) for k, v in qc_counts.items() if v]
    for key, value in sorted(nonzero_qc):
        lines.append(f"- `{key}`: {value}")
    lines.append("")
    lines.append("## Archive-Derived Highest-Risk File Clusters (V1)")
    lines.append("")
    by_file = Counter(row["file"] for row in archive_exports["archive_v1_high_critical_claims"])
    for file, count in by_file.most_common(20):
        lines.append(f"- `{file}`: {count} archived high/critical claims")
    lines.append("")
    lines.append("## Honesty Clause")
    lines.append("")
    lines.append("This directory is the fullest current catalogue grounded in the repo’s own claim metadata, proof-chain extraction, archive ledgers, QC drift rules, and direct source reads. It is still not logically absolute completeness: untagged or subtly wrong proofs can exist outside these detection surfaces.")
    lines.append("")

    (out_dir / "CATALOGUE.md").write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    mkdirp(out_dir)

    claims = read_claims()
    claim_index = extract_claim_index(claims)
    archive_exports = build_archive_exports()
    duplicate_exports = build_local_duplicate_exports(claims)
    manual_findings = build_manual_findings()
    qc_exports, qc_counts = collect_qc_math_surfaces()
    auditor_summary, auditor_exports = build_auditor_exports(claim_index)
    counts = build_counts(claims, archive_exports, duplicate_exports, qc_counts, auditor_summary)

    write_json(out_dir / "manual_findings.json", manual_findings)
    write_json(out_dir / "qc_math_surfaces.json", qc_exports)
    write_json(out_dir / "counts.json", counts)

    write_csv(out_dir / "auditor_findings.csv", auditor_exports["auditor_findings"])
    write_csv(out_dir / "auditor_bottlenecks.csv", auditor_exports["auditor_bottlenecks"])
    write_csv(out_dir / "auditor_uncovered_provedhere.csv", auditor_exports["auditor_uncovered_provedhere"])
    write_csv(out_dir / "archive_v1_high_critical_claims.csv", archive_exports["archive_v1_high_critical_claims"])
    write_csv(out_dir / "archive_v1_frontier_claims.csv", archive_exports["archive_v1_frontier_claims"])
    write_csv(out_dir / "archive_v1_suspicious_proved_dependencies.csv", archive_exports["archive_v1_suspicious_proved_dependencies"])
    write_csv(out_dir / "archive_label_status_conflicts_touching_v1.csv", archive_exports["archive_label_status_conflicts_touching_v1"])
    write_csv(out_dir / "local_duplicate_labels.csv", duplicate_exports["local_duplicate_labels"])
    write_csv(out_dir / "duplicate_title_clusters.csv", duplicate_exports["duplicate_title_clusters"])
    write_markdown_catalogue(out_dir, counts, manual_findings, archive_exports, qc_counts, auditor_summary)

    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
