import pymupdf
import json

from lib.texts.getMeta import get_meta2024
from lib.texts.getCurrentConditions import get_current_conditions
from lib.texts.getAnalysis import get_analysis
from lib.texts.getMultimodel import get_multimodel

def get_text(pathPT, pathEN, pathES, yyyy, mmdd):
    bulletin_dict = {}
    doc = pymupdf.open(pathPT)
    bulletin_dict = get_meta2024(doc, bulletin_dict)
    bulletin_dict = get_current_conditions(pathPT, pathEN, pathES, bulletin_dict)
    bulletin_dict = get_analysis(doc, bulletin_dict)
    bulletin_dict = get_multimodel(pathPT, pathEN, pathES, bulletin_dict)
    with open(f'/home/inacio/script-clima-amazonia/data/{yyyy}/{mmdd}.json', 'w') as f:
        json.dump(bulletin_dict, f, ensure_ascii=False, indent=3)
    return bulletin_dict   