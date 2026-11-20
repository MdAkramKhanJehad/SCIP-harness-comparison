# vvaharness/remediation_agent/report_parser/fields.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_parser/fields.py.evidence.json`. SHA-256: `f6b748f4da1ece617b9afb7b6ec4f8e0235fb8649b842ea8d6817bc7e1227905`.

```sudo
// Source: vvaharness/remediation_agent/report_parser/fields.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from typing import Literal, cast, get_args; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding as ScanFinding; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_parser/fields.py:22-39
In source order: Resolve source import from vvaharness.models import Severity, VulnClass; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser.field_sections import _CLASS_RE, _CVSS_SCORE_RE, _CVSS_VECONLY_RE, _CWE_RE, _SINK_RE, _SOURCE_RE, _VERDICT_RE, _file_loc, _first_code_block, _sections; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser.finding import Finding; preserve alias and import-time effects. Then Evaluate once Literal['TRUE_POSITIVE', 'FALSE_POSITIVE']; assign in source target order to _VerdictLabel. Then For _VERDICT_LABELS, assign frozenset(get_args(_VerdictLabel)); source annotation frozenset[str].
// Source: vvaharness/remediation_agent/report_parser/fields.py:42-69
// Source signature: to_scan_finding(finding: Finding) -> ScanFinding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_scan_finding(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:43-45
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then Evaluate once parse_finding_fields(finding); assign in source target order to f. Then Evaluate once VulnClass(f['vuln_class']); assign in source target order to vuln_class.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:46-69
  End this invocation with ScanFinding(title=f['title'], file=f['file'], line_start=f['line_start'], line_end=f['line_end'], vuln_class=vuln_class, vuln_class_label=f['vuln_class'] if vuln_class is VulnClass.OTHER else '', severity=_severity(finding.severity), cwe=f['cwe'], description=f['description'], recommendation=f['recommendation'], code_snippet=f['code_snippet'], impact=f['impact'], exploit_scenario=f['exploit_scenario'], preconditions=f['preconditions'], source_ref=f['source_ref'], sink_ref=f['sink_ref'], verdict=_verdict_label(f['verdict']), verdict_confidence=f['verdict_confidence'], verdict_reason=f['verdict_reason'], cvss_vector=f['cvss_vector'], cvss_score=f['cvss_score'], cvss_rating=f['cvss_rating']).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/fields.py:72-77
// Source signature: _severity(label: str | None) -> Severity
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _severity(label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:73-73
  In source order: Retain source documentation literal source_literal_73_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:74-77
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/report_parser/fields.py:75-75
    End this invocation with Severity(label or 'medium').
  }
  // Source: vvaharness/remediation_agent/report_parser/fields.py:76-77
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/remediation_agent/report_parser/fields.py:77-77
    End this invocation with Severity.MEDIUM.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/fields.py:80-82
// Source signature: _verdict_label(value: str | None) -> _VerdictLabel | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _verdict_label(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:82-82
  End this invocation with cast('_VerdictLabel', value) if value in _VERDICT_LABELS else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/fields.py:85-155
// Source signature: parse_finding_fields(finding: Finding) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_finding_fields(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:86-91
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then Evaluate once finding.body or ''; assign in source target order to body. Then Evaluate once _sections(body); assign in source target order to secs. Then Evaluate once secs.get('', ''); assign in source target order to head. Then Evaluate once ''; assign in source target order to vuln_class.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:92-96
  In source order: Evaluate once None; assign in source target order to cwe. Then Evaluate once finding.file or ''; assign in source target order to file_ref. Then Evaluate once _file_loc(file_ref) if file_ref else ('', 0, 0); assign in source target order to (file_path, line_start, line_end). Then Evaluate once None; assign in source target order to cvss_vector, cvss_rating. Then Evaluate once None; assign in source target order to cvss_score.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:97-99
  In source order: Evaluate once None; assign in source target order to verdict. Then Evaluate once None; assign in source target order to verdict_confidence. Then Evaluate once None; assign in source target order to source_ref, sink_ref.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:101-116
  for each line in head.splitlines() {
    // Source: vvaharness/remediation_agent/report_parser/fields.py:102-102
    In source order: Evaluate once line.strip(); assign in source target order to line.
    // Source: vvaharness/remediation_agent/report_parser/fields.py:103-116
    if (the source predicate (m := _CLASS_RE.match(line)) is truthy) {
      // Source: vvaharness/remediation_agent/report_parser/fields.py:104-104
      In source order: Evaluate once m.group(1).strip(); assign in source target order to vuln_class.
    }
    else {
      // Source: vvaharness/remediation_agent/report_parser/fields.py:105-116
      if (the source predicate (m := _CWE_RE.match(line)) is truthy) {
        // Source: vvaharness/remediation_agent/report_parser/fields.py:106-106
        In source order: Evaluate once m.group(1).strip(); assign in source target order to cwe.
      }
      else {
        // Source: vvaharness/remediation_agent/report_parser/fields.py:107-116
        if (the source predicate (m := _CVSS_SCORE_RE.match(line)) is truthy) {
          // Source: vvaharness/remediation_agent/report_parser/fields.py:108-110
          In source order: Evaluate once float(m.group(1)); assign in source target order to cvss_score. Then Evaluate once m.group(2).strip(); assign in source target order to cvss_rating. Then Evaluate once m.group(3).strip(); assign in source target order to cvss_vector.
        }
        else {
          // Source: vvaharness/remediation_agent/report_parser/fields.py:111-116
          if (the source predicate (m := _CVSS_VECONLY_RE.match(line)) is truthy) {
            // Source: vvaharness/remediation_agent/report_parser/fields.py:112-112
            In source order: Evaluate once m.group(1).strip(); assign in source target order to cvss_vector.
          }
          else {
            // Source: vvaharness/remediation_agent/report_parser/fields.py:113-116
            if (the source predicate (m := _SOURCE_RE.match(line)) is truthy) {
              // Source: vvaharness/remediation_agent/report_parser/fields.py:114-114
              In source order: Evaluate once m.group(1).strip(); assign in source target order to source_ref.
            }
            else {
              // Source: vvaharness/remediation_agent/report_parser/fields.py:115-116
              if (the source predicate (m := _SINK_RE.match(line)) is truthy) {
                // Source: vvaharness/remediation_agent/report_parser/fields.py:116-116
                In source order: Evaluate once m.group(1).strip(); assign in source target order to sink_ref.
              }
            }
          }
        }
      }
    }
  }
  // Source: vvaharness/remediation_agent/report_parser/fields.py:119-122
  if (the source predicate cwe is None and vuln_class is truthy) {
    // Source: vvaharness/remediation_agent/report_parser/fields.py:120-120
    In source order: Evaluate once re.match('(CWE-\\d+)', vuln_class); assign in source target order to cm.
    // Source: vvaharness/remediation_agent/report_parser/fields.py:121-122
    if (the source predicate cm is truthy) {
      // Source: vvaharness/remediation_agent/report_parser/fields.py:122-122
      In source order: Evaluate once cm.group(1); assign in source target order to cwe.
    }
  }
  // Source: vvaharness/remediation_agent/report_parser/fields.py:124-131
  In source order: Evaluate once _verification(secs.get('adversarial verification', '')); assign in source target order to (verdict, verdict_confidence, verdict_reason). Then Evaluate once [re.sub('^[-*]\\s+', '', ln).strip() for ln in secs.get('preconditions', '').splitlines() if ln.strip().startswith(('-', '*'))]; assign in source target order to preconds.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:133-155
  End this invocation with {'_source': 'vvaharness s8 (verbatim Finding fields)', 'title': finding.title, 'vuln_class': vuln_class, 'cwe': cwe, 'file': file_path, 'line_start': line_start, 'line_end': line_end, 'source_ref': source_ref, 'sink_ref': sink_ref, 'description': secs.get('description', ''), 'recommendation': secs.get('how to fix', ''), 'code_snippet': _first_code_block(body), 'impact': secs.get('impact', ''), 'exploit_scenario': secs.get('exploit scenario', ''), 'preconditions': preconds, 'verdict': verdict, 'verdict_confidence': verdict_confidence, 'verdict_reason': verdict_reason, 'cvss_vector': cvss_vector, 'cvss_score': cvss_score, 'cvss_rating': cvss_rating}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/fields.py:158-165
// Source signature: _verification(section: str) -> tuple[str | None, int | None, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _verification(section) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:159-159
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_parser/fields.py:160-164
  for each (i, line) in enumerate(section.splitlines()) {
    // Source: vvaharness/remediation_agent/report_parser/fields.py:161-161
    In source order: Evaluate once _VERDICT_RE.match(line.strip()); assign in source target order to vm.
    // Source: vvaharness/remediation_agent/report_parser/fields.py:162-164
    if (the source predicate vm is truthy) {
      // Source: vvaharness/remediation_agent/report_parser/fields.py:163-163
      In source order: Evaluate once int(vm.group(2)) if vm.group(2) is not None else None; assign in source target order to conf.
      // Source: vvaharness/remediation_agent/report_parser/fields.py:164-164
      End this invocation with (vm.group(1).strip(), conf, vm.group(3).strip()).
    }
  }
  // Source: vvaharness/remediation_agent/report_parser/fields.py:165-165
  End this invocation with (None, None, '').
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Finding as ScanFinding` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models import Severity, VulnClass` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser.field_sections import _CLASS_RE, _CVSS_SCORE_RE, _CVSS_VECONLY_RE, _CWE_RE, _SINK_RE, _SOURCE_RE, _VERDICT_RE, _file_loc, _first_code_block, _sections` at source line 23: `source_detail/vvaharness/remediation_agent/report_parser/field_sections.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser.finding import Finding` at source line 35: `source_detail/vvaharness/remediation_agent/report_parser/finding.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/report_parser/fields.py.sudo.md). Exact strings in the evidence asset support this conversion.
