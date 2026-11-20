"""Connect converted model instructions to structural and mirrored source views."""
import hashlib,json,os,re
from pathlib import Path
OUT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def link(origin,target):return os.path.relpath(target,origin.parent)
manifest=json.loads((OUT/'prompt_conversion_manifest.json').read_text())
marker='\n<!-- converted-model-instructions -->\n'
active={r['source'] for r in manifest}
for detail in (OUT/'source_detail').rglob('*.sudo.md'):
 rel=detail.relative_to(OUT/'source_detail').as_posix().removesuffix('.sudo.md')
 if rel not in active and marker in detail.read_text():detail.write_text(detail.read_text().split(marker)[0])
for row in manifest:
 target=OUT/row['representation'];detail=OUT/'source_detail'/(row['source']+'.sudo.md')
 if row['kind']=='markdown-model-instructions':
  detail.parent.mkdir(parents=True,exist_ok=True)
  detail.write_text(target.read_text()+marker+'Original supporting evidence: [exact source copy]('+link(detail,OUT/'assets/original'/row['source'])+').\n')
 elif detail.exists():
  body=detail.read_text().split(marker)[0]
  detail.write_text(body+marker+'Model behavior requested by this source: [converted instructions]('+link(detail,target)+'). Exact strings in the evidence asset support this conversion.\n')
# Links on readable workflow/components do not change their execution hierarchy.
for path in (OUT/'representation').rglob('*.sudo.md'):
 original=path.read_text().split(marker)[0]
 if path.name=='harness.sudo.md':selected=manifest
 else:
  rel=path.relative_to(OUT/'representation').as_posix().removesuffix('.sudo.md')
  selected=[r for r in manifest if r['source']==rel+'.py' or r['source'].startswith(rel+'/')]
 if selected:
  path.write_text(original+marker+'Requested model behavior is expanded in the [prompt workflow map]('+link(path,OUT/'prompt_workflow.sudo.md')+').\n\n'+ '\n'.join('- ['+r['source']+']('+link(path,OUT/r['representation'])+')' for r in selected)+'\n')
structural=json.loads((OUT/'structural_manifest.json').read_text())
for row in structural:row['representation_sha256']=digest(OUT/row['representation'])
(OUT/'structural_manifest.json').write_text(json.dumps(structural,indent=2)+'\n')
print('Integrated',len(manifest),'converted prompt source views; Markdown source_detail now contains converted instructions.')
