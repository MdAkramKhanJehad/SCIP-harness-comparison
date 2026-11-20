# vvaharness/backends/llm/sdk.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _cache_route — source lines 341–347

Source context: callable `_cache_route`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/backends/llm/sdk.py:341-347
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] note: prompt caching is enabled by default, but the configured endpoint is not recognised as Anthropic, Vertex or Bedrock (route classification: unknown), so cache markers are withheld and prompt tokens are billed uncached on this route.
  The requested conditional/temporal rule is: If the gateway is Anthropic-Messages-compatible, set `cache_route: anthropic` in your config to enable prompt caching.
  The request retains this source rule, criterion or rationale, with its original modal force: This affects cost only; scan results are unchanged.
}
```

## kw — source lines 723–723

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:723-723
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## prompt — source lines 774–780

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `f' [{tag}]' if tag else ''; conversion=none; format_spec=none`
- `_up_chars; conversion=none; format_spec=none`
- `max_tok; conversion=none; format_spec=none`
- `f', T={temperature}' if 'temperature' in kw.get('extra_body', {}) else ''; conversion=none; format_spec=none`
- `f', thinking={thinking_budget}' if 'thinking' in kw and (not effort_kw) else ''; conversion=none; format_spec=none`
- `f', effort={effort}' if effort_kw else ''; conversion=none; format_spec=none`
- `request_timeout; conversion=none; format_spec=f'g'`

```sudo
// Source: vvaharness/backends/llm/sdk.py:774-780
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] prompt -> [dynamic source value: model; conversion=none; format_spec=none][dynamic source value: f' [{tag}]' if tag else ''; conversion=none; format_spec=none] ([dynamic source value: _up_chars; conversion=none; format_spec=none] chars, max_tokens=[dynamic source value: max_tok; conversion=none; format_spec=none][dynamic source value: f', T={temperature}' if 'temperature' in kw.get('extra_body', {}) else ''; conversion=none; format_spec=none][dynamic source value: f', thinking={thinking_budget}' if 'thinking' in kw and (not effort_kw) else ''; conversion=none; format_spec=none][dynamic source value: f', effort={effort}' if effort_kw else ''; conversion=none; format_spec=none], timeout=[dynamic source value: request_timeout; conversion=none; format_spec=f'g']s)
}
```

## category — source lines 587–587

Source context: callable `_refusal_category`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:587-587
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stop_details
}
```

## _raise_if_refused — source lines 593–593

Source context: callable `_raise_if_refused`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:593-593
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stop_reason
}
```

## kw['extra_headers'] — source lines 739–739

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:739-739
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: extra_headers
}
```

## prompt — source lines 962–964

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `sorted(kw); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:962-964
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Anthropic SDK call to [dynamic source value: model; conversion=none; format_spec=none] exhausted all retries without a successful response (every attempt hit a parameter-drop retry).
  The request retains this source rule, criterion or rationale, with its original modal force: Final request kwargs keys: [dynamic source value: sorted(kw); conversion=none; format_spec=none].
}
```

## out — source lines 974–974

Source context: callable `prompt`; enclosing call `usage.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:974-974
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_tokens
}
```

## cache_info — source lines 975–975

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `cr; conversion=none; format_spec=none`
- `cw; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:975-975
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (cache_read=[dynamic source value: cr; conversion=none; format_spec=none], cache_write=[dynamic source value: cw; conversion=none; format_spec=none])
}
```

## prompt — source lines 976–976

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_in; conversion=none; format_spec=none`
- `cache_info; conversion=none; format_spec=none`
- `out; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:976-976
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] usage: in=[dynamic source value: _in; conversion=none; format_spec=none][dynamic source value: cache_info; conversion=none; format_spec=none] out=[dynamic source value: out; conversion=none; format_spec=none]
}
```

## _build_system_content — source lines 453–453

Source context: callable `_build_system_content`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:453-453
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_control
}
```

## kw['tool_choice'] — source lines 732–732

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:732-732
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tool_choice
}
```

## kw['max_tokens'] — source lines 746–746

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:746-746
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## cr — source lines 972–972

Source context: callable `prompt`; enclosing call `usage.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:972-972
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_read_input_tokens
}
```

## cw — source lines 973–973

Source context: callable `prompt`; enclosing call `usage.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:973-973
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_creation_input_tokens
}
```

## _get_client — source lines 232–237

Source context: callable `_get_client`; enclosing call `AuthenticationError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/backends/llm/sdk.py:232-237
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: no sdk credential resolved: set ANTHROPIC_SDK_API_KEY or `sdk.api_key` in the model's config. ANTHROPIC_API_KEY is accepted only when sdk/deepagents are the sole backends in the profile (sdk.allow_api_key_fallback), so it is deliberately NOT read here — an ambient key must never silently bill a run whose via:cli roles authenticate as someone else.
}
```

## kw.setdefault('extra_body', {})['temperature'] — source lines 755–755

Source context: callable `prompt`; enclosing call `kw.setdefault`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:755-755
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: extra_body
}
```

## prompt — source lines 758–759

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `temperature; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:758-759
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] note: [dynamic source value: model; conversion=none; format_spec=none] does not accept `temperature`; dropping T=[dynamic source value: temperature; conversion=none; format_spec=none] for this and subsequent calls
}
```

## prompt — source lines 774–774

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:774-774
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: tag; conversion=none; format_spec=none]]
}
```

## prompt — source lines 777–777

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `temperature; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:777-777
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , T=[dynamic source value: temperature; conversion=none; format_spec=none]
}
```

## prompt — source lines 778–778

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `thinking_budget; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:778-778
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , thinking=[dynamic source value: thinking_budget; conversion=none; format_spec=none]
}
```

## prompt — source lines 779–779

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `effort; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:779-779
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: , effort=[dynamic source value: effort; conversion=none; format_spec=none]
}
```

## requested_now — source lines 811–811

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:811-811
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## prompt — source lines 932–933

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `redact(body); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:932-933
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Anthropic SDK call failed (status=[dynamic source value: e.status_code; conversion=none; format_spec=none], model=[dynamic source value: model; conversion=none; format_spec=none]): [dynamic source value: redact(body); conversion=none; format_spec=none]
}
```

## prompt — source lines 952–957

Source context: callable `prompt`; enclosing call `RuntimeError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `attempts; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `redact(str(e)); conversion=none; format_spec=none`
- `redact(cause_chain(e) or 'no underlying cause reported'); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:952-957
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Anthropic SDK connection error after [dynamic source value: attempts; conversion=none; format_spec=none] attempts (model=[dynamic source value: model; conversion=none; format_spec=none]): [dynamic source value: redact(str(e)); conversion=none; format_spec=none] cause: [dynamic source value: redact(cause_chain(e) or 'no underlying cause reported'); conversion=none; format_spec=none] hint: this is a network/TLS/DNS/proxy failure, not an auth/model error.
  The request retains this source rule, criterion or rationale, with its original modal force: Behind a TLS-intercepting proxy set SSL_CERT_FILE to the model's CA bundle, and check HTTPS_PROXY / ANTHROPIC_SDK_BASE_URL.
}
```

## _in — source lines 969–969

Source context: callable `prompt`; enclosing call `usage.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:969-969
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: input_tokens
}
```

## _in — source lines 971–971

Source context: callable `prompt`; enclosing call `usage.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:971-971
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_read_input_tokens
}
```

## produced — source lines 810–810

Source context: callable `prompt`; enclosing call `clipped_usage.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:810-810
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_tokens
}
```

## prompt — source lines 844–845

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:844-845
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] [dynamic source value: model; conversion=none; format_spec=none] rejected `temperature` — retrying without it
}
```

## prompt — source lines 874–876

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model; conversion=none; format_spec=none`
- `kw['thinking']; conversion=none; format_spec=none`
- `'' if unsupported else ' (this request only)'; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:874-876
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] [dynamic source value: model; conversion=none; format_spec=none] rejected extended thinking ([dynamic source value: kw['thinking']; conversion=none; format_spec=none]) — retrying without it[dynamic source value: '' if unsupported else ' (this request only)'; conversion=none; format_spec=none]
}
```

## prompt — source lines 925–927

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `attempt; conversion=none; format_spec=none`
- `attempts; conversion=none; format_spec=none`
- `model; conversion=none; format_spec=none`
- `wait; conversion=none; format_spec=f'.1f'`

```sudo
// Source: vvaharness/backends/llm/sdk.py:925-927
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] transient error (status=[dynamic source value: e.status_code; conversion=none; format_spec=none], attempt [dynamic source value: attempt; conversion=none; format_spec=none]/[dynamic source value: attempts; conversion=none; format_spec=none], model=[dynamic source value: model; conversion=none; format_spec=none]); retrying in [dynamic source value: wait; conversion=none; format_spec=f'.1f']s
}
```

## prompt — source lines 947–948

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `attempt; conversion=none; format_spec=none`
- `attempts; conversion=none; format_spec=none`
- `e; conversion=none; format_spec=none`
- `wait; conversion=none; format_spec=f'.1f'`

```sudo
// Source: vvaharness/backends/llm/sdk.py:947-948
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] connection error (attempt [dynamic source value: attempt; conversion=none; format_spec=none]/[dynamic source value: attempts; conversion=none; format_spec=none]): [dynamic source value: e; conversion=none; format_spec=none] — retrying in [dynamic source value: wait; conversion=none; format_spec=f'.1f']s
}
```

## _in — source lines 970–970

Source context: callable `prompt`; enclosing call `usage.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:970-970
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cache_creation_input_tokens
}
```

## agentic — source lines 1575–1577

Source context: callable `agentic`; enclosing call `messages.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_RESPONSE_MODEL_TOOL_NAME; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:1575-1577
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Tool budget exhausted.
  The request retains this source rule, criterion or rationale, with its original modal force: Call [dynamic source value: _RESPONSE_MODEL_TOOL_NAME; conversion=none; format_spec=none] now with the model's best answer based on what the model have read so far.
}
```

## agentic — source lines 1583–1585

Source context: callable `agentic`; enclosing call `messages.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:1583-1585
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Tool budget exhausted.
  The request retains this source rule, criterion or rationale, with its original modal force: Reply now with the model's final answer based on what the model have read so far; do not call any tool.
}
```

## prompt — source lines 777–777

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:777-777
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: extra_body
}
```

## prompt — source lines 825–827

Source context: callable `prompt`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `requested_now; conversion=none; format_spec=none`
- `retry_at; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:825-827
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: VVAH-E005 warning: reply truncated at max_tokens=[dynamic source value: requested_now; conversion=none; format_spec=none]; retrying once at [dynamic source value: retry_at; conversion=none; format_spec=none]
}
```

## kw['max_tokens'] — source lines 830–830

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:830-830
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_tokens
}
```

## prompt — source lines 841–841

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:841-841
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: extra_body
}
```

## unsupported — source lines 869–869

Source context: callable `prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:869-869
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: not supported
}
```

## prompt — source lines 881–881

Source context: callable `prompt`; enclosing call `kw.pop`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:881-881
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_config
}
```

## prompt — source lines 908–911

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e.status_code; conversion=none; format_spec=none`
- `auth_attempt + 1; conversion=none; format_spec=none`
- `_AUTH_MAX_RETRIES_SDK; conversion=none; format_spec=none`
- `wait; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:908-911
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [sdk] authentication error (status=[dynamic source value: e.status_code; conversion=none; format_spec=none], attempt [dynamic source value: auth_attempt + 1; conversion=none; format_spec=none]/[dynamic source value: _AUTH_MAX_RETRIES_SDK; conversion=none; format_spec=none]); retrying in [dynamic source value: wait; conversion=none; format_spec=none]s
}
```

## prompt — source lines 939–939

Source context: callable `prompt`; enclosing call `call_timeout_error`; keyword `cause_text`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `request_timeout; conversion=none; format_spec=f'g'`

```sudo
// Source: vvaharness/backends/llm/sdk.py:939-939
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Anthropic SDK request exceeded [dynamic source value: request_timeout; conversion=none; format_spec=f'g']s
}
```

## prompt — source lines 846–846

Source context: callable `prompt`; enclosing call `kw.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:846-846
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: extra_body
}
```

## agentic — source lines 1521–1522

Source context: callable `agentic`; enclosing call `results.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `str(exc)[:600]; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/sdk.py:1521-1522
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Rejected: [dynamic source value: str(exc)[:600]; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Fix the named fields and call the tool again.
}
```

## prompt — source lines 876–876

Source context: callable `prompt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:876-876
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (this request only)
}
```

## prompt — source lines 954–954

Source context: callable `prompt`; enclosing call `redact`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/sdk.py:954-954
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: no underlying cause reported
}
```

