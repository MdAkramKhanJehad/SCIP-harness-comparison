# vvaharness/report/redact.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/report/redact.py.evidence.json`. SHA-256: `731dfcd703115dde170476014134a7ef59220b5f55af9200103accb1abcdf784`.

```sudo
// Source: vvaharness/report/redact.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections import OrderedDict; preserve alias and import-time effects.
// Source: vvaharness/report/redact.py:21-24
In source order: Resolve source import from typing import Callable, TypeVar; preserve alias and import-time effects. Then Evaluate once TypeVar('_TreeT'); assign in source target order to _TreeT.
// Source: vvaharness/report/redact.py:28-38
// Source signature: _luhn(digits: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _luhn(digits) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:29-29
  In source order: Evaluate once (0, True); assign in source target order to (total, odd).
  // Source: vvaharness/report/redact.py:30-37
  for each ch in reversed(digits) {
    // Source: vvaharness/report/redact.py:31-31
    In source order: Evaluate once int(ch); assign in source target order to n.
    // Source: vvaharness/report/redact.py:32-35
    if (the source predicate not odd is truthy) {
      // Source: vvaharness/report/redact.py:33-33
      In source order: Apply source augmented assignment n *= 2 with source evaluation/in-place semantics.
      // Source: vvaharness/report/redact.py:34-35
      if (the source predicate n > 9 is truthy) {
        // Source: vvaharness/report/redact.py:35-35
        In source order: Apply source augmented assignment n -= 9 with source evaluation/in-place semantics.
      }
    }
    // Source: vvaharness/report/redact.py:36-37
    In source order: Apply source augmented assignment total += n with source evaluation/in-place semantics. Then Evaluate once not odd; assign in source target order to odd.
  }
  // Source: vvaharness/report/redact.py:38-38
  End this invocation with total % 10 == 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:41-41
In source order: Evaluate once (12, 19); assign in source target order to (_PAN_MIN_DIGITS, _PAN_MAX_DIGITS).
// Source: vvaharness/report/redact.py:44-46
// Source signature: _iin(lo: int, hi: int) -> frozenset[int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _iin(lo, hi) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:45-45
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call.
  // Source: vvaharness/report/redact.py:46-46
  End this invocation with frozenset(range(lo, hi + 1)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:49-64
In source order: For _CARD_NETWORKS, assign (('amex', 15, 15, 2, _iin(34, 34) | _iin(37, 37)), ('visa', 13, 19, 1, _iin(4, 4)), ('mastercard', 16, 16, 2, _iin(51, 55)), ('mastercard-2-series', 16, 16, 4, _iin(2221, 2720)), ('discover-6011', 16, 19, 4, _iin(6011, 6011)), ('discover-65', 16, 19, 2, _iin(65, 65)), ('discover-64x', 16, 19, 3, _iin(644, 649)), ('jcb', 16, 19, 4, _iin(3528, 3589)), ('unionpay', 16, 19, 2, _iin(62, 62)), ('diners', 14, 19, 2, _iin(36, 36)), ('maestro', 12, 19, 4, frozenset({5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763})), ('rupay-508', 16, 16, 3, _iin(508, 508)), ('rupay-8x', 16, 16, 2, _iin(81, 82))); source annotation tuple[tuple[str, int, int, int, frozenset[int]], ...].
// Source: vvaharness/report/redact.py:67-73
// Source signature: _cc_network(digits: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cc_network(digits) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:68-69
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call. Then Evaluate once len(digits); assign in source target order to n.
  // Source: vvaharness/report/redact.py:70-71
  if (the source predicate n < _PAN_MIN_DIGITS or n > _PAN_MAX_DIGITS is truthy) {
    // Source: vvaharness/report/redact.py:71-71
    End this invocation with False.
  }
  // Source: vvaharness/report/redact.py:72-73
  End this invocation with any((lo <= n <= hi and int(digits[:width]) in prefixes for _, lo, hi, width, prefixes in _CARD_NETWORKS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:76-76
In source order: Evaluate once 666; assign in source target order to _SSN_NEVER_ISSUED_AREA.
// Source: vvaharness/report/redact.py:79-82
// Source signature: _ssn_valid(d: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ssn_valid(d) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:80-81
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call. Then Evaluate once (int(d[:3]), int(d[3:5]), int(d[5:9])); assign in source target order to (area, group, serial).
  // Source: vvaharness/report/redact.py:82-82
  End this invocation with not (area == 0 or area == _SSN_NEVER_ISSUED_AREA or group == 0 or (serial == 0)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:85-87
// Source signature: _bearer_credential(m: re.Match) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bearer_credential(m) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:86-86
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call.
  // Source: vvaharness/report/redact.py:87-87
  End this invocation with any((not c.isalpha() for c in m.group('bv'))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:89-104
In source order: Evaluate once re.compile('^\\(|^[A-Za-z_]\\w*\\(|^[A-Za-z_]\\w*\\.\\w'); assign in source target order to _SECRET_CODE_SHAPE. Then Evaluate once re.compile('^[A-Za-z_]\\w*\\.\\w+\\('); assign in source target order to _SECRET_CODE_SHAPE_DOTTED_CALL. Then Evaluate once re.compile('[A-Za-z]+(?:_[A-Za-z]+)+'); assign in source target order to _IDENTIFIER_SHAPE. Then Evaluate once re.compile('[A-Z][A-Z0-9_]*=(?!=)'); assign in source target order to _NEXT_LINE_ENV_KEY. Then Evaluate once '\\[redacted-[a-z0-9-]+]'; assign in source target order to _REDACTED_TAG_FRAGMENT.
// Source: vvaharness/report/redact.py:105-247
In source order: Evaluate once re.compile('(?i)' + _REDACTED_TAG_FRAGMENT); assign in source target order to _REDACTED_TAG_RX. Then Evaluate once re.compile('(?i)\\$\\{?[A-Z0-9_.]+}?|%[A-Z0-9_]+%|<[^>]+>|\\*{3,}|x{3,}|\\[?redacted]?|' + _REDACTED_TAG_FRAGMENT + '|null|none|true|false|changeme|your[_-]?\\w+|placeholder|example'); assign in source target order to _PLACEHOLDER_RX. Then Evaluate once '[A-Za-z0-9_-]'; assign in source target order to _b64u. Then For _PATTERNS, assign [('PAN', re.compile('(?<![0-9A-Za-z])(?:\\d[\\s\\-]?){12,18}\\d(?![0-9A-Za-z])'), lambda m: (lambda d: _cc_network(d) and _luhn(d))(re.sub('\\D', '', m.group(0)))), ('CVV', re.compile('(?i)\\b(cvv2?|cvc2?|cid|csc)\\b\\s*[:=]?\\s*\\"?(\\d{3,4})\\"?'), None), ('TRACK', re.compile('%B\\d{12,19}\\^[^?]{2,90}\\?'), None), ('SSN', re.compile('(?<!\\d)(\\d{3})[-.\\t \\u00a0\\u2009\\u202f\\u2007](\\d{2})[-.\\t \\u00a0\\u2009\\u202f\\u2007](\\d{4})(?!\\d)'), lambda m: _ssn_valid(m.group(1) + m.group(2) + m.group(3))), ('SSN-CTX', re.compile(source_literal_142_9), lambda m: _ssn_valid(m.group(2))), ('AWS-KEY', re.compile('\\b(?:AKIA|ASIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA)[0-9A-Z]{16}\\b'), None), ('GITHUB-TOKEN', re.compile('\\b(?:gh[pousr]_[A-Za-z0-9]{36,255}|github_pat_[A-Za-z0-9_]{22}_[A-Za-z0-9]{59})\\b'), None), ('SLACK-TOKEN', re.compile('\\bxox[baprs]-[A-Za-z0-9-]{10,72}\\b'), None), ('ANTHROPIC-KEY', re.compile('\\bsk-ant-[A-Za-z0-9_-]{16,}\\b'), None), ('STRIPE-KEY', re.compile('\\b(?:sk|rk)_(?:live|test)_[A-Za-z0-9]{24,99}\\b'), None), ('GOOGLE-API-KEY', re.compile('\\bAIza[0-9A-Za-z_-]{35}\\b'), None), ('AZURE-SAS', re.compile('(?i)\\bsig=[0-9A-Za-z%+/=]{20,}\\b'), None), ('TWILIO-KEY', re.compile('\\bSK[0-9a-fA-F]{32}\\b'), None), ('JWT', re.compile('\\beyJ' + _b64u + '{10,}\\.' + _b64u + '{10,}\\.' + _b64u + '{10,}\\b'), None), ('BEARER', re.compile('(?i)\\b(?:Bearer|Basic)\\s+(?P<bv>[A-Za-z0-9+/=._-]{8,})\\b'), _bearer_credential), ('URL-CRED', re.compile('(?i)\\b([a-z][a-z0-9+.\\-]*://[^\\s:/@]+:)([^\\s/@]{1,256})@'), None), ('PRIVATE-KEY', re.compile('-{5}BEGIN [A-Z ]*PRIVATE KEY-{5}[\\s\\S]*?-{5}END [A-Z ]*PRIVATE KEY-{5}'), None), ('SECRET', re.compile(source_literal_194_9), lambda m: not _PLACEHOLDER_RX.fullmatch(m.group('v')) and (m.group('op') in (':', '=') or bool(m.group('q'))) and (not (m.group('v') or '').startswith('<'))), ('SECRET-XML', re.compile(source_literal_232_16), lambda m: not _PLACEHOLDER_RX.fullmatch(m.group('v'))), ('SECRET-ARG', re.compile('\\bjwt\\.(?:encode|decode)\\(\\s*[^,()]*,\\s*[bBrRuU]{0,2}(?P<q>[\'\\"])(?P<v>[^\'\\"\\s\\x00]{6,256})(?P=q)'), lambda m: not _PLACEHOLDER_RX.fullmatch(m.group('v')))]; source annotation list[tuple[str, re.Pattern, Callable[[re.Match], bool] | None]]. Then For _KNOWN_VALUES, assign OrderedDict(); source annotation OrderedDict[str, None].
// Source: vvaharness/report/redact.py:248-257
In source order: Evaluate once threading.Lock(); assign in source target order to _KNOWN_LOCK. Then Evaluate once 2048; assign in source target order to _KNOWN_VALUES_MAX. Then Evaluate once 10; assign in source target order to _MIN_KNOWN_LEN. Then Evaluate once 12; assign in source target order to _KNOWN_LONG_ENOUGH_ALONE.
// Source: vvaharness/report/redact.py:260-267
// Source signature: _class_diversity(value: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _class_diversity(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:261-261
  In source order: Retain source documentation literal source_literal_261_4; it is not a model call.
  // Source: vvaharness/report/redact.py:262-267
  End this invocation with sum((any((c.islower() for c in value)), any((c.isupper() for c in value)), any((c.isdigit() for c in value)), any((not c.isalnum() for c in value)))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:270-277
// Source signature: _rememberable(value: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rememberable(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:271-271
  In source order: Retain source documentation literal source_literal_271_4; it is not a model call.
  // Source: vvaharness/report/redact.py:273-274
  if (the source predicate len(value) < _MIN_KNOWN_LEN is truthy) {
    // Source: vvaharness/report/redact.py:274-274
    End this invocation with False.
  }
  // Source: vvaharness/report/redact.py:275-276
  if (the source predicate len(value) >= _KNOWN_LONG_ENOUGH_ALONE is truthy) {
    // Source: vvaharness/report/redact.py:276-276
    End this invocation with True.
  }
  // Source: vvaharness/report/redact.py:277-277
  End this invocation with _class_diversity(value) >= 2.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:280-288
// Source signature: _remember_known_value(value: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remember_known_value(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:281-281
  In source order: Retain source documentation literal source_literal_281_4; it is not a model call.
  // Source: vvaharness/report/redact.py:283-285
  if (the source predicate value in _KNOWN_VALUES is truthy) {
    // Source: vvaharness/report/redact.py:284-284
    In source order: Evaluate _KNOWN_VALUES.move_to_end(value); retain side effects and discard the expression result.
    // Source: vvaharness/report/redact.py:285-285
    End this invocation with None.
  }
  // Source: vvaharness/report/redact.py:286-287
  if (the source predicate len(_KNOWN_VALUES) >= _KNOWN_VALUES_MAX is truthy) {
    // Source: vvaharness/report/redact.py:287-287
    In source order: Evaluate _KNOWN_VALUES.popitem(last=False); retain side effects and discard the expression result.
  }
  // Source: vvaharness/report/redact.py:288-288
  In source order: Evaluate once None; assign in source target order to _KNOWN_VALUES[value].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:291-295
// Source signature: reset_known_values() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reset_known_values() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:292-292
  In source order: Retain source documentation literal source_literal_292_4; it is not a model call.
  // Source: vvaharness/report/redact.py:294-295
  Enter source context managers left-to-right: _KNOWN_LOCK {
    // Source: vvaharness/report/redact.py:295-295
    In source order: Evaluate _KNOWN_VALUES.clear(); retain side effects and discard the expression result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:300-408
// Source signature: _redact_impl(text: str, *, carry: bool=True) -> tuple[str, dict[str, int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _redact_impl(text, carry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:301-301
  In source order: Retain source documentation literal source_literal_301_4; it is not a model call.
  // Source: vvaharness/report/redact.py:303-304
  if (the source predicate '\x00' in text is truthy) {
    // Source: vvaharness/report/redact.py:304-304
    In source order: Evaluate once text.replace('\x00', ''); assign in source target order to text.
  }
  // Source: vvaharness/report/redact.py:305-307
  In source order: For counts, assign {}; source annotation dict[str, int]. Then For placeholders, assign []; source annotation list[str]. Then Evaluate once '\x00{}\x00'; assign in source target order to sentinel.
  // Source: vvaharness/report/redact.py:309-320
  // Source signature: _mask(label: str, m: re.Match, *, span: str | None=None, remember: bool=True) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _mask(label, m, span, remember) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/report/redact.py:311-314
    In source order: Evaluate once counts.get(label, 0) + 1; assign in source target order to counts[label]. Then Evaluate once span if span is not None else m.group(0); assign in source target order to value. Then Evaluate once value.count(source_literal_314_25); assign in source target order to nl.
    // Source: vvaharness/report/redact.py:316-318
    if (the source predicate nl == 0 and remember and _rememberable(value) is truthy) {
      // Source: vvaharness/report/redact.py:317-318
      Enter source context managers left-to-right: _KNOWN_LOCK {
        // Source: vvaharness/report/redact.py:318-318
        In source order: Evaluate _remember_known_value(value); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/report/redact.py:319-319
    In source order: Evaluate placeholders.append(source_template_319_28 + source_literal_319_52 * nl); retain side effects and discard the expression result.
    // Source: vvaharness/report/redact.py:320-320
    End this invocation with sentinel.format(len(placeholders) - 1).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/report/redact.py:322-322
  In source order: Evaluate once text; assign in source target order to out.
  // Source: vvaharness/report/redact.py:323-385
  for each (label, rx, validator) in _PATTERNS {
    // Source: vvaharness/report/redact.py:324-384
    // Source signature: _sub(m: re.Match, _label=label, _ok=validator) -> str
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _sub(m, _label, _ok) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/report/redact.py:325-326
      if (the source predicate _ok is not None and (not _ok(m)) is truthy) {
        // Source: vvaharness/report/redact.py:326-326
        End this invocation with m.group(0).
      }
      // Source: vvaharness/report/redact.py:327-371
      if (the source predicate _label == 'SECRET' is truthy) {
        // Source: vvaharness/report/redact.py:328-331
        In source order: Evaluate once m.group('v'); assign in source target order to v. Then Evaluate once bool(m.group('q')); assign in source target order to quoted. Then Evaluate once v if quoted else v.rstrip(').}]!?>*|') or v; assign in source target order to v_core.
        // Source: vvaharness/report/redact.py:332-333
        if (the source predicate len(v_core) < 6 is truthy) {
          // Source: vvaharness/report/redact.py:333-333
          In source order: Evaluate once v; assign in source target order to v_core.
        }
        // Source: vvaharness/report/redact.py:335-336
        if (the source predicate _REDACTED_TAG_RX.match(v) is truthy) {
          // Source: vvaharness/report/redact.py:336-336
          End this invocation with m.group(0).
        }
        // Source: vvaharness/report/redact.py:338-340
        if (the source predicate not m.group('q') and source_literal_338_40 in m.group(0)[:m.start('v') - m.start(0)] and (v.endswith(':') or _NEXT_LINE_ENV_KEY.match(v)) is truthy) {
          // Source: vvaharness/report/redact.py:340-340
          End this invocation with m.group(0).
        }
        // Source: vvaharness/report/redact.py:341-352
        In source order: Evaluate once re.sub('[^a-z]', '', m.group(1).lower()); assign in source target order to keyword. Then Evaluate once {'password', 'passwd', 'pwd', 'apikey', 'accesskey', 'clientsecret', 'authtoken', 'passphrase', 'privatekey', 'secretkey', 'signingkey', 'encryptionkey', 'aeskey', 'jwtkey', 'hmackey', 'masterkey'}; assign in source target order to strong. Then Evaluate once not quoted; assign in source target order to unquoted. Then Evaluate once keyword not in strong and unquoted; assign in source target order to generic_unquoted. Then Evaluate once m.group('op') == '=' and (not m.group('presp')) and (not m.group('postsp')); assign in source target order to tight_equals_assignment.
        // Source: vvaharness/report/redact.py:354-362
        In source order: Evaluate once len(v_core) < 20; assign in source target order to short. Then Evaluate once short and bool(_IDENTIFIER_SHAPE.fullmatch(v_core)); assign in source target order to identifier. Then Evaluate once generic_unquoted and (not tight_equals_assignment) and v_core.islower() and (v_core.isalpha() and short or identifier); assign in source target order to plain_word. Then Evaluate once unquoted and bool(_SECRET_CODE_SHAPE.match(v_core) if generic_unquoted else _SECRET_CODE_SHAPE_DOTTED_CALL.match(v_core)); assign in source target order to code_shape.
        // Source: vvaharness/report/redact.py:363-364
        if (the source predicate plain_word or code_shape is truthy) {
          // Source: vvaharness/report/redact.py:364-364
          End this invocation with m.group(0).
        }
        // Source: vvaharness/report/redact.py:365-369
        In source order: Evaluate once m.group(0)[:m.start('v') - m.start(0)]; assign in source target order to head. Then Evaluate once v[len(v_core):] + m.group(0)[m.end('v') - m.start(0):]; assign in source target order to tail. Then Evaluate once not (unquoted and (_SECRET_CODE_SHAPE.match(v_core) or identifier)); assign in source target order to remember.
        // Source: vvaharness/report/redact.py:370-371
        End this invocation with head + _mask(_label, m, span=v_core, remember=remember) + tail.
      }
      // Source: vvaharness/report/redact.py:372-376
      if (the source predicate _label in ('SECRET-XML', 'SECRET-ARG') is truthy) {
        // Source: vvaharness/report/redact.py:374-376
        End this invocation with m.group(0)[:m.start('v') - m.start(0)] + _mask('SECRET', m, span=m.group('v')) + m.group(0)[m.end('v') - m.start(0):].
      }
      // Source: vvaharness/report/redact.py:377-378
      if (the source predicate _label == 'CVV' is truthy) {
        // Source: vvaharness/report/redact.py:378-378
        End this invocation with m.group(0)[:m.start(2) - m.start(0)] + _mask(_label, m, span=m.group(2)).
      }
      // Source: vvaharness/report/redact.py:379-381
      if (the source predicate _label == 'SSN-CTX' is truthy) {
        // Source: vvaharness/report/redact.py:381-381
        End this invocation with m.group(0)[:m.start(2) - m.start(0)] + _mask('SSN', m, span=m.group(2)).
      }
      // Source: vvaharness/report/redact.py:382-383
      if (the source predicate _label == 'URL-CRED' is truthy) {
        // Source: vvaharness/report/redact.py:383-383
        End this invocation with m.group(1) + _mask(_label, m, span=m.group(2)) + '@'.
      }
      // Source: vvaharness/report/redact.py:384-384
      End this invocation with _mask(_label, m).
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/report/redact.py:385-385
    In source order: Evaluate once rx.sub(_sub, out); assign in source target order to out.
  }
  // Source: vvaharness/report/redact.py:388-400
  if (the source predicate carry and _KNOWN_VALUES is truthy) {
    // Source: vvaharness/report/redact.py:389-391
    Enter source context managers left-to-right: _KNOWN_LOCK {
      // Source: vvaharness/report/redact.py:391-391
      In source order: Evaluate once sorted(_KNOWN_VALUES, key=lambda s: (-len(s), s)); assign in source target order to known.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/report/redact.py:392-400
    for each value in known {
      // Source: vvaharness/report/redact.py:393-400
      if (the source predicate value in out is truthy) {
        // Source: vvaharness/report/redact.py:395-397
        Enter source context managers left-to-right: _KNOWN_LOCK {
          // Source: vvaharness/report/redact.py:396-397
          if (the source predicate value in _KNOWN_VALUES is truthy) {
            // Source: vvaharness/report/redact.py:397-397
            In source order: Evaluate _KNOWN_VALUES.move_to_end(value); retain side effects and discard the expression result.
          }
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
        // Source: vvaharness/report/redact.py:398-400
        In source order: Evaluate once re.sub(re.escape(value), lambda m: _mask('SECRET-RESTATED', m), out); assign in source target order to out.
      }
    }
  }
  // Source: vvaharness/report/redact.py:402-407
  if (the source predicate placeholders is truthy) {
    // Source: vvaharness/report/redact.py:403-406
    // Source signature: _reinsert(m: re.Match) -> str
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _reinsert(m) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/report/redact.py:404-404
      In source order: Evaluate once int(m.group(1)); assign in source target order to idx.
      // Source: vvaharness/report/redact.py:406-406
      End this invocation with placeholders[idx] if 0 <= idx < len(placeholders) else m.group(0).
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/report/redact.py:407-407
    In source order: Evaluate once re.sub('\\x00(\\d+)\\x00', _reinsert, out); assign in source target order to out.
  }
  // Source: vvaharness/report/redact.py:408-408
  End this invocation with (out, counts).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:411-417
// Source signature: redact(text: str, *, carry: bool=True) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn redact(text, carry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:412-412
  In source order: Retain source documentation literal source_literal_412_4; it is not a model call.
  // Source: vvaharness/report/redact.py:413-414
  if (the source predicate not text is truthy) {
    // Source: vvaharness/report/redact.py:414-414
    End this invocation with text.
  }
  // Source: vvaharness/report/redact.py:415-416
  In source order: Evaluate once _redact_impl(text, carry=carry); assign in source target order to (out, counts). Then Evaluate once dict(counts); assign in source target order to redact.last_counts.
  // Source: vvaharness/report/redact.py:417-417
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:420-424
// Source signature: redact_counts(text: str, *, carry: bool=True) -> tuple[str, dict[str, int]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn redact_counts(text, carry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:421-421
  In source order: Retain source documentation literal source_literal_421_4; it is not a model call.
  // Source: vvaharness/report/redact.py:422-423
  if (the source predicate not text is truthy) {
    // Source: vvaharness/report/redact.py:423-423
    End this invocation with (text, {}).
  }
  // Source: vvaharness/report/redact.py:424-424
  End this invocation with _redact_impl(text, carry=carry).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/redact.py:428-432
In source order: Evaluate once frozenset({'file', 'uri', 'source_ref', 'sink_ref', 'chunk_id', 'case_id', 'ruleId', 'partialFingerprints', 'aliasFindingIds', 'filePath', 'file_path', 'filenames', 'path'}); assign in source target order to _NO_CARRY_KEYS.
// Source: vvaharness/report/redact.py:435-446
// Source signature: redact_tree(obj: _TreeT, *, carry: bool=True) -> _TreeT
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn redact_tree(obj, carry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/redact.py:436-436
  In source order: Retain source documentation literal source_literal_436_4; it is not a model call.
  // Source: vvaharness/report/redact.py:437-439
  if (the source predicate isinstance(obj, dict) is truthy) {
    // Source: vvaharness/report/redact.py:438-439
    End this invocation with {k: redact_tree(v, carry=carry and k not in _NO_CARRY_KEYS) for k, v in obj.items()}.
  }
  // Source: vvaharness/report/redact.py:440-441
  if (the source predicate isinstance(obj, list) is truthy) {
    // Source: vvaharness/report/redact.py:441-441
    End this invocation with [redact_tree(v, carry=carry) for v in obj].
  }
  // Source: vvaharness/report/redact.py:442-443
  if (the source predicate isinstance(obj, tuple) is truthy) {
    // Source: vvaharness/report/redact.py:443-443
    End this invocation with tuple((redact_tree(v, carry=carry) for v in obj)).
  }
  // Source: vvaharness/report/redact.py:444-445
  if (the source predicate isinstance(obj, str) is truthy) {
    // Source: vvaharness/report/redact.py:445-445
    End this invocation with redact(obj, carry=carry).
  }
  // Source: vvaharness/report/redact.py:446-446
  End this invocation with obj.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/report/redact.py.sudo.md). Exact strings in the evidence asset support this conversion.
