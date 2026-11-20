# vvaharness/sdk/stages.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/sdk/stages.py.evidence.json`. SHA-256: `45c5b81ebe192d12fa6612e8f0bcb7b046d70f27484e1e379c1c0e292b551dc6`.

```sudo
// Source: vvaharness/sdk/stages.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, FinalReport, Finding, SeedPackage, TaskManifest, ThreatModel; preserve alias and import-time effects.
// Source: vvaharness/sdk/stages.py:31-37
interface Phase {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/stages.py:32-37
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then Evaluate once 'discover'; assign in source target order to DISCOVER. Then Evaluate once 'analyze'; assign in source target order to ANALYZE. Then Evaluate once 'verify'; assign in source target order to VERIFY. Then Evaluate once 'remediate'; assign in source target order to REMEDIATE.
}
// Source: vvaharness/sdk/stages.py:40-47
interface Seam {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/stages.py:41-46
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then Evaluate once 'enrich-graph'; assign in source target order to ENRICH_GRAPH. Then Evaluate once 'swap-graph'; assign in source target order to SWAP_GRAPH. Then Evaluate once 'bring-dto'; assign in source target order to BRING_DTO. Then Evaluate once 'add-tools'; assign in source target order to ADD_TOOLS.
  // Source: vvaharness/sdk/stages.py:47-47
  In source order: Evaluate once 'add-subagents'; assign in source target order to ADD_SUBAGENTS.
}
// Source: vvaharness/sdk/stages.py:51-62
// Source: vvaharness/sdk/stages.py:50-50
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/sdk/stages.py:51-62
interface Stage {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/stages.py:52-57
  In source order: Retain source documentation literal source_literal_52_4; it is not a model call. Then For id, declare without assigning a value; source annotation str. Then For phase, declare without assigning a value; source annotation Phase. Then For name, declare without assigning a value; source annotation str. Then For dto, declare without assigning a value; source annotation type | None.
  // Source: vvaharness/sdk/stages.py:58-62
  In source order: For payload, declare without assigning a value; source annotation str. Then For agentic, assign False; source annotation bool. Then For injectable, assign False; source annotation bool. Then For seams, assign (); source annotation tuple[Seam, ...]. Then For caveat, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/sdk/stages.py:67-108
In source order: For STAGES, assign (Stage('s0', Phase.DISCOVER, 'Seed', SeedPackage, 'SeedPackage', seams=(Seam.ENRICH_GRAPH, Seam.SWAP_GRAPH), caveat='the graph is built here, so this is the only place an enricher runs'), Stage('s1', Phase.DISCOVER, 'Precompute', ContextPackage, 'ContextPackage', injectable=True, seams=(Seam.BRING_DTO,), caveat='ContextPackage.graph_handle is exclude=True, so an injected one has no graph and S2/S4/S6 warn then stand down'), Stage('s2', Phase.ANALYZE, 'Threat model', ThreatModel, 'ThreatModel', agentic=True, injectable=True, seams=(Seam.BRING_DTO, Seam.ADD_TOOLS, Seam.ADD_SUBAGENTS)), Stage('s3', Phase.ANALYZE, 'Decompose', TaskManifest, 'TaskManifest', injectable=True, seams=(Seam.BRING_DTO,), caveat='deterministic: one InvestigationUnit per threat, zero model calls'), Stage('s4', Phase.ANALYZE, 'Deep dive', Finding, '{"findings": list[Finding], "outcomes": dict[str, str]}', agentic=True, injectable=True, seams=(Seam.BRING_DTO, Seam.ADD_TOOLS, Seam.ADD_SUBAGENTS), caveat='seed this to run S5 onward on findings you already have'), Stage('s5', Phase.VERIFY, 'Prefilter', Finding, '{"findings": list[Finding], "pre_dropped": list[Finding]}', injectable=True, seams=(Seam.BRING_DTO,)), Stage('s6', Phase.VERIFY, 'Verify', Finding, '{"verified": list[Finding], "dropped": list[Finding]}', agentic=True, seams=(Seam.ADD_TOOLS, Seam.ADD_SUBAGENTS)), Stage('s7', Phase.VERIFY, 'Dedupe', Finding, '(pre_dropped, verified, dropped, canonical, dup_dropped, s5_out_count)', caveat='a 6-tuple, not a dict; the only stage whose envelope is positional'), Stage('s8', Phase.VERIFY, 'Report', FinalReport, 'FinalReport'), Stage('s9', Phase.VERIFY, 'SARIF', None, 'str (path to the written sarif)'), Stage('s10', Phase.REMEDIATE, 'Remediate', None, 'not checkpointed by scan_repo', agentic=True, seams=(Seam.ADD_TOOLS, Seam.ADD_SUBAGENTS), caveat='reachable as vvaharness.sdk.remediate(finding, repo=...)'), Stage('s11', Phase.REMEDIATE, 'Validate', None, 'not checkpointed by scan_repo', agentic=True, caveat='reachable as vvaharness.sdk.validate(finding, remediation, ...)')); source annotation tuple[Stage, ...]. Then For _BY_ID, assign {s.id: s for s in STAGES}; source annotation dict[str, Stage]. Then For CHECKPOINTED, assign tuple((s.id for s in STAGES if not s.payload.startswith('not checkpointed'))); source annotation tuple[str, ...].
// Source: vvaharness/sdk/stages.py:111-116
// Source signature: stage(stage_id: str) -> Stage
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stage(stage_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/stages.py:112-112
  In source order: Retain source documentation literal source_literal_112_4; it is not a model call.
  // Source: vvaharness/sdk/stages.py:113-116
  Perform the following protected operations {
    // Source: vvaharness/sdk/stages.py:114-114
    End this invocation with _BY_ID[stage_id].
  }
  // Source: vvaharness/sdk/stages.py:115-116
  On the first matching source exception KeyError, in handler order {
    // Source: vvaharness/sdk/stages.py:116-116
    Raise KeyError(source_template_116_23) with explicit source cause None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/stages.py:119-122
// Source signature: stages_in(phase: Phase | str) -> tuple[Stage, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stages_in(phase) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/stages.py:120-121
  In source order: Retain source documentation literal source_literal_120_4; it is not a model call. Then Evaluate once Phase(phase); assign in source target order to wanted.
  // Source: vvaharness/sdk/stages.py:122-122
  End this invocation with tuple((s for s in STAGES if s.phase is wanted)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/stages.py:125-128
// Source signature: stages_with(seam: Seam | str) -> tuple[Stage, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stages_with(seam) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/stages.py:126-127
  In source order: Retain source documentation literal source_literal_126_4; it is not a model call. Then Evaluate once Seam(seam); assign in source target order to wanted.
  // Source: vvaharness/sdk/stages.py:128-128
  End this invocation with tuple((s for s in STAGES if wanted in s.seams)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/stages.py:131-133
// Source signature: injectable_stages() -> tuple[Stage, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn injectable_stages() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/stages.py:132-132
  In source order: Retain source documentation literal source_literal_132_4; it is not a model call.
  // Source: vvaharness/sdk/stages.py:133-133
  End this invocation with tuple((s for s in STAGES if s.injectable)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/stages.py:136-146
In source order: Evaluate once ['CHECKPOINTED', 'STAGES', 'Phase', 'Seam', 'Stage', 'injectable_stages', 'stage', 'stages_in', 'stages_with']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.models import ContextPackage, FinalReport, Finding, SeedPackage, TaskManifest, ThreatModel` at source line 21: `source_detail/vvaharness/models/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/sdk/stages.py.sudo.md). Exact strings in the evidence asset support this conversion.
