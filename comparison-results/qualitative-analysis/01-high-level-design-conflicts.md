# Conflicts in high-level design decisions between VulnHunter and VVAH

This document compares the two harnesses at the level of architecture: who is in control, how the search for vulnerabilities is organised, what counts as proof, and how resources are governed. A conflict here means the two harnesses make opposite or incompatible choices about the same design question, so that one cannot simply be switched into the other by changing a setting.

**Reading the evidence.** Every claim cites the real source as `path:line`, relative to the harness repository (`VulnHunter/` or `visa-vulnerability-agentic-harness/`). Knob identifiers come from the registries `vulnhunter.knobs.yaml` and `vvah.knobs.yaml` and are written in code formatting. Each conflict ends with an evidence strength: *verified in source* means the cited lines were read and say what is claimed; *inferred* means the conclusion follows from several verified facts but is not stated in the source.

**Names.** VVAH is the Visa Vulnerability Agentic Harness (package `vvaharness`). Stage numbers refer to VVAH's pipeline: Stage 0 seeding, Stage 1 context building, Stage 2 threat modelling, Stage 3 decomposition into investigation units, Stage 4 deep investigation, Stage 5 enrichment and prefiltering, Stage 6 adversarial verification, Stage 7 deduplication, Stage 8 chaining and ranking, Stage 9 report writing, Stage 10 remediation, Stage 11 validation of fixes. VulnHunter's phases are named as in its prompt files: Phase 1 reconnaissance, Phase 2 hunt, Phase 2b adversarial verification, Phase 3 proof of concept and exploit test, Phase 3c fix strategy, Phase 3d sweep, Phase 4 report.

## Summary of the design conflicts

| Number | Design question | VulnHunter | VVAH |
|---|---|---|---|
| 1 | Who controls the scan | The model, following prompt files | Python code, calling the model stage by stage |
| 2 | How the search is organised | Bottom-up: enumerate every input, trace each one forward | Top-down: hypothesise threats first, then confirm or refute each |
| 3 | What defines complete coverage | Every row of the input inventory receives a disposition | Only files named by some threat are ever investigated |
| 4 | How the unit of work is formed | Partition of the application times vulnerability class group | One investigation unit per threat, batched by shared files |
| 5 | How false positives are removed | Hard gates in a fixed order, then a binary adversarial pass | A numeric confidence floor, three-way verdicts, deterministic validators |
| 6 | What counts as proof of exploitability | A proof of concept and exploit test for every confirmed High or Medium finding | Optional live verification against a running target, which can only add confirmation |
| 7 | How much the model is trusted to follow rules | Rules are prose; compliance is requested, then checked by counting | Rules are typed outputs and code gates; the model's prose is not trusted |
| 8 | How resources are governed | No turn limit, no cost limit, no token limit | Limits on turns, model calls, tokens, wall clock time and cost for every stage |
| 9 | Whether a scan can be resumed | A scan refuses to start if earlier results exist | Checkpoints, resume, and replay after a deadline |
| 10 | Which models are used | One Claude model for everything, Opus required | A model, route and provider chosen per role |
| 11 | Where the lifecycle ends | Scan, then issues, verification, fix and fix verification as separate skills linked by GitHub issues | One pipeline with optional fix and validation stages, ending in files for downstream tools |
| 12 | Where humans take part | Fixing is interactive with an approval gate at every phase boundary | The whole pipeline is unattended |
| 13 | Whether the harness measures itself | A benchmark with a judge, recall only, and a miss analysis that proposes prompt edits | Nothing in the repository |

---

## Design conflict 1: the scan is controlled by a prompt in one harness and by a program in the other

**VulnHunter's choice.** The control flow of a scan is written as prose in the orchestrator prompt `vulnhunt/SKILL.md` and the phase files under `vulnhunt/phases/`. The Python launcher only clones the repository, opens one model session, sends the command `/vulnhunt <clone>` with some precomputed facts, and re-prompts the model while background helpers are still running (`vulnhunter-agent/agent/runner.py:680` for the session, `runner.py:459` for the stall limit). The options passed to the session contain no system prompt and no limit on turns or cost (`vulnhunter-agent/agent/runner.py:680` to `:708`). The phases are carried out by the model starting its own helper agents.

**VVAH's choice.** The control flow is a linear program: `vvaharness/orchestrator/scan.py` (function `scan_repo`) calls Stage 0 to Stage 11 in a fixed order, and every model call sits between deterministic preparation and deterministic checking. The architecture document states the shape: "Every model stage has the same shape" with deterministic preparation, one agentic session per unit, and typed output followed by deterministic gates (`docs/architecture.md`, section "How a stage runs").

**Why the two conflict.** The same rule has a different status in each harness. A statement that the adversarial pass is mandatory is a request to the model in VulnHunter (`vulnhunt/phases/phase2b_verify.md:12`, "MANDATORY — DO NOT SKIP") and a line of code in VVAH. In VulnHunter the model can skip, reorder or merge steps and the harness will not notice unless a later counting check fails. In VVAH the model cannot skip a stage because the program decides what runs. The two designs therefore disagree about where enforcement lives, and a rule cannot be moved from one to the other without being rewritten from prose into code or from code into prose.

**Consequence for results.** VulnHunter's behaviour varies with the model's compliance and with how much conversation has accumulated; VVAH's stage structure does not vary, and only the content of each stage does. This is the largest single reason the two harnesses cannot be compared knob for knob.

**What it means for interventions.** In VulnHunter an intervention on a rule changes the prompt text and its effect passes through model compliance. In VVAH an intervention on a rule changes a value that code reads and takes effect with certainty. Effects measured in one harness cannot be assumed to transfer.

**Evidence strength.** Verified in source.

---

## Design conflict 2: the search is bottom-up in one harness and top-down in the other

**VulnHunter's choice.** Reconnaissance first builds an inventory of every input the application accepts: Step 1b is titled "Input Inventory (CRITICAL — this drives the entire audit)" (`vulnhunt/phases/phase1_recon.md:51`). The hunt then follows each input forward through the code until it reaches a dangerous sink, and records a disposition for it. A separate sink-driven agent starts from the sinks instead (`vulnhunt/phases/phase2_hunt.md:25`, "Also spawn 1 sink-driven audit agent").

**VVAH's choice.** Stage 2 builds a threat model first: for each trust boundary the model walks the STRIDE categories (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) and proposes threats (`vvaharness/pipeline/stages/s2/prompts.py:61`). Stages 3 and 4 then investigate each proposed threat. The code of the application is read in service of a hypothesis, not in order to enumerate inputs.

**Why the two conflict.** A bottom-up search finds what the code does and asks whether it is dangerous; a top-down search imagines what could go wrong and asks whether the code allows it. They answer different questions and fail in different ways. The bottom-up search cannot report a design weakness that has no input to trace (for example a missing control), and spends effort on inputs that no threat would name. The top-down search cannot report a weakness the threat model did not think of. The two also disagree about when planning happens: VulnHunter plans by enumeration before any judgement, VVAH plans by judgement before any enumeration.

**Consequence for results.** The sets of findings the two harnesses can reach are different by construction. VVAH adds a separate skill `missing-controls` and a baseline checklist per kind of repository (`vvaharness/rules/repo_kinds.py`) to compensate for the weakness of the top-down search; VulnHunter compensates for the weakness of the bottom-up search with its threat model section and the absent-input checkpoint in the hunt phase.

**What it means for interventions.** Changing how many threats Stage 2 may emit (`step2.max_threats`, default 50) and changing the size at which VulnHunter splits a partition (`prompt.recon.oversize_inputs`, default 20) both change coverage, but through different mechanisms, so they should not be treated as the same lever.

**Evidence strength.** Verified in source.

---

## Design conflict 3: complete coverage means something different in each harness

**VulnHunter's choice.** Coverage is defined over the input inventory. After the class-group agents return, their dispositions are merged per input and the count is compared with the inventory count from Phase 1; unresolved inputs must be investigated before the candidate list is presented (`vulnhunt/phases/phase2_hunt.md:213` and `:233`, "Merge input dispositions across class groups"). The minimum number of agents is stated as a formula: "Minimum agent count = (3 × production_partition_count) + 1 sink-driven" (`vulnhunt/phases/phase2_hunt.md:30`).

**VVAH's choice.** Coverage is a ceiling set by Stage 2. Stage 4 only investigates files named in some threat's `surface_files`, and Stage 2's output is cut to `step2.max_threats` threats (`vvaharness/pipeline/stages/s2/__init__.py:235`). Paths in a threat that do not resolve to the inventory are dropped by code (`vvaharness/pipeline/stages/s2/outcomes.py:52`). The harness reports files named by no investigation unit in its diagnostics, which acknowledges the gap but does not close it.

**Why the two conflict.** VulnHunter treats an uninvestigated input as a defect to be detected by counting; VVAH treats an uninvestigated file as an accepted consequence of the threat model. The first design promises that every input is looked at within its supported class groups; the second promises only that every proposed threat is looked at.

**Consequence for results.** On a large application VVAH's recall is bounded by the quality and the cap of one model call, and VulnHunter's recall is bounded by the model's willingness to continue through a long list. VulnHunter also limits itself to three class groups (`vulnhunt/phases/phase2_hunt.md:46`), so its coverage is complete only within the classes it knows.

**What it means for interventions.** The coverage ceiling is a different object in each harness: a number in VVAH, a counting rule in VulnHunter's prompt.

**Evidence strength.** Verified in source.

---

## Design conflict 4: the unit of work is a partition in one harness and a threat in the other

**VulnHunter's choice.** The application is partitioned by computing which inputs share application functions (union-find, `vulnhunt/phases/phase1_recon.md:289`), partitions larger than 20 inputs or 15 application files are split (`phase1_recon.md:312`), and a hunt agent is started for every pair of production partition and class group. Agents are dispatched in waves of at most six (`phase2_hunt.md:54`).

**VVAH's choice.** One investigation unit is made per threat, ranked by impact times likelihood, with sizes defined by lines of code: small below 2,000 and medium below 8,000 (`vvaharness/pipeline/stages/s3_decompose.py:32`). Units that share files are placed together in one session by `plan_batches` (`vvaharness/pipeline/stages/s4/batching.py:34`), with large units alone, up to `step4.parallel` sessions at a time (default 12).

**Why the two conflict.** The partition is derived from the structure of the code; the threat is derived from the model's reading of the design. Two inputs in one partition can belong to unrelated threats, and one threat can span several partitions. One harness limits context by splitting the code and the other by splitting the hypotheses, so the context each investigator sees is cut along different lines.

**Consequence for results.** A vulnerability that crosses partitions is seen by one harness through the cross-class merge of dispositions and by the other through one threat's surface files. Neither mechanism is guaranteed to bring the relevant files together.

**Evidence strength.** Verified in source.

---

## Design conflict 5: false positives are removed by gates and a binary verdict in one harness, and by confidence and a three-way verdict in the other

**VulnHunter's choice.** Each candidate must pass five hard gates in a fixed order before it is recorded (`vulnhunt/phases/phase2_shared.md:111`). Phase 2b then re-examines every candidate with a stated prior: "Historically, ~50% of candidate findings are false positives" (`vulnhunt/phases/phase2b_verify.md:18`). The verdict is binary: confirmed or false positive. A consensus rule lets an elimination that all agents of a partition support with the same evidence at the first gate stand without re-reading the source, while every candidate is fully verified (`phase2b_verify.md:31`).

**VVAH's choice.** Stage 6 tells the verifier "Assume each one is WRONG until you have confirmed it yourself" (`vvaharness/pipeline/stages/s6/prompts.py:25`). The verifier returns one of three verdicts with a confidence from 0 to 10. A true positive below `step6_verify.min_confidence` is dropped; an inconclusive verdict is kept as undetermined (`vvaharness/pipeline/stages/s6/outcomes.py:262`). Code then validates paths, lines and Common Weakness Enumeration labels.

**Why the two conflict.** They disagree about uncertainty. VulnHunter has no category for "I cannot tell": the verifier must choose confirmed or false positive, and the gates push towards elimination when a condition is not met. VVAH keeps uncertain findings in the report as undetermined and lets the operator choose the cut-off with a number. They also disagree about the source of the prior: VulnHunter gives the verifier a historical base rate (about half are false), while VVAH gives a stance (assume wrong) with no base rate.

**Consequence for results.** At the same underlying evidence, VulnHunter produces fewer reported findings with no undetermined class, and VVAH produces more with an explicit uncertainty class. Precision and recall measured on the same repository would therefore reflect this design choice as much as the quality of the detection.

**What it means for interventions.** The confidence floor is a continuous lever in VVAH and has no counterpart in VulnHunter, where the nearest lever is the text of the gates.

**Evidence strength.** Verified in source.

---

## Design conflict 6: proof of exploitability is mandatory but usually not executed in one harness, and optional but executed in the other

**VulnHunter's choice.** Phase 3 produces a proof of concept and an exploit test for every confirmed High or Medium finding, and the phase is headed "Exploit Test (MANDATORY — DO NOT SKIP)" (`vulnhunt/phases/phase3_reproduce_test.md:109`, severity scope at `phase3_reproduce_test.md:22`). The test is run only when the model has a shell; the default scan removes the shell, so the same file speaks of "running (or mentally executing)" the test (`phase3_reproduce_test.md:194`). The default tools are `Agent`, `Glob`, `Read` and `Write` (`vulnhunter-agent/agent/config.py:572`), and the shell is enabled only by `--enable-bash` together with `--no-read-only` (`vulnhunter-agent/agent/__main__.py:238`).

**VVAH's choice.** The scan has no proof stage by default. An optional exploit verification stage (beta) classifies findings, maps endpoints, generates payloads, attacks a running target and judges the outcome, and it can only add confirmation: it never removes a finding and, in every shipped profile, it does not override the static verdict (`step6_exploit_verification.enabled` is `auto`, `vvaharness/config/__init__.py:506`). This stage is outside the scope of this study and is mentioned only to describe the design.

**Why the two conflict.** One harness requires a proof artefact for every important finding but, in its default configuration, produces that artefact by reasoning rather than by execution. The other produces proof only by execution but treats it as an extra. The word "mandatory" in a VulnHunter prompt and the word "optional" in a VVAH setting describe the same activity with opposite obligations, and in practice neither default executes exploit code.

**Consequence for results.** A VulnHunter finding that carries a proof of concept has not necessarily been demonstrated; the proof is a model-written argument in the default mode. A VVAH finding without live verification carries no proof at all. Readers who treat the presence of a proof of concept as evidence will draw the wrong conclusion from VulnHunter's report.

**Evidence strength.** Verified in source for the defaults and the tool list; the statement that live verification never overrides the static verdict in any shipped profile is verified in earlier reading; that the default VulnHunter scan does not execute tests is inferred from the tool list and the wording at `phase3_reproduce_test.md:194`.

---

## Design conflict 7: how far the model is trusted to follow the rules

**VulnHunter's choice.** Rules are written as instructions with strong wording, and compliance is checked by the model itself against counts. The model is asked to STOP if it is not at least Opus 4.7 (`vulnhunt/SKILL.md:18`), to answer a fixed list of checks per candidate, and to match counts between stages.

**VVAH's choice.** The prompt is treated as a request and the result as untrusted: every reply is a typed object, a malformed reply gets a bounded re-ask or one repair call, and code checks the content (`docs/architecture.md`, section "How a stage runs"). Examples include path checks against the inventory, dropping any chain with fewer than two distinct findings, and only allowing severity changes that the evidence supports.

**Why the two conflict.** They answer opposite ways to whether the model may be left to police itself. The VulnHunter fixer, by contrast, is heavily mechanised (seven delivery gate scripts, `vulnhunter-fix/scripts/run-gates.py`), which shows that VulnHunter itself does not trust prose alone after the scan; the scan phases remain prose-governed.

**Consequence for results.** A VulnHunter scan can silently under-perform when a long conversation degrades compliance; a VVAH scan degrades visibly, through drops and counters. VVAH can also fail by over-filtering, since code gates reject a correct finding whose path or line does not resolve.

**Evidence strength.** Verified in source for each side; the comparative conclusion is inferred.

---

## Design conflict 8: resource governance is absent in one harness and pervasive in the other

**VulnHunter's choice.** The scan session is opened with no maximum number of turns and no maximum cost (`vulnhunter-agent/agent/runner.py:680`, registry entries `sdk.max_turns` and `sdk.max_budget_usd` are not set). Termination relies on the model finishing, a stall timeout for helper agents, and the launcher giving up after 60 idle re-prompts (`runner.py:459`). Cost is measured and recorded but never enforced.

**VVAH's choice.** Every model stage has limits on turns, model calls, tokens and a wall clock deadline (for example `step4.max_turns` 15, `step4.max_model_calls` 8 in the shipped profile, `step4.deadline` 600 seconds). When a deadline passes, the harness resumes the live session with one instruction or, failing that, replays the transcript without tools at low effort, and distrusts the replayed result downstream (`vvaharness/pipeline/stages/replay.py`). The last permitted model call has all tools removed except the one that reports the outcome.

**Why the two conflict.** One harness accepts open-ended cost in exchange for not truncating the search; the other accepts truncation in exchange for predictable cost. The consequence is that cost, latency and thoroughness trade off in opposite directions, and the same repository can cost very different amounts in the two harnesses with no setting to equalise them.

**What it means for interventions.** Interventions on budget are expressible in VVAH as a number and in VulnHunter only by changing how many agents the prompt asks for or by editing the launcher.

**Evidence strength.** Verified in source.

---

## Design conflict 9: a scan can be resumed in one harness and is forbidden to start over in the other

**VulnHunter's choice.** The launcher refuses to start if a results directory from an earlier scan exists in the clone, so that the model cannot read its own previous output (`vulnhunter-agent/agent/runner.py:411`, "Refuse to start when an existing ``*_VULNHUNT_RESULTS_*`` dir is present"). A failed scan is restarted from nothing.

**VVAH's choice.** State is kept in a database outside the repository, a rerun of one stage invalidates every later checkpoint, and `--resume` continues a scan; if the repository's head commit has changed since the checkpoint, the run is reset (`vvaharness/orchestrator/scan.py:396`).

**Why the two conflict.** The same wish, not reading earlier output, is satisfied by prohibition in one harness and by keeping state outside the repository in the other. The consequence is that VulnHunter's long scans carry the full risk of loss while VVAH's can be recovered, and an experiment design that assumes repeated runs on one clone is possible only in VVAH.

**Evidence strength.** Verified in source.

---

## Design conflict 10: one model for everything versus a model per role

**VulnHunter's choice.** The scan uses one configured model, which the documentation requires to be Opus (`anthropic.model`, required, `vulnhunter-agent/agent/config.py:448`). Cheaper models are used only for extraction and deduplication of issues, with a fallback chain.

**VVAH's choice.** Each role (auto-exclusion, threat modelling, deep investigation, verification, deduplication, chaining, remediation, validation) has its own model, route and provider, and four routes exist (command line, software development kit, OpenAI-compatible, and a deepagents graph route). Even stages that make no model call still require a model key to be present and probed.

**Why the two conflict.** VulnHunter's design assumes that one strong model reasons about everything, including orchestration; VVAH's design assumes roles that can be served by different models. The consequence for comparison is that "which model" is a single knob in one harness and a vector of knobs in the other, and some VVAH routes give the same setting different meaning (for example the turn limit is a hard cap on one route and a floor on another).

**Evidence strength.** Verified in source.

---

## Design conflict 11: the lifecycle is split across skills in one harness and contained in one pipeline in the other

**VulnHunter's choice.** Scanning, filing issues, verifying a fix and writing a fix are different skills that communicate through GitHub issues and markers inside issue bodies (`vulnhunter-agent/agent/issues.py`, `verify.py`; the fixer and fix verifier live in `vulnhunter-fix/` and `vulnhunt-fix-verify/`). The fix verifier is a separate session with a read-only tool set.

**VVAH's choice.** Remediation (Stage 10) and fix validation (Stage 11) are optional stages of the same pipeline, enabled by `step_remediate.enabled` and `step_validate.enabled` (both off in the default profile), and results leave as `findings.json`, Markdown and SARIF.

**Why the two conflict.** The unit of exchange differs: a human-visible issue with tamper detection in one harness, structured files in the other. The consequence is that fix verification in VulnHunter is anchored to a public record that a developer can edit (and the harness reconstructs the original body to detect this), whereas VVAH has no such external record to protect.

**Evidence strength.** Verified in source.

---

## Design conflict 12: humans take part in fixing in one harness and nowhere in the other

**VulnHunter's choice.** The fixer asks the operator to approve or pause at every phase boundary and uses a collaboration loop with explicit option lists when it is blocked (`vulnhunter-fix/SKILL.md`, phase boundary gate; `vulnhunter-fix/prompts/implement.md`, collaboration loop).

**VVAH's choice.** Remediation and validation run unattended, selecting the top findings by severity score and bounded by a policy gate before and after the model acts.

**Why the two conflict.** They make opposite assumptions about who carries responsibility for a risky change: a person in VulnHunter, a policy in VVAH. The consequence is that VulnHunter's fixer cannot be run in batch and VVAH's cannot ask a question.

**Evidence strength.** Verified in source.

---

## Design conflict 13: one harness measures itself and the other does not

**VulnHunter's choice.** A local harness clones repositories at fixed commits, scans, judges the findings against known vulnerabilities with a model, tallies a detection rate, and runs a miss analysis that proposes prompt edits (`harness/local_harness/benchmark/`). The judge is lenient (a shallower classification in the same data flow counts) and scores recall only, so false positives are not measured.

**VVAH's choice.** No evaluation harness exists in the repository.

**Why the two conflict.** This is a difference of feedback loops rather than of design philosophy, but it conflicts in effect: VulnHunter's prompts have been shaped by a recall-only signal, which biases them towards finding more, while VVAH's thresholds were set without a published measurement. The two sets of defaults are therefore tuned against different, partly unobserved, objectives.

**Evidence strength.** Verified in source for the existence of the benchmark and its recall-only scoring; the claim about the influence on prompts is inferred.

---

## Where the conflicts matter most for later work

1. Conflicts 1, 7 and 8 determine whether an intervention is certain (VVAH) or mediated by model compliance (VulnHunter). They should be treated as a property of the experiment, not a detail of any one knob.
2. Conflicts 2, 3 and 4 determine what can be found at all. Comparisons of recall between the harnesses mix differences of method with differences of tuning.
3. Conflict 5 and conflict 6 determine what is reported as a finding and with what evidence, so any precision measurement depends on them.
4. Conflicts 9 and 13 determine whether repeated trials and feedback are possible.

The next layer (`02-mid-level-conflicts.md`) descends to individual mechanisms: how each harness implements verification, deduplication, severity, context supply, tool access, termination and fixing, and where those implementations disagree.
