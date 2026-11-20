# vvaharness/models/scan/_sections_chain.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _ranked_threat_rows — source lines 237–237

Source context: callable `_ranked_threat_rows`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/models/scan/_sections_chain.py:237-237
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: none — never reviewed |
}
```

## clauses — source lines 150–152

Source context: callable `_empty_chain_section_copy`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `report.chains_dropped; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_chain.py:150-152
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: report.chains_dropped; conversion=none; format_spec=none] proposed chain(s) were removed because their steps did not resolve to two or more distinct findings in this report.
}
```

## clauses — source lines 153–154

Source context: callable `_empty_chain_section_copy`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `report.chains_deduped; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_chain.py:153-154
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: report.chains_deduped; conversion=none; format_spec=none] proposed chain(s) were identical to another and were collapsed.
}
```

## clauses — source lines 155–156

Source context: callable `_empty_chain_section_copy`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `report.chains_invalid; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_chain.py:155-156
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: report.chains_invalid; conversion=none; format_spec=none] proposed chain(s) were written in a shape this report could not read and were removed.
}
```

## clauses — source lines 157–159

Source context: callable `_empty_chain_section_copy`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(report.unpromoted_links); conversion=none; format_spec=none`
- `_unpromoted_pairs_text(report); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/models/scan/_sections_chain.py:157-159
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: len(report.unpromoted_links); conversion=none; format_spec=none] link(s) between findings were marked as chain potential ([dynamic source value: _unpromoted_pairs_text(report); conversion=none; format_spec=none]) but no surviving chain carries them.
}
```

