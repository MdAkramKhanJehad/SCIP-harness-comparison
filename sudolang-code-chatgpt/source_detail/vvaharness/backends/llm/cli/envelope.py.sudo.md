# vvaharness/backends/llm/cli/envelope.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/envelope.py.evidence.json`. SHA-256: `f159d7d21387bf3b0857561883d122eebf2df869de72a9d0f05d60652f2bb601`.

```sudo
// Source: vvaharness/backends/llm/cli/envelope.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cache as _cache; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/envelope.py:22-33
In source order: Resolve source import from vvaharness.backends.llm.models import ANTHROPIC_STOP_REFUSAL, CLI_CONTINUED_REPLIES_COUNTER, EnvelopeResult, GuardrailBlocked, model_refusal, refusal_category; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/envelope.py:36-46
In source order: Resolve source import from vvaharness.util.tokens import TOKENS, TokenUsage; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once frozenset({'Your request was not allowed'}); assign in source target order to _GUARDRAIL_REFUSALS.
// Source: vvaharness/backends/llm/cli/envelope.py:49-60
// Source signature: _check_guardrail(env: dict) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_guardrail(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:50-50
  In source order: Evaluate once env.get('result'); assign in source target order to text.
  // Source: vvaharness/backends/llm/cli/envelope.py:51-60
  if (the source predicate isinstance(text, str) and text.strip() in _GUARDRAIL_REFUSALS and ((env.get('num_turns') or 1) <= 1) and (not env.get('is_error')) is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:55-55
    In source order: Evaluate once (env.get('usage') or {}).get('output_tokens'); assign in source target order to out_tok.
    // Source: vvaharness/backends/llm/cli/envelope.py:56-60
    Raise GuardrailBlocked(source_template_57_12).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:63-68
// Source signature: _spend_of(event: dict | None) -> tuple[int | None, float | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _spend_of(event) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:64-66
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Evaluate once (event or {}).get('num_turns'); assign in source target order to turns. Then Evaluate once (event or {}).get('total_cost_usd'); assign in source target order to usd.
  // Source: vvaharness/backends/llm/cli/envelope.py:67-68
  End this invocation with (turns if isinstance(turns, int) else None, float(usd) if isinstance(usd, (int, float)) else None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:71-79
// Source signature: _structured_text(event: dict | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _structured_text(event) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:72-73
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once (event or {}).get('structured_output'); assign in source target order to payload.
  // Source: vvaharness/backends/llm/cli/envelope.py:74-75
  if (the source predicate not isinstance(payload, (dict, list)) is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:75-75
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:76-79
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/envelope.py:77-77
    End this invocation with json.dumps(payload).
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:78-79
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/backends/llm/cli/envelope.py:79-79
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:82-88
// Source signature: _telemetry_of(event: dict | None) -> tuple[str | None, dict | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _telemetry_of(event) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:83-86
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call. Then Evaluate once (event or {}).get('stop_reason'); assign in source target order to stop. Then Evaluate once (event or {}).get('modelUsage'); assign in source target order to usage.
  // Source: vvaharness/backends/llm/cli/envelope.py:87-88
  End this invocation with (stop if isinstance(stop, str) else None, usage if isinstance(usage, dict) else None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:91-106
// Source signature: _decode_stream(stdout: str) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _decode_stream(stdout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/envelope.py:93-96
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/envelope.py:94-94
    End this invocation with json.loads(stdout).
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:95-96
  On the first matching source exception (json.JSONDecodeError, TypeError), in handler order {
    // Source: vvaharness/backends/llm/cli/envelope.py:96-96
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:97-97
  In source order: For objs, assign []; source annotation list.
  // Source: vvaharness/backends/llm/cli/envelope.py:98-105
  for each ln in stdout.splitlines() {
    // Source: vvaharness/backends/llm/cli/envelope.py:99-99
    In source order: Evaluate once ln.strip(); assign in source target order to ln.
    // Source: vvaharness/backends/llm/cli/envelope.py:100-101
    if (the source predicate not ln is truthy) {
      // Source: vvaharness/backends/llm/cli/envelope.py:101-101
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/cli/envelope.py:102-105
    Perform the following protected operations {
      // Source: vvaharness/backends/llm/cli/envelope.py:103-103
      In source order: Evaluate objs.append(json.loads(ln)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/envelope.py:104-105
    On the first matching source exception (json.JSONDecodeError, TypeError), in handler order {
      // Source: vvaharness/backends/llm/cli/envelope.py:105-105
      Continue the immediately enclosing source loop at its next iteration.
    }
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:106-106
  End this invocation with objs or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:109-114
// Source signature: _stream_events(stdout: str) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stream_events(stdout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:110-112
  In source order: Retain source documentation literal source_literal_110_4; it is not a model call. Then Evaluate once _decode_stream(stdout); assign in source target order to doc. Then Evaluate once doc if isinstance(doc, list) else [doc]; assign in source target order to items.
  // Source: vvaharness/backends/llm/cli/envelope.py:113-114
  End this invocation with [e for item in items for e in (item if isinstance(item, list) else [item]) if isinstance(e, dict)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:117-131
// Source signature: _refusal_category_of(stdout: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refusal_category_of(stdout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:118-125
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call. Then Evaluate once _stream_events(stdout); assign in source target order to events. Then Evaluate once [e['message'] for e in events if e.get('type') == 'assistant' and isinstance(e.get('message'), dict) and (e['message'].get('stop_reason') == ANTHROPIC_STOP_REFUSAL)]; assign in source target order to refused. Then Evaluate once refusal_category(refused[-1]) if refused else None; assign in source target order to category.
  // Source: vvaharness/backends/llm/cli/envelope.py:126-127
  if (the source predicate category is not None is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:127-127
    End this invocation with category.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:128-130
  In source order: Evaluate once next((e.get('apiRefusalCategory') for e in reversed(events) if e.get('type') == 'system' and e.get('subtype') == 'model_refusal_no_fallback'), None); assign in source target order to api.
  // Source: vvaharness/backends/llm/cli/envelope.py:131-131
  End this invocation with api if isinstance(api, str) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:134-140
// Source signature: _raise_if_refused(stop_reason: str | None, *, tag: str | None, stdout: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raise_if_refused(stop_reason, tag, stdout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:135-135
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/envelope.py:138-140
  if (the source predicate stop_reason == ANTHROPIC_STOP_REFUSAL is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:139-140
    Raise model_refusal(route='cli', stage=tag or '', category=_refusal_category_of(stdout)).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:143-155
// Source signature: _raise_if_refused_exit(stdout: str, *, tag: str | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raise_if_refused_exit(stdout, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:144-144
  In source order: Retain source documentation literal source_literal_144_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/envelope.py:147-150
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/envelope.py:148-148
    In source order: Evaluate once _parse_envelope(stdout); assign in source target order to env_res.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:149-150
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/llm/cli/envelope.py:150-150
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:151-152
  if (the source predicate env_res.stop_reason != ANTHROPIC_STOP_REFUSAL is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:152-152
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:153-155
  In source order: Evaluate _note_unparsed_cache_keys(env_res.usage); retain side effects and discard the expression result. Then Evaluate TOKENS.add(env_res.usage, usd=env_res.usd, turns=env_res.turns); retain side effects and discard the expression result. Then Evaluate _raise_if_refused(env_res.stop_reason, tag=tag, stdout=stdout); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:158-167
// Source signature: _assistant_text(events: list) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _assistant_text(events) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:159-160
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call. Then For parts, assign []; source annotation list[str].
  // Source: vvaharness/backends/llm/cli/envelope.py:161-166
  for each evt in events {
    // Source: vvaharness/backends/llm/cli/envelope.py:162-163
    if (the source predicate not isinstance(evt, dict) or evt.get('type') != 'assistant' is truthy) {
      // Source: vvaharness/backends/llm/cli/envelope.py:163-163
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/llm/cli/envelope.py:164-166
    for each blk in (evt.get('message', {}) or {}).get('content', []) or [] {
      // Source: vvaharness/backends/llm/cli/envelope.py:165-166
      if (the source predicate isinstance(blk, dict) and blk.get('type') == 'text' is truthy) {
        // Source: vvaharness/backends/llm/cli/envelope.py:166-166
        In source order: Evaluate parts.append(blk.get('text', '')); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:167-167
  End this invocation with ''.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:170-184
// Source signature: _stitch_continuation(events: list, result_text: str, *, turns: int | None, tag: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stitch_continuation(events, result_text, turns, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:172-172
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/envelope.py:174-175
  if (the source predicate not turns or turns <= 1 is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:175-175
    End this invocation with result_text.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:176-177
  In source order: Evaluate once _assistant_text(events).strip(); assign in source target order to stitched. Then Evaluate once result_text.strip(); assign in source target order to body.
  // Source: vvaharness/backends/llm/cli/envelope.py:178-180
  if (the source predicate not stitched or not body or stitched == body or (not stitched.endswith(body)) is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:180-180
    End this invocation with result_text.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:181-183
  In source order: Evaluate COUNTERS.bump(CLI_CONTINUED_REPLIES_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.CLI_REPLY_SPLIT_ACROSS_TURNS, turns=turns, tag=tag or None, result_chars=len(body), stream_chars=len(stitched)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/envelope.py:184-184
  End this invocation with stitched.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:187-239
// Source signature: _parse_envelope(stdout: str, *, stitch_continuations: bool=False, tag: str | None=None) -> EnvelopeResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_envelope(stdout, stitch_continuations, tag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:189-190
  In source order: Retain source documentation literal source_literal_189_4; it is not a model call. Then Evaluate once _decode_stream(stdout); assign in source target order to env.
  // Source: vvaharness/backends/llm/cli/envelope.py:191-192
  if (the source predicate env is None is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:192-192
    End this invocation with EnvelopeResult(stdout.strip(), None).
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:194-223
  if (the source predicate isinstance(env, list) is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:195-197
    In source order: Evaluate once next((e for e in reversed(env) if isinstance(e, dict) and e.get('type') == 'result'), None); assign in source target order to result_evt.
    // Source: vvaharness/backends/llm/cli/envelope.py:198-199
    if (the source predicate result_evt is truthy) {
      // Source: vvaharness/backends/llm/cli/envelope.py:199-199
      In source order: Evaluate _check_guardrail(result_evt); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/llm/cli/envelope.py:200-201
    In source order: Evaluate once (result_evt or {}).get('usage'); assign in source target order to usage. Then Evaluate once _structured_text(result_evt) or (result_evt or {}).get('result'); assign in source target order to text.
    // Source: vvaharness/backends/llm/cli/envelope.py:202-214
    if (the source predicate not isinstance(text, str) or not text.strip() is truthy) {
      // Source: vvaharness/backends/llm/cli/envelope.py:203-214
      In source order: Evaluate once next((e for e in reversed(env) if isinstance(e, dict) and e.get('type') == 'assistant'), None); assign in source target order to last_asst. Then Evaluate once [blk.get('text', '') for blk in ((last_asst or {}).get('message', {}) or {}).get('content', []) or [] if isinstance(blk, dict) and blk.get('type') == 'text']; assign in source target order to parts. Then Evaluate once ''.join(parts); assign in source target order to text.
    }
    // Source: vvaharness/backends/llm/cli/envelope.py:215-217
    In source order: Evaluate once _spend_of(result_evt); assign in source target order to (turns, usd). Then Evaluate once _telemetry_of(result_evt); assign in source target order to (stop_reason, model_usage). Then Evaluate once text.strip(); assign in source target order to text.
    // Source: vvaharness/backends/llm/cli/envelope.py:218-219
    if (the source predicate stitch_continuations is truthy) {
      // Source: vvaharness/backends/llm/cli/envelope.py:219-219
      In source order: Evaluate once _stitch_continuation(env, text, turns=turns, tag=tag); assign in source target order to text.
    }
    // Source: vvaharness/backends/llm/cli/envelope.py:220-223
    End this invocation with EnvelopeResult(text, cast('TokenUsage', usage) if isinstance(usage, dict) else None, turns, usd, stop_reason, model_usage).
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:225-226
  if (the source predicate not isinstance(env, dict) is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:226-226
    End this invocation with EnvelopeResult(stdout.strip(), None).
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:227-228
  In source order: Evaluate _check_guardrail(env); retain side effects and discard the expression result. Then Evaluate once _structured_text(env) or env.get('result'); assign in source target order to result.
  // Source: vvaharness/backends/llm/cli/envelope.py:229-231
  if (the source predicate not isinstance(result, str) is truthy) {
    // Source: vvaharness/backends/llm/cli/envelope.py:231-231
    In source order: Evaluate once ''; assign in source target order to result.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:232-234
  In source order: Evaluate once env.get('usage'); assign in source target order to raw_usage. Then Evaluate once _spend_of(env); assign in source target order to (turns, usd). Then Evaluate once _telemetry_of(env); assign in source target order to (stop_reason, model_usage).
  // Source: vvaharness/backends/llm/cli/envelope.py:236-239
  End this invocation with EnvelopeResult(result.strip(), cast('TokenUsage', raw_usage) if isinstance(raw_usage, dict) else None, turns, usd, stop_reason, model_usage).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:242-242
In source order: Evaluate once _cache.ANTHROPIC_PARSED_CACHE_KEYS; assign in source target order to _PARSED_USAGE_CACHE_KEYS.
// Source: vvaharness/backends/llm/cli/envelope.py:245-247
// Source signature: _note_unparsed_cache_keys(usage: dict | None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _note_unparsed_cache_keys(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:246-247
  In source order: Retain source documentation literal source_literal_246_4; it is not a model call. Then Evaluate _cache.note_unparsed_cache_keys(usage, via='cli'); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/envelope.py:252-265
// Source signature: parse_json_response(text: str) -> dict | list
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_json_response(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/envelope.py:253-253
  In source order: Retain source documentation literal source_literal_253_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/envelope.py:254-263
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/envelope.py:255-255
    In source order: Evaluate once json.loads(text); assign in source target order to envelope.
    // Source: vvaharness/backends/llm/cli/envelope.py:256-260
    if (the source predicate isinstance(envelope, dict) and 'result' in envelope is truthy) {
      // Source: vvaharness/backends/llm/cli/envelope.py:257-257
      In source order: Evaluate once envelope['result']; assign in source target order to content.
      // Source: vvaharness/backends/llm/cli/envelope.py:258-259
      if (the source predicate isinstance(content, str) is truthy) {
        // Source: vvaharness/backends/llm/cli/envelope.py:259-259
        End this invocation with json.loads(content).
      }
      // Source: vvaharness/backends/llm/cli/envelope.py:260-260
      End this invocation with content.
    }
    // Source: vvaharness/backends/llm/cli/envelope.py:261-261
    End this invocation with envelope.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:262-263
  On the first matching source exception (json.JSONDecodeError, TypeError), in handler order {
    // Source: vvaharness/backends/llm/cli/envelope.py:263-263
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/backends/llm/cli/envelope.py:265-265
  End this invocation with extract_json(text).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.llm import cache as _cache` at source line 21: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cache as _cache` at source line 21: `source_detail/vvaharness/backends/llm/cache.py.sudo.md`.
- `from vvaharness.backends.llm.models import ANTHROPIC_STOP_REFUSAL, CLI_CONTINUED_REPLIES_COUNTER, EnvelopeResult, GuardrailBlocked, model_refusal, refusal_category` at source line 22: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 30: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 31: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 32: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 33: `source_detail/vvaharness/util/json_extract.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS, TokenUsage` at source line 36: `source_detail/vvaharness/util/tokens.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/llm/cli/envelope.py.sudo.md). Exact strings in the evidence asset support this conversion.
