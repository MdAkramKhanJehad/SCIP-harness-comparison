# vvaharness/validation/config/settings/ghe.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/settings/ghe.py.evidence.json`. SHA-256: `c6230a52a925e6e08624af6f3082ed9673e40ee4ac6eafd468a699bf70626567`.

```sudo
// Source: vvaharness/validation/config/settings/ghe.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict; preserve alias and import-time effects.
// Source: vvaharness/validation/config/settings/ghe.py:22-28
interface GheConfig {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/config/settings/ghe.py:23-28
  In source order: Retain source documentation literal source_literal_23_4; it is not a model call. Then Evaluate once ConfigDict(extra='forbid'); assign in source target order to model_config. Then For token, assign ''; source annotation str. Then For archived_token, assign ''; source annotation str.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
