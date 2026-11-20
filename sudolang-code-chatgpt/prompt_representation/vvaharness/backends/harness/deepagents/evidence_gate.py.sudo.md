# vvaharness/backends/harness/deepagents/evidence_gate.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _relent_warning — source lines 44–47

Source context: callable `_relent_warning`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `stage_label(counter); conversion=none; format_spec=none`
- `max_rejections; conversion=none; format_spec=none`
- `reason; conversion=none; format_spec=none`
- `counter; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:44-47
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [dynamic source value: stage_label(counter); conversion=none; format_spec=none]: the evidence gate rejected a verdict [dynamic source value: max_rejections; conversion=none; format_spec=none] time(s) for [dynamic source value: reason; conversion=none; format_spec=none], then relented -- this stage's output shipped without that evidence.
  The request retains this source rule, criterion or rationale, with its original modal force: Count in [dynamic source value: counter; conversion=none; format_spec=none]_relented.
  The request retains this source rule, criterion or rationale, with its original modal force: Raise this stage's rejection limit in the scan config, or review this run's output by hand.
}
```

## reason — source lines 42–42

Source context: callable `_relent_warning`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `', '.join(sorted(required)); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:42-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: missing [dynamic source value: ', '.join(sorted(required)); conversion=none; format_spec=none]
}
```

## reason — source lines 42–42

Source context: callable `_relent_warning`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:42-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: an unfinished plan
}
```

## __init__ — source lines 84–84

Source context: callable `__init__`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:84-84
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: evidence_gate_rejected
}
```

## name — source lines 120–120

Source context: callable `name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `self.__class__.__name__; conversion=none; format_spec=none`
- `self._counter; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:120-120
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: self.__class__.__name__; conversion=none; format_spec=none][[dynamic source value: self._counter; conversion=none; format_spec=none]]
}
```

## listed — source lines 67–67

Source context: callable `_nudge`; enclosing call `'\n'.join`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `c; conversion=none; format_spec=none`

Formatting/composition call retained as source expression evidence:

````python
"\n".join(f"  - {c}" for c in outstanding)
````

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:67-67
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: c; conversion=none; format_spec=none]
}
```

## _nudge — source lines 69–76

Source context: callable `_nudge`; enclosing call `HumanMessage`; keyword `content`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `len(outstanding); conversion=none; format_spec=none`
- `listed; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:69-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HOLD.
  The request retains this source rule, criterion or rationale, with its original modal force: the model tried to report a verdict, but [dynamic source value: len(outstanding); conversion=none; format_spec=none] todo(s) on the model's own plan are not completed: [dynamic source value: listed; conversion=none; format_spec=none]
}
```

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:69-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: That verdict is rejected and has not been recorded.
  The request retains this source rule, criterion or rationale, with its original modal force: Do the outstanding work now — read the code each todo names (to the END of the file; continue any paginated Read), load the skill it calls for, grep for the sibling sites, enumerate the places a missing control belongs.
  The request retains this source rule, criterion or rationale, with its original modal force: Then mark each todo completed with `write_todos` and report.
}
```

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:69-76
Constraints {
  The requested conditional/temporal rule is: If a todo genuinely does not apply, mark it completed and say why in your rationale.
  The requested model behavior excludes resend the same verdict without new evidence.
}
```

## hold_for_verdict — source lines 155–161

Source context: callable `hold_for_verdict`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:155-161
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: to establish reachability from the call graph before submitting this verdict.
  The request retains this source rule, criterion or rationale, with its original modal force: Call one now: GraphImporters(file) for who imports a file, GraphNeighbors(file, function) for its callers and callees, GraphCommunityOf(file) for its module, GraphSinksInCommunity(community) for the other sinks near it.
  The request retains this source rule, criterion or rationale, with its original modal force: These are deterministic and answer in one call what a file sweep answers badly.
  The request retains this source rule, criterion or rationale, with its original modal force: Call one, then resend the model's verdict with that evidence.
}
```

## hold_for_verdict — source lines 147–147

Source context: callable `hold_for_verdict`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `self._counter; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:147-147
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: self._counter; conversion=none; format_spec=none]_relented
}
```

## hold_for_verdict — source lines 153–153

Source context: callable `hold_for_verdict`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:153-153
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Rejected: the model have not called any of
}
```

## _tool_call_items — source lines 167–167

Source context: callable `_tool_call_items`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:167-167
Constraints {
  The model is asked to obtain and examine the code with a tool before you report
}
```

## _premature — source lines 172–172

Source context: callable `_premature`; enclosing call `getattr`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:172-172
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: structured_response
}
```

## _premature — source lines 189–189

Source context: callable `_premature`; enclosing call `COUNTERS.bump`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `self._counter; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:189-189
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: self._counter; conversion=none; format_spec=none]_relented
}
```

## outstanding — source lines 179–183

Source context: callable `_premature`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:179-183
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: .
  The request retains this source rule, criterion or rationale, with its original modal force: Call one now: GraphImporters(file) for who imports a file, GraphNeighbors(file, function) for its callers and callees, GraphCommunityOf(file) for its module, GraphSinksInCommunity(community) for the other sinks near it.
  The request retains this source rule, criterion or rationale, with its original modal force: These are deterministic and answer in one call what a file sweep answers badly
}
```

## outstanding — source lines 177–177

Source context: callable `_premature`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:177-177
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: establish reachability from the call graph — the model have not called any of
}
```

