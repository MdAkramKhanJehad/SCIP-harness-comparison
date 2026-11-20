# .github/workflows/issue-acknowledgement.yml

Role: repository/build/operating context, outside scan execution.

Exact source asset: `assets/original/.github/workflows/issue-acknowledgement.yml`. SHA-256 `d975dad5431d7d66c5761f61923d221cf84b187a25f9a2bd25a43c5a1f86b41d`.

```sudo
// Source: .github/workflows/issue-acknowledgement.yml:1-56
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| name | "Public issue acknowledgement" |
| True.issues.types | ["opened"] |
| concurrency.group | "issue-intake-ack-${{ github.event.issue.number }}" |
| concurrency.cancel-in-progress | false |
| jobs.acknowledge.if | "${{ !github.event.issue.pull_request }}" |
| jobs.acknowledge.runs-on | "ubuntu-latest" |
| jobs.acknowledge.timeout-minutes | 3 |
| jobs.acknowledge.permissions.issues | "write" |
| jobs.acknowledge.env.GH_TOKEN | "${{ secrets.GITHUB_TOKEN }}" |
| jobs.acknowledge.env.GH_REPO | "${{ github.repository }}" |
| jobs.acknowledge.env.ISSUE_NUMBER | "${{ github.event.issue.number }}" |
| jobs.acknowledge.env.SECURITY_POLICY_URL | "${{ github.server_url }}/${{ github.repository }}/security/policy" |
| jobs.acknowledge.env.VVAH_TEAM_NAME | "VVAH Team" |
| jobs.acknowledge.env.VVAH_TEAM_EMAIL | "vvaharness@visa.com" |
| jobs.acknowledge.steps | [{"name": "Acknowledge issue", "shell": "bash", "run": "{\n  printf '%s\\n\\n' \"Thank you for submitting this issue. We've confirmed it has been received and logged for review.\"\n  printf '%s\\n\\n' \"Please note this acknowledgment reflects receipt only, it does not indicate acceptance, confirm a defect, or commit us to a specific remedy or timeline. We'll follow up if additional information is needed.\"\n  printf '%s\\n\\n' 'We appreciate you taking time to help improve the project.'\n  printf 'Feel free to reach out to us at [%s](mailto:%s) for feedback on the issue submission process or any other questions.\\n\\n' \"${VVAH_TEAM_EMAIL}\" \"${VVAH_TEAM_EMAIL}\"\n  printf '%s\\n' \"${VVAH_TEAM_NAME}\"\n} > \"${RUNNER_TEMP}/acknowledgement.md\"\ngh api \\\n  --method POST \\\n  -H \"Accept: application/vnd.github+json\" \\\n  \"/repos/${GH_REPO}/issues/${ISSUE_NUMBER}/comments\" \\\n  --raw-field \"body=$(cat \"${RUNNER_TEMP}/acknowledgement.md\")\""}] |
