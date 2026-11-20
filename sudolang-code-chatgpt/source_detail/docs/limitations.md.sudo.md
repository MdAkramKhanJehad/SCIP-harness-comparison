# docs/limitations.md

Role: repository/build/operating context, outside scan execution.

Exact source asset: `assets/original/docs/limitations.md`. SHA-256 `6a3fc14d0031f98cbb2c34d5c4931b9cd96f7e596b0037a8d3a0ec7b8660f599`.

```sudo
// Source: docs/limitations.md:1-103
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
<!--
Copyright 2026 Visa, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
# Limitations

vvaharness finds candidate security weaknesses in source code with model-driven
stages, verifies each candidate adversarially, and writes a Markdown report and
SARIF. It can also add live API evidence (exploit verification), fix findings
in the target's source (S10 remediation; `remediate --mode report-only`
proposes without edits) and review those fixes (S11 validation). The limits
below are design boundaries: know them before you rely on a result.

## Read first

> [!IMPORTANT]
> **Findings and fixes are LLM-generated triage candidates**, not confirmed
> vulnerabilities or production-ready patches. Output is non-deterministic, so
> runs can differ. An empty report does not prove the code is safe. A human must
> review every finding and every fix.

> [!WARNING]
> **Exploit verification (Beta — API only) sends live attack traffic.** It is the
> only component that sends requests to your application, and only to a target
> you are already running on a loopback address. It sends `GET`, `HEAD`,
> `OPTIONS` and `POST`; every shipped profile also allows `PUT` and `PATCH`.
> `DELETE` also needs `safe_mode: false`, which no shipped profile sets. The
> pinned address fixes where it sends, not what listens there, so point it only
> at a disposable local instance you own. Model calls, batch clones and the
> optional report upload also send network traffic; see
> [SECURITY.md](../SECURITY.md#how-the-tool-handles-your-data).

> [!WARNING]
> **S10 remediation edits your source.** The `full` and `sdk` profiles run it, and
> `--remediate` turns it on with any profile. Use `--stop-after s9` to skip it.

> [!IMPORTANT]
> **Scan only authorized, trusted repositories.** Prompts send source to the
> configured model provider and can expose sensitive files or credentials in
> that code. Every scan spends model tokens: run
> `vvaharness estimate --repo <path>` first (no spend).

## Detection and coverage

| Limit | Impact | What to do |
|---|---|---|
| vvaharness reads the target; it never builds, runs or tests it, and no shipped profile gives a model a shell. | No finding is confirmed by execution. | Treat every finding as unproven until you confirm it. |
| Accuracy varies by repository, language, vulnerability class, and model configuration. | Benchmark precision and recall do not guarantee equivalent performance on another codebase. The report's `Verifier confirmation rate` grades the pipeline's own findings; it is not a precision figure. | Validate performance using labelled applications representative of your environment. |
| No stage votes across runs, and no shipped profile re-runs a unit for agreement. | Findings can differ between runs of the same code. | Re-run important targets as fresh scans (without `--resume`) and compare reports before you conclude a weakness is absent. |
| Coverage is bounded, not complete: S4 deep-dives only the files a threat names (the S0 and S5 pattern checks still scan the rest), stage caps limit threats and findings, and failed or timed-out units are skipped. | Some code is never reviewed. | Read Scan Health and "Files named by no investigation unit" in the report; see [security.md](security.md). |
| Severity comes from a model-assigned CVSS 3.1 vector: the VulContextSeverity band when application context is supplied, else the base-score band. A finding that ships without a vector keeps the model's own severity label. | Severity is a model judgment, and a label with no vector has no score behind it. | Re-score high-impact findings before you set priority. |
| Business prioritization depends on application context supplied to the scan. | Without that context, priority labels cannot reflect the application's exposure, data sensitivity or business criticality. | Supply approved application context or perform downstream business-risk triage. |
| Analysis is not path-sensitive taint tracking: S0 builds no taint paths and tracks no sanitizers or reflection. S0 matches one fixed, built-in set of text patterns against every in-scope file, and you cannot add your own source/sink rules. Most S0 patterns name Python APIs; the rest are generic call names such as `eval(` and `.execute(`. S5 detectors run only on Python (6 rules), web templates (3 rules) and JavaScript/TypeScript (1 of those 3). The code graph extracts symbols for 17 language labels. | Code outside Python gets fewer and less precise deterministic seeds and detector findings. | Review code in other languages with extra care. |

## Exploit verification (Beta — API only)

| Limit | Impact | What to do |
|---|---|---|
| It tests only findings that map to an endpoint in the API collection you supply. | All other findings keep only the static verdict. | Add missing routes to the collection. |
| It sends only to loopback addresses; no setting overrides this. | You cannot test a remote or staging host. | Run the target locally or forward its port to `127.0.0.1`. |
| It is positive-only, and some classes (for example, authorization across two accounts) need manual review. | A finding it does not confirm is not proven safe. | Keep reviewing unconfirmed findings. |
| Its results appear in the Markdown report and `findings.json`, never in SARIF. | SARIF-based gates do not see live evidence. | Read `findings.json` when CI must act on it. |
| A batch run (`--repo-file`) does not run it: the batch ignores `EV_API_COLLECTION`, with a warning. | Batch findings keep only the static verdict. | Run exploit verification as a single-repo scan of each target. |

## Remediation and validation

| Limit | Impact | What to do |
|---|---|---|
| S10 does not build, run or test the patched code. | A fix can break the build or behaviour. | Build, test and review every diff on a clean branch. |
| S11 validation reviews code; it does not run tests. | A positive S11 verdict is a model review, not a test result. | Run your own tests on every accepted fix. |
| S10 fix mode needs edit tools, and the direct `via: openai` route has none; in-scan S10 has no report-only setting. | A `via: openai` remediate role cannot apply fixes, in-scan or standalone. Each finding ends `not fixed`, and S10 does not change the exit code. | Run standalone `remediate --mode report-only` on that route, or move `models.remediate` to `via: cli`, `via: sdk` or `via: deepagents`. |
| S10 runs report-only while the target contains a symlink that resolves outside it, dangles or loops. The check reads up to 20,000 files and 20,000 directories, and skips `.git`, `node_modules`, virtual environments and tool caches. | Fix mode edits nothing on such a target on `via: sdk`, `via: openai` and `via: deepagents`; on `via: cli`, report-only there keeps every tool in `step_remediate.allowed_tools`, so list only `Read` and `Grep` there first. S10 prints `[remediate] REFUSING fix mode` and names the links. A link past those bounds does not switch S10 to report-only. | Remove links you do not need, or remediate a clean copy. |
| The S10 content check reads only the code lines a patch adds to Python, Java, Kotlin, Scala, Groovy, JavaScript, TypeScript, C#, Go, Ruby, PHP, C, C++ and Rust files, and to shell and PowerShell scripts. | A change to another file type, such as Swift, Dart, Solidity, YAML or Markdown, is not checked for those constructs. | Review every diff, including files the check does not read. |
| `validate` and in-scan S11 judge only cases that S10 recorded in this machine's state store for the same checkout path. | Cases from another machine, path or `VVAHARNESS_STATE_DIR`, and cases whose record a fresh scan, `gc` or a later `remediate` removed, are skipped. When no case has a record, S11 exits `1`. | Run `remediate` and `validate` on the same machine and path with the same `VVAHARNESS_STATE_DIR`, and validate before the next scan without `--resume`. |
| The S11 staged copy leaves out `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md`, `GEMINI.md`, `.cursorrules` and `.mcp.json`, because they can give the panel instructions. It also leaves out every `.git`, `venv`, `.venv`, `node_modules`, `__pycache__`, `checkpoints`, `security-scan` and `security-remediation` directory, `*.pyc` files, and links that dangle or leave the repository. | The panel cannot review a fix to a file in one of those places. | Review such a fix yourself. |

## Operation and platform

| Limit | Impact | What to do |
|---|---|---|
| Configuration is not schema-validated. An unknown or misspelled key is ignored; only unknown `models.<role>` keys get a warning. | A typo silently does nothing. | Copy key names from a shipped profile. |
| Tool limits are checks inside the process, not an operating-system sandbox. | A hostile repository can try to steer the model through its content. | Scan repositories you trust. For others, use a disposable environment and apply [Hardening for less-trusted or sensitive targets](security.md#hardening-for-less-trusted-or-sensitive-targets). |
| Scans of one checkout cannot run in parallel: checkpoints and `security-scan/` outputs are keyed by the resolved repository path, and nothing locks a running scan. | Two concurrent scans of one checkout overwrite each other's checkpoints and `findings.json`. | Use a separate clone for each parallel scan. |
| Redaction is heuristic and depends on recognized names and value shapes. | Unusually named secrets or sensitive source may appear in prompts, logs, transcripts or artifacts. | Treat scan inputs and outputs as sensitive. Leave `scan_progress.style` off `llm_debug`, which prints every prompt to stderr ([security.md](security.md#prompts-are-written-to-stderr-under-llm_debug)). |
| `--resume` reuses each saved stage result as it is, with one exception: an S4 result with any unit that ended `error`, `halted`, `failed` or `uninvestigated` is not reused, so S4 to S8 run again in full. S6 batches recorded as `VERIFY_ERROR` are reused when S4 is reused. A stage also runs again when it has no saved result or an earlier stage ran again. | A resume after an S4 failure costs a full S4 run, and a unit that fails the same way each time makes every resume repeat S4. A resumed run does not retry failed S6 batches, and its runtime, cost and output can differ from the interrupted attempt. | To retry failed S6 work, run the scan without `--resume`. To stop repeated S4 runs, fix the cause that `*_errors.jsonl` names. Record every attempt as part of the run provenance. |

## Further reading

[USER_GUIDE.md](USER_GUIDE.md) · [features.md](features.md) ·
[architecture.md](architecture.md) · [models.md](models.md) ·
[integrations.md](integrations.md) · [SKILLS.md](SKILLS.md) ·
[security.md](security.md) · [SECURITY.md](../SECURITY.md)

``````

