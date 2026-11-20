# P8-validation examples

## 1. Consensus threshold (verified pass-1 file)

Source, `vvaharness/validation/synthesis/_consensus.py:146-157`:
```
        evaluated = [s for s in votes.values() if s != GateStatus.SKIP]
        if not evaluated:
            chosen_status, confidence = GateStatus.SKIP, SynthesisConfidence.FLAGGED
        else:
            counter = Counter(evaluated)
            top_frequency = max(counter.values())
            top_statuses = [s for s, freq in counter.items() if freq == top_frequency]
            if len(top_statuses) == 1 and top_frequency >= MIN_CONSENSUS_VOTES:
                chosen_status, confidence = top_statuses[0], SynthesisConfidence.HIGH
            else:
                chosen_status = _most_conservative_status(top_statuses)
                confidence = SynthesisConfidence.FLAGGED
```
SudoLang, `vvah/vvaharness/validation/synthesis/_consensus.sudo`:
```
    evaluated = votes values where status != SKIP
    if (evaluated is empty) {
      [chosen_status, confidence] = [SKIP, FLAGGED]
    } else {
      counter = count of each status in evaluated
      top_frequency = max count
      top_statuses = statuses with count == top_frequency
      if (length(top_statuses) == 1 && top_frequency >= MIN_CONSENSUS_VOTES) {   // MIN_CONSENSUS_VOTES = 2
        [chosen_status, confidence] = [top_statuses[0], HIGH]
      } else {
        chosen_status = _most_conservative_status(top_statuses); confidence = FLAGGED
      }
    }
```

## 2. Tool narrowing gate (written in pass 2)

Source, `vvaharness/validation/subagents/_loader.py:93-111` (excerpt):
```
        if tools_override is not None:
            override_set = set(tools_override)
            narrowed = tuple(
                t for t in (subagent.tools or ())
                if t in override_set or t in FACT_TOOLS
            )
            subagent = replace(subagent, tools=narrowed)
        if prompt_suffix:
            subagent = replace(
                subagent, prompt=f"{subagent.prompt.rstrip()}\n\n{prompt_suffix}"
            )
        # 0 and None both leave the persona unmetered
        subagent = replace(subagent, max_model_calls=max_model_calls or None)
```
SudoLang, `vvah/vvaharness/validation/subagents/_loader.sudo`:
```
    if (tools_override != null) {
      // narrows only: a tool the persona does not declare is never added; FACT_TOOLS are never dropped
      subagent.tools = [t for each t in (subagent.tools || []) if t in tools_override || t in FACT_TOOLS]
    }
    if (prompt_suffix) subagent.prompt = rstrip(subagent.prompt) + "\n\n" + prompt_suffix
    subagent.max_model_calls = max_model_calls || null   // "0 and None both leave the persona unmetered"
```

## 3. Model instruction: mandatory parallel persona spawn (written in pass 2)

Source, `vvaharness/validation/prompts/system.md:68-77`:
```
### Step 2 — Spawn all three personas in one message
Spawn ALL THREE personas listed below — security-architect, penetration-tester,
AND cross-repo-analyzer — in a SINGLE message using parallel `task()` calls.
This is MANDATORY, not situational: spawn all three on every finding, regardless
of repo count, finding type, or your own judgment of relevance. ...
```
SudoLang, `vvah/vvaharness/validation/prompts/system.sudo.md`:
```
  Constraints {
    // Step 2 — Spawn all three personas in one message
    "Spawn ALL THREE personas listed below — security-architect, penetration-tester, AND cross-repo-analyzer — in a SINGLE message using parallel `task()` calls. This is MANDATORY, not situational: spawn all three on every finding, regardless of repo count, finding type, or your own judgment of relevance. ..."
```
