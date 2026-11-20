# vvaharness/report/cwe.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/report/cwe.py.evidence.json`. SHA-256: `980aabbc8d5fdba71019b4416d45e2a192037e4d89c7bc34d31f39b3902c4674`.

```sudo
// Source: vvaharness/report/cwe.py:15-138
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then For CWE_NAMES, assign {'CWE-20': 'Improper Input Validation', 'CWE-22': 'Improper Limitation of a Pathname to a Restricted Directory (Path Traversal)', 'CWE-23': 'Relative Path Traversal', 'CWE-36': 'Absolute Path Traversal', 'CWE-73': 'External Control of File Name or Path', 'CWE-74': 'Improper Neutralization of Special Elements in Output (Injection)', 'CWE-77': 'Improper Neutralization of Special Elements used in a Command (Command Injection)', 'CWE-78': 'Improper Neutralization of Special Elements used in an OS Command (OS Command Injection)', 'CWE-79': 'Improper Neutralization of Input During Web Page Generation (Cross-site Scripting)', 'CWE-80': 'Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS)', 'CWE-88': 'Improper Neutralization of Argument Delimiters in a Command (Argument Injection)', 'CWE-89': 'Improper Neutralization of Special Elements used in an SQL Command (SQL Injection)', 'CWE-90': 'Improper Neutralization of Special Elements used in an LDAP Query (LDAP Injection)', 'CWE-94': 'Improper Control of Generation of Code (Code Injection)', 'CWE-95': 'Improper Neutralization of Directives in Dynamically Evaluated Code (Eval Injection)', 'CWE-113': 'Improper Neutralization of CRLF Sequences in HTTP Headers (HTTP Request/Response Splitting)', 'CWE-117': 'Improper Output Neutralization for Logs', 'CWE-119': 'Improper Restriction of Operations within the Bounds of a Memory Buffer', 'CWE-120': 'Buffer Copy without Checking Size of Input (Classic Buffer Overflow)', 'CWE-121': 'Stack-based Buffer Overflow', 'CWE-122': 'Heap-based Buffer Overflow', 'CWE-125': 'Out-of-bounds Read', 'CWE-134': 'Use of Externally-Controlled Format String', 'CWE-190': 'Integer Overflow or Wraparound', 'CWE-200': 'Exposure of Sensitive Information to an Unauthorized Actor', 'CWE-201': 'Insertion of Sensitive Information Into Sent Data', 'CWE-204': 'Observable Response Discrepancy', 'CWE-209': 'Generation of Error Message Containing Sensitive Information', 'CWE-215': 'Insertion of Sensitive Information Into Debugging Code', 'CWE-256': 'Plaintext Storage of a Password', 'CWE-259': 'Use of Hard-coded Password', 'CWE-269': 'Improper Privilege Management', 'CWE-276': 'Incorrect Default Permissions', 'CWE-284': 'Improper Access Control', 'CWE-285': 'Improper Authorization', 'CWE-287': 'Improper Authentication', 'CWE-294': 'Authentication Bypass by Capture-replay', 'CWE-295': 'Improper Certificate Validation', 'CWE-306': 'Missing Authentication for Critical Function', 'CWE-307': 'Improper Restriction of Excessive Authentication Attempts', 'CWE-311': 'Missing Encryption of Sensitive Data', 'CWE-312': 'Cleartext Storage of Sensitive Information', 'CWE-319': 'Cleartext Transmission of Sensitive Information', 'CWE-321': 'Use of Hard-coded Cryptographic Key', 'CWE-326': 'Inadequate Encryption Strength', 'CWE-327': 'Use of a Broken or Risky Cryptographic Algorithm', 'CWE-328': 'Use of Weak Hash', 'CWE-330': 'Use of Insufficiently Random Values', 'CWE-338': 'Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)', 'CWE-345': 'Insufficient Verification of Data Authenticity', 'CWE-346': 'Origin Validation Error', 'CWE-347': 'Improper Verification of Cryptographic Signature', 'CWE-352': 'Cross-Site Request Forgery (CSRF)', 'CWE-359': 'Exposure of Private Personal Information to an Unauthorized Actor', 'CWE-362': 'Concurrent Execution using Shared Resource with Improper Synchronization (Race Condition)', 'CWE-367': 'Time-of-check Time-of-use (TOCTOU) Race Condition', 'CWE-384': 'Session Fixation', 'CWE-400': 'Uncontrolled Resource Consumption', 'CWE-416': 'Use After Free', 'CWE-426': 'Untrusted Search Path', 'CWE-434': 'Unrestricted Upload of File with Dangerous Type', 'CWE-436': 'Interpretation Conflict', 'CWE-444': 'Inconsistent Interpretation of HTTP Requests (HTTP Request/Response Smuggling)', 'CWE-476': 'NULL Pointer Dereference', 'CWE-489': 'Active Debug Code', 'CWE-502': 'Deserialization of Untrusted Data', 'CWE-521': 'Weak Password Requirements', 'CWE-522': 'Insufficiently Protected Credentials', 'CWE-532': 'Insertion of Sensitive Information into Log File', 'CWE-538': 'Insertion of Sensitive Information into Externally-Accessible File or Directory', 'CWE-540': 'Inclusion of Sensitive Information in Source Code', 'CWE-552': 'Files or Directories Accessible to External Parties', 'CWE-564': 'SQL Injection: Hibernate', 'CWE-598': 'Use of GET Request Method With Sensitive Query Strings', 'CWE-601': 'URL Redirection to Untrusted Site (Open Redirect)', 'CWE-602': 'Client-Side Enforcement of Server-Side Security', 'CWE-611': 'Improper Restriction of XML External Entity Reference', 'CWE-613': 'Insufficient Session Expiration', 'CWE-614': 'Sensitive Cookie in HTTPS Session Without Secure Attribute', 'CWE-620': 'Unverified Password Change', 'CWE-639': 'Authorization Bypass Through User-Controlled Key', 'CWE-640': 'Weak Password Recovery Mechanism for Forgotten Password', 'CWE-643': 'Improper Neutralization of Data within XPath Expressions (XPath Injection)', 'CWE-668': 'Exposure of Resource to Wrong Sphere', 'CWE-672': 'Operation on a Resource after Expiration or Release', 'CWE-693': 'Protection Mechanism Failure', 'CWE-732': 'Incorrect Permission Assignment for Critical Resource', 'CWE-759': 'Use of a One-Way Hash without a Salt', 'CWE-770': 'Allocation of Resources Without Limits or Throttling', 'CWE-778': 'Insufficient Logging', 'CWE-787': 'Out-of-bounds Write', 'CWE-798': 'Use of Hard-coded Credentials', 'CWE-799': 'Improper Control of Interaction Frequency', 'CWE-807': 'Reliance on Untrusted Inputs in a Security Decision', 'CWE-829': 'Inclusion of Functionality from Untrusted Control Sphere', 'CWE-841': 'Improper Enforcement of Behavioral Workflow', 'CWE-843': 'Access of Resource Using Incompatible Type (Type Confusion)', 'CWE-862': 'Missing Authorization', 'CWE-863': 'Incorrect Authorization', 'CWE-915': 'Improperly Controlled Modification of Dynamically-Determined Object Attributes', 'CWE-916': 'Use of Password Hash With Insufficient Computational Effort', 'CWE-917': 'Improper Neutralization of Special Elements used in an Expression Language Statement (Expression Language Injection)', 'CWE-918': 'Server-Side Request Forgery (SSRF)', 'CWE-923': 'Improper Restriction of Communication Channel to Intended Endpoints', 'CWE-926': 'Improper Export of Android Application Components', 'CWE-927': 'Use of Implicit Intent for Sensitive Communication', 'CWE-942': 'Permissive Cross-domain Security Policy with Untrusted Domains', 'CWE-943': 'Improper Neutralization of Special Elements in Data Query Logic', 'CWE-1004': 'Sensitive Cookie Without HttpOnly Flag', 'CWE-1021': 'Improper Restriction of Rendered UI Layers or Frames', 'CWE-1104': 'Use of Unmaintained Third Party Components', 'CWE-1188': 'Initialization of a Resource with an Insecure Default', 'CWE-1236': 'Improper Neutralization of Formula Elements in a CSV File', 'CWE-1275': 'Sensitive Cookie with Improper SameSite Attribute', 'CWE-1333': 'Inefficient Regular Expression Complexity', 'CWE-1336': 'Improper Neutralization of Special Elements Used in a Template Engine', 'CWE-1390': 'Weak Authentication', 'CWE-1391': 'Use of Weak Credentials'}; source annotation dict[str, str].
// Source: vvaharness/report/cwe.py:141-145
// Source signature: cwe_name(cwe_id: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cwe_name(cwe_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cwe.py:142-142
  In source order: Retain source documentation literal source_literal_142_4; it is not a model call.
  // Source: vvaharness/report/cwe.py:143-144
  if (the source predicate not cwe_id is truthy) {
    // Source: vvaharness/report/cwe.py:144-144
    End this invocation with ''.
  }
  // Source: vvaharness/report/cwe.py:145-145
  End this invocation with CWE_NAMES.get(cwe_id.upper().strip(), '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cwe.py:149-162
In source order: For VULNCLASS_CWE, assign {'use-after-free': 'CWE-416', 'heap-overflow': 'CWE-122', 'stack-overflow': 'CWE-121', 'format-string': 'CWE-134', 'integer-overflow': 'CWE-190', 'type-confusion': 'CWE-843', 'race-condition': 'CWE-362', 'injection': 'CWE-74', 'unsafe-deserialization': 'CWE-502', 'logic-flaw': 'CWE-841', 'info-leak': 'CWE-200', 'other': ''}; source annotation dict[str, str].
// Source: vvaharness/report/cwe.py:165-171
// Source signature: cwe_for(cwe_id: str | None, vuln_class) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cwe_for(cwe_id, vuln_class) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cwe.py:166-166
  In source order: Retain source documentation literal source_literal_166_4; it is not a model call.
  // Source: vvaharness/report/cwe.py:167-168
  if (the source predicate cwe_id is truthy) {
    // Source: vvaharness/report/cwe.py:168-168
    End this invocation with cwe_id.upper().strip().
  }
  // Source: vvaharness/report/cwe.py:169-170
  In source order: Evaluate once getattr(vuln_class, 'value', None) or str(vuln_class or ''); assign in source target order to key. Then Evaluate once VULNCLASS_CWE.get(key, ''); assign in source target order to fb.
  // Source: vvaharness/report/cwe.py:171-171
  End this invocation with fb or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cwe.py:174-179
// Source signature: cwe_label(cwe_id: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cwe_label(cwe_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cwe.py:175-175
  In source order: Retain source documentation literal source_literal_175_4; it is not a model call.
  // Source: vvaharness/report/cwe.py:176-177
  if (the source predicate not cwe_id is truthy) {
    // Source: vvaharness/report/cwe.py:177-177
    End this invocation with ''.
  }
  // Source: vvaharness/report/cwe.py:178-178
  In source order: Evaluate once cwe_name(cwe_id); assign in source target order to name.
  // Source: vvaharness/report/cwe.py:179-179
  End this invocation with source_template_179_11 if name else cwe_id.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/report/cwe.py.sudo.md). Exact strings in the evidence asset support this conversion.
