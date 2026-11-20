# vvaharness/models/scan/context.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/context.py.evidence.json`. SHA-256: `15465877dc5fa55c5763d31fe31e58e28f048808fff3ee0b8e478c7cee5b2afd`.

```sudo
// Source: vvaharness/models/scan/context.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field; preserve alias and import-time effects.
// Source: vvaharness/models/scan/context.py:23-27
In source order: Resolve source import from vvaharness.models.scan.inputs import CVE, AppProfile, Control; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.surface import EntryPoint, ModuleInfo, Sink; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan.threat import ThreatModel; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log.
// Source: vvaharness/models/scan/context.py:29-115
interface ContextPackage {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/context.py:30-35
  In source order: For repo_root, declare without assigning a value; source annotation str. Then For language, declare without assigning a value; source annotation str. Then For seed_taint_paths, assign []; source annotation list[list[str]]. Then For entry_points, assign []; source annotation list[EntryPoint]. Then For unsafe_sinks, assign []; source annotation list[Sink].
  // Source: vvaharness/models/scan/context.py:36-40
  In source order: For modules, assign []; source annotation list[ModuleInfo]. Then For all_files, assign []; source annotation list[str]. Then For excluded, assign {}; source annotation dict. Then For known_cves, assign []; source annotation list[CVE]. Then For design_controls, assign []; source annotation list[Control].
  // Source: vvaharness/models/scan/context.py:41-47
  In source order: For app_profile, assign None; source annotation AppProfile | None. Then For threat_model, assign None; source annotation ThreatModel | None. Then For notes, assign ''; source annotation str. Then For ev_collection, assign None; source annotation dict | None. Then For graph_handle, assign Field(default=None, exclude=True); source annotation Any.
  // Source: vvaharness/models/scan/context.py:49-115
  // Source signature: ast_context_view(self, *, max_files: int=250, max_entry_points: int=120, max_sinks: int=160, max_modules: int=40, max_edges: int=120) -> ContextPackage
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ast_context_view(self, max_files, max_entry_points, max_sinks, max_modules, max_edges) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/context.py:52-53
    In source order: For seed_files, assign []; source annotation list[str]. Then For _seen, assign set(); source annotation set[str].
    // Source: vvaharness/models/scan/context.py:55-61
    // Source signature: _add_file(path: str) -> None
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _add_file(path) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/models/scan/context.py:56-56
      In source order: Evaluate once path.replace('\\', '/'); assign in source target order to norm.
      // Source: vvaharness/models/scan/context.py:57-58
      while (the source predicate norm.startswith('./') is truthy) {
        // Source: vvaharness/models/scan/context.py:58-58
        In source order: Evaluate once norm[2:]; assign in source target order to norm.
      }
      // Source: vvaharness/models/scan/context.py:59-61
      if (the source predicate norm and norm not in _seen is truthy) {
        // Source: vvaharness/models/scan/context.py:60-61
        In source order: Evaluate _seen.add(norm); retain side effects and discard the expression result. Then Evaluate seed_files.append(norm); retain side effects and discard the expression result.
      }
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/models/scan/context.py:63-64
    for each entry in self.entry_points[:max_entry_points] {
      // Source: vvaharness/models/scan/context.py:64-64
      In source order: Evaluate _add_file(entry.file); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/context.py:65-66
    for each sink in self.unsafe_sinks[:max_sinks] {
      // Source: vvaharness/models/scan/context.py:66-66
      In source order: Evaluate _add_file(sink.file); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/context.py:67-69
    for each path in self.seed_taint_paths {
      // Source: vvaharness/models/scan/context.py:68-69
      for each node in path {
        // Source: vvaharness/models/scan/context.py:69-69
        In source order: Evaluate _add_file(node.split(':', 1)[0]); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/context.py:70-72
    for each module in self.modules[:max_modules] {
      // Source: vvaharness/models/scan/context.py:71-72
      for each path in module.files[:5] {
        // Source: vvaharness/models/scan/context.py:72-72
        In source order: Evaluate _add_file(path); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/context.py:74-76
    In source order: For all_files, assign []; source annotation list[str]. Then Evaluate once set(self.all_files); assign in source target order to all_files_set. Then For seen_all, assign set(); source annotation set[str].
    // Source: vvaharness/models/scan/context.py:77-82
    for each path in seed_files {
      // Source: vvaharness/models/scan/context.py:78-82
      if (the source predicate path in all_files_set and path not in seen_all is truthy) {
        // Source: vvaharness/models/scan/context.py:79-80
        In source order: Evaluate seen_all.add(path); retain side effects and discard the expression result. Then Evaluate all_files.append(path); retain side effects and discard the expression result.
        // Source: vvaharness/models/scan/context.py:81-82
        if (the source predicate len(all_files) >= max_files is truthy) {
          // Source: vvaharness/models/scan/context.py:82-82
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
      }
    }
    // Source: vvaharness/models/scan/context.py:83-89
    if (the source predicate len(all_files) < max_files is truthy) {
      // Source: vvaharness/models/scan/context.py:84-89
      for each path in self.all_files {
        // Source: vvaharness/models/scan/context.py:85-89
        if (the source predicate path not in seen_all is truthy) {
          // Source: vvaharness/models/scan/context.py:86-87
          In source order: Evaluate seen_all.add(path); retain side effects and discard the expression result. Then Evaluate all_files.append(path); retain side effects and discard the expression result.
          // Source: vvaharness/models/scan/context.py:88-89
          if (the source predicate len(all_files) >= max_files is truthy) {
            // Source: vvaharness/models/scan/context.py:89-89
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
      }
    }
    // Source: vvaharness/models/scan/context.py:91-95
    In source order: Evaluate once set(all_files); assign in source target order to allowed_files. Then Evaluate once [e for e in self.entry_points if e.file in allowed_files][:max_entry_points]; assign in source target order to entry_points. Then Evaluate once [s for s in self.unsafe_sinks if s.file in allowed_files][:max_sinks]; assign in source target order to unsafe_sinks. Then Evaluate once []; assign in source target order to modules.
    // Source: vvaharness/models/scan/context.py:96-101
    for each module in self.modules {
      // Source: vvaharness/models/scan/context.py:97-97
      In source order: Evaluate once [path for path in module.files if path in allowed_files][:10]; assign in source target order to kept.
      // Source: vvaharness/models/scan/context.py:98-99
      if (the source predicate kept is truthy) {
        // Source: vvaharness/models/scan/context.py:99-99
        In source order: Evaluate modules.append(module.model_copy(update={'files': kept})); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/context.py:100-101
      if (the source predicate len(modules) >= max_modules is truthy) {
        // Source: vvaharness/models/scan/context.py:101-101
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vvaharness/models/scan/context.py:103-103
    In source order: Evaluate once []; assign in source target order to trimmed_paths.
    // Source: vvaharness/models/scan/context.py:104-107
    for each path in self.seed_taint_paths {
      // Source: vvaharness/models/scan/context.py:105-105
      In source order: Evaluate once [node for node in path if node.split(':', 1)[0] in allowed_files]; assign in source target order to kept.
      // Source: vvaharness/models/scan/context.py:106-107
      if (the source predicate kept is truthy) {
        // Source: vvaharness/models/scan/context.py:107-107
        In source order: Evaluate trimmed_paths.append(kept[:8]); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/models/scan/context.py:109-115
    End this invocation with self.model_copy(update={'all_files': all_files, 'entry_points': entry_points, 'unsafe_sinks': unsafe_sinks, 'modules': modules, 'seed_taint_paths': trimmed_paths}).
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.models.scan.inputs import CVE, AppProfile, Control` at source line 23: `source_detail/vvaharness/models/scan/inputs.py.sudo.md`.
- `from vvaharness.models.scan.surface import EntryPoint, ModuleInfo, Sink` at source line 24: `source_detail/vvaharness/models/scan/surface.py.sudo.md`.
- `from vvaharness.models.scan.threat import ThreatModel` at source line 25: `source_detail/vvaharness/models/scan/threat.py.sudo.md`.
