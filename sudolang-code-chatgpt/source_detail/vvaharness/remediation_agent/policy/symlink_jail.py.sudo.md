# vvaharness/remediation_agent/policy/symlink_jail.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/symlink_jail.py.evidence.json`. SHA-256: `3e68ca806ce084931cbed8eedcdfc59733206b0e921c9ab9adbff71b9616dcad`.

```sudo
// Source: vvaharness/remediation_agent/policy/symlink_jail.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once 20000; assign in source target order to _SCAN_FILE_MAX.
// Source: vvaharness/remediation_agent/policy/symlink_jail.py:30-36
In source order: Evaluate once 20000; assign in source target order to _SCAN_DIR_MAX. Then Evaluate once frozenset({'.git', 'node_modules', '.venv', 'venv', '__pycache__', '.mypy_cache', '.pytest_cache', '.ruff_cache', '.tox'}); assign in source target order to _SKIP_DIRS.
// Source: vvaharness/remediation_agent/policy/symlink_jail.py:39-75
// Source signature: escaping_symlinks(repo: Path) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn escaping_symlinks(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:40-48
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:49-52
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:50-50
    In source order: Evaluate once repo.resolve(); assign in source target order to root.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:51-52
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:52-52
    End this invocation with {}.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:53-55
  In source order: For found, assign {}; source annotation dict[str, str]. Then Evaluate once 0; assign in source target order to files_seen. Then Evaluate once 0; assign in source target order to dirs_seen.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:56-74
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:58-72
    for each (dirpath, dirnames, filenames) in os.walk(repo, followlinks=False) {
      // Source: vvaharness/remediation_agent/policy/symlink_jail.py:59-59
      In source order: Apply source augmented assignment dirs_seen += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/remediation_agent/policy/symlink_jail.py:60-61
      if (the source predicate dirs_seen > _SCAN_DIR_MAX is truthy) {
        // Source: vvaharness/remediation_agent/policy/symlink_jail.py:61-61
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vvaharness/remediation_agent/policy/symlink_jail.py:63-67
      for each name in list(dirnames) {
        // Source: vvaharness/remediation_agent/policy/symlink_jail.py:64-66
        if (the source predicate name in _SKIP_DIRS is truthy) {
          // Source: vvaharness/remediation_agent/policy/symlink_jail.py:65-65
          In source order: Evaluate dirnames.remove(name); retain side effects and discard the expression result.
          // Source: vvaharness/remediation_agent/policy/symlink_jail.py:66-66
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/remediation_agent/policy/symlink_jail.py:67-67
        In source order: Evaluate _record(root, repo, Path(dirpath) / name, found); retain side effects and discard the expression result.
      }
      // Source: vvaharness/remediation_agent/policy/symlink_jail.py:68-72
      for each name in filenames {
        // Source: vvaharness/remediation_agent/policy/symlink_jail.py:69-69
        In source order: Apply source augmented assignment files_seen += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/remediation_agent/policy/symlink_jail.py:70-71
        if (the source predicate files_seen > _SCAN_FILE_MAX is truthy) {
          // Source: vvaharness/remediation_agent/policy/symlink_jail.py:71-71
          End this invocation with found.
        }
        // Source: vvaharness/remediation_agent/policy/symlink_jail.py:72-72
        In source order: Evaluate _record(root, repo, Path(dirpath) / name, found); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:73-74
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:74-74
    End this invocation with found.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:75-75
  End this invocation with found.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/symlink_jail.py:78-107
// Source signature: _record(root: Path, repo: Path, path: Path, out: dict[str, str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _record(root, repo, path, out) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:79-85
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:86-90
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:87-88
    if (the source predicate not path.is_symlink() is truthy) {
      // Source: vvaharness/remediation_agent/policy/symlink_jail.py:88-88
      End this invocation with None.
    }
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:89-90
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:90-90
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:91-94
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:92-92
    In source order: Evaluate once path.relative_to(repo).as_posix(); assign in source target order to rel.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:93-94
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:94-94
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:95-100
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:96-96
    In source order: Evaluate once path.resolve(); assign in source target order to target.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:97-100
  On the first matching source exception (OSError, RuntimeError), in handler order {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:99-99
    In source order: Evaluate once _raw_target(path); assign in source target order to out[rel].
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:100-100
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:101-105
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:102-102
    In source order: Evaluate target.relative_to(root); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:103-105
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:104-104
    In source order: Evaluate once str(target); assign in source target order to out[rel].
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:105-105
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:106-107
  if (the source predicate not target.exists() is truthy) {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:107-107
    In source order: Evaluate once source_template_107_19; assign in source target order to out[rel].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/symlink_jail.py:110-115
// Source signature: _raw_target(path: Path) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raw_target(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:111-111
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:112-115
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:113-113
    End this invocation with os.readlink(path).
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:114-115
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:115-115
    End this invocation with '<unreadable>'.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/symlink_jail.py:118-124
// Source signature: describe_escapes(escapes: dict[str, str], limit: int=5) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn describe_escapes(escapes, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:119-121
  In source order: Retain source documentation literal source_literal_119_4; it is not a model call. Then Evaluate once sorted(escapes.items()); assign in source target order to items. Then Evaluate once ', '.join((source_template_121_22 for link, target in items[:limit])); assign in source target order to shown.
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:122-123
  if (the source predicate len(items) > limit is truthy) {
    // Source: vvaharness/remediation_agent/policy/symlink_jail.py:123-123
    In source order: Apply source augmented assignment shown += source_template_123_17 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/remediation_agent/policy/symlink_jail.py:124-124
  End this invocation with shown.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/symlink_jail.py:127-127
In source order: Evaluate once ['describe_escapes', 'escaping_symlinks']; assign in source target order to __all__.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
