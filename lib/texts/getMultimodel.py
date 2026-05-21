import pymupdf
import re

def get_multimodel(pathPT, pathEN, pathES, bulletin_dict):
    multimodel = {
        "pt": {},
        "en": {},
        "es": {}
    }
    # pt
    doc = pymupdf.open(pathPT)
    page = doc.load_page(15)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        if "A Figura acima," in text:
            seven_days = text.replace("\n", "")
            seven_days = seven_days.replace("acima, ", "")
            multimodel['pt']['seven_days'] = seven_days
            break
    page = doc.load_page(16)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        if "A Figura acima," in text:
            fourteen_days = text.replace("\n", "")
            fourteen_days = fourteen_days.replace("acima, ", "")
            multimodel['pt']['fourteen_days'] = fourteen_days
            break
    # en
    doc = pymupdf.open(pathEN)
    page = doc.load_page(15)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        text = re.sub(r'\s+', ' ', text).strip()
        if "The figure above"in text:
            seven_days = text.replace("\n", "")
            seven_days = seven_days.replace("above ", "")
            multimodel['en']['seven_days'] = seven_days
            break
    page = doc.load_page(16)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        text = re.sub(r'\s+', ' ', text).strip()
        if "The figure above" in text:
            fourteen_days = text.replace("\n", "")
            fourteen_days = fourteen_days.replace("above ", "")
            multimodel['en']['fourteen_days'] = fourteen_days
            break
    # es
    doc = pymupdf.open(pathES)
    page = doc.load_page(15)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        text = re.sub(r'\s+', ' ', text).strip()
        if "La figura de arriba"in text:
            seven_days = text.replace("\n", "")
            seven_days = seven_days.replace("de arriba ", "")
            multimodel['es']['seven_days'] = seven_days
            break
    page = doc.load_page(16)
    blocks = page.get_text("blocks")
    for x0, y0, x1, y1, text, *_ in blocks:
        text = re.sub(r'\s+', ' ', text).strip()
        if "La figura de arriba" in text:
            fourteen_days = text.replace("\n", "")
            fourteen_days = fourteen_days.replace("de arriba ", "")
            multimodel['es']['fourteen_days'] = fourteen_days
            break

    bulletin_dict['multimodel'] = multimodel


    return bulletin_dict