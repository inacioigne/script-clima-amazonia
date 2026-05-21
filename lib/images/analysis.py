from pathlib import Path
from PIL import Image
import io

from lib.helpers.slugify import slugify

def img_analysis(doc, output_path):
    bacias = ['Bacia do Rio Branco', 'Bacia do Rio Negro','Bacia do Rio Marañon', 'Bacia do Rio Ucayali', 'Bacia do Rio Napo', 
    'Curso principal do Rio Amazonas (Peru)','Bacia do Rio Javari','Bacia do Rio Içá (Putumayo)','Bacia do Rio Jutaí','Bacia do Rio Juruá',
    'Bacia do Rio Japurá (Caquetá)','Bacia do Rio Tefé','Bacia do Rio Coari','Bacia do Rio Purus','Curso principal do Rio Solimões',
    'Bacia dos rios Beni e Madre de Dios','Bacia do Rio Mamoré','Bacia do Rio Guaporé (Iténez)','Bacia do Rio Ji-Paraná','Bacia do Rio Aripuanã',
    'Bacia do Rio Madeira','Bacias da margem esquerda do Rio Amazonas (Amazonas)','Bacia do Rio Abacaxis','Bacia do Rio Juruena','Bacia do Rio Teles Pires',
    'Bacia do Rio Tapajós','Bacias da margem esquerda do Rio Amazonas (noroeste do Pará)','Bacia do Rio Curuá Una','Bacias da margem esquerda do Rio Amazonas (nordeste do PA)',
    'Bacia do Rio Iriri','Bacia do Rio Xingu','Curso principal do Rio Amazonas (Brasil)']
    
    # path = f"{output_path}/analysis"
    path = Path(output_path, "analysis")
    path.mkdir(parents=True, exist_ok=True)
    images = []
    for b in bacias:
        slug_name = slugify(b)
        images.append(f'{slug_name}-acc.webp')
        images.append(f'{slug_name}-ano.webp')
    c = 0
    for i in range(4, 15):
        page = doc.load_page(i)
        d = page.get_text("dict")
        blocks = d["blocks"] 
        imgblocks = [b for b in blocks if b["type"] == 1]
        for i in imgblocks:
            if i['bbox'][0] < 100.0:
                img = i['image']
                img_name = images[c]
                output_file = f'{path}/{img_name}'
                image = Image.open(io.BytesIO(img))
                image.save(
                    output_file,
                    "WEBP",
                    quality=50,      
                    method=6        
                )
                # with open(f'{path}/{img_name}', "wb") as f:
                #                 f.write(img)
                c += 1