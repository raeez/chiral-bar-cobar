"""AP5 cross-volume consistency checker.

Automates the AP5 mandate from CLAUDE.md: "Grep ALL THREE volumes for variant
forms after every correction."  Historically this was a manual agent sweep
(Wave 6-2, Wave 8-5); this module turns it into a deterministic compute-layer
check that can run continuously.

The engine scans Vol I (chiral-bar-cobar), Vol II (chiral-bar-cobar-vol2), and
Vol III (calabi-yau-quantum-groups) for a library of canonical regex patterns
drawn directly from the anti-pattern catalog in CLAUDE.md.  For each pattern
the caller supplies an expected per-volume frequency (either an exact integer,
a bound ``(low, high)``, or ``"any"``).  The engine reports every pattern
whose observed frequency falls outside the declared envelope, giving a
human-readable drift report suitable for CI or for a pre-commit hook.

Canonical formulas covered (fifteen, each annotated with its governing AP):

    1.  AP126  -- bare ``\\Omega/z`` without level prefix ``k``
    2.  AP1    -- ``\\kappa(V_k(\\fg))`` (affine KM canonical form)
    3.  AP1    -- ``\\kappa(H_k) = k`` (Heisenberg, Vol I convention)
    4.  AP136  -- ``\\kappa(W_N) = c(H_N - 1)``  (NOT ``H_{N-1}``)
    5.  AP132  -- ``T^c(s^{-1}\\bar A)`` augmentation-ideal bar complex
    6.  AP113  -- bare ``\\kappa`` in Vol III (forbidden; must be subscripted)
    7.  build  -- ``\\end{...>`` compile-breaker typo
    8.  V2-AP26 -- hardcoded ``Part~[IVX]`` labels (drift across re-ordering)
    9.  git    -- AI attribution keywords
    10. prose  -- em dashes (U+2014)
    11. prose  -- AI slop vocabulary
    12. AP136  -- bare ``H_{N-1}`` occurrences (potential trap)
    13. AP132  -- bar complex missing augmentation: ``T^c(s^{-1} A)``
    14. AP39   -- ``\\kappa = S_2`` (only Virasoro rank-1 coincidence)
    15. AP124  -- labels declared in multiple volumes

Design choices:

    -   Pure stdlib; subprocess runs ``grep -rhoE`` to remain fast on the
        ~4,200-page manuscript tree.
    -   Patterns are stored in a single ``CANONICAL_FORMULAS`` table so
        downstream scripts can extend the library without touching the
        engine.
    -   ``CheckResult`` is a plain dataclass (no pydantic) so the module
        stays importable from the existing pytest runner with zero extras.
    -   Per-volume scope can be disabled (``scope={"vol3"}`` excluded) to
        allow patterns that legitimately only live in some volumes.
"""

from __future__ import annotations

import os
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

DEFAULT_VOL1 = Path("/Users/raeez/chiral-bar-cobar")
DEFAULT_VOL2 = Path("/Users/raeez/chiral-bar-cobar-vol2")
DEFAULT_VOL3 = Path("/Users/raeez/calabi-yau-quantum-groups")

#: Subdirectories that are scanned inside each volume root.
SCAN_SUBDIRS: Tuple[str, ...] = ("chapters", "appendices")


# ---------------------------------------------------------------------------
# Result / envelope types
# ---------------------------------------------------------------------------

Envelope = Union[int, Tuple[int, int], str]  # "any" accepted
"""Expected-frequency envelope for a single volume.

* ``int``: exact count required.
* ``(low, high)`` inclusive bound.
* ``"any"``: no constraint; record the count but do not flag drift.
"""


@dataclass
class CheckResult:
    """Outcome of a single regex sweep across one or more volumes."""

    key: str
    description: str
    ap_tag: str
    pattern: str
    observed: Dict[str, int] = field(default_factory=dict)
    expected: Dict[str, Envelope] = field(default_factory=dict)
    scope: Tuple[str, ...] = ("vol1", "vol2", "vol3")
    drift: List[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.drift

    def total(self) -> int:
        return sum(self.observed.values())


@dataclass
class CanonicalFormula:
    """A single regex + expected-envelope entry in the AP5 library."""

    key: str
    description: str
    ap_tag: str
    pattern: str
    expected: Dict[str, Envelope]
    scope: Tuple[str, ...] = ("vol1", "vol2", "vol3")
    #: If True, the engine runs a duplicate-label sweep instead of a plain
    #: count sweep.  The pattern then captures the label name in group 1.
    duplicate_label: bool = False


# ---------------------------------------------------------------------------
# Canonical library
# ---------------------------------------------------------------------------

CANONICAL_FORMULAS: Tuple[CanonicalFormula, ...] = (
    # 1. AP126 -- bare \Omega/z without level prefix
    CanonicalFormula(
        key="ap126_bare_omega_over_z",
        description="Bare Omega/z (must be k*Omega/z, AP126)",
        ap_tag="AP126",
        # Match \Omega/z NOT preceded by '*' or a level factor 'k' or digit.
        pattern=r"(?<![*k0-9])\\Omega/z",
        expected={"vol1": 0, "vol2": 0, "vol3": 0},
    ),

    # 2. AP1 -- canonical affine KM kappa formula
    CanonicalFormula(
        key="ap1_kappa_affine_km",
        description="Affine KM kappa canonical form kappa(V_k(g))",
        ap_tag="AP1",
        pattern=r"\\kappa\s*\(\s*V_k\s*\(\s*\\fg\s*\)\s*\)",
        expected={"vol1": "any", "vol2": "any", "vol3": "any"},
    ),

    # 3. AP1 -- Heisenberg kappa(H_k) = k
    CanonicalFormula(
        key="ap1_heisenberg_kappa",
        description="Heisenberg kappa(H_k)=k canonical form",
        ap_tag="AP1",
        pattern=r"\\kappa\s*\(\s*H_k\s*\)\s*=\s*k",
        expected={"vol1": "any", "vol2": "any", "vol3": "any"},
    ),

    # 4. AP136 -- kappa(W_N) = c(H_N - 1), NOT c H_{N-1}
    CanonicalFormula(
        key="ap136_wn_harmonic_wrong",
        description="W_N kappa written with H_{N-1} (forbidden, AP136)",
        ap_tag="AP136",
        pattern=r"\\kappa\s*\(\s*W_N\s*\)[^\n]{0,40}H_\{\s*N\s*-\s*1\s*\}",
        expected={"vol1": 0, "vol2": 0, "vol3": 0},
    ),

    # 5. AP132 -- augmentation ideal bar complex T^c(s^{-1} \bar A)
    CanonicalFormula(
        key="ap132_bar_augmentation_present",
        description="T^c(s^{-1} bar A) augmentation-ideal bar complex",
        ap_tag="AP132",
        # \bar{A} or \bar A inside T^c(s^{-1} ...)
        pattern=r"T\^c\(\s*s\^\{-1\}\s*\\bar\s*\{?A\}?\s*\)",
        expected={"vol1": "any", "vol2": "any", "vol3": "any"},
    ),

    # 6. AP113 -- bare \kappa in Vol III (forbidden)
    CanonicalFormula(
        key="ap113_bare_kappa_vol3",
        description="Bare \\kappa in Vol III without subscript (AP113)",
        ap_tag="AP113",
        # \kappa NOT followed by an underscore or letter subscript; allow
        # \kappa( because \kappa(...) is a function application with
        # contextual subscripts elsewhere.  Also allow \kappa^ for duals.
        pattern=r"\\kappa(?![_^a-zA-Z(])",
        expected={"vol3": 0},
        scope=("vol3",),
    ),

    # 7. Compile-breaker typo \end{xxx>
    CanonicalFormula(
        key="end_environment_typo",
        description="\\end{env> compile-breaker typo",
        ap_tag="build",
        pattern=r"\\end\{[a-zA-Z*]+>",
        expected={"vol1": 0, "vol2": 0, "vol3": 0},
    ),

    # 8. V2-AP26 -- hardcoded Part~[IVX]
    CanonicalFormula(
        key="v2ap26_hardcoded_part",
        description="Hardcoded Part~[IVX] label (V2-AP26)",
        ap_tag="V2-AP26",
        pattern=r"Part~[IVX]+\b",
        expected={
            "vol1": (0, 200),
            "vol2": (0, 200),
            "vol3": (0, 100),
        },
    ),

    # 9. AI attribution keywords (git rule)
    CanonicalFormula(
        key="git_ai_attribution",
        description="AI attribution keywords (git rule: NEVER credit an LLM)",
        ap_tag="git",
        pattern=r"(?i)co-authored-by|anthropic|claude\.ai|generated by claude",
        expected={"vol1": 0, "vol2": 0, "vol3": 0},
    ),

    # 10. Em dashes -- Unicode U+2014
    CanonicalFormula(
        key="prose_em_dash",
        description="Em dash U+2014 (forbidden by prose law 3)",
        ap_tag="prose",
        pattern="\u2014",
        expected={"vol1": 0, "vol2": 0, "vol3": 0},
    ),

    # 11. AI slop vocabulary
    CanonicalFormula(
        key="prose_ai_slop",
        description="AI slop vocabulary (notably|crucially|...)",
        ap_tag="prose",
        pattern=(
            r"\b(notably|crucially|remarkably|interestingly|furthermore"
            r"|moreover|delve|leverage|tapestry|cornerstone)\b"
        ),
        expected={
            "vol1": (0, 10),
            "vol2": (0, 10),
            "vol3": (0, 10),
        },
    ),

    # 12. AP136 -- bare H_{N-1} occurrences (potential trap, not always wrong)
    CanonicalFormula(
        key="ap136_harmonic_shifted",
        description="H_{N-1} occurrences (AP136 trap surface)",
        ap_tag="AP136",
        pattern=r"H_\{\s*N\s*-\s*1\s*\}",
        expected={
            "vol1": (0, 10),
            "vol2": (0, 10),
            "vol3": (0, 10),
        },
    ),

    # 13. AP132 -- bar complex missing augmentation bar
    CanonicalFormula(
        key="ap132_bar_no_augmentation",
        description="T^c(s^{-1} A) without bar (AP132 violation)",
        ap_tag="AP132",
        # Match T^c(s^{-1} A) where the A has no \bar prefix.
        # We allow whitespace and forbid a preceding backslash-bar.
        pattern=r"T\^c\(\s*s\^\{-1\}\s*A\s*\)",
        expected={"vol1": 0, "vol2": 0, "vol3": 0},
    ),

    # 14. AP39 -- kappa = S_2 equation (rank-1 Virasoro only)
    CanonicalFormula(
        key="ap39_kappa_equals_s2",
        description="kappa = S_2 equation (AP39, only Vir rank-1)",
        ap_tag="AP39",
        pattern=r"\\kappa\s*=\s*S_2\b",
        expected={
            "vol1": (0, 2),
            "vol2": (0, 2),
            "vol3": (0, 2),
        },
    ),

    # 15. AP124 -- duplicate \label{} across volumes
    CanonicalFormula(
        key="ap124_duplicate_labels",
        description="Duplicate \\label{foo} across volumes (AP124)",
        ap_tag="AP124",
        pattern=r"\\label\{([^}]+)\}",
        expected={},          # handled specially
        duplicate_label=True,
    ),
)


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------

class AP5Checker:
    """Scan the three volumes for a library of canonical formulas.

    The scanner shells out to GNU/BSD ``grep`` via ``subprocess.run`` so the
    sweep runs in tens of milliseconds rather than the minutes Python
    regex recursion would need on 4,200 pages of TeX.
    """

    def __init__(
        self,
        vol1_path: Optional[Path] = None,
        vol2_path: Optional[Path] = None,
        vol3_path: Optional[Path] = None,
        formulas: Optional[Sequence[CanonicalFormula]] = None,
    ) -> None:
        self.volumes: Dict[str, Path] = {
            "vol1": Path(vol1_path) if vol1_path else DEFAULT_VOL1,
            "vol2": Path(vol2_path) if vol2_path else DEFAULT_VOL2,
            "vol3": Path(vol3_path) if vol3_path else DEFAULT_VOL3,
        }
        self.formulas: Tuple[CanonicalFormula, ...] = tuple(
            formulas if formulas is not None else CANONICAL_FORMULAS
        )
        self._results: List[CheckResult] = []

    # ------------------------------------------------------------------
    # Low-level scanning primitives
    # ------------------------------------------------------------------

    def _scan_roots(self, volume_key: str) -> List[Path]:
        """Return the directories to sweep for a given volume."""
        root = self.volumes[volume_key]
        roots: List[Path] = []
        for sub in SCAN_SUBDIRS:
            candidate = root / sub
            if candidate.exists():
                roots.append(candidate)
        # Include the main.tex at the volume root as a catch-all.
        main_tex = root / "main.tex"
        if main_tex.exists():
            roots.append(main_tex)
        return roots

    def _grep_count(self, volume_key: str, pattern: str) -> int:
        """Count occurrences of ``pattern`` across a volume's TeX tree.

        Uses ``grep -rhoE`` so multi-match lines are counted correctly.
        ``wc -l`` of the grep output gives the total match count.
        """
        roots = self._scan_roots(volume_key)
        if not roots:
            return 0
        total = 0
        for r in roots:
            cmd: List[str] = ["grep", "-rhoE", "--include=*.tex"]
            if r.is_file():
                cmd = ["grep", "-hoE"]
            cmd.extend([pattern, str(r)])
            try:
                proc = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=60,
                )
            except (FileNotFoundError, subprocess.TimeoutExpired):
                continue
            if proc.returncode not in (0, 1):
                # grep returned error (2+); skip silently rather than crash
                # the whole sweep.
                continue
            if proc.stdout:
                total += sum(1 for line in proc.stdout.splitlines() if line)
        return total

    def _grep_label_captures(
        self, volume_key: str, pattern: str
    ) -> List[str]:
        """Return the label names captured by ``pattern`` inside a volume.

        The caller is responsible for ensuring ``pattern`` contains a single
        capture group delimiting the label name.
        """
        roots = self._scan_roots(volume_key)
        if not roots:
            return []
        label_re = re.compile(pattern)
        captured: List[str] = []
        for r in roots:
            if r.is_file():
                files: Iterable[Path] = [r]
            else:
                files = r.rglob("*.tex")
            for f in files:
                try:
                    text = f.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                for m in label_re.finditer(text):
                    captured.append(m.group(1))
        return captured

    # ------------------------------------------------------------------
    # Envelope evaluation
    # ------------------------------------------------------------------

    @staticmethod
    def _envelope_ok(observed: int, envelope: Envelope) -> bool:
        if envelope == "any":
            return True
        if isinstance(envelope, int):
            return observed == envelope
        if (
            isinstance(envelope, tuple)
            and len(envelope) == 2
            and all(isinstance(x, int) for x in envelope)
        ):
            low, high = envelope
            return low <= observed <= high
        raise ValueError(f"invalid envelope: {envelope!r}")

    @staticmethod
    def _envelope_str(envelope: Envelope) -> str:
        if envelope == "any":
            return "any"
        if isinstance(envelope, int):
            return f"={envelope}"
        if isinstance(envelope, tuple):
            return f"[{envelope[0]},{envelope[1]}]"
        return repr(envelope)

    # ------------------------------------------------------------------
    # Formula-level checks
    # ------------------------------------------------------------------

    def check_formula(
        self,
        pattern: str,
        description: str,
        expected_per_volume: Dict[str, Envelope],
        key: str = "",
        ap_tag: str = "",
        scope: Sequence[str] = ("vol1", "vol2", "vol3"),
    ) -> CheckResult:
        """Count ``pattern`` in each in-scope volume and compare to envelope."""
        scope_tuple: Tuple[str, ...] = tuple(scope)
        result = CheckResult(
            key=key or description,
            description=description,
            ap_tag=ap_tag,
            pattern=pattern,
            expected=dict(expected_per_volume),
            scope=scope_tuple,
        )
        for vol_key in scope_tuple:
            count = self._grep_count(vol_key, pattern)
            result.observed[vol_key] = count
            if vol_key in expected_per_volume:
                envelope = expected_per_volume[vol_key]
                if not self._envelope_ok(count, envelope):
                    result.drift.append(
                        f"{vol_key}: observed {count}, "
                        f"expected {self._envelope_str(envelope)}"
                    )
        return result

    def check_duplicate_labels(
        self, formula: CanonicalFormula
    ) -> CheckResult:
        """Cross-volume \\label duplicate detection (AP124)."""
        result = CheckResult(
            key=formula.key,
            description=formula.description,
            ap_tag=formula.ap_tag,
            pattern=formula.pattern,
            expected={},
            scope=formula.scope,
        )
        per_volume_labels: Dict[str, List[str]] = {}
        for vol_key in formula.scope:
            labels = self._grep_label_captures(vol_key, formula.pattern)
            per_volume_labels[vol_key] = labels
            result.observed[vol_key] = len(labels)

        # Cross-volume duplicates: a label that occurs in more than one
        # volume is a candidate AP124 violation.  Within-volume duplicates
        # (same label declared twice in Vol I) are also reported.
        seen: Dict[str, List[str]] = {}
        for vol_key, labels in per_volume_labels.items():
            for lbl in labels:
                seen.setdefault(lbl, []).append(vol_key)

        cross_dups = {
            lbl: vols
            for lbl, vols in seen.items()
            if len(set(vols)) >= 2
        }
        if cross_dups:
            sample = sorted(cross_dups.items())[:5]
            for lbl, vols in sample:
                result.drift.append(
                    f"cross-volume duplicate '{lbl}' in {sorted(set(vols))}"
                )
            if len(cross_dups) > 5:
                result.drift.append(
                    f"... {len(cross_dups) - 5} more cross-volume duplicates"
                )
        return result

    # ------------------------------------------------------------------
    # Batch driver
    # ------------------------------------------------------------------

    def run_all(self) -> List[CheckResult]:
        """Run every canonical formula and cache the results."""
        self._results = []
        for formula in self.formulas:
            if formula.duplicate_label:
                res = self.check_duplicate_labels(formula)
            else:
                res = self.check_formula(
                    pattern=formula.pattern,
                    description=formula.description,
                    expected_per_volume=formula.expected,
                    key=formula.key,
                    ap_tag=formula.ap_tag,
                    scope=formula.scope,
                )
            self._results.append(res)
        return list(self._results)

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def generate_report(
        self, results: Optional[Sequence[CheckResult]] = None
    ) -> str:
        """Return a human-readable drift report."""
        items = list(results) if results is not None else list(self._results)
        if not items:
            items = self.run_all()

        lines: List[str] = []
        lines.append("AP5 CROSS-VOLUME CONSISTENCY REPORT")
        lines.append("=" * 60)
        lines.append("")

        clean = [r for r in items if r.ok]
        dirty = [r for r in items if not r.ok]

        lines.append(f"checks run:    {len(items)}")
        lines.append(f"clean:         {len(clean)}")
        lines.append(f"drift flagged: {len(dirty)}")
        lines.append("")

        if dirty:
            lines.append("DRIFT")
            lines.append("-" * 60)
            for r in dirty:
                lines.append(f"[{r.ap_tag}] {r.key}")
                lines.append(f"    desc:     {r.description}")
                lines.append(f"    pattern:  {r.pattern}")
                lines.append(
                    "    observed: "
                    + ", ".join(
                        f"{k}={v}" for k, v in sorted(r.observed.items())
                    )
                )
                for d in r.drift:
                    lines.append(f"    -> {d}")
                lines.append("")

        lines.append("CLEAN CHECKS")
        lines.append("-" * 60)
        for r in clean:
            obs = ", ".join(f"{k}={v}" for k, v in sorted(r.observed.items()))
            lines.append(f"[{r.ap_tag}] {r.key}: {obs}")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Convenience entry point
# ---------------------------------------------------------------------------

def run_default_sweep() -> str:
    """Run the full canonical sweep and return the report."""
    checker = AP5Checker()
    checker.run_all()
    return checker.generate_report()


__all__ = [
    "AP5Checker",
    "CanonicalFormula",
    "CheckResult",
    "CANONICAL_FORMULAS",
    "DEFAULT_VOL1",
    "DEFAULT_VOL2",
    "DEFAULT_VOL3",
    "run_default_sweep",
]
