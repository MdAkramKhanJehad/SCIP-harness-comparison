# vvaharness/remediation_agent/models/change.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/models/change.py.evidence.json`. SHA-256: `ebfb278f339f96d34088f2532b9034c8580b73a54235dd906997693310e6e9e5`.

```sudo
// Source: vvaharness/remediation_agent/models/change.py:15-18
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/models/change.py:21-23
interface Change {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/models/change.py:22-23
  In source order: For file, assign Field(default='', description='repo-relative path that was edited'); source annotation str. Then For summary, assign Field(default='', description='what changed and why (≤ 2 sentences)'); source annotation str.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/models/change.py.sudo.md). Exact strings in the evidence asset support this conversion.
