# vvaharness/validation/tools/_scope.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/tools/_scope.py.evidence.json`. SHA-256: `9e9e309e44339dbf05eea4083eb0c48725871bb467a583f5ee468c88fdeec334`.

```sudo
// Source: vvaharness/validation/tools/_scope.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterator; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/_scope.py:25-40
In source order: Resolve source import from vvaharness.scope import _DEFAULT_EXCLUDE_DIRS, _DEFAULT_EXCLUDE_EXTS, _DEFAULT_EXCLUDE_GLOBS, _has_target_build_marker, glob_hit; preserve alias and import-time effects. Then For _TEST_DIRS, assign frozenset({'test', 'tests', '__tests__', '__test__', 'e2e', 'testdata', 'fixtures', '__fixtures__', 'mocks', '__mocks__', 'stubs'}); source annotation frozenset[str]. Then For _PRODUCTION_EXCLUDE_DIRS, assign frozenset((d.lower() for d in _DEFAULT_EXCLUDE_DIRS)); source annotation frozenset[str]. Then For _INFRA_DIRS, assign _PRODUCTION_EXCLUDE_DIRS - _TEST_DIRS; source annotation frozenset[str]. Then For _EXCLUDE_EXTS, assign frozenset((e.lower() for e in _DEFAULT_EXCLUDE_EXTS)); source annotation frozenset[str].
// Source: vvaharness/validation/tools/_scope.py:43-47
if (the source predicate not _TEST_DIRS <= _PRODUCTION_EXCLUDE_DIRS is truthy) {
  // Source: vvaharness/validation/tools/_scope.py:44-47
  Raise RuntimeError(source_template_45_8).
}
// Source: vvaharness/validation/tools/_scope.py:50-52
// Source signature: _has_excluded_ext(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _has_excluded_ext(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/_scope.py:51-51
  In source order: Evaluate once name.lower(); assign in source target order to lowered.
  // Source: vvaharness/validation/tools/_scope.py:52-52
  End this invocation with any((lowered.endswith(ext) for ext in _EXCLUDE_EXTS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/_scope.py:55-60
// Source signature: _excluded_file(rel_path: Path, *, include_tests: bool) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _excluded_file(rel_path, include_tests) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/_scope.py:56-57
  if (the source predicate _has_excluded_ext(rel_path.name) is truthy) {
    // Source: vvaharness/validation/tools/_scope.py:57-57
    End this invocation with True.
  }
  // Source: vvaharness/validation/tools/_scope.py:58-60
  End this invocation with not include_tests and bool(glob_hit(rel_path.as_posix(), _DEFAULT_EXCLUDE_GLOBS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/_scope.py:63-71
// Source signature: _escapes_workspace(path: Path, root: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _escapes_workspace(path, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/_scope.py:64-64
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/validation/tools/_scope.py:65-66
  if (the source predicate not path.is_symlink() is truthy) {
    // Source: vvaharness/validation/tools/_scope.py:66-66
    End this invocation with False.
  }
  // Source: vvaharness/validation/tools/_scope.py:67-70
  Perform the following protected operations {
    // Source: vvaharness/validation/tools/_scope.py:68-68
    In source order: Evaluate path.resolve().relative_to(root); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/_scope.py:69-70
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/validation/tools/_scope.py:70-70
    End this invocation with True.
  }
  // Source: vvaharness/validation/tools/_scope.py:71-71
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/_scope.py:74-96
// Source signature: iter_in_scope_files(workspace: Path, *, include_tests: bool) -> Iterator[Path]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn iter_in_scope_files(workspace, include_tests) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/_scope.py:75-78
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once workspace.resolve(); assign in source target order to root. Then Evaluate once _INFRA_DIRS if include_tests else _INFRA_DIRS | _TEST_DIRS; assign in source target order to excluded_dirs.
  // Source: vvaharness/validation/tools/_scope.py:79-96
  for each (current, dir_names, file_names) in os.walk(workspace, followlinks=False) {
    // Source: vvaharness/validation/tools/_scope.py:80-86
    In source order: Evaluate once Path(current); assign in source target order to current_path. Then Evaluate once sorted((name for name in dir_names if name.lower() not in excluded_dirs or (name.lower() == 'target' and (not _has_target_build_marker(current_path, []))))); assign in source target order to dir_names[:].
    // Source: vvaharness/validation/tools/_scope.py:87-96
    for each name in sorted(file_names) {
      // Source: vvaharness/validation/tools/_scope.py:88-89
      In source order: Evaluate once current_path / name; assign in source target order to path. Then Evaluate once path.relative_to(workspace); assign in source target order to rel_path.
      // Source: vvaharness/validation/tools/_scope.py:90-95
      if (the source predicate _excluded_file(rel_path, include_tests=include_tests) or _escapes_workspace(path, root) or (not path.is_file()) is truthy) {
        // Source: vvaharness/validation/tools/_scope.py:95-95
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/validation/tools/_scope.py:96-96
      In source order: Yield path; suspend this generator until resumed.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.scope import _DEFAULT_EXCLUDE_DIRS, _DEFAULT_EXCLUDE_EXTS, _DEFAULT_EXCLUDE_GLOBS, _has_target_build_marker, glob_hit` at source line 25: `source_detail/vvaharness/scope/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/tools/_scope.py.sudo.md). Exact strings in the evidence asset support this conversion.
