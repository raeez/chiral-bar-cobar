from pathlib import Path
import hashlib,json,subprocess,shutil
root=Path.cwd();r=root/'reports/research/cbc_native026/candidate002';src=root/'research-candidates/cbc_native026/candidate002';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((r/'source-manifest.json').read_text());assert all(sha(root/x['path'])==x['sha256'] for x in m['source_files'])
parent=json.loads((r/'parent-source-manifest.json').read_text());assert all(sha(root/x['path'])==x['sha256'] for x in parent['source_files'])
rows=[];objects=r/'tex-inputs';objects.mkdir(exist_ok=True)
for kind,stem in [('proof','comparison_main'),('native','main')]:
 cwd=src/('proof' if kind=='proof' else 'cbc')
 fls=r/('build-'+kind)/(stem+'.fls')
 seen=set()
 for line in fls.read_text().splitlines():
  if not line.startswith('INPUT '):continue
  p=Path(line[6:]);p=p if p.is_absolute() else cwd/p;p=p.resolve()
  if p in seen or not p.is_file():continue
  seen.add(p);h=sha(p);obj=objects/h
  if not obj.exists():shutil.copyfile(p,obj)
  rows.append({'kind':kind,'path':str(p),'sha256':h,'object':str(obj.relative_to(r))})
(r/'build-input-closure.json').write_text(json.dumps(rows,indent=2)+'\n')
checks={'source_manifest_sha256':sha(r/'source-manifest.json'),'source_count':len(m['source_files']),'parent76_preserved':True,'build_inputs':len(rows),'unique_input_objects':len(list(objects.iterdir())),'pdfs':{}}
for kind,stem in [('proof','comparison_main'),('native','main')]:
 p=r/('build-'+kind)/(stem+'.pdf');info=subprocess.check_output(['pdfinfo',str(p)],text=True);(r/(kind+'-pdfinfo.txt')).write_text(info);checks['pdfs'][kind]={'sha256':sha(p),'pages':int(next(x for x in info.splitlines() if x.startswith('Pages:')).split(':')[1]),'build_report':kind+'-build.json'}
(r/'verification.json').write_text(json.dumps(checks,indent=2)+'\n');print(json.dumps(checks))
