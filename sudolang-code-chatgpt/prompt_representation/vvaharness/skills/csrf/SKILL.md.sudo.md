# vvaharness/skills/csrf/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## CSRF conjunction and explicit exemption exception

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:24-102
Constraints {
  The requested attacker scenario is a logged-in victim visiting a malicious origin that submits a state-changing request.
  Ordinarily, a requested finding needs all three: a state change, cookie/basic session authentication, and no effective handler token, SameSite Strict/Lax, Origin/Referer or custom-header defense on that path.
  if (any ordinary gate is absent) { The requested ordinary disposition is to drop the finding. }
  if (a state-changing handler explicitly disables framework CSRF protection through @csrf_exempt, @csrf.exempt, csrf.disable() or skip_before_action :verify_authenticity_token) {
    The exception instruction treats authentication condition (b) as satisfied by the exemption itself, including currently unauthenticated handlers.
    The model is asked to report each such handler; do not reconcile this exception with the stricter session-auth examples later in the source.
  }
  The model is asked to inspect the source-listed Django, Flask, Express, Spring and Rails middleware/matcher/form/method gaps, JSON-only assumptions, logout, and especially password/email changes.
  Every independently vulnerable state-changing handler gets its own function/file/line finding, never an omnibus report.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:1-4
Constraints {
  The source declares name = "csrf". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find state-changing requests that a third-party origin can forge: missing or unverified CSRF tokens, unsafe SameSite, and CORS that trusts a reflected Origin with credentials.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is state-changing requests that a third-party origin can forge: missing or unverified CSRF tokens, unsafe SameSite, and CORS that trusts a reflected Origin with credentials.
}
```

# Csrf Lens

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:24-27
Constraints {
  The requested model role and scope are a Cross-Site Request Forgery (CSRF) expert.
  The requested search/review target is state-changing endpoints that can be triggered by a forged cross-origin request — the attacker model is a logged-in user visiting a malicious page that silently fires a request to this application.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:29-29
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — a finding requires ALL THREE:
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:30-31
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: an endpoint that performs a state change (write, delete, transfer, update password, change email, modify settings — NOT a read-only GET),
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:32-33
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the endpoint authenticates via cookie or HTTP basic auth (stateful session), AND
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:34-37
// Source list marker (c); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: there is no effective CSRF defence: no synchronizer token verified on this specific handler, no SameSite=Strict/Lax cookie attribute, no Origin/Referer check on this path, and no custom request header requirement.
  The requested conditional/temporal rule is: If any one of (a)–(c) is absent, DROP the finding.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:39-47
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: EXPLICIT @csrf_exempt EXCEPTION — bypass condition (b): If a handler is decorated with @csrf_exempt (Django), @csrf.exempt (Flask), csrf.disable(), or skip_before_action :verify_authenticity_token (Rails), the CSRF protection has been deliberately removed at the framework level.
  The request retains this source rule, criterion or rationale, with its original modal force: Report EVERY such state-changing handler as a CSRF finding even when it currently appears to be unauthenticated — the decorator is a standing removal of a security control that applies the moment authentication is added or the endpoint is reused in a context that has a session.
  The request retains this source rule, criterion or rationale, with its original modal force: Condition (b) is SATISFIED by the explicit exemption decorator alone.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:49-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where to look first (non-exhaustive — reason beyond this list):
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:51-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DJANGO / Python
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:52-53
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Views decorated with @csrf_exempt — any state-changing action on an exempt view is a confirmed CSRF if it uses session auth.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:54-55
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Django: CsrfViewMiddleware absent from MIDDLEWARE in settings.py → global bypass; all state-changing views are vulnerable.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:56-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: State-changing GET handlers (any view that mutates DB/session on a GET request) bypass CSRF token checking entirely — Django's middleware only protects unsafe HTTP methods.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:59-59
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Forms without {% csrf_token %} that POST to state-changing views.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:60-60
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: @require_POST not present: the same handler accepts GET, defeating token.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:61-62
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: AJAX endpoints that rely only on the session cookie and do not verify X-CSRFToken header or a body token.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:64-64
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FLASK / Python
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:65-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Flask-WTF / flask_wtf.csrf not initialized (CSRFProtect not applied globally or per-blueprint), AND views accept POST with session auth.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:67-67
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Blueprint or route decorated with @csrf.exempt for state-changing actions.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:68-70
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested conditional/temporal rule is: Before-request CSRF check that is conditionally bypassed (request.method in ('GET','HEAD','OPTIONS','TRACE') check missing; non-safe methods not checked).
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:72-72
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: EXPRESS / Node.js
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:73-74
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: csurf middleware not applied to the router, or applied only to a subset of routes, leaving state-changing routes uncovered.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:75-75
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SameSite not set to Strict or Lax on session cookie; no custom header check.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SPRING MVC / Java
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:78-78
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CsrfConfigurer disabled: .csrf().disable() in security config.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:79-80
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Spring Security's CSRF protection is enabled by default — look for explicit disablement or for request matchers that exclude state-changing paths.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:81-81
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SameSite not set on session cookie AND no CSRF token checked.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:83-83
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: RAILS / Ruby
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:84-85
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: protect_from_forgery :with => :null_session or :with => :exception bypassed, or skip_before_action :verify_authenticity_token on state-changing actions.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:87-87
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CROSS-CUTTING
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:88-90
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Any state-changing JSON API that relies only on Content-Type: application/json without also checking a CSRF token or custom header — Flash-based or form- encoded cross-origin requests can set arbitrary Content-Type in some browsers.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:91-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Logout endpoints without CSRF protection allow forced logout (session fixation compound attack).
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:93-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Password/email change endpoints are the highest-severity CSRF target — always check these specifically.
}
```

```sudo
// Source: vvaharness/skills/csrf/SKILL.md:96-102
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ENUMERATION RULE (CRITICAL — do not skip) When the model find multiple handlers that are each independently CSRF-vulnerable (e.g., multiple @csrf_exempt views, multiple routes lacking a CSRF token), report EACH ONE as a SEPARATE finding with its own function name, file, and line number.
  The requested model behavior excludes collapse all instances into a single omnibus finding.
  The request retains this source rule, criterion or rationale, with its original modal force: Every distinct state-changing endpoint without CSRF protection is an independent vulnerability with its own exploitability and fix location.
}
```

