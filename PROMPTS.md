
# Bitácora de uso de IA — TI-Metrics

Asignatura: Programación II  
Estudiante: Jennyfer Yanza  
Proyecto: TI-Metrics — Engine de Analítica de Logs y Monitoreo de Infraestructura

## Registro de Prompt #1: Organización inicial del proyecto

- Fecha: 2026-09-25
- Módulo/Función: Estructura inicial del proyecto.
- Prompt enviado: Solicité orientación para comprender cómo iniciar el proyecto TI-Metrics y organizar sus archivos en Python.
- Respuesta de la IA: Recibí una explicación sobre la separación de responsabilidades entre la lectura de datos, el procesamiento de registros y la generación de reportes.
- Análisis crítico: La organización por módulos facilita la comprensión y el mantenimiento del programa. Sin embargo, fue necesario identificar qué archivos correspondían a las funciones realmente implementadas en el primer avance.
- Solución final aplicada: Organicé el proyecto en carpetas para los datos de entrada, los analizadores, los servicios y los reportes. La estructura se puede ampliar en los siguientes hitos.

## Registro de Prompt #2: Archivos CSV y JSON

- Fecha: 2026-09-25
- Módulo/Función: src/parsers/csv_parser.py y src/parsers/json_parser.py
- Prompt enviado: Solicité ayuda para definir datos de prueba en archivos CSV y JSON y comprender cómo estructurarlos para analizar registros.
- Respuesta de la IA: Recibí ejemplos de registros con direcciones IP, códigos HTTP y valores relacionados con el consumo de recursos.
- Análisis crítico: Los datos de prueba permiten verificar la lectura de distintos formatos y el cálculo de métricas. Es necesario comprobar que la estructura de cada registro coincida con la que espera el programa.
- Solución final aplicada: Utilicé datos de prueba en logs.csv y events.json para ejecutar el programa y revisar los registros procesados.

## Registro de Prompt #3: Consulta de información geográfica

- Fecha: 2026-09-25
- Módulo/Función: src/services/geo_service.py
- Prompt enviado: Solicité orientación para elegir una API que permitiera obtener información geográfica aproximada a partir de una dirección IP y utilizarla desde Python.
- Respuesta de la IA: Recibí una explicación sobre IP-API y el uso de la biblioteca requests para realizar solicitudes HTTP.
- Análisis crítico: La consulta depende de un servicio externo, por lo que pueden existir errores de conexión, límites de uso o respuestas incompletas. También es importante comprobar el estado de la respuesta antes de utilizar sus datos.
- Solución final aplicada: Integré las consultas a IP-API en el proyecto y comprobé que las solicitudes de prueba devolvieran respuestas satisfactorias.

## Registro de Prompt #4: Comprobación de resultados

- Fecha: 2026-10-10
- Módulo/Función: src/main.py y src/services/report_service.py
- Prompt enviado: Solicité ayuda para comprender los resultados del programa y revisar las métricas relacionadas con errores HTTP 500 y registros duplicados.
- Respuesta de la IA: Recibí explicaciones sobre la interpretación de las métricas y la revisión del reporte generado.
- Análisis crítico: Los resultados deben corresponder a los datos de entrada y las reglas de validación implementadas. Es necesario distinguir los registros leídos de los registros válidos, duplicados y únicos.
- Solución final aplicada: Ejecuté el programa, revisé los resultados impresos en consola y comprobé la generación de reports/summary.json.

## Observaciones

Esta bitácora documenta las consultas de apoyo utilizadas durante el desarrollo del proyecto. Se actualizará en los siguientes hitos para registrar las nuevas consultas, las respuestas recibidas, el análisis del código y las modificaciones realizadas.
