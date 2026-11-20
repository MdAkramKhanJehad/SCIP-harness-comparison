# vvaharness/backends/llm/openai.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## raw — source lines 377–377

Source context: callable `_prompt_cache_key`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `stage; conversion=none; format_spec=none`
- `repo_name; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `bucket; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:377-377
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: stage; conversion=none; format_spec=none]:[dynamic source value: repo_name; conversion=none; format_spec=none]:[dynamic source value: model; conversion=none; format_spec=none]:[dynamic source value: bucket; conversion=none; format_spec=none]
}
```

## prompt — source lines 676–681

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `f' [{tag}]' if tag else ''; conversion=none; format_spec=none`
- `_up_chars; conversion=none; format_spec=none`
- `max_tok; conversion=none; format_spec=none`
- `f', T={temperature}' if 'temperature' in kw else ''; conversion=none; format_spec=none`
- `', json' if 'response_format' in kw else ''; conversion=none; format_spec=none`
- `f', effort={effort}' if 'reasoning_effort' in kw else ''; conversion=none; format_spec=none`
- `request_timeout; conversion=none; format_spec=f'g'`

```sudo
// Source: vvaharness/backends/llm/openai.py:676-681
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] prompt -> [dynamic source value: model; conversion=none; format_spec=none][dynamic source value: f' [{tag}]' if tag else ''; conversion=none; format_spec=none] ([dynamic source value: _up_chars; conversion=none; format_spec=none] chars, max_tokens=[dynamic source value: max_tok; conversion=none; format_spec=none][dynamic source value: f', T={temperature}' if 'temperature' in kw else ''; conversion=none; format_spec=none][dynamic source value: ', json' if 'response_format' in kw else ''; conversion=none; format_spec=none][dynamic source value: f', effort={effort}' if 'reasoning_effort' in kw else ''; conversion=none; format_spec=none], timeout=[dynamic source value: request_timeout; conversion=none; format_spec=f'g']s)
}
```

## instruction — source lines 2069–2071

Source context: callable `agentic`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `RESPONSE_MODEL_TOOL_NAME; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:2069-2071
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Tool budget exhausted.
  The request retains this source rule, criterion or rationale, with its original modal force: Call `[dynamic source value: RESPONSE_MODEL_TOOL_NAME; conversion=none; format_spec=none]` now with what the model have established so far; it is the only way to reply.
}
```

## instruction — source lines 2073–2074

Source context: callable `agentic`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:2073-2074
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Tool budget exhausted.
  The request retains this source rule, criterion or rationale, with its original modal force: Reply now with the model's final answer based on what the model have read so far; do not call tools.
}
```

## bucket — source lines 376–376

Source context: callable `_prompt_cache_key`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `shard; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:376-376
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: r[dynamic source value: shard; conversion=none; format_spec=none]
}
```

## kw['stream_options'] — source lines 647–647

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:647-647
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stream_options
}
```

## kw['stream_options'] — source lines 647–647

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:647-647
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: include_usage
}
```

## kw['prompt_cache_key'] — source lines 651–651

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:651-651
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_cache_key
}
```

## kw['max_tokens'] — source lines 656–656

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:656-656
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## kw['max_completion_tokens'] — source lines 658–658

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:658-658
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_completion_tokens
}
```

## kw['response_format'] — source lines 664–664

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:664-664
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: response_format
}
```

## prompt — source lines 1076–1078

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `sorted(kw); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:1076-1078
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OpenAI call to [dynamic source value: model; conversion=none; format_spec=none] exhausted all retries without a successful response (every attempt hit a parameter-drop retry).
  The request retains this source rule, criterion or rationale, with its original modal force: Final request kwargs keys: [dynamic source value: sorted(kw); conversion=none; format_spec=none].
}
```

## written — source lines 1088–1088

Source context: callable `prompt`; enclosing call `norm.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1088-1088
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_creation_input_tokens
}
```

## prompt — source lines 1089–1092

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `u.get('prompt_tokens', 0); conversion=none; format_spec=none`
- `norm['cache_read_input_tokens']; conversion=none; format_spec=none`
- `f', cache_write={written}' if written is not None else ''; conversion=none; format_spec=none`
- `u.get('completion_tokens', 0); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:1089-1092
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] usage: in=[dynamic source value: u.get('prompt_tokens', 0); conversion=none; format_spec=none] (cached=[dynamic source value: norm['cache_read_input_tokens']; conversion=none; format_spec=none][dynamic source value: f', cache_write={written}' if written is not None else ''; conversion=none; format_spec=none]) out=[dynamic source value: u.get('completion_tokens', 0); conversion=none; format_spec=none]
}
```

## base_kw['prompt_cache_key'] — source lines 1693–1693

Source context: callable `agentic`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1693-1693
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_cache_key
}
```

## repo_name — source lines 366–366

Source context: callable `_prompt_cache_key`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:366-366
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: repo_name
}
```

## u — source lines 1082–1082

Source context: callable `prompt`; enclosing call `hasattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1082-1082
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: model_dump
}
```

## out_tokens — source lines 1099–1099

Source context: callable `prompt`; enclosing call `output_tokens_for_gate`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1099-1099
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_tokens
}
```

## _anthropic_tool_to_openai — source lines 1203–1203

Source context: callable `_anthropic_tool_to_openai`; enclosing call `t.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/openai.py:1203-1203
Constraints {
  The advertised description supplied with this operation is a model-visible claim: description
}
```

## prompt — source lines 676–676

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:676-676
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: tag; conversion=none; format_spec=none]]
}
```

## prompt — source lines 678–678

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `temperature; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:678-678
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , T=[dynamic source value: temperature; conversion=none; format_spec=none]
}
```

## prompt — source lines 680–680

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `effort; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:680-680
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , effort=[dynamic source value: effort; conversion=none; format_spec=none]
}
```

## prompt — source lines 805–805

Source context: callable `prompt`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:805-805
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: llm_effort_tier_stepped_down_on_server_error
}
```

## prompt — source lines 807–807

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `probed_model; conversion=none; format_spec=none`
- `probed_sent; conversion=none; format_spec=none`
- `learned; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:807-807
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: server_error_tier:[dynamic source value: probed_model; conversion=none; format_spec=none]:[dynamic source value: probed_sent; conversion=none; format_spec=none]:[dynamic source value: learned; conversion=none; format_spec=none]
}
```

## prompt — source lines 808–811

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `probed_model; conversion=none; format_spec=none`
- `probed_sent; conversion=repr; format_spec=none`
- `kw.get('reasoning_effort'); conversion=repr; format_spec=none`
- `kw.get('reasoning_effort'); conversion=repr; format_spec=none`
- `'for the rest of this run' if learned else 'for this call'; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:808-811
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [openai]: [dynamic source value: probed_model; conversion=none; format_spec=none] returned a server error at reasoning_effort=[dynamic source value: probed_sent; conversion=repr; format_spec=none] and succeeded at [dynamic source value: kw.get('reasoning_effort'); conversion=repr; format_spec=none]; using [dynamic source value: kw.get('reasoning_effort'); conversion=repr; format_spec=none] [dynamic source value: 'for the rest of this run' if learned else 'for this call'; conversion=none; format_spec=none].
}
```

## prompt — source lines 966–968

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `_summarise_status_error(e); conversion=none; format_spec=none`
- `_payload_shape(messages, str(e)); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:966-968
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OpenAI call failed (status=[dynamic source value: e.status_code; conversion=none; format_spec=none], model=[dynamic source value: model; conversion=none; format_spec=none]): [dynamic source value: _summarise_status_error(e); conversion=none; format_spec=none] [dynamic source value: _payload_shape(messages, str(e)); conversion=none; format_spec=none]
}
```

## sent — source lines 1017–1017

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1017-1017
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## prompt — source lines 1032–1033

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `_summarise_status_error(e); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:1032-1033
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OpenAI call failed (status=[dynamic source value: e.status_code; conversion=none; format_spec=none], model=[dynamic source value: model; conversion=none; format_spec=none]): [dynamic source value: _summarise_status_error(e); conversion=none; format_spec=none]
}
```

## where — source lines 1049–1049

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1049-1049
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: mid-stream
}
```

## prompt — source lines 1060–1066

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `where; conversion=none; format_spec=none`
- `attempts; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `e; conversion=none; format_spec=none`
- `detail; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:1060-1066
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OpenAI [dynamic source value: where; conversion=none; format_spec=none] error after [dynamic source value: attempts; conversion=none; format_spec=none] attempts (model=[dynamic source value: model; conversion=none; format_spec=none]): [dynamic source value: e; conversion=none; format_spec=none] cause: [dynamic source value: detail; conversion=none; format_spec=none] hint: CERTIFICATE_VERIFY_FAILED → set openai.ca_cert in config.yaml; 'Illegal header value' → OPENAI_API_KEY has trailing whitespace; otherwise check HTTPS_PROXY / OPENAI_BASE_URL.
}
```

## out_tokens — source lines 1099–1099

Source context: callable `prompt`; enclosing call `u.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1099-1099
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: completion_tokens
}
```

## flat[f'prompt_tokens_details.{k}'] — source lines 1128–1128

Source context: callable `_note_unparsed_cache_keys`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `k; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:1128-1128
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_tokens_details.[dynamic source value: k; conversion=none; format_spec=none]
}
```

## user_content — source lines 631–631

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:631-631
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_control
}
```

## prompt — source lines 679–679

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:679-679
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: response_format
}
```

## prompt — source lines 680–680

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:680-680
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## produced — source lines 783–783

Source context: callable `prompt`; enclosing call `norm.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:783-783
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_tokens
}
```

## reasoning_tokens — source lines 784–784

Source context: callable `prompt`; enclosing call `norm.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:784-784
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_tokens
}
```

## prompt — source lines 789–790

Source context: callable `prompt`; enclosing call `TruncatedResponseError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:789-790
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reply still hit the output-token budget after the doubled retry
}
```

## prompt — source lines 791–792

Source context: callable `prompt`; enclosing call `TruncatedResponseError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:791-792
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reply hit the output-token budget with no retry budget left
}
```

## prompt — source lines 850–851

Source context: callable `prompt`; enclosing call `TruncatedResponseError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `redact(_scrub_secrets(str(e)))[:200]; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:850-851
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: provider rejected the doubled output budget as over its cap: [dynamic source value: redact(_scrub_secrets(str(e)))[:200]; conversion=none; format_spec=none]
}
```

## prompt — source lines 863–864

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:863-864
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] [dynamic source value: model; conversion=none; format_spec=none] rejected `temperature` — retrying without it
}
```

## prompt — source lines 960–962

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `attempt; conversion=none; format_spec=none`
- `attempts; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `wait; conversion=none; format_spec=f'.1f'`

```sudo
// Source: vvaharness/backends/llm/openai.py:960-962
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] transient [dynamic source value: e.status_code; conversion=none; format_spec=none] (attempt [dynamic source value: attempt; conversion=none; format_spec=none]/[dynamic source value: attempts; conversion=none; format_spec=none], model=[dynamic source value: model; conversion=none; format_spec=none]); retrying in [dynamic source value: wait; conversion=none; format_spec=f'.1f']s
}
```

## prompt — source lines 1005–1007

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `attempt; conversion=none; format_spec=none`
- `attempts; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `wait; conversion=none; format_spec=f'.1f'`

```sudo
// Source: vvaharness/backends/llm/openai.py:1005-1007
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] transient [dynamic source value: e.status_code; conversion=none; format_spec=none] (attempt [dynamic source value: attempt; conversion=none; format_spec=none]/[dynamic source value: attempts; conversion=none; format_spec=none], model=[dynamic source value: model; conversion=none; format_spec=none]); retrying in [dynamic source value: wait; conversion=none; format_spec=f'.1f']s
}
```

## prompt — source lines 1014–1015

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `server_error_exc.status_code; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `_summarise_status_error(server_error_exc); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:1014-1015
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OpenAI call failed (status=[dynamic source value: server_error_exc.status_code; conversion=none; format_spec=none], model=[dynamic source value: model; conversion=none; format_spec=none]): [dynamic source value: _summarise_status_error(server_error_exc); conversion=none; format_spec=none]
}
```

## kw['reasoning_effort'] — source lines 1027–1027

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1027-1027
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## prompt — source lines 1055–1056

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `where; conversion=none; format_spec=none`
- `attempt; conversion=none; format_spec=none`
- `attempts; conversion=none; format_spec=none`
- `detail; conversion=none; format_spec=none`
- `wait; conversion=none; format_spec=f'.1f'`

```sudo
// Source: vvaharness/backends/llm/openai.py:1055-1056
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] [dynamic source value: where; conversion=none; format_spec=none] error (attempt [dynamic source value: attempt; conversion=none; format_spec=none]/[dynamic source value: attempts; conversion=none; format_spec=none]): [dynamic source value: detail; conversion=none; format_spec=none] — retrying in [dynamic source value: wait; conversion=none; format_spec=f'.1f']s
}
```

## prompt — source lines 1089–1089

Source context: callable `prompt`; enclosing call `u.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1089-1089
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_tokens
}
```

## prompt — source lines 1090–1090

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1090-1090
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_read_input_tokens
}
```

## prompt — source lines 1091–1091

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `written; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:1091-1091
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , cache_write=[dynamic source value: written; conversion=none; format_spec=none]
}
```

## prompt — source lines 1092–1092

Source context: callable `prompt`; enclosing call `u.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:1092-1092
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: completion_tokens
}
```

## finish — source lines 732–732

Source context: callable `prompt`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:732-732
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: finish_reason
}
```

## prompt — source lines 769–771

Source context: callable `prompt`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `budget_key; conversion=none; format_spec=none`
- `requested_now; conversion=none; format_spec=none`
- `retry_at; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:769-771
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: VVAH-E005 warning: reply truncated at [dynamic source value: budget_key; conversion=none; format_spec=none]=[dynamic source value: requested_now; conversion=none; format_spec=none]; retrying once at [dynamic source value: retry_at; conversion=none; format_spec=none]
}
```

## prompt — source lines 826–826

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:826-826
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: learned_cap:[dynamic source value: model; conversion=none; format_spec=none]
}
```

## prompt — source lines 827–832

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `budget_key_now; conversion=none; format_spec=none`
- `kw[budget_key_now]; conversion=none; format_spec=none`
- `learned; conversion=none; format_spec=none`
- `learned; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:827-832
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [openai]: [dynamic source value: model; conversion=none; format_spec=none] rejected [dynamic source value: budget_key_now; conversion=none; format_spec=none]=[dynamic source value: kw[budget_key_now]; conversion=none; format_spec=none] — learned its real output cap ([dynamic source value: learned; conversion=none; format_spec=none]) from the gateway's own error and will use it for the rest of this process.
  The request retains this source rule, criterion or rationale, with its original modal force: Set models.<role>.max_tokens: [dynamic source value: learned; conversion=none; format_spec=none] to skip this extra round-trip next time.
}
```

## produced — source lines 845–845

Source context: callable `prompt`; enclosing call `stale.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:845-845
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_tokens
}
```

## prompt — source lines 867–867

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:867-867
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_completion_tokens
}
```

## prompt — source lines 867–867

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:867-867
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_completion_tokens
}
```

## kw['max_tokens'] — source lines 869–869

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:869-869
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## kw['max_tokens'] — source lines 869–869

Source context: callable `prompt`; enclosing call `kw.pop`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:869-869
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_completion_tokens
}
```

## prompt — source lines 870–871

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:870-871
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] [dynamic source value: model; conversion=none; format_spec=none] rejected `max_completion_tokens` — retrying with legacy `max_tokens`
}
```

## prompt — source lines 988–991

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `auth_attempt + 1; conversion=none; format_spec=none`
- `_AUTH_MAX_RETRIES_OAI; conversion=none; format_spec=none`
- `wait; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:988-991
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] authentication error (status=[dynamic source value: e.status_code; conversion=none; format_spec=none], attempt [dynamic source value: auth_attempt + 1; conversion=none; format_spec=none]/[dynamic source value: _AUTH_MAX_RETRIES_OAI; conversion=none; format_spec=none]); retrying in [dynamic source value: wait; conversion=none; format_spec=none]s
}
```

## prompt — source lines 1041–1041

Source context: callable `prompt`; enclosing call `call_timeout_error`; keyword `cause_text`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `request_timeout; conversion=none; format_spec=f'g'`

```sudo
// Source: vvaharness/backends/llm/openai.py:1041-1041
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OpenAI request exceeded [dynamic source value: request_timeout; conversion=none; format_spec=f'g']s
}
```

## prompt — source lines 810–810

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:810-810
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## prompt — source lines 810–810

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:810-810
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## prompt — source lines 811–811

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:811-811
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: for the rest of this run
}
```

## prompt — source lines 811–811

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:811-811
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: for this call
}
```

## prompt — source lines 873–873

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:873-873
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## prompt — source lines 873–873

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:873-873
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_completion_tokens
}
```

## kw['max_completion_tokens'] — source lines 874–874

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:874-874
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_completion_tokens
}
```

## kw['max_completion_tokens'] — source lines 874–874

Source context: callable `prompt`; enclosing call `kw.pop`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:874-874
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## prompt — source lines 875–876

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:875-876
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] [dynamic source value: model; conversion=none; format_spec=none] requires `max_completion_tokens` — retrying
}
```

## agentic — source lines 2015–2016

Source context: callable `agentic`; enclosing call `messages.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `str(exc)[:600]; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:2015-2016
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Rejected: [dynamic source value: str(exc)[:600]; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Fix the named fields and call the tool again.
}
```

## prompt — source lines 856–856

Source context: callable `prompt`; enclosing call `stale.get`; keyword `reasoning_tokens`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:856-856
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_tokens
}
```

## prompt — source lines 878–878

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:878-878
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_cache_key
}
```

## prompt — source lines 878–878

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:878-878
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_cache_key
}
```

## prompt — source lines 883–883

Source context: callable `prompt`; enclosing call `kw.pop`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:883-883
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_cache_key
}
```

## prompt — source lines 884–885

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:884-885
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [openai] [dynamic source value: model; conversion=none; format_spec=none] rejected `prompt_cache_key` — retrying without it
}
```

## prompt — source lines 774–774

Source context: callable `prompt`; enclosing call `discarded.get`; keyword `produced`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:774-774
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_tokens
}
```

## prompt — source lines 887–887

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:887-887
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: json_schema
}
```

## prompt — source lines 888–888

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:888-888
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: json_schema
}
```

## kw['response_format'] — source lines 893–893

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:893-893
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: response_format
}
```

## kw['response_format'] — source lines 893–893

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:893-893
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: json_object
}
```

## prompt — source lines 895–895

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:895-895
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: json_schema:[dynamic source value: model; conversion=none; format_spec=none]
}
```

## prompt — source lines 896–902

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:896-902
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [openai]: [dynamic source value: model; conversion=none; format_spec=none] rejected `response_format` type json_schema (Structured Outputs) — falling back to json_object mode for the rest of this run.
  The request retains this source rule, criterion or rationale, with its original modal force: Replies are syntactically valid JSON but NOT schema-validated, so a stage that needs a validated payload depends on its own parser; route that role via: sdk, cli or deepagents for enforced structured output.
}
```

## prompt — source lines 904–904

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:904-904
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## sent — source lines 908–908

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:908-908
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## prompt — source lines 911–911

Source context: callable `prompt`; enclosing call `kw.pop`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:911-911
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## prompt — source lines 912–912

Source context: callable `prompt`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:912-912
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: llm_effort_field_dropped
}
```

## prompt — source lines 914–914

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:914-914
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort_field:[dynamic source value: model; conversion=none; format_spec=none]
}
```

## prompt — source lines 915–917

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:915-917
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [openai]: [dynamic source value: model; conversion=none; format_spec=none] rejected `reasoning_effort` as an unsupported parameter — retrying without it for the rest of this run.
}
```

## prompt — source lines 927–927

Source context: callable `prompt`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:927-927
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: llm_effort_tier_stepped_down
}
```

## prompt — source lines 929–929

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `sent; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:929-929
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort:[dynamic source value: model; conversion=none; format_spec=none]:[dynamic source value: sent; conversion=none; format_spec=none]
}
```

## prompt — source lines 930–931

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `sent; conversion=repr; format_spec=none`
- `_next_effort_label(nxt); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:930-931
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [openai]: [dynamic source value: model; conversion=none; format_spec=none] rejected reasoning_effort=[dynamic source value: sent; conversion=repr; format_spec=none] — retrying at [dynamic source value: _next_effort_label(nxt); conversion=none; format_spec=none].
}
```

## prompt — source lines 933–933

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:933-933
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stream_options
}
```

## prompt — source lines 933–933

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:933-933
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stream_options
}
```

## prompt — source lines 937–937

Source context: callable `prompt`; enclosing call `kw.pop`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:937-937
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stream_options
}
```

## prompt — source lines 939–939

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:939-939
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stream_options:[dynamic source value: model; conversion=none; format_spec=none]
}
```

## prompt — source lines 940–942

Source context: callable `prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/openai.py:940-942
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [openai]: [dynamic source value: model; conversion=none; format_spec=none] rejected `stream_options` — retrying without it.
  The request retains this source rule, criterion or rationale, with its original modal force: Token usage is not reported on streamed calls to this endpoint, so cost figures for this role will read zero.
}
```

## prompt — source lines 888–888

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:888-888
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: response_format
}
```

## prompt — source lines 924–924

Source context: callable `prompt`; enclosing call `kw.pop`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:924-924
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

## kw['reasoning_effort'] — source lines 926–926

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai.py:926-926
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: reasoning_effort
}
```

