# vvaharness/skills/sibling-instances/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Confirmation-conditioned repository sweep

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:24-89
Constraints {
  if (a weakness class is confirmed at a site) {
    Requested sequence: name its concrete searchable pattern; grep the entire repository with two or three phrasings; open and independently judge every hit; emit one anchored finding per confirmed distinct site; reject duplicates of the same construct.
    The rationale is requested to state the sweep term, candidate count and confirmed count.
  } else {
    The model is asked not to sweep a refuted or unsupported speculative class.
  }
  The recurrence examples are ordered from most to least reliable as source guidance, not probability thresholds.
  Before leaving a read location, the model is asked to consider other weakness classes and report each with its own CWE; same location does not imply same class.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:1-4
Constraints {
  The source declares name = "sibling-instances". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "After confirming a weakness, sweep the repository for every other site of the same pattern and report each one — a class confirmed at one location is almost never present at only one location.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested conditional/temporal rule is: After confirming a weakness, sweep the repository for every other site of the same pattern and report each one — a class confirmed at one location is almost never present at only one location.
}
```

# Sibling-Instance Sweep

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:24-27
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A weakness class is a property of how the codebase was written, not of one line.
  The request retains this source rule, criterion or rationale, with its original modal force: The developer who interpolated a value into SQL once did it wherever they wrote SQL; the one who reached for MD5 reached for it in every hashing path.
  The request retains this source rule, criterion or rationale, with its original modal force: So once the model have confirmed a class at one site, the question is no longer "is this a bug" — it is "where else?"
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:29-30
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Reporting one instance of a repeated defect is a partial answer that reads like a complete one.
  The request retains this source rule, criterion or rationale, with its original modal force: The person who applies the model's fix patches the site the model named and ships the rest.
}
```

## When this applies

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:34-35
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Only after a confirmation.
  The requested model behavior excludes sweep for a class you just refuted, and do not sweep speculatively for classes you have no evidence of — that is how precision dies.
}
```

## The sweep

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:39-40
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested evidence/output includes the pattern you just confirmed, concretely enough to search for: the sink call, the algorithm name, the decorator that was missing, the flag that was unset.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:41-44
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Grep the whole repository for it. Not the file the model were given, not the directory — the repository.
  The model is asked to adopt two or three phrasings, because the same defect rarely looks identical twice: `hashlib.md5` and `md5(`; `f"SELECT` and `"SELECT " +` and `.format(` near `execute`; `set_cookie(` with and without keyword arguments.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:45-47
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Open every hit and judge it on its own evidence. A hit is a candidate, not a finding.
  The request retains this source rule, criterion or rationale, with its original modal force: The same call in a test fixture, behind a different guard, or on a value that is a fixed literal is a different situation and may be fine.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:48-51
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report one finding per confirmed site, each with its own file and its own line span pointing at the construct a fix would edit.
  The requested model behavior excludes fold five sites into one finding with five paths in the description — each site needs its own anchor to be actionable, and a single blanket finding can only ever be credited, tracked or fixed once.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:52-53
// Source list marker 5.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes pad. Near-identical findings at the *same* construct are duplicates, not breadth.
  The request retains this source rule, criterion or rationale, with its original modal force: One per distinct site.
}
```

## Patterns that recur, from most to least reliably

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:57-59
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Query construction. One interpolated query means the whole data-access layer is suspect.
  The model is asked to establish every `execute` / `query` / `raw` call, including ones in different modules from the one you started in.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:60-63
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hashing and randomness. A weak hash or a predictable RNG appears wherever that operation is performed — registration *and* login *and* password reset *and* a token minter.
  The request retains this source rule, criterion or rationale, with its original modal force: The classic miss is exactly this: MD5 in the model's `set_password` and inline in the registration handler.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:64-65
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Regex compiled from a pattern with nested quantifiers. ReDoS lives in every such pattern in the file, not the first one.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:66-67
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Outbound requests. One un-allow-listed URL fetch usually means several, often in the same helper module, each reachable from a different route.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:68-69
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Deserialization. `yaml.load` / `pickle.loads` / native object streams tend to appear in an import path *and* an export path *and* a cache layer.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:70-71
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Cookie writes and header setters. Frequently one per handler, each missing the same flags, with a config default that covers none of them.
}
```

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:72-73
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Decorator omissions. If one handler in a module lacks the guard its siblings have, check every handler in that module — and every other module with the same shape.
}
```

## The other axis: the same location, a different class

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:77-81
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The converse of this sweep, and just as commonly missed.
  The request retains this source rule, criterion or rationale, with its original modal force: One handler routinely holds several unrelated weaknesses — a missing authorization check *and* an injection sink *and* an unflagged cookie *and* a logic flaw on the amount.
  The requested conditional/temporal rule is: Before the model leave a location the model have already read, ask what *else* is wrong with it, and report each class separately with its own CWE.
  The request retains this source rule, criterion or rationale, with its original modal force: Two classes at one line are two findings, not one broad finding.
}
```

## Rationale requirement

```sudo
// Source: vvaharness/skills/sibling-instances/SKILL.md:85-89
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: State what the model swept for, how many candidate sites the search returned, and how many the model confirmed. "Grepped `hashlib.md5` across the repo: 2 hits, both confirmed, at the two password-writing sites I cite below" is the shape of a complete answer — the sweep term, the hit count, and the confirmed count.
  The request retains this source rule, criterion or rationale, with its original modal force: A confirmation with no sweep leaves the reader unable to tell whether the class was isolated or the model simply stopped looking.
}
```

