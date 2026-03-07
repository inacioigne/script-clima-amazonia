import pymupdf

def img_multimodel(doc, output_path):
    path = f"{output_path}/multimodel"
    page = doc.load_page(15)
    d = page.get_text("dict")
    blocks = d["blocks"] 
    imgblocks = [b for b in blocks if b["type"] == 1]
    for i in imgblocks:
        if i['height'] > 400:
            img = i
            print(img)
            break
    left, top, right, bottom = img['bbox'] # type: ignore
    right += 100
    rect = pymupdf.Rect(left, top, right, bottom)
    zoom = 3
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    pix.save(f'{path}/seven_days.png')
    
    # fourteen_days
    page = doc.load_page(16)
    d = page.get_text("dict")
    blocks = d["blocks"] 
    imgblocks = [b for b in blocks if b["type"] == 1]
    for i in imgblocks:
        if i['height'] > 400:
            img = i
            print(img)
            break
    left, top, right, bottom = img['bbox'] # type: ignore
    right += 100
    rect = pymupdf.Rect(left, top, right, bottom)
    zoom = 3
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    pix.save(f'{path}/fourteen_days.png')