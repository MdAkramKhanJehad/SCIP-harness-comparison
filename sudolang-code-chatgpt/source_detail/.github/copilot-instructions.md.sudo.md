# .github/copilot-instructions.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

Supply relationship: operator-facing agent instructions; not an automatic scan-stage action. Packaged installation is separately represented in agentdoc/setup code.

# GitHub Copilot instructions

```sudo
// Source: .github/copilot-instructions.md:18-19
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: This repo is vvaharness, a released CLI security-scanning product.
  The request retains this source rule, criterion or rationale, with its original modal force: The full agent operating manual is in `AGENTS.md` at the repo root — follow it.
}
```

```sudo
// Source: .github/copilot-instructions.md:21-25
Constraints {
  The requested model behavior excludes modify the `vvaharness/` package or hand-write config files to make a scan run.
  The requested conditional/temporal rule is: If a command fails, run `vvaharness setup` / `vvaharness doctor` with the same `--config`, fix the environment (usually a missing credential or the `ANTHROPIC_BASE_URL` gateway), then re-run.
  The request retains this source rule, criterion or rationale, with its original modal force: Report genuine bugs instead of patching the source.
}
```

```sudo
// Source: .github/copilot-instructions.md:27-31
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Scan only code the user is authorized to scan.
  The requested model behavior excludes arm exploit verification or fix mode unless the user asks: exploit verification sends live attack traffic, and fix mode edits source.
  The request retains this source rule, criterion or rationale, with its original modal force: Prompts send target source to the model provider.
  The request retains this source rule, criterion or rationale, with its original modal force: Scans spend real tokens, so run `vvaharness estimate --repo <path>` first (no spend).
}
```

```sudo
// Source: .github/copilot-instructions.md:33-35
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Detection-only: `uv sync` → `uv run vvaharness setup` → `uv run vvaharness scan --repo <path> --stop-after s9`.
  The request retains this source rule, criterion or rationale, with its original modal force: This is a uv project; `pipx install .` / `pip install .` also work.
}
```

```sudo
// Source: .github/copilot-instructions.md:37-43
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The packaged default sets `step_remediate.enabled: false` and `step_validate.enabled: false`, so a plain scan using it skips S10/S11. `sdk`, `full` or a local overlay can enable them. `--remediate` enables S10 only and can edit target source; in-scan S11 needs `step_validate.enabled: true`.
  The request retains this source rule, criterion or rationale, with its original modal force: Standalone `remediate` defaults to fix mode and edits source (`--mode report-only` only proposes fixes).
  The request retains this source rule, criterion or rationale, with its original modal force: Keep `--stop-after s9` to skip both stages with any profile.
}
```

```sudo
// Source: .github/copilot-instructions.md:45-50
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Beta — API only. Exploit verification needs a Postman/OpenAPI/Swagger collection and can only verify findings that map to an HTTP endpoint; everything else stays SAST-only.
  The request retains this source rule, criterion or rationale, with its original modal force: It is localhost-only and sends live attack traffic.
  The request retains this source rule, criterion or rationale, with its original modal force: It turns on when `EV_API_COLLECTION` is set (a stale `.env` value counts), and `--resume` turns it back on for a run that had it.
  The request retains this source rule, criterion or rationale, with its original modal force: To send no traffic, unset `EV_API_COLLECTION` and start a fresh run without `--resume`.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../../assets/original/.github/copilot-instructions.md).
