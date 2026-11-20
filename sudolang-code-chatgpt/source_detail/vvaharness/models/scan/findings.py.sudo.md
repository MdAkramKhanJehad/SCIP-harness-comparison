# vvaharness/models/scan/findings.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/findings.py.evidence.json`. SHA-256: `9df30c031044873d36355c0194299994a27e105c94a215ef0b550b05c0fba1bc`.

```sudo
// Source: vvaharness/models/scan/findings.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/models/scan/findings.py:21-27
In source order: Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, field_validator, model_validator; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._coerce import text as _coerce_text; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.work import DupLocation; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import Severity, VulnClass; preserve alias and import-time effects.
// Source: vvaharness/models/scan/findings.py:29-29
In source order: Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/findings.py:31-113
interface Finding {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/findings.py:32-37
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then For title, declare without assigning a value; source annotation str. Then For file, declare without assigning a value; source annotation str. Then For line_start, declare without assigning a value; source annotation int. Then For vuln_class, declare without assigning a value; source annotation VulnClass.
  // Source: vvaharness/models/scan/findings.py:39-43
  In source order: For severity, assign Severity.MEDIUM; source annotation Severity. Then For line_end, assign 0; source annotation int. Then For cwe, assign None; source annotation str | None. Then For vuln_class_label, assign ''; source annotation str. Then For chunk_id, assign ''; source annotation str.
  // Source: vvaharness/models/scan/findings.py:45-49
  In source order: For impact, assign ''; source annotation str. Then For description, assign ''; source annotation str. Then For exploit_scenario, assign ''; source annotation str. Then For preconditions, assign []; source annotation list[str]. Then For recommendation, assign ''; source annotation str.
  // Source: vvaharness/models/scan/findings.py:51-56
  In source order: For code_snippet, assign ''; source annotation str. Then For source_ref, assign None; source annotation str | None. Then For sink_ref, assign None; source annotation str | None. Then For duplicates, assign []; source annotation list[DupLocation]. Then For backfilled_refs, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/findings.py:58-65
  In source order: For pre_anchor_line, assign 0; source annotation int. Then For case_id, assign ''; source annotation str. Then For exploitability_notes, assign ''; source annotation str. Then For severity_prose_mismatch, assign ''; source annotation str. Then For channel, assign 'main'; source annotation str.
  // Source: vvaharness/models/scan/findings.py:67-71
  In source order: For control_absence, assign False; source annotation bool. Then For origin, assign ''; source annotation str. Then For is_repeat_clone, assign False; source annotation bool.
  // Source: vvaharness/models/scan/findings.py:75-77
  // Source: vvaharness/models/scan/findings.py:73-74
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('channel', mode='before'), classmethod.
  // Source: vvaharness/models/scan/findings.py:75-77
  // Source signature: _v_channel(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_channel(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/findings.py:76-76
    In source order: Retain source documentation literal source_literal_76_8; it is not a model call.
    // Source: vvaharness/models/scan/findings.py:77-77
    End this invocation with 'posture' if isinstance(v, str) and v.strip().casefold() == 'posture' else 'main'.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/findings.py:79-83
  In source order: For verdict, assign None; source annotation Literal['TRUE_POSITIVE', 'FALSE_POSITIVE'] | None. Then For verdict_confidence, assign None; source annotation int | None. Then For verdict_reason, assign ''; source annotation str. Then For cvss_vector, assign None; source annotation str | None. Then For cvss_score, assign None; source annotation float | None.
  // Source: vvaharness/models/scan/findings.py:84-91
  In source order: For cvss_rating, assign None; source annotation str | None. Then For ev_status, assign None; source annotation str | None. Then For ev_evidence, assign ''; source annotation str. Then For ev_reason_source, assign ''; source annotation str. Then For ev_repro, assign ''; source annotation str.
  // Source: vvaharness/models/scan/findings.py:92-99
  In source order: For ev_method, assign ''; source annotation str. Then For ev_confidence, assign ''; source annotation str. Then For ev_confidence_score, assign None; source annotation int | None. Then For ev_cvss_vector, assign ''; source annotation str. Then For ev_cvss_score, assign None; source annotation float | None.
  // Source: vvaharness/models/scan/findings.py:100-107
  In source order: For ev_cvss_rating, assign None; source annotation str | None. Then For ev_repro_detail, assign Field(default_factory=dict); source annotation dict. Then For vsvs_vector, assign None; source annotation str | None. Then For vsvs_score, assign None; source annotation float | None. Then For vsvs_rating, assign None; source annotation str | None.
  // Source: vvaharness/models/scan/findings.py:108-109
  In source order: For offensive_priority, assign None; source annotation str | None. Then For offensive_reason, assign ''; source annotation str.
  // Source: vvaharness/models/scan/findings.py:111-113
  // Source signature: canonical_key(self, line_bucket: int=10) -> tuple
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn canonical_key(self, line_bucket) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/findings.py:112-112
    In source order: Retain source documentation literal source_literal_112_8; it is not a model call.
    // Source: vvaharness/models/scan/findings.py:113-113
    End this invocation with (self.file, self.line_start // line_bucket, self.vuln_class, self.cwe).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/models/scan/findings.py:121-121
In source order: Evaluate once re.compile('^\\s*((?:(?!->)\\S)+?):(\\d+)(?::\\d+)?(?![\\w/\\\\]|\\.\\w)', re.ASCII); assign in source target order to _FILE_LINE_RX.
// Source: vvaharness/models/scan/findings.py:124-168
interface LinkEvidence {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/findings.py:125-132
  In source order: Retain source documentation literal source_literal_125_4; it is not a model call. Then For from_id, assign Field(default='', description='The FINDING id this link starts at (e.g. f3).'); source annotation str. Then For to_id, assign Field(default='', description='The FINDING id this link leads to (e.g. f7).'); source annotation str. Then For mechanism, assign Field(default='', description=source_literal_129_8); source annotation str. Then For file, assign Field(default='', description='Repo-relative path of the code that shows this link holds.'); source annotation str.
  // Source: vvaharness/models/scan/findings.py:133-134
  In source order: For line, assign Field(default=0, description='Line in that file which shows it. Must be a real line.'); source annotation int.
  // Source: vvaharness/models/scan/findings.py:139-151
  // Source: vvaharness/models/scan/findings.py:137-138
  Before creating this callable, evaluate and retain decorators top-to-bottom: model_validator(mode='before'), classmethod.
  // Source: vvaharness/models/scan/findings.py:139-151
  // Source signature: _unpack_file_line(cls, data: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _unpack_file_line(cls, data) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/findings.py:140-141
    if (the source predicate not isinstance(data, dict) or not isinstance(data.get('file_line'), str) is truthy) {
      // Source: vvaharness/models/scan/findings.py:141-141
      End this invocation with data.
    }
    // Source: vvaharness/models/scan/findings.py:142-143
    In source order: Evaluate once dict(data); assign in source target order to data. Then Evaluate once _FILE_LINE_RX.match(data.pop('file_line')); assign in source target order to m.
    // Source: vvaharness/models/scan/findings.py:144-150
    if (the source predicate m is truthy) {
      // Source: vvaharness/models/scan/findings.py:145-146
      if (the source predicate not data.get('file') is truthy) {
        // Source: vvaharness/models/scan/findings.py:146-146
        In source order: Evaluate once m.group(1); assign in source target order to data['file'].
      }
      // Source: vvaharness/models/scan/findings.py:148-150
      if (the source predicate not cls._coerce_line(data.get('line')) is truthy) {
        // Source: vvaharness/models/scan/findings.py:150-150
        In source order: Evaluate once m.group(2); assign in source target order to data['line'].
      }
    }
    // Source: vvaharness/models/scan/findings.py:151-151
    End this invocation with data.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/findings.py:156-163
  // Source: vvaharness/models/scan/findings.py:154-155
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('line', mode='before'), classmethod.
  // Source: vvaharness/models/scan/findings.py:156-163
  // Source signature: _coerce_line(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_line(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/findings.py:158-161
    Perform the following protected operations {
      // Source: vvaharness/models/scan/findings.py:159-159
      In source order: Evaluate once float(v); assign in source target order to f.
    }
    // Source: vvaharness/models/scan/findings.py:160-161
    On the first matching source exception (TypeError, ValueError), in handler order {
      // Source: vvaharness/models/scan/findings.py:161-161
      End this invocation with 0.
    }
    // Source: vvaharness/models/scan/findings.py:163-163
    End this invocation with max(int(f), 0) if math.isfinite(f) else 0.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/findings.py:167-168
  // Source: vvaharness/models/scan/findings.py:165-166
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('from_id', 'to_id', 'mechanism', 'file', mode='before'), classmethod.
  // Source: vvaharness/models/scan/findings.py:167-168
  // Source signature: _coerce_str(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_str(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/findings.py:168-168
    End this invocation with _coerce_text(v).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/scan/findings.py:171-189
interface Chain {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/findings.py:172-176
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call. Then For title, declare without assigning a value; source annotation str. Then For steps, declare without assigning a value; source annotation list[int]. Then For severity, declare without assigning a value; source annotation Severity. Then For blocked_by_controls, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/findings.py:178-185
  In source order: For preconditions, assign []; source annotation list[str]. Then For link_evidence, assign []; source annotation list[LinkEvidence]. Then For entry_reachability, assign ''; source annotation str. Then For quality_notes, assign []; source annotation list[str]. Then For disclosures, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/findings.py:187-189
  In source order: For severity_decision, assign ''; source annotation str. Then For link_coverage, assign ''; source annotation str. Then For narrative, declare without assigning a value; source annotation str.
}
// Source: vvaharness/models/scan/findings.py:196-196
In source order: Evaluate once '(no chain role found by the chaining pass; severity from the CVSS band)'; assign in source target order to NOT_RANKED_NOTE.
// Source: vvaharness/models/scan/findings.py:199-202
interface RankedFinding {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/findings.py:200-202
  In source order: For finding, declare without assigning a value; source annotation Finding. Then For severity, declare without assigning a value; source annotation Severity. Then For exploitability_notes, declare without assigning a value; source annotation str.
}
// Source: vvaharness/models/scan/findings.py:205-215
interface DroppedFinding {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/findings.py:206-210
  In source order: Retain source documentation literal source_literal_206_4; it is not a model call. Then For file, declare without assigning a value; source annotation str. Then For line, declare without assigning a value; source annotation int. Then For vuln_class, declare without assigning a value; source annotation VulnClass. Then For title, declare without assigning a value; source annotation str.
  // Source: vvaharness/models/scan/findings.py:211-215
  In source order: For chunk_id, declare without assigning a value; source annotation str. Then For reason, declare without assigning a value; source annotation Literal['FALSE_POSITIVE', 'VERIFY_ERROR', 'DUPLICATE', 'UNCONFIRMED', 'EXCLUDED', 'GUARDRAIL_BLOCKED', 'INCONCLUSIVE']. Then For detail, assign ''; source annotation str. Then For canonical_idx, assign None; source annotation int | None.
}
```

## Local import links

- `from vvaharness.models.scan._coerce import text as _coerce_text` at source line 25: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.models.scan.work import DupLocation` at source line 26: `source_detail/vvaharness/models/scan/work.py.sudo.md`.
- `from vvaharness.models.vocab import Severity, VulnClass` at source line 27: `source_detail/vvaharness/models/vocab.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/models/scan/findings.py.sudo.md). Exact strings in the evidence asset support this conversion.
