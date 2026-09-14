from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw
import subprocess,json,hashlib

root=Path(__file__).resolve().parents[3]
r=root/'reports/research/cbc_native026'
pdf=r/'build-native/main.pdf'
selection=json.loads((r/'native-page-selection.json').read_text())['selected_pages']
out=r/'render-native';out.mkdir(exist_ok=True)
def render(n):
    base=out/f'page-{n:04}'
    argv=['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-scale-to','1250','-png',str(pdf),str(base)]
    subprocess.run(argv,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    p=base.with_suffix('.png')
    return {'page':n,'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'argv':argv}
with ThreadPoolExecutor(max_workers=6) as pool: rows=list(pool.map(render,selection))
for n in range(0,len(rows),4):
    canvas=Image.new('RGB',(1610,2070),'#aaaaaa')
    for j,row in enumerate(rows[n:n+4]):
        im=Image.open(root/row['path']).convert('RGB');im.thumbnail((775,1000))
        tile=Image.new('RGB',(805,1035),'#d0d0d0');tile.paste(im,((805-im.width)//2,25))
        ImageDraw.Draw(tile).text((12,5),f"Page {row['page']}",fill='black')
        canvas.paste(tile,((j%2)*805,(j//2)*1035))
    canvas.save(out/f'montage-{n//4+1:02}.png')
(r/'native-render-binding.json').write_text(json.dumps({'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':rows},indent=2)+'\n')
print('Rendered',len(rows),'native pages')
