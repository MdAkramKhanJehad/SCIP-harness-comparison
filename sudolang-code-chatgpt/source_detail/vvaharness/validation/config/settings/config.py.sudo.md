# vvaharness/validation/config/settings/config.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/settings/config.py.evidence.json`. SHA-256: `ae75fa8c612fb3dd065e43ab55660182544ff0ec3208ce4cb523806bf5b28152`.

```sudo
// Source: vvaharness/validation/config/settings/config.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.overrides import ValidateOverrides; preserve alias and import-time effects.
// Source: vvaharness/validation/config/settings/config.py:24-38
In source order: Resolve source import from vvaharness.validation.config.settings.agent import AgentConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.settings.env import _EnvScalars; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.settings.ghe import GheConfig; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.settings.paths import PathsConfig, _build_paths; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import DEFAULT_EFFORT, DEFAULT_MAX_BUDGET_USD, DEFAULT_MAX_FINDINGS, DEFAULT_MAX_TURNS, DEFAULT_MODEL, DEFAULT_ORCHESTRATOR_MAX_MODEL_CALLS, DEFAULT_PERSONA_MAX_MODEL_CALLS, DEFAULT_TIMEOUT_S, DEFAULT_VALIDATION_VIA; preserve alias and import-time effects.
// Source: vvaharness/validation/config/settings/config.py:41-52
interface Config {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/config/settings/config.py:42-48
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Evaluate once ConfigDict(extra='forbid'); assign in source target order to model_config. Then For paths, declare without assigning a value; source annotation PathsConfig. Then For agent, assign Field(default_factory=AgentConfig); source annotation AgentConfig. Then For ghe, assign Field(default_factory=GheConfig); source annotation GheConfig.
  // Source: vvaharness/validation/config/settings/config.py:49-52
  In source order: For max_findings, assign DEFAULT_MAX_FINDINGS; source annotation int | None. Then For live, assign False; source annotation bool. Then For verbose, assign False; source annotation bool. Then For dry_run, assign False; source annotation bool.
}
// Source: vvaharness/validation/config/settings/config.py:55-58
// Source signature: _parse_tools(raw: str) -> tuple[str, ...] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_tools(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/config/settings/config.py:56-57
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call. Then Evaluate once tuple((tool.strip() for tool in raw.split(',') if tool.strip())); assign in source target order to tools.
  // Source: vvaharness/validation/config/settings/config.py:58-58
  End this invocation with tools or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/config/settings/config.py:61-97
// Source signature: load_config(project_root: Path | None=None, *, live: bool=False, overrides: ValidateOverrides | None=None) -> Config
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_config(project_root, live, overrides) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/config/settings/config.py:67-95
  In source order: Retain source documentation literal source_literal_67_4; it is not a model call. Then For ov, assign overrides or {}; source annotation ValidateOverrides. Then Evaluate once _EnvScalars(); assign in source target order to env. Then Evaluate once project_root if project_root is not None else Path.cwd(); assign in source target order to root. Then Evaluate once Config(paths=_build_paths(root), agent=AgentConfig(binary=env.binary, model=ov.get('model', DEFAULT_MODEL), max_turns=ov.get('max_turns', DEFAULT_MAX_TURNS), max_budget_usd=ov.get('max_budget_usd', DEFAULT_MAX_BUDGET_USD), effort=ov.get('effort', DEFAULT_EFFORT), timeout=ov.get('timeout', DEFAULT_TIMEOUT_S) or DEFAULT_TIMEOUT_S, max_model_calls=ov.get('max_model_calls', DEFAULT_PERSONA_MAX_MODEL_CALLS), orchestrator_max_model_calls=ov.get('orchestrator_max_model_calls', DEFAULT_ORCHESTRATOR_MAX_MODEL_CALLS), via=ov.get('via', DEFAULT_VALIDATION_VIA), provider=ov.get('provider', None), use_responses_api=ov.get('use_responses_api', None), security_architect_model=ov.get('security_architect_model', None), penetration_tester_model=ov.get('penetration_tester_model', None), cross_repo_analyzer_model=ov.get('cross_repo_analyzer_model', None), validate_tools=_parse_tools(ov.get('validate_tools', '')), cache_markers=ov.get('cache_markers', True)), ghe=GheConfig(token=env.ghe_token, archived_token=env.ghe_archived_token), max_findings=ov.get('max_findings', DEFAULT_MAX_FINDINGS), live=live); assign in source target order to cfg.
  // Source: vvaharness/validation/config/settings/config.py:97-97
  End this invocation with cfg.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.config.overrides import ValidateOverrides` at source line 23: `source_detail/vvaharness/validation/config/overrides.py.sudo.md`.
- `from vvaharness.validation.config.settings.agent import AgentConfig` at source line 24: `source_detail/vvaharness/validation/config/settings/agent.py.sudo.md`.
- `from vvaharness.validation.config.settings.env import _EnvScalars` at source line 25: `source_detail/vvaharness/validation/config/settings/env.py.sudo.md`.
- `from vvaharness.validation.config.settings.ghe import GheConfig` at source line 26: `source_detail/vvaharness/validation/config/settings/ghe.py.sudo.md`.
- `from vvaharness.validation.config.settings.paths import PathsConfig, _build_paths` at source line 27: `source_detail/vvaharness/validation/config/settings/paths.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import DEFAULT_EFFORT, DEFAULT_MAX_BUDGET_USD, DEFAULT_MAX_FINDINGS, DEFAULT_MAX_TURNS, DEFAULT_MODEL, DEFAULT_ORCHESTRATOR_MAX_MODEL_CALLS, DEFAULT_PERSONA_MAX_MODEL_CALLS, DEFAULT_TIMEOUT_S, DEFAULT_VALIDATION_VIA` at source line 28: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
