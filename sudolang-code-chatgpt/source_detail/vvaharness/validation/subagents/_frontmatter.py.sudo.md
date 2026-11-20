# vvaharness/validation/subagents/_frontmatter.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/subagents/_frontmatter.py.evidence.json`. SHA-256: `7bd955131c0432fb634353c39835ed9a0d11a2c46c288780a919cdec18a72df1`.

```sudo
// Source: vvaharness/validation/subagents/_frontmatter.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.subagents.models import ParsedFrontmatter, SubagentFrontmatterMeta; preserve alias and import-time effects.
// Source: vvaharness/validation/subagents/_frontmatter.py:24-26
In source order: Evaluate once re.compile('^---\\s*\\n(.*?)\\n---\\s*\\n(.*)\\Z', re.DOTALL); assign in source target order to _FRONTMATTER_RE. Then Evaluate once frozenset({'name', 'model', 'description'}); assign in source target order to _SCALAR_KEYS. Then Evaluate once frozenset({'allowedTools', 'deniedTools', 'skills'}); assign in source target order to _LIST_KEYS.
// Source: vvaharness/validation/subagents/_frontmatter.py:29-41
// Source signature: _append_list_item(meta: dict[str, object], current_list_key: str | None, raw_line: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _append_list_item(meta, current_list_key, raw_line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_frontmatter.py:34-34
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call.
  // Source: vvaharness/validation/subagents/_frontmatter.py:35-36
  if (the source predicate current_list_key is None is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:36-36
    Raise ValueError(source_template_36_25).
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:37-38
  In source order: Evaluate once raw_line.rstrip().split('- ', 1)[1].strip(); assign in source target order to value. Then Evaluate once meta[current_list_key]; assign in source target order to bucket.
  // Source: vvaharness/validation/subagents/_frontmatter.py:39-40
  if (the source predicate not isinstance(bucket, list) is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:40-40
    Raise TypeError(source_template_40_24).
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:41-41
  In source order: Evaluate bucket.append(value); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/subagents/_frontmatter.py:44-58
// Source signature: _apply_key_line(meta: dict[str, object], raw_line: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _apply_key_line(meta, raw_line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_frontmatter.py:45-46
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call. Then Evaluate once raw_line.rstrip().partition(':'); assign in source target order to (field_key, separator, value).
  // Source: vvaharness/validation/subagents/_frontmatter.py:47-48
  if (the source predicate not separator is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:48-48
    Raise ValueError(source_template_48_25).
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:49-49
  In source order: Evaluate once (field_key.strip(), value.strip()); assign in source target order to (field_key, value).
  // Source: vvaharness/validation/subagents/_frontmatter.py:50-52
  if (the source predicate field_key in _SCALAR_KEYS is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:51-51
    In source order: Evaluate once value; assign in source target order to meta[field_key].
    // Source: vvaharness/validation/subagents/_frontmatter.py:52-52
    End this invocation with None.
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:53-57
  if (the source predicate field_key in _LIST_KEYS is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:54-55
    if (the source predicate value is truthy) {
      // Source: vvaharness/validation/subagents/_frontmatter.py:55-55
      Raise ValueError(source_template_55_29).
    }
    // Source: vvaharness/validation/subagents/_frontmatter.py:56-56
    In source order: Evaluate once []; assign in source target order to meta[field_key].
    // Source: vvaharness/validation/subagents/_frontmatter.py:57-57
    End this invocation with field_key.
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:58-58
  Raise ValueError(source_template_58_21).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/subagents/_frontmatter.py:61-71
// Source signature: _classify_line(meta: dict[str, object], current_list_key: str | None, raw_line: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _classify_line(meta, current_list_key, raw_line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_frontmatter.py:64-65
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Evaluate once raw_line.rstrip(); assign in source target order to line.
  // Source: vvaharness/validation/subagents/_frontmatter.py:66-67
  if (the source predicate not line.strip() is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:67-67
    End this invocation with None.
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:68-70
  if (the source predicate line.startswith(('  - ', '\t- ')) is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:69-69
    In source order: Evaluate _append_list_item(meta, current_list_key, raw_line); retain side effects and discard the expression result.
    // Source: vvaharness/validation/subagents/_frontmatter.py:70-70
    End this invocation with current_list_key.
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:71-71
  End this invocation with _apply_key_line(meta, raw_line).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/subagents/_frontmatter.py:74-84
// Source signature: parse_frontmatter(text: str) -> ParsedFrontmatter
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_frontmatter(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/subagents/_frontmatter.py:75-76
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call. Then Evaluate once _FRONTMATTER_RE.match(text); assign in source target order to match.
  // Source: vvaharness/validation/subagents/_frontmatter.py:77-78
  if (the source predicate not match is truthy) {
    // Source: vvaharness/validation/subagents/_frontmatter.py:78-78
    Raise ValueError('subagent file missing YAML frontmatter').
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:79-81
  In source order: Evaluate once (match.group(1), match.group(2)); assign in source target order to (head, body). Then For meta, assign {}; source annotation dict[str, object]. Then For current_list_key, assign None; source annotation str | None.
  // Source: vvaharness/validation/subagents/_frontmatter.py:82-83
  for each raw_line in head.splitlines() {
    // Source: vvaharness/validation/subagents/_frontmatter.py:83-83
    In source order: Evaluate once _classify_line(meta, current_list_key, raw_line); assign in source target order to current_list_key.
  }
  // Source: vvaharness/validation/subagents/_frontmatter.py:84-84
  End this invocation with ParsedFrontmatter(cast(SubagentFrontmatterMeta, meta), body.strip()).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.subagents.models import ParsedFrontmatter, SubagentFrontmatterMeta` at source line 22: `source_detail/vvaharness/validation/subagents/models.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/subagents/_frontmatter.py.sudo.md). Exact strings in the evidence asset support this conversion.
