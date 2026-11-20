# vvaharness/backends/llm/cli/retry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/retry.py.evidence.json`. SHA-256: `bf7d5dfaa5fab07fd1127dfefaafe16d1e22b1dd2c77ba26e05b931af07c0ad5`.

```sudo
// Source: vvaharness/backends/llm/cli/retry.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/retry.py:21-31
In source order: Resolve source import import time; preserve alias and import-time effects. Then Resolve source import import uuid; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import AuthenticationError, ProxyError, TruncatedResponseError, truncated_below_budget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import cancel as _cancel; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/retry.py:32-48
In source order: Resolve source import from vvaharness.backends.llm.cli import envelope as _envelope; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.cli import process as _process; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import CLI_CONN_TRANSIENT_RX, CLI_RETRYABLE_STATUS, CLI_STATUS_429_RX, CLI_TOKEN_CAP_RX, LLM_TRUNCATED_BELOW_BUDGET_COUNTER, PROXY_CAUSE_RX, RATE_LIMIT_TRANSIENT_RX, TIMEOUT_MAX_RETRIES, TRUNCATED_REPLIES_COUNTER, TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/retry.py:49-56
In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once re.compile('hit your (usage )?limit.*resets', re.IGNORECASE); assign in source target order to _RL_HARD_CAP.
// Source: vvaharness/backends/llm/cli/retry.py:57-71
In source order: Evaluate once 4; assign in source target order to _RL_MAX_RETRIES. Then Evaluate once (30, 60, 120, 240); assign in source target order to _RL_BACKOFF. Then Evaluate once TIMEOUT_MAX_RETRIES; assign in source target order to _TIMEOUT_MAX_RETRIES. Then Evaluate once re.compile(source_literal_64_4, re.IGNORECASE); assign in source target order to _PENDING_RESULT_RX. Then Evaluate once 3; assign in source target order to _PENDING_MAX_RETRIES.
// Source: vvaharness/backends/llm/cli/retry.py:72-72
In source order: Evaluate once (5, 15, 30); assign in source target order to _PENDING_BACKOFF.
// Source: vvaharness/backends/llm/cli/retry.py:75-78
// Source signature: _is_pending_result(text: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_pending_result(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:76-77
  if (the source predicate not isinstance(text, str) is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:77-77
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:78-78
  End this invocation with bool(_PENDING_RESULT_RX.search(text)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:82-95
In source order: Evaluate once re.compile(source_literal_83_4, re.IGNORECASE); assign in source target order to _AUTH_FAILURE. Then Evaluate once 3; assign in source target order to _AUTH_MAX_RETRIES. Then Evaluate once (2, 4, 8); assign in source target order to _AUTH_BACKOFF. Then Evaluate once PROXY_CAUSE_RX; assign in source target order to _PROXY_FAILURE.
// Source: vvaharness/backends/llm/cli/retry.py:98-104
// Source signature: _envelope_fields(env: dict) -> tuple[int | None, str | None, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _envelope_fields(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:99-101
  In source order: Retain source documentation literal source_literal_99_4; it is not a model call. Then Evaluate once env.get('api_error_status'); assign in source target order to status. Then Evaluate once env.get('result') or env.get('error') or env.get('message'); assign in source target order to text.
  // Source: vvaharness/backends/llm/cli/retry.py:102-104
  End this invocation with (status if isinstance(status, int) else None, text if isinstance(text, str) else None, True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:107-123
// Source signature: _last_result_line(stdout: str) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _last_result_line(stdout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:108-112
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/retry.py:113-122
  for each line in reversed(stdout.splitlines()) {
    // Source: vvaharness/backends/llm/cli/retry.py:114-114
    In source order: Evaluate once line.strip(); assign in source target order to line.
    // Source: vvaharness/backends/llm/cli/retry.py:115-116
    if (the source predicate not line is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:116-116
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:117-120
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/retry.py:118-118
      In source order: Evaluate once json.loads(line); assign in source target order to evt.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:119-120
    On the first matching source exception (json.JSONDecodeError, TypeError), in handler order {
      // Source: vvaharness/backends/llm/cli/retry.py:120-120
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:121-122
    if (the source predicate isinstance(evt, dict) and evt.get('type') == 'result' is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:122-122
      End this invocation with evt.
    }
  }
  // Source: vvaharness/backends/llm/cli/retry.py:123-123
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:126-147
// Source signature: _terminal_result_fields(stdout: str | None) -> tuple[int | None, str | None, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _terminal_result_fields(stdout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:128-128
  In source order: Retain source documentation literal source_literal_128_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/retry.py:129-130
  if (the source predicate not stdout is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:130-130
    End this invocation with (None, None, False).
  }
  // Source: vvaharness/backends/llm/cli/retry.py:131-132
  In source order: Evaluate once stdout.strip(); assign in source target order to s. Then Evaluate once [p for p in (s.find('{'), s.find('[')) if p >= 0]; assign in source target order to candidates.
  // Source: vvaharness/backends/llm/cli/retry.py:133-134
  if (the source predicate not candidates is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:134-134
    End this invocation with (None, None, False).
  }
  // Source: vvaharness/backends/llm/cli/retry.py:135-139
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/retry.py:136-136
    In source order: Evaluate once json.loads(s[min(candidates):]); assign in source target order to env.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:137-139
  On the first matching source exception (json.JSONDecodeError, ValueError, TypeError), in handler order {
    // Source: vvaharness/backends/llm/cli/retry.py:138-138
    In source order: Evaluate once _last_result_line(s); assign in source target order to env.
    // Source: vvaharness/backends/llm/cli/retry.py:139-139
    End this invocation with _envelope_fields(env) if env is not None else (None, None, False).
  }
  // Source: vvaharness/backends/llm/cli/retry.py:140-144
  if (the source predicate isinstance(env, list) is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:141-142
    In source order: Evaluate once next((e for e in reversed(env) if isinstance(e, dict) and e.get('type') == 'result'), None); assign in source target order to env.
    // Source: vvaharness/backends/llm/cli/retry.py:143-144
    if (the source predicate env is None is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:144-144
      End this invocation with (None, None, False).
    }
  }
  // Source: vvaharness/backends/llm/cli/retry.py:145-146
  if (the source predicate not isinstance(env, dict) is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:146-146
    End this invocation with (None, None, False).
  }
  // Source: vvaharness/backends/llm/cli/retry.py:147-147
  End this invocation with _envelope_fields(env).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:150-161
// Source signature: _truncation_cap(result: subprocess.CompletedProcess) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _truncation_cap(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:151-155
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then Evaluate once _terminal_result_fields(result.stdout); assign in source target order to (_status, text, found). Then Evaluate once text if found and text else source_template_154_39; assign in source target order to blob. Then Evaluate once CLI_TOKEN_CAP_RX.search(blob or ''); assign in source target order to m.
  // Source: vvaharness/backends/llm/cli/retry.py:156-157
  if (the source predicate not m is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:157-157
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:158-161
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/retry.py:159-159
    End this invocation with int(m.group(1)).
  }
  // Source: vvaharness/backends/llm/cli/retry.py:160-161
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/backends/llm/cli/retry.py:161-161
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:164-179
// Source signature: _truncation_error(*, requested: int, retried: int, tag: str | None, retry_at: int | None, produced: int | None=None) -> TruncatedResponseError
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _truncation_error(requested, retried, tag, retry_at, produced) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:167-168
  In source order: Retain source documentation literal source_literal_167_4; it is not a model call. Then Evaluate COUNTERS.bump(TRUNCATED_REPLIES_COUNTER); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/retry.py:169-170
  if (the source predicate truncated_below_budget(produced, requested) is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:170-170
    In source order: Evaluate COUNTERS.bump(LLM_TRUNCATED_BELOW_BUDGET_COUNTER); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:171-177
  if (the source predicate retried is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:172-172
    In source order: Evaluate once 'reply still hit the output-token budget after the doubled retry'; assign in source target order to msg.
  }
  else {
    // Source: vvaharness/backends/llm/cli/retry.py:173-177
    if (the source predicate retry_at is None is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:174-175
      In source order: Evaluate once source_template_174_15; assign in source target order to msg.
    }
    else {
      // Source: vvaharness/backends/llm/cli/retry.py:177-177
      In source order: Evaluate once 'reply hit the output-token budget with no retry budget left'; assign in source target order to msg.
    }
  }
  // Source: vvaharness/backends/llm/cli/retry.py:178-179
  End this invocation with TruncatedResponseError(msg, stage=tag or '', requested=requested, retried=retried, produced=produced).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:182-191
// Source signature: _log_truncation_retry(*, tag: str | None, requested: int, retry_at: int, label: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _log_truncation_retry(tag, requested, retry_at, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:184-191
  In source order: Retain source documentation literal source_literal_184_4; it is not a model call. Then Evaluate COUNTERS.bump(TRUNCATED_RETRY_ATTEMPTED_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.TRUNCATED_RETRY, route=label, budget=requested, retry_at=retry_at); retain side effects and discard the expression result. Then Evaluate _errlog.log(tag or label, tag or 'truncation', source_template_189_8, error_code=TruncatedResponseError.error_code, recovered=True); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:194-198
// Source signature: _accept_reply(text: str, *, trunc_retried: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _accept_reply(text, trunc_retried) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:195-195
  In source order: Retain source documentation literal source_literal_195_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/retry.py:196-197
  if (the source predicate trunc_retried is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:197-197
    In source order: Evaluate COUNTERS.bump(TRUNCATED_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:198-198
  End this invocation with text.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:201-218
// Source signature: _is_transient_failure(result: subprocess.CompletedProcess) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_transient_failure(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:202-203
  In source order: Retain source documentation literal source_literal_202_4; it is not a model call. Then Evaluate once _terminal_result_fields(result.stdout); assign in source target order to (status, text, found).
  // Source: vvaharness/backends/llm/cli/retry.py:204-212
  if (the source predicate found is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:205-206
    if (the source predicate status in CLI_RETRYABLE_STATUS is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:206-206
      End this invocation with True.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:208-211
    if (the source predicate status is None and text and (RATE_LIMIT_TRANSIENT_RX.search(text) or CLI_STATUS_429_RX.search(text) or CLI_CONN_TRANSIENT_RX.search(text)) is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:211-211
      End this invocation with True.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:212-212
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:216-218
  End this invocation with bool(RATE_LIMIT_TRANSIENT_RX.search(result.stderr or '') or CLI_STATUS_429_RX.search(result.stderr or '') or CLI_CONN_TRANSIENT_RX.search(result.stderr or '')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:221-232
// Source signature: _is_auth_failure(result: subprocess.CompletedProcess) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_auth_failure(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:222-223
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call. Then Evaluate once _terminal_result_fields(result.stdout); assign in source target order to (status, text, found).
  // Source: vvaharness/backends/llm/cli/retry.py:224-227
  if (the source predicate found is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:225-226
    if (the source predicate status == 401 is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:226-226
      End this invocation with True.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:227-227
    End this invocation with bool(text and _AUTH_FAILURE.search(text)).
  }
  // Source: vvaharness/backends/llm/cli/retry.py:232-232
  End this invocation with bool(_AUTH_FAILURE.search(result.stderr or '')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:235-253
// Source signature: _proxy_failure_evidence(result: subprocess.CompletedProcess) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _proxy_failure_evidence(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:236-238
  In source order: Retain source documentation literal source_literal_236_4; it is not a model call. Then Evaluate once _terminal_result_fields(result.stdout); assign in source target order to (status, text, found).
  // Source: vvaharness/backends/llm/cli/retry.py:239-248
  if (the source predicate found is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:240-241
    if (the source predicate status == 407 is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:241-241
      End this invocation with 'terminal result reported status 407'.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:242-242
    In source order: Evaluate once text or ''; assign in source target order to haystack.
  }
  else {
    // Source: vvaharness/backends/llm/cli/retry.py:248-248
    In source order: Evaluate once source_template_248_19; assign in source target order to haystack.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:249-249
  In source order: Evaluate once _PROXY_FAILURE.search(haystack); assign in source target order to m.
  // Source: vvaharness/backends/llm/cli/retry.py:250-251
  if (the source predicate m is None is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:251-251
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:252-252
  In source order: Evaluate once (max(0, m.start() - 120), min(len(haystack), m.end() + 120)); assign in source target order to (lo, hi).
  // Source: vvaharness/backends/llm/cli/retry.py:253-253
  End this invocation with source_template_253_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:256-258
// Source signature: _is_proxy_failure(result: subprocess.CompletedProcess) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_proxy_failure(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:257-257
  In source order: Retain source documentation literal source_literal_257_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/retry.py:258-258
  End this invocation with _proxy_failure_evidence(result) is not None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:261-264
// Source signature: _rotate_session_id(cmd: list[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rotate_session_id(cmd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:262-262
  In source order: Retain source documentation literal source_literal_262_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/retry.py:263-264
  if (the source predicate '--session-id' in cmd is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:264-264
    In source order: Evaluate once str(uuid.uuid4()); assign in source target order to cmd[cmd.index('--session-id') + 1].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:267-330
// Source signature: _run_with_retry(cmd: list[str], *, label: str, timeout_retries: int=_TIMEOUT_MAX_RETRIES, **kw) -> subprocess.CompletedProcess
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _run_with_retry(cmd, label, timeout_retries, kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:270-274
  In source order: Retain source documentation literal source_literal_270_4; it is not a model call. Then Evaluate once 0; assign in source target order to attempt. Then Evaluate once 0; assign in source target order to auth_attempt. Then Evaluate once 0; assign in source target order to timeout_attempt.
  // Source: vvaharness/backends/llm/cli/retry.py:275-330
  while (the source predicate True is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:276-285
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/retry.py:277-277
      In source order: Evaluate once _process._run(cmd, **kw); assign in source target order to result.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:278-285
    On the first matching source exception subprocess.TimeoutExpired, in handler order {
      // Source: vvaharness/backends/llm/cli/retry.py:280-281
      if (the source predicate _cancel._ABORT.is_set() or timeout_attempt >= timeout_retries is truthy) {
        // Source: vvaharness/backends/llm/cli/retry.py:281-281
        Raise the currently handled exception.
      }
      // Source: vvaharness/backends/llm/cli/retry.py:282-284
      In source order: Apply source augmented assignment timeout_attempt += 1 with source evaluation/in-place semantics. Then Evaluate console.write(source_template_283_26); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/retry.py:285-285
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:286-287
    if (the source predicate result.returncode == 0 is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:287-287
      End this invocation with result.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:288-294
    In source order: Evaluate once _terminal_result_fields(result.stdout); assign in source target order to (_, text, _). Then Evaluate once text or source_template_289_27; assign in source target order to err_text. Then Evaluate _envelope._raise_if_refused_exit(result.stdout, tag=label); retain side effects and discard the expression result. Then Evaluate once _proxy_failure_evidence(result); assign in source target order to proxy_evidence.
    // Source: vvaharness/backends/llm/cli/retry.py:295-302
    if (the source predicate proxy_evidence is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:296-302
      Raise ProxyError(source_template_298_16, status_code=407 if re.search('\\b407\\b', err_text) else None, backend='cli').
    }
    // Source: vvaharness/backends/llm/cli/retry.py:303-314
    if (the source predicate _is_auth_failure(result) is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:304-312
      if (the source predicate auth_attempt < _AUTH_MAX_RETRIES is truthy) {
        // Source: vvaharness/backends/llm/cli/retry.py:305-311
        In source order: Evaluate once _AUTH_BACKOFF[min(auth_attempt, len(_AUTH_BACKOFF) - 1)]; assign in source target order to wait. Then Evaluate console.write(source_template_306_30); retain side effects and discard the expression result. Then Evaluate time.sleep(wait); retain side effects and discard the expression result. Then Apply source augmented assignment auth_attempt += 1 with source evaluation/in-place semantics. Then Evaluate _rotate_session_id(cmd); retain side effects and discard the expression result.
        // Source: vvaharness/backends/llm/cli/retry.py:312-312
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/backends/llm/cli/retry.py:313-314
      Raise AuthenticationError(redact(err_text)[:400], status_code=401, backend='cli').
    }
    // Source: vvaharness/backends/llm/cli/retry.py:315-317
    if (the source predicate _RL_HARD_CAP.search(err_text) is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:316-316
      In source order: Evaluate console.write(source_template_316_26); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/retry.py:317-317
      End this invocation with result.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:318-319
    if (the source predicate attempt >= _RL_MAX_RETRIES or not _is_transient_failure(result) is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:319-319
      End this invocation with result.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:320-323
    In source order: Evaluate once _RL_BACKOFF[min(attempt, len(_RL_BACKOFF) - 1)]; assign in source target order to wait. Then Evaluate console.write(source_template_321_22); retain side effects and discard the expression result. Then Evaluate once 0; assign in source target order to slept.
    // Source: vvaharness/backends/llm/cli/retry.py:324-328
    while (the source predicate slept < wait is truthy) {
      // Source: vvaharness/backends/llm/cli/retry.py:325-326
      if (the source predicate _cancel._ABORT.is_set() is truthy) {
        // Source: vvaharness/backends/llm/cli/retry.py:326-326
        Raise RuntimeError('aborted by user (Ctrl-C)').
      }
      // Source: vvaharness/backends/llm/cli/retry.py:327-328
      In source order: Evaluate time.sleep(min(5, wait - slept)); retain side effects and discard the expression result. Then Apply source augmented assignment slept += 5 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:329-330
    In source order: Evaluate _rotate_session_id(cmd); retain side effects and discard the expression result. Then Apply source augmented assignment attempt += 1 with source evaluation/in-place semantics.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/retry.py:333-353
// Source signature: _log_usage(usage: dict | None, *, stop_reason: str | None=None, model_usage: dict | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _log_usage(usage, stop_reason, model_usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/retry.py:335-335
  In source order: Retain source documentation literal source_literal_335_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/retry.py:337-338
  if (the source predicate not usage is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:338-338
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:339-344
  In source order: Evaluate once int(usage.get('cache_read_input_tokens', 0) or 0); assign in source target order to _cache_r. Then Evaluate once int(usage.get('cache_creation_input_tokens', 0) or 0); assign in source target order to _cache_w. Then Evaluate once int(usage.get('input_tokens', 0) or 0) + _cache_r + _cache_w; assign in source target order to _in. Then Evaluate once int(usage.get('output_tokens', 0) or 0); assign in source target order to _out. Then Evaluate once source_template_343_18 if _cache_r or _cache_w else ''; assign in source target order to cache_info.
  // Source: vvaharness/backends/llm/cli/retry.py:345-345
  In source order: Evaluate once source_template_345_12 if stop_reason else ''; assign in source target order to extra.
  // Source: vvaharness/backends/llm/cli/retry.py:346-352
  if (the source predicate model_usage is truthy) {
    // Source: vvaharness/backends/llm/cli/retry.py:348-348
    In source order: Evaluate once []; assign in source target order to echoes.
    // Source: vvaharness/backends/llm/cli/retry.py:349-351
    for each (resolved, spend) in model_usage.items() {
      // Source: vvaharness/backends/llm/cli/retry.py:350-351
      In source order: Evaluate once (spend or {}).get('costUSD') if isinstance(spend, dict) else None; assign in source target order to cost. Then Evaluate echoes.append(source_template_351_26 + (source_template_351_43 if cost is not None else '')); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/retry.py:352-352
    In source order: Apply source augmented assignment extra += source_template_352_17 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/backends/llm/cli/retry.py:353-353
  In source order: Evaluate console.write(source_template_353_18); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.harness.deepagents.limits import MODEL_MAX_OUTPUT_TOKENS` at source line 24: `source_detail/vvaharness/backends/harness/deepagents/limits.py.sudo.md`.
- `from vvaharness.backends.harness.models import AuthenticationError, ProxyError, TruncatedResponseError, truncated_below_budget` at source line 25: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 31: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import cancel as _cancel` at source line 31: `source_detail/vvaharness/backends/llm/cli/cancel.py.sudo.md`.
- `from vvaharness.backends.llm.cli import envelope as _envelope` at source line 32: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import envelope as _envelope` at source line 32: `source_detail/vvaharness/backends/llm/cli/envelope.py.sudo.md`.
- `from vvaharness.backends.llm.cli import process as _process` at source line 33: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm.cli import process as _process` at source line 33: `source_detail/vvaharness/backends/llm/cli/process.py.sudo.md`.
- `from vvaharness.backends.llm.models import CLI_CONN_TRANSIENT_RX, CLI_RETRYABLE_STATUS, CLI_STATUS_429_RX, CLI_TOKEN_CAP_RX, LLM_TRUNCATED_BELOW_BUDGET_COUNTER, PROXY_CAUSE_RX, RATE_LIMIT_TRANSIENT_RX, TIMEOUT_MAX_RETRIES, TRUNCATED_REPLIES_COUNTER, TRUNCATED_RETRY_ATTEMPTED_COUNTER, TRUNCATED_RETRY_RECOVERED_COUNTER` at source line 34: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 47: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 48: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 48: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 48: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 49: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 49: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 50: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 51: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/llm/cli/retry.py.sudo.md). Exact strings in the evidence asset support this conversion.
