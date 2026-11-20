# vvaharness/orchestrator/store/_db.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/store/_db.py.evidence.json`. SHA-256: `6a4a94f470099d6a028341fc05ac90db00b17d83da6a962cd8838f6a9d413c01`.

```sudo
// Source: vvaharness/orchestrator/store/_db.py:14-19
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import sqlite3; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/store/_db.py:20-25
In source order: Resolve source import import stat; preserve alias and import-time effects. Then Resolve source import from collections.abc import Collection; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store._schema import _DDL, _DDL_V2, _DDL_V3; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/store/_db.py:27-35
In source order: Evaluate once 3; assign in source target order to _SCHEMA_VERSION. Then Evaluate once 1024 * 1024; assign in source target order to _REPLAY_MAX_BYTES. Then Evaluate once 384; assign in source target order to _DB_FILE_MODE. Then Evaluate once 448; assign in source target order to _STATE_DIR_MODE. Then Evaluate once ('-wal', '-shm', '-journal'); assign in source target order to _SIDECAR_SUFFIXES.
// Source: vvaharness/orchestrator/store/_db.py:37-38
In source order: Evaluate once os.name == 'posix'; assign in source target order to _POSIX. Then For _PERM_WARNED, assign set(); source annotation set[str].
// Source: vvaharness/orchestrator/store/_db.py:41-43
// Source signature: _warn_once(key: str, message: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_once(key, message) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:42-43
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then Evaluate warn_once(_PERM_WARNED, key, source_template_43_33); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:46-62
// Source signature: _tighten_mode(path: Path, mode: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tighten_mode(path, mode) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:47-47
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call.
  // Source: vvaharness/orchestrator/store/_db.py:49-50
  if (the source predicate not _POSIX is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:50-50
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/store/_db.py:51-54
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:52-52
    In source order: Evaluate once stat.S_IMODE(path.stat().st_mode); assign in source target order to current.
  }
  // Source: vvaharness/orchestrator/store/_db.py:53-54
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/orchestrator/store/_db.py:54-54
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/store/_db.py:55-56
  if (the source predicate not current & ~mode is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:56-56
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/store/_db.py:57-62
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:58-58
    In source order: Evaluate os.chmod(path, mode); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/_db.py:59-62
  On the first matching source exception OSError as e, in handler order {
    // Source: vvaharness/orchestrator/store/_db.py:60-62
    In source order: Evaluate _warn_once(str(path), source_template_61_19); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:65-66
interface StoreError {
  Describe the source Python type, preserving its base/metaclass expression order: RuntimeError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/store/_db.py:66-66
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call.
}
// Source: vvaharness/orchestrator/store/_db.py:69-73
// Source signature: state_root() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn state_root() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:70-70
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call.
  // Source: vvaharness/orchestrator/store/_db.py:72-73
  End this invocation with Path(os.environ.get('VVAHARNESS_STATE_DIR') or Path.home() / '.vvaharness' / 'state').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:76-125
// Source signature: ensure_state_dir(*parts: str) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn ensure_state_dir(parts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:77-79
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then Evaluate once state_root(); assign in source target order to root.
  // Source: vvaharness/orchestrator/store/_db.py:80-88
  if (the source predicate _POSIX is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:82-85
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/store/_db.py:83-83
      In source order: Evaluate once root.lstat(); assign in source target order to lst.
    }
    // Source: vvaharness/orchestrator/store/_db.py:84-85
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/orchestrator/store/_db.py:85-85
      In source order: Evaluate once None; assign in source target order to lst.
    }
    // Source: vvaharness/orchestrator/store/_db.py:86-88
    if (the source predicate lst is not None and stat.S_ISLNK(lst.st_mode) is truthy) {
      // Source: vvaharness/orchestrator/store/_db.py:87-88
      Raise StoreError(source_template_88_16).
    }
  }
  // Source: vvaharness/orchestrator/store/_db.py:89-119
  if (the source predicate root.is_dir() is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:91-109
    if (the source predicate _POSIX is truthy) {
      // Source: vvaharness/orchestrator/store/_db.py:92-95
      Perform the following protected operations {
        // Source: vvaharness/orchestrator/store/_db.py:93-93
        In source order: Evaluate once stat.S_IMODE(root.stat().st_mode); assign in source target order to mode.
      }
      // Source: vvaharness/orchestrator/store/_db.py:94-95
      On the first matching source exception OSError, in handler order {
        // Source: vvaharness/orchestrator/store/_db.py:95-95
        In source order: Evaluate once 0; assign in source target order to mode.
      }
      // Source: vvaharness/orchestrator/store/_db.py:96-109
      if (the source predicate mode & 63 is truthy) {
        // Source: vvaharness/orchestrator/store/_db.py:97-109
        if (the source predicate os.environ.get('VVAHARNESS_STATE_DIR') is truthy) {
          // Source: vvaharness/orchestrator/store/_db.py:98-102
          In source order: Evaluate _warn_once(str(root), source_template_100_24); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/orchestrator/store/_db.py:104-109
          In source order: Evaluate _tighten_mode(root, _STATE_DIR_MODE); retain side effects and discard the expression result. Then Evaluate _warn_once(str(root), source_template_107_24); retain side effects and discard the expression result.
        }
      }
    }
  }
  else {
    // Source: vvaharness/orchestrator/store/_db.py:111-117
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/store/_db.py:112-112
      In source order: Evaluate root.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/store/_db.py:113-117
    On the first matching source exception FileExistsError as e, in handler order {
      // Source: vvaharness/orchestrator/store/_db.py:115-117
      Raise StoreError(source_template_116_16) with explicit source cause e.
    }
    // Source: vvaharness/orchestrator/store/_db.py:119-119
    In source order: Evaluate _tighten_mode(root, _STATE_DIR_MODE); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/_db.py:120-120
  In source order: Evaluate once root; assign in source target order to path.
  // Source: vvaharness/orchestrator/store/_db.py:121-124
  for each part in parts {
    // Source: vvaharness/orchestrator/store/_db.py:122-124
    In source order: Evaluate once path / part; assign in source target order to path. Then Evaluate path.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate _tighten_mode(path, _STATE_DIR_MODE); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/_db.py:125-125
  End this invocation with path.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:129-129
In source order: Evaluate once 'vvaharness.db'; assign in source target order to _DB_NAME.
// Source: vvaharness/orchestrator/store/_db.py:132-135
// Source signature: db_location() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn db_location() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:133-133
  In source order: Retain source documentation literal source_literal_133_4; it is not a model call.
  // Source: vvaharness/orchestrator/store/_db.py:135-135
  End this invocation with state_root() / _DB_NAME.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:138-155
// Source signature: run_exists(run_id: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_exists(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:139-140
  In source order: Retain source documentation literal source_literal_139_4; it is not a model call. Then Evaluate once db_location(); assign in source target order to path.
  // Source: vvaharness/orchestrator/store/_db.py:141-155
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:142-144
    for each candidate in (state_root(), path) {
      // Source: vvaharness/orchestrator/store/_db.py:143-144
      if (the source predicate candidate.is_symlink() is truthy) {
        // Source: vvaharness/orchestrator/store/_db.py:144-144
        Raise StoreError(source_template_144_33).
      }
    }
    // Source: vvaharness/orchestrator/store/_db.py:145-148
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/store/_db.py:146-146
      In source order: Evaluate path.stat(); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/store/_db.py:147-148
    On the first matching source exception FileNotFoundError, in handler order {
      // Source: vvaharness/orchestrator/store/_db.py:148-148
      End this invocation with False.
    }
    // Source: vvaharness/orchestrator/store/_db.py:149-149
    In source order: Evaluate once sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True); assign in source target order to con.
    // Source: vvaharness/orchestrator/store/_db.py:150-153
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/store/_db.py:151-151
      End this invocation with con.execute('SELECT 1 FROM runs WHERE run_id = ?', (run_id,)).fetchone() is not None.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/orchestrator/store/_db.py:153-153
      In source order: Evaluate con.close(); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/store/_db.py:154-155
  On the first matching source exception (OSError, sqlite3.Error) as error, in handler order {
    // Source: vvaharness/orchestrator/store/_db.py:155-155
    Raise StoreError(source_template_155_25) with explicit source cause error.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:158-160
// Source signature: db_path() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn db_path() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:159-159
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call.
  // Source: vvaharness/orchestrator/store/_db.py:160-160
  End this invocation with ensure_state_dir() / _DB_NAME.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:163-179
// Source signature: _create_db_file_safe(path: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _create_db_file_safe(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:164-164
  In source order: Retain source documentation literal source_literal_164_4; it is not a model call.
  // Source: vvaharness/orchestrator/store/_db.py:166-171
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:167-168
    In source order: Evaluate os.close(os.open(path, os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_RDWR, _DB_FILE_MODE)); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/store/_db.py:169-169
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/store/_db.py:170-171
  On the first matching source exception OSError as err, in handler order {
    // Source: vvaharness/orchestrator/store/_db.py:171-171
    In source order: Evaluate once err; assign in source target order to open_err.
  }
  // Source: vvaharness/orchestrator/store/_db.py:172-177
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:173-173
    In source order: Evaluate once os.lstat(path); assign in source target order to st.
  }
  // Source: vvaharness/orchestrator/store/_db.py:174-177
  On the first matching source exception FileNotFoundError, in handler order {
    // Source: vvaharness/orchestrator/store/_db.py:176-177
    Raise FileNotFoundError(source_template_177_12) with explicit source cause open_err.
  }
  // Source: vvaharness/orchestrator/store/_db.py:178-179
  if (the source predicate stat.S_ISLNK(st.st_mode) is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:179-179
    Raise StoreError(source_template_179_25).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:182-200
// Source signature: connect() -> sqlite3.Connection
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn connect() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:183-184
  In source order: Retain source documentation literal source_literal_183_4; it is not a model call. Then Evaluate once db_path(); assign in source target order to path.
  // Source: vvaharness/orchestrator/store/_db.py:185-186
  if (the source predicate _POSIX is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:186-186
    In source order: Evaluate _create_db_file_safe(path); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/_db.py:187-193
  In source order: Evaluate once sqlite3.connect(path); assign in source target order to con. Then Evaluate con.execute('PRAGMA foreign_keys = ON'); retain side effects and discard the expression result. Then Evaluate con.execute('PRAGMA busy_timeout = 30000'); retain side effects and discard the expression result. Then Evaluate con.execute('PRAGMA synchronous  = NORMAL'); retain side effects and discard the expression result. Then Evaluate once con.execute('PRAGMA user_version').fetchone()[0]; assign in source target order to have.
  // Source: vvaharness/orchestrator/store/_db.py:194-195
  if (the source predicate have != _SCHEMA_VERSION is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:195-195
    In source order: Evaluate _migrate(con, have); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/_db.py:197-199
  for each p in (path, *(path.with_name(path.name + s) for s in _SIDECAR_SUFFIXES)) {
    // Source: vvaharness/orchestrator/store/_db.py:199-199
    In source order: Evaluate _tighten_mode(p, _DB_FILE_MODE); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/store/_db.py:200-200
  End this invocation with con.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:203-213
// Source signature: _migrate(con: sqlite3.Connection, have: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _migrate(con, have) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:205-211
  if (the source predicate have == 0 is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:206-206
    In source order: Evaluate con.executescript(_DDL); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/orchestrator/store/_db.py:208-209
    if (the source predicate have < 2 is truthy) {
      // Source: vvaharness/orchestrator/store/_db.py:209-209
      In source order: Evaluate con.executescript(_DDL_V2); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/store/_db.py:210-211
    if (the source predicate have < 3 is truthy) {
      // Source: vvaharness/orchestrator/store/_db.py:211-211
      In source order: Evaluate con.executescript(_DDL_V3); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/store/_db.py:212-213
  In source order: Evaluate con.execute(source_template_212_16); retain side effects and discard the expression result. Then Evaluate con.commit(); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:216-232
// Source signature: register_run(run_id: str, *, repo_root: str, repo_name: str | None=None, app_id: str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn register_run(run_id, repo_root, repo_name, app_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:219-220
  In source order: Retain source documentation literal source_literal_219_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/_db.py:221-231
  Enter source context managers left-to-right: con {
    // Source: vvaharness/orchestrator/store/_db.py:222-231
    In source order: Evaluate con.execute(source_literal_223_12, (run_id, repo_root, repo_name, app_id)); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/orchestrator/store/_db.py:232-232
  In source order: Evaluate con.close(); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:235-248
// Source signature: reset_run(run_id: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reset_run(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:236-238
  In source order: Retain source documentation literal source_literal_236_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/_db.py:239-248
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:240-246
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/_db.py:241-245
      In source order: Evaluate once 0; assign in source target order to cleared. Then Evaluate once con.execute('DELETE FROM checkpoints WHERE run_id = ?', (run_id,)); assign in source target order to cur. Then Apply source augmented assignment cleared += cur.rowcount or 0 with source evaluation/in-place semantics. Then Evaluate once con.execute('DELETE FROM callgraph_snapshots WHERE run_id = ?', (run_id,)); assign in source target order to cur. Then Apply source augmented assignment cleared += cur.rowcount or 0 with source evaluation/in-place semantics.
      // Source: vvaharness/orchestrator/store/_db.py:246-246
      End this invocation with cleared.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/_db.py:248-248
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:251-259
// Source signature: steps_with_prefix(run_id: str, prefix: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn steps_with_prefix(run_id, prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:252-253
  In source order: Retain source documentation literal source_literal_252_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/_db.py:254-259
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:255-256
    In source order: Evaluate once con.execute('SELECT step FROM checkpoints WHERE run_id = ?', (run_id,)).fetchall(); assign in source target order to rows.
    // Source: vvaharness/orchestrator/store/_db.py:257-257
    End this invocation with sorted((r[0] for r in rows if r[0].startswith(prefix))).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/_db.py:259-259
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:262-275
// Source signature: delete_steps(run_id: str, prefix: str, keep: Collection[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn delete_steps(run_id, prefix, keep) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:263-264
  In source order: Retain source documentation literal source_literal_263_4; it is not a model call. Then Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/_db.py:265-275
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:266-272
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/_db.py:267-272
      In source order: Evaluate once con.execute('SELECT step FROM checkpoints WHERE run_id = ?', (run_id,)).fetchall(); assign in source target order to rows. Then Evaluate once sorted((r[0] for r in rows if r[0].startswith(prefix) and r[0] not in keep)); assign in source target order to victims. Then Evaluate con.executemany('DELETE FROM checkpoints WHERE run_id = ? AND step = ?', [(run_id, v) for v in victims]); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/orchestrator/store/_db.py:273-273
    End this invocation with victims.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/_db.py:275-275
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:278-280
// Source signature: delete_run_graphs(run_id: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn delete_run_graphs(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:279-280
  In source order: Retain source documentation literal source_literal_279_4; it is not a model call. Then Evaluate shutil.rmtree(state_root() / 'graphs' / run_id, ignore_errors=True); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/store/_db.py:283-300
// Source signature: delete_run(run_id: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn delete_run(run_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/store/_db.py:284-284
  In source order: Retain source documentation literal source_literal_284_4; it is not a model call.
  // Source: vvaharness/orchestrator/store/_db.py:286-287
  if (the source predicate not db_location().exists() is truthy) {
    // Source: vvaharness/orchestrator/store/_db.py:287-287
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/store/_db.py:288-288
  In source order: Evaluate once connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/store/_db.py:289-300
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/store/_db.py:290-292
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/store/_db.py:291-292
      In source order: Evaluate once con.execute('DELETE FROM runs WHERE run_id = ?', (run_id,)); assign in source target order to cur. Then Evaluate once cur.rowcount or 0; assign in source target order to deleted.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/orchestrator/store/_db.py:293-296
    if (the source predicate deleted is truthy) {
      // Source: vvaharness/orchestrator/store/_db.py:295-296
      In source order: Evaluate con.execute('PRAGMA incremental_vacuum').fetchall(); retain side effects and discard the expression result. Then Evaluate con.execute('PRAGMA wal_checkpoint(TRUNCATE)'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/store/_db.py:297-297
    In source order: Evaluate delete_run_graphs(run_id); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/store/_db.py:298-298
    End this invocation with deleted > 0.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/store/_db.py:300-300
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.orchestrator.store._schema import _DDL, _DDL_V2, _DDL_V3` at source line 24: `source_detail/vvaharness/orchestrator/store/_schema.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 25: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/orchestrator/store/_db.py.sudo.md). Exact strings in the evidence asset support this conversion.
