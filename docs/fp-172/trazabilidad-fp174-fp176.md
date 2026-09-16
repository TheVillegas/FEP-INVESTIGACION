# FP-174 y FP-176 — Trazabilidad de regiones y parámetros

## FP-174

La hoja `Regiones` del maestro TINV-04 compara Chile Central y East US con servicios, unidades, moneda, fecha, residencia, latencia/HA y prima regional. La disponibilidad de PostgreSQL se tomó de Microsoft Learn; la latencia continúa como expectativa no medida.

## FP-176

La hoja `Parametros_TCO` contiene 15 parámetros con unidad, valor/rango, justificación, fuente, fecha y riesgo. Incluye Container Apps, PostgreSQL, storage, egress, logs, backup, HA, regiones, horizonte y los dos inputs pendientes de operación.

## Relación con FP-52

FP-182 y FP-183 consumen estos parámetros. Los vacíos de horas y tarifa operativa permanecen pendientes y no se convierten en cero.
