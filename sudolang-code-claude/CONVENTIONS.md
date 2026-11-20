# Representation conventions for the VVAH SudoLang rendering

This document is the contract every generated `.sudo` file follows. It separates three things and never mixes them:

1. **SudoLang constructs**: syntax taken from the SudoLang specification (`sudolang.sudo.md`, v2.0) or demonstrated in the repository's examples (commit `dcef61e`).
2. **Harness vocabulary**: identifiers and comment markers introduced *inside* those constructs. They are ordinary user-defined names. They do not change the SudoLang language. Every one is recorded in `vocabulary_extensions.md`.
3. **Language extension proposals**: grammar changes. None are used in the representation (see `conversion_notes.md`, section "Grammar decisions").

## 1. SudoLang constructs used, with where each is defined

| Construct | Form used here | Defined in |
|---|---|---|
| Markdown preamble, headings, lists | `# Title` then prose | spec "Markdown"; every example |
| Comments, which count as meaning | `// ...`, `/* ... */` | spec "Markdown" ("Comments are meaningful"); `syntaxes/syntax-test.sudo` "Comments" |
| Interface | `Name { field; field: default; ... }`, `interface` optional | spec "Interfaces"; `syntax-test.sudo` |
| Typed field, union of values | `mode: "light" \| "dark"`, `id: String` | `syntax-test.sudo` "Interfaces" |
| State block | `State { ... }` | spec "Constraints" (ChatBot); `todo.sudo` |
| Constraints | `Constraints { ... }`, `constraint: ...`, `constraint Name { ... }` | spec "Constraints" |
| Requirements | `require ...`, `warn ...`, `throw` | spec "Requirements" |
| Inferred function declaration | `fn name;` / `function name(args);` | spec "Functions" |
| Function with body | `name(args) { ... }` (keyword optional) | spec "Functions"; `syntax-test.sudo` |
| Function modifiers | `fn():key=value`; at call time `f():key=value` | spec "Modifiers"; `syntax-test.sudo` "Function Modifiers" |
| Variables, compound assignment | `x = 0`, `x += 1` | spec "Variables & Assignments" |
| Template strings | `"text $var"`, `"${ expr }"` | spec "Template strings" |
| Conditional, also as an expression | `if (c) { ... } else { ... }`; `v = if (c) a else b` | spec "Conditional Expressions" |
| Logical and math operators | `&&`, `\|\|`, `!`, `xor`, `==`, `>=`, `union`, `intersection` | spec "Logical operators", "Math operators" |
| For each | `for each x, action;` and block form `for each x { ... }` | spec "Natural Foreach loop"; `ai-rpg.sudo.md`, `teach.sudo` |
| While, loop | `while (c) { ... }`, `loop { ... }` | spec "While loop", "Infinite loops" |
| Pattern matching | `match (v) { case ... => ...; default => ... }` | spec "Pattern matching"; `robot.sudo` |
| Destructuring | `{ a, b } = obj`, `[a, b] = list` | spec "Destructuring" |
| Pipe | `a \|> f \|> g` | spec "Pipe operator" |
| Range | `1..3` | spec "range" |
| Return | `return x` | examples `autodux.sudo` (`testCases`), `teach.sudo` (`getInput`) |
| Try and catch | `try f(); catch error => ...` | example `riteway.sudo` (`alwaysThrows`), not described in the spec text |
| emit | `emit({ ... })` | spec "Constraints" (MinimumSalary) |
| Options | `Options { name: value }` | spec "Options" |
| Mermaid diagram | fenced `mermaid` block | spec "Mermaid Diagrams" |
| Arrow function | `x => x + 1` | spec "Pipe operator"; `fibonacci.sudo` |

Constructs the style guide discourages and that are therefore **not** used: `class`, `new`, `extends`, `inherit` (spec "SudoLang Linting").

## 2. Files and organization

- One output file per source file, at the same relative path under `vvah/`, with the extension replaced: `vvaharness/pipeline/stages/s4_deepdive.py` becomes `vvah/vvaharness/pipeline/stages/s4_deepdive.sudo`. Markdown and YAML sources (skills, prompt files, profiles) become `<name>.sudo.md` beside the same path, for example `vvah/vvaharness/skills/injection/SKILL.sudo.md`.
- A source file with nothing to represent (only re-exports, an empty `__init__.py`, a lint configuration) gets no output file. It is listed in `coverage.tsv` as `skipped` with the reason.
- `vvah/INDEX.sudo.md` shows the flow hierarchy (pipeline, stages, components) and links each node to its file.

## 3. File header

Every file starts with a Markdown preamble:

```
# <source module path>

<one or two sentences: what this module does in the workflow>

Source: `vvaharness/.../file.py` (lines 1-527)
Executor: code | model | mixed   // whole-module summary
Called from: `<caller file>` <function>   // where it sits in the hierarchy
```

## 4. Traceability

- Each substantive block (interface, function, prompt, `match`, loop) is immediately preceded by `// src: <path>:<first>-<last>`. The path is relative to the harness repository root (`visa-vulnerability-agentic-harness/`).
- A prompt has its own `// prompt-src: <path>:<first>-<last>` and keeps decisive wording in quotation marks. Wording quoted from a prompt is copied exactly. Paraphrase is never placed inside quotation marks.

## 5. Who carries out each step (code versus model)

This is the distinction that matters most for later analysis. It is expressed in three ways, all with standard constructs:

1. **Function modifier `:executor=`** on every function declaration: `code` (plain Python), `model` (the body is a model's work, steered only by instructions), or `mixed` (code builds the call and checks the result, the model does the reasoning).
2. **`require` / `warn`** are used only for checks the Python code actually performs. `require` means the code raises or refuses. `warn` means the code logs and continues. When the code's reaction to a failed requirement is something other than raising (for example it returns an error string or skips an item), the reaction follows an arrow: `require <condition> => <reaction>`. This form combines the spec's `require` with the semantic-match arrow used in `vector-search.sudo` (`(require: code interpreter is available in the current context) => explain()`) and in the spec's pattern matching.
3. **`Constraints { ... }`** inside a prompt interface hold only what is *asked of the model*. A constraint is never evidence that the behaviour happens. When the code later checks the model's output, that check is written separately as `require` in the consuming code-executed function.

A model call is written with the vocabulary function `callModel({ ... })` (defined in `vocabulary_extensions.md`), listing role, route, prompt interfaces, tools offered, turn or budget limits, and the expected output shape. Tools listed in `tools:` are *offered*. Whether the model invokes them is the model's decision and is never written as a step.

## 6. Settings (knobs)

- A configuration read is written `knob("step4.parallel", default=12)`. This mirrors the source helper `vvaharness.util.config.knob` and the attribute reads `getattr(cfg.step4, "parallel", 12)`. The default shown is the default *at that read site*. Shipped profile values are listed in the profile files under `vvah/vvaharness/config/profiles/`.
- Where the source reads the same setting with different defaults at different sites, each site keeps its own default, and the difference is marked with `// preserved: ...`.
- Constants in code that act as thresholds are written as named assignments with their source line, for example `guardrailGate = max(3, parallel)  // src: ...:63`.

## 7. Concurrency, shared state, termination

- SudoLang has no parallel construct. Parallel execution is written with the vocabulary function `runConcurrently(items, workers=n, fn)`. Its result order is stated by modifier: `:order=completion` (Python `as_completed`) or `:order=input` (Python `map` or index order). Only synchronization that the source performs is written (a lock, a join, a shared counter). Nothing is added.
- Retries and loops are written with `while` or `for each` and carry their exact termination conditions and caps.
- Cleanup that the source runs on every exit (`try ... finally`) is written as a named constraint, `constraint OnEveryExit { ... }`, in the function that owns it.

## 8. Markers for uncertainty and fidelity

All are ordinary comments:

- `// unresolved: <what is unknown>; missing evidence: <what would settle it>`: behaviour that cannot be determined from available material.
- `// preserved: <short description>`: source behaviour that looks contradictory, inconsistent or surprising, kept as it is rather than corrected.
- `// external: <library or module>`: a call into code outside the represented scope (third-party library, `vendor/`, live network targets). The exploit verification package was excluded in pass 1 and is rendered since pass 2.
- `// abstracted: <what was condensed and why it is safe>`: a place where several source lines are summarized. Never used to hide a branch, threshold, gate, retry or model instruction.

## 9. Naming

- Source identifiers (functions, classes, enumeration values, step identifiers such as `s4`, configuration keys) are kept exactly as written in the source, in `snake_case` or `CamelCase` as found, so they can be searched in the source.
- New names are introduced only for the vocabulary in `vocabulary_extensions.md`. A new name is never used for a concept that already has a source name.
- Stage names use the source labels: `s0` ... `s11`, with the console title as given in `orchestrator/scan.py` (for example "Step 4 — Deep-dive").

## 10. Abstraction level

- Keep: ordering, every branch condition, filters, gates, thresholds and cutoffs, retries and their caps, termination conditions, model calls and the instructions given in them, tool lists and tool restrictions, parallelism and shared state, checkpoint and resume conditions, and error paths that change what is reported.
- Condense (with `// abstracted:`): logging, console output, metrics bookkeeping, formatting helpers, type coercion, unless they change a decision or what reaches the report.
- Prompts: render the *instructions* as `Constraints` in a prompt interface, keep the input slots as template variables, and quote decisive rules exactly. Long reference material inside a prompt (tables, lists of examples) may be summarized with `// abstracted:` and its line range.
