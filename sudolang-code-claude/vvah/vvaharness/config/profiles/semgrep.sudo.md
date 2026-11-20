# vvaharness/config/profiles/semgrep.yaml

`default.yaml` plus the Semgrep plugin and nothing else. The plugin's four read-only graph tools reach Stages 2, 4 and 6. It needs a `semgrep` binary on PATH; with neither binary nor rules reachable nothing raises and the tools report an absent scan.

**Rendering convention for this file.** `default.yaml` is rendered in full in `vvah/vvaharness/config/profiles/default.sudo.md`. This file lists only (a) every leaf key whose value differs from `default.yaml`, and (b) every leaf key present in one of the two files and absent from the other. Every other key has exactly the `default.yaml` value. The differences were computed mechanically by flattening both YAML files to dotted leaf paths and comparing values.

Source: `vvaharness/config/profiles/semgrep.yaml` (lines 1-430)
Executor: code (data read by `knob(...)` across all stages)
Called from: `vvaharness/config/__init__.py` load (selected with `--config`); the plugin list is read by `vvaharness/sdk/loading.py` load_plugin_set through `knob(cfg, "sdk.plugins", [])`

// src: vvaharness/config/profiles/semgrep.yaml:15-27
// Profile note: "default.yaml plus the Semgrep plugin, and nothing else: its four read-only graph tools reach S2/S4/S6."

Keys whose value differs from default.yaml: none.

## Key present only in this profile

// src: vvaharness/config/profiles/semgrep.yaml:83-86
Options sdk {
  plugins: [ { name: "semgrep", configs: [], rulesets: ["p/security-audit", "p/python", "p/secrets"] } ]
  // nested under the `sdk:` transport block; that is the key load_plugin_set reads ("sdk.plugins")
}
