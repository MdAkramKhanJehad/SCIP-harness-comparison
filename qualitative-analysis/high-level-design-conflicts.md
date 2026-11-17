# High-level design conflicts between the harnesses

## 1. Workflow authority: host-owned stages versus model-directed procedure

**Classification: architectural tradeoff.**

**Visa Vulnerability Agentic Harness:** host code owns the numbered stage transitions, typed artifacts, deterministic transformations, and the boundaries around model sessions. Its architecture explicitly describes deterministic gates after model stages. Evidence: [host-owned stage architecture](../visa-vulnerability-agentic-harness/docs/architecture.md#L47).

**VulnHunter:** the hunting instructions tell the orchestrator to dispatch class-specific investigators, merge their work, complete adversarial verification, and advance through reporting. Python surrounds that procedure with session management and continuation instructions. Evidence: [model-directed investigation](../VulnHunter/vulnhunt/phases/phase2_hunt.md#L9); [workflow continuation instruction](../VulnHunter/vulnhunter-agent/agent/runner.py#L460).

**Same situation:** an investigator has returned results, but the next required investigation phase has not been completed.

**Conflict:** one design places more transition authority in executable host structure; the other places more authority in instructions interpreted by the orchestrator. Both use code and prompts, so this is a relative allocation of authority, not an exclusive distinction.

**Why it matters:** expressing both as an identical pseudocode loop conceals whether the transition is enforced or requested. This is a design conflict, not evidence that either source contains an incorrect instruction.

## 2. Coverage contract: investigate modeled threats versus resolve inventoried inputs

**Classification: architectural tradeoff with procedural consequences.**

**Visa Vulnerability Agentic Harness:** produce a threat model and derive one investigation unit from each threat with valid surface files. Files outside all threat surfaces are explicitly reported as never reviewed by those units. Evidence: [threat-derived assignment](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s3_decompose.py#L15); [unassigned file coverage](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s3_decompose.py#L169).

**VulnHunter:** reconnaissance enumerates external inputs; investigation must resolve those inputs across class groups. Its input inventory is presented as the completeness guarantee. Evidence: [inventory-based completeness](../VulnHunter/vulnhunt/phases/phase1_recon.md#L55); [required input resolution](../VulnHunter/vulnhunt/phases/phase2_shared.md#L90).

**Same situation:** a production input is inventoried, but no explicit threat in the threat model names its file.

**Conflict:** VulnHunter's coverage obligation follows the inventoried input; Visa Vulnerability Agentic Harness's threat-derived investigation obligation follows the modeled threat and validated surface. Completing one ledger does not establish completion of the other.

**Why it matters:** later deterministic detectors or sink audits can recover omissions, but they do not make the initial coverage contracts equivalent. A common representation must retain the denominator behind a completeness claim.

## 3. Search objective: bounded investigation versus exhaustive tracing obligations

**Classification: architectural tradeoff.**

**Visa Vulnerability Agentic Harness:** cap threat-model output and investigation resource use, with explicit controls for model calls and other budgets. Evidence: [threat output cap](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s2/__init__.py#L235); [investigation model-call cap](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s4/session.py#L105).

**VulnHunter:** require all relevant paths, callers, readers, and assigned inputs to be traced; its dispatch wave limit bounds simultaneous agents rather than total investigation. Evidence: [exhaustive tracing obligation](../VulnHunter/vulnhunt/SKILL.md#L155); [concurrency instruction](../VulnHunter/vulnhunt/phases/phase2_hunt.md#L54).

**Same situation:** a remaining caller has not been inspected when the investigation's available resource allowance is exhausted.

**Conflict:** a bounded session may terminate before the exhaustive obligation is satisfied. The exhaustive instruction does not itself provide a resource policy for completing arbitrarily large work.

**Why it matters:** this is an unresolved cost-versus-completeness tradeoff between designs. It does not establish that VulnHunter has no runtime limits or that Visa Vulnerability Agentic Harness intends to inspect only one path.

## 4. Finding identity: separate attack contexts versus a shared engineering fix

**Classification: conditional policy conflict.**

**VulnHunter:** the general anti-merge rule preserves different attacker authentication levels, routes, middleware contexts, and exploited parameters. Evidence: [attack-context identity](../VulnHunter/vulnhunt/phases/phase2b_verify.md#L267).

**Visa Vulnerability Agentic Harness:** the semantic consolidation prompt asks whether one engineering fix closes both findings and explicitly permits merging different call sites through a shared helper. Evidence: [engineering-fix identity](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s7/prompts.py#L26); [shared-helper consolidation](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s7/prompts.py#L33).

**Same situation:** two routes with different authentication contexts call the same defective helper, and one helper edit fixes both.

**Conflict:** VulnHunter's general rule says to keep the attack contexts separate; the semantic consolidation rule permits one canonical defect with multiple locations.

**Why it matters:** the number of reported findings changes without a change in discovered paths. This comparison is conditional: semantic consolidation is disabled in the shipped default Visa profile, and both harnesses contain more specific rules and exceptions. The low-level document separately compares an active deterministic merge rule.
