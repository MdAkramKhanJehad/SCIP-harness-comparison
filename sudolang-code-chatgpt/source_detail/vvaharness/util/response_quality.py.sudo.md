# vvaharness/util/response_quality.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/response_quality.py.evidence.json`. SHA-256: `ab4edda018432949828d295c3733f663c4b44cc54046b84fb120fd896425a4d0`.

```sudo
// Source: vvaharness/util/response_quality.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Iterator, Mapping, Sequence; preserve alias and import-time effects.
// Source: vvaharness/util/response_quality.py:21-44
In source order: Resolve source import from contextlib import contextmanager; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import AuthenticationError, DegenerateResponseError, HarnessCLINotFoundError, ProxyError, ToolStateNotRoundTrippedError, TruncatedResponseError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import REFUSAL_RETRY_ATTEMPTED_COUNTER, REFUSAL_RETRY_RECOVERED_COUNTER, GuardrailBlocked, ModelRefusal, finish_truncated, reply_finish; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact, redact_counts; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects.
// Source: vvaharness/util/response_quality.py:45-53
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.exceptions import exception_chain; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 150; assign in source target order to _DEFAULT_MIN_CHARS.
// Source: vvaharness/util/response_quality.py:54-62
In source order: Evaluate once 30; assign in source target order to _DEFAULT_MIN_TOKENS. Then Evaluate once 3; assign in source target order to _DEGENERATE_MAX_CONSECUTIVE. Then Evaluate once 300; assign in source target order to _RAW_HEAD_CHARS. Then Evaluate once threading.Lock(); assign in source target order to _lock. Then For _consecutive, assign {}; source annotation dict[str, int].
// Source: vvaharness/util/response_quality.py:64-64
In source order: For _stage_floors, assign {}; source annotation dict[str, tuple[int | None, int | None]].
// Source: vvaharness/util/response_quality.py:67-70
// Source signature: reset_counters() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reset_counters() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:68-68
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:69-70
  Enter source context managers left-to-right: _lock {
    // Source: vvaharness/util/response_quality.py:70-70
    In source order: Evaluate _consecutive.clear(); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:74-94
// Source: vvaharness/util/response_quality.py:73-73
Before creating this callable, evaluate and retain decorators top-to-bottom: contextmanager.
// Source: vvaharness/util/response_quality.py:74-94
// Source signature: stage_floors(stage: str, *, min_chars: int | None=None, min_tokens: int | None=None) -> Iterator[None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stage_floors(stage, min_chars, min_tokens) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:80-80
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:81-86
  Enter source context managers left-to-right: _lock {
    // Source: vvaharness/util/response_quality.py:82-86
    In source order: Evaluate once _stage_floors.get(stage); assign in source target order to prev. Then Evaluate once (int(min_chars) if min_chars is not None else None, int(min_tokens) if min_tokens is not None else None); assign in source target order to _stage_floors[stage].
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/util/response_quality.py:87-94
  Perform the following protected operations {
    // Source: vvaharness/util/response_quality.py:88-88
    In source order: Yield None; suspend this generator until resumed.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/util/response_quality.py:90-94
    Enter source context managers left-to-right: _lock {
      // Source: vvaharness/util/response_quality.py:91-94
      if (the source predicate prev is None is truthy) {
        // Source: vvaharness/util/response_quality.py:92-92
        In source order: Evaluate _stage_floors.pop(stage, None); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/util/response_quality.py:94-94
        In source order: Evaluate once prev; assign in source target order to _stage_floors[stage].
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/util/response_quality.py:99-111
// Source signature: output_tokens_for_gate(usage: Mapping[str, object] | None) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn output_tokens_for_gate(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:102-103
  if (the source predicate usage is None is truthy) {
    // Source: vvaharness/util/response_quality.py:103-103
    End this invocation with None.
  }
  // Source: vvaharness/util/response_quality.py:104-104
  In source order: Evaluate once usage.get('output_tokens'); assign in source target order to raw.
  // Source: vvaharness/util/response_quality.py:105-106
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/util/response_quality.py:106-106
    End this invocation with None.
  }
  // Source: vvaharness/util/response_quality.py:107-111
  Perform the following protected operations {
    // Source: vvaharness/util/response_quality.py:108-108
    End this invocation with int(raw).
  }
  // Source: vvaharness/util/response_quality.py:109-111
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/util/response_quality.py:111-111
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:114-186
// Source signature: check_response_quality(text: str, stage: str='', *, min_chars: int | None=None, output_tokens: int | None=None, expected_markers: Sequence[str] | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn check_response_quality(text, stage, min_chars, output_tokens, expected_markers) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:122-122
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:123-124
  Enter source context managers left-to-right: _lock {
    // Source: vvaharness/util/response_quality.py:124-124
    In source order: Evaluate once _stage_floors.get(stage, (None, None)); assign in source target order to (ov_chars, ov_tokens).
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/util/response_quality.py:125-126
  if (the source predicate min_chars is None is truthy) {
    // Source: vvaharness/util/response_quality.py:126-126
    In source order: Evaluate once ov_chars if ov_chars is not None else _DEFAULT_MIN_CHARS; assign in source target order to min_chars.
  }
  // Source: vvaharness/util/response_quality.py:127-129
  In source order: Evaluate once ov_tokens if ov_tokens is not None else _DEFAULT_MIN_TOKENS; assign in source target order to min_tokens. Then Evaluate once (text or '').strip(); assign in source target order to stripped. Then For reasons, assign []; source annotation list[str].
  // Source: vvaharness/util/response_quality.py:131-134
  if (the source predicate len(stripped) < min_chars is truthy) {
    // Source: vvaharness/util/response_quality.py:132-134
    In source order: Evaluate reasons.append(source_template_133_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/response_quality.py:136-140
  if (the source predicate output_tokens is not None and output_tokens < min_tokens is truthy) {
    // Source: vvaharness/util/response_quality.py:137-140
    In source order: Evaluate reasons.append(source_template_138_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/response_quality.py:142-145
  if (the source predicate expected_markers is truthy) {
    // Source: vvaharness/util/response_quality.py:143-143
    In source order: Evaluate once [m for m in expected_markers if m not in stripped]; assign in source target order to missing.
    // Source: vvaharness/util/response_quality.py:144-145
    if (the source predicate missing is truthy) {
      // Source: vvaharness/util/response_quality.py:145-145
      In source order: Evaluate reasons.append(source_template_145_27); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/util/response_quality.py:147-150
  if (the source predicate not reasons is truthy) {
    // Source: vvaharness/util/response_quality.py:148-149
    Enter source context managers left-to-right: _lock {
      // Source: vvaharness/util/response_quality.py:149-149
      In source order: Evaluate _consecutive.pop(stage, None); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/util/response_quality.py:150-150
    End this invocation with None.
  }
  // Source: vvaharness/util/response_quality.py:153-155
  Enter source context managers left-to-right: _lock {
    // Source: vvaharness/util/response_quality.py:154-155
    In source order: Evaluate once _consecutive.get(stage, 0) + 1; assign in source target order to count. Then Evaluate once count; assign in source target order to _consecutive[stage].
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/util/response_quality.py:157-157
  In source order: Evaluate once '; '.join(reasons); assign in source target order to summary.
  // Source: vvaharness/util/response_quality.py:159-172
  if (the source predicate count < _DEGENERATE_MAX_CONSECUTIVE is truthy) {
    // Source: vvaharness/util/response_quality.py:160-171
    In source order: Evaluate log.warning(Event.RESPONSE_DEGENERATE_ACCEPTED, error_code='VVAH-E003', stage=stage, consecutive=source_template_161_32, detail=summary); retain side effects and discard the expression result. Then Evaluate _errlog.log(stage or 'quality', stage or 'response_quality', source_template_165_12, error_code=DegenerateResponseError.error_code, raw_head=redact(stripped)[:_RAW_HEAD_CHARS], recovered=True); retain side effects and discard the expression result.
    // Source: vvaharness/util/response_quality.py:172-172
    End this invocation with None.
  }
  // Source: vvaharness/util/response_quality.py:175-176
  Enter source context managers left-to-right: _lock {
    // Source: vvaharness/util/response_quality.py:176-176
    In source order: Evaluate once 1; assign in source target order to _consecutive[stage].
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/util/response_quality.py:179-179
  In source order: Evaluate once len(stripped) < min_chars; assign in source target order to char_axis_failed.
  // Source: vvaharness/util/response_quality.py:180-186
  Raise DegenerateResponseError(summary, stage=stage, response_len=len(stripped), threshold=min_chars if char_axis_failed else 0, consecutive=count).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:191-199
interface StructuredOutputRejected {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/response_quality.py:192-192
  In source order: Retain source documentation literal source_literal_192_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:196-199
  // Source signature: __init__(self, message: str, *, finish: str | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, finish) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/response_quality.py:197-199
    In source order: Evaluate super().__init__(message); retain side effects and discard the expression result. Then Evaluate once finish; assign in source target order to self.finish.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/response_quality.py:203-207
In source order: Evaluate once ('StructuredOutputValidationError', 'OutputParserException', 'StructuredOutputRejected'); assign in source target order to _STRUCTURED_OUTPUT_FAILURE_NAMES.
// Source: vvaharness/util/response_quality.py:210-224
// Source signature: is_structured_output_failure(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_structured_output_failure(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:211-213
  In source order: Retain source documentation literal source_literal_211_4; it is not a model call. Then For seen, assign set(); source annotation set[int]. Then For cur, assign exc; source annotation BaseException | None.
  // Source: vvaharness/util/response_quality.py:214-223
  while (the source predicate cur is not None and id(cur) not in seen is truthy) {
    // Source: vvaharness/util/response_quality.py:215-215
    In source order: Evaluate seen.add(id(cur)); retain side effects and discard the expression result.
    // Source: vvaharness/util/response_quality.py:217-218
    if (the source predicate isinstance(cur, GuardrailBlocked) is truthy) {
      // Source: vvaharness/util/response_quality.py:218-218
      End this invocation with False.
    }
    // Source: vvaharness/util/response_quality.py:219-220
    if (the source predicate type(cur).__name__ in _STRUCTURED_OUTPUT_FAILURE_NAMES is truthy) {
      // Source: vvaharness/util/response_quality.py:220-220
      End this invocation with True.
    }
    // Source: vvaharness/util/response_quality.py:221-222
    if (the source predicate any((n in str(cur) for n in _STRUCTURED_OUTPUT_FAILURE_NAMES)) is truthy) {
      // Source: vvaharness/util/response_quality.py:222-222
      End this invocation with True.
    }
    // Source: vvaharness/util/response_quality.py:223-223
    In source order: Evaluate once cur.__cause__ or cur.__context__; assign in source target order to cur.
  }
  // Source: vvaharness/util/response_quality.py:224-224
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:227-229
// Source signature: is_truncated_without_retry(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_truncated_without_retry(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:228-228
  In source order: Retain source documentation literal source_literal_228_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:229-229
  End this invocation with isinstance(exc, TruncatedResponseError) and (not exc.retried).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:233-234
In source order: Evaluate once 300; assign in source target order to _FAILURE_DETAIL_CHARS. Then Evaluate once 40; assign in source target order to _FINISH_MARKER_CHARS.
// Source: vvaharness/util/response_quality.py:237-259
// Source signature: structured_failure_detail(exc: BaseException) -> tuple[str, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn structured_failure_detail(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:238-244
  In source order: Retain source documentation literal source_literal_238_4; it is not a model call. Then Evaluate once exception_chain(exc); assign in source target order to chain. Then Evaluate once next((c for c in chain if type(c).__name__ in _STRUCTURED_OUTPUT_FAILURE_NAMES), chain[-1]); assign in source target order to link. Then Evaluate once chain[-1]; assign in source target order to root. Then Evaluate once source_template_244_12; assign in source target order to cause.
  // Source: vvaharness/util/response_quality.py:245-246
  if (the source predicate root is not link and str(root) not in str(link) is truthy) {
    // Source: vvaharness/util/response_quality.py:246-246
    In source order: Apply source augmented assignment cause += source_template_246_17 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/util/response_quality.py:248-248
  In source order: Evaluate once redact_counts(cause)[0][:_FAILURE_DETAIL_CHARS]; assign in source target order to detail.
  // Source: vvaharness/util/response_quality.py:252-258
  for each c in chain {
    // Source: vvaharness/util/response_quality.py:253-255
    In source order: Evaluate once getattr(getattr(c, 'ai_message', None), 'response_metadata', None); assign in source target order to meta. Then Evaluate once getattr(c, 'finish', None) or (reply_finish(meta) if isinstance(meta, Mapping) else None); assign in source target order to finish.
    // Source: vvaharness/util/response_quality.py:256-258
    if (the source predicate finish is truthy) {
      // Source: vvaharness/util/response_quality.py:257-257
      In source order: Evaluate once redact_counts(str(finish))[0][:_FINISH_MARKER_CHARS]; assign in source target order to marker.
      // Source: vvaharness/util/response_quality.py:258-258
      End this invocation with (source_template_258_19, finish_truncated(finish)).
    }
  }
  // Source: vvaharness/util/response_quality.py:259-259
  End this invocation with (detail, False).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:262-290
// Source signature: _resending_refusal_once(dispatch: Callable[..., str], label: str, *, stage: str, allowed: Callable[[], bool] | None=None) -> Callable[..., str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resending_refusal_once(dispatch, label, stage, allowed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:264-265
  In source order: Retain source documentation literal source_literal_264_4; it is not a model call. Then Evaluate once 1; assign in source target order to left.
  // Source: vvaharness/util/response_quality.py:267-288
  // Source signature: send(*, drop_thinking: bool) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn send(drop_thinking) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/response_quality.py:268-268
    In source order: Bind names in enclosing nonlocal scope: left.
    // Source: vvaharness/util/response_quality.py:269-276
    Perform the following protected operations {
      // Source: vvaharness/util/response_quality.py:270-270
      End this invocation with dispatch(drop_thinking=drop_thinking).
    }
    // Source: vvaharness/util/response_quality.py:271-276
    On the first matching source exception ModelRefusal as exc, in handler order {
      // Source: vvaharness/util/response_quality.py:273-274
      if (the source predicate left <= 0 or (allowed is not None and (not allowed())) is truthy) {
        // Source: vvaharness/util/response_quality.py:274-274
        Raise the currently handled exception.
      }
      // Source: vvaharness/util/response_quality.py:275-276
      In source order: Apply source augmented assignment left -= 1 with source evaluation/in-place semantics. Then Evaluate once exc; assign in source target order to refused.
    }
    // Source: vvaharness/util/response_quality.py:277-287
    In source order: Evaluate COUNTERS.bump(REFUSAL_RETRY_ATTEMPTED_COUNTER); retain side effects and discard the expression result. Then Evaluate log.warning(Event.MODEL_REFUSAL_RESEND, stage=stage, label=label, route=refused.route or '-', category=refused.category or 'unspecified', detail=redact_counts(str(refused))[0][:_FAILURE_DETAIL_CHARS]); retain side effects and discard the expression result. Then Evaluate _errlog.log(stage, label, refused, reason='refusal_retry_attempted', route=refused.route, recovered=True); retain side effects and discard the expression result. Then Evaluate once dispatch(drop_thinking=drop_thinking); assign in source target order to raw. Then Evaluate COUNTERS.bump(REFUSAL_RETRY_RECOVERED_COUNTER); retain side effects and discard the expression result.
    // Source: vvaharness/util/response_quality.py:288-288
    End this invocation with raw.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/response_quality.py:290-290
  End this invocation with send.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:293-332
// Source signature: dispatch_or_retry_unforced(dispatch: Callable[..., str], label: str, *, stage: str, may_retry: Callable[[], bool] | None=None, effort: str | None=None, resend_refusal: bool=False, may_resend_refusal: Callable[[], bool] | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dispatch_or_retry_unforced(dispatch, label, stage, may_retry, effort, resend_refusal, may_resend_refusal) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:299-299
  In source order: Retain source documentation literal source_literal_299_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:307-309
  if (the source predicate resend_refusal is truthy) {
    // Source: vvaharness/util/response_quality.py:308-309
    In source order: Evaluate once _resending_refusal_once(dispatch, label, stage=stage, allowed=may_resend_refusal); assign in source target order to dispatch.
  }
  // Source: vvaharness/util/response_quality.py:310-319
  Perform the following protected operations {
    // Source: vvaharness/util/response_quality.py:311-311
    End this invocation with dispatch(drop_thinking=False).
  }
  // Source: vvaharness/util/response_quality.py:312-319
  On the first matching source exception Exception as exc, in handler order {
    // Source: vvaharness/util/response_quality.py:313-313
    In source order: Evaluate once effort is not None and is_truncated_without_retry(exc); assign in source target order to clipped.
    // Source: vvaharness/util/response_quality.py:314-315
    if (the source predicate not (clipped or is_structured_output_failure(exc)) is truthy) {
      // Source: vvaharness/util/response_quality.py:315-315
      Raise the currently handled exception.
    }
    // Source: vvaharness/util/response_quality.py:316-317
    if (the source predicate may_retry is not None and (not may_retry()) is truthy) {
      // Source: vvaharness/util/response_quality.py:317-317
      Raise the currently handled exception.
    }
    // Source: vvaharness/util/response_quality.py:319-319
    In source order: Evaluate once structured_failure_detail(exc); assign in source target order to (detail, cut_off).
  }
  // Source: vvaharness/util/response_quality.py:320-322
  In source order: Evaluate once 'truncated' if clipped else 'structured'; assign in source target order to kind. Then Evaluate once Event.REPLY_CLIPPED_RETRY if clipped else Event.STRUCTURED_REPLY_REJECTED_RETRY; assign in source target order to event. Then Evaluate COUNTERS.bump(source_template_322_18); retain side effects and discard the expression result.
  // Source: vvaharness/util/response_quality.py:323-326
  if (the source predicate cut_off is truthy) {
    // Source: vvaharness/util/response_quality.py:326-326
    In source order: Evaluate COUNTERS.bump('llm_structured_retry_truncated'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/response_quality.py:327-331
  In source order: Evaluate log.warning(event, stage=stage, label=label, detail=detail); retain side effects and discard the expression result. Then Evaluate once dispatch(drop_thinking=True); assign in source target order to raw. Then Evaluate COUNTERS.bump(source_template_331_18); retain side effects and discard the expression result.
  // Source: vvaharness/util/response_quality.py:332-332
  End this invocation with raw.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:338-346
In source order: Evaluate once frozenset({'TimeoutExpired', 'APITimeoutError', 'TimeoutException', 'ConnectTimeout', 'ReadTimeout', 'WriteTimeout', 'PoolTimeout'}); assign in source target order to _TIMEOUT_FAILURE_NAMES.
// Source: vvaharness/util/response_quality.py:349-362
// Source signature: is_timeout_failure(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_timeout_failure(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:350-353
  In source order: Retain source documentation literal source_literal_350_4; it is not a model call. Then For seen, assign set(); source annotation set[int]. Then For cur, assign exc; source annotation BaseException | None.
  // Source: vvaharness/util/response_quality.py:354-361
  while (the source predicate cur is not None and id(cur) not in seen is truthy) {
    // Source: vvaharness/util/response_quality.py:355-355
    In source order: Evaluate seen.add(id(cur)); retain side effects and discard the expression result.
    // Source: vvaharness/util/response_quality.py:357-358
    if (the source predicate isinstance(cur, GuardrailBlocked) is truthy) {
      // Source: vvaharness/util/response_quality.py:358-358
      End this invocation with False.
    }
    // Source: vvaharness/util/response_quality.py:359-360
    if (the source predicate isinstance(cur, TimeoutError) or type(cur).__name__ in _TIMEOUT_FAILURE_NAMES is truthy) {
      // Source: vvaharness/util/response_quality.py:360-360
      End this invocation with True.
    }
    // Source: vvaharness/util/response_quality.py:361-361
    In source order: Evaluate once cur.__cause__ or cur.__context__; assign in source target order to cur.
  }
  // Source: vvaharness/util/response_quality.py:362-362
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:365-369
In source order: Evaluate once frozenset({'APIConnectionError', 'ModelConnectionError', 'TransportError'}); assign in source target order to _CONNECTION_FAILURE_NAMES.
// Source: vvaharness/util/response_quality.py:372-386
// Source signature: is_connection_failure(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_connection_failure(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:373-373
  In source order: Retain source documentation literal source_literal_373_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:374-375
  if (the source predicate is_timeout_failure(exc) is truthy) {
    // Source: vvaharness/util/response_quality.py:375-375
    End this invocation with False.
  }
  // Source: vvaharness/util/response_quality.py:376-378
  In source order: For seen, assign set(); source annotation set[int]. Then For cur, assign exc; source annotation BaseException | None. Then Evaluate once False; assign in source target order to connection.
  // Source: vvaharness/util/response_quality.py:379-385
  while (the source predicate cur is not None and id(cur) not in seen is truthy) {
    // Source: vvaharness/util/response_quality.py:380-380
    In source order: Evaluate seen.add(id(cur)); retain side effects and discard the expression result.
    // Source: vvaharness/util/response_quality.py:381-382
    if (the source predicate isinstance(getattr(cur, 'status_code', None), int) is truthy) {
      // Source: vvaharness/util/response_quality.py:382-382
      End this invocation with False.
    }
    // Source: vvaharness/util/response_quality.py:383-384
    if (the source predicate {cls.__name__ for cls in type(cur).__mro__} & _CONNECTION_FAILURE_NAMES is truthy) {
      // Source: vvaharness/util/response_quality.py:384-384
      In source order: Evaluate once True; assign in source target order to connection.
    }
    // Source: vvaharness/util/response_quality.py:385-385
    In source order: Evaluate once cur.__cause__ or cur.__context__; assign in source target order to cur.
  }
  // Source: vvaharness/util/response_quality.py:386-386
  End this invocation with connection.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/response_quality.py:389-391
In source order: Evaluate once (AuthenticationError, ProxyError, ToolStateNotRoundTrippedError, HarnessCLINotFoundError); assign in source target order to _DETERMINISTIC_FAILURE_TYPES.
// Source: vvaharness/util/response_quality.py:394-396
// Source signature: is_deterministic_failure(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_deterministic_failure(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/response_quality.py:395-395
  In source order: Retain source documentation literal source_literal_395_4; it is not a model call.
  // Source: vvaharness/util/response_quality.py:396-396
  End this invocation with any((isinstance(err, _DETERMINISTIC_FAILURE_TYPES) for err in exception_chain(exc))).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.models import AuthenticationError, DegenerateResponseError, HarnessCLINotFoundError, ProxyError, ToolStateNotRoundTrippedError, TruncatedResponseError` at source line 23: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.models import REFUSAL_RETRY_ATTEMPTED_COUNTER, REFUSAL_RETRY_RECOVERED_COUNTER, GuardrailBlocked, ModelRefusal, finish_truncated, reply_finish` at source line 33: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.report.redact import redact, redact_counts` at source line 43: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 44: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 44: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 45: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.exceptions import exception_chain` at source line 46: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 47: `source_detail/vvaharness/util/events.py.sudo.md`.
