# Low-level contradictions between Visa Vulnerability Agentic Harness and VulnHunter

This document compares specific decision rules **between** the two harnesses. It does not add internal contradictions to files 03 or 04. Each finding holds a concrete case constant and identifies incompatible instructions or classification conditions: whether to investigate, retain, report, consolidate, or accept a fix. A contradiction here means the two policies prescribe different treatment of that case; it does not establish which policy is correct.

The analysis contains **11 findings: 5 high-consequence and 6 medium-consequence**. Seven compare model-facing rules, two compare executable consolidation rules with model-facing rules, and two compare fix-classification criteria. Consequence levels describe the likely effect on a harness comparison, not the severity of a vulnerability.

The common pseudocode provides the decision points and source mappings. Every quoted rule below was reopened in the original local source. A rule represented by a `Theta` lookup requires its underlying prompt or configuration value; the lookup alone does not prove the rule’s meaning. The evidence concerns the current local files, read on 17 November 2026. No historical commit identity is inferred from earlier analysis documents.

Source citations are relative to the repository named on each evidence line: `visa-vulnerability-agentic-harness/` or `VulnHunter/`. Exact source identifiers are preserved; ordinary terminology is written in full. Common Weakness Enumeration identifiers appear as literals such as `CWE-295`.

## Comparison at a glance

| Finding | Shared decision | Visa Vulnerability Agentic Harness | VulnHunter |
|---|---|---|---|
| 1 | Necessary downstream evidence is unavailable | Leave undetermined | Retain unsanitized backend propagation; high-severity floor when service credentials apply |
| 2 | A necessary defense cannot be inspected | Leave undetermined when it prevents a verdict | Treat the defense as ineffective and continue |
| 3 | A fetch-shaped helper demonstrably performs no fetch | Skill accepts the fetch contract | Require a new attacker outcome |
| 4 | First-party source proves vulnerable dependency use | Exclude the dependency-version finding | Report the narrow call-site-proven case |
| 5 | Shipped image packaging exposes a secret or debugging | Inspect the Dockerfile case | Normally exclude Dockerfiles, with an infrastructure exception |
| 6 | A flat object key contains traversal characters | Reject the traversal framing | Include cloud storage in the traversal sink reference; later impact gate can reject |
| 7 | Human-readable logs can be forged without a parser | Exclude the log-forging claim | Allow misleading records as a low-severity outcome |
| 8 | Two parameters independently exploit one identical sink span | Deterministic consolidation can merge | Keep separate findings |
| 9 | A service lacks authentication across its protected handlers | Preserve incompatible weakness families | Replace specified candidates with one platform finding |
| 10 | Certificate verification is repaired without application key changes | Complete if the case-specific criteria pass | Require the cryptography trust-chain fields for a full fix |
| 11 | A checked batch-size limit completely closes the identified resource weakness | Complete if the case-specific criteria pass | A matching length-check pattern produces mitigation |

## Findings

### Finding 1: Unavailable downstream code leaves Visa unable to confirm the impact, while VulnHunter treats unsanitized backend propagation as a finding

- **Kind:** Prompt rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:91` — “you could not reach the evidence either way”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:92` — “unavailable, or the path leaves the repository.”
  - **VulnHunter:** `vulnhunt/phases/phase2_class_inj.md:158` — “data crossing a tier boundary is a confirmed finding”
  - **VulnHunter:** `vulnhunt/phases/phase2_class_inj.md:164` — “Confirmed injection reaching a backend system with service credentials: **High**”
  - **VulnHunter:** `vulnhunt/phases/phase2_class_inj.md:168` — “behavior with injected parameters is unknown and must be assumed hostile.”
- **Same case:** A reachable handler interpolates an attacker-controlled query fragment into a service-authenticated downstream request. The local source establishes propagation, but the downstream implementation is absent and is necessary to establish whether the fragment changes authorization or query semantics. No independent local consequence has been demonstrated.
- **What conflicts:** Visa requires an undetermined verdict when necessary evidence is unavailable or the path leaves the repository. VulnHunter explicitly treats unsanitized propagation across this boundary as a finding, requires source evidence to downgrade it, and applies a high-severity floor to confirmed injection using service credentials. The conflict is whether crossing the boundary supplies the missing impact evidence.
- **What actually happens:** At Visa Stage 6 (adversarial source verification), the stated rule returns `INCONCLUSIVE` and keeps the claim visible as undetermined. In VulnHunter’s injection investigation, the stated rule retains a `CANDIDATE` and calls the boundary crossing confirmed. Later VulnHunter verification and reproduction still apply; this is not evidence that every retained candidate reaches the final report.
- **Consequence:** A comparison can count an undetermined claim on one side and a high-severity candidate on the other without either harness having more downstream source. Preserve the distinction between propagation evidence and demonstrated impact when comparing their findings.
- **Consequence level:** high
- **Controls involved:** Visa `p.s6_prompts.verdict_inconclusive`; VulnHunter `p.phase2_class_inj.gate3_keep_unsanitized_value_crossing_tier` and `p.phase2_class_inj.severity_floor_backend_injection`
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 2: An unreadable defense creates uncertainty for Visa, but VulnHunter explicitly treats that defense as ineffective

- **Kind:** Prompt rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:86` — “no control fully closes the path.”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:92` — “unavailable, or the path leaves the repository.”
  - **VulnHunter:** `vulnhunt/phases/phase2_shared.md:214` — “If the source is unavailable, **treat the defense as ineffective**”
  - **VulnHunter:** `vulnhunt/phases/phase2_class_inj.md:135` — “**(c) If you cannot read the source or construct a test**”
- **Same case:** A local handler calls a proprietary sanitizer before a local dangerous interpreter. Its implementation is unavailable, no applicable framework guarantee establishes its behavior, and no source reading or constructed test settles whether it blocks the payload. The attacker origin and dangerous sink are otherwise known.
- **What conflicts:** Visa’s confirmation requires a path not fully closed by a control, and its unavailable-evidence rule provides an undetermined outcome. VulnHunter instead gives an explicit default for this missing evidence: treat the defense as ineffective and continue with the claim intact. Unknown effectiveness is therefore uncertainty in one rule and absence of effective protection in the other.
- **What actually happens:** The Visa rule supports `INCONCLUSIVE` when this missing file prevents establishing the verdict. VulnHunter’s shared defense gate and its injection-specific fallback both continue to the new-capability gate. They do not waive that later gate or guarantee eventual reporting.
- **Consequence:** The two harnesses can retain the same suspicious flow at different confidence levels. This case differs from Finding 1: the missing evidence concerns a control before a known sink, rather than the semantics of an unavailable downstream sink.
- **Consequence level:** high
- **Controls involved:** Visa `p.s6_prompts.verdict_inconclusive`; VulnHunter defense-source fallback in `phase2_shared.md` and sanitizer fallback in `phase2_class_inj.md`
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 3: Visa accepts a fetch contract even when the helper only returns an empty value, while VulnHunter requires a new attacker outcome

- **Kind:** Prompt rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/skills/ssrf/SKILL.md:29` — “even when its body is stubbed, vendored or unseen;”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/skills/ssrf/SKILL.md:51` — “where the helper module was nine lines of stubs returning empty literals”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/skills/ssrf/SKILL.md:53` — “Never refute on "the body makes no request", "the helper is a stub"”
  - **VulnHunter:** `vulnhunt/phases/phase2_shared.md:240` — “You must AFFIRMATIVELY demonstrate what new outcome the attacker achieves.”
  - **VulnHunter:** `vulnhunt/phases/phase2_shared.md:258` — “**Also eliminate** if the finding proves a mechanism but not an outcome”
- **Same case:** An exposed route passes a request-supplied address to `get_base64_image_blob`. The helper is available to read and returns an empty literal on every path, with no network operation, replacement mechanism, or later use capable of producing an attacker benefit.
- **What conflicts:** Visa’s request-forgery skill explicitly accepts a fetch-shaped contract even when the body is stubbed and forbids refuting for that reason. VulnHunter’s new-capability gate requires an affirmative outcome and eliminates mechanism-only claims. In this concrete case, naming a fetch operation does not establish that an operation occurs.
- **What actually happens:** Following the Visa skill produces or preserves a request-forgery candidate based on the contract. Following VulnHunter’s outcome gate supplies a reason to stop this claim because the executed helper cannot cause the alleged effect. This is a skill-level conflict: Visa’s later adversarial verifier can independently inspect reachability and impact. The finding does not assert that the final Visa report must contain the candidate.
- **Consequence:** The harnesses can disagree about whether a known non-operating helper is sufficient evidence to initiate or preserve a security finding. Keep this separate from genuinely opaque deployed implementations and from blind request forgery, where an actual network request occurs even without returning its body.
- **Consequence level:** high
- **Controls involved:** Visa request-forgery skill hard gate and opaque-helper exception; VulnHunter shared new-capability gate
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 4: Visa excludes vulnerable dependency versions from this scan, while VulnHunter reports them when the first-party call site proves the vulnerable path

- **Kind:** Prompt rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:59` — “- Vulnerable third-party library versions — covered by the SCA/dependency”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:60` — “pipeline, not this scan.”
  - **VulnHunter:** `vulnhunt/phases/phase4_report.md:180` — “first-party code clearly invokes the vulnerable API path with attacker-controlled”
  - **VulnHunter:** `vulnhunt/phases/phase4_report.md:181` — “input (provable from the first-party call site alone), report it as a finding”
- **Same case:** A first-party request handler invokes a known vulnerable library version with attacker-controlled input. The published vulnerability conditions are apparent from the first-party call site alone. The proposed finding concerns that dependency vulnerability, with no separate first-party implementation defect.
- **What conflicts:** Visa explicitly routes vulnerable third-party versions to a separate dependency pipeline. VulnHunter’s reporting rule makes a narrow exception to its dependency exclusion: report this case when first-party source alone establishes the vulnerable use. The condition that permits reporting in VulnHunter does not remove Visa’s stated exclusion.
- **What actually happens:** Visa’s adversarial source-verification exclusions say not to report this class in the scan. VulnHunter’s final-report instructions say to report the proven call-site case with the published vulnerability reference; cases requiring deep dependency-internal analysis become code-quality notes instead.
- **Consequence:** A missing dependency-related finding in Visa can be a deliberate division of responsibility rather than a detection failure. Compare first-party implementation defects separately from dependency-version exposure.
- **Consequence level:** high
- **Controls involved:** Visa `p.s6_prompts.exclusion_d_third_party_versions`; VulnHunter dependency-reporting exception in `phase4_report.md`
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 5: Visa investigates security defects in shipped Dockerfiles, while VulnHunter normally forbids auditing those files

- **Kind:** Prompt rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/scope/walk.py:57` — “# Dockerfile/Jenkinsfile/Makefile/*.tf and Helm YAML are KEPT; below is repo metadata only”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/skills/client-side/SKILL.md:66` — “**In the shipped-artifacts section**: a dev-server `CMD` ships hot reload and source maps”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/skills/client-side/SKILL.md:67` — “`COPY . .` with no `.dockerignore` entry sweeps in `.env`/`.git`”
  - **VulnHunter:** `vulnhunt/SKILL.md:85` — “never report findings in them, never trace data flows”
  - **VulnHunter:** `vulnhunt/SKILL.md:89` — “**Build/config scripts**: `Makefile`, `Dockerfile`, `*.gradle`, `pom.xml`,”
  - **VulnHunter:** `vulnhunt/SKILL.md:91` — “**Exception: security-relevant infrastructure config.**”
- **Same case:** The production image is built by a first-party `Dockerfile` that packages a secret-bearing file through `COPY . .`, or starts a development server that exposes debugging features. This case concerns image packaging or its startup command, rather than a reverse-proxy, transport-termination, header-forwarding, or similar application-security directive.
- **What conflicts:** Visa keeps Dockerfiles in its built-in file scope and gives concrete instructions to inspect these shipped-artifact defects. VulnHunter explicitly lists Dockerfiles among files that must not be reported, traced, or investigated. Its infrastructure exception means this is a qualified scope conflict, not a claim that it ignores all deployment configuration.
- **What actually happens:** The Visa scope rule permits discovery; it does not guarantee investigation or confirmation, and user exclusions can narrow it. When the client-side skill is used, it names these checks directly. VulnHunter’s general production-code rule excludes the packaging case unless the analyst interprets it as belonging to the infrastructure-security exception.
- **Consequence:** Image-packaging and development-server findings can disappear from one harness’s comparison set before equivalent source analysis begins. Record whether the infrastructure exception was applied; do not generalize this finding to checked-in reverse-proxy rules, which VulnHunter explicitly includes.
- **Consequence level:** high
- **Controls involved:** Visa built-in scope exclusions and client-side shipped-artifact rules; VulnHunter production-code scope and infrastructure exception
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 6: Visa rejects traversal claims on flat object-store keys, while VulnHunter includes cloud-storage paths in its traversal sink model

- **Kind:** Prompt rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:54` — “- "../" in object-store or blob keys where the key space is flat and no”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:55` — “filesystem boundary exists to cross.”
  - **VulnHunter:** `vulnhunt/phases/phase2_class_inj.md:11` — “filesystem clients** as equivalent sinks: SMB/CIFS, SFTP, FTP, NFS, cloud”
  - **VulnHunter:** `vulnhunt/phases/phase2_class_inj.md:12` — “storage clients where the key/path is user-controlled. Path traversal applies”
  - **VulnHunter:** `vulnhunt/phases/phase2_class_inj.md:13` — “identically via `../` or `..\` sequences across network boundaries.”
- **Same case:** An attacker-controlled string becomes an object-store key containing `../`. The service treats the entire string as a literal key: there is no normalization into another namespace, filesystem extraction, or other boundary-crossing behavior.
- **What conflicts:** Visa’s exclusion explicitly requires a filesystem boundary before this traversal claim is eligible. VulnHunter’s sink reference includes cloud-storage clients and says traversal applies identically across network boundaries, without the flat-key qualification. The conflict concerns the initial semantic model of the sink, not a proven difference in final reports.
- **What actually happens:** Visa has an explicit reason to reject the traversal framing. VulnHunter’s sink rule invites a traversal trace, but its separate new-capability gate can still eliminate the claim after the literal-key semantics are established. If a wrapper normalizes paths or the object is later extracted to disk, the stated shared case no longer applies.
- **Consequence:** The two rule sets allocate investigation effort differently and risk treating the same `../` string as different evidence. Do not count every object-store key candidate as a confirmed traversal vulnerability or confuse object-authorization failures with directory traversal.
- **Consequence level:** medium
- **Controls involved:** Visa `p.s6_prompts.exclusion_c_flat_object_keys`; VulnHunter network-filesystem and cloud-storage sink reference
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 7: Visa excludes log forging without a downstream parser, while VulnHunter allows misleading log entries as a low-severity finding

- **Kind:** Prompt rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:66` — “- Log injection / log forging with no downstream parser.”
  - **VulnHunter:** `vulnhunt/phases/phase2_shared.md:327` — “**Low** — Exploitation requires privileged position or yields minimal impact:”
  - **VulnHunter:** `vulnhunt/phases/phase2_shared.md:328` — “- Log injection (attacker can write misleading log entries)”
  - **VulnHunter:** `vulnhunt/phases/phase2_shared.md:318` — “- Audit trail manipulation (attacker can cover their tracks)”
- **Same case:** An exposed endpoint writes an attacker-controlled value to a plain-text audit log without escaping newlines. A payload forges a plausible second record and misleads a human reader. No downstream parser, secret disclosure, or code-execution consequence is present.
- **What conflicts:** Visa’s noise-floor exclusion rejects the log-forging claim because no downstream parser exists. VulnHunter’s low-severity examples expressly admit the ability to write misleading log entries; its impact examples also recognize audit-trail manipulation. Human deception supplies an outcome under that rule even though no parser consumes the log.
- **What actually happens:** Visa’s verification policy says not to report this framing. VulnHunter has a low-severity reporting basis if reachability, attacker control, lack of effective defenses, and the misleading-record outcome are actually shown. Its separate gates still reject harmless string changes that cannot mislead anybody.
- **Consequence:** The discrepancy can be a genuine reporting-policy difference rather than disagreement over whether newline injection works. Keep the parser requirement explicit, and do not transfer this exclusion to plaintext-secret logging, which is a different exposure.
- **Consequence level:** medium
- **Controls involved:** Visa `p.s6_prompts.exclusion_e_log_injection`; VulnHunter low-severity examples and audit-trail impact examples
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 8: Visa can merge two independently exploitable parameters at one sink, while VulnHunter requires a separate finding for each parameter

- **Kind:** Executable rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s7/collapse.py:186` — “if a.file != b.file:”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s7/collapse.py:212` — “if title_overlap(a, b) < min_title_overlap:”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s7/collapse.py:217` — “if close or overlap:”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s7/collapse.py:220` — “canonical_of[j] = i”
  - **VulnHunter:** `vulnhunt/phases/phase2b_verify.md:267` — “Do NOT merge, subsume, or consolidate findings that differ in”
  - **VulnHunter:** `vulnhunt/phases/phase2b_verify.md:270` — “operating on different parameters at the same endpoint are separate vulnerabilities”
- **Same case:** A handler builds one raw database query from two independently attacker-controlled parameters. Two already-supported findings have the same file, identical sink coordinates, injection class, Common Weakness Enumeration identifier, and title, but different exploited parameters and payloads. The platform-wide authentication exception does not apply.
- **What conflicts:** Visa’s deterministic duplicate check compares file, class or weakness family, title overlap, and coordinate distance or overlap. It has no condition requiring equality of the exploited parameter. VulnHunter’s anti-merge rule explicitly requires separate findings when that parameter differs, including at the same endpoint.
- **What actually happens:** At Visa Stage 7 (duplicate consolidation), this pair satisfies the deterministic merge predicate even with zero line tolerance because the spans overlap. It becomes one canonical finding; same-coordinate duplicate handling does not create two independently identified parameter findings. VulnHunter’s verification instructions require two verdict rows. Visa’s use of pre-anchor coordinates does not alter the case because those are stipulated equal too.
- **Consequence:** Finding counts and apparent coverage diverge although both harnesses found the same two input weaknesses. Compare the preserved source-to-sink and parameter combinations, not just canonical finding counts. This instantiates the broader consolidation contrast in file 02 with a specific executable predicate.
- **Consequence level:** medium
- **Controls involved:** Visa `step7_dedup.line_tolerance`, title-overlap constant, and `collapse_trivial`; VulnHunter `p.phase2b_verify.anti_merge_dimensions`
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 9: Visa preserves distinct authentication and object-authorization weaknesses, while VulnHunter can replace them with one platform authentication finding

- **Kind:** Executable rule against prompt rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s7/collapse.py:62` — “return key_a is None or key_a != key_b”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s7/collapse.py:199` — “if cwe_conflict(a, b):”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s7_dedup.py:102` — “if cwe_conflict(verified[g_idx], verified[root(g_canon)]):”
  - **VulnHunter:** `vulnhunt/phases/phase2b_verify.md:236` — “`VULN-PLATFORM-AUTHN` (High, CWE-306). Subsume CONFIRMED CWE ∈”
  - **VulnHunter:** `vulnhunt/phases/phase2b_verify.md:237` — “{287, 306, 441, 639, 862, 863, 915, 1390}.”
  - **VulnHunter:** `vulnhunt/phases/phase2b_verify.md:247` — “not surfaced as separate findings.”
- **Same case:** A service has protected-data handlers but no valid authentication code anywhere in their call chains. Its supported candidates include missing authentication (`CWE-306`), attacker-selected resource access (`CWE-639`), and mass assignment (`CWE-915`). Hold this candidate set constant before comparing consolidation.
- **What conflicts:** Visa’s consolidation rejects merges between different normalized weakness families. These three identifiers are not one of its equivalent-weakness clusters. VulnHunter’s universal authentication-gap rule explicitly subsumes all three when no in-scope handler has valid authentication, overriding its normal anti-merge rule.
- **What actually happens:** Visa’s deterministic pass keeps the differently classified candidates separate, and its semantic pass also checks the weakness conflict before accepting a merge. VulnHunter emits one high-severity platform authentication finding, marks the original rows as subsumed, and does not surface them as separate report findings. Its authentication-system exclusions and zero-handler exception must be checked before applying this rollup.
- **Consequence:** VulnHunter can have fewer report entries without having missed the underlying candidates. This differs from Finding 8: Visa merges while VulnHunter separates in that case; here their decisions reverse because VulnHunter applies a named platform exception.
- **Consequence level:** medium
- **Controls involved:** Visa `cwe_conflict` and `step7_dedup.semantic`; VulnHunter universal authentication-gap rollup and its anti-merge exception
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 10: Visa can accept restored certificate verification as a complete fix, while VulnHunter also requires cryptographic key and rotation evidence

- **Kind:** Fix-classification rule against fix-classification rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/remediation_agent/prompts.py:122` — “constant-time compare, TLS on, auth dependency, input allow-list).”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/validation/claude_config/rules/scoring-matrix.md:22` — “The applied diff modifies the vulnerable code path with proper mitigation”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/validation/claude_config/rules/scoring-matrix.md:48` — “| raw_score >= 0.80 | Fixed |”
  - **VulnHunter:** `vulnhunter-fix/prompts/worker_agent_crypto.md:1` — “# Worker Agent — Crypto (CWE-295/326/327/328/330/345/347)”
  - **VulnHunter:** `vulnhunter-fix/prompts/worker_agent_crypto.md:30` — “If any boolean is `false` (or missing), you MUST classify `MITIGATION`”
  - **VulnHunter:** `vulnhunter-fix/scripts/compute-completeness-tier.py:135` — “signals.append("mitigation.crypto_trust_chain_incomplete")”
- **Same case:** A `CWE-295` finding concerns an outbound request using disabled certificate verification. The patch restores the framework’s standard certificate verification and removes every bypass on the relevant paths. Assume the fix introduces no other defect and satisfies all four Visa validation criteria. The client has no application-level encryption key to source or rotate.
- **What conflicts:** Visa’s four-criterion validation can classify this root-cause fix as fixed; its rules do not add a universal cryptographic key-source or rotation prerequisite for certificate-verification findings. VulnHunter routes `CWE-295` to a cryptography worker that requires all four trust-chain booleans, including approved key source and rotation evidence, for a full fix. A missing or false value forces mitigation under that worker rule.
- **What actually happens:** For the stipulated all-passing criteria, Visa’s numerical scoring permits its fully ready outcome. In VulnHunter, false cryptographic trust-chain fields produce a mitigation signal in code as well as the worker instruction. The checker’s fields concern evidence it detects, not a proof that this particular certificate-verification repair needs an application key. This compares acceptance criteria, not identical words in the two verdict schemas.
- **Consequence:** One repaired defect can be accepted as complete under Visa’s case-specific criteria and retained as mitigation under VulnHunter’s class-wide prerequisites. Distinguish a residual attack path from a missing prerequisite that may not apply to the repaired operation.
- **Consequence level:** medium
- **Controls involved:** Visa validation criteria and thresholds; VulnHunter `crypto_trust_chain` booleans and cryptography worker completeness gate
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

### Finding 11: Visa can accept a complete resource-limit repair, while VulnHunter marks a matching length check as mitigation regardless of its purpose

- **Kind:** Fix-classification rule against fix-classification rule between harnesses
- **Where:**
  - **Visa Vulnerability Agentic Harness:** `vvaharness/pipeline/stages/s6/prompts.py:63` — “unbounded allocation from a single request).”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/validation/claude_config/rules/scoring-matrix.md:22` — “The applied diff modifies the vulnerable code path with proper mitigation”
  - **Visa Vulnerability Agentic Harness:** `vvaharness/validation/claude_config/rules/scoring-matrix.md:48` — “| raw_score >= 0.80 | Fixed |”
  - **VulnHunter:** `vulnhunter-fix/scripts/compute-completeness-tier.py:125` — “if re.search(r"if\s+len\(\w+\)\s*[<>]=?\s*\d+", added)”
  - **VulnHunter:** `vulnhunter-fix/scripts/compute-completeness-tier.py:126` — “signals.append("mitigation.length_or_complexity_cap")”
  - **VulnHunter:** `vulnhunter-fix/scripts/compute-completeness-tier.py:190` — “mitigation = _check_mitigation_signals(diff, plan)”
  - **VulnHunter:** `vulnhunter-fix/scripts/compute-completeness-tier.py:193` — “"tier": "MITIGATION",”
- **Same case:** A request can trigger excessive per-item work because the application lacks a batch-size bound. The patch adds `if len(items) > 100:` and rejects the request before that work. Assume the surrounding request-byte cap, all call paths, and the chosen bound have been checked, so the identified resource-exhaustion path is actually closed; all four Visa validation criteria pass.
- **What conflicts:** Visa’s validation criteria permit a proper root-cause mitigation to receive a fixed verdict when coverage and safety also pass. VulnHunter’s classifier assigns a mitigation signal whenever added code matches its literal length-check expression or a maximum-length pattern. That rule does not first ask whether the size bound is the complete intended repair for this weakness.
- **What actually happens:** The stipulated all-passing Visa gates permit a complete result. VulnHunter’s conservative classifier sees the added `if len(items) > 100:` and emits `mitigation.length_or_complexity_cap`; its classification walk considers mitigation signals before full-fix signals. This is a deterministic classification condition, not a claim that any arbitrary size limit is sufficient security remediation.
- **Consequence:** The same complete repair can receive different completeness labels because one rule evaluates the repaired vulnerability and the other classifies a syntactic patch pattern conservatively. In comparisons, record whether a lower completeness label represents a demonstrated remaining exploit or this generic pattern rule.
- **Consequence level:** medium
- **Controls involved:** Visa validation criteria and thresholds; VulnHunter `_check_mitigation_signals` and conservative classification order
- **Evidence strength:** verified in source for the rules and predicates; the comparative outcome is inferred from the stated case, not measured in a harness run.

## Pseudocode traceability

The following paired representations expose the principal rules used above. Paths are relative to `comparison-results/pseudocode/`. The original-source evidence controls whenever a rendered method, comment, or parameterized rule is less specific.

| Findings | Visa pseudocode | VulnHunter pseudocode |
|---|---|---|
| 1–2 | `vvah/vvaharness/pipeline/stages/s6/prompts.pseudo` | `vulnhunter/vulnhunt/phases/phase2_class_inj.pseudo`; `vulnhunter/vulnhunt/phases/phase2_shared.pseudo` |
| 3 | `vvah/vvaharness/skills/ssrf/SKILL.pseudo` | `vulnhunter/vulnhunt/phases/phase2_shared.pseudo` |
| 4 | `vvah/vvaharness/pipeline/stages/s6/prompts.pseudo` | `vulnhunter/vulnhunt/phases/phase4_report.pseudo` |
| 5 | `vvah/vvaharness/scope/walk.pseudo`; `vvah/vvaharness/skills/client-side/SKILL.pseudo` | `vulnhunter/vulnhunt/SKILL.pseudo` |
| 6–7 | `vvah/vvaharness/pipeline/stages/s6/prompts.pseudo` | `vulnhunter/vulnhunt/phases/phase2_class_inj.pseudo`; `vulnhunter/vulnhunt/phases/phase2_shared.pseudo` |
| 8–9 | `vvah/vvaharness/pipeline/stages/s7/collapse.pseudo`; `vvah/vvaharness/pipeline/stages/s7_dedup.pseudo` | `vulnhunter/vulnhunt/phases/phase2b_verify.pseudo` |
| 10–11 | `vvah/vvaharness/remediation_agent/prompts.pseudo`; `vvah/vvaharness/validation/claude_config/rules/scoring-matrix.pseudo` | `vulnhunter/vulnhunter-fix/prompts/worker_agent_crypto.pseudo`; `vulnhunter/vulnhunter-fix/scripts/compute-completeness-tier.pseudo` |

## Candidates not confirmed

These were checked and excluded from the finding count because the stated opposition is not established.

1. **Fixed-host path injection is not necessarily a request-forgery disagreement.** Visa rejects the request-forgery label when the attacker controls only the path, but explicitly permits another class for path or parameter injection. VulnHunter’s combined request-forgery and path-injection investigation does not require every such case to receive `CWE-918`. Source: Visa `vvaharness/skills/ssrf/SKILL.md:74`; VulnHunter `vulnhunt/phases/phase2_class_inj.md:58`.
2. **Discarding a fetched response does not establish opposite decisions about blind request forgery.** A real request can still create a network capability. A helper that performs no request, as in Finding 3, is a different case. Source: Visa `vvaharness/skills/ssrf/SKILL.md:62`; VulnHunter `vulnhunt/phases/phase2_shared.md:238`.
3. **Caller-chosen callback addresses are not automatically a conflict.** VulnHunter excludes intentional caller-serving features but preserves authorization-boundary exceptions. A demonstrated internal-network capability can satisfy both harnesses. Source: Visa `vvaharness/skills/ssrf/SKILL.md:24`; VulnHunter `vulnhunt/phases/phase2_shared.md:135`.
4. **Ordinary production-unreachable test code is excluded by both.** Visa’s skill discussion of seeded fixture data does not prove an opposite default scan scope; its walker also excludes test and fixture directories. Source: Visa `vvaharness/scope/walk.py:39`; VulnHunter `vulnhunt/SKILL.md:87`.
5. **A missing local call site is not sufficient to prove a cross-harness library-entry-point conflict.** Visa’s request-forgery skill permits an exported library entry point, while VulnHunter also says a library function is production code unless guarded. VulnHunter’s separate zero-usage instruction creates an internal tension, not an unqualified opposite cross-harness policy. Source: Visa `vvaharness/skills/ssrf/SKILL.md:85`; VulnHunter `vulnhunt/phases/phase2_shared.md:155` and `vulnhunt/phases/phase2_shared.md:164`.
6. **Resource-exhaustion reporting is not generally excluded by Visa.** Visa excludes pure volumetric or rate-limit denial of service but explicitly retains input-driven complexity and single-request allocation blowups, which VulnHunter also investigates. Finding 11 concerns repair classification, not opposite detection scope. Source: Visa `vvaharness/pipeline/stages/s6/prompts.py:61`; VulnHunter `vulnhunt/phases/phase2_class_log.md:100`.
7. **Public-key prefixes in browser code do not establish a conflict.** Visa explicitly refutes keys public by design; VulnHunter still requires a security outcome for a secret-exposure claim. Merely listing hardcoded keys as a search pattern does not order reporting every literal. Source: Visa `vvaharness/skills/client-side/SKILL.md:81`; VulnHunter `vulnhunt/phases/phase2_class_log.md:15` and `vulnhunt/phases/phase2_shared.md:238`.
8. **An informational delegated-authorization finding is not elimination.** VulnHunter explicitly continues to report these findings. Visa’s demand to examine object ownership does not, by itself, establish a contrary severity value for the same delegated flow. Source: Visa `vvaharness/skills/access-control/SKILL.md:29`; VulnHunter `vulnhunt/phases/phase2_shared.md:333` and `vulnhunt/phases/phase2b_verify.md:184`.
9. **Browser path changes alone do not establish opposite vulnerability verdicts.** Visa rejects server-side classes raised against pure browser code, and VulnHunter includes client-side asset traversal in its search reference. Without a demonstrated additional capability, VulnHunter’s outcome gate can reject the same claim. This is insufficient evidence for an unconditional report-versus-reject finding. Source: Visa `vvaharness/pipeline/stages/s6/prompts.py:50`; VulnHunter `vulnhunt/phases/phase2_class_inj.md:56` and `vulnhunt/phases/phase2_shared.md:238`.

## Interpretation and limits

The findings distinguish conflicting early rules from incompatible final consolidation predicates. Findings 3, 5, and 6 explicitly allow later verification or an exception to reconcile the results. Findings 8 and 9 show why report counts can move in opposite directions under different consolidation conditions. Findings 10 and 11 compare completeness requirements; `FULL`, `MITIGATION`, and Visa’s complete or partial decisions are not assumed to be identical schemas.

This is source-backed qualitative analysis of the common pseudocode representation, not an executed benchmark, measured false-positive rate, or proof of model compliance. It does not claim that every named skill is loaded in every Visa investigation or that every prompt directive is mechanically enforced. It does not analyze optional exploit verification. The source repositories, pseudocode, schema, and knob registries were not changed.
