import pymupdf
import re

def get_current_conditions(pathPT, pathEN, pathES, bulletin_dict):
    doc = pymupdf.open(pathPT)     
    page = doc.load_page(3)
    textPT = page.get_text()
    textPT = re.sub(r'\n+', ' ', textPT) # type: ignore
    textPT = re.sub(r'\s+', ' ', textPT)
    textPT = textPT.split("Condições atuais ")[1]
    # textPT = textPT.split("CODAM Página 1 ")[1]
    textPT = textPT.split("1 Abacaxis ")[0].rstrip()
    # EN
    doc = pymupdf.open(pathEN)     
    page = doc.load_page(3)
    textEN = page.get_text()
    textEN = re.sub(r'\n+', ' ', textEN) # type: ignore
    textEN = re.sub(r'\s+', ' ', textEN)
    textEN = textEN.split("Current conditions ")[1]
    textEN = textEN.split("1 Abacaxis ")[0].rstrip()
    # ES
    doc = pymupdf.open(pathES)     
    page = doc.load_page(3)
    textES = page.get_text()
    textES = re.sub(r'\n+', ' ', textES) # type: ignore
    textES = re.sub(r'\s+', ' ', textES)
    textES = textES.split("Condiciones actuales ")[1]
    textES = textES.split("1 Abacaxis ")[0].rstrip()
    
    current_conditions = {
        "pt": textPT,
        "en": textEN,
        "es": textES
    }
    
    bulletin_dict['current_conditions'] = current_conditions
    return bulletin_dict 