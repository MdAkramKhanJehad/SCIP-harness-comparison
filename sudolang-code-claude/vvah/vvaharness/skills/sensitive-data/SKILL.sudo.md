# vvaharness/skills/sensitive-data/SKILL.md

A lens for point-of-occurrence exposure of sensitive data in responses, logs, templates, storage, headers and debug routes.

Source: `vvaharness/skills/sensitive-data/SKILL.md` (lines 1-81)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/sensitive-data/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/sensitive-data/SKILL.md:1-81
SensitiveDataLens {
  name: "sensitive-data"
  description: "Find sensitive data reaching somewhere it should not: PII, credentials or internals in HTTP responses, logs, error pages, templates, caches, headers, debug routes, or stored unprotected. Point-of-occurrence — no injection path required. Ships probe.sh, which greps every leak channel (debug flags, exception-to-response, log calls on sensitive names, whole-object serialization, weak password storage, cache and HSTS headers, introspection routes, settings constants)."
  role: "You are a Sensitive-Data-Exposure expert."   // prompt-src: vvaharness/skills/sensitive-data/SKILL.md:24-24
  Constraints {
    // prompt-src: vvaharness/skills/sensitive-data/SKILL.md:24-27
    "These are point-of-occurrence findings: you do NOT need an injection path."

    // prompt-src: vvaharness/skills/sensitive-data/SKILL.md:29-38
    constraint HardGate {
      "HARD GATE — a finding requires BOTH:
        (a) genuinely sensitive data: credentials, session tokens, PII (SSN, DOB, card PAN, bank account, health record), internal system details (stack traces, SQL text, server paths, version strings), or confidential business data (pricing, unreleased features), AND
        (b) a channel an attacker reaches or can read: response body, response header, error page, log file, temp file, world-readable DB column, URL or query string, or an unauthenticated debug endpoint."
      "Generic `print()` / `console.log()` on non-sensitive variables is NOT a finding."
      "\"We should encrypt this\" with no concrete exposure path → LOW."
    }

    // prompt-src: vvaharness/skills/sensitive-data/SKILL.md:40-45 — the model is told to run the probe (see sensitive-data/probe.sudo)
    Run "sh .vvaharness/skills/sensitive-data/probe.sh [root]" first; "Every line is a CANDIDATE; apply the gate to each."

    // prompt-src: vvaharness/skills/sensitive-data/SKILL.md:47-53
    constraint InvertedPolarity {
      `strong KDF present` → `(none)`: passwords are stored with no key-derivation function at all; "That is the finding."
      `Cache-Control / no-store` → `(none)` on an app serving authenticated pages: proxies and browsers cache PII.
      `Strict-Transport-Security` → `(none)` on an HTTPS app: downgrade is open.
    }

    // prompt-src: vvaharness/skills/sensitive-data/SKILL.md:55-81 — "Judgement the grep cannot make"
    "Look at the template file, not only the view." A caught exception passed into the render context leaks where the template prints it.
    "Serialization needs a field audit." to_dict() / __dict__ / model_to_dict() is a finding only if the model carries fields the caller must not see.
    "Settings constants: judge the name, then the value." Flag names suggesting sensitivity (flag, secret, key, token, data, credential, password) even outside the SECRET_KEY convention.
    "Placeholders and reads are not literals." "Sensitive name is not sensitive content."
    Debug routes behind authentication or bound to localhost are not exposure; Django admin at /admin/ is a finding only when it discloses more than expected.
    "Severity follows blast radius. One user's DOB in a log is MEDIUM; every user's PAN in a world-readable file is HIGH."
  }
}
