# vvaharness/pipeline/stages/s4/prompts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s4/prompts.py.evidence.json`. SHA-256: `ee59a851ac1608d258b7fdaa4e066a3043955a2280779c825251065a53b9e803`.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, graph_tool_names; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.work import InvestigationUnit; preserve alias and import-time effects. Then Evaluate once source_literal_23_4; assign in source target order to _CWE_CLAUSE.
// Source: vvaharness/pipeline/stages/s4/prompts.py:31-77
In source order: Evaluate once source_literal_32_4; assign in source target order to _BREADTH_CLAUSE. Then Evaluate once source_literal_42_4; assign in source target order to _CWE_PAIRS. Then Evaluate once source_literal_62_4; assign in source target order to _CWE_TOOL_DUTY. Then Evaluate once 'A plugin has also registered these graph tools, and they are as callable as the six above: '; assign in source target order to _PLUGIN_TOOL_DUTY_HEAD. Then Evaluate once source_literal_74_4; assign in source target order to _PLUGIN_TOOL_DUTY_TAIL.
// Source: vvaharness/pipeline/stages/s4/prompts.py:79-134
In source order: Evaluate once source_literal_80_4; assign in source target order to _GRAPH_TOOL_DUTY. Then Evaluate once source_literal_93_4; assign in source target order to _VERDICT_CLAUSE. Then Evaluate once source_literal_105_4; assign in source target order to _SCOPE_CLAUSE. Then Evaluate once source_literal_116_4; assign in source target order to _FP_DISCIPLINE. Then Evaluate once source_literal_123_4; assign in source target order to _READ_COMPLETELY_CLAUSE.
// Source: vvaharness/pipeline/stages/s4/prompts.py:136-192
In source order: Evaluate once source_literal_137_4; assign in source target order to _ABSENCE_METHOD. Then Evaluate once source_literal_159_4; assign in source target order to _SKILL_DUTY. Then Evaluate once source_literal_174_4; assign in source target order to _SURFACE_INLINED. Then Evaluate once source_literal_181_4; assign in source target order to _SURFACE_TO_READ. Then Evaluate once source_literal_189_4; assign in source target order to _BUDGETED_REACHABILITY_GRAPH.
// Source: vvaharness/pipeline/stages/s4/prompts.py:194-198
In source order: Evaluate once source_literal_195_4; assign in source target order to _BUDGETED_REACHABILITY_NO_GRAPH.
// Source: vvaharness/pipeline/stages/s4/prompts.py:201-225
// Source signature: _budgeted_sweep(budget: int, inlined: bool, graph: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _budgeted_sweep(budget, inlined, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:202-203
  In source order: Retain source documentation literal source_literal_202_4; it is not a model call. Then Evaluate once max(0, budget - 1); assign in source target order to lookups.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:204-225
  End this invocation with source_template_205_4 + (source_literal_208_7 if inlined else source_literal_210_7) + source_literal_212_6 + (_BUDGETED_REACHABILITY_GRAPH if graph else _BUDGETED_REACHABILITY_NO_GRAPH) + source_literal_214_6.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:228-238
In source order: Evaluate once source_literal_229_4; assign in source target order to _REACHABILITY_GRAPH. Then Evaluate once source_literal_235_4; assign in source target order to _REACHABILITY_NO_GRAPH.
// Source: vvaharness/pipeline/stages/s4/prompts.py:241-260
// Source signature: _breadth_sweep(inlined: bool, graph: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _breadth_sweep(inlined, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:242-242
  In source order: Retain source documentation literal source_literal_242_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:243-260
  End this invocation with source_literal_244_4 + (_SURFACE_INLINED if inlined else _SURFACE_TO_READ) + (_REACHABILITY_GRAPH if graph else _REACHABILITY_NO_GRAPH) + source_literal_248_6.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:263-296
In source order: Evaluate once source_literal_264_4; assign in source target order to _SHELL_DUTY. Then Evaluate once source_literal_287_4; assign in source target order to _SHELL_GRAPH_HANDOFF. Then Evaluate once source_literal_293_4; assign in source target order to _SHELL_NOTES.
// Source: vvaharness/pipeline/stages/s4/prompts.py:299-301
// Source signature: _shell_duty(graph: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shell_duty(graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:300-300
  In source order: Retain source documentation literal source_literal_300_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:301-301
  End this invocation with _SHELL_DUTY + (_SHELL_GRAPH_HANDOFF if graph else '') + _SHELL_NOTES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:304-308
// Source signature: _sweep(budget: int, inlined: bool, graph: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sweep(budget, inlined, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:305-305
  In source order: Retain source documentation literal source_literal_305_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:306-307
  if (the source predicate budget > 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:307-307
    End this invocation with _budgeted_sweep(budget, inlined, graph).
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:308-308
  End this invocation with _breadth_sweep(inlined, graph).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:311-315
// Source signature: _closing(budget: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _closing(budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:312-312
  In source order: Retain source documentation literal source_literal_312_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:313-314
  if (the source predicate budget > 0 is truthy) {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:314-314
    End this invocation with 'Spend your lookups, then report the outcome object.'.
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:315-315
  End this invocation with 'Work your plan, make all four passes, then report the outcome object.'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:318-378
In source order: Evaluate once source_literal_319_4; assign in source target order to _OUTPUT_EXAMPLE. Then Evaluate once 'You confirm or refute ONE specific threat claim against the code that implements it.'; assign in source target order to _ROLE. Then Evaluate once source_literal_351_4; assign in source target order to _PLAN_HEAD. Then Evaluate once source_literal_367_4; assign in source target order to _PLAN_REACHABILITY_GRAPH. Then Evaluate once source_literal_374_4; assign in source target order to _PLAN_REACHABILITY_NO_GRAPH.
// Source: vvaharness/pipeline/stages/s4/prompts.py:380-396
In source order: Evaluate once source_literal_381_4; assign in source target order to _PLAN_TAIL.
// Source: vvaharness/pipeline/stages/s4/prompts.py:399-401
// Source signature: build_plan_system_prompt(graph: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_plan_system_prompt(graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:400-400
  In source order: Retain source documentation literal source_literal_400_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:401-401
  End this invocation with _PLAN_HEAD + (_PLAN_REACHABILITY_GRAPH if graph else _PLAN_REACHABILITY_NO_GRAPH) + _PLAN_TAIL.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:404-412
In source order: Evaluate once source_literal_405_4; assign in source target order to PLAN_TOOL_DESCRIPTION.
// Source: vvaharness/pipeline/stages/s4/prompts.py:415-420
// Source signature: _plugin_tool_duty() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _plugin_tool_duty() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:416-417
  In source order: Retain source documentation literal source_literal_416_4; it is not a model call. Then Evaluate once tuple((n for n in graph_tool_names() if n not in GRAPH_TOOL_NAMES)); assign in source target order to extra.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:418-419
  if (the source predicate not extra is truthy) {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:419-419
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:420-420
  End this invocation with _PLUGIN_TOOL_DUTY_HEAD + ', '.join((source_template_420_46 for n in extra)) + _PLUGIN_TOOL_DUTY_TAIL.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:423-444
// Source signature: build_system_prompt(shell: bool=False, graph: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_system_prompt(shell, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:424-424
  In source order: Retain source documentation literal source_literal_424_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:426-444
  End this invocation with source_literal_426_11.join([c for c in (_ROLE, _SCOPE_CLAUSE, _VERDICT_CLAUSE, _BREADTH_CLAUSE, _CWE_CLAUSE, _CWE_PAIRS, _CWE_TOOL_DUTY, _GRAPH_TOOL_DUTY if graph else '', _plugin_tool_duty() if graph else '', _shell_duty(graph) if shell else '', _ABSENCE_METHOD, _SKILL_DUTY, _READ_COMPLETELY_CLAUSE, _FP_DISCIPLINE, _OUTPUT_EXAMPLE) if c]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:447-452
// Source signature: _sink_lines(unit: InvestigationUnit) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sink_lines(unit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:448-451
  In source order: Evaluate once [source_template_449_8 for s in unit.sinks]; assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:452-452
  End this invocation with source_literal_452_11 + source_literal_452_47.join(lines) + source_literal_452_66.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:455-460
// Source signature: _entry_point_lines(unit: InvestigationUnit) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _entry_point_lines(unit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:456-456
  In source order: Evaluate once []; assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:457-459
  for each ep in unit.entry_points {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:458-459
    In source order: Evaluate once '[unauth]' if ep.reachable_from_unauth else '[auth]'; assign in source target order to auth_tag. Then Evaluate lines.append(source_template_459_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:460-460
  End this invocation with source_literal_460_11 + source_literal_460_33.join(lines) + source_literal_460_52.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:463-465
// Source signature: _cve_lines(unit: InvestigationUnit) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cve_lines(unit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:464-464
  In source order: Evaluate once [source_template_464_13 for cve in unit.related_cves]; assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:465-465
  End this invocation with source_literal_465_11 + source_literal_465_60.join(lines) + source_literal_465_79.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:468-475
// Source signature: _community_lines(unit: InvestigationUnit, graph: bool) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _community_lines(unit, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:469-474
  In source order: Retain source documentation literal source_literal_469_4; it is not a model call. Then Evaluate once [source_template_471_13 for c in unit.communities]; assign in source target order to lines. Then Evaluate once source_literal_472_13 if graph else 'CALL-GRAPH NEIGHBOURHOODS'; assign in source target order to label.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:475-475
  End this invocation with source_template_475_11 + source_literal_475_29.join(lines) + source_literal_475_48.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:478-484
// Source signature: _cwe_lines(unit: InvestigationUnit) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cwe_lines(unit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:479-479
  In source order: Retain source documentation literal source_literal_479_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:481-484
  End this invocation with source_template_481_12.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:487-490
// Source signature: _file_list(unit: InvestigationUnit) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _file_list(unit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:488-489
  In source order: Retain source documentation literal source_literal_488_4; it is not a model call. Then Evaluate once source_literal_489_17.join((source_template_489_27 for f in unit.files)); assign in source target order to file_lines.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:490-490
  End this invocation with source_template_490_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:493-500
// Source signature: _source_section(unit: InvestigationUnit, code: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _source_section(unit, code) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:494-495
  if (the source predicate code is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:495-495
    End this invocation with source_template_495_15.
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:496-500
  End this invocation with source_template_497_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:503-525
// Source signature: _unit_block(unit: InvestigationUnit, code: str | None, *, files_only: bool=False, graph: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unit_block(unit, code, files_only, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:505-506
  In source order: Retain source documentation literal source_literal_505_4; it is not a model call. Then Evaluate once []; assign in source target order to extra_lines.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:507-508
  if (the source predicate unit.controls is truthy) {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:508-508
    In source order: Evaluate extra_lines.append(source_template_508_27); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:509-510
  if (the source predicate unit.evidence is truthy) {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:510-510
    In source order: Evaluate extra_lines.append(source_template_510_27); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:511-516
  In source order: Evaluate once source_literal_511_19 + source_literal_511_26.join(extra_lines) + source_literal_511_51 if extra_lines else ''; assign in source target order to extra_block. Then Evaluate once _sink_lines(unit) if unit.sinks else ''; assign in source target order to sinks_block. Then Evaluate once _entry_point_lines(unit) if unit.entry_points else ''; assign in source target order to eps_block. Then Evaluate once _cve_lines(unit) if unit.related_cves else ''; assign in source target order to cve_block. Then Evaluate once _community_lines(unit, graph) if unit.communities else ''; assign in source target order to comm_block.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:517-517
  In source order: Evaluate once _cwe_lines(unit) if unit.cwes else ''; assign in source target order to cwe_block.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:519-525
  End this invocation with source_template_519_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:528-533
// Source signature: build_initial_prompt(unit: InvestigationUnit, code: str | None, call_budget: int=0, graph: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_initial_prompt(unit, code, call_budget, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:530-530
  In source order: Retain source documentation literal source_literal_530_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:531-533
  End this invocation with source_template_531_12.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:536-556
// Source signature: _batch_duty(units: list[InvestigationUnit]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _batch_duty(units) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:537-538
  In source order: Retain source documentation literal source_literal_537_4; it is not a model call. Then Evaluate once ', '.join((u.id for u in units)); assign in source target order to ids.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:539-556
  End this invocation with source_template_540_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:559-568
// Source signature: _shared_code_section(code: str | None, n_files: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shared_code_section(code, n_files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:560-560
  In source order: Retain source documentation literal source_literal_560_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:561-563
  if (the source predicate code is None is truthy) {
    // Source: vvaharness/pipeline/stages/s4/prompts.py:562-563
    End this invocation with source_literal_562_16.
  }
  // Source: vvaharness/pipeline/stages/s4/prompts.py:564-568
  End this invocation with source_template_565_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s4/prompts.py:571-578
// Source signature: build_batch_prompt(units: list[InvestigationUnit], code: str | None, n_files: int, call_budget: int=0, graph: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_batch_prompt(units, code, n_files, call_budget, graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:573-575
  In source order: Retain source documentation literal source_literal_573_4; it is not a model call. Then Evaluate once source_literal_574_13.join((_unit_block(u, None, files_only=True, graph=graph) for u in units)); assign in source target order to blocks.
  // Source: vvaharness/pipeline/stages/s4/prompts.py:576-578
  End this invocation with source_template_576_12.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, graph_tool_names` at source line 18: `source_detail/vvaharness/codegraph/tools.py.sudo.md`.
- `from vvaharness.models.scan.work import InvestigationUnit` at source line 19: `source_detail/vvaharness/models/scan/work.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s4/prompts.py.sudo.md). Exact strings in the evidence asset support this conversion.
