# vvaharness/remediation_agent/plugin_runner/run.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/plugin_runner/run.py.evidence.json`. SHA-256: `4905cf525b2bee8af49e150a96e3460a4f29b6b76f3546271dc126e7653c0551`.

```sudo
// Source: vvaharness/remediation_agent/plugin_runner/run.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from datetime import UTC, datetime; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/run.py:21-33
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import LLM_REGISTRY, Provenance, Remediation, RemediationEvidence, RemediationKind, finalize; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent import artifacts; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent import policy as _policy; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/run.py:34-38
In source order: Resolve source import from vvaharness.remediation_agent.artifacts.diff import _norm_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import Gates, RemediationVerdict, to_evidence; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS, Spend, reported_between; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/plugin_runner/run.py:40-52
In source order: Evaluate once ['Amended', 'EngineRequest', 'GuardedCall', 'apply_plugin', 'call_with_guards', 'checkpoint_record', 'engine_model', 'harness_amend']; assign in source target order to __all__. Then Evaluate once 'vvaharness.remediation_agent'; assign in source target order to ENGINE_ID.
// Source: vvaharness/remediation_agent/plugin_runner/run.py:56-69
// Source: vvaharness/remediation_agent/plugin_runner/run.py:55-55
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/plugin_runner/run.py:56-69
interface EngineRequest {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:57-62
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call. Then For target, declare without assigning a value; source annotation RemediationTarget. Then For repo, declare without assigning a value; source annotation Path. Then For mode, declare without assigning a value; source annotation str. Then For cfg, declare without assigning a value; source annotation Any.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:63-64
  In source order: For verbose, assign False; source annotation bool. Then For policy_ctx, assign None; source annotation Any.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:67-69
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:66-66
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:67-69
  // Source signature: enforce(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn enforce(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:68-68
    In source order: Retain source documentation literal source_literal_68_8; it is not a model call.
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:69-69
    End this invocation with self.policy_ctx is not None and getattr(self.policy_ctx, 'enabled', False).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/plugin_runner/run.py:73-83
// Source: vvaharness/remediation_agent/plugin_runner/run.py:72-72
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/plugin_runner/run.py:73-83
interface GuardedCall {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:74-79
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call. Then For verdict, declare without assigning a value; source annotation RemediationVerdict. Then For snapshot, assign field(default_factory=dict); source annotation dict[str, str | None]. Then For pre, assign None; source annotation Any. Then For meta, assign field(default_factory=dict); source annotation dict.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:80-83
  In source order: For denied, assign False; source annotation bool. Then For started, assign None; source annotation datetime | None. Then For spend_before, assign Spend(); source annotation Spend. Then For pre_call_dirty, assign (); source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/plugin_runner/run.py:87-92
// Source: vvaharness/remediation_agent/plugin_runner/run.py:86-86
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/remediation_agent/plugin_runner/run.py:87-92
interface Amended {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:88-92
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call. Then For remediation, declare without assigning a value; source annotation Remediation. Then For reverted_paths, assign (); source annotation tuple[str, ...]. Then For meta, assign field(default_factory=dict); source annotation dict.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/plugin_runner/run.py:95-120
// Source signature: call_with_guards(fn: Callable[..., Any], request: EngineRequest) -> GuardedCall
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn call_with_guards(fn, request) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:96-101
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent import plugin_runner as _pr; preserve alias and import-time effects. Then Evaluate once datetime.now(UTC); assign in source target order to started. Then Evaluate once TOKENS.spend(); assign in source target order to spend_before. Then Evaluate once _base_meta(request, started); assign in source target order to meta.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:102-102
  In source order: Evaluate once _policy.pre_decision(request.policy_ctx, request.target) if request.enforce else None; assign in source target order to pre.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:103-104
  if (the source predicate request.verbose is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:104-104
    In source order: Evaluate _trace_policy(request, pre); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:105-106
  if (the source predicate pre is not None and (not pre.allowed) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:106-106
    End this invocation with _denied(request, pre, meta, started, spend_before).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:109-111
  In source order: Evaluate once artifacts.changed_files_whole_tree(request.repo); assign in source target order to pre_call_dirty. Then Evaluate once artifacts.snapshot_files(request.repo, pre_call_dirty); assign in source target order to pre_call_snapshot. Then Evaluate once artifacts.snapshot_files(request.repo, _snapshot_targets(request)); assign in source target order to snapshot.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:112-116
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:113-113
    In source order: Evaluate once _call_engine(fn, request, pre); assign in source target order to raw.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:114-116
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:115-116
    End this invocation with _engine_failed(request, exc, pre_call_dirty, pre_call_snapshot, snapshot, pre, meta, started, spend_before).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:117-120
  End this invocation with GuardedCall(verdict=_pr._coerce_verdict(raw, request.target), snapshot=snapshot, pre=pre, meta=meta, started=started, spend_before=spend_before, pre_call_dirty=tuple(pre_call_dirty)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:123-143
// Source signature: _engine_failed(request: EngineRequest, exc: Exception, pre_call_dirty: list[str], pre_call_snapshot: dict[str, str | None], snapshot: dict[str, str | None], pre: Any, meta: dict, started: datetime, spend_before: Spend) -> GuardedCall
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _engine_failed(request, exc, pre_call_dirty, pre_call_snapshot, snapshot, pre, meta, started, spend_before) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:127-131
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call. Then Evaluate once artifacts.changed_files_whole_tree(request.repo); assign in source target order to now_dirty. Then Evaluate once [f for f in now_dirty if f not in set(pre_call_dirty)]; assign in source target order to new_untracked. Then Evaluate once artifacts.changed_since_snapshot(request.repo, pre_call_snapshot); assign in source target order to changed_during_call. Then Evaluate once list(dict.fromkeys([*changed_during_call, *new_untracked])); assign in source target order to to_revert.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:132-140
  In source order: Evaluate once _policy.revert_files(request.repo, to_revert, pre_call_snapshot) if to_revert else []; assign in source target order to reverted. Then Evaluate once getattr(exc, 'stderr', None) or str(exc); assign in source target order to detail. Then Evaluate console.write(source_template_136_8); retain side effects and discard the expression result. Then Evaluate once RemediationVerdict(finding_index=request.target.index, verdict='Not Fixed', gates=Gates(), changes=[], summary=source_template_140_28); assign in source target order to verdict.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:142-143
  End this invocation with GuardedCall(verdict=verdict, snapshot=snapshot, pre=pre, meta=meta, started=started, spend_before=spend_before).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:146-168
// Source signature: harness_amend(remediation: RemediationVerdict, snapshot: dict[str, str | None], *, request: EngineRequest, pre: Any=None, denied: bool=False, started: datetime | None=None, spend_before: Spend=Spend(), pre_call_dirty: tuple[str, ...]=()) -> Amended
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn harness_amend(remediation, snapshot, request, pre, denied, started, spend_before, pre_call_dirty) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:151-153
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then For reverted, assign (); source annotation tuple[str, ...]. Then For meta, assign {}; source annotation dict.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:154-158
  if (the source predicate pre is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:155-158
    In source order: Evaluate once _policy.enforce_post(request.policy_ctx, request.target, remediation, pre, repo=request.repo, before_snapshot=snapshot); assign in source target order to post. Then Evaluate once tuple(post.reverted); assign in source target order to reverted. Then Evaluate once _post_meta(pre, post); assign in source target order to meta.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:159-167
  In source order: Evaluate once artifacts.derive_diff(request.repo, snapshot, [c.file for c in remediation.changes if c.file]); assign in source target order to diff. Then Evaluate once to_evidence(remediation, provenance=_provenance(request, denied=denied, started=started, spend_before=spend_before)); assign in source target order to evidence. Then Evaluate once finalize(evidence, mode=request.mode, diff=diff, files_touched=_files_touched(request.repo, evidence, snapshot, pre_call_dirty)); assign in source target order to contract. Then Evaluate once _reconcile_post_meta(meta, contract); assign in source target order to meta.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:168-168
  End this invocation with Amended(remediation=contract, reverted_paths=reverted, meta=meta).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:171-188
// Source signature: _reconcile_post_meta(meta: dict, remediation: Remediation) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reconcile_post_meta(meta, remediation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:172-172
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:174-175
  if (the source predicate meta.get('policy_action') != 'patch' or meta.get('policy_reverted') is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:175-175
    End this invocation with meta.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:176-177
  In source order: Evaluate once remediation.kind in (RemediationKind.NO_ACTION, RemediationKind.ALREADY_RESOLVED); assign in source target order to no_action.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:178-179
  if (the source predicate remediation.diff and (not no_action) is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:179-179
    End this invocation with meta.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:180-185
  In source order: Evaluate once 'no_diff_captured' if not remediation.diff else 'remediation_not_applied'; assign in source target order to reason. Then Evaluate once {**meta, 'policy_reason': reason, 'final_verdict': 'REJECT'}; assign in source target order to reconciled.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:186-187
  if (the source predicate meta.get('policy_reason') != reason is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:187-187
    In source order: Evaluate once meta.get('policy_reason', ''); assign in source target order to reconciled['policy_pre_reason'].
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:188-188
  End this invocation with reconciled.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:191-207
// Source signature: apply_plugin(target: RemediationTarget, out_dir: Path, *, cfg, repo: Path, mode: str='fix', verbose: bool=False, policy_ctx=None) -> Remediation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn apply_plugin(target, out_dir, cfg, repo, mode, verbose, policy_ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:194-203
  In source order: Retain source documentation literal source_literal_194_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent import plugin_runner as _pr; preserve alias and import-time effects. Then Evaluate once EngineRequest(target=target, repo=Path(repo), mode=mode, cfg=cfg, verbose=verbose, policy_ctx=policy_ctx); assign in source target order to request. Then Evaluate once call_with_guards(_pr._invoke, request); assign in source target order to guarded. Then Evaluate once harness_amend(guarded.verdict, guarded.snapshot, request=request, pre=guarded.pre, denied=guarded.denied, started=guarded.started, spend_before=guarded.spend_before, pre_call_dirty=guarded.pre_call_dirty); assign in source target order to amended.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:204-206
  In source order: Evaluate artifacts.write_case(out_dir, guarded.verdict, amended.remediation, meta={**guarded.meta, **amended.meta}, target=target, reverted_paths=amended.reverted_paths); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:207-207
  End this invocation with amended.remediation.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:210-220
// Source signature: checkpoint_record(target: RemediationTarget, out_dir: Path, remediation: Remediation) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn checkpoint_record(target, out_dir, remediation) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:212-213
  In source order: Retain source documentation literal source_literal_212_4; it is not a model call. Then Evaluate once remediation.disposition; assign in source target order to disposition.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:214-220
  End this invocation with {'finding_index': target.index, 'artifact_dir': str(out_dir), 'kind': remediation.kind.value, 'disposition': disposition.value if disposition is not None else None, 'diff_captured': bool(remediation.diff)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:223-239
// Source signature: _files_touched(repo: Path, evidence: RemediationEvidence, snapshot: dict[str, str | None], pre_call_dirty: tuple[str, ...]=()) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _files_touched(repo, evidence, snapshot, pre_call_dirty) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:226-227
  In source order: Retain source documentation literal source_literal_226_4; it is not a model call. Then Evaluate once artifacts.changed_files_whole_tree(repo); assign in source target order to proven.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:228-236
  if (the source predicate proven is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:231-235
    In source order: Evaluate once {_norm_path(f) for f in pre_call_dirty}; assign in source target order to pre_norm. Then Evaluate once {_norm_path(f) for f in artifacts.changed_since_snapshot(repo, snapshot)} if snapshot else set(); assign in source target order to changed_this_case. Then Evaluate once [f for f in proven if _norm_path(f) not in pre_norm or _norm_path(f) in changed_this_case]; assign in source target order to proven.
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:236-236
    End this invocation with tuple(proven).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:237-238
  In source order: Evaluate once artifacts.changed_since_snapshot(repo, snapshot); assign in source target order to from_snapshot. Then Evaluate once [c.file for c in evidence.changes if _resolves(repo, c.file)]; assign in source target order to claimed.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:239-239
  End this invocation with tuple(dict.fromkeys([*from_snapshot, *claimed])).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:242-247
// Source signature: _resolves(repo: Path, ref: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolves(repo, ref) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:243-243
  In source order: Retain source documentation literal source_literal_243_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:244-245
  if (the source predicate not ref is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:245-245
    End this invocation with False.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:246-246
  In source order: Evaluate once artifacts._safe_repo_path(repo, ref); assign in source target order to resolved.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:247-247
  End this invocation with resolved is not None and resolved.is_file().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:250-258
// Source signature: _base_meta(request: EngineRequest, started: datetime) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _base_meta(request, started) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:251-251
  In source order: Retain source documentation literal source_literal_251_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:252-258
  End this invocation with {'severity': request.target.severity, 'title': request.target.title, 'file': request.target.file, 'mode': request.mode, 'generated': started.isoformat()}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:261-274
// Source signature: _post_meta(pre: Any, post: Any) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _post_meta(pre, post) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:262-268
  In source order: Retain source documentation literal source_literal_262_4; it is not a model call. Then Evaluate once post.reason or pre.decision.reason; assign in source target order to reason. Then Evaluate once {'policy_action': pre.decision.action.value, 'policy_reason': reason, 'final_verdict': post.final_verdict}; assign in source target order to meta.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:269-270
  if (the source predicate post.reason is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:270-270
    In source order: Evaluate once pre.decision.reason; assign in source target order to meta['policy_pre_reason'].
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:271-273
  if (the source predicate post.reverted is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:272-273
    In source order: Evaluate once post.reverted; assign in source target order to meta['policy_reverted']. Then Evaluate once post.matched_globs; assign in source target order to meta['policy_matched_globs'].
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:274-274
  End this invocation with meta.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:277-286
// Source signature: _trace_policy(request: EngineRequest, pre: Any) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _trace_policy(request, pre) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:278-279
  In source order: Retain source documentation literal source_literal_278_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent import plugin_runner as _pr; preserve alias and import-time effects.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:281-283
  if (the source predicate pre is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:282-282
    In source order: Evaluate _pr._dump_policy(request.target, pre); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:283-283
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:284-286
  In source order: Evaluate console.write(source_template_284_18); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:289-302
// Source signature: _denied(request: EngineRequest, pre: Any, meta: dict, started: datetime, spend_before: Spend) -> GuardedCall
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _denied(request, pre, meta, started, spend_before) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:291-294
  In source order: Retain source documentation literal source_literal_291_4; it is not a model call. Then Evaluate once _policy.guidance_verdict(request.policy_ctx, request.target, pre); assign in source target order to verdict. Then Evaluate console.write(source_template_293_18); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:295-302
  End this invocation with GuardedCall(verdict=verdict, meta={**meta, 'policy_action': pre.decision.action.value, 'policy_reason': pre.decision.reason, 'final_verdict': 'REJECT'}, denied=True, started=started, spend_before=spend_before).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:305-316
// Source signature: _snapshot_targets(request: EngineRequest) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _snapshot_targets(request) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:306-309
  In source order: Retain source documentation literal source_literal_306_4; it is not a model call. Then Evaluate once [request.target.file] if request.target.file else []; assign in source target order to targets. Then Evaluate targets.extend(_policy.workflow_snapshot_paths(request.repo)); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:310-311
  if (the source predicate not request.enforce is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:311-311
    End this invocation with targets.
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:312-314
  In source order: Evaluate once getattr(request.policy_ctx, 'gate', None); assign in source target order to gate. Then Evaluate once [*getattr(gate, 'forbid_patch_paths', []), *getattr(gate, 'deny_paths', [])] if gate else []; assign in source target order to patterns.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:315-316
  End this invocation with list(dict.fromkeys([*targets, *_policy.worktree_forbidden_matches(request.repo, patterns)])).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:319-324
// Source signature: _call_engine(fn: Callable[..., Any], request: EngineRequest, pre: Any) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_engine(fn, request, pre) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:320-320
  In source order: Retain source documentation literal source_literal_320_4; it is not a model call.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:321-323
  if (the source predicate pre is not None is truthy) {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:322-323
    End this invocation with fn(request.target, request.cfg, request.repo, request.mode, request.verbose, pre=pre, ctx=request.policy_ctx).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:324-324
  End this invocation with fn(request.target, request.cfg, request.repo, request.mode, request.verbose).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:327-339
// Source signature: _provenance(request: EngineRequest, *, denied: bool=False, started: datetime | None=None, spend_before: Spend=Spend()) -> Provenance
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _provenance(request, denied, started, spend_before) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:330-335
  In source order: Retain source documentation literal source_literal_330_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Evaluate once ('', '') if denied else engine_model(request.cfg); assign in source target order to (model, backend). Then Evaluate once (0.0, 0) if denied else reported_between(spend_before, TOKENS.spend()); assign in source target order to (usd, turns).
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:336-339
  End this invocation with Provenance(engine=ENGINE_ID, engine_version=__version__, model=model, backend=backend, started=started, ended=datetime.now(UTC) if started else None, usd=usd, turns=turns).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/plugin_runner/run.py:342-351
// Source signature: engine_model(cfg) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn engine_model(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:343-344
  In source order: Retain source documentation literal source_literal_343_4; it is not a model call. Then Resolve source import from vvaharness.backends.llm.registry import resolve as resolve_model; preserve alias and import-time effects.
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:346-349
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:347-347
    In source order: Evaluate once resolve_model(cfg.models.remediate); assign in source target order to (mid, via, _).
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:348-349
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/plugin_runner/run.py:349-349
    End this invocation with ('', '').
  }
  // Source: vvaharness/remediation_agent/plugin_runner/run.py:351-351
  End this invocation with (str(mid), source_template_351_21).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import LLM_REGISTRY, Provenance, Remediation, RemediationEvidence, RemediationKind, finalize` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import artifacts` at source line 32: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import artifacts` at source line 32: `source_detail/vvaharness/remediation_agent/artifacts/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import policy as _policy` at source line 33: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import policy as _policy` at source line 33: `source_detail/vvaharness/remediation_agent/policy/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.artifacts.diff import _norm_path` at source line 34: `source_detail/vvaharness/remediation_agent/artifacts/diff/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.models import Gates, RemediationVerdict, to_evidence` at source line 35: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 36: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.util import console` at source line 37: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 37: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, Spend, reported_between` at source line 38: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.remediation_agent import plugin_runner as _pr` at source line 97: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import plugin_runner as _pr` at source line 97: `source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import plugin_runner as _pr` at source line 195: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import plugin_runner as _pr` at source line 195: `source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import plugin_runner as _pr` at source line 279: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import plugin_runner as _pr` at source line 279: `source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md`.
- `from vvaharness import __version__` at source line 331: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve as resolve_model` at source line 344: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
