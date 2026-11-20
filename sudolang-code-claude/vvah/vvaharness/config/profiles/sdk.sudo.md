# vvaharness/config/profiles/sdk.yaml

Every model role via `sdk` (the Anthropic Python SDK) at the sonnet tier, with Stage 10 (remediation) and Stage 11 (validation) enabled. The file has no `openai:`, `cli:` or `step0:` block.

**Rendering convention for this file.** `default.yaml` is rendered in full in `vvah/vvaharness/config/profiles/default.sudo.md`. This file lists only (a) every leaf key whose value differs from `default.yaml`, and (b) every leaf key present in one of the two files and absent from the other. Every other key has exactly the `default.yaml` value. The differences were computed mechanically by flattening both YAML files to dotted leaf paths and comparing values. Where a key is absent from this profile, the value that runs is the `_STEP_DEFAULTS` value from `vvah/vvaharness/config/__init__.sudo` when that key is registered there; otherwise the reader's own fallback applies.

Source: `vvaharness/config/profiles/sdk.yaml` (lines 1-399)
Executor: code (data read by `knob(...)` and `getattr(cfg...)` across all stages)
Called from: `vvaharness/config/__init__.py` load (selected with `--config`)

// src: vvaharness/config/profiles/sdk.yaml:15-25
// Profile note: "Every role via:sdk (Anthropic Python SDK), sonnet tier. S10/S11 enabled." Same max_turns note as default.yaml,
//   including that on via:sdk max_turns is a HARD per-session turn cap.

## Model roles

// src: vvaharness/config/profiles/sdk.yaml:26-56
Options models {   // every listed role: via "sdk" (default "deepagents"); no `provider` key on any role (default "anthropic")
  autoexclude: { id: "claude-sonnet-4-6", via: "sdk" }          // default id "claude-opus-4-7"
  preprocess:  { id: "claude-sonnet-4-6", via: "sdk" }          // id unchanged
  threatmodel: { id: "claude-sonnet-4-6", via: "sdk" }          // default id "claude-opus-4-7"
  decompose:   { id: "claude-sonnet-4-6", via: "sdk" }          // default id "claude-opus-4-7"
  deepdive:    { id: "claude-sonnet-4-6", via: "sdk", temperature: 0.4 }   // default id "claude-opus-4-7"; temperature present only here
  verify:      { id: "claude-sonnet-4-6", via: "sdk" }          // default id "claude-opus-4-7"
  dedup:       { id: "claude-sonnet-4-6", via: "sdk" }          // default id "claude-opus-4-7"
  chain:       { id: "claude-sonnet-4-6", via: "sdk" }          // default id "claude-opus-4-7"
  remediate:   { id: "claude-opus-4-8",   via: "sdk" }          // id unchanged; on via: sdk the Edit/Write grant hands the session to the Claude Agent SDK
  validate.orchestrator:        { id: "claude-sonnet-4-6", via: "sdk" }   // default id "claude-opus-5"
  validate.penetration_tester:  { id: "claude-sonnet-4-6" }     // default "claude-opus-4-8"
  validate.cross_repo_analyzer: { id: "claude-sonnet-4-6" }     // default "claude-opus-4-8"
  // validate.security_architect unchanged: "claude-opus-4-8"
  exploit_verification.attacker: { id: "claude-sonnet-4-6", via: "sdk" }   // default id "claude-opus-4-7"
  exploit_verification.judge:    { via: "sdk" }                 // id unchanged "claude-opus-4-8"
  exploit_verification.classify: { via: "sdk" }                 // id unchanged
  exploit_verification.mapper:   { via: "sdk" }                 // id unchanged
}

## Transport and caching

// src: vvaharness/config/profiles/sdk.yaml:58-75
Options transport {   // differences only
  sdk.cache_markers: absent        // default "on"; commented out here ("switch for via:deepagents roles only; none here")
  openai: absent                   // default api_key, base_url, verify_ssl, ca_cert all absent
  cli: absent                      // default verify_ssl, ca_cert, effort "high", mcp_tools true, restricted true all absent;
                                   // _STEP_DEFAULTS still supplies cli.mcp_tools true and cli.restricted true
}

## Stage settings

// src: vvaharness/config/profiles/sdk.yaml:75-77 — step1 follows cache_route directly; there is no step0 block
Options step0 { callgraph_detection: absent, min_graph_nodes_for_gate: absent }
  // the whole step0 block is absent; _STEP_DEFAULTS supplies callgraph_detection "rules" and min_graph_nodes_for_gate 10 (same as default.yaml)

// src: vvaharness/config/profiles/sdk.yaml:129-171
Options step2 {   // differences only
  max_turns: 60                    // default 20
  graph_tool_budget: 6             // default 12
  planning: true                   // default false
  max_manifest_total_chars: 24000  // default 32000
  max_graph_sinks: 80              // default 100
}

// src: vvaharness/config/profiles/sdk.yaml:172-196
Options step4 {   // differences only
  batch_size: 1                    // default 4
  max_turns: 60                    // default 15
  max_model_calls: 0               // default 8
  deadline: 400                    // default 600
  replay_timeout: 60               // default 90
  resume_timeout: absent           // default 90; _STEP_DEFAULTS supplies 60
  cwe_tool_budget: 6               // default 8
  graph_tool_budget: 6             // default 16
  planning: true                   // default false
  inline_source: false             // default true
  line_bucket: 10                  // default 5
}

// src: vvaharness/config/profiles/sdk.yaml:206-237
Options step6_verify {   // differences only
  batch_size: 12                   // default 4
  max_turns: 30                    // default 20
  max_model_calls: 0               // default 12
  batch_deadline: 400              // default 530
  resume_timeout: absent           // default 90; _STEP_DEFAULTS supplies 60
  graph_tools: false               // default true
  graph_tool_budget: 16            // default 20
}

// src: vvaharness/config/profiles/sdk.yaml:238-280
Options step6_exploit_verification {   // differences only
  max_requests_per_finding: 300    // default 200
  max_payloads_per_finding: 50     // default 25
  attacker.max_turns: 20           // default 15
}

// src: vvaharness/config/profiles/sdk.yaml:281-287
Options step7_dedup { line_tolerance: 3 }   // default 5

// src: vvaharness/config/profiles/sdk.yaml:288-311
Options step8 {   // differences only
  deadline: 800                    // default 600
  max_tokens: 64000                // default 48000
  timeout: 2400                    // default 1800
}

// src: vvaharness/config/profiles/sdk.yaml:315-330
Options step_remediate { enabled: true }   // default false: S10 fix mode edits files in the target repository

// src: vvaharness/config/profiles/sdk.yaml:331-344
Options step_validate { enabled: true }    // default false

// src: vvaharness/config/profiles/sdk.yaml:372-380
Options scan_progress { enabled: false }   // default true
