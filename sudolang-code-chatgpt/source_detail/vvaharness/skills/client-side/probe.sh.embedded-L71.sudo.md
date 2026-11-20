# vvaharness/skills/client-side/probe.sh

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/skills/client-side/probe.sh.embedded-L71.evidence.json`. SHA-256: `5e88fc2be4fc35952e2476c9ad5dada087841c208112d91381d91a78898bcf66`.

```sudo
// Source: vvaharness/skills/client-side/probe.sh:71-82
In source order: Resolve source import import collections, os, sys; preserve alias and import-time effects. Then Evaluate once sys.argv[1]; assign in source target order to root. Then Evaluate once {'.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs', '.vue', '.svelte', '.html', '.htm', '.ejs', '.hbs', '.handlebars', '.pug', '.jade', '.erb', '.twig', '.mustache'}; assign in source target order to exts. Then Evaluate once {'node_modules', '.git', 'dist', 'build', 'coverage', '.next', 'out', 'vendor', '__pycache__', '.venv', 'bower_components'}; assign in source target order to skip. Then Evaluate once ('package.json', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', '.dockerignore', '.npmrc', 'webpack.config.js', 'vite.config.js', 'vite.config.ts', 'next.config.js', 'next.config.mjs', 'nuxt.config.js', 'angular.json', 'setupProxy.js', 'config.js', 'constants.js', 'constants.ts', 'environment.prod.ts', 'service-worker.js'); assign in source target order to interesting.
// Source: vvaharness/skills/client-side/probe.sh:83-85
In source order: Evaluate once collections.Counter(); assign in source target order to counts. Then Evaluate once collections.Counter(); assign in source target order to dirs. Then Evaluate once []; assign in source target order to files.
// Source: vvaharness/skills/client-side/probe.sh:86-96
for each (dirpath, dirnames, filenames) in os.walk(root) {
  // Source: vvaharness/skills/client-side/probe.sh:87-87
  In source order: Evaluate once [d for d in dirnames if d not in skip]; assign in source target order to dirnames[:].
  // Source: vvaharness/skills/client-side/probe.sh:88-96
  for each name in filenames {
    // Source: vvaharness/skills/client-side/probe.sh:89-90
    In source order: Evaluate once os.path.relpath(os.path.join(dirpath, name), root); assign in source target order to rel. Then Evaluate once os.path.splitext(name)[1].lower(); assign in source target order to ext.
    // Source: vvaharness/skills/client-side/probe.sh:91-93
    if (the source predicate ext in exts and (not name.endswith(('.min.js', '-min.js', '.bundle.js'))) is truthy) {
      // Source: vvaharness/skills/client-side/probe.sh:92-93
      In source order: Apply source augmented assignment counts[ext] += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment dirs[os.sep.join(rel.split(os.sep)[:2])] += 1 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/skills/client-side/probe.sh:94-96
    if (the source predicate name in interesting or name.startswith('.env') or name.startswith('Dockerfile') or name.endswith('.map') is truthy) {
      // Source: vvaharness/skills/client-side/probe.sh:96-96
      In source order: Evaluate files.append(rel); retain side effects and discard the expression result.
    }
  }
}
// Source: vvaharness/skills/client-side/probe.sh:97-102
if (the source predicate counts is truthy) {
  // Source: vvaharness/skills/client-side/probe.sh:98-98
  In source order: Evaluate print('client files: ' + ', '.join(('%s=%d' % kv for kv in counts.most_common()))); retain side effects and discard the expression result.
  // Source: vvaharness/skills/client-side/probe.sh:99-100
  for each (d, n) in dirs.most_common(10) {
    // Source: vvaharness/skills/client-side/probe.sh:100-100
    In source order: Evaluate print('  %6d  %s' % (n, d)); retain side effects and discard the expression result.
  }
}
else {
  // Source: vvaharness/skills/client-side/probe.sh:102-102
  In source order: Evaluate print('client files: (none)'); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/client-side/probe.sh:103-110
if (the source predicate files is truthy) {
  // Source: vvaharness/skills/client-side/probe.sh:104-104
  In source order: Evaluate print('files of interest:'); retain side effects and discard the expression result.
  // Source: vvaharness/skills/client-side/probe.sh:105-106
  for each f in sorted(files)[:30] {
    // Source: vvaharness/skills/client-side/probe.sh:106-106
    In source order: Evaluate print('  ' + f); retain side effects and discard the expression result.
  }
  // Source: vvaharness/skills/client-side/probe.sh:107-108
  if (the source predicate len(files) > 30 is truthy) {
    // Source: vvaharness/skills/client-side/probe.sh:108-108
    In source order: Evaluate print('  ... %d total' % len(files)); retain side effects and discard the expression result.
  }
}
else {
  // Source: vvaharness/skills/client-side/probe.sh:110-110
  In source order: Evaluate print('files of interest: (none)'); retain side effects and discard the expression result.
}
// Source: vvaharness/skills/client-side/probe.sh:111-117
for each lock in ('package-lock.json', 'yarn.lock', 'pnpm-lock.yaml') {
  // Source: vvaharness/skills/client-side/probe.sh:112-114
  if (the source predicate os.path.exists(os.path.join(root, lock)) is truthy) {
    // Source: vvaharness/skills/client-side/probe.sh:113-113
    In source order: Evaluate print('lockfile: ' + lock); retain side effects and discard the expression result.
    // Source: vvaharness/skills/client-side/probe.sh:114-114
    Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
  }
}
Only on normal iterator exhaustion, with no break from this loop {
  // Source: vvaharness/skills/client-side/probe.sh:116-117
  if (the source predicate os.path.exists(os.path.join(root, 'package.json')) is truthy) {
    // Source: vvaharness/skills/client-side/probe.sh:117-117
    In source order: Evaluate print('lockfile: NONE beside package.json -- ^ ranges resolve at build time'); retain side effects and discard the expression result.
  }
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
