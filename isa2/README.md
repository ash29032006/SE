# ISA 2 — Calculator Module & Automated Quality Checks

## Overview
Python arithmetic module (`x.py`) with input validation, paired with a `unittest` (PyUnit) test suite (`test_x.py`) and a custom `.pylintrc` configuration, executed automatically in CI on every push and pull request.

## Files
| File | Description |
|---|---|
| `x.py` | Arithmetic operations (`add`, `subtract`, `multiply`, `divide`, `factorial`) with `ValueError` and `TypeError` validation |
| `test_x.py` | 18 `unittest` test cases covering normal, boundary, float, and error conditions |
| `.pylintrc` | Pylint configuration (`max-line-length = 100`, `good-names = i, j, k, n, a, b, x, y, _`) |

## Running Locally

### Run Unit Tests
```bash
python -m unittest discover -s isa2 -p "test_*.py" -v
```

### Run Pylint
```bash
pylint isa2/x.py --rcfile=isa2/.pylintrc
```
