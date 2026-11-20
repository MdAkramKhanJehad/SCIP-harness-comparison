# vvaharness/plugins/semgrep/plugin.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/plugins/semgrep/plugin.py.evidence.json`. SHA-256: `150449deaaf4bc9e1e32f34beb95c91800da2b96af1d11424e03f319a466ec1d`.

```sudo
// Source: vvaharness/plugins/semgrep/plugin.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.plugins import GraphEnricher; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/plugin.py:23-27
In source order: Resolve source import from vvaharness.plugins.semgrep.enricher import SemgrepEnricher; preserve alias and import-time effects. Then Resolve source import from vvaharness.plugins.semgrep.tools import SEMGREP_TOOLS; preserve alias and import-time effects. Then Resolve source import from vvaharness.plugins.semgrep.triage import semgrep_triage_subagent; preserve alias and import-time effects. Then Resolve source import from vvaharness.sdk.plugins import Contribution, PluginInfo; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/plugin.py:29-32
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once '1'; assign in source target order to VERSION. Then Evaluate once 32; assign in source target order to _MAX_CONFIG_FILES.
// Source: vvaharness/plugins/semgrep/plugin.py:35-36
interface SemgrepConfigError {
  Describe the source Python type, preserving its base/metaclass expression order: ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/plugin.py:36-36
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call.
}
// Source: vvaharness/plugins/semgrep/plugin.py:39-49
// Source signature: _validated_configs(configs: tuple[Path | str, ...]) -> tuple[Path, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validated_configs(configs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/plugin.py:40-40
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/plugin.py:41-42
  if (the source predicate len(configs) > _MAX_CONFIG_FILES is truthy) {
    // Source: vvaharness/plugins/semgrep/plugin.py:42-42
    Raise SemgrepConfigError(source_template_42_33).
  }
  // Source: vvaharness/plugins/semgrep/plugin.py:43-43
  In source order: Evaluate once []; assign in source target order to resolved.
  // Source: vvaharness/plugins/semgrep/plugin.py:44-48
  for each raw in configs {
    // Source: vvaharness/plugins/semgrep/plugin.py:45-45
    In source order: Evaluate once Path(raw).expanduser(); assign in source target order to path.
    // Source: vvaharness/plugins/semgrep/plugin.py:46-47
    if (the source predicate not path.is_file() is truthy) {
      // Source: vvaharness/plugins/semgrep/plugin.py:47-47
      Raise SemgrepConfigError(source_template_47_37).
    }
    // Source: vvaharness/plugins/semgrep/plugin.py:48-48
    In source order: Evaluate resolved.append(path.resolve()); retain side effects and discard the expression result.
  }
  // Source: vvaharness/plugins/semgrep/plugin.py:49-49
  End this invocation with tuple(resolved).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/plugin.py:53-89
// Source: vvaharness/plugins/semgrep/plugin.py:52-52
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/plugins/semgrep/plugin.py:53-89
interface SemgrepPlugin {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/plugin.py:54-59
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call. Then For configs, assign (); source annotation tuple[Path, ...]. Then For rulesets, assign (); source annotation tuple[str, ...]. Then For executable, assign 'semgrep'; source annotation str. Then For timeout_seconds, assign 120.0; source annotation float.
  // Source: vvaharness/plugins/semgrep/plugin.py:60-61
  In source order: For enricher, assign None; source annotation GraphEnricher | None. Then For priority, assign 100; source annotation int.
  // Source: vvaharness/plugins/semgrep/plugin.py:64-66
  // Source: vvaharness/plugins/semgrep/plugin.py:63-63
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/plugins/semgrep/plugin.py:64-66
  // Source signature: info(self) -> PluginInfo
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn info(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/plugin.py:65-65
    In source order: Retain source documentation literal source_literal_65_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/plugin.py:66-66
    End this invocation with PluginInfo(name='semgrep', version=VERSION, priority=self.priority).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/plugins/semgrep/plugin.py:68-74
  // Source signature: contribute(self) -> Contribution
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn contribute(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/plugin.py:69-69
    In source order: Retain source documentation literal source_literal_69_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/plugin.py:70-74
    End this invocation with Contribution(enrichers=self._enrichers(), graph_tools=dict(SEMGREP_TOOLS), subagents=(semgrep_triage_subagent(),)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/plugin.py:76-89
  // Source signature: _enrichers(self) -> tuple[GraphEnricher, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _enrichers(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/plugin.py:77-77
    In source order: Retain source documentation literal source_literal_77_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/plugin.py:78-79
    if (the source predicate self.enricher is not None is truthy) {
      // Source: vvaharness/plugins/semgrep/plugin.py:79-79
      End this invocation with (self.enricher,).
    }
    // Source: vvaharness/plugins/semgrep/plugin.py:80-86
    if (the source predicate not self.configs and (not self.rulesets) is truthy) {
      // Source: vvaharness/plugins/semgrep/plugin.py:81-85
      In source order: Evaluate log.warning(source_literal_82_16); retain side effects and discard the expression result.
      // Source: vvaharness/plugins/semgrep/plugin.py:86-86
      End this invocation with ().
    }
    // Source: vvaharness/plugins/semgrep/plugin.py:87-89
    End this invocation with (SemgrepEnricher(configs=_validated_configs(self.configs) if self.configs else (), rulesets=tuple(self.rulesets), executable=self.executable, timeout_seconds=self.timeout_seconds, priority=self.priority),).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/plugins/semgrep/plugin.py:92-92
In source order: Evaluate once ['VERSION', 'SemgrepConfigError', 'SemgrepPlugin']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk.plugins import GraphEnricher` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/__init__.py.sudo.md`.
- `from vvaharness.plugins.semgrep.enricher import SemgrepEnricher` at source line 23: `source_detail/vvaharness/plugins/semgrep/enricher.py.sudo.md`.
- `from vvaharness.plugins.semgrep.tools import SEMGREP_TOOLS` at source line 24: `source_detail/vvaharness/plugins/semgrep/tools.py.sudo.md`.
- `from vvaharness.plugins.semgrep.triage import semgrep_triage_subagent` at source line 25: `source_detail/vvaharness/plugins/semgrep/triage.py.sudo.md`.
- `from vvaharness.sdk.plugins import Contribution, PluginInfo` at source line 26: `source_detail/vvaharness/sdk/plugins.py.sudo.md`.
- `from vvaharness.util import logs` at source line 27: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 27: `source_detail/vvaharness/util/logs.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/plugins/semgrep/plugin.py.sudo.md). Exact strings in the evidence asset support this conversion.
