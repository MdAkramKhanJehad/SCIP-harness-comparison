# Brief: exhaustive prompt-knob extraction

## Goal

We are building a registry of every "knob" in two vulnerability-detection harnesses so that a later project can vary them one at a time and measure the effect (causal inference, then planning). Config-file knobs are already complete. Your job is the knobs that live in **prompt text**: read the files assigned to you line by line and record every one.

Both harness repos are read-only. Do not modify anything under `/home/spl/akram/harness-comparison/VulnHunter` or `/home/spl/akram/harness-comparison/visa-vulnerability-agentic-harness`. Write only the one JSON output file named in your task.

## What counts as a prompt knob

A piece of prompt text that someone could change to a different value and expect the scanner's behaviour to change. Record one knob per independently variable rule:

- A number, threshold, cap or budget ("at most 6", "≤20 words", "two levels deep", "confidence 0-10").
- An enumerated set the model must choose from or work through (verdicts, severity tiers, class groups, audit lists, exclusion lists, required output fields).
- An on/off rule or mandatory step ("MANDATORY", "MUST", "Do NOT", "always", "never", "before X do Y").
- An ordering or procedure whose order matters.
- A stance, prior or persona ("assume each finding is wrong", "~50% are false positives", "You are a ...").
- A decision rule or tie-break ("if any agent says CANDIDATE, the input is a CANDIDATE", "when unsure, do not exclude").
- An exemption or exception to another rule.
- An evidence requirement ("must cite file:line").
- An output-format constraint that shapes downstream behaviour (required table, required fields, length limits).
- A conditional prompt variant (text that is included only when a flag is set; say which flag in `requires`).

Do not record: pure explanation of why a rule exists, worked examples, sample tables, code snippets used as illustration, headings with no rule, or text that only restates a rule you already recorded from the same file. If the same rule appears in two files, record it once per file only if the wording gives a different value or scope; otherwise record the first and mention the other location in `does`.

Be exhaustive. A file of 300 lines of dense instructions typically yields 30-80 knobs. Prefer splitting a paragraph into its separate rules over one vague row. Do not skip a rule because it seems minor.

## Avoid duplicates of what already exists

The current registries are:
- `/home/spl/akram/harness-comparison/comparison-results/vulnhunter.knobs.yaml`
- `/home/spl/akram/harness-comparison/comparison-results/vvah.knobs.yaml`

Read the one for your harness first (it is long; the `categories:` section is what matters). If a rule is already there with `origin: prompt_text` and the same source file, do not repeat it unless your row is a finer-grained part of it. Finer-grained rows are wanted.

## Output: one JSON file

A JSON array of objects, each with exactly these keys:

```json
{
  "id": "p.phase2_shared.sanitizer_sink_match_check",
  "category": "gating_and_thresholds",
  "group": "hard_gates",
  "stage": "phase2",
  "does": "Before recording SAFE on the basis of sanitization, check that the sanitizer covers the sink's dangerous characters.",
  "default": true,
  "type": "bool",
  "domain": null,
  "requires": null,
  "affects": ["recall", "precision"],
  "source": "vulnhunt/phases/phase2_shared.md:55",
  "quote": "**Sanitizer-sink match check:** Before recording SAFE based on sanitization,"
}
```

Field rules:

- `id`: `p.<file stem>.<short_snake_name>`, unique within your file. For Python files use the module stem (e.g. `p.s6_prompts.exclusion_rule_a`; for `pipeline/stages/s6/prompts.py` use `s6_prompts`, for `s4/outcomes.py` use `s4_outcomes`). For skills use `p.skill_<skill-name>.<name>`.
- `category`: one of
  `model_routing`, `budget_and_termination`, `decomposition_and_parallelism`, `scope_and_coverage`, `context_supply`, `tool_access`, `detection_method`, `gating_and_thresholds`, `verification_depth`, `dedup_and_merge`, `ranking_and_reporting`, `remediation`, `runtime_and_infra`, `evaluation`.
  Meanings:
  - model_routing: which model answers, how much it reasons, persona/role lines.
  - budget_and_termination: turn, call, token, word, time limits; retries; stop conditions.
  - decomposition_and_parallelism: how work is split into units and run concurrently.
  - scope_and_coverage: what code is in or out of scope; coverage requirements and ceilings.
  - context_supply: what material the model is given or told to read or not read.
  - tool_access: which tools to use or avoid, and how.
  - detection_method: search strategy, tracing procedure, mandatory checks while hunting.
  - gating_and_thresholds: rules a candidate must pass; verdict sets; severity rules; evidence requirements.
  - verification_depth: second-opinion passes, exploit testing, sweeps, fix validation.
  - dedup_and_merge: when findings are merged or kept separate.
  - ranking_and_reporting: ranking, chains, report and output format.
  - remediation: anything about producing, limiting or gating a fix.
  - runtime_and_infra: safety against hostile input, secrets handling, paths, plumbing.
  - evaluation: benchmark and judging.
- `group`: a snake_case sub-group. Reuse an existing one from the registry when it fits (e.g. `hard_gates`, `exemptions`, `severity_rules`, `verdict_scheme`, `evidence_gates`, `confidence`, `adversarial_review`, `exploit_testing`, `sweep`, `fix_validation`, `search_strategy`, `mandatory_checks`, `planning`, `exclusions`, `coverage_ceilings`, `seed_detection`, `work_units`, `concurrency`, `batching`, `merge_rules`, `dedup_rules`, `output_files`, `channels`, `chains`, `issue_filing`, `injected_knowledge`, `source_delivery`, `orchestrator_context`, `tool_allowlist`, `shell`, `turn_and_call_caps`, `output_tokens`, `wall_clock`, `retries_and_recovery`, `policy`, `limits`, `enablement`, `hostile_repo_hardening`, `persona`). Create a new one only when none fits.
- `stage`: the phase or stage the prompt belongs to (VulnHunter: `phase1`, `phase2`, `phase2 INJ`, `phase2b`, `phase3a`, `phase3b`, `phase3c`, `phase3d`, `phase4`, `orchestrator`, `fix`, `verify`, `issues`, `benchmark`; VVAH: `S1-auto`, `S2`, `S4`, `S6`, `S6-EV`, `S7`, `S8`, `S10`, `S11`, `global`).
- `does`: one plain sentence saying what the rule makes the model do. Your own words, not a copy of the quote.
- `default`: the value the prompt currently sets. A number, `true` for a rule that is simply present, a short string, or a list for enumerated sets. Keep strings under ~150 characters.
- `type`: `bool`, `int`, `float`, `str`, `enum` or `list`.
- `domain`: `null`, unless the prompt itself states the allowed values (then a list).
- `requires`: `null`, or a short condition under which the text applies (e.g. "class group is NAV", "Bash available", "graph tools present").
- `affects`: subset of `recall`, `precision`, `cost`, `latency`, `safety`, `reliability`, `reporting`. Your best judgement; may be empty.
- `source`: path relative to the harness root (`VulnHunter/` or `visa-vulnerability-agentic-harness/` stripped), then `:` and the 1-based line number where the rule starts.
- `quote`: an exact, verbatim substring (20-120 characters) of that source line, copied character for character. It will be checked by script against the file, so do not paraphrase, do not join two lines, and do not include a leading line number. If the line is long, quote a distinctive part of it.

Get line numbers from the Read tool's line numbering or `grep -n`. Before you finish, run a self-check: for every row, confirm the quote occurs on the cited line (a short Python script over your JSON is the reliable way) and fix any that do not. Also confirm the file parses as JSON and ids are unique.

## What to return

Write the JSON file, then reply with: the output path, the number of knobs per source file, and a short list of anything you were unsure how to classify. Keep the reply under 200 words; the knobs themselves belong in the file, not the reply.
