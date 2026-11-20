# P1-pipeline unresolved

- vvah/vvaharness/pipeline/stages/replay.sudo — whether resume_agentic can continue a session on routes other than deepagents — vvaharness/backends/llm/deepagents.py resume_agentic — resolved in final pass: only cli and deepagents resume; other vias raise SessionNotResumableError -> replay
- vvah/vvaharness/pipeline/stages/s4/session.sudo — whether build_graph_tool_builder yields callable tools when ctx.graph_handle is null — vvaharness/codegraph/tools.py — resolved in final pass: reader tools only; _graph_tools returns [] when graph_handle is null
- vvah/vvaharness/pipeline/stages/s4/session.sudo — exactly when resume_or_replay resumes and when it calls replay — the resume_or_replay body (stages/replay.py; not re-verified in pass 2) — resolved in final pass: always tries resume first; ModelRefusal re-raises, any other exception -> replay()
- vvah/vvaharness/pipeline/stages/s4/prompts.sudo — whether the shell tool itself enforces read-only commands — allow_shell handling in backends/llm/deepagents — resolved in final pass: no harness-side filter; execute is deepagents LocalShellBackend (external), read-only is prompt-only
- vvah/vvaharness/pipeline/stages/s4/prompts.sudo — whether a single-unit session's {"outcomes": [...]}-shaped reply parses in parse_outcome — extract_json behaviour — resolved in final pass: does not parse: extract_json returns the wrapper, validation fails, single-unit path repairs

The 22 files first checked only for declaration ranges were then reviewed line by line in a continuation of pass 2 (see coverage notes).

Grammar: none needed.
