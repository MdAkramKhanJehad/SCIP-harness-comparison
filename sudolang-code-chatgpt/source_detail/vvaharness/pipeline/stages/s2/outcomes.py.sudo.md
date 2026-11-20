# vvaharness/pipeline/stages/s2/outcomes.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s2/outcomes.py.evidence.json`. SHA-256: `0b1e00bbe7c320eb3b36129a25dedb226e9a1394eaee1f98560ed1c4896ed61e`.

```sudo
// Source: vvaharness/pipeline/stages/s2/outcomes.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, ThreatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import resolve_inventory_path; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/outcomes.py:22-26
In source order: Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/outcomes.py:28-28
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/pipeline/stages/s2/outcomes.py:31-41
// Source signature: _parse_threat_model(raw: str) -> ThreatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_threat_model(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:32-33
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then Evaluate once extract_json(raw); assign in source target order to data.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:35-40
  if (the source predicate isinstance(data, dict) and data and (not data.keys() & ThreatModel.model_fields.keys()) is truthy) {
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:37-40
    Raise ValueError(source_template_38_12).
  }
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:41-41
  End this invocation with ThreatModel.model_validate(data).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/outcomes.py:42-70
// Source signature: _finalize_threats(tm: ThreatModel, ctx: ContextPackage | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _finalize_threats(tm, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:43-43
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:44-45
  for each (i, t) in enumerate(tm.threats, start=1) {
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:45-45
    In source order: Evaluate once source_template_45_15; assign in source target order to t.id.
  }
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:46-47
  if (the source predicate ctx is None or not tm.threats is truthy) {
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:47-47
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:48-50
  In source order: Evaluate once set(ctx.all_files); assign in source target order to valid. Then Evaluate once 0; assign in source target order to emitted. Then For dropped, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:51-55
  for each t in tm.threats {
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:52-55
    In source order: Evaluate once [(raw, resolve_inventory_path(ctx.repo_root, raw, valid)) for raw in t.surface_files]; assign in source target order to pairs. Then Evaluate once list(dict.fromkeys((rel for _, rel in pairs if rel in valid))); assign in source target order to t.surface_files. Then Apply source augmented assignment dropped += [raw for raw, rel in pairs if rel not in valid] with source evaluation/in-place semantics. Then Apply source augmented assignment emitted += len(pairs) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:56-57
  In source order: Evaluate console.write(source_template_56_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:58-59
  if (the source predicate not dropped is truthy) {
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:59-59
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:60-63
  In source order: Evaluate COUNTERS.bump('s2_surface_files_dropped', len(dropped)); retain side effects and discard the expression result. Then Evaluate once redact(', '.join(dropped))[:300]; assign in source target order to sample. Then Evaluate log.warning(Event.S2_SURFACE_FILES_DROPPED, dropped=len(dropped), sample=sample); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:64-70
  if (the source predicate len(dropped) == emitted is truthy) {
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:67-70
    In source order: Evaluate _errlog.log('s2', 'threatmodel', 'every surface_files path was rejected — no threat keeps a validated surface; s3 will mint no investigation unit', dropped=sample); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/outcomes.py:74-78
In source order: Evaluate once (('threats', 'max_threats', None), ('assets', 'max_assets', 's2_assets_truncated'), ('trust_boundaries', 'max_trust_boundaries', 's2_trust_boundaries_truncated')); assign in source target order to _OUTPUT_CAPS.
// Source: vvaharness/pipeline/stages/s2/outcomes.py:81-91
// Source signature: _warn_output_caps(raw: tuple[int, int, int], tm: ThreatModel, limits: tuple[int, int, int]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_output_caps(raw, tm, limits) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:83-84
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call. Then Evaluate once (len(tm.threats), len(tm.assets), len(tm.trust_boundaries)); assign in source target order to kept.
  // Source: vvaharness/pipeline/stages/s2/outcomes.py:85-91
  for each ((kind, key, counter), total, n, limit) in zip(_OUTPUT_CAPS, raw, kept, limits) {
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:86-87
    if (the source predicate n >= total is truthy) {
      // Source: vvaharness/pipeline/stages/s2/outcomes.py:87-87
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:88-89
    if (the source predicate counter is truthy) {
      // Source: vvaharness/pipeline/stages/s2/outcomes.py:89-89
      In source order: Evaluate COUNTERS.bump(counter, total - n); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s2/outcomes.py:90-91
    In source order: Evaluate log.warning(Event.S2_CAP_TRUNCATED, kind=kind, kept=n, total=total, excluded=total - n, cap=source_template_91_44, limit=limit); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import ContextPackage, ThreatModel` at source line 19: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 20: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.scope import resolve_inventory_path` at source line 21: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 22: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 22: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 23: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 24: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 25: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 26: `source_detail/vvaharness/util/json_extract.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s2/outcomes.py.sudo.md). Exact strings in the evidence asset support this conversion.
