# vvaharness/skills/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/skills/__init__.py.evidence.json`. SHA-256: `1745ffb792e144a660e255cd2608066f966d8b20a021a3b9f1e82dcddd409f72`.

```sudo
// Source: vvaharness/skills/__init__.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from functools import wraps; preserve alias and import-time effects.
// Source: vvaharness/skills/__init__.py:22-30
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once Path(__file__).parent; assign in source target order to PACKAGED_SKILLS. Then Evaluate once Path('.vvaharness') / 'skills'; assign in source target order to INJECTED_SUBDIR. Then For _INJECTED, assign {}; source annotation dict[str, Path | None]. Then For _TEMP_COPIES, assign {}; source annotation dict[str, tuple[Path, bool]].
// Source: vvaharness/skills/__init__.py:31-31
In source order: Evaluate once threading.Lock(); assign in source target order to _INJECT_LOCK.
// Source: vvaharness/skills/__init__.py:34-39
// Source signature: skill_names() -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn skill_names() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/skills/__init__.py:35-35
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call.
  // Source: vvaharness/skills/__init__.py:36-39
  End this invocation with tuple(sorted((d.name for d in PACKAGED_SKILLS.iterdir() if d.is_dir() and (d / 'SKILL.md').is_file()))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/skills/__init__.py:42-64
// Source signature: _inject(repo_root: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inject(repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/skills/__init__.py:43-44
  In source order: Retain source documentation literal source_literal_43_4; it is not a model call. Then Evaluate once Path(repo_root) / INJECTED_SUBDIR.parent; assign in source target order to parent.
  // Source: vvaharness/skills/__init__.py:45-46
  if (the source predicate parent.is_symlink() is truthy) {
    // Source: vvaharness/skills/__init__.py:46-46
    End this invocation with None.
  }
  // Source: vvaharness/skills/__init__.py:47-47
  In source order: Evaluate once parent.exists(); assign in source target order to parent_existed.
  // Source: vvaharness/skills/__init__.py:48-53
  Perform the following protected operations {
    // Source: vvaharness/skills/__init__.py:49-51
    In source order: Evaluate parent.mkdir(exist_ok=True); retain side effects and discard the expression result. Then Evaluate once Path(repo_root) / INJECTED_SUBDIR; assign in source target order to dst. Then Evaluate dst.mkdir(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/skills/__init__.py:52-53
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/skills/__init__.py:53-53
    End this invocation with None.
  }
  // Source: vvaharness/skills/__init__.py:54-54
  In source order: Evaluate once (dst, parent_existed); assign in source target order to _TEMP_COPIES[str(repo_root.resolve())].
  // Source: vvaharness/skills/__init__.py:55-58
  Perform the following protected operations {
    // Source: vvaharness/skills/__init__.py:56-56
    In source order: Evaluate shutil.copytree(PACKAGED_SKILLS, dst, dirs_exist_ok=True); retain side effects and discard the expression result.
  }
  // Source: vvaharness/skills/__init__.py:57-58
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/skills/__init__.py:58-58
    End this invocation with None.
  }
  // Source: vvaharness/skills/__init__.py:59-63
  for each leftover in (dst / '__init__.py', dst / '__pycache__') {
    // Source: vvaharness/skills/__init__.py:60-63
    if (the source predicate leftover.is_dir() is truthy) {
      // Source: vvaharness/skills/__init__.py:61-61
      In source order: Evaluate shutil.rmtree(leftover, ignore_errors=True); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/skills/__init__.py:62-63
      if (the source predicate leftover.exists() is truthy) {
        // Source: vvaharness/skills/__init__.py:63-63
        In source order: Evaluate leftover.unlink(missing_ok=True); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/skills/__init__.py:64-64
  End this invocation with dst.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/skills/__init__.py:67-73
// Source signature: inject_skills(repo_root: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn inject_skills(repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/skills/__init__.py:68-69
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call. Then Evaluate once str(Path(repo_root).resolve()); assign in source target order to key.
  // Source: vvaharness/skills/__init__.py:70-73
  Enter source context managers left-to-right: _INJECT_LOCK {
    // Source: vvaharness/skills/__init__.py:71-72
    if (the source predicate key not in _INJECTED is truthy) {
      // Source: vvaharness/skills/__init__.py:72-72
      In source order: Evaluate once _inject(Path(repo_root)); assign in source target order to _INJECTED[key].
    }
    // Source: vvaharness/skills/__init__.py:73-73
    End this invocation with _INJECTED[key].
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/skills/__init__.py:76-95
// Source signature: with_injected_skills(function)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn with_injected_skills(function) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/skills/__init__.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
  // Source: vvaharness/skills/__init__.py:79-94
  // Source: vvaharness/skills/__init__.py:78-78
  Before creating this callable, evaluate and retain decorators top-to-bottom: wraps(function).
  // Source: vvaharness/skills/__init__.py:79-94
  // Source signature: scoped(repo: Path, *args, **kwargs)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn scoped(repo, args, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/skills/__init__.py:80-94
    Perform the following protected operations {
      // Source: vvaharness/skills/__init__.py:81-81
      End this invocation with function(repo, *args, **kwargs).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/skills/__init__.py:83-83
      In source order: Evaluate once str(Path(repo).resolve()); assign in source target order to key.
      // Source: vvaharness/skills/__init__.py:84-94
      Enter source context managers left-to-right: _INJECT_LOCK {
        // Source: vvaharness/skills/__init__.py:85-86
        In source order: Evaluate _INJECTED.pop(key, None); retain side effects and discard the expression result. Then Evaluate once _TEMP_COPIES.pop(key, None); assign in source target order to copy.
        // Source: vvaharness/skills/__init__.py:87-94
        if (the source predicate copy is not None is truthy) {
          // Source: vvaharness/skills/__init__.py:88-89
          In source order: Evaluate once copy; assign in source target order to (destination, parent_existed). Then Evaluate shutil.rmtree(destination); retain side effects and discard the expression result.
          // Source: vvaharness/skills/__init__.py:90-94
          if (the source predicate not parent_existed is truthy) {
            // Source: vvaharness/skills/__init__.py:91-94
            Perform the following protected operations {
              // Source: vvaharness/skills/__init__.py:92-92
              In source order: Evaluate (Path(repo) / INJECTED_SUBDIR.parent).rmdir(); retain side effects and discard the expression result.
            }
            // Source: vvaharness/skills/__init__.py:93-94
            On the first matching source exception OSError, in handler order {
              // Source: vvaharness/skills/__init__.py:94-94
              In source order: Perform no operation at this source statement.
            }
          }
        }
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/skills/__init__.py:95-95
  End this invocation with scoped.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/skills/__init__.py:98-99
In source order: Evaluate once ['INJECTED_SUBDIR', 'PACKAGED_SKILLS', 'inject_skills', 'skill_names', 'with_injected_skills']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
