import json
from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).resolve().parents[2]
REPORTS_DIR = BASE_DIR / "reports"

def calcular_metricas(eventos):
    """Calcula los errores HTTP 500 y las IP críticas."""
    total_eventos = len(eventos)

    errores_500 = [
        evento for evento in eventos
        if evento["status_code"] == 500
    ]

    cantidad_errores = len(errores_500)

    if total_eventos > 0:
        porcentaje = round(
            cantidad_errores / total_eventos * 100, 2
        )
    else:
        porcentaje = 0.0

    conteo_ips = Counter(
        evento["ip"] for evento in errores_500
    )

    ips_criticas = [
        {"ip": ip, "errores_500": cantidad}
        for ip, cantidad in conteo_ips.most_common()
    ]

    return {
        "total_errores_500": cantidad_errores,
        "porcentaje_errores_500": porcentaje,
        "ips_criticas": ips_criticas
    }

def guardar_reporte(
    registros_csv,
    registros_json,
    invalidos,
    duplicados,
    eventos,
    datos_geograficos
):
    """Genera y guarda el resumen final en formato JSON."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    reporte = {
        "proyecto": "TI-Metrics",
        "resumen": {
            "registros_csv": registros_csv,
            "registros_json": registros_json,
            "registros_invalidos": invalidos,
            "registros_duplicados": duplicados,
            "eventos_unicos": len(eventos)
        },
        "metricas": calcular_metricas(eventos),
        "datos_geograficos": datos_geograficos
    }

    ruta_reporte = REPORTS_DIR / "summary.json"

    with open(ruta_reporte, "w", encoding="utf-8") as archivo:
        json.dump(
            reporte,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    return ruta_reporte