# vvaharness/backends/harness/capabilities.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/harness/capabilities.py.evidence.json`. SHA-256: `3e490a2d354f7a83e9baa616ef570072541ad680203eece182ae41cb2c9e2c36`.

```sudo
// Source: vvaharness/backends/harness/capabilities.py:15-24
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from typing import Final, NamedTuple; preserve alias and import-time effects. Then Evaluate once ['HarnessCapabilities', 'capabilities_for']; assign in source target order to __all__.
// Source: vvaharness/backends/harness/capabilities.py:27-31
interface HarnessCapabilities {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/backends/harness/capabilities.py:28-31
  In source order: Retain source documentation literal source_literal_28_4; it is not a model call. Then For reads_injected_claude_config, declare without assigning a value; source annotation bool. Then For returns_schema_validated_reports, declare without assigning a value; source annotation bool.
}
// Source: vvaharness/backends/harness/capabilities.py:35-55
In source order: For _NONE, assign HarnessCapabilities(reads_injected_claude_config=False, returns_schema_validated_reports=False); source annotation Final. Then For _BY_VIA, assign {'cli': HarnessCapabilities(reads_injected_claude_config=True, returns_schema_validated_reports=True), 'sdk': HarnessCapabilities(reads_injected_claude_config=True, returns_schema_validated_reports=True), 'deepagents': HarnessCapabilities(reads_injected_claude_config=False, returns_schema_validated_reports=True)}; source annotation Final[Mapping[str, HarnessCapabilities]].
// Source: vvaharness/backends/harness/capabilities.py:58-60
// Source signature: capabilities_for(via: str | None) -> HarnessCapabilities
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn capabilities_for(via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/harness/capabilities.py:59-59
  In source order: Retain source documentation literal source_literal_59_4; it is not a model call.
  // Source: vvaharness/backends/harness/capabilities.py:60-60
  End this invocation with _BY_VIA.get(via or '', _NONE).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
