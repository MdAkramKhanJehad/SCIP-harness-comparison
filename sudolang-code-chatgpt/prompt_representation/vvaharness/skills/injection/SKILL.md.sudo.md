# vvaharness/skills/injection/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Injection source/sink/defense decisions

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/injection/SKILL.md:24-76
Constraints {
  Requested confirmation needs an interpreting sink, an externally reachable source (including second-order writes), and no effective intervening parameterization, allow-list, context-correct escaping or safe wrapper.
  if (the sink receives a hardcoded literal or no path reaches it) { The model is asked to drop it. }
  A validation recommendation without a sink is not a requested finding here.
  First request: run sh .vvaharness/skills/injection/probe.sh [root], examine class candidates and defense census.
  if (a class section is (none)) { This prompt asks the model to stop that class; retain that rule despite other skills' different stopping instructions. }
  The model is asked to distinguish correct-context defenses from wrong-variable/wrong-context escaping and query interpolation from parameter binding; trace parse-check-use mismatches and second-order writes; inspect XXE security flags, metadata-permitting SSRF allow-lists and archive member validation.
  if (catastrophic regex input is length-capped) { The requested ReDoS severity is LOW. }
  The section called What refutes includes both refutations and positive-finding examples; that mixed source organization is preserved.
  Every distinct sink and weakness class receives a separate anchored finding, not a generic missing-validation aggregate.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/injection/SKILL.md:1-4
Constraints {
  The source declares name = "injection". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Hunt injection classes (SQL, NoSQL, OS command, LDAP, XPath, XXE, CRLF, SSTI, open redirect, path traversal, SSRF, server-emitted XSS, ReDoS) under a source/sink/no-defence hard gate. Ships probe.sh: a per-class sink sweep plus a census of the defences present.". Tool lists here describe the request profile; source loaders determine actual grants.
  The request retains this source rule, criterion or rationale, with its original modal force: Hunt injection classes (SQL, NoSQL, OS command, LDAP, XPath, XXE, CRLF, SSTI, open redirect, path traversal, SSRF, server-emitted XSS, ReDoS) under a source/sink/no-defence hard gate. Ships probe.sh: a per-class sink sweep plus a census of the defences present.
}
```

# Injection Lens

```sudo
// Source: vvaharness/skills/injection/SKILL.md:24-26
Constraints {
  The requested search/review target is where attacker-controlled input is merged into a downstream interpreter without separating code from data, across every class named in this skill's description.
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:28-28
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — a finding requires ALL THREE:
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/injection/SKILL.md:29-31
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a SINK that interprets its input — SQL executor, shell exec, XML parser, HTTP client, response writer, file open, regex compile, template render, redirect, header setter,
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/injection/SKILL.md:32-34
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a SOURCE reachable from an external actor — request field, message body, file upload, CLI arg, env var, or a DB row previously written by an untrusted party (second-order),
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/injection/SKILL.md:35-38
// Source list marker (c); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: NO intervening defence: no parameterisation, no allow-list, no context-correct escaper, no library-provided safe wrapper.
  The requested conditional/temporal rule is: If (a)'s argument is a hardcoded literal, or nothing reaches the sink on any path, DROP it. "We should validate this" with no sink is not a finding here.
}
```

## Probe first

```sudo
// Source: vvaharness/skills/injection/SKILL.md:42-45
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `sh .vvaharness/skills/injection/probe.sh [root]` — a labelled `file:line` section of sink hits per class, then a DEFENCE CENSUS counting the files that carry each defence.
  The request retains this source rule, criterion or rationale, with its original modal force: Every line is a CANDIDATE; `(none)` is a real answer, so stop working that class.
  The request retains this source rule, criterion or rationale, with its original modal force: The sections are a starting set, not the lens.
}
```

## What refutes a candidate

```sudo
// Source: vvaharness/skills/injection/SKILL.md:49-49
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Literal argument. Constant, column name from a fixed tuple, internal enum.
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:50-53
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Defence in the wrong context. HTML-escaping a value bound for JS or an attribute; `shlex.quote` on the binary but not its args; an allow-list on a different variable than the one reaching the sink; `%s` inside the query string (interpolation) read as `%s` with a params tuple (binding).
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:54-56
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Parse-check-use mismatch. The reverse, and a finding: code parses the URL or path to check host/prefix, then builds the request or `open()` from the raw string.
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:57-59
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Second-order flow. Taint entered on an earlier write — DB row, cache, config — later concatenated into a query.
  The request retains this source rule, criterion or rationale, with its original modal force: The call site looks clean; only tracing the write reveals it.
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:60-62
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: XXE flags. A parser factory is vulnerable only if `disallow-doctype-decl` / `FEATURE_SECURE_PROCESSING` / `resolve_entities=False` is absent.
  The request retains this source rule, criterion or rationale, with its original modal force: The probe finds the factory; the model check the flag.
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:63-64
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SSRF allow-list that still permits metadata — `169.254.169.254`, `metadata.google.internal`, `metadata.azure.com`.
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:65-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ReDoS input size. Catastrophic patterns matter against unbounded input; on a length-capped field, LOW.
}
```

```sudo
// Source: vvaharness/skills/injection/SKILL.md:67-68
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Zip-Slip. `extractall` counts only with unvalidated member names on an attacker-supplied archive.
}
```

## ENUMERATION RULE (CRITICAL — do not skip)

```sudo
// Source: vvaharness/skills/injection/SKILL.md:72-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every distinct sink is its own finding, with its own class (SQLi / CMDi / SSRF / …), file, line, source, and sink.
  The request retains this source rule, criterion or rationale, with its original modal force: Three raw SQL builders across two files are three findings; one SSRF plus one path traversal in one handler are two.
  The requested model behavior excludes collapse them into an omnibus "input validation missing" — each sink has its own exploitability and its own fix location.
}
```

