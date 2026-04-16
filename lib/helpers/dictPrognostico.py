def dict_prognostico(prognostico, lang):
    d = {
        "muito-seco-ou-tendencia-a-extremamente-seco": {
            "en": "very dry behavior or a tending to be extremely dry",
            "es": "muy seco o con tendencia a ser extremadamente seco"
        },
        "muito-seco-ou-tendencia-a-muito-seco": {
            "en": "very dry behavior or a tending to be very dry",
            "es": "muy seco o con tendencia a ser muy seco"
        },
        "seco-ou-tendencia-a-muito-seco": {
            "en": "dry behavior or a tending to be very dry",
            "es": "seco o con tendencia a ser muy seco"
        },
        "tendencia-a-muito-seco-ou-muito-seco": {
            "en": "very dry behavior or a tending to be very dry",
            "es": "muy seco o con tendencia a ser muy seco"
        },
        "tendencia-a-seco-ou-seco": {
            "en": "dry behavior or a tending to be dry",
            "es": "seco o con tendencia a ser seco"
        },
        "tendencia-a-muito-seco-ou-seco": {
            "en": "very dry behavior or a tending to be dry",
            "es": "muy seco o con tendencia a ser seco"
        },
        "tendencia-a-seco-ou-proximo-da-normalidade": {
            "en": "dry behavior or behavior close",
            "es": "seco o con cerca de la normalidad"
        },
        "tendencia-a-chuvoso-ou-proximo-a-normalidade": {
            "en": "behavior close to normality or a tending to be rainy",
            "es": "cerca de la normalidad o con tendencia a lluvioso"
        },
        "chuvoso-ou-tendencia-a-chuvoso": {
            "en": "rainy behavior or a tending to be rainy",
            "es": "lluvioso o propenso a lluvioso."
        },
        "tendencia-a-muito-chuvoso-ou-chuvoso": {
            "en": "tending rainy behavior or a tending to be very rainy",
            "es": "lluvioso o propenso a muy lluvioso."
        },
        "tendencia-a-chuvoso-ou-proximo-da-normalidade": {
            "en": "tending rainy behavior or close to normality",
            "es": "propenso a lluvioso o cerca de la normalidad"
        },
        "proximo-a-normalidade-ou-tendencia-a-chuvoso": {
            "en": "tending rainy behavior or close to normality",
            "es": "propenso a lluvioso o cerca de la normalidad"
        },
        "chuvoso": {
            "en": "rainy behavior",
            "es": "lluvioso."
        },
        "proximo-da-normalidade-ou-tendencia-a-chuvoso": {
            "en": "behavior close to normality or a tending to be rainy",
            "es": "cerca de la normalidad o con tendencia a lluvioso"
        },
        "proximo-da-normalidade-ou-tendencia-a-seco": {
            "en": "behavior close to normality or a tending to be dry",
            "es": "cerca de la normalidad o con tendencia a ser seco"
        },
         "proximo-da-normalidade": {
            "en": "behavior close to normality",
            "es": "cerca de la normalidad"
        },
         "seco-ou-tendencia-a-seco": {
            "en": "dry behavior or a tending to be dry",
            "es": "seco o con tendencia a ser seco"
        },
         'tendencia-a-chuvoso-ou-chuvoso': {
            "en": "rainy behavior or a tending to be rainy",
            "es": "lluvioso o con tendencia a ser lluvioso"
        },
         'chuvoso-ou-tendencia-a-muito-chuvoso': {
            "en": "rainy behavior or a tending to be very rainy",
            "es": "lluvioso o con tendencia a ser muy lluvioso"
        },
         'muito-chuvoso-ou-tendencia-a-muito-chuvoso': {
            "en": "very rainy behavior or a tending to be very rainy",
            "es": "muy lluvioso o con tendencia a muy lluvioso"
        },
         'muito-chuvoso-ou-tendencia-a-extremamente-chuvoso': {
            "en": "very rainy behavior or a tending to be extremely rainy",
            "es": "muy seco o con tendencia a ser extremadamente seco"
        },
         'extremamente-chuvoso-ou-tendencia-a-extremamente-chuvoso': {
            "en": "extremely rainy behavior or a tending to be extremely rainy",
            "es": "extremadamente lluvioso o con tendencia a extremadamente lluvioso"
        },
         'extremamente-seco-ou-tendencia-a-extremamente-seco': {
            "en": "extremely dry behavior or a tending to be extremely dry",
            "es": "extremadamente seco o con tendencia a ser extremadamente seco"
        },
         'extremamante-seco-ou-tendencia-a-extremamente-seco': {
            "en": "extremely dry behavior or a tending to be extremely dry",
            "es": "extremadamente seco o con tendencia a ser extremadamente seco"
        },
         "muito-seco-ou-tendencia-a-seco": {
            "en": "very dry behavior or a tending to be dry",
            "es": "muy seco o con tendencia a ser seco"
        },
         'tendencia-a-muito-chuvoso-ou-muito-chuvoso': {
            "en": "very rainy behavior or a tending to be very rainy",
            "es": "muy lluvioso o con tendencia a ser muy lluvioso"
        },  
         'muito-chuvoso-ou-chuvoso': {
            "en": "very rainy behavior or behavior rainy",
            "es": "muy lluvioso o lluvioso"
        },
         'chuvoso-ou-tendencia-chuvoso': {
            "en": "rainy behavior or tending to be rainy",
            "es": "muy lluvioso o con tendencia a ser lluvioso"
        },
         'tendencia-chuvoso-ou-proximo-da-normalidade': {
            "en": "rainy behavior or tending to be rainy",
            "es": "muy lluvioso o con tendencia a ser lluvioso"
        }
         
              
         
    }
    return d[prognostico][lang]  