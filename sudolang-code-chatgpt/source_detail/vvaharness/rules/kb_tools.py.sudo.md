# vvaharness/rules/kb_tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/rules/kb_tools.py.evidence.json`. SHA-256: `ce69ad1baeb61ff5e55c38f27dda580c7b5524c420b6c5be835cb608ad63ffab`.

```sudo
// Source: vvaharness/rules/kb_tools.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Sequence; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool, tool; preserve alias and import-time effects.
// Source: vvaharness/rules/kb_tools.py:23-29
In source order: Resolve source import from vvaharness.backends.harness import StreamingOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules import CweKB; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then For KB_TOOL_NAMES, assign ('CweGuidance',); source annotation tuple[str, ...]. Then Evaluate once threading.Lock(); assign in source target order to _unknown_cwe_lock.
// Source: vvaharness/rules/kb_tools.py:30-30
In source order: For _unknown_cwe_ids, assign set(); source annotation set[str].
// Source: vvaharness/rules/kb_tools.py:33-42
// Source signature: _note_unknown_cwe(cwe_id: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _note_unknown_cwe(cwe_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/kb_tools.py:34-34
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call.
  // Source: vvaharness/rules/kb_tools.py:37-41
  Enter source context managers left-to-right: _unknown_cwe_lock {
    // Source: vvaharness/rules/kb_tools.py:38-39
    if (the source predicate cwe_id in _unknown_cwe_ids is truthy) {
      // Source: vvaharness/rules/kb_tools.py:39-39
      End this invocation with None.
    }
    // Source: vvaharness/rules/kb_tools.py:40-41
    In source order: Evaluate _unknown_cwe_ids.add(cwe_id); retain side effects and discard the expression result. Then Evaluate once ','.join(sorted(_unknown_cwe_ids)); assign in source target order to ids.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/rules/kb_tools.py:42-42
  In source order: Evaluate COUNTERS.note('s4_cwe_guidance_unknown_ids', ids); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/rules/kb_tools.py:46-55
// Source: vvaharness/rules/kb_tools.py:45-45
Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
// Source: vvaharness/rules/kb_tools.py:46-55
// Source signature: CweGuidance(cwe_id: str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn CweGuidance(cwe_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/kb_tools.py:47-50
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then Evaluate COUNTERS.bump('s4_cwe_guidance_called'); retain side effects and discard the expression result. Then Evaluate once CweKB.load().for_cwes([cwe_id]); assign in source target order to entry.
  // Source: vvaharness/rules/kb_tools.py:52-54
  if (the source predicate not entry.get('cwe') is truthy) {
    // Source: vvaharness/rules/kb_tools.py:53-54
    In source order: Evaluate COUNTERS.bump('s4_cwe_guidance_unknown_cwe'); retain side effects and discard the expression result. Then Evaluate _note_unknown_cwe(cwe_id); retain side effects and discard the expression result.
  }
  // Source: vvaharness/rules/kb_tools.py:55-55
  End this invocation with entry.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/rules/kb_tools.py:58-66
// Source signature: build_kb_tool_builder()
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_kb_tool_builder() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/kb_tools.py:59-59
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call.
  // Source: vvaharness/rules/kb_tools.py:61-64
  // Source signature: _build(options: StreamingOptions, *, allowed_tools: Sequence[str] | None=None) -> list[BaseTool]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _build(options, allowed_tools) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/kb_tools.py:62-63
    if (the source predicate 'CweGuidance' not in set(getattr(options, 'fact_tools', ()) or ()) is truthy) {
      // Source: vvaharness/rules/kb_tools.py:63-63
      End this invocation with [].
    }
    // Source: vvaharness/rules/kb_tools.py:64-64
    End this invocation with [CweGuidance].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/rules/kb_tools.py:66-66
  End this invocation with _build.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/rules/kb_tools.py:69-69
In source order: Evaluate once ['KB_TOOL_NAMES', 'CweGuidance', 'build_kb_tool_builder']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness import StreamingOptions` at source line 23: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.rules import CweKB` at source line 24: `source_detail/vvaharness/rules/__init__.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 25: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/rules/kb_tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
