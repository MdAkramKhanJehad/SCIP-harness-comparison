# vvaharness/validation/subagents/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/subagents/__init__.py.evidence.json`. SHA-256: `954f97d9974186f47ef0e84e9631313d4bce4e076e2d5315a308b3eb428d9794`.

```sudo
// Source: vvaharness/validation/subagents/__init__.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from vvaharness.validation.subagents._loader import load_agents; preserve alias and import-time effects. Then Evaluate once ['load_agents']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.validation.subagents._loader import load_agents` at source line 17: `source_detail/vvaharness/validation/subagents/_loader.py.sudo.md`.
