# vvaharness/scope/walk.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/scope/walk.py.evidence.json`. SHA-256: `73ce3d0a3965a91071504b09f6504b17c1de7d64f7322d80ef1e4ebe89003ea4`.

```sudo
// Source: vvaharness/scope/walk.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import fnmatch; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections.abc import Collection; preserve alias and import-time effects.
// Source: vvaharness/scope/walk.py:21-27
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from types import SimpleNamespace; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/scope/walk.py:29-30
interface EmptyScopeError {
  Describe the source Python type, preserving its base/metaclass expression order: RuntimeError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/scope/walk.py:30-30
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call.
}
// Source: vvaharness/scope/walk.py:34-68
In source order: Evaluate once {'.git', '.hg', '.svn', 'node_modules', '__pycache__', '.venv', 'venv', 'dist', 'build', '.idea', '.vscode', 'target', 'vendor', '.terraform', '.next', '.nuxt', 'coverage', '.pytest_cache', '.mypy_cache', 'test', 'tests', '__tests__', '__test__', 'e2e', 'testdata', 'fixtures', '__fixtures__', 'mocks', '__mocks__', 'stubs', 'checkpoints', 'security-scan', 'security-remediation', '.vvaharness'}; assign in source target order to _DEFAULT_EXCLUDE_DIRS. Then Evaluate once {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.pdf', '.zip', '.gz', '.tar', '.7z', '.jar', '.war', '.class', '.exe', '.dll', '.so', '.dylib', '.bin', '.o', '.a', '.obj', '.pyc', '.pyo', '.pkl', '.lock', '.min.js', '.map', '.woff', '.woff2', '.ttf', '.eot', '.mp4', '.mp3', '.wav'}; assign in source target order to _DEFAULT_EXCLUDE_EXTS. Then Evaluate once ('**/test_*.py', '**/*_test.py', '**/conftest.py', '**/*_test.go', '**/*.test.js', '**/*.test.ts', '**/*.test.jsx', '**/*.test.tsx', '**/*.spec.js', '**/*.spec.ts', '**/*.spec.jsx', '**/*.spec.tsx', '**/*Test.java', '**/*Tests.java', '**/*IT.java', '**/*Test.cs', '**/*Tests.cs', '**/*Test.kt', '**/.gitignore', '**/.gitattributes', '**/.gitmodules', '**/.gitkeep', '**/.editorconfig', '**/.dockerignore', '**/.npmignore', '**/.eslintignore', '**/.prettierignore', '**/.mailmap', '**/CODEOWNERS', '**/.DS_Store', '**/LICENSE', '**/LICENSE.*', '**/NOTICE'); assign in source target order to _DEFAULT_EXCLUDE_GLOBS. Then Evaluate once ('pom.xml', 'build.gradle', 'build.gradle.kts', 'Cargo.toml', 'build.sbt', 'project.clj'); assign in source target order to _TARGET_BUILD_MARKERS.
// Source: vvaharness/scope/walk.py:71-77
// Source signature: _has_target_build_marker(root: Path, parent_parts: list[str]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _has_target_build_marker(root, parent_parts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:72-76
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once root.joinpath(*parent_parts) if parent_parts else root; assign in source target order to parent.
  // Source: vvaharness/scope/walk.py:77-77
  End this invocation with any(((parent / marker).is_file() for marker in _TARGET_BUILD_MARKERS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:80-87
// Source signature: _exclusion_sets(cfg) -> tuple[set[str], set[str], list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _exclusion_sets(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:81-86
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call. Then Evaluate once {d.lower() for d in _DEFAULT_EXCLUDE_DIRS | set(getattr(cfg.step1, 'exclude_dirs', None) or [])}; assign in source target order to excl_dirs. Then Evaluate once _DEFAULT_EXCLUDE_EXTS | set(getattr(cfg.step1, 'exclude_exts', None) or []); assign in source target order to excl_exts. Then Evaluate once list(_DEFAULT_EXCLUDE_GLOBS) + list(getattr(cfg.step1, 'exclude_globs', None) or []); assign in source target order to excl_globs.
  // Source: vvaharness/scope/walk.py:87-87
  End this invocation with (excl_dirs, excl_exts, excl_globs).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:88-96
// Source signature: glob_hit(rel: str, globs) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn glob_hit(rel, globs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:89-90
  In source order: Retain source documentation literal source_literal_89_4; it is not a model call. Then Evaluate once rel.rsplit('/', 1)[-1]; assign in source target order to name.
  // Source: vvaharness/scope/walk.py:91-95
  for each g in globs {
    // Source: vvaharness/scope/walk.py:92-93
    if (the source predicate fnmatch.fnmatchcase(rel, g) is truthy) {
      // Source: vvaharness/scope/walk.py:93-93
      End this invocation with g.
    }
    // Source: vvaharness/scope/walk.py:94-95
    if (the source predicate g.startswith('**/') and fnmatch.fnmatchcase(name, g[3:]) is truthy) {
      // Source: vvaharness/scope/walk.py:95-95
      End this invocation with g.
    }
  }
  // Source: vvaharness/scope/walk.py:96-96
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:99-104
// Source signature: _fold_slashes(p: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fold_slashes(p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:100-101
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once p.replace('\\', '/'); assign in source target order to p.
  // Source: vvaharness/scope/walk.py:102-103
  while (the source predicate p.startswith('./') is truthy) {
    // Source: vvaharness/scope/walk.py:103-103
    In source order: Evaluate once p[2:]; assign in source target order to p.
  }
  // Source: vvaharness/scope/walk.py:104-104
  End this invocation with p.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:107-119
// Source signature: _norm_rel(repo_root: str, p: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _norm_rel(repo_root, p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:108-108
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call.
  // Source: vvaharness/scope/walk.py:109-110
  if (the source predicate not p is truthy) {
    // Source: vvaharness/scope/walk.py:110-110
    End this invocation with p.
  }
  // Source: vvaharness/scope/walk.py:111-114
  In source order: Evaluate once _fold_slashes(p); assign in source target order to p. Then Evaluate once str(Path(repo_root)).replace('\\', '/').rstrip('/') + '/'; assign in source target order to rel_root. Then Evaluate once str(Path(repo_root).resolve()).replace('\\', '/').rstrip('/') + '/'; assign in source target order to abs_root. Then Evaluate once p.lower(); assign in source target order to pl.
  // Source: vvaharness/scope/walk.py:115-117
  for each r in (abs_root, rel_root) {
    // Source: vvaharness/scope/walk.py:116-117
    if (the source predicate pl.startswith(r.lower()) is truthy) {
      // Source: vvaharness/scope/walk.py:117-117
      End this invocation with p[len(r):].
    }
  }
  // Source: vvaharness/scope/walk.py:119-119
  End this invocation with p.lstrip('/').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:122-136
// Source signature: resolve_inventory_path(repo_root: str, p: str, inventory: Collection[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_inventory_path(repo_root, p, inventory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:123-123
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call.
  // Source: vvaharness/scope/walk.py:124-125
  if (the source predicate not p is truthy) {
    // Source: vvaharness/scope/walk.py:125-125
    End this invocation with p.
  }
  // Source: vvaharness/scope/walk.py:126-126
  In source order: Evaluate once _fold_slashes(p); assign in source target order to folded.
  // Source: vvaharness/scope/walk.py:127-130
  if (the source predicate not inventory is truthy) {
    // Source: vvaharness/scope/walk.py:130-130
    End this invocation with folded.lstrip('/').
  }
  // Source: vvaharness/scope/walk.py:133-135
  for each cand in (folded, folded.lstrip('/'), folded.removeprefix(Path(repo_root).name + '/')) {
    // Source: vvaharness/scope/walk.py:134-135
    if (the source predicate cand in inventory is truthy) {
      // Source: vvaharness/scope/walk.py:135-135
      End this invocation with cand.
    }
  }
  // Source: vvaharness/scope/walk.py:136-136
  End this invocation with _norm_rel(repo_root, folded).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:139-148
// Source signature: _resolve_scope_path(path: str, repo_root: str, keep: set[str], top_dirs: list[str]) -> tuple[str | None, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_scope_path(path, repo_root, keep, top_dirs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:141-142
  In source order: Retain source documentation literal source_literal_141_4; it is not a model call. Then Evaluate once resolve_inventory_path(repo_root, path, keep); assign in source target order to rel.
  // Source: vvaharness/scope/walk.py:143-144
  if (the source predicate rel in keep is truthy) {
    // Source: vvaharness/scope/walk.py:144-144
    End this invocation with (rel, False).
  }
  // Source: vvaharness/scope/walk.py:145-145
  In source order: Evaluate once [source_template_145_15 for td in top_dirs if source_template_145_51 in keep]; assign in source target order to matches.
  // Source: vvaharness/scope/walk.py:146-147
  if (the source predicate len(matches) == 1 is truthy) {
    // Source: vvaharness/scope/walk.py:147-147
    End this invocation with (matches[0], False).
  }
  // Source: vvaharness/scope/walk.py:148-148
  End this invocation with (None, len(matches) > 1).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:151-164
// Source signature: scope_after(repo_root: str, cfg, *, dirs=(), exts=(), globs=(), max_file_kb: int | None=None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scope_after(repo_root, cfg, dirs, exts, globs, max_file_kb) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:153-163
  In source order: Retain source documentation literal source_literal_153_4; it is not a model call. Then Evaluate once _exclusion_sets(cfg); assign in source target order to (base_dirs, base_exts, base_globs). Then Evaluate once SimpleNamespace(step1=SimpleNamespace(exclude_dirs=sorted(base_dirs | {d.lower() for d in dirs}), exclude_exts=sorted(base_exts | set(exts)), exclude_globs=list(base_globs) + list(globs), max_file_kb=max_file_kb if max_file_kb is not None else getattr(cfg.step1, 'max_file_kb', 1024), follow_symlinks=False)); assign in source target order to shadow.
  // Source: vvaharness/scope/walk.py:164-164
  End this invocation with _walk_repo(repo_root, shadow)[0].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:167-257
// Source signature: _walk_repo(repo_root: str, cfg) -> tuple[list[str], dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _walk_repo(repo_root, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/walk.py:168-173
  In source order: Evaluate once Path(repo_root); assign in source target order to root. Then Evaluate once root.resolve(); assign in source target order to root_resolved. Then Evaluate once _exclusion_sets(cfg); assign in source target order to (excl_dirs, excl_exts, excl_globs). Then Evaluate once getattr(cfg.step1, 'max_file_kb', 1024); assign in source target order to max_kb. Then Evaluate once bool(getattr(cfg.step1, 'follow_symlinks', False)); assign in source target order to follow_symlinks.
  // Source: vvaharness/scope/walk.py:174-177
  if (the source predicate follow_symlinks is truthy) {
    // Source: vvaharness/scope/walk.py:175-177
    In source order: Evaluate console.write(source_literal_175_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/scope/walk.py:179-183
  In source order: For out, assign []; source annotation list[str]. Then For skipped_dirs, assign {}; source annotation dict[str, int]. Then For skipped_exts, assign {}; source annotation dict[str, int]. Then For skipped_globs, assign {}; source annotation dict[str, int]. Then For skipped_size, assign []; source annotation list[tuple[str, int]].
  // Source: vvaharness/scope/walk.py:184-185
  In source order: For skipped_symlinks, assign {}; source annotation dict[str, int]. Then For skipped_symlink_targets, assign {}; source annotation dict[str, int].
  // Source: vvaharness/scope/walk.py:187-207
  // Source signature: _rule_hit(r: str) -> tuple[dict[str, int], str] | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _rule_hit(r) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/scope/walk.py:188-196
    In source order: Retain source documentation literal source_literal_188_8; it is not a model call. Then Evaluate once r.split('/'); assign in source target order to parts. Then Evaluate once next((i for i, part in enumerate(parts[:-1]) if part.lower() in excl_dirs and (part.lower() != 'target' or _has_target_build_marker(root, parts[:i]))), None); assign in source target order to hit_idx.
    // Source: vvaharness/scope/walk.py:197-198
    if (the source predicate hit_idx is not None is truthy) {
      // Source: vvaharness/scope/walk.py:198-198
      End this invocation with (skipped_dirs, '/'.join(parts[:hit_idx + 1])).
    }
    // Source: vvaharness/scope/walk.py:199-201
    In source order: Evaluate once parts[-1].lower(); assign in source target order to name. Then Evaluate once next((e for e in excl_exts if Path(name).suffix == e or name.endswith(e)), None); assign in source target order to hit_ext.
    // Source: vvaharness/scope/walk.py:202-203
    if (the source predicate hit_ext is truthy) {
      // Source: vvaharness/scope/walk.py:203-203
      End this invocation with (skipped_exts, hit_ext).
    }
    // Source: vvaharness/scope/walk.py:204-204
    In source order: Evaluate once glob_hit(r, excl_globs); assign in source target order to hit_glob.
    // Source: vvaharness/scope/walk.py:205-206
    if (the source predicate hit_glob is truthy) {
      // Source: vvaharness/scope/walk.py:206-206
      End this invocation with (skipped_globs, hit_glob).
    }
    // Source: vvaharness/scope/walk.py:207-207
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/scope/walk.py:209-246
  for each p in root.rglob('*') {
    // Source: vvaharness/scope/walk.py:210-211
    if (the source predicate not p.is_file() is truthy) {
      // Source: vvaharness/scope/walk.py:211-211
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/scope/walk.py:212-214
    In source order: Evaluate once str(p.relative_to(root)).replace('\\', '/'); assign in source target order to rel. Then Evaluate once None; assign in source target order to tgt_rel.
    // Source: vvaharness/scope/walk.py:215-227
    if (the source predicate p.is_symlink() is truthy) {
      // Source: vvaharness/scope/walk.py:216-224
      Perform the following protected operations {
        // Source: vvaharness/scope/walk.py:217-218
        In source order: Evaluate once p.resolve(strict=False); assign in source target order to tgt. Then Evaluate once not tgt.is_relative_to(root_resolved); assign in source target order to escapes.
        // Source: vvaharness/scope/walk.py:219-220
        if (the source predicate not escapes is truthy) {
          // Source: vvaharness/scope/walk.py:220-220
          In source order: Evaluate once tgt.relative_to(root_resolved).as_posix(); assign in source target order to tgt_rel.
        }
      }
      // Source: vvaharness/scope/walk.py:221-224
      On the first matching source exception OSError as _sym_err, in handler order {
        // Source: vvaharness/scope/walk.py:222-224
        In source order: Evaluate once True; assign in source target order to escapes. Then Evaluate _errlog.log('s1', rel, _sym_err, reason='symlink_resolve_failed', note='treated as escaping — file excluded from scope'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/scope/walk.py:225-227
      if (the source predicate escapes is truthy) {
        // Source: vvaharness/scope/walk.py:226-226
        In source order: Evaluate once skipped_symlinks.get(rel, 0) + 1; assign in source target order to skipped_symlinks[rel].
        // Source: vvaharness/scope/walk.py:227-227
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    // Source: vvaharness/scope/walk.py:228-228
    In source order: Evaluate once _rule_hit(rel); assign in source target order to hit.
    // Source: vvaharness/scope/walk.py:229-232
    if (the source predicate hit is truthy) {
      // Source: vvaharness/scope/walk.py:230-231
      In source order: Evaluate once hit; assign in source target order to (bucket, key). Then Evaluate once bucket.get(key, 0) + 1; assign in source target order to bucket[key].
      // Source: vvaharness/scope/walk.py:232-232
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/scope/walk.py:234-236
    if (the source predicate tgt_rel is not None and _rule_hit(tgt_rel) is truthy) {
      // Source: vvaharness/scope/walk.py:235-235
      In source order: Evaluate once skipped_symlink_targets.get(rel, 0) + 1; assign in source target order to skipped_symlink_targets[rel].
      // Source: vvaharness/scope/walk.py:236-236
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/scope/walk.py:237-245
    Perform the following protected operations {
      // Source: vvaharness/scope/walk.py:238-238
      In source order: Evaluate once p.stat().st_size; assign in source target order to sz.
      // Source: vvaharness/scope/walk.py:239-241
      if (the source predicate sz > max_kb * 1024 is truthy) {
        // Source: vvaharness/scope/walk.py:240-240
        In source order: Evaluate skipped_size.append((rel, sz)); retain side effects and discard the expression result.
        // Source: vvaharness/scope/walk.py:241-241
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    // Source: vvaharness/scope/walk.py:242-245
    On the first matching source exception OSError as _stat_err, in handler order {
      // Source: vvaharness/scope/walk.py:243-244
      In source order: Evaluate _errlog.log('s1', rel, _stat_err, reason='stat_failed', note='file excluded from scan scope'); retain side effects and discard the expression result.
      // Source: vvaharness/scope/walk.py:245-245
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/scope/walk.py:246-246
    In source order: Evaluate out.append(rel); retain side effects and discard the expression result.
  }
  // Source: vvaharness/scope/walk.py:248-256
  In source order: Evaluate once {'dirs': skipped_dirs, 'exts': skipped_exts, 'globs': skipped_globs, 'oversize': len(skipped_size), 'oversize_files': sorted(skipped_size, key=lambda kv: -kv[1]), 'symlinks': skipped_symlinks, 'symlink_targets': skipped_symlink_targets}; assign in source target order to excluded.
  // Source: vvaharness/scope/walk.py:257-257
  End this invocation with (sorted(out), excluded).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/walk.py:262-298
In source order: Evaluate once {'enabled': True, 'exts': ('.yml', '.yaml', '.json', '.toml', '.ini', '.properties', '.conf', '.cfg', '.env'), 'min_cluster_size': 3, 'keep_per_top_dir': True, 'promote_on_secret_hit': True, 'promote_on_insecure_value': True, 'max_file_kb': 512}; assign in source target order to _DEDUP_DEFAULTS. Then Evaluate once re.compile(source_literal_275_4); assign in source target order to _SECRET_RX. Then Evaluate once re.compile(source_literal_290_4); assign in source target order to _INSECURE_RX.
```

## Local import links

- `from vvaharness.util import console, logs` at source line 24: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 24: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 24: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 25: `source_detail/vvaharness/util/errlog.py.sudo.md`.
