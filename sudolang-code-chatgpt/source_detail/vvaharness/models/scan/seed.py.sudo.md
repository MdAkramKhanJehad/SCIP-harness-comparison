# vvaharness/models/scan/seed.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/seed.py.evidence.json`. SHA-256: `05562356d14447f0757137955536149111ab74452dc13536147dea5c64427f1d`.

```sudo
// Source: vvaharness/models/scan/seed.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.surface import EntryPoint, Sink; preserve alias and import-time effects.
// Source: vvaharness/models/scan/seed.py:24-37
// Source: vvaharness/models/scan/seed.py:23-23
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/models/scan/seed.py:24-37
interface SeedPackage {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/seed.py:25-30
  In source order: Retain source documentation literal source_literal_25_4; it is not a model call. Then For entry_points, assign field(default_factory=list); source annotation list[EntryPoint]. Then For unsafe_sinks, assign field(default_factory=list); source annotation list[Sink]. Then For taint_paths, assign field(default_factory=list); source annotation list[list[str]]. Then For languages, assign field(default_factory=list); source annotation list[str].
  // Source: vvaharness/models/scan/seed.py:32-33
  In source order: For all_files, assign field(default_factory=list); source annotation list[str]. Then For excluded, assign field(default_factory=dict); source annotation dict.
  // Source: vvaharness/models/scan/seed.py:35-37
  // Source signature: __bool__(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __bool__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/seed.py:36-36
    In source order: Retain source documentation literal source_literal_36_8; it is not a model call.
    // Source: vvaharness/models/scan/seed.py:37-37
    End this invocation with bool(self.entry_points or self.unsafe_sinks or self.taint_paths).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from vvaharness.models.scan.surface import EntryPoint, Sink` at source line 20: `source_detail/vvaharness/models/scan/surface.py.sudo.md`.
