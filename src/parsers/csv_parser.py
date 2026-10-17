import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"

def leer_csv(ruta=None):
    if ruta is None:
        ruta = DATA_DIR / "logs.csv"

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)

    except (OSError, csv.Error) as error:
        print(f"Error al leer el CSV: {error}")
        return []