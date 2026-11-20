# vvaharness/validation/config/settings/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/settings/__init__.py.evidence.json`. SHA-256: `1e487461322b05aeac2b9e44cb449af22266c12c9fd9df4b822a5a2ad84fbd4f`.

```sudo
// Source: vvaharness/validation/config/settings/__init__.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.settings.agent import AgentConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.settings.config import Config, _parse_tools, load_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.settings.ghe import GheConfig; preserve alias and import-time effects.
// Source: vvaharness/validation/config/settings/__init__.py:22-32
In source order: Resolve source import from vvaharness.validation.config.settings.paths import _ASSETS_ROOT, PathsConfig; preserve alias and import-time effects. Then Evaluate once ['_ASSETS_ROOT', 'AgentConfig', 'Config', 'GheConfig', 'PathsConfig', '_parse_tools', 'load_config']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.validation.config.settings.agent import AgentConfig` at source line 19: `source_detail/vvaharness/validation/config/settings/agent.py.sudo.md`.
- `from vvaharness.validation.config.settings.config import Config, _parse_tools, load_config` at source line 20: `source_detail/vvaharness/validation/config/settings/config.py.sudo.md`.
- `from vvaharness.validation.config.settings.ghe import GheConfig` at source line 21: `source_detail/vvaharness/validation/config/settings/ghe.py.sudo.md`.
- `from vvaharness.validation.config.settings.paths import _ASSETS_ROOT, PathsConfig` at source line 22: `source_detail/vvaharness/validation/config/settings/paths.py.sudo.md`.
