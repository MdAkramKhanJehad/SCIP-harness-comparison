# Common harness pseudocode format

This is an analysis representation shared by every harness. Write algorithms in
Java-style pseudocode, regardless of the original language. Preserve behavior
while removing syntax, framework boilerplate and purely cosmetic output. Do not
translate source tokens mechanically or introduce a second source-mirror dialect.

The syntax/types contract is [Common.pseudo](schema/Common.pseudo). The machine-readable
structure and knob contract is [knobspace.schema.json](schema/knobspace.schema.json).
Both apply to all harnesses, including future additions.

## What precision means

Preserve each meaningful decision, loop, early return, retry, fallback, ordering,
concurrency boundary, input/output contract, error path and side effect. Include
helpers when they affect those behaviors. Collapse logging and display formatting
to named operations, retaining their conditions and any downstream-consumed shape.
Show cleanup with `finally`/`with` and async waits explicitly. Preserve zero/null
semantics, inclusive/exclusive bounds, stable sorting and first/last-match rules.

Represent the behavior present in the source, including bugs and contradictions.
Use `// unclear:` for ambiguity and explain known source quirks. Do not silently
repair a source bug in the pseudocode, invent a missing check, strengthen an error
handler, or convert a prompt requirement into code enforcement.

An algorithm can be precise without being executable or retaining every source
line. Source pointers identify the source routine or definition; they do not
constitute a semantic-equivalence proof. The validators below check structure,
references and coverage, not model compliance or algorithmic equivalence.

## File and component rules

Use `<harness-folder>/<source-relative-path>.pseudo`; replace the source suffix.
Keep the source tree recognizable for navigation. A namespace-only source file can
be an annotated empty class with an explanation of exports. It needs no invented
`run()` method. A source function can be a method on a module-named class, and a
source data class can become a record. Flatten nested classes into uniquely named
top-level classes. Keep nested-function scope/captured inputs explicit.

Each file starts with `// file: <source-relative-path>` and a short purpose comment.
Every class/record/enum has `@executedBy` and `@role`. A routine may use
`@src("path:line")` for its source definition; put `// src: path:line` on knob
reads for the actual source definition/enforcement site. Do not invent exact
statement-line correspondences when summarizing several statements.

Declare methods on one line ending in an opening brace. Use braces only for
blocks, not inside prose strings/comments. Register primary class names in
`tools/class_names.json`; keep class names unique within each harness. If two
harnesses reuse the same relative path, select its naming table with
`python3 tools/class_name.py --harness <folder> <path>`. Invoke
other rendered files as `ClassName.method(...)` using the declared target method.
Use constructors for records. Do not invent static factories to disguise missing
implementations. Standard library operations and explicitly described external
dependencies may remain abstract; internal behavioral helpers should be rendered.

Use the existing `@role` vocabulary: pipeline, stage, step, prompt, rule_set,
agent, tool, skill, config, backend, io, evaluation, stub, types. Preserve the
harness's own stage IDs in `@stage`; roles and knob categories provide the common
comparison vocabulary.

## Executor and prompt rules

- `CODE`: deterministic program logic enforces the step.
- `MODEL`: the model is instructed to follow it. No enforcement guarantee.
- `MIXED`: explicitly describe the model part and the host-code gate around it.

Build prompts with `Prompt.must/forbid/step/checklist/threshold/evidence/format`.
When prose specifies an algorithm, also express its decisions/loops as a
`MODEL` procedure. Keep model sessions explicit as `Runtime.agent`,
`Runtime.subagent` or `Runtime.llm`. A prompt's word "mandatory" never changes its
executor to `CODE`.

## Knob rules

Read each registered knob as `θ["id"]` where it affects behavior. Use one stable
ID across all readers of the same control. Record origin accurately: a code
constant is an intervention requiring a source edit, not an existing config
switch. A prompt constraint is a prompt-text knob, not a deterministic gate.

Record behavior-changing constants: limits, thresholds, retries, timeouts,
sampling/truncation policies, ranking weights, pattern sets and allow/deny lists.
Reuse existing IDs rather than duplicating defaults of real config knobs. Keep
independent code and prompt copies distinct when their enforcement can diverge.
Do not promote unused constants, labels, log text, artifact names or pure type
definitions to effective behavioral controls. Mark inert settings as such.

New constant rows go in `tools/new_knobs/<harness-token>_<group>.json` with id,
target, category, group, stage, origin, kind, type, exact default, source, does
and affects. Every row must have a real reader in its target. Existing registry
knobs use `tools/worklists/<harness-token>_<group>.json` to assign targets.
Domains are authoritative only when code defines them; observed shipped values
are not automatically legal tuning ranges. Explain `affects` as hypotheses.

## Add a future harness

1. Add a row to `harnesses.json`: unique key, folder, name, repository path,
   registry YAML filename, output JSON filename, version/profiles (or null), and
   a unique worklist token. Repo paths are relative to this directory. Set
   `source_globs` to the source files whose file coverage must be checked.
2. Put its registry YAML beside `comparison.md` with `commit`, `about` and
   `categories`, following the same category/group/knob structure as existing
   registries. Add target worklists and primary class names.
3. Render its components using this document and Common.pseudo. State explicit
   exclusions and external boundaries. Exploit verification remains excluded for
   the present comparison; do not copy its prompts/attack implementation.
4. Run the shared tools below. Their harness lists and paths come from the
   catalog; adding a harness does not require a renderer or checker fork.

Run from this folder; absolute script paths also work from other directories:

```
python3 tools/check_pseudocode.py --harness <key> --calls --strict
python3 tools/check_src.py
python3 tools/check_coverage.py --harness <key>
python3 tools/build_knobspace.py
python3 tools/export_configspace.py <folder>/<name>.knobs.json
```

The JSON and ConfigSpace files are derived outputs. Regenerate them after changes;
do not treat successful schema validation as a fidelity audit. Inspect any
remaining unresolved calls and source ambiguities before claiming completeness.
