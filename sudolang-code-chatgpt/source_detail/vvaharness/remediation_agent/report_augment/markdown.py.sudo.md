# vvaharness/remediation_agent/report_augment/markdown.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_augment/markdown.py.evidence.json`. SHA-256: `91db54fb8280a9a860af31826119323c2849f21c52a28567dba0192ed98d1efa`.

```sudo
// Source: vvaharness/remediation_agent/report_augment/markdown.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_augment.dto import CaseRecord, _files_touched, _finding_of, _skipped_record, _summary_of; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/markdown.py:28-37
In source order: Resolve source import from vvaharness.remediation_agent.report_augment.mdsafe import _md_code_span, _md_escape; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_augment.summary import _md_summary_section; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once re.compile('(?m)^### (\\d+)\\. \\[[^\\]]*\\]\\s*(.+?)\\s*$'); assign in source target order to _FINDING_RE.
// Source: vvaharness/remediation_agent/report_augment/markdown.py:39-43
In source order: Evaluate once re.compile('(?s)\\n+### Remediation\\n.*\\Z'); assign in source target order to _EXISTING_REMEDIATION_RE. Then Evaluate once re.compile('(?s)## Remediation Summary\\n.*?(?=\\n#{1,6} |\\Z)'); assign in source target order to _SUMMARY_RE. Then Evaluate once re.compile('(?m)^## '); assign in source target order to _LEVEL2_HEADING_RE.
// Source: vvaharness/remediation_agent/report_augment/markdown.py:46-73
// Source signature: _md_remediation_section(record: CaseRecord) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _md_remediation_section(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:47-50
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then Evaluate once record.bucket; assign in source target order to status. Then Evaluate once _summary_of(record) or record.reason.strip() or 'n/a'; assign in source target order to summary. Then Evaluate once _files_touched(record); assign in source target order to files.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:52-59
  if (the source predicate status == 'remediated' is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:53-54
    In source order: Evaluate once 'Automated fix applied by the Remediation Agent and written as a unified diff; awaiting validation.'; assign in source target order to approach.
  }
  else {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:55-59
    if (the source predicate status == 'deny' is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/markdown.py:56-57
      In source order: Evaluate once 'Policy gate denied automated patching; guidance-only — a human must remediate.'; assign in source target order to approach.
    }
    else {
      // Source: vvaharness/remediation_agent/report_augment/markdown.py:59-59
      In source order: Evaluate once 'No automated patch applied.'; assign in source target order to approach.
    }
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:62-68
  In source order: Evaluate once ['### Remediation', source_template_64_8, source_template_65_8, source_template_66_8, '- **Details of what was remediated:**']; assign in source target order to lines.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:69-72
  if (the source predicate files is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:70-70
    In source order: Apply source augmented assignment lines += [source_template_70_18 for f in files] with source evaluation/in-place semantics.
  }
  else {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:72-72
    In source order: Evaluate lines.append('  - (no files changed)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:73-73
  End this invocation with source_literal_73_11.join(lines) + source_literal_73_30.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/markdown.py:76-79
// Source signature: _case_title(record: CaseRecord) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _case_title(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:77-78
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once _finding_of(record); assign in source target order to finding.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:79-79
  End this invocation with finding.title.strip().lower() if finding is not None else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/markdown.py:82-105
// Source signature: _best_md_match(title: str, records: list[CaseRecord]) -> CaseRecord | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _best_md_match(title, records) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:83-84
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call. Then Evaluate once title.strip().lower(); assign in source target order to norm.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:85-86
  if (the source predicate not norm is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:86-86
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:88-88
  In source order: Evaluate once [r for r in records if _case_title(r) == norm]; assign in source target order to exact.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:89-90
  if (the source predicate len(exact) == 1 is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:90-90
    End this invocation with exact[0].
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:91-94
  if (the source predicate len(exact) > 1 is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:92-93
    In source order: Evaluate log.warning('remediate: %d cases share the exact title %r — refusing to guess; finding rendered as skipped', len(exact), title); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:94-94
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:97-98
  In source order: Evaluate once [r for r in records if _case_title(r) and (_case_title(r) in norm or norm in _case_title(r))]; assign in source target order to fuzzy.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:99-100
  if (the source predicate len(fuzzy) == 1 is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:100-100
    End this invocation with fuzzy[0].
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:101-104
  if (the source predicate len(fuzzy) > 1 is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:102-104
    In source order: Evaluate log.warning('remediate: ambiguous title match for %r (%d candidates) — refusing to guess; finding rendered as skipped', title, len(fuzzy)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:105-105
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/markdown.py:108-130
// Source signature: _augment_md(path: Path, records: list[CaseRecord], *, ordinal_matches: dict[int, CaseRecord] | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment_md(path, records, ordinal_matches) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:110-114
  In source order: Retain source documentation literal source_literal_110_4; it is not a model call. Then Evaluate once path.read_text(encoding='utf-8'); assign in source target order to text. Then Evaluate once _SUMMARY_RE.sub('', text).rstrip() + source_literal_113_48; assign in source target order to text. Then Evaluate once list(_FINDING_RE.finditer(text)); assign in source target order to matches.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:115-116
  if (the source predicate not matches is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:116-116
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:117-118
  In source order: Evaluate once [m.start() for m in matches] + [len(text)]; assign in source target order to bounds. Then Evaluate once [text[:bounds[0]]]; assign in source target order to rebuilt.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:119-128
  for each (i, m) in enumerate(matches) {
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:120-126
    In source order: Evaluate once (bounds[i], bounds[i + 1]); assign in source target order to (start, end). Then Evaluate once _LEVEL2_HEADING_RE.search(text, m.end(), end); assign in source target order to cut. Then Evaluate once cut.start() if cut else end; assign in source target order to seg_end. Then Evaluate once int(m.group(1)); assign in source target order to ordinal. Then Evaluate once (ordinal_matches or {}).get(ordinal) or _best_md_match(m.group(2), records) or _skipped_record(); assign in source target order to record.
    // Source: vvaharness/remediation_agent/report_augment/markdown.py:127-128
    In source order: Evaluate rebuilt.append(_augment_segment(text[start:seg_end], record)); retain side effects and discard the expression result. Then Evaluate rebuilt.append(text[seg_end:end]); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:129-130
  In source order: Evaluate rebuilt.append(source_literal_129_19 + _md_summary_section(records)); retain side effects and discard the expression result. Then Evaluate path.write_text(''.join(rebuilt), encoding='utf-8'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/markdown.py:133-136
// Source signature: _augment_segment(segment: str, record: CaseRecord) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _augment_segment(segment, record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:134-135
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call. Then Evaluate once _EXISTING_REMEDIATION_RE.sub('', segment); assign in source target order to stripped.
  // Source: vvaharness/remediation_agent/report_augment/markdown.py:136-136
  End this invocation with stripped.rstrip() + source_literal_136_31 + _md_remediation_section(record) + source_literal_136_74.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.report_augment.dto import CaseRecord, _files_touched, _finding_of, _skipped_record, _summary_of` at source line 21: `source_detail/vvaharness/remediation_agent/report_augment/dto.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment.mdsafe import _md_code_span, _md_escape` at source line 28: `source_detail/vvaharness/remediation_agent/report_augment/mdsafe.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment.summary import _md_summary_section` at source line 29: `source_detail/vvaharness/remediation_agent/report_augment/summary.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/logs.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/report_augment/markdown.py.sudo.md). Exact strings in the evidence asset support this conversion.
