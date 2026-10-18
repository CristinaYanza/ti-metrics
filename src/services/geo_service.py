import requests
import time

def consultar_ip(ip):
    """Consulta la información geográfica aproximada de una IP."""
    url = f"http://ip-api.com/json/{ip}"

    parametros = {
        "fields": "status,message,query,country,regionName,city,lat,lon"
    }

    try:
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=10
        )
        respuesta.raise_for_status()
        datos = respuesta.json()

        if datos.get("status") != "success":
            return {
                "ip": ip,
                "estado": "error",
                "mensaje": datos.get("message", "Consulta fallida")
            }

        return {
            "ip": datos.get("query", ip),
            "pais": datos.get("country"),
            "region": datos.get("regionName"),
            "ciudad": datos.get("city"),
            "latitud": datos.get("lat"),
            "longitud": datos.get("lon"),
            "estado": "success"
        }

    except (requests.RequestException, ValueError) as error:
        return {
            "ip": ip,
            "estado": "error",
            "mensaje": str(error)
        }

def consultar_ips(ips):
    """Consulta cada IP una sola vez."""
    resultados = []

    for indice, ip in enumerate(sorted(set(ips))):
        resultados.append(consultar_ip(ip))

        # Pausa entre consultas para no saturar el servicio.
        if indice < len(set(ips)) - 1:
            time.sleep(1.5)

    return resultados