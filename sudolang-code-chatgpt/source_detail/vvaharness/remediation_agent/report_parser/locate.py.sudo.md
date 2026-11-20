# vvaharness/remediation_agent/report_parser/locate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_parser/locate.py.evidence.json`. SHA-256: `6e147740929e69057a33d429f2b26f3a3cd53ccd08a1918dbd9a1045f68b645e`.

```sudo
// Source: vvaharness/remediation_agent/report_parser/locate.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once 'security-scan'; assign in source target order to SCAN_DIR_NAME. Then Evaluate once 'security-remediation'; assign in source target order to REMEDIATION_DIR_NAME.
// Source: vvaharness/remediation_agent/report_parser/locate.py:23-23
In source order: Evaluate once '*_report.md'; assign in source target order to REPORT_GLOB.
// Source: vvaharness/remediation_agent/report_parser/locate.py:26-29
// Source signature: find_scan_dir(repo: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn find_scan_dir(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/locate.py:27-28
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then Evaluate once Path(repo) / SCAN_DIR_NAME; assign in source target order to scan_dir.
  // Source: vvaharness/remediation_agent/report_parser/locate.py:29-29
  End this invocation with scan_dir if scan_dir.is_dir() else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_parser/locate.py:32-38
// Source signature: latest_report(scan_dir: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn latest_report(scan_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_parser/locate.py:33-37
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then Evaluate once sorted(Path(scan_dir).glob(REPORT_GLOB), key=lambda p: (p.name, p.stat().st_mtime)); assign in source target order to reports.
  // Source: vvaharness/remediation_agent/report_parser/locate.py:38-38
  End this invocation with reports[-1] if reports else None.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
