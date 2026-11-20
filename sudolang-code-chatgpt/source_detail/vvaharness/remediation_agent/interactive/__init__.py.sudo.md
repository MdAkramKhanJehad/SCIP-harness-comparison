# vvaharness/remediation_agent/interactive/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/interactive/__init__.py.evidence.json`. SHA-256: `b71958e82f1afa4af948c787cb6ef50878eba3ba7118f01af2b839f285650f05`.

```sudo
// Source: vvaharness/remediation_agent/interactive/__init__.py:15-30
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.interactive.keys import DOWN, ENTER, OTHER, QUIT, UP, decode_key; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.interactive.loop import run_interactive; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.interactive.render import parse_selection, render_rows; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/interactive/__init__.py:32-42
In source order: Evaluate once ['DOWN', 'ENTER', 'OTHER', 'QUIT', 'UP', 'decode_key', 'parse_selection', 'render_rows', 'run_interactive']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.interactive.keys import DOWN, ENTER, OTHER, QUIT, UP, decode_key` at source line 18: `source_detail/vvaharness/remediation_agent/interactive/keys.py.sudo.md`.
- `from vvaharness.remediation_agent.interactive.loop import run_interactive` at source line 26: `source_detail/vvaharness/remediation_agent/interactive/loop.py.sudo.md`.
- `from vvaharness.remediation_agent.interactive.render import parse_selection, render_rows` at source line 27: `source_detail/vvaharness/remediation_agent/interactive/render.py.sudo.md`.
