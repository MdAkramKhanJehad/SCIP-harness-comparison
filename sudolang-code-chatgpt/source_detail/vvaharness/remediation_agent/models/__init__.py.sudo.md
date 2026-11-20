# vvaharness/remediation_agent/models/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/models/__init__.py.evidence.json`. SHA-256: `c3c5405ea92a019bf39b1d3c4f35861b2c17e8f47bafb5fbf6890cef70e85ecf`.

```sudo
// Source: vvaharness/remediation_agent/models/__init__.py:15-24
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models.change import Change; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models.fixer import FixerResult, FixerStatus; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models.gates import EvidenceGateStatus, Gates, GateStatus; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/models/__init__.py:25-41
In source order: Resolve source import from vvaharness.remediation_agent.models.verdict import RemediationVerdict, Verdict, to_evidence; preserve alias and import-time effects. Then Evaluate once ['Change', 'EvidenceGateStatus', 'FixerResult', 'FixerStatus', 'GateStatus', 'Gates', 'RemediationVerdict', 'Verdict', 'to_evidence']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.models.change import Change` at source line 18: `source_detail/vvaharness/remediation_agent/models/change.py.sudo.md`.
- `from vvaharness.remediation_agent.models.fixer import FixerResult, FixerStatus` at source line 19: `source_detail/vvaharness/remediation_agent/models/fixer.py.sudo.md`.
- `from vvaharness.remediation_agent.models.gates import EvidenceGateStatus, Gates, GateStatus` at source line 20: `source_detail/vvaharness/remediation_agent/models/gates.py.sudo.md`.
- `from vvaharness.remediation_agent.models.verdict import RemediationVerdict, Verdict, to_evidence` at source line 25: `source_detail/vvaharness/remediation_agent/models/verdict.py.sudo.md`.
