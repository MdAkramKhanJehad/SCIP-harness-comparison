# vvaharness/pipeline/stages/s9/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s9/__init__.py.evidence.json`. SHA-256: `9acbaadfd03000123239a909a2ceeeb89b264ec7b598ae3a29d475e2f12df132`.

```sudo
// Source: vvaharness/pipeline/stages/s9/__init__.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s9.health import scan_health; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s9.typed_sarif import write_sarif; preserve alias and import-time effects. Then Evaluate once ['scan_health', 'write_sarif']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.pipeline.stages.s9.health import scan_health` at source line 19: `source_detail/vvaharness/pipeline/stages/s9/health.py.sudo.md`.
- `from vvaharness.pipeline.stages.s9.typed_sarif import write_sarif` at source line 20: `source_detail/vvaharness/pipeline/stages/s9/typed_sarif.py.sudo.md`.
