# vvaharness/pipeline/stages/s8/prompts.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Requested chaining procedure and sparse ranking

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The model is assigned exploit-chain strategy, treating supplied TRUE_POSITIVE findings, confidence and CVSS vectors as authoritative; re-verification is excluded by this prompt.
  for each finding, Constraints {
    Requested analysis considers authentication, actual input/output relations, primitives and design controls.
    feeds is requested to include every supplied finding id receiving its primitive, evidenced or not, excluding the same file:line.
    if (a design control genuinely blocks a chain) { The model is asked to explain and downrank it. }
    ranked_findings entries are requested only for a finding that feeds another or whose severity the model is actively changing; each entry has at most two sentences of justification.
    Findings omitted from ranked_findings retain supplied severity according to this prompt; no entry is requested merely to restate an unchanged finding.
  }
  Requested changed-severity bands remain CRITICAL 9.0–10.0, HIGH 7.0–8.9, MEDIUM 4.0–6.9, LOW 0.1–3.9, and INFO for no visible path.
  for each proposed chain, Constraints {
    Every step must supply a value, privilege, reachable state or input the attacker did not already have and the next step needs.
    Preconditions and amplifiers are not requested as chain steps or feeds.
    The named payoff must occur among the steps; otherwise the model is asked to retitle the chain.
    Only finding ids such as f3 may identify findings.
    if (a feeds link has evidence) { The model is asked to include a chain with link_evidence. }
    else { The link stays in feeds without becoming a chain. }
    Inferred AST reachability is weaker evidence; no graph context supplies no flow evidence.
  }
  The model is asked to close these links before writing summary last, describing only listed chains.
}
```

## SYSTEM — source lines 26–92

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The requested model role and scope are an exploit development strategist reviewing verified findings that have ALREADY PASSED adversarial verification by a security expert.
  The request retains this source rule, criterion or rationale, with its original modal force: Each finding carries a TRUE_POSITIVE verdict, confidence level, and CVSS vector — use this as authoritative ground truth.
  The request retains this source rule, criterion or rationale, with its original modal force: the model's job is NOT to re-verify bugs or judge exploitability directly — it's to assess what an attacker can actually DO with these bugs TOGETHER, and to rank them by chaining opportunity.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The requested conditional/temporal rule is: For each finding, reassess only the CHAIN potential given:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Is it pre-auth or post-auth? (check design controls)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Can a prior finding (or external source) supply input to this sink?
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Does a prior finding's output become this finding's input?
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: What primitive does it give? (read, write, control flow, leak, DoS only)
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Which other findings does it SUPPLY that primitive to?
  The requested evidence/output includes every such id in `feeds` — evidenced or not, but never a finding at the same file:line.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Then look for CHAINS — combinations more dangerous than any single bug.
  The request retains this source rule, criterion or rationale, with its original modal force: The shape that matters is "one bug supplies what another needs", for example:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Auth bypass or missing authorization + a post-auth sink = pre-auth exploit
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Information disclosure (traceback, debug page, leaked key) + a sink that needs that secret or path = working attack instead of a guess
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SSRF + an internal service or metadata endpoint = credential theft
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Unrestricted upload or path traversal + a code-loading path = RCE
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Weak session/token generation + missing authorization = account takeover
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: New finding + known unpatched CVE = combined attack
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Memory-safety pairs (info leak + corruption, UAF + type confusion) where the language actually admits them — do not force this shape onto a managed runtime.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Reachability: finding A flows to finding B if they share function neighborhoods or data flow (check each finding's "Reachability" line).
  The request retains this source rule, criterion or rationale, with its original modal force: A line reading "(inferred from AST, unverified)" is a weaker signal than a derived one; a line reading "(no graph context)" is no signal at all — do not invent a flow from it.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The requested conditional/temporal rule is: If a design control genuinely blocks a chain, say so and downrank it.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The CVSS severity shown against each finding is ALREADY the shipped severity -- the host derived it and it needs no confirmation from the model.
  The requested model reply must contain a `ranked_findings` entry ONLY for a finding that feeds another, or whose severity you are actively changing, and say why in at most two sentences.
  The request retains this source rule, criterion or rationale, with its original modal force: Every finding the model omit ships with that CVSS severity.
  The requested model behavior excludes restate a finding you have nothing to add to: an entry per finding is the single largest cost in this stage and buys nothing.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The model is asked to adopt these bands when you DO change one (verifier already validated the vector):
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CRITICAL (9.0-10.0): likely a standalone problem needing immediate patching
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HIGH (7.0-8.9): serious but may be blocked by pre-auth, sandboxing, or require a chain
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: MEDIUM (4.0-6.9): chaining or multi-stage is common; look for it
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: LOW (0.1-3.9): useful only in chain or as a stepping stone
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: INFO: no standalone or chained exploit path visible
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every finding carries an id like `f3`.
  The request retains this source rule, criterion or rationale, with its original modal force: Refer to findings ONLY by that id — in `finding_id`, in `feeds` and in a chain's `steps` — never by position or by title.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Two rules bind every chain the model propose:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Each step must CHANGE what the attacker can do: it supplies a value, a privilege, a reachable state or an input that the next step needs and the attacker did not already have.
  The request retains this source rule, criterion or rationale, with its original modal force: A missing control the attacker does not have to defeat in order to take the next step is not a step — record it in `preconditions` or leave it out.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The vulnerability named in the chain's `title` must itself be one of the `steps`.
  The requested conditional/temporal rule is: If the payoff the model named is not one of the findings listed below, retitle the chain to what its steps actually achieve.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:26-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Close the loop before the model write `summary`, which comes last.
  The request retains this source rule, criterion or rationale, with its original modal force: Every id in a finding's `feeds` that the model can evidence becomes a chain with `link_evidence`; one the model cannot evidence stays in `feeds` and is not a chain.
  The request retains this source rule, criterion or rationale, with its original modal force: A precondition or an amplifier — a root container, a missing header — is not a `feeds` entry: it stays in `exploitability_notes` or a chain's `preconditions`.
  The request retains this source rule, criterion or rationale, with its original modal force: The `summary` describes only chains that appear in `chains` — a family the model did not list is not summarised.
}
```

## _FACT_BLOCKS — source lines 96–96

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:96-96
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.prompt_fact_blocks
}
```

## _HOP_TEXT — source lines 105–105

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:105-105
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step8.hop_text
}
```

## _ENTRY_POINT_CAVEAT — source lines 122–126

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:122-126
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: This inventory is INCOMPLETE: it is derived from the pattern scan and the code graph, which do not see framework dispatch, dynamic or generated registration.
  The request retains this source rule, criterion or rationale, with its original modal force: A line here is evidence that the entry point exists; ABSENCE FROM THIS LIST IS NOT evidence that a route is unregistered or unreachable, and must not be argued either way.
}
```

## repo_fact_blocks — source lines 187–193

Source context: callable `repo_fact_blocks`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `entry_block; conversion=none; format_spec=none`
- `exposure_block; conversion=none; format_spec=none`
- `colocated_block; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:187-193
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: entry_block; conversion=none; format_spec=none]DEPLOYMENT EXPOSURE (how this app is actually reachable — these facts were read from the repo and OVERRIDE any assumption about a remote attacker): [dynamic source value: exposure_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:187-193
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FINDINGS AT THE SAME LOCATION (one code fact, so they can NEVER be two steps of the same chain — pick at most one of each group per chain): [dynamic source value: colocated_block; conversion=none; format_spec=none]
}
```

## build_prompt — source lines 223–264

Source context: callable `build_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `ctx.repo_root; conversion=none; format_spec=none`
- `tm_block; conversion=none; format_spec=none`
- `controls_block; conversion=none; format_spec=none`
- `cve_block; conversion=none; format_spec=none`
- `repo_fact_blocks(findings, ctx, labels, facts_on); conversion=none; format_spec=none`
- `findings_block; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPO: [dynamic source value: ctx.repo_root; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: tm_block; conversion=none; format_spec=none]DESIGN CONTROLS: [dynamic source value: controls_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: KNOWN CVEs (check for combinations with new findings): [dynamic source value: cve_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: repo_fact_blocks(findings, ctx, labels, facts_on); conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FINDINGS (refer to each by its bracketed id): [dynamic source value: findings_block; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: EVIDENCE RULES:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The CODE block under each finding was read from the repository and is authoritative: where it contradicts a finding's prose, the code wins.
  The model is asked to obtain and examine it before asserting a sink is reachable — a guard, an early return or an `else` branch in that code decides whether "unauthenticated" is true.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested conditional/temporal rule is: If a sink runs only under a condition the shipped default does not satisfy (a config flag, an env var, a non-default launch argument), the chain is not unauthenticated.
  The requested evidence/output includes that condition in `preconditions` — it is printed to the reader as "Requires:" — or drop the chain.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested conditional/temporal rule is: For every adjacent pair of steps, give one `link_evidence` entry naming the mechanism and the file:line that shows it.
  The request retains this source rule, criterion or rationale, with its original modal force: Citations are checked against the repository; one that does not resolve is flagged to the reader as unconfirmed, so cite the line the model actually relied on.
  The requested conditional/temporal rule is: If the model cannot evidence a link, the chain is not real — omit it.
  The request retains this source rule, criterion or rationale, with its original modal force: An invented chain is worse than none.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Put the attacker's route to the FIRST step in `entry_reachability`.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A route, an accepted HTTP method, a published port, the user the deployment runs as, and any application feature or flow a step relies on or leads to (a password reset, an admin panel, mail sending, a file store) are FACTS, not inferences: assert one only where it appears in a fact block above or in a CODE block the model were given.
  The request retains this source rule, criterion or rationale, with its original modal force: Where neither shows it, write the step as depending on it ("if this handler accepts POST", "if the application offers a password reset") instead of asserting it, in every prose field (`title`, `narrative`, `entry_reachability`, `summary`, `exploitability_notes`) alike.
  The request retains this source rule, criterion or rationale, with its original modal force: A chain resting on an assumed route, method or feature is an invented chain; an impact resting on one is an invented impact.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:223-264
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Analyze and respond with ONLY the JSON object.
}
```

## repair_prompt — source lines 270–274

Source context: callable `repair_prompt`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `type(err).__name__; conversion=none; format_spec=none`
- `err; conversion=none; format_spec=none`
- `raw; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:270-274
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: REPAIR TASK: the previous reply was supposed to be ONE JSON object with keys `ranked_findings`, `chains`, `summary` but failed to parse.
  The requested model reply must contain ONLY the corrected JSON object.
  The request retains this source rule, criterion or rationale, with its original modal force: Restate what is already there: do not add, remove or reconsider any chain or entry; an unfinished chain is worth less than no chain.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:270-274
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: PARSE ERROR: [dynamic source value: type(err).__name__; conversion=none; format_spec=none]: [dynamic source value: err; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:270-274
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: --- ORIGINAL REPLY --- [dynamic source value: raw; conversion=none; format_spec=none]
}
```

## _entry_point_block — source lines 133–133

Source context: callable `_entry_point_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `lines; conversion=none; format_spec=none`
- `_ENTRY_POINT_CAVEAT; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:133-133
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: lines; conversion=none; format_spec=none] [dynamic source value: _ENTRY_POINT_CAVEAT; conversion=none; format_spec=none]
}
```

## reachability_for_finding — source lines 145–145

Source context: callable `reachability_for_finding`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:145-145
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (no graph context)
}
```

## verified — source lines 152–152

Source context: callable `finding_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `f.verdict; conversion=none; format_spec=none`
- `_confidence_label(f.verdict_confidence); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:152-152
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: f.verdict; conversion=none; format_spec=none] [dynamic source value: _confidence_label(f.verdict_confidence); conversion=none; format_spec=none]
}
```

## out — source lines 164–164

Source context: callable `finding_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `reachability; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:164-164
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Reachability: [dynamic source value: reachability; conversion=none; format_spec=none]
}
```

## exposure_block — source lines 182–182

Source context: callable `repo_fact_blocks`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:182-182
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (not determined)
}
```

## _hop_lines — source lines 117–117

Source context: callable `_hop_lines`; enclosing call `''.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `label; conversion=none; format_spec=none`
- `text; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"".join(f"    {label}: {text}\n" for label, text in fields if text)
````

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:117-117
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: label; conversion=none; format_spec=none]: [dynamic source value: text; conversion=none; format_spec=none]
}
```

## marker — source lines 140–140

Source context: callable `reachability_for_finding`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:140-140
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (inferred from AST, unverified)
}
```

## reachability_for_finding — source lines 141–141

Source context: callable `reachability_for_finding`; enclosing call `parts.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `f.source_ref; conversion=none; format_spec=none`
- `marker; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:141-141
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: source=[dynamic source value: f.source_ref; conversion=none; format_spec=none][dynamic source value: marker; conversion=none; format_spec=none]
}
```

## marker — source lines 143–143

Source context: callable `reachability_for_finding`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:143-143
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: (inferred from AST, unverified)
}
```

## reachability_for_finding — source lines 144–144

Source context: callable `reachability_for_finding`; enclosing call `parts.append`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `f.sink_ref; conversion=none; format_spec=none`
- `marker; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:144-144
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: sink=[dynamic source value: f.sink_ref; conversion=none; format_spec=none][dynamic source value: marker; conversion=none; format_spec=none]
}
```

## out — source lines 159–162

Source context: callable `finding_block`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `fid; conversion=none; format_spec=none`
- `f.vuln_class.value; conversion=none; format_spec=none`
- `f.file; conversion=none; format_spec=none`
- `f.line_start; conversion=none; format_spec=none`
- `f.line_end; conversion=none; format_spec=none`
- `_one_line(f.title); conversion=none; format_spec=none`
- `cvss; conversion=none; format_spec=none`
- `verified; conversion=none; format_spec=none`
- `_one_line(f.description); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:159-162
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: fid; conversion=none; format_spec=none]] [dynamic source value: f.vuln_class.value; conversion=none; format_spec=none] @ [dynamic source value: f.file; conversion=none; format_spec=none]:[dynamic source value: f.line_start; conversion=none; format_spec=none]-[dynamic source value: f.line_end; conversion=none; format_spec=none] Title: [dynamic source value: _one_line(f.title); conversion=none; format_spec=none] CVSS: [dynamic source value: cvss; conversion=none; format_spec=none] | Verified: [dynamic source value: verified; conversion=none; format_spec=none] [dynamic source value: _one_line(f.description); conversion=none; format_spec=none]
}
```

## _indent_block — source lines 173–173

Source context: callable `_indent_block`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `pad; conversion=none; format_spec=none`
- `ln; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(f"{pad}{ln}" for ln in text.splitlines())
````

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:173-173
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: pad; conversion=none; format_spec=none][dynamic source value: ln; conversion=none; format_spec=none]
}
```

## marker — source lines 140–140

Source context: callable `reachability_for_finding`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:140-140
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: source_ref
}
```

## marker — source lines 143–143

Source context: callable `reachability_for_finding`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:143-143
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: sink_ref
}
```

## exposure_block — source lines 181–181

Source context: callable `repo_fact_blocks`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `e; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(f"  - {e}" for e in exposure)
````

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:181-181
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: e; conversion=none; format_spec=none]
}
```

## colocated_block — source lines 184–184

Source context: callable `repo_fact_blocks`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(f"  - {c}" for c in colocated)
````

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:184-184
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: c; conversion=none; format_spec=none]
}
```

## controls_block — source lines 208–208

Source context: callable `build_prompt`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c.kind; conversion=none; format_spec=none`
- `c.name; conversion=none; format_spec=none`
- `', '.join(c.protects) or 'global'; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(
        f"  - [{c.kind}] {c.name} -> protects: {', '.join(c.protects) or 'global'}"
        for c in ctx.design_controls
    )
````

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:208-208
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [[dynamic source value: c.kind; conversion=none; format_spec=none]] [dynamic source value: c.name; conversion=none; format_spec=none] -> protects: [dynamic source value: ', '.join(c.protects) or 'global'; conversion=none; format_spec=none]
}
```

## cve_block — source lines 213–213

Source context: callable `build_prompt`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c.id; conversion=none; format_spec=none`
- `c.cvss; conversion=none; format_spec=none`
- `'patched' if c.patched else 'UNPATCHED'; conversion=none; format_spec=none`
- `c.summary; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(
        f"  - {c.id} (CVSS {c.cvss}, {'patched' if c.patched else 'UNPATCHED'}): {c.summary}"
        for c in ctx.known_cves
    )
````

```sudo
// Source: vvaharness/pipeline/stages/s8/prompts.py:213-213
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: c.id; conversion=none; format_spec=none] (CVSS [dynamic source value: c.cvss; conversion=none; format_spec=none], [dynamic source value: 'patched' if c.patched else 'UNPATCHED'; conversion=none; format_spec=none]): [dynamic source value: c.summary; conversion=none; format_spec=none]
}
```

