# vvaharness/skills/ssrf/probe.sh — model-visible probe feedback

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

```sudo
// Source: vvaharness/skills/ssrf/probe.sh:130-130
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: == DECLARED HTTP-CLIENT DEPENDENCIES (absence NEVER refutes a fetch sink) ==
}
```

```sudo
// Source: vvaharness/skills/ssrf/probe.sh:147-151
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: == REFERENCE: bypasses to name against any host check or deny-list above == decimal 2130706433 | octal 0177.0.0.1 | hex 0x7f.1 | short 127.1 | IPv4-mapped [::ffff:127.0.0.1] | [::] credentials prefix http://allowed.com@169.254.169.254/ | trailing dot metadata.google.internal. mixed-case scheme HTTP:// FiLe:// | attacker DNS resolving private 127.0.0.1.nip.io percent-encoded or IDN host | fragment trick http://evil/#@169.254.169.254/
}
```

```sudo
// Source: vvaharness/skills/ssrf/probe.sh:153-156
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: == REFERENCE: redirect following (the allow-list must re-run on EVERY hop) == on by default: requests allow_redirects=True | urllib urlopen | JS fetch | OkHttp followRedirects off, commonly switched on: httpx follow_redirects=True | HttpClient.Builder.followRedirects(ALWAYS) | PHP CURLOPT_FOLLOWLOCATION an allowed host that 302s to 169.254.169.254 wins unless every hop is re-checked
}
```

```sudo
// Source: vvaharness/skills/ssrf/probe.sh:158-161
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: == REFERENCE: check-then-fetch races (TOCTOU / DNS rebinding) == a getaddrinfo / gethostbyname / InetAddress.getByName check followed by a fetch on the original string resolves twice and can see a different address the second time - same defect when code inspects urlparse(...).hostname or new URL(s).hostname but hands the raw string to the client
}
```

```sudo
// Source: vvaharness/skills/ssrf/probe.sh:163-168
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: == REFERENCE: internal targets to name, highest impact first == metadata (credential theft): 169.254.169.254/latest/meta-data/iam/security-credentials/ (AWS) metadata.google.internal + header Metadata-Flavor: Google | 169.254.169.254/metadata/instance + Metadata: true (Azure) | 100.100.200.200 (Alibaba) private space: localhost 127.x.x.x ::1 0.0.0.0 | 10/8 172.16/12 192.168/16 169.254/16 | *.internal *.local *.svc.cluster.local | unqualified names via search domains admin ports: 2375 docker | 6379 redis | 9200 elasticsearch | 8500 consul | 10250 kubelet | 5432 3306 db | 15672 rabbit | 9090 prometheus schemes: file:///etc/passwd | gopher:// crafted TCP to redis/smtp | dict:// | ftp:// | ldap:// | jar: netdoc: in Java
}
```

