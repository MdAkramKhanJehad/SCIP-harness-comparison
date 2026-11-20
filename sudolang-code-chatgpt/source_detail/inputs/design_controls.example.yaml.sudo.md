# inputs/design_controls.example.yaml

Role: configuration/policy/rules/input data; loader controls interpretation.

Exact source asset: `assets/original/inputs/design_controls.example.yaml`. SHA-256 `b2eb16b3ff822ab105d2849bce44135236fbd623822678b4be22c17a398a4e97`.

```sudo
// Source: inputs/design_controls.example.yaml:1-26
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| controls | [{"name": "api-gateway-auth", "kind": "auth", "protects": ["src/handlers/**"], "notes": "All handler entry points sit behind JWT validation in the gateway."}, {"name": "seccomp-sandbox", "kind": "sandbox", "protects": ["src/workers/**"], "notes": "Worker processes run under seccomp-bpf; no execve, no socket."}] |

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../prompt_representation/inputs/design_controls.example.yaml.sudo.md). Exact strings in the evidence asset support this conversion.
