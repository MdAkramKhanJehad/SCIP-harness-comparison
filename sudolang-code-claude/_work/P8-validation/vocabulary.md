# P8-validation vocabulary

New names in `vvah/vvaharness/validation/**` that are not source identifiers and not in the shared table of `_work/BRIEF.md`.

### ArtifactNames
- Definition: grouping interface for the artifact file and directory name constants.
- Why needed: groups related module-level constants into one interface block.
- Kind: tool-specific identifier
- Original source term or wording: "Single source of truth for artifact names, DTO layout, and runtime environment keys."
- Source references: vvaharness/validation/constants/artifacts.py:24-33
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

### EnvironmentNames
- Definition: grouping interface for the VVAHARNESS_* environment-variable name constants.
- Why needed: groups module constants and separates the inert names from the ones that are read.
- Kind: tool-specific identifier
- Original source term or wording: "Only ENV_CLAUDE_BINARY/ENV_GHE_* are read (config.settings._EnvScalars); the rest are inert names"
- Source references: vvaharness/validation/constants/artifacts.py:69-86
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

### SessionEnvironmentNames
- Definition: grouping interface for the environment names set on the launched validation session.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: "Agent-session environment contract (set on the launched validation session)."
- Source references: vvaharness/validation/constants/artifacts.py:88-99
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

### AgentDefaults
- Definition: grouping interface for the DEFAULT_* agent runtime values.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: "Default agent runtime values (mirror AgentConfig defaults in config.settings)."
- Source references: vvaharness/validation/constants/artifacts.py:127-140
- Used in: vvah/vvaharness/validation/constants/artifacts.sudo

### DiffMarkers
- Definition: grouping interface for the diff-parsing regular expression and marker constants.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: "Constants for deterministic diff-based fact tools."
- Source references: vvaharness/validation/constants/diff.py:26-43
- Used in: vvah/vvaharness/validation/constants/diff.sudo

### TestFileNames
- Definition: grouping interface for the test-file naming rules.
- Why needed: groups module constants.
- Kind: tool-specific identifier
- Original source term or wording: PY_TEST_EXACT_NAMES, PY_TEST_NAME_PREFIX, PY_TEST_NAME_SUFFIX, JS_TEST_SUFFIXES
- Source references: vvaharness/validation/constants/test_inventory.py:19-25
- Used in: vvah/vvaharness/validation/constants/test_inventory.sudo

### console:
- Definition: helper verb meaning "write this line to stderr through vvaharness.util.console.write"; it stops nothing and is not a logger warning.
- Why needed: keeps operator-facing console lines apart from `warn`, which is used for logger warnings.
- Kind: general harness concept
- Original source term or wording: console.write(...)
- Source references: vvaharness/validation/ingest/case_loader.py:84-87; vvaharness/validation/cli/__init__.py:73,264-267; vvaharness/validation/cli/_run.py:189-311; vvaharness/validation/cli/_model.py:95-123; vvaharness/validation/report/augment.py:248-250
- Used in: vvah/vvaharness/validation/ingest/case_loader.sudo, ingest/workspace.sudo, cli/__init__.sudo, cli/_run.sudo, cli/_model.sudo, report/augment.sudo

### VALIDATION_LAUNCH_PROMPT
- Definition: interface for the user-turn prompt that `build_launch_prompt` assembles.
- Why needed: the prompt is built line by line in code, with no source constant.
- Kind: tool-specific identifier
- Original source term or wording: build_launch_prompt / "launch prompt"
- Source references: vvaharness/validation/session/launch_prompt.py:99-127
- Used in: vvah/vvaharness/validation/session/launch_prompt.sudo, vvah/vvaharness/validation/session/launcher.sudo

### VALIDATION_SYNTHESIS_SECTION
- Definition: interface for the "## Synthesis boundary" text added to the system prompt; the backend decides which version is used.
- Why needed: the source returns this text from a function, not a constant.
- Kind: tool-specific identifier
- Original source term or wording: _synthesis_section
- Source references: vvaharness/validation/session/launcher.py:374-394
- Used in: vvah/vvaharness/validation/session/launcher.sudo

### VALIDATION_RULES_SECTION
- Definition: interface for the "## Rules" text added to the system prompt; it either points to `.claude/rules/` or includes the rules in full.
- Why needed: the source returns this text from a function, not a constant.
- Kind: tool-specific identifier
- Original source term or wording: _rules_section
- Source references: vvaharness/validation/session/launcher.py:353-366
- Used in: vvah/vvaharness/validation/session/launcher.sudo

### VALIDATION_SYSTEM_PROMPT
- Definition: the text of `prompts/system.md`, the base of the orchestrator's system prompt.
- Why needed: gives a name to a Markdown file's contents.
- Kind: tool-specific identifier
- Original source term or wording: SYSTEM_PROMPT_FILENAME "system.md"
- Source references: vvaharness/validation/prompts/system.md:16-154; vvaharness/validation/session/launcher.py:397-409; vvaharness/validation/constants/artifacts.py:150
- Used in: vvah/vvaharness/validation/prompts/system.sudo.md, vvah/vvaharness/validation/session/launcher.sudo

### SECURITY_ARCHITECT_PROMPT / PENETRATION_TESTER_PROMPT / CROSS_REPO_ANALYZER_PROMPT
- Definition: interfaces for the body (system prompt) of each reviewer-persona `.md` file.
- Why needed: the prompts are Markdown files with no source constant name.
- Kind: tool-specific identifier
- Original source term or wording: subagent names "security-architect", "penetration-tester", "cross-repo-analyzer"
- Source references: vvaharness/validation/subagents/security-architect.md:35-98; vvaharness/validation/subagents/penetration-tester.md:35-99; vvaharness/validation/subagents/cross-repo-analyzer.md:35-122
- Used in: vvah/vvaharness/validation/subagents/*.sudo.md

### ADVERSARIAL_REVIEW_RULES / SCORING_MATRIX_RULES / VALIDATION_SCORING_SKILL
- Definition: interfaces for the two rules files and the skill file given to the validation session.
- Why needed: the files have no source constant name (the code refers to them through ADVERSARIAL_RULES / SCORING_RULES file-name constants).
- Kind: tool-specific identifier
- Original source term or wording: "Adversarial Review Rules", "Scoring Matrix", "Validation Scoring Skill"
- Source references: vvaharness/validation/claude_config/rules/adversarial-review.md:16-68; vvaharness/validation/claude_config/rules/scoring-matrix.md:16-200; vvaharness/validation/claude_config/skills/validation-scoring/SKILL.md:22-86
- Used in: vvah/vvaharness/validation/claude_config/rules/*.sudo.md, vvah/vvaharness/validation/claude_config/skills/validation-scoring/SKILL.sudo.md

### Prompt section blocks
- Definition: named sub-blocks inside a prompt interface that mirror the Markdown headings of the source prompt: Role, Directive, FocusAreas, AntiManipulation, Inputs, Tools, FieldNotes, Guardrails, PersonaIsolation, SynthesisRules, EvidenceRequirements, SecretExposureEvidence, SignalToNoise, ScoringReference, Rules, Criteria, StatusMultipliers, DecisionThresholds, MergeReadiness, ScoringExecution, InputAndOutputSchema, SessionMarkers, JiraStatusTransitions, CodeLevelSignalsOnly, SecretExposureVerification, SecretExposureGateMapping, RotationAttestation, SecretExposureVerdict, SecretExposureAuditLine. All contain model-facing text only (like Constraints).
- Why needed: keeps the section structure of long prompts traceable to their headings.
- Kind: general harness concept
- Original source term or wording: the Markdown section headings ("## Directive", "## Focus Areas", "## Anti-Manipulation", and so on)
- Source references: the prompt files listed in the three entries above, and vvaharness/validation/prompts/system.md
- Used in: vvah/vvaharness/validation/prompts/system.sudo.md, subagents/*.sudo.md, claude_config/rules/*.sudo.md, claude_config/skills/validation-scoring/SKILL.sudo.md

### capture_transcript
- Definition: function name for the body of the Stop-hook shell script.
- Why needed: a shell script has no function name; the file name is used.
- Kind: tool-specific identifier
- Original source term or wording: capture_transcript.sh
- Source references: vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:16-35
- Used in: vvah/vvaharness/validation/claude_config/hooks/logging/capture_transcript.sudo

### SessionCall
- Definition: the validation session written as one `callModel(...)`.
- Why needed: shows the role, tools, subagents and limits of the one orchestrator call in one place.
- Kind: general harness concept
- Original source term or wording: StreamingOptions plus harness.run_streaming
- Source references: vvaharness/validation/session/launcher.py:299-345, 620-631
- Used in: vvah/vvaharness/validation/session/launcher.sudo

### $findingDetails / $orchestratorRulesText
- Definition: template slots for the finding-details block and for the full rules text.
- Why needed: placeholders for text that helper functions build.
- Kind: tool-specific identifier
- Original source term or wording: _append_finding_details, orchestrator_rules_text()
- Source references: vvaharness/validation/session/launch_prompt.py:81-96; vvaharness/validation/session/rules.py:41-43
- Used in: vvah/vvaharness/validation/session/launch_prompt.sudo, vvah/vvaharness/validation/session/launcher.sudo

### offer
- Definition: `offer X(args) => body` means a tool is built and made available to the model, not that it is called.
- Why needed: keeps building a tool separate from calling it.
- Kind: general harness concept
- Original source term or wording: @tool def ...; tools.append(...)
- Source references: vvaharness/validation/tools/deep_tools.py:37-90
- Used in: vvah/vvaharness/validation/tools/deep_tools.sudo
