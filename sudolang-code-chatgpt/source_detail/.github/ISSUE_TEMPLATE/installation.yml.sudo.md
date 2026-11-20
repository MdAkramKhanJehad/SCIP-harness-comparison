# .github/ISSUE_TEMPLATE/installation.yml

Role: repository/build/operating context, outside scan execution.

Exact source asset: `assets/original/.github/ISSUE_TEMPLATE/installation.yml`. SHA-256 `39eb75d7930ccc2dcede3493d1acfbee6a0f470467df6f8c012ae35b144ec91a`.

```sudo
// Source: .github/ISSUE_TEMPLATE/installation.yml:1-76
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| name | "🛠️ Installation / setup problem" |
| description | "Trouble installing, configuring credentials, or running vvaharness doctor" |
| title | "[Setup]: " |
| labels | ["type:setup", "status:needs-triage"] |
| body | [{"type": "markdown", "attributes": {"value": "Please run vvaharness doctor first and review https://github.com/visa/visa-vulnerability-agentic-harness/blob/main/docs/USER_GUIDE.md before filing."}}, {"type": "input", "id": "environment", "attributes": {"label": "OS, Python version, install method", "placeholder": "e.g. macOS 15, Python 3.12, pipx"}, "validations": {"required": true}}, {"type": "dropdown", "id": "profile", "attributes": {"label": "Profile in use", "options": ["default.yaml", "sdk.yaml", "taint.yaml", "full.yaml", "custom", "not sure"]}}, {"type": "dropdown", "id": "backend", "attributes": {"label": "Backend you are configuring", "options": ["cli (Claude CLI login)", "sdk (Anthropic SDK key)", "openai (OpenAI-compatible)", "deepagents (provider-routed)", "mixed / custom", "not sure"]}, "validations": {"required": true}}, {"type": "dropdown", "id": "command", "attributes": {"label": "Command that fails", "options": ["setup", "doctor", "scan", "remediate", "validate", "ev-replay", "estimate", "install step", "other"]}, "validations": {"required": true}}, {"type": "textarea", "id": "executed", "attributes": {"label": "Exact command(s) executed", "placeholder": "e.g. pip install ."}, "validations": {"required": true}}, {"type": "textarea", "id": "doctor", "attributes": {"label": "Output of vvaharness doctor", "description": "Redact any tokens/keys before pasting.", "render": "shell"}, "validations": {"required": true}}, {"type": "textarea", "id": "problem", "attributes": {"label": "What's failing?"}, "validations": {"required": true}}, {"type": "checkboxes", "id": "acknowledgements", "attributes": {"label": "Acknowledgements", "options": [{"label": "I understand that any Contribution I submit is subject to the **Contribution Submission Terms and Agreement** within [**CONTRIBUTING.md**](https://github.com/visa/visa-vulnerability-agentic-harness/blob/main/CONTRIBUTING.md), including the provisions on Ownership and Sufficient Rights, Legal Authority to Bind, No Conflicting Obligations, No Restricted Data, and Applicable License Terms, and further that a record of my agreement to these terms, including my username and submission metadata, will be maintained indefinitely as part of the project's public record, and that the rights I have granted under the applicable license are irrevocable.", "required": true}]}}] |
