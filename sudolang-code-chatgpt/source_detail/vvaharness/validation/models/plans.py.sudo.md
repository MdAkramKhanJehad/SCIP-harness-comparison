# vvaharness/validation/models/plans.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/models/plans.py.evidence.json`. SHA-256: `b071662766d14578b67fa5cffd7f39385c741f0b0cc6377c29ecce1c6d468a25`.

```sudo
// Source: vvaharness/validation/models/plans.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Provenance, ScoringPolicy; preserve alias and import-time effects.
// Source: vvaharness/validation/models/plans.py:23-25
In source order: Resolve source import from vvaharness.validation.models.manifest import Manifest; preserve alias and import-time effects. Then Evaluate once ['FixValidationPlan']; assign in source target order to __all__.
// Source: vvaharness/validation/models/plans.py:29-38
// Source: vvaharness/validation/models/plans.py:28-28
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/models/plans.py:29-38
interface FixValidationPlan {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/plans.py:30-35
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then For case_id, declare without assigning a value; source annotation str. Then For session_id, declare without assigning a value; source annotation str. Then For manifest, declare without assigning a value; source annotation Manifest. Then For workspace_dir, declare without assigning a value; source annotation Path.
  // Source: vvaharness/validation/models/plans.py:36-38
  In source order: For output_dir, declare without assigning a value; source annotation Path. Then For provenance, assign field(default_factory=Provenance); source annotation Provenance. Then For policy, assign None; source annotation ScoringPolicy | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from vvaharness.models import Provenance, ScoringPolicy` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models.manifest import Manifest` at source line 23: `source_detail/vvaharness/validation/models/manifest.py.sudo.md`.
