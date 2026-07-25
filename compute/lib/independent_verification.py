"""
Independent verification registry for ProvedHere claims.

MOTIVATION
----------
The 2026-04-16 adversarial audit (cache entries 57-68) exposed a systematic
failure mode: tests verify formulas against the SAME hardcoded table from
which the formula was derived. Example: kappa_BKM_universal.py defines
FRAME_SHAPE_DATA[N] = (weight, c_0, ...) with weight := c_0 / 2 literal, and
99 tests check Fraction(10, 2) == 5 against that table. This is tautology
dressed as verification.

PROTOCOL
--------
Every test that claims to verify a ProvedHere theorem must:

1. Declare its claim label via @independent_verification decorator.
2. Enumerate the DERIVATION sources (where the formula came from).
3. Enumerate the VERIFICATION sources (what the test compares against).
4. Assert derivation and verification sources are DISJOINT.

This module provides:
  - The decorator (run-time assertion + registry entry)
  - The registry (queryable by claim label, source, tautology status)
  - `assert_sources_disjoint`: the core disjointness check
  - `IndependentVerificationError`: raised when sources overlap

A companion lint (compute/scripts/audit_independent_verification.py) scans
.tex for ProvedHere tags and compares against the registry to produce a
coverage report.

USAGE
-----
    from compute.lib.independent_verification import independent_verification

    @independent_verification(
        claim="prop:bkm-weight-universal",
        derived_from=["Borcherds 1998 weight theorem",
                      "FRAME_SHAPE_DATA orbifold table (Gaberdiel-Volpato)"],
        verified_against=["Gritsenko-Nikulin Phi_10 denominator identity",
                          "Imaginary root multiplicities from g_{Delta_5} root system"],
        disjoint_rationale=(
            "FRAME_SHAPE_DATA supplies c_0 by definition of the lift input. "
            "Denominator identity independently computes the BKM central charge "
            "from imaginary root multiplicities without reference to the lift."),
    )
    def test_kappa_bkm_equals_bkm_central_charge():
        ...

If derived_from and verified_against share an element, the decorator raises
IndependentVerificationError at import time. This is intentional: tautological
tests must not silently register as verification.
"""

from __future__ import annotations

import ast
import functools
import inspect
import re
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class VerificationEntry:
    """Record of one (test, claim) verification relationship.

    ``manuscript_read_paths`` and ``derivation_module_imports`` are filled
    by the static source scan performed at decoration time (see the
    ``independent_verification`` docstring for exactly what the scan does
    and does not guarantee).
    """
    claim: str
    test_qualname: str
    test_file: str
    derived_from: tuple[str, ...]
    verified_against: tuple[str, ...]
    disjoint_rationale: str
    manuscript_read_paths: tuple[str, ...] = ()
    derivation_module_imports: tuple[str, ...] = ()

    def is_tautological(self) -> bool:
        """True if any derivation source also appears as a verification source.

        Comparison is case-insensitive and strips whitespace.
        """
        deriv = {s.strip().lower() for s in self.derived_from}
        verif = {s.strip().lower() for s in self.verified_against}
        return bool(deriv & verif)


# Module-level registry. Populated at import time as tests are loaded.
_REGISTRY: list[VerificationEntry] = []


def registry() -> list[VerificationEntry]:
    """Return the current registry (copy, so callers can't mutate)."""
    return list(_REGISTRY)


def claims_covered() -> set[str]:
    """Set of claim labels with at least one registered independent test."""
    return {e.claim for e in _REGISTRY if not e.is_tautological()}


def entries_for(claim: str) -> list[VerificationEntry]:
    """All entries registered against a specific claim label."""
    return [e for e in _REGISTRY if e.claim == claim]


def tautological_entries() -> list[VerificationEntry]:
    """Entries whose derivation and verification sources overlap."""
    return [e for e in _REGISTRY if e.is_tautological()]


def manuscript_reading_entries() -> list[VerificationEntry]:
    """Entries whose test module statically appears to read ``.tex`` files.

    A verification value obtained by reading the manuscript is compared
    against the manuscript -- circular by construction. These entries are
    flagged for audit; see ``independent_verification`` for scan semantics.
    """
    return [e for e in _REGISTRY if e.manuscript_read_paths]


def derivation_import_entries() -> list[VerificationEntry]:
    """Entries whose test module imports a cited derivation module.

    Flagged for audit: the rationale must argue function-level
    disjointness inside the shared module, or the entry is tautological.
    """
    return [e for e in _REGISTRY if e.derivation_module_imports]


def clear_registry() -> None:
    """Clear the registry. Used by the infra self-test to isolate state."""
    _REGISTRY.clear()


# ---------------------------------------------------------------------------
# Error
# ---------------------------------------------------------------------------


class IndependentVerificationError(AssertionError):
    """Raised when verification and derivation sources overlap.

    Subclasses AssertionError so pytest reports it as a test failure, not
    as a harness crash. This means: a tautological @independent_verification
    decoration will cause the test to fail at collection time.
    """


# ---------------------------------------------------------------------------
# Disjointness check
# ---------------------------------------------------------------------------


def assert_sources_disjoint(
    derived_from: Iterable[str],
    verified_against: Iterable[str],
    claim: str = "",
) -> None:
    """Raise IndependentVerificationError if the two source sets intersect.

    Whitespace-insensitive, case-insensitive comparison. Source labels must
    be exact strings (not substrings); callers are responsible for choosing
    canonical names.
    """
    deriv = {s.strip().lower() for s in derived_from}
    verif = {s.strip().lower() for s in verified_against}
    overlap = deriv & verif
    if overlap:
        raise IndependentVerificationError(
            f"claim={claim!r}: verification sources overlap with derivation "
            f"sources: {sorted(overlap)!r}. "
            "Tautological verification is not independent verification. "
            "Pick a source disjoint from the derivation, or restate the "
            "theorem's scope."
        )


# ---------------------------------------------------------------------------
# Static source scan (module-level, best-effort)
# ---------------------------------------------------------------------------

# Explicit python-module references inside source-description strings, e.g.
# "compute.lib.kappa_bkm_universal" or "kappa_BKM_universal.py".
_MODULE_REF_PATTERNS = (
    re.compile(r"compute\.lib\.([A-Za-z_]\w*)"),
    re.compile(r"([A-Za-z_]\w*)\.py\b"),
)


def _parse_module_source(module) -> ast.Module | None:
    """Best-effort AST of the module defining the decorated test."""
    try:
        source = inspect.getsource(module)
        return ast.parse(source)
    except (OSError, TypeError, SyntaxError):
        return None


def _imported_module_names(tree: ast.Module) -> set[str]:
    """All module names imported by the module (top of dotted path and leaf)."""
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                names.update(alias.name.split("."))
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                names.update(node.module.split("."))
            for alias in node.names:
                names.add(alias.name)
    return names


def _derivation_module_tokens(derived_from: Iterable[str]) -> set[str]:
    """Python-module names explicitly cited as DERIVATION sources."""
    tokens: set[str] = set()
    for source in derived_from:
        for pattern in _MODULE_REF_PATTERNS:
            tokens.update(match.lower() for match in pattern.findall(source))
    return tokens


def _is_iv_decorator_call(node: ast.Call) -> bool:
    """True if the Call node is an ``independent_verification(...)`` call."""
    func = node.func
    name = getattr(func, "id", None) or getattr(func, "attr", None)
    return name == "independent_verification"


def _tex_paths_in_calls(tree: ast.Module) -> tuple[str, ...]:
    """String constants ending in ``.tex`` used inside call expressions.

    Docstrings, comments, and prose citations mentioning ``.tex`` mid-string
    are NOT flagged; only path-shaped strings (ending with ``.tex``) that
    flow into a function call (``open``, ``Path(...)``, ``read_text``
    argument chains, glob patterns, ...) are collected.  Arguments of the
    ``independent_verification`` decorator itself (source-citation prose)
    are excluded.
    """
    found: list[str] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or _is_iv_decorator_call(node):
            continue
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call) and _is_iv_decorator_call(sub):
                continue
            if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                if sub.value.endswith(".tex"):
                    found.append(sub.value)
    return tuple(dict.fromkeys(found))


def _scan_module(
    module,
    derived_from: tuple[str, ...],
    claim: str,
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Run both static checks; flag findings on the entry and warn.

    Returns ``(manuscript_read_paths, derivation_module_imports)``.

    Neither finding is a hard error: derivation and verification may
    legitimately live in DIFFERENT FUNCTIONS of one engine module (the
    rationale must argue the function-level disjointness), and a module
    may read .tex files for reasons other than sourcing expected values.
    Both situations are recorded for audit rather than silently passed.
    """
    tree = _parse_module_source(module)
    if tree is None:
        return (), ()

    imported = {name.lower() for name in _imported_module_names(tree)}
    derivation_tokens = _derivation_module_tokens(derived_from)
    overlap = tuple(sorted(imported & derivation_tokens))
    if overlap:
        warnings.warn(
            f"claim={claim!r}: the test module imports {overlap!r}, which "
            "derived_from explicitly names as a derivation source. If the "
            "verification value flows through the same code path as the "
            "derivation, this is a tautology; entry flagged in the "
            "registry (derivation_module_imports).",
            stacklevel=3,
        )

    tex_paths = _tex_paths_in_calls(tree)
    if tex_paths:
        warnings.warn(
            f"claim={claim!r}: the test module passes .tex paths to calls "
            f"({tex_paths!r}). Manuscript-derived expected values are not "
            "independent verification; entry flagged in the registry "
            "(see manuscript_reading_entries()).",
            stacklevel=3,
        )
    return tex_paths, overlap


# ---------------------------------------------------------------------------
# Decorator
# ---------------------------------------------------------------------------


def independent_verification(
    *,
    claim: str,
    derived_from: Iterable[str],
    verified_against: Iterable[str],
    disjoint_rationale: str,
) -> Callable:
    """Register a test as independently verifying a ProvedHere claim.

    Parameters
    ----------
    claim : str
        Label of the theorem/proposition being verified. Must match a
        \\label{...} in chapters/ or working_notes.tex. Convention: use the
        LaTeX label verbatim, e.g., "thm:phi-k3-explicit".
    derived_from : list[str]
        Canonical names of the data/papers/conventions from which the
        CLAIMED FORMULA was derived. These are the "suspect" sources that
        the test must AVOID when computing the verification value.
    verified_against : list[str]
        Canonical names of independent data/papers/conventions from which
        the TEST computes its expected value. These must be disjoint from
        derived_from.
    disjoint_rationale : str
        One-sentence explanation of why the two source sets are genuinely
        independent (not just renamed). Reviewed during audit.

    Raises
    ------
    IndependentVerificationError
        At decoration time, if derived_from and verified_against overlap
        as strings. This surfaces as a test collection failure -- the
        tautology is caught before the test runs.

    Notes
    -----
    WHAT THIS DECORATOR GUARANTEES (all checks are static and best-effort):

    1. String disjointness (hard error): ``derived_from`` and
       ``verified_against`` share no element (case/whitespace-insensitive
       exact-string comparison).
    2. Derivation-import flagging (warning + registry flag): if the module
       containing the decorated test imports a python module explicitly
       cited in ``derived_from`` via a ``compute.lib.<name>`` or
       ``<name>.py`` reference, the import is recorded on the entry
       (``derivation_module_imports``) and a ``UserWarning`` is emitted.
       Not a hard error, because derivation and verification may
       legitimately be different FUNCTIONS of one engine module -- the
       ``disjoint_rationale`` must then argue function-level disjointness.
    3. Manuscript-read flagging (warning + registry flag): string
       constants ending in ``.tex`` that appear inside call expressions of
       the test's module (file opens, Path construction, glob patterns)
       are recorded on the entry (``manuscript_read_paths``). Comparing a
       computed value against a number scraped from the manuscript is
       circular whenever the manuscript value came from the same
       derivation; such entries are queryable via
       ``manuscript_reading_entries()`` for audit. Prose citations that
       merely mention a ``.tex`` file (including inside this decorator's
       own arguments) are not flagged.

    WHAT IT DOES NOT GUARANTEE:

    - Genuine mathematical independence of the two source sets. Renaming a
      source, re-deriving the same formula in a second module, or citing a
      secondary reference that itself derives from the primary all pass
      every static check. Only the ``disjoint_rationale`` review catches
      these.
    - Transitive import hygiene: an imported module may itself import the
      derivation module; the scan is one level deep by design.
    - Dynamic behaviour: file paths assembled at runtime, ``importlib``
      loads, or data files that cache manuscript values are invisible to
      the AST scan.
    - Data provenance: a hardcoded constant inside the verification path
      is not traced to its origin.

    The decorator does not change test behaviour at call time. It installs
    a registry entry, enforces string disjointness, and records the two
    static-scan flags at import time.
    """
    derived_tuple = tuple(derived_from)
    verified_tuple = tuple(verified_against)
    # Fail fast at import time -- tautological decorations cannot even be
    # registered.
    assert_sources_disjoint(derived_tuple, verified_tuple, claim=claim)
    if not disjoint_rationale or not disjoint_rationale.strip():
        raise IndependentVerificationError(
            f"claim={claim!r}: disjoint_rationale is required and must be "
            "non-empty. Explain WHY the two source sets are independent."
        )

    def decorator(fn: Callable) -> Callable:
        module = inspect.getmodule(fn)
        test_file = (
            str(Path(module.__file__).resolve())
            if module and module.__file__
            else "<unknown>"
        )
        if module is not None:
            tex_paths, derivation_imports = _scan_module(
                module, derived_tuple, claim,
            )
        else:
            tex_paths, derivation_imports = (), ()
        entry = VerificationEntry(
            claim=claim,
            test_qualname=f"{fn.__module__}.{fn.__qualname__}",
            test_file=test_file,
            derived_from=derived_tuple,
            verified_against=verified_tuple,
            disjoint_rationale=disjoint_rationale.strip(),
            manuscript_read_paths=tex_paths,
            derivation_module_imports=derivation_imports,
        )
        _REGISTRY.append(entry)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)

        # Expose the entry on the wrapper for introspection.
        wrapper._iv_entry = entry  # type: ignore[attr-defined]
        return wrapper

    return decorator


# ---------------------------------------------------------------------------
# Coverage helpers (used by the lint script)
# ---------------------------------------------------------------------------


@dataclass
class CoverageReport:
    """Summary of ProvedHere coverage vs the registry."""
    proved_here_claims: set[str] = field(default_factory=set)
    other_valid_claims: set[str] = field(default_factory=set)
    covered_claims: set[str] = field(default_factory=set)
    tautological: list[VerificationEntry] = field(default_factory=list)

    @property
    def uncovered_claims(self) -> set[str]:
        return self.proved_here_claims - self.covered_claims

    @property
    def orphan_entries(self) -> list[VerificationEntry]:
        """Registry entries whose claim is not found in any .tex.

        Valid targets include ProvedHere theorems AND other-valid claims
        (ProvedElsewhere, Conjectured, Conditional, Construction, Definition).
        Sub-labels of the form ``parent::child`` are accepted if ``parent``
        exists as a valid target.
        """
        valid = self.proved_here_claims | self.other_valid_claims
        orphans = []
        for e in _REGISTRY:
            if e.claim in valid:
                continue
            # Accept ``parent::child`` sub-labels if parent exists.
            if "::" in e.claim:
                parent = e.claim.split("::", 1)[0]
                if parent in valid:
                    continue
            orphans.append(e)
        return orphans

    def summary(self) -> str:
        n_proved = len(self.proved_here_claims)
        n_other = len(self.other_valid_claims)
        n_covered = len(self.covered_claims)
        pct = (100.0 * n_covered / n_proved) if n_proved else 0.0
        lines = [
            f"ProvedHere claims found in .tex: {n_proved}",
            f"Other valid claims (Conj./Cond./Elsewhere/Constr.): {n_other}",
            f"Claims with independent verification:  {n_covered} ({pct:.1f}%)",
            f"Claims WITHOUT independent verification: {len(self.uncovered_claims)}",
            f"Tautological registry entries: {len(self.tautological)}",
            f"Orphan registry entries (claim not found in .tex): "
            f"{len(self.orphan_entries)}",
        ]
        return "\n".join(lines)


def build_coverage_report(
    proved_here_labels: Iterable[str],
    other_valid_labels: Iterable[str] = (),
) -> CoverageReport:
    """Combine the current registry with sets of valid claim labels.

    The caller (lint script) supplies labels scraped from .tex. This module
    stays independent of the scraper so the module is testable without any
    .tex files present. Decorations on Conjectured/Conditional/Construction/
    Definition/ProvedElsewhere labels are valid (they verify falsifiable
    predictions, not the claim's truth itself).
    """
    proved_set = set(proved_here_labels)
    other_set = set(other_valid_labels)
    return CoverageReport(
        proved_here_claims=proved_set,
        other_valid_claims=other_set,
        covered_claims=claims_covered() & proved_set,
        tautological=tautological_entries(),
    )
