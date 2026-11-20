# scripts/inspect_units.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/scripts/inspect_units.py.evidence.json`. SHA-256: `5dcd1493182cd8b06c4fc522f0a8b83905ff010e7a1352f411349a92cfb69ebf`.

```sudo
// Source: scripts/inspect_units.py:15-31
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import argparse; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: scripts/inspect_units.py:32-39
In source order: Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from collections import deque; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import import vvaharness.models as models; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import load_ckpt, run_id_for; preserve alias and import-time effects.
// Source: scripts/inspect_units.py:40-40
In source order: Resolve source import from vvaharness.orchestrator import store; preserve alias and import-time effects.
// Source: scripts/inspect_units.py:43-49
// Source signature: _avail_runs() -> list[tuple[str, str | None]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _avail_runs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: scripts/inspect_units.py:44-44
  In source order: Evaluate once store.connect(); assign in source target order to con.
  // Source: scripts/inspect_units.py:45-49
  Perform the following protected operations {
    // Source: scripts/inspect_units.py:46-47
    End this invocation with list(con.execute('SELECT run_id, repo_root FROM runs ORDER BY updated_at DESC')).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: scripts/inspect_units.py:49-49
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: scripts/inspect_units.py:52-56
// Source signature: _count_loc(p: Path) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _count_loc(p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: scripts/inspect_units.py:53-56
  Perform the following protected operations {
    // Source: scripts/inspect_units.py:54-54
    End this invocation with sum((1 for _ in p.open('r', encoding='utf-8', errors='replace'))).
  }
  // Source: scripts/inspect_units.py:55-56
  On the first matching source exception OSError, in handler order {
    // Source: scripts/inspect_units.py:56-56
    End this invocation with 0.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: scripts/inspect_units.py:59-60
// Source signature: _fmt(n: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fmt(n) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: scripts/inspect_units.py:60-60
  End this invocation with source_template_60_11 if n >= 1000 else str(n).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: scripts/inspect_units.py:63-79
// Source signature: _bfs_reaches(start: str, graph: dict, sinks: set[str], max_hops: int) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bfs_reaches(start, graph, sinks, max_hops) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: scripts/inspect_units.py:64-65
  if (the source predicate not start is truthy) {
    // Source: scripts/inspect_units.py:65-65
    End this invocation with set().
  }
  // Source: scripts/inspect_units.py:66-68
  In source order: For hit, assign set(); source annotation set[str]. Then Evaluate once {start}; assign in source target order to seen. Then Evaluate once deque([(start, 0)]); assign in source target order to q.
  // Source: scripts/inspect_units.py:69-78
  while (the source predicate q is truthy) {
    // Source: scripts/inspect_units.py:70-70
    In source order: Evaluate once q.popleft(); assign in source target order to (node, d).
    // Source: scripts/inspect_units.py:71-78
    for each nx in graph.get(node, ()) {
      // Source: scripts/inspect_units.py:72-73
      if (the source predicate nx in seen is truthy) {
        // Source: scripts/inspect_units.py:73-73
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: scripts/inspect_units.py:74-74
      In source order: Evaluate seen.add(nx); retain side effects and discard the expression result.
      // Source: scripts/inspect_units.py:75-76
      if (the source predicate nx in sinks is truthy) {
        // Source: scripts/inspect_units.py:76-76
        In source order: Evaluate hit.add(nx); retain side effects and discard the expression result.
      }
      // Source: scripts/inspect_units.py:77-78
      if (the source predicate d + 1 < max_hops is truthy) {
        // Source: scripts/inspect_units.py:78-78
        In source order: Evaluate q.append((nx, d + 1)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: scripts/inspect_units.py:79-79
  End this invocation with hit.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: scripts/inspect_units.py:82-272
// Source signature: main() -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn main() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: scripts/inspect_units.py:83-91
  In source order: Evaluate once argparse.ArgumentParser(description=__doc__); assign in source target order to ap. Then Evaluate ap.add_argument('--repo', required=True, help='target repo that was scanned'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--run-id', help='explicit run id; default = derived from --repo path (must match the absolute path the scan ran against)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--state-dir', help='state root containing vvaharness.db; default = $VVAHARNESS_STATE_DIR or ~/.vvaharness/state'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--file', help='show which unit(s) contain this file'); retain side effects and discard the expression result.
  // Source: scripts/inspect_units.py:92-98
  In source order: Evaluate ap.add_argument('--json', nargs='?', const='-', help='dump TaskManifest as JSON (to path, or stdout if bare)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--max-hops', type=int, default=12, help='BFS depth for orphaned-sink check'); retain side effects and discard the expression result. Then Evaluate once ap.parse_args(); assign in source target order to args. Then Evaluate once Path(args.repo).resolve(); assign in source target order to repo.
  // Source: scripts/inspect_units.py:99-100
  if (the source predicate args.state_dir is truthy) {
    // Source: scripts/inspect_units.py:100-100
    In source order: Evaluate once args.state_dir; assign in source target order to os.environ['VVAHARNESS_STATE_DIR'].
  }
  // Source: scripts/inspect_units.py:101-105
  In source order: Evaluate once args.run_id or run_id_for(repo); assign in source target order to run_id. Then Evaluate once load_ckpt(None, run_id, 's1'); assign in source target order to ctx. Then Evaluate once load_ckpt(None, run_id, 's2'); assign in source target order to tm. Then Evaluate once load_ckpt(None, run_id, 's3'); assign in source target order to manifest.
  // Source: scripts/inspect_units.py:106-117
  if (the source predicate ctx is None or manifest is None is truthy) {
    // Source: scripts/inspect_units.py:107-116
    In source order: Evaluate once _avail_runs(); assign in source target order to avail. Then Evaluate once source_literal_108_19.join((source_template_108_33 for r, root in avail)) if avail else '<none>'; assign in source target order to listing. Then Evaluate print(source_template_110_14 + listing, file=sys.stderr); retain side effects and discard the expression result.
    // Source: scripts/inspect_units.py:117-117
    End this invocation with 1.
  }
  // Source: scripts/inspect_units.py:119-125
  In source order: Evaluate print(source_template_119_10); retain side effects and discard the expression result. Then Evaluate print(source_template_120_10); retain side effects and discard the expression result. Then Evaluate print(source_template_121_10); retain side effects and discard the expression result. Then Evaluate once ctx.call_graph or {}; assign in source target order to cg. Then Evaluate once sum((len(v) for v in cg.values())); assign in source target order to n_edges.
  // Source: scripts/inspect_units.py:126-131
  In source order: Evaluate print('## s1 ContextPackage'); retain side effects and discard the expression result. Then Evaluate print(source_template_127_10); retain side effects and discard the expression result. Then Evaluate print(source_template_128_10); retain side effects and discard the expression result. Then Evaluate print(source_template_129_10); retain side effects and discard the expression result. Then Evaluate print(source_template_130_10); retain side effects and discard the expression result.
  // Source: scripts/inspect_units.py:132-134
  In source order: Evaluate print(source_template_132_10); retain side effects and discard the expression result. Then Evaluate print(source_template_133_10); retain side effects and discard the expression result.
  // Source: scripts/inspect_units.py:135-137
  if (the source predicate tm is truthy) {
    // Source: scripts/inspect_units.py:136-137
    In source order: Evaluate print(source_template_136_14); retain side effects and discard the expression result.
  }
  // Source: scripts/inspect_units.py:138-143
  In source order: Evaluate print(); retain side effects and discard the expression result. Then Evaluate once {s.function for s in ctx.unsafe_sinks if s.function}; assign in source target order to sink_fns. Then Evaluate once {e.file for e in ctx.entry_points}; assign in source target order to entry_files. Then For reached, assign set(); source annotation set[str].
  // Source: scripts/inspect_units.py:144-145
  for each ep in ctx.entry_points {
    // Source: scripts/inspect_units.py:145-145
    In source order: Apply source augmented assignment reached |= _bfs_reaches(ep.function, cg, sink_fns, args.max_hops) with source evaluation/in-place semantics.
  }
  // Source: scripts/inspect_units.py:146-152
  In source order: Evaluate once [s for s in ctx.unsafe_sinks if s.function not in reached and s.file not in entry_files]; assign in source target order to orphans. Then Evaluate once len(ctx.unsafe_sinks); assign in source target order to ns. Then Evaluate print('## Taint reachability'); retain side effects and discard the expression result. Then Evaluate print(source_template_150_10); retain side effects and discard the expression result.
  // Source: scripts/inspect_units.py:153-156
  if (the source predicate orphans is truthy) {
    // Source: scripts/inspect_units.py:154-154
    In source order: Evaluate print(source_template_154_14); retain side effects and discard the expression result.
    // Source: scripts/inspect_units.py:155-156
    for each s in orphans {
      // Source: scripts/inspect_units.py:156-156
      In source order: Evaluate print(source_template_156_18); retain side effects and discard the expression result.
    }
  }
  // Source: scripts/inspect_units.py:157-170
  In source order: Evaluate print(); retain side effects and discard the expression result. Then Evaluate once Path(ctx.repo_root); assign in source target order to scan_root. Then Evaluate once repo; assign in source target order to loc_root. Then Evaluate once [f for u in manifest.sorted_units() for f in u.files][:25]; assign in source target order to probe_files. Then Evaluate once sum((1 for f in probe_files if (repo / f).exists())); assign in source target order to live_hits.
  // Source: scripts/inspect_units.py:171-171
  In source order: Evaluate once sum((1 for f in probe_files if (scan_root / f).exists())); assign in source target order to scan_hits.
  // Source: scripts/inspect_units.py:172-180
  if (the source predicate probe_files and live_hits == 0 and (scan_hits > 0) is truthy) {
    // Source: scripts/inspect_units.py:173-176
    In source order: Evaluate once scan_root; assign in source target order to loc_root. Then Evaluate print(source_template_174_14, file=sys.stderr); retain side effects and discard the expression result.
  }
  else {
    // Source: scripts/inspect_units.py:177-180
    if (the source predicate probe_files and live_hits == 0 and (scan_hits == 0) is truthy) {
      // Source: scripts/inspect_units.py:178-180
      In source order: Evaluate print(source_template_178_14, file=sys.stderr); retain side effects and discard the expression result.
    }
  }
  // Source: scripts/inspect_units.py:181-183
  In source order: Evaluate once loc_root; assign in source target order to repo_root. Then Evaluate once manifest.sorted_units(); assign in source target order to units. Then For rows, assign []; source annotation list[tuple].
  // Source: scripts/inspect_units.py:184-186
  for each u in units {
    // Source: scripts/inspect_units.py:185-186
    In source order: Evaluate once sum((_count_loc(repo_root / f) for f in u.files)); assign in source target order to loc. Then Evaluate rows.append((u, loc)); retain side effects and discard the expression result.
  }
  // Source: scripts/inspect_units.py:188-191
  In source order: Evaluate print(source_template_188_10); retain side effects and discard the expression result. Then Evaluate print(source_template_189_10); retain side effects and discard the expression result. Then Evaluate print(source_template_191_10); retain side effects and discard the expression result.
  // Source: scripts/inspect_units.py:192-196
  for each (u, loc) in rows {
    // Source: scripts/inspect_units.py:193-196
    In source order: Evaluate once ','.join(u.languages[:3]) or '-'; assign in source target order to langs. Then Evaluate once (u.threat or '').replace(source_literal_194_42, ' '); assign in source target order to threat. Then Evaluate print(source_template_195_14); retain side effects and discard the expression result.
  }
  // Source: scripts/inspect_units.py:197-200
  In source order: Evaluate print(); retain side effects and discard the expression result. Then Evaluate once sorted((loc for _, loc in rows)); assign in source target order to locs.
  // Source: scripts/inspect_units.py:201-211
  if (the source predicate locs is truthy) {
    // Source: scripts/inspect_units.py:202-207
    In source order: Evaluate once len(locs); assign in source target order to n. Then Evaluate print('## Unit LOC distribution'); retain side effects and discard the expression result. Then Evaluate print(source_template_204_14); retain side effects and discard the expression result. Then Evaluate once [(u.id, loc) for u, loc in rows if loc > 10000]; assign in source target order to big.
    // Source: scripts/inspect_units.py:208-210
    if (the source predicate big is truthy) {
      // Source: scripts/inspect_units.py:209-210
      In source order: Evaluate print(source_template_209_18 + ', '.join((source_template_210_30 for uid, l in big))); retain side effects and discard the expression result.
    }
    // Source: scripts/inspect_units.py:211-211
    In source order: Evaluate print(); retain side effects and discard the expression result.
  }
  // Source: scripts/inspect_units.py:216-227
  if (the source predicate tm and tm.threats is truthy) {
    // Source: scripts/inspect_units.py:217-221
    In source order: Evaluate once {u.id for u in units}; assign in source target order to covered. Then Evaluate once [t.id for t in tm.threats]; assign in source target order to ids. Then Evaluate once [t for t in ids if t not in covered]; assign in source target order to missing. Then Evaluate print('## Threat coverage'); retain side effects and discard the expression result. Then Evaluate print(source_template_221_14); retain side effects and discard the expression result.
    // Source: scripts/inspect_units.py:222-226
    if (the source predicate missing is truthy) {
      // Source: scripts/inspect_units.py:223-223
      In source order: Evaluate once {t.id: t for t in tm.threats}; assign in source target order to by_id.
      // Source: scripts/inspect_units.py:224-226
      for each tid in missing {
        // Source: scripts/inspect_units.py:225-226
        In source order: Evaluate once by_id[tid]; assign in source target order to t. Then Evaluate print(source_template_226_22); retain side effects and discard the expression result.
      }
    }
    // Source: scripts/inspect_units.py:227-227
    In source order: Evaluate print(); retain side effects and discard the expression result.
  }
  // Source: scripts/inspect_units.py:230-244
  if (the source predicate args.file is truthy) {
    // Source: scripts/inspect_units.py:231-235
    In source order: Evaluate once args.file.replace('\\', '/'); assign in source target order to needle. Then Evaluate once [u for u in units if any((needle == f or needle in f or f.endswith('/' + needle) for f in u.files))]; assign in source target order to hits. Then Evaluate print(source_template_235_14); retain side effects and discard the expression result.
    // Source: scripts/inspect_units.py:236-243
    if (the source predicate not hits is truthy) {
      // Source: scripts/inspect_units.py:237-240
      In source order: Evaluate once any((needle == f or f.endswith('/' + needle) for f in ctx.all_files)); assign in source target order to in_scope. Then Evaluate print(source_template_239_18); retain side effects and discard the expression result.
    }
    else {
      // Source: scripts/inspect_units.py:242-243
      for each u in hits {
        // Source: scripts/inspect_units.py:243-243
        In source order: Evaluate print(source_template_243_22); retain side effects and discard the expression result.
      }
    }
    // Source: scripts/inspect_units.py:244-244
    In source order: Evaluate print(); retain side effects and discard the expression result.
  }
  // Source: scripts/inspect_units.py:247-270
  if (the source predicate args.json is truthy) {
    // Source: scripts/inspect_units.py:248-265
    In source order: Evaluate once {'context': {'language': ctx.language, 'files_in_scope': len(ctx.all_files), 'entry_points': [e.model_dump() for e in ctx.entry_points], 'unsafe_sinks': [s.model_dump() for s in ctx.unsafe_sinks], 'call_graph_nodes': len(cg), 'call_graph_edges': n_edges}, 'orphaned_sinks': [{'file': s.file, 'line': s.line, 'function': s.function} for s in orphans], 'units': [dict(u.model_dump(), loc=loc) for u, loc in rows]}; assign in source target order to payload. Then Evaluate once json.dumps(payload, indent=2); assign in source target order to out.
    // Source: scripts/inspect_units.py:266-270
    if (the source predicate args.json == '-' is truthy) {
      // Source: scripts/inspect_units.py:267-267
      In source order: Evaluate print(out); retain side effects and discard the expression result.
    }
    else {
      // Source: scripts/inspect_units.py:269-270
      In source order: Evaluate Path(args.json).write_text(out, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate print(source_template_270_18); retain side effects and discard the expression result.
    }
  }
  // Source: scripts/inspect_units.py:272-272
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: scripts/inspect_units.py:275-276
if (the source predicate __name__ == '__main__' is truthy) {
  // Source: scripts/inspect_units.py:276-276
  Raise SystemExit(main()).
}
```

## Local import links

- `import vvaharness.models as models` at source line 36: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import load_ckpt, run_id_for` at source line 39: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 40: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 40: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../prompt_representation/scripts/inspect_units.py.sudo.md). Exact strings in the evidence asset support this conversion.
