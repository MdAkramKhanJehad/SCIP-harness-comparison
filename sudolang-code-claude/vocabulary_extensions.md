# Vocabulary extensions

Every term or identifier this representation introduces beyond the SudoLang baseline (specification v2.0, `paralleldrive/sudolang` commit `dcef61e`). Source identifiers (function, class, constant and configuration names kept exactly as in `vvaharness`) are **not** listed. They come from the harness, not from this rendering.

**None of these entries changes the SudoLang language.** Each is a user-defined identifier, a field name, or a comment convention, used inside constructs the specification already defines: interfaces, functions with modifiers, `require`/`warn`, `Constraints`, `constraint Name { }` and comments. Grammar changes would be recorded in `language_extension_proposals.md`. None were adopted, so that file does not exist (see `conversion_notes.md`, "Grammar decisions").

**Status of every entry:** no vocabulary extension was supplied with the task, so every entry is *newly introduced*. None is reused from a supplied extension.

The document has two parts:
1. Shared vocabulary: terms defined once, before the batch conversion, and used across the whole tree (`_work/BRIEF.md`, `CONVENTIONS.md`).
2. Area vocabulary: terms introduced while rendering one area. These were harvested by each batch from every output file in its area and copied here unchanged. The heading of each part names its batch.

Paths under "Source references" are relative to `visa-vulnerability-agentic-harness/`. Paths under "Used in" are relative to this folder.

## Part 1: shared vocabulary

| Term | Definition and intended meaning | Why needed | Kind | Original source term | Source references | Used in |
|---|---|---|---|---|---|---|
| `:executor=code\|model\|mixed` | Function modifier (SudoLang modifier syntax `fn():key=value`) saying who carries out the body. `code` means plain Python. `model` means the work of a model, steered only by instructions. `mixed` means code builds the call and checks the result while a model does the reasoning. | The central distinction for analysis: enforced behaviour versus behaviour requested of a model. | general harness concept | none (implicit in the Python) | every module; for example `vvaharness/pipeline/stages/s4/session.py` | every `.sudo` function |
| `callModel({ role, route, system, prompt, tools, limits, output })` | One model invocation made by the code. `role` is the configured model role. `route` is the backend (`cli`, `sdk`, `openai`, `deepagents`) or `resolve_model(knob("models.<role>")).via`. `tools` are the tools *offered*. `limits` are turn, token, time or budget caps. `output` is the expected shape. | The source spreads model calls across four backends with different wrappers. One name makes every model call findable and states what is offered without claiming that any tool is used. | general harness concept | `agentic(...)`, `oneshot(...)`, backend `run`/`query` calls | `vvaharness/backends/llm/registry.py`, `vvaharness/backends/llm/*.py` | stage, remediation, validation and exploit-verification files |
| `runConcurrently(items, workers=n, fn):order=completion\|input` | Parallel execution the source performs (thread pool or asyncio gather). `order` is the order in which results are consumed. | SudoLang has no parallel construct. This keeps parallelism visible without adding synchronization. | general harness concept | `ThreadPoolExecutor`, `as_completed`, `asyncio.gather` | for example `vvaharness/pipeline/stages/s4_deepdive.py`, `s6_verify.py`, `orchestrator/batch.py` | stages 4, 6, 7, batch, exploit-verification executor |
| `knob("dotted.key", default=v)` | A configuration read, with the default that applies at that read site. | Thresholds and toggles must be traceable to configuration keys. Defaults differ between read sites. | tool-specific identifier | `vvaharness.util.config.knob`, `getattr(cfg.stepN, "...", d)` | `vvaharness/util/config.py`, `vvaharness/config/__init__.py` | throughout |
| `constraint OnEveryExit { ... }` | Cleanup that runs on every exit from a function. | Keeps `try/finally` and context-manager cleanup visible without inventing control flow. | general harness concept | `try ... finally`, `with` blocks | for example `vvaharness/orchestrator/scan.py:591-592, 1067-1072` | scan, stage and backend files |
| `// src: path:a-b`, `// prompt-src: path:a-b` | Traceability pointers to the source lines a block represents, and to the lines of prompt text. | Required for review against the source. Checked mechanically by `tools/check_rendering.py`. | general harness concept | n/a | n/a | every substantive block |
| `// unresolved: ...; missing evidence: ...` | Behaviour that cannot be determined from the available material. | Requirement not to invent behaviour. | general harness concept | n/a | n/a | 1 place (see `conversion_notes.md`, section 7) |
| `// preserved: ...` | Source behaviour that is contradictory or surprising, kept as is. | Requirement to keep oddities rather than correct them. | general harness concept | n/a | n/a | 267 places |
| `// external: ...` | A call outside the rendered scope (third-party library, `vendor/`, live network targets). | Marks where behaviour depends on code that is not represented. | general harness concept | n/a | n/a | 129 places |
| `// abstracted: ...` | Source lines condensed, with what was condensed and why it is safe. Never used to hide a branch, threshold, gate, retry or model instruction. | The abstraction level asked for. Makes every condensation reviewable. | general harness concept | n/a | n/a | 190 places |
| `require <condition> => <reaction>` | A code-performed check whose failure leads to something other than a throw, for example returning an error string or skipping an item. | Combines the specification's `require` with the arrow form of semantic pattern matching (`vector-search.sudo`). This is a usage of existing constructs, not new grammar. | general harness concept | `if not ...: return ...` | throughout | throughout |
| "x, or, when absent, y" / "(a.b if a exists, else null)" | Wording for an absent-key fallback and for safe attribute access. | Pass-2 drafts used the non-SudoLang operators `??` and `?.`. These were rewritten in natural language rather than adding operators. | general harness concept | Python `d.get(k, default)`, `x or default`, `getattr(x, "a", None)` | throughout | exploit verification, validation, config, report and backend files |
| `// source: subclass of X` | Records Python exception inheritance as a comment on an empty interface. | The SudoLang lint prohibits `extends` and `inherit`. | general harness concept | `class E(X)` | for example `vvaharness/validation/case_api.py`, `vvaharness/exploit_verification/errors.py` | validation, exploit verification |

## Part 2: area vocabulary

Note on overlap: `Role` (batch P7) and `role` (batch P9) name the same concept, a field holding a prompt's quoted persona sentence. The case differs only because they were written in different areas. Batch P8 groups `Role`, `Directive`, `FocusAreas` and similar section-block names in one entry with the same meaning for `Role`. Interface names such as `Constants` (a group of module-level constants under one pointer) appear in several areas with the same meaning and are defined where first recorded. Batch P10 (exploit verification core) introduced no names beyond the shared vocabulary.


### Batch P1-pipeline

Harvest is complete for the 22 files verified or written in pass 2. The 22 `partial` files were not harvested line by line.

#### resolve_model
- Definition: resolves a configured model role to its backend route; `.via` is the route name.
- Why needed: avoids a clash with the generic word "resolve" in pseudocode.
- Kind: tool-specific identifier
- Original source term or wording: `resolve` (imported from `vvaharness.backends.llm.registry`)
- Source references: vvaharness/pipeline/stages/s6/session.py:99, 179, 291; vvaharness/pipeline/stages/s4/session.py (several)
- Used in: vvah/vvaharness/pipeline/stages/s6/session.sudo, s6_verify.sudo, s4/session.sudo, s2/session.sudo, s2/__init__.sudo, s1_autoexclude.sudo

#### floors (callModel limits key)
- Definition: the minimum-response floors (characters, tokens) that the code sets around one model call with `stage_floors`.
- Why needed: `callModel` has no slot for the response-quality floor wrapper.
- Kind: general harness concept
- Original source term or wording: `with stage_floors(tag, min_chars=..., min_tokens=...)`
- Source references: vvaharness/pipeline/stages/s6/session.py:260, 339-340
- Used in: vvah/vvaharness/pipeline/stages/s6/session.sudo

#### then "..." followed by $x (prompt layout phrase)
- Definition: inside a prompt's `Constraints`, means a literal separator line followed by a slot appended after the instructions.
- Why needed: shows how the prompt is built, not something the model is asked to do.
- Kind: general harness concept
- Original source term or wording: `"\n\n--- ORIGINAL REPLY ---\n{raw}"`
- Source references: vvaharness/pipeline/stages/s6/prompts.py:383
- Used in: vvah/vvaharness/pipeline/stages/s6/prompts.sudo, s4/session.sudo

#### _ROLE, _VERDICT_CLAUSE, ... (s6 prompt fragment interfaces)
- Definition: prompt interfaces named after the source constants. They are source identifiers and are listed here only so readers can find them.
- Why needed: not a new name.
- Kind: tool-specific identifier
- Original source term or wording: the same names
- Source references: vvaharness/pipeline/stages/s6/prompts.py:23-229
- Used in: vvah/vvaharness/pipeline/stages/s6/prompts.sudo

#### S8_USER_PROMPT
- Definition: interface for the Stage 8 user prompt returned by `build_prompt` (repository, design controls, known CVEs, fact blocks, finding blocks, evidence rules).
- Why needed: the source builds it as an f-string with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: return value of `build_prompt`
- Source references: vvaharness/pipeline/stages/s8/prompts.py:223-264
- Used in: vvah/vvaharness/pipeline/stages/s8/prompts.sudo, vvah/vvaharness/pipeline/stages/s8/session.sudo

#### Constants, VetoSets
- Definition: grouping interfaces for the module constants and the veto sets of auto-exclude.
- Why needed: groups module-level constants into one block each.
- Kind: general harness concept
- Original source term or wording: module-level constants
- Source references: vvaharness/pipeline/stages/s1_autoexclude.py:97-122, 303-335
- Used in: vvah/vvaharness/pipeline/stages/s1_autoexclude.sudo

#### S1_AUTOEXCLUDE_USER_PROMPT
- Definition: interface for the inline auto-exclude user prompt.
- Why needed: the source builds it as an unnamed f-string.
- Kind: tool-specific identifier
- Original source term or wording: inline f-string
- Source references: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
- Used in: vvah/vvaharness/pipeline/stages/s1_autoexclude.sudo

#### constraint StageFloors
- Definition: constraint naming the `stage_floors` context manager scope.
- Why needed: renders a context manager whose exit matters.
- Kind: tool-specific identifier
- Original source term or wording: `stage_floors`
- Source references: vvaharness/pipeline/stages/s1_autoexclude.py:658-663
- Used in: vvah/vvaharness/pipeline/stages/s1_autoexclude.sudo

#### MINIMUM_BASELINE_BLOCK
- Definition: interface for the prompt block built in `_baseline_block`.
- Why needed: the source builds it as an unnamed f-string.
- Kind: tool-specific identifier
- Original source term or wording: return value of `_baseline_block`
- Source references: vvaharness/pipeline/stages/s2/prompts.py:221-239
- Used in: vvah/vvaharness/pipeline/stages/s2/prompts.sudo


### Batch P2-backends-harness

#### SubmitToolDescription
- Definition: Prompt interface for the tool description of the `SubmitPersonaReport` tool on the Claude route.
- Why needed: The description is an inline f-string in `_submit_tool`, with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: description argument of `@sdk_tool(SUBMIT_TOOL, ...)`
- Source references: vvaharness/backends/harness/claude/facts.py:125-129
- Used in: vvah/vvaharness/backends/harness/claude/facts.sudo

#### SubmitInstruction
- Definition: Prompt interface for the one line `with_submit_instruction` appends to a system prompt, naming the structured-output tool as the only accepted reply.
- Why needed: The source builds this line inside a function and has no constant name for it.
- Kind: general harness concept
- Original source term or wording: with_submit_instruction ("When you have your final {response_model.__name__}, call the `{tool_name}` tool with it; a plain-text reply is not accepted.")
- Source references: vvaharness/backends/llm/models.py:165-174, vvaharness/backends/harness/deepagents/options/response_format.py:124-143
- Used in: vvah/vvaharness/backends/harness/deepagents/options/response_format.sudo

#### stock read / stock grep / stock glob / stock ls / stock resolution
- Definition: The inherited deepagents FilesystemBackend method that a subclass calls through `super()` after its own check.
- Why needed: Shows where VVAH's own filter ends and the library's behaviour begins.
- Kind: general harness concept
- Original source term or wording: super().read(...), super().grep(...), super().glob(...), super().ls(...), super()._resolve_path(key)
- Source references: vvaharness/backends/harness/deepagents/options/filesystem.py:120, 158, 182, 195, 212
- Used in: vvah/vvaharness/backends/harness/deepagents/options/filesystem.sudo

#### EvidenceGateNudge
- Definition: Prompt interface for the "HOLD." HumanMessage that replaces a premature verdict.
- Why needed: The source builds this message in function `_nudge`; it is not a named constant.
- Kind: tool-specific identifier
- Original source term or wording: `_nudge(outstanding)`
- Source references: vvaharness/backends/harness/deepagents/evidence_gate.py:65-77
- Used in: vvah/vvaharness/backends/harness/deepagents/evidence_gate.sudo

#### HoldForVerdictRefusal
- Definition: Prompt interface for the refusal text that `hold_for_verdict` returns ("Rejected: you have not called any of ...").
- Why needed: The text is an inline string literal in the source.
- Kind: tool-specific identifier
- Original source term or wording: return value of `EvidenceGate.hold_for_verdict`
- Source references: vvaharness/backends/harness/deepagents/evidence_gate.py:152-162
- Used in: vvah/vvaharness/backends/harness/deepagents/evidence_gate.sudo

#### ReachabilityItem
- Definition: Prompt interface for the extra outstanding item ("establish reachability from the call graph ...") added when no required graph tool was called.
- Why needed: The text is an inline string literal in `_premature`.
- Kind: tool-specific identifier
- Original source term or wording: inline literal in `EvidenceGate._premature`
- Source references: vvaharness/backends/harness/deepagents/evidence_gate.py:176-184
- Used in: vvah/vvaharness/backends/harness/deepagents/evidence_gate.sudo

#### ReportNowMessage
- Definition: Prompt interface for the "Report your outcome NOW" HumanMessage that ForceVerdictOnly appends.
- Why needed: The source builds it in function `_report_now`.
- Kind: tool-specific identifier
- Original source term or wording: `_report_now(tool_names)`
- Source references: vvaharness/backends/harness/deepagents/force_verdict_only.py:48-54
- Used in: vvah/vvaharness/backends/harness/deepagents/force_verdict_only.sudo

#### FinalTurnNotice
- Definition: Prompt interface for the "FINAL TURN." HumanMessage on the last call ModelCallBudget allows.
- Why needed: The source builds it in function `_final_turn_notice`.
- Kind: tool-specific identifier
- Original source term or wording: `_final_turn_notice(limit)`
- Source references: vvaharness/backends/harness/deepagents/model_call_budget.py:29-39
- Used in: vvah/vvaharness/backends/harness/deepagents/model_call_budget.sudo

#### WithdrawnNotice
- Definition: Prompt interface for the one-time notice that ToolCallBudget appends when it withdraws the metered tools.
- Why needed: The source builds it in function `_withdrawn_notice`.
- Kind: tool-specific identifier
- Original source term or wording: `_withdrawn_notice(tool_names)`
- Source references: vvaharness/backends/harness/deepagents/tool_budget.py:83-89
- Used in: vvah/vvaharness/backends/harness/deepagents/tool_budget.sudo

#### warn once per <key>
- Definition: Prose step for the source helper `warn_once(registry, key, text)`, which prints a warning the first time a key is seen in the process.
- Why needed: Keeps the once-only behaviour visible without rendering the registry sets.
- Kind: general harness concept
- Original source term or wording: `warn_once`
- Source references: evidence_gate.py:148-149, tool_budget.py:129-130, tool_choice_rejection.py:75-80, usage.py:97-105, client.py:197-202, tools.py:51-56
- Used in: deepagents/evidence_gate.sudo, tool_budget.sudo, tool_choice_rejection.sudo, usage.sudo, client.sudo, tools.sudo


### Batch P3-backends-llm

New names in `vvah/vvaharness/backends/llm/` that are neither source identifiers nor in the shared table of `_work/BRIEF.md`. Harvested from every output file in the area (pass-1 and pass-2).

#### Constants
- Definition: interface block that groups a module's module-level constant assignments, with their values, under one `// src:` range.
- Why needed: the source declares these as loose module-level names; one block lets one pointer cover them and puts threshold values in one place.
- Kind: general harness concept
- Original source term or wording: none (module-level `NAME = value` assignments)
- Source references: vvaharness/backends/llm/cache.py:25-34, vvaharness/backends/llm/tls.py:30-34, vvaharness/backends/llm/tools.py:28-41, vvaharness/backends/llm/agent_sdk.py:44-49, vvaharness/backends/llm/openai_responses.py:46-59
- Used in: vvah/vvaharness/backends/llm/cache.sudo, tls.sudo, tools.sudo, agent_sdk.sudo, openai_responses.sudo

#### OpenAiConfig defaults
- Definition: the starting values of the module's `_cfg` dictionary, whose type is the source's `OpenAiConfig`.
- Why needed: names the block of initial configuration values ("defaults" is added to the source type name).
- Kind: tool-specific identifier
- Original source term or wording: `_cfg: OpenAiConfig = {...}`
- Source references: vvaharness/backends/llm/openai.py:240-242
- Used in: vvah/vvaharness/backends/llm/openai.sudo

#### SdkConfig defaults
- Definition: the starting values of the module's `_cfg` dictionary, whose type is the source's `SdkConfig`.
- Why needed: names the block of initial configuration values ("defaults" is added to the source type name).
- Kind: tool-specific identifier
- Original source term or wording: `_cfg: SdkConfig = {...}`
- Source references: vvaharness/backends/llm/sdk.py:129-143
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

#### OPENAI_FORCED_FINAL_SUBMIT
- Definition: prompt interface for the user message `openai.agentic()` appends when the turn cap is reached and a response_model is set; it tells the model to call the submit tool.
- Why needed: the source builds it inline as `instruction` with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: f"Tool budget exhausted. Call `{RESPONSE_MODEL_TOOL_NAME}` now with what you have established so far; it is the only way to reply."
- Source references: vvaharness/backends/llm/openai.py:2069-2071
- Used in: vvah/vvaharness/backends/llm/openai.sudo

#### OPENAI_FORCED_FINAL_TEXT
- Definition: prompt interface for the forced-final user message on the openai route when no response_model is set (reply in prose, call no tools).
- Why needed: inline string with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: "Tool budget exhausted. Reply now with your final answer based on what you have read so far; do not call tools."
- Source references: vvaharness/backends/llm/openai.py:2073-2074
- Used in: vvah/vvaharness/backends/llm/openai.sudo

#### OPENAI_SUBMIT_REJECTED_RESULT
- Definition: prompt interface for the tool-result text sent back to the model when its emit_structured_response arguments fail validation on the openai route.
- Why needed: inline f-string with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: f"Rejected: {str(exc)[:600]}. Fix the named fields and call the tool again."
- Source references: vvaharness/backends/llm/openai.py:2015-2016
- Used in: vvah/vvaharness/backends/llm/openai.sudo

#### SDK_FORCED_FINAL_SUBMIT
- Definition: prompt interface for the user message appended on the sdk route when the turn cap is reached and a response_model is set; asks the model to call emit_structured_response now.
- Why needed: inline prompt text with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: "Tool budget exhausted. Call emit_structured_response now with your best answer based on what you have read so far."
- Source references: vvaharness/backends/llm/sdk.py:1571-1578
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

#### SDK_FORCED_FINAL_TEXT
- Definition: prompt interface for the user message appended on the sdk route when the turn cap is reached and no response_model is set.
- Why needed: inline prompt text with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: "Tool budget exhausted. Reply now with your final answer based on what you have read so far; do not call any tool."
- Source references: vvaharness/backends/llm/sdk.py:1579-1586
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

#### SDK_SUBMIT_REJECTED_RESULT
- Definition: prompt interface for the tool result sent back when an emit_structured_response submit fails schema validation on the sdk route.
- Why needed: inline model-facing text with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: f"Rejected: {str(exc)[:600]}. Fix the named fields and call the tool again."
- Source references: vvaharness/backends/llm/sdk.py:1518-1523
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

#### JSON_SCHEMA_FALLBACK_SUFFIX
- Definition: prompt interface for the text appended to the user prompt when the installed `claude` build lacks `--json-schema`, asking for only a schema-conforming JSON object.
- Why needed: inline f-string with no constant name; the conventions need an interface name for a prompt.
- Kind: tool-specific identifier
- Original source term or wording: f"{user_prompt}\n\nRespond with ONLY a JSON object conforming to this JSON Schema:\n{json.dumps(json_schema)}"
- Source references: vvaharness/backends/llm/cli/oneshot.py:86-89
- Used in: vvah/vvaharness/backends/llm/cli/oneshot.sudo

#### deny / allow (PreToolUse decisions)
- Definition: helper verbs for the hook result `permissionDecision: "deny"` with a reason, and `"allow"` with an updatedInput.
- Why needed: shorten the nested hookSpecificOutput dictionaries without losing the decision.
- Kind: tool-specific identifier
- Original source term or wording: `_deny(reason)` and the inline allow dictionary
- Source references: vvaharness/backends/llm/agent_sdk.py:161-166, 191-195
- Used in: vvah/vvaharness/backends/llm/agent_sdk.sudo

#### trim
- Definition: helper verb for removing leading and trailing whitespace from model text.
- Why needed: renders Python `str.strip()` in plain words.
- Kind: general harness concept
- Original source term or wording: `.strip()`
- Source references: vvaharness/backends/llm/sdk.py, deepagents.py, agent_sdk.py (text returned to the caller)
- Used in: vvah/vvaharness/backends/llm/sdk.sudo, deepagents.sudo, agent_sdk.sudo


### Batch P4-orchestrator-cli-sdk

#### ScanArgs
- Definition: interface listing the `vvaharness scan` command-line options and their defaults
- Why needed: argparse builds an untyped namespace with no source class name
- Kind: tool-specific identifier
- Original source term or wording: `build_parser()` / `args`
- Source references: vvaharness/orchestrator/entry.py:140-223
- Used in: vvah/vvaharness/orchestrator/entry.sudo

#### PROBE_PING_PROMPT
- Definition: prompt interface for the literal "ping" sent by the connectivity probe
- Why needed: the prompt is an inline literal, not a named constant
- Kind: tool-specific identifier
- Original source term or wording: `_probe("ping", ...)`
- Source references: vvaharness/orchestrator/preflight.py:781
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

#### DEEPAGENTS_PROBE_PROMPT
- Definition: prompt interface for "reply with the single word ok"
- Why needed: inline literal
- Kind: tool-specific identifier
- Original source term or wording: `run_oneshot("reply with the single word ok", ...)`
- Source references: vvaharness/orchestrator/preflight.py:716
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

#### CLI_BRIDGE_PROMPT
- Definition: prompt interface for the instruction to call the echo tool through the CLI MCP bridge
- Why needed: inline f-string
- Kind: tool-specific identifier
- Original source term or wording: `f"Call the {_PROBE_BRIDGE_TOOL_NAME} tool with marker='{nonce}', ..."`
- Source references: vvaharness/orchestrator/preflight.py:641-642
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

#### "preflight" (callModel role label)
- Definition: role label for probe calls made by preflight, which are not tied to one configured pipeline role
- Why needed: callModel requires a role; the probe calls run outside any stage
- Kind: general harness concept
- Original source term or wording: preflight probe functions (_probe_deepagents_harness, CLI bridge probe)
- Source references: vvaharness/orchestrator/preflight.py:641-642, 716
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

#### put
- Definition: the nested helper inside _install_agents that writes one agent file unless it already exists or has a symlinked ancestor (POSIX only)
- Why needed: nested function with no module-level name (source name kept)
- Kind: tool-specific identifier
- Original source term or wording: `def put(path, content, *, anchor)` nested in `_install_agents`
- Source references: vvaharness/cli/_setup.py:96-108
- Used in: vvah/vvaharness/cli/_setup.sudo

#### PluginContract
- Definition: the plugin contract and seams the SDK README states
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:1-46
- Used in: vvah/vvaharness/sdk/README.sudo.md

#### FailureContract
- Definition: the README's statement of how plugin failures and SDK bounds affect a scan
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:97-115
- Used in: vvah/vvaharness/sdk/README.sudo.md

#### RemediateAndValidate
- Definition: the README's statements about sdk.remediate and sdk.validate
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:117-143
- Used in: vvah/vvaharness/sdk/README.sudo.md

#### Limitations
- Definition: the README's current-limitations section
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:145-161
- Used in: vvah/vvaharness/sdk/README.sudo.md

#### SemgrepReferenceVariant
- Definition: the README's summary of the Semgrep reference plugin and its bounds
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:163-206
- Used in: vvah/vvaharness/sdk/README.sudo.md

#### RunningGuide
- Definition: the README's statements about sdk.scan
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:208-224
- Used in: vvah/vvaharness/sdk/README.sudo.md

#### HandoffGuide
- Definition: the README's guidance for inject_findings, distinct from the source dataclass Handoff
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:226-325
- Used in: vvah/vvaharness/sdk/README.sudo.md


### Batch P5-config-rules-report

#### Options blocks named after profile sections (`Options models`, `Options transport`, `Options caching`, `Options reasoning`, `Options entries`, `Options weights`, `Options keywords`, `Options validators`, `Options shapes`, `Options sniff_patterns`)
- Definition: grouping labels for data rendered as SudoLang `Options`; `transport`, `caching`, `reasoning` group top-level profile keys (sdk/openai/cli; cache_*; think_in_prompt); the others group module constants.
- Why needed: data files and constant tables have no function or interface name in the source.
- Kind: general harness concept
- Original source term or wording: YAML top-level keys / module-level constants
- Source references: vvaharness/config/profiles/default.yaml:71-108,424-429; vvaharness/report/cvss.py:20-54; vvaharness/report/appcontext.py:36-78; vvaharness/report/redact.py:28-112; vvaharness/lang/detect.py:157-206; vvaharness/rules/generic.kb.yaml:20
- Used in: vvah/vvaharness/config/profiles/*.sudo.md, vvah/vvaharness/report/{cvss,appcontext,redact}.sudo, vvah/vvaharness/lang/detect.sudo, vvah/vvaharness/rules/generic.kb.sudo.md

#### absent (profile value)
- Definition: in a difference-only profile rendering, the key exists in default.yaml but not in this profile.
- Why needed: the difference convention for the four non-default profiles.
- Kind: general harness concept
- Original source term or wording: key missing from YAML
- Source references: vvaharness/config/profiles/sdk.yaml, taint.yaml
- Used in: vvah/vvaharness/config/profiles/{sdk,taint}.sudo.md

#### Slot
- Definition: the merged per-CWE record inside CweKB._by_cwe (cwe, title, origin, five lists); aliases share the same Slot object.
- Why needed: the source uses an anonymous dict named `slot`.
- Kind: tool-specific identifier
- Original source term or wording: `slot`
- Source references: vvaharness/rules/__init__.py:139-155
- Used in: vvah/vvaharness/rules/__init__.sudo

#### mask (helper inside _redact_impl)
- Definition: count a label, optionally remember the value, return a placeholder sentinel.
- Why needed: shorter name for the nested `_mask` closure.
- Kind: tool-specific identifier
- Original source term or wording: `_mask`
- Source references: vvaharness/report/redact.py:309-320
- Used in: vvah/vvaharness/report/redact.sudo


### Batch P6-models-detect-evidence

#### FindingCase.with_attempt / FindingCase.with_verdict / FindingCase.read / FindingCase.write (dotted method form)
- Definition: a method of a source class written as `Interface.method` because SudoLang has no class construct.
- Why needed: CONVENTIONS forbid `class`; the dotted name keeps the source method name searchable.
- Kind: general harness concept
- Original source term or wording: methods `with_attempt`, `with_verdict`, `read`, `write` of class `FindingCase`; `missing_from` of `ScoringPolicy`
- Source references: vvaharness/models/case.py:78-110, vvaharness/models/context.py:53-59
- Used in: vvah/vvaharness/models/case.sudo, vvah/vvaharness/models/context.sudo

#### coercion (comment label)
- Definition: comment label for a pydantic `field_validator`/`model_validator(mode="before")` or an enumeration `_missing_` hook that rewrites an input value before validation instead of rejecting it.
- Why needed: these hooks change what is stored (null to empty string, gate name normalised, unknown label to a fail-closed member) but are not checks, so they are not `require`.
- Kind: general harness concept
- Original source term or wording: `_none_to_empty`, `_canonical_name`, `_drop_derived`, `_missing_`
- Source references: vvaharness/models/gates.py:36-40, vvaharness/models/gates.py:55-59, vvaharness/models/case.py:70-76, vvaharness/models/vocab.py:56-60, 92-101, 142-148, 160-166
- Used in: vvah/vvaharness/models/gates.sudo, vvah/vvaharness/models/case.sudo, vvah/vvaharness/models/vocab.sudo

#### first N of X
- Definition: the first N items (or characters) of a list or string; used instead of `X[0..N]` because SudoLang ranges are inclusive.
- Why needed: Python slices `x[:n]` are exclusive; an inclusive range would misstate caps by one.
- Kind: general harness concept
- Original source term or wording: `x[:n]`
- Source references: vvaharness/models/scan/context.py:63-107, vvaharness/detect/matcher.py:73, vvaharness/models/scan/threat.py:338,346
- Used in: vvah/vvaharness/models/scan/context.sudo, threat.sudo, _sections_chain.sudo, vvah/vvaharness/detect/matcher.sudo

#### RenderBlocks / ExclusionDefaults
- Definition: grouping interfaces that collect a module's renderer functions (evidence/render.py) or its default exclusion constants (scope/walk.py).
- Why needed: groups many one-line source definitions under one pointer.
- Kind: general harness concept
- Original source term or wording: none (module-level definitions)
- Source references: vvaharness/evidence/render.py:21-91, vvaharness/scope/walk.py:33-68
- Used in: vvah/vvaharness/evidence/render.sudo, vvah/vvaharness/scope/walk.sudo

#### description (in tool interfaces)
- Definition: the model-facing tool description, quoted from the tool function's docstring.
- Why needed: tools are rendered as interfaces; the docstring is what the model sees.
- Kind: general harness concept
- Original source term or wording: `@tool` docstring
- Source references: vvaharness/codegraph/tools.py:149-263, vvaharness/plugins/semgrep/tools.py:75-108
- Used in: vvah/vvaharness/codegraph/tools.sudo, vvah/vvaharness/plugins/semgrep/tools.sudo


### Batch P7-remediation-inputs

Only non-source names are listed. Interface names for prompts in this area are source constants or functions (`SYSTEM`, `FIXER_SYSTEM`, `ORCHESTRATOR_SYSTEM`, `build_user`, `_verdict_extraction_prompt`, `Strategy.as_prompt_block`), so they are not new.

#### Template
- Definition: a field inside a prompt interface holding the literal text skeleton of a prompt assembled by code, with `$variable` slots.
- Why needed: the per-finding user prompt and the playbook strategy block are built by f-strings; the skeleton shows exactly what the model receives.
- Kind: general harness concept
- Original source term or wording: f-string return value of `build_user`, `as_prompt_block`
- Source references: vvaharness/remediation_agent/prompts.py:197-207, vvaharness/remediation_agent/playbook.py:52-64
- Used in: vvah/vvaharness/remediation_agent/prompts.sudo, vvah/vvaharness/remediation_agent/playbook.sudo

#### Role
- Definition: a field inside a system-prompt interface holding the opening identity paragraph of the prompt, quoted exactly.
- Why needed: separates the persona sentence from the rule list in `Constraints`.
- Kind: general harness concept
- Original source term or wording: first paragraph of each system prompt ("You are ...")
- Source references: vvaharness/remediation_agent/prompts.py:26-29, 83-84, 110-111
- Used in: vvah/vvaharness/remediation_agent/prompts.sudo

#### Termination summary
- Definition: a closing comment block that states the loop bounds derived from a guard's state machine (number of dispatches, malformed refusals).
- Why needed: the fixer loop has no explicit loop statement; its bound is spread across state fields.
- Kind: general harness concept
- Original source term or wording: none (derived from `_attempts`, `_malformed_rejections`, `_terminal`)
- Source references: vvaharness/remediation_agent/plugin_runner/handoff.py:64-145
- Used in: vvah/vvaharness/remediation_agent/plugin_runner/handoff.sudo

#### Options blocks in input files
- Definition: in `vvah/inputs/*.sudo.md`, an `Options { ... }` block lists the decisive keys and values of a data file; per-CWE playbook entries are condensed to strategy names with their line ranges.
- Why needed: data files have no functions; the gates read these values.
- Kind: general harness concept
- Original source term or wording: YAML/JSON/CSV keys as in the files
- Source references: inputs/remediation_policy.yaml:32-85, inputs/remediation_playbook.yaml:39-406
- Used in: vvah/inputs/*.sudo.md


### Batch P8-validation

New names in `vvah/vvaharness/validation/**` that are not source identifiers and not in the shared table of `_work/BRIEF.md`.

#### ArtifactNames
- Definition: grouping interface for the artifact file and directory name constants.
- Why needed: groups related module-level constants into one interface block.
- Kind: tool-specific identifier
- Original source term or wording: "Single source of truth for artifact names, DTO layout, and runtime environment keys."
- Source references: vvaharness/validation/constants/artifacts.py:24-33
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

#### EnvironmentNames
- Definition: grouping interface for the VVAHARNESS_* environment-variable name constants.
- Why needed: groups module constants and separates the inert names from the ones that are read.
- Kind: tool-specific identifier
- Original source term or wording: "Only ENV_CLAUDE_BINARY/ENV_GHE_* are read (config.settings._EnvScalars); the rest are inert names"
- Source references: vvaharness/validation/constants/artifacts.py:69-86
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

#### SessionEnvironmentNames
- Definition: grouping interface for the environment names set on the launched validation session.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: "Agent-session environment contract (set on the launched validation session)."
- Source references: vvaharness/validation/constants/artifacts.py:88-99
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

#### AgentDefaults
- Definition: grouping interface for the DEFAULT_* agent runtime values.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: "Default agent runtime values (mirror AgentConfig defaults in config.settings)."
- Source references: vvaharness/validation/constants/artifacts.py:127-140
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

#### DiffMarkers
- Definition: grouping interface for the diff-parsing regular expression and marker constants.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: "Constants for deterministic diff-based fact tools."
- Source references: vvaharness/validation/constants/diff.py:26-43
- Used in: vvah/vvaharness/validation/constants/diff.sudo

#### TestFileNames
- Definition: grouping interface for the test-file naming rules.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: PY_TEST_EXACT_NAMES, PY_TEST_NAME_PREFIX, PY_TEST_NAME_SUFFIX, JS_TEST_SUFFIXES
- Source references: vvaharness/validation/constants/test_inventory.py:19-25
- Used in: vvah/vvaharness/validation/constants/test_inventory.sudo

#### console:
- Definition: helper verb meaning "write this line to stderr through vvaharness.util.console.write"; it stops nothing and is not a logger warning.
- Why needed: keeps operator-facing console lines apart from `warn`, which is used for logger warnings.
- Kind: general harness concept
- Original source term or wording: console.write(...)
- Source references: vvaharness/validation/ingest/case_loader.py:84-87; vvaharness/validation/cli/__init__.py:73,264-267; vvaharness/validation/cli/_run.py:189-311; vvaharness/validation/cli/_model.py:95-123; vvaharness/validation/report/augment.py:248-250
- Used in: vvah/vvaharness/validation/ingest/case_loader.sudo, ingest/workspace.sudo, cli/__init__.sudo, cli/_run.sudo, cli/_model.sudo, report/augment.sudo

#### VALIDATION_LAUNCH_PROMPT
- Definition: interface for the user-turn prompt that `build_launch_prompt` assembles.
- Why needed: the prompt is built line by line in code, with no source constant.
- Kind: tool-specific identifier
- Original source term or wording: build_launch_prompt / "launch prompt"
- Source references: vvaharness/validation/session/launch_prompt.py:99-127
- Used in: vvah/vvaharness/validation/session/launch_prompt.sudo, vvah/vvaharness/validation/session/launcher.sudo

#### VALIDATION_SYNTHESIS_SECTION
- Definition: interface for the "## Synthesis boundary" text added to the system prompt; the backend decides which version is used.
- Why needed: the source returns this text from a function, not a constant.
- Kind: tool-specific identifier
- Original source term or wording: _synthesis_section
- Source references: vvaharness/validation/session/launcher.py:374-394
- Used in: vvah/vvaharness/validation/session/launcher.sudo

#### VALIDATION_RULES_SECTION
- Definition: interface for the "## Rules" text added to the system prompt; it either points to `.claude/rules/` or includes the rules in full.
- Why needed: the source returns this text from a function, not a constant.
- Kind: tool-specific identifier
- Original source term or wording: _rules_section
- Source references: vvaharness/validation/session/launcher.py:353-366
- Used in: vvah/vvaharness/validation/session/launcher.sudo

#### VALIDATION_SYSTEM_PROMPT
- Definition: the text of `prompts/system.md`, the base of the orchestrator's system prompt.
- Why needed: gives a name to a Markdown file's contents.
- Kind: tool-specific identifier
- Original source term or wording: SYSTEM_PROMPT_FILENAME "system.md"
- Source references: vvaharness/validation/prompts/system.md:16-154; vvaharness/validation/session/launcher.py:397-409; vvaharness/validation/constants/artifacts.py:150
- Used in: vvah/vvaharness/validation/prompts/system.sudo.md, vvah/vvaharness/validation/session/launcher.sudo

#### SECURITY_ARCHITECT_PROMPT / PENETRATION_TESTER_PROMPT / CROSS_REPO_ANALYZER_PROMPT
- Definition: interfaces for the body (system prompt) of each reviewer-persona `.md` file.
- Why needed: the prompts are Markdown files with no source constant name.
- Kind: tool-specific identifier
- Original source term or wording: subagent names "security-architect", "penetration-tester", "cross-repo-analyzer"
- Source references: vvaharness/validation/subagents/security-architect.md:35-98; vvaharness/validation/subagents/penetration-tester.md:35-99; vvaharness/validation/subagents/cross-repo-analyzer.md:35-122
- Used in: vvah/vvaharness/validation/subagents/*.sudo.md

#### ADVERSARIAL_REVIEW_RULES / SCORING_MATRIX_RULES / VALIDATION_SCORING_SKILL
- Definition: interfaces for the two rules files and the skill file given to the validation session.
- Why needed: the files have no source constant name (the code refers to them through ADVERSARIAL_RULES / SCORING_RULES file-name constants).
- Kind: tool-specific identifier
- Original source term or wording: "Adversarial Review Rules", "Scoring Matrix", "Validation Scoring Skill"
- Source references: vvaharness/validation/claude_config/rules/adversarial-review.md:16-68; vvaharness/validation/claude_config/rules/scoring-matrix.md:16-200; vvaharness/validation/claude_config/skills/validation-scoring/SKILL.md:22-86
- Used in: vvah/vvaharness/validation/claude_config/rules/*.sudo.md, vvah/vvaharness/validation/claude_config/skills/validation-scoring/SKILL.sudo.md

#### Prompt section blocks
- Definition: named sub-blocks inside a prompt interface that mirror the Markdown headings of the source prompt: Role, Directive, FocusAreas, AntiManipulation, Inputs, Tools, FieldNotes, Guardrails, PersonaIsolation, SynthesisRules, EvidenceRequirements, SecretExposureEvidence, SignalToNoise, ScoringReference, Rules, Criteria, StatusMultipliers, DecisionThresholds, MergeReadiness, ScoringExecution, InputAndOutputSchema, SessionMarkers, JiraStatusTransitions, CodeLevelSignalsOnly, SecretExposureVerification, SecretExposureGateMapping, RotationAttestation, SecretExposureVerdict, SecretExposureAuditLine. All contain model-facing text only (like Constraints).
- Why needed: keeps the section structure of long prompts traceable to their headings.
- Kind: general harness concept
- Original source term or wording: the Markdown section headings ("## Directive", "## Focus Areas", "## Anti-Manipulation", and so on)
- Source references: the prompt files listed in the three entries above, and vvaharness/validation/prompts/system.md
- Used in: vvah/vvaharness/validation/prompts/system.sudo.md, subagents/*.sudo.md, claude_config/rules/*.sudo.md, claude_config/skills/validation-scoring/SKILL.sudo.md

#### capture_transcript
- Definition: function name for the body of the Stop-hook shell script.
- Why needed: a shell script has no function name; the file name is used.
- Kind: tool-specific identifier
- Original source term or wording: capture_transcript.sh
- Source references: vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:16-35
- Used in: vvah/vvaharness/validation/claude_config/hooks/logging/capture_transcript.sudo

#### SessionCall
- Definition: the validation session written as one `callModel(...)`.
- Why needed: shows the role, tools, subagents and limits of the one orchestrator call in one place.
- Kind: general harness concept
- Original source term or wording: StreamingOptions plus harness.run_streaming
- Source references: vvaharness/validation/session/launcher.py:299-345, 620-631
- Used in: vvah/vvaharness/validation/session/launcher.sudo

#### $findingDetails / $orchestratorRulesText
- Definition: template slots for the finding-details block and for the full rules text.
- Why needed: placeholders for text that helper functions build.
- Kind: tool-specific identifier
- Original source term or wording: _append_finding_details, orchestrator_rules_text()
- Source references: vvaharness/validation/session/launch_prompt.py:81-96; vvaharness/validation/session/rules.py:41-43
- Used in: vvah/vvaharness/validation/session/launch_prompt.sudo, vvah/vvaharness/validation/session/launcher.sudo

#### offer
- Definition: `offer X(args) => body` means a tool is built and made available to the model, not that it is called.
- Why needed: keeps building a tool separate from calling it.
- Kind: general harness concept
- Original source term or wording: @tool def ...; tools.append(...)
- Source references: vvaharness/validation/tools/deep_tools.py:37-90
- Used in: vvah/vvaharness/validation/tools/deep_tools.sudo


### Batch P9-skills-util

Shell helpers (`scan`, `scan2`, `count`, `hits`, `flist`, `nlist`, `files`, `sec`, `emit`, `norm`, `dedup`, `tgrep`, `sgrep`, `tpl_files`) and util names are source identifiers and are not listed.

#### AccessControlLens
- Definition: prompt interface for the `access-control` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Access Control Lens"; frontmatter name "access-control"
- Source references: vvaharness/skills/access-control/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/access-control/SKILL.sudo.md

#### BatchEtlLens
- Definition: prompt interface for the `batch-etl` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Batch Etl Lens"; frontmatter name "batch-etl"
- Source references: vvaharness/skills/batch-etl/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/batch-etl/SKILL.sudo.md

#### ClientSideLens
- Definition: prompt interface for the `client-side` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Client-Side Lens"; frontmatter name "client-side"
- Source references: vvaharness/skills/client-side/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/client-side/SKILL.sudo.md

#### ExhaustiveRepositoryExploration
- Definition: prompt interface for the `code-exploration` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Exhaustive Repository Exploration"; frontmatter name "code-exploration"
- Source references: vvaharness/skills/code-exploration/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/code-exploration/SKILL.sudo.md

#### CryptoLens
- Definition: prompt interface for the `crypto` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Crypto Lens"; frontmatter name "crypto"
- Source references: vvaharness/skills/crypto/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/crypto/SKILL.sudo.md

#### CsrfLens
- Definition: prompt interface for the `csrf` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Csrf Lens"; frontmatter name "csrf"
- Source references: vvaharness/skills/csrf/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/csrf/SKILL.sudo.md

#### DeserializationLens
- Definition: prompt interface for the `deserialization` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Deserialization Lens"; frontmatter name "deserialization"
- Source references: vvaharness/skills/deserialization/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/deserialization/SKILL.sudo.md

#### HardcodedCredsLens
- Definition: prompt interface for the `hardcoded-creds` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Hardcoded Creds Lens"; frontmatter name "hardcoded-creds"
- Source references: vvaharness/skills/hardcoded-creds/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/hardcoded-creds/SKILL.sudo.md

#### IacLens
- Definition: prompt interface for the `iac` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Iac Lens"; frontmatter name "iac"
- Source references: vvaharness/skills/iac/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/iac/SKILL.sudo.md

#### InjectionLens
- Definition: prompt interface for the `injection` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Injection Lens"; frontmatter name "injection"
- Source references: vvaharness/skills/injection/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/injection/SKILL.sudo.md

#### LogInjectionLens
- Definition: prompt interface for the `log-injection` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Log Injection Lens"; frontmatter name "log-injection"
- Source references: vvaharness/skills/log-injection/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/log-injection/SKILL.sudo.md

#### LogicBugLens
- Definition: prompt interface for the `logic-bug` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Logic Bug Lens"; frontmatter name "logic-bug"
- Source references: vvaharness/skills/logic-bug/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/logic-bug/SKILL.sudo.md

#### AbsentControlLens
- Definition: prompt interface for the `missing-controls` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Absent-Control Lens"; frontmatter name "missing-controls"
- Source references: vvaharness/skills/missing-controls/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/missing-controls/SKILL.sudo.md

#### SensitiveDataLens
- Definition: prompt interface for the `sensitive-data` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Sensitive Data Lens"; frontmatter name "sensitive-data"
- Source references: vvaharness/skills/sensitive-data/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/sensitive-data/SKILL.sudo.md

#### SiblingInstanceSweep
- Definition: prompt interface for the `sibling-instances` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Sibling-Instance Sweep"; frontmatter name "sibling-instances"
- Source references: vvaharness/skills/sibling-instances/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/sibling-instances/SKILL.sudo.md

#### SsrfLens
- Definition: prompt interface for the `ssrf` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "SSRF Lens"; frontmatter name "ssrf"
- Source references: vvaharness/skills/ssrf/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/ssrf/SKILL.sudo.md

#### TemplateViewLayerLens
- Definition: prompt interface for the `templates` skill file given to a model
- Why needed: a SKILL.md has no source constant name; the interface needs one
- Kind: tool-specific identifier
- Original source term or wording: Markdown heading "Template and View-Layer Lens"; frontmatter name "templates"
- Source references: vvaharness/skills/templates/SKILL.md:1-22
- Used in: vvah/vvaharness/skills/templates/SKILL.sudo.md

#### ClassAHardGate
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "CLASS A HARD GATE"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/log-injection/SKILL.sudo.md

#### ClassBHardGate
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "CLASS B HARD GATE"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/log-injection/SKILL.sudo.md

#### ClassC
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "CLASS C — Plaintext Credentials in Logs"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/log-injection/SKILL.sudo.md

#### CsrfExemptException
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "EXPLICIT @csrf_exempt EXCEPTION"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/csrf/SKILL.sudo.md

#### EmptiedExpressions
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "Emptied expressions are still sinks"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/templates/SKILL.sudo.md

#### EnumerateBeforeConcluding
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "Enumerate before you conclude"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/missing-controls/SKILL.sudo.md

#### EnumerationRule
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "ENUMERATION RULE" section
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/client-side/SKILL.sudo.md, vvah/vvaharness/skills/code-exploration/SKILL.sudo.md, vvah/vvaharness/skills/csrf/SKILL.sudo.md, vvah/vvaharness/skills/injection/SKILL.sudo.md, vvah/vvaharness/skills/ssrf/SKILL.sudo.md, vvah/vvaharness/skills/templates/SKILL.sudo.md

#### FalsePositiveDiscipline
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "False-positive discipline"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/missing-controls/SKILL.sudo.md

#### FollowTheEdges
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "4. Follow the edges"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/code-exploration/SKILL.sudo.md

#### HardGate
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "HARD GATE" / "Hard gate" section
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/access-control/SKILL.sudo.md, vvah/vvaharness/skills/batch-etl/SKILL.sudo.md, vvah/vvaharness/skills/client-side/SKILL.sudo.md, vvah/vvaharness/skills/code-exploration/SKILL.sudo.md, vvah/vvaharness/skills/csrf/SKILL.sudo.md, vvah/vvaharness/skills/deserialization/SKILL.sudo.md, vvah/vvaharness/skills/hardcoded-creds/SKILL.sudo.md, vvah/vvaharness/skills/iac/SKILL.sudo.md, vvah/vvaharness/skills/injection/SKILL.sudo.md, vvah/vvaharness/skills/logic-bug/SKILL.sudo.md, vvah/vvaharness/skills/missing-controls/SKILL.sudo.md, vvah/vvaharness/skills/sensitive-data/SKILL.sudo.md, vvah/vvaharness/skills/ssrf/SKILL.sudo.md, vvah/vvaharness/skills/templates/SKILL.sudo.md

#### InvertedPolarity
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "Polarity: ... findings when EMPTY" section
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/iac/SKILL.sudo.md, vvah/vvaharness/skills/sensitive-data/SKILL.sudo.md

#### OpaqueFetchHelper
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "THE SHAPE WE MISS MOST — an opaque fetch helper"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/ssrf/SKILL.sudo.md

#### ReadToTheEnd
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "3. READ TO THE END"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/code-exploration/SKILL.sudo.md

#### Refutations
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "FP CHECKS" section
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/code-exploration/SKILL.sudo.md, vvah/vvaharness/skills/ssrf/SKILL.sudo.md

#### ReportCoverage
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "Report coverage honestly" / "The inventory decides when you are done"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/code-exploration/SKILL.sudo.md

#### SeverityRules
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "SEVERITY RULES"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/hardcoded-creds/SKILL.sudo.md

#### WhenThisApplies
- Definition: named constraint block grouping one section of rules asked of the model
- Why needed: gives a reusable name to a Markdown section of model instructions
- Kind: general harness concept
- Original source term or wording: "When this applies"
- Source references: the matching section of each SKILL.md listed in Used in
- Used in: vvah/vvaharness/skills/sibling-instances/SKILL.sudo.md

#### ControlCatalogue
- Definition: interface listing the absent-control families and where each belongs
- Why needed: groups seven sub-sections of reference rules
- Kind: tool-specific identifier
- Original source term or wording: "The controls, and where each belongs"
- Source references: vvaharness/skills/missing-controls/SKILL.md:58-121
- Used in: vvah/vvaharness/skills/missing-controls/SKILL.sudo.md

#### enumerate
- Definition: model-executed procedure: build and check the inventory before reading
- Why needed: the numbered procedure is a step sequence for the model
- Kind: general harness concept
- Original source term or wording: "1. Enumerate before you read"
- Source references: vvaharness/skills/code-exploration/SKILL.md:75-110
- Used in: vvah/vvaharness/skills/code-exploration/SKILL.sudo.md

#### sweep
- Definition: model-executed sibling-instance sweep procedure
- Why needed: numbered model procedure
- Kind: general harness concept
- Original source term or wording: "The sweep"
- Source references: vvaharness/skills/sibling-instances/SKILL.md:37-53
- Used in: vvah/vvaharness/skills/sibling-instances/SKILL.sudo.md

#### traceStoredPath
- Definition: model-executed procedure tracing a stored XSS source across files
- Why needed: numbered model procedure
- Kind: general harness concept
- Original source term or wording: "The stored path: sink and source are in different files"
- Source references: vvaharness/skills/templates/SKILL.md:74-84
- Used in: vvah/vvaharness/skills/templates/SKILL.sudo.md

#### role
- Definition: field holding the quoted persona sentence of a lens
- Why needed: separates the persona line from the rules
- Kind: general harness concept
- Original source term or wording: "You are a ... expert."
- Source references: line 24 of each SKILL.md that has one
- Used in: access-control, batch-etl, csrf, deserialization, hardcoded-creds, log-injection, sensitive-data SKILL.sudo.md

#### probe
- Definition: function standing for a whole shell probe script (top level of the script)
- Why needed: shell scripts have no entry function name
- Kind: general harness concept
- Original source term or wording: `sh .vvaharness/skills/<lens>/probe.sh [root]`
- Source references: each vvaharness/skills/*/probe.sh
- Used in: vvah/vvaharness/skills/*/probe.sudo (8 files)

#### inventory
- Definition: block naming the embedded python3 inventory section of the client-side probe
- Why needed: the heredoc has no name
- Kind: tool-specific identifier
- Original source term or wording: "== INVENTORY / FILES OF INTEREST =="
- Source references: vvaharness/skills/client-side/probe.sh:69-118
- Used in: vvah/vvaharness/skills/client-side/probe.sudo


### Batch P10-ev-core

none

Every interface, constant and function name in the P10 output files is a source identifier (for example `_SYSTEM`, `TELL_DOC`, `_REMEDIATION_SYSTEM`, `_ATTACK_PATH_SCHEMA`, `Verdict`, `ReproDetail`) or a shared name from `_work/BRIEF.md` (`callModel`, `runConcurrently`, `knob`, `constraint OnEveryExit`, the markers). Model roles in `callModel({ role: ... })` are written as the source configuration paths `exploit_verification.classify`, `exploit_verification.judge`, `exploit_verification.attacker`.


### Batch P11-ev-exec

#### targetSlots / perEndpointMax / endpointSlots
- Definition: state of `ConcurrencyLimiter`: the whole-target bounded semaphore, the per-endpoint cap, and the map of per-endpoint semaphores.
- Why needed: readable names for private attributes inside a `State` block.
- Kind: tool-specific identifier
- Original source term or wording: `self._target`, `self._per_endpoint_max`, `self._endpoint`
- Source references: vvaharness/exploit_verification/executor/concurrency.py:26-31
- Used in: vvah/vvaharness/exploit_verification/executor/concurrency.sudo

#### now_monotonic()
- Definition: the monotonic clock read (`time.monotonic()`).
- Why needed: distinguishes the monotonic clock from wall-clock `now()` in rate-limit, nonce and self-test timing.
- Kind: general harness concept
- Original source term or wording: `time.monotonic()`
- Source references: vvaharness/exploit_verification/executor/ratelimit.py:33-35, vvaharness/exploit_verification/executor/oob.py:84,152
- Used in: vvah/vvaharness/exploit_verification/executor/ratelimit.sudo, vvah/vvaharness/exploit_verification/executor/oob.sudo

#### _default_runner user prompt
- Definition: interface for the user message the finding-map runner builds (located endpoints plus findings, as JSON).
- Why needed: the prompt is an inline expression, not a named constant.
- Kind: tool-specific identifier
- Original source term or wording: `user = ("Located endpoints:\n" + ...)` in `_default_runner`
- Source references: vvaharness/exploit_verification/mapping/finding_map.py:289-294
- Used in: vvah/vvaharness/exploit_verification/mapping/finding_map.sudo

#### author's note (template comment block)
- Definition: the YAML file's leading comment, reproduced as a `/* */` block; it is documentation, never sent to a model or read by code.
- Why needed: the templates' comments state each payload set's intent and oracle tell; kept so a reader sees the author's stated purpose.
- Kind: general harness concept
- Original source term or wording: leading `#` comments in each `payloads/templates/*.yaml`
- Source references: vvaharness/exploit_verification/payloads/templates/*.yaml (comment lines after the license header)
- Used in: vvah/vvaharness/exploit_verification/payloads/templates/*.sudo.md (15 files)
