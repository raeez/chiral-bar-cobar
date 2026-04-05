---
description: "Scaffold a new compute engine with multi-path tests"
---

# New Compute Engine Scaffold

**Engine name/topic**: $ARGUMENTS

Create a new compute module following the project's verification-engine pattern.

## Protocol

### 1. Survey existing infrastructure
```bash
ls ~/chiral-bar-cobar/compute/lib/
ls ~/chiral-bar-cobar/compute/tests/
```

### 2. Create the engine module

File: `compute/lib/{name}_engine.py`

Structure:
```python
"""
{Name} Engine — {brief description}

Part of the verification engine for the modular Koszul duality programme.
Every function corresponds to a formula in the manuscript; every test
verifies it by at least 2 independent methods.

References:
- [manuscript location]
- [literature source if applicable]
"""

from fractions import Fraction
# Import from existing engines as needed
```

### 3. Create the test suite

File: `compute/tests/test_{name}_engine.py`

Structure:
```python
"""
Tests for {name}_engine.py

Multi-path verification mandate: every numerical claim needs 3+ independent paths.
AP10: Never hardcode expected values without cross-check.
"""

import pytest
from compute.lib.{name}_engine import *

class TestBasicIdentities:
    """Direct computation vs alternative formula."""
    pass

class TestLimitingCases:
    """Special cases: k=0, c=0, N=1, genus=0, etc."""
    pass

class TestCrossFamilyConsistency:
    """Additivity, multiplicativity, functoriality across families."""
    pass

class TestDualityRelations:
    """Complementarity, level-rank, DS reduction, Feigin-Frenkel."""
    pass

class TestLiteratureComparison:
    """Comparison with published values (AP38: record source + convention)."""
    pass
```

### 4. Multi-path verification standard

Every test class should encode a DIFFERENT verification path. A test that passes because it compares one computation to itself (AP10) is worthless. The test suite is the manuscript's immune system.

### 5. Run and verify
```bash
cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/test_{name}_engine.py -v
```

### 6. Integration

- Add imports to `compute/lib/__init__.py` if it exists
- Cross-reference with manuscript location
- Update concordance.tex if the engine verifies a claim

Target: minimum 30 tests per engine, minimum 3 verification paths per formula.
