# vvaharness/remediation_agent/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/__init__.py.evidence.json`. SHA-256: `ea32896ac946d69167d88a6ddf8237fd18a7f4b9b55b43d2ff8cf26bc4e82e75`.

```sudo
// Source: vvaharness/remediation_agent/__init__.py:15-31
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.discovery import Layout, cvss_score_of, load_findings, locate_report, prepare_layout; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.interactive import decode_key, parse_selection, render_rows, run_interactive; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import RemediationVerdict; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/__init__.py:32-52
In source order: Resolve source import from vvaharness.remediation_agent.options import VALID_MODES, RemediateOptions, parse_options; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.plugin_runner import apply_plugin; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.remediate import remediate; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.report_parser import DONE_MARKER, REMEDIATION_DIR_NAME, SCAN_DIR_NAME, Finding, find_scan_dir, latest_report, parse_findings; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.runner import model_banner, process_targets, remediate_one; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/__init__.py:53-60
In source order: Resolve source import from vvaharness.remediation_agent.select import band_score, cfg_top_n_findings, parse_top_arg, resolve_top, select_top_by_cvss, select_top_logged; preserve alias and import-time effects.
```

## Local import links

- `from vvaharness.remediation_agent.discovery import Layout, cvss_score_of, load_findings, locate_report, prepare_layout` at source line 18: `source_detail/vvaharness/remediation_agent/discovery.py.sudo.md`.
- `from vvaharness.remediation_agent.interactive import decode_key, parse_selection, render_rows, run_interactive` at source line 25: `source_detail/vvaharness/remediation_agent/interactive/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.models import RemediationVerdict` at source line 31: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.options import VALID_MODES, RemediateOptions, parse_options` at source line 32: `source_detail/vvaharness/remediation_agent/options.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner import apply_plugin` at source line 37: `source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.remediate import remediate` at source line 38: `source_detail/vvaharness/remediation_agent/remediate.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser import DONE_MARKER, REMEDIATION_DIR_NAME, SCAN_DIR_NAME, Finding, find_scan_dir, latest_report, parse_findings` at source line 39: `source_detail/vvaharness/remediation_agent/report_parser/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.runner import model_banner, process_targets, remediate_one` at source line 48: `source_detail/vvaharness/remediation_agent/runner.py.sudo.md`.
- `from vvaharness.remediation_agent.select import band_score, cfg_top_n_findings, parse_top_arg, resolve_top, select_top_by_cvss, select_top_logged` at source line 53: `source_detail/vvaharness/remediation_agent/select/__init__.py.sudo.md`.
