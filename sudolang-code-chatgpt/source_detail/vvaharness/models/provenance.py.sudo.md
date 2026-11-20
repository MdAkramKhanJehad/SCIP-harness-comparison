# vvaharness/models/provenance.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/provenance.py.evidence.json`. SHA-256: `59e47c12579a9b1717b03118a0477b4ec175c9bb316d50719959de4d7758b5d2`.

```sudo
// Source: vvaharness/models/provenance.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from datetime import datetime; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field; preserve alias and import-time effects. Then Evaluate once ['HARNESS_REGISTRY', 'LLM_REGISTRY', 'Provenance']; assign in source target order to __all__.
// Source: vvaharness/models/provenance.py:26-27
In source order: Evaluate once 'llm'; assign in source target order to LLM_REGISTRY. Then Evaluate once 'harness'; assign in source target order to HARNESS_REGISTRY.
// Source: vvaharness/models/provenance.py:30-56
interface Provenance {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/provenance.py:31-38
  In source order: Retain source documentation literal source_literal_31_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For engine, assign Field(default='', description="engine identity, e.g. 'vvaharness.agentic'"); source annotation str. Then For engine_version, assign Field(default='', description='version of that engine'); source annotation str. Then For model, assign Field(default='', description='model id, when the engine used one'); source annotation str.
  // Source: vvaharness/models/provenance.py:40-56
  In source order: For backend, assign Field(default='', description=source_literal_43_12); source annotation str. Then For turns, assign Field(default=None, description='agent turns; None when unreported'); source annotation int | None. Then For usd, assign Field(default=None, description='spend in USD; None when unreported'); source annotation float | None. Then For started, assign Field(default=None, description='UTC start'); source annotation datetime | None. Then For ended, assign Field(default=None, description='UTC finish'); source annotation datetime | None.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/models/provenance.py.sudo.md). Exact strings in the evidence asset support this conversion.
