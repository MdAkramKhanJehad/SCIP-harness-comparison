# vvaharness/backends/llm/openai_responses.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## kwargs['prompt_cache_key'] — source lines 215–215

Source context: callable `_responses_only_kwargs`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai_responses.py:215-215
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_cache_key
}
```

## prompt_details — source lines 260–260

Source context: callable `usage_as_chat`; enclosing call `_get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai_responses.py:260-260
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: input_tokens_details
}
```

## _text_input_item — source lines 140–140

Source context: callable `_text_input_item`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/openai_responses.py:140-140
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: output_text
}
```

## to_responses_tools — source lines 90–90

Source context: callable `to_responses_tools`; enclosing call `fn.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/openai_responses.py:90-90
Constraints {
  The advertised description supplied with this operation is a model-visible claim: description
}
```

