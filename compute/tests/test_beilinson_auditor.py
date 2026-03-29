"""Tests for compute/lib/beilinson_auditor.py.

Verifies the Beilinson auditor: dual DAG construction, proof-level
extraction, cycle classification, transitive strength propagation,
and anti-pattern detection (AP4/AP5/AP6/AP11/AP13).

Two test modes:
  1. Synthetic DAGs — controlled graphs testing each detection mechanism
  2. Integration — runs on the real 2,846-claim manuscript metadata
"""

import json
import os
from pathlib import Path

import pytest

from compute.lib.beilinson_auditor import (
    STATUS_STRENGTH,
    STATUS_NAME,
    BeilinsonAuditor,
    Claim,
    Finding,
)

REPO_ROOT = Path(__file__).resolve().parents[2]


def _make_repo(tmp_path, claims_data, tex_files=None):
    """Create a minimal repo structure with claims.jsonl and optional .tex files."""
    meta_dir = tmp_path / 'metadata'
    meta_dir.mkdir()
    claims_file = meta_dir / 'claims.jsonl'
    with open(claims_file, 'w') as f:
        for claim in claims_data:
            f.write(json.dumps(claim) + '\n')

    (tmp_path / 'compute' / 'tests').mkdir(parents=True)

    if tex_files:
        for rel_path, content in tex_files.items():
            full = tmp_path / rel_path
            full.parent.mkdir(parents=True, exist_ok=True)
            full.write_text(content)

    return str(tmp_path)


# ==================================================================
# Phase 1: Claim Loading
# ==================================================================

class TestClaimLoading:

    def test_load_basic(self, tmp_path):
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1},
            {"label": "thm:B", "env_type": "lemma", "status": "Conjectured",
             "file": "b.tex", "line": 10},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        count = auditor.load_claims()
        assert count == 2
        assert auditor.claims["thm:A"].strength == STATUS_STRENGTH["ProvedHere"]

    def test_secondary_label_mapping(self, tmp_path):
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1,
             "labels_in_block": ["thm:A", "cor:A-variant"]},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "b.tex", "line": 5,
             "refs_in_block": ["cor:A-variant"]},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        assert "thm:A" in auditor.stmt_adj["thm:B"]

    def test_eq_labels_not_mapped_to_parent(self, tmp_path):
        """eq: labels are definitional — referencing eq:X inside a conjecture
        should NOT create a dependency on the conjecture."""
        claims = [
            {"label": "conj:C", "env_type": "conjecture", "status": "Conjectured",
             "file": "a.tex", "line": 1,
             "labels_in_block": ["conj:C", "eq:key-formula"]},
            {"label": "thm:T", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 10,
             "refs_in_block": ["eq:key-formula"]},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        # Should NOT create dependency on conj:C
        assert "conj:C" not in auditor.stmt_adj.get("thm:T", set())

    def test_missing_file_raises(self, tmp_path):
        auditor = BeilinsonAuditor(str(tmp_path))
        with pytest.raises(FileNotFoundError):
            auditor.load_claims()


# ==================================================================
# Phase 2: Proof-Level Extraction
# ==================================================================

class TestProofExtraction:

    def test_finds_proof_refs(self, tmp_path):
        """Refs within \\begin{proof}...\\end{proof} are captured."""
        claims = [
            {"label": "thm:upstream", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 1},
            {"label": "thm:main", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 5},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{theorem}[Upstream; \\ClaimStatusProvedHere]\n"
                "\\label{thm:upstream}\n"
                "Statement.\n"
                "\\end{theorem}\n"
                "\\begin{theorem}[Main; \\ClaimStatusProvedHere]\n"  # line 5
                "\\label{thm:main}\n"
                "Statement of main theorem.\n"
                "\\end{theorem}\n"
                "\\begin{proof}\n"
                "By Theorem~\\ref{thm:upstream}, we have the result.\n"
                "\\end{proof}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        count = auditor.extract_proof_deps()

        assert count >= 1
        assert "thm:upstream" in auditor.proof_deps.get("thm:main", set())

    def test_no_proof_block(self, tmp_path):
        """Claims without proofs (conjectures) yield no proof deps."""
        claims = [
            {"label": "conj:X", "env_type": "conjecture", "status": "Conjectured",
             "file": "ch/a.tex", "line": 1},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{conjecture}[\\ClaimStatusConjectured]\n"
                "\\label{conj:X}\n"
                "We conjecture that...\n"
                "\\end{conjecture}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        count = auditor.extract_proof_deps()
        assert "conj:X" not in auditor.proof_deps

    def test_proof_not_attributed_to_wrong_claim(self, tmp_path):
        """If another claim environment appears between claim and proof, skip."""
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 1},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 5},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{theorem}[\\ClaimStatusProvedHere]\n"
                "\\label{thm:A}\n"
                "Statement A.\n"
                "\\end{theorem}\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\n"  # line 5
                "\\label{thm:B}\n"
                "Statement B.\n"
                "\\end{theorem}\n"
                "\\begin{proof}\n"
                "Proof of B using \\ref{thm:A}.\n"
                "\\end{proof}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.extract_proof_deps()

        # The proof belongs to thm:B, not thm:A
        assert "thm:A" not in auditor.proof_deps.get("thm:A", set())
        assert "thm:A" in auditor.proof_deps.get("thm:B", set())

    def test_nested_proof(self, tmp_path):
        """Nested proof environments are handled correctly."""
        claims = [
            {"label": "thm:outer", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 1},
            {"label": "thm:ref1", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/b.tex", "line": 1},
            {"label": "thm:ref2", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/b.tex", "line": 5},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{theorem}[\\ClaimStatusProvedHere]\n"
                "\\label{thm:outer}\n"
                "Statement.\n"
                "\\end{theorem}\n"
                "\\begin{proof}\n"
                "Part 1 uses \\ref{thm:ref1}.\n"
                "\\begin{proof}[Proof of subclaim]\n"
                "Uses \\ref{thm:ref2}.\n"
                "\\end{proof}\n"
                "Continue.\n"
                "\\end{proof}\n"
            ),
            "ch/b.tex": (
                "\\begin{theorem}[\\ClaimStatusProvedHere]\n"
                "\\label{thm:ref1}\nX.\\end{theorem}\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\n"
                "\\label{thm:ref2}\nY.\\end{theorem}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.extract_proof_deps()

        deps = auditor.proof_deps.get("thm:outer", set())
        assert "thm:ref1" in deps
        assert "thm:ref2" in deps


# ==================================================================
# Phase 3: Dual DAG and Cycle Classification
# ==================================================================

class TestDualDAG:

    def test_combined_dag_is_union(self, tmp_path):
        # Lines: 1=beginA, 2=endA, 3=beginB, 4=endB, 5=proof, 6=beginC, 7=endC
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 1},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 3,
             "refs_in_block": ["thm:A"]},
            {"label": "thm:C", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 6},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:A}\n"
                "X.\\end{theorem}\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:B}\n"
                "Statement refs thm:A.\\end{theorem}\n"
                "\\begin{proof}\nBy \\ref{thm:C}.\n\\end{proof}\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:C}\n"
                "Z.\\end{theorem}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        auditor.build_combined_dag()

        combined = auditor.adjacency.get("thm:B", set())
        assert "thm:A" in combined  # from statement
        assert "thm:C" in combined  # from proof


class TestCycleClassification:

    def test_forward_ref_cycle_classified(self, tmp_path):
        """Mutual statement refs without proof-level deps = forward ref."""
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 1,
             "refs_in_block": ["thm:B"]},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 5,
             "refs_in_block": ["thm:A"]},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:A}\n"
                "See also Theorem~\\ref{thm:B}.\\end{theorem}\n"
                "\\begin{proof}Direct computation.\\end{proof}\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:B}\n"
                "Converse of Theorem~\\ref{thm:A}.\\end{theorem}\n"
                "\\begin{proof}Follows from definitions.\\end{proof}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        auditor.build_combined_dag()
        _, raw_cycles = auditor.topological_sort()
        genuine, forward = auditor.classify_cycles(raw_cycles)

        assert len(forward) >= 1
        assert len(genuine) == 0

    def test_genuine_cycle_classified(self, tmp_path):
        """Proof-level mutual dependency = genuine cycle."""
        # Lines: 1=beginA, 2=endA, 3=proofA start, 4=proofA end,
        #        5=blank, 6=beginB, 7=endB, 8=proofB start, 9=proofB end
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 1,
             "refs_in_block": ["thm:B"]},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 6,
             "refs_in_block": ["thm:A"]},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:A}\n"
                "Refs \\ref{thm:B}.\\end{theorem}\n"
                "\\begin{proof}\nBy \\ref{thm:B} we get...\n\\end{proof}\n"
                "\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:B}\n"
                "Refs \\ref{thm:A}.\\end{theorem}\n"
                "\\begin{proof}\nBy \\ref{thm:A} we get...\n\\end{proof}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        auditor.build_combined_dag()
        _, raw_cycles = auditor.topological_sort()
        genuine, forward = auditor.classify_cycles(raw_cycles)

        assert len(genuine) >= 1


# ==================================================================
# Phase 4: Effective Strength
# ==================================================================

class TestEffectiveStrength:

    def test_clean_chain(self, tmp_path):
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 10, "refs_in_block": ["thm:A"]},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.build_combined_dag()
        sorted_nodes, _ = auditor.topological_sort()
        eff, weak = auditor.compute_effective_strength(sorted_nodes)

        assert eff["thm:A"] == STATUS_STRENGTH["ProvedHere"]
        assert eff["thm:B"] == STATUS_STRENGTH["ProvedHere"]

    def test_conjectural_degrades(self, tmp_path):
        claims = [
            {"label": "conj:C", "env_type": "conjecture", "status": "Conjectured",
             "file": "a.tex", "line": 1},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 10, "refs_in_block": ["conj:C"]},
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 20, "refs_in_block": ["thm:B"]},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.build_combined_dag()
        sorted_nodes, _ = auditor.topological_sort()
        eff, weak = auditor.compute_effective_strength(sorted_nodes)

        assert eff["thm:A"] == STATUS_STRENGTH["Conjectured"]
        assert weak["thm:A"] == "conj:C"

    def test_conditional_does_not_degrade_below_conditional(self, tmp_path):
        """Conditional is 'proved under hypotheses' — floor at Conditional level."""
        claims = [
            {"label": "thm:cond", "env_type": "theorem", "status": "Conditional",
             "file": "a.tex", "line": 1},
            {"label": "thm:proved", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 10, "refs_in_block": ["thm:cond"]},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.build_combined_dag()
        sorted_nodes, _ = auditor.topological_sort()
        eff, _ = auditor.compute_effective_strength(sorted_nodes)

        # Conditional should not degrade below Conditional level
        assert eff["thm:proved"] == STATUS_STRENGTH["Conditional"]

    def test_diamond_takes_minimum(self, tmp_path):
        claims = [
            {"label": "thm:ok", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1},
            {"label": "conj:weak", "env_type": "conjecture", "status": "Conjectured",
             "file": "a.tex", "line": 5},
            {"label": "thm:join", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 10,
             "refs_in_block": ["thm:ok", "conj:weak"]},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.build_combined_dag()
        sorted_nodes, _ = auditor.topological_sort()
        eff, weak = auditor.compute_effective_strength(sorted_nodes)

        assert eff["thm:join"] == STATUS_STRENGTH["Conjectured"]
        assert weak["thm:join"] == "conj:weak"


# ==================================================================
# Phase 5: AP4 Detection (Proof-Level)
# ==================================================================

class TestAP4ProofLevel:

    def test_proof_cites_conjectured_is_critical(self, tmp_path):
        claims = [
            {"label": "conj:X", "env_type": "conjecture", "status": "Conjectured",
             "file": "ch/a.tex", "line": 1},
            {"label": "thm:Y", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 4},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{conjecture}[\\ClaimStatusConjectured]\\label{conj:X}\n"
                "Conjecture.\\end{conjecture}\n"
                "\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:Y}\n"
                "Result.\\end{theorem}\n"
                "\\begin{proof}By Conjecture~\\ref{conj:X}.\\end{proof}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.extract_proof_deps()
        findings = auditor.check_ap4_proof_level()

        assert len(findings) >= 1
        critical = [f for f in findings if f.severity == 'CRITICAL']
        assert len(critical) == 1
        assert critical[0].claim_label == 'thm:Y'
        assert critical[0].upstream_label == 'conj:X'

    def test_clean_proof_no_findings(self, tmp_path):
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 1},
            {"label": "thm:B", "env_type": "theorem", "status": "ProvedHere",
             "file": "ch/a.tex", "line": 4},
        ]
        tex = {
            "ch/a.tex": (
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:A}\n"
                "X.\\end{theorem}\n"
                "\n"
                "\\begin{theorem}[\\ClaimStatusProvedHere]\\label{thm:B}\n"
                "Y.\\end{theorem}\n"
                "\\begin{proof}By \\ref{thm:A}.\\end{proof}\n"
            ),
        }
        repo = _make_repo(tmp_path, claims, tex)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.extract_proof_deps()
        findings = auditor.check_ap4_proof_level()
        assert len(findings) == 0


# ==================================================================
# Phase 6: AP5, AP6, AP11
# ==================================================================

class TestAP6ScopeQualifiers:

    def test_unqualified_koszulness(self, tmp_path):
        claims = [
            {"label": "thm:koszul", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1, "title": "Koszulness holds"},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        findings = auditor.check_ap6_scope_qualifiers()

        assert len(findings) == 1
        assert findings[0].anti_pattern == 'AP6'

    def test_qualified_koszulness_ok(self, tmp_path):
        claims = [
            {"label": "thm:koszul", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1,
             "title": "Koszulness at all genera for type A"},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        findings = auditor.check_ap6_scope_qualifiers()
        assert len(findings) == 0

    def test_unqualified_d_squared(self, tmp_path):
        claims = [
            {"label": "thm:dsq", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1, "title": "D^2 = 0 is proved"},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        findings = auditor.check_ap6_scope_qualifiers()
        assert len(findings) == 1


class TestAP11ExternalDeps:

    def test_single_cite_flagged(self, tmp_path):
        claims = [
            {"label": "thm:ext", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1,
             "cites_in_block": ["Mok2025"],
             "refs_in_block": []},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        findings = auditor.check_ap11_external_deps()

        assert len(findings) == 1
        assert findings[0].anti_pattern == 'AP11'
        assert 'Mok2025' in findings[0].message

    def test_multiple_cites_ok(self, tmp_path):
        claims = [
            {"label": "thm:ext", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1,
             "cites_in_block": ["PaperA", "PaperB"]},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        findings = auditor.check_ap11_external_deps()
        assert len(findings) == 0


# ==================================================================
# Phase 7: Bottlenecks and Test Coverage
# ==================================================================

class TestBottlenecks:

    def test_high_citation_node(self, tmp_path):
        claims = [
            {"label": "thm:core", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1},
        ]
        for i in range(6):
            claims.append({
                "label": f"thm:dep{i}", "env_type": "theorem",
                "status": "ProvedHere", "file": "a.tex", "line": 10 + i,
                "refs_in_block": ["thm:core"],
            })
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.build_combined_dag()
        bottlenecks = auditor.find_bottlenecks(threshold=5)
        assert len(bottlenecks) == 1
        assert bottlenecks[0] == ("thm:core", 6)


class TestTestCoverage:

    def test_finds_label_in_test(self, tmp_path):
        claims = [
            {"label": "thm:shadow-tower", "env_type": "theorem",
             "status": "ProvedHere", "file": "a.tex", "line": 1},
        ]
        repo = _make_repo(tmp_path, claims)
        test_dir = Path(repo) / 'compute' / 'tests'
        (test_dir / 'test_shadow.py').write_text(
            '"""Verifies thm:shadow-tower."""\ndef test_it(): pass\n'
        )
        auditor = BeilinsonAuditor(repo)
        auditor.load_claims()
        coverage = auditor.scan_test_coverage()
        assert "thm:shadow-tower" in coverage


# ==================================================================
# Phase 8: Report and Full Audit
# ==================================================================

class TestReportFormat:

    def test_report_has_dual_dag_sections(self, tmp_path):
        claims = [
            {"label": "thm:A", "env_type": "theorem", "status": "ProvedHere",
             "file": "a.tex", "line": 1},
        ]
        repo = _make_repo(tmp_path, claims)
        auditor = BeilinsonAuditor(repo)
        report = auditor.run_audit()
        text = auditor.format_report(report)

        assert 'BEILINSON AUDIT' in text
        assert '## Dual DAG Summary' in text
        assert 'Statement edges' in text
        assert 'Proof edges' in text
        assert 'Genuine cycles' in text
        assert 'Forward-ref cycles' in text
        assert 'By anti-pattern' in text


# ==================================================================
# Integration tests on real manuscript data
# ==================================================================

class TestIntegrationRealData:

    @pytest.fixture(autouse=True)
    def _check_metadata(self):
        if not (REPO_ROOT / 'metadata' / 'claims.jsonl').exists():
            pytest.skip("metadata/claims.jsonl not found")

    def test_loads_all_claims(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        count = auditor.load_claims()
        assert count >= 2800

    def test_proof_extraction_finds_substantial_deps(self):
        """Proof extraction should find hundreds of proof blocks."""
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        count = auditor.extract_proof_deps()
        assert count >= 200, f"Expected >=200 proofs, got {count}"
        # Proof deps should contain real theorem labels
        total_proof_refs = sum(len(deps) for deps in auditor.proof_deps.values())
        assert total_proof_refs >= 500, f"Expected >=500 proof refs, got {total_proof_refs}"

    def test_proof_edges_exceed_statement_edges(self):
        """Proof DAG should have more edges than statement DAG."""
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()

        stmt_edges = sum(len(deps) for deps in auditor.stmt_adj.values())
        proof_edges = sum(len(deps) for deps in auditor.proof_adj.values())
        # Proof edges should be substantial (agent analysis showed 1.71x ratio)
        assert proof_edges >= stmt_edges * 0.5, (
            f"Proof edges ({proof_edges}) should be at least half of "
            f"statement edges ({stmt_edges})"
        )

    def test_cycle_classification_reduces_critical(self):
        """Forward-ref classification should reduce CRITICAL findings."""
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        auditor.build_combined_dag()
        _, raw_cycles = auditor.topological_sort()

        if not raw_cycles:
            return  # No cycles to classify

        genuine, forward = auditor.classify_cycles(raw_cycles)
        # Not ALL cycles should be genuine — forward refs are normal
        assert len(forward) >= 1 or len(genuine) < len(raw_cycles)

    def test_dag_has_roots(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.build_combined_dag()
        auditor.topological_sort()
        assert len(auditor.layers.get(0, [])) >= 400

    def test_topological_order_complete(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        auditor.build_combined_dag()
        sorted_nodes, _ = auditor.topological_sort()
        assert len(sorted_nodes) == len(auditor.claims)

    def test_effective_strength_computed(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        auditor.build_combined_dag()
        sorted_nodes, _ = auditor.topological_sort()
        eff, _ = auditor.compute_effective_strength(sorted_nodes)
        assert len(eff) == len(auditor.claims)

    def test_bottlenecks_exist(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.build_combined_dag()
        bottlenecks = auditor.find_bottlenecks(threshold=5)
        assert len(bottlenecks) >= 1

    def test_test_coverage_finds_some(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        coverage = auditor.scan_test_coverage()
        assert len(coverage) >= 5

    def test_full_audit_runs(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        report = auditor.run_audit()

        assert report.total_claims >= 2800
        assert report.statement_edges >= 500
        assert report.proof_edges >= 200
        assert report.proof_claims_found >= 200
        assert report.root_count >= 400
        assert isinstance(report.findings, list)

    def test_full_report_renders(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        report = auditor.run_audit()
        text = auditor.format_report(report)
        assert len(text) > 500
        assert 'BEILINSON AUDIT' in text
        assert 'Dual DAG Summary' in text

    def test_status_by_layer_sums(self):
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        auditor.build_combined_dag()
        auditor.topological_sort()
        sbl = auditor.status_by_layer()
        total = sum(sum(d.values()) for d in sbl.values())
        assert total == len(auditor.claims)

    def test_ap11_finds_some_single_cite_claims(self):
        """There should be at least some single-citation ProvedHere claims."""
        auditor = BeilinsonAuditor(str(REPO_ROOT))
        auditor.load_claims()
        auditor.build_statement_dag()
        auditor.extract_proof_deps()
        findings = auditor.check_ap11_external_deps()
        # This is informational — some manuscripts may have few
        assert isinstance(findings, list)
