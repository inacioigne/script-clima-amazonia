from typing import Dict
import re


def extract_fields(text: str) -> Dict[str, str | None]:

    climatologia = re.search(r"entre\s+(\d+\s+e\s+\d+\s+mm)", text).group(1) # type: ignore
    min = climatologia.split()[0]
    max = climatologia.split()[2]
    observados = re.search(r"foram\s+observados\s+(\d+\s+mm)", text)
    anomalia = re.search(r"valor\s+de\s+([-\d\.]+)", text)
    classification = re.search(r"classifica\s+a\s+bacia\s+em\s+condição\s+de\s+([^\.]+)", text)
    prognostico = re.search(r"sugere\s+um\s+comportamento\s+([^\.]+)", text)
    trend = text.split("comportamento climático indica ")
    trend = trend[1].split(" ",1)[0]


    return {
        "min": min,
        "max": max,
        "observados": observados.group(1) if observados else None,
        "anomalia": anomalia.group(1) if anomalia else None,
        "classification": classification.group(1).strip() if classification else None,
        "prognostico": prognostico.group(1).strip() if prognostico else None,
        "trend": trend
    }