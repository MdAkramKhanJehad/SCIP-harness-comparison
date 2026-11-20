# vvaharness/report/appcontext.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/report/appcontext.py.evidence.json`. SHA-256: `538c87815afe4645451603f72c77dd62695eb6fe0f59990ffd69a3c573fda2e5`.

```sudo
// Source: vvaharness/report/appcontext.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import csv; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/report/appcontext.py:22-28
In source order: Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from vvaharness.report import cvss; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/report/appcontext.py:30-65
In source order: Evaluate csv.field_size_limit(2 ** 31 - 1); retain side effects and discard the expression result. Then Evaluate once ('P', 'O', 'C'); assign in source target order to (SAST_E, SAST_RL, SAST_RC). Then Evaluate once ('source code is accessible', 'access to the source', 'access to the repo', 'read access to the repo', 'decompil', 'reverse engineer', 'if the attacker knows', 'knowing the function', 'knowledge of the source', 'internal function name', 'would need to know', 'hardcoded credential', 'hardcoded password', 'hardcoded secret', 'hardcoded token', 'hard-coded credential', 'hard-coded password', 'hard-coded secret', 'credential in source', 'secret in source', 'test credential', 'qa credential', 'qa password', 'test password', 'encryption key in source', 'key hardcoded'); assign in source target order to KW_CODE_KNOWLEDGE. Then Evaluate once ('internal network', 'intranet', 'corporate network', 'internal-only', 'internal only', 'back-office', 'corporate sso', 'enterprise sso', 'enterprise idp', 'behind sso', 'behind the idp', 'loopback', '127.0.0.1', 'localhost', 'local listener', 'local user', 'local access', 'same host', 'on the host', 'service-to-service', 'mtls', 'behind api gateway', 'behind the gateway', 'vpn', 'external partner', 'third-party provisioned', 'log access', 'db access', 'database access', 'mitm', 'man-in-the-middle', 'man in the middle', 'compromised server', 'compromise of', 'control of the', 'physical access', 'adjacent network'); assign in source target order to KW_INTERNAL. Then Evaluate once ('super_admin', 'super admin', 'system_admin', 'dist_admin', 'with admin', 'as an admin', 'an admin user', 'admin role', 'privileged user', 'privileged account', 'requires admin', 'admin-only', 'admin privileges'); assign in source target order to KW_HIGH_PRIV.
// Source: vvaharness/report/appcontext.py:66-78
In source order: Evaluate once ('self-registration', 'self-registered', 'self registration', 'free signup', 'sign up for', 'any registered user', 'any authenticated user', 'any user account', 'any valid user', 'developer account', 'portal user', 'merchant account', 'low-privilege user', 'low privilege user', 'lowest role'); assign in source target order to KW_OBTAINABLE_AUTH. Then Evaluate once ('unauthenticated', 'no authentication', 'without authentication', 'no auth required', 'without auth', 'pre-auth', 'anonymous', 'no credentials', 'without credentials', '[allowanonymous]', 'allowanonymous', 'publicly accessible', 'public endpoint'); assign in source target order to KW_NO_AUTH.
// Source: vvaharness/report/appcontext.py:83-110
// Source: vvaharness/report/appcontext.py:82-82
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/report/appcontext.py:83-110
interface AppInfo {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/report/appcontext.py:84-88
  In source order: For id, assign ''; source annotation str. Then For name, assign ''; source annotation str. Then For externally_facing, assign False; source annotation bool. Then For pci_scoped, assign False; source annotation bool. Then For processes_pan, assign False; source annotation bool.
  // Source: vvaharness/report/appcontext.py:89-93
  In source order: For pii, assign False; source annotation bool. Then For ext_raw, assign None; source annotation str | None. Then For pci_raw, assign None; source annotation str | None. Then For pan_raw, assign None; source annotation str | None. Then For pii_raw, assign None; source annotation str | None.
  // Source: vvaharness/report/appcontext.py:94-95
  In source order: For parent_app_id, assign None; source annotation str | None. Then For source, assign 'application'; source annotation str.
  // Source: vvaharness/report/appcontext.py:97-98
  // Source signature: cr(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn cr(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/report/appcontext.py:98-98
    End this invocation with 'H' if self.pci_scoped or self.processes_pan or self.pii else 'M'.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/report/appcontext.py:100-101
  // Source signature: ir(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ir(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/report/appcontext.py:101-101
    End this invocation with 'H' if self.pci_scoped or self.processes_pan else 'M'.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/report/appcontext.py:103-104
  // Source signature: ar(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ar(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/report/appcontext.py:104-104
    End this invocation with 'M'.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/report/appcontext.py:106-107
  // Source signature: mav(self, base_av: str) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn mav(self, base_av) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/report/appcontext.py:107-107
    End this invocation with 'A' if not self.externally_facing and base_av == 'N' else base_av.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/report/appcontext.py:109-110
  // Source signature: env_summary(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn env_summary(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/report/appcontext.py:110-110
    End this invocation with source_template_110_15.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/report/appcontext.py:113-114
// Source signature: _yes(v: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _yes(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:114-114
  End this invocation with v is not None and v.strip().lower() == 'yes'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:117-121
// Source signature: _nz(v: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _nz(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:118-119
  if (the source predicate v is None is truthy) {
    // Source: vvaharness/report/appcontext.py:119-119
    End this invocation with None.
  }
  // Source: vvaharness/report/appcontext.py:120-120
  In source order: Evaluate once v.strip(); assign in source target order to v.
  // Source: vvaharness/report/appcontext.py:121-121
  End this invocation with v or None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:124-128
// Source signature: normalize_app_id(app_id: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn normalize_app_id(app_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:125-126
  if (the source predicate app_id is None is truthy) {
    // Source: vvaharness/report/appcontext.py:126-126
    End this invocation with None.
  }
  // Source: vvaharness/report/appcontext.py:127-127
  In source order: Evaluate once re.sub('^0+', '', app_id.strip()); assign in source target order to s.
  // Source: vvaharness/report/appcontext.py:128-128
  End this invocation with s or '0'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:131-136
// Source signature: _csv_col(hdr: dict, *names: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _csv_col(hdr, names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:132-135
  for each n in names {
    // Source: vvaharness/report/appcontext.py:133-133
    In source order: Evaluate once hdr.get(n.lower()); assign in source target order to i.
    // Source: vvaharness/report/appcontext.py:134-135
    if (the source predicate i is not None is truthy) {
      // Source: vvaharness/report/appcontext.py:135-135
      End this invocation with i.
    }
  }
  // Source: vvaharness/report/appcontext.py:136-136
  End this invocation with -1.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:139-144
// Source signature: _cmdb_enrichment_differs(x: AppInfo, y: AppInfo) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cmdb_enrichment_differs(x, y) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:140-140
  In source order: Retain source documentation literal source_literal_140_4; it is not a model call.
  // Source: vvaharness/report/appcontext.py:141-143
  for each f in ('externally_facing', 'pci_scoped', 'processes_pan', 'pii') {
    // Source: vvaharness/report/appcontext.py:142-143
    if (the source predicate getattr(x, f) != getattr(y, f) is truthy) {
      // Source: vvaharness/report/appcontext.py:143-143
      End this invocation with True.
    }
  }
  // Source: vvaharness/report/appcontext.py:144-144
  End this invocation with normalize_app_id(x.parent_app_id) != normalize_app_id(y.parent_app_id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:147-204
// Source signature: load_cmdb_csv(path: str) -> dict[str, AppInfo]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_cmdb_csv(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:148-148
  In source order: For out, assign {}; source annotation dict[str, AppInfo].
  // Source: vvaharness/report/appcontext.py:149-150
  if (the source predicate not path or not os.path.isfile(path) is truthy) {
    // Source: vvaharness/report/appcontext.py:150-150
    End this invocation with out.
  }
  // Source: vvaharness/report/appcontext.py:151-203
  Enter source context managers left-to-right: open(path, newline='', encoding='utf-8-sig', errors='replace') bound to fh {
    // Source: vvaharness/report/appcontext.py:152-154
    In source order: Evaluate once csv.reader(fh); assign in source target order to reader. Then Evaluate once None; assign in source target order to header.
    // Source: vvaharness/report/appcontext.py:155-162
    for each row in reader {
      // Source: vvaharness/report/appcontext.py:156-157
      if (the source predicate not row is truthy) {
        // Source: vvaharness/report/appcontext.py:157-157
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/report/appcontext.py:158-158
      In source order: Evaluate once (row[0] or '').lstrip(); assign in source target order to first.
      // Source: vvaharness/report/appcontext.py:159-160
      if (the source predicate first.startswith('#') or not any(((c or '').strip() for c in row)) is truthy) {
        // Source: vvaharness/report/appcontext.py:160-160
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/report/appcontext.py:161-161
      In source order: Evaluate once row; assign in source target order to header.
      // Source: vvaharness/report/appcontext.py:162-162
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vvaharness/report/appcontext.py:163-164
    if (the source predicate header is None is truthy) {
      // Source: vvaharness/report/appcontext.py:164-164
      End this invocation with out.
    }
    // Source: vvaharness/report/appcontext.py:165-169
    In source order: Evaluate once {h.strip().lower(): i for i, h in enumerate(header)}; assign in source target order to hdr. Then Evaluate once _csv_col(hdr, 'id'); assign in source target order to i_id. Then Evaluate once _csv_col(hdr, 'name'); assign in source target order to i_name. Then Evaluate once _csv_col(hdr, 'externally_facing'); assign in source target order to i_ext. Then Evaluate once _csv_col(hdr, 'pci'); assign in source target order to i_pci.
    // Source: vvaharness/report/appcontext.py:170-172
    In source order: Evaluate once _csv_col(hdr, 'pan'); assign in source target order to i_pan. Then Evaluate once _csv_col(hdr, 'pii'); assign in source target order to i_pii. Then Evaluate once _csv_col(hdr, 'parent_id'); assign in source target order to i_par.
    // Source: vvaharness/report/appcontext.py:173-174
    if (the source predicate i_id < 0 is truthy) {
      // Source: vvaharness/report/appcontext.py:174-174
      Raise ValueError(source_template_174_29).
    }
    // Source: vvaharness/report/appcontext.py:176-177
    // Source signature: at(row, i)
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn at(row, i) {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/report/appcontext.py:177-177
      End this invocation with row[i] if 0 <= i < len(row) else None.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/report/appcontext.py:179-203
    for each row in reader {
      // Source: vvaharness/report/appcontext.py:180-180
      In source order: Evaluate once at(row, i_id); assign in source target order to rid.
      // Source: vvaharness/report/appcontext.py:181-182
      if (the source predicate not rid or not rid.strip() is truthy) {
        // Source: vvaharness/report/appcontext.py:182-182
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/report/appcontext.py:183-188
      In source order: Evaluate once AppInfo(); assign in source target order to a. Then Evaluate once rid.strip(); assign in source target order to a.id. Then Evaluate once at(row, i_name) or ''; assign in source target order to a.name. Then Evaluate once _nz(at(row, i_ext)); assign in source target order to a.ext_raw. Then Evaluate once _nz(at(row, i_pci)); assign in source target order to a.pci_raw.
      // Source: vvaharness/report/appcontext.py:189-193
      In source order: Evaluate once _nz(at(row, i_pan)); assign in source target order to a.pan_raw. Then Evaluate once _nz(at(row, i_pii)); assign in source target order to a.pii_raw. Then Evaluate once _yes(a.ext_raw); assign in source target order to a.externally_facing. Then Evaluate once _yes(a.pci_raw); assign in source target order to a.pci_scoped. Then Evaluate once _yes(a.pan_raw); assign in source target order to a.processes_pan.
      // Source: vvaharness/report/appcontext.py:194-197
      In source order: Evaluate once _yes(a.pii_raw); assign in source target order to a.pii. Then Evaluate once _nz(at(row, i_par)); assign in source target order to a.parent_app_id. Then Evaluate once normalize_app_id(a.id); assign in source target order to key. Then Evaluate once out.get(key); assign in source target order to prior.
      // Source: vvaharness/report/appcontext.py:198-202
      if (the source predicate prior is not None and _cmdb_enrichment_differs(prior, a) is truthy) {
        // Source: vvaharness/report/appcontext.py:200-202
        In source order: Evaluate log.warning(Event.APPCONTEXT_KEY_COLLISION, app_id=a.id, key=key, prior_id=prior.id, prior=prior.env_summary(), current=a.env_summary(), remedy='disambiguate the CMDB to avoid severity-enrichment drift'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/report/appcontext.py:203-203
      In source order: Evaluate once a; assign in source target order to out[key].
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/report/appcontext.py:204-204
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:207-213
// Source signature: _pick(own: AppInfo | None, parent: AppInfo | None, raw: str, val: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pick(own, parent, raw, val) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:209-210
  if (the source predicate own is not None and getattr(own, raw) is not None is truthy) {
    // Source: vvaharness/report/appcontext.py:210-210
    End this invocation with getattr(own, val).
  }
  // Source: vvaharness/report/appcontext.py:211-212
  if (the source predicate parent is not None is truthy) {
    // Source: vvaharness/report/appcontext.py:212-212
    End this invocation with getattr(parent, val).
  }
  // Source: vvaharness/report/appcontext.py:213-213
  End this invocation with own is not None and getattr(own, val).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:216-227
// Source signature: _merge_with_parent(base: AppInfo, own: AppInfo | None, parent: AppInfo | None, source: str) -> AppInfo
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _merge_with_parent(base, own, parent, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:218-222
  In source order: Evaluate once AppInfo(); assign in source target order to r. Then Evaluate once base.id; assign in source target order to r.id. Then Evaluate once base.name; assign in source target order to r.name. Then Evaluate once own.parent_app_id if own else base.parent_app_id; assign in source target order to r.parent_app_id. Then Evaluate once source; assign in source target order to r.source.
  // Source: vvaharness/report/appcontext.py:223-226
  In source order: Evaluate once _pick(own, parent, 'ext_raw', 'externally_facing'); assign in source target order to r.externally_facing. Then Evaluate once _pick(own, parent, 'pci_raw', 'pci_scoped'); assign in source target order to r.pci_scoped. Then Evaluate once _pick(own, parent, 'pan_raw', 'processes_pan'); assign in source target order to r.processes_pan. Then Evaluate once _pick(own, parent, 'pii_raw', 'pii'); assign in source target order to r.pii.
  // Source: vvaharness/report/appcontext.py:227-227
  End this invocation with r.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:230-254
// Source signature: lookup_app(app_id: str, cmdb: dict[str, AppInfo], cmdb_comp: dict[str, AppInfo]) -> AppInfo | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn lookup_app(app_id, cmdb, cmdb_comp) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:232-233
  if (the source predicate not app_id is truthy) {
    // Source: vvaharness/report/appcontext.py:233-233
    End this invocation with None.
  }
  // Source: vvaharness/report/appcontext.py:234-236
  In source order: Evaluate once normalize_app_id(app_id); assign in source target order to key. Then Evaluate once cmdb.get(key); assign in source target order to a. Then Evaluate once cmdb_comp.get(key); assign in source target order to c.
  // Source: vvaharness/report/appcontext.py:238-247
  if (the source predicate a is not None is truthy) {
    // Source: vvaharness/report/appcontext.py:239-241
    In source order: Evaluate once a.pci_raw is None or a.pan_raw is None or a.pii_raw is None or (a.ext_raw is None); assign in source target order to any_blank. Then Evaluate once a.parent_app_id or (c.parent_app_id if c else None); assign in source target order to parent_id.
    // Source: vvaharness/report/appcontext.py:242-245
    if (the source predicate any_blank and parent_id is truthy) {
      // Source: vvaharness/report/appcontext.py:243-243
      In source order: Evaluate once cmdb.get(normalize_app_id(parent_id)); assign in source target order to p.
      // Source: vvaharness/report/appcontext.py:244-245
      if (the source predicate p and normalize_app_id(p.id) != key is truthy) {
        // Source: vvaharness/report/appcontext.py:245-245
        End this invocation with _merge_with_parent(a, a, p, source_template_245_51).
      }
    }
    // Source: vvaharness/report/appcontext.py:246-246
    In source order: Evaluate once 'application'; assign in source target order to a.source.
    // Source: vvaharness/report/appcontext.py:247-247
    End this invocation with a.
  }
  // Source: vvaharness/report/appcontext.py:249-250
  if (the source predicate c is None is truthy) {
    // Source: vvaharness/report/appcontext.py:250-250
    End this invocation with None.
  }
  // Source: vvaharness/report/appcontext.py:251-251
  In source order: Evaluate once cmdb.get(normalize_app_id(c.parent_app_id)) if c.parent_app_id else None; assign in source target order to p.
  // Source: vvaharness/report/appcontext.py:252-254
  End this invocation with _merge_with_parent(c, c, p, source_template_253_17 if p else 'component').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:258-264
// Source signature: parse_vector(vector: str) -> dict[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn parse_vector(vector) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:259-259
  In source order: For m, assign {}; source annotation dict[str, str].
  // Source: vvaharness/report/appcontext.py:260-263
  for each part in vector.split('/') {
    // Source: vvaharness/report/appcontext.py:261-263
    if (the source predicate ':' in part is truthy) {
      // Source: vvaharness/report/appcontext.py:262-263
      In source order: Evaluate once part.split(':', 1); assign in source target order to (k, v). Then Evaluate once v.strip().upper(); assign in source target order to m[k.strip().upper()].
    }
  }
  // Source: vvaharness/report/appcontext.py:264-264
  End this invocation with m.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:268-271
// Source: vvaharness/report/appcontext.py:267-267
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vvaharness/report/appcontext.py:268-271
interface VsvsResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/report/appcontext.py:269-271
  In source order: For vector, declare without assigning a value; source annotation str. Then For score, declare without assigning a value; source annotation float. Then For rating, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/report/appcontext.py:274-277
// Source signature: _env_vector(base: str, mav: str, app: AppInfo) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _env_vector(base, mav, app) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:275-275
  In source order: Evaluate once base if base.startswith('CVSS:') else source_template_275_51; assign in source target order to prefix.
  // Source: vvaharness/report/appcontext.py:276-277
  End this invocation with source_template_276_12.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:280-310
// Source signature: vsvs_score(base_vector: str | None, app: AppInfo | None) -> VsvsResult | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn vsvs_score(base_vector, app) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:281-282
  if (the source predicate not base_vector or app is None is truthy) {
    // Source: vvaharness/report/appcontext.py:282-282
    End this invocation with None.
  }
  // Source: vvaharness/report/appcontext.py:283-285
  In source order: Evaluate once parse_vector(base_vector); assign in source target order to m. Then Evaluate once (m.get('AV'), m.get('AC'), m.get('PR'), m.get('UI')); assign in source target order to (av, ac, pr, ui). Then Evaluate once (m.get('S'), m.get('C'), m.get('I'), m.get('A')); assign in source target order to (s, c, i, a).
  // Source: vvaharness/report/appcontext.py:286-287
  if (the source predicate None in (av, ac, pr, ui, s, c, i, a) is truthy) {
    // Source: vvaharness/report/appcontext.py:287-287
    End this invocation with None.
  }
  // Source: vvaharness/report/appcontext.py:288-293
  In source order: Evaluate once app.mav(av); assign in source target order to mav. Then Evaluate once s == 'C'; assign in source target order to scope_changed. Then Evaluate once cvss.AV.get(mav, cvss.NO_SCORE); assign in source target order to mav_v. Then Evaluate once cvss.AC.get(ac, cvss.NO_SCORE); assign in source target order to ac_v. Then Evaluate once (cvss.PR_SCOPE_CHANGED if scope_changed else cvss.PR_SCOPE_UNCHANGED).get(pr, cvss.NO_SCORE); assign in source target order to pr_v.
  // Source: vvaharness/report/appcontext.py:294-297
  In source order: Evaluate once cvss.UI.get(ui, cvss.NO_SCORE); assign in source target order to ui_v. Then Evaluate once (cvss.CIA.get(x, cvss.NO_SCORE) for x in (c, i, a)); assign in source target order to (c_v, i_v, a_v). Then Evaluate once (cvss.REQ.get(x, cvss.NEUTRAL_WEIGHT) for x in (app.cr(), app.ir(), app.ar())); assign in source target order to (cr_v, ir_v, ar_v).
  // Source: vvaharness/report/appcontext.py:298-299
  if (the source predicate min(mav_v, ac_v, pr_v, ui_v, c_v, i_v, a_v) < 0 is truthy) {
    // Source: vvaharness/report/appcontext.py:299-299
    End this invocation with None.
  }
  // Source: vvaharness/report/appcontext.py:300-304
  In source order: Evaluate once cvss.EXPLOIT_MATURITY.get(SAST_E, cvss.NEUTRAL_WEIGHT); assign in source target order to e_v. Then Evaluate once cvss.REMEDIATION_LEVEL.get(SAST_RL, cvss.NEUTRAL_WEIGHT); assign in source target order to rl_v. Then Evaluate once cvss.REPORT_CONFIDENCE.get(SAST_RC, cvss.NEUTRAL_WEIGHT); assign in source target order to rc_v. Then Evaluate once min(1 - (1 - cr_v * c_v) * (1 - ir_v * i_v) * (1 - ar_v * a_v), cvss.MISS_CAP); assign in source target order to miss. Then Evaluate once cvss.modified_impact(miss, scope_changed); assign in source target order to m_impact.
  // Source: vvaharness/report/appcontext.py:305-306
  if (the source predicate m_impact <= 0 is truthy) {
    // Source: vvaharness/report/appcontext.py:306-306
    End this invocation with VsvsResult(_env_vector(base_vector, mav, app), 0.0, 'None').
  }
  // Source: vvaharness/report/appcontext.py:307-309
  In source order: Evaluate once cvss.EXPLOITABILITY_COEFF * mav_v * ac_v * pr_v * ui_v; assign in source target order to m_exploit. Then Evaluate once cvss.combine(m_impact, m_exploit, scope_changed); assign in source target order to mod_base. Then Evaluate once cvss.roundup1(mod_base * e_v * rl_v * rc_v); assign in source target order to env.
  // Source: vvaharness/report/appcontext.py:310-310
  End this invocation with VsvsResult(_env_vector(base_vector, mav, app), env, cvss.rating(env)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:314-315
// Source signature: _contains_any(haystack: str, needles) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _contains_any(haystack, needles) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:315-315
  End this invocation with any((n in haystack for n in needles)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/appcontext.py:318-384
// Source signature: offensive_priority_for(title: str, category: str | None, description: str, cvss_vector: str | None, app: AppInfo | None) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn offensive_priority_for(title, category, description, cvss_vector, app) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/appcontext.py:321-325
  In source order: Retain source documentation literal source_literal_321_4; it is not a model call. Then Evaluate once ' '.join((x or '' for x in (title, category, description))).lower(); assign in source target order to body. Then Evaluate once parse_vector(cvss_vector) if cvss_vector else {}; assign in source target order to v. Then Evaluate once v.get('AV', 'N'); assign in source target order to av. Then Evaluate once v.get('PR', 'L'); assign in source target order to pr.
  // Source: vvaharness/report/appcontext.py:326-333
  In source order: Evaluate once 'PR' in v; assign in source target order to pr_explicit. Then Evaluate once v.get('AC', 'L'); assign in source target order to ac. Then Evaluate once app is not None and app.externally_facing; assign in source target order to cmdb_external. Then Evaluate once app is not None and (not app.externally_facing); assign in source target order to cmdb_internal. Then Evaluate once _contains_any(body, KW_CODE_KNOWLEDGE) or (category and 'hardcoded' in category.lower()); assign in source target order to code_knowledge.
  // Source: vvaharness/report/appcontext.py:334-342
  In source order: Evaluate once cmdb_internal or av in ('A', 'L', 'P') or _contains_any(body, KW_INTERNAL); assign in source target order to internal_net. Then Evaluate once pr == 'H' or _contains_any(body, KW_HIGH_PRIV); assign in source target order to high_priv. Then Evaluate once pr == 'L' or _contains_any(body, KW_OBTAINABLE_AUTH); assign in source target order to obtainable_auth. Then Evaluate once pr_explicit and pr in ('L', 'H'); assign in source target order to pr_requires_auth. Then Evaluate once not pr_requires_auth and (_contains_any(body, KW_NO_AUTH) or (pr == 'N' and (not obtainable_auth) and (not high_priv))); assign in source target order to no_auth.
  // Source: vvaharness/report/appcontext.py:343-346
  In source order: Evaluate once av == 'N' and (not internal_net) and cmdb_external; assign in source target order to internet_reachable. Then Evaluate once app is None and av == 'N' and (not internal_net); assign in source target order to exposure_unknown. Then For why, assign []; source annotation list[str].
  // Source: vvaharness/report/appcontext.py:347-379
  if (the source predicate code_knowledge is truthy) {
    // Source: vvaharness/report/appcontext.py:348-349
    In source order: Evaluate once 'P4'; assign in source target order to prio. Then Evaluate why.append('requires source-code / insider knowledge'); retain side effects and discard the expression result.
    // Source: vvaharness/report/appcontext.py:350-353
    if (the source predicate cmdb_internal is truthy) {
      // Source: vvaharness/report/appcontext.py:351-351
      In source order: Evaluate why.append('app not externally facing (CMDB)'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/report/appcontext.py:352-353
      if (the source predicate av != 'N' is truthy) {
        // Source: vvaharness/report/appcontext.py:353-353
        In source order: Evaluate why.append(source_template_353_23); retain side effects and discard the expression result.
      }
    }
  }
  else {
    // Source: vvaharness/report/appcontext.py:354-379
    if (the source predicate exposure_unknown and (not high_priv) is truthy) {
      // Source: vvaharness/report/appcontext.py:355-357
      In source order: Evaluate once 'P3'; assign in source target order to prio. Then Evaluate why.append('exposure unverified — no CMDB context'); retain side effects and discard the expression result. Then Evaluate why.append(source_template_357_19); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/report/appcontext.py:358-379
      if (the source predicate not internet_reachable or high_priv is truthy) {
        // Source: vvaharness/report/appcontext.py:359-359
        In source order: Evaluate once 'P3'; assign in source target order to prio.
        // Source: vvaharness/report/appcontext.py:360-365
        if (the source predicate cmdb_internal is truthy) {
          // Source: vvaharness/report/appcontext.py:361-361
          In source order: Evaluate why.append('app not externally facing (CMDB)'); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/report/appcontext.py:362-365
          if (the source predicate av != 'N' is truthy) {
            // Source: vvaharness/report/appcontext.py:363-363
            In source order: Evaluate why.append(source_template_363_23); retain side effects and discard the expression result.
          }
          else {
            // Source: vvaharness/report/appcontext.py:364-365
            if (the source predicate internal_net is truthy) {
              // Source: vvaharness/report/appcontext.py:365-365
              In source order: Evaluate why.append('internal-network position required'); retain side effects and discard the expression result.
            }
          }
        }
        // Source: vvaharness/report/appcontext.py:366-368
        if (the source predicate high_priv is truthy) {
          // Source: vvaharness/report/appcontext.py:367-368
          In source order: Evaluate why.append('PR:H - high-privilege auth required' if pr == 'H' else 'admin/privileged role required'); retain side effects and discard the expression result.
        }
        // Source: vvaharness/report/appcontext.py:369-370
        if (the source predicate not why is truthy) {
          // Source: vvaharness/report/appcontext.py:370-370
          In source order: Evaluate why.append('internal network / privileged position required'); retain side effects and discard the expression result.
        }
      }
      else {
        // Source: vvaharness/report/appcontext.py:371-379
        if (the source predicate no_auth is truthy) {
          // Source: vvaharness/report/appcontext.py:372-375
          In source order: Evaluate once 'P1'; assign in source target order to prio. Then Evaluate why.append('internet-facing' + (' (CMDB)' if cmdb_external else '')); retain side effects and discard the expression result. Then Evaluate why.append(source_template_374_19 + (source_template_375_22 if pr_explicit else '')); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/report/appcontext.py:377-379
          In source order: Evaluate once 'P2'; assign in source target order to prio. Then Evaluate why.append('internet-facing' + (' (CMDB)' if cmdb_external else '')); retain side effects and discard the expression result. Then Evaluate why.append(source_template_379_19); retain side effects and discard the expression result.
        }
      }
    }
  }
  // Source: vvaharness/report/appcontext.py:381-382
  if (the source predicate ac == 'H' and prio in ('P1', 'P2') is truthy) {
    // Source: vvaharness/report/appcontext.py:382-382
    In source order: Evaluate why.append('AC:H - complex preconditions'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/report/appcontext.py:384-384
  End this invocation with (prio, '; '.join(why)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.report import cvss` at source line 25: `source_detail/vvaharness/report/__init__.py.sudo.md`.
- `from vvaharness.report import cvss` at source line 25: `source_detail/vvaharness/report/cvss.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 26: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/report/appcontext.py.sudo.md). Exact strings in the evidence asset support this conversion.
