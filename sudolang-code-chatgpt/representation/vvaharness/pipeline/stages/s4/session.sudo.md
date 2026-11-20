# s4/session.py — investigation sessions

Executable setup and reply handling. The generic dispatch/replay/response-quality
implementations are expanded in source_detail/; the arguments and call relationships
are preserved here. Exposing a tool does not imply a call to it.

```sudo
// Source: vvaharness/pipeline/stages/s4/session.py:83-153
fn deepdive_tools(cfg) {
  validate_detection_tools(knob(cfg,"step4.allowed_tools",["Read","Glob","Grep"]),
    config_key="step4.allowed_tools", via=resolve(cfg.models.deepdive).via)
}
fn _budget(s4, key, names, counter) {
  limit=_cap_int(s4,key,6)
  if (limit<=0) { yield None } else { yield ToolCallBudget(names,limit,counter) }
}
fn _batch_limit(limit, members) { limit + max(0,members-1) }
fn _call_budget(s4, outcome, members=1, tag="") {
  limit=_cap_int(s4,"max_model_calls",0)
  if (limit<=0) { yield None }
  else { yield ModelCallBudget(limit=_batch_limit(limit,members), outcome_tools={outcome},
    counter="s4_model_call_budget_final_turn", raise_when_exhausted=true, stage=tag) }
}
fn _graph_tools_registered(ctx, cfg=None) { ctx.graph_handle != None && !graph_is_degenerate(ctx,cfg) }
fn _planner(s4, graph=true) {
  if (!s4.planning, default true) { yield None }
  else { yield TodoListMiddleware(system_prompt=build_plan_system_prompt(graph),
    tool_description=PLAN_TOOL_DESCRIPTION) }
}
fn _gate(s4, ctx, cfg=None, degenerate_stand_down_counted=None) {
  if (!(s4.planning default true) || !(s4.evidence_gate default true)) { yield None and end this call }
  declared=s4.require_graph, default true
  degenerate=declared && graph_is_degenerate(ctx,cfg)
  if (degenerate) {
    Warn once; bump evidence_gate_stood_down_degenerate_graph only if shared flag absent or false.
    Set shared flag true when supplied.
  }
  required = GRAPH_TOOL_NAMES if declared && !degenerate, else empty set
  yield EvidenceGate(max_rejections=_cap_int(s4,"evidence_gate_refusals",3),
    counter="s4_evidence_gate_rejected", required_tools=required)
}

// Source: vvaharness/pipeline/stages/s4/session.py:156-183
fn _tool_setup(ctx, s4, outcome="InvestigationOutcome", members=1, cfg=None,
    degenerate_stand_down_counted=None, tag="", graph=true) {
  builders=[build_graph_tool_builder(ctx)]; names=graph_tool_names()
  middleware=[_budget(s4,"graph_tool_budget",graph_tool_names(),"s4_graph_tool_budget_exhausted")]
  if (s4.cwe_tools, default true) {
    Append build_kb_tool_builder to builders; append KB_TOOL_NAMES to names.
    Append _budget(s4,"cwe_tool_budget",KB_TOOL_NAMES,"s4_cwe_tool_budget_exhausted") to middleware.
  }
  Append in order: _planner(s4,graph), _gate(s4,ctx,cfg,shared flag), _call_budget(s4,outcome,members,tag).
  yield [compose_tool_builders(builders), names, non-None middleware in that order]
  Tool-builder internals and route-specific registration are expanded in source_detail/.
}
fn _load_code(unit, repo_root, s4) {
  if (unit.size==UnitSize.LARGE || !(s4.inline_source default false)) { yield None }
  else { yield _load_files_full(unit.files,repo_root) }
}

// Source: vvaharness/pipeline/stages/s4/session.py:186-240
fn _repair_prompt(raw, unit_id) {
  Format exact repair string: request ONLY corrected InvestigationOutcome JSON,
    exact unit_id, preserve findings/facts, followed by original raw reply.
  This is a model request, not proof the repaired reply obeys it.
}
_REPLAY_EFFORT="low"
fn _deadline_seconds(cfg) { integer(knob(cfg,"step4.deadline",0) or 0) }
fn _session_timeout(cfg, effort) {
  deadline_bound(None,_deadline_seconds(cfg),effort,via=resolve(cfg.models.deepdive).via)
}
fn _deadline_bounded(call, replay, cfg, tag, session_id) {
  Call run_with_deadline(call,seconds=_deadline_seconds(cfg),stage=tag,effort="low").
  Only on CallTimeoutError, log and call resume_or_replay(session_id,replay,
    model=cfg.models.deepdive,cfg,instruction=S4_REPLAY_INSTRUCTION,stage="s4",tag,
    timeout=_cap_int(cfg.step4,"resume_timeout",60)).
}
fn _replay_call(prompt_text, transcript, cfg, repo_root, tag, response_model) {
  Bump s4_deadline_replay.
  Dispatch a tool-free replay_prompt(transcript,prompt_text,S4_REPLAY_INSTRUCTION,stage="s4")
    through _deepagents.dispatch_prompt with deepdive model, cfg, cwd=repo_root,
    graph_name="s4-deepdive", tag suffixed replay, effort="low", response_model,
    max_tokens=_cap_int(step4,"replay_max_tokens",16000),
    timeout=_cap_int(step4,"replay_timeout",60).
}

// Source: vvaharness/pipeline/stages/s4/session.py:243-337
fn _investigate_unit_once(unit, ctx, repo_root, cfg) {
  s4=cfg.step4; code=_load_code(unit,repo_root,s4)
  response_model=InvestigationOutcome if deepdive route in RESPONSE_MODEL_VIAS, else None
  degenerate_stand_down_counted=[false]; tag="s4 " + unit.id
  graph=_graph_tools_registered(ctx,cfg); effort=s4.effort or None; tools=deepdive_tools(cfg)
  Define nested _dispatch(drop_thinking):
    Rebuild _tool_setup per attempt, sharing only degenerate_stand_down_counted.
    initial=build_initial_prompt(unit,code,_cap_int(s4,"max_model_calls",0),graph)
    Create fresh Transcript; append RecordTranscript after other middleware.
    Within pinned_session("s4",unit.id), call _deadline_bounded with:
      primary callable invoking _agentic;
      replay callable invoking _replay_call(initial,transcript,...).
  Define nested _agentic to call _deepagents.dispatch_agentic with:
    initial, model=cfg.models.deepdive, cfg, cwd=repo_root,
    system_prompt=build_system_prompt(shell=bool(s4.bash default false),graph),
    graph_name="s4-deepdive", tag, tool_builder, fact_tools, response_model,
    allowed_tools=tools, parent_middleware=middleware,
    max_output_tokens=int(knob(cfg,"step4.max_tokens",64000)),
    cache_prefix=_build_shared_context_block(ctx) or None,
    skill_root=inject_skills(repo_root) if s4.skills default true, else None,
    effort=None when drop_thinking else effort,
    max_turns=_cap_int(s4,"max_turns",15),
    timeout=_session_timeout(cfg,None when drop_thinking else effort),
    allow_shell=bool(s4.bash default false), session_id.
  raw=dispatch_or_retry_unforced(_dispatch,unit.id,stage="s4",
    effort=_deepagents.droppable_effort(deepdive model,effort,agentic=true),
    resend_refusal=refusal_resend_allowed(cfg,deepdive model))
  [findings,by_unit]=reduce_outcomes([unit],{unit.id:raw},cfg,repo_root,inventory=set(ctx.all_files))
  if (by_unit[unit.id]=="failed") {
    Log recovered repair attempt; bump repair counter.
    repaired=_deepagents.dispatch_prompt(_repair_prompt(raw,unit.id),deepdive model,cfg,
      cwd=repo_root,graph_name="s4-deepdive",tag suffixed json-repair,
      max_tokens=int(knob(cfg,"step4.max_tokens",64000)),response_model)
    [findings,by_unit]=reduce_outcomes([unit],{unit.id:repaired},cfg,repo_root,inventory)
    if (by_unit[unit.id]!="failed") { bump repair success }
  }
  if (by_unit[unit.id]=="failed") { raise RuntimeError for parse failure after repair }
  yield _cap_findings(unit.id,findings,cfg)
}

// Source: vvaharness/pipeline/stages/s4/session.py:340-376
fn _cap_findings(unit_id, findings, cfg) {
  cap=cfg.step4.max_findings_per_run, default None
  if (cap is truthy && len(findings)>cap) {
    Count/log truncated rows; keep first cap findings in emission order.
  }
  yield findings
}
fn _dedup_by_key(findings, line_bucket) {
  Keep first finding for each canonical_key(line_bucket), preserving insertion order.
  Count merged rows; bump counter when positive; yield [retained,merged].
}
fn investigate_unit(unit, ctx, repo_root, cfg, stats=None) {
  if (cli.aborted()) { raise RuntimeError }
  findings=_investigate_unit_once(unit,ctx,repo_root,cfg)
  [deduped,merged]=_dedup_by_key(findings,cfg.step4.line_bucket default 10)
  if (stats!=None) { stats.merged=merged }
  yield deduped
}

// Source: vvaharness/pipeline/stages/s4/session.py:379-459
fn _batch_repair_prompt(raw, unit_ids) {
  Request ONLY corrected {outcomes:[...]} JSON with exactly those ids, one each,
    preserving findings and facts; append original reply. Exact string is in assets.
}
fn _batch_reply(batch, ctx, repo_root, cfg) {
  s4=cfg.step4
  files=union of member files, first occurrence order
  code=_load_files_full(files,repo_root) only when inline_source default false is enabled
    AND every unit is non-LARGE; otherwise None.
  response_model=InvestigationOutcomes if route in RESPONSE_MODEL_VIAS, else None
  Use fresh shared flag, graph predicate, effort and validated tools as on singleton path.
  Nested _dispatch rebuilds _tool_setup with outcome="InvestigationOutcomes" and members=len(batch).
  initial=build_batch_prompt(batch,code,len(files),_cap_int(s4,"max_model_calls",0),graph)
  Append fresh transcript recorder, pin session to ["s4",batch[0].id], use same deadline/resume/replay path.
  _agentic supplies all the same fields/defaults as singleton _agentic above, with batch tag/schema.
  yield dispatch_or_retry_unforced(_dispatch,batch tag,stage="s4",
    droppable_effort(...,agentic=true),resend_refusal=refusal_resend_allowed(...))
  The prompt gets the unscaled call limit; middleware gets _batch_limit(limit,len(batch)).
}

// Source: vvaharness/pipeline/stages/s4/session.py:462-514
fn investigate_batch(batch, ctx, repo_root, cfg, stats=None) {
  ids=member ids; raw=_batch_reply(batch,ctx,repo_root,cfg)
  per_unit=split_batch_reply(raw,ids)
  if (!per_unit) {
    Log recovered repair attempt; increment attempted counter.
    Dispatch _batch_repair_prompt(raw,ids) through dispatch_prompt with deepdive model,
      cfg,cwd,graph_name,repair tag,max_tokens default 64000,
      response_model=InvestigationOutcomes only for RESPONSE_MODEL_VIAS.
    per_unit=split_batch_reply(repaired,ids)
    if (per_unit) { bump repair success }
  }
  if (!per_unit) { raise RuntimeError for shared reply parse failure after repair }
  [findings,by_unit]=reduce_outcomes(batch,per_unit,cfg,repo_root,inventory=set(ctx.all_files))
  out = dictionary with empty list for every member id
  Group findings by finding.chunk_id into out, creating other keys if returned.
  for each unit in batch {
    capped=_cap_findings(unit.id,out[unit.id],cfg)
    [out[unit.id],merged_by_unit[unit.id]]=_dedup_by_key(capped,cfg.step4.line_bucket default 10)
  }
  if (stats!=None) { stats.merged_by_unit=merged_by_unit }
  Count by_unit verdicts uninvestigated/failed; yield [out,by_unit].
}
```

`max_findings_per_run` is applied per unit, including each batch member, before
canonical-key deduplication. Its name is retained. The generic retry helper and
outcome reducer are not treated as verified simply because their callers were read.

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../../../prompt_workflow.sudo.md).

- [vvaharness/pipeline/stages/s4/session.py](../../../../../prompt_representation/vvaharness/pipeline/stages/s4/session.py.sudo.md)
