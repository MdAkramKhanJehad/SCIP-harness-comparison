# vvaharness/pipeline/stages/s2/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s2/__init__.py.evidence.json`. SHA-256: `6588bdc580de5f7f56360b1d771b253b9f983459c829fd7f16557db8e2107e0d`.

```sudo
// Source: vvaharness/pipeline/stages/s2/__init__.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/__init__.py:24-33
In source order: Resolve source import from langchain.agents.middleware import TodoListMiddleware; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS, refusal_resend_allowed, validate_detection_tools; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/__init__.py:34-65
In source order: Resolve source import from vvaharness.backends.llm.registry import resolve; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.build import graph_is_degenerate; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence import ThreatEvidence, _cap_int, gather, render_api_artefacts_block, render_components_block, render_config_reps_block, render_docs_block, render_entry_points_block, render_inventory_block, render_language_block, render_manifests_block, render_modules_block; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import CVE, AppProfile, ContextPackage, Control, Threat, ThreatModel, _cap_assets, _cap_boundaries, _cap_threats; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/__init__.py:66-74
In source order: Resolve source import from vvaharness.pipeline.stages.s2_planning import PLAN_SYSTEM_PROMPT as S2_PLAN_SYSTEM_PROMPT; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s2_planning import PLAN_TOOL_DESCRIPTION as S2_PLAN_TOOL_DESCRIPTION; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.repo_kinds import BASELINES, STRIDE_BY_KIND, repo_kind; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import resolve_inventory_path; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/__init__.py:75-79
In source order: Resolve source import from vvaharness.skills import inject_skills; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/__init__.py:80-93
In source order: Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import dispatch_or_retry_unforced; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Resolve source import from vvaharness.pipeline.stages.s2.baseline import _BASELINE_EVIDENCE_RX, _baseline_audit, _category_covered_elsewhere, _category_terms, _required_baselines; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/__init__.py:94-121
In source order: Resolve source import from vvaharness.pipeline.stages.s2.outcomes import _finalize_threats, _parse_threat_model, _warn_output_caps; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s2.prompts import SYSTEM, _AGENTIC_SYSTEM_LINE, _GRAPH_TOOLS_SYSTEM_LINE, _baseline_block, _build_user_prompt, _repair_json_prompt; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.replay import RecordTranscript, Transcript, replay_prompt, run_with_deadline; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s2.session import _DISPATCH_TAG, _WARNED_DEGENERATE_GRAPH, _WARNED_NO_GRAPH_TOOLS, _graph_tool_route_ok, _retry_if_hollow, _threatmodel_call; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s2/__init__.py:123-124
In source order: Evaluate once ['RecordTranscript', 'SYSTEM', 'Transcript', 'gather', 'replay_prompt', 'run', 'run_with_deadline']; assign in source target order to __all__.
// Source: vvaharness/pipeline/stages/s2/__init__.py:127-272
// Source signature: run(repo_root: str, repo_name: str, cfg, known_cves: list[CVE], controls: list[Control], ctx: ContextPackage | None=None, app_profile: AppProfile | None=None) -> ThreatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(repo_root, repo_name, cfg, known_cves, controls, ctx, app_profile) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:131-133
  In source order: Evaluate once getattr(cfg, 'step2', None); assign in source target order to s2. Then Evaluate once getattr(cfg, '_scan_progress', None); assign in source target order to tracker. Then Evaluate log.info('s2/threatmodel: starting threat modeling for %s', repo_name); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:134-136
  if (the source predicate ctx is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:135-136
    In source order: Evaluate log.debug('s2/threatmodel: context has_ast_view=%s files=%d', hasattr(ctx, 'ast_context_view'), len(getattr(ctx, 'all_files', []) or [])); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:137-141
  In source order: Evaluate once gather(repo_root, cfg, ctx); assign in source target order to ev. Then Evaluate once console.counts('s2', 'evidence', files=ev.file_count, modules=len(ev.modules), entry_points=len(ev.entry_points), config_reps=len(ev.config_reps), api_artefacts=len(ev.api_artefacts), docs=len(ev.docs), manifests=len(ev.manifests)); assign in source target order to note.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:142-143
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:143-143
    In source order: Evaluate tracker.stage_note('s2', source_template_143_33); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:144-150
  In source order: Evaluate console.write(source_template_144_18); retain side effects and discard the expression result. Then Evaluate once getattr(s2, 'baseline', 'auto'); assign in source target order to baseline_mode. Then Evaluate once _baseline_block(ev, ctx, baseline_mode); assign in source target order to (kinds, baseline). Then Evaluate COUNTERS.note('s2_repo_kinds', ','.join(sorted(kinds))); retain side effects and discard the expression result. Then Evaluate console.write(source_template_150_18); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:152-154
  In source order: Evaluate once _build_user_prompt(repo_name, ev, known_cves, controls, app_profile=app_profile, baseline_block=baseline); assign in source target order to user.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:155-156
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:156-156
    In source order: Evaluate tracker.stage_note('s2', 'threat-model LLM request started'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:158-158
  In source order: Evaluate once getattr(s2, 'effort', None) or None; assign in source target order to effort.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:159-176
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:163-170
    In source order: Evaluate once dispatch_or_retry_unforced(lambda *, drop_thinking: _threatmodel_call(user, cfg, repo_root, ctx, drop_thinking=drop_thinking, require_tool_call=ev.file_count > 0), repo_name, stage='s2', effort=_deepagents.droppable_effort(cfg.models.threatmodel, effort, agentic=True), may_retry=lambda: bool(getattr(s2, 'empty_retry', True)), resend_refusal=refusal_resend_allowed(cfg, cfg.models.threatmodel)); assign in source target order to raw.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:171-176
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:174-175
    In source order: Evaluate log.error(Event.S2_CALL_FAILED, detail=redact(str(e))); retain side effects and discard the expression result. Then Evaluate _errlog.log('s2', repo_name, e, reason='threat_model_call_failed'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s2/__init__.py:176-176
    Raise the currently handled exception.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:177-178
  if (the source predicate tracker is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:178-178
    In source order: Evaluate tracker.stage_note('s2', 'threat-model LLM response received'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:180-215
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:181-181
    In source order: Evaluate once _parse_threat_model(raw); assign in source target order to tm.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:182-215
  On the first matching source exception Exception as parse_err, in handler order {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:184-188
    In source order: Evaluate console.write(source_template_184_22); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s2_parse_repair_attempted'); retain side effects and discard the expression result. Then Evaluate once None; assign in source target order to repaired.
    // Source: vvaharness/pipeline/stages/s2/__init__.py:189-213
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s2/__init__.py:191-201
      In source order: Evaluate once _deepagents.dispatch_prompt(_repair_json_prompt(raw, parse_err), model=cfg.models.threatmodel, cfg=cfg, cwd=repo_root, system_prompt=SYSTEM, max_tokens=getattr(s2, 'max_tokens', 64000), timeout=_cap_int(s2, 'timeout', 1800), tag='s2 threatmodel json-repair'); assign in source target order to repaired. Then Evaluate once _parse_threat_model(repaired); assign in source target order to tm.
    }
    // Source: vvaharness/pipeline/stages/s2/__init__.py:202-213
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/pipeline/stages/s2/__init__.py:204-212
      In source order: Evaluate log.error(Event.S2_RESPONSE_UNPARSEABLE, detail=str(e)); retain side effects and discard the expression result. Then Evaluate _errlog.log('s2', repo_name, e, reason='threat_model_parse_failed', raw_head=redact((repaired if repaired is not None else raw) or '')[:500], note='s2 JSON extraction or model validation failed after one repair retry; s3–s8 will receive no threat context'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s2/__init__.py:213-213
      Raise the currently handled exception.
    }
    // Source: vvaharness/pipeline/stages/s2/__init__.py:214-215
    In source order: Evaluate COUNTERS.bump('s2_parse_repair_recovered'); retain side effects and discard the expression result. Then Evaluate log.warning(Event.S2_PARSE_REPAIR_RECOVERED); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:217-219
  In source order: Evaluate _finalize_threats(tm, ctx); retain side effects and discard the expression result. Then Evaluate once _retry_if_hollow(tm, ev, user, cfg, repo_root, ctx); assign in source target order to tm.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:221-230
  if (the source predicate not tm.threats is truthy) {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:223-227
    In source order: Evaluate _errlog.log('s2', 'threatmodel', "zero threats — s3's per-threat annotator has nothing to annotate; the run proceeds with no threat-derived targeting"); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s2/__init__.py:228-230
    if (the source predicate ev.file_count > 0 is truthy) {
      // Source: vvaharness/pipeline/stages/s2/__init__.py:230-230
      In source order: Evaluate COUNTERS.bump('s2_degraded'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:233-238
  In source order: Evaluate once _baseline_audit(tm, kinds); assign in source target order to undisposed. Then Evaluate once _cap_int(s2, 'max_threats', 50); assign in source target order to max_threats. Then Evaluate once _cap_int(s2, 'max_assets', 40); assign in source target order to max_assets. Then Evaluate once _cap_int(s2, 'max_trust_boundaries', 60); assign in source target order to max_boundaries. Then Evaluate once (len(tm.threats), len(tm.assets), len(tm.trust_boundaries)); assign in source target order to raw_counts.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:239-245
  In source order: Evaluate once _cap_threats(tm, max_threats); assign in source target order to tm. Then Evaluate once _cap_assets(tm, max_assets); assign in source target order to tm. Then Evaluate once _cap_boundaries(tm, max_boundaries); assign in source target order to tm. Then Evaluate _warn_output_caps(raw_counts, tm, (max_threats, max_assets, max_boundaries)); retain side effects and discard the expression result. Then Evaluate COUNTERS.note('s2_baseline_undisposed', ','.join(sorted(undisposed))); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:246-266
  if (the source predicate undisposed is truthy) {
    // Source: vvaharness/pipeline/stages/s2/__init__.py:248-252
    In source order: Evaluate once _required_baselines(kinds) - set(undisposed); assign in source target order to disposed. Then Evaluate once all((_category_covered_elsewhere(bid, tm.threats, disposed=disposed) for bid in undisposed)); assign in source target order to all_covered_elsewhere.
    // Source: vvaharness/pipeline/stages/s2/__init__.py:253-263
    if (the source predicate all_covered_elsewhere is truthy) {
      // Source: vvaharness/pipeline/stages/s2/__init__.py:254-258
      In source order: Evaluate _errlog.log('s2', repo_name, 'baseline items undisposed', reason='baseline_items_undisposed', baseline_ids=sorted(undisposed), recovered=True); retain side effects and discard the expression result. Then Evaluate COUNTERS.bump('s2_baseline_undisposed_recovered'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/pipeline/stages/s2/__init__.py:261-263
      In source order: Evaluate _errlog.log('s2', repo_name, 'baseline items undisposed', reason='baseline_items_undisposed', baseline_ids=sorted(undisposed)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s2/__init__.py:264-266
    In source order: Evaluate log.warning(Event.S2_BASELINE_UNDISPOSED, count=len(undisposed), baseline_ids=sorted(undisposed), covered_elsewhere=all_covered_elsewhere); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s2/__init__.py:268-271
  In source order: Evaluate console.counts('s2', 'done', assets=len(tm.assets), trust_boundaries=len(tm.trust_boundaries), threats=len(tm.threats)); retain side effects and discard the expression result. Then Evaluate log.info('s2/threatmodel: threat model complete - assets=%d boundaries=%d threats=%d', len(tm.assets), len(tm.trust_boundaries), len(tm.threats)); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s2/__init__.py:272-272
  End this invocation with tm.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.evidence_gate import EvidenceGate` at source line 26: `source_detail/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tool_budget import ToolCallBudget` at source line 27: `source_detail/vvaharness/backends/harness/deepagents/tool_budget.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 28: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 28: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.models import RESPONSE_MODEL_VIAS, refusal_resend_allowed, validate_detection_tools` at source line 29: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve` at source line 34: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.codegraph.build import graph_is_degenerate` at source line 35: `source_detail/vvaharness/codegraph/build.py.sudo.md`.
- `from vvaharness.codegraph.tools import GRAPH_TOOL_NAMES, build_graph_tool_builder, graph_tool_names` at source line 36: `source_detail/vvaharness/codegraph/tools.py.sudo.md`.
- `from vvaharness.evidence import ThreatEvidence, _cap_int, gather, render_api_artefacts_block, render_components_block, render_config_reps_block, render_docs_block, render_entry_points_block, render_inventory_block, render_language_block, render_manifests_block, render_modules_block` at source line 41: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.evidence import ThreatEvidence, _cap_int, gather, render_api_artefacts_block, render_components_block, render_config_reps_block, render_docs_block, render_entry_points_block, render_inventory_block, render_language_block, render_manifests_block, render_modules_block` at source line 41: `source_detail/vvaharness/evidence/gather.py.sudo.md`.
- `from vvaharness.models import CVE, AppProfile, ContextPackage, Control, Threat, ThreatModel, _cap_assets, _cap_boundaries, _cap_threats` at source line 55: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2_planning import PLAN_SYSTEM_PROMPT as S2_PLAN_SYSTEM_PROMPT` at source line 66: `source_detail/vvaharness/pipeline/stages/s2_planning.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2_planning import PLAN_TOOL_DESCRIPTION as S2_PLAN_TOOL_DESCRIPTION` at source line 69: `source_detail/vvaharness/pipeline/stages/s2_planning.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 72: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.rules.repo_kinds import BASELINES, STRIDE_BY_KIND, repo_kind` at source line 73: `source_detail/vvaharness/rules/repo_kinds.py.sudo.md`.
- `from vvaharness.scope import resolve_inventory_path` at source line 74: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.skills import inject_skills` at source line 75: `source_detail/vvaharness/skills/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 76: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 76: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 77: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 77: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 78: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 79: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 80: `source_detail/vvaharness/util/json_extract.py.sudo.md`.
- `from vvaharness.util.response_quality import dispatch_or_retry_unforced` at source line 81: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.warn_once import warn_once` at source line 82: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2.baseline import _BASELINE_EVIDENCE_RX, _baseline_audit, _category_covered_elsewhere, _category_terms, _required_baselines` at source line 87: `source_detail/vvaharness/pipeline/stages/s2/baseline.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2.outcomes import _finalize_threats, _parse_threat_model, _warn_output_caps` at source line 94: `source_detail/vvaharness/pipeline/stages/s2/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2.prompts import SYSTEM, _AGENTIC_SYSTEM_LINE, _GRAPH_TOOLS_SYSTEM_LINE, _baseline_block, _build_user_prompt, _repair_json_prompt` at source line 99: `source_detail/vvaharness/pipeline/stages/s2/prompts.py.sudo.md`.
- `from vvaharness.pipeline.stages.replay import RecordTranscript, Transcript, replay_prompt, run_with_deadline` at source line 107: `source_detail/vvaharness/pipeline/stages/replay.py.sudo.md`.
- `from vvaharness.pipeline.stages.s2.session import _DISPATCH_TAG, _WARNED_DEGENERATE_GRAPH, _WARNED_NO_GRAPH_TOOLS, _graph_tool_route_ok, _retry_if_hollow, _threatmodel_call` at source line 113: `source_detail/vvaharness/pipeline/stages/s2/session.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 121: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s2/__init__.py.sudo.md). Exact strings in the evidence asset support this conversion.
