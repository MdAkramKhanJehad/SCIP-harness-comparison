# vvaharness/scope/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/scope/__init__.py.evidence.json`. SHA-256: `4a519750e52dae1321bd588807c4bd1d76c3a803690327f4e1a1d00fe01401c3`.

```sudo
// Source: vvaharness/scope/__init__.py:15-64
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope.configs import _dedup_configs, _flatten_keys, _rep_score, _shape_hash, _suspicious_set; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope.walk import _DEDUP_DEFAULTS, _DEFAULT_EXCLUDE_DIRS, _DEFAULT_EXCLUDE_EXTS, _DEFAULT_EXCLUDE_GLOBS, _INSECURE_RX, _SECRET_RX, EmptyScopeError, _exclusion_sets, _has_target_build_marker, _norm_rel, _resolve_scope_path, _walk_repo, glob_hit, resolve_inventory_path, scope_after; preserve alias and import-time effects. Then Evaluate once ['_DEDUP_DEFAULTS', '_DEFAULT_EXCLUDE_DIRS', '_DEFAULT_EXCLUDE_EXTS', '_DEFAULT_EXCLUDE_GLOBS', '_INSECURE_RX', '_SECRET_RX', 'EmptyScopeError', '_dedup_configs', '_exclusion_sets', '_flatten_keys', '_has_target_build_marker', '_norm_rel', '_rep_score', '_resolve_scope_path', '_shape_hash', '_suspicious_set', '_walk_repo', 'glob_hit', 'resolve_inventory_path', 'scope_after']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.scope.configs import _dedup_configs, _flatten_keys, _rep_score, _shape_hash, _suspicious_set` at source line 18: `source_detail/vvaharness/scope/configs.py.sudo.md`.
- `from vvaharness.scope.walk import _DEDUP_DEFAULTS, _DEFAULT_EXCLUDE_DIRS, _DEFAULT_EXCLUDE_EXTS, _DEFAULT_EXCLUDE_GLOBS, _INSECURE_RX, _SECRET_RX, EmptyScopeError, _exclusion_sets, _has_target_build_marker, _norm_rel, _resolve_scope_path, _walk_repo, glob_hit, resolve_inventory_path, scope_after` at source line 25: `source_detail/vvaharness/scope/walk.py.sudo.md`.
