# vvaharness/models/scan/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/__init__.py.evidence.json`. SHA-256: `ee6ac8cbe44d29b40a78858369112fe5c86e8d455f2e33a1b1cc4d55e84bae24`.

```sudo
// Source: vvaharness/models/scan/__init__.py:15-42
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from vvaharness.models.scan._coerce import _coerce_enum, _coerce_int, _coerce_scalar_str, _coerce_str_list, _norm; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _ATX_HEADING_RX, _FENCE_RX, _MD_INVISIBLE_RX, _MD_LINEBREAK_RX, _demote_md_headings, _md_cell, _render_repro_block, _snippet_fence, _vector_span; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.context import ContextPackage; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.findings import Chain, DroppedFinding, Finding, LinkEvidence, RankedFinding; preserve alias and import-time effects.
// Source: vvaharness/models/scan/__init__.py:43-47
In source order: Resolve source import from vvaharness.models.scan.inputs import CVE, AppProfile, Control; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.metrics import ScanMetrics, ScopeEntry; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.report import FinalReport; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.seed import SeedPackage; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.surface import EntryPoint, ModuleInfo, Sink; preserve alias and import-time effects.
// Source: vvaharness/models/scan/__init__.py:48-105
In source order: Resolve source import from vvaharness.models.scan.threat import Asset, Threat, ThreatModel, TrustBoundary, _cap_assets, _cap_boundaries, _cap_threats; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.work import DupLocation, InvestigationUnit, TaskManifest, UnitSize; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import OFFENSIVE_LABELS, Severity, VulnClass; preserve alias and import-time effects. Then Evaluate once ['CVE', 'OFFENSIVE_LABELS', '_ATX_HEADING_RX', '_FENCE_RX', '_MD_INVISIBLE_RX', '_MD_LINEBREAK_RX', 'AppProfile', 'Asset', 'Chain', 'ContextPackage', 'Control', 'DroppedFinding', 'DupLocation', 'EntryPoint', 'FinalReport', 'Finding', 'InvestigationUnit', 'LinkEvidence', 'ModuleInfo', 'RankedFinding', 'ScanMetrics', 'ScopeEntry', 'SeedPackage', 'Severity', 'Sink', 'TaskManifest', 'Threat', 'ThreatModel', 'TrustBoundary', 'UnitSize', 'VulnClass', '_cap_assets', '_cap_boundaries', '_cap_threats', '_coerce_enum', '_coerce_int', '_coerce_scalar_str', '_coerce_str_list', '_demote_md_headings', '_md_cell', '_norm', '_render_repro_block', '_snippet_fence', '_vector_span']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.models.scan._coerce import _coerce_enum, _coerce_int, _coerce_scalar_str, _coerce_str_list, _norm` at source line 17: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.models.scan._render import _ATX_HEADING_RX, _FENCE_RX, _MD_INVISIBLE_RX, _MD_LINEBREAK_RX, _demote_md_headings, _md_cell, _render_repro_block, _snippet_fence, _vector_span` at source line 24: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.models.scan.context import ContextPackage` at source line 35: `source_detail/vvaharness/models/scan/context.py.sudo.md`.
- `from vvaharness.models.scan.findings import Chain, DroppedFinding, Finding, LinkEvidence, RankedFinding` at source line 36: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.scan.inputs import CVE, AppProfile, Control` at source line 43: `source_detail/vvaharness/models/scan/inputs.py.sudo.md`.
- `from vvaharness.models.scan.metrics import ScanMetrics, ScopeEntry` at source line 44: `source_detail/vvaharness/models/scan/metrics.py.sudo.md`.
- `from vvaharness.models.scan.report import FinalReport` at source line 45: `source_detail/vvaharness/models/scan/report.py.sudo.md`.
- `from vvaharness.models.scan.seed import SeedPackage` at source line 46: `source_detail/vvaharness/models/scan/seed.py.sudo.md`.
- `from vvaharness.models.scan.surface import EntryPoint, ModuleInfo, Sink` at source line 47: `source_detail/vvaharness/models/scan/surface.py.sudo.md`.
- `from vvaharness.models.scan.threat import Asset, Threat, ThreatModel, TrustBoundary, _cap_assets, _cap_boundaries, _cap_threats` at source line 48: `source_detail/vvaharness/models/scan/threat.py.sudo.md`.
- `from vvaharness.models.scan.work import DupLocation, InvestigationUnit, TaskManifest, UnitSize` at source line 57: `source_detail/vvaharness/models/scan/work.py.sudo.md`.
- `from vvaharness.models.vocab import OFFENSIVE_LABELS, Severity, VulnClass` at source line 58: `source_detail/vvaharness/models/vocab.py.sudo.md`.
