# vvaharness/rules/repo_kinds.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/rules/repo_kinds.py.evidence.json`. SHA-256: `93dca902cc86d70cf869225854e12c50dd2e4b593f2aea7b63337d749bad7fde`.

```sudo
// Source: vvaharness/rules/repo_kinds.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence import ThreatEvidence; preserve alias and import-time effects. Then Resolve source import from vvaharness.lang.detect import LANG_DISPLAY, is_iac_file, is_web_template; preserve alias and import-time effects.
// Source: vvaharness/rules/repo_kinds.py:22-44
In source order: Resolve source import from vvaharness.models import ContextPackage; preserve alias and import-time effects. Then Evaluate once {'network': 'S T R I D E', 'framework': 'S T R I D E', 'ipc': 'T I E', 'file': 'T I D', 'cli': 'T E', 'deserialization': 'T E', 'other': 'T I'}; assign in source target order to STRIDE_BY_KIND. Then Evaluate once re.compile(source_literal_37_4, re.IGNORECASE); assign in source target order to WEB_FW_RX. Then Evaluate once {'c', 'cpp', 'c++', 'c-cpp', 'c/c++', 'rust', 'objective-c', 'objc'}; assign in source target order to NATIVE_LANGS. Then Evaluate once {'web-template', LANG_DISPLAY['web-template'].lower()}; assign in source target order to _WEB_TEMPLATE_LANG_LABELS.
// Source: vvaharness/rules/repo_kinds.py:47-94
In source order: For BASELINES, assign {'web-api': (('BL-WEB-A01', 'OWASP A01 Broken Access Control (IDOR, path traversal, forced browsing, privilege escalation)'), ('BL-WEB-A02', 'OWASP A02 Cryptographic Failures (weak/missing crypto, plaintext secrets/transport)'), ('BL-WEB-A03', 'OWASP A03 Injection (SQL/NoSQL/OS/LDAP/template/header)'), ('BL-WEB-A04', 'OWASP A04 Insecure Design (missing rate-limit, trust-boundary assumptions)'), ('BL-WEB-A05', 'OWASP A05 Security Misconfiguration (default creds, debug on, permissive CORS)'), ('BL-WEB-A07', 'OWASP A07 Identification & Authentication Failures (weak session, missing MFA, JWT flaws)'), ('BL-WEB-A08', 'OWASP A08 Software & Data Integrity Failures (unsafe deserialization, unsigned updates)'), ('BL-WEB-A10', 'OWASP A10 Server-Side Request Forgery'), ('BL-WEB-XSS', 'XSS (reflected / stored / DOM)'), ('BL-WEB-CSRF', 'CSRF / state-changing GET')), 'mobile': (('BL-MOB-M1', 'OWASP M1 Improper Credential Usage (hardcoded keys, token leakage)'), ('BL-MOB-M3', 'OWASP M3 Insecure Authentication/Authorization'), ('BL-MOB-M5', 'OWASP M5 Insecure Communication (no cert pinning, cleartext traffic)'), ('BL-MOB-M8', 'OWASP M8 Security Misconfiguration (exported components, debuggable build)'), ('BL-MOB-M9', 'OWASP M9 Insecure Data Storage (world-readable prefs, unencrypted DB)')), 'native': (('BL-NAT-119', 'CWE-119/787 Buffer overflow (stack/heap write OOB)'), ('BL-NAT-416', 'CWE-416 Use-after-free / double-free'), ('BL-NAT-190', 'CWE-190 Integer overflow leading to undersized allocation'), ('BL-NAT-134', 'CWE-134 Format-string'), ('BL-NAT-362', 'CWE-362 TOCTOU / race condition'), ('BL-NAT-78', 'CWE-78 OS command injection via system()/exec()')), 'iac': (('BL-IAC-IAM', 'Over-permissive IAM / RBAC (wildcard actions, cluster-admin bindings)'), ('BL-IAC-NET', 'Public network exposure (0.0.0.0/0 ingress, hostNetwork, public S3/bucket)'), ('BL-IAC-SECRETS', 'Secrets committed in plaintext / env'), ('BL-IAC-PRIV', 'Privileged or root containers, missing securityContext'), ('BL-IAC-TLS', 'Disabled TLS / unencrypted storage classes')), 'library': (('BL-LIB-INJ', 'Injection via untrusted caller input (SQL/OS/path)'), ('BL-LIB-DESER', 'Unsafe deserialization (pickle/yaml.load/XMLDecoder/ObjectInputStream)'), ('BL-LIB-PATH', 'Path traversal in file-handling APIs'), ('BL-LIB-REDOS', 'ReDoS / algorithmic-complexity DoS')), 'web-template': (('BL-TPL-XSS', 'XSS via unescaped/raw template output (e.g. Jinja `|safe`, Handlebars `{{{ }}}`, ERB `<%= raw %>`)'), ('BL-TPL-SSTI', 'Server-side template injection (untrusted input reaching the template source/name)'), ('BL-TPL-CSRF', 'CSRF-vulnerable forms (state-changing `<form>` with no anti-CSRF token)'), ('BL-TPL-SECRET', 'Secrets or internal config leaked into rendered markup (hardcoded keys, comments, debug data)'))}; source annotation dict[str, tuple[tuple[str, str], ...]].
// Source: vvaharness/rules/repo_kinds.py:97-130
// Source signature: repo_kind(ev: ThreatEvidence, ctx: ContextPackage | None) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn repo_kind(ev, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/repo_kinds.py:98-104
  In source order: For kinds, assign set(); source annotation set[str]. Then Evaluate once [f.lower() for f in (ctx.all_files if ctx else [])]; assign in source target order to all_files. Then Evaluate once source_literal_100_20.join((body for _, body in ev.manifests)); assign in source target order to manifest_text. Then Evaluate once {(ev.primary_language or '').lower(), *(lang.lower() for lang, _ in ev.languages)}; assign in source target order to langs. Then Evaluate once langs - ({''} | _WEB_TEMPLATE_LANG_LABELS); assign in source target order to non_template_langs.
  // Source: vvaharness/rules/repo_kinds.py:106-112
  In source order: Evaluate once any((k in ('network', 'framework') for k, *_ in ev.entry_points)) or bool(ev.api_artefacts); assign in source target order to has_entrypoint_or_artefact_signal. Then Evaluate once bool(WEB_FW_RX.search(manifest_text)); assign in source target order to manifest_web_fw_match. Then Evaluate once bool(all_files) and (not non_template_langs) and any((is_web_template(f) for f in all_files)); assign in source target order to template_dominated.
  // Source: vvaharness/rules/repo_kinds.py:114-117
  if (the source predicate has_entrypoint_or_artefact_signal or (manifest_web_fw_match and (not template_dominated)) is truthy) {
    // Source: vvaharness/rules/repo_kinds.py:115-115
    In source order: Evaluate kinds.add('web-api'); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/rules/repo_kinds.py:116-117
    if (the source predicate template_dominated is truthy) {
      // Source: vvaharness/rules/repo_kinds.py:117-117
      In source order: Evaluate kinds.add('web-template'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/rules/repo_kinds.py:119-122
  if (the source predicate any((f.endswith(('androidmanifest.xml', 'info.plist', 'podfile')) for f in all_files)) or re.search('\\bcom\\.android\\b', manifest_text) is truthy) {
    // Source: vvaharness/rules/repo_kinds.py:122-122
    In source order: Evaluate kinds.add('mobile'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/rules/repo_kinds.py:124-125
  if (the source predicate any((is_iac_file(f) for f in all_files)) is truthy) {
    // Source: vvaharness/rules/repo_kinds.py:125-125
    In source order: Evaluate kinds.add('iac'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/rules/repo_kinds.py:127-128
  if (the source predicate langs & NATIVE_LANGS is truthy) {
    // Source: vvaharness/rules/repo_kinds.py:128-128
    In source order: Evaluate kinds.add('native'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/rules/repo_kinds.py:130-130
  End this invocation with kinds or {'library'}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/rules/repo_kinds.py:133-139
In source order: Evaluate once ['BASELINES', 'NATIVE_LANGS', 'STRIDE_BY_KIND', 'WEB_FW_RX', 'repo_kind']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.evidence import ThreatEvidence` at source line 20: `source_detail/vvaharness/evidence/__init__.py.sudo.md`.
- `from vvaharness.lang.detect import LANG_DISPLAY, is_iac_file, is_web_template` at source line 21: `source_detail/vvaharness/lang/detect.py.sudo.md`.
- `from vvaharness.models import ContextPackage` at source line 22: `source_detail/vvaharness/models/__init__.py.sudo.md`.
