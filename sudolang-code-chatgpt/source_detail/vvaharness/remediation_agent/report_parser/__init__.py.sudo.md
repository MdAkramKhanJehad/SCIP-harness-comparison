# vvaharness/remediation_agent/report_parser/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_parser/__init__.py.evidence.json`. SHA-256: `a584c60fea614480af337483ef4f820417cebf3f37ad35c390bc18dd3d96cfde`.

```sudo
// Source: vvaharness/remediation_agent/report_parser/__init__.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser.fields import parse_finding_fields, to_scan_finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser.finding import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser.locate import REMEDIATION_DIR_NAME, REPORT_GLOB, SCAN_DIR_NAME, find_scan_dir, latest_report; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_parser/__init__.py:30-46
In source order: Resolve source import from vvaharness.remediation_agent.report_parser.parse import DONE_MARKER, parse_findings; preserve alias and import-time effects. Then Evaluate once ['DONE_MARKER', 'REMEDIATION_DIR_NAME', 'REPORT_GLOB', 'SCAN_DIR_NAME', 'Finding', 'find_scan_dir', 'latest_report', 'parse_finding_fields', 'parse_findings', 'to_scan_finding']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.report_parser.fields import parse_finding_fields, to_scan_finding` at source line 18: `source_detail/vvaharness/remediation_agent/report_parser/fields.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser.finding import Finding` at source line 22: `source_detail/vvaharness/remediation_agent/report_parser/finding.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser.locate import REMEDIATION_DIR_NAME, REPORT_GLOB, SCAN_DIR_NAME, find_scan_dir, latest_report` at source line 23: `source_detail/vvaharness/remediation_agent/report_parser/locate.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser.parse import DONE_MARKER, parse_findings` at source line 30: `source_detail/vvaharness/remediation_agent/report_parser/parse.py.sudo.md`.
