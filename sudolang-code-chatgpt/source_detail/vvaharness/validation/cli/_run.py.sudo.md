# vvaharness/validation/cli/_run.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/cli/_run.py.evidence.json`. SHA-256: `9e48781d6b059a759d2f903c364e8d4e9aa43e635f064dc36a86f0cd93925751`.

```sudo
// Source: vvaharness/validation/cli/_run.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import uuid; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_run.py:22-27
In source order: Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from datetime import UTC, datetime; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import from pydantic import ValidationError; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_run.py:29-33
In source order: Resolve source import from vvaharness.models import HARNESS_REGISTRY, Provenance, ScoringPolicy, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import UnsafeArtifactDir; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import VALIDATE_PREFIX, step_key_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_run.py:34-46
In source order: Resolve source import from vvaharness.util.tokens import TOKENS, Spend, reported_between; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.cli._patterns import _UNSAFE; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config import Config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import CMD_PREVIEW_LEN, LOGGING_DIRNAME, ORCHESTRATOR_LOG_DIRNAME, SESSION_LOG_FILENAME, VALIDATABLE_STATES, VALIDATE_ALIAS_S11, VALIDATION_SESSION_LOG_PREFIX; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.scoring import FIX_POLICY; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_run.py:47-57
In source order: Resolve source import from vvaharness.validation.execution.pipeline import execute_plan; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.case_loader import LoadedCase, all_case_ids, discover_cases, load_case, select_cases; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.errors import IngestError; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.manifest_builder import build_manifest; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.workspace import assert_remediation_applied, stage_workspace; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_run.py:58-62
In source order: Resolve source import from vvaharness.validation.io.case_writeback import build_verdict, write_back_verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.io.result_collector import CollectedFinding; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models import RunMetadata, ValidationResult; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.plans import FixValidationPlan; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.report import augment_reports; preserve alias and import-time effects.
// Source: vvaharness/validation/cli/_run.py:63-68
In source order: Resolve source import from vvaharness.validation.report.models import ValidatedFinding; preserve alias and import-time effects. Then Evaluate once ['VALIDATION_ENGINE_ID', 'Selection', 'ValidationRunResult', 'run_validation']; assign in source target order to __all__. Then Evaluate once 'vvaharness.validation'; assign in source target order to VALIDATION_ENGINE_ID.
// Source: vvaharness/validation/cli/_run.py:71-75
interface SessionLogPaths {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_run.py:72-75
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then For source, declare without assigning a value; source annotation Path. Then For destination, declare without assigning a value; source annotation Path.
}
// Source: vvaharness/validation/cli/_run.py:78-84
interface ValidatedCase {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_run.py:79-84
  In source order: Retain source documentation literal source_literal_79_4; it is not a model call. Then For loaded, declare without assigning a value; source annotation LoadedCase. Then For verdict, declare without assigning a value; source annotation Verdict. Then For row, declare without assigning a value; source annotation ValidationResult. Then For session_failed, declare without assigning a value; source annotation bool.
}
// Source: vvaharness/validation/cli/_run.py:87-92
interface ValidationRunResult {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_run.py:88-92
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call. Then For exit_code, declare without assigning a value; source annotation int. Then For verdicts, declare without assigning a value; source annotation tuple[Verdict, ...]. Then For metadata, declare without assigning a value; source annotation RunMetadata.
}
// Source: vvaharness/validation/cli/_run.py:95-97
// Source signature: _safe(case_id: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _safe(case_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:96-96
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call.
  // Source: vvaharness/validation/cli/_run.py:97-97
  End this invocation with _UNSAFE.sub('_', case_id)[:CMD_PREVIEW_LEN].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:100-102
// Source signature: _engine_identity(config: Config) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _engine_identity(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:101-101
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call.
  // Source: vvaharness/validation/cli/_run.py:102-102
  End this invocation with (str(config.agent.model), source_template_102_36).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:105-110
// Source signature: _step_key(case_id: str, *, model: str, backend: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _step_key(case_id, model, backend) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:106-107
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects.
  // Source: vvaharness/validation/cli/_run.py:108-110
  End this invocation with step_key_for(VALIDATE_PREFIX, engine_id=VALIDATION_ENGINE_ID, engine_version=__version__, case_id=case_id, model=model, backend=backend).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:113-119
// Source signature: _session_log_dest(workspace: Path, loaded: LoadedCase) -> SessionLogPaths | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _session_log_dest(workspace, loaded) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:114-115
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call. Then Evaluate once workspace / LOGGING_DIRNAME / ORCHESTRATOR_LOG_DIRNAME / SESSION_LOG_FILENAME; assign in source target order to src.
  // Source: vvaharness/validation/cli/_run.py:116-117
  if (the source predicate not src.exists() is truthy) {
    // Source: vvaharness/validation/cli/_run.py:117-117
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_run.py:118-118
  In source order: Evaluate once source_template_118_12; assign in source target order to fname.
  // Source: vvaharness/validation/cli/_run.py:119-119
  End this invocation with SessionLogPaths(src, loaded.path.parent / fname).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:122-135
// Source signature: _persist_session_log(workspace: Path, loaded: LoadedCase) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _persist_session_log(workspace, loaded) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:123-124
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call. Then Evaluate once _session_log_dest(workspace, loaded); assign in source target order to resolved.
  // Source: vvaharness/validation/cli/_run.py:125-126
  if (the source predicate resolved is None is truthy) {
    // Source: vvaharness/validation/cli/_run.py:126-126
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_run.py:127-127
  In source order: Evaluate once resolved; assign in source target order to (src, dest).
  // Source: vvaharness/validation/cli/_run.py:128-134
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/_run.py:129-131
    In source order: Evaluate dest.write_text(redact(src.read_text(encoding='utf-8', errors='replace')), encoding='utf-8'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/_run.py:132-134
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/validation/cli/_run.py:133-133
    In source order: Evaluate dest.unlink(missing_ok=True); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_run.py:134-134
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_run.py:135-135
  End this invocation with dest.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:138-142
// Source signature: _print_result(row: ValidationResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _print_result(row) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:139-140
  In source order: Retain source documentation literal source_literal_139_4; it is not a model call. Then Evaluate print(source_template_140_10); retain side effects and discard the expression result.
  // Source: vvaharness/validation/cli/_run.py:141-142
  if (the source predicate row.justification is truthy) {
    // Source: vvaharness/validation/cli/_run.py:142-142
    In source order: Evaluate print(source_template_142_14); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:145-175
// Source signature: _run_plan(loaded: LoadedCase, run: ValidationRun, workspace: Path) -> ValidatedCase
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_plan(loaded, run, workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:146-150
  In source order: Retain source documentation literal source_literal_146_4; it is not a model call. Then Evaluate once datetime.now(UTC); assign in source target order to started. Then Evaluate once TOKENS.spend(); assign in source target order to spend_before. Then Evaluate once uuid.uuid4().hex; assign in source target order to session_id. Then Evaluate once loaded.case.attempts[-1]; assign in source target order to latest.
  // Source: vvaharness/validation/cli/_run.py:151-173
  In source order: Evaluate stage_workspace(run.repo, workspace, latest.remediation.diff); retain side effects and discard the expression result. Then Evaluate once FixValidationPlan(case_id=loaded.case_id, session_id=session_id, manifest=build_manifest(loaded.case, session_id=session_id), workspace_dir=workspace, output_dir=workspace, provenance=run.provenance, policy=run.policy); assign in source target order to plan. Then Evaluate once asyncio.run(execute_plan(plan, run.config, post_results=False, meta=RunMetadata(total_findings=1))); assign in source target order to outcome. Then For collected, assign outcome.findings[0]; source annotation CollectedFinding. Then Evaluate once build_verdict(loaded.case, workspace, provenance=_measured(run.provenance, started, spend_before), policy=run.policy, session_failed=outcome.session_failed); assign in source target order to verdict.
  // Source: vvaharness/validation/cli/_run.py:174-174
  In source order: Evaluate _record(loaded, verdict, workspace); retain side effects and discard the expression result.
  // Source: vvaharness/validation/cli/_run.py:175-175
  End this invocation with ValidatedCase(loaded, verdict, collected.row, outcome.session_failed).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:178-182
// Source signature: _measured(base: Provenance, started: datetime, spend_before: Spend) -> Provenance
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _measured(base, started, spend_before) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:179-180
  In source order: Retain source documentation literal source_literal_179_4; it is not a model call. Then Evaluate once reported_between(spend_before, TOKENS.spend()); assign in source target order to (usd, turns).
  // Source: vvaharness/validation/cli/_run.py:181-182
  End this invocation with base.model_copy(update={'started': started, 'ended': datetime.now(UTC), 'usd': usd, 'turns': turns}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:185-195
// Source signature: _record(loaded: LoadedCase, verdict: Verdict, workspace: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _record(loaded, verdict, workspace) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:186-187
  In source order: Retain source documentation literal source_literal_186_4; it is not a model call. Then Evaluate once _persist_session_log(workspace, loaded); assign in source target order to record.
  // Source: vvaharness/validation/cli/_run.py:188-189
  if (the source predicate record is not None is truthy) {
    // Source: vvaharness/validation/cli/_run.py:189-189
    In source order: Evaluate console.write(source_template_189_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/_run.py:190-190
  In source order: Evaluate once write_back_verdict(loaded.case, verdict, loaded.path); assign in source target order to judged.
  // Source: vvaharness/validation/cli/_run.py:191-195
  if (the source predicate judged is not None is truthy) {
    // Source: vvaharness/validation/cli/_run.py:192-195
    In source order: Evaluate console.write(source_template_193_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:198-212
// Source signature: _validate_one(loaded: LoadedCase, run: ValidationRun) -> ValidatedCase | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_one(loaded, run) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:199-199
  In source order: Retain source documentation literal source_literal_199_4; it is not a model call.
  // Source: vvaharness/validation/cli/_run.py:200-202
  if (the source predicate not loaded.case.attempts is truthy) {
    // Source: vvaharness/validation/cli/_run.py:201-201
    In source order: Evaluate console.write(source_template_201_22); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_run.py:202-202
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_run.py:203-203
  In source order: Evaluate once run.workspace_root / _safe(loaded.case_id); assign in source target order to workspace.
  // Source: vvaharness/validation/cli/_run.py:204-208
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/_run.py:205-205
    In source order: Evaluate assert_remediation_applied(run.repo, loaded.case.attempts[-1].remediation.files_touched); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/_run.py:206-208
  On the first matching source exception IngestError as exc, in handler order {
    // Source: vvaharness/validation/cli/_run.py:207-207
    In source order: Evaluate console.write(source_template_207_22); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_run.py:208-208
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_run.py:209-212
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/_run.py:210-210
    End this invocation with _run_plan(loaded, run, workspace).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/validation/cli/_run.py:212-212
    In source order: Evaluate shutil.rmtree(workspace, ignore_errors=True); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:215-218
// Source signature: _resume_hit(run: ValidationRun, step: str) -> ValidationResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resume_hit(run, step) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:216-217
  In source order: Retain source documentation literal source_literal_216_4; it is not a model call. Then Resolve source import from vvaharness.orchestrator.checkpoints import load_ckpt; preserve alias and import-time effects.
  // Source: vvaharness/validation/cli/_run.py:218-218
  End this invocation with load_ckpt(run.workspace_root, run.run_id, step).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:221-237
// Source signature: _process_case(loaded: LoadedCase, run: ValidationRun) -> ValidatedCase | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _process_case(loaded, run) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:222-224
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call. Then Evaluate once _engine_identity(run.config); assign in source target order to (model, backend). Then Evaluate once _step_key(loaded.case_id, model=model, backend=backend); assign in source target order to step.
  // Source: vvaharness/validation/cli/_run.py:225-232
  if (the source predicate run.resume is truthy) {
    // Source: vvaharness/validation/cli/_run.py:226-226
    In source order: Evaluate once _resume_hit(run, step); assign in source target order to cached.
    // Source: vvaharness/validation/cli/_run.py:228-232
    if (the source predicate cached is not None and cached.tracking_id == loaded.case_id is truthy) {
      // Source: vvaharness/validation/cli/_run.py:229-231
      In source order: Evaluate console.write(source_template_230_16); retain side effects and discard the expression result.
      // Source: vvaharness/validation/cli/_run.py:232-232
      End this invocation with _resumed(loaded, cached).
    }
  }
  // Source: vvaharness/validation/cli/_run.py:233-233
  In source order: Evaluate once _validate_one(loaded, run); assign in source target order to validated.
  // Source: vvaharness/validation/cli/_run.py:234-236
  if (the source predicate validated is not None is truthy) {
    // Source: vvaharness/validation/cli/_run.py:235-236
    In source order: Resolve source import from vvaharness.orchestrator.checkpoints import save_ckpt; preserve alias and import-time effects. Then Evaluate save_ckpt(run.workspace_root, run.run_id, step, validated.row); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/_run.py:237-237
  End this invocation with validated.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:240-246
// Source signature: _resumed(loaded: LoadedCase, cached: ValidationResult) -> ValidatedCase
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resumed(loaded, cached) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:241-243
  In source order: Retain source documentation literal source_literal_241_4; it is not a model call. Then Evaluate once loaded.case.attempts[-1] if loaded.case.attempts else None; assign in source target order to latest. Then Evaluate once latest.verdict if latest is not None else None; assign in source target order to verdict.
  // Source: vvaharness/validation/cli/_run.py:244-245
  if (the source predicate verdict is None is truthy) {
    // Source: vvaharness/validation/cli/_run.py:245-245
    End this invocation with ValidatedCase(loaded, _no_verdict(), cached, session_failed=True).
  }
  // Source: vvaharness/validation/cli/_run.py:246-246
  End this invocation with ValidatedCase(loaded, verdict, cached, session_failed=False).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:249-258
// Source signature: _no_verdict() -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _no_verdict() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:250-252
  In source order: Retain source documentation literal source_literal_250_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Decision; preserve alias and import-time effects.
  // Source: vvaharness/validation/cli/_run.py:253-258
  End this invocation with Verdict(decision=Decision.INCONCLUSIVE, rationale='resumed from a checkpoint, but the case file records no verdict', score=None, produced_by=Provenance(engine=VALIDATION_ENGINE_ID, engine_version=__version__)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:261-277
// Source signature: _run_cases(cases: list[LoadedCase], run: ValidationRun) -> tuple[int, list[ValidatedCase]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_cases(cases, run) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:262-264
  In source order: Retain source documentation literal source_literal_262_4; it is not a model call. Then Evaluate once 0; assign in source target order to failures. Then For validated, assign []; source annotation list[ValidatedCase].
  // Source: vvaharness/validation/cli/_run.py:265-276
  for each loaded in cases {
    // Source: vvaharness/validation/cli/_run.py:266-266
    In source order: Evaluate once _process_case(loaded, run); assign in source target order to result.
    // Source: vvaharness/validation/cli/_run.py:267-269
    if (the source predicate result is None is truthy) {
      // Source: vvaharness/validation/cli/_run.py:268-268
      In source order: Apply source augmented assignment failures += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/validation/cli/_run.py:269-269
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/cli/_run.py:270-275
    if (the source predicate result.session_failed is truthy) {
      // Source: vvaharness/validation/cli/_run.py:272-273
      In source order: Evaluate console.write(source_template_272_26); retain side effects and discard the expression result. Then Apply source augmented assignment failures += 1 with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/validation/cli/_run.py:275-275
      In source order: Evaluate _print_result(result.row); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/cli/_run.py:276-276
    In source order: Evaluate validated.append(result); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/_run.py:277-277
  End this invocation with (failures, validated).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:281-286
// Source: vvaharness/validation/cli/_run.py:280-280
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/cli/_run.py:281-286
interface Selection {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_run.py:282-286
  In source order: Retain source documentation literal source_literal_282_4; it is not a model call. Then For case_ids, assign None; source annotation list[str] | None. Then For max_findings, assign None; source annotation int | None. Then For resume, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/cli/_run.py:290-299
// Source: vvaharness/validation/cli/_run.py:289-289
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/cli/_run.py:290-299
interface ValidationRun {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/cli/_run.py:291-296
  In source order: Retain source documentation literal source_literal_291_4; it is not a model call. Then For repo, declare without assigning a value; source annotation Path. Then For workspace_root, declare without assigning a value; source annotation Path. Then For config, declare without assigning a value; source annotation Config. Then For run_id, declare without assigning a value; source annotation str.
  // Source: vvaharness/validation/cli/_run.py:297-299
  In source order: For provenance, declare without assigning a value; source annotation Provenance. Then For policy, declare without assigning a value; source annotation ScoringPolicy. Then For resume, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/cli/_run.py:302-311
// Source signature: _cleanup_workspace(workspace_root: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cleanup_workspace(workspace_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:303-303
  In source order: Retain source documentation literal source_literal_303_4; it is not a model call.
  // Source: vvaharness/validation/cli/_run.py:304-311
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/_run.py:305-305
    In source order: Evaluate shutil.rmtree(workspace_root); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/cli/_run.py:306-307
  On the first matching source exception FileNotFoundError, in handler order {
    // Source: vvaharness/validation/cli/_run.py:307-307
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/validation/cli/_run.py:308-311
  On the first matching source exception OSError as exc, in handler order {
    // Source: vvaharness/validation/cli/_run.py:309-311
    In source order: Evaluate console.write(source_template_310_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:314-323
// Source signature: _any_owned(paths: list[Path], owned: set[tuple[str, Path]]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _any_owned(paths, owned) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:315-315
  In source order: Retain source documentation literal source_literal_315_4; it is not a model call.
  // Source: vvaharness/validation/cli/_run.py:316-322
  for each path in paths {
    // Source: vvaharness/validation/cli/_run.py:317-320
    Perform the following protected operations {
      // Source: vvaharness/validation/cli/_run.py:318-318
      In source order: Evaluate once load_case(path).case_id; assign in source target order to case_id.
    }
    // Source: vvaharness/validation/cli/_run.py:319-320
    On the first matching source exception (OSError, ValueError, ValidationError), in handler order {
      // Source: vvaharness/validation/cli/_run.py:320-320
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/cli/_run.py:321-322
    if (the source predicate (case_id, path.parent.resolve()) in owned is truthy) {
      // Source: vvaharness/validation/cli/_run.py:322-322
      End this invocation with True.
    }
  }
  // Source: vvaharness/validation/cli/_run.py:323-323
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:326-349
// Source signature: _empty_selection_rc(repo: Path, *, owned: set[tuple[str, Path]] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _empty_selection_rc(repo, owned) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:327-332
  In source order: Retain source documentation literal source_literal_327_4; it is not a model call. Then Evaluate once discover_cases(repo); assign in source target order to discovered.
  // Source: vvaharness/validation/cli/_run.py:333-338
  if (the source predicate not discovered is truthy) {
    // Source: vvaharness/validation/cli/_run.py:334-337
    In source order: Evaluate once ' / '.join(sorted((state.value for state in VALIDATABLE_STATES))); assign in source target order to valid. Then Evaluate console.write(source_template_336_12); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_run.py:338-338
    End this invocation with 1.
  }
  // Source: vvaharness/validation/cli/_run.py:339-344
  if (the source predicate owned is not None and (not _any_owned(discovered, owned)) is truthy) {
    // Source: vvaharness/validation/cli/_run.py:340-343
    In source order: Evaluate console.write(source_template_341_12); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_run.py:344-344
    End this invocation with 1.
  }
  // Source: vvaharness/validation/cli/_run.py:345-348
  In source order: Evaluate console.write(source_template_346_8); retain side effects and discard the expression result.
  // Source: vvaharness/validation/cli/_run.py:349-349
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:352-360
// Source signature: _prune_orphans(repo: Path, run_id: str, *, model: str, backend: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _prune_orphans(repo, run_id, model, backend) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:353-355
  In source order: Retain source documentation literal source_literal_353_4; it is not a model call. Then Resolve source import from vvaharness.orchestrator.checkpoints import prune_stale_steps; preserve alias and import-time effects. Then Evaluate once all_case_ids(repo); assign in source target order to case_ids.
  // Source: vvaharness/validation/cli/_run.py:356-357
  if (the source predicate case_ids is None is truthy) {
    // Source: vvaharness/validation/cli/_run.py:357-357
    End this invocation with None.
  }
  // Source: vvaharness/validation/cli/_run.py:358-360
  In source order: Evaluate prune_stale_steps(run_id, VALIDATE_PREFIX, [_step_key(cid, model=model, backend=backend) for cid in case_ids]); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:363-372
// Source signature: _provenance_for(config: Config) -> Provenance
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _provenance_for(config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:364-366
  In source order: Retain source documentation literal source_literal_364_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Evaluate once _engine_identity(config); assign in source target order to (model, backend).
  // Source: vvaharness/validation/cli/_run.py:367-372
  End this invocation with Provenance(engine=VALIDATION_ENGINE_ID, engine_version=__version__, model=model, backend=backend).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/cli/_run.py:375-434
// Source signature: run_validation(*, repo: Path, selection: Selection, workspace_root: Path, config: Config, report_md: Path | None=None) -> ValidationRunResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_validation(repo, selection, workspace_root, config, report_md) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/cli/_run.py:383-391
  In source order: Retain source documentation literal source_literal_383_4; it is not a model call. Then Evaluate once RunMetadata(); assign in source target order to meta. Then Resolve source import from vvaharness.orchestrator.checkpoints import run_id_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store import register_run; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.provenance import owned_cases; preserve alias and import-time effects.
  // Source: vvaharness/validation/cli/_run.py:392-394
  In source order: Evaluate once run_id_for(repo); assign in source target order to run_id. Then Evaluate register_run(run_id, repo_root=str(repo.resolve())); retain side effects and discard the expression result. Then Evaluate once owned_cases(run_id); assign in source target order to owned.
  // Source: vvaharness/validation/cli/_run.py:395-400
  Perform the following protected operations {
    // Source: vvaharness/validation/cli/_run.py:396-396
    In source order: Evaluate once select_cases(repo, selection.case_ids, selection.max_findings, owned=owned); assign in source target order to cases.
  }
  // Source: vvaharness/validation/cli/_run.py:397-400
  On the first matching source exception (IngestError, UnsafeArtifactDir) as exc, in handler order {
    // Source: vvaharness/validation/cli/_run.py:398-399
    In source order: Evaluate console.write(source_template_398_22); retain side effects and discard the expression result. Then Evaluate meta.errors.append(str(exc)); retain side effects and discard the expression result.
    // Source: vvaharness/validation/cli/_run.py:400-400
    End this invocation with ValidationRunResult(1, (), meta).
  }
  // Source: vvaharness/validation/cli/_run.py:401-402
  if (the source predicate not cases is truthy) {
    // Source: vvaharness/validation/cli/_run.py:402-402
    End this invocation with ValidationRunResult(_empty_selection_rc(repo, owned=owned), (), meta).
  }
  // Source: vvaharness/validation/cli/_run.py:403-415
  In source order: Evaluate once _engine_identity(config); assign in source target order to (model, backend). Then Evaluate _prune_orphans(repo, run_id, model=model, backend=backend); retain side effects and discard the expression result. Then Evaluate once ValidationRun(repo=repo, workspace_root=workspace_root, config=config, run_id=run_id, provenance=_provenance_for(config), policy=FIX_POLICY, resume=selection.resume); assign in source target order to run. Then Evaluate once _run_cases(cases, run); assign in source target order to (failures, validated). Then Evaluate once len(cases); assign in source target order to meta.total_findings.
  // Source: vvaharness/validation/cli/_run.py:416-428
  In source order: Evaluate once len(validated); assign in source target order to meta.findings_processed. Then Evaluate once failures; assign in source target order to meta.findings_failed. Then Evaluate augment_reports(repo, [ValidatedFinding(item.loaded.case.finding, item.row, item.session_failed) for item in validated], report_md); retain side effects and discard the expression result. Then Evaluate _cleanup_workspace(workspace_root); retain side effects and discard the expression result. Then Resolve source import from vvaharness.orchestrator.case_rollup import rc_for_verdicts; preserve alias and import-time effects.
  // Source: vvaharness/validation/cli/_run.py:429-429
  In source order: Evaluate once tuple((item.verdict for item in validated)); assign in source target order to verdicts.
  // Source: vvaharness/validation/cli/_run.py:430-434
  End this invocation with ValidationRunResult(exit_code=1 if failures else rc_for_verdicts(verdicts), verdicts=verdicts, metadata=meta).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import HARNESS_REGISTRY, Provenance, ScoringPolicy, Verdict` at source line 29: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import UnsafeArtifactDir` at source line 30: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import VALIDATE_PREFIX, step_key_for` at source line 31: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 32: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 33: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 33: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, Spend, reported_between` at source line 34: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.validation.cli._patterns import _UNSAFE` at source line 35: `source_detail/vvaharness/validation/cli/_patterns.py.sudo.md`.
- `from vvaharness.validation.config import Config` at source line 36: `source_detail/vvaharness/validation/config/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import CMD_PREVIEW_LEN, LOGGING_DIRNAME, ORCHESTRATOR_LOG_DIRNAME, SESSION_LOG_FILENAME, VALIDATABLE_STATES, VALIDATE_ALIAS_S11, VALIDATION_SESSION_LOG_PREFIX` at source line 37: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.constants.scoring import FIX_POLICY` at source line 46: `source_detail/vvaharness/validation/constants/scoring.py.sudo.md`.
- `from vvaharness.validation.execution.pipeline import execute_plan` at source line 47: `source_detail/vvaharness/validation/execution/pipeline.py.sudo.md`.
- `from vvaharness.validation.ingest.case_loader import LoadedCase, all_case_ids, discover_cases, load_case, select_cases` at source line 48: `source_detail/vvaharness/validation/ingest/case_loader.py.sudo.md`.
- `from vvaharness.validation.ingest.errors import IngestError` at source line 55: `source_detail/vvaharness/validation/ingest/errors.py.sudo.md`.
- `from vvaharness.validation.ingest.manifest_builder import build_manifest` at source line 56: `source_detail/vvaharness/validation/ingest/manifest_builder.py.sudo.md`.
- `from vvaharness.validation.ingest.workspace import assert_remediation_applied, stage_workspace` at source line 57: `source_detail/vvaharness/validation/ingest/workspace.py.sudo.md`.
- `from vvaharness.validation.io.case_writeback import build_verdict, write_back_verdict` at source line 58: `source_detail/vvaharness/validation/io/case_writeback.py.sudo.md`.
- `from vvaharness.validation.io.result_collector import CollectedFinding` at source line 59: `source_detail/vvaharness/validation/io/result_collector.py.sudo.md`.
- `from vvaharness.validation.models import RunMetadata, ValidationResult` at source line 60: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models.plans import FixValidationPlan` at source line 61: `source_detail/vvaharness/validation/models/plans.py.sudo.md`.
- `from vvaharness.validation.report import augment_reports` at source line 62: `source_detail/vvaharness/validation/report/__init__.py.sudo.md`.
- `from vvaharness.validation.report.models import ValidatedFinding` at source line 63: `source_detail/vvaharness/validation/report/models.py.sudo.md`.
- `from vvaharness import __version__` at source line 107: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import load_ckpt` at source line 217: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness import __version__` at source line 251: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.models import Decision` at source line 252: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import prune_stale_steps` at source line 354: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness import __version__` at source line 365: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import run_id_for` at source line 389: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator.store import register_run` at source line 390: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.provenance import owned_cases` at source line 391: `source_detail/vvaharness/remediation_agent/provenance.py.sudo.md`.
- `from vvaharness.orchestrator.case_rollup import rc_for_verdicts` at source line 428: `source_detail/vvaharness/orchestrator/case_rollup.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import save_ckpt` at source line 235: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
