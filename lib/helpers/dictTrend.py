def dict_trend(trend, lang):
    d = {
        "elevacao": {
            "en": "increase",
            "es": "elevación"
        },
        "manutencao": {
            "en": "increase",
            "es": "maintenance"
        },
        "reducao": {
            "en": "decrease",
            "es": "reducción"
        }
    }
    return d[trend][lang]