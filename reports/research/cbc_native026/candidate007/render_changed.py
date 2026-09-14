from pathlib import Path
import re,json,subprocess
from pypdf import PdfReader
root=Path(__file__).resolve().parents[4];report=Path(__file__).resolve().parent;source=root/'research-candidates/cbc_native026/candidate007'
kind=__import__('sys').argv[1];stem={'native':'main','proof':'comparison_main'}[kind]
pdf=report/('build-'+kind)/(stem+'.pdf')
reader=PdfReader(pdf);page_labels=reader.page_labels
label_to_index={label:i+1 for i,label in enumerate(page_labels)}
labels={}
for p in (report/('build-'+kind)).rglob('*.aux'):
 for name,page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^\n]*?\}\{([^}]+)\}',p.read_text(errors='replace')):
  if page in label_to_index:labels[name]=label_to_index[page]
selected=set();anchors=[]
if kind=='proof':selected.update(range(45,len(reader.pages)+1))
else:
 hunks=json.loads((report/'changed-ranges.json').read_text())
 for h in hunks:
  if not h['file'].startswith('cbc/'):continue
  lines=(source/h['file']).read_text().splitlines()
  locations=[(i+1,n) for i,l in enumerate(lines) for n in re.findall(r'\\label\{([^}]+)\}',l) if n in labels]
  lo,hi=h['new_lines'];hi=max(lo,hi)
  before=[x for x in locations if x[0]<=lo];after=[x for x in locations if x[0]>=hi]
  within=[x for x in locations if lo<=x[0]<=hi]
  picks=(before[-1:] if before else [])+within+(after[:1] if after else [])
  if picks:
   nums=[labels[n] for _,n in picks]
   # Source input statements may sit between distant chapter labels. Keep the selected anchors when wide.
   if max(nums)-min(nums)<=18:
    pages=set(range(max(1,min(nums)-1),min(len(reader.pages),max(nums)+1)+1))
   else:pages={j for n in nums for j in [n-1,n,n+1] if 1<=j<=len(reader.pages)}
   selected.update(pages);anchors.append({'hunk':h,'labels':picks,'physical_pages':sorted(pages)})
 # Include the two reflowed inherited paragraphs explicitly by printed page label.
 for label in ['537','1502']:
  if label in label_to_index:selected.add(label_to_index[label])
folder=report/('render-'+kind);folder.mkdir(exist_ok=True)
for page in sorted(selected):
 subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1200','-png',str(pdf),str(folder/f'page-{page:04d}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
(report/(kind+'-render-pages.json')).write_text(json.dumps({'pdf':str(pdf.relative_to(root)),'physical_pages':sorted(selected),'page_labels':{str(i):page_labels[i-1] for i in sorted(selected)},'selection':anchors},indent=2)+'\n')
print(kind,'rendered',len(selected),'pages',sorted(selected))
