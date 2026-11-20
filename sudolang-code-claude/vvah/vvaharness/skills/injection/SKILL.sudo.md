# vvaharness/skills/injection/SKILL.md

A lens for every injection class under a source, sink and no-defence hard gate, with a probe that lists sink candidates and a census of defences.

Source: `vvaharness/skills/injection/SKILL.md` (lines 1-76)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/injection/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/injection/SKILL.md:1-76
InjectionLens {
  name: "injection"
  description: "Hunt injection classes (SQL, NoSQL, OS command, LDAP, XPath, XXE, CRLF, SSTI, open redirect, path traversal, SSRF, server-emitted XSS, ReDoS) under a source/sink/no-defence hard gate. Ships probe.sh: a per-class sink sweep plus a census of the defences present."
  Constraints {
    // prompt-src: vvaharness/skills/injection/SKILL.md:24-26
    "Find where attacker-controlled input is merged into a downstream interpreter without separating code from data, across every class named in this skill's description."

    // prompt-src: vvaharness/skills/injection/SKILL.md:28-38
    constraint HardGate {
      "HARD GATE — a finding requires ALL THREE:
        (a) a SINK that interprets its input — SQL executor, shell exec, XML parser, HTTP client, response writer, file open, regex compile, template render, redirect, header setter,
        (b) a SOURCE reachable from an external actor — request field, message body, file upload, CLI arg, env var, or a DB row previously written by an untrusted party (second-order),
        (c) NO intervening defence: no parameterisation, no allow-list, no context-correct escaper, no library-provided safe wrapper."
      "If (a)'s argument is a hardcoded literal, or nothing reaches the sink on any path, DROP it."
      "\"We should validate this\" with no sink is not a finding here."
    }

    // prompt-src: vvaharness/skills/injection/SKILL.md:40-45 — the model is told to run the probe (see injection/probe.sudo)
    Run "sh .vvaharness/skills/injection/probe.sh [root]" first.
    "Every line is a CANDIDATE; `(none)` is a real answer, so stop working that class. The sections are a starting set, not the lens."

    // prompt-src: vvaharness/skills/injection/SKILL.md:47-68 — "What refutes a candidate"
    Literal argument: a constant, a column name from a fixed tuple, an internal enumeration.
    Defence in the wrong context (refutation does not hold): HTML escaping for a JavaScript or attribute context; shlex.quote on the binary but not its arguments; an allow-list on a different variable; "%s" interpolated into the query string mistaken for parameter binding.
    Parse-check-use mismatch is a finding: the code checks the parsed URL or path, then uses the raw string.
    Second-order flow: taint written earlier to a database row, cache or config and later concatenated into a query.
    XXE: a parser factory is vulnerable only if disallow-doctype-decl / FEATURE_SECURE_PROCESSING / resolve_entities=False is absent; "The probe finds the factory; you check the flag."
    An SSRF allow-list that still permits 169.254.169.254, metadata.google.internal or metadata.azure.com does not refute.
    ReDoS: catastrophic patterns matter on unbounded input; "on a length-capped field, LOW."
    Zip-Slip counts only with unvalidated member names on an attacker-supplied archive.

    // prompt-src: vvaharness/skills/injection/SKILL.md:70-76
    constraint EnumerationRule {
      "Every distinct sink is its own finding, with its own class (SQLi / CMDi / SSRF / …), file, line, source, and sink."
      "Never collapse them into an omnibus \"input validation missing\" — each sink has its own exploitability and its own fix location."
    }
  }
}
