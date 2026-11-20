"""Convert prompt text into descriptive SudoLang model constraints, never execute it.

Text remains natural language where that is the faithful SudoLang abstraction.
Paragraph/list/section hierarchy, source alternatives and qualitative modifiers
are preserved. Manual decision blocks supplement source-specific complex gates.
"""
from __future__ import annotations
import ast
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import yaml

OUT=Path(__file__).resolve().parents[1]
SRC=OUT.parent/'visa-vulnerability-agentic-harness'
ROOT=OUT/'prompt_representation'
MARKDOWN=[*sorted((SRC/'vvaharness/skills').glob('*/SKILL.md')),
 *sorted((SRC/'vvaharness/validation').rglob('*.md')),
 SRC/'AGENTS.md',SRC/'CLAUDE.md',SRC/'.github/copilot-instructions.md']
PROMPT_FILE=re.compile(r'(?:prompts?\.py$|/prompts/|/s[2678]/(?:session|outcomes)\.py$|/s4/(?:session|outcomes)\.py$|/verify/(?:judge|prompt|tools)\.py$|/classify/llm\.py$|/mapping/(?:endpoint_index|finding_map)\.py$|deepagents/(?:profiles|evidence_gate|tool_budget|model_call_budget)\.py$|/session/(?:launch_prompt|launcher)\.py$|/replay\.py$|/s1_autoexclude\.py$|/s2_planning\.py$|/semgrep/(?:triage|tools)\.py$|/agentdoc\.py$|/fact_specs\.py$)')
CONTEXT=re.compile(r'prompt|instruction|system|notice|nudge|description|clause|duty|sweep|replay|repair|guidance|tool_schema|_refuse|refusal|_final|build_user|build_launch|_budget_message|posture',re.I)
DIRECTIVE=re.compile(r'\b(?:you|your|must|never|should|always|ensure|strictly|avoid|ignore|prefer|choose|do not|don.t|return only|respond|report each|before reporting|call (?:one|the|a)|read (?:the|every|each)|JSON only|output only)\b|^(?:Read|Use|Call|Send|Return|Emit|Respond|Please|Follow|Retry|Stop|Continue|Check|Inspect|Report|Avoid|Analyze|Analyse|Perform|Write|Make|Include|Ignore)\b',re.I)


def write_tsv(path,fields,rows):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)


def natural(text,role='instruction'):
 """Change address/imperatives into declarative requested constraints.

 Qualitative scope and exceptions remain source-language predicates, never numeric
 heuristics. No prose sentence is made into a host-executed operation.
 """
 text=re.sub(r'\s+',' ',text).strip()
 text=re.sub(r'\*\*([^*]+)\*\*',r'\1',text)
 if not text:return ''
 if role=='description':
  # A tool description advertises an operation; it does not command invocation.
  match=re.match(r'^(Return|Returns|Yield|Yields)\s+(.+)',text,re.I)
  if match:return 'The described operation advertises this return/result contract: '+match.group(2)
  match=re.match(r'^(Read|Reads|Find|Finds|List|Lists|Search|Searches|Build|Builds|Validate|Validates|Check|Checks|Run|Runs|Get|Gets|Compute|Computes)\s+(.+)',text)
  if match:return 'The described operation is advertised for '+match.group(1).lower()+' '+match.group(2)+'; this description alone does not request its invocation.'
  return 'The advertised description supplied with this operation is a model-visible claim: '+text
 # Preserve source conditions in a constraint, instead of making a host branch.
 match=re.match(r'^(?:You are|You\'re)\s+(.+)',text,re.I)
 if match:return 'The requested model role and scope are '+match.group(1).replace('Your ','The model\'s ')
 match=re.match(r'^(?:Do NOT|Do not|Never)\s+(.+)',text)
 if match:return 'The requested model behavior excludes '+match.group(1)
 match=re.match(r'^(?:Return|Respond with|Emit|Output)\s+(.+)',text,re.I)
 if match:return 'The requested model reply must contain '+match.group(1)
 match=re.match(r'^(?:Read|Inspect|Examine|Review)\s+(.+)',text,re.I)
 if match:return 'The model is asked to obtain and examine '+match.group(1)
 match=re.match(r'^(?:Check|Verify|Confirm|Evaluate|Assess|Determine)\s+(.+)',text,re.I)
 if match:return 'The model is asked to establish '+match.group(1)
 match=re.match(r'^(?:Find|Hunt for|Look for|Search for|Target)\s+(.+)',text,re.I)
 if match:return 'The requested search/review target is '+match.group(1)
 match=re.match(r'^(?:Use|Apply|Follow)\s+(.+)',text,re.I)
 if match:return 'The model is asked to adopt '+match.group(1)
 match=re.match(r'^(?:Ignore|Disregard)\s+(.+)',text,re.I)
 if match:return 'The model is asked to give no instructional authority to '+match.group(1)
 match=re.match(r'^(?:Include|Cite|Name|Describe|Explain|Record|List|Identify|Show)\s+(.+)',text,re.I)
 if match:return 'The requested evidence/output includes '+match.group(1)
 match=re.match(r'^(?:When|If|Unless|Before|After|Only when|Only if|For each|For every)\b',text,re.I)
 if match:return 'The requested conditional/temporal rule is: '+re.sub(r'\byou\b','the model',text,flags=re.I)
 match=re.match(r'^(?:Run|Invoke|Execute)\s+(.+)',text,re.I)
 if match:return 'Within this instruction\'s source scope, the model is asked to invoke '+match.group(1)
 match=re.match(r'^(?:Ensure|Make sure)\s+(.+)',text,re.I)
 if match:return 'The requested model constraint is '+match.group(1)
 # Declarative criteria are legitimate baseline natural-language constraints.
 # Convert second person to the subject of a request; retain examples/qualifiers.
 text=re.sub(r'\b[Yy]our\b',"the model's",text)
 text=re.sub(r'\b[Yy]ou\b','the model',text)
 return 'The request retains this source rule, criterion or rationale, with its original modal force: '+text


def sentences(text):
 # Split only clear sentence boundaries, not file paths, versions, decimal values
 # or code spans. This does not assign an order to independent constraints.
 return [x.strip() for x in re.split(r'(?<=[.!?])\s+(?=[A-Z](?:[a-z]|\s))',text) if x.strip()]


def units(text,start=1):
 """Paragraph/list/fence units with original coordinates and list indentation."""
 lines=text.splitlines();result=[];i=0;comment=False
 while i<len(lines):
  line=lines[i];ln=start+i
  if line.lstrip().startswith('<!--') and any('Copyright' in x or 'Licensed under' in x for x in lines[i:i+5]):comment=True
  if comment:
   if '-->' in line:comment=False
   i+=1;continue
  if not line.strip():i+=1;continue
  if re.match(r'^\s*(`{3,}|~{3,})',line):
   delim=re.match(r'^\s*(`{3,}|~{3,})',line).group(1);begin=i;i+=1
   while i<len(lines) and not lines[i].lstrip().startswith(delim):i+=1
   if i<len(lines):i+=1
   result.append(dict(kind='example',text='\n'.join(lines[begin:i]),start=start+begin,end=start+i-1,indent=0));continue
  if re.match(r'^#{1,6}\s',line):
   result.append(dict(kind='heading',text=line.strip(),start=ln,end=ln,indent=0));i+=1;continue
  if line.strip() in ('---','***'):
   result.append(dict(kind='separator',text=line.strip(),start=ln,end=ln,indent=0));i+=1;continue
  begin=i;indent=len(line)-len(line.lstrip());bullet=re.match(r'^\s*(?:[-*+] |\d+[.)]\s|\([a-z]\)\s)',line)
  i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^\s*(?:[-*+] |\d+[.)]\s|\([a-z]\)\s|#{1,6}\s|`{3,}|~{3,})',lines[i]) and '<!--' not in lines[i]:i+=1
  body=' '.join(x.strip() for x in lines[begin:i])
  marker=bullet.group(0).strip() if bullet else ''
  if bullet:body=re.sub(r'^(?:[-*+] |\d+[.)]\s|\([a-z]\)\s)','',body)
  result.append(dict(kind='item' if bullet else 'paragraph',text=body,start=start+begin,end=start+i-1,indent=indent,marker=marker))
 return result


def block(rel,unit,role='instruction'):
 lines=[f"// Source: {rel}:{unit['start']}-{unit['end']}"]
 if unit.get('marker'):
  lines.append('// Source list marker '+unit['marker']+'; preserve its source grouping, not an invented execution order.')
 if unit['kind']=='example':
  raw=unit['text'].splitlines();body='\n'.join(raw[1:-1])
  language=raw[0].lstrip('`~').strip()
  lines += ['Constraints {','  The model is asked to use this source example as a format/pattern reference; it is not an observed result or a host-executed operation.',
            '  Preserve the source example\'s keys, enum spellings, placeholder values and command arguments.',
            *['  The requested example format/pattern includes '+m.group(1)+' with source contract '+m.group(2).strip()+'.' for m in re.finditer(r'(?m)^\s*[\"\']?([A-Za-z_][A-Za-z0-9_]*)[\"\']?\s*:\s*(.+)',body)],
            '  Example code is a candidate reference shape, not an assertion it was executed; source context determines whether it illustrates a permitted, prohibited, before-fix or after-fix case.','}',
            '```','',f'Example data/source notation ({language or "untyped"}):','', '``````text',body,'``````','', '```sudo']
  return lines
 lines += ['Constraints {']
 for sentence in sentences(unit['text']): lines.append('  '+natural(sentence,role))
 lines += ['}']
 return lines


def python_carriers(path,snippet=None,line_offset=0):
 raw=path.read_text();tree=ast.parse(raw if snippet is None else snippet)
 if line_offset:ast.increment_lineno(tree,line_offset)
 parents={c:n for n in ast.walk(tree) for c in ast.iter_child_nodes(n)}
 # Maximal literal/template carriers. F-string text fragments are not separate prompts.
 for node in ast.walk(tree):
  if not isinstance(node,(ast.Constant,ast.JoinedStr)):continue
  if isinstance(node,ast.Constant) and not isinstance(node.value,str):continue
  parent=parents.get(node)
  if isinstance(parent,(ast.JoinedStr,ast.FormattedValue)):continue
  ancestors=[];n=node
  while n in parents:n=parents[n];ancestors.append(n)
  if isinstance(node,ast.Constant):text=node.value;slots=[]
  else:
   bits=[];slots=[]
   for value in node.values:
    if isinstance(value,ast.Constant):bits.append(str(value.value))
    else:
     expression=ast.unparse(value.value)
     conversion={-1:'none',97:'ascii',114:'repr',115:'str'}.get(value.conversion,str(value.conversion))
     spec=ast.unparse(value.format_spec) if value.format_spec else 'none'
     slots.append(expression+'; conversion='+conversion+'; format_spec='+spec)
     bits.append('[dynamic source value: '+expression+'; conversion='+conversion+'; format_spec='+spec+']')
   text=''.join(bits)
  owner=next((n.name for n in ancestors if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))),'<module>')
  assignment=next((n for n in ancestors if isinstance(n,(ast.Assign,ast.AnnAssign))),None)
  binding=ast.unparse(assignment.targets[0] if isinstance(assignment,ast.Assign) else assignment.target) if assignment else ''
  doc=isinstance(parent,ast.Expr) and any(getattr(n,'body',[None])[0] is parent for n in ancestors if isinstance(n,(ast.Module,ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)))
  call=next((n for n in ancestors if isinstance(n,ast.Call)),None)
  call_name=ast.unparse(call.func) if call else ''
  keyword=next((n.arg for n in ancestors if isinstance(n,ast.keyword)),None)
  words=re.findall(r'[A-Za-z]{2,}',text)
  dictionary_description=False
  dictionary_instruction=False
  for container in ancestors:
   if isinstance(container,ast.Dict):
    for key,value in zip(container.keys,container.values):
     if isinstance(key,ast.Constant) and isinstance(key.value,str) and (value is node or value in ancestors):
      if key.value in ('description','tool_description'):dictionary_description=True
      if key.value in ('prompt','system_prompt','instructions','instruction','content'):dictionary_instruction=True
  contextual=bool(dictionary_description or dictionary_instruction or PROMPT_FILE.search(path.as_posix()) or CONTEXT.search(owner+' '+binding) or keyword in ('description','system_prompt','instructions','tool_description') or call_name.endswith(('HumanMessage','SystemMessage','ToolMessage')))
  if not text.strip():role='evidence-only-empty';reason='empty formatting/data literal'
  elif doc:
   tools='tool' in path.stem or 'tools' in path.parts or any(isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and any('tool' in ast.unparse(d).lower() for d in n.decorator_list) for n in ancestors)
   role='converted-tool-description' if tools else 'evidence-only-documentation'
   reason='tool-facing description; actual registration/caller controls exposure' if tools else 'source documentation, not supplied model instruction at this source site'
  elif len(words)<2 and not (dictionary_description or keyword=='description' or contextual and text.strip().rstrip('.!').lower() in ('stop','continue','retry')):role='evidence-only-data';reason='label/key/enum/path/short data fragment, not an independent behavioral instruction'
  elif dictionary_description:role='converted-tool-description';reason='schema/dictionary description; advertised meaning or field contract, not mandatory tool invocation'
  elif contextual:role='converted-model-instructions';reason='prompt-bearing source context or message/schema description'
  elif DIRECTIVE.search(text):role='converted-conditional-instructions';reason='instruction-bearing text; model exposure depends on source caller (could be host diagnostic/tool feedback)'
  else:role='evidence-only-data';reason='descriptive value/format/status/pattern, without identified model instruction'
  yield dict(node=node,text=text,slots=slots,owner=owner,binding=binding,role=role,reason=reason,
             call_name=call_name,keyword=keyword,raw=raw,source_expression=ast.get_source_segment(raw,node),
             format_call=ast.get_source_segment(raw,call) if call and isinstance(call.func,ast.Attribute) and call.func.attr in ('format','format_map','replace','join') else '')


def main():
 ROOT.mkdir(exist_ok=True);coverage=[];triage=[];allunits=[];vocab=[];manifest=[]
 # The two terminology additions are looked up before recording any new entry.
 existing={}
 for name in ('vocabulary_symbols.tsv','resource_vocabulary.tsv'):
  with (OUT/name).open() as f:
   for row in csv.DictReader(f,delimiter='\t'):existing.setdefault(row['identifier'],[]).append(row)
 decisions=json.loads((OUT/'prompt_decision_views.json').read_text())
 def record(rel,u,target,role,label=''):
  index=len(allunits)+1
  allunits.append(dict(id=index,source=rel,line_start=u['start'],line_end=u['end'],kind=u['kind'],
                       representation=target.relative_to(OUT).as_posix(),role=role,source_label=label,
                       source_text=u['text'],sha256=hashlib.sha256(u['text'].encode()).hexdigest()))
  return index
 def write(rel,content,kind):
  structured=[]
  for view in decisions:
   if view['source']!=rel:continue
   u=dict(kind='structured-decision-view',text='\n'.join((SRC/rel).read_text().splitlines()[view['start']-1:view['end']]),start=view['start'],end=view['end'])
   record(rel,u,ROOT/(rel+'.sudo.md'),'model-request-structured-view',view['title'])
   structured += ['## '+view['title'],'', 'Structured view of the same source instructions, not an additional pass or an assertion of model compliance.','',
     '```sudo',f"// Source: {rel}:{view['start']}-{view['end']}",view['code'],'```','']
  content=content[:2+len(common)]+structured+content[2+len(common):]
  target=ROOT/(rel+'.sudo.md');target.parent.mkdir(parents=True,exist_ok=True)
  target.write_text('\n'.join(content)+'\n')
  manifest.append(dict(source=rel,representation=target.relative_to(OUT).as_posix(),kind=kind,
                       source_sha256=hashlib.sha256((SRC/rel).read_bytes()).hexdigest(),
                       representation_sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
  return target
 common=['Model-request representation: these constraints describe instructions addressed to a model.',
         'They do not execute the host workflow, prove compliance, or require every available tool to be called.',
         'Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.',
         'Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.',
         'Qualitative words, exceptions, contradictions and example values retain their source meanings.',
         'Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.','']
 for path in MARKDOWN:
  if not path.exists():continue
  rel=path.relative_to(SRC).as_posix();text=path.read_text();target=ROOT/(rel+'.sudo.md')
  content=[f'# {rel} — model instructions','',*common]
  if rel.startswith('vvaharness/skills/'):
   content += ['Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.', '']
  elif 'validation' in rel:
   content += ['Supply relationship: validation configuration/session/launcher and subagent loaders select system, rule, skill and persona text; effective permissions are separately built by executable code.', '']
  else:content += ['Supply relationship: operator-facing agent instructions; not an automatic scan-stage action. Packaged installation is separately represented in agentdoc/setup code.','']
  # Frontmatter is role/tool configuration, not a prose body or runtime guarantee.
  offset=0
  if text.startswith('---\n'):
   end=text.find('\n---',4)
   if end>=0:
    endline=text[:end+4].count('\n')+1
    content += ['## Declared request metadata','', '```sudo',f'// Source: {rel}:1-{endline}', 'Constraints {']
    data=yaml.safe_load(text[4:end]) or {}
    for key,value in data.items():
     content.append(f'  The source declares {key} = {json.dumps(value,ensure_ascii=False)}. Tool lists here describe the request profile; source loaders determine actual grants.')
     if key=='description' and isinstance(value,str):content.append('  '+natural(value))
     prior=[r for r in existing.get(key,[]) if r['role']=='resource key' or 'member' in r['role'] or 'binding' in r['role']]
     vocab.append(dict(source=rel,identifier=key,definition='Source request metadata field '+key,why='preserve persona/skill role and declared tool/profile configuration',kind='tool-specific identifier',original=key,
        line_start=1,line_end=endline,used_in=target.relative_to(OUT).as_posix(),reuse='reused existing spelling; source request metadata meaning documented separately' if prior else 'new source-specific metadata record; absent matching prior metadata entry',
        previous='; '.join(r['source']+':'+r['line_start'] for r in prior[:3])))
    for key,value in data.items():
     if key=='description':continue
     values=value if isinstance(value,list) else [value]
     for identifier in values:
      if not isinstance(identifier,str) or not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.-]*',identifier):continue
      prior=[r for r in existing.get(identifier,[]) if r['source']==rel]
      vocab.append(dict(source=rel,identifier=identifier,definition='Declared '+key+' metadata value; this names the source persona/skill/model/tool profile, not an effective permission guarantee',why='preserve named role, model choice and advertised tool/skill references',kind='tool-specific identifier',original=identifier,line_start=1,line_end=endline,used_in=target.relative_to(OUT).as_posix(),reuse='reused source-local vocabulary spelling' if prior else 'new source metadata reference; existing spellings checked without merging contexts',previous='; '.join(r['source']+':'+r['line_start'] for r in prior[:3]) if prior else ('checked existing vocabulary: '+str(len(existing.get(identifier,[])))+' other-context matches')))
    content += ['}','```','']
    offset=endline;text='\n'.join(text.splitlines()[offset:])
  section=[]
  for u in units(text,offset+1):
   if u['kind']=='separator':continue
   if u['kind']=='heading':
    level=len(u['text'])-len(u['text'].lstrip('#'))
    section=section[:level-1]+[u['text'].lstrip('# ')]
    content += [u['text'],''];continue
   record(rel,u,target,'model-request',' / '.join(section))
   if u['kind']=='item' and u['indent']:content += [f'Nested source item (indent {u["indent"]}); applies within the preceding source list/criterion.','']
   content += ['```sudo',*block(rel,u),'```','']
  write(rel,content,'markdown-model-instructions')
  coverage.append(dict(source=rel,content='Markdown role, procedures, constraints, criteria, examples and output requirements',status='converted-model-instructions',representation=target.relative_to(OUT).as_posix(),notes='exact original remains evidence; no model compliance inferred'))
 # Triage every maximal Python literal/template; no extraction heuristic is a proof of use.
 for path in sorted(SRC.rglob('*.py')):
  if 'tests' in path.relative_to(SRC).parts:continue
  rel=path.relative_to(SRC).as_posix();content=[f'# {rel} — model instruction carriers','',*common];converted=0
  target=ROOT/(rel+'.sudo.md')
  for carrier in python_carriers(path):
   node=carrier['node'];r=dict(source=rel,line_start=node.lineno,line_end=node.end_lineno,column=node.col_offset,
      owner=carrier['owner'],binding=carrier['binding'],status=carrier['role'],reason=carrier['reason'],representation='')
   if carrier['role'].startswith('converted'):
    converted+=1;r['representation']=target.relative_to(OUT).as_posix()
    content += [f'## {carrier["binding"] or carrier["owner"]} — source lines {node.lineno}–{node.end_lineno}', '',
     f'Source context: callable `{carrier["owner"]}`; enclosing call `{carrier["call_name"] or "none"}`; keyword `{carrier["keyword"] or "none"}`.',
     'Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.','']
    if carrier['role']=='converted-conditional-instructions':content += ['Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.','']
    if carrier['role']=='converted-tool-description':content += ['Role: advertised tool description; it guides understanding/selection if exposed, and does not command invocation.','']
    if carrier['slots']:
     content += ['Dynamic values are inserted in source expression order (format conversions/specifiers remain in exact expression evidence):','']
     for slot in carrier['slots']:content.append('- `'+slot+'`')
     content.append('')
    if carrier['format_call']:content += ['Formatting/composition call retained as source expression evidence:', '', '````python',carrier['format_call'],'````','']
    for u in units(carrier['text'],node.lineno):
     # Runtime text newlines are not source newlines (concatenation/f-strings).
     # Cite the exact containing expression, never fabricate per-runtime-line ranges.
     u['start'],u['end']=node.lineno,node.end_lineno
     if u['kind']=='separator':continue
     if u['kind']=='heading':content += [u['text'],''];continue
     record(rel,u,target,carrier['role'],carrier['binding'] or carrier['owner'])
     content += ['```sudo',*block(rel,u,'description' if carrier['role']=='converted-tool-description' else 'instruction'),'```','']
   triage.append(r)
  if converted:
   write(rel,content,'python-model-instructions')
   coverage.append(dict(source=rel,content=f'{converted} instruction/description carriers',status='converted-model-instructions',representation=target.relative_to(OUT).as_posix(),notes='all other Python carriers independently dispositioned in prompt_content_triage.tsv'))
 # Embedded Python probe code receives the same carrier triage; none currently
 # carries model instructions. Fail rather than silently omit a future new one.
 with (OUT/'embedded_python.tsv').open() as f:
  for row in csv.DictReader(f,delimiter='\t'):
   path=SRC/row['source'];start,end=int(row['line_start']),int(row['line_end'])
   snippet='\n'.join(path.read_text().splitlines()[start-1:end])
   for carrier in python_carriers(path,snippet,start-1):
    node=carrier['node']
    assert not carrier['role'].startswith('converted'), 'New embedded instruction requires a behavioral view: '+row['source']
    triage.append(dict(source=row['source'],line_start=node.lineno,line_end=node.end_lineno,column=node.col_offset,
      owner=carrier['owner'],binding=carrier['binding'],status=carrier['role'],reason='embedded Python: '+carrier['reason'],representation=''))
 # Resource text: selected supplied instruction-bearing sources; ordinary configs
 # remain source data with executable interpretation in code, not invented prompts.
 resource_names=['inputs/remediation_playbook.yaml','inputs/validator_hints.yaml','inputs/remediation_policy.yaml',
                 'inputs/remediation_policy.yaml.example','inputs/design_controls.example.yaml','inputs/known_cves.example.json',
                 'vvaharness/rules/generic.kb.yaml']
 resource_names=list(dict.fromkeys(resource_names+[p.relative_to(SRC).as_posix() for p in sorted(SRC.rglob('*'))
    if p.is_file() and 'tests' not in p.relative_to(SRC).parts and p.relative_to(SRC).parts[0] in ('vvaharness','inputs') and p.suffix in ('.yaml','.yml','.json')]))
 for rel in resource_names:
  path=SRC/rel
  if not path.exists():continue
  text=path.read_text();content=[f'# {rel} — supplied guidance and request data','',*common]
  target=ROOT/(rel+'.sudo.md');count=0
  if rel=='inputs/remediation_playbook.yaml':content += ['Activation boundary: Playbook._load reads cwe and policy. Strategy.as_prompt_block supplies the selected instruction, optional example_after and allowed_deps; the root prompt_template is not read by this loader. Its instructions are converted as inactive supplied content, not an asserted dispatch path.','']
  if rel=='inputs/known_cves.example.json':
   # Supplied CVE descriptions are context, not behavioral commands.
   coverage.append(dict(source=rel,content='CVE/context example JSON',status='evidence-only-data',representation='source_detail/'+rel+'.sudo.md',notes='no behavioral instruction assumed from vulnerability context; loader/use is represented in code'));continue
  tree=yaml.compose(text)
  def walk(node,keys=()):
   if isinstance(node,yaml.MappingNode):
    for key,value in node.value:yield from walk(value,(*keys,key.value))
   elif isinstance(node,yaml.SequenceNode):
    for i,value in enumerate(node.value):yield from walk(value,(*keys,str(i)))
   else:yield keys,node
  cwe_context={}
  if rel.endswith('generic.kb.yaml'):
   loaded=yaml.safe_load(text) or {}
   for i,entry in enumerate(loaded.get('entries',[])):
    cwe_context[str(i)]=(entry.get('cwe',''),entry.get('title',''))
   for ctx_keys,ctx_node in walk(tree):
    if len(ctx_keys)==3 and ctx_keys[0]=='entries' and ctx_keys[2]=='cwe':
     prior=[r for r in existing.get(ctx_node.value,[]) if r['source']==rel]
     vocab.append(dict(source=rel,identifier=ctx_node.value,definition='CWE selector for the knowledge-base entry whose source/sink/sanitizer/FP criteria are supplied together',why='keep each criterion associated with its original weakness class',kind='tool-specific identifier',original=ctx_node.value,line_start=ctx_node.start_mark.line+1,line_end=ctx_node.start_mark.line+1,used_in=target.relative_to(OUT).as_posix(),reuse='reused existing local vocabulary entry' if prior else 'newly recorded source CWE selector; vocabulary checked before addition',previous='; '.join(r['source']+':'+r['line_start'] for r in prior[:3]) if prior else 'checked vocabulary_symbols.tsv and resource_vocabulary.tsv; no matching local entry'))
  for keys,node in walk(tree):
   if node.tag!='tag:yaml.org,2002:str' or not node.value.strip():continue
   field=keys[-2] if keys[-1].isdigit() and len(keys)>1 else keys[-1]
   semantic_field=bool(re.search(r'prompt|instruction|guidance|fp_checks|sanitizers|sources|sinks|rationale|notes|description|hint',field,re.I))
   if len(re.findall(r'[A-Za-z]{2,}',node.value))<2 and not (semantic_field or rel.endswith('validator_hints.yaml') or field.startswith('example_')):continue
   if not (semantic_field or DIRECTIVE.search(node.value) or rel.endswith('validator_hints.yaml') or field.startswith('example_')):continue
   # Code samples remain examples, not guaranteed model/host edits.
   example=any(k.startswith('example_') for k in keys)
   end=min(len(text.splitlines()),max(node.start_mark.line+1,node.end_mark.line+(1 if node.end_mark.column else 0)))
   u=dict(kind='example' if example else 'paragraph',text=('```source\n'+node.value+'\n```') if example else node.value,start=node.start_mark.line+1,end=end,indent=0)
   label='.'.join(keys)
   content += [f'## {label}','', 'Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.','']
   if rel.endswith('generic.kb.yaml'):
    cwe,title=cwe_context.get(keys[1],('',''))
    content += ['Source CWE-entry selector: `'+cwe+'` — '+title+'. The array index in the heading identifies this original entry, not a new priority/order.','']
    field=keys[-2] if keys[-1].isdigit() and len(keys)>1 else keys[-1]
    content += [f'Guidance role: `{field}` in this source CWE entry. Sources/sinks are candidate patterns; sanitizers/non_sanitizers/FP checks are decision criteria, not guaranteed code facts.','']
   record(rel,u,target,'configured-model-guidance',label)
   field=keys[-2] if keys[-1].isdigit() and len(keys)>1 else keys[-1]
   if field in ('sources','sinks','sanitizers','non_sanitizers','fp_checks'):
    content += ['```sudo',f"// Source: {rel}:{u['start']}-{u['end']}",'Constraints {',
      '  The model is supplied the following '+field+' criterion for this particular CWE entry: '+re.sub(r'\s+',' ',node.value),
      '  It is asked to assess applicability from actual evidence; this criterion is not proof the condition holds.','}','```','']
   else:content += ['```sudo',*block(rel,u),'```','']
   count+=1
  if count:
   write(rel,content,'resource-model-guidance')
   coverage.append(dict(source=rel,content=f'{count} guidance/template/example values',status='converted-model-instructions',representation=target.relative_to(OUT).as_posix(),notes='selection, substitution and activation remain source-loader decisions; policy executable enforcement is separate'))
 # Probe output can instruct the model even though the shell itself only prints.
 # Convert literal output/heredoc text separately from executable shell operations.
 for path in sorted(SRC.rglob('*.sh')):
  if 'tests' in path.relative_to(SRC).parts:continue
  rel=path.relative_to(SRC).as_posix();text=path.read_text();lines=text.splitlines()
  target=ROOT/(rel+'.sudo.md');content=[f'# {rel} — model-visible probe feedback','',*common];count=0;i=0
  while i<len(lines):
   line=lines[i];match=re.search(r"<<-?\s*['\"]?([A-Za-z_]\w*)['\"]?",line)
   if match:
    begin=i+1;end=begin
    while end<len(lines) and lines[end].strip()!=match.group(1):end+=1
    if match.group(1)!='PY' and end>begin:
     for u in units('\n'.join(lines[begin:end]),begin+1):
      if u['kind'] in ('heading','separator'):continue
      record(rel,u,target,'conditional-probe-feedback','literal heredoc output')
      content += ['```sudo',*block(rel,u),'```',''];count+=1
    i=end
   elif not line.lstrip().startswith('#') and re.search(r'\b(?:echo|printf)\b',line):
    # Literal emission format is evidence; parameter expansion stays source-controlled.
    fragments=re.findall(r"'([^']*)'|\"([^\"]*)\"",line)
    for fragment in fragments:
     value=next((v for v in fragment if v),'')
     if not DIRECTIVE.search(value):continue
     u=dict(kind='paragraph',text=value,start=i+1,end=i+1,indent=0)
     record(rel,u,target,'conditional-probe-feedback','printed shell message')
     content += ['```sudo',*block(rel,u),'```',''];count+=1
   i+=1
  if count:
   write(rel,content,'shell-model-feedback')
   coverage.append(dict(source=rel,content=f'{count} literal output guidance units',status='converted-model-instructions',representation=target.relative_to(OUT).as_posix(),notes='only a tool invocation exposes this feedback; shell execution and stdout formatting remain source-defined'))
 # All other Markdown/config/resources receive an explicit evidence-only disposition.
 converted_sources={r['source'] for r in coverage}
 with (OUT/'resource_coverage.tsv').open() as f:
  for row in csv.DictReader(f,delimiter='\t'):
   rel=row['source']
   if rel in converted_sources or row['status']=='excluded-test':continue
   coverage.append(dict(source=rel,content=row['role'],status='evidence-only-data',representation=row['representation'],notes='resource/build/documentation/example; no model-behavior instructions established by this source classification'))
 # Look up every explicit prompt identifier before recording it. Natural English
 # in a Constraints body is baseline prose, not a declared identifier.
 seen_vocab={(r['source'],r['identifier']) for r in vocab}
 for unit in allunits:
  text=unit['source_text'];rel=unit['source']
  names=set()
  for token in re.findall(r'`([^`\n]+)`',text):
   if re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.-]*',token):names.add(token)
  names.update(re.findall(r'\b(?:[a-z]+_[a-z_]+|[A-Z][a-z]+[A-Z][A-Za-z]*|CWE-\d+|TRUE_POSITIVE|FALSE_POSITIVE|INCONCLUSIVE)\b',text))
  names.update(set(re.findall(r'\b[A-Z][A-Z0-9_]{1,}\b',text))-set('A AN AND ARE AS AT BE BEFORE BY CAN DO DOES EACH EVERY FOR FROM HAS HAVE IF IN IS IT ITS MUST NEVER NO NOT OF ON ONLY OR OTHERWISE SHOULD SO THAT THE THEN THERE THESE THIS TO USE WHEN WHERE WHICH WITH WITHOUT YOU YOUR'.split()))
  if unit['source_label'] and re.fullmatch(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*',unit['source_label']):names.add(unit['source_label'])
  for identifier in sorted(names):
   if (rel,identifier) in seen_vocab:continue
   seen_vocab.add((rel,identifier))
   prior=[r for r in existing.get(identifier,[]) if r['source']==rel]
   other=existing.get(identifier,[])
   vocab.append(dict(source=rel,identifier=identifier,
     definition=('Reuse the existing local '+prior[0]['role']+': '+prior[0]['definition'][:500]) if prior else 'Source-spelled prompt identifier/pattern in '+(unit['source_label'] or unit['role'])+': '+re.sub(r'\s+',' ',text)[:500],
     why='retain the instruction-specific field, tool, enum, pattern or subject without merging its source context',kind='tool-specific identifier',original=identifier,
     line_start=unit['line_start'],line_end=unit['line_end'],used_in=unit['representation'],
     reuse='reused existing local vocabulary entry' if prior else 'newly recorded source prompt identifier; no matching local vocabulary entry',
     previous='; '.join(r['source']+':'+r['line_start']+' '+r['role'] for r in prior[:3]) if prior else ('same-spelled entries checked, distinct source context: '+'; '.join(r['source']+':'+r['line_start'] for r in other[:3]) if other else 'checked vocabulary_symbols.tsv and resource_vocabulary.tsv: no matching spelling')))
 write_tsv(OUT/'prompt_content_coverage.tsv',['source','content','status','representation','notes'],coverage)
 write_tsv(OUT/'prompt_content_triage.tsv',['source','line_start','line_end','column','owner','binding','status','reason','representation'],triage)
 write_tsv(OUT/'prompt_vocabulary.tsv',['source','identifier','definition','why','kind','original','line_start','line_end','used_in','reuse','previous'],vocab)
 (OUT/'prompt_conversion_units.json').write_text(json.dumps(allunits,indent=2,ensure_ascii=False)+'\n')
 (OUT/'prompt_conversion_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 active_views={r['representation'] for r in manifest}
 for old in ROOT.rglob('*.sudo.md'):
  if old.relative_to(OUT).as_posix() not in active_views:old.unlink()
 print(json.dumps({'files':len(manifest),'converted_units':len(allunits),'carrier_statuses':dict(Counter(r['status'] for r in triage)),'coverage_statuses':dict(Counter(r['status'] for r in coverage))},indent=2))

if __name__=='__main__':main()
