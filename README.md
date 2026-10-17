# TI-Metrics: Análisis de registros

**Asignatura:** Programación II  
**Estudiante:** Jennyfer Yanza  
**Carrera:** Ingeniería en Tecnologías de la Información

## 1. Descripción

TI-Metrics es un proyecto desarrollado en Python que permite leer archivos CSV y JSON, validar los registros, eliminar duplicados y calcular métricas de errores HTTP 500. También consulta información geográfica aproximada de las direcciones IP mediante una API.

## 2. Objetivos

- Leer archivos CSV y JSON.
- Validar los datos y eliminar duplicados.
- Utilizar diccionarios, tuplas y conjuntos.
- Calcular los errores HTTP 500 y su porcentaje.
- Identificar las IP con más errores.
- Consultar información geográfica.
- Generar un reporte JSON.

## 3. Badges del proyecto

| Badge | Estado | Hito |
|:---|:---|:---|
| Data Wrangler | Completado, sujeto a validación final | Hito 1: datos y API |
| OOP Architect | Pendiente | Hito 2: programación orientada a objetos |
| PyTest Guardian | Pendiente | Hito 3: pruebas automatizadas |
| AI Auditor | En progreso | Bitácora de IA y pruebas |
| Git Flow Master | Pendiente | Control de versiones |

## 4. Tecnologías utilizadas

- Python 3
- CSV y JSON
- `requests`
- `collections.Counter`
- IP-API
- Git y GitHub

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

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

Ejecutar el programa desde la carpeta principal:

```bash
python -m src.main
```

## 7. Resultados de prueba

| Indicador | Resultado |
|:---|---:|
| Registros CSV | 8 |
| Registros JSON | 4 |
| Registros inválidos | 0 |
| Registros duplicados | 1 |
| Eventos únicos | 11 |
| Errores HTTP 500 | 5 |
| Porcentaje de errores | 45,45 % |

Estos resultados corresponden a los datos utilizados en las pruebas y pueden cambiar si se modifican los archivos.

## 8. API utilizada

Se utiliza [IP-API](http://ip-api.com/) para obtener información geográfica aproximada de las IP. Los resultados dependen de la disponibilidad del servicio.

## 9. Estado del proyecto

El primer hito incluye la lectura y validación de datos, la eliminación de duplicados, el cálculo de métricas, la consulta de la API y la generación del reporte JSON.
