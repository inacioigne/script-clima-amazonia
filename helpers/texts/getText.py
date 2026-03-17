import pymupdf

def get_text(pathPT, yyyy, mmdd):
    bulletin_dict = {}
    doc = pymupdf.open(pathPT)
    bulletin_dict = get_meta(doc, bulletin_dict)
    # bulletin_dict = get_meta_2025(doc, bulletin_dict)    
    bulletin_dict = get_current_conditions(pathPT, pathEN, pathES, bulletin_dict)
    bulletin_dict = get_analysis(doc, bulletin_dict)
    bulletin_dict = get_multimodel(pathPT, pathEN, pathES, bulletin_dict)
    with open(f'/home/inacio/script-clima-amazonia/data/{yyyy}/{mmdd}.json', 'w') as f:
        json.dump(bulletin_dict, f, ensure_ascii=False, indent=3)
    return bulletin_dict   