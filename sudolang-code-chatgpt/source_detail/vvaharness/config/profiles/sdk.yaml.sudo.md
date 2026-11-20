# vvaharness/config/profiles/sdk.yaml

Role: configuration/policy/rules/input data; loader controls interpretation.

Exact source asset: `assets/original/vvaharness/config/profiles/sdk.yaml`. SHA-256 `7bdce42fdd7f8ea4ed0118ad38d584f74d995d4705c109e37a55433e0396b81f`.

```sudo
// Source: vvaharness/config/profiles/sdk.yaml:1-399
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| models.autoexclude.id | "claude-sonnet-4-6" |
| models.autoexclude.via | "sdk" |
| models.preprocess.id | "claude-sonnet-4-6" |
| models.preprocess.via | "sdk" |
| models.threatmodel.id | "claude-sonnet-4-6" |
| models.threatmodel.via | "sdk" |
| models.decompose.id | "claude-sonnet-4-6" |
| models.decompose.via | "sdk" |
| models.deepdive.id | "claude-sonnet-4-6" |
| models.deepdive.via | "sdk" |
| models.deepdive.temperature | 0.4 |
| models.verify.id | "claude-sonnet-4-6" |
| models.verify.via | "sdk" |
| models.dedup.id | "claude-sonnet-4-6" |
| models.dedup.via | "sdk" |
| models.chain.id | "claude-sonnet-4-6" |
| models.chain.via | "sdk" |
| models.remediate.id | "claude-opus-4-8" |
| models.remediate.via | "sdk" |
| models.validate.orchestrator.id | "claude-sonnet-4-6" |
| models.validate.orchestrator.via | "sdk" |
| models.validate.security_architect.id | "claude-opus-4-8" |
| models.validate.penetration_tester.id | "claude-sonnet-4-6" |
| models.validate.cross_repo_analyzer.id | "claude-sonnet-4-6" |
| models.exploit_verification.attacker.id | "claude-sonnet-4-6" |
| models.exploit_verification.attacker.via | "sdk" |
| models.exploit_verification.judge.id | "claude-opus-4-8" |
| models.exploit_verification.judge.via | "sdk" |
| models.exploit_verification.classify.id | "claude-sonnet-4-6" |
| models.exploit_verification.classify.via | "sdk" |
| models.exploit_verification.mapper.id | "claude-sonnet-4-6" |
| models.exploit_verification.mapper.via | "sdk" |
| sdk.api_key | "${ANTHROPIC_SDK_API_KEY}" |
| sdk.base_url | "${ANTHROPIC_SDK_BASE_URL}" |
| sdk.verify_ssl | true |
| sdk.ca_cert | "${ANTHROPIC_SDK_CA_CERT}" |
| sdk.client_cert | "${ANTHROPIC_SDK_CLIENT_CERT}" |
| cache_markers | "on" |
| cache_min_block_tokens | null |
| cache_route | "anthropic" |
| step1.auto_exclude | true |
| step1.auto_exclude_protect_templates | true |
| step1.auto_exclude_protect_key_material | true |
| step1.auto_exclude_protect_secrets | true |
| step1.auto_exclude_protect_client_sinks | true |
| step1.auto_exclude_max_tokens | 8000 |
| step1.auto_exclude_effort | "high" |
| step1.allowed_tools | ["Read", "Grep"] |
| step1.exclude_dirs | [".vs", ".settings", ".vscode", ".idea", "node_modules"] |
| step1.exclude_exts | [".msi", ".nupkg", ".pdb", ".lib", ".aar", ".ser", ".pbix", ".p12", ".pfx", ".jks", ".der", ".cer", ".doc", ".docx", ".xls", ".xlsx", ".xlsm", ".bmp", ".sqlite", ".db"] |
| step1.exclude_globs | ["**/._*"] |
| step1.max_file_kb | 1024 |
| step1.follow_symlinks | false |
| step1.config_dedup.enabled | true |
| step1.config_dedup.min_cluster_size | 5 |
| step1.config_dedup.keep_per_top_dir | true |
| step1.config_dedup.promote_on_secret_hit | true |
| step1.config_dedup.promote_on_insecure_value | true |
| step2.max_threats | 50 |
| step2.max_assets | 40 |
| step2.max_trust_boundaries | 60 |
| step2.baseline | "auto" |
| step2.empty_retry | true |
| step2.max_tokens | 64000 |
| step2.effort | "high" |
| step2.max_turns | 60 |
| step2.max_model_calls | 4 |
| step2.deadline | 400 |
| step2.replay_timeout | 300 |
| step2.replay_max_tokens | 16000 |
| step2.timeout | 900 |
| step2.allowed_tools | ["Read", "Grep"] |
| step2.bash | false |
| step2.graph_tools | true |
| step2.graph_tool_budget | 6 |
| step2.planning | true |
| step2.require_graph | true |
| step2.require_graph_rejections | 2 |
| step2.skills | true |
| step2.max_doc_chars | 32000 |
| step2.max_manifest_chars | 4000 |
| step2.max_manifest_total_chars | 24000 |
| step2.max_manifests | 12 |
| step2.max_manifests_per_kind | 2 |
| step2.max_manifest_depth | 3 |
| step2.max_prompt_modules | 100 |
| step2.max_prompt_entry_points | 400 |
| step2.max_inventory_files | 1200 |
| step2.max_api_artefacts | 100 |
| step2.max_config_reps | 80 |
| step2.max_config_rep_chars | 2000 |
| step2.max_config_rep_bodies | 12 |
| step2.max_modules | 100 |
| step2.max_entry_points | 400 |
| step2.max_graph_files | 220 |
| step2.max_graph_sinks | 80 |
| step2.max_graph_edges | 100 |
| step4.parallel | 12 |
| step4.batch_size | 1 |
| step4.max_tokens | 64000 |
| step4.effort | "high" |
| step4.max_turns | 60 |
| step4.max_model_calls | 0 |
| step4.deadline | 400 |
| step4.replay_timeout | 60 |
| step4.replay_max_tokens | 16000 |
| step4.cwe_tools | true |
| step4.cwe_tool_budget | 6 |
| step4.graph_tool_budget | 6 |
| step4.require_graph | true |
| step4.evidence_gate | true |
| step4.evidence_gate_refusals | 3 |
| step4.planning | true |
| step4.skills | true |
| step4.inline_source | false |
| step4.bash | false |
| step4.line_bucket | 10 |
| step4.max_extra_cwes | 2 |
| step4.max_findings_per_run | 50 |
| step4.split_retry | true |
| step5_prefilter.sink_reanchor | true |
| step5_prefilter.sink_reanchor_max_move_lines | 40 |
| step5_prefilter.line_tolerance | 5 |
| step5_detectors.enabled | true |
| step5_detectors.max_rows | 200 |
| step6_verify.parallel | 7 |
| step6_verify.batch_size | 12 |
| step6_verify.max_tokens | 32000 |
| step6_verify.effort | "high" |
| step6_verify.max_turns | 30 |
| step6_verify.max_model_calls | 0 |
| step6_verify.batch_deadline | 400 |
| step6_verify.replay_timeout | 60 |
| step6_verify.replay_max_tokens | 12000 |
| step6_verify.batch_wall_clock_ceiling | 900 |
| step6_verify.split_retry | true |
| step6_verify.min_confidence | 5 |
| step6_verify.trait_stamps | true |
| step6_verify.reframe_enabled | false |
| step6_verify.inline_source | true |
| step6_verify.graph_tools | false |
| step6_verify.graph_tool_budget | 16 |
| step6_verify.require_graph | false |
| step6_verify.evidence_gate_refusals | 3 |
| step6_verify.max_budget_usd | 10.0 |
| step6_verify.progress_file | false |
| step6_verify.allowed_tools | ["Read", "Grep"] |
| step6_exploit_verification.enabled | "auto" |
| step6_exploit_verification.on_unreachable | "drop" |
| step6_exploit_verification.timeout_s | 15 |
| step6_exploit_verification.safe_mode | true |
| step6_exploit_verification.allow_state_changing_methods | true |
| step6_exploit_verification.ev_overrides_static | false |
| step6_exploit_verification.max_requests_per_finding | 300 |
| step6_exploit_verification.max_payloads_per_finding | 50 |
| step6_exploit_verification.rate_limit_rps | 0 |
| step6_exploit_verification.max_concurrency_target | 8 |
| step6_exploit_verification.max_concurrency_endpoint | 4 |
| step6_exploit_verification.parallel | 5 |
| step6_exploit_verification.store_probes | false |
| step6_exploit_verification.oob | "auto" |
| step6_exploit_verification.ev_replay_variants | true |
| step6_exploit_verification.on_auth_failure | "degrade" |
| step6_exploit_verification.auth_expiry_skew_s | 60 |
| step6_exploit_verification.max_reauth | 3 |
| step6_exploit_verification.classify.batch | 10 |
| step6_exploit_verification.classify.parallel | 5 |
| step6_exploit_verification.classify.effort | "high" |
| step6_exploit_verification.mapper.max_turns | 20 |
| step6_exploit_verification.mapper.parallel | 4 |
| step6_exploit_verification.mapper.effort | "high" |
| step6_exploit_verification.mapper.endpoint_index.chunk | 10 |
| step6_exploit_verification.mapper.finding_map.chunk | 6 |
| step6_exploit_verification.mapper.finding_map.max_endpoints | 5 |
| step6_exploit_verification.attacker.enabled | true |
| step6_exploit_verification.attacker.max_turns | 20 |
| step6_exploit_verification.attacker.max_tool_result_chars | 12000 |
| step6_exploit_verification.attacker.effort | "high" |
| step6_exploit_verification.judge.max_tokens | 4000 |
| step6_exploit_verification.judge.max_records | 24 |
| step6_exploit_verification.judge.effort | "high" |
| step7_dedup.line_tolerance | 3 |
| step7_dedup.per_sink_keep | true |
| step7_dedup.semantic | false |
| step7_dedup.max_tokens | 64000 |
| step7_dedup.effort | "high" |
| step8.severity_lift_gate | true |
| step8.chain_quality_checks | true |
| step8.chain_dedup | true |
| step8.prompt_fact_blocks | true |
| step8.max_model_calls | 1 |
| step8.max_turns | 2 |
| step8.deadline | 800 |
| step8.replay_timeout | 300 |
| step8.replay_max_tokens | 16000 |
| step8.max_tokens | 64000 |
| step8.effort | "high" |
| step8.timeout | 2400 |
| step8.prompt_token_budget | 100000 |
| step9.duplicate_result_guard | true |
| step_remediate.enabled | true |
| step_remediate.enforce_policy | true |
| step_remediate.policy_file | null |
| step_remediate.playbook_file | null |
| step_remediate.top_n_findings | 5 |
| step_remediate.max_budget_usd | 10.0 |
| step_remediate.max_turns | 40 |
| step_remediate.max_model_calls | 20 |
| step_remediate.timeout | 3600 |
| step_remediate.allowed_tools | ["Read", "Grep", "Edit", "Write"] |
| step_validate.enabled | true |
| step_validate.effort | "high" |
| step_validate.max_turns | 50 |
| step_validate.max_budget_usd | 15.0 |
| step_validate.max_findings | 20 |
| step_validate.timeout | 3600 |
| step_validate.max_model_calls | 60 |
| step_validate.orchestrator_max_model_calls | 40 |
| step_validate.allowed_tools | ["Read", "Grep", "Glob"] |
| inject.cve_file | "../../../inputs/known_cves.json" |
| inject.controls_file | "../../../inputs/design_controls.yaml" |
| inject.cmdb_file | "../../../inputs/cmdb.csv" |
| batch.git_token | "${GITHUB_TOKEN}" |
| batch.git_base_url | "${GIT_BASE_URL}" |
| batch.skip_repo_patterns | ["*automation*", "*-playwright*", "*-selenium*", "*-karate*", "*perf-script*", "*perf-test*", "*test-buddy*", "*-e2e*", "*-mock-*"] |
| scan_progress.enabled | false |
| scan_progress.style | "compact" |
| output.posture_channel | true |
| output.emit_unreachable_appendix | false |
| output.preserve_on_cleanup | ["security-scan", "security-remediation"] |
| output.ingest_url | "${VVAHARNESS_INGEST_URL:-}" |
| output.ingest_token | "${VVAHARNESS_INGEST_TOKEN:-}" |
| output.ingest_verify | "${VVAHARNESS_INGEST_VERIFY:-true}" |
| think_in_prompt | true |
