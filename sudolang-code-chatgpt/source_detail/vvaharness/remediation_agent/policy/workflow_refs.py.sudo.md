# vvaharness/remediation_agent/policy/workflow_refs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/workflow_refs.py.evidence.json`. SHA-256: `7f5241e69d6f8386710dae86cb21c920963f43ee6e9c6171876337d378d107b1`.

```sudo
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections import Counter, defaultdict; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:21-31
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff import _norm_path, _safe_repo_path; preserve alias and import-time effects. Then Evaluate once '.github/workflows/'; assign in source target order to _WORKFLOW_PREFIX. Then Evaluate once re.compile('[0-9a-fA-F]{40}\\Z'); assign in source target order to _FULL_SHA. Then Evaluate once re.compile('(?im)^\\s*(?:-\\s*)?uses\\s*:\\s*[\'\\"]?(?P<workflow>[^@\\s\'\\"#]+/\\.github/workflows/[^@\\s\'\\"#]+\\.ya?ml)@(?P<ref>[^\\s\'\\"#]+)'); assign in source target order to _USES.
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:34-47
// Source signature: workflow_snapshot_paths(repo: Path) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn workflow_snapshot_paths(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:35-36
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call. Then Evaluate once Path(repo) / _WORKFLOW_PREFIX; assign in source target order to root.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:37-38
  if (the source predicate not root.is_dir() is truthy) {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:38-38
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:39-47
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:40-45
    End this invocation with sorted((p.relative_to(repo).as_posix() for pattern in ('*.yml', '*.yaml') for p in root.glob(pattern) if p.is_file())).
  }
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:46-47
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:47-47
    End this invocation with [].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:50-90
// Source signature: introduced_unsafe_workflow_refs(repo: Path, before: Mapping[str, str | None] | None) -> dict[str, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn introduced_unsafe_workflow_refs(repo, before) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:53-57
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once before or {}; assign in source target order to snapshot. Then For trusted, assign defaultdict(set); source annotation dict[str, set[str]]. Then For prior, assign {}; source annotation dict[str, Counter[tuple[str, str]]].
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:58-66
  for each (raw_path, text) in snapshot.items() {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:59-59
    In source order: Evaluate once _norm_path(raw_path); assign in source target order to path.
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:60-61
    if (the source predicate not _is_workflow_path(path) or text is None is truthy) {
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:61-61
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:62-63
    In source order: Evaluate once _references(text); assign in source target order to refs. Then Evaluate once Counter(refs); assign in source target order to prior[path].
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:64-66
    for each (workflow, ref) in refs {
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:65-66
      if (the source predicate _is_nonplaceholder_sha(ref) is truthy) {
        // Source: vvaharness/remediation_agent/policy/workflow_refs.py:66-66
        In source order: Evaluate trusted[workflow.casefold()].add(ref.casefold()); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:68-70
  In source order: Evaluate once set(workflow_snapshot_paths(repo)); assign in source target order to current_paths. Then Evaluate current_paths.update((path for path in snapshot if _is_workflow_path(path))); retain side effects and discard the expression result. Then For issues, assign {}; source annotation dict[str, list[str]].
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:71-89
  for each path in sorted(current_paths) {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:72-72
    In source order: Evaluate once _safe_repo_path(Path(repo), path); assign in source target order to target.
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:73-74
    if (the source predicate target is None is truthy) {
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:74-74
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:75-78
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:76-76
      In source order: Evaluate once target.read_text(encoding='utf-8') if target.is_file() else ''; assign in source target order to current.
    }
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:77-78
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:78-78
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:79-80
    In source order: Evaluate once prior.get(path, Counter()); assign in source target order to previous. Then For seen, assign Counter(); source annotation Counter[tuple[str, str]].
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:81-89
    for each (workflow, ref) in _references(current) {
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:82-83
      In source order: Evaluate once (workflow, ref); assign in source target order to key. Then Apply source augmented assignment seen[key] += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:84-85
      if (the source predicate seen[key] <= previous[key] is truthy) {
        // Source: vvaharness/remediation_agent/policy/workflow_refs.py:85-85
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:86-86
      In source order: Evaluate once _unsafe_reason(workflow, ref, trusted); assign in source target order to reason.
      // Source: vvaharness/remediation_agent/policy/workflow_refs.py:87-89
      if (the source predicate reason is truthy) {
        // Source: vvaharness/remediation_agent/policy/workflow_refs.py:88-89
        In source order: Evaluate issues.setdefault(path, []).append(source_template_89_20); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:90-90
  End this invocation with issues.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:93-97
// Source signature: _references(text: str) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _references(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:94-97
  End this invocation with [(match.group('workflow'), match.group('ref')) for match in _USES.finditer(text)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:100-102
// Source signature: _is_workflow_path(path: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_workflow_path(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:101-101
  In source order: Evaluate once path.casefold(); assign in source target order to folded.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:102-102
  End this invocation with folded.startswith(_WORKFLOW_PREFIX) and folded.endswith(('.yml', '.yaml')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:105-106
// Source signature: _is_nonplaceholder_sha(ref: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_nonplaceholder_sha(ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:106-106
  End this invocation with bool(_FULL_SHA.fullmatch(ref)) and len(set(ref.casefold())) > 1.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:109-118
// Source signature: _unsafe_reason(workflow: str, ref: str, trusted: dict[str, set[str]]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unsafe_reason(workflow, ref, trusted) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:112-113
  if (the source predicate not _FULL_SHA.fullmatch(ref) is truthy) {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:113-113
    End this invocation with 'not an immutable 40-character commit SHA'.
  }
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:114-115
  if (the source predicate not _is_nonplaceholder_sha(ref) is truthy) {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:115-115
    End this invocation with 'placeholder commit SHA'.
  }
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:116-117
  if (the source predicate ref.casefold() not in trusted.get(workflow.casefold(), set()) is truthy) {
    // Source: vvaharness/remediation_agent/policy/workflow_refs.py:117-117
    End this invocation with 'commit SHA is not established by the pre-edit repository'.
  }
  // Source: vvaharness/remediation_agent/policy/workflow_refs.py:118-118
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/workflow_refs.py:121-121
In source order: Evaluate once ['introduced_unsafe_workflow_refs', 'workflow_snapshot_paths']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff import _norm_path, _safe_repo_path` at source line 23: `source_detail/vvaharness/remediation_agent/artifacts/diff/__init__.py.sudo.md`.
