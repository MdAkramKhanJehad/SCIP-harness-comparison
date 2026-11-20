# vvaharness/remediation_agent/policy/revert.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/revert.py.evidence.json`. SHA-256: `5f03b39a2439752a48eb59fed1a4b708bb556c539d8343618564f302a458a711`.

```sudo
// Source: vvaharness/remediation_agent/policy/revert.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff import _norm_path, _safe_repo_path; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/revert.py:22-25
In source order: Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.git_paths import is_git_metadata; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/policy/revert.py:28-35
// Source signature: _is_git_worktree(repo: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_git_worktree(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/revert.py:29-35
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/revert.py:30-32
    In source order: Evaluate once subprocess.run(['git', '-C', str(repo), 'rev-parse', '--is-inside-work-tree'], capture_output=True, text=True, timeout=15); assign in source target order to r.
    // Source: vvaharness/remediation_agent/policy/revert.py:33-33
    End this invocation with r.returncode == 0 and r.stdout.strip() == 'true'.
  }
  // Source: vvaharness/remediation_agent/policy/revert.py:34-35
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/policy/revert.py:35-35
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/revert.py:38-45
// Source signature: _is_tracked(repo: Path, rel: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_tracked(repo, rel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/revert.py:39-45
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/revert.py:40-42
    In source order: Evaluate once subprocess.run(['git', '-C', str(repo), 'ls-files', '--error-unmatch', '--', rel], capture_output=True, text=True, timeout=15); assign in source target order to r.
    // Source: vvaharness/remediation_agent/policy/revert.py:43-43
    End this invocation with r.returncode == 0.
  }
  // Source: vvaharness/remediation_agent/policy/revert.py:44-45
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/policy/revert.py:45-45
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/revert.py:48-91
// Source signature: revert_files(repo: Path, files: list[str], before_snapshot: dict[str, str | None] | None=None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn revert_files(repo, files, before_snapshot) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/revert.py:50-55
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo. Then Evaluate once before_snapshot or {}; assign in source target order to snap. Then Evaluate once _is_git_worktree(repo); assign in source target order to is_git. Then For reverted, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/policy/revert.py:56-90
  for each raw in files or [] {
    // Source: vvaharness/remediation_agent/policy/revert.py:57-57
    In source order: Evaluate once _norm_path(raw); assign in source target order to rel.
    // Source: vvaharness/remediation_agent/policy/revert.py:58-59
    if (the source predicate not rel is truthy) {
      // Source: vvaharness/remediation_agent/policy/revert.py:59-59
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/revert.py:61-64
    if (the source predicate _safe_repo_path(repo, raw) is None is truthy) {
      // Source: vvaharness/remediation_agent/policy/revert.py:62-63
      In source order: Evaluate log.warning('refusing to revert out-of-repo path %r (escapes %s)', raw, repo); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/policy/revert.py:64-64
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/revert.py:66-68
    if (the source predicate is_git_metadata(rel) is truthy) {
      // Source: vvaharness/remediation_agent/policy/revert.py:67-67
      In source order: Evaluate log.warning('refusing to revert .git-owned path %r', rel); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/policy/revert.py:68-68
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/revert.py:69-69
    In source order: Evaluate once repo / rel; assign in source target order to p.
    // Source: vvaharness/remediation_agent/policy/revert.py:70-90
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/policy/revert.py:71-79
      if (the source predicate rel in snap is truthy) {
        // Source: vvaharness/remediation_agent/policy/revert.py:72-72
        In source order: Evaluate once snap[rel]; assign in source target order to old.
        // Source: vvaharness/remediation_agent/policy/revert.py:73-77
        if (the source predicate old is None is truthy) {
          // Source: vvaharness/remediation_agent/policy/revert.py:74-75
          if (the source predicate p.exists() is truthy) {
            // Source: vvaharness/remediation_agent/policy/revert.py:75-75
            In source order: Evaluate p.unlink(); retain side effects and discard the expression result.
          }
        }
        else {
          // Source: vvaharness/remediation_agent/policy/revert.py:77-77
          In source order: Evaluate p.write_text(old, encoding='utf-8'); retain side effects and discard the expression result.
        }
        // Source: vvaharness/remediation_agent/policy/revert.py:78-78
        In source order: Evaluate reverted.append(rel); retain side effects and discard the expression result.
        // Source: vvaharness/remediation_agent/policy/revert.py:79-79
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/policy/revert.py:80-88
      if (the source predicate is_git is truthy) {
        // Source: vvaharness/remediation_agent/policy/revert.py:81-87
        if (the source predicate _is_tracked(repo, rel) is truthy) {
          // Source: vvaharness/remediation_agent/policy/revert.py:82-84
          In source order: Evaluate subprocess.run(['git', '-C', str(repo), 'checkout', '--', rel], capture_output=True, text=True, timeout=30); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/remediation_agent/policy/revert.py:85-87
          if (the source predicate p.exists() is truthy) {
            // Source: vvaharness/remediation_agent/policy/revert.py:87-87
            In source order: Evaluate p.unlink(); retain side effects and discard the expression result.
          }
        }
        // Source: vvaharness/remediation_agent/policy/revert.py:88-88
        In source order: Evaluate reverted.append(rel); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/remediation_agent/policy/revert.py:89-90
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/remediation_agent/policy/revert.py:90-90
      In source order: Evaluate log.warning('failed to revert %s: %s', rel, e); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/policy/revert.py:91-91
  End this invocation with reverted.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff import _norm_path, _safe_repo_path` at source line 21: `source_detail/vvaharness/remediation_agent/artifacts/diff/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.git_paths import is_git_metadata` at source line 23: `source_detail/vvaharness/util/git_paths.py.sudo.md`.
