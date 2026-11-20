# vvaharness/pipeline/stages/s4/session.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s4/session.py.evidence.json`. SHA-256: `eacfba29aa34c44b36066117b7d3010416bf3d6094518a9c5302d5d40ae76d3c`.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from langchain.agents.middleware import AgentMiddleware, TodoListMiddleware; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import ToolBuilder, compose_tool_builders; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/session.py:23-27
In source order: Resolve source import from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import CallTimeoutError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cli; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/session.py:28-40
In source order: Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS, refusal_resend_allowed, validate_detection_tools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.build import graph_is_degenerate; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/session.py:41-65
In source order: Resolve source import from vvaharness.evidence import _cap_int; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding, InvestigationUnit, UnitSize; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.replay import S4_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, pinned_session, replay_prompt, resume_or_replay, run_with_deadline; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s4.outcomes import InvestigationOutcome, InvestigationOutcomes, reduce_outcomes, split_batch_reply; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s4.prompts import PLAN_TOOL_DESCRIPTION, build_batch_prompt, build_initial_prompt, build_plan_system_prompt, build_system_prompt; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/session.py:66-70
In source order: Resolve source import from vvaharness.rules.kb_tools import KB_TOOL_NAMES, build_kb_tool_builder; preserve alias and import-time effects. Then Resolve source import from vvaharness.skills import inject_skills; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s4/session.py:71-76
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import dispatch_or_retry_unforced; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/pipeline/stages/s4/session.py:78-80
In source order: Evaluate once RESPONSE_MODEL_VIAS; assign in source target order to _STRUCTURED_VIAS. Then For _WARNED_DEGENERATE_GRAPH, assign set(); source annotation set[str].
// Source: vvaharness/pipeline/stages/s4/session.py:83-88
// Source signature: deepdive_tools(cfg) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn deepdive_tools(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:84-84
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:86-88
  End this invocation with validate_detection_tools(knob(cfg, 'step4.allowed_tools', ('Read', 'Glob', 'Grep')), config_key='step4.allowed_tools', via=resolve(cfg.models.deepdive).via).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:91-96
// Source signature: _budget(s4, key: str, names: tuple[str, ...], counter: str) -> ToolCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _budget(s4, key, names, counter) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:92-93
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call. Then Evaluate once _cap_int(s4, key, 6); assign in source target order to limit.
  // Source: vvaharness/pipeline/stages/s4/session.py:94-95
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:95-95
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:96-96
  End this invocation with ToolCallBudget(frozenset(names), limit=limit, counter=counter).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:99-101
// Source signature: _batch_limit(limit: int, members: int) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _batch_limit(limit, members) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:101-101
  End this invocation with limit + max(0, members - 1).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:104-113
// Source signature: _call_budget(s4, outcome: str, members: int=1, *, tag: str='') -> ModelCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_budget(s4, outcome, members, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:105-107
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call. Then Evaluate once _cap_int(s4, 'max_model_calls', 0); assign in source target order to limit.
  // Source: vvaharness/pipeline/stages/s4/session.py:108-109
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:109-109
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:110-113
  End this invocation with ModelCallBudget(limit=_batch_limit(limit, members), outcome_tools=frozenset({outcome}), counter='s4_model_call_budget_final_turn', raise_when_exhausted=True, stage=tag).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:116-119
// Source signature: _graph_tools_registered(ctx: ContextPackage, cfg: object=None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _graph_tools_registered(ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:117-117
  In source order: Retain source documentation literal source_literal_117_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:119-119
  End this invocation with ctx.graph_handle is not None and (not graph_is_degenerate(ctx, cfg)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:122-127
// Source signature: _planner(s4, graph: bool=True) -> TodoListMiddleware | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _planner(s4, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:123-123
  In source order: Retain source documentation literal source_literal_123_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:124-125
  if (the source predicate not getattr(s4, 'planning', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:125-125
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:126-127
  End this invocation with TodoListMiddleware(system_prompt=build_plan_system_prompt(graph), tool_description=PLAN_TOOL_DESCRIPTION).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:130-153
// Source signature: _gate(s4, ctx: ContextPackage, cfg: object=None, *, degenerate_stand_down_counted: list[bool] | None=None) -> EvidenceGate | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gate(s4, ctx, cfg, degenerate_stand_down_counted) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:132-132
  In source order: Retain source documentation literal source_literal_132_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:134-135
  if (the source predicate not getattr(s4, 'planning', True) or not getattr(s4, 'evidence_gate', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:135-135
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:136-137
  In source order: Evaluate once bool(getattr(s4, 'require_graph', True)); assign in source target order to declared. Then Evaluate once declared and graph_is_degenerate(ctx, cfg); assign in source target order to degenerate.
  // Source: vvaharness/pipeline/stages/s4/session.py:138-148
  if (the source predicate degenerate is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:139-144
    In source order: Evaluate warn_once(_WARNED_DEGENERATE_GRAPH, 's4-require-graph', source_literal_141_12); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s4/session.py:145-148
    if (the source predicate degenerate_stand_down_counted is None or not degenerate_stand_down_counted[0] is truthy) {
      // Source: vvaharness/pipeline/stages/s4/session.py:146-147
      if (the source predicate degenerate_stand_down_counted is not None is truthy) {
        // Source: vvaharness/pipeline/stages/s4/session.py:147-147
        In source order: Evaluate once True; assign in source target order to degenerate_stand_down_counted[0].
      }
      // Source: vvaharness/pipeline/stages/s4/session.py:148-148
      In source order: Evaluate COUNTERS.bump('evidence_gate_stood_down_degenerate_graph'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:150-150
  In source order: Evaluate once frozenset(GRAPH_TOOL_NAMES) if declared and (not degenerate) else frozenset(); assign in source target order to required.
  // Source: vvaharness/pipeline/stages/s4/session.py:151-153
  End this invocation with EvidenceGate(max_rejections=_cap_int(s4, 'evidence_gate_refusals', 3), counter='s4_evidence_gate_rejected', required_tools=required).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:156-175
// Source signature: _tool_setup(ctx: ContextPackage, s4, outcome: str=InvestigationOutcome.__name__, members: int=1, *, cfg: object=None, degenerate_stand_down_counted: list[bool] | None=None, tag: str='', graph: bool=True) -> tuple[ToolBuilder, tuple[str, ...], tuple[AgentMiddleware, ...]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_setup(ctx, s4, outcome, members, cfg, degenerate_stand_down_counted, tag, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:161-165
  In source order: Retain source documentation literal source_literal_161_4; it is not a model call. Then Evaluate once [build_graph_tool_builder(ctx)]; assign in source target order to builders. Then Evaluate once graph_tool_names(); assign in source target order to names. Then Evaluate once [_budget(s4, 'graph_tool_budget', graph_tool_names(), 's4_graph_tool_budget_exhausted')]; assign in source target order to middleware.
  // Source: vvaharness/pipeline/stages/s4/session.py:166-170
  if (the source predicate getattr(s4, 'cwe_tools', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:167-170
    In source order: Evaluate builders.append(build_kb_tool_builder()); retain side effects and discard the expression result. Then Apply source augmented assignment names += KB_TOOL_NAMES with source evaluation/in-place semantics. Then Evaluate middleware.append(_budget(s4, 'cwe_tool_budget', KB_TOOL_NAMES, 's4_cwe_tool_budget_exhausted')); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:171-174
  In source order: Evaluate middleware.extend([_planner(s4, graph), _gate(s4, ctx, cfg, degenerate_stand_down_counted=degenerate_stand_down_counted), _call_budget(s4, outcome, members, tag=tag)]); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s4/session.py:175-175
  End this invocation with (compose_tool_builders(*builders), names, tuple((m for m in middleware if m))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:178-183
// Source signature: _load_code(unit: InvestigationUnit, repo_root: Path, s4) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_code(unit, repo_root, s4) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:179-179
  In source order: Retain source documentation literal source_literal_179_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:180-181
  if (the source predicate unit.size == UnitSize.LARGE or not getattr(s4, 'inline_source', False) is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:181-181
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:182-182
  In source order: Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _load_files_full; preserve alias and import-time effects.
  // Source: vvaharness/pipeline/stages/s4/session.py:183-183
  End this invocation with _load_files_full(unit.files, repo_root).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:186-193
// Source signature: _repair_prompt(raw: str, unit_id: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repair_prompt(raw, unit_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:187-193
  End this invocation with source_template_188_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:197-197
In source order: Evaluate once 'low'; assign in source target order to _REPLAY_EFFORT.
// Source: vvaharness/pipeline/stages/s4/session.py:200-202
// Source signature: _deadline_seconds(cfg) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deadline_seconds(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:201-201
  In source order: Retain source documentation literal source_literal_201_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:202-202
  End this invocation with int(knob(cfg, 'step4.deadline', 0) or 0).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:205-209
// Source signature: _session_timeout(cfg, effort: str | None) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _session_timeout(cfg, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:206-206
  In source order: Retain source documentation literal source_literal_206_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:208-209
  End this invocation with deadline_bound(None, _deadline_seconds(cfg), effort, via=resolve(cfg.models.deepdive).via).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:212-222
// Source signature: _deadline_bounded(call, replay, *, cfg, tag: str, session_id: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deadline_bounded(call, replay, cfg, tag, session_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:213-214
  In source order: Retain source documentation literal source_literal_213_4; it is not a model call. Then Evaluate once _deadline_seconds(cfg); assign in source target order to seconds.
  // Source: vvaharness/pipeline/stages/s4/session.py:215-222
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s4/session.py:216-216
    End this invocation with run_with_deadline(call, seconds=seconds, stage=tag, effort=_REPLAY_EFFORT).
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:217-222
  On the first matching source exception CallTimeoutError, in handler order {
    // Source: vvaharness/pipeline/stages/s4/session.py:218-219
    In source order: Evaluate console.write(source_template_218_22); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s4/session.py:220-222
    End this invocation with resume_or_replay(session_id, replay, model=cfg.models.deepdive, cfg=cfg, instruction=S4_REPLAY_INSTRUCTION, stage='s4', tag=tag, timeout=_cap_int(cfg.step4, 'resume_timeout', 60)).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:225-240
// Source signature: _replay_call(prompt_text: str, transcript: Transcript, *, cfg, repo_root: Path, tag: str, response_model) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replay_call(prompt_text, transcript, cfg, repo_root, tag, response_model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:227-228
  In source order: Retain source documentation literal source_literal_227_4; it is not a model call. Then Evaluate COUNTERS.bump('s4_deadline_replay'); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s4/session.py:229-240
  End this invocation with _deepagents.dispatch_prompt(replay_prompt(transcript, prompt_text, instruction=S4_REPLAY_INSTRUCTION, stage='s4'), model=cfg.models.deepdive, cfg=cfg, cwd=str(repo_root), graph_name='s4-deepdive', tag=source_template_235_12, max_tokens=_cap_int(cfg.step4, 'replay_max_tokens', 16000), timeout=_cap_int(cfg.step4, 'replay_timeout', 60), response_model=response_model, effort=_REPLAY_EFFORT).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:243-337
// Source signature: _investigate_unit_once(unit: InvestigationUnit, ctx: ContextPackage, repo_root: Path, cfg) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _investigate_unit_once(unit, ctx, repo_root, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:245-252
  In source order: Retain source documentation literal source_literal_245_4; it is not a model call. Then Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _build_shared_context_block; preserve alias and import-time effects. Then Evaluate once cfg.step4; assign in source target order to s4. Then Evaluate once _load_code(unit, repo_root, s4); assign in source target order to code. Then Evaluate once InvestigationOutcome if resolve(cfg.models.deepdive).via in _STRUCTURED_VIAS else None; assign in source target order to response_model.
  // Source: vvaharness/pipeline/stages/s4/session.py:254-259
  In source order: Evaluate once [False]; assign in source target order to degenerate_stand_down_counted. Then Evaluate once source_template_255_10; assign in source target order to tag. Then Evaluate once _graph_tools_registered(ctx, cfg); assign in source target order to graph. Then Evaluate once getattr(s4, 'effort', None) or None; assign in source target order to effort. Then Evaluate once deepdive_tools(cfg); assign in source target order to tools.
  // Source: vvaharness/pipeline/stages/s4/session.py:260-275
  // Source signature: _dispatch(*, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _dispatch(drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4/session.py:262-268
    In source order: Evaluate once _tool_setup(ctx, s4, cfg=cfg, degenerate_stand_down_counted=degenerate_stand_down_counted, tag=tag, graph=graph); assign in source target order to (tool_builder, fact_tools, middleware). Then Evaluate once build_initial_prompt(unit, code, _cap_int(s4, 'max_model_calls', 0), graph=graph); assign in source target order to initial. Then Evaluate once Transcript(); assign in source target order to transcript. Then Evaluate once (*middleware, RecordTranscript(transcript)); assign in source target order to middleware.
    // Source: vvaharness/pipeline/stages/s4/session.py:269-275
    Enter source context managers left-to-right: pinned_session('s4', unit.id) bound to session_id {
      // Source: vvaharness/pipeline/stages/s4/session.py:270-275
      End this invocation with _deadline_bounded(lambda: _agentic(initial, tool_builder, fact_tools, middleware, session_id=session_id, drop_thinking=drop_thinking), lambda: _replay_call(initial, transcript, cfg=cfg, repo_root=repo_root, tag=tag, response_model=response_model), cfg=cfg, tag=tag, session_id=session_id).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:277-302
  // Source signature: _agentic(initial: str, tool_builder, fact_tools, middleware, *, session_id: str, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _agentic(initial, tool_builder, fact_tools, middleware, session_id, drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4/session.py:279-302
    End this invocation with _deepagents.dispatch_agentic(initial, model=cfg.models.deepdive, cfg=cfg, cwd=str(repo_root), system_prompt=build_system_prompt(shell=bool(getattr(s4, 'bash', False)), graph=graph), graph_name='s4-deepdive', tag=tag, tool_builder=tool_builder, fact_tools=fact_tools, response_model=response_model, allowed_tools=tools, parent_middleware=middleware, max_output_tokens=int(knob(cfg, 'step4.max_tokens', 64000)), cache_prefix=_build_shared_context_block(ctx) or None, skill_root=inject_skills(repo_root) if getattr(s4, 'skills', True) else None, effort=None if drop_thinking else effort, max_turns=_cap_int(s4, 'max_turns', 15), timeout=_session_timeout(cfg, None if drop_thinking else effort), allow_shell=bool(getattr(s4, 'bash', False)), session_id=session_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:304-309
  In source order: Evaluate once dispatch_or_retry_unforced(_dispatch, unit.id, stage='s4', effort=_deepagents.droppable_effort(cfg.models.deepdive, effort, agentic=True), resend_refusal=refusal_resend_allowed(cfg, cfg.models.deepdive)); assign in source target order to raw. Then Evaluate once reduce_outcomes([unit], {unit.id: raw}, cfg, repo_root=str(repo_root), inventory=set(ctx.all_files)); assign in source target order to (findings, by_unit).
  // Source: vvaharness/pipeline/stages/s4/session.py:310-332
  if (the source predicate by_unit[unit.id] == 'failed' is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:312-330
    In source order: Evaluate console.write(source_template_312_22); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', unit.id, 'primary reply did not parse as an InvestigationOutcome', reason='s4_outcome_repair_attempted', recovered=True); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s4_outcome_repaired_attempt'); retain side effects and discard the expression result. Then Evaluate once _deepagents.dispatch_prompt(_repair_prompt(raw, unit.id), model=cfg.models.deepdive, cfg=cfg, cwd=str(repo_root), graph_name='s4-deepdive', tag=source_template_324_16, max_tokens=int(knob(cfg, 'step4.max_tokens', 64000)), response_model=response_model); assign in source target order to repaired. Then Evaluate once reduce_outcomes([unit], {unit.id: repaired}, cfg, repo_root=str(repo_root), inventory=set(ctx.all_files)); assign in source target order to (findings, by_unit).
    // Source: vvaharness/pipeline/stages/s4/session.py:331-332
    if (the source predicate by_unit[unit.id] != 'failed' is truthy) {
      // Source: vvaharness/pipeline/stages/s4/session.py:332-332
      In source order: Evaluate COUNTERS.bump('s4_outcome_repaired_ok'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:333-335
  if (the source predicate by_unit[unit.id] == 'failed' is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:334-335
    Raise RuntimeError(source_template_334_27).
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:337-337
  End this invocation with _cap_findings(unit.id, findings, cfg).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:340-350
// Source signature: _cap_findings(unit_id: str, findings: list[Finding], cfg) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap_findings(unit_id, findings, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:341-342
  In source order: Retain source documentation literal source_literal_341_4; it is not a model call. Then Evaluate once getattr(cfg.step4, 'max_findings_per_run', None); assign in source target order to cap.
  // Source: vvaharness/pipeline/stages/s4/session.py:343-349
  if (the source predicate cap and len(findings) > cap is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:345-349
    In source order: Evaluate once len(findings) - cap; assign in source target order to dropped. Then Evaluate COUNTERS.bump('s4_findings_truncated', dropped); retain side effects and discard the expression result. Then Evaluate log.warning(Event.S4_FINDINGS_CAPPED, unit=unit_id, findings=len(findings), cap=cap, dropped=dropped); retain side effects and discard the expression result. Then Evaluate once findings[:cap]; assign in source target order to findings.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:350-350
  End this invocation with findings.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:353-363
// Source signature: _dedup_by_key(findings: list[Finding], line_bucket: int) -> tuple[list[Finding], int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dedup_by_key(findings, line_bucket) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:354-356
  In source order: Retain source documentation literal source_literal_354_4; it is not a model call. Then For by_key, assign {}; source annotation dict[tuple, Finding].
  // Source: vvaharness/pipeline/stages/s4/session.py:357-358
  for each f in findings {
    // Source: vvaharness/pipeline/stages/s4/session.py:358-358
    In source order: Evaluate by_key.setdefault(f.canonical_key(line_bucket), f); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:360-360
  In source order: Evaluate once len(findings) - len(by_key); assign in source target order to merged.
  // Source: vvaharness/pipeline/stages/s4/session.py:361-362
  if (the source predicate merged > 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:362-362
    In source order: Evaluate COUNTERS.bump('s4_unit_key_deduped', merged); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:363-363
  End this invocation with (list(by_key.values()), merged).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:366-376
// Source signature: investigate_unit(unit: InvestigationUnit, ctx: ContextPackage, repo_root: Path, cfg, stats: dict | None=None) -> list[Finding]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn investigate_unit(unit, ctx, repo_root, cfg, stats) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:368-368
  In source order: Retain source documentation literal source_literal_368_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/session.py:369-370
  if (the source predicate cli.aborted() is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:370-370
    Raise RuntimeError('aborted by user (Ctrl-C)').
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:371-373
  In source order: Evaluate once getattr(cfg.step4, 'line_bucket', 10); assign in source target order to line_bucket. Then Evaluate once _investigate_unit_once(unit, ctx, repo_root, cfg); assign in source target order to findings. Then Evaluate once _dedup_by_key(findings, line_bucket); assign in source target order to (deduped, merged).
  // Source: vvaharness/pipeline/stages/s4/session.py:374-375
  if (the source predicate stats is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:375-375
    In source order: Evaluate once merged; assign in source target order to stats['merged'].
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:376-376
  End this invocation with deduped.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:379-386
// Source signature: _batch_repair_prompt(raw: str, unit_ids: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _batch_repair_prompt(raw, unit_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:380-386
  End this invocation with source_template_381_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:389-459
// Source signature: _batch_reply(batch: list[InvestigationUnit], ctx: ContextPackage, repo_root: Path, cfg) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _batch_reply(batch, ctx, repo_root, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:391-401
  In source order: Retain source documentation literal source_literal_391_4; it is not a model call. Then Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _build_shared_context_block, _load_files_full; preserve alias and import-time effects. Then Evaluate once cfg.step4; assign in source target order to s4. Then Evaluate once list(dict.fromkeys((f for u in batch for f in u.files))); assign in source target order to files. Then Evaluate once _load_files_full(files, repo_root) if getattr(s4, 'inline_source', False) and all((u.size != UnitSize.LARGE for u in batch)) else None; assign in source target order to code.
  // Source: vvaharness/pipeline/stages/s4/session.py:402-410
  In source order: Evaluate once InvestigationOutcomes if resolve(cfg.models.deepdive).via in _STRUCTURED_VIAS else None; assign in source target order to response_model. Then Evaluate once [False]; assign in source target order to degenerate_stand_down_counted. Then Evaluate once source_template_407_10; assign in source target order to tag. Then Evaluate once _graph_tools_registered(ctx, cfg); assign in source target order to graph. Then Evaluate once getattr(s4, 'effort', None) or None; assign in source target order to effort.
  // Source: vvaharness/pipeline/stages/s4/session.py:411-411
  In source order: Evaluate once deepdive_tools(cfg); assign in source target order to tools.
  // Source: vvaharness/pipeline/stages/s4/session.py:412-428
  // Source signature: _dispatch(*, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _dispatch(drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4/session.py:414-421
    In source order: Evaluate once _tool_setup(ctx, s4, InvestigationOutcomes.__name__, len(batch), cfg=cfg, degenerate_stand_down_counted=degenerate_stand_down_counted, tag=tag, graph=graph); assign in source target order to (tool_builder, fact_tools, middleware). Then Evaluate once build_batch_prompt(batch, code, len(files), _cap_int(s4, 'max_model_calls', 0), graph=graph); assign in source target order to initial. Then Evaluate once Transcript(); assign in source target order to transcript. Then Evaluate once (*middleware, RecordTranscript(transcript)); assign in source target order to middleware.
    // Source: vvaharness/pipeline/stages/s4/session.py:422-428
    Enter source context managers left-to-right: pinned_session('s4', batch[0].id) bound to session_id {
      // Source: vvaharness/pipeline/stages/s4/session.py:423-428
      End this invocation with _deadline_bounded(lambda: _agentic(initial, tool_builder, fact_tools, middleware, session_id=session_id, drop_thinking=drop_thinking), lambda: _replay_call(initial, transcript, cfg=cfg, repo_root=repo_root, tag=tag, response_model=response_model), cfg=cfg, tag=tag, session_id=session_id).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:430-454
  // Source signature: _agentic(initial: str, tool_builder, fact_tools, middleware, *, session_id: str, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _agentic(initial, tool_builder, fact_tools, middleware, session_id, drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s4/session.py:432-454
    End this invocation with _deepagents.dispatch_agentic(initial, model=cfg.models.deepdive, cfg=cfg, cwd=str(repo_root), system_prompt=build_system_prompt(shell=bool(getattr(s4, 'bash', False)), graph=graph), graph_name='s4-deepdive', tag=tag, tool_builder=tool_builder, fact_tools=fact_tools, response_model=response_model, allowed_tools=tools, parent_middleware=middleware, max_output_tokens=int(knob(cfg, 'step4.max_tokens', 64000)), cache_prefix=_build_shared_context_block(ctx) or None, skill_root=inject_skills(repo_root) if getattr(s4, 'skills', True) else None, effort=None if drop_thinking else effort, max_turns=_cap_int(s4, 'max_turns', 15), timeout=_session_timeout(cfg, None if drop_thinking else effort), allow_shell=bool(getattr(s4, 'bash', False)), session_id=session_id).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:456-459
  End this invocation with dispatch_or_retry_unforced(_dispatch, source_template_457_19, stage='s4', effort=_deepagents.droppable_effort(cfg.models.deepdive, effort, agentic=True), resend_refusal=refusal_resend_allowed(cfg, cfg.models.deepdive)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/session.py:462-514
// Source signature: investigate_batch(batch: list[InvestigationUnit], ctx: ContextPackage, repo_root: Path, cfg, *, stats: dict | None=None) -> tuple[dict[str, list[Finding]], dict[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn investigate_batch(batch, ctx, repo_root, cfg, stats) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/session.py:465-470
  In source order: Retain source documentation literal source_literal_465_4; it is not a model call. Then Evaluate once [u.id for u in batch]; assign in source target order to ids. Then Evaluate once _batch_reply(batch, ctx, repo_root, cfg); assign in source target order to raw. Then Evaluate once split_batch_reply(raw, ids); assign in source target order to per_unit.
  // Source: vvaharness/pipeline/stages/s4/session.py:471-493
  if (the source predicate not per_unit is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:472-491
    In source order: Evaluate console.write(source_template_472_22); retain side effects and discard the expression result. Then Evaluate _errlog.log('s4', source_template_474_26, 'shared session reply did not parse as InvestigationOutcomes', reason='s4_batch_repair_attempted', recovered=True); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s4_batch_repaired_attempt'); retain side effects and discard the expression result. Then Evaluate once _deepagents.dispatch_prompt(_batch_repair_prompt(raw, ids), model=cfg.models.deepdive, cfg=cfg, cwd=str(repo_root), graph_name='s4-deepdive', tag=source_template_484_16, max_tokens=int(knob(cfg, 'step4.max_tokens', 64000)), response_model=InvestigationOutcomes if resolve(cfg.models.deepdive).via in _STRUCTURED_VIAS else None); assign in source target order to repaired. Then Evaluate once split_batch_reply(repaired, ids); assign in source target order to per_unit.
    // Source: vvaharness/pipeline/stages/s4/session.py:492-493
    if (the source predicate per_unit is truthy) {
      // Source: vvaharness/pipeline/stages/s4/session.py:493-493
      In source order: Evaluate COUNTERS.bump('s4_batch_repaired_ok'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:494-496
  if (the source predicate not per_unit is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:495-496
    Raise RuntimeError(source_template_495_27).
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:497-499
  In source order: Evaluate once reduce_outcomes(batch, per_unit, cfg, repo_root=str(repo_root), inventory=set(ctx.all_files)); assign in source target order to (findings, by_unit). Then For out, assign {u.id: [] for u in batch}; source annotation dict[str, list[Finding]].
  // Source: vvaharness/pipeline/stages/s4/session.py:500-501
  for each f in findings {
    // Source: vvaharness/pipeline/stages/s4/session.py:501-501
    In source order: Evaluate out.setdefault(f.chunk_id, []).append(f); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:504-505
  In source order: Evaluate once getattr(cfg.step4, 'line_bucket', 10); assign in source target order to line_bucket. Then For merged_by_unit, assign {}; source annotation dict[str, int].
  // Source: vvaharness/pipeline/stages/s4/session.py:506-508
  for each u in batch {
    // Source: vvaharness/pipeline/stages/s4/session.py:507-508
    In source order: Evaluate once _cap_findings(u.id, out[u.id], cfg); assign in source target order to capped. Then Evaluate once _dedup_by_key(capped, line_bucket); assign in source target order to (out[u.id], merged_by_unit[u.id]).
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:509-510
  if (the source predicate stats is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/session.py:510-510
    In source order: Evaluate once merged_by_unit; assign in source target order to stats['merged_by_unit'].
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:511-513
  for each verdict in by_unit.values() {
    // Source: vvaharness/pipeline/stages/s4/session.py:512-513
    if (the source predicate verdict in {'uninvestigated', 'failed'} is truthy) {
      // Source: vvaharness/pipeline/stages/s4/session.py:513-513
      In source order: Evaluate COUNTERS.bump(source_template_513_26); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s4/session.py:514-514
  End this invocation with (out, by_unit).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness import ToolBuilder, compose_tool_builders` at source line 22: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate` at source line 23: `source_detail/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 24: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget` at source line 25: `source_detail/vvaharness/backends/harness/deepagents/tool_budget.py.sudo.md`.
- `from vvaharness.backends.harness.models import CallTimeoutError` at source line 26: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 27: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli` at source line 27: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 28: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 28: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS, refusal_resend_allowed, validate_detection_tools` at source line 29: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve` at source line 34: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.codegraph.build import graph_is_degenerate` at source line 35: `source_detail/vvaharness/codegraph/build.py.sudo.md`.
- `from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names` at source line 36: `source_detail/vvaharness/codegraph/tools.py.sudo.md`.
- `from vvaharness.evidence import _cap_int` at source line 41: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding, InvestigationUnit, UnitSize` at source line 42: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.replay import S4_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, pinned_session, replay_prompt, resume_or_replay, run_with_deadline` at source line 43: `source_detail/vvaharness/pipeline/stages/replay.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4.outcomes import InvestigationOutcome, InvestigationOutcomes, reduce_outcomes, split_batch_reply` at source line 53: `source_detail/vvaharness/pipeline/stages/s4/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4.prompts import PLAN_TOOL_DESCRIPTION, build_batch_prompt, build_initial_prompt, build_plan_system_prompt, build_system_prompt` at source line 59: `source_detail/vvaharness/pipeline/stages/s4/prompts.py.sudo.md`.
- `from vvaharness.rules.kb_tools import KB_TOOL_NAMES, build_kb_tool_builder` at source line 66: `source_detail/vvaharness/rules/kb_tools.py.sudo.md`.
- `from vvaharness.skills import inject_skills` at source line 67: `source_detail/vvaharness/skills/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 68: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 68: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 68: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 69: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 69: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 70: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 71: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 72: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.response_quality import dispatch_or_retry_unforced` at source line 73: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 74: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _load_files_full` at source line 182: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _build_shared_context_block` at source line 246: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _build_shared_context_block, _load_files_full` at source line 392: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s4/session.py.sudo.md). Exact strings in the evidence asset support this conversion.
