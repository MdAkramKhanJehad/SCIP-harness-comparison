# vvaharness/detect/spec.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/detect/spec.py.evidence.json`. SHA-256: `b13d5c2b76fde86d2dc75de56d32ba1f17c71b6ae199b43f16c6204fffbd7977`.

```sudo
// Source: vvaharness/detect/spec.py:15-18
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects.
// Source: vvaharness/detect/spec.py:22-48
// Source: vvaharness/detect/spec.py:21-21
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/detect/spec.py:22-48
interface MatchSpec {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/detect/spec.py:23-28
  In source order: Retain source documentation literal source_literal_23_4; it is not a model call. Then For rule_id, declare without assigning a value; source annotation str. Then For role, declare without assigning a value; source annotation str. Then For pattern, declare without assigning a value; source annotation str. Then For cwe, declare without assigning a value; source annotation str.
  // Source: vvaharness/detect/spec.py:29-35
  In source order: For kind, declare without assigning a value; source annotation str. Then For semantic_family, assign ''; source annotation str. Then For owasp_top10_2025, assign field(default_factory=frozenset); source annotation frozenset[str]. Then For enabled, assign True; source annotation bool. Then For languages, assign field(default_factory=frozenset); source annotation frozenset[str].
  // Source: vvaharness/detect/spec.py:36-41
  In source order: For title, assign ''; source annotation str. Then For citation, assign ''; source annotation str. Then For span, assign 'line'; source annotation str. Then For span_end, assign ''; source annotation str. Then For span_max_lines, assign 1; source annotation int.
  // Source: vvaharness/detect/spec.py:42-47
  In source order: For present_re, assign ''; source annotation str. Then For absent_re, assign ''; source annotation str. Then For absent_window, assign 0; source annotation int. Then For file_re, assign ''; source annotation str. Then For near_re, assign ''; source annotation str.
  // Source: vvaharness/detect/spec.py:48-48
  In source order: For near_window, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
