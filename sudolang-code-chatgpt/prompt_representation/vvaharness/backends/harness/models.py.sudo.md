# vvaharness/backends/harness/models.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _AUTH_REMEDIATION — source lines 403–410

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/backends/harness/models.py:403-410
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Credential options (pick the one that matches the model's profile): CLI backend (default): run `claude /login` or export CLAUDE_CODE_OAUTH_TOKEN=<fresh-token> SDK / API backend: export ANTHROPIC_SDK_API_KEY=<key> or ANTHROPIC_API_KEY=<key> Gateway / JWT backend: regenerate the model's JWT and set ANTHROPIC_BASE_URL=https://<gateway>/
}
```

```sudo
// Source: vvaharness/backends/harness/models.py:403-410
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Then run: vvaharness doctor To continue from the last checkpoint: add --resume to the model's scan command.
}
```

