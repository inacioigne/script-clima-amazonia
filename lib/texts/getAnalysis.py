import re
from lib.helpers.dictClasses import dict_classes
from lib.helpers.dictPrognostico import dict_prognostico
from lib.helpers.dictTrend import dict_trend
from lib.helpers.extractFields import extract_fields
from lib.helpers.slugify import slugify

def get_analysis(doc, bulletin_dict):
    bacias = ['Bacia do Rio Branco', 'Bacia do Rio Negro','Bacia do Rio Marañon', 'Bacia do Rio Ucayali', 'Bacia do Rio Napo', 
'Curso principal do Rio Amazonas (Peru)','Bacia do Rio Javari','Bacia do Rio Içá (Putumayo)','Bacia do Rio Jutaí','Bacia do Rio Juruá',
'Bacia do Rio Japurá (Caquetá)','Bacia do Rio Tefé','Bacia do Rio Coari','Bacia do Rio Purus','Curso principal do Rio Solimões',
'Bacia dos rios Beni e Madre de Dios','Bacia do Rio Mamoré','Bacia do Rio Guaporé (Iténez)','Bacia do Rio Ji-Paraná','Bacia do Rio Aripuanã',
'Bacia do Rio Madeira','Bacias da margem esquerda do Rio Amazonas (Amazonas)','Bacia do Rio Abacaxis','Bacia do Rio Juruena','Bacia do Rio Teles Pires',
'Bacia do Rio Tapajós','Bacias da margem esquerda do Rio Amazonas (noroeste do Pará)','Bacia do Rio Curuá Una','Bacias da margem esquerda do Rio Amazonas (nordeste do PA)',
'Bacia do Rio Iriri','Bacia do Rio Xingu','Curso principal do Rio Amazonas (Brasil)']
    analysis = []
    texts = [doc.load_page(pg).get_text() for pg in range(5,16)]
    text = " ".join(texts)
    text = re.sub(r"\s*\n\s*", " ", text)
    text = re.sub(r"\s{2,}", " ", text).strip()
    for i, nome in enumerate(bacias):
        nome_regex = re.escape(nome)
        start_match = re.search(nome_regex, text)
        start = start_match.end() # type: ignore
        if i < len(bacias) - 1:
            next_nome = re.escape(bacias[i + 1])
            next_match = re.search(next_nome, text)
            end = next_match.start() if next_match else len(text)
        else:
            end = len(text)
        basin_text = text[start:end].strip()
        fields = extract_fields(basin_text)
        slug_name = slugify(nome)
        classification = fields["classification"]
        slug_classification = slugify(classification) # type: ignore
        # trend
        trend = fields["trend"]
        slug_trend = slugify(trend) # type: ignore
        # prognostico
        prognostico = fields["prognostico"]
        slug_prognostico = slugify(prognostico) # type: ignore

        
        bacia = {
                "id": slug_name,
                "name": nome,
                "min": fields["min"],
                "max": fields["max"],
                "observados": fields["observados"],
                "anomalia": fields["anomalia"],
                "i18n": {
                    "pt": {
                        "classification": classification,
                        "trend": trend,
                        "prognostico": prognostico
                    },
                    "en": {
                        "classification": dict_classes(slug_classification, "en"),
                        "trend": dict_trend(slug_trend, "en"),
                        "prognostico": dict_prognostico(slug_prognostico, "en")
                    },
                    "es": {
                        "classification": dict_classes(slug_classification, "es"),
                        "trend": dict_trend(slug_trend, "es"),
                        "prognostico": dict_prognostico(slug_prognostico, "es")
                    }
                }
            }
        # print(bacia)
        analysis.append(bacia)
    bulletin_dict['analysis'] = analysis
    
    return bulletin_dict

# def get_analysis(doc, bulletin_dict):
#     bacias = ['Bacia do Rio Branco', 'Bacia do Rio Negro','Bacia do Rio Marañon', 'Bacia do Rio Ucayali', 'Bacia do Rio Napo', 
# 'Curso principal do Rio Amazonas (Peru)','Bacia do Rio Javari','Bacia do Rio Içá (Putumayo)','Bacia do Rio Jutaí','Bacia do Rio Juruá',
# 'Bacia do Rio Japurá (Caquetá)','Bacia do Rio Tefé','Bacia do Rio Coari','Bacia do Rio Purus','Curso principal do Rio Solimões',
# 'Bacia dos rios Beni e Madre de Dios','Bacia do Rio Mamoré','Bacia do Rio Guaporé (Iténez)','Bacia do Rio Ji-Paraná','Bacia do Rio Aripuanã',
# 'Bacia do Rio Madeira','Bacias da margem esquerda do Rio Amazonas (Amazonas)','Bacia do Rio Abacaxis','Bacia do Rio Juruena','Bacia do Rio Teles Pires',
# 'Bacia do Rio Tapajós','Bacias da margem esquerda do Rio Amazonas (noroeste do Pará)','Bacia do Rio Curuá Una','Bacias da margem esquerda do Rio Amazonas (nordeste do PA)',
# 'Bacia do Rio Iriri','Bacia do Rio Xingu','Curso principal do Rio Amazonas (Brasil)']
#     analysis = []
#     texts = [doc.load_page(pg).get_text() for pg in range(4,15)]
#     text = " ".join(texts)
#     text = re.sub(r"\s*\n\s*", " ", text)
#     text = re.sub(r"\s{2,}", " ", text).strip()
#     for i, nome in enumerate(bacias):
#         nome_regex = re.escape(nome)
#         start_match = re.search(nome_regex, text)
#         start = start_match.end() # type: ignore
#         if i < len(bacias) - 1:
#             next_nome = re.escape(bacias[i + 1])
#             next_match = re.search(next_nome, text)
#             end = next_match.start() if next_match else len(text)
#         else:
#             end = len(text)
#         basin_text = text[start:end].strip()
#         if basin_text != "":
#             fields = extract_fields(basin_text)
#             slug_name = slugify(nome)
#             classification = fields["classification"]
#             slug_classification = slugify(classification) # type: ignore
#             # trend
#             # trend = fields["trend"]
#             # slug_trend = slugify(trend) # type: ignore
#             # prognostico
#             prognostico = fields["prognostico"]
#             slug_prognostico: str = slugify(prognostico) # type: ignore

            
#             bacia = {
#                     "id": slug_name,
#                     "name": nome,
#                     "min": fields["min"],
#                     "max": fields["max"],
#                     "observados": fields["observados"],
#                     "anomalia": fields["anomalia"],
#                     "i18n": {
#                         "pt": {
#                             "classification": classification,
#                             # "trend": trend,
#                             "prognostico": prognostico
#                         },
#                         "en": {
#                             "classification": dict_classes(slug_classification, "en"),
#                             # "trend": dict_trend(slug_trend, "en"),
#                             "prognostico": dict_prognostico(slug_prognostico, "en")
#                         },
#                         "es": {
#                             "classification": dict_classes(slug_classification, "es"),
#                             # "trend": dict_trend(slug_trend, "es"),
#                             "prognostico": dict_prognostico(slug_prognostico, "es")
#                         }
#                     }
#                 }
#             # print(bacia)
#             analysis.append(bacia)
#     bulletin_dict['analysis'] = analysis
    
#     return bulletin_dict