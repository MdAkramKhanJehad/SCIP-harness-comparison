# vvaharness/backends/llm/cli/session.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _FINAL_ANSWER_INSTRUCTION — source lines 146–148

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/session.py:146-148
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model's turn limit was reached.
  The request retains this source rule, criterion or rationale, with its original modal force: Give the model's final answer now, in the exact format the original instructions asked for, using only what the model already have.
  The requested model behavior excludes use any tool.
}
```

## cmd — source lines 166–166

Source context: callable `_finalize_via_resume`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/session.py:166-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --output-format
}
```

## _finalize_via_resume — source lines 168–168

Source context: callable `_finalize_via_resume`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/session.py:168-168
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: json_schema
}
```

## _finalize_via_resume — source lines 169–169

Source context: callable `_finalize_via_resume`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/llm/cli/session.py:169-169
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --json-schema
}
```

## resume_agentic — source lines 238–238

Source context: callable `resume_agentic`; enclosing call `SessionNotResumableError`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `session_id; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/session.py:238-238
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cli session [dynamic source value: session_id; conversion=repr; format_spec=none] was never pinned or has been released
}
```

## deny — source lines 300–300

Source context: callable `_confinement_argv`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `d; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/cli/session.py:300-300
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Read(./[dynamic source value: d; conversion=none; format_spec=none]/**)
}
```

## agentic — source lines 370–372

Source context: callable `agentic`; enclosing call `warn_once`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/backends/llm/cli/session.py:370-372
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [cli] WARN: this `claude` build does not advertise --json-schema; the agentic reply is not schema-validated and the caller must salvage it from free text.
}
```

