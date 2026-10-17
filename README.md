
# TI-Metrics: Análisis de Registros

**Asignatura:** Programación II  
**Estudiante:** Jennyfer Yanza  
**Carrera:** Ingeniería en Tecnologías de la Información

## 1. Descripción

TI-Metrics es un proyecto desarrollado en Python que permite leer archivos CSV y JSON, validar registros, identificar duplicados y calcular métricas relacionadas con errores HTTP 500. También consulta información geográfica aproximada de las direcciones IP mediante una API y genera un reporte en formato JSON.

## 2. Objetivos

- Leer archivos CSV y JSON.
- Validar los datos e identificar registros duplicados.
- Utilizar diccionarios, tuplas y conjuntos para procesar información.
- Calcular los errores HTTP 500 y su porcentaje.
- Identificar las IP con más errores.
- Consultar información geográfica aproximada mediante una API.
- Generar un reporte JSON con los resultados.

## 3. Badges del proyecto

| Badge | Estado | Hito asociado |
|---|---|---|
| Data Wrangler | En desarrollo | Hito 1: Persistencia y APIs |
| OOP Architect | Pendiente | Hito 2: Arquitectura POO |
| PyTest Guardian | Pendiente | Hito 3: Pruebas automatizadas |
| AI Auditor | En progreso | Bitácora de IA y pruebas |
| Git Flow Master | En progreso | Control de versiones y commits |

## 4. Tecnologías utilizadas

- Python 3
- CSV y JSON
- `requests`
- `collections.Counter`
- IP-API
- Git y GitHub
- Pytest, para las pruebas automatizadas cuando estén implementadas

## 5. Estructura del proyecto

```text
ti-metrics/
├── data/
│   ├── logs.csv
│   └── events.json
├── src/
│   ├── main.py
│   ├── parsers/
│   │   ├── csv_parser.py
│   │   └── json_parser.py
│   └── services/
│       ├── geo_service.py
│       └── report_service.py
├── reports/
│   └── summary.json
├── PROMPTS.md
├── README.md
├── requirements.txt
└── .gitignore
```

## 6. Ejecución

Instalar las dependencias desde la carpeta principal del proyecto:

```bash
python -m pip install -r requirements.txt
```

Ejecutar el programa:

```bash
python -m src.main
```

## 7. Resultados de ejecución

Los indicadores se obtienen de los archivos de entrada procesados por el programa. Los valores pueden cambiar cuando se modifican los datos.

Para consultar los resultados actualizados, ejecutar el programa y revisar el archivo `reports/summary.json`.

## 8. API utilizada

Se utiliza [IP-API](http://ip-api.com/) para consultar información geográfica aproximada de las direcciones IP. La disponibilidad y los resultados dependen del servicio externo.

## 9. Estado del proyecto

El primer hito contempla la lectura y validación de datos, la identificación de duplicados, el cálculo de métricas, la consulta de la API y la generación del reporte JSON. Los siguientes hitos incorporarán las funcionalidades y pruebas que establezca el proyecto integrador.

