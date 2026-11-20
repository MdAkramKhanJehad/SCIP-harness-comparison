# inputs/design_controls.example.yaml

Example design-controls input: compensating controls the scan feeds to the model stages (Stage 1 context, Stage 2 threat model, Stage 6 and Stage 8 prompts).

Source: `inputs/design_controls.example.yaml` (lines 1-26)
Executor: code (data)
Called from: `vvaharness/orchestrator/scan.sudo` (load_controls(knob("inject.controls_file")))

// src: inputs/design_controls.example.yaml:15-26
Options {
  controls: [
    { name: "api-gateway-auth", kind: "auth", protects: ["src/handlers/**"], notes: "All handler entry points sit behind JWT validation in the gateway." },
    { name: "seccomp-sandbox", kind: "sandbox", protects: ["src/workers/**"], notes: "Worker processes run under seccomp-bpf; no execve, no socket." }
  ]
}
