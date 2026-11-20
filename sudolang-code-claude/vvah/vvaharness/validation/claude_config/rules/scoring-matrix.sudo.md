# vvaharness/validation/claude_config/rules/scoring-matrix.md

The scoring rubric given to the orchestrator: four weighted gates, status multipliers, decision thresholds, the critical gate, merge readiness, the exact scoring algorithm the model is told to do by hand, and the code-level-signals and secret-exposure rules. It is required: the session refuses to start without it (`session/config_inject.sudo`, `session/rules.sudo`).

Source: `vvaharness/validation/claude_config/rules/scoring-matrix.md` (lines 1-200)
Executor: model
Called from: `vvaharness/validation/session/rules.sudo` orchestrator_rules_text; `vvaharness/validation/session/config_inject.sudo`

// abstracted: lines 1-15 are the license comment, stripped before the text reaches a model
// prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:16-200
SCORING_MATRIX_RULES {
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:18-27
  Criteria {
    root_cause: 0.43               // "The applied diff modifies the vulnerable code path with proper mitigation" (FC1)
    instance_coverage: 0.2467      // "All affected files in the diff; no remaining vulnerable code paths" (FC2)
    no_new_vulnerabilities: 0.1867 // "Code review shows fix doesn't introduce new security issues" (FC3)
    security_best_practices: 0.1366 // "Fix uses framework-recommended patterns (parameterized queries, encoding, etc.)" (FC4)
    "Weights sum to 1.00. The git-oriented `branch_targeting` gate (formerly 0.10) is removed: s11 validates a pre-applied diff on a dirty tree with no release-branch concept. The remaining four weights are renormalized to sum to 1.0."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:29-42
  StatusMultipliers {
    pass: 1.0; partial: 0.5; fail: 0.0; skip: 0.0
    "Synthesized gates should normally be `pass`/`partial`/`fail`. A `skip` marks an *unevaluated* gate: it is excluded from scoring entirely -- dropped from BOTH the numerator and the denominator -- so it is weight-neutral (it neither earns nor drags credit). The score is **renormalized** over the gates actually evaluated; a skip's weight is redistributed across the evaluated gates, not counted as a failure (see Scoring Execution)."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:44-57
  DecisionThresholds {
    "raw_score >= 0.80" => "Fixed"; "raw_score >= 0.50" => "Partially Fixed"; "raw_score < 0.50" => "Not Fixed"
    "Missing/duplicate criteria, or evaluated coverage < 0.50" => "UNVERIFIABLE"
    "`no_new_vulnerabilities` is a **critical gate**: if its status is `skip` or `invalid`, the verdict is forced to `UNVERIFIABLE` regardless of the numeric score (non-waivable, cannot be out-weighted). If its status is `partial` or `fail`, the numeric score stands but the verdict label is capped one step below Fixed — a score ≥ 0.80 that would otherwise be Fixed becomes Partially Fixed."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:59-66
  MergeReadiness { Fixed => "Ready"; "Partially Fixed" => "Ready with Conditions"; "Not Fixed" => "Not Ready"; UNVERIFIABLE => "Not Ready" }
  // the host recomputes the same algorithm in code (scoring/_engine.sudo, io/_host_score.sudo); these steps are what the model is told
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:68-81
  ScoringExecution {
    "The orchestrator returns its synthesized gates in its structured response — it has no Write tool and the host persists them — and **computes the verdict directly from this matrix** — there is no Bash/shell in the session, so do the arithmetic yourself. Apply this exact algorithm (it mirrors the canonical scoring engine):"
    "1. **Validate the gate set.** Exactly the four gates `root_cause`, `instance_coverage`, `no_new_vulnerabilities`, `security_best_practices` must be present, each exactly once. Any missing or duplicated gate → `fix_status = UNVERIFIABLE`, `raw_score = 0.0`, `gate_scores = {}` — stop here."
    "2. **Per-gate weighted score (evaluated gates only).** A `skip` gate is *unevaluated* — exclude it from BOTH numerator and denominator (weight-neutral). An `invalid` gate (any non-str or unrecognised status) is *evaluated* but scores 0.0 and its weight IS counted in the denominator (fail-closed, not weight-neutral). For each evaluated gate (`pass`/`partial`/`fail`/`invalid`): `weighted_score = weight × status_multiplier` (`pass=1.0`, `partial=0.5`, `fail=0.0`, `invalid=0.0`). Round each to 4 decimal places (this is the per-gate value shown in `gate_scores`)."
    "3. **`raw_score` (renormalized).** `raw_score = (Σ evaluated weighted_scores) ÷ (Σ evaluated gate weights)`, clamped to a maximum of `1.0`, rounded to 4 decimal places. Skipped gates are dropped from BOTH sums, so the score is normalized over the gates actually evaluated (a skip's weight is redistributed, never counted as a failure). When no gate is skipped the denominator is `1.0` and this reduces to the plain weighted sum."
    "4. **Coverage floor.** If the evaluated (non-skip) weights sum to less than `0.50`, coverage is too low to trust a verdict → `fix_status = UNVERIFIABLE`, `raw_score = 0.0` (stop here)."
    "5. **Critical gate.** If `no_new_vulnerabilities` is `skip` or `invalid` → `fix_status = UNVERIFIABLE`, `raw_score = 0.0` (stop here — this check precedes scoring in the engine and cannot be waived by a high numeric score). If it is `partial` or `fail`, the numeric score from step 3 stands, but the verdict label is capped: a score ≥ 0.80 becomes Partially Fixed, not Fixed."
    "6. **`fix_status`** from the Decision Thresholds table (`>=0.80` Fixed, `>=0.50` Partially Fixed, else Not Fixed)."
    "7. **`merge_readiness`** from the Merge Readiness table."
    "8. Apply the secret-exposure rotation cap below if and only if that section applies."
    "Show the per-gate arithmetic (`weight × multiplier = weighted_score`) and the renormalized division (`Σ weighted_score ÷ Σ evaluated weight = raw_score`) in the report `justification`."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:83-105
  InputAndOutputSchema {
    "Top-level array of one finding per entry. Each gate object requires `gate_name` and `status`; `summary`, `evidence`, and `details` are recommended for traceability but not required."
    "All four gates must be present. Missing gates produce `UNVERIFIABLE`. Valid `status` values are `pass`, `partial`, `fail`, `skip`, `invalid`. A `skip` gate is weight-neutral (excluded from the denominator). An `invalid` gate (the engine maps any non-str or unrecognised value here) scores 0.0 and stays in the denominator. If `no_new_vulnerabilities` is `skip` or `invalid`, the verdict is UNVERIFIABLE regardless of all other gates."
    "The output JSON contains `fix_status`, `raw_score`, `justification`, `merge_readiness`, and a `gate_scores` dict keyed by `gate_name`."
  }
  // abstracted: the JSON example at lines 87-99 shows one finding with the four gates, each with gate_name, status, summary, evidence, details
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:107-112
  SessionMarkers {
    "All posted results include an idempotency marker:"
    "- JIRA comments: `<!-- validation-session:{SESSION_ID} -->`"
    "These markers identify which validation run posted each comment. The host (not the agent) posts results after the session exits."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:114-125
  JiraStatusTransitions {
    "After scoring, the agent transitions the JIRA ticket:"
    "Transition failures are non-fatal warnings."
  }
    // table at lines 118-123: Fixed => "Accepted/Done"; "Partially Fixed", "Not Fixed", UNVERIFIABLE => "In Progress"
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:127-146
  CodeLevelSignalsOnly {
    "Applies to all Path A findings, regardless of class."
    "The agent assesses fix completeness from code-level signals: the applied diff (`diff.patch`), source files in the patched workspace tree, build/config files committed to the repo, and the framework's standard security idioms. Operational and process controls do NOT count toward gate scoring and must NOT appear in `recommendations`."
    "The following do NOT downgrade any gate (`root_cause`, `instance_coverage`, `no_new_vulnerabilities`, `security_best_practices`) and must NOT be surfaced as recommendations, for any finding class:"
    "- Manual cyber validation / out-of-band cyber review."
    "- Document or process verification (governance documents, change-management approvals, sign-off workflows, ADR documentation)."
    "- Runtime monitoring / alerting / anomaly detection / SIEM / IDS rules."
    "- WAF / IPS / network-layer controls configured outside the codebase."
    "- GHAS push-protection or secret-scanning enablement (already enabled at the org level)."
    "- Pre-commit hooks (gitleaks, detect-secrets, husky, etc.)."
    "- Attestations or process commitments from teams outside the dev (Cyber, IAM, Compliance) when used as gating evidence."
    "- Any control that does not modify the code being validated."
    "These items MAY be mentioned in passing in `justification` if directly relevant to the finding's narrative, but they cannot be the basis for a partial/fail gate status, and they cannot appear in the `recommendations` array."
    "`recommendations` is reserved for code-level hardening genuinely missing from the fix (e.g., the env-var read lacks error handling; the parameterized query has a fallback path that string-interpolates; another vulnerable instance remains in a sibling file)."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:148-161
  SecretExposureVerification {
    "A specific instance of \"Code-level signals only\" for the hardcoded-credential / API-key / token / password / private-key / connection-string / OAuth-secret class, where the verification commands and the rotation attestation are well-defined. Path A only. Does not apply to injection / auth-bypass / similar findings even if titles contain \"credential.\""
    "Persisted remediation diffs are secret-redacted. Use their paths, hunk ranges, redaction markers, and non-sensitive replacement lines as change evidence; never reconstruct, persist, or place a removed plaintext credential in a search query."
    "- Inspect the patched source at every reported location and confirm that no literal credential remains and the replacement reads from a config-time source (env var / Vault / AWS Secrets Manager / equivalent) or removes the credential entirely."
    "- Run the deterministic `PatternScan(\"secret_exposure\")` fact tool over the patched workspace when it is present in the persona's granted tools. It scans in-scope production files for conservative secret shapes and excludes the redacted `diff.patch`; match records expose only paths and line numbers, followed by a count/limits/truncation summary. Review every candidate relevant to the finding's credential class and affected paths. If the summary reports truncation or skipped files, do not describe the scan as clean; inspect the affected paths with the available read-only tools and state the coverage limit. On a backend without `PatternScan`, use `Read` and credential-name or delimiter searches that do not contain the removed value, and do not claim that PatternScan ran."
    "- Treat a complete scan with no relevant candidates as supporting evidence alongside inspection of the reported locations, not as proof that every opaque credential shape is absent. Do not downgrade a gate merely because exact-value `grep -F` verification is intentionally unavailable."
    "- Record only an abstract result in `justification`; never copy candidate snippets or secret-bearing tool output into persisted narrative."
    "Repository-history hygiene is NOT a gating concern. This workspace has no version-control history -- do not attempt to inspect or rewrite it, and do not recommend history rewriting or history-scrubbing. Once no literal credential remains at the patched locations, the conservative workspace scan has no relevant candidates, and rotation attestation is present, the historical exposure is neutralized by rotation; the residual cryptographic value is zero."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:163-171
  SecretExposureGateMapping {
    "When this section applies:"
    "- `root_cause` passes when the patched workspace tree is clean and the replacement reads from a config-time source (env var / Vault / AWS Secrets Manager / equivalent) or removes the credential entirely."
    "- `security_best_practices` passes when the replacement pattern follows the framework's standard secret-loading idiom."
    "- `instance_coverage`, `no_new_vulnerabilities` evaluate normally."
    "(Per \"Code-level signals only\" above, missing rotation attestation, missing monitoring, missing pre-commit hooks, and missing ADR docs do NOT downgrade these gates. Repository-history state does NOT downgrade these gates either -- see \"Verification\" above. Rotation attestation is handled separately as a verdict gate, below.)"
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:173-180
  RotationAttestation {
    "Look in (a) developer-authored Jira comments (already in the prefetch payload), (b) the PR description, (c) PR comments. Accept any plausible developer statement that the credential has been -- or has been concretely committed to be -- rotated, revoked, regenerated, replaced, or deactivated. Two forms of attestation count:"
    "1. **Done-state.** Past-tense statement that the credential has been rotated, revoked, regenerated, replaced, or deactivated."
    "2. **Scheduled commitment.** Forward-tense statement that pins the rotation to a concrete execution context: a specific date, a scheduled change window, or a tracked change identifier (CRQ, CHG, RFC, INC, ServiceNow number, or equivalent auditable ticket -- which by definition references a real schedule). Any one of these markers is sufficient; multiple environments covered separately (e.g., distinct SBX and PROD entries) strengthen the attestation but are not required."
    "The following do NOT count, regardless of phrasing: vague intentions (\"we should rotate\", \"TODO: rotate\", \"will rotate eventually\"), unscheduled future-tense with no date, window, or tracking identifier, bot/orchestrator-authored text, and screenshot-only comments without a text body."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:182-191
  SecretExposureVerdict {
    "Standard threshold scoring computes a base verdict from `raw_score` (>=0.80 Fixed, 0.50-0.79 Partially Fixed, <0.50 Not Fixed). Rotation attestation then applies as a verdict cap, independent of which gates passed:"
    "- Attestation present -> base verdict stands."
    "- Attestation missing -> verdict is capped at `Partially Fixed`. A `Fixed` base verdict downgrades to `Partially Fixed`; a `Partially Fixed` or `Not Fixed` base verdict is unchanged."
    "When attestation is missing, the `recommendations` array MUST include this exact item: `\"Reply with text confirming that the leaked credential has been rotated, revoked, or regenerated -- or with a scheduled rotation date, change window, or tracked change identifier (e.g., CRQ/CHG/RFC number).\"` Code-level recommendations driven by standard gate failures (per the standard matrix) sit alongside it; the rotation request neither replaces them nor is replaced by them."
    "When attestation is present, recommendations follow the standard matrix for any failed/partial gates."
  }
  // prompt-src: vvaharness/validation/claude_config/rules/scoring-matrix.md:193-200
  SecretExposureAuditLine {
    "When this section applies, include one truthful audit line based on the tools actually used:"
    "- With PatternScan: \"Secret-exposure handling applied. Patched locations inspected -> <N> clean, <N> with a remaining literal. PatternScan(secret_exposure) -> <count> relevant candidate locations; complete (or: truncated: <safe summary reasons>). Rotation attestation: `<source + brief quote>` (or: not found).\""
    "- Without PatternScan: \"Secret-exposure handling applied. Patched locations inspected with available Read/Grep/Glob tools using credential names or delimiters -> <N> clean, <N> with a remaining literal; deterministic PatternScan unavailable. Rotation attestation: `<source + brief quote>` (or: not found).\""
    "Do NOT include candidate snippets, secret-bearing command output, or actual secret values; describe verification abstractly per the \"Never echo plaintext secrets\" rule."
  }
  // preserved: "After scoring, the agent transitions the JIRA ticket" (line 116) conflicts with "The host (not the agent) posts results" (line 112) and with the system prompt's "No JIRA calls"
  // preserved: rotation attestation is to be looked up in "Jira comments (already in the prefetch payload)", "the PR description" and "PR comments" (line 175), none of which the system prompt lists as inputs
  // preserved: step 4 calls a coverage floor below 0.50 UNVERIFIABLE; scoring/_engine.sudo records how the code treats it
}
