# vvaharness/skills/hardcoded-creds/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Literal credentials and requested severity

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:24-76
Constraints {
  The requested attacker has repository read access; findings require directly usable committed literal values.
  if (the value is only an environment/config interpolation or runtime secret-source read) { The model is asked not to report a literal credential. }
  Settings/config files are the requested first/high-yield search, followed by source; include live-looking sample values, actual credentials in tests/comments, auth equality checks, nested in-memory user maps and attribute assignments, including unconventional sensitive names.
  Requested severities: signing/JWT/crypto key material CRITICAL; database/cloud/internal-service/webhook credentials HIGH; shipped demo/default seed passwords MEDIUM.
  if (a value looks like changeme, TODO or FIXME) {
    The model is asked to treat it as LOW/note-only unless it appears actually used in production paths.
  }
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:1-4
Constraints {
  The source declares name = "hardcoded-creds". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find credentials, keys, tokens and signing secrets committed in source, config, manifests or deployment files.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is credentials, keys, tokens and signing secrets committed in source, config, manifests or deployment files.
}
```

# Hardcoded Creds Lens

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:24-26
Constraints {
  The requested model role and scope are a Hardcoded-Credentials expert.
  The requested search/review target is secrets baked into source code or checked-in configuration — the attacker model is anyone with read access to the repository (developer, CI system, leaked archive).
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:28-31
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — a finding requires an ACTUAL VALUE committed to source, not a reference to an environment variable. ${ENV_VAR}, os.environ.get('KEY'), process.env.KEY, @Value("${...}") are NOT findings — they load from the environment at runtime.
  The request retains this source rule, criterion or rationale, with its original modal force: Only report literal values that are directly usable.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:33-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where to look first (non-exhaustive — reason beyond this list):
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:35-35
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SETTINGS / CONFIG FILES (highest yield — scan these first)
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:36-38
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Django settings.py: SECRET_KEY = '...literal...', DATABASES password literal, EMAIL_HOST_PASSWORD, AWS_SECRET_ACCESS_KEY, STRIPE_SECRET_KEY.
  The request retains this source rule, criterion or rationale, with its original modal force: Flag ALL literal values in security-sensitive keys, not just common names.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:39-40
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Flask config.py / app.config: SECRET_KEY, SQLALCHEMY_DATABASE_URI with embedded password, JWT_SECRET_KEY, MAIL_PASSWORD.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:41-42
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: .env files committed to the repo (not in .gitignore): KEY=literal_value.
  The request retains this source rule, criterion or rationale, with its original modal force: Even sample .env files with real-looking secrets are findings.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:43-44
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: application.properties / application.yml (Spring): spring.datasource.password, spring.security.oauth2.client.secret, jwt.secret.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:45-46
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config.yaml / config.json: any key named password, secret, token, api_key, private_key, access_key containing a non-placeholder string value.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SOURCE CODE
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:49-49
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hardcoded JWT signing secrets: jwt.encode(payload, "literal_secret", ...)
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:50-51
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hardcoded API keys: requests.get(..., headers={"Authorization": "Bearer sk-literal..."}) or api_key = "literal"
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:52-52
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hardcoded DB passwords: psycopg2.connect("...password=literal...")
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:53-53
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hardcoded cryptographic keys: AES_KEY = b"0123456789abcdef"
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:54-54
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hardcoded admin/default passwords in user-seeding or migration scripts.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:55-56
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Test files with real credentials (test_*.py, *_test.go) — these get committed and are just as exploitable as production code.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:57-57
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Passwords committed as comments: # password is 'literal' (for testing)
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:58-62
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: In-function auth comparison checks: `if username == 'admin' and password == 'secret'` or `elif name=='jack' and password=='jacktheripper'` — literal values in equality comparisons inside view/handler/auth functions are just as dangerous as assignment patterns.
  The request retains this source rule, criterion or rationale, with its original modal force: Flag every hardcoded credential used in an authentication comparison, even if the variable name is not 'password'.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:63-65
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: In-memory user stores with hardcoded credentials: `users = {'admin': {'password': 'admin123'}}` — dict/map literals where the 'password' key holds a non-hashed string value.
  The request retains this source rule, criterion or rationale, with its original modal force: Includes Flask/Express in-memory user tables.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:66-68
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Object attribute assignment: `app.secret_key = 'literal'`, `self.password = 'literal'` — attribute-style assignments to security- sensitive names are equivalent to variable assignments.
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:70-70
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SEVERITY RULES
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:71-71
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Signing keys / JWT secrets / crypto keys → CRITICAL (forgeable tokens, key material)
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:72-72
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DB connection passwords / cloud API keys → HIGH (data access / billing abuse)
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:73-73
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Internal service tokens / webhook secrets → HIGH
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:74-74
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Default / demo passwords shipped in seed data → MEDIUM
}
```

```sudo
// Source: vvaharness/skills/hardcoded-creds/SKILL.md:75-76
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Placeholder-looking values ("changeme", "TODO", "FIXME") → LOW (note only) unless the application appears to actually use them in production paths.
}
```

