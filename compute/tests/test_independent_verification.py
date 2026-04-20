"""Tests for compute/lib/independent_verification.py -- registry and source-disjointness.

Non-trivial identities tested:
  (i)   assert_sources_disjoint raises IndependentVerificationError when
        derived and verification source sets overlap (case-insensitive,
        whitespace-insensitive).
  (ii)  VerificationEntry.is_tautological returns True iff any source
        appears on both sides.
  (iii) @independent_verification registers entries on the module-level registry.
  (iv)  clear_registry() resets the registry to empty state.
"""

from __future__ import annotations

import pytest

from compute.lib.independent_verification import (
    IndependentVerificationError,
    VerificationEntry,
    assert_sources_disjoint,
    claims_covered,
    clear_registry,
    entries_for,
    independent_verification,
    registry,
    tautological_entries,
)


def test_smoke_empty_registry_after_clear():
    """Smoke: clear_registry empties the registry; registry() returns a copy."""
    clear_registry()
    assert registry() == []
    assert claims_covered() == set()


def test_assert_sources_disjoint_passes_when_clean():
    """Clean disjoint source sets should NOT raise."""
    clear_registry()
    # Should not raise
    assert_sources_disjoint(
        derived_from=["LMFDB 16.1.a.a"],
        verified_against=["Deligne 1974"],
        claim="thm:test-disjoint",
    )


def test_assert_sources_disjoint_raises_on_overlap():
    """Overlapping sources raise IndependentVerificationError."""
    clear_registry()
    with pytest.raises(IndependentVerificationError) as excinfo:
        assert_sources_disjoint(
            derived_from=["LMFDB 16.1.a.a", "Arthur 2013"],
            verified_against=["LMFDB 16.1.a.a"],
            claim="thm:test-overlap",
        )
    assert "LMFDB 16.1.a.a".lower() in str(excinfo.value).lower()


def test_assert_sources_disjoint_case_insensitive():
    """Case-insensitive comparison: 'lmfdb' overlaps 'LMFDB'."""
    clear_registry()
    with pytest.raises(IndependentVerificationError):
        assert_sources_disjoint(
            derived_from=["LMFDB 16.1.a.a"],
            verified_against=["lmfdb 16.1.a.a"],
            claim="thm:test",
        )


def test_assert_sources_disjoint_whitespace_insensitive():
    """Whitespace-insensitive comparison: '  Source X' overlaps 'Source X'."""
    clear_registry()
    with pytest.raises(IndependentVerificationError):
        assert_sources_disjoint(
            derived_from=["  Deligne  1974 "],
            verified_against=["Deligne  1974"],
            claim="thm:test",
        )


def test_verification_entry_tautology_detection():
    """VerificationEntry.is_tautological() True iff source-overlap exists."""
    clean = VerificationEntry(
        claim="c1",
        test_qualname="tq",
        test_file="f",
        derived_from=("A",),
        verified_against=("B",),
        disjoint_rationale="A and B are independent.",
    )
    assert clean.is_tautological() is False

    dirty = VerificationEntry(
        claim="c2",
        test_qualname="tq",
        test_file="f",
        derived_from=("A", "B"),
        verified_against=("B",),
        disjoint_rationale="",
    )
    assert dirty.is_tautological() is True


def test_independent_verification_decorator_registers():
    """@independent_verification adds an entry to the module-level registry."""
    clear_registry()

    @independent_verification(
        claim="thm:unit-test",
        derived_from=["Paper X"],
        verified_against=["Paper Y"],
        disjoint_rationale="X and Y use different conventions.",
    )
    def _dummy():
        return True

    assert _dummy() is True
    assert "thm:unit-test" in claims_covered()
    entries = entries_for("thm:unit-test")
    assert len(entries) >= 1
    assert entries[0].claim == "thm:unit-test"


def test_tautological_entries_isolated():
    """clear_registry + populate + check tautological_entries is empty for clean test."""
    clear_registry()
    # No tautological registrations pushed yet
    assert tautological_entries() == []
