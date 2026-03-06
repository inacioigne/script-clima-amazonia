import pymupdf

def img_anomaly(doc, output_path, edition):
    c = 1
    path = f"{output_path}/{edition}/anomaly"
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
                pix.save(f'{path}/bacia_{c}.png')
                c += 1