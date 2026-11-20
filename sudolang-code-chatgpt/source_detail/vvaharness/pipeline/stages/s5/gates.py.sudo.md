# vvaharness/pipeline/stages/s5/gates.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s5/gates.py.evidence.json`. SHA-256: `429083c6d399907807fedddbfec5f7fdf6ad8bd4bc882490b142f1efa84ed2fb`.

```sudo
// Source: vvaharness/pipeline/stages/s5/gates.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s5.rules import EXCLUDE_PATH_RE, is_secret_class; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/gates.py:23-29
// Source signature: reject_path(f: Finding, valid_files: set[str] | None) -> tuple[str, str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reject_path(f, valid_files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/gates.py:24-24
  In source order: Retain source documentation literal source_literal_24_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/gates.py:25-26
  if (the source predicate EXCLUDE_PATH_RE.search(f.file) and (not is_secret_class(f)) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/gates.py:26-26
    End this invocation with ('EXCLUDED', 'test/mock/example path').
  }
  // Source: vvaharness/pipeline/stages/s5/gates.py:27-28
  if (the source predicate valid_files is not None and f.file not in valid_files is truthy) {
    // Source: vvaharness/pipeline/stages/s5/gates.py:28-28
    End this invocation with ('EXCLUDED', 'file not in repo inventory').
  }
  // Source: vvaharness/pipeline/stages/s5/gates.py:29-29
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/gates.py:32-47
// Source signature: reject(f: Finding, valid_files: set[str] | None, lines: list[str] | None) -> tuple[str, str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reject(f, valid_files, lines) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/gates.py:34-35
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call. Then Evaluate once reject_path(f, valid_files); assign in source target order to verdict.
  // Source: vvaharness/pipeline/stages/s5/gates.py:36-37
  if (the source predicate verdict is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s5/gates.py:37-37
    End this invocation with verdict.
  }
  // Source: vvaharness/pipeline/stages/s5/gates.py:38-39
  if (the source predicate lines is None is truthy) {
    // Source: vvaharness/pipeline/stages/s5/gates.py:39-39
    End this invocation with ('EXCLUDED', 'file could not be read from the repo').
  }
  // Source: vvaharness/pipeline/stages/s5/gates.py:40-40
  In source order: Evaluate once int(f.line_start or 0); assign in source target order to line.
  // Source: vvaharness/pipeline/stages/s5/gates.py:41-42
  if (the source predicate not 1 <= line <= len(lines) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/gates.py:42-42
    End this invocation with ('EXCLUDED', source_template_42_27).
  }
  // Source: vvaharness/pipeline/stages/s5/gates.py:44-46
  if (the source predicate f.line_end > len(lines) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/gates.py:45-46
    In source order: Evaluate once len(lines); assign in source target order to f.line_end. Then Evaluate COUNTERS.bump('s5_line_end_clamped_eof'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s5/gates.py:47-47
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Finding` at source line 18: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s5.rules import EXCLUDE_PATH_RE, is_secret_class` at source line 19: `source_detail/vvaharness/pipeline/stages/s5/rules.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 20: `source_detail/vvaharness/util/counters.py.sudo.md`.
