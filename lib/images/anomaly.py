import pymupdf
from pathlib import Path
from PIL import Image
import io

def img_anomaly(doc, output_path):
    
    c = 1
    # path = f"{output_path}/anomaly"
    path = Path(output_path, "anomaly")
    path.mkdir(parents=True, exist_ok=True)
    for p in range(19,23):
        page = doc.load_page(p)
        d = page.get_text("dict")
        blocks = d["blocks"] 
        imgblocks = [b for b in blocks if b["type"] == 1]
        for i in imgblocks:
            if i['height'] > 250:
                bbox = i['bbox']
                rect = pymupdf.Rect(bbox)
                zoom = 3
                mat = pymupdf.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
                img_bytes = pix.tobytes("png")
                image = Image.open(io.BytesIO(img_bytes))
                output_file = Path(path, f"bacia_{c}.webp")
                image.save(
                output_file,
                "WEBP",
                quality=50,
                method=6
                )
                c += 1