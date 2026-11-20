# vvaharness/validation/report/augment.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/report/augment.py.evidence.json`. SHA-256: `8b44eb81035a7c776f969555ad6e928c24d6dfc8c6b36b744cf03de44c7497ac`.

```sudo
// Source: vvaharness/validation/report/augment.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects.
// Source: vvaharness/validation/report/augment.py:21-34
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, cast; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import _MD_INVISIBLE_RX, _MD_LINEBREAK_RX; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s9.typed_sarif import FINGERPRINT_KEY, record_result_block, result_fingerprint, result_identifies; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects.
// Source: vvaharness/validation/report/augment.py:35-45
In source order: Resolve source import from vvaharness.validation.constants.artifacts import REMEDIATION_DIRNAME, SCAN_REPORT_GLOB; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.results import SarifLocation; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.report.models import CombinedReportPaths, SarifResult, SarifValidationBlock, ValidatedFinding; preserve alias and import-time effects.
// Source: vvaharness/validation/report/augment.py:47-49
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/report/augment.py:48-49
  In source order: Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models import ValidationResult; preserve alias and import-time effects.
}
// Source: vvaharness/validation/report/augment.py:51-61
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once re.compile('(?m)^### \\d+\\. \\[[^\\]]*\\]\\s*(.+?)\\s*$'); assign in source target order to _FINDING_RE. Then Evaluate once re.compile('(?s)\\n+### Validation\\n.*\\Z'); assign in source target order to _EXISTING_VALIDATION_RE. Then Evaluate once re.compile('(?m)^## '); assign in source target order to _LEVEL2_HEADING_RE. Then Evaluate once 'validation'; assign in source target order to BLOCK_KEY.
// Source: vvaharness/validation/report/augment.py:62-62
In source order: Evaluate once 'validationAliases'; assign in source target order to ALIAS_BLOCK_KEY.
// Source: vvaharness/validation/report/augment.py:65-75
// Source signature: augment_reports(repo: Path, pairs: list[ValidatedFinding], report_md: Path | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn augment_reports(repo, pairs, report_md) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:68-68
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:69-75
  Perform the following protected operations {
    // Source: vvaharness/validation/report/augment.py:70-70
    In source order: Evaluate _augment(repo, pairs, report_md); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/report/augment.py:71-75
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/validation/report/augment.py:72-75
    In source order: Evaluate log.warning('report augmentation skipped (results not written to combined report): %s: %s', type(exc).__name__, exc); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:78-88
// Source signature: _augment(repo: Path, pairs: list[ValidatedFinding], report_md: Path | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment(repo, pairs, report_md) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:79-80
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call. Then Evaluate once _locate_combined_report(repo, report_md); assign in source target order to located.
  // Source: vvaharness/validation/report/augment.py:81-84
  if (the source predicate located is None is truthy) {
    // Source: vvaharness/validation/report/augment.py:82-83
    In source order: Evaluate log.warning('no combined report under %s/%s — skipping report augmentation', repo, REMEDIATION_DIRNAME); retain side effects and discard the expression result.
    // Source: vvaharness/validation/report/augment.py:84-84
    End this invocation with None.
  }
  // Source: vvaharness/validation/report/augment.py:85-88
  In source order: Evaluate once located; assign in source target order to (sarif_dst, md_dst). Then Evaluate _augment_sarif(sarif_dst, pairs); retain side effects and discard the expression result. Then Evaluate _augment_md(md_dst, pairs); retain side effects and discard the expression result. Then Evaluate log.info('validation results written to combined report under %s', sarif_dst.parent); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:91-104
// Source signature: _locate_combined_report(repo: Path, report_md: Path | None=None) -> CombinedReportPaths | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _locate_combined_report(repo, report_md) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:94-94
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:95-98
  if (the source predicate report_md is not None is truthy) {
    // Source: vvaharness/validation/report/augment.py:96-97
    In source order: Evaluate once repo / REMEDIATION_DIRNAME / Path(report_md).with_suffix('.md').name; assign in source target order to md. Then Evaluate once md.with_suffix('.sarif'); assign in source target order to sarif.
    // Source: vvaharness/validation/report/augment.py:98-98
    End this invocation with CombinedReportPaths(sarif, md) if md.exists() and sarif.exists() else None.
  }
  // Source: vvaharness/validation/report/augment.py:99-99
  In source order: Evaluate once sorted((repo / REMEDIATION_DIRNAME).glob(SCAN_REPORT_GLOB)); assign in source target order to sarifs.
  // Source: vvaharness/validation/report/augment.py:100-101
  if (the source predicate not sarifs is truthy) {
    // Source: vvaharness/validation/report/augment.py:101-101
    End this invocation with None.
  }
  // Source: vvaharness/validation/report/augment.py:102-103
  In source order: Evaluate once sarifs[-1]; assign in source target order to sarif. Then Evaluate once sarif.with_suffix('.md'); assign in source target order to md.
  // Source: vvaharness/validation/report/augment.py:104-104
  End this invocation with CombinedReportPaths(sarif, md) if md.exists() else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:110-120
// Source signature: _status_label(result: ValidationResult, *, session_failed: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _status_label(result, session_failed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:111-111
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:112-113
  if (the source predicate session_failed is truthy) {
    // Source: vvaharness/validation/report/augment.py:113-113
    End this invocation with 'inconclusive'.
  }
  // Source: vvaharness/validation/report/augment.py:114-115
  if (the source predicate result.fixed == 'Yes' is truthy) {
    // Source: vvaharness/validation/report/augment.py:115-115
    End this invocation with 'fixed'.
  }
  // Source: vvaharness/validation/report/augment.py:116-117
  if (the source predicate result.partially_fixed == 'Yes' is truthy) {
    // Source: vvaharness/validation/report/augment.py:117-117
    End this invocation with 'partially_fixed'.
  }
  // Source: vvaharness/validation/report/augment.py:118-119
  if (the source predicate result.not_fixed == 'Yes' is truthy) {
    // Source: vvaharness/validation/report/augment.py:119-119
    End this invocation with 'not_fixed'.
  }
  // Source: vvaharness/validation/report/augment.py:120-120
  End this invocation with 'inconclusive'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:123-127
// Source signature: _status_word(result: ValidationResult, *, session_failed: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _status_word(result, session_failed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:124-124
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:125-127
  End this invocation with {'fixed': 'Fixed', 'partially_fixed': 'Partially Fixed', 'not_fixed': 'Not Fixed', 'inconclusive': 'Inconclusive'}[_status_label(result, session_failed=session_failed)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:130-138
// Source signature: _parse_gates(raw_json: str) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_gates(raw_json) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:131-131
  In source order: Retain source documentation literal source_literal_131_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:132-133
  if (the source predicate not raw_json is truthy) {
    // Source: vvaharness/validation/report/augment.py:133-133
    End this invocation with {}.
  }
  // Source: vvaharness/validation/report/augment.py:134-137
  Perform the following protected operations {
    // Source: vvaharness/validation/report/augment.py:135-135
    In source order: Evaluate once json.loads(raw_json); assign in source target order to parsed.
  }
  // Source: vvaharness/validation/report/augment.py:136-137
  On the first matching source exception (ValueError, TypeError), in handler order {
    // Source: vvaharness/validation/report/augment.py:137-137
    End this invocation with {}.
  }
  // Source: vvaharness/validation/report/augment.py:138-138
  End this invocation with parsed if isinstance(parsed, dict) else {}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:141-153
// Source signature: _validation_block(result: ValidationResult, *, session_failed: bool=False) -> SarifValidationBlock
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validation_block(result, session_failed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:143-144
  In source order: Retain source documentation literal source_literal_143_4; it is not a model call. Then Evaluate once (result.reason_for_decision or result.justification or '').strip(); assign in source target order to reason.
  // Source: vvaharness/validation/report/augment.py:145-146
  if (the source predicate session_failed and (not reason) is truthy) {
    // Source: vvaharness/validation/report/augment.py:146-146
    In source order: Evaluate once 'validation session failed; no verdict was reached'; assign in source target order to reason.
  }
  // Source: vvaharness/validation/report/augment.py:147-153
  End this invocation with {'validationStatus': _status_label(result, session_failed=session_failed), 'validationReason': reason[:2000], 'weightedScore': result.fix_confidence, 'mergeReadiness': result.pr_merge_readiness, 'gateScores': _parse_gates(result.gate_results_json)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:159-161
// Source signature: _norm_path(path_text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _norm_path(path_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:160-160
  In source order: Retain source documentation literal source_literal_160_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:161-161
  End this invocation with path_text.replace('\\', '/').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:164-176
// Source signature: _result_loc(sarif_result: SarifResult) -> SarifLocation | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _result_loc(sarif_result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:165-165
  In source order: Retain source documentation literal source_literal_165_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:166-176
  Perform the following protected operations {
    // Source: vvaharness/validation/report/augment.py:167-171
    In source order: Evaluate once cast(list[object], sarif_result['locations']); assign in source target order to locations. Then Evaluate once cast(SarifResult, locations[0]); assign in source target order to first_location. Then Evaluate once cast(SarifResult, first_location['physicalLocation']); assign in source target order to physical. Then Evaluate once cast(SarifResult, physical['artifactLocation']); assign in source target order to artifact. Then Evaluate once cast(SarifResult, physical['region']); assign in source target order to region.
    // Source: vvaharness/validation/report/augment.py:172-173
    In source order: Evaluate once _norm_path(str(artifact['uri'])); assign in source target order to uri. Then Evaluate once int(cast(int, region['startLine'])); assign in source target order to start_line.
    // Source: vvaharness/validation/report/augment.py:174-174
    End this invocation with SarifLocation(uri, start_line).
  }
  // Source: vvaharness/validation/report/augment.py:175-176
  On the first matching source exception (KeyError, IndexError, TypeError, ValueError), in handler order {
    // Source: vvaharness/validation/report/augment.py:176-176
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:179-185
// Source signature: _match_by_loc(results: list[SarifResult], file: str, line: int) -> SarifResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _match_by_loc(results, file, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:180-181
  In source order: Retain source documentation literal source_literal_180_4; it is not a model call. Then Evaluate once SarifLocation(_norm_path(file), line); assign in source target order to target.
  // Source: vvaharness/validation/report/augment.py:182-184
  for each result in results {
    // Source: vvaharness/validation/report/augment.py:183-184
    if (the source predicate _result_loc(result) == target is truthy) {
      // Source: vvaharness/validation/report/augment.py:184-184
      End this invocation with result.
    }
  }
  // Source: vvaharness/validation/report/augment.py:185-185
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:188-191
// Source signature: _message_text(result: SarifResult) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _message_text(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:189-190
  In source order: Retain source documentation literal source_literal_189_4; it is not a model call. Then Evaluate once cast(SarifResult, result.get('message') or {}); assign in source target order to message.
  // Source: vvaharness/validation/report/augment.py:191-191
  End this invocation with str(message.get('text', '')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:194-197
// Source signature: _match_by_title(results: list[SarifResult], title: str) -> SarifResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _match_by_title(results, title) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:195-196
  In source order: Retain source documentation literal source_literal_195_4; it is not a model call. Then Evaluate once [result for result in results if _message_text(result).startswith(title)]; assign in source target order to hits.
  // Source: vvaharness/validation/report/augment.py:197-197
  End this invocation with hits[0] if len(hits) == 1 else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:200-207
// Source signature: _match_by_fingerprint(results: list[SarifResult], case_id: str) -> SarifResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _match_by_fingerprint(results, case_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:202-203
  if (the source predicate not case_id is truthy) {
    // Source: vvaharness/validation/report/augment.py:203-203
    End this invocation with None.
  }
  // Source: vvaharness/validation/report/augment.py:204-206
  for each result in results {
    // Source: vvaharness/validation/report/augment.py:205-206
    if (the source predicate result_identifies(result, case_id) is truthy) {
      // Source: vvaharness/validation/report/augment.py:206-206
      End this invocation with result.
    }
  }
  // Source: vvaharness/validation/report/augment.py:207-207
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:210-225
// Source signature: _match_sarif(results: list[SarifResult], finding: Finding, case_id: str='') -> SarifResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _match_sarif(results, finding, case_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:212-214
  In source order: Retain source documentation literal source_literal_212_4; it is not a model call. Then Evaluate once _match_by_fingerprint(results, case_id); assign in source target order to hit.
  // Source: vvaharness/validation/report/augment.py:215-216
  if (the source predicate hit is not None is truthy) {
    // Source: vvaharness/validation/report/augment.py:216-216
    End this invocation with hit.
  }
  // Source: vvaharness/validation/report/augment.py:217-221
  In source order: Evaluate once [r for r in results if not case_id or not result_fingerprint(r) or result_identifies(r, case_id)]; assign in source target order to candidates. Then Evaluate once _match_by_loc(candidates, finding.file, finding.line_start) if finding.file else None; assign in source target order to by_loc.
  // Source: vvaharness/validation/report/augment.py:222-223
  if (the source predicate by_loc is not None is truthy) {
    // Source: vvaharness/validation/report/augment.py:223-223
    End this invocation with by_loc.
  }
  // Source: vvaharness/validation/report/augment.py:224-224
  In source order: Evaluate once (finding.title or '').strip(); assign in source target order to title.
  // Source: vvaharness/validation/report/augment.py:225-225
  End this invocation with _match_by_title(candidates, title) if title else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:228-251
// Source signature: _augment_sarif(path: Path, pairs: list[ValidatedFinding]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment_sarif(path, pairs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:229-233
  In source order: Retain source documentation literal source_literal_229_4; it is not a model call. Then Evaluate once json.loads(path.read_text(encoding='utf-8')); assign in source target order to document. Then Evaluate once document.get('runs') or [{}]; assign in source target order to runs. Then Evaluate once runs[0].get('results', []) if runs else []; assign in source target order to results. Then Evaluate once 0; assign in source target order to by_print, matched, aliased.
  // Source: vvaharness/validation/report/augment.py:234-246
  for each (finding, row, session_failed) in pairs {
    // Source: vvaharness/validation/report/augment.py:236-237
    In source order: Evaluate once str(finding.case_id or row.tracking_id or ''); assign in source target order to case_id. Then Evaluate once _match_sarif(results, finding, case_id); assign in source target order to match.
    // Source: vvaharness/validation/report/augment.py:238-239
    if (the source predicate match is None is truthy) {
      // Source: vvaharness/validation/report/augment.py:239-239
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/report/augment.py:240-240
    In source order: Apply source augmented assignment matched += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/validation/report/augment.py:241-242
    if (the source predicate case_id and result_identifies(match, case_id) is truthy) {
      // Source: vvaharness/validation/report/augment.py:242-242
      In source order: Apply source augmented assignment by_print += 1 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/validation/report/augment.py:243-243
    In source order: Evaluate once _validation_block(row, session_failed=session_failed); assign in source target order to block.
    // Source: vvaharness/validation/report/augment.py:244-246
    if (the source predicate not record_result_block(match, case_id, block, key=BLOCK_KEY, alias_key=ALIAS_BLOCK_KEY) is truthy) {
      // Source: vvaharness/validation/report/augment.py:246-246
      In source order: Apply source augmented assignment aliased += 1 with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/validation/report/augment.py:248-251
  In source order: Evaluate console.write(source_template_248_18 + (source_template_250_21 if aliased else '')); retain side effects and discard the expression result. Then Evaluate path.write_text(json.dumps(document, indent=2) + source_literal_251_53, encoding='utf-8'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:258-262
In source order: For _MD_ESCAPE, assign {'\\': '\\\\', '`': '\\`', '*': '\\*', '_': '\\_', '[': '\\[', ']': '\\]', '|': '\\|', '#': '\\#', '<': '&lt;', '>': '&gt;', '&': '&amp;'}; source annotation dict[str, str].
// Source: vvaharness/validation/report/augment.py:265-269
// Source signature: _trim_dangling_escape(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _trim_dangling_escape(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:266-266
  In source order: Retain source documentation literal source_literal_266_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:267-268
  if (the source predicate (len(text) - len(text.rstrip('\\'))) % 2 is truthy) {
    // Source: vvaharness/validation/report/augment.py:268-268
    End this invocation with text[:-1].
  }
  // Source: vvaharness/validation/report/augment.py:269-269
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:272-279
// Source signature: _md_escape(text: object, limit: int=2000) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_escape(text, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:273-273
  In source order: Retain source documentation literal source_literal_273_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:274-275
  if (the source predicate text is None is truthy) {
    // Source: vvaharness/validation/report/augment.py:275-275
    End this invocation with ''.
  }
  // Source: vvaharness/validation/report/augment.py:276-278
  In source order: Evaluate once _MD_LINEBREAK_RX.sub(' ', str(text)); assign in source target order to cleaned. Then Evaluate once _MD_INVISIBLE_RX.sub('', cleaned); assign in source target order to cleaned. Then Evaluate once ''.join((_MD_ESCAPE.get(char, char) for char in cleaned)); assign in source target order to cleaned.
  // Source: vvaharness/validation/report/augment.py:279-279
  End this invocation with _trim_dangling_escape(cleaned[:limit]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:283-283
In source order: Evaluate once 'weighted_score'; assign in source target order to _WEIGHTED_SCORE_KEY.
// Source: vvaharness/validation/report/augment.py:286-288
// Source signature: _md_cell(text: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_cell(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:287-287
  In source order: Retain source documentation literal source_literal_287_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:288-288
  End this invocation with _md_escape(text, limit=200).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:291-303
// Source signature: _gate_rows(gates: Mapping[str, object]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gate_rows(gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:292-293
  In source order: Retain source documentation literal source_literal_292_4; it is not a model call. Then For rows, assign []; source annotation list[str].
  // Source: vvaharness/validation/report/augment.py:294-302
  for each (name, entry) in gates.items() {
    // Source: vvaharness/validation/report/augment.py:295-302
    if (the source predicate isinstance(entry, dict) is truthy) {
      // Source: vvaharness/validation/report/augment.py:296-300
      In source order: Evaluate once entry.get('status', ''); assign in source target order to status. Then Evaluate once entry.get('weight', ''); assign in source target order to weight. Then Evaluate once entry.get(_WEIGHTED_SCORE_KEY, ''); assign in source target order to weighted. Then Evaluate once ' | '.join((_md_cell(field) for field in (name, status, weight, weighted))); assign in source target order to cells. Then Evaluate rows.append(source_template_300_24); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/validation/report/augment.py:302-302
      In source order: Evaluate rows.append(source_template_302_24); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/validation/report/augment.py:303-303
  End this invocation with rows.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:306-324
// Source signature: _md_validation_section(result: ValidationResult, *, session_failed: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_validation_section(result, session_failed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:307-314
  In source order: Retain source documentation literal source_literal_307_4; it is not a model call. Then Evaluate once ['### Validation', source_template_310_8, source_template_311_8]; assign in source target order to lines. Then Evaluate once (result.justification or result.reason_for_decision or '').strip(); assign in source target order to summary.
  // Source: vvaharness/validation/report/augment.py:315-316
  if (the source predicate not summary and session_failed is truthy) {
    // Source: vvaharness/validation/report/augment.py:316-316
    In source order: Evaluate once 'validation session failed; no verdict was reached'; assign in source target order to summary.
  }
  // Source: vvaharness/validation/report/augment.py:317-318
  if (the source predicate summary is truthy) {
    // Source: vvaharness/validation/report/augment.py:318-318
    In source order: Evaluate lines.append(source_template_318_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/report/augment.py:319-320
  In source order: Evaluate once _parse_gates(result.gate_results_json); assign in source target order to gates. Then Evaluate once _gate_rows(gates); assign in source target order to rows.
  // Source: vvaharness/validation/report/augment.py:321-323
  if (the source predicate rows is truthy) {
    // Source: vvaharness/validation/report/augment.py:322-323
    In source order: Apply source augmented assignment lines += ['- **Gate scores:**', '', '  | gate | status | weight | weighted |', '  |---|---|---|---|', *rows] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/validation/report/augment.py:324-324
  End this invocation with source_literal_324_11.join(lines) + source_literal_324_30.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:327-329
// Source signature: _ftitle(pair: ValidatedFinding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ftitle(pair) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:328-328
  In source order: Retain source documentation literal source_literal_328_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:329-329
  End this invocation with (pair.finding.title or pair.row.finding_title or '').strip().lower().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:332-334
// Source signature: _only(pairs: list[ValidatedFinding]) -> ValidatedFinding | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _only(pairs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:333-333
  In source order: Retain source documentation literal source_literal_333_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:334-334
  End this invocation with pairs[0] if len(pairs) == 1 else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:337-348
// Source signature: _best_md_match(title: str, pairs: list[ValidatedFinding]) -> ValidatedFinding | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _best_md_match(title, pairs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:338-339
  In source order: Retain source documentation literal source_literal_338_4; it is not a model call. Then Evaluate once title.strip().lower(); assign in source target order to norm.
  // Source: vvaharness/validation/report/augment.py:340-341
  if (the source predicate not norm is truthy) {
    // Source: vvaharness/validation/report/augment.py:341-341
    End this invocation with None.
  }
  // Source: vvaharness/validation/report/augment.py:342-342
  In source order: Evaluate once [pair for pair in pairs if _ftitle(pair) == norm]; assign in source target order to exact.
  // Source: vvaharness/validation/report/augment.py:343-344
  if (the source predicate exact is truthy) {
    // Source: vvaharness/validation/report/augment.py:344-344
    End this invocation with _only(exact).
  }
  // Source: vvaharness/validation/report/augment.py:345-348
  End this invocation with _only([pair for pair in pairs if (pair_title := _ftitle(pair)) and (pair_title in norm or norm in pair_title)]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:351-366
// Source signature: _augment_md(path: Path, pairs: list[ValidatedFinding]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment_md(path, pairs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:352-354
  In source order: Retain source documentation literal source_literal_352_4; it is not a model call. Then Evaluate once path.read_text(encoding='utf-8'); assign in source target order to text. Then Evaluate once list(_FINDING_RE.finditer(text)); assign in source target order to matches.
  // Source: vvaharness/validation/report/augment.py:355-356
  if (the source predicate not matches is truthy) {
    // Source: vvaharness/validation/report/augment.py:356-356
    End this invocation with None.
  }
  // Source: vvaharness/validation/report/augment.py:357-358
  In source order: Evaluate once [heading_match.start() for heading_match in matches] + [len(text)]; assign in source target order to bounds. Then Evaluate once [text[:bounds[0]]]; assign in source target order to rebuilt.
  // Source: vvaharness/validation/report/augment.py:359-365
  for each (index, heading_match) in enumerate(matches) {
    // Source: vvaharness/validation/report/augment.py:360-364
    In source order: Evaluate once (bounds[index], bounds[index + 1]); assign in source target order to (start, end). Then Evaluate once _LEVEL2_HEADING_RE.search(text, heading_match.end(), end); assign in source target order to cut. Then Evaluate once cut.start() if cut else end; assign in source target order to seg_end. Then Evaluate once _best_md_match(heading_match.group(1), pairs); assign in source target order to pair. Then Evaluate rebuilt.append(_augment_segment(text[start:seg_end], pair)); retain side effects and discard the expression result.
    // Source: vvaharness/validation/report/augment.py:365-365
    In source order: Evaluate rebuilt.append(text[seg_end:end]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/report/augment.py:366-366
  In source order: Evaluate path.write_text(''.join(rebuilt), encoding='utf-8'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/report/augment.py:369-375
// Source signature: _augment_segment(segment: str, pair: ValidatedFinding | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment_segment(segment, pair) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/report/augment.py:370-370
  In source order: Retain source documentation literal source_literal_370_4; it is not a model call.
  // Source: vvaharness/validation/report/augment.py:371-372
  if (the source predicate pair is None is truthy) {
    // Source: vvaharness/validation/report/augment.py:372-372
    End this invocation with segment.
  }
  // Source: vvaharness/validation/report/augment.py:373-374
  In source order: Evaluate once _EXISTING_VALIDATION_RE.sub('', segment); assign in source target order to stripped. Then Evaluate once _md_validation_section(pair.row, session_failed=pair.session_failed); assign in source target order to section.
  // Source: vvaharness/validation/report/augment.py:375-375
  End this invocation with stripped.rstrip() + source_literal_375_31 + section + source_literal_375_50.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import _MD_INVISIBLE_RX, _MD_LINEBREAK_RX` at source line 25: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s9.typed_sarif import FINGERPRINT_KEY, record_result_block, result_fingerprint, result_identifies` at source line 28: `source_detail/vvaharness/pipeline/stages/s9/typed_sarif.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 34: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 34: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 34: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import REMEDIATION_DIRNAME, SCAN_REPORT_GLOB` at source line 35: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.models.results import SarifLocation` at source line 39: `source_detail/vvaharness/validation/models/results.py.sudo.md`.
- `from vvaharness.validation.report.models import CombinedReportPaths, SarifResult, SarifValidationBlock, ValidatedFinding` at source line 40: `source_detail/vvaharness/validation/report/models.py.sudo.md`.
- `from vvaharness.models import Finding` at source line 48: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models import ValidationResult` at source line 49: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/report/augment.py.sudo.md). Exact strings in the evidence asset support this conversion.
