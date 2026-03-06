import pymupdf

def img_reference(doc, output_path, edition):
    path = f"{output_path}/{edition}/reference"
    page = doc.load_page(17)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        if 'Abacaxis' in text:
            break
    rect = pymupdf.Rect(x0, y0, x1, y1) # type: ignore
    zoom = 3 
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    pix.save(f'{path}/reference_table.png')