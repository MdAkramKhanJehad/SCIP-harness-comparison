# vvaharness — readable workflow map

Read this together with `orchestrator/scan.sudo.md`. This map adds the remaining
stage/component behavior without flattening their nested calls. All exact
conditions, helpers, configuration defaults, exception scopes and source
expressions are expanded under `source_detail/<original-path>.sudo.md`.
The detail tree includes the vendored SDK, operational entrypoints and data
models. A function named below is the original source callable, not new grammar.

## Entry, configuration and batch hierarchy

```sudo
// Source: vvaharness/config/__init__.py:839-905
fn load(path) {
  raw=read_primary(path)
  Validate existence, file type, readability, UTF-8, YAML and mapping shape in read_primary.
  Fill missing values by _deep_merge(_STEP_DEFAULTS,raw).
  Resolve optional trusted config.local.yaml beside this profile, honoring its disabling environment flag.
  Merge accepted local overlay above the profile, then expand the merged tree's environment references.
  Validate refusal_retries; emit accepted overlay's resolved override details.
  Wrap Config and record _config_dir; do not read target-owned configuration implicitly here.
}

// Source: vvaharness/config/__init__.py:907-1008
fn apply_step1_overlay(cfg,path,expand=true) {
  Refuse network/UNC path before filesystem access; absent local file yields [cfg,false].
  Enforce 1 MiB read limit, UTF-8, valid YAML mapping.
  Unwrap an exactly-one-key step1 mapping when its value is a mapping.
  Expand environment only when expand is true.
  Append previously absent top-level list entries; replace scalars.
  For nested dictionaries use replace-merge, so their lists replace rather than append.
  Yield [cfg,true]. refusal_retries separately accepts None or integer 0..1, excluding booleans.
}

// Source: vvaharness/orchestrator/batch.py:380-504
fn run_batch(list_file,args,cfg) {
  Parse CSV or text manifest using its source-specific validation/size limits.
  Filter case-insensitive RepoName globs before cloning; all skipped yields exit 2.
  if (args.group_by_app) { delegate to _run_batch_grouped and end this call }
  for each entry in manifest order {
    Reset tokens, stages, counters, cached provenance, response-quality/warn-once registries,
      known redaction values and CLI abort state.
    Acquire local path or clone; stop-after clone records acquisition and skips scan.
    Otherwise call scan_repo with path_prefix=repo_name and collect its ScanOutcome.
    Rethrow authentication/proxy/state-store faults; log ordinary per-repo failures and continue.
    On exit purge a cloned target only when keep_clones is false and stop_after is not clone.
  }
  Write batch summary; return 1 for health failures before considering EXIT_NOT_REMEDIATED;
    return 0 only when neither failed nor unremediated entries remain.
}
```

Grouped acquisition/scanning is kept as its own source branch in
`source_detail/vvaharness/orchestrator/batch.py.sudo.md` (lines 545–647);
it stages repos by application, resets scan state per application and scans
the application directory. It is not represented as parallel independent repo scans.
The CLI command dispatcher, SDK stage entrypoints and direct remediation/validation
APIs retain separate entrypaths in `source_detail/vvaharness/{cli,sdk,api.py}`.

## Static context and threat-derived work

```sudo
// Source: vvaharness/pipeline/stages/s0_seed.py:40-79
fn s0_seed.run(repo_root,cfg,ckpt_dir) {
  Walk scoped source; detect/canonicalize languages and optionally narrow language labels.
  Warn on unknown configured language labels.
  Match detect.scan against SORTED in-scope source files; construct SeedPackage with
    returned entry points and unsafe sinks, language labels, inventory and exclusions.
  No model is called here. Preserve the source log that calls this AST-based even though matching is textual.
}

// Source: vvaharness/codegraph/build.py:34-83
fn build_graph(repo_root,project_id,workspace_dir,enrichers) {
  Construct Workspace with ArcadeDBBackendFactory; analyze repo with trusted enrichers.
  On analysis exception close workspace then rethrow; do not silently substitute an absent graph.
  Read graph info; return GraphHandle retaining workspace, graph, counts and enricher names.
}
fn graph_is_degenerate(ctx,cfg) {
  Missing handle or exactly zero edges yields true.
  Unmeasured node count yields false.
  Otherwise compare node count < step0.min_graph_nodes_for_gate (default 10).
}

// Source: vvaharness/pipeline/stages/s1_preprocess.py:76-207
fn s1_preprocess.run(repo_root,cfg,known_cves,controls,seed,graph_handle) {
  Reuse a seed's nonempty inventory, else walk source again.
  Set local read-tool scope BEFORE configuration-file deduplication; dedup inventory/config representatives.
  Resolve seeded paths against retained inventory and top-level prefixes; discard ambiguous/unresolvable paths.
  Keep resolved taint paths only when at least two hops remain.
  Merge seed entry points/sinks; derive language/modules/notes from graph when present,
    else use empty modules/notes and extension-frequency language fallback.
  Attach CVEs, design controls, inventory and exclusions; validate ContextPackage.
  Empty inventory raises EmptyScopeError.
  Nonempty inventory with zero modules/entry points/sinks is logged as s1_zero_output.
  No model call is made despite the configured preprocess role displayed by orchestration.
}

// Source: vvaharness/pipeline/stages/s2/__init__.py:127-272
fn s2.run(repo_root,repo_name,cfg,known_cves,controls,ctx,app_profile) {
  Gather bounded source evidence; derive repository-kind baseline and build model user prompt.
  Call dispatch_or_retry_unforced around _threatmodel_call, passing evidence-dependent tool requirement.
  Record-and-rethrow call failure.
  Parse reply; on parse failure attempt one repair with full step2 token/timeout caps.
  Failed repair logs and rethrows, rather than returning an empty model as clean success.
  Finalize threat paths; call _retry_if_hollow; record zero-threat degradation when applicable.
  Audit required baseline categories BEFORE output caps; cap threats, assets, boundaries;
    report cap effects and undisposed baseline categories using the source's branches.
  Exact baseline checks, hollow retry and prompt clauses are in the linked s2 detail modules.
}

// Source: vvaharness/pipeline/stages/s3_decompose.py:44-171
fn s3_decompose.run(ctx,cfg) {
  Build empty TaskManifest; append one InvestigationUnit per threat with nonempty validated surface files.
  A threat lacking surface files is recorded in threats_without_unit and receives no unit.
  Preserve the complete deduplicated surface rather than splitting by community or LOC.
  Attach sinks, entry points, related CVEs, communities and CWE hints from those files.
  risk_rank=base_rank + 26 - impact_ordinal*likelihood_ordinal.
  LOC < 2000 gives SMALL; LOC < 8000 gives MEDIUM; otherwise LARGE.
  Add language annotations; record files named by no unit in unreachable_files;
    report LOC distribution and queue units for tracker.
  No model call is made by this stage.
}
```

The entire S4 branch—including serial/batched scheduling, singleton retries,
model-call/evidence/tool budgets, repair, deadline resume/replay, shared state and
finding fan-out—is described in the existing `pipeline/stages/s4*` readable files.
Their previously unresolved local calls now resolve to the complete detail tree.

## Enrichment, independent verification, deduplication and reporting

```sudo
// Source: vvaharness/pipeline/stages/s5/__init__.py:57-119
fn s5.run(findings,ctx,cfg) {
  Create bounded FileCache; derive entry anchors and seed paths.
  valid_files=set(ctx.all_files) only if nonempty, else None (no inventory-membership check).
  Enable sink reanchoring by knob (default true), movement bound default 40 lines.
  for each raw finding {
    Call reject_path BEFORE enrichment can read it: reject matching test/mock/example paths
      except secret-class findings; reject inventory nonmembers only when valid_files is not None.
    If path accepted, enrich/reanchor then apply coordinate/readability/EOF gate.
    Keep valid finding and its original pre_anchor_line; record every rejected finding.
  }
  Trivially dedup using ORIGINAL anchors and line tolerance (S5 None falls back to S7 default 3; zero stays zero).
  if (step5_detectors.enabled, default true) {
    Add deterministic rule candidates up to max_rows default 200;
    enrich without reanchoring and apply coordinate gate to each.
  }
  Return kept and drop audit. No model call occurs in this stage.
}

// Source: vvaharness/pipeline/stages/s6_verify.py:150-233
fn s6_verify.run(findings,ctx,cfg,run_id) {
  Empty findings finish progress and yield two empty lists.
  Resolve parallel (default 5), confidence gate (default 7/10), split_retry (default true),
    route-specific allowed tools and optional read-timeout override.
  Label findings; plan shared sessions (batch_size default 12).
  Create shared _Sink with filed lines, seen canonical keys, FileCache readers,
    trait-stamp/reframe knobs and optional inventory.
  Under the process-wide timeout override, create one daemon-worker pool for both waves.
  captive=_run_wave(original batches,...).
  _reverify_discoveries(...,captive).
  On every exit shut down pool with wait=false and cancel_futures=true.
  Report explicit drop buckets and uniform-confidence diagnostics; return shared verified/dropped lists.
}

// Source: vvaharness/pipeline/stages/s6_verify.py:283-543
fn _run_wave(batches,ctx,cfg,tools,sink,ex,split_retry,ceiling,parallel,sweep_tier,captive,abort_on_guardrail) {
  Submit batches; start each wall clock INSIDE its worker, not when queued.
  Maintain pending, resolved, abandoned flags and distinct retry-child tracking sets.
  while (pending is nonempty) {
    Wait for first completed with heartbeat/ceiling wake interval.
    Resolve each batch index at most once; late results from abandoned parents cannot file results.
    Branch separately on guardrail/refusal, output truncation, structured-output error,
      timeout, other deterministic/transient failure, and normal partial/full outcomes.
    Multi-member failures may split to singletons only under the source's per-cause gates.
    Structured failure permits a bounded singleton retry; refusal children do not resend refusal again.
    Omitted members of a shared reply may receive singleton judgments; already judged members are accepted once.
    Apply ceiling from actual start; abandon expired parent and optionally split children with fresh clocks.
    If all workers stay captive for a further ceiling, cancel never-started work and record VERIFY_ERROR.
  }
  Return still-running captives for the next wave; interrupted processing aborts CLI work and rethrows.
}

// Source: vvaharness/pipeline/stages/s6_verify.py:250-280
fn _reverify_discoveries(ctx,cfg,tools,sink,ex,captive) {
  Remove first-wave s6_discovered rows from shared verified list IN PLACE.
  Disable new discovery minting and repeat cloning, widen progress first, pre-file discovered lines.
  Independently run a second wave with guardrail fail-fast disabled.
  Restore both flags on every exit. No recursive discovery waves are introduced.
}

// Source: vvaharness/pipeline/stages/s6_verify.py:685-871
_Sink classifies each verdict by min_confidence; contradicted missing-import false-positive premises
  become INCONCLUSIVE. Confirmed primary/repeat rows may ship; other rows get explicit drop reasons.
Tool-free replay discoveries are discarded; low-confidence discoveries are discarded;
  remaining discoveries require inventory/EOF validity and an atomic shared canonical-key reservation.
The classifications, CVSS corrections, repeat expansion and normalization are expanded in s6/outcomes.py.

// Source: vvaharness/pipeline/stages/s7_dedup.py:35-138
fn s7_dedup.run(verified,cfg,ctx) {
  Zero/one rows return a list copy plus an empty dropped list.
  First collapse trivial same-file/weakness rows using pre_anchor_line when nonzero and tolerance default 3.
  If two or more unresolved rows and semantic enabled, ask semantic_dedup for proposed relations.
  Convert its local positions to original indices; accept only backward relations;
    block CWE conflicts against the canonical ROOT.
  Preserve independent sites only under per_sink_keep (default true) and source independence judgment.
  Attach duplicate references; build canonical list and DroppedFinding entries with canonical indices.
}

// Source: vvaharness/pipeline/stages/s8_chain.py:147-275
fn s8_chain.run(findings,ctx,cfg,dropped,raw_findings_count,metrics) {
  Empty findings distinguish empty scope (degraded) from no surviving findings.
  Choose bounded enrichment window; invalid window configuration falls back to all findings.
  If window admits zero findings, use deterministic_report without asking a model.
  Call chain model; at-cap unretried truncation may halve the rank-prefix window and resend ONCE.
  Persist redacted raw reply before parse; bounded eligible JSON repair is optional on parse failure.
  Non-halt call/parse/hydration failures fall back to deterministic_report.
  Restore any temporarily changed severity before deterministic hydration fallback.
  Rank/hydrate with source severity floor, id/chain/evidence validation and index remapping.
  If windowed, supplement model summary with whole-report templated summary.
  Preserve every canonical finding even when model enrichment omits it.
}

// Source: vvaharness/pipeline/stages/s9_sarif.py:26-31
fn s9_sarif.run(report,sarif_path,application_id,app_info,cfg) {
  Delegate to write_sarif(report, sarif_path, application_id, app_info, cfg=cfg).
  Typed finding, chain, code-flow, related-location, scan-health and application context
    mappings are detailed in pipeline/stages/s9/typed_sarif.py and s9/health.py.
}
```

## Optional live-verification branch inside S6

```sudo
// Source: vvaharness/exploit_verification/verify/router.py:301-607
fn ev_router.run(findings,ctx,cfg,run_id) {
  Run _run inside its s6-ev token phase.
  If collection unusable, delegate all findings to static verification.
  Load options/auth; adopt collection auth strategy when operator left strategy unset; start shared OOB listener.
  Build static classification hints, then require usable model classification;
    absent/unavailable classification stands down entirely to static.
  Partition classes into non-live/static, passive posture and active route-bound work.
  For route-bound work build one endpoint/code index and map finding ids to bounded endpoint matches;
    mapper model falls back to classifier. Unmapped work goes to static, without invented endpoints.
  Map passive observations to reachable endpoints.
  Check credential freshness: source policy chooses abort-to-static, warn/proceed, or authz/idor degradation.
  Run live candidates using source executor concurrency/rate/budget controls; collect verdicts and evidence.
  Default ev_overrides_static=false sends EV-confirmed rows through static verification too.
  After static returns, rescue matching EV-confirmed rows that static dropped; retain their static verdict alongside EV evidence.
  Legacy override=true can keep hard EV proofs and skip static for those source-qualified cases.
  Reduce live results in candidate order, persist replay/probe bundles best-effort, then run static and rescue.
  On exit from live candidate processing, execute its finally branch: inspect callback count then call OOB stop.
  Earlier stand-down branches call stop explicitly.
  Do not widen this finally scope to cover earlier classification/mapping/setup failures.
  After static/rescue processing return hard-proof rows + static-verified rows + rescued rows, then remaining drops.
}

// Source: vvaharness/exploit_verification/verify/run.py:418-576
fn verify_candidate(finding,matches,opts,auth,...) {
  If no matches, return INCONCLUSIVE with no requests.
  Use ONE shared request budget across all ranked endpoints for this finding.
  for each match in matches {
    v=verify_finding(finding,match,...,budget)
    if (v.status=="CONFIRMED") { end this invocation with v }
    Retain the FIRST non-confirmed verdict as best, as the source does.
    If refusal flag was set, stop trying further endpoints.
  }
  Return retained verdict.
}
fn verify_finding(finding,match,opts,auth,...) {
  Build bounded deterministic attack plan and execute its first-set specs.
  Oracle derives a tell from transcript; it is evidence, not confirmation authority.
  If judge unavailable, return INCONCLUSIVE/static fallback even when a tell fired.
  Otherwise optionally run attacker loop (sdk/openai/deepagents only); do not short-circuit on an early tell.
  Discard attacker final text; retain executor transcript. Refusal sets finding-wide flag;
    other attacker failure still allows adjudication of existing transcript.
  Re-evaluate oracle; call judge only when tell confirmed or a request reached the application.
  Use adjudication's confirmation/proof/counterfactual/impact checks and source privilege clamp;
    confirmed output gets replay bundle; other final output preserves category/request count.
}
```

Collection parsing, optional-mode resolution, offline gate, reachability probe,
credential refresh, URL/TLS/method restrictions, OOB listener, executor locking,
rate limiting, payload templates, judge prompts and replay execution each retain
their own source tree under `source_detail/vvaharness/exploit_verification/`.
Availability of an HTTP tool does not mean the model invokes it.

## S10, S11 and standalone application APIs

```sudo
// Source: vvaharness/remediation_agent/runner.py:96-184
fn process_targets(targets,layout,cfg,repo_path,opts,report,progress) {
  Build optional policy context; process targets SEQUENTIALLY via remediate_one.
  Per-target resume checks, finding identity, policy pre-gate, plugin invocation,
    artifacts/provenance/checkpoint and result classification remain in remediate_one and plugin_runner.
  Count FIXED, NOT_FIXED and FAILED separately. Progress records attempted=total,
    fixed=fixed, not_fixed=total-fixed; this progress not_fixed includes failed cases.
  Best-effort augment reports; return 1 only when FAILED count is nonzero, else 0.
}

// Source: vvaharness/remediation_agent/plugin_runner/__init__.py:435-505
fn _invoke(target,cfg,repo,mode,verbose,pre,ctx) {
  Build user prompt BEFORE applying _symlink_safe_mode; preserve that ordering.
  Fix mode with escaping symlinks is downgraded to source mode string "report".
  Select deepagents, cli, or legacy sdk/openai branch using resolved route.
  sdk/openai remove Edit/Write then re-add them only in fix mode;
    actual route tool implementations still determine what executes.
  cli keeps its configured tool list; no blanket report-mode write prohibition is inferred.
  Apply the selected route's timeout/turn/budget options; limits differ by route.
  Return raw route output (with optional verbose display). Parsing, post-policy checks and case persistence
    occur in calling functions, not inside _invoke.
}

// Source: vvaharness/remediation_agent/plugin_runner/run.py:95-120
fn call_with_guards(fn,request) {
  Build policy pre-gate and provenance. If policy denies, return guidance without a model call.
  Record preexisting dirty state and snapshots; call the supplied engine function through _call_engine.
  On engine exception, _engine_failed reverts this call's changed/new files using the pre-call snapshot
    and returns a Not Fixed verdict. Otherwise coerce raw output into a RemediationVerdict.
}

// Source: vvaharness/remediation_agent/plugin_runner/run.py:146-168
fn harness_amend(remediation,snapshot,request,pre,denied,started,spend_before,pre_call_dirty) {
  If pre is present, enforce_post and record its policy result/reverted paths.
  Derive actual diff; build evidence/provenance; finalize using request.mode, diff and files_touched.
  Reconcile post metadata and return Amended contract.
}

// Source: vvaharness/remediation_agent/plugin_runner/run.py:191-207
fn apply_plugin(target,out_dir,cfg,repo,mode,verbose,policy_ctx) {
  request=EngineRequest(target,repo,mode,cfg,verbose,policy_ctx)
  guarded=call_with_guards(plugin_runner._invoke,request)
  amended=harness_amend(guarded.verdict,guarded.snapshot,request,guarded.pre,
    guarded.denied,guarded.started,guarded.spend_before,guarded.pre_call_dirty)
  Write case artifacts from guarded verdict, amended contract, merged metadata and reverted paths.
  End this invocation with amended.remediation.
}

// Source: vvaharness/pipeline/stages/s11_validate.py:26-53
fn s11_validate.run(repo,cfg,config_path,finding_ids,resume,report_md,progress) {
  Build standalone validate CLI arguments; pass config/report only when truthy, one finding flag per id,
    and resume flag only when true. Invoke validate_main, optionally forwarding progress.
  Best-effort case rollup must not change returned code.
}

// Source: vvaharness/validation/cli/_run.py:375-434
fn run_validation(repo,selection,workspace_root,config,report_md) {
  Register path-derived run; load owned S10 case provenance BEFORE selecting cases.
  Reject malformed/unsafe ingest; source-specific no-case exit status applies to empty selection.
  Prune stale producer checkpoints; create validation run with FIX_POLICY and resume setting.
  Run validatable cases in sequence; reuse producer-matching checkpoints only under resume.
  Each plan launches a bounded session, collects persona/gate results and writes host-scored result.
  Best-effort augment reports; clean staging workspace.
  Session failure yields exit 1 ahead of verdict-derived rc_for_verdicts.
}

// Source: vvaharness/validation/constants/synthesis.py:20-20
MIN_CONSENSUS_VOTES=2

// Source: vvaharness/validation/synthesis/_consensus.py:68-189
fn synthesize_gates_for_finding(reports,tracking_id,required_gates) {
  Select matching tracking id; group entries by gate; fold duplicate persona votes conservatively.
  Ignore SKIP in evaluated votes; all skips yields SKIP/FLAGGED.
  A unique most-frequent status with at least MIN_CONSENSUS_VOTES yields HIGH confidence.
  Otherwise choose most conservative among tied top statuses and FLAGGED confidence.
  Conservative ordering is FAIL, PARTIAL, PASS, SKIP, INVALID.
  Merge evidence and descriptions deterministically; add INVALID/FLAGGED for unanswered required gates
    only when some gate was answered. Preserve the empty-by_gate exception.
}
```

Validation sessions register persona agents and tools. Their prompts request
adversarial roles; registered personas are not asserted to execute in a fixed
order or all be called. Host synthesis, score renormalization, critical-gate and
consensus checks are executable; their exact thresholds reside in the converted
scoring/constants/configuration files. Direct `api.remediate`/`api.validate`
and SDK stage APIs are retained independently of the scan CLI and can take
different argument/configuration paths.

## Remaining supporting components

Every file below has corresponding detailed pseudocode and source-linked assets;
this table is a navigation map, not a substitute for those definitions.

| Original subtree | Role and preserved relationships |
|---|---|
| `cli/`, `__main__.py`, `manifest.py`, `sdk/`, `api.py` | command dispatch, setup/doctor/estimate, manifests, programmatic stages and handoffs |
| `config/`, `scope/`, `lang/`, `detect/` | defaults/overlays, ordered scope filters, path normalization, language matching and deterministic rule dispatch |
| `codegraph/`, `vendor/context_graph_sdk/` | build/handle/graph tools; vendored extraction, resolution, enrichment, snapshot publication, query processes and read limits |
| `backends/llm/`, `backends/harness/` | distinct legacy loop and streaming-harness routes; native/fact tools, capability checks, response parsing, tool/permission/evidence/budget middleware, TLS, cache and retries |
| `evidence/`, `injectors/`, `rules/` | evidence budgets and source excerpts, CVE/design-control/app context injection, CWE/KB normalization and tool guidance |
| `skills/`, `plugins/` | available lenses/probes, temporary injection/cleanup and trusted plugin contracts; loading never implies use |
| `models/`, `report/` | typed contracts, coercions, CVSS/CWE/severity/context scoring, redaction, rendering and report composition |
| `orchestrator/store/`, `util/` | out-of-target SQLite state, transactions/checkpoints/replays, telemetry, progress, token counts, runtime environment/readiness/error handling |
| `inputs/`, `validation/claude_config/`, payload templates | exact policies, playbooks, hints, schema/settings/query/prompt assets with original organization and value indexes |
| `scripts/` | repository-local checkpoint/unit inspection helpers; not inserted as scan stages |

External model/provider implementations, actual database/native parser behavior,
OS scheduling and live target outcomes remain the explicit boundaries documented
in `dependency_boundaries.md`. They are not invented to complete this map.

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../prompt_workflow.sudo.md).

- [vvaharness/skills/access-control/SKILL.md](../prompt_representation/vvaharness/skills/access-control/SKILL.md.sudo.md)
- [vvaharness/skills/batch-etl/SKILL.md](../prompt_representation/vvaharness/skills/batch-etl/SKILL.md.sudo.md)
- [vvaharness/skills/client-side/SKILL.md](../prompt_representation/vvaharness/skills/client-side/SKILL.md.sudo.md)
- [vvaharness/skills/code-exploration/SKILL.md](../prompt_representation/vvaharness/skills/code-exploration/SKILL.md.sudo.md)
- [vvaharness/skills/crypto/SKILL.md](../prompt_representation/vvaharness/skills/crypto/SKILL.md.sudo.md)
- [vvaharness/skills/csrf/SKILL.md](../prompt_representation/vvaharness/skills/csrf/SKILL.md.sudo.md)
- [vvaharness/skills/deserialization/SKILL.md](../prompt_representation/vvaharness/skills/deserialization/SKILL.md.sudo.md)
- [vvaharness/skills/hardcoded-creds/SKILL.md](../prompt_representation/vvaharness/skills/hardcoded-creds/SKILL.md.sudo.md)
- [vvaharness/skills/iac/SKILL.md](../prompt_representation/vvaharness/skills/iac/SKILL.md.sudo.md)
- [vvaharness/skills/injection/SKILL.md](../prompt_representation/vvaharness/skills/injection/SKILL.md.sudo.md)
- [vvaharness/skills/log-injection/SKILL.md](../prompt_representation/vvaharness/skills/log-injection/SKILL.md.sudo.md)
- [vvaharness/skills/logic-bug/SKILL.md](../prompt_representation/vvaharness/skills/logic-bug/SKILL.md.sudo.md)
- [vvaharness/skills/missing-controls/SKILL.md](../prompt_representation/vvaharness/skills/missing-controls/SKILL.md.sudo.md)
- [vvaharness/skills/sensitive-data/SKILL.md](../prompt_representation/vvaharness/skills/sensitive-data/SKILL.md.sudo.md)
- [vvaharness/skills/sibling-instances/SKILL.md](../prompt_representation/vvaharness/skills/sibling-instances/SKILL.md.sudo.md)
- [vvaharness/skills/ssrf/SKILL.md](../prompt_representation/vvaharness/skills/ssrf/SKILL.md.sudo.md)
- [vvaharness/skills/templates/SKILL.md](../prompt_representation/vvaharness/skills/templates/SKILL.md.sudo.md)
- [vvaharness/validation/claude_config/rules/adversarial-review.md](../prompt_representation/vvaharness/validation/claude_config/rules/adversarial-review.md.sudo.md)
- [vvaharness/validation/claude_config/rules/scoring-matrix.md](../prompt_representation/vvaharness/validation/claude_config/rules/scoring-matrix.md.sudo.md)
- [vvaharness/validation/claude_config/skills/validation-scoring/SKILL.md](../prompt_representation/vvaharness/validation/claude_config/skills/validation-scoring/SKILL.md.sudo.md)
- [vvaharness/validation/prompts/system.md](../prompt_representation/vvaharness/validation/prompts/system.md.sudo.md)
- [vvaharness/validation/subagents/cross-repo-analyzer.md](../prompt_representation/vvaharness/validation/subagents/cross-repo-analyzer.md.sudo.md)
- [vvaharness/validation/subagents/penetration-tester.md](../prompt_representation/vvaharness/validation/subagents/penetration-tester.md.sudo.md)
- [vvaharness/validation/subagents/security-architect.md](../prompt_representation/vvaharness/validation/subagents/security-architect.md.sudo.md)
- [AGENTS.md](../prompt_representation/AGENTS.md.sudo.md)
- [CLAUDE.md](../prompt_representation/CLAUDE.md.sudo.md)
- [.github/copilot-instructions.md](../prompt_representation/.github/copilot-instructions.md.sudo.md)
- [scripts/inspect_units.py](../prompt_representation/scripts/inspect_units.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/analysis/processes.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/backends/arcadedb.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/identity.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/models.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/context.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/plugins/correlation.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/plugins/registry.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/plugins/runner.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/progress.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/progress.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/query/context.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/context.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/contracts.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/protocol.py.sudo.md)
- [vendor/context_graph_sdk/src/context_graph_sdk/query/results.py](../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/query/results.py.sudo.md)
- [vvaharness/agentdoc.py](../prompt_representation/vvaharness/agentdoc.py.sudo.md)
- [vvaharness/backends/harness/claude/facts.py](../prompt_representation/vvaharness/backends/harness/claude/facts.py.sudo.md)
- [vvaharness/backends/harness/deepagents/evidence_gate.py](../prompt_representation/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md)
- [vvaharness/backends/harness/deepagents/exclude_tools.py](../prompt_representation/vvaharness/backends/harness/deepagents/exclude_tools.py.sudo.md)
- [vvaharness/backends/harness/deepagents/force_verdict_only.py](../prompt_representation/vvaharness/backends/harness/deepagents/force_verdict_only.py.sudo.md)
- [vvaharness/backends/harness/deepagents/invalid_tool_args.py](../prompt_representation/vvaharness/backends/harness/deepagents/invalid_tool_args.py.sudo.md)
- [vvaharness/backends/harness/deepagents/model_call_budget.py](../prompt_representation/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md)
- [vvaharness/backends/harness/deepagents/options/filesystem.py](../prompt_representation/vvaharness/backends/harness/deepagents/options/filesystem.py.sudo.md)
- [vvaharness/backends/harness/deepagents/options/model_building.py](../prompt_representation/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md)
- [vvaharness/backends/harness/deepagents/options/response_format.py](../prompt_representation/vvaharness/backends/harness/deepagents/options/response_format.py.sudo.md)
- [vvaharness/backends/harness/deepagents/options/tool_call_state.py](../prompt_representation/vvaharness/backends/harness/deepagents/options/tool_call_state.py.sudo.md)
- [vvaharness/backends/harness/deepagents/permit_tools.py](../prompt_representation/vvaharness/backends/harness/deepagents/permit_tools.py.sudo.md)
- [vvaharness/backends/harness/deepagents/profiles.py](../prompt_representation/vvaharness/backends/harness/deepagents/profiles.py.sudo.md)
- [vvaharness/backends/harness/deepagents/tool_budget.py](../prompt_representation/vvaharness/backends/harness/deepagents/tool_budget.py.sudo.md)
- [vvaharness/backends/harness/deepagents/tool_choice_rejection.py](../prompt_representation/vvaharness/backends/harness/deepagents/tool_choice_rejection.py.sudo.md)
- [vvaharness/backends/harness/deepagents/tools.py](../prompt_representation/vvaharness/backends/harness/deepagents/tools.py.sudo.md)
- [vvaharness/backends/harness/deepagents/translate.py](../prompt_representation/vvaharness/backends/harness/deepagents/translate.py.sudo.md)
- [vvaharness/backends/harness/models.py](../prompt_representation/vvaharness/backends/harness/models.py.sudo.md)
- [vvaharness/backends/harness/permission_rules.py](../prompt_representation/vvaharness/backends/harness/permission_rules.py.sudo.md)
- [vvaharness/backends/harness/permissions.py](../prompt_representation/vvaharness/backends/harness/permissions.py.sudo.md)
- [vvaharness/backends/llm/agent_sdk.py](../prompt_representation/vvaharness/backends/llm/agent_sdk.py.sudo.md)
- [vvaharness/backends/llm/cli/env.py](../prompt_representation/vvaharness/backends/llm/cli/env.py.sudo.md)
- [vvaharness/backends/llm/cli/envelope.py](../prompt_representation/vvaharness/backends/llm/cli/envelope.py.sudo.md)
- [vvaharness/backends/llm/cli/oneshot.py](../prompt_representation/vvaharness/backends/llm/cli/oneshot.py.sudo.md)
- [vvaharness/backends/llm/cli/retry.py](../prompt_representation/vvaharness/backends/llm/cli/retry.py.sudo.md)
- [vvaharness/backends/llm/cli/session.py](../prompt_representation/vvaharness/backends/llm/cli/session.py.sudo.md)
- [vvaharness/backends/llm/cli_mcp.py](../prompt_representation/vvaharness/backends/llm/cli_mcp.py.sudo.md)
- [vvaharness/backends/llm/deepagents.py](../prompt_representation/vvaharness/backends/llm/deepagents.py.sudo.md)
- [vvaharness/backends/llm/models.py](../prompt_representation/vvaharness/backends/llm/models.py.sudo.md)
- [vvaharness/backends/llm/openai.py](../prompt_representation/vvaharness/backends/llm/openai.py.sudo.md)
- [vvaharness/backends/llm/openai_responses.py](../prompt_representation/vvaharness/backends/llm/openai_responses.py.sudo.md)
- [vvaharness/backends/llm/registry.py](../prompt_representation/vvaharness/backends/llm/registry.py.sudo.md)
- [vvaharness/backends/llm/sdk.py](../prompt_representation/vvaharness/backends/llm/sdk.py.sudo.md)
- [vvaharness/backends/llm/tool_adapter.py](../prompt_representation/vvaharness/backends/llm/tool_adapter.py.sudo.md)
- [vvaharness/backends/llm/tools.py](../prompt_representation/vvaharness/backends/llm/tools.py.sudo.md)
- [vvaharness/cli/__init__.py](../prompt_representation/vvaharness/cli/__init__.py.sudo.md)
- [vvaharness/cli/_app.py](../prompt_representation/vvaharness/cli/_app.py.sudo.md)
- [vvaharness/cli/_commands.py](../prompt_representation/vvaharness/cli/_commands.py.sudo.md)
- [vvaharness/cli/_setup.py](../prompt_representation/vvaharness/cli/_setup.py.sudo.md)
- [vvaharness/codegraph/queries.py](../prompt_representation/vvaharness/codegraph/queries.py.sudo.md)
- [vvaharness/codegraph/tools.py](../prompt_representation/vvaharness/codegraph/tools.py.sudo.md)
- [vvaharness/config/__init__.py](../prompt_representation/vvaharness/config/__init__.py.sudo.md)
- [vvaharness/exploit_verification/_route.py](../prompt_representation/vvaharness/exploit_verification/_route.py.sudo.md)
- [vvaharness/exploit_verification/auth.py](../prompt_representation/vvaharness/exploit_verification/auth.py.sudo.md)
- [vvaharness/exploit_verification/classify/_tables.py](../prompt_representation/vvaharness/exploit_verification/classify/_tables.py.sudo.md)
- [vvaharness/exploit_verification/classify/llm.py](../prompt_representation/vvaharness/exploit_verification/classify/llm.py.sudo.md)
- [vvaharness/exploit_verification/executor/tool.py](../prompt_representation/vvaharness/exploit_verification/executor/tool.py.sudo.md)
- [vvaharness/exploit_verification/gate.py](../prompt_representation/vvaharness/exploit_verification/gate.py.sudo.md)
- [vvaharness/exploit_verification/mapping/endpoint_index.py](../prompt_representation/vvaharness/exploit_verification/mapping/endpoint_index.py.sudo.md)
- [vvaharness/exploit_verification/mapping/finding_map.py](../prompt_representation/vvaharness/exploit_verification/mapping/finding_map.py.sudo.md)
- [vvaharness/exploit_verification/options.py](../prompt_representation/vvaharness/exploit_verification/options.py.sudo.md)
- [vvaharness/exploit_verification/payloads/loader.py](../prompt_representation/vvaharness/exploit_verification/payloads/loader.py.sudo.md)
- [vvaharness/exploit_verification/probe.py](../prompt_representation/vvaharness/exploit_verification/probe.py.sudo.md)
- [vvaharness/exploit_verification/replay/report.py](../prompt_representation/vvaharness/exploit_verification/replay/report.py.sudo.md)
- [vvaharness/exploit_verification/replay/run.py](../prompt_representation/vvaharness/exploit_verification/replay/run.py.sudo.md)
- [vvaharness/exploit_verification/verify/_da_attacker.py](../prompt_representation/vvaharness/exploit_verification/verify/_da_attacker.py.sudo.md)
- [vvaharness/exploit_verification/verify/judge.py](../prompt_representation/vvaharness/exploit_verification/verify/judge.py.sudo.md)
- [vvaharness/exploit_verification/verify/model.py](../prompt_representation/vvaharness/exploit_verification/verify/model.py.sudo.md)
- [vvaharness/exploit_verification/verify/oracle.py](../prompt_representation/vvaharness/exploit_verification/verify/oracle.py.sudo.md)
- [vvaharness/exploit_verification/verify/prompt.py](../prompt_representation/vvaharness/exploit_verification/verify/prompt.py.sudo.md)
- [vvaharness/exploit_verification/verify/router.py](../prompt_representation/vvaharness/exploit_verification/verify/router.py.sudo.md)
- [vvaharness/exploit_verification/verify/run.py](../prompt_representation/vvaharness/exploit_verification/verify/run.py.sudo.md)
- [vvaharness/exploit_verification/verify/tools.py](../prompt_representation/vvaharness/exploit_verification/verify/tools.py.sudo.md)
- [vvaharness/injectors/cve_feed.py](../prompt_representation/vvaharness/injectors/cve_feed.py.sudo.md)
- [vvaharness/models/case.py](../prompt_representation/vvaharness/models/case.py.sudo.md)
- [vvaharness/models/context.py](../prompt_representation/vvaharness/models/context.py.sudo.md)
- [vvaharness/models/gates.py](../prompt_representation/vvaharness/models/gates.py.sudo.md)
- [vvaharness/models/provenance.py](../prompt_representation/vvaharness/models/provenance.py.sudo.md)
- [vvaharness/models/remediation.py](../prompt_representation/vvaharness/models/remediation.py.sudo.md)
- [vvaharness/models/scan/_sections_chain.py](../prompt_representation/vvaharness/models/scan/_sections_chain.py.sudo.md)
- [vvaharness/models/scan/_sections_pipeline.py](../prompt_representation/vvaharness/models/scan/_sections_pipeline.py.sudo.md)
- [vvaharness/models/scan/findings.py](../prompt_representation/vvaharness/models/scan/findings.py.sudo.md)
- [vvaharness/models/scan/inputs.py](../prompt_representation/vvaharness/models/scan/inputs.py.sudo.md)
- [vvaharness/models/scan/threat.py](../prompt_representation/vvaharness/models/scan/threat.py.sudo.md)
- [vvaharness/models/verdict.py](../prompt_representation/vvaharness/models/verdict.py.sudo.md)
- [vvaharness/models/vocab.py](../prompt_representation/vvaharness/models/vocab.py.sudo.md)
- [vvaharness/orchestrator/batch.py](../prompt_representation/vvaharness/orchestrator/batch.py.sudo.md)
- [vvaharness/orchestrator/checkpoints.py](../prompt_representation/vvaharness/orchestrator/checkpoints.py.sudo.md)
- [vvaharness/orchestrator/entry.py](../prompt_representation/vvaharness/orchestrator/entry.py.sudo.md)
- [vvaharness/orchestrator/preflight.py](../prompt_representation/vvaharness/orchestrator/preflight.py.sudo.md)
- [vvaharness/orchestrator/scan.py](../prompt_representation/vvaharness/orchestrator/scan.py.sudo.md)
- [vvaharness/orchestrator/store/_db.py](../prompt_representation/vvaharness/orchestrator/store/_db.py.sudo.md)
- [vvaharness/orchestrator/store/_schema.py](../prompt_representation/vvaharness/orchestrator/store/_schema.py.sudo.md)
- [vvaharness/orchestrator/store/callgraph.py](../prompt_representation/vvaharness/orchestrator/store/callgraph.py.sudo.md)
- [vvaharness/orchestrator/store/replays.py](../prompt_representation/vvaharness/orchestrator/store/replays.py.sudo.md)
- [vvaharness/pipeline/stages/replay.py](../prompt_representation/vvaharness/pipeline/stages/replay.py.sudo.md)
- [vvaharness/pipeline/stages/s1_autoexclude.py](../prompt_representation/vvaharness/pipeline/stages/s1_autoexclude.py.sudo.md)
- [vvaharness/pipeline/stages/s2/__init__.py](../prompt_representation/vvaharness/pipeline/stages/s2/__init__.py.sudo.md)
- [vvaharness/pipeline/stages/s2/outcomes.py](../prompt_representation/vvaharness/pipeline/stages/s2/outcomes.py.sudo.md)
- [vvaharness/pipeline/stages/s2/prompts.py](../prompt_representation/vvaharness/pipeline/stages/s2/prompts.py.sudo.md)
- [vvaharness/pipeline/stages/s2/session.py](../prompt_representation/vvaharness/pipeline/stages/s2/session.py.sudo.md)
- [vvaharness/pipeline/stages/s2_planning.py](../prompt_representation/vvaharness/pipeline/stages/s2_planning.py.sudo.md)
- [vvaharness/pipeline/stages/s3_decompose.py](../prompt_representation/vvaharness/pipeline/stages/s3_decompose.py.sudo.md)
- [vvaharness/pipeline/stages/s4/outcomes.py](../prompt_representation/vvaharness/pipeline/stages/s4/outcomes.py.sudo.md)
- [vvaharness/pipeline/stages/s4/prompts.py](../prompt_representation/vvaharness/pipeline/stages/s4/prompts.py.sudo.md)
- [vvaharness/pipeline/stages/s4/session.py](../prompt_representation/vvaharness/pipeline/stages/s4/session.py.sudo.md)
- [vvaharness/pipeline/stages/s5/detectors.py](../prompt_representation/vvaharness/pipeline/stages/s5/detectors.py.sudo.md)
- [vvaharness/pipeline/stages/s6/outcomes.py](../prompt_representation/vvaharness/pipeline/stages/s6/outcomes.py.sudo.md)
- [vvaharness/pipeline/stages/s6/prompts.py](../prompt_representation/vvaharness/pipeline/stages/s6/prompts.py.sudo.md)
- [vvaharness/pipeline/stages/s6/session.py](../prompt_representation/vvaharness/pipeline/stages/s6/session.py.sudo.md)
- [vvaharness/pipeline/stages/s6_verify.py](../prompt_representation/vvaharness/pipeline/stages/s6_verify.py.sudo.md)
- [vvaharness/pipeline/stages/s7/outcomes.py](../prompt_representation/vvaharness/pipeline/stages/s7/outcomes.py.sudo.md)
- [vvaharness/pipeline/stages/s7/prompts.py](../prompt_representation/vvaharness/pipeline/stages/s7/prompts.py.sudo.md)
- [vvaharness/pipeline/stages/s7/session.py](../prompt_representation/vvaharness/pipeline/stages/s7/session.py.sudo.md)
- [vvaharness/pipeline/stages/s8/outcomes.py](../prompt_representation/vvaharness/pipeline/stages/s8/outcomes.py.sudo.md)
- [vvaharness/pipeline/stages/s8/prompts.py](../prompt_representation/vvaharness/pipeline/stages/s8/prompts.py.sudo.md)
- [vvaharness/pipeline/stages/s8/session.py](../prompt_representation/vvaharness/pipeline/stages/s8/session.py.sudo.md)
- [vvaharness/pipeline/stages/s8/validate.py](../prompt_representation/vvaharness/pipeline/stages/s8/validate.py.sudo.md)
- [vvaharness/pipeline/stages/s8_chain.py](../prompt_representation/vvaharness/pipeline/stages/s8_chain.py.sudo.md)
- [vvaharness/pipeline/stages/s9/typed_sarif.py](../prompt_representation/vvaharness/pipeline/stages/s9/typed_sarif.py.sudo.md)
- [vvaharness/plugins/semgrep/enricher.py](../prompt_representation/vvaharness/plugins/semgrep/enricher.py.sudo.md)
- [vvaharness/plugins/semgrep/plugin.py](../prompt_representation/vvaharness/plugins/semgrep/plugin.py.sudo.md)
- [vvaharness/plugins/semgrep/tools.py](../prompt_representation/vvaharness/plugins/semgrep/tools.py.sudo.md)
- [vvaharness/plugins/semgrep/triage.py](../prompt_representation/vvaharness/plugins/semgrep/triage.py.sudo.md)
- [vvaharness/remediation_agent/interactive/loop.py](../prompt_representation/vvaharness/remediation_agent/interactive/loop.py.sudo.md)
- [vvaharness/remediation_agent/models/change.py](../prompt_representation/vvaharness/remediation_agent/models/change.py.sudo.md)
- [vvaharness/remediation_agent/models/gates.py](../prompt_representation/vvaharness/remediation_agent/models/gates.py.sudo.md)
- [vvaharness/remediation_agent/models/verdict.py](../prompt_representation/vvaharness/remediation_agent/models/verdict.py.sudo.md)
- [vvaharness/remediation_agent/options.py](../prompt_representation/vvaharness/remediation_agent/options.py.sudo.md)
- [vvaharness/remediation_agent/playbook.py](../prompt_representation/vvaharness/remediation_agent/playbook.py.sudo.md)
- [vvaharness/remediation_agent/plugin_runner/__init__.py](../prompt_representation/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md)
- [vvaharness/remediation_agent/plugin_runner/handoff.py](../prompt_representation/vvaharness/remediation_agent/plugin_runner/handoff.py.sudo.md)
- [vvaharness/remediation_agent/policy/decide.py](../prompt_representation/vvaharness/remediation_agent/policy/decide.py.sudo.md)
- [vvaharness/remediation_agent/policy/postgate.py](../prompt_representation/vvaharness/remediation_agent/policy/postgate.py.sudo.md)
- [vvaharness/remediation_agent/policy_gate/action.py](../prompt_representation/vvaharness/remediation_agent/policy_gate/action.py.sudo.md)
- [vvaharness/remediation_agent/prompts.py](../prompt_representation/vvaharness/remediation_agent/prompts.py.sudo.md)
- [vvaharness/remediation_agent/report_augment/locate.py](../prompt_representation/vvaharness/remediation_agent/report_augment/locate.py.sudo.md)
- [vvaharness/remediation_agent/report_augment/markdown.py](../prompt_representation/vvaharness/remediation_agent/report_augment/markdown.py.sudo.md)
- [vvaharness/remediation_agent/report_parser/fields.py](../prompt_representation/vvaharness/remediation_agent/report_parser/fields.py.sudo.md)
- [vvaharness/remediation_agent/select/topspec.py](../prompt_representation/vvaharness/remediation_agent/select/topspec.py.sudo.md)
- [vvaharness/report/appcontext.py](../prompt_representation/vvaharness/report/appcontext.py.sudo.md)
- [vvaharness/report/cwe.py](../prompt_representation/vvaharness/report/cwe.py.sudo.md)
- [vvaharness/report/redact.py](../prompt_representation/vvaharness/report/redact.py.sudo.md)
- [vvaharness/rules/__init__.py](../prompt_representation/vvaharness/rules/__init__.py.sudo.md)
- [vvaharness/rules/kb_tools.py](../prompt_representation/vvaharness/rules/kb_tools.py.sudo.md)
- [vvaharness/sdk/handoff.py](../prompt_representation/vvaharness/sdk/handoff.py.sudo.md)
- [vvaharness/sdk/loading.py](../prompt_representation/vvaharness/sdk/loading.py.sudo.md)
- [vvaharness/sdk/stages.py](../prompt_representation/vvaharness/sdk/stages.py.sudo.md)
- [vvaharness/util/counters.py](../prompt_representation/vvaharness/util/counters.py.sudo.md)
- [vvaharness/util/environment.py](../prompt_representation/vvaharness/util/environment.py.sudo.md)
- [vvaharness/util/events.py](../prompt_representation/vvaharness/util/events.py.sudo.md)
- [vvaharness/util/logs.py](../prompt_representation/vvaharness/util/logs.py.sudo.md)
- [vvaharness/util/scan_progress.py](../prompt_representation/vvaharness/util/scan_progress.py.sudo.md)
- [vvaharness/validation/case_api.py](../prompt_representation/vvaharness/validation/case_api.py.sudo.md)
- [vvaharness/validation/cli/_parser.py](../prompt_representation/vvaharness/validation/cli/_parser.py.sudo.md)
- [vvaharness/validation/constants/artifacts.py](../prompt_representation/vvaharness/validation/constants/artifacts.py.sudo.md)
- [vvaharness/validation/constants/test_inventory.py](../prompt_representation/vvaharness/validation/constants/test_inventory.py.sudo.md)
- [vvaharness/validation/constants/tools.py](../prompt_representation/vvaharness/validation/constants/tools.py.sudo.md)
- [vvaharness/validation/report/augment.py](../prompt_representation/vvaharness/validation/report/augment.py.sudo.md)
- [vvaharness/validation/session/launch_prompt.py](../prompt_representation/vvaharness/validation/session/launch_prompt.py.sudo.md)
- [vvaharness/validation/session/launcher.py](../prompt_representation/vvaharness/validation/session/launcher.py.sudo.md)
- [vvaharness/validation/subagents/_frontmatter.py](../prompt_representation/vvaharness/validation/subagents/_frontmatter.py.sudo.md)
- [vvaharness/validation/tools/__init__.py](../prompt_representation/vvaharness/validation/tools/__init__.py.sudo.md)
- [vvaharness/validation/tools/_scope.py](../prompt_representation/vvaharness/validation/tools/_scope.py.sudo.md)
- [vvaharness/validation/tools/deep_tools.py](../prompt_representation/vvaharness/validation/tools/deep_tools.py.sudo.md)
- [vvaharness/validation/tools/diff_facts.py](../prompt_representation/vvaharness/validation/tools/diff_facts.py.sudo.md)
- [vvaharness/validation/tools/fact_specs.py](../prompt_representation/vvaharness/validation/tools/fact_specs.py.sudo.md)
- [vvaharness/validation/tools/pattern_scanner.py](../prompt_representation/vvaharness/validation/tools/pattern_scanner.py.sudo.md)
- [vvaharness/validation/tools/test_inventory.py](../prompt_representation/vvaharness/validation/tools/test_inventory.py.sudo.md)
- [inputs/remediation_playbook.yaml](../prompt_representation/inputs/remediation_playbook.yaml.sudo.md)
- [inputs/validator_hints.yaml](../prompt_representation/inputs/validator_hints.yaml.sudo.md)
- [inputs/design_controls.example.yaml](../prompt_representation/inputs/design_controls.example.yaml.sudo.md)
- [vvaharness/rules/generic.kb.yaml](../prompt_representation/vvaharness/rules/generic.kb.yaml.sudo.md)
- [vvaharness/skills/code-exploration/probe.sh](../prompt_representation/vvaharness/skills/code-exploration/probe.sh.sudo.md)
- [vvaharness/skills/iac/probe.sh](../prompt_representation/vvaharness/skills/iac/probe.sh.sudo.md)
- [vvaharness/skills/injection/probe.sh](../prompt_representation/vvaharness/skills/injection/probe.sh.sudo.md)
- [vvaharness/skills/ssrf/probe.sh](../prompt_representation/vvaharness/skills/ssrf/probe.sh.sudo.md)
- [vvaharness/skills/templates/probe.sh](../prompt_representation/vvaharness/skills/templates/probe.sh.sudo.md)
