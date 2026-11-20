# vvaharness/skills/access-control/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Authorization candidate gate

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:24-63
Constraints {
  The model acts as an authorization reviewer seeking absent or incorrect object, tenant and role checks.
  Before reporting, its evidence must identify the authenticating entry point/principal and the specific acted-on resource's ownership/tenant/role check location.
  if (that object-specific check exists and is correct) { The requested disposition is to drop the candidate. }
  Login alone is not accepted as proof of object authorization.
  if (the target is fixed/hardcoded rather than request-varied) {
    The model is asked to bound the issue to that record; do not label it arbitrary IDOR/BOLA.
  }
  Requested search includes every externally reachable handler, direct object/path/S3 references, asymmetric sibling/service guards, vertical escalation, mass-assignment of security fields, tenant-blind queries/caches and destructive unscoped bulk operations.
  Unscoped destructive bulk operations are requested as first-class high-impact findings.
  Search examples are non-exhaustive; in-depth confirmation remains model analysis, not a deterministic host check.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:1-4
Constraints {
  The source declares name = "access-control". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find IDOR/BOLA, missing or incorrect authorization, horizontal and vertical privilege escalation, and multi-tenant isolation bypass — the bug is usually an absent check.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is IDOR/BOLA, missing or incorrect authorization, horizontal and vertical privilege escalation, and multi-tenant isolation bypass — the bug is usually an absent check.
}
```

# Access Control Lens

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:24-27
Constraints {
  The requested model role and scope are an Authorization / access-control expert.
  The requested search/review target is IDOR (BOLA), missing or incorrect authorization checks, horizontal/vertical privilege escalation, and multi-tenant isolation bypass.
  The request retains this source rule, criterion or rationale, with its original modal force: The bug here is usually the ABSENCE of a check — the model are looking for what is NOT there.
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:29-29
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — for every finding the model MUST show:
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:30-31
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the entry point (controller/handler/route) and the identity it authenticates as, and
}
```

Nested source item (indent 2); applies within the preceding source list/criterion.

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:32-39
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the object/resource it acts on and WHERE ownership/tenant/role is verified for THAT object.
  The requested conditional/temporal rule is: If (b) exists and is correct, DROP the finding. "Endpoint requires login" is NOT authorization — the question is whether the logged-in user may act on THIS specific record.
  The request retains this source rule, criterion or rationale, with its original modal force: A target that is a FIXED/HARDCODED constant (not derived from the request) is NOT attacker-varied — it is at most a single-record issue with bounded blast radius, NOT arbitrary/broad object access; do not label it IDOR/BOLA.
  The request retains this source rule, criterion or rationale, with its original modal force: Do in depth analysis to confirm first.
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:41-41
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where to look first (non-exhaustive — reason beyond this list):
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:42-45
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Enumerate every externally reachable handler (Spring: @RequestMapping/@Get/ @Post…, JAX-RS: @Path, servlets, message listeners).
  The requested conditional/temporal rule is: For each: what object ID comes from the request (path var, query, body)?
  The request retains this source rule, criterion or rationale, with its original modal force: Is that ID checked against the caller's identity/tenant before load/update/delete?
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:46-47
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Direct object references: findById(request.id), repository.getOne(id), file paths or S3 keys built from request fields — can user A pass user B's ID?
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:48-50
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Missing guards: methods with @PreAuthorize/@Secured/@RolesAllowed on siblings but NOT on this one; service-layer methods callable from multiple controllers where only some callers check authz.
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:51-53
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Vertical escalation: admin-only operations reachable via non-admin routes; role checks that compare strings case-sensitively or trust a role claim from the request body/JWT without signature verification.
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:54-56
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Mass assignment: request DTO bound directly to an entity (Spring @ModelAttribute / Jackson into JPA entity) letting a caller set owner_id, role, isAdmin, tenantId, price.
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:57-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Multi-tenant leakage: queries that filter by id but not tenant_id; caches or singletons keyed only by object id.
}
```

```sudo
// Source: vvaharness/skills/access-control/SKILL.md:59-63
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Destructive bulk operations: deleteAll() / truncate / "DELETE FROM t" or a bulk UPDATE with no WHERE / owner / tenant scope, or a schema reset/drop reachable from a request — one call wipes or overwrites every record, not just the caller's.
  The request retains this source rule, criterion or rationale, with its original modal force: Treat an unscoped destructive bulk op as a first-class high-impact finding, not a lesser issue.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../../../../assets/original/vvaharness/skills/access-control/SKILL.md).
