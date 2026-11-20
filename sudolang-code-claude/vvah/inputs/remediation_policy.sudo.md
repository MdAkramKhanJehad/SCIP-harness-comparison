# inputs/remediation_policy.yaml

The shipped remediation policy: the hard gate the Stage 10 remediation agent loads before any model call (`policy_gate/loader.sudo` parse_policy, `policy_gate/gate.sudo` decide). This shipped file allows every CWE and only forbids edits to repository automation and version-control metadata.

Source: `inputs/remediation_policy.yaml` (lines 1-85)
Executor: code (data read by the policy gate)
Called from: `vvaharness/remediation_agent/policy_gate/gate.sudo` DEFAULT_POLICY_PATH (unless `step_remediate.policy_file` overrides it)

// src: inputs/remediation_policy.yaml:15-30
// File comments state the semantics; the code that implements them is policy_gate/gate.sudo decide:
//   "Evaluation order: kill_switch → deny → deny_paths → allow → default_action"
//   "Fail-closed: missing/invalid policy file ⇒ treat ALL as deny"

// src: inputs/remediation_policy.yaml:32-56
Options {
  schema_version: "1.0"   // not read by the loader
  default_action: "allow"   // every CWE not denied is patch-eligible
  kill_switch: {
    env_var: "VVAHARNESS_REMEDIATE_DISABLE"   // "1", "true", "yes" or "on" disables patching
    file: "./.vvaharness-remediate-off"   // presence disables patching
  }
  deny: []
  deny_paths: []
  // allow is absent: an empty allow set
}
// preserved: the kill-switch file path is relative, so it is checked relative to the process working directory, not the scanned repository
// preserved: the comments at lines 51-55 and 59-63 say a post-gate hit "downgrades to guidance"; the code reverts the files and sets the verdict to "Needs Review" or "Not Fixed" (policy/postgate.sudo)
// preserved: with default_action allow and an empty deny list, CWEs the playbook marks "guidance" or lists under never_autofix_cwes (for example CWE-284, CWE-916) are patched

// src: inputs/remediation_policy.yaml:65-85
Options {
  // matched against the changed-file set after the session; a hit reverts the file (policy/postgate.sudo)
  forbid_patch_paths: ["**/.git", "**/.git/**", "**/.github/**", "**/.gitlab/**", "**/.gitlab-ci.*", "**/.circleci/**", "**/.buildkite/**", "**/Jenkinsfile*", "**/azure-pipelines*.yml", "**/azure-pipelines*.yaml", "**/bitbucket-pipelines.yml", "**/bitbucket-pipelines.yaml", "**/cloudbuild.yml", "**/cloudbuild.yaml", "**/buildspec.yml", "**/buildspec.yaml", "**/.githooks/**", "**/.husky/**"]
}
