# vvaharness/backends/harness/deepagents/options/tool_call_state.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/options/tool_call_state.py.evidence.json`. SHA-256: `3687b5059f32a680314a7f2f2155c263eb0b42ad70513ba1f01d7519a564cc02`.

```sudo
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects. Then Resolve source import from typing import Any, Final; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import AIMessage, BaseMessage; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:22-34
In source order: Resolve source import from langchain_core.outputs import ChatResult; preserve alias and import-time effects. Then Resolve source import from langchain_openai import ChatOpenAI; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once ['TOOL_CALL_STATE_KEY', 'TOOL_STATE_CAPTURED_COUNTER', 'ToolCallStateChatOpenAI']; assign in source target order to __all__. Then For TOOL_CALL_STATE_KEY, assign '__vvaharness_tool_call_state__'; source annotation Final.
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:35-38
In source order: For TOOL_STATE_CAPTURED_COUNTER, assign 'deepagents_tool_state_captured'; source annotation Final. Then For _WIRE_TOOL_CALL_KEYS, assign frozenset({'id', 'type', 'function', 'custom', 'index'}); source annotation Final.
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:41-47
// Source signature: _state_by_id(tool_calls: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _state_by_id(tool_calls) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:42-42
  In source order: For state, assign {}; source annotation dict[str, dict[str, Any]].
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:43-46
  for each call in tool_calls {
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:44-44
    In source order: Evaluate once {k: v for k, v in call.items() if k not in _WIRE_TOOL_CALL_KEYS and v is not None}; assign in source target order to fields.
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:45-46
    if (the source predicate call.get('id') and fields is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:46-46
      In source order: Evaluate once fields; assign in source target order to state[call['id']].
    }
  }
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:47-47
  End this invocation with state.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:50-53
// Source signature: _choice_tool_calls(choice: Any) -> list[dict[str, Any]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _choice_tool_calls(choice) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:51-52
  if (the source predicate isinstance(choice, dict) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:52-52
    End this invocation with (choice.get('message') or {}).get('tool_calls') or [].
  }
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:53-53
  End this invocation with [{'id': call.id, **(call.model_extra or {})} for call in choice.message.tool_calls or ()].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:56-59
// Source signature: _replay(state: dict[str, dict[str, Any]], sent: dict[str, Any]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replay(state, sent) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:57-59
  for each call in sent.get('tool_calls') or () {
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:58-59
    for each (key, value) in state.get(call.get('id'), {}).items() {
      // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:59-59
      In source order: Evaluate call.setdefault(key, value); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:62-68
// Source signature: _replay_all(messages: list[BaseMessage], wire: list[dict[str, Any]]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replay_all(messages, wire) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:63-64
  if (the source predicate len(messages) != len(wire) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:64-64
    End this invocation with None.
  }
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:65-68
  for each (message, sent) in zip(messages, wire, strict=True) {
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:66-66
    In source order: Evaluate once message.additional_kwargs.get(TOOL_CALL_STATE_KEY); assign in source target order to state.
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:67-68
    if (the source predicate state is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:68-68
      In source order: Evaluate _replay(state, sent); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:71-96
interface ToolCallStateChatOpenAI {
  Describe the source Python type, preserving its base/metaclass expression order: ChatOpenAI.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:72-72
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:75-87
  // Source signature: _create_chat_result(self, response: Any, generation_info: dict | None=None) -> ChatResult
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _create_chat_result(self, response, generation_info) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:78-81
    In source order: Evaluate once super()._create_chat_result(response, generation_info); assign in source target order to result. Then Evaluate once (response.get('choices') if isinstance(response, dict) else response.choices) or (); assign in source target order to choices.
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:82-86
    for each (generation, choice) in zip(result.generations, choices, strict=False) {
      // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:83-83
      In source order: Evaluate once _state_by_id(_choice_tool_calls(choice)); assign in source target order to state.
      // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:84-86
      if (the source predicate state and isinstance(generation.message, AIMessage) is truthy) {
        // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:85-86
        In source order: Evaluate once state; assign in source target order to generation.message.additional_kwargs[TOOL_CALL_STATE_KEY]. Then Evaluate COUNTERS.bump(TOOL_STATE_CAPTURED_COUNTER); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:87-87
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:89-96
  // Source signature: _get_request_payload(self, input_: Any, *, stop: list[str] | None=None, **kwargs: Any) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _get_request_payload(self, input_, stop, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:92-93
    In source order: Evaluate once super()._get_request_payload(input_, stop=stop, **kwargs); assign in source target order to payload. Then Evaluate once payload.get('messages'); assign in source target order to wire.
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:94-95
    if (the source predicate isinstance(wire, list) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:95-95
      In source order: Evaluate _replay_all(self._convert_input(input_).to_messages(), wire); retain side effects and discard the expression result.
    }
    // Source: vvaharness/backends/harness/deepagents/options/tool_call_state.py:96-96
    End this invocation with payload.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.util.counters import COUNTERS` at source line 25: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vvaharness/backends/harness/deepagents/options/tool_call_state.py.sudo.md). Exact strings in the evidence asset support this conversion.
