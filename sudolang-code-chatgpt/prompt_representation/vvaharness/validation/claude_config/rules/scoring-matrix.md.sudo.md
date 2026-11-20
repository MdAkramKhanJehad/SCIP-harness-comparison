# vvaharness/validation/claude_config/rules/scoring-matrix.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Requested scoring algorithm, stopping gates and rotation cap

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:18-200
Constraints {
  Requested weights are root_cause=0.43, instance_coverage=0.2467, no_new_vulnerabilities=0.1867 and security_best_practices=0.1366; branch_targeting is removed.
  if (the gate set is not exactly those four once each) { The requested result is UNVERIFIABLE, raw_score=0 and empty gate_scores; stop this scoring procedure. }
  Requested multipliers are pass=1, partial=0.5, fail=0 and invalid=0. Skip is unevaluated and excluded from numerator AND denominator; invalid remains evaluated with zero credit.
  Requested per-gate values are weight times multiplier rounded to four decimals; raw_score is their sum divided by evaluated weights, capped at 1 and rounded to four decimals.
  if (evaluated weight is below 0.50) { The requested result is UNVERIFIABLE with score zero; stop. }
  if (no_new_vulnerabilities is skip or invalid) { The requested result is UNVERIFIABLE with score zero, regardless of the arithmetic. }
  Otherwise requested labels use >=0.80 Fixed, >=0.50 Partially Fixed, else Not Fixed; partial/fail critical gate caps Fixed at Partially Fixed without altering its numeric score.
  Requested readiness maps Fixed to Ready, Partially Fixed to Ready with Conditions, and Not Fixed/UNVERIFIABLE to Not Ready.
  The requested justification shows weighted arithmetic and renormalized division; preserve the source note that the engine checks the critical gate before scoring although this numbered procedure states it later.
  Operational/process controls are excluded from gate downgrades and recommendations; relevant passing context may appear only in justification. Recommendations otherwise concern code-level hardening.
  For applicable Path A secret-exposure classes: inspect every patched location and normal config-time secret loading; use granted PatternScan or safe name/delimiter searches, disclose limits, and never reconstruct or persist the removed secret. No history inspection/rewriting is requested.
  Rotation is a separate verdict gate, not a downgrade to the four code gates. Accept plausible developer past-tense rotation/revocation/replacement/deactivation or a concrete future date/window/tracked change identifier. Exclude vague/unscheduled, bot-authored or screenshot-only claims.
  if (applicable rotation attestation is absent) {
    The requested Fixed label becomes Partially Fixed; lower base labels stay as they are.
    The model is asked to include the exact source rotation-attestation recommendation alongside any code recommendations and a truthful tool-dependent audit line.
  }
  The source both says the host posts results and later asks the agent to transition JIRA; retain that tension alongside the no-JIRA-tool instructions, without inventing a call.
}
```

Supply relationship: validation configuration/session/launcher and subagent loaders select system, rule, skill and persona text; effective permissions are separately built by executable code.

# Scoring Matrix (PRD Section 8.6 -- Fix Validation)

## Four Criteria

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:20-25
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Criterion | Weight | Description | PRD Reference | |-----------|--------|-------------|---------------| | root_cause | 0.43 | The applied diff modifies the vulnerable code path with proper mitigation | FC1 | | instance_coverage | 0.2467 | All affected files in the diff; no remaining vulnerable code paths | FC2 | | no_new_vulnerabilities | 0.1867 | Code review shows fix doesn't introduce new security issues | FC3 | | security_best_practices | 0.1366 | Fix uses framework-recommended patterns (parameterized queries, encoding, etc.) | FC4 |
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:27-27
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Weights sum to 1.00.
  The request retains this source rule, criterion or rationale, with its original modal force: The git-oriented `branch_targeting` gate (formerly 0.10) is removed: s11 validates a pre-applied diff on a dirty tree with no release-branch concept.
  The request retains this source rule, criterion or rationale, with its original modal force: The remaining four weights are renormalized to sum to 1.0.
}
```

## Status Multipliers

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:31-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Status | Multiplier | |--------|------------| | pass | 1.0 | | partial | 0.5 | | fail | 0.0 | | skip | 0.0 |
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:38-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Synthesized gates should normally be `pass`/`partial`/`fail`.
  The request retains this source rule, criterion or rationale, with its original modal force: A `skip` marks an *unevaluated* gate: it is excluded from scoring entirely -- dropped from BOTH the numerator and the denominator -- so it is weight-neutral (it neither earns nor drags credit).
  The request retains this source rule, criterion or rationale, with its original modal force: The score is renormalized over the gates actually evaluated; a skip's weight is redistributed across the evaluated gates, not counted as a failure (see Scoring Execution).
}
```

## Decision Thresholds

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:46-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Condition | Fix Status | |-----------|-----------| | raw_score >= 0.80 | Fixed | | raw_score >= 0.50 | Partially Fixed | | raw_score < 0.50 | Not Fixed | | Missing/duplicate criteria, or evaluated coverage < 0.50 | UNVERIFIABLE |
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:53-57
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `no_new_vulnerabilities` is a critical gate: if its status is `skip` or `invalid`, the verdict is forced to `UNVERIFIABLE` regardless of the numeric score (non-waivable, cannot be out-weighted).
  The requested conditional/temporal rule is: If its status is `partial` or `fail`, the numeric score stands but the verdict label is capped one step below Fixed — a score ≥ 0.80 that would otherwise be Fixed becomes Partially Fixed.
}
```

## Merge Readiness

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:61-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Fix Status | Merge Readiness | |-----------|----------------| | Fixed | Ready | | Partially Fixed | Ready with Conditions | | Not Fixed | Not Ready | | UNVERIFIABLE | Not Ready |
}
```

## Scoring Execution

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:70-70
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The orchestrator returns its synthesized gates in its structured response — it has no Write tool and the host persists them — and computes the verdict directly from this matrix — there is no Bash/shell in the session, so do the arithmetic yourself.
  The model is asked to adopt this exact algorithm (it mirrors the canonical scoring engine):
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:72-72
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Validate the gate set. Exactly the four gates `root_cause`, `instance_coverage`, `no_new_vulnerabilities`, `security_best_practices` must be present, each exactly once.
  The request retains this source rule, criterion or rationale, with its original modal force: Any missing or duplicated gate → `fix_status = UNVERIFIABLE`, `raw_score = 0.0`, `gate_scores = {}` — stop here.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:73-73
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Per-gate weighted score (evaluated gates only). A `skip` gate is *unevaluated* — exclude it from BOTH numerator and denominator (weight-neutral).
  The request retains this source rule, criterion or rationale, with its original modal force: An `invalid` gate (any non-str or unrecognised status) is *evaluated* but scores 0.0 and its weight IS counted in the denominator (fail-closed, not weight-neutral).
  The requested conditional/temporal rule is: For each evaluated gate (`pass`/`partial`/`fail`/`invalid`): `weighted_score = weight × status_multiplier` (`pass=1.0`, `partial=0.5`, `fail=0.0`, `invalid=0.0`).
  The request retains this source rule, criterion or rationale, with its original modal force: Round each to 4 decimal places (this is the per-gate value shown in `gate_scores`).
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:74-74
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `raw_score` (renormalized). `raw_score = (Σ evaluated weighted_scores) ÷ (Σ evaluated gate weights)`, clamped to a maximum of `1.0`, rounded to 4 decimal places.
  The request retains this source rule, criterion or rationale, with its original modal force: Skipped gates are dropped from BOTH sums, so the score is normalized over the gates actually evaluated (a skip's weight is redistributed, never counted as a failure).
  The requested conditional/temporal rule is: When no gate is skipped the denominator is `1.0` and this reduces to the plain weighted sum.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:75-75
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Coverage floor. If the evaluated (non-skip) weights sum to less than `0.50`, coverage is too low to trust a verdict → `fix_status = UNVERIFIABLE`, `raw_score = 0.0` (stop here).
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:76-76
// Source list marker 5.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Critical gate. If `no_new_vulnerabilities` is `skip` or `invalid` → `fix_status = UNVERIFIABLE`, `raw_score = 0.0` (stop here — this check precedes scoring in the engine and cannot be waived by a high numeric score).
  The requested conditional/temporal rule is: If it is `partial` or `fail`, the numeric score from step 3 stands, but the verdict label is capped: a score ≥ 0.80 becomes Partially Fixed, not Fixed.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:77-77
// Source list marker 6.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `fix_status` from the Decision Thresholds table (`>=0.80` Fixed, `>=0.50` Partially Fixed, else Not Fixed).
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:78-78
// Source list marker 7.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `merge_readiness` from the Merge Readiness table.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:79-79
// Source list marker 8.; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to adopt the secret-exposure rotation cap below if and only if that section applies.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:81-81
Constraints {
  The requested evidence/output includes the per-gate arithmetic (`weight × multiplier = weighted_score`) and the renormalized division (`Σ weighted_score ÷ Σ evaluated weight = raw_score`) in the report `justification`.
}
```

### Input schema (`synthesized_gates.json`)

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:85-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Top-level array of one finding per entry.
  The request retains this source rule, criterion or rationale, with its original modal force: Each gate object requires `gate_name` and `status`; `summary`, `evidence`, and `details` are recommended for traceability but not required.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:87-99
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  The requested example format/pattern includes tracking_id with source contract "FINDING-XXXXXXX",.
  The requested example format/pattern includes gates with source contract [.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (json):

``````text
[
  {
    "tracking_id": "FINDING-XXXXXXX",
    "gates": [
      {"gate_name": "root_cause",              "status": "pass", "summary": "...", "evidence": [], "details": ""},
      {"gate_name": "instance_coverage",       "status": "pass", "summary": "...", "evidence": [], "details": ""},
      {"gate_name": "no_new_vulnerabilities",  "status": "pass", "summary": "...", "evidence": [], "details": ""},
      {"gate_name": "security_best_practices", "status": "pass", "summary": "...", "evidence": [], "details": ""}
    ]
  }
]
``````

```sudo
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:101-101
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: All four gates must be present.
  The request retains this source rule, criterion or rationale, with its original modal force: Missing gates produce `UNVERIFIABLE`.
  The request retains this source rule, criterion or rationale, with its original modal force: Valid `status` values are `pass`, `partial`, `fail`, `skip`, `invalid`.
  The request retains this source rule, criterion or rationale, with its original modal force: A `skip` gate is weight-neutral (excluded from the denominator).
  The request retains this source rule, criterion or rationale, with its original modal force: An `invalid` gate (the engine maps any non-str or unrecognised value here) scores 0.0 and stays in the denominator.
  The requested conditional/temporal rule is: If `no_new_vulnerabilities` is `skip` or `invalid`, the verdict is UNVERIFIABLE regardless of all other gates.
}
```

### Output

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:105-105
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The output JSON contains `fix_status`, `raw_score`, `justification`, `merge_readiness`, and a `gate_scores` dict keyed by `gate_name`.
}
```

## Session Markers

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:109-109
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: All posted results include an idempotency marker:
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:110-110
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: JIRA comments: `<!-- validation-session:{SESSION_ID} -->`
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:112-112
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: These markers identify which validation run posted each comment.
  The request retains this source rule, criterion or rationale, with its original modal force: The host (not the agent) posts results after the session exits.
}
```

## JIRA Status Transitions

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:116-116
Constraints {
  The requested conditional/temporal rule is: After scoring, the agent transitions the JIRA ticket:
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:118-123
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Fix Status | Target Status | |-----------|--------------| | Fixed | Accepted/Done | | Partially Fixed | In Progress | | Not Fixed | In Progress | | UNVERIFIABLE | In Progress |
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:125-125
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Transition failures are non-fatal warnings.
}
```

## Code-level signals only

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:129-129
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Applies to all Path A findings, regardless of class.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:131-131
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The agent assesses fix completeness from code-level signals: the applied diff (`diff.patch`), source files in the patched workspace tree, build/config files committed to the repo, and the framework's standard security idioms.
  The request retains this source rule, criterion or rationale, with its original modal force: Operational and process controls do NOT count toward gate scoring and must NOT appear in `recommendations`.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:133-133
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The following do NOT downgrade any gate (`root_cause`, `instance_coverage`, `no_new_vulnerabilities`, `security_best_practices`) and must NOT be surfaced as recommendations, for any finding class:
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:135-135
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Manual cyber validation / out-of-band cyber review.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:136-136
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Document or process verification (governance documents, change-management approvals, sign-off workflows, ADR documentation).
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:137-137
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Runtime monitoring / alerting / anomaly detection / SIEM / IDS rules.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:138-138
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WAF / IPS / network-layer controls configured outside the codebase.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:139-139
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: GHAS push-protection or secret-scanning enablement (already enabled at the org level).
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:140-140
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Pre-commit hooks (gitleaks, detect-secrets, husky, etc.).
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:141-141
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Attestations or process commitments from teams outside the dev (Cyber, IAM, Compliance) when used as gating evidence.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:142-142
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Any control that does not modify the code being validated.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:144-144
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: These items MAY be mentioned in passing in `justification` if directly relevant to the finding's narrative, but they cannot be the basis for a partial/fail gate status, and they cannot appear in the `recommendations` array.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:146-146
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `recommendations` is reserved for code-level hardening genuinely missing from the fix (e.g., the env-var read lacks error handling; the parameterized query has a fallback path that string-interpolates; another vulnerable instance remains in a sibling file).
}
```

## Secret-exposure handling

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:150-150
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A specific instance of "Code-level signals only" for the hardcoded-credential / API-key / token / password / private-key / connection-string / OAuth-secret class, where the verification commands and the rotation attestation are well-defined.
  The request retains this source rule, criterion or rationale, with its original modal force: Path A only.
  The request retains this source rule, criterion or rationale, with its original modal force: Does not apply to injection / auth-bypass / similar findings even if titles contain "credential."
}
```

### Verification (non-negotiable)

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:154-154
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Persisted remediation diffs are secret-redacted.
  The model is asked to adopt their paths, hunk ranges, redaction markers, and non-sensitive replacement lines as change evidence; never reconstruct, persist, or place a removed plaintext credential in a search query.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:156-156
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to obtain and examine the patched source at every reported location and confirm that no literal credential remains and the replacement reads from a config-time source (env var / Vault / AWS Secrets Manager / equivalent) or removes the credential entirely.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:157-157
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  Within this instruction's source scope, the model is asked to invoke the deterministic `PatternScan("secret_exposure")` fact tool over the patched workspace when it is present in the persona's granted tools.
  The request retains this source rule, criterion or rationale, with its original modal force: It scans in-scope production files for conservative secret shapes and excludes the redacted `diff.patch`; match records expose only paths and line numbers, followed by a count/limits/truncation summary.
  The model is asked to obtain and examine every candidate relevant to the finding's credential class and affected paths.
  The requested conditional/temporal rule is: If the summary reports truncation or skipped files, do not describe the scan as clean; inspect the affected paths with the available read-only tools and state the coverage limit.
  The request retains this source rule, criterion or rationale, with its original modal force: On a backend without `PatternScan`, use `Read` and credential-name or delimiter searches that do not contain the removed value, and do not claim that PatternScan ran.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:158-158
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Treat a complete scan with no relevant candidates as supporting evidence alongside inspection of the reported locations, not as proof that every opaque credential shape is absent.
  The requested model behavior excludes downgrade a gate merely because exact-value `grep -F` verification is intentionally unavailable.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:159-159
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested evidence/output includes only an abstract result in `justification`; never copy candidate snippets or secret-bearing tool output into persisted narrative.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:161-161
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Repository-history hygiene is NOT a gating concern.
  The request retains this source rule, criterion or rationale, with its original modal force: This workspace has no version-control history -- do not attempt to inspect or rewrite it, and do not recommend history rewriting or history-scrubbing.
  The request retains this source rule, criterion or rationale, with its original modal force: Once no literal credential remains at the patched locations, the conservative workspace scan has no relevant candidates, and rotation attestation is present, the historical exposure is neutralized by rotation; the residual cryptographic value is zero.
}
```

### Gate mapping

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:165-165
Constraints {
  The requested conditional/temporal rule is: When this section applies:
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:167-167
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `root_cause` passes when the patched workspace tree is clean and the replacement reads from a config-time source (env var / Vault / AWS Secrets Manager / equivalent) or removes the credential entirely.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:168-168
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `security_best_practices` passes when the replacement pattern follows the framework's standard secret-loading idiom.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:169-169
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `instance_coverage`, `no_new_vulnerabilities` evaluate normally.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:171-171
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (Per "Code-level signals only" above, missing rotation attestation, missing monitoring, missing pre-commit hooks, and missing ADR docs do NOT downgrade these gates.
  The request retains this source rule, criterion or rationale, with its original modal force: Repository-history state does NOT downgrade these gates either -- see "Verification" above.
  The request retains this source rule, criterion or rationale, with its original modal force: Rotation attestation is handled separately as a verdict gate, below.)
}
```

### Rotation attestation

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:175-175
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Look in (a) developer-authored Jira comments (already in the prefetch payload), (b) the PR description, (c) PR comments.
  The request retains this source rule, criterion or rationale, with its original modal force: Accept any plausible developer statement that the credential has been -- or has been concretely committed to be -- rotated, revoked, regenerated, replaced, or deactivated.
  The request retains this source rule, criterion or rationale, with its original modal force: Two forms of attestation count:
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:177-177
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Done-state. Past-tense statement that the credential has been rotated, revoked, regenerated, replaced, or deactivated.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:178-178
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Scheduled commitment. Forward-tense statement that pins the rotation to a concrete execution context: a specific date, a scheduled change window, or a tracked change identifier (CRQ, CHG, RFC, INC, ServiceNow number, or equivalent auditable ticket -- which by definition references a real schedule).
  The request retains this source rule, criterion or rationale, with its original modal force: Any one of these markers is sufficient; multiple environments covered separately (e.g., distinct SBX and PROD entries) strengthen the attestation but are not required.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:180-180
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The following do NOT count, regardless of phrasing: vague intentions ("we should rotate", "TODO: rotate", "will rotate eventually"), unscheduled future-tense with no date, window, or tracking identifier, bot/orchestrator-authored text, and screenshot-only comments without a text body.
}
```

### Verdict and recommendations

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:184-184
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Standard threshold scoring computes a base verdict from `raw_score` (>=0.80 Fixed, 0.50-0.79 Partially Fixed, <0.50 Not Fixed).
  The request retains this source rule, criterion or rationale, with its original modal force: Rotation attestation then applies as a verdict cap, independent of which gates passed:
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:186-186
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Attestation present -> base verdict stands.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:187-187
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Attestation missing -> verdict is capped at `Partially Fixed`.
  The request retains this source rule, criterion or rationale, with its original modal force: A `Fixed` base verdict downgrades to `Partially Fixed`; a `Partially Fixed` or `Not Fixed` base verdict is unchanged.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:189-189
Constraints {
  The requested conditional/temporal rule is: When attestation is missing, the `recommendations` array MUST include this exact item: `"Reply with text confirming that the leaked credential has been rotated, revoked, or regenerated -- or with a scheduled rotation date, change window, or tracked change identifier (e.g., CRQ/CHG/RFC number)."` Code-level recommendations driven by standard gate failures (per the standard matrix) sit alongside it; the rotation request neither replaces them nor is replaced by them.
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:191-191
Constraints {
  The requested conditional/temporal rule is: When attestation is present, recommendations follow the standard matrix for any failed/partial gates.
}
```

### Audit line in `justification`

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:195-195
Constraints {
  The requested conditional/temporal rule is: When this section applies, include one truthful audit line based on the tools actually used:
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:197-197
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: With PatternScan: "Secret-exposure handling applied.
  The request retains this source rule, criterion or rationale, with its original modal force: Patched locations inspected -> <N> clean, <N> with a remaining literal.
  The request retains this source rule, criterion or rationale, with its original modal force: PatternScan(secret_exposure) -> <count> relevant candidate locations; complete (or: truncated: <safe summary reasons>).
  The request retains this source rule, criterion or rationale, with its original modal force: Rotation attestation: `<source + brief quote>` (or: not found)."
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:198-198
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Without PatternScan: "Secret-exposure handling applied.
  The request retains this source rule, criterion or rationale, with its original modal force: Patched locations inspected with available Read/Grep/Glob tools using credential names or delimiters -> <N> clean, <N> with a remaining literal; deterministic PatternScan unavailable.
  The request retains this source rule, criterion or rationale, with its original modal force: Rotation attestation: `<source + brief quote>` (or: not found)."
}
```

```sudo
// Source: vvaharness/validation/claude_config/rules/scoring-matrix.md:200-200
Constraints {
  The requested model behavior excludes include candidate snippets, secret-bearing command output, or actual secret values; describe verification abstractly per the "Never echo plaintext secrets" rule.
}
```

