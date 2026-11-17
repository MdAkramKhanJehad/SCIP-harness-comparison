"""Parse .pseudo files written to the conventions in schema/Common.pseudo.

parse_tree(root) -> (components, refs, problems)
  components: list of dicts (id, kind, parent, executed_by, role, stage, real_source, line, calls, knobs, doc)
  refs:       list of (knob_id, component_id, file, line)
  problems:   list of strings (convention violations)
"""
import re
from pathlib import Path

THETA = re.compile(r'θ\["([^"]+)"\]')
DECL = re.compile(r'^\s*(?:(?:public|private|protected|abstract|final|static|sealed)\s+)*'
                  r'(class|enum|interface|record)\s+([A-Za-z_]\w*)')
METHOD = re.compile(r'^\s*(?:@\w+(?:\([^)]*\))?\s+)*(?:(?:public|private|protected|abstract|final|static|default|synchronized)\s+)*'
                    r'(?:<[^>]*>\s+)?(?:[\w$.]+(?:<[^{}]*?>)?(?:\[\])*\s+)?([A-Za-z_]\w*)\s*\(.*\)\s*(?:throws\s+[\w.,\s]+)?\{(?:\s*\})?\s*(?://.*)?$')
NOT_METHODS = {"if", "for", "while", "switch", "catch", "synchronized", "return", "new", "else", "try",
               "do", "foreach", "with", "when", "case", "loop", "repeat", "until"}
ANNOT = re.compile(r'@(\w+)\(([^)]*)\)')
CALL = re.compile(r'\b([A-Z][A-Za-z0-9_]*)\.([a-z_][A-Za-z0-9_]*)\s*\(')
SRC = re.compile(r'//\s*src:\s*(\S+)')
FILE_HDR = re.compile(r'^//\s*file:\s*(.+)$')
EXECUTORS = {"CODE", "MODEL", "MIXED"}
ROLES = {"pipeline", "stage", "step", "prompt", "rule_set", "agent", "tool", "skill", "config",
         "backend", "io", "evaluation", "stub", "types"}


def _strip(line):
    """Remove string literals and // comments, for brace counting."""
    out, i, n, q = [], 0, len(line), None
    while i < n:
        ch = line[i]
        if q:
            if ch == "\\":
                i += 2
                continue
            if ch == q:
                q = None
            i += 1
            continue
        if ch in "\"'" and not (ch == "'" and i + 1 < n and line[i - 1:i].isalnum()):
            q = ch
            i += 1
            continue
        if line.startswith("//", i):
            break
        out.append(ch)
        i += 1
    return "".join(out)


def _annots(lines):
    d = {}
    for l in lines:
        for k, v in ANNOT.findall(l):
            d[k] = v.strip().strip('"')
    return d


def parse_file(path, rel):
    comps, refs, probs = [], [], []
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    mod_id = rel
    hdr = FILE_HDR.match(lines[0]) if lines else None
    if not hdr:
        probs.append(f"{rel}:1 missing '// file:' header")
    real = [s.strip() for s in hdr.group(1).split(",")] if hdr else []
    doc = []
    for l in lines[1:6]:
        if l.startswith("//") and not l.startswith("// src"):
            doc.append(l[2:].strip())
        else:
            break
    module = dict(id=mod_id, kind="module", parent=None, executed_by="CODE", role=None, stage=None,
                  real_source=real, line=1, calls=[], knobs=[], doc=" ".join(doc)[:400])
    comps.append(module)

    depth = 0
    pending = []          # annotation lines waiting for a declaration
    cls = None            # current class component (depth 0 -> 1)
    meth = None           # current method component
    meth_depth = None
    in_block_comment = False
    for no, raw in enumerate(lines, 1):
        line = raw
        s = line.strip()
        if in_block_comment:
            if "*/" in s:
                in_block_comment = False
            continue
        if s.startswith("/*") and "*/" not in s:
            in_block_comment = True
            continue
        if s.startswith("/*"):
            continue
        # knob refs (anywhere, including comments? -> only code part before //)
        owner = meth or cls or module
        for kid in THETA.findall(line.split("// src:", 1)[0]):
            refs.append((kid, owner["id"], rel, no))
            if kid not in owner["knobs"]:
                owner["knobs"].append(kid)
        for m in SRC.findall(line):
            if m not in owner["real_source"] and owner is not module:
                if len(owner["real_source"]) < 40:
                    owner["real_source"].append(m)
        if s.startswith("@") and not DECL.match(s) and not METHOD.match(s):
            pending.append(s)
            continue
        dm = DECL.match(line)
        stripped = _strip(line)
        if dm and depth == 0:
            a = _annots(pending + [line])
            pending = []
            ex = a.get("executedBy", "CODE")
            ro = a.get("role")
            if ex not in EXECUTORS:
                probs.append(f"{rel}:{no} bad @executedBy({ex})")
            if ro is None:
                probs.append(f"{rel}:{no} class {dm.group(2)} missing @role")
            elif ro not in ROLES:
                probs.append(f"{rel}:{no} bad @role({ro})")
            cls = dict(id=f"{rel}#{dm.group(2)}", kind="class", parent=mod_id, executed_by=ex, role=ro,
                       stage=a.get("stage"), real_source=[a["src"]] if "src" in a else [], line=no,
                       calls=[], knobs=[], doc="")
            if "executedBy" not in a:
                probs.append(f"{rel}:{no} class {dm.group(2)} missing @executedBy")
            comps.append(cls)
        elif depth == 1 and cls is not None and meth is None:
            mm = METHOD.match(line)
            if mm and mm.group(1) not in NOT_METHODS and "{" in stripped:
                a = _annots(pending + [line])
                pending = []
                meth = dict(id=f"{cls['id']}.{mm.group(1)}", kind="method", parent=cls["id"],
                            executed_by=a.get("executedBy", cls["executed_by"]), role=a.get("role", cls["role"]),
                            stage=a.get("stage", cls["stage"]), real_source=[a["src"]] if "src" in a else [],
                            line=no, calls=[], knobs=[], doc="")
                comps.append(meth)
                meth_depth = depth
                # re-attribute refs found on the declaration line itself
                for kid in THETA.findall(line):
                    for i in range(len(refs) - 1, -1, -1):
                        if refs[i][3] == no and refs[i][0] == kid:
                            refs[i] = (kid, meth["id"], rel, no)
                            break
                    if kid not in meth["knobs"]:
                        meth["knobs"].append(kid)
            else:
                pending = []
        else:
            if s and not s.startswith("//"):
                pending = []
        if meth is not None:
            for c, m in CALL.findall(stripped):
                name = f"{c}.{m}"
                if name not in meth["calls"]:
                    meth["calls"].append(name)
        opens, closes = stripped.count("{"), stripped.count("}")
        depth += opens - closes
        if depth < 0:
            probs.append(f"{rel}:{no} unbalanced closing brace")
            depth = 0
        if meth is not None and depth <= meth_depth:
            meth, meth_depth = None, None
        if cls is not None and depth == 0:
            cls = None
    if depth != 0:
        probs.append(f"{rel}: braces unbalanced at end of file (depth {depth})")
    # de-duplicate component ids (overloaded methods share an id; keep first, merge knobs)
    seen = {}
    out = []
    for c in comps:
        if c["id"] in seen:
            p = seen[c["id"]]
            for k in c["knobs"]:
                if k not in p["knobs"]:
                    p["knobs"].append(k)
            for k in c["calls"]:
                if k not in p["calls"]:
                    p["calls"].append(k)
            continue
        seen[c["id"]] = c
        out.append(c)
    return out, refs, probs


def parse_tree(root):
    root = Path(root)
    comps, refs, probs = [], [], []
    for p in sorted(root.rglob("*.pseudo")):
        rel = p.relative_to(root).as_posix()
        c, r, pr = parse_file(p, rel)
        comps += c
        refs += r
        probs += pr
    return comps, refs, probs
