# vvaharness/pipeline/stages/s8/window.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8/window.py.evidence.json`. SHA-256: `51f8750258a1cd701169b1a605c29b3fd1eed44862f9860fa325c094d4e699c4`.

```sudo
// Source: vvaharness/pipeline/stages/s8/window.py:16-22
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import ContextPackage, Finding, Severity; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/window.py:23-38
In source order: Resolve source import from vvaharness.models.vocab import SEV_RANK; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.outcomes import ChainReport, final_severity, offensive_rank; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8.prompts import SYSTEM, build_prompt, facts_enabled, finding_block, hop_text_enabled, repo_fact_blocks; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/window.py:39-46
In source order: Resolve source import from vvaharness.util.tokens import estimate_tokens; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 1500; assign in source target order to _OUT_RESERVE. Then Evaluate once 100; assign in source target order to _TOKENS_PER_ENTRY.
// Source: vvaharness/pipeline/stages/s8/window.py:48-53
In source order: Evaluate once estimate_tokens(json.dumps(ChainReport.model_json_schema())) + 250; assign in source target order to _SCHEMA_TOKENS. Then Evaluate once 1.25; assign in source target order to _PULLIN_CEILING. Then Evaluate once (Severity.MEDIUM, Severity.LOW, Severity.INFO); assign in source target order to _PULLIN_BANDS.
// Source: vvaharness/pipeline/stages/s8/window.py:56-62
// Source signature: _floor_order(findings: list[Finding]) -> list[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _floor_order(findings) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/window.py:57-57
  In source order: Retain source documentation literal source_literal_57_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/window.py:59-62
  End this invocation with sorted(range(len(findings)), key=lambda i: (SEV_RANK[final_severity(findings[i], findings[i].severity)], offensive_rank(findings[i]))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/window.py:65-71
// Source signature: half_window(findings: list[Finding], window: list[int]) -> list[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn half_window(findings, window) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/window.py:66-70
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call. Then Evaluate once [findings[i] for i in window]; assign in source target order to sub. Then Evaluate once _floor_order(sub); assign in source target order to order. Then Evaluate once max(1, len(order) // 2); assign in source target order to half_n.
  // Source: vvaharness/pipeline/stages/s8/window.py:71-71
  End this invocation with sorted((window[k] for k in order[:half_n])).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/window.py:74-143
// Source signature: select_window(findings: list[Finding], ctx: ContextPackage, cfg) -> list[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn select_window(findings, ctx, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/window.py:76-80
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call. Then Evaluate once len(findings); assign in source target order to n. Then Evaluate once int(knob(cfg, 'step8.prompt_token_budget', 100000) or 100000); assign in source target order to budget. Then Evaluate once int(knob(cfg, 'step8.max_tokens', 64000) or 64000); assign in source target order to max_out. Then Evaluate once max((max_out - _OUT_RESERVE) // _TOKENS_PER_ENTRY, 1); assign in source target order to k_out.
  // Source: vvaharness/pipeline/stages/s8/window.py:83-92
  In source order: Evaluate once facts_enabled(cfg); assign in source target order to facts_on. Then Evaluate once hop_text_enabled(cfg); assign in source target order to hop_text. Then Evaluate once [estimate_tokens(finding_block(source_template_86_38, findings[i], ctx, facts_on, hop_text)) for i in range(n)]; assign in source target order to block_costs. Then Evaluate once build_prompt([], ctx, labels=[], cfg=cfg); assign in source target order to scaffold. Then Evaluate once repo_fact_blocks(findings, ctx, [source_template_91_50 for i in range(n)], facts_on); assign in source target order to repo_facts.
  // Source: vvaharness/pipeline/stages/s8/window.py:93-94
  In source order: Evaluate once estimate_tokens(SYSTEM) + estimate_tokens(scaffold) + estimate_tokens(repo_facts) + _SCHEMA_TOKENS; assign in source target order to fixed.
  // Source: vvaharness/pipeline/stages/s8/window.py:96-97
  if (the source predicate fixed + sum(block_costs) <= budget and n <= k_out is truthy) {
    // Source: vvaharness/pipeline/stages/s8/window.py:97-97
    End this invocation with list(range(n)).
  }
  // Source: vvaharness/pipeline/stages/s8/window.py:99-101
  In source order: Evaluate once _floor_order(findings); assign in source target order to order. Then For included, assign []; source annotation list[int]. Then Evaluate once fixed; assign in source target order to total.
  // Source: vvaharness/pipeline/stages/s8/window.py:102-107
  for each i in order {
    // Source: vvaharness/pipeline/stages/s8/window.py:104-105
    if (the source predicate len(included) >= k_out or total + block_costs[i] > budget is truthy) {
      // Source: vvaharness/pipeline/stages/s8/window.py:105-105
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/pipeline/stages/s8/window.py:106-107
    In source order: Evaluate included.append(i); retain side effects and discard the expression result. Then Apply source augmented assignment total += block_costs[i] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s8/window.py:110-112
  In source order: Evaluate once set(included); assign in source target order to included_set. Then Evaluate once {findings[i].file for i in included}; assign in source target order to seed_files. Then Evaluate once 0; assign in source target order to pullins.
  // Source: vvaharness/pipeline/stages/s8/window.py:113-123
  for each i in order {
    // Source: vvaharness/pipeline/stages/s8/window.py:114-115
    if (the source predicate i in included_set or len(included) >= k_out is truthy) {
      // Source: vvaharness/pipeline/stages/s8/window.py:115-115
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/window.py:116-116
    In source order: Evaluate once findings[i]; assign in source target order to f.
    // Source: vvaharness/pipeline/stages/s8/window.py:117-123
    if (the source predicate final_severity(f, f.severity) in _PULLIN_BANDS and f.file in seed_files and (total + block_costs[i] <= budget * _PULLIN_CEILING) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/window.py:120-123
      In source order: Evaluate included.append(i); retain side effects and discard the expression result. Then Evaluate included_set.add(i); retain side effects and discard the expression result. Then Apply source augmented assignment total += block_costs[i] with source evaluation/in-place semantics. Then Apply source augmented assignment pullins += 1 with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/window.py:125-125
  In source order: Evaluate once n - len(included); assign in source target order to excluded.
  // Source: vvaharness/pipeline/stages/s8/window.py:126-128
  if (the source predicate not excluded is truthy) {
    // Source: vvaharness/pipeline/stages/s8/window.py:128-128
    End this invocation with sorted(included).
  }
  // Source: vvaharness/pipeline/stages/s8/window.py:129-129
  In source order: Evaluate COUNTERS.bump('s8_findings_windowed', excluded); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8/window.py:130-131
  if (the source predicate pullins is truthy) {
    // Source: vvaharness/pipeline/stages/s8/window.py:131-131
    In source order: Evaluate COUNTERS.bump('s8_windowed_pullins', pullins); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/window.py:133-133
  In source order: For by_band, assign {}; source annotation dict[str, list[int]].
  // Source: vvaharness/pipeline/stages/s8/window.py:134-136
  for each i in range(n) {
    // Source: vvaharness/pipeline/stages/s8/window.py:135-136
    In source order: Evaluate once final_severity(findings[i], findings[i].severity).value; assign in source target order to band. Then Apply source augmented assignment by_band.setdefault(band, [0, 0])[0 if i in included_set else 1] += 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s8/window.py:137-141
  In source order: Evaluate once '  '.join((source_template_137_22 for b, (inc, exc) in sorted(by_band.items()))); assign in source target order to bands. Then Evaluate log.warning(Event.S8_ENRICHMENT_WINDOWED, sent=len(included), findings=n, pullins=pullins, est_tokens=total, budget=budget, pullin_ceiling=_PULLIN_CEILING, k_out=k_out, bands=bands); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8/window.py:143-143
  End this invocation with sorted(included).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.models import ContextPackage, Finding, Severity` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.vocab import SEV_RANK` at source line 23: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.outcomes import ChainReport, final_severity, offensive_rank` at source line 24: `source_detail/vvaharness/pipeline/stages/s8/outcomes.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8.prompts import SYSTEM, build_prompt, facts_enabled, finding_block, hop_text_enabled, repo_fact_blocks` at source line 29: `source_detail/vvaharness/pipeline/stages/s8/prompts.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 37: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 38: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.tokens import estimate_tokens` at source line 39: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 40: `source_detail/vvaharness/util/events.py.sudo.md`.
