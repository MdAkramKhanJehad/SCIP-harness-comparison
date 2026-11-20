# vvaharness/backends/llm/cli/oneshot.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/oneshot.py.evidence.json`. SHA-256: `6855c68be04c3b7a6766c79582f911aec3919ee950a7d2602cb7ebe86672caa7`.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/oneshot.py:22-26
In source order: Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import cancel as _cancel; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import discovery as _discovery; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import env as _env; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import envelope as _envelope; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/oneshot.py:27-39
In source order: Resolve source import from vvaharness.backends.llm.cli import retry as _retry; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import session as _session; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import ANTHROPIC_STOP_MAX_TOKENS, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, call_timeout_error, effort_scaled_seconds, note_budget_use, truncation_retry_max; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/oneshot.py:40-43
In source order: Resolve source import from vvaharness.util.response_quality import check_response_quality, output_tokens_for_gate; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/backends/llm/cli/oneshot.py:46-180
// Source signature: prompt(user_prompt: str | list[dict], *, model: str, system_prompt: str | None=None, json_schema: dict | None=None, output_format: str='text', cwd: str | None=None, max_budget_usd: float | None=None, max_tokens: int | None=None, timeout: int=1800, tag: str | None=None, effort: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prompt(user_prompt, model, system_prompt, json_schema, output_format, cwd, max_budget_usd, max_tokens, timeout, tag, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/oneshot.py:60-60
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/oneshot.py:62-66
  if (the source predicate isinstance(user_prompt, list) is truthy) {
    // Source: vvaharness/backends/llm/cli/oneshot.py:63-66
    In source order: Evaluate once source_literal_63_22.join((b.get('text', '') for b in user_prompt if isinstance(b, dict) and b.get('type') == 'text')); assign in source target order to user_prompt.
  }
  // Source: vvaharness/backends/llm/cli/oneshot.py:67-68
  if (the source predicate _cancel._ABORT.is_set() is truthy) {
    // Source: vvaharness/backends/llm/cli/oneshot.py:68-68
    Raise RuntimeError('aborted by user (Ctrl-C)').
  }
  // Source: vvaharness/backends/llm/cli/oneshot.py:69-71
  In source order: Evaluate once _env._effective_effort(effort); assign in source target order to tier. Then Evaluate once effort_scaled_seconds(timeout, tier, kind=ClockKind.REQUEST); assign in source target order to wall. Then Evaluate once [*_discovery._CLAUDE_CMD, '-p', '--model', model, *_env._effort_argv(effort)]; assign in source target order to cmd.
  // Source: vvaharness/backends/llm/cli/oneshot.py:73-74
  if (the source predicate system_prompt is truthy) {
    // Source: vvaharness/backends/llm/cli/oneshot.py:74-74
    In source order: Apply source augmented assignment cmd += ['--system-prompt', system_prompt] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/oneshot.py:76-76
  In source order: Apply source augmented assignment cmd += ['--output-format', 'json'] with source evaluation/in-place semantics.
  // Source: vvaharness/backends/llm/cli/oneshot.py:77-89
  if (the source predicate json_schema is truthy) {
    // Source: vvaharness/backends/llm/cli/oneshot.py:78-89
    if (the source predicate _discovery._cli_capabilities()['json_schema'] is truthy) {
      // Source: vvaharness/backends/llm/cli/oneshot.py:79-79
      In source order: Apply source augmented assignment cmd += ['--json-schema', json.dumps(json_schema)] with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/backends/llm/cli/oneshot.py:82-89
      In source order: Evaluate log.warning(source_literal_82_24); retain side effects and discard the expression result. Then Evaluate once source_template_87_16; assign in source target order to user_prompt.
    }
  }
  // Source: vvaharness/backends/llm/cli/oneshot.py:91-92
  if (the source predicate max_budget_usd and _discovery._cli_capabilities().get('max_budget') is truthy) {
    // Source: vvaharness/backends/llm/cli/oneshot.py:92-92
    In source order: Apply source augmented assignment cmd += ['--max-budget-usd', str(max_budget_usd)] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/oneshot.py:96-106
  In source order: Apply source augmented assignment cmd += ['--tools', ''] with source evaluation/in-place semantics. Then Apply source augmented assignment cmd += _session._confinement_argv(allowed_tools=None, disallowed_tools=None, permission_prompts=None) with source evaluation/in-place semantics. Then Evaluate once _env._call_env(max_tokens=max_tokens, effort=effort); assign in source target order to env. Then Evaluate once source_template_104_14 if tag else ''; assign in source target order to tag_sfx. Then Evaluate console.write(source_template_105_18); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/oneshot.py:109-109
  In source order: Evaluate once 0; assign in source target order to trunc_retried.
  // Source: vvaharness/backends/llm/cli/oneshot.py:110-171
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/llm/cli/oneshot.py:113-113
    In source order: Evaluate once time.monotonic(); assign in source target order to _call_start.
    // Source: vvaharness/backends/llm/cli/oneshot.py:114-128
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/oneshot.py:115-124
      In source order: Evaluate once _retry._run_with_retry(cmd, label=source_template_117_22, input=user_prompt, cwd=cwd, timeout=wall, timeout_retries=0, env=env, heartbeat_label=source_template_123_32); assign in source target order to result.
    }
    // Source: vvaharness/backends/llm/cli/oneshot.py:125-128
    On the first matching source exception subprocess.TimeoutExpired as e, in handler order {
      // Source: vvaharness/backends/llm/cli/oneshot.py:126-128
      Raise call_timeout_error(stage=tag or '', route='cli', budget_s=wall, effort=tier, cause_text=source_template_128_27) with explicit source cause e.
    }
    // Source: vvaharness/backends/llm/cli/oneshot.py:130-149
    if (the source predicate result.returncode != 0 is truthy) {
      // Source: vvaharness/backends/llm/cli/oneshot.py:131-131
      In source order: Evaluate once _retry._truncation_cap(result); assign in source target order to cap.
      // Source: vvaharness/backends/llm/cli/oneshot.py:132-134
      if (the source predicate cap is None is truthy) {
        // Source: vvaharness/backends/llm/cli/oneshot.py:133-134
        Raise RuntimeError(_discovery._format_cli_error('claude CLI failed', cmd, result)).
      }
      // Source: vvaharness/backends/llm/cli/oneshot.py:136-139
      In source order: Evaluate once max_tokens or cap; assign in source target order to requested. Then Evaluate once None if trunc_retried else truncation_retry_max(requested, cap=MODEL_MAX_OUTPUT_TOKENS); assign in source target order to retry_at.
      // Source: vvaharness/backends/llm/cli/oneshot.py:140-147
      if (the source predicate retry_at is not None is truthy) {
        // Source: vvaharness/backends/llm/cli/oneshot.py:141-146
        In source order: Evaluate _retry._log_truncation_retry(tag=tag, requested=requested, retry_at=retry_at, label='cli'); retain side effects and discard the expression result. Then Evaluate once dict(env or {}); assign in source target order to env. Then Evaluate once str(retry_at); assign in source target order to env['CLAUDE_CODE_MAX_OUTPUT_TOKENS']. Then Evaluate once retry_at; assign in source target order to trunc_retried.
        // Source: vvaharness/backends/llm/cli/oneshot.py:147-147
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/cli/oneshot.py:148-149
      Raise _retry._truncation_error(requested=requested, retried=trunc_retried, tag=tag, retry_at=retry_at).
    }
    // Source: vvaharness/backends/llm/cli/oneshot.py:152-153
    In source order: Evaluate once _envelope._parse_envelope(result.stdout, stitch_continuations=True, tag=tag); assign in source target order to (text, usage, turns, usd, stop_reason, model_usage).
    // Source: vvaharness/backends/llm/cli/oneshot.py:155-168
    if (the source predicate stop_reason == ANTHROPIC_STOP_MAX_TOKENS is truthy) {
      // Source: vvaharness/backends/llm/cli/oneshot.py:156-159
      In source order: Evaluate once max_tokens or MODEL_MAX_OUTPUT_TOKENS; assign in source target order to requested. Then Evaluate once None if trunc_retried else truncation_retry_max(requested, cap=MODEL_MAX_OUTPUT_TOKENS); assign in source target order to retry_at.
      // Source: vvaharness/backends/llm/cli/oneshot.py:160-166
      if (the source predicate retry_at is not None is truthy) {
        // Source: vvaharness/backends/llm/cli/oneshot.py:161-165
        In source order: Evaluate _retry._log_truncation_retry(tag=tag, requested=requested, retry_at=retry_at, label='cli'); retain side effects and discard the expression result. Then Evaluate once dict(env or {}); assign in source target order to env. Then Evaluate once str(retry_at); assign in source target order to env['CLAUDE_CODE_MAX_OUTPUT_TOKENS']. Then Evaluate once retry_at; assign in source target order to trunc_retried.
        // Source: vvaharness/backends/llm/cli/oneshot.py:166-166
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/cli/oneshot.py:167-168
      Raise _retry._truncation_error(requested=requested, retried=trunc_retried, tag=tag, retry_at=retry_at).
    }
    // Source: vvaharness/backends/llm/cli/oneshot.py:169-170
    if (the source predicate trunc_retried is truthy) {
      // Source: vvaharness/backends/llm/cli/oneshot.py:170-170
      In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/oneshot.py:171-171
    Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
  }
  // Source: vvaharness/backends/llm/cli/oneshot.py:173-177
  In source order: Evaluate note_budget_use(time.monotonic() - _call_start, wall, tier); retain side effects and discard the expression result. Then Evaluate _envelope._note_unparsed_cache_keys(usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(usage, usd=usd, turns=turns); retain side effects and discard the expression result. Then Evaluate _retry._log_usage(usage, stop_reason=stop_reason, model_usage=model_usage); retain side effects and discard the expression result. Then Evaluate _envelope._raise_if_refused(stop_reason, tag=tag, stdout=result.stdout); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/oneshot.py:178-179
  In source order: Evaluate check_response_quality(text, stage=tag or '', output_tokens=output_tokens_for_gate(usage)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/oneshot.py:180-180
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS` at source line 22: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 23: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 23: `source_detail/vvaharness/backends/llm/cli/cancel.py.sudo.md`.
- `from vvaharness.backends.llm.cli import discovery as _discovery` at source line 24: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import discovery as _discovery` at source line 24: `source_detail/vvaharness/backends/llm/cli/discovery.py.sudo.md`.
- `from vvaharness.backends.llm.cli import env as _env` at source line 25: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import env as _env` at source line 25: `source_detail/vvaharness/backends/llm/cli/env.py.sudo.md`.
- `from vvaharness.backends.llm.cli import envelope as _envelope` at source line 26: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import envelope as _envelope` at source line 26: `source_detail/vvaharness/backends/llm/cli/envelope.py.sudo.md`.
- `from vvaharness.backends.llm.cli import retry as _retry` at source line 27: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import retry as _retry` at source line 27: `source_detail/vvaharness/backends/llm/cli/retry.py.sudo.md`.
- `from vvaharness.backends.llm.cli import session as _session` at source line 28: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import session as _session` at source line 28: `source_detail/vvaharness/backends/llm/cli/session.py.sudo.md`.
- `from vvaharness.backends.llm.models import ANTHROPIC_STOP_MAX_TOKENS, TRUNCATED_RETRY_RECOVERED_COUNTER, ClockKind, call_timeout_error, effort_scaled_seconds, note_budget_use, truncation_retry_max` at source line 29: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 38: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 38: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 38: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 39: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.response_quality import check_response_quality, output_tokens_for_gate` at source line 40: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 41: `source_detail/vvaharness/util/tokens.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/llm/cli/oneshot.py.sudo.md). Exact strings in the evidence asset support this conversion.
