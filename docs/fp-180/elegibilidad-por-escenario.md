# FP-180 — Condición de elegibilidad de E2 aplicada

> Generado por `apply_scenario_eligibility.py` el 2026-09-17. Corrección derivada del texto de FP-177, sin decisión metodológica nueva.

## Qué dice FP-177

La sección 4 enumera las categorías elegibles de cada escenario, y cuatro entradas llevan condición explícita:

| Escenario | Categoría | Condición | Tipo |
|---|---|---|---|
| E2 | nativas | «para la parte de su proveedor» | **alcance** |
| E3 | multicloud | «si integran datos de clúster» | elegibilidad |
| E4 | nativas | «cuando soporten estimación previa» | elegibilidad |
| E5 | Kubernetes | «cuando el servicio compartido se ejecute en clúster» | contexto |

Las tres últimas deciden si el producto entra al escenario, y la matriz ya las respeta. La de E2 es distinta: el producto entra, pero con su alcance acotado, y esa no se estaba aplicando.

## El problema corregido

Las herramientas nativas en E2 estaban puntuadas `M1 = M2 = 0`, que significa ausencia verificada de consolidación multinube. Como Multicloud es criterio crítico de E2, las siete figuraban **incumpliendo un criterio crítico por no hacer algo que el escenario no les pide**.

El estado correcto es `NA` con justificación de alcance. Conviene notar la diferencia con los `NA` corregidos en `correcciones-aplicadas.md`: aquellos los ponía el evaluador razonando que otro producto del mismo proveedor cubría la función, y eran ausencia verificada disfrazada. Este lo declara el escenario en el texto aprobado por el equipo, que es precisamente el respaldo que a los otros les faltaba.

## Celdas corregidas (14)

| Producto | Indicador | Antes | Ahora |
|---|---|---:|---|
| AWS Cost Explorer | M1 | 0 | `NA` |
| AWS Cost Explorer | M2 | 0 | `NA` |
| AWS Cost Optimization Hub | M1 | 0 | `NA` |
| AWS Cost Optimization Hub | M2 | 0 | `NA` |
| Azure Cost Management | M1 | 0 | `NA` |
| Azure Cost Management | M2 | 0 | `NA` |
| Google Cloud Billing | M1 | 0 | `NA` |
| Google Cloud Billing | M2 | 0 | `NA` |
| Google Cloud FinOps Hub | M1 | 0 | `NA` |
| Google Cloud FinOps Hub | M2 | 0 | `NA` |
| IBM Cloud Cost Estimator | M1 | 0 | `NA` |
| IBM Cloud Cost Estimator | M2 | 0 | `NA` |
| OCI Cost Analysis | M1 | 0 | `NA` |
| OCI Cost Analysis | M2 | 0 | `NA` |

## Efecto en los resultados

| Escenario | Producto | S antes | S después | Cobertura antes | Cobertura después |
|---|---|---|---|---:|---:|
| E2 | AWS Cost Explorer | Insuf. | Insuf. | 22.2% | 12.5% |
| E2 | AWS Cost Optimization Hub | Insuf. | Insuf. | 11.1% | 0.0% |
| E2 | Azure Cost Management | Insuf. | Insuf. | 22.2% | 12.5% |
| E2 | Google Cloud Billing | Insuf. | Insuf. | 22.2% | 12.5% |
| E2 | Google Cloud FinOps Hub | Insuf. | Insuf. | 11.1% | 0.0% |
| E2 | IBM Cloud Cost Estimator | Insuf. | Insuf. | 11.1% | 0.0% |
| E2 | OCI Cost Analysis | Insuf. | Insuf. | 11.1% | 0.0% |

## Hallazgo relacionado, no aplicado

La condición de E4 —nativas «cuando soporten estimación previa»— habilita un caso que la matriz tampoco cubre: **IBM Cloud Cost Estimator cumple esa condición y no está evaluado en E4**. Toda la evidencia recogida para ese producto describe estimación previa al despliegue, es decir, corresponde a E4 y no a E1, donde hoy figura por pertenecer a la categoría nativa.

Eso resolvería sin reclasificar nada la tensión registrada en `alternativas-adicionales.md`: el producto no está mal categorizado, está evaluado en el escenario equivocado. Requiere decisión del equipo antes de aplicarse.
