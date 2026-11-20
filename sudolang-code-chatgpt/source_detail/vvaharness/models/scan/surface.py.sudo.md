# vvaharness/models/scan/surface.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/surface.py.evidence.json`. SHA-256: `c69063db377f6eb5983d60b7bda9db8caaf668637b78956760b5217523fc7676`.

```sudo
// Source: vvaharness/models/scan/surface.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, field_validator; preserve alias and import-time effects.
// Source: vvaharness/models/scan/surface.py:23-43
In source order: Resolve source import from vvaharness.models.scan._coerce import _coerce_enum, _coerce_int; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log. Then Evaluate once {'network', 'ipc', 'file', 'cli', 'deserialization', 'framework', 'other'}; assign in source target order to _EP_KINDS. Then Evaluate once {'rpc': 'network', 'grpc': 'network', 'http': 'network', 'https': 'network', 'rest': 'network', 'api': 'network', 'graphql': 'network', 'websocket': 'network', 'ws': 'network', 'soap': 'network', 'tcp': 'network', 'udp': 'network', 'socket': 'network', 'webhook': 'network', 'endpoint': 'network', 'queue': 'ipc', 'message': 'ipc', 'mq': 'ipc', 'kafka': 'ipc', 'amqp': 'ipc', 'jms': 'ipc', 'pubsub': 'ipc', 'event': 'ipc', 'signal': 'ipc', 'pipe': 'ipc', 'bus': 'ipc', 'stdin': 'cli', 'argv': 'cli', 'command': 'cli', 'arg': 'cli', 'config': 'file', 'env': 'file', 'filesystem': 'file', 'fs': 'file', 'deserialize': 'deserialization', 'serde': 'deserialization', 'unmarshal': 'deserialization', 'parse': 'deserialization', 'pickle': 'deserialization', 'json': 'deserialization', 'spring': 'framework', 'django': 'framework', 'aspnet': 'framework'}; assign in source target order to _EP_KIND_ALIAS.
// Source: vvaharness/models/scan/surface.py:46-55
interface EntryPoint {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/surface.py:47-50
  In source order: For file, declare without assigning a value; source annotation str. Then For function, declare without assigning a value; source annotation str. Then For kind, declare without assigning a value; source annotation Literal['network', 'ipc', 'file', 'cli', 'deserialization', 'framework', 'other']. Then For reachable_from_unauth, assign False; source annotation bool.
  // Source: vvaharness/models/scan/surface.py:54-55
  // Source: vvaharness/models/scan/surface.py:52-53
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('kind', mode='before'), classmethod.
  // Source: vvaharness/models/scan/surface.py:54-55
  // Source signature: _v_kind(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_kind(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/surface.py:55-55
    End this invocation with _coerce_enum(v, _EP_KINDS, _EP_KIND_ALIAS, 'other').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/scan/surface.py:58-70
interface Sink {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/surface.py:59-63
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call. Then For file, declare without assigning a value; source annotation str. Then For line, assign 0; source annotation int. Then For function, declare without assigning a value; source annotation str. Then For snippet, assign ''; source annotation str.
  // Source: vvaharness/models/scan/surface.py:65-65
  In source order: For cwe, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/surface.py:69-70
  // Source: vvaharness/models/scan/surface.py:67-68
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('line', mode='before'), classmethod.
  // Source: vvaharness/models/scan/surface.py:69-70
  // Source signature: _v_line(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_line(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/surface.py:70-70
    End this invocation with _coerce_int(v, 0).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/scan/surface.py:73-82
interface ModuleInfo {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/surface.py:74-77
  In source order: For name, declare without assigning a value; source annotation str. Then For files, assign []; source annotation list[str]. Then For loc, assign 0; source annotation int. Then For purpose, assign ''; source annotation str.
  // Source: vvaharness/models/scan/surface.py:81-82
  // Source: vvaharness/models/scan/surface.py:79-80
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('loc', mode='before'), classmethod.
  // Source: vvaharness/models/scan/surface.py:81-82
  // Source signature: _v_loc(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_loc(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/surface.py:82-82
    End this invocation with _coerce_int(v, 0).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
```

## Local import links

- `from vvaharness.models.scan._coerce import _coerce_enum, _coerce_int` at source line 23: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
