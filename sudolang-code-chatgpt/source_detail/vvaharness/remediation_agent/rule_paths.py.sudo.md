# vvaharness/remediation_agent/rule_paths.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/rule_paths.py.evidence.json`. SHA-256: `421ae873588225544127d2bb6b8261cb45021e5d7cab9d9d23662e18d48de808`.

```sudo
// Source: vvaharness/remediation_agent/rule_paths.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/rule_paths.py:21-23
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once ('remediation_policy.yaml', 'remediation_playbook.yaml'); assign in source target order to RULE_FILES.
// Source: vvaharness/remediation_agent/rule_paths.py:26-31
// Source signature: settings_path() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn settings_path() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/rule_paths.py:27-27
  In source order: Evaluate once os.environ.get('VVAHARNESS_SETTINGS_FILE'); assign in source target order to override.
  // Source: vvaharness/remediation_agent/rule_paths.py:28-29
  if (the source predicate override is truthy) {
    // Source: vvaharness/remediation_agent/rule_paths.py:29-29
    End this invocation with Path(override).expanduser().
  }
  // Source: vvaharness/remediation_agent/rule_paths.py:30-30
  In source order: Evaluate once Path(os.environ.get('XDG_CONFIG_HOME', Path.home() / '.config')); assign in source target order to root.
  // Source: vvaharness/remediation_agent/rule_paths.py:31-31
  End this invocation with root / 'vvaharness' / 'settings.json'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/rule_paths.py:34-40
// Source signature: configured_inputs_dir() -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn configured_inputs_dir() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/rule_paths.py:35-40
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/rule_paths.py:36-37
    In source order: Evaluate once json.loads(settings_path().read_text(encoding='utf-8')); assign in source target order to raw. Then Evaluate once raw.get('inputs_dir') if isinstance(raw, dict) else None; assign in source target order to value.
    // Source: vvaharness/remediation_agent/rule_paths.py:38-38
    End this invocation with Path(value).expanduser() if value else None.
  }
  // Source: vvaharness/remediation_agent/rule_paths.py:39-40
  On the first matching source exception (OSError, ValueError, TypeError), in handler order {
    // Source: vvaharness/remediation_agent/rule_paths.py:40-40
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/rule_paths.py:43-56
// Source signature: save_inputs_dir(path: str | Path) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn save_inputs_dir(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/rule_paths.py:44-47
  In source order: Evaluate once Path(path).expanduser().resolve(); assign in source target order to directory. Then Evaluate once settings_path(); assign in source target order to target. Then Evaluate target.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then For data, assign {}; source annotation dict[str, object].
  // Source: vvaharness/remediation_agent/rule_paths.py:48-53
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/rule_paths.py:49-49
    In source order: Evaluate once json.loads(target.read_text(encoding='utf-8')); assign in source target order to existing.
    // Source: vvaharness/remediation_agent/rule_paths.py:50-51
    if (the source predicate isinstance(existing, dict) is truthy) {
      // Source: vvaharness/remediation_agent/rule_paths.py:51-51
      In source order: Evaluate data.update(existing); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/rule_paths.py:52-53
  On the first matching source exception (OSError, ValueError, TypeError), in handler order {
    // Source: vvaharness/remediation_agent/rule_paths.py:53-53
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/remediation_agent/rule_paths.py:54-55
  In source order: Evaluate once str(directory); assign in source target order to data['inputs_dir']. Then Evaluate target.write_text(json.dumps(data, indent=2) + source_literal_55_51, encoding='utf-8'); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/rule_paths.py:56-56
  End this invocation with target.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/rule_paths.py:59-66
// Source signature: candidate_inputs_dirs(package_file: str | Path) -> tuple[Path, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn candidate_inputs_dirs(package_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/rule_paths.py:60-64
  In source order: Delete source targets in order: package_file. Then Evaluate once Path(__file__).resolve().parents[2] / 'inputs'; assign in source target order to source_inputs. Then Evaluate once Path(sys.prefix) / 'share' / 'vvaharness' / 'rules'; assign in source target order to shared_inputs. Then Evaluate once configured_inputs_dir(); assign in source target order to configured. Then Evaluate once (source_inputs, shared_inputs, configured); assign in source target order to ordered.
  // Source: vvaharness/remediation_agent/rule_paths.py:65-66
  End this invocation with tuple((path for i, path in enumerate(ordered) if path is not None and path not in ordered[:i])).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/rule_paths.py:69-71
// Source signature: locate_rule(filename: str, package_file: str | Path) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn locate_rule(filename, package_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/rule_paths.py:70-70
  In source order: Evaluate once tuple((path / filename for path in candidate_inputs_dirs(package_file))); assign in source target order to candidates.
  // Source: vvaharness/remediation_agent/rule_paths.py:71-71
  End this invocation with next((path for path in candidates if path.is_file()), candidates[0]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/rule_paths.py:74-75
// Source signature: missing_rules(package_file: str | Path) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn missing_rules(package_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/rule_paths.py:75-75
  End this invocation with [name for name in RULE_FILES if not locate_rule(name, package_file).is_file()].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/rule_paths.py:78-81
// Source signature: validate_inputs_dir(path: str | Path) -> tuple[Path, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_inputs_dir(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/rule_paths.py:79-80
  In source order: Evaluate once Path(path).expanduser(); assign in source target order to directory. Then Evaluate once [name for name in RULE_FILES if not (directory / name).is_file()]; assign in source target order to missing.
  // Source: vvaharness/remediation_agent/rule_paths.py:81-81
  End this invocation with (directory, missing).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
