# vvaharness/orchestrator/store/replays.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/store/replays.py.evidence.json`. SHA-256: `446460330ce8f360bdd204ef146aa441b08c225942226b3f2a9e0bd9360b691b`.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:14-20
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import sqlite3; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store._db import _REPLAY_MAX_BYTES, connect; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/store/replays.py:21-23
In source order: Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/store/replays.py:26-49
// Source signature: save_replays(run_id: str, items: list[tuple[str, bytes]]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn save_replays(run_id, items) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/replays.py:27-30
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con. Then Evaluate once 0; assign in source target order to written.
  // Source: vvaharness/orchestrator/store/replays.py:31-48
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/replays.py:32-46
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/replays.py:33-37
      In source order: Evaluate con.execute("INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')", (run_id,)); retain side effects and discard the expression result. Then Evaluate con.execute("UPDATE runs SET updated_at = datetime('now') WHERE run_id = ?", (run_id,)); retain side effects and discard the expression result. Then Evaluate con.execute('DELETE FROM ev_replays WHERE run_id = ?', (run_id,)); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/store/replays.py:38-46
      for each (key, blob) in items {
        // Source: vvaharness/orchestrator/store/replays.py:39-42
        if (the source predicate len(blob) > _REPLAY_MAX_BYTES is truthy) {
          // Source: vvaharness/orchestrator/store/replays.py:40-41
          In source order: Evaluate log.warning(Event.REPLAY_TOO_LARGE, key=key[:12], size=len(blob), cap=_REPLAY_MAX_BYTES); retain side effects and discard the expression result.
          // Source: vvaharness/orchestrator/store/replays.py:42-42
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/orchestrator/store/replays.py:43-46
        In source order: Evaluate con.execute('INSERT OR REPLACE INTO ev_replays(run_id, finding_key, payload, size) VALUES (?, ?, ?, ?)', (run_id, key, blob, len(blob))); retain side effects and discard the expression result. Then Apply source augmented assignment written += 1 with source evaluation/in-place semantics.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/replays.py:48-48
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/replays.py:49-49
  End this invocation with written.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/replays.py:52-68
// Source signature: prune_replays(run_id: str, keep_keys) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prune_replays(run_id, keep_keys) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/replays.py:53-57
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once set(keep_keys or ()); assign in source target order to keep. Then For stale, assign []; source annotation list[str]. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/replays.py:58-67
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/replays.py:59-65
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/replays.py:60-62
      In source order: Evaluate once con.execute('SELECT finding_key FROM ev_replays WHERE run_id = ?', (run_id,)).fetchall(); assign in source target order to rows. Then Evaluate once [r[0] for r in rows if r[0] not in keep]; assign in source target order to stale.
      // Source: vvaharness/orchestrator/store/replays.py:63-65
      for each key in stale {
        // Source: vvaharness/orchestrator/store/replays.py:64-65
        In source order: Evaluate con.execute('DELETE FROM ev_replays WHERE run_id = ? AND finding_key = ?', (run_id, key)); retain side effects and discard the expression result.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/replays.py:67-67
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/replays.py:68-68
  End this invocation with len(stale).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/replays.py:71-86
// Source signature: load_replays(run_id: str) -> list[tuple[str, bytes]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_replays(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/replays.py:72-73
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/replays.py:74-79
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/replays.py:75-77
    In source order: Evaluate once con.execute('SELECT finding_key, payload, size FROM ev_replays WHERE run_id = ? ORDER BY created_at, finding_key', (run_id,)).fetchall(); assign in source target order to rows.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/replays.py:79-79
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/replays.py:80-80
  In source order: For out, assign []; source annotation list[tuple[str, bytes]].
  // Source: vvaharness/orchestrator/store/replays.py:81-85
  for each (key, payload, size) in rows {
    // Source: vvaharness/orchestrator/store/replays.py:82-84
    if (the source predicate size > _REPLAY_MAX_BYTES is truthy) {
      // Source: vvaharness/orchestrator/store/replays.py:83-83
      In source order: Evaluate log.warning(Event.REPLAY_STORED_TOO_LARGE, key=key[:12], cap=_REPLAY_MAX_BYTES); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/store/replays.py:84-84
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/store/replays.py:85-85
    In source order: Evaluate out.append((key, payload)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/replays.py:86-86
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/replays.py:89-97
// Source signature: delete_replays(run_id: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn delete_replays(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/replays.py:90-91
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/replays.py:92-97
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/replays.py:93-95
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/replays.py:94-94
      In source order: Evaluate once con.execute('DELETE FROM ev_replays WHERE run_id = ?', (run_id,)); assign in source target order to cur.
      // Source: vvaharness/orchestrator/store/replays.py:95-95
      End this invocation with cur.rowcount or 0.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/replays.py:97-97
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/replays.py:101-105
In source order: Evaluate once ('finding_key', 'finding_title', 'file', 'line_start', 'line_end', 'cwe', 'vuln_class', 'ev_class', 'ev_subtype', 'ev_verdict', 'endpoint_method', 'endpoint_path', 'payload_label', 'injection_point', 'req_method', 'req_url', 'req_query', 'req_body', 'authed', 'auth_applied', 'resp_status', 'resp_ms', 'resp_snippet'); assign in source target order to _EV_PROBE_COLS.
// Source: vvaharness/orchestrator/store/replays.py:108-129
// Source signature: save_ev_probes(run_id: str, rows: list[dict]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn save_ev_probes(run_id, rows) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/replays.py:109-114
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call. Then Evaluate once ', '.join(_EV_PROBE_COLS); assign in source target order to cols. Then Evaluate once ', '.join(('?' for _ in _EV_PROBE_COLS)); assign in source target order to ph. Then Evaluate once connect(); assign in source target order to con. Then Evaluate once 0; assign in source target order to written.
  // Source: vvaharness/orchestrator/store/replays.py:115-128
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/replays.py:116-126
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/replays.py:117-121
      In source order: Evaluate con.execute("INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')", (run_id,)); retain side effects and discard the expression result. Then Evaluate con.execute("UPDATE runs SET updated_at = datetime('now') WHERE run_id = ?", (run_id,)); retain side effects and discard the expression result. Then Evaluate con.execute('DELETE FROM ev_probes WHERE run_id = ?', (run_id,)); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/store/replays.py:122-126
      for each r in rows {
        // Source: vvaharness/orchestrator/store/replays.py:123-126
        In source order: Evaluate con.execute(source_template_124_20, (run_id, *(r.get(c) for c in _EV_PROBE_COLS))); retain side effects and discard the expression result. Then Apply source augmented assignment written += 1 with source evaluation/in-place semantics.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/replays.py:128-128
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/replays.py:129-129
  End this invocation with written.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/replays.py:132-142
// Source signature: load_ev_probes(run_id: str) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_ev_probes(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/replays.py:133-134
  In source order: Retain source documentation literal source_literal_133_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/replays.py:135-142
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/replays.py:136-139
    In source order: Evaluate once sqlite3.Row; assign in source target order to con.row_factory. Then Evaluate once con.execute(source_template_138_12, (run_id,)); assign in source target order to cur.
    // Source: vvaharness/orchestrator/store/replays.py:140-140
    End this invocation with [dict(row) for row in cur.fetchall()].
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/replays.py:142-142
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 16: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 16: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.orchestrator.store._db import _REPLAY_MAX_BYTES, connect` at source line 20: `source_detail/vvaharness/orchestrator/store/_db.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 21: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/orchestrator/store/replays.py.sudo.md). Exact strings in the evidence asset support this conversion.
