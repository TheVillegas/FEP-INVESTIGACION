# FP-180 — Escenario E1 completado con las plataformas multinube

> Generado por `apply_e1_multicloud.py` el 2026-09-16. Queda a validacion humana.

## Por que

FP-177 §4 lista a las plataformas multinube como elegibles en E1 **sin condicion alguna**, pero ninguna tenia puntaje ahi: la convencion de escenario ancla dejaba su evidencia estacionada en E2. Al abandonar ese atajo, E1 se puede completar como corresponde.

## Dos tipos de evidencia, declarados celda por celda

**Evidencia propia de E1.** Las salidas esperadas de E1 incluyen «gasto no asignado» y un reporte de showback, que E2 nunca pide. Por eso A1 se investigo especificamente contra eso: si la herramienta hace visible el gasto que no logra asignar.

**Evidencia subsumida.** Para el resto de indicadores dependientes del escenario, la capacidad documentada para E2 cubre E1 por inclusion: una plataforma que consolida y desglosa costo entre varios proveedores necesariamente lo hace para uno, que es la condicion de E1. Es un argumento explicito registrado en cada celda, no un valor copiado: donde la capacidad no subsume, la celda no se toca.

## Celdas completadas (60)

| Producto | Indicador | Valor | Tipo de evidencia |
|---|---|---:|---|
| CloudHealth | A1 | 2 | propia de E1 |
| CloudHealth | A2 | 2 | subsumida desde E2 |
| CloudHealth | AD1 | 2 | subsumida desde E2 |
| CloudHealth | AU1 | 2 | subsumida desde E2 |
| CloudHealth | I1 | 2 | subsumida desde E2 |
| CloudHealth | I2 | 1 | subsumida desde E2 |
| CloudHealth | O1 | 2 | subsumida desde E2 |
| CloudHealth | P2 | 2 | subsumida desde E2 |
| CloudHealth | V1 | 2 | subsumida desde E2 |
| CloudZero | A1 | 2 | propia de E1 |
| CloudZero | A2 | 2 | subsumida desde E2 |
| CloudZero | AD1 | 2 | subsumida desde E2 |
| CloudZero | AU1 | 0 | subsumida desde E2 |
| CloudZero | I1 | 2 | subsumida desde E2 |
| CloudZero | I2 | 2 | subsumida desde E2 |
| CloudZero | O1 | 2 | subsumida desde E2 |
| CloudZero | P2 | 2 | subsumida desde E2 |
| CloudZero | V1 | 2 | subsumida desde E2 |
| Cloudability | A1 | 1 | subsumida desde E2 |
| Cloudability | A2 | 1 | subsumida desde E2 |
| Cloudability | AD1 | 1 | subsumida desde E2 |
| Cloudability | I1 | 1 | subsumida desde E2 |
| Cloudability | I2 | 1 | subsumida desde E2 |
| Cloudability | O1 | 1 | subsumida desde E2 |
| Cloudability | V1 | 1 | subsumida desde E2 |
| Densify | A1 | 0 | ausencia verificada en E1 |
| Densify | A2 | 0 | ausencia verificada en E1 |
| Densify | AU1 | 2 | ausencia verificada en E1 |
| Densify | O1 | 2 | ausencia verificada en E1 |
| Densify | V1 | 0 | ausencia verificada en E1 |
| Finout | A1 | 2 | subsumida desde E2 |
| Finout | A2 | 2 | subsumida desde E2 |
| Finout | AD1 | 2 | subsumida desde E2 |
| Finout | I1 | 2 | subsumida desde E2 |
| Finout | I2 | 1 | subsumida desde E2 |
| Finout | O1 | 2 | subsumida desde E2 |
| Finout | V1 | 2 | subsumida desde E2 |
| Harness Cloud Cost Management | A1 | 2 | subsumida desde E2 |
| Harness Cloud Cost Management | AU1 | 2 | subsumida desde E2 |
| Harness Cloud Cost Management | I1 | 2 | subsumida desde E2 |
| Harness Cloud Cost Management | I2 | 2 | subsumida desde E2 |
| Harness Cloud Cost Management | O1 | 2 | subsumida desde E2 |
| Harness Cloud Cost Management | V1 | 2 | subsumida desde E2 |
| Vantage | A1 | 2 | propia de E1 |
| Vantage | A2 | 2 | subsumida desde E2 |
| Vantage | AD1 | 2 | subsumida desde E2 |
| Vantage | AU1 | 2 | subsumida desde E2 |
| Vantage | I1 | 2 | subsumida desde E2 |
| Vantage | I2 | 2 | subsumida desde E2 |
| Vantage | O1 | 2 | subsumida desde E2 |
| Vantage | P2 | 2 | subsumida desde E2 |
| Vantage | V1 | 2 | subsumida desde E2 |
| nOps | A1 | 2 | subsumida desde E2 |
| nOps | A2 | 2 | subsumida desde E2 |
| nOps | AD1 | 2 | subsumida desde E2 |
| nOps | AU1 | 2 | subsumida desde E2 |
| nOps | I1 | 2 | subsumida desde E2 |
| nOps | O1 | 2 | subsumida desde E2 |
| nOps | P2 | 1 | subsumida desde E2 |
| nOps | V1 | 2 | subsumida desde E2 |

## Celdas que siguen en NE

Su producto tampoco tiene evidencia en E2, asi que no hay nada que subsumir. El motivo original ya esta registrado en cada celda.

| Producto | Indicador |
|---|---|
| Cloudability | AU1 |
| Cloudability | P2 |
| Densify | AD1 |
| Densify | I1 |
| Densify | I2 |
| Densify | P2 |
| Finout | AU1 |
| Finout | P2 |
| Harness Cloud Cost Management | A2 |
| Harness Cloud Cost Management | AD1 |
| Harness Cloud Cost Management | P2 |
| nOps | I2 |

## Estado de E1 tras esta pasada

| Producto | Categoria | S linea base | Banda | Cobertura |
|---|---|---:|---|---:|
| Vantage | Multicloud | 66.67 | Solid | 88.9% |
| nOps | Multicloud | 59.52 | Solid | 77.8% |
| CloudZero | Multicloud | 58.33 | Solid | 88.9% |
| CloudHealth | Multicloud | 56.25 | Solid | 88.9% |
| AWS Cost Explorer | Cloud nativa | 51.85 | Solid | 100.0% |
| Azure Cost Management | Cloud nativa | 51.85 | Solid | 100.0% |
| Google Cloud Billing | Cloud nativa | 38.89 | Basic | 100.0% |
| Google Cloud FinOps Hub | Cloud nativa | 23.81 | Basic | 77.8% |
| AWS Cost Optimization Hub | Cloud nativa | 19.05 | Basic | 77.8% |

Siguen en «Insufficient evidence» en E1: Cloudability, Densify, Finout, Harness Cloud Cost Management, IBM Cloud Cost Estimator, OCI Cost Analysis. El motivo de cada celda pendiente esta registrado en la hoja Puntuacion.
