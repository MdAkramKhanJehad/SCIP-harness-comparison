# vvaharness/remediation_agent/playbook.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/playbook.py.evidence.json`. SHA-256: `d576732fdc47b320a10909b4f9e2a3af00688a3c2e08fb5f4a902d5bb1f201ba`.

```sudo
// Source: vvaharness/remediation_agent/playbook.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/playbook.py:23-26
In source order: Resolve source import from vvaharness.remediation_agent.rule_paths import locate_rule; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/playbook.py:28-30
// Source signature: _default_playbook_path() -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _default_playbook_path() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/playbook.py:29-29
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call.
  // Source: vvaharness/remediation_agent/playbook.py:30-30
  End this invocation with locate_rule('remediation_playbook.yaml', __file__).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/playbook.py:33-34
In source order: Evaluate once _default_playbook_path(); assign in source target order to DEFAULT_PLAYBOOK_PATH. Then Evaluate once DEFAULT_PLAYBOOK_PATH.parent; assign in source target order to RULES_DIR.
// Source: vvaharness/remediation_agent/playbook.py:38-65
// Source: vvaharness/remediation_agent/playbook.py:37-37
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/remediation_agent/playbook.py:38-65
interface Strategy {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/playbook.py:39-43
  In source order: For name, declare without assigning a value; source annotation str. Then For instruction, declare without assigning a value; source annotation str. Then For cwe, declare without assigning a value; source annotation str. Then For cwe_title, assign ''; source annotation str. Then For confidence, assign 'suggest'; source annotation str.
  // Source: vvaharness/remediation_agent/playbook.py:44-48
  In source order: For example_before, assign ''; source annotation str. Then For example_after, assign ''; source annotation str. Then For allowed_deps, assign field(default_factory=list); source annotation list[str]. Then For fix_location, assign 'sink'; source annotation str. Then For notes, assign ''; source annotation str.
  // Source: vvaharness/remediation_agent/playbook.py:50-65
  // Source signature: as_prompt_block(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn as_prompt_block(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/playbook.py:51-58
    In source order: Retain source documentation literal source_literal_51_8; it is not a model call. Then Evaluate once [source_template_53_12, source_template_54_12 + (source_template_54_34 if self.cwe_title else ''), source_template_55_12, '', self.instruction.strip() or '(no specific instruction)']; assign in source target order to lines.
    // Source: vvaharness/remediation_agent/playbook.py:59-61
    if (the source predicate self.example_after is truthy) {
      // Source: vvaharness/remediation_agent/playbook.py:60-61
      In source order: Apply source augmented assignment lines += ['', 'Reference pattern (the shape your fix should take):', '```', self.example_after.strip(), '```'] with source evaluation/in-place semantics.
    }
    // Source: vvaharness/remediation_agent/playbook.py:62-64
    In source order: Evaluate once ', '.join(self.allowed_deps) if self.allowed_deps else '(none)'; assign in source target order to deps. Then Apply source augmented assignment lines += ['', source_template_63_22, 'Select THIS strategy; do not invent an alternative approach.'] with source evaluation/in-place semantics.
    // Source: vvaharness/remediation_agent/playbook.py:65-65
    End this invocation with source_literal_65_15.join(lines).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/playbook.py:68-145
interface Playbook {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/playbook.py:70-74
  // Source signature: __init__(self, path: Path | str | None=None)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/playbook.py:71-74
    In source order: For self._cwe, assign {}; source annotation dict. Then For self._policy, assign {}; source annotation dict. Then Evaluate once False; assign in source target order to self._loaded. Then Evaluate self._load(Path(path) if path else DEFAULT_PLAYBOOK_PATH); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/playbook.py:76-85
  // Source signature: _load(self, path: Path) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _load(self, path) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/playbook.py:77-82
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/playbook.py:78-78
      In source order: Evaluate once yaml.safe_load(path.read_text(encoding='utf-8')) or {}; assign in source target order to doc.
    }
    // Source: vvaharness/remediation_agent/playbook.py:79-82
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/remediation_agent/playbook.py:80-81
      In source order: Evaluate log.error('playbook load failed (%s) — guidance-only for all findings', exc); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/playbook.py:82-82
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/playbook.py:83-85
    In source order: Evaluate once doc.get('cwe') or {}; assign in source target order to self._cwe. Then Evaluate once doc.get('policy') or {}; assign in source target order to self._policy. Then Evaluate once True; assign in source target order to self._loaded.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/playbook.py:88-89
  // Source: vvaharness/remediation_agent/playbook.py:87-87
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/playbook.py:88-89
  // Source signature: max_diff_lines(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn max_diff_lines(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/playbook.py:89-89
    End this invocation with int(self._policy.get('max_diff_lines', 40)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/playbook.py:92-93
  // Source: vvaharness/remediation_agent/playbook.py:91-91
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/remediation_agent/playbook.py:92-93
  // Source signature: max_files_touched(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn max_files_touched(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/playbook.py:93-93
    End this invocation with int(self._policy.get('max_files_touched', 2)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/remediation_agent/playbook.py:96-133
  // Source signature: resolve(self, cwe: str | None, language: str, frameworks: set[str]) -> Strategy | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn resolve(self, cwe, language, frameworks) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/playbook.py:98-99
    In source order: Retain source documentation literal source_literal_98_8; it is not a model call. Then Evaluate once self._cwe.get(cwe or ''); assign in source target order to entry.
    // Source: vvaharness/remediation_agent/playbook.py:100-101
    if (the source predicate not entry is truthy) {
      // Source: vvaharness/remediation_agent/playbook.py:101-101
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/playbook.py:102-107
    In source order: Evaluate once entry.get('title', ''); assign in source target order to title. Then Evaluate once entry.get('confidence', 'suggest'); assign in source target order to conf. Then Evaluate once entry.get('fix_location', 'sink'); assign in source target order to loc. Then Evaluate once entry.get('notes', ''); assign in source target order to notes. Then Evaluate once entry.get('strategies') or {}; assign in source target order to strategies.
    // Source: vvaharness/remediation_agent/playbook.py:108-110
    In source order: Evaluate once strategies.get(language) or strategies.get('default') or {}; assign in source target order to lang_block. Then For node, assign None; source annotation dict | None.
    // Source: vvaharness/remediation_agent/playbook.py:111-119
    if (the source predicate isinstance(lang_block, dict) is truthy) {
      // Source: vvaharness/remediation_agent/playbook.py:113-116
      for each fw in frameworks or set() {
        // Source: vvaharness/remediation_agent/playbook.py:114-116
        if (the source predicate fw in lang_block is truthy) {
          // Source: vvaharness/remediation_agent/playbook.py:115-115
          In source order: Evaluate once lang_block[fw]; assign in source target order to node.
          // Source: vvaharness/remediation_agent/playbook.py:116-116
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
      }
      // Source: vvaharness/remediation_agent/playbook.py:117-119
      if (the source predicate node is None is truthy) {
        // Source: vvaharness/remediation_agent/playbook.py:118-119
        In source order: Evaluate once lang_block.get('default') or (lang_block if 'name' in lang_block else None); assign in source target order to node.
      }
    }
    // Source: vvaharness/remediation_agent/playbook.py:120-121
    if (the source predicate node is None is truthy) {
      // Source: vvaharness/remediation_agent/playbook.py:121-121
      In source order: Evaluate once entry.get('fallback'); assign in source target order to node.
    }
    // Source: vvaharness/remediation_agent/playbook.py:122-123
    if (the source predicate not node is truthy) {
      // Source: vvaharness/remediation_agent/playbook.py:123-123
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/playbook.py:124-133
    End this invocation with Strategy(name=node.get('name', 'unnamed'), instruction=str(node.get('instruction', '')).strip(), cwe=cwe or '', cwe_title=title, confidence=node.get('confidence', conf), example_before=str(node.get('example_before', '')).strip(), example_after=str(node.get('example_after', '')).strip(), allowed_deps=list(node.get('allowed_deps') or []), fix_location=loc, notes=notes).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/remediation_agent/playbook.py:135-145
  // Source signature: guidance_for(self, cwe: str | None) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn guidance_for(self, cwe) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/remediation_agent/playbook.py:136-140
    In source order: Retain source documentation literal source_literal_136_8; it is not a model call. Then Evaluate once self._cwe.get(cwe or '') or {}; assign in source target order to entry. Then Evaluate once entry.get('notes') or ''; assign in source target order to notes. Then Evaluate once entry.get('title') or (cwe or 'this finding'); assign in source target order to title. Then Evaluate once (entry.get('fallback') or {}).get('instruction', ''); assign in source target order to fb.
    // Source: vvaharness/remediation_agent/playbook.py:141-144
    In source order: Evaluate once notes or fb or source_literal_142_12; assign in source target order to body.
    // Source: vvaharness/remediation_agent/playbook.py:145-145
    End this invocation with source_template_145_15.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.remediation_agent.rule_paths import locate_rule` at source line 23: `source_detail/vvaharness/remediation_agent/rule_paths.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 24: `source_detail/vvaharness/util/logs.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/remediation_agent/playbook.py.sudo.md). Exact strings in the evidence asset support this conversion.
