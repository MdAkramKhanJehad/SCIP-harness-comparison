# vvaharness/codegraph/handle.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/codegraph/handle.py.evidence.json`. SHA-256: `222296f76730f80e6069add638e94e218353c2f2b92e211a7d219d3327ffd84b`.

```sudo
// Source: vvaharness/codegraph/handle.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.api import Workspace; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.code_graph import CodeGraph; preserve alias and import-time effects.
// Source: vvaharness/codegraph/handle.py:23-25
In source order: Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/codegraph/handle.py:29-41
// Source: vvaharness/codegraph/handle.py:28-28
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/codegraph/handle.py:29-41
interface GraphHandle {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/codegraph/handle.py:30-35
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then For workspace, declare without assigning a value; source annotation Workspace. Then For graph, declare without assigning a value; source annotation CodeGraph. Then For project_id, declare without assigning a value; source annotation str. Then For node_count, assign None; source annotation int | None.
  // Source: vvaharness/codegraph/handle.py:36-37
  In source order: For edge_count, assign None; source annotation int | None. Then For enrichers, assign (); source annotation tuple[str, ...].
  // Source: vvaharness/codegraph/handle.py:39-41
  // Source signature: close(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn close(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/handle.py:40-41
    In source order: Retain source documentation literal source_literal_40_8; it is not a model call. Then Evaluate self.workspace.close(); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from context_graph_sdk.api import Workspace` at source line 20: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/api.py.sudo.md`.
- `from context_graph_sdk.code_graph import CodeGraph` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/code_graph.py.sudo.md`.
- `from vvaharness.util import logs` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 23: `source_detail/vvaharness/util/logs.py.sudo.md`.
