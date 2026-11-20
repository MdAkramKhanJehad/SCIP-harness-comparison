# vvaharness/remediation_agent/render.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/render.py.evidence.json`. SHA-256: `9fbe230a39185c9d464c5de9715de1c254e576ec9831604d3c658ee5a6d9c59f`.

```sudo
// Source: vvaharness/remediation_agent/render.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding, _demote_md_headings, _md_cell, _snippet_fence, _vector_span; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _confidence_label; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cwe import cwe_for, cwe_name; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/render.py:28-28
In source order: Evaluate once ['render_finding_md']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/render.py:31-39
// Source signature: render_finding_md(finding: Finding, index: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_finding_md(finding, index) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:32-38
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then Evaluate once [source_template_34_8, *_metadata_lines(finding), '']; assign in source target order to lines. Then Evaluate lines.extend(_narrative_lines(finding)); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/render.py:39-39
  End this invocation with source_literal_39_11.join(lines).rstrip() + source_literal_39_39.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/render.py:42-48
// Source signature: _cwe_label(finding: Finding) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cwe_label(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:43-44
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then Evaluate once cwe_for(finding.cwe, finding.vuln_class); assign in source target order to cwe.
  // Source: vvaharness/remediation_agent/render.py:45-46
  if (the source predicate not cwe is truthy) {
    // Source: vvaharness/remediation_agent/render.py:46-46
    End this invocation with ('', '').
  }
  // Source: vvaharness/remediation_agent/render.py:47-47
  In source order: Evaluate once cwe_name(cwe); assign in source target order to name.
  // Source: vvaharness/remediation_agent/render.py:48-48
  End this invocation with (cwe, source_template_48_16 if name else cwe).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/render.py:51-58
// Source signature: _cvss_text(finding: Finding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cvss_text(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:52-52
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call.
  // Source: vvaharness/remediation_agent/render.py:53-55
  if (the source predicate finding.cvss_score is not None is truthy) {
    // Source: vvaharness/remediation_agent/render.py:54-55
    End this invocation with source_template_54_16.
  }
  // Source: vvaharness/remediation_agent/render.py:56-57
  if (the source predicate finding.cvss_vector is truthy) {
    // Source: vvaharness/remediation_agent/render.py:57-57
    End this invocation with _vector_span(finding.cvss_vector).
  }
  // Source: vvaharness/remediation_agent/render.py:58-58
  End this invocation with '_not computed_'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/render.py:61-77
// Source signature: _metadata_lines(finding: Finding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _metadata_lines(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:62-64
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call. Then Evaluate once _cwe_label(finding); assign in source target order to (cwe, label). Then Evaluate once [source_template_64_13]; assign in source target order to lines.
  // Source: vvaharness/remediation_agent/render.py:65-68
  if (the source predicate cwe is truthy) {
    // Source: vvaharness/remediation_agent/render.py:66-68
    In source order: Evaluate once cwe.split('-')[-1]; assign in source target order to number. Then Evaluate lines.append(source_template_67_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/render.py:69-70
  In source order: Evaluate lines.append(source_template_69_17); retain side effects and discard the expression result. Then Evaluate lines.append(source_template_70_17); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/render.py:72-73
  if (the source predicate finding.source_ref is truthy) {
    // Source: vvaharness/remediation_agent/render.py:73-73
    In source order: Evaluate lines.append(source_template_73_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/render.py:74-75
  if (the source predicate finding.sink_ref is truthy) {
    // Source: vvaharness/remediation_agent/render.py:75-75
    In source order: Evaluate lines.append(source_template_75_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/render.py:76-76
  In source order: Evaluate lines.extend(_duplicate_lines(finding)); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/render.py:77-77
  End this invocation with lines.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/render.py:80-89
// Source signature: _duplicate_lines(finding: Finding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _duplicate_lines(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/remediation_agent/render.py:82-83
  if (the source predicate not finding.duplicates is truthy) {
    // Source: vvaharness/remediation_agent/render.py:83-83
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/render.py:84-88
  In source order: Evaluate once ', '.join((source_template_85_8 + (source_template_86_11 if d.line_end and d.line_end != d.line_start else '`') for d in finding.duplicates)); assign in source target order to refs.
  // Source: vvaharness/remediation_agent/render.py:89-89
  End this invocation with [source_template_89_12].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/render.py:92-112
// Source signature: _narrative_lines(finding: Finding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _narrative_lines(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:93-94
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call. Then Evaluate once ['#### Description', _demote_md_headings(finding.description), '']; assign in source target order to lines.
  // Source: vvaharness/remediation_agent/render.py:95-98
  for each (heading, text) in (('Impact', finding.impact), ('Exploit scenario', finding.exploit_scenario)) {
    // Source: vvaharness/remediation_agent/render.py:97-98
    if (the source predicate text is truthy) {
      // Source: vvaharness/remediation_agent/render.py:98-98
      In source order: Evaluate lines.extend([source_template_98_26, _demote_md_headings(text), '']); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/render.py:99-102
  if (the source predicate finding.preconditions is truthy) {
    // Source: vvaharness/remediation_agent/render.py:100-102
    In source order: Evaluate lines.append('#### Preconditions'); retain side effects and discard the expression result. Then Evaluate lines.extend((source_template_101_21 for p in finding.preconditions)); retain side effects and discard the expression result. Then Evaluate lines.append(''); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/render.py:103-106
  if (the source predicate finding.code_snippet is truthy) {
    // Source: vvaharness/remediation_agent/render.py:105-106
    In source order: Evaluate once _snippet_fence(finding.code_snippet); assign in source target order to fence. Then Evaluate lines.extend([fence, finding.code_snippet, fence, '']); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/render.py:107-109
  if (the source predicate finding.recommendation is truthy) {
    // Source: vvaharness/remediation_agent/render.py:108-109
    In source order: Evaluate lines.extend(['#### How to fix', _demote_md_headings(finding.recommendation), '']); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/render.py:110-111
  In source order: Evaluate lines.extend(_verification_lines(finding)); retain side effects and discard the expression result. Then Evaluate lines.extend(_exploitability_lines(finding)); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/render.py:112-112
  End this invocation with lines.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/render.py:115-122
// Source signature: _exploitability_lines(finding: Finding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exploitability_lines(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:116-116
  In source order: Retain source documentation literal source_literal_116_4; it is not a model call.
  // Source: vvaharness/remediation_agent/render.py:117-118
  if (the source predicate not finding.exploitability_notes is truthy) {
    // Source: vvaharness/remediation_agent/render.py:118-118
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/render.py:119-122
  End this invocation with [source_template_120_8, ''].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/render.py:125-135
// Source signature: _verification_lines(finding: Finding) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _verification_lines(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/render.py:126-126
  In source order: Retain source documentation literal source_literal_126_4; it is not a model call.
  // Source: vvaharness/remediation_agent/render.py:127-128
  if (the source predicate not finding.verdict is truthy) {
    // Source: vvaharness/remediation_agent/render.py:128-128
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/render.py:129-135
  End this invocation with ['#### Adversarial verification', source_template_131_8, ''].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Finding, _demote_md_headings, _md_cell, _snippet_fence, _vector_span` at source line 18: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.scan._render import _confidence_label` at source line 25: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.report.cwe import cwe_for, cwe_name` at source line 26: `source_detail/vvaharness/report/cwe.py.sudo.md`.
