# Review against the original conversion prompt

This review uses the [verbatim supplied prompt](conversion_instructions.md), the
pinned SudoLang specification/examples, the supplied harness source, and the
actual generated artifacts. It concerns conversion fidelity, not vulnerability
analysis or harness redesign.

This revision adds the previously missing behavioral prompt conversion. Earlier
claims of full completion based on exact prompt copies were too broad. Current
coverage distinguishes converted instructions, evidence-only data/context, tests
excluded from production conversion, and unresolved runtime/dependency behavior.
See [the prompt workflow](prompt_workflow.sudo.md) and [revision 4 notes](conversion_notes.md#revision-4--behavioral-prompt-conversion).

| Original requirement | Review and evidence | Qualification |
|---|---|---|
| Read the full specification and all examples first | Pinned v2.0 specification, README and all 26 example files were read; all were reread during this audit. `baseline_review.tsv` records paths/hashes. | Reading is a work record, not something a hash check proves. Older examples do not override the v2.0 baseline. |
| Identify inaccessible material | Direct clone supplies all requested specification/example files. All 945 harness files are accessible and classified. | External runtime implementations and effective dependency versions are identified in `dependency_boundaries.md`. |
| Distinguish constructs, vocabulary and grammar extensions | `representation_specification.md` maps baseline constructs and natural-language conventions; vocabulary is separately recorded. Existing functions/interfaces/conditions/loops and natural-language bodies suffice. | Source Python expressions, shell/query syntax and exact prompt text are source evidence, not proposed SudoLang operators/keywords. No grammar proposal is needed. |
| Represent executable code, prompts, configuration and available dependencies | 542 production Python modules, two embedded Python blocks, nine shell procedures, all 132 non-Python production/context resources, all five primary profiles, all 89 vendored SDK Python modules and its 16 query files are covered. | The 271 repository tests/fixtures are inventoried and hashed, not converted into production behavior. Packaging selects production packages; no statically resolved production import of root `tests` was found. Installed converter packages do not establish the harness runtime. |
| Preserve stage/component/substep hierarchy and source organization | `representation/harness.sudo.md`, the eleven readable component files, configuration/shell guides, and mirrored `source_detail/` retain entry branches, S0–S11 nesting and local callable definitions. `source_index.md` maps every supplied file. | The readable map is paired with exhaustive detail; it is not an independent flattened algorithm. |
| Preserve ordering, conditions, filters, gates, thresholds and cutoffs | Source/output audit checks statement order and indentation, signatures, control markers and expression placement. Exact source expressions and resources retain values. Manual comparisons cover configuration, stages, S4 scheduling/prompts/budgets, EV and remediation/validation handoffs. | Artifact checks establish structural properties, not a proof of all interactions among abstractions. Literal profile settings are distinguished from defaults and later overlays. |
| Preserve loops, retries and termination | Source loop bodies/exhaustion, breaks/continues, handlers and returns remain nested. Manual anchors include S4 split retries/deadline replay, S6 discovery waves/captive workers, EV endpoint budgets, remediation sequential processing and validation resume. | Unspecified provider/library retries are not inferred. |
| Preserve tools, parallelism, shared state and synchronization | Registration and calls remain distinct; exact call expressions are retained. Pool submissions/completion/wait/shutdown, timeout scopes, locks and shared counters remain in detailed source order. | Completion order is not invented as submission/risk order. Dynamic dispatch and library-internal scheduling remain boundaries. |
| Separate code enforcement from prompt instructions and model discretion | Markdown, literal, schema-dictionary/Field, configured guidance and shell feedback instructions are converted into model-request constraints and decision blocks. `prompt_workflow.sudo.md` maps supply/assembly to stages. Host gates, budgets and available tools remain separate; coverage and triage distinguish evidence-only content. | The literal/resource index is deliberately a superset of prompts. A string's presence does not establish model use or compliance; source callers determine its use. |
| Preserve contradictions and unusual behavior | S7 caller/schema tuple mismatch, graph-before-S0-stop, unconditional S4 inline-source wording, FILES schema versus wider prompt scope, finite evidence-gate relent and initial refusal exit status remain. EV rescue and remediation mode/prompt ordering are explicit. | These are fidelity records, not downstream flaw findings. |
| Avoid unnecessary line-by-line expansion | The readable map/groups explain workflow, while complete detail groups straight-line statements and preserves low-level decisions behind references. Prompt/query/shell lexical details remain exact evidence. | The detail and exhaustive vocabulary are large. They are review references for conditions that a shorter rendering could hide, not the recommended starting point. |
| Record every introduced identifier and its meaning/provenance/use | Vocabulary includes source names, import/exception bindings, member receivers, scope/context, literal/template identifiers and generated shell/readable wrappers; each table has definition, need, kind, original wording, source/use and reuse fields. | Context labels distinguish occurrences and do not claim compiler name resolution. No vocabulary extension was supplied; nothing is claimed as reused from one. |
| Cite substantive blocks and extracted prompts | `source_links.tsv` indexes citations; `prompt_locations.tsv`, `.evidence.json`, original resource copies and YAML value spans locate text. Decorators have their own source spans. Empty/binary resources have no invented source line. | Citation validation verifies file/range/target location. It does not prove that prose accurately summarizes the cited source. |
| Document versions, instructions/revisions, coverage, abstraction, hierarchy and missing evidence | `conversion_notes.md`, verbatim `conversion_instructions.md`, coverage/indexes, representation conventions, this review and dependency boundaries provide these records. | Earlier partial-status records remain explicitly historical under `history/`. |
| Review omissions, altered hierarchy/order, invented behavior and vocabulary consistency | Full source/output structural audit plus documented manual comparisons; the concrete corrections below were applied and artifacts regenerated. | No model agreement, runtime scan or fabricated test outcome is used as correctness evidence. |
| Keep scope focused and disclose partial coverage | Work remains representation/vocabulary/conversion documentation under `sudolang-code-chatgpt/`. No harness implementation was changed, and no scan/model/EV/remediation operation was executed. | Tests and external runtime boundaries are disclosed above and per file. No identified instruction-bearing production content remains evidence-only. Excluded tests and unknown runtime/dependency behavior are explicit; universal semantic verification is not claimed. |

## Corrections made during this audit

| Conversion issue | Correction and review anchor |
|---|---|
| The earlier checker counted AST records without checking their placement in pseudocode | Added `tools/audit_requirements.py`: independent source preorder, rendered statement locations/indentation, function signatures, control markers, expression placement and source-expression roundtrips, including embedded scripts. |
| Embedded Python headers linked a nonexistent generic evidence path | Both headers now point to their actual `.embedded-L*.evidence.json`; embedded expressions/strings are included and audited. See `embedded_python.tsv`. |
| Decorator timing and try-else wording were imprecise | Render decorator evaluation before defaults/type bases/body and application after object creation; function bodies are invocation descriptions. Try-else requires normal fallthrough, excluding return/break/continue. All decorated definitions are covered by the output audit. |
| Readable S10 summary put caller operations inside `_invoke` | `_invoke` now returns raw route output. Separate `call_with_guards`, `harness_amend` and `apply_plugin` blocks retain parsing, policy, contract and persistence hierarchy. Compare `plugin_runner/__init__.py:461-505` and `plugin_runner/run.py:95-120,146-168,191-207`. |
| A SARIF parameter and an S4 prompt call had inconsistent argument spelling/binding | The SARIF wrapper consistently uses `sarif_path`; `_unit_block` explicitly receives `graph=graph`. Compare `s9_sarif.py:26-31` and `s4/prompts.py:528-533`. |
| S5/EV/S7/progress summaries could hide conditions or imply stronger behavior | Clarified S5 secret-class exception and optional inventory gate; EV candidate order, static/drop rescue, final concatenation and cleanup scope; S7 zero/one list-copy behavior; remediation progress includes failures in its own not_fixed count. Corresponding exact modules remain linked from the readable map. |
| Vocabulary collapsed same-spelled names across functions and receivers and missed some wrappers/bindings | Added source scope/context, lambda/comprehension coordinates, symbol role, full member receivers, import/exception bindings, explicit wrapper entries and actual use sites. These are ordinary identifiers, not grammar changes. |
| A YAML block-scalar end mark was treated as inclusive and extended beyond EOF | Convert exclusive YAML marks to inclusive spans. `inputs/remediation_playbook.yaml`'s prompt template ends on line 439. Validate every YAML and prompt-index span. |
| Empty typing-marker files had artificial 1–1 citations | Keep exact empty assets, explicitly state that no source line exists, and omit them from the text-location index. |
| Prompt evidence was difficult to locate outside Python and Markdown | Add `prompt_locations.tsv` covering Python/embedded literals, resource text and YAML string values, including configurable prompt templates. Roles explicitly avoid assuming every indexed string is a model instruction. |
| Completion documentation retained older counts/status wording | Update current notes and README; preserve historical records as history. Keep actual checks and semantic limitations separate. |

## What remains unverified

Manual semantic comparison is limited to the recorded source-to-representation
anchors and the representation conventions. No claim is made that a human has
manually audited every statement in all 542 modules. The structural audit does not
establish formal equivalence, interpret SudoLang, resolve every dynamic call, prove
model compliance, or validate provider/native dependency internals. External
implementations, future inputs/plugins and live results remain the specific
boundaries in `dependency_boundaries.md`.

The current machine-readable results are `verification.json` and
`audit_results.json`. They report artifact/source checks, not harness tests.

## Recorded audit result

Both static reports pass with zero errors. The audit checked 46,003 rendered
statement locations (45,906 module statements plus 97 embedded statements),
3,639 function signatures, 33,358 rendered expressions with restored-source
roundtrips, 400 decorated definitions and 6,109 evidence identifiers. It checked
112,591 source/resource vocabulary rows, distinguishing 19,563 same-spelled names
across source contexts; generated readable-wrapper entries are recorded as well.
All 2,415 YAML scalar spans and 32,017 literal/resource location records have
valid source ranges. The companion verification checks all 945 source hashes,
542 module renderings, 132 byte-identical resources and 34,304 citations.

These are the measured artifact results, not a semantic correctness percentage.
No harness source/configuration diff was introduced.

## Behavioral prompt review added in revision 4

| User clarification | Current artifact/check | Limit |
|---|---|---|
| Inspect Markdown prompts, skills, personas and embedded/configured strings | 27 Markdown conversions; all maximal Python/embedded carriers triaged; all 132 resources dispositioned | Ordinary docs/data are evidence-only; tests remain excluded |
| Convert roles, goals, procedures, gates, tools, retries, stopping and output | 215 instruction source views, including 39 structured decision views; source-cited detailed constraints preserve remaining clauses | A requested action is not proof it ran |
| Preserve code/request/model-choice distinction | Model-request prefaces, host-assembly blocks, advertised-description roles, conditional exposure and source-detail dispatch links | Unobserved dynamic delivery is unresolved |
| Preserve prompt hierarchy and dynamic insertion | Original headings/list nesting; source-specific decision views; actual f-string slots and format-call evidence | Independent criteria gain no invented order |
| Preserve ambiguity, exceptions and contradictions | Revision 4 review anchors and tensions, with exact source evidence retained | No invented missing continuation, threshold or precedence |
| Reuse vocabulary before adding identifiers | `prompt_vocabulary.tsv` records existing lookup, source context, definition, need, kind, use and reuse; integrated in main vocabulary | Same spelling across contexts does not force same meaning |
| Update coverage and source references | Main coverage has instruction-status/view columns; prompt coverage, units, triage and source-link indexes | Structural coverage alone is not semantic correctness |
| Keep evidence separate from conversion | Markdown source_detail is converted; code/config/shell views link to converted instructions; original copies stay in assets | Literal examples remain evidence for the converted format/pattern role |

`prompt_verification.json` records the current static prompt checks.
`verification.json` and `audit_results.json` record the structural checks. Manual
comparisons are explicitly listed in conversion notes. No model agreement or
runtime test is used to establish correctness.
