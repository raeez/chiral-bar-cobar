from pathlib import Path
import hashlib,json,difflib,subprocess,re
root=Path(__file__).resolve().parents[4]
report=Path(__file__).resolve().parent
source=root/'research-candidates/cbc_native026/candidate007'
parent=root/'research-candidates/cbc_native026/candidate006'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[];diff=[];hunks=[]
for p in sorted(source.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(source);prior=parent/rel;actual=sha(p);before=sha(prior) if prior.is_file() else None
 rows.append({'path':str(p.relative_to(root)),'sha256':actual,'parent_sha256':before,'changed':actual!=before})
 if actual==before:continue
 a=prior.read_text().splitlines(True) if prior.is_file() else [];b=p.read_text().splitlines(True)
 diff.extend(difflib.unified_diff(a,b,fromfile='candidate006/'+str(rel),tofile='candidate007/'+str(rel)))
 for tag,i,j,x,y in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes():
  if tag!='equal':hunks.append({'file':str(rel),'old_lines':[i+1,j],'new_lines':[x+1,y],'operation':tag})
(report/'source.diff').write_text(''.join(diff))
manifest={'base_head':subprocess.run(['git','rev-parse','HEAD'],capture_output=True,text=True,check=True,cwd=root).stdout.strip(),'parent_source_manifest':sha(root/'reports/research/cbc_native026/candidate006/source-manifest.json'),'parent_final_manifest':sha(root/'reports/research/cbc_native026/candidate006/final-manifest.json'),'source_files':rows,'aggregate_diff_sha256':sha(report/'source.diff'),'status':'Frozen for exact build/render and fresh independent review; not accepted.'}
(report/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
(report/'changed-ranges.json').write_text(json.dumps(hunks,indent=2)+'\n')
# Preserve every old file, not merely previously accepted proof bodies.
old=json.loads((root/'reports/research/cbc_native026/candidate006/final-manifest.json').read_text())
checks=[{'path':r['path'],'expected':r['sha256'],'actual':sha(root/r['path'])} for r in old['files']]
assert all(r['expected']==r['actual'] for r in checks)
(report/'parent-exit-custody.json').write_text(json.dumps({'files_verified':len(checks),'parent_final_manifest_sha256':sha(root/'reports/research/cbc_native026/candidate006/final-manifest.json'),'files':checks},indent=2)+'\n')
proofs=['ds_chain_comparisons','affine_ds_global','relative_p1_comparison','unital_p1_chains','elliptic_normalizations','elliptic_propagator','edge_contraction_signs']
preserved=[]
for name in proofs:
 p=source/'cbc/chapters/theory'/(name+'.tex');q=parent/p.relative_to(source)
 assert sha(p)==sha(q)
 preserved.append({'path':str(p.relative_to(root)),'sha256':sha(p),'parent_sha256':sha(q),'identical':True})
(report/'preservation.json').write_text(json.dumps({'named_proof_files':preserved,'all_other_source_files':rows,'subregular_ds_change':'Only the primary-source good-grading page locator changes from 3–5 to 3–6.'},indent=2)+'\n')
print(json.dumps({'source_files':len(rows),'changed_files':sum(r['changed'] for r in rows),'source_manifest_sha256':sha(report/'source-manifest.json'),'aggregate_diff_sha256':sha(report/'source.diff'),'parent_files_verified':len(checks)},indent=2))
