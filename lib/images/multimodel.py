from pathlib import Path
from PIL import Image
import io

import pymupdf

def img_multimodel(doc, output_path):
    
    # path = f"{output_path}/multimodel"
    path = Path(output_path, "multimodel")
    path.mkdir(parents=True, exist_ok=True)
    page = doc.load_page(15)
    d = page.get_text("dict")
    blocks = d["blocks"] 
    imgblocks = [b for b in blocks if b["type"] == 1]
    for i in imgblocks:
        if i['height'] > 400:
            img = i
            break
    left, top, right, bottom = img['bbox'] # type: ignore
    right += 100
    rect = pymupdf.Rect(left, top, right, bottom)
    zoom = 3
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    img_bytes = pix.tobytes("png")
    image = Image.open(io.BytesIO(img_bytes))
    output_file = Path(path, "seven_days.webp")
    image.save(
    output_file,
    "WEBP",
    quality=50,
    method=6
    )
    # pix.save(f'{path}/seven_days.png')
    
    # fourteen_days
    page = doc.load_page(16)
    d = page.get_text("dict")
    blocks = d["blocks"] 
    imgblocks = [b for b in blocks if b["type"] == 1]
    for i in imgblocks:
        if i['height'] > 400:
            img = i
            break
    left, top, right, bottom = img['bbox'] # type: ignore
    right += 100
    rect = pymupdf.Rect(left, top, right, bottom)
    zoom = 3
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    img_bytes = pix.tobytes("png")
    image = Image.open(io.BytesIO(img_bytes))
    output_file = Path(path, "fourteen_days.webp")
    image.save(
    output_file,
    "WEBP",
    quality=50,
    method=6
    )
    # pix.save(f'{path}/fourteen_days.png')