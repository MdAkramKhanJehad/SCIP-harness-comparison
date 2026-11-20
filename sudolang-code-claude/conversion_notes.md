# Conversion notes: VVAH in SudoLang

This file records how the representation in this folder was produced, what it covers, the choices made in producing it, and what remains unsettled. It makes no claim that the representation is correct. Agreement between the model-written batches, or between a model and a mechanical check, does not prove fidelity. What was checked, and how, is stated under "Review" below.

## 1. Versions

| Item | Version |
|---|---|
| SudoLang | specification `sudolang.sudo.md` v2.0, repository `github.com/paralleldrive/sudolang`, commit `dcef61e` (2025-12-23) |
| Harness | `visa-vulnerability-agentic-harness/`, package `vvaharness` 1.5.1 (`pyproject.toml:21`) |
| Harness snapshot | the harness has no git history of its own here. It is a folder in the `harness-comparison` repository, added in commit `e86fd4f` (2026-11-16) and unchanged since (checked with `git log -- visa-vulnerability-agentic-harness`). The repository head at the time of conversion was `fe88503`. |

## 2. Specification and examples reviewed

- `sudolang.sudo.md` (all 417 lines). It was re-read in the final session from a fresh clone of the same commit, because the copy used in the first session lived in a scratch directory on another machine.
- `syntaxes/syntax-test.sudo` and `examples/`: `ai-friend`, `ai-rpg.sudo.md`, `autodux`, `codebot`, `experience-levels`, `fibonacci`, `green-tara`, `improve-anything`, `learn-sudolang`, `life-coach`, `music-recommender`, `newsbot`, `productmanager`, `prompt-crafter`, `reflective-thought-composition` (and its `.readme.md` and `-mini`), `riteway`, `robot`, `studybot`, `symbolic-cot`, `teach`, `therapist`, `todo`, `vector-search`, `whispers`. Every batch writer was required to read at least the specification, `syntax-test.sudo`, `robot.sudo`, `riteway.sudo`, `autodux.sudo` and `teach.sudo`. `CONVENTIONS.md` section 1 lists, for every construct used, where it is defined.
- Inaccessible: none. `syntaxes/sudolang.tmLanguage.json` is an editor grammar. It was not used as a language definition.
- Facts about the specification that matter for this rendering: `return` and `try`/`catch` appear in the examples (`autodux`, `teach`, `riteway`) but are not described in the specification text. The lint section prohibits `new`, `extends`, `extend` and `inherit` and warns on `class`.

## 3. Instructions and revisions

The task as given (summarized; the full text is in the session that produced this folder):

1. Read SudoLang and its examples, then the harness. Report anything inaccessible. Invent no syntax or behaviour.
2. Use SudoLang as the baseline. Separate its constructs from harness vocabulary and from language extensions. Propose an extension only when it is needed, and record it separately.
3. Represent the harness while keeping its flow hierarchy, ordering, branching, calls and parallelism, and its directory organization. Keep gates, thresholds, loops, retries, model calls and instructions, and tool availability. Separate code-enforced behaviour from prompt-requested behaviour. Mark what is unresolved. Keep contradictions.
4. Keep `vocabulary_extensions.md`, and `language_extension_proposals.md` if needed.
5. Make every block traceable to source lines, review the result, and keep this file.
6. Keep the scope to representation: no flaw analysis, redesign or invented test results. Work in batches with a coverage record, and never present partial work as complete.

Revisions during the work:

- **Session 1** (another login to the same server): wrote `CONVENTIONS.md`, the spine `orchestrator/scan.sudo` as the worked example, `INDEX.sudo.md`, the batch brief `_work/BRIEF.md` and `tools/check_rendering.py`. It then ran ten batch writers (A-J), which wrote 278 output files. The session ended before any batch wrote its records. In that session `vvaharness/exploit_verification/` was excluded from scope. Nothing in the record says the user approved that exclusion.
- **Session 2** (this one) was asked to double-check and finish. Findings at the start:
  - 180 source files had no output;
  - none of the batch coverage, vocabulary, unresolved or example records existed;
  - spot checks found invented content in pass-1 files (for example, a "duplicated license header" in `s4/batching.sudo` that does not exist) and line ranges that drifted by 5 to 80 lines.
  
  So pass-1 output was treated as unverified. A second pass (`_work/BRIEF_PASS2.md`) gave each of eleven area batches (P1-P11) three jobs: verify and fix every existing file against source, render the missing files, and write the four records.
- **Scope revision:** the user decided to include `vvaharness/exploit_verification/` (batches P10 and P11). `CONVENTIONS.md`, `scan.sudo` and `INDEX.sudo.md` were updated to match.
- **Syntax revision:** some pass-2 drafts used `??`, `?.` and `extends`, which are not SudoLang. All were rewritten in natural language, or as `// source: subclass of X` comments, rather than proposed as extensions.
- **Follow-up passes:** files that a batch had checked only for pointer ranges (22 in the pipeline area, then 13 across three other areas) were given a full content check by separate reviewers. They are marked `full` only after that check.

## 4. Files covered and not covered

`coverage.tsv` has one row per file under `vvaharness/` and `inputs/`, 526 in all. It is generated by `python3 tools/check_rendering.py --write-coverage` from the batch records `_work/*/coverage.tsv`.

| Status | Count | Meaning |
|---|---|---|
| full | 456 | rendered, and checked against the source in pass 2 (or written in pass 2) |
| partial | 0 | |
| skipped | 70 | nothing to represent: `__init__.py` files that only re-export names or hold a license header or docstring, `ruff.toml` lint files, the `py.typed` marker. Each row gives its reason. |
| not covered | 0 | |

Harness material deliberately **not** represented, because it is not harness behaviour:

- `tests/`, `scripts/`, `docs/` (395 files together with `vendor/`). They describe or test the harness. Where a source comment points to them, the rendering says so.
- `vendor/`: third-party code. Calls into it are marked `// external:`.
- Top-level project files (`README.md`, `AGENTS.md`, `CLAUDE.md`, `CHANGELOG.md`, licences, governance, `pyproject.toml`). Only the package version was taken from `pyproject.toml`.
- Third-party libraries the harness imports (`claude_agent_sdk`, `deepagents`, LangGraph, `httpx`, `openai` and others). Behaviour that depends on them is marked `// external:` (129 places).

## 5. Abstraction choices and rationale

The full contract is in `CONVENTIONS.md`. In short:

- **One output per source file, at the mirrored path.** This keeps the source organization and makes every block findable by its source path.
- **Who acts is always stated.** Every function carries `:executor=code|model|mixed`. `require`/`warn` are used only for checks the Python performs. `Constraints { }` holds only what a prompt asks of a model. A tool listed in `callModel({ tools })` is offered, never assumed to be called. This is the distinction the task asked for between enforced and requested behaviour.
- **Prompts** are interfaces named after the source constant or builder. Decisive rules are quoted exactly, and conditional fragments are rendered with `if`. Long reference tables inside prompts may be summarized with `// abstracted:` and a range.
- **Settings** are written `knob("key", default=...)`, with the default of each read site. Where read sites disagree, both are kept and marked `// preserved:`. The five shipped profiles are rendered as follows: `default.yaml` in full, and the other four as differences from it, computed mechanically. Each profile file says so in its preamble.
- **Data files** (playbook, policy, hints, payload templates, the rules knowledge base) are rendered as `Options { }` or interface blocks that keep every value a gate or threshold reads. Large display-only tables (CWE names, extension-to-language maps, the full regular-expression texts in `report/redact.py`) are condensed with `// abstracted:`.
- **Condensed** (190 `// abstracted:` markers): logging, console output, metrics bookkeeping, formatting helpers, type coercion, and data tables that change no decision. An `// abstracted:` marker never hides a branch, threshold, gate, retry, tool restriction or model instruction.
- **Not condensed, although verbose:** the guardrail and budget logic in `backends/harness/deepagents/`, the exploit-verification safety gates, the policy gate for remediation patches, and the redaction applied before a prompt or report leaves the harness. These decide what a model sees or what reaches the target, so they are kept at statement level.

## 6. How the harness flow hierarchy maps to the representation

`vvah/INDEX.sudo.md` is the map. It has four levels, each tied to the source:

1. **Entry points:** `__main__`, `cli/`, `orchestrator/entry`, `orchestrator/batch`, `api`, `sdk/`, standalone `remediation_agent/remediate`, `validation/cli`.
2. **Pipeline for one repository:** `orchestrator/scan.sudo` `scan_repo`, with stages in source order. A preparation step for exploit verification and an optional Stage 1 auto-exclude overlay come first, then s0 to s11. Each stage is checkpointed. On resume, a stage is reused only if the stage it depends on was reused. `--stop-after` stop points and exit codes are kept. A Mermaid chart shows the order. It adds no ordering that the source lacks.
3. **Stages and their components:** each stage file calls its own `prompts`, `session` and `outcomes` modules by module and function name (for example `s4.session.investigate_unit(...)`), so the call hierarchy can be followed file to file. Stage 6 has two branches in the same stage: `s6_verify`, or, when `ctx.ev_collection` is set, `exploit_verification/verify/router`. The router still delegates findings it cannot verify live, and all findings on its fallback paths, to `s6_verify` (`router.py` `_static`).
4. **Shared layers:** `backends/llm` (route selection and the four model routes), `backends/harness` (session options, tool permissions, budgets, guards), `models/` (data passed between stages), `config/`, `util/`.

Parallelism is rendered only where the source runs it (`runConcurrently`, with the worker count and the order results are consumed). No synchronization was added beyond the locks, joins and shared counters the source has.

## 7. Unresolved behaviour and missing material

Material that was inaccessible: none. Every file in scope was readable.

`// unresolved:` markers that remain (each names its missing evidence in place):

One marker remains:

- `vvah/vvaharness/orchestrator/store/_schema.sudo`: `_DDL_V2` and `_DDL_V3` do not create `ix_runs_updated`, so a migrated database has that index only if the version 1 schema created it. Missing evidence: the version 1 DDL, which is not in the source.

Six markers written by batch writers who could not see code outside their batch were settled in a final pass, against the source, with verified pointers (`_work/P1-pipeline/unresolved.md`, `_work/P3-backends-llm/unresolved.md`):

1. `backends/llm/deepagents.sudo`, how `max_turns` becomes a recursion limit: the streaming route uses `(max_turns or 50) + 900` LangGraph supersteps, and the one-shot route uses `+5` (`backends/harness/deepagents/limits.py:19-30`, `options/streaming.py:141`). This value was also checked by hand.
2. `pipeline/stages/replay.sudo`, which routes can resume a session: only `cli` and `deepagents`. Any other route raises `SessionNotResumableError`, which leads to a replay.
3. `pipeline/stages/s4/prompts.sudo`, read-only shell commands: the harness adds no command filter, so read-only is a prompt instruction only. Commands run through the deepagents library's local shell backend (`// external:`).
4. `pipeline/stages/s4/prompts.sudo`, a single-unit `{"outcomes": [...]}` reply: it does not parse as a single outcome. Validation fails, and the single-unit path makes one repair re-ask.
5. `pipeline/stages/s4/session.sudo`, a null graph handle: the builder returns only the reader tools. Graph tool names and their budget stay registered with no tools behind them.
6. `pipeline/stages/s4/session.sudo`, `resume_or_replay`: it always tries a resume first. A model refusal is re-raised, and any other error calls `replay()`.

Further limits, not unresolved behaviour:

- The fallback used when `sdk.cache_markers` is absent from a profile: the key is not in `_STEP_DEFAULTS`, so the effective value is whatever the reader in the deepagents backend falls back to (see `config/profiles/sdk.sudo.md`).
- What a model does with an offered tool, a skill (`SKILL.md`) or a probe script (`probe.sh`): no harness code runs the probe scripts, so whether they run is the model's decision. This is stated in each `probe.sudo` header and is unknowable from the source by design.
- Behaviour of third-party libraries: marked `// external:`.

## 8. Review: what was checked and what was not

Checked:

- **Mechanically, on all 457 output files** (`tools/check_rendering.py`, 0 problems at completion):
  - every one of 3,479 `// src:` and `// prompt-src:` pointers names an existing file and a range inside it;
  - every output file names an existing source file;
  - every one of the 526 in-scope source files has exactly one coverage row, and each `full` row's output file exists.
- **Mechanically, a declaration check:** for 1,730 pointers placed directly above a named function or interface, the source range must contain that name. 18 ranges that started inside a body were anchored to the definition line. The 10 remaining flags were inspected by hand. They are either multi-range pointers whose definition lies in the second range, or grouping interfaces (`Options`, `State`, `Constants`) recorded in the vocabulary.
- **Mechanically, for vocabulary:** every interface, function and named-constraint name in the outputs is either present in the harness source or recorded in `vocabulary_extensions.md` (0 unrecorded).
- **Mechanically, for syntax:** no `??`, `?.`, `extends` (as syntax), `class` or `new` remains in the code parts of the outputs.
- **By reviewers, file by file against source:**
  - every pass-1 file was compared with its source in pass 2 (branches, thresholds, knob defaults, quoted wording, tool lists, code versus model, nothing invented, nothing decisive omitted);
  - files a batch could check only partly were re-reviewed by a separate reviewer;
  - fixes are listed in each row's `notes` in `coverage.tsv`.
- **By hand in the final session** (spot checks, not exhaustive):
  - `s4/batching.sudo` against `s4/batching.py`;
  - the Stage 1 and Stage 3 "model role" comments in `scan.sudo` (corrected: those stages make no model call);
  - the Stage 6 branch and router delegation in `scan.py:756-787` and `router.py:294-312`;
  - the duplicated `http://` scheme in out-of-band payload templates (`executor/oob.py:124` and `payloads/templates/*.yaml`).

Not verified:

- The reviewers are language models. Their file-by-file checks were not independently repeated, except for the spot checks above. A file marked `full` means "reviewed once against source", not "proven faithful".
- Whether each `// preserved:` note reports a real oddity, as opposed to a reviewer's misreading, was checked only for the spot checks listed above.
- Quoted prompt text was copied by script in some files (validation personas and rules, payload templates, the rules knowledge base). Elsewhere it was copied by hand by the writer. No mechanical comparison of every quoted string against source was run.
- Nothing was executed. No harness run, test or model call was made to confirm behaviour, and no test results are reported.

## 9. Grammar decisions

No change to SudoLang grammar was adopted, so `language_extension_proposals.md` was not created. Every harness concept was expressed with existing constructs plus identifiers:

| Need | Considered | Decision |
|---|---|---|
| Parallel execution | a `parallel { }` block | the identifier `runConcurrently(items, workers, fn):order=...` (a function with a modifier) |
| Code-enforced check with a non-throwing reaction | a new keyword | `require <condition> => <reaction>`, which combines the specification's `require` with its semantic-match arrow |
| Cleanup on every exit | `finally` | the named constraint `constraint OnEveryExit { }` |
| Absent-key fallback | `??` (used in some drafts) | natural language, for example "x, or, when absent, y" |
| Exception subtype | `extends` (prohibited by the SudoLang lint) | an empty interface plus `// source: subclass of X` |
| Regular expressions | a literal form | `/.../` written as ordinary values inside assignments, which SudoLang does not define but reads as values |

Two batches noted that a native way to say "error type B is a kind of A" would remove a comment. That is recorded here as an observation, not a proposal.

## 10. Source-to-representation examples for manual checking

Each batch record `_work/P1-pipeline/examples.md` ... `_work/P11-ev-exec/examples.md` holds two or three pairs, each with a short source excerpt and line range beside the SudoLang excerpt, chosen because they carry a gate, threshold, retry or model instruction. Two more pairs follow, checked in the final session.

**A. Batching with a size cap and a LARGE-unit rule.** Source `vvaharness/pipeline/stages/s4/batching.py:34-48`:

```python
def plan_batches(units: list[InvestigationUnit], size: int) -> list[list[InvestigationUnit]]:
    if size <= 1:
        return [[u] for u in units]
    ordered = sorted(units, key=lambda u: (u.risk_rank, u.id))
    # LARGE units run alone: a shared session re-sends every member's code every turn.
    large = [[u] for u in ordered if u.size == UnitSize.LARGE]
    pool = [u for u in ordered if u.size != UnitSize.LARGE]
    batches: list[list[InvestigationUnit]] = []
    while pool:
        batch = [pool.pop(0)]
        while pool and len(batch) < size:
            batch.append(pool.pop(pool.index(_best_partner(batch, pool))))
        batches.append(batch)
    return batches + large
```

Representation `vvah/vvaharness/pipeline/stages/s4/batching.sudo`:

```
// src: vvaharness/pipeline/stages/s4/batching.py:34-48
fn plan_batches(units, size):executor=code {
  if (size <= 1) return each unit as its own batch   // input order kept (run already sorted by risk_rank)
  ordered = units sorted by (risk_rank, id)
  // LARGE units run alone: a shared session re-sends every member's code every turn
  large = each unit in ordered with size == UnitSize.LARGE, as its own batch
  pool = units in ordered with size != UnitSize.LARGE
  batches = []
  while (pool is not empty) {
    batch = [take the first unit from pool]
    while (pool is not empty && length(batch) < size) {
      batch += take _best_partner(batch, pool) from pool
    }
    batches += batch
  }
  return batches + large   // LARGE singletons come after all shared batches
}
```

**B. The Stage 6 branch (a conditional transition between components).** Source `vvaharness/orchestrator/scan.py:766-774`:

```python
                    if getattr(ctx, "ev_collection", None):
                        # EV armed: live-verifiable findings to the confirm-agent, rest stay static
                        from vvaharness.exploit_verification.verify import (
                            router as ev_router,
                        )
                        verified, dropped = ev_router.run(findings, ctx, cfg,
                                                          run_id=run_id)
                    else:
                        verified, dropped = s6_verify.run(findings, ctx, cfg, run_id=run_id)
```

Representation: `vvah/vvaharness/orchestrator/scan.sudo` (the Stage 6 block, which calls `exploit_verification.verify.router.run`, else `s6_verify.run`). The router's own fallbacks are in `vvah/vvaharness/exploit_verification/verify/router.sudo` (`fn _static`, and `if (col == null) return _static(...)`).

## 11. Working records

`_work/` holds the briefs (`BRIEF.md` for pass 1, `BRIEF_PASS2.md` for pass 2), the spine's coverage rows, and, for each pass-2 batch P1-P11, `coverage.tsv`, `vocabulary.md`, `unresolved.md` and `examples.md`. The batch folders of pass 1 (A-J) were empty and have been removed.
