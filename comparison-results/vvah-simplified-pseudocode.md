# vvah: simplified pipeline

```
# How one scan runs, top to bottom.  Entry point: orchestrator/scan.py
#
#   [knob]   a knob id from `categories` in vvah.knobs.yaml that controls the step
#   CODE     deterministic Python, no model
#   LLM      a single model call
#   AGENT    a model session that can use tools over many turns
#
# Coverage note: step 6 decides which files are ever examined. Later steps
# only look at files named in a threat's surface_files.

1. Preflight                                                   CODE
   Probe every configured model / provider pair before starting.     [models.*]

2. Auto-exclude (optional)                                     LLM + CODE
   Runs only if [step1.auto_exclude].
   - A model surveys the repo and proposes paths to skip.
   - Code vetoes any proposal that would drop templates, key material,
     secrets or client-side sinks.                                    [step1.auto_exclude_protect_*]

3. S0  Seed                                                    CODE
   Find entry points and sinks by pattern matching.                   [step0.*, step1.exclude_*]

4. Code graph                                                  CODE
   Parse the repo with tree-sitter and cluster it into communities.

5. S1  Build context                                           CODE
   Combine seeds and graph into the threat modeler's input.           [inject.*]

6. S2  Threat model                                            AGENT
   Output: a list of threats, each naming the files it touches (surface_files).
   Limits on the session:
     evidence passed in            [step2.max_*]
     tools                         [step2.allowed_tools] + graph tools, capped by [step2.graph_tool_budget]
     turns / calls / time          [step2.max_turns], [step2.max_model_calls], [step2.deadline]
     must call a graph tool        [step2.require_graph]
     planning mode                 [step2.planning]
   Then keep the first [step2.max_threats] threats and drop any whose files don't exist.

7. S3  Work units                                              CODE
   One unit per threat, ranked.

8. S4  Hunt                                                    AGENT, in parallel
   Units are grouped into batches of [step4.batch_size] by shared files;
   [step4.parallel] batches run at once. Each batch gets one session:
     tools                         Read, Glob, Grep, CweGuidance, graph tools
     skills / planning             [step4.skills], [step4.planning]
     evidence gate                 [step4.evidence_gate]
     turns / calls / time          [step4.max_turns], [step4.max_model_calls], [step4.deadline]
   Output per unit: confirmed | refuted | inconclusive, plus any findings.

9. S5  Clean up candidates                                     CODE
   Drop findings with bad paths, re-anchor line numbers, collapse duplicates
   at the same site. Add hits from built-in detectors if [step5_detectors.enabled].

10. Exploit verification (only when armed)
    classify -> map -> generate payloads -> attack -> oracle -> judge

11. S6  Verify                                                 AGENT, in parallel
    Batches of [step6_verify.batch_size], [step6_verify.parallel] at once.
    Each finding gets: TRUE_POSITIVE | FALSE_POSITIVE | INCONCLUSIVE,
    a confidence 0-10, and a CVSS score.
    Keep:  TRUE_POSITIVE with confidence >= [step6_verify.min_confidence]
           INCONCLUSIVE, marked "undetermined"
    Drop:  everything else

12. S7  Deduplicate                                            CODE, then optional LLM
    Merge findings within [step7_dedup.line_tolerance] lines of each other.
    If [step7_dedup.semantic], a model call also merges findings that mean the same thing.

13. S8  Write report                                           LLM + CODE
    A model writes the report; code validates it. If validation fails,
    fall back to a plain list sorted by severity.

14. S9  Export                                                 CODE
    findings.json, Markdown, SARIF.

15. S10 Remediate (optional)                                   AGENT
    Runs if [step_remediate.enabled] or --remediate.
    Fix the top [step_remediate.top_n_findings] findings by CVSS, each between policy gates.

16. S11 Validate fixes (optional)                              AGENT + CODE
    Runs if [step_validate.enabled].
    Each fix is reviewed by an orchestrator and 3 personas; code combines
    their reports into a consensus status and score.
```
