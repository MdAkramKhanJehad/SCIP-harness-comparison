# ToolCallBudget — per-session tool-family allowance

Executable. Refusal and withdrawal text are model requests layered on host checks.

```sudo
// Source: vvaharness/backends/harness/deepagents/tool_budget.py:37-89
fn _calls_counter_name(counter, tool) {
  if (counter=="tool_call_budget_exhausted") { yield "tool_calls_" + tool }
  else { yield counter with trailing "_budget_exhausted" removed + "_calls_" + tool }
}
Warnings map stage counters to their graph/CWE budget config paths when known,
  otherwise a generic label; warn once per counter. Refusals are error ToolMessages
  with original tool name/id. Withdrawal is a HumanMessage. Exact text is in assets.

// Source: vvaharness/backends/harness/deepagents/tool_budget.py:92-142
interface ToolCallBudget {
  Initialization stores tool_names, limit, counter default "tool_call_budget_exhausted".
  _spent=0; _lock=threading.Lock(); _withdrawal_announced=false.
  name = "ToolCallBudget[" + counter + "]".
}
fn _claim() {
  Under _lock:
    if (_spent>=_limit) { yield false } else { _spent+=1; yield true }
}
fn _gate(tool_call) {
  if (tool_call.name not in _tool_names) { yield None and end this call }
  if (_claim()) { bump usage counter for this tool; yield None and end this call }
  Bump exhaustion counter; warn once; yield synthetic error ToolMessage containing _BUDGET_MESSAGE.
}
fn exhausted_tools() {
  Under _lock, yield _tool_names when _spent>=_limit, else empty set.
}
fn refusal_for(tool_name) {
  Run _gate with synthetic id="out-of-loop" and empty args.
  Yield None if allowed, otherwise refusal.content as string.
}

// Source: vvaharness/backends/harness/deepagents/tool_budget.py:144-189
fn wrap_tool_call(request, handler) {
  Yield _gate(request.tool_call) or handler(request), using short circuit.
  Async counterpart checks gate, then awaits handler only when refusal is None.
  A claimed allowance is spent before handler success/failure; no refund is shown.
}
fn _withdraw(request) {
  Keep tools whose name is not in metered set.
  Append withdrawal HumanMessage only on first withdrawal; set _withdrawal_announced=true.
  Yield request overridden with kept tools and selected messages.
}
fn wrap_model_call(request, handler) {
  if (exhausted_tools()) { request=_withdraw(request) }
  yield handler(request)
  Async counterpart makes same withdrawal then awaits handler.
}
```

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../../../prompt_workflow.sudo.md).

- [vvaharness/backends/harness/deepagents/tool_budget.py](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/tool_budget.py.sudo.md)
