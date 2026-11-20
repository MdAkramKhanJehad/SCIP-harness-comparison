# vvaharness/orchestrator/store/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/store/__init__.py.evidence.json`. SHA-256: `38e5ad04d731345d5cf260d6700830d3241aeb1fb96d16a40a9ae744488ae753`.

```sudo
// Source: vvaharness/orchestrator/store/__init__.py:14-38
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store._db import _PERM_WARNED, _POSIX, _REPLAY_MAX_BYTES, _SCHEMA_VERSION, StoreError, _create_db_file_safe, connect, db_location, db_path, delete_run, delete_run_graphs, delete_steps, ensure_state_dir, register_run, run_exists, reset_run, state_root, steps_with_prefix; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store._schema import _DDL; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store.callgraph import load_callgraph, save_callgraph; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/store/__init__.py:39-76
In source order: Resolve source import from vvaharness.orchestrator.store.replays import delete_replays, load_ev_probes, load_replays, prune_replays, save_ev_probes, save_replays; preserve alias and import-time effects. Then Evaluate once ['_DDL', '_PERM_WARNED', '_POSIX', '_REPLAY_MAX_BYTES', '_SCHEMA_VERSION', 'StoreError', '_create_db_file_safe', 'connect', 'db_location', 'db_path', 'delete_replays', 'delete_run', 'delete_run_graphs', 'delete_steps', 'ensure_state_dir', 'load_callgraph', 'load_ev_probes', 'load_replays', 'prune_replays', 'register_run', 'run_exists', 'reset_run', 'save_callgraph', 'save_ev_probes', 'save_replays', 'state_root', 'steps_with_prefix']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.orchestrator.store._db import _PERM_WARNED, _POSIX, _REPLAY_MAX_BYTES, _SCHEMA_VERSION, StoreError, _create_db_file_safe, connect, db_location, db_path, delete_run, delete_run_graphs, delete_steps, ensure_state_dir, register_run, run_exists, reset_run, state_root, steps_with_prefix` at source line 17: `source_detail/vvaharness/orchestrator/store/_db.py.sudo.md`.
- `from vvaharness.orchestrator.store._schema import _DDL` at source line 37: `source_detail/vvaharness/orchestrator/store/_schema.py.sudo.md`.
- `from vvaharness.orchestrator.store.callgraph import load_callgraph, save_callgraph` at source line 38: `source_detail/vvaharness/orchestrator/store/callgraph.py.sudo.md`.
- `from vvaharness.orchestrator.store.replays import delete_replays, load_ev_probes, load_replays, prune_replays, save_ev_probes, save_replays` at source line 39: `source_detail/vvaharness/orchestrator/store/replays.py.sudo.md`.
