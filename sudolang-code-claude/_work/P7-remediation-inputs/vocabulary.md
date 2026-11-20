# Vocabulary — P7-remediation-inputs

Only non-source names are listed. Interface names for prompts in this area are source constants or functions (`SYSTEM`, `FIXER_SYSTEM`, `ORCHESTRATOR_SYSTEM`, `build_user`, `_verdict_extraction_prompt`, `Strategy.as_prompt_block`), so they are not new.

### Template
- Definition: a field inside a prompt interface holding the literal text skeleton of a prompt assembled by code, with `$variable` slots.
- Why needed: the per-finding user prompt and the playbook strategy block are built by f-strings; the skeleton shows exactly what the model receives.
- Kind: general harness concept
- Original source term or wording: f-string return value of `build_user`, `as_prompt_block`
- Source references: vvaharness/remediation_agent/prompts.py:197-207, vvaharness/remediation_agent/playbook.py:52-64
- Used in: vvah/vvaharness/remediation_agent/prompts.sudo, vvah/vvaharness/remediation_agent/playbook.sudo

### Role
- Definition: a field inside a system-prompt interface holding the opening identity paragraph of the prompt, quoted exactly.
- Why needed: separates the persona sentence from the rule list in `Constraints`.
- Kind: general harness concept
- Original source term or wording: first paragraph of each system prompt ("You are ...")
- Source references: vvaharness/remediation_agent/prompts.py:26-29, 83-84, 110-111
- Used in: vvah/vvaharness/remediation_agent/prompts.sudo

### Termination summary
- Definition: a closing comment block that states the loop bounds derived from a guard's state machine (number of dispatches, malformed refusals).
- Why needed: the fixer loop has no explicit loop statement; its bound is spread across state fields.
- Kind: general harness concept
- Original source term or wording: none (derived from `_attempts`, `_malformed_rejections`, `_terminal`)
- Source references: vvaharness/remediation_agent/plugin_runner/handoff.py:64-145
- Used in: vvah/vvaharness/remediation_agent/plugin_runner/handoff.sudo

### Options blocks in input files
- Definition: in `vvah/inputs/*.sudo.md`, an `Options { ... }` block lists the decisive keys and values of a data file; per-CWE playbook entries are condensed to strategy names with their line ranges.
- Why needed: data files have no functions; the gates read these values.
- Kind: general harness concept
- Original source term or wording: YAML/JSON/CSV keys as in the files
- Source references: inputs/remediation_policy.yaml:32-85, inputs/remediation_playbook.yaml:39-406
- Used in: vvah/inputs/*.sudo.md
