# .github/ISSUE_TEMPLATE/documentation.yml

Role: repository/build/operating context, outside scan execution.

Exact source asset: `assets/original/.github/ISSUE_TEMPLATE/documentation.yml`. SHA-256 `0d38c191ce439aab1998b645eb895bcfcfe59526e2bcf3e85a5bede399d8433f`.

```sudo
// Source: .github/ISSUE_TEMPLATE/documentation.yml:1-58
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| name | "📚 Documentation issue" |
| description | "Report unclear, missing, or incorrect documentation" |
| title | "[Docs]: " |
| labels | ["type:docs", "status:needs-triage"] |
| body | [{"type": "dropdown", "id": "doc-set", "attributes": {"label": "Documentation area", "options": ["README.md", "AGENTS.md", "docs/USER_GUIDE.md", "docs/features.md", "docs/architecture.md", "docs/models.md", "docs/integrations.md", "docs/SKILLS.md", "docs/security.md", "docs/limitations.md", "SECURITY.md", "Other"]}, "validations": {"required": true}}, {"type": "input", "id": "location", "attributes": {"label": "Where?", "placeholder": "e.g. docs/USER_GUIDE.md Run section"}, "validations": {"required": true}}, {"type": "textarea", "id": "issue", "attributes": {"label": "What is unclear, missing, or wrong?"}, "validations": {"required": true}}, {"type": "textarea", "id": "suggestion", "attributes": {"label": "Suggested improvement (optional)"}}, {"type": "checkboxes", "id": "checks", "attributes": {"label": "Quick checks", "options": [{"label": "I checked whether this behavior is already documented in README.md or docs/USER_GUIDE.md.", "required": false}]}}, {"type": "checkboxes", "id": "acknowledgements", "attributes": {"label": "Acknowledgements", "options": [{"label": "I understand that any Contribution I submit is subject to the **Contribution Submission Terms and Agreement** within [**CONTRIBUTING.md**](https://github.com/visa/visa-vulnerability-agentic-harness/blob/main/CONTRIBUTING.md), including the provisions on Ownership and Sufficient Rights, Legal Authority to Bind, No Conflicting Obligations, No Restricted Data, and Applicable License Terms and further that a record of my agreement to these terms, including my username and submission metadata, will be maintained indefinitely as part of the project's public record, and that the rights I have granted under the applicable license are irrevocable.", "required": true}]}}] |
