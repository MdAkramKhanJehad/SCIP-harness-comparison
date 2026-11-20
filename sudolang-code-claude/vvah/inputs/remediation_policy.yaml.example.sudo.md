# inputs/remediation_policy.yaml.example

A stricter example policy (allow-list mode) that an operator can point `step_remediate.policy_file` at. Same format as `remediation_policy.yaml`.

Source: `inputs/remediation_policy.yaml.example` (lines 1-245)
Executor: code (data, only when configured)
Called from: not loaded by default; `vvaharness/remediation_agent/policy/context.sudo` _resolve_input when configured

// src: inputs/remediation_policy.yaml.example:32-41
Options {
  default_action: "deny"   // only CWEs on the allow list are patched
  kill_switch: { env_var: "VVAHARNESS_REMEDIATE_DISABLE", file: "./.vvaharness-remediate-off" }
}

// src: inputs/remediation_policy.yaml.example:47-179
Options {
  // each deny id plus its listed descendants is denied (loader adds descendants with reason "descendant_of:<id> (<reason>)")
  deny: [
    { id: "CWE-284", reason: "requires knowledge of intended authorization policy", descendants: [CWE-285, CWE-639, CWE-862, CWE-863, CWE-566, CWE-732, CWE-1390] },
    { id: "CWE-287", reason: "auth flow changes need architectural review", descendants: [CWE-306, CWE-303, CWE-304, CWE-620, CWE-640, CWE-294, CWE-302, CWE-307] },
    { id: "CWE-840", reason: "no generic safe transformation exists", descendants: [CWE-841, CWE-770, CWE-1284, CWE-682, CWE-369] },
    { id: "CWE-310", reason: "crypto choices need org policy + key-mgmt review", descendants: [CWE-327, CWE-326, CWE-328, CWE-916, CWE-329, CWE-330, CWE-338, CWE-321, CWE-323, CWE-757, CWE-1240] },
    { id: "CWE-269", reason: "privilege boundaries are policy decisions", descendants: [CWE-250, CWE-266, CWE-268, CWE-271] },
    { id: "CWE-613", reason: "session lifetime is product/compliance policy", descendants: [CWE-384] },
    { id: "CWE-119", reason: "bounds/lifetime fixes are design-specific; no generic patch", descendants: [CWE-120, CWE-121, CWE-122, CWE-124, CWE-125, CWE-787, CWE-126, CWE-127, CWE-131, CWE-680, CWE-805, CWE-806] },
    { id: "CWE-416", reason: "requires ownership/lifetime redesign", descendants: [CWE-415] },
    { id: "CWE-476", reason: "correct fix depends on whether null is a valid state", descendants: [] },
    { id: "CWE-134", reason: "often co-occurs with varargs ABI; needs caller-by-caller review", descendants: [] },
    { id: "CWE-190", reason: "correct overflow handling is domain-specific (saturate vs error vs widen)", descendants: [CWE-191, CWE-128, CWE-681] },
    { id: "CWE-843", reason: "requires type-system / variant redesign", descendants: [] },
    { id: "CWE-362", reason: "synchronization strategy is architectural", descendants: [CWE-367, CWE-366, CWE-421] },
    { id: "CWE-401", reason: "ownership fix; auto-inserting free() risks UAF/double-free", descendants: [CWE-772, CWE-775] }
  ]
  // preserved: every entry sets include_descendants: true, but the loader never reads that key; only the explicit descendants list counts
}

// src: inputs/remediation_policy.yaml.example:185-197
Options { allow: [CWE-89, CWE-943, CWE-78, CWE-22, CWE-611, CWE-601, CWE-79, CWE-502, CWE-918, CWE-798, CWE-1333] }

// src: inputs/remediation_policy.yaml.example:205-215
Options { deny_paths: ["**/auth/**", "**/authn/**", "**/authz/**", "**/security/**", "**/iam/**", "**/*crypto*", "**/*Permission*", "**/*Policy*", "**/middleware/access*"] }   // checked on the finding location (pre-gate) and the changed files (post-gate)

// src: inputs/remediation_policy.yaml.example:224-245
Options { forbid_patch_paths: ["**/setup.py", "**/setup.cfg", "**/pyproject.toml", "**/conftest.py", "**/Makefile", "**/CMakeLists.txt", "**/*.gradle", "**/*.gradle.kts", "**/pom.xml", "**/build.sbt", "**/package.json", "**/.npmrc", "**/webpack.config.*", "**/Dockerfile*", "**/.github/**", "**/.gitlab-ci.*", "**/Jenkinsfile*", "**/*.sh", "**/*.ps1", "**/*.bat", "**/*.cmd"] }
// unlike the shipped policy, this list does not include "**/.git" or "**/.git/**"
