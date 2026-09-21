# Preguntas — Escenarios, metodología comparativa y línea base TCO (FP-52)

- **Tema:** caso aplicado, arquitectura y supuestos, costo total de propiedad, optimización, sensibilidad y evaluación financiera.
- **Entregable de referencia:** `Trabajo_de_Investigación___OneByte/Secciones/05-CasoAplicado-TINV.tex`.
- **Responsable:** Lucas.
- **Estado:** matriz de 10 preguntas preparada; redacción humana pendiente.

## Resumen de referencia

> Síntesis organizativa de la sección 5; no reemplaza su lectura ni interpreta sus cifras.

- **Caso y arquitectura:** alcance académico, servicios de Azure y condiciones comunes entre regiones (§5.1–§5.3).
- **Supuestos y demanda:** parámetros técnicos, costos de referencia, volumen de solicitudes y limitaciones (§5.4–§5.5).
- **Costos y optimización:** costos mensuales, costo por solicitud, costo total de propiedad y tres medidas de optimización (§5.6–§5.11).
- **Comparación y sensibilidad:** diferencias regionales y variables con mayor efecto en la factura (§5.12–§5.14).
- **Evaluación financiera:** valor actual neto, tasa interna de retorno, periodo de recuperación y conclusión del caso (§5.15–§5.16).

## Distribución exigida para este aporte

| Dificultad | Cantidad | Competencia principal |
|---|---:|---|
| Básica | 4 | Comprensión |
| Intermedia | 4 | Aplicación |
| Avanzada | 2 | Análisis crítico |
| **Total** | **10** | |

La distribución equivale al 40 % de preguntas básicas, 40 % intermedias y 20 % avanzadas exigido por la rúbrica. Los cuatro formatos obligatorios quedan representados: selección múltiple, verdadero o falso, completar y respuesta corta.

## Matriz de redacción humana

| N.º | Nivel | Formato | Subsección | Objetivo que debe evaluar | Evidencia disponible en la sección 5 |
|---:|---|---|---|---|---|
| 1 | Básica | Selección múltiple | §5.1 | Reconocer el propósito y el alcance del caso aplicado. | Horizonte de cinco años; análisis documental; sin despliegue ni pruebas de carga. |
| 2 | Básica | Verdadero o falso | §5.2–§5.3 | Identificar los componentes de la arquitectura y las variables que permanecen constantes entre regiones. | Container Apps, PostgreSQL, Blob Storage y Azure Monitor; misma arquitectura y demanda. |
| 3 | Básica | Completar | §5.4 | Distinguir un supuesto de modelación de una medición productiva. | Latencia y rendimiento no medidos; tasa y tarifa horaria usadas como referencias. |
| 4 | Básica | Respuesta corta | §5.5–§5.7 | Explicar cómo se obtiene el costo por solicitud. | 1,1 millones de solicitudes mensuales y 66 millones en 60 meses. |
| 5 | Intermedia | Selección múltiple | §5.6–§5.8 | Comparar los costos regionales y seleccionar la alternativa económica bajo los supuestos del caso. | USD 22.741,97 en Chile Central y USD 16.476,92 en East US. |
| 6 | Intermedia | Verdadero o falso | §5.9–§5.11 | Aplicar las condiciones de las tres medidas de optimización sin atribuir ahorros no medidos. | Reducción de horas no productivas, ingesta de registros y salida de datos. |
| 7 | Intermedia | Completar | §5.12 | Relacionar costo, residencia de datos, latencia y disponibilidad con la recomendación regional. | East US es la alternativa económica; Chile Central se mantiene si se prioriza proximidad o residencia. |
| 8 | Intermedia | Respuesta corta | §5.13–§5.14 | Interpretar qué variable domina la sensibilidad del costo y por qué. | PostgreSQL con 4 vCores produce la mayor variación; la capacidad está provisionada. |
| 9 | Avanzada | Selección múltiple | §5.15 | Analizar la diferencia entre elegir la región más barata y decidir si conviene aplicar el paquete FinOps. | East US tiene menor costo regional; el paquete obtiene VAN positivo en Chile Central y negativo en East US. |
| 10 | Avanzada | Respuesta corta | §5.4, §5.12 y §5.16 | Evaluar la solidez de la recomendación considerando supuestos y evidencia faltante. | Faltan mediciones de latencia, rendimiento y telemetría; se requiere revisión comercial, técnica y legal. |

## Control de calidad para la redacción

- Cada pregunta debe medir solo el objetivo asignado en la matriz.
- Las preguntas de selección múltiple deben incluir cuatro alternativas homogéneas y una sola respuesta correcta.
- Los distractores deben ser plausibles y no pueden introducir datos ausentes de la sección 5.
- Las preguntas de verdadero o falso deben evitar absolutos que revelen la respuesta.
- Las preguntas de completar deben admitir una respuesta inequívoca.
- Las respuestas cortas deben indicar los elementos mínimos esperados para corregirlas.
- Cada pregunta debe incluir respuesta correcta y una justificación breve que cite la subsección correspondiente.
- Las preguntas 9 y 10 deben exigir una relación entre resultados y supuestos, no la repetición aislada de una cifra.
- Antes de consolidar, una persona debe comprobar que no haya duplicaciones, ambigüedades ni pistas involuntarias.

## Preguntas

<!--
Lucas redacta aquí las 10 preguntas según la matriz anterior.
La rúbrica 6.1 reserva a una persona la redacción de enunciados, opciones,
respuestas y justificaciones. No reemplazar este comentario con texto generado por IA.
-->
