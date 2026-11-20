# vvaharness/codegraph/build.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/codegraph/build.py.evidence.json`. SHA-256: `f91eb2dc92b76cc882c2bdf6924b0619d8d683dd60fa95969d392345d21e6617`.

```sudo
// Source: vvaharness/codegraph/build.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.api import Workspace; preserve alias and import-time effects.
// Source: vvaharness/codegraph/build.py:22-27
In source order: Resolve source import from context_graph_sdk.backends.arcadedb import ArcadeDBBackendFactory; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.code_graph import CodeGraph; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.plugins import GraphEnricher; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.handle import GraphHandle; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
// Source: vvaharness/codegraph/build.py:28-31
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once 10; assign in source target order to _MIN_GRAPH_NODES_FOR_GATE.
// Source: vvaharness/codegraph/build.py:34-40
// Source signature: _analyze(workspace: Workspace, repo_root: str, project_id: str, enrichers: tuple[GraphEnricher, ...]) -> CodeGraph
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _analyze(workspace, repo_root, project_id, enrichers) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/build.py:36-40
  Perform the following protected operations {
    // Source: vvaharness/codegraph/build.py:37-37
    End this invocation with workspace.analyze(repo_root, project_id, enrichers).
  }
  // Source: vvaharness/codegraph/build.py:38-40
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/codegraph/build.py:39-39
    In source order: Evaluate workspace.close(); retain side effects and discard the expression result.
    // Source: vvaharness/codegraph/build.py:40-40
    Raise the currently handled exception.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/build.py:43-48
// Source signature: _enricher_names(plugins: tuple[object, ...]) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _enricher_names(plugins) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/build.py:44-44
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call.
  // Source: vvaharness/codegraph/build.py:45-48
  Perform the following protected operations {
    // Source: vvaharness/codegraph/build.py:46-46
    End this invocation with tuple((str(getattr(p.metadata, 'name', '?')) for p in plugins)).
  }
  // Source: vvaharness/codegraph/build.py:47-48
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/codegraph/build.py:48-48
    End this invocation with tuple(('?' for _ in plugins)).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/build.py:51-68
// Source signature: build_graph(repo_root: str, project_id: str, workspace_dir: Path, enrichers: Iterable[GraphEnricher]=()) -> GraphHandle
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_graph(repo_root, project_id, workspace_dir, enrichers) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/build.py:53-59
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once tuple(enrichers); assign in source target order to plugins. Then Evaluate once _enricher_names(plugins); assign in source target order to names. Then Evaluate once Workspace(workspace_dir, ArcadeDBBackendFactory()); assign in source target order to workspace. Then Evaluate once _analyze(workspace, repo_root, project_id, plugins); assign in source target order to graph.
  // Source: vvaharness/codegraph/build.py:60-61
  for each name in names {
    // Source: vvaharness/codegraph/build.py:61-61
    In source order: Evaluate COUNTERS.bump(source_template_61_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/codegraph/build.py:62-62
  In source order: Evaluate once graph.info(); assign in source target order to info.
  // Source: vvaharness/codegraph/build.py:63-68
  End this invocation with GraphHandle(workspace=workspace, graph=graph, project_id=project_id, node_count=info.node_count, edge_count=info.edge_count, enrichers=tuple(names)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/build.py:71-83
// Source signature: graph_is_degenerate(ctx: object, cfg: object=None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn graph_is_degenerate(ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/build.py:72-74
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once getattr(ctx, 'graph_handle', None); assign in source target order to handle.
  // Source: vvaharness/codegraph/build.py:75-76
  if (the source predicate handle is None is truthy) {
    // Source: vvaharness/codegraph/build.py:76-76
    End this invocation with True.
  }
  // Source: vvaharness/codegraph/build.py:77-78
  if (the source predicate getattr(handle, 'edge_count', None) == 0 is truthy) {
    // Source: vvaharness/codegraph/build.py:78-78
    End this invocation with True.
  }
  // Source: vvaharness/codegraph/build.py:79-79
  In source order: Evaluate once getattr(handle, 'node_count', None); assign in source target order to nodes.
  // Source: vvaharness/codegraph/build.py:80-81
  if (the source predicate nodes is None is truthy) {
    // Source: vvaharness/codegraph/build.py:81-81
    End this invocation with False.
  }
  // Source: vvaharness/codegraph/build.py:82-82
  In source order: Evaluate once int(knob(cfg, 'step0.min_graph_nodes_for_gate', _MIN_GRAPH_NODES_FOR_GATE)); assign in source target order to min_nodes.
  // Source: vvaharness/codegraph/build.py:83-83
  End this invocation with nodes < min_nodes.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.api import Workspace` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/api.py.sudo.md`.
- `from context_graph_sdk.backends.arcadedb import ArcadeDBBackendFactory` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py.sudo.md`.
- `from context_graph_sdk.code_graph import CodeGraph` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py.sudo.md`.
- `from context_graph_sdk.plugins import GraphEnricher` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/__init__.py.sudo.md`.
- `from vvaharness.codegraph.handle import GraphHandle` at source line 26: `source_detail/vvaharness/codegraph/handle.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 27: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 28: `source_detail/vvaharness/util/counters.py.sudo.md`.
