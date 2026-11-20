# s4/prompts.py — prompt construction

Executable formatting; resulting instructions are **model requests**. Literal
prompt text is preserved without execution in the adjacent mirrored asset tree
`assets/vvaharness/pipeline/stages/s4/prompts.py.strings.json` (source spans per
string). Schema descriptions and session repair messages have their own extracts.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:21-198
Model-request clauses retain source identifiers:
  _CWE_CLAUSE: most-specific CWE required in every finding; use evidence over task label.
  _BREADTH_CLAUSE: separate distinct weakness classes at one location, avoid duplicates.
  _CWE_PAIRS: cookie HttpOnly/Secure/SameSite, CSRF/authorization, login rate/enumeration/password,
    password-hash specificity, template/XSS/eval specificity, SSRF/redirect examples.
  _CWE_TOOL_DUTY: call CweGuidance only for cases not already covered, address FP checks.
  _GRAPH_TOOL_DUTY: six graph tools for reachability/context; importers alone do not prove reachability.
  _SCOPE_CLAUSE: FILES is a starting point; follow this threat elsewhere in repository.
  _VERDICT_CLAUSE: confirmed/refuted/inconclusive must reflect evidence; none is a default guess.
  _FP_DISCIPLINE: address why existing controls fail when still claiming exploitability.
  _READ_COMPLETELY_CLAUSE: asserts source already inlined; avoid fetching it again, finish paginated reads.
  _ABSENCE_METHOD: enumerate real reachable sites, justify control, check central mechanisms;
    report absent sites or refute with population count.
  _SKILL_DUTY: at most one family lens, only if FP guidance is missing, name it in rationale.
  _SURFACE_INLINED / _SURFACE_TO_READ: use inline text or read every listed path to end.
  Budgeted and full reachability clauses select graph tools versus Grep callers.
These statements are content, not actions executed by this module.

// Source: vvaharness/pipeline/stages/s4/prompts.py:201-315
fn _budgeted_sweep(budget, inlined, graph) {
  lookups=max(0,budget-1)
  Format request reserving last model call for outcome; describe lookups count.
  Choose inline/no-inline clause, graph/Grep reachability clause,
    breadth in one probe/execute/grep call, report all evidenced distinct weaknesses.
}
fn _breadth_sweep(inlined, graph) {
  Request four passes IN ORDER: surface, reachability, co-located classes, siblings.
  Choose surface clause from inlined; choose reachability clause from graph.
  Request all passes by same agent, no subagents. No execution guarantee is inferred.
}
fn _shell_duty(graph) {
  Join _SHELL_DUTY, _SHELL_GRAPH_HANDOFF only if graph, then _SHELL_NOTES.
  Request narrow POSIX read-only shell use, batched patterns, probes, no writes/install/network/git mutation;
    graph still establishes reachability. These are prompt restrictions, not a shell sandbox implementation.
}
fn _sweep(budget,inlined,graph) {
  if (budget>0) { _budgeted_sweep(budget,inlined,graph) }
  else { _breadth_sweep(inlined,graph) }
}
fn _closing(budget) {
  if (budget>0) { "Spend your lookups, then report the outcome object." }
  else { "Work your plan, make all four passes, then report the outcome object." }
}

// Source: vvaharness/pipeline/stages/s4/prompts.py:318-420
_OUTPUT_EXAMPLE is literal example JSON/prose, not an observed scan result.
fn build_plan_system_prompt(graph=true) {
  _PLAN_HEAD + (_PLAN_REACHABILITY_GRAPH if graph else _PLAN_REACHABILITY_NO_GRAPH) + _PLAN_TAIL
  These request FIRST write_todos, coverage of every file, locating implementation,
    reachability, claim/FP judgment, other classes, siblings, missing-control enumeration;
    accurate statuses and more todos as evidence expands.
  The text claims plan completion is the only way to report. Actual EvidenceGate can relent.
}
PLAN_TOOL_DESCRIPTION requests first call, current statuses and no twice-in-one-turn call.
fn _plugin_tool_duty() {
  extra=graph_tool_names() excluding built-in GRAPH_TOOL_NAMES
  if (!extra) { yield "" }
  else { format head + comma-joined backtick-quoted extra names + tail }
}

// Source: vvaharness/pipeline/stages/s4/prompts.py:423-444
fn build_system_prompt(shell=false,graph=true) {
  Join nonempty clauses with blank lines, IN ORDER:
    _ROLE, _SCOPE_CLAUSE, _VERDICT_CLAUSE, _BREADTH_CLAUSE, _CWE_CLAUSE, _CWE_PAIRS,
    _CWE_TOOL_DUTY, _GRAPH_TOOL_DUTY only if graph, _plugin_tool_duty only if graph,
    _shell_duty(graph) only if shell, _ABSENCE_METHOD, _SKILL_DUTY,
    _READ_COMPLETELY_CLAUSE, _FP_DISCIPLINE, _OUTPUT_EXAMPLE.
  _READ_COMPLETELY_CLAUSE remains unconditional even when inline_source is disabled.
}

// Source: vvaharness/pipeline/stages/s4/prompts.py:447-525
fn _sink_lines(unit) { format file:line, function, snippet and joined CWE values for every sink }
fn _entry_point_lines(unit) { format auth/unauth tag, kind and file::function for every entry point }
fn _cve_lines(unit) { format related_cves as variant/sibling leads }
fn _community_lines(unit,graph) {
  Format community strings; when graph, label them as literal GraphSinksInCommunity/GraphCommunityOf arguments.
}
fn _cwe_lines(unit) { format deterministic matches as a floor to check, not this threat's classification }
fn _file_list(unit) { FILES count and every path in order }
fn _source_section(unit,code) {
  if (code!=None) { format SOURCE CODE plus code }
  else { format _file_list plus request to read every path }
}
fn _unit_block(unit,code,files_only=false,graph=true) {
  Format UNIT id, size, impact/likelihood, actor, claim, surface prose, asset.
  Then optional controls, evidence, sinks, CWEs, entry points, communities, CVEs, in that order.
  Finally _file_list if files_only, otherwise _source_section.
}

// Source: vvaharness/pipeline/stages/s4/prompts.py:528-578
fn build_initial_prompt(unit,code,call_budget=0,graph=true) {
  _unit_block(unit,code,graph=graph) + blank lines + _sweep(call_budget,code!=None,graph)
    + blank lines + _closing(call_budget)
}
fn _batch_duty(units) {
  Format member count and ids; request OWN outcome/rationale/findings per id,
    separate judgments despite shared files, correct surface assignment,
    no equal-output quota and no summarizing several sites into one span.
}
fn _shared_code_section(code,n_files) {
  if (code==None) { request reading listed paths }
  else { inline union source once with file count; explain shared path can pose different questions }
}
fn build_batch_prompt(units,code,n_files,call_budget=0,graph=true) {
  blocks = _unit_block of each unit with code=None, files_only=true, graph, separated by Markdown rules
  Format IN ORDER: _batch_duty, blocks, _shared_code_section, _sweep, _closing,
    with source blank-line/rule delimiters.
}
```

No content here is promoted into an always-executed investigation substep.
The schema file's “from FILES list” description and system prompt's broader
scope are both retained.

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../../../prompt_workflow.sudo.md).

- [vvaharness/pipeline/stages/s4/prompts.py](../../../../../prompt_representation/vvaharness/pipeline/stages/s4/prompts.py.sudo.md)
