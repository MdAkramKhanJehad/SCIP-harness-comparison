# vvaharness/pipeline/stages/s7/session.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s7/session.py.evidence.json`. SHA-256: `02b90c9508420fefc981d2399098eaa63d52486cee517d1d141fc1e361f595bd`.

```sudo
// Source: vvaharness/pipeline/stages/s7/session.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import is_halt_error; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import refusal_resend_allowed; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s7/session.py:22-26
In source order: Resolve source import from vvaharness.models import ContextPackage, Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s7.outcomes import DedupDecisions, parse_decisions; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s7.prompts import SYSTEM, build_payload; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s7/session.py:27-33
In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors; preserve alias and import-time effects. Then Evaluate once 90; assign in source target order to MIN_RESPONSE_CHARS. Then Evaluate once 15; assign in source target order to MIN_RESPONSE_TOKENS.
// Source: vvaharness/pipeline/stages/s7/session.py:36-75
// Source signature: semantic_dedup(verified: list[Finding], unresolved: list[int], cfg, ctx: ContextPackage, label: str='s7-dedup') -> list[tuple[int, int, str, bool]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn semantic_dedup(verified, unresolved, cfg, ctx, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/session.py:39-42
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call. Then Evaluate once label.replace('-', ' '); assign in source target order to tag. Then Evaluate once knob(cfg, 'step7_dedup.effort', None) or None; assign in source target order to effort.
  // Source: vvaharness/pipeline/stages/s7/session.py:44-56
  // Source signature: _dispatch(*, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _dispatch(drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s7/session.py:46-56
    End this invocation with _deepagents.dispatch_prompt(build_payload(verified, unresolved), model=cfg.models.dedup, cfg=cfg, cwd=ctx.repo_root, system_prompt=SYSTEM, max_tokens=getattr(cfg.step7_dedup, 'max_tokens', 64000), response_model=DedupDecisions, tag=tag, effort=None if drop_thinking else effort).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s7/session.py:58-74
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s7/session.py:59-67
    Enter source context managers left-to-right: stage_floors(tag, min_chars=MIN_RESPONSE_CHARS, min_tokens=MIN_RESPONSE_TOKENS) {
      // Source: vvaharness/pipeline/stages/s7/session.py:63-67
      In source order: Evaluate once dispatch_or_retry_unforced(_dispatch, 'semantic', stage=label.split('-', 1)[0], effort=_deepagents.droppable_effort(cfg.models.dedup, effort, agentic=False), may_retry=lambda: effort is not None, resend_refusal=refusal_resend_allowed(cfg, cfg.models.dedup)); assign in source target order to raw.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/pipeline/stages/s7/session.py:68-74
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/pipeline/stages/s7/session.py:69-70
    if (the source predicate is_halt_error(e) is truthy) {
      // Source: vvaharness/pipeline/stages/s7/session.py:70-70
      Raise the currently handled exception.
    }
    // Source: vvaharness/pipeline/stages/s7/session.py:71-73
    In source order: Evaluate console.write(source_template_71_22); retain side effects and discard the expression result. Then Evaluate _errlog.log(label, 'semantic', e); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s7/session.py:74-74
    End this invocation with [].
  }
  // Source: vvaharness/pipeline/stages/s7/session.py:75-75
  End this invocation with parse_decisions(raw, len(unresolved), label).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.models import is_halt_error` at source line 19: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 20: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 20: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import refusal_resend_allowed` at source line 21: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s7.outcomes import DedupDecisions, parse_decisions` at source line 23: `source_detail/vvaharness/pipeline/stages/s7/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s7.prompts import SYSTEM, build_payload` at source line 24: `source_detail/vvaharness/pipeline/stages/s7/prompts.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 25: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 27: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 27: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 28: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.response_quality import dispatch_or_retry_unforced, stage_floors` at source line 29: `source_detail/vvaharness/util/response_quality.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s7/session.py.sudo.md). Exact strings in the evidence asset support this conversion.
