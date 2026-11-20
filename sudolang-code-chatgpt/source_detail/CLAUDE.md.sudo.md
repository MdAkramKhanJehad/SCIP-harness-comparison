# CLAUDE.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

Supply relationship: operator-facing agent instructions; not an automatic scan-stage action. Packaged installation is separately represented in agentdoc/setup code.

# CLAUDE.md

```sudo
// Source: CLAUDE.md:18-19
Constraints {
  The model is asked to obtain and examine `AGENTS.md` in full before doing anything in this repo. It is the operating manual for running vvaharness.
}
```

```sudo
// Source: CLAUDE.md:21-22
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: vvaharness is a *released* CLI security-scanning product — operate it, don't develop or repair it.
  The request retains this source rule, criterion or rationale, with its original modal force: A hand-edited tool gives unsupported, non-reproducible results.
}
```

```sudo
// Source: CLAUDE.md:24-24
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Critical rules (full details in AGENTS.md):
}
```

```sudo
// Source: CLAUDE.md:25-25
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes edit files under `vvaharness/` to make a scan run.
}
```

```sudo
// Source: CLAUDE.md:26-27
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes hand-write config — use a shipped profile via `--config`.
  The request retains this source rule, criterion or rationale, with its original modal force: The one sanctioned exception is a git-ignored `config.local.yaml` overlay.
}
```

```sudo
// Source: CLAUDE.md:28-29
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: On any failure run `vvaharness setup` / `vvaharness doctor`, fix the environment it points to, and re-run.
  The request retains this source rule, criterion or rationale, with its original modal force: Report bugs; don't patch around them.
}
```

```sudo
// Source: CLAUDE.md:30-32
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Scan only code the user is authorized to scan.
  The requested model behavior excludes arm exploit verification or fix mode unless the user asks: exploit verification sends live attack traffic, and fix mode edits the user's source.
}
```

```sudo
// Source: CLAUDE.md:34-36
Constraints {
  The requested conditional/temporal rule is: Before the model scan: prompts send target source to the configured model provider; scans spend real tokens, so run `vvaharness estimate --repo <path>` first (no spend).
}
```

```sudo
// Source: CLAUDE.md:38-41
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Detection-only quick start: `uv sync` → `uv run vvaharness setup` → `uv run vvaharness scan --repo <path> --stop-after s9`. `pipx install .` / `pip install .` also work and need no extra index, because the vendored code-graph SDK ships inside the `vvaharness` distribution.
}
```

```sudo
// Source: CLAUDE.md:43-47
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: > [!WARNING] > S10 remediation can edit the target's source. The packaged default > profile disables S10 remediation and S11 validation; `sdk` and `full` enable > both. `--remediate` enables S10 only; in-scan S11 needs > `step_validate.enabled: true`. `--stop-after s9` skips both with any profile.
}
```

```sudo
// Source: CLAUDE.md:49-56
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: > [!WARNING] > Exploit verification (Beta, API only) sends live attack traffic, including > state-changing requests, to a localhost target.
  The request retains this source rule, criterion or rationale, with its original modal force: It needs a > Postman/OpenAPI/Swagger collection and checks only findings that map to an HTTP > endpoint; all others stay static-analysis only.
  The request retains this source rule, criterion or rationale, with its original modal force: It turns on when > `EV_API_COLLECTION` is set — a stale value in `.env` counts — and `--resume` > turns it back on for a run that had it, even with the variable unset.
  The request retains this source rule, criterion or rationale, with its original modal force: To send no > traffic, unset `EV_API_COLLECTION` and start a fresh run without `--resume`.
}
```


<!-- converted-model-instructions -->
Original supporting evidence: [exact source copy](../assets/original/CLAUDE.md).
