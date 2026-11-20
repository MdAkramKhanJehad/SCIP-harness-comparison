# vvaharness/pipeline/callgraph_consumer.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/callgraph_consumer.py.evidence.json`. SHA-256: `384ade7bb423a9256694d9c626c3030f30047ddfe6fa5272ec0572f05fada2f8`.

```sudo
// Source: vvaharness/pipeline/callgraph_consumer.py:15-34
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import weakref; preserve alias and import-time effects. Then Resolve source import from collections import defaultdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage; preserve alias and import-time effects.
// Source: vvaharness/pipeline/callgraph_consumer.py:37-38
// Source signature: _q_file(qn: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _q_file(qn) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:38-38
  End this invocation with qn.rpartition('::')[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:41-46
// Source signature: parse_hop(hop: str) -> tuple[str, int | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_hop(hop) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:42-43
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Evaluate once hop.rpartition(':'); assign in source target order to (file_part, sep, line_part).
  // Source: vvaharness/pipeline/callgraph_consumer.py:44-45
  if (the source predicate sep and file_part and line_part.isdigit() is truthy) {
    // Source: vvaharness/pipeline/callgraph_consumer.py:45-45
    End this invocation with (file_part, max(1, int(line_part))).
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:46-46
  End this invocation with (hop, None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:51-62
// Source signature: seed_paths_by_file(seed_taint_paths: list[list[str]] | None) -> dict[str, list[list[str]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn seed_paths_by_file(seed_taint_paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:52-53
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then For out, assign defaultdict(list); source annotation dict[str, list[list[str]]].
  // Source: vvaharness/pipeline/callgraph_consumer.py:54-61
  for each path in seed_taint_paths or () {
    // Source: vvaharness/pipeline/callgraph_consumer.py:55-55
    In source order: For touched, assign set(); source annotation set[str].
    // Source: vvaharness/pipeline/callgraph_consumer.py:56-59
    for each hop in path {
      // Source: vvaharness/pipeline/callgraph_consumer.py:57-57
      In source order: Evaluate once parse_hop(hop); assign in source target order to (f, _ln).
      // Source: vvaharness/pipeline/callgraph_consumer.py:58-59
      if (the source predicate f is truthy) {
        // Source: vvaharness/pipeline/callgraph_consumer.py:59-59
        In source order: Evaluate touched.add(f); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/pipeline/callgraph_consumer.py:60-61
    for each f in touched {
      // Source: vvaharness/pipeline/callgraph_consumer.py:61-61
      In source order: Evaluate out[f].append(path); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:62-62
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:65-76
// Source signature: best_source_from_seed(paths: list[list[str]]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn best_source_from_seed(paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:66-66
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call.
  // Source: vvaharness/pipeline/callgraph_consumer.py:67-75
  for each path in paths {
    // Source: vvaharness/pipeline/callgraph_consumer.py:68-69
    if (the source predicate not path is truthy) {
      // Source: vvaharness/pipeline/callgraph_consumer.py:69-69
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/callgraph_consumer.py:70-71
    In source order: Evaluate once path[0]; assign in source target order to src. Then Evaluate once parse_hop(src); assign in source target order to (sf, sl).
    // Source: vvaharness/pipeline/callgraph_consumer.py:72-73
    if (the source predicate sf and sl is not None is truthy) {
      // Source: vvaharness/pipeline/callgraph_consumer.py:73-73
      End this invocation with source_template_73_19.
    }
    // Source: vvaharness/pipeline/callgraph_consumer.py:74-75
    if (the source predicate src is truthy) {
      // Source: vvaharness/pipeline/callgraph_consumer.py:75-75
      End this invocation with src.
    }
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:76-76
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:79-82
// Source signature: entry_anchor_lines(ctx: ContextPackage) -> dict[str, list[int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn entry_anchor_lines(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:80-81
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call. Then Delete source targets in order: ctx.
  // Source: vvaharness/pipeline/callgraph_consumer.py:82-82
  End this invocation with {}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:85-94
// Source signature: graph_qnodes_by_file(ctx: ContextPackage) -> dict[str, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn graph_qnodes_by_file(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:86-88
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then For out, assign defaultdict(list); source annotation dict[str, list[str]]. Then For seen, assign defaultdict(set); source annotation dict[str, set[str]].
  // Source: vvaharness/pipeline/callgraph_consumer.py:89-93
  for each qn in getattr(ctx, 'call_graph', None) or {} {
    // Source: vvaharness/pipeline/callgraph_consumer.py:90-90
    In source order: Evaluate once _q_file(qn); assign in source target order to f.
    // Source: vvaharness/pipeline/callgraph_consumer.py:91-93
    if (the source predicate f and qn not in seen[f] is truthy) {
      // Source: vvaharness/pipeline/callgraph_consumer.py:92-93
      In source order: Evaluate out[f].append(qn); retain side effects and discard the expression result. Then Evaluate seen[f].add(qn); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:94-94
  End this invocation with dict(out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:97-105
// Source signature: qnodes_at(view: GraphView, file: str, line_start: int, line_end: int, *, limit: int=6) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn qnodes_at(view, file, line_start, line_end, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:99-102
  In source order: Retain source documentation literal source_literal_99_4; it is not a model call. Then Delete source targets in order: line_start, line_end. Then Evaluate once (file or '').replace('\\', '/'); assign in source target order to file. Then Evaluate once view.file_qnodes.get(file); assign in source target order to cg.
  // Source: vvaharness/pipeline/callgraph_consumer.py:103-104
  if (the source predicate cg is truthy) {
    // Source: vvaharness/pipeline/callgraph_consumer.py:104-104
    End this invocation with list(dict.fromkeys(cg))[:limit].
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:105-105
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:108-117
// Source signature: neighborhood(view: GraphView, qnodes, *, max_edges: int=8) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn neighborhood(view, qnodes, max_edges) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:109-111
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call. Then Evaluate once view.forward; assign in source target order to graph. Then For around, assign {}; source annotation dict[str, dict[str, list[str]]].
  // Source: vvaharness/pipeline/callgraph_consumer.py:112-116
  for each qn in qnodes {
    // Source: vvaharness/pipeline/callgraph_consumer.py:113-116
    In source order: Evaluate once {'callers': (view.rev.get(qn) or [])[:max_edges], 'callees': (graph.get(qn) or [])[:max_edges]}; assign in source target order to around[qn].
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:117-117
  End this invocation with around.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/callgraph_consumer.py:120-128
interface GraphView {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:121-123
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call. Then Evaluate once ('file_qnodes', 'forward', 'rev'); assign in source target order to __slots__.
  // Source: vvaharness/pipeline/callgraph_consumer.py:125-128
  // Source signature: __init__(self, ctx: ContextPackage) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, ctx) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/callgraph_consumer.py:126-128
    In source order: Evaluate once getattr(ctx, 'call_graph', None) or {}; assign in source target order to self.forward. Then Evaluate once graph_qnodes_by_file(ctx); assign in source target order to self.file_qnodes. Then For self.rev, assign {}; source annotation dict[str, list[str]].
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/pipeline/callgraph_consumer.py:132-132
In source order: For _VIEW_CACHE, assign {}; source annotation dict[int, tuple].
// Source: vvaharness/pipeline/callgraph_consumer.py:135-150
// Source signature: graph_view(ctx: ContextPackage) -> GraphView
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn graph_view(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/callgraph_consumer.py:136-138
  In source order: Retain source documentation literal source_literal_136_4; it is not a model call. Then Evaluate once id(ctx); assign in source target order to key. Then Evaluate once _VIEW_CACHE.get(key); assign in source target order to entry.
  // Source: vvaharness/pipeline/callgraph_consumer.py:139-142
  if (the source predicate entry is not None is truthy) {
    // Source: vvaharness/pipeline/callgraph_consumer.py:140-140
    In source order: Evaluate once entry; assign in source target order to (ref, view).
    // Source: vvaharness/pipeline/callgraph_consumer.py:141-142
    if (the source predicate ref() is ctx is truthy) {
      // Source: vvaharness/pipeline/callgraph_consumer.py:142-142
      End this invocation with view.
    }
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:143-143
  In source order: Evaluate once GraphView(ctx); assign in source target order to view.
  // Source: vvaharness/pipeline/callgraph_consumer.py:144-148
  Perform the following protected operations {
    // Source: vvaharness/pipeline/callgraph_consumer.py:145-145
    In source order: Evaluate once weakref.ref(ctx); assign in source target order to ref.
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:146-148
  On the first matching source exception TypeError, in handler order {
    // Source: vvaharness/pipeline/callgraph_consumer.py:147-148
    // Source signature: ref(_c=ctx)
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn ref(_c) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/pipeline/callgraph_consumer.py:148-148
      End this invocation with _c.
      If execution reaches this end, finish with the source implicit None result.
    }
  }
  // Source: vvaharness/pipeline/callgraph_consumer.py:149-149
  In source order: Evaluate once (ref, view); assign in source target order to _VIEW_CACHE[key].
  // Source: vvaharness/pipeline/callgraph_consumer.py:150-150
  End this invocation with view.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import ContextPackage` at source line 34: `source_detail/vvaharness/models/__init__.py.sudo.md`.
