# VulnHunter: simplified pipeline

```
# How one scan runs, top to bottom.
#
#   [knob]   a knob id from `categories` in vulnhunter.knobs.yaml that controls the step
#
# Only Part 1 is code. Part 2 is instructions written in prompt files
# (vulnhunt/SKILL.md and phases/*.md): the model is told to follow them,
# but nothing in code enforces them.

PART 1 - Launcher (Python: vulnhunter-agent/agent/runner.py)

1. Clone the target repo.                                    [code.clone_depth]
2. Stop if results from an earlier scan are already there.   [code.prior_results_guard]
3. Open one Claude Agent SDK session:
     model                       [anthropic.model]
     tools                       [scan.allowed_tools], minus Bash
                                 (Bash only with --no-read-only --enable-bash)
     permission mode             [scan.permission_mode]
     no system prompt, no turn limit, no cost limit
4. Send "/vulnhunt <clone path>" plus precomputed run info
   (results dir, branch, sha, repo URL, model, Bash on/off).  [code.kickoff_metadata]
5. While subagents are still running, send a "keep going" message.   [code.continuation_prompt]
   Give up after this many re-prompts with no progress.             [code.max_stalled_continuations]
6. Publish results, if enabled.                              [publish.enabled]
7. File GitHub issues, if enabled: take Confirmed findings,
   drop duplicates, post one issue each.                     [issues.enabled]

PART 2 - The /vulnhunt skill (prompt: vulnhunt/SKILL.md)

Before starting
  - Interactive runs stop if the model is weaker than [skill.min_model].
  - Pick a mode: STATIC (read and reason only) or EXECUTE (needs Bash;
    installs dependencies and actually runs tests).

Phase A - Recon                                   (one subagent: phase1_recon)
  - List every input the app accepts, every dangerous sink, and a call
    graph [prompt.recon.callgraph_depth] levels deep.
  - Modules imported by more than [prompt.recon.shared_infra_import_share]
    of entry points are "shared infrastructure".
  - Group inputs into partitions SG-1..SG-n: inputs that reach the same
    app functions go together (union-find).
  - Split any partition with more than [prompt.recon.oversize_inputs]
    inputs or [prompt.recon.oversize_files] files.
  - Tag each partition PRODUCTION or DEV-ONLY. Only PRODUCTION is hunted.
  - Write a threat model: 3 auth questions, each answered with a
    file:line or NONE.

Phase B - Hunt                                    (many subagents)
  - Start one tracer for every pair of
      (PRODUCTION partition, vulnerability class group [prompt.hunt.class_groups])
    plus [prompt.hunt.sink_driven_agents] sink auditors, which start from
    sinks instead of inputs.
  - Run them in waves of [prompt.hunt.wave_size]; sink auditors go last.
  - A tracer follows each input in its partition forward through the code
    [prompt.investigation_discipline] and labels it:
      CANDIDATE      looks exploitable
      SAFE           reaches a sink but is defended
      NO-MATCH       never reaches a sink of this class
      CROSS-CLASS    a problem, but for a different class group
      DESIGN-INTENT  behaves as designed
  - A CANDIDATE must pass every hard gate, in order; the first failure
    removes it.                                              [prompt.hard_gates]
      0 not design intent, 1 reachable, 2a attacker-controlled,
      2b not sanitized, 3 gives a new capability
  - Merge results:
      - an input is a CANDIDATE if any tracer said so
      - candidates at the same sink file:line become one
      - every input in the inventory must have exactly one label
      - check what happens when security-relevant inputs are left out   [prompt.absent_input_analysis]

Phase C - Verify (try to disprove)                (one subagent: phase2b)   [prompt.phase2b.*]
  - Count the candidates first; the verdict table must have that many rows.
  - Skip re-reading source when all tracers cited the same evidence at
    the same file:line.
  - Run nine checks on each candidate.
  - Verdict: CONFIRMED or FALSE POSITIVE. A FALSE POSITIVE must cite the
    file:line that rules it out, or the finding stands.

Phase D - Reproduce                               (one subagent: phase3 + phase3c)
  For each CONFIRMED finding whose severity is in [prompt.scope.phase3_severity_floor]:
  - Write a PoC and an exploit test.
  - EXECUTE mode runs the test; STATIC mode reasons through it.
  - Test passes  -> write a fix strategy (the fix is not applied).
    Otherwise    -> downgrade to Code Smell or Potential, or drop it.

Phase E - Sweep                                   (one subagent: phase3d)
  Grep the whole repo for each confirmed root cause. New hits go back
  through the pipeline as candidates.

Report                                            (orchestrator: phase4)
  After count checks, write one VULN-NNN entry per sink location.
```
