# vvaharness/agentdoc.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## AGENT_DOC — source lines 26–91

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

# Operating vvaharness (for AI coding agents)

```sudo
// Source: vvaharness/agentdoc.py:26-91
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `vvaharness` is a released CLI security-scanning product. Operate it, do not develop or repair it. It writes a Markdown report and SARIF 2.1.0; findings are triage candidates, not confirmed vulnerabilities.
}
```

## The four rules

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes edit the `vvaharness` package source to make a scan run.
  The request retains this source rule, criterion or rationale, with its original modal force: A hand-edited tool gives unsupported, non-reproducible results.
}
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model behavior excludes hand-write config files. Use a shipped profile via `--config`.
  The request retains this source rule, criterion or rationale, with its original modal force: The one sanctioned exception is a git-ignored `config.local.yaml` overlay.
}
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: On any failure, run `vvaharness setup` (or `doctor`), fix the environment it points to, and re-run. Report bugs with `VVAHARNESS_DEBUG=1`; don't patch around them.
}
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: **Scan only code the user is authorized to scan.
  The requested model behavior excludes arm exploit verification or fix mode unless the user asks.** Exploit verification sends live attack traffic; fix mode edits the user's source.
}
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
Constraints {
  The requested conditional/temporal rule is: Before the model scan: prompts send target source to the configured model provider, and scans spend real tokens.
  Within this instruction's source scope, the model is asked to invoke `vvaharness estimate --repo <path>` first (no spend).
}
```

## Run it

```sudo
// Source: vvaharness/agentdoc.py:26-91
Constraints {
  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.
  Preserve the source example's keys, enum spellings, placeholder values and command arguments.
  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.
}
```

Example data/source notation (untyped):

``````text
pipx install .                     # from the vvaharness folder; or: pip install .
vvaharness setup                   # checks Python, keys, gateway, config
vvaharness scan --repo <path> --stop-after s9   # detection only; --application-id <id> is optional
``````

```sudo
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Pick a profile with `--config vvaharness/config/profiles/<name>.yaml` (`default`, `sdk`, `full`, `taint`, `semgrep`), then re-run `setup` with it. `sdk` uses `ANTHROPIC_SDK_API_KEY` for detection; its S11 needs `ANTHROPIC_API_KEY` / `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_OAUTH_TOKEN` or a `claude` login. `full` needs `OPENAI_API_KEY` only when exploit verification is armed.
}
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The packaged default sets `step_remediate.enabled: false` and `step_validate.enabled: false`, so a plain scan using it skips S10/S11.
  The request retains this source rule, criterion or rationale, with its original modal force: Other profiles or a local overlay can enable them (`sdk` and `full` do). `--remediate` enables S10 only and S10 can edit target source.
  The request retains this source rule, criterion or rationale, with its original modal force: In-scan S11 requires `step_validate.enabled: true`; there is no scan `--validate` flag.
  The request retains this source rule, criterion or rationale, with its original modal force: Standalone `remediate` and `validate` remain available when these flags are false.
  The request retains this source rule, criterion or rationale, with its original modal force: Keep `--stop-after s9` to explicitly skip both stages with any profile, even with `--remediate`.
}
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Exploit verification is Beta — API only. It sends live HTTP attack traffic, including state-changing requests, to a localhost target, and only verifies findings that map to an HTTP endpoint.
  The request retains this source rule, criterion or rationale, with its original modal force: It turns on when `EV_API_COLLECTION` names a Postman/OpenAPI/Swagger collection (a stale value in `.env` counts), and `--resume` turns it back on for a run that had it, even with the variable unset.
  The request retains this source rule, criterion or rationale, with its original modal force: To send no traffic, unset `EV_API_COLLECTION` and start a fresh run without `--resume`. `--stop-after ev` parses the collection and probes the target, then stops before S0 with no model spend. `vvaharness ev-replay --repo <path>` re-checks exploit-verified findings against a redeployed target.
}
```

```sudo
// Source: vvaharness/agentdoc.py:26-91
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Behind an Anthropic-compatible gateway (a JWT-shaped `eyJ…` key), set `ANTHROPIC_BASE_URL=https://<the model's-gateway>/`, plus `SSL_CERT_FILE` if the gateway uses a private CA.
  Within this instruction's source scope, the model is asked to invoke `setup` for exact guidance.
}
```

## On failure

```sudo
// Source: vvaharness/agentdoc.py:26-91
Constraints {
  The model is asked to obtain and examine the one-line `✗ scan failed: …`, run `vvaharness doctor`, fix what it flags (usually a credential or `ANTHROPIC_BASE_URL`), re-run.
  The request retains this source rule, criterion or rationale, with its original modal force: Full trace: `VVAHARNESS_DEBUG=1`.
}
```

## CLAUDE_SKILL — source lines 95–101

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/agentdoc.py:95-101
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: name: vvaharness description: Operate the vvaharness SAST CLI (install, setup, doctor, scan).
  The model is asked to adopt when asked to scan a repo for vulnerabilities with vvaharness.
  The request retains this source rule, criterion or rationale, with its original modal force: Operate the tool; never edit its source or hand-write its config.
  The request retains this source rule, criterion or rationale, with its original modal force: Exploit verification is Beta and API-only; do not arm it unless asked. ---
}
```

## gemini_doc — source lines 106–106

Source context: callable `gemini_doc`; enclosing call `AGENT_DOC.replace`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Formatting/composition call retained as source expression evidence:

````python
AGENT_DOC.replace("(for AI coding agents)", "(for the Gemini CLI)")
````

```sudo
// Source: vvaharness/agentdoc.py:106-106
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (for AI coding agents)
}
```

## gemini_doc — source lines 106–106

Source context: callable `gemini_doc`; enclosing call `AGENT_DOC.replace`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Formatting/composition call retained as source expression evidence:

````python
AGENT_DOC.replace("(for AI coding agents)", "(for the Gemini CLI)")
````

```sudo
// Source: vvaharness/agentdoc.py:106-106
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (for the Gemini CLI)
}
```

