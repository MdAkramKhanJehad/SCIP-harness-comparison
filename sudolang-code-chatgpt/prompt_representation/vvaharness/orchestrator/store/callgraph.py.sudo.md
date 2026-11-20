# vvaharness/orchestrator/store/callgraph.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## save_callgraph — source lines 93–93

Source context: callable `save_callgraph`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/store/callgraph.py:93-93
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')
}
```

