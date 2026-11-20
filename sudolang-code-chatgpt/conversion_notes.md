# Conversion notes

## Completion, scope and versions

The conversion now includes a behavioral prompt layer alongside the existing
production-code representation. Earlier completion wording was too broad: retaining
Markdown and string literals as evidence did not convert their instructions. The
current prompt layer represents those instructions with SudoLang constraints and
requested decision/procedure blocks; evidence copies remain separate.

The supplied scope is non-test production code and resources. Tests/fixtures remain
explicitly excluded, and unavailable dependency internals and runtime/model choices
remain unresolved. Coverage is not a claim of whole-runtime equivalence or an
exhaustive manual semantic audit.

- Conversion date: 2026-11-20, America/New_York (user session date).
- SudoLang: `https://github.com/paralleldrive/sudolang`, commit
  `dcef61ef253e389d02c72b67215cf97de5bdbbae`, specification **SudoLang v2.0**.
  Full local repository snapshot: `reference/sudolang/`.
- Harness: `visa-vulnerability-agentic-harness/pyproject.toml` declares
  **vvaharness 1.5.1**. The source directory has no independent Git checkout.
  Parent comparison-repository commit `fe88503a680ccfbd7248cf32000e58cd7b796dbb`
  (2026-11-17) is not asserted to be an upstream Visa commit.
- SHA-256 hashes in `coverage.tsv` identify the actual inspected working-tree
  sources. All available vendored runtime Python code is included.

## Instructions and revision history

The user's governing instructions are retained here for review:

1. Work under `sudolang-code-chatgpt/`; first read the entire supplied SudoLang
   specification and every example, then inspect harness code and resources.
2. Prefer baseline constructs and vocabulary additions. Propose grammar changes
   separately only when existing constructs genuinely cannot express behavior.
3. Preserve directory/file mappings, stage/component/substep hierarchy, order,
   branches, call relationships, gates, filters, thresholds, retries, termination,
   tools, shared state and explicitly specified parallelism/synchronization.
4. Include prompts/configuration/available dependency code. Separate host-enforced
   execution from model requests and available tools. Never infer unavailable behavior.
5. Cite substantive blocks and extracted prompts. Preserve apparent contradictions
   and unusual behavior rather than correcting them. Avoid unnecessary expansion;
   retain detail where abstraction could hide decisions.
6. Maintain an exhaustive vocabulary record with meaning, need, category, original
   wording, references, use and reuse status, plus conversion/review/coverage notes.
7. Produce representation and documentation only. No downstream flaw analysis,
   redesign, invented tests or correctness claims based on model agreement.

Revision 1 delivered eleven readable modules and explicitly marked incomplete
coverage. That record is preserved in `history/batch1_conversion_notes.md`.
The user's subsequent instruction was to complete the main request; this revision
adds all remaining non-test Python modules and resources, a full workflow map,
configuration/shell guides, exact prompt evidence, comprehensive vocabulary and
independent structural checks. Historical status documents are not current ledgers.

During review, source oddities were retained: graph construction precedes the S0
stop; the S7 four-tuple caller fallback remains beside the checkpoint five/six-tuple
schema; finite executable evidence-gate rejection remains separate from stronger
prompt wording; source truthiness, cleanup scopes and empty-map behavior remain.
The review tool's expression checks were corrected to handle nested AST nodes with
shared coordinates and multiline concatenated f-strings. These were converter
verification changes, not harness behavior changes.

The harness `AGENTS.md` was read completely. No scan/model/EV/remediation operation
was required or run, and no harness source or configuration was changed.

## Baseline reviewed and accessibility

The full `sudolang.sudo.md` (417 lines), repository README and all **26** files
under `examples/`, including `reflective-thought-composition.readme.md`, were read.
`baseline_review.tsv` records all 28 paths, line counts, hashes and reading status.
Examples cover interfaces/state/commands, functions/composition, conditions, loops,
options, requirements, constraints and mixed Markdown. Older adventure syntax and
minimalist examples are not silently promoted to replacement grammar.

GitHub's examples HTML initially reported a loading error; direct Git cloning
succeeded. **No supplied specification/example or harness file remained
inaccessible.** Linked videos, articles and share chats are not repository examples
and were not claimed as read. No interpreter/conformance execution is claimed.

Existing SudoLang constructs suffice. Exception handling, asynchronous calls,
locks, futures and lifecycle rules are natural-language statements inside ordinary
functions, not new keywords. Source expressions are evidence within those statements;
Python operators are not proposed SudoLang grammar. No
`language_extension_proposals.md` is necessary or created.

## Coverage record

`coverage.tsv` is authoritative per source file and includes exact hashes and
representation/asset paths. `source_index.md` groups the same original organization.

| Status | Files | Treatment |
|---|---:|---|
| represented-structural | 542 | Every non-test Python module has nested structural pseudocode and exact expression/string evidence |
| shell-procedure | 9 | Shell helper/control-flow representation plus exact ordered command source; two Python heredocs also converted |
| prompt-document | 25 | Resource inventory category; actual instruction Markdown is converted, with evidence-only documentation distinguished in the separate prompt ledger |
| data-resource | 30 | Exact original data; YAML/JSON/TOML parsed values and configuration scalar locations where applicable |
| query-resource | 16 | Exact Tree-sitter query data with source mapping; invocation remains in converted SDK code |
| support-resource | 12 | Exact support/build assets, classified outside scan-stage behavior |
| context-document | 39 | Complete repository/build/operating context retained, not invented as executable workflow |
| context-binary | 1 | Exact pipeline GIF retained as binary context, without invented line citations |
| excluded-test | 271 | Tests/fixtures inventoried and hashed; not converted into production behavior or executed |
| **Total** | **945** | **Every supplied file classified** |

The 542 Python modules comprise 451 under `vvaharness/`, 89 under
`vendor/context_graph_sdk/`, and two repository scripts. Runtime files are selected
by source location, not by a filename beginning with `test`. Test directories and
fixtures are deliberately excluded, with their individual paths visible in the
ledger. Exact resource copies cover all 132 non-Python non-test files.
The two embedded Python blocks contain 97 additional statements at original shell
coordinates; see `embedded_python.tsv`.

The old planned batches are now closed: entry/configuration/scope/graph/S0–S3;
S5–S9/report/models; backend dispatch/tools/middleware; EV/remediation/validation;
and supporting resources all have corresponding detail. Eleven earlier manually
written component renderings remain useful readable companions, not the extent
of current coverage.

## Abstraction and hierarchy mapping

The representation has two complementary layers:

- `representation/harness.sudo.md` explains entry/configuration/batch branches,
  S0–S11 nesting, S5/S6 discovery/retry waves, EV collection/gates/probe/mapping/
  attack/judge/replay, and remediation/validation handoffs. Existing readable
  `representation/vvaharness/` modules retain the full scan orchestration and S4
  scheduler/session/prompt/middleware nesting. `configuration.sudo.md` and
  `shell-probes.sudo.md` explain overlays/profile choices and probe helper caps.
- `source_detail/<original-path>.sudo.md` mirrors every non-test source path,
  retaining original extensions to avoid collisions. Python functions remain
  functions, source classes are described through interfaces, and branches/loops/
  handlers/context managers remain nested at their original positions. Async and
  yield positions, decorators, signatures, defaults, imports and call expressions
  are retained. Straight-line operations are grouped in source order; the extra
  detail keeps decision-relevant defaults and exceptional transitions reviewable.

`entry.main` dispatches batch/single workflows after configuration/preflight;
`scan_repo` establishes identity, seeds/builds graph, then enters its protected
stage sequence. S5/S6 checkpoint reuse remains nested inside the S7-bundle branch.
S4 partitions work and collects initial futures before singleton retry futures;
session middleware/replay/resume/outcome reduction remain nested calls. EV is
inside S6's selected verification path. S10/S11 are conditional downstream calls,
while direct API/SDK entrypaths remain independent source entrypaths. Alternative
branches are not flattened into guaranteed sequential actions.

Concurrency is stated only where source dispatch/wait/lock/shutdown operations
specify it. Calls/imports remain explicit relationships, not an invented global
call order. `call_sites.tsv` and `import_links.tsv` are static references, not a
claim to resolve all dynamic dispatch. No tool registration is promoted to a call.
Model-facing text is requested behavior; actual middleware and host validators
are separate executable gates.

All source strings (30,079 AST string nodes) are retained with coordinates in
`assets/<module>.evidence.json`. Exact original source and expression records
accompany them. Long strings use ordinary `source_literal_LINE_COLUMN` identifiers;
f-strings use `source_template_LINE_COLUMN` with original interpolation. Callers
establish which strings are prompts; extraction alone does not. `prompt_assets.tsv`
indexes this evidence and complete Markdown documents. Resource originals live in
`assets/original/`; parsed data and 2,415 YAML scalar locations support review.
Exact command/query appendices are source evidence, not added grammar.

The exhaustive vocabulary record includes source bindings/fields/parameters/keys,
qualified names, evidence identifiers and explanatory concepts. Source contexts
remain distinct. Definitions use source expressions/docstrings rather than inferred
external implementations. Each row records why needed, source/use and provenance.
No supplied vocabulary-extension file was provided; all are newly recorded relative
to baseline, with original source spellings reused where meanings match. Ordinary
English statements do not declare new language identifiers.

## Review and limitations

Full structural coverage was checked mechanically; it was not a manual line-by-line
semantic audit of every module. Readable source comparisons and workflow checks
cover the cases below plus main configuration merge/overlay ordering, stage
handoffs, discovery-wave retries, shell probe limits and source-selected verification/
remediation/validation branches. Exact detail/evidence is available for further
manual review. Structural checks do not prove the renderer captures every runtime
semantic interaction correctly.

| Source location | Representation location | Checked correspondence |
|---|---|---|
| `entry.py:243-290` | `entry.sudo.md`, main startup | trusted-config before load; explicit step1 overlay disables auto derivation |
| `entry.py:318-338` | `entry.sudo.md`, backend preflight | clone/ev bypass readiness probe, unreachable remediation/validation roles skipped |
| `scan.py:394-443` | `scan.sudo.md`, initialization | fresh reset exception for ev, HEAD mismatch reset without toggling resume, refusal default exit 0 |
| `scan.py:584-614` | `scan.sudo.md`, graph/S1 | build graph before s0 stop; attach live graph after restored S1; cleanup boundary retained |
| `scan.py:617-730` | `scan.sudo.md`, S2–S4/S7 gates | attempted S2 rerun invalidates S3 reuse, S3 restore gates S4 reuse, S4 restore gates S7 reuse |
| `checkpoints.py:67-70` | `checkpoints.sudo.md`, completeness | exact untrusted outcome set; empty map accepted, despite caller warning mentioning no outcome |
| `checkpoints.py:83-93,133-149` and `scan.py:808-830` | both checkpoint and scan renderings | five/six-tuple schema and four-tuple caller fallback both retained |
| `scan.py:977-993` | `scan.sudo.md`, S9 | optional upload/checkpoint precedes s9 stop |
| `scan.py:1003-1052` | `scan.sudo.md`, S10/S11 | preflight refusal disables stage without setting rem_rc/val_rc; first truthy exit-code precedence |
| `s4/batching.py:34-48` | `batching.sudo.md` | file overlap preference, risk/id ties, LARGE singles appended after normal batches |
| `s4_deepdive.py:193-344` | `s4_deepdive.sudo.md` | initial completions then retry completions; halt tracking skips existing outcomes; final waiting shutdown |
| `s4/session.py:99-113,418-419` | `session.sudo.md` | middleware batch limit grows by extra members; prompt receives unscaled configured value |
| `s4/session.py:340-376,504-508` | `session.sudo.md` | cap before canonical-key dedup; per batch member, emission-order cap |
| `s4/outcomes.py:274-300` | `outcomes.sudo.md` | dictionary-key reduction, no explicit returned-unit-id comparison or verdict-based suppression here |
| `s4/prompts.py:122-134,423-444` | `prompts.sudo.md` | unconditional already-inlined clause alongside conditional source-section wording |
| `s4/outcomes.py:36` and `s4/prompts.py:104-113` | `outcomes.sudo.md` and `prompts.sudo.md` | FILES-list field wording versus prompt allowing evidence-led movement beyond FILES |
| `evidence_gate.py:142-194` | `evidence_gate.sudo.md` | any required-tool intersection suffices; finite rejections; out-of-loop form ignores todos |
| `tool_budget.py:113-159` | `tool_budget.sudo.md` | atomic claim before handler, no shown refund, nonmetered tools pass |
| `model_call_budget.py:65-117` | `model_call_budget.sudo.md` | final turn at >= limit, subsequent opted-in error, resume grants one renewed final turn |


Additional manual review anchors:

| Source | Representation | Checked correspondence |
|---|---|---|
| `vvaharness/config/__init__.py:839-1008` | `representation/harness.sudo.md`, configuration | default/profile/local merge order; separate step1 append-versus-replace semantics; size/path/shape gates |
| `vvaharness/orchestrator/batch.py:380-504,545-647` | workflow map and mirrored batch detail | manifest filtering before acquisition; sequential entries versus grouped applications; cleanup and exit precedence |
| `vvaharness/pipeline/stages/s0_seed.py:40-79` | mirrored S0 detail and workflow map | optional language narrowing preserves warnings and exact membership; walk then deterministic detection |
| `vvaharness/skills/client-side/probe.sh:71-117` | shell guide and embedded-L71 detail | exact embedded Python and original coordinates; host script remains optional tool behavior |
| `vvaharness/skills/code-exploration/probe.sh:51-158` | shell guide and embedded-L51 detail | embedded Python coverage, loop structure and original script boundary |

Preserved code/prompt distinctions include the unconditional already-inlined S4
clause alongside conditional source-section wording, FILES-list schema wording
alongside evidence-led wider exploration, and the finite evidence gate alongside
prompt requirements. No redesign or flaw assessment is inferred from these records.

Unresolved evidence is listed in `dependency_boundaries.md`: external DeepAgents/
LangChain/LangGraph/provider/native-parser/database implementations, effective
runtime dependency versions, runtime plugins/operator inputs, actual scheduler/
process/network/database outcomes and model decisions/compliance. Vendored code
is available and converted; external requirements are represented at call boundaries.
Converter-environment package metadata does not establish a harness runtime. No
project lockfile or project virtual environment was found at checked locations.

Tests/fixtures remain unconverted by explicit scope. No runtime harness test,
security scan, model invocation, exploit verification or remediation result is
claimed. No model-generated output or agreement between models proves correctness.

## Reproducibility and actual checks

From the comparison-repository root:

```sh
python sudolang-code-chatgpt/tools/complete_representation.py
python sudolang-code-chatgpt/tools/complete_assets.py
python sudolang-code-chatgpt/tools/convert_prompt_instructions.py
python sudolang-code-chatgpt/tools/integrate_prompt_views.py
python sudolang-code-chatgpt/tools/finalize_indexes.py
python sudolang-code-chatgpt/tools/check_complete.py
python sudolang-code-chatgpt/tools/audit_requirements.py
python sudolang-code-chatgpt/tools/check_prompt_conversion.py
```

These tools parse/copy supplied sources; they do not import or execute harness
modules. Compatibility entrypoints `index_evidence.py` and `check_artifacts.py`
respectively run current index finalization and current checks. Old implementations
are retained only in `history/`.

The completed `verification.json` reports **passed**, with zero errors:

| Check | Count |
|---|---:|
| Supplied source hashes and inventory | 945 |
| Python modules | 542 |
| Source AST statements matched to detail records | 45,906 |
| Exact source string nodes | 30,079 |
| Expression AST roundtrips after restoring evidence identifiers | 33,267 |
| Byte-identical resource copies | 132 |
| Embedded Python blocks / statements | 2 / 97 |
| Source citations with valid file/range/target locations (including converted prompts) | 38,297 |
| Resolved local import target references | 2,668 |
| Baseline reading records / example files | 28 / 26 |

Statement comparison uses node kind and original line/end-line/column coordinates;
string values and original source bytes are checked independently. Expression
roundtrips compare parsed source expressions after restoring literal/template
references. Resource checks compare bytes. Citation checks verify ranges, not the
semantic truth of prose. These checks establish coverage and artifact consistency,
not formal equivalence, runtime success or downstream vulnerability findings.

## Revision 3 — audit against the supplied prompt

The user supplied the original prompt again and requested a full double-check.
The exact prompt is preserved in `conversion_instructions.md`;
`requirements_review.md` maps every requirement to artifacts, review evidence
and explicit qualifications. The pinned specification/README and all 26 examples
were reread during this audit; their hashes/versions remain unchanged.

This audit corrected embedded-evidence links, decorator/try-else descriptions,
readable remediation calling hierarchy, argument spelling/binding, source gates
and cleanup qualifications, vocabulary scope/role distinctions, YAML exclusive
end positions and empty-file line citations. It added `prompt_locations.tsv`
for literal/resource/YAML instruction locations and `tools/audit_requirements.py`
for source/output checks beyond the earlier record-count verification. See the
requirement review's correction table for source anchors.

Vocabulary records now distinguish source function/type scopes, lambda and
comprehension contexts, symbol roles and member receivers. Context labels are
locations, not inferred compiler bindings or universal definitions of short names.
Import/exception bindings and generated shell wrapper identifiers are included.

Run the additional audit from the repository root:

```sh
python sudolang-code-chatgpt/tools/audit_requirements.py
```

`audit_results.json` records source/output statement order, nesting and locations;
function signatures; expression placement and source roundtrips; evidence links;
vocabulary source/use ranges; exact resources; and YAML/prompt location ranges.
Both check reports establish static artifact properties only. The readable
changes were compared against their cited source; the manual examples above
remain a bounded review record, not an exhaustive manual semantic audit. No
production-conversion batch remains pending. The 271 tests/fixtures remain
explicitly excluded from production pseudocode and were not executed. No scan,
model call, EV operation or remediation was run; product sources were unchanged.

Final audit results: both reports pass with zero errors. The output-facing audit
covers 46,003 statement locations, 3,639 signatures, 33,358 expressions, 400
decorated definitions, 112,591 vocabulary rows, 2,415 YAML spans and 32,017
literal/resource locations. See `requirements_review.md` for the correction
record, source anchors and scope qualifications. Vocabulary use coordinates
identify corresponding rendered statement/block locations; they do not claim
to resolve every dynamic binding.

## Revision 4 — behavioral prompt conversion

The user clarified that verbatim Markdown prompts, personas, skills and embedded
prompt strings were insufficient, and required their behavioral instructions to be
translated. This revision preserves the original source files and adds the missing
representation within this output directory. This supersedes the earlier
completion claims insofar as they treated exact prompt preservation as conversion.
The user's “try now” instruction continued this same work; no task scope changed.

### Content coverage and evidence roles

- `prompt_representation/` mirrors each instruction-bearing source. There are
  **215 converted source views**: **27 Markdown**, **179 Python**, **four YAML/
  configuration guidance** and **five shell feedback** sources. Markdown includes
  all seventeen detection skills, all seven validation system/persona/rule/skill
  documents, and the three repository/operator agent instruction documents.
- **27,792 maximal Python/embedded string or template sites** have individual
  dispositions in `prompt_content_triage.tsv`. Maximal templates avoid counting
  f-string fragments as separate prompts. Literal labels, enums, empty values,
  documentation and ordinary data are distinguished from instruction carriers.
- Every one of the **132 non-test resources** is classified in
  `prompt_content_coverage.tsv`; **96** remain evidence-only data/context rather
  than invented model instructions. Configuration guidance covers the selected
  playbook instructions/examples, validator hints, design-control guidance and
  generic CWE knowledge-base criteria. Ordinary policies, payload data, TOML and
  JSON remain data with executable interpretation represented separately.
- `prompt_conversion_units.json` identifies converted paragraphs, nested items,
  examples and structured decision blocks with source ranges and hashes.
  `prompt_conversion_manifest.json` ties source and generated view hashes together.
- `source_detail/` Markdown prompt files now contain the actual conversion;
  Python/config/shell views link to converted content. `coverage.tsv`,
  `source_index.md`, prompt asset/location indexes and `source_links.tsv` incorporate
  the prompt layer. `assets/original/` and `.evidence.json` remain supporting evidence.
- No identified instruction-bearing production content is intentionally left as
  verbatim evidence alone. Tests/fixtures are excluded from this production scope.
  Unknown runtime files, library-generated text and external implementation
  behavior remain outside the supplied-source conversion, not silently inferred.

### Abstraction, hierarchy and dynamic supply

The baseline already supports natural-language constraints, conditional expressions,
`while` and natural `for each`. No grammar extension was needed. Source spellings
are reused; `prompt_vocabulary.tsv` documents existing-vocabulary lookups before
recording additional prompt identifiers, metadata values and field/pattern terms.
The corresponding records are included in `vocabulary_extensions.md`.

Paragraphs, source headings and nested lists retain their grouping. Thirty-nine
hand-authored structured views supplement complex source procedures and gates;
they describe the same instructions, not additional execution passes. Unspecified
order remains unspecified. Mandatory language, soft preferences, prohibitions and
permission to choose tools retain their source force. Prompt predicates remain
qualitative where the source is qualitative, including “genuinely”, “when unsure”,
“plausible” and “exhausted”. No new numerical cutoff replaces them.

`prompt_workflow.sudo.md` maps optional S1 scope triage, S2 modeling/planning, S4
investigation/skill supply, S6 verification and nested EV, S7 collapse, S8 chaining,
S10 remediation and S11 validation into the existing harness hierarchy. Executable
assembly and dispatch remain in `source_detail/`; the prompt layer describes what
the model is asked to do, not a guarantee it complied. Tool availability,
requested tool use, explicit model choice and actual host invocation are separate.

Dynamic f-string expressions retain expression order, conversions and format specs;
format-call evidence preserves placeholder bindings. Source-detail code retains
branch-selected clauses, slices, joins, optional values and call arguments.
Runtime substitutions and model-selected tool calls are unresolved rather than
invented. Conservative conversion of diagnostic/feedback text is explicitly
conditional on model exposure where no definite delivery edge is established.

### Review anchors and preserved tensions

| Source | Converted location | What was compared |
|---|---|---|
| `skills/*/SKILL.md` | Mirrored prompt/source-detail views; first structured block in each | All seventeen skills' roles, priority searches, gates, exceptions, probe rules, FP criteria, evidence/output and stopping rules; the exploration inventory/read/pagination procedure and other lenses remain distinct |
| `validation/prompts/system.md`, three persona Markdown files, two rule files and scoring skill | Mirrored prompt views | Requested parent order and parallel tasks, report completeness/retry, persona expertise, four gates, synthesis, exact weights/caps/rounding/bands, secret and output handling |
| `pipeline/stages/s1_autoexclude.py:_SYSTEM` | Prompt view, production-scope block | Exclusion categories, NEVER EXCLUDE categories, uncertainty and YAML-only response versus executable overlay vetting |
| `pipeline/stages/s2/prompts.py:SYSTEM` | Prompt view, threat-model block | Ordered stages, per-boundary STRIDE, baseline traces, inventory subtraction, per-file class breadth and object-only schema |
| `pipeline/stages/s4/prompts.py` | Prompt view, breadth/budget blocks; existing source detail | Four ordered passes inside the same agent, budgeted lookups/outcome request, selected skill/graph/planning clauses and source inclusion |
| `pipeline/stages/s6/prompts.py` | Prompt view, second-opinion block | Per-finding method/verdict, confidence guidance, exclusions, correction versus optional reframing, repeats/extras, optional trait/graph duties and CVSS |
| `pipeline/stages/s7/prompts.py`, `s8/prompts.py` | Prompt views, collapse/chaining blocks | One-fix criterion, CWE sibling exception, local index/independent_sites; feeds versus evidenced chains, sparse ranking, capability-changing steps and summary last |
| `exploit_verification/verify/prompt.py`, `judge.py`, `executor/tool.py`, `auth.py` | Mirrored prompt views and workflow map | Probe restrictions, measured authentication, method choices, consequence-driven stopping, property versus mechanism, benign/control/second-identity gates, ordered JSON fields and old/new re-check |
| `remediation_agent/prompts.py`, `playbook.py`, plugin helper/runner | Prompt views and workflow map | Three gates, policy/strategy insertion, parent read-only plan, fixer current-byte read, statuses, one retry for retryable tool_error and host postgates |
| `skills/__init__.py`, validation `_loader.py`, session `rules.py`/`launcher.py` | Workflow map with executable links | Temporary skill supply/cleanup, metadata/tool narrowing, suffix/rules order, capability branches and system-file selection |
| `inputs/*.yaml`, `rules/generic.kb.yaml` | Four guidance views; remaining resources in ledger | Per-CWE/strategy selection, hint patterns, sanitizer/non-sanitizer/FP criteria and reference code; inactive playbook root prompt_template is converted without asserting it is dispatched |

The following remain source tensions, not repaired behavior:

- Crypto repeats a criterion; log-injection's introduction says two classes but
  supplies A/B/C. Repetition/class headings remain visible.
- Ordinary CSRF gates coexist with an explicit unauthenticated exemption case;
  template constant-input gates coexist with an emptied-expression exception and
  an unfinished source criterion. No missing continuation is invented.
- Injection's empty-probe stop differs from SSRF's explicit instruction to continue.
  The exploration skill's inventory/EOF completion rule is not substituted for
  either. Source-specific gates are not merged because they sound similar.
- S6 excludes vulnerable third-party versions while other source prompts mention
  reviewing vulnerable dependencies. Stage-specific scope is retained.
- Validation-scoring requests a real-secret grep whereas adversarial rules forbid
  literal secrets in tool arguments. Both are represented; no secret search ran.
- Validation's two-persona-agreement and disagreement-conservative clauses can
  overlap. The conversion records both rather than inventing a tie-break.
- Agent-scoring/Jira language exists beside launcher capability branches asking
  schema reports/host synthesis. Source assembly order and executable scoring are
  recorded without asserting a universal conflict-resolution priority.
- The exploit judge first treats deterministic signals as confirmation unless
  contradicted, and later says they are the excluded benign explanation and to
  answer exploited. Both formulations remain, alongside property/rendering gates.

### Actual verification and remaining uncertainty

`prompt_verification.json` records checks for source/view hashes, citation ranges,
Markdown instruction-line coverage, complete maximal-carrier triage, source-detail
integration, new links, vocabulary record completeness and current coverage roles.
`verification.json` and `audit_results.json` retain independent structural,
expression, resource and source/output checks. The final run of all three check
commands returned passed with zero errors. Prompt checks covered 3,293 converted
units, all 1,761 substantive Markdown content lines, 181 knowledge-base criteria,
27,792 maximal carrier sites and 4,106 prompt vocabulary records. The command sequence above
regenerates the current result without importing or running harness code.

The manual comparisons are the families/decision blocks listed above, not a claim
that every generated sentence across every Python module received an independent
manual semantic audit. Keyword/context triage is conservative and does not prove
absence of every possible indirect model exposure. External dependency behavior,
unavailable runtime prompt files, actual substitutions and actual model compliance
remain unresolved. These are evidence limits; no model agreement, generated output,
runtime scan or fabricated test result is offered as proof of correctness.
