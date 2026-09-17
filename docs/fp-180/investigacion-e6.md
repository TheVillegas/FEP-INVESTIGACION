# FP-180 — Escenario E6, carga distribuida y cientifica de gran escala

> Generado por `apply_e6_distributed.py` el 2026-09-16. Queda a validacion humana.

## Por que

E6 no tenia ningun par puntuado. Sus criterios criticos son Visibilidad e Integracion, y entre sus salidas esperadas estan los componentes del costo total y el costo de red por flujo de trabajo. La red es lo que distingue a este escenario: la evidencia ATLAS/CERN que lo sustenta muestra que la transferencia puede dominar el costo.

## Regla estricta aplicada

V1 e I1 son los dos indicadores donde E6 se diferencia de cualquier otro escenario, y son ademas sus criterios criticos. Aqui se puntuan **solo con evidencia propia sobre costo de red y transferencia**. Un producto sin esa evidencia los conserva en `NE`, aunque su capacidad general de desglose este documentada en otro lado — precisamente para que los criterios criticos de este escenario nunca queden satisfechos por una capacidad verificada para otro.

El resto de indicadores dependientes se subsume desde el escenario de origen del producto, con el argumento registrado celda por celda.

## Celdas completadas (95)

| Producto | Indicador | Valor | Tipo |
|---|---|---:|---|
| AWS Cost Explorer | A1 | 2 | subsumida |
| AWS Cost Explorer | A2 | 2 | subsumida |
| AWS Cost Explorer | AD1 | 2 | subsumida |
| AWS Cost Explorer | AU1 | 2 | subsumida |
| AWS Cost Explorer | I1 | 2 | propia de E6 |
| AWS Cost Explorer | I2 | 2 | subsumida |
| AWS Cost Explorer | O1 | 1 | subsumida |
| AWS Cost Explorer | P2 | 1 | subsumida |
| AWS Cost Explorer | V1 | 2 | propia de E6 |
| AWS Cost Optimization Hub | A1 | 0 | subsumida |
| AWS Cost Optimization Hub | A2 | 0 | subsumida |
| AWS Cost Optimization Hub | AD1 | 2 | subsumida |
| AWS Cost Optimization Hub | AU1 | 0 | subsumida |
| AWS Cost Optimization Hub | I2 | 2 | subsumida |
| AWS Cost Optimization Hub | O1 | 2 | subsumida |
| AWS Cost Optimization Hub | P2 | 0 | subsumida |
| Azure Cost Management | A1 | 2 | subsumida |
| Azure Cost Management | A2 | 2 | subsumida |
| Azure Cost Management | AD1 | 2 | subsumida |
| Azure Cost Management | AU1 | 2 | subsumida |
| Azure Cost Management | I2 | 2 | subsumida |
| Azure Cost Management | O1 | 2 | subsumida |
| Azure Cost Management | P2 | 1 | subsumida |
| CloudHealth | A1 | 2 | subsumida |
| CloudHealth | A2 | 2 | subsumida |
| CloudHealth | AD1 | 2 | subsumida |
| CloudHealth | AU1 | 2 | subsumida |
| CloudHealth | I2 | 1 | subsumida |
| CloudHealth | O1 | 2 | subsumida |
| CloudHealth | P2 | 2 | subsumida |
| CloudZero | A1 | 2 | subsumida |
| CloudZero | A2 | 2 | subsumida |
| CloudZero | AD1 | 2 | subsumida |
| CloudZero | AU1 | 0 | subsumida |
| CloudZero | I2 | 2 | subsumida |
| CloudZero | O1 | 2 | subsumida |
| CloudZero | P2 | 2 | subsumida |
| Cloudability | A1 | 1 | subsumida |
| Cloudability | A2 | 1 | subsumida |
| Cloudability | AD1 | 1 | subsumida |
| Cloudability | I2 | 1 | subsumida |
| Cloudability | O1 | 1 | subsumida |
| Densify | A1 | 0 | subsumida |
| Densify | A2 | 0 | subsumida |
| Densify | AU1 | 2 | subsumida |
| Densify | O1 | 2 | subsumida |
| Finout | A1 | 2 | subsumida |
| Finout | A2 | 2 | subsumida |
| Finout | AD1 | 2 | subsumida |
| Finout | I2 | 1 | subsumida |
| Finout | O1 | 2 | subsumida |
| Google Cloud Billing | A1 | 1 | subsumida |
| Google Cloud Billing | A2 | 0 | subsumida |
| Google Cloud Billing | AD1 | 2 | subsumida |
| Google Cloud Billing | AU1 | 2 | subsumida |
| Google Cloud Billing | I2 | 2 | subsumida |
| Google Cloud Billing | O1 | 0 | subsumida |
| Google Cloud Billing | P2 | 1 | subsumida |
| Google Cloud FinOps Hub | A1 | 0 | subsumida |
| Google Cloud FinOps Hub | A2 | 0 | subsumida |
| Google Cloud FinOps Hub | AD1 | 1 | subsumida |
| Google Cloud FinOps Hub | AU1 | 1 | subsumida |
| Google Cloud FinOps Hub | I2 | 1 | subsumida |
| Google Cloud FinOps Hub | O1 | 2 | subsumida |
| Google Cloud FinOps Hub | P2 | 0 | subsumida |
| Harness Cloud Cost Management | A1 | 2 | subsumida |
| Harness Cloud Cost Management | AU1 | 2 | subsumida |
| Harness Cloud Cost Management | I2 | 2 | subsumida |
| Harness Cloud Cost Management | O1 | 2 | subsumida |
| IBM Cloud Cost Estimator | A1 | 0 | subsumida |
| IBM Cloud Cost Estimator | A2 | 0 | subsumida |
| IBM Cloud Cost Estimator | AU1 | 0 | subsumida |
| IBM Cloud Cost Estimator | I2 | 2 | subsumida |
| IBM Cloud Cost Estimator | O1 | 1 | subsumida |
| IBM Cloud Cost Estimator | P2 | 2 | subsumida |
| OCI Cost Analysis | A1 | 1 | subsumida |
| OCI Cost Analysis | AD1 | 2 | subsumida |
| OCI Cost Analysis | AU1 | 1 | subsumida |
| OCI Cost Analysis | I2 | 2 | subsumida |
| OCI Cost Analysis | O1 | 2 | subsumida |
| Vantage | A1 | 2 | subsumida |
| Vantage | A2 | 2 | subsumida |
| Vantage | AD1 | 2 | subsumida |
| Vantage | AU1 | 2 | subsumida |
| Vantage | I1 | 2 | propia de E6 |
| Vantage | I2 | 2 | subsumida |
| Vantage | O1 | 2 | subsumida |
| Vantage | P2 | 2 | subsumida |
| Vantage | V1 | 2 | propia de E6 |
| nOps | A1 | 2 | subsumida |
| nOps | A2 | 2 | subsumida |
| nOps | AD1 | 2 | subsumida |
| nOps | AU1 | 2 | subsumida |
| nOps | O1 | 2 | subsumida |
| nOps | P2 | 1 | subsumida |

## Estado de E6 tras esta pasada

| Producto | Categoria | S linea base | Banda | Cobertura |
|---|---|---:|---|---:|
| Vantage | Multicloud | 66.67 | Solid | 88.9% |
| AWS Cost Explorer | Cloud nativa | 51.85 | Solid | 100.0% |
| Azure Cost Management | Cloud nativa | 47.62 | Basic | 77.8% |
| Google Cloud Billing | Cloud nativa | 30.95 | Basic | 77.8% |

## Siguen sin puntaje en E6

Les falta evidencia propia sobre costo de red y transferencia, que este escenario exige en sus dos criterios criticos.

| Producto | Cobertura |
|---|---:|
| AWS Cost Optimization Hub | 55.6% |
| CloudHealth | 66.7% |
| CloudZero | 66.7% |
| Cloudability | 33.3% |
| Densify | 22.2% |
| Finout | 44.4% |
| Google Cloud FinOps Hub | 55.6% |
| Harness Cloud Cost Management | 0.0% |
| IBM Cloud Cost Estimator | 44.4% |
| OCI Cost Analysis | 33.3% |
| nOps | 66.7% |
