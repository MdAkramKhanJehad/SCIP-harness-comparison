# vvaharness/remediation_agent/artifacts/diff/paths.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/diff/paths.py.evidence.json`. SHA-256: `6447754c8742fe80698ee709bf033b9ffc5906fed7f87d6a86c8e89ce149792e`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/diff/paths.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/diff/paths.py:23-26
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once re.compile('^(?:[\\\\/]{2}|[A-Za-z]:)'); assign in source target order to _UNC_OR_DRIVE.
// Source: vvaharness/remediation_agent/artifacts/diff/paths.py:29-35
// Source signature: _norm_path(ref: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _norm_path(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:30-31
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then Evaluate once (ref or '').strip(); assign in source target order to ref.
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:32-33
  if (the source predicate not ref is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:33-33
    End this invocation with ''.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:35-35
  End this invocation with re.sub(':\\d+(?:-\\d+)?$', '', ref).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/artifacts/diff/paths.py:38-49
// Source signature: _safe_repo_path(repo: Path, ref: str) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _safe_repo_path(repo, ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:39-41
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call. Then Evaluate once _norm_path(ref); assign in source target order to rel.
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:42-43
  if (the source predicate not rel or Path(rel).is_absolute() or _UNC_OR_DRIVE.match(rel) is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:43-43
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:44-48
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:45-46
    In source order: Evaluate once (repo / rel).resolve(); assign in source target order to target. Then Evaluate target.relative_to(repo.resolve()); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:47-48
  On the first matching source exception (ValueError, OSError), in handler order {
    // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:48-48
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/paths.py:49-49
  End this invocation with target.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 21: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 21: `source_detail/vvaharness/util/logs.py.sudo.md`.
