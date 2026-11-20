# vvaharness/models/verdict.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/verdict.py.evidence.json`. SHA-256: `3f2009295c1d7e53097f01ac9a1227c5536ad471d0b8deacfd7baf83e7bb97a9`.

```sudo
// Source: vvaharness/models/verdict.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, ConfigDict, Field; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.gates import GateAssessment; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.provenance import Provenance; preserve alias and import-time effects.
// Source: vvaharness/models/verdict.py:23-25
In source order: Resolve source import from vvaharness.models.vocab import Decision, Disposition; preserve alias and import-time effects. Then Evaluate once ['Ticket', 'Verdict']; assign in source target order to __all__.
// Source: vvaharness/models/verdict.py:28-35
interface Ticket {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/verdict.py:29-35
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For ref, assign Field(description="the validator's own identifier for the pending review"); source annotation str. Then For opaque, assign Field(default='', description='validator-private state to resume with'); source annotation str.
}
// Source: vvaharness/models/verdict.py:38-60
interface Verdict {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/verdict.py:39-49
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call. Then Evaluate once ConfigDict(frozen=True, extra='ignore'); assign in source target order to model_config. Then For decision, assign Field(description='did the fix work'); source annotation Decision. Then For rationale, assign Field(description='why, as the host scored it'); source annotation str. Then For engine_rationale, assign Field(default='', description="the validator's own account, verbatim; empty when it gave none"); source annotation str.
  // Source: vvaharness/models/verdict.py:50-58
  In source order: For score, assign Field(default=None, ge=0.0, le=1.0, description='0-1 confidence; None when unscored'); source annotation float | None. Then For gates, assign Field(default=(), description='per-check outcomes'); source annotation tuple[GateAssessment, ...]. Then For conditions, assign Field(default=(), description='what would make this a full fix'); source annotation tuple[str, ...]. Then For recommendations, assign Field(default=(), description='code-level follow-ups'); source annotation tuple[str, ...]. Then For disposition, assign Field(default=None, description='accepted risk or false positive, when a reviewer says so'); source annotation Disposition | None.
  // Source: vvaharness/models/verdict.py:59-60
  In source order: For ticket, assign Field(default=None, description='set when the verdict is deferred'); source annotation Ticket | None. Then For produced_by, assign Field(default=Provenance(), description='attributable origin'); source annotation Provenance.
}
```

## Local import links

- `from vvaharness.models.gates import GateAssessment` at source line 21: `source_detail/vvaharness/models/gates.py.sudo.md`.
- `from vvaharness.models.provenance import Provenance` at source line 22: `source_detail/vvaharness/models/provenance.py.sudo.md`.
- `from vvaharness.models.vocab import Decision, Disposition` at source line 23: `source_detail/vvaharness/models/vocab.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/models/verdict.py.sudo.md). Exact strings in the evidence asset support this conversion.
