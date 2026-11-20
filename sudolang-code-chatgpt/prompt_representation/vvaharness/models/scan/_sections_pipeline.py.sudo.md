# vvaharness/models/scan/_sections_pipeline.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _render_pipeline_diagnostics — source lines 141–142

Source context: callable `_render_pipeline_diagnostics`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `m.s3_threats_without_unit; conversion=none; format_spec=none`
- `listed; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_pipeline.py:141-142
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Threats with no investigation unit minted: [dynamic source value: m.s3_threats_without_unit; conversion=none; format_spec=none][dynamic source value: listed; conversion=none; format_spec=none] — never reviewed.
}
```

## _render_pipeline_diagnostics — source lines 202–212

Source context: callable `_render_pipeline_diagnostics`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `m.llm_adapter_evidence_gate_unenforced; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_pipeline.py:202-212
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Verdicts reached without a required fact-tool call on via: sdk / via: openai: [dynamic source value: m.llm_adapter_evidence_gate_unenforced; conversion=none; format_spec=none] (`llm_adapter_evidence_gate_unenforced`) — an agentic session produced a verdict without calling a fact tool its stage's evidence gate required.
  The request retains this source rule, criterion or rationale, with its original modal force: The in-loop gate that would have rejected that verdict and re-asked is deepagents-only (neither raw provider loop has the seam), so this count plus a one-time WARN is the whole enforcement: those verdicts were reached from the prompt alone.
  The request retains this source rule, criterion or rationale, with its original modal force: Route the stage via: deepagents if the gate must actually hold.
}
```

## _render_pipeline_diagnostics — source lines 216–224

Source context: callable `_render_pipeline_diagnostics`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `m.cli_mcp_evidence_gate_unenforced; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_pipeline.py:216-224
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Verdicts reached without a required fact-tool call on via: cli: [dynamic source value: m.cli_mcp_evidence_gate_unenforced; conversion=none; format_spec=none] (`cli_mcp_evidence_gate_unenforced`) — the same evidence-gate shortfall on the via: cli MCP-bridged tool loop: a session with graph tools and require_graph produced a verdict without calling any of the required fact tools. via: cli has no in-loop seam either, so this count plus a one-time WARN is the whole enforcement on that route.
  The request retains this source rule, criterion or rationale, with its original modal force: Route the stage via: deepagents if the gate must actually hold.
}
```

## _render_pipeline_diagnostics — source lines 229–238

Source context: callable `_render_pipeline_diagnostics`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `m.s6_confirmed_without_vector; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_pipeline.py:229-238
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Verified findings confirmed with no CVSS vector: [dynamic source value: m.s6_confirmed_without_vector; conversion=none; format_spec=none] (`s6_confirmed_without_vector`) — a TRUE_POSITIVE verdict, or a verifier-discovered finding kept above the confidence floor, with no `cvss_vector` (the prompt's own instruction is to leave it empty rather than invent metrics, so this is expected, not a failure).
  The request retains this source rule, criterion or rationale, with its original modal force: Such a finding's shipped severity comes from its own CVSS/VulContextSeverity band if one exists, else its detection-time label — never a blanket INFO floor.
}
```

## prompt_cuts — source lines 83–83

Source context: callable `_render_pipeline_diagnostics`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/_sections_pipeline.py:83-83
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: inventory files
}
```

## prompt_cuts — source lines 84–84

Source context: callable `_render_pipeline_diagnostics`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/models/scan/_sections_pipeline.py:84-84
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: entry points
}
```

