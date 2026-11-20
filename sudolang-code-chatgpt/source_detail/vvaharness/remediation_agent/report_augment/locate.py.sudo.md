# vvaharness/remediation_agent/report_augment/locate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/report_augment/locate.py.evidence.json`. SHA-256: `1f63daba581217a02be394b9063c253550a586ecf4fa987d9c3c0e3551ddd5b5`.

```sudo
// Source: vvaharness/remediation_agent/report_augment/locate.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import artifact_dir; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/report_augment/locate.py:22-31
In source order: Resolve source import from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME, SCAN_DIR_NAME; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once '*_report.sarif'; assign in source target order to SCAN_REPORT_GLOB.
// Source: vvaharness/remediation_agent/report_augment/locate.py:34-61
// Source signature: _locate_scan_report(repo: Path, report_md: Path | None=None) -> tuple[Path, Path] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _locate_scan_report(repo, report_md) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/locate.py:36-36
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call.
  // Source: vvaharness/remediation_agent/report_augment/locate.py:38-47
  if (the source predicate report_md is not None is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/locate.py:39-39
    In source order: Evaluate once Path(report_md); assign in source target order to md.
    // Source: vvaharness/remediation_agent/report_augment/locate.py:40-42
    if (the source predicate not md.exists() is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/locate.py:41-41
      In source order: Evaluate log.warning('explicit scan report %s not found — skipping augmentation', md); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/report_augment/locate.py:42-42
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/report_augment/locate.py:43-43
    In source order: Evaluate once md.with_suffix('.sarif'); assign in source target order to sarif.
    // Source: vvaharness/remediation_agent/report_augment/locate.py:44-46
    if (the source predicate not sarif.exists() is truthy) {
      // Source: vvaharness/remediation_agent/report_augment/locate.py:45-45
      In source order: Evaluate log.warning('sibling SARIF for %s not found — skipping augmentation', md); retain side effects and discard the expression result.
      // Source: vvaharness/remediation_agent/report_augment/locate.py:46-46
      End this invocation with None.
    }
    // Source: vvaharness/remediation_agent/report_augment/locate.py:47-47
    End this invocation with (sarif, md).
  }
  // Source: vvaharness/remediation_agent/report_augment/locate.py:49-49
  In source order: Evaluate once sorted((repo / SCAN_DIR_NAME).glob(SCAN_REPORT_GLOB)); assign in source target order to sarifs.
  // Source: vvaharness/remediation_agent/report_augment/locate.py:50-51
  if (the source predicate not sarifs is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/locate.py:51-51
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/locate.py:52-58
  if (the source predicate len(sarifs) > 1 is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/locate.py:53-57
    In source order: Evaluate log.warning(source_literal_54_12, len(sarifs), repo, SCAN_DIR_NAME); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/report_augment/locate.py:58-58
    End this invocation with None.
  }
  // Source: vvaharness/remediation_agent/report_augment/locate.py:59-60
  In source order: Evaluate once sarifs[0]; assign in source target order to sarif. Then Evaluate once sarif.with_suffix('.md'); assign in source target order to md.
  // Source: vvaharness/remediation_agent/report_augment/locate.py:61-61
  End this invocation with (sarif, md) if md.exists() else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/report_augment/locate.py:64-76
// Source signature: _ensure_combined(repo: Path, sarif_src: Path, md_src: Path) -> tuple[Path, Path]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ensure_combined(repo, sarif_src, md_src) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/report_augment/locate.py:65-71
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then Evaluate once artifact_dir(repo, REMEDIATION_DIR_NAME); assign in source target order to dst_dir. Then Evaluate dst_dir.mkdir(exist_ok=True); retain side effects and discard the expression result. Then Evaluate once dst_dir / sarif_src.name; assign in source target order to sarif_dst. Then Evaluate once dst_dir / md_src.name; assign in source target order to md_dst.
  // Source: vvaharness/remediation_agent/report_augment/locate.py:72-73
  if (the source predicate not sarif_dst.exists() is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/locate.py:73-73
    In source order: Evaluate shutil.copy2(sarif_src, sarif_dst); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/locate.py:74-75
  if (the source predicate not md_dst.exists() is truthy) {
    // Source: vvaharness/remediation_agent/report_augment/locate.py:75-75
    In source order: Evaluate shutil.copy2(md_src, md_dst); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/report_augment/locate.py:76-76
  End this invocation with (sarif_dst, md_dst).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.orchestrator.artifacts import artifact_dir` at source line 21: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.remediation_agent.report_parser import REMEDIATION_DIR_NAME, SCAN_DIR_NAME` at source line 22: `source_detail/vvaharness/remediation_agent/report_parser/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 26: `source_detail/vvaharness/util/logs.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/report_augment/locate.py.sudo.md). Exact strings in the evidence asset support this conversion.
