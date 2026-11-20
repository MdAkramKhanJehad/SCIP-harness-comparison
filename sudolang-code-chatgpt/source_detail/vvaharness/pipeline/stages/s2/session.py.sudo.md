# vvaharness/pipeline/stages/s2/session.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s2/session.py.evidence.json`. SHA-256: `76c63d95c9953c7608b15634f53ddcdc00255b97e2fc67403c14f9e13aac1ca1`.

```sudo
// Source: vvaharness/pipeline/stages/s2/session.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/session.py:24-29
In source order: Resolve source import from langchain.agents.middleware import TodoListMiddleware; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import CallTimeoutError, is_halt_error; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/session.py:30-38
In source order: Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS, validate_detection_tools; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.build import graph_is_degenerate; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/session.py:39-58
In source order: Resolve source import from vvaharness.evidence import ThreatEvidence, _cap_int; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, ThreatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.replay import S2_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, release_pinned_session, replay_prompt, resume_or_replay, run_with_deadline, session_id_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s2.outcomes import _finalize_threats, _parse_threat_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s2.prompts import _AGENTIC_SYSTEM_LINE, _GRAPH_TOOLS_SYSTEM_LINE, _SHELL_SYSTEM_LINE, SYSTEM; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/session.py:59-67
In source order: Resolve source import from vvaharness.pipeline.stages.s2_planning import PLAN_SYSTEM_PROMPT as S2_PLAN_SYSTEM_PROMPT; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s2_planning import PLAN_TOOL_DESCRIPTION as S2_PLAN_TOOL_DESCRIPTION; preserve alias and import-time effects. Then Resolve source import from vvaharness.skills import inject_skills; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/session.py:68-73
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.exceptions import S2HollowAfterRetry; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/pipeline/stages/s2/session.py:75-84
In source order: Evaluate once 's2 threatmodel'; assign in source target order to _DISPATCH_TAG. Then Evaluate once 's2-threatmodel'; assign in source target order to _GRAPH_NAME. Then Evaluate once 'low'; assign in source target order to _REPLAY_EFFORT. Then For _WARNED_NO_GRAPH_TOOLS, assign set(); source annotation set[str]. Then For _WARNED_DEGENERATE_GRAPH, assign set(); source annotation set[str].
// Source: vvaharness/pipeline/stages/s2/session.py:87-96
In source order: Evaluate once {'no_threats': source_literal_89_8, 'no_validated_surface': source_literal_92_8}; assign in source target order to _HOLLOW_RETRY_DIRECTIVES.
// Source: vvaharness/pipeline/stages/s2/session.py:99-109
// Source signature: _call_budget(s2) -> ModelCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_budget(s2) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:100-104
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once _cap_int(s2, 'max_model_calls', 0); assign in source target order to limit.
  // Source: vvaharness/pipeline/stages/s2/session.py:105-106
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:106-106
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:107-109
  End this invocation with ModelCallBudget(limit=limit, outcome_tools=frozenset({ThreatModel.__name__}), counter='s2_model_call_budget_final_turn').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/session.py:112-124
// Source signature: _graph_tool_route_ok(cfg: object, *, agentic: bool=True) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _graph_tool_route_ok(cfg, agentic) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:113-115
  In source order: Retain source documentation literal source_literal_113_4; it is not a model call. Then Evaluate once resolve(cfg.models.threatmodel).via; assign in source target order to via. Then Evaluate once _deepagents.route_carries_tools(cfg, via); assign in source target order to (ok, reason).
  // Source: vvaharness/pipeline/stages/s2/session.py:116-117
  if (the source predicate ok is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:117-117
    End this invocation with True.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:118-123
  In source order: Evaluate warn_once(_WARNED_NO_GRAPH_TOOLS, source_template_119_32, source_template_120_8); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/session.py:124-124
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/session.py:127-217
// Source signature: _threatmodel_call(user: str, cfg: object, repo_root: str, ctx: ContextPackage | None=None, *, drop_thinking: bool=False, require_tool_call: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _threatmodel_call(user, cfg, repo_root, ctx, drop_thinking, require_tool_call) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:131-135
  In source order: Retain source documentation literal source_literal_131_4; it is not a model call. Then Evaluate once getattr(cfg, 'step2', None); assign in source target order to s2. Then Evaluate once resolve(cfg.models.threatmodel).via; assign in source target order to via. Then Evaluate once None; assign in source target order to tool_builder. Then For fact_tools, assign (); source annotation tuple[str, ...].
  // Source: vvaharness/pipeline/stages/s2/session.py:136-138
  In source order: Evaluate once ''; assign in source target order to graph_tools_line. Then For parent_middleware, assign (); source annotation tuple[ToolCallBudget, ...]. Then Evaluate once False; assign in source target order to gate_installed.
  // Source: vvaharness/pipeline/stages/s2/session.py:139-176
  if (the source predicate ctx is not None and getattr(ctx, 'graph_handle', None) is not None and getattr(s2, 'graph_tools', True) and _graph_tool_route_ok(cfg, agentic=True) is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:142-151
    In source order: Evaluate once build_graph_tool_builder(ctx); assign in source target order to tool_builder. Then Evaluate once graph_tool_names(); assign in source target order to fact_tools. Then Evaluate once graph_is_degenerate(ctx, cfg); assign in source target order to degenerate. Then Evaluate once '' if degenerate else _GRAPH_TOOLS_SYSTEM_LINE; assign in source target order to graph_tools_line. Then Evaluate once (ToolCallBudget(frozenset(graph_tool_names()), limit=_cap_int(s2, 'graph_tool_budget', 6), counter='s2_graph_tool_budget_exhausted'),); assign in source target order to parent_middleware.
    // Source: vvaharness/pipeline/stages/s2/session.py:152-156
    if (the source predicate getattr(s2, 'planning', True) is truthy) {
      // Source: vvaharness/pipeline/stages/s2/session.py:153-156
      In source order: Apply source augmented assignment parent_middleware += (TodoListMiddleware(system_prompt=S2_PLAN_SYSTEM_PROMPT, tool_description=S2_PLAN_TOOL_DESCRIPTION),) with source evaluation/in-place semantics.
    }
    // Source: vvaharness/pipeline/stages/s2/session.py:157-176
    if (the source predicate getattr(s2, 'require_graph', True) is truthy) {
      // Source: vvaharness/pipeline/stages/s2/session.py:159-159
      In source order: Evaluate once frozenset(GRAPH_TOOL_NAMES); assign in source target order to required_tools.
      // Source: vvaharness/pipeline/stages/s2/session.py:160-168
      if (the source predicate degenerate is truthy) {
        // Source: vvaharness/pipeline/stages/s2/session.py:161-168
        In source order: Evaluate warn_once(_WARNED_DEGENERATE_GRAPH, 's2-require-graph', source_literal_163_20); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('evidence_gate_stood_down_degenerate_graph'); retain side effects and discard the expression result. Then Evaluate once frozenset(); assign in source target order to required_tools.
      }
      // Source: vvaharness/pipeline/stages/s2/session.py:169-176
      In source order: Apply source augmented assignment parent_middleware += (EvidenceGate(max_rejections=_cap_int(s2, 'require_graph_rejections', 2), counter='s2_evidence_gate_rejected', required_tools=required_tools, require_tool_call=require_tool_call, ignored_tools=frozenset({'write_todos', ThreatModel.__name__})),) with source evaluation/in-place semantics. Then Evaluate once True; assign in source target order to gate_installed.
    }
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:177-184
  if (the source predicate not gate_installed and require_tool_call and (via == 'deepagents') is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:178-184
    In source order: Apply source augmented assignment parent_middleware += (EvidenceGate(max_rejections=_cap_int(s2, 'require_graph_rejections', 2), counter='s2_evidence_gate_rejected', required_tools=frozenset(), require_tool_call=True, ignored_tools=frozenset({'write_todos', ThreatModel.__name__})),) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:185-194
  In source order: Evaluate once _cap_int(s2, 'max_turns', 12); assign in source target order to max_turns. Then Evaluate once ThreatModel if via in RESPONSE_MODEL_VIAS else None; assign in source target order to threat_model_arg. Then Evaluate once SYSTEM + _AGENTIC_SYSTEM_LINE + graph_tools_line + (_SHELL_SYSTEM_LINE if getattr(s2, 'bash', False) else ''); assign in source target order to system_prompt. Then Evaluate once session_id_for('s2', 'threatmodel'); assign in source target order to session_id. Then Evaluate once Transcript(); assign in source target order to transcript.
  // Source: vvaharness/pipeline/stages/s2/session.py:195-196
  In source order: Apply source augmented assignment parent_middleware += (RecordTranscript(transcript),) with source evaluation/in-place semantics. Then Evaluate once _call_budget(s2); assign in source target order to budget.
  // Source: vvaharness/pipeline/stages/s2/session.py:197-198
  if (the source predicate budget is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:198-198
    In source order: Apply source augmented assignment parent_middleware += (budget,) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:199-200
  In source order: Evaluate once _cap_int(s2, 'deadline', 0); assign in source target order to deadline. Then Evaluate once None if drop_thinking else getattr(s2, 'effort', None) or None; assign in source target order to effort.
  // Source: vvaharness/pipeline/stages/s2/session.py:201-217
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s2/session.py:202-206
    End this invocation with run_with_deadline(lambda: _agentic_leg(user, cfg, repo_root, system_prompt, parent_middleware, tool_builder, fact_tools, max_turns, threat_model_arg, session_id=session_id, drop_thinking=drop_thinking), seconds=deadline, stage=_DISPATCH_TAG, effort=effort).
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:207-215
  On the first matching source exception CallTimeoutError, in handler order {
    // Source: vvaharness/pipeline/stages/s2/session.py:208-209
    In source order: Evaluate console.write(source_template_208_22); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s2/session.py:210-215
    End this invocation with resume_or_replay(session_id, lambda: _replay_leg(user, cfg, repo_root, system_prompt, transcript), model=cfg.models.threatmodel, cfg=cfg, instruction=S2_REPLAY_INSTRUCTION, stage='s2', tag=_DISPATCH_TAG, timeout=_cap_int(s2, 'resume_timeout', 300)).
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/pipeline/stages/s2/session.py:217-217
    In source order: Evaluate release_pinned_session(session_id); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/session.py:220-244
// Source signature: _replay_leg(user: str, cfg: object, repo_root: str, system_prompt: str, transcript: Transcript) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replay_leg(user, cfg, repo_root, system_prompt, transcript) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:222-242
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call. Then Evaluate once getattr(cfg, 'step2', None); assign in source target order to s2. Then Evaluate COUNTERS.bump('s2_deadline_replay'); retain side effects and discard the expression result. Then Evaluate once time.monotonic(); assign in source target order to started. Then Evaluate once _deepagents.dispatch_prompt(replay_prompt(transcript, user, instruction=S2_REPLAY_INSTRUCTION, stage='s2'), model=cfg.models.threatmodel, cfg=cfg, cwd=repo_root, system_prompt=system_prompt, max_tokens=_cap_int(s2, 'replay_max_tokens', 16000), timeout=_cap_int(s2, 'replay_timeout', 300), response_model=ThreatModel if resolve(cfg.models.threatmodel).via in RESPONSE_MODEL_VIAS else None, tag=source_template_239_12, graph_name=_GRAPH_NAME, effort=_REPLAY_EFFORT); assign in source target order to out.
  // Source: vvaharness/pipeline/stages/s2/session.py:243-243
  In source order: Evaluate console.write(source_template_243_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/session.py:244-244
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/session.py:247-281
// Source signature: _agentic_leg(user: str, cfg: object, repo_root: str, system_prompt: str, parent_middleware: tuple, tool_builder: object, fact_tools: tuple[str, ...], max_turns: int, threat_model_arg: object, *, session_id: str, drop_thinking: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _agentic_leg(user, cfg, repo_root, system_prompt, parent_middleware, tool_builder, fact_tools, max_turns, threat_model_arg, session_id, drop_thinking) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:251-252
  In source order: Retain source documentation literal source_literal_251_4; it is not a model call. Then Evaluate once getattr(cfg, 'step2', None); assign in source target order to s2.
  // Source: vvaharness/pipeline/stages/s2/session.py:253-281
  End this invocation with _deepagents.dispatch_agentic(user, model=cfg.models.threatmodel, cfg=cfg, system_prompt=system_prompt, allowed_tools=validate_detection_tools(getattr(s2, 'allowed_tools', None), config_key='step2.allowed_tools', via=resolve(cfg.models.threatmodel).via), cwd=repo_root, max_turns=max_turns, timeout=deadline_bound(_cap_int(s2, 'timeout', 1800), _cap_int(s2, 'deadline', 0), None if drop_thinking else getattr(s2, 'effort', None) or None, via=resolve(cfg.models.threatmodel).via), max_output_tokens=int(knob(cfg, 'step2.max_tokens', 64000)), tag=_DISPATCH_TAG, graph_name=_GRAPH_NAME, tool_builder=tool_builder, fact_tools=fact_tools, response_model=threat_model_arg, parent_middleware=parent_middleware, effort=None if drop_thinking else getattr(s2, 'effort', None) or None, skill_root=inject_skills(Path(repo_root)) if getattr(s2, 'skills', True) else None, allow_shell=bool(getattr(s2, 'bash', False)), session_id=session_id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/session.py:284-308
// Source signature: _snapshot_leg(user: str, cfg: object, repo_root: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _snapshot_leg(user, cfg, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:285-295
  In source order: Retain source documentation literal source_literal_285_4; it is not a model call. Then Evaluate once getattr(cfg, 'step2', None); assign in source target order to s2. Then Evaluate once resolve(cfg.models.threatmodel).via; assign in source target order to via.
  // Source: vvaharness/pipeline/stages/s2/session.py:296-308
  End this invocation with _deepagents.dispatch_prompt(user, model=cfg.models.threatmodel, cfg=cfg, cwd=repo_root, system_prompt=SYSTEM, max_tokens=int(knob(cfg, 'step2.max_tokens', 64000)), timeout=_cap_int(s2, 'timeout', 1800), response_model=ThreatModel if via in RESPONSE_MODEL_VIAS else None, tag=source_template_305_12, graph_name=_GRAPH_NAME, effort=getattr(s2, 'effort', None) or None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/session.py:311-317
// Source signature: _hollow_reason(tm: ThreatModel, resolved: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _hollow_reason(tm, resolved) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:312-312
  In source order: Retain source documentation literal source_literal_312_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s2/session.py:313-314
  if (the source predicate not tm.threats is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:314-314
    End this invocation with 'no_threats'.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:315-316
  if (the source predicate resolved and (not any((t.surface_files for t in tm.threats))) is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:316-316
    End this invocation with 'no_validated_surface'.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:317-317
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/session.py:320-355
// Source signature: _retry_if_hollow(tm: ThreatModel, ev: ThreatEvidence, user: str, cfg, repo_root: str, ctx: ContextPackage | None) -> ThreatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _retry_if_hollow(tm, ev, user, cfg, repo_root, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/session.py:323-324
  In source order: Retain source documentation literal source_literal_323_4; it is not a model call. Then Evaluate once getattr(cfg, 'step2', None); assign in source target order to s2.
  // Source: vvaharness/pipeline/stages/s2/session.py:325-326
  if (the source predicate not getattr(s2, 'empty_retry', True) is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:326-326
    End this invocation with tm.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:327-327
  In source order: Evaluate once _hollow_reason(tm, ctx is not None); assign in source target order to reason.
  // Source: vvaharness/pipeline/stages/s2/session.py:328-329
  if (the source predicate not reason is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:329-329
    End this invocation with tm.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:331-332
  if (the source predicate not ev.file_count is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:332-332
    End this invocation with tm.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:333-335
  In source order: Evaluate COUNTERS.bump('s2_empty_retry_attempted'); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump(source_template_334_18); retain side effects and discard the expression result. Then Evaluate log.warning(Event.S2_HOLLOW_RETRY_ATTEMPTED, reason=reason, threats=len(tm.threats)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/session.py:336-344
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s2/session.py:337-338
    In source order: Evaluate once _parse_threat_model(_snapshot_leg(user + source_literal_338_19 + _HOLLOW_RETRY_DIRECTIVES[reason], cfg, repo_root)); assign in source target order to retry_tm.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:339-344
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/pipeline/stages/s2/session.py:340-341
    if (the source predicate is_halt_error(e) is truthy) {
      // Source: vvaharness/pipeline/stages/s2/session.py:341-341
      Raise the currently handled exception.
    }
    // Source: vvaharness/pipeline/stages/s2/session.py:343-343
    In source order: Evaluate log.warning(Event.S2_HOLLOW_RETRY_FAILED, detail=str(e)); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s2/session.py:344-344
    End this invocation with tm.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:345-346
  In source order: Evaluate _finalize_threats(retry_tm, ctx); retain side effects and discard the expression result. Then Evaluate once _hollow_reason(retry_tm, ctx is not None); assign in source target order to retry_reason.
  // Source: vvaharness/pipeline/stages/s2/session.py:347-350
  if (the source predicate not retry_reason is truthy) {
    // Source: vvaharness/pipeline/stages/s2/session.py:348-349
    In source order: Evaluate COUNTERS.bump('s2_empty_retry_recovered'); retain side effects and discard the expression result. Then Evaluate log.warning(Event.S2_RETRY_RECOVERED, threats=len(retry_tm.threats)); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s2/session.py:350-350
    End this invocation with retry_tm.
  }
  // Source: vvaharness/pipeline/stages/s2/session.py:351-354
  In source order: Evaluate COUNTERS.bump('s2_hollow_after_retry'); retain side effects and discard the expression result. Then Evaluate log.error(Event.S2_HOLLOW_RETRY_EMPTY, reason=retry_reason, remedy=source_literal_353_21); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/session.py:355-355
  Raise S2HollowAfterRetry(retry_reason).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate` at source line 26: `source_detail/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 27: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget` at source line 28: `source_detail/vvaharness/backends/harness/deepagents/tool_budget.py.sudo.md`.
- `from vvaharness.backends.harness.models import CallTimeoutError, is_halt_error` at source line 29: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 30: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 30: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS, validate_detection_tools` at source line 31: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve` at source line 32: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.codegraph.build import graph_is_degenerate` at source line 33: `source_detail/vvaharness/codegraph/build.py.sudo.md`.
- `from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names` at source line 34: `source_detail/vvaharness/codegraph/tools.py.sudo.md`.
- `from vvaharness.evidence import ThreatEvidence, _cap_int` at source line 39: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.models import ContextPackage, ThreatModel` at source line 40: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.replay import S2_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, release_pinned_session, replay_prompt, resume_or_replay, run_with_deadline, session_id_for` at source line 41: `source_detail/vvaharness/pipeline/stages/replay.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2.outcomes import _finalize_threats, _parse_threat_model` at source line 52: `source_detail/vvaharness/pipeline/stages/s2/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2.prompts import _AGENTIC_SYSTEM_LINE, _GRAPH_TOOLS_SYSTEM_LINE, _SHELL_SYSTEM_LINE, SYSTEM` at source line 53: `source_detail/vvaharness/pipeline/stages/s2/prompts.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2_planning import PLAN_SYSTEM_PROMPT as S2_PLAN_SYSTEM_PROMPT` at source line 59: `source_detail/vvaharness/pipeline/stages/s2_planning.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2_planning import PLAN_TOOL_DESCRIPTION as S2_PLAN_TOOL_DESCRIPTION` at source line 62: `source_detail/vvaharness/pipeline/stages/s2_planning.py.sudo.md`.
- `from vvaharness.skills import inject_skills` at source line 65: `source_detail/vvaharness/skills/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 66: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 66: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 67: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 68: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.exceptions import S2HollowAfterRetry` at source line 69: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 70: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 71: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s2/session.py.sudo.md). Exact strings in the evidence asset support this conversion.
