#!/usr/bin/env python3
"""Resumable shard runner for the full compute pytest suite.

This keeps the slow-suite lock for the whole orchestration, executes the
collected nodeids in bounded shards, emits heartbeat lines during long
symbolic runs, and checkpoints completed shards so an interrupted wrapper
can resume instead of restarting from 0%. The checkpointed shard state can
live outside the shared build-log directory so unrelated TeX/build work
does not erase the full-suite resume surface.
"""

from __future__ import annotations

import argparse
import fcntl
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Iterable, Sequence


PARENT_LOCK_ENV = "PYTEST_SLOW_SUITE_PARENT_TOKEN"
DEFAULT_HEARTBEAT_SECONDS = 60
DEFAULT_NODEIDS_PER_SHARD = 10
DEFAULT_DURATIONS = 20
DEFAULT_DURATIONS_MIN = 5.0
DEFAULT_TARGET_SECONDS_PER_SHARD = 60.0

SHARD_TOTAL_RE = re.compile(
    r"=+\s+(?P<count>\d+) passed in (?P<seconds>[0-9.]+)s(?: \((?P<clock>[^)]+)\))?\s*=+"
)
DURATION_RE = re.compile(r"^\s*(?P<seconds>[0-9.]+)s call\s+(?P<nodeid>compute/.*)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the full pytest suite in resumable shards.",
    )
    parser.add_argument(
        "--python-bin",
        default=sys.executable,
        help="Python interpreter used to launch pytest subprocesses.",
    )
    parser.add_argument(
        "--log-dir",
        required=True,
        help="Directory that receives the user-facing runner log and lock file.",
    )
    parser.add_argument(
        "--state-dir",
        default=None,
        help=(
            "Directory that receives checkpoint state, durations, and shard logs. "
            "Defaults to --log-dir."
        ),
    )
    parser.add_argument(
        "--faulthandler-timeout",
        type=int,
        required=True,
        help="Per-test faulthandler timeout forwarded to pytest.",
    )
    parser.add_argument(
        "--heartbeat-seconds",
        type=int,
        default=DEFAULT_HEARTBEAT_SECONDS,
        help="Emit a progress heartbeat after this many seconds of shard silence.",
    )
    parser.add_argument(
        "--max-nodeids-per-shard",
        type=int,
        default=DEFAULT_NODEIDS_PER_SHARD,
        help="Maximum number of collected nodeids to execute in a single shard.",
    )
    parser.add_argument(
        "--target-seconds-per-shard",
        type=float,
        default=DEFAULT_TARGET_SECONDS_PER_SHARD,
        help="Soft target for predicted shard runtime based on historical durations.",
    )
    parser.add_argument(
        "--durations",
        type=int,
        default=DEFAULT_DURATIONS,
        help="Forwarded to pytest --durations.",
    )
    parser.add_argument(
        "--durations-min",
        type=float,
        default=DEFAULT_DURATIONS_MIN,
        help="Forwarded to pytest --durations-min.",
    )
    parser.add_argument(
        "targets",
        nargs="*",
        default=["compute/tests/"],
        help="Pytest collection targets for the full suite.",
    )
    return parser.parse_args()


class RunnerLog:
    """Print to stdout and mirror the same lines to the runner log."""

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def reset(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("", encoding="utf-8")

    def write(self, message: str) -> None:
        text = message.rstrip()
        print(text, flush=True)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(text + "\n")


class ShardFailure(RuntimeError):
    """Structured shard failure so the runner can salvage partial progress."""

    def __init__(
        self,
        message: str,
        *,
        returncode: int,
        shard_log_path: Path,
        nodeids: Sequence[str],
    ) -> None:
        super().__init__(message)
        self.returncode = returncode
        self.shard_log_path = shard_log_path
        self.nodeids = tuple(nodeids)


class SlowSuiteOwner:
    """Acquire the repo-wide slow-suite lock for the whole shard runner."""

    def __init__(self, lock_path: Path, repo_root: Path):
        self.lock_path = lock_path
        self.repo_root = repo_root
        self.handle = None
        self.token = uuid.uuid4().hex

    def acquire(self) -> None:
        self.lock_path.parent.mkdir(parents=True, exist_ok=True)
        handle = self.lock_path.open("a+", encoding="utf-8")
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            handle.seek(0)
            owner = handle.read().strip()
            handle.close()
            raise RuntimeError(
                "another --run-slow pytest session already owns "
                f"{self.lock_path}"
                + (f" ({owner})" if owner else "")
                + "; exiting to avoid concurrent slow-suite contention"
            ) from None

        handle.seek(0)
        handle.truncate()
        handle.write(
            "runner_token="
            f"{self.token} "
            f"pid={os.getpid()} "
            f"cwd={self.repo_root} "
            f"argv={' '.join(sys.argv)}\n"
        )
        handle.flush()
        self.handle = handle

    def release(self) -> None:
        if self.handle is None:
            return
        try:
            self.handle.seek(0)
            self.handle.truncate()
            self.handle.flush()
            fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
        finally:
            self.handle.close()
            self.handle = None

    def child_env(self) -> dict[str, str]:
        env = os.environ.copy()
        env[PARENT_LOCK_ENV] = self.token
        return env


def hash_nodeids(nodeids: Sequence[str]) -> str:
    payload = json.dumps(list(nodeids), separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def extract_passed_nodeids(shard_log_path: Path) -> tuple[str, ...]:
    nodeids = []
    if not shard_log_path.exists():
        return ()
    for line in shard_log_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if " PASSED" not in line:
            continue
        stripped = line.strip()
        if stripped.startswith("compute/"):
            nodeids.append(stripped.split(" PASSED", 1)[0])
    return tuple(nodeids)


def load_completed_nodeids(state_path: Path, nodeids_hash: str, shard_log_dir: Path) -> set[str]:
    if not state_path.exists():
        return set()
    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set()
    completed_nodeids = data.get("completed_nodeids")
    if isinstance(completed_nodeids, list):
        if data.get("nodeids_hash") != nodeids_hash:
            return set()
        return {str(nodeid) for nodeid in completed_nodeids}

    # Legacy fallback: reconstruct completed nodeids from the old shard-index state.
    completed = set()
    for index in data.get("completed_shards", []):
        try:
            shard_index = int(index)
        except (TypeError, ValueError):
            continue
        shard_log_path = shard_log_dir / f"shard-{shard_index:03d}.log"
        completed.update(extract_passed_nodeids(shard_log_path))
    return completed


def extract_nodeid_durations(shard_log_path: Path) -> dict[str, float]:
    durations: dict[str, float] = {}
    if not shard_log_path.exists():
        return durations
    for line in shard_log_path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = DURATION_RE.match(line)
        if not match:
            continue
        durations[match.group("nodeid")] = float(match.group("seconds"))
    return durations


def load_duration_estimates(duration_path: Path, shard_log_dir: Path) -> dict[str, float]:
    durations: dict[str, float] = {}
    if duration_path.exists():
        try:
            data = json.loads(duration_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
        for nodeid, seconds in data.items():
            try:
                durations[str(nodeid)] = float(seconds)
            except (TypeError, ValueError):
                continue
    for shard_log_path in sorted(shard_log_dir.glob("shard-*.log")):
        for nodeid, seconds in extract_nodeid_durations(shard_log_path).items():
            durations[nodeid] = seconds
    return durations


def save_duration_estimates(duration_path: Path, durations: dict[str, float]) -> None:
    temp_path = duration_path.with_suffix(duration_path.suffix + ".tmp")
    payload = {nodeid: durations[nodeid] for nodeid in sorted(durations)}
    temp_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temp_path.replace(duration_path)


def save_completed_nodeids(
    state_path: Path,
    nodeids_hash: str,
    completed_nodeids: Iterable[str],
) -> None:
    payload = {
        "nodeids_hash": nodeids_hash,
        "completed_nodeids": sorted(set(str(nodeid) for nodeid in completed_nodeids)),
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    temp_path = state_path.with_suffix(state_path.suffix + ".tmp")
    temp_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temp_path.replace(state_path)


def collect_nodeids(
    python_bin: str,
    targets: Sequence[str],
    env: dict[str, str],
    repo_root: Path,
) -> list[str]:
    command = [
        python_bin,
        "-m",
        "pytest",
        *targets,
        "--collect-only",
        "-q",
        "--run-slow",
    ]
    result = subprocess.run(
        command,
        cwd=repo_root,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stdout + "\n" + result.stderr).strip()
        raise RuntimeError("pytest collection failed:\n" + detail)
    nodeids = []
    for line in result.stdout.splitlines():
        stripped = line.strip()
        if stripped.startswith("compute/") and ".py" in stripped:
            nodeids.append(stripped)
    if not nodeids:
        raise RuntimeError("pytest collection returned no nodeids for the requested targets")
    return nodeids


def build_shards(
    nodeids: Sequence[str],
    max_nodeids_per_shard: int,
    target_seconds_per_shard: float,
    duration_estimates: dict[str, float] | None = None,
) -> list[list[str]]:
    if max_nodeids_per_shard <= 0:
        raise ValueError("max-nodeids-per-shard must be positive")
    if target_seconds_per_shard <= 0:
        raise ValueError("target-seconds-per-shard must be positive")
    duration_estimates = duration_estimates or {}
    shards: list[list[str]] = []
    current: list[str] = []
    current_module: str | None = None
    current_seconds = 0.0
    for nodeid in nodeids:
        module = nodeid.split("::", 1)[0]
        predicted_seconds = duration_estimates.get(nodeid, 1.0)
        if current and (
            module != current_module
            or len(current) >= max_nodeids_per_shard
            or (
                current_seconds > 0
                and current_seconds + predicted_seconds > target_seconds_per_shard
            )
        ):
            shards.append(current)
            current = []
            current_seconds = 0.0
        if not current:
            current_module = module
        current.append(nodeid)
        current_seconds += predicted_seconds
    if current:
        shards.append(current)
    return shards


def tail_lines(path: Path, count: int) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8", errors="replace").splitlines()[-count:]


def last_nonempty_line(path: Path) -> str:
    for line in reversed(tail_lines(path, 40)):
        stripped = line.strip()
        if stripped:
            return stripped
    return "(waiting for pytest output)"


def format_elapsed(seconds: float) -> str:
    total_seconds = int(seconds)
    hours, rem = divmod(total_seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def run_shard(
    shard_index: int,
    shard_count: int,
    nodeids: Sequence[str],
    args: argparse.Namespace,
    env: dict[str, str],
    repo_root: Path,
    shard_log_path: Path,
    log: RunnerLog,
) -> None:
    shard_log_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        args.python_bin,
        "-m",
        "pytest",
        "-vv",
        "-ra",
        "--run-slow",
        "-o",
        f"faulthandler_timeout={args.faulthandler_timeout}",
        "-o",
        "faulthandler_exit_on_timeout=true",
        f"--durations={args.durations}",
        f"--durations-min={args.durations_min}",
        *nodeids,
    ]
    head = nodeids[0]
    tail = nodeids[-1]
    log.write(
        f"[shard {shard_index}/{shard_count}] start "
        f"{len(nodeids)} nodeids | first={head} | last={tail}"
    )
    start = time.monotonic()
    with shard_log_path.open("w", encoding="utf-8") as handle:
        process = subprocess.Popen(
            command,
            cwd=repo_root,
            env=env,
            stdout=handle,
            stderr=subprocess.STDOUT,
            text=True,
        )
    next_heartbeat = start + max(1, args.heartbeat_seconds)
    while True:
        returncode = process.poll()
        if returncode is not None:
            elapsed = format_elapsed(time.monotonic() - start)
            if returncode == 0:
                log.write(f"[shard {shard_index}/{shard_count}] passed in {elapsed}")
                for line in tail_lines(shard_log_path, 3):
                    log.write(f"  {line}")
                return
            log.write(
                f"[shard {shard_index}/{shard_count}] failed with exit code {returncode} "
                f"after {elapsed}"
            )
            for line in tail_lines(shard_log_path, 120):
                log.write(line)
            raise ShardFailure(
                f"pytest shard {shard_index}/{shard_count} failed; see {shard_log_path}",
                returncode=returncode,
                shard_log_path=shard_log_path,
                nodeids=nodeids,
            )
        now = time.monotonic()
        if now >= next_heartbeat:
            elapsed = format_elapsed(now - start)
            log.write(
                f"[heartbeat shard {shard_index}/{shard_count}] elapsed={elapsed} "
                f"last={last_nonempty_line(shard_log_path)}"
            )
            next_heartbeat = now + max(1, args.heartbeat_seconds)
        time.sleep(min(0.2, max(0.05, next_heartbeat - now)))


def install_signal_handlers() -> None:
    def _raise_interrupt(_signum, _frame):
        raise KeyboardInterrupt

    signal.signal(signal.SIGINT, _raise_interrupt)
    signal.signal(signal.SIGTERM, _raise_interrupt)


def main() -> int:
    args = parse_args()
    install_signal_handlers()

    repo_root = Path(__file__).resolve().parents[2]
    log_dir = Path(args.log_dir).resolve()
    state_dir = Path(args.state_dir).resolve() if args.state_dir else log_dir
    state_dir.mkdir(parents=True, exist_ok=True)
    state_path = state_dir / "pytest-full.state.json"
    duration_path = state_dir / "pytest-full.durations.json"
    shard_log_dir = state_dir / "pytest-full-shards"
    lock_path = log_dir / "pytest-slow.lock"
    owner = SlowSuiteOwner(lock_path=lock_path, repo_root=repo_root)

    try:
        owner.acquire()
    except RuntimeError as exc:
        print(str(exc), flush=True)
        return 0

    try:
        runner_log = RunnerLog(log_dir / "pytest-full.log")
        child_env = owner.child_env()
        nodeids = collect_nodeids(
            python_bin=args.python_bin,
            targets=args.targets,
            env=child_env,
            repo_root=repo_root,
        )
        nodeids_hash = hash_nodeids(nodeids)
        duration_estimates = load_duration_estimates(duration_path, shard_log_dir)
        completed_nodeids = load_completed_nodeids(state_path, nodeids_hash, shard_log_dir)
        pending_nodeids = [nodeid for nodeid in nodeids if nodeid not in completed_nodeids]
        shards = build_shards(
            pending_nodeids,
            args.max_nodeids_per_shard,
            args.target_seconds_per_shard,
            duration_estimates=duration_estimates,
        )
        if not completed_nodeids:
            runner_log.reset()
        if completed_nodeids:
            runner_log.write(
                "Resuming pytest-full from checkpoint: "
                f"{len(completed_nodeids)}/{len(nodeids)} nodeids already passed; "
                f"{len(pending_nodeids)} remain in {len(shards)} shards."
            )
        else:
            runner_log.write(
                f"Starting pytest-full: {len(nodeids)} collected nodeids across {len(shards)} shards."
            )
        runner_log.write(
            "Shard policy: "
            f"max_nodeids={args.max_nodeids_per_shard}, "
            f"target_seconds={args.target_seconds_per_shard:.1f}, "
            f"historical_durations={len(duration_estimates)}"
        )

        if not pending_nodeids:
            if state_path.exists():
                state_path.unlink()
            runner_log.write("Full pytest suite already completed.")
            runner_log.write(f"Shard logs: {shard_log_dir}")
            return 0

        shard_queue = [list(shard) for shard in shards]
        shard_index = 0
        while shard_index < len(shard_queue):
            shard = shard_queue[shard_index]
            display_index = shard_index + 1
            shard_log_path = shard_log_dir / f"shard-{display_index:03d}.log"
            try:
                run_shard(
                    shard_index=display_index,
                    shard_count=len(shard_queue),
                    nodeids=shard,
                    args=args,
                    env=child_env,
                    repo_root=repo_root,
                    shard_log_path=shard_log_path,
                    log=runner_log,
                )
            except ShardFailure as exc:
                duration_estimates.update(extract_nodeid_durations(exc.shard_log_path))
                save_duration_estimates(duration_path, duration_estimates)

                passed_nodeids = extract_passed_nodeids(exc.shard_log_path)
                if passed_nodeids:
                    completed_nodeids.update(passed_nodeids)
                    save_completed_nodeids(state_path, nodeids_hash, completed_nodeids)
                    runner_log.write(
                        f"[shard {display_index}/{len(shard_queue)}] salvaged "
                        f"{len(passed_nodeids)} passed nodeids before failure"
                    )

                remaining_nodeids = [
                    nodeid for nodeid in shard if nodeid not in completed_nodeids
                ]
                if not remaining_nodeids:
                    runner_log.write(
                        f"[shard {display_index}/{len(shard_queue)}] no nodeids remain after salvage; continuing"
                    )
                    shard_index += 1
                    continue

                if exc.returncode < 0 and len(remaining_nodeids) > 1:
                    midpoint = max(1, len(remaining_nodeids) // 2)
                    left = remaining_nodeids[:midpoint]
                    right = remaining_nodeids[midpoint:]
                    runner_log.write(
                        f"[shard {display_index}/{len(shard_queue)}] hard failure exit {exc.returncode}; "
                        f"splitting remaining {len(remaining_nodeids)} nodeids into "
                        f"{len(left)} and {len(right)}"
                    )
                    shard_queue[shard_index : shard_index + 1] = [left, right]
                    continue
                raise

            duration_estimates.update(extract_nodeid_durations(shard_log_path))
            save_duration_estimates(duration_path, duration_estimates)
            completed_nodeids.update(shard)
            save_completed_nodeids(state_path, nodeids_hash, completed_nodeids)
            shard_index += 1

        if state_path.exists():
            state_path.unlink()
        runner_log.write("Full pytest suite passed.")
        runner_log.write(f"Shard logs: {shard_log_dir}")
        return 0
    except KeyboardInterrupt:
        runner_log.write(
            "pytest-full interrupted; completed shards were checkpointed and will resume on the next run."
        )
        return 130
    except RuntimeError as exc:
        runner_log.write(str(exc))
        return 1
    finally:
        owner.release()


if __name__ == "__main__":
    raise SystemExit(main())
