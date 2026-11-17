# Brief, pass 3: close the function-level gaps

Passes 1 and 2 rendered every file that holds knobs, but many large Python files were rendered as a short summary: their functions were never written out. `tools/check_functions.py` measures this: it lists every function and class of a source file that has no matching name in the pseudocode. Your job is to render those functions, completely and faithfully, and to render the few source files that have no pseudocode file at all.

## Read first (all still apply)

1. `/home/spl/akram/harness-comparison/comparison-results/pseudocode/FORMAT.md` — the common format and fidelity contract. Represent the behaviour in the source, including bugs; do not repair or invent.
2. `tools/BRIEF.md` and `tools/BRIEF2.md` — conventions, syntax limits (`// file:` header, `// src:` pointers, `@executedBy`, `@role`, no braces in strings or comments, top-level declarations only), what counts as a new code-constant knob, new-knob row format. Harness repos are read-only. Exploit verification stays out of scope.
3. `schema/Common.pseudo`.
4. Your work list: `tools/phase2/<group>.json`. Each row has the real `file`, its `lines`, `missing_functions` (count) and the `target` .pseudo path (relative to `pseudocode/vvah/` or `pseudocode/vulnhunter/`).

## What to do, per source file in your list

1. List what is missing: `python3 tools/check_functions.py --only <source path>` (run from `pseudocode/`). It prints each unnamed function with its source line number.
2. Read the real source file completely, then add every missing function to the existing target .pseudo file: a method of its primary class (name from `python3 tools/class_name.py <target>`), or a record or enum for data classes. Keep the real names (camelCase, no leading underscore) so the checker finds them. Where the file defines several top-level classes, give each its own top-level class in the .pseudo file. Flatten nested classes and nested functions (make captured inputs explicit parameters).
3. Render each function with all its decision points: branches, loops, early exits, retries, fallbacks, error paths, ordering, concurrency boundaries, input and output contracts, side effects. Summarise only logging and display formatting. If a function is very long, split it as the source does. Do not drop what existing methods in the file already contain; extend them where they omit decision points of the source function they claim to render.
4. Do not remove or rename any existing `θ["..."]` read, class or method: other files call them. Do not edit files outside your list, except to fix a wrong call name inside a file in your list.
5. Where the source file has no .pseudo file (`missing_functions` is 0 and the target does not exist), create it with the full mirror of the source, following FORMAT.md. Source files that only re-export names get an annotated empty class.

## Calls

- Pass-1 and pass-2 files already call into your classes, sometimes with wrong method names. `tools/unresolved_calls.json` lists them as `[harness, caller component, "Class.method", file that defines Class]`. For every entry whose defining file is one of your targets, make a method with that name exist when a real source function does the job (it is usually the function you are about to render: name your method after the call). When the call is wrong (the real function is in another class), write the correct class and method in your reply instead of editing the caller. Do not add an alias that does not exist in the source.
- Your own calls into other files: `ClassName.method(...)` using names from `python3 tools/class_name.py <path>`; check that the method exists in that file.

## New knobs

Record hard-coded constants that change behaviour, per BRIEF2.md, in `tools/new_knobs/<group>.json` (a JSON array; the group name is your work-list name, for example `p3_vvah_llm_a`). Before adding one, search `tools/new_knobs/*.json`, `tools/worklists/*.json` and `../vvah.knobs.yaml` or `../vulnhunter.knobs.yaml` for the constant: reuse the existing id when the value is already a knob or the fallback default of one. Each new knob must be read as `θ["<id>"]` in its target at the line where it acts, with `// src:`.

## Acceptance

Work file by file and save after each one. When finished, from `pseudocode/`:

```
python3 tools/check_functions.py --only <each of your source files>   # every file at or near 100%
python3 tools/check_pseudocode.py --group <your group> --calls           # no missing, unknown ids or convention problems
python3 tools/check_src.py                                               # no bad pointers
```

A function that is intentionally not rendered (a test hook, a type alias, a one-line re-export) may stay unnamed; list each such case in your reply with the reason.

## Reply

Under 150 words: files changed or created, unnamed functions left (with reasons), new knobs added, calls you could not satisfy (caller, wrong name, right class and method), and anything unclear.
