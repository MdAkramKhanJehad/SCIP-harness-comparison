# Contradictions inside Visa Vulnerability Agentic Harness: conflicting rules, inactive controls, and implementation mismatches

## Introduction

This is the fourth file in the layered analysis. It examines only contradictions within Visa Vulnerability Agentic Harness (package `vvaharness`), following `BRIEF-low-level.md` and the finding structure used in file 03. It does not compare the two harnesses here.

The review read the original source on November 17, 2026, pairing instructions or configuration with their consumers. Pseudocode ambiguity notes and the knob inventory were leads, not proof. Every finding below has at least two exact source locations and quotations of at most twenty-five words. Paths are relative to `visa-vulnerability-agentic-harness/`; a source location confirms the cited text, not the frequency or runtime impact of the behavior.

The inspected areas were Stage 4 (deep investigation) prompt construction and evidence middleware; Stage 8 (chaining and ranking) recovery; Stage 10 (remediation) policy, playbook, prompts, and patch-content checks; Stage 11 (fix validation) rules, persona reports, synthesis, and scoring; and Semgrep enrichment and tools. Searches for allegedly unused controls covered the product Python and bundled configuration, with relevant prompt consumers read directly. Common Weakness Enumeration identifiers remain literal source identifiers. Ordinary concepts are written in full.

**Counts:** 25 findings: 7 high, 11 medium, 7 low. By primary kind: ambiguity with consequence 1, configuration against code 7, dead or unreachable rules 3, documentation against behaviour 4, prompt against code 8, prompt against prompt 2. Consequence levels describe the potential effect of the confirmed mismatch, not a measured vulnerability severity. Where model behavior or a final result is inferred, the consequence says so.

No harness source, pseudocode, configuration, or shared schema was changed. No scan, model session, remediation, or exploit was executed. Mechanical document checks verify citations, quotation locations, and structure; they do not prove end-to-end behavior. Optional exploit verification remains excluded.

---

### Finding 1: The playbook forbids automatic fixes for selected weakness classes, but the active eligibility policy allows them

- **Kind:** Configuration against code
- **Where:**
  - `inputs/remediation_playbook.yaml:51` — “never_autofix_cwes: # always route to human regardless of entry”
  - `inputs/remediation_policy.yaml:34` — “# default_action: allow → patch everything EXCEPT what the deny list blocks.”
  - `inputs/remediation_policy.yaml:49` — “deny: []”
  - `vvaharness/remediation_agent/policy/decide.py:44` — “decision = ctx.gate.decide(cwe, file_path)”
- **What conflicts:** The playbook declares an unconditional human-routing list for authentication, authorization, business logic, and cryptographic weakness classes. Eligibility is instead decided by the separate remediation policy, whose shipped default allows non-denied classes and has an empty deny list.
- **What actually happens:** The pre-gate reads the finding through `RemediationGate`, then resolves a playbook strategy only as supplementary context. A repository-wide search of the product finds no reader of `never_autofix_cwes`. Other path, content, and evidence checks remain active; they do not implement this class-wide prohibition.
- **Consequence:** A finding in a listed class can be offered to the patch agent despite the playbook saying it must always go to a human. Actual acceptance still depends on the remaining gates.
- **Consequence level:** high
- **Knobs involved:** `playbook.policy.never_autofix_cwes`, `step_remediate.enforce_policy`
- **Evidence strength:** verified in source

### Finding 2: A guidance-only password-hashing entry says not to patch, but a missing strategy does not stop the patch agent

- **Kind:** Configuration against code
- **Where:**
  - `inputs/remediation_playbook.yaml:392` — “confidence: guidance # migration needed → no auto-patch”
  - `inputs/remediation_playbook.yaml:396` — “pattern. Do not emit a code patch.”
  - `vvaharness/remediation_agent/policy/decide.py:48` — “# The playbook is SUPPLEMENTARY context, not a second gate — the policy gate alone owns allow/deny.”
  - `vvaharness/remediation_agent/plugin_runner/run.py:105` — “if pre is not None and not pre.allowed:”
- **What conflicts:** The weak-password-hashing entry explicitly requires migration guidance and no code patch. The execution gate tests policy permission, not the playbook confidence or the existence of a strategy.
- **What actually happens:** For the shipped guidance-only entry, strategy resolution has no strategy node to return. An allowed policy decision still reaches the engine, and `_build_user` falls back to the generic fix prompt when `pre.strategy` is absent. The entry’s explanatory notes are not automatically substituted for that fix request.
- **Consequence:** The migration-sensitive weakness can reach an autonomous fixer without the no-patch instruction that the playbook associates with it. Whether the model edits anything is not established by this reading.
- **Consequence level:** high
- **Knobs involved:** `step_remediate.enforce_policy`
- **Evidence strength:** verified in source

### Finding 3: The playbook promises patch-size rejection, but neither its line limit nor its file limit is consumed

- **Kind:** Configuration against code
- **Where:**
  - `inputs/remediation_playbook.yaml:40` — “max_diff_lines: 40 # reject any candidate larger than this”
  - `inputs/remediation_playbook.yaml:41` — “max_files_touched: 2”
  - `vvaharness/remediation_agent/playbook.py:88` — “def max_diff_lines(self) -> int:”
  - `vvaharness/remediation_agent/policy/postgate.py:155` — “unsafe_content = scan_added_lines(diff)”
- **What conflicts:** The global policy labels forty changed lines as a rejection limit and sets a two-file limit. The loader exposes both values as properties, but the remediation pipeline never reads those properties.
- **What actually happens:** The post-gate checks forbidden paths, workflow references, patch content, and the agent’s evidence gates. It does not compare the changed-line or touched-file count with these playbook values. Searching product code finds only the property definitions and their underlying key lookups.
- **Consequence:** Changing either value does not enforce the advertised patch-size boundary. A larger patch can pass the implemented checks, increasing the potential review burden; the frequency and security impact are unmeasured.
- **Consequence level:** high
- **Knobs involved:** `playbook.policy.max_diff_lines`, `playbook.policy.max_files_touched`
- **Evidence strength:** verified in source

### Finding 4: The required secret-externalization fix can be rejected as credential exfiltration by the content gate

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/remediation_agent/prompts.py:132` — “assignment with an environment-variable or secrets-manager read.”
  - `inputs/remediation_playbook.yaml:384` — “Replace the literal with a read from environment variable or”
  - `vvaharness/remediation_agent/policy/patch_content.py:108` — “"reads credentials or secret material into a new code path",”
  - `vvaharness/remediation_agent/policy/patch_content.py:116` — “r"(?i)\bos\.environ(?:\.get)?\s*[\[(]\s*['\"][^'\"\n]*"”
  - `vvaharness/remediation_agent/policy/postgate.py:156` — “bad = list(dict.fromkeys([*forbidden, *unsafe_refs, *unsafe_content]))”
- **What conflicts:** The remediation instructions require externalizing a hardcoded secret. The content scanner categorizes new `os.environ` reads of secret-bearing names as credential exfiltration without distinguishing a legitimate replacement read from an unrelated credential-harvesting path.
- **What actually happens:** An added Python assignment using `os.environ.get` with a name containing `API_KEY`, `TOKEN`, or `PASSWORD` matches that scanner rule. If the file is in the scanned executable-source scope, the post-gate adds it to the rejected paths and reverts it. This is conditional: alternative secret-loading expressions are not all matched.
- **Consequence:** A normal implementation of the prescribed fix can be undone by the security gate even when it contains no outbound transmission. This can prevent an otherwise appropriate hardcoded-credential remediation.
- **Consequence level:** high
- **Knobs involved:** `p.remediation_prompts.orch_root_cause_idioms`, `step_remediate.enforce_policy`
- **Evidence strength:** verified in source

### Finding 5: The patch-content scanner is described as fail-closed, but a parsing exception returns the same result as a clean patch

- **Kind:** Documentation against behaviour
- **Where:**
  - `vvaharness/remediation_agent/policy/patch_content.py:15` — “"""Fail-closed content scan of the lines an S10 patch ADDED (CWE-1427).”
  - `vvaharness/remediation_agent/policy/patch_content.py:250` — “except Exception: # noqa: BLE001 — a best-effort scan must never break a run”
  - `vvaharness/remediation_agent/policy/patch_content.py:245` — “not take down a run, but note that an empty result is also what a clean”
  - `vvaharness/remediation_agent/policy/postgate.py:159` — “if not bad:”
- **What conflicts:** The module introduces the scanner as fail-closed. The function explicitly catches a failure while extracting added lines and returns an empty issue map, which is also its clean-patch result.
- **What actually happens:** The post-gate uses that map together with independent path and workflow checks. If those checks also find nothing, the scanner failure does not independently force rejection. This conclusion concerns the exception branch; no claim is made that a normal generated diff triggers it.
- **Consequence:** A content-analysis failure can remove that particular safety check while the patch remains eligible for acceptance. Other gates still apply, but the claimed fail-closed behavior does not hold for this failure mode.
- **Consequence level:** high
- **Knobs involved:** `step_remediate.enforce_policy`
- **Evidence strength:** verified in source

### Finding 6: Missing credential-rotation attestation must cap a fix verdict, but host scoring discards that separate cap

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/validation/claude_config/rules/scoring-matrix.md:187` — “- Attestation missing -> verdict is capped at `Partially Fixed`. A `Fixed` base verdict downgrades to `Partially Fixed`; a `Partially Fixed` or `Not Fixed` base”
  - `vvaharness/validation/claude_config/rules/scoring-matrix.md:171` — “(Per "Code-level signals only" above, missing rotation attestation, missing monitoring, missing pre-commit hooks, and missing ADR docs do NOT downgrade these gates. Repository-history state does”
  - `vvaharness/validation/io/_host_score.py:130` — “"""Return the authoritative verdict: host numbers, agent narrative, never fix_status."""”
  - `vvaharness/validation/io/_host_score.py:142` — “scored = score_fix(list(gates), policy=policy)”
- **What conflicts:** The scoring matrix says missing rotation evidence must cap an otherwise fixed secret-exposure result at partially fixed, independently of the gate statuses. It also says missing attestation must not downgrade those gates. The authoritative host result is recomputed from the gates and does not accept the agent’s final status as authority.
- **What actually happens:** The host scorer has no rotation-attestation input or matching cap. If all four gates pass, its numerical decision can remain fully ready even when the agent narrative says attestation is missing. Recommendations and narrative are retained separately and do not change that computed decision. An explicit conditions list can still lower merge readiness, but it does not implement the missing-attestation cap on the decision itself.
- **Consequence:** The authoritative fix decision can be stronger than the secret-exposure policy permits. This is a source-derived execution-path finding, not an observed validation run.
- **Consequence level:** high
- **Knobs involved:** `p.scoring_matrix.rotation_cap_independent_of_gates`, `p.scoring_matrix.missing_rotation_does_not_downgrade_gates`
- **Evidence strength:** verified in source

### Finding 7: The validation skill requests a search for the leaked secret, while the validation rules forbid putting it in a query

- **Kind:** Prompt against prompt
- **Where:**
  - `vvaharness/validation/claude_config/skills/validation-scoring/SKILL.md:84` — “- Grep the leaked secret across the patched tree and report match count (not the secret value).”
  - `vvaharness/validation/claude_config/rules/scoring-matrix.md:154` — “Persisted remediation diffs are secret-redacted. Use their paths, hunk ranges, redaction markers, and non-sensitive replacement lines as change evidence; never reconstruct, persist, or place a”
  - `vvaharness/validation/claude_config/rules/adversarial-review.md:49` — “For hardcoded credential, API-key, token, password, private-key, connection-string, and OAuth-secret findings, the persisted diff is intentionally redacted. Never reconstruct the removed value or place it”
- **What conflicts:** The packaged validation skill tells the model to search for the leaked secret itself. The matrix and adversarial-review rules prohibit reconstructing that value or including it in a tool query, and instead prescribe safe location, name, and shape-based checks.
- **What actually happens:** These are different search procedures for the same credential-removal task. A session that receives both instructions cannot follow the literal-value search and the query prohibition simultaneously. The conflict is conditional on loading the skill; the rules are supplied through the configured validation rule path.
- **Consequence:** Following the skill can expose the removed value in a tool invocation; following the safer rule requires disregarding that skill instruction. No actual secret search or exposure was performed.
- **Consequence level:** high
- **Knobs involved:** `p.validation_system.never_echo_plaintext_secrets`
- **Evidence strength:** verified in source

### Finding 8: The default profile enables the evidence gate but disables the planning condition needed to construct it

- **Kind:** Configuration against code
- **Where:**
  - `vvaharness/config/profiles/default.yaml:223` — “evidence_gate: true”
  - `vvaharness/config/profiles/default.yaml:225` — “planning: false # true requires a write_todos plan first (deepagents only); costs a turn per session”
  - `vvaharness/pipeline/stages/s4/session.py:134` — “if not getattr(s4, "planning", True) or not getattr(s4, "evidence_gate", True):”
- **What conflicts:** The shipped default sets the evidence-gate switch to true, but the factory returns no gate whenever planning is false. The setting therefore does not independently enable the behavior its name suggests.
- **What actually happens:** In that profile, Stage 4 (deep investigation) constructs no instance of this plan-completion gate. The dependency is visible in code and related configuration commentary; it is not evidence that the later finding validators are absent.
- **Consequence:** An experiment that toggles only `step4.evidence_gate` while leaving planning disabled compares two inactive settings. Evidence quality cannot be attributed to that switch under these conditions.
- **Consequence level:** medium
- **Knobs involved:** `step4.evidence_gate`, `step4.planning`
- **Evidence strength:** verified in source

### Finding 9: The planning prompt says completion is the only way to report, but the gate eventually accepts an unfinished plan

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/pipeline/stages/s4/prompts.py:393` — “'in_progress is refused and handed back to you with the outstanding items named. Finishing '”
  - `vvaharness/backends/harness/deepagents/evidence_gate.py:88` — “"""Reject premature verdicts up to *max_rejections* times, then relent."""”
  - `vvaharness/backends/harness/deepagents/evidence_gate.py:146` — “if not self._claim():”
  - `vvaharness/backends/harness/deepagents/evidence_gate.py:46` — “f"shipped without that evidence. Count in {counter}_relented. Raise this stage's "”
- **What conflicts:** The model-facing planning instruction describes plan completion as a non-bypassable prerequisite. The implementation imposes a rejection allowance and then relents even if the outstanding work or required tool use remains unresolved.
- **What actually happens:** On the in-loop path, exhausting `_claim` causes the premature-response check to return no outstanding items, allowing the handler’s response through. A warning and counter record the relaxation. The documented implementation is recoverable degradation, whereas the prompt presents an absolute rule.
- **Consequence:** A result can be submitted without satisfying the advertised completion condition. The warning makes this visible, but does not make the prompt’s only-way assertion true.
- **Consequence level:** medium
- **Knobs involved:** `step4.evidence_gate_refusals`, `p.evidence_gate.max_rejections_default`
- **Evidence strength:** verified in source

### Finding 10: Deep-investigation prompts say every file is already inlined even when the loader deliberately supplies no source

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/pipeline/stages/s4/prompts.py:124` — “'The SOURCE CODE block in your first user message carries every file in FILES, whole. '”
  - `vvaharness/pipeline/stages/s4/prompts.py:440` — “_READ_COMPLETELY_CLAUSE,”
  - `vvaharness/pipeline/stages/s4/prompts.py:357` — “'them. Their source is already inlined below, so this costs you no tool calls; what it buys '”
  - `vvaharness/pipeline/stages/s4/session.py:180` — “if unit.size == UnitSize.LARGE or not getattr(s4, "inline_source", False):”
- **What conflicts:** The common system prompt says the full source is already present and restricts repeated reads. The planning prompt makes the same assumption. The loader supplies no source when inlining is disabled or when the investigation unit is large.
- **What actually happens:** The system-prompt builder includes the assertion regardless of source availability, and the planner has no inlining parameter. Other user-prompt sections can correctly say no source was inlined, leaving competing instructions in one session rather than resolving the system claim.
- **Consequence:** A model may avoid the initial source read because it was told the bytes were already present. That possible detection effect is inferred; the inconsistent prompt construction is directly verified.
- **Consequence level:** medium
- **Knobs involved:** `step4.inline_source`, `step4.planning`, `prompt.s4.read_completely`
- **Evidence strength:** verified in source

### Finding 11: The budgeted investigation prompt recommends shell execution even when shell capability is disabled

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/pipeline/stages/s4/prompts.py:215` — “'that whole weakness family across the tree in a single `execute`, and its empty sections are '”
  - `vvaharness/pipeline/stages/s4/prompts.py:307` — “return _budgeted_sweep(budget, inlined, graph)”
  - `vvaharness/pipeline/stages/s4/session.py:300` — “allow_shell=bool(getattr(s4, "bash", False)),”
  - `vvaharness/config/profiles/default.yaml:182` — “bash: false”
- **What conflicts:** The model-call-budget prompt recommends running a probe script through `execute` or using a shell grep command. That prompt has no shell-availability argument, while actual shell capability is controlled separately and is disabled in the shipped default.
- **What actually happens:** When a positive model-call budget selects this spend-plan text, it can name an unavailable execution route. The system prompt correctly gates its separate shell-duty section, but that does not remove the execution advice embedded in the budgeted user prompt.
- **Consequence:** A scarce investigation turn may be spent trying an unavailable operation or adapting an instruction to different tools. The prompt does not authorize actual shell access; the code still controls capability.
- **Consequence level:** medium
- **Knobs involved:** `step4.max_model_calls`, `step4.bash`
- **Evidence strength:** verified in source

### Finding 12: The scoring matrix permits a skipped root-cause gate, while the host treats that gate as mandatory for any conclusive verdict

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/validation/claude_config/rules/scoring-matrix.md:53` — “`no_new_vulnerabilities` is a **critical gate**: if its status is `skip` or `invalid`, the”
  - `vvaharness/validation/claude_config/rules/scoring-matrix.md:73` — “2. **Per-gate weighted score (evaluated gates only).** A `skip` gate is *unevaluated* — exclude it from BOTH numerator and denominator (weight-neutral). An `invalid` gate (any”
  - `vvaharness/validation/constants/scoring.py:43` — “_CRITICAL_GATES: Final[frozenset[str]] = frozenset({"no_new_vulnerabilities", "root_cause"})”
  - `vvaharness/validation/scoring/_engine.py:132` — “if criterion.name in config.critical_criteria and criterion.status in _UNEVALUATED:”
- **What conflicts:** The matrix names only the no-new-vulnerabilities gate as non-waivable and treats other skipped gates as weight-neutral. The host critical set includes both that gate and root cause.
- **What actually happens:** If root cause is skipped and the other gates pass, the prompt’s stated arithmetic has evaluated weight above one half and can produce a fixed status. The host instead returns inconclusive before scoring because root cause was not evaluated. This is the reachable mismatch; no claim depends on an unreachable below-floor case.
- **Consequence:** An agent-written score and the authoritative host status can disagree on the same gate set, with a stricter host outcome than the model was instructed to derive.
- **Consequence level:** medium
- **Knobs involved:** `p.scoring_matrix.critical_gate`, `code.validation.constants.scoring.critical_gates`
- **Evidence strength:** verified in source

### Finding 13: The prompt requires exactly three persona reports, but two agreeing reports can still produce host consensus

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/validation/prompts/system.md:105` — “missing, spawn it now before continuing; do not finish with fewer than 3.”
  - `vvaharness/validation/session/launcher.py:273` — “missing = sorted(set(FIX_VALIDATION.agent_names) - {r.persona for r in reports})”
  - `vvaharness/validation/session/launcher.py:277` — “if not reports:”
  - `vvaharness/validation/synthesis/_consensus.py:153` — “if len(top_statuses) == 1 and top_frequency >= MIN_CONSENSUS_VOTES:”
  - `vvaharness/validation/constants/synthesis.py:20` — “MIN_CONSENSUS_VOTES: int = 2”
- **What conflicts:** The orchestrator is told not to finish until it has reports from all three named personas. The host logs missing names but does not impose an all-three precondition before synthesis.
- **What actually happens:** If two distinct accepted reports agree on every required gate, the synthesis threshold can produce high-confidence statuses even with a missing third report. The no-reports branch is a refusal, but the two-reports case is not. The result is conditional on the other gate and scoring checks passing.
- **Consequence:** The validation panel can be narrower than the prompt’s mandatory review contract without automatically becoming inconclusive.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 14: The playbook calls its forbidden patterns hard rejections, but the post-gate never reads that list

- **Kind:** Configuration against code
- **Where:**
  - `inputs/remediation_playbook.yaml:44` — “forbid_patterns: # hard-reject if patch contains any of these”
  - `inputs/remediation_playbook.yaml:46` — “- "#\\s*nosec"”
  - `vvaharness/remediation_agent/playbook.py:84` — “self._policy = doc.get("policy") or {}”
  - `vvaharness/remediation_agent/policy/patch_content.py:31` — “_RULES: tuple[tuple[str, str, tuple[re.Pattern[str], ...]], ...] = (”
  - `vvaharness/remediation_agent/policy/patch_content.py:263` — “if (not text.strip() or _COMMENT_ONLY.match(text)”
- **What conflicts:** The playbook declares a configurable list of hard-rejected patch patterns, including suppression comments. The content gate uses its own fixed rules and deliberately skips comment-only additions.
- **What actually happens:** Product searches find no consumer of the playbook `forbid_patterns` list. Adding a suppression comment alone does not activate that content scanner because the line is skipped; independent forbidden-path and workflow checks can still reject the file for other reasons.
- **Consequence:** An operator cannot change content rejection by editing the advertised list, and at least the comment-suppression prohibition is not enforced by this gate.
- **Consequence level:** medium
- **Knobs involved:** `step_remediate.enforce_policy`
- **Evidence strength:** verified in source

### Finding 15: Semgrep coverage can say complete after findings, relationships, or paths were omitted

- **Kind:** Documentation against behaviour
- **Where:**
  - `vvaharness/plugins/semgrep/tools.py:108` — “A complete scan means no represented coverage loss;”
  - `vvaharness/plugins/semgrep/enricher.py:298` — “complete=not dropped and not error_count, findings=written, errors=error_count,”
  - `vvaharness/plugins/semgrep/enricher.py:257` — “if not isinstance(raw_path, str) or not isinstance(line, int):”
  - `vvaharness/plugins/semgrep/enricher.py:221` — “if len(self.edges) >= MAX_EDGES:”
- **What conflicts:** The tool description equates a complete scan with no represented coverage loss. The Boolean tests ranked-result truncation and reported errors, but not whether every retained row was inserted, whether every edge insertion succeeded, or whether the reported skipped-path count is nonzero.
- **What actually happens:** An unusable finding location can return false after ranking without changing `dropped`; exhausted edge insertion can return false without changing the coverage flag. Skipped paths are exposed as a separate count. The flag can therefore remain true under those conditions.
- **Consequence:** A consumer using the Boolean alone can overstate available evidence or coverage. This is a metadata-contract problem, not proof that an actual vulnerability was missed.
- **Consequence level:** medium
- **Knobs involved:** `code.plugins.semgrep.enricher.max_edges`
- **Evidence strength:** verified in source

### Finding 16: The Semgrep enricher promises never to raise, but graph-mutation construction is outside its protected report-reading block

- **Kind:** Documentation against behaviour
- **Where:**
  - `vvaharness/plugins/semgrep/enricher.py:322` — “"""The Semgrep subgraph, or a scan node saying why there is none; never raises."""”
  - `vvaharness/plugins/semgrep/enricher.py:332` — “return _mutation(project_id, context.graph, document, root)”
  - `vvaharness/plugins/semgrep/enricher.py:171` — “int((result.get("start") or {}).get("line") or 0),”
  - `vvaharness/plugins/semgrep/enricher.py:366` — “except Exception as exc:”
- **What conflicts:** The `enrich` contract promises graceful results rather than exceptions. Its broad exception handler belongs to report execution and reading, while ranking and mutation construction occur later outside that handler.
- **What actually happens:** For example, a truthy nonnumeric line value reaches an integer conversion in ranking and can raise. Graph-object construction may also raise. The method itself does not convert those failures to its degraded-coverage result; an outer caller might still handle them.
- **Consequence:** Plugin failure behavior is narrower than advertised and can interrupt enrichment rather than produce the promised explanatory coverage node. Whole-scan failure is not asserted without tracing the outer caller.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 17: Report-only command-line remediation is described as having no writer, but configured edit tools remain in its tool list

- **Kind:** Documentation against behaviour
- **Where:**
  - `vvaharness/remediation_agent/plugin_runner/__init__.py:429` — “# acceptEdits only where edits are wanted; report mode ships no writer at all.”
  - `vvaharness/remediation_agent/plugin_runner/__init__.py:402` — “tools = [t for t in _tools(cfg) if t != "Bash"]”
  - `vvaharness/remediation_agent/plugin_runner/helpers.py:33` — “return list(tools) if tools else list(_DEFAULT_TOOLS)”
  - `AGENTS.md:146` — “> report-only there keeps every listed tool. Report that to the user, and”
- **What conflicts:** The implementation comment says report mode ships no writer. The tool construction removes the shell but does not remove configured Write or Edit tools when the mode is report-only. The operating manual explicitly acknowledges that limitation.
- **What actually happens:** With a custom remediation tool list containing writers, the command-line session retains those names even though its prompt prohibits edits and its permission mode is more restrictive. This is a capability mismatch, not proof that such an edit is automatically approved or persists after outer guards.
- **Consequence:** The mode label alone does not establish absence of write capability. The operator must apply the manual’s route-specific tool restriction, contrary to the local no-writer comment.
- **Consequence level:** medium
- **Knobs involved:** `step_remediate.allowed_tools`
- **Evidence strength:** verified in source

### Finding 18: No framework priority is defined when a repository matches several playbook strategies, so set iteration chooses the required fix

- **Kind:** Ambiguity with consequence
- **Where:**
  - `vvaharness/remediation_agent/frameworks.py:72` — “found: set[str] = set()”
  - `vvaharness/remediation_agent/playbook.py:113` — “for fw in frameworks or set():”
  - `inputs/remediation_playbook.yaml:223` — “name: autoescape-on”
  - `inputs/remediation_playbook.yaml:230` — “name: jinja-escape”
- **What conflicts:** The playbook supplies distinct framework-specific strategies, but neither the policy nor the resolver defines a tie rule when several detected frameworks have a matching strategy for the same language and weakness. Framework detection is repository-wide rather than tied to the affected file.
- **What actually happens:** For a repository containing both Django and Flask, the resolver selects the first matching member of a set and stops. Set iteration is not a declared framework precedence or evidence that the affected file uses the chosen framework. The selected strategy is then presented to the fixer as required.
- **Consequence:** The same finding can receive a strategy for the wrong sub-application, and selection may vary across processes. The frequency and final patch effects are unmeasured; the undefined selection priority and first-match implementation are confirmed.
- **Consequence level:** medium
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 19: The playbook requests three competing patch candidates, but the runtime performs one fixer attempt with only a narrow error retry

- **Kind:** Configuration against code
- **Where:**
  - `inputs/remediation_playbook.yaml:43` — “candidates_per_finding: 3 # N patches generated, validation picks winner”
  - `vvaharness/remediation_agent/prompts.py:155` — “status `tool_error` with `retryable=true`. Never retry `not_applied` or”
  - `vvaharness/remediation_agent/prompts.py:156` — “`already_applied`, and never dispatch a second fixer after `applied`.”
  - `vvaharness/remediation_agent/playbook.py:84` — “self._policy = doc.get("policy") or {}”
- **What conflicts:** The global policy describes generating three patches and letting validation select a winner. The active orchestration prompt allows one applied fixer result and only one retry of a retryable tool error.
- **What actually happens:** No product reader consumes `candidates_per_finding`, and the active flow has no candidate-ranking loop for alternative fixes to the same finding. Error recovery is not generation of three competing patches.
- **Consequence:** The advertised selection procedure is absent and changing the value does not alter it. Broader effects on patch quality are not measured.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 20: The playbook contains a patch prompt template, but the runtime builds a different prompt and never renders that template

- **Kind:** Dead or unreachable rules
- **Where:**
  - `inputs/remediation_playbook.yaml:415` — “prompt_template: |”
  - `inputs/remediation_playbook.yaml:435` — “- Touch the fewest lines possible (hard limit: {max_diff_lines}).”
  - `vvaharness/remediation_agent/playbook.py:83` — “self._cwe = doc.get("cwe") or {}”
  - `vvaharness/remediation_agent/prompts.py:187` — “def build_user(target: RemediationTarget, repo: str, mode: str = "fix", *,”
- **What conflicts:** The shipped playbook includes a complete patch-generation template with vulnerability fields and a hard line limit. Its loader retains only the weakness entries and policy map, and the runtime constructs the user prompt in Python.
- **What actually happens:** Product code has no reader or renderer for the YAML `prompt_template` field. The active prompt injects the resolved strategy through `as_prompt_block` rather than formatting the full template.
- **Consequence:** Editing this template changes no executed prompt. None observable for detection; configuration maintenance and remediation interventions can target inactive text.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 21: Stage 8 exposes a resume timeout even though its deadline handler always replays instead of resuming

- **Kind:** Dead or unreachable rules
- **Where:**
  - `vvaharness/config/__init__.py:588` — “"resume_timeout": 300,”
  - `vvaharness/config/__init__.py:586` — “# Registered for parity with step2/4/6; s8 never resumes (see”
  - `vvaharness/pipeline/stages/s8/session.py:176` — “# re-run, not a continuation. Go straight to the transcript re-ask instead.”
  - `vvaharness/pipeline/stages/s8/session.py:180` — “return _replay_leg(user, ctx, cfg, transcript)”
- **What conflicts:** The configuration exposes a Stage 8 (chaining and ranking) resume timeout alongside active clocks. The implementation and its own nearby comment state that this one-call stage never resumes.
- **What actually happens:** The deadline branch calls the replay path, which reads the replay timeout. The resume-timeout value can appear in configuration and manifest metadata, but there is no behavioral reader for it on this stage.
- **Consequence:** Tuning this value cannot change recovery timing. None observable for detection from changing this control alone; the issue is an inert intervention surface rather than an unhandled deadline.
- **Consequence level:** low
- **Knobs involved:** `step8.resume_timeout`
- **Evidence strength:** verified in source

### Finding 22: Clock-saving and no-narration prompt rules are defined but never included in any registered backend profile

- **Kind:** Dead or unreachable rules
- **Where:**
  - `vvaharness/backends/harness/deepagents/profiles.py:58` — “_BEAT_THE_CLOCK = """\”
  - `vvaharness/backends/harness/deepagents/profiles.py:65` — “_DO_NOT_NARRATE = """\”
  - `vvaharness/backends/harness/deepagents/profiles.py:74` — “_REFLECT_IN_WRITING,”
  - `vvaharness/backends/harness/deepagents/profiles.py:110` — “profile = HarnessProfile(system_prompt_suffix=_INVESTIGATION_FLOOR)”
- **What conflicts:** The module defines instructions against narration and against writing intermediate reflections to save the deadline. The installed investigation-floor profile instead includes written reflection, and neither no-narration constant participates in the registered composition.
- **What actually happens:** The per-model and per-stage override dictionaries are empty, and searches find no use of these two constants outside their definitions. They are not simultaneously contradictory live instructions; the dead-rule contradiction is treating the available-looking fragments as active backend policy.
- **Consequence:** Editing either unused fragment does not change the registered model prompt. None observable for detection; intended cost or latency interventions can be ineffective.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 23: Semgrep tools declare row and trace limits as constants, but the queries use independent hard-coded limits

- **Kind:** Configuration against code
- **Where:**
  - `vvaharness/plugins/semgrep/tools.py:22` — “_MAX_ROWS = 25”
  - `vvaharness/plugins/semgrep/tools.py:23` — “_MAX_TRACE_STEPS = 40”
  - `vvaharness/plugins/semgrep/tools.py:32` — “LIMIT 25”
  - `vvaharness/plugins/semgrep/tools.py:41` — “LIMIT 40”
- **What conflicts:** The module declares two values that appear to control result limits. Its query text embeds separate numeric limits and does not interpolate or otherwise read those constants.
- **What actually happens:** Current numbers agree, so no present default mismatch is claimed. Editing the apparent constants alone leaves query behavior unchanged; editing the query text changes the effective limit.
- **Consequence:** An intervention on the named constants has no effect on context volume or query cost. This is an inert control definition, not evidence that the current numeric bounds are wrong.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

### Finding 24: The scoring matrix rounds every gate before summing, while the host rounds only the final normalized score

- **Kind:** Prompt against code
- **Where:**
  - `vvaharness/validation/claude_config/rules/scoring-matrix.md:73` — “Round each to 4 decimal places”
  - `vvaharness/validation/scoring/_engine.py:113` — “earned += config.weights[criterion.name] * config.status_multiplier.get(”
  - `vvaharness/validation/scoring/_engine.py:119` — “return round(min(earned / active_weight, 1.0), SCORE_PRECISION)”
- **What conflicts:** The written exact algorithm instructs per-gate rounding before summation. The host accumulates unrounded weighted products and rounds only after division.
- **What actually happens:** With the bundled weights and multipliers root cause fail, instance coverage fail, no-new-vulnerabilities partial, and security best practices pass, final-only arithmetic gives 0.2299 while per-gate four-place rounding can give 0.2300. This example follows the expressions without running the product.
- **Consequence:** The displayed arithmetic can differ from the authoritative score. No decision-threshold crossing is established for the bundled gate combinations, so the confirmed consequence is numeric and reporting inconsistency.
- **Consequence level:** low
- **Knobs involved:** `p.scoring_matrix.weight_root_cause`
- **Evidence strength:** verified in source

### Finding 25: The scoring matrix tells the agent to transition a ticket, while the system prompt says it has no ticket tools and the host owns transitions

- **Kind:** Prompt against prompt
- **Where:**
  - `vvaharness/validation/claude_config/rules/scoring-matrix.md:116` — “After scoring, the agent transitions the JIRA ticket:”
  - `vvaharness/validation/prompts/system.md:154` — “- No JIRA calls — the host posts results after you exit.”
  - `vvaharness/validation/prompts/system.md:148` — “- `target_jira_status` — observability only; the host derives the real transition”
- **What conflicts:** The matrix assigns ticket transitions to the agent after scoring. The orchestrator system prompt prohibits those calls, provides no ticket tool, and makes the model’s target-status field observational only.
- **What actually happens:** The model cannot perform the matrix’s transition action through its granted interface. In this repository’s scan validation path, the result is a local validation artifact; the ticket-oriented wording reflects a different integration contract rather than an available capability.
- **Consequence:** None observable for vulnerability detection. The conflicting responsibility can produce misleading expectations about external ticket updates, and any attempt to obey it would be outside the described tool set.
- **Consequence level:** low
- **Knobs involved:** none
- **Evidence strength:** verified in source

---

## Candidates not confirmed

- **The missing one-half coverage floor creates an accepted low-coverage verdict.** The engine lacks that explicit check, but its two non-skippable critical gates have combined weight 0.6167. Under the bundled policy, a conclusive below-0.50 evaluated-weight case is already blocked. The missing check is not counted as an independently reachable failure.
- **Built-in defaults and shipped profiles disagree.** Configuration explicitly defines profile values as overriding built-in defaults. Different confidence floors or batch sizes are not contradictions without a conflicting effective-default claim.
- **Stage 4 never uses the repeat guard or `ForceVerdictOnly`.** Their absence from one call site is not a promise they must be active there. Other budgets and backend-specific middleware govern this route, so no independent required-versus-actual contradiction was established.
- **Written reflection and no-narration instructions both reach the same registered profile.** The no-narration fragment is unused. The confirmed finding is dead prompt text, not a simultaneous pair of live instructions.
- **The playbook global new-dependency flag is unenforced independently of every strategy.** The global field has no reader, but per-strategy dependency lists are passed into active prompts. A distinct same-case mismatch beyond that separate mechanism was not established confidently enough to add another finding.
- **A two-to-one persona split always violates conservative synthesis.** The rules give majority agreement its own branch. Reading conservative disagreement as overriding an explicit majority would ignore that precedence; no blanket contradiction is counted.
- **Validation fact tools ignoring custom scan exclusions always contradicts a declared scope contract.** The tools explicitly reuse the built-in production scope. Custom exclusions are not passed through, but that alone does not establish a promised identity with every scan-specific overlay.
- **A turn limit is broken because DeepAgents adds recursion headroom.** The shipped profiles and backend constants explicitly document the backend-dependent meaning. Without an independent uniform-cap promise, this is a documented semantic difference rather than a new contradiction.
- **Direct software development kit spending limits are silently guaranteed.** The implementation explicitly warns that the accepted parameter is not enforced on that route. An unqualified contrary guarantee was not established for the same route.
- **The secret-rotation cap is enforced through lower gate scores.** The matrix explicitly prohibits downgrading gates for missing attestation. That does not resolve the confirmed host-recomputation mismatch; it is why the separate cap matters.
- **The rules say to use a single persona’s assessment, but host scoring rejects its flagged confidence.** Using a status during synthesis does not promise that its flagged confidence is sufficient for a conclusive score. The two steps can be followed together.
- **Every gate is required to cite evidence, but the scoring matrix makes evidence optional and illustrates passing gates with empty evidence.** The evidence array is optional, but a source citation can be supplied in summary or details. Empty structured evidence alone does not prove violation of the separate citation duty.
- **The matrix tells the orchestrator to calculate scores while the host-synthesis instruction explicitly forbids that calculation.** The backend-specific synthesis boundary explicitly assigns scoring to the host. It can be read as a specific override of the general matrix rather than an unresolved requirement to do both.

Not checked exhaustively: every language-specific detection playbook, vendor graph-extraction internals, all external backend-library semantics, all packaging variants, and every configuration key. Earlier scratch research notes outside this repository were not needed for the confirmed findings. The optional exploit verification implementation was not inspected. These limits mean this is a source-backed sample, not an exhaustive proof that no other contradictions exist.
