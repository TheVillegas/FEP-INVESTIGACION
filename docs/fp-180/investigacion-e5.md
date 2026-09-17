# FP-180 — Escenario E5, atribucion en servicio compartido o multi-tenant

> Generado por `apply_e5_multitenant.py` el 2026-09-16. Queda a validacion humana.

## Por que

E5 no tenia ningun par puntuado. Sus criterios criticos son Asignacion y Visibilidad, y sus salidas esperadas son el costo atribuido, **la porcion que no se puede atribuir**, el metodo de reparto y la trazabilidad de sus supuestos.

## Como se puntuo

El indicador que define este escenario es A2, la regla de reparto del costo compartido, asi que se investigo **por separado para E5** en lugar de arrastrarlo. El resto de los indicadores dependientes se subsumen desde el escenario de origen de cada producto con el mismo argumento explicito usado en E1: la capacidad de desglosar y asignar costo no cambia porque la carga sea compartida; donde si cambia —la regla de reparto— la evidencia es propia.

La evidencia de A2 encontrada nombra el caso de E5 de forma directa: AWS documenta split charge rules para «costs shared by multiple teams, business units, and financial owners»; Vantage menciona literalmente «multi-tenant databases»; CloudHealth separa Direct de Indirect Costs; y CloudZero deja el remanente no atribuible en un elemento identificable.

## Celdas completadas (1)

| Producto | Indicador | Valor | Tipo |
|---|---|---:|---|
| Google Cloud Billing | A2 | 1 | propia de E5 |

## Estado de E5 tras esta pasada

| Producto | Categoria | S linea base | Banda | Cobertura |
|---|---|---:|---|---:|
| Vantage | Multicloud | 66.67 | Solid | 88.9% |
| CloudZero | Multicloud | 58.33 | Solid | 88.9% |
| CloudHealth | Multicloud | 56.25 | Solid | 88.9% |
| AWS Cost Explorer | Cloud nativa | 51.85 | Solid | 100.0% |
| Azure Cost Management | Cloud nativa | 51.85 | Solid | 100.0% |
| Google Cloud Billing | Cloud nativa | 40.74 | Basic | 100.0% |

Siguen sin puntaje en E5: AWS Cost Optimization Hub (66.7%), Cast AI (44.4%), Cloudability (33.3%), Densify (22.2%), Finout (55.6%), Google Cloud FinOps Hub (66.7%), Harness Cloud Cost Management (11.1%), IBM Cloud Cost Estimator (55.6%), Kubecost (44.4%), OCI Cost Analysis (55.6%), OpenCost (66.7%), PerfectScale (22.2%), ScaleOps (22.2%), StormForge (33.3%), nOps (66.7%).

El motivo de cada celda pendiente esta registrado en la hoja Puntuacion.
