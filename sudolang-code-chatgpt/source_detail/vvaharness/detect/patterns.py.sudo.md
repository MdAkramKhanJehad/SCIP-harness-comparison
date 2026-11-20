# vvaharness/detect/patterns.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/detect/patterns.py.evidence.json`. SHA-256: `709795a5312dbd6c2fd90ebd79abe42243ef4beed9867c75cb20a0d0a0cccec6`.

```sudo
// Source: vvaharness/detect/patterns.py:15-19
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.detect.spec import MatchSpec; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import OWASP_2025_BY_SEMANTIC; preserve alias and import-time effects.
// Source: vvaharness/detect/patterns.py:24-25
// Source signature: _owasp(family: str) -> frozenset[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _owasp(family) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:25-25
  End this invocation with frozenset(OWASP_2025_BY_SEMANTIC.get(family, ('A03:2025-Injection',))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:28-29
// Source signature: _bare_call(name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bare_call(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:29-29
  End this invocation with source_template_29_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:32-33
// Source signature: _method_call(name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _method_call(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:33-33
  End this invocation with source_template_33_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:36-37
// Source signature: _qualified_call(module: str, name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _qualified_call(module, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:37-37
  End this invocation with source_template_37_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:41-66
In source order: Evaluate once '|'.join((source_template_41_26 for name in ('a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'base', 'bdi', 'bdo', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'link', 'main', 'map', 'mark', 'menu', 'meta', 'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup', 'option', 'output', 'p', 'param', 'picture', 'pre', 'progress', 'q', 'rp', 'rt', 'ruby', 's', 'samp', 'script', 'search', 'section', 'select', 'slot', 'small', 'source', 'span', 'strong', 'style', 'sub', 'summary', 'sup', 'svg', 'table', 'tbody', 'td', 'template', 'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'u', 'ul', 'var', 'video', 'wbr'))); assign in source target order to _HTML_ELEMENTS. Then Evaluate once ('system', 'popen', 'spawn', 'exec', 'eval'); assign in source target order to _COMMAND_METHODS. Then Evaluate once {'os': ('system',), 'subprocess': ('run', 'call', 'check_output', 'check_call', 'Popen')}; assign in source target order to _COMMAND_QUALIFIED. Then Evaluate once ('execute', 'executemany', 'raw', 'query'); assign in source target order to _SQL_METHODS. Then Evaluate once ('loads', 'load', 'deserialize', 'unmarshal'); assign in source target order to _DESERIALIZE_METHODS.
// Source: vvaharness/detect/patterns.py:67-94
In source order: Evaluate once {'pickle': ('loads', 'load'), 'yaml': ('load',)}; assign in source target order to _DESERIALIZE_MODULE_METHODS. Then Evaluate once {'request.args': 'network', 'request.form': 'network', 'request.json': 'network', 'request.data': 'network', 'request.headers': 'network', 'request.cookies': 'network', 'request.get_json': 'network', 'request.GET': 'network', 'request.POST': 'network', 'request.META': 'network', 'request.FILES': 'network', 'request.COOKIES': 'network', 'request.body': 'network', 'os.environ': 'file', 'os.getenv': 'file', 'sys.argv': 'cli', 'sys.stdin': 'cli', 'BaseHTTPRequestHandler': 'network', 'SimpleHTTPRequestHandler': 'network'}; assign in source target order to _SOURCE_ACCESSORS.
// Source: vvaharness/detect/patterns.py:97-123
// Source signature: _command_specs() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _command_specs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:98-122
  In source order: Evaluate once [MatchSpec(rule_id=source_template_100_20, role='sink', pattern=_bare_call(name), cwe='CWE-78', kind='command_injection', semantic_family='command-exec', owasp_top10_2025=_owasp('command-exec')) for name in _COMMAND_METHODS]; assign in source target order to specs. Then Evaluate specs.extend((MatchSpec(rule_id=source_template_112_20, role='sink', pattern=_qualified_call(module, name), cwe='CWE-78', kind='command_injection', semantic_family='command-exec', owasp_top10_2025=_owasp('command-exec')) for module, names in _COMMAND_QUALIFIED.items() for name in names)); retain side effects and discard the expression result.
  // Source: vvaharness/detect/patterns.py:123-123
  End this invocation with specs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:126-137
// Source signature: _template_specs() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _template_specs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:127-137
  End this invocation with [MatchSpec(rule_id='detect-sink-template-render_template_string', role='sink', pattern=_bare_call('render_template_string'), cwe='CWE-79', kind='xss', semantic_family='html-response', owasp_top10_2025=_owasp('html-response'))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:140-151
// Source signature: _cookie_specs() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cookie_specs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:142-151
  End this invocation with [MatchSpec(rule_id=source_template_144_20, role='sink', pattern=_method_call('set_cookie'), cwe=cwe, kind='cookie_flag') for flag, cwe in (('httponly', 'CWE-1004'), ('secure', 'CWE-614'))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:154-166
// Source signature: _sql_specs() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sql_specs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:155-166
  End this invocation with [MatchSpec(rule_id=source_template_157_20, role='sink', pattern=_method_call(name), cwe='CWE-89', kind='sql_injection', semantic_family='sql-exec', owasp_top10_2025=_owasp('sql-exec')) for name in _SQL_METHODS].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:169-195
// Source signature: _deserialize_specs() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deserialize_specs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:170-194
  In source order: Evaluate once [MatchSpec(rule_id=source_template_172_20, role='sink', pattern=_bare_call(name), cwe='CWE-502', kind='unsafe_deserialization', semantic_family='deserialization', owasp_top10_2025=_owasp('deserialization')) for name in _DESERIALIZE_METHODS]; assign in source target order to specs. Then Evaluate specs.extend((MatchSpec(rule_id=source_template_184_20, role='sink', pattern=_qualified_call(module, name), cwe='CWE-502', kind='unsafe_deserialization', semantic_family='deserialization', owasp_top10_2025=_owasp('deserialization')) for module, names in _DESERIALIZE_MODULE_METHODS.items() for name in names)); retain side effects and discard the expression result.
  // Source: vvaharness/detect/patterns.py:195-195
  End this invocation with specs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:198-210
// Source signature: _source_specs() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _source_specs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:199-210
  End this invocation with [MatchSpec(rule_id=source_template_201_20, role='source', pattern=source_template_203_20, cwe='CWE-20', kind=kind, semantic_family='untrusted-input', owasp_top10_2025=_owasp('untrusted-input')) for accessor, kind in _SOURCE_ACCESSORS.items()].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:213-216
// Source signature: default_corpus() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn default_corpus() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:214-214
  In source order: Retain source documentation literal source_literal_214_4; it is not a model call.
  // Source: vvaharness/detect/patterns.py:215-216
  End this invocation with [*_command_specs(), *_sql_specs(), *_deserialize_specs(), *_template_specs(), *_cookie_specs(), *_source_specs()].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/detect/patterns.py:221-398
// Source signature: detector_corpus() -> list[MatchSpec]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detector_corpus() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/detect/patterns.py:222-222
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call.
  // Source: vvaharness/detect/patterns.py:223-398
  End this invocation with [MatchSpec(rule_id='detector-cookie-httponly', role='detector', pattern='\\.set_cookie\\s*\\(', cwe='CWE-1004', kind='cookie-flag', languages=frozenset({'python'}), title='Cookie set without the HttpOnly flag', citation="CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag (https://cwe.mitre.org/data/definitions/1004.html)", span='call', span_max_lines=20, absent_re='(?i)\\bhttponly\\s*=\\s*(?!false\\b|none\\b|0\\b)'), MatchSpec(rule_id='detector-cookie-secure', role='detector', pattern='\\.set_cookie\\s*\\(', cwe='CWE-614', kind='cookie-flag', languages=frozenset({'python'}), title='Cookie set without the Secure flag', citation="CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute (https://cwe.mitre.org/data/definitions/614.html)", span='call', span_max_lines=20, absent_re='(?i)\\bsecure\\s*=\\s*(?!false\\b|none\\b|0\\b)'), MatchSpec(rule_id='detector-autoescape-off-code', role='detector', pattern='\\bautoescape\\s*=\\s*False\\b', cwe='CWE-79', kind='xss', semantic_family='html-response', languages=frozenset({'python'}), title='Template auto-escaping explicitly disabled', citation='CWE-79: Improper Neutralization of Input During Web Page Generation (https://cwe.mitre.org/data/definitions/79.html)'), MatchSpec(rule_id='detector-autoescape-off-template', role='detector', pattern='\\{%-?\\s*autoescape\\s+(?:false|off)\\b', cwe='CWE-79', kind='xss', semantic_family='html-response', languages=frozenset({'web-template'}), title='Template block disables auto-escaping', citation='CWE-79: Improper Neutralization of Input During Web Page Generation (https://cwe.mitre.org/data/definitions/79.html)'), MatchSpec(rule_id='detector-jinja-env-noescape', role='detector', pattern='\\bEnvironment\\s*\\(', cwe='CWE-79', kind='xss', semantic_family='html-response', languages=frozenset({'python'}), title='Jinja2 Environment constructed without autoescape', citation='CWE-79 via jinja2.Environment(autoescape=False is the default) (https://cwe.mitre.org/data/definitions/79.html)', span='call', span_max_lines=20, absent_re='autoescape', file_re='(?m)^[^\\S\\n]*(?:import\\s+jinja2\\b|from\\s+jinja2(?:\\.\\w+)*\\s+import\\b)'), MatchSpec(rule_id='detector-template-safe', role='detector', pattern='\\{\\{[^{}]*\\|\\s*safe\\b', cwe='CWE-79', kind='xss', semantic_family='html-response', languages=frozenset({'web-template'}), title='Template output piped through |safe', citation='CWE-79: the |safe filter marks a value exempt from output escaping (https://cwe.mitre.org/data/definitions/79.html)'), MatchSpec(rule_id='detector-docwrite-location', role='detector', pattern='document\\.write(?:ln)?\\s*\\(', cwe='CWE-79', kind='xss', semantic_family='html-response', languages=frozenset({'javascript', 'typescript', 'web-template'}), title='document.write near a URL-derived value', citation='CWE-79 DOM-based XSS via document.write of location data (https://owasp.org/www-community/attacks/DOM_Based_XSS)', near_re='(?:\\blocation\\.|\\bdocument\\.URL\\b|\\bdecodeURIComponent\\s*\\()', near_window=3), MatchSpec(rule_id='detector-form-no-csrf-post', role='detector', enabled=False, pattern='<form\\b', cwe='CWE-352', kind='csrf', languages=frozenset({'web-template'}), title='POST form without a CSRF token', citation='CWE-352: Cross-Site Request Forgery (https://cwe.mitre.org/data/definitions/352.html)', span='block', span_end='</form', span_max_lines=120, present_re='(?is)method\\s*=\\s*[\\"\']?post', absent_re='(?i)csrf|hidden_tag\\s*\\(|authenticity_token|__RequestVerificationToken'), MatchSpec(rule_id='detector-form-get-password', role='detector', enabled=False, pattern='<form\\b', cwe='CWE-598', kind='sensitive-data', languages=frozenset({'web-template'}), title='Password form submits with GET', citation='CWE-598: Use of GET Request Method With Sensitive Query Strings (https://cwe.mitre.org/data/definitions/598.html)', span='block', span_end='</form', span_max_lines=120, present_re='(?is)type\\s*=\\s*[\\"\']?password', absent_re='(?i)method\\s*=\\s*[\\"\']?post'), MatchSpec(rule_id='detector-httpresponse-concat', role='detector', pattern='\\bHttpResponse\\s*\\(', cwe='CWE-79', kind='xss', semantic_family='html-response', languages=frozenset({'python'}), title='HttpResponse built from string interpolation', citation=source_literal_367_21, span='call', span_max_lines=20, present_re='(?:[\\"\']\\s*\\+|\\+\\s*[\\"\']|[\\"\'\\s]%[\\s_a-zA-Z(\\"\']|%\\s*\\(|\\.format\\s*\\(|\\bf[\\"\'])'), MatchSpec(rule_id='detector-html-string-concat', role='detector', pattern='[\\"\']<(?:!--|/?(?:' + _HTML_ELEMENTS + ')\\b[^<>]{0,160}?>)', cwe='CWE-79', kind='xss', semantic_family='html-response', languages=frozenset({'python'}), title='HTML assembled by string concatenation', citation='CWE-79: HTML built from values without output encoding (https://cwe.mitre.org/data/definitions/79.html)', present_re='(?:\\+\\s*[A-Za-z_(]|[\\"\'\\s]%[\\s_a-zA-Z(\\"\']|%\\s*\\(|\\.format\\s*\\(|\\bf[\\"\']<[^\\n]{0,200}\\{)', absent_re='(?:\\b(?:escape|quote|quoteattr|sanitize|bleach|Markup)\\s*\\(|\\bstruct\\.\\w+\\s*\\(|\\b__repr__\\b)', absent_window=2)].
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.detect.spec import MatchSpec` at source line 18: `source_detail/vvaharness/detect/spec.py.sudo.md`.
- `from vvaharness.rules.cwe import OWASP_2025_BY_SEMANTIC` at source line 19: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
