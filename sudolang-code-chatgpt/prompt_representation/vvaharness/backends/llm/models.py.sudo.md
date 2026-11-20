# vvaharness/backends/llm/models.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## STRUCTURED_PROSE_REASK — source lines 161–162

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `RESPONSE_MODEL_TOOL_NAME; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:161-162
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Call the `[dynamic source value: RESPONSE_MODEL_TOOL_NAME; conversion=none; format_spec=none]` tool now with the model's findings as its arguments.
  The requested model behavior excludes reply with prose; the result is only accepted through that tool.
}
```

## LLM_MODEL_REFUSALS_COUNTER — source lines 503–503

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:503-503
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: llm_model_refusals
}
```

## REFUSAL_RETRY_ATTEMPTED_COUNTER — source lines 506–506

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:506-506
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: llm_refusal_retry_attempted
}
```

## REFUSAL_RETRY_RECOVERED_COUNTER — source lines 507–507

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:507-507
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: llm_refusal_retry_recovered
}
```

## line — source lines 172–173

Source context: callable `with_submit_instruction`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `response_model.__name__; conversion=none; format_spec=none`
- `tool_name; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:172-173
Constraints {
  The requested conditional/temporal rule is: When the model have your final [dynamic source value: response_model.__name__; conversion=none; format_spec=none], call the `[dynamic source value: tool_name; conversion=none; format_spec=none]` tool with it; a plain-text reply is not accepted.
}
```

## response_model_tool — source lines 153–153

Source context: callable `response_model_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `response_model.__name__; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:153-153
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Submit the final [dynamic source value: response_model.__name__; conversion=none; format_spec=none].
}
```

## with_submit_instruction — source lines 174–174

Source context: callable `with_submit_instruction`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `system_prompt; conversion=none; format_spec=none`
- `line; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:174-174
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: system_prompt; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/backends/llm/models.py:174-174
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: line; conversion=none; format_spec=none]
}
```

## where — source lines 538–538

Source context: callable `model_refusal`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `stage; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:538-538
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , stage=[dynamic source value: stage; conversion=none; format_spec=none]
}
```

## tail — source lines 540–540

Source context: callable `model_refusal`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `redact(detail)[:200]; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:540-540
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: : [dynamic source value: redact(detail)[:200]; conversion=none; format_spec=none]
}
```

## model_refusal — source lines 542–543

Source context: callable `model_refusal`; enclosing call `ModelRefusal`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `route; conversion=none; format_spec=none`
- `category or 'unspecified'; conversion=none; format_spec=none`
- `where; conversion=none; format_spec=none`
- `tail; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:542-543
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: model refused the request (route=[dynamic source value: route; conversion=none; format_spec=none], category=[dynamic source value: category or 'unspecified'; conversion=none; format_spec=none][dynamic source value: where; conversion=none; format_spec=none])[dynamic source value: tail; conversion=none; format_spec=none]
}
```

## meta — source lines 561–561

Source context: callable `ai_message_refused`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:561-561
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: response_metadata
}
```

## extra — source lines 569–569

Source context: callable `_openai_refused`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:569-569
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: additional_kwargs
}
```

## _named_tools — source lines 367–368

Source context: callable `_named_tools`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `config_key; conversion=none; format_spec=none`
- `tools; conversion=repr; format_spec=none`
- `tools; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:367-368
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: config_key; conversion=none; format_spec=none] must be a YAML list of tool names, got the bare string [dynamic source value: tools; conversion=repr; format_spec=none] — write it as `allowed_tools: [[dynamic source value: tools; conversion=none; format_spec=none]]`
}
```

## _named_tools — source lines 377–378

Source context: callable `_named_tools`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `config_key; conversion=none; format_spec=none`
- `[t for t in named if not isinstance(t, str)]; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/models.py:377-378
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: config_key; conversion=none; format_spec=none] must contain only strings, got [dynamic source value: [t for t in named if not isinstance(t, str)]; conversion=repr; format_spec=none]
}
```

## category — source lines 554–554

Source context: callable `refusal_category`; enclosing call `meta.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:554-554
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stop_details
}
```

## wait_overrun — source lines 917–917

Source context: callable `wait_overrun`; enclosing call `call_timeout_error`; keyword `cause_text`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `wait; conversion=none; format_spec=f'.1f'`
- `session_budget; conversion=none; format_spec=f'g'`

```sudo
// Source: vvaharness/backends/llm/models.py:917-917
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: retry wait of [dynamic source value: wait; conversion=none; format_spec=f'.1f']s would cross the [dynamic source value: session_budget; conversion=none; format_spec=f'g']s session clock
}
```

## refusal_resend_allowed — source lines 514–514

Source context: callable `refusal_resend_allowed`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:514-514
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refusal_retries
}
```

## ai_message_refused — source lines 562–562

Source context: callable `ai_message_refused`; enclosing call `meta.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:562-562
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stop_reason
}
```

## (refused, category) — source lines 585–585

Source context: callable `_refusal_link`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:585-585
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ai_message
}
```

## api_link — source lines 581–581

Source context: callable `_refusal_link`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/models.py:581-581
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: status_code
}
```

