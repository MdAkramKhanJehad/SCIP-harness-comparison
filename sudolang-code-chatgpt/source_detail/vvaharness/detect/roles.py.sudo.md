# vvaharness/detect/roles.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/detect/roles.py.evidence.json`. SHA-256: `3ab52eb110b58e889ce8e4404123895cf104b16d7703a8d41d6fbecad1fcca15`.

```sudo
// Source: vvaharness/detect/roles.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Literal, get_args; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.matcher import Hit; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.surface import EntryPoint, Sink; preserve alias and import-time effects.
// Source: vvaharness/detect/roles.py:23-24
In source order: Evaluate once Literal['network', 'ipc', 'file', 'cli', 'deserialization', 'framework', 'other']; assign in source target order to _EPKind. Then For _EP_KINDS, assign frozenset(get_args(_EPKind)); source annotation frozenset[str].
// Source: vvaharness/detect/roles.py:27-28
// Source signature: _sink_function(hit: Hit) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sink_function(hit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/roles.py:28-28
  End this invocation with hit.spec.rule_id.rsplit('-', 1)[-1].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/roles.py:31-50
// Source signature: hits_to_sinks(hits: list[Hit]) -> list[Sink]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn hits_to_sinks(hits) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/roles.py:32-34
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then For seen, assign set(); source annotation set[tuple[str, int, str]]. Then For sinks, assign []; source annotation list[Sink].
  // Source: vvaharness/detect/roles.py:35-49
  for each hit in hits {
    // Source: vvaharness/detect/roles.py:36-37
    if (the source predicate hit.spec.role != 'sink' is truthy) {
      // Source: vvaharness/detect/roles.py:37-37
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/detect/roles.py:38-39
    In source order: Evaluate once _sink_function(hit); assign in source target order to function. Then Evaluate once (hit.file, hit.line, function); assign in source target order to key.
    // Source: vvaharness/detect/roles.py:40-41
    if (the source predicate key in seen is truthy) {
      // Source: vvaharness/detect/roles.py:41-41
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/detect/roles.py:42-49
    In source order: Evaluate seen.add(key); retain side effects and discard the expression result. Then Evaluate sinks.append(Sink(file=hit.file, line=hit.line, function=function, snippet=hit.snippet, cwe=[hit.spec.cwe])); retain side effects and discard the expression result.
  }
  // Source: vvaharness/detect/roles.py:50-50
  End this invocation with sinks.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/roles.py:53-70
// Source signature: hits_to_entry_points(hits: list[Hit]) -> list[EntryPoint]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn hits_to_entry_points(hits) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/roles.py:54-56
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call. Then For seen, assign set(); source annotation set[tuple[str, str]]. Then For entry_points, assign []; source annotation list[EntryPoint].
  // Source: vvaharness/detect/roles.py:57-69
  for each hit in hits {
    // Source: vvaharness/detect/roles.py:58-59
    if (the source predicate hit.spec.role != 'source' is truthy) {
      // Source: vvaharness/detect/roles.py:59-59
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/detect/roles.py:60-61
    In source order: For kind, assign hit.spec.kind if hit.spec.kind in _EP_KINDS else 'other'; source annotation _EPKind. Then Evaluate once (hit.file, kind); assign in source target order to key.
    // Source: vvaharness/detect/roles.py:62-63
    if (the source predicate key in seen is truthy) {
      // Source: vvaharness/detect/roles.py:63-63
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/detect/roles.py:64-69
    In source order: Evaluate seen.add(key); retain side effects and discard the expression result. Then Evaluate entry_points.append(EntryPoint(file=hit.file, function=hit.snippet, kind=kind)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/detect/roles.py:70-70
  End this invocation with entry_points.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.detect.matcher import Hit` at source line 20: `source_detail/vvaharness/detect/matcher.py.sudo.md`.
- `from vvaharness.models.scan.surface import EntryPoint, Sink` at source line 21: `source_detail/vvaharness/models/scan/surface.py.sudo.md`.
