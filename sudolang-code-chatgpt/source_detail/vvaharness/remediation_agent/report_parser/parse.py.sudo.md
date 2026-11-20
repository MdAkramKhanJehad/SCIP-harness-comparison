# vvaharness/remediation_agent/report_parser/parse.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_parser/parse.py.evidence.json`. SHA-256: `fffe8730a9f8be93d7c38b8c20a0e796600e2d9f8a74ee5242c2205ed328783a`.

```sudo
// Source: vvaharness/remediation_agent/report_parser/parse.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser.fields import to_scan_finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser.finding import Finding; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_parser/parse.py:22-34
In source order: Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Evaluate once '<!-- remediation-agent:done -->'; assign in source target order to DONE_MARKER. Then Evaluate once re.compile('^###\\s+(\\d+)\\.\\s*\\[(CRITICAL|HIGH|MEDIUM|LOW|INFO)\\]\\s*(.+?)\\s*(<!--\\s*remediation-agent:done\\s*-->)?\\s*$', re.IGNORECASE); assign in source target order to _HEADER_RE. Then Evaluate once re.compile('^\\*\\*File:\\*\\*\\s*`([^`]+)`'); assign in source target order to _FILE_RE.
// Source: vvaharness/remediation_agent/report_parser/parse.py:37-43
// Source signature: parse_findings(md_text: str) -> list[RemediationTarget]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_findings(md_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/parse.py:38-38
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_parser/parse.py:39-43
  End this invocation with [RemediationTarget(finding=to_scan_finding(parsed), index=parsed.index, done=parsed.done) for parsed in _parse_blocks(md_text)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/parse.py:46-76
// Source signature: _parse_blocks(md_text: str) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_blocks(md_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/parse.py:47-50
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then For findings, assign []; source annotation list[Finding]. Then For current, assign None; source annotation Finding | None. Then For buf, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/report_parser/parse.py:52-54
  // Source signature: _flush() -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _flush() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/report_parser/parse.py:53-54
    if (the source predicate current is not None is truthy) {
      // Source: vvaharness/remediation_agent/report_parser/parse.py:54-54
      In source order: Evaluate once source_literal_54_27.join(buf).strip(); assign in source target order to current.body.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/report_parser/parse.py:56-74
  for each line in md_text.splitlines() {
    // Source: vvaharness/remediation_agent/report_parser/parse.py:57-57
    In source order: Evaluate once _HEADER_RE.match(line); assign in source target order to m.
    // Source: vvaharness/remediation_agent/report_parser/parse.py:58-68
    if (the source predicate m is truthy) {
      // Source: vvaharness/remediation_agent/report_parser/parse.py:59-67
      In source order: Evaluate _flush(); retain side effects and discard the expression result. Then Evaluate once Finding(index=int(m.group(1)), severity=m.group(2).upper(), title=m.group(3).strip(), done=bool(m.group(4))); assign in source target order to current. Then Evaluate findings.append(current); retain side effects and discard the expression result. Then Evaluate once [line]; assign in source target order to buf.
      // Source: vvaharness/remediation_agent/report_parser/parse.py:68-68
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/report_parser/parse.py:69-74
    if (the source predicate current is not None is truthy) {
      // Source: vvaharness/remediation_agent/report_parser/parse.py:70-70
      In source order: Evaluate buf.append(line); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/report_parser/parse.py:71-74
      if (the source predicate current.file is None is truthy) {
        // Source: vvaharness/remediation_agent/report_parser/parse.py:72-72
        In source order: Evaluate once _FILE_RE.match(line.strip()); assign in source target order to fm.
        // Source: vvaharness/remediation_agent/report_parser/parse.py:73-74
        if (the source predicate fm is truthy) {
          // Source: vvaharness/remediation_agent/report_parser/parse.py:74-74
          In source order: Evaluate once fm.group(1).strip(); assign in source target order to current.file.
        }
      }
    }
  }
  // Source: vvaharness/remediation_agent/report_parser/parse.py:75-75
  In source order: Evaluate _flush(); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/report_parser/parse.py:76-76
  End this invocation with findings.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.report_parser.fields import to_scan_finding` at source line 20: `source_detail/vvaharness/remediation_agent/report_parser/fields.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser.finding import Finding` at source line 21: `source_detail/vvaharness/remediation_agent/report_parser/finding.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 22: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
