# vvaharness/validation/config/settings/paths.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/settings/paths.py.evidence.json`. SHA-256: `1021187deb7135d486455dc0bb9461d2db698c9e350e96a6c4ed00374cddb051`.

```sudo
// Source: vvaharness/validation/config/settings/paths.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import OUTPUTS_DIRNAME, PROMPTS_DIRNAME, TARGETS_DIRNAME; preserve alias and import-time effects.
// Source: vvaharness/validation/config/settings/paths.py:29-29
In source order: Evaluate once Path(__file__).resolve().parent.parent.parent; assign in source target order to _ASSETS_ROOT.
// Source: vvaharness/validation/config/settings/paths.py:32-40
interface PathsConfig {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/config/settings/paths.py:33-39
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then Evaluate once ConfigDict(extra='forbid'); assign in source target order to model_config. Then For project_root, declare without assigning a value; source annotation Path. Then For targets_dir, declare without assigning a value; source annotation Path. Then For outputs_dir, declare without assigning a value; source annotation Path.
  // Source: vvaharness/validation/config/settings/paths.py:40-40
  In source order: For prompts_dir, declare without assigning a value; source annotation Path.
}
// Source: vvaharness/validation/config/settings/paths.py:43-50
// Source signature: _build_paths(project_root: Path) -> PathsConfig
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_paths(project_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/config/settings/paths.py:44-44
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call.
  // Source: vvaharness/validation/config/settings/paths.py:45-50
  End this invocation with PathsConfig(project_root=project_root, targets_dir=project_root / TARGETS_DIRNAME, outputs_dir=project_root / OUTPUTS_DIRNAME, prompts_dir=_ASSETS_ROOT / PROMPTS_DIRNAME).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.constants.artifacts import OUTPUTS_DIRNAME, PROMPTS_DIRNAME, TARGETS_DIRNAME` at source line 23: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
