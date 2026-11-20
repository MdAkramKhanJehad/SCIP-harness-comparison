# vvaharness/remediation_agent/report_augment/dto.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_augment/dto.py.evidence.json`. SHA-256: `08c250c6954014076c9765626a4d9de5a698acebc5800c9f27984f98e6847313`.

```sudo
// Source: vvaharness/remediation_agent/report_augment/dto.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/dto.py:21-34
In source order: Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import CaseState, Disposition, Finding, FindingCase, Remediation; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once ['DENY', 'REMEDIATED', 'SKIPPED', 'CaseRecord']; assign in source target order to __all__. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/report_augment/dto.py:36-42
In source order: Evaluate once 'finding_case.json'; assign in source target order to FINDING_CASE_FILENAME. Then Evaluate once ('evidence', 'triage.json'); assign in source target order to TRIAGE_RELPATH. Then Evaluate once 'remediated'; assign in source target order to REMEDIATED. Then Evaluate once 'deny'; assign in source target order to DENY. Then Evaluate once 'skipped'; assign in source target order to SKIPPED.
// Source: vvaharness/remediation_agent/report_augment/dto.py:45-55
In source order: Evaluate once 'finding not processed for remediation'; assign in source target order to _NOT_PROCESSED_REASON. Then For _STATE_BUCKET, assign {CaseState.REMEDIATED: REMEDIATED, CaseState.VALIDATED: REMEDIATED, CaseState.FAILED: SKIPPED, CaseState.DECLINED: SKIPPED, CaseState.OPEN: SKIPPED, CaseState.PENDING: SKIPPED}; source annotation Final[dict[CaseState, str]].
// Source: vvaharness/remediation_agent/report_augment/dto.py:59-65
// Source: vvaharness/remediation_agent/report_augment/dto.py:58-58
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/report_augment/dto.py:59-65
interface CaseRecord {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:60-65
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then For bucket, declare without assigning a value; source annotation str. Then For reason, declare without assigning a value; source annotation str. Then For case, assign None; source annotation FindingCase | None. Then For false_positive, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/report_augment/dto.py:68-80
// Source signature: _load_cases(rem_dir: Path) -> list[CaseRecord]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_cases(rem_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:69-70
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call. Then For records, assign []; source annotation list[CaseRecord].
  // Source: vvaharness/remediation_agent/report_augment/dto.py:71-79
  for each path in sorted(rem_dir.glob(source_template_71_36)) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:72-72
    In source order: Evaluate once _read_case(path); assign in source target order to case.
    // Source: vvaharness/remediation_agent/report_augment/dto.py:73-74
    if (the source predicate case is None is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/dto.py:74-74
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/report_augment/dto.py:75-79
    In source order: Evaluate once _bucket_and_reason(case, _load_triage(path.parent)); assign in source target order to (bucket, reason). Then Evaluate records.append(CaseRecord(bucket=bucket, reason=reason, case=case, false_positive=_disposition_of(case) is Disposition.FALSE_POSITIVE)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:80-80
  End this invocation with records.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:83-90
// Source signature: _read_case(path: Path) -> FindingCase | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_case(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:84-84
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:85-90
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:86-86
    End this invocation with FindingCase.read(path).
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:87-90
  On the first matching source exception (OSError, ValueError) as e, in handler order {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:88-89
    In source order: Evaluate log.warning("remediate: skipping unreadable case '%s' (%s): %s", path.parent.name, path, e); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/report_augment/dto.py:90-90
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:93-100
// Source signature: _load_triage(finding_dir: Path) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_triage(finding_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:94-95
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call. Then Evaluate once finding_dir.joinpath(*TRIAGE_RELPATH); assign in source target order to triage_path.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:96-99
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:97-97
    In source order: Evaluate once json.loads(triage_path.read_text(encoding='utf-8')); assign in source target order to data.
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:98-99
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:99-99
    End this invocation with {}.
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:100-100
  End this invocation with data if isinstance(data, dict) else {}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:103-114
// Source signature: _bucket_and_reason(case: FindingCase, triage: dict) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bucket_and_reason(case, triage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:104-106
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call. Then Evaluate once _remediation_of(case); assign in source target order to remediation. Then Evaluate once remediation.summary.strip() if remediation is not None else ''; assign in source target order to summary.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:107-110
  if (the source predicate remediation is not None and remediation.disposition is Disposition.POLICY_DENIED is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:108-109
    In source order: Evaluate once triage.get('policy_reason') or summary or 'policy gate denied automated remediation'; assign in source target order to reason.
    // Source: vvaharness/remediation_agent/report_augment/dto.py:110-110
    End this invocation with (DENY, str(reason)).
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:111-111
  In source order: Evaluate once _STATE_BUCKET[case.state]; assign in source target order to bucket.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:112-113
  if (the source predicate bucket == REMEDIATED is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:113-113
    End this invocation with (REMEDIATED, summary or 'remediation applied').
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:114-114
  End this invocation with (SKIPPED, summary or _skipped_reason(case)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:117-125
// Source signature: _skipped_reason(case: FindingCase) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _skipped_reason(case) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:118-118
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:119-120
  if (the source predicate _disposition_of(case) is Disposition.FALSE_POSITIVE is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:120-120
    End this invocation with 'finding rejected as a false positive'.
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:121-122
  if (the source predicate case.state is CaseState.FAILED is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:122-122
    End this invocation with 'fix applied but failed validation; needs rework'.
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:123-124
  if (the source predicate case.state is CaseState.OPEN and case.attempts is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:124-124
    End this invocation with 'fix applied; validation inconclusive, pending re-validation'.
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:125-125
  End this invocation with 'remediation not applied; needs review'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:128-132
// Source signature: _remediation_of(case: FindingCase | None) -> Remediation | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remediation_of(case) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:129-129
  In source order: Retain source documentation literal source_literal_129_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:130-131
  if (the source predicate case is None or not case.attempts is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:131-131
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:132-132
  End this invocation with case.attempts[-1].remediation.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:135-138
// Source signature: _disposition_of(case: FindingCase | None) -> Disposition | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _disposition_of(case) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:136-137
  In source order: Retain source documentation literal source_literal_136_4; it is not a model call. Then Evaluate once _remediation_of(case); assign in source target order to remediation.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:138-138
  End this invocation with remediation.disposition if remediation is not None else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:141-143
// Source signature: _skipped_record() -> CaseRecord
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _skipped_record() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:142-142
  In source order: Retain source documentation literal source_literal_142_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:143-143
  End this invocation with CaseRecord(bucket=SKIPPED, reason=_NOT_PROCESSED_REASON).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:146-148
// Source signature: _finding_of(record: CaseRecord) -> Finding | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _finding_of(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:147-147
  In source order: Retain source documentation literal source_literal_147_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:148-148
  End this invocation with record.case.finding if record.case is not None else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:151-154
// Source signature: _summary_of(record: CaseRecord) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _summary_of(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:152-153
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call. Then Evaluate once _remediation_of(record.case); assign in source target order to remediation.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:154-154
  End this invocation with remediation.summary.strip() if remediation is not None else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:157-168
// Source signature: _files_touched(record: CaseRecord) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _files_touched(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:158-159
  In source order: Retain source documentation literal source_literal_158_4; it is not a model call. Then Evaluate once _remediation_of(record.case); assign in source target order to remediation.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:160-161
  if (the source predicate remediation is None is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:161-161
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:162-163
  In source order: For seen, assign set(); source annotation set[str]. Then For unique, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/report_augment/dto.py:164-167
  for each f in remediation.files_touched {
    // Source: vvaharness/remediation_agent/report_augment/dto.py:165-167
    if (the source predicate f and f not in seen is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/dto.py:166-167
      In source order: Evaluate seen.add(f); retain side effects and discard the expression result. Then Evaluate unique.append(f); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/report_augment/dto.py:168-168
  End this invocation with unique.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/dto.py:171-176
// Source signature: _remediation_block(record: CaseRecord) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remediation_block(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:172-172
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/dto.py:173-176
  End this invocation with {'remediationStatus': record.bucket, 'remediationReason': record.reason[:2000]}.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import CaseState, Disposition, Finding, FindingCase, Remediation` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/logs.py.sudo.md`.
