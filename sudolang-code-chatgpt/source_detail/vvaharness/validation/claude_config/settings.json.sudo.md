# vvaharness/validation/claude_config/settings.json

Role: configuration/policy/rules/input data; loader controls interpretation.

Exact source asset: `assets/original/vvaharness/validation/claude_config/settings.json`. SHA-256 `a0780cb6f69a971a1ff248add90cfba2956757939e9b7d9ba28e233b7421c5a1`.

```sudo
// Source: vvaharness/validation/claude_config/settings.json:1-17
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| model | "claude-opus-4-8[1m]" |
| permissions.allow | ["Read", "Grep", "Glob"] |
| permissions.deny | ["Write", "Edit", "NotebookEdit", "Bash"] |
| hooks.Stop | [{"type": "command", "command": "bash .claude/hooks/logging/capture_transcript.sh", "timeout": 30}] |
