# docs/errors.md

Role: repository/build/operating context, outside scan execution.

Exact source asset: `assets/original/docs/errors.md`. SHA-256 `c66966032cbe42db1db889cacb9e77f0c4522c145eb61e1e52e77a6bbd4f88b1`.

```sudo
// Source: docs/errors.md:1-603
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
<!--
Copyright 2026 Visa, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Errors and Exit Codes

VVAH reports a process exit code for the overall command and may also record a
named `VVAH-E00x` error in the terminal output or the per-run `*_errors.jsonl`
file; the run manifest carries per-stage error counts (`errors_by_stage`), not
named codes. A non-fatal stage error does not necessarily make the process exit
non-zero; check the scan health and error artifact as well as the exit code.

## Process exit codes

| Code | Meaning | Operator action |
|---|---|---|
| `0` | The command completed successfully. | Review findings and scan health. |
| `1` | The command failed, or a scan finished with a degraded report. A degraded scan still writes its report, `findings.json` and SARIF, and the report's Scan Health section shows **DEGRADED** with the reason. For `ev-replay` only, a **completed** replay also exits `1` when at least one finding is still vulnerable; see the note below. | Read the terminal error, the DEGRADED reason in Scan Health, and `*_errors.jsonl`. Fix the named cause and rerun. For `ev-replay`, look for the final `done:` line before you treat `1` as a failure. |
| `2` | The command refused to start or continue because of an invocation, configuration, scope, or validation gate. Most exploit-verification (Beta — API only) preflight refusals also land here — see [Exploit-verification refusals (exit 2)](#exploit-verification-refusals-exit-2) below. | Correct the command, configuration, or scope, then rerun. |
| `3` | The run completed, no remediation was validated as fixed, and at least one case failed validation. A run of only inconclusive cases exits `0`; see [validation](features.md#validate-review-fixes-independently). | Review the validation results and remediate or revalidate the affected cases. |
| `130` | The user interrupted the command with SIGINT or Ctrl-C. | Rerun when ready. |
| `143` | The command was stopped with SIGTERM, for example by a CI job timeout or `kill`. | Rerun. For a scan, `--resume` reuses the stages that finished. |

Scope: this table covers `scan`, `batch`, `remediate` and `validate`. Only
validation produces `3`: `validate`, or a scan or batch that runs S11.
`validate` exits `1` before it starts a validation session in these cases:

| Condition | What to do |
|---|---|
| A network (UNC) `--repo`/`--workspace` | Use a local path |
| A non-empty `--workspace` | Pass a new or empty path |
| `--workspace` or the default temporary workspace resolves inside `--repo` | Pass a `--workspace` outside the repository, or point `TMPDIR` (or `TEMP`/`TMP`) outside it |
| `security-remediation/` is a symbolic link, not a directory, or outside the repository | Replace it with a real directory inside the repository |
| No case is under `security-remediation/`, or a `--finding` id is not found or not validatable | Run `remediate` first, or pass an id that `validate` lists as selected |
| No case has an S10 record in this machine's state store | Run `remediate` for the case again on this machine |

A workspace inside the repository is refused because on
`cli` and `sdk` the S11 session reads `CLAUDE.md` from every parent directory,
which would load the target's own file. `doctor`, `setup`, `estimate` and
`ev-replay` map their outcomes onto codes in their own terms; see
[Exit codes](architecture.md#exit-codes), and read the terminal message, not
only the code.

`1` means the harness broke: the command failed, or the scan report is
degraded. `3` means the fixes did not pass validation. On `3`, also read Scan
Health for the detection result.

`ev-replay` uses `1` for two outcomes. A replay that ran to completion exits
`1` when at least one finding is still vulnerable, and it ends with a
`done: … → <path>_ev-replay.md` line. A replay that stopped on an error exits
`1` without that line. Tell the two apart by the `done:` line, not by a report
file: each replay writes a new timestamped report, and older reports stay. A
missing or non-loopback `EV_TARGET_URL` or `EV_OOB_URL` exits `2`.

Some coverage losses keep exit `0`: failed S4 units, S6 batches that end
`VERIFY_ERROR`, and stages that completed with errors. Read Scan Health,
`run_manifest_*.json` and `*_errors.jsonl` for them. A failed threat model
(S2), S4 units halted by an authentication or proxy failure, or a chain step
(S8) that fell back to the deterministic report makes the report degraded, and
the scan exits `1`.

Exit `0` also covers one refusal. `--resume` needs the checkpoint directory
(under `$VVAHARNESS_STATE_DIR`, default `~/.vvaharness/state`) outside the
scanned repository. If it resolves inside, the scan prints
`refusing --resume: …`, runs no stage and exits `0`; in batch mode that repo
counts as OK. Before you treat a run as clean, confirm that the terminal shows
`[out] wrote …_report.md` for this run: each scan writes a new timestamped
report, and older reports stay in `<repo>/security-scan/`.

Exit `2` is a refusal rather than a failure, but it is not a promise that the
run spent nothing overall: the validation step has its own preflight, so a
configuration it rejects — a cross-vendor persona, for instance — surfaces as
`2` at the end of a scan whose detection stages have already run and billed.

### Batch exit codes

A batch run (`--repo-file`) reports one exit code for the whole invocation
and maps refusals onto it differently from a single-repo run. Refusals that
exit `2` on a single-repo run — an empty scan scope, an exploit-verification
input or reachability refusal, a validation gate — are recorded as an
ordinary per-repo failure and surface as batch exit `1`; read
`<workspace>/batch_summary.md` and each repo's terminal output to see which
repos were refused rather than broken.

An authentication (VVAH-E001) or proxy/network (VVAH-E002) failure in S4 or
S6 stays inside that repo: the row ends `DEGRADED` or carries `VERIFY_ERROR`
findings, and the batch moves on. The same failure in any other stage stops
the whole batch at that repo, because every remaining repo would fail the same
way; later repos are not scanned. Read the terminal output to find the repo
and stage. Fix the credential or proxy, run `vvaharness doctor`, and run the
batch again without `--resume`.

### Exploit-verification refusals (exit 2)

Exploit verification (Beta — API only) refuses in more ways than the table row
can list; most of its preflight refusals exit `2`. The families:

- the collection file is missing or cannot be parsed;
- `step6_exploit_verification.enabled: true` with no collection to use (no
  `EV_API_COLLECTION`, and no checkpointed collection on a `--resume` run), or
  `enabled: false` with `EV_API_COLLECTION` set. Leave `enabled: auto`, as
  shipped, or make the two agree;
- `--stop-after ev` with no `EV_API_COLLECTION` and no `--resume`;
- an `EV_API_COLLECTION` on a network (UNC) path. Copy the collection to a
  local disk;
- the collection gate fails — the refusal reads "cannot run as configured —
  fix and re-run:" with one line per failed check;
- a declared auth strategy is missing its credential, or an
  `EV_AUTH_STRATEGY` / `EV_AUTH_API_KEY_LOCATION` value is not one of the
  accepted ones;
- an unrecognized `step6_exploit_verification.on_unreachable` or
  `.on_auth_failure` value in the profile;
- mTLS client material that cannot be loaded — a missing file, non-PEM
  material, or a missing or wrong `EV_TARGET_CLIENT_KEY_PASSPHRASE`. These
  are reported through the collection gate's refusal, so read the itemized
  lines under it rather than assuming the collection itself is at fault;
- a `models.exploit_verification` role that is missing (`judge` and
  `classify` are required), unusable, or missing its backend credential. Exploit verification re-checks its roles at its own
  preflight and refuses with exit `2`, naming the role — the check that
  covers what the startup credential probe cannot see, such as a `--resume`
  run's checkpointed collection or a role on a transport its purpose cannot
  use. A gap the startup probe does see — a fresh run with the collection
  set and the role's backend credential missing — is reported there instead
  and exits `1`, like any other backend-credential gap found before a scan
  starts. Either exit is a configuration problem to fix up front, not the
  in-flight VVAH-E001 authentication failure described below;
- nothing in the collection reachable at the probe. This is also how a
  non-local `EV_TARGET_URL` surfaces: the configuration error is reported as
  unreachability ("no collection endpoint is reachable — every endpoint was
  skipped by the safety envelope — exploit verification only targets
  localhost"), so fix the URL rather than the network.

For a setup and limitations overview, see
[exploit verification](features.md#exploit-verification-add-live-api-evidence).

## Named errors

### Model refusals (no E-code)

A provider or model that refuses a request — an Anthropic `stop_reason:
refusal`, an OpenAI `refusal` message or `content_filter` finish, or an
OpenAI-compatible endpoint's `cyber_policy` 400 — is raised as a typed refusal on
every route (`sdk`, `openai`, `deepagents`, `cli`, and the MCP-bridged `cli-mcp`
leg) instead of surfacing as an empty or unparseable reply. It has no E-code of
its own; the message reads

    model refused the request (route=<route>, category=<category>, stage=<stage>): <detail>

where `category` is the provider's own label when it sends one (for example
`cyber` or `reasoning_extraction`; `content_filter` for that OpenAI finish;
`cyber` for a `cyber_policy` rejection), else `unspecified`, and `<detail>` is the
provider's text, redacted and capped at 200 characters. Each refused **call**
bumps `llm_model_refusals` (see
[architecture.md](architecture.md#pipeline-diagnostics-markdown)), and the record in
`*_errors.jsonl` carries the message.

A refused call is re-sent unchanged **once**, and only on a route whose
provider is `anthropic` (`via: cli`, `via: sdk`, or `via: deepagents` that
resolves to that provider), under
the top-level profile key `refusal_retries` (`1`, the default, or `0` to turn
the resend off; any other value is refused when the profile loads). Some
models answer an identical repeat; on one that refuses every repeat the
resend costs one more billed send. It is the same model and the same
prompt, never a fallback model. A second refusal is final. On an
OpenAI-compatible route (`via: openai`, or `via: deepagents` resolving to
it) a refusal is never re-sent, because a provider may restrict the account
after repeated flagged requests. A refused S6 batch of several findings is
not re-sent whole: on a route whose provider is `anthropic`, with `refusal_retries: 1`, it is
split once into one-finding batches (`s6_batch_refusal_split`, under
`step6_verify.split_retry`) so the members the classifier did not object to
still get verdicts; a split singleton that is refused again is final, so each
member costs at most one batch send plus one singleton send. There is still no
unforced or effort-free retry and no transport fallback for a refusal, and a
refusal during a deadline resume is raised rather than replayed. Resends are
counted in `llm_refusal_retry_attempted` / `llm_refusal_retry_recovered`. An S4
unit ends with outcome `guardrail`, the members of an S6 batch end in the
`GUARDRAIL_BLOCKED` drop bucket (excluded, undetermined), and S2/S7/S8 degrade
as on any failed call, with the message in the report (S8 ships the
deterministic chain report, as it does when its one json-repair re-ask of an
unparseable chain reply is refused; the remedy is to point `models.chain` at a
model that passes, or to accept that report). Refusals do not count toward the S4/S6
guardrail abort gate, which counts only provider content-guardrail blocks on
the CLI/OAuth path.

On the `cli` and `cli-mcp` routes every Claude Code session is started with
`CLAUDE_CODE_DISABLE_REFUSAL_RETRY=1` and `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1`,
which turn off the CLI's own resend of a refused turn on the same or a fallback
model. On `deepagents`, a refused S10 remediation is reported as a failed
finding naming the refusal instead of being re-sent for post-hoc verdict
extraction, and a refused exploit-verification attacker raises the typed refusal
instead of returning an empty reply.

### VVAH-E001: Authentication failure

The configured LLM provider rejected or could not use the credential. What
happens next depends on the stage that hit the failure:

- S4 stops starting units and marks every unit it did not analyze `halted`
  (the terminal shows `[s4] unit <id> HALTED`). The report is degraded, so the
  scan exits `1`.
- S6 records each batch that hit the failure as `VERIFY_ERROR` (excluded,
  undetermined) and continues with its other batches.
- In S1, S2, S7 or S8, the scan stops with exit `1`.

Fix the credential and run `vvaharness doctor`. Then run the scan again
**without** `--resume`. A resume re-runs S4 when any unit halted, but when S4
is reused it keeps the S6 batches that this failure recorded as
`VERIFY_ERROR`, so those findings stay unverified.

### VVAH-E002: Proxy, TLS, or network configuration failure

The request could not reach the configured provider because of a proxy, TLS,
certificate, gateway, or related network configuration problem. VVAH-E002
has the same effect as VVAH-E001 in each stage.

Check the configured endpoint, proxy, and CA settings, then run
`vvaharness doctor`. See the [TLS guide](USER_GUIDE.md#tls-and-private-gateways)
for backend-specific settings. Retry only after correcting the configuration,
and follow the same `--resume` rule as for VVAH-E001.

### VVAH-E003: Degenerate LLM response

The provider returned a response that fell below the response-quality floor:
too short or empty by characters or output tokens, or a long, well-formed
reply that is missing an expected marker. It is recorded as a non-fatal stage
error when the owning stage can continue; a stage may fail if its error
handling cannot recover. The first two consecutive failures for a stage only
log the diagnostic `degenerate response accepted and used; it raises only
after more repeats` (code `RESPONSE_DEGENERATE_ACCEPTED`, field
`error_code=VVAH-E003`); the third consecutive failure for the same stage
raises. That diagnostic on stderr during an otherwise healthy run is
expected, not a fault.

Review `*_errors.jsonl`, check the model and stage configuration, and consider
reducing prompt size or increasing the relevant output budget.

The quality floor also applies to agentic replies on every route. For an
agentic reply only the character floor applies, because the token count covers
the whole session, not that reply.

### VVAH-E004: Prompt exceeds the context ceiling

`via: deepagents` only. The harness refuses a prompt estimated above 150,000
tokens before it sends anything, so the refused call costs nothing. No setting
changes this ceiling. The affected unit, such as a chunk or model pass, fails
while the pipeline continues.

Make the call pack less: lower `batch_size` (`step4`, `step6_verify`), set
`inline_source: false` so the session reads files with tools, lower
`step8.prompt_token_budget`, or narrow the scan scope.

### VVAH-E005: Truncated LLM response

The provider reply reached its output-token limit, and the one retry also came
back cut off or could not be made. The affected unit fails while the pipeline
continues. A clipped reply is never used as a result.

Lower the stage's `effort` (the tier's thinking is billed inside the same
`max_tokens` as the reply), reduce what the call packs, or raise `max_tokens`
where it is below the route's retry ceiling. See the
[configuration guide](USER_GUIDE.md#5-configuration).

VVAH-E005 can occur on every route (`sdk`, `openai`, `cli`, `deepagents`), on
single-prompt and agentic calls. Before the unit fails, the route resends the
clipped request once with double the output budget, up to its retry ceiling:

| Route | Retry ceiling |
|---|---|
| `sdk`, `cli` | 64000 tokens |
| `deepagents` | The model node's `max_tokens`, else 64000 tokens |
| `openai` | The model node's `max_tokens`, else none |

A request already at its ceiling gets no doubled retry, because a retry that
cannot grow would only pay for the same call twice; the first truncation fails
the unit. On every shipped profile, `step2`, `step4` and `step7_dedup` request
64000, so those stages get no doubled retry on `sdk`, `cli` or `deepagents`.
`step6_verify` (32000) gets one on every route. `step8` gets one in the
`default` and `semgrep` profiles (48000), but not in `full`, `sdk` or `taint`
(64000). A `via: deepagents` call with no `max_tokens` (exploit-verification
classify) runs at 64000. On `openai`, a doubled budget that the provider
rejects also fails the unit with VVAH-E005. To give a stage at its ceiling room
for the retry, lower its `max_tokens`; otherwise lower `effort` or shrink what
the call packs.

An agentic retry resends only the clipped model request, not the whole
session: tool calls already made are not repeated. If the retry also clips,
the owning stage records the final failure and handles it like any other
failed call.

The `recovered: true` VVAH-E005 warning in `*_errors.jsonl` is written when
the retry starts, not when it succeeds. `llm_truncated_retry_recovered` counts
the retries that succeeded; a failed retry is recorded by the owning stage
without `recovered: true`.

> **At the ceiling, the `effort` tier is the remaining lever.** A call at its
> ceiling that sends an `effort` tier on `via: sdk`, `openai` or `deepagents`
> is resent once without the tier, at the same budget. The provider's default
> reasoning then applies, so on a model that reasons by default the resend can
> clip again. The terminal shows `reply clipped at an output budget the route
> could not grow; retrying once without the effort tier, which shares that
> budget` (code `REPLY_CLIPPED_RETRY`, fields `stage=`, `label=`, `detail=`).
> The counters `<stage>_truncated_retry_attempted` / `_recovered` (`s1`, `s2`,
> `s4`, `s6`, `s7`, `s8`, `ev_classify`) are under `metrics` in
> `findings.json` and in the report's Pipeline Diagnostics `Primary model
> calls re-dispatched` line. For S2, S4 and S6 the resend is a whole agentic
> session of up to `max_turns` model calls; an S6 batch that still clips is
> split, and each child gets the same one resend. The unit fails only if the
> resend also clips. There is no such resend on `via: cli` (the resend would
> still carry the global `cli.effort`), for one-shot calls on a `via: sdk`
> model node with `thinking_budget`, or with `effort: null`; there the first
> truncation is final.

On `via: cli` the harness recognizes this failure from the CLI's own error
message. If a newer `claude` build changes that message, the failure shows as
an untyped CLI error instead of VVAH-E005; report it with the CLI version.

**`via: cli` also has a second output-budget failure, and the harness handles
it instead of reporting it.** The CLI sometimes continues a long reply across
turns, and its final result then holds only the last turn: the start of the
reply is missing, and for a JSON-emitting stage the opening brace is gone. The
backend rebuilds the full text from the stream, after it checks that the
result really is the tail of that text. It counts the event under
`cli_continued_replies` and prints a `NOTE` that names the stage. **Nothing is
lost, but the count is a signal to raise that stage's `max_tokens`**, because a
split reply costs extra turns.

### VVAH-E006: Tool-call state not round-tripped

`via: deepagents` only. Some models return opaque per-call state on a tool call
and require the client to send it back on every replay of that call, or the
endpoint answers HTTP 400. On Chat Completions the route keeps every field an
endpoint puts on a tool call outside the standard schema and sends it back on
the same call. VVAH-E006 means the endpoint rejected a replayed tool call as
missing its per-call state.

This is **not a role-specific limitation.** Any `via: deepagents`
session that makes one tool call and then continues fails identically on its
SECOND tool-using turn, including ordinary graph-tool usage. Only a role
whose actual, resolved config advertises no tool at all (never any role by
name; see [backend selection](features.md#models-choose-a-backend) for a routing overview)
cannot hit it.

The affected unit fails loudly (non-halt: the pipeline continues past it), but
it is **deterministic**: the same model and route fail the same way in every
session, so fix it before a scan instead of retrying past it.
`vvaharness doctor` and the scan's start-up probe each round-trip one real tool
call. Both probes report VVAH-E006 for the `preprocess`, `threatmodel` and
`verify` roles, and the start-up probe stops the run with exit `1` before any
scan spend. Other tool-using roles show this error only when the scan reaches
them.

What to do:

1. Run `vvaharness doctor --config <profile>` and read the probe line for the
   role.
2. If that probe line reports VVAH-E006 and the doctor output shows no
   "retrying on Chat Completions" warning for the model, pin
   `use_responses_api: false` on the role's model and run the doctor probe
   again. The route moves to Chat Completions on its own when a model's first
   Responses API call in the process fails. It never moves for a role that
   pins `use_responses_api: true`. A model that shows the warning already runs
   on Chat Completions and needs no pin.
3. If the probe still reports VVAH-E006 after you pin Chat Completions, route
   the role `via: openai`. On Chat Completions that route replays every field
   of a tool call and keeps the same graph and tool set. This works for
   `preprocess`, `threatmodel`, `deepdive`, `verify` and the
   exploit-verification roles. It does not work for `remediate`, because S10
   fix mode needs edit tools that `via: openai` does not have, or for
   `validate`, because S11 runs a `via: openai` role on its default backend.
   For those two roles, choose a model that does not need its tool-call state
   echoed back. See [backend selection](features.md#models-choose-a-backend)
   for route-specific limitations.

Limits of the Chat Completions echo:

- The route sends the state back only when the endpoint returns it as a
  top-level field of the tool call. A field in another place is not echoed, and
  VVAH-E006 stays.
- Neither probe covers the `remediate` or `validate` role. Before you rely on
  S10 fix mode or S11 with such a model, run one remediation and one
  validation on a test target and check that neither reports VVAH-E006.

Turning off the role's tools also avoids the failure, but the role then loses
all code-graph evidence, and a verdict rests on that evidence. Use it only as
a last resort, and treat the result as reduced coverage.

### VVAH-E007: Model-call budget exhausted

Raised only by S4 on `via: deepagents`; other routes do not meter
`max_model_calls`, and `step4.max_turns` stops their sessions.
`step4.max_model_calls` caps a unit's model calls and reserves the last one
for the verdict: once spent, every tool but the outcome report is withdrawn
and the model is told this is its final turn. This code is raised when that
forced final turn still did not end the session on the outcome tool — the
unit's budget was too small for it to converge, not a parse or provider
failure. Non-halt: the affected unit fails, the pipeline continues past it,
and the scan's overall exit code does not change.

Raise `step4.max_model_calls`, or reduce what the unit's prompt packs so it
converges within the existing budget. `0` turns the budget off; on
`via: deepagents` the session is then bounded by `step4.deadline` (when set)
and a recursion budget, not by `step4.max_turns`. See the
[configuration guide](USER_GUIDE.md#5-configuration).

A deadline **resume** does not raise it: when `step4.deadline` expires after the
forced final turn was issued, the budget re-issues that final turn for the
resumed session (`via: deepagents`), so the resume can still end on the outcome
tool instead of failing on its first call. See the
[configuration guide](USER_GUIDE.md#5-configuration).

### VVAH-E008: Call timed out

A model call or agentic session exceeded its wall-clock budget: `step2.timeout`,
`step6_verify.batch_wall_clock_ceiling`, `step8.timeout`, `step_remediate.timeout`,
`step_validate.timeout`, or, where no stage knob applies, the route's fallback
clock. Every one of those budgets is the `high`-tier value: a **request** clock
(one single-prompt call or one model request) is scaled ×1.1 at `xhigh` and
×1.2 at `max`; a **session** clock (an agentic session, or the S6 batch
ceiling) is scaled ×1.1 and ×1.5. Two clocks differ. `step_validate.timeout`
applies as configured: `step_validate.effort` does not scale it.
`step_remediate.timeout` applies as configured on every route except
`via: cli`, where the global `cli.effort` tier scales it, because S10 has no
effort knob of its own. Every shipped profile ships `effort: high`, so no
shipped clock value changes; raising a stage's `effort` raises its other
clock(s) by the same factor.
See [Timeouts and retries](architecture.md#timeouts-and-retries) for each
route's fallback clock.

What happens next is route-specific:

- `via: cli`: the subprocess is sent `SIGINT` on its own process group, given
  a 20s grace to exit (a session that flushes its session file on `SIGINT`
  stays resumable; `SIGKILL` never is), then killed outright if it ignored
  that. When the call carries a stage session id (S2, S4, S6 and S8 calls
  do; the stage owns the resume), the route raises VVAH-E008 at once with no
  in-route salvage and no second attempt — see the **stage deadline**
  paragraph below for what follows. Without a stage session id (for example
  S10, and the turn-watchdog and legacy probe paths), the harness asks the
  stopped session to resume and give its final answer with tools disabled —
  re-passing the call's `--json-schema` when it had one and the binary
  advertises the flag, so a structured call is salvaged as structured
  output rather than free text; if that salvage succeeds, the call returns
  the salvaged text instead of failing, and `*_errors.jsonl` carries a
  `recovered: true` VVAH-E008 record (see below). If the salvage fails too,
  one fresh attempt is made before VVAH-E008 is finally raised.
- Agent SDK sessions (the `via: cli` MCP-bridged leg, S10 fix mode on
  `via: sdk`, and S11 on `via: cli` and `via: sdk`): the deadline sits inside
  the live client session; on expiry the harness calls the SDK's
  `interrupt()`, drains for a further grace period in case a result message is
  already in flight, then lets the client's own close sequence run
  uninterrupted so the underlying `claude` child is never left running in the
  background.
- `via: sdk` / `via: openai`: the vendor SDK has already retried the request
  twice at the transport layer; the harness raises VVAH-E008 immediately
  rather than treating the timeout as a generic connection error worth
  another resend (other transient errors are still retried).
- `via: deepagents`: the session's future is cancelled, which propagates into
  the LangGraph stream and aborts the in-flight HTTP request. S10 and S11
  sessions have no subprocess to orphan, so this cancellation is immediate —
  no interrupt/grace step.
- The S6 batch sweep: a multi-finding batch past its ceiling is
  split-retried as singletons when `split_retry` is on; a singleton (or
  `split_retry: false`) resolves `VERIFY_ERROR` (excluded, undetermined)
  instead.

- The **stage deadline** (`step2.deadline`, `step4.deadline`,
  `step6_verify.batch_deadline`, `step8.deadline`) raises VVAH-E008 with route
  `stage` when the stage itself abandons the session. On every route the stage
  gives the route a session clock that ends about 20s before the deadline, so
  the route stops its own session first and one deadline hit counts once in
  `llm_call_timeouts`. S8 then replays the chain analysis from the transcript
  at once. S2, S4 and S6 first resume the stopped session for a final answer
  (`via: deepagents`, and the plain `via: cli` leg on CLI 2.1.286 or later);
  on other routes, or when the resume is not possible, they replay the
  transcript instead. See
  [Timeouts and retries](architecture.md#timeouts-and-retries).

- The **S11 backstop**: a second clock wraps each whole S11 session at
  `step_validate.timeout` plus 40 seconds on every route, and raises
  VVAH-E008 with route `backstop`. It stops a session that its route clock
  did not stop. An `[s11] heartbeat:` line prints every 60 seconds with the
  case, the elapsed time, the quiet time and a tool-call count for each agent
  that has made a call (`none` before the first call). It prints on a fixed
  cadence, even while a session is busy, so it also shows a session stuck in
  a tool loop (VVAH-E009 below).

VVAH-E008 never halts the run: the affected unit or batch fails (or is
salvaged) and the pipeline continues. A timeout in S4, S6 or S10 leaves the
exit code unchanged. An S11 timeout reports that case `INCONCLUSIVE`, and S11
goes on to the next case; `validate`, and a scan that runs S11, then exit
`1`, because a session failure outranks every verdict. An inconclusive
verdict from a completed session still exits `0`. A timeout that fails
S2, or that sends S8 to its deterministic fallback report, makes the report
degraded, so the scan exits `1` after it writes the report.

A `recovered: true` VVAH-E008 record in `*_errors.jsonl` means that a
`via: cli` call without a stage session was saved by resuming the stopped
session.

Raise the stage's `timeout` / `batch_wall_clock_ceiling` knob (for S11,
`step_validate.timeout`), lower that stage's `effort` (S10 has no effort knob,
and `step_validate.effort` does not change the S11 clock), or reduce what the
call packs (fewer findings per S6 batch, a smaller prompt). See the
[configuration guide](USER_GUIDE.md#5-configuration).

A fixed CLI/SDK start-up and shut-down overhead — process spawn, the Agent
SDK's own `close()` escalation, and similar fixed costs — sits outside every
one of these budgets; it is not something raising a `timeout` buys back.

### VVAH-E009: Repeated identical tool call

An S10 remediation session or an S11 validation session called the same
tool with the same input 20 times in a row, and was stopped as
non-converging rather than left to run out its timeout. The message names
the stage, route, agent, tool and repeat count. The guard counts calls per
agent in the order they stream, so calls from parallel personas interleave
and reset each other's count.

The guard is a backstop. On `via: deepagents`, `max_turns` is a LangGraph
recursion floor (`max_turns + 900`), not a cap; the model-call caps
(`step_remediate.max_model_calls`, `step_validate.max_model_calls` and
`step_validate.orchestrator_max_model_calls`) bound those sessions first.
VVAH-E009 still fires when a cap is `0`, when one turn issues many parallel
identical calls, or for a subagent with no cap of its own. In S10 it applies
on `via: deepagents`; in S11 it applies on every route, since it costs
nothing while a session behaves.

VVAH-E009 never halts the run. In S10 the finding is recorded not fixed, any
in-flight edit is reverted, and S10 goes on to the next finding. In S11 the
case is recorded `INCONCLUSIVE`, the same as any other S11 session failure,
and S11 goes on to the next case. The failure is logged once, without a
traceback.

The limit has no profile knob. If a session trips it, lower the stage's
`max_model_calls` cap rather than leaving it at `0`, and report the session
log (`security-remediation/<case>/validation_session_*.jsonl` for S11) as a
bug if it repeats.

## Glob/Grep tool-call timeouts (`via: deepagents`)

On `via: deepagents` stages (S6 verify and the S6-EV attacker), an unscoped
model tool call — `Glob()` with no pattern, or `Grep("/")` against the whole
repo — can time out on a repo of any real size. The transcript shows a
vendor-generated message such as `glob timed out after 5s` or
`grep timed out after 15s`; this is not a `VVAH-E00x` code — the vendor
`deepagents` filesystem backend hardcodes these budgets (5s glob / 15s grep)
with no per-call override, so vvaharness cannot raise them from the tool
call site itself. The timed-out call still returns to the model (partial or
empty results, not an exception), so it is usually a silent quality issue —
a missed file — rather than a stage failure.

Operator action: set `step6_verify.tool_timeout_s` (seconds; default `null`
= vendor default) in your profile to raise both budgets for S6 verify; the
exploit-verification attacker keeps the vendor budgets. Reducing
`step6_verify.parallel` also helps indirectly, by lowering how many
concurrent Glob/Grep calls compete for repo I/O on a large tree.

## The error log (`*_errors.jsonl`)

Each record is one JSON object per line: `ts`, `stage`, `unit`, `error`, plus
any extra context fields the logging site adds (including an `error_code` such
as `VVAH-E003` when one applies, or the `category` of a model refusal).
Exception records carry a `traceback` — redacted, and capped to its final 4000
characters.

A record may carry `recovered: true`: a retry or repair that started, a
warning whose reply was still used, or a policy note. Such a record is not a
lost unit. If the retry or repair then fails, a separate record without the
flag reports the failure.

Only `scan`, including each repo of a batch, writes the per-run
`<repo>/security-scan/*_errors.jsonl`. `doctor`, `remediate`, `validate`,
`ev-replay` and a scan's own preflight append their records to
`pipeline-errors.jsonl` in the current working directory.

The manifest's `errors_by_stage` counts every logged record for a stage,
including transients the pipeline recovered from, so a non-zero count beside
a clean console does not mean coverage was lost. Cross-check `*_errors.jsonl`
(a record stamped `recovered: true` is an attempt or a note, not a lost unit) and the
report's Scan Health section, which reflects actual coverage. In batch mode
the manifest's `errors_by_stage` reflects only the last repo of the batch,
not the whole invocation.

## Where to look

- Terminal output gives the immediate error and recovery hint.
- `*_errors.jsonl` contains per-stage non-fatal errors when they are recorded.
- `run_manifest_*.json` contains stage health, timing, and error summaries for
  scans that write a manifest.
- `vvaharness doctor` checks configured backend readiness; it does not replace
  reviewing scan artifacts.

``````

