# vvaharness/plugins/semgrep/triage.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/plugins/semgrep/triage.py.evidence.json`. SHA-256: `7fa0d3cf1a968a098d921bfed1c75d65d1fa73473b503bf4b326e03bf36aec79`.

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:15-36
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import SubagentDefinition; preserve alias and import-time effects. Then Resolve source import from vvaharness.plugins.semgrep.tools import SEMGREP_TOOL_NAMES; preserve alias and import-time effects. Then Evaluate once source_literal_21_17; assign in source target order to _TRIAGE_PROMPT.
// Source: vvaharness/plugins/semgrep/triage.py:39-48
// Source signature: semgrep_triage_subagent(tools: tuple[str, ...]=SEMGREP_TOOL_NAMES) -> SubagentDefinition
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn semgrep_triage_subagent(tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/triage.py:40-40
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/triage.py:41-48
  End this invocation with SubagentDefinition(name='semgrep-triage', description=source_literal_43_21, prompt=_TRIAGE_PROMPT, tools=tuple(tools)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/triage.py:51-51
In source order: Evaluate once ['semgrep_triage_subagent']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness import SubagentDefinition` at source line 18: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.plugins.semgrep.tools import SEMGREP_TOOL_NAMES` at source line 19: `source_detail/vvaharness/plugins/semgrep/tools.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/plugins/semgrep/triage.py.sudo.md). Exact strings in the evidence asset support this conversion.
