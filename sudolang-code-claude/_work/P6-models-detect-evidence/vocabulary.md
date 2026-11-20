# Vocabulary, slice models (top level)

### FindingCase.with_attempt / FindingCase.with_verdict / FindingCase.read / FindingCase.write (dotted method form)
- Definition: a method of a source class written as `Interface.method` because SudoLang has no class construct.
- Why needed: CONVENTIONS forbid `class`; the dotted name keeps the source method name searchable.
- Kind: general harness concept
- Original source term or wording: methods `with_attempt`, `with_verdict`, `read`, `write` of class `FindingCase`; `missing_from` of `ScoringPolicy`
- Source references: vvaharness/models/case.py:78-110, vvaharness/models/context.py:53-59
- Used in: vvah/vvaharness/models/case.sudo, vvah/vvaharness/models/context.sudo

### coercion (comment label)
- Definition: comment label for a pydantic `field_validator`/`model_validator(mode="before")` or an enumeration `_missing_` hook that rewrites an input value before validation instead of rejecting it.
- Why needed: these hooks change what is stored (null to empty string, gate name normalised, unknown label to a fail-closed member) but are not checks, so they are not `require`.
- Kind: general harness concept
- Original source term or wording: `_none_to_empty`, `_canonical_name`, `_drop_derived`, `_missing_`
- Source references: vvaharness/models/gates.py:36-40, vvaharness/models/gates.py:55-59, vvaharness/models/case.py:70-76, vvaharness/models/vocab.py:56-60, 92-101, 142-148, 160-166
- Used in: vvah/vvaharness/models/gates.sudo, vvah/vvaharness/models/case.sudo, vvah/vvaharness/models/vocab.sudo

### first N of X
- Definition: the first N items (or characters) of a list or string; used instead of `X[0..N]` because SudoLang ranges are inclusive.
- Why needed: Python slices `x[:n]` are exclusive; an inclusive range would misstate caps by one.
- Kind: general harness concept
- Original source term or wording: `x[:n]`
- Source references: vvaharness/models/scan/context.py:63-107, vvaharness/detect/matcher.py:73, vvaharness/models/scan/threat.py:338,346
- Used in: vvah/vvaharness/models/scan/context.sudo, threat.sudo, _sections_chain.sudo, vvah/vvaharness/detect/matcher.sudo

### RenderBlocks / ExclusionDefaults
- Definition: grouping interfaces that collect a module's renderer functions (evidence/render.py) or its default exclusion constants (scope/walk.py).
- Why needed: groups many one-line source definitions under one pointer.
- Kind: general harness concept
- Original source term or wording: none (module-level definitions)
- Source references: vvaharness/evidence/render.py:21-91, vvaharness/scope/walk.py:33-68
- Used in: vvah/vvaharness/evidence/render.sudo, vvah/vvaharness/scope/walk.sudo

### description (in tool interfaces)
- Definition: the model-facing tool description, quoted from the tool function's docstring.
- Why needed: tools are rendered as interfaces; the docstring is what the model sees.
- Kind: general harness concept
- Original source term or wording: `@tool` docstring
- Source references: vvaharness/codegraph/tools.py:149-263, vvaharness/plugins/semgrep/tools.py:75-108
- Used in: vvah/vvaharness/codegraph/tools.sudo, vvah/vvaharness/plugins/semgrep/tools.sudo
