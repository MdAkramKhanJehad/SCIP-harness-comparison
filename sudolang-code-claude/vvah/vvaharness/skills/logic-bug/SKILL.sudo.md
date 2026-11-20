# vvaharness/skills/logic-bug/SKILL.md

A lens for behavioural and state-machine defects that have no single grep signature.

Source: `vvaharness/skills/logic-bug/SKILL.md` (lines 1-54)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/logic-bug/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/logic-bug/SKILL.md:1-54
LogicBugLens {
  name: "logic-bug"
  description: "Find business-logic defects: missing validation on amounts and quantities, race conditions and TOCTOU, workflow steps that can be skipped or replayed."
  Constraints {
    // prompt-src: vvaharness/skills/logic-bug/SKILL.md:24-26
    Review for behavioural and state-machine defects that surface only when reasoning about ordering, concurrency and edge-case inputs.

    // prompt-src: vvaharness/skills/logic-bug/SKILL.md:28-32
    constraint HardGate {
      "HARD GATE — for every finding you MUST cite the exact trust boundary that is crossed: the file:line where untrusted/external input enters, and the file:line where the security decision is made on that input."
      "If both sides are internal (service-to-service, same trust domain, idempotent retry, intentional design), DROP the finding."
      "No trust-boundary citation → no finding."
    }

    // prompt-src: vvaharness/skills/logic-bug/SKILL.md:34-54 — "Reason about behaviour, don't pattern-match. Seed questions:"
    Check-then-act windows between a permission, ownership or balance check and the mutation.
    Authentication and session state on empty, null, duplicated or out-of-order messages; concurrent requests leaving a session half-authenticated.
    Numeric identity and counters at overflow, zero, or negative after a narrowing cast; 32-bit truncated identifiers colliding with a privileged record.
    Connection or protocol state left mid-parse by a malformed message so the next request is misinterpreted.
    Caches and memoized decisions missing the tenant, user or role dimension; a cached "authorised" decision outliving a revocation.
    Sentinel return values (indexOf / find / search returning -1 or null, parseInt returning NaN) used as offset, length or success without the "== -1" guard.
  }
}
