# vvaharness/agentdoc.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/agentdoc.py.evidence.json`. SHA-256: `14c9514d9a32539bf05fa84d40760de91614ba66d0aef4f17353eef06e10dda6`.

```sudo
// Source: vvaharness/agentdoc.py:15-102
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Evaluate once source_literal_26_12; assign in source target order to AGENT_DOC. Then Evaluate once source_literal_95_4 + AGENT_DOC; assign in source target order to CLAUDE_SKILL.
// Source: vvaharness/agentdoc.py:105-106
// Source signature: gemini_doc() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gemini_doc() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/agentdoc.py:106-106
  End this invocation with AGENT_DOC.replace('(for AI coding agents)', '(for the Gemini CLI)').
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../prompt_representation/vvaharness/agentdoc.py.sudo.md). Exact strings in the evidence asset support this conversion.
