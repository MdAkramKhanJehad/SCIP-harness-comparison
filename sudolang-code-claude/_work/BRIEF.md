# Brief for a batch writer: VVAH in SudoLang

You render one batch of the VVAH harness source as SudoLang pseudocode. Several writers work in parallel on separate batches, so stay inside your batch's files and output folders.

## Paths

- Harness source (read-only, never modify): `/home/spl/akram/harness-comparison/visa-vulnerability-agentic-harness/`. Package `vvaharness` version 1.5.1.
- Output root: `/home/spl/akram/harness-comparison/sudolang-code-claude/`. Write only:
  - your `.sudo` / `.sudo.md` files under `vvah/<same relative path as the source>`;
  - your four batch records under `_work/<batch>/` (see "Records").
- SudoLang baseline (read before writing): the specification `/scratch/mkhan04/tmp/claude-261169/-home-spl-akram-update-cap-one-harness-VulnHunter/21512d31-6460-4dde-a2e9-e398bfab60b3/scratchpad/sudolang/sudolang.sudo.md`, the examples folder beside it (`examples/`, `syntaxes/syntax-test.sudo`). Read at least the spec, `syntax-test.sudo`, `robot.sudo`, `riteway.sudo`, `autodux.sudo`, `teach.sudo`.
- **The contract you must follow:** `/home/spl/akram/harness-comparison/sudolang-code-claude/CONVENTIONS.md`. Read it fully.
- **The worked example to imitate:** `/home/spl/akram/harness-comparison/sudolang-code-claude/vvah/vvaharness/orchestrator/scan.sudo` (the pipeline spine, already written; do not edit it). It shows the header, `// src:` pointers, `:executor=` modifiers, `knob(...)`, `require ... =>`, `match`, `constraint OnEveryExit`, and the markers.
- Do not read or copy from `/home/spl/akram/harness-comparison/comparison-results/`. This rendering must come from the source.

## Shared vocabulary (use these exact names; do not invent synonyms)

| Name | Meaning |
|---|---|
| `:executor=code\|model\|mixed` | function modifier: who carries out the body |
| `callModel({ role, route, system, prompt, tools, limits, output })` | one model invocation made by the code. `role` is the configured model role (for example `deepdive`, `verify`); `route` is the backend (`cli`, `sdk`, `openai`, `deepagents`) when the code fixes it, otherwise `resolve_model(knob("models.<role>")).via`; `tools` are the tools offered; `limits` are turn, token, time or budget caps the code passes; `output` is the expected shape or schema |
| `runConcurrently(items, workers=n, fn):order=completion\|input` | parallel execution the source performs (thread pool, asyncio gather); `order` is the order results are consumed |
| `knob("dotted.key", default=v)` | a configuration read, default as at that read site (mirrors source helper `vvaharness.util.config.knob`) |
| `constraint OnEveryExit { ... }` | cleanup on every exit (source `try/finally`, context managers that matter) |
| `// src: path:a-b` / `// prompt-src: path:a-b` | traceability pointers; path relative to the harness repository root |
| `// unresolved: ...; missing evidence: ...` | cannot be determined from the material |
| `// preserved: ...` | contradictory or surprising source behaviour, kept as is |
| `// external: ...` | call outside the rendered scope (third-party library, `vendor/`, `vvaharness/exploit_verification/`) |
| `// abstracted: ...` | lines condensed, with what and why it is safe |

Source identifiers (function names, classes, enumeration values, configuration keys, stage ids `s0`...`s11`) are kept exactly as in the source. If you need any other new name (a new interface name for a prompt, a helper verb), add it to your vocabulary record. Prefer the source's own term.

## How to render

1. For each source file in your batch, read it fully. Then write the `.sudo` file at the mirrored path with the header from CONVENTIONS section 3.
2. Keep the call hierarchy: a public entry function first, then the functions it calls in call order, then helpers. Calls to functions in other files use the source module and function name (for example `s4.session.investigate_unit(...)`), so a reader can follow them to the other file.
3. Keep everything listed in CONVENTIONS section 10 under "Keep". Thresholds, caps, retry counts, filters, gates, ordering, parallelism and model instructions must appear with their exact values and source lines.
4. Prompts: render each prompt as an interface named after the source constant or function, for example `S4_SYSTEM_PROMPT { ... }`. Put the model-facing instructions in `Constraints { ... }`, keep template slots as `$variable`, quote decisive rules exactly, and give `// prompt-src:`. Where a prompt is assembled conditionally (fragments added when a setting is on), render the condition with `if`.
5. Never turn a prompt instruction into a code step. If the code checks the model's output afterwards, write that check as `require` in the consuming code function, with its own `// src:`.
6. Tools: list tools *offered* in `callModel({ tools: [...] })`. Write code-enforced restrictions (allow lists, deny lists, permission rules, budgets) as `require`. Never write that a tool is called unless the code calls it.
7. If behaviour depends on something you cannot see (a third-party library, a file outside your batch whose behaviour you would have to guess), write `// unresolved:` or `// external:`. You may open files outside your batch to understand a call, but do not render them.
8. Keep contradictions and oddities as they are, with `// preserved:`.
9. Skip files with nothing to represent (re-export-only `__init__.py`, `ruff.toml`), but list them in coverage as `skipped` with the reason. A `__init__.py` with real logic is rendered.
10. Write in full words in comments and prose. No abbreviations for ordinary words (write "false positive", not "FP"; "for example", not "e.g.").

## Records (write all four under `_work/<batch>/`)

1. `coverage.tsv`: header `source_path	source_lines	output_path	status	notes`; one row per source file in your batch; `status` is `full`, `partial` (say what is missing in notes), or `skipped` (say why).
2. `vocabulary.md`: every new name you introduced that is not a source identifier and not in the shared table above. For each, in this exact shape:
   ```
   ### <term>
   - Definition:
   - Why needed:
   - Kind: general harness concept | tool-specific identifier
   - Original source term or wording:
   - Source references: path:line, ...
   - Used in: output file paths
   ```
   Write "none" if you introduced nothing.
3. `unresolved.md`: every `// unresolved:` you wrote, as `output_path — what — missing evidence`, plus anything in the source you could not read.
4. `examples.md`: two or three source-to-representation pairs suitable for manual checking: a short source excerpt (at most 25 lines, with path and lines) and the corresponding SudoLang excerpt. Pick ones that carry a gate, threshold, retry or model instruction.

Also note in `unresolved.md` anything that seems to need a grammar change to SudoLang (not a new identifier). Do not invent new grammar in the `.sudo` files.

## Self-check before you finish

- Every source file in your batch has a coverage row.
- Every substantive block has a `// src:` with a line range that you verified.
- Every `require`/`warn` is a check that the code performs; every `Constraints` item is something asked of a model or a declared rule.
- No prompt wording inside quotation marks is paraphrased.
- Every `knob(...)` default matches its read site.

## Reply

Under 150 words: files written, coverage counts (full, partial, skipped), number of vocabulary entries, number of unresolved items, and anything you could not finish. Never call a partial batch complete.
