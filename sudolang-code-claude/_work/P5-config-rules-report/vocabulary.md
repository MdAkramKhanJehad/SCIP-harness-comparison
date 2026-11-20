# Vocabulary: P5-config-rules-report

### Options blocks named after profile sections (`Options models`, `Options transport`, `Options caching`, `Options reasoning`, `Options entries`, `Options weights`, `Options keywords`, `Options validators`, `Options shapes`, `Options sniff_patterns`)
- Definition: grouping labels for data rendered as SudoLang `Options`; `transport`, `caching`, `reasoning` group top-level profile keys (sdk/openai/cli; cache_*; think_in_prompt); the others group module constants.
- Why needed: data files and constant tables have no function or interface name in the source.
- Kind: general harness concept
- Original source term or wording: YAML top-level keys / module-level constants
- Source references: vvaharness/config/profiles/default.yaml:71-108,424-429; vvaharness/report/cvss.py:20-54; vvaharness/report/appcontext.py:36-78; vvaharness/report/redact.py:28-112; vvaharness/lang/detect.py:157-206; vvaharness/rules/generic.kb.yaml:20
- Used in: vvah/vvaharness/config/profiles/*.sudo.md, vvah/vvaharness/report/{cvss,appcontext,redact}.sudo, vvah/vvaharness/lang/detect.sudo, vvah/vvaharness/rules/generic.kb.sudo.md

### absent (profile value)
- Definition: in a difference-only profile rendering, the key exists in default.yaml but not in this profile.
- Why needed: the difference convention for the four non-default profiles.
- Kind: general harness concept
- Original source term or wording: key missing from YAML
- Source references: vvaharness/config/profiles/sdk.yaml, taint.yaml
- Used in: vvah/vvaharness/config/profiles/{sdk,taint}.sudo.md

### Slot
- Definition: the merged per-CWE record inside CweKB._by_cwe (cwe, title, origin, five lists); aliases share the same Slot object.
- Why needed: the source uses an anonymous dict named `slot`.
- Kind: tool-specific identifier
- Original source term or wording: `slot`
- Source references: vvaharness/rules/__init__.py:139-155
- Used in: vvah/vvaharness/rules/__init__.sudo

### mask (helper inside _redact_impl)
- Definition: count a label, optionally remember the value, return a placeholder sentinel.
- Why needed: shorter name for the nested `_mask` closure.
- Kind: tool-specific identifier
- Original source term or wording: `_mask`
- Source references: vvaharness/report/redact.py:309-320
- Used in: vvah/vvaharness/report/redact.sudo
