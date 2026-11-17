# Brief: contradictions inside one harness (low level)

## Goal

Find places where ONE harness contradicts itself, and verify each against the real source. This is the third and lowest layer of a layered qualitative analysis of two vulnerability-detection harnesses. The upper layers (design conflicts between the two harnesses) are written elsewhere. You work on one harness only.

The harness repositories are read-only. Write only the output file named in your task.

## Writing rule

Write every word in full. No abbreviations or shortened forms for ordinary words or concepts: write "threat model", not "tm"; "false positive", not "FP"; "proof of concept", not "PoC"; "exploit verification", not "EV"; "Common Weakness Enumeration" on first use before "CWE"; "versus", not "vs."; "for example", not "e.g."; "that is", not "i.e.". The two harness names (VulnHunter, VVAH) and literal identifiers (file paths, knob identifiers, function names, enumeration values) are written as they are, in code formatting. Stage numbers are written with their meaning, for example "Stage 4 (deep investigation)".

## What counts as a contradiction

1. **Prompt against prompt:** two statements in the model-facing text of this harness that cannot both be followed, or that give different values for the same rule.
2. **Prompt against code:** the prompt tells the model something that the code does not do, or the code enforces a different rule from the one the prompt states.
3. **Configuration against code:** a declared setting that is ignored, never read, overridden, or behaves differently from its documentation or name.
4. **Configuration against configuration:** two layers that disagree about the same setting (built-in default, shipped profile, example file, documentation).
5. **Documentation against behaviour:** a comment, README or docstring that says something the code does not do.
6. **Dead or unreachable rules:** text or code that is defined but can never take effect (never registered, never called, gated off in every shipped configuration).
7. **Ambiguity with consequence:** a rule whose text leaves a case undefined, where the missing case changes what the harness reports.

Not a contradiction: a limitation, a design choice you would have made differently, a style problem, or a harness that is merely simpler than the other one.

## Where to look

- The real source: for VVAH `/home/spl/akram/harness-comparison/visa-vulnerability-agentic-harness/` (Python package `vvaharness/`, prompt strings in `*/prompts.py`, skills in `vvaharness/skills/*/SKILL.md`, configuration in `vvaharness/config/__init__.py` and `vvaharness/config/profiles/*.yaml`); for VulnHunter `/home/spl/akram/harness-comparison/VulnHunter/` (prompts in `vulnhunt/SKILL.md`, `vulnhunt/phases/*.md`, `vulnhunter-fix/`, `vulnhunt-fix-verify/`; Python in `vulnhunter-agent/agent/`; configuration in `vulnhunter-agent/agent/config.py`, `config.example.toml` and `vulnhunter-fix/config.json`).
- The pseudocode, which renders every file and marks ambiguity: `/home/spl/akram/harness-comparison/comparison-results/pseudocode/<vvah or vulnhunter>/`. Search it for `unclear:` and read the surrounding code. The list of all such notes is `/home/spl/akram/harness-comparison/comparison-results/qualitative-analysis/evidence-unclear-notes.tsv` (many are only about method names: skip those).
- The knob registries: `/home/spl/akram/harness-comparison/comparison-results/vvah.knobs.yaml` and `vulnhunter.knobs.yaml` (each knob has `source`, `default`, `requires`), and the knob lists in `.../pseudocode/tools/new_knobs/*.json`.
- Earlier research notes with leads (some are only leads, verify them): `/scratch/mkhan04/tmp/claude-261169/-home-spl-akram-update-cap-one-harness-VulnHunter/21512d31-6460-4dde-a2e9-e398bfab60b3/scratchpad/vulnhunter_notes.md` and `visa_notes.md`.
- Leads already known, to verify and expand: VulnHunter: phase 2 hunt text says the sink-driven agent runs as its own final wave in one place and in parallel in another; `fix.behavior.confirm_before_push` is true in the skill text and false in the configuration; `fix.models.routing` is unused; the example configuration ships `sandbox.enabled = false` and `issues.enabled = false` while the code defaults are true; `verify_refs.py` documents one model and uses another; `analyze_misses.py` points at a directory that does not exist; the verification table rows for FULL and MITIGATION overlap when column 6 is yes; the stub disposition in fix-verify. VVAH: the system and planning prompts say the source is already inlined even when `step4.inline_source` is off; `step8.resume_timeout` is never read; `max_diff_lines`, `max_files_touched`, `allow_new_dependencies` and `never_autofix_cwes` in the remediation playbook are never read; host scoring treats `root_cause` as critical and has no 0.5 coverage floor while the scoring prompt says otherwise; a validation skill says to search for a leaked secret while the scoring matrix forbids it; prompt fragments defined in `profiles.py` but never registered; `ForceVerdictOnly` and the repeat guard are not used by Stage 4; the built-in default and shipped profile defaults disagree for `step6_verify.min_confidence` (7, 5, 1); `step4.evidence_gate` is only enforced when planning is on and the route is deepagents; the recursion-limit floor makes `max_turns` behave differently on different routes. Exploit verification (VVAH Stage 6 exploit stage) is out of scope.

## How to work

1. Collect candidates from the leads, the unclear notes, and your own reading. For VVAH read the prompts and the code that consumes their output side by side; for VulnHunter read each phase prompt against the next phase prompt and the Python that launches them.
2. For each candidate, open BOTH locations in the real source and confirm the contradiction from the text, with line numbers. Drop candidates you cannot confirm; list them in a final section "Candidates not confirmed" with one line each saying why.
3. Aim for 25 to 40 confirmed findings of real substance. Quality over quantity. Order them by consequence (largest effect on what the harness reports or misses first).

## Output format

One Markdown file at the path given in your task. Start with a short introduction (what was checked, how, counts by kind and by consequence level). Then one section per finding, in this exact shape:

```
### Finding <number>: <title in full words>

- **Kind:** <one of the seven kinds above, in words>
- **Where:** <two or more locations, each as `path:line` followed by a quotation of at most twenty-five words>
- **What conflicts:** <two to four sentences>
- **What actually happens:** <what the code or the model-facing text does in practice, with the evidence for that>
- **Consequence:** <effect on detection, false positives, cost, safety, or reporting; say "none observable" if it is only a documentation problem>
- **Consequence level:** high | medium | low
- **Knobs involved:** <knob identifiers in code formatting, or "none">
- **Evidence strength:** verified in source | verified in pseudocode only | inferred
```

End with the section "Candidates not confirmed".

## Reply

Under 120 words: the output path, number of findings by consequence level, number of candidates not confirmed, anything you could not check.
