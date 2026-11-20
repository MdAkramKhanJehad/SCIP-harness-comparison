# vvaharness/remediation_agent/artifacts/writer.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/writer.py.evidence.json`. SHA-256: `2e2366a44dab9adb603a369838094323d027e62c95442e8800563cf84ace5bf0`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/writer.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/writer.py:22-32
In source order: Resolve source import from vvaharness.models import FindingCase, Remediation; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.layout import DIFF_PATCH, EVIDENCE_DIR, FINDING_CASE_JSON, SUMMARY_MD, TRIAGE_JSON; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.report import build_report; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.summary import render_summary; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import RemediationVerdict; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/writer.py:33-61
In source order: Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact, redact_tree; preserve alias and import-time effects. Then Evaluate once ['write_case']; assign in source target order to __all__. Then Evaluate once re.compile('^@@ -\\d+(?:,(?P<old_count>\\d+))? \\+\\d+(?:,(?P<new_count>\\d+))? @@'); assign in source target order to _HUNK_HEADER_RE. Then Evaluate once ('diff --git ', 'index ', '--- ', '+++ ', 'old mode ', 'new mode ', 'new file mode ', 'deleted file mode ', 'similarity index ', 'dissimilarity index ', 'rename from ', 'rename to ', 'copy from ', 'copy to ', 'Binary files ', 'GIT binary patch', 'literal ', 'delta ', '# (synthesized diff '); assign in source target order to _DIFF_STRUCTURE_PREFIXES.
// Source: vvaharness/remediation_agent/artifacts/writer.py:62-81
In source order: Evaluate once re.compile(source_literal_63_4); assign in source target order to _SAFE_CONFIG_READ_RE. Then Evaluate once re.compile(source_literal_71_4); assign in source target order to _SECRET_ASSIGNMENT_PREFIX_RE. Then Evaluate once re.compile('\\s*[)\\]}]*[,;]?\\s*(?:(?:#|//).*)?$'); assign in source target order to _SAFE_CONFIG_SUFFIX_RE. Then Evaluate once re.compile('-{5}(?:BEGIN|END) [A-Z0-9 ]*PRIVATE KEY-{5}'); assign in source target order to _PEM_BOUNDARY_RE. Then Evaluate once re.compile('^(?:Proc-Type|DEK-Info):', re.IGNORECASE); assign in source target order to _PEM_HEADER_RE.
// Source: vvaharness/remediation_agent/artifacts/writer.py:82-96
In source order: Evaluate once re.compile('^\\s*[\\"\'`]?(?P<body>[A-Za-z0-9+/]{2,}={0,2})[\\"\'`]?[;,]?\\s*$'); assign in source target order to _PEM_FRAGMENT_RE. Then Evaluate once re.compile('(?:[\\"\'`]|>\\s*)(?P<body>[A-Za-z0-9+/]{2,}={0,2})(?=(?:\\\\[rn])?(?:[\\"\'`]|<))'); assign in source target order to _PEM_WRAPPED_FRAGMENT_RE. Then Evaluate once re.compile(source_literal_90_4, re.IGNORECASE); assign in source target order to _PEM_SHORT_CONTEXT_RE.
// Source: vvaharness/remediation_agent/artifacts/writer.py:99-120
// Source signature: write_case(out_dir: Path, verdict: RemediationVerdict, remediation: Remediation, *, meta: dict, target: RemediationTarget | None=None, reverted_paths: tuple[str, ...]=()) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn write_case(out_dir, verdict, remediation, meta, target, reverted_paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:103-107
  In source order: Retain source documentation literal source_literal_103_4; it is not a model call. Then Evaluate out_dir.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once out_dir / EVIDENCE_DIR; assign in source target order to evidence_dir. Then Evaluate evidence_dir.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once {**verdict.model_dump(), **meta, 'diff_captured': bool(remediation.diff)}; assign in source target order to payload.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:110-113
  In source order: Evaluate (evidence_dir / TRIAGE_JSON).write_text(json.dumps(redact_tree(payload), indent=2), encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate (evidence_dir / SUMMARY_MD).write_text(redact(render_summary(verdict, meta=meta)), encoding='utf-8'); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:114-116
  if (the source predicate remediation.diff is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:115-116
    In source order: Evaluate (evidence_dir / DIFF_PATCH).write_text(_redact_diff(remediation.diff), encoding='utf-8', newline=''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:118-120
  if (the source predicate target is not None is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:119-120
    In source order: Evaluate once build_report(target, remediation, reverted_paths=reverted_paths); assign in source target order to case. Then Evaluate _write_json(out_dir / FINDING_CASE_JSON, _redacted_case(case)); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:123-128
// Source signature: _redacted_case(case: FindingCase) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redacted_case(case) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:124-125
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call. Then Evaluate once redact_tree(case.model_dump(mode='json')); assign in source target order to payload.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:126-127
  for each (attempt, source) in zip(payload['attempts'], case.attempts, strict=True) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:127-127
    In source order: Evaluate once _redact_diff(source.remediation.diff); assign in source target order to attempt['remediation']['diff'].
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:128-128
  End this invocation with payload.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:131-137
// Source signature: _line_parts(line: str) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _line_parts(line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:132-132
  In source order: Retain source documentation literal source_literal_132_4; it is not a model call.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:133-134
  if (the source predicate line.endswith(source_literal_133_21) is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:134-134
    End this invocation with (line[:-2], source_literal_134_26).
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:135-136
  if (the source predicate line.endswith(('\r', source_literal_135_28)) is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:136-136
    End this invocation with (line[:-1], line[-1:]).
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:137-137
  End this invocation with (line, '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:140-149
// Source signature: _private_key_payloads(body: str) -> list[tuple[int, int, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _private_key_payloads(body) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:141-142
  In source order: For matches, assign []; source annotation list[tuple[int, int, str]]. Then Evaluate once _PEM_FRAGMENT_RE.fullmatch(body); assign in source target order to bare.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:143-144
  if (the source predicate bare is not None is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:144-144
    In source order: Evaluate matches.append((*bare.span('body'), bare.group('body'))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:145-148
  In source order: Evaluate matches.extend(((*match.span('body'), match.group('body')) for match in _PEM_WRAPPED_FRAGMENT_RE.finditer(body))); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:149-149
  End this invocation with list(dict.fromkeys(matches)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:152-156
// Source signature: _short_private_key_fragment(body: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _short_private_key_fragment(body) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:153-156
  End this invocation with any((len(payload) >= 4 and len(payload) % 4 == 0 for _, _, payload in _private_key_payloads(body))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:159-169
// Source signature: _private_key_fragment(body: str, *, continuation: bool) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _private_key_fragment(body, continuation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:160-161
  In source order: Retain source documentation literal source_literal_160_4; it is not a model call. Then Evaluate once _PEM_SHORT_CONTEXT_RE.search(body) is not None; assign in source target order to explicit_context.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:162-163
  if (the source predicate _PEM_HEADER_RE.match(body.strip()) is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:163-163
    End this invocation with True.
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:164-169
  End this invocation with any((payload.startswith(('MII', 'MHc', 'MIG')) or len(payload) >= 24 or ((continuation or explicit_context) and len(payload) % 4 == 0) for _, _, payload in _private_key_payloads(body))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:172-175
// Source signature: _replace_spans(text: str, spans: list[tuple[int, int]]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replace_spans(text, spans) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:173-174
  for each (start, end) in sorted(set(spans), reverse=True) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:174-174
    In source order: Evaluate once text[:start] + '[REDACTED-PRIVATE-KEY]' + text[end:]; assign in source target order to text.
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:175-175
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:178-181
// Source signature: _mask_private_key_body(body: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mask_private_key_body(body) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:179-180
  In source order: Evaluate once [match.span() for match in _PEM_BOUNDARY_RE.finditer(body)]; assign in source target order to spans. Then Evaluate spans.extend(((start, end) for start, end, _ in _private_key_payloads(body))); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:181-181
  End this invocation with _replace_spans(body, spans) if spans else '[REDACTED-PRIVATE-KEY]'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:184-186
// Source signature: _mask_diff_line(line: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mask_diff_line(line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:185-185
  In source order: Evaluate once _line_parts(line); assign in source target order to (content, ending).
  // Source: vvaharness/remediation_agent/artifacts/writer.py:186-186
  End this invocation with content[:1] + _mask_private_key_body(content[1:]) + ending.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:189-212
// Source signature: _redact_diff_text(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_diff_text(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:190-196
  In source order: Retain source documentation literal source_literal_190_4; it is not a model call. Then Evaluate once [match for match in _SAFE_CONFIG_READ_RE.finditer(text) if _SECRET_ASSIGNMENT_PREFIX_RE.search(text[:match.start()]) and _SAFE_CONFIG_SUFFIX_RE.fullmatch(text[match.end():])]; assign in source target order to safe_reads.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:197-198
  if (the source predicate not safe_reads is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:198-198
    End this invocation with redact(text).
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:200-201
  In source order: Evaluate once text; assign in source target order to protected. Then For replacements, assign []; source annotation list[tuple[str, str]].
  // Source: vvaharness/remediation_agent/artifacts/writer.py:202-207
  for each (index, match) in reversed(list(enumerate(safe_reads))) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:203-203
    In source order: Evaluate once source_template_203_17; assign in source target order to marker.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:204-205
    while (the source predicate marker in text is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:205-205
      In source order: Apply source augmented assignment marker += '_' with source evaluation/in-place semantics.
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:206-207
    In source order: Evaluate replacements.append((marker, match.group(0))); retain side effects and discard the expression result. Then Evaluate once protected[:match.start()] + marker + protected[match.end():]; assign in source target order to protected.
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:209-209
  In source order: Evaluate once redact(protected); assign in source target order to masked.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:210-211
  for each (marker, source) in replacements {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:211-211
    In source order: Evaluate once masked.replace(marker, source); assign in source target order to masked.
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:212-212
  End this invocation with masked.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:215-221
// Source signature: _redact_unstructured_diff_text(text: str, *, continuation: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_unstructured_diff_text(text, continuation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:216-220
  if (the source predicate _PEM_BOUNDARY_RE.search(text) is not None or _private_key_fragment(text, continuation=continuation) is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:220-220
    In source order: Evaluate once _mask_private_key_body(text); assign in source target order to text.
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:221-221
  End this invocation with _redact_diff_text(text).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:224-330
// Source signature: _redact_diff(diff: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_diff(diff) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:225-229
  In source order: Retain source documentation literal source_literal_225_4; it is not a model call. Then For redacted, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to old_remaining, new_remaining. Then Evaluate once False; assign in source target order to old_private_key, new_private_key. Then Evaluate once False; assign in source target order to old_fragment, new_fragment.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:230-231
  In source order: For old_pending, assign None; source annotation int | None. Then For new_pending, assign None; source annotation int | None.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:233-328
  for each physical_line in diff.splitlines(keepends=True) {
    // Source: vvaharness/remediation_agent/artifacts/writer.py:234-235
    In source order: Evaluate once _line_parts(physical_line); assign in source target order to (line, ending). Then Evaluate once _HUNK_HEADER_RE.match(line); assign in source target order to header.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:236-247
    if (the source predicate header is not None is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:237-241
      In source order: Evaluate once False; assign in source target order to old_private_key, new_private_key. Then Evaluate once False; assign in source target order to old_fragment, new_fragment. Then Evaluate once None; assign in source target order to old_pending, new_pending. Then Evaluate once int(header.group('old_count') or 1); assign in source target order to old_remaining. Then Evaluate once int(header.group('new_count') or 1); assign in source target order to new_remaining.
      // Source: vvaharness/remediation_agent/artifacts/writer.py:242-246
      In source order: Evaluate redacted.append(line[:header.end()] + _redact_unstructured_diff_text(line[header.end():]) + ending); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/artifacts/writer.py:247-247
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:249-249
    In source order: Evaluate once old_remaining > 0 or new_remaining > 0; assign in source target order to in_hunk.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:250-252
    if (the source predicate line.startswith('\\') is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:251-251
      In source order: Evaluate redacted.append('\\' + _redact_diff_text(line[1:]) + ending); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/artifacts/writer.py:252-252
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:254-254
    In source order: Evaluate once line[:1]; assign in source target order to prefix.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:255-263
    if (the source predicate not in_hunk is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:256-258
      In source order: Evaluate once False; assign in source target order to old_private_key, new_private_key. Then Evaluate once False; assign in source target order to old_fragment, new_fragment. Then Evaluate once None; assign in source target order to old_pending, new_pending.
      // Source: vvaharness/remediation_agent/artifacts/writer.py:259-262
      if (the source predicate line.startswith(_DIFF_STRUCTURE_PREFIXES) is truthy) {
        // Source: vvaharness/remediation_agent/artifacts/writer.py:260-260
        In source order: Evaluate redacted.append(physical_line); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/remediation_agent/artifacts/writer.py:262-262
        In source order: Evaluate redacted.append(_redact_unstructured_diff_text(line) + ending); retain side effects and discard the expression result.
      }
      // Source: vvaharness/remediation_agent/artifacts/writer.py:263-263
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:265-279
    if (the source predicate prefix not in {' ', '+', '-'} is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:266-278
      if (the source predicate line.startswith(_DIFF_STRUCTURE_PREFIXES) is truthy) {
        // Source: vvaharness/remediation_agent/artifacts/writer.py:267-271
        In source order: Evaluate once 0; assign in source target order to old_remaining, new_remaining. Then Evaluate once False; assign in source target order to old_private_key, new_private_key. Then Evaluate once False; assign in source target order to old_fragment, new_fragment. Then Evaluate once None; assign in source target order to old_pending, new_pending. Then Evaluate redacted.append(physical_line); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/remediation_agent/artifacts/writer.py:274-278
        In source order: Evaluate redacted.append(_redact_unstructured_diff_text(line, continuation=old_private_key or new_private_key) + ending); retain side effects and discard the expression result.
      }
      // Source: vvaharness/remediation_agent/artifacts/writer.py:279-279
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:281-285
    In source order: Evaluate once line[1:]; assign in source target order to body. Then Evaluate once prefix in {' ', '-'}; assign in source target order to old_line. Then Evaluate once prefix in {' ', '+'}; assign in source target order to new_line. Then Evaluate once _PEM_BOUNDARY_RE.search(body) is not None; assign in source target order to boundary. Then Evaluate once '-----BEGIN ' in body and 'PRIVATE KEY-----' in body; assign in source target order to begins.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:286-286
    In source order: Evaluate once '-----END ' in body and 'PRIVATE KEY-----' in body; assign in source target order to ends.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:287-295
    if (the source predicate ends is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:288-293
      In source order: Evaluate once {index for index in (old_pending if old_line else None, new_pending if new_line else None) if index is not None}; assign in source target order to pending.
      // Source: vvaharness/remediation_agent/artifacts/writer.py:294-295
      for each index in pending {
        // Source: vvaharness/remediation_agent/artifacts/writer.py:295-295
        In source order: Evaluate once _mask_diff_line(redacted[index]); assign in source target order to redacted[index].
      }
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:297-309
    In source order: Evaluate once _private_key_fragment(body, continuation=old_line and old_fragment or (new_line and new_fragment)); assign in source target order to fragment. Then Evaluate once boundary or fragment or (old_line and old_private_key) or (new_line and new_private_key); assign in source target order to mask. Then Evaluate once _mask_private_key_body(body) if mask else _redact_diff_text(body); assign in source target order to safe_body. Then Evaluate redacted.append(prefix + safe_body + ending); retain side effects and discard the expression result. Then Evaluate once len(redacted) - 1; assign in source target order to output_index.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:310-310
    In source order: Evaluate once _short_private_key_fragment(body); assign in source target order to short_fragment.
    // Source: vvaharness/remediation_agent/artifacts/writer.py:312-317
    if (the source predicate old_line is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:313-315
      In source order: Evaluate once (old_private_key or begins) and (not ends); assign in source target order to old_private_key. Then Evaluate once fragment and (not ends); assign in source target order to old_fragment. Then Evaluate once output_index if short_fragment and (not ends) else None; assign in source target order to old_pending.
      // Source: vvaharness/remediation_agent/artifacts/writer.py:316-317
      if (the source predicate old_remaining > 0 is truthy) {
        // Source: vvaharness/remediation_agent/artifacts/writer.py:317-317
        In source order: Apply source augmented assignment old_remaining -= 1 with source evaluation/in-place semantics.
      }
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:318-323
    if (the source predicate new_line is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:319-321
      In source order: Evaluate once (new_private_key or begins) and (not ends); assign in source target order to new_private_key. Then Evaluate once fragment and (not ends); assign in source target order to new_fragment. Then Evaluate once output_index if short_fragment and (not ends) else None; assign in source target order to new_pending.
      // Source: vvaharness/remediation_agent/artifacts/writer.py:322-323
      if (the source predicate new_remaining > 0 is truthy) {
        // Source: vvaharness/remediation_agent/artifacts/writer.py:323-323
        In source order: Apply source augmented assignment new_remaining -= 1 with source evaluation/in-place semantics.
      }
    }
    // Source: vvaharness/remediation_agent/artifacts/writer.py:325-328
    if (the source predicate old_remaining == 0 and new_remaining == 0 is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/writer.py:326-328
      In source order: Evaluate once False; assign in source target order to old_private_key, new_private_key. Then Evaluate once False; assign in source target order to old_fragment, new_fragment. Then Evaluate once None; assign in source target order to old_pending, new_pending.
    }
  }
  // Source: vvaharness/remediation_agent/artifacts/writer.py:330-330
  End this invocation with ''.join(redacted).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/writer.py:333-337
// Source signature: _write_json(path: Path, payload: dict) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _write_json(path, payload) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/writer.py:334-337
  In source order: Retain source documentation literal source_literal_334_4; it is not a model call. Then Evaluate once path.with_suffix(source_template_335_27); assign in source target order to tmp. Then Evaluate tmp.write_text(json.dumps(payload, indent=2) + source_literal_336_51, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate tmp.replace(path); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FindingCase, Remediation` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.layout import DIFF_PATCH, EVIDENCE_DIR, FINDING_CASE_JSON, SUMMARY_MD, TRIAGE_JSON` at source line 23: `source_detail/vvaharness/remediation_agent/artifacts/layout.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.report import build_report` at source line 30: `source_detail/vvaharness/remediation_agent/artifacts/report.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.summary import render_summary` at source line 31: `source_detail/vvaharness/remediation_agent/artifacts/summary.py.sudo.md`.
- `from vvaharness.remediation_agent.models import RemediationVerdict` at source line 32: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 33: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.report.redact import redact, redact_tree` at source line 34: `source_detail/vvaharness/report/redact.py.sudo.md`.
