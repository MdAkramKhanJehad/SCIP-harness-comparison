# vvaharness/validation/tools/deep_tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/tools/deep_tools.py.evidence.json`. SHA-256: `e33204aaec384af66bee95949edf97ae38552fbc8a1936fd0117d3b43d5b791f`.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool, tool; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import StreamingOptions; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/deep_tools.py:24-31
In source order: Resolve source import from vvaharness.backends.harness.deepagents.tools import build_tools as build_reader_tools; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.tools.diff_facts import build_diff_impact_map, changed_lines, diff_touched; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.tools.pattern_scanner import pattern_scan; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.tools.test_inventory import test_inventory; preserve alias and import-time effects.
// Source: vvaharness/validation/tools/deep_tools.py:33-34
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/validation/tools/deep_tools.py:34-34
  In source order: Resolve source import from collections.abc import Sequence; preserve alias and import-time effects.
}
// Source: vvaharness/validation/tools/deep_tools.py:37-90
// Source signature: _fact_tools(options: StreamingOptions, allowed: set[str]) -> list[BaseTool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fact_tools(options, allowed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/deep_tools.py:38-40
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then Evaluate once options.cwd; assign in source target order to workspace. Then For tools, assign []; source annotation list[BaseTool].
  // Source: vvaharness/validation/tools/deep_tools.py:42-48
  if (the source predicate 'DiffTouched' in allowed is truthy) {
    // Source: vvaharness/validation/tools/deep_tools.py:44-46
    // Source: vvaharness/validation/tools/deep_tools.py:43-43
    Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
    // Source: vvaharness/validation/tools/deep_tools.py:44-46
    // Source signature: DiffTouched(file_path: str) -> dict
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn DiffTouched(file_path) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/validation/tools/deep_tools.py:45-45
      In source order: Retain source documentation literal source_literal_45_12; it is not a model call.
      // Source: vvaharness/validation/tools/deep_tools.py:46-46
      End this invocation with diff_touched(workspace, file_path).
      If execution reaches this end, finish with the source implicit None result.
    }
    At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
    // Source: vvaharness/validation/tools/deep_tools.py:48-48
    In source order: Evaluate tools.append(DiffTouched); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/deep_tools.py:50-56
  if (the source predicate 'ChangedLines' in allowed is truthy) {
    // Source: vvaharness/validation/tools/deep_tools.py:52-54
    // Source: vvaharness/validation/tools/deep_tools.py:51-51
    Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
    // Source: vvaharness/validation/tools/deep_tools.py:52-54
    // Source signature: ChangedLines(file_path: str) -> list[tuple[int, int]]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn ChangedLines(file_path) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/validation/tools/deep_tools.py:53-53
      In source order: Retain source documentation literal source_literal_53_12; it is not a model call.
      // Source: vvaharness/validation/tools/deep_tools.py:54-54
      End this invocation with changed_lines(workspace, file_path).
      If execution reaches this end, finish with the source implicit None result.
    }
    At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
    // Source: vvaharness/validation/tools/deep_tools.py:56-56
    In source order: Evaluate tools.append(ChangedLines); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/deep_tools.py:58-68
  if (the source predicate 'DiffImpactMap' in allowed is truthy) {
    // Source: vvaharness/validation/tools/deep_tools.py:60-66
    // Source: vvaharness/validation/tools/deep_tools.py:59-59
    Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
    // Source: vvaharness/validation/tools/deep_tools.py:60-66
    // Source signature: DiffImpactMap() -> dict
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn DiffImpactMap() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/validation/tools/deep_tools.py:61-62
      In source order: Retain source documentation literal source_literal_61_12; it is not a model call. Then Evaluate once build_diff_impact_map(workspace); assign in source target order to impact.
      // Source: vvaharness/validation/tools/deep_tools.py:63-66
      End this invocation with {'files_changed': impact.files_changed, 'trust_boundary_touched': impact.trust_boundary_touched}.
      If execution reaches this end, finish with the source implicit None result.
    }
    At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
    // Source: vvaharness/validation/tools/deep_tools.py:68-68
    In source order: Evaluate tools.append(DiffImpactMap); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/deep_tools.py:70-80
  if (the source predicate 'PatternScan' in allowed is truthy) {
    // Source: vvaharness/validation/tools/deep_tools.py:72-78
    // Source: vvaharness/validation/tools/deep_tools.py:71-71
    Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
    // Source: vvaharness/validation/tools/deep_tools.py:72-78
    // Source signature: PatternScan(pattern_set: str) -> list[dict]
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn PatternScan(pattern_set) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/validation/tools/deep_tools.py:73-77
      In source order: Retain source documentation literal source_literal_73_12; it is not a model call.
      // Source: vvaharness/validation/tools/deep_tools.py:78-78
      End this invocation with pattern_scan(workspace, pattern_set).
      If execution reaches this end, finish with the source implicit None result.
    }
    At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
    // Source: vvaharness/validation/tools/deep_tools.py:80-80
    In source order: Evaluate tools.append(PatternScan); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/deep_tools.py:82-88
  if (the source predicate 'TestInventory' in allowed is truthy) {
    // Source: vvaharness/validation/tools/deep_tools.py:84-86
    // Source: vvaharness/validation/tools/deep_tools.py:83-83
    Before creating this callable, evaluate and retain decorators top-to-bottom: tool.
    // Source: vvaharness/validation/tools/deep_tools.py:84-86
    // Source signature: TestInventory() -> dict
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn TestInventory() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/validation/tools/deep_tools.py:85-85
      In source order: Retain source documentation literal source_literal_85_12; it is not a model call.
      // Source: vvaharness/validation/tools/deep_tools.py:86-86
      End this invocation with test_inventory(workspace).
      If execution reaches this end, finish with the source implicit None result.
    }
    At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
    // Source: vvaharness/validation/tools/deep_tools.py:88-88
    In source order: Evaluate tools.append(TestInventory); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/tools/deep_tools.py:90-90
  End this invocation with tools.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/deep_tools.py:93-101
// Source signature: build_validation_tools(options: StreamingOptions, *, allowed_tools: Sequence[str] | None) -> list[BaseTool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_validation_tools(options, allowed_tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/tools/deep_tools.py:98-100
  In source order: Retain source documentation literal source_literal_98_4; it is not a model call. Then Evaluate once build_reader_tools(options, allowed_tools=allowed_tools); assign in source target order to reader_tools. Then Evaluate once set(allowed_tools if allowed_tools is not None else ()); assign in source target order to allowed.
  // Source: vvaharness/validation/tools/deep_tools.py:101-101
  End this invocation with reader_tools + _fact_tools(options, allowed).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/tools/deep_tools.py:104-104
In source order: Evaluate once ['build_validation_tools']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.backends.harness import StreamingOptions` at source line 23: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tools import build_tools as build_reader_tools` at source line 24: `source_detail/vvaharness/backends/harness/deepagents/tools.py.sudo.md`.
- `from vvaharness.validation.tools.diff_facts import build_diff_impact_map, changed_lines, diff_touched` at source line 25: `source_detail/vvaharness/validation/tools/diff_facts.py.sudo.md`.
- `from vvaharness.validation.tools.pattern_scanner import pattern_scan` at source line 30: `source_detail/vvaharness/validation/tools/pattern_scanner.py.sudo.md`.
- `from vvaharness.validation.tools.test_inventory import test_inventory` at source line 31: `source_detail/vvaharness/validation/tools/test_inventory.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/tools/deep_tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
