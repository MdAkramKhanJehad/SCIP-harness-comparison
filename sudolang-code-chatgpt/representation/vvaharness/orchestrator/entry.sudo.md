# orchestrator/entry.py — scan command

Executable control flow. Imported helper internals remain boundaries unless
separately represented. Parser flags retain their source spellings.

```sudo
// Source: vvaharness/orchestrator/entry.py:56-60
On module import, attempt to set stdout and stderr encoding to UTF-8.
Ignore AttributeError and ValueError from that operation.

// Source: vvaharness/orchestrator/entry.py:63-69
fn _top_arg(raw) {
  Use _coerce_top_value(raw, source="--top").
  Convert its ValueError into argparse.ArgumentTypeError.
}

// Source: vvaharness/orchestrator/entry.py:72-100
fn _ev_gate(args, cfg) {
  path = ev_collection_path(os.environ)
  if (!path) {
    if (args.stop_after == "ev" && !args.resume) { yield [2, None] and end this call }
    yield [None, None] and end this call
  }
  if (config_mod.is_network_path(path)) { yield [2, None] and end this call }
  if (args.repo_file) { warn that EV is ignored for batch; yield [None, None] and end this call }
  Run ev_gate.run_gate(ev_load_options(cfg, os.environ)).
  On EVInputError, display the redacted error and yield [2, None].
  Otherwise print checks only when result.enabled; yield [None, result.collection].
}

// Source: vvaharness/orchestrator/entry.py:103-137
fn _resolve_auto_step1(flag, cfg, disable=false) {
  if (disable) { yield [false, "--no-auto-step1"] and end this call }
  if (flag) { yield [true, "--auto-step1"] and end this call }
  if (cfg.step1.auto_exclude, default false) { yield [true, "step1.auto_exclude"] }
  else { yield [false, None] }
}
fn _repo_name(repo, explicit) {
  Use stripped explicit name when nonempty, else resolved directory name, else "repo".
}
fn _pricing_note(cfg) {
  With no pricing.file, failed rate-table load, or no missing models, yield None.
  Otherwise warn for sorted distinct configured role model ids missing from the table;
  their cost reports as null. No model call is made here.
}

// Source: vvaharness/orchestrator/entry.py:140-223
fn build_parser() {
  Require exactly one of --repo and --repo-file.
  Accept --config (None), --repo-name, --application-id,
    --workspace ("./batch-workspace"), --keep-clones, --group-by-app, --resume,
    --s6-progress-file, --remediate, --top (_top_arg, default None), --force,
    --skip-preflight, --step1-config.
  --stop-after choices = ["clone", "ev", "s0", "s1", "s2", "s3", "s4", "s5",
    "s6", "s7", "s8", "s9", "s10", "s11"].
  --auto-step1 and --no-auto-step1 are mutually exclusive flags.
  Boolean action flags default false; other unspecified optional values default None.
  --step1-config versus --auto-step1 is resolved later, not a parser exclusion.
}

// Source: vvaharness/orchestrator/entry.py:226-304
fn main(argv=None) {
  args = build_parser().parse_args(argv)
  if (!args.repo_file) {
    Check the repo's stat mode is a directory; OSError, ValueError or nondirectory yields 2.
    repo_name = _repo_name(repo, args.repo_name)
  }
  config_explicit = args.config != None
  if (!config_explicit) { args.config = _default_config() }
  Apply trusted_config(args.config, boundary=args.repo, explicit=config_explicit), then config_mod.load.
  On ConfigPolicyError, log refusal and yield 2.
  if (args.s6_progress_file) { cfg.step6_verify.progress_file = true }
  Display effective config; set CMDB path relative to its directory.
  [args.auto_step1, auto_step1_src] = _resolve_auto_step1(args.auto_step1, cfg, args.no_auto_step1)
  if (args.step1_config) {
    Reject network path with code 2.
    Apply explicit step1 overlay; ConfigPolicyError, ValueError or not applied yields 2.
    args.auto_step1 = false
  }
  Missing CMDB only warns. Emit _pricing_note when present.

  // Source: vvaharness/orchestrator/entry.py:305-350
  configure_backends(cfg, cfg_dir)
  if (ev_resolution_error(cfg, args)) { log conflict; yield 2 and end this call }
  [rc, ev_collection_in] = _ev_gate(args, cfg)
  if (rc != None) { yield rc and end this call }
  if (!args.skip_preflight && args.stop_after not in ["clone", "ev"]) {
    _skip = empty set if single-repo && ev_may_run(cfg, os.environ), else EV_MODEL_ROLES
    _rem_on = args.remediate || cfg.step_remediate.enabled (default false)
    if (!(args.stop_after in [None, "s10", "s11"] && _rem_on)) { add "remediate" to _skip }
    if (!(args.stop_after in [None, "s11"] && cfg.step_validate.enabled (default false))) {
      add "validate" to _skip
    }
    if (!check_backends(cfg, skip_roles=_skip)) { yield 1 and end this call }
    KeyboardInterrupt here yields 130.
  }
  if (args.repo_file) {
    Reject a non-file list path with code 2.
    yield run_batch(list_file, args, cfg); StoreError here yields 2.
    End this call. run_batch internals are expanded in source_detail/vvaharness/orchestrator/batch.py.sudo.md.
  }

  // Source: vvaharness/orchestrator/entry.py:352-405
  Call scan_repo(repo, repo_name, args.application_id, args, cfg, ev_collection_in).
  Handle exceptions from this single-repo call in this order:
    KeyboardInterrupt: display abort, yield 130.
    AuthenticationError: log auth error/code/application id, advise doctor/resume, yield 1.
    ProxyError: log proxy error/code/application id, advise doctor, yield 1.
    EVUnreachableError or EVInputError: display redacted EV error, yield 2.
    StoreError: display error, yield 2.
    EmptyScopeError: log s1 empty_scope/application id, yield 2.
    Other Exception: display redacted failure, log scan error;
      print traceback only if VVAHARNESS_DEBUG is truthy; yield 1.
  On normal completion yield outcome.exit_code, including remediation/validation/degraded status.
}
```

The CLI dispatcher above this command, configuration loader, preflight routines,
and batch implementation are represented in the corresponding `source_detail/`
modules and summarized in `representation/harness.sudo.md`. Error handling scope above
matches the source; it is not a blanket handler around every startup operation.

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../prompt_workflow.sudo.md).

- [vvaharness/orchestrator/entry.py](../../../prompt_representation/vvaharness/orchestrator/entry.py.sudo.md)
