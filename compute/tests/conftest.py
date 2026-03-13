"""Pytest configuration for compute tests."""

import gc
import sys
from pathlib import Path

import pytest

# Add repo root to sys.path so 'compute.lib' imports resolve when running
# pytest from any working directory (e.g., `pytest compute/tests/`).
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


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


def pytest_runtest_teardown(item, nextitem):
    """Clear lru caches when transitioning between test modules.

    This fires after every test.  We only clear caches when the *next*
    test belongs to a different module (or there is no next test),
    avoiding unnecessary overhead within a single file.
    """
    if nextitem is None or item.module is not getattr(nextitem, "module", None):
        _clear_all_lru_caches()
        gc.collect()
