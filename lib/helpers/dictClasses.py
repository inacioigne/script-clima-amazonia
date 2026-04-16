def dict_classes(slugname, lang):
    d = {
        'seco': {
            "en": "dry condition",
            "es": "seco"
        },
        'tendencia-a-muito-chuvoso': {
            "en": "tendency to very rainy condition",
            "es": "tendiendo a muy lluvioso"
        },
        'tendencia-a-chuvoso': {
            "en": "tendency to rainy condition",
            "es": "tendiendo a lluvioso"
        },
        'normalidade': {
            "en": "normal contition",
            "es": "normalidad"
        },
        'tendencia-a-extremamente-seco': {
            "en": "tendency to extremely dry condition",
            "es": "tendiendo a extremadamente seco"
        },
        'tendencia-a-muito-seco': {
            "en": "tendency to very dry contition",
            "es": "tendiendo a muy seco"
        },
         'tendencia-a-seco': {
            "en": "tendency to dry contition",
            "es": "tendiendo a seco"
        },
         'muito-seco': {
            "en": "very dry condition",
            "es": "muy seco"
        },
         'chuvoso': {
            "en": "rainy",
            "es": "lluvioso"
        },
         'muito-chuvoso': {
            "en": "ver rainy",
            "es": "muy lluvioso"
        },
         'extremamente-chuvoso': {
            "en": "extremely rainy",
            "es": "extremadamente lluvioso"
        },
         'tendencia-a-extremamente-chuvoso': {
            "en": "tending to be extremely rainy",
            "es": "tendencia a ser extremadamente lluvioso"
        },
         'extremamente-seco-ou-tendencia-a-extremamente-seco': {
            "en": "extremely dry behavior or a tending to be extremely dry",
            "es": "extremadamente seco o con tendencia a ser extremadamente seco"
        },
         'extremamente-seco': {
            "en": "extremely dry",
            "es": "extremadamente seco"
        }
    }
    return d[slugname][lang]