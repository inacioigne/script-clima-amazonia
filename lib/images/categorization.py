from pathlib import Path
from PIL import Image
import io

import pymupdf

def img_categorization(doc, output_path):
    
    # path = f"{output_path}/categorization"
    path = Path(output_path, "categorization")
    path.mkdir(parents=True, exist_ok=True)
    page = doc.load_page(18)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        if 'Abacaxis' in text:
            break
    rect = pymupdf.Rect(x0, y0, x1, y1) # type: ignore
    zoom = 3 
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    img_bytes = pix.tobytes("png")
    image = Image.open(io.BytesIO(img_bytes))
    output_file = Path(path, "table.webp")
    image.save(
    output_file,
    "WEBP",
    quality=50,
    method=6
    )
    # pix.save(f'{path}/table.png')