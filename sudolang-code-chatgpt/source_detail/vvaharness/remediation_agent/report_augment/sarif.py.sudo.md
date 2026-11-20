# vvaharness/remediation_agent/report_augment/sarif.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_augment/sarif.py.evidence.json`. SHA-256: `596771d6d0965e83b296f30f876e2c7f5f057600bdeda73e68d8c27bdea21f62`.

```sudo
// Source: vvaharness/remediation_agent/report_augment/sarif.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s9.typed_sarif import FINGERPRINT_KEY, record_result_block, result_fingerprint, result_identifies; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/sarif.py:27-33
In source order: Resolve source import from vvaharness.remediation_agent.report_augment.dto import CaseRecord, _finding_of, _remediation_block, _skipped_record; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/sarif.py:36-42
// Source signature: _result_loc(sarif_result: dict) -> tuple[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _result_loc(sarif_result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:37-37
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:38-42
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:39-39
    In source order: Evaluate once sarif_result['locations'][0]['physicalLocation']; assign in source target order to pl.
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:40-40
    End this invocation with (pl['artifactLocation']['uri'], int(pl['region']['startLine'])).
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:41-42
  On the first matching source exception (KeyError, IndexError, TypeError, ValueError), in handler order {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:42-42
    End this invocation with ('', -1).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/sarif.py:45-50
// Source signature: _match_by_loc(results: list[dict], file: str, line: int) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _match_by_loc(results, file, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:46-46
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:47-49
  for each r in results {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:48-49
    if (the source predicate _result_loc(r) == (file, line) is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:49-49
      End this invocation with r.
    }
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:50-50
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/sarif.py:53-58
// Source signature: _match_by_title(results: list[dict], title: str) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _match_by_title(results, title) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:54-54
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:55-57
  for each r in results {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:56-57
    if (the source predicate str(r.get('message', {}).get('text', '')).startswith(title) is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:57-57
      End this invocation with r.
    }
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:58-58
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/sarif.py:62-63
In source order: Evaluate once 'remediation'; assign in source target order to BLOCK_KEY. Then Evaluate once 'remediationAliases'; assign in source target order to ALIAS_BLOCK_KEY.
// Source: vvaharness/remediation_agent/report_augment/sarif.py:66-70
// Source signature: _case_id_of(record: CaseRecord) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _case_id_of(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:67-67
  In source order: Evaluate once record.case; assign in source target order to case.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:68-69
  if (the source predicate case is None is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:69-69
    End this invocation with ''.
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:70-70
  End this invocation with str(case.case_id or (case.finding.case_id if case.finding else '') or '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/sarif.py:73-92
// Source signature: _match_sarif(results: list[dict], record: CaseRecord) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _match_sarif(results, record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:74-76
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call. Then Evaluate once _finding_of(record); assign in source target order to finding.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:77-78
  if (the source predicate finding is None is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:78-78
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:79-79
  In source order: Evaluate once _case_id_of(record); assign in source target order to case_id.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:80-83
  if (the source predicate case_id is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:81-83
    for each r in results {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:82-83
      if (the source predicate result_identifies(r, case_id) is truthy) {
        // Source: vvaharness/remediation_agent/report_augment/sarif.py:83-83
        End this invocation with r.
      }
    }
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:84-88
  In source order: Evaluate once [r for r in results if not case_id or not result_fingerprint(r) or result_identifies(r, case_id)]; assign in source target order to candidates. Then Evaluate once _match_by_loc(candidates, finding.file, finding.line_start) if finding.file else None; assign in source target order to by_loc.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:89-90
  if (the source predicate by_loc is not None is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:90-90
    End this invocation with by_loc.
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:91-91
  In source order: Evaluate once finding.title.strip(); assign in source target order to title.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:92-92
  End this invocation with _match_by_title(candidates, title) if title else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/sarif.py:95-137
// Source signature: _augment_sarif(path: Path, records: list[CaseRecord]) -> dict[int, CaseRecord]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment_sarif(path, records) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:96-100
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call. Then Evaluate once json.loads(path.read_text(encoding='utf-8')); assign in source target order to doc. Then Evaluate once doc.get('runs') or [{}]; assign in source target order to runs. Then Evaluate once runs[0].get('results', []) if runs else []; assign in source target order to results. Then For matched_ids, assign set(); source annotation set[int].
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:101-104
  In source order: For ordinal_matches, assign {}; source annotation dict[int, CaseRecord]. Then For ordinal_collisions, assign set(); source annotation set[int]. Then Evaluate once 0; assign in source target order to by_print, aliased.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:105-125
  for each record in records {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:106-106
    In source order: Evaluate once _match_sarif(results, record); assign in source target order to match.
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:107-108
    if (the source predicate match is None is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:108-108
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:109-117
    for each (idx, r) in enumerate(results) {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:110-117
      if (the source predicate r is match is truthy) {
        // Source: vvaharness/remediation_agent/report_augment/sarif.py:111-112
        In source order: Evaluate once idx + 1; assign in source target order to ordinal. Then Evaluate once ordinal_matches.get(ordinal); assign in source target order to prior.
        // Source: vvaharness/remediation_agent/report_augment/sarif.py:113-116
        if (the source predicate prior is not None and prior is not record is truthy) {
          // Source: vvaharness/remediation_agent/report_augment/sarif.py:114-114
          In source order: Evaluate ordinal_collisions.add(ordinal); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/remediation_agent/report_augment/sarif.py:116-116
          In source order: Evaluate once record; assign in source target order to ordinal_matches[ordinal].
        }
        // Source: vvaharness/remediation_agent/report_augment/sarif.py:117-117
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:118-118
    In source order: Evaluate once _case_id_of(record); assign in source target order to case_id.
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:119-120
    if (the source predicate case_id and result_identifies(match, case_id) is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:120-120
      In source order: Apply source augmented assignment by_print += 1 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:121-124
    if (the source predicate not record_result_block(match, case_id, _remediation_block(record), key=BLOCK_KEY, alias_key=ALIAS_BLOCK_KEY) is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:123-123
      In source order: Apply source augmented assignment aliased += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:124-124
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:125-125
    In source order: Evaluate matched_ids.add(id(match)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:126-127
  for each ordinal in ordinal_collisions {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:127-127
    In source order: Evaluate ordinal_matches.pop(ordinal, None); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:128-132
  In source order: Evaluate console.write(source_template_128_18 + (source_template_130_21 if aliased else '')); retain side effects and discard the expression result. Then Evaluate once _remediation_block(_skipped_record()); assign in source target order to skipped.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:133-135
  for each r in results {
    // Source: vvaharness/remediation_agent/report_augment/sarif.py:134-135
    if (the source predicate id(r) not in matched_ids is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/sarif.py:135-135
      In source order: Evaluate once dict(skipped); assign in source target order to r.setdefault('properties', {})[BLOCK_KEY].
    }
  }
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:136-136
  In source order: Evaluate path.write_text(json.dumps(doc, indent=2) + source_literal_136_48, encoding='utf-8'); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/report_augment/sarif.py:137-137
  End this invocation with ordinal_matches.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.pipeline.stages.s9.typed_sarif import FINGERPRINT_KEY, record_result_block, result_fingerprint, result_identifies` at source line 21: `source_detail/vvaharness/pipeline/stages/s9/typed_sarif.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment.dto import CaseRecord, _finding_of, _remediation_block, _skipped_record` at source line 27: `source_detail/vvaharness/remediation_agent/report_augment/dto.py.sudo.md`.
- `from vvaharness.util import console` at source line 33: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 33: `source_detail/vvaharness/util/console.py.sudo.md`.
