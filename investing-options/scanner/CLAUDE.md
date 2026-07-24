# Options Scanner

Python package that scans options premiums to find covered call and
cash-secured put opportunities. Uses setuptools (`setup.py`); Python 3.8+.

## Layout

- `src/options_scanner/` — package source; entry point is `scanner.py:main`
- `tests/` — pytest test suite
- `examples/` — usage examples
- `requirements.txt` — runtime dependencies
- `requirements-dev.txt` — dev dependencies (includes pytest)

## Commands

```bash
pip install -e ".[dev]"   # install with dev deps
python -m pytest tests/   # run tests
options-scanner           # run CLI entry point
```

## Conventions

- Source lives under `src/` (src layout — `package_dir={"": "src"}` in setup.py)
- Import as `from options_scanner.scanner import ...` not a relative path
- Tests live in `tests/`, not alongside source
