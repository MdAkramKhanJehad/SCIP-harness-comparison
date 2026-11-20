# vvaharness/skills/missing-controls/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Absence-search procedure and per-site judgment

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:24-146
Constraints {
  Requested order: enumerate actual sites before judging whether a control is absent.
  For each listed control, the model is asked to grep the whole repository and decide every applicable site individually.
  Before reporting, its evidence must establish a reachable concrete site, the protected asset/actor making the control appropriate, and absence on this particular path after checking middleware, inheritance, decorator factories, proxies and framework defaults.
  if (the control exists anywhere on the path) { The requested outcome is a refutation naming that location. }
  if (the control exists at every enumerated site) { The requested rationale gives the checked-site count. }
  The control-specific site lists and present/absent examples below remain constraints for anti-automation, session revocation/lifetimes, per-write cookie/transport settings, deployment/debug, data-at-rest/transit, CSRF/origin and authorization.
  Storage of a LoginAttempt/failed_count without refusal enforcement is not accepted as the control; config defaults do not automatically protect explicit cookie overrides.
  Cleartext storage and response disclosure are distinct requested findings, even for one field; translate framework examples to the actual framework.
  Requested exclusions include genuinely public low-resource endpoints, unshipped/unseeded obviously synthetic fixtures and non-attacker-varied fixed targets; a seeded real-looking sensitive value is treated differently.
  The model is asked to state its searches and emit one finding per absent site, anchored where the fix edits, with enumeration/control-presence counts.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:1-4
Constraints {
  The source declares name = "missing-controls". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find weaknesses that consist of an ABSENT control — no rate limit, no session invalidation, no cookie flags, debug left on, secrets or PII stored in cleartext — by enumerating every site the control belongs and checking each.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is weaknesses that consist of an ABSENT control — no rate limit, no session invalidation, no cookie flags, debug left on, secrets or PII stored in cleartext — by enumerating every site the control belongs and checking each.
}
```

# Absent-Control Lens

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:24-28
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every other lens hunts for a dangerous construct — a sink, a concatenation, a weak algorithm.
  The request retains this source rule, criterion or rationale, with its original modal force: This lens hunts for a hole.
  The request retains this source rule, criterion or rationale, with its original modal force: the model cannot grep for a decorator that was never written, and a deterministic scanner will never hand the model a line number for it, so nothing upstream will point the model at these.
  The requested conditional/temporal rule is: If the model only investigate what the model were shown, the model will never report one.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:30-31
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The method is inverted.
  The request retains this source rule, criterion or rationale, with its original modal force: Instead of "is this construct dangerous?", ask "what should be here, and is it?" That requires enumerating sites first and judging second.
}
```

## Hard gate — a finding requires all three

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:35-36
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The site is real and reachable. A concrete handler, route, cookie write, session config, or storage write that an external actor can reach.
  The request retains this source rule, criterion or rationale, with its original modal force: Not a hypothetical.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:37-39
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The control genuinely belongs there. Name the asset it would protect and the actor it would stop. "Every endpoint should have rate limiting" is not analysis; "`/api/login` accepts unlimited password guesses against a user-supplied username" is.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:40-42
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: It is absent on THIS path, and the model checked — not merely "not visible in the file the model were given".
  The request retains this source rule, criterion or rationale, with its original modal force: Middleware, a base class, a decorator factory, a reverse-proxy config, or a framework default can supply it somewhere the model have not looked yet.
  The request retains this source rule, criterion or rationale, with its original modal force: Look, then conclude.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:44-45
Constraints {
  The requested conditional/temporal rule is: If the control exists anywhere on the path, refute and say where it is.
  The request retains this source rule, criterion or rationale, with its original modal force: A refutation here is a real result: it is how the FP rate stays low.
}
```

## Enumerate before you conclude

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:49-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: These are systemic gaps, and a systemic gap is only actionable if the site list is complete.
  The request retains this source rule, criterion or rationale, with its original modal force: Reporting one unprotected route while four others are equally exposed means whoever applies the model's fix still ships the vulnerability.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:53-56
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: So for each control below: Grep the whole repository for every site of the kind it protects, then decide site by site. Report one finding per absent site, each with its own file and line.
  The requested conditional/temporal rule is: If it is present everywhere the model enumerated, refute and say how many sites the model checked.
}
```

## The controls, and where each belongs

### Anti-automation on credential and cost endpoints — CWE-307, CWE-799

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:61-69
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sites: every handler that verifies a credential or consumes a scarce resource — login, registration, password reset, OTP/MFA verification, token refresh, email send, payment, file upload, expensive search. Present looks like: `flask-limiter` `@limiter.limit(...)`; `django-ratelimit` `@ratelimit`; DRF throttle classes; `slowapi` on FastAPI; `express-rate-limit`; Spring `Bucket4j`; a failed-attempt counter with lockout persisted per account or per source; a CAPTCHA gate; an upstream WAF/gateway rule only if the model can see it in this repo. Note: a `LoginAttempt` model or a `failed_count` column existing is not the control — find the code that *reads* it and *refuses*.
  The request retains this source rule, criterion or rationale, with its original modal force: Storage without enforcement is a decoy.
}
```

### Session termination — CWE-613, CWE-384

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:72-79
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sites: logout, password change, email change, role change, account deactivation. Present looks like: server-side session destroy (`session.clear()`, `request.session.flush()`, store delete); for stateless JWT a denylist/`jti` revocation check, or a `token_version`/`password_changed_at` claim compared on every request. The classic hole: a logout endpoint that returns `200 {"message": "logged out"}` and nothing else, while the issued JWT stays valid until expiry — the token is still a working credential.
  The request retains this source rule, criterion or rationale, with its original modal force: Also: a password change that does not invalidate other live sessions, and a session with no absolute or idle lifetime at all.
}
```

### Cookie and transport flags — CWE-614, CWE-1004, CWE-1275, CWE-319

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:82-88
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sites: every `set_cookie` / `Set-Cookie` write and every framework session config key.
  The request retains this source rule, criterion or rationale, with its original modal force: There are usually more of these than the model expect; grep for all of them. Present looks like: `httponly=True`, `secure=True`, `samesite="Lax"` or `"Strict"` on each write; `SESSION_COOKIE_HTTPONLY` / `_SECURE` / `_SAMESITE`; Django `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`. Report per site. A config-level default does not cover an explicit `set_cookie` that overrides it, and fixing the config does not fix the explicit writes.
}
```

### Deployment and debug posture — CWE-16, CWE-215, CWE-489

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:91-99
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sites: app entrypoints, settings modules, Dockerfiles, compose files, CI/CD manifests. The holes: `app.run(debug=True)` — the Werkzeug console is remote code execution, and `host="0.0.0.0"` makes it reachable; Django `DEBUG = True`; `ALLOWED_HOSTS = ["*"]`; stack traces or exception detail returned to the client; verbose error handlers; directory listing; admin or metrics endpoints exposed without auth; default credentials left in a seed or fixture. On CWE choice: report the class the model's evidence supports.
  The requested conditional/temporal rule is: If debug mode yields arbitrary code execution, that is what it yields — say so, and name the misconfiguration as the cause in your description so both readings are recoverable.
}
```

### Data at rest and in transit — CWE-312, CWE-311, CWE-319, CWE-359

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:102-110
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sites: model/schema definitions, migrations, seed and fixture data, serializers, cache and queue writes, log statements, backup and export paths. The holes: identifiers and PII (national ID, DOB, full address, card data, health data) stored as plain columns or plain JSON blobs; a seed/fixture that commits real-looking sensitive values; secrets written to a cache or queue unencrypted; TLS verification disabled on an outbound call (`verify=False`, `rejectUnauthorized: false`). Distinguish: stored-in-cleartext (CWE-312) is a different finding from returned-in-a-response (CWE-359/200) even for the same field.
  The requested conditional/temporal rule is: If both hold, both are findings — they have different fixes and different blast radii.
}
```

### Request forgery and origin trust — CWE-352, CWE-942, CWE-1021

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:113-115
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Covered in depth by the `csrf` lens; treat it as part of this sweep when the claim is that a *protection is missing* rather than that a sink is dangerous. Enumerate every state-changing handler, not just the one the model were pointed at.
}
```

### Authorization

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:118-121
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Covered by the `access-control` lens, which already frames it as an absence.
  The request retains this source rule, criterion or rationale, with its original modal force: Note its "where to look" examples are Spring/JAX-RS; translate to the framework in front of the model — Flask `@login_required` / `before_request`, Django permission classes and mixins, FastAPI `Depends(...)`, Express middleware.
}
```

## False-positive discipline

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:125-125
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Refute, do not report, when:
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:127-129
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The control is present anywhere on the path, including in middleware, a base class, a dependency, a decorator applied at the blueprint/router level, or a framework default the model can point to.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:130-132
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The endpoint is genuinely public and unauthenticated by design (health check, static asset, public docs, webhook with signature verification present) and holds no scarce resource.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:133-134
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The "sensitive" data is obviously synthetic test fixture data and the file is not shipped or seeded into a running environment.
  The requested conditional/temporal rule is: If it *is* seeded, it is a finding.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:135-136
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The target is a fixed constant rather than attacker-varied — bounded blast radius, do not inflate it.
}
```

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:138-139
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Say which of these the model checked.
  The request retains this source rule, criterion or rationale, with its original modal force: An absence claim with no stated search is indistinguishable from a guess, and the reader cannot tell them apart.
}
```

## What good output looks like

```sudo
// Source: vvaharness/skills/missing-controls/SKILL.md:143-146
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One finding per absent site, each naming the file and the line the fix must edit — the handler signature or decorator line for a missing guard, the `set_cookie` call for a missing flag, the settings line for a posture problem.
  The request retains this source rule, criterion or rationale, with its original modal force: The rationale states what the model enumerated, how many sites the model found, which had the control and which did not.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../../../../assets/original/vvaharness/skills/missing-controls/SKILL.md).
