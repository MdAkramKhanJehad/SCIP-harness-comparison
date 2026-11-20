# vvaharness/skills/sensitive-data/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Exposure gate without injection prerequisite

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:24-81
Constraints {
  Requested findings are point-of-occurrence exposures; no injection path is required.
  The requested gate combines genuinely sensitive content with a channel an attacker can reach/read.
  Non-sensitive print/log calls are excluded; encryption advice without concrete exposure is requested as LOW.
  First request: run sh .vvaharness/skills/sensitive-data/probe.sh [root]; treat every hit as a candidate.
  if (no strong KDF exists AND passwords are stored without one) { The model is asked to recognize a missing-KDF finding. }
  if (Cache-Control/no-store is absent on authenticated pages) { The model is asked to consider PII caching. }
  if (HSTS is absent on an HTTPS application) { The model is asked to consider downgrade exposure. }
  Requested judgment reads view and template, inspects actual serialized model fields, judges sensitive constants by both name and value, distinguishes secret-source reads/placeholders and harmless token_count/flagged_at names, and establishes debug/admin reachability and excess disclosure.
  Severity follows the source's qualitative blast-radius examples: one DOB in a log MEDIUM, all PANs in a world-readable file HIGH.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:1-4
Constraints {
  The source declares name = "sensitive-data". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find sensitive data reaching somewhere it should not: PII, credentials or internals in HTTP responses, logs, error pages, templates, caches, headers, debug routes, or stored unprotected. Point-of-occurrence — no injection path required. Ships probe.sh, which greps every leak channel (debug flags, exception-to-response, log calls on sensitive names, whole-object serialization, weak password storage, cache and HSTS headers, introspection routes, settings constants).". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is sensitive data reaching somewhere it should not: PII, credentials or internals in HTTP responses, logs, error pages, templates, caches, headers, debug routes, or stored unprotected. Point-of-occurrence — no injection path required. Ships probe.sh, which greps every leak channel (debug flags, exception-to-response, log calls on sensitive names, whole-object serialization, weak password storage, cache and HSTS headers, introspection routes, settings constants).
}
```

# Sensitive Data Lens

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:24-27
Constraints {
  The requested model role and scope are a Sensitive-Data-Exposure expert.
  The request retains this source rule, criterion or rationale, with its original modal force: Hunt places where the application reveals more than necessary — to the user, to logs, or at rest.
  The request retains this source rule, criterion or rationale, with its original modal force: These are point-of-occurrence findings: the model do NOT need an injection path.
  The request retains this source rule, criterion or rationale, with its original modal force: The question is only "does this output, store, or log contain data an attacker can harvest?"
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:29-29
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — a finding requires BOTH:
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:30-33
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: genuinely sensitive data: credentials, session tokens, PII (SSN, DOB, card PAN, bank account, health record), internal system details (stack traces, SQL text, server paths, version strings), or confidential business data (pricing, unreleased features), AND
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:34-38
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a channel an attacker reaches or can read: response body, response header, error page, log file, temp file, world-readable DB column, URL or query string, or an unauthenticated debug endpoint.
  The request retains this source rule, criterion or rationale, with its original modal force: Generic `print()` / `console.log()` on non-sensitive variables is NOT a finding. "We should encrypt this" with no concrete exposure path → LOW.
}
```

## Probe first

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:42-45
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `sh .vvaharness/skills/sensitive-data/probe.sh [root]` — labelled `file:line` sections across error/debug exposure, logging, response and serialization leakage, storage, headers and caching, debug/admin routes, and settings constants.
  The request retains this source rule, criterion or rationale, with its original modal force: Every line is a CANDIDATE; apply the gate to each.
}
```

## Polarity: three sections are findings when EMPTY

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:49-50
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `strong KDF present` → `(none)` and passwords are stored with no key-derivation function at all.
  The request retains this source rule, criterion or rationale, with its original modal force: That is the finding.
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:51-52
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `Cache-Control / no-store` → `(none)` on an app serving authenticated pages: proxies and browsers cache PII.
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:53-53
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `Strict-Transport-Security` → `(none)` on an HTTPS app: downgrade is open.
}
```

## Judgement the grep cannot make

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:57-60
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Look at the template file, not only the view. A view that *catches* an exception and passes the raw message into the render context still leaks it.
  The request retains this source rule, criterion or rationale, with its original modal force: The leak is in the `.html`, where `{{ error }}` / `{{ sql_error }}` / `{{ exception }}` prints it.
  The model is asked to obtain and examine both sides before deciding.
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:61-64
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Serialization needs a field audit. `to_dict()` / `__dict__` / `model_to_dict()` is only a finding when the model actually carries fields the caller must not see — `is_admin`, `internal_id`, `token`, `hashed_password`.
  The request retains this source rule, criterion or rationale, with its original modal force: Open the model and check.
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:65-70
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Settings constants: judge the name, then the value. The probe lists every ALL_CAPS constant holding a non-trivial string literal.
  The request retains this source rule, criterion or rationale, with its original modal force: Flag the ones whose name suggests sensitivity even when they do not follow the framework's `SECRET_KEY` convention — `flag`, `secret`, `key`, `token`, `data`, `credential`, `password`.
  The request retains this source rule, criterion or rationale, with its original modal force: A literal like `SENSITIVE_DATA = 'FLAG...'` is a finding; `APP_NAME = 'billing-service'` is not.
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:71-72
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Placeholders and reads are not literals. `os.environ[...]`, `${VAR}`, and vault lookups in a credential position are indirection.
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:73-75
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sensitive name is not sensitive content. A log line mentioning `token_count` or a column named `flagged_at` matches the pattern and is nothing.
  The model is asked to obtain and examine the value that actually flows.
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:76-79
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Reachability of a debug route. `/metrics` or `/health` behind authentication or bound to localhost is not exposure.
  The request retains this source rule, criterion or rationale, with its original modal force: Django admin reachable at `/admin/` is not a finding by itself — flag it only when it discloses more than expected (user emails, session tokens).
}
```

```sudo
// Source: vvaharness/skills/sensitive-data/SKILL.md:80-81
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Severity follows blast radius. One user's DOB in a log is MEDIUM; every user's PAN in a world-readable file is HIGH.
}
```

