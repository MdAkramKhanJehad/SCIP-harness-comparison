# Layer two: conflicts in mechanisms between VulnHunter and VVAH

Layer one (`01-high-level-design-conflicts.md`) compared architecture. This layer descends to the individual mechanisms that do comparable jobs in both harnesses: how severity is decided, how a finding is verified, how duplicates are merged, what the model is shown, which tools it may use, how a fix is produced and checked. A conflict at this level means the two mechanisms do the same job under rules that cannot both hold, so that the same input would be treated differently, or a setting with the same name would mean different things.

**Reading the evidence.** Citations are `path:line` relative to the harness repository (`VulnHunter/` or `visa-vulnerability-agentic-harness/`). Knob identifiers are in code formatting and come from `vulnhunter.knobs.yaml` and `vvah.knobs.yaml`. *Verified in source* means the cited lines were opened and read while writing this document. *Verified in earlier reading* means the fact was read in the source earlier in this study and recorded in research notes, with the location, but the line was not reopened for this document. *Inferred* means the conclusion follows from verified facts without being stated.

**Names.** VVAH is the Visa Vulnerability Agentic Harness. VVAH stages are named by number and meaning on first use: Stage 2 threat modelling, Stage 4 deep investigation, Stage 6 adversarial verification, Stage 7 deduplication, Stage 8 chaining and ranking, Stage 10 remediation, Stage 11 validation of fixes.

## Summary

| Number | Mechanism | The conflict in one sentence |
|---|---|---|
| 1 | Severity | A model-judged tier by attacker position versus a code-computed score from a model-chosen vector; and a harness that forbids its own top label in output versus one that uses it |
| 2 | Verification procedure | In one harness an elimination that all agents agree on stands without re-reading the source; in the other even a verifier's refutation is checked against the file |
| 3 | Deduplication | Default bias to keep findings apart versus default bias to merge neighbours |
| 4 | Context supply | The model finds its own context versus code selects and inlines it |
| 5 | Navigation tools | A default tool list without a search tool for prompts written around search, versus a default with search and a code graph |
| 6 | Write authority of the detection model | The scanning model may write files; the detection model in the other harness never can |
| 7 | Planning and reasoning control | A fixed prose procedure with no reasoning setting versus a planning object, an evidence gate and a reasoning setting per stage |
| 8 | Sibling and variant search | A mandatory separate phase with re-entry versus an instruction inside each unit's session |
| 9 | Knowledge supply | Class procedures always in the prompt versus knowledge fetched from a tool, skills and injected data |
| 10 | Structured output | Data recovered from prose by a second model call versus prose rendered from typed data |
| 11 | Fix strategy | The model designs the fix under evidence requirements versus the model chooses from a playbook under policy |
| 12 | Fix validation | One independent verifier with four gates versus three voters with consensus |
| 13 | Protection against a hostile repository | Defence by session configuration and prompt envelopes versus defence by tool and middleware layers |
| 14 | Concurrency | Concurrency decided by the model within one conversation versus by a thread pool |

---

## Mechanism conflict 1: severity is decided differently, and the top label is forbidden in one harness and defined in the other

**VulnHunter.** The model classifies severity "using the tier definitions below (not numeric CVSS)" and "the worst-case caller determines tier" (`vulnhunt/phases/phase2_shared.md:304`). The tiers are defined by the attacker's position and the achieved effect: High+, High, Medium, Low, and informational (`phase2_shared.md:306` onward). Severity then drives downstream work: only confirmed High and Medium findings receive a proof of concept and exploit test (`vulnhunt/phases/phase3_reproduce_test.md:22`).

**VVAH.** The verifier is asked to produce a Common Vulnerability Scoring System 3.1 base vector (`vvaharness/pipeline/stages/s6/prompts.py:192`), and code turns the vector into a score and a band: below 4.0 Low, below 7.0 Medium, below 9.0 High, otherwise Critical (`vvaharness/report/cvss.py:40`, `cvss.py:123`). Severity then drives remediation: the top findings by score are selected for Stage 10 (`step_remediate.top_n_findings`).

**The conflict.** First, the decision is made by the model in one harness (a tier) and by code in the other (a band from a model-chosen vector). Second, the vocabularies collide on the highest label. VulnHunter's delivery rules forbid the word "critical" in every pull request title, body, issue body and commit message, apart from five safe phrases, and require the replacement term `High+` (`vulnhunter-fix/references/severity-mask-rule.md`, section "Rule"; enforced by `vulnhunter-fix/scripts/check-severity-mask.py`). VVAH's top band is literally named "Critical". A finding that VulnHunter would label High+ and a finding that VVAH would label Critical are not the same set: High+ is defined by attacker position, Critical by a score of 9.0 or more.

**Consequence.** Severity-based selection is not comparable between the harnesses. Any experiment that conditions on "high severity" selects different findings and, in VulnHunter, also changes what extra work is done.

**Evidence strength.** Verified in source.

---

## Mechanism conflict 2: an agreed elimination stands unchecked in one harness, and a refutation is checked against the file in the other

**VulnHunter.** Phase 2b begins with a consensus rule (`vulnhunt/phases/phase2b_verify.md:31`, section "Consensus-Skip (before full verification)"; knob `prompt.phase2b.consensus_skip`, default true). When all agents for a partition cite the same gating evidence at the same file and line for a failure of the first hard gate, the candidate is recorded as "ELIMINATED — Gate 1 consensus" "without re-reading source" (`phase2b_verify.md:35` to `:37`). The rule runs only in one direction: a split decision, any candidate disposition from any agent, and every candidate from the sink-driven agent always receive full verification (`phase2b_verify.md:38` to `:41`). Candidates that are verified go through a list of checks (registry `prompt.phase2b.checks`, `phase2b_verify.md:46`) and receive a binary verdict (`phase2b_verify.md:249`).

**VVAH.** Stage 6 has no elimination by agreement: every finding that reaches it is placed in a file-sorted batch and verified in a session (`vvaharness/pipeline/stages/s6/batching.py:34`). Verdicts carry a confidence; a true positive below `step6_verify.min_confidence` is dropped, and an inconclusive verdict is kept as undetermined (`vvaharness/pipeline/stages/s6/outcomes.py:262`). A false-positive reason that claims a module is not imported is checked against the file, and the finding is held as inconclusive if the premise is wrong (research notes, `vvaharness/pipeline/stages/s6_verify.py:639`; verified in earlier reading).

**The conflict.** The two harnesses treat a negative judgement differently. VulnHunter verifies every positive in full but lets an elimination stand when the agents agree, saving effort by trusting agreement among agents that share a prompt and a model. Agreement among such agents is not independent evidence, so a wrong elimination on which they agree is never re-examined. VVAH's design pays attention to the same risk from the opposite side: it re-checks the factual premise of a refutation against the file and holds the finding as inconclusive when the premise is wrong.

**Consequence.** A true vulnerability that the trace agents consistently dismiss at the first gate is lost without a second look in VulnHunter, which affects recall and is invisible in the report except for the "consensus-skipped" marker in the verification table. In VVAH the same dismissal would face the premise check. Conversely, VulnHunter spends the saved effort on full verification of every positive.

**Evidence strength.** Verified in source for the consensus rule and the confidence floor; verified in earlier reading for the premise check.

---

## Mechanism conflict 3: deduplication defaults to keeping findings apart in one harness and to merging neighbours in the other

**VulnHunter.** An anti-merge rule forbids merging, subsuming or consolidating findings that differ in attacker authentication level, entry point, gateway context or exploited parameter, with one stated exception for the rollup of a universal authentication gap (`vulnhunt/phases/phase2b_verify.md:267`). The report has one entry per sink location. A second deduplication happens only when issues are filed: first by a marker key (a hash of location, weakness and root cause), then by a conservative model comparison that must agree on location, root cause and impact (research notes, `vulnhunter-agent/agent/issues_dedup.py`; verified in earlier reading, module docstring at lines 1 to 12).

**VVAH.** Stage 7 collapses findings in the same file with a compatible class or weakness label whose lines are within a tolerance, using title similarity, with a stricter weakness match for logic flaws (`vvaharness/pipeline/stages/s7/collapse.py:16`, module docstring "collapse same-site duplicates"). The tolerance has two values: 3 in the built-in defaults and 5 in the shipped profile (`step7_dedup.line_tolerance`, `vvaharness/config/__init__.py:553`). A model-based merge exists but is off in every shipped profile (`step7_dedup.semantic`, default false).

**The conflict.** VulnHunter's instruction is to resist merging; VVAH's code merges by default whenever two findings are near each other and compatible. The same pair of findings (two parameters of one function, one reachable without authentication and one with) is kept as two entries by VulnHunter's rule and is a candidate for collapse by VVAH's code. The place in the pipeline also differs: VulnHunter deduplicates during verification and again after the report, in the issue tracker; VVAH deduplicates once, before ranking.

**Consequence.** Finding counts per repository are not comparable, and a precision measure that counts duplicates as false positives would penalise VulnHunter's design.

**Evidence strength.** Verified in source for the rules and the tolerance defaults; the example pair is an illustration, not an observed case.

---

## Mechanism conflict 4: who decides what the model is shown

**VulnHunter.** The model decides: it lists files with a glob tool and reads what it needs, and writes its own inventory and partition files as it goes (`vulnhunt/phases/phase1_recon.md:51`). The launcher passes only run metadata.

**VVAH.** Code decides. Stage 2 receives an evidence snapshot assembled by code with a cap on every kind of item (documents, manifests, configuration samples, interface artefacts, modules, entry points, file inventory), each counted and warned about when cut (`vvaharness/evidence/gather.py`). Stage 4 can receive whole-file source inlined for each unit (`vvaharness/pipeline/stages/s4/session.py:179`, function `_load_code`: "Whole-file source when `step4.inline_source` is on; `None` otherwise and always for LARGE"), and Stage 6 packs findings sorted by file so that co-located findings share a read (`vvaharness/pipeline/stages/s6/batching.py:34`).

**The conflict.** In one design the context is an outcome of the model's own navigation; in the other it is an input chosen by code, with caps that can silently remove evidence from view. The same cap in VVAH that protects cost (for example `step2.max_modules`) is, in VulnHunter's design, a decision the model makes without any declared limit.

**Consequence.** Differences in findings may come from what was shown rather than from how it was analysed. A cap in VVAH is a measurable intervention on exposure; no equivalent exists in VulnHunter.

**Evidence strength.** Verified in source.

---

## Mechanism conflict 5: the default tools of the scanning model

**VulnHunter.** The default and the shipped example allow only `Agent`, `Glob`, `Read` and `Write` (`vulnhunter-agent/agent/config.py:572`; `vulnhunter-agent/agent/config.example.toml:100`). The default has no content-search tool and no shell. The skill prompts nevertheless are written around search: "Use the tools available to you — **Grep**, **Glob**, and **Read**" (`vulnhunt/SKILL.md:111`), forward tracing "using Grep" (`vulnhunt/SKILL.md:129`), and the sweep says "Use the **Grep tool** to search the entire codebase" (`vulnhunt/phases/phase3d_sweep.md:39`). The configuration comment acknowledges the gap: "See config.example.toml for what to add when phases need forward tracing (Grep)" (`vulnhunter-agent/agent/config.py:561`), and the launcher adjusts the prompt so that it does not claim tools that are absent (`vulnhunter-agent/agent/runner.py:186`).

**VVAH.** Detection sessions use search by default: Stage 2 and Stage 6 allow `Read` and `Grep` (`step2.allowed_tools`, `step6_verify.allowed_tools`), Stage 4 allows `Read`, `Glob` and `Grep` (`step4.allowed_tools`, `vvaharness/config/__init__.py:315`), and the shell is off in `step2.bash` and `step4.bash`, plus six code-graph tools and a weakness-guidance tool (`vvaharness/rules/kb_tools.py:46`). Tool permits are enforced in code and fail closed.

**The conflict.** One harness's prompts require a search capability that its default configuration does not grant; the other grants search by default and adds structured navigation. The practical consequence is that with default settings VulnHunter's trace and sweep must fall back to reading files and listing paths, which changes both cost and coverage.

**Consequence.** A VulnHunter scan with default tools is not the scan its prompts describe. This is also a contradiction inside VulnHunter and is cross-referenced in `03-low-level-contradictions-within-vulnhunter.md`.

**Evidence strength.** Verified in source.

---

## Mechanism conflict 6: whether the detection model may write

**VulnHunter.** The scanning session is given `Write` and runs with permission mode `acceptEdits` (`vulnhunter-agent/agent/config.py:576`), because the model writes the report, the proof-of-concept files and the exploit tests into a results directory that the launcher creates in advance (`vulnhunter-agent/agent/runner.py:398`).

**VVAH.** Detection tools are read-only, and code writes every artefact. Write access exists only in remediation: on the deepagents route a single fixer sub-agent holds the only write tool (`docs/architecture.md`, "Sub-agents" paragraph: "Sub-agents exist only in S10 (one `fixer`, deepagents only: it holds the only write tool)"), and on the software development kit route the Claude Agent software development kit performs the edits with confined edit tools (research notes, `vvaharness/backends/llm/agent_sdk.py`; verified in earlier reading).

**The conflict.** The two harnesses draw the line between reasoning and recording in different places. In VulnHunter the model both reasons and records, so the quality of the record depends on the model; in VVAH the model returns typed objects and code records them.

**Consequence.** A VulnHunter result can contain a record that the model wrote incorrectly (a wrong count, a misnamed file) without any structural check; a VVAH result cannot, but VVAH loses whatever the typed schema cannot express.

**Evidence strength.** Verified in source.

---

## Mechanism conflict 7: planning and reasoning control

**VulnHunter.** The investigation procedure is a fixed numbered list in the prompt (`vulnhunt/SKILL.md:119`, "Investigation Discipline"), the same for every input. No reasoning setting is passed to the model (no `effort` knob exists in the launcher; registry entries `sdk.max_turns` and `sdk.max_budget_usd` are likewise unset).

**VVAH.** Planning is an object at run time: with `step2.planning` or `step4.planning` the model first writes a todo list, and an evidence gate can refuse a verdict until all todos are complete and a graph tool has been used (`step4.evidence_gate`). Planning is on in the built-in defaults and off in the shipped profile (`vvaharness/config/__init__.py:339`: `step4.planning` is true built in and false in the profile). Each stage has an `effort` setting (high everywhere in the shipped profile) and a switch `think_in_prompt` (default true) that replaces native thinking by written reasoning appended to the system prompt (`vvaharness/backends/harness/deepagents/options/model_building.py`).

**The conflict.** One harness prescribes the order of thought and leaves depth to the model; the other leaves the order to the model and controls depth and verification. A gate that depends on planning cannot be tested in VulnHunter, and a fixed order cannot be varied in VVAH without editing prompts.

**Consequence.** The levers that exist for reasoning are different in kind, and effects found for one do not carry over.

**Evidence strength.** Verified in source for the defaults; the statement about the absence of an effort setting in VulnHunter is verified for the launcher and inferred for the skills.

---

## Mechanism conflict 8: sibling and variant search

**VulnHunter.** Phase 3d is a separate mandatory phase ("Sweep Verification (MANDATORY — DO NOT SKIP)", `vulnhunt/phases/phase3d_sweep.md:6`) that runs after all findings are confirmed, searches the whole codebase regardless of partitions, and sends new hits back through the pipeline.

**VVAH.** Sibling search is an instruction inside each investigation unit's own session: a breadth clause in the Stage 4 prompt (`vvaharness/pipeline/stages/s4/prompts.py:31`, `_BREADTH_CLAUSE`) and a skill called `sibling-instances` that begins "After confirming a weakness, sweep the repository for every other site of the same pattern" (`vvaharness/skills/sibling-instances/SKILL.md:3`). Probe scripts shipped with some skills run in one call to support breadth (`vvaharness/pipeline/stages/s4/prompts.py:214`).

**The conflict.** The sweep is a global step after confirmation in one harness and a local step during investigation in the other. A sibling found by VulnHunter's sweep enters verification afterwards; a sibling found in VVAH is a finding in its unit's output and is verified by Stage 6 with everything else. A sibling in files that no threat names is never reached in VVAH but is reached by VulnHunter's whole-repository sweep.

**Consequence.** Recall on repeated patterns differs systematically, and in VVAH it depends on the threat model's file selection.

**Evidence strength.** Verified in source.

---

## Mechanism conflict 9: where knowledge comes from

**VulnHunter.** Class-specific procedures are written into the phase files for three class groups (injection, navigation and authorisation, logging; `vulnhunt/phases/phase2_hunt.md:46`), and nothing is fetched at run time.

**VVAH.** Knowledge is supplied through a tool and through selectable material: a weakness-guidance tool (`vvaharness/rules/kb_tools.py:46`, function `CweGuidance`), seventeen skills of which eight ship probe scripts, injected known vulnerabilities and design controls (`inject.*` settings), and a baseline checklist chosen by the kind of repository (`vvaharness/rules/repo_kinds.py`).

**The conflict.** One design makes all knowledge part of the prompt, so it is always in context and always costs tokens; the other makes it retrievable, so it can be absent when needed and is only used if the model calls it. VVAH's evidence gate partly forces use of graph tools but not of the guidance tool.

**Consequence.** Adding knowledge is a prompt edit in VulnHunter and a data change in VVAH, with different cost profiles and different risks (prompt bloat versus non-retrieval).

**Evidence strength.** Verified in source.

---

## Mechanism conflict 10: structured output is recovered from prose in one harness and rendered from data in the other

**VulnHunter.** The scan produces a Markdown report written by the model. When issues are filed, a second model call converts the report into structured findings, restricted to confirmed findings, with file paths taken from the file system rather than from the model (research notes, `vulnhunter-agent/agent/issues_extract.py`; verified in earlier reading).

**VVAH.** Findings are typed objects from the first stage on; the report, the JSON file and the SARIF file are rendered by code from one final report object (`vvaharness/pipeline/stages/s9_sarif.py`, `s9/typed_sarif.py`), and a failed narrative stage falls back to a severity-sorted report.

**The conflict.** In VulnHunter the machine-readable result is a reading of a human-readable text by a model, which adds a second opportunity for loss or invention (guarded by an instruction to "never invent values"); in VVAH the human-readable text is a rendering of the structure.

**Consequence.** Information that the report states loosely does not reach the issue tracker. In VVAH, information that the typed schema cannot hold does not reach the report.

**Evidence strength.** Verified in earlier reading.

---

## Mechanism conflict 11: how a fix is produced

**VulnHunter.** The fixer designs the fix itself, under evidence requirements: a failing test must exist before any source edit, evidence that the test fails before and passes after the fix, a fresh-context reviewer of the test, a completeness tier (full, mitigation or workaround) that is never full by default, residual risks that must be listed whenever the tier is not full, and a nine-column verification table in which every "yes" cites a file and line (research notes, `vulnhunter-fix/references/remediation-rigor.md` and `scripts/validate-verification.py`; verified in earlier reading). Seven mechanical delivery gates then check the result.

**VVAH.** The remediation agent selects a strategy from a playbook and does not invent one (`inputs/remediation_playbook.yaml`); a policy gate runs before any model call, and a gate after the model reverts edits to forbidden paths and scans added lines for backdoor literals, always-true checks and disabled certificate verification (`vvaharness/remediation_agent/policy/patch_content.py`, verified in earlier reading). A fix that cannot be applied safely is reported instead of applied.

**The conflict.** VulnHunter widens what the model may do and demands proof afterwards (a test that discriminates); VVAH narrows what the model may do and checks the content afterwards. VVAH does not require a test of the fix at all, and VulnHunter does not restrict the strategy to a list.

**Consequence.** The two fixers have different failure modes: VulnHunter can produce a creative but wrong fix that passes its own test; VVAH can fail to fix anything the playbook does not contain.

**Evidence strength.** Verified in earlier reading.

---

## Mechanism conflict 12: how a fix is validated

**VulnHunter.** One independent read-only session judges each finding with four gates (the sink is mitigated, the sink is reachable, the whole class is eliminated, the sweep is complete), each with a status of pass, fail, skipped or not applicable; pass and fail are authoritative and skipped means the gate ran but could not reach a verdict (`vulnhunter-agent/verify_disposition.schema.json:79` to `:122`). All gates skipped gives an inconclusive verdict, and any verdict other than fixed reopens the issue (research notes, `verify_post.py`; verified in earlier reading).

**VVAH.** A panel of three isolated personas each reports gate statuses, and code applies "conservative consensus: 2+ votes win at HIGH, else most conservative wins FLAGGED" (`vvaharness/validation/synthesis/_consensus.py:134`, with `MIN_CONSENSUS_VOTES`); code also computes a weighted score from the gates, with a critical-gate rule.

**The conflict.** A single judge cannot disagree with itself, so VulnHunter has no mechanism for detecting model variance in validation; VVAH detects it by voting but resolves disagreement towards caution. VulnHunter's gates are structural (about the code), VVAH's are scored (a number from weighted gates).

**Consequence.** Validation outcomes are not comparable, and a harness that measures agreement between runs can do so only for VVAH.

**Evidence strength.** Verified in source for the consensus rule and the gate statuses; verified in earlier reading for the weighted score, the critical-gate rule and the reopening rule.

---

## Mechanism conflict 13: protection against a hostile repository

**VulnHunter.** Protection is placed in how the session is configured and in how untrusted text is wrapped: only user-level settings are loaded, an MCP configuration from the repository is rejected, network access is limited to the inference host in the sandbox, reads are limited to the working directory, and untrusted text passed to a model is wrapped in nonce-delimited envelopes with begin and end markers (research notes, section E; verified in earlier reading).

**VVAH.** Protection is placed in the tool and middleware layer: file tools are jailed to the working directory and the Stage 1 inventory, tool permits fail closed, tool results are redacted before the model sees them (secrets, payment card numbers that pass the Luhn check, tokens, private keys, credentials in addresses; `vvaharness/report/redact.py`), a `.env` file in the target is ignored, and the validation stage works on a staged copy that omits files addressed to coding agents (verified in earlier reading).

**The conflict.** The first design assumes the model will see raw content and tries to contain what it can do; the second filters what it sees. They disagree about whether secrets in the scanned repository should reach the model, and about whether the model's own reading of repository instructions is a hazard to be removed (VVAH deletes the files) or to be fenced (VulnHunter wraps text in markers).

**Consequence.** A prompt injection in a scanned file has different reach in the two harnesses, and neither harness's defence tests the other's threat.

**Evidence strength.** Verified in earlier reading.

---

## Mechanism conflict 14: who sets concurrency

**VulnHunter.** The orchestrator prompt tells the model to dispatch agents in waves "of at most 6" in a single message and not to dispatch all agents in one message (`vulnhunt/phases/phase2_hunt.md:54` and `:56`). Whether six run at once depends on the model and the platform.

**VVAH.** Concurrency is a thread pool sized by settings: `step4.parallel` is 12 in both the built-in defaults and the shipped profile; `step6_verify.parallel` is 5 built in and 7 in the shipped profile (`vvaharness/config/__init__.py:299`, `:400`).

**The conflict.** An instruction in prose and a number read by code both set "how many at once", but only the second is enforced. A VulnHunter wave size changed from 6 to 12 in the prompt would be followed only as far as the model follows it.

**Consequence.** Cost and latency comparisons that treat the two numbers as the same lever overstate the control available in VulnHunter.

**Evidence strength.** Verified in source.

---

## Cross-cutting observation: defaults that disagree inside VVAH's own layers

Several VVAH values differ between the built-in defaults and the shipped profile (`step6_verify.min_confidence` 7 versus 5, `step4.batch_size` 1 versus 4, `step4.inline_source` false versus true, `step4.planning` true versus false, `step1.auto_exclude` false versus true). Any comparison with VulnHunter must state which layer was used, because the harness's behaviour in a profile is not its behaviour in its built-in defaults. These layer disagreements are examined as contradictions inside VVAH in `04-low-level-contradictions-within-vvah.md`.

## What carries forward to the third layer

The mechanisms above show where the two harnesses differ by design. The third layer asks a different question: where does a single harness disagree with itself. Mechanism conflict 5 (the missing search tool) and the layered defaults in the paragraph above are the two places where this layer and the next meet.
