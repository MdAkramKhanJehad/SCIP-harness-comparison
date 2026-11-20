# vvaharness/orchestrator/entry.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## build_parser — source lines 166–166

Source context: callable `build_parser`; enclosing call `ap.add_argument`; keyword `help`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/entry.py:166-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: do not delete cloned repos after scanning (batch mode)
}
```

## build_parser — source lines 177–181

Source context: callable `build_parser`; enclosing call `ap.add_argument`; keyword `help`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/entry.py:177-181
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stop after the named step (for debugging); 'clone' stops right after acquiring repos in batch mode and implies --keep-clones; 'ev' verifies the collection named by EV_API_COLLECTION (parse + reachability probe) and stops before S1)
}
```

## build_parser — source lines 183–184

Source context: callable `build_parser`; enclosing call `ap.add_argument`; keyword `help`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/entry.py:183-184
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: write state/s6_progress/<run_id>/s6_progress.json after each S6 verification
}
```

## build_parser — source lines 218–222

Source context: callable `build_parser`; enclosing call `auto_grp.add_argument`; keyword `help`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/entry.py:218-222
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: hard-disable AI auto-exclude for this run, irrespective of step1.auto_exclude in the active profile.
  The request retains this source rule, criterion or rationale, with its original modal force: Wins over --auto-step1 and any config default. (To also disable it persistently, set step1.auto_exclude: false in the model's profile.)
}
```

