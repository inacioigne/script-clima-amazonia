import json
import sys
from pathlib import Path

import pymupdf

from lib.images.analysis import img_analysis
from lib.images.anomaly import img_anomaly
from lib.images.categorization import img_categorization
from lib.images.current_conditions import img_current_conditions
from lib.images.multimodel import img_multimodel
from lib.images.reference import img_reference
from lib.texts.getAnalysis import get_analysis
from lib.texts.getCurrentConditions import get_current_conditions
from lib.texts.getMeta import get_meta
from lib.texts.getMultimodel import get_multimodel

def insert_images(mmdd):
    images = {
      "current_conditions": {
         "table_current_conditions": f"https://climamazonia.shop/2026/{mmdd}/current_conditions/table_current_conditions.webp",
         "map_current_conditions": f"https://climamazonia.shop/2026/{mmdd}/current_conditions/map_current_conditions.webp"
      },
      "analysis": {
         "bacia-do-rio-abacaxis-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-abacaxis-acc.webp",
         "bacia-do-rio-juruena-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-juruena-ano.webp",
         "bacia-do-rio-jutai-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-jutai-ano.webp",
         "bacia-do-rio-xingu-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-xingu-ano.webp",
         "bacia-do-rio-javari-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-javari-acc.webp",
         "curso-principal-do-rio-solimoes-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/curso-principal-do-rio-solimoes-ano.webp",
         "bacia-do-rio-coari-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-coari-ano.webp",
         "bacia-do-rio-ica-putumayo-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-ica-putumayo-acc.webp",
         "bacia-dos-rios-beni-e-madre-de-dios-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-dos-rios-beni-e-madre-de-dios-acc.webp",
         "curso-principal-do-rio-amazonas-brasil-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/curso-principal-do-rio-amazonas-brasil-acc.webp",
         "bacia-do-rio-iriri-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-iriri-ano.webp",
         "bacia-do-rio-abacaxis-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-abacaxis-ano.webp",
         "bacia-do-rio-negro-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-negro-ano.webp",
         "bacia-do-rio-juruena-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-juruena-acc.webp",
         "bacia-do-rio-curua-una-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-curua-una-ano.webp",
         "bacia-do-rio-tefe-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-tefe-ano.webp",
         "curso-principal-do-rio-solimoes-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/curso-principal-do-rio-solimoes-acc.webp",
         "bacia-do-rio-aripuana-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-aripuana-acc.webp",
         "bacia-do-rio-japura-caqueta-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-japura-caqueta-acc.webp",
         "bacia-do-rio-xingu-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-xingu-acc.webp",
         "bacia-do-rio-ucayali-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-ucayali-acc.webp",
         "bacia-do-rio-javari-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-javari-ano.webp",
         "bacia-do-rio-napo-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-napo-ano.webp",
         "bacias-da-margem-esquerda-do-rio-amazonas-nordeste-do-pa-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacias-da-margem-esquerda-do-rio-amazonas-nordeste-do-pa-ano.webp",
         "bacia-do-rio-mamore-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-mamore-acc.webp",
         "bacia-do-rio-branco-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-branco-ano.webp",
         "bacia-do-rio-napo-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-napo-acc.webp",
         "bacias-da-margem-esquerda-do-rio-amazonas-amazonas-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacias-da-margem-esquerda-do-rio-amazonas-amazonas-acc.webp",
         "bacia-do-rio-mamore-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-mamore-ano.webp",
         "bacia-do-rio-madeira-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-madeira-acc.webp",
         "bacia-do-rio-branco-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-branco-acc.webp",
         "bacia-do-rio-teles-pires-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-teles-pires-ano.webp",
         "bacia-do-rio-ucayali-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-ucayali-ano.webp",
         "bacia-do-rio-teles-pires-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-teles-pires-acc.webp",
         "bacia-do-rio-jurua-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-jurua-acc.webp",
         "bacia-do-rio-jutai-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-jutai-acc.webp",
         "bacia-do-rio-iriri-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-iriri-acc.webp",
         "bacia-do-rio-purus-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-purus-ano.webp",
         "bacia-do-rio-coari-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-coari-acc.webp",
         "bacia-do-rio-maranon-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-maranon-ano.webp",
         "bacia-do-rio-purus-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-purus-acc.webp",
         "curso-principal-do-rio-amazonas-peru-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/curso-principal-do-rio-amazonas-peru-ano.webp",
         "bacia-do-rio-curua-una-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-curua-una-acc.webp",
         "bacia-do-rio-madeira-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-madeira-ano.webp",
         "bacia-do-rio-maranon-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-maranon-acc.webp",
         "bacia-do-rio-guapore-itenez-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-guapore-itenez-ano.webp",
         "bacia-do-rio-tapajos-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-tapajos-acc.webp",
         "curso-principal-do-rio-amazonas-brasil-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/curso-principal-do-rio-amazonas-brasil-ano.webp",
         "bacias-da-margem-esquerda-do-rio-amazonas-noroeste-do-para-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacias-da-margem-esquerda-do-rio-amazonas-noroeste-do-para-ano.webp",
         "curso-principal-do-rio-amazonas-peru-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/curso-principal-do-rio-amazonas-peru-acc.webp",
         "bacias-da-margem-esquerda-do-rio-amazonas-noroeste-do-para-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacias-da-margem-esquerda-do-rio-amazonas-noroeste-do-para-acc.webp",
         "bacia-do-rio-negro-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-negro-acc.webp",
         "bacia-do-rio-tefe-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-tefe-acc.webp",
         "bacias-da-margem-esquerda-do-rio-amazonas-nordeste-do-pa-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacias-da-margem-esquerda-do-rio-amazonas-nordeste-do-pa-acc.webp",
         "bacia-do-rio-tapajos-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-tapajos-ano.webp",
         "bacia-do-rio-guapore-itenez-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-guapore-itenez-acc.webp",
         "bacia-do-rio-ji-parana-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-ji-parana-ano.webp",
         "bacia-do-rio-aripuana-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-aripuana-ano.webp",
         "bacia-dos-rios-beni-e-madre-de-dios-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-dos-rios-beni-e-madre-de-dios-ano.webp",
         "bacia-do-rio-ji-parana-acc": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-ji-parana-acc.webp",
         "bacia-do-rio-japura-caqueta-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-japura-caqueta-ano.webp",
         "bacia-do-rio-ica-putumayo-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-ica(continued)-putumayo-ano.webp",
         "bacia-do-rio-jurua-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacia-do-rio-jurua-ano.webp",
         "bacias-da-margem-esquerda-do-rio-amazonas-amazonas-ano": f"https://climamazonia.shop/2026/{mmdd}/analysis/bacias-da-margem-esquerda-do-rio-amazonas-amazonas-ano.webp"
      },
      "anomaly": {
         "bacia_1": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_1.webp",
         "bacia_24": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_24.webp",
         "bacia_2": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_2.webp",
         "bacia_29": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_29.webp",
         "bacia_16": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_16.webp",
         "bacia_23": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_23.webp",
         "bacia_27": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_27.webp",
         "bacia_9": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_9.webp",
         "bacia_3": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_3.webp",
         "bacia_19": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_19.webp",
         "bacia_20": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_20.webp",
         "bacia_30": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_30.webp",
         "bacia_6": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_6.webp",
         "bacia_25": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_25.webp",
         "bacia_7": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_7.webp",
         "bacia_13": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_13.webp",
         "bacia_28": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_28.webp",
         "bacia_17": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_17.webp",
         "bacia_11": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_11.webp",
         "bacia_21": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_21.webp",
         "bacia_12": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_12.webp",
         "bacia_32": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_32.webp",
         "bacia_22": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_22.webp",
         "bacia_10": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_10.webp",
         "bacia_8": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_8.webp",
         "bacia_15": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_15.webp",
         "bacia_4": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_4.webp",
         "bacia_18": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_18.webp",
         "bacia_31": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_31.webp",
         "bacia_14": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_14.webp",
         "bacia_26": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_26.webp",
         "bacia_5": f"https://climamazonia.shop/2026/{mmdd}/anomaly/bacia_5.webp"
      },
      "reference": {
         "reference_table": f"https://climamazonia.shop/2026/{mmdd}/reference/reference_table.webp"
      },
      "multimodel": {
         "fourteen_days": f"https://climamazonia.shop/2026/{mmdd}/multimodel/fourteen_days.webp",
         "seven_days": f"https://climamazonia.shop/2026/{mmdd}/multimodel/seven_days.webp"
      },
      "categorization": {
         "table": f"https://climamazonia.shop/2026/{mmdd}/categorization/table.webp"
      }
   }
    return images


def get_text(pathPT, pathEN, pathES, mmdd):
    
    print('Processing bulletin for date:', mmdd)
    output_path = Path(f"data/output/{mmdd}")
    output_path.mkdir(parents=True, exist_ok=True)
    bulletin_dict = {}
    doc = pymupdf.open(pathPT)
    bulletin_dict = get_meta(doc, bulletin_dict) 
    bulletin_dict = get_current_conditions(pathPT, pathEN, pathES, bulletin_dict)
    bulletin_dict = get_analysis(doc, bulletin_dict)
    bulletin_dict = get_multimodel(pathPT, pathEN, pathES, bulletin_dict)
    images = insert_images(mmdd)
    bulletin_dict["images"] = images
    bulletin_dict["pdf"] = {
        "pt": "",
        "en": "",
        "es": ""
    }
    
    with open(f'{output_path}/{mmdd}.json', 'w') as f:
        json.dump(bulletin_dict, f, ensure_ascii=False, indent=3)
        
    return bulletin_dict  

def get_images(pathPT, mmdd):
    
    print('Extracting images from bulletin...')
    output_path = Path(f"data/output/{mmdd}/{mmdd}")
    output_path.mkdir(parents=True, exist_ok=True)
    
    doc = pymupdf.open(pathPT)
    img_current_conditions(doc, output_path)
    img_analysis(doc, output_path)
    img_multimodel(doc, output_path)
    img_reference(doc, output_path)
    img_categorization(doc, output_path)
    img_anomaly(doc, output_path)

def main():
    mmdd = sys.argv[1] 
    pathPT = Path(f'data/input/BHA_PT_2026{mmdd}.pdf')
    pathEN = Path(f'data/input/BHA_EN_2026{mmdd}.pdf')
    pathES = Path(f'data/input/BHA_ES_2026{mmdd}.pdf')
    get_text(pathPT, pathEN, pathES, mmdd) 
    get_images(pathPT, mmdd)

if __name__ == "__main__":
    main()