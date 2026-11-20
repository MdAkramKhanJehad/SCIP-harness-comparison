# vvaharness/validation/execution/pipeline.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/execution/pipeline.py.evidence.json`. SHA-256: `4f4221a74fc0957684a7abf9b9a19be5393d1559cb0c429a73c4853a5a22ebc9`.

```sudo
// Source: vvaharness/validation/execution/pipeline.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Decision, Provenance, Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/validation/execution/pipeline.py:23-27
In source order: Resolve source import from vvaharness.validation.config import Config; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import MANIFEST_FILENAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.io.result_collector import CollectedFinding, collect_and_enrich; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models import RunMetadata, unverifiable_row; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.plans import FixValidationPlan; preserve alias and import-time effects.
// Source: vvaharness/validation/execution/pipeline.py:28-33
In source order: Resolve source import from vvaharness.validation.session.errors import ValidationSessionError; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.session.launcher import launch_session; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['PlanOutcome', 'execute_plan']; assign in source target order to __all__.
// Source: vvaharness/validation/execution/pipeline.py:36-40
interface PlanOutcome {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/execution/pipeline.py:37-40
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then For findings, declare without assigning a value; source annotation list[CollectedFinding]. Then For session_failed, assign False; source annotation bool.
}
// Source: vvaharness/validation/execution/pipeline.py:43-64
// Source signature: _unverifiable(plan: FixValidationPlan, reason: str, provenance: Provenance) -> PlanOutcome
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unverifiable(plan, reason, provenance) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/execution/pipeline.py:46-53
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call. Then Evaluate once Verdict(decision=Decision.INCONCLUSIVE, rationale=reason, score=None, recommendations=(source_template_51_25,), produced_by=provenance); assign in source target order to verdict.
  // Source: vvaharness/validation/execution/pipeline.py:54-64
  End this invocation with PlanOutcome(findings=[CollectedFinding(verdict=verdict, row=unverifiable_row(tracking_id=plan.case_id, title=plan.case_id, reason=reason))], session_failed=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/execution/pipeline.py:67-91
// Source signature: execute_plan(plan: FixValidationPlan, config: Config, *, post_results: bool, meta: RunMetadata) -> PlanOutcome
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn execute_plan(plan, config, post_results, meta) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  This callable produces a coroutine or async generator; await/suspension positions remain in source expressions.
  // Source: vvaharness/validation/execution/pipeline.py:74-78
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call. Then Evaluate once plan.provenance; assign in source target order to stamp. Then Evaluate once plan.workspace_dir; assign in source target order to workspace_dir. Then Evaluate workspace_dir.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate once plan.manifest.model_copy(update={'post_results': post_results}); assign in source target order to manifest.
  // Source: vvaharness/validation/execution/pipeline.py:79-80
  In source order: Evaluate manifest.write(workspace_dir / MANIFEST_FILENAME); retain side effects and discard the expression result. Then Evaluate log.info('Launching validation session %s for %s', plan.session_id, plan.case_id); retain side effects and discard the expression result.
  // Source: vvaharness/validation/execution/pipeline.py:81-87
  Perform the following protected operations {
    // Source: vvaharness/validation/execution/pipeline.py:82-82
    In source order: Evaluate await launch_session(config, manifest, workspace_dir, plan.output_dir); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/execution/pipeline.py:83-87
  On the first matching source exception ValidationSessionError as exc, in handler order {
    // Source: vvaharness/validation/execution/pipeline.py:85-86
    In source order: Evaluate log.warning('Validation session failed for %s: %s', plan.case_id, exc.reason_string()); retain side effects and discard the expression result. Then Evaluate meta.errors.append(source_template_86_27); retain side effects and discard the expression result.
    // Source: vvaharness/validation/execution/pipeline.py:87-87
    End this invocation with _unverifiable(plan, exc.reason_string(), stamp).
  }
  // Source: vvaharness/validation/execution/pipeline.py:88-88
  In source order: Evaluate once collect_and_enrich(workspace_dir, provenance=stamp, policy=plan.policy); assign in source target order to collected.
  // Source: vvaharness/validation/execution/pipeline.py:89-90
  if (the source predicate not collected is truthy) {
    // Source: vvaharness/validation/execution/pipeline.py:90-90
    End this invocation with _unverifiable(plan, 'Validation session produced no results', stamp).
  }
  // Source: vvaharness/validation/execution/pipeline.py:91-91
  End this invocation with PlanOutcome(findings=collected).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Decision, Provenance, Verdict` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.config import Config` at source line 23: `source_detail/vvaharness/validation/config/__init__.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import MANIFEST_FILENAME` at source line 24: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.io.result_collector import CollectedFinding, collect_and_enrich` at source line 25: `source_detail/vvaharness/validation/io/result_collector.py.sudo.md`.
- `from vvaharness.validation.models import RunMetadata, unverifiable_row` at source line 26: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
- `from vvaharness.validation.models.plans import FixValidationPlan` at source line 27: `source_detail/vvaharness/validation/models/plans.py.sudo.md`.
- `from vvaharness.validation.session.errors import ValidationSessionError` at source line 28: `source_detail/vvaharness/validation/session/errors.py.sudo.md`.
- `from vvaharness.validation.session.launcher import launch_session` at source line 29: `source_detail/vvaharness/validation/session/launcher.py.sudo.md`.
