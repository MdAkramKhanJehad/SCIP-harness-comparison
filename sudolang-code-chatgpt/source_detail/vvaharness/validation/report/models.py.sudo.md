# vvaharness/validation/report/models.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/report/models.py.evidence.json`. SHA-256: `41d712238a02eafb69ac510194fb23d4c4de6a23e8889c782e884962f6cc697d`.

```sudo
// Source: vvaharness/validation/report/models.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, NamedTuple, TypedDict; preserve alias and import-time effects.
// Source: vvaharness/validation/report/models.py:22-24
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/report/models.py:23-24
  In source order: Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models import ValidationResult; preserve alias and import-time effects.
}
// Source: vvaharness/validation/report/models.py:26-31
In source order: Evaluate once ['CombinedReportPaths', 'SarifResult', 'SarifValidationBlock', 'ValidatedFinding']; assign in source target order to __all__.
// Source: vvaharness/validation/report/models.py:34-38
interface CombinedReportPaths {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/report/models.py:35-38
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call. Then For sarif, declare without assigning a value; source annotation Path. Then For md, declare without assigning a value; source annotation Path.
}
// Source: vvaharness/validation/report/models.py:41-46
interface ValidatedFinding {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/report/models.py:42-46
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then For finding, declare without assigning a value; source annotation Finding. Then For row, declare without assigning a value; source annotation ValidationResult. Then For session_failed, assign False; source annotation bool.
}
// Source: vvaharness/validation/report/models.py:50-50
In source order: Evaluate once dict[str, object]; assign in source target order to SarifResult.
// Source: vvaharness/validation/report/models.py:53-60
interface SarifValidationBlock {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/report/models.py:54-59
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call. Then For validationStatus, declare without assigning a value; source annotation str. Then For validationReason, declare without assigning a value; source annotation str. Then For weightedScore, declare without assigning a value; source annotation float. Then For mergeReadiness, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/report/models.py:60-60
  In source order: For gateScores, declare without assigning a value; source annotation dict[str, object].
}
```

## Local import links

- `from vvaharness.models import Finding` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models import ValidationResult` at source line 24: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
