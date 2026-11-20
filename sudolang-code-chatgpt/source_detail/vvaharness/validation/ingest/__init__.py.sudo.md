# vvaharness/validation/ingest/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/ingest/__init__.py.evidence.json`. SHA-256: `30b7ba245c2a9ddaf52f83539bd42c15df7a8284bd93ddf623c2efd0f4b855ca`.

```sudo
// Source: vvaharness/validation/ingest/__init__.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.case_loader import LoadedCase, discover_cases, load_case, select_cases; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.errors import IngestError; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.manifest_builder import build_manifest; preserve alias and import-time effects.
// Source: vvaharness/validation/ingest/__init__.py:27-41
In source order: Resolve source import from vvaharness.validation.ingest.workspace import assert_remediation_applied, stage_workspace; preserve alias and import-time effects. Then Evaluate once ['IngestError', 'LoadedCase', 'assert_remediation_applied', 'build_manifest', 'discover_cases', 'load_case', 'select_cases', 'stage_workspace']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.validation.ingest.case_loader import LoadedCase, discover_cases, load_case, select_cases` at source line 19: `source_detail/vvaharness/validation/ingest/case_loader.py.sudo.md`.
- `from vvaharness.validation.ingest.errors import IngestError` at source line 25: `source_detail/vvaharness/validation/ingest/errors.py.sudo.md`.
- `from vvaharness.validation.ingest.manifest_builder import build_manifest` at source line 26: `source_detail/vvaharness/validation/ingest/manifest_builder.py.sudo.md`.
- `from vvaharness.validation.ingest.workspace import assert_remediation_applied, stage_workspace` at source line 27: `source_detail/vvaharness/validation/ingest/workspace.py.sudo.md`.
