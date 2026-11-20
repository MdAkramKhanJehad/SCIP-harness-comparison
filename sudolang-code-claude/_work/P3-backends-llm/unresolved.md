# Unresolved: P3-backends-llm

- vvah/vvaharness/backends/llm/deepagents.sudo — exact conversion from `max_turns` to the LangGraph recursion limit (the source comment says "+900", "40 ≈ 470 turns") — missing evidence: `vvaharness/backends/harness/deepagents/` (outside this area) — resolved in final pass: recursion_limit = (max_turns or 50) + 900 on streaming, +5 one-shot (limits.py, streaming.py:141)

No other `// unresolved:` markers in the area. All source files were readable. Nothing needs a SudoLang grammar change.

Notes:
- The batch prompt said `cli/__init__.py` "has logic". On reading, lines 14-279 are only `from ... import` lines and an `__all__` list, so it is skipped as re-exports only.
- `deepagents.sudo` contains a route-comparison table that cites `sdk.py` and `openai.py`; its pointers were checked, its prose claims about those routes only partly.
