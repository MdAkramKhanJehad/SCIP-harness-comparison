# vvaharness/validation/config/settings/agent.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/settings/agent.py.evidence.json`. SHA-256: `d76584e9adaba6703c218c3e84e84fd5b8d31c2e67e0b67e44ce34ad228d5df8`.

```sudo
// Source: vvaharness/validation/config/settings/agent.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import DEFAULT_CLAUDE_BINARY, DEFAULT_EFFORT, DEFAULT_MAX_BUDGET_USD, DEFAULT_MAX_TURNS, DEFAULT_MODEL, DEFAULT_ORCHESTRATOR_MAX_MODEL_CALLS, DEFAULT_PERSONA_MAX_MODEL_CALLS, DEFAULT_TIMEOUT_S, DEFAULT_VALIDATION_VIA; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.enums import EffortLevel; preserve alias and import-time effects.
// Source: vvaharness/validation/config/settings/agent.py:35-62
interface AgentConfig {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/config/settings/agent.py:36-42
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then Evaluate once ConfigDict(extra='forbid'); assign in source target order to model_config. Then For binary, assign DEFAULT_CLAUDE_BINARY; source annotation str. Then For model, assign DEFAULT_MODEL; source annotation str. Then For max_turns, assign DEFAULT_MAX_TURNS; source annotation int.
  // Source: vvaharness/validation/config/settings/agent.py:43-50
  In source order: For max_budget_usd, assign DEFAULT_MAX_BUDGET_USD; source annotation float | None. Then For effort, assign DEFAULT_EFFORT; source annotation EffortLevel. Then For timeout, assign DEFAULT_TIMEOUT_S; source annotation int. Then For max_model_calls, assign DEFAULT_PERSONA_MAX_MODEL_CALLS; source annotation int. Then For orchestrator_max_model_calls, assign DEFAULT_ORCHESTRATOR_MAX_MODEL_CALLS; source annotation int.
  // Source: vvaharness/validation/config/settings/agent.py:51-57
  In source order: For via, assign DEFAULT_VALIDATION_VIA; source annotation str. Then For provider, assign None; source annotation str | None. Then For use_responses_api, assign None; source annotation bool | None. Then For security_architect_model, assign None; source annotation str | None. Then For penetration_tester_model, assign None; source annotation str | None.
  // Source: vvaharness/validation/config/settings/agent.py:58-62
  In source order: For cross_repo_analyzer_model, assign None; source annotation str | None. Then For validate_tools, assign None; source annotation tuple[str, ...] | None. Then For cache_markers, assign True; source annotation bool.
}
```

## Local import links

- `from vvaharness.validation.constants.artifacts import DEFAULT_CLAUDE_BINARY, DEFAULT_EFFORT, DEFAULT_MAX_BUDGET_USD, DEFAULT_MAX_TURNS, DEFAULT_MODEL, DEFAULT_ORCHESTRATOR_MAX_MODEL_CALLS, DEFAULT_PERSONA_MAX_MODEL_CALLS, DEFAULT_TIMEOUT_S, DEFAULT_VALIDATION_VIA` at source line 21: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.enums import EffortLevel` at source line 32: `source_detail/vvaharness/validation/enums/__init__.py.sudo.md`.
