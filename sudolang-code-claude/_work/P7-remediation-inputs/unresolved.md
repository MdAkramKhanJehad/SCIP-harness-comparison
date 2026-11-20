# Unresolved — P7-remediation-inputs

No `// unresolved:` markers were written in this area. Every behaviour was settled from the source; calls into other packages are marked `// external:` (vvaharness/models finalize and FindingCase, orchestrator/checkpoints, orchestrator/artifacts, backends/harness deepagents, backends/llm/registry agentic, pipeline/stages/s9/typed_sarif, report/redact).

Limits of verification (not unresolved behaviour):
- Pass-1 files `frameworks.sudo`, `provenance.sudo`, `render.sudo`, `rule_paths.sudo`, `models/*.sudo` were checked for pointer ranges and key claims against the source; their prose was not rewritten.
- `artifacts/writer.sudo` condenses the diff-redaction state machine (writer.py:38-96, 131-330) with `// abstracted:`; it changes only what is persisted.

Grammar: nothing here needed a grammar change. Regular expressions are written as `/.../` literals inside assignments, which SudoLang does not define but reads as ordinary values.
