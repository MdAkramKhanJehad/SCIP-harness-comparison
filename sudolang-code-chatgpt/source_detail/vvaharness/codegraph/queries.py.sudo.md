# vvaharness/codegraph/queries.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/codegraph/queries.py.evidence.json`. SHA-256: `f0f021264e775d6f18be6177c482fb0a9198c44e67bd27e937737a397e870d11`.

```sudo
// Source: vvaharness/codegraph/queries.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.handle import GraphHandle; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/codegraph/queries.py:23-40
In source order: Evaluate once source_literal_23_25; assign in source target order to _COMMUNITY_FILES_QUERY. Then Evaluate once source_literal_29_25; assign in source target order to _LANGUAGE_COUNTS_QUERY. Then Evaluate once {'files': 'MATCH (f:File) RETURN count(f) AS n', 'functions': 'MATCH (fn:Function) RETURN count(fn) AS n', 'communities': 'MATCH (c:Community) RETURN count(c) AS n'}; assign in source target order to _COUNT_QUERIES.
// Source: vvaharness/codegraph/queries.py:43-54
// Source signature: communities_as_modules(handle: GraphHandle) -> dict[str, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn communities_as_modules(handle) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/queries.py:44-45
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then For modules, assign {}; source annotation dict[str, list[str]].
  // Source: vvaharness/codegraph/queries.py:46-53
  for each row in handle.graph.cypher(_COMMUNITY_FILES_QUERY).rows {
    // Source: vvaharness/codegraph/queries.py:47-48
    In source order: Evaluate once row.to_dict(); assign in source target order to values. Then Evaluate once (values.get('community'), values.get('path')); assign in source target order to (name, path).
    // Source: vvaharness/codegraph/queries.py:49-50
    if (the source predicate not isinstance(name, str) or not isinstance(path, str) is truthy) {
      // Source: vvaharness/codegraph/queries.py:50-50
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/codegraph/queries.py:51-51
    In source order: Evaluate modules.setdefault(name, []); retain side effects and discard the expression result.
    // Source: vvaharness/codegraph/queries.py:52-53
    if (the source predicate path not in modules[name] is truthy) {
      // Source: vvaharness/codegraph/queries.py:53-53
      In source order: Evaluate modules[name].append(path); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/codegraph/queries.py:54-54
  End this invocation with modules.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/queries.py:57-63
// Source signature: primary_language(handle: GraphHandle) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn primary_language(handle) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/queries.py:58-59
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then Evaluate once handle.graph.cypher(_LANGUAGE_COUNTS_QUERY).rows; assign in source target order to rows.
  // Source: vvaharness/codegraph/queries.py:60-61
  if (the source predicate not rows is truthy) {
    // Source: vvaharness/codegraph/queries.py:61-61
    End this invocation with None.
  }
  // Source: vvaharness/codegraph/queries.py:62-62
  In source order: Evaluate once rows[0].to_dict().get('language'); assign in source target order to language.
  // Source: vvaharness/codegraph/queries.py:63-63
  End this invocation with language if isinstance(language, str) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/queries.py:66-71
// Source signature: _int_count(handle: GraphHandle, query: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _int_count(handle, query) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/queries.py:67-67
  In source order: Evaluate once handle.graph.cypher(query).rows; assign in source target order to rows.
  // Source: vvaharness/codegraph/queries.py:68-69
  if (the source predicate not rows is truthy) {
    // Source: vvaharness/codegraph/queries.py:69-69
    End this invocation with 0.
  }
  // Source: vvaharness/codegraph/queries.py:70-70
  In source order: Evaluate once rows[0].to_dict().get('n'); assign in source target order to n.
  // Source: vvaharness/codegraph/queries.py:71-71
  End this invocation with n if isinstance(n, int) else 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/queries.py:74-84
// Source signature: system_context_notes(handle: GraphHandle) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn system_context_notes(handle) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/queries.py:75-81
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once {key: _int_count(handle, query) for key, query in _COUNT_QUERIES.items()}; assign in source target order to counts. Then Evaluate once [lang for r in handle.graph.cypher(_LANGUAGE_COUNTS_QUERY).rows if isinstance((lang := r.to_dict().get('language')), str)]; assign in source target order to languages. Then Evaluate once ', '.join(languages[:5]) or 'unknown'; assign in source target order to lang_str.
  // Source: vvaharness/codegraph/queries.py:82-84
  End this invocation with source_template_82_12.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.codegraph.handle import GraphHandle` at source line 18: `source_detail/vvaharness/codegraph/handle.py.sudo.md`.
- `from vvaharness.util import logs` at source line 19: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 19: `source_detail/vvaharness/util/logs.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/codegraph/queries.py.sudo.md). Exact strings in the evidence asset support this conversion.
