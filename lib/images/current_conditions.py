from pathlib import Path
from PIL import Image
import io

import pymupdf 

def img_current_conditions(doc, output_path):

    # path = f"{output_path}/current_conditions/"
    path = Path(output_path, f"current_conditions")
    path.mkdir(parents=True, exist_ok=True)
    page = doc.load_page(3)
    # maps
    d = page.get_text("dict")
    blocks = d["blocks"] 
    imgblocks = [b for b in blocks if b["type"] == 1]
    img = None
    for i in imgblocks:
        if i['height'] > 400:
            img = i['image'] 
            break
    if img is None:
        raise ValueError("Nenhuma imagem encontrada.")
    output_file = f'{path}/map_current_conditions.webp'
    image = Image.open(io.BytesIO(img))
    image.save(
        output_file,
        "WEBP",
        quality=50,      
        method=6        
    )
    # Tabels
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        if "1\nAbacaxis" in text:
            break

    top = y0 - 5 # type: ignore
    left = x0 - 15 # type: ignore
    right = x1 + 45 # type: ignore
    bottom = y1 + 5 # type: ignore
    rect = pymupdf.Rect(left, top, right, bottom)
    zoom = 3 
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    img_bytes = pix.tobytes("png")
    image = Image.open(io.BytesIO(img_bytes))
    output_file = Path(path, "table_current_conditions.webp")
    image.save(
    output_file,
    "WEBP",
    quality=50,
    method=6
    )
    # pix.save(f'{path}/table_current_conditions.png')