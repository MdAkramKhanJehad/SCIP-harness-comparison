# vvaharness/backends/harness/claude/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/claude/__init__.py.evidence.json`. SHA-256: `e2384b1b9e743bd60c924d0a8cc02b0f6b7ab9349991c14b9658233083dbf41b`.

```sudo
// Source: vvaharness/backends/harness/claude/__init__.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from .client import ClaudeHarness; preserve alias and import-time effects. Then Evaluate once ['ClaudeHarness']; assign in source target order to __all__.
```

## Local import links

- `from .client import ClaudeHarness` at source line 17: `source_detail/vvaharness/backends/harness/claude/client.py.sudo.md`.
