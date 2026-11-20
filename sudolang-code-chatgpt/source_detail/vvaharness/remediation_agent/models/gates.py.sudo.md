# vvaharness/remediation_agent/models/gates.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/models/gates.py.evidence.json`. SHA-256: `31a1ed4342767736ea6be13e3440b405ea7db1888cb66a85449c5c22252b6a0c`.

```sudo
// Source: vvaharness/remediation_agent/models/gates.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field; preserve alias and import-time effects. Then Evaluate once Literal['pass', 'partial', 'fail']; assign in source target order to EvidenceGateStatus.
// Source: vvaharness/remediation_agent/models/gates.py:25-25
In source order: Evaluate once EvidenceGateStatus; assign in source target order to GateStatus.
// Source: vvaharness/remediation_agent/models/gates.py:28-32
interface Gates {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/models/gates.py:30-32
  In source order: For source, assign Field(default='fail', description='Gate A — attacker-controlled source identified'); source annotation EvidenceGateStatus. Then For sink, assign Field(default='fail', description='Gate B — security-relevant sink reachable from source'); source annotation EvidenceGateStatus. Then For missing_control, assign Field(default='fail', description='Gate C — missing/insufficient validation'); source annotation EvidenceGateStatus.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/models/gates.py.sudo.md). Exact strings in the evidence asset support this conversion.
