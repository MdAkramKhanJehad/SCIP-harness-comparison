# vvaharness/remediation_agent/artifacts/diff/snapshot.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/diff/snapshot.py.evidence.json`. SHA-256: `c8c879541fce7325e2aeffa0240e324ed01692337d61fed9147bf35365ebbf77`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:15-24
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:26-26
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:29-43
// Source signature: changed_since_snapshot(repo: Path, before: dict[str, str | None] | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn changed_since_snapshot(repo, before) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:30-32
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo. Then For changed, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:33-42
  for each (rel, old) in (before or {}).items() {
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:34-34
    In source order: Evaluate once _safe_repo_path(repo, rel); assign in source target order to p.
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:35-36
    if (the source predicate p is None is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:36-36
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:37-40
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:38-38
      In source order: Evaluate once p.read_text(encoding='utf-8') if p.is_file() else None; assign in source target order to now.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:39-40
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:40-40
      In source order: Evaluate once None; assign in source target order to now.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:41-42
    if (the source predicate now != old is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:42-42
      In source order: Evaluate changed.append(rel); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:43-43
  End this invocation with changed.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:46-64
// Source signature: snapshot_files(repo: Path, files: list[str]) -> dict[str, str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn snapshot_files(repo, files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:47-49
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo. Then For snap, assign {}; source annotation dict[str, str | None].
  // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:50-63
  for each f in files or [] {
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:51-51
    In source order: Evaluate once _norm_path(f); assign in source target order to rel.
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:52-53
    if (the source predicate not rel or rel in snap is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:53-53
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:55-55
    In source order: Evaluate once _safe_repo_path(repo, f); assign in source target order to p.
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:56-59
    if (the source predicate p is None is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:57-58
      In source order: Evaluate log.warning('snapshot: refusing out-of-repo file reference %r (escapes %s)', f, repo); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:59-59
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:60-63
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:61-61
      In source order: Evaluate once p.read_text(encoding='utf-8') if p.is_file() else None; assign in source target order to snap[rel].
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:62-63
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:63-63
      In source order: Evaluate once None; assign in source target order to snap[rel].
    }
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/snapshot.py:64-64
  End this invocation with snap.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path` at source line 20: `source_detail/vvaharness/remediation_agent/artifacts/diff/paths.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/logs.py.sudo.md`.
