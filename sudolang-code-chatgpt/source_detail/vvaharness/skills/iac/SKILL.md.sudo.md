# vvaharness/skills/iac/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Platform applicability and conjunctions

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/iac/SKILL.md:24-94
Constraints {
  Requested first operation: run sh .vvaharness/skills/iac/probe.sh [root], then read the platform inventory before judging platform directives.
  if (a platform has no manifests) { The model is asked not to invent a platform-hardening finding. }
  Requested findings cite a resource/step/directive file:line and a violated security property.
  Best-practice-only items without a concrete attack path are requested as LOW; vendor-baseline defaults are excluded.
  Empty USER, securityContext/readOnlyRootFilesystem, NetworkPolicy or audit/logging sections are requested as absence candidates, not clean results. Cross-account trust without matching ExternalId is the source's confused-deputy criterion.
  if (pull_request_target AND checkout of PR head AND execution from that checkout occur in the same workflow) { The model is asked to assess the secret-bearing RCE case. }
  pull_request_target alone is not enough.
  Requested distinctions include event interpolation in run versus quoted env/if usage; secrets executing untrusted code or later logged versus direct SHA-pinned action use; public self-hosted non-isolated runners versus private/ephemeral runners; uncovered GitLab approval branches; Vault ciphertext plus committed decryption key versus ciphertext alone; per-FROM digest/latest/minor-tag judgments; base64 Kubernetes secrets versus external/sealed references; variable placeholders versus their committed defaults.
  Environment remains a qualitative severity dependency; the source examples assign production public/admin/database exposure HIGH and missing development log retention LOW.
  Every requested finding identifies the exact remediation directive to add/remove.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/iac/SKILL.md:1-4
Constraints {
  The source declares name = "iac". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find infrastructure-as-code and deployment misconfiguration in Terraform, Dockerfiles, Kubernetes/Helm, compose, CloudFormation, Ansible, and CI pipelines: over-permissive IAM, exposed services, container escape, secrets in manifests, unpinned supply chain, disabled controls. Ships probe.sh, which inventories the platforms present and greps each one's known-bad directives.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is infrastructure-as-code and deployment misconfiguration in Terraform, Dockerfiles, Kubernetes/Helm, compose, CloudFormation, Ansible, and CI pipelines: over-permissive IAM, exposed services, container escape, secrets in manifests, unpinned supply chain, disabled controls. Ships probe.sh, which inventories the platforms present and greps each one's known-bad directives.
}
```

# Iac Lens

```sudo
// Source: vvaharness/skills/iac/SKILL.md:24-25
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hunt misconfigurations that expose data, escalate privilege, or let an attacker inject code into the build or deploy pipeline.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:27-31
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — every finding MUST cite the specific resource block, step, or directive (file:line) AND the security property it violates: least privilege, network isolation, supply-chain integrity, or secret hygiene.
  The request retains this source rule, criterion or rationale, with its original modal force: A best-practice item with no concrete attack path is LOW.
  The request retains this source rule, criterion or rationale, with its original modal force: Vendor-default settings that match the platform baseline are NOT findings.
}
```

## Probe first

```sudo
// Source: vvaharness/skills/iac/SKILL.md:35-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `sh .vvaharness/skills/iac/probe.sh [root]` — a MANIFEST INVENTORY naming which platforms actually exist here, then labelled `file:line` sections of known-bad directives per platform, plus cross-cutting TLS and credential literals.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:39-40
Constraints {
  The model is asked to obtain and examine the inventory first.
  The request retains this source rule, criterion or rationale, with its original modal force: An absent platform is not a finding — do not report Kubernetes hardening for a repo with no manifests.
}
```

## Polarity: some sections are findings when EMPTY

```sudo
// Source: vvaharness/skills/iac/SKILL.md:44-45
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The probe lists presence for controls whose *absence* is the defect.
  The request retains this source rule, criterion or rationale, with its original modal force: Invert these deliberately — `(none)` here is the finding, not a clean result:
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:47-47
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `every USER directive` — no image drops root.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:48-48
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `securityContext` / `readOnlyRootFilesystem` — containers run unconstrained.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:49-49
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `NetworkPolicy` — flat pod network; one compromised pod reaches every service.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:50-50
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `audit / logging config` — no trail exists to detect abuse.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:51-52
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `cross-account trust` — hits *without* a matching `ExternalId` in the same policy are the confused-deputy case.
}
```

## Judgement the grep cannot make

```sudo
// Source: vvaharness/skills/iac/SKILL.md:56-59
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CI trust boundary is a conjunction. `pull_request_target` alone is fine.
  The request retains this source rule, criterion or rationale, with its original modal force: It is RCE with repo secrets only when the workflow *also* checks out the PR head ref *and* executes something from that checkout (install, build, test, lint).
  The model is asked to establish all three in one workflow before reporting.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:60-62
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Event data is attacker-authored. Issue and PR titles, branch names, commit messages, bodies. `${{ github.event.* }}` inside `run:` is shell injection; the same expression in an `if:`, or passed via `env:` and quoted, is not.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:63-68
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: **A `secrets.*` reference is not a finding.** Every workflow that deploys anything reads one, so `secrets reaching a step` is the sweep's highest-volume label.
  The request retains this source rule, criterion or rationale, with its original modal force: It becomes a finding on one of two conditions: the step it reaches executes untrusted code, or the secret is written into `env:` / `outputs` where a later step logs it.
  The request retains this source rule, criterion or rationale, with its original modal force: A secret passed straight to a SHA-pinned action is neither.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:69-73
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Self-hosted runners need both qualifiers. The finding is a self-hosted runner on a public repo without per-job isolation (fresh VM or container per job) — a fork PR then runs on infrastructure that keeps state between jobs.
  The request retains this source rule, criterion or rationale, with its original modal force: On a private repo, or with ephemeral runners, `runs-on: self-hosted` is ordinary configuration.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:74-77
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: GitLab `rules:` can route around approval. A `rules:` / `only:` / `except:` clause that lets a deploy or release job run on a branch the approval gate does not cover is an authorization bypass, not a hygiene nit.
  The model is asked to obtain and examine which branches the gate protects before judging.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:78-81
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Ansible Vault is only as good as where the key lives. `$ANSIBLE_VAULT;` material in the repo is correct practice — it is a credential exposure when the vault password or key file is committed alongside it, since anyone with the repo can then decrypt.
  The model is asked to establish both probe labels together.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:82-83
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Base-image pinning. Judge each `FROM`: a digest is pinned, `:latest` or a bare name is not, a moving minor tag is a prod-only supply-chain risk.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:84-86
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Kubernetes `data:` is base64, not encryption. Material under `data:` or `stringData:` is a committed secret; a sealed-secret or external-secrets reference is not.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:87-89
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Placeholders are not literals. `${var}`, `{{ .Values.x }}`, `$(VAR)` in a credential position are indirection — but check the committed `values.yaml` / `*.tfvars` defaults they resolve to.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:90-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Environment decides severity. A public bucket, or `0.0.0.0/0` on 22/3389/3306/5432/6379/9200/27017, in prod is HIGH; a missing log-retention setting on a dev account is LOW.
}
```

```sudo
// Source: vvaharness/skills/iac/SKILL.md:94-94
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Give every finding a concrete remediation: the exact directive to add or remove.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../../../../assets/original/vvaharness/skills/iac/SKILL.md).
