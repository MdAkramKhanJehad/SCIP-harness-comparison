# vvaharness/pipeline/stages/s4/outcomes.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s4/outcomes.py.evidence.json`. SHA-256: `6edb1ce49417e3d1513dc81ae6a4e659b20ebe07f883da4a53941151181c60f2`.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Collection; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, field_validator; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/outcomes.py:23-27
In source order: Resolve source import from vvaharness.models.scan._coerce import _coerce_int; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.findings import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.work import InvestigationUnit; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import Severity, VulnClass; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import norm_cwe, same_weakness; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/outcomes.py:28-31
In source order: Resolve source import from vvaharness.scope import resolve_inventory_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/outcomes.py:34-109
interface InvestigatedFinding {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:35-49
  In source order: For cwe, assign Field(description='Exactly one most-specific CWE id, e.g. CWE-89.'); source annotation str. Then For file, assign Field(description="Repo-relative path, from this threat's FILES list."); source annotation str. Then For line_start, assign Field(description=source_literal_37_40); source annotation int. Then For sink_line, assign Field(default=0, description=source_literal_40_50); source annotation int. Then For line_end, assign Field(default=0, description=source_literal_45_49); source annotation int.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:50-74
  In source order: For also_cwes, assign Field(default=[], description=source_literal_51_8); source annotation list[str]. Then For repeat_lines, assign Field(default=[], description=source_literal_59_8); source annotation list[int]. Then For preconditions, assign Field(default=[], description=source_literal_66_8); source annotation list[str].
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:78-80
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:76-77
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('sink_line', 'line_end', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:78-80
  // Source signature: _coerce_line(cls, v: object) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_line(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:79-79
    In source order: Retain source documentation literal source_literal_79_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:80-80
    End this invocation with _coerce_int(v, 0).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:84-90
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:82-83
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('repeat_lines', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:84-90
  // Source signature: _coerce_repeat_lines(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_repeat_lines(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:85-85
    In source order: Retain source documentation literal source_literal_85_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:86-87
    if (the source predicate v is None is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:87-87
      End this invocation with [].
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:88-89
    if (the source predicate isinstance(v, (list, tuple)) is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:89-89
      End this invocation with [_coerce_int(x, 0) for x in v].
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:90-90
    End this invocation with v.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:91-106
  In source order: For vuln_class, assign Field(description='Weakness class; unrecognized labels fold to OTHER.'); source annotation VulnClass. Then For title, assign Field(description='One line, at most 12 words, naming the weakness and its location. No prose.'); source annotation str. Then For severity, assign Field(description='One enum value. s6 re-scores every finding from a CVSS vector, so do not argue it here.'); source annotation Severity. Then For description, assign Field(description=source_literal_97_8); source annotation str. Then For exploit_scenario, assign Field(description=source_literal_101_8); source annotation str.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:107-109
  In source order: For recommendation, assign Field(description=source_literal_108_8); source annotation str.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:112-120
interface InvestigationOutcome {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:113-120
  In source order: For unit_id, assign Field(description='Echo the UNIT id you were given, verbatim.'); source annotation str. Then For verdict, assign Field(description=source_literal_115_8); source annotation Literal['confirmed', 'refuted', 'inconclusive']. Then For rationale, assign Field(description='Why, in 1-3 sentences. Required for refuted.'); source annotation str. Then For findings, assign Field(default=[], description=source_literal_119_8); source annotation list[InvestigatedFinding].
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:123-126
interface InvestigationOutcomes {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:124-126
  In source order: For outcomes, assign Field(description=source_literal_125_8); source annotation list[InvestigationOutcome].
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:129-133
// Source signature: _validate_direct(raw: str) -> InvestigationOutcome | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_direct(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:130-133
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:131-131
    End this invocation with InvestigationOutcome.model_validate_json(raw).
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:132-133
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:133-133
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:136-140
// Source signature: _validate_batch_direct(raw: str) -> InvestigationOutcomes | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_batch_direct(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:137-140
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:138-138
    End this invocation with InvestigationOutcomes.model_validate_json(raw).
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:139-140
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:140-140
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:143-147
// Source signature: _validate_batch_salvaged(raw: str) -> InvestigationOutcomes | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_batch_salvaged(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:144-147
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:145-145
    End this invocation with InvestigationOutcomes.model_validate(extract_json(raw)).
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:146-147
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:147-147
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:150-156
// Source signature: _as_batch(raw: str) -> InvestigationOutcomes | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _as_batch(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:151-152
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then Evaluate once _validate_batch_direct(raw) or _validate_batch_salvaged(raw); assign in source target order to batch.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:153-154
  if (the source predicate batch is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:154-154
    End this invocation with batch.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:155-155
  In source order: Evaluate once parse_outcome(raw); assign in source target order to lone.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:156-156
  End this invocation with InvestigationOutcomes(outcomes=[lone]) if lone is not None else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:159-174
// Source signature: split_batch_reply(raw: str, unit_ids: list[str]) -> dict[str, str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn split_batch_reply(raw, unit_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:160-161
  In source order: Retain source documentation literal source_literal_160_4; it is not a model call. Then Evaluate once _as_batch(raw); assign in source target order to batch.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:162-163
  if (the source predicate batch is None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:163-163
    End this invocation with {}.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:164-165
  In source order: Evaluate once set(unit_ids); assign in source target order to wanted. Then For by_unit, assign {}; source annotation dict[str, str | None].
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:166-170
  for each outcome in batch.outcomes {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:167-169
    if (the source predicate outcome.unit_id not in wanted is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:168-168
      In source order: Evaluate COUNTERS.bump('s4_batch_unit_id_invented'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:169-169
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:170-170
    In source order: Evaluate once outcome.model_dump_json(); assign in source target order to by_unit[outcome.unit_id].
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:171-171
  In source order: Evaluate once len(wanted) - len(by_unit); assign in source target order to absent.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:172-173
  if (the source predicate absent is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:173-173
    In source order: Evaluate COUNTERS.bump('s4_batch_unit_omitted', absent); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:174-174
  End this invocation with by_unit.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:177-181
// Source signature: _validate_salvaged(raw: str) -> InvestigationOutcome | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_salvaged(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:178-181
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:179-179
    End this invocation with InvestigationOutcome.model_validate(extract_json(raw)).
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:180-181
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:181-181
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:184-189
// Source signature: _bump_parse_failure(raw: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bump_parse_failure(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:185-185
  In source order: Evaluate once raw.strip(); assign in source target order to stripped.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:186-189
  if (the source predicate stripped and (not stripped.endswith('}')) is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:187-187
    In source order: Evaluate COUNTERS.bump('s4_outcome_truncated'); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:189-189
    In source order: Evaluate COUNTERS.bump('s4_outcome_malformed'); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:192-201
// Source signature: parse_outcome(raw: str) -> InvestigationOutcome | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_outcome(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:193-194
  In source order: Retain source documentation literal source_literal_193_4; it is not a model call. Then Evaluate once _validate_direct(raw); assign in source target order to outcome.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:195-196
  if (the source predicate outcome is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:196-196
    End this invocation with outcome.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:197-197
  In source order: Evaluate once _validate_salvaged(raw); assign in source target order to outcome.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:198-199
  if (the source predicate outcome is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:199-199
    End this invocation with outcome.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:200-200
  In source order: Evaluate _bump_parse_failure(raw); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:201-201
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:204-212
// Source signature: _resolved_cwe(f: InvestigatedFinding, fallback_cwes: list[str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolved_cwe(f, fallback_cwes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:205-206
  In source order: Retain source documentation literal source_literal_205_4; it is not a model call. Then Evaluate once norm_cwe(f.cwe); assign in source target order to cwe.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:207-208
  if (the source predicate cwe is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:208-208
    End this invocation with cwe.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:209-209
  In source order: Evaluate once fallback_cwes[0] if fallback_cwes else None; assign in source target order to cwe.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:210-211
  if (the source predicate cwe is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:211-211
    In source order: Evaluate COUNTERS.bump('s4_finding_cwe_backfilled'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:212-212
  End this invocation with cwe.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:215-225
// Source signature: _at_line(f: InvestigatedFinding, chunk_id: str, cwe: str | None, line_start: int, width: int, sink_ref: str | None) -> Finding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _at_line(f, chunk_id, cwe, line_start, width, sink_ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:217-217
  In source order: Retain source documentation literal source_literal_217_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:218-225
  End this invocation with Finding(title=f.title, file=f.file, line_start=line_start, line_end=line_start + width, vuln_class=f.vuln_class, severity=f.severity, cwe=cwe, description=f.description, exploit_scenario=f.exploit_scenario, recommendation=f.recommendation, preconditions=f.preconditions, chunk_id=chunk_id, sink_ref=sink_ref).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:228-245
// Source signature: _extra_cwes(f: InvestigatedFinding, primary: str | None, *, max_extra: int) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extra_cwes(f, primary, max_extra) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:229-231
  In source order: Retain source documentation literal source_literal_229_4; it is not a model call. Then For seen, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to collapsed.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:232-239
  for each raw in f.also_cwes {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:233-233
    In source order: Evaluate once norm_cwe(raw); assign in source target order to c.
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:234-235
    if (the source predicate not c or c == primary or c in seen is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:235-235
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:236-238
    if (the source predicate primary and same_weakness(primary, c) is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:237-237
      In source order: Apply source augmented assignment collapsed += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:238-238
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:239-239
    In source order: Evaluate seen.append(c); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:240-241
  if (the source predicate collapsed is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:241-241
    In source order: Evaluate COUNTERS.bump('s4_finding_extra_cwe_collapsed', collapsed); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:242-242
  In source order: Evaluate once max(max_extra, 0); assign in source target order to cap.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:243-244
  if (the source predicate len(seen) > cap is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:244-244
    In source order: Evaluate COUNTERS.bump('s4_finding_extra_cwes_capped', len(seen) - cap); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:245-245
  End this invocation with seen[:cap].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:248-271
// Source signature: fan_out(f: InvestigatedFinding, chunk_id: str, fallback_cwes: list[str] | None=None, cfg=None, *, repo_root: str, inventory: Collection[str]) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn fan_out(f, chunk_id, fallback_cwes, cfg, repo_root, inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:251-255
  In source order: Retain source documentation literal source_literal_251_4; it is not a model call. Then Evaluate once f.model_copy(update={'file': resolve_inventory_path(repo_root, f.file, inventory)}); assign in source target order to f. Then Evaluate once _resolved_cwe(f, fallback_cwes or []); assign in source target order to cwe. Then Evaluate once max(f.line_end, f.line_start) - f.line_start; assign in source target order to width. Then Evaluate once [f.line_start]; assign in source target order to anchors.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:256-259
  In source order: Apply source augmented assignment anchors += [n for n in sorted(set(f.repeat_lines)) if n > 0 and n != f.line_start] with source evaluation/in-place semantics. Then Evaluate once int(knob(cfg, 'step4.max_extra_cwes', 2)); assign in source target order to max_extra. Then Evaluate once [cwe, *_extra_cwes(f, cwe, max_extra=max_extra)]; assign in source target order to cwes.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:260-262
  if (the source predicate len(anchors) > 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:261-262
    In source order: Evaluate COUNTERS.bump('s4_finding_repeat_sites', len(anchors) - 1); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s4_finding_with_repeats'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:263-265
  if (the source predicate len(cwes) > 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:264-265
    In source order: Evaluate COUNTERS.bump('s4_finding_extra_cwes', len(cwes) - 1); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s4_finding_with_extra_cwes'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:267-267
  In source order: Evaluate once source_template_267_11 if f.sink_line >= 1 else None; assign in source target order to sink.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:268-269
  if (the source predicate sink is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:269-269
    In source order: Evaluate COUNTERS.bump('s4_finding_sink_line'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:270-271
  End this invocation with [_at_line(f, chunk_id, c, n, width, sink if n == f.line_start else None) for n in anchors for c in cwes].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/outcomes.py:274-300
// Source signature: reduce_outcomes(units: list[InvestigationUnit], raw_outcomes: dict[str, str | None], cfg=None, *, repo_root: str, inventory: Collection[str]) -> tuple[list[Finding], dict[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reduce_outcomes(units, raw_outcomes, cfg, repo_root, inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:278-281
  In source order: Retain source documentation literal source_literal_278_4; it is not a model call. Then Evaluate once {u.id: 'uninvestigated' for u in units}; assign in source target order to by_unit. Then Evaluate once {u.id: u for u in units}; assign in source target order to units_by_id. Then For findings, assign []; source annotation list[Finding].
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:282-296
  for each (unit_id, raw) in raw_outcomes.items() {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:283-285
    if (the source predicate unit_id not in by_unit is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:284-284
      In source order: Evaluate COUNTERS.bump('s4_unit_id_invented'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:285-285
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:286-287
    if (the source predicate raw is None is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:287-287
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:288-288
    In source order: Evaluate once parse_outcome(raw); assign in source target order to outcome.
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:289-291
    if (the source predicate outcome is None is truthy) {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:290-290
      In source order: Evaluate once 'failed'; assign in source target order to by_unit[unit_id].
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:291-291
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:292-293
    In source order: Evaluate once outcome.verdict; assign in source target order to by_unit[unit_id]. Then Evaluate once units_by_id[unit_id]; assign in source target order to unit.
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:294-296
    for each f in outcome.findings {
      // Source: vvaharness/pipeline/stages/s4/outcomes.py:295-296
      In source order: Evaluate findings.extend(fan_out(f, unit.id, unit.cwes, cfg, repo_root=repo_root, inventory=inventory)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:297-297
  In source order: Evaluate once sum((1 for v in by_unit.values() if v == 'uninvestigated')); assign in source target order to missing.
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:298-299
  if (the source predicate missing is truthy) {
    // Source: vvaharness/pipeline/stages/s4/outcomes.py:299-299
    In source order: Evaluate COUNTERS.bump('s4_unit_no_outcome', missing); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/outcomes.py:300-300
  End this invocation with (findings, by_unit).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan._coerce import _coerce_int` at source line 23: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.models.scan.findings import Finding` at source line 24: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.scan.work import InvestigationUnit` at source line 25: `source_detail/vvaharness/models/scan/work.py.sudo.md`.
- `from vvaharness.models.vocab import Severity, VulnClass` at source line 26: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.rules.cwe import norm_cwe, same_weakness` at source line 27: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
- `from vvaharness.scope import resolve_inventory_path` at source line 28: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 29: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 30: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 31: `source_detail/vvaharness/util/json_extract.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s4/outcomes.py.sudo.md). Exact strings in the evidence asset support this conversion.
