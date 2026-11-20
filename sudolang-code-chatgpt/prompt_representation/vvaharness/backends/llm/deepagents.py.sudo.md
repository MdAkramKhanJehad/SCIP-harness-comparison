# vvaharness/backends/llm/deepagents.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _OVERSIZE_PROMPT_COUNTER — source lines 256–256

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:256-256
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: deepagents_oversize_prompts
}
```

## _MODEL_CALL_BUDGET_CLAUSE — source lines 1068–1068

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:1068-1068
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `max_model_calls` does not bound this session on this route — `max_turns` does
}
```

## _EVIDENCE_GATE_NO_STACK_CLAUSE — source lines 1070–1070

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:1070-1070
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the evidence gate's tool-call requirement cannot apply with no tool stack
}
```

## _check_prompt_ceiling — source lines 269–270

Source context: callable `_check_prompt_ceiling`; enclosing call `OversizePromptError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:269-270
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refused before dispatch; reduce what this call packs (chunk sizing / per-call caps) and re-run
}
```

## _warn_dropped_model_knobs — source lines 461–463

Source context: callable `_warn_dropped_model_knobs`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `model_id; conversion=repr; format_spec=none`
- `name; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/deepagents.py:461-463
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [deepagents]: models entry [dynamic source value: model_id; conversion=repr; format_spec=none] sets [dynamic source value: name; conversion=none; format_spec=none], which the deepagents route never sends — ignored.
  The request retains this source rule, criterion or rationale, with its original modal force: Route this role via: sdk (or via: openai) to have it honoured.
}
```

## think_in_prompt_enabled — source lines 952–952

Source context: callable `think_in_prompt_enabled`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:952-952
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: think_in_prompt
}
```

## _resume_agentic_deepagents — source lines 1170–1170

Source context: callable `_resume_agentic_deepagents`; enclosing call `SessionNotResumableError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `session_id; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/deepagents.py:1170-1170
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: session [dynamic source value: session_id; conversion=repr; format_spec=none] was never pinned or has been released
}
```

## raw — source lines 372–372

Source context: callable `_retry_after_seconds`; enclosing call `headers.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:372-372
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: retry-after
}
```

## dispatch_prompt — source lines 988–988

Source context: callable `dispatch_prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `via; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/deepagents.py:988-988
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: prompt_no_tools:[dynamic source value: via; conversion=none; format_spec=none]
}
```

## dispatch_prompt — source lines 989–990

Source context: callable `dispatch_prompt`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `via; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/deepagents.py:989-990
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [[dynamic source value: via; conversion=none; format_spec=none]]: dispatch_prompt has no tool seam on this route — tool_builder/fact_tools/parent_middleware are accepted but ignored.
}
```

## raise_if_refused — source lines 692–692

Source context: callable `raise_if_refused`; enclosing call `getattr`; keyword `category`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:692-692
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refusal_category
}
```

## legacy_kw['json_schema'] — source lines 996–996

Source context: callable `dispatch_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:996-996
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: json_schema
}
```

## legacy_kw['response_model'] — source lines 998–998

Source context: callable `dispatch_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/deepagents.py:998-998
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: response_model
}
```

## dispatch_prompt — source lines 1001–1002

Source context: callable `dispatch_prompt`; enclosing call `ValueError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `via; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/deepagents.py:1001-1002
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: dispatch_prompt: response_model is not supported on via=[dynamic source value: via; conversion=repr; format_spec=none] (only deepagents/sdk/cli/openai)
}
```

