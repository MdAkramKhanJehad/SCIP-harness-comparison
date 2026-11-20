# vvaharness/remediation_agent/select/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/select/__init__.py.evidence.json`. SHA-256: `2a101f253a596037acde5eb1bbaf6fd92395106ad8222c3f862aa380c414c1b2`.

```sudo
// Source: vvaharness/remediation_agent/select/__init__.py:15-42
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.select.pq import band_score, drop_non_main_channel, select_top_by_cvss, select_top_logged; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.select.topspec import ALL_FINDINGS, _coerce_top_value, cfg_top_n_findings, parse_top_arg, resolve_top; preserve alias and import-time effects. Then Evaluate once ['ALL_FINDINGS', '_coerce_top_value', 'band_score', 'cfg_top_n_findings', 'drop_non_main_channel', 'parse_top_arg', 'resolve_top', 'select_top_by_cvss', 'select_top_logged']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.select.pq import band_score, drop_non_main_channel, select_top_by_cvss, select_top_logged` at source line 18: `source_detail/vvaharness/remediation_agent/select/pq.py.sudo.md`.
- `from vvaharness.remediation_agent.select.topspec import ALL_FINDINGS, _coerce_top_value, cfg_top_n_findings, parse_top_arg, resolve_top` at source line 24: `source_detail/vvaharness/remediation_agent/select/topspec.py.sudo.md`.
