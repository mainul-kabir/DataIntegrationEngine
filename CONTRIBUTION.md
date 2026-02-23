## Contribution Summary

### What this repo does
This repository provides a CLI-based Data Integration Engine for New Mexico water data. It fetches, normalizes, and exports groundwater level and water quality data from multiple agencies into unified outputs (summary/time-series/sites).

### Improvement made
1. CLI bugfix in `frontend/cli.py`
   - Corrected `--no-*` flags to default to `False` (they were incorrectly `True`).
   - Corrected source mapping logic to `use_source_<agency> = not no_<agency>` for `weave` and `sites`.
2. Test additions
   - Added `tests/test_cli/test_flags.py` to ensure `--no-wqp` excludes WQP.
   - Added missing `tests/test_cli/test_bor.py` with BoR parameter support mapping.
3. README updates
   - Added a `Running Tests` section (full suite, single file, single test).
   - Added a source-exclusion CLI usage example.
   - Corrected BoR bicarbonate support in the parameter matrix.
   - Fixed a typo ("Initiative").

### Why this was chosen
This was a high-impact, low-risk fix: it corrected behavior users rely on (`--no-*` semantics), aligned implementation with documentation, and added regression tests to prevent the bug from returning.

### What I would do next with more time
1. Add CLI tests for `sites` exclusion behavior across all sources.
2. Add parameterized tests for every `--no-*` flag.
3. Clean up remaining ad-hoc `print()` calls and standardize logging/test diagnostics.
4. Implement the remaining in-development geographic and date filters end-to-end (`--bbox`, `--county`, `--wkt`, `--start-date`, `--end-date`) in the data retrieval pipeline.

### Running/testing instructions
Run full suite:

```bash
pytest
```

Run one file:

```bash
pytest tests/test_cli/test_bor.py
```

Run one specific test:

```bash
pytest tests/test_cli/test_flags.py::test_weave_no_source_flag_excludes_source
```
