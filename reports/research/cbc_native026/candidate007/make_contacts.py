from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import json
report=Path(__file__).resolve().parent
rows=[]
for kind in ['proof','native']:
 files=sorted((report/('render-'+kind)).glob('*.png'));folder=report/('contacts-'+kind);folder.mkdir(exist_ok=True)
 for i in range(0,len(files),4):
  batch=files[i:i+4];canvas=Image.new('RGB',(1900,2460),'#dddddd');draw=ImageDraw.Draw(canvas)
  for j,p in enumerate(batch):
   im=Image.open(p).convert('RGB');canvas.paste(im,((j%2)*950,30+(j//2)*1230));draw.text(((j%2)*950+20,10+(j//2)*1230),p.stem,fill='black')
  out=folder/f'contact-{i//4+1:03d}.png';canvas.save(out);rows.append({'contact':str(out.relative_to(report)),'pages':[str(p.relative_to(report)) for p in batch]})
(report/'contact-pages.json').write_text(json.dumps(rows,indent=2)+'\n');print('contacts',len(rows))
