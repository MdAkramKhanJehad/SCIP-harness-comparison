# vvaharness/pipeline/stages/s4/prompts.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Requested full S4 investigation passes

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:241-260
Constraints {
  The same model/agent is asked to perform four passes IN ORDER: surface, reachability, co-located weakness classes and sibling sites; no subagent delegation.
  Surface instructions select inline versus tool-read wording, and reachability instructions select graph versus Grep wording from the actual arguments.
  Every pass is a requested procedure, not an assertion the code or model completed it.
}
```

## Budgeted prompt procedure

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:201-225
Constraints {
  The model is told the configured budget, with lookups=max(0,budget-1), and asked to reserve the last model call for a structured outcome.
  Requested surface/reachability wording follows inlined/graph inputs; consolidate breadth into a probe/execute/grep lookup and report all distinct evidenced weaknesses.
  This is a request to allocate model calls, not proof that the requested investigation or final outcome occurs.
}
```

## _CWE_CLAUSE — source lines 23–27

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:23-27
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every finding the model report MUST carry `cwe`: one most-specific CWE id, formatted exactly as "CWE-79".
  The request retains this source rule, criterion or rationale, with its original modal force: This is required, not optional — a finding without a CWE cannot be acted on downstream, so there is no case in which the model leave it out.
  The request retains this source rule, criterion or rationale, with its original modal force: Where the model's task line already gives a suspected weakness class and the model's own analysis agrees with it, use that id; where the model's analysis disagrees, use the id the model's evidence actually supports.
}
```

## _BREADTH_CLAUSE — source lines 32–37

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:32-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One location often holds MORE THAN ONE distinct weakness.
  The request retains this source rule, criterion or rationale, with its original modal force: Report a SEPARATE finding for each distinct weakness class the model have evidence for at a location, each with its own cwe and its own line_start/line_end spanning that specific construct.
  The requested model behavior excludes fold two different classes into one broad finding, and do not split one class into near-duplicate findings. "Evidence for" is the bar — report what the code shows, not what could conceivably be wrong here.
}
```

## _CWE_PAIRS — source lines 42–58

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:42-58
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WEAKNESSES THAT TRAVEL IN PAIRS.
  The request retains this source rule, criterion or rationale, with its original modal force: At one location these co-occur far more often than not.
  The requested conditional/temporal rule is: When the model confirm the first, check for the second and put it in `also_cwes`:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:42-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a cookie set without HttpOnly (CWE-1004) is usually also set without Secure (CWE-614), and often without SameSite (CWE-1275)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:42-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a route with no CSRF token (CWE-352) frequently also has no authorization check (CWE-862) — these are different defects, not two names for one
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:42-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a login endpoint with no rate limit or lockout (CWE-307) commonly also leaks which accounts exist (CWE-204) and may use a weak password policy (CWE-521)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:42-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a weak or unsalted password hash is CWE-916 / CWE-759 / CWE-328 depending on which property fails; pick the one the model's evidence supports and name the others only if they independently hold
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:42-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: user input reaching a template is CWE-79, and reaching a template *engine* is CWE-1336; reaching `eval`/`exec` is CWE-95, not the broader CWE-94
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:42-58
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: a request built from user-controlled host or URL is CWE-918, and if it also follows redirects to an attacker-chosen target, CWE-601 Prefer the most specific id the model's evidence supports.
  The request retains this source rule, criterion or rationale, with its original modal force: A parent id where the child is provable reads as a weaker finding downstream, and the grader may not accept it.
}
```

## _CWE_TOOL_DUTY — source lines 62–64

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:62-64
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The pairs above cover the common cases.
  The request retains this source rule, criterion or rationale, with its original modal force: Call `CweGuidance` only for a CWE those lines do not address, and address that entry's FP CHECKS in the model's rationale.
  The request retains this source rule, criterion or rationale, with its original modal force: Each call re-sends this whole session, so do not look up what the model have just been told.
}
```

## _PLUGIN_TOOL_DUTY_HEAD — source lines 71–71

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:71-71
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A plugin has also registered these graph tools, and they are as callable as the six above:
}
```

## _PLUGIN_TOOL_DUTY_TAIL — source lines 74–76

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:74-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: .
  The request retains this source rule, criterion or rationale, with its original modal force: Their descriptions say what each returns and what an empty result does NOT prove — read them before the model decide a question cannot be answered from the graph.
  The request retains this source rule, criterion or rationale, with its original modal force: A plugin tool costs the same budget as a built-in, so prefer whichever answers the model's actual question.
}
```

## _GRAPH_TOOL_DUTY — source lines 80–89

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:80-89
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model have six graph tools and native Read/Grep/Glob.
  The model is asked to adopt `GraphImpact` to check whether a function is actually reachable before you rely on that in a verdict — do not assume reachability from `GraphImporters`, which only lists files that import a file.
  The model is asked to adopt `GraphNeighbors` or `GraphCommunityOf` to see the call context around a function without reading every file that might call it.
  The model is asked to adopt `GraphSinksInCommunity` to check whether other sinks share this unit's call neighbourhood.
  The model is asked to adopt `GraphContext` for a node's full surroundings in one call, and `GraphImpact` for what is reachable FROM a node when you weigh blast radius.
  The request retains this source rule, criterion or rationale, with its original modal force: Reading a file to answer what a graph tool answers deterministically costs more and gives the model a weaker answer.
}
```

## _VERDICT_CLAUSE — source lines 93–100

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:93-100
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model must reach exactly one of three verdicts: `confirmed` (the model have evidence the claim holds — list every distinct finding), `refuted` (the model followed the threat to wherever it is actually implemented and the claim does not hold — this is a first-class, successful outcome, not a failure, and it is exactly as valuable as a confirmed finding), or `inconclusive` (the model could not reach the evidence needed to decide either way, e.g. a tool or file was unavailable). `refuted` is not a fallback for running low on turns, and `confirmed` is never a default guess — each verdict must be earned by what the model actually read or called.
}
```

## _SCOPE_CLAUSE — source lines 105–112

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:105-112
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FILES lists where the threat model first saw this threat.
  The request retains this source rule, criterion or rationale, with its original modal force: It is a STARTING POINT, NOT A BOUNDARY.
  The request retains this source rule, criterion or rationale, with its original modal force: the model have the whole repository available through Read/Grep/Glob, and the model are expected to leave FILES whenever the evidence leads out of it — a sink in a helper module, the caller that supplies the tainted value, a config or settings module holding the real default, a template that renders the value, a base class carrying the missing check.
  The request retains this source rule, criterion or rationale, with its original modal force: A finding in a file that FILES never mentioned is valid and expected when that is where the threat actually lives; report it with its real path and line.
  The requested model behavior excludes widen into unrelated code for its own sake — follow THIS threat, and follow it as far as it goes.
}
```

## _FP_DISCIPLINE — source lines 116–119

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:116-119
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ALREADY IN PLACE, when present, lists controls that exist in this codebase today.
  The requested conditional/temporal rule is: If one of them mitigates what the model are looking at, either refute the claim, or — if the model still believe it is exploitable — state explicitly in your rationale why that control fails to cover this path.
}
```

## _READ_COMPLETELY_CLAUSE — source lines 123–133

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## The source you need is already here; do not re-fetch it

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:123-133
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The SOURCE CODE block in the model's first user message carries every file in FILES, whole.
  The request retains this source rule, criterion or rationale, with its original modal force: Reading it there costs nothing.
  The request retains this source rule, criterion or rationale, with its original modal force: Calling Read on a path that is already in that block spends a turn to obtain bytes the model were handed, and every such duplicate is re-sent on every later turn of this session — it is the single most expensive mistake available to the model here.
  The request retains this source rule, criterion or rationale, with its original modal force: Call Read only for: a path NOT in FILES that the evidence points the model to, or a file the block explicitly marks as truncated.
  The request retains this source rule, criterion or rationale, with its original modal force: In those cases finish the file — when a result ends with a marker like `@@ lines 1-100 of 340 | next offset 100 @@` the model have seen a fraction, so call Read again at that offset until the model reach the end.
  The request retains this source rule, criterion or rationale, with its original modal force: Silence in the part the model read is not evidence of absence in the part the model did not.
}
```

## _ABSENCE_METHOD — source lines 137–155

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## When the claim is that something is MISSING

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:137-155
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model cannot grep for a decorator nobody wrote, so nothing upstream will hand the model a line number for it.
  The request retains this source rule, criterion or rationale, with its original modal force: This is where recall is lost, and the method is inverted: do not ask "is this construct dangerous", ask "what should be here, and is it?" — which means ENUMERATE the sites first and judge second.
  The request retains this source rule, criterion or rationale, with its original modal force: A finding needs all three:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:137-155
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The site is real and reachable by an external actor — a concrete handler, route, cookie write, session config or storage write.
  The request retains this source rule, criterion or rationale, with its original modal force: Not a hypothetical.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:137-155
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The control genuinely belongs there.
  The requested evidence/output includes the asset it protects and the actor it stops. "Every endpoint should have rate limiting" is not analysis; "/api/login accepts unlimited password guesses against a user-supplied username" is.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:137-155
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: It is absent on THIS path and the model checked.
  The request retains this source rule, criterion or rationale, with its original modal force: Middleware, a base class, a decorator factory, a proxy config or a framework default can supply it somewhere the model have not looked.
  The request retains this source rule, criterion or rationale, with its original modal force: A control applied centrally is NOT missing, and missing that is the classic false positive in this class.
  The request retains this source rule, criterion or rationale, with its original modal force: Enumerate the whole population with Grep, state its size, then report one finding per absent site with its own file and line.
  The requested conditional/temporal rule is: If the control is present everywhere the model enumerated, REFUTE and say how many sites the model checked — that is a real result and it is how the FP rate stays low.
}
```

## _SKILL_DUTY — source lines 159–170

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## Load a lens only when this prompt has not already given you one

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:159-170
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Per-family lenses live under `.vvaharness/skills/<name>/SKILL.md`: the FP traps, the sanitizers that genuinely mitigate, and the patterns worth grepping for in ONE weakness family. access-control, batch-etl, client-side, code-exploration, crypto, csrf, deserialization, hardcoded-creds, iac, injection, log-injection, logic-bug, missing-controls, sensitive-data, sibling-instances, ssrf, templates Read AT MOST ONE, and only when the model need the family-specific FP checks and neither this prompt nor `CweGuidance` has already given them to the model.
  The request retains this source rule, criterion or rationale, with its original modal force: A skill body is large and stays in the model's context for the rest of the session, so a lens the model did not need is paid for on every later turn.
  The request retains this source rule, criterion or rationale, with its original modal force: The absence method and the sibling sweep are already above — do not spend a call fetching them.
  The requested evidence/output includes any skill you did load in your rationale.
}
```

## _SURFACE_INLINED — source lines 174–177

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:174-177
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SURFACE — the source above already carries this unit's files.
  The request retains this source rule, criterion or rationale, with its original modal force: Work from it.
  The request retains this source rule, criterion or rationale, with its original modal force: Call Read only for a path that is NOT shown there, or for one the block marks as clipped.
  The request retains this source rule, criterion or rationale, with its original modal force: Re-reading a file the model were already given spends a turn for bytes the model hold, and the duplicate is re-sent on every later turn.
}
```

## _SURFACE_TO_READ — source lines 181–183

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:181-183
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SURFACE — no source was inlined, so Read every path in FILES, each to its end.
  The request retains this source rule, criterion or rationale, with its original modal force: A paginated result is a prefix: call Read again at the stated offset until the model reach the last line.
  The request retains this source rule, criterion or rationale, with its original modal force: A weakness in the part the model did not read is one the model will report as absent.
}
```

## _BUDGETED_REACHABILITY_GRAPH — source lines 189–191

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:189-191
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REACHABILITY — one `GraphContext` on the implicated symbol returns callers, callees, imports and call paths together.
  The request retains this source rule, criterion or rationale, with its original modal force: An unreachable sink is not a finding, and this is the one question no amount of reading the file answers.
}
```

## _BUDGETED_REACHABILITY_NO_GRAPH — source lines 195–197

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:195-197
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REACHABILITY — one repo-wide Grep for the implicated symbol's name returns its callers with their paths and lines; follow those toward an entry point.
  The request retains this source rule, criterion or rationale, with its original modal force: An unreachable sink is not a finding, and this is the one question no amount of reading the file answers.
}
```

## _REACHABILITY_GRAPH — source lines 229–231

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:229-231
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REACHABILITY — one `GraphContext` call on the implicated symbol returns its callers, callees, imports and call paths together.
  The request retains this source rule, criterion or rationale, with its original modal force: Prefer it over several Reads.
  The request retains this source rule, criterion or rationale, with its original modal force: An unreachable sink is not a finding; a caller the model never looked for is how a real one is missed.
}
```

## _REACHABILITY_NO_GRAPH — source lines 235–237

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:235-237
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REACHABILITY — Grep the repo for the implicated symbol's name to find its callers, and follow them toward an entry point.
  The request retains this source rule, criterion or rationale, with its original modal force: Prefer one wide Grep over several Reads.
  The request retains this source rule, criterion or rationale, with its original modal force: An unreachable sink is not a finding; a caller the model never looked for is how a real one is missed.
}
```

## _SHELL_DUTY — source lines 264–282

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## `execute` — ask a narrow question, get a narrow answer

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:264-282
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model have a POSIX shell.
  The request retains this source rule, criterion or rationale, with its original modal force: Available: `grep`, `sed`, `awk`, `sort`, `head`, `wc`, `python3`, and pipes. `rg`/`ripgrep` is NOT installed — use `grep`.
  The request retains this source rule, criterion or rationale, with its original modal force: Reach for the shell where a whole file is the wrong unit of answer:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:264-282
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `grep -rEn "pat1|pat2|pat3" --include="*.py" .` — every occurrence of SEVERAL patterns at once, each with its path and line number, repo-wide, in ONE call.
  The request retains this source rule, criterion or rationale, with its original modal force: This is how the model make the SIBLINGS pass: one command finds the other places the same weak construct appears, where Grep-then-Read-each is several turns per site.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:264-282
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `sed -n "120,180p" path` — exactly the span the model want.
  The request retains this source rule, criterion or rationale, with its original modal force: Prefer it to Read once the model know roughly where the model are going, e.g. following a caller a grep just located.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:264-282
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `grep -rln pat .` for filenames, `grep -rc pat .` for counts, `... | head -40` to cap a result the model expect to be wide.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:264-282
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where a lens under `.vvaharness/skills/` ships a `probe.sh` beside its SKILL.md, that SKILL.md names it: `sh .vvaharness/skills/<lens>/probe.sh` runs that family's whole pattern battery in ONE turn and prints only the hits, labelled by section.
  The request retains this source rule, criterion or rationale, with its original modal force: A labelled section that comes back empty is itself evidence — it is the absence, established.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:264-282
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Why this matters, concretely: everything a tool returns stays in the model's context and is re-sent to the model on EVERY later turn of this session.
  The request retains this source rule, criterion or rationale, with its original modal force: A whole file read to find one line is paid again on every turn after it.
  The request retains this source rule, criterion or rationale, with its original modal force: Forty lines costs forty lines, once.
}
```

## _SHELL_GRAPH_HANDOFF — source lines 287–289

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:287-289
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The shell does NOT replace the graph tools.
  The request retains this source rule, criterion or rationale, with its original modal force: Text search finds a NAME; `GraphContext` resolves what actually CALLS it, which is the reachability question, and the model's verdict is held until a graph tool has run.
  The request retains this source rule, criterion or rationale, with its original modal force: Grep to locate, graph to prove reachable.
}
```

## _SHELL_NOTES — source lines 293–295

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:293-295
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Notes: grep exits 1 when nothing matched — that is a real answer, not an error, so do not retry it broader and broader hoping for text.
  The request retains this source rule, criterion or rationale, with its original modal force: Quote every pattern.
  The request retains this source rule, criterion or rationale, with its original modal force: Read-only commands only: no writes, no installs, no network, no `git` mutations, and stay inside this repository.
}
```

## _OUTPUT_EXAMPLE — source lines 319–345

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:319-345
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Example of the JSON shape, one confirmed and one refuted outcome: {"outcomes": [ {"unit_id": "threat-t8", "verdict": "confirmed", "rationale": "The bearer token in core/config.py is a single shared secret with no per-caller identity; ALREADY IN PLACE only checks that the token is set, not who holds it.", "findings": [ {"cwe": "CWE-306", "file": "routers/repo_credentials.py", "line_start": 42, "line_end": 58, "repeat_lines": [71, 96], "sink_line": 0, "title": "Missing per-caller authentication", "severity": "high", "description": "...", "exploit_scenario": "...", "recommendation": "...", "preconditions": ["Caller needs no session or bearer token — this route accepts anonymous requests"]} ]}, ^ line_start/line_end, sink_line and repeat_lines: the schema field descriptions are authoritative.
  The request retains this source rule, criterion or rationale, with its original modal force: Here 42-58 spans the whole construct (decorator to end of body); sink_line is 0 because a missing control has no single dangerous statement (a query executed at line 55 would be "sink_line": 55); repeat_lines [71, 96] reports the SAME defect at two more sites with the prose written once — never one 42-96 span swallowing all three. preconditions and exploit_scenario are likewise governed by their own schema descriptions — name the gate (unauthenticated reach, a feature flag, a specific input shape), never leave preconditions empty by default, and let exploit_scenario reach only consequences the code the model read supports. {"unit_id": "threat-t7", "verdict": "refuted", "rationale": "The timing difference in login() is under 2ms across 50 runs and does not correlate with account existence — not exploitable as a side channel.", "findings": []} ]}
}
```

## _ROLE — source lines 348–348

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:348-348
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model confirm or refute ONE specific threat claim against the code that implements it.
}
```

## _PLAN_HEAD — source lines 351–363

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## Planning is mandatory here

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:351-363
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model's FIRST action in every session is `write_todos`.
  The requested model behavior excludes answer, and do not call the outcome tool, before you have written a plan and worked it.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:351-363
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The claim the model were handed is a LEAD, not the scope of the work.
  The request retains this source rule, criterion or rationale, with its original modal force: A plan that only says "check the claim" is a bad plan.
  The request retains this source rule, criterion or rationale, with its original modal force: Every plan covers at least:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:351-363
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Account for EVERY path in FILES — one todo per file, or one todo naming a group of them.
  The request retains this source rule, criterion or rationale, with its original modal force: Their source is already inlined below, so this costs the model no tool calls; what it buys is that no file on the model's surface goes unexamined.
  The request retains this source rule, criterion or rationale, with its original modal force: Load the specialist skill for this weakness family from `.vvaharness/skills/` only if this prompt does not already tell the model the FP checks for it.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:351-363
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Locate where this threat is actually implemented — the sink, the caller that supplies the tainted value, the config or base class holding the real default.
  The request retains this source rule, criterion or rationale, with its original modal force: Work from the inlined source; Read only what is not there.
}
```

## _PLAN_REACHABILITY_GRAPH — source lines 367–370

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:367-370
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Establish REACHABILITY from the call graph, not from the file list: one `GraphContext` call returns callers, callees, imports and call paths together, and `GraphImpact` answers whether anything reaches the symbol at all.
  The request retains this source rule, criterion or rationale, with its original modal force: An unreachable sink is not a finding, and a caller the model never looked for is how a real one gets missed.
}
```

## _PLAN_REACHABILITY_NO_GRAPH — source lines 374–377

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:374-377
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Establish REACHABILITY from the callers, not from the file list: Grep for the implicated symbol's name to find what calls it, and follow those callers toward an entry point.
  The request retains this source rule, criterion or rationale, with its original modal force: An unreachable sink is not a finding, and a caller the model never looked for is how a real one gets missed.
}
```

## _PLAN_TAIL — source lines 381–395

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:381-395
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Decide the claim on that evidence, and address the CweGuidance FP CHECKS for the CWE the model are about to report.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:381-395
// Source list marker 5.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested search/review target is OTHER weakness classes at the same location.
  The request retains this source rule, criterion or rationale, with its original modal force: One handler routinely holds several — a missing authorization check and an injection sink and an unflagged cookie.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:381-395
// Source list marker 6.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested search/review target is SIBLING INSTANCES of whatever you confirm.
  The request retains this source rule, criterion or rationale, with its original modal force: A weak hash in one function is usually the same weak hash in three; Grep for the pattern and report each site.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:381-395
// Source list marker 7.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: For a claim that a control is MISSING, enumerate every place that control belongs before concluding it is absent anywhere.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:381-395
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Mark each todo in_progress as the model start it and completed only when the model have actually done it.
  The request retains this source rule, criterion or rationale, with its original modal force: Keep at least one in_progress until the work is finished.
  The request retains this source rule, criterion or rationale, with its original modal force: Add todos when the evidence opens something new.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:381-395
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The outcome tool is GATED on this list: a call to it while any todo is still pending or in_progress is refused and handed back to the model with the outstanding items named.
  The request retains this source rule, criterion or rationale, with its original modal force: Finishing the plan is the only way to report.
  The requested conditional/temporal rule is: If a todo turns out not to apply, mark it completed and say why — do not leave it open, and do not retry the same verdict without doing the work.
}
```

## PLAN_TOOL_DESCRIPTION — source lines 405–411

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:405-411
Constraints {
  The requested evidence/output includes and update your investigation plan for this threat.
  The request retains this source rule, criterion or rationale, with its original modal force: Call this FIRST, before any other tool and before any verdict, then keep it current as the model work: mark a todo in_progress when the model start it and completed when the model have genuinely finished it, and add todos as new evidence opens new questions.
  The request retains this source rule, criterion or rationale, with its original modal force: This is not optional and it is not only for long tasks — a verdict reached without a worked plan is not acceptable output here.
  The request retains this source rule, criterion or rationale, with its original modal force: Statuses are "pending", "in_progress" and "completed".
  The requested model behavior excludes call this tool twice in one turn.
}
```

## _closing — source lines 315–315

Source context: callable `_closing`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:315-315
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Work the model's plan, make all four passes, then report the outcome object.
}
```

## _cwe_lines — source lines 481–484

Source context: callable `_cwe_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `', '.join(unit.cwes); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:481-484
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CWEs THE DETERMINISTIC SCANNER ALREADY MATCHED HERE: [dynamic source value: ', '.join(unit.cwes); conversion=none; format_spec=none] These are confirmed pattern hits, not the classification of THIS threat.
  The request retains this source rule, criterion or rationale, with its original modal force: The claim above may be a different class entirely, and the scanner cannot see a weakness that consists of something MISSING.
  The request retains this source rule, criterion or rationale, with its original modal force: Treat them as a floor to check, never a ceiling.
}
```

## _file_list — source lines 490–490

Source context: callable `_file_list`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(unit.files); conversion=none; format_spec=none`
- `file_lines; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:490-490
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FILES ([dynamic source value: len(unit.files); conversion=none; format_spec=none]): [dynamic source value: file_lines; conversion=none; format_spec=none]
}
```

## _source_section — source lines 497–499

Source context: callable `_source_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_file_list(unit); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:497-499
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _file_list(unit); conversion=none; format_spec=none] No source is inlined for this unit.
  The model is asked to obtain and examine every path above — the sink lines are a starting point, not the full picture.
}
```

## _unit_block — source lines 519–525

Source context: callable `_unit_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit.id; conversion=none; format_spec=none`
- `unit.size.value; conversion=none; format_spec=none`
- `unit.impact; conversion=none; format_spec=none`
- `unit.likelihood; conversion=none; format_spec=none`
- `unit.actor; conversion=none; format_spec=none`
- `unit.threat; conversion=none; format_spec=none`
- `unit.surface; conversion=none; format_spec=none`
- `unit.asset; conversion=none; format_spec=none`
- `extra_block; conversion=none; format_spec=none`
- `sinks_block; conversion=none; format_spec=none`
- `cwe_block; conversion=none; format_spec=none`
- `eps_block; conversion=none; format_spec=none`
- `comm_block; conversion=none; format_spec=none`
- `cve_block; conversion=none; format_spec=none`
- `_file_list(unit) if files_only else _source_section(unit, code); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:519-525
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: UNIT: [dynamic source value: unit.id; conversion=none; format_spec=none] SIZE: [dynamic source value: unit.size.value; conversion=none; format_spec=none] RISK: [dynamic source value: unit.impact; conversion=none; format_spec=none]/[dynamic source value: unit.likelihood; conversion=none; format_spec=none] ACTOR: [dynamic source value: unit.actor; conversion=none; format_spec=none] CLAIM: [dynamic source value: unit.threat; conversion=none; format_spec=none] SURFACE (prose, from the threat model): [dynamic source value: unit.surface; conversion=none; format_spec=none] ASSET: [dynamic source value: unit.asset; conversion=none; format_spec=none] [dynamic source value: extra_block; conversion=none; format_spec=none][dynamic source value: sinks_block; conversion=none; format_spec=none][dynamic source value: cwe_block; conversion=none; format_spec=none][dynamic source value: eps_block; conversion=none; format_spec=none][dynamic source value: comm_block; conversion=none; format_spec=none][dynamic source value: cve_block; conversion=none; format_spec=none] [dynamic source value: _file_list(unit) if files_only else _source_section(unit, code); conversion=none; format_spec=none]
}
```

## build_initial_prompt — source lines 531–533

Source context: callable `build_initial_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_unit_block(unit, code, graph=graph); conversion=none; format_spec=none`
- `_sweep(call_budget, code is not None, graph); conversion=none; format_spec=none`
- `_closing(call_budget); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:531-533
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _unit_block(unit, code, graph=graph); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:531-533
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _sweep(call_budget, code is not None, graph); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:531-533
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _closing(call_budget); conversion=none; format_spec=none]
}
```

## _batch_duty — source lines 540–555

Source context: callable `_batch_duty`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(units); conversion=none; format_spec=none`
- `ids; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:540-555
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: THIS SESSION CARRIES [dynamic source value: len(units); conversion=none; format_spec=none] UNITS: [dynamic source value: ids; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:540-555
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: They were put together because their files overlap, so one lookup often serves several — that is the point, and it is why the model have them at once.
  The request retains this source rule, criterion or rationale, with its original modal force: What it is NOT is permission to merge them.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:540-555
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Each unit gets its OWN entry in `outcomes`, with its own verdict, its own rationale and its own findings, echoing its own id.
  The request retains this source rule, criterion or rationale, with its original modal force: A unit the model leave out is recorded as uninvestigated, which is worse than a refutation the model had to reason the model's way to.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:540-555
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Two units sharing a file do NOT share an answer: the same handler can satisfy one claim and refute another.
  The request retains this source rule, criterion or rationale, with its original modal force: Decide each claim on its own evidence.
  The request retains this source rule, criterion or rationale, with its original modal force: And a weakness the model find while working one unit belongs to whichever unit's surface actually holds it — file it there, not wherever the model happened to be looking.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:540-555
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report every distinct weakness in EACH unit, proportional to what is actually there.
  The request retains this source rule, criterion or rationale, with its original modal force: These units are NOT owed equal output: one may hold eleven findings while its neighbours hold one each, and that is the correct answer when that is what the code says.
  The request retains this source rule, criterion or rationale, with its original modal force: Enumerate every site the model can evidence — do not ration findings across units, and do not summarise several call sites into one broad finding to keep the reply short.
}
```

## _shared_code_section — source lines 565–567

Source context: callable `_shared_code_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `n_files; conversion=none; format_spec=none`
- `code; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:565-567
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SOURCE CODE — all [dynamic source value: n_files; conversion=none; format_spec=none] file(s) across every unit above, each inlined ONCE: [dynamic source value: code; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:565-567
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A file listed under two units appears here a single time.
  The requested conditional/temporal rule is: When two units name the same path, they are asking different questions of the same code.
}
```

## build_batch_prompt — source lines 576–578

Source context: callable `build_batch_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `_batch_duty(units); conversion=none; format_spec=none`
- `blocks; conversion=none; format_spec=none`
- `_shared_code_section(code, n_files); conversion=none; format_spec=none`
- `_sweep(call_budget, code is not None, graph); conversion=none; format_spec=none`
- `_closing(call_budget); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:576-578
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _batch_duty(units); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:576-578
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: blocks; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:576-578
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _shared_code_section(code, n_files); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:576-578
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _sweep(call_budget, code is not None, graph); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:576-578
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: _closing(call_budget); conversion=none; format_spec=none]
}
```

## _budgeted_sweep — source lines 214–224

Source context: callable `_budgeted_sweep`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:214-224
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: BREADTH IN ONE CALL — a lens under `.vvaharness/skills/` that ships a `probe.sh` runs that whole weakness family across the tree in a single `execute`, and its empty sections are evidence of absence.
  The request retains this source rule, criterion or rationale, with its original modal force: One `grep -rEn "pat1|pat2|pat3"` does the same for patterns the model choose.
  The request retains this source rule, criterion or rationale, with its original modal force: Prefer either over several narrow lookups.
  The request retains this source rule, criterion or rationale, with its original modal force: Then report EVERY distinct weakness the model have evidence for — the claim the model were handed plus anything else the code in front of the model shows: injection, authorization, crypto, secrets, deserialization, sensitive data in logs or responses, request forgery, cookie and transport flags, resource exhaustion, logic flaws.
  The request retains this source rule, criterion or rationale, with its original modal force: A narrow budget is a reason to look at the whole surface in one pass, not a reason to report one finding.
  The requested model behavior excludes spend a call re-fetching bytes you already hold, and do not end with an empty findings list because you ran out of lookups — report what you established.
}
```

## _breadth_sweep — source lines 248–259

Source context: callable `_breadth_sweep`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:248-259
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CO-LOCATED CLASSES — having settled the claim, walk the same location for everything ELSE wrong with it: injection, authorization, crypto and randomness, secrets, deserialization, sensitive data in responses and logs, request forgery, cookie and transport flags, resource exhaustion, logic flaws on amounts and identifiers.
  The requested model role and scope are anchored on your claim and will not see these unless you look deliberately.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:248-259
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SIBLINGS — for anything the model confirm, Grep the repo for two or three phrasings of the same pattern and judge each hit on its own evidence.
  The request retains this source rule, criterion or rationale, with its original modal force: A weak hash in one function is usually the same weak hash in three.
  The request retains this source rule, criterion or rationale, with its original modal force: Each site is its own finding with its own cwe, file and line_start.
  The request retains this source rule, criterion or rationale, with its original modal force: A session that confirms one weakness and makes none of these passes has reported a fraction of what is there.
  The request retains this source rule, criterion or rationale, with its original modal force: Make them even when the claim looks narrow and obvious — that is exactly the case where the rest of the surface goes unexamined.
}
```

## _closing — source lines 314–314

Source context: callable `_closing`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:314-314
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Spend the model's lookups, then report the outcome object.
}
```

## lines — source lines 449–449

Source context: callable `_sink_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `s.file; conversion=none; format_spec=none`
- `s.line; conversion=none; format_spec=none`
- `s.function; conversion=none; format_spec=none`
- `s.snippet; conversion=none; format_spec=none`
- `', '.join(s.cwe); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:449-449
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: s.file; conversion=none; format_spec=none]:[dynamic source value: s.line; conversion=none; format_spec=none] [dynamic source value: s.function; conversion=none; format_spec=none] [dynamic source value: s.snippet; conversion=none; format_spec=none] [dynamic source value: ', '.join(s.cwe); conversion=none; format_spec=none]
}
```

## lines — source lines 464–464

Source context: callable `_cve_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `cve; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:464-464
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: cve; conversion=none; format_spec=none]
}
```

## lines — source lines 471–471

Source context: callable `_community_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:471-471
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: c; conversion=none; format_spec=none]
}
```

## label — source lines 472–473

Source context: callable `_community_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:472-473
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CALL-GRAPH NEIGHBOURHOODS (pass one of these strings verbatim as the `community` argument to GraphSinksInCommunity or GraphCommunityOf)
}
```

## label — source lines 474–474

Source context: callable `_community_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:474-474
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CALL-GRAPH NEIGHBOURHOODS
}
```

## _source_section — source lines 495–495

Source context: callable `_source_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `code; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:495-495
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SOURCE CODE: [dynamic source value: code; conversion=none; format_spec=none]
}
```

## _shared_code_section — source lines 562–563

Source context: callable `_shared_code_section`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:562-563
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: No source is inlined for this session.
  The model is asked to obtain and examine the paths listed under each unit — the sink lines are a starting point, not the full picture.
}
```

## _sink_lines — source lines 452–452

Source context: callable `_sink_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:452-452
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: KNOWN SINKS IN THESE FILES:
}
```

## _entry_point_lines — source lines 459–459

Source context: callable `_entry_point_lines`; enclosing call `lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `auth_tag; conversion=none; format_spec=none`
- `ep.kind; conversion=none; format_spec=none`
- `ep.file; conversion=none; format_spec=none`
- `ep.function; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:459-459
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: auth_tag; conversion=none; format_spec=none] [[dynamic source value: ep.kind; conversion=none; format_spec=none]] [dynamic source value: ep.file; conversion=none; format_spec=none]::[dynamic source value: ep.function; conversion=none; format_spec=none]
}
```

## _entry_point_lines — source lines 460–460

Source context: callable `_entry_point_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:460-460
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ENTRY POINTS:
}
```

## _cve_lines — source lines 465–465

Source context: callable `_cve_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:465-465
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: KNOWN CVEs (hunt for variants/siblings):
}
```

## _community_lines — source lines 475–475

Source context: callable `_community_lines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `label; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:475-475
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: label; conversion=none; format_spec=none]:
}
```

## file_lines — source lines 489–489

Source context: callable `_file_list`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `f; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(f"  {f}" for f in unit.files)
````

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:489-489
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: f; conversion=none; format_spec=none]
}
```

## _unit_block — source lines 508–508

Source context: callable `_unit_block`; enclosing call `extra_lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit.controls; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:508-508
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ALREADY IN PLACE: [dynamic source value: unit.controls; conversion=none; format_spec=none]
}
```

## _unit_block — source lines 510–510

Source context: callable `_unit_block`; enclosing call `extra_lines.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `unit.evidence; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:510-510
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WHERE S2 SAW IT: [dynamic source value: unit.evidence; conversion=none; format_spec=none]
}
```

## _budgeted_sweep — source lines 212–212

Source context: callable `_budgeted_sweep`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:212-212
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Spend the lookups on what the prompt above cannot tell the model, in this order of value:
}
```

## _breadth_sweep — source lines 244–245

Source context: callable `_breadth_sweep`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:244-245
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FOUR PASSES, in this order, before the model report.
  The request retains this source rule, criterion or rationale, with its original modal force: the model have no sub-agents: every pass is yours, and the todo list is what proves the model made them.
}
```

## _budgeted_sweep — source lines 205–207

Source context: callable `_budgeted_sweep`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `budget; conversion=none; format_spec=none`
- `lookups; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:205-207
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: YOU HAVE [dynamic source value: budget; conversion=none; format_spec=none] MODEL CALLS FOR THIS UNIT, and the last one is reserved: every tool except the outcome report is withdrawn on it.
  The request retains this source rule, criterion or rationale, with its original modal force: So the model have [dynamic source value: lookups; conversion=none; format_spec=none] call(s) that may use tools, then the model report.
  The request retains this source rule, criterion or rationale, with its original modal force: Plan the spend before the model spend it.
}
```

## _plugin_tool_duty — source lines 420–420

Source context: callable `_plugin_tool_duty`; enclosing call `', '.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `n; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
", ".join(f"`{n}`" for n in extra)
````

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:420-420
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `[dynamic source value: n; conversion=none; format_spec=none]`
}
```

## _budgeted_sweep — source lines 208–208

Source context: callable `_budgeted_sweep`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:208-208
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The source above already carries every file in FILES.
  The request retains this source rule, criterion or rationale, with its original modal force: the model do not need a single Read.
}
```

## _budgeted_sweep — source lines 210–211

Source context: callable `_budgeted_sweep`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s4/prompts.py:210-211
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: No source was inlined, so one of the model's lookups must be the Read — prefer one call that batches what the model need.
}
```

