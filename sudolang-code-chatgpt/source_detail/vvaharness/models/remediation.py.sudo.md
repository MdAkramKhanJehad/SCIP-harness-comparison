# vvaharness/models/remediation.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/remediation.py.evidence.json`. SHA-256: `88e75228966e9dc5903d9cb42827035845035dd2997e2074fce78938e47e044d`.

```sudo
// Source: vvaharness/models/remediation.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field, model_validator; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.gates import GateAssessment; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.provenance import Provenance; preserve alias and import-time effects.
// Source: vvaharness/models/remediation.py:23-28
In source order: Resolve source import from vvaharness.models.vocab import Disposition, RemediationKind, RemediationOutcome; preserve alias and import-time effects. Then Evaluate once ['FileChange', 'Remediation', 'RemediationEvidence', 'finalize']; assign in source target order to __all__. Then Evaluate once frozenset({'report-only', 'report_only'}); assign in source target order to _REPORT_ONLY.
// Source: vvaharness/models/remediation.py:31-38
interface FileChange {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/remediation.py:32-38
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For file, assign Field(description='repo-relative path that was edited'); source annotation str. Then For summary, assign Field(default='', description='what changed and why'); source annotation str.
}
// Source: vvaharness/models/remediation.py:41-69
interface Remediation {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/remediation.py:42-51
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For kind, assign Field(description='what the engine did'); source annotation RemediationKind. Then For summary, assign Field(description='human-readable account of the attempt'); source annotation str. Then For disposition, assign Field(default=None, description='why nothing was applied; required when kind is no_action'); source annotation Disposition | None.
  // Source: vvaharness/models/remediation.py:53-57
  In source order: For diff, assign Field(default='', description='unified diff, when the engine produced one'); source annotation str. Then For files_touched, assign Field(default=(), description='advisory list of edits'); source annotation tuple[str, ...]. Then For changes, assign Field(default=(), description='per-file rationale'); source annotation tuple[FileChange, ...]. Then For gates, assign Field(default=(), description='evidence gates asserted'); source annotation tuple[GateAssessment, ...]. Then For root_cause, assign Field(default='', description='why the vulnerability existed'); source annotation str.
  // Source: vvaharness/models/remediation.py:58-61
  In source order: For remaining_risks, assign Field(default=(), description='what the fix does not cover'); source annotation tuple[str, ...]. Then For recommendations, assign Field(default=(), description='code-level follow-ups'); source annotation tuple[str, ...]. Then For external_ref, assign Field(default='', description='pull-request URL, for engines that open one'); source annotation str. Then For produced_by, assign Field(default=Provenance(), description='attributable origin'); source annotation Provenance.
  // Source: vvaharness/models/remediation.py:64-69
  // Source: vvaharness/models/remediation.py:63-63
  Before creating this callable, evaluate and retain decorators top-to-bottom: model_validator(mode='after').
  // Source: vvaharness/models/remediation.py:64-69
  // Source signature: _require_disposition_for_no_action(self) -> Remediation
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _require_disposition_for_no_action(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/remediation.py:65-65
    In source order: Retain source documentation literal source_literal_65_8; it is not a model call.
    // Source: vvaharness/models/remediation.py:66-68
    if (the source predicate self.kind is RemediationKind.NO_ACTION and self.disposition is None is truthy) {
      // Source: vvaharness/models/remediation.py:67-67
      In source order: Evaluate once 'kind=no_action requires a disposition explaining why nothing was applied'; assign in source target order to msg.
      // Source: vvaharness/models/remediation.py:68-68
      Raise ValueError(msg).
    }
    // Source: vvaharness/models/remediation.py:69-69
    End this invocation with self.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/remediation.py:72-85
interface RemediationEvidence {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/remediation.py:73-80
  In source order: Retain source documentation literal source_literal_73_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For outcome, assign Field(description='what the engine claims it achieved'); source annotation RemediationOutcome. Then For summary, assign Field(description='human-readable account of the attempt'); source annotation str. Then For root_cause, assign Field(default='', description='why the vulnerability existed'); source annotation str.
  // Source: vvaharness/models/remediation.py:81-85
  In source order: For changes, assign Field(default=(), description='per-file rationale'); source annotation tuple[FileChange, ...]. Then For gates, assign Field(default=(), description='evidence gates asserted'); source annotation tuple[GateAssessment, ...]. Then For remaining_risks, assign Field(default=(), description='what the fix does not cover'); source annotation tuple[str, ...]. Then For recommendations, assign Field(default=(), description='code-level follow-ups'); source annotation tuple[str, ...]. Then For produced_by, assign Field(default=Provenance(), description='attributable origin'); source annotation Provenance.
}
// Source: vvaharness/models/remediation.py:89-102
In source order: For _KIND, assign {RemediationOutcome.FIXED: (RemediationKind.EDITS_APPLIED, RemediationKind.DIFF_PROPOSED, None), RemediationOutcome.PARTIALLY_FIXED: (RemediationKind.EDITS_APPLIED, RemediationKind.DIFF_PROPOSED, None), RemediationOutcome.NOT_FIXED: (RemediationKind.NO_ACTION, RemediationKind.NO_ACTION, Disposition.NOT_APPLICABLE), RemediationOutcome.FALSE_POSITIVE: (RemediationKind.NO_ACTION, RemediationKind.NO_ACTION, Disposition.FALSE_POSITIVE), RemediationOutcome.NEEDS_REVIEW: (RemediationKind.NO_ACTION, RemediationKind.NO_ACTION, Disposition.NOT_APPLICABLE), RemediationOutcome.DENIED: (RemediationKind.NO_ACTION, RemediationKind.NO_ACTION, Disposition.POLICY_DENIED)}; source annotation dict[RemediationOutcome, tuple[RemediationKind, RemediationKind, Disposition | None]].
// Source: vvaharness/models/remediation.py:105-125
// Source signature: finalize(evidence: RemediationEvidence, *, mode: str, diff: str='', files_touched: tuple[str, ...]=()) -> Remediation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn finalize(evidence, mode, diff, files_touched) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/remediation.py:107-109
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call. Then Evaluate once _KIND[evidence.outcome]; assign in source target order to (fix_kind, report_kind, disposition). Then Evaluate once report_kind if mode in _REPORT_ONLY else fix_kind; assign in source target order to kind.
  // Source: vvaharness/models/remediation.py:111-112
  if (the source predicate kind is RemediationKind.EDITS_APPLIED and (not files_touched) and (not diff) is truthy) {
    // Source: vvaharness/models/remediation.py:112-112
    In source order: Evaluate once RemediationKind.ALREADY_RESOLVED; assign in source target order to kind.
  }
  // Source: vvaharness/models/remediation.py:113-125
  End this invocation with Remediation(kind=kind, summary=evidence.summary, disposition=disposition, diff=diff, files_touched=files_touched, changes=evidence.changes, gates=evidence.gates, root_cause=evidence.root_cause, remaining_risks=evidence.remaining_risks, recommendations=evidence.recommendations, produced_by=evidence.produced_by).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.gates import GateAssessment` at source line 21: `source_detail/vvaharness/models/gates.py.sudo.md`.
- `from vvaharness.models.provenance import Provenance` at source line 22: `source_detail/vvaharness/models/provenance.py.sudo.md`.
- `from vvaharness.models.vocab import Disposition, RemediationKind, RemediationOutcome` at source line 23: `source_detail/vvaharness/models/vocab.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/models/remediation.py.sudo.md). Exact strings in the evidence asset support this conversion.
