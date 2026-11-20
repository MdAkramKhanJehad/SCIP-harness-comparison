# vvaharness/validation/models/manifest.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/models/manifest.py.evidence.json`. SHA-256: `b94cf5227963511449753e135d8880d2092b8205ee3c2c1775d7ce88dbbd60e1`.

```sudo
// Source: vvaharness/validation/models/manifest.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field; preserve alias and import-time effects.
// Source: vvaharness/validation/models/manifest.py:24-26
In source order: Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Evaluate once ['Manifest']; assign in source target order to __all__.
// Source: vvaharness/validation/models/manifest.py:29-52
interface Manifest {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/models/manifest.py:30-36
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then Evaluate once ConfigDict(extra='ignore'); assign in source target order to model_config. Then For case_id, assign ''; source annotation str. Then For session_id, assign ''; source annotation str. Then For finding, assign None; source annotation Finding | None.
  // Source: vvaharness/validation/models/manifest.py:38-39
  In source order: For affected_files, assign Field(default_factory=list); source annotation list[str]. Then For post_results, assign False; source annotation bool.
  // Source: vvaharness/validation/models/manifest.py:41-43
  // Source signature: to_dict(self) -> dict[str, object]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn to_dict(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/manifest.py:42-42
    In source order: Retain source documentation literal source_literal_42_8; it is not a model call.
    // Source: vvaharness/validation/models/manifest.py:43-43
    End this invocation with self.model_dump(mode='json').
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/models/manifest.py:45-47
  // Source signature: write(self, path: Path) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/manifest.py:46-47
    In source order: Retain source documentation literal source_literal_46_8; it is not a model call. Then Evaluate path.write_text(json.dumps(self.to_dict(), indent=2) + source_literal_47_63, encoding='utf-8'); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/models/manifest.py:50-52
  // Source: vvaharness/validation/models/manifest.py:49-49
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/validation/models/manifest.py:50-52
  // Source signature: from_file(cls, path: Path) -> Manifest
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn from_file(cls, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/models/manifest.py:51-51
    In source order: Retain source documentation literal source_literal_51_8; it is not a model call.
    // Source: vvaharness/validation/models/manifest.py:52-52
    End this invocation with cls.model_validate(json.loads(path.read_text(encoding='utf-8'))).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
```

## Local import links

- `from vvaharness.models import Finding` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
