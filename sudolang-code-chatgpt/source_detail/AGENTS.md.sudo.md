# AGENTS.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

Supply relationship: operator-facing agent instructions; not an automatic scan-stage action. Packaged installation is separately represented in agentdoc/setup code.

# AGENTS.md — How to operate vvaharness (for AI coding agents)

```sudo
// Source: AGENTS.md:18-20
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: vvaharness is a *released* command-line security-scanning product.
  The request retains this source rule, criterion or rationale, with its original modal force: It finds vulnerability candidates in a codebase and writes a Markdown report and SARIF 2.1.0.
  The request retains this source rule, criterion or rationale, with its original modal force: the model's job is to operate it, not to develop or repair it.
}
```

```sudo
// Source: AGENTS.md:22-23
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: This is the operating manual for AI agents (Claude Code, GitHub Copilot, Cursor, Codex and others).
  The model is asked to obtain and examine it fully before you run any command.
}
```

## The four rules

```sudo
// Source: AGENTS.md:27-29
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes modify the product's source to make a scan run. Files under `vvaharness/` are the shipped tool. *Why:* a hand-edited tool gives unsupported, non-reproducible results.
}
```

```sudo
// Source: AGENTS.md:30-36
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes hand-write config files. Pick a shipped profile with `--config`.
  The request retains this source rule, criterion or rationale, with its original modal force: The one sanctioned exception is a git-ignored `config.local.yaml` in the same directory as the chosen config.
  The request retains this source rule, criterion or rationale, with its original modal force: For a shipped profile, that directory is `vvaharness/config/profiles/`: the overlay is the only file the model may add under `vvaharness/`, and it applies to every profile there.
  The request retains this source rule, criterion or rationale, with its original modal force: The tool deep-merges it and logs `config overlay: … applied`. *Why:* shipped profiles are tested combinations of models and stages.
}
```

```sudo
// Source: AGENTS.md:37-40
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: On any failure, run `vvaharness setup` (or `doctor`) with the same `--config`, fix the environment it points to, and re-run the same command. *Why:* the checks name the exact missing credential, endpoint or dependency, but only for the profile the model pass.
}
```

```sudo
// Source: AGENTS.md:41-43
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: **Scan only code the user is authorized to scan.
  The requested model behavior excludes arm exploit verification or fix mode unless the user asks.** *Why:* exploit verification sends live attack traffic, and fix mode edits the user's source.
}
```

```sudo
// Source: AGENTS.md:45-47
Constraints {
  The requested conditional/temporal rule is: If the tool misbehaves after `setup` is green, report a bug.
  The requested model behavior excludes patch around it.
  The request retains this source rule, criterion or rationale, with its original modal force: Attach the traceback from `<target>/security-scan/*_errors.jsonl`.
  The model is asked to establish any trace for secrets before you share it, because bug reports are public.
}
```

## Before you scan

```sudo
// Source: AGENTS.md:51-53
Constraints {
  The model is asked to establish the user may scan the code.
  The request retains this source rule, criterion or rationale, with its original modal force: Prompts send target source to the configured model provider.
  The request retains this source rule, criterion or rationale, with its original modal force: Scans spend real tokens, so run `vvaharness estimate --repo <path>` first (no spend).
}
```

```sudo
// Source: AGENTS.md:55-58
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Keep `VVAHARNESS_INGEST_URL` and `VVAHARNESS_INGEST_TOKEN` unset unless the user wants a report upload.
  The requested conditional/temporal rule is: When both are set (a stale `.env` value counts), each scan uploads its report and SARIF to that URL after S9, also with `--stop-after s9`.
}
```

## First run

```sudo
// Source: AGENTS.md:62-65
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (bash):

``````text
uv sync                     # this is a uv project
uv run vvaharness setup     # or: pipx install . / pip install . then `vvaharness setup`
``````

```sudo
```

```sudo
// Source: AGENTS.md:67-69
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Do what `setup` reports and re-run it until green.
  The request retains this source rule, criterion or rationale, with its original modal force: Re-run it with `--config <profile>` after the model choose a profile; each profile needs different credentials.
}
```

```sudo
// Source: AGENTS.md:71-73
Constraints {
  Within this instruction's source scope, the model is asked to invoke `vvaharness setup --install-agents` only when the user asks, and never inside the scan target, because it adds files to the current directory.
  The request retains this source rule, criterion or rationale, with its original modal force: It writes a short packaged version of these rules and never overwrites a file:
}
```

```sudo
// Source: AGENTS.md:75-75
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `AGENTS.md` and `.github/copilot-instructions.md` in the current directory.
}
```

```sudo
// Source: AGENTS.md:76-77
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `CLAUDE.md` in the current directory and `~/.claude/skills/vvaharness/SKILL.md` in the model's home directory, when `claude` is on `PATH`.
}
```

```sudo
// Source: AGENTS.md:78-78
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `GEMINI.md` in the current directory, when `gemini` is on `PATH`.
}
```

## Choose a profile

```sudo
// Source: AGENTS.md:82-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Pass a profile as `--config vvaharness/config/profiles/<name>.yaml`.
  The request retains this source rule, criterion or rationale, with its original modal force: The path is relative to the checkout root; from another directory, pass the absolute path.
  The request retains this source rule, criterion or rationale, with its original modal force: With no `--config`, a `config.yaml` in the current directory wins; otherwise the packaged `default` runs.
  The request retains this source rule, criterion or rationale, with its original modal force: The effective path prints as `config: …`.
}
```

```sudo
// Source: AGENTS.md:87-93
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Profile | Detection route | S10 remediation / S11 validation | Credentials | Extra needs | |---|---|---|---|---| | `default` | DeepAgents, Anthropic | Off / off | One Anthropic credential: `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN` or `ANTHROPIC_SDK_API_KEY` | None | | `sdk` | Anthropic SDK | On / on | `ANTHROPIC_SDK_API_KEY` (or a standard Anthropic credential) | S11 needs a `claude` CLI on `PATH` (or an absolute path in `VVAHARNESS_CLAUDE_BINARY`) and `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN` or a `claude` login | | `full` | DeepAgents, Anthropic | On / on | One Anthropic credential | `OPENAI_API_KEY` only when exploit verification is armed (its `judge` uses OpenAI) | | `taint` | DeepAgents, Anthropic | Off / off | One Anthropic credential | None; alternate tuning, not a separate taint engine | | `semgrep` | DeepAgents, Anthropic | Off / off | One Anthropic credential | A `semgrep` binary on `PATH`; the shipped registry rulesets need network access |
}
```

## Use an Anthropic-compatible gateway (common cause of 401)

```sudo
// Source: AGENTS.md:97-98
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A JWT-shaped key (`eyJ…`) is a gateway token.
  The request retains this source rule, criterion or rationale, with its original modal force: It returns 401 against the public API until the model point the tool at the gateway.
  The request retains this source rule, criterion or rationale, with its original modal force: Set these in the model's shell or `.env`:
}
```

```sudo
// Source: AGENTS.md:100-104
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (bash):

``````text
export ANTHROPIC_BASE_URL=https://<your-gateway>/
export SSL_CERT_FILE=/path/to/ca-bundle.pem        # only if the gateway uses a private CA
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1    # only on "400 invalid beta flag"
``````

```sudo
```

```sudo
// Source: AGENTS.md:106-109
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Route | Endpoint variable | CA variable | |---|---|---| | DeepAgents roles on Anthropic, `via: sdk` roles | `ANTHROPIC_BASE_URL` (`ANTHROPIC_SDK_BASE_URL` overrides it when set) | `SSL_CERT_FILE` or `ANTHROPIC_SDK_CA_CERT` | | `via: cli` roles, S11 launcher | `ANTHROPIC_BASE_URL` | `NODE_EXTRA_CA_CERTS` |
}
```

```sudo
// Source: AGENTS.md:111-112
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested conditional/temporal rule is: If a `setup` endpoint row fails, set `ANTHROPIC_BASE_URL` to your gateway, as the row says.
}
```

## Run a scan

```sudo
// Source: AGENTS.md:116-119
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (bash):

``````text
vvaharness estimate --repo /path/to/target                    # scope/cost preview, no spend
vvaharness scan --repo /path/to/target --stop-after s9 [--config <profile>]
``````

```sudo
```

```sudo
// Source: AGENTS.md:121-123
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `--stop-after s9` ends the scan after the report and SARIF (S0–S9) and skips S10 and S11 with any profile.
  The request retains this source rule, criterion or rationale, with its original modal force: It does not turn off exploit verification (S6) or the report upload.
}
```

```sudo
// Source: AGENTS.md:124-124
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Optional `--application-id <id>` tags the SARIF and drives severity context.
}
```

```sudo
// Source: AGENTS.md:125-125
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Scope a large repo with `--repo <subdir>` or stop early with `--stop-after s3`.
}
```

```sudo
// Source: AGENTS.md:126-128
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Each stage prints `▶` (a spinner on a terminal), then `✓`, `⚠` (finished, logged errors) or `✗` (failed). `scan_progress.enabled` (off in `sdk`) adds `[progress]` lines.
}
```

```sudo
// Source: AGENTS.md:129-130
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: S0 seeds the scan at no token cost: built-in patterns match Python input sources and common sink call names in every file. S1–S9 run for every language.
}
```

## Remediation (S10) and validation (S11)

```sudo
// Source: AGENTS.md:134-148
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: > [!WARNING] > S10 remediation edits files in the target repo. Fix mode applies patches > and writes `<repo>/security-remediation/`. `sdk` and `full` enable it, and > `--remediate` enables it on any profile.
  Within this instruction's source scope, the model is asked to invoke it only when the user asks, on a > clean working tree they can review. `--stop-after s9` skips S10 and S11 with > any profile, even with `--remediate`. > > If the target has a symlink that points outside it, dangles or loops, S10 > prints `[remediate] REFUSING fix mode` and runs report-only: it proposes > fixes and edits no source file on `via: sdk`, `via: openai` and > `via: deepagents`.
  The request retains this source rule, criterion or rationale, with its original modal force: On `via: cli`, list only `Read` and `Grep` in > `step_remediate.allowed_tools` before the model run S10 on that route, because > report-only there keeps every listed tool.
  The request retains this source rule, criterion or rationale, with its original modal force: Report that to the user, and > offer to scan a copy without the link.
  The requested model behavior excludes delete the link without > asking. *Why:* the link is part of the user's checkout.
}
```

```sudo
// Source: AGENTS.md:150-151
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `--remediate` enables S10 only.
  The request retains this source rule, criterion or rationale, with its original modal force: In-scan S11 needs `step_validate.enabled: true`; there is no scan `--validate` flag.
}
```

```sudo
// Source: AGENTS.md:152-156
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `vvaharness remediate --repo <path>` remediates a prior scan's findings.
  The request retains this source rule, criterion or rationale, with its original modal force: Its default is fix mode, which edits source; `--mode report-only` proposes fixes without edits on `via: sdk`, `via: openai` and `via: deepagents`.
  The request retains this source rule, criterion or rationale, with its original modal force: On `via: cli`, list only `Read` and `Grep` in `step_remediate.allowed_tools` first, because that route keeps every listed tool in report-only too.
}
```

```sudo
// Source: AGENTS.md:157-159
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `vvaharness validate --repo <path>` runs an adversarial review panel over applied fixes.
  The request retains this source rule, criterion or rationale, with its original modal force: It never edits source; it writes its verdicts under `<repo>/security-remediation/`.
  The request retains this source rule, criterion or rationale, with its original modal force: Re-runs skip validated findings.
}
```

```sudo
// Source: AGENTS.md:160-164
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `validate` judges only cases that `remediate` or in-scan S10 recorded on this machine for the same path.
  The request retains this source rule, criterion or rationale, with its original modal force: It skips other cases with `no S10 record for this case`.
  The request retains this source rule, criterion or rationale, with its original modal force: A new scan without `--resume` clears those records, so run `validate` before the next scan. *Why:* a case file committed to the repository is untrusted input.
}
```

```sudo
// Source: AGENTS.md:165-168
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Leave `validate --workspace` unset, or pass a new or empty directory outside the repository; otherwise `validate` exits `1`. *Why:* a workspace inside the repository loads the target's own `CLAUDE.md` as instructions for the review panel.
}
```

## Exploit verification (Beta — API only)

```sudo
// Source: AGENTS.md:172-184
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: > [!WARNING] > Exploit verification sends live attack traffic, including state-changing > requests, to a localhost target. It needs a Postman/OpenAPI/Swagger > collection and checks only findings that map to an HTTP endpoint; all others > stay static-analysis only. > > - It turns on when `EV_API_COLLECTION` is set.
  The request retains this source rule, criterion or rationale, with its original modal force: A stale value in the loaded > `.env` counts: `./.env`, else `~/.env`.
  The request retains this source rule, criterion or rationale, with its original modal force: The `[env] loaded …` line names the > file. > - `--resume` turns it back on for a run that had it, even with the variable > unset. > - To send no traffic, unset `EV_API_COLLECTION` and start a fresh run > without `--resume`.
}
```

```sudo
// Source: AGENTS.md:186-186
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Arm it only when the user asks, against a disposable local deployment.
}
```

```sudo
// Source: AGENTS.md:187-188
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `scan --stop-after ev` parses the collection, probes reachability and stops before S0: no code graph, no model spend.
}
```

```sudo
// Source: AGENTS.md:189-190
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `vvaharness ev-replay --repo <path>` re-checks exploit-verified findings against a redeployed target; it needs a prior armed scan and `EV_TARGET_URL`.
}
```

## Outputs

```sudo
// Source: AGENTS.md:194-199
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Artifact | Location | |---|---| | Markdown report and SARIF | `<target>/security-scan/*_report.md`, `*_report.sarif` | | Typed findings for tools and `remediate` | `<target>/security-scan/findings.json` | | Non-fatal stage errors | `<target>/security-scan/*_errors.jsonl` (only when a stage logged one) | | Run manifest (models, config, timing) | `run_manifest_*.json` in the current directory |
}
```

```sudo
// Source: AGENTS.md:201-201
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Full list: [USER_GUIDE.md, Output](docs/USER_GUIDE.md#6-output).
}
```

```sudo
// Source: AGENTS.md:203-203
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Findings are triage candidates, not confirmed vulnerabilities; say so in summaries.
}
```

## When a scan fails

```sudo
// Source: AGENTS.md:207-207
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to obtain and examine the one-line `✗ scan failed: …` message.
}
```

```sudo
// Source: AGENTS.md:208-209
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  Within this instruction's source scope, the model is asked to invoke `vvaharness doctor --config <profile>` and fix every ✗ it reports (usually a credential or `ANTHROPIC_BASE_URL`).
}
```

```sudo
// Source: AGENTS.md:210-210
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Re-run the same scan command.
  The request retains this source rule, criterion or rationale, with its original modal force: Add `VVAHARNESS_DEBUG=1` for a full trace.
}
```

```sudo
// Source: AGENTS.md:211-211
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Still failing with a green `doctor`?
  The request retains this source rule, criterion or rationale, with its original modal force: Report a bug.
  The requested model behavior excludes edit source.
}
```

## Trust and safety

```sudo
// Source: AGENTS.md:215-217
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  Within this instruction's source scope, the model is asked to invoke from outside the target with an explicit `--config`. *Why:* the tool refuses a `--config` inside the scan target and ignores an auto-detected `config.yaml` there, so a hostile repo cannot configure its own scan.
}
```

```sudo
// Source: AGENTS.md:218-220
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Keep shipped profiles as they are; never add `Bash` to a role's `allowed_tools`. *Why:* no shipped profile grants a shell, and a shell lets prompt injection in the target run commands on the model's machine.
}
```

```sudo
// Source: AGENTS.md:221-223
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Own the overlay. The tool refuses a `config.local.yaml` the model (or root) do not own, or one that is group- or world-writable.
  The request retains this source rule, criterion or rationale, with its original modal force: Set `VVAHARNESS_NO_LOCAL_CONFIG=1` to ignore it for a reproducible run.
}
```

```sudo
// Source: AGENTS.md:224-225
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to adopt `--resume` only to continue an interrupted run on unchanged code. *Why:* resume reuses cached stage results.
}
```

```sudo
// Source: AGENTS.md:226-229
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Treat output as sensitive as the repository. *Why:* redaction masks credential-shaped values by name and shape, not by meaning.
  The request retains this source rule, criterion or rationale, with its original modal force: Take the same care with stderr (above all `scan_progress.style: llm_debug`, which prints whole prompts) and EV artifacts.
  The requested model behavior excludes widen what is printed.
}
```

## Do / Don't

```sudo
// Source: AGENTS.md:233-239
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: | Do | Don't | |---|---| | Run `setup` / `doctor` on any error | Edit files under `vvaharness/` | | Pick a shipped `--config` profile | Hand-write a `config-*.yaml` | | Put credentials and gateway settings in env vars or `.env` | Paste keys into config or source | | Run from outside the target with explicit `--config` | `cd` into the scanned repo and run there | | Keep `--stop-after s9` unless the user asks for fixes | Arm exploit verification or fix mode unasked |
}
```

## Further reading

```sudo
// Source: AGENTS.md:243-249
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Commands and flags: [docs/USER_GUIDE.md](docs/USER_GUIDE.md).
  The request retains this source rule, criterion or rationale, with its original modal force: Profiles and capabilities: [docs/features.md](docs/features.md), [docs/SKILLS.md](docs/SKILLS.md).
  The request retains this source rule, criterion or rationale, with its original modal force: Models: [docs/models.md](docs/models.md).
  The request retains this source rule, criterion or rationale, with its original modal force: Trust model, redaction and data egress: [docs/security.md](docs/security.md).
  The request retains this source rule, criterion or rationale, with its original modal force: Design: [docs/architecture.md](docs/architecture.md).
  The request retains this source rule, criterion or rationale, with its original modal force: Overview: [README.md](README.md).
  The request retains this source rule, criterion or rationale, with its original modal force: Report a vulnerability in vvaharness: [SECURITY.md](SECURITY.md).
  The request retains this source rule, criterion or rationale, with its original modal force: Contribute: [CONTRIBUTING.md](CONTRIBUTING.md).
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../assets/original/AGENTS.md).
