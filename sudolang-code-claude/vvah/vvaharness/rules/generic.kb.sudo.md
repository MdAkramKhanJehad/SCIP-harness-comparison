# vvaharness/rules/generic.kb.yaml

The shipped generic CWE knowledge base: 27 entries (24 distinct CWE ids; CWE-117, CWE-22 and CWE-306 each appear twice, and `CweKB._merge` accumulates the second entry's list items into the first entry's slot while keeping the first title). Its items reach the Stage 4 model as the result of the `CweGuidance` tool. Every entry is copied below with its values exactly; items with a `lang:` prefix (for example `python: cursor.execute`) are filtered by language in `_filter_lang`.

Source: `vvaharness/rules/generic.kb.yaml` (lines 1-444)
Executor: code (data loaded by `vvaharness/rules/__init__.py` CweKB.load)
Called from: `vvaharness/rules/__init__.py` _kb_files

// src: vvaharness/rules/generic.kb.yaml:16-20
// File header: "Generated generic CWE/OWASP starter pack." builder=1.1.0 llm=False via=sdk model=claude-haiku-4-5. Every entry has origin "generic" and aliases [].

Options entries {
// src: vvaharness/rules/generic.kb.yaml:21-42
CWE-89 { title: "SQL Injection", origin: "generic", aliases: []
  sources: "user input, request params, form fields, query strings"; "path params, headers, JSON bodies, cookies"
  sinks: "string-built SQL passed to execute/query/update"; "dynamic SQL fragments used for table, column, or ORDER BY names"; "python: cursor.execute"; "java: Statement.executeQuery"
  sanitizers: "Parameterized queries / prepared statements"; "java: PreparedStatement"; "server-side allow-lists for dynamic identifiers"
  non_sanitizers: "manual escaping"; "regex blacklists for SQL keywords"
  fp_checks: "taint reaches a bound parameter value, not the SQL string"; "query is fully static and only values are interpolated via binds"
}

// src: vvaharness/rules/generic.kb.yaml:43-59
CWE-78 { title: "OWASP A03 Injection: command execution", origin: "generic", aliases: []
  sources: "user input, argv/env, request params, config values"
  sinks: "shell invocation, Runtime.exec, Process.Start, child_process.exec"; "any string passed to a shell or eval-style command runner"
  sanitizers: "argv-array execution with shell disabled"; "strict allow-list of commands and arguments"
  non_sanitizers: "quoting only"; "blocking punctuation characters"
  fp_checks: "command is constant and arguments are not attacker-controlled"
}

// src: vvaharness/rules/generic.kb.yaml:60-77
CWE-79 { title: "OWASP A03 Injection: HTML / template output", origin: "generic", aliases: []
  sources: "HTTP input, comments, markdown, profiles, stored text"
  sinks: "innerHTML, document.write, render_template_string, res.send(html)"; "template raw blocks, safe markers, triple-stache, Markup()"
  sanitizers: "context-aware HTML encoding"; "template auto-escape that stays enabled end-to-end"
  non_sanitizers: "strip_tags"; "URL encoding"; "JSON serialization"
  fp_checks: "sink is textContent / innerText / JSON response"
}

// src: vvaharness/rules/generic.kb.yaml:78-94
CWE-22 { title: "OWASP A01 Broken Access Control: path traversal", origin: "generic", aliases: []
  sources: "user-supplied filename, path, archive member, upload name"
  sinks: "open/read/write/delete/sendFile/serveFile on attacker-influenced paths"
  sanitizers: "canonicalize then verify inside a fixed base directory"; "server-side id to path mapping with no raw path joins"
  non_sanitizers: "basename alone"; "single ../ replacement"; "prefix check before resolve"
  fp_checks: "path is constant or fully server-derived"
}

// src: vvaharness/rules/generic.kb.yaml:95-110
CWE-918 { title: "OWASP A10 SSRF: server-side URL fetch", origin: "generic", aliases: []
  sources: "user URL, webhook target, callback URL, redirect URL"
  sinks: "requests/fetch/HttpClient/curl/file_get_contents on remote URLs"
  sanitizers: "host allow-list after DNS resolution"; "private-range and loopback blocking on every hop"
  non_sanitizers: "scheme allow-list only"; "string prefix checks on hosts"
  fp_checks: "URL is fixed or drawn from a trusted allow-list"
}

// src: vvaharness/rules/generic.kb.yaml:111-127
CWE-502 { title: "OWASP A08 Software / data integrity: unsafe deserialization", origin: "generic", aliases: []
  sources: "untrusted blob, file, message, cookie, session payload"
  sinks: "pickle.loads, ObjectInputStream.readObject, BinaryFormatter.Deserialize"; "YAML/native object loaders that execute constructors or gadgets"
  sanitizers: "safe_load / data-only parsing"; "class allow-list filters before object creation"
  non_sanitizers: "signature check after deserialization"; "class-name blacklists"
  fp_checks: "input is immutable trusted data and cannot be attacker-writable"
}

// src: vvaharness/rules/generic.kb.yaml:128-142
CWE-611 { title: "OWASP A08 software integrity: XML external entity expansion", origin: "generic", aliases: []
  sources: "XML input from request, file, message, or partner system"
  sinks: "XML parsers with DTD/entity resolution enabled"
  sanitizers: "disable DTDs and external entities before parsing"
  non_sanitizers: "post-parse exception handling"; "schema validation alone"
  fp_checks: "defused XML parser or equivalent hardened factory is used"
}

// src: vvaharness/rules/generic.kb.yaml:143-157
CWE-601 { title: "OWASP A01 Broken Access Control: open redirect", origin: "generic", aliases: []
  sources: "next, returnUrl, redirect, callback, destination parameters"
  sinks: "response redirects and client-side navigation sinks"
  sanitizers: "relative-path allow-list or exact host allow-list"
  non_sanitizers: "startswith('/')"; "substring host checks"
  fp_checks: "redirect target is fully server constant"
}

// src: vvaharness/rules/generic.kb.yaml:158-173
CWE-117 { title: "OWASP A09 logging / monitoring: log injection", origin: "generic", aliases: []
  sources: "user-controlled strings, headers, stack traces, request bodies"
  sinks: "raw log lines, audit events, CSV export of logs"
  sanitizers: "structured logging with escaping or field separation"
  non_sanitizers: "trimming"; "length checks"; "removing a few delimiters"
  fp_checks: "output is structured and encoded before log emission"
}

// src: vvaharness/rules/generic.kb.yaml:174-188
CWE-352 { title: "OWASP A01 / session integrity: CSRF on state-changing actions", origin: "generic", aliases: []
  sources: "browser-originated requests, forms, fetches, cookies"
  sinks: "state-changing endpoints without anti-CSRF verification"
  sanitizers: "anti-CSRF token or same-site gate checked on every state change"
  non_sanitizers: "custom header names only"; "Referer check alone"
  fp_checks: "action is read-only or token is required and validated"
}

// src: vvaharness/rules/generic.kb.yaml:189-203
CWE-306 { title: "OWASP A07 authentication: missing auth check", origin: "generic", aliases: []
  sources: "public route, anonymous request, unauthenticated job trigger"
  sinks: "privileged endpoint or command without authentication gate"
  sanitizers: "authentication required before the sensitive action"
  non_sanitizers: "UI-only restriction"; "client-side gating"
  fp_checks: "route is internal-only and unreachable from any external entry point"
}

// src: vvaharness/rules/generic.kb.yaml:204-218
CWE-862 { title: "OWASP A01 broken access control: missing authorization", origin: "generic", aliases: []
  sources: "tenant id, object id, row id, account id, URL path id"
  sinks: "object access without ownership / role / policy checks"
  sanitizers: "server-side authorization check tied to the resource"
  non_sanitizers: "hiding the id from the UI"; "guessable ids are not enough"
  fp_checks: "resource is global or intentionally public"
}

// src: vvaharness/rules/generic.kb.yaml:219-233
CWE-639 { title: "OWASP A01 broken access control: IDOR / object reference", origin: "generic", aliases: []
  sources: "object identifiers from request path, query, or body"
  sinks: "fetch/update/delete of another user's object"
  sanitizers: "ownership lookup against authenticated principal"
  non_sanitizers: "UUIDs alone"; "random ids alone"
  fp_checks: "identifier is scoped by server-side tenant context before use"
}

// src: vvaharness/rules/generic.kb.yaml:234-248
CWE-20 { title: "OWASP A04 insecure design: missing input validation", origin: "generic", aliases: []
  sources: "any untrusted field crossing a trust boundary"
  sinks: "security-sensitive business logic consuming unchecked input"
  sanitizers: "strict type, range, format, and allow-list validation"
  non_sanitizers: "null checks"; "length checks only"
  fp_checks: "all attacker-controlled inputs are normalized and validated before use"
}

// src: vvaharness/rules/generic.kb.yaml:249-263
CWE-327 { title: "OWASP A02 cryptographic failures: weak or broken crypto", origin: "generic", aliases: []
  sources: "secrets, credentials, tokens, PII, payment data"
  sinks: "MD5/SHA1 for security, hard-coded IVs, obsolete protocols"
  sanitizers: "modern authenticated encryption and strong hash choices"
  non_sanitizers: "HMAC with weak hash"; "password hashing with unsalted fast hash"
  fp_checks: "crypto is legacy-only and not used for security decisions"
}

// src: vvaharness/rules/generic.kb.yaml:264-278
CWE-295 { title: "OWASP A02 transport: TLS verification disabled", origin: "generic", aliases: []
  sources: "client configuration, deployment config, README instructions"
  sinks: "verify=false, rejectUnauthorized=false, InsecureSkipVerify"
  sanitizers: "TLS verification enabled with trusted CA / pinning policy"
  non_sanitizers: "accepting any certificate"; "environmental trust without verification"
  fp_checks: "dev-only harness or isolated test fixture that never ships"
}

// src: vvaharness/rules/generic.kb.yaml:279-293
CWE-798 { title: "OWASP A02 credentials: hardcoded secret or token", origin: "generic", aliases: []
  sources: "source code literals, checked-in configs, fixtures, docs"
  sinks: "API keys, passwords, JWTs, private keys, cloud credentials"
  sanitizers: "secret manager lookup or runtime injection from secure storage"
  non_sanitizers: "base64 encoding"; "renaming the variable"
  fp_checks: "string is clearly a non-secret placeholder or a public example token"
}

// src: vvaharness/rules/generic.kb.yaml:294-308
CWE-434 { title: "OWASP A05 misconfiguration: unrestricted file upload", origin: "generic", aliases: []
  sources: "user file uploads, multipart forms, drag-and-drop files"
  sinks: "storage or execution of uploaded content without validation"
  sanitizers: "type / extension / size allow-lists and safe storage outside web root"
  non_sanitizers: "extension blacklists"; "MIME type alone"
  fp_checks: "upload is converted to inert data or stored under a non-executable path"
}

// src: vvaharness/rules/generic.kb.yaml:309-322
CWE-1333 { title: "OWASP A04 availability: regex denial of service", origin: "generic", aliases: []
  sources: "attacker-controlled text evaluated by complex regex"
  sinks: "catastrophic-backtracking patterns in search / validation"
  sanitizers: "linear-time regex or bounded matching with input limits"
  non_sanitizers: "short-circuit checks that still leave the bad regex path"
  fp_checks: "pattern is precompiled and not evaluated on attacker-controlled length"
}

// src: vvaharness/rules/generic.kb.yaml:323-337
CWE-400 { title: "OWASP A04 availability: unbounded resource consumption", origin: "generic", aliases: []
  sources: "user-controlled pagination, loops, recursion, batch size, uploads"
  sinks: "CPU / memory / disk amplification without hard caps"
  sanitizers: "server-side quotas, paging limits, timeouts, and bounded queues"
  non_sanitizers: "client hints"; "best-effort throttling"
  fp_checks: "resource use is bounded by server-enforced limits"
}

// src: vvaharness/rules/generic.kb.yaml:338-353
CWE-94 { title: "OWASP A03 injection: code / expression evaluation", origin: "generic", aliases: []
  sources: "template fragments, user expressions, rule text, scripts"
  sinks: "eval, exec, ScriptEngine, new Function, template eval"
  sanitizers: "literal allow-lists and sandboxed expression engines"
  non_sanitizers: "character stripping"; "blacklists"; "string concatenation"
  fp_checks: "expression is fully authored by trusted code and never data-derived"
}

// src: vvaharness/rules/generic.kb.yaml:354-368
CWE-117 { title: "OWASP A09 observability: sensitive data in logs", origin: "generic", aliases: []
  sources: "PII, PAN, tokens, secrets, debug traces"
  sinks: "logs, metrics tags, tracing spans, error telemetry"
  sanitizers: "redaction before write, field-level masking, structured fields"
  non_sanitizers: "manual truncation"; "suffix masking only"
  fp_checks: "sensitive fields are redacted before emission"
}

// src: vvaharness/rules/generic.kb.yaml:369-383
CWE-200 { title: "OWASP A01 / A02 information exposure", origin: "generic", aliases: []
  sources: "stack traces, debug flags, config dumps, internal ids"
  sinks: "public responses, error pages, diagnostic endpoints"
  sanitizers: "least-information responses and internal-only diagnostics"
  non_sanitizers: "hiding the UI button"; "client-side only protections"
  fp_checks: "response is explicitly internal and inaccessible to external actors"
}

// src: vvaharness/rules/generic.kb.yaml:384-398
CWE-22 { title: "OWASP A01 broken access control: archive / path member traversal", origin: "generic", aliases: []
  sources: "zip member names, tar entries, upload names, import paths"
  sinks: "file extraction or access using raw member names"
  sanitizers: "member name normalization and base-dir checks"
  non_sanitizers: "single-pass replacement of '../'"; "basename alone"
  fp_checks: "archive members are validated against a fixed extraction root"
}

// src: vvaharness/rules/generic.kb.yaml:399-414
CWE-269 { title: "OWASP A01 privilege issue: over-privileged action", origin: "generic", aliases: []
  sources: "privileged command, admin endpoint, service token, host OS action"
  sinks: "write/delete/execute beyond the caller's privilege boundary"
  sanitizers: "least-privilege execution / role enforcement / policy checks"
  non_sanitizers: "UI hints"; "obscurity"; "self-declared role strings"
  fp_checks: "operation is already confined to the caller's minimal privilege"
}

// src: vvaharness/rules/generic.kb.yaml:415-429
CWE-306 { title: "OWASP A07 auth: unauthenticated control plane action", origin: "generic", aliases: []
  sources: "scheduler jobs, webhooks, admin APIs, CLI switches"
  sinks: "sensitive control plane operations without auth"
  sanitizers: "auth gate plus server-side permission check"
  non_sanitizers: "hidden routes"; "unguarded localhost assumptions"
  fp_checks: "endpoint is unreachable from any untrusted entry point"
}

// src: vvaharness/rules/generic.kb.yaml:430-444
CWE-326 { title: "OWASP A02 cryptography: insufficient encryption strength", origin: "generic", aliases: []
  sources: "data at rest, data in transit, long-lived tokens"
  sinks: "weak algorithms, truncated keys, low-entropy secrets"
  sanitizers: "strong modern algorithm and key-size choices"
  non_sanitizers: "homegrown crypto"; "security through obscurity"
  fp_checks: "algorithm is non-security legacy only"
}

}
