# Conversion notes

## Status and versions

**Partial: batch 1.** This delivery does not represent the entire harness.
Eleven Python modules (4,457 source lines) have a local semantic rendering in
1,476 lines of SudoLang/Markdown. This is a coverage statement, not a correctness
score. Imported code is not covered transitively. The file-level ledger covers
all 945 supplied files, including 109 vendored files and 271 test files.

- Conversion date: 2026-11-20, America/New_York (user session date).
- SudoLang: repository `https://github.com/paralleldrive/sudolang`, fetched from
  `main`, commit `dcef61ef253e389d02c72b67215cf97de5bdbbae`;
  specification title **SudoLang v2.0**. Local snapshot under `reference/sudolang/`.
- Harness: `visa-vulnerability-agentic-harness/pyproject.toml` declares
  **vvaharness 1.5.1**. This directory has no independent `.git` checkout.
  `git -C visa-vulnerability-agentic-harness rev-parse HEAD` resolves to the
  **parent comparison repository** commit
  `fe88503a680ccfbd7248cf32000e58cd7b796dbb`; it is not asserted to be the
  upstream Visa commit. That parent's commit date is 2026-11-17.
- Current-file SHA-256 hashes in `coverage.tsv` identify the actual inspected
  working-tree versions, independently of the parent commit. The vendored
  `context_graph_sdk` tree is present; its code is pending review/conversion.

## Conversion instructions and revision record

The user requested all work under `sudolang-code-chatgpt/`, starting with full
reading of the supplied specification and every repository example, followed by
source-based pseudocode. The governing instructions are:

1. Use baseline grammar; add identifiers/vocabulary before considering grammar.
   Any real grammar extension needs a separate justified proposal.
2. Preserve source organization and stage/component/substep nesting, order,
   branches, call relationships and specified parallelism. Preserve gates,
   thresholds, cutoffs, loops, retries, termination, shared state and synchronization.
3. Include relevant code, prompts, configuration and available dependency code.
   Do not invent unavailable dependency behavior. Distinguish code-enforced
   action from instructions to a model and tools merely made available.
4. Give paths and line ranges per substantive block and per extracted prompt.
   Keep contradictions and unusual behavior rather than repairing them.
5. Record every added identifier/term, definition, reason, kind, source wording,
   references, use and reuse status in `vocabulary_extensions.md`. No supplied
   vocabulary extension was identified in this request.
6. Document versions, readings, coverage, choices, hierarchy, missing evidence and
   examples for manual review. Explicitly label batches and incomplete conversion.
7. Produce representation/documentation only; no flaw analysis, redesign or
   invented test results. Model agreement does not prove correctness.

Revision 1 establishes conventions and the first batch. During source review,
the four-tuple S7 fallback was kept despite the checkpoint facade's five/six-tuple
schema, graph creation was kept before the S0 stop, and the S4 gate's finite
rejection behavior was kept separate from the prompt's stronger wording.
Review revisions clarified scalar/default truthiness expressions, out-of-loop
gate behavior, batch call-limit scaling, empty S4 outcome maps, and cleanup scope.

The harness `AGENTS.md` was read completely. Its operating rules do not require
running a scan for this documentation task. No product source/configuration was
edited, no scan was performed, and EV/remediation were not invoked.

## Baseline reading and accessibility

Read the entire `sudolang.sudo.md` (417 lines), repository README, and all **26**
files under `examples/`, including `reflective-thought-composition.readme.md`.
`baseline_review.tsv` individually lists every path, line count, hash and reading
status. The examples include interfaces/state/commands, natural-language bodies,
conditionals, loops, composition, options, inferred functions, requirements and
mixed Markdown. The minimalist RTC example and older adventure syntax were read
without silently promoting their stylistic variations into new grammar.

The GitHub examples HTML page reported a loading error. A direct Git clone
succeeded, making all supplied specification/example files accessible locally.
**No supplied example remained inaccessible.** Linked videos/articles/share
chats are not repository examples and were not claimed as reviewed. No
SudoLang interpreter/conformance suite was invoked; baseline support is justified
by the read specification, not by model self-certification.

## Coverage and batches

`coverage.tsv` is authoritative per file. Status meanings:

| Status | Meaning |
|---|---|
| represented-local | Read and represented at this batch's abstraction; dependencies can remain pending |
| reviewed-context | Read for operating instructions/version/dependency context; no pseudocode rendering |
| copied-unreviewed | Exact configuration asset retained; semantic/effective-configuration conversion pending |
| pending | Available file inventoried and hashed; no semantic review/conversion claim |
| not-converted-tests | Test/fixture inventory only; not executed or treated as runtime behavior |

Batch 1 modules mirror their source paths:

- `orchestrator/entry.py`, `scan.py`, `checkpoints.py`.
- `pipeline/stages/s4_deepdive.py` and `s4/{batching,session,prompts,outcomes}.py`.
- `backends/harness/deepagents/{evidence_gate,tool_budget,model_call_budget}.py`.

Other statuses after this batch: 656 pending, 271 tests/fixtures not converted,
five profiles copied but unreviewed, two context documents read. The `default`
profile's opening portion was also read for context; no full profile-review
claim follows from that partial read.

Remaining work is organized as the following batches, **not yet completed**:

| Batch | Scope |
|---|---|
| 2 | CLI/API/SDK entrypoints, batch orchestration, trusted configuration merging, scope walk, graph build, vendored SDK, S0–S3 and auto-exclusion |
| 3 | S5 enrichment/detectors/gates, S6 static verification, S7 dedup, S8 chains, S9 SARIF, models and report/scoring |
| 4 | Route dispatch, permissions, native/fact tools, generic retry/deadline/replay, plugin/skill loading and all remaining backend middleware |
| 5 | EV collection/gates/probe/mapping/attack/judge/replay, remediation and validation trees including prompts, policies, tools and personas; remaining operational utilities/assets |

Test files are inventoried separately. Their assertions can later inform manual
checks but do not replace reading production behavior. Root governance/docs,
scripts and build metadata remain classified individually in the ledger.

## Abstraction choices and hierarchy

The representation does not execute the user's target or emulate a model.
Source functions keep their identities; Python classes become SudoLang
interfaces with described method behavior. Import/license boilerplate, repeated
console formatting and repetitive telemetry presentation are condensed.
Decision-relevant defaults, scope of exception handlers, counter-triggered gates,
checkpoint contents, and cleanup boundaries are retained. No new grammar is
necessary: natural-language statements within functions express executor futures,
async handlers, locks, transactional writes and on-exit cleanup.

The scan hierarchy remains nested:

1. `entry.main` parses/validates target and configuration, selects overlays,
   configures backends, resolves EV input and preflight, then dispatches batch or
   single scan. Batch internals are explicitly pending.
2. `scan_repo` establishes identity/state, prepares EV, optionally auto-excludes,
   sets progress/injectors, seeds S0 and rebuilds graph, then enters the protected
   S1–S11 sequence. Cleanup covers only the region after successful graph build.
3. S5/S6/S7 are nested inside the branch without a reusable S7 bundle; S5/S6
   checkpoint gates further nest within it. Legacy bundle handling remains beside
   this branch. Stage stops are left at their exact source positions.
4. S4 sorts units and removes empty work before choosing serial or parallel
   scheduling. Parallel execution partitions batches and then collects initial
   futures followed by singleton retries. Reassembly follows risk order.
5. Each S4 session owns its middleware/transcript, may take a deadline resume or
   replay path, reduces/repairs replies, caps and deduplicates findings. Batch
   outcome reduction stays per member, with CWE/repeat-site cross-product expansion.
6. Prompt building retains clause order and conditionally selected wording.
   The requested investigation passes are described inside the model request;
   they are not inserted as guaranteed host-executed stages.

`source_links.tsv` indexes every `// Source:` citation (56 initial blocks; later
edits regenerate this count). Prompt strings, schema descriptions, logs and
docstrings from represented files are extracted into `assets/<source>.strings.json`.
Each string has source start/end lines. F-strings additionally retain source
expressions, preserving interpolation rather than inventing rendered values.
Extraction preserves a superset of prompt evidence; it does not make every
literal a model instruction. No extraction imports or executes harness code.

All five shipped profile YAMLs are copied exactly under `assets/` with original
organization. They remain data evidence: configuration loader defaults, local/env
overlays and runtime route interpretation are not yet converted.

`vocabulary_extensions.md` contains a curated concept table and a per-module
symbol appendix generated from names actually appearing in the rendering.
The appendix retains bindings, fields, callables, qualified names and referenced
literal keys/status/counter/tool names, with local source excerpts and use sites.
It deliberately keeps module contexts separate, including repeated short names.
Source-derived local identifiers are newly recorded relative to the SudoLang
baseline, not newly invented harness concepts. Static binding excerpts anchor
their local meaning; imported implementations remain unresolved.

## Unresolved behavior and missing evidence

- The many **available but unconverted** modules are pending work, not inaccessible
  material. In particular, scope filters, S0–S3 planning, later-stage confidence
  thresholds, route-specific tool enforcement, actual replay behavior, remediation
  sandboxing and validation consensus cannot be inferred from this batch's callers.
- `with_injected_skills`, tool builders, model route registry, graph degeneracy
  predicate, `_cap_int`, JSON salvage, enum coercion, canonical keys, CWE
  normalization/equivalence and inventory path resolution are called here but
  their definitions are pending. Call-site arguments/defaults are preserved.
- Vendored `vendor/context_graph_sdk/` code is accessible and inventoried,
  **not yet semantically inspected**.
- Package metadata inspection in the converter's Python 3.12 environment found
  `openai 3.49.0`, `pydantic 2.14.3`, `httpx 0.28.1`. Their implementation source
  has not been reviewed; installed versions do not establish the harness's runtime
  environment. No project lockfile or `.venv` was found at the checked locations.
- `deepagents`, `langchain`, `langgraph`, `langchain-anthropic`,
  `langchain-openai`, `anthropic`, `claude-agent-sdk`, `tree-sitter` and
  `arcadedb-embedded` distribution metadata was absent from that interpreter.
  Their external implementations were not inspected or installed. Declared
  requirements in `pyproject.toml` are available; effective runtime package
  versions and library scheduling/retry/middleware details remain unresolved.
- Model outputs, provider behavior, graph extraction results and live HTTP
  outcomes were not observed. No scan/model-network/EV run or runtime test is claimed.

## Manual source-to-representation review

These comparisons were made against the cited production source. They are
manual checks, not proofs or downstream flaw assessments.

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

Remaining unverified: semantic completeness across unconverted files; actual
external middleware composition/order and source-runtime behavior; model compliance;
all runtime outcomes. No agreement between models was used as evidence.

## Bookkeeping verification

`tools/index_evidence.py` regenerates file hashes, source-link index, baseline
reading inventory, literal assets and symbol appendix. It is not a converter.
`tools/check_artifacts.py` verifies citation ranges, ledger hashes, asset identity,
baseline inventory and generated-file links, and reports structural results in
`verification.json`. Those checks establish artifact consistency only. See that
file for actual results; no harness test results are fabricated here.

No `language_extension_proposals.md` is created because no grammar extension was
needed for inspected behavior. This does not pre-judge the remaining batches.
