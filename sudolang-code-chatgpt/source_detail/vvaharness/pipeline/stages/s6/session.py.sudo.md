# vvaharness/pipeline/stages/s6/session.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s6/session.py.evidence.json`. SHA-256: `52bb5a536c69e828a6c6e41dd86cc771c3e703b4860e39fca7923bea9c0b26ed`.

```sudo
// Source: vvaharness/pipeline/stages/s6/session.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/session.py:21-27
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware import AgentMiddleware; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import ToolBuilder, compose_tool_builders; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/session.py:28-32
In source order: Resolve source import from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import CallTimeoutError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cli; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/session.py:33-41
In source order: Resolve source import from vvaharness.backends.llm.registry import resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.build import graph_is_degenerate; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence import _cap_int; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/session.py:42-65
In source order: Resolve source import from vvaharness.pipeline.stages.replay import S6_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, release_pinned_session, replay_prompt, resume_or_replay, run_with_deadline, session_id_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s6.batching import ceiling_secs; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s6.outcomes import VerificationOutcome, VerificationOutcomes, split_batch_reply; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s6.prompts import build_shared_context, build_system_prompt, build_verify_prompt, repair_prompt; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/session.py:66-70
In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/session.py:73-79
In source order: Evaluate once 'low'; assign in source target order to _REPLAY_EFFORT. Then Evaluate once 40; assign in source target order to _PRIMARY_MIN_CHARS. Then Evaluate once 10; assign in source target order to _PRIMARY_MIN_TOKENS. Then Evaluate once ('TRUE_POSITIVE', 'FALSE_POSITIVE', 'INCONCLUSIVE'); assign in source target order to _VERDICT_TOKENS.
// Source: vvaharness/pipeline/stages/s6/session.py:82-84
// Source signature: _has_verdict_material(raw) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _has_verdict_material(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:83-83
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/session.py:84-84
  End this invocation with isinstance(raw, str) and any((t in raw for t in _VERDICT_TOKENS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:88-91
In source order: For _WARNED_NO_GRAPH, assign set(); source annotation set[str]. Then For _WARNED_DEGENERATE_GRAPH, assign set(); source annotation set[str].
// Source: vvaharness/pipeline/stages/s6/session.py:94-108
// Source signature: _graph_enabled(cfg, s6) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _graph_enabled(cfg, s6) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:95-95
  In source order: Retain source documentation literal source_literal_95_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/session.py:96-97
  if (the source predicate not getattr(s6, 'graph_tools', False) is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:97-97
    End this invocation with False.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:99-100
  In source order: Evaluate once resolve(cfg.models.verify).via; assign in source target order to via. Then Evaluate once _deepagents.route_carries_tools(cfg, via); assign in source target order to (ok, reason).
  // Source: vvaharness/pipeline/stages/s6/session.py:101-107
  if (the source predicate not ok is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:102-107
    In source order: Evaluate warn_once(_WARNED_NO_GRAPH, via, source_template_104_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:108-108
  End this invocation with ok.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:111-119
// Source signature: _call_budget(s6, members: int) -> ModelCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_budget(s6, members) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:112-113
  In source order: Retain source documentation literal source_literal_112_4; it is not a model call. Then Evaluate once _cap_int(s6, 'max_model_calls', 0); assign in source target order to limit.
  // Source: vvaharness/pipeline/stages/s6/session.py:114-115
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:115-115
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:116-119
  End this invocation with ModelCallBudget(limit=limit + max(0, members - 1), outcome_tools=frozenset({VerificationOutcomes.__name__, VerificationOutcome.__name__}), counter='s6_model_call_budget_final_turn').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:122-125
// Source signature: _per_item(base: int, members: int) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _per_item(base, members) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:123-123
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/session.py:125-125
  End this invocation with base * max(1, members).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:128-161
// Source signature: _tool_setup(ctx: ContextPackage, cfg, s6, members: int=1) -> tuple[ToolBuilder | None, tuple[str, ...], tuple[AgentMiddleware, ...]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_setup(ctx, cfg, s6, members) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:131-134
  In source order: Retain source documentation literal source_literal_131_4; it is not a model call. Then For middleware, assign []; source annotation list[AgentMiddleware | None]. Then For builder, assign None; source annotation ToolBuilder | None. Then For names, assign (); source annotation tuple[str, ...].
  // Source: vvaharness/pipeline/stages/s6/session.py:135-159
  if (the source predicate _graph_enabled(cfg, s6) is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:136-138
    In source order: Evaluate once compose_tool_builders(build_graph_tool_builder(ctx)); assign in source target order to builder. Then Evaluate once graph_tool_names(); assign in source target order to names. Then Evaluate once _cap_int(s6, 'graph_tool_budget', 4); assign in source target order to limit.
    // Source: vvaharness/pipeline/stages/s6/session.py:139-142
    if (the source predicate limit > 0 is truthy) {
      // Source: vvaharness/pipeline/stages/s6/session.py:140-142
      In source order: Evaluate middleware.append(ToolCallBudget(frozenset(graph_tool_names()), limit=_per_item(limit, members), counter='s6_graph_tool_budget_exhausted')); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s6/session.py:143-159
    if (the source predicate getattr(s6, 'require_graph', False) is truthy) {
      // Source: vvaharness/pipeline/stages/s6/session.py:145-145
      In source order: Evaluate once frozenset(GRAPH_TOOL_NAMES); assign in source target order to required_tools.
      // Source: vvaharness/pipeline/stages/s6/session.py:146-154
      if (the source predicate graph_is_degenerate(ctx, cfg) is truthy) {
        // Source: vvaharness/pipeline/stages/s6/session.py:147-154
        In source order: Evaluate warn_once(_WARNED_DEGENERATE_GRAPH, 's6-require-graph', source_literal_149_20); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('evidence_gate_stood_down_degenerate_graph'); retain side effects and discard the expression result. Then Evaluate once frozenset(); assign in source target order to required_tools.
      }
      // Source: vvaharness/pipeline/stages/s6/session.py:155-159
      In source order: Evaluate middleware.append(EvidenceGate(max_rejections=_per_item(_cap_int(s6, 'evidence_gate_refusals', 3), members), counter='s6_evidence_gate_rejected', required_tools=required_tools)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:160-160
  In source order: Evaluate middleware.append(_call_budget(s6, members)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s6/session.py:161-161
  End this invocation with (builder, names, tuple((m for m in middleware if m))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:164-170
// Source signature: _load_code(files: list[str], repo_root: Path, s6) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_code(files, repo_root, s6) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:165-165
  In source order: Retain source documentation literal source_literal_165_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/session.py:166-167
  if (the source predicate not getattr(s6, 'inline_source', False) is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:167-167
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:168-168
  In source order: Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _load_files_full; preserve alias and import-time effects.
  // Source: vvaharness/pipeline/stages/s6/session.py:170-170
  End this invocation with _load_files_full(files, repo_root, stage='s6').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:173-173
In source order: Evaluate once RESPONSE_MODEL_VIAS; assign in source target order to _STRUCTURED_VIAS.
// Source: vvaharness/pipeline/stages/s6/session.py:176-179
// Source signature: _response_model(cfg) -> type[VerificationOutcomes] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _response_model(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:177-177
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/session.py:178-179
  End this invocation with VerificationOutcomes if resolve(cfg.models.verify).via in _STRUCTURED_VIAS else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:182-184
// Source signature: _effort(cfg) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effort(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:183-183
  In source order: Retain source documentation literal source_literal_183_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/session.py:184-184
  End this invocation with knob(cfg, 'step6_verify.effort', None) or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:188-191
// Source: vvaharness/pipeline/stages/s6/session.py:187-187
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/pipeline/stages/s6/session.py:188-191
interface _Attempt {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s6/session.py:189-191
  In source order: Retain source documentation literal source_literal_189_4; it is not a model call. Then For replayed, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/pipeline/stages/s6/session.py:194-223
// Source signature: _dispatch(items: list[tuple[str, Finding]], ctx: ContextPackage, cfg, tools: list[str], tag: str, *, drop_thinking: bool=False, attempt: _Attempt | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dispatch(items, ctx, cfg, tools, tag, drop_thinking, attempt) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:197-203
  In source order: Retain source documentation literal source_literal_197_4; it is not a model call. Then Evaluate once _Attempt() if attempt is None else attempt; assign in source target order to attempt. Then Evaluate once False; assign in source target order to attempt.replayed. Then Evaluate once cfg.step6_verify; assign in source target order to s6. Then Evaluate once Transcript(); assign in source target order to transcript.
  // Source: vvaharness/pipeline/stages/s6/session.py:204-205
  In source order: Evaluate once int(knob(cfg, 'step6_verify.batch_deadline', 0) or 0); assign in source target order to deadline. Then Evaluate once session_id_for('s6', tag.replace(' ', '-')); assign in source target order to session_id.
  // Source: vvaharness/pipeline/stages/s6/session.py:206-223
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s6/session.py:207-210
    End this invocation with run_with_deadline(lambda: _agentic_leg(items, ctx, cfg, tools, tag, transcript, session_id=session_id, drop_thinking=drop_thinking), seconds=deadline, stage=tag, effort=_effort(cfg)).
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:211-221
  On the first matching source exception CallTimeoutError, in handler order {
    // Source: vvaharness/pipeline/stages/s6/session.py:212-213
    In source order: Evaluate console.write(source_template_212_22); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6/session.py:214-216
    // Source signature: _replay() -> str
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _replay() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/pipeline/stages/s6/session.py:215-215
      In source order: Evaluate once True; assign in source target order to attempt.replayed.
      // Source: vvaharness/pipeline/stages/s6/session.py:216-216
      End this invocation with _replay_leg(items, ctx, cfg, tag, transcript, s6).
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/pipeline/stages/s6/session.py:217-221
    End this invocation with resume_or_replay(session_id, _replay, model=cfg.models.verify, cfg=cfg, instruction=S6_REPLAY_INSTRUCTION, stage='s6', tag=tag, timeout=_cap_int(s6, 'resume_timeout', 60)).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/pipeline/stages/s6/session.py:223-223
    In source order: Evaluate release_pinned_session(session_id); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:226-247
// Source signature: _replay_leg(items: list[tuple[str, Finding]], ctx: ContextPackage, cfg, tag: str, transcript: Transcript, s6) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replay_leg(items, ctx, cfg, tag, transcript, s6) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:228-245
  In source order: Retain source documentation literal source_literal_228_4; it is not a model call. Then Evaluate COUNTERS.bump('s6_deadline_replay'); retain side effects and discard the expression result. Then Evaluate once _load_code(list(dict.fromkeys((f.file for _, f in items))), Path(ctx.repo_root), s6); assign in source target order to code. Then Evaluate once time.monotonic(); assign in source target order to started. Then Evaluate once _deepagents.dispatch_prompt(replay_prompt(transcript, build_verify_prompt(items, ctx, code), instruction=S6_REPLAY_INSTRUCTION, stage='s6'), model=cfg.models.verify, cfg=cfg, cwd=str(ctx.repo_root), graph_name='s6-verify', tag=source_template_240_12, max_tokens=int(knob(cfg, 'step6_verify.replay_max_tokens', 12000)), timeout=int(knob(cfg, 'step6_verify.replay_timeout', 60)), response_model=_response_model(cfg), effort=_REPLAY_EFFORT); assign in source target order to out.
  // Source: vvaharness/pipeline/stages/s6/session.py:246-246
  In source order: Evaluate console.write(source_template_246_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s6/session.py:247-247
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:250-293
// Source signature: _agentic_leg(items: list[tuple[str, Finding]], ctx: ContextPackage, cfg, tools: list[str], tag: str, transcript: Transcript, *, session_id: str, drop_thinking: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _agentic_leg(items, ctx, cfg, tools, tag, transcript, session_id, drop_thinking) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:253-257
  In source order: Retain source documentation literal source_literal_253_4; it is not a model call. Then Evaluate once cfg.step6_verify; assign in source target order to s6. Then Evaluate once Path(ctx.repo_root); assign in source target order to repo_root. Then Evaluate once list(dict.fromkeys((f.file for _, f in items))); assign in source target order to files. Then Evaluate once _load_code(files, repo_root, s6); assign in source target order to code.
  // Source: vvaharness/pipeline/stages/s6/session.py:258-259
  In source order: Evaluate once _tool_setup(ctx, cfg, s6, len(items)); assign in source target order to (tool_builder, fact_tools, middleware). Then Evaluate once (*middleware, RecordTranscript(transcript)); assign in source target order to middleware.
  // Source: vvaharness/pipeline/stages/s6/session.py:260-293
  Enter source context managers left-to-right: stage_floors(tag, min_chars=_PRIMARY_MIN_CHARS, min_tokens=_PRIMARY_MIN_TOKENS) {
    // Source: vvaharness/pipeline/stages/s6/session.py:261-293
    End this invocation with _deepagents.dispatch_agentic(build_verify_prompt(items, ctx, code), model=cfg.models.verify, cfg=cfg, cwd=str(repo_root), system_prompt=build_system_prompt(graph=_graph_enabled(cfg, s6) and ctx.graph_handle is not None and (not graph_is_degenerate(ctx, cfg)), trait_stamps=bool(knob(cfg, 'step6_verify.trait_stamps', True)), reframe=bool(knob(cfg, 'step6_verify.reframe_enabled', False))), graph_name='s6-verify', tag=tag, allowed_tools=list(tools), tool_builder=tool_builder, fact_tools=fact_tools, response_model=_response_model(cfg), parent_middleware=middleware, cache_prefix=build_shared_context(ctx) or None, max_budget_usd=getattr(s6, 'max_budget_usd', 10.0), max_turns=getattr(s6, 'max_turns', None), effort=None if drop_thinking else _effort(cfg), max_output_tokens=int(knob(cfg, 'step6_verify.max_tokens', 32000)), timeout=deadline_bound(ceiling_secs(s6) or None, int(knob(cfg, 'step6_verify.batch_deadline', 0) or 0), None if drop_thinking else _effort(cfg), via=resolve(cfg.models.verify).via), session_id=session_id).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:296-356
// Source signature: verify_batch(items: list[tuple[str, Finding]], ctx: ContextPackage, cfg, tools: list[str], *, abandoned: Callable[[], bool]=lambda: False, resend_refusal: bool=False) -> dict[str, VerificationOutcome]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn verify_batch(items, ctx, cfg, tools, abandoned, resend_refusal) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:301-306
  In source order: Retain source documentation literal source_literal_301_4; it is not a model call. Then Evaluate once [fid for fid, _ in items]; assign in source target order to ids. Then Evaluate once source_template_304_10; assign in source target order to tag. Then Evaluate once _effort(cfg); assign in source target order to effort. Then Evaluate once _Attempt(); assign in source target order to attempt.
  // Source: vvaharness/pipeline/stages/s6/session.py:312-320
  In source order: Evaluate once dispatch_or_retry_unforced(lambda *, drop_thinking: _dispatch(items, ctx, cfg, tools, tag, drop_thinking=drop_thinking, attempt=attempt), tag, stage='s6', effort=_deepagents.droppable_effort(cfg.models.verify, effort, agentic=True), may_retry=lambda: effort is not None and (not abandoned()), resend_refusal=resend_refusal, may_resend_refusal=lambda: not abandoned() and (not cli.aborted())); assign in source target order to raw. Then Evaluate once split_batch_reply(raw, ids); assign in source target order to outcomes.
  // Source: vvaharness/pipeline/stages/s6/session.py:321-322
  if (the source predicate outcomes is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:322-322
    End this invocation with _stamped(outcomes, attempt.replayed).
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:324-326
  if (the source predicate abandoned() is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:325-325
    In source order: Evaluate COUNTERS.bump('s6_outcome_repair_skipped_abandoned'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6/session.py:326-326
    End this invocation with {}.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:327-335
  if (the source predicate not _has_verdict_material(raw) is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:329-334
    In source order: Evaluate console.write(source_template_329_22); retain side effects and discard the expression result. Then Evaluate _errlog.log('s6-verify', tag, 'primary reply had no verdict material', reason='s6_outcome_repair_skipped_no_verdict', recovered=True); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s6_outcome_repair_skipped_no_verdict'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s6/session.py:335-335
    End this invocation with {}.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:336-338
  In source order: Evaluate COUNTERS.bump('s6_outcome_repaired_attempt'); retain side effects and discard the expression result. Then Evaluate once source_template_338_17; assign in source target order to repair_tag.
  // Source: vvaharness/pipeline/stages/s6/session.py:339-351
  Enter source context managers left-to-right: stage_floors(repair_tag, min_chars=_PRIMARY_MIN_CHARS, min_tokens=_PRIMARY_MIN_TOKENS) {
    // Source: vvaharness/pipeline/stages/s6/session.py:341-351
    In source order: Evaluate once _deepagents.dispatch_prompt(repair_prompt(raw, ids), model=cfg.models.verify, cfg=cfg, cwd=str(ctx.repo_root), graph_name='s6-verify', tag=repair_tag, max_tokens=int(knob(cfg, 'step6_verify.max_tokens', 32000)), response_model=_response_model(cfg)); assign in source target order to repaired.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/pipeline/stages/s6/session.py:352-352
  In source order: Evaluate once split_batch_reply(repaired, ids); assign in source target order to outcomes.
  // Source: vvaharness/pipeline/stages/s6/session.py:353-354
  if (the source predicate outcomes is truthy) {
    // Source: vvaharness/pipeline/stages/s6/session.py:354-354
    In source order: Evaluate COUNTERS.bump('s6_outcome_repaired_ok'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:356-356
  End this invocation with _stamped(outcomes, attempt.replayed).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/session.py:359-364
// Source signature: _stamped(outcomes: dict[str, VerificationOutcome], replayed: bool) -> dict[str, VerificationOutcome]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stamped(outcomes, replayed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/session.py:361-361
  In source order: Retain source documentation literal source_literal_361_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/session.py:362-363
  for each outcome in outcomes.values() {
    // Source: vvaharness/pipeline/stages/s6/session.py:363-363
    In source order: Evaluate once replayed; assign in source target order to outcome.replayed.
  }
  // Source: vvaharness/pipeline/stages/s6/session.py:364-364
  End this invocation with outcomes.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness import ToolBuilder, compose_tool_builders` at source line 25: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate` at source line 26: `source_detail/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 27: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget` at source line 28: `source_detail/vvaharness/backends/harness/deepagents/tool_budget.py.sudo.md`.
- `from vvaharness.backends.harness.models import CallTimeoutError` at source line 29: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 30: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 30: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 31: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 31: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS` at source line 32: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve` at source line 33: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.codegraph.build import graph_is_degenerate` at source line 34: `source_detail/vvaharness/codegraph/build.py.sudo.md`.
- `from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names` at source line 35: `source_detail/vvaharness/codegraph/tools.py.sudo.md`.
- `from vvaharness.evidence import _cap_int` at source line 40: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding` at source line 41: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.replay import S6_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, release_pinned_session, replay_prompt, resume_or_replay, run_with_deadline, session_id_for` at source line 42: `source_detail/vvaharness/pipeline/stages/replay.py.sudo.md`.
- `from vvaharness.pipeline.stages.s6.batching import ceiling_secs` at source line 53: `source_detail/vvaharness/pipeline/stages/s6/batching.py.sudo.md`.
- `from vvaharness.pipeline.stages.s6.outcomes import VerificationOutcome, VerificationOutcomes, split_batch_reply` at source line 54: `source_detail/vvaharness/pipeline/stages/s6/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s6.prompts import build_shared_context, build_system_prompt, build_verify_prompt, repair_prompt` at source line 59: `source_detail/vvaharness/pipeline/stages/s6/prompts.py.sudo.md`.
- `from vvaharness.util import console` at source line 65: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 65: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 66: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 66: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 67: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 68: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors` at source line 69: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 70: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _load_files_full` at source line 168: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s6/session.py.sudo.md). Exact strings in the evidence asset support this conversion.
