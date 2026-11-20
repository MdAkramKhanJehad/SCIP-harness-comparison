# vvaharness/validation/synthesis/_consensus.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/synthesis/_consensus.py.evidence.json`. SHA-256: `7867451b2b5113f0df5967350d717f67550153f0ac315cf80514db2cf04a12f3`.

```sudo
// Source: vvaharness/validation/synthesis/_consensus.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections import Counter; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel; preserve alias and import-time effects.
// Source: vvaharness/validation/synthesis/_consensus.py:24-28
In source order: Resolve source import from vvaharness.models import FIX_VALIDATION_GATES, GateStatus; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import normalise_gate_name; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.synthesis import MIN_CONSENSUS_VOTES; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.enums.synthesis import SynthesisConfidence; preserve alias and import-time effects.
// Source: vvaharness/validation/synthesis/_consensus.py:29-43
In source order: Resolve source import from vvaharness.validation.models.persona_report import PersonaGateEntry, PersonaReport; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then For _STATUS_CONSERVATIVE_RANK, assign (GateStatus.FAIL, GateStatus.PARTIAL, GateStatus.PASS, GateStatus.SKIP, GateStatus.INVALID); source annotation tuple[GateStatus, ...].
// Source: vvaharness/validation/synthesis/_consensus.py:46-52
interface SynthesizedEvidence {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/synthesis/_consensus.py:47-52
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then For persona, declare without assigning a value; source annotation str. Then For file, declare without assigning a value; source annotation str. Then For line, declare without assigning a value; source annotation int | None. Then For snippet, declare without assigning a value; source annotation str.
}
// Source: vvaharness/validation/synthesis/_consensus.py:55-65
interface SynthesizedGate {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/synthesis/_consensus.py:56-61
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call. Then For tracking_id, declare without assigning a value; source annotation str. Then For gate_name, declare without assigning a value; source annotation str. Then For status, declare without assigning a value; source annotation GateStatus. Then For confidence, declare without assigning a value; source annotation SynthesisConfidence.
  // Source: vvaharness/validation/synthesis/_consensus.py:62-65
  In source order: For summary, declare without assigning a value; source annotation str. Then For details, declare without assigning a value; source annotation str. Then For evidence, declare without assigning a value; source annotation list[SynthesizedEvidence]. Then For persona_votes, declare without assigning a value; source annotation dict[str, GateStatus].
}
// Source: vvaharness/validation/synthesis/_consensus.py:68-74
// Source signature: _most_conservative_status(statuses: Iterable[GateStatus]) -> GateStatus
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _most_conservative_status(statuses) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/synthesis/_consensus.py:69-70
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call. Then Evaluate once set(statuses); assign in source target order to present.
  // Source: vvaharness/validation/synthesis/_consensus.py:71-73
  for each status in _STATUS_CONSERVATIVE_RANK {
    // Source: vvaharness/validation/synthesis/_consensus.py:72-73
    if (the source predicate status in present is truthy) {
      // Source: vvaharness/validation/synthesis/_consensus.py:73-73
      End this invocation with status.
    }
  }
  // Source: vvaharness/validation/synthesis/_consensus.py:74-74
  End this invocation with GateStatus.INVALID.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/synthesis/_consensus.py:77-100
// Source signature: _persona_votes(entries: list[tuple[str, PersonaGateEntry]], gate_name: str, tracking_id: str) -> dict[str, GateStatus]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _persona_votes(entries, gate_name, tracking_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/synthesis/_consensus.py:82-84
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call. Then For votes, assign {}; source annotation dict[str, GateStatus].
  // Source: vvaharness/validation/synthesis/_consensus.py:85-99
  for each (persona, gate) in entries {
    // Source: vvaharness/validation/synthesis/_consensus.py:86-86
    In source order: Evaluate once votes.get(persona); assign in source target order to prior.
    // Source: vvaharness/validation/synthesis/_consensus.py:87-96
    if (the source predicate prior is truthy) {
      // Source: vvaharness/validation/synthesis/_consensus.py:88-96
      In source order: Evaluate log.warning('duplicate gate vote for persona=%s gate=%s tracking_id=%s: prior=%s new=%s; merging to most conservative status', persona, gate_name, tracking_id, prior, gate.status); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/synthesis/_consensus.py:97-99
    In source order: Evaluate once _most_conservative_status([prior, gate.status]) if prior else gate.status; assign in source target order to votes[persona].
  }
  // Source: vvaharness/validation/synthesis/_consensus.py:100-100
  End this invocation with votes.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/synthesis/_consensus.py:103-126
// Source signature: _missing_required_gates(by_gate: dict[str, list[tuple[str, PersonaGateEntry]]], tracking_id: str, required_gates: Iterable[str]) -> list[SynthesizedGate]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _missing_required_gates(by_gate, tracking_id, required_gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/synthesis/_consensus.py:108-108
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call.
  // Source: vvaharness/validation/synthesis/_consensus.py:110-111
  if (the source predicate not by_gate is truthy) {
    // Source: vvaharness/validation/synthesis/_consensus.py:111-111
    End this invocation with [].
  }
  // Source: vvaharness/validation/synthesis/_consensus.py:112-112
  In source order: Evaluate once {normalise_gate_name(name) for name in by_gate}; assign in source target order to answered.
  // Source: vvaharness/validation/synthesis/_consensus.py:113-126
  End this invocation with [SynthesizedGate(tracking_id=tracking_id, gate_name=gate_name, status=GateStatus.INVALID, confidence=SynthesisConfidence.FLAGGED, summary='', details=source_template_120_20, evidence=[], persona_votes={}) for gate_name in required_gates if normalise_gate_name(gate_name) not in answered].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/synthesis/_consensus.py:129-189
// Source signature: synthesize_gates_for_finding(reports: list[PersonaReport], tracking_id: str, required_gates: Iterable[str]=FIX_VALIDATION_GATES) -> list[SynthesizedGate]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn synthesize_gates_for_finding(reports, tracking_id, required_gates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/synthesis/_consensus.py:134-135
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call. Then For by_gate, assign {}; source annotation dict[str, list[tuple[str, PersonaGateEntry]]].
  // Source: vvaharness/validation/synthesis/_consensus.py:136-140
  for each report in reports {
    // Source: vvaharness/validation/synthesis/_consensus.py:137-138
    if (the source predicate report.tracking_id != tracking_id is truthy) {
      // Source: vvaharness/validation/synthesis/_consensus.py:138-138
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/synthesis/_consensus.py:139-140
    for each gate in report.gates {
      // Source: vvaharness/validation/synthesis/_consensus.py:140-140
      In source order: Evaluate by_gate.setdefault(gate.gate_name, []).append((report.persona, gate)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/validation/synthesis/_consensus.py:142-142
  In source order: For synthesized, assign []; source annotation list[SynthesizedGate].
  // Source: vvaharness/validation/synthesis/_consensus.py:143-186
  for each (gate_name, entries) in sorted(by_gate.items()) {
    // Source: vvaharness/validation/synthesis/_consensus.py:144-146
    In source order: Evaluate once _persona_votes(entries, gate_name, tracking_id); assign in source target order to votes. Then Evaluate once [s for s in votes.values() if s != GateStatus.SKIP]; assign in source target order to evaluated.
    // Source: vvaharness/validation/synthesis/_consensus.py:147-157
    if (the source predicate not evaluated is truthy) {
      // Source: vvaharness/validation/synthesis/_consensus.py:148-148
      In source order: Evaluate once (GateStatus.SKIP, SynthesisConfidence.FLAGGED); assign in source target order to (chosen_status, confidence).
    }
    else {
      // Source: vvaharness/validation/synthesis/_consensus.py:150-152
      In source order: Evaluate once Counter(evaluated); assign in source target order to counter. Then Evaluate once max(counter.values()); assign in source target order to top_frequency. Then Evaluate once [s for s, freq in counter.items() if freq == top_frequency]; assign in source target order to top_statuses.
      // Source: vvaharness/validation/synthesis/_consensus.py:153-157
      if (the source predicate len(top_statuses) == 1 and top_frequency >= MIN_CONSENSUS_VOTES is truthy) {
        // Source: vvaharness/validation/synthesis/_consensus.py:154-154
        In source order: Evaluate once (top_statuses[0], SynthesisConfidence.HIGH); assign in source target order to (chosen_status, confidence).
      }
      else {
        // Source: vvaharness/validation/synthesis/_consensus.py:156-157
        In source order: Evaluate once _most_conservative_status(top_statuses); assign in source target order to chosen_status. Then Evaluate once SynthesisConfidence.FLAGGED; assign in source target order to confidence.
      }
    }
    // Source: vvaharness/validation/synthesis/_consensus.py:159-161
    In source order: For summaries, assign []; source annotation list[str]. Then For details_pieces, assign []; source annotation list[str]. Then For evidence, assign []; source annotation list[SynthesizedEvidence].
    // Source: vvaharness/validation/synthesis/_consensus.py:162-170
    for each (persona, gate) in sorted(entries, key=lambda item: item[0]) {
      // Source: vvaharness/validation/synthesis/_consensus.py:163-164
      if (the source predicate gate.summary is truthy) {
        // Source: vvaharness/validation/synthesis/_consensus.py:164-164
        In source order: Evaluate summaries.append(source_template_164_33); retain side effects and discard the expression result.
      }
      // Source: vvaharness/validation/synthesis/_consensus.py:165-166
      if (the source predicate gate.details is truthy) {
        // Source: vvaharness/validation/synthesis/_consensus.py:166-166
        In source order: Evaluate details_pieces.append(source_template_166_38); retain side effects and discard the expression result.
      }
      // Source: vvaharness/validation/synthesis/_consensus.py:167-170
      In source order: Evaluate evidence.extend((SynthesizedEvidence(persona=persona, file=ev.file, line=ev.line, snippet=ev.snippet) for ev in gate.evidence)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/synthesis/_consensus.py:172-186
    In source order: Evaluate synthesized.append(SynthesizedGate(tracking_id=tracking_id, gate_name=gate_name, status=chosen_status, confidence=confidence, summary=' | '.join(summaries), details=' | '.join(details_pieces), evidence=sorted(evidence, key=lambda item: (item.file or '', item.line or 0)), persona_votes=dict(sorted(votes.items())))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/synthesis/_consensus.py:188-188
  In source order: Evaluate synthesized.extend(_missing_required_gates(by_gate, tracking_id, required_gates)); retain side effects and discard the expression result.
  // Source: vvaharness/validation/synthesis/_consensus.py:189-189
  End this invocation with synthesized.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FIX_VALIDATION_GATES, GateStatus` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.vocab import normalise_gate_name` at source line 25: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.constants.synthesis import MIN_CONSENSUS_VOTES` at source line 27: `source_detail/vvaharness/validation/constants/synthesis.py.sudo.md`.
- `from vvaharness.validation.enums.synthesis import SynthesisConfidence` at source line 28: `source_detail/vvaharness/validation/enums/synthesis.py.sudo.md`.
- `from vvaharness.validation.models.persona_report import PersonaGateEntry, PersonaReport` at source line 29: `source_detail/vvaharness/validation/models/persona_report.py.sudo.md`.
