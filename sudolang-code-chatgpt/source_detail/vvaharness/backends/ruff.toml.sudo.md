# vvaharness/backends/ruff.toml

Role: typing/tooling/package metadata; no scan stage introduced.

Exact source asset: `assets/original/vvaharness/backends/ruff.toml`. SHA-256 `4cd4fb1b1c4c40f14e66b19b99686f3396a5386d1ce5b911d8a7955a40d62bb9`.

```sudo
// Source: vvaharness/backends/ruff.toml:1-33
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| extend | "../validation/ruff.toml" |
| src | ["../.."] |
| lint.extend-select | ["PLC0415", "ERA001"] |
| lint.per-file-ignores.**/__init__.py | ["D104", "F401"] |
| lint.per-file-ignores.**/llm/deepagents.py | ["PLR0913", "ARG001"] |
