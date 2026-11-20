# vvaharness/orchestrator/cmdb.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/cmdb.py.evidence.json`. SHA-256: `ec1f7a33d62dee4c036b492cf0e4ccc95ae854a503bf6e145cee518a423ddff2`.

```sudo
// Source: vvaharness/orchestrator/cmdb.py:16-22
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Retain source documentation literal source_literal_18_0; it is not a model call. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import AppProfile; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import _resolve_against; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/cmdb.py:23-26
In source order: Resolve source import from vvaharness.report import appcontext; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then For _CMDB_CSV, assign ''; source annotation str.
// Source: vvaharness/orchestrator/cmdb.py:29-30
// Source signature: _cmdb_path() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cmdb_path() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/cmdb.py:30-30
  End this invocation with _CMDB_CSV.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/cmdb.py:33-37
// Source signature: _set_cmdb_path(cfg, cfg_dir: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _set_cmdb_path(cfg, cfg_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/cmdb.py:34-37
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call. Then Bind names in module scope: _CMDB_CSV. Then Evaluate once getattr(getattr(cfg, 'inject', None), 'cmdb_file', None); assign in source target order to p. Then Evaluate once _resolve_against(cfg_dir, p) if p else ''; assign in source target order to _CMDB_CSV.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/cmdb.py:40-63
// Source signature: _load_app_profile(application_id: str | None) -> tuple[AppProfile | None, appcontext.AppInfo | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_app_profile(application_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/cmdb.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
  // Source: vvaharness/orchestrator/cmdb.py:43-44
  if (the source predicate not application_id is truthy) {
    // Source: vvaharness/orchestrator/cmdb.py:44-44
    End this invocation with (None, None).
  }
  // Source: vvaharness/orchestrator/cmdb.py:45-50
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/cmdb.py:46-47
    In source order: Evaluate once appcontext.load_cmdb_csv(_cmdb_path()); assign in source target order to cmdb. Then Evaluate once appcontext.lookup_app(application_id, cmdb, {}); assign in source target order to info.
  }
  // Source: vvaharness/orchestrator/cmdb.py:48-50
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/orchestrator/cmdb.py:49-49
    In source order: Evaluate console.write(source_template_49_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/cmdb.py:50-50
    End this invocation with (None, None).
  }
  // Source: vvaharness/orchestrator/cmdb.py:51-53
  if (the source predicate info is None is truthy) {
    // Source: vvaharness/orchestrator/cmdb.py:52-52
    In source order: Evaluate console.write(source_template_52_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/cmdb.py:53-53
    End this invocation with (None, None).
  }
  // Source: vvaharness/orchestrator/cmdb.py:54-62
  In source order: Evaluate once AppProfile(application_id=str(application_id), name=info.name, externally_facing=info.externally_facing, pci_scoped=info.pci_scoped, processes_pan=info.processes_pan, pii=info.pii, source=info.source); assign in source target order to profile.
  // Source: vvaharness/orchestrator/cmdb.py:63-63
  End this invocation with (profile, info).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import AppProfile` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _resolve_against` at source line 22: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.report import appcontext` at source line 23: `source_detail/vvaharness/report/__init__.py.sudo.md`.
- `from vvaharness.report import appcontext` at source line 23: `source_detail/vvaharness/report/appcontext.py.sudo.md`.
- `from vvaharness.util import console` at source line 24: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 24: `source_detail/vvaharness/util/console.py.sudo.md`.
