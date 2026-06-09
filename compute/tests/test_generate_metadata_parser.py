"""Regression tests for the manuscript metadata parser."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


def load_generator():
    script = Path(__file__).resolve().parents[2] / "scripts" / "generate_metadata.py"
    spec = importlib.util.spec_from_file_location("generate_metadata", script)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_commented_claim_environments_are_ignored(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)

    tex = tmp_path / "sample.tex"
    tex.write_text(
        r"""
% \begin{conjecture}[False; \ClaimStatusProvedHere]
% \label{conj:commented}
% This is dead source and must not enter metadata.
% \end{conjecture}

\begin{theorem}[Live theorem; \ClaimStatusProvedHere]
\label{thm:live}
The active proof cites \ref{lem:live}.
\end{theorem}
""",
        encoding="utf-8",
    )

    claims = gm.extract_claims(tex)

    assert [claim.label for claim in claims] == ["thm:live"]
    assert claims[0].env_type == "theorem"
    assert claims[0].status == "ProvedHere"
    assert claims[0].refs_in_block == ["lem:live"]


def test_definitional_claim_environments_are_extracted(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)

    tex = tmp_path / "sample.tex"
    tex.write_text(
        r"""
\begin{definition}[Hecke defect class; \ClaimStatusDefinitional]
\label{def:hecke-defect-class}
The class is represented by \ref{rem:prime-locality-obstruction}.
\end{definition}
""",
        encoding="utf-8",
    )

    claims = gm.extract_claims(tex)
    labels = gm.extract_all_labels(tex)

    assert [claim.label for claim in claims] == ["def:hecke-defect-class"]
    assert claims[0].env_type == "definition"
    assert claims[0].status == "Definitional"
    assert claims[0].title == "Hecke defect class"
    assert claims[0].refs_in_block == ["rem:prime-locality-obstruction"]
    assert labels[0].env_type == "definition"


def test_construction_claim_environments_are_extracted(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)

    tex = tmp_path / "sample.tex"
    tex.write_text(
        r"""
\begin{construction}[Complexified integral; \ClaimStatusDefinitional]
\label{constr:complex-integral}
\begin{equation}\label{eq:complex-integral}
Z = \int_{\mathcal C} e^{-S}\,D\sigma .
\end{equation}
The normalization cites \ref{eq:reference-normalization}.
\end{construction}
""",
        encoding="utf-8",
    )

    claims = gm.extract_claims(tex)

    assert [claim.label for claim in claims] == ["constr:complex-integral"]
    assert claims[0].env_type == "construction"
    assert claims[0].status == "Definitional"
    assert claims[0].title == "Complexified integral"
    assert claims[0].aliases == [
        "constr:complex-integral",
        "eq:complex-integral",
    ]
    assert claims[0].refs_in_block == ["eq:reference-normalization"]


def test_convention_claim_environments_are_extracted(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)

    tex = tmp_path / "sample.tex"
    tex.write_text(
        r"""
\begin{convention}[Semantic levels; \ClaimStatusDefinitional]
\label{conv:semantic-levels}
The H-level cites \ref{prop:model-independence}.
\end{convention}
""",
        encoding="utf-8",
    )

    claims = gm.extract_claims(tex)
    labels = gm.extract_all_labels(tex)

    assert [claim.label for claim in claims] == ["conv:semantic-levels"]
    assert claims[0].env_type == "convention"
    assert claims[0].status == "Definitional"
    assert claims[0].title == "Semantic levels"
    assert claims[0].refs_in_block == ["prop:model-independence"]
    assert labels[0].env_type == "convention"


def test_commented_labels_refs_and_statuses_are_ignored(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)

    tex = tmp_path / "sample.tex"
    tex.write_text(
        r"""
% \label{sec:commented}
\label{sec:active}
% See \ref{thm:commented}.
See \ref{thm:active}.
% \ClaimStatusConjectured
\ClaimStatusProvedHere
""",
        encoding="utf-8",
    )

    labels = gm.extract_all_labels(tex)
    refs = gm.extract_all_refs(tex)
    counts = gm.raw_grep_counts([tex])

    assert [entry.label for entry in labels] == ["sec:active"]
    assert refs == [("thm:active", "sample.tex", 5)]
    assert counts == {"ProvedHere": 1}


def test_theorem_index_has_no_status_surface(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)
    monkeypatch.setattr(gm, "STANDALONE_DIR", tmp_path / "standalone")

    claims = [
        gm.Claim(
            label="rem:open-status-ledger",
            env_type="remark",
            status="ProvedHere",
            file="chapters/theory/sample.tex",
            line=12,
            title=(
                "Conditional Open Heuristic ProvedHere ProvedElsewhere "
                "Conjectured Definitional status ledger theorem-level record"
            ),
        )
    ]

    gm.write_theorem_index(claims)
    index_text = (tmp_path / "standalone" / "theorem_index.tex").read_text(
        encoding="utf-8"
    )

    assert "Env & Label & Name & File:line" in index_text
    assert "Status" not in index_text
    assert "ProvedHere" not in index_text
    assert "status" not in index_text.lower()
    assert "ledger" not in index_text.lower()
    assert "theorem-level" not in index_text.lower()
    assert "Conditional" not in index_text
    assert "Open" not in index_text
    assert "Heuristic" not in index_text
    assert "ProvedElsewhere" not in index_text
    assert "Conjectured" not in index_text
    assert "Definitional" not in index_text


def test_duplicate_labels_are_aliases_not_node_keys(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)
    monkeypatch.setattr(gm, "METADATA_DIR", tmp_path / "metadata")
    gm.METADATA_DIR.mkdir()

    tex_a = tmp_path / "a.tex"
    tex_b = tmp_path / "b.tex"
    tex_c = tmp_path / "c.tex"
    tex_a.write_text(
        r"""
\begin{theorem}[First occurrence; \ClaimStatusProvedHere]
\label{thm:duplicate}
First claim.
\end{theorem}
""",
        encoding="utf-8",
    )
    tex_b.write_text(
        r"""
\begin{proposition}[Second occurrence; \ClaimStatusProvedHere]
\label{thm:duplicate}
Second claim.
\end{proposition}
""",
        encoding="utf-8",
    )
    tex_c.write_text(
        r"""
\begin{lemma}[Referencing occurrence; \ClaimStatusProvedHere]
\label{lem:source}
Uses \ref{thm:duplicate}.
\end{lemma}
""",
        encoding="utf-8",
    )

    files = [tex_a, tex_b, tex_c]
    claims = [claim for path in files for claim in gm.extract_claims(path)]
    labels = [entry for path in files for entry in gm.extract_all_labels(path)]

    duplicate_claims = [claim for claim in claims if claim.label == "thm:duplicate"]
    assert len(duplicate_claims) == 2
    assert len({claim.node_key for claim in duplicate_claims}) == 2

    gm.write_label_index(labels, claims)
    label_index = json.loads((gm.METADATA_DIR / "label_index.json").read_text())
    duplicate = label_index["thm:duplicate"]
    assert duplicate["duplicate"] is True
    assert len(duplicate["occurrences"]) == 2
    assert len(duplicate["claim_node_keys"]) == 2

    gm.write_dependency_graph(claims, labels)
    dot = (gm.METADATA_DIR / "dependency_graph.dot").read_text(encoding="utf-8")
    source_key = next(claim.node_key for claim in claims if claim.label == "lem:source")
    for target in duplicate["claim_node_keys"]:
        assert f'"{source_key}" -> "{target}"' in dot


def test_duplicate_labels_are_aliases_not_node_keys(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)
    monkeypatch.setattr(gm, "METADATA_DIR", tmp_path / "metadata")
    (tmp_path / "metadata").mkdir()

    first = tmp_path / "a.tex"
    second = tmp_path / "b.tex"
    first.write_text(
        r"""
\begin{theorem}[First; \ClaimStatusProvedHere]
\label{thm:duplicate}
Uses \ref{thm:target}.
\end{theorem}
""",
        encoding="utf-8",
    )
    second.write_text(
        r"""
\begin{lemma}[Second; \ClaimStatusProvedHere]
\label{thm:duplicate}
\label{thm:target}
Done.
\end{lemma}
""",
        encoding="utf-8",
    )

    claims = gm.extract_claims(first) + gm.extract_claims(second)
    labels = gm.extract_all_labels(first) + gm.extract_all_labels(second)

    assert len({claim.node_key for claim in claims}) == 2
    assert [claim.label for claim in claims] == ["thm:duplicate", "thm:duplicate"]

    gm.write_label_index(labels, claims)
    index = gm.json.loads((tmp_path / "metadata" / "label_index.json").read_text())
    duplicate = index["thm:duplicate"]

    assert duplicate["duplicate"] is True
    assert len(duplicate["occurrences"]) == 2
    assert len(duplicate["claim_node_keys"]) == 2
    assert all("thm:duplicate" not in key for key in duplicate["claim_node_keys"])


def test_dependency_graph_uses_node_key_for_duplicate_aliases(tmp_path, monkeypatch):
    gm = load_generator()
    monkeypatch.setattr(gm, "ROOT", tmp_path)
    monkeypatch.setattr(gm, "METADATA_DIR", tmp_path / "metadata")
    (tmp_path / "metadata").mkdir()

    source = tmp_path / "source.tex"
    target_a = tmp_path / "target_a.tex"
    target_b = tmp_path / "target_b.tex"

    source.write_text(
        r"""
\begin{proposition}[Source; \ClaimStatusProvedHere]
\label{prop:source}
Uses \ref{thm:duplicate}.
\end{proposition}
""",
        encoding="utf-8",
    )
    target_a.write_text(
        r"""
\begin{theorem}[Target A; \ClaimStatusProvedHere]
\label{thm:duplicate}
Done.
\end{theorem}
""",
        encoding="utf-8",
    )
    target_b.write_text(
        r"""
\begin{theorem}[Target B; \ClaimStatusProvedHere]
\label{thm:duplicate}
Done.
\end{theorem}
""",
        encoding="utf-8",
    )

    claims = (
        gm.extract_claims(source)
        + gm.extract_claims(target_a)
        + gm.extract_claims(target_b)
    )
    labels = (
        gm.extract_all_labels(source)
        + gm.extract_all_labels(target_a)
        + gm.extract_all_labels(target_b)
    )

    gm.write_dependency_graph(claims, labels)
    graph = (tmp_path / "metadata" / "dependency_graph.dot").read_text()

    assert '"source.tex#proposition:2:1"' in graph
    assert '"target_a.tex#theorem:2:1"' in graph
    assert '"target_b.tex#theorem:2:1"' in graph
    assert '"source.tex#proposition:2:1" -> "target_a.tex#theorem:2:1";' in graph
    assert '"source.tex#proposition:2:1" -> "target_b.tex#theorem:2:1";' in graph
