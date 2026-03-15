#!/usr/bin/env python3
"""Summarize full-suite shard logs by shard duration and slow nodeids."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


SHARD_TOTAL_RE = re.compile(
    r"=+\s+(?P<count>\d+) passed in (?P<seconds>[0-9.]+)s(?: \((?P<clock>[^)]+)\))?\s*=+"
)
DURATION_RE = re.compile(r"^\s*(?P<seconds>[0-9.]+)s call\s+(?P<nodeid>compute/.*)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze pytest shard logs.")
    default_log_dir = ".pytest-full-state"
    if not (Path(default_log_dir) / "pytest-full-shards").exists():
        default_log_dir = ".build_logs"
    parser.add_argument(
        "--log-dir",
        default=default_log_dir,
        help="Directory that contains pytest-full-shards.",
    )
    parser.add_argument(
        "--top-shards",
        type=int,
        default=15,
        help="Number of slowest shards to print.",
    )
    parser.add_argument(
        "--top-tests",
        type=int,
        default=20,
        help="Number of slowest individual tests to print.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    log_dir = Path(args.log_dir).resolve()
    shard_dir = log_dir / "pytest-full-shards"
    if not shard_dir.exists():
        raise SystemExit(f"missing shard log directory: {shard_dir}")

    shard_rows = []
    nodeid_durations: dict[str, float] = {}
    module_totals: defaultdict[str, float] = defaultdict(float)
    module_counts: defaultdict[str, int] = defaultdict(int)

    for path in sorted(shard_dir.glob("shard-*.log")):
        text = path.read_text(encoding="utf-8", errors="replace")
        total_match = SHARD_TOTAL_RE.search(text)
        if total_match:
            shard_rows.append(
                (
                    float(total_match.group("seconds")),
                    path.name,
                    int(total_match.group("count")),
                )
            )
        for line in text.splitlines():
            duration_match = DURATION_RE.match(line)
            if not duration_match:
                continue
            seconds = float(duration_match.group("seconds"))
            nodeid = duration_match.group("nodeid")
            nodeid_durations[nodeid] = max(seconds, nodeid_durations.get(nodeid, 0.0))
            module = nodeid.split("::", 1)[0]
            module_totals[module] += seconds
            module_counts[module] += 1

    shard_rows.sort(reverse=True)
    slow_tests = sorted(
        ((seconds, nodeid) for nodeid, seconds in nodeid_durations.items()),
        reverse=True,
    )
    slow_modules = sorted(
        (
            (total, module_counts[module], module)
            for module, total in module_totals.items()
        ),
        reverse=True,
    )

    print(f"Shard logs: {shard_dir}")
    print("")
    print("Slowest shards")
    for seconds, name, count in shard_rows[: args.top_shards]:
        print(f"{seconds:8.2f}s  {name}  tests={count}")

    print("")
    print("Slowest tests")
    for seconds, nodeid in slow_tests[: args.top_tests]:
        print(f"{seconds:8.2f}s  {nodeid}")

    print("")
    print("Heaviest modules")
    for total, count, module in slow_modules[:10]:
        average = total / count if count else 0.0
        print(f"{total:8.2f}s  avg={average:6.2f}s  samples={count:3d}  {module}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
