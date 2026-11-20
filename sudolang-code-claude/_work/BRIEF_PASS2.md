# Brief for pass 2: review, complete, and record one area

Pass 1 (batches A-J) wrote 278 `.sudo` files but was interrupted before it wrote any batch records, and it left 180 source files unrendered. Spot checks found that some pass-1 files have line ranges that drift by 5-80 lines from the real source, and one file (`s4/batching.sudo`) described a duplicated license header that does not exist. So pass-1 output is **unverified**. Your job is to make your area correct and complete.

Read first, in this order:
1. `/home/spl/akram/harness-comparison/sudolang-code-claude/_work/BRIEF.md`: the original batch brief. Everything in it still applies (shared vocabulary, how to render, record formats, self-check). One correction: the SudoLang baseline is now at `/scratch/mkhan04/tmp/claude-261169/-home-spl-akram-harness-comparison/dfdf2fac-a6e8-4bc9-b42a-98883ca406c4/scratchpad/sudolang/` (same commit `dcef61e`): read `sudolang.sudo.md` and at least `syntaxes/syntax-test.sudo`, `examples/robot.sudo`, `examples/riteway.sudo`, `examples/autodux.sudo`, `examples/teach.sudo`.
2. `/home/spl/akram/harness-comparison/sudolang-code-claude/CONVENTIONS.md`: the contract.
3. `/home/spl/akram/harness-comparison/sudolang-code-claude/vvah/vvaharness/orchestrator/scan.sudo`: the worked example (do not edit it).

## Your three jobs, for the area named in your prompt

### Job 1: verify and fix every existing output file in your area

For each existing `.sudo` / `.sudo.md` under your area, open it beside its source and check:
- every `// src:` and `// prompt-src:` range actually covers the code or prompt it labels (start at the `def`/`class`/constant line, end at its last line). Fix drifted ranges using `grep -n` / `cat -n` on the source; never estimate a range.
- nothing is invented: every branch, threshold, retry cap, knob default, tool list, and `// preserved:` claim is in the source. Remove or correct anything that is not.
- nothing decisive is omitted (CONVENTIONS section 10 "Keep"). Add omitted gates, thresholds, retries, model instructions, tool restrictions, ordering, or parallelism.
- prompt wording inside quotation marks is copied exactly.
- `require`/`warn` are only code-performed checks; `Constraints` only model-facing requests.
Edit the file in place. Keep the existing style.

### Job 2: render the source files in your area that have no output

Mapping: `x.py` → `x.sudo`; `x.sh` → `x.sudo`; Markdown/YAML/JSON/CSV/other data → `x.sudo.md` (for example `config/profiles/default.yaml` → `config/profiles/default.sudo.md`, `inputs/remediation_policy.yaml` → `vvah/inputs/remediation_policy.sudo.md`). Paths stay relative to the harness root under `vvah/`.
- `__init__.py` that only re-exports: skip, coverage `skipped` with reason "re-exports only". An `__init__.py` with logic (functions, registries, constants that act as thresholds, import-time side effects): render.
- `ruff.toml`, `py.typed`: skip, reason "lint configuration" / "typing marker".
- Data/config files (profiles, playbooks, policies, hints, example inputs): render as a `.sudo.md` with a `Source:` header and an `Options { ... }` or interface block per section that lists the decisive values (thresholds, toggles, model roles, tool lists, deny rules, prompt text). `// src:` ranges per section. Long repetitive tables may be `// abstracted:` with counts and the range, but every value that a gate or threshold reads must be kept.
- Shell probes: render the commands' decisions (what is searched, filters, limits) as functions with `:executor=code`.
- Markdown prompt/rule files given to a model (for example `validation/prompts/system.md`, subagent `.md`, `claude_config/rules/*.md`, skill `SKILL.md`): render as prompt interfaces with `Constraints { ... }`, quote decisive rules exactly, `// prompt-src:`.

### Job 3: write the four records under `_work/<your batch id>/`

`coverage.tsv`, `vocabulary.md`, `unresolved.md`, `examples.md`, exactly as `_work/BRIEF.md` "Records" says. Additions:
- `coverage.tsv` must have **one row for every source file in your area**, existing outputs included. Status `full` only for files you verified in Job 1 or wrote in Job 2. Add a `notes` value `verified-pass2` or `written-pass2`, plus what you fixed (for example "fixed 4 drifted ranges").
- `vocabulary.md` must cover new names **in every file in your area**, including pass-1 files (harvest them: interface names for prompts that are not source constants, helper verbs, any non-source identifier). Not the shared names in `_work/BRIEF.md`.
- Do not add rows for `vvaharness/orchestrator/scan.py`, `vvaharness/py.typed`, `vvaharness/backends/ruff.toml` (already in `_work/spine/coverage.tsv`).

## Mechanical check

When you finish, run `python3 /home/spl/akram/harness-comparison/sudolang-code-claude/tools/check_rendering.py | grep -F '<your area path>'` and fix every problem it lists for your area (pointer ranges, missing outputs). Other areas' problems are not yours.

## Limits

- Write only inside your area under `vvah/` and in `_work/<your batch id>/`. Other agents are editing other areas at the same time.
- Never modify the harness source, `CONVENTIONS.md`, `scan.sudo`, `INDEX.sudo.md`, or `tools/`.
- Do not read `/home/spl/akram/harness-comparison/comparison-results/`, `old-comparison-results/`, `old-qualitative-analysis/`, or `sudolang-code-chatgpt/`. The rendering must come from the source.
- No flaw analysis, no redesign, no invented test results.

## Reply (under 200 words)

Files verified (and how many needed fixes, with the kinds of fixes), files written, coverage counts (full, partial, skipped), vocabulary entries, unresolved items, checker result for your area, anything not finished. Never call a partial area complete.
