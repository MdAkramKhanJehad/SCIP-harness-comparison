# vvaharness/evidence/manifests.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/manifests.py.evidence.json`. SHA-256: `4134ceb515aec640fe6cea858f6ffaae308c3bbc47fd99d6fa0ff4d24c714112`.

```sudo
// Source: vvaharness/evidence/manifests.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import tomllib; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/evidence/manifests.py:22-27
In source order: Resolve source import from vvaharness.evidence._grouping import _round_robin_select; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.read import _cap_text, _contained, _read_capped; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import _DEFAULT_EXCLUDE_DIRS, _has_target_build_marker; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/evidence/manifests.py:29-42
In source order: Evaluate once ('package.json', 'pom.xml', 'build.gradle', 'build.gradle.kts', 'setup.py', 'pyproject.toml', 'requirements.txt', 'go.mod', 'Cargo.toml', 'Gemfile', 'composer.json', 'Dockerfile', 'docker-compose.yml', 'docker-compose.yaml', '.csproj'); assign in source target order to _MANIFEST_CANDIDATES. Then Evaluate once 500000; assign in source target order to _MANIFEST_RAW_CEILING. Then Evaluate once ('name', 'version', 'dependencies', 'devDependencies', 'peerDependencies', 'require', 'require-dev', 'scripts'); assign in source target order to _PACKAGE_JSON_KEYS. Then Evaluate once ('name', 'version', 'dependencies', 'optional-dependencies'); assign in source target order to _PYPROJECT_PROJECT_KEYS.
// Source: vvaharness/evidence/manifests.py:45-55
// Source signature: _truncate_package_json(raw: str, cap: int) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _truncate_package_json(raw, cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:46-46
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call.
  // Source: vvaharness/evidence/manifests.py:47-51
  Perform the following protected operations {
    // Source: vvaharness/evidence/manifests.py:48-48
    In source order: Evaluate once json.loads(raw); assign in source target order to data.
  }
  // Source: vvaharness/evidence/manifests.py:49-51
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/evidence/manifests.py:50-50
    In source order: Evaluate log.debug('manifest structural truncation: unparseable JSON', exc_info=True); retain side effects and discard the expression result.
    // Source: vvaharness/evidence/manifests.py:51-51
    End this invocation with None.
  }
  // Source: vvaharness/evidence/manifests.py:52-53
  if (the source predicate not isinstance(data, dict) is truthy) {
    // Source: vvaharness/evidence/manifests.py:53-53
    End this invocation with None.
  }
  // Source: vvaharness/evidence/manifests.py:54-54
  In source order: Evaluate once {k: v for k, v in data.items() if k in _PACKAGE_JSON_KEYS}; assign in source target order to keep.
  // Source: vvaharness/evidence/manifests.py:55-55
  End this invocation with _cap_text(json.dumps(keep, indent=2, sort_keys=True), cap) if keep else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:58-70
// Source signature: _pyproject_keep(data: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pyproject_keep(data) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:59-61
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then For keep, assign {}; source annotation dict. Then Evaluate once data.get('project') if isinstance(data, dict) else None; assign in source target order to project.
  // Source: vvaharness/evidence/manifests.py:62-65
  if (the source predicate isinstance(project, dict) is truthy) {
    // Source: vvaharness/evidence/manifests.py:63-63
    In source order: Evaluate once {k: v for k, v in project.items() if k in _PYPROJECT_PROJECT_KEYS}; assign in source target order to sub.
    // Source: vvaharness/evidence/manifests.py:64-65
    if (the source predicate sub is truthy) {
      // Source: vvaharness/evidence/manifests.py:65-65
      In source order: Evaluate once sub; assign in source target order to keep['project'].
    }
  }
  // Source: vvaharness/evidence/manifests.py:66-67
  In source order: Evaluate once data.get('tool') if isinstance(data, dict) else None; assign in source target order to tool. Then Evaluate once tool.get('poetry') if isinstance(tool, dict) else None; assign in source target order to poetry.
  // Source: vvaharness/evidence/manifests.py:68-69
  if (the source predicate isinstance(poetry, dict) and 'dependencies' in poetry is truthy) {
    // Source: vvaharness/evidence/manifests.py:69-69
    In source order: Evaluate once {'poetry': {'dependencies': poetry['dependencies']}}; assign in source target order to keep['tool'].
  }
  // Source: vvaharness/evidence/manifests.py:70-70
  End this invocation with keep.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:73-81
// Source signature: _truncate_pyproject_toml(raw: str, cap: int) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _truncate_pyproject_toml(raw, cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:74-74
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call.
  // Source: vvaharness/evidence/manifests.py:75-79
  Perform the following protected operations {
    // Source: vvaharness/evidence/manifests.py:76-76
    In source order: Evaluate once tomllib.loads(raw); assign in source target order to data.
  }
  // Source: vvaharness/evidence/manifests.py:77-79
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/evidence/manifests.py:78-78
    In source order: Evaluate log.debug('manifest structural truncation: unparseable TOML', exc_info=True); retain side effects and discard the expression result.
    // Source: vvaharness/evidence/manifests.py:79-79
    End this invocation with None.
  }
  // Source: vvaharness/evidence/manifests.py:80-80
  In source order: Evaluate once _pyproject_keep(data); assign in source target order to keep.
  // Source: vvaharness/evidence/manifests.py:81-81
  End this invocation with _cap_text(json.dumps(keep, indent=2, sort_keys=True, default=str), cap) if keep else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:84-88
In source order: Evaluate once {'package.json': _truncate_package_json, 'composer.json': _truncate_package_json, 'pyproject.toml': _truncate_pyproject_toml}; assign in source target order to _TRUNCATORS.
// Source: vvaharness/evidence/manifests.py:91-95
// Source signature: _structural_truncate(kind: str, raw: str, cap: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _structural_truncate(kind, raw, cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:92-94
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call. Then Evaluate once _TRUNCATORS.get(kind); assign in source target order to truncate. Then Evaluate once truncate(raw, cap) if truncate else None; assign in source target order to kept.
  // Source: vvaharness/evidence/manifests.py:95-95
  End this invocation with kept if kept is not None else _cap_text(raw, cap).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:98-110
// Source signature: _apply_manifest_total_cap(manifests: list[tuple[str, str]], total_cap: int) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_manifest_total_cap(manifests, total_cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:100-102
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then For out, assign []; source annotation list[tuple[str, str]]. Then Evaluate once total_cap; assign in source target order to remaining.
  // Source: vvaharness/evidence/manifests.py:103-109
  for each (name, text) in manifests {
    // Source: vvaharness/evidence/manifests.py:104-105
    if (the source predicate remaining <= 0 is truthy) {
      // Source: vvaharness/evidence/manifests.py:105-105
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/evidence/manifests.py:106-107
    if (the source predicate len(text) > remaining is truthy) {
      // Source: vvaharness/evidence/manifests.py:107-107
      In source order: Evaluate once _cap_text(text, remaining); assign in source target order to text.
    }
    // Source: vvaharness/evidence/manifests.py:108-109
    In source order: Evaluate out.append((name, text)); retain side effects and discard the expression result. Then Apply source augmented assignment remaining -= len(text) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/evidence/manifests.py:110-110
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:113-124
// Source signature: _dir_manifest_hits(root: Path, d: Path) -> dict[str, list[Path]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dir_manifest_hits(root, d) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:114-115
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call. Then For hits, assign {}; source annotation dict[str, list[Path]].
  // Source: vvaharness/evidence/manifests.py:116-123
  for each name in _MANIFEST_CANDIDATES {
    // Source: vvaharness/evidence/manifests.py:117-117
    In source order: Evaluate once sorted(d.glob(source_template_117_35)) if name.startswith('.') else [d / name]; assign in source target order to candidates.
    // Source: vvaharness/evidence/manifests.py:118-123
    for each p in candidates {
      // Source: vvaharness/evidence/manifests.py:120-121
      if (the source predicate p.is_symlink() is truthy) {
        // Source: vvaharness/evidence/manifests.py:121-121
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/evidence/manifests.py:122-123
      if (the source predicate p.is_file() and _contained(root, p) is not None is truthy) {
        // Source: vvaharness/evidence/manifests.py:123-123
        In source order: Evaluate hits.setdefault(name, []).append(p); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/evidence/manifests.py:124-124
  End this invocation with hits.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:127-147
// Source signature: _walkable_children(d: Path) -> list[Path]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _walkable_children(d) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:128-135
  In source order: Retain source documentation literal source_literal_128_4; it is not a model call.
  // Source: vvaharness/evidence/manifests.py:136-139
  Perform the following protected operations {
    // Source: vvaharness/evidence/manifests.py:137-137
    In source order: Evaluate once sorted((c for c in d.iterdir() if c.is_dir())); assign in source target order to children.
  }
  // Source: vvaharness/evidence/manifests.py:138-139
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/evidence/manifests.py:139-139
    End this invocation with [].
  }
  // Source: vvaharness/evidence/manifests.py:140-147
  End this invocation with [c for c in children if not c.is_symlink() and (c.name not in _DEFAULT_EXCLUDE_DIRS or (c.name == 'target' and (not _has_target_build_marker(d, []))))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:150-158
// Source signature: _walk_for_manifests(root: Path, d: Path, depth: int, max_depth: int, hits_by_kind: dict[str, list[Path]]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _walk_for_manifests(root, d, depth, max_depth, hits_by_kind) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:152-152
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call.
  // Source: vvaharness/evidence/manifests.py:153-154
  for each (name, paths) in _dir_manifest_hits(root, d).items() {
    // Source: vvaharness/evidence/manifests.py:154-154
    In source order: Evaluate hits_by_kind.setdefault(name, []).extend(paths); retain side effects and discard the expression result.
  }
  // Source: vvaharness/evidence/manifests.py:155-156
  if (the source predicate depth >= max_depth is truthy) {
    // Source: vvaharness/evidence/manifests.py:156-156
    End this invocation with None.
  }
  // Source: vvaharness/evidence/manifests.py:157-158
  for each child in _walkable_children(d) {
    // Source: vvaharness/evidence/manifests.py:158-158
    In source order: Evaluate _walk_for_manifests(root, child, depth + 1, max_depth, hits_by_kind); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:161-169
// Source signature: _find_manifests(root: Path, max_depth: int, max_total: int, max_per_kind: int) -> list[tuple[str, Path]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_manifests(root, max_depth, max_total, max_per_kind) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:163-165
  In source order: Retain source documentation literal source_literal_163_4; it is not a model call. Then For hits_by_kind, assign {}; source annotation dict[str, list[Path]]. Then Evaluate _walk_for_manifests(root, root, 0, max_depth, hits_by_kind); retain side effects and discard the expression result.
  // Source: vvaharness/evidence/manifests.py:166-167
  for each kind in hits_by_kind {
    // Source: vvaharness/evidence/manifests.py:167-167
    In source order: Evaluate once hits_by_kind[kind][:max_per_kind]; assign in source target order to hits_by_kind[kind].
  }
  // Source: vvaharness/evidence/manifests.py:168-168
  In source order: Evaluate once [k for k in _MANIFEST_CANDIDATES if k in hits_by_kind]; assign in source target order to ordered_kinds.
  // Source: vvaharness/evidence/manifests.py:169-169
  End this invocation with _round_robin_select(hits_by_kind, max_total, keys=ordered_kinds).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:172-176
// Source signature: _manifest_relpath(root: Path, p: Path) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _manifest_relpath(root, p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:173-176
  Perform the following protected operations {
    // Source: vvaharness/evidence/manifests.py:174-174
    End this invocation with str(p.relative_to(root)).replace('\\', '/').
  }
  // Source: vvaharness/evidence/manifests.py:175-176
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/evidence/manifests.py:176-176
    End this invocation with str(p).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/manifests.py:179-190
// Source signature: gather_manifests(root: Path, walk_bounds: tuple[int, int, int], manifest_cap: int, manifest_total_cap: int) -> list[tuple[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gather_manifests(root, walk_bounds, manifest_cap, manifest_total_cap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/manifests.py:181-183
  In source order: Retain source documentation literal source_literal_181_4; it is not a model call. Then Evaluate once walk_bounds; assign in source target order to (max_depth, max_total, max_per_kind). Then For manifests_struct, assign []; source annotation list[tuple[str, str]].
  // Source: vvaharness/evidence/manifests.py:184-189
  for each (kind, p) in _find_manifests(root, max_depth, max_total, max_per_kind) {
    // Source: vvaharness/evidence/manifests.py:185-185
    In source order: Evaluate once _read_capped(root, p, _MANIFEST_RAW_CEILING); assign in source target order to raw.
    // Source: vvaharness/evidence/manifests.py:186-187
    if (the source predicate not raw is truthy) {
      // Source: vvaharness/evidence/manifests.py:187-187
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/evidence/manifests.py:188-189
    In source order: Evaluate once _manifest_relpath(root, p); assign in source target order to relpath. Then Evaluate manifests_struct.append((relpath, _structural_truncate(kind, raw, manifest_cap))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/evidence/manifests.py:190-190
  End this invocation with _apply_manifest_total_cap(manifests_struct, manifest_total_cap).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.evidence._grouping import _round_robin_select` at source line 22: `source_detail/vvaharness/evidence/_grouping.py.sudo.md`.
- `from vvaharness.evidence.read import _cap_text, _contained, _read_capped` at source line 23: `source_detail/vvaharness/evidence/read.py.sudo.md`.
- `from vvaharness.scope import _DEFAULT_EXCLUDE_DIRS, _has_target_build_marker` at source line 24: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/logs.py.sudo.md`.
