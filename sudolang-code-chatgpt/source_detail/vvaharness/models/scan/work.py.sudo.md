# vvaharness/models/scan/work.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/work.py.evidence.json`. SHA-256: `64250b7cbaad94ef12add9cdf1615dcdc6ce4a67e4c5b41d7f63aaf832652377`.

```sudo
// Source: vvaharness/models/scan/work.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field, field_validator; preserve alias and import-time effects.
// Source: vvaharness/models/scan/work.py:23-28
In source order: Resolve source import from vvaharness.models.scan._coerce import _coerce_enum, _coerce_int, _coerce_str_list; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.surface import EntryPoint, Sink; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.threat import ThreatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import VulnClass; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/work.py:30-33
interface UnitSize {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/work.py:31-33
  In source order: Evaluate once 'small'; assign in source target order to SMALL. Then Evaluate once 'medium'; assign in source target order to MEDIUM. Then Evaluate once 'large'; assign in source target order to LARGE.
}
// Source: vvaharness/models/scan/work.py:36-43
In source order: Evaluate once {'small', 'medium', 'large'}; assign in source target order to _UNIT_SIZES. Then Evaluate once {'xs': 'small', 'tiny': 'small', 's': 'small', 'm': 'medium', 'med': 'medium', 'moderate': 'medium', 'normal': 'medium', 'default': 'medium', 'l': 'large', 'xl': 'large', 'xxl': 'large', 'big': 'large', 'huge': 'large', 'x_large': 'large'}; assign in source target order to _UNIT_SIZE_ALIAS.
// Source: vvaharness/models/scan/work.py:46-48
// Source signature: threat_unit_id(threat_id: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn threat_unit_id(threat_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/work.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/models/scan/work.py:48-48
  End this invocation with source_template_48_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/work.py:51-88
interface InvestigationUnit {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/work.py:52-57
  In source order: Evaluate once ConfigDict(populate_by_name=True); assign in source target order to model_config. Then For id, declare without assigning a value; source annotation str. Then For threat, declare without assigning a value; source annotation str. Then For surface, declare without assigning a value; source annotation str. Then For actor, declare without assigning a value; source annotation str.
  // Source: vvaharness/models/scan/work.py:58-62
  In source order: For asset, declare without assigning a value; source annotation str. Then For impact, declare without assigning a value; source annotation str. Then For likelihood, declare without assigning a value; source annotation str. Then For controls, assign ''; source annotation str. Then For evidence, assign ''; source annotation str.
  // Source: vvaharness/models/scan/work.py:63-67
  In source order: For files, assign Field(default=[], alias='file_ids'); source annotation list[str]. Then For sinks, assign []; source annotation list[Sink]. Then For entry_points, assign []; source annotation list[EntryPoint]. Then For related_cves, assign []; source annotation list[str]. Then For cwes, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/work.py:68-72
  In source order: For communities, assign []; source annotation list[str]. Then For risk_rank, assign 999; source annotation int. Then For size, assign UnitSize.MEDIUM; source annotation UnitSize. Then For languages, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/work.py:76-77
  // Source: vvaharness/models/scan/work.py:74-75
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('size', mode='before'), classmethod.
  // Source: vvaharness/models/scan/work.py:76-77
  // Source signature: _v_size(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_size(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/work.py:77-77
    End this invocation with _coerce_enum(v, _UNIT_SIZES, _UNIT_SIZE_ALIAS, 'medium').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/work.py:81-82
  // Source: vvaharness/models/scan/work.py:79-80
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('risk_rank', mode='before'), classmethod.
  // Source: vvaharness/models/scan/work.py:81-82
  // Source signature: _v_rank(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_rank(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/work.py:82-82
    End this invocation with _coerce_int(v, 999).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/work.py:87-88
  // Source: vvaharness/models/scan/work.py:84-86
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('files', 'related_cves', 'cwes', 'communities', 'languages', mode='before'), classmethod.
  // Source: vvaharness/models/scan/work.py:87-88
  // Source signature: _v_str_list(cls, v, info)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_str_list(cls, v, info) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/work.py:88-88
    End this invocation with _coerce_str_list(v, source_template_88_35).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/scan/work.py:91-118
interface TaskManifest {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/work.py:92-96
  In source order: For units, declare without assigning a value; source annotation list[InvestigationUnit]. Then For unreachable_files, assign []; source annotation list[str]. Then For threats_without_unit, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/work.py:100-101
  // Source: vvaharness/models/scan/work.py:98-99
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('unreachable_files', mode='before'), classmethod.
  // Source: vvaharness/models/scan/work.py:100-101
  // Source signature: _v_unreachable_files(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_unreachable_files(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/work.py:101-101
    End this invocation with _coerce_str_list(v, 'TaskManifest.unreachable_files').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/work.py:105-106
  // Source: vvaharness/models/scan/work.py:103-104
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('threats_without_unit', mode='before'), classmethod.
  // Source: vvaharness/models/scan/work.py:105-106
  // Source signature: _v_threats_without_unit(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_threats_without_unit(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/work.py:106-106
    End this invocation with _coerce_str_list(v, 'TaskManifest.threats_without_unit').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/work.py:108-109
  // Source signature: sorted_units(self) -> list[InvestigationUnit]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn sorted_units(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/work.py:109-109
    End this invocation with sorted(self.units, key=lambda u: u.risk_rank).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/work.py:111-118
  // Source signature: threats_without_unit_for(self, tm: ThreatModel | None) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn threats_without_unit_for(self, tm) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/work.py:112-112
    In source order: Retain source documentation literal source_literal_112_8; it is not a model call.
    // Source: vvaharness/models/scan/work.py:115-116
    if (the source predicate tm is None is truthy) {
      // Source: vvaharness/models/scan/work.py:116-116
      End this invocation with list(self.threats_without_unit).
    }
    // Source: vvaharness/models/scan/work.py:117-117
    In source order: Evaluate once {u.id for u in self.units}; assign in source target order to minted.
    // Source: vvaharness/models/scan/work.py:118-118
    End this invocation with [tid for tid in tm.threat_ids() if threat_unit_id(tid) not in minted].
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/models/scan/work.py:121-131
interface DupLocation {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/work.py:122-126
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call. Then For file, declare without assigning a value; source annotation str. Then For line_start, declare without assigning a value; source annotation int. Then For line_end, assign 0; source annotation int. Then For vuln_class, declare without assigning a value; source annotation VulnClass.
  // Source: vvaharness/models/scan/work.py:127-131
  In source order: For title, assign ''; source annotation str. Then For chunk_id, assign ''; source annotation str. Then For source_ref, assign None; source annotation str | None. Then For sink_ref, assign None; source annotation str | None. Then For reasoning, assign ''; source annotation str.
}
```

## Local import links

- `from vvaharness.models.scan._coerce import _coerce_enum, _coerce_int, _coerce_str_list` at source line 23: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.models.scan.surface import EntryPoint, Sink` at source line 24: `source_detail/vvaharness/models/scan/surface.py.sudo.md`.
- `from vvaharness.models.scan.threat import ThreatModel` at source line 25: `source_detail/vvaharness/models/scan/threat.py.sudo.md`.
- `from vvaharness.models.vocab import VulnClass` at source line 26: `source_detail/vvaharness/models/vocab.py.sudo.md`.
