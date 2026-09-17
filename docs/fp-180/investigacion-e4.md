# FP-180 — Escenario E4, estimacion y politica antes del despliegue

> Generado por `apply_e4_calculators.py` el 2026-09-16. Queda a validacion humana.

## Por que

E4 tenia dos pares puntuados —Infracost y Cloud Custodian— mientras las dos alternativas que FP-126 registro para la categoria, las calculadoras de precios de AWS y Azure, quedaban bajo el umbral de cobertura.

## Una inconsistencia propia corregida

El criterio Optimizacion habia quedado en `NE` para ambas calculadoras cuando la ausencia esta en realidad verificada: ninguna detecta desperdicio ni oportunidades de rightsizing, porque estiman el costo de una configuracion que el usuario describe. Eso es un `0` frente al ancla de FP-177, no un hueco de investigacion, y O2 pasa a `NA` porque no hay recomendacion propia que explicar ni seguir.

## Un hallazgo sobre AWS Pricing Calculator

Es de los pocos productos de la poblacion que documenta su acoplamiento y su salida. Declara donde se guardan las estimaciones («Estimates are saved to the AWS public servers»), exige un reconocimiento explicito antes de compartirlas, fija la vigencia de los enlaces en un ano y ofrece operaciones de borrado por API. Junto con Kubecost, son los unicos dos casos de `D2` puntuado en toda la matriz.

## Celdas completadas (7)

| Producto | Indicador | Valor |
|---|---|---:|
| AWS Pricing Calculator | D2 | 2 |
| AWS Pricing Calculator | O1 | 0 |
| AWS Pricing Calculator | O2 | NA |
| Azure Pricing Calculator | D1 | 2 |
| Azure Pricing Calculator | I2 | 1 |
| Azure Pricing Calculator | O1 | 0 |
| Azure Pricing Calculator | O2 | NA |

## Estado de E4 tras esta pasada

| Producto | S linea base | Banda | Cobertura |
|---|---:|---|---:|
| Infracost | 47.22 | Basic | 75.0% |
| AWS Pricing Calculator | 35.71 | Basic | 87.5% |
| Azure Pricing Calculator | 30.56 | Basic | 75.0% |
| Cloud Custodian | 19.05 | Basic | 77.8% |
