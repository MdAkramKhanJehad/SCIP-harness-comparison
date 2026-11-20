# vvaharness/skills/iac/SKILL.md

A lens for infrastructure-as-code and pipeline misconfiguration. It tells the model to run its probe first and to read some empty probe sections as findings.

Source: `vvaharness/skills/iac/SKILL.md` (lines 1-94)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/iac/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/iac/SKILL.md:1-94
IacLens {
  name: "iac"
  description: "Find infrastructure-as-code and deployment misconfiguration in Terraform, Dockerfiles, Kubernetes/Helm, compose, CloudFormation, Ansible, and CI pipelines: over-permissive IAM, exposed services, container escape, secrets in manifests, unpinned supply chain, disabled controls. Ships probe.sh, which inventories the platforms present and greps each one's known-bad directives."
  Constraints {
    // prompt-src: vvaharness/skills/iac/SKILL.md:24-25
    Hunt misconfigurations that expose data, escalate privilege, or let an attacker inject code into the build or deploy pipeline.

    // prompt-src: vvaharness/skills/iac/SKILL.md:27-31
    constraint HardGate {
      "HARD GATE — every finding MUST cite the specific resource block, step, or directive (file:line) AND the security property it violates: least privilege, network isolation, supply-chain integrity, or secret hygiene."
      "A best-practice item with no concrete attack path is LOW."
      "Vendor-default settings that match the platform baseline are NOT findings."
    }

    // prompt-src: vvaharness/skills/iac/SKILL.md:33-40 — the model is told to run the probe (see iac/probe.sudo)
    Run "sh .vvaharness/skills/iac/probe.sh [root]" first; read its manifest inventory first.
    "An absent platform is not a finding — do not report Kubernetes hardening for a repo with no manifests."

    // prompt-src: vvaharness/skills/iac/SKILL.md:42-52
    constraint InvertedPolarity {
      "Invert these deliberately — `(none)` here is the finding, not a clean result:"
      `every USER directive` empty: no image drops root.
      `securityContext` / `readOnlyRootFilesystem` empty: containers run unconstrained.
      `NetworkPolicy` empty: flat pod network.
      `audit / logging config` empty: no trail exists.
      `cross-account trust`: hits without a matching `ExternalId` in the same policy are the confused-deputy case.
    }

    // prompt-src: vvaharness/skills/iac/SKILL.md:54-92 — "Judgement the grep cannot make"
    "CI trust boundary is a conjunction." pull_request_target is remote code execution with repository secrets only when the same workflow also checks out the pull request head ref and executes something from it; "Verify all three in one workflow before reporting."
    Event data (titles, branch names, commit messages) inside `run:` is shell injection; the same expression in `if:` or passed via quoted `env:` is not.
    "A `secrets.*` reference is not a finding." It becomes one only when the step executes untrusted code or the secret is written into `env:` / `outputs` where a later step logs it.
    Self-hosted runners are a finding only on a public repository without per-job isolation.
    GitLab `rules:` / `only:` / `except:` that let a deploy job run on a branch the approval gate does not cover is an authorization bypass.
    Ansible Vault material is correct practice; it is exposure only when the vault password or key file is committed alongside it.
    Base images: a digest is pinned; `:latest` or a bare name is not; a moving minor tag is a production-only supply-chain risk.
    Kubernetes `data:` / `stringData:` is base64, not encryption; a sealed-secret or external-secrets reference is not a committed secret.
    Placeholders (${var}, {{ .Values.x }}, $(VAR)) are indirection, but check the committed values.yaml / *.tfvars defaults.
    "Environment decides severity." A public bucket or 0.0.0.0/0 on 22/3389/3306/5432/6379/9200/27017 in production is HIGH; a missing log-retention setting on a development account is LOW.

    // prompt-src: vvaharness/skills/iac/SKILL.md:94
    "Give every finding a concrete remediation: the exact directive to add or remove."
  }
}
