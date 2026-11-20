# vvaharness/models/scan/_coerce.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/_coerce.py.evidence.json`. SHA-256: `4b1fc9e0504439322732abefd983aef09433cb64c0c030ba20b3a97083c7f05e`.

```sudo
// Source: vvaharness/models/scan/_coerce.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/_coerce.py:22-23
// Source signature: _norm(v) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _norm(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_coerce.py:23-23
  End this invocation with str(v or '').strip().lower().replace('-', '_').replace(' ', '_').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_coerce.py:26-33
// Source signature: _coerce_enum(v, valid: set[str], alias: dict[str, str], default: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coerce_enum(v, valid, alias, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_coerce.py:27-27
  In source order: Evaluate once str(v or '').strip(); assign in source target order to raw.
  // Source: vvaharness/models/scan/_coerce.py:28-29
  if (the source predicate raw in valid is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:29-29
    End this invocation with raw.
  }
  // Source: vvaharness/models/scan/_coerce.py:30-30
  In source order: Evaluate once _norm(v); assign in source target order to k.
  // Source: vvaharness/models/scan/_coerce.py:31-32
  if (the source predicate k in valid is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:32-32
    End this invocation with k.
  }
  // Source: vvaharness/models/scan/_coerce.py:33-33
  End this invocation with alias.get(k, default).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_coerce.py:36-49
// Source signature: _coerce_int(v, default: int=0) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coerce_int(v, default) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_coerce.py:37-38
  if (the source predicate isinstance(v, bool) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:38-38
    End this invocation with default.
  }
  // Source: vvaharness/models/scan/_coerce.py:39-40
  if (the source predicate isinstance(v, int) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:40-40
    End this invocation with v.
  }
  // Source: vvaharness/models/scan/_coerce.py:41-45
  if (the source predicate isinstance(v, float) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:43-44
    if (the source predicate v != v or v in (float('inf'), float('-inf')) is truthy) {
      // Source: vvaharness/models/scan/_coerce.py:44-44
      End this invocation with default.
    }
    // Source: vvaharness/models/scan/_coerce.py:45-45
    End this invocation with int(v).
  }
  // Source: vvaharness/models/scan/_coerce.py:46-49
  Perform the following protected operations {
    // Source: vvaharness/models/scan/_coerce.py:47-47
    End this invocation with int(str(v).strip()).
  }
  // Source: vvaharness/models/scan/_coerce.py:48-49
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/models/scan/_coerce.py:49-49
    End this invocation with default.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_coerce.py:52-60
// Source signature: flag(v: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn flag(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_coerce.py:53-53
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call.
  // Source: vvaharness/models/scan/_coerce.py:54-55
  if (the source predicate isinstance(v, bool) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:55-55
    End this invocation with v.
  }
  // Source: vvaharness/models/scan/_coerce.py:56-57
  if (the source predicate isinstance(v, str) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:57-57
    End this invocation with v.strip().lower() in {'true', 'yes', '1'}.
  }
  // Source: vvaharness/models/scan/_coerce.py:58-59
  if (the source predicate isinstance(v, (int, float)) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:59-59
    End this invocation with bool(v).
  }
  // Source: vvaharness/models/scan/_coerce.py:60-60
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_coerce.py:63-65
// Source signature: text(v: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn text(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_coerce.py:64-64
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call.
  // Source: vvaharness/models/scan/_coerce.py:65-65
  End this invocation with v if isinstance(v, str) else '' if v is None else str(v).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_coerce.py:68-88
// Source signature: _coerce_scalar_str(v, default, label: str)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coerce_scalar_str(v, default, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_coerce.py:69-69
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call.
  // Source: vvaharness/models/scan/_coerce.py:70-71
  if (the source predicate isinstance(v, str) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:71-71
    End this invocation with v.
  }
  // Source: vvaharness/models/scan/_coerce.py:73-77
  if (the source predicate isinstance(v, (list, tuple)) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:74-76
    In source order: Evaluate once next((x for x in v if x not in (None, '')), None); assign in source target order to first. Then Evaluate log.warning('LLM output coercion: %s was a %d-element list; keeping the first element %r', label, len(v), first); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_coerce.py:77-77
    End this invocation with _coerce_scalar_str(first, default, label).
  }
  // Source: vvaharness/models/scan/_coerce.py:78-83
  if (the source predicate v is None is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:79-80
    if (the source predicate default is None is truthy) {
      // Source: vvaharness/models/scan/_coerce.py:80-80
      End this invocation with None.
    }
    // Source: vvaharness/models/scan/_coerce.py:81-82
    In source order: Evaluate log.warning('LLM output coercion: %s was null; using default %r', label, default); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_coerce.py:83-83
    End this invocation with default.
  }
  // Source: vvaharness/models/scan/_coerce.py:84-87
  if (the source predicate isinstance(v, (int, float)) and (not isinstance(v, bool)) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:85-86
    In source order: Evaluate log.warning('LLM output coercion: %s was a bare %s (%r); using its string form', label, type(v).__name__, v); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_coerce.py:87-87
    End this invocation with str(v).
  }
  // Source: vvaharness/models/scan/_coerce.py:88-88
  End this invocation with v.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/_coerce.py:91-106
// Source signature: _coerce_str_list(v, label: str)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coerce_str_list(v, label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/_coerce.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/models/scan/_coerce.py:93-94
  if (the source predicate isinstance(v, list) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:94-94
    End this invocation with v.
  }
  // Source: vvaharness/models/scan/_coerce.py:95-98
  if (the source predicate v is None is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:96-97
    In source order: Evaluate log.warning('LLM output coercion: %s was null; using an empty list', label); retain side effects and discard the expression result.
    // Source: vvaharness/models/scan/_coerce.py:98-98
    End this invocation with [].
  }
  // Source: vvaharness/models/scan/_coerce.py:99-100
  if (the source predicate isinstance(v, tuple) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:100-100
    End this invocation with list(v).
  }
  // Source: vvaharness/models/scan/_coerce.py:101-105
  if (the source predicate isinstance(v, (str, int, float)) and (not isinstance(v, bool)) is truthy) {
    // Source: vvaharness/models/scan/_coerce.py:102-104
    In source order: Evaluate log.warning('LLM output coercion: %s was a bare %s; wrapping it in a list', label, type(v).__name__); retain side effects and discard the expression result. Then Evaluate once str(v).strip(); assign in source target order to s.
    // Source: vvaharness/models/scan/_coerce.py:105-105
    End this invocation with [s] if s else [].
  }
  // Source: vvaharness/models/scan/_coerce.py:106-106
  End this invocation with v.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
