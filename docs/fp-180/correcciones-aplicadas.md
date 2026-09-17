# FP-180 — Correcciones de alcance aplicadas

> Generado por `apply_scope_corrections.py` el 2026-09-16. Propuesta de corrección metodológica pendiente de validación del equipo.

## Por qué

La primera pasada de puntuación usó `NA` en celdas cuya justificación registrada afirma una **ausencia verificada** («no ofrece», «no calcula», «no expone», «no ejecuta») o una **falta de investigación** («la documentación revisada no describe», «no se identificó»).

En FP-177 los tres estados no son intercambiables: `0` es ausencia verificada y penaliza; `NE` no evidencia y reduce la cobertura; `NA` no aplica y **renormaliza los pesos**, repartiendo el peso ausente entre los criterios restantes. Marcar una ausencia verificada como `NA` elimina la penalización y la convierte en ventaja: un producto angosto supera a uno amplio que sí cubre el escenario. Es justamente lo que el criterio de término de FP-180 prohíbe.

Esta pasada **no agrega investigación nueva ni modifica evidencia o fuentes**: cada cambio se deriva del texto que la propia celda ya tenía registrado.

`NA` se conserva donde el indicador no tiene objeto para el producto en la unidad de análisis del escenario (por ejemplo AU2, «salvaguardas antes de actuar», cuando AU1 es 0: no hay ejecución que resguardar).

## Celdas corregidas (163 filas; 48 celdas únicas)

| Producto | Indicador | NA → | Motivo |
|---|---|---|---|
| AWS Cost Optimization Hub | A1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | A2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | AD2 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| AWS Cost Optimization Hub | AU1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | D1 | `NE` | La justificación es una decisión de alcance del evaluador para evitar doble conteo entre productos del mismo proveedor, no una propiedad verificada del producto: se marca NE hasta investigarlo. |
| AWS Cost Optimization Hub | D2 | `NE` | La justificación es una decisión de alcance del evaluador para evitar doble conteo entre productos del mismo proveedor, no una propiedad verificada del producto: se marca NE hasta investigarlo. |
| AWS Cost Optimization Hub | M1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | M2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | P1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | P2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | V1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| AWS Cost Optimization Hub | V2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Cast AI | P1 | `NE` | La justificación NA reinterpreta P1 como estimación previa al despliegue; el indicador tiene objeto y no fue investigado. |
| Cast AI | P2 | `NE` | Mismo motivo que P1. |
| Cloud Custodian | A1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Cloud Custodian | A2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Cloud Custodian | O2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Cloud Custodian | P1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Cloud Custodian | P2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Cloud Custodian | V1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Cloud Custodian | V2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud Billing | O1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud Billing | O2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | A1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | A2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | AU2 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| Google Cloud FinOps Hub | D1 | `NE` | La justificación es una decisión de alcance del evaluador para evitar doble conteo entre productos del mismo proveedor, no una propiedad verificada del producto: se marca NE hasta investigarlo. |
| Google Cloud FinOps Hub | D2 | `NE` | La justificación es una decisión de alcance del evaluador para evitar doble conteo entre productos del mismo proveedor, no una propiedad verificada del producto: se marca NE hasta investigarlo. |
| Google Cloud FinOps Hub | M1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | M2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | P1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | P2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | V1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Google Cloud FinOps Hub | V2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Infracost | AU1 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| Kubecost | P1 | `NE` | La justificación NA reinterpreta P1 como estimación previa al despliegue; el indicador tiene objeto y no fue investigado. |
| Kubecost | P2 | `NE` | Mismo motivo que P1. |
| OpenCost | O2 | `0` | La justificación registrada afirma una ausencia verificada contra documentación oficial, no una inaplicabilidad: en FP-177 eso corresponde al valor 0, no a NA. |
| OpenCost | P1 | `NE` | La justificación NA reinterpreta P1 como estimación previa al despliegue; FP-177 define P1 como exposición de precio, moneda, región, unidad y supuestos, que sí tiene objeto para una herramienta de costo de clúster. Queda NE hasta investigarlo. |
| OpenCost | P2 | `NE` | Mismo motivo que P1: el indicador tiene objeto y no fue investigado. |
| StormForge | A1 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| StormForge | A2 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| StormForge | M1 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| StormForge | M2 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| StormForge | P1 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| StormForge | P2 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| StormForge | V1 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |
| StormForge | V2 | `NE` | La justificación registrada indica que la documentación revisada no describe la función o que no se investigó: en FP-177 eso corresponde a NE (reduce cobertura), no a NA (renormaliza pesos). |

## Efecto en los resultados

| Escenario | Producto | S base antes | S base después | Banda antes | Banda después |
|---|---|---:|---:|---|---|
| E1 | AWS Cost Optimization Hub | 66.67 | 19.05 | Solid | Basic |
| E2 | AWS Cost Optimization Hub | 66.67 | 19.05 | Solid | Basic |
| E3 | AWS Cost Optimization Hub | 66.67 | 19.05 | Solid | Basic |
| E5 | AWS Cost Optimization Hub | 66.67 | 19.05 | Solid | Basic |
| E6 | AWS Cost Optimization Hub | 66.67 | 19.05 | Solid | Basic |
| E1 | Google Cloud Billing | 43.75 | 38.89 | Basic | Basic |
| E2 | Google Cloud Billing | 43.75 | 38.89 | Basic | Basic |
| E3 | Google Cloud Billing | 43.75 | 38.89 | Basic | Basic |
| E5 | Google Cloud Billing | 43.75 | 38.89 | Basic | Basic |
| E6 | Google Cloud Billing | 43.75 | 38.89 | Basic | Basic |
| E1 | Google Cloud FinOps Hub | 50.00 | 23.81 | Solid | Basic |
| E2 | Google Cloud FinOps Hub | 50.00 | 23.81 | Solid | Basic |
| E3 | Google Cloud FinOps Hub | 50.00 | 23.81 | Solid | Basic |
| E5 | Google Cloud FinOps Hub | 50.00 | 23.81 | Solid | Basic |
| E6 | Google Cloud FinOps Hub | 50.00 | 23.81 | Solid | Basic |
| E3 | OpenCost | 35.71 | 33.33 | Basic | Basic |
| E5 | OpenCost | 35.71 | 33.33 | Basic | Basic |
| E4 | Infracost | 56.67 | 47.22 | Solid | Basic |
| E4 | Cloud Custodian | — | 19.05 | Insufficient evidence | Basic |

## Qué sigue sin resolver

Esta corrección no toca el segundo defecto de fondo: la puntuación sigue siendo idéntica para un mismo producto en todos sus escenarios, de modo que la unidad de análisis producto × escenario que declara FP-177 todavía no está implementada. Requiere re-evaluar los indicadores sensibles al escenario (V1, V2, A2, O1, AU1, M1, M2, I1, I2, P2, AD1) contra las entradas y salidas de cada escenario, con investigación documental adicional.
