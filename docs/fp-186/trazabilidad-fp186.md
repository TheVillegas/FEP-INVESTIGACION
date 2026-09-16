# FP-186 — Trazabilidad del análisis de sensibilidad

## Entradas

| Tarea | Uso |
|---|---|
| FP-182 | Arquitectura, configuración y reglas de franquicia. |
| FP-183 | Costos mensuales y tarifas; hash verificado antes y después de ejecutar. |
| FP-184 | Contexto de palancas y costos de implementación pendientes. |
| FP-185 | Comparación regional y disponibilidad. |

## Método corregido

1. `sensitivity.py` abre FP-183 en solo lectura.
2. Reproduce las 12 líneas facturables por región, incluidas franquicias y egress gratuito.
3. Evalúa variables continuas con un rango exploratorio del equipo de ±20 %.
4. Evalúa PostgreSQL con tamaños General Purpose discretos de 2, 4 y 8 vCores; no usa porcentajes fraccionarios sobre una SKU.
5. Ordena por máximo cambio relativo promedio entre regiones y genera una matriz conjunta 3×5.
6. Verifica 1.440 celdas mensuales, totales, monotonicidad y SHA-256.

## Resultado

- Variables principales: **vCores PostgreSQL producción** y **vCPU producción**.
- Base Chile Central: USD 23.256,32.
- Base East US: USD 16.474,60.
- El rango ±20 % es una decisión de escenario del equipo, no una cifra extraída de papers.

## Evidencia

- `docs/fp-186/sensitivity.py`
- `docs/fp-186/resultados.json`
- `docs/fp-186/sensibilidad.html`
- `docs/fp-183/modelo-tco-linea-base-5-anos.xlsx`

## Trazabilidad académica

- Chaisiri et al.: provisión bajo incertidumbre.
- Cho: optimización con restricciones presupuestarias.
- CloudPricingOps: comparación de políticas y necesidad de datos vigentes.
- DoE Kubernetes: experimentación de CPU/memoria.
- ATLAS: materialidad potencial del egress.

El paper de contabilidad de recursos compartidos se usa para asignación/costos compartidos, no como evidencia directa de backup o egress.

## Pendientes humanos

- Completar esfuerzo operativo y costos de implementación.
- Validar rangos, SKU, HA y contrato.
- Medir latencia antes de la recomendación regional final.
