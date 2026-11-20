# s4/outcomes.py — reply contracts and finding expansion

Executable validation and reduction are separated from model-facing field
descriptions. Enum/coercion/path-resolution helpers are expanded in source_detail/.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:34-126
interface InvestigatedFinding {
  Required typed fields: cwe:string, file:string, line_start:integer,
    vuln_class:VulnClass, title:string, severity:Severity, description:string,
    exploit_scenario:string, recommendation:string.
  sink_line=0; line_end=0; also_cwes=[]; repeat_lines=[]; preconditions=[].
  Before validating sink_line/line_end, apply _coerce_int(value,0).
  Before validating repeat_lines:
    None becomes []; list/tuple maps each member through _coerce_int(value,0);
    other values pass unchanged to subsequent typed validation.
}
interface InvestigationOutcome {
  Required: unit_id:string, verdict in ["confirmed","refuted","inconclusive"], rationale:string.
  findings:list of InvestigatedFinding = [].
}
interface InvestigationOutcomes { required outcomes:list of InvestigationOutcome }
```

Model request, same source lines 34–126: schema descriptions ask for one
most-specific CWE; a repository-relative file “from this threat's FILES list”;
inclusive construct spans, a distinct sink statement or zero; distinct additional
CWEs and same-file repeat sites; concrete preconditions; a title of at most 12
words, description/recommendation at most two sentences, scenario at most five,
and rationale at 1–3 sentences. They request exact unit ids and all batch members.
These prose length/membership/evidence requirements have no corresponding
validator in this module. Field text is preserved exactly in the assets.

```sudo
// Source: vvaharness/pipeline/stages/s4/outcomes.py:129-201
fn _validate_direct(raw) {
  InvestigationOutcome.model_validate_json(raw); ValueError yields None.
}
fn _validate_batch_direct(raw) {
  InvestigationOutcomes.model_validate_json(raw); ValueError yields None.
}
fn _validate_salvaged(raw) {
  InvestigationOutcome.model_validate(extract_json(raw)); ValueError yields None.
}
fn _validate_batch_salvaged(raw) {
  InvestigationOutcomes.model_validate(extract_json(raw)); ValueError yields None.
}
fn _bump_parse_failure(raw) {
  if (stripped raw is nonempty && does not end with "}") { bump s4_outcome_truncated }
  else { bump s4_outcome_malformed }
}
fn parse_outcome(raw) {
  Try direct, then salvaged validation, yielding first non-None result.
  Otherwise _bump_parse_failure(raw); yield None.
  Only the validators' ValueError is caught; no invented blanket exception handler.
}
fn _as_batch(raw) {
  Try direct batch, then salvaged batch; if either non-None yield it.
  Otherwise parse_outcome(raw); wrap a non-None result as singleton InvestigationOutcomes,
    else yield None.
}
fn split_batch_reply(raw, unit_ids) {
  batch=_as_batch(raw)
  if (batch==None) { yield {} and end this call }
  wanted=set(unit_ids); by_unit={}
  for each outcome in batch.outcomes {
    if (outcome.unit_id not in wanted) { bump s4_batch_unit_id_invented; continue }
    by_unit[outcome.unit_id]=outcome.model_dump_json()
    Later duplicate ids overwrite earlier replies.
  }
  Count wanted ids absent from by_unit; bump omitted count when nonzero; yield by_unit.
}

// Source: vvaharness/pipeline/stages/s4/outcomes.py:204-245
fn _resolved_cwe(f, fallback_cwes) {
  cwe=norm_cwe(f.cwe)
  if (cwe) { yield cwe and end this call }
  cwe=first fallback_cwes entry if any, else None
  if (cwe) { bump s4_finding_cwe_backfilled }
  yield cwe
}
fn _at_line(f, chunk_id, cwe, line_start, width, sink_ref) {
  Build Finding with supplied anchor, line_end=line_start+width, supplied cwe/chunk_id/sink_ref;
    copy title,file,vuln_class,severity,description,exploit_scenario,recommendation,preconditions from f.
  Other Finding defaults are expanded in source_detail/vvaharness/models/scan/findings.py.sudo.md.
}
fn _extra_cwes(f, primary, max_extra) {
  seen=[]; collapsed=0
  for each raw in f.also_cwes {
    c=norm_cwe(raw)
    if (!c || c==primary || c in seen) { continue }
    if (primary && same_weakness(primary,c)) { collapsed+=1; continue }
    Append c to seen.
  }
  Count collapsed and excess entries; yield first max(max_extra,0) of seen in input order.
}

// Source: vvaharness/pipeline/stages/s4/outcomes.py:248-271
fn fan_out(f, chunk_id, fallback_cwes=None, cfg=None, repo_root, inventory) {
  f=copy f with file=resolve_inventory_path(repo_root,f.file,inventory)
  cwe=_resolved_cwe(f,fallback_cwes or [])
  width=max(f.line_end,f.line_start)-f.line_start
  anchors=[f.line_start] + sorted distinct positive repeat_lines excluding primary line
  cwes=[cwe] + _extra_cwes(f,cwe,max_extra=int(knob(cfg,"step4.max_extra_cwes",2)))
  Count repeat anchors and extra CWEs, separately and once-per-finding.
  sink=file + ":" + sink_line only if sink_line>=1, else None; count nonempty sink.
  Yield cross product of anchors (outer order) and cwes (inner order), via _at_line.
  Preserve span width at every anchor; retain sink_ref only at primary anchor.
  No file EOF check is implemented in this function; later-stage gates are represented separately.
}

// Source: vvaharness/pipeline/stages/s4/outcomes.py:274-300
fn reduce_outcomes(units, raw_outcomes, cfg=None, repo_root, inventory) {
  by_unit=map every unit.id to "uninvestigated"; units_by_id=map id to unit; findings=[]
  for each [unit_id,raw] in raw_outcomes insertion order {
    if (unit_id not in by_unit) { bump invented id; continue }
    if (raw==None) { continue }
    outcome=parse_outcome(raw)
    if (outcome==None) { by_unit[unit_id]="failed"; continue }
    by_unit[unit_id]=outcome.verdict
    unit=units_by_id[unit_id]
    for each f in outcome.findings { append fan_out(f,unit.id,unit.cwes,cfg,repo_root,inventory) results }
    No comparison between outcome.unit_id and this dictionary key is made here.
    No branch suppresses findings based on refuted/inconclusive verdict here.
  }
  Count units still uninvestigated; yield [findings,by_unit].
}
```

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../../../prompt_workflow.sudo.md).

- [vvaharness/pipeline/stages/s4/outcomes.py](../../../../../prompt_representation/vvaharness/pipeline/stages/s4/outcomes.py.sudo.md)
