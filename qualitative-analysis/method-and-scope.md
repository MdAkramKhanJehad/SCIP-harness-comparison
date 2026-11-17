# Method and scope

## The comparison unit is a paired decision

A finding belongs here only when it compares both harnesses. The analysis uses a shared situation, identifies the relevant instruction or code path in each harness, and states the decision that differs: read or ignore, investigate or stop, classify one way or another, retain uncertainty or proceed, merge or keep separate.

The layers describe the scale of that decision:

- **High level:** who owns the workflow, what defines investigation coverage, and what identifies a finding.
- **Mid level:** reconnaissance, partitioning, verification, consolidation, and remediation procedures.
- **Low level:** specific inclusion, exclusion, classification, reachability, evidence, or merge rules.

A conflict between the harnesses is not necessarily a defect. Two legitimate security policies can disagree. A difference becomes a direct contradiction only when the same object, conditions, and decision are being compared.

## Three classifications

| Classification | Meaning | Example |
|---|---|---|
| Direct rule opposition | Under the stated conditions, one rule says to perform an action and the other says to exclude or reject it. | Read repository documentation versus ignore it. |
| Conditional policy conflict | Rules lead in different directions, but their application depends on a backend, deployment assumption, exception, or stage. | Browser asset traversal included by one class playbook and excluded as a server-side class by the other verifier. |
| Architectural tradeoff | The designs assign authority or organize work differently; neither issues the literal negation of the other. | Host-owned stages versus a model-directed investigation procedure. |

The documents label these differences instead of presenting every architectural distinction as an opposite instruction.

## Evidence

The existing [comparison](../comparison-results/comparison.md) and [common pseudocode](../comparison-results/pseudocode/README.md) guide navigation. Original source files, configuration, and instruction files support the paired claims. The [source index](evidence/source-index.json) records the cited locations.

The older comparison's revision identifiers are historical metadata; this analysis does not independently establish checkout identities. Likewise, pseudocode coverage and valid source pointers do not prove complete semantic equivalence. The source rules cited here are the authority for this analysis.

The comparison uses the rules of the named stages. For example, reading a document as threat-model context does not establish that a vulnerability in that document will be reported. An instruction to investigate a suspicious flow does not guarantee a confirmed finding. A consolidation prompt that is disabled in a shipped profile cannot explain that profile's observed output.

## Avoiding false oppositions

Both harnesses reject many intended features and non-production paths, require source evidence, and investigate missing controls. Those shared principles are not contradictions merely because their wording differs. The examples below avoid claiming otherwise.

Named exceptions also matter. VulnHunter permits security-relevant infrastructure configuration despite excluding ordinary build files: [infrastructure exception](../VulnHunter/vulnhunt/SKILL.md#L91). Visa Vulnerability Agentic Harness explicitly says fixed-origin path manipulation can belong to another class: [alternative classification](../visa-vulnerability-agentic-harness/vvaharness/skills/ssrf/SKILL.md#L76). Neither qualification can be discarded to manufacture a disagreement.

## Scope and limits

This is a qualitative source analysis of detection and its surrounding preparation, consolidation, remediation intake, and fix-validation interfaces. It excludes the optional exploit verification subsystem and standalone internal defect audits. No scans, model calls, exploit execution, or delivery actions are required or performed for this revision.

The example outcomes are consequences of applying the cited rules. They do not establish how often a model follows those rules, which rule wins when other instructions apply, or which harness achieves better precision or recall. Those questions require controlled runs and independently adjudicated findings.
