# Low-level rule conflicts between the harnesses

Each entry pairs rules from both harnesses. The examples describe rule-directed actions under the stated conditions, rather than observed model behavior.

## 1. Documentation: read it for preparation versus ignore it

**Classification: direct rule opposition at preparation scope.**

**Visa Vulnerability Agentic Harness says:** construct system context and trust boundaries from documents and manifests. Its document collector prioritizes threat-model, security, and architecture documents. Evidence: [documentation as context](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s2/prompts.py#L49); [prioritized documentation](../visa-vulnerability-agentic-harness/vvaharness/evidence/docs.py#L25).

**VulnHunter says:** always ignore the named excluded categories, never investigate them, and includes documentation files in that list. Evidence: [scope exclusion instruction](../VulnHunter/vulnhunt/SKILL.md#L85); [documentation exclusion](../VulnHunter/vulnhunt/SKILL.md#L104).

**Same case:** `ARCHITECTURE.md` explains a trust boundary absent from filenames.

**Opposing action:** read it as threat-model input versus exclude it under the general audit-scope rule.

**Boundary:** the disagreement is about context acquisition, not whether a vulnerability written in a document is itself reportable. Visa's document reader is bounded and does not necessarily read every document in full.

## 2. Build artifacts: retain them versus exclude them by default

**Classification: conditional scope conflict.**

**Visa Vulnerability Agentic Harness says:** its built-in file walk keeps Dockerfile, Jenkinsfile, Makefile, infrastructure declarations, and deployment configuration, subject to later exclusions and configuration. Evidence: [retained build and deployment files](../visa-vulnerability-agentic-harness/vvaharness/scope/walk.py#L57).

**VulnHunter says:** exclude build/configuration scripts, explicitly including Dockerfile, Makefile, package manifests, and continuous integration configuration. Its separate exception restores security-relevant infrastructure configuration. Evidence: [build-file exclusion](../VulnHunter/vulnhunt/SKILL.md#L89); [security infrastructure exception](../VulnHunter/vulnhunt/SKILL.md#L91).

**Same case:** a Makefile target consumes a lower-trust job parameter, and the file does not fall within the named infrastructure exception.

**Opposing action:** retain the artifact for possible threat analysis versus exclude it by the operating rule. Visa's verifier separately recognizes lower-trust job parameters as a possible trust-boundary crossing: [job-parameter trust boundary](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s6/prompts.py#L37).

**Boundary:** retained does not mean investigated or confirmed; local profile exclusions can change the Visa file inventory. The claim is a default scope conflict with explicit exceptions, not universal inclusion in every run.

## 3. Fixed-origin request paths: refute request forgery versus include in the combined hunt category

**Classification: direct classification opposition, not necessarily opposite final reporting.**

**Visa Vulnerability Agentic Harness says:** server-side request forgery requires control of host or scheme; path-only influence is excluded by the verifier. Its dedicated playbook explicitly routes fixed-origin path or query manipulation to another class. Evidence: [path-only exclusion](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s6/prompts.py#L56); [fixed-origin refutation](../visa-vulnerability-agentic-harness/vvaharness/skills/ssrf/SKILL.md#L75).

**VulnHunter says:** reconnaissance must inventory URL concatenation as request-forgery/path-traversal sinks even when the base address is hardcoded. The injection playbook combines request forgery and URL path injection in one class heading. Evidence: [fixed-base sink inclusion](../VulnHunter/vulnhunt/phases/phase1_recon.md#L47); [combined hunt category](../VulnHunter/vulnhunt/phases/phase2_class_inj.md#L58).

**Same case:** a request to a pinned origin allows `../` to select a different backend route, but input cannot alter host, port, or scheme.

**Opposing action:** refuse the server-side request forgery classification versus include the flow in VulnHunter's combined request-forgery/path-manipulation hunt category.

**Boundary:** Visa can still report a valid path or parameter injection weakness. VulnHunter's combined wording does not prove it will assign the request-forgery weakness identifier in the final report. The conflict is classification and investigation routing.

## 4. Browser-only asset traversal: excluded server-side class versus explicit class example

**Classification: conditional inclusion-versus-exclusion conflict.**

**Visa Vulnerability Agentic Harness says:** server-side bug classes, including path traversal and request forgery, raised against pure browser code belong to the wrong layer and should not be reported under those classes. Evidence: [browser-layer exclusion](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s6/prompts.py#L50).

**VulnHunter says:** include client-side configuration/asset traversal in single-page applications, with user input changing the configuration file fetched. Evidence: [browser asset-traversal inclusion](../VulnHunter/vulnhunt/phases/phase2_class_inj.md#L56).

**Same case:** browser code interpolates an attacker-controlled value into a configuration asset URL, allowing a different asset to load; no server-side filesystem boundary is crossed.

**Opposing action:** exclude a server-side path-traversal claim on that code versus investigate the pattern under the injection playbook's path-traversal example.

**Boundary:** this does not mean Visa ignores browser security generally or that VulnHunter confirms every changed asset as exploitable. A distinct browser data exposure or script-execution consequence may be classified differently.

## 5. Cloud object keys: reject filesystem semantics versus apply traversal wording

**Classification: conditional semantic conflict.**

**Visa Vulnerability Agentic Harness says:** exclude `../` in object-store keys when the key space is flat and no filesystem boundary is crossed. Evidence: [flat-key exclusion](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s6/prompts.py#L54).

**VulnHunter says:** include network filesystem and cloud-storage clients as equivalent sinks, with traversal applying identically across network boundaries. Evidence: [cloud-client sink inclusion](../VulnHunter/vulnhunt/phases/phase2_class_inj.md#L12); [network traversal equivalence](../VulnHunter/vulnhunt/phases/phase2_class_inj.md#L13).

**Same case:** an object-store operation treats `folder/../secret` as a literal flat key; no intermediary normalizes it and no authorization boundary is bypassed.

**Opposing action:** Visa's explicit semantic exclusion rejects traversal on that basis; VulnHunter's broad sink wording directs the investigator toward a traversal check for the cloud client.

**Boundary:** this is a conflict in the breadth of class guidance, not proof that VulnHunter's later gates accept a nonexistent traversal. If a wrapper normalizes keys or a backend implements hierarchical paths, the flat-key premise fails and the conflict may disappear.

## 6. An exported function without local callers: library entry point versus dead-code elimination

**Classification: conditional reachability conflict.**

**Visa Vulnerability Agentic Harness says:** the request-forgery playbook explicitly recognizes an exported fetch helper without a caller in the repository as a library entry point, separately reportable when appropriate. Evidence: [exported library entry point](../visa-vulnerability-agentic-harness/vvaharness/skills/ssrf/SKILL.md#L85).

**VulnHunter says:** if its production-usage search finds zero usages, record dead code and stop investigating the finding. Evidence: [zero-usage elimination](../VulnHunter/vulnhunt/phases/phase2_shared.md#L155).

**Same case:** a published library exports a URL-fetching function intended for downstream consumers, but the checkout contains no production call site.

**Opposing action:** allow external library entry-point reasoning versus eliminate on a zero-local-usage result.

**Boundary:** the Visa rule permits separate reporting or no report according to the remaining evidence; it does not guarantee confirmation. VulnHunter also has broader library-reachability guidance. The conflict is the explicit zero-usage stopping rule against an explicit external-entry exception, not a claim that every public export is exploitable.

## 7. Missing defense source: retain uncertainty versus assume ineffectiveness

**Classification: conditional evidence-policy conflict.**

**Visa Vulnerability Agentic Harness says:** return an inconclusive verifier result when evidence cannot be reached either way, including a needed file being unavailable or a path leaving the repository. Evidence: [inconclusive missing evidence](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s6/prompts.py#L91).

**VulnHunter says:** when a defense implementation is unavailable, treat the defense as ineffective and proceed with the finding intact. Evidence: [unavailable-defense rule](../VulnHunter/vulnhunt/phases/phase2_shared.md#L214).

**Same case:** exploitability depends on an external sanitizer whose implementation cannot be inspected and whose behavior is otherwise unknown.

**Opposing action:** retain an unresolved evidence state versus continue evaluation using an adverse assumption about the defense.

**Boundary:** proceeding past the sanitizer gate is not final confirmation; VulnHunter has further checks and named trust exceptions. Visa's inconclusive rule applies when the missing evidence prevents a judgment, rather than whenever any dependency source is absent. The conflict is the default treatment of decisive unknown evidence.

## 8. Different parameters at one sink: preserve separate findings versus deterministic proximity merge

**Classification: direct conditional decision conflict in consolidation.**

**VulnHunter says:** findings exploiting different user-controlled parameters remain separate even at the same endpoint. Evidence: [parameter-sensitive anti-merge rule](../VulnHunter/vulnhunt/phases/phase2b_verify.md#L270).

**Visa Vulnerability Agentic Harness does:** deterministic consolidation can merge findings when file, class or weakness, title overlap, and line proximity conditions match. The compared parameters are not an additional discriminator in that decision. Evidence: [deterministic merge procedure](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s7/collapse.py#L158); [title-overlap condition](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s7/collapse.py#L212); [merge decision](../visa-vulnerability-agentic-harness/vvaharness/pipeline/stages/s7/collapse.py#L217).

**Same case:** two verified injection findings concern two distinct parameters concatenated into the same query line, with matching weakness identifiers and sufficiently overlapping titles.

**Opposing action:** VulnHunter's parameter rule requires separate findings. Visa's deterministic rule can collapse them to a canonical finding because the specified merge conditions are satisfied.

**Boundary:** this compares two findings that already exist before consolidation; it does not assume both systems discover both. Duplicate-location retention can preserve some affected sites, but it does not preserve two canonical identities for the two exploited parameters. This difference is independent of optional semantic consolidation.
