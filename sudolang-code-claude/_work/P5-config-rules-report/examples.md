# Examples: P5-config-rules-report

## 1. refusal_retries gate
Source `vvaharness/config/__init__.py:903-915`:
```
_REFUSAL_RETRIES_MAX: Final = 1
def _check_refusal_retries(value: object, p: Path) -> None:
    if value is None or (isinstance(value, int) and not isinstance(value, bool)
                         and 0 <= value <= _REFUSAL_RETRIES_MAX):
        return
    raise ConfigPolicyError(...)
```
SudoLang (`vvah/vvaharness/config/__init__.sudo`):
```
_REFUSAL_RETRIES_MAX = 1
fn _check_refusal_retries(value, p):executor=code {
  require value == null || (value is an int && value is not a bool && 0 <= value <= _REFUSAL_RETRIES_MAX)
    => throw ConfigPolicyError("config $p: refusal_retries must be an integer from 0 to 1 ...")
}
```

## 2. same_weakness equivalence
Source `vvaharness/rules/cwe.py:69-84` (generic parent rule):
```
    a_generic = a in _GENERIC_PARENT_CWES
    b_generic = b in _GENERIC_PARENT_CWES
    if a_generic != b_generic:
        return True
    if a_generic and b_generic:
        return False
    return weakness_key(a) == weakness_key(b)
```
SudoLang (`vvah/vvaharness/rules/cwe.sudo`):
```
  if (a_generic xor b_generic) return true
  if (a_generic && b_generic) return false
  return weakness_key(a) == weakness_key(b)
```

## 3. Model-facing knowledge-base text (prompt_block labels)
Source `vvaharness/rules/__init__.py:193-204`:
```
            ("sanitizers",
             "SANITIZERS — if ANY of these sits on the path, REFUTE:"),
            ...
            ("fp_checks",
             "FP CHECKS — if ANY is true, REFUTE:"),
```
SudoLang (`vvah/vvaharness/rules/__init__.sudo`): the same four label strings quoted exactly in `CweKB.prompt_block`, with `limit = 20` and the "…(+N more)" overflow line.
