# vvaharness/skills/client-side/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Browser evidence, gate and enumeration

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:24-110
Constraints {
  The model is asked to treat browser-delivered code as attacker-editable and shipped values as public.
  Requested first operation: run sh .vvaharness/skills/client-side/probe.sh [root]. The approximate one-second/read-only description is a source claim, not a converter timing result.
  if (a probe section is missing) { The model is asked to recognize probe failure. }
  if (a hit-count tail indicates truncation) { The model is asked to grep that class independently. }
  Before reporting, require in the requested evidence: a concrete construct/span, a named asset consequence, and exactly one most-specific CweGuidance-checked CWE.
  if (the claim is frontend-only enforcement) {
    The model is asked to inspect the server handler and identify the trusted client value or absent check.
    if (the backend is unreachable) { The requested claim is unverified/downgraded, not asserted as established. }
  }
  Requested analysis covers client-supplied principal/role/amount, unauthenticated JWT decoding, build-inlined environment secrets, weak origin matching and wildcard postMessage tokens, Host-derived bearer destinations and credentialed reflected CORS, dev servers/source maps, broad COPY and missing lockfiles, non-persisted security toggles, password-change reauthentication, protocol-relative redirects and markup-only numeric limits.
  Requested refutations include path sanitization/default escaping, closed values or safe function/attribute forms, intentionally public credentials, server-side revalidation/verified principals and patched dependency versions; state which was checked.
  Report separately by storage write, raw-HTML occurrence, client-identity request, vulnerable package pin and weakness class. Do not count every read of one stored token as a new write.
  The model is asked to use client code as evidence that a server parameter is attacker-controlled, and anchor that server-side defect at the server line.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:1-4
Constraints {
  The source declares name = "client-side". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Weaknesses in browser-delivered code — JS/TS, JSX/TSX, Vue, Svelte, Angular, HTML, templates, bundler and Docker config. DOM XSS and code-exec sinks, secrets in bundles or config.js, build-inlined REACT_APP_/NEXT_PUBLIC_/VITE_ env, source maps and dev servers shipped in images, tokens in localStorage or non-httpOnly cookies, client-side JWT decoding, postMessage without an origin check, permissive CORS/credentials, unvalidated redirects, prototype pollution, missing SRI, vulnerable package.json pins — and above all security decisions made only in the frontend (disabled buttons, hidden fields, is_admin render gates, a client-computed user_id) that the server never repeats. Ships probe.sh, which greps every sink class in one pass. Activate on frontend/, public/, static/, src/components/, bundler config, or .js/.jsx/.ts/.tsx/.vue/.svelte/.html files.". Tool lists here describe the request profile; source loaders determine actual grants.
  The request retains this source rule, criterion or rationale, with its original modal force: Weaknesses in browser-delivered code — JS/TS, JSX/TSX, Vue, Svelte, Angular, HTML, templates, bundler and Docker config. DOM XSS and code-exec sinks, secrets in bundles or config.js, build-inlined REACT_APP_/NEXT_PUBLIC_/VITE_ env, source maps and dev servers shipped in images, tokens in localStorage or non-httpOnly cookies, client-side JWT decoding, postMessage without an origin check, permissive CORS/credentials, unvalidated redirects, prototype pollution, missing SRI, vulnerable package.json pins — and above all security decisions made only in the frontend (disabled buttons, hidden fields, is_admin render gates, a client-computed user_id) that the server never repeats. Ships probe.sh, which greps every sink class in one pass. Activate on frontend/, public/, static/, src/components/, bundler config, or .js/.jsx/.ts/.tsx/.vue/.svelte/.html files.
}
```

# Client-Side Lens

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:24-29
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: This code is already the attacker's — on their machine, in DevTools, editable before it runs. Nothing shipped to the client is secret: keys, connection strings, source maps, an inlined `.env`. A client-side control is not a security control: `disabled`, `hidden`, an `is_admin` render gate, a form schema, a client-computed ID.
  The request retains this source rule, criterion or rationale, with its original modal force: So a check that exists only in the frontend IS the finding — the defect is the server-side absence it conceals.
  The request retains this source rule, criterion or rationale, with its original modal force: Nothing upstream hands the model frontend code; go look.
}
```

## Run the probe first

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:33-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `sh .vvaharness/skills/client-side/probe.sh [root]`
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:35-39
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Read-only, ~1s.
  The request retains this source rule, criterion or rationale, with its original modal force: It greps every client-side sink class at once, including the *server* lines that read client-sent parameters, and skips test, mock, story and example paths, which are not shipped.
  The request retains this source rule, criterion or rationale, with its original modal force: Sections are CWE-labelled and print `path:line` or `(none)`.
  The request retains this source rule, criterion or rationale, with its original modal force: A *missing* section means the probe broke; `...
  The request retains this source rule, criterion or rationale, with its original modal force: N hits total` means the cap truncated, so grep that class yourself.
  The request retains this source rule, criterion or rationale, with its original modal force: It locates, it decides nothing below.
}
```

## HARD GATE — a finding requires ALL of

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:43-44
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A construct with a line span — sink call, storage write, literal secret, listener, build key, pin.
  The request retains this source rule, criterion or rationale, with its original modal force: Not "the SPA should validate input".
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:45-46
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A named consequence to an asset — which credential leaks, which account is acted on, what the attacker executes.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:47-48
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: For a "the frontend enforces X" claim, the server gap in hand — the handler trusts the client value or omits the check.
  The request retains this source rule, criterion or rationale, with its original modal force: Unreachable backend: unverified, downgrade, never assert.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:49-51
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Exactly one most-specific CWE, `CweGuidance`-checked: `innerHTML` XSS is CWE-79 not CWE-20, client-enforced authorization CWE-602 not CWE-284, a server trusting a client `user_id` CWE-639 not CWE-863.
}
```

## Judgement the probe cannot make

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:55-57
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Client-supplied identity — highest value here. Client sends `user_id`/`role`/`amount`; handler reads `data.get('user_id')` instead of the authenticated principal. CWE-639 at the server line, client line as evidence.
  The request retains this source rule, criterion or rationale, with its original modal force: Probe prints both halves; read the handler.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:58-59
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Client-side JWT decode is unauthenticated parsing — a claim used as identity or permission trusts a payload the client mints.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:60-60
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Build-inlined env is published; ask only whether the value is secret.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:61-62
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Origin checks by `indexOf`/`startsWith`/`endsWith` pass `https://trusted.evil.com`; only strict equality against an allow-list refutes. `postMessage(data,'*')` with a token is CWE-201.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:63-65
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A base URL from `window.location.hostname` sends every `Bearer` where the Host header points; with cross-origin `credentials:'include'`, check the server for middleware reflecting the request `Origin` with `Allow-Credentials: true` — a full same-origin-policy bypass.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:66-68
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: In the shipped-artifacts section: a dev-server `CMD` ships hot reload and source maps (CWE-489); `COPY . .` with no `.dockerignore` entry sweeps in `.env`/`.git`; no lockfile beside `npm install` means `^` resolved at build time, so what ships is unpinned.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:69-70
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Toggles that persist nowhere (2FA checkbox on `useState`, no request) have no server side at all — the model see it only by reading the component.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:71-71
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A password form with only a new-password field misses re-authentication (CWE-620).
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:72-73
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `startsWith('/')` does not refute a redirect (`//evil.com` is protocol-relative), and a bound only in markup (`step="0.01"`) is no bound — check the handler rejects negatives.
}
```

## FP CHECKS — what REFUTES

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:77-78
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A sanitizer on the path (probe's sanitizer section); React/Vue/Svelte interpolation escapes by default and is not a finding.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:79-80
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Sink value is a literal or closed enum; `setTimeout` given a function reference; `setAttribute` on a non-URL, non-`on*` attribute.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:81-82
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The "secret" is public by design — the probe flags the known-public prefixes (`pk_live_`, Firebase, Sentry DSN, Maps).
  The requested evidence/output includes which, and refute.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:83-85
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The server repeats the check: identity from the verified principal, amount re-validated, role re-checked.
  The request retains this source rule, criterion or rationale, with its original modal force: A client-sent id used only as a *lookup target* while the handler derives the actor (`sender_id=current_user.id`) is not CWE-639.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:86-86
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The pin is patched — read the version, and name it in the finding.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:88-88
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Say which the model checked; an unqualified frontend finding reads as a lint rule.
}
```

## ENUMERATION RULE (CRITICAL — do not skip)

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:92-93
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One finding per distinct site, with its own file and `line_start..line_end` on the construct a fix edits.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:95-96
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Anchor token storage at the write, not at every `getItem` — but `token` in storage and `refresh_token` in a JS cookie are two findings.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:97-97
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every raw-HTML sink occurrence is its own finding: different source, fix, line.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:98-99
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every client-supplied-identity request is its own: a password change and a transaction list each sending `user_id` are two defects, two handlers.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:100-100
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every vulnerable pin is its own finding.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:101-103
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The other axis: one component usually holds several classes at once — token storage, client-derived identity, missing re-auth, a cleartext base URL.
  The requested conditional/temporal rule is: Before leaving a file, ask what else is wrong with it; emit each class with its own CWE.
}
```

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:104-104
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes collapse into "frontend security issues" — a blanket finding is credited once.
}
```

## The shape we miss

```sudo
// Source: vvaharness/skills/client-side/SKILL.md:108-110
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A client file is proof that a server-side parameter is attacker-controlled. `frontend/src/` went unread in every measured run while a whole authorization-bypass chain sat in it.
  The model is asked to obtain and examine the client to learn which server parameters to distrust, then report the server line.
}
```

