# Vocabulary: P2-backends-harness

### SubmitToolDescription
- Definition: Prompt interface for the tool description of the `SubmitPersonaReport` tool on the Claude route.
- Why needed: The description is an inline f-string in `_submit_tool`, with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: description argument of `@sdk_tool(SUBMIT_TOOL, ...)`
- Source references: vvaharness/backends/harness/claude/facts.py:125-129
- Used in: vvah/vvaharness/backends/harness/claude/facts.sudo

### SubmitInstruction
- Definition: Prompt interface for the one line `with_submit_instruction` appends to a system prompt, naming the structured-output tool as the only accepted reply.
- Why needed: The source builds this line inside a function and has no constant name for it.
- Kind: general harness concept
- Original source term or wording: with_submit_instruction ("When you have your final {response_model.__name__}, call the `{tool_name}` tool with it; a plain-text reply is not accepted.")
- Source references: vvaharness/backends/llm/models.py:165-174, vvaharness/backends/harness/deepagents/options/response_format.py:124-143
- Used in: vvah/vvaharness/backends/harness/deepagents/options/response_format.sudo

### stock read / stock grep / stock glob / stock ls / stock resolution
- Definition: The inherited deepagents FilesystemBackend method that a subclass calls through `super()` after its own check.
- Why needed: Shows where VVAH's own filter ends and the library's behaviour begins.
- Kind: general harness concept
- Original source term or wording: super().read(...), super().grep(...), super().glob(...), super().ls(...), super()._resolve_path(key)
- Source references: vvaharness/backends/harness/deepagents/options/filesystem.py:120, 158, 182, 195, 212
- Used in: vvah/vvaharness/backends/harness/deepagents/options/filesystem.sudo

### EvidenceGateNudge
- Definition: Prompt interface for the "HOLD." HumanMessage that replaces a premature verdict.
- Why needed: The source builds this message in function `_nudge`; it is not a named constant.
- Kind: tool-specific identifier
- Original source term or wording: `_nudge(outstanding)`
- Source references: vvaharness/backends/harness/deepagents/evidence_gate.py:65-77
- Used in: vvah/vvaharness/backends/harness/deepagents/evidence_gate.sudo

### HoldForVerdictRefusal
- Definition: Prompt interface for the refusal text that `hold_for_verdict` returns ("Rejected: you have not called any of ...").
- Why needed: The text is an inline string literal in the source.
- Kind: tool-specific identifier
- Original source term or wording: return value of `EvidenceGate.hold_for_verdict`
- Source references: vvaharness/backends/harness/deepagents/evidence_gate.py:152-162
- Used in: vvah/vvaharness/backends/harness/deepagents/evidence_gate.sudo

### ReachabilityItem
- Definition: Prompt interface for the extra outstanding item ("establish reachability from the call graph ...") added when no required graph tool was called.
- Why needed: The text is an inline string literal in `_premature`.
- Kind: tool-specific identifier
- Original source term or wording: inline literal in `EvidenceGate._premature`
- Source references: vvaharness/backends/harness/deepagents/evidence_gate.py:176-184
- Used in: vvah/vvaharness/backends/harness/deepagents/evidence_gate.sudo

### ReportNowMessage
- Definition: Prompt interface for the "Report your outcome NOW" HumanMessage that ForceVerdictOnly appends.
- Why needed: The source builds it in function `_report_now`.
- Kind: tool-specific identifier
- Original source term or wording: `_report_now(tool_names)`
- Source references: vvaharness/backends/harness/deepagents/force_verdict_only.py:48-54
- Used in: vvah/vvaharness/backends/harness/deepagents/force_verdict_only.sudo

### FinalTurnNotice
- Definition: Prompt interface for the "FINAL TURN." HumanMessage on the last call ModelCallBudget allows.
- Why needed: The source builds it in function `_final_turn_notice`.
- Kind: tool-specific identifier
- Original source term or wording: `_final_turn_notice(limit)`
- Source references: vvaharness/backends/harness/deepagents/model_call_budget.py:29-39
- Used in: vvah/vvaharness/backends/harness/deepagents/model_call_budget.sudo

### WithdrawnNotice
- Definition: Prompt interface for the one-time notice that ToolCallBudget appends when it withdraws the metered tools.
- Why needed: The source builds it in function `_withdrawn_notice`.
- Kind: tool-specific identifier
- Original source term or wording: `_withdrawn_notice(tool_names)`
- Source references: vvaharness/backends/harness/deepagents/tool_budget.py:83-89
- Used in: vvah/vvaharness/backends/harness/deepagents/tool_budget.sudo

### warn once per <key>
- Definition: Prose step for the source helper `warn_once(registry, key, text)`, which prints a warning the first time a key is seen in the process.
- Why needed: Keeps the once-only behaviour visible without rendering the registry sets.
- Kind: general harness concept
- Original source term or wording: `warn_once`
- Source references: evidence_gate.py:148-149, tool_budget.py:129-130, tool_choice_rejection.py:75-80, usage.py:97-105, client.py:197-202, tools.py:51-56
- Used in: deepagents/evidence_gate.sudo, tool_budget.sudo, tool_choice_rejection.sudo, usage.sudo, client.sudo, tools.sudo
