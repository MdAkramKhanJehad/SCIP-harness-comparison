# vvaharness/remediation_agent/runner.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/runner.py.evidence.json`. SHA-256: `9098362e3493e881bc2365e90ea74dc3f36d2e6b71f1be3ad47012aedde54e72`.

```sudo
// Source: vvaharness/remediation_agent/runner.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from collections.abc import MutableMapping; preserve alias and import-time effects. Then Resolve source import from enum import Enum; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/runner.py:21-31
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve as resolve_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import RemediationKind; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, load_ckpt, save_ckpt, step_key_for; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/runner.py:32-41
In source order: Resolve source import from vvaharness.remediation_agent import policy as _policy; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.discovery import Layout; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.options import RemediateOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.plugin_runner import ENGINE_ID, apply_plugin, checkpoint_record, engine_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/runner.py:42-47
In source order: Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.status import stage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/runner.py:49-49
In source order: Evaluate once ['model_banner', 'process_targets', 'remediate_one', 'step_key_of']; assign in source target order to __all__.
// Source: vvaharness/remediation_agent/runner.py:52-55
interface _Result {
  Describe the source Python type, preserving its base/metaclass expression order: Enum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/runner.py:53-55
  In source order: Evaluate once 'fixed'; assign in source target order to FIXED. Then Evaluate once 'not fixed'; assign in source target order to NOT_FIXED. Then Evaluate once 'failed'; assign in source target order to FAILED.
}
// Source: vvaharness/remediation_agent/runner.py:58-68
// Source signature: _result_for_kind(kind: RemediationKind | str | None, *, diff_captured: bool | None=None) -> _Result
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _result_for_kind(kind, diff_captured) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/runner.py:60-61
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate once kind.value if isinstance(kind, RemediationKind) else kind; assign in source target order to value.
  // Source: vvaharness/remediation_agent/runner.py:63-64
  if (the source predicate diff_captured is False is truthy) {
    // Source: vvaharness/remediation_agent/runner.py:64-64
    End this invocation with _Result.NOT_FIXED.
  }
  // Source: vvaharness/remediation_agent/runner.py:65-68
  End this invocation with _Result.FIXED if value in (RemediationKind.EDITS_APPLIED.value, RemediationKind.PULL_REQUEST.value) else _Result.NOT_FIXED.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/runner.py:71-77
// Source signature: model_banner(cfg) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn model_banner(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/runner.py:72-72
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call.
  // Source: vvaharness/remediation_agent/runner.py:73-77
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/runner.py:74-74
    In source order: Evaluate once resolve_model(cfg.models.remediate); assign in source target order to (mid, via, _).
    // Source: vvaharness/remediation_agent/runner.py:75-75
    End this invocation with source_template_75_15.
  }
  // Source: vvaharness/remediation_agent/runner.py:76-77
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/runner.py:77-77
    End this invocation with 'unknown'.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/runner.py:80-88
// Source signature: step_key_of(target: RemediationTarget, cfg) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn step_key_of(target, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/runner.py:81-85
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Evaluate once engine_model(cfg); assign in source target order to (model, backend).
  // Source: vvaharness/remediation_agent/runner.py:86-88
  End this invocation with step_key_for(REMEDIATE_PREFIX, engine_id=ENGINE_ID, engine_version=__version__, case_id=target.case_id, model=model, backend=backend).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/runner.py:91-93
// Source signature: _finding_identity(target: RemediationTarget) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _finding_identity(target) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/runner.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/remediation_agent/runner.py:93-93
  End this invocation with target.case_id.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/runner.py:96-143
// Source signature: remediate_one(target: RemediationTarget, *, idx: int, total: int, layout: Layout, cfg, repo_path: Path, opts: RemediateOptions, policy_ctx=None, _results: list[_Result] | None=None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn remediate_one(target, idx, total, layout, cfg, repo_path, opts, policy_ctx, _results) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/runner.py:99-102
  In source order: Retain source documentation literal source_literal_99_4; it is not a model call. Then Evaluate once redact(target.label); assign in source target order to label. Then Evaluate once step_key_of(target, cfg); assign in source target order to step. Then Evaluate once _finding_identity(target); assign in source target order to fid.
  // Source: vvaharness/remediation_agent/runner.py:105-115
  if (the source predicate opts.resume is truthy) {
    // Source: vvaharness/remediation_agent/runner.py:106-106
    In source order: Evaluate once load_ckpt(layout.ckpt_dir, layout.run_id, step); assign in source target order to cached.
    // Source: vvaharness/remediation_agent/runner.py:107-115
    if (the source predicate isinstance(cached, dict) and cached.get('finding_id') == fid is truthy) {
      // Source: vvaharness/remediation_agent/runner.py:108-109
      In source order: Evaluate once _result_for_kind(cached.get('kind'), diff_captured=cached.get('diff_captured')); assign in source target order to cached_result.
      // Source: vvaharness/remediation_agent/runner.py:110-112
      Enter source context managers left-to-right: stage(source_template_110_23, n=idx, total=total) bound to progress {
        // Source: vvaharness/remediation_agent/runner.py:111-112
        if (the source predicate cached_result is _Result.NOT_FIXED is truthy) {
          // Source: vvaharness/remediation_agent/runner.py:112-112
          In source order: Evaluate progress.mark_incomplete('not fixed'); retain side effects and discard the expression result.
        }
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/remediation_agent/runner.py:113-114
      if (the source predicate _results is not None is truthy) {
        // Source: vvaharness/remediation_agent/runner.py:114-114
        In source order: Evaluate _results.append(cached_result); retain side effects and discard the expression result.
      }
      // Source: vvaharness/remediation_agent/runner.py:115-115
      End this invocation with True.
    }
  }
  // Source: vvaharness/remediation_agent/runner.py:119-119
  In source order: Evaluate once artifact_dir(layout.rem_dir, target.slug); assign in source target order to out_dir.
  // Source: vvaharness/remediation_agent/runner.py:121-143
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/runner.py:123-123
    In source order: Evaluate once False if opts.verbose else None; assign in source target order to animate.
    // Source: vvaharness/remediation_agent/runner.py:124-135
    Enter source context managers left-to-right: stage(label, n=idx, total=total, animate=animate) bound to progress {
      // Source: vvaharness/remediation_agent/runner.py:125-133
      In source order: Evaluate once apply_plugin(target, out_dir, cfg=cfg, repo=repo_path, mode=opts.mode, verbose=opts.verbose, policy_ctx=policy_ctx); assign in source target order to remediation. Then Evaluate once {**checkpoint_record(target, out_dir, remediation), 'finding_id': fid}; assign in source target order to record. Then Evaluate save_ckpt(layout.ckpt_dir, layout.run_id, step, record); retain side effects and discard the expression result. Then Evaluate once _result_for_kind(remediation.kind, diff_captured=bool(remediation.diff)); assign in source target order to result.
      // Source: vvaharness/remediation_agent/runner.py:134-135
      if (the source predicate result is _Result.NOT_FIXED is truthy) {
        // Source: vvaharness/remediation_agent/runner.py:135-135
        In source order: Evaluate progress.mark_incomplete('not fixed'); retain side effects and discard the expression result.
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/remediation_agent/runner.py:136-137
    if (the source predicate _results is not None is truthy) {
      // Source: vvaharness/remediation_agent/runner.py:137-137
      In source order: Evaluate _results.append(result); retain side effects and discard the expression result.
    }
    // Source: vvaharness/remediation_agent/runner.py:138-138
    End this invocation with True.
  }
  // Source: vvaharness/remediation_agent/runner.py:139-143
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/remediation_agent/runner.py:140-140
    In source order: Evaluate log.warning(Event.REMEDIATION_FINDING_FAILED, finding=target.index, detail=redact(str(e))); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/runner.py:141-142
    if (the source predicate _results is not None is truthy) {
      // Source: vvaharness/remediation_agent/runner.py:142-142
      In source order: Evaluate _results.append(_Result.FAILED); retain side effects and discard the expression result.
    }
    // Source: vvaharness/remediation_agent/runner.py:143-143
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/runner.py:146-184
// Source signature: process_targets(targets: list[RemediationTarget], *, layout: Layout, cfg, repo_path: Path, opts: RemediateOptions, report: Path | None=None, progress: MutableMapping[str, int] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn process_targets(targets, layout, cfg, repo_path, opts, report, progress) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/runner.py:150-154
  In source order: Retain source documentation literal source_literal_150_4; it is not a model call. Then Evaluate once len(targets); assign in source target order to total. Then Evaluate once _policy.build_context(cfg, repo_path); assign in source target order to policy_ctx.
  // Source: vvaharness/remediation_agent/runner.py:155-157
  if (the source predicate policy_ctx.enabled is truthy) {
    // Source: vvaharness/remediation_agent/runner.py:156-157
    In source order: Evaluate console.write('  [Remediation Agent] policy gate ENABLED (deny-list + playbook + diff post-gate)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/runner.py:158-167
  In source order: For results, assign []; source annotation list[_Result]. Then Evaluate once [remediate_one(target, idx=i, total=total, layout=layout, cfg=cfg, repo_path=repo_path, opts=opts, policy_ctx=policy_ctx, _results=results) for i, target in enumerate(targets, start=1)]; assign in source target order to processed_ok. Then Evaluate once results.count(_Result.FIXED); assign in source target order to fixed. Then Evaluate once results.count(_Result.NOT_FIXED); assign in source target order to not_fixed. Then Evaluate once results.count(_Result.FAILED); assign in source target order to failed.
  // Source: vvaharness/remediation_agent/runner.py:168-168
  In source order: Evaluate once sum(processed_ok); assign in source target order to processed.
  // Source: vvaharness/remediation_agent/runner.py:169-175
  if (the source predicate progress is not None is truthy) {
    // Source: vvaharness/remediation_agent/runner.py:171-175
    In source order: Evaluate progress.update(attempted=total, fixed=fixed, not_fixed=total - fixed); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/runner.py:176-183
  In source order: Evaluate once source_template_176_19 if failed else ''; assign in source target order to failure_note. Then Evaluate once 'fail' if failed else 'warn' if not_fixed else 'ok'; assign in source target order to outcome. Then Evaluate console.mark(outcome, source_template_178_26, lead=source_literal_180_22); retain side effects and discard the expression result. Then Resolve source import from vvaharness.remediation_agent.report_augment import augment_reports; preserve alias and import-time effects. Then Evaluate augment_reports(repo_path, report); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/runner.py:184-184
  End this invocation with 0 if failed == 0 else 1.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve as resolve_model` at source line 23: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.models import RemediationKind` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import artifact_dir` at source line 25: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, load_ckpt, save_ckpt, step_key_for` at source line 26: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.remediation_agent import policy as _policy` at source line 32: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import policy as _policy` at source line 32: `source_detail/vvaharness/remediation_agent/policy/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.discovery import Layout` at source line 33: `source_detail/vvaharness/remediation_agent/discovery.py.sudo.md`.
- `from vvaharness.remediation_agent.options import RemediateOptions` at source line 34: `source_detail/vvaharness/remediation_agent/options.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner import ENGINE_ID, apply_plugin, checkpoint_record, engine_model` at source line 35: `source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 41: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 42: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 43: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 43: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.status import stage` at source line 44: `source_detail/vvaharness/util/status.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 45: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness import __version__` at source line 83: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.report_augment import augment_reports` at source line 182: `source_detail/vvaharness/remediation_agent/report_augment/__init__.py.sudo.md`.
