# vvaharness/validation/ingest/workspace.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/ingest/workspace.py.evidence.json`. SHA-256: `c79e9c9273ba43d16ba437928a19e4d07d184b04af17e57350e930750ca9baa0`.

```sudo
// Source: vvaharness/validation/ingest/workspace.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Sequence; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/validation/ingest/workspace.py:23-46
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import AGENT_INSTRUCTION_FILENAMES, APP_DIRNAME, DIFF_FILENAME, MCP_CONFIG_FILENAME, REMEDIATION_DIRNAME, SCAN_DIRNAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.errors import IngestError; preserve alias and import-time effects. Then Evaluate once shutil.ignore_patterns('.git', 'venv', '.venv', 'checkpoints', SCAN_DIRNAME, REMEDIATION_DIRNAME, '__pycache__', '*.pyc', 'node_modules', MCP_CONFIG_FILENAME, *AGENT_INSTRUCTION_FILENAMES); assign in source target order to _IGNORE.
// Source: vvaharness/validation/ingest/workspace.py:49-58
// Source signature: _link_rel(repo: Path, candidate: Path) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _link_rel(repo, candidate) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:50-54
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call.
  // Source: vvaharness/validation/ingest/workspace.py:55-58
  Perform the following protected operations {
    // Source: vvaharness/validation/ingest/workspace.py:56-56
    End this invocation with candidate.relative_to(repo).
  }
  // Source: vvaharness/validation/ingest/workspace.py:57-58
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/validation/ingest/workspace.py:58-58
    End this invocation with candidate.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/workspace.py:61-70
// Source signature: _link_escape_reason(candidate: Path, root: Path) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _link_escape_reason(candidate, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:62-65
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call.
  // Source: vvaharness/validation/ingest/workspace.py:66-69
  Perform the following protected operations {
    // Source: vvaharness/validation/ingest/workspace.py:67-67
    In source order: Evaluate once candidate.resolve(strict=True); assign in source target order to resolved.
  }
  // Source: vvaharness/validation/ingest/workspace.py:68-69
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/validation/ingest/workspace.py:69-69
    End this invocation with 'dangling (missing target)'.
  }
  // Source: vvaharness/validation/ingest/workspace.py:70-70
  End this invocation with None if resolved.is_relative_to(root) else 'outside repository'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/workspace.py:73-97
// Source signature: _ignore_escaping_links(repo: Path) -> Callable[[str, list[str]], set[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ignore_escaping_links(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:74-83
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call. Then Evaluate once repo.resolve(); assign in source target order to root.
  // Source: vvaharness/validation/ingest/workspace.py:85-95
  // Source signature: ignore(src_dir: str, names: list[str]) -> set[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ignore(src_dir, names) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/ingest/workspace.py:86-88
    In source order: Evaluate once set(_IGNORE(src_dir, names)); assign in source target order to skip. Then Evaluate once (Path(src_dir) / name for name in names if name not in skip); assign in source target order to candidates. Then Evaluate once [c for c in candidates if c.is_symlink()]; assign in source target order to links.
    // Source: vvaharness/validation/ingest/workspace.py:89-94
    for each candidate in links {
      // Source: vvaharness/validation/ingest/workspace.py:90-90
      In source order: Evaluate once _link_escape_reason(candidate, root); assign in source target order to reason.
      // Source: vvaharness/validation/ingest/workspace.py:91-94
      if (the source predicate reason is not None is truthy) {
        // Source: vvaharness/validation/ingest/workspace.py:92-94
        In source order: Evaluate once _link_rel(repo, candidate); assign in source target order to rel. Then Evaluate console.write(source_template_93_30); retain side effects and discard the expression result. Then Evaluate skip.add(candidate.name); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/validation/ingest/workspace.py:95-95
    End this invocation with skip.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/validation/ingest/workspace.py:97-97
  End this invocation with ignore.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/workspace.py:100-105
// Source signature: stage_workspace(repo: Path, workspace: Path, diff: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stage_workspace(repo, workspace, diff) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:101-101
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call.
  // Source: vvaharness/validation/ingest/workspace.py:102-103
  if (the source predicate workspace.exists() is truthy) {
    // Source: vvaharness/validation/ingest/workspace.py:103-103
    In source order: Evaluate shutil.rmtree(workspace); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/ingest/workspace.py:104-105
  In source order: Evaluate shutil.copytree(repo, workspace, ignore=_ignore_escaping_links(repo)); retain side effects and discard the expression result. Then Evaluate (workspace / DIFF_FILENAME).write_text(diff, encoding='utf-8', newline=''); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/workspace.py:108-115
// Source signature: _under_repo(repo: Path, candidate: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _under_repo(repo, candidate) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:109-109
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call.
  // Source: vvaharness/validation/ingest/workspace.py:110-114
  Perform the following protected operations {
    // Source: vvaharness/validation/ingest/workspace.py:111-112
    In source order: Evaluate once candidate.resolve(); assign in source target order to resolved. Then Evaluate resolved.relative_to(repo.resolve()); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/ingest/workspace.py:113-114
  On the first matching source exception (ValueError, OSError), in handler order {
    // Source: vvaharness/validation/ingest/workspace.py:114-114
    End this invocation with None.
  }
  // Source: vvaharness/validation/ingest/workspace.py:115-115
  End this invocation with resolved.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/workspace.py:118-126
// Source signature: _resolve_touched(repo: Path, touched: str) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_touched(repo, touched) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:119-119
  In source order: Retain source documentation literal source_literal_119_4; it is not a model call.
  // Source: vvaharness/validation/ingest/workspace.py:120-121
  if (the source predicate Path(touched).is_absolute() is truthy) {
    // Source: vvaharness/validation/ingest/workspace.py:121-121
    End this invocation with None.
  }
  // Source: vvaharness/validation/ingest/workspace.py:122-125
  for each base in (repo / touched, repo / APP_DIRNAME / touched) {
    // Source: vvaharness/validation/ingest/workspace.py:123-123
    In source order: Evaluate once _under_repo(repo, base); assign in source target order to candidate.
    // Source: vvaharness/validation/ingest/workspace.py:124-125
    if (the source predicate candidate is not None and candidate.exists() is truthy) {
      // Source: vvaharness/validation/ingest/workspace.py:125-125
      End this invocation with candidate.
    }
  }
  // Source: vvaharness/validation/ingest/workspace.py:126-126
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/workspace.py:129-131
// Source signature: _any_touched_exists(repo: Path, files_touched: Sequence[str]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _any_touched_exists(repo, files_touched) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:130-130
  In source order: Retain source documentation literal source_literal_130_4; it is not a model call.
  // Source: vvaharness/validation/ingest/workspace.py:131-131
  End this invocation with any((_resolve_touched(repo, touched) is not None for touched in files_touched)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/workspace.py:134-137
// Source signature: assert_remediation_applied(repo: Path, files_touched: Sequence[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn assert_remediation_applied(repo, files_touched) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/workspace.py:135-135
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call.
  // Source: vvaharness/validation/ingest/workspace.py:136-137
  if (the source predicate not _any_touched_exists(repo, files_touched) is truthy) {
    // Source: vvaharness/validation/ingest/workspace.py:137-137
    Raise IngestError(source_template_137_26).
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 23: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import AGENT_INSTRUCTION_FILENAMES, APP_DIRNAME, DIFF_FILENAME, MCP_CONFIG_FILENAME, REMEDIATION_DIRNAME, SCAN_DIRNAME` at source line 24: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.ingest.errors import IngestError` at source line 32: `source_detail/vvaharness/validation/ingest/errors.py.sudo.md`.
