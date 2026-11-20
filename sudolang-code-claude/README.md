# VVAH represented in SudoLang

This folder represents the Visa Vulnerability Agentic Harness (VVAH, package `vvaharness` 1.5.1) as SudoLang pseudocode, for systematic analysis of its design decisions and behaviour. It is a faithful representation, not a redesign, and it contains no flaw analysis.

## Contents

| Path | What it is |
|---|---|
| `README.md` | This file: the SudoLang baseline and the representation conventions in brief |
| `CONVENTIONS.md` | The full representation contract (constructs, files, markers, abstraction rules) |
| `vvah/` | The pseudocode, mirroring the harness source tree file for file |
| `vvah/INDEX.sudo.md` | The workflow hierarchy (pipeline, stages, components) with links to files |
| `vocabulary_extensions.md` | Every identifier introduced beyond the SudoLang baseline |
| `conversion_notes.md` | Versions, material reviewed, instructions, coverage, abstraction choices, unresolved behaviour, examples for manual checking |
| `coverage.tsv` | One row per harness source file (526): output file and status. 456 full, 70 skipped, 0 partial, 0 not covered |
| `tools/check_rendering.py` | Mechanical check of source pointers and coverage |
| `_work/` | Working records from the batch conversion (briefs for pass 1 and pass 2, per-batch coverage, vocabulary, unresolved items, examples) |

## The SudoLang baseline

SudoLang (specification v2.0, repository `paralleldrive/sudolang`, commit `dcef61e`) is a pseudocode language for language models. It mixes Markdown prose with light program structure. Its core constructs are:
- interfaces with state, `Constraints` and `/commands`;
- natural-language constraints, which the model is asked to keep satisfied;
- `require` and `warn`, which signal violations;
- functions, declared with or without bodies, with call-time modifiers (`fn():key=value`);
- `if`/`else` (also usable as an expression), `for each`, `while`, `loop` and `match` with destructuring;
- the pipe `|>`, template strings, `Options` and Mermaid diagrams.

The specification calls functions the model fills in "referential omnipotence" and treats comments as meaningful. The style guide asks for interfaces and composition, not `class`, `new` or `extends`. `return` and `try`/`catch` appear in the repository's examples but are not described in the specification text.

## Representation conventions in brief

- **Same tree as the source.** `vvaharness/pipeline/stages/s4_deepdive.py` becomes `vvah/vvaharness/pipeline/stages/s4_deepdive.sudo`. Markdown and YAML sources become `.sudo.md` files.
- **Traceable.** Every file names its source. Every substantive block carries `// src: path:first-last`, and every prompt carries `// prompt-src:`.
- **Who carries out each step.** Every function has `:executor=code`, `model` or `mixed`. `require`/`warn` mark only checks the code performs. `Constraints { ... }` hold only what a prompt asks of a model. Model calls are written `callModel({ ... })`, listing the tools offered. An offered tool is never written as a step that happens.
- **Settings.** Settings are written `knob("dotted.key", default=...)`, with the default that applies at that read site.
- **Concurrency.** Parallelism the source performs is written `runConcurrently(items, workers=n, fn):order=...`. No synchronization is added beyond what the source does.
- **Markers.** Marker comments flag the limits of the rendering. `// unresolved:` means the material cannot settle a behaviour. `// preserved:` marks a contradiction or oddity kept on purpose. `// external:` marks a call outside the rendered scope. `// abstracted:` marks condensed lines that contain no decision.
- **Grammar.** These are all ordinary identifiers and comments inside standard SudoLang constructs. They do not change the language. See `vocabulary_extensions.md`. No grammar change was needed, so there is no `language_extension_proposals.md`. `conversion_notes.md` section 9 records the options considered.
- **Scope.** All of `vvaharness/` (including `exploit_verification/`) and `inputs/`. Tests, scripts, docs and `vendor/` are not represented (see `conversion_notes.md` section 4).

## Where to start reading

1. `vvah/INDEX.sudo.md`, for the shape of the workflow.
2. `vvah/vvaharness/orchestrator/scan.sudo`, the pipeline for one repository (Stage 0 to Stage 11, checkpoints, resume, stop points, exit codes).
3. The stage files linked from the index, then the prompts and backends they call.
