# vvaharness/remediation_agent/report_parser/field_sections.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_parser/field_sections.py.evidence.json`. SHA-256: `1be78fbf0370c3afc02b3dde3f0e9dee1ef3bf2858204d5af2db56839fa1e04a`.

```sudo
// Source: vvaharness/remediation_agent/report_parser/field_sections.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once re.compile('^\\*\\*Class:\\*\\*\\s*(.+?)\\s*$'); assign in source target order to _CLASS_RE. Then Evaluate once re.compile('^\\*\\*CWE:\\*\\*\\s*(CWE-\\d+)'); assign in source target order to _CWE_RE.
// Source: vvaharness/remediation_agent/report_parser/field_sections.py:23-31
In source order: Evaluate once re.compile('^\\*\\*CVSS 3\\.1:\\*\\*\\s*\\*\\*([0-9.]+)\\*\\*\\s*\\(([^)]+)\\)\\s*—\\s*`([^`]+)`'); assign in source target order to _CVSS_SCORE_RE. Then Evaluate once re.compile('^\\*\\*CVSS 3\\.1:\\*\\*\\s*`([^`]+)`'); assign in source target order to _CVSS_VECONLY_RE. Then Evaluate once re.compile('^\\*\\*Source:\\*\\*\\s*`?([^`]+?)`?\\s*$'); assign in source target order to _SOURCE_RE. Then Evaluate once re.compile('^\\*\\*Sink:\\*\\*\\s*`?([^`]+?)`?\\s*$'); assign in source target order to _SINK_RE. Then Evaluate once re.compile('^\\*\\*Verdict:\\*\\*\\s*(\\w+)\\s*\\(confidence:\\s*(?:(\\d+)/10|not scored)\\)\\s*—?\\s*(.*)$'); assign in source target order to _VERDICT_RE.
// Source: vvaharness/remediation_agent/report_parser/field_sections.py:33-33
In source order: Evaluate once re.compile('^(.*?):(\\d+)(?:-(\\d+))?$'); assign in source target order to _FILELOC_RE.
// Source: vvaharness/remediation_agent/report_parser/field_sections.py:36-43
// Source signature: _file_loc(ref: str) -> tuple[str, int, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _file_loc(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:37-38
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then Evaluate once _FILELOC_RE.match(ref.strip()); assign in source target order to m.
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:39-40
  if (the source predicate not m is truthy) {
    // Source: vvaharness/remediation_agent/report_parser/field_sections.py:40-40
    End this invocation with (ref.strip(), 0, 0).
  }
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:41-42
  In source order: Evaluate once int(m.group(2)); assign in source target order to start. Then Evaluate once int(m.group(3)) if m.group(3) else start; assign in source target order to end.
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:43-43
  End this invocation with (m.group(1).strip(), start, end).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/field_sections.py:46-60
// Source signature: _sections(body: str) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sections(body) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:47-50
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then For out, assign {}; source annotation dict[str, str]. Then Evaluate once ''; assign in source target order to key. Then For buf, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:51-58
  for each line in body.splitlines() {
    // Source: vvaharness/remediation_agent/report_parser/field_sections.py:52-52
    In source order: Evaluate once re.match('^####\\s+(.+?)\\s*$', line); assign in source target order to m.
    // Source: vvaharness/remediation_agent/report_parser/field_sections.py:53-57
    if (the source predicate m is truthy) {
      // Source: vvaharness/remediation_agent/report_parser/field_sections.py:54-56
      In source order: Evaluate once source_literal_54_23.join(buf).strip(); assign in source target order to out[key]. Then Evaluate once m.group(1).strip().lower(); assign in source target order to key. Then Evaluate once []; assign in source target order to buf.
      // Source: vvaharness/remediation_agent/report_parser/field_sections.py:57-57
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/report_parser/field_sections.py:58-58
    In source order: Evaluate buf.append(line); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:59-59
  In source order: Evaluate once source_literal_59_15.join(buf).strip(); assign in source target order to out[key].
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:60-60
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/field_sections.py:63-66
// Source signature: _first_code_block(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _first_code_block(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:64-65
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Evaluate once re.search('```[^\\n]*\\n(.*?)\\n```', text, re.DOTALL); assign in source target order to m.
  // Source: vvaharness/remediation_agent/report_parser/field_sections.py:66-66
  End this invocation with m.group(1) if m else ''.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
