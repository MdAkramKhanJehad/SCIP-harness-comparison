# vvaharness/util/events.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## S2_RETRY_RECOVERED — source lines 42–42

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/util/events.py:42-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: retry recovered a threat model
}
```

## S2_PARSE_REPAIR_RECOVERED — source lines 48–48

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the repair retry recovered a valid threat model
}
```

## TOOL_CALL_REFUSED — source lines 89–89

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:89-89
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refused a tool call outside this session's permitted set
}
```

## RESPONSE_MODEL_FORCED_FINAL_INVALID — source lines 98–99

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:98-99
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the forced-final structured-output call did not validate; returning raw text
}
```

## MODEL_REFUSAL_RESEND — source lines 114–114

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:114-114
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model refused; re-sending the identical request once
}
```

## CONFIG_POLICY_REFUSED — source lines 117–117

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:117-117
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: configuration refused by policy
}
```

## CONFIG_PATH_NOT_LOCAL — source lines 118–118

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/util/events.py:118-118
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: path must be local; refusing network fetch
}
```

## DOTENV_UNTRUSTED — source lines 120–121

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/util/events.py:120-121
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ignoring an untrusted .env; it must be a user-owned, non-group/world-writable file
}
```

## STEP1_OVERLAY_REFUSED — source lines 124–124

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:124-124
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the --step1-config overlay was refused
}
```

## STATE_DIR_REFUSED — source lines 131–131

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:131-131
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: refusing to use state directory
}
```

## REPLAY_TOO_LARGE — source lines 142–142

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:142-142
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: replay bundle exceeds the cap; not persisted
}
```

## REPLAY_STORED_TOO_LARGE — source lines 143–143

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:143-143
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the stored replay bundle exceeds the cap; ignoring it
}
```

## REPLAY_PRUNE_FAILED — source lines 144–144

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:144-144
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: could not prune replay bundles
}
```

## TRACING_UPLOADS_PROMPTS — source lines 165–165

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:165-165
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tracing is on; it uploads every prompt, repo source included
}
```

## EV_COLLECTION_NOT_LOCAL — source lines 180–180

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/util/events.py:180-180
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: EV_API_COLLECTION must be a local path; refusing a network path
}
```

## FIXER_DISPATCH_REFUSED — source lines 188–188

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:188-188
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: fixer dispatch refused
}
```

## REPLAY_NO_LIVE_SESSION — source lines 199–199

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/util/events.py:199-199
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: no live session to resume; re-asking from the transcript
}
```

