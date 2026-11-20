# vvaharness/evidence/render.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/render.py.evidence.json`. SHA-256: `f1cd310892e52fdc56552636314e4ba944e1aad061085d475aa3c32312806450`.

```sudo
// Source: vvaharness/evidence/render.py:15-18
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.gather import ThreatEvidence; preserve alias and import-time effects.
// Source: vvaharness/evidence/render.py:21-23
// Source signature: render_language_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_language_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:22-22
  In source order: Retain source documentation literal source_literal_22_4; it is not a model call.
  // Source: vvaharness/evidence/render.py:23-23
  End this invocation with source_literal_23_11.join((source_template_23_21 for lang, n in ev.languages)) or '  (none detected)'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:26-28
// Source signature: render_components_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_components_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:27-27
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call.
  // Source: vvaharness/evidence/render.py:28-28
  End this invocation with source_literal_28_11.join((source_template_28_21 for d in ev.top_dirs)) or '  (flat repo)'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:31-43
// Source signature: render_inventory_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_inventory_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:32-33
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then For by_dir, assign {}; source annotation dict[str, list[str]].
  // Source: vvaharness/evidence/render.py:34-36
  for each rel in ev.inventory {
    // Source: vvaharness/evidence/render.py:35-36
    In source order: Evaluate once rel.rpartition('/'); assign in source target order to (head, _, tail). Then Evaluate by_dir.setdefault(head or '.', []).append(tail); retain side effects and discard the expression result.
  }
  // Source: vvaharness/evidence/render.py:37-40
  In source order: Evaluate once source_literal_37_12.join((source_template_38_8 + '  '.join(sorted(names)) for d, names in sorted(by_dir.items()))) or '  (no files in scope)'; assign in source target order to block.
  // Source: vvaharness/evidence/render.py:41-42
  if (the source predicate ev.inventory_truncated is truthy) {
    // Source: vvaharness/evidence/render.py:42-42
    In source order: Apply source augmented assignment block += source_literal_42_17 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/evidence/render.py:43-43
  End this invocation with block.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:46-53
// Source signature: render_modules_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_modules_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:47-50
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then Evaluate once source_literal_48_12.join((source_template_49_8 for name, purpose, loc in ev.modules)) or '  (s1 emitted no modules)'; assign in source target order to block.
  // Source: vvaharness/evidence/render.py:51-52
  if (the source predicate ev.modules_truncated is truthy) {
    // Source: vvaharness/evidence/render.py:52-52
    In source order: Apply source augmented assignment block += source_literal_52_17 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/evidence/render.py:53-53
  End this invocation with block.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:56-65
// Source signature: render_entry_points_block(ev: ThreatEvidence, stride_by_kind: dict[str, str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_entry_points_block(ev, stride_by_kind) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:57-62
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call. Then Evaluate once source_literal_58_12.join((source_template_59_8 for kind, unauth, file, func in ev.entry_points)) or '  (s1 emitted no entry points)'; assign in source target order to block.
  // Source: vvaharness/evidence/render.py:63-64
  if (the source predicate ev.entry_points_truncated is truthy) {
    // Source: vvaharness/evidence/render.py:64-64
    In source order: Apply source augmented assignment block += source_literal_64_17 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/evidence/render.py:65-65
  End this invocation with block.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:68-72
// Source signature: render_config_reps_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_config_reps_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:69-69
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call.
  // Source: vvaharness/evidence/render.py:70-72
  End this invocation with source_literal_70_11.join((source_template_71_8 if body else source_template_71_48 for rel, body in ev.config_reps)) or '  (none)'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:75-77
// Source signature: render_api_artefacts_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_api_artefacts_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vvaharness/evidence/render.py:77-77
  End this invocation with source_literal_77_11.join((source_template_77_21 for p in ev.api_artefacts)) or '  (none)'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:80-84
// Source signature: render_docs_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_docs_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/evidence/render.py:82-84
  End this invocation with source_literal_82_11.join((source_template_83_8 for name, body in ev.docs)) or '(no README / SECURITY / ARCHITECTURE docs found)'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/evidence/render.py:87-91
// Source signature: render_manifests_block(ev: ThreatEvidence) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn render_manifests_block(ev) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/render.py:88-88
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call.
  // Source: vvaharness/evidence/render.py:89-91
  End this invocation with source_literal_89_11.join((source_template_90_8 for name, body in ev.manifests)) or '(no build/dependency manifests found)'.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.evidence.gather import ThreatEvidence` at source line 18: `source_detail/vvaharness/evidence/gather.py.sudo.md`.
