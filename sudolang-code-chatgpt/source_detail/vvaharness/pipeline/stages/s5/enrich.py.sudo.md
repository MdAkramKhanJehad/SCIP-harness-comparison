# vvaharness/pipeline/stages/s5/enrich.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s5/enrich.py.evidence.json`. SHA-256: `c7e510507836d330700a789a5dc3ddfd659c7651832165b2b16d01a2e9fdd551`.

```sudo
// Source: vvaharness/pipeline/stages/s5/enrich.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import stat; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.matcher import split_lines; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s5/enrich.py:22-27
In source order: Resolve source import from vvaharness.models import Finding, VulnClass; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.callgraph_consumer import best_source_from_seed; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once 40; assign in source target order to MAX_SNIPPET_LINES.
// Source: vvaharness/pipeline/stages/s5/enrich.py:30-38
// Source signature: _read_lines(path: Path | None) -> list[str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_lines(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:31-31
  In source order: Retain source documentation literal source_literal_31_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:32-33
  if (the source predicate path is None is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:33-33
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:34-38
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:35-35
    End this invocation with split_lines(path.read_text(errors='replace')).
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:37-38
  On the first matching source exception (OSError, ValueError, MemoryError), in handler order {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:38-38
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/enrich.py:41-73
interface FileCache {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:44-48
  // Source signature: __init__(self, repo_root: str | Path, max_kb: int=1024)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, repo_root, max_kb) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:45-48
    In source order: Evaluate once Path(repo_root); assign in source target order to self.root. Then Evaluate once self.root.resolve(); assign in source target order to self._resolved_root. Then Evaluate once max(1, int(max_kb)) * 1024; assign in source target order to self._max_bytes. Then For self._lines, assign {}; source annotation dict[str, list[str] | None].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:50-62
  // Source signature: _safe_path(self, rel: str) -> Path | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _safe_path(self, rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:51-51
    In source order: Retain source documentation literal source_literal_51_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:52-62
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s5/enrich.py:53-54
      if (the source predicate Path(rel).is_absolute() is truthy) {
        // Source: vvaharness/pipeline/stages/s5/enrich.py:54-54
        End this invocation with None.
      }
      // Source: vvaharness/pipeline/stages/s5/enrich.py:55-57
      In source order: Evaluate once (self.root / rel).resolve(); assign in source target order to target. Then Evaluate target.relative_to(self._resolved_root); retain side effects and discard the expression result. Then Evaluate once target.stat(); assign in source target order to st.
      // Source: vvaharness/pipeline/stages/s5/enrich.py:58-59
      if (the source predicate not stat.S_ISREG(st.st_mode) or st.st_size > self._max_bytes is truthy) {
        // Source: vvaharness/pipeline/stages/s5/enrich.py:59-59
        End this invocation with None.
      }
      // Source: vvaharness/pipeline/stages/s5/enrich.py:60-60
      End this invocation with target.
    }
    // Source: vvaharness/pipeline/stages/s5/enrich.py:61-62
    On the first matching source exception (OSError, ValueError, RuntimeError), in handler order {
      // Source: vvaharness/pipeline/stages/s5/enrich.py:62-62
      End this invocation with None.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:64-68
  // Source signature: lines(self, rel: str) -> list[str] | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn lines(self, rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:65-65
    In source order: Retain source documentation literal source_literal_65_8; it is not a model call.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:66-67
    if (the source predicate rel not in self._lines is truthy) {
      // Source: vvaharness/pipeline/stages/s5/enrich.py:67-67
      In source order: Evaluate once _read_lines(self._safe_path(rel)); assign in source target order to self._lines[rel].
    }
    // Source: vvaharness/pipeline/stages/s5/enrich.py:68-68
    End this invocation with self._lines[rel].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:70-73
  // Source signature: line_count(self, rel: str) -> int | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn line_count(self, rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:71-72
    In source order: Retain source documentation literal source_literal_71_8; it is not a model call. Then Evaluate once self.lines(rel); assign in source target order to lines.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:73-73
    End this invocation with None if lines is None else len(lines).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/pipeline/stages/s5/enrich.py:76-84
// Source signature: snippet(f: Finding, lines: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn snippet(f, lines) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:77-78
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once max(1, int(f.line_start)); assign in source target order to start.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:79-80
  if (the source predicate start > len(lines) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:80-80
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:81-83
  In source order: Evaluate once max(start, int(f.line_end or start)); assign in source target order to want. Then Evaluate once min(want, start + MAX_SNIPPET_LINES - 1, len(lines)); assign in source target order to end. Then Evaluate once source_literal_83_11.join(lines[start - 1:end]); assign in source target order to body.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:84-84
  End this invocation with source_template_84_11 if want > end else body.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/enrich.py:87-89
// Source signature: _sink_ref(f: Finding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sink_ref(f) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:88-88
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:89-89
  End this invocation with (f.sink_ref or '').strip() or source_template_89_41.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/enrich.py:92-103
// Source signature: _origin_ref(f: Finding, sink: str, anchors: dict[str, list[int]], seeds: dict[str, list[list[str]]]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _origin_ref(f, sink, anchors, seeds) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:94-95
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call. Then Evaluate once (f.source_ref or '').strip(); assign in source target order to own.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:96-97
  if (the source predicate own is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:97-97
    End this invocation with own.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:98-99
  if (the source predicate f.vuln_class == VulnClass.INFO_LEAK is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:99-99
    End this invocation with sink.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:100-100
  In source order: Evaluate once anchors.get(f.file) or (); assign in source target order to near.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:101-102
  if (the source predicate near is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:102-102
    End this invocation with source_template_102_15.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:103-103
  End this invocation with best_source_from_seed(seeds.get(f.file, ())) or ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/enrich.py:106-119
// Source signature: refs(f: Finding, anchors: dict[str, list[int]], seeds: dict[str, list[list[str]]]) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn refs(f, anchors, seeds) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:108-113
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call. Then Evaluate once _sink_ref(f); assign in source target order to sink. Then Evaluate once _origin_ref(f, sink, anchors, seeds); assign in source target order to origin. Then Evaluate once [name for name, own in (('sink_ref', f.sink_ref), ('source_ref', f.source_ref)) if not (own or '').strip()]; assign in source target order to empty. Then Evaluate once {'sink_ref': sink or None, 'source_ref': origin or None}; assign in source target order to new.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:115-115
  In source order: Evaluate once [name for name in empty if new[name]]; assign in source target order to filled.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:116-117
  if (the source predicate not filled is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:117-117
    End this invocation with {}.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:118-119
  End this invocation with {**{name: new[name] for name in empty}, 'backfilled_refs': sorted(set(f.backfilled_refs) | set(filled))}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s5/enrich.py:122-137
// Source signature: enrich(f: Finding, cache: FileCache, anchors: dict[str, list[int]], seeds: dict[str, list[list[str]]], reanchorer=None) -> Finding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn enrich(f, cache, anchors, seeds, reanchorer) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:124-124
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:125-126
  if (the source predicate reanchorer is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:126-126
    In source order: Evaluate once reanchorer.apply(f); assign in source target order to f.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:127-128
  In source order: For update, assign {}; source annotation dict. Then Evaluate once cache.lines(f.file); assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:129-133
  if (the source predicate lines is not None and (not f.code_snippet.strip()) is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:130-130
    In source order: Evaluate once snippet(f, lines); assign in source target order to body.
    // Source: vvaharness/pipeline/stages/s5/enrich.py:131-133
    if (the source predicate body is truthy) {
      // Source: vvaharness/pipeline/stages/s5/enrich.py:132-133
      In source order: Evaluate once body; assign in source target order to update['code_snippet']. Then Evaluate COUNTERS.bump('s5_snippet_filled'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:134-134
  In source order: Evaluate update.update(refs(f, anchors, seeds)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s5/enrich.py:135-136
  if (the source predicate 'backfilled_refs' in update is truthy) {
    // Source: vvaharness/pipeline/stages/s5/enrich.py:136-136
    In source order: Evaluate COUNTERS.bump('s5_refs_backfilled'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s5/enrich.py:137-137
  End this invocation with f.model_copy(update=update) if update else f.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.detect.matcher import split_lines` at source line 21: `source_detail/vvaharness/detect/matcher.py.sudo.md`.
- `from vvaharness.models import Finding, VulnClass` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.callgraph_consumer import best_source_from_seed` at source line 23: `source_detail/vvaharness/pipeline/callgraph_consumer.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 24: `source_detail/vvaharness/util/counters.py.sudo.md`.
