# vvaharness/detect/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/detect/__init__.py.evidence.json`. SHA-256: `6214943259681ec81ec1d5949cc7e2941d5466e1fb26d5d95bf2f8296026c95c`.

```sudo
// Source: vvaharness/detect/__init__.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.matcher import Hit, scan_files; preserve alias and import-time effects.
// Source: vvaharness/detect/__init__.py:22-33
In source order: Resolve source import from vvaharness.detect.patterns import default_corpus; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.roles import hits_to_entry_points, hits_to_sinks; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.spec import MatchSpec; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.surface import EntryPoint, Sink; preserve alias and import-time effects. Then Evaluate once ['Hit', 'MatchSpec', 'Result', 'default_corpus', 'scan']; assign in source target order to __all__.
// Source: vvaharness/detect/__init__.py:37-42
// Source: vvaharness/detect/__init__.py:36-36
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/detect/__init__.py:37-42
interface Result {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/detect/__init__.py:38-42
  In source order: Retain source documentation literal source_literal_38_4; it is not a model call. Then For entry_points, declare without assigning a value; source annotation list[EntryPoint]. Then For unsafe_sinks, declare without assigning a value; source annotation list[Sink]. Then For hits, declare without assigning a value; source annotation list[Hit].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/detect/__init__.py:45-52
// Source signature: scan(repo_root: Path, rel_paths: list[str]) -> Result
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan(repo_root, rel_paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/__init__.py:46-47
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call. Then Evaluate once scan_files(repo_root, rel_paths, default_corpus()); assign in source target order to hits.
  // Source: vvaharness/detect/__init__.py:48-52
  End this invocation with Result(entry_points=hits_to_entry_points(hits), unsafe_sinks=hits_to_sinks(hits), hits=hits).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.detect.matcher import Hit, scan_files` at source line 21: `source_detail/vvaharness/detect/matcher.py.sudo.md`.
- `from vvaharness.detect.patterns import default_corpus` at source line 22: `source_detail/vvaharness/detect/patterns.py.sudo.md`.
- `from vvaharness.detect.roles import hits_to_entry_points, hits_to_sinks` at source line 23: `source_detail/vvaharness/detect/roles.py.sudo.md`.
- `from vvaharness.detect.spec import MatchSpec` at source line 24: `source_detail/vvaharness/detect/spec.py.sudo.md`.
- `from vvaharness.models.scan.surface import EntryPoint, Sink` at source line 25: `source_detail/vvaharness/models/scan/surface.py.sudo.md`.
