# VulnHunter vs VVAH: configuration and knobs

Compared: `VulnHunter` at commit `6d25b5c` (Capital One) and `visa-vulnerability-agentic-harness` at `0e6f00d` (Visa, vvaharness 1.5.1), both under `harness-comparison/`.

## Files in this folder

| File | What it is |
|---|---|
| `vulnhunter.knobs.yaml` | 2,723 knobs for VulnHunter, with stage-flow pseudocode at the top |
| `vvah.knobs.yaml` | 1,990 knobs for VVAH, with stage-flow pseudocode at the top |
| `knob_categories.yaml` | Only the hierarchy: the 14 parent categories and their sub-groups, with knob counts per harness |
| `comparison.md` | This document |
| `tools/prompt_knobs/*.json` | Rows from the exhaustive prompt pass, one file per group of prompts; `REJECTED.tsv` lists rows that failed the quote check |
| `tools/dump_vvah_knobs.py` | Reads VVAH's built-in defaults and five profiles straight from source |
| `tools/build_registry.py` | Holds the classification and the hand-collected knobs; writes both YAML files |
| `tools/check_sources.py` | Checks that every knob's cited file and line exist |

Both YAML files use the same 14 parent categories, the same sub-groups where they apply, and the same fields per knob. Each knob has an `origin` field saying whether it is real configuration or was collected from a prompt or from code.

## Where the knobs located

| Origin | VulnHunter | VVAH |
|---|---|---|
| Real configuration (config file, built-in default table, CLI flag, env var) | 45 | 290 |
| Prompt text (a number or rule written in a prompt) | 2,647 | 1,683 |
| Code constant (hard-coded in source) | 26 | 17 |
| Not set at all (the harness leaves the SDK default) | 5 | 0 |
| **Total** | **2,723** | **1,990** |

Both harnesses carry far more rules in prompt text than in configuration. The difference is what the configuration covers. VulnHunter's 45 real settings are mostly plumbing, and nothing that decides what gets found is configurable. VVAH's 290 settings include the model, limits, tool budgets and thresholds for every stage, and its prompt text is assembled by code that those settings switch on and off.

How the counts were made:

- **Config knobs.** VVAH's 271 config keys were read from source by script and are complete. VulnHunter's are complete except four plumbing sections folded into one row each (`oauth.*`, `github.*`, `publish.*`, `verify.*`).
- **Prompt knobs.** Every prompt file was read line by line and each independently variable rule recorded with an exact quote. 4,212 rows passed a script check that the quote is on the cited line; 2 failed and were dropped. The one gap is VVAH's exploit-verification prompts (classifier, endpoint mapper, attacker, judge), which were not extracted.
- **Granularity is a judgement.** A paragraph of rules can be split into three rows or eight, so the prompt totals show scale, not an exact measure. Different readers split at slightly different grain.
- **Code constants** are still a selection.

Prompt knobs by part of each harness:

| Part | VulnHunter | VVAH |
|---|---|---|
| Detection (scan) | 1,106 | 1,265 (500 of them in the 17 skill playbooks) |
| Fix stage | 1,146 | 104 |
| Fix validation | 306 | 314 |
| Issue filing and benchmark | 89 | none |

For detection alone the two are close in size. VulnHunter's larger total comes from its fixer skill, which is specified almost entirely in prompts.

## Knobs by category and origin

Each cell is `config / prompt / code`. VulnHunter also has 5 "not set" knobs: 2 under model routing, 3 under budget. VulnHunter's knobs fall into 153 sub-groups and VVAH's into 118; `knob_categories.yaml` lists them.

| Category | VulnHunter | VVAH |
|---|---|---|
| model_routing | 6 / 43 / 2 | 59 / 26 / 1 |
| budget_and_termination | 4 / 98 / 10 | 56 / 71 / 6 |
| decomposition_and_parallelism | 0 / 88 / 1 | 11 / 17 / 3 |
| scope_and_coverage | 0 / 161 / 2 | 22 / 82 / 1 |
| context_supply | 0 / 119 / 2 | 32 / 116 / 0 |
| tool_access | 7 / 71 / 2 | 23 / 122 / 0 |
| detection_method | 0 / 127 / 0 | 5 / 359 / 1 |
| gating_and_thresholds | 0 / 407 / 0 | 9 / 472 / 2 |
| verification_depth | 0 / 361 / 0 | 11 / 42 / 3 |
| dedup_and_merge | 4 / 80 / 2 | 7 / 70 / 0 |
| ranking_and_reporting | 5 / 361 / 0 | 9 / 172 / 0 |
| remediation | 6 / 570 / 1 | 13 / 105 / 0 |
| runtime_and_infra | 13 / 119 / 2 | 33 / 29 / 0 |
| evaluation | 0 / 42 / 2 | none |

In both harnesses the largest block of prompt rules is gating: what a candidate must pass to be reported.

In VulnHunter, six categories have no real config at all: decomposition, scope, context supply, detection method, gating, and verification depth. Those are the categories that decide what gets found. Changing any of them means editing a prompt file.

## Similarities

- **Same overall shape.** Both run: map the code, generate candidates, have a separate adversarial pass try to reject them, then report. Both add an optional fix stage and a separate fix-validation stage.
- **A coverage map built first.** VulnHunter's recon builds an input inventory and partitions; VVAH's S2 builds a threat model. In both, later stages only look where this first stage points.
- **An adversarial second pass with a stated bias.** VulnHunter tells the verifier that about half of candidates are false positives. VVAH tells it to assume each finding is wrong.
- **Evidence must cite code.** Both require file and line for claims, and both refuse to accept comments or naming as proof.
- **Rejecting a finding needs a reason.** VulnHunter's FALSE POSITIVE needs a file:line. VVAH's FALSE_POSITIVE must name the control or fact that refutes it.
- **Sibling search.** VulnHunter's Phase 3d sweep and VVAH's S4 breadth clause plus `sibling-instances` skill both look for the same root cause elsewhere.
- **Read-only by default.** Neither gives the detection model a shell unless the operator opts in (`--enable-bash`; `step2.bash` / `step4.bash`).
- **Hardening against a hostile repo.** Both ignore the scanned repo's own agent settings and jail file reads.
- **Parallel fan-out with a cap.** Waves of 6 agents in VulnHunter; `step4.parallel` 12 and `step6_verify.parallel` 7 in VVAH.
- **Fix strategies are constrained.** VulnHunter only describes fixes during the scan; VVAH's fixer must pick a playbook strategy.

## Differences

| Aspect | VulnHunter | VVAH |
|---|---|---|
| Where control flow lives | In the orchestrator prompt | In Python (`orchestrator/scan.py`) |
| Search strategy | Trace every input forward to a sink, plus one backward sink audit | Hypothesise threats (STRIDE), then confirm or refute each one |
| Unit of work | Partition x class group (INJ, NAV, LOG) | One investigation unit per threat, batched by file overlap |
| What bounds coverage | The input inventory; every row needs a disposition | `step2.max_threats`; files no threat names are never read |
| Models | One model for everything; Opus required | A model, backend and provider per role |
| Reasoning tier | Not set | `effort` per stage; `think_in_prompt` |
| Turn and cost limits | None. Only a 20-minute stall timeout and a 60-idle-continue abort | `max_turns`, `max_model_calls`, `max_tokens`, deadlines and `max_budget_usd` per stage |
| Precision filter | Five pass/fail hard gates in order | A 0-10 confidence floor (`step6_verify.min_confidence`) plus evidence gates |
| Verdicts | CONFIRMED or FALSE POSITIVE | TRUE_POSITIVE, FALSE_POSITIVE or INCONCLUSIVE (kept as undetermined) |
| Severity | Five named tiers defined by attacker position | CVSS 3.1 vector scored by the verifier |
| Proof of exploit | A PoC and exploit test for every High and Medium finding; run only with Bash | Optional live HTTP verification against a running target (beta) |
| Code navigation | Glob, Read, and Grep where available | Read, Grep, plus six code-graph tools and a CWE knowledge-base tool |
| Rule enforcement | Prose: MANDATORY, STOP, row-count checks | Code: typed outputs, validators, tool budgets, forced final call |
| Dedup | Anti-merge rule; one finding per sink location | Line tolerance; optional semantic pass (off in every profile) |
| Deterministic detectors | None | Pattern detectors in S5 (9 of 11 rules enabled) |
| Presets | One config | Five profiles: default, full, sdk, semgrep, taint |
| Outputs | Markdown report, PoC files, exploit tests, GitHub issues | Markdown, SARIF, `findings.json` |
| Evaluation | Benchmark with an LLM judge, recall only | None in the repo |

## Knob counterparts

These pairs do the same job in each harness. They are the natural rows for a like-for-like comparison or a shared action space.

| Job | VulnHunter knob | VVAH knob |
|---|---|---|
| Detection model | `anthropic.model` | `models.deepdive.id` (and one per other role) |
| Coverage ceiling | `prompt.scope.input_inventory` | `step2.max_threats` |
| How work is split | `prompt.hunt.class_groups`, `prompt.recon.partition_rule` | `code.s3.unit_rule`, `step4.batch_size` |
| Unit size limit | `prompt.recon.oversize_inputs` (20), `prompt.recon.oversize_files` (15) | `code.s3.small_unit_loc_max` (2000), `code.s3.medium_unit_loc_max` (8000) |
| Concurrency | `prompt.hunt.wave_size` (6) | `step4.parallel` (12), `step6_verify.parallel` (7) |
| Exclusions | `prompt.scope.exclusions` | `step1.exclude_dirs`, `step1.exclude_exts`, `step1.exclude_globs`, `step1.auto_exclude` |
| Drop non-production code | `prompt.scope.dev_only_skip` | `code.s5.test_path_gate` |
| Tool list | `scan.allowed_tools` | `step2.allowed_tools`, `step4.allowed_tools`, `step6_verify.allowed_tools` |
| Shell access | `cli.enable_bash` | `step2.bash`, `step4.bash` |
| Session length | not set (`sdk.max_turns`) | `step4.max_turns`, `step4.max_model_calls`, `step4.deadline` |
| Cost cap | not set (`sdk.max_budget_usd`) | `step6_verify.max_budget_usd` |
| Planning before work | `prompt.investigation_discipline` (fixed order) | `step2.planning`, `step4.planning` |
| Precision gate | `prompt.hard_gates` | `step6_verify.min_confidence`, `prompt.s6.exclusion_rules` |
| Proof-of-work gate | `prompt.phase2b.candidate_manifest`, count checks | `step4.evidence_gate`, `step2.require_graph` |
| Adversarial pass on/off | `prompt.phase2b.enabled` | S6 always runs; `step6_verify.reframe_enabled` tunes it |
| Verifier prior | `prompt.phase2b.fp_prior` | `prompt.s6.stance` |
| Skip re-verification | `prompt.phase2b.consensus_skip` | none |
| Exploit proof | `prompt.exploit_test.enabled`, `prompt.exploit_test.execution` | `step6_exploit_verification.enabled` |
| Sibling search | `prompt.sweep.enabled` | `prompt.s4.breadth_and_siblings` |
| Dedup tolerance | `prompt.aggregate.same_sink_dedup` (same file:line) | `step7_dedup.line_tolerance` (5 lines) |
| Semantic dedup | `issues.semantic_dedup` (issues only) | `step7_dedup.semantic` |
| Do-not-merge rule | `prompt.anti_merge_rule` | `prompt.s7.collapse_test` |
| Severity scheme | `prompt.severity_tiers` | `prompt.s6.cvss_duty` |
| Fix stage | `/vulnhunter-fix` skill (separate) | `step_remediate.enabled` |
| Fix validation | `/vulnhunt-fix-verify` (4 gates) | `step_validate.enabled` (3 personas, 4 gates) |
| Stall guard | `code.max_stalled_continuations` (60) | `code.repeat_call_limit` (20) |

## Knobs with no counterpart

**Only in VulnHunter**
- Class-group split of every partition (`prompt.hunt.class_groups`).
- A dedicated backward sink audit (`prompt.sink_audits`).
- Mandatory per-input checks: request-body gate, resource-ID gate, absent-input analysis.
- Named gate exemptions (`prompt.gate_exemptions`).
- Orchestrator context rules and the 20-word return limit.
- The continuation loop that re-prompts a stopped orchestrator.
- A benchmark with a judge (`evaluation` category).
- GitHub issue filing and dedup.

**Only in VVAH**
- Per-role model, backend and provider.
- Reasoning tier per stage.
- Tool-call budgets (`graph_tool_budget`, `cwe_tool_budget`).
- Code-graph tools and the CWE knowledge base.
- Prompt-size caps for the threat model (20 `step2.max_*` keys).
- Deadline handling: resume, then tool-free replay.
- Batching with split-retry.
- Deterministic detectors.
- Attack chains (S8).
- Live-traffic safety knobs for exploit verification.
- Profiles.
- Prompt-cache controls.

## Things to know before intervening on knobs

These matter for causal analysis, because a knob's name does not always describe its effect.

1. **`max_turns` in VVAH is not a cap on the default route.** On `deepagents` it becomes a recursion limit of `max_turns + 900`. The real bounds there are `max_model_calls`, `max_tokens` and the deadlines.
2. **VVAH has two default layers.** The built-in table and `default.yaml` disagree on many keys (for example `step6_verify.min_confidence` 7 vs 5, `step4.batch_size` 1 vs 4). The registry records both under `default`.
3. **Some VVAH knobs are coupled.** `step4.evidence_gate` only enforces when `step4.planning` is on and the route is `deepagents`. It is true but inactive in the `default` and `semgrep` profiles. The `requires` field records these conditions.
4. **Some VVAH knobs are route-dependent.** `max_budget_usd` is enforced on the `cli` route and ignored on `sdk`. `think_in_prompt` only applies on `deepagents`.
5. **VVAH ignores unknown config keys.** A misspelled knob changes nothing and raises no error.
6. **Most VulnHunter knobs need templating before they can be varied.** They are sentences. To intervene, replace the value with a placeholder and render the prompt per run.
7. **A VulnHunter prompt knob is a request, not a guarantee.** The model may not honour "waves of at most 6". The effect has to be measured from run logs, not assumed from the setting.
8. **VulnHunter's agent default has no Grep.** `scan.allowed_tools` is `Agent, Glob, Read, Write`, while the skill tells the model to grep throughout. The benchmark harness does include Grep, so agent runs and benchmark runs are not the same treatment.
9. **Exploit tests are not executed by default in VulnHunter.** Without Bash they are reasoned through, so "exploit test PASS" means two different things depending on `cli.enable_bash`.
10. **There is no false-positive measurement in either repo.** VulnHunter's benchmark scores recall only, and VVAH ships no benchmark. A reward that penalises false positives needs a new labelling step.
11. **S2 is a mediator in VVAH.** Any knob that changes the threat model changes everything after it, so effects of S4 and S6 knobs should be estimated conditional on the S2 output.
12. **Runs are not deterministic.** Each setting needs repeated runs.

## Limits of this registry

- The exhaustive prompt pass was done by eight separate readers working from one written brief. Their quotes were checked by script; their classification and descriptions were spot-checked, not reviewed row by row.
- The readers created many new sub-groups, so some sub-groups overlap in meaning (for example `fp_checks` and `hard_gates`). The parent categories are consistent; the sub-group level would benefit from a consolidation pass.
- The earlier hand-picked rows (ids starting `prompt.`) are kept, so some rules appear twice: once as a summary row and once or more as finer `p.` rows.
- VVAH's exploit-verification prompts are not covered by the exhaustive pass.
- Code-constant knobs were selected by reading; a different reader could draw the line elsewhere.
- `domain` is only authoritative where `domain_basis` is `code`. `observed` lists the values the shipped configs use, and `suggested` is my proposed range.
- Five VVAH descriptions are inferred from the key name and say so (`step1.config_dedup.*`, `step4.line_bucket`).
- `step1.allowed_tools` is set in the VVAH profiles, but I found no reader for it; it is marked as likely inert.
- `affects` is my expectation of which outcomes a knob moves. It is a starting hypothesis for the causal graph, not a measured effect.
- This describes the `harness-comparison/VulnHunter` checkout, not the edited copy in `update-cap-one-harness`.
