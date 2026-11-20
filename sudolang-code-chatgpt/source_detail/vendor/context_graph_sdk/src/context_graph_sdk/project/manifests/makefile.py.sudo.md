# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py.evidence.json`. SHA-256: `bb9501dea220276dcfd4985c8e65d65869506d52ca67ad8f5f0115970cb84ef5`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:15-37
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.project.config import BuildProcessRecord, ManifestReader, ProjectConfig; preserve alias and import-time effects. Then Evaluate once frozenset({'build', 'test', 'lint', 'format', 'fmt', 'check', 'clean', 'install', 'dev', 'run', 'release'}); assign in source target order to HIGH_SIGNAL_TARGETS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:41-41
In source order: Evaluate once re.compile('^([^\\t:=#][^:=]*):(?:[^=]|$)'); assign in source target order to _RULE_LINE.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:44-57
// Source signature: load_makefile_processes(reader: ManifestReader, config: ProjectConfig) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_makefile_processes(reader, config) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:45-57
  for each relative in reader.by_base_name('Makefile', 'GNUmakefile', 'BSDmakefile') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:46-46
    In source order: Evaluate once reader.read_text(relative); assign in source target order to text.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:47-48
    if (the source predicate text is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:48-48
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:49-57
    for each line in text.split(source_literal_49_31) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:50-50
      In source order: Evaluate once _RULE_LINE.match(line.rstrip('\r')); assign in source target order to match.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:51-52
      if (the source predicate match is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:52-52
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:53-57
      for each target in match.group(1).split() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:54-57
        if (the source predicate target in HIGH_SIGNAL_TARGETS is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py:55-57
          In source order: Evaluate config.add_build_process(BuildProcessRecord(target, relative, 'make', source_template_56_69)); retain side effects and discard the expression result.
        }
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.project.config import BuildProcessRecord, ManifestReader, ProjectConfig` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/config.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py.sudo.md). Exact strings in the evidence asset support this conversion.
