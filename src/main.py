from src.parsers.csv_parser import leer_csv
from src.parsers.json_parser import leer_json
from src.services.geo_service import consultar_ips
from src.services.report_service import guardar_reporte

def normalizar_evento(evento):
    try:
        campos = ["timestamp", "ip", "status_code", "cpu", "memory"]

        if not isinstance(evento, dict):
            return None

        if any(campo not in evento for campo in campos):
            return None

        timestamp = str(evento["timestamp"]).strip()
        ip = str(evento["ip"]).strip()

        if not timestamp or not ip:
            return None

        status_code = int(evento["status_code"])
        cpu = float(evento["cpu"])
        memory = float(evento["memory"])

        if not 100 <= status_code <= 599:
            return None

        if not 0 <= cpu <= 100 or not 0 <= memory <= 100:
            return None

        return {
            "timestamp": timestamp,
            "ip": ip,
            "status_code": status_code,
            "cpu": cpu,
            "memory": memory
        }

    except (ValueError, TypeError, OverflowError):
        return None

def filtrar_y_deduplicar(eventos):
    """Descarta eventos inválidos y elimina duplicados."""
    eventos_unicos = []
    vistos = set()
    invalidos = 0
    duplicados = 0

    for evento in eventos:
        normalizado = normalizar_evento(evento)

        if normalizado is None:
            invalidos += 1
            continue

        clave = (
            normalizado["timestamp"],
            normalizado["ip"],
            normalizado["status_code"],
            normalizado["cpu"],
            normalizado["memory"]
        )

        if clave in vistos:
            duplicados += 1
            continue

        vistos.add(clave)
        eventos_unicos.append(normalizado)

    return eventos_unicos, invalidos, duplicados

def main():
    print("========== TI-METRICS ==========")

    eventos_csv = leer_csv()
    eventos_json = leer_json()

    print(f"Registros leídos del CSV: {len(eventos_csv)}")
    print(f"Registros leídos del JSON: {len(eventos_json)}")

    todos_eventos = eventos_csv + eventos_json

    eventos, invalidos, duplicados = filtrar_y_deduplicar(
        todos_eventos
    )

    print(f"Registros inválidos: {invalidos}")
    print(f"Registros duplicados: {duplicados}")
    print(f"Eventos válidos y únicos: {len(eventos)}")

    errores_500 = sum(
        1 for evento in eventos
        if evento["status_code"] == 500
    )

    porcentaje = (
        round(errores_500 / len(eventos) * 100, 2)
        if eventos else 0.0
    )

    print(f"Errores HTTP 500: {errores_500}")
    print(f"Porcentaje de errores 500: {porcentaje:.2f}%")

    from collections import Counter

    conteo_ips = Counter(
        evento["ip"] for evento in eventos
        if evento["status_code"] == 500
    )

    ips_criticas = [
        {"ip": ip, "errores_500": cantidad}
        for ip, cantidad in conteo_ips.most_common()
    ]

    print(f"IPs críticas: {ips_criticas}")

    print("\nConsultando API geográfica...")
    ips = [evento["ip"] for evento in eventos]
    datos_geograficos = consultar_ips(ips)

    for dato in datos_geograficos:
        print(f'{dato["ip"]}: {dato["estado"]}')

    ruta = guardar_reporte(
        registros_csv=len(eventos_csv),
        registros_json=len(eventos_json),
        invalidos=invalidos,
        duplicados=duplicados,
        eventos=eventos,
        datos_geograficos=datos_geograficos
    )

    print(f"\nReporte guardado en: {ruta}")

if __name__ == "__main__":
    main()