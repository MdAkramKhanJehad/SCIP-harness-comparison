# orchestrator/scan.py — nested scan workflow

Executable orchestration. Every stage and local helper now has a mirrored
definition under source_detail/. The `with_injected_skills` decorator is
expanded in source_detail/vvaharness/skills/__init__.py.sudo.md.

```sudo
// Source: vvaharness/orchestrator/scan.py:106-168
interface ScanOutcome { report_path; finding_count; exit_code = 0 }
fn _head_sha(repo) {
  Run git -C repo rev-parse HEAD with captured text and timeout 20 seconds.
  Yield stripped stdout only for exit 0; yield None on other status or any Exception.
}
fn _config_file_sha256(config_path) {
  Yield SHA-256 of raw config bytes; OSError yields None.
}
fn _ledger_imbalance(s5_out_count, verified, dropped) {
  s6_discovered_verified = count verified with origin == "s6_discovered"
  clones = count verified with is_repeat_clone
  s6_dropped_from_s5 = count dropped whose chunk_id does not end with "+s6"
  accounted = len(verified) - s6_discovered_verified - clones + s6_dropped_from_s5
  if (accounted == s5_out_count) { yield None }
  else { yield a message distinguishing missing rows from excess/double-counted rows }
}
fn _verified_counts(verified) {
  tps = verified rows with verdict == "TRUE_POSITIVE"
  yield [len(tps), count tps with origin == "s6_discovered",
    count tps with is_repeat_clone, len(verified) - len(tps)]
}
fn _verified_order(verified) {
  Sort by [file, line_start, line_end, cwe or "", vuln_class or "", title or "", chunk_id or ""].
}

// Source: vvaharness/orchestrator/scan.py:171-211
fn _prune_ev_replays(run_id, canonical, ctx) {
  if (!ctx.ev_collection) { end this call }
  Prune replay bundles to replay_key of canonical findings.
  Any Exception only logs a warning with its type.
}
fn _ev_collection_in(repo, args, ckpt_dir, run_id, collection_in=None) {
  if (ev_options.collection_path(os.environ)) {
    if (collection_in == None) { log skipping EV; yield [None, false] }
    else { yield [collection_in, false] }
    End this call; do not fall back to a checkpoint in this branch.
  }
  if (!args.resume) { yield [None, false] and end this call }
  col = load_ckpt(ckpt_dir, run_id, EV_COLLECTION_STEP)
  if (col == None) { log only when stop_after == "ev"; yield [None, false] }
  else { log EV re-enabled from checkpoint; yield [col, true] }
}

// Source: vvaharness/orchestrator/scan.py:214-284
fn _ev_prep(repo, args, cfg, ckpt_dir, run_id, collection_in=None) {
  if (ev_options.profile_disabled(cfg)) { yield None and end this call }
  [col_in, resumed] = _ev_collection_in(repo, args, ckpt_dir, run_id, collection_in)
  if (col_in == None) {
    if (ev_options.required(cfg)) { raise EVInputError for required collection missing }
    yield None and end this call
  }
  opts = ev_options.load_options(cfg, os.environ, resumed_collection=resumed)
  if (!opts.enabled) { yield None and end this call }
  if (ev_options.model_preflight(cfg) reports error) { raise EVInputError }
  if (resumed) { run ev_gate.run_gate(opts, os.environ, collection=col_in); display its checks }
  else { save_ckpt(ckpt_dir, run_id, EV_COLLECTION_STEP, col_in) }
  col = ev_probe.run_probe(col_in, opts,
    allow_state_changing=bool(ev_options.ev_section(cfg).allow_state_changing_methods))
  if (col == None) { yield None and end this call }
  _ev_oob_selftest(opts)
  yield col.model_dump()
}
fn _ev_oob_selftest(opts) {
  mgr = resolve_oob(opts)
  if (!mgr.enabled) { log listener off unless oob_mode is "off"; end this call }
  Start mgr, run self_test, log reachable or not reachable.
  Always stop mgr on exit from this start/test block.
}

// Source: vvaharness/orchestrator/scan.py:287-299
fn _hydrate_ctx_callgraph_from_store(run_id, ctx, steps) {
  for each step in steps, in supplied order {
    graph = _store.load_callgraph(run_id, step)
    if (graph) { yield ctx.model_copy(update={call_graph: graph.call_graph}) and end this call }
  }
  yield ctx
}

// Source: vvaharness/orchestrator/scan.py:302-360
fn _upload_to_ingest(md_path, sarif_path, repository_name, application_id, cfg, cfg_dir) {
  url = cfg.output.ingest_url, default None
  token = cfg.output.ingest_token, default None
  if (!url || !token || either report file is missing) { log reason; yield false and end this call }
  verify = cfg.output.ingest_verify
  if (verify == None) { verify = cfg.sdk.verify_ssl, default true }
  verify = coerce_verify(verify)
  if (verify is a string) {
    Resolve it against cfg_dir.
    if (that path does not exist) { log missing CA; yield false and end this call }
  }
  Open both report files as binary; use httpx.Client(timeout=60, verify=verify).
  POST url with Bearer token, accept application/json, repositoryName,
    applicationId only when truthy, multipart file (Markdown) and sarifFile (JSON).
  No destination restriction is applied by this function.
  if (HTTP status >= 400) { log status and first 500 response characters; yield false }
  else { log success; yield true }
  Any Exception in the open/client/post block logs nonfatal failure and yields false.
}

// Source: vvaharness/orchestrator/scan.py:363-376
fn _recorded_stage_outcome(step_id, fallback) {
  Use recorded STAGES outcome unless absent, "running" or "not_run"; otherwise fallback.
}
fn _artifact_module_name(repo_name) {
  Replace each character except alphanumeric, dot, underscore or hyphen with underscore.
  Yield "repo" when result is empty or consists only of dots; otherwise the result.
}

// Source: vvaharness/orchestrator/scan.py:379-443
fn scan_repo(repo, repo_name, application_id, args, cfg, path_prefix=None, ev_collection_in=None) {
  Apply source decorator with_injected_skills around this call, including its scoped cleanup.
  run_id = run_id_for(repo)
  ckpt_dir = _store.state_root() / "checkpoints" / run_id
  _store.register_run(run_id, repo_root=resolved repo, repo_name, app_id=application_id)
  if (!args.resume && args.stop_after != "ev") { _store.reset_run(run_id) }
  repo_head = _head_sha(repo)
  if (args.resume && repo_head) {
    prior_head = load_ckpt(ckpt_dir, run_id, REPO_IDENTITY_STEP)
    if (prior_head is a nonempty string && prior_head != repo_head) { _store.reset_run(run_id) }
  }
  if (repo_head) { save_ckpt(ckpt_dir, run_id, REPO_IDENTITY_STEP, repo_head) }
  out_dir = artifact_dir(repo, SCAN_DIR_NAME)
  rem_rc = 0
  if (args.resume && ckpt_dir resolves inside repo) {
    Display refusal; yield ScanOutcome(None, 0) and end this call.
    The default exit_code remains 0 in this refusal branch.
  }
  Record wall-clock start and ISO start_ts.
  Build out_path and sarif_path using _artifact_module_name(repo_name), start_ts with colons/hyphens removed,
    suffixes _report.md and _report.sarif under out_dir.
  Configure timestamped error log under out_dir before any stages.
  ev_collection = _ev_prep(repo, args, cfg, ckpt_dir, run_id, ev_collection_in)
  if (args.stop_after == "ev") { yield ScanOutcome(None, 0) and end this call }

  // Source: vvaharness/orchestrator/scan.py:445-503
  if (args.auto_step1, default false) {
    Ensure owner-only checkpoints/run_id state directory; auto_path = ckpt_dir / "step1.yaml".
    if (!(args.resume && auto_path.is_file())) {
      Run s1_autoexclude.run(repo, cfg, out_path=auto_path) in s1-autoexclude token phase.
      On halt-class Exception rethrow; on other Exception log, set auto_path=None and continue.
    } else {
      Parse stored YAML, default empty object.
      if (stored is a dictionary) {
        Re-vet exclude_dirs, exclude_exts, exclude_globs using vet_overlay and config_dedup using vet_config_dedup.
        When vetoes or dedup changes exist, update these fields, remove empty config_dedup,
          and rewrite the stored overlay with generated-file header.
      }
    }
    if (auto_path && auto_path.is_file()) {
      Deep-copy cfg._data into a fresh Config, preventing batch-target accumulation.
      Apply overlay with expand=false so model-authored ${...} stays literal.
    }
  }

  // Source: vvaharness/orchestrator/scan.py:505-567
  tracker = ScanProgress.from_cfg(cfg, repo_name)
  Set active tracker; cfg._data["_scan_progress"] = tracker.
  Define nested _sp_start: report stage start only when tracker.enabled.
  Define nested _sp_done: mark STAGES for outcomes other than completed/error;
    on cached, load stage provenance into CACHED_PROVENANCE when available;
    report actual recorded outcome via _recorded_stage_outcome when tracker.enabled.
  Display role model ids/routes; cfg_dir = parent of resolved args.config.
  Load CVEs and controls from paths resolved against cfg_dir; load optional app profile/info.
  Resolve role model ids and routes, load cached pricing, hash raw config bytes.
  Define nested _save_stage_provenance: store role model/route, raw config hash and
    stage_token_bucket from current TOKENS snapshot. S1 bucket includes auto-exclusion.

  // Source: vvaharness/orchestrator/scan.py:569-614
  seed = load_ckpt(ckpt_dir, run_id, "s0") if args.resume, else None
  if (seed == None) {
    Run s0_seed.run(str(repo), cfg, ckpt_dir) in s0 stage/token phase.
    Save s0 checkpoint and provenance; record completion.
  } else { record s0 cached }
  _store.save_callgraph(run_id, "s0", seed)
  _plugins = load_plugin_set(cfg)
  _plugins.install_graph_tools()
  graph_dir = unique state directory graphs/run_id/uuid4.hex
  graph_handle = build_graph(str(repo), run_id, graph_dir, enrichers=_plugins.contribution.enrichers)
  From here through the workflow below, on every exit stop tracker, close a truthy graph_handle,
    and remove graph_dir with ignore_errors=true. Earlier failures are outside this cleanup block.
  if (args.stop_after == "s0") { yield ScanOutcome(None, 0) and end this call }

  ctx = load_ckpt(ckpt_dir, run_id, "s1") if args.resume, else None
  if (ctx == None) {
    Run s1_preprocess.run(str(repo), cfg, cves, controls, seed, graph_handle) in s1 stage/token phase.
    Save s1 checkpoint and provenance; record completion.
  } else { record s1 cached }
  Save s1 callgraph; hydrate ctx from [s1, s0], first stored hit.
  Attach app_profile, ev_collection and live graph_handle to ctx.
  if (args.stop_after == "s1") { yield ScanOutcome(None, 0) and end this call }

  // Source: vvaharness/orchestrator/scan.py:616-668
  tm = load_ckpt(ckpt_dir, run_id, "s2") if args.resume, else None
  s2_reran = false
  if (tm == None) {
    s2_reran = true
    Run s2.run(str(repo), repo_name, cfg, cves, controls, ctx, app_profile) in s2 stage/token phase.
    if (tm.threats || tm.assets || tm.trust_boundaries) { save s2 checkpoint and provenance }
    else { bump s2_degraded counter }
    Record completion.
    On S2HollowAfterRetry: bump degraded, log reason, record error, stop tracker,
      display failure; yield ScanOutcome(None, 0, 1) and end this call.
    On other Exception: rethrow halt errors; otherwise warn, log unless already_logged,
      record redacted error, bump degraded, set tm=None, and continue.
  } else { record s2 cached }
  ctx.threat_model = tm
  Save s2 callgraph; hydrate ctx from [s2, s1, s0].
  if (args.stop_after == "s2") { yield ScanOutcome(None, 0) and end this call }

  // Source: vvaharness/orchestrator/scan.py:670-725
  manifest = load s3 only if args.resume && !s2_reran, else None
  s3_resumed = manifest != None
  if (manifest == None) {
    Run s3_decompose.run(ctx, cfg) in s3 stage/token phase; save checkpoint/provenance; record completion.
  } else { record s3 cached }
  Save s3 callgraph.
  if (args.stop_after == "s3") { yield ScanOutcome(None, 0) and end this call }

  s4_ckpt = load s4 only if args.resume && s3_resumed, else None
  if (s4_ckpt != None && !(s4_ckpt is dictionary && s4_stage_complete(s4_ckpt))) {
    Warn that prior S4 was degraded; s4_ckpt = None.
  }
  s4_resumed = s4_ckpt != None
  unit_outcomes = {}; external_input = false
  if (s4_ckpt == None) {
    [findings, unit_outcomes] = s4_deepdive.run(manifest.sorted_units(), ctx, cfg)
    Run that call in s4 stage/token phase; save {findings, outcomes:unit_outcomes} and provenance.
    Record completion.
  } else {
    findings = s4_ckpt.get("findings", [])
    unit_outcomes = s4_ckpt.get("outcomes", {})
    external_input = s4_input_kind(s4_ckpt) == "external"
    Record s4 cached.
  }
  Save s4 callgraph.
  if (args.stop_after == "s4") { yield ScanOutcome(None, 0) and end this call }
  s4_count = len(findings)

  // Source: vvaharness/orchestrator/scan.py:726-807
  s7_ckpt = load s7 only if args.resume && s4_resumed, else None
  legacy_s7_note = ""
  if (s7_ckpt == None) {
    s5_ckpt = load s5 only if args.resume && s4_resumed, else None
    s5_resumed = s5_ckpt != None
    if (s5_ckpt == None) {
      [findings, pre_dropped] = s5.run(findings, ctx, cfg)
      Run in s5 stage/token phase; save {findings, pre_dropped} and provenance; record completion.
    } else { restore findings and pre_dropped; record s5 cached }
    if (args.stop_after == "s5") { yield ScanOutcome(None, 0) and end this call }

    s6_ckpt = load s6 only if args.resume && s5_resumed, else None
    if (s6_ckpt == None) {
      Hydrate ctx from [s4, s3, s2, s1, s0].
      In s6 stage/token phase:
        if (ctx.ev_collection) { [verified, dropped] = ev_router.run(findings, ctx, cfg, run_id) }
        else { [verified, dropped] = s6_verify.run(findings, ctx, cfg, run_id) }
      verified = _verified_order(verified)
      Save {verified, dropped} as s6 and provenance; record completion.
    } else { verified = _verified_order(s6_ckpt.verified); restore dropped; record s6 cached }
    if (args.stop_after == "s6") { yield ScanOutcome(None, 0) and end this call }

    Hydrate ctx from [s4, s3, s2, s1, s0].
    [canonical, dup_dropped] = s7_dedup.run(verified, cfg, ctx), in s7 stage/token phase
    Record s7 completion; _prune_ev_replays(run_id, canonical, ctx).
    s5_out_count = len(findings)
    Save s7 tuple [pre_dropped, verified, dropped, canonical, dup_dropped, s5_out_count], then provenance.
    Display resume command including application id only when supplied.
  } else {
    // Source: vvaharness/orchestrator/scan.py:808-846
    if (len(s7_ckpt) == 6) { restore all six fields }
    else if (len(s7_ckpt) == 5) {
      Restore first five; s5_out_count=None.
      legacy_s7_note = "s5 post-enrich count unavailable for the finding ledger balance check (legacy checkpoint)"
    } else {
      Unpack as four fields [verified, dropped, canonical, dup_dropped]; pre_dropped=[]; s5_out_count=None.
      legacy_s7_note = "s5 drop audit unavailable (legacy checkpoint)"
      This is the source's fallback, not a check accepting every other tuple length.
    }
    Record s5, s6 and s7 cached.
  }
  if (args.stop_after in ["s5", "s6"]) { yield ScanOutcome(None, 0) and end this call }
  _enrich_findings(canonical, app_info, path_prefix)
  all_dropped = pre_dropped + dropped + dup_dropped
  raw_count = s5_out_count if not None, else s4_count
  if (s5_out_count != None) {
    ledger_msg = _ledger_imbalance(s5_out_count, verified, dropped)
    if (ledger_msg) { warn; log s6-verify recovered=true; continue }
  }
  Save s7 callgraph.
  if (args.stop_after == "s7") { yield ScanOutcome(None, 0) and end this call }

  // Source: vvaharness/orchestrator/scan.py:848-959
  Hydrate ctx from [s4, s3, s2, s1, s0].
  s7_resumed = s7_ckpt != None
  report = load s8 only if args.resume && s7_resumed, else None
  if (report == None) {
    Build metrics from ctx, manifest, timing, raw_count, FALSE_POSITIVE drops,
      _verified_counts, duplicate count, unit_outcomes, external_input, role models and pricing.
    report = s8_chain.run(canonical, ctx, cfg, dropped=all_dropped, raw_findings_count=raw_count, metrics)
    Run in s8 stage/token phase; refresh token metrics AFTER s8's spend.
    Attach repo_name, tm, app_profile, manifest.threats_without_unit_for(tm), current git_sha.
    if (cfg.output.emit_unreachable_appendix, default false) { attach manifest.unreachable_files }
    Save s8 checkpoint and provenance; record completion.
  } else { record s8 cached }
  Save s8 callgraph.
  Append legacy_s7_note once when nonempty and absent; set report.degraded=true when appended.
  for each stage id in [s2, s4, s6] {
    if (STAGES recorded outcome == "error") {
      Append once a failure clause with last redacted stage error if available;
      set degraded when appended. Collect failed stage id.
    }
  }
  If any such stages failed, display investigation-incomplete warning.
  Count "halted" unit_outcomes; when nonzero append its clause once and set degraded.
  degraded_rc = 1 if report.degraded, else 0
  mint_case_ids(report) BEFORE any following report persistence; errors propagate.
  Create output directory; write_findings_json(report, repo).
  md_text = redact(report.to_markdown(
    posture_channel=bool(knob(cfg, "output.posture_channel", true)),
    unreachable_appendix=bool(knob(cfg, "output.emit_unreachable_appendix", false))))
  Write md_text to out_path, report redaction counts.
  if (args.stop_after == "s8") { yield ScanOutcome(out_path, len(report.findings), rem_rc or degraded_rc) and end this call }

  // Source: vvaharness/orchestrator/scan.py:961-993
  s9_done = load s9 if args.resume, else None
  if (s9_done == None || !sarif_path.exists()) {
    Run s9_sarif.run(report, sarif_path, application_id, app_info, cfg) in s9 stage.
    Save string sarif_path as s9; record completion. No s9 provenance is saved here.
  } else { record s9 cached }
  Save s9 callgraph.
  ingest_done = load ingest checkpoint if args.resume, else None
  if (!ingest_done) {
    ok = _upload_to_ingest(out_path, sarif_path, repo_name, application_id, cfg, cfg_dir)
    if (ok) { save ingest=true checkpoint }
  }
  if (args.stop_after == "s9") { yield ScanOutcome(out_path, len(report.findings), rem_rc or degraded_rc) and end this call }

  // Source: vvaharness/orchestrator/scan.py:995-1072
  rem_on = args.remediate || cfg.step_remediate.enabled (default false)
  if (!(rem_on && report.findings)) { record s10 disabled }
  else {
    rem_err = _remediate_preflight(cfg, args, repo, report)
    if (rem_err) { display/log error; record disabled; do not change rem_rc }
    else {
      rem_rc = _run_remediation(report, repo, cfg, ckpt_dir, run_id,
        resume=args.resume, top=args.top, report_md=out_path, progress=rem_progress)
      Run in s10 stage/token phase; record attempted/fixed/not_fixed counters; warn on nonzero rem_rc.
    }
  }
  if (args.stop_after == "s10") { yield ScanOutcome(out_path, len(report.findings), rem_rc or degraded_rc) and end this call }
  val_rc = 0
  val_on = cfg.step_validate.enabled (default false)
  if (!(val_on && report.findings)) { record s11 disabled }
  else {
    val_err = _validate_preflight(cfg)
    if (val_err) { display/log error; record disabled; do not change val_rc }
    else {
      val_rc = _run_validation(repo, cfg, config_path=args.config, resume=args.resume,
        report_md=out_path, progress=val_progress)
      Run in s11 stage/token phase; record validated/passed/failed counters.
    }
  }
  if (args.stop_after == "s11") { yield ScanOutcome(out_path, len(report.findings), rem_rc or val_rc or degraded_rc) and end this call }
  Display elapsed time, findings/dropped/chains, token totals or unavailable, report path; print md_text.
  yield ScanOutcome(out_path, len(report.findings), rem_rc or val_rc or degraded_rc)
  Execute the cleanup described after graph construction on every exit from that protected region.
}

// Source: vvaharness/orchestrator/scan.py:1075-1144
fn _run_remediation(report, repo, cfg, ckpt_dir, run_id, resume=false, top=None, report_md=None, progress=None) {
  Create artifact_dir(repo, REMEDIATION_DIR_NAME).
  eff_top = resolve_top(top, cfg)
  selected = select_top_logged(drop_non_main_channel(report.findings), eff_top,
    score_of=wrapped finding.cvss_score)
  Filtering precedes the cap. Extract underlying findings in selected order.
  Warn fix mode for routes cli/sdk/deepagents; otherwise warn backend cannot edit;
    neither warning prevents process_targets from being called.
  layout = Layout(rem_dir, ckpt_dir, run_id)
  opts = RemediateOptions(resume=resume, mode="fix")
  Build RemediationTarget for each selected finding with fresh 1-based display index.
  yield process_targets(targets, layout, cfg, repo_path=repo, opts, report=report_md,
    progress only when not None)
}
fn _run_validation(repo, cfg, config_path, resume=false, report_md=None, progress=None) {
  rc = s11_run(repo, cfg, config_path, resume, report_md, progress only when not None)
  Warn when rc != 0; yield rc.
}
fn _progress_detail(progress, fields) { join field=progress.get(field, 0) entries with spaces }

// Source: vvaharness/orchestrator/scan.py:1147-1193
fn _remediate_preflight(cfg, args, repo, report) {
  Missing models.remediate yields an error string.
  UnsafeArtifactDir from artifact_dir(repo, REMEDIATION_DIR_NAME) yields its error string.
  Resolve remediation model/route/provider; failed _backend_credential_ok yields error string.
  cur = _head_sha(repo)
  if (report.git_sha && cur && report.git_sha != cur && !args.force) { yield HEAD-moved error }
  else { yield None }
}
fn _validate_preflight(cfg) {
  val = validate_model_spec(cfg)
  if (val == None) { yield missing models.validate.orchestrator error and end this call }
  Resolve val; normalize_validate_backend(via, provider).
  Yield None if _backend_credential_ok succeeds, else its role/route/detail error string.
}
```

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../prompt_workflow.sudo.md).

- [vvaharness/orchestrator/scan.py](../../../prompt_representation/vvaharness/orchestrator/scan.py.sudo.md)
