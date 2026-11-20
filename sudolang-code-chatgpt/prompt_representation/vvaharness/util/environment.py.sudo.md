# vvaharness/util/environment.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## langsmith_tracing_check — source lines 345–349

Source context: callable `langsmith_tracing_check`; enclosing call `Check`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `gate; conversion=none; format_spec=none`
- `key_note; conversion=none; format_spec=none`
- `gate; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/util/environment.py:345-349
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: gate; conversion=none; format_spec=none]=true — every model prompt (which contains scanned repository source) and every completion will be sent to the LangSmith service, a third-party egress channel this tool does not otherwise use.[dynamic source value: key_note; conversion=none; format_spec=none] Unset [dynamic source value: gate; conversion=none; format_spec=none] unless the model are deliberately tracing in an isolated lab.
}
```

## client_tls_check — source lines 863–867

Source context: callable `client_tls_check`; enclosing call `Check`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `host; conversion=none; format_spec=none`
- `port; conversion=none; format_spec=none`
- `source; conversion=none; format_spec=none`
- `node_ca; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/util/environment.py:863-867
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: host; conversion=none; format_spec=none]:[dynamic source value: port; conversion=none; format_spec=none] is rejected by the trust via:sdk and deepagents-Anthropic use ([dynamic source value: source; conversion=none; format_spec=none]) but accepted with NODE_EXTRA_CA_CERTS, which only via:cli reads — scan preflight will fail with a certificate-verification error.
  The request retains this source rule, criterion or rationale, with its original modal force: Fix: export SSL_CERT_FILE=[dynamic source value: node_ca; conversion=none; format_spec=none] (or set sdk.ca_cert / ANTHROPIC_SDK_CA_CERT). SSL_CERT_FILE replaces the default trust, so the bundle must hold every root the model need.
}
```

## _gateway_check — source lines 362–366

Source context: callable `_gateway_check`; enclosing call `Check`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/util/environment.py:362-366
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ANTHROPIC_API_KEY looks like a gateway/Claude-Code token (eyJ…) but ANTHROPIC_BASE_URL is unset — it will 401 against the public API.
  The request retains this source rule, criterion or rationale, with its original modal force: Set ANTHROPIC_BASE_URL to the model's gateway (and SSL_CERT_FILE — or sdk.ca_cert in the profile — if it needs a private CA).
}
```

## _applied_overlay_check — source lines 457–457

Source context: callable `_applied_overlay_check`; enclosing call `Check`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `local; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/util/environment.py:457-457
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: local; conversion=none; format_spec=none] must be a YAML mapping
}
```

## src — source lines 763–765

Source context: callable `tls_check`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/util/environment.py:763-765
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: via NODE_EXTRA_CA_CERTS (the trust via:cli reads) — note: via:sdk and deepagents-Anthropic do not read that variable; they use the OS trust store, or SSL_CERT_FILE / sdk.ca_cert when set
}
```

## hint — source lines 777–779

Source context: callable `tls_check`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/util/environment.py:777-779
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Point SSL_CERT_FILE at the model's org's CA bundle (covers via:sdk and via:deepagents; via:cli reads NODE_EXTRA_CA_CERTS instead).
}
```

## tls_check — source lines 781–784

Source context: callable `tls_check`; enclosing call `Check`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `host; conversion=none; format_spec=none`
- `hint; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/util/environment.py:781-784
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: host; conversion=none; format_spec=none] presents a certificate the system trust store does not accept — this machine reaches it through a private CA (a TLS-intercepting proxy or a private endpoint), so the model need the model's org's CA bundle.[dynamic source value: hint; conversion=none; format_spec=none]
}
```

## client_tls_check — source lines 857–860

Source context: callable `client_tls_check`; enclosing call `Check`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `host; conversion=none; format_spec=none`
- `port; conversion=none; format_spec=none`
- `source; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/util/environment.py:857-860
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: host; conversion=none; format_spec=none]:[dynamic source value: port; conversion=none; format_spec=none] is rejected by the trust via:sdk and deepagents-Anthropic use ([dynamic source value: source; conversion=none; format_spec=none]); set SSL_CERT_FILE (or sdk.ca_cert) to the model's org's CA bundle — scan preflight will fail with a certificate-verification error until then
}
```

## check — source lines 476–478

Source context: callable `overlay_check`; enclosing call `Check`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):

- `local; conversion=none; format_spec=none`
- `NO_LOCAL_CONFIG_ENV; conversion=none; format_spec=none`

```sudo
// Source: vvaharness/util/environment.py:476-478
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: [dynamic source value: local; conversion=none; format_spec=none] untrusted — must be owned by the invoking user (or root) and not group/world-writable; `chmod go-w` / `chown` it, or set [dynamic source value: NO_LOCAL_CONFIG_ENV; conversion=none; format_spec=none] to skip it
}
```

