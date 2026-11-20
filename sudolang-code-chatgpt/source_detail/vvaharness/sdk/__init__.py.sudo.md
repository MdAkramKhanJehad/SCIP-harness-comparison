# vvaharness/sdk/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/sdk/__init__.py.evidence.json`. SHA-256: `50fa1ae01b6d625b60391d33a779528917402f50af51eefe97fb4cb0831c70bd`.

```sudo
// Source: vvaharness/sdk/__init__.py:15-50
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from vvaharness.api import MergeReadiness, Remediation, ScoringPolicy, Verdict, merge_readiness_for, remediate, state_of, validate; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, FinalReport, Finding, InvestigationUnit, SeedPackage, TaskManifest, ThreatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.sdk.handoff import DISCOVERY_STAGES, MAX_INJECTED_FINDINGS, Handoff, HandoffError, inject_findings; preserve alias and import-time effects. Then Resolve source import from vvaharness.sdk.plugins import MAX_PLUGIN_GRAPH_TOOLS, MAX_PLUGINS, Contribution, GraphEnricher, PluginInfo, PluginSet, VvahPlugin; preserve alias and import-time effects.
// Source: vvaharness/sdk/__init__.py:51-112
In source order: Resolve source import from vvaharness.sdk.runner import ScanOptions, ScanOptionsError, ScanResult, profile_path, scan; preserve alias and import-time effects. Then Resolve source import from vvaharness.sdk.stages import CHECKPOINTED, STAGES, Phase, Seam, Stage, injectable_stages, stage, stages_in, stages_with; preserve alias and import-time effects. Then Evaluate once ['CHECKPOINTED', 'DISCOVERY_STAGES', 'MAX_INJECTED_FINDINGS', 'MAX_PLUGINS', 'MAX_PLUGIN_GRAPH_TOOLS', 'STAGES', 'ContextPackage', 'Contribution', 'FinalReport', 'Finding', 'GraphEnricher', 'Handoff', 'HandoffError', 'InvestigationUnit', 'MergeReadiness', 'Phase', 'PluginInfo', 'PluginSet', 'Remediation', 'ScanOptions', 'ScanOptionsError', 'ScanResult', 'ScoringPolicy', 'Seam', 'SeedPackage', 'Stage', 'TaskManifest', 'ThreatModel', 'Verdict', 'VvahPlugin', 'inject_findings', 'injectable_stages', 'merge_readiness_for', 'profile_path', 'remediate', 'scan', 'stage', 'stages_in', 'stages_with', 'state_of', 'validate']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.api import MergeReadiness, Remediation, ScoringPolicy, Verdict, merge_readiness_for, remediate, state_of, validate` at source line 16: `source_detail/vvaharness/api.py.sudo.md`.
- `from vvaharness.models import ContextPackage, FinalReport, Finding, InvestigationUnit, SeedPackage, TaskManifest, ThreatModel` at source line 26: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.sdk.handoff import DISCOVERY_STAGES, MAX_INJECTED_FINDINGS, Handoff, HandoffError, inject_findings` at source line 35: `source_detail/vvaharness/sdk/handoff.py.sudo.md`.
- `from vvaharness.sdk.plugins import MAX_PLUGIN_GRAPH_TOOLS, MAX_PLUGINS, Contribution, GraphEnricher, PluginInfo, PluginSet, VvahPlugin` at source line 42: `source_detail/vvaharness/sdk/plugins.py.sudo.md`.
- `from vvaharness.sdk.runner import ScanOptions, ScanOptionsError, ScanResult, profile_path, scan` at source line 51: `source_detail/vvaharness/sdk/runner.py.sudo.md`.
- `from vvaharness.sdk.stages import CHECKPOINTED, STAGES, Phase, Seam, Stage, injectable_stages, stage, stages_in, stages_with` at source line 58: `source_detail/vvaharness/sdk/stages.py.sudo.md`.
