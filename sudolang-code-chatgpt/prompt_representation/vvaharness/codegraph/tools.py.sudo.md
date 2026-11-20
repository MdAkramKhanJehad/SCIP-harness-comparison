# vvaharness/codegraph/tools.py — model instruction carriers

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
// Source: vvaharness/codegraph/tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Read-only graph-query tools over ``ctx.graph_handle``; S2, S4 and S6 each build these.
}
```

## _qname — source lines 58–58

Source context: callable `_qname`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:58-58
Constraints {
  The advertised description supplied with this operation is a model-visible claim: A cypher row rendered as ``file::name``, or empty when either half is missing.
}
```

## _ref — source lines 64–64

Source context: callable `_ref`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:64-64
Constraints {
  The advertised description supplied with this operation is a model-visible claim: An entity rendered as ``file::name``, or its name alone when it carries no path.
}
```

## _refs — source lines 71–71

Source context: callable `_refs`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:71-71
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Up to ``_REF_CAP`` rendered entity references, dropping empties.
}
```

## _paths — source lines 76–76

Source context: callable `_paths`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:76-76
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Up to ``_PATH_CAP`` call paths, each an arrow-joined reference chain.
}
```

## _selector — source lines 82–82

Source context: callable `_selector`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:82-82
Constraints {
  The advertised description supplied with this operation is a model-visible claim: A ``SymbolSelector`` for *symbol* scoped to *file*, optionally pinned to *line*.
}
```

## _resolve_error — source lines 87–87

Source context: callable `_resolve_error`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:87-87
Constraints {
  The advertised description supplied with this operation is a model-visible claim: A usable answer when the graph cannot resolve *symbol*, instead of a raised tool error.
}
```

## _cypher_error — source lines 99–99

Source context: callable `_cypher_error`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:99-99
Constraints {
  The advertised description supplied with this operation is a model-visible claim: A usable answer when a direct graph query fails, instead of a raised tool error.
}
```

## _is_empty_result — source lines 104–104

Source context: callable `_is_empty_result`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:104-104
Constraints {
  The advertised description supplied with this operation is a model-visible claim: ``None``, an empty list, or a dict whose list-valued entries are all empty.
}
```

## _count_result — source lines 111–111

Source context: callable `_count_result`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:111-111
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Bumps exactly one ``graph_tool_result_{error,empty,hit}`` counter for *result*.
}
```

## _counted — source lines 121–121

Source context: callable `_counted`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:121-121
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Counts a graph tool's return value via :func:`_count_result`; place under ``@tool``.
}
```

## _community_files — source lines 131–131

Source context: callable `_community_files`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:131-131
Constraints {
  The advertised description supplied with this operation is a model-visible claim: ``ctx.modules`` re-keyed by module name.
}
```

## <module> — source lines 137–137

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:137-137
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Everything a graph-tool factory may read; grows by field, not by signature change.
}
```

## _context_tool — source lines 144–144

Source context: callable `_context_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:144-144
Constraints {
  The described operation is advertised for builds ``GraphContext``, the one-call neighbourhood query.; this description alone does not request its invocation.
}
```

## _impact_tool — source lines 169–169

Source context: callable `_impact_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:169-169
Constraints {
  The described operation is advertised for builds ``GraphImpact``, the transitive-reachability query.; this description alone does not request its invocation.
}
```

## _neighbors_tool — source lines 200–200

Source context: callable `_neighbors_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:200-200
Constraints {
  The described operation is advertised for builds ``GraphNeighbors`` as two single-MATCH queries; an OPTIONAL MATCH composite cartesian-products into QueryTimeoutError.; this description alone does not request its invocation.
}
```

## _community_of_tool — source lines 227–227

Source context: callable `_community_of_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:227-227
Constraints {
  The described operation is advertised for builds ``GraphCommunityOf``, a pure scan of ``ctx.modules`` that touches no graph.; this description alone does not request its invocation.
}
```

## _importers_tool — source lines 242–242

Source context: callable `_importers_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:242-242
Constraints {
  The described operation is advertised for builds ``GraphImporters``, the file-level inbound-import query.; this description alone does not request its invocation.
}
```

## _sinks_in_community_tool — source lines 258–258

Source context: callable `_sinks_in_community_tool`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:258-258
Constraints {
  The described operation is advertised for builds ``GraphSinksInCommunity``, joining ``ctx.unsafe_sinks`` onto a module's file set.; this description alone does not request its invocation.
}
```

## register_graph_tools — source lines 293–293

Source context: callable `register_graph_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:293-293
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Adds plugin graph tools; call before any stage opens a session, since names are read then.
}
```

## clear_plugin_graph_tools — source lines 301–301

Source context: callable `clear_plugin_graph_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:301-301
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Drops every registered plugin tool, leaving the built-ins; for tests and repeated scans.
}
```

## graph_tool_names — source lines 306–306

Source context: callable `graph_tool_names`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:306-306
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Built-in names then plugin names; a call, not a constant, so registration is not too late.
}
```

## _graph_tools — source lines 311–311

Source context: callable `_graph_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:311-311
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The graph tools named in *allowed*; empty when ``ctx`` carries no graph handle.
}
```

## build_graph_tool_builder — source lines 321–321

Source context: callable `build_graph_tool_builder`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:321-321
Constraints {
  The advertised description supplied with this operation is a model-visible claim: A ``ToolBuilder`` returning the generic reader tools followed by the graph tools.
}
```

## hint — source lines 89–90

Source context: callable `_resolve_error`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `symbol; conversion=none; format_spec=none`
- `file; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/codegraph/tools.py:89-90
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: several symbols named '[dynamic source value: symbol; conversion=none; format_spec=none]' exist in [dynamic source value: file; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Pass `line` to pick the one the model mean, or name the enclosing class or function so the name is unique.
}
```

## GraphContext — source lines 149–149

Source context: callable `GraphContext`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:149-149
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Callers, callees, imports, implementors and call paths of *symbol* in *file*, in one call.
  The advertised description supplied with this operation is a model-visible claim: Prefer this over GraphNeighbors. `file` is the exact repo-relative path; `symbol` is the bare defined name, not `Class.method`, a route, or a template; `line` disambiguates a name defined more than once in the file.
}
```

## GraphImpact — source lines 175–175

Source context: callable `GraphImpact`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:175-175
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Transitive reachability of *symbol*: direction "upstream" = everything that can reach it (an empty result means nothing calls it, so it is an entry point or dead code), "downstream" = everything it reaches. `file` is the exact repo-relative path; `symbol` is the bare defined name, not `Class.method`, a route, or a template; `line` disambiguates a name defined more than once in the file.
}
```

## GraphNeighbors — source lines 205–205

Source context: callable `GraphNeighbors`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:205-205
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Direct callers and callees of *function* defined in *file*. `file` is the exact repo-relative path; `function` is the bare defined name, not `Class.method`.
}
```

## GraphCommunityOf — source lines 232–232

Source context: callable `GraphCommunityOf`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:232-232
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Which module/community *file* belongs to, or None if unmapped. `file` is the exact repo-relative path.
}
```

## GraphImporters — source lines 247–247

Source context: callable `GraphImporters`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:247-247
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Files that import *file* — a trust-boundary signal, not a function-reachability check. `file` is the exact repo-relative path.
}
```

## GraphSinksInCommunity — source lines 263–263

Source context: callable `GraphSinksInCommunity`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:263-263
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Unsafe sinks whose file belongs to *community*.
}
```

## _build — source lines 325–325

Source context: callable `_build`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/codegraph/tools.py:325-325
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Gates on ``options.fact_tools``; streaming.py's parent_tools strips fact names out of allowed_tools, so gating on that alone builds nothing.
}
```

