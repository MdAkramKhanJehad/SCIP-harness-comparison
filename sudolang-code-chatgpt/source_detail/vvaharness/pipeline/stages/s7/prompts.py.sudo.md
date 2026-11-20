# vvaharness/pipeline/stages/s7/prompts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s7/prompts.py.evidence.json`. SHA-256: `149d0652f8f21830a6931bc3a8b9a7da14f3263bef4bf3c90da87833997157ce`.

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:16-66
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Finding; preserve alias and import-time effects. Then Evaluate once source_literal_23_9; assign in source target order to SYSTEM.
// Source: vvaharness/pipeline/stages/s7/prompts.py:69-83
// Source signature: build_payload(verified: list[Finding], unresolved: list[int]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_payload(verified, unresolved) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s7/prompts.py:70-82
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once [{'index': local, 'file': verified[g].file, 'line': verified[g].line_start, 'category': verified[g].vuln_class.value, 'title': verified[g].title, 'description': verified[g].description[:500], 'exploit_scenario': verified[g].exploit_scenario[:300], 'cwe': verified[g].cwe, 'source_ref': verified[g].source_ref, 'sink_ref': verified[g].sink_ref} for local, g in enumerate(unresolved)]; assign in source target order to payload.
  // Source: vvaharness/pipeline/stages/s7/prompts.py:83-83
  End this invocation with source_literal_83_11 + json.dumps(payload, indent=2).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Finding` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s7/prompts.py.sudo.md). Exact strings in the evidence asset support this conversion.
