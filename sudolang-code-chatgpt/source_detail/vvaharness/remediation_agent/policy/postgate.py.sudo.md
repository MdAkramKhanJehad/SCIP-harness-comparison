# vvaharness/remediation_agent/policy/postgate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/policy/postgate.py.evidence.json`. SHA-256: `f2adc06bdc1cc46ed942f5c086a71f7c79c2dd220ac723731a7147baa53aaad0`.

```sudo
// Source: vvaharness/remediation_agent/policy/postgate.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/postgate.py:22-32
In source order: Resolve source import from vvaharness.remediation_agent.artifacts.diff import _norm_path, capture_git_diff, changed_files_whole_tree, changed_since_snapshot, synth_unified_diff; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.models import RemediationVerdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.context import PolicyContext; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.decide import PreResult; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.patch_content import scan_added_lines; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/postgate.py:33-39
In source order: Resolve source import from vvaharness.remediation_agent.policy.revert import revert_files; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy.workflow_refs import introduced_unsafe_workflow_refs; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate import cap_verdict, inspect_diff; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.policy_gate.matching import _glob_match; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.target import RemediationTarget; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/policy/postgate.py:40-46
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.git_paths import is_git_metadata; preserve alias and import-time effects. Then Evaluate once 20000; assign in source target order to _WORKTREE_SCAN_MAX. Then Evaluate once 20000; assign in source target order to _WORKTREE_DIR_MAX.
// Source: vvaharness/remediation_agent/policy/postgate.py:49-80
// Source signature: worktree_forbidden_matches(repo: Path, patterns: list[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn worktree_forbidden_matches(repo, patterns) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/postgate.py:50-50
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call.
  // Source: vvaharness/remediation_agent/policy/postgate.py:51-52
  if (the source predicate not patterns is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:52-52
    End this invocation with [].
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:53-56
  In source order: Evaluate once Path(repo); assign in source target order to repo. Then For out, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to seen. Then Evaluate once 0; assign in source target order to dirs_seen.
  // Source: vvaharness/remediation_agent/policy/postgate.py:57-79
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/policy/postgate.py:58-77
    for each (dirpath, _dirnames, filenames) in os.walk(repo, followlinks=False) {
      // Source: vvaharness/remediation_agent/policy/postgate.py:59-59
      In source order: Apply source augmented assignment dirs_seen += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/remediation_agent/policy/postgate.py:60-61
      if (the source predicate dirs_seen > _WORKTREE_DIR_MAX is truthy) {
        // Source: vvaharness/remediation_agent/policy/postgate.py:61-61
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vvaharness/remediation_agent/policy/postgate.py:62-77
      for each name in filenames {
        // Source: vvaharness/remediation_agent/policy/postgate.py:63-63
        In source order: Evaluate once Path(dirpath) / name; assign in source target order to p.
        // Source: vvaharness/remediation_agent/policy/postgate.py:64-65
        if (the source predicate not p.is_file() is truthy) {
          // Source: vvaharness/remediation_agent/policy/postgate.py:65-65
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/remediation_agent/policy/postgate.py:67-67
        In source order: Apply source augmented assignment seen += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/remediation_agent/policy/postgate.py:68-69
        if (the source predicate seen > _WORKTREE_SCAN_MAX is truthy) {
          // Source: vvaharness/remediation_agent/policy/postgate.py:69-69
          End this invocation with out.
        }
        // Source: vvaharness/remediation_agent/policy/postgate.py:70-73
        Perform the following protected operations {
          // Source: vvaharness/remediation_agent/policy/postgate.py:71-71
          In source order: Evaluate once p.relative_to(repo).as_posix(); assign in source target order to rel.
        }
        // Source: vvaharness/remediation_agent/policy/postgate.py:72-73
        On the first matching source exception ValueError, in handler order {
          // Source: vvaharness/remediation_agent/policy/postgate.py:73-73
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/remediation_agent/policy/postgate.py:74-77
        for each pat in patterns {
          // Source: vvaharness/remediation_agent/policy/postgate.py:75-77
          if (the source predicate _glob_match(rel, pat) is truthy) {
            // Source: vvaharness/remediation_agent/policy/postgate.py:76-76
            In source order: Evaluate out.append(rel); retain side effects and discard the expression result.
            // Source: vvaharness/remediation_agent/policy/postgate.py:77-77
            Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
          }
        }
      }
    }
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:78-79
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/policy/postgate.py:79-79
    End this invocation with out.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:80-80
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/postgate.py:85-91
// Source: vvaharness/remediation_agent/policy/postgate.py:84-84
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/remediation_agent/policy/postgate.py:85-91
interface PostResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/remediation_agent/policy/postgate.py:86-90
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then For reverted, declare without assigning a value; source annotation list[str]. Then For matched_globs, declare without assigning a value; source annotation list[str]. Then For downgraded, declare without assigning a value; source annotation bool. Then For final_verdict, declare without assigning a value; source annotation str.
  // Source: vvaharness/remediation_agent/policy/postgate.py:91-91
  In source order: For reason, assign None; source annotation str | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/remediation_agent/policy/postgate.py:94-100
// Source signature: _gates_ok(verdict: RemediationVerdict) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gates_ok(verdict) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/postgate.py:95-96
  In source order: Retain source documentation literal source_literal_95_4; it is not a model call. Then Evaluate once getattr(verdict, 'gates', None); assign in source target order to g.
  // Source: vvaharness/remediation_agent/policy/postgate.py:97-98
  if (the source predicate g is None is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:98-98
    End this invocation with False.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:99-100
  End this invocation with g.source == 'pass' and g.sink == 'pass' and (g.missing_control == 'pass').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/policy/postgate.py:103-222
// Source signature: enforce_post(ctx: PolicyContext, target: RemediationTarget, verdict: RemediationVerdict, pre: PreResult, *, repo: Path, before_snapshot: dict[str, str | None] | None=None, all_gates_passed: bool=True) -> PostResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn enforce_post(ctx, target, verdict, pre, repo, before_snapshot, all_gates_passed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/policy/postgate.py:108-115
  In source order: Retain source documentation literal source_literal_108_4; it is not a model call. Then Evaluate once [c.file for c in verdict.changes if c.file]; assign in source target order to changed. Then Evaluate once changed_files_whole_tree(repo); assign in source target order to whole_tree. Then For worktree_forbidden, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/policy/postgate.py:116-118
  if (the source predicate not whole_tree is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:117-118
    In source order: Evaluate once worktree_forbidden_matches(repo, [*ctx.gate.forbid_patch_paths, *ctx.gate.deny_paths]); assign in source target order to worktree_forbidden.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:122-131
  if (the source predicate before_snapshot is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:123-131
    In source order: Evaluate once set(before_snapshot) - set(changed_since_snapshot(repo, before_snapshot)); assign in source target order to unchanged_baseline. Then Evaluate once {_norm_path(f) for f in unchanged_baseline}; assign in source target order to unchanged_norm. Then Evaluate once [f for f in whole_tree if _norm_path(f) not in unchanged_norm]; assign in source target order to whole_tree. Then Evaluate once [f for f in worktree_forbidden if _norm_path(f) not in unchanged_norm]; assign in source target order to worktree_forbidden. Then Evaluate once [f for f in changed if is_git_metadata(f) or _norm_path(f) not in unchanged_norm]; assign in source target order to changed.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:134-136
  In source order: Evaluate once list(dict.fromkeys([*changed, *whole_tree])); assign in source target order to diff_scope. Then Evaluate once capture_git_diff(repo, diff_scope, baseline=before_snapshot); assign in source target order to diff.
  // Source: vvaharness/remediation_agent/policy/postgate.py:137-138
  if (the source predicate not diff and before_snapshot is not None is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:138-138
    In source order: Evaluate once synth_unified_diff(repo, before_snapshot, extra_files=diff_scope); assign in source target order to diff.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:139-144
  In source order: Evaluate once inspect_diff(diff); assign in source target order to diff_files. Then Evaluate once list(dict.fromkeys([*diff_files, *changed, *whole_tree, *worktree_forbidden])); assign in source target order to candidates. Then Evaluate once ctx.gate.forbidden_files(candidates); assign in source target order to forbidden. Then For matched, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/policy/postgate.py:145-149
  for each f in forbidden {
    // Source: vvaharness/remediation_agent/policy/postgate.py:146-147
    In source order: Evaluate once ctx.gate.patch_touches_forbidden([f]) or ctx.gate.changed_paths_hit_deny([f]); assign in source target order to g.
    // Source: vvaharness/remediation_agent/policy/postgate.py:148-149
    if (the source predicate g is truthy) {
      // Source: vvaharness/remediation_agent/policy/postgate.py:149-149
      In source order: Evaluate matched.append(g); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:151-158
  In source order: Evaluate once introduced_unsafe_workflow_refs(repo, before_snapshot); assign in source target order to unsafe_refs. Then Evaluate once scan_added_lines(diff); assign in source target order to unsafe_content. Then Evaluate once list(dict.fromkeys([*forbidden, *unsafe_refs, *unsafe_content])); assign in source target order to bad. Then Evaluate once pre.decision.action; assign in source target order to ceiling.
  // Source: vvaharness/remediation_agent/policy/postgate.py:159-166
  if (the source predicate not bad is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:161-164
    In source order: Evaluate once bool(diff and diff.strip()); assign in source target order to patch_applied. Then Evaluate once all_gates_passed and _gates_ok(verdict) and patch_applied and (verdict.verdict in ('Fixed', 'Partially Fixed')); assign in source target order to gates_passed.
    // Source: vvaharness/remediation_agent/policy/postgate.py:165-166
    End this invocation with PostResult(reverted=[], matched_globs=[], downgraded=False, final_verdict=cap_verdict(ceiling, gates_passed)).
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:168-173
  In source order: Evaluate once revert_files(repo, bad, before_snapshot); assign in source target order to reverted. Then Evaluate once {_norm_path(f) for f in bad}; assign in source target order to bad_norm. Then Evaluate once [c for c in verdict.changes if _norm_path(c.file) not in bad_norm]; assign in source target order to verdict.changes. Then For notes, assign []; source annotation list[str].
  // Source: vvaharness/remediation_agent/policy/postgate.py:174-177
  if (the source predicate forbidden is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:175-177
    In source order: Evaluate notes.append(source_template_176_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:178-184
  if (the source predicate unsafe_refs is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:179-184
    In source order: Evaluate once '; '.join((source_template_180_12 for path, refs in unsafe_refs.items())); assign in source target order to detail. Then Evaluate notes.append(source_template_182_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:185-194
  if (the source predicate unsafe_content is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:186-194
    In source order: Evaluate once '; '.join((source_template_187_12 for path, hits in sorted(unsafe_content.items()))); assign in source target order to detail. Then Evaluate notes.append(source_template_190_12); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:195-195
  In source order: Evaluate once [f for f in bad if is_git_metadata(f)]; assign in source target order to refused.
  // Source: vvaharness/remediation_agent/policy/postgate.py:196-198
  if (the source predicate refused is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:197-198
    In source order: Evaluate notes.append(source_template_197_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:199-203
  In source order: Evaluate once source_template_200_8; assign in source target order to note. Then Evaluate once list(verdict.remaining_risks) + [note]; assign in source target order to verdict.remaining_risks.
  // Source: vvaharness/remediation_agent/policy/postgate.py:207-210
  if (the source predicate unsafe_refs or unsafe_content is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:208-208
    In source order: Evaluate once 'Not Fixed'; assign in source target order to verdict.verdict.
  }
  else {
    // Source: vvaharness/remediation_agent/policy/postgate.py:209-210
    if (the source predicate verdict.verdict in ('Fixed', 'Partially Fixed') is truthy) {
      // Source: vvaharness/remediation_agent/policy/postgate.py:210-210
      In source order: Evaluate once 'Needs Review'; assign in source target order to verdict.verdict.
    }
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:211-213
  In source order: Evaluate once (verdict.summary + ' ' if verdict.summary else '') + note; assign in source target order to verdict.summary. Then Evaluate console.write(source_template_212_18); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/policy/postgate.py:214-219
  if (the source predicate unsafe_refs is truthy) {
    // Source: vvaharness/remediation_agent/policy/postgate.py:215-215
    In source order: Evaluate once 'unsafe_workflow_reference'; assign in source target order to reason.
  }
  else {
    // Source: vvaharness/remediation_agent/policy/postgate.py:216-219
    if (the source predicate unsafe_content is truthy) {
      // Source: vvaharness/remediation_agent/policy/postgate.py:217-217
      In source order: Evaluate once 'unsafe_patch_content'; assign in source target order to reason.
    }
    else {
      // Source: vvaharness/remediation_agent/policy/postgate.py:219-219
      In source order: Evaluate once None; assign in source target order to reason.
    }
  }
  // Source: vvaharness/remediation_agent/policy/postgate.py:220-222
  End this invocation with PostResult(reverted=reverted, matched_globs=sorted(set(matched)), downgraded=True, final_verdict='REJECT', reason=reason).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.remediation_agent.artifacts.diff import _norm_path, capture_git_diff, changed_files_whole_tree, changed_since_snapshot, synth_unified_diff` at source line 22: `source_detail/vvaharness/remediation_agent/artifacts/diff/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.models import RemediationVerdict` at source line 29: `source_detail/vvaharness/remediation_agent/models/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.context import PolicyContext` at source line 30: `source_detail/vvaharness/remediation_agent/policy/context.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.decide import PreResult` at source line 31: `source_detail/vvaharness/remediation_agent/policy/decide.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.patch_content import scan_added_lines` at source line 32: `source_detail/vvaharness/remediation_agent/policy/patch_content.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.revert import revert_files` at source line 33: `source_detail/vvaharness/remediation_agent/policy/revert.py.sudo.md`.
- `from vvaharness.remediation_agent.policy.workflow_refs import introduced_unsafe_workflow_refs` at source line 34: `source_detail/vvaharness/remediation_agent/policy/workflow_refs.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate import cap_verdict, inspect_diff` at source line 37: `source_detail/vvaharness/remediation_agent/policy_gate/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.policy_gate.matching import _glob_match` at source line 38: `source_detail/vvaharness/remediation_agent/policy_gate/matching.py.sudo.md`.
- `from vvaharness.remediation_agent.target import RemediationTarget` at source line 39: `source_detail/vvaharness/remediation_agent/target.py.sudo.md`.
- `from vvaharness.util import console` at source line 40: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 40: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.git_paths import is_git_metadata` at source line 41: `source_detail/vvaharness/util/git_paths.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/policy/postgate.py.sudo.md). Exact strings in the evidence asset support this conversion.
