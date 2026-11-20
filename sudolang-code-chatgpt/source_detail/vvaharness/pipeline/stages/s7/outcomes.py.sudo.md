# vvaharness/pipeline/stages/s7/outcomes.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s7/outcomes.py.evidence.json`. SHA-256: `0f1150a3815342cc3062e2708b8b455c1c1b939a6966f875492ae9e39a0b5c68`.

```sudo
// Source: vvaharness/pipeline/stages/s7/outcomes.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, field_validator; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._coerce import flag as _coerce_bool; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s7/outcomes.py:23-27
In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s7/outcomes.py:29-29
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/pipeline/stages/s7/outcomes.py:32-52
interface DedupDecision {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:33-46
  In source order: For index, assign Field(description='Echo the FINDING index you were given, verbatim.'); source annotation int. Then For duplicate_of, assign Field(description=source_literal_35_8); source annotation int. Then For reasoning, assign Field(description=source_literal_39_8); source annotation str. Then For independent_sites, assign Field(default=False, description=source_literal_43_8); source annotation bool.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:50-52
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:48-49
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('independent_sites', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:50-52
  // Source signature: _coerce_flag(cls, v: object) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_flag(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:51-51
    In source order: Retain source documentation literal source_literal_51_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:52-52
    End this invocation with _coerce_bool(v).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/pipeline/stages/s7/outcomes.py:55-58
interface DedupDecisions {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:56-58
  In source order: For decisions, assign Field(description=source_literal_57_8); source annotation list[DedupDecision].
}
// Source: vvaharness/pipeline/stages/s7/outcomes.py:61-70
// Source signature: _decisions(raw: str) -> DedupDecisions | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _decisions(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:62-62
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:63-66
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:64-64
    End this invocation with DedupDecisions.model_validate_json(raw).
  }
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:65-66
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:66-66
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:67-70
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:68-68
    End this invocation with DedupDecisions.model_validate(extract_json(raw)).
  }
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:69-70
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:70-70
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s7/outcomes.py:73-95
// Source signature: parse_decisions(raw: str, n: int, label: str='s7-dedup') -> list[tuple[int, int, str, bool]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_decisions(raw, n, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:75-76
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once _decisions(raw); assign in source target order to parsed.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:77-86
  if (the source predicate parsed is None is truthy) {
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:78-85
    if (the source predicate raw.strip() is truthy) {
      // Source: vvaharness/pipeline/stages/s7/outcomes.py:80-85
      In source order: Evaluate COUNTERS.bump('s7_dedup_parse_miss'); retain side effects and discard the expression result. Then Evaluate once redact(raw)[:500].replace(source_literal_82_45, '\\n'); assign in source target order to head. Then Evaluate log.warning(Event.S7_DEDUP_UNPARSEABLE, stage=label, findings=n, raw_head=head); retain side effects and discard the expression result. Then Evaluate _errlog.log(label, 'semantic-parse', source_template_85_24, raw_head=head); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:86-86
    End this invocation with [].
  }
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:87-87
  In source order: For out, assign []; source annotation list[tuple[int, int, str, bool]].
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:88-91
  for each d in parsed.decisions {
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:89-91
    if (the source predicate 0 <= d.duplicate_of < d.index < n is truthy) {
      // Source: vvaharness/pipeline/stages/s7/outcomes.py:90-91
      In source order: Evaluate out.append((d.index, d.duplicate_of, d.reasoning.strip(), d.independent_sites)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:92-92
  In source order: Evaluate once n - len(parsed.decisions); assign in source target order to absent.
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:93-94
  if (the source predicate absent > 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s7/outcomes.py:94-94
    In source order: Evaluate COUNTERS.bump('s7_dedup_index_omitted', absent); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s7/outcomes.py:95-95
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan._coerce import flag as _coerce_bool` at source line 21: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 22: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 23: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 25: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 26: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 27: `source_detail/vvaharness/util/json_extract.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s7/outcomes.py.sudo.md). Exact strings in the evidence asset support this conversion.
