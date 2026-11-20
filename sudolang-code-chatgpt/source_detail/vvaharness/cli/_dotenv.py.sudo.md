# vvaharness/cli/_dotenv.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/cli/_dotenv.py.evidence.json`. SHA-256: `c8e0698acb08ad642f7cb73c4c58024ed4ce7c6484db596b015e6b24d43e8c53`.

```sudo
// Source: vvaharness/cli/_dotenv.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import stat; preserve alias and import-time effects.
// Source: vvaharness/cli/_dotenv.py:22-26
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/cli/_dotenv.py:29-44
// Source signature: _dotenv_path_is_trusted(path: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dotenv_path_is_trusted(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_dotenv.py:30-30
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call.
  // Source: vvaharness/cli/_dotenv.py:31-34
  Perform the following protected operations {
    // Source: vvaharness/cli/_dotenv.py:32-32
    In source order: Evaluate once (path.parent.stat(), path.stat()); assign in source target order to entries.
  }
  // Source: vvaharness/cli/_dotenv.py:33-34
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/cli/_dotenv.py:34-34
    End this invocation with False.
  }
  // Source: vvaharness/cli/_dotenv.py:35-35
  In source order: Evaluate once getattr(os, 'geteuid', None); assign in source target order to get_euid.
  // Source: vvaharness/cli/_dotenv.py:36-37
  if (the source predicate get_euid is None is truthy) {
    // Source: vvaharness/cli/_dotenv.py:37-37
    End this invocation with True.
  }
  // Source: vvaharness/cli/_dotenv.py:38-38
  In source order: Evaluate once get_euid(); assign in source target order to effective_uid.
  // Source: vvaharness/cli/_dotenv.py:39-43
  for each entry in entries {
    // Source: vvaharness/cli/_dotenv.py:40-41
    if (the source predicate entry.st_uid != effective_uid is truthy) {
      // Source: vvaharness/cli/_dotenv.py:41-41
      End this invocation with False.
    }
    // Source: vvaharness/cli/_dotenv.py:42-43
    if (the source predicate entry.st_mode & (stat.S_IWGRP | stat.S_IWOTH) is truthy) {
      // Source: vvaharness/cli/_dotenv.py:43-43
      End this invocation with False.
    }
  }
  // Source: vvaharness/cli/_dotenv.py:44-44
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_dotenv.py:46-85
// Source signature: _dotenv_selection(repo: str | None=None, *, warn: bool=False) -> tuple[Path | None, str | None, tuple[Path, ...]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dotenv_selection(repo, warn) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_dotenv.py:49-50
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call. Then For roots, assign []; source annotation list[tuple[str, Path]].
  // Source: vvaharness/cli/_dotenv.py:51-55
  for each (source, get_root) in (('cwd', Path.cwd), ('home', Path.home)) {
    // Source: vvaharness/cli/_dotenv.py:52-55
    Perform the following protected operations {
      // Source: vvaharness/cli/_dotenv.py:53-53
      In source order: Evaluate roots.append((source, get_root().resolve())); retain side effects and discard the expression result.
    }
    // Source: vvaharness/cli/_dotenv.py:54-55
    On the first matching source exception (OSError, RuntimeError), in handler order {
      // Source: vvaharness/cli/_dotenv.py:55-55
      Continue the immediately enclosing source loop at its next iteration.
    }
  }
  // Source: vvaharness/cli/_dotenv.py:57-58
  In source order: For rejected, assign []; source annotation list[Path]. Then For seen_roots, assign set(); source annotation set[Path].
  // Source: vvaharness/cli/_dotenv.py:59-84
  for each (source, root) in roots {
    // Source: vvaharness/cli/_dotenv.py:60-61
    if (the source predicate root in seen_roots is truthy) {
      // Source: vvaharness/cli/_dotenv.py:61-61
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/cli/_dotenv.py:62-63
    In source order: Evaluate seen_roots.add(root); retain side effects and discard the expression result. Then Evaluate once root / '.env'; assign in source target order to candidate.
    // Source: vvaharness/cli/_dotenv.py:64-65
    if (the source predicate not candidate.is_file() is truthy) {
      // Source: vvaharness/cli/_dotenv.py:65-65
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/cli/_dotenv.py:66-69
    Perform the following protected operations {
      // Source: vvaharness/cli/_dotenv.py:67-67
      In source order: Evaluate once candidate.resolve(strict=True); assign in source target order to path.
    }
    // Source: vvaharness/cli/_dotenv.py:68-69
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/cli/_dotenv.py:69-69
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/cli/_dotenv.py:70-75
    if (the source predicate path.parent != root or not _dotenv_path_is_trusted(path) is truthy) {
      // Source: vvaharness/cli/_dotenv.py:71-71
      In source order: Evaluate rejected.append(candidate); retain side effects and discard the expression result.
      // Source: vvaharness/cli/_dotenv.py:72-74
      if (the source predicate warn is truthy) {
        // Source: vvaharness/cli/_dotenv.py:73-74
        In source order: Evaluate log.warning(Event.DOTENV_UNTRUSTED, path=candidate, override='VVAHARNESS_ALLOW_CWD_CONFIG=1'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/cli/_dotenv.py:75-75
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/cli/_dotenv.py:76-83
    if (the source predicate repo and (not os.environ.get('VVAHARNESS_ALLOW_CWD_CONFIG')) is truthy) {
      // Source: vvaharness/cli/_dotenv.py:77-77
      In source order: Resolve source import from vvaharness.orchestrator.config_paths import _path_within; preserve alias and import-time effects.
      // Source: vvaharness/cli/_dotenv.py:78-83
      if (the source predicate _path_within(path, repo) is truthy) {
        // Source: vvaharness/cli/_dotenv.py:79-79
        In source order: Evaluate rejected.append(candidate); retain side effects and discard the expression result.
        // Source: vvaharness/cli/_dotenv.py:80-82
        if (the source predicate warn is truthy) {
          // Source: vvaharness/cli/_dotenv.py:81-82
          In source order: Evaluate log.warning(Event.DOTENV_INSIDE_TARGET, path=path, override='VVAHARNESS_ALLOW_CWD_CONFIG=1'); retain side effects and discard the expression result.
        }
        // Source: vvaharness/cli/_dotenv.py:83-83
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    // Source: vvaharness/cli/_dotenv.py:84-84
    End this invocation with (path, source, tuple(rejected)).
  }
  // Source: vvaharness/cli/_dotenv.py:85-85
  End this invocation with (None, None, tuple(rejected)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_dotenv.py:87-89
// Source signature: _dotenv_path(repo: str | None=None, *, warn: bool=False) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dotenv_path(repo, warn) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_dotenv.py:88-88
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call.
  // Source: vvaharness/cli/_dotenv.py:89-89
  End this invocation with _dotenv_selection(repo, warn=warn)[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_dotenv.py:91-102
// Source signature: _load_dotenv(repo: str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_dotenv(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_dotenv.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/cli/_dotenv.py:93-96
  Perform the following protected operations {
    // Source: vvaharness/cli/_dotenv.py:94-94
    In source order: Resolve source import from dotenv import load_dotenv; preserve alias and import-time effects.
  }
  // Source: vvaharness/cli/_dotenv.py:95-96
  On the first matching source exception ImportError, in handler order {
    // Source: vvaharness/cli/_dotenv.py:96-96
    End this invocation with None.
  }
  // Source: vvaharness/cli/_dotenv.py:98-98
  In source order: Evaluate once _dotenv_path(repo, warn=True); assign in source target order to path.
  // Source: vvaharness/cli/_dotenv.py:99-100
  if (the source predicate path is None is truthy) {
    // Source: vvaharness/cli/_dotenv.py:100-100
    End this invocation with None.
  }
  // Source: vvaharness/cli/_dotenv.py:101-102
  In source order: Evaluate load_dotenv(path, override=False); retain side effects and discard the expression result. Then Evaluate console.write(source_template_102_18); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 24: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _path_within` at source line 77: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
