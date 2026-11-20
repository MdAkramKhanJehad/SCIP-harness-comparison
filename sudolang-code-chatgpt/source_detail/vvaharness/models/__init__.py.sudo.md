# vvaharness/models/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/__init__.py.evidence.json`. SHA-256: `4d4a6aa8541ddfdf0e637695df1a510a053721126be691ee9022a43127d4a594`.

```sudo
// Source: vvaharness/models/__init__.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from vvaharness.models.case import Attempt, FindingCase; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.context import ScoringPolicy; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.derive import merge_readiness_for, state_of, verdict_state; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.gates import EvidenceAnchor, GateAssessment; preserve alias and import-time effects.
// Source: vvaharness/models/__init__.py:22-84
In source order: Resolve source import from vvaharness.models.provenance import HARNESS_REGISTRY, LLM_REGISTRY, Provenance; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.remediation import FileChange, Remediation, RemediationEvidence, finalize; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan import _MD_INVISIBLE_RX, _MD_LINEBREAK_RX, CVE, OFFENSIVE_LABELS, AppProfile, Asset, Chain, ContextPackage, Control, DroppedFinding, DupLocation, EntryPoint, FinalReport, Finding, InvestigationUnit, LinkEvidence, ModuleInfo, RankedFinding, ScanMetrics, ScopeEntry, SeedPackage, Severity, Sink, TaskManifest, Threat, ThreatModel, TrustBoundary, UnitSize, VulnClass, _cap_assets, _cap_boundaries, _cap_threats, _demote_md_headings, _md_cell, _snippet_fence, _vector_span; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.verdict import Ticket, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import CANONICAL_GATE_NAMES, EVIDENCE_GATES, FIX_VALIDATION_GATES, CaseState, Decision, Disposition, GateStatus, MergeReadiness, RemediationKind, RemediationOutcome, normalise_gate_name; preserve alias and import-time effects.
// Source: vvaharness/models/__init__.py:86-142
In source order: Evaluate once ['CANONICAL_GATE_NAMES', 'CVE', 'EVIDENCE_GATES', 'FIX_VALIDATION_GATES', 'HARNESS_REGISTRY', 'LLM_REGISTRY', 'OFFENSIVE_LABELS', 'AppProfile', 'Asset', 'Attempt', 'CaseState', 'Chain', 'ContextPackage', 'Control', 'Decision', 'Disposition', 'DroppedFinding', 'DupLocation', 'EntryPoint', 'EvidenceAnchor', 'FileChange', 'FinalReport', 'Finding', 'FindingCase', 'GateAssessment', 'GateStatus', 'InvestigationUnit', 'LinkEvidence', 'MergeReadiness', 'ModuleInfo', 'Provenance', 'RankedFinding', 'Remediation', 'RemediationEvidence', 'RemediationKind', 'RemediationOutcome', 'ScanMetrics', 'ScopeEntry', 'ScoringPolicy', 'SeedPackage', 'Severity', 'Sink', 'TaskManifest', 'Threat', 'ThreatModel', 'Ticket', 'TrustBoundary', 'UnitSize', 'Verdict', 'VulnClass', 'finalize', 'merge_readiness_for', 'normalise_gate_name', 'state_of', 'verdict_state']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.models.case import Attempt, FindingCase` at source line 18: `source_detail/vvaharness/models/case.py.sudo.md`.
- `from vvaharness.models.context import ScoringPolicy` at source line 19: `source_detail/vvaharness/models/context.py.sudo.md`.
- `from vvaharness.models.derive import merge_readiness_for, state_of, verdict_state` at source line 20: `source_detail/vvaharness/models/derive.py.sudo.md`.
- `from vvaharness.models.gates import EvidenceAnchor, GateAssessment` at source line 21: `source_detail/vvaharness/models/gates.py.sudo.md`.
- `from vvaharness.models.provenance import HARNESS_REGISTRY, LLM_REGISTRY, Provenance` at source line 22: `source_detail/vvaharness/models/provenance.py.sudo.md`.
- `from vvaharness.models.remediation import FileChange, Remediation, RemediationEvidence, finalize` at source line 27: `source_detail/vvaharness/models/remediation.py.sudo.md`.
- `from vvaharness.models.scan import _MD_INVISIBLE_RX, _MD_LINEBREAK_RX, CVE, OFFENSIVE_LABELS, AppProfile, Asset, Chain, ContextPackage, Control, DroppedFinding, DupLocation, EntryPoint, FinalReport, Finding, InvestigationUnit, LinkEvidence, ModuleInfo, RankedFinding, ScanMetrics, ScopeEntry, SeedPackage, Severity, Sink, TaskManifest, Threat, ThreatModel, TrustBoundary, UnitSize, VulnClass, _cap_assets, _cap_boundaries, _cap_threats, _demote_md_headings, _md_cell, _snippet_fence, _vector_span` at source line 33: `source_detail/vvaharness/models/scan/__init__.py.sudo.md`.
- `from vvaharness.models.verdict import Ticket, Verdict` at source line 71: `source_detail/vvaharness/models/verdict.py.sudo.md`.
- `from vvaharness.models.vocab import CANONICAL_GATE_NAMES, EVIDENCE_GATES, FIX_VALIDATION_GATES, CaseState, Decision, Disposition, GateStatus, MergeReadiness, RemediationKind, RemediationOutcome, normalise_gate_name` at source line 72: `source_detail/vvaharness/models/vocab.py.sudo.md`.
