# vvaharness/validation/models/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/models/__init__.py.evidence.json`. SHA-256: `0bc6d3711da55b634e1f107ab91aafb91f7d1ccc17a53dd7713799739d093a7e`.

```sudo
// Source: vvaharness/validation/models/__init__.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.manifest import Manifest; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.output import GateEntry, OutputFinding, SynthesizedGatesEntry, ValidationOutput, ValidationReport, to_verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.persona_report import HarnessTerminalState, PersonaGateEntry, PersonaReport; preserve alias and import-time effects.
// Source: vvaharness/validation/models/__init__.py:33-75
In source order: Resolve source import from vvaharness.validation.models.plans import FixValidationPlan; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.results import RunMetadata, SarifLocation, ValidationResult, gate_score_rows, render_row, unverifiable_row; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.scoring import RawCriterion, RawExtra, ScoreResult, ScoringConfig, ValidationScore, VerdictRule; preserve alias and import-time effects. Then Evaluate once ['FixValidationPlan', 'GateEntry', 'HarnessTerminalState', 'Manifest', 'OutputFinding', 'PersonaGateEntry', 'PersonaReport', 'RawCriterion', 'RawExtra', 'RunMetadata', 'SarifLocation', 'ScoreResult', 'ScoringConfig', 'SynthesizedGatesEntry', 'ValidationOutput', 'ValidationReport', 'ValidationResult', 'ValidationScore', 'VerdictRule', 'gate_score_rows', 'render_row', 'to_verdict', 'unverifiable_row']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.validation.models.manifest import Manifest` at source line 19: `source_detail/vvaharness/validation/models/manifest.py.sudo.md`.
- `from vvaharness.validation.models.output import GateEntry, OutputFinding, SynthesizedGatesEntry, ValidationOutput, ValidationReport, to_verdict` at source line 20: `source_detail/vvaharness/validation/models/output.py.sudo.md`.
- `from vvaharness.validation.models.persona_report import HarnessTerminalState, PersonaGateEntry, PersonaReport` at source line 28: `source_detail/vvaharness/validation/models/persona_report.py.sudo.md`.
- `from vvaharness.validation.models.plans import FixValidationPlan` at source line 33: `source_detail/vvaharness/validation/models/plans.py.sudo.md`.
- `from vvaharness.validation.models.results import RunMetadata, SarifLocation, ValidationResult, gate_score_rows, render_row, unverifiable_row` at source line 34: `source_detail/vvaharness/validation/models/results.py.sudo.md`.
- `from vvaharness.validation.models.scoring import RawCriterion, RawExtra, ScoreResult, ScoringConfig, ValidationScore, VerdictRule` at source line 42: `source_detail/vvaharness/validation/models/scoring.py.sudo.md`.
