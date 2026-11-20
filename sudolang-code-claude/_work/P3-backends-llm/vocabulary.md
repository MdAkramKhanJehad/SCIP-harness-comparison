# Vocabulary: P3-backends-llm

New names in `vvah/vvaharness/backends/llm/` that are neither source identifiers nor in the shared table of `_work/BRIEF.md`. Harvested from every output file in the area (pass-1 and pass-2).

### Constants
- Definition: interface block that groups a module's module-level constant assignments, with their values, under one `// src:` range.
- Why needed: the source declares these as loose module-level names; one block lets one pointer cover them and puts threshold values in one place.
- Kind: general harness concept
- Original source term or wording: none (module-level `NAME = value` assignments)
- Source references: vvaharness/backends/llm/cache.py:25-34, vvaharness/backends/llm/tls.py:30-34, vvaharness/backends/llm/tools.py:28-41, vvaharness/backends/llm/agent_sdk.py:44-49, vvaharness/backends/llm/openai_responses.py:46-59
- Used in: vvah/vvaharness/backends/llm/cache.sudo, tls.sudo, tools.sudo, agent_sdk.sudo, openai_responses.sudo

### OpenAiConfig defaults
- Definition: the starting values of the module's `_cfg` dictionary, whose type is the source's `OpenAiConfig`.
- Why needed: names the block of initial configuration values ("defaults" is added to the source type name).
- Kind: tool-specific identifier
- Original source term or wording: `_cfg: OpenAiConfig = {...}`
- Source references: vvaharness/backends/llm/openai.py:240-242
- Used in: vvah/vvaharness/backends/llm/openai.sudo

### SdkConfig defaults
- Definition: the starting values of the module's `_cfg` dictionary, whose type is the source's `SdkConfig`.
- Why needed: names the block of initial configuration values ("defaults" is added to the source type name).
- Kind: tool-specific identifier
- Original source term or wording: `_cfg: SdkConfig = {...}`
- Source references: vvaharness/backends/llm/sdk.py:129-143
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

### OPENAI_FORCED_FINAL_SUBMIT
- Definition: prompt interface for the user message `openai.agentic()` appends when the turn cap is reached and a response_model is set; it tells the model to call the submit tool.
- Why needed: the source builds it inline as `instruction` with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: f"Tool budget exhausted. Call `{RESPONSE_MODEL_TOOL_NAME}` now with what you have established so far; it is the only way to reply."
- Source references: vvaharness/backends/llm/openai.py:2069-2071
- Used in: vvah/vvaharness/backends/llm/openai.sudo

### OPENAI_FORCED_FINAL_TEXT
- Definition: prompt interface for the forced-final user message on the openai route when no response_model is set (reply in prose, call no tools).
- Why needed: inline string with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: "Tool budget exhausted. Reply now with your final answer based on what you have read so far; do not call tools."
- Source references: vvaharness/backends/llm/openai.py:2073-2074
- Used in: vvah/vvaharness/backends/llm/openai.sudo

### OPENAI_SUBMIT_REJECTED_RESULT
- Definition: prompt interface for the tool-result text sent back to the model when its emit_structured_response arguments fail validation on the openai route.
- Why needed: inline f-string with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: f"Rejected: {str(exc)[:600]}. Fix the named fields and call the tool again."
- Source references: vvaharness/backends/llm/openai.py:2015-2016
- Used in: vvah/vvaharness/backends/llm/openai.sudo

### SDK_FORCED_FINAL_SUBMIT
- Definition: prompt interface for the user message appended on the sdk route when the turn cap is reached and a response_model is set; asks the model to call emit_structured_response now.
- Why needed: inline prompt text with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: "Tool budget exhausted. Call emit_structured_response now with your best answer based on what you have read so far."
- Source references: vvaharness/backends/llm/sdk.py:1571-1578
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

### SDK_FORCED_FINAL_TEXT
- Definition: prompt interface for the user message appended on the sdk route when the turn cap is reached and no response_model is set.
- Why needed: inline prompt text with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: "Tool budget exhausted. Reply now with your final answer based on what you have read so far; do not call any tool."
- Source references: vvaharness/backends/llm/sdk.py:1579-1586
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

### SDK_SUBMIT_REJECTED_RESULT
- Definition: prompt interface for the tool result sent back when an emit_structured_response submit fails schema validation on the sdk route.
- Why needed: inline model-facing text with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: f"Rejected: {str(exc)[:600]}. Fix the named fields and call the tool again."
- Source references: vvaharness/backends/llm/sdk.py:1518-1523
- Used in: vvah/vvaharness/backends/llm/sdk.sudo

### JSON_SCHEMA_FALLBACK_SUFFIX
- Definition: prompt interface for the text appended to the user prompt when the installed `claude` build lacks `--json-schema`, asking for only a schema-conforming JSON object.
- Why needed: inline f-string with no constant name; the conventions need an interface name for a prompt.
- Kind: tool-specific identifier
- Original source term or wording: f"{user_prompt}\n\nRespond with ONLY a JSON object conforming to this JSON Schema:\n{json.dumps(json_schema)}"
- Source references: vvaharness/backends/llm/cli/oneshot.py:86-89
- Used in: vvah/vvaharness/backends/llm/cli/oneshot.sudo

### deny / allow (PreToolUse decisions)
- Definition: helper verbs for the hook result `permissionDecision: "deny"` with a reason, and `"allow"` with an updatedInput.
- Why needed: shorten the nested hookSpecificOutput dictionaries without losing the decision.
- Kind: tool-specific identifier
- Original source term or wording: `_deny(reason)` and the inline allow dictionary
- Source references: vvaharness/backends/llm/agent_sdk.py:161-166, 191-195
- Used in: vvah/vvaharness/backends/llm/agent_sdk.sudo

### trim
- Definition: helper verb for removing leading and trailing whitespace from model text.
- Why needed: renders Python `str.strip()` in plain words.
- Kind: general harness concept
- Original source term or wording: `.strip()`
- Source references: vvaharness/backends/llm/sdk.py, deepagents.py, agent_sdk.py (text returned to the caller)
- Used in: vvah/vvaharness/backends/llm/sdk.sudo, deepagents.sudo, agent_sdk.sudo
