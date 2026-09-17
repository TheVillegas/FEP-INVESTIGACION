# FP-180 — Escenario E3, optimizacion y automatizacion en Kubernetes

> Generado por `apply_e3_kubernetes.py` el 2026-09-16. Queda a validacion humana.

## Por que

E3 tenia un solo par puntuado (OpenCost) pese a contar con seis herramientas de Kubernetes elegibles, mas las categorias nativa y multinube. Esta pasada completa las celdas que bloqueaban a los productos mas cercanos al umbral.

## CloudZero y la condicion de elegibilidad

FP-177 §4 admite plataformas multinube en E3 solo «si integran datos de cluster». Esa condicion se **verifico** en lugar de suponerse: la documentacion de CloudZero describe un agente de Kubernetes que recoge uso por pod, mas dos vias alternativas de ingesta (AWS Split Cost Allocation Data y GKE Cost Allocation).

Sus celdas de E3 se puntuaron contra las entradas y salidas de este escenario, **no se arrastraron desde E2**: consolidar varios proveedores no dice nada sobre leer un cluster, asi que ahi no hay subsuncion posible.

## Celdas completadas (6)

| Producto | Indicador | Valor |
|---|---|---:|
| CloudZero | A2 | 2 |
| CloudZero | AD1 | 2 |
| CloudZero | AU1 | 0 |
| CloudZero | I2 | 2 |
| CloudZero | O1 | 2 |
| Kubecost | D2 | 2 |

## Estado de E3 tras esta pasada

| Producto | Categoria | S linea base | Banda | Cobertura |
|---|---|---:|---|---:|
| CloudZero | Multicloud | 57.14 | Solid | 77.8% |
| Kubecost | Kubernetes | 50.00 | Solid | 77.8% |
| OpenCost | Kubernetes | 33.33 | Basic | 77.8% |

## Siguen sin puntaje en E3

| Producto | Cobertura |
|---|---:|
| AWS Cost Explorer | 22.2% |
| AWS Cost Optimization Hub | 11.1% |
| Azure Cost Management | 22.2% |
| Cast AI | 55.6% |
| Google Cloud Billing | 22.2% |
| Google Cloud FinOps Hub | 11.1% |
| IBM Cloud Cost Estimator | 11.1% |
| OCI Cost Analysis | 11.1% |
| PerfectScale | 22.2% |
| ScaleOps | 22.2% |
| StormForge | 33.3% |

El motivo de cada celda pendiente esta registrado en la hoja Puntuacion.
