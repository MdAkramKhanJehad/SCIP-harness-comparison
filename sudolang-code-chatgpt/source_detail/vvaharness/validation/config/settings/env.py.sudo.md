# vvaharness/validation/config/settings/env.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/settings/env.py.evidence.json`. SHA-256: `0c16689bde428f77f96048ca18b088edf1fb874765720346980bb751602e9031`.

```sudo
// Source: vvaharness/validation/config/settings/env.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import Field; preserve alias and import-time effects. Then Resolve source import from pydantic_settings import BaseSettings, SettingsConfigDict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import DEFAULT_CLAUDE_BINARY, ENV_CLAUDE_BINARY, ENV_GHE_ARCHIVED_TOKEN, ENV_GHE_TOKEN; preserve alias and import-time effects.
// Source: vvaharness/validation/config/settings/env.py:30-41
interface _EnvScalars {
  Describe the source Python type, preserving its base/metaclass expression order: BaseSettings.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/config/settings/env.py:31-41
  In source order: Retain source documentation literal source_literal_31_4; it is not a model call. Then Evaluate once SettingsConfigDict(extra='ignore', populate_by_name=True); assign in source target order to model_config. Then For binary, assign Field(default=DEFAULT_CLAUDE_BINARY, alias=ENV_CLAUDE_BINARY); source annotation str. Then For ghe_token, assign Field(default='', alias=ENV_GHE_TOKEN); source annotation str. Then For ghe_archived_token, assign Field(default='', alias=ENV_GHE_ARCHIVED_TOKEN); source annotation str.
}
```

## Local import links

- `from vvaharness.validation.constants.artifacts import DEFAULT_CLAUDE_BINARY, ENV_CLAUDE_BINARY, ENV_GHE_ARCHIVED_TOKEN, ENV_GHE_TOKEN` at source line 22: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
