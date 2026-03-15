"""Pytest configuration for compute tests."""

import gc
import os
import sys
from pathlib import Path

import fcntl

import pytest

# Add repo root to sys.path so 'compute.lib' imports resolve when running
# pytest from any working directory (e.g., `pytest compute/tests/`).
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


_SLOW_SUITE_LOCK_HANDLE = None
_SLOW_SUITE_LOCK_PATH = Path(__file__).resolve().parents[2] / ".build_logs" / "pytest-slow.lock"
_SLOW_SUITE_PARENT_TOKEN_ENV = "PYTEST_SLOW_SUITE_PARENT_TOKEN"


def _clear_all_lru_caches():
    """Clear all lru_cache instances in compute.lib modules.

    When running the full test suite in a single process, unbounded
    lru_cache entries accumulate across test files and can push RSS
    well past 10 GB.  Clearing caches between modules keeps memory
    bounded without affecting correctness (caches are transparent).
    """
    for name, mod in list(sys.modules.items()):
        if not name.startswith("compute.lib"):
            continue
        for attr_name in dir(mod):
            obj = getattr(mod, attr_name, None)
            if callable(getattr(obj, "cache_clear", None)):
                obj.cache_clear()


def pytest_addoption(parser):
    """Add an explicit opt-in for slow tests.

    The repo's default iteration target is the fast suite; heavy symbolic
    Drinfeld--Sokolov / PBW jobs are marked ``slow`` and should run only
    when explicitly requested.
    """
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="run tests marked slow",
    )


def pytest_collection_modifyitems(config, items):
    """Deselect slow tests unless the caller explicitly opts in."""
    if config.getoption("--run-slow"):
        return

    keep = []
    deselected = []
    for item in items:
        if "slow" in item.keywords:
            deselected.append(item)
        else:
            keep.append(item)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = keep


def _acquire_slow_suite_lock(config):
    """Allow only one `--run-slow` pytest owner at a time.

    Codex can keep multiple live desktop threads open in the same repo.
    When two sibling threads launch slow symbolic DS suites concurrently,
    they contend for memory and make `make test-full` non-diagnostic.
    """
    global _SLOW_SUITE_LOCK_HANDLE

    if not config.getoption("--run-slow"):
        return

    # The shard runner may hold the repo-wide flock across multiple child
    # pytest invocations.  Those children inherit a token that proves the
    # parent already owns the lock, so they should not try to re-acquire it.
    parent_token = os.environ.get(_SLOW_SUITE_PARENT_TOKEN_ENV)
    if parent_token and _SLOW_SUITE_LOCK_PATH.exists():
        owner = _SLOW_SUITE_LOCK_PATH.read_text(encoding="utf-8").strip()
        if f"runner_token={parent_token}" in owner:
            return

    _SLOW_SUITE_LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    handle = _SLOW_SUITE_LOCK_PATH.open("a+", encoding="utf-8")
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        handle.seek(0)
        owner = handle.read().strip()
        handle.close()
        pytest.exit(
            "another --run-slow pytest session already owns "
            f"{_SLOW_SUITE_LOCK_PATH}"
            + (f" ({owner})" if owner else "")
            + "; exiting to avoid concurrent slow-suite contention",
            returncode=0,
        )

    handle.seek(0)
    handle.truncate()
    handle.write(
        f"pid={os.getpid()} cwd={Path.cwd()} argv={' '.join(sys.argv)}\n"
    )
    handle.flush()
    _SLOW_SUITE_LOCK_HANDLE = handle


def _release_slow_suite_lock():
    """Release the slow-suite interprocess lock if this session owns it."""
    global _SLOW_SUITE_LOCK_HANDLE

    if _SLOW_SUITE_LOCK_HANDLE is None:
        return

    try:
        _SLOW_SUITE_LOCK_HANDLE.seek(0)
        _SLOW_SUITE_LOCK_HANDLE.truncate()
        _SLOW_SUITE_LOCK_HANDLE.flush()
        fcntl.flock(_SLOW_SUITE_LOCK_HANDLE.fileno(), fcntl.LOCK_UN)
    finally:
        _SLOW_SUITE_LOCK_HANDLE.close()
        _SLOW_SUITE_LOCK_HANDLE = None


def pytest_sessionstart(session):
    """Acquire the slow-suite lock before collection/running begins."""
    _acquire_slow_suite_lock(session.config)


def pytest_sessionfinish(session, exitstatus):
    """Release the slow-suite lock when the session ends."""
    _release_slow_suite_lock()


def pytest_runtest_teardown(item, nextitem):
    """Clear lru caches when transitioning between test modules.

    This fires after every test.  We only clear caches when the *next*
    test belongs to a different module (or there is no next test),
    avoiding unnecessary overhead within a single file.
    """
    if nextitem is None or item.module is not getattr(nextitem, "module", None):
        _clear_all_lru_caches()
        gc.collect()
