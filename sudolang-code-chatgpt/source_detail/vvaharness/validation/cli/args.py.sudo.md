# vvaharness/validation/cli/args.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/cli/args.py.evidence.json`. SHA-256: `14f2761c24f92fcb04b8c1f6d20b916d64faaebcd1216c9afbfe7a46f66b96e7`.

```sudo
// Source: vvaharness/validation/cli/args.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import argparse; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/args.py:23-23
In source order: Evaluate once ['ValidateArgs']; assign in source target order to __all__.
// Source: vvaharness/validation/cli/args.py:27-51
// Source: vvaharness/validation/cli/args.py:26-26
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/cli/args.py:27-51
interface ValidateArgs {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/args.py:28-33
  In source order: Retain source documentation literal source_literal_28_4; it is not a model call. Then For repo, declare without assigning a value; source annotation Path. Then For config, assign None; source annotation str | None. Then For findings, assign (); source annotation tuple[str, ...]. Then For every_validatable, assign False; source annotation bool.
  // Source: vvaharness/validation/cli/args.py:34-37
  In source order: For max_findings, assign None; source annotation int | None. Then For workspace, assign None; source annotation Path | None. Then For resume, assign False; source annotation bool. Then For scan_report, assign None; source annotation Path | None.
  // Source: vvaharness/validation/cli/args.py:40-51
  // Source: vvaharness/validation/cli/args.py:39-39
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/validation/cli/args.py:40-51
  // Source signature: of(cls, parsed: argparse.Namespace) -> ValidateArgs
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn of(cls, parsed) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/cli/args.py:41-41
    In source order: Retain source documentation literal source_literal_41_8; it is not a model call.
    // Source: vvaharness/validation/cli/args.py:42-51
    End this invocation with cls(repo=parsed.repo, config=parsed.config, findings=tuple(parsed.findings or ()), every_validatable=bool(parsed.all), max_findings=parsed.max_findings, workspace=parsed.workspace, resume=bool(parsed.resume), scan_report=parsed.scan_report).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
