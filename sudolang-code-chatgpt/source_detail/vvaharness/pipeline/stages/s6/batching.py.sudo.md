# vvaharness/pipeline/stages/s6/batching.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s6/batching.py.evidence.json`. SHA-256: `ab620bd0e447cf8db671ef302c381d7ac31a4f249c3547f9ea3a44257168176b`.

```sudo
// Source: vvaharness/pipeline/stages/s6/batching.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import ClockKind, TIMEOUT_STOP_GRACE_SECONDS, effort_scaled_seconds; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Evaluate once tuple[str, Finding]; assign in source target order to Item.
// Source: vvaharness/pipeline/stages/s6/batching.py:28-30
// Source signature: label(findings: list[Finding]) -> list[Item]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn label(findings) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/batching.py:29-29
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/batching.py:30-30
  End this invocation with [(source_template_30_13, f) for i, f in enumerate(findings)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/batching.py:33-38
// Source signature: plan_batches(items: list[Item], size: int) -> list[list[Item]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn plan_batches(items, size) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/batching.py:34-34
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/batching.py:35-36
  if (the source predicate size <= 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s6/batching.py:36-36
    End this invocation with [[item] for item in items].
  }
  // Source: vvaharness/pipeline/stages/s6/batching.py:37-37
  In source order: Evaluate once sorted(items, key=lambda it: it[1].file); assign in source target order to packed.
  // Source: vvaharness/pipeline/stages/s6/batching.py:38-38
  End this invocation with [packed[i:i + size] for i in range(0, len(packed), size)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/batching.py:41-47
// Source signature: ceiling_secs(s6) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn ceiling_secs(s6) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/batching.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/batching.py:44-47
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s6/batching.py:45-45
    End this invocation with max(0, int(getattr(s6, 'batch_wall_clock_ceiling', 900))).
  }
  // Source: vvaharness/pipeline/stages/s6/batching.py:46-47
  On the first matching source exception (TypeError, ValueError, OverflowError), in handler order {
    // Source: vvaharness/pipeline/stages/s6/batching.py:47-47
    End this invocation with 900.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/batching.py:50-52
// Source signature: sweep_effort(s6, *, via: str | None, cli_effort: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn sweep_effort(s6, via, cli_effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/batching.py:51-51
  In source order: Retain source documentation literal source_literal_51_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/batching.py:52-52
  End this invocation with getattr(s6, 'effort', None) or (cli_effort if via == 'cli' else None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/batching.py:55-62
// Source signature: sweep_ceiling_secs(s6, *, via: str | None, cli_effort: str | None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn sweep_ceiling_secs(s6, via, cli_effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/batching.py:56-57
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call. Then Evaluate once ceiling_secs(s6); assign in source target order to raw.
  // Source: vvaharness/pipeline/stages/s6/batching.py:58-59
  if (the source predicate raw == 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s6/batching.py:59-59
    End this invocation with 0.
  }
  // Source: vvaharness/pipeline/stages/s6/batching.py:60-61
  In source order: Evaluate once effort_scaled_seconds(raw, sweep_effort(s6, via=via, cli_effort=cli_effort), kind=ClockKind.SESSION); assign in source target order to scaled.
  // Source: vvaharness/pipeline/stages/s6/batching.py:62-62
  End this invocation with scaled + TIMEOUT_STOP_GRACE_SECONDS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/batching.py:65-70
// Source signature: filed_lines(items: list[Item]) -> dict[str, set[int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn filed_lines(items) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/batching.py:66-67
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call. Then For by_file, assign {}; source annotation dict[str, set[int]].
  // Source: vvaharness/pipeline/stages/s6/batching.py:68-69
  for each (_, f) in items {
    // Source: vvaharness/pipeline/stages/s6/batching.py:69-69
    In source order: Evaluate by_file.setdefault(f.file, set()).add(f.line_start); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/batching.py:70-70
  End this invocation with by_file.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.llm.models import ClockKind, TIMEOUT_STOP_GRACE_SECONDS, effort_scaled_seconds` at source line 18: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.models import Finding` at source line 23: `source_detail/vvaharness/models/__init__.py.sudo.md`.
