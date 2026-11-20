# vvaharness/config/profiles/full.yaml

The maximum-coverage profile: wider budgets, planning on, Stage 10 (remediation) and Stage 11 (validation) enabled, and a mixed-vendor exploit-verification panel with an OpenAI judge.

**Rendering convention for this file.** `default.yaml` is rendered in full in `vvah/vvaharness/config/profiles/default.sudo.md`. This file lists only (a) every leaf key whose value differs from `default.yaml`, and (b) every leaf key present in one of the two files and absent from the other. Every other key has exactly the `default.yaml` value. The differences were computed mechanically by flattening both YAML files to dotted leaf paths and comparing values. Where a key is absent from this profile, the value that runs is the `_STEP_DEFAULTS` value from `vvah/vvaharness/config/__init__.sudo` when that key is registered there.

Source: `vvaharness/config/profiles/full.yaml` (lines 1-455)
Executor: code (data read by `knob(...)` and `getattr(cfg...)` across all stages)
Called from: `vvaharness/config/__init__.py` load (selected with `--config`)

// src: vvaharness/config/profiles/full.yaml:15-25
// Profile note: "Maximum-coverage profile: wider budgets, planning on, S10/S11 enabled." Same max_turns note as default.yaml.

Keys absent from one of the two files: none.

## Model roles

// src: vvaharness/config/profiles/full.yaml:26-92
Options models {   // differences only
  exploit_verification.attacker.id: "claude-opus-4-8"     // default: "claude-opus-4-7"
  exploit_verification.judge: { id: "gpt-5.6-sol", provider: "openai" }   // default: id "claude-opus-4-8", provider "anthropic"; via stays "deepagents"
  exploit_verification.classify.id: "claude-opus-4-8"     // default: "claude-sonnet-4-6"
  exploit_verification.mapper.id: "claude-opus-4-8"       // default: "claude-sonnet-4-6"
}

## Stage settings

// src: vvaharness/config/profiles/full.yaml:186-228
Options step2 {   // differences only
  max_threats: 80                  // default 50
  max_turns: 12                    // default 20
  graph_tool_budget: 6             // default 12
  planning: true                   // default false
  max_manifest_total_chars: 24000  // default 32000
  max_graph_files: 250             // default 220
}

// src: vvaharness/config/profiles/full.yaml:229-254
Options step4 {   // differences only
  batch_size: 2                    // default 4
  max_turns: 20                    // default 15
  max_model_calls: 0               // default 8 (0 = unmetered)
  deadline: 500                    // default 600
  replay_timeout: 60               // default 90
  cwe_tool_budget: 6               // default 8
  graph_tool_budget: 20            // default 16
  planning: true                   // default false
  inline_source: false             // default true
  max_findings_per_run: 100        // default 50
}

// src: vvaharness/config/profiles/full.yaml:255-259
Options step5_prefilter { line_tolerance: 0 }   // default 5

// src: vvaharness/config/profiles/full.yaml:264-296
Options step6_verify {   // differences only
  batch_size: 8                    // default 4
  max_turns: 30                    // default 20
  max_model_calls: 0               // default 12
  batch_deadline: 420              // default 530
  min_confidence: 1                // default 5
}

// src: vvaharness/config/profiles/full.yaml:297-339
Options step6_exploit_verification {   // differences only
  max_requests_per_finding: 300    // default 200
  max_payloads_per_finding: 50     // default 25
  attacker.max_turns: 20           // default 15
}

// src: vvaharness/config/profiles/full.yaml:340-352
Options step7_dedup { line_tolerance: 0 }   // default 5

// src: vvaharness/config/profiles/full.yaml:353-367
Options step8 {   // differences only
  deadline: 800                    // default 600
  max_tokens: 64000                // default 48000
  timeout: 2400                    // default 1800
}

// src: vvaharness/config/profiles/full.yaml:371-386
Options step_remediate {   // differences only
  enabled: true                    // default false: S10 fix mode edits files in the target repository
  top_n_findings: 20               // default 5
}

// src: vvaharness/config/profiles/full.yaml:387-400
Options step_validate { enabled: true }   // default false
