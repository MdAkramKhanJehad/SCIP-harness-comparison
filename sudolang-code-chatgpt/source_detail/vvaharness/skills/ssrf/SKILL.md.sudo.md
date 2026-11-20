# vvaharness/skills/ssrf/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Opaque sink contracts and nonterminal empty probes

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:24-92
Constraints {
  Requested confirmation needs a network sink OR fetch-contract helper even with unseen/stubbed body; a request/second-order-controlled URL; and no scheme-and-host allow-list enforced on the connected address.
  Literal/trusted deployment-only URLs are requested to be dropped, unless a handler can write that config.
  First request: run sh .vvaharness/skills/ssrf/probe.sh with optional subtree. Empty sink sections do not terminate this lens; trace helper callers using GraphImporters/GraphNeighbors.
  An opaque fetch helper is not refuted merely by a stub, absent HTTP import or missing library. Prefer the route call-site anchor; if only the helper contract is evidenced, anchor its def and name the caller.
  Blind channels and discarded bodies still count under the requested rules; search for readers and state channel/internal target, redirect checks, rebinding race and bypass evidence.
  Requested genuine refutations require resolved/pinned destination enforcement with redirect checks/disablement, repo-configured destination-restricting egress, hardened client or fixed authority. Syntax/scheme-only/unresolved-string checks are not accepted as refutations.
  Emit one site per route call; count a helper separately only if independently reachable. An exported helper without a local caller may be separately reported or omitted: that choice is explicitly left to the model.
  Requested CWE choice: 918 normally; 611 for XML-entity fetching; 441 for arbitrary relay; never substitute 601. Ask CweGuidance for the selected id.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:1-4
Constraints {
  The source declares name = "ssrf". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Hunt Server-Side Request Forgery (CWE-918) — any outbound fetch whose URL, scheme, host or port derives from a request. Activate on avatar-by-URL, webhook/callback registration, URL preview/unfurl, render-to-PDF/screenshot/thumbnailer, import-from-URL, feed ingest, OAuth redirect_uri/jwks_uri discovery, \"test connection\" probes, proxy and media passthrough, and on helpers named download/fetch/get_image/get_base64_image_blob/load_url whose bodies you cannot see. Ships probe.sh, which greps fetch sinks across seven ecosystems, url-parameter contracts, their call sites and allow-list posture in one pass. Keywords SSRF, requests.get, urlopen, httpx, fetch, axios, OkHttp, curl_exec, 169.254.169.254, cloud metadata, gopher://, allow_redirects, DNS rebinding, blind SSRF, URLField.". Tool lists here describe the request profile; source loaders determine actual grants.
  The request retains this source rule, criterion or rationale, with its original modal force: Hunt Server-Side Request Forgery (CWE-918) — any outbound fetch whose URL, scheme, host or port derives from a request. Activate on avatar-by-URL, webhook/callback registration, URL preview/unfurl, render-to-PDF/screenshot/thumbnailer, import-from-URL, feed ingest, OAuth redirect_uri/jwks_uri discovery, "test connection" probes, proxy and media passthrough, and on helpers named download/fetch/get_image/get_base64_image_blob/load_url whose bodies the model cannot see. Ships probe.sh, which greps fetch sinks across seven ecosystems, url-parameter contracts, their call sites and allow-list posture in one pass. Keywords SSRF, requests.get, urlopen, httpx, fetch, axios, OkHttp, curl_exec, 169.254.169.254, cloud metadata, gopher://, allow_redirects, DNS rebinding, blind SSRF, URLField.
}
```

# SSRF Lens

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:24-24
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The application is the attacker's HTTP client: inside the perimeter, holding an instance role.
}
```

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:26-26
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — all three, or no finding:
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:27-29
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SINK — a call doing network I/O to a URL, host or port, OR a function whose contract is to fetch a URL (parameter `url`/`uri`/`src`/`endpoint`/`callback`, or name in download/fetch/get_*/import_*/render_*) even when its body is stubbed, vendored or unseen;
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:30-32
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SOURCE — the URL derives from a request-controlled channel (query, form, JSON body, header, path segment, webhook registration, uploaded document) or a DB column an untrusted party wrote earlier (second-order);
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:33-34
// Source list marker (c); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: NO allow-list of scheme AND host enforced on the address actually connected to.
  The request retains this source rule, criterion or rationale, with its original modal force: Literal URL, or one only settable through deployment config: DROP.
}
```

## Run the probe first

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:38-44
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `sh .vvaharness/skills/ssrf/probe.sh` (optional arg: subtree) prints labelled path:line hits for fetch sinks in all seven ecosystems, indirect mechanisms (XXE, headless render, image coders, `dblink`), url-parameter contracts AND their call sites, request sources, allow-list and redirect posture, and — only when a sink exists — reference tables of internal targets, admin ports, schemes, redirect defaults, rebinding races and deny-list bypasses to cite.
  The request retains this source rule, criterion or rationale, with its original modal force: An empty ecosystem section means the repo does not use it; empty sink sections do NOT end the hunt.
  The request retains this source rule, criterion or rationale, with its original modal force: Trace helpers to callers with GraphImporters and GraphNeighbors.
}
```

## THE SHAPE WE MISS MOST — an opaque fetch helper

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:48-58
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A route hands a request-supplied URL to a local helper whose body holds no greppable HTTP call: a stub, a thin wrapper, a vendored module, a C extension.
  The request retains this source rule, criterion or rationale, with its original modal force: The `url` PARAMETER is the sink.
  The request retains this source rule, criterion or rationale, with its original modal force: Measured instance: a route assigned `get_base64_image_blob(form.url.data)` out of `ImageForm(request.form)` where the helper module was nine lines of stubs returning empty literals, with no HTTP client imported anywhere and none in `requirements.txt`.
  The request retains this source rule, criterion or rationale, with its original modal force: Nothing text-matches: the fetch IS the contract of the parameter.
  The requested model behavior excludes refute on "the body makes no request", "the helper is a stub" or "no HTTP library is installed".
  The request retains this source rule, criterion or rationale, with its original modal force: Same repo's fake defence: WTForms `URLField('url', [validators.DataRequired()])` is a widget plus a non-emptiness check — no scheme, host or resolution — and the template posted free-text `<input type="text" name="url">`. ANCHOR the span on the route's call site; when only the helper's contract is in evidence, anchor its `def` line and name the calling route.
}
```

## What still counts

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:62-67
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Blind — status, latency, byte count or error text only — is SSRF: port scanning, reachability mapping, `gopher://` POST-shaped effects.
  The request retains this source rule, criterion or rationale, with its original modal force: Say which channel the attacker observes.
  The request retains this source rule, criterion or rationale, with its original modal force: A fetched body written to a column no template reads back is still a finding; never refute because the response is discarded, but grep for a reader — if it is re-served, severity rises, so say so.
  The requested evidence/output includes the internal target you reach.
  The request retains this source rule, criterion or rationale, with its original modal force: A host check that resolves once, or a deny-list of private literals, does not hold: cite the per-hop redirect rule, the rebinding race, one bypass string.
}
```

## FP CHECKS — what genuinely refutes this

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:71-79
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Refute, saying which applies, on: an allow-list of BOTH scheme and host enforced against the RESOLVED address (resolve, reject non-public or non-listed IPs, connect to that pinned address, redirects re-checked per hop or disabled); egress through a destination-restricting proxy or gateway configured IN THIS REPO, or an SSRF-hardened client; a hardcoded URL, or a fixed base where input fills only a path or query segment and cannot change host, port or scheme (path traversal or parameter injection, another class); a URL from trusted deployment config and no request field — unless a handler can write that config value. NOT refutations: scheme-only checks, a host check on the unresolved string, and syntax validators (`validators.URL()`, `URLField`, `new URL(s)`, `^https?://`) — they constrain the string, not the destination.
}
```

## ENUMERATION RULE (CRITICAL — do not skip)

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:83-88
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One finding per distinct sink site.
  The request retains this source rule, criterion or rationale, with its original modal force: Two routes calling the same fetch helper are TWO findings, each anchored at its own span — each has its own source, reachability and guard.
  The request retains this source rule, criterion or rationale, with its original modal force: The helper is a third only if independently reachable; an exported fetch helper with no caller in the repo is a library entry point, reported separately or not at all, never merged into a route's finding.
  The requested model behavior excludes collapse sites into "URL input is not validated", and report SSRF separately from any other class at the same lines (open redirect, path traversal, XXE) — different fixes.
}
```

```sudo
// Source: vvaharness/skills/ssrf/SKILL.md:90-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CWE, exactly one: 918 by default; 611 when an XML parser's external entity is the fetch mechanism; 441 when the endpoint exists to relay arbitrary requests. 601 is open redirect, never a substitute.
  The request retains this source rule, criterion or rationale, with its original modal force: Call CweGuidance for the model's id.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../../../../assets/original/vvaharness/skills/ssrf/SKILL.md).
