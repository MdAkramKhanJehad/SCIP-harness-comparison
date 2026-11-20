# vvaharness/orchestrator/store/callgraph.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/store/callgraph.py.evidence.json`. SHA-256: `095d4fe821c649e698d8c48bd2dfa854c25330d61262c91eba22c51783923934`.

```sudo
// Source: vvaharness/orchestrator/store/callgraph.py:14-20
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store._db import connect; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/store/callgraph.py:23-26
// Source signature: _qnode(file_path: str, function_name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _qnode(file_path, function_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/callgraph.py:24-25
  In source order: Evaluate once (file_path or '').replace('\\', '/'); assign in source target order to file_part. Then Evaluate once function_name or ''; assign in source target order to fn_part.
  // Source: vvaharness/orchestrator/store/callgraph.py:26-26
  End this invocation with source_template_26_11 if file_part or fn_part else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/callgraph.py:29-34
// Source signature: _split_qnode(qnode: str) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _split_qnode(qnode) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/callgraph.py:31-32
  if (the source predicate '::' not in qnode is truthy) {
    // Source: vvaharness/orchestrator/store/callgraph.py:32-32
    End this invocation with ('', qnode).
  }
  // Source: vvaharness/orchestrator/store/callgraph.py:33-33
  In source order: Evaluate once qnode.rpartition('::'); assign in source target order to (f, _, n).
  // Source: vvaharness/orchestrator/store/callgraph.py:34-34
  End this invocation with (f, n).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/callgraph.py:37-77
// Source signature: _graph_rows(obj) -> list[dict] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _graph_rows(obj) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/callgraph.py:38-40
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then Evaluate once list(getattr(obj, 'entry_points', ()) or ()); assign in source target order to entry_points. Then Evaluate once list(getattr(obj, 'unsafe_sinks', ()) or ()); assign in source target order to unsafe_sinks.
  // Source: vvaharness/orchestrator/store/callgraph.py:41-42
  if (the source predicate not (entry_points or unsafe_sinks) is truthy) {
    // Source: vvaharness/orchestrator/store/callgraph.py:42-42
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/store/callgraph.py:44-44
  In source order: For entry_meta, assign {}; source annotation dict[str, tuple[str, int]].
  // Source: vvaharness/orchestrator/store/callgraph.py:45-51
  for each ep in entry_points {
    // Source: vvaharness/orchestrator/store/callgraph.py:46-46
    In source order: Evaluate once _qnode(getattr(ep, 'file', ''), getattr(ep, 'function', '')); assign in source target order to qn.
    // Source: vvaharness/orchestrator/store/callgraph.py:47-51
    if (the source predicate qn is truthy) {
      // Source: vvaharness/orchestrator/store/callgraph.py:48-51
      In source order: Evaluate once (getattr(ep, 'kind', '') or '', 1 if bool(getattr(ep, 'reachable_from_unauth', False)) else 0); assign in source target order to entry_meta[qn].
    }
  }
  // Source: vvaharness/orchestrator/store/callgraph.py:53-53
  In source order: For sink_meta, assign {}; source annotation dict[str, int].
  // Source: vvaharness/orchestrator/store/callgraph.py:54-59
  for each sink in unsafe_sinks {
    // Source: vvaharness/orchestrator/store/callgraph.py:55-55
    In source order: Evaluate once _qnode(getattr(sink, 'file', ''), getattr(sink, 'function', '')); assign in source target order to qn.
    // Source: vvaharness/orchestrator/store/callgraph.py:56-59
    if (the source predicate qn is truthy) {
      // Source: vvaharness/orchestrator/store/callgraph.py:57-59
      In source order: Evaluate once int(getattr(sink, 'line', 0) or 0); assign in source target order to line. Then Evaluate once sink_meta.get(qn); assign in source target order to prev. Then Evaluate once line if prev is None or (line and line < prev) else prev; assign in source target order to sink_meta[qn].
    }
  }
  // Source: vvaharness/orchestrator/store/callgraph.py:61-61
  In source order: For node_rows, assign []; source annotation list[dict].
  // Source: vvaharness/orchestrator/store/callgraph.py:62-75
  for each qn in sorted(set(entry_meta) | set(sink_meta)) {
    // Source: vvaharness/orchestrator/store/callgraph.py:63-75
    In source order: Evaluate once _split_qnode(qn); assign in source target order to (file_path, function_name). Then Evaluate once entry_meta.get(qn, ('', 0)); assign in source target order to (entry_kind, unauth). Then Evaluate once sink_meta.get(qn, 0); assign in source target order to sink_line. Then Evaluate node_rows.append({'qnode': qn, 'file_path': file_path, 'function_name': function_name, 'is_entry_point': 1 if qn in entry_meta else 0, 'entry_kind': entry_kind, 'reachable_from_unauth': unauth, 'is_sink': 1 if qn in sink_meta else 0, 'sink_line': sink_line}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/callgraph.py:77-77
  End this invocation with node_rows.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/callgraph.py:80-139
// Source signature: save_callgraph(run_id: str, step: str, obj) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn save_callgraph(run_id, step, obj) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/callgraph.py:81-82
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call. Then Evaluate once _graph_rows(obj); assign in source target order to node_rows.
  // Source: vvaharness/orchestrator/store/callgraph.py:83-84
  if (the source predicate node_rows is None is truthy) {
    // Source: vvaharness/orchestrator/store/callgraph.py:84-84
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/store/callgraph.py:85-90
  In source order: Evaluate once json.dumps({'nodes': node_rows}, sort_keys=True, separators=(',', ':')).encode(); assign in source target order to payload. Then Evaluate once hashlib.sha256(payload).hexdigest()[:32]; assign in source target order to graph_id. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/callgraph.py:91-139
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/callgraph.py:92-136
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/callgraph.py:93-100
      In source order: Evaluate con.execute("INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')", (run_id,)); retain side effects and discard the expression result. Then Evaluate con.execute("UPDATE runs SET updated_at = datetime('now') WHERE run_id = ?", (run_id,)); retain side effects and discard the expression result. Then Evaluate once con.execute('SELECT 1 FROM callgraph_snapshots WHERE run_id=? AND graph_id=?', (run_id, graph_id)).fetchone(); assign in source target order to exists.
      // Source: vvaharness/orchestrator/store/callgraph.py:101-132
      if (the source predicate exists is None is truthy) {
        // Source: vvaharness/orchestrator/store/callgraph.py:102-132
        In source order: Evaluate con.execute(source_literal_103_20, (run_id, graph_id, len(node_rows), 0, sum((r['is_entry_point'] for r in node_rows)), sum((r['is_sink'] for r in node_rows)))); retain side effects and discard the expression result. Then Evaluate con.executemany(source_literal_116_20, [(run_id, graph_id, row['qnode'], row['file_path'], row['function_name'], row['is_entry_point'], row['entry_kind'], row['reachable_from_unauth'], row['is_sink'], row['sink_line']) for row in node_rows]); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/store/callgraph.py:133-136
      In source order: Evaluate con.execute('INSERT OR REPLACE INTO callgraph_stage_refs(run_id, step, graph_id) VALUES (?, ?, ?)', (run_id, step, graph_id)); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/orchestrator/store/callgraph.py:137-137
    End this invocation with graph_id.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/callgraph.py:139-139
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/callgraph.py:142-164
// Source signature: load_callgraph(run_id: str, step: str) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_callgraph(run_id, step) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/callgraph.py:143-144
  In source order: Retain source documentation literal source_literal_143_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/callgraph.py:145-158
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/callgraph.py:146-149
    In source order: Evaluate once con.execute('SELECT graph_id FROM callgraph_stage_refs WHERE run_id=? AND step=?', (run_id, step)).fetchone(); assign in source target order to ref.
    // Source: vvaharness/orchestrator/store/callgraph.py:150-151
    if (the source predicate ref is None is truthy) {
      // Source: vvaharness/orchestrator/store/callgraph.py:151-151
      End this invocation with None.
    }
    // Source: vvaharness/orchestrator/store/callgraph.py:152-156
    In source order: Evaluate once ref[0]; assign in source target order to graph_id. Then Evaluate once con.execute('SELECT qnode FROM callgraph_nodes WHERE run_id=? AND graph_id=?', (run_id, graph_id)).fetchall(); assign in source target order to node_rows.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/callgraph.py:158-158
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/callgraph.py:160-164
  End this invocation with {'graph_id': graph_id, 'call_graph': {qn: [] for qn, in node_rows}, 'node_count': len(node_rows)}.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.orchestrator.store._db import connect` at source line 20: `source_detail/vvaharness/orchestrator/store/_db.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/orchestrator/store/callgraph.py.sudo.md). Exact strings in the evidence asset support this conversion.
