# vvaharness/backends/llm/tools.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## <module> — source lines 15–15

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Sandboxed Read/Glob/Grep for non-CLI backends (sdk.py, openai.py); skips shelling to `claude`.
}
```

## _always_allowed — source lines 45–45

Source context: callable `_always_allowed`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:45-45
Constraints {
  The advertised description supplied with this operation is a model-visible claim: True when *rel* is harness-injected content exempt from inventory scoping.
}
```

## set_scope — source lines 50–50

Source context: callable `set_scope`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:50-50
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Register the scan's in-scope file inventory (repo-relative posix paths) for *root*.
}
```

## _excluded_rel — source lines 66–66

Source context: callable `_excluded_rel`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:66-66
Constraints {
  The advertised description supplied with this operation is a model-visible claim: True when the repo-relative posix path is outside the tool read surface: under an always-excluded directo...
}
```

## _excluded_target — source lines 76–76

Source context: callable `_excluded_target`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:76-76
Constraints {
  The advertised description supplied with this operation is a model-visible claim: _excluded_rel for an explicit Grep target, which unlike a Read target may name a directory.
}
```

## _is_binary_text — source lines 104–104

Source context: callable `_is_binary_text`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:104-104
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Cheap binary sniff on the decoded head: a null byte is the conventional test; a high U+FFFD density catch...
}
```

## sanitize_packed_text — source lines 124–124

Source context: callable `sanitize_packed_text`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:124-124
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Guard *text* before it is packed into a prompt: binary content becomes a visible elision marker (never mo...
}
```

## cap_tool_result — source lines 135–135

Source context: callable `cap_tool_result`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:135-135
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Trim *result* to `TOOL_RESULT_CAP`, telling the model what was cut and how to re-read.
}
```

## _grep_wanted — source lines 208–208

Source context: callable `_grep_wanted`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:208-208
Constraints {
  The advertised description supplied with this operation is a model-visible claim: True when *rel*, or its basename, matches *glob* — or no glob was given.
}
```

## _grep_skip_harness — source lines 216–216

Source context: callable `_grep_skip_harness`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:216-216
Constraints {
  The advertised description supplied with this operation is a model-visible claim: True when *rel* is harness skill content a walk that did not name it must not surface.
}
```

## _grep_files — source lines 234–234

Source context: callable `_grep_files`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:234-234
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Resolve the Grep file list for *path*/*glob*, or an ERROR string on a bad/excluded path.
}
```

## _emit_grep_match — source lines 259–259

Source context: callable `_emit_grep_match`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:259-259
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Append one match (with its context window, if any) to *out*; return the lines it cost.
}
```

## schemas_for — source lines 375–375

Source context: callable `schemas_for`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:375-375
Constraints {
  The described operation advertises this return/result contract: OpenAI `tools=[...]` entries for the requested tool names.
}
```

## anthropic_schemas_for — source lines 386–386

Source context: callable `anthropic_schemas_for`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:386-386
Constraints {
  The described operation advertises this return/result contract: Anthropic Messages-API `tools=[...]` entries for the requested tool names.
}
```

## summarize_args — source lines 404–404

Source context: callable `summarize_args`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:404-404
Constraints {
  The described operation advertises this return/result contract: a bounded, non-sensitive summary for a local-tool invocation.
}
```

## cap_tool_result — source lines 140–141

Source context: callable `cap_tool_result`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `extra; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/llm/tools.py:140-141
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: …[truncated [dynamic source value: extra; conversion=none; format_spec=none] chars to fit context — re-read a specific line range with Read offset/limit if the model need more]
}
```

## _SCHEMAS — source lines 317–317

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:317-317
Constraints {
  The described operation is advertised for read a file from the repository.; this description alone does not request its invocation.
  The described operation advertises this return/result contract: numbered lines.
}
```

## _SCHEMAS — source lines 332–333

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:332-333
Constraints {
  The described operation is advertised for list files in the repository matching a glob pattern (e.g. **/*.java).; this description alone does not request its invocation.
}
```

## _SCHEMAS — source lines 343–344

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:343-344
Constraints {
  The described operation is advertised for search file contents for a regex.; this description alone does not request its invocation.
  The described operation advertises this return/result contract: file:line:text for each match.
}
```

## _SCHEMAS — source lines 322–322

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:322-322
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Path relative to the repo root
}
```

## _SCHEMAS — source lines 324–324

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:324-324
Constraints {
  The advertised description supplied with this operation is a model-visible claim: 0-based line to start from (default 0)
}
```

## _SCHEMAS — source lines 326–326

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:326-326
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Max lines to return (default 2000)
}
```

## _SCHEMAS — source lines 349–349

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:349-349
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Python regex
}
```

## _SCHEMAS — source lines 351–351

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:351-351
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Restrict to this file or directory
}
```

## _SCHEMAS — source lines 353–353

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:353-353
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Restrict to files matching this glob
}
```

## _SCHEMAS — source lines 356–356

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:356-356
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Lines of context around each match
}
```

## anthropic_schemas_for — source lines 392–392

Source context: callable `anthropic_schemas_for`; enclosing call `out.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/llm/tools.py:392-392
Constraints {
  The advertised description supplied with this operation is a model-visible claim: description
}
```

