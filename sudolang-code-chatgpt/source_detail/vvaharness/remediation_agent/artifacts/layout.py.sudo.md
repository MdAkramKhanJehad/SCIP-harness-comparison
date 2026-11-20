# vvaharness/remediation_agent/artifacts/layout.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/layout.py.evidence.json`. SHA-256: `4a8346ede036ce0d6dacdac3189aa144631033607c225df9c674be62c5b3e0eb`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/layout.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Evaluate once ['DIFF_PATCH', 'EVIDENCE_DIR', 'FINDING_CASE_JSON', 'SUMMARY_MD', 'TRIAGE_JSON']; assign in source target order to __all__. Then Evaluate once 'evidence'; assign in source target order to EVIDENCE_DIR. Then Evaluate once 'triage.json'; assign in source target order to TRIAGE_JSON.
// Source: vvaharness/remediation_agent/artifacts/layout.py:28-31
In source order: Evaluate once 'summary.md'; assign in source target order to SUMMARY_MD. Then Evaluate once 'diff.patch'; assign in source target order to DIFF_PATCH. Then Evaluate once 'finding_case.json'; assign in source target order to FINDING_CASE_JSON.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
