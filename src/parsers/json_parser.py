import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"

def leer_json(ruta=None):
    if ruta is None:
        ruta = DATA_DIR / "events.json"

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            print("Error: el JSON debe contener una lista.")
            return []

        return datos

    except (OSError, json.JSONDecodeError) as error:
        print(f"Error al leer el JSON: {error}")
        return []