# vvaharness/backends/harness/deepagents/tool_budget.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## <module> — source lines 15–15

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Middleware that caps how many times a session may call a named set of tools.
}
```

## _BUDGET_MESSAGE — source lines 38–40

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:38-40
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model's tool-call budget for this session is exhausted.
  The requested model behavior excludes call any further tool in the metered set; finish from the evidence you already have.
  The request retains this source rule, criterion or rationale, with its original modal force: Calling one again will not run and only spends a turn.
}
```

## _DEFAULT_COUNTER — source lines 43–43

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:43-43
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tool_call_budget_exhausted
}
```

## _KNOB_NAMES — source lines 48–48

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s2_graph_tool_budget_exhausted
}
```

## _KNOB_NAMES — source lines 49–49

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:49-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_graph_tool_budget_exhausted
}
```

## _KNOB_NAMES — source lines 50–50

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:50-50
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s4_cwe_tool_budget_exhausted
}
```

## _KNOB_NAMES — source lines 51–51

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:51-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: s6_graph_tool_budget_exhausted
}
```

## _KNOB_NAMES — source lines 48–48

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step2.graph_tool_budget
}
```

## _KNOB_NAMES — source lines 49–49

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:49-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.graph_tool_budget
}
```

## _KNOB_NAMES — source lines 50–50

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:50-50
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step4.cwe_tool_budget
}
```

## _KNOB_NAMES — source lines 51–51

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:51-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: step6_verify.graph_tool_budget
}
```

## _calls_counter_name — source lines 58–58

Source context: callable `_calls_counter_name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:58-58
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The usage-tally key for *tool*, derived from the exhaustion counter's own name.
}
```

## _calls_counter_name — source lines 61–61

Source context: callable `_calls_counter_name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `counter.removesuffix('_budget_exhausted'); conversion=none; format_spec=none`
- `tool; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:61-61
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: counter.removesuffix('_budget_exhausted'); conversion=none; format_spec=none]_calls_[dynamic source value: tool; conversion=none; format_spec=none]
}
```

## _exhaustion_warning — source lines 65–65

Source context: callable `_exhaustion_warning`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:65-65
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The once-per-(stage, family)-per-run WARN line for the first refusal on *counter*.
}
```

## _exhaustion_warning — source lines 69–73

Source context: callable `_exhaustion_warning`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `stage_label(counter); conversion=none; format_spec=none`
- `knob; conversion=none; format_spec=none`
- `limit; conversion=none; format_spec=none`
- `names; conversion=none; format_spec=none`
- `counter; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:69-73
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: WARN [dynamic source value: stage_label(counter); conversion=none; format_spec=none]: tool-call budget ([dynamic source value: knob; conversion=none; format_spec=none]=[dynamic source value: limit; conversion=none; format_spec=none] per session) exhausted in at least one session for [dynamic source value: names; conversion=none; format_spec=none] -- further calls there are refused now, and the tool family is withdrawn once the model calls again; it finishes from the evidence it already has.
  The request retains this source rule, criterion or rationale, with its original modal force: Count in the run manifest under [dynamic source value: counter; conversion=none; format_spec=none].
  The request retains this source rule, criterion or rationale, with its original modal force: Raise the knob in the scan config if this recurs.
}
```

## _refuse — source lines 78–78

Source context: callable `_refuse`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:78-78
Constraints {
  The advertised description supplied with this operation is a model-visible claim: A synthetic error ToolMessage explaining why a call was not executed.
}
```

## _withdrawn_notice — source lines 84–84

Source context: callable `_withdrawn_notice`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:84-84
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The one-time turn appended when a metered tool is removed from availability.
}
```

## <module> — source lines 93–93

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:93-93
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Refuse any metered tool call once one session has spent its total allowance.
}
```

## _calls_counter_name — source lines 60–60

Source context: callable `_calls_counter_name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `tool; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:60-60
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tool_calls_[dynamic source value: tool; conversion=none; format_spec=none]
}
```

## knob — source lines 66–66

Source context: callable `_exhaustion_warning`; enclosing call `_KNOB_NAMES.get`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:66-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: its scan-config budget knob
}
```

## __init__ — source lines 97–97

Source context: callable `__init__`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:97-97
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: tool_call_budget_exhausted
}
```

## __init__ — source lines 98–98

Source context: callable `__init__`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:98-98
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Allow *limit* calls across *tool_names* in this session, then refuse the rest.
}
```

## name — source lines 109–109

Source context: callable `name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:109-109
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Per-instance name; langchain asserts middleware names are unique per agent.
}
```

## name — source lines 111–111

Source context: callable `name`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `self.__class__.__name__; conversion=none; format_spec=none`
- `self._counter; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:111-111
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: self.__class__.__name__; conversion=none; format_spec=none][[dynamic source value: self._counter; conversion=none; format_spec=none]]
}
```

## _claim — source lines 114–114

Source context: callable `_claim`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:114-114
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Take one unit of budget, returning whether there was any left.
}
```

## _gate — source lines 122–122

Source context: callable `_gate`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:122-122
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The refusal to return when the budget is gone, else None to proceed.
}
```

## exhausted_tools — source lines 134–134

Source context: callable `exhausted_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:134-134
Constraints {
  The advertised description supplied with this operation is a model-visible claim: The metered tool name(s) with no allowance left, or ``frozenset()`` while any remains.
}
```

## refusal_for — source lines 139–139

Source context: callable `refusal_for`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:139-139
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Claim one unit for *tool_name*, returning the refusal text when none is left.
}
```

## wrap_tool_call — source lines 149–149

Source context: callable `wrap_tool_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:149-149
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Execute while budget remains; otherwise refuse without running the tool.
}
```

## awrap_tool_call — source lines 157–157

Source context: callable `awrap_tool_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:157-157
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Async counterpart of :meth:`wrap_tool_call`.
}
```

## _withdraw — source lines 162–162

Source context: callable `_withdraw`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:162-162
Constraints {
  The advertised description supplied with this operation is a model-visible claim: *request* with this budget's exhausted tool(s) removed from the tool list.
}
```

## wrap_model_call — source lines 176–176

Source context: callable `wrap_model_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:176-176
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Withdraw this budget's tool(s) from the request once its pool is spent.
}
```

## awrap_model_call — source lines 186–186

Source context: callable `awrap_model_call`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:186-186
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Async counterpart of :meth:`wrap_model_call`.
}
```

## _withdrawn_notice — source lines 86–88

Source context: callable `_withdrawn_notice`; enclosing call `HumanMessage`; keyword `content`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `', '.join(sorted(tool_names)); conversion=none; format_spec=none`

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:86-88
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: the model's budget for [dynamic source value: ', '.join(sorted(tool_names)); conversion=none; format_spec=none] is exhausted; it/they have been withdrawn from the model's available tools for the rest of this session -- finish from the evidence the model already have rather than asking for it/them again.
}
```

## _calls_counter_name — source lines 61–61

Source context: callable `_calls_counter_name`; enclosing call `counter.removesuffix`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:61-61
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: _budget_exhausted
}
```

## refusal — source lines 141–141

Source context: callable `refusal_for`; enclosing call `self._gate`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:141-141
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: out-of-loop
}
```

