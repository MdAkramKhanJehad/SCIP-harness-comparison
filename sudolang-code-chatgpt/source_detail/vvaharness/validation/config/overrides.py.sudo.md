# vvaharness/validation/config/overrides.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/config/overrides.py.evidence.json`. SHA-256: `ee15e04b6b10e63ebda49116c763006f583a7e9c8805d24eec809b11d1db1d50`.

```sudo
// Source: vvaharness/validation/config/overrides.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TypedDict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.enums import EffortLevel; preserve alias and import-time effects. Then Evaluate once ['ValidateOverrides']; assign in source target order to __all__.
// Source: vvaharness/validation/config/overrides.py:26-49
interface ValidateOverrides {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/config/overrides.py:27-37
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then For model, declare without assigning a value; source annotation str. Then For via, declare without assigning a value; source annotation str. Then For provider, declare without assigning a value; source annotation str | None. Then For use_responses_api, declare without assigning a value; source annotation bool | None.
  // Source: vvaharness/validation/config/overrides.py:38-42
  In source order: For effort, declare without assigning a value; source annotation EffortLevel. Then For max_turns, declare without assigning a value; source annotation int. Then For max_budget_usd, declare without assigning a value; source annotation float | None. Then For max_findings, declare without assigning a value; source annotation int | None. Then For timeout, declare without assigning a value; source annotation int.
  // Source: vvaharness/validation/config/overrides.py:43-47
  In source order: For max_model_calls, declare without assigning a value; source annotation int. Then For orchestrator_max_model_calls, declare without assigning a value; source annotation int. Then For security_architect_model, declare without assigning a value; source annotation str. Then For penetration_tester_model, declare without assigning a value; source annotation str. Then For cross_repo_analyzer_model, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/config/overrides.py:48-49
  In source order: For validate_tools, declare without assigning a value; source annotation str. Then For cache_markers, declare without assigning a value; source annotation bool.
}
```

## Local import links

- `from vvaharness.validation.enums import EffortLevel` at source line 21: `source_detail/vvaharness/validation/enums/__init__.py.sudo.md`.
