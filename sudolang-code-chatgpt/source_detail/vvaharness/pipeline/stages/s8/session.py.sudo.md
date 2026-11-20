# vvaharness/pipeline/stages/s8/session.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8/session.py.evidence.json`. SHA-256: `2bec7a23ef9f7c44897d86e7fac11d79518a444cc2cf24ddcefef6f7f3717643`.

```sudo
// Source: vvaharness/pipeline/stages/s8/session.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import CallTimeoutError; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/session.py:23-27
In source order: Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence import _cap_int; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/session.py:28-41
In source order: Resolve source import from vvaharness.pipeline.stages.replay import S8_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, release_pinned_session, replay_prompt, run_with_deadline, session_id_for; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.outcomes import ChainReport; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.prompts import SYSTEM, build_prompt, repair_prompt; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/session.py:42-48
In source order: Resolve source import from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import estimate_tokens; preserve alias and import-time effects. Then Evaluate once 90; assign in source target order to MIN_RESPONSE_CHARS. Then Evaluate once 15; assign in source target order to MIN_RESPONSE_TOKENS. Then Evaluate once 's8 chain'; assign in source target order to TAG.
// Source: vvaharness/pipeline/stages/s8/session.py:51-54
In source order: Evaluate once 'low'; assign in source target order to _REPLAY_EFFORT. Then Evaluate once re.compile('\\b(ranked_findings|chains)"?\\s*(?::|=|\\bis\\b)\\s*[\\[{]'); assign in source target order to _REPAIRABLE_RX.
// Source: vvaharness/pipeline/stages/s8/session.py:57-67
// Source signature: _call_budget(s8) -> ModelCallBudget | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_budget(s8) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:58-62
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then Evaluate once _cap_int(s8, 'max_model_calls', 1); assign in source target order to limit.
  // Source: vvaharness/pipeline/stages/s8/session.py:63-64
  if (the source predicate limit <= 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s8/session.py:64-64
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s8/session.py:65-67
  End this invocation with ModelCallBudget(limit=limit, outcome_tools=frozenset({ChainReport.__name__}), counter='s8_model_call_budget_final_turn').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:70-95
// Source signature: _agentic_leg(user: str, ctx: ContextPackage, cfg, *, session_id: str, parent_middleware: tuple, drop_thinking: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _agentic_leg(user, ctx, cfg, session_id, parent_middleware, drop_thinking) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:72-75
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once getattr(cfg, 'step8', None); assign in source target order to s8. Then Evaluate once knob(cfg, 'step8.effort', None) or None; assign in source target order to effort. Then Evaluate once resolve(cfg.models.chain).via; assign in source target order to via.
  // Source: vvaharness/pipeline/stages/s8/session.py:76-95
  End this invocation with _deepagents.dispatch_agentic(user, model=cfg.models.chain, cfg=cfg, cwd=ctx.repo_root, system_prompt=SYSTEM, max_turns=_cap_int(s8, 'max_turns', 2), timeout=deadline_bound(_cap_int(s8, 'timeout', 3600), _cap_int(s8, 'deadline', 0), None if drop_thinking else effort, via=via), max_output_tokens=int(knob(cfg, 'step8.max_tokens', 64000)), response_model=ChainReport if via in RESPONSE_MODEL_VIAS else None, allowed_tools=(), parent_middleware=parent_middleware, tag=TAG, effort=None if drop_thinking else effort, session_id=session_id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:98-100
// Source signature: _replay_max_tokens(cfg) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replay_max_tokens(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:99-99
  In source order: Retain source documentation literal source_literal_99_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/session.py:100-100
  End this invocation with _cap_int(getattr(cfg, 'step8', None), 'replay_max_tokens', 16000).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:103-122
// Source signature: _cold_call(prompt: str, ctx: ContextPackage, cfg, *, tag: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cold_call(prompt, ctx, cfg, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:104-105
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call. Then Evaluate once getattr(cfg, 'step8', None); assign in source target order to s8.
  // Source: vvaharness/pipeline/stages/s8/session.py:107-122
  Enter source context managers left-to-right: stage_floors(tag, min_chars=MIN_RESPONSE_CHARS, min_tokens=MIN_RESPONSE_TOKENS) {
    // Source: vvaharness/pipeline/stages/s8/session.py:108-122
    End this invocation with _deepagents.dispatch_prompt(prompt, model=cfg.models.chain, cfg=cfg, cwd=ctx.repo_root, system_prompt=SYSTEM, max_tokens=_replay_max_tokens(cfg), timeout=_cap_int(s8, 'replay_timeout', 300), response_model=ChainReport if resolve(cfg.models.chain).via in RESPONSE_MODEL_VIAS else None, tag=tag, effort=_REPLAY_EFFORT).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:125-129
// Source signature: _replay_leg(user: str, ctx: ContextPackage, cfg, transcript: Transcript) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replay_leg(user, ctx, cfg, transcript) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:126-126
  In source order: Retain source documentation literal source_literal_126_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/session.py:127-129
  End this invocation with _cold_call(replay_prompt(transcript, user, instruction=S8_REPLAY_INSTRUCTION, stage='s8'), ctx, cfg, tag=source_template_129_22).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:132-134
// Source signature: repairable(raw: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn repairable(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:133-133
  In source order: Retain source documentation literal source_literal_133_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/session.py:134-134
  End this invocation with isinstance(raw, str) and bool(_REPAIRABLE_RX.search(raw)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:137-141
// Source signature: repair_fits(raw: str, cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn repair_fits(raw, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/session.py:141-141
  End this invocation with estimate_tokens(raw) <= _replay_max_tokens(cfg).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:144-146
// Source signature: repair_call(raw: str, err: Exception, ctx: ContextPackage, cfg) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn repair_call(raw, err, ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:145-145
  In source order: Retain source documentation literal source_literal_145_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/session.py:146-146
  End this invocation with _cold_call(repair_prompt(raw, err), ctx, cfg, tag=source_template_146_61).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/session.py:149-197
// Source signature: chain_call(findings: list[Finding], ctx: ContextPackage, cfg, *, labels: list[str] | None=None, allow_resend: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn chain_call(findings, ctx, cfg, labels, allow_resend) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/session.py:151-155
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then Evaluate once getattr(cfg, 'step8', None); assign in source target order to s8. Then Evaluate once knob(cfg, 'step8.effort', None) or None; assign in source target order to effort. Then Evaluate once build_prompt(findings, ctx, labels=labels, cfg=cfg); assign in source target order to user. Then Evaluate once _cap_int(s8, 'deadline', 0); assign in source target order to deadline.
  // Source: vvaharness/pipeline/stages/s8/session.py:156-156
  In source order: Evaluate once False; assign in source target order to replayed.
  // Source: vvaharness/pipeline/stages/s8/session.py:158-182
  // Source signature: _dispatch(*, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _dispatch(drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/session.py:159-163
    In source order: Bind names in enclosing nonlocal scope: replayed. Then Evaluate once session_id_for('s8', 'chain'); assign in source target order to session_id. Then Evaluate once Transcript(); assign in source target order to transcript. Then For middleware, assign (RecordTranscript(transcript),); source annotation tuple. Then Evaluate once _call_budget(s8); assign in source target order to budget.
    // Source: vvaharness/pipeline/stages/s8/session.py:164-165
    if (the source predicate budget is not None is truthy) {
      // Source: vvaharness/pipeline/stages/s8/session.py:165-165
      In source order: Apply source augmented assignment middleware += (budget,) with source evaluation/in-place semantics.
    }
    // Source: vvaharness/pipeline/stages/s8/session.py:166-182
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s8/session.py:167-171
      End this invocation with run_with_deadline(lambda: _agentic_leg(user, ctx, cfg, session_id=session_id, parent_middleware=middleware, drop_thinking=drop_thinking), seconds=deadline, stage=TAG, effort=effort).
    }
    // Source: vvaharness/pipeline/stages/s8/session.py:172-180
    On the first matching source exception CallTimeoutError, in handler order {
      // Source: vvaharness/pipeline/stages/s8/session.py:177-179
      In source order: Evaluate console.write(source_template_177_26); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to replayed.
      // Source: vvaharness/pipeline/stages/s8/session.py:180-180
      End this invocation with _replay_leg(user, ctx, cfg, transcript).
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/pipeline/stages/s8/session.py:182-182
      In source order: Evaluate release_pinned_session(session_id); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s8/session.py:184-197
  Enter source context managers left-to-right: stage_floors(TAG, min_chars=MIN_RESPONSE_CHARS, min_tokens=MIN_RESPONSE_TOKENS) {
    // Source: vvaharness/pipeline/stages/s8/session.py:193-197
    End this invocation with dispatch_or_retry_unforced(_dispatch, 'chain', stage='s8', effort=_deepagents.droppable_effort(cfg.models.chain, effort, agentic=True), may_retry=lambda: allow_resend and effort is not None and (not replayed), resend_refusal=False).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.model_call_budget import ModelCallBudget` at source line 21: `source_detail/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md`.
- `from vvaharness.backends.harness.models import CallTimeoutError` at source line 22: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 23: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 23: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS` at source line 24: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve` at source line 25: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.evidence import _cap_int` at source line 26: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding` at source line 27: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.replay import S8_REPLAY_INSTRUCTION, RecordTranscript, Transcript, deadline_bound, release_pinned_session, replay_prompt, run_with_deadline, session_id_for` at source line 28: `source_detail/vvaharness/pipeline/stages/replay.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.outcomes import ChainReport` at source line 38: `source_detail/vvaharness/pipeline/stages/s8/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.prompts import SYSTEM, build_prompt, repair_prompt` at source line 39: `source_detail/vvaharness/pipeline/stages/s8/prompts.py.sudo.md`.
- `from vvaharness.util import console` at source line 40: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 40: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 41: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors` at source line 42: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.tokens import estimate_tokens` at source line 43: `source_detail/vvaharness/util/tokens.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s8/session.py.sudo.md). Exact strings in the evidence asset support this conversion.
