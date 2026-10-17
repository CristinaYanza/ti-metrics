# TI-Metrics: Engine de Analítica de Logs

Asignatura: Programación II  
Estudiante: Jennyfer Yanza  
Carrera: Ingeniería en Tecnologías de la Información

## Cuadro de Logros y Badges

| Badge | Estado | Hito Asociado |
| :--- | :---: | :--- |
| Data Wrangler | ![Data Wrangler](https://img.shields.io/badge/Data_Wrangler-En_progreso-orange?style=for-the-badge&logo=python) | Hito 1: Persistencia y APIs |
| OOP Architect | ![OOP Architect](https://img.shields.io/badge/OOP_Architect-Bloqueado-inactive?style=for-the-badge&logo=diagrams.net) | Hito 2: Arquitectura POO |
| PyTest Guardian | ![PyTest Guardian](https://img.shields.io/badge/PyTest_Guardian-Bloqueado-inactive?style=for-the-badge&logo=pytest) | Hito 3: Cobertura superior al 80 % |
| AI Auditor | ![AI Auditor](https://img.shields.io/badge/AI_Auditor-En_progreso-orange?style=for-the-badge&logo=openai) | Hito 3: PROMPTS.md y TDD |
| Git Flow Master | ![Git Flow Master](https://img.shields.io/badge/Git_Flow_Master-En_progreso-orange?style=for-the-badge&logo=github) | Transversal: Commits semánticos |

## 1. Descripción del proyecto

TI-Metrics es un proyecto desarrollado en Python para analizar registros de eventos de infraestructura tecnológica. Permite leer archivos CSV y JSON, validar registros, identificar duplicados y calcular métricas relacionadas con errores HTTP 500.

También consulta información geográfica aproximada de direcciones IP mediante una API y genera un reporte con los resultados.

## 2. Objetivos

- Leer archivos CSV y JSON.
- Validar registros e identificar datos inválidos.
- Detectar registros duplicados.
- Procesar datos mediante estructuras de Python.
- Calcular la cantidad y el porcentaje de errores HTTP 500.
- Identificar las direcciones IP con más errores.
- Consultar información geográfica aproximada mediante una API.
- Generar reportes en formato JSON.

## 3. Tecnologías utilizadas

- Python 3
- Archivos CSV y JSON
- Biblioteca requests
- collections.Counter
- API IP-API
- Git y GitHub
- PyCharm

## 4. Estructura del proyecto

```text
ti-metrics/
├── data/
│   ├── logs.csv
│   └── events.json
├── reports/
│   └── summary.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── csv_parser.py
│   │   └── json_parser.py
│   └── services/
│       ├── __init__.py
│       ├── geo_service.py
│       └── report_service.py
├── PROMPTS.md
├── README.md
├── requirements.txt
└── .gitignore
```

## 5. Instalación y ejecución

Para instalar las dependencias, ejecutar desde la carpeta principal del proyecto:

```bash
python -m pip install -r requirements.txt
```

Para ejecutar el programa:

```bash
python -m src.main
```

## 6. Resultados de ejecución

En una ejecución de prueba se obtuvieron los siguientes resultados:

| Indicador | Resultado |
| :--- | ---: |
| Registros leídos del CSV | 8 |
| Registros leídos del JSON | 4 |
| Registros inválidos | 0 |
| Registros duplicados | 1 |
| Eventos válidos y únicos | 11 |
| Errores HTTP 500 | 5 |
| Porcentaje de errores HTTP 500 | 45,45 % |

Estos resultados corresponden a los archivos procesados durante esa ejecución. Los valores pueden cambiar si se modifican los datos de entrada.

El reporte se guarda en reports/summary.json.

## 7. API utilizada

El proyecto utiliza IP-API para consultar información geográfica aproximada de las direcciones IP.

Página del servicio: http://ip-api.com/

La disponibilidad de las consultas depende del servicio externo. La ubicación obtenida es aproximada.

## 8. Bitácora de inteligencia artificial

El archivo PROMPTS.md documenta el uso de herramientas de inteligencia artificial durante el desarrollo. La bitácora debe reflejar las consultas realizadas, las sugerencias recibidas y las comprobaciones efectuadas sobre el código.

## 9. Control de versiones

El proyecto utiliza Git para registrar los cambios y GitHub para mantener el repositorio remoto.

Los commits siguen los prefijos semánticos establecidos en la guía de Programación II:

- feat: agregar funcionalidades.
- fix: corregir errores.
- refactor: reorganizar el código sin cambiar su comportamiento.
- docs: actualizar documentación.
- test: agregar o modificar pruebas.

Repositorio del proyecto: https://github.com/CristinaYanza/ti-metrics

## 10. Estado del proyecto

El primer avance contempla la lectura de archivos CSV y JSON, la validación de datos, la identificación de duplicados, el cálculo de métricas, la consulta de la API y la generación del reporte JSON.

Los siguientes hitos incorporarán las mejoras de arquitectura, las pruebas automatizadas y los demás requisitos establecidos por la asignatura.