# vvaharness/validation/models/persona_report.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/models/persona_report.py.evidence.json`. SHA-256: `b9e44f334d45af2ad42249c8e1e7d6bd043bb94113b11a8afdbb2b30823b87b0`.

```sudo
// Source: vvaharness/validation/models/persona_report.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import NotRequired, TypedDict; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import EvidenceAnchor, GateStatus; preserve alias and import-time effects.
// Source: vvaharness/validation/models/persona_report.py:25-25
In source order: Evaluate once ['HarnessTerminalState', 'PersonaGateEntry', 'PersonaReport']; assign in source target order to __all__.
// Source: vvaharness/validation/models/persona_report.py:28-32
interface HarnessTerminalState {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/persona_report.py:29-32
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then For sdk_persona_reports, declare without assigning a value; source annotation NotRequired[list[dict[str, object]]]. Then For messages, declare without assigning a value; source annotation NotRequired[list[object]].
}
// Source: vvaharness/validation/models/persona_report.py:35-46
interface PersonaGateEntry {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/persona_report.py:36-44
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For gate_name, declare without assigning a value; source annotation str. Then For status, declare without assigning a value; source annotation GateStatus. Then For summary, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/models/persona_report.py:45-46
  In source order: For details, assign ''; source annotation str. Then For evidence, assign Field(default_factory=list); source annotation list[EvidenceAnchor].
}
// Source: vvaharness/validation/models/persona_report.py:49-57
interface PersonaReport {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/persona_report.py:50-57
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For persona, declare without assigning a value; source annotation str. Then For tracking_id, declare without assigning a value; source annotation str. Then For gates, declare without assigning a value; source annotation list[PersonaGateEntry].
}
```

## Local import links

- `from vvaharness.models import EvidenceAnchor, GateStatus` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
