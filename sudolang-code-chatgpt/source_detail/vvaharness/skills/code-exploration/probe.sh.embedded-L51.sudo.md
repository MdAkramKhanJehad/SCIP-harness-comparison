# vvaharness/skills/code-exploration/probe.sh

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/skills/code-exploration/probe.sh.embedded-L51.evidence.json`. SHA-256: `e0f6d249a55423d66c5885bd98a18c8097ce30fe1ab4efeec07f8afe2e75b59e`.

```sudo
// Source: vvaharness/skills/code-exploration/probe.sh:51-55
In source order: Resolve source import import fnmatch, os, sys; preserve alias and import-time effects. Then Resolve source import from collections import Counter; preserve alias and import-time effects. Then Evaluate once set(sys.argv[1].split()); assign in source target order to prune. Then Evaluate once ([], []); assign in source target order to (files, pruned).
// Source: vvaharness/skills/code-exploration/probe.sh:56-65
for each (dirpath, dirnames, filenames) in os.walk('.') {
  // Source: vvaharness/skills/code-exploration/probe.sh:57-57
  In source order: Evaluate once []; assign in source target order to keep.
  // Source: vvaharness/skills/code-exploration/probe.sh:58-62
  for each d in sorted(dirnames) {
    // Source: vvaharness/skills/code-exploration/probe.sh:59-62
    if (the source predicate d in prune is truthy) {
      // Source: vvaharness/skills/code-exploration/probe.sh:60-60
      In source order: Evaluate pruned.append(os.path.join(dirpath, d)[2:]); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/skills/code-exploration/probe.sh:62-62
      In source order: Evaluate keep.append(d); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/skills/code-exploration/probe.sh:63-63
  In source order: Evaluate once keep; assign in source target order to dirnames[:].
  // Source: vvaharness/skills/code-exploration/probe.sh:64-65
  for each f in sorted(filenames) {
    // Source: vvaharness/skills/code-exploration/probe.sh:65-65
    In source order: Evaluate files.append(os.path.join(dirpath, f)[2:]); retain side effects and discard the expression result.
  }
}
// Source: vvaharness/skills/code-exploration/probe.sh:67-69
In source order: Evaluate once Counter((os.path.dirname(p) or '<root>' for p in files)); assign in source target order to groups. Then Evaluate print(); retain side effects and discard the expression result. Then Evaluate print('== INVENTORY (%d files, %d directory groups; authoritative, not truncated) ==' % (len(files), len(groups))); retain side effects and discard the expression result.
// Source: vvaharness/skills/code-exploration/probe.sh:70-71
for each (d, n) in sorted(groups.items(), key=lambda kv: (-kv[1], kv[0]))[:40] {
  // Source: vvaharness/skills/code-exploration/probe.sh:71-71
  In source order: Evaluate print('%6d  %s' % (n, d)); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:72-73
if (the source predicate len(groups) > 40 is truthy) {
  // Source: vvaharness/skills/code-exploration/probe.sh:73-73
  In source order: Evaluate print('  ... (%d more directory groups)' % (len(groups) - 40)); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:74-75
if (the source predicate pruned is truthy) {
  // Source: vvaharness/skills/code-exploration/probe.sh:75-75
  In source order: Evaluate print('PRUNED SUBTREES (not counted above): %s' % ', '.join(sorted(set(pruned))[:12])); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:77-116
In source order: Evaluate once [('TEMPLATES AND VIEWS', ['*.html', '*.htm', '*.jinja', '*.jinja2', '*.j2', '*.jsx', '*.tsx', '*.vue', '*.erb', '*.jsp', '*.jspx', '*.twig', '*.hbs', '*.handlebars', '*.ejs', '*.blade.php', '*.mustache', '*.pug', '*.haml', '*.svelte', '*.astro'], []), ('CONTAINER / ORCHESTRATION / IaC', ['Dockerfile*', '*.dockerfile', 'Containerfile*', 'docker-compose*.yml', 'docker-compose*.yaml', 'compose.yml', 'compose.yaml', '*.tf', '*.tfvars', '*.tfstate', 'Procfile', 'uwsgi.ini', 'gunicorn*.py', '*nginx*.conf', '*.conf', 'supervisord.conf', '*.service', '*.socket', 'Vagrantfile', '*deployment*.yml', '*deployment*.yaml', 'values.yaml', 'Chart.yaml', 'kustomization.yml', 'kustomization.yaml', '*.pp'], ['k8s', 'kubernetes', 'helm', 'charts', 'deploy', 'ansible', '.ebextensions', 'terraform']), ('CI / CD', ['.gitlab-ci.yml', 'Jenkinsfile*', 'azure-pipelines*.yml', '.travis.yml', '.drone.yml', 'bitbucket-pipelines.yml', 'cloudbuild.yml', 'cloudbuild.yaml', 'buildspec.yml', 'buildspec.yaml', 'Makefile', '*.mk'], ['.github', '.circleci', '.buildkite']), ('DEPENDENCY MANIFESTS', ['requirements*.txt', 'pyproject.toml', 'setup.py', 'setup.cfg', 'Pipfile', 'Pipfile.lock', 'poetry.lock', 'uv.lock', 'package.json', 'package-lock.json', '*-lock.json', 'yarn.lock', 'pnpm-lock.yaml', 'pom.xml', 'build.gradle', 'build.gradle.kts', 'go.mod', 'go.sum', 'Gemfile', 'Gemfile.lock', '*.csproj', '*.fsproj', 'Cargo.toml', 'Cargo.lock', 'composer.json', 'composer.lock'], []), ('ENV / CREDENTIAL-SHAPED DOTFILES', ['.env', '.env.*', '*.env', '*.env.example', '.dockerignore', '.npmrc', '.netrc', '.pypirc', '.git-credentials', '.gitconfig', '.htpasswd', '.htaccess', '*.pem', '*.key', '*.p12', '*.jks', '*.keystore', 'id_rsa*', '*.ovpn', 'credentials*'], ['.aws', '.ssh', '.docker', '.gnupg', '.kube']), ('SQL / MIGRATIONS / SEEDS', ['*.sql', '*.db', '*.sqlite', '*.sqlite3', 'db_seed*', 'seed*.py', '*fixture*.sql', '*.dump', '*.bak'], ['migrations', 'alembic', 'seeds', 'seed']), ('STATIC / BUILT ASSETS', ['*.map', '*.min.js', '*.min.css'], ['static', 'public', 'assets', 'dist', 'wwwroot', 'staticfiles']), ('CENTRAL CONTROLS (__init__, base, middleware, utils)', ['__init__.py', 'base.py', 'base_*.py', 'base*.py', 'middleware.py', 'middleware*.py', 'middlewares.py', 'conftest.py', 'decorators.py', '*decorator*.py', 'permissions.py', 'authz*.py', 'security*.py', 'app.py', 'wsgi.py', 'asgi.py', 'main.py', 'settings.py', 'config.py', 'urls.py', 'routes.py'], ['utils', 'util', 'helpers', 'common', 'middleware', 'middlewares'])]; assign in source target order to CLASSES.
// Source: vvaharness/skills/code-exploration/probe.sh:118-125
// Source signature: hits(basenames, dirs)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn hits(basenames, dirs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/skills/code-exploration/probe.sh:119-119
  In source order: Evaluate once []; assign in source target order to out.
  // Source: vvaharness/skills/code-exploration/probe.sh:120-124
  for each p in files {
    // Source: vvaharness/skills/code-exploration/probe.sh:121-122
    In source order: Evaluate once os.path.basename(p); assign in source target order to b. Then Evaluate once p.split(os.sep)[:-1]; assign in source target order to parts.
    // Source: vvaharness/skills/code-exploration/probe.sh:123-124
    if (the source predicate any((fnmatch.fnmatch(b, g) for g in basenames)) or any((x in dirs for x in parts)) is truthy) {
      // Source: vvaharness/skills/code-exploration/probe.sh:124-124
      In source order: Evaluate out.append(p); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/skills/code-exploration/probe.sh:125-125
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:127-137
for each (label, basenames, dirs) in CLASSES {
  // Source: vvaharness/skills/code-exploration/probe.sh:128-130
  In source order: Evaluate once hits(basenames, dirs); assign in source target order to found. Then Evaluate print(); retain side effects and discard the expression result. Then Evaluate print('== %s (%d) ==' % (label, len(found))); retain side effects and discard the expression result.
  // Source: vvaharness/skills/code-exploration/probe.sh:131-133
  if (the source predicate not found is truthy) {
    // Source: vvaharness/skills/code-exploration/probe.sh:132-132
    In source order: Evaluate print('(none)'); retain side effects and discard the expression result.
    // Source: vvaharness/skills/code-exploration/probe.sh:133-133
    Continue the immediately enclosing source loop at its next iteration.
  }
  // Source: vvaharness/skills/code-exploration/probe.sh:134-135
  for each p in found[:15] {
    // Source: vvaharness/skills/code-exploration/probe.sh:135-135
    In source order: Evaluate print('  ' + p); retain side effects and discard the expression result.
  }
  // Source: vvaharness/skills/code-exploration/probe.sh:136-137
  if (the source predicate len(found) > 15 is truthy) {
    // Source: vvaharness/skills/code-exploration/probe.sh:137-137
    In source order: Evaluate print('  ... (%d more)' % (len(found) - 15)); retain side effects and discard the expression result.
  }
}
// Source: vvaharness/skills/code-exploration/probe.sh:139-141
In source order: Evaluate once [p for p in files if any((x.startswith('.') for x in p.split(os.sep)))]; assign in source target order to dots. Then Evaluate print(); retain side effects and discard the expression result. Then Evaluate print('== ALL DOTFILES (%d) -- the namespace the graph walk skips entirely ==' % len(dots)); retain side effects and discard the expression result.
// Source: vvaharness/skills/code-exploration/probe.sh:142-143
if (the source predicate not dots is truthy) {
  // Source: vvaharness/skills/code-exploration/probe.sh:143-143
  In source order: Evaluate print('(none)'); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:144-145
for each p in dots[:20] {
  // Source: vvaharness/skills/code-exploration/probe.sh:145-145
  In source order: Evaluate print('  ' + p); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:146-147
if (the source predicate len(dots) > 20 is truthy) {
  // Source: vvaharness/skills/code-exploration/probe.sh:147-147
  In source order: Evaluate print('  ... (%d more)' % (len(dots) - 20)); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:149-152
In source order: Evaluate once [p for p in files if os.path.exists(p) and os.path.getsize(p) == 0]; assign in source target order to empty. Then Evaluate print(); retain side effects and discard the expression result. Then Evaluate print('== ZERO-BYTE FILES (%d) ==' % len(empty)); retain side effects and discard the expression result. Then Evaluate once empty[:10]; assign in source target order to emptyshown.
// Source: vvaharness/skills/code-exploration/probe.sh:153-154
if (the source predicate not emptyshown is truthy) {
  // Source: vvaharness/skills/code-exploration/probe.sh:154-154
  In source order: Evaluate print('(none)'); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:155-156
for each p in emptyshown {
  // Source: vvaharness/skills/code-exploration/probe.sh:156-156
  In source order: Evaluate print('  ' + p); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/code-exploration/probe.sh:157-158
if (the source predicate len(empty) > 10 is truthy) {
  // Source: vvaharness/skills/code-exploration/probe.sh:158-158
  In source order: Evaluate print('  ... (%d more)' % (len(empty) - 10)); retain side effects and discard the expression result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
