# vvaharness/remediation_agent/artifacts/diff/synth.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/artifacts/diff/synth.py.evidence.json`. SHA-256: `6f6ebc19a6d3e43fce8269bf9880efa98d48ad0050d1b944013a24eb7415bf92`.

```sudo
// Source: vvaharness/remediation_agent/artifacts/diff/synth.py:15-24
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import difflib; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/artifacts/diff/synth.py:25-31
In source order: Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once source_literal_31_15; assign in source target order to SYNTH_HEADER.
// Source: vvaharness/remediation_agent/artifacts/diff/synth.py:34-85
// Source signature: synth_unified_diff(repo: Path, before: dict[str, str | None], extra_files: list[str] | None=None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn synth_unified_diff(repo, before, extra_files) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:36-42
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then Evaluate once Path(repo); assign in source target order to repo. Then Evaluate once before or {}; assign in source target order to before. Then For paths, assign []; source annotation list[str]. Then For safe, assign {}; source annotation dict[str, Path].
  // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:43-53
  for each ref in list(before.keys()) + list(extra_files or []) {
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:44-44
    In source order: Evaluate once _norm_path(ref); assign in source target order to rel.
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:45-46
    if (the source predicate not rel or rel in safe is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:46-46
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:47-47
    In source order: Evaluate once _safe_repo_path(repo, ref); assign in source target order to p.
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:48-51
    if (the source predicate p is None is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:49-50
      In source order: Evaluate log.warning('synth diff: refusing out-of-repo file reference %r (escapes %s)', ref, repo); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:51-51
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:52-53
    In source order: Evaluate once p; assign in source target order to safe[rel]. Then Evaluate paths.append(rel); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:54-55
  if (the source predicate not paths is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:55-55
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:57-57
  In source order: For chunks, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:58-81
  for each rel in paths {
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:59-61
    In source order: Evaluate once before.get(rel); assign in source target order to old. Then Evaluate once '' if old is None else old; assign in source target order to old_text. Then Evaluate once safe[rel]; assign in source target order to p.
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:62-65
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:63-63
      In source order: Evaluate once p.read_text(encoding='utf-8') if p.is_file() else ''; assign in source target order to new_text.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:64-65
    On the first matching source exception Exception, in handler order {
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:65-65
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:67-68
    if (the source predicate old_text == new_text is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:68-68
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:69-75
    In source order: Evaluate once '/dev/null' if old is None else source_template_69_53; assign in source target order to from_label. Then Evaluate once source_template_70_19 if new_text != '' else '/dev/null'; assign in source target order to to_label. Then Evaluate once difflib.unified_diff(old_text.splitlines(keepends=True), new_text.splitlines(keepends=True), fromfile=from_label, tofile=to_label); assign in source target order to diff. Then Evaluate once ''.join(diff); assign in source target order to body.
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:76-77
    if (the source predicate not body is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:77-77
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:79-80
    if (the source predicate not body.endswith(source_literal_79_29) is truthy) {
      // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:80-80
      In source order: Apply source augmented assignment body += source_literal_80_20 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:81-81
    In source order: Evaluate chunks.append(source_template_81_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:83-84
  if (the source predicate not chunks is truthy) {
    // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:84-84
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/artifacts/diff/synth.py:85-85
  End this invocation with SYNTH_HEADER + ''.join(chunks).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff.paths import _norm_path, _safe_repo_path` at source line 21: `source_detail/vvaharness/remediation_agent/artifacts/diff/paths.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 25: `source_detail/vvaharness/util/logs.py.sudo.md`.
