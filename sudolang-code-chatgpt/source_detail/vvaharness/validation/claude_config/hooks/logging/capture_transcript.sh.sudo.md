# vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh

Role: optional executable shell script; not assumed invoked.

Exact source asset: `assets/original/vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh`. SHA-256 `55a71cc732ef4d5f7319efb4b6fded4b823289a292b0fb000f6527dcc9129b8b`.

```sudo
// Source: vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:1-35
fn source_shell_procedure(arguments, environment) {
  Interpret the exact source asset using its declared shell, preserving argument expansion,
    command substitutions, pipeline/status rules, redirects, function scopes and command order.
  Use the helper/gate/cap descriptions in representation/shell-probes.sudo.md.
  The ordered source-command appendix below retains every pattern, include/exclude flag,
    conditional and cutoff; it is the detailed procedure, not a claim this tool was invoked.
}
```

## Ordered source-command evidence

These exact shell fragments disambiguate lexical/regex details; they are inert evidence.

Source: `vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:1-14`

````sh
#!/usr/bin/env bash
# Copyright 2026 Visa, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
````

Source: `vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:16-19`

````sh
# Stop hook: copies the Claude session transcript into the logging directory.
# The transcript contains the full conversation for all agents (top-level + sub-agents).
# Fail-open: if any step fails, exits 0 silently.
set +e
````

Source: `vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:21-24`

````sh
# The raw transcript is UNREDACTED (it can contain secrets/PII the agent read from
# the target repo). Persist it only when an operator explicitly opts in for debugging;
# by default it is never written, and the redacted session.jsonl is persisted instead.
[ -n "${VALIDATION_DEBUG_TRANSCRIPT:-}" ] || exit 0
````

Source: `vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:26-28`

````sh
_INPUT="$(cat)"
_TRANSCRIPT="$(echo "$_INPUT" | jq -r '.transcript_path // ""' 2>/dev/null | sed "s|^~|$HOME|")"
_LOG_DIR="${VALIDATION_LOG_DIR:-}"
````

Source: `vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:30-30`

````sh
[ -z "$_TRANSCRIPT" ] || [ ! -f "$_TRANSCRIPT" ] || [ -z "$_LOG_DIR" ] && exit 0
````

Source: `vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:32-35`

````sh
_DEST="$_LOG_DIR/subagents/transcript.jsonl"
mkdir -p "$(dirname "$_DEST")" 2>/dev/null
cp "$_TRANSCRIPT" "$_DEST" 2>/dev/null || true
exit 0
````

