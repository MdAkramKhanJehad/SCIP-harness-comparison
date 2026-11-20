# ModelCallBudget — final-turn shaping

Executable. Withdrawal restricts model-request tools; the notice asks for an
outcome. This module does not itself guarantee an outcome is returned.

```sudo
// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:29-58
interface ModelCallBudget {
  Initialization accepts limit, outcome_tools, counter="model_call_budget_final_turn",
    raise_when_exhausted=false, stage="".
  _limit=max(1,int(limit)); _outcome=outcome_tools; _counter=counter;
    _calls=0; _lock=threading.Lock(); _raise_when_exhausted=raise_when_exhausted;
    _stage=stage; _final_turn_issued=false.
}
_final_turn_notice requests outcome NOW from available evidence,
  retaining confirmed findings and using inconclusive for open questions.

// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:60-93
name is "ModelCallBudget[" + counter + "]".
fn _claim() { under _lock, increment _calls; yield _calls>=_limit }
fn grant_resume_turn() {
  Under _lock:
    if (!_final_turn_issued) { end this call }
    _final_turn_issued=false; _calls=_limit-1
}
fn _final(request) {
  Keep only tools whose names are in _outcome; bump _counter.
  Override request tools and append _final_turn_notice(_limit) to messages.
}
fn _check_exhausted() {
  if (_raise_when_exhausted && _final_turn_issued) {
    Raise ModelCallBudgetExhaustedError with stage and limit.
  }
}

// Source: vvaharness/backends/harness/deepagents/model_call_budget.py:95-117
fn wrap_model_call(request, handler) {
  _check_exhausted()
  if (_claim()) { _final_turn_issued=true; request=_final(request) }
  yield handler(request)
  Async counterpart preserves sequence, then awaits handler.
}
```

The source comment at line 44 says CapOutputTokens' doubled retry is one
uncounted call. That component is expanded in source_detail/; this comment is retained as
a source claim, not an independently verified end-to-end budget guarantee.

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../../../prompt_workflow.sudo.md).

- [vvaharness/backends/harness/deepagents/model_call_budget.py](../../../../../prompt_representation/vvaharness/backends/harness/deepagents/model_call_budget.py.sudo.md)
