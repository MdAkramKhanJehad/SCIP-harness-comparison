# P11-ev-exec vocabulary

### targetSlots / perEndpointMax / endpointSlots
- Definition: state of `ConcurrencyLimiter`: the whole-target bounded semaphore, the per-endpoint cap, and the map of per-endpoint semaphores.
- Why needed: readable names for private attributes inside a `State` block.
- Kind: tool-specific identifier
- Original source term or wording: `self._target`, `self._per_endpoint_max`, `self._endpoint`
- Source references: vvaharness/exploit_verification/executor/concurrency.py:26-31
- Used in: vvah/vvaharness/exploit_verification/executor/concurrency.sudo

### now_monotonic()
- Definition: the monotonic clock read (`time.monotonic()`).
- Why needed: distinguishes the monotonic clock from wall-clock `now()` in rate-limit, nonce and self-test timing.
- Kind: general harness concept
- Original source term or wording: `time.monotonic()`
- Source references: vvaharness/exploit_verification/executor/ratelimit.py:33-35, vvaharness/exploit_verification/executor/oob.py:84,152
- Used in: vvah/vvaharness/exploit_verification/executor/ratelimit.sudo, vvah/vvaharness/exploit_verification/executor/oob.sudo

### _default_runner user prompt
- Definition: interface for the user message the finding-map runner builds (located endpoints plus findings, as JSON).
- Why needed: the prompt is an inline expression, not a named constant.
- Kind: tool-specific identifier
- Original source term or wording: `user = ("Located endpoints:\n" + ...)` in `_default_runner`
- Source references: vvaharness/exploit_verification/mapping/finding_map.py:289-294
- Used in: vvah/vvaharness/exploit_verification/mapping/finding_map.sudo

### author's note (template comment block)
- Definition: the YAML file's leading comment, reproduced as a `/* */` block; it is documentation, never sent to a model or read by code.
- Why needed: the templates' comments state each payload set's intent and oracle tell; kept so a reader sees the author's stated purpose.
- Kind: general harness concept
- Original source term or wording: leading `#` comments in each `payloads/templates/*.yaml`
- Source references: vvaharness/exploit_verification/payloads/templates/*.yaml (comment lines after the license header)
- Used in: vvah/vvaharness/exploit_verification/payloads/templates/*.sudo.md (15 files)
