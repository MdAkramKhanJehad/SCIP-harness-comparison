# vvaharness/pipeline/stages/s8/outcomes.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/pipeline/stages/s8/outcomes.py.evidence.json`. SHA-256: `948538b2505ff740873c769bee48ee4417309b2f25c0ec2263d133c4f0b78e3b`.

```sudo
// Source: vvaharness/pipeline/stages/s8/outcomes.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import itertools; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:22-35
In source order: Resolve source import from typing import NamedTuple; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator; preserve alias and import-time effects. Then Resolve source import from pydantic.json_schema import SkipJsonSchema; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import Chain, FinalReport, Finding, LinkEvidence, RankedFinding, Severity; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan._coerce import text as _coerce_text; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:36-40
In source order: Resolve source import from vvaharness.models.scan.findings import NOT_RANKED_NOTE; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import SEV_RANK; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.s8 import validate as _validate; preserve alias and import-time effects. Then Resolve source import from vvaharness.report import cvss as _cvss; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.config import knob; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:41-42
In source order: Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.json_extract import extract_json; preserve alias and import-time effects.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:45-53
// Source signature: _str_list(v: object) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _str_list(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:46-46
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:47-48
  if (the source predicate v is None is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:48-48
    End this invocation with [].
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:49-50
  if (the source predicate isinstance(v, str) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:50-50
    End this invocation with [v].
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:51-52
  if (the source predicate isinstance(v, list) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:52-52
    End this invocation with [x if isinstance(x, str) else str(x) for x in v].
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:53-53
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:58-58
In source order: Evaluate once 1000; assign in source target order to _CHAINS_INVALID_MAX.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:61-69
// Source signature: _salvage(items: list, model: type[BaseModel]) -> tuple[list, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _salvage(items, model) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:62-63
  In source order: Retain source documentation literal source_literal_62_4; it is not a model call. Then For kept, assign []; source annotation list.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:64-68
  for each item in items {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:65-68
    Perform the following protected operations {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:66-66
      In source order: Evaluate kept.append(model.model_validate(item)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:67-68
    On the first matching source exception ValidationError, in handler order {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:68-68
      In source order: Perform no operation at this source statement.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:69-69
  End this invocation with (kept, len(items) - len(kept)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:72-99
interface RankedEntry {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:73-87
  In source order: For finding_id, assign Field(description='Echo the FINDING id you were given, verbatim.'); source annotation str. Then For severity, assign Field(default='', description=source_literal_75_8); source annotation str. Then For exploitability_notes, assign Field(default='', description=source_literal_79_8); source annotation str. Then For feeds, assign Field(default=[], description=source_literal_82_8); source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:93-94
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:90-92
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('finding_id', 'severity', 'exploitability_notes', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:93-94
  // Source signature: _coerce_str(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_str(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:94-94
    End this invocation with _coerce_text(v).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:98-99
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:96-97
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('feeds', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:98-99
  // Source signature: _coerce_feeds(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_feeds(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:99-99
    End this invocation with _str_list(v).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:102-152
interface ChainEntry {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:103-114
  In source order: For title, assign Field(description="The chain in a few words, e.g. 'SSRF -> metadata creds -> S3'."); source annotation str. Then For steps, assign Field(description=source_literal_105_8); source annotation list[str]. Then For severity, assign Field(default='', description=source_literal_108_8); source annotation str. Then For blocked_by_controls, assign Field(default=[], description='Names of design controls that genuinely block this chain, if any.'); source annotation list[str]. Then For narrative, assign Field(default='', description=source_literal_113_8); source annotation str.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:116-127
  In source order: For link_evidence, assign Field(default=[], description=source_literal_117_8); source annotation list[LinkEvidence]. Then For entry_reachability, assign Field(default='', description=source_literal_122_8); source annotation str. Then For preconditions, assign Field(default=[], description=source_literal_125_8); source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:133-134
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:130-132
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('title', 'severity', 'narrative', 'entry_reachability', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:133-134
  // Source signature: _coerce_str(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_str(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:134-134
    End this invocation with _coerce_text(v).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:139-140
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:136-138
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('steps', 'blocked_by_controls', 'preconditions', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:139-140
  // Source signature: _coerce_str_list(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_str_list(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:140-140
    End this invocation with _str_list(v).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:144-152
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:142-143
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('link_evidence', mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:144-152
  // Source signature: _coerce_links(cls, v: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _coerce_links(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:147-148
    if (the source predicate not isinstance(v, list) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:148-148
      End this invocation with [].
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:149-149
    In source order: Evaluate once [x for x in v if isinstance(x, (dict, LinkEvidence))]; assign in source target order to kept.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:150-151
    if (the source predicate len(kept) < len(v) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:151-151
      In source order: Evaluate COUNTERS.bump('s8_link_evidence_entry_invalid', len(v) - len(kept)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:152-152
    End this invocation with kept.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:157-198
interface ChainReport {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:158-172
  In source order: For ranked_findings, assign Field(default=[], description=source_literal_159_8); source annotation list[RankedEntry]. Then For chains, assign Field(default=[], description='Chains of two or more findings. Empty is correct when no finding feeds another — an invented chain is worse than none.'); source annotation list[ChainEntry]. Then For summary, assign Field(description=source_literal_167_8); source annotation str. Then For chains_invalid, assign 0; source annotation SkipJsonSchema[int].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:176-198
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:174-175
  Before creating this callable, evaluate and retain decorators top-to-bottom: model_validator(mode='before'), classmethod.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:176-198
  // Source signature: _salvage_entries(cls, data: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _salvage_entries(cls, data) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:179-180
    if (the source predicate not isinstance(data, dict) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:180-180
      End this invocation with data.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:181-181
    In source order: Evaluate once dict(data); assign in source target order to data.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:182-183
    if (the source predicate 'chains' not in data is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:183-183
      In source order: Evaluate COUNTERS.bump('s8_chains_key_absent'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:184-184
    In source order: For dropped, assign {}; source annotation dict[str, int].
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:185-188
    for each (field, model) in (('ranked_findings', RankedEntry), ('chains', ChainEntry)) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:186-186
      In source order: Evaluate once data.get(field); assign in source target order to items.
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:187-188
      if (the source predicate isinstance(items, list) is truthy) {
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:188-188
        In source order: Evaluate once _salvage(items, model); assign in source target order to (data[field], dropped[field]).
      }
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:189-191
    for each (field, n) in dropped.items() {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:190-191
      if (the source predicate n is truthy) {
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:191-191
        In source order: Evaluate COUNTERS.bump(source_template_191_30, n); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:194-194
    In source order: Evaluate once data.get('chains_invalid'); assign in source target order to carried.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:195-196
    if (the source predicate type(carried) is not int or not 0 <= carried <= _CHAINS_INVALID_MAX is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:196-196
      In source order: Evaluate once 0; assign in source target order to carried.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:197-197
    In source order: Evaluate once carried + dropped.get('chains', 0); assign in source target order to data['chains_invalid'].
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:198-198
    End this invocation with data.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:201-206
// Source signature: parse_chain_reply(raw: str) -> ChainReport
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_chain_reply(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:202-202
  In source order: Retain source documentation literal source_literal_202_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:203-206
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:204-204
    End this invocation with ChainReport.model_validate_json(raw).
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:205-206
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:206-206
    End this invocation with ChainReport.model_validate(extract_json(raw)).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:209-211
// Source signature: finding_ids(findings: list[Finding]) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn finding_ids(findings) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:210-210
  In source order: Retain source documentation literal source_literal_210_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:211-211
  End this invocation with {source_template_211_12: i for i in range(len(findings))}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:214-219
In source order: Evaluate once {'critical': Severity.CRITICAL, 'high': Severity.HIGH, 'medium': Severity.MEDIUM, 'low': Severity.LOW}; assign in source target order to CVSS_BAND_TO_SEV.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:221-223
// Source signature: _strongest(severities: list[Severity]) -> Severity
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _strongest(severities) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:222-222
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:223-223
  End this invocation with min(severities, key=lambda s: SEV_RANK[s]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:226-228
// Source signature: _weakest(severities: list[Severity]) -> Severity
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _weakest(severities) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:227-227
  In source order: Retain source documentation literal source_literal_227_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:228-228
  End this invocation with max(severities, key=lambda s: SEV_RANK[s]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:231-240
// Source signature: _model_or_derived_chain_severity(raw_severity: str, hop_sevs: list[Severity]) -> tuple[Severity, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _model_or_derived_chain_severity(raw_severity, hop_sevs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:233-236
  In source order: Retain source documentation literal source_literal_233_4; it is not a model call. Then Evaluate once _coerce_sev_or_none(raw_severity); assign in source target order to parsed.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:237-238
  if (the source predicate parsed is not None is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:238-238
    End this invocation with (parsed, False).
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:239-239
  In source order: Evaluate COUNTERS.bump('s8_chain_severity_derived'); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:240-240
  End this invocation with (_weakest(hop_sevs), True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:244-257
In source order: Evaluate once '_Severity aligned to the highest-severity finding in this path._'; assign in source target order to _LIFT_NOTE. Then Evaluate once source_literal_247_19; assign in source target order to _CAP_ANNOTATION. Then Evaluate once '(?:/|[\\-–—]|\\.\\.)'; assign in source target order to _PROSE_ID_JOIN. Then Evaluate once re.compile(source_template_256_4); assign in source target order to _PROSE_ID_RX. Then Evaluate once re.compile(source_template_257_32); assign in source target order to _PROSE_ID_SPLIT_RX.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:259-264
In source order: Evaluate once re.compile('(`+[^`]*`+)'); assign in source target order to _CODE_SPAN_RX. Then Evaluate once source_literal_262_18; assign in source target order to _PROSE_ID_NOTE.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:267-300
// Source signature: _remap_prose_ids(text: str, display: dict[str, str]) -> tuple[str, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remap_prose_ids(text, display) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:268-268
  In source order: Retain source documentation literal source_literal_268_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:269-270
  if (the source predicate not text is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:270-270
    End this invocation with (text, []).
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:271-271
  In source order: For unresolved, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:273-294
  // Source signature: _one(match: re.Match) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _one(match) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:274-279
    In source order: Retain source documentation literal source_literal_274_8; it is not a model call. Then Evaluate once match.group(0); assign in source target order to token. Then Evaluate once _PROSE_ID_SPLIT_RX.split(token); assign in source target order to parts. Then Evaluate once (parts[0::2], parts[1::2]); assign in source target order to (ids, joins). Then Evaluate once [i for i in ids if display.get(i) is None]; assign in source target order to missing.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:280-282
    if (the source predicate missing is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:281-281
      In source order: Evaluate unresolved.extend(missing); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:282-282
      End this invocation with token.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:283-283
    In source order: Evaluate once [int(i[1:]) for i in ids]; assign in source target order to nums.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:284-292
    if (the source predicate len(ids) == 2 and joins[0] != '/' and (nums[0] < nums[1]) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:287-288
      In source order: Evaluate once [source_template_287_23 for n in range(nums[0], nums[1] + 1)]; assign in source target order to members. Then Evaluate once [i for i in members if display.get(i) is None]; assign in source target order to gaps.
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:289-291
      if (the source predicate gaps is truthy) {
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:290-290
        In source order: Evaluate unresolved.extend(gaps); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:291-291
        End this invocation with token.
      }
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:292-292
      End this invocation with '/'.join((display[i] for i in members)).
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:294-294
    End this invocation with ''.join((display[p] if k % 2 == 0 else p for k, p in enumerate(parts))).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:297-297
  In source order: Evaluate once _CODE_SPAN_RX.split(text); assign in source target order to parts.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:298-299
  for each i in range(0, len(parts), 2) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:299-299
    In source order: Evaluate once _PROSE_ID_RX.sub(_one, parts[i]); assign in source target order to parts[i].
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:300-300
  End this invocation with (''.join(parts), list(dict.fromkeys(unresolved))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:304-308
In source order: Evaluate once ((re.compile('\\b(the )chains (?:array|list)\\b', re.IGNORECASE), '\\1chain list'), (re.compile('\\branked_findings\\b'), 'ranking'), (re.compile('\\blink_evidence\\b'), 'link evidence')); assign in source target order to _SUMMARY_WORDING.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:311-319
// Source signature: _reword_schema_terms(text: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reword_schema_terms(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:312-312
  In source order: Retain source documentation literal source_literal_312_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:313-314
  if (the source predicate not text is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:314-314
    End this invocation with text.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:315-315
  In source order: Evaluate once _CODE_SPAN_RX.split(text); assign in source target order to parts.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:316-318
  for each i in range(0, len(parts), 2) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:317-318
    for each (rx, repl) in _SUMMARY_WORDING {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:318-318
      In source order: Evaluate once rx.sub(repl, parts[i]); assign in source target order to parts[i].
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:319-319
  End this invocation with ''.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:322-330
interface _ChainProse {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:323-327
  In source order: Retain source documentation literal source_literal_323_4; it is not a model call. Then For title, declare without assigning a value; source annotation str. Then For narrative, declare without assigning a value; source annotation str. Then For reachability, declare without assigning a value; source annotation str. Then For blocked, declare without assigning a value; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:328-330
  In source order: For preconditions, declare without assigning a value; source annotation list[str]. Then For mechanisms, declare without assigning a value; source annotation list[str]. Then For missed, declare without assigning a value; source annotation list[str].
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:333-353
// Source signature: _remap_item_prose(item: ChainEntry, narrative: str, display: dict[str, str]) -> _ChainProse
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remap_item_prose(item, narrative, display) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:335-336
  In source order: Retain source documentation literal source_literal_335_4; it is not a model call. Then For missed, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:338-341
  // Source signature: _one(text: str) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _one(text) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:339-340
    In source order: Evaluate once _remap_prose_ids(text, display); assign in source target order to (out, gone). Then Evaluate missed.extend(gone); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:341-341
    End this invocation with out.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:343-349
  In source order: Evaluate once _one(item.title); assign in source target order to title. Then Evaluate once _one(narrative); assign in source target order to narrative. Then Evaluate once _one(item.entry_reachability.strip()); assign in source target order to reachability. Then Evaluate once [_one(v) for v in _validate.clean_controls(item.blocked_by_controls)]; assign in source target order to blocked. Then Evaluate once [_one(v) for v in _validate.clean_preconditions(item)]; assign in source target order to preconditions.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:351-351
  In source order: Evaluate once [_one(ln.mechanism.strip()) for ln in item.link_evidence]; assign in source target order to mechanisms.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:352-353
  End this invocation with _ChainProse(title, narrative, reachability, blocked, preconditions, mechanisms, list(dict.fromkeys(missed))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:356-358
// Source signature: sev_from_band(rating: str | None) -> Severity | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn sev_from_band(rating) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:357-357
  In source order: Retain source documentation literal source_literal_357_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:358-358
  End this invocation with CVSS_BAND_TO_SEV.get((rating or '').strip().lower()).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:361-365
// Source signature: final_severity(finding, llm_label: Severity) -> Severity
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn final_severity(finding, llm_label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:362-362
  In source order: Retain source documentation literal source_literal_362_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:363-365
  End this invocation with sev_from_band(getattr(finding, 'vsvs_rating', None)) or sev_from_band(getattr(finding, 'cvss_rating', None)) or llm_label.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:368-370
In source order: Evaluate once source_literal_368_22; assign in source target order to _SEV_MISMATCH_NOTE.
// Source: vvaharness/pipeline/stages/s8/outcomes.py:373-378
// Source signature: severity_prose_mismatch(model_label: Severity, shipped: Severity) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn severity_prose_mismatch(model_label, shipped) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:374-374
  In source order: Retain source documentation literal source_literal_374_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:375-376
  if (the source predicate model_label is shipped is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:376-376
    End this invocation with ''.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:377-378
  End this invocation with _SEV_MISMATCH_NOTE.format(model=model_label.value, shipped=shipped.value).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:381-386
// Source signature: ranked_finding(finding, severity: Severity, notes: str) -> RankedFinding
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn ranked_finding(finding, severity, notes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:382-384
  In source order: Retain source documentation literal source_literal_382_4; it is not a model call. Then Evaluate once severity; assign in source target order to finding.severity. Then Evaluate once notes; assign in source target order to finding.exploitability_notes.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:385-386
  End this invocation with RankedFinding(finding=finding, severity=severity, exploitability_notes=notes).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:389-392
// Source signature: offensive_rank(finding) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn offensive_rank(finding) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:390-391
  In source order: Retain source documentation literal source_literal_390_4; it is not a model call. Then Evaluate once (getattr(finding, 'offensive_priority', None) or '').strip().upper(); assign in source target order to op.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:392-392
  End this invocation with int(op[1]) if len(op) == 2 and op[0] == 'P' and op[1].isdigit() else 9.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:395-399
// Source signature: severity_sort_order(ranked: list[RankedFinding]) -> list[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn severity_sort_order(ranked) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:396-396
  In source order: Retain source documentation literal source_literal_396_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:397-399
  End this invocation with sorted(range(len(ranked)), key=lambda k: (SEV_RANK[ranked[k].severity], offensive_rank(ranked[k].finding))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:402-421
// Source signature: _coerce_sev_or_none(s) -> Severity | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _coerce_sev_or_none(s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:403-403
  In source order: Retain source documentation literal source_literal_403_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:404-405
  if (the source predicate not s is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:405-405
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:406-406
  In source order: Evaluate once str(s).strip().lower(); assign in source target order to key.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:407-410
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:408-408
    End this invocation with Severity(key).
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:409-410
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:410-410
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:412-413
  if (the source predicate not isinstance(s, str) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:413-413
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:414-414
  In source order: Evaluate once key.split('/', 1)[0].strip(); assign in source target order to token.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:415-418
  Perform the following protected operations {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:416-416
    In source order: Evaluate once float(token); assign in source target order to score.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:417-418
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:418-418
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:419-420
  if (the source predicate not math.isfinite(score) or not 0.0 <= score <= 10.0 is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:420-420
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:421-421
  End this invocation with sev_from_band(_cvss.rating(score)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:424-425
// Source signature: coerce_sev(s) -> Severity
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn coerce_sev(s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:425-425
  End this invocation with _coerce_sev_or_none(s) or Severity.INFO.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:428-441
// Source signature: _sort_and_remap(ranked: list[RankedFinding], ranked_orig_idx: list[int], dropped) -> tuple[list[RankedFinding], dict[int, int], list]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sort_and_remap(ranked, ranked_orig_idx, dropped) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:430-434
  In source order: Retain source documentation literal source_literal_430_4; it is not a model call. Then Evaluate once severity_sort_order(ranked); assign in source target order to order. Then Evaluate once [ranked[k] for k in order]; assign in source target order to ranked. Then Evaluate once [ranked_orig_idx[k] for k in order]; assign in source target order to orig_sorted. Then Evaluate once {orig: new_i for new_i, orig in enumerate(orig_sorted)}; assign in source target order to orig_to_sorted.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:435-440
  In source order: Evaluate once [d.model_copy(update={'canonical_idx': orig_to_sorted[d.canonical_idx]}) if d.reason == 'DUPLICATE' and d.canonical_idx in orig_to_sorted else d for d in dropped]; assign in source target order to dropped_out.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:441-441
  End this invocation with (ranked, orig_to_sorted, dropped_out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:444-453
// Source signature: templated_summary(ranked: list[RankedFinding]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn templated_summary(ranked) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:445-445
  In source order: Retain source documentation literal source_literal_445_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:446-447
  if (the source predicate not ranked is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:447-447
    End this invocation with 'No verified findings.'.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:448-448
  In source order: For counts, assign {}; source annotation dict[Severity, int].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:449-450
  for each r in ranked {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:450-450
    In source order: Evaluate once counts.get(r.severity, 0) + 1; assign in source target order to counts[r.severity].
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:451-452
  In source order: Evaluate once ', '.join((source_template_451_22 for s in SEV_RANK if counts.get(s))); assign in source target order to bands.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:453-453
  End this invocation with source_template_453_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:456-483
// Source signature: deterministic_report(ctx, findings, dropped, raw_findings_count, metrics, *, enrichment_failure: str) -> FinalReport
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn deterministic_report(ctx, findings, dropped, raw_findings_count, metrics, enrichment_failure) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:458-458
  In source order: Retain source documentation literal source_literal_458_4; it is not a model call.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:460-462
  for each f in findings {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:462-462
    In source order: Evaluate once ''; assign in source target order to f.severity_prose_mismatch.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:464-469
  In source order: Evaluate once [ranked_finding(f, final_severity(f, f.severity), '(enrichment unavailable — severity from CVSS or the detection label)') for f in findings]; assign in source target order to ranked. Then Evaluate once _sort_and_remap(ranked, list(range(len(findings))), dropped); assign in source target order to (ranked, _, dropped_out).
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:470-483
  End this invocation with FinalReport(repo_root=ctx.repo_root, findings=ranked, chains=[], dropped=dropped_out, raw_findings_count=raw_findings_count, metrics=metrics, summary=templated_summary(ranked), degraded=True, enrichment_unavailable=True, degraded_reason=source_template_481_25).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:486-495
// Source signature: _positionally_filled(item: ChainEntry) -> list[LinkEvidence]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _positionally_filled(item) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:487-489
  In source order: Retain source documentation literal source_literal_487_4; it is not a model call. Then Evaluate once item.link_evidence; assign in source target order to links.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:490-492
  if (the source predicate not links or len(links) != len(item.steps) - 1 or any((ln.from_id.strip() or ln.to_id.strip() for ln in links)) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:492-492
    End this invocation with links.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:493-493
  In source order: Evaluate COUNTERS.bump('s8_chain_links_positionally_filled'); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:494-495
  End this invocation with [ln.model_copy(update={'from_id': item.steps[k], 'to_id': item.steps[k + 1]}) for k, ln in enumerate(links)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:498-648
// Source signature: _build_chain(item: ChainEntry, *, ranked: list[RankedFinding], index_of: dict[str, int], orig_to_sorted: dict[int, int], prose_ids: dict[str, str], repo_root, window: set[int] | None, gate_on: bool, checks_on: bool) -> Chain | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_chain(item, ranked, index_of, orig_to_sorted, prose_ids, repo_root, window, gate_on, checks_on) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:503-505
  In source order: Retain source documentation literal source_literal_503_4; it is not a model call. Then Evaluate once _validate.annotate_hedges(item.narrative); assign in source target order to (narrative, hedged).
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:508-512
  if (the source predicate len(item.link_evidence) == len(item.steps) >= 2 and all((not ln.from_id.strip() and (not ln.to_id.strip()) for ln in item.link_evidence)) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:511-512
    In source order: Evaluate once item.model_copy(update={'link_evidence': item.link_evidence[1:]}); assign in source target order to item. Then Evaluate COUNTERS.bump('s8_chain_links_origin_dropped'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:514-523
  In source order: Evaluate once _remap_item_prose(item, narrative, prose_ids); assign in source target order to prose. Then Evaluate once prose.narrative; assign in source target order to narrative. Then Evaluate once [index_of[s.strip()] for s in item.steps if s.strip() in index_of and (window is None or index_of[s.strip()] in window)]; assign in source target order to steps. Then Evaluate once [s for s in item.steps if s.strip() not in index_of or (window is not None and index_of[s.strip()] not in window)]; assign in source target order to unknown.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:524-525
  if (the source predicate unknown is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:525-525
    In source order: Evaluate COUNTERS.bump('s8_chain_step_id_unknown', len(unknown)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:526-528
  In source order: Evaluate once [orig_to_sorted[s] for s in steps if s in orig_to_sorted]; assign in source target order to named. Then Evaluate once _validate.collapse_same_location(named, ranked); assign in source target order to (remapped, dupes).
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:529-530
  if (the source predicate dupes is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:530-530
    In source order: Evaluate COUNTERS.bump('s8_chain_hop_same_location', dupes); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:531-535
  if (the source predicate len(remapped) < 2 is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:533-534
    In source order: Evaluate COUNTERS.bump('s8_chain_dropped_unresolved_steps' if unknown or not dupes else 's8_chain_dropped_same_location'); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:535-535
    End this invocation with None.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:537-546
  if (the source predicate unknown is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:538-546
    In source order: Evaluate once unknown[:20]; assign in source target order to shown. Then Evaluate once '' if len(unknown) <= 20 else source_template_539_46; assign in source target order to extra. Then Evaluate once "outside this pass's view (not in the verified set, or not sent to the windowed enrichment call)" if window is not None else 'not in the verified set'; assign in source target order to why. Then Evaluate once source_template_544_21.strip(); assign in source target order to narrative.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:550-554
  In source order: Evaluate once _positionally_filled(item); assign in source target order to filled. Then Evaluate once set(itertools.pairwise(remapped)); assign in source target order to path_hops. Then Evaluate once {_validate.location_key(ranked, s): s for s in remapped}; assign in source target order to survivor. Then Evaluate once {s: survivor[_validate.location_key(ranked, s)] for s in named}; assign in source target order to alias. Then For links, assign []; source annotation list[LinkEvidence].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:555-565
  for each (ln, mech) in zip(filled, prose.mechanisms) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:556-557
    In source order: Evaluate once alias.get(orig_to_sorted.get(index_of.get(ln.from_id.strip(), -1))); assign in source target order to src. Then Evaluate once alias.get(orig_to_sorted.get(index_of.get(ln.to_id.strip(), -1))); assign in source target order to dst.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:558-565
    if (the source predicate (src, dst) in path_hops is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:560-565
      In source order: Evaluate once _validate.resolved_citation(repo_root, ln.file, ln.line); assign in source target order to (_, cfile, cline). Then Evaluate links.append(LinkEvidence(from_id=source_template_563_24, to_id=source_template_563_45, mechanism=mech, file=cfile, line=cline)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:567-568
  if (the source predicate len(filled) > len(links) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:568-568
    In source order: Evaluate COUNTERS.bump('s8_chain_links_unplaced', len(filled) - len(links)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:572-578
  In source order: Evaluate once _validate.link_ok(links, remapped, repo_root); assign in source target order to (links_ok, resolved_links, hops). Then Evaluate once _validate.hardening_steps(remapped, ranked); assign in source target order to hardening. Then For quality_notes, assign []; source annotation list[str]. Then For disclosures, assign []; source annotation list[str].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:579-583
  if (the source predicate checks_on is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:580-583
    In source order: Evaluate quality_notes.extend(_validate.quality_annotations(item.model_copy(update={'link_evidence': links}), remapped, ranked, repo_root, links_ok=links_ok, resolved=resolved_links, hops=hops, hardening=hardening)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:585-586
  In source order: Evaluate once [t for t in prose.missed if t not in {s.strip() for s in unknown}]; assign in source target order to prose_missed.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:587-589
  if (the source predicate prose_missed is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:588-589
    In source order: Evaluate COUNTERS.bump('s8_chain_prose_id_unresolved', len(prose_missed)); retain side effects and discard the expression result. Then Evaluate quality_notes.append(_PROSE_ID_NOTE.format(ids=prose_missed[:20])); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:592-600
  In source order: Evaluate once bool(prose.blocked or prose.preconditions); assign in source target order to explained. Then Evaluate once [ranked[st].severity for st in remapped]; assign in source target order to hop_sevs. Then Evaluate once _model_or_derived_chain_severity(item.severity, hop_sevs); assign in source target order to (model_sev, derived). Then Evaluate once model_sev; assign in source target order to severity. Then Evaluate once [b for st in remapped if (b := (sev_from_band(ranked[st].finding.vsvs_rating) or sev_from_band(ranked[st].finding.cvss_rating)))]; assign in source target order to hop_bands.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:601-607
  In source order: Evaluate once _strongest(hop_bands) if hop_bands else None; assign in source target order to floor. Then Evaluate once _strongest(hop_sevs); assign in source target order to effective. Then Evaluate once not gate_on or _validate.lift_allowed(links_ok, hardening, hedged); assign in source target order to allowed. Then Evaluate once ''; assign in source target order to decision.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:610-629
  if (the source predicate floor is not None and SEV_RANK[model_sev] > SEV_RANK[floor] and (derived or not explained) is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:612-619
    if (the source predicate allowed is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:613-615
      In source order: Evaluate once floor; assign in source target order to severity. Then Evaluate COUNTERS.bump('s8_chain_severity_lifted'); retain side effects and discard the expression result. Then Evaluate once source_template_615_24.strip(); assign in source target order to narrative.
    }
    else {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:618-619
      In source order: Evaluate COUNTERS.bump('s8_chain_lift_suppressed'); retain side effects and discard the expression result. Then Evaluate once 'lift_withheld'; assign in source target order to decision.
    }
  }
  else {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:620-629
    if (the source predicate SEV_RANK[severity] > SEV_RANK[effective] and (not explained) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:622-622
      In source order: Evaluate COUNTERS.bump('s8_chain_severity_under_hops'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:623-629
      if (the source predicate SEV_RANK[model_sev] < SEV_RANK[effective] is truthy) {
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:624-624
        In source order: Evaluate COUNTERS.bump('s8_chain_severity_raised'); retain side effects and discard the expression result.
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:625-629
        if (the source predicate not allowed is truthy) {
          // Source: vvaharness/pipeline/stages/s8/outcomes.py:627-629
          In source order: Evaluate once effective; assign in source target order to severity. Then Evaluate COUNTERS.bump('s8_chain_severity_capped'); retain side effects and discard the expression result. Then Evaluate once 'self_raise_capped'; assign in source target order to decision.
        }
      }
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:631-632
  if (the source predicate decision is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:632-632
    In source order: Evaluate disclosures.append(_CAP_ANNOTATION); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:634-648
  End this invocation with Chain(title=prose.title or 'Unnamed chain', steps=remapped, severity=severity, blocked_by_controls=prose.blocked, preconditions=prose.preconditions, link_evidence=links, entry_reachability=prose.reachability, quality_notes=quality_notes, disclosures=disclosures, severity_decision=decision, link_coverage=source_template_646_22 if checks_on else '', narrative=narrative).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/pipeline/stages/s8/outcomes.py:651-787
// Source signature: hydrate_report(data: ChainReport, ctx, findings, dropped, raw_findings_count, metrics, *, window: set[int] | None=None, cfg=None) -> tuple[FinalReport, set[int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn hydrate_report(data, ctx, findings, dropped, raw_findings_count, metrics, window, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:655-660
  In source order: Retain source documentation literal source_literal_655_4; it is not a model call. Then Evaluate once finding_ids(findings); assign in source target order to index_of. Then For ranked, assign []; source annotation list[RankedFinding]. Then For ranked_orig_idx, assign []; source annotation list[int]. Then For covered, assign set(); source annotation set[int].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:661-661
  In source order: For claims, assign set(); source annotation set[tuple[int, int]].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:662-692
  for each item in data.ranked_findings {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:663-663
    In source order: Evaluate once index_of.get(item.finding_id.strip()); assign in source target order to idx.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:664-666
    if (the source predicate window is not None and idx is not None and (idx not in window) is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:666-666
      In source order: Evaluate once None; assign in source target order to idx.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:667-670
    if (the source predicate idx is None or idx in covered is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:668-669
      In source order: Evaluate COUNTERS.bump('s8_ranked_finding_id_unknown' if idx is None else 's8_ranked_finding_id_repeated'); retain side effects and discard the expression result.
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:670-670
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:671-671
    In source order: Evaluate covered.add(idx); retain side effects and discard the expression result.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:672-678
    for each token in item.feeds {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:673-673
      In source order: Evaluate once index_of.get(token.strip()); assign in source target order to t.
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:674-678
      if (the source predicate t is None or (window is not None and t not in window) is truthy) {
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:676-676
        In source order: Evaluate COUNTERS.bump('s8_chain_feeds_id_unknown'); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/pipeline/stages/s8/outcomes.py:677-678
        if (the source predicate t != idx is truthy) {
          // Source: vvaharness/pipeline/stages/s8/outcomes.py:678-678
          In source order: Evaluate claims.add((idx, t)); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:679-692
    In source order: Evaluate once _coerce_sev_or_none(item.severity); assign in source target order to parsed_sev. Then Evaluate once final_severity(findings[idx], parsed_sev or findings[idx].severity); assign in source target order to shipped_sev. Then Evaluate once severity_prose_mismatch(parsed_sev, shipped_sev) if parsed_sev is not None else ''; assign in source target order to findings[idx].severity_prose_mismatch. Then Evaluate ranked.append(ranked_finding(findings[idx], shipped_sev, item.exploitability_notes)); retain side effects and discard the expression result. Then Evaluate ranked_orig_idx.append(idx); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:694-702
  for each (i, f) in enumerate(findings) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:695-702
    if (the source predicate i not in covered is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:696-702
      In source order: Evaluate once NOT_RANKED_NOTE if window is None or i in window else '(not sent to the enrichment pass — report windowed)'; assign in source target order to note. Then Evaluate ranked.append(ranked_finding(f, final_severity(f, f.severity), note)); retain side effects and discard the expression result. Then Evaluate ranked_orig_idx.append(i); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:704-714
  In source order: Evaluate once _sort_and_remap(ranked, ranked_orig_idx, dropped); assign in source target order to (ranked, orig_to_sorted, dropped_out). Then Evaluate once knob(cfg, 'step8.severity_lift_gate', True); assign in source target order to gate_on. Then Evaluate once knob(cfg, 'step8.chain_quality_checks', True); assign in source target order to checks_on. Then Evaluate once knob(cfg, 'step8.chain_dedup', True); assign in source target order to dedup_on. Then Evaluate once {token: source_template_713_24 for token, i in index_of.items() if i in orig_to_sorted}; assign in source target order to prose_ids.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:716-721
  for each rf in ranked {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:717-719
    In source order: Evaluate once _remap_prose_ids(rf.exploitability_notes, prose_ids); assign in source target order to (remapped, notes_missed). Then Evaluate once remapped; assign in source target order to rf.exploitability_notes. Then Evaluate once remapped; assign in source target order to rf.finding.exploitability_notes.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:720-721
    if (the source predicate notes_missed is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:721-721
      In source order: Evaluate COUNTERS.bump('s8_chain_prose_id_unresolved', len(notes_missed)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:723-723
  In source order: Evaluate once _remap_prose_ids(data.summary, prose_ids); assign in source target order to (summary, summary_missed).
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:724-725
  if (the source predicate summary_missed is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:725-725
    In source order: Evaluate COUNTERS.bump('s8_chain_prose_id_unresolved', len(summary_missed)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:726-729
  In source order: Evaluate once _reword_schema_terms(summary); assign in source target order to summary. Then For chains, assign []; source annotation list[Chain]. Then Evaluate once 0; assign in source target order to chains_dropped.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:730-739
  for each item in data.chains {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:731-735
    In source order: Evaluate once _build_chain(item, ranked=ranked, index_of=index_of, orig_to_sorted=orig_to_sorted, prose_ids=prose_ids, repo_root=ctx.repo_root, window=window, gate_on=gate_on, checks_on=checks_on); assign in source target order to chain.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:736-739
    if (the source predicate chain is None is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:737-737
      In source order: Apply source augmented assignment chains_dropped += 1 with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:739-739
      In source order: Evaluate chains.append(chain); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:741-742
  if (the source predicate chains_dropped is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:742-742
    In source order: Evaluate COUNTERS.bump('s8_chain_dropped', chains_dropped); retain side effects and discard the expression result.
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:746-746
  In source order: For unpromoted, assign []; source annotation list[tuple[int, int]].
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:747-751
  if (the source predicate checks_on is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:748-749
    In source order: Evaluate once _validate.unpromoted_links(sorted(((orig_to_sorted[o], orig_to_sorted[t]) for o, t in claims)), chains, ranked); assign in source target order to unpromoted.
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:750-751
    if (the source predicate unpromoted is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:751-751
      In source order: Evaluate COUNTERS.bump('s8_chain_link_unpromoted', len(unpromoted)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:753-753
  In source order: Evaluate once 0; assign in source target order to chains_deduped.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:754-769
  if (the source predicate dedup_on is truthy) {
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:755-755
    In source order: Evaluate once _validate.dedup_chains(chains); assign in source target order to (chains, chains_deduped, pairs).
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:756-757
    if (the source predicate chains_deduped is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:757-757
      In source order: Evaluate COUNTERS.bump('s8_chain_deduped', chains_deduped); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:758-760
    if (the source predicate pairs is truthy) {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:760-760
      In source order: Evaluate COUNTERS.bump('s8_chain_near_duplicate', len(pairs)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:762-762
    In source order: For siblings, assign {}; source annotation dict[int, int].
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:763-765
    for each (a, b) in pairs {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:764-765
      In source order: Evaluate once siblings.get(a, 0) + 1; assign in source target order to siblings[a]. Then Evaluate once siblings.get(b, 0) + 1; assign in source target order to siblings[b].
    }
    // Source: vvaharness/pipeline/stages/s8/outcomes.py:766-769
    for each (i, n) in siblings.items() {
      // Source: vvaharness/pipeline/stages/s8/outcomes.py:768-769
      In source order: Evaluate chains[i].disclosures.append(_validate.NEAR_DUPLICATE_NOTE.format(n=chains[i].steps[-1] + 1, others=n)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:772-772
  In source order: Evaluate chains.sort(key=lambda c: (SEV_RANK[c.severity], bool(c.blocked_by_controls))); retain side effects and discard the expression result.
  // Source: vvaharness/pipeline/stages/s8/outcomes.py:774-787
  End this invocation with (FinalReport(repo_root=ctx.repo_root, findings=ranked, chains=chains, chains_dropped=chains_dropped, chains_deduped=chains_deduped, chains_invalid=data.chains_invalid, unpromoted_links=unpromoted, dropped=dropped_out, raw_findings_count=raw_findings_count, metrics=metrics, summary=summary), covered).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models import Chain, FinalReport, Finding, LinkEvidence, RankedFinding, Severity` at source line 27: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.scan._coerce import text as _coerce_text` at source line 35: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.models.scan.findings import NOT_RANKED_NOTE` at source line 36: `source_detail/vvaharness/models/scan/findings.py.sudo.md`.
- `from vvaharness.models.vocab import SEV_RANK` at source line 37: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8 import validate as _validate` at source line 38: `source_detail/vvaharness/pipeline/stages/s8/__init__.py.sudo.md`.
- `from vvaharness.pipeline.stages.s8 import validate as _validate` at source line 38: `source_detail/vvaharness/pipeline/stages/s8/validate.py.sudo.md`.
- `from vvaharness.report import cvss as _cvss` at source line 39: `source_detail/vvaharness/report/__init__.py.sudo.md`.
- `from vvaharness.report import cvss as _cvss` at source line 39: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.util.config import knob` at source line 40: `source_detail/vvaharness/util/config.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 41: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.json_extract import extract_json` at source line 42: `source_detail/vvaharness/util/json_extract.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vvaharness/pipeline/stages/s8/outcomes.py.sudo.md). Exact strings in the evidence asset support this conversion.
