# vvaharness/backends/llm/cli/oneshot.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## prompt — source lines 76–76

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --output-format
}
```

## tag_sfx — source lines 104–104

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:104-104
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: tag; conversion=none; format_spec=none]]
}
```

## prompt — source lines 105–106

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `tag_sfx; conversion=none; format_spec=none`
- `len(user_prompt); conversion=none; format_spec=none`
- `f', max_tokens={max_tokens}' if max_tokens else ''; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:105-106
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [cli] prompt mode -> [dynamic source value: model; conversion=none; format_spec=none][dynamic source value: tag_sfx; conversion=none; format_spec=none] ([dynamic source value: len(user_prompt); conversion=none; format_spec=none] chars[dynamic source value: f', max_tokens={max_tokens}' if max_tokens else ''; conversion=none; format_spec=none])
}
```

## prompt — source lines 68–68

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:68-68
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: aborted by user (Ctrl-C)
}
```

## prompt — source lines 74–74

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:74-74
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --system-prompt
}
```

## prompt — source lines 78–78

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:78-78
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: json_schema
}
```

## user_prompt — source lines 87–88

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `user_prompt; conversion=none; format_spec=none`
- `json.dumps(json_schema); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:87-88
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: user_prompt; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:87-88
Constraints {
  The requested model reply must contain ONLY a JSON object conforming to this JSON Schema: [dynamic source value: json.dumps(json_schema); conversion=none; format_spec=none]
}
```

## prompt — source lines 91–91

Source context: callable `prompt`; enclosing call `_discovery._cli_capabilities().get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:91-91
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_budget
}
```

## prompt — source lines 92–92

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:92-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --max-budget-usd
}
```

## prompt — source lines 79–79

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:79-79
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --json-schema
}
```

## prompt — source lines 82–85

Source context: callable `prompt`; enclosing call `log.warning`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:82-85
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: this `claude` build does not advertise --json-schema; embedding the schema in the prompt instead.
  The request retains this source rule, criterion or rationale, with its original modal force: Structured output is no longer validator-enforced — upgrade the CLI, or route the role via: sdk, for schema guarantees.
}
```

## prompt — source lines 106–106

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `max_tokens; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:106-106
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , max_tokens=[dynamic source value: max_tokens; conversion=none; format_spec=none]
}
```

## result — source lines 117–117

Source context: callable `prompt`; enclosing call `_retry._run_with_retry`; keyword `label`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `tag_sfx; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:117-117
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt([dynamic source value: model; conversion=none; format_spec=none])[dynamic source value: tag_sfx; conversion=none; format_spec=none]
}
```

## result — source lines 123–123

Source context: callable `prompt`; enclosing call `_retry._run_with_retry`; keyword `heartbeat_label`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `tag_sfx; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:123-123
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt mode ([dynamic source value: model; conversion=none; format_spec=none])[dynamic source value: tag_sfx; conversion=none; format_spec=none]
}
```

## env['CLAUDE_CODE_MAX_OUTPUT_TOKENS'] — source lines 145–145

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:145-145
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CLAUDE_CODE_MAX_OUTPUT_TOKENS
}
```

## env['CLAUDE_CODE_MAX_OUTPUT_TOKENS'] — source lines 164–164

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:164-164
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CLAUDE_CODE_MAX_OUTPUT_TOKENS
}
```

## prompt — source lines 128–128

Source context: callable `prompt`; enclosing call `call_timeout_error`; keyword `cause_text`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `wall; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:128-128
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: claude subprocess exceeded [dynamic source value: wall; conversion=none; format_spec=none]s
}
```

## prompt — source lines 134–134

Source context: callable `prompt`; enclosing call `_discovery._format_cli_error`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/oneshot.py:134-134
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: claude CLI failed
}
```

