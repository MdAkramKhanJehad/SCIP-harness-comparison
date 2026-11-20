# vvaharness/skills/templates/probe.sh — model-visible probe feedback

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

```sudo
// Source: vvaharness/skills/templates/probe.sh:145-158
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: FNR == 1 { ins = 0 } { l = tolower($0) interp = (l ~ /(\{\{|\{%[[:space:]]*(if|for|print)|<%[=-]|\$\{|#\{|\[\[\$|\[\(\$)/) opens_here = (l ~ /<script/) if (interp && (ins > 0 || opens_here)) { enc = (l ~ /tojson|json_script|json\.stringify|escapejs|template\.js|jsonify|jsonencode|\|[[:space:]]*e[[:space:]]*[}|]/) ? "ENCODED?" : "RAW" s = $0 gsub(/[ ][ ]*/, " ", s) printf "%s:%d: [%s] %s\n", FILENAME, FNR, enc, substr(s, 1, 150) } ins = ins + gsub(/<script/, "&", l) - gsub(/<\/script/, "&", l) if (ins < 0) { ins = 0 } }
}
```

```sudo
// Source: vvaharness/skills/templates/probe.sh:177-210
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: BEGIN { Q = "[" sprintf("%c", 34) sprintf("%c", 39) "]" } FNR == 1 { if (inform) { flush_form() } ; inform = 0 } { l = tolower($0) gsub(Q, "", l) rest = l while (1) { if (!inform) { p = index(rest, "<form") if (p == 0) { break } inform = 1 startline = FNR buf = "" rest = substr(rest, p) } q = index(rest, "</form") if (q == 0) { buf = buf " " rest; break } buf = buf " " substr(rest, 1, q - 1) flush_form() inform = 0 rest = substr(rest, q + 6) } } END { if (inform) { flush_form() } } function flush_form() { verb = "GET/UNSPECIFIED" if (buf ~ /method[ ]*=[ ]*(post|put|delete|patch)/) { verb = "STATE-CHANGING" } tok = "NO-TOKEN" if (buf ~ /csrf|xsrf|authenticity_token|antiforgerytoken|hidden_tag|_token|requestverificationtoken/) { tok = "token-present" } act = "?" if (match(buf, /action[ ]*=[ ]*[^ >]+/)) { act = substr(buf, RSTART, RLENGTH) } printf "%s:%d: %s %s (%s)\n", FILENAME, startline, verb, tok, act forms++ }
}
```

