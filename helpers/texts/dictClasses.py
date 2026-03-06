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
            "en": "tendency to very dry contition",
            "es": "tendency to dry condition"
        },
         'muito-seco': {
            "en": "very dry condition",
            "es": "muy seco"
        },
    }
    return d[slugname][lang]