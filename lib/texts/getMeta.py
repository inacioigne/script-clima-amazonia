import re

def date_to_en(date):
    meses = {
        "janeiro": "January",
        "fevereiro": "February",
        "março": "March",
        "marco": "March",
        "abril": "April",
        "maio": "May",
        "junho": "June",
        "julho": "July",
        "agosto": "August",
        "setembro": "September",
        "outubro": "October",
        "novembro": "November",
        "dezembro": "December"
    }
    mes = date.split()[2]
    dia = date.split()[0]
    ano = date.split()[-1]
    mes_en = meses[mes]
    date_en = f'{mes_en} {dia}, {ano}'
    return date_en

def date_to_es(date):
    meses = {
        "janeiro": "enero",
        "fevereiro": "febrero",
        "março": "marzo",
        "marco": "marzo",
        "abril": "abril",
        "maio": "mayo",
        "junho": "junio",
        "julho": "julio",
        "agosto": "agosto",
        "setembro": "septiembre",
        "outubro": "octubre",
        "novembro": "noviembre",
        "dezembro": "diciembre"
    }
    mes = date.split()[2]
    dia = date.split()[0]
    ano = date.split()[-1]
    mes_es = meses[mes]
    date_es = f'{dia} de {mes_es} de {ano}'
    return date_es

def get_meta2024(doc, bulletin_dict):
    # Page 1
    page = doc.load_page(0)
    text = page.get_text()
    padrao_numero = r"Número\s+(\d+)"
    padrao_data = r"(\d{1,2}\s+de\s+[A-Za-zçãõáéíóúâêô]+\s+de\s+\d{4})"
    match_numero = re.search(padrao_numero, text, re.IGNORECASE)
    match_data = re.search(padrao_data, text, re.IGNORECASE)
    number = match_numero.group(1) # type: ignore
    date = match_data.group(1) # type: ignore

    meta = {
        "meta": {
        "pt": {
            "doi": f'10.61818/029104{number}',
            "issn": "2965-0291",
            "volume": "04",
            "date": date
        },
        "en": {
            "doi": f'10.61818/785702{number}',
            "issn": "2965-7857",
            "volume": "02",
            "date": date_to_en(date)
        },
        "es": {
            "doi": f'10.61818/770902{number}',
            "issn": "2965-7709",
            "volume": "02",
            "date": date_to_es(date)
        },
         "number": number
    }
        }
    bulletin_dict.update(meta)
    return bulletin_dict