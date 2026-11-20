# vvaharness/validation/constants/scoring.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/scoring.py.evidence.json`. SHA-256: `818cc07aa9ff7be87d356215aa4e8709ad3946abe5ed89e4fbb147a2de70145d`.

```sudo
// Source: vvaharness/validation/constants/scoring.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import FIX_VALIDATION_GATES, GateStatus, ScoringPolicy; preserve alias and import-time effects. Then Evaluate once ['CONFIDENCE_PERCENT_SCALE', 'CRITERION_NAME_FIELD', 'FIX_POLICY', 'GATE_WEIGHTS', 'MAX_EVIDENCE_ANCHORS', 'SCORE_FLOOR', 'SCORE_PRECISION', 'STATUS_MULTIPLIER']; assign in source target order to __all__.
// Source: vvaharness/validation/constants/scoring.py:35-62
In source order: For GATE_WEIGHTS, assign {'root_cause': 0.43, 'instance_coverage': 0.2467, 'no_new_vulnerabilities': 0.1867, 'security_best_practices': 0.1366}; source annotation Final[dict[str, float]]. Then For _CRITICAL_GATES, assign frozenset({'no_new_vulnerabilities', 'root_cause'}); source annotation Final[frozenset[str]]. Then For FIX_POLICY, assign ScoringPolicy(required_gates=FIX_VALIDATION_GATES, weights=GATE_WEIGHTS, critical=_CRITICAL_GATES, ready_at=0.8, conditional_at=0.5); source annotation Final[ScoringPolicy]. Then For STATUS_MULTIPLIER, assign {GateStatus.PASS.value: 1.0, GateStatus.PARTIAL.value: 0.5, GateStatus.FAIL.value: 0.0, GateStatus.SKIP.value: 0.0}; source annotation Final[dict[str, float]]. Then For SCORE_FLOOR, assign 0.0; source annotation Final[float].
// Source: vvaharness/validation/constants/scoring.py:65-71
In source order: For CRITERION_NAME_FIELD, assign 'gate_name'; source annotation Final[str]. Then For SCORE_PRECISION, assign 4; source annotation Final[int]. Then For CONFIDENCE_PERCENT_SCALE, assign 100; source annotation Final[int]. Then For MAX_EVIDENCE_ANCHORS, assign 5; source annotation Final[int].
```

## Local import links

- `from vvaharness.models import FIX_VALIDATION_GATES, GateStatus, ScoringPolicy` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
