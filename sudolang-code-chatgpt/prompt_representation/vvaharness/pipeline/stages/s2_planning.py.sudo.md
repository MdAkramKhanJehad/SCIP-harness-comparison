# vvaharness/pipeline/stages/s2_planning.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## PLAN_SYSTEM_PROMPT — source lines 20–53

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

## Planning is mandatory here

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model's FIRST action is `write_todos`.
  The requested model behavior excludes emit the threat model before you have written a plan and worked it.
  The request retains this source rule, criterion or rationale, with its original modal force: Every threat the model name has to rest on code the model actually opened, and every threat the model fail to name is invisible to every later stage — this stage sets the ceiling on what the whole scan can find.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model have no sub-agents.
  The request retains this source rule, criterion or rationale, with its original modal force: The todo list IS the model's coverage guarantee, and it is the only thing standing between a directory and being silently unread.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every plan covers at least:
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Partition the FILE INVENTORY into directory groups and write one todo per group, so the plan itself accounts for every file in scope.
  The request retains this source rule, criterion or rationale, with its original modal force: A group with no todo is a set of files no later stage will open.
  The request retains this source rule, criterion or rationale, with its original modal force: The inventory is already in this prompt — partition it, do not go and re-enumerate it with `ls` or Glob.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Work the groups in order of how likely they are to hide a threat nothing else will find: templates and views first, then container/CI/IaC, then models and persistence, then utils.
  The request retains this source rule, criterion or rationale, with its original modal force: Request handlers last — they are the best-covered code in any repo and the rest of the pipeline still sees them.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Open the entry points and confirm which are reachable unauthenticated.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Establish module structure and blast radius from the graph rather than from directory names: `GraphContext` for a symbol's callers, callees and imports in one call, `GraphImpact` for whether anything reaches it, `GraphCommunityOf` for a file's module, `GraphSinksInCommunity` for the sinks already known in it.
  The request retains this source rule, criterion or rationale, with its original modal force: One `GraphContext` call answers what several Reads would.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 5.; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to obtain and examine the container, CI and infrastructure files — `Dockerfile`, `docker-compose*.yml`, IaC, `.github/**`.
  The request retains this source rule, criterion or rationale, with its original modal force: Secrets and deployment posture live there and nowhere else.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 6.; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to obtain and examine the templates and client-side files.
  The request retains this source rule, criterion or rationale, with its original modal force: An unescaped interpolation of stored data is a finding, and nothing else in the pipeline will look for it.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 7.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Give every threat a `surface_files` list of real paths taken from what the model actually read.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
// Source list marker 8.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Reconcile: subtract every path the model named from the inventory and account for what is left, either with a new threat or a one-line reason in `open_questions`.
  The requested model reply must contain "unreviewed: <n> file(s) — <reason>" when any remain.
}
```

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:20-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Mark each todo in_progress as the model start it and completed only when genuinely done.
  The request retains this source rule, criterion or rationale, with its original modal force: Add todos when what the model read opens something new.
  The request retains this source rule, criterion or rationale, with its original modal force: Only once every todo is completed do the model emit the threat model.
}
```

## PLAN_TOOL_DESCRIPTION — source lines 57–61

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:57-61
Constraints {
  The requested evidence/output includes and update your threat-modelling plan.
  The request retains this source rule, criterion or rationale, with its original modal force: Call this FIRST, before any other tool, then keep it current: mark a todo in_progress when the model start it and completed when the model have genuinely finished it, and add todos as the code opens new questions.
  The request retains this source rule, criterion or rationale, with its original modal force: This is not optional and not only for long tasks.
  The request retains this source rule, criterion or rationale, with its original modal force: Statuses are "pending", "in_progress" and "completed".
  The requested model behavior excludes call this tool twice in one turn.
}
```

## __all__ — source lines 65–65

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:65-65
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: PLAN_SYSTEM_PROMPT
}
```

## __all__ — source lines 66–66

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/pipeline/stages/s2_planning.py:66-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: PLAN_TOOL_DESCRIPTION
}
```

