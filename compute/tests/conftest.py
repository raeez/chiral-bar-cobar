"""Pytest configuration for compute tests."""

import sys
from pathlib import Path

# Add project root to path so 'compute.lib' imports work
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
