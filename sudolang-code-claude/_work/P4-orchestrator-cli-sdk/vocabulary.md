# Vocabulary: P4-orchestrator-cli-sdk

### ScanArgs
- Definition: interface listing the `vvaharness scan` command-line options and their defaults
- Why needed: argparse builds an untyped namespace with no source class name
- Kind: tool-specific identifier
- Original source term or wording: `build_parser()` / `args`
- Source references: vvaharness/orchestrator/entry.py:140-223
- Used in: vvah/vvaharness/orchestrator/entry.sudo

### PROBE_PING_PROMPT
- Definition: prompt interface for the literal "ping" sent by the connectivity probe
- Why needed: the prompt is an inline literal, not a named constant
- Kind: tool-specific identifier
- Original source term or wording: `_probe("ping", ...)`
- Source references: vvaharness/orchestrator/preflight.py:781
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

### DEEPAGENTS_PROBE_PROMPT
- Definition: prompt interface for "reply with the single word ok"
- Why needed: inline literal
- Kind: tool-specific identifier
- Original source term or wording: `run_oneshot("reply with the single word ok", ...)`
- Source references: vvaharness/orchestrator/preflight.py:716
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

### CLI_BRIDGE_PROMPT
- Definition: prompt interface for the instruction to call the echo tool through the CLI MCP bridge
- Why needed: inline f-string
- Kind: tool-specific identifier
- Original source term or wording: `f"Call the {_PROBE_BRIDGE_TOOL_NAME} tool with marker='{nonce}', ..."`
- Source references: vvaharness/orchestrator/preflight.py:641-642
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

### "preflight" (callModel role label)
- Definition: role label for probe calls made by preflight, which are not tied to one configured pipeline role
- Why needed: callModel requires a role; the probe calls run outside any stage
- Kind: general harness concept
- Original source term or wording: preflight probe functions (_probe_deepagents_harness, CLI bridge probe)
- Source references: vvaharness/orchestrator/preflight.py:641-642, 716
- Used in: vvah/vvaharness/orchestrator/preflight.sudo

### put
- Definition: the nested helper inside _install_agents that writes one agent file unless it already exists or has a symlinked ancestor (POSIX only)
- Why needed: nested function with no module-level name (source name kept)
- Kind: tool-specific identifier
- Original source term or wording: `def put(path, content, *, anchor)` nested in `_install_agents`
- Source references: vvaharness/cli/_setup.py:96-108
- Used in: vvah/vvaharness/cli/_setup.sudo

### PluginContract
- Definition: the plugin contract and seams the SDK README states
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:1-46
- Used in: vvah/vvaharness/sdk/README.sudo.md

### FailureContract
- Definition: the README's statement of how plugin failures and SDK bounds affect a scan
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:97-115
- Used in: vvah/vvaharness/sdk/README.sudo.md

### RemediateAndValidate
- Definition: the README's statements about sdk.remediate and sdk.validate
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:117-143
- Used in: vvah/vvaharness/sdk/README.sudo.md

### Limitations
- Definition: the README's current-limitations section
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:145-161
- Used in: vvah/vvaharness/sdk/README.sudo.md

### SemgrepReferenceVariant
- Definition: the README's summary of the Semgrep reference plugin and its bounds
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:163-206
- Used in: vvah/vvaharness/sdk/README.sudo.md

### RunningGuide
- Definition: the README's statements about sdk.scan
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:208-224
- Used in: vvah/vvaharness/sdk/README.sudo.md

### HandoffGuide
- Definition: the README's guidance for inject_findings, distinct from the source dataclass Handoff
- Why needed: a README section heading has no identifier; an interface groups its decisive values
- Kind: tool-specific identifier
- Original source term or wording: README section heading
- Source references: vvaharness/sdk/README.md:226-325
- Used in: vvah/vvaharness/sdk/README.sudo.md
