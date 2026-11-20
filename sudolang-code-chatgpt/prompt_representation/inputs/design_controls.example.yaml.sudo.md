# inputs/design_controls.example.yaml — supplied guidance and request data

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## controls.0.notes

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/design_controls.example.yaml:20-20
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: All handler entry points sit behind JWT validation in the gateway.
}
```

## controls.1.notes

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/design_controls.example.yaml:26-26
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Worker processes run under seccomp-bpf; no execve, no socket.
}
```

