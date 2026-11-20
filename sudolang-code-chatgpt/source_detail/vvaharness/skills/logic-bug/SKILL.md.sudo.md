# vvaharness/skills/logic-bug/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Behavioral trust-boundary review

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:24-54
Constraints {
  The requested method reasons about state, ordering, concurrency and edge-case inputs rather than a grep signature.
  Requested findings cite the external-input file:line and the security-decision file:line crossing a trust boundary.
  if (both sides are internal in the same trust domain, an idempotent retry or intentional design) { The model is asked to drop the candidate. }
  Without a trust-boundary citation, no finding is requested.
  Seed questions cover check-to-mutation races, empty/null/duplicate/out-of-order authentication messages, concurrent half-authentication, numeric overflow/zero/narrowing/negative identity collisions, connection parser desynchronization, tenant/user/role cache keys and revocation, and unguarded -1/null/NaN sentinel results.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:1-4
Constraints {
  The source declares name = "logic-bug". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find business-logic defects: missing validation on amounts and quantities, race conditions and TOCTOU, workflow steps that can be skipped or replayed.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is business-logic defects: missing validation on amounts and quantities, race conditions and TOCTOU, workflow steps that can be skipped or replayed.
}
```

# Logic Bug Lens

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:24-26
Constraints {
  The requested model role and scope are reviewing for behavioural / state-machine defects — the class of bug that has no single grep signature and only surfaces when you reason about ordering, concurrency, and edge-case inputs.
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:28-32
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — for every finding the model MUST cite the exact trust boundary that is crossed: the file:line where untrusted/external input enters, and the file:line where the security decision is made on that input.
  The requested conditional/temporal rule is: If both sides are internal (service-to-service, same trust domain, idempotent retry, intentional design), DROP the finding.
  The request retains this source rule, criterion or rationale, with its original modal force: No trust-boundary citation → no finding.
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:34-34
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Reason about behaviour, don't pattern-match.
  The request retains this source rule, criterion or rationale, with its original modal force: Seed questions:
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:35-37
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Check-then-act windows: between the permission/ownership/balance check and the mutation, can a second request, another thread, or a filesystem actor change what was checked?
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:38-40
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Auth/session state: what does the login or step-up flow do on empty, null, duplicated, or out-of-order messages?
  The request retains this source rule, criterion or rationale, with its original modal force: Can two concurrent requests against one session leave it half-authenticated?
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:41-43
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Numeric identity and counters: what happens at overflow, at zero, at negative after a narrowing cast?
  The request retains this source rule, criterion or rationale, with its original modal force: Does an ID truncated to 32-bit collide with a privileged record?
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:44-46
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Connection/protocol state: can a malformed or truncated message leave the parser mid-state so the NEXT request on the same connection is misinterpreted?
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:47-49
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Caches and memoised decisions: is the cache key missing the tenant/user/role dimension, so one principal's result is served to another?
  The request retains this source rule, criterion or rationale, with its original modal force: Does a cached "authorised" decision outlive a revocation?
}
```

```sudo
// Source: vvaharness/skills/logic-bug/SKILL.md:50-54
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sentinel return values: is the result of indexOf/find/search (which returns -1 / null when the token is absent) used as an offset or length WITHOUT the `== -1` guard, so "not found" silently becomes position 0 or a wrong substring slice?
  The request retains this source rule, criterion or rationale, with its original modal force: Same for parseInt→NaN or a lookup returning null treated as success.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../../../../assets/original/vvaharness/skills/logic-bug/SKILL.md).
