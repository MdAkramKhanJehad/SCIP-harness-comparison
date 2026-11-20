# vvaharness/orchestrator/checkpoints.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## save_ckpt — source lines 252–253

Source context: callable `save_ckpt`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/checkpoints.py:252-253
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')
}
```

## load_ckpt — source lines 279–281

Source context: callable `load_ckpt`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `run_id[:12]; conversion=none; format_spec=none`
- `store.db_path(); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/orchestrator/checkpoints.py:279-281
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [ckpt] no checkpoints for [dynamic source value: run_id[:12]; conversion=none; format_spec=none]… in [dynamic source value: store.db_path(); conversion=none; format_spec=none] — if the model expected resume, check $VVAHARNESS_STATE_DIR
}
```

