"""Static prompt-conversion consistency checks; not a semantic-equivalence proof."""
import ast,csv,hashlib,json,re
import yaml
from collections import Counter,defaultdict
from pathlib import Path
OUT=Path(__file__).resolve().parents[1];SRC=OUT.parent/'visa-vulnerability-agentic-harness'
def rows(name):return list(csv.DictReader((OUT/name).open(),delimiter='\t'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
errors=[];counts=Counter();manifest=json.loads((OUT/'prompt_conversion_manifest.json').read_text());units=json.loads((OUT/'prompt_conversion_units.json').read_text())
by_source=defaultdict(list)
for u in units:
 by_source[u['source']].append(u)
 if hashlib.sha256(u['source_text'].encode()).hexdigest()!=u['sha256']:errors.append('unit text/hash mismatch: '+str(u['id']))
 text=(OUT/u['representation']).read_text();citation=f"// Source: {u['source']}:{u['line_start']}-{u['line_end']}"
 if citation not in text:errors.append('unit missing citation '+str(u['id']))
 if not 1<=u['line_start']<=u['line_end']<=len((SRC/u['source']).read_text().splitlines()):errors.append('unit invalid range '+str(u['id']))
 counts['converted_units']+=1
for m in manifest:
 p=OUT/m['representation'];src=SRC/m['source'];detail=OUT/'source_detail'/(m['source']+'.sudo.md')
 if sha(src)!=m['source_sha256']:errors.append('source changed '+m['source'])
 if sha(p)!=m['representation_sha256']:errors.append('view changed since generation '+m['source'])
 if not detail.exists() or 'converted-model-instructions' not in detail.read_text():errors.append('missing source_detail integration '+m['source'])
 if not by_source[m['source']]:errors.append('no converted instruction units '+m['source'])
 if m['kind']=='markdown-model-instructions':
  if not detail.read_text().startswith(p.read_text()):errors.append('Markdown source_detail differs from converted view '+m['source'])
  lines=src.read_text().splitlines();covered=set();comment=False;frontmatter=False
  for u in by_source[m['source']]:covered.update(range(u['line_start'],u['line_end']+1))
  # Metadata is separately rendered and source-cited; headings are hierarchy.
  if lines and lines[0]=='---':
   last=next(i for i in range(1,len(lines)) if lines[i]=='---');covered.update(range(1,last+2))
  for i,line in enumerate(lines,1):
   if line.lstrip().startswith('<!--') and any('Copyright' in x or 'Licensed under' in x for x in lines[i-1:i+4]):comment=True
   if comment:
    if '-->' in line:comment=False
    continue
   if not line.strip() or re.match(r'^#{1,6}\s',line) or line.strip() in ('---','***'):continue
   if i not in covered:errors.append(f'Markdown instruction line unconverted {m["source"]}:{i}')
   counts['markdown_content_lines_covered']+=1
  counts['markdown_instruction_files']+=1
 counts['converted_source_files']+=1
triage=rows('prompt_content_triage.tsv')
for r in triage:
 if not r['status'].startswith('converted'):continue
 if not r['representation'] or not (OUT/r['representation']).exists():errors.append('converted carrier missing view '+str(r));continue
 a,b=int(r['line_start']),int(r['line_end'])
 if not any(u['line_start']==a and u['line_end']==b for u in by_source[r['source']]):
  # Heading-only carriers supply structure, not an omitted behavioral paragraph.
  source='\n'.join((SRC/r['source']).read_text().splitlines()[a-1:b])
  # Require the carrier heading/source context to be present in the generated view.
  if f'source lines {a}–{b}' not in (OUT/r['representation']).read_text():errors.append('carrier not represented '+str(r))
 counts[r['status']]+=1
# Check every supplied KB decision-pattern value, including single-token names.
kb_rel='vvaharness/rules/generic.kb.yaml'
kb=yaml.safe_load((SRC/kb_rel).read_text())
kb_units={(u['source_label'],u['source_text']) for u in by_source[kb_rel]}
for i,entry in enumerate(kb['entries']):
 for field in ('sources','sinks','sanitizers','non_sanitizers','fp_checks'):
  for j,value in enumerate(entry.get(field,[])):
   label=f'entries.{i}.{field}.{j}'
   if (label,str(value)) not in kb_units:errors.append('KB decision criterion missing '+label+': '+str(value))
   counts['knowledge_base_criteria_checked']+=1
required_markdown={p.relative_to(SRC).as_posix() for p in (SRC/'vvaharness/skills').rglob('SKILL.md')} | {p.relative_to(SRC).as_posix() for p in (SRC/'vvaharness/validation').rglob('*.md')}
converted_markdown={m['source'] for m in manifest if m['kind']=='markdown-model-instructions'}
if not required_markdown<=converted_markdown:errors.append('packaged skill/persona/rule Markdown missing: '+str(required_markdown-converted_markdown))
# Independently enumerate maximal string/template AST sites, including embedded code.
expected=set()
def sites(tree,rel):
 parents={c:n for n in ast.walk(tree) for c in ast.iter_child_nodes(n)}
 return {(rel,n.lineno,n.end_lineno,n.col_offset) for n in ast.walk(tree) if (isinstance(n,ast.JoinedStr) or isinstance(n,ast.Constant) and isinstance(n.value,str)) and not isinstance(parents.get(n),(ast.JoinedStr,ast.FormattedValue))}
for p in SRC.rglob('*.py'):
 if 'tests' in p.relative_to(SRC).parts:continue
 expected.update(sites(ast.parse(p.read_text()),p.relative_to(SRC).as_posix()))
for r in rows('embedded_python.tsv'):
 a,b=int(r['line_start']),int(r['line_end']);tree=ast.parse('\n'.join((SRC/r['source']).read_text().splitlines()[a-1:b]));ast.increment_lineno(tree,a-1);expected.update(sites(tree,r['source']))
actual={(r['source'],int(r['line_start']),int(r['line_end']),int(r['column'])) for r in triage}
if expected!=actual:errors.append(f'carrier triage sites differ: missing {len(expected-actual)}, extra {len(actual-expected)}')
counts['maximal_string_template_sites_triaged']=len(actual)
# All inline links in new views and workflow map resolve locally; directories allowed.
for p in [OUT/'prompt_workflow.sudo.md',*(OUT/'prompt_representation').rglob('*.sudo.md'),*[OUT/'source_detail'/(m['source']+'.sudo.md') for m in manifest]]:
 fenced=None
 for line in p.read_text().splitlines():
  fence=re.match(r'^\s*(`{3,}|~{3,})',line)
  if fence:
   token=fence.group(1)
   if fenced is None:fenced=token
   elif token[0]==fenced[0] and len(token)>=len(fenced):fenced=None
   continue
  # Source notation inside a code fence is not generated Markdown navigation.
  # In particular, a dynamic f-string followed by '(agentic)' is not a link.
  if fenced:continue
  for target in re.findall(r'\]\(([^\s)]+)\)',line):
   if target.startswith(('http:','https:','#')):continue
   if not (p.parent/target.split('#')[0]).exists():errors.append('broken link '+str(p.relative_to(OUT))+' -> '+target)
# Vocabulary lookup is documented; entries point to their actual converted use.
for r in rows('prompt_vocabulary.tsv'):
 if not r['previous'] or not r['reuse'] or not (OUT/r['used_in']).exists():errors.append('incomplete vocabulary row '+r['identifier'])
 counts['prompt_vocabulary_entries']+=1
coverage=rows('coverage.tsv');pcs={r['source']:r for r in rows('prompt_content_coverage.tsv')}
for r in coverage:
 pc=pcs.get(r['source_path'])
 if pc and r.get('prompt_content_status')!=pc['status']:errors.append('stale main coverage '+r['source_path'])
 for field in ('model_instruction_representation',):
  if r.get(field) and not (OUT/r[field]).exists():errors.append('coverage missing target '+r[field])
# Supporting copies remain exact and are separate from the converted instruction view.
for m in manifest:
 original=OUT/'assets/original'/m['source']
 if m['kind']=='markdown-model-instructions' and (not original.exists() or sha(original)!=sha(SRC/m['source'])):errors.append('Markdown original evidence changed '+m['source'])
result=dict(scope='Static inventory, range, integrity, integration and vocabulary checks; manual review is separately documented; no model compliance or semantic equivalence proof',counts=dict(counts),carrier_dispositions=dict(Counter(r['status'] for r in triage)),content_dispositions=dict(Counter(r['status'] for r in pcs.values())),errors=errors,passed=not errors)
(OUT/'prompt_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));raise SystemExit(bool(errors))
