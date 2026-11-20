# vvaharness/validation/io/persona_report_stash.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/io/persona_report_stash.py.evidence.json`. SHA-256: `c04c1852b4b5abdf5f885facd3c16b7317cda91e00bbbb8d2dc97a80a223735d`.

```sudo
// Source: vvaharness/validation/io/persona_report_stash.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from langchain_core.messages import ToolMessage; preserve alias and import-time effects.
// Source: vvaharness/validation/io/persona_report_stash.py:23-27
In source order: Resolve source import from pydantic import ValidationError; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.models.persona_report import HarnessTerminalState, PersonaReport; preserve alias and import-time effects. Then Evaluate once 1048576; assign in source target order to MAX_TOOL_MESSAGE_CHARS.
// Source: vvaharness/validation/io/persona_report_stash.py:30-49
// Source signature: _validate_candidates(candidates: list[Any]) -> list[PersonaReport]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_candidates(candidates) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/persona_report_stash.py:33-35
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then For reports, assign []; source annotation list[PersonaReport]. Then For seen, assign set(); source annotation set[tuple[str | None, str | None]].
  // Source: vvaharness/validation/io/persona_report_stash.py:36-48
  for each data in candidates {
    // Source: vvaharness/validation/io/persona_report_stash.py:37-38
    if (the source predicate not isinstance(data, dict) is truthy) {
      // Source: vvaharness/validation/io/persona_report_stash.py:38-38
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:39-40
    if (the source predicate 'persona' not in data or 'gates' not in data is truthy) {
      // Source: vvaharness/validation/io/persona_report_stash.py:40-40
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:41-41
    In source order: Evaluate once (data.get('persona'), data.get('tracking_id')); assign in source target order to key.
    // Source: vvaharness/validation/io/persona_report_stash.py:42-43
    if (the source predicate key in seen is truthy) {
      // Source: vvaharness/validation/io/persona_report_stash.py:43-43
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:44-44
    In source order: Evaluate seen.add(key); retain side effects and discard the expression result.
    // Source: vvaharness/validation/io/persona_report_stash.py:45-48
    Perform the following protected operations {
      // Source: vvaharness/validation/io/persona_report_stash.py:46-46
      In source order: Evaluate reports.append(PersonaReport.model_validate(data)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:47-48
    On the first matching source exception ValidationError, in handler order {
      // Source: vvaharness/validation/io/persona_report_stash.py:48-48
      Continue the immediately enclosing source loop at its next iteration.
    }
  }
  // Source: vvaharness/validation/io/persona_report_stash.py:49-49
  End this invocation with reports.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/io/persona_report_stash.py:52-80
// Source signature: extract_subagent_reports(final_state: HarnessTerminalState) -> list[PersonaReport]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_subagent_reports(final_state) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/io/persona_report_stash.py:55-55
  In source order: Retain source documentation literal source_literal_55_4; it is not a model call.
  // Source: vvaharness/validation/io/persona_report_stash.py:57-58
  if (the source predicate 'sdk_persona_reports' in final_state is truthy) {
    // Source: vvaharness/validation/io/persona_report_stash.py:58-58
    End this invocation with _validate_candidates(final_state['sdk_persona_reports']).
  }
  // Source: vvaharness/validation/io/persona_report_stash.py:61-61
  In source order: For candidates, assign []; source annotation list[Any].
  // Source: vvaharness/validation/io/persona_report_stash.py:62-78
  for each msg in final_state.get('messages', []) {
    // Source: vvaharness/validation/io/persona_report_stash.py:63-64
    if (the source predicate not isinstance(msg, ToolMessage) is truthy) {
      // Source: vvaharness/validation/io/persona_report_stash.py:64-64
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:65-65
    In source order: Evaluate once msg.content; assign in source target order to content.
    // Source: vvaharness/validation/io/persona_report_stash.py:66-67
    if (the source predicate isinstance(content, (list, tuple)) is truthy) {
      // Source: vvaharness/validation/io/persona_report_stash.py:67-67
      In source order: Evaluate once content[0] if content else ''; assign in source target order to content.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:68-73
    if (the source predicate not isinstance(content, str) or len(content) > MAX_TOOL_MESSAGE_CHARS or (not content.strip()) is truthy) {
      // Source: vvaharness/validation/io/persona_report_stash.py:73-73
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:74-77
    Perform the following protected operations {
      // Source: vvaharness/validation/io/persona_report_stash.py:75-75
      In source order: Evaluate once json.loads(content.strip()); assign in source target order to data.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:76-77
    On the first matching source exception json.JSONDecodeError, in handler order {
      // Source: vvaharness/validation/io/persona_report_stash.py:77-77
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/validation/io/persona_report_stash.py:78-78
    In source order: Evaluate candidates.append(data); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/io/persona_report_stash.py:80-80
  End this invocation with _validate_candidates(candidates).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.models.persona_report import HarnessTerminalState, PersonaReport` at source line 25: `source_detail/vvaharness/validation/models/persona_report.py.sudo.md`.
