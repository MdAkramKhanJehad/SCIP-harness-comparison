# vvaharness/validation/tools/deep_tools.py — model instruction carriers

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
// Source: vvaharness/validation/tools/deep_tools.py:15-15
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Validation's DeepAgents tool-builder: generic readers + deterministic fact tools.
}
```

## _fact_tools — source lines 38–38

Source context: callable `_fact_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:38-38
Constraints {
  The described operation is advertised for build the deterministic fact tools whose names appear in *allowed*.; this description alone does not request its invocation.
}
```

## build_validation_tools — source lines 98–98

Source context: callable `build_validation_tools`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:98-98
Constraints {
  The described operation is advertised for build validation's tool set: generic readers plus the fact tools in the allow-list.; this description alone does not request its invocation.
}
```

## DiffTouched — source lines 45–45

Source context: callable `DiffTouched`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:45-45
Constraints {
  The described operation advertises this return/result contract: whether *file_path* is in diff.patch and its changed line ranges.
}
```

## ChangedLines — source lines 53–53

Source context: callable `ChangedLines`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:53-53
Constraints {
  The described operation advertises this return/result contract: added line ranges for *file_path* from diff.patch.
}
```

## DiffImpactMap — source lines 61–61

Source context: callable `DiffImpactMap`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:61-61
Constraints {
  The described operation advertises this return/result contract: files changed by diff.patch and whether a trust boundary was touched.
}
```

## PatternScan — source lines 73–77

Source context: callable `PatternScan`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:73-77
Constraints {
  The described operation advertises this return/result contract: bounded, secret-free match metadata and a scan summary.
}
```

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:73-77
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Builtin sets: "secret_exposure", "insecure_value".
  The advertised description supplied with this operation is a model-visible claim: The final item reports counts, limits, and whether results were truncated.
}
```

## TestInventory — source lines 85–85

Source context: callable `TestInventory`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.

```sudo
// Source: vvaharness/validation/tools/deep_tools.py:85-85
Constraints {
  The advertised description supplied with this operation is a model-visible claim: Inventory test files and detect negative/adversarial test markers.
}
```

