# vvaharness/codegraph/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/codegraph/__init__.py.evidence.json`. SHA-256: `f5d934656c66481e74635d406de233c5c2b33b12c2e2bd9b99f9bbd723961a95`.

```sudo
// Source: vvaharness/codegraph/__init__.py:15-24
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.build import build_graph; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.handle import GraphHandle; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.queries import communities_as_modules, primary_language, system_context_notes; preserve alias and import-time effects.
// Source: vvaharness/codegraph/__init__.py:26-32
In source order: Evaluate once ['GraphHandle', 'build_graph', 'communities_as_modules', 'primary_language', 'system_context_notes']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.codegraph.build import build_graph` at source line 18: `source_detail/vvaharness/codegraph/build.py.sudo.md`.
- `from vvaharness.codegraph.handle import GraphHandle` at source line 19: `source_detail/vvaharness/codegraph/handle.py.sudo.md`.
- `from vvaharness.codegraph.queries import communities_as_modules, primary_language, system_context_notes` at source line 20: `source_detail/vvaharness/codegraph/queries.py.sudo.md`.
