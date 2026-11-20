# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py.evidence.json`. SHA-256: `3816bc8afad6ac1a9bb5b80d0fb0307b8f5d423c4f64a68285bb952bbb3490d5`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ProjectConfig; preserve alias and import-time effects. Then Evaluate once re.compile('^\\s*gem\\s+[\'\\"]([^\'\\"]+)[\'\\"](?:\\s*,\\s*[\'\\"]([^\'\\"]+)[\'\\"])?'); assign in source target order to _GEM_LINE.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:26-38
// Source signature: load_gemfile_dependencies(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_gemfile_dependencies(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:27-38
  for each relative in reader.by_base_name('Gemfile') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:28-29
    if (the source predicate relative != 'Gemfile' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:29-29
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:30-30
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:31-32
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:32-32
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:33-38
    for each line in text.split(source_literal_33_31) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:34-34
      In source order: Evaluate once _GEM_LINE.match(line); assign in source target order to match.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:35-38
      if (the source predicate match is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py:36-38
        In source order: Evaluate config.add_dependency(DependencyRecord(match.group(1), match.group(2) or '', relative)); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import DependencyRecord, ManifestReader, ProjectConfig` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.
