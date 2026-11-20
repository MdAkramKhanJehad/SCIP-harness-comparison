# inputs/remediation_policy.yaml

Role: configuration/policy/rules/input data; loader controls interpretation.

Exact source asset: `assets/original/inputs/remediation_policy.yaml`. SHA-256 `99f21f35f7c2557aed4d9593557952542dbe2862269f5e4198cb71779e96a769`.

```sudo
// Source: inputs/remediation_policy.yaml:1-85
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| schema_version | "1.0" |
| default_action | "allow" |
| kill_switch.env_var | "VVAHARNESS_REMEDIATE_DISABLE" |
| kill_switch.file | "./.vvaharness-remediate-off" |
| deny | [] |
| deny_paths | [] |
| forbid_patch_paths | ["**/.git", "**/.git/**", "**/.github/**", "**/.gitlab/**", "**/.gitlab-ci.*", "**/.circleci/**", "**/.buildkite/**", "**/Jenkinsfile*", "**/azure-pipelines*.yml", "**/azure-pipelines*.yaml", "**/bitbucket-pipelines.yml", "**/bitbucket-pipelines.yaml", "**/cloudbuild.yml", "**/cloudbuild.yaml", "**/buildspec.yml", "**/buildspec.yaml", "**/.githooks/**", "**/.husky/**"] |
