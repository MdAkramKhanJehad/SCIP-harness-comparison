# Mid-level workflow conflicts between the harnesses

## 1. Reconnaissance: infer a threat model from a snapshot versus enumerate concrete sources and sinks

**Classification: conditional procedural conflict.**

**Visa Vulnerability Agentic Harness:** the threat-model prompt says its initial input is a structural snapshot containing documentation, manifests, modules, entry points, configuration representatives, and contracts, rather than source bodies. It explicitly asks for plausible threats and leaves source checking to later stages. Evidence: [snapshot-based threat modeling](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s2/prompts.py#L40); [retain plausible threats](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s2/prompts.py#L67).

**VulnHunter:** reconnaissance first enumerates dangerous sinks, then external inputs and concrete input locations. Investigation safety is deferred until the inventory exists. Evidence: [sink-first reconnaissance](../VulnHunter/vulnhunt/phases/phase1_recon.md#L24); [deferred input safety judgment](../VulnHunter/vulnhunt/phases/phase1_recon.md#L170).

**Same case:** architecture documents suggest a batch-import trust boundary, but the concrete imported-field inventory is incomplete.

**Different action:** Visa's threat-model procedure can retain the plausible boundary and threat as work; VulnHunter's reconnaissance procedure must continue identifying concrete inputs and sinks rather than treating the architectural description as a completed inventory.

**Implication:** a threat model and a reconnaissance input inventory cannot substitute for one another even though both precede hunting. Neither rule by itself determines whether a final vulnerability is accepted.

## 2. Work decomposition: preserve a threat surface versus repeat each partition across class groups

**Classification: architectural tradeoff expressed as opposing assignment rules.**

**Visa Vulnerability Agentic Harness:** decomposition creates one unit per threat with its validated surface carried uncut. Evidence: [uncut threat surface](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s3_decompose.py#L91).

**VulnHunter:** each normal production partition gets separate class-group investigators; the prompt prohibits combining those groups. Evidence: [separate class-group assignments](../VulnHunter/vulnhunt/phases/phase2_hunt.md#L28); [sequential fallback exception](../VulnHunter/vulnhunt/phases/phase2_hunt.md#L67).

**Same case:** one surface contains injection, navigation, and logic concerns.

**Different action:** the threat-based procedure preserves the threat's full surface as a unit; the partition-based procedure repeats that partition across distinct class perspectives. VulnHunter has an explicit sequential fallback, so the class separation is not a claim that all work always runs concurrently.

**Implication:** matching the number of agents or batch size does not match the investigated work. Compare both the assignment object and the required class coverage.

## 3. Verification: new independent inspection versus a consensus-based early stop

**Classification: conditional policy conflict.**

**Visa Vulnerability Agentic Harness:** the verifier is told to assume the claim is wrong until it confirms the source itself. Evidence: [independent source confirmation](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s6/prompts.py#L25).

**VulnHunter:** matching Gate 1 eliminations by all partition investigators can be recorded without rereading source. Any actual candidate from any investigator still requires full verification. Evidence: [consensus-based early stop](../VulnHunter/vulnhunt/phases/phase2b_verify.md#L37); [candidate exception](../VulnHunter/vulnhunt/phases/phase2b_verify.md#L40).

**Same case:** investigators all mark a partition unreachable and cite the same location.

**Different action:** VulnHunter explicitly permits accepting that elimination without a fresh read. Visa's verifier instruction requires its own source confirmation for the claims that reach that stage.

**Implication:** these are different rechecking policies, not proof that the exact eliminated object would reach Visa's verifier. The conflict concerns the required freshness of evidence, with different stage input contracts clearly retained.

## 4. Consolidation: explicit platform rollup versus optional semantic grouping

**Classification: conditional policy conflict.**

**VulnHunter:** when all applicable handlers lack valid authentication, the verification procedure requires one platform authentication finding and subsumes specified authentication and authorization classes. It explicitly overrides the normal anti-merge rule. Evidence: [platform authentication rollup](../VulnHunter/vulnhunt/phases/phase2b_verify.md#L235); [rollup exception](../VulnHunter/vulnhunt/phases/phase2b_verify.md#L245).

**Visa Vulnerability Agentic Harness:** default deterministic consolidation is based on site proximity and weakness compatibility; semantic consolidation is disabled in its shipped default profile. Evidence: [same-file deterministic grouping](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s7/collapse.py#L186); [default semantic consolidation disabled](../visa-vulnerability-agentic-harness/vvaharness/config/profiles/default.yaml#L323).

**Same case:** two separately verified missing-authentication findings occur in different files and collectively satisfy VulnHunter's platform rule.

**Different action:** VulnHunter requires the platform rollup. Visa's default deterministic consolidation does not merge those two findings merely because both belong to a globally missing authentication layer.

**Implication:** this is a concrete configuration-conditioned difference in report identity. The rollup retains an audit trail; it should not automatically be scored as missing a vulnerability.

## 5. Remediation intake: local provenance requirement versus issue-driven portability

**Classification: conditional lifecycle conflict.**

**Visa Vulnerability Agentic Harness:** fix validation accepts cases recorded locally by remediation on the same machine and checkout path; a case committed in a repository is not sufficient authority. Evidence: [local provenance requirement](../visa-vulnerability-agentic-harness/AGENTS.md#L160).

**VulnHunter:** its default in-place fixer harvests labeled issues from the repository and creates per-finding worktrees and pull requests. Evidence: [issue-based fixer intake](../VulnHunter/vulnhunter-fix/README.md#L40).

**Same case:** a finding and proposed change arrive through an issue from another machine, without a local remediation record.

**Different action:** the issue is a supported intake object for the VulnHunter fixer; it does not alone qualify as a trusted case for Visa's validation procedure.

**Implication:** the comparison spans different lifecycle stages, so it does not establish that either harness cannot import or process external findings through other interfaces. It shows that a portable issue and a locally owned validation case carry different authority.
