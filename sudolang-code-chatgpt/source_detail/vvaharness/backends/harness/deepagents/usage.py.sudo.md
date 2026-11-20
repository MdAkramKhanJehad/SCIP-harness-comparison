# vvaharness/backends/harness/deepagents/usage.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/deepagents/usage.py.evidence.json`. SHA-256: `448da5e8dbf5de97318d9f5d9175058d32edb1a4f60e226fe6354edb7a80f23c`.

```sudo
// Source: vvaharness/backends/harness/deepagents/usage.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/usage.py:25-28
In source order: Resolve source import from langchain_core.messages import AIMessage, BaseMessage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TokenUsage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/backends/harness/deepagents/usage.py:31-36
interface SessionUsage {
  Describe the source Python type, preserving its base/metaclass expression order: TokenUsage, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:32-36
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then For calls, declare without assigning a value; source annotation int. Then For turns, declare without assigning a value; source annotation int. Then For subagents, declare without assigning a value; source annotation dict[str, TokenUsage].
}
// Source: vvaharness/backends/harness/deepagents/usage.py:39-42
// Source signature: _as_int(value: object) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _as_int(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:40-41
  if (the source predicate isinstance(value, bool) or not isinstance(value, int) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/usage.py:41-41
    End this invocation with 0.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:42-42
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/usage.py:46-49
In source order: For _EPHEMERAL_CACHE_KEYS, assign ('ephemeral_5m_input_tokens', 'ephemeral_1h_input_tokens'); source annotation Final. Then For _EXCLUSIVE_USAGE_WARNED, assign set(); source annotation set[str].
// Source: vvaharness/backends/harness/deepagents/usage.py:52-59
// Source signature: _cache_counts(meta: Mapping[str, object]) -> tuple[int, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_counts(meta) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:53-54
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once meta.get('input_token_details'); assign in source target order to details.
  // Source: vvaharness/backends/harness/deepagents/usage.py:55-56
  if (the source predicate not isinstance(details, Mapping) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/usage.py:56-56
    End this invocation with (0, 0).
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:57-58
  In source order: Evaluate once sum((_as_int(details.get(key)) for key in _EPHEMERAL_CACHE_KEYS)); assign in source target order to ephemeral. Then Evaluate once ephemeral if ephemeral > 0 else _as_int(details.get('cache_creation')); assign in source target order to cache_creation.
  // Source: vvaharness/backends/harness/deepagents/usage.py:59-59
  End this invocation with (_as_int(details.get('cache_read')), cache_creation).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/usage.py:62-72
// Source signature: _raw_cache_creation(raw: Mapping[str, object] | None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _raw_cache_creation(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:63-63
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/usage.py:64-65
  if (the source predicate raw is None is truthy) {
    // Source: vvaharness/backends/harness/deepagents/usage.py:65-65
    End this invocation with 0.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:66-66
  In source order: Evaluate once _as_int(raw.get('cache_creation_input_tokens')); assign in source target order to creation.
  // Source: vvaharness/backends/harness/deepagents/usage.py:67-71
  if (the source predicate not creation is truthy) {
    // Source: vvaharness/backends/harness/deepagents/usage.py:69-69
    In source order: Evaluate once raw.get('cache_creation'); assign in source target order to nested.
    // Source: vvaharness/backends/harness/deepagents/usage.py:70-71
    if (the source predicate isinstance(nested, Mapping) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:71-71
      In source order: Evaluate once sum((_as_int(nested.get(key)) for key in _EPHEMERAL_CACHE_KEYS)); assign in source target order to creation.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:72-72
  End this invocation with creation.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/usage.py:76-121
// Source: vvaharness/backends/harness/deepagents/usage.py:75-75
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/backends/harness/deepagents/usage.py:76-121
interface _Counts {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:77-82
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call. Then For input_tokens, assign 0; source annotation int. Then For output_tokens, assign 0; source annotation int. Then For cache_read, assign 0; source annotation int. Then For cache_creation, assign 0; source annotation int.
  // Source: vvaharness/backends/harness/deepagents/usage.py:83-83
  In source order: For calls, assign 0; source annotation int.
  // Source: vvaharness/backends/harness/deepagents/usage.py:85-113
  // Source signature: add(self, meta: Mapping[str, object], raw_usage: Mapping[str, object] | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add(self, meta, raw_usage) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:89-89
    In source order: Evaluate once _cache_counts(meta); assign in source target order to (cache_read, cache_creation).
    // Source: vvaharness/backends/harness/deepagents/usage.py:90-92
    if (the source predicate cache_creation == 0 is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:92-92
      In source order: Evaluate once _raw_cache_creation(raw_usage); assign in source target order to cache_creation.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:93-94
    In source order: Evaluate once _as_int(meta.get('input_tokens')); assign in source target order to total_input. Then Evaluate once cache_read + cache_creation; assign in source target order to cached.
    // Source: vvaharness/backends/harness/deepagents/usage.py:95-108
    if (the source predicate total_input < cached is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:97-106
      In source order: Evaluate warn_once(_EXCLUSIVE_USAGE_WARNED, 'exclusive-usage-record', source_template_100_16); retain side effects and discard the expression result. Then Evaluate once total_input; assign in source target order to fresh.
    }
    else {
      // Source: vvaharness/backends/harness/deepagents/usage.py:108-108
      In source order: Evaluate once total_input - cached; assign in source target order to fresh.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:109-113
    In source order: Apply source augmented assignment self.input_tokens += fresh with source evaluation/in-place semantics. Then Apply source augmented assignment self.output_tokens += _as_int(meta.get('output_tokens')) with source evaluation/in-place semantics. Then Apply source augmented assignment self.cache_read += cache_read with source evaluation/in-place semantics. Then Apply source augmented assignment self.cache_creation += cache_creation with source evaluation/in-place semantics. Then Apply source augmented assignment self.calls += 1 with source evaluation/in-place semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:115-121
  // Source signature: as_usage(self) -> TokenUsage
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn as_usage(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:116-121
    End this invocation with TokenUsage(input_tokens=self.input_tokens, output_tokens=self.output_tokens, cache_read_input_tokens=self.cache_read, cache_creation_input_tokens=self.cache_creation).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/backends/harness/deepagents/usage.py:124-139
// Source signature: _unpack_event(event: tuple[object, ...] | Mapping[str, object]) -> tuple[tuple[str, ...], Mapping[str, object] | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unpack_event(event) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:127-127
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/usage.py:128-129
  if (the source predicate not isinstance(event, tuple) is truthy) {
    // Source: vvaharness/backends/harness/deepagents/usage.py:129-129
    End this invocation with ((), event).
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:130-133
  Perform the following protected operations {
    // Source: vvaharness/backends/harness/deepagents/usage.py:131-131
    In source order: Evaluate once event; assign in source target order to (raw_ns, payload).
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:132-133
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/backends/harness/deepagents/usage.py:133-133
    End this invocation with ((), None).
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:134-138
  In source order: Evaluate once tuple((str(part) for part in raw_ns)) if isinstance(raw_ns, (list, tuple)) else (); assign in source target order to namespace.
  // Source: vvaharness/backends/harness/deepagents/usage.py:139-139
  End this invocation with (namespace, payload if isinstance(payload, Mapping) else None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/usage.py:142-221
interface UsageAccumulator {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:143-143
  In source order: Retain source documentation literal source_literal_143_4; it is not a model call.
  // Source: vvaharness/backends/harness/deepagents/usage.py:145-150
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:146-150
    In source order: Retain source documentation literal source_literal_146_8; it is not a model call. Then For self._seen_ids, assign set(); source annotation set[str]. Then For self._total, assign _Counts(); source annotation _Counts. Then For self._subagents, assign {}; source annotation dict[str, _Counts]. Then For self._ns_to_agent, assign {}; source annotation dict[tuple[str, ...], str].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:152-160
  // Source signature: add_event(self, event: tuple[object, ...] | Mapping[str, object]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_event(self, event) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:155-156
    In source order: Retain source documentation literal source_literal_155_8; it is not a model call. Then Evaluate once _unpack_event(event); assign in source target order to (namespace, payload).
    // Source: vvaharness/backends/harness/deepagents/usage.py:157-158
    if (the source predicate payload is None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:158-158
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:159-160
    for each update in payload.values() {
      // Source: vvaharness/backends/harness/deepagents/usage.py:160-160
      In source order: Evaluate self._add_update(update, namespace); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:162-170
  // Source signature: _add_update(self, update: object, namespace: tuple[str, ...]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _add_update(self, update, namespace) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:163-164
    if (the source predicate not isinstance(update, Mapping) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:164-164
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:165-165
    In source order: Evaluate once update.get('messages'); assign in source target order to msgs.
    // Source: vvaharness/backends/harness/deepagents/usage.py:166-167
    if (the source predicate not isinstance(msgs, Sequence) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:167-167
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:168-170
    for each msg in msgs {
      // Source: vvaharness/backends/harness/deepagents/usage.py:169-170
      if (the source predicate isinstance(msg, BaseMessage) is truthy) {
        // Source: vvaharness/backends/harness/deepagents/usage.py:170-170
        In source order: Evaluate self.add_message(msg, namespace=namespace); retain side effects and discard the expression result.
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:172-178
  // Source signature: _is_duplicate(self, message_id: object) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _is_duplicate(self, message_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:173-174
    if (the source predicate not isinstance(message_id, str) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:174-174
      End this invocation with False.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:175-176
    if (the source predicate message_id in self._seen_ids is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:176-176
      End this invocation with True.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:177-177
    In source order: Evaluate self._seen_ids.add(message_id); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/usage.py:178-178
    End this invocation with False.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:180-197
  // Source signature: add_message(self, message: BaseMessage, namespace: tuple[str, ...]=()) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add_message(self, message, namespace) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:183-183
    In source order: Retain source documentation literal source_literal_183_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/usage.py:184-185
    if (the source predicate not isinstance(message, AIMessage) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:185-185
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:186-186
    In source order: Evaluate once message.name; assign in source target order to name.
    // Source: vvaharness/backends/harness/deepagents/usage.py:187-188
    if (the source predicate namespace and isinstance(name, str) and name is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:188-188
      In source order: Evaluate once name; assign in source target order to self._ns_to_agent[namespace].
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:189-189
    In source order: Evaluate once message.usage_metadata; assign in source target order to meta.
    // Source: vvaharness/backends/harness/deepagents/usage.py:190-191
    if (the source predicate meta is None or self._is_duplicate(message.id) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:191-191
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:192-194
    In source order: Evaluate once message.response_metadata.get('usage'); assign in source target order to raw. Then Evaluate once raw if isinstance(raw, Mapping) else None; assign in source target order to raw_usage. Then Evaluate self._total.add(meta, raw_usage); retain side effects and discard the expression result.
    // Source: vvaharness/backends/harness/deepagents/usage.py:195-197
    if (the source predicate namespace is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:196-197
      In source order: Evaluate once self._agent_label(namespace, name); assign in source target order to agent. Then Evaluate self._subagents.setdefault(agent, _Counts()).add(meta, raw_usage); retain side effects and discard the expression result.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:199-206
  // Source signature: _agent_label(self, namespace: tuple[str, ...], name: str | None) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _agent_label(self, namespace, name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:200-201
    if (the source predicate isinstance(name, str) and name is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:201-201
      End this invocation with name.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:202-202
    In source order: Evaluate once self._ns_to_agent.get(namespace); assign in source target order to learned.
    // Source: vvaharness/backends/harness/deepagents/usage.py:203-204
    if (the source predicate learned is not None is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:204-204
      End this invocation with learned.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:206-206
    End this invocation with namespace[0].split(':', 1)[0].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:208-221
  // Source signature: snapshot(self) -> SessionUsage | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn snapshot(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/backends/harness/deepagents/usage.py:209-209
    In source order: Retain source documentation literal source_literal_209_8; it is not a model call.
    // Source: vvaharness/backends/harness/deepagents/usage.py:211-212
    if (the source predicate self._total.calls == 0 is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:212-212
      End this invocation with None.
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:213-215
    In source order: Evaluate once SessionUsage(**self._total.as_usage()); assign in source target order to usage. Then Evaluate once self._total.calls; assign in source target order to usage['calls']. Then Evaluate once self._total.calls; assign in source target order to usage['turns'].
    // Source: vvaharness/backends/harness/deepagents/usage.py:216-220
    if (the source predicate self._subagents is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:217-220
      In source order: Evaluate once {agent: counts.as_usage() for agent, counts in sorted(self._subagents.items())}; assign in source target order to usage['subagents'].
    }
    // Source: vvaharness/backends/harness/deepagents/usage.py:221-221
    End this invocation with usage.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/backends/harness/deepagents/usage.py:224-230
// Source signature: aggregate_usage_metadata(messages: Sequence[object]) -> SessionUsage | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn aggregate_usage_metadata(messages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/deepagents/usage.py:225-226
  In source order: Retain source documentation literal source_literal_225_4; it is not a model call. Then Evaluate once UsageAccumulator(); assign in source target order to accumulator.
  // Source: vvaharness/backends/harness/deepagents/usage.py:227-229
  for each message in messages {
    // Source: vvaharness/backends/harness/deepagents/usage.py:228-229
    if (the source predicate isinstance(message, BaseMessage) is truthy) {
      // Source: vvaharness/backends/harness/deepagents/usage.py:229-229
      In source order: Evaluate accumulator.add_message(message); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/harness/deepagents/usage.py:230-230
  End this invocation with accumulator.snapshot().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/harness/deepagents/usage.py:233-233
In source order: Evaluate once ['SessionUsage', 'UsageAccumulator', 'aggregate_usage_metadata']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.util.tokens import TokenUsage` at source line 27: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 28: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
