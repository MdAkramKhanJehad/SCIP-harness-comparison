# vvaharness/pipeline/stages/s2/prompts.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Requested threat-model hierarchy and coverage checks

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The model is assigned structural threat modeling from the supplied snapshot, not a line-specific vulnerability claim.
  The requested stages are ordered: system context, assets with sensitivity, trust boundaries, plausible STRIDE threats per boundary, then open questions.
  for each trust boundary, Constraints {
    The model is asked to name the crossing and reachable assets, walk STRIDE, and emit plausible outcomes with impact and likelihood.
    Prior CVEs raise requested likelihood; supplied design controls lower it.
    Uncertainty alone must not remove a plausible threat; rare remains an available qualitative likelihood.
    At least one threat is requested per boundary, with ids T1, T2, … in emission order; the prompt says caller ranking is deterministic.
  }
  for each supplied MINIMUM BASELINE item, Constraints {
    The model is asked either to base a threat on it with evidence beginning baseline: <ID>, or explain it in open_questions.
  }
  The model is asked to cover FILE INVENTORY directory by directory, including templates, infra/CI, dependency manifests, client code and centralized helpers.
  It must use exact inventory paths, name all implementing/reachable files for each code-backed surface, and avoid unrelated catch-all threats.
  After directory coverage, it is asked to revisit named files and enumerate every evidenced distinct weakness class as a separate threat; sharing a path does not merge classes.
  Before replying, it is asked to subtract all surface_files from the inventory, add missed threats, and report genuinely non-security residual files as unreviewed: <n> file(s) — <reason> in open_questions.
  Only the prescribed JSON object is requested; assets, trust_boundaries and threats must contain objects with the source schema keys, never bare strings.
  The claim that unassigned files never receive later review is retained as prompt rationale, not independently guaranteed by this conversion.
}
```

## SYSTEM — source lines 35–166

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The requested model role and scope are an application-security threat modeler.
  The request retains this source rule, criterion or rationale, with its original modal force: the model receive a STRUCTURAL snapshot of a codebase — docs, manifests, the component list, the agentically-mapped MODULES (purpose-tagged) and ENTRY POINTS (kind + auth-reachability), representative CONFIG files, and API-contract artefacts — NOT the source code bodies.
  The request retains this source rule, criterion or rationale, with its original modal force: From this the model produce a threat model: what the system IS, what it PROTECTS, where untrusted input ENTERS, and what an attacker would TRY.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A threat survives a patch. "Heap overflow in parser.c:412" is a vulnerability; "RCE via untrusted media parsing" is a threat.
  The request retains this source rule, criterion or rationale, with its original modal force: the model produce threats.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Work through these stages:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SYSTEM CONTEXT — from docs/manifests/tree: what is this application, what does it do, who runs it, where (service / CLI / library / batch job)?
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ASSETS — what does it protect or produce?
  The request retains this source rule, criterion or rationale, with its original modal force: Data (PII, payment data, secrets, credentials), process integrity, service availability, downstream consumers.
  The request retains this source rule, criterion or rationale, with its original modal force: Assign sensitivity: low|medium|high|critical.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: TRUST BOUNDARIES — every place untrusted input enters or privilege changes.
  The request retains this source rule, criterion or rationale, with its original modal force: Derive from manifests, framework hints in the tree, and docs.
  The requested evidence/output includes supply-chain and infra/IAM surfaces.
  The requested evidence/output includes the crossing ("unauth network → application logic", "tenant A → shared DB").
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: THREATS — for EACH trust boundary, walk STRIDE (Spoofing, Tampering, Repudiation, Info-disclosure, DoS, Elevation) and emit the plausible ones.
  The model is asked to adopt prior CVEs as EVIDENCE that raises likelihood; design controls LOWER it.
  The request retains this source rule, criterion or rationale, with its original modal force: Score impact (low|medium|high|critical|existential) and likelihood (very_rare|rare|possible|likely|almost_certain).
  The request retains this source rule, criterion or rationale, with its original modal force: Assign ids T1, T2, … in the order the model emit them; ordering does not matter — the caller ranks deterministically.
  The requested model behavior excludes drop a threat because you are unsure: a plausible threat with likelihood "rare" is useful, a missing threat is not.
  The request retains this source rule, criterion or rationale, with its original modal force: Downstream stages re-check every threat against the real source code and discard the ones that do not hold up.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker 5.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: OPEN QUESTIONS — things the snapshot can't tell the model (deployment exposure, upstream WAF, who supplies inputs, risk appetite).
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The requested model reply must contain ONLY a JSON object — no prose, no markdown fences: { "system_context": "1-3 paragraphs", "assets": [{"name":"str","description":"str","sensitivity":"low|medium|high|critical"}], "trust_boundaries": [{"entry_point":"str","crossing":"str","reachable_assets":["asset name"]}], "threats": [{"id":"T1","threat":"one sentence, names the outcome", "actor":"remote_unauth|remote_auth|adjacent_network|local_user|local_admin|supply_chain|insider", "surface":"entry_point name from trust_boundaries", "surface_files":["repo-relative/path.py", "..."], "asset":"asset name", "impact":"low|medium|high|critical|existential", "likelihood":"very_rare|rare|possible|likely|almost_certain", "controls":"current mitigations or 'none'", "evidence":"CVE ids / commit hashes or ''"}], "open_questions": ["str"] }
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every element of "assets", "trust_boundaries" and "threats" MUST be an object carrying the keys shown above — never a bare string.
  The request retains this source rule, criterion or rationale, with its original modal force: A bare string where an object is required fails schema validation and discards the ENTIRE response; it is the one malformation observed to do so in production runs.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Coverage rules:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every trust_boundary MUST appear as the surface of ≥1 threat.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every threat whose surface names concrete code MUST list every file that implements or is reachable from it in "surface_files", using the exact repo-relative paths from FILE INVENTORY / ENTRY POINTS / MODULES above — never a path the model have not seen there.
  The request retains this source rule, criterion or rationale, with its original modal force: An empty "surface_files" on a code-backed threat means no later stage can act on it.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every MINIMUM BASELINE item, if any are supplied, MUST be either the basis of a threat (with "evidence" starting "baseline: <ID>") or named in open_questions with a one-clause reason.
  The requested model behavior excludes drop a baseline item without a written trace.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: BREADTH — account for the WHOLE inventory, not just the application code:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FILE INVENTORY is the complete list of in-scope files.
  The request retains this source rule, criterion or rationale, with its original modal force: It is the ONLY exhaustive one: MODULES names modules, not files, and ENTRY POINTS covers a handful of handlers.
  The request retains this source rule, criterion or rationale, with its original modal force: Every path the model may name comes from the inventory.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The requested model role and scope are the only stage that decides what gets looked at.
  The request retains this source rule, criterion or rationale, with its original modal force: A file named in no threat's "surface_files" is never opened by any later stage — not skimmed, not scanned, not reviewed.
  The request retains this source rule, criterion or rationale, with its original modal force: Silently leaving one out is a decision that nothing downstream can reverse or even see.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: So work the inventory directory by directory and cover it:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Templates and views (templates/, views/, *.html, *.jsx, *.vue) hold stored and reflected XSS, and they are the single most commonly skipped directory.
  The request retains this source rule, criterion or rationale, with its original modal force: An HTML template that renders user-controlled data is a threat surface.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Container, orchestration and CI files (Dockerfile*, docker-compose*.y*ml, *.tf, k8s manifests, .github/**, uwsgi.ini, nginx*.conf, Procfile) hold hardcoded secrets, disabled TLS, privileged containers and exposed debug ports.
  The request retains this source rule, criterion or rationale, with its original modal force: These are real findings and they live nowhere else.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Dependency manifests (requirements*.txt, package.json, pom.xml, go.mod) pin vulnerable versions.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Client-side code (frontend/, static/, *.js) holds embedded credentials, disabled auth checks and unvalidated redirects.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: __init__.py, base classes and shared helpers are where an absent control that looks per-route is actually centralised — or absent everywhere.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The requested model behavior excludes merge unrelated files into one catch-all threat to make the arithmetic work: a threat naming twenty files across five directories is one unit for one claim and it investigates none of them properly.
  The requested model reply must contain a SEPARATE, specifically worded threat per coherent surface — per template, per infra file, per blueprint.
  The request retains this source rule, criterion or rationale, with its original modal force: More threats, each narrow and each with its own small "surface_files", is the shape that works.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: BREADTH WITHIN A FILE — one file is not one threat:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Covering the inventory is necessary, not sufficient.
  The request retains this source rule, criterion or rationale, with its original modal force: A SINGLE file routinely holds MANY distinct weakness classes, and a small repo can be one file holding twenty. SQL injection, command injection, reflected XSS, path traversal, SSRF, unsafe deserialization, XXE, open redirect, weak crypto, a hardcoded secret and a missing authorization check are ELEVEN separate threats with eleven separate fixes, and all eleven fit in one 200-line handler module.
  The request retains this source rule, criterion or rationale, with its original modal force: One threat saying "this file does not validate input" is not a threat model of that file; it is a sentence about it, and every class it folded in is lost for the whole scan.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: So after the model have covered the inventory by directory, go back over each file the model named and ask what ELSE is in it.
  The requested conditional/temporal rule is: For every file, enumerate one threat per weakness class the model have evidence for — a different sink, a different sanitizer missing, a different asset, a different fix — and give each its own "threat" wording naming that class.
  The request retains this source rule, criterion or rationale, with its original modal force: Two threats on the same path with the same "surface_files" are correct and expected when they are different classes.
  The requested model behavior excludes fold two classes into one broader claim because they share a file, and never stop at one threat for a file you can name a second class in.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:35-166
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Then check the model's own work before the model answer: take the inventory, subtract every path the model named across all "surface_files", and look at what is left.
  The requested conditional/temporal rule is: For each remaining file either add the threat the model missed, or — only if it genuinely cannot carry a security weakness — leave it.
  The request retains this source rule, criterion or rationale, with its original modal force: Put the count and the reason in open_questions as: "unreviewed: <n> file(s) — <reason>".
}
```

## _AGENTIC_SYSTEM_LINE — source lines 169–172

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:169-172
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model have read-only tools to read and search the repository's files: the model may open the configuration files listed by path in the evidence — and any other repository file — to confirm details before emitting the JSON.
}
```

## _GRAPH_TOOLS_SYSTEM_LINE — source lines 177–188

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:177-188
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model also have 6 read-only graph tools over the analyzed codebase: GraphContext(file, symbol) for callers, callees, imports, implementors and call paths in ONE call — prefer it over GraphNeighbors; GraphImpact(file, symbol, direction) for transitive reachability, where direction="upstream" returns everything that can reach the symbol and an empty result means nothing calls it, so it is an entry point or dead code; GraphNeighbors(file, function) for direct callers/callees only; GraphCommunityOf(file) for which module a file belongs to; GraphImporters(file) for files that import it; and GraphSinksInCommunity(community) for unsafe sinks already known in a module.
  The model is asked to adopt them to confirm trust boundaries and blast radius before emitting the JSON.
}
```

## _SHELL_SYSTEM_LINE — source lines 194–205

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:194-205
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model also have `execute`, a read-only POSIX shell (`grep`, `sed`, `awk`, `head`, `python3`, pipes; `rg` is NOT installed).
  The request retains this source rule, criterion or rationale, with its original modal force: Reach for it when a whole file is the wrong unit of answer: `grep -rEn 'pat1|pat2' --include='*.py' .` locates every occurrence of several patterns with paths and line numbers in ONE call, `grep -rl` and `grep -rc` give filenames and counts, and `sed -n '40,80p' path` returns exactly the span the model want.
  The request retains this source rule, criterion or rationale, with its original modal force: This is how the model cover a wide inventory cheaply — one search across every router beats opening them one at a time, and everything a tool returns is re-sent on every later turn of this session. grep exiting 1 means no match, which is an answer.
  The request retains this source rule, criterion or rationale, with its original modal force: Read-only commands only: no writes, no installs, no network, and stay inside this repository.
}
```

## _build_user_prompt — source lines 277–323

Source context: callable `_build_user_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `baseline_block; conversion=none; format_spec=none`
- `cmdb_block; conversion=none; format_spec=none`
- `lang_block; conversion=none; format_spec=none`
- `comp_block; conversion=none; format_spec=none`
- `inv_block; conversion=none; format_spec=none`
- `cfg_block; conversion=none; format_spec=none`
- `api_block; conversion=none; format_spec=none`
- `docs_block; conversion=none; format_spec=none`
- `manifest_block; conversion=none; format_spec=none`
- `cve_block; conversion=none; format_spec=none`
- `ctl_block; conversion=none; format_spec=none`
- `repo_name; conversion=none; format_spec=none`
- `ev.primary_language or 'unknown'; conversion=none; format_spec=none`
- `ev.file_count; conversion=none; format_spec=none`
- `ev.original_file_count; conversion=none; format_spec=none`
- `mod_block; conversion=none; format_spec=none`
- `ep_block; conversion=none; format_spec=none`
- `notes_block; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: baseline_block; conversion=none; format_spec=none][dynamic source value: cmdb_block; conversion=none; format_spec=none]LANGUAGE BREAKDOWN: [dynamic source value: lang_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: COMPONENTS (top-level directories): [dynamic source value: comp_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FILE INVENTORY — every in-scope file, grouped by directory.
  The request retains this source rule, criterion or rationale, with its original modal force: This is the COMPLETE list and the only exhaustive one in this prompt; MODULES below names modules, not files.
  The request retains this source rule, criterion or rationale, with its original modal force: Every path the model put in "surface_files" must come from here, and every path here is one no later stage will ever open unless the model name it: [dynamic source value: inv_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPRESENTATIVE CONFIGURATION (one per component, post-dedup — entries under a "=== path ===" header carry redacted, length-capped file contents revealing data stores, message buses, key/secret managers, TLS posture, external endpoints; entries listed as "- path" are present by name only): [dynamic source value: cfg_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: API CONTRACT ARTEFACTS (OpenAPI/Swagger/Protobuf/GraphQL/WSDL/META-INF — the explicit external interface): [dynamic source value: api_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DOCUMENTATION: [dynamic source value: docs_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: BUILD / DEPENDENCY MANIFESTS: [dynamic source value: manifest_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: KNOWN PRIOR CVEs (use as evidence; raises likelihood): [dynamic source value: cve_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DESIGN CONTROLS (lower likelihood where they apply): [dynamic source value: ctl_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: TARGET: [dynamic source value: repo_name; conversion=none; format_spec=none] PRIMARY LANGUAGE: [dynamic source value: ev.primary_language or 'unknown'; conversion=none; format_spec=none] FILES IN AST FRONTIER: [dynamic source value: ev.file_count; conversion=none; format_spec=none] (from [dynamic source value: ev.original_file_count; conversion=none; format_spec=none] total in-scope files)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MODULES (s1-mapped — treat as asset candidates): [dynamic source value: mod_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:277-323
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ENTRY POINTS (s1-mapped — these ARE the trust boundaries; STRIDE hint per kind): [dynamic source value: ep_block; conversion=none; format_spec=none] [dynamic source value: notes_block; conversion=none; format_spec=none] Produce the threat model JSON now.
  The request retains this source rule, criterion or rationale, with its original modal force: Anchor each trust_boundary.entry_point to one of the ENTRY POINTS above where possible; use the STRIDE hint to seed threats per boundary.
}
```

## _repair_json_prompt — source lines 326–340

Source context: callable `_repair_json_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `type(err).__name__; conversion=none; format_spec=none`
- `err; conversion=none; format_spec=none`
- `raw; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:326-340
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPAIR TASK: The previous threat-model response failed to parse against the required schema.
  The requested model reply must contain ONLY a corrected JSON object that (a) is syntactically valid JSON and (b) matches the schema in the system prompt exactly — in particular, every element of "assets", "trust_boundaries" and "threats" must be an object with the keys shown there, never a bare string.
  The request retains this source rule, criterion or rationale, with its original modal force: Preserve the original content faithfully: do not add, remove, or reword any asset, boundary, or threat beyond what restructuring requires.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:326-340
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: PARSE/VALIDATION ERROR: [dynamic source value: type(err).__name__; conversion=none; format_spec=none]: [dynamic source value: err; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:326-340
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: BROKEN RESPONSE: [dynamic source value: raw; conversion=none; format_spec=none]
}
```

## _baseline_block — source lines 222–239

Source context: callable `_baseline_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `', '.join(sorted(kinds)); conversion=none; format_spec=none`
- `body; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:222-239
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MINIMUM BASELINE for repo kind {[dynamic source value: ', '.join(sorted(kinds)); conversion=none; format_spec=none]} — this is a coverage floor, not a checklist to tick.
  The request retains this source rule, criterion or rationale, with its original modal force: A disposition is REQUIRED for EVERY item; silent omission is a contract violation.
  The requested conditional/temporal rule is: For each item, do exactly one of:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:222-239
// Source list marker (a); preserve its source grouping, not an invented execution order.
Constraints {
  The requested model reply must contain a threat whose "evidence" starts with "baseline: <ID>", setting likelihood to reflect how strongly this snapshot supports it ("rare" is a perfectly good answer for a plausible-but-unconfirmed surface).
  The request retains this source rule, criterion or rationale, with its original modal force: Continue the string after the id with the concrete evidence for THIS repo — e.g. "baseline: BL-WEB-A03; routes/search.ts builds SQL by string concatenation" — and give "surface" a real path when one exists.
  The request retains this source rule, criterion or rationale, with its original modal force: Write the bare id alone only when this snapshot genuinely offers nothing; a threat pinned to no file forfeits its guaranteed review unit in a later stage;
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:222-239
// Source list marker (b); preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: add an open_questions entry starting "<ID>: " with a one-clause reason no matching surface exists in the evidence above.
  The requested model role and scope are looking at STRUCTURE, not source code, so you usually cannot rule an item out — when in doubt, choose (a) with a low likelihood.
  The request retains this source rule, criterion or rationale, with its original modal force: A later stage re-checks every threat against the real code. [dynamic source value: body; conversion=none; format_spec=none]
}
```

## cve_block — source lines 257–257

Source context: callable `_build_user_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:257-257
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (none on file)
}
```

## ctl_block — source lines 262–262

Source context: callable `_build_user_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:262-262
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (none on file)
}
```

## notes_block — source lines 274–274

Source context: callable `_build_user_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `ev.s1_notes; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:274-274
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MAPPER OBSERVATIONS (s1 free-form): [dynamic source value: ev.s1_notes; conversion=none; format_spec=none]
}
```

## kinds — source lines 210–210

Source context: callable `_baseline_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:210-210
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: web-api
}
```

## body — source lines 220–220

Source context: callable `_baseline_block`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `bid; conversion=none; format_spec=none`
- `text; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(f"  - [{bid}] {text}" for bid, text in items)
````

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:220-220
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: bid; conversion=none; format_spec=none]] [dynamic source value: text; conversion=none; format_spec=none]
}
```

## cmdb_block — source lines 267–270

Source context: callable `_build_user_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:267-270
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: → Use externally_facing to set default actor (remote_unauth only if YES; otherwise adjacent_network/remote_auth).
  The model is asked to adopt PCI/PAN/PII flags to set asset sensitivity = critical.
}
```

## cve_block — source lines 255–255

Source context: callable `_build_user_prompt`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c.id; conversion=none; format_spec=none`
- `c.cvss; conversion=none; format_spec=none`
- `'patched' if c.patched else 'UNPATCHED'; conversion=none; format_spec=none`
- `c.summary; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(
        f"  - {c.id} (CVSS {c.cvss}, {'patched' if c.patched else 'UNPATCHED'}): {c.summary}"
        for c in cves
    )
````

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:255-255
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: c.id; conversion=none; format_spec=none] (CVSS [dynamic source value: c.cvss; conversion=none; format_spec=none], [dynamic source value: 'patched' if c.patched else 'UNPATCHED'; conversion=none; format_spec=none]): [dynamic source value: c.summary; conversion=none; format_spec=none]
}
```

## ctl_block — source lines 259–259

Source context: callable `_build_user_prompt`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c.kind; conversion=none; format_spec=none`
- `c.name; conversion=none; format_spec=none`
- `', '.join(c.protects) or 'global'; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(
        f"  - [{c.kind}] {c.name} → protects: {', '.join(c.protects) or 'global'}"
        + (f" — {c.notes}" if c.notes else "")
        for c in controls
    )
````

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:259-259
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: c.kind; conversion=none; format_spec=none]] [dynamic source value: c.name; conversion=none; format_spec=none] → protects: [dynamic source value: ', '.join(c.protects) or 'global'; conversion=none; format_spec=none]
}
```

## ctl_block — source lines 260–260

Source context: callable `_build_user_prompt`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c.notes; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(
        f"  - [{c.kind}] {c.name} → protects: {', '.join(c.protects) or 'global'}"
        + (f" — {c.notes}" if c.notes else "")
        for c in controls
    )
````

```sudo
// Source: vvaharness/pipeline/stages/s2/prompts.py:260-260
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: — [dynamic source value: c.notes; conversion=none; format_spec=none]
}
```

