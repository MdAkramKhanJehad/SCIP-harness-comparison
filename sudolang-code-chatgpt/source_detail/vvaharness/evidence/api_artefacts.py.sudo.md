# vvaharness/evidence/api_artefacts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/api_artefacts.py.evidence.json`. SHA-256: `c99ab182322a68c2d334da96900bba436a308dc9f235c0afc0df66e4fcbc2013`.

```sudo
// Source: vvaharness/evidence/api_artefacts.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import fnmatch; preserve alias and import-time effects. Then Evaluate once ('*openapi*.y*ml', '*openapi*.json', '*swagger*.y*ml', '*swagger*.json', '*.proto', '*.graphql', '*.graphqls', '*.avsc', '*.wsdl', '*.thrift', '*META-INF/*', '*AndroidManifest.xml'); assign in source target order to _API_SURFACE_GLOBS.
// Source: vvaharness/evidence/api_artefacts.py:29-37
// Source signature: gather_api_artefacts(full_files: list[str], max_api_artefacts: int) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gather_api_artefacts(full_files, max_api_artefacts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/evidence/api_artefacts.py:30-31
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then For artefacts, assign []; source annotation list[str].
  // Source: vvaharness/evidence/api_artefacts.py:32-36
  for each rel in full_files {
    // Source: vvaharness/evidence/api_artefacts.py:33-36
    for each g in _API_SURFACE_GLOBS {
      // Source: vvaharness/evidence/api_artefacts.py:34-36
      if (the source predicate fnmatch.fnmatchcase(rel, g) or fnmatch.fnmatchcase(rel.lower(), g) is truthy) {
        // Source: vvaharness/evidence/api_artefacts.py:35-35
        In source order: Evaluate artefacts.append(rel); retain side effects and discard the expression result.
        // Source: vvaharness/evidence/api_artefacts.py:36-36
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
  }
  // Source: vvaharness/evidence/api_artefacts.py:37-37
  End this invocation with artefacts[:max_api_artefacts].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
