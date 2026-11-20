# vvaharness/skills/access-control/SKILL.md

A lens telling the model how to hunt missing or wrong authorization (IDOR / BOLA, privilege escalation, tenant isolation, unscoped bulk deletes).

Source: `vvaharness/skills/access-control/SKILL.md` (lines 1-63)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/access-control/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/access-control/SKILL.md:1-63
AccessControlLens {
  name: "access-control"
  description: "Find IDOR/BOLA, missing or incorrect authorization, horizontal and vertical privilege escalation, and multi-tenant isolation bypass — the bug is usually an absent check."
  role: "You are an Authorization / access-control expert."   // prompt-src: vvaharness/skills/access-control/SKILL.md:24-24
  Constraints {
    // prompt-src: vvaharness/skills/access-control/SKILL.md:24-27
    Hunt for IDOR (BOLA), missing or incorrect authorization checks, horizontal and vertical privilege escalation, and multi-tenant isolation bypass.
    "The bug here is usually the ABSENCE of a check — you are looking for what is NOT there."

    // prompt-src: vvaharness/skills/access-control/SKILL.md:29-39 — hard gate
    constraint HardGate {
      "HARD GATE — for every finding you MUST show:
        (a) the entry point (controller/handler/route) and the identity it authenticates as, and
        (b) the object/resource it acts on and WHERE ownership/tenant/role is verified for THAT object."
      "If (b) exists and is correct, DROP the finding."
      "\"Endpoint requires login\" is NOT authorization — the question is whether the logged-in user may act on THIS specific record."
      "A target that is a FIXED/HARDCODED constant (not derived from the request) is NOT attacker-varied — it is at most a single-record issue with bounded blast radius, NOT arbitrary/broad object access; do not label it IDOR/BOLA."
      "Do in depth analysis to confirm first."
    }

    // prompt-src: vvaharness/skills/access-control/SKILL.md:41-63 — "Where to look first (non-exhaustive — reason beyond this list)"
    Enumerate every externally reachable handler (Spring request mappings, JAX-RS @Path, servlets, message listeners); for each, find the object identifier taken from the request and whether it is checked against the caller's identity or tenant before load, update or delete.
    Direct object references: findById(request.id), repository.getOne(id), file paths or S3 keys built from request fields — "can user A pass user B's ID?"
    Missing guards: @PreAuthorize / @Secured / @RolesAllowed on sibling methods but not this one; service methods reached from several controllers where only some callers check authorization.
    Vertical escalation: admin-only operations reachable through non-admin routes; case-sensitive role string comparison; a role claim trusted from the request body or a JWT without signature verification.
    Mass assignment: a request DTO bound directly to an entity, letting a caller set owner_id, role, isAdmin, tenantId, price.
    Multi-tenant leakage: queries filtering by id but not tenant_id; caches or singletons keyed only by object id.
    "Treat an unscoped destructive bulk op as a first-class high-impact finding, not a lesser issue."   // deleteAll(), truncate, DELETE or bulk UPDATE with no WHERE / owner / tenant scope, or a schema reset reachable from a request
  }
}
