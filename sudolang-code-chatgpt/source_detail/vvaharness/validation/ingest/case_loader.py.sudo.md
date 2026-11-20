# vvaharness/validation/ingest/case_loader.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/ingest/case_loader.py.evidence.json`. SHA-256: `e270e994911633cb715ad842b953b9e0f31c17d089ed408ed6aa349a2a4a0c38`.

```sudo
// Source: vvaharness/validation/ingest/case_loader.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from pydantic import ValidationError; preserve alias and import-time effects.
// Source: vvaharness/validation/ingest/case_loader.py:24-32
In source order: Resolve source import from vvaharness.models import CaseState, Disposition, FindingCase; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import FINDING_CASE_FILENAME, REMEDIATION_DIRNAME, VALIDATABLE_STATES; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.ingest.errors import IngestError; preserve alias and import-time effects.
// Source: vvaharness/validation/ingest/case_loader.py:34-40
In source order: Evaluate once ['LoadedCase', 'all_case_ids', 'discover_cases', 'load_case', 'select_cases']; assign in source target order to __all__. Then Evaluate once ', '.join(sorted([*(state.value for state in VALIDATABLE_STATES), source_template_40_5])); assign in source target order to _VALIDATABLE.
// Source: vvaharness/validation/ingest/case_loader.py:44-53
// Source: vvaharness/validation/ingest/case_loader.py:43-43
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/validation/ingest/case_loader.py:44-53
interface LoadedCase {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/validation/ingest/case_loader.py:45-48
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call. Then For case, declare without assigning a value; source annotation FindingCase. Then For path, declare without assigning a value; source annotation Path.
  // Source: vvaharness/validation/ingest/case_loader.py:51-53
  // Source: vvaharness/validation/ingest/case_loader.py:50-50
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/validation/ingest/case_loader.py:51-53
  // Source signature: case_id(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn case_id(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/validation/ingest/case_loader.py:52-52
    In source order: Retain source documentation literal source_literal_52_8; it is not a model call.
    // Source: vvaharness/validation/ingest/case_loader.py:53-53
    End this invocation with self.case.case_id.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/validation/ingest/case_loader.py:56-71
// Source signature: discover_cases(repo: Path) -> list[Path]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn discover_cases(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:57-65
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call. Then Evaluate once artifact_dir(repo, REMEDIATION_DIRNAME); assign in source target order to rem_dir.
  // Source: vvaharness/validation/ingest/case_loader.py:66-67
  if (the source predicate not rem_dir.is_dir() is truthy) {
    // Source: vvaharness/validation/ingest/case_loader.py:67-67
    End this invocation with [].
  }
  // Source: vvaharness/validation/ingest/case_loader.py:68-71
  End this invocation with sorted((path for path in rem_dir.glob(source_template_69_38) if not path.is_symlink() and (not path.parent.is_symlink()))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:74-76
// Source signature: load_case(path: Path) -> LoadedCase
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_case(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:75-75
  In source order: Retain source documentation literal source_literal_75_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:76-76
  End this invocation with LoadedCase(case=FindingCase.read(path), path=path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:79-88
// Source signature: _load_case_safe(path: Path) -> LoadedCase | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _load_case_safe(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:80-80
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:81-88
  Perform the following protected operations {
    // Source: vvaharness/validation/ingest/case_loader.py:82-82
    End this invocation with load_case(path).
  }
  // Source: vvaharness/validation/ingest/case_loader.py:83-88
  On the first matching source exception (OSError, ValueError, ValidationError) as exc, in handler order {
    // Source: vvaharness/validation/ingest/case_loader.py:84-87
    In source order: Evaluate console.write(source_template_85_12); retain side effects and discard the expression result.
    // Source: vvaharness/validation/ingest/case_loader.py:88-88
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:91-96
// Source signature: all_case_ids(repo: Path) -> list[str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn all_case_ids(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:93-96
  Perform the following protected operations {
    // Source: vvaharness/validation/ingest/case_loader.py:94-94
    End this invocation with [load_case(path).case_id for path in discover_cases(repo)].
  }
  // Source: vvaharness/validation/ingest/case_loader.py:95-96
  On the first matching source exception (OSError, ValueError, ValidationError), in handler order {
    // Source: vvaharness/validation/ingest/case_loader.py:96-96
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:99-101
// Source signature: _all_cases(repo: Path) -> list[LoadedCase]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _all_cases(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:100-100
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:101-101
  End this invocation with [c for path in discover_cases(repo) if (c := _load_case_safe(path)) is not None].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:104-109
// Source signature: _is_validatable(loaded: LoadedCase) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_validatable(loaded) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:105-106
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call. Then Evaluate once loaded.case; assign in source target order to case.
  // Source: vvaharness/validation/ingest/case_loader.py:107-108
  if (the source predicate case.state in VALIDATABLE_STATES is truthy) {
    // Source: vvaharness/validation/ingest/case_loader.py:108-108
    End this invocation with True.
  }
  // Source: vvaharness/validation/ingest/case_loader.py:109-109
  End this invocation with case.state is CaseState.DECLINED and _declined_for_review(case).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:112-116
// Source signature: _declined_for_review(case: FindingCase) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _declined_for_review(case) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:113-114
  In source order: Retain source documentation literal source_literal_113_4; it is not a model call. Then Evaluate once case.attempts[-1] if case.attempts else None; assign in source target order to latest.
  // Source: vvaharness/validation/ingest/case_loader.py:115-116
  End this invocation with latest is not None and latest.remediation.disposition is Disposition.NOT_APPLICABLE.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:119-121
// Source signature: _cvss_score(loaded: LoadedCase) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cvss_score(loaded) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:120-120
  In source order: Retain source documentation literal source_literal_120_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:121-121
  End this invocation with loaded.case.finding.cvss_score or 0.0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:124-126
// Source signature: _top_by_cvss(cases: list[LoadedCase], limit: int) -> list[LoadedCase]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _top_by_cvss(cases, limit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:125-125
  In source order: Retain source documentation literal source_literal_125_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:126-126
  End this invocation with sorted(cases, key=_cvss_score, reverse=True)[:limit].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:129-134
// Source signature: _log_selection(cases: list[LoadedCase]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _log_selection(cases) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:130-130
  In source order: Retain source documentation literal source_literal_130_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:131-134
  for each loaded in cases {
    // Source: vvaharness/validation/ingest/case_loader.py:132-134
    In source order: Evaluate console.write(source_template_133_12); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:137-146
// Source signature: _capped(cases: list[LoadedCase], max_findings: int | None) -> list[LoadedCase]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _capped(cases, max_findings) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:138-138
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call.
  // Source: vvaharness/validation/ingest/case_loader.py:139-140
  if (the source predicate max_findings is None or max_findings <= 0 or len(cases) <= max_findings is truthy) {
    // Source: vvaharness/validation/ingest/case_loader.py:140-140
    End this invocation with cases.
  }
  // Source: vvaharness/validation/ingest/case_loader.py:141-145
  In source order: Evaluate once len(cases); assign in source target order to total. Then Evaluate console.write(source_template_143_8); retain side effects and discard the expression result.
  // Source: vvaharness/validation/ingest/case_loader.py:146-146
  End this invocation with _top_by_cvss(cases, max_findings).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:149-169
// Source signature: _filter_owned(cases: list[LoadedCase], owned: set[tuple[str, Path]]) -> list[LoadedCase]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _filter_owned(cases, owned) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:152-159
  In source order: Retain source documentation literal source_literal_152_4; it is not a model call. Then Evaluate once []; assign in source target order to kept.
  // Source: vvaharness/validation/ingest/case_loader.py:160-168
  for each loaded in cases {
    // Source: vvaharness/validation/ingest/case_loader.py:161-161
    In source order: Evaluate once (loaded.case_id, loaded.path.parent.resolve()); assign in source target order to key.
    // Source: vvaharness/validation/ingest/case_loader.py:162-168
    if (the source predicate key in owned is truthy) {
      // Source: vvaharness/validation/ingest/case_loader.py:163-163
      In source order: Evaluate kept.append(loaded); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/validation/ingest/case_loader.py:165-168
      In source order: Evaluate console.write(source_template_166_16); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/validation/ingest/case_loader.py:169-169
  End this invocation with kept.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:172-193
// Source signature: select_cases(repo: Path, case_ids: list[str] | None, max_findings: int | None=None, *, owned: set[tuple[str, Path]] | None=None) -> list[LoadedCase]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn select_cases(repo, case_ids, max_findings, owned) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:179-185
  In source order: Retain source documentation literal source_literal_179_4; it is not a model call. Then Evaluate once _all_cases(repo); assign in source target order to all_cases.
  // Source: vvaharness/validation/ingest/case_loader.py:186-187
  if (the source predicate owned is not None is truthy) {
    // Source: vvaharness/validation/ingest/case_loader.py:187-187
    In source order: Evaluate once _filter_owned(all_cases, owned); assign in source target order to all_cases.
  }
  // Source: vvaharness/validation/ingest/case_loader.py:188-191
  if (the source predicate case_ids is not None is truthy) {
    // Source: vvaharness/validation/ingest/case_loader.py:189-189
    In source order: Evaluate once _select_by_id(all_cases, case_ids); assign in source target order to selected.
  }
  else {
    // Source: vvaharness/validation/ingest/case_loader.py:191-191
    In source order: Evaluate once _capped([c for c in all_cases if _is_validatable(c)], max_findings); assign in source target order to selected.
  }
  // Source: vvaharness/validation/ingest/case_loader.py:192-192
  In source order: Evaluate _log_selection(selected); retain side effects and discard the expression result.
  // Source: vvaharness/validation/ingest/case_loader.py:193-193
  End this invocation with selected.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/ingest/case_loader.py:196-212
// Source signature: _select_by_id(all_cases: list[LoadedCase], case_ids: list[str]) -> list[LoadedCase]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _select_by_id(all_cases, case_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/ingest/case_loader.py:197-199
  In source order: Retain source documentation literal source_literal_197_4; it is not a model call. Then Evaluate once {loaded.case_id: loaded for loaded in all_cases}; assign in source target order to by_id. Then Evaluate once [cid for cid in case_ids if cid not in by_id]; assign in source target order to missing.
  // Source: vvaharness/validation/ingest/case_loader.py:200-201
  if (the source predicate missing is truthy) {
    // Source: vvaharness/validation/ingest/case_loader.py:201-201
    Raise IngestError(source_template_201_26).
  }
  // Source: vvaharness/validation/ingest/case_loader.py:202-206
  In source order: Evaluate once [source_template_203_8 for cid in case_ids if not _is_validatable(by_id[cid])]; assign in source target order to not_validatable.
  // Source: vvaharness/validation/ingest/case_loader.py:207-211
  if (the source predicate not_validatable is truthy) {
    // Source: vvaharness/validation/ingest/case_loader.py:208-211
    Raise IngestError(source_template_209_12).
  }
  // Source: vvaharness/validation/ingest/case_loader.py:212-212
  End this invocation with [by_id[cid] for cid in case_ids].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import CaseState, Disposition, FindingCase` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import artifact_dir` at source line 25: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import FINDING_CASE_FILENAME, REMEDIATION_DIRNAME, VALIDATABLE_STATES` at source line 27: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.validation.ingest.errors import IngestError` at source line 32: `source_detail/vvaharness/validation/ingest/errors.py.sudo.md`.
