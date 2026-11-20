# vvaharness/validation/case_api.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/case_api.py.evidence.json`. SHA-256: `66038bf51f84d820d78f4a4922a7b279209edd2c0fa9fa1e3e4bddd3b250e9af`.

```sudo
// Source: vvaharness/validation/case_api.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import asyncio; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import tempfile; preserve alias and import-time effects.
// Source: vvaharness/validation/case_api.py:21-33
In source order: Resolve source import import uuid; preserve alias and import-time effects. Then Resolve source import from datetime import UTC, datetime; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding, FindingCase, Provenance, Remediation, ScoringPolicy, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.report import build_report; preserve alias and import-time effects.
// Source: vvaharness/validation/case_api.py:34-38
In source order: Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, reported_between; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config import Config, load_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.scoring import FIX_POLICY; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.execution.pipeline import execute_plan; preserve alias and import-time effects.
// Source: vvaharness/validation/case_api.py:39-43
In source order: Resolve source import from vvaharness.validation.ingest.manifest_builder import build_manifest; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.workspace import stage_workspace; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.io.case_writeback import build_verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models import RunMetadata; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.plans import FixValidationPlan; preserve alias and import-time effects.
// Source: vvaharness/validation/case_api.py:47-47
In source order: Evaluate once 'vvaharness.sdk.validate'; assign in source target order to ENGINE.
// Source: vvaharness/validation/case_api.py:50-51
interface ValidationCaseError {
  Describe the source Python type, preserving its base/metaclass expression order: ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/case_api.py:51-51
  In source order: Retain source documentation literal source_literal_51_4; it is not a model call.
}
// Source: vvaharness/validation/case_api.py:54-55
interface ValidationBusyError {
  Describe the source Python type, preserving its base/metaclass expression order: RuntimeError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/case_api.py:55-55
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call.
}
// Source: vvaharness/validation/case_api.py:58-61
// Source signature: case_for(finding: Finding, remediation: Remediation) -> FindingCase
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn case_for(finding, remediation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/case_api.py:59-60
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then Evaluate once RemediationTarget(finding=finding, index=1); assign in source target order to target.
  // Source: vvaharness/validation/case_api.py:61-61
  End this invocation with build_report(target, remediation).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/case_api.py:64-72
// Source signature: _refusal(finding: Finding, remediation: Remediation, repo: Path) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refusal(finding, remediation, repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/case_api.py:65-71
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then Evaluate once ((not repo.is_dir(), source_template_67_28), (not finding.file, 'the finding carries no file, so no workspace can be staged for it'), (not remediation.diff, 'the remediation carries no diff, so there is nothing to apply and judge')); assign in source target order to checks.
  // Source: vvaharness/validation/case_api.py:72-72
  End this invocation with next((why for failed, why in checks if failed), '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/case_api.py:75-81
// Source signature: _already_running() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _already_running() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/case_api.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vvaharness/validation/case_api.py:77-80
  Perform the following protected operations {
    // Source: vvaharness/validation/case_api.py:78-78
    In source order: Evaluate asyncio.get_running_loop(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/case_api.py:79-80
  On the first matching source exception RuntimeError, in handler order {
    // Source: vvaharness/validation/case_api.py:80-80
    End this invocation with False.
  }
  // Source: vvaharness/validation/case_api.py:81-81
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/case_api.py:84-88
// Source signature: _provenance(started: datetime, spend_before: object) -> Provenance
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _provenance(started, spend_before) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/case_api.py:85-86
  In source order: Retain source documentation literal source_literal_85_4; it is not a model call. Then Evaluate once reported_between(spend_before, TOKENS.spend()); assign in source target order to (usd, turns).
  // Source: vvaharness/validation/case_api.py:87-88
  End this invocation with Provenance(engine=ENGINE, started=started, ended=datetime.now(UTC), usd=usd, turns=turns).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/case_api.py:91-112
// Source signature: _judge(case: FindingCase, repo: Path, workspace: Path, *, config: Config, policy: ScoringPolicy) -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _judge(case, repo, workspace, config, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/case_api.py:93-97
  In source order: Retain source documentation literal source_literal_93_4; it is not a model call. Then Evaluate once datetime.now(UTC); assign in source target order to started. Then Evaluate once TOKENS.spend(); assign in source target order to spend_before. Then Evaluate once uuid.uuid4().hex; assign in source target order to session_id. Then Evaluate stage_workspace(repo, workspace, case.attempts[-1].remediation.diff); retain side effects and discard the expression result.
  // Source: vvaharness/validation/case_api.py:98-109
  In source order: Evaluate once FixValidationPlan(case_id=case.case_id, session_id=session_id, manifest=build_manifest(case, session_id=session_id), workspace_dir=workspace, output_dir=workspace, provenance=_provenance(started, spend_before), policy=policy); assign in source target order to plan. Then Evaluate once asyncio.run(execute_plan(plan, config, post_results=False, meta=RunMetadata(total_findings=1))); assign in source target order to outcome.
  // Source: vvaharness/validation/case_api.py:110-112
  End this invocation with build_verdict(case, workspace, provenance=_provenance(started, spend_before), policy=policy, session_failed=outcome.session_failed).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/case_api.py:115-136
// Source signature: validate_case(finding: Finding, remediation: Remediation, *, repo: Path, config: Config | None=None, policy: ScoringPolicy | None=None) -> Verdict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_case(finding, remediation, repo, config, policy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/case_api.py:118-120
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo. Then Evaluate once _refusal(finding, remediation, repo); assign in source target order to refusal.
  // Source: vvaharness/validation/case_api.py:121-122
  if (the source predicate refusal is truthy) {
    // Source: vvaharness/validation/case_api.py:122-122
    Raise ValidationCaseError(refusal).
  }
  // Source: vvaharness/validation/case_api.py:123-127
  if (the source predicate _already_running() is truthy) {
    // Source: vvaharness/validation/case_api.py:124-127
    Raise ValidationBusyError(source_literal_125_12).
  }
  // Source: vvaharness/validation/case_api.py:128-131
  In source order: Evaluate once case_for(finding, remediation); assign in source target order to case. Then Evaluate once policy if policy is not None else FIX_POLICY; assign in source target order to resolved_policy. Then Evaluate once config if config is not None else load_config(project_root=repo); assign in source target order to resolved_config. Then Evaluate once Path(tempfile.mkdtemp(prefix='vvah-validate-')); assign in source target order to workspace_root.
  // Source: vvaharness/validation/case_api.py:132-136
  Perform the following protected operations {
    // Source: vvaharness/validation/case_api.py:133-134
    End this invocation with _judge(case, repo, workspace_root / case.case_id, config=resolved_config, policy=resolved_policy).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/validation/case_api.py:136-136
    In source order: Evaluate shutil.rmtree(workspace_root, ignore_errors=True); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/case_api.py:139-145
In source order: Evaluate once ['ENGINE', 'ValidationBusyError', 'ValidationCaseError', 'case_for', 'validate_case']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.models import Finding, FindingCase, Provenance, Remediation, ScoringPolicy, Verdict` at source line 25: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.report import build_report` at source line 33: `source_detail/vvaharness/remediation_agent/artifacts/report.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 34: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, reported_between` at source line 35: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.validation.config import Config, load_config` at source line 36: `source_detail/vvaharness/validation/config/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.scoring import FIX_POLICY` at source line 37: `source_detail/vvaharness/validation/constants/scoring.py.sudo.md`.
- `from vvaharness.validation.execution.pipeline import execute_plan` at source line 38: `source_detail/vvaharness/validation/execution/pipeline.py.sudo.md`.
- `from vvaharness.validation.ingest.manifest_builder import build_manifest` at source line 39: `source_detail/vvaharness/validation/ingest/manifest_builder.py.sudo.md`.
- `from vvaharness.validation.ingest.workspace import stage_workspace` at source line 40: `source_detail/vvaharness/validation/ingest/workspace.py.sudo.md`.
- `from vvaharness.validation.io.case_writeback import build_verdict` at source line 41: `source_detail/vvaharness/validation/io/case_writeback.py.sudo.md`.
- `from vvaharness.validation.models import RunMetadata` at source line 42: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models.plans import FixValidationPlan` at source line 43: `source_detail/vvaharness/validation/models/plans.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/validation/case_api.py.sudo.md). Exact strings in the evidence asset support this conversion.
