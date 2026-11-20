# vvaharness/pipeline/stages/s11_validate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s11_validate.py.evidence.json`. SHA-256: `5d8882ea4ffe650ca9208d0177a1520f72f9c8a7b447d153f6bfc2d3e3004e51`.

```sudo
// Source: vvaharness/pipeline/stages/s11_validate.py:14-19
In source order: Retain source documentation literal source_literal_14_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import MutableMapping; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s11_validate.py:21-22
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/pipeline/stages/s11_validate.py:22-22
  In source order: Resolve source import from vvaharness.config import Config; preserve alias and import-time effects.
}
// Source: vvaharness/pipeline/stages/s11_validate.py:25-53
// Source signature: run(repo: Path | str, *, cfg: Config, config_path: str, finding_ids: list[str] | None=None, resume: bool=False, report_md: Path | str | None=None, progress: MutableMapping[str, int] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(repo, cfg, config_path, finding_ids, resume, report_md, progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s11_validate.py:35-37
  In source order: Retain source documentation literal source_literal_35_4; it is not a model call. Then Resolve source import from vvaharness.validation.cli import main as validate_main; preserve alias and import-time effects. Then Evaluate once ['--repo', str(repo)]; assign in source target order to argv.
  // Source: vvaharness/pipeline/stages/s11_validate.py:38-40
  for each (flag, value) in (('--config', config_path), ('--scan-report', report_md)) {
    // Source: vvaharness/pipeline/stages/s11_validate.py:39-40
    if (the source predicate value is truthy) {
      // Source: vvaharness/pipeline/stages/s11_validate.py:40-40
      In source order: Apply source augmented assignment argv += [flag, str(value)] with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/pipeline/stages/s11_validate.py:41-42
  for each finding_id in finding_ids or () {
    // Source: vvaharness/pipeline/stages/s11_validate.py:42-42
    In source order: Apply source augmented assignment argv += ['--finding', finding_id] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s11_validate.py:43-44
  if (the source predicate resume is truthy) {
    // Source: vvaharness/pipeline/stages/s11_validate.py:44-44
    In source order: Evaluate argv.append('--resume'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s11_validate.py:45-46
  In source order: Evaluate once validate_main(argv, progress=progress) if progress is not None else validate_main(argv); assign in source target order to code.
  // Source: vvaharness/pipeline/stages/s11_validate.py:48-52
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s11_validate.py:49-50
    In source order: Resolve source import from vvaharness.orchestrator import case_rollup; preserve alias and import-time effects. Then Evaluate case_rollup.record(repo); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s11_validate.py:51-52
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/pipeline/stages/s11_validate.py:52-52
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/pipeline/stages/s11_validate.py:53-53
  End this invocation with code.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.config import Config` at source line 22: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.validation.cli import main as validate_main` at source line 36: `source_detail/vvaharness/validation/cli/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import case_rollup` at source line 49: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import case_rollup` at source line 49: `source_detail/vvaharness/orchestrator/case_rollup.py.sudo.md`.
