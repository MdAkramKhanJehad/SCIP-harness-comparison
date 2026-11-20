# vvaharness/pipeline/stages/s9_sarif.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s9_sarif.py.evidence.json`. SHA-256: `58450e138cc657e2577301b9d5687f5971a6add9086a25aa79af6e7e03bb31c0`.

```sudo
// Source: vvaharness/pipeline/stages/s9_sarif.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import FinalReport; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s9.typed_sarif import write_sarif; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s9_sarif.py:23-23
In source order: Resolve source import from vvaharness.report.appcontext import AppInfo; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s9_sarif.py:26-31
// Source signature: run(report: FinalReport, sarif_path: Path, *, application_id: str | None=None, app_info: AppInfo | None=None, cfg=None) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(report, sarif_path, application_id, app_info, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s9_sarif.py:29-29
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s9_sarif.py:31-31
  End this invocation with write_sarif(report, sarif_path, application_id, app_info, cfg=cfg).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import FinalReport` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s9.typed_sarif import write_sarif` at source line 22: `source_detail/vvaharness/pipeline/stages/s9/typed_sarif.py.sudo.md`.
- `from vvaharness.report.appcontext import AppInfo` at source line 23: `source_detail/vvaharness/report/appcontext.py.sudo.md`.
