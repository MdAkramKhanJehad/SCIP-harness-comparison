# Brief: write harness pseudocode with every knob in place

## Goal

We are rewriting two vulnerability-detection harnesses as Java-style pseudocode (not compilable) so a later project can analyse them: which knob acts where, who enforces it (code or model), and how the pieces call each other. The pseudocode must **zoom in like the real code**: one .pseudo file per real module or prompt file, classes and methods that follow the real structure, down to individual rules. Every knob in your work list must be read, as `θ["<id>"]`, at the place where it acts.

Harness repos (read-only; never modify anything in them):
- VVAH: `/home/spl/akram/harness-comparison/visa-vulnerability-agentic-harness/`
- VulnHunter: `/home/spl/akram/harness-comparison/VulnHunter/`

Pseudocode roots (write only inside your assigned files/folders):
- VVAH: `/home/spl/akram/harness-comparison/comparison-results/pseudocode/vvah/`
- VulnHunter: `/home/spl/akram/harness-comparison/comparison-results/pseudocode/vulnhunter/`

A .pseudo file's path under the root mirrors its real file's path under the repo, with the extension replaced: `vvaharness/pipeline/stages/s4/prompts.py` → `vvah/vvaharness/pipeline/stages/s4/prompts.pseudo`; `vulnhunt/phases/phase2_shared.md` → `vulnhunter/vulnhunt/phases/phase2_shared.pseudo`.

## Read first

1. `/home/spl/akram/harness-comparison/comparison-results/pseudocode/schema/Common.pseudo` — the conventions and shared types. Follow them exactly; a parser depends on them.
2. Your work list: `/home/spl/akram/harness-comparison/comparison-results/pseudocode/tools/worklists/<group>.json`. Each row is a knob: `id`, `target` (the .pseudo file it must appear in, relative to the harness pseudocode root), `does`, `default`, `type`, `origin`, `requires`, `source` (real file:line), `quote`.
3. The real source files in your area (code and prompts). Read them fully; the structure comes from them, not from the work list.

## Rules

**Coverage.** Every id in your work list must appear as `θ["<id>"]` in its `target` file, exactly spelled, at the point where it takes effect (a branch, a bound, a prompt rule, a gate). Several reads of one knob are fine. Never write `θ["..."]` with an id that is not in a work list (the checker flags unknown ids); for a value with no knob, write the literal with a comment.

**Structure follows the real code.**
- Python modules: mirror the real classes and functions (same names in CamelCase/camelCase, same call order, same branches and loops, same early exits). Simplify bodies, but keep every decision point. Where a function is long, split into the real helper functions it calls.
- Prompt files (.md, prompt strings in .py, SKILL.md): write a class `@executedBy(MODEL) @role(prompt)` whose methods build the prompt sections in order (`Prompt p = new Prompt(); p.must(θ["..."]); ...`), one method per section/heading. When the prompt tells the model to carry out a procedure (loops over inputs, numbered steps, decisions, verdicts), also write that procedure as ordinary control flow in methods marked `@executedBy(MODEL)` — this is how the prompt-only harness logic becomes code-shaped. Conditional prompt text is an `if` on the flag that includes it.
- Enumerated sets (verdicts, severities, class groups) become `enum`s or `List.of(...)` values read from the knob.
- Mixed logic (model produces, code checks) is `@executedBy(MIXED)` or two methods (one MODEL, one CODE).
- Add `// src: <real path>:<line>` at the end of each line that renders a specific real line (every knob line should have one).

**Names.** The primary class of each file is named by `python3 tools/class_name.py <path relative to the harness pseudocode root>` (run it from `/home/spl/akram/harness-comparison/comparison-results/pseudocode`). A stage/phase/prompt file's main entry method is `run(...)`. Call other files as `<ClassName>.<method>(...)` so calls can be traced across files. Extra classes in a file get any descriptive name.

**Syntax limits (the parser needs these).**
- First line of every file: `// file: <real path>[, <real path>]`, then 1–3 `//` lines saying what the file is.
- Top-level declarations only (`class`, `enum`, `record`, `interface`); no nested classes. Methods at class level, each declared on one line ending in `{`. Annotations (`@executedBy(...)`, `@role(...)`, `@stage("...")`, `@src("...")`) on the line(s) directly above a class or method.
- `{` and `}` only as block delimiters: never inside strings or comments. Write quotes from prompts without braces (replace `{x}` with `<x>`).
- `@role` values: pipeline, stage, step, prompt, rule_set, agent, tool, skill, config, backend, io, evaluation, stub, types.
- Executors: CODE, MODEL, MIXED.

**Exploit verification (VVAH).** Not in scope. Only a stub file holding its config knobs (`exploit_verification/stub.pseudo`, `@role(stub)`), with a one-line method per stage name (classify, map, payloads, attacker, oracle, judge) that just reads the relevant config knobs. Do not read or render the exploit-verification prompts, payloads or attack logic.

**Do not invent behaviour.** If the real code/prompt is unclear, write what it says and add `// unclear: ...`. Do not add knobs.

## Example (style only)

```
// file: vvaharness/pipeline/stages/s6_verify.py
// S6: adversarial verification of candidate findings, in parallel batches.

@executedBy(CODE) @role(stage) @stage("S6")
class S6Verify {

    List<Verdict> run(List<Candidate> cands, Theta θ) {
        List<List<Candidate>> batches = S6Batching.group(cands, θ["step6_verify.batch_size"]);          // src: vvaharness/pipeline/stages/s6_verify.py:210
        List<Verdict> out = Runtime.parallel(θ["step6_verify.parallel"], batches, b -> verifyBatch(b, θ)); // src: vvaharness/pipeline/stages/s6_verify.py:233
        return keep(out, θ);
    }

    List<Verdict> keep(List<Verdict> vs, Theta θ) {
        return vs.filter(v -> v.label == TRUE_POSITIVE && v.confidence >= θ["step6_verify.min_confidence"]); // src: vvaharness/pipeline/stages/s6_verify.py:301
    }
}

@executedBy(MODEL) @role(prompt) @stage("S6")
class S6Prompts {
    Prompt system(Theta θ) {
        Prompt p = new Prompt();
        p.persona(θ["p.s6_prompts.persona_skeptical_reviewer"]);     // src: vvaharness/pipeline/stages/s6/prompts.py:14
        p.choose(θ["p.s6_prompts.verdict_set"]);                     // src: vvaharness/pipeline/stages/s6/prompts.py:40
        if (θ["step6_verify.cvss"]) p.format(θ["p.s6_prompts.cvss_vector_required"]); // src: vvaharness/pipeline/stages/s6/prompts.py:77
        return p;
    }
}
```
(The ids above are illustrations, not real ids.)

## Self-check before you finish

From `/home/spl/akram/harness-comparison/comparison-results/pseudocode` run:

```
python3 tools/check_pseudocode.py --group <your group>
```

Fix until it reports `missing 0`, `unknown ids 0`, `convention problems 0`. "OUTSIDE TARGET" lines mean a knob is read only in a different file than its target: move or add the read in the target file.

Write files as you go (one Write per file, or several for a big file) so work is not lost if you are interrupted.

## Reply

Under 150 words: files written (count), the checker's summary line, and anything you were unsure how to render.
