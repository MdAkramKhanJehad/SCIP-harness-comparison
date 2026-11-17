# Contradictions inside VulnHunter (low level)

## Introduction

This document lists places where VulnHunter (repository `/home/spl/akram/harness-comparison/VulnHunter/`) contradicts itself. Every finding was confirmed by opening both locations in the real source and quoting the text with line numbers. Line numbers refer to the working tree as checked out. Nothing was run: this is a reading study.

What was read, in full or in the relevant parts:

- The scan orchestrator prompt `vulnhunt/SKILL.md` and all phase files (`phase1_recon.md`, `phase2_hunt.md`, `phase2_shared.md`, the three class-group files, `phase2b_verify.md`, `phase3_reproduce_test.md`, `phase3c_fixes.md`, `phase3d_sweep.md`, `phase4_report.md`), compared pair by pair for numbers, orderings, verdict names and gate order.
- The verification skill `vulnhunt-fix-verify/` (orchestrator, phase 2, phase 4, schema `vulnhunter-agent/verify_disposition.schema.json`).
- The fixer `vulnhunter-fix/` (`SKILL.md`, `config.json`, prompts, reference rule books, `scripts/run-gates.py`, `scripts/compute-completeness-tier.py`, `scripts/setup_worktree.sh`, `vulnhunter_fix/delivery.py`).
- The Python launcher and helpers in `vulnhunter-agent/agent/` (`config.py`, `config.example.toml`, `runner.py`, `publish.py`, `verify_refs.py`, `issues_extract.py`, `manifest` schema) and the benchmark harness in `harness/local_harness/`.

Counts: 38 confirmed findings. By consequence level: 8 high, 20 medium, 10 low. By kind: prompt against prompt 18; prompt against code 6; configuration against code 4; configuration against configuration 2; documentation against behaviour 3; dead or unreachable rules 3; ambiguity with consequence 2 (several findings also contain a second kind in their text; the first listed kind is counted here). Evidence strength is "verified in source" for every finding unless stated; where a consequence is an inference about model behaviour rather than something the text itself forces, the finding says so.

---

### Finding 1: The shipped agent gives the scan no search tool, while every phase file requires one

- **Kind:** Prompt against code
- **Where:**
  - `vulnhunt/phases/phase2_shared.md:151` "Use the **Grep tool** to search for all call sites of the suspect symbol across the codebase."
  - `vulnhunt/phases/phase2_shared.md:157` "This check is one tool call — never skip it."
  - `vulnhunter-agent/agent/config.py:572` `default=["Agent", "Glob", "Read", "Write"],`
  - `vulnhunter-agent/agent/config.example.toml:93` "Add `Grep` if forward-tracing through the source tree starts coming back"
  - `harness/local_harness/scan.py:443` `"--tools", "Read,Write,Edit,Grep,Glob,Agent"`
- **What conflicts:** The scan prompts instruct the model to use the Grep tool for reachability (Gate 1), caller exhaustion, sweeps, and the sink-driven audits. The headless agent, which is the production launcher, restricts the tool list to Agent, Glob, Read and Write. The benchmark harness, which measures the harness, gives the model Grep and Edit.
- **What actually happens:** `runner.py:199-204` renders the kickoff line from the effective tool list, so the model is told "Bash is NOT available — use Glob/Read/Write only." The skill text is unchanged and still demands Grep. The example configuration comment treats Grep as an optional extra to add "if forward-tracing ... starts coming back empty".
- **Consequence:** In production runs, caller enumeration, sink-pattern greps and the sweep (Phase 3d) must be done by reading files one by one, so coverage depends on the model's patience and the context budget. Benchmark detection rates are measured with a stronger tool set than production uses, so the benchmark overstates production recall.
- **Consequence level:** high
- **Knobs involved:** `scan.allowed_tools`
- **Evidence strength:** verified in source

### Finding 2: Vendored code is declared off limits, yet sanitizer verification requires reading vendored source that read-only scans never install

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/SKILL.md:84-86` "Always ignore the following — never report findings in them, never trace data flows through them, never investigate annotations in them"
  - `vulnhunt/SKILL.md:100` "**Vendored/third-party code**: `**/vendor/**`, `**/node_modules/**`,"
  - `vulnhunt/phases/phase2_class_inj.md:124` "**(a) Read the sanitizer's source code** (in node_modules, vendor, stdlib, or the project's own code)"
  - `vulnhunt/phases/phase2_shared.md:214-215` "If the source is unavailable, **treat the defense as ineffective** — do NOT assume it works."
  - `vulnhunt/SKILL.md:54` "Read-only → skip to Phase 1"
- **What conflicts:** Gate 2b demands that every defense be confirmed by reading its source, including third-party sanitizers, but the operating principles forbid tracing through those directories. Dependency installation is skipped in the default read-only mode, so `node_modules` and similar directories do not exist.
- **What actually happens:** The only rule that can be followed literally in a read-only scan is the fallback: the source is unavailable, so the defense is treated as ineffective and the candidate proceeds with its finding intact. Option (b) in the class file (run a one-line test such as `node -e`) needs a shell that the default agent does not have.
- **Consequence:** Candidates guarded by well-known third-party sanitizers and framework protections are kept rather than cleared at Gate 2b. This raises candidates that Phase 2b (adversarial verification) must then remove, with the same missing source, so false positives are likely to reach the report. This is an inference about the sanitizer cases; the instruction conflict itself is verified.
- **Consequence level:** high
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 3: The sink-driven audit agent has no output file, no return limit and an unspecified hand-off

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2_hunt.md:109` "Write results to: ${VULNHUNT_DIR}/results/sg-{SG_ID}_{class}_results.md" (trace agent template only)
  - `vulnhunt/phases/phase2_hunt.md:201-202` "For each finding, return the candidate format used by trace agents (but do NOT assign VULN-NNN IDs)."
  - `vulnhunt/SKILL.md:338` "Return messages from subagents must be ≤20 words"
  - `vulnhunt/phases/phase2b_verify.md:24` "Before verifying anything, read every result file and build a flat list of all CANDIDATE entries"
  - `harness/local_harness/benchmark/analyze_misses.py:~200` expects a results filename containing `sink_driven`
- **What conflicts:** The trace agents are told to write to a named file and to return fewer than twenty words. The sink-driven prompt (lines 141-203) names no file and tells the agent to "return" its candidates. Returning candidates in the message breaks the twenty-word rule; returning twenty words loses them. Phase 2b only reads result files.
- **What actually happens:** Nothing in the text says where the sink-driven candidates live. The orchestrator is told at line 205 to "Merge the sink-driven agent's candidates into the main results", but is also forbidden to hold analysis in its context (Finding 22).
- **Consequence:** Findings that only the sink-driven audits can reach (wildcard cloud permissions, credential-issuing paths, weak cryptography, race conditions, attempt counters) may never reach Phase 2b, so they would be silently absent from the report. Whether it happens depends on what the model chooses to do with the undefined output, which is the point of the gap.
- **Consequence level:** high
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 4: The Phase 3 identifier table counts only "High and Medium" findings, but the severity scale has five tiers

- **Kind:** Ambiguity with consequence
- **Where:**
  - `vulnhunt/phases/phase3_reproduce_test.md:22-23` "produce a VULN-NNN assignment table mapping every CONFIRMED finding from Phase 2b (High and Medium severity)"
  - `vulnhunt/phases/phase3_reproduce_test.md:28` "Row count MUST equal the total High + Medium CONFIRMED findings in Phase 2b."
  - `vulnhunt/phases/phase2_shared.md:307-336` tiers "High+", "High", "Medium", "Low", "Informational"
  - `vulnhunt/phases/phase4_report.md:60-61` "A finding is INVALID if either the **PoC** or **Exploit Test** field is empty"
- **What conflicts:** Read literally, the completeness table excludes the most severe tier (`High+`), the `Low` tier and the `Informational` tier (which Phase 2b section 8 says still gets a proof of concept). Phase 4 then invalidates any finding lacking a proof of concept and exploit test.
- **What actually happens:** The text does not say whether `High` means "High and above". If the table is built literally, a `High+` remote code execution finding is outside the row-count check that is meant to prevent dropped findings, and Low or Informational findings are never assigned a proof of concept.
- **Consequence:** Either the most severe findings escape the anti-drop check, or lower-tier confirmed findings are removed at report time as "INVALID". Both change what the report lists.
- **Consequence level:** high
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 5: Weak cryptography and hardcoded secrets are exempt from Gate 2a in one prompt and eliminated by the input rule in another

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2_hunt.md:174-176` "Attacker-controlled input is NOT required — weak crypto is a flaw in the protection mechanism itself. Do NOT apply Gate 2a to eliminate crypto findings."
  - `vulnhunt/phases/phase2b_verify.md:58-61` "If a candidate has no attacker-controlled input ... it fails Gate 2a. Route to Code Quality, not VULN-NNN."
  - `vulnhunt/phases/phase2_shared.md:189` "If the input is NOT attacker-controlled, eliminate the finding."
  - `vulnhunt/phases/phase2_class_log.md:238` "- Hardcoded secrets/keys"
- **What conflicts:** The crypto exemption exists only inside the sink-driven agent prompt. The logic and crypto trace agents (`phase2_class_log.md`) list hardcoded secrets, weak algorithms and insecure random numbers as classes but do not repeat the exemption; they read `phase2_shared.md`, which eliminates anything not attacker-controlled. Phase 2b section 1 then tells the verifier to do the same.
- **What actually happens:** A weak-cipher candidate from the sink-driven agent is created because Gate 2a does not apply, then met in Phase 2b by a rule that applies Gate 2a and sends it to Code Quality. The Phase 4 code-smell source list ("Crypto inventory") partly catches it, but only as a defence-in-depth note.
- **Consequence:** Whether a hardcoded key or weak cipher is a finding or a code smell depends on which agent met it first. Because Phase 3d sweeps for "all hardcoded keys" and "all weak crypto" on the strength of one confirmed instance, the inconsistency is multiplied.
- **Consequence level:** high
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 6: Sequential-fallback partitions are processed inline in the orchestrator, against three other rules, and their output goes where Phase 2b does not look

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2_hunt.md:29-30` "Do NOT analyze partitions "inline" — every production partition gets agents. **Minimum agent count = (3 × production_partition_count) + 1 sink-driven.**"
  - `vulnhunt/phases/phase2_hunt.md:67-68` "**SEQUENTIAL-FALLBACK partitions**: process sequentially in the orchestrator's context"
  - `vulnhunt/phases/phase2_hunt.md:255` "`${VULNHUNT_DIR}/candidates/sg-N_entrypoint_classgroup.md`"
  - `vulnhunt/SKILL.md:326-327` "You do NOT perform analysis yourself."
  - `vulnhunt/SKILL.md:251` "Read all result files from `${VULNHUNT_DIR}/results/`."
  - `vulnhunt/phases/phase1_recon.md:312-319` oversized partitions ">20 inputs or >15 app-specific files"; fallback only when "cannot split below 20 inputs"
- **What conflicts:** The dispatch procedure forbids inline analysis and sets a minimum agent count that includes every production partition, yet the fallback requires the orchestrator to analyse those partitions itself, which the orchestrator role forbids. The fallback saves to `candidates/`, while Phase 2b is told to read `results/`. Phase 1 splits a partition that exceeds fifteen files but only falls back when it exceeds twenty inputs, so a partition with eighteen inputs and thirty files is neither splittable nor marked.
- **What actually happens:** The largest, most complex codebases are the ones that produce fallback partitions. Their candidates exist only in `candidates/` files and in the orchestrator's context, and Phase 2b builds its candidate manifest from `results/`.
- **Consequence:** Findings from the largest partitions can be missing from verification and from the report, and the count of agents the orchestrator is told it "violated the procedure" by not reaching cannot be met.
- **Consequence level:** high
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 7: A deleted code path is called "fixed" by Gate 2 but makes Gate 1 "skipped", which can never produce `FIXED`

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt-fix-verify/phases/phase2_verify.md:73-74` "mark the gate `skipped` and note "original location absent; no successor found""
  - `vulnhunt-fix-verify/phases/phase2_verify.md:104-107` "the code path was deleted entirely ... The verdict still counts this as fixed"
  - `vulnhunt-fix-verify/phases/phase2_verify.md:166` "All applicable gates pass."
  - `vulnhunt-fix-verify/phases/phase2_verify.md:169` "at least three gates `skipped` and `sink_mitigated` not definitive"
- **What conflicts:** For a fix that deletes the vulnerable endpoint, Gate 1 finds no sink and no successor and records `skipped`; Gate 2 is said to count that case as fixed. The verdict table requires every applicable gate to be `pass` for `FIXED`, and a `skipped` gate is not a pass.
- **What actually happens:** A removed code path produces `skipped` at Gate 1. The table gives `FIXED` only when all applicable gates pass, so removal cannot yield `FIXED`; it yields `INCONCLUSIVE` only if three gates are skipped, and is otherwise outside every verdict row (Finding 23).
- **Consequence:** Removing the vulnerable feature is the most reliable fix, and the verifier cannot recognise it. The issue is reopened for manual review as `INCONCLUSIVE` or falls into an undefined case.
- **Consequence level:** high
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 8: The `INCONCLUSIVE` stub that rescues a failed verification omits a field the schema requires, which fails the whole run

- **Kind:** Prompt against code
- **Where:**
  - `vulnhunt-fix-verify/SKILL.md:173-175` "write a stub `INCONCLUSIVE` for it with a rationale noting the failure and continue — a partial result is preferable to halting the whole run."
  - `vulnhunt-fix-verify/phases/phase2_verify.md:35-38` stub with "verdict `INCONCLUSIVE`, rationale describing the missing section, and all four gates `skipped`"
  - `vulnhunter-agent/verify_disposition.schema.json` (disposition, `required` lists `issue_comment`; `issue_comment` has `minLength` 1)
  - `vulnhunter-agent/agent/verify_runner.py:169` validates against `verify_disposition.schema.json`
- **What conflicts:** The stub description lists a verdict, a rationale and four gates, but never an `issue_comment`, which the schema marks as required and non-empty, and which the agent posts verbatim to the issue. The skill promises that a partial result is better than halting.
- **What actually happens:** A stub written as described fails schema validation. The agent then treats the run as an infrastructure failure (`SCHEMA_INVALID`) and, as designed, makes no GitHub change for any issue in the batch. Phase 4 would have to supply the missing comment, but nothing tells it to.
- **Consequence:** One failed finding can cancel the verdicts, comments and reopenings of all findings in the same run, the opposite of the stated intent.
- **Consequence level:** high
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 9: The report allows statuses and tiers that the issue extractor discards

- **Kind:** Prompt against code
- **Where:**
  - `vulnhunt/phases/phase4_report.md:32` "Confirmed/Fixed/Verified" (Status column) and `vulnhunt/phases/phase4_report.md:172-174` Informational findings under section 8 "ARE reported with full data flow and PoC"
  - `vulnhunter-agent/agent/issues_extract.py:75-78` "ONLY findings whose status is "Confirmed" are in scope; ignore ... "Informational", or any finding marked anything other than "Confirmed""
- **What conflicts:** The report format lets a finding carry status `Fixed` or `Verified`, and reports findings downgraded to `Informational` as findings with full detail. The extractor posts issues only for rows whose status is exactly `Confirmed` and tells the extraction model to ignore `Informational`.
- **What actually happens:** The scan "does not modify source files" (`phase4_report.md:8`), so `Fixed` cannot be true, but a model that marks a passing exploit test as `Verified` is a plausible reading of "PASS" and "Verified". Informational rows from the authorization delegation rule are real reported findings.
- **Consequence:** Reported findings can silently fail to become issues, and therefore never reach the fixer, depending on a free-text status word that the report format leaves open.
- **Consequence level:** medium
- **Knobs involved:** `issues.enabled`
- **Evidence strength:** verified in source

### Finding 10: The report severity scale has `High+`, but the issue extractor and manifest schema have `Critical`

- **Kind:** Prompt against code
- **Where:**
  - `vulnhunt/phases/phase4_report.md:32` "High+/High/Medium/Low/Informational"
  - `vulnhunter-agent/agent/issues_extract.py:93` `"severity": "Critical|High|Medium|Low",`
  - `vulnhunter-agent/scan_manifest.schema.json:68` `"enum": ["Critical", "High", "Medium", "Low", ""]`
  - `vulnhunter-fix/prompts/parse_issues.md:206` "Recognize `Critical`, `High+`, `High`, `Medium`, `Low`. **Normalize `High+` → `Critical`**."
- **What conflicts:** The scanner never emits `Critical`; the extractor asks the model to pick from a scale that does not contain `High+`, and no code in `vulnhunter-agent/agent/` maps `High+` to anything. The fixer does map `High+` to `Critical`, so it expects reports to contain both.
- **What actually happens:** The extractor model must decide what `High+` means. If it copies `High+` literally, the value is outside the manifest enumeration; if it writes `High` the most severe findings are labelled one tier lower than the report says. The exact outcome is an inference about model behaviour.
- **Consequence:** Severity of the most serious findings is unstable in issues and in the manifest, which the fixer then uses to cluster and order work.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source for the text conflict; inferred for the outcome

### Finding 11: Candidates raised during Phase 1 are never delivered to Phase 2b

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase1_recon.md:356-358` "Any match is a CANDIDATE even if no inventoried input currently reaches it ... Add them to the inventory as "gate logic" entries"
  - `vulnhunt/phases/phase1_recon.md:374-375` "Add these to the inventory as "auth bypass path" entries for Phase 2 tracing."
  - `vulnhunt/phases/phase1_recon.md:218-224` partitions are built in Step 1d, before Steps 1e and 1f
  - `vulnhunt/phases/phase2b_verify.md:24` "read every result file and build a flat list of all CANDIDATE entries"
  - `vulnhunt/SKILL.md:237-238` "Read ONLY the partition table and input inventory table for dispatch"
- **What conflicts:** Steps 1e and 1f declare candidates and add inventory rows after the partition table exists, so no partition and no trace agent owns them. Phase 2b only reads trace result files, and the orchestrator reads only two tables of the recon file.
- **What actually happens:** The "gate logic" and "auth bypass path" rows have no entry point, so nothing in the dispatch procedure assigns them to a partition. The Phase 2 completeness check requires every inventory row to have a disposition, so either that check fails or the rows are dropped.
- **Consequence:** Latent authorization bypasses (substring allow-list checks, unverified authentication branches) found in Phase 1 are among the highest-value findings and can disappear before verification.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 12: Phase 1 marks whole partitions "dev-only" by route gating, which Gate 1 says is not enough

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase1_recon.md:327-336` "Check if the route is behind an environment gate ... mark all inputs as `SAFE (not production-reachable)`."
  - `vulnhunt/phases/phase2_shared.md:164-168` "**Route registration ≠ code reachability.** ... A dev-gated route mounting it does NOT make the code dev-only"
  - `vulnhunt/phases/phase2_hunt.md:24` "Skip DEV-ONLY partitions entirely (already marked SAFE in Phase 1)."
  - `vulnhunt/phases/phase2b_verify.md:129-132` SAFE spot-check applies to "SAFE inputs" of each subgraph
- **What conflicts:** The rule that forbids eliminating a sink because one route to it is dev-gated is applied by trace agents, but Phase 1 uses exactly that evidence (the route mounting) to remove entire partitions before any trace agent sees them.
- **What actually happens:** Inputs in a dev-only partition receive `SAFE` with no agent, no Gate 1 call-site search and no spot-check, because Phase 2b only re-verifies candidates and SAFE inputs "for each subgraph" that was traced. Shared functions are excluded from the union-find step, so a handler that is also used elsewhere may be marked dev-only.
- **Consequence:** A route that is dev-gated in one file but whose handler is reachable another way is eliminated at the cheapest point and never revisited.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 13: Candidate identifiers are requested from every trace agent and also assigned by the orchestrator, and the second assignment is never saved

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2_shared.md:367` "#### [VULN-NNN] Title" (candidate output format for each trace agent)
  - `vulnhunt/phases/phase2_hunt.md:223-224` "**Assign VULN-NNN IDs** to all candidates across all subgraphs. Number sequentially (VULN-001, VULN-002, ...)"
  - `vulnhunt/phases/phase2b_verify.md:24` "one line per candidate: SG-N class VULN-ID"
  - `vulnhunt/phases/phase3_reproduce_test.md:22` "produce a VULN-NNN assignment table mapping every CONFIRMED finding from Phase 2b ... to a sequential ID"
- **What conflicts:** Parallel agents each number their own candidates from the start of their file, so identifiers collide across result files. The orchestrator is meant to renumber, but nothing writes the renumbered list to disk, and the Phase 2b subagent reads result files, not the orchestrator's context. Phase 3 then assigns identifiers a third time.
- **What actually happens:** Phase 2b works with whatever identifiers are in the files, which may be duplicated across partitions. Phase 3 maps "Phase 2b #" to new identifiers, so the identifier in the verification table need not match the one in the final report.
- **Consequence:** Traceability from a candidate to its final finding can break, and duplicate identifiers risk two distinct candidates being treated as one row in the verification manifest.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 14: A failed exploit test has four different destinations, and one of them has no place in the report

- **Kind:** Ambiguity with consequence
- **Where:**
  - `vulnhunt/phases/phase3_reproduce_test.md:199-204` outcomes "Code Smell", "Eliminate", "Downgrade to **Potential**", "check if the exception itself leaks info"
  - `vulnhunt/phases/phase3_reproduce_test.md:247` "FAIL — constructor sig mismatch | Downgrade to Informational"
  - `vulnhunt/phases/phase4_report.md:172-174` Informational is excluded "that aren't exploitable"
  - `vulnhunt/phases/phase4_report.md:63` "downgraded to Potential or eliminated"
- **What conflicts:** The same word "FAIL" leads to Code Smell, elimination, `Potential` or `Informational`. `Informational` is reserved by the authorization delegation rule and excluded from the report otherwise. `Potential` is mentioned in three files but no section, table or heading in `phase4_report.md` defines where such a finding is written.
- **What actually happens:** The model chooses the destination. A finding sent to `Potential` or to a non-delegation `Informational` has no report section and is not a code smell, so it is not output.
- **Consequence:** Findings for which the exploit test could not be built (a frequent outcome in read-only scans) are lost rather than reported as unproven, which lowers visible recall and hides what a reviewer might want to check.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 15: Phase 2b routes items to "Code Quality", a route that Phase 3 and Phase 4 do not accept

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2b_verify.md:59-60` "If a candidate has no attacker-controlled input ... Route to Code Quality, not VULN-NNN."
  - `vulnhunt/phases/phase2b_verify.md:281` "**Drop all FALSE POSITIVE findings.** Only CONFIRMED findings proceed to Phase 3."
  - `vulnhunt/phases/phase3_reproduce_test.md:211-216` "Before downgrading any candidate to Code Smell, you MUST write the PoC file and the exploit test file ... FIRST"
  - `vulnhunt/phases/phase4_report.md:91-97` code-smell sources are near-misses, security configuration, crypto inventory and defence-in-depth gaps
- **What conflicts:** Phase 2b names verdicts `CONFIRMED`, `FALSE POSITIVE`, `consensus-skipped`, an elimination string and `SUBSUMED-BY`, and also a "Code Quality" route. Only `CONFIRMED` proceeds, and a code smell may only be created after a proof of concept and exploit test exist, which an item routed away in Phase 2b never gets.
- **What actually happens:** An item routed to Code Quality in Phase 2b is not `CONFIRMED`, so it is dropped; the Phase 4 code-smell source table does not list "no-input" or "IAM-delegated" items. The route has no receiver.
- **Consequence:** Operational-failure and IAM-gated items that the prompt says should be reported as code quality notes are never reported.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 16: Code smells must have proof of concept files, but the report says they have none, and the sweep treats every proof of concept file as confirmed

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase3_reproduce_test.md:211-213` "you MUST write the PoC file and the exploit test file in `${VULNHUNT_DIR}/poc/` FIRST"
  - `vulnhunt/phases/phase4_report.md:86` "They do not get VULN-NNN IDs or PoC files."
  - `vulnhunt/SKILL.md:272` "Read confirmed findings from `${VULNHUNT_DIR}/poc/`."
  - `vulnhunt/phases/phase3d_sweep.md:195` "(you know these from the poc/ files you already read)"
- **What conflicts:** Phase 3 puts proof of concept files for rejected candidates in `poc/`. Phase 4 says code smells have no such files. Phase 3d, which reads `poc/` to learn which findings are confirmed, cannot tell a confirmed finding from a smell.
- **What actually happens:** The sweep receives smell files as if they were findings and seeds root-cause sweeps from them, while the report artifact table and the "one row per exploit test PASS" check have to reconcile files that may or may not belong.
- **Consequence:** The sweep spends effort on non-findings and may promote instances of a pattern that Phase 3 already judged mitigated, adding false positives.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 17: The exploit-test examples assert the mechanism, while the rules say a test must prove the outcome; and in read-only scans no test is run

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase3_reproduce_test.md:118` "The test must prove the **attacker's goal is achieved**, not just that a code pattern exists."
  - `vulnhunt/phases/phase3_reproduce_test.md:175-179` "assert the payload reaches the query unescaped" `assert "OR '1'='1" in query`
  - `vulnhunt/phases/phase3_reproduce_test.md:189-190` "crypto (assert weak algorithm used)"
  - `vulnhunt/phases/phase2_shared.md:247` "The exploit test for Gate 3 must prove the OUTCOME, not the MECHANISM."
  - `vulnhunt/phases/phase3_reproduce_test.md:194` "After running (or mentally executing) each test"
- **What conflicts:** The rules and Gate 3 require the outcome (unauthorized data returned, plaintext recovered), but the worked examples and the guidance for crypto assert only that the payload reaches the query or that a weak algorithm is used. In the default read-only agent no test is run at all ("exploit tests written but not run", `SKILL.md:46`).
- **What actually happens:** A model that follows the examples writes mechanism-level tests that "pass" trivially; a model that follows the rules still cannot observe a result in read-only mode, so "PASS" is a mental judgement. Phase 4 requires PASS or FAIL for each row and counts rows by PASS.
- **Consequence:** The proof that is supposed to remove false positives is weakest in exactly the default mode, and the examples push it further toward mechanism-only checks.
- **Consequence level:** medium
- **Knobs involved:** `scan.allowed_tools`
- **Evidence strength:** verified in source

### Finding 18: The gateway-library rule contains a placeholder that was never replaced, so it cannot match

- **Kind:** Dead or unreachable rule
- **Where:**
  - `vulnhunt/phases/phase2b_verify.md:199` "A dependency whose import path matches `*<your-gateway>*` is PoP token validation."
  - `vulnhunt/phases/phase2b_verify.md:234` "`*<your-gateway>*` PoP."
  - `vulnhunt/phases/phase2_shared.md:359` "A dependency matching `*<your-gateway>*` is PoP validation"
  - `vulnhunt/phases/phase3c_fixes.md:65` "`*<your-gateway>*` PoP/mTLS AND caller-scope"
- **What conflicts:** Four rules (the authorization delegation severity ladder, the universal authentication gap rollup, the narrow severity exception and the fix guidance) depend on recognising a gateway library by an import pattern. The pattern is a literal template placeholder and no configuration or phase supplies a value.
- **What actually happens:** A dependency can never match the string `*<your-gateway>*`, so the shortcut "do not require reading the library source" can only be applied by a model that guesses which import is the gateway. Phase 1 separately forbids crediting "known-library shortcuts" (`phase1_recon.md:388-389`).
- **Consequence:** The downgrade of insecure direct object reference findings to `Informational` or `Medium`, and the platform-level rollups, depend on a guess; severity and subsumption differ run to run.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 19: The fix guidance forbids ownership checks, while the principles and the verifier require fixes that eliminate the class

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase3c_fixes.md:54-57` "Do NOT propose new `caller_scope.assert_caller_can_act_on_account`-style helpers ... or per-account ownership lookups in the service"
  - `vulnhunt/SKILL.md:82-83` "Proposed fixes must eliminate the vulnerability class, not just block the specific PoC payload."
  - `vulnhunt/phases/phase2_class_nav.md:46-47` "Does the code verify the authenticated caller owns or is authorized for THIS SPECIFIC ID?"
  - `vulnhunt-fix-verify/phases/phase2_verify.md:116-117` "Does the fix eliminate the vulnerability class, or only block the specific PoC payload?"
- **What conflicts:** The scan finds an insecure direct object reference because no ownership check exists, then Phase 3c prescribes only a header-presence check or an allow-list, explicitly excluding an ownership check, and states that this "lifts the finding to Informational on re-scan". The fix-verify skill later asks whether the class is eliminated.
- **What actually happens:** The proposed fix satisfies the delegation rule that lowers the severity label, not the ownership requirement the finding was raised for. A faithful implementation can be judged `PARTIAL` or `NOT_FIXED` by the verifier on the class-elimination gate.
- **Consequence:** Developers following the report's proposed fix may be told by the verification run that the fix is incomplete, and a re-scan that reports `Informational` may be read as "fixed".
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 20: Missing-authentication candidates are immune to elimination in the shared rules but routed away for identity-gated entry points in Phase 2b

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2_shared.md:283-285` "CWE-306/639 findings are immune to Gate 3 elimination when the baseline derives from all-NONE auth fields."
  - `vulnhunt/phases/phase2_shared.md:83-84` "CVB findings are **immune to DESIGN-INTENT and Gate 0 dismissal**"
  - `vulnhunt/phases/phase2b_verify.md:103-109` "route unconstrained inputs to Code Quality ... bare CWE-306 is Code Quality."
- **What conflicts:** The shared rules protect Common Weakness Enumeration 306 and 639 candidates from the usual eliminations and treat conditional validation bypass as non-dismissible. Phase 2b section 4 then sends bare 306 candidates on identity-gated entry points (queue and event consumers, cloud-permission entry points) to Code Quality.
- **What actually happens:** The boundary between a protected 306 candidate and a "bare" 306 is not defined. The Phase 2b rule is applied after the shared rule, so it wins whenever a consumer or permission-gated entry point is involved, and the Code Quality route has no receiver (Finding 15).
- **Consequence:** Missing-authentication findings on queue consumers and cloud-permission entry points are dropped by a rule that the earlier phases said could not drop them.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 21: The sink-driven agent is "in parallel" with the trace agents in one place and a final wave after them in another

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2_hunt.md:63-64` "Always dispatch the sink-driven agent as its own final wave after all partition agents complete."
  - `vulnhunt/phases/phase2_hunt.md:134` "In parallel with trace agents, spawn one additional agent"
  - `vulnhunt/phases/phase2_hunt.md:54-56` "Spawn agents in waves of at most 6"
  - `vulnhunt/SKILL.md:245` "**Minimum agent count = (3 × partition_count) + 1 sink-driven.**"
- **What conflicts:** The first text makes the sink-driven agent a separate wave after all partition agents. The second makes it run concurrently. With the waves-of-six cap, "in parallel" would put it in a wave with trace agents or, if placed in none, outside the cap that exists to prevent rate-limit failures.
- **What actually happens:** The worked example (six partitions, nineteen agents, four waves) follows the final-wave reading. The section heading "Orchestrator-Only Sections" and the sentence at line 134 follow the parallel reading. The model must pick one.
- **Consequence:** The choice changes the number of concurrent agents, so it affects rate-limit failures (cost and reliability) and whether the sink-driven agent can use the trace agents' results; it does not change what is reported by itself.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 22: The orchestrator is told never to read results or analyse, and also to merge, deduplicate and count them

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/SKILL.md:335` "Do NOT read result files, recon output analysis, or source code into your context"
  - `vulnhunt/SKILL.md:237-238` "Read ONLY the partition table and input inventory table for dispatch"
  - `vulnhunt/SKILL.md:242-243` "extracting each partition's inputs, file scope, shared infrastructure catalog, and threat model"
  - `vulnhunt/phases/phase2_hunt.md:213-221` "collect dispositions from all 3 class-group agents ... CROSS-CLASS: Cross-reference against the target class agent's results"
  - `vulnhunt/phases/phase2_hunt.md:239-243` "Absent-input verification checkpoint (MANDATORY)"
- **What conflicts:** The aggregation procedure requires the orchestrator to read every results file, resolve cross-class references, count dispositions and run a cross-input reasoning checkpoint that "single-partition agents cannot do". Dispatch also needs the shared infrastructure catalog and threat model, which the orchestrator is told it may not read.
- **What actually happens:** The orchestrator cannot do the aggregation without reading the files; if it follows the context rule it skips the merge, completeness check and absent-input checkpoint, and if it follows the merge rule it reads the files the rule forbids.
- **Consequence:** Either a mandatory checkpoint (conditional validation bypass across inputs) is skipped, or the context control that keeps long scans within the model window is broken. Either changes recall or cost.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 23: The verifier has three thresholds for `INCONCLUSIVE` and leaves common gate combinations without a verdict

- **Kind:** Ambiguity with consequence
- **Where:**
  - `vulnhunt-fix-verify/SKILL.md:232` "All four gates `skipped` for a finding → verdict is `INCONCLUSIVE`"
  - `vulnhunt-fix-verify/phases/phase2_verify.md:169` "at least three gates `skipped` and `sink_mitigated` not definitive"
  - `vulnhunt-fix-verify/phases/phase2_verify.md:109-112` "the overall verdict will be `INCONCLUSIVE` unless other gates give us enough signal"
  - `vulnhunt-fix-verify/phases/phase2_verify.md:164-169` verdict table; `phase2_verify.md:101-103` Gate 2 lists only pass, pass with flag, and skipped
- **What conflicts:** The orchestrator says all four gates; phase 2 says three; Gate 2 says one skipped gate is enough in some cases. The table has no row for, for example, sink pass with reachability skipped, or sink pass with reachability fail (Gate 2 defines no failing outcome). A `n/a` gate counts as passing for `FIXED` but does not count as skipped for `INCONCLUSIVE`.
- **What actually happens:** Sink pass, class pass, sweep pass and reachability skipped matches no verdict row, so the model chooses `FIXED`, `PARTIAL` or `INCONCLUSIVE` by judgement. Sink skipped, reachability skipped, class skipped and sweep `n/a` is `INCONCLUSIVE` by one rule and not by the other.
- **Consequence:** The verdict that controls whether an issue is reopened (`NOT_FIXED`, `PARTIAL`, `INCONCLUSIVE` reopen; `FIXED` does not) varies for the same evidence.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 24: The example configuration turns off the sandbox and issue posting, while the code defaults turn both on

- **Kind:** Configuration against configuration
- **Where:**
  - `vulnhunter-agent/agent/config.example.toml:72-74` `enabled = false` `fail_if_unavailable = true` (under `[sandbox]`)
  - `vulnhunter-agent/agent/config.py:506` `_resolve(sandbox_raw, "sandbox", "enabled", kind=bool, default=True)`
  - `vulnhunter-agent/agent/config.example.toml:152` `enabled = false` (under `[issues]`)
  - `vulnhunter-agent/agent/config.py:652` `_resolve(issues_raw, "issues", "enabled", kind=bool, default=True)`
- **What conflicts:** An operator who copies the example file gets no sandbox and no issues; an operator who supplies a partial file or none gets both. The example also sets `fail_if_unavailable = true` next to a disabled sandbox, so the setting that says "fail if the sandbox is unavailable" has nothing to apply to.
- **What actually happens:** `build_settings.py:99-107` writes whatever `cfg.sandbox` holds into the settings. Starting from the example, the operating-system sandbox that limits reads to the clone and network to the inference host is off.
- **Consequence:** The safety posture for scanning untrusted repositories differs by how the file was created, and issue posting can be switched on by omission. The default scan has no Bash, which lowers the effect of the sandbox, but the denied-read list is lost.
- **Consequence level:** medium
- **Knobs involved:** `sandbox.enabled`, `sandbox.fail_if_unavailable`, `issues.enabled`
- **Evidence strength:** verified in source

### Finding 25: The miss-analysis tool points at a prompt directory that does not exist and recognises phases the pipeline no longer has

- **Kind:** Configuration against code
- **Where:**
  - `harness/local_harness/benchmark/analyze_misses.py:32-37` `"phase1": ["skill/phases/phase1_recon.md"],`
  - `harness/local_harness/benchmark/analyze_misses.py:230` `prompt_paths = [os.path.join(REPO_ROOT, p) for p in prompt_files]`
  - `harness/local_harness/config.py:8` `REPO_ROOT = os.path.dirname(HARNESS_DIR)`
  - `harness/local_harness/benchmark/analyze_misses.py:151-162` loss phases are only `phase2b`, class results, `phase1`
- **What conflicts:** The prompts live in `vulnhunt/phases/`, not `skill/phases/`. In addition, `REPO_ROOT` resolves to the `harness/` directory, so even a correct relative name would be searched under `harness/`. The loss-phase logic never returns Phase 3 or Phase 3d, and the sink-driven results file name is guessed from `sink_driven`, a name the prompts never produce (Finding 3).
- **What actually happens:** The diagnostic agent is told to read prompt files that are not there. It can still reach prompts through the `--add-dir` argument only if that path also existed, and it does not (`analyze_misses.py:278`).
- **Consequence:** The benchmark's miss diagnosis, which is the harness's way of suggesting prompt edits, cannot see the prompts it blames, so its advice is not grounded in them, and misses lost in the exploit-test or sweep phases are mis-assigned.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 26: The fixer judges the same extraction model unreliable that the agent uses first for issue extraction

- **Kind:** Configuration against configuration
- **Where:**
  - `vulnhunter-fix/prompts/parse_issues.md:472` "README extraction was originally Haiku-targeted (the upstream `issues_extract.py` uses Haiku for this), but Haiku has proven unreliable"
  - `vulnhunter-fix/prompts/parse_issues.md:56` "Haiku has dropped findings on real reports"
  - `vulnhunter-agent/agent/config.py:674-678` `haiku_model ... default="claude-haiku-4-5"`
  - `vulnhunter-agent/agent/issues_extract.py:210-211` `primary_model=config.issues.haiku_model,`
- **What conflicts:** The fixer documents that the smaller model drops rollup-subsumed findings and misreads multi-weakness rows, and switches its own extraction to the larger model. The agent still uses the smaller model as the primary extractor for the same report and falls back only on transport or parse failure, not on a quietly incomplete list.
- **What actually happens:** Issues are filed from the smaller model's output. A dropped finding produces no issue, and the fixer, which harvests issues, never sees it.
- **Consequence:** Findings in the report can be lost between the scan and the fixer without any error. The same transform is run with a model the project's own prompts call unreliable.
- **Consequence level:** medium
- **Knobs involved:** `issues.haiku_model`, `issues.sonnet_model`
- **Evidence strength:** verified in source for the conflict; inferred for how often it loses findings

### Finding 27: The fixer's documented "ask before pushing" default is `true` in the skill text and `false` in the configuration file

- **Kind:** Configuration against configuration
- **Where:**
  - `vulnhunter-fix/SKILL.md:384` "`behavior.confirm_before_push`: Ask before pushing (default: true) — fork mode only"
  - `vulnhunter-fix/config.json:25` `"confirm_before_push": false,`
  - `vulnhunter-fix/SKILL.md:387` "`verification.max_retries`: Legacy synonym for `max_repair_attempts`"
  - `vulnhunter-fix/config.json:16-17` `"max_retries": 2,` `"max_repair_attempts": 3,`
- **What conflicts:** The text documents confirmation as on by default; the shipped file turns it off. Separately, `max_retries` is called a synonym of `max_repair_attempts` but carries a different value (two versus three), and the "headless" documents that supposedly read it do not exist in the repository.
- **What actually happens:** No prompt or script reads `confirm_before_push` or `max_retries` (a search of non-test files finds only the skill text and `worker_agent_common.md:63`, which hardcodes 2). The fixer's own rules (`SKILL.md:299-310`) require an approval question at each phase boundary but the push itself is not gated by the setting.
- **Consequence:** An operator who relies on the documented default expects a confirmation before pushing to a fork; the shipped value says none, and in either case the setting is not enforced by code. Retry counts of two and three coexist.
- **Consequence level:** medium
- **Knobs involved:** `behavior.confirm_before_push`, `verification.max_retries`, `verification.max_repair_attempts`
- **Evidence strength:** verified in source

### Finding 28: The verification-table truth table has overlapping rows, and the code resolves them differently from the document

- **Kind:** Prompt against code
- **Where:**
  - `vulnhunter-fix/references/verification-table-rules.md:~86-88` FULL row "yes | yes | yes | yes/n/a | yes/n/a | yes/n/a" and MITIGATION row "yes | yes | yes | yes | yes/n/a | yes/n/a"
  - `vulnhunter-fix/vulnhunter_fix/delivery.py:224-228` `return "FULL"` is tested before `return "MITIGATION"`
  - `vulnhunter-fix/vulnhunter_fix/delivery.py:112-120` "completeness_tier == FULL requires empty residual_vectors[]"
- **What conflicts:** When column 6 ("Residual risk documented?") is `yes` and all other columns are `yes`, both the FULL and MITIGATION rows match. The code checks FULL first, with no condition on columns 7 and 8 for MITIGATION, so MITIGATION is reached only when column 7 or 8 is `no`, a case the document's table does not list for MITIGATION at all. A FULL tier must also have no documented residuals, so a `yes` in column 6 contradicts FULL.
- **What actually happens:** A fix whose residual risk is documented and whose other columns are all `yes` is labelled `FULL` in the table, while a fix with a missing caller route (column 7 `no`) is labelled `MITIGATION`.
- **Consequence:** The "mechanically computed" verdict printed in the pull request can say FULL for a fix the worker classified as MITIGATION, and misdescribes why a non-full fix is non-full.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 29: The gate runner is described as running seven gates, but the anti-merge gate never has input and cannot run

- **Kind:** Dead or unreachable rule
- **Where:**
  - `vulnhunter-fix/prompts/verify.md:558` "`run-gates.py` reported `pass: true` (all seven gates)."
  - `vulnhunter-fix/scripts/run-gates.py:108-110` `anti_merge = (ctx.sidecar or {}).get("anti_merge") or {}` ... `return []  # no-op`
  - `vulnhunter-fix/scripts/run-gates.py:~218` `REQUIRED_GATES` omits `gate5_anti_merge`
  - `vulnhunter-fix/prompts/verify.md:534` `--sidecar .work/<repo>/graph_context/VULN-NNN.json`
- **What conflicts:** The skill, `verify.md` and `deliver.md` state that all seven gates must pass. The fifth gate reads an `anti_merge` block from the triage sidecar. The only place in the repository that mentions `anti_merge` outside tests is this reader; no prompt or script writes the block, and the sidecar passed in is the per-finding triage file.
- **What actually happens:** Gate 5 returns no invocations on every real run, and the runner does not list it among required gates, so the result is `pass: true` over six gates. The grouping check at plan time (`plan.md:118`) is the only place anti-merge is enforced.
- **Consequence:** The delivery-time protection against grouping unrelated findings into one pull request is not in force, while the checklist says it is.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 30: Draft versus ready pull requests are decided by two different rules, and the configuration default is ignored by both

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunter-fix/prompts/deliver.md:97-98` "Ready PR | Fully non-breaking. No caller changes, no new config ..." / "Draft PR | Non-breaking at the code level **but requires setup**"
  - `vulnhunter-fix/prompts/deliver.md:481` "WORKAROUND fixes open as **Draft**; FULL and MITIGATION open **Ready**"
  - `vulnhunter-fix/vulnhunter_fix/delivery.py:166-168` `return tier == "WORKAROUND"`
  - `vulnhunter-fix/README.md:108` "`github.pr_draft` | `true` | Open PRs as drafts"
  - `vulnhunter-fix/config.json:9` `"pr_draft": true,`
- **What conflicts:** One rule decides by whether setup is required; the other decides by completeness tier. A MITIGATION fix that needs a new environment variable is Draft by the first rule and Ready by the second. A WORKAROUND fix that needs no setup is Ready by the first and Draft by the second. The documented configuration default says all pull requests open as drafts and is overridden by both rules.
- **What actually happens:** The text does not say which rule wins. `SKILL.md:345` says "Ready PRs override" the flag.
- **Consequence:** Whether a partial fix is merged without a human gate depends on which rule the model applies; a configuration value that reviewers believe forces drafts has no effect.
- **Consequence level:** medium
- **Knobs involved:** `github.pr_draft`
- **Evidence strength:** verified in source

### Finding 31: Several fixer configuration keys are never read, and one is overridden by a hardcoded value

- **Kind:** Configuration against code
- **Where:**
  - `vulnhunter-fix/config.json:28-31` `"models": { "override": null, "default": "sonnet", "routing": {`
  - `vulnhunter-fix/SKILL.md:101` "calibrated for Opus. Sonnet and Haiku produce noticeably worse results"
  - `vulnhunter-fix/config.json:13` `"branch_prefix": "vulnfix"` and `vulnhunter-fix/scripts/setup_worktree.sh:42` `BRANCH_PREFIX="vulnfix"`
  - `vulnhunter-fix/SKILL.md:262` "Read `config.json` ... (GitHub host, branch prefix, behavior flags)."
- **What conflicts:** The configuration declares a model routing table (Opus for Critical and complex weaknesses, Sonnet for High, Haiku for Low and Medium) and a default of Sonnet, while the skill stops if the session is not Opus and never reads `models`. The branch prefix is configurable by name but hardcoded in the worktree script. A search of non-test files finds no reader of `models.*`, `ssl_verify`, `fork_visibility`, `deliver_to_fork_only`, `fallback_to_issue` or `auto_fork_on_no_access` beyond one prompt line.
- **What actually happens:** Worker model selection is whatever the orchestrating model chooses for the `"model"` field in the worker manifest; the routing table has no effect. `branch_prefix` changes nothing.
- **Consequence:** An operator who edits the routing table to save cost or force a stronger model for authentication fixes sees no change; fix quality and cost are not governed by the declared policy.
- **Consequence level:** low
- **Knobs involved:** `models.routing`, `models.default`, `git.branch_prefix`
- **Evidence strength:** verified in source

### Finding 32: Model settings declared in prompts cannot be applied by anything in the repository

- **Kind:** Dead or unreachable rule
- **Where:**
  - `vulnhunter-fix/prompts/reviewer_test.md:10` "**Model settings:** temperature=0, max_tokens=800."
  - `vulnhunter-fix/prompts/tier_judgment.md:6` "**Model settings:** temperature=0, max_tokens=800, single completion."
  - `vulnhunter-fix/prompts/agent_fix.md:5` "**Model settings:** temperature=0, fresh context"
  - `vulnhunter-fix/prompts/tier_judgment.md:61-62` "the caller retries once"
- **What conflicts:** The prompts state sampling settings, and `tier_judgment.md` says "single completion" and also describes a retry. The reviewer output includes reasoning and a repair brief that may exceed eight hundred tokens. A search of every Python, shell, JSON and TOML file finds no `temperature` or `max_tokens`; the subagents are launched through the Agent tool, which this skill describes without such parameters.
- **What actually happens:** The settings are text only; the subagents run with the host's defaults.
- **Consequence:** The reproducibility that the tier classifier and the test reviewer claim (deterministic judgments) is not provided; two runs on the same diff can disagree on tier or verdict.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source (absence of any setter); the effect on variation is inferred

### Finding 33: Two names exist for "already fixed upstream", and only one is allowed in the result file

- **Kind:** Prompt against code
- **Where:**
  - `vulnhunter-fix/prompts/verify.md:84-85` "Mark as `FIX_NOT_NEEDED`"
  - `vulnhunter-fix/prompts/plan.md` (live check) marks the same case `ALREADY_FIXED`
  - `vulnhunter-fix/references/result-schema.json:12-23` `workerStatus` enumeration contains `ALREADY_FIXED` and not `FIX_NOT_NEEDED`
  - `vulnhunter-fix/prompts/deliver.md:105` "`FIX_NOT_NEEDED` → No artifact (branch deleted, see Step 5c)."
- **What conflicts:** The status values the delivery and verification prompts act on include a name that the result schema (and the validator that gates the phase exit) does not accept.
- **What actually happens:** A result file that records `FIX_NOT_NEEDED` would fail `validate-result.py`; one that records `ALREADY_FIXED` is not handled by the delivery text, which only names `FIX_NOT_NEEDED`.
- **Consequence:** The path for findings already fixed upstream can raise a validation error or be skipped, which changes whether the branch is deleted and what the tracking issue records.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 34: The agent's continuation prompt tells the model to run phases the scan skill says to skip

- **Kind:** Prompt against code
- **Where:**
  - `vulnhunter-agent/agent/runner.py:462-464` "do not stop until every dispatched task has completed and you have advanced through Phase 2b, Phase 3, Phase 3d, and the final report."
  - `vulnhunt/SKILL.md:351-352` "If the audit ends early (zero findings after Phase 2b), skip to step 3 (Write report)."
  - `vulnhunt/SKILL.md:310-312` "Zero confirmed findings is a valid outcome."
- **What conflicts:** The session loop re-sends the continuation text whenever a result message arrives with subagents pending, and the text names Phase 3 and Phase 3d as required stages. The skill allows a clean scan to jump to the report.
- **What actually happens:** On a zero-finding scan, a continuation prompt can push the model to produce Phase 3 and Phase 3d outputs and the sweep table for nothing, or to write placeholder files to satisfy "verify each phase's output files exist".
- **Consequence:** Wasted cost on clean scans, and a risk of fabricated phase outputs in the results directory that the issues stage later reads.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source for the text; inferred for model behaviour

### Finding 35: The scan skill contains interactive instructions that a headless run cannot follow, and a pointer to a check that is not there

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/SKILL.md:225-226` "**Mandatory First Actions**: Check for prior results + install dependencies. See top of this file."
  - `vulnhunt/SKILL.md:63-64` "give the user the exact command and STOP. Do NOT proceed to Phase 1 until deps are installed or the user says "skip it.""
  - `vulnhunt/SKILL.md:229` "run `/cost` and report the result to the user."
  - `vulnhunt/phases/phase2_hunt.md:236` "Present the merged candidate list and the resolved inventory to the user"
  - `vulnhunter-agent/agent/runner.py:~86-95` "Do NOT ask for approval or confirmation. Execute immediately."
- **What conflicts:** The top of the skill contains no check for prior results (the Python launcher performs it, `runner.py:411-431`; direct invocation does not). Several steps require talking to a user, and the headless kickoff forbids it. In Bash-enabled headless runs, a failed dependency install is meant to stop and wait.
- **What actually happens:** The user-facing steps are no-ops or stall points under the agent; the prior-results guard exists only in the Python path, so a direct run relies on a fresh timestamped name.
- **Consequence:** A Bash-enabled headless scan can end after a failed install without a report; direct invocation lacks the guard that stops the skill reading its own earlier results.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 36: The authorization delegation ladder is mandatory in one place and optional in another, and the platform rollup subsumes findings that other rules say must stay separate

- **Kind:** Prompt against prompt
- **Where:**
  - `vulnhunt/phases/phase2_shared.md:358-359` "the Authorization Delegation Rule (phase2b_verify.md §8) MAY downgrade IDOR findings to Informational or Medium."
  - `vulnhunt/phases/phase2b_verify.md:186` "apply this severity ladder ONCE."
  - `vulnhunt/phases/phase2b_verify.md:236-237` rollup "Subsume CONFIRMED CWE ∈ {287, 306, 441, 639, 862, 863, 915, 1390}."
  - `vulnhunt/phases/phase2_class_nav.md:139-141` "do NOT subsume it into ... co-located IDOR/CWE-639 findings"
  - `vulnhunt/phases/phase2b_verify.md:276-279` mass assignment and insecure direct object reference "are always separate findings"
- **What conflicts:** The shared file says the ladder may be applied; Phase 2b says it must be. The class and anti-merge text say authorization and mass-assignment findings are never subsumed, while the rollup subsumes both 862 and 915. The anti-merge paragraph does carry an exception for the rollup, but the navigation file and the closing sentence of the paragraph do not.
- **What actually happens:** The rollup takes precedence in Phase 2b, since it runs once before the verdict table.
- **Consequence:** Individual authorization and mass-assignment findings are replaced by one platform row in a codebase where no handler has authentication code, reducing the number of reported findings by design but contradicting the navigation file's instruction to emit them.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 37: The fixer's phase list, mode references and branch masking disagree about what exists

- **Kind:** Dead or unreachable rule
- **Where:**
  - `vulnhunter-fix/SKILL.md:299` "(Parse → Plan → Implement → Verify → Sweep → Deliver)" versus `SKILL.md:315-345` five numbered phases with sweep inside verify
  - `vulnhunter-fix/SKILL.md:111` "Headless mode invokes the executor with a fixed Opus model under the hood"
  - `vulnhunter-fix/SKILL.md:387` "referenced by `headless/` docs"
  - `vulnhunter-fix/prompts/verify.md:110` "Fix branch: `vulnfix/VULN-NNN-short-description`" versus `vulnhunter-fix/vulnhunter_fix/delivery.py:355` `fix/code-quality-{descriptor}-{key_prefix}`
- **What conflicts:** Six phase boundaries are named for approval gates but only five phases are defined; headless mode and its documents are referred to as an existing runtime but there is no such directory in the skill. Branch examples in the verify prompt use a form the code says new branches never use (the prompt does carry a note at line 7 that it is illustrative).
- **What actually happens:** The "fork / headless" rules (three repair attempts, issue fallback) are described as a runtime that is not shipped, and the approval gate at every boundary assumes an interactive operator.
- **Consequence:** A reader or automation cannot tell which rules apply to which mode; branch names shown to users differ from those created.
- **Consequence level:** low
- **Knobs involved:** `verification.max_repair_attempts`
- **Evidence strength:** verified in source

### Finding 38: Three documentation statements in the agent contradict the code or each other

- **Kind:** Documentation against behaviour
- **Where:**
  - `vulnhunter-agent/agent/config.example.toml:140-141` "destination_repo must exist before the agent runs — auto-creation is not supported."
  - `vulnhunter-agent/agent/publish.py:66-67` "Make sure the destination repo exists, creating it private if not."
  - `vulnhunter-agent/agent/verify_refs.py:6` "the orchestrator runs this Haiku pre-flight" and `verify_refs.py:142-143` "Verify uses the same model as the scan (config.anthropic.model)"
  - `vulnhunter-agent/scan_manifest.schema.json:5` "agent exit codes 0, 1, 3, 4, or 5" and `scan_manifest.schema.json:29` "0=success, 1=no findings, 2=publish failed, 3=partial issue post, 4=agent crash"
- **What conflicts:** The example says auto-creation is unsupported while the code creates a private repository; the module description names Haiku while the code uses the scan model with no fallback; the schema's top description lists exit code 5, which does not exist, and omits code 2.
- **What actually happens:** The code does what the code says: a missing destination repository is created, the scan model runs the reference extraction, and the exit codes are 0 to 4.
- **Consequence:** None observable for detection. An operator may be surprised that a repository is created in their account, and may expect a cheaper model than the one that is billed for pre-flight.
- **Consequence level:** low
- **Knobs involved:** `publish.enabled`, `publish.destination_repo`, `anthropic.model`
- **Evidence strength:** verified in source

---

## Candidates not confirmed

- Test-quality rubric intro versus verdict matrix (`vulnhunter-fix/references/test-quality-rubric.md:6-8` "WEAK at best and typically WRONG" versus the matrix where only the first, fourth and fifth rules give WRONG): the intro is hedged with "typically", so it is emphasis rather than a different rule.
- Scan skill "do NOT switch to sink-driven hunting" (`phase2_shared.md:107`) versus the sink-driven agent: the sentence is addressed to the class-group trace agents, not the orchestrator.
- Principle 1 ("do not second-guess the gates") versus Gate 3 elimination: the two can be read as consistent (gates are the filter); no case was found where both cannot be followed.
- Phase 1 file glob list omitting Ruby, PHP and C# while input examples mention Rails: the text says to glob each extension "present", so the list is a starting point.
- Severity-mask safe-list entries "criticism" and "critique" that the rule itself says never match the stem: the document states this openly, so it is a harmless redundancy rather than a conflict.
- Fix-verify templates using "—" for a gate that did not run, versus the four-value gate enumeration: the symbol appears only in rendered comment tables, not in the JSON.
- `phase2b_verify.md` "do not require reading library source" versus Phase 1's "do not credit known-library shortcuts": the text deliberately assigns the shortcut to Phase 2b section 8.
- Readme "Model" field and the model tag the agent supplies (`opus48_1m`): ambiguous wording but no observable difference was established.
- Judge prompt in the harness having no tool flags: no contradicting statement exists to compare against.

Not checked: the fixer's `implement.md` and most worker prompts beyond the sections quoted, the `evals/` directory, the graph package, `comment_rules.md` against `phase0_preflight.md` rule by rule, and the knob registries `vulnhunter.knobs.yaml` against the source; the pseudocode notes were used only as leads and each was re-read in the source.
