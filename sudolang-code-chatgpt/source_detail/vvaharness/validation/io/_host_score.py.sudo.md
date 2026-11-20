# vvaharness/validation/io/_host_score.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/io/_host_score.py.evidence.json`. SHA-256: `f584d02ee1ba6d912f5042d80015b51a1095c4aadb22e5b4470919debe9e5cf8`.

```sudo
// Source: vvaharness/validation/io/_host_score.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/validation/io/_host_score.py:22-27
In source order: Resolve source import from typing import TYPE_CHECKING, NamedTuple; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Decision, Provenance, ScoringPolicy, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import SYNTHESIZED_GATES_FILENAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.scoring import score_fix; preserve alias and import-time effects.
// Source: vvaharness/validation/io/_host_score.py:29-30
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/io/_host_score.py:30-30
  In source order: Resolve source import from vvaharness.validation.models.output import OutputFinding; preserve alias and import-time effects.
}
// Source: vvaharness/validation/io/_host_score.py:32-40
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['conformant', 'load_synthesized_gates', 'verdict_for']; assign in source target order to __all__. Then Evaluate once source_literal_38_4; assign in source target order to _NO_GATES.
// Source: vvaharness/validation/io/_host_score.py:43-48
// Source signature: _read_gates_text(workspace_dir: Path) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_gates_text(workspace_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/_host_score.py:44-44
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call.
  // Source: vvaharness/validation/io/_host_score.py:45-48
  Perform the following protected operations {
    // Source: vvaharness/validation/io/_host_score.py:46-46
    End this invocation with (workspace_dir / SYNTHESIZED_GATES_FILENAME).read_text(encoding='utf-8').
  }
  // Source: vvaharness/validation/io/_host_score.py:47-48
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/validation/io/_host_score.py:48-48
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/_host_score.py:51-61
// Source signature: _parse_gates_array(text: str) -> list[object] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_gates_array(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/_host_score.py:52-52
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call.
  // Source: vvaharness/validation/io/_host_score.py:53-57
  Perform the following protected operations {
    // Source: vvaharness/validation/io/_host_score.py:54-54
    In source order: For data, assign json.loads(text); source annotation object.
  }
  // Source: vvaharness/validation/io/_host_score.py:55-57
  On the first matching source exception (json.JSONDecodeError, ValueError), in handler order {
    // Source: vvaharness/validation/io/_host_score.py:56-56
    In source order: Evaluate log.warning('%s present but unparseable; failing closed', SYNTHESIZED_GATES_FILENAME); retain side effects and discard the expression result.
    // Source: vvaharness/validation/io/_host_score.py:57-57
    End this invocation with None.
  }
  // Source: vvaharness/validation/io/_host_score.py:58-59
  if (the source predicate isinstance(data, list) is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:59-59
    End this invocation with data.
  }
  // Source: vvaharness/validation/io/_host_score.py:60-60
  In source order: Evaluate log.warning('%s is not a JSON array; failing closed', SYNTHESIZED_GATES_FILENAME); retain side effects and discard the expression result.
  // Source: vvaharness/validation/io/_host_score.py:61-61
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/_host_score.py:64-75
// Source signature: _gates_by_tracking_id(data: list[object]) -> dict[str, list[Mapping[str, object]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gates_by_tracking_id(data) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/_host_score.py:65-67
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then For gates_by_id, assign {}; source annotation dict[str, list[Mapping[str, object]]]. Then For dropped, assign 0; source annotation int.
  // Source: vvaharness/validation/io/_host_score.py:68-72
  for each entry in data {
    // Source: vvaharness/validation/io/_host_score.py:69-72
    if (the source predicate isinstance(entry, Mapping) and isinstance(entry.get('gates'), list) is truthy) {
      // Source: vvaharness/validation/io/_host_score.py:70-70
      In source order: Evaluate once entry['gates']; assign in source target order to gates_by_id[str(entry.get('tracking_id', ''))].
    }
    else {
      // Source: vvaharness/validation/io/_host_score.py:72-72
      In source order: Apply source augmented assignment dropped += 1 with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/validation/io/_host_score.py:73-74
  if (the source predicate dropped is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:74-74
    In source order: Evaluate log.warning('dropped %d malformed entries from %s', dropped, SYNTHESIZED_GATES_FILENAME); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/io/_host_score.py:75-75
  End this invocation with gates_by_id.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/_host_score.py:78-86
// Source signature: load_synthesized_gates(workspace_dir: Path) -> dict[str, list[Mapping[str, object]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_synthesized_gates(workspace_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/_host_score.py:79-80
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call. Then For text, assign _read_gates_text(workspace_dir); source annotation str | None.
  // Source: vvaharness/validation/io/_host_score.py:81-82
  if (the source predicate text is None is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:82-82
    End this invocation with {}.
  }
  // Source: vvaharness/validation/io/_host_score.py:83-83
  In source order: For data, assign _parse_gates_array(text); source annotation list[object] | None.
  // Source: vvaharness/validation/io/_host_score.py:84-85
  if (the source predicate data is None is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:85-85
    End this invocation with {}.
  }
  // Source: vvaharness/validation/io/_host_score.py:86-86
  End this invocation with _gates_by_tracking_id(data).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/_host_score.py:89-94
interface _Narrative {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/io/_host_score.py:90-94
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call. Then For conditions, assign (); source annotation tuple[str, ...]. Then For recommendations, assign (); source annotation tuple[str, ...]. Then For rationale, assign ''; source annotation str.
}
// Source: vvaharness/validation/io/_host_score.py:97-105
// Source signature: _narrative(output_finding: OutputFinding | None) -> _Narrative
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _narrative(output_finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/_host_score.py:98-98
  In source order: Retain source documentation literal source_literal_98_4; it is not a model call.
  // Source: vvaharness/validation/io/_host_score.py:99-100
  if (the source predicate output_finding is None is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:100-100
    End this invocation with _Narrative().
  }
  // Source: vvaharness/validation/io/_host_score.py:101-105
  End this invocation with _Narrative(conditions=tuple(output_finding.conditions_for_full_fix), recommendations=tuple(output_finding.recommendations), rationale=output_finding.justification or '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/_host_score.py:108-120
// Source signature: conformant(verdict: Verdict, policy: ScoringPolicy | None) -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn conformant(verdict, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/_host_score.py:109-109
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call.
  // Source: vvaharness/validation/io/_host_score.py:110-111
  if (the source predicate policy is None is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:111-111
    End this invocation with verdict.
  }
  // Source: vvaharness/validation/io/_host_score.py:112-112
  In source order: Evaluate once policy.missing_from((gate.name for gate in verdict.gates)); assign in source target order to missing.
  // Source: vvaharness/validation/io/_host_score.py:113-114
  if (the source predicate not missing is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:114-114
    End this invocation with verdict.
  }
  // Source: vvaharness/validation/io/_host_score.py:115-120
  End this invocation with verdict.model_copy(update={'decision': Decision.INCONCLUSIVE, 'score': None, 'rationale': source_template_118_22}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/_host_score.py:123-153
// Source signature: verdict_for(output_finding: OutputFinding | None, gates: list[Mapping[str, object]] | None, *, provenance: Provenance, policy: ScoringPolicy | None=None) -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn verdict_for(output_finding, gates, provenance, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/_host_score.py:130-131
  In source order: Retain source documentation literal source_literal_130_4; it is not a model call. Then Evaluate once _narrative(output_finding); assign in source target order to said.
  // Source: vvaharness/validation/io/_host_score.py:132-141
  if (the source predicate not gates is truthy) {
    // Source: vvaharness/validation/io/_host_score.py:133-141
    End this invocation with Verdict(decision=Decision.INCONCLUSIVE, rationale=_NO_GATES, score=None, conditions=said.conditions, recommendations=said.recommendations, engine_rationale=said.rationale, produced_by=provenance).
  }
  // Source: vvaharness/validation/io/_host_score.py:142-142
  In source order: Evaluate once score_fix(list(gates), policy=policy); assign in source target order to scored.
  // Source: vvaharness/validation/io/_host_score.py:143-153
  End this invocation with Verdict(decision=scored.decision, rationale=scored.justification, score=None if scored.decision is Decision.INCONCLUSIVE else scored.raw_score, gates=scored.gates, conditions=said.conditions, recommendations=said.recommendations, engine_rationale=said.rationale, produced_by=provenance).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Decision, Provenance, ScoringPolicy, Verdict` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import SYNTHESIZED_GATES_FILENAME` at source line 26: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.scoring import score_fix` at source line 27: `source_detail/vvaharness/validation/scoring/__init__.py.sudo.md`.
- `from vvaharness.validation.models.output import OutputFinding` at source line 30: `source_detail/vvaharness/validation/models/output.py.sudo.md`.
