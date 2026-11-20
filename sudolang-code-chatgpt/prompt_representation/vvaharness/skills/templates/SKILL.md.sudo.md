# vvaharness/skills/templates/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## View-layer source/guard exceptions and enumeration

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/templates/SKILL.md:24-125
Constraints {
  Requested first move: run sh .vvaharness/skills/templates/probe.sh, then read listed layouts/partials before leaf pages.
  A requested template finding is anchored at the output interpolation/form location, not merely the rendering handler.
  The four-part requested gate needs a template sink, a non-local-constant value, a named external-actor path and no context-correct defense.
  if (a blank/stubbed helper stands for a live column with live markup and a writing handler) {
    The explicit exception asks for the template finding despite today's constant expression; name that column.
  }
  Requested context analysis distinguishes HTML body, URL scheme, event JavaScript, script serialization/end tags, unquoted attributes and CSS; HTML escaping is not generalized across contexts.
  Stored-path procedure: start at interpolation; find rendering kwarg/route/query; find model writes and graph importers; inspect readers/cross-account visibility; report template span plus writer file:line.
  Separate requested classes include output XSS, template information disclosure and missing form CSRF; inspect fetch/axios/ajax script requests as well as forms. Installed-but-unused Flask-WTF is not accepted as protection.
  Requested refutations include correct-context default/outer escaping, genuinely bounded helpers (except the explicit stub case), named write-path sanitizer and unrendered files. CSP may lower severity without refuting URL/attribute injection; browser editors alone are not server sanitizers.
  The model is asked to open every inventoried template, not sample; emit per file/span/class/path and state templates/interpolations/confirmations/autoescape-refutations counts.
  The source information-disclosure bullet ends with an unfinished 'and'; no missing continuation is invented.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/templates/SKILL.md:1-4
Constraints {
  The source declares name = "templates". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "View-layer lens: stored and reflected XSS in server-rendered templates of every dialect (Jinja2 |safe / autoescape false / safe_columns, Django mark_safe, Handlebars {{{ }}}, ERB raw / html_safe, Thymeleaf th:utext, JSP <%= %>, Vue v-html, React dangerouslySetInnerHTML, Razor @Html.Raw, Go text/template), context-confusion bugs in href / src / onclick / <script> interpolations, SSTI from runtime-built template source, template-layer information disclosure, and state-changing forms rendered with no CSRF token. Activate whenever the repo holds templates/, views/, *.html, *.j2, *.erb, *.hbs, *.jsp, *.cshtml, *.vue, or a render_template / render / res.render call.". Tool lists here describe the request profile; source loaders determine actual grants.
  The request retains this source rule, criterion or rationale, with its original modal force: View-layer lens: stored and reflected XSS in server-rendered templates of every dialect (Jinja2 |safe / autoescape false / safe_columns, Django mark_safe, Handlebars {{{ }}}, ERB raw / html_safe, Thymeleaf th:utext, JSP <%= %>, Vue v-html, React dangerouslySetInnerHTML, Razor @Html.Raw, Go text/template), context-confusion bugs in href / src / onclick / <script> interpolations, SSTI from runtime-built template source, template-layer information disclosure, and state-changing forms rendered with no CSRF token. Activate whenever the repo holds templates/, views/, *.html, *.j2, *.erb, *.hbs, *.jsp, *.cshtml, *.vue, or a render_template / render / res.render call.
}
```

# Template and View-Layer Lens

```sudo
// Source: vvaharness/skills/templates/SKILL.md:24-28
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Templates are not call-graph nodes: `GraphSinksInCommunity` and `GraphNeighbors` never return one, so `routes/` and `models/` show the model the route that *renders* a template, never the template that *emits* the value. A template file is a finding LOCATION — anchor the finding on the template line that emits the value, not on the handler line that renders the template.
  The request retains this source rule, criterion or rationale, with its original modal force: The fix edits the template.
}
```

## First move

```sudo
// Source: vvaharness/skills/templates/SKILL.md:32-34
Constraints {
  Within this instruction's source scope, the model is asked to invoke `sh .vvaharness/skills/templates/probe.sh` — one read-only pass over every dialect: view-tree inventory, labelled `path:line` hits for the whole sink battery, and a per-`<form>` verdict on whether a CSRF token field sits inside it.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:36-39
Constraints {
  The model is asked to obtain and examine the layouts and partials it lists before any leaf page: one bad interpolation in `base.html` or `fragments/*.html` renders on every page that extends or includes it — highest multiplier in the repo, and the file nobody opens.
  The request retains this source rule, criterion or rationale, with its original modal force: The probe gives candidates; the judgement below is not greppable.
}
```

## Hard gate — all four

```sudo
// Source: vvaharness/skills/templates/SKILL.md:43-44
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A template sink — safe/raw marker, autoescape off, a macro kwarg marking a *column* safe, or a context HTML-escaping misses.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:45-46
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A value that is not a template-local constant. Request field, DB column, filename, exception object: source.
  The request retains this source rule, criterion or rationale, with its original modal force: Helper: not.
  The model is asked to obtain and examine *Emptied expressions* before refuting here.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:47-48
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A named path from an external actor. Stored: name the writing handler and the column.
  The request retains this source rule, criterion or rationale, with its original modal force: Reflected: name the request field and the `render_template(...)` kwarg carrying it.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:49-50
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: No context-correct escaper between them — no sanitizer, no scheme allow-list for URL context, no `|tojson` for script context.
}
```

## Context is not one context

```sudo
// Source: vvaharness/skills/templates/SKILL.md:54-55
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Escaping `< > & " '` defends the HTML *body* only.
  The request retains this source rule, criterion or rationale, with its original modal force: Judge by the bytes around the interpolation, not by the filter.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:57-59
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: URL — `javascript:` and `data:image/svg+xml;base64,…` (SVG runs script inside `<object>`/`<embed>`/`<iframe>`) hold no HTML metacharacters, so autoescape passes them through untouched.
  The request retains this source rule, criterion or rationale, with its original modal force: Needs a scheme allow-list, not escaping.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:60-61
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Event handler — the attribute body is JavaScript, and the HTML parser un-escapes entities before the JS parser sees them.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:62-63
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Script — needs `|tojson` / `json_script` / `template.JS`; `</script>` inside a quoted JS string still ends the block.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:64-65
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Unquoted attribute — `class={{u}}`: a space starts `onmouseover=…`. CSS — `style` and `<style>` bodies.
}
```

## Emptied expressions are still sinks

```sudo
// Source: vvaharness/skills/templates/SKILL.md:69-72
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Refusing a blanked or stubbed sink is how this class gets missed.
  The request retains this source rule, criterion or rationale, with its original modal force: A helper stubbed to return `""` "for SAST compatibility" still sits in live markup fed by a live column: when markup, column and writing handler all exist, report the template line even though today's expression is constant, and name the column the stub stands in for.
}
```

## The stored path: sink and source are in different files

```sudo
// Source: vvaharness/skills/templates/SKILL.md:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: The template reads a column an earlier request wrote; neither file mentions the other.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:78-78
// Source list marker 1.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Take the interpolated expression (`note.text`, the `safe_columns` entry).
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:79-79
// Source list marker 2.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Grep the view kwarg: `render_template('home.html'` → the route; the kwarg → the query.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:80-81
// Source list marker 3.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Grep the model attribute and every write to it. `GraphImporters` on the model module and on the query helper enumerates its readers and writers; the writers are the model's sources.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:82-83
// Source list marker 4.; preserve its source grouping, not an invented execution order.
Constraints {
  The model is asked to establish who reads it back. `or_(Note.user_id == user_id, Note.private == False)` renders attacker rows in *other* users' pages — cross-account stored XSS, not self-XSS.
  The request retains this source rule, criterion or rationale, with its original modal force: Say which.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:84-84
// Source list marker 5.; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Report at the template line, citing the writer's file:line.
}
```

## Two more classes at these same lines

```sudo
// Source: vvaharness/skills/templates/SKILL.md:88-91
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Information disclosure, separate from any XSS on the line.
  The request retains this source rule, criterion or rationale, with its original modal force: Exception or debug objects rendered: CWE-209, cause in the handler, location at the template line.
  The request retains this source rule, criterion or rationale, with its original modal force: Config, secret keys, password columns, absolute paths, SQL text, version banners: CWE-200 / CWE-540.
  The request retains this source rule, criterion or rationale, with its original modal force: Hidden is not secret — `hidden` and `password` input values and `data-` attributes all ship, and
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:92-92
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: `<!-- HTML comments -->` reach the client where `{# … #}` does not.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:93-98
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Missing CSRF token, CWE-352 at the `<form>` tag: template finding, template fix.
  The request retains this source rule, criterion or rationale, with its original modal force: Take the probe's per-form verdict, then cover `fetch` / `axios` / `$.ajax` POSTs in `<script>` blocks yourself.
  The request retains this source rule, criterion or rationale, with its original modal force: Zero CSRF machinery repo-wide plus forms subclassing `wtforms.Form` rather than `flask_wtf.FlaskForm` makes every state-changing form a finding; unused `Flask-WTF` in `requirements.txt` is not a defence.
  The request retains this source rule, criterion or rationale, with its original modal force: Handler-side judgement is the `csrf` lens; `CweGuidance('CWE-352')` has the class detail.
}
```

## FP checks — what refutes the finding

```sudo
// Source: vvaharness/skills/templates/SKILL.md:102-103
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Autoescape on, no safe marker, HTML-body or quoted-attribute context. Jinja under Flask escapes `"` to `&#34;`, so a quoted attribute holding a plain column is defended.
  The request retains this source rule, criterion or rationale, with its original modal force: Say why.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:104-105
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Helper or bounded expression — `url_for`, `strftime`, an integer PK, a closed enum, a two-value ternary.
  The request retains this source rule, criterion or rationale, with its original modal force: Does not cover a stubbed helper backed by a live column.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:106-107
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Re-escaped at the outer interpolation. `render_template_string()` returns `str`, not `Markup`, so `<p>{{ msg }}</p>` escapes what the handler built: XSS refuted, SSTI (CWE-1336) not.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:108-109
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: A sanitizer on the write path — name it and its line.
  The request retains this source rule, criterion or rationale, with its original modal force: A rich-text editor is not one: CKEditor / TinyMCE / Quill sanitize in the browser and constrain nothing the POST handler accepts.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:110-111
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: CSP without `unsafe-inline`, plus a nonce, lowers severity; it does not refute URL- or attribute-context injection.
  The request retains this source rule, criterion or rationale, with its original modal force: State what it blocks.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:112-112
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Not rendered — under `static/`, a fixture, or absent from the probe's render call sites.
}
```

## Enumeration rule

```sudo
// Source: vvaharness/skills/templates/SKILL.md:116-116
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Every interpolation is its own finding; never one "templates do not escape output" finding.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:118-118
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Open every template the probe's inventory lists, partials included.
  The requested model behavior excludes sample.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:119-121
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One finding per template file and line span.
  The request retains this source rule, criterion or rationale, with its original modal force: The same column rendered unsafe in three templates is three findings: each is edited separately, and a blanket finding can only be credited, tracked or fixed once.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:122-124
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: One line can carry two classes: CWE-79 at `{{ x | safe }}` and CWE-200 because the field should not reach the page at all.
  The request retains this source rule, criterion or rationale, with its original modal force: Split reflected from stored at one sink too — different paths, different fixes.
}
```

```sudo
// Source: vvaharness/skills/templates/SKILL.md:125-125
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: State the sweep: templates globbed, interpolations judged, confirmed, autoescape-refuted.
}
```

