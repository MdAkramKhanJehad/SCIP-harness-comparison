# vvaharness/config/profiles/default.yaml

The packaged default profile: every model role runs via `deepagents` on Anthropic, Stage 10 (remediation) and Stage 11 (validation) are disabled. This file is rendered in full. The other four profiles (`full`, `sdk`, `semgrep`, `taint`) are rendered as differences from this one.

The loader (`vvaharness/config/__init__.sudo`, `load`) merges this file over `_STEP_DEFAULTS`, so a key that is absent here takes the `_STEP_DEFAULTS` value, and a key present here wins over it. `${NAME}` and `${NAME:-default}` are expanded from the environment at load time under the secret-name policy.

Source: `vvaharness/config/profiles/default.yaml` (lines 1-429)
Executor: code (data read by `knob(...)` and `getattr(cfg...)` across all stages)
Called from: `vvaharness/config/__init__.py` load (selected with `--config` or the packaged default)

// src: vvaharness/config/profiles/default.yaml:15-27
// Profile notes (comments in the file, not settings):
//   "Packaged default: every role via:deepagents on Anthropic. S10/S11 disabled."
//   max_turns meaning is backend-dependent: on via:sdk / via:cli / via:openai a HARD per-session turn cap
//   ("Exhausting it fails the stage, and the pipeline continues without it (findings silently drop toward 0)");
//   on via:deepagents "a langgraph recursion limit of max_turns + 900, i.e. a FLOOR, not a ceiling".
//   "Every value below was tuned against deepagents."

## Model roles

// src: vvaharness/config/profiles/default.yaml:28-69
Options models {
  autoexclude:  { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }
  preprocess:   { id: "claude-sonnet-4-6", via: "deepagents", provider: "anthropic" }
  threatmodel:  { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }
  decompose:    { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }
  deepdive:     { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }
  verify:       { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }
  dedup:        { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }
  chain:        { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }
  remediate:    { id: "claude-opus-4-8",   via: "deepagents", provider: "anthropic" }   // S10 fix mode edits files in the target repository
  validate: {
    orchestrator:        { id: "claude-opus-5", via: "deepagents", provider: "anthropic" }
    security_architect:  { id: "claude-opus-4-8" }
    penetration_tester:  { id: "claude-opus-4-8" }
    cross_repo_analyzer: { id: "claude-opus-4-8" }
  }
  exploit_verification: {
    attacker: { id: "claude-opus-4-7",   via: "deepagents", provider: "anthropic" }   // optional; needs sdk, openai or deepagents, never cli
    judge:    { id: "claude-opus-4-8",   via: "deepagents", provider: "anthropic" }   // the confirmation authority
    classify: { id: "claude-sonnet-4-6", via: "deepagents", provider: "anthropic" }
    mapper:   { id: "claude-sonnet-4-6", via: "deepagents", provider: "anthropic" }   // falls back to classify when omitted
  }
}

## Transport blocks

// src: vvaharness/config/profiles/default.yaml:71-99
Options transport {
  sdk: {
    api_key: "${ANTHROPIC_SDK_API_KEY}", base_url: "${ANTHROPIC_SDK_BASE_URL}"
    verify_ssl: true, ca_cert: "${ANTHROPIC_SDK_CA_CERT}", client_cert: "${ANTHROPIC_SDK_CLIENT_CERT}"
    cache_markers: "on"     // the ONLY cache-marker switch for via: deepagents
  }
  openai: {
    api_key: "${OPENAI_API_KEY}", base_url: "${OPENAI_BASE_URL}"
    verify_ssl: true, ca_cert: "${OPENAI_CA_CERT}"
  }
  cli: {
    verify_ssl: true, ca_cert: "${CLAUDE_CLI_CA_CERT}"   // exported as NODE_EXTRA_CA_CERTS
    effort: "high"          // passed as --effort
    mcp_tools: true         // false is refused at preflight when the deepdive role is via: cli
    restricted: true        // pass --restricted: the only read jail on via: cli
  }
}

// src: vvaharness/config/profiles/default.yaml:101-108
Options caching {
  cache_markers: "on"
  cache_min_block_tokens: null
  cache_route: "anthropic"  // differs from _STEP_DEFAULTS "auto"; "anthropic" always sends Anthropic-shaped markers
}

## Stage settings

// src: vvaharness/config/profiles/default.yaml:110-112
Options step0 { callgraph_detection: "rules", min_graph_nodes_for_gate: 10 }

// src: vvaharness/config/profiles/default.yaml:114-163
Options step1 {
  auto_exclude: true                         // the model-written exclusion overlay is ON in the default profile (_STEP_DEFAULTS: false)
  auto_exclude_protect_templates: true
  auto_exclude_protect_key_material: true
  auto_exclude_protect_secrets: true
  auto_exclude_protect_client_sinks: true
  auto_exclude_max_tokens: 8000
  auto_exclude_effort: "high"
  allowed_tools: ["Read", "Grep"]
  exclude_dirs: [".vs", ".settings", ".vscode", ".idea", "node_modules"]
  exclude_exts: [".msi", ".nupkg", ".pdb", ".lib", ".aar", ".ser", ".pbix", ".p12", ".pfx", ".jks", ".der", ".cer",
                 ".doc", ".docx", ".xls", ".xlsx", ".xlsm", ".bmp", ".sqlite", ".db"]
  exclude_globs: ["**/._*"]
  max_file_kb: 1024
  follow_symlinks: false
  config_dedup: {
    enabled: true, min_cluster_size: 5, keep_per_top_dir: true
    promote_on_secret_hit: true              // never drop a file holding a literal credential
    promote_on_insecure_value: true
  }
}

// src: vvaharness/config/profiles/default.yaml:165-206
Options step2 {
  max_threats: 50, max_assets: 40, max_trust_boundaries: 60
  baseline: "auto"
  empty_retry: true                          // re-run once on zero threats on a non-empty repo or schema failure
  max_tokens: 64000, effort: "high"
  max_turns: 20
  max_model_calls: 4                         // the last call keeps only ThreatModel (0 = unmetered)
  deadline: 400, replay_timeout: 300, replay_max_tokens: 16000
  timeout: 900
  allowed_tools: ["Read", "Grep"]
  bash: false
  graph_tools: true, graph_tool_budget: 12
  planning: false                            // true requires a write_todos plan first (deepagents only)
  require_graph: true, require_graph_rejections: 2
  skills: true
  max_doc_chars: 32000, max_manifest_chars: 4000, max_manifest_total_chars: 32000
  max_manifests: 12, max_manifests_per_kind: 2, max_manifest_depth: 3
  max_prompt_modules: 100, max_prompt_entry_points: 400, max_inventory_files: 1200
  max_api_artefacts: 100, max_config_reps: 80, max_config_rep_chars: 2000, max_config_rep_bodies: 12
  max_modules: 100, max_entry_points: 400
  max_graph_files: 220, max_graph_sinks: 100, max_graph_edges: 100
  // resume_timeout absent here: _STEP_DEFAULTS supplies 300
}

// src: vvaharness/config/profiles/default.yaml:208-232
Options step4 {
  parallel: 12, batch_size: 4
  max_tokens: 64000, effort: "high"
  max_turns: 15, max_model_calls: 8
  deadline: 600, replay_timeout: 90, replay_max_tokens: 16000, resume_timeout: 90
  cwe_tools: true, cwe_tool_budget: 8, graph_tool_budget: 16
  require_graph: true
  evidence_gate: true, evidence_gate_refusals: 3
  planning: false
  skills: true
  inline_source: true                        // LARGE units are never inlined
  bash: false
  line_bucket: 5
  max_extra_cwes: 2
  max_findings_per_run: 50
  split_retry: true
  // allowed_tools absent here: _STEP_DEFAULTS supplies ("Read", "Glob", "Grep")
}

// src: vvaharness/config/profiles/default.yaml:234-241
Options step5 {
  step5_prefilter: { sink_reanchor: true, sink_reanchor_max_move_lines: 40, line_tolerance: 5 }
  step5_detectors: { enabled: true, max_rows: 200 }
}

// src: vvaharness/config/profiles/default.yaml:243-269
Options step6_verify {
  parallel: 7, batch_size: 4
  max_tokens: 32000, effort: "high"
  max_turns: 20, max_model_calls: 12
  batch_deadline: 530, replay_timeout: 60, replay_max_tokens: 12000, resume_timeout: 90
  batch_wall_clock_ceiling: 900
  split_retry: true
  min_confidence: 5
  trait_stamps: true, reframe_enabled: false
  inline_source: true
  graph_tools: true, graph_tool_budget: 20
  require_graph: false, evidence_gate_refusals: 3
  max_budget_usd: 10.0
  progress_file: false
  allowed_tools: ["Read", "Grep"]            // Glob dropped: the file list is already in the prompt
  // tool_timeout_s commented out: _STEP_DEFAULTS null (vendor default)
}

// src: vvaharness/config/profiles/default.yaml:271-318
Options step6_exploit_verification {          // live attack traffic; exploit verification package excluded from this rendering
  enabled: "auto"
  on_unreachable: "drop"                     // drop | warn | abort; abort disables exploit verification, never the static scan
  timeout_s: 15, safe_mode: true
  allow_state_changing_methods: true         // differs from _STEP_DEFAULTS false
  ev_overrides_static: false
  max_requests_per_finding: 200, max_payloads_per_finding: 25
  rate_limit_rps: 0, max_concurrency_target: 8, max_concurrency_endpoint: 4
  parallel: 5, store_probes: false, oob: "auto", ev_replay_variants: true
  on_auth_failure: "degrade", auth_expiry_skew_s: 60, max_reauth: 3
  classify: { batch: 10, parallel: 5, effort: "high" }
  mapper: { max_turns: 20, parallel: 4, effort: "high", endpoint_index: { chunk: 10 }, finding_map: { chunk: 6, max_endpoints: 5 } }
  attacker: { enabled: true, max_turns: 15, max_tool_result_chars: 12000, effort: "high" }
  judge: { max_tokens: 4000, max_records: 24, effort: "high" }
}

// src: vvaharness/config/profiles/default.yaml:320-325
Options step7_dedup { line_tolerance: 5, per_sink_keep: true, semantic: false, max_tokens: 64000, effort: "high" }

// src: vvaharness/config/profiles/default.yaml:327-340
Options step8 {
  severity_lift_gate: true, chain_quality_checks: true, chain_dedup: true, prompt_fact_blocks: true
  max_model_calls: 1, max_turns: 2
  deadline: 600, replay_timeout: 300, replay_max_tokens: 16000
  max_tokens: 48000, effort: "high"
  timeout: 1800
  prompt_token_budget: 100000
}

// src: vvaharness/config/profiles/default.yaml:342-343
Options step9 { duplicate_result_guard: true }

// src: vvaharness/config/profiles/default.yaml:345-359
Options step_remediate {
  enabled: false
  enforce_policy: true
  policy_file: null                          // null or a missing path (WARN) uses the bundled policy
  playbook_file: null
  top_n_findings: 5
  max_budget_usd: 10.0, max_turns: 40
  max_model_calls: 20                        // the last call keeps only the verdict
  timeout: 3600
  allowed_tools: ["Read", "Grep", "Edit", "Write"]
}

// src: vvaharness/config/profiles/default.yaml:361-373
Options step_validate {
  enabled: false, effort: "high"
  max_turns: 50, max_budget_usd: 15.0, max_findings: 20
  timeout: 3600                              // the S11 bound every route honours
  max_model_calls: 60                        // per reviewer persona, then a forced final report turn
  orchestrator_max_model_calls: 40
  allowed_tools: ["Read", "Grep", "Glob"]
}

## Inputs, batch, progress, output

// src: vvaharness/config/profiles/default.yaml:375-384
Options inject {
  cve_file: "../../../inputs/known_cves.json"
  controls_file: "../../../inputs/design_controls.yaml"
  cmdb_file: "../../../inputs/cmdb.csv"
  // pricing block commented out: no price table bundled
}

// src: vvaharness/config/profiles/default.yaml:386-400
Options batch {
  git_token: "${GITHUB_TOKEN}", git_base_url: "${GIT_BASE_URL}"
  skip_repo_patterns: ["*automation*", "*-playwright*", "*-selenium*", "*-karate*", "*perf-script*",
                       "*perf-test*", "*test-buddy*", "*-e2e*", "*-mock-*"]   // case-insensitive globs on RepoName; never cloned or scanned
}

// src: vvaharness/config/profiles/default.yaml:402-410
Options scan_progress { enabled: true, style: "compact" }   // compact | verbose | summary_only | stage_only | llm_debug | live

// src: vvaharness/config/profiles/default.yaml:412-422
Options output {
  posture_channel: true, emit_unreachable_appendix: false
  preserve_on_cleanup: ["security-scan", "security-remediation"]
  ingest_url: "${VVAHARNESS_INGEST_URL:-}", ingest_token: "${VVAHARNESS_INGEST_TOKEN:-}"
  ingest_verify: "${VVAHARNESS_INGEST_VERIFY:-true}"   // a CA path that does not exist skips the upload; never downgrades to unverified TLS
}

// src: vvaharness/config/profiles/default.yaml:424-429
Options reasoning { think_in_prompt: true }   // via: deepagents only
