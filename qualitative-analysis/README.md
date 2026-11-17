# Conflicts between Visa Vulnerability Agentic Harness and VulnHunter

This analysis compares the two harnesses against each other at every layer. Each conflict identifies what one harness requires, what the other requires, and a situation where the difference changes the investigation or decision. It does not catalog contradictions inside either harness.

The strongest conflicts concern what reconnaissance may read, what counts as a reportable attack surface, how to classify path manipulation, how to handle unavailable evidence, and when separate findings may be merged.

## Reading order

1. [Method and scope](method-and-scope.md): what qualifies as an opposing rule, a conditional conflict, or an architectural tradeoff.
2. [High-level design conflicts](high-level-design-conflicts.md): four conflicting design commitments.
3. [Mid-level workflow conflicts](mid-level-workflow-conflicts.md): five procedural conflicts, including reconnaissance and verification.
4. [Low-level rule conflicts](low-level-rule-conflicts.md): eight paired rules applied to concrete cases.
5. [Comparison consequences](comparison-consequences.md): how these disagreements affect a common pseudocode representation and evaluation.

## Concrete examples

| Same case | Visa Vulnerability Agentic Harness | VulnHunter | Conflict |
|---|---|---|---|
| A repository contains an architecture document. | Read selected documentation to construct the threat model. | The general operating rule says to ignore documentation. | Read versus exclude during preparation. |
| A build file contains a security-relevant operation. | The built-in file walker keeps Dockerfile and Makefile files, subject to later configuration. | The general scope rule excludes build files, with a specific infrastructure-security exception. | Retain for possible review versus exclude unless the exception applies. |
| Attacker input changes only an outbound request's path; origin cannot change. | Refute the server-side request forgery classification; another class may apply. | Reconnaissance explicitly inventories fixed-base concatenations as request-forgery/path-traversal sinks. | Exclude from one class versus include in a combined hunt category. |
| A browser fetch chooses a different configuration asset through path traversal. | The verifier excludes server-side path-traversal classes on pure browser code. | The injection playbook explicitly includes client-side configuration/asset traversal. | Exclude that class in this execution context versus investigate it. |
| A required defense implementation is unavailable. | The verifier allows an inconclusive outcome when needed evidence cannot be reached. | The generic sanitizer gate says to treat the unavailable defense as ineffective and continue. | Suspend judgment versus continue under an adverse assumption. |

Each row is qualified and sourced in the detailed documents. These are rule-level consequences, not measured model outcomes. Some differences affect investigation or classification without implying opposite final vulnerability verdicts.

The analysis concerns the local checkouts as available on November 16, 2026. Optional exploit verification remains excluded. Full terms are used in the prose; exact source identifiers are preserved where needed for traceability. Neither harness, the common pseudocode, the knob records, nor the shared schema was changed.
