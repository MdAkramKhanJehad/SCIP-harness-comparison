# vvaharness/remediation_agent/artifacts/diff/gitcapture.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/diff/gitcapture.py.evidence.json`. SHA-256: `793acd4f2e1277ae0c8569edaff7b2caafe7ed8e1693befd5e856b4a6aea2d98`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:21-27
In source order: Resolve source import import tempfile; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:30-89
// Source signature: changed_files_whole_tree(repo: Path) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn changed_files_whole_tree(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:31-34
  In source order: Retain source documentation literal source_literal_31_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo. Then Evaluate once repo.resolve(); assign in source target order to root.
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:35-57
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:36-38
    In source order: Evaluate once subprocess.run(['git', '-C', str(repo), 'rev-parse', '--is-inside-work-tree'], capture_output=True, text=True, timeout=15); assign in source target order to chk.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:39-40
    if (the source predicate chk.returncode != 0 or chk.stdout.strip() != 'true' is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:40-40
      End this invocation with [].
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:41-43
    In source order: Evaluate once subprocess.run(['git', '-C', str(repo), 'rev-parse', '--show-toplevel'], capture_output=True, text=True, timeout=15); assign in source target order to top.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:44-45
    if (the source predicate top.returncode != 0 or not top.stdout.strip() is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:45-45
      End this invocation with [].
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:46-53
    In source order: Evaluate once Path(top.stdout.strip()).resolve(); assign in source target order to toplevel. Then Evaluate once subprocess.run(['git', '-C', str(repo), 'status', '--porcelain', '-z', '--untracked-files=all', '--', '.'], capture_output=True, text=True, timeout=60); assign in source target order to out.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:54-55
    if (the source predicate out.returncode != 0 is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:55-55
      End this invocation with [].
    }
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:56-57
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:57-57
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:59-60
  In source order: For files, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:62-75
  // Source signature: _add(path: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _add(path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:63-64
    if (the source predicate not path is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:64-64
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:69-72
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:70-70
      In source order: Evaluate once (toplevel / path).resolve().relative_to(root).as_posix(); assign in source target order to rel.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:71-72
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:72-72
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:73-75
    if (the source predicate rel not in seen is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:74-75
      In source order: Evaluate seen.add(rel); retain side effects and discard the expression result. Then Evaluate files.append(rel); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:78-79
  In source order: Evaluate once out.stdout.split('\x00'); assign in source target order to records. Then Evaluate once (0, len(records)); assign in source target order to (i, n).
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:80-88
  while (the source predicate i < n is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:81-82
    In source order: Evaluate once records[i]; assign in source target order to rec. Then Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:83-84
    if (the source predicate not rec is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:84-84
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:85-85
    In source order: Evaluate _add(rec[3:] if len(rec) > 3 else ''); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:86-88
    if (the source predicate ('R' in rec[:2] or 'C' in rec[:2]) and i < n is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:87-88
      In source order: Evaluate _add(records[i]); retain side effects and discard the expression result. Then Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:89-89
  End this invocation with files.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:92-157
// Source signature: capture_git_diff(repo: Path, files: list[str], *, baseline: dict[str, str | None] | None=None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn capture_git_diff(repo, files, baseline) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:94-99
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo. Then Evaluate once repo.resolve(); assign in source target order to root. Then For paths, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:100-103
  for each f in files or [] {
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:101-101
    In source order: Evaluate once _safe_repo_path(repo, f); assign in source target order to safe.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:102-103
    if (the source predicate safe is not None is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:103-103
      In source order: Evaluate paths.append(safe.relative_to(root).as_posix()); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:104-105
  if (the source predicate not paths is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:105-105
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:106-107
  In source order: Evaluate once {**os.environ, 'LC_ALL': 'C'}; assign in source target order to env. Then Evaluate once ['git', '-C', str(repo), '-c', 'color.ui=false']; assign in source target order to git.
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:108-157
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:109-111
    In source order: Evaluate once subprocess.run([*git, 'rev-parse', '--is-inside-work-tree'], capture_output=True, text=True, timeout=15, env=env); assign in source target order to chk.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:112-113
    if (the source predicate chk.returncode != 0 or chk.stdout.strip() != 'true' is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:113-113
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:115-117
    In source order: Evaluate once subprocess.run([*git, 'rev-parse', '--git-dir'], capture_output=True, text=True, timeout=15, env=env); assign in source target order to gd. Then Evaluate once Path(gd.stdout.strip()) if gd.returncode == 0 and gd.stdout.strip() else None; assign in source target order to git_dir.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:118-119
    if (the source predicate git_dir is not None and (not git_dir.is_absolute()) is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:119-119
      In source order: Evaluate once (repo / git_dir).resolve(); assign in source target order to git_dir.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:120-120
    In source order: Evaluate once git_dir / 'index' if git_dir is not None else None; assign in source target order to real_index.
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:122-155
    Enter source context managers left-to-right: tempfile.TemporaryDirectory() bound to tmp {
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:123-123
      In source order: Evaluate once Path(tmp) / 'index'; assign in source target order to tmp_index.
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:124-125
      if (the source predicate real_index is not None and real_index.exists() is truthy) {
        // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:125-125
        In source order: Evaluate shutil.copyfile(real_index, tmp_index); retain side effects and discard the expression result.
      }
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:126-126
      In source order: Evaluate once {**env, 'GIT_INDEX_FILE': str(tmp_index)}; assign in source target order to scoped_env.
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:128-147
      if (the source predicate baseline is truthy) {
        // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:129-129
        In source order: Evaluate once {_norm_path(k): v for k, v in baseline.items()}; assign in source target order to baseline_norm.
        // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:130-147
        for each rel in paths {
          // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:131-132
          if (the source predicate rel not in baseline_norm is truthy) {
            // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:132-132
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:133-133
          In source order: Evaluate once baseline_norm[rel]; assign in source target order to old.
          // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:134-138
          if (the source predicate old is None is truthy) {
            // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:136-137
            In source order: Evaluate subprocess.run([*git, 'update-index', '--force-remove', '--', rel], capture_output=True, text=True, timeout=30, env=scoped_env); retain side effects and discard the expression result.
            // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:138-138
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:139-142
          In source order: Evaluate once subprocess.run([*git, 'hash-object', '-w', '--stdin'], input=old, capture_output=True, text=True, timeout=30, env=scoped_env); assign in source target order to blob. Then Evaluate once blob.stdout.strip(); assign in source target order to sha.
          // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:143-147
          if (the source predicate blob.returncode == 0 and sha is truthy) {
            // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:144-147
            In source order: Evaluate subprocess.run([*git, 'update-index', '--add', '--cacheinfo', source_template_146_29], capture_output=True, text=True, timeout=30, env=scoped_env); retain side effects and discard the expression result.
          }
        }
      }
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:149-154
      In source order: Evaluate subprocess.run([*git, 'add', '-N', '--', *paths], capture_output=True, text=True, timeout=30, env=scoped_env); retain side effects and discard the expression result. Then Evaluate once subprocess.run([*git, 'diff', '--no-ext-diff', '--', *paths], capture_output=True, text=True, timeout=60, env=scoped_env); assign in source target order to out. Then Evaluate once out.stdout; assign in source target order to diff.
      // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:155-155
      End this invocation with diff if diff.strip() else None.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:156-157
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/artifacts/diff/gitcapture.py:157-157
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path` at source line 24: `source_detail/vvaharness/remediation_agent/artifacts/diff/paths.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/logs.py.sudo.md`.
