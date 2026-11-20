# vvaharness/pipeline/stages/s8/prompts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8/prompts.py.evidence.json`. SHA-256: `074685f723acd227f77aafa232d1f6ad6b1e3f0eab67515b5576499b47d3cfd9`.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _confidence_label, _one_line; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s6.prompts import _entry_point_lines; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/prompts.py:22-96
In source order: Resolve source import from vvaharness.pipeline.stages.s8 import facts as _facts; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.outcomes import finding_ids; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Evaluate once source_literal_26_9; assign in source target order to SYSTEM. Then Evaluate once 'step8.prompt_fact_blocks'; assign in source target order to _FACT_BLOCKS.
// Source: vvaharness/pipeline/stages/s8/prompts.py:99-101
// Source signature: facts_enabled(cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn facts_enabled(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:101-101
  End this invocation with bool(knob(cfg, _FACT_BLOCKS, True)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:105-105
In source order: Evaluate once 'step8.hop_text'; assign in source target order to _HOP_TEXT.
// Source: vvaharness/pipeline/stages/s8/prompts.py:108-110
// Source signature: hop_text_enabled(cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn hop_text_enabled(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:109-109
  In source order: Retain source documentation literal source_literal_109_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:110-110
  End this invocation with bool(knob(cfg, _HOP_TEXT, False)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:113-117
// Source signature: _hop_lines(f: Finding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _hop_lines(f) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:114-116
  In source order: Retain source documentation literal source_literal_114_4; it is not a model call. Then Evaluate once (('Scenario', _one_line(f.exploit_scenario)), ('Preconditions', '; '.join(filter(None, map(_one_line, f.preconditions))))); assign in source target order to fields.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:117-117
  End this invocation with ''.join((source_template_117_19 for label, text in fields if text)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:121-127
In source order: Evaluate once source_literal_122_4; assign in source target order to _ENTRY_POINT_CAVEAT.
// Source: vvaharness/pipeline/stages/s8/prompts.py:130-133
// Source signature: _entry_point_block(ctx: ContextPackage) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _entry_point_block(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:131-132
  In source order: Retain source documentation literal source_literal_131_4; it is not a model call. Then Evaluate once _entry_point_lines(ctx); assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:133-133
  End this invocation with source_template_133_11 if lines else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:136-145
// Source signature: reachability_for_finding(f: Finding, ctx: ContextPackage) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reachability_for_finding(f, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:137-138
  In source order: Retain source documentation literal source_literal_137_4; it is not a model call. Then Evaluate once []; assign in source target order to parts.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:139-141
  if (the source predicate f.source_ref is truthy) {
    // Source: vvaharness/pipeline/stages/s8/prompts.py:140-141
    In source order: Evaluate once ' (inferred from AST, unverified)' if 'source_ref' in f.backfilled_refs else ''; assign in source target order to marker. Then Evaluate parts.append(source_template_141_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/prompts.py:142-144
  if (the source predicate f.sink_ref is truthy) {
    // Source: vvaharness/pipeline/stages/s8/prompts.py:143-144
    In source order: Evaluate once ' (inferred from AST, unverified)' if 'sink_ref' in f.backfilled_refs else ''; assign in source target order to marker. Then Evaluate parts.append(source_template_144_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/prompts.py:145-145
  End this invocation with ' '.join(parts) if parts else '(no graph context)'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:148-168
// Source signature: finding_block(fid: str, f: Finding, ctx: ContextPackage, facts_on: bool=True, hop_text: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn finding_block(fid, f, ctx, facts_on, hop_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:150-156
  In source order: Retain source documentation literal source_literal_150_4; it is not a model call. Then Evaluate once f.cvss_vector or 'n/a'; assign in source target order to cvss. Then Evaluate once source_template_152_16 if f.verdict else 'unverified'; assign in source target order to verified. Then Evaluate once reachability_for_finding(f, ctx); assign in source target order to reachability. Then Evaluate once _facts.snippet_for(f, ctx.repo_root, include_decorators=facts_on); assign in source target order to snippet.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:158-165
  In source order: Evaluate once source_template_159_8 + (_hop_lines(f) if hop_text else '') + source_template_164_10; assign in source target order to out.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:166-167
  if (the source predicate snippet is truthy) {
    // Source: vvaharness/pipeline/stages/s8/prompts.py:167-167
    In source order: Apply source augmented assignment out += source_literal_167_15 + _indent_block(snippet) + source_literal_167_56 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s8/prompts.py:168-168
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:171-173
// Source signature: _indent_block(text: str, pad: str='      ') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _indent_block(text, pad) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:172-172
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:173-173
  End this invocation with source_literal_173_11.join((source_template_173_21 for ln in text.splitlines())).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:176-193
// Source signature: repo_fact_blocks(findings: list[Finding], ctx: ContextPackage, labels: list[str], facts_on: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn repo_fact_blocks(findings, ctx, labels, facts_on) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:178-185
  In source order: Retain source documentation literal source_literal_178_4; it is not a model call. Then Evaluate once _facts.exposure_facts(ctx, findings, user_facts=facts_on); assign in source target order to exposure. Then Evaluate once source_literal_181_22.join((source_template_181_32 for e in exposure)) if exposure else '  (not determined)'; assign in source target order to exposure_block. Then Evaluate once _facts.same_location_groups(findings, labels); assign in source target order to colocated. Then Evaluate once source_literal_184_23.join((source_template_184_33 for c in colocated)) if colocated else '  (none)'; assign in source target order to colocated_block.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:186-186
  In source order: Evaluate once _entry_point_block(ctx) if facts_on else ''; assign in source target order to entry_block.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:187-193
  End this invocation with source_template_187_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:196-264
// Source signature: build_prompt(findings: list[Finding], ctx: ContextPackage, *, labels: list[str] | None=None, cfg=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_prompt(findings, ctx, labels, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:198-198
  In source order: Retain source documentation literal source_literal_198_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:199-200
  if (the source predicate labels is None is truthy) {
    // Source: vvaharness/pipeline/stages/s8/prompts.py:200-200
    In source order: Evaluate once list(finding_ids(findings)); assign in source target order to labels.
  }
  // Source: vvaharness/pipeline/stages/s8/prompts.py:201-210
  In source order: Evaluate once facts_enabled(cfg); assign in source target order to facts_on. Then Evaluate once hop_text_enabled(cfg); assign in source target order to hop_text. Then Evaluate once [finding_block(fid, f, ctx, facts_on, hop_text) for fid, f in zip(labels, findings)]; assign in source target order to blocks. Then Evaluate once source_literal_205_21.join(blocks); assign in source target order to findings_block. Then Evaluate once source_literal_207_21.join((source_template_208_8 for c in ctx.design_controls)) or '  (none)'; assign in source target order to controls_block.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:212-217
  In source order: Evaluate once source_literal_212_16.join((source_template_213_8 for c in ctx.known_cves)) or '  (none)'; assign in source target order to cve_block. Then Evaluate once ''; assign in source target order to tm_block.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:218-219
  if (the source predicate ctx.app_profile is truthy) {
    // Source: vvaharness/pipeline/stages/s8/prompts.py:219-219
    In source order: Apply source augmented assignment tm_block += ctx.app_profile.to_prompt_block() + source_literal_219_56 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s8/prompts.py:220-221
  if (the source predicate ctx.threat_model is truthy) {
    // Source: vvaharness/pipeline/stages/s8/prompts.py:221-221
    In source order: Apply source augmented assignment tm_block += ctx.threat_model.to_prompt_block() + source_literal_221_57 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
  End this invocation with source_template_223_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:267-275
// Source signature: repair_prompt(raw: str, err: Exception) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn repair_prompt(raw, err) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:268-268
  In source order: Retain source documentation literal source_literal_268_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/prompts.py:269-275
  End this invocation with source_template_270_8.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import ContextPackage, Finding` at source line 19: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.scan._render import _confidence_label, _one_line` at source line 20: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.pipeline.stages.s6.prompts import _entry_point_lines` at source line 21: `source_detail/vvaharness/pipeline/stages/s6/prompts.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8 import facts as _facts` at source line 22: `source_detail/vvaharness/pipeline/stages/s8/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8 import facts as _facts` at source line 22: `source_detail/vvaharness/pipeline/stages/s8/facts.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.outcomes import finding_ids` at source line 23: `source_detail/vvaharness/pipeline/stages/s8/outcomes.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 24: `source_detail/vvaharness/util/config.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s8/prompts.py.sudo.md). Exact strings in the evidence asset support this conversion.
