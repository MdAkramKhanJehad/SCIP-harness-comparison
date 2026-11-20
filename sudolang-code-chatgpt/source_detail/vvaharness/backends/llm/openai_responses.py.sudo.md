# vvaharness/backends/llm/openai_responses.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/openai_responses.py.evidence.json`. SHA-256: `fa4f6bae81e07ffb436b73a6ebe8423ad0c51bd44a85dc56e4bf7cd275dbd8ad`.

```sudo
// Source: vvaharness/backends/llm/openai_responses.py:15-41
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Any, Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import REASONING_OFF; preserve alias and import-time effects. Then Evaluate once ['INCLUDE_ENCRYPTED_REASONING', 'ITEM_ID_KEY', 'REASONING_ITEMS_KEY', 'finish_of', 'from_response', 'to_chat_messages', 'to_responses_input', 'to_responses_request', 'to_responses_tool_choice', 'to_responses_tools', 'usage_as_chat']; assign in source target order to __all__.
// Source: vvaharness/backends/llm/openai_responses.py:46-59
In source order: Evaluate once '_reasoning_items'; assign in source target order to REASONING_ITEMS_KEY. Then Evaluate once '_item_id'; assign in source target order to ITEM_ID_KEY. Then For INCLUDE_ENCRYPTED_REASONING, assign ('reasoning.encrypted_content',); source annotation Final[tuple[str, ...]]. Then For _REASONING_INPUT_FIELDS, assign ('type', 'id', 'encrypted_content', 'summary'); source annotation Final[tuple[str, ...]].
// Source: vvaharness/backends/llm/openai_responses.py:62-68
// Source signature: _get(obj: Any, key: str, default: Any=None) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _get(obj, key, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:63-63
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai_responses.py:64-65
  if (the source predicate obj is None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:65-65
    End this invocation with default.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:66-67
  if (the source predicate isinstance(obj, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:67-67
    End this invocation with obj.get(key, default).
  }
  // Source: vvaharness/backends/llm/openai_responses.py:68-68
  End this invocation with getattr(obj, key, default).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:71-77
// Source signature: _as_dict(obj: Any) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _as_dict(obj) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:72-72
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai_responses.py:73-74
  if (the source predicate obj is None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:74-74
    End this invocation with {}.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:75-76
  if (the source predicate isinstance(obj, dict) is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:76-76
    End this invocation with dict(obj).
  }
  // Source: vvaharness/backends/llm/openai_responses.py:77-77
  End this invocation with obj.model_dump() if hasattr(obj, 'model_dump') else dict(vars(obj)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:80-95
// Source signature: to_responses_tools(tools: list[dict] | None) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_responses_tools(tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai_responses.py:82-83
  if (the source predicate not tools is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:83-83
    End this invocation with [].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:84-84
  In source order: Evaluate once []; assign in source target order to flattened.
  // Source: vvaharness/backends/llm/openai_responses.py:85-94
  for each tool in tools {
    // Source: vvaharness/backends/llm/openai_responses.py:86-94
    In source order: Evaluate once tool['function']; assign in source target order to fn. Then Evaluate flattened.append({'type': 'function', 'name': fn['name'], 'description': fn.get('description'), 'parameters': fn.get('parameters'), 'strict': False}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:95-95
  End this invocation with flattened.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:98-103
// Source signature: _is_forced_function_choice(tool_choice: Any) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_forced_function_choice(tool_choice) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:99-103
  End this invocation with isinstance(tool_choice, dict) and tool_choice.get('type') == 'function' and ('function' in tool_choice).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:106-110
// Source signature: to_responses_tool_choice(tool_choice: Any) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_responses_tool_choice(tool_choice) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:107-107
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai_responses.py:108-109
  if (the source predicate _is_forced_function_choice(tool_choice) is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:109-109
    End this invocation with {'type': 'function', 'name': tool_choice['function']['name']}.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:110-110
  End this invocation with tool_choice.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:113-121
// Source signature: _input_content(content: Any) -> Any
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _input_content(content) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:114-120
  if (the source predicate isinstance(content, list) is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:115-120
    End this invocation with [{'type': 'input_text', 'text': block.get('text', '')} if isinstance(block, dict) and block.get('type') == 'text' else block for block in content].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:121-121
  End this invocation with content.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:124-130
// Source signature: _reasoning_input_items(entry: dict) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reasoning_input_items(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:127-130
  End this invocation with [dict(item) for item in entry.get(REASONING_ITEMS_KEY) or [] if item.get('encrypted_content')].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:133-141
// Source signature: _text_input_item(entry: dict) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _text_input_item(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:134-134
  In source order: Evaluate once entry.get('content'); assign in source target order to content.
  // Source: vvaharness/backends/llm/openai_responses.py:135-136
  if (the source predicate not content is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:136-136
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:137-141
  End this invocation with {'type': 'message', 'role': 'assistant', 'content': [{'type': 'output_text', 'text': content, 'annotations': []}]}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:144-161
// Source signature: _function_call_items(entry: dict) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _function_call_items(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:148-148
  In source order: Evaluate once []; assign in source target order to items.
  // Source: vvaharness/backends/llm/openai_responses.py:149-160
  for each tool_call in entry.get('tool_calls') or [] {
    // Source: vvaharness/backends/llm/openai_responses.py:150-157
    In source order: Evaluate once tool_call.get('function') or {}; assign in source target order to fn. Then Evaluate once {'type': 'function_call', 'call_id': tool_call.get('id'), 'name': fn.get('name'), 'arguments': fn.get('arguments')}; assign in source target order to call_item. Then Evaluate once tool_call.get(ITEM_ID_KEY); assign in source target order to item_id.
    // Source: vvaharness/backends/llm/openai_responses.py:158-159
    if (the source predicate item_id is not None is truthy) {
      // Source: vvaharness/backends/llm/openai_responses.py:159-159
      In source order: Evaluate once item_id; assign in source target order to call_item['id'].
    }
    // Source: vvaharness/backends/llm/openai_responses.py:160-160
    In source order: Evaluate items.append(call_item); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:161-161
  End this invocation with items.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:164-170
// Source signature: _assistant_items(entry: dict) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _assistant_items(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:165-166
  In source order: Evaluate once _reasoning_input_items(entry); assign in source target order to items. Then Evaluate once _text_input_item(entry); assign in source target order to text_item.
  // Source: vvaharness/backends/llm/openai_responses.py:167-168
  if (the source predicate text_item is not None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:168-168
    In source order: Evaluate items.append(text_item); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:169-169
  In source order: Evaluate items.extend(_function_call_items(entry)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai_responses.py:170-170
  End this invocation with items.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:173-188
// Source signature: to_responses_input(messages: list[dict]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_responses_input(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:174-175
  In source order: Retain source documentation literal source_literal_174_4; it is not a model call. Then For items, assign []; source annotation list[dict].
  // Source: vvaharness/backends/llm/openai_responses.py:176-187
  for each entry in messages {
    // Source: vvaharness/backends/llm/openai_responses.py:177-177
    In source order: Evaluate once entry.get('role'); assign in source target order to role.
    // Source: vvaharness/backends/llm/openai_responses.py:178-187
    if (the source predicate role == 'assistant' is truthy) {
      // Source: vvaharness/backends/llm/openai_responses.py:179-179
      In source order: Evaluate items.extend(_assistant_items(entry)); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/llm/openai_responses.py:180-187
      if (the source predicate role == 'tool' is truthy) {
        // Source: vvaharness/backends/llm/openai_responses.py:181-185
        In source order: Evaluate items.append({'type': 'function_call_output', 'call_id': entry.get('tool_call_id'), 'output': entry.get('content')}); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/backends/llm/openai_responses.py:187-187
        In source order: Evaluate items.append({'role': role, 'content': _input_content(entry.get('content'))}); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/backends/llm/openai_responses.py:188-188
  End this invocation with items.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:191-199
// Source signature: _tool_kwargs(base_kw: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_kwargs(base_kw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:192-193
  In source order: For kwargs, assign {}; source annotation dict. Then Evaluate once to_responses_tools(base_kw.get('tools')); assign in source target order to tools.
  // Source: vvaharness/backends/llm/openai_responses.py:194-195
  if (the source predicate tools is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:195-195
    In source order: Evaluate once tools; assign in source target order to kwargs['tools'].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:196-196
  In source order: Evaluate once base_kw.get('tool_choice'); assign in source target order to tool_choice.
  // Source: vvaharness/backends/llm/openai_responses.py:197-198
  if (the source predicate tool_choice is not None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:198-198
    In source order: Evaluate once to_responses_tool_choice(tool_choice); assign in source target order to kwargs['tool_choice'].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:199-199
  End this invocation with kwargs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:202-218
// Source signature: _responses_only_kwargs(base_kw: dict, *, include_encrypted: bool) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _responses_only_kwargs(base_kw, include_encrypted) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:204-205
  In source order: For kwargs, assign {'store': False}; source annotation dict. Then Evaluate once base_kw.get('max_completion_tokens', base_kw.get('max_tokens')); assign in source target order to max_tokens.
  // Source: vvaharness/backends/llm/openai_responses.py:206-207
  if (the source predicate max_tokens is not None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:207-207
    In source order: Evaluate once max_tokens; assign in source target order to kwargs['max_output_tokens'].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:208-208
  In source order: Evaluate once base_kw.get('reasoning_effort'); assign in source target order to effort.
  // Source: vvaharness/backends/llm/openai_responses.py:211-212
  if (the source predicate effort is not None and effort != REASONING_OFF is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:212-212
    In source order: Evaluate once {'effort': effort}; assign in source target order to kwargs['reasoning'].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:213-213
  In source order: Evaluate once base_kw.get('prompt_cache_key'); assign in source target order to cache_key.
  // Source: vvaharness/backends/llm/openai_responses.py:214-215
  if (the source predicate cache_key is not None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:215-215
    In source order: Evaluate once cache_key; assign in source target order to kwargs['prompt_cache_key'].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:216-217
  if (the source predicate include_encrypted is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:217-217
    In source order: Evaluate once list(INCLUDE_ENCRYPTED_REASONING); assign in source target order to kwargs['include'].
  }
  // Source: vvaharness/backends/llm/openai_responses.py:218-218
  End this invocation with kwargs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:221-233
// Source signature: to_responses_request(messages: list[dict], base_kw: dict, *, include_encrypted: bool) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_responses_request(messages, base_kw, include_encrypted) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:224-232
  In source order: Retain source documentation literal source_literal_224_4; it is not a model call. Then For request, assign {'model': base_kw['model'], 'input': to_responses_input(messages)}; source annotation dict. Then Evaluate request.update(_tool_kwargs(base_kw)); retain side effects and discard the expression result. Then Evaluate request.update(_responses_only_kwargs(base_kw, include_encrypted=include_encrypted)); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai_responses.py:233-233
  End this invocation with request.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:236-247
// Source signature: to_chat_messages(messages: list[dict]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn to_chat_messages(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:237-238
  In source order: Retain source documentation literal source_literal_237_4; it is not a model call. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/backends/llm/openai_responses.py:239-246
  for each entry in messages {
    // Source: vvaharness/backends/llm/openai_responses.py:240-241
    In source order: Evaluate once {k: v for k, v in entry.items() if k != REASONING_ITEMS_KEY}; assign in source target order to copy. Then Evaluate once copy.get('tool_calls'); assign in source target order to tool_calls.
    // Source: vvaharness/backends/llm/openai_responses.py:242-245
    if (the source predicate tool_calls is truthy) {
      // Source: vvaharness/backends/llm/openai_responses.py:243-245
      In source order: Evaluate once [{k: v for k, v in tc.items() if k != ITEM_ID_KEY} for tc in tool_calls]; assign in source target order to copy['tool_calls'].
    }
    // Source: vvaharness/backends/llm/openai_responses.py:246-246
    In source order: Evaluate out.append(copy); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:247-247
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:250-273
// Source signature: usage_as_chat(usage: Any) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn usage_as_chat(usage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:251-251
  In source order: Retain source documentation literal source_literal_251_4; it is not a model call.
  // Source: vvaharness/backends/llm/openai_responses.py:252-253
  if (the source predicate usage is None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:253-253
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:254-256
  In source order: Evaluate once _get(usage, 'input_tokens') or 0; assign in source target order to input_tokens. Then Evaluate once _get(usage, 'output_tokens') or 0; assign in source target order to output_tokens. Then Evaluate once _get(usage, 'total_tokens'); assign in source target order to total_tokens.
  // Source: vvaharness/backends/llm/openai_responses.py:257-258
  if (the source predicate total_tokens is None is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:258-258
    In source order: Evaluate once input_tokens + output_tokens; assign in source target order to total_tokens.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:260-265
  In source order: Evaluate once _as_dict(_get(usage, 'input_tokens_details')); assign in source target order to prompt_details. Then Evaluate prompt_details.setdefault('cached_tokens', 0); retain side effects and discard the expression result. Then Evaluate prompt_details.setdefault('cache_write_tokens', 0); retain side effects and discard the expression result. Then Evaluate once _as_dict(_get(usage, 'output_tokens_details')); assign in source target order to completion_details. Then Evaluate completion_details.setdefault('reasoning_tokens', 0); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/openai_responses.py:267-273
  End this invocation with {'prompt_tokens': input_tokens, 'completion_tokens': output_tokens, 'total_tokens': total_tokens, 'prompt_tokens_details': prompt_details, 'completion_tokens_details': completion_details}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:276-285
// Source signature: finish_of(resp: Any, has_tool_calls: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn finish_of(resp, has_tool_calls) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:277-280
  In source order: Retain source documentation literal source_literal_277_4; it is not a model call. Then Evaluate once _get(resp, 'status'); assign in source target order to status. Then Evaluate once _get(resp, 'incomplete_details'); assign in source target order to incomplete. Then Evaluate once _get(incomplete, 'reason') if incomplete is not None else None; assign in source target order to reason.
  // Source: vvaharness/backends/llm/openai_responses.py:281-282
  if (the source predicate status == 'incomplete' and reason == 'max_output_tokens' is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:282-282
    End this invocation with 'length'.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:283-284
  if (the source predicate reason == 'content_filter' is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:284-284
    End this invocation with 'content_filter'.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:285-285
  End this invocation with 'tool_calls' if has_tool_calls else 'stop'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:288-293
interface _Function {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/openai_responses.py:289-289
  In source order: Evaluate once ('arguments', 'name'); assign in source target order to __slots__.
  // Source: vvaharness/backends/llm/openai_responses.py:291-293
  // Source signature: __init__(self, name: str | None, arguments: str | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, name, arguments) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/openai_responses.py:292-293
    In source order: Evaluate once name; assign in source target order to self.name. Then Evaluate once arguments; assign in source target order to self.arguments.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/openai_responses.py:296-314
interface _ToolCall {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/openai_responses.py:297-297
  In source order: Evaluate once ('_item_id', 'function', 'id', 'type'); assign in source target order to __slots__.
  // Source: vvaharness/backends/llm/openai_responses.py:299-304
  // Source signature: __init__(self, call_id: str | None, name: str | None, arguments: str | None, item_id: str | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, call_id, name, arguments, item_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/openai_responses.py:301-304
    In source order: Evaluate once call_id; assign in source target order to self.id. Then Evaluate once 'function'; assign in source target order to self.type. Then Evaluate once _Function(name, arguments); assign in source target order to self.function. Then Evaluate once item_id; assign in source target order to self._item_id.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:306-314
  // Source signature: model_dump(self) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn model_dump(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/openai_responses.py:307-311
    In source order: Evaluate once {'id': self.id, 'type': 'function', 'function': {'name': self.function.name, 'arguments': self.function.arguments}}; assign in source target order to dumped.
    // Source: vvaharness/backends/llm/openai_responses.py:312-313
    if (the source predicate self._item_id is not None is truthy) {
      // Source: vvaharness/backends/llm/openai_responses.py:313-313
      In source order: Evaluate once self._item_id; assign in source target order to dumped[ITEM_ID_KEY].
    }
    // Source: vvaharness/backends/llm/openai_responses.py:314-314
    End this invocation with dumped.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/openai_responses.py:317-325
interface _Message {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/openai_responses.py:318-318
  In source order: Evaluate once ('content', 'reasoning_items', 'refusal', 'tool_calls'); assign in source target order to __slots__.
  // Source: vvaharness/backends/llm/openai_responses.py:320-325
  // Source signature: __init__(self, content: str | None, tool_calls: list[_ToolCall], refusal: str | None, reasoning_items: list[dict]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, content, tool_calls, refusal, reasoning_items) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/openai_responses.py:322-325
    In source order: Evaluate once content; assign in source target order to self.content. Then Evaluate once tool_calls; assign in source target order to self.tool_calls. Then Evaluate once refusal; assign in source target order to self.refusal. Then Evaluate once reasoning_items; assign in source target order to self.reasoning_items.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/openai_responses.py:328-333
interface _Choice {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/openai_responses.py:329-329
  In source order: Evaluate once ('finish_reason', 'message'); assign in source target order to __slots__.
  // Source: vvaharness/backends/llm/openai_responses.py:331-333
  // Source signature: __init__(self, message: _Message, finish_reason: str) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, message, finish_reason) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/openai_responses.py:332-333
    In source order: Evaluate once message; assign in source target order to self.message. Then Evaluate once finish_reason; assign in source target order to self.finish_reason.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/openai_responses.py:336-341
interface _ResponsesReply {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/llm/openai_responses.py:337-337
  In source order: Evaluate once ('choices', 'usage'); assign in source target order to __slots__.
  // Source: vvaharness/backends/llm/openai_responses.py:339-341
  // Source signature: __init__(self, choices: list[_Choice], usage: dict | None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, choices, usage) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/llm/openai_responses.py:340-341
    In source order: Evaluate once choices; assign in source target order to self.choices. Then Evaluate once usage; assign in source target order to self.usage.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/llm/openai_responses.py:344-355
// Source signature: _raise_for_error(resp: Any) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raise_for_error(resp) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:345-346
  In source order: Evaluate once _get(resp, 'error'); assign in source target order to error. Then Evaluate once _get(resp, 'status'); assign in source target order to status.
  // Source: vvaharness/backends/llm/openai_responses.py:347-348
  if (the source predicate not error and status != 'failed' is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:348-348
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:349-354
  if (the source predicate error is truthy) {
    // Source: vvaharness/backends/llm/openai_responses.py:350-350
    In source order: Evaluate once error if isinstance(error, str) else _get(error, 'message') or str(error); assign in source target order to message.
  }
  else {
    // Source: vvaharness/backends/llm/openai_responses.py:354-354
    In source order: Evaluate once source_template_354_18; assign in source target order to message.
  }
  // Source: vvaharness/backends/llm/openai_responses.py:355-355
  Raise RuntimeError(message).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:358-367
// Source signature: _message_content(item: Any) -> tuple[list[str], str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _message_content(item) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:359-360
  In source order: For text_parts, assign []; source annotation list[str]. Then For refusal, assign None; source annotation str | None.
  // Source: vvaharness/backends/llm/openai_responses.py:361-366
  for each block in _get(item, 'content') or [] {
    // Source: vvaharness/backends/llm/openai_responses.py:362-362
    In source order: Evaluate once _get(block, 'type'); assign in source target order to block_type.
    // Source: vvaharness/backends/llm/openai_responses.py:363-366
    if (the source predicate block_type == 'output_text' is truthy) {
      // Source: vvaharness/backends/llm/openai_responses.py:364-364
      In source order: Evaluate text_parts.append(_get(block, 'text') or ''); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/llm/openai_responses.py:365-366
      if (the source predicate block_type == 'refusal' and refusal is None is truthy) {
        // Source: vvaharness/backends/llm/openai_responses.py:366-366
        In source order: Evaluate once _get(block, 'refusal'); assign in source target order to refusal.
      }
    }
  }
  // Source: vvaharness/backends/llm/openai_responses.py:367-367
  End this invocation with (text_parts, refusal).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:370-375
// Source signature: _tool_call_from_item(item: Any) -> _ToolCall
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tool_call_from_item(item) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:373-375
  End this invocation with _ToolCall(_get(item, 'call_id'), _get(item, 'name'), _get(item, 'arguments'), _get(item, 'id')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:378-384
// Source signature: _encrypted_reasoning_items(items: list) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _encrypted_reasoning_items(items) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:379-384
  End this invocation with [{field: _get(item, field) for field in _REASONING_INPUT_FIELDS if _get(item, field) is not None} for item in items if _get(item, 'type') == 'reasoning' and _get(item, 'encrypted_content')].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/openai_responses.py:387-408
// Source signature: from_response(resp: Any) -> _ResponsesReply
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn from_response(resp) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/openai_responses.py:388-393
  In source order: Retain source documentation literal source_literal_388_4; it is not a model call. Then Evaluate _raise_for_error(resp); retain side effects and discard the expression result. Then Evaluate once _get(resp, 'output') or []; assign in source target order to output_items. Then For output_text_parts, assign []; source annotation list[str]. Then For refusal_text, assign None; source annotation str | None.
  // Source: vvaharness/backends/llm/openai_responses.py:394-394
  In source order: For tool_calls, assign []; source annotation list[_ToolCall].
  // Source: vvaharness/backends/llm/openai_responses.py:395-403
  for each item in output_items {
    // Source: vvaharness/backends/llm/openai_responses.py:396-396
    In source order: Evaluate once _get(item, 'type'); assign in source target order to item_type.
    // Source: vvaharness/backends/llm/openai_responses.py:397-403
    if (the source predicate item_type == 'message' is truthy) {
      // Source: vvaharness/backends/llm/openai_responses.py:398-399
      In source order: Evaluate once _message_content(item); assign in source target order to (text_parts, refusal). Then Evaluate output_text_parts.extend(text_parts); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/openai_responses.py:400-401
      if (the source predicate refusal_text is None is truthy) {
        // Source: vvaharness/backends/llm/openai_responses.py:401-401
        In source order: Evaluate once refusal; assign in source target order to refusal_text.
      }
    }
    else {
      // Source: vvaharness/backends/llm/openai_responses.py:402-403
      if (the source predicate item_type == 'function_call' is truthy) {
        // Source: vvaharness/backends/llm/openai_responses.py:403-403
        In source order: Evaluate tool_calls.append(_tool_call_from_item(item)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/backends/llm/openai_responses.py:405-407
  In source order: Evaluate once ''.join(output_text_parts) if output_text_parts else None; assign in source target order to content. Then Evaluate once _Message(content, tool_calls, refusal_text, _encrypted_reasoning_items(output_items)); assign in source target order to message. Then Evaluate once _Choice(message, finish_of(resp, has_tool_calls=bool(tool_calls))); assign in source target order to choice.
  // Source: vvaharness/backends/llm/openai_responses.py:408-408
  End this invocation with _ResponsesReply([choice], usage_as_chat(_get(resp, 'usage'))).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.backends.llm.models import REASONING_OFF` at source line 27: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/backends/llm/openai_responses.py.sudo.md). Exact strings in the evidence asset support this conversion.
