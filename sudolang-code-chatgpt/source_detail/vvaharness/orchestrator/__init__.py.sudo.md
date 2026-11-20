# vvaharness/orchestrator/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/__init__.py.evidence.json`. SHA-256: `0d7e44a356f5041055840de79697eb513fb5756bb3f49c249eeed4f728e48236`.

```sudo
// Source: vvaharness/orchestrator/__init__.py:16-24
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Retain source documentation literal source_literal_18_0; it is not a model call. Then Resolve source import import shutil as shutil; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.batch import run_batch as run_batch; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import load_ckpt as load_ckpt; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/__init__.py:25-37
In source order: Resolve source import from vvaharness.orchestrator.checkpoints import run_id_for as run_id_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import save_ckpt as save_ckpt; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import _default_config as _default_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import trusted_config as trusted_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.entry import main as main; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/__init__.py:38-52
In source order: Resolve source import from vvaharness.orchestrator.preflight import _mask as _mask; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.preflight import _reachable_despite_token_cap as _reachable_despite_token_cap; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.preflight import _reachable_despite_truncated_reply as _reachable_despite_truncated_reply; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.preflight import check_backends as check_backends; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.preflight import configure_backends as configure_backends; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/__init__.py:53-56
In source order: Resolve source import from vvaharness.orchestrator.preflight import probe_backends as probe_backends; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.scan import scan_repo as scan_repo; preserve alias and import-time effects.
```

## Local import links

- `from vvaharness.orchestrator.batch import run_batch as run_batch` at source line 21: `source_detail/vvaharness/orchestrator/batch.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import load_ckpt as load_ckpt` at source line 22: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import run_id_for as run_id_for` at source line 25: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import save_ckpt as save_ckpt` at source line 28: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _default_config as _default_config` at source line 31: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import trusted_config as trusted_config` at source line 34: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.orchestrator.entry import main as main` at source line 37: `source_detail/vvaharness/orchestrator/entry.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import _mask as _mask` at source line 38: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import _reachable_despite_token_cap as _reachable_despite_token_cap` at source line 41: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import _reachable_despite_truncated_reply as _reachable_despite_truncated_reply` at source line 44: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import check_backends as check_backends` at source line 47: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import configure_backends as configure_backends` at source line 50: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import probe_backends as probe_backends` at source line 53: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.
- `from vvaharness.orchestrator.scan import scan_repo as scan_repo` at source line 56: `source_detail/vvaharness/orchestrator/scan.py.sudo.md`.
