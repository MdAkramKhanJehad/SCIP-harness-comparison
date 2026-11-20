# vvaharness/models/ruff.toml

Role: typing/tooling/package metadata; no scan stage introduced.

Exact source asset: `assets/original/vvaharness/models/ruff.toml`. SHA-256 `c25170b65b1ac4a6c8cf86bb683a30a4bb90046721ebbe860ee1e73008b3705b`.

```sudo
// Source: vvaharness/models/ruff.toml:1-54
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| line-length | 100 |
| target-version | "py311" |
| lint.select | ["E", "W", "F", "I", "N", "UP", "B", "SIM", "RET", "TRY", "C90", "PLR", "ANN", "D", "PTH", "RUF", "ARG", "C4", "PERF", "PIE", "DTZ", "ISC", "A", "S"] |
| lint.ignore | ["TRY003", "D203", "D213", "ANN401"] |
| lint.extend-select | ["TRY201", "TRY300", "TRY301", "TRY400", "SIM910"] |
| lint.per-file-ignores.__init__.py | ["D104", "F401"] |
| lint.per-file-ignores.**/test_*.py | ["S101", "ANN", "D", "PLR2004"] |
| lint.mccabe.max-complexity | 6 |
| lint.pylint.max-args | 5 |
| lint.pylint.max-branches | 4 |
| lint.pylint.max-returns | 3 |
| lint.pylint.max-statements | 30 |
| lint.pydocstyle.convention | "google" |
| lint.isort.known-first-party | ["vvaharness"] |
| format.quote-style | "double" |
