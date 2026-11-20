# vvaharness/backends/harness/ruff.toml

Role: typing/tooling/package metadata; no scan stage introduced.

Exact source asset: `assets/original/vvaharness/backends/harness/ruff.toml`. SHA-256 `56f9762700faf56a310222928f0e818966fa7a819cf3e409037c4b802342e72e`.

```sudo
// Source: vvaharness/backends/harness/ruff.toml:1-65
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| extend | "../ruff.toml" |
| lint.per-file-ignores.**/__init__.py | ["D104", "F401"] |
| lint.per-file-ignores.**/claude/client.py | ["C901", "PLR0912", "PLR0915"] |
| lint.per-file-ignores.**/claude/options.py | ["PLR0912"] |
| lint.per-file-ignores.**/deepagents/client.py | ["C901", "PLR0912"] |
| lint.per-file-ignores.**/deepagents/translate.py | ["C901", "PLR0912", "ARG001"] |
| lint.per-file-ignores.**/deepagents/options/model_building.py | ["PLR0911", "PLR0912"] |
| lint.per-file-ignores.**/deepagents/options/graph_builder.py | ["C901", "PLR0912", "PLR0913", "PLR0915"] |
| lint.per-file-ignores.**/deepagents/tools.py | ["ARG001"] |
