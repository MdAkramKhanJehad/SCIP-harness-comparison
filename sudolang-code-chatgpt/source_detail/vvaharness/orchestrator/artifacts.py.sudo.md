# vvaharness/orchestrator/artifacts.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/artifacts.py.evidence.json`. SHA-256: `730852f9f2b81885e6926176c48ccd9b54fbfc252d4a19add99a170bb3958cd2`.

```sudo
// Source: vvaharness/orchestrator/artifacts.py:15-29
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Evaluate once ['CASE_DIR_NAME', 'CASE_FILE_NAME', 'FINDINGS_JSON_NAME', 'SCAN_DIR_NAME', 'UnsafeArtifactDir', 'artifact_dir']; assign in source target order to __all__.
// Source: vvaharness/orchestrator/artifacts.py:32-41
In source order: For SCAN_DIR_NAME, assign 'security-scan'; source annotation Final. Then For CASE_DIR_NAME, assign 'security-remediation'; source annotation Final. Then For CASE_FILE_NAME, assign 'finding_case.json'; source annotation Final. Then For FINDINGS_JSON_NAME, assign 'findings.json'; source annotation Final.
// Source: vvaharness/orchestrator/artifacts.py:44-45
interface UnsafeArtifactDir {
  Describe the source Python type, preserving its base/metaclass expression order: RuntimeError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/artifacts.py:45-45
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call.
}
// Source: vvaharness/orchestrator/artifacts.py:49-54
// Source signature: _link_target(path: Path) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _link_target(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/artifacts.py:50-50
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call.
  // Source: vvaharness/orchestrator/artifacts.py:51-54
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/artifacts.py:52-52
    End this invocation with str(path.readlink()).
  }
  // Source: vvaharness/orchestrator/artifacts.py:53-54
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/orchestrator/artifacts.py:54-54
    End this invocation with '?'.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/artifacts.py:57-82
// Source signature: artifact_dir(repo: Path | str, name: str) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn artifact_dir(repo, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/artifacts.py:58-61
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to root. Then Evaluate once root / name; assign in source target order to out.
  // Source: vvaharness/orchestrator/artifacts.py:62-66
  if (the source predicate out.is_symlink() is truthy) {
    // Source: vvaharness/orchestrator/artifacts.py:63-66
    Raise UnsafeArtifactDir(source_template_64_12).
  }
  // Source: vvaharness/orchestrator/artifacts.py:67-70
  if (the source predicate out.exists() and (not out.is_dir()) is truthy) {
    // Source: vvaharness/orchestrator/artifacts.py:68-70
    Raise UnsafeArtifactDir(source_template_69_12).
  }
  // Source: vvaharness/orchestrator/artifacts.py:71-76
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/artifacts.py:72-72
    In source order: Evaluate once out.resolve().is_relative_to(root.resolve()); assign in source target order to inside.
  }
  // Source: vvaharness/orchestrator/artifacts.py:73-76
  On the first matching source exception OSError as exc, in handler order {
    // Source: vvaharness/orchestrator/artifacts.py:74-76
    Raise UnsafeArtifactDir(source_template_75_12) with explicit source cause exc.
  }
  // Source: vvaharness/orchestrator/artifacts.py:77-81
  if (the source predicate not inside is truthy) {
    // Source: vvaharness/orchestrator/artifacts.py:78-81
    Raise UnsafeArtifactDir(source_template_79_12).
  }
  // Source: vvaharness/orchestrator/artifacts.py:82-82
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
