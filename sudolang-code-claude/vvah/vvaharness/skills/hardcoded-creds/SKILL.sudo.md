# vvaharness/skills/hardcoded-creds/SKILL.md

A lens for literal secrets committed to source or configuration, with an explicit severity table.

Source: `vvaharness/skills/hardcoded-creds/SKILL.md` (lines 1-76)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/hardcoded-creds/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/hardcoded-creds/SKILL.md:1-76
HardcodedCredsLens {
  name: "hardcoded-creds"
  description: "Find credentials, keys, tokens and signing secrets committed in source, config, manifests or deployment files."
  role: "You are a Hardcoded-Credentials expert."   // prompt-src: vvaharness/skills/hardcoded-creds/SKILL.md:24-24
  Constraints {
    // prompt-src: vvaharness/skills/hardcoded-creds/SKILL.md:24-26
    The attacker model is anyone with read access to the repository (developer, CI system, leaked archive).

    // prompt-src: vvaharness/skills/hardcoded-creds/SKILL.md:28-31
    constraint HardGate {
      "HARD GATE — a finding requires an ACTUAL VALUE committed to source, not a reference to an environment variable."
      "${ENV_VAR}, os.environ.get('KEY'), process.env.KEY, @Value(\"${...}\") are NOT findings — they load from the environment at runtime."
      "Only report literal values that are directly usable."
    }

    // prompt-src: vvaharness/skills/hardcoded-creds/SKILL.md:33-47 — settings and config files, "highest yield — scan these first"
    Django settings.py literals (SECRET_KEY, DATABASES password, EMAIL_HOST_PASSWORD, AWS_SECRET_ACCESS_KEY, STRIPE_SECRET_KEY); "Flag ALL literal values in security-sensitive keys, not just common names."
    Flask config (SECRET_KEY, SQLALCHEMY_DATABASE_URI with embedded password, JWT_SECRET_KEY, MAIL_PASSWORD).
    Committed .env files; "Even sample .env files with real-looking secrets are findings."
    Spring application.properties / application.yml secrets; config.yaml / config.json keys named password, secret, token, api_key, private_key, access_key holding a non-placeholder string.

    // prompt-src: vvaharness/skills/hardcoded-creds/SKILL.md:48-68 — source code
    Literal JWT signing secrets, API keys, database passwords in connection strings, cryptographic key bytes, admin or default passwords in seeding or migration scripts, real credentials in test files, passwords in comments.
    "Flag every hardcoded credential used in an authentication comparison, even if the variable name is not 'password'."   // for example if username == 'admin' and password == 'secret'
    In-memory user stores (dict or map literals whose password key holds a non-hashed string) and attribute assignments (app.secret_key = 'literal', self.password = 'literal').

    // prompt-src: vvaharness/skills/hardcoded-creds/SKILL.md:70-76
    constraint SeverityRules {
      "Signing keys / JWT secrets / crypto keys → CRITICAL (forgeable tokens, key material)"
      "DB connection passwords / cloud API keys → HIGH (data access / billing abuse)"
      "Internal service tokens / webhook secrets → HIGH"
      "Default / demo passwords shipped in seed data → MEDIUM"
      "Placeholder-looking values (\"changeme\", \"TODO\", \"FIXME\") → LOW (note only) unless the application appears to actually use them in production paths."
    }
  }
}
