# vvaharness/pipeline/stages/s8/validate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8/validate.py.evidence.json`. SHA-256: `bf553c5927ccaa899eb4864e0ab7dddfb8ca6c50750a8374f2c1581ccb714c23`.

```sudo
// Source: vvaharness/pipeline/stages/s8/validate.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import itertools; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from functools import cache; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/validate.py:22-27
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import VulnClass; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import SEV_RANK; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8 import facts as _facts; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.cwe import cwe_name; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/validate.py:28-36
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once re.compile('(?i)\\b(even without|future maintainer|alternatively\\b)'); assign in source target order to _HEDGE_RX. Then Evaluate once source_literal_34_15; assign in source target order to _HEDGE_NOTE.
// Source: vvaharness/pipeline/stages/s8/validate.py:39-43
// Source signature: location_key(ranked, step: int) -> tuple[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn location_key(ranked, step) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:40-41
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call. Then Evaluate once ranked[step].finding; assign in source target order to f.
  // Source: vvaharness/pipeline/stages/s8/validate.py:43-43
  End this invocation with (f.file, f.line_start).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:46-56
// Source signature: collapse_same_location(steps: list[int], ranked) -> tuple[list[int], int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn collapse_same_location(steps, ranked) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:47-49
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then For seen, assign set(); source annotation set[tuple[str, int]]. Then For kept, assign []; source annotation list[int].
  // Source: vvaharness/pipeline/stages/s8/validate.py:50-55
  for each s in steps {
    // Source: vvaharness/pipeline/stages/s8/validate.py:51-51
    In source order: Evaluate once location_key(ranked, s); assign in source target order to loc.
    // Source: vvaharness/pipeline/stages/s8/validate.py:52-53
    if (the source predicate loc in seen is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:53-53
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:54-55
    In source order: Evaluate seen.add(loc); retain side effects and discard the expression result. Then Evaluate kept.append(s); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:56-56
  End this invocation with (kept, len(steps) - len(kept)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:59-87
// Source signature: resolve_citation(repo_root: str | Path, file: str, line: int) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_citation(repo_root, file, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:60-60
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:61-62
  if (the source predicate not file or line < 1 is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:62-62
    End this invocation with False.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:64-67
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8/validate.py:65-65
    In source order: Evaluate once Path(repo_root).resolve(); assign in source target order to root.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:66-67
  On the first matching source exception (OSError, ValueError, RuntimeError), in handler order {
    // Source: vvaharness/pipeline/stages/s8/validate.py:67-67
    End this invocation with False.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:69-71
  // Source signature: _ok(rel: str) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _ok(rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/validate.py:71-71
    End this invocation with len(_facts._file_lines(root, rel)) >= line.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:74-75
  In source order: Evaluate once [file]; assign in source target order to candidates. Then Evaluate once file.lstrip('/\\'); assign in source target order to stripped.
  // Source: vvaharness/pipeline/stages/s8/validate.py:76-77
  if (the source predicate stripped != file is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:77-77
    In source order: Evaluate candidates.append(stripped); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:78-82
  if (the source predicate file.startswith(('/', '\\')) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:79-82
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s8/validate.py:80-80
      In source order: Evaluate candidates.append(str(Path(file).resolve().relative_to(root))); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:81-82
    On the first matching source exception (OSError, ValueError, RuntimeError), in handler order {
      // Source: vvaharness/pipeline/stages/s8/validate.py:82-82
      In source order: Perform no operation at this source statement.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:83-86
  for each cand in (file, stripped) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:84-84
    In source order: Evaluate once cand.partition('/'); assign in source target order to (head, _, tail).
    // Source: vvaharness/pipeline/stages/s8/validate.py:85-86
    if (the source predicate tail and head == root.name is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:86-86
      In source order: Evaluate candidates.append(tail); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:87-87
  End this invocation with any((_ok(c) for c in dict.fromkeys(candidates))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:91-92
In source order: Evaluate once re.compile(':(\\d+)\\s*$'); assign in source target order to _PACKED_LINE_RX. Then Evaluate once re.compile('^\\w+://[^/]+(/.*)$'); assign in source target order to _URL_PATH_RX.
// Source: vvaharness/pipeline/stages/s8/validate.py:95-107
// Source signature: _unpacked_citation(file: str, line: int) -> tuple[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _unpacked_citation(file, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:96-98
  In source order: Retain source documentation literal source_literal_96_4; it is not a model call. Then Evaluate once file or ''; assign in source target order to candidate. Then Evaluate once _URL_PATH_RX.match(candidate); assign in source target order to m.
  // Source: vvaharness/pipeline/stages/s8/validate.py:99-100
  if (the source predicate m is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:100-100
    In source order: Evaluate once m.group(1).lstrip('/'); assign in source target order to candidate.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:101-102
  if (the source predicate '\\' in candidate is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:102-102
    In source order: Evaluate once re.sub('^[A-Za-z]:\\\\', '', candidate).replace('\\', '/'); assign in source target order to candidate.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:104-104
  In source order: Evaluate once _PACKED_LINE_RX.search(candidate); assign in source target order to pm.
  // Source: vvaharness/pipeline/stages/s8/validate.py:105-106
  if (the source predicate pm and (not line or line == int(pm.group(1))) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:106-106
    In source order: Evaluate once (candidate[:pm.start()], int(pm.group(1))); assign in source target order to (candidate, line).
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:107-107
  End this invocation with (candidate, line).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:110-122
// Source signature: resolved_citation(repo_root: str | Path, file: str, line: int) -> tuple[bool, str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolved_citation(repo_root, file, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:112-114
  In source order: Retain source documentation literal source_literal_112_4; it is not a model call. Then Evaluate once (file or '').strip(); assign in source target order to file.
  // Source: vvaharness/pipeline/stages/s8/validate.py:115-116
  if (the source predicate resolve_citation(repo_root, file, line) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:116-116
    End this invocation with (True, file, line).
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:117-117
  In source order: Evaluate once _unpacked_citation(file, line); assign in source target order to (cand_file, cand_line).
  // Source: vvaharness/pipeline/stages/s8/validate.py:118-120
  if (the source predicate (cand_file, cand_line) != (file, line) and resolve_citation(repo_root, cand_file, cand_line) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:120-120
    End this invocation with (True, cand_file, cand_line).
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:122-122
  End this invocation with (False, file, 0).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:125-134
// Source signature: link_ok(link_evidence, steps, repo_root: str | Path) -> tuple[bool, int, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn link_ok(link_evidence, steps, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:127-133
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call. Then Evaluate once list(link_evidence or []); assign in source target order to links. Then Evaluate once max(len(steps) - 1, 0); assign in source target order to hops. Then Evaluate once sum((1 for ln in links if resolved_citation(repo_root, ln.file, ln.line)[0])); assign in source target order to resolved.
  // Source: vvaharness/pipeline/stages/s8/validate.py:134-134
  End this invocation with (len(links) >= hops and resolved == len(links), resolved, hops).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:138-138
In source order: Evaluate once ('#', '//', '/*', '*', '<!--'); assign in source target order to _COMMENT_PREFIXES.
// Source: vvaharness/pipeline/stages/s8/validate.py:141-145
// Source signature: _line_text(repo_root: str | Path, file: str, line: int) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _line_text(repo_root, file, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:142-144
  In source order: Retain source documentation literal source_literal_142_4; it is not a model call. Then Evaluate once _facts._file_lines(repo_root, file.lstrip('/\\')); assign in source target order to lines.
  // Source: vvaharness/pipeline/stages/s8/validate.py:145-145
  End this invocation with lines[line - 1] if 1 <= line <= len(lines) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:148-157
// Source signature: cited_comment_lines(link_evidence, repo_root: str | Path) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cited_comment_lines(link_evidence, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:149-150
  In source order: Retain source documentation literal source_literal_149_4; it is not a model call. Then For out, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/validate.py:151-156
  for each ln in link_evidence or [] {
    // Source: vvaharness/pipeline/stages/s8/validate.py:152-152
    In source order: Evaluate once _line_text(repo_root, ln.file, ln.line); assign in source target order to text.
    // Source: vvaharness/pipeline/stages/s8/validate.py:153-154
    if (the source predicate text is None is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:154-154
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:155-156
    if (the source predicate text.strip().startswith(_COMMENT_PREFIXES) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:156-156
      In source order: Evaluate out.append(source_template_156_23); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:157-157
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:160-164
// Source signature: clean_controls(values) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn clean_controls(values) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:161-161
  In source order: Retain source documentation literal source_literal_161_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:163-164
  End this invocation with list(dict.fromkeys((v.strip() for v in values or [] if isinstance(v, str) and v.strip()))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:167-173
// Source signature: clean_preconditions(chain) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn clean_preconditions(chain) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:168-170
  In source order: Retain source documentation literal source_literal_168_4; it is not a model call. Then Evaluate once clean_controls(getattr(chain, 'preconditions', [])); assign in source target order to pre.
  // Source: vvaharness/pipeline/stages/s8/validate.py:171-172
  if (the source predicate pre is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:172-172
    In source order: Evaluate COUNTERS.bump('s8_chain_gated'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:173-173
  End this invocation with pre.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:176-182
// Source signature: annotate_hedges(narrative: str) -> tuple[str, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn annotate_hedges(narrative) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:177-177
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:179-180
  if (the source predicate not (narrative and _HEDGE_RX.search(narrative)) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:180-180
    End this invocation with (narrative, False).
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:181-181
  In source order: Evaluate COUNTERS.bump('s8_chain_narrative_hedged'); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8/validate.py:182-182
  End this invocation with (source_template_182_11.strip(), True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:188-192
// Source signature: hardening_steps(steps: list[int], ranked) -> list[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn hardening_steps(steps, ranked) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:189-189
  In source order: Retain source documentation literal source_literal_189_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:191-192
  End this invocation with [i for i, s in enumerate(steps[:-1]) if getattr(ranked[s].finding, 'control_absence', False)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:195-213
In source order: Evaluate once source_literal_195_19; assign in source target order to _HARDENING_NOTE. Then Evaluate once '{n} of {m} step-to-step hop(s) carry a citation this scan could check.'; assign in source target order to _LINK_COVERAGE_NOTE. Then Evaluate once 'Link evidence cites a line that is wholly a comment ({where}), which documents an intention rather than the mechanism.'; assign in source target order to _COMMENT_CITATION_NOTE. Then Evaluate once 'The chain title names "{term}", which none of its steps covers.'; assign in source target order to _TITLE_DIVERGENCE_NOTE. Then Evaluate once 'Ends at the same final step (finding #{n}) as {others} other proposed path(s), reached from a different entry point.'; assign in source target order to NEAR_DUPLICATE_NOTE.
// Source: vvaharness/pipeline/stages/s8/validate.py:216-216
In source order: Evaluate once 7; assign in source target order to _HEAD_MIN_CHARS.
// Source: vvaharness/pipeline/stages/s8/validate.py:219-221
// Source signature: _tokens(text: str) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tokens(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:220-220
  In source order: Retain source documentation literal source_literal_220_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:221-221
  End this invocation with [t for t in re.split('[^A-Za-z]+', (text or '').lower()) if t].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:224-226
// Source signature: _words(text: str) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _words(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:225-225
  In source order: Retain source documentation literal source_literal_225_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:226-226
  End this invocation with set(_tokens(text)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:230-246
// Source: vvaharness/pipeline/stages/s8/validate.py:229-229
Before creating this callable, evaluate and retain decorators top-to-bottom: cache.
// Source: vvaharness/pipeline/stages/s8/validate.py:230-246
// Source signature: _class_phrases() -> tuple[set[str], set[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _class_phrases() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:231-233
  In source order: Retain source documentation literal source_literal_231_4; it is not a model call. Then For phrases, assign set(); source annotation set[str]. Then For heads, assign set(); source annotation set[str].
  // Source: vvaharness/pipeline/stages/s8/validate.py:234-245
  for each member in VulnClass {
    // Source: vvaharness/pipeline/stages/s8/validate.py:236-237
    if (the source predicate member is VulnClass.OTHER is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:237-237
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:238-238
    In source order: Evaluate once _tokens(member.value); assign in source target order to tokens.
    // Source: vvaharness/pipeline/stages/s8/validate.py:239-240
    if (the source predicate not tokens is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:240-240
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:241-242
    if (the source predicate len(tokens) > 1 is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:242-242
      In source order: Evaluate phrases.add(' '.join(tokens)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:244-245
    if (the source predicate len(tokens) == 1 or len(tokens[-1]) >= _HEAD_MIN_CHARS is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:245-245
      In source order: Evaluate heads.add(tokens[-1]); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:246-246
  End this invocation with (phrases, heads).
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/pipeline/stages/s8/validate.py:249-270
// Source signature: title_divergence(title: str, steps: list[int], ranked) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn title_divergence(title, steps, ranked) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:250-252
  In source order: Retain source documentation literal source_literal_250_4; it is not a model call. Then Evaluate once _class_phrases(); assign in source target order to (phrases, heads). Then For covered, assign set(); source annotation set[str].
  // Source: vvaharness/pipeline/stages/s8/validate.py:253-261
  for each s in steps {
    // Source: vvaharness/pipeline/stages/s8/validate.py:254-260
    In source order: Evaluate once ranked[s].finding; assign in source target order to f. Then Apply source augmented assignment covered |= _words(getattr(f.vuln_class, 'value', str(f.vuln_class))) with source evaluation/in-place semantics. Then Apply source augmented assignment covered |= _words(getattr(f, 'vuln_class_label', '')) with source evaluation/in-place semantics. Then Apply source augmented assignment covered |= _words(getattr(f, 'title', '')) with source evaluation/in-place semantics. Then Apply source augmented assignment covered |= _words(cwe_name(getattr(f, 'cwe', ''))) with source evaluation/in-place semantics.
    // Source: vvaharness/pipeline/stages/s8/validate.py:261-261
    In source order: Apply source augmented assignment covered |= _words(Path(f.file or '').name) with source evaluation/in-place semantics.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:262-263
  In source order: Evaluate once _words(title); assign in source target order to title_words. Then Evaluate once ' '.join(_tokens(title)); assign in source target order to flat.
  // Source: vvaharness/pipeline/stages/s8/validate.py:264-266
  for each phrase in sorted(phrases) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:265-266
    if (the source predicate ' ' in phrase and phrase in flat and (not set(phrase.split()) & covered) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:266-266
      End this invocation with phrase.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:267-269
  for each head in sorted(heads) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:268-269
    if (the source predicate head in title_words and head not in covered is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:269-269
      End this invocation with head.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:270-270
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:273-303
// Source signature: quality_annotations(chain, steps: list[int], ranked, repo_root: str | Path, *, links_ok: bool, resolved: int, hops: int, hardening: list[int]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn quality_annotations(chain, steps, ranked, repo_root, links_ok, resolved, hops, hardening) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:277-279
  In source order: Retain source documentation literal source_literal_277_4; it is not a model call. Then For out, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/validate.py:280-283
  if (the source predicate hardening is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:281-283
    In source order: Evaluate COUNTERS.bump('s8_chain_hardening_step', len(hardening)); retain side effects and discard the expression result. Then Evaluate out.append(_HARDENING_NOTE.format(pos=', '.join((str(p + 1) for p in hardening)))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:284-284
  In source order: Evaluate once list(getattr(chain, 'link_evidence', []) or []); assign in source target order to links.
  // Source: vvaharness/pipeline/stages/s8/validate.py:285-292
  if (the source predicate not links_ok is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:286-286
    In source order: Evaluate COUNTERS.bump('s8_chain_link_coverage_short'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s8/validate.py:288-291
    if (the source predicate links is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:289-291
      In source order: Evaluate COUNTERS.bump('s8_chain_link_evidence_missing' if len(links) != hops else 's8_chain_citation_unresolved'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:292-292
    In source order: Evaluate out.append(_LINK_COVERAGE_NOTE.format(n=resolved, m=hops)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:293-293
  In source order: Evaluate once cited_comment_lines(links, repo_root); assign in source target order to comment_cites.
  // Source: vvaharness/pipeline/stages/s8/validate.py:294-298
  if (the source predicate comment_cites is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:295-298
    In source order: Evaluate COUNTERS.bump('s8_chain_cited_line_comment', len(comment_cites)); retain side effects and discard the expression result. Then Evaluate out.append(_COMMENT_CITATION_NOTE.format(where=', '.join(comment_cites[:3]))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:299-299
  In source order: Evaluate once title_divergence(getattr(chain, 'title', ''), steps, ranked); assign in source target order to term.
  // Source: vvaharness/pipeline/stages/s8/validate.py:300-302
  if (the source predicate term is truthy) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:301-302
    In source order: Evaluate COUNTERS.bump('s8_chain_title_divergence'); retain side effects and discard the expression result. Then Evaluate out.append(_TITLE_DIVERGENCE_NOTE.format(term=term)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:303-303
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:309-312
// Source signature: lift_allowed(links_ok: bool, hardening: list[int], hedged: bool) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn lift_allowed(links_ok, hardening, hedged) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:310-310
  In source order: Retain source documentation literal source_literal_310_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:312-312
  End this invocation with links_ok and (not hardening) and (not hedged).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:318-321
// Source signature: _survivor_key(chain) -> tuple
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _survivor_key(chain) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:319-319
  In source order: Retain source documentation literal source_literal_319_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/validate.py:321-321
  End this invocation with (SEV_RANK[chain.severity], -len(chain.link_evidence), chain.title).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:324-342
// Source signature: dedup_chains(chains: list) -> tuple[list, int, list[tuple[int, int]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dedup_chains(chains) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:325-327
  In source order: Retain source documentation literal source_literal_325_4; it is not a model call. Then For best, assign {}; source annotation dict[tuple, int].
  // Source: vvaharness/pipeline/stages/s8/validate.py:328-332
  for each (i, c) in enumerate(chains) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:329-330
    In source order: Evaluate once tuple(c.steps); assign in source target order to key. Then Evaluate once best.get(key); assign in source target order to first.
    // Source: vvaharness/pipeline/stages/s8/validate.py:331-332
    if (the source predicate first is None or _survivor_key(c) < _survivor_key(chains[first]) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:332-332
      In source order: Evaluate once i; assign in source target order to best[key].
    }
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:333-336
  In source order: Evaluate once [chains[i] for i in sorted(best.values())]; assign in source target order to kept. Then For related, assign []; source annotation list[tuple[int, int]].
  // Source: vvaharness/pipeline/stages/s8/validate.py:337-341
  for each ((a, ca), (b, cb)) in itertools.combinations(enumerate(kept), 2) {
    // Source: vvaharness/pipeline/stages/s8/validate.py:339-340
    if (the source predicate ca.steps[-1] != cb.steps[-1] or ca.steps[0] == cb.steps[0] is truthy) {
      // Source: vvaharness/pipeline/stages/s8/validate.py:340-340
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/validate.py:341-341
    In source order: Evaluate related.append((a, b)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/validate.py:342-342
  End this invocation with (kept, len(chains) - len(kept), related).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/validate.py:348-358
// Source signature: unpromoted_links(claims: list[tuple[int, int]], chains: list, ranked) -> list[tuple[int, int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn unpromoted_links(claims, chains, ranked) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/validate.py:350-357
  In source order: Retain source documentation literal source_literal_350_4; it is not a model call. Then Evaluate once {(location_key(ranked, a), location_key(ranked, b)) for c in chains for i, a in enumerate(c.steps) for b in c.steps[i + 1:]}; assign in source target order to covered. Then Evaluate once ((o, t, location_key(ranked, o), location_key(ranked, t)) for o, t in claims); assign in source target order to keyed.
  // Source: vvaharness/pipeline/stages/s8/validate.py:358-358
  End this invocation with [(o, t) for o, t, lo, lt in keyed if lo != lt and (lo, lt) not in covered].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import VulnClass` at source line 24: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.vocab import SEV_RANK` at source line 25: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8 import facts as _facts` at source line 26: `source_detail/vvaharness/pipeline/stages/s8/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8 import facts as _facts` at source line 26: `source_detail/vvaharness/pipeline/stages/s8/facts.py.sudo.md`.
- `from vvaharness.report.cwe import cwe_name` at source line 27: `source_detail/vvaharness/report/cwe.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 28: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s8/validate.py.sudo.md). Exact strings in the evidence asset support this conversion.
