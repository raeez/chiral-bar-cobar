"""Regression tests for the manuscript metadata parser."""

from __future__ import annotations

import importlib.util
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
                "Conjectured status ledger theorem-level record"
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
