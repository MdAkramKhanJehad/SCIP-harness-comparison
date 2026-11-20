# vvaharness/remediation_agent/models/verdict.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/models/verdict.py.evidence.json`. SHA-256: `b98963aeee2043a13f8f7ce6475d85d7c27279e1bef636371e6062e69d86c3ac`.

```sudo
// Source: vvaharness/remediation_agent/models/verdict.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from typing import Final, Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/models/verdict.py:23-37
In source order: Resolve source import from vvaharness.models import FileChange, GateAssessment, GateStatus, Provenance, RemediationEvidence, RemediationOutcome; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models.change import Change; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models.gates import Gates; preserve alias and import-time effects. Then Evaluate once ['RemediationVerdict', 'Verdict', 'to_evidence']; assign in source target order to __all__. Then Evaluate once Literal['Fixed', 'Partially Fixed', 'Not Fixed', 'False Positive', 'Needs Review', 'Denied']; assign in source target order to Verdict.
// Source: vvaharness/remediation_agent/models/verdict.py:40-95
interface RemediationVerdict {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/models/verdict.py:41-51
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then For finding_index, assign 0; source annotation int. Then For verdict, assign 'Needs Review'; source annotation Verdict. Then For gates, assign Field(default_factory=Gates); source annotation Gates. Then For root_cause, assign Field(default='', description='one paragraph, cites file:line'); source annotation str.
  // Source: vvaharness/remediation_agent/models/verdict.py:52-59
  In source order: For changes, assign Field(default_factory=list, description='edits applied (fix mode) or proposed (report-only)'); source annotation list[Change]. Then For remaining_risks, assign Field(default_factory=list); source annotation list[str]. Then For recommendations, assign Field(default_factory=list, description='code-level follow-ups only — no operational controls'); source annotation list[str]. Then For summary, assign Field(default='', description='2-4 sentence human-readable summary'); source annotation str.
  // Source: vvaharness/remediation_agent/models/verdict.py:62-64
  // Source: vvaharness/remediation_agent/models/verdict.py:61-61
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/remediation_agent/models/verdict.py:62-64
  // Source signature: schema_json_compact(cls) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn schema_json_compact(cls) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/models/verdict.py:63-63
    In source order: Retain source documentation literal source_literal_63_8; it is not a model call.
    // Source: vvaharness/remediation_agent/models/verdict.py:64-64
    End this invocation with json.dumps(cls.model_json_schema(), separators=(',', ':')).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/models/verdict.py:67-95
  // Source: vvaharness/remediation_agent/models/verdict.py:66-66
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/remediation_agent/models/verdict.py:67-95
  // Source signature: coerce(cls, data, *, finding_index: int) -> RemediationVerdict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn coerce(cls, data, finding_index) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/models/verdict.py:68-68
    In source order: Retain source documentation literal source_literal_68_8; it is not a model call.
    // Source: vvaharness/remediation_agent/models/verdict.py:69-71
    if (the source predicate not isinstance(data, dict) is truthy) {
      // Source: vvaharness/remediation_agent/models/verdict.py:70-71
      End this invocation with cls(finding_index=finding_index, verdict='Needs Review', summary='agent response was not a JSON object').
    }
    // Source: vvaharness/remediation_agent/models/verdict.py:72-77
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/models/verdict.py:73-74
      In source order: Evaluate once cls.model_validate(data); assign in source target order to v. Then Evaluate once finding_index; assign in source target order to v.finding_index.
      // Source: vvaharness/remediation_agent/models/verdict.py:75-75
      End this invocation with v.
    }
    // Source: vvaharness/remediation_agent/models/verdict.py:76-77
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/remediation_agent/models/verdict.py:77-77
      In source order: Perform no operation at this source statement.
    }
    // Source: vvaharness/remediation_agent/models/verdict.py:79-80
    In source order: Evaluate once {k: data[k] for k in cls.model_fields if k in data}; assign in source target order to clean. Then Evaluate once set(Verdict.__args__); assign in source target order to valid_verdicts.
    // Source: vvaharness/remediation_agent/models/verdict.py:81-82
    if (the source predicate clean.get('verdict') not in valid_verdicts is truthy) {
      // Source: vvaharness/remediation_agent/models/verdict.py:82-82
      In source order: Evaluate once 'Needs Review'; assign in source target order to clean['verdict'].
    }
    // Source: vvaharness/remediation_agent/models/verdict.py:83-93
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/models/verdict.py:84-84
      In source order: Evaluate once cls.model_validate(clean); assign in source target order to v.
    }
    // Source: vvaharness/remediation_agent/models/verdict.py:85-93
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/remediation_agent/models/verdict.py:86-88
      In source order: Evaluate once cls(verdict='Needs Review', summary='agent verdict could not be fully validated; salvaged available fields'); assign in source target order to v.
      // Source: vvaharness/remediation_agent/models/verdict.py:89-93
      for each (k, val) in clean.items() {
        // Source: vvaharness/remediation_agent/models/verdict.py:90-93
        Perform the following protected operations {
          // Source: vvaharness/remediation_agent/models/verdict.py:91-91
          In source order: Evaluate setattr(v, k, val); retain side effects and discard the expression result.
        }
        // Source: vvaharness/remediation_agent/models/verdict.py:92-93
        On the first matching source exception Exception, in handler order {
          // Source: vvaharness/remediation_agent/models/verdict.py:93-93
          In source order: Perform no operation at this source statement.
        }
      }
    }
    // Source: vvaharness/remediation_agent/models/verdict.py:94-94
    In source order: Evaluate once finding_index; assign in source target order to v.finding_index.
    // Source: vvaharness/remediation_agent/models/verdict.py:95-95
    End this invocation with v.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/remediation_agent/models/verdict.py:99-109
In source order: For _OUTCOMES, assign {'Fixed': RemediationOutcome.FIXED, 'Partially Fixed': RemediationOutcome.PARTIALLY_FIXED, 'Not Fixed': RemediationOutcome.NOT_FIXED, 'False Positive': RemediationOutcome.FALSE_POSITIVE, 'Needs Review': RemediationOutcome.NEEDS_REVIEW, 'Denied': RemediationOutcome.DENIED}; source annotation Final[dict[str, RemediationOutcome]]. Then For _GATE_FIELDS, assign ('source', 'sink', 'missing_control'); source annotation Final[tuple[str, ...]].
// Source: vvaharness/remediation_agent/models/verdict.py:112-117
// Source signature: _gate_assessments(gates: Gates) -> tuple[GateAssessment, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gate_assessments(gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/models/verdict.py:113-113
  In source order: Retain source documentation literal source_literal_113_4; it is not a model call.
  // Source: vvaharness/remediation_agent/models/verdict.py:114-117
  End this invocation with tuple((GateAssessment(name=name, status=GateStatus(getattr(gates, name))) for name in _GATE_FIELDS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/models/verdict.py:120-133
// Source signature: to_evidence(verdict: RemediationVerdict, *, provenance: Provenance) -> RemediationEvidence
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_evidence(verdict, provenance) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/models/verdict.py:122-122
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call.
  // Source: vvaharness/remediation_agent/models/verdict.py:123-133
  End this invocation with RemediationEvidence(outcome=_OUTCOMES[verdict.verdict], summary=verdict.summary, root_cause=verdict.root_cause, changes=tuple((FileChange(file=c.file, summary=c.summary) for c in verdict.changes if c.file)), gates=_gate_assessments(verdict.gates), remaining_risks=tuple(verdict.remaining_risks), recommendations=tuple(verdict.recommendations), produced_by=provenance).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FileChange, GateAssessment, GateStatus, Provenance, RemediationEvidence, RemediationOutcome` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.models.change import Change` at source line 31: `source_detail/vvaharness/remediation_agent/models/change.py.sudo.md`.
- `from vvaharness.remediation_agent.models.gates import Gates` at source line 32: `source_detail/vvaharness/remediation_agent/models/gates.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/models/verdict.py.sudo.md). Exact strings in the evidence asset support this conversion.
