# P1-pipeline vocabulary

Harvest is complete for the 22 files verified or written in pass 2. The 22 `partial` files were not harvested line by line.

### resolve_model
- Definition: resolves a configured model role to its backend route; `.via` is the route name.
- Why needed: avoids a clash with the generic word "resolve" in pseudocode.
- Kind: tool-specific identifier
- Original source term or wording: `resolve` (imported from `vvaharness.backends.llm.registry`)
- Source references: vvaharness/pipeline/stages/s6/session.py:99, 179, 291; vvaharness/pipeline/stages/s4/session.py (several)
- Used in: vvah/vvaharness/pipeline/stages/s6/session.sudo, s6_verify.sudo, s4/session.sudo, s2/session.sudo, s2/__init__.sudo, s1_autoexclude.sudo

### floors (callModel limits key)
- Definition: the minimum-response floors (characters, tokens) that the code sets around one model call with `stage_floors`.
- Why needed: `callModel` has no slot for the response-quality floor wrapper.
- Kind: general harness concept
- Original source term or wording: `with stage_floors(tag, min_chars=..., min_tokens=...)`
- Source references: vvaharness/pipeline/stages/s6/session.py:260, 339-340
- Used in: vvah/vvaharness/pipeline/stages/s6/session.sudo

### then "..." followed by $x (prompt layout phrase)
- Definition: inside a prompt's `Constraints`, means a literal separator line followed by a slot appended after the instructions.
- Why needed: shows how the prompt is built, not something the model is asked to do.
- Kind: general harness concept
- Original source term or wording: `"\n\n--- ORIGINAL REPLY ---\n{raw}"`
- Source references: vvaharness/pipeline/stages/s6/prompts.py:383
- Used in: vvah/vvaharness/pipeline/stages/s6/prompts.sudo, s4/session.sudo

### _ROLE, _VERDICT_CLAUSE, ... (s6 prompt fragment interfaces)
- Definition: prompt interfaces named after the source constants. They are source identifiers and are listed here only so readers can find them.
- Why needed: not a new name.
- Kind: tool-specific identifier
- Original source term or wording: the same names
- Source references: vvaharness/pipeline/stages/s6/prompts.py:23-229
- Used in: vvah/vvaharness/pipeline/stages/s6/prompts.sudo

### S8_USER_PROMPT
- Definition: interface for the Stage 8 user prompt returned by `build_prompt` (repository, design controls, known CVEs, fact blocks, finding blocks, evidence rules).
- Why needed: the source builds it as an f-string with no constant name.
- Kind: tool-specific identifier
- Original source term or wording: return value of `build_prompt`
- Source references: vvaharness/pipeline/stages/s8/prompts.py:223-264
- Used in: vvah/vvaharness/pipeline/stages/s8/prompts.sudo, vvah/vvaharness/pipeline/stages/s8/session.sudo

### Constants, VetoSets
- Definition: grouping interfaces for the module constants and the veto sets of auto-exclude.
- Why needed: groups module-level constants into one block each.
- Kind: general harness concept
- Original source term or wording: module-level constants
- Source references: vvaharness/pipeline/stages/s1_autoexclude.py:97-122, 303-335
- Used in: vvah/vvaharness/pipeline/stages/s1_autoexclude.sudo

### S1_AUTOEXCLUDE_USER_PROMPT
- Definition: interface for the inline auto-exclude user prompt.
- Why needed: the source builds it as an unnamed f-string.
- Kind: tool-specific identifier
- Original source term or wording: inline f-string
- Source references: vvaharness/pipeline/stages/s1_autoexclude.py:603-636
- Used in: vvah/vvaharness/pipeline/stages/s1_autoexclude.sudo

### constraint StageFloors
- Definition: constraint naming the `stage_floors` context manager scope.
- Why needed: renders a context manager whose exit matters.
- Kind: tool-specific identifier
- Original source term or wording: `stage_floors`
- Source references: vvaharness/pipeline/stages/s1_autoexclude.py:658-663
- Used in: vvah/vvaharness/pipeline/stages/s1_autoexclude.sudo

### MINIMUM_BASELINE_BLOCK
- Definition: interface for the prompt block built in `_baseline_block`.
- Why needed: the source builds it as an unnamed f-string.
- Kind: tool-specific identifier
- Original source term or wording: return value of `_baseline_block`
- Source references: vvaharness/pipeline/stages/s2/prompts.py:221-239
- Used in: vvah/vvaharness/pipeline/stages/s2/prompts.sudo
