# Prompt supply within the harness workflow

This view extends [the scan hierarchy](representation/harness.sudo.md). `Constraints`, `if`, `for each` and natural-language predicates are baseline SudoLang. Names retain their existing source meanings. Blocks labelled **host assembly** describe executable operations; blocks labelled **model request** describe requested compliance. Available tools and model choices remain distinct. Mirrored instruction views are in `prompt_representation/`; the per-source ledger is [prompt_content_coverage.tsv](prompt_content_coverage.tsv).

## Detection skill supply — host assembly

```sudo
// Source: vvaharness/skills/__init__.py:36-99
Constraints {
  skill_names discovers sorted directories containing SKILL.md.
  inject_skills takes the lock, caches by resolved repository root and tries to copy the packaged skills beneath .vvaharness/skills.
  if (the parent is a symlink or filesystem copying fails) { No usable injected skill root is promised. }
  The wrapper removes temporary copies in finally, including on failure or interruption.
  Supplying a skill root exposes files; it does not execute all skills or their probes.
}
```

The seventeen converted [detection skill views](prompt_representation/vvaharness/skills/) retain each lens's own gates, exceptions, procedures and completion rules. The crypto file open in the IDE now contains its actual conversion in [source_detail](source_detail/vvaharness/skills/crypto/SKILL.md.sudo.md). Requested use of a sibling sweep, probe, graph or helper is not a host assertion that it ran.

## S1 — optional scope-exclusion request

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
Constraints {
  The triage model is asked to exclude only non-production survey categories, preserve all NEVER EXCLUDE categories, retain uncertain cases and reply with one YAML fence.
  The actual overlay vetting, protected-file rescues, response quality floors and aggressive keep-ratio warning remain executable code, not guaranteed model compliance.
}
```

The [S1 instruction conversion](prompt_representation/vvaharness/pipeline/stages/s1_autoexclude.py.sudo.md) includes the survey message and all exceptions; [source detail](source_detail/vvaharness/pipeline/stages/s1_autoexclude.py.sudo.md) retains when this optional call is made and which returned exclusions are accepted.

## S2 — structural threat model

Host assembly:

```sudo
// Source: vvaharness/pipeline/stages/s2/session.py:130-217
Constraints {
  System text is assembled as SYSTEM, then read-only agentic guidance, then the selected graph guidance, then optional shell guidance.
  if (graph handle, graph_tools setting and route support admit graph tools) {
    The code registers graph tools and their budget.
    if (the graph is degenerate) { The graph guidance is omitted while tools remain registered. }
    Optional planning and finite evidence-gate middleware are composed by the cited branches.
  }
  Timeout recovery supplies the replay instruction and recorded transcript through resume_or_replay; finally releases the pinned session.
}
```

Model request: [S2 instructions](prompt_representation/vvaharness/pipeline/stages/s2/prompts.py.sudo.md) preserve the ordered context/assets/boundaries/STRIDE/questions procedure and inventory reconciliation. `_build_user_prompt` inserts the repository name, evidence, selected baseline, inventory, modules, entry points and optional context in its actual source branches; [_build_user_prompt detail](source_detail/vvaharness/pipeline/stages/s2/prompts.py.sudo.md) records exact slicing, joins and formatting. Planning, shell and graph guidance apply only when actually supplied. The prompt's snapshot-only role and later optional permission to read files are both retained.

## S4 — agentic detection inside investigation units

Host assembly and requests:

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:423-444
Constraints {
  The generated system text's instructions are model requests, including source-reading and output requirements.
  Caller-selected graph, plan, skill and budget clauses retain the original conditions in the companion executable representation.
}
```

The [full S4 content conversion](prompt_representation/vvaharness/pipeline/stages/s4/prompts.py.sudo.md) keeps the four breadth passes within the same agent, the optional budgeted sweep, per-unit bindings and the unconditional “already inlined” clause beside actual conditional source inclusion. [Session assembly](source_detail/vvaharness/pipeline/stages/s4/session.py.sudo.md), [finite evidence gate](representation/vvaharness/backends/harness/deepagents/evidence_gate.sudo.md), and [converted middleware notices](prompt_representation/vvaharness/backends/harness/deepagents/) remain separate. Requested evidence does not replace executable finite rejection/relent behavior. Configured tools remain available choices except for requirements explicitly requested or enforced by those separate layers.

## S6 — per-batch second opinion, with nested optional EV

Host assembly:

```sudo
// Source: vvaharness/pipeline/stages/s6/prompts.py:232-250
Constraints {
  build_system_prompt joins role, verdict, confidence and method clauses in source order.
  Graph duty is included only when graph is true; reframe duty only when reframe is true; trait duty only when trait_stamps is true.
  Corrections, repeats, extras, exclusions, CVSS duty and the example retain the displayed assembly order.
}
```

[Converted S6 instructions](prompt_representation/vvaharness/pipeline/stages/s6/prompts.py.sudo.md) retain the four review steps, three verdicts, actual-evidence requirement, configured-floor warning, ordinary corrections versus optional reframing, repeat/additional findings and all exclusion exceptions. Per-batch `items`, `ctx`, optional `code`, controls and ids are inserted by [build_verify_prompt and helpers](source_detail/vvaharness/pipeline/stages/s6/prompts.py.sudo.md); [session code](source_detail/vvaharness/pipeline/stages/s6/session.py.sudo.md) selects routes, tools, replay and repair. Schema descriptions in the [outcomes conversion](prompt_representation/vvaharness/pipeline/stages/s6/outcomes.py.sudo.md) also constrain the requested reply. The third-party-version exclusion is retained even though other stage/skill instructions mention vulnerable versions.

Nested EV host supply and model requests:

```sudo
// Source: vvaharness/exploit_verification/verify/prompt.py:82-87
Constraints {
  system_prompt appends the supplied auth_posture when present; an absent posture contributes no invented authentication fact.
}
// Source: vvaharness/exploit_verification/verify/judge.py:301-325
Constraints {
  The judge's finding fields, attacked endpoint, injection point and bounded code/claim text are serialized into the user message.
  if (tell is present) { Its re-redacted value is appended as a deterministic signal. }
  Real transcript response views follow; the static verdict is not included in this finding block.
}
```

[Probe instructions](prompt_representation/vvaharness/exploit_verification/verify/prompt.py.sudo.md) govern adaptive, minimally destructive endpoint-bound evidence gathering, allowed method choice, measured credential state and stopping. [Judge instructions](prompt_representation/vvaharness/exploit_verification/verify/judge.py.sudo.md) separately govern adjudication, benign readings, mechanism/property distinctions, second identity, comparison indexes, CVSS, ordered output fields and remediation re-checking. Exact assembly, marker/OOB/history conditions and limits remain in the [probe source view](source_detail/vvaharness/exploit_verification/verify/prompt.py.sudo.md) and [run source view](source_detail/vvaharness/exploit_verification/verify/run.py.sudo.md). Neither available HTTP tools nor requested continued adaptation implies a particular request was sent. Classifier and endpoint/finding mapper instructions are separately converted under `prompt_representation/vvaharness/exploit_verification/` and linked from their executable source views.

## S7 and S8 — collapse, then chain/rank

```sudo
// Source: vvaharness/pipeline/stages/s7/prompts.py:69-83
Constraints {
  build_payload assigns local indexes only to unresolved candidates, with source field limits and exact cwe/source/sink fields.
  The model is asked to apply the one-fix collapse criterion, CWE sibling exception, lower index and independent_sites contract; uncertainty requests keeping both.
}
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-89
Constraints {
  The S8 model is asked to accept supplied verified findings as ground truth and assess joint primitives rather than re-verify.
  Proposed feeds may lack evidence; proposed chains require evidenced links and capability-changing steps.
  Only feeds or actively changed severities request ranked_findings entries. Summary is requested last and may describe only listed chains.
}
```

Full instruction conversions: [S7](prompt_representation/vvaharness/pipeline/stages/s7/prompts.py.sudo.md), [S8](prompt_representation/vvaharness/pipeline/stages/s8/prompts.py.sudo.md). Source assembly preserves unresolved/global versus local indexing, exact field truncation, facts/graph context, optional hop text and repair calls. The dynamic values are identified at every converted f-string and remain executable expressions in the corresponding `source_detail/` view.

## S10 — remediation strategy, triage and optional fixer

Host assembly:

```sudo
// Source: vvaharness/remediation_agent/playbook.py:50-65
Constraints {
  Strategy.as_prompt_block inserts selected name, CWE/title, fix_location and instruction.
  if (example_after exists) { It appends that reference pattern. }
  It appends allowed_deps or (none), then the request to select THIS strategy without inventing another.
}
// Source: vvaharness/remediation_agent/playbook.py:78-139
Constraints {
  Loading records cwe and policy only; a load exception leaves guidance-only resolution.
  Resolution tries language or default, a framework from the supplied set, a language default/direct named node, then CWE fallback.
  Set iteration does not establish a deterministic precedence among multiple matching frameworks.
  The root YAML prompt_template is not consumed by this loader; converting its instructions does not make it active.
}
```

[Remediation prompt conversion](prompt_representation/vvaharness/remediation_agent/prompts.py.sudo.md) distinguishes single-agent three-gate triage/minimal fixes from parent planning and the fixer request. The fixer is asked to re-read current bytes and return already_applied/applied/not_applied/tool_error accurately; parent requests permit one retry only for retryable tool_error and prohibit re-fixing an applied result. Host edit permissions, postgates and actual retries remain [executable code](source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md). [Playbook guidance](prompt_representation/inputs/remediation_playbook.yaml.sudo.md) is converted per CWE/language/framework/fallback including examples, while inactive template text is explicitly conditional. Policy/configuration data is not recast as a model guarantee. Optional strategy/policy sections and rendered finding/triage/mode values retain their original assembly in `build_user` and `plugin_runner/helpers.py`.

## S11 — validation parent, persona requests, synthesis and scoring

Host assembly:

```sudo
// Source: vvaharness/validation/session/launcher.py:325-345
Constraints {
  Parent/session options supply tools, fact-tool specs, optional injected skill root and selected agents.
  load_agents receives configured names, model overrides, narrowed tools, persona call cap and a route-dependent prompt suffix.
  if (the route reads injected Claude configuration) { The persona suffix is SUBMIT_PROMPT_SUFFIX. }
  else { The persona suffix is persona_rules_text(). }
}
// Source: vvaharness/validation/subagents/_loader.py:89-120
Constraints {
  Bundled Markdown is read and frontmatter/body are parsed into SubagentDefinition.
  Requested names filter inclusion; model overrides replace matching models.
  Tool narrowing retains only tools already declared by a persona and either allowed by override or in FACT_TOOLS.
  A nonempty suffix is appended after the persona body; max_model_calls zero or None leaves it unmetered.
}
// Source: vvaharness/validation/session/launcher.py:348-409
Constraints {
  Route capabilities determine whether rules are referenced as injected configuration or inlined.
  if (the route returns schema-validated reports) { Appended synthesis instructions ask for reports and [], leaving synthesis/scoring to the host. }
  else { Appended instructions request gate synthesis; host code still recomputes scoring rather than trusting raw score/readiness/fix_result. }
  if (configured system prompt file is truthy and exists) { Its stripped text precedes synthesis instructions and rules instructions. }
  else { This loader returns None. }
}
```

The [validation system conversion](prompt_representation/vvaharness/validation/prompts/system.md.sudo.md) preserves read-only parent review, requested parallel persona tasks, report completeness/retry, synthesis and final output constraints. The three [persona conversions](prompt_representation/vvaharness/validation/subagents/) preserve their separate expertise, tools-if-granted conditions, evidence and gate contracts, qualitative decision criteria and model discretion. The [rules](prompt_representation/vvaharness/validation/claude_config/rules/) and [scoring skill](prompt_representation/vvaharness/validation/claude_config/skills/validation-scoring/SKILL.md.sudo.md) retain weights, coverage/critical caps, thresholds, rounding and secret handling. Earlier agent-scoring/Jira instructions remain beside capability-selected host-synthesis text; no unspecified precedence is invented. Dynamic launch evidence, optional posting context, validation hints, fact descriptions and persona suffixes are converted in their individual source views. Runtime values not in the supplied files remain unresolved.

## Scope and unresolved evidence

All source-defined requests are represented as requests, including those whose delivery is conditional. Some ordinary diagnostic strings are conservatively converted with an explicit “only if supplied to a model” boundary. This does not invent an actual delivery edge. Provider defaults, unseen user files, runtime model choices, actual compliance and external tool/dependency internals remain unresolved. Original sources and example payloads are supporting evidence; they are not substitutes for the converted behavioral blocks.
