# Examples: P2-backends-harness

## 1. Repeat guard (threshold 20, VVAH-E009)

Source `vvaharness/backends/harness/repeat_guard.py:30-31, 55-66`:
```
REPEAT_CALL_LIMIT: Final = 20
...
        async for msg in source:
            if isinstance(msg, HarnessToolUse):
                signature = _signature(msg)
                streak = streak + 1 if signature == last else 1
                last = signature
                if streak >= REPEAT_CALL_LIMIT:
                    raise RepeatedToolCallError(...)
            yield msg
```
SudoLang `vvah/vvaharness/backends/harness/repeat_guard.sudo`:
```
REPEAT_CALL_LIMIT = 20
for each msg in source {
  if (msg is HarnessToolUse) {
    signature = _signature(msg)
    streak = if (signature == last) streak + 1 else 1
    last = signature
    require streak < REPEAT_CALL_LIMIT
      => throw RepeatedToolCallError("${signature.agent} called ${msg.name} with identical input $streak times in a row", stage, route, tool_name=msg.name, repeats=streak)
  }
  yield msg
}
```

## 2. Model-call budget (last call forced to the outcome)

Source `vvaharness/backends/harness/deepagents/model_call_budget.py:65-69, 95-105`:
```
    def _claim(self) -> bool:
        with self._lock:
            self._calls += 1
            return self._calls >= self._limit
...
    def wrap_model_call(self, request, handler):
        self._check_exhausted()
        if self._claim():
            self._final_turn_issued = True
            request = self._final(request)
        return handler(request)
```
SudoLang `vvah/vvaharness/backends/harness/deepagents/model_call_budget.sudo`:
```
fn _claim():executor=code { with _lock { _calls += 1; return _calls >= _limit } }
fn wrap_model_call(request, handler):executor=code {
  _check_exhausted()
  if (_claim()) { _final_turn_issued = true; request = _final(request) }
  return handler(request)
}
```

## 3. One doubled truncation retry

Source `vvaharness/backends/harness/deepagents/options/graph_builder.py:213-220`:
```
    def _truncation_retry_at(self, discarded: ModelCallResult) -> int | None:
        if not reply_truncated(_result_messages(discarded)):
            return None
        retry_at = self._retry_at()
        if retry_at is not None:
            self._log_retry(retry_at, self._bank(discarded))
        return retry_at
```
SudoLang `vvah/vvaharness/backends/harness/deepagents/options/graph_builder.sudo`:
```
fn _truncation_retry_at(discarded):executor=code {
  if (!translate.reply_truncated(messages of discarded)) return null
  retry_at = truncation_retry_max(_max_tokens, cap=_cap_ceiling)   // min(_max_tokens * 2, cap); null when already at cap
  if (retry_at != null) _log_retry(retry_at, _bank(discarded))
  return retry_at
}
```
