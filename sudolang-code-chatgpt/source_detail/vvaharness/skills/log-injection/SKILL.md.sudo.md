# vvaharness/skills/log-injection/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Three classes despite two-class introduction

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:24-81
Constraints {
  The introduction says two classes, then defines A, B and C; retain all three without correcting the source.
  Class A requested gate: a log call plus external input whose newline/CR/encoded-newline characters are not stripped. Sanitized/fixed messages are excluded.
  Class B requested gate: an identifiable security-relevant failure event with zero log output; inspect authentication/admin/security-exception/reset/MFA/sensitive-file events.
  Class C is independent of injection: requested evidence is a log argument named password/passwd/secret/token/api_key/private_key/auth_token case-insensitively, or a sensitive literal label followed by the value.
  Requested searches also cover user-influenced log paths and structured events that can override levels, timestamps or fields.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:1-4
Constraints {
  The source declares name = "log-injection". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find unsanitised input reaching log sinks: forged log records, injected control characters, and sensitive values written to logs.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is unsanitised input reaching log sinks: forged log records, injected control characters, and sensitive values written to logs.
}
```

# Log Injection Lens

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:24-25
Constraints {
  The requested model role and scope are a Log-Injection / Insufficient-Logging expert.
  The requested search/review target is two distinct classes:
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:27-29
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CLASS A — Log Injection (CWE-117): attacker-controlled data written to logs without sanitisation allows forged log entries, log poisoning, or downstream log-parser exploitation.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:31-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CLASS B — Missing / Insufficient Logging (CWE-778, OWASP A09): security- relevant events not logged at all — silent authentication failures, privilege changes, admin actions — which blind incident responders.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:35-35
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CLASS A HARD GATE — requires BOTH:
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:36-37
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a log call (logging.*, logger.*, console.log, System.out.println, log4j, logback, sentry, etc.) AND
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:38-41
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a value in the log message that originates from external/attacker input (request body, query param, header, uploaded filename, user-supplied field) WITHOUT stripping newlines (\n, \r, %0a, %0d) before logging.
  The request retains this source rule, criterion or rationale, with its original modal force: Logging of sanitised or fixed strings is NOT a finding.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:43-52
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CLASS C — Plaintext Credentials in Logs (CWE-312 / CWE-532): a log call that records a password, secret, token, or private key value — regardless of whether log injection is possible.
  The request retains this source rule, criterion or rationale, with its original modal force: This is a finding on its own even if the logged value cannot be weaponised for log injection.
  The request retains this source rule, criterion or rationale, with its original modal force: Examples: `L.info(f"POST request with username {username} and password {password}")`, `logger.debug("auth token: %s", token)`, `print(f"secret={key}")`. HARD GATE: log call includes a parameter whose name is password / passwd / secret / token / api_key / private_key / auth_token (case-insensitive), OR the string literal in the log message contains those keywords followed by the variable value.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:54-57
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CLASS B HARD GATE — requires an identifiable security event that produces zero log output on failure: a login function with no logging on incorrect password, an admin action with no audit trail, a permission-denied path with no record.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:59-59
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where to look first (non-exhaustive — reason beyond this list):
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:61-61
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: LOG INJECTION
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:62-63
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: logging.info("User %s logged in", request.form['username']) — if the username contains \n it injects a new log line.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:64-64
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: logger.warning(f"Invalid input: {user_data}") — f-string with raw input.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:65-66
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Any logging call where the format string or arguments include an HTTP parameter, header value, uploaded filename, or user profile field.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:67-68
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Log rotation targets: if a logger writes to a file whose path is user- influenced, the attacker can write to arbitrary files (log4shell-class).
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:69-71
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Structured loggers (structlog, winston, bunyan): if an attacker-controlled key or value is merged into the event dict without sanitisation it can override log levels, timestamps, or inject arbitrary fields.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:73-73
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MISSING LOGGING
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:74-75
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Authentication: failed login with wrong password, locked account, expired session — if none of these produce a log entry, brute-force is invisible.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:76-77
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Admin actions (user role change, account deletion, config update) with no audit log.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:78-79
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Security exceptions (PermissionDenied, AccessDenied, AuthenticationError) caught and swallowed silently (bare except: pass, except Exception: continue).
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:80-80
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Password reset / MFA enrolment / 2FA bypass events not logged.
}
```

```sudo
// Source: vvaharness/skills/log-injection/SKILL.md:81-81
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: File upload or download of sensitive files not logged.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../../../../assets/original/vvaharness/skills/log-injection/SKILL.md).
