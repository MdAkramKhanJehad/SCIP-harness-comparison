# vvaharness/sdk/README.md

Developer documentation for the SDK: how a plugin is written and enabled, the bounds and failure contract, programmatic scan, remediate and validate calls, and the findings handoff. It is not given to any model and has no runtime effect. The rendering lists the decisive values it states; each claim is the README's own statement, and the code that enforces it is noted where it is in this area.

Source: `vvaharness/sdk/README.md` (lines 1-331)
Executor: code (documentation only; nothing here executes)
Called from: not called; read by developers

// src: vvaharness/sdk/README.md:1-46
PluginContract {
  // one Protocol, VvahPlugin, returning one Contribution; every field optional
  seams: [
    { field: "enrichers",   reaches: "Workspace.analyze, so every graph query downstream" },
    { field: "graph_tools", reaches: "S2, S4 and S6 — advertised, permitted and budgeted together" },
    { field: "subagents",   reaches: "extension API; not yet consumed by detection stages" }
  ]
  "A scan loads a plugin only when `BUILTIN_PLUGINS` lists it and the profile names it"   // enforced in sdk/loading.sudo _built
  "`scan()` has no plugin argument."
  // enrichers are context_graph_sdk GraphEnricher; the SDK bounds them (deadline, cancellation, registry validation, phases PRE_DERIVATION and POST_DERIVATION only)   // external: context_graph_sdk
}

// src: vvaharness/sdk/README.md:48-81
Options {
  shipped semgrep profile: rulesets ["p/security-audit", "p/python", "p/secrets"] (fetched over the network); needs a semgrep binary on PATH
  local override: config.local.yaml beside the profile, deep-merged; must be owned by the user and not group- or world-writable (refused on POSIX otherwise)
  sdk.plugins entries: { name, configs, rulesets }; "Every key except `name` becomes a keyword argument of the plugin's constructor."
  "A dotted import path is **deliberately refused**"   // enforced in sdk/loading.sudo (BUILTIN_PLUGINS)
  // "In a single YAML file, a second top-level `sdk:` replaces the first, credentials included, so never add one."
}

// src: vvaharness/sdk/README.md:83-95
Options {
  MAX_PLUGINS: 16                 // sdk/plugins.sudo
  MAX_PLUGIN_GRAPH_TOOLS: 8       // "every tool is advertised in the system prompt of three stages"
  plugin name length: 64
  duplicate graph-tool name across plugins: raises
  plugin tool named like a built-in (GraphContext, GraphImpact, GraphNeighbors, GraphCommunityOf, GraphImporters, GraphSinksInCommunity): raises   // codegraph/tools.py register_graph_tools
  duplicate plugin name: raises; non-conforming object: TypeError
  order: (priority, name)
}

// src: vvaharness/sdk/README.md:97-115
FailureContract {
  "**A plugin that raises fails the scan.**"   // Workspace.analyze raises PluginError; "The scan stops after S0, before S1, prints `scan failed`, and exits 1."
  "**A hung `enrich()` hangs the analysis.**"   // the SDK deadline of 300 seconds is cooperative
  per-enricher bounds: 10000 nodes, 20000 edges, 20000 removals; per analysis: 50000 work units, at most 64 enrichers   // external: context_graph_sdk
  "**`PluginContext.configuration` is always empty.**"   // configure a plugin through its constructor
}

// src: vvaharness/sdk/README.md:117-143
RemediateAndValidate {
  "**`remediate()` defaults to `mode=\"fix\"` and edits target source.**"
  // report-only gives a proposed patch with no edits on via sdk, openai and deepagents; on via cli, list only Read and Grep in step_remediate.allowed_tools first, because that route keeps every listed tool in report-only too
  "**`remediate()` runs no policy gate.**"   // the path gates and patch content check apply only to the remediate command and in-scan S10
  validate(finding, remediation, repo, config=null): copies repo to a temporary workspace, writes remediation.diff as diff.patch for review, runs S11, cleans up; "does not apply the diff"
  ValidationCaseError: repo not a directory, finding.file empty, or diff empty; ValidationBusyError: called inside a running event loop
  "Handled session failures are inconclusive, not proof of a fix."
  // uses default DeepAgents validation settings; config supplies only the parent directory
}

// src: vvaharness/sdk/README.md:145-161
Limitations {
  graph_tools reach DeepAgents, the SDK and OpenAI tool adapters, and CLI sessions with MCP tools enabled; they require a working code graph
  "No detection stage passes `subagents` yet"
  // a tool docstring becomes the JSON-schema description the model reads
}

// src: vvaharness/sdk/README.md:163-206
SemgrepReferenceVariant {
  // abstracted: README.md:163-206 describes vvaharness/plugins/semgrep/ (rendered in its own files): nodes SemgrepScan, SemgrepRule, SemgrepFinding; edges FLAGGED_BY, DETECTED_BY, TRACE_TOUCHES; enrich() never raises; runs POST_DERIVATION
  bounds: MAX_FINDING_NODES 500 (severity-ranked), MAX_TRACE_STEPS 20 per finding, MAX_EDGES 18000
}

// src: vvaharness/sdk/README.md:208-224
RunningGuide {
  "**`scan()` runs the same pipeline as the CLI.**"   // sdk/runner.sudo scan → orchestrator.entry.main
  // inherits the configuration trust gate; ScanOptions.argv() reproduces the run
}

// src: vvaharness/sdk/README.md:226-325
HandoffGuide {
  "**Run the handoff against a dedicated, empty state directory.**"   // inject_findings writes only s2 to s4; older s5 to s8 rows of the same path would be resumed (sdk/handoff.sudo)
  seeds: s4 with input_kind "external"; s2 and s3 empty unless skip_discovery=false
  skip_discovery=false: "If either is missing, S4 runs its own deep dive and replaces the injected findings."
  "The resumed scan still spends model tokens in the auto-exclude survey and in S6–S8."   // skip the survey with extra_argv=("--no-auto-step1",)
  per-step model calls (README table, lines 281-294): auto-exclude yes; s0 no; graph no; s1 no; s2, s3, s4 skipped; s5 no; s6 yes; s7 "when findings need semantic grouping"; s8 "when findings remain"; s9 no
  S5 drops: paths not in the repository inventory (convert with repo=), test, mock or example paths (secrets and information leaks kept), lines outside the file
  conversion: first CWE becomes cwe; unmapped CWE becomes vuln class other; results without path or start.line dropped; missing results key raises; origin "semgrep:<rule-id>"
  bounds: MAX_FINDINGS 2000 results per report, MAX_JSON_BYTES 64 MiB, MAX_INJECTED_FINDINGS 2000
}
