# vvaharness/plugins/semgrep/triage.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _TRIAGE_PROMPT — source lines 21–36

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model triage Semgrep findings against the code graph.
}
```

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model return leads, not verdicts.
}
```

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: For the file the model are given:
}
```

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Call GraphSemgrepFindings to see what Semgrep flagged and which CWE ids its rules carry.
}
```

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The requested conditional/temporal rule is: For each distinct rule id, call GraphSemgrepTaintTrace and read the role of each step.
  The request retains this source rule, criterion or rationale, with its original modal force: A trace whose source is not attacker-controlled is a lead the model should drop.
}
```

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Call GraphSemgrepSinkCallers.
  The request retains this source rule, criterion or rationale, with its original modal force: A sink no caller reaches is not exploitable as written.
}
```

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Call GraphSemgrepCoverage once.
  The requested conditional/temporal rule is: If the scan was incomplete, say so in your summary, because absence of a finding then carries even less weight than usual.
}
```

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:21-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report at most the ten strongest leads, each as one line: file:line, rule id, CWE, and the single reason the model kept it.
  The request retains this source rule, criterion or rationale, with its original modal force: Drop the rest and state how many the model dropped.
  The requested model behavior excludes report a lead whose trace you could not read; say the trace was absent instead.
}
```

## __all__ — source lines 51–51

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:51-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: semgrep_triage_subagent
}
```

## semgrep_triage_subagent — source lines 42–42

Source context: callable `semgrep_triage_subagent`; enclosing call `SubagentDefinition`; keyword `name`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:42-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: semgrep-triage
}
```

## semgrep_triage_subagent — source lines 43–45

Source context: callable `semgrep_triage_subagent`; enclosing call `SubagentDefinition`; keyword `description`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/plugins/semgrep/triage.py:43-45
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Triages this repository's Semgrep findings against the code graph and returns a short ranked list of leads.
  The model is asked to adopt it instead of reading Semgrep output directly.
}
```

