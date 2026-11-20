# vvaharness/backends/harness/deepagents/tool_choice_rejection.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/tool_choice_rejection.py.evidence.json`. SHA-256: `2b69dc4a29d61038fd6eb2187b9056e9f1beae687921e93fb381c91398d52cf4`.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.exceptions import exception_chain; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:27-38
In source order: Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once 400; assign in source target order to _HTTP_BAD_REQUEST. Then Evaluate once ('tool_choice', 'not supported for this model'); assign in source target order to _MARKERS. Then For KNOWN_UNSUPPORTED, assign frozenset({'claude-opus-5-5'}); source annotation frozenset[str]. Then For UNSUPPORTED_MODELS, assign set(KNOWN_UNSUPPORTED); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:40-40
In source order: For _WARNED, assign set(); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:43-51
// Source signature: is_tool_choice_unsupported_rejection(exc: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_tool_choice_unsupported_rejection(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:44-44
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:45-49
  for each link in exception_chain(exc) {
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:46-47
    In source order: Evaluate once getattr(link, 'status_code', None); assign in source target order to status. Then Evaluate once str(getattr(link, 'message', link)).lower(); assign in source target order to body.
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:48-49
    if (the source predicate status == _HTTP_BAD_REQUEST and all((m in body for m in _MARKERS)) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:49-49
      End this invocation with True.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:50-50
  In source order: Evaluate once str(getattr(exc, 'stderr', '') or '').lower(); assign in source target order to stderr.
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:51-51
  End this invocation with '400' in stderr and all((m in stderr for m in _MARKERS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:54-67
// Source signature: rejected_model(exc: BaseException) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn rejected_model(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:55-55
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:57-66
  for each link in exception_chain(exc) {
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:58-58
    In source order: Evaluate once getattr(getattr(link, 'request', None), 'content', None); assign in source target order to body.
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:59-60
    if (the source predicate not isinstance(body, (bytes, str)) or not body is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:60-60
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:61-64
    Perform the following protected operations {
      // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:62-62
      In source order: Evaluate once json.loads(body).get('model'); assign in source target order to model.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:63-64
    On the first matching source exception (ValueError, AttributeError), in handler order {
      // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:64-64
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:65-66
    if (the source predicate isinstance(model, str) and model is truthy) {
      // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:66-66
      End this invocation with model.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:67-67
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:70-80
// Source signature: learn_tool_choice_unsupported(*model_ids: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn learn_tool_choice_unsupported(model_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:71-71
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:72-80
  for each model_id in model_ids {
    // Source: vvaharness/backends/harness/deepagents/tool_choice_rejection.py:73-80
    In source order: Evaluate UNSUPPORTED_MODELS.add(model_id); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('deepagents_tool_choice_unsupported_fallback'); retain side effects and discard the expression result. Then Evaluate warn_once(_WARNED, model_id, source_template_78_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util.counters import COUNTERS` at source line 25: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.exceptions import exception_chain` at source line 26: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 27: `source_detail/vvaharness/util/warn_once.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/tool_choice_rejection.py.sudo.md). Exact strings in the evidence asset support this conversion.
