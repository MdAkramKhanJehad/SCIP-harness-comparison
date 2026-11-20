# vvaharness/rules/generic.kb.yaml — supplied guidance and request data

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## entries.0.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:25-25
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: user input, request params, form fields, query strings
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sources.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:26-26
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: path params, headers, JSON bodies, cookies
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:28-28
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: string-built SQL passed to execute/query/update
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sinks.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:29-29
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: dynamic SQL fragments used for table, column, or ORDER BY names
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sinks.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:30-30
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: python: cursor.execute
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sinks.3

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:31-31
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: java: Statement.executeQuery
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:33-33
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: Parameterized queries / prepared statements
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:34-34
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: java: PreparedStatement
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.sanitizers.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:35-35
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: server-side allow-lists for dynamic identifiers
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:37-37
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: manual escaping
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:38-38
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: regex blacklists for SQL keywords
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:40-40
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: taint reaches a bound parameter value, not the SQL string
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.0.fp_checks.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-89` — SQL Injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:41-41
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: query is fully static and only values are interpolated via binds
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:47-47
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: user input, argv/env, request params, config values
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:49-49
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: shell invocation, Runtime.exec, Process.Start, child_process.exec
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.sinks.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:50-50
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: any string passed to a shell or eval-style command runner
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:52-52
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: argv-array execution with shell disabled
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:53-53
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: strict allow-list of commands and arguments
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:55-55
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: quoting only
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:56-56
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: blocking punctuation characters
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.1.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-78` — OWASP A03 Injection: command execution. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:58-58
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: command is constant and arguments are not attacker-controlled
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:64-64
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: HTTP input, comments, markdown, profiles, stored text
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:66-66
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: innerHTML, document.write, render_template_string, res.send(html)
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.sinks.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:67-67
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: template raw blocks, safe markers, triple-stache, Markup()
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:69-69
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: context-aware HTML encoding
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:70-70
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: template auto-escape that stays enabled end-to-end
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:72-72
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: strip_tags
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:73-73
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: URL encoding
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.non_sanitizers.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:74-74
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: JSON serialization
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.2.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-79` — OWASP A03 Injection: HTML / template output. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:76-76
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: sink is textContent / innerText / JSON response
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:82-82
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: user-supplied filename, path, archive member, upload name
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:84-84
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: open/read/write/delete/sendFile/serveFile on attacker-influenced paths
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:86-86
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: canonicalize then verify inside a fixed base directory
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:87-87
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: server-side id to path mapping with no raw path joins
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:89-89
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: basename alone
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:90-90
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: single ../ replacement
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.non_sanitizers.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:91-91
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: prefix check before resolve
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.3.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 Broken Access Control: path traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:93-93
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: path is constant or fully server-derived
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.4.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-918` — OWASP A10 SSRF: server-side URL fetch. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:99-99
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: user URL, webhook target, callback URL, redirect URL
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.4.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-918` — OWASP A10 SSRF: server-side URL fetch. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:101-101
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: requests/fetch/HttpClient/curl/file_get_contents on remote URLs
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.4.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-918` — OWASP A10 SSRF: server-side URL fetch. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:103-103
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: host allow-list after DNS resolution
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.4.sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-918` — OWASP A10 SSRF: server-side URL fetch. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:104-104
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: private-range and loopback blocking on every hop
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.4.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-918` — OWASP A10 SSRF: server-side URL fetch. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:106-106
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: scheme allow-list only
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.4.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-918` — OWASP A10 SSRF: server-side URL fetch. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:107-107
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: string prefix checks on hosts
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.4.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-918` — OWASP A10 SSRF: server-side URL fetch. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:109-109
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: URL is fixed or drawn from a trusted allow-list
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:115-115
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: untrusted blob, file, message, cookie, session payload
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:117-117
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: pickle.loads, ObjectInputStream.readObject, BinaryFormatter.Deserialize
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.sinks.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:118-118
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: YAML/native object loaders that execute constructors or gadgets
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:120-120
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: safe_load / data-only parsing
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:121-121
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: class allow-list filters before object creation
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:123-123
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: signature check after deserialization
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:124-124
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: class-name blacklists
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.5.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-502` — OWASP A08 Software / data integrity: unsafe deserialization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:126-126
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: input is immutable trusted data and cannot be attacker-writable
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.6.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-611` — OWASP A08 software integrity: XML external entity expansion. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:132-132
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: XML input from request, file, message, or partner system
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.6.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-611` — OWASP A08 software integrity: XML external entity expansion. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:134-134
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: XML parsers with DTD/entity resolution enabled
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.6.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-611` — OWASP A08 software integrity: XML external entity expansion. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:136-136
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: disable DTDs and external entities before parsing
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.6.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-611` — OWASP A08 software integrity: XML external entity expansion. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:138-138
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: post-parse exception handling
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.6.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-611` — OWASP A08 software integrity: XML external entity expansion. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:139-139
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: schema validation alone
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.6.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-611` — OWASP A08 software integrity: XML external entity expansion. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:141-141
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: defused XML parser or equivalent hardened factory is used
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.7.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-601` — OWASP A01 Broken Access Control: open redirect. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:147-147
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: next, returnUrl, redirect, callback, destination parameters
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.7.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-601` — OWASP A01 Broken Access Control: open redirect. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:149-149
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: response redirects and client-side navigation sinks
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.7.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-601` — OWASP A01 Broken Access Control: open redirect. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:151-151
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: relative-path allow-list or exact host allow-list
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.7.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-601` — OWASP A01 Broken Access Control: open redirect. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:153-153
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: startswith('/')
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.7.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-601` — OWASP A01 Broken Access Control: open redirect. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:154-154
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: substring host checks
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.7.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-601` — OWASP A01 Broken Access Control: open redirect. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:156-156
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: redirect target is fully server constant
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.8.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 logging / monitoring: log injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:162-162
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: user-controlled strings, headers, stack traces, request bodies
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.8.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 logging / monitoring: log injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:164-164
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: raw log lines, audit events, CSV export of logs
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.8.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 logging / monitoring: log injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:166-166
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: structured logging with escaping or field separation
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.8.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 logging / monitoring: log injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:168-168
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: trimming
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.8.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 logging / monitoring: log injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:169-169
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: length checks
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.8.non_sanitizers.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 logging / monitoring: log injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:170-170
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: removing a few delimiters
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.8.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 logging / monitoring: log injection. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:172-172
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: output is structured and encoded before log emission
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.9.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-352` — OWASP A01 / session integrity: CSRF on state-changing actions. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:178-178
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: browser-originated requests, forms, fetches, cookies
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.9.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-352` — OWASP A01 / session integrity: CSRF on state-changing actions. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:180-180
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: state-changing endpoints without anti-CSRF verification
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.9.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-352` — OWASP A01 / session integrity: CSRF on state-changing actions. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:182-182
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: anti-CSRF token or same-site gate checked on every state change
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.9.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-352` — OWASP A01 / session integrity: CSRF on state-changing actions. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:184-184
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: custom header names only
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.9.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-352` — OWASP A01 / session integrity: CSRF on state-changing actions. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:185-185
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: Referer check alone
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.9.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-352` — OWASP A01 / session integrity: CSRF on state-changing actions. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:187-187
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: action is read-only or token is required and validated
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.10.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 authentication: missing auth check. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:193-193
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: public route, anonymous request, unauthenticated job trigger
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.10.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 authentication: missing auth check. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:195-195
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: privileged endpoint or command without authentication gate
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.10.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 authentication: missing auth check. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:197-197
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: authentication required before the sensitive action
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.10.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 authentication: missing auth check. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:199-199
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: UI-only restriction
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.10.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 authentication: missing auth check. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:200-200
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: client-side gating
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.10.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 authentication: missing auth check. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:202-202
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: route is internal-only and unreachable from any external entry point
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.11.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-862` — OWASP A01 broken access control: missing authorization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:208-208
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: tenant id, object id, row id, account id, URL path id
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.11.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-862` — OWASP A01 broken access control: missing authorization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:210-210
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: object access without ownership / role / policy checks
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.11.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-862` — OWASP A01 broken access control: missing authorization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:212-212
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: server-side authorization check tied to the resource
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.11.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-862` — OWASP A01 broken access control: missing authorization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:214-214
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: hiding the id from the UI
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.11.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-862` — OWASP A01 broken access control: missing authorization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:215-215
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: guessable ids are not enough
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.11.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-862` — OWASP A01 broken access control: missing authorization. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:217-217
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: resource is global or intentionally public
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.12.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-639` — OWASP A01 broken access control: IDOR / object reference. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:223-223
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: object identifiers from request path, query, or body
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.12.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-639` — OWASP A01 broken access control: IDOR / object reference. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:225-225
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: fetch/update/delete of another user's object
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.12.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-639` — OWASP A01 broken access control: IDOR / object reference. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:227-227
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: ownership lookup against authenticated principal
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.12.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-639` — OWASP A01 broken access control: IDOR / object reference. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:229-229
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: UUIDs alone
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.12.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-639` — OWASP A01 broken access control: IDOR / object reference. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:230-230
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: random ids alone
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.12.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-639` — OWASP A01 broken access control: IDOR / object reference. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:232-232
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: identifier is scoped by server-side tenant context before use
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.13.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-20` — OWASP A04 insecure design: missing input validation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:238-238
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: any untrusted field crossing a trust boundary
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.13.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-20` — OWASP A04 insecure design: missing input validation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:240-240
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: security-sensitive business logic consuming unchecked input
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.13.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-20` — OWASP A04 insecure design: missing input validation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:242-242
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: strict type, range, format, and allow-list validation
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.13.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-20` — OWASP A04 insecure design: missing input validation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:244-244
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: null checks
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.13.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-20` — OWASP A04 insecure design: missing input validation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:245-245
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: length checks only
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.13.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-20` — OWASP A04 insecure design: missing input validation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:247-247
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: all attacker-controlled inputs are normalized and validated before use
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.14.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-327` — OWASP A02 cryptographic failures: weak or broken crypto. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:253-253
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: secrets, credentials, tokens, PII, payment data
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.14.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-327` — OWASP A02 cryptographic failures: weak or broken crypto. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:255-255
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: MD5/SHA1 for security, hard-coded IVs, obsolete protocols
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.14.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-327` — OWASP A02 cryptographic failures: weak or broken crypto. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:257-257
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: modern authenticated encryption and strong hash choices
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.14.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-327` — OWASP A02 cryptographic failures: weak or broken crypto. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:259-259
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: HMAC with weak hash
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.14.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-327` — OWASP A02 cryptographic failures: weak or broken crypto. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:260-260
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: password hashing with unsalted fast hash
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.14.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-327` — OWASP A02 cryptographic failures: weak or broken crypto. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:262-262
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: crypto is legacy-only and not used for security decisions
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.15.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-295` — OWASP A02 transport: TLS verification disabled. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:268-268
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: client configuration, deployment config, README instructions
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.15.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-295` — OWASP A02 transport: TLS verification disabled. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:270-270
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: verify=false, rejectUnauthorized=false, InsecureSkipVerify
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.15.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-295` — OWASP A02 transport: TLS verification disabled. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:272-272
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: TLS verification enabled with trusted CA / pinning policy
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.15.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-295` — OWASP A02 transport: TLS verification disabled. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:274-274
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: accepting any certificate
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.15.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-295` — OWASP A02 transport: TLS verification disabled. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:275-275
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: environmental trust without verification
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.15.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-295` — OWASP A02 transport: TLS verification disabled. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:277-277
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: dev-only harness or isolated test fixture that never ships
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.16.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-798` — OWASP A02 credentials: hardcoded secret or token. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:283-283
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: source code literals, checked-in configs, fixtures, docs
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.16.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-798` — OWASP A02 credentials: hardcoded secret or token. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:285-285
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: API keys, passwords, JWTs, private keys, cloud credentials
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.16.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-798` — OWASP A02 credentials: hardcoded secret or token. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:287-287
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: secret manager lookup or runtime injection from secure storage
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.16.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-798` — OWASP A02 credentials: hardcoded secret or token. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:289-289
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: base64 encoding
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.16.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-798` — OWASP A02 credentials: hardcoded secret or token. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:290-290
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: renaming the variable
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.16.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-798` — OWASP A02 credentials: hardcoded secret or token. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:292-292
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: string is clearly a non-secret placeholder or a public example token
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.17.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-434` — OWASP A05 misconfiguration: unrestricted file upload. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:298-298
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: user file uploads, multipart forms, drag-and-drop files
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.17.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-434` — OWASP A05 misconfiguration: unrestricted file upload. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:300-300
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: storage or execution of uploaded content without validation
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.17.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-434` — OWASP A05 misconfiguration: unrestricted file upload. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:302-302
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: type / extension / size allow-lists and safe storage outside web root
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.17.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-434` — OWASP A05 misconfiguration: unrestricted file upload. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:304-304
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: extension blacklists
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.17.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-434` — OWASP A05 misconfiguration: unrestricted file upload. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:305-305
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: MIME type alone
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.17.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-434` — OWASP A05 misconfiguration: unrestricted file upload. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:307-307
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: upload is converted to inert data or stored under a non-executable path
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.18.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-1333` — OWASP A04 availability: regex denial of service. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:313-313
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: attacker-controlled text evaluated by complex regex
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.18.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-1333` — OWASP A04 availability: regex denial of service. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:315-315
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: catastrophic-backtracking patterns in search / validation
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.18.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-1333` — OWASP A04 availability: regex denial of service. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:317-317
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: linear-time regex or bounded matching with input limits
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.18.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-1333` — OWASP A04 availability: regex denial of service. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:319-319
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: short-circuit checks that still leave the bad regex path
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.18.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-1333` — OWASP A04 availability: regex denial of service. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:321-321
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: pattern is precompiled and not evaluated on attacker-controlled length
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.19.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-400` — OWASP A04 availability: unbounded resource consumption. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:327-327
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: user-controlled pagination, loops, recursion, batch size, uploads
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.19.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-400` — OWASP A04 availability: unbounded resource consumption. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:329-329
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: CPU / memory / disk amplification without hard caps
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.19.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-400` — OWASP A04 availability: unbounded resource consumption. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:331-331
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: server-side quotas, paging limits, timeouts, and bounded queues
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.19.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-400` — OWASP A04 availability: unbounded resource consumption. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:333-333
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: client hints
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.19.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-400` — OWASP A04 availability: unbounded resource consumption. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:334-334
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: best-effort throttling
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.19.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-400` — OWASP A04 availability: unbounded resource consumption. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:336-336
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: resource use is bounded by server-enforced limits
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.20.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-94` — OWASP A03 injection: code / expression evaluation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:342-342
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: template fragments, user expressions, rule text, scripts
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.20.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-94` — OWASP A03 injection: code / expression evaluation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:344-344
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: eval, exec, ScriptEngine, new Function, template eval
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.20.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-94` — OWASP A03 injection: code / expression evaluation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:346-346
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: literal allow-lists and sandboxed expression engines
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.20.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-94` — OWASP A03 injection: code / expression evaluation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:348-348
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: character stripping
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.20.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-94` — OWASP A03 injection: code / expression evaluation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:349-349
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: blacklists
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.20.non_sanitizers.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-94` — OWASP A03 injection: code / expression evaluation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:350-350
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: string concatenation
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.20.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-94` — OWASP A03 injection: code / expression evaluation. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:352-352
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: expression is fully authored by trusted code and never data-derived
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.21.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 observability: sensitive data in logs. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:358-358
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: PII, PAN, tokens, secrets, debug traces
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.21.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 observability: sensitive data in logs. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:360-360
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: logs, metrics tags, tracing spans, error telemetry
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.21.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 observability: sensitive data in logs. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:362-362
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: redaction before write, field-level masking, structured fields
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.21.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 observability: sensitive data in logs. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:364-364
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: manual truncation
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.21.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 observability: sensitive data in logs. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:365-365
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: suffix masking only
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.21.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-117` — OWASP A09 observability: sensitive data in logs. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:367-367
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: sensitive fields are redacted before emission
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.22.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-200` — OWASP A01 / A02 information exposure. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:373-373
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: stack traces, debug flags, config dumps, internal ids
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.22.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-200` — OWASP A01 / A02 information exposure. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:375-375
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: public responses, error pages, diagnostic endpoints
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.22.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-200` — OWASP A01 / A02 information exposure. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:377-377
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: least-information responses and internal-only diagnostics
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.22.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-200` — OWASP A01 / A02 information exposure. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:379-379
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: hiding the UI button
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.22.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-200` — OWASP A01 / A02 information exposure. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:380-380
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: client-side only protections
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.22.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-200` — OWASP A01 / A02 information exposure. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:382-382
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: response is explicitly internal and inaccessible to external actors
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.23.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 broken access control: archive / path member traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:388-388
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: zip member names, tar entries, upload names, import paths
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.23.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 broken access control: archive / path member traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:390-390
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: file extraction or access using raw member names
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.23.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 broken access control: archive / path member traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:392-392
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: member name normalization and base-dir checks
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.23.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 broken access control: archive / path member traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:394-394
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: single-pass replacement of '../'
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.23.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 broken access control: archive / path member traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:395-395
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: basename alone
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.23.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-22` — OWASP A01 broken access control: archive / path member traversal. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:397-397
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: archive members are validated against a fixed extraction root
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.24.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-269` — OWASP A01 privilege issue: over-privileged action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:403-403
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: privileged command, admin endpoint, service token, host OS action
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.24.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-269` — OWASP A01 privilege issue: over-privileged action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:405-405
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: write/delete/execute beyond the caller's privilege boundary
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.24.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-269` — OWASP A01 privilege issue: over-privileged action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:407-407
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: least-privilege execution / role enforcement / policy checks
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.24.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-269` — OWASP A01 privilege issue: over-privileged action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:409-409
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: UI hints
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.24.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-269` — OWASP A01 privilege issue: over-privileged action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:410-410
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: obscurity
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.24.non_sanitizers.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-269` — OWASP A01 privilege issue: over-privileged action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:411-411
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: self-declared role strings
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.24.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-269` — OWASP A01 privilege issue: over-privileged action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:413-413
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: operation is already confined to the caller's minimal privilege
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.25.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 auth: unauthenticated control plane action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:419-419
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: scheduler jobs, webhooks, admin APIs, CLI switches
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.25.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 auth: unauthenticated control plane action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:421-421
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: sensitive control plane operations without auth
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.25.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 auth: unauthenticated control plane action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:423-423
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: auth gate plus server-side permission check
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.25.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 auth: unauthenticated control plane action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:425-425
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: hidden routes
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.25.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 auth: unauthenticated control plane action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:426-426
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: unguarded localhost assumptions
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.25.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-306` — OWASP A07 auth: unauthenticated control plane action. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:428-428
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: endpoint is unreachable from any untrusted entry point
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.26.sources.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-326` — OWASP A02 cryptography: insufficient encryption strength. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sources` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:434-434
Constraints {
  The model is supplied the following sources criterion for this particular CWE entry: data at rest, data in transit, long-lived tokens
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.26.sinks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-326` — OWASP A02 cryptography: insufficient encryption strength. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sinks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:436-436
Constraints {
  The model is supplied the following sinks criterion for this particular CWE entry: weak algorithms, truncated keys, low-entropy secrets
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.26.sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-326` — OWASP A02 cryptography: insufficient encryption strength. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:438-438
Constraints {
  The model is supplied the following sanitizers criterion for this particular CWE entry: strong modern algorithm and key-size choices
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.26.non_sanitizers.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-326` — OWASP A02 cryptography: insufficient encryption strength. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:440-440
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: homegrown crypto
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.26.non_sanitizers.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-326` — OWASP A02 cryptography: insufficient encryption strength. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `non_sanitizers` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:441-441
Constraints {
  The model is supplied the following non_sanitizers criterion for this particular CWE entry: security through obscurity
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

## entries.26.fp_checks.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

Source CWE-entry selector: `CWE-326` — OWASP A02 cryptography: insufficient encryption strength. The array index in the heading identifies this original entry, not a new priority/order.

Guidance role: `fp_checks` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.

```sudo
// Source: vvaharness/rules/generic.kb.yaml:443-443
Constraints {
  The model is supplied the following fp_checks criterion for this particular CWE entry: algorithm is non-security legacy only
  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.
}
```

