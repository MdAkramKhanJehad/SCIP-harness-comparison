# vvaharness/backends/harness/deepagents/options/filesystem.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/filesystem.py.evidence.json`. SHA-256: `89b5cc8a12b26201a160a8cc8c1084114334a84bd3b680e1ec67d752c1fa4f90`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import contextlib; preserve alias and import-time effects. Then Resolve source import from functools import lru_cache; preserve alias and import-time effects. Then Resolve source import from pathlib import Path, PurePosixPath; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:23-27
In source order: Resolve source import from deepagents.backends import FilesystemBackend; preserve alias and import-time effects. Then Resolve source import from deepagents.backends import filesystem as _deepagents_filesystem; preserve alias and import-time effects. Then Resolve source import from deepagents.backends.composite import CompositeBackend; preserve alias and import-time effects. Then Resolve source import from deepagents.backends.filesystem import _raise_if_symlink_loop; preserve alias and import-time effects. Then Resolve source import from deepagents.backends.local_shell import LocalShellBackend; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:28-48
In source order: Resolve source import from deepagents.backends.protocol import BackendProtocol, DeleteResult, EditResult, FileInfo, FileUploadResponse, GlobResult, GrepResult, LsResult, ReadResult, WriteResult; preserve alias and import-time effects. Then Resolve source import from deepagents.middleware.filesystem import FilesystemPermission; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.models import GIT_INTERNALS_DENY, READ_ONLY_PERMISSIONS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import OneShotOptions, StreamingOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import tools as _scan_scope; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:49-53
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.git_paths import is_git_metadata; preserve alias and import-time effects. Then Evaluate once "ERROR: path '{path}' is outside the scan root; use a repo-relative path"; assign in source target order to _JAIL_ERROR.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:56-68
// Source signature: _filesystem_permissions(options: OneShotOptions | StreamingOptions) -> list[FilesystemPermission]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _filesystem_permissions(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:59-59
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:60-67
  if (the source predicate options.allow_writes is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:62-62
    In source order: Evaluate once options.cwd.resolve(); assign in source target order to root.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:63-66
    for each raw in options.writable_paths {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:64-64
      In source order: Evaluate once Path(raw).resolve(); assign in source target order to candidate.
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:65-66
      if (the source predicate candidate != root and root not in candidate.parents is truthy) {
        // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:66-66
        Raise ValueError(source_template_66_33).
      }
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:67-67
    End this invocation with GIT_INTERNALS_DENY.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:68-68
  End this invocation with READ_ONLY_PERMISSIONS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:72-80
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:71-71
Before creating this callable, evaluate and retain decorators top-to-bottom: lru_cache(maxsize=8).
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:72-80
// Source signature: _in_scope_dirs(scope: frozenset[str]) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _in_scope_dirs(scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:73-75
  In source order: Retain source documentation literal source_literal_73_4; it is not a model call. Then For dirs, assign set(); source annotation set[str].
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:76-79
  for each rel in scope {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:77-77
    In source order: Evaluate once rel.split('/')[:-1]; assign in source target order to parts.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:78-79
    for each depth in range(1, len(parts) + 1) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:79-79
      In source order: Evaluate dirs.add('/'.join(parts[:depth])); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:80-80
  End this invocation with frozenset(dirs).
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:84-84
In source order: Evaluate once 'write operations are disabled on detection sessions: {path}'; assign in source target order to _WRITE_REFUSED.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:87-112
interface _NoWriteBackend {
  Describe the source Python type, preserving its base/metaclass expression order: FilesystemBackend.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:88-88
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:91-92
  // Source signature: write(self, file_path: str, content: str) -> WriteResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write(self, file_path, content) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:92-92
    End this invocation with WriteResult(error=_WRITE_REFUSED.format(path=file_path)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:94-101
  // Source signature: edit(self, file_path: str, old_string: str, new_string: str, replace_all: bool=False) -> EditResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn edit(self, file_path, old_string, new_string, replace_all) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:101-101
    End this invocation with EditResult(error=_WRITE_REFUSED.format(path=file_path)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:103-104
  // Source signature: delete(self, file_path: str) -> DeleteResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn delete(self, file_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:104-104
    End this invocation with DeleteResult(error=_WRITE_REFUSED.format(path=file_path)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:106-112
  // Source signature: upload_files(self, files: list[tuple[str, bytes]]) -> list[FileUploadResponse]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn upload_files(self, files) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:109-112
    End this invocation with [FileUploadResponse(path=path, error=_WRITE_REFUSED.format(path=path)) for path, _content in files].
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:115-134
interface _PathJail {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:116-116
  In source order: Retain source documentation literal source_literal_116_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:118-134
  // Source signature: _resolve_path(self, key: str) -> Path
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _resolve_path(self, key) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:119-120
    if (the source predicate not self.virtual_mode is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:120-120
      End this invocation with super()._resolve_path(key).
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:121-121
    In source order: Evaluate once key if key.startswith('/') else source_template_121_48; assign in source target order to vpath.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:124-126
    if (the source predicate '..' in PurePosixPath(vpath).parts or key.startswith('~') is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:125-125
      In source order: Evaluate COUNTERS.bump('deepagents_path_jail_refused'); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:126-126
      Raise PermissionError(_JAIL_ERROR.format(path=key)).
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:127-127
    In source order: Evaluate once (self.cwd / vpath.lstrip('/')).resolve(); assign in source target order to full.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:128-132
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:129-129
      In source order: Evaluate full.relative_to(self.cwd); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:130-132
    On the first matching source exception ValueError, in handler order {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:131-131
      In source order: Evaluate COUNTERS.bump('deepagents_path_jail_refused'); retain side effects and discard the expression result.
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:132-132
      Raise PermissionError(_JAIL_ERROR.format(path=key)) with explicit source cause None.
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:133-133
    In source order: Evaluate _raise_if_symlink_loop(full); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:134-134
    End this invocation with full.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:137-218
interface _ScopedReadBackend {
  Describe the source Python type, preserving its base/metaclass expression order: _PathJail, _NoWriteBackend.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:141-143
  // Source signature: _scope(self) -> frozenset[str] | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _scope(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:142-142
    In source order: Retain source documentation literal source_literal_142_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:143-143
    End this invocation with _scan_scope._scope_for(self.cwd).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:145-151
  // Source signature: _rel_of(self, file_path: str) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _rel_of(self, file_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:146-146
    In source order: Retain source documentation literal source_literal_146_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:148-151
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:149-149
      End this invocation with self._resolve_path(file_path).relative_to(self.cwd).as_posix().
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:150-151
    On the first matching source exception (ValueError, OSError, RuntimeError), in handler order {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:151-151
      End this invocation with None.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:153-158
  // Source signature: read(self, file_path: str, offset: int=0, limit: int=2000) -> ReadResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn read(self, file_path, offset, limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:154-154
    In source order: Evaluate once self._rel_of(file_path); assign in source target order to rel.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:156-157
    if (the source predicate rel is not None and rel != '.' and _scan_scope._excluded_rel(rel, self._scope()) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:157-157
      End this invocation with ReadResult(error=_scan_scope._SCOPE_ERROR.format(path=file_path)).
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:158-158
    End this invocation with super().read(file_path, offset, limit).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:160-192
  // Source signature: grep(self, pattern: str, path: str | None=None, glob: str | None=None, *, max_count: int | None=None, context_lines: int=0) -> GrepResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn grep(self, pattern, path, glob, max_count, context_lines) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:169-169
    In source order: Evaluate once self._scope(); assign in source target order to scope.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:170-181
    if (the source predicate path is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:172-172
      In source order: Evaluate once self._rel_of(path); assign in source target order to rel.
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:173-181
      if (the source predicate rel is not None and rel != '.' and (self.cwd / rel).is_file() and _scan_scope._excluded_rel(rel, scope) is truthy) {
        // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:179-181
        End this invocation with GrepResult(error=_scan_scope._SCOPE_ERROR.format(path=path), matches=[]).
      }
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:182-184
    In source order: Evaluate once super().grep(pattern, path, glob, max_count=max_count, context_lines=context_lines); assign in source target order to result.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:185-191
    if (the source predicate result.matches is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:187-191
      In source order: Evaluate once [m for m in result.matches if not _scan_scope._excluded_rel(m['path'].lstrip('/'), scope)]; assign in source target order to result.matches.
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:192-192
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:194-203
  // Source signature: glob(self, pattern: str, path: str | None=None) -> GlobResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn glob(self, pattern, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:195-195
    In source order: Evaluate once super().glob(pattern, path); assign in source target order to result.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:196-202
    if (the source predicate result.matches is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:197-202
      In source order: Evaluate once self._scope(); assign in source target order to scope. Then Evaluate once [m for m in result.matches if not _scan_scope._excluded_rel(m['path'].lstrip('/'), scope)]; assign in source target order to result.matches.
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:203-203
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:205-209
  // Source signature: _entry_excluded(self, entry: FileInfo, scope: frozenset[str] | None) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _entry_excluded(self, entry, scope) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:206-206
    In source order: Evaluate once entry['path'].strip('/'); assign in source target order to rel.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:207-208
    if (the source predicate not entry.get('is_dir') is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:208-208
      End this invocation with bool(rel) and _scan_scope._excluded_rel(rel, scope).
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:209-209
    End this invocation with _dir_excluded(rel, scope).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:211-218
  // Source signature: ls(self, path: str) -> LsResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ls(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:212-212
    In source order: Evaluate once super().ls(path); assign in source target order to result.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:213-217
    if (the source predicate result.entries is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:214-217
      In source order: Evaluate once self._scope(); assign in source target order to scope. Then Evaluate once [e for e in result.entries if not self._entry_excluded(e, scope)]; assign in source target order to result.entries.
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:218-218
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:221-228
// Source signature: _dir_excluded(rel: str, scope: frozenset[str] | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dir_excluded(rel, scope) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:222-222
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:223-224
  if (the source predicate any((part.lower() in _scan_scope._ALWAYS_EXCLUDED_DIRS for part in rel.split('/'))) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:224-224
    End this invocation with True.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:226-227
  if (the source predicate _scan_scope._always_allowed(rel + '/') is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:227-227
    End this invocation with False.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:228-228
  End this invocation with bool(rel) and scope is not None and (rel not in _in_scope_dirs(scope)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:231-232
interface _ShellScopedReadBackend {
  Describe the source Python type, preserving its base/metaclass expression order: _ScopedReadBackend, LocalShellBackend.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:232-232
  In source order: Retain source documentation literal source_literal_232_4; it is not a model call.
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:235-239
// Source signature: _shell_composite(cwd: str) -> CompositeBackend
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shell_composite(cwd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:236-238
  In source order: Retain source documentation literal source_literal_236_4; it is not a model call. Then Evaluate once _ShellScopedReadBackend(root_dir=cwd, virtual_mode=True, inherit_env=False); assign in source target order to shell.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:239-239
  End this invocation with CompositeBackend(default=shell, routes={'/': shell}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:242-246
// Source signature: _scoped_backend(options: StreamingOptions) -> BackendProtocol
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scoped_backend(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:243-243
  In source order: Retain source documentation literal source_literal_243_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:244-245
  if (the source predicate getattr(options, 'allow_shell', False) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:245-245
    End this invocation with _shell_composite(options.cwd).
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:246-246
  End this invocation with _ScopedReadBackend(root_dir=options.cwd, virtual_mode=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:250-250
In source order: Evaluate once 'writes into version-control metadata (.git) are refused: {path}'; assign in source target order to _GIT_WRITE_REFUSED.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:253-287
interface _StockReadBackend {
  Describe the source Python type, preserving its base/metaclass expression order: _PathJail, FilesystemBackend.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:254-254
  In source order: Retain source documentation literal source_literal_254_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:257-260
  // Source signature: write(self, file_path: str, content: str) -> WriteResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn write(self, file_path, content) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:258-259
    if (the source predicate is_git_metadata(file_path) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:259-259
      End this invocation with WriteResult(error=_GIT_WRITE_REFUSED.format(path=file_path)).
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:260-260
    End this invocation with super().write(file_path, content).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:262-271
  // Source signature: edit(self, file_path: str, old_string: str, new_string: str, replace_all: bool=False) -> EditResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn edit(self, file_path, old_string, new_string, replace_all) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:269-270
    if (the source predicate is_git_metadata(file_path) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:270-270
      End this invocation with EditResult(error=_GIT_WRITE_REFUSED.format(path=file_path)).
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:271-271
    End this invocation with super().edit(file_path, old_string, new_string, replace_all).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:273-276
  // Source signature: delete(self, file_path: str) -> DeleteResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn delete(self, file_path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:274-275
    if (the source predicate is_git_metadata(file_path) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:275-275
      End this invocation with DeleteResult(error=_GIT_WRITE_REFUSED.format(path=file_path)).
    }
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:276-276
    End this invocation with super().delete(file_path).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:278-287
  // Source signature: upload_files(self, files: list[tuple[str, bytes]]) -> list[FileUploadResponse]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn upload_files(self, files) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:281-282
    In source order: Evaluate once [(p, c) for p, c in files if not is_git_metadata(p)]; assign in source target order to allowed. Then Evaluate once iter(super().upload_files(allowed) if allowed else []); assign in source target order to results.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:283-287
    End this invocation with [FileUploadResponse(path=p, error=_GIT_WRITE_REFUSED.format(path=p)) if is_git_metadata(p) else next(results) for p, _c in files].
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:290-303
// Source signature: _session_backend(options: OneShotOptions | StreamingOptions) -> BackendProtocol | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _session_backend(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:293-295
  In source order: Retain source documentation literal source_literal_293_4; it is not a model call. Then Evaluate _filesystem_permissions(options); retain side effects and discard the expression result.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:297-298
  if (the source predicate getattr(options, 'permitted_tool_calls', None) is not None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:298-298
    End this invocation with _scoped_backend(options).
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:300-301
  if (the source predicate isinstance(options, OneShotOptions) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:301-301
    End this invocation with _NoWriteBackend(root_dir=options.cwd, virtual_mode=True).
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:303-303
  End this invocation with _StockReadBackend(root_dir=options.cwd, virtual_mode=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:307-334
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:306-306
Before creating this callable, evaluate and retain decorators top-to-bottom: contextlib.contextmanager.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:307-334
// Source signature: patched_read_timeouts(seconds: float | None)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn patched_read_timeouts(seconds) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:308-308
  In source order: Retain source documentation literal source_literal_308_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:309-311
  if (the source predicate seconds is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:310-310
    In source order: Yield None; suspend this generator until resumed.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:311-311
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:312-321
  In source order: Evaluate once _deepagents_filesystem; assign in source target order to mod. Then Evaluate once int(seconds); assign in source target order to grep_timeout. Then Evaluate once 2 * grep_timeout + 5; assign in source target order to async_grep_timeout. Then Evaluate once mod.FilesystemBackend._python_search.__kwdefaults__; assign in source target order to python_search_defaults. Then Evaluate once (mod._DEFAULT_GLOB_TIMEOUT, mod.DEFAULT_GREP_TIMEOUT, mod.ASYNC_GREP_TIMEOUT, python_search_defaults['timeout']); assign in source target order to originals.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:322-334
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:323-327
    In source order: Evaluate once seconds; assign in source target order to mod._DEFAULT_GLOB_TIMEOUT. Then Evaluate once grep_timeout; assign in source target order to mod.DEFAULT_GREP_TIMEOUT. Then Evaluate once async_grep_timeout; assign in source target order to mod.ASYNC_GREP_TIMEOUT. Then Evaluate once grep_timeout; assign in source target order to python_search_defaults['timeout']. Then Yield None; suspend this generator until resumed.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:329-334
    In source order: Evaluate once originals; assign in source target order to (mod._DEFAULT_GLOB_TIMEOUT, mod.DEFAULT_GREP_TIMEOUT, mod.ASYNC_GREP_TIMEOUT, python_search_defaults['timeout']).
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/deepagents/options/filesystem.py:337-346
// Source signature: _skill_sources(skill_root: Path | None, cwd: Path) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _skill_sources(skill_root, cwd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:338-338
  In source order: Retain source documentation literal source_literal_338_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:339-340
  if (the source predicate skill_root is None or not skill_root.is_dir() is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:340-340
    End this invocation with [].
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:341-341
  In source order: Evaluate once (skill_root.resolve(), cwd.resolve()); assign in source target order to (root, base).
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:342-344
  if (the source predicate not root.is_relative_to(base) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:343-343
    In source order: Evaluate once source_template_343_14; assign in source target order to msg.
    // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:344-344
    Raise ValueError(msg).
  }
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:345-345
  In source order: Evaluate once root.relative_to(base).as_posix(); assign in source target order to relative.
  // Source: vvaharness/backends/harness/deepagents/options/filesystem.py:346-346
  End this invocation with [source_template_346_12 if relative != '.' else '/'].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.models import GIT_INTERNALS_DENY, READ_ONLY_PERMISSIONS` at source line 43: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.models import OneShotOptions, StreamingOptions` at source line 47: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _scan_scope` at source line 48: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import tools as _scan_scope` at source line 48: `source_detail/vvaharness/backends/llm/tools.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 49: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.git_paths import is_git_metadata` at source line 50: `source_detail/vvaharness/util/git_paths.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vvaharness/backends/harness/deepagents/options/filesystem.py.sudo.md). Exact strings in the evidence asset support this conversion.
