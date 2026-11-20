# vvaharness/config/profiles/taint.yaml

The taint-oriented profile: narrow batches, planning on, unreachable-findings appendix on, verbose progress.

**Rendering convention for this file.** `default.yaml` is rendered in full in `vvah/vvaharness/config/profiles/default.sudo.md`. This file lists only (a) every leaf key whose value differs from `default.yaml`, and (b) every leaf key present in one of the two files and absent from the other. Every other key has exactly the `default.yaml` value. The differences were computed mechanically by flattening both YAML files to dotted leaf paths and comparing values. Where a key is absent from this profile, the value that runs is the `_STEP_DEFAULTS` value from `vvah/vvaharness/config/__init__.sudo` when that key is registered there; otherwise the reader's own fallback applies.

Source: `vvaharness/config/profiles/taint.yaml` (lines 1-410)
Executor: code (data read by `knob(...)` and `getattr(cfg...)` across all stages)
Called from: `vvaharness/config/__init__.py` load (selected with `--config`)

// src: vvaharness/config/profiles/taint.yaml:15-25
// Profile note: "Taint-oriented profile: narrow batches, planning on, unreachable appendix on." Same max_turns note as default.yaml.

Model roles: no differences.

// src: vvaharness/config/profiles/taint.yaml:62-68
Options sdk { cache_markers: absent }   // default "on"; commented out here as `# cache_markers: "off"`

// src: vvaharness/config/profiles/taint.yaml:102-150
Options step1 { exclude_dirs: [".vs", ".settings"] }   // default [".vs", ".settings", ".vscode", ".idea", "node_modules"]

// src: vvaharness/config/profiles/taint.yaml:151-193
Options step2 {   // differences only
  max_turns: 12                    // default 20
  graph_tool_budget: 6             // default 12
  planning: true                   // default false
  max_manifest_total_chars: 24000  // default 32000
  max_graph_files: 250             // default 220
}

// src: vvaharness/config/profiles/taint.yaml:194-218
Options step4 {   // differences only
  batch_size: 1                    // default 4
  max_model_calls: 0               // default 8
  deadline: 400                    // default 600
  replay_timeout: 60               // default 90
  resume_timeout: absent           // default 90; _STEP_DEFAULTS supplies 60
  cwe_tool_budget: 6               // default 8
  graph_tool_budget: 8             // default 16
  planning: true                   // default false
  inline_source: false             // default true
}

// src: vvaharness/config/profiles/taint.yaml:228-259
Options step6_verify {   // differences only
  batch_size: 12                   // default 4
  max_model_calls: 0               // default 12
  batch_deadline: 400              // default 530
  resume_timeout: absent           // default 90; _STEP_DEFAULTS supplies 60
  graph_tool_budget: 16            // default 20
}

// src: vvaharness/config/profiles/taint.yaml:260-302
Options step6_exploit_verification {   // differences only
  max_requests_per_finding: 300    // default 200
  max_payloads_per_finding: 50     // default 25
  attacker.max_turns: 20           // default 15
}

// src: vvaharness/config/profiles/taint.yaml:310-324
Options step8 {   // differences only
  deadline: 800                    // default 600
  max_tokens: 64000                // default 48000
  timeout: 2400                    // default 1800
}

// src: vvaharness/config/profiles/taint.yaml:385-392
Options scan_progress { style: "verbose" }   // default "compact"

// src: vvaharness/config/profiles/taint.yaml:393-409
Options output { emit_unreachable_appendix: true }   // default false
