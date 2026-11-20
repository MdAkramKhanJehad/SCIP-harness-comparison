# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py.evidence.json`. SHA-256: `dc535efd798f57da42eb177c26e8107bee898b2cb030c6c22bddc6e56b24e4bc`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import tomllib; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:24-29
// Source signature: parse_json_object(text: str) -> dict[str, object] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_json_object(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:25-28
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:26-26
    In source order: Evaluate once cast(object, json.loads(text)); assign in source target order to parsed.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:27-28
  On the first matching source exception ValueError, in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:28-28
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:29-29
  End this invocation with as_mapping(parsed).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:32-36
// Source signature: parse_toml(text: str) -> dict[str, object] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_toml(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:33-36
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:34-34
    End this invocation with cast(dict[str, object], tomllib.loads(text)).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:35-36
  On the first matching source exception (tomllib.TOMLDecodeError, ValueError), in handler order {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:36-36
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:39-42
// Source signature: as_mapping(value: object) -> dict[str, object] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn as_mapping(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:40-41
  if (the source predicate isinstance(value, dict) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:41-41
    End this invocation with cast(dict[str, object], value).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:42-42
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:45-48
// Source signature: as_list(value: object) -> list[object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn as_list(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:46-47
  if (the source predicate isinstance(value, list) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:47-47
    End this invocation with cast(list[object], value).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:48-48
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:51-52
// Source signature: as_str(value: object, default: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn as_str(value, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:52-52
  End this invocation with value if isinstance(value, str) else default.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:55-59
// Source signature: mapping_at(value: object, *keys: str) -> dict[str, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn mapping_at(value, keys) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:56-56
  In source order: Evaluate once as_mapping(value) or {}; assign in source target order to current.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:57-58
  for each key in keys {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:58-58
    In source order: Evaluate once as_mapping(current.get(key)) or {}; assign in source target order to current.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:59-59
  End this invocation with current.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:62-63
// Source signature: string_list(value: object) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn string_list(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:63-63
  End this invocation with tuple((item for item in as_list(value) if isinstance(item, str) and item)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:66-68
// Source signature: string_items(value: object) -> tuple[tuple[str, str], ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn string_items(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:67-67
  In source order: Evaluate once as_mapping(value) or {}; assign in source target order to mapping.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/_data.py:68-68
  End this invocation with tuple(((key, item) for key, item in mapping.items() if isinstance(item, str))).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
