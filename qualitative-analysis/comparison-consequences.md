# Consequences of the cross-harness conflicts

## The most consequential disagreements

The reconnaissance conflicts affect what information reaches later reasoning. Documentation and build-file exclusions can remove a surface before investigators evaluate it. The class-definition conflicts affect how an investigated surface is routed or labeled. The evidence conflict affects whether unknown behavior stops a judgment or is treated as a missing defense. The consolidation conflict changes whether two discovered attacks retain separate identities.

These are different causal mechanisms. They should not be combined into a single statement that one harness is stricter. One can be broader in preparation, narrower in a vulnerability class, more conservative about uncertainty, and more aggressive about merging at the same time.

## Preserve paired decisions in common pseudocode

| Decision | Required comparison information |
|---|---|
| Read or exclude a file | Stage, artifact type, explicit exceptions, and effective configuration. |
| Create investigation work | Threat or input identity, assigned surface, and completeness denominator. |
| Classify a path manipulation | Execution environment, actual destination control, backend path semantics, and allowed alternate class. |
| Establish reachability | Local call sites, framework entry points, and external library consumers. |
| Handle unavailable evidence | Unknown fact, default assumption, unresolved outcome, and named exceptions. |
| Merge two findings | Parameter identity, attacker context, root cause, weakness identity, and retained locations. |

The same pseudocode format should expose these rule disagreements rather than replacing them with a shared generic instruction such as investigate all inputs or verify reachability. Matching procedure names cannot establish matching policy.

## Avoid three misleading comparisons

**Finding count:** VulnHunter's parameter-sensitive anti-merge rule and Visa's deterministic site grouping can yield different canonical counts for the same discovered attacks. Compare attack paths and root causes before comparing totals.

**Coverage:** completing all threat units is not the same claim as resolving every inventoried input. Preserve original inventories and identify surfaces omitted before assignment.

**Precision:** a difference in class labels or uncertainty handling does not establish measured false-positive rates. A fixed-origin path injection reclassified by Visa is not automatically a missed vulnerability, and a suspicious cloud key investigated by VulnHunter is not automatically a false positive.

## Questions for controlled follow-up

1. On the same repository, which documentation and build artifacts does each harness actually read before hunting?
2. When the target has fixed-origin URL path manipulation, do both report the same impact under different classes, or does one drop it?
3. How does each handle externally consumed library functions with no local callers?
4. When a defense cannot be inspected, does the final artifact preserve uncertainty or imply that no effective defense exists?
5. Do two parameters reaching one sink remain separately traceable after consolidation?

Each question follows a paired source conflict. Answering it requires execution traces and adjudication, not assuming perfect compliance with prompt rules. No such runtime outcome is claimed in this analysis.

## Similarities that should not be presented as contradictions

Both harnesses distinguish intended functionality from security boundary failures. Both have exceptions and additional checks for missing controls, non-production code, and shared defenses. Both can preserve a location without accepting the associated claim. Those shared commitments remain compatible even where specific scope, classification, or consolidation rules differ.

For example, VulnHunter explicitly permits infrastructure-security configuration despite its general build-file exclusion, while Visa explicitly allows path manipulation to be classified outside request forgery. These qualifications are part of the comparison, not reasons to erase the narrower paired conflicts.

The result is a layered comparison of disagreements between the two harnesses. It does not recommend repairing either harness or change either implementation, the common pseudocode, or its schema.
