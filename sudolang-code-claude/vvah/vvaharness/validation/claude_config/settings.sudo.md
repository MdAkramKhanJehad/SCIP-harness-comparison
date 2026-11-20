# vvaharness/validation/claude_config/settings.json

Claude Code project settings copied into the validation workspace as `.claude/settings.json`: the model, the permission allow and deny lists, and the Stop hook.

Source: `vvaharness/validation/claude_config/settings.json` (lines 1-17)
Executor: code (read by Claude Code, which enforces the permissions)
Called from: copied by `vvaharness/validation/session/config_inject.sudo` inject_claude_config

// src: vvaharness/validation/claude_config/settings.json:1-17
Options {
  model: "claude-opus-4-8[1m]"
  permissions.allow: ["Read", "Grep", "Glob"]
  permissions.deny: ["Write", "Edit", "NotebookEdit", "Bash"]
  hooks.Stop: [{ type: "command", command: "bash .claude/hooks/logging/capture_transcript.sh", timeout: 30 }]
}
// these permissions are applied by Claude Code for sessions that load project settings (cli and sdk backends); how the launcher selects the backend and setting sources is in session/launcher.sudo
// preserved: the model here is fixed in the file, while the launcher passes its own model from AgentConfig (config/settings/agent.sudo)
