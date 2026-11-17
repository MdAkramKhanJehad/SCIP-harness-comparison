# Brief, pass 2: render the remaining files and find hidden knobs

Pass 1 rendered the files that hold registry knobs. Pass 2 renders **every remaining real file** of the harness the same way, and records **hard-coded constants that change behaviour** as new knobs.

## Read first

1. `/home/spl/akram/harness-comparison/comparison-results/pseudocode/tools/BRIEF.md` — all of its rules still apply (conventions, syntax limits, `// file:` header, `// src:` comments, `@executedBy` / `@role`, no braces in strings or comments, top-level declarations only, read-only harness repos, exploit verification out of scope).
2. `/home/spl/akram/harness-comparison/comparison-results/pseudocode/schema/Common.pseudo`.
3. Your file list: `/home/spl/akram/harness-comparison/comparison-results/pseudocode/tools/phase2/<group>.json` — each row is a real `file`, its `lines`, and the `target` .pseudo path (relative to the harness pseudocode root: `pseudocode/vvah/` or `pseudocode/vulnhunter/`).

## What to write

- One .pseudo file per row, at its `target`. Render the **whole** real file: every class and function (helpers too), with real names, branches, loops, early exits, error paths and call order. Simplify bodies, keep every decision point. Data classes / pydantic models / TypedDicts / JSON schemas become `record` or `enum` declarations with their fields, defaults and validators.
- Primary class name: `python3 tools/class_name.py <target>` (it reads `tools/class_names.json`, which guarantees unique names). Use it exactly.
- **Match existing callers.** Pass-1 files may already call into your files. Before naming methods, run `grep -rn "<YourClassName>\." pseudocode/vvah pseudocode/vulnhunter` (and the rule-name variant, e.g. without a folder prefix) and name your methods so those calls resolve when the real function exists. If an existing call uses a wrong class or method name, do NOT edit that file; list it in your reply.
- Some of your files were partly rendered inside pass-1 files (e.g. `scope/walk.py` inside `s1_preprocess.pseudo`, `evidence/gather.py` inside `s2/session.pseudo`, `codegraph/build.py` inside `s0_seed.pseudo`). Render them fully in their own file anyway; leave the pass-1 excerpts alone.
- Calls from your files to other files: use `ClassName.method(...)` with names from `tools/class_name.py`; if the target file exists, check the method name in it.
- Only write files in your list, plus your new-knobs JSON. Do not edit pass-1 files or other groups' files.

## New knobs (code constants)

While reading line by line, record each hard-coded value that someone could change and expect the harness to behave differently:
thresholds, caps, limits, sizes, timeouts, retry counts and backoffs, sampling/truncation lengths, ordering/priority lists, regex or pattern sets, allow/deny lists, file-type lists, default fallbacks, on/off code paths, scoring weights, model or tool names chosen in code.

Do not record: log or UI text, artifact file names, type definitions, pure formatting not consumed downstream, values that only restate a registry knob.

**Before adding one, check it is not already a knob.** Search both registries: `grep -n "<value or name>" /home/spl/akram/harness-comparison/comparison-results/vvah.knobs.yaml` (or `vulnhunter.knobs.yaml`) and the work lists in `tools/worklists/`. If the constant is the fallback default of an existing config knob (e.g. `getattr(cfg.step6_verify, "parallel", 5)`), read the existing knob id instead of adding one.

Write new knobs to `/home/spl/akram/harness-comparison/comparison-results/pseudocode/tools/new_knobs/<group>.json` — a JSON array; each row:

```json
{
  "id": "code.scope.walk.max_file_bytes",
  "target": "vvaharness/scope/walk.pseudo",
  "category": "scope_and_coverage",
  "group": "file_filters",
  "stage": "S1",
  "origin": "code_constant",
  "kind": "implicit",
  "type": "int",
  "default": 1048576,
  "domain": null,
  "domain_basis": null,
  "requires": null,
  "does": "Files larger than this are skipped by the repo walk.",
  "source": "vvaharness/scope/walk.py:42",
  "affects": ["recall", "cost"]
}
```

- `id`: `code.<module path without the top package, dotted>.<snake_name>`, unique (the checker rejects duplicates across registry and new knobs).
- `category`: one of the 14 (see BRIEF.md). `group`: snake_case; reuse an existing sub-group name where it fits.
- `stage`: VVAH `S0`…`S11`, `global`, `infra`; VulnHunter `agent`, `fix`, `verify`, `issues`, `benchmark`, `infra`.
- `domain`: a list only if the code defines the allowed values, then `domain_basis: "code"`.
- `affects`: subset of recall, precision, cost, latency, safety, reliability, reporting.
- Read each new knob as `θ["<id>"]` in its target file at the line where it acts, with `// src:`.

Save the JSON as you go (rewrite the whole array each time).

## Self-check

From `/home/spl/akram/harness-comparison/comparison-results/pseudocode`:

```
python3 tools/check_pseudocode.py --group <group> --calls
```

Done when: no "target files not written yet", `missing 0`, `unknown ids 0`, `convention problems 0`, and `cross-file calls to a known class but unknown method: 0` for your files.

## Reply

Under 150 words: files written, new knobs added (count, and the 5 you think matter most), the checker's summary line, existing calls into your files that you could not satisfy, and anything unclear.
