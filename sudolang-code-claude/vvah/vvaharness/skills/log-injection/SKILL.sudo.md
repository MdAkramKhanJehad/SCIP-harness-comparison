# vvaharness/skills/log-injection/SKILL.md

A lens covering three classes: log injection, missing security logging, and plaintext credentials written to logs.

Source: `vvaharness/skills/log-injection/SKILL.md` (lines 1-81)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/log-injection/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/log-injection/SKILL.md:1-81
LogInjectionLens {
  name: "log-injection"
  description: "Find unsanitised input reaching log sinks: forged log records, injected control characters, and sensitive values written to logs."
  role: "You are a Log-Injection / Insufficient-Logging expert."   // prompt-src: vvaharness/skills/log-injection/SKILL.md:24-24
  Constraints {
    // prompt-src: vvaharness/skills/log-injection/SKILL.md:24-33
    Hunt for two distinct classes:   // preserved: the text announces "two distinct classes" and then defines three (A, B and C at lines 43-52)
    CLASS A — Log Injection (CWE-117): attacker-controlled data written to logs without sanitisation (forged entries, log poisoning, downstream parser exploitation).
    CLASS B — Missing / Insufficient Logging (CWE-778, OWASP A09): security-relevant events not logged at all.

    // prompt-src: vvaharness/skills/log-injection/SKILL.md:35-41
    constraint ClassAHardGate {
      "CLASS A HARD GATE — requires BOTH:
        (a) a log call (logging.*, logger.*, console.log, System.out.println, log4j, logback, sentry, etc.) AND
        (b) a value in the log message that originates from external/attacker input (request body, query param, header, uploaded filename, user-supplied field) WITHOUT stripping newlines (\n, \r, %0a, %0d) before logging."
      "Logging of sanitised or fixed strings is NOT a finding."
    }

    // prompt-src: vvaharness/skills/log-injection/SKILL.md:43-52
    constraint ClassC {
      CLASS C — Plaintext Credentials in Logs (CWE-312 / CWE-532): a finding on its own even when the value cannot be weaponised for log injection.
      "HARD GATE: log call includes a parameter whose name is password / passwd / secret / token / api_key / private_key / auth_token (case-insensitive), OR the string literal in the log message contains those keywords followed by the variable value."
    }

    // prompt-src: vvaharness/skills/log-injection/SKILL.md:54-57
    constraint ClassBHardGate {
      "CLASS B HARD GATE — requires an identifiable security event that produces zero log output on failure: a login function with no logging on incorrect password, an admin action with no audit trail, a permission-denied path with no record."
    }

    // prompt-src: vvaharness/skills/log-injection/SKILL.md:59-81 — "Where to look first (non-exhaustive — reason beyond this list)"
    Log injection: request fields formatted into log calls (printf-style or f-strings); HTTP parameters, headers, uploaded file names or profile fields in log arguments; a log file path influenced by the user; attacker keys or values merged into structured-logger event dictionaries.
    Missing logging: failed logins, locked accounts, expired sessions; admin actions with no audit log; security exceptions swallowed silently; password reset, MFA enrolment and 2FA bypass events; upload or download of sensitive files.
  }
}
