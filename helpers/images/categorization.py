import pymupdf

def img_categorization(doc, output_path):
    path = f"{output_path}/categorization"
    page = doc.load_page(18)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        if 'Abacaxis' in text:
            break
    rect = pymupdf.Rect(x0, y0, x1, y1) # type: ignore
    zoom = 3 
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    pix.save(f'{path}/table.png')