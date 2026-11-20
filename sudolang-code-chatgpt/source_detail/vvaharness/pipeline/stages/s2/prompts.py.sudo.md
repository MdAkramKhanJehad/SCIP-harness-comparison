# vvaharness/pipeline/stages/s2/prompts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s2/prompts.py.evidence.json`. SHA-256: `3013bbc9d898c27241d99a88c19649cb6b5e95339b9da98d630f27c8105d34b2`.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:16-32
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence import ThreatEvidence, render_api_artefacts_block, render_components_block, render_config_reps_block, render_docs_block, render_entry_points_block, render_inventory_block, render_language_block, render_manifests_block, render_modules_block; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import CVE, AppProfile, ContextPackage, Control; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.repo_kinds import BASELINES, STRIDE_BY_KIND, repo_kind; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-206
In source order: Evaluate once source_literal_35_9; assign in source target order to SYSTEM. Then Evaluate once source_literal_169_4; assign in source target order to _AGENTIC_SYSTEM_LINE. Then Evaluate once source_literal_177_4; assign in source target order to _GRAPH_TOOLS_SYSTEM_LINE. Then Evaluate once source_literal_194_4; assign in source target order to _SHELL_SYSTEM_LINE.
// Source: vvaharness/pipeline/stages/s2/prompts.py:207-239
// Source signature: _baseline_block(ev: ThreatEvidence, ctx: ContextPackage | None, mode: str) -> tuple[set[str], str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _baseline_block(ev, ctx, mode) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:208-209
  if (the source predicate mode == 'none' is truthy) {
    // Source: vvaharness/pipeline/stages/s2/prompts.py:209-209
    End this invocation with (set(), '').
  }
  // Source: vvaharness/pipeline/stages/s2/prompts.py:210-212
  In source order: Evaluate once {'web-api'} if mode == 'owasp' else repo_kind(ev, ctx); assign in source target order to kinds. Then For seen, assign set(); source annotation set[str]. Then For items, assign []; source annotation list[tuple[str, str]].
  // Source: vvaharness/pipeline/stages/s2/prompts.py:213-217
  for each k in sorted(kinds) {
    // Source: vvaharness/pipeline/stages/s2/prompts.py:214-217
    for each (bid, text) in BASELINES.get(k, ()) {
      // Source: vvaharness/pipeline/stages/s2/prompts.py:215-217
      if (the source predicate bid not in seen is truthy) {
        // Source: vvaharness/pipeline/stages/s2/prompts.py:216-217
        In source order: Evaluate seen.add(bid); retain side effects and discard the expression result. Then Evaluate items.append((bid, text)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s2/prompts.py:218-219
  if (the source predicate not items is truthy) {
    // Source: vvaharness/pipeline/stages/s2/prompts.py:219-219
    End this invocation with (kinds, '').
  }
  // Source: vvaharness/pipeline/stages/s2/prompts.py:220-220
  In source order: Evaluate once source_literal_220_11.join((source_template_220_21 for bid, text in items)); assign in source target order to body.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:221-239
  End this invocation with (kinds, source_template_222_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/prompts.py:240-323
// Source signature: _build_user_prompt(repo_name: str, ev: ThreatEvidence, cves: list[CVE], controls: list[Control], app_profile: AppProfile | None=None, baseline_block: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_user_prompt(repo_name, ev, cves, controls, app_profile, baseline_block) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:244-248
  In source order: Evaluate once render_language_block(ev); assign in source target order to lang_block. Then Evaluate once render_components_block(ev); assign in source target order to comp_block. Then Evaluate once render_inventory_block(ev); assign in source target order to inv_block. Then Evaluate once render_modules_block(ev); assign in source target order to mod_block. Then Evaluate once render_entry_points_block(ev, STRIDE_BY_KIND); assign in source target order to ep_block.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:249-257
  In source order: Evaluate once render_config_reps_block(ev); assign in source target order to cfg_block. Then Evaluate once render_api_artefacts_block(ev); assign in source target order to api_block. Then Evaluate once render_docs_block(ev); assign in source target order to docs_block. Then Evaluate once render_manifests_block(ev); assign in source target order to manifest_block. Then Evaluate once source_literal_254_16.join((source_template_255_8 for c in cves)) or '  (none on file)'; assign in source target order to cve_block.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:258-264
  In source order: Evaluate once source_literal_258_16.join((source_template_259_8 + (source_template_260_11 if c.notes else '') for c in controls)) or '  (none on file)'; assign in source target order to ctl_block. Then Evaluate once ''; assign in source target order to cmdb_block.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:265-270
  if (the source predicate app_profile is truthy) {
    // Source: vvaharness/pipeline/stages/s2/prompts.py:266-270
    In source order: Evaluate once app_profile.to_prompt_block() + source_literal_267_24; assign in source target order to cmdb_block.
  }
  // Source: vvaharness/pipeline/stages/s2/prompts.py:272-272
  In source order: Evaluate once ''; assign in source target order to notes_block.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:273-274
  if (the source predicate ev.s1_notes is truthy) {
    // Source: vvaharness/pipeline/stages/s2/prompts.py:274-274
    In source order: Evaluate once source_template_274_22; assign in source target order to notes_block.
  }
  // Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
  End this invocation with source_template_277_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s2/prompts.py:324-340
// Source signature: _repair_json_prompt(raw: str, err: Exception) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repair_json_prompt(raw, err) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:325-325
  In source order: Retain source documentation literal source_literal_325_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s2/prompts.py:326-340
  End this invocation with source_template_326_11.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.evidence import ThreatEvidence, render_api_artefacts_block, render_components_block, render_config_reps_block, render_docs_block, render_entry_points_block, render_inventory_block, render_language_block, render_manifests_block, render_modules_block` at source line 19: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.models import CVE, AppProfile, ContextPackage, Control` at source line 31: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.rules.repo_kinds import BASELINES, STRIDE_BY_KIND, repo_kind` at source line 32: `source_detail/vvaharness/rules/repo_kinds.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s2/prompts.py.sudo.md). Exact strings in the evidence asset support this conversion.
