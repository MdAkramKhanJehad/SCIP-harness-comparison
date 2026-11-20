# vvaharness/validation/subagents/models.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/subagents/models.py.evidence.json`. SHA-256: `1bc5d52480f8232dd9380c873f641919d50d6af16e26a97ce9c206348c4e0214`.

```sudo
// Source: vvaharness/validation/subagents/models.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import from typing_extensions import TypedDict; preserve alias and import-time effects.
// Source: vvaharness/validation/subagents/models.py:24-32
interface SubagentFrontmatterMeta {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/subagents/models.py:25-30
  In source order: Retain source documentation literal source_literal_25_4; it is not a model call. Then For name, declare without assigning a value; source annotation str. Then For model, declare without assigning a value; source annotation str. Then For description, declare without assigning a value; source annotation str. Then For allowedTools, declare without assigning a value; source annotation list[str].
  // Source: vvaharness/validation/subagents/models.py:31-32
  In source order: For deniedTools, declare without assigning a value; source annotation list[str]. Then For skills, declare without assigning a value; source annotation list[str].
}
// Source: vvaharness/validation/subagents/models.py:35-39
interface ParsedFrontmatter {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/subagents/models.py:36-39
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then For meta, declare without assigning a value; source annotation SubagentFrontmatterMeta. Then For body, declare without assigning a value; source annotation str.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
