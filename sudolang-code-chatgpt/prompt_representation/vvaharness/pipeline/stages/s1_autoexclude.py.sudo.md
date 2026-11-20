# vvaharness/pipeline/stages/s1_autoexclude.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Requested production-scope triage

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
Constraints {
  The model is asked to infer non-production exclusions from a deterministic structural survey and build/README excerpts, not to inspect an invented source tree.
  Requested exclusion categories include generated code, third-party copies, test-only trees, editor metadata, build outputs, docs-only trees, demo apps, data dumps, non-code localization bundles and non-source lock/manifests.
  if (a candidate is application code, runtime configuration, production IaC, migrations, source API schemas, security code, internally maintained shared libraries or server templates) {
    The model is instructed NEVER to exclude it, even if its directory resembles a normally excluded category.
  }
  if (production status is uncertain) { The model is instructed to retain the candidate. }
  Only one fenced YAML block is requested; executable overlay vetting and keep-ratio reporting are separate source code decisions, not model guarantees.
}
```

## _SYSTEM — source lines 49–94

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
Constraints {
  The requested model role and scope are a build/scan triage agent.
  The request retains this source rule, criterion or rationale, with its original modal force: the model will be shown a deterministic survey of a source tree (directory layout, file counts, extension histogram, and excerpts from build/README files).
  The request retains this source rule, criterion or rationale, with its original modal force: Decide which parts are NOT production code so a security scanner can skip them.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: EXCLUDE these categories:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Generated/auto-generated code: protobuf stubs, OpenAPI clients, code-gen output, compiled assets, *.pb.go, *.generated.*, *_pb2.py
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Vendored/third-party copies: vendor/, third_party/, node_modules/ (if checked in), bower_components/, external/
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Test-only trees: test fixtures, sample data, mock servers, e2e test suites, cypress/fixtures, __snapshots__
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: IDE/editor metadata: .idea/, .vscode/ (except shared settings), .vs/, *.swp, *~
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Build/CI output: dist/, build/, out/, target/, bin/ (compiled output), .cache/, coverage/
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Documentation-only trees: docs/, documentation/, wiki/, man/, guides/
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Demo/example apps: examples/, samples/, demo/, playground/, tutorial/
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Data dumps: fixtures with large data files, seed data, database backups (NOT migration scripts — those are NEVER EXCLUDE, below)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Localisation bundles: locale/, i18n/, l10n/, translations/ (unless they contain code)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Lock files and manifests that are not source: package-lock.json, yarn.lock, Gemfile.lock, poetry.lock, go.sum, Cargo.lock
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: NEVER EXCLUDE — these are in scope even if they look non-functional:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Application source code in ANY language
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Configuration files that affect runtime behavior (nginx.conf, app.yaml, settings.py, application.properties, .env.example)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Infrastructure-as-code that provisions production (Terraform, CloudFormation, Helm charts, Kubernetes manifests, Ansible playbooks, Dockerfiles)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Database migration scripts (they modify production schema)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: API schema definitions (OpenAPI/Swagger YAML, GraphQL SDL, protobuf .proto source files — NOT generated stubs)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Security-related files (auth middleware, RBAC config, certificate handling)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Shared libraries or internal packages (even if they look like vendor code, if they are maintained in this repo they are production)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Server-side template directories (Django/Jinja/ERB/JSP templates — .html/.j2/.erb files rendered by the app are XSS/SSTI attack surface, even in dirs named template/, templates/, views/, static/)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
Constraints {
  The requested conditional/temporal rule is: When unsure whether something is production code, do NOT exclude it.
  The request retains this source rule, criterion or rationale, with its original modal force: A false negative (scanning non-production code) wastes time; a false positive (excluding production code) misses vulnerabilities.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:49-94
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model MUST reply with a single fenced ```yaml block and nothing else.
}
```

## _EXCERPT_NAMES — source lines 99–102

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:99-102
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ^(readme(\..*)?|package\.json|pom\.xml|build\.gradle(\.kts)?|setup\.(py|cfg)|pyproject\.toml|cargo\.toml|go\.mod|makefile|dockerfile|composer\.json|gemfile|.*\.csproj|.*\.sln|angular\.json|lerna\.json|nx\.json|turbo\.json)$
}
```

## _DEDUP_KEYS — source lines 112–112

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:112-112
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: min_cluster_size
}
```

## _DEDUP_KEYS — source lines 113–113

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:113-113
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: keep_per_top_dir
}
```

## _DEDUP_KEYS — source lines 113–113

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:113-113
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: promote_on_secret_hit
}
```

## _DEDUP_KEYS — source lines 114–114

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:114-114
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: promote_on_insecure_value
}
```

## _DEDUP_KEYS — source lines 114–114

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:114-114
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## survey — source lines 226–233

Source context: callable `_survey`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_TREE_DEPTH + 1; conversion=none; format_spec=none`
- `render_tree(); conversion=none; format_spec=none`
- `_EXT_TOP_N; conversion=none; format_spec=none`
- `ext_block; conversion=none; format_spec=none`
- `_LARGEST_N; conversion=none; format_spec=none`
- `large_block; conversion=none; format_spec=none`
- `exc_block; conversion=none; format_spec=none`

## Directory tree (depth ≤[dynamic source value: _TREE_DEPTH + 1; conversion=none; format_spec=none], already-excluded dirs hidden, counts = files that survive current exclusions)

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:226-233
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (untyped):

``````text
[dynamic source value: render_tree(); conversion=none; format_spec=none]
``````

```sudo
```

## Extension histogram (top [dynamic source value: _EXT_TOP_N; conversion=none; format_spec=none])

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:226-233
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (untyped):

``````text
[dynamic source value: ext_block; conversion=none; format_spec=none]
``````

```sudo
```

## Largest [dynamic source value: _LARGEST_N; conversion=none; format_spec=none] files (after current exclusions)

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:226-233
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (untyped):

``````text
[dynamic source value: large_block; conversion=none; format_spec=none]
``````

```sudo
```

## Build / README excerpts

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:226-233
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: exc_block; conversion=none; format_spec=none]
}
```

## _FENCE_RX — source lines 239–239

Source context: callable `<module>`; enclosing call `re.compile`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:239-239
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation ((?P<lang>[A-Za-z0-9_+.-]*)[^\S\n]*\n(?P<body>.*?)(?:\n```|\Z)):

``````text

``````

```sudo
```

## _KEY_MATERIAL_NAME_PREFIXES — source lines 332–332

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:332-332
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: id_rsa
}
```

## _KEY_MATERIAL_NAME_PREFIXES — source lines 332–332

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:332-332
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: id_dsa
}
```

## _KEY_MATERIAL_NAME_PREFIXES — source lines 332–332

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:332-332
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: id_ecdsa
}
```

## _KEY_MATERIAL_NAME_PREFIXES — source lines 332–332

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:332-332
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: id_ed25519
}
```

## user_prompt — source lines 603–636

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `', '.join(sorted(base_dirs)); conversion=none; format_spec=none`
- `', '.join(sorted(base_exts)); conversion=none; format_spec=none`
- `', '.join(base_globs); conversion=none; format_spec=none`
- `cur_max_kb; conversion=none; format_spec=none`
- `list(cur_dedup['exts']); conversion=none; format_spec=none`
- `cur_dedup['min_cluster_size']; conversion=none; format_spec=none`
- `survey; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Below is a deterministic survey of a repository.
  The request retains this source rule, criterion or rationale, with its original modal force: Propose ADDITIONAL scan exclusions so the security scanner only sees production code.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Already excluded (do NOT repeat these — propose only repo-specific extras): dirs : [dynamic source value: ', '.join(sorted(base_dirs)); conversion=none; format_spec=none] exts : [dynamic source value: ', '.join(sorted(base_exts)); conversion=none; format_spec=none] globs: [dynamic source value: ', '.join(base_globs); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Current max_file_kb = [dynamic source value: cur_max_kb; conversion=none; format_spec=none] Current config_dedup = {exts: [dynamic source value: list(cur_dedup['exts']); conversion=none; format_spec=none], min_cluster_size: [dynamic source value: cur_dedup['min_cluster_size']; conversion=none; format_spec=none]}
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: survey; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
Constraints {
  The requested model reply must contain ONLY a fenced YAML block with these keys (omit any key you have no change for — do NOT emit empty/null placeholders):
}
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  The requested example format/pattern includes exclude_dirs with source contract # directory NAMES (any depth), e.g. "generated", "samples".
  The requested example format/pattern includes exclude_exts with source contract # file extensions WITH leading dot, e.g. ".pb.go", ".min.js".
  The requested example format/pattern includes exclude_globs with source contract # repo-relative posix fnmatch, e.g. "**/*.g.dart", "tools/codegen/**".
  The requested example format/pattern includes max_file_kb with source contract 1024   # OPTIONAL int. Only emit if the largest-files list shows.
  The requested example format/pattern includes config_dedup with source contract # OPTIONAL. Only emit keys you want to change..
  The requested example format/pattern includes exts with source contract [...]       # FULL list (REPLACES current). Include defaults you want.
  The requested example format/pattern includes min_cluster_size with source contract 3.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (yaml):

``````text
exclude_dirs:   # directory NAMES (any depth), e.g. "generated", "samples"
  - ...
exclude_exts:   # file extensions WITH leading dot, e.g. ".pb.go", ".min.js"
  - ...
exclude_globs:  # repo-relative posix fnmatch, e.g. "**/*.g.dart", "tools/codegen/**"
  - ...
max_file_kb: 1024   # OPTIONAL int. Only emit if the largest-files list shows
                    # genuine source bigger than the current limit (raise it)
                    # or only data dumps above a lower threshold (lower it).
config_dedup:       # OPTIONAL. Only emit keys you want to change.
  exts: [...]       # FULL list (REPLACES current). Include defaults you want
                    # to keep plus repo-specific formats e.g. ".tfvars", ".cue".
  min_cluster_size: 3
``````

```sudo
```

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Whole sub-repos that are clearly test-automation, demo, or tooling-only may be excluded via exclude_globs (e.g. "that-repo/**").
  The request retains this source rule, criterion or rationale, with its original modal force: Be conservative.
}
```

## _survey — source lines 215–215

Source context: callable `_survey`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(ext_hist) - _EXT_TOP_N; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:215-215
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: … (+[dynamic source value: len(ext_hist) - _EXT_TOP_N; conversion=none; format_spec=none] more extensions)
}
```

## exc_block — source lines 219–219

Source context: callable `_survey`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:219-219
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (no README/build files found at depth ≤2)
}
```

## _OVERLAY_KEYS — source lines 243–243

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:243-243
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_dirs
}
```

## _OVERLAY_KEYS — source lines 243–243

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:243-243
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_exts
}
```

## _OVERLAY_KEYS — source lines 243–243

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:243-243
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_globs
}
```

## _OVERLAY_KEYS — source lines 244–244

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:244-244
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## _OVERLAY_KEYS — source lines 244–244

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:244-244
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## _VENDOR_PATH_SEGMENTS — source lines 306–306

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:306-306
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: third_party
}
```

## _VENDOR_PATH_SEGMENTS — source lines 307–307

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:307-307
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: node_modules
}
```

## _VENDOR_PATH_SEGMENTS — source lines 307–307

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:307-307
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: bower_components
}
```

## _VENDOR_PATH_SEGMENTS — source lines 307–307

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:307-307
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: jspm_packages
}
```

## _VENDOR_PATH_SEGMENTS — source lines 307–307

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:307-307
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: site-packages
}
```

## _KEY_MATERIAL_NAMES — source lines 334–334

Source context: callable `<module>`; enclosing call `frozenset`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:334-334
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: .git-credentials
}
```

## vet_config_dedup — source lines 442–442

Source context: callable `vet_config_dedup`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:442-442
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: promote_on_secret_hit
}
```

## vet_config_dedup — source lines 442–442

Source context: callable `vet_config_dedup`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:442-442
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: promote_on_insecure_value
}
```

## vet_overlay — source lines 536–536

Source context: callable `vet_overlay`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:536-536
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: auto_exclude_protect_templates
}
```

## vet_overlay — source lines 547–547

Source context: callable `vet_overlay`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:547-547
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: auto_exclude_protect_key_material
}
```

## vet_overlay — source lines 558–558

Source context: callable `vet_overlay`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:558-558
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: auto_exclude_protect_secrets
}
```

## vet_overlay — source lines 569–569

Source context: callable `vet_overlay`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:569-569
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: auto_exclude_protect_client_sinks
}
```

## user_dd — source lines 592–592

Source context: callable `run`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:592-592
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## run — source lines 638–639

Source context: callable `run`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `repo_root; conversion=none; format_spec=none`
- `n_files; conversion=none; format_spec=none`
- `len(user_prompt); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:638-639
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [auto-step1] surveying [dynamic source value: repo_root; conversion=none; format_spec=none] ([dynamic source value: n_files; conversion=none; format_spec=none] files, prompt [dynamic source value: len(user_prompt); conversion=none; format_spec=none] chars)
}
```

## mfk — source lines 686–686

Source context: callable `run`; enclosing call `data.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:686-686
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## overlay — source lines 714–714

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:714-714
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_dirs
}
```

## overlay — source lines 714–714

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:714-714
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_exts
}
```

## overlay — source lines 715–715

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:715-715
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_globs
}
```

## dd_in — source lines 719–719

Source context: callable `run`; enclosing call `data.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:719-719
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## run — source lines 741–741

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:741-741
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## run — source lines 752–752

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:752-752
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## run — source lines 754–754

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:754-754
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## run — source lines 756–758

Source context: callable `run`; enclosing call `console.write`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `out; conversion=none; format_spec=none`
- `len(dirs); conversion=none; format_spec=none`
- `len(exts); conversion=none; format_spec=none`
- `len(globs); conversion=none; format_spec=none`
- `', ' + ', '.join(extras) if extras else ''; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:756-758
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [auto-step1] wrote [dynamic source value: out; conversion=none; format_spec=none] (+[dynamic source value: len(dirs); conversion=none; format_spec=none] dirs, +[dynamic source value: len(exts); conversion=none; format_spec=none] exts, +[dynamic source value: len(globs); conversion=none; format_spec=none] globs[dynamic source value: ', ' + ', '.join(extras) if extras else ''; conversion=none; format_spec=none])
}
```

## lines — source lines 197–197

Source context: callable `render_tree`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tree[''][1]; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:197-197
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ./ ([dynamic source value: tree[''][1]; conversion=none; format_spec=none] files)
}
```

## vet_overlay — source lines 492–494

Source context: callable `vet_overlay`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `vetoed; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:492-494
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: language-erasure veto: model-proposed exclusion(s) [dynamic source value: vetoed; conversion=repr; format_spec=none] would erase an entire scanner-known language from scope; entries dropped from the overlay
}
```

## vet_overlay — source lines 497–497

Source context: callable `vet_overlay`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:497-497
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_language_veto
}
```

## cur_max_kb — source lines 590–590

Source context: callable `run`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:590-590
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## max_tok — source lines 601–601

Source context: callable `run`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:601-601
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: auto_exclude_max_tokens
}
```

## effort — source lines 640–640

Source context: callable `run`; enclosing call `knob`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:640-640
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step1.auto_exclude_effort
}
```

## run — source lines 672–672

Source context: callable `run`; enclosing call `data.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:672-672
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_exts
}
```

## run — source lines 702–703

Source context: callable `run`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `n_before; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:702-703
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: auto-exclude overlay would empty the scope ([dynamic source value: n_before; conversion=none; format_spec=none] files -> 0); overlay discarded
}
```

## overlay['max_file_kb'] — source lines 717–717

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:717-717
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## overlay['config_dedup'] — source lines 742–742

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:742-742
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## run — source lines 747–747

Source context: callable `run`; enclosing call `out.write_text`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

# Auto-generated by vvaharness auto-step1 — appended to global step1.

## run — source lines 753–753

Source context: callable `run`; enclosing call `extras.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `overlay['max_file_kb']; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:753-753
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb=[dynamic source value: overlay['max_file_kb']; conversion=none; format_spec=none]
}
```

## run — source lines 755–755

Source context: callable `run`; enclosing call `extras.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `sorted(overlay['config_dedup']); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:755-755
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup=[dynamic source value: sorted(overlay['config_dedup']); conversion=none; format_spec=none]
}
```

## rel — source lines 153–153

Source context: callable `_survey`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `rel_dir; conversion=none; format_spec=none`
- `fn; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:153-153
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: rel_dir; conversion=none; format_spec=none]/[dynamic source value: fn; conversion=none; format_spec=none]
}
```

## render_tree — source lines 202–202

Source context: callable `render_tree`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `indent; conversion=none; format_spec=none`
- `PurePosixPath(rel).name; conversion=none; format_spec=none`
- `cnt; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:202-202
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: indent; conversion=none; format_spec=none][dynamic source value: PurePosixPath(rel).name; conversion=none; format_spec=none]/ ([dynamic source value: cnt; conversion=none; format_spec=none] files)
}
```

## ext_block — source lines 212–212

Source context: callable `_survey`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `ext; conversion=none; format_spec=f'<16'`
- `n; conversion=none; format_spec=f'>7'`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(
        f"  {ext:<16} {n:>7}" for ext, n in ext_hist.most_common(_EXT_TOP_N)
    )
````

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:212-212
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: ext; conversion=none; format_spec=f'<16'] [dynamic source value: n; conversion=none; format_spec=f'>7']
}
```

## exc_block — source lines 218–218

Source context: callable `_survey`; enclosing call `'\n\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `rel; conversion=none; format_spec=none`
- `txt; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n\n".join(
        f"### {rel}\n```\n{txt}\n```" for rel, txt in excerpts
    )
````

### [dynamic source value: rel; conversion=none; format_spec=none]

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:218-218
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (untyped):

``````text
[dynamic source value: txt; conversion=none; format_spec=none]
``````

```sudo
```

## large_block — source lines 222–222

Source context: callable `_survey`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `sz / 1024; conversion=none; format_spec=f'8.1f'`
- `rel; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(
        f"  {sz / 1024:8.1f} KB  {rel}" for sz, rel in largest
    )
````

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:222-222
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: sz / 1024; conversion=none; format_spec=f'8.1f'] KB [dynamic source value: rel; conversion=none; format_spec=none]
}
```

## _CLIENT_SINK_DETECTORS — source lines 370–370

Source context: callable `<module>`; enclosing call `compile_detectors`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:370-370
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: detector-docwrite-location
}
```

## cache — source lines 379–379

Source context: callable `_client_sink_files`; enclosing call `getattr`; keyword `max_kb`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:379-379
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## vet_config_dedup — source lines 447–448

Source context: callable `vet_config_dedup`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `flag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:447-448
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup veto: model-proposed [dynamic source value: flag; conversion=none; format_spec=none]=false refused; the flag stays enabled
}
```

## vet_config_dedup — source lines 451–451

Source context: callable `vet_config_dedup`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:451-451
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_dedup_flag_veto
}
```

## vet_config_dedup — source lines 462–465

Source context: callable `vet_config_dedup`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `bad; conversion=repr; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:462-465
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup veto: model-proposed exts [dynamic source value: bad; conversion=repr; format_spec=none] refused (key material, language-erasing, and template extensions may not be added to the dedup allowlist)
}
```

## vet_config_dedup — source lines 468–468

Source context: callable `vet_config_dedup`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:468-468
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_dedup_ext_veto
}
```

## vet_overlay — source lines 489–489

Source context: callable `vet_overlay`; enclosing call `log.warning`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:489-489
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: would erase scannable source
}
```

## vet_overlay — source lines 495–495

Source context: callable `vet_overlay`; enclosing call `_errlog.log`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:495-495
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_language_veto
}
```

## vet_overlay — source lines 539–539

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `noun`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:539-539
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: server-side template file(s)
}
```

## vet_overlay — source lines 540–540

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `label`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:540-540
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: template-containment
}
```

## vet_overlay — source lines 541–541

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:541-541
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_template_veto
}
```

## vet_overlay — source lines 542–542

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:542-542
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_template_veto
}
```

## vet_overlay — source lines 543–543

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_files`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:543-543
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_template_files_protected
}
```

## vet_overlay — source lines 544–544

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `errlog_files_key`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:544-544
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: n_template_files
}
```

## vet_overlay — source lines 545–545

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_vendor`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:545-545
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_template_veto_vendor_exempt
}
```

## vet_overlay — source lines 550–550

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `noun`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:550-550
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: key-material file(s)
}
```

## vet_overlay — source lines 551–551

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `label`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:551-551
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: key-material-containment
}
```

## vet_overlay — source lines 552–552

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:552-552
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_key_material_veto
}
```

## vet_overlay — source lines 553–553

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:553-553
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_key_material_veto
}
```

## vet_overlay — source lines 554–554

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_files`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:554-554
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_key_material_files_protected
}
```

## vet_overlay — source lines 555–555

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `errlog_files_key`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:555-555
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: n_key_material_files
}
```

## vet_overlay — source lines 556–556

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_vendor`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:556-556
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_key_material_veto_vendor_exempt
}
```

## vet_overlay — source lines 561–561

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `noun`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:561-561
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: secret-bearing file(s)
}
```

## vet_overlay — source lines 562–562

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `label`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:562-562
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: secret-bearing-containment
}
```

## vet_overlay — source lines 563–563

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:563-563
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_secret_bearing_veto
}
```

## vet_overlay — source lines 564–564

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:564-564
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_secret_bearing_veto
}
```

## vet_overlay — source lines 565–565

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_files`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:565-565
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_secret_bearing_files_protected
}
```

## vet_overlay — source lines 566–566

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `errlog_files_key`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:566-566
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: n_secret_bearing_files
}
```

## vet_overlay — source lines 567–567

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_vendor`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:567-567
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_secret_bearing_veto_vendor_exempt
}
```

## vet_overlay — source lines 572–572

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `noun`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:572-572
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: first-party client file(s) with a DOM sink
}
```

## vet_overlay — source lines 573–573

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `label`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:573-573
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: client-sink-containment
}
```

## vet_overlay — source lines 574–574

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:574-574
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_client_sink_veto
}
```

## vet_overlay — source lines 575–575

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:575-575
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_client_sink_veto
}
```

## vet_overlay — source lines 576–576

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_files`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:576-576
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_client_sink_files_protected
}
```

## vet_overlay — source lines 577–577

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `errlog_files_key`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:577-577
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: n_client_sink_files
}
```

## vet_overlay — source lines 578–578

Source context: callable `vet_overlay`; enclosing call `_run_containment_veto`; keyword `counter_vendor`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:578-578
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_client_sink_veto_vendor_exempt
}
```

## user_prompt — source lines 612–612

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:612-612
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: min_cluster_size
}
```

## run — source lines 700–700

Source context: callable `run`; enclosing call `log.warning`; keyword `remedy`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:700-700
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: scanning with global step1 only
}
```

## run — source lines 704–704

Source context: callable `run`; enclosing call `_errlog.log`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:704-704
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_empty_scope
}
```

## overlay['config_dedup'] — source lines 738–738

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:738-738
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## overlay['config_dedup'] — source lines 742–742

Source context: callable `run`; enclosing call `vet_config_dedup`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:742-742
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## run — source lines 743–743

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:743-743
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## run — source lines 744–744

Source context: callable `run`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:744-744
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## vet_config_dedup — source lines 444–444

Source context: callable `vet_config_dedup`; enclosing call `log.warning`; keyword `key`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `flag; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:444-444
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup.[dynamic source value: flag; conversion=none; format_spec=none]
}
```

## vet_config_dedup — source lines 445–445

Source context: callable `vet_config_dedup`; enclosing call `log.warning`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:445-445
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a credential-bearing config file could be silently dropped as a near-duplicate
}
```

## vet_config_dedup — source lines 449–449

Source context: callable `vet_config_dedup`; enclosing call `_errlog.log`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:449-449
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_dedup_flag_veto
}
```

## vet_config_dedup — source lines 459–459

Source context: callable `vet_config_dedup`; enclosing call `log.warning`; keyword `key`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:459-459
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup.exts
}
```

## vet_config_dedup — source lines 460–460

Source context: callable `vet_config_dedup`; enclosing call `log.warning`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:460-460
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: key material, a scanner-known language or a server-side template is never safe to drop as a near-duplicate
}
```

## vet_config_dedup — source lines 466–466

Source context: callable `vet_config_dedup`; enclosing call `_errlog.log`; keyword `reason`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:466-466
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s1_autoexclude_dedup_ext_veto
}
```

## _veto — source lines 523–525

Source context: callable `_veto`; enclosing call `_errlog.log`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `label; conversion=none; format_spec=none`
- `kind; conversion=none; format_spec=none`
- `entry; conversion=repr; format_spec=none`
- `len(hits); conversion=none; format_spec=none`
- `noun; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:523-525
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: label; conversion=none; format_spec=none] veto: model-proposed [dynamic source value: kind; conversion=none; format_spec=none] exclusion [dynamic source value: entry; conversion=repr; format_spec=none] would remove [dynamic source value: len(hits); conversion=none; format_spec=none] [dynamic source value: noun; conversion=none; format_spec=none]; entry dropped from the overlay
}
```

## dirs — source lines 669–669

Source context: callable `run`; enclosing call `data.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:669-669
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_dirs
}
```

## globs — source lines 677–677

Source context: callable `run`; enclosing call `data.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:677-677
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: exclude_globs
}
```

## run — source lines 711–711

Source context: callable `run`; enclosing call `log.warning`; keyword `dropped`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `100 * (1 - n_after / n_before); conversion=none; format_spec=f'.0f'`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:711-711
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: 100 * (1 - n_after / n_before); conversion=none; format_spec=f'.0f']%
}
```

## run — source lines 712–712

Source context: callable `run`; enclosing call `log.warning`; keyword `remedy`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:712-712
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: re-run with --no-auto-step1 if coverage looks wrong
}
```

## render_tree — source lines 206–206

Source context: callable `render_tree`; enclosing call `lines.extend`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `indent; conversion=none; format_spec=none`
- `k; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:206-206
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: indent; conversion=none; format_spec=none] [dynamic source value: k; conversion=none; format_spec=none]/
}
```

## render_tree — source lines 208–208

Source context: callable `render_tree`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `indent; conversion=none; format_spec=none`
- `len(kids) - _TREE_MAX_CHILDREN; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:208-208
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: indent; conversion=none; format_spec=none] … (+[dynamic source value: len(kids) - _TREE_MAX_CHILDREN; conversion=none; format_spec=none] more)
}
```

## run — source lines 753–753

Source context: callable `run`; enclosing call `extras.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:753-753
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: max_file_kb
}
```

## run — source lines 755–755

Source context: callable `run`; enclosing call `sorted`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:755-755
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: config_dedup
}
```

## dirnames[:] — source lines 147–147

Source context: callable `_survey`; enclosing call `globbed`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `rel_dir; conversion=none; format_spec=none`
- `d; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s1_autoexclude.py:147-147
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: rel_dir; conversion=none; format_spec=none]/[dynamic source value: d; conversion=none; format_spec=none]
}
```

