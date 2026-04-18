#!/usr/bin/env python3
"""
Phantom label detector v2 — AP286-aware, multi-line env-scan, alias-pair recognition.

Closes three detector gaps surfaced in Wave-17:

  (AP317) multi-line env-scan gap
    `\begin{env}[title]` and `\label{foo}` on separate lines evade
    single-line grep. v2 scans ±5 lines below every `\begin` header.

  (AP321) supervisor-grep-blind decorator-regex gap
    Narrow regex for one decorator form misses aliases. v2 matches the
    comprehensive union
      @independent_verification | @_iv\( | @_iv_v[0-9]+_[a-zA-Z_]+\(
        | TestGoldStandardDisjointPaths

  (AP286) umbrella-detection gap
    A `\phantomsection\label{foo}` adjacent to a canonical
    `\label{v1-foo}` / `\label{foo-inline}` (within 5 lines) OR followed
    by an in-line comment `% <target-path>:<line>` / `% target: label`
    pointing cross-volume is a LEGITIMATE semantic alias, not a phantom.

Per-volume classification:
  CLEAN                — label inscribed in a real environment
  AP286-ALIAS          — phantomsection adjacent to canonical inscription
  CROSS-VOL-UMBRELLA   — phantomsection + comment target verified in another volume
  AP255-PHANTOM        — genuine phantom (label cited but never inscribed)
  RETIRABLE-ORPHAN     — phantomsection with zero live-tex consumers
  AP316-WORKTREE       — hit lives in a worktree/backup/archive path (excluded)

Live-tex consumer filter excludes:
  relaunch_*, rectification_*, healing_*, opus_audit_*, wave*_audit_*,
  .claude/worktrees/*, notes/, adversarial_swarm_*/, backup*, archive*,
  fix_wave_*, _archive/*

Usage:
  python3 scripts/phantom_detector_v2.py
  python3 scripts/phantom_detector_v2.py --vol 1
  python3 scripts/phantom_detector_v2.py --json  # machine-readable report
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

VOL_ROOTS = {
    "vol1": Path("/Users/raeez/chiral-bar-cobar"),
    "vol2": Path("/Users/raeez/chiral-bar-cobar-vol2"),
    "vol3": Path("/Users/raeez/calabi-yau-quantum-groups"),
}

# Subtrees where "live" manuscript lives. Everything outside is excluded
# from both label-index construction AND consumer counting.
LIVE_SUBTREES = ("chapters", "standalone", "appendices", "main.tex")

# Path-substring exclusions for live-tex consumer filter (AP316 etc.).
EXCLUDED_SUBSTRINGS = (
    "relaunch_",
    "rectification_",
    "healing_",
    "opus_audit_",
    "_audit_",  # catches wave*_audit_*
    ".claude/worktrees/",
    "/notes/",
    "adversarial_swarm_",
    "/backup",
    "/archive",
    "fix_wave_",
    "/_archive/",
    ".bak",
    ".orig",
)

# --- Regex library ---------------------------------------------------------

PHANTOMSECTION_LABEL_RE = re.compile(
    r"\\phantomsection\s*\\label\{([^}]+)\}"
)
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(
    r"\\(?:ref|autoref|Cref|cref|eqref|nameref|hyperref)\{([^}]+)\}"
)
BEGIN_ENV_RE = re.compile(r"\\begin\{([a-zA-Z*]+)\}")
INLINE_COMMENT_TARGET_RE = re.compile(
    # match any .tex filename anywhere after the % sigil; tolerate free-form
    # intervening prose like "Vol II chapter " or "alias: this chapter ..."
    r"([A-Za-z0-9_\-/]+\.tex)(?::(\d+))?",
)
# Secondary cue: a comment that cites an alias-canonical pair like
# "thm:foo + thm:bar" or "thm:foo-canonical".
INLINE_COMMENT_ALIAS_RE = re.compile(
    r"alias:[^\n]*?([a-z]+:[A-Za-z0-9_\-]+)",
    re.IGNORECASE,
)

# Environments whose presence means "label foo is genuinely inscribed".
REAL_ENVS = {
    "theorem", "proposition", "lemma", "corollary", "conjecture",
    "definition", "remark", "example", "construction", "computation",
    "calculation", "maintheorem", "observation", "principle",
    "notation", "framework", "convention", "question", "openproblem",
    "setup", "strategy", "verification",
    # equation-like
    "equation", "align", "gather", "multline", "equation*",
    "align*", "gather*", "multline*",
    # miscellaneous structural labels
    "figure", "table",
}

# Comprehensive HZ-IV decorator regex (AP321 heal).
DECORATOR_RE = re.compile(
    r"@independent_verification|"
    r"@_iv\s*\(|"
    r"@_iv_v[0-9]+_[a-zA-Z_]+\s*\(|"
    r"class\s+TestGoldStandardDisjointPaths"
)

ENV_SCAN_WINDOW = 5   # lines below \begin{env} to search for \label (AP317)
ALIAS_ADJ_WINDOW = 5  # lines around phantomsection to look for canonical twin


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class LabelSite:
    label: str
    file: Path
    line: int
    kind: str  # "real" | "phantomsection"
    env: str = ""             # environment name if kind == "real"
    nearby_labels: list[str] = field(default_factory=list)
    nearby_comment_target: str = ""  # cross-vol file path from in-line comment

@dataclass
class Classification:
    label: str
    verdict: str  # CLEAN | AP286-ALIAS | CROSS-VOL-UMBRELLA | AP255-PHANTOM | RETIRABLE-ORPHAN
    volume: str
    site: LabelSite
    consumer_count: int
    note: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        d["site"] = {
            "label": self.site.label,
            "file": str(self.site.file),
            "line": self.site.line,
            "kind": self.site.kind,
            "env": self.site.env,
            "nearby_labels": self.site.nearby_labels,
            "nearby_comment_target": self.site.nearby_comment_target,
        }
        return d


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def is_live_path(p: Path, vol_root: Path) -> bool:
    try:
        rel = p.relative_to(vol_root)
    except ValueError:
        return False
    rel_s = str(rel)
    if any(x in rel_s for x in EXCLUDED_SUBSTRINGS):
        return False
    if rel_s == "main.tex":
        return True
    first = rel.parts[0] if rel.parts else ""
    return first in LIVE_SUBTREES


def iter_tex_files(vol_root: Path) -> Iterable[Path]:
    for sub in LIVE_SUBTREES:
        if sub == "main.tex":
            p = vol_root / "main.tex"
            if p.is_file():
                yield p
            continue
        base = vol_root / sub
        if not base.is_dir():
            continue
        for p in base.rglob("*.tex"):
            if is_live_path(p, vol_root):
                yield p


def strip_comments_keep_lines(text: str) -> list[str]:
    """Return per-line comment-stripped text but keep ORIGINAL lines too.

    We need originals to inspect in-line comments for the AP286 cross-vol
    target recognition; comment-stripped content is used for env/label
    detection.
    """
    stripped = []
    for line in text.splitlines():
        out = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                break
            out.append(line[i])
            i += 1
        stripped.append("".join(out))
    return stripped


# ---------------------------------------------------------------------------
# Pass 1: build label-site index (multi-line env-scan, AP317)
# ---------------------------------------------------------------------------

def index_labels(vol_root: Path) -> tuple[dict[str, list[LabelSite]], dict[Path, list[str]]]:
    """Return (label -> [LabelSite...], file -> raw_lines)."""
    idx: dict[str, list[LabelSite]] = defaultdict(list)
    file_raw: dict[Path, list[str]] = {}

    for path in iter_tex_files(vol_root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        raw_lines = text.splitlines()
        file_raw[path] = raw_lines
        stripped = strip_comments_keep_lines(text)

        # (A) phantomsection\label — scan the RAW text (comments stripped)
        for i, sline in enumerate(stripped):
            for m in PHANTOMSECTION_LABEL_RE.finditer(sline):
                label = m.group(1)

                # Adjacent-label sweep (AP286 detection) in stripped text
                lo = max(0, i - ALIAS_ADJ_WINDOW)
                hi = min(len(stripped), i + ALIAS_ADJ_WINDOW + 1)
                nearby = []
                for j in range(lo, hi):
                    if j == i:
                        continue
                    for lm in LABEL_RE.finditer(stripped[j]):
                        if PHANTOMSECTION_LABEL_RE.search(stripped[j]):
                            # skip other phantomsections
                            continue
                        nearby.append(lm.group(1))

                # In-line comment target (AP286 CROSS-VOL-UMBRELLA)
                comment_target = ""
                alias_target = ""
                raw_line = raw_lines[i] if i < len(raw_lines) else ""
                after_stripped = raw_line[len(sline):]
                cm = INLINE_COMMENT_TARGET_RE.search(after_stripped)
                if cm:
                    comment_target = cm.group(1)
                am = INLINE_COMMENT_ALIAS_RE.search(after_stripped)
                if am:
                    alias_target = am.group(1)

                site = LabelSite(
                    label=label, file=path, line=i + 1,
                    kind="phantomsection",
                    nearby_labels=nearby,
                    nearby_comment_target=comment_target,
                )
                # Stash alias_target via nearby_labels so classify() sees it.
                if alias_target:
                    site.nearby_labels = list(site.nearby_labels) + [alias_target]
                idx[label].append(site)

        # (B) real environments: scan \begin{env}, then sweep ±ENV_SCAN_WINDOW
        for i, sline in enumerate(stripped):
            for bm in BEGIN_ENV_RE.finditer(sline):
                env = bm.group(1)
                if env not in REAL_ENVS:
                    continue
                hi = min(len(stripped), i + ENV_SCAN_WINDOW + 1)
                for j in range(i, hi):
                    # stop if another \begin intervenes below i
                    if j > i and BEGIN_ENV_RE.search(stripped[j]):
                        break
                    for lm in LABEL_RE.finditer(stripped[j]):
                        if PHANTOMSECTION_LABEL_RE.search(stripped[j]):
                            continue
                        label = lm.group(1)
                        # Dedup: only record once per (label, file, line)
                        already = any(
                            s.kind == "real" and s.file == path and s.line == j + 1
                            for s in idx[label]
                        )
                        if not already:
                            idx[label].append(LabelSite(
                                label=label, file=path, line=j + 1,
                                kind="real", env=env,
                            ))

        # (C) plain \label outside of envs — equation-anchor labels. Record
        # as "real" with env="" only if not already matched above.
        for i, sline in enumerate(stripped):
            if PHANTOMSECTION_LABEL_RE.search(sline):
                continue
            for lm in LABEL_RE.finditer(sline):
                label = lm.group(1)
                if any(s.file == path and s.line == i + 1 for s in idx[label]):
                    continue
                idx[label].append(LabelSite(
                    label=label, file=path, line=i + 1,
                    kind="real", env="(bare)",
                ))

    return idx, file_raw


# ---------------------------------------------------------------------------
# Pass 2: live consumer counting
# ---------------------------------------------------------------------------

def count_consumers(label: str, vol_root: Path, file_raw: dict[Path, list[str]]) -> int:
    needle = f"{{{label}}}"
    count = 0
    for path, lines in file_raw.items():
        for ln in lines:
            # cheap containment filter then regex confirm
            if needle not in ln:
                continue
            for m in REF_RE.finditer(ln):
                if m.group(1) == label:
                    count += 1
    return count


# ---------------------------------------------------------------------------
# Pass 3: classification
# ---------------------------------------------------------------------------

def build_cross_vol_real_label_set() -> dict[str, set[str]]:
    """Real-label (kind='real') sets keyed by vol name, for CROSS-VOL-UMBRELLA."""
    out: dict[str, set[str]] = {}
    for vol, root in VOL_ROOTS.items():
        labels: set[str] = set()
        for path in iter_tex_files(root):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            stripped = strip_comments_keep_lines(text)
            for sline in stripped:
                if PHANTOMSECTION_LABEL_RE.search(sline):
                    continue
                for lm in LABEL_RE.finditer(sline):
                    labels.add(lm.group(1))
        out[vol] = labels
    return out


def alias_twin_label(label: str) -> set[str]:
    """Candidate canonical twin labels of a phantomsection label."""
    candidates = set()
    # v1-/v2-/v3- prefix variants
    if label.startswith(("v1-", "v2-", "v3-", "V1-", "V2-", "V3-")):
        candidates.add(label.split("-", 1)[1])
    else:
        for pfx in ("v1-", "v2-", "v3-", "V1-", "V2-", "V3-"):
            candidates.add(pfx + label)
    # -inline / -alias / -local suffix variants
    for sfx in ("-inline", "-alias", "-local", "-platonic"):
        if label.endswith(sfx):
            candidates.add(label[: -len(sfx)])
        else:
            candidates.add(label + sfx)
    return candidates


def classify(
    label: str,
    sites: list[LabelSite],
    vol: str,
    vol_root: Path,
    file_raw: dict[Path, list[str]],
    cross_vol_real: dict[str, set[str]],
) -> Classification:
    consumers = count_consumers(label, vol_root, file_raw)

    # If ANY real inscription exists in this volume, not a phantom.
    real_here = [s for s in sites if s.kind == "real"]
    phantoms_here = [s for s in sites if s.kind == "phantomsection"]

    if real_here:
        return Classification(
            label=label, verdict="CLEAN", volume=vol,
            site=real_here[0], consumer_count=consumers,
            note=f"real {real_here[0].env}",
        )

    # Only phantomsections for this label in this volume.
    # If none were ever seen, skip (shouldn't reach here).
    if not phantoms_here:
        return None  # type: ignore

    phantom = phantoms_here[0]

    # AP286 alias-pair: phantomsection adjacent to canonical twin label
    # inscribed in the SAME volume (same file window).
    twins = alias_twin_label(label)
    if any(t in phantom.nearby_labels for t in twins):
        return Classification(
            label=label, verdict="AP286-ALIAS", volume=vol,
            site=phantom, consumer_count=consumers,
            note=f"adjacent canonical twin in nearby_labels",
        )

    # Look up adjacent labels against the live real-label set of this vol.
    vol_real = cross_vol_real.get(vol, set())
    adj_canonical = [n for n in phantom.nearby_labels if n in vol_real]
    if adj_canonical:
        return Classification(
            label=label, verdict="AP286-ALIAS", volume=vol,
            site=phantom, consumer_count=consumers,
            note=f"adjacent real label: {adj_canonical[0]}",
        )

    # CROSS-VOL-UMBRELLA: in-line comment cites a path in another volume.
    # Three flavours accepted:
    #   (a) exact-label match in other vol at comment target
    #   (b) other-vol file exists; comment says "alias: foo" and foo is real there
    #   (c) other-vol file exists; label OR twin is real in that vol
    if phantom.nearby_comment_target:
        target_file = phantom.nearby_comment_target
        # scan just the basename against every tex file in other volumes
        basename = target_file.rsplit("/", 1)[-1]
        for other_vol, other_root in VOL_ROOTS.items():
            if other_vol == vol:
                continue
            # Try relative path first
            candidates = [other_root / target_file]
            # Search by basename if relative path miss
            for cand in other_root.rglob(basename):
                candidates.append(cand)
            if any(c.is_file() for c in candidates):
                # File exists cross-vol. Now try to confirm label linkage.
                for t in {label} | twins | set(phantom.nearby_labels):
                    if t in cross_vol_real.get(other_vol, set()):
                        return Classification(
                            label=label, verdict="CROSS-VOL-UMBRELLA", volume=vol,
                            site=phantom, consumer_count=consumers,
                            note=f"target file present in {other_vol}; linked via '{t}'",
                        )
                # File exists but no explicit label linkage — the comment
                # itself is the attribution; treat as umbrella if comment
                # explicitly declares "alias" or uses v1-/v2-/v3- prefix.
                raw_line = ""
                try:
                    raw_line = phantom.file.read_text(
                        encoding="utf-8", errors="ignore"
                    ).splitlines()[phantom.line - 1]
                except (OSError, IndexError):
                    pass
                if "alias:" in raw_line.lower() or "AP286" in raw_line:
                    return Classification(
                        label=label, verdict="CROSS-VOL-UMBRELLA", volume=vol,
                        site=phantom, consumer_count=consumers,
                        note=f"explicit alias: annotation to {other_vol}:{target_file}",
                    )

    # Implicit umbrella via twin: no comment, but a plausible twin is
    # inscribed in another volume.
    for other_vol in VOL_ROOTS:
        if other_vol == vol:
            continue
        for t in twins | {label}:
            if t in cross_vol_real.get(other_vol, set()):
                return Classification(
                    label=label, verdict="CROSS-VOL-UMBRELLA", volume=vol,
                    site=phantom, consumer_count=consumers,
                    note=f"implicit umbrella — twin '{t}' in {other_vol}",
                )

    # No comment target. Still: if label OR any twin is real in another vol,
    # it's an umbrella, not a phantom.
    for other_vol in VOL_ROOTS:
        if other_vol == vol:
            continue
        for t in twins | {label}:
            if t in cross_vol_real.get(other_vol, set()):
                return Classification(
                    label=label, verdict="CROSS-VOL-UMBRELLA", volume=vol,
                    site=phantom, consumer_count=consumers,
                    note=f"implicit umbrella — twin '{t}' in {other_vol}",
                )

    # No real inscription anywhere and no twin in other vols.
    if consumers == 0:
        return Classification(
            label=label, verdict="RETIRABLE-ORPHAN", volume=vol,
            site=phantom, consumer_count=0,
            note="phantomsection with zero live consumers",
        )
    return Classification(
        label=label, verdict="AP255-PHANTOM", volume=vol,
        site=phantom, consumer_count=consumers,
        note="no real inscription, no twin, has live consumers",
    )


# ---------------------------------------------------------------------------
# Main per-volume pipeline
# ---------------------------------------------------------------------------

def analyse_volume(vol: str, root: Path, cross_vol_real: dict[str, set[str]]) -> list[Classification]:
    idx, file_raw = index_labels(root)
    out: list[Classification] = []
    for label, sites in idx.items():
        # We only classify labels that have at least one phantomsection site.
        if not any(s.kind == "phantomsection" for s in sites):
            continue
        c = classify(label, sites, vol, root, file_raw, cross_vol_real)
        if c is not None:
            out.append(c)
    return out


def print_report(per_vol: dict[str, list[Classification]]) -> None:
    wave14_counts = {"vol1": 134, "vol2": 223, "vol3": 41}  # prior-session baselines
    print("=" * 72)
    print("Phantom Detector v2 — AP286/AP317/AP321-aware")
    print("=" * 72)
    for vol in ("vol1", "vol2", "vol3"):
        classifs = per_vol.get(vol, [])
        counts = Counter(c.verdict for c in classifs)
        total_phantom_candidates = len(classifs)
        ap255 = counts.get("AP255-PHANTOM", 0)
        print(f"\n[{vol}]  phantomsection-labels scanned: {total_phantom_candidates}")
        print(f"  Wave-14 naive grep count                : {wave14_counts[vol]}")
        print(f"  CLEAN                                   : {counts.get('CLEAN', 0)}")
        print(f"  AP286-ALIAS (canonical twin adjacent)   : {counts.get('AP286-ALIAS', 0)}")
        print(f"  CROSS-VOL-UMBRELLA (twin/target in ov)  : {counts.get('CROSS-VOL-UMBRELLA', 0)}")
        print(f"  RETIRABLE-ORPHAN (phantom, 0 consumers) : {counts.get('RETIRABLE-ORPHAN', 0)}")
        print(f"  AP255-PHANTOM (true phantom, live refs) : {ap255}")
        print(f"  TRUE PHANTOM COUNT                      : {ap255}")

        # Spotlight top-5 AP255 by consumer count
        ap255_list = [c for c in classifs if c.verdict == "AP255-PHANTOM"]
        ap255_list.sort(key=lambda c: -c.consumer_count)
        if ap255_list:
            print("  Top AP255-PHANTOM (by consumer count):")
            for c in ap255_list[:5]:
                rel = c.site.file.relative_to(VOL_ROOTS[vol])
                print(f"    {c.label:50s} refs={c.consumer_count:3d}  @ {rel}:{c.site.line}")

    print("\n" + "=" * 72)


def validate_top20(per_vol: dict[str, list[Classification]]) -> None:
    """Spot-check top-20 labels known to be AP286-legitimate post-Wave-14."""
    expected_legit = [
        "conj:master-bv-brst",
        "thm:topologization-tower",
        "thm:chiral-positselski-7-2",
        "conj:v1-master-bv-brst",
        "ch:k3-times-e",
        "chap:toroidal-elliptic",
        "chap:universal-holography-functor",
        "chap:chiral-higher-deligne",
        "prop:standard-strong-filtration",
        "rem:twining-genera",
        "V1-thm:koszul-reflection",
        "V1-chap:universal-conductor",
        "thm:chiral-positselski-5-3",
        "thm:chiral-positselski-5-2",
        "thm:grt1-rigidity",
        "thm:A-infinity-2",
        "thm:iterated-sugawara-construction",
        "thm:e-infinity-topologization-ladder",
        "thm:chiral-higher-deligne",
        "thm:universal-celestial-holography",
    ]
    print("\n[Top-20 AP286-legit validation]")
    all_classif = [c for vol_list in per_vol.values() for c in vol_list]
    by_label = defaultdict(list)
    for c in all_classif:
        by_label[c.label].append(c)
    legit_ok = 0
    absent = 0
    misclass = 0
    for lab in expected_legit:
        hits = by_label.get(lab, [])
        if not hits:
            # Could be cleanly inscribed already, or absent entirely.
            absent += 1
            print(f"  [ABSENT]      {lab}")
            continue
        best = hits[0]
        ok = best.verdict in ("AP286-ALIAS", "CROSS-VOL-UMBRELLA", "CLEAN")
        if ok:
            legit_ok += 1
            print(f"  [{best.verdict:18s}] {lab}  ({best.volume}, refs={best.consumer_count})")
        else:
            misclass += 1
            print(f"  [MISCLASS={best.verdict}] {lab}  ({best.volume})")
    print(f"  Summary: legit-ok={legit_ok}  absent={absent}  misclass={misclass}  of 20")


# ---------------------------------------------------------------------------
# CLI entry
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vol", choices=("1", "2", "3", "all"), default="all")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-validate", action="store_true")
    args = ap.parse_args()

    cross_vol_real = build_cross_vol_real_label_set()

    target_vols = (
        ["vol" + args.vol] if args.vol in ("1", "2", "3")
        else ["vol1", "vol2", "vol3"]
    )
    per_vol: dict[str, list[Classification]] = {}
    for vol in target_vols:
        per_vol[vol] = analyse_volume(vol, VOL_ROOTS[vol], cross_vol_real)

    if args.json:
        payload = {
            vol: [c.to_dict() for c in classifs]
            for vol, classifs in per_vol.items()
        }
        print(json.dumps(payload, indent=2, default=str))
        return 0

    print_report(per_vol)
    if not args.no_validate:
        validate_top20(per_vol)
    return 0


if __name__ == "__main__":
    sys.exit(main())
