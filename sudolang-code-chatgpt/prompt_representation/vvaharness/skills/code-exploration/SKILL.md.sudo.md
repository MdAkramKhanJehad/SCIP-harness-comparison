# vvaharness/skills/code-exploration/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Inventory, pagination, graph limitations and completion

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:24-285
Constraints {
  This is requested coverage work before a lens or an absence conclusion, not a vulnerability lens itself.
  Requested first operation: Glob **/* including dotfiles, then write counted directory groups whose sum equals the inventory.
  if (Glob shows its 500-hit truncation marker) { The model is asked to narrow by subtree until each group is complete. }
  if (Read refuses an excluded path) { The requested coverage state is excluded, not clean or read. }
  The graph's file-node list must not replace Glob; dotfiles/templates/config may be outside graph coverage.
  The requested inventory includes the source-listed templates, deployment/CI/config, manifests, dotfiles/env, SQL/migrations/seeds, assets and package/base/helper files; examples illustrate shapes, not paths/results in the target repository.
  Requested findings need a written inventory, an EOF-complete read, a real relative span and one most-specific CWE; absence claims name the files searched for controls.
  while (the requested Read still shows truncation) {
    The model is asked to continue from the last displayed line number as the zero-based offset.
  }
  A past-EOF marker or short untruncated page is the source's usual completion indication.
  if (the underlying 800000-character decode window or 200000-character page cap makes apparent EOF unreliable) {
    The model is asked to grep for an expected late construct and record partial coverage if pages never reached it.
  }
  Requested scope expansion follows handlers to templates/models/bases/migrations/serializers/config and template parents; graph calls use exact source signatures.
  if (a live module has no module-level importer in the graph) { The model is asked to inspect __init__.py/function-local registration rather than conclude it is dead. }
  Requested FP checks inspect shared controls, actual escaping, shipped/example/fixture status, constants and unfinished reads.
  Separate requested sites/classes are not collapsed; weak-hash writers are distinguished from verifier hits and same-construct duplicates.
  Before stopping, the model is asked to compute inventory minus EOF-read files.
  if (that difference is empty OR every remaining member is named with a reason) { The source permits ending exploration. }
  else { The requested state is still mid-pass. }
  Closing coverage includes counts, unfinished names/reasons and open/closed directory groups. Deadlines/size/binary/exclusion are disclosed, not silently treated as clean.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:1-4
Constraints {
  The source declares name = "code-exploration". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Exhaustive repository exploration procedure — Glob the whole tree into a written inventory, group it by directory, and account for every file including templates, Dockerfiles, compose and k8s manifests, nginx/uwsgi/gunicorn config, CI workflows, dotfiles, SQL migrations, static assets and __init__.py. Load FIRST, before any lens, when you are asked to map a repository, enumerate its attack surface, find entry points, decide what is in scope, or conclude that something is absent. Covers reading paginated files to the last line, following handler-to-template and handler-to-model edges with GraphImporters / GraphNeighbors, and reporting coverage gaps honestly.". Tool lists here describe the request profile; source loaders determine actual grants.
  The request retains this source rule, criterion or rationale, with its original modal force: Exhaustive repository exploration procedure — Glob the whole tree into a written inventory, group it by directory, and account for every file including templates, Dockerfiles, compose and k8s manifests, nginx/uwsgi/gunicorn config, CI workflows, dotfiles, SQL migrations, static assets and __init__.py. Load FIRST, before any lens, when the model are asked to map a repository, enumerate its attack surface, find entry points, decide what is in scope, or conclude that something is absent. Covers reading paginated files to the last line, following handler-to-template and handler-to-model edges with GraphImporters / GraphNeighbors, and reporting coverage gaps honestly.
}
```

# Exhaustive Repository Exploration

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:24-26
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: This is not a vulnerability lens.
  The request retains this source rule, criterion or rationale, with its original modal force: It is the coverage procedure every lens runs on top of.
  The request retains this source rule, criterion or rationale, with its original modal force: A lens pointed at 38% of a repository finds at most 38% of its bugs, and reports that fraction in the confident tone of a complete answer.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:28-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: > About the examples below. Every path, line number and snippet in this document is an > *illustration of a shape*, drawn from patterns that recur across web applications.
  The request retains this source rule, criterion or rationale, with its original modal force: None of > them is a claim about the repository the model are scanning.
  The requested model behavior excludes go looking for `app.py` or > `routes/` because this file mentions them, and never report a finding you have not read in > the tree in front of you. `Glob` tells you what actually exists; this document only tells > you where to look and what the answer tends to look like.
}
```

## The measured failure

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:37-43
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: This procedure exists because of a repeated, measured result.
  The request retains this source rule, criterion or rationale, with its original modal force: On a small Python web application, an unaided threat-modelling pass could name only 17 paths — 38% of the 44 files it claimed to have accounted for, while `Glob **/*` returned 45. 27 files were invisible to it: every HTML template, the entry module itself, `Dockerfile`, `docker-compose.yml`, the nginx and uwsgi config, and every `__init__.py`.
  The request retains this source rule, criterion or rationale, with its original modal force: On a second application of 23 files, only 7 paths (30%) were nameable and an entire `frontend/` tree of 14 files was never opened.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:45-46
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Those gaps are where findings hide, and the two shapes below are why.
  The request retains this source rule, criterion or rationale, with its original modal force: Both are invisible to a `*.py`-only sweep, and both were missed for the same reason: nobody opened the file.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:48-53
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A tiny entry module carries the worst of it. A 34-line module can hold both `app.secret_key = "super secret key"` — the key that signs every session cookie — and a 404 handler that does `render_template_string(f"{error}.
  The request retains this source rule, criterion or rationale, with its original modal force: Requested URL was {request.path}")`, compiling an attacker-controlled request path as a Jinja template.
  The request retains this source rule, criterion or rationale, with its original modal force: Two classes, two CWEs, one file short enough that it reads as boilerplate.
  The request retains this source rule, criterion or rationale, with its original modal force: The WSGI config (`module = app:app` in a `uwsgi.ini`) is what tells the model that file is the live entry point.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:54-61
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The client names the victim, in a file the backend sweep never opens. A frontend component decodes the JWT it already holds — `const userId = JSON.parse(atob(token.split('.')[1])).user_id` — and POSTs that id in the request body.
  The request retains this source rule, criterion or rationale, with its original modal force: The handler then does `user_id = data.get('user_id')` → `User.query.get(user_id)` → `user.set_password(...)`, never reading the authenticated principal its `@token_required` decorator bound one line earlier.
  The request retains this source rule, criterion or rationale, with its original modal force: The unread frontend file is the proof that the id is client-supplied and trivially swappable; without it the handler looks like it is merely trusting its own input.
}
```

## HARD GATE — every finding you emit from this pass requires all four

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:65-66
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: An inventory exists, written down, before any conclusion. The `Glob` output, grouped by directory, with a count.
  The request retains this source rule, criterion or rationale, with its original modal force: Not "I looked around".
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:67-68
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The file was opened and read to its last line. Not a `Grep` hit with two lines of context.
  The request retains this source rule, criterion or rationale, with its original modal force: Not the first page of a paginated `Read`.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:69-70
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A repo-relative path and a real `line_start..line_end` copied from the numbered `Read` output, plus exactly one most-specific CWE id.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:71-73
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: For any absence claim — no auth, no escaping, no rate limit, no TLS — name the files the model opened looking for the control.
  The request retains this source rule, criterion or rationale, with its original modal force: An absence asserted against an unread directory is not a finding, it is the shape of one.
}
```

## 1. Enumerate before you read

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `Glob` first, always, and never start from the file the model were handed.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:79-81
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (untyped):

``````text
**/*            → every path, dotfiles included; this is the inventory
``````

```sudo
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:83-84
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Then split the inventory by directory and write the group list down as the model's plan.
  The request retains this source rule, criterion or rationale, with its original modal force: The shape of that plan, for a mid-sized Flask-style application, is a census like:
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:86-89
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (untyped):

``````text
<root> (11)  routes/ (7)  templates/ (9)  templates/partials/ (2)
models/ (5)  forms/ (6)   utils/ (3)      conf/ (1)  static/ (1)     = 45
``````

```sudo
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:91-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Mark each group open or closed as the model go, and make the counts sum to the inventory size.
  The request retains this source rule, criterion or rationale, with its original modal force: The sum is the point: a census that does not add up is a census with a directory missing from it.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:94-96
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Coverage is the set difference between the inventory and the set of files the model have opened. Compute it explicitly before the model stop.
  The requested conditional/temporal rule is: If the difference is non-empty the model are not done, the model are mid-pass.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:98-98
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Three ways the inventory itself lies, all of which the model must check for:
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:100-102
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `Glob` truncates at 500 hits, appending `... (N more)`.
  The requested conditional/temporal rule is: If the model see that line, your inventory is a prefix — narrow by subtree (`routes/`, `frontend/`) until every group returns whole.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:103-106
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Scope exclusions are invisible in `Glob` but loud in `Read`. A path outside the scan scope returns `ERROR: path '<p>' is excluded from the scan scope (not in the scanned file inventory)`.
  The request retains this source rule, criterion or rationale, with its original modal force: That is a third state, neither read nor unread — record it as excluded, not as clean.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:107-110
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes substitute a graph node list for the inventory. The graph walk skips the entire dot-namespace — files like `.dockerignore`, `.prettierrc` and `.pylintrc` exist in the tree and none is a file node. `Glob` returns them.
  The request retains this source rule, criterion or rationale, with its original modal force: Glob is the inventory; the graph is an index over part of it.
}
```

## 2. The file classes a source-only sweep skips

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:114-115
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Each of these carries findings and each is invisible to a `*.py` / `*.java` / `*.js` sweep.
  The request retains this source rule, criterion or rationale, with its original modal force: Glob them by name.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:117-124
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Templates and views — `**/*.html`, `**/*.jinja2`, `**/*.j2`, `**/*.jsx`, `**/*.tsx`, `**/*.vue`, `**/*.erb`, `**/*.jsp`, `**/*.twig`, `**/*.hbs`, `**/*.ejs`, `**/*.blade.php`.
  The request retains this source rule, criterion or rationale, with its original modal force: The escape decision lives here, not in the handler. `Grep` templates for `| safe`, `safe_columns`, `autoescape false`, `{{{`, `html_safe`, `raw(`, `dangerouslySetInnerHTML`, `v-html`.
  The request retains this source rule, criterion or rationale, with its original modal force: That grep is usually short — a handful of lines across the whole template tree — and each line it returns is a location where escaping was switched off deliberately, in the form `{{ note.text | safe }}` or `render_table(rows, safe_columns=['text'])`.
  The request retains this source rule, criterion or rationale, with its original modal force: Short is not the same as empty: read every hit.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:126-133
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Container and orchestration — `Dockerfile*`, `**/Dockerfile`, `docker-compose*.y*ml`, `**/*.tf`, `**/*.tfvars`, `k8s/`, `/*deployment*.y*ml`, `/values.yaml`, `/templates/*.yaml` (Helm), `Procfile`, `uwsgi.ini`, `gunicorn.conf.py`, `**/nginx*.conf`, `**/conf/*.conf`, `supervisord.conf`, `**/*.service`.
  The request retains this source rule, criterion or rationale, with its original modal force: These compose into single findings that no one file states.
  The request retains this source rule, criterion or rationale, with its original modal force: A reverse-proxy config whose only listener is `listen 80 default_server` with `uwsgi_pass` behind it and not one `ssl` token in the file; a compose file publishing `ports: - 5000:80`; a `Dockerfile` whose `CMD` starts that proxy — four files, one cleartext -transport finding, zero of them `.py`.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:135-137
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CI/CD — `.github/**`, `.gitlab-ci.yml`, `Jenkinsfile*`, `azure-pipelines.yml`, `.circleci/config.yml`, `bitbucket-pipelines.yml`.
  The model is asked to obtain and examine for `pull_request_target`, unpinned third-party actions, `${{ github.event.* }}` interpolated into `run:`, secrets echoed to logs.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:139-142
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Dependency manifests — `requirements*.txt`, `pyproject.toml`, `Pipfile*`, `poetry.lock`, `package.json`, `*-lock.json`, `yarn.lock`, `pom.xml`, `build.gradle*`, `go.mod`, `Gemfile*`, `*.csproj`.
  The request retains this source rule, criterion or rationale, with its original modal force: Unpinned or ancient versions are findings; the manifest is also how the model learn which framework defaults apply.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:144-147
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Dotfiles and env templates — `.env*`, `*.env.example`, `.dockerignore`, `.npmrc`, `.netrc`, `.pylintrc`, `.prettierrc`, `.git-credentials`, `/.aws/`.
  The request retains this source rule, criterion or rationale, with its original modal force: Committed real values are credential findings, and `.dockerignore` is how the model learn what a broad `COPY . /srv/app` in the `Dockerfile` did *not* exclude from the image.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:149-150
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SQL and migrations — `**/*.sql`, `migrations/`, `alembic/versions/`, `db_seed.py`, `/fixtures/`, `/seeds/`.
  The request retains this source rule, criterion or rationale, with its original modal force: Seed files ship default credentials into running systems.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:152-153
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Static assets — `static/`, `public/`, `assets/`, `/*.map`.
  The request retains this source rule, criterion or rationale, with its original modal force: Source maps, API keys in bundled JS, backup files served by the static handler.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:155-158
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `__init__.py`, base classes, shared helpers — `/__init__.py`, `/base*.py`, `**/base_*.py`, `**/middleware*`, `/conftest.py`, `/utils/**`.
  The request retains this source rule, criterion or rationale, with its original modal force: This is where centrally-applied controls live, and where their absence is centrally fatal.
  The request retains this source rule, criterion or rationale, with its original modal force: Four shapes to expect:
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:160-162
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A package `__init__.py` whose entire body is `import routes.<name>` statements inside a `def init():` called once from the entry module. That is the route registration, so a route table reconstructed without it is short every module it names.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:163-164
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: An `__init__.py` that builds the engine — `create_engine('sqlite:///' + ..., echo=True)` — logging every SQL statement, including the ones carrying credentials.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:165-166
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: An `__abstract__ = True` base model supplying `id` and `created_at` to every subclass.
  The model is asked to obtain and examine it before claiming any model lacks either.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:167-170
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A base template: one read of it settles a control for every template that `extends` it.
  The requested conditional/temporal rule is: If its `{% block head %}` holds three `<meta>` tags and none is a `Content-Security-Policy`, that is one finding covering the whole tree — and the model only know it because the model opened the parent.
}
```

## 3. READ TO THE END

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:174-176
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `Read` is paginated — `read(file_path, offset=0, limit=2000)` — and its output is byte-capped, so a large file returns a prefix.
  The request retains this source rule, criterion or rationale, with its original modal force: A file read halfway produces exactly the same false "absent" conclusion as a file never read, and produces it with more confidence.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:178-180
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Watch the tail of every `Read` for `... [truncated]` or `…[truncated N chars to fit context — re-read a specific line range with Read offset/limit if the model need more]`.
  The request retains this source rule, criterion or rationale, with its original modal force: Either marker means the model hold a prefix.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:181-183
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Continue from the last line number the model were shown. `offset` is a 0-based line index and output is `cat -n` style, so a first page ending at displayed line 2000 continues at `offset: 2000`.
  The request retains this source rule, criterion or rationale, with its original modal force: Repeat until the tail carries no truncation marker.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:184-186
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to establish you reached the end: a `Read` whose `offset` is past the final line returns `(file is empty or offset past EOF)`.
  The request retains this source rule, criterion or rationale, with its original modal force: That, or a page shorter than `limit` with no truncation marker, is the proof the file is finished.
  The request retains this source rule, criterion or rationale, with its original modal force: Assumption is not proof.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:187-191
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One exception, and it is a trap. The reader only decodes the first 800,000 characters of a file and caps each rendered page at 200,000.
  The request retains this source rule, criterion or rationale, with its original modal force: On a file larger than that, the EOF marker is a *false* end-of-file — it means the model exhausted the window, not the file. `Grep` the file for a construct the model expect near its end; if it hits at a line the model's pages never reached, record the file as partially read in the model's coverage report.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:192-193
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Narrow with `offset`/`limit` only *after* the model have seen the whole file once. `Grep` is for locating, never for concluding.
}
```

## 4. Follow the edges

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:197-198
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The inventory tells the model what exists; the edges tell the model what a file the model just read pulls into scope.
  The request retains this source rule, criterion or rationale, with its original modal force: Both are mandatory.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:200-203
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A handler that renders a template puts that template in scope. A handler that builds `text(f"text like '%{search_param}%'")` into a query is one finding; the template it then renders, marking that same column as `safe_columns=['text']`, is a second one in a different file.
  The model is asked to obtain and examine the handler, miss a class; read both, get two findings.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:204-205
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A model the handler writes puts that model in scope — and its base class, its migration, and any serializer that returns it.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:206-207
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A config key a handler reads puts the config file in scope; a template that `extends` or `include`s another puts the parent in scope.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:208-214
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to adopt the graph with its real signatures; do not guess. `GraphImporters(file)` → the files that import `file`. `GraphNeighbors(file, function)` → `{"callers": [...], "callees": [...]}`; it needs BOTH arguments, an exact path and an exact function name. `GraphCommunityOf(file)` → the module name, which you then hand to `GraphSinksInCommunity(community)` for the sinks already known in that cluster. `CweGuidance(cwe_id)` once you have a class in hand.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:215-219
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: An empty graph answer is a signal, not an all-clear. `GraphImporters` reads module-level import edges only.
  The request retains this source rule, criterion or rationale, with its original modal force: A module imported from inside a function body — the `def init():` registration shape above — has no module-level importer, so the graph correctly reports none while the module is plainly live.
  The requested conditional/temporal rule is: When the graph says a live module has no importer, go read the `__init__.py` yourself.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:220-221
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Graph hits *add to* the inventory-driven sweep, never replace it.
  The request retains this source rule, criterion or rationale, with its original modal force: Templates, YAML, `.conf` and dotfiles are reachable only by `Glob`.
}
```

## FP CHECKS — what refutes a finding from this pass

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:225-225
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Refute and say so; a refutation with a named search is a result.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:227-230
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The control exists somewhere the model had not read. Before claiming a missing guard, open `/__init__.py`, the base class, the blueprint/router registration, `/middleware*`, and the reverse-proxy config.
  The request retains this source rule, criterion or rationale, with its original modal force: A `before_request`, a decorator applied at blueprint level, or an nginx `auth_request` refutes it.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:231-233
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The template escapes after all. Jinja and ERB autoescape by default.
  The request retains this source rule, criterion or rationale, with its original modal force: Only an explicit `| safe`, `safe_columns=`, `autoescape=False`, `{{{`, `raw()`, `html_safe`, `v-html` or `dangerouslySetInnerHTML` defeats it.
  The request retains this source rule, criterion or rationale, with its original modal force: No such marker → no XSS from that render.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:234-237
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The file is not shipped. `.dockerignore` / `.gitignore` excludes it from the image, it lives under `tests/`, or it is documentation (`docs/`, `course/`, `*.md`).
  The request retains this source rule, criterion or rationale, with its original modal force: Prose describing a vulnerability is not the vulnerability — do not report a write-up of a bug as the bug.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:238-239
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The config is an example. `*.example`, `*.sample`, `*.template` with placeholder values are not credential leaks.
  The request retains this source rule, criterion or rationale, with its original modal force: Real-looking values in a live `.env` or a seed script are.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:240-240
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The value is a fixed literal, not attacker-varied.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:241-242
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model only read a prefix. If the model cannot state that the model reached the last line, the finding is not gated yet.
  The request retains this source rule, criterion or rationale, with its original modal force: Finish the read.
}
```

## ENUMERATION RULE

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:246-248
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One finding per distinct site, each with its own file and its own line span. Three templates disabling escaping on the same field is three findings, at three template paths, because each is an independent edit a fix must make.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:250-256
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The same rule survives contact with a noisy grep.
  The request retains this source rule, criterion or rationale, with its original modal force: Sweeping a weak-hash call across a backend typically returns a mix the model must sort, not a count the model can report: a `set_password` that does `self.password_hash = hashlib.md5(password.encode()).hexdigest()`, the identical expression inlined into a registration handler in another file, and the verifier that compares against that same digest.
  The request retains this source rule, criterion or rationale, with its original modal force: The first two are two independent password-writing sites, so two findings at two anchors in two files.
  The request retains this source rule, criterion or rationale, with its original modal force: The third is a hit to judge — it reads the digest rather than writing it — not a third finding to bank.
  The request retains this source rule, criterion or rationale, with its original modal force: State which the model counted and why.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:258-261
Constraints {
  The requested model behavior excludes collapse sites into an omnibus "output encoding missing across templates" or "insecure deployment configuration".
  The request retains this source rule, criterion or rationale, with its original modal force: A blanket finding can be credited, tracked and fixed exactly once, so the remaining sites ship.
  The request retains this source rule, criterion or rationale, with its original modal force: Equally: do not pad — the *same* construct reported twice is a duplicate, not coverage.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:263-265
Constraints {
  The requested conditional/temporal rule is: Before leaving a file the model have already read, ask what *else* is wrong with it.
  The request retains this source rule, criterion or rationale, with its original modal force: The entry-module shape at the top of this document is the reminder: a hardcoded signing key and an SSTI sink can share one short file.
  The request retains this source rule, criterion or rationale, with its original modal force: Two classes, two CWEs, two findings, one file the model already had open.
}
```

## Report coverage honestly

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:269-269
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Close the pass with the arithmetic:
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:271-271
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Inventory size, files opened, files read to the end, files refused as out of scope.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:272-274
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The named list of what the model did not finish, and why — deadline, size, binary, excluded.
  The request retains this source rule, criterion or rationale, with its original modal force: A vendored minified asset skipped as vendored is a fine entry. `frontend/ (14 files) not read — ran out of turns` is a fine entry.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:275-275
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Which directory groups are closed and which are open.
}
```

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:277-278
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A visible gap is recoverable: the next agent, or the next stage, picks it up.
  The request retains this source rule, criterion or rationale, with its original modal force: A silent gap is permanent, and in the output it is indistinguishable from clean coverage.
}
```

## The inventory decides when you are done

```sudo
// Source: vvaharness/skills/code-exploration/SKILL.md:282-285
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Not intuition, not "I have enough for a good report", not the point at which findings stop arriving.
  The request retains this source rule, criterion or rationale, with its original modal force: Exploration ends when the set difference between the inventory and the files the model have read to the end is empty, or when every remaining element of it is listed in the model's coverage report with a reason.
  The request retains this source rule, criterion or rationale, with its original modal force: Those are the only two endings.
}
```

