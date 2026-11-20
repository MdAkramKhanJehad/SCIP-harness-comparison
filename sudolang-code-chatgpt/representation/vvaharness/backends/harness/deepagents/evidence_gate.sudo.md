# EvidenceGate — middleware behavior

Executable middleware, with model-facing hold messages as requests. Its adapters
for other routes are expanded in source_detail/; the external middleware engine
remains an explicit dependency boundary.

```sudo
// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:35-77
fn _todos(state) {
  Read state.get("todos") if get exists, else state.todos default None.
  AttributeError/TypeError yields []; otherwise retain dictionary entries only.
}
fn _outstanding(todos) {
  Yield content as string, default "?", for every todo whose status != "completed".
}
fn _nudge(outstanding) {
  Create HumanMessage listing outstanding todos and requesting reads to EOF,
    skill/sibling/absence work, write_todos updates and then a verdict.
  Exact message is preserved in assets. Its directions do not prove work occurred.
}

// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:80-140
interface EvidenceGate {
  Initialization accepts max_rejections=3, counter="evidence_gate_rejected",
    required_tools=empty set, require_tool_call=false, ignored_tools=empty set.
  Store _max,_counter,_required,_require_tool_call,_ignored;
    _called=empty set; _rejected=0; _lock=threading.Lock().
  name is "EvidenceGate[" + counter + "]"; required_tools exposes _required.
}
fn wrap_tool_call(request, handler) {
  Add request.tool_call.name to _called BEFORE invoking handler(request), without explicit lock here.
  Yield handler result. Async counterpart adds name then awaits handler.
}
fn note_call(name) { under _lock, add name to _called }
fn _claim() {
  Under _lock:
    if (_rejected>=_max) { yield false }
    else { _rejected+=1; yield true }
}

// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:142-194
fn hold_for_verdict() {
  if (!_required || _required intersects _called) { yield None and end this call }
  if (!_claim()) { bump counter_relented; warn once; yield None and end this call }
  Bump rejection counter; yield rejection text asking to call ONE required graph tool then resubmit.
  This out-of-loop form does not inspect todos or require_tool_call.
}
fn _tool_call_items() {
  if (_require_tool_call && no called tool remains after removing _ignored) {
    yield ["read the code with a tool before you report"]
  } else { yield [] }
}
fn _premature(request, response) {
  if (response.structured_response is None) { yield [] and end this call }
  outstanding=_outstanding(_todos(request.state))
  if (_required && no intersection with _called) { append missing-graph-call item }
  Append _tool_call_items().
  if (!outstanding) { yield [] and end this call }
  if (!_claim()) { bump counter_relented; warn once; yield [] and end this call }
  Bump rejection counter; yield outstanding.
  Reaching the rejection limit relents; this is not an unconditional evidence requirement.
}

// Source: vvaharness/backends/harness/deepagents/evidence_gate.py:196-223
fn _retry_request(request, outstanding) {
  Yield request.override(messages=original request.messages plus _nudge(outstanding)).
  Drop rejected response rather than inserting an unmatched tool_use into history.
}
fn wrap_model_call(request, handler) {
  response=handler(request)
  outstanding=_premature(request,response)
  while (outstanding is nonempty) {
    request=_retry_request(request,outstanding)
    response=handler(request)
    outstanding=_premature(request,response)
  }
  yield response
  Async counterpart preserves the same sequence, awaiting each handler call.
}
```

Source warning construction at lines 40–48 identifies the rejection count and
either required tools or an unfinished plan; it does not alter the gate result.

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../../../prompt_workflow.sudo.md).

- [vvaharness/backends/harness/deepagents/evidence_gate.py](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/evidence_gate.py.sudo.md)
