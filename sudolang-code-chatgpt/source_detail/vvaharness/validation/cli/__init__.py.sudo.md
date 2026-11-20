# vvaharness/validation/cli/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/cli/__init__.py.evidence.json`. SHA-256: `04e6898bb86e651c15c66a099e8a22a0f9574baf2c8141d8b318cab2b5cefd8b`.

```sudo
// Source: vvaharness/validation/cli/__init__.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import tempfile; preserve alias and import-time effects. Then Resolve source import from collections.abc import MutableMapping; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/__init__.py:22-28
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects. Then Resolve source import from pydantic import ValidationError; preserve alias and import-time effects. Then Resolve source import from vvaharness.config import ConfigPolicyError, is_network_path; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/__init__.py:29-37
In source order: Resolve source import from vvaharness.orchestrator import _default_config, trusted_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.cli._model import ModelEnvResult, _apply_model_env, _check_persona_vendors; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.cli._parser import _build_parser; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.cli._run import Selection, ValidationRunResult, run_validation; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/__init__.py:38-42
In source order: Resolve source import from vvaharness.validation.cli.args import ValidateArgs; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config import Config, load_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.overrides import ValidateOverrides; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.errors import IngestError; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.errors import ValidationSessionError; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/__init__.py:45-55
In source order: Evaluate once 'vvah-validate-'; assign in source target order to _WORKSPACE_PREFIX. Then Evaluate once (IngestError, ValidationSessionError, ValidationError, FileNotFoundError, OSError, yaml.YAMLError); assign in source target order to _KNOWN_ERRORS.
// Source: vvaharness/validation/cli/__init__.py:58-65
// Source signature: _resolve_selection(args: ValidateArgs, config: Config) -> Selection
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_selection(args, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:59-59
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:60-61
  if (the source predicate args.findings is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:61-61
    End this invocation with Selection(case_ids=list(args.findings), resume=args.resume).
  }
  // Source: vvaharness/validation/cli/__init__.py:62-63
  if (the source predicate args.every_validatable is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:63-63
    End this invocation with Selection(resume=args.resume).
  }
  // Source: vvaharness/validation/cli/__init__.py:64-64
  In source order: Evaluate once args.max_findings if args.max_findings is not None else config.max_findings; assign in source target order to cap.
  // Source: vvaharness/validation/cli/__init__.py:65-65
  End this invocation with Selection(max_findings=cap, resume=args.resume).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:68-74
// Source signature: _resolve_config_path(args: ValidateArgs) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_config_path(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:69-69
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:70-71
  if (the source predicate args.config is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:71-71
    End this invocation with str(args.config).
  }
  // Source: vvaharness/validation/cli/__init__.py:72-73
  In source order: Evaluate once str(_default_config()); assign in source target order to default. Then Evaluate console.write(source_template_73_18); retain side effects and discard the expression result.
  // Source: vvaharness/validation/cli/__init__.py:74-74
  End this invocation with default.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:77-79
// Source signature: _is_nonempty_dir(path: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_nonempty_dir(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:78-78
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:79-79
  End this invocation with path.is_dir() and any(path.iterdir()).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:82-90
// Source signature: _network_path_error(args: ValidateArgs) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _network_path_error(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:83-83
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:84-89
  for each (flag, path) in (('--workspace', args.workspace), ('--repo', args.repo)) {
    // Source: vvaharness/validation/cli/__init__.py:85-89
    if (the source predicate path is not None and is_network_path(path) is truthy) {
      // Source: vvaharness/validation/cli/__init__.py:86-89
      End this invocation with source_template_87_16.
    }
  }
  // Source: vvaharness/validation/cli/__init__.py:90-90
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:93-107
// Source signature: _workspace_inside_repo_error(args: ValidateArgs) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _workspace_inside_repo_error(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:94-98
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:99-100
  if (the source predicate args.workspace is None is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:100-100
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/__init__.py:101-102
  if (the source predicate not args.workspace.resolve().is_relative_to(args.repo.resolve()) is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:102-102
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/__init__.py:103-107
  End this invocation with source_template_104_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:110-117
// Source signature: _nonempty_workspace_error(args: ValidateArgs) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _nonempty_workspace_error(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:111-111
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:112-113
  if (the source predicate args.workspace is None or not _is_nonempty_dir(args.workspace) is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:113-113
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/__init__.py:114-117
  End this invocation with source_template_115_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:120-126
// Source signature: _check_path_guards(args: ValidateArgs) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_path_guards(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:121-121
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:122-126
  End this invocation with _network_path_error(args) or _workspace_inside_repo_error(args) or _nonempty_workspace_error(args).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:129-137
// Source signature: _trusted_model_env(args: ValidateArgs) -> ModelEnvResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _trusted_model_env(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:130-130
  In source order: Retain source documentation literal source_literal_130_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:131-136
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/__init__.py:132-133
    In source order: Evaluate once trusted_config(_resolve_config_path(args), args.repo, explicit=args.config is not None); assign in source target order to cfg_path.
  }
  // Source: vvaharness/validation/cli/__init__.py:134-136
  On the first matching source exception ConfigPolicyError as e, in handler order {
    // Source: vvaharness/validation/cli/__init__.py:135-135
    In source order: Evaluate console.write(source_template_135_22); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/__init__.py:136-136
    End this invocation with ModelEnvResult(2, ValidateOverrides()).
  }
  // Source: vvaharness/validation/cli/__init__.py:137-137
  End this invocation with _apply_model_env(cfg_path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:140-145
interface _WorkspacePlan {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/__init__.py:141-145
  In source order: Retain source documentation literal source_literal_141_4; it is not a model call. Then For workspace_root, declare without assigning a value; source annotation Path. Then For owns_workspace, declare without assigning a value; source annotation bool. Then For error, declare without assigning a value; source annotation str | None.
}
// Source: vvaharness/validation/cli/__init__.py:148-169
// Source signature: _resolve_workspace_plan(args: ValidateArgs, repo: Path) -> _WorkspacePlan
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_workspace_plan(args, repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:149-154
  In source order: Retain source documentation literal source_literal_149_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:155-156
  if (the source predicate args.workspace is not None is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:156-156
    End this invocation with _WorkspacePlan(args.workspace.resolve(), owns_workspace=False, error=None).
  }
  // Source: vvaharness/validation/cli/__init__.py:157-157
  In source order: Evaluate once Path(tempfile.mkdtemp(prefix=_WORKSPACE_PREFIX)).resolve(); assign in source target order to workspace_root.
  // Source: vvaharness/validation/cli/__init__.py:158-159
  if (the source predicate not workspace_root.is_relative_to(repo) is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:159-159
    End this invocation with _WorkspacePlan(workspace_root, owns_workspace=True, error=None).
  }
  // Source: vvaharness/validation/cli/__init__.py:162-168
  In source order: Evaluate shutil.rmtree(workspace_root, ignore_errors=True); retain side effects and discard the expression result. Then Evaluate once source_template_164_8; assign in source target order to error.
  // Source: vvaharness/validation/cli/__init__.py:169-169
  End this invocation with _WorkspacePlan(workspace_root, owns_workspace=True, error=error).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:172-184
// Source signature: _preflight(args: ValidateArgs) -> tuple[int, ValidateOverrides]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _preflight(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:173-177
  In source order: Retain source documentation literal source_literal_173_4; it is not a model call. Then Evaluate once _trusted_model_env(args); assign in source target order to (rc, overrides).
  // Source: vvaharness/validation/cli/__init__.py:178-179
  if (the source predicate rc != 0 is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:179-179
    End this invocation with (rc, overrides).
  }
  // Source: vvaharness/validation/cli/__init__.py:180-183
  for each (code, err) in ((2, _check_persona_vendors(overrides)), (1, _check_path_guards(args))) {
    // Source: vvaharness/validation/cli/__init__.py:181-183
    if (the source predicate err is truthy) {
      // Source: vvaharness/validation/cli/__init__.py:182-182
      In source order: Evaluate console.write(err); retain side effects and discard the expression result.
      // Source: vvaharness/validation/cli/__init__.py:183-183
      End this invocation with (code, overrides).
    }
  }
  // Source: vvaharness/validation/cli/__init__.py:184-184
  End this invocation with (0, overrides).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:187-206
// Source signature: _run_validation_cleaning_up(*, repo: Path, args: ValidateArgs, config: Config, plan: _WorkspacePlan) -> ValidationRunResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_validation_cleaning_up(repo, args, config, plan) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:190-195
  In source order: Retain source documentation literal source_literal_190_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:196-206
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/__init__.py:197-203
    End this invocation with run_validation(repo=repo, selection=_resolve_selection(args, config), workspace_root=plan.workspace_root, config=config, report_md=args.scan_report).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/validation/cli/__init__.py:205-206
    if (the source predicate plan.owns_workspace is truthy) {
      // Source: vvaharness/validation/cli/__init__.py:206-206
      In source order: Evaluate shutil.rmtree(plan.workspace_root, ignore_errors=True); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:209-230
// Source signature: _dispatch(argv: list[str] | None, *, progress: MutableMapping[str, int] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dispatch(argv, progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:214-216
  In source order: Retain source documentation literal source_literal_214_4; it is not a model call. Then Evaluate once ValidateArgs.of(_build_parser().parse_args(argv)); assign in source target order to args. Then Evaluate once _preflight(args); assign in source target order to (rc, overrides).
  // Source: vvaharness/validation/cli/__init__.py:217-218
  if (the source predicate rc != 0 is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:218-218
    End this invocation with rc.
  }
  // Source: vvaharness/validation/cli/__init__.py:219-222
  In source order: Evaluate once load_config(overrides=overrides); assign in source target order to config. Then For repo, assign args.repo.resolve(); source annotation Path. Then Evaluate once _resolve_workspace_plan(args, repo); assign in source target order to plan.
  // Source: vvaharness/validation/cli/__init__.py:223-225
  if (the source predicate plan.error is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:224-224
    In source order: Evaluate console.write(plan.error); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/__init__.py:225-225
    End this invocation with 1.
  }
  // Source: vvaharness/validation/cli/__init__.py:226-226
  In source order: Evaluate once _run_validation_cleaning_up(repo=repo, args=args, config=config, plan=plan); assign in source target order to result.
  // Source: vvaharness/validation/cli/__init__.py:227-228
  if (the source predicate progress is not None is truthy) {
    // Source: vvaharness/validation/cli/__init__.py:228-228
    In source order: Evaluate _record_progress(result, progress); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/__init__.py:230-230
  End this invocation with result.exit_code.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:233-251
// Source signature: _record_progress(result: ValidationRunResult, progress: MutableMapping[str, int]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _record_progress(result, progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:237-246
  In source order: Retain source documentation literal source_literal_237_4; it is not a model call. Then Resolve source import from vvaharness.models import CaseState; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.derive import verdict_state; preserve alias and import-time effects. Then Evaluate once sum((verdict_state(verdict) is CaseState.VALIDATED for verdict in result.verdicts)); assign in source target order to passed. Then Evaluate once result.metadata.total_findings; assign in source target order to validated.
  // Source: vvaharness/validation/cli/__init__.py:247-251
  In source order: Evaluate progress.update(validated=validated, passed=passed, failed=validated - passed); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:254-268
// Source signature: main(argv: list[str] | None=None, *, progress: MutableMapping[str, int] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn main(argv, progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/__init__.py:259-259
  In source order: Retain source documentation literal source_literal_259_4; it is not a model call.
  // Source: vvaharness/validation/cli/__init__.py:260-268
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/__init__.py:261-262
    End this invocation with _dispatch(argv, progress=progress) if progress is not None else _dispatch(argv).
  }
  // Source: vvaharness/validation/cli/__init__.py:263-265
  On the first matching source exception _KNOWN_ERRORS as e, in handler order {
    // Source: vvaharness/validation/cli/__init__.py:264-264
    In source order: Evaluate console.write(source_template_264_22); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/__init__.py:265-265
    End this invocation with 1.
  }
  // Source: vvaharness/validation/cli/__init__.py:266-268
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/validation/cli/__init__.py:267-267
    In source order: Evaluate console.write(source_template_267_22); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/__init__.py:268-268
    End this invocation with 1.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/__init__.py:271-272
if (the source predicate __name__ == '__main__' is truthy) {
  // Source: vvaharness/validation/cli/__init__.py:272-272
  Raise SystemExit(main()).
}
```

## Local import links

- `from vvaharness.config import ConfigPolicyError, is_network_path` at source line 28: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import _default_config, trusted_config` at source line 29: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 30: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 30: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.validation.cli._model import ModelEnvResult, _apply_model_env, _check_persona_vendors` at source line 31: `source_detail/vvaharness/validation/cli/_model.py.sudo.md`.
- `from vvaharness.validation.cli._parser import _build_parser` at source line 36: `source_detail/vvaharness/validation/cli/_parser.py.sudo.md`.
- `from vvaharness.validation.cli._run import Selection, ValidationRunResult, run_validation` at source line 37: `source_detail/vvaharness/validation/cli/_run.py.sudo.md`.
- `from vvaharness.validation.cli.args import ValidateArgs` at source line 38: `source_detail/vvaharness/validation/cli/args.py.sudo.md`.
- `from vvaharness.validation.config import Config, load_config` at source line 39: `source_detail/vvaharness/validation/config/__init__.py.sudo.md`.
- `from vvaharness.validation.config.overrides import ValidateOverrides` at source line 40: `source_detail/vvaharness/validation/config/overrides.py.sudo.md`.
- `from vvaharness.validation.ingest.errors import IngestError` at source line 41: `source_detail/vvaharness/validation/ingest/errors.py.sudo.md`.
- `from vvaharness.validation.session.errors import ValidationSessionError` at source line 42: `source_detail/vvaharness/validation/session/errors.py.sudo.md`.
- `from vvaharness.models import CaseState` at source line 238: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.derive import verdict_state` at source line 239: `source_detail/vvaharness/models/derive.py.sudo.md`.
