# Harness pseudocode and knob spaces

Both harnesses use one Java-style pseudocode format and one shared JSON schema.
The purpose is to compare algorithms and controls across implementations, and to
represent future harnesses using the same vocabulary.

Start with [FORMAT.md](FORMAT.md), the common authoring and fidelity contract.
[Common.pseudo](schema/Common.pseudo) defines syntax, executors and shared types;
[knobspace.schema.json](schema/knobspace.schema.json) defines the exported data.
[harnesses.json](harnesses.json) registers harnesses, paths, worklist ownership and
selected source globs. The parser, builder and checks read that catalog.

## Current artifacts

| | VVAH | VulnHunter |
|---|---:|---:|
| Pseudocode files | 386 | 153 |
| Components (modules, classes, methods) | 3,617 | 1,904 |
| Knobs | 2,383 | 2,899 |
| Methods: CODE / MODEL / MIXED | 2,134 / 387 / 36 | 694 / 692 / 63 |
| Missing knob reads / unknown IDs / convention problems | 0 / 0 / 0 | 0 / 0 / 0 |
| Remaining unresolved calls to known classes | 64 | 47 |

The completion pass added 26 VVAH files and 6 VulnHunter files, 67 VVAH knobs
and 21 VulnHunter knobs. It also removed ten misplaced duplicate VVAH knob rows
from a VulnHunter worklist, normalized legacy type aliases to the common schema,
and resolved duplicate class names and several incorrect cross-file targets.

Selected source-file coverage is complete: 133 VVAH Python files across scope,
evidence, codegraph, plugins, util, report, cli and validation; 64 VulnHunter
Python files across agent helpers and fixer scripts. Coverage means a corresponding
file exists with the correct source header. It is not a branch-equivalence proof.

The source audit corrected evidence-cap sanitization (including zero and error
fallbacks), propagation of sanitized limits, config-dedup overlays, missing map
bucket initialization, and graph-tool reference/path caps, plugin registration,
query result formatting and telemetry. New Semgrep and validation files preserve
host-versus-model enforcement and source failure behavior.

## Reading order

| Harness | Entry | Follow with |
|---|---|---|
| VVAH | `vvah/vvaharness/orchestrator/scan.pseudo` | pipeline stages, their prompts/session/outcome helpers, then skills |
| VulnHunter | `vulnhunter/vulnhunter-agent/agent/runner.pseudo` and `vulnhunter/vulnhunt/SKILL.pseudo` | recon, hunt/class groups, verify, reproduce, sweep and report |

An entry point can summarize lower-level behavior; detailed helpers live at their
source-relative paths. Calls use the target's declared `Class.method`. A routine
may cite its source definition with `@src`; knob reads cite their definitions or
enforcement sites with `// src:`. Both pointer forms are checked.

`θ["id"]` connects the procedure to the knob space. `CODE`, `MODEL` and `MIXED`
state who enforces each component. A MODEL procedure is a rendering of prompt
instructions, not a guarantee that the model follows them. A code-constant knob
represents a possible source edit, not an existing runtime option.

## Layout and derived outputs

- `<harness-folder>/.../*.pseudo`: the common-format algorithms.
- `<harness-folder>/<name>.knobs.json`: generated components and knob readers in
  the shared schema; these have been regenerated for the completion pass.
- `tools/worklists/`: registry knob target assignments.
- `tools/new_knobs/`: additional source constants and prompt constraints.
- `tools/class_names.json`: unique primary class names per harness.
- `tools/BRIEF.md`, `tools/BRIEF2.md`: historical authoring briefs; FORMAT.md is
  the consolidated contract for new work.

The YAML comparison registries and the top-level comparison.md describe the
original 1,990/2,723-knob baseline. Additional extraction lives in new_knobs and
is included in the generated JSON. Do not interpret the baseline totals as the
current full pseudocode inventory.

The existing ConfigSpace JSON files are older snapshots and have not been
regenerated in this pass: ConfigSpace is not installed in this environment.
Regenerate them with export_configspace.py before using them for search. Real
numeric domains are often only observed shipped values, not continuous ranges.

## Checks

Run from this folder (or use absolute script paths from another directory):

```
python3 tools/check_coverage.py
python3 tools/check_src.py
python3 tools/check_pseudocode.py --calls
python3 tools/check_pseudocode.py --group completion_vvah --calls --strict
python3 tools/check_pseudocode.py --group completion_vh --calls --strict
python3 tools/build_knobspace.py
python3 -m unittest discover -s tools/tests -v
```

The builder requires PyYAML and jsonschema. Validation here used `/usr/bin/python3`
for the builder/tests because the ambient `python3` has incompatible jsonschema
transitive dependencies. The dependency-free structural checks work with either.

Both generated knob files validate against the shared schema. Source pointers
resolve to real files and in-range lines. The new-knob target groups pass strict
checks. The four integration tests exercise adding a third harness without
checker changes, rejection of invalid source annotations from another working
directory, strict rejection of unresolved calls, and explicit naming-table selection for shared relative paths.

## Limits of the current pseudocode

The older files still contain the unresolved calls listed above. Some are
abstract factories or library-like shorthand; others need further source-backed
rendering. Run `check_pseudocode.py --calls --strict` to see them and receive a
nonzero exit status. The default check preserves its historical behavior of
failing only missing/unknown knob IDs, so a zero default exit is not full approval.

Neither schema validation, file coverage, call resolution nor source-pointer
validation proves semantic fidelity. In particular, no automated check proves
that a prompt's modeled procedure happens at runtime. Source ambiguities remain
marked `// unclear:`. These artifacts should not be described as a fully verified
precise representation of every behavior in both products.

Exploit verification remains out of scope: only the pre-existing config stub and
pipeline boundary are represented. No source repository was modified or executed.
