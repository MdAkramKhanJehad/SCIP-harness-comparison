# Configuration and resource interpretation

All five primary profiles and every bundled policy, playbook, hint, KB, payload,
validation settings file and input example are represented in their mirrored
`source_detail/` paths. Their exact bytes live under `assets/original/`;
parsed YAML/JSON/TOML values have `.parsed.json` assets.
`configuration_values.tsv` provides original spans for every YAML scalar leaf,
including ordered list positions. It is a source-value index, not a measurement
of a scan's effective environment.

```sudo
// Source: vvaharness/config/__init__.py:121-147
fn _deep_merge(base,over) {
  Copy base; for each overlay key in order {
    If both values are dictionaries, recursively merge them.
    Otherwise replace base value with overlay value, including lists.
  }
  Return merged dictionary.
}

// Source: vvaharness/config/__init__.py:147-713
_STEP_DEFAULTS supplies scalar defaults only where the chosen primary profile omits them.
Keep the exact 22 nested default blocks from the structural detail and original source.
Do not substitute a call-site fallback for a default already supplied by load().

// Source: vvaharness/config/__init__.py:868-905
fn load(path) {
  read_primary -> merge built-in defaults below primary -> merge accepted local overlay above primary
    -> environment expansion -> refusal_retries validation -> Config wrapper with _config_dir.
  Overlay existence, operator ownership/writability, disabling flag and visible override log
    are governed by _local_overlay/_require_overlay_trust, represented in the same detail module.
}

// Source: vvaharness/orchestrator/scan.py:445-503
The scan's AI-generated auto-step1 overlay is applied AFTER configuration load,
  using a deep copy for the target and expand=false. Resumed overlays are re-vetted.
Explicit operator step1 overlay selection is resolved earlier by entry.main and disables auto-step1.
```

These are literal primary-profile values, before any local overlay or environment:

| Profile | S4 batch / model-call cap / planning | S6 batch / confidence gate | S10 / S11 enabled | EV enabled setting / request budget |
|---|---|---|---|---|
| default | 4 / 8 / false | 4 / 5 | false / false | auto / 200 |
| full | 2 / 0 / true | 8 / 1 | true / true | auto / 300 |
| sdk | 1 / 0 / true | 12 / 5 | true / true | auto / 300 |
| semgrep | 4 / 8 / false | 4 / 5 | false / false | auto / 200 |
| taint | 1 / 0 / true | 12 / 5 | false / false | auto / 300 |

Each value above is supported by its profile's source node in
`configuration_values.tsv`; complete model ids/routes, filters, thresholds,
tools, caps, deadlines, templates and lists are retained in that profile's
mirrored detail file. Zero model-call cap means the source session-budget
builder returns no such budget; it does not remove other limits. The profile
name does not establish an implementation absent from the executable stage.

The runtime graph/node, prompt/evidence, turn/token, timeout, retry, confidence,
per-finding/site and policy limits have separate roles. Their names remain
separate even when values happen to match. Route adapters can interpret or
drop settings differently: the source route branches, warning paths and
middleware adapters are represented rather than normalizing all routes into
one imagined behavior.

Model-facing resources include field descriptions in Python as well as Markdown
system/persona/rule/skill documents. All Python strings/templates have source
spans in `.evidence.json`; all 25 Markdown package documents retain complete
text under `source_detail/`. Documentation-only files are labeled as such;
loader code determines which document becomes a prompt. Printing a warning,
example, instruction or claimed security property is not the same as enforcing it.
