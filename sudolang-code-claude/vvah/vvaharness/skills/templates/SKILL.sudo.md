# vvaharness/skills/templates/SKILL.md

A lens for the view layer: cross-site scripting by output context, server-side template injection, information disclosure in templates, and forms without a CSRF token. Findings are anchored on the template line.

Source: `vvaharness/skills/templates/SKILL.md` (lines 1-125)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/templates/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/templates/SKILL.md:1-125
TemplateViewLayerLens {
  name: "templates"
  description: "View-layer lens: stored and reflected XSS in server-rendered templates of every dialect"   // abstracted: the rest of line 3 lists the dialect markers, context-confusion bugs, SSTI, template-layer information disclosure and forms with no CSRF token, and ends "Activate whenever the repo holds templates/, views/, *.html, *.j2, *.erb, *.hbs, *.jsp, *.cshtml, *.vue, or a render_template / render / res.render call."
  Constraints {
    // prompt-src: vvaharness/skills/templates/SKILL.md:24-28
    Templates are not call-graph nodes; GraphSinksInCommunity and GraphNeighbors never return one.
    "**A template file is a finding LOCATION** — anchor the finding on the template line that emits the value, not on the handler line that renders the template. The fix edits the template."

    // prompt-src: vvaharness/skills/templates/SKILL.md:30-39 — the model is told to run the probe (see templates/probe.sudo)
    Run "sh .vvaharness/skills/templates/probe.sh" first.
    Read the layouts and partials it lists "**before any leaf page**". "The probe gives candidates; the judgement below is not greppable."

    // prompt-src: vvaharness/skills/templates/SKILL.md:41-50
    constraint HardGate {
      All four:
      1. "A template sink" — safe or raw marker, autoescape off, a macro keyword argument marking a column safe, or a context HTML escaping misses.
      2. "A value that is not a template-local constant." "Read *Emptied expressions* before refuting here."
      3. "A named path from an external actor." Stored: the writing handler and column. Reflected: the request field and the render_template keyword argument.
      4. "No context-correct escaper between them" — no sanitizer, no scheme allow-list for URL context, no |tojson for script context.
    }

    // prompt-src: vvaharness/skills/templates/SKILL.md:52-65
    "Escaping `< > & \" '` defends the HTML *body* only. Judge by the bytes around the interpolation, not by the filter."
    Contexts: URL (javascript: and data:image/svg+xml pass autoescape; needs a scheme allow-list), event handler (entities decode before the JavaScript parser), script (needs |tojson / json_script / template.JS; </script> ends the block), unquoted attribute, CSS.

    // prompt-src: vvaharness/skills/templates/SKILL.md:67-72
    constraint EmptiedExpressions {
      A helper stubbed to return "" still sits in live markup fed by a live column: "when markup, column and writing handler all exist, report the template line even though today's expression is constant, and name the column the stub stands in for."
    }

    // prompt-src: vvaharness/skills/templates/SKILL.md:74-84
    fn traceStoredPath():executor=model {
      1. Take the interpolated expression.
      2. Grep the view keyword argument to the route and the query.
      3. Grep the model attribute and every write; GraphImporters on the model and query helper; "the writers are your sources."
      4. Check who reads it back: rows rendered in other users' pages is "cross-account stored XSS, not self-XSS. Say which."
      5. "Report at the template line, citing the writer's file:line."
    }

    // prompt-src: vvaharness/skills/templates/SKILL.md:86-98
    Information disclosure is separate from any XSS on the line: exception or debug objects rendered are CWE-209 (cause in handler, location at template line); config, secret keys, password columns, paths, SQL text, banners are CWE-200 / CWE-540; "Hidden is not secret".
    Missing CSRF token: "CWE-352 **at the `<form>` tag**"; take the probe's per-form verdict, then cover fetch / axios / $.ajax POSTs yourself. Zero CSRF machinery repo-wide plus wtforms.Form instead of flask_wtf.FlaskForm makes "**every** state-changing form a finding"; an unused Flask-WTF in requirements.txt is not a defence.

    // prompt-src: vvaharness/skills/templates/SKILL.md:100-112 — "FP checks — what refutes the finding"
    Autoescape on, no safe marker, HTML-body or quoted-attribute context ("Say why."); a helper or bounded expression (url_for, strftime, integer key, closed enumeration, two-value ternary) but "Does **not** cover a stubbed helper backed by a live column."; re-escaped at the outer interpolation ("XSS refuted, SSTI (CWE-1336) not."); a sanitizer on the write path, name it (browser-side rich-text editors are not one); CSP without unsafe-inline plus a nonce lowers severity but does not refute URL or attribute context; not rendered.

    // prompt-src: vvaharness/skills/templates/SKILL.md:114-125
    constraint EnumerationRule {
      "Every interpolation is its own finding; never one \"templates do not escape output\" finding."
      "Open every template the probe's inventory lists, partials included. Do not sample."
      One finding per template file and line span; one line can carry two classes (CWE-79 and CWE-200); split reflected from stored.
      "State the sweep: templates globbed, interpolations judged, confirmed, autoescape-refuted."
    }
  }
}
