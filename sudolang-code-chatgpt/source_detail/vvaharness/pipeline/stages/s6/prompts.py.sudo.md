# vvaharness/pipeline/stages/s6/prompts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s6/prompts.py.evidence.json`. SHA-256: `7215c310786bb5948cb95216aea651cc2f9fc5f303674107dcb63e42546bba4b`.

```sudo
// Source: vvaharness/pipeline/stages/s6/prompts.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import fnmatch; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._render import _one_line; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s6/prompts.py:23-123
In source order: Evaluate once source_literal_24_4; assign in source target order to _ROLE. Then Evaluate once source_literal_29_18; assign in source target order to EXCLUSION_RULES. Then Evaluate once source_literal_85_4; assign in source target order to _VERDICT_CLAUSE. Then Evaluate once source_literal_101_4; assign in source target order to _CONFIDENCE_CLAUSE. Then Evaluate once source_literal_109_4; assign in source target order to _METHOD.
// Source: vvaharness/pipeline/stages/s6/prompts.py:125-181
In source order: Evaluate once source_literal_126_4; assign in source target order to _GRAPH_DUTY. Then Evaluate once source_literal_136_4; assign in source target order to _CORRECTION_DUTY. Then Evaluate once source_literal_152_4; assign in source target order to _REFRAME_DUTY. Then Evaluate once source_literal_168_4; assign in source target order to _TRAIT_STAMP_DUTY. Then Evaluate once source_literal_175_4; assign in source target order to _REPEAT_DUTY.
// Source: vvaharness/pipeline/stages/s6/prompts.py:183-229
In source order: Evaluate once source_literal_184_4; assign in source target order to _EXTRA_DUTY. Then Evaluate once source_literal_193_4; assign in source target order to _CVSS_DUTY. Then Evaluate once source_literal_206_4; assign in source target order to _OUTPUT_EXAMPLE.
// Source: vvaharness/pipeline/stages/s6/prompts.py:232-250
// Source signature: build_system_prompt(graph: bool=False, trait_stamps: bool=True, reframe: bool=False) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_system_prompt(graph, trait_stamps, reframe) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:234-234
  In source order: Retain source documentation literal source_literal_234_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:236-250
  End this invocation with source_literal_236_11.join((c for c in (_ROLE, _VERDICT_CLAUSE, _CONFIDENCE_CLAUSE, _METHOD, _GRAPH_DUTY if graph else '', _CORRECTION_DUTY, _REFRAME_DUTY if reframe else '', _REPEAT_DUTY, _EXTRA_DUTY, _TRAIT_STAMP_DUTY if trait_stamps else '', EXCLUSION_RULES, _CVSS_DUTY, _OUTPUT_EXAMPLE) if c)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:253-262
// Source signature: _entry_point_lines(ctx: ContextPackage, limit: int=25) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _entry_point_lines(ctx, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:254-257
  In source order: Retain source documentation literal source_literal_254_4; it is not a model call. Then Evaluate once [source_template_255_11 for e in ctx.entry_points]; assign in source target order to eps.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:258-259
  if (the source predicate not eps is truthy) {
    // Source: vvaharness/pipeline/stages/s6/prompts.py:259-259
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s6/prompts.py:260-260
  In source order: Evaluate once source_template_260_11 if len(eps) > limit else ''; assign in source target order to more.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:261-262
  End this invocation with source_literal_261_12 + source_literal_262_27.join(eps[:limit]) + more.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:265-271
// Source signature: build_shared_context(ctx: ContextPackage) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_shared_context(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:266-268
  In source order: Retain source documentation literal source_literal_266_4; it is not a model call. Then Evaluate once [_entry_point_lines(ctx)]; assign in source target order to blocks.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:269-270
  if (the source predicate ctx.notes is truthy) {
    // Source: vvaharness/pipeline/stages/s6/prompts.py:270-270
    In source order: Evaluate blocks.append(source_template_270_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/prompts.py:271-271
  End this invocation with source_literal_271_11.join((b for b in blocks if b)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:274-282
// Source signature: _controls_for(file: str, ctx: ContextPackage) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _controls_for(file, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:275-276
  In source order: Retain source documentation literal source_literal_275_4; it is not a model call. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:277-281
  for each c in ctx.design_controls {
    // Source: vvaharness/pipeline/stages/s6/prompts.py:278-279
    if (the source predicate c.protects and (not any((fnmatch.fnmatch(file, g) for g in c.protects))) is truthy) {
      // Source: vvaharness/pipeline/stages/s6/prompts.py:279-279
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s6/prompts.py:280-281
    In source order: Evaluate once source_template_280_15 if c.notes else ''; assign in source target order to note. Then Evaluate out.append(source_template_281_19); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s6/prompts.py:282-282
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:285-296
// Source signature: _controls_block(files: list[str], ctx: ContextPackage) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _controls_block(files, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:286-287
  In source order: Retain source documentation literal source_literal_286_4; it is not a model call. Then For lines, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s6/prompts.py:288-291
  for each file in files {
    // Source: vvaharness/pipeline/stages/s6/prompts.py:289-291
    for each line in _controls_for(file, ctx) {
      // Source: vvaharness/pipeline/stages/s6/prompts.py:290-291
      if (the source predicate line not in lines is truthy) {
        // Source: vvaharness/pipeline/stages/s6/prompts.py:291-291
        In source order: Evaluate lines.append(line); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s6/prompts.py:292-293
  if (the source predicate not lines is truthy) {
    // Source: vvaharness/pipeline/stages/s6/prompts.py:293-293
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s6/prompts.py:294-296
  End this invocation with source_literal_294_12 + source_literal_294_60.join(lines) + source_literal_295_14.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:299-321
// Source signature: _finding_block(fid: str, f: Finding) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _finding_block(fid, f) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:300-305
  In source order: Retain source documentation literal source_literal_300_4; it is not a model call. Then Resolve source import from vvaharness.pipeline.stages.s4_deepdive import _redact_source; preserve alias and import-time effects. Then Evaluate once source_literal_303_11.join((source_template_303_21 for p in f.preconditions)) or '  (none listed)'; assign in source target order to pre. Then Evaluate once (f.code_snippet or '').strip(); assign in source target order to snippet.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:306-308
  if (the source predicate snippet is truthy) {
    // Source: vvaharness/pipeline/stages/s6/prompts.py:308-308
    In source order: Evaluate once _redact_source(snippet, f.file, stage='s6'); assign in source target order to snippet.
  }
  // Source: vvaharness/pipeline/stages/s6/prompts.py:309-310
  In source order: Evaluate once source_template_309_21 if snippet else ''; assign in source target order to snippet_block.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:311-321
  End this invocation with source_template_311_12.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:325-346
// Source signature: _batch_duty(ids: list[str], files: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _batch_duty(ids, files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:326-327
  In source order: Retain source documentation literal source_literal_326_4; it is not a model call. Then Evaluate once files[0] if len(files) == 1 else source_template_327_45; assign in source target order to where.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:328-346
  End this invocation with source_template_329_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:349-359
// Source signature: _source_section(code: str | None, n_files: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _source_section(code, n_files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:350-350
  In source order: Retain source documentation literal source_literal_350_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:351-353
  if (the source predicate code is None is truthy) {
    // Source: vvaharness/pipeline/stages/s6/prompts.py:352-353
    End this invocation with "No source is inlined. Read each cited file — the snippets above are the scanner's copy and may be stale or mis-located.".
  }
  // Source: vvaharness/pipeline/stages/s6/prompts.py:354-359
  End this invocation with source_template_354_12.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:362-372
// Source signature: build_verify_prompt(items: list[tuple[str, Finding]], ctx: ContextPackage, code: str | None=None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_verify_prompt(items, ctx, code) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:364-368
  In source order: Retain source documentation literal source_literal_364_4; it is not a model call. Then Evaluate once [fid for fid, _ in items]; assign in source target order to ids. Then Evaluate once list(dict.fromkeys((f.file for _, f in items))); assign in source target order to files. Then Evaluate once source_literal_367_13.join((_finding_block(fid, f) for fid, f in items)); assign in source target order to blocks. Then Evaluate once _controls_block(files, ctx); assign in source target order to controls.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:369-371
  In source order: Evaluate once [_batch_duty(ids, files) if len(items) > 1 else '', blocks, controls, _source_section(code, len(files)), 'Verify each finding, then report one outcome per finding id above.']; assign in source target order to parts.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:372-372
  End this invocation with source_literal_372_11.join((p for p in parts if p)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s6/prompts.py:375-384
// Source signature: repair_prompt(raw: str, ids: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn repair_prompt(raw, ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:376-376
  In source order: Retain source documentation literal source_literal_376_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s6/prompts.py:377-384
  End this invocation with source_template_378_8.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import ContextPackage, Finding` at source line 20: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.scan._render import _one_line` at source line 21: `source_detail/vvaharness/models/scan/_render.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4_deepdive import _redact_source` at source line 301: `source_detail/vvaharness/pipeline/stages/s4_deepdive.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s6/prompts.py.sudo.md). Exact strings in the evidence asset support this conversion.
