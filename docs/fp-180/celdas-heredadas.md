# FP-180 — Celdas heredadas marcadas como NE

> Generado por `mark_scenario_inherited.py` el 2026-09-16. Propuesta de corrección metodológica pendiente de validación del equipo.

## Por qué

Cada producto se investigó una sola vez y su puntuación se copió a todos sus escenarios elegibles: los 15 productos multiescenario tenían valores **y texto de evidencia idénticos** en todos ellos. Las 61 filas de la hoja Calculo contenían 17 evaluaciones, no 61.

FP-177 §1 fija la unidad de resultado en producto × escenario y exige probar cada producto «con las mismas entradas del escenario». Una recomendación por escenario no puede salir de una matriz cuyos números no cambian entre escenarios.

## Qué indicadores dependen del escenario

Un indicador depende del escenario cuando su pregunta observable en la matriz de FP-177 se refiere al escenario mismo:

| Indicador | Por qué depende del escenario |
|---|---|
| V1 | La unidad de desglose cambia: cuenta/proyecto en E1, namespace en E3, entidad en E5. |
| A1 | La entidad de asignación es la del escenario. |
| A2 | Las reglas de reparto compartido son centrales en E5 y marginales en E1. |
| O1 | Pregunta por desperdicio «relevante al escenario» (texto literal). |
| AU1 | Las acciones de costo son las del escenario. |
| I1 | Pregunta si integra «los datos requeridos … del escenario» (texto literal). |
| I2 | Pregunta por el «flujo de trabajo relevante» del escenario (texto literal). |
| AD1 | Pregunta por acceso «para los roles del escenario» (texto literal). |
| P2 | La estimación o comparación es contextual al escenario. |

Los otros nueve (V2, O2, AU2, M1, M2, AD2, P1, D1, D2) describen propiedades del producto y no del escenario, así que una sola investigación los sostiene en todos y **no se tocaron**.

## Escenario ancla por categoría

La evidencia registrada sostiene el valor solo en el escenario donde se recogió: el escenario en que FP-177 §4 sitúa a esa categoría como actor principal.

| Categoría | Escenario ancla |
|---|---|
| Cloud nativa | E1 |
| Multicloud | E2 |
| Kubernetes | E3 |
| Estimacion temprana | E4 |

Fuera del ancla el valor es heredado, no tiene evidencia propia y pasa a `NE`: sale del puntaje y reduce la cobertura, que es lo que FP-177 prescribe para lo no evidenciado. No pasa a `NA`, que renormalizaría los pesos y escondería el hueco.

## Celdas marcadas (338)

| Producto | Escenario | Indicador | Valor heredado | Escenario de origen |
|---|---|---|---:|---|
| AWS Cost Explorer | E2 | A1 | 2 | E1 |
| AWS Cost Explorer | E2 | A2 | 2 | E1 |
| AWS Cost Explorer | E2 | AD1 | 2 | E1 |
| AWS Cost Explorer | E2 | AU1 | 2 | E1 |
| AWS Cost Explorer | E2 | I1 | 2 | E1 |
| AWS Cost Explorer | E2 | I2 | 2 | E1 |
| AWS Cost Explorer | E2 | O1 | 1 | E1 |
| AWS Cost Explorer | E2 | P2 | 1 | E1 |
| AWS Cost Explorer | E2 | V1 | 2 | E1 |
| AWS Cost Explorer | E3 | A1 | 2 | E1 |
| AWS Cost Explorer | E3 | A2 | 2 | E1 |
| AWS Cost Explorer | E3 | AD1 | 2 | E1 |
| AWS Cost Explorer | E3 | AU1 | 2 | E1 |
| AWS Cost Explorer | E3 | I1 | 2 | E1 |
| AWS Cost Explorer | E3 | I2 | 2 | E1 |
| AWS Cost Explorer | E3 | O1 | 1 | E1 |
| AWS Cost Explorer | E3 | P2 | 1 | E1 |
| AWS Cost Explorer | E3 | V1 | 2 | E1 |
| AWS Cost Explorer | E5 | A1 | 2 | E1 |
| AWS Cost Explorer | E5 | A2 | 2 | E1 |
| AWS Cost Explorer | E5 | AD1 | 2 | E1 |
| AWS Cost Explorer | E5 | AU1 | 2 | E1 |
| AWS Cost Explorer | E5 | I1 | 2 | E1 |
| AWS Cost Explorer | E5 | I2 | 2 | E1 |
| AWS Cost Explorer | E5 | O1 | 1 | E1 |
| AWS Cost Explorer | E5 | P2 | 1 | E1 |
| AWS Cost Explorer | E5 | V1 | 2 | E1 |
| AWS Cost Explorer | E6 | A1 | 2 | E1 |
| AWS Cost Explorer | E6 | A2 | 2 | E1 |
| AWS Cost Explorer | E6 | AD1 | 2 | E1 |
| AWS Cost Explorer | E6 | AU1 | 2 | E1 |
| AWS Cost Explorer | E6 | I1 | 2 | E1 |
| AWS Cost Explorer | E6 | I2 | 2 | E1 |
| AWS Cost Explorer | E6 | O1 | 1 | E1 |
| AWS Cost Explorer | E6 | P2 | 1 | E1 |
| AWS Cost Explorer | E6 | V1 | 2 | E1 |
| AWS Cost Optimization Hub | E2 | A1 | 0 | E1 |
| AWS Cost Optimization Hub | E2 | A2 | 0 | E1 |
| AWS Cost Optimization Hub | E2 | AD1 | 2 | E1 |
| AWS Cost Optimization Hub | E2 | AU1 | 0 | E1 |
| AWS Cost Optimization Hub | E2 | I1 | 2 | E1 |
| AWS Cost Optimization Hub | E2 | I2 | 2 | E1 |
| AWS Cost Optimization Hub | E2 | O1 | 2 | E1 |
| AWS Cost Optimization Hub | E2 | P2 | 0 | E1 |
| AWS Cost Optimization Hub | E2 | V1 | 0 | E1 |
| AWS Cost Optimization Hub | E3 | A1 | 0 | E1 |
| AWS Cost Optimization Hub | E3 | A2 | 0 | E1 |
| AWS Cost Optimization Hub | E3 | AD1 | 2 | E1 |
| AWS Cost Optimization Hub | E3 | AU1 | 0 | E1 |
| AWS Cost Optimization Hub | E3 | I1 | 2 | E1 |
| AWS Cost Optimization Hub | E3 | I2 | 2 | E1 |
| AWS Cost Optimization Hub | E3 | O1 | 2 | E1 |
| AWS Cost Optimization Hub | E3 | P2 | 0 | E1 |
| AWS Cost Optimization Hub | E3 | V1 | 0 | E1 |
| AWS Cost Optimization Hub | E5 | A1 | 0 | E1 |
| AWS Cost Optimization Hub | E5 | A2 | 0 | E1 |
| AWS Cost Optimization Hub | E5 | AD1 | 2 | E1 |
| AWS Cost Optimization Hub | E5 | AU1 | 0 | E1 |
| AWS Cost Optimization Hub | E5 | I1 | 2 | E1 |
| AWS Cost Optimization Hub | E5 | I2 | 2 | E1 |
| AWS Cost Optimization Hub | E5 | O1 | 2 | E1 |
| AWS Cost Optimization Hub | E5 | P2 | 0 | E1 |
| AWS Cost Optimization Hub | E5 | V1 | 0 | E1 |
| AWS Cost Optimization Hub | E6 | A1 | 0 | E1 |
| AWS Cost Optimization Hub | E6 | A2 | 0 | E1 |
| AWS Cost Optimization Hub | E6 | AD1 | 2 | E1 |
| AWS Cost Optimization Hub | E6 | AU1 | 0 | E1 |
| AWS Cost Optimization Hub | E6 | I1 | 2 | E1 |
| AWS Cost Optimization Hub | E6 | I2 | 2 | E1 |
| AWS Cost Optimization Hub | E6 | O1 | 2 | E1 |
| AWS Cost Optimization Hub | E6 | P2 | 0 | E1 |
| AWS Cost Optimization Hub | E6 | V1 | 0 | E1 |
| Azure Cost Management | E2 | A1 | 2 | E1 |
| Azure Cost Management | E2 | A2 | 2 | E1 |
| Azure Cost Management | E2 | AD1 | 2 | E1 |
| Azure Cost Management | E2 | AU1 | 2 | E1 |
| Azure Cost Management | E2 | I1 | 2 | E1 |
| Azure Cost Management | E2 | I2 | 2 | E1 |
| Azure Cost Management | E2 | O1 | 2 | E1 |
| Azure Cost Management | E2 | P2 | 1 | E1 |
| Azure Cost Management | E2 | V1 | 2 | E1 |
| Azure Cost Management | E3 | A1 | 2 | E1 |
| Azure Cost Management | E3 | A2 | 2 | E1 |
| Azure Cost Management | E3 | AD1 | 2 | E1 |
| Azure Cost Management | E3 | AU1 | 2 | E1 |
| Azure Cost Management | E3 | I1 | 2 | E1 |
| Azure Cost Management | E3 | I2 | 2 | E1 |
| Azure Cost Management | E3 | O1 | 2 | E1 |
| Azure Cost Management | E3 | P2 | 1 | E1 |
| Azure Cost Management | E3 | V1 | 2 | E1 |
| Azure Cost Management | E5 | A1 | 2 | E1 |
| Azure Cost Management | E5 | A2 | 2 | E1 |
| Azure Cost Management | E5 | AD1 | 2 | E1 |
| Azure Cost Management | E5 | AU1 | 2 | E1 |
| Azure Cost Management | E5 | I1 | 2 | E1 |
| Azure Cost Management | E5 | I2 | 2 | E1 |
| Azure Cost Management | E5 | O1 | 2 | E1 |
| Azure Cost Management | E5 | P2 | 1 | E1 |
| Azure Cost Management | E5 | V1 | 2 | E1 |
| Azure Cost Management | E6 | A1 | 2 | E1 |
| Azure Cost Management | E6 | A2 | 2 | E1 |
| Azure Cost Management | E6 | AD1 | 2 | E1 |
| Azure Cost Management | E6 | AU1 | 2 | E1 |
| Azure Cost Management | E6 | I1 | 2 | E1 |
| Azure Cost Management | E6 | I2 | 2 | E1 |
| Azure Cost Management | E6 | O1 | 2 | E1 |
| Azure Cost Management | E6 | P2 | 1 | E1 |
| Azure Cost Management | E6 | V1 | 2 | E1 |
| Cast AI | E5 | A1 | 1 | E3 |
| Cast AI | E5 | AU1 | 2 | E3 |
| Cast AI | E5 | I1 | 2 | E3 |
| Cast AI | E5 | O1 | 2 | E3 |
| Cast AI | E5 | V1 | 2 | E3 |
| CloudHealth | E1 | A1 | 2 | E2 |
| CloudHealth | E1 | A2 | 2 | E2 |
| CloudHealth | E1 | AU1 | 2 | E2 |
| CloudHealth | E1 | I1 | 2 | E2 |
| CloudHealth | E1 | I2 | 1 | E2 |
| CloudHealth | E1 | O1 | 2 | E2 |
| CloudHealth | E1 | V1 | 2 | E2 |
| CloudHealth | E5 | A1 | 2 | E2 |
| CloudHealth | E5 | A2 | 2 | E2 |
| CloudHealth | E5 | AU1 | 2 | E2 |
| CloudHealth | E5 | I1 | 2 | E2 |
| CloudHealth | E5 | I2 | 1 | E2 |
| CloudHealth | E5 | O1 | 2 | E2 |
| CloudHealth | E5 | V1 | 2 | E2 |
| CloudHealth | E6 | A1 | 2 | E2 |
| CloudHealth | E6 | A2 | 2 | E2 |
| CloudHealth | E6 | AU1 | 2 | E2 |
| CloudHealth | E6 | I1 | 2 | E2 |
| CloudHealth | E6 | I2 | 1 | E2 |
| CloudHealth | E6 | O1 | 2 | E2 |
| CloudHealth | E6 | V1 | 2 | E2 |
| CloudZero | E1 | A1 | 2 | E2 |
| CloudZero | E1 | A2 | 2 | E2 |
| CloudZero | E1 | AD1 | 2 | E2 |
| CloudZero | E1 | AU1 | 0 | E2 |
| CloudZero | E1 | I1 | 2 | E2 |
| CloudZero | E1 | O1 | 2 | E2 |
| CloudZero | E1 | V1 | 2 | E2 |
| CloudZero | E3 | A1 | 2 | E2 |
| CloudZero | E3 | A2 | 2 | E2 |
| CloudZero | E3 | AD1 | 2 | E2 |
| CloudZero | E3 | AU1 | 0 | E2 |
| CloudZero | E3 | I1 | 2 | E2 |
| CloudZero | E3 | O1 | 2 | E2 |
| CloudZero | E3 | V1 | 2 | E2 |
| CloudZero | E5 | A1 | 2 | E2 |
| CloudZero | E5 | A2 | 2 | E2 |
| CloudZero | E5 | AD1 | 2 | E2 |
| CloudZero | E5 | AU1 | 0 | E2 |
| CloudZero | E5 | I1 | 2 | E2 |
| CloudZero | E5 | O1 | 2 | E2 |
| CloudZero | E5 | V1 | 2 | E2 |
| CloudZero | E6 | A1 | 2 | E2 |
| CloudZero | E6 | A2 | 2 | E2 |
| CloudZero | E6 | AD1 | 2 | E2 |
| CloudZero | E6 | AU1 | 0 | E2 |
| CloudZero | E6 | I1 | 2 | E2 |
| CloudZero | E6 | O1 | 2 | E2 |
| CloudZero | E6 | V1 | 2 | E2 |
| Cloudability | E1 | A1 | 1 | E2 |
| Cloudability | E1 | A2 | 1 | E2 |
| Cloudability | E1 | AD1 | 1 | E2 |
| Cloudability | E1 | I1 | 1 | E2 |
| Cloudability | E1 | I2 | 1 | E2 |
| Cloudability | E1 | O1 | 1 | E2 |
| Cloudability | E1 | V1 | 1 | E2 |
| Cloudability | E5 | A1 | 1 | E2 |
| Cloudability | E5 | A2 | 1 | E2 |
| Cloudability | E5 | AD1 | 1 | E2 |
| Cloudability | E5 | I1 | 1 | E2 |
| Cloudability | E5 | I2 | 1 | E2 |
| Cloudability | E5 | O1 | 1 | E2 |
| Cloudability | E5 | V1 | 1 | E2 |
| Cloudability | E6 | A1 | 1 | E2 |
| Cloudability | E6 | A2 | 1 | E2 |
| Cloudability | E6 | AD1 | 1 | E2 |
| Cloudability | E6 | I1 | 1 | E2 |
| Cloudability | E6 | I2 | 1 | E2 |
| Cloudability | E6 | O1 | 1 | E2 |
| Cloudability | E6 | V1 | 1 | E2 |
| Finout | E1 | A1 | 2 | E2 |
| Finout | E1 | A2 | 2 | E2 |
| Finout | E1 | AD1 | 2 | E2 |
| Finout | E1 | I1 | 2 | E2 |
| Finout | E1 | I2 | 1 | E2 |
| Finout | E1 | O1 | 2 | E2 |
| Finout | E1 | V1 | 2 | E2 |
| Finout | E5 | A1 | 2 | E2 |
| Finout | E5 | A2 | 2 | E2 |
| Finout | E5 | AD1 | 2 | E2 |
| Finout | E5 | I1 | 2 | E2 |
| Finout | E5 | I2 | 1 | E2 |
| Finout | E5 | O1 | 2 | E2 |
| Finout | E5 | V1 | 2 | E2 |
| Finout | E6 | A1 | 2 | E2 |
| Finout | E6 | A2 | 2 | E2 |
| Finout | E6 | AD1 | 2 | E2 |
| Finout | E6 | I1 | 2 | E2 |
| Finout | E6 | I2 | 1 | E2 |
| Finout | E6 | O1 | 2 | E2 |
| Finout | E6 | V1 | 2 | E2 |
| Google Cloud Billing | E2 | A1 | 1 | E1 |
| Google Cloud Billing | E2 | A2 | 0 | E1 |
| Google Cloud Billing | E2 | AD1 | 2 | E1 |
| Google Cloud Billing | E2 | AU1 | 2 | E1 |
| Google Cloud Billing | E2 | I1 | 2 | E1 |
| Google Cloud Billing | E2 | I2 | 2 | E1 |
| Google Cloud Billing | E2 | O1 | 0 | E1 |
| Google Cloud Billing | E2 | P2 | 1 | E1 |
| Google Cloud Billing | E2 | V1 | 2 | E1 |
| Google Cloud Billing | E3 | A1 | 1 | E1 |
| Google Cloud Billing | E3 | A2 | 0 | E1 |
| Google Cloud Billing | E3 | AD1 | 2 | E1 |
| Google Cloud Billing | E3 | AU1 | 2 | E1 |
| Google Cloud Billing | E3 | I1 | 2 | E1 |
| Google Cloud Billing | E3 | I2 | 2 | E1 |
| Google Cloud Billing | E3 | O1 | 0 | E1 |
| Google Cloud Billing | E3 | P2 | 1 | E1 |
| Google Cloud Billing | E3 | V1 | 2 | E1 |
| Google Cloud Billing | E5 | A1 | 1 | E1 |
| Google Cloud Billing | E5 | A2 | 0 | E1 |
| Google Cloud Billing | E5 | AD1 | 2 | E1 |
| Google Cloud Billing | E5 | AU1 | 2 | E1 |
| Google Cloud Billing | E5 | I1 | 2 | E1 |
| Google Cloud Billing | E5 | I2 | 2 | E1 |
| Google Cloud Billing | E5 | O1 | 0 | E1 |
| Google Cloud Billing | E5 | P2 | 1 | E1 |
| Google Cloud Billing | E5 | V1 | 2 | E1 |
| Google Cloud Billing | E6 | A1 | 1 | E1 |
| Google Cloud Billing | E6 | A2 | 0 | E1 |
| Google Cloud Billing | E6 | AD1 | 2 | E1 |
| Google Cloud Billing | E6 | AU1 | 2 | E1 |
| Google Cloud Billing | E6 | I1 | 2 | E1 |
| Google Cloud Billing | E6 | I2 | 2 | E1 |
| Google Cloud Billing | E6 | O1 | 0 | E1 |
| Google Cloud Billing | E6 | P2 | 1 | E1 |
| Google Cloud Billing | E6 | V1 | 2 | E1 |
| Google Cloud FinOps Hub | E2 | A1 | 0 | E1 |
| Google Cloud FinOps Hub | E2 | A2 | 0 | E1 |
| Google Cloud FinOps Hub | E2 | AD1 | 1 | E1 |
| Google Cloud FinOps Hub | E2 | AU1 | 1 | E1 |
| Google Cloud FinOps Hub | E2 | I1 | 2 | E1 |
| Google Cloud FinOps Hub | E2 | I2 | 1 | E1 |
| Google Cloud FinOps Hub | E2 | O1 | 2 | E1 |
| Google Cloud FinOps Hub | E2 | P2 | 0 | E1 |
| Google Cloud FinOps Hub | E2 | V1 | 0 | E1 |
| Google Cloud FinOps Hub | E3 | A1 | 0 | E1 |
| Google Cloud FinOps Hub | E3 | A2 | 0 | E1 |
| Google Cloud FinOps Hub | E3 | AD1 | 1 | E1 |
| Google Cloud FinOps Hub | E3 | AU1 | 1 | E1 |
| Google Cloud FinOps Hub | E3 | I1 | 2 | E1 |
| Google Cloud FinOps Hub | E3 | I2 | 1 | E1 |
| Google Cloud FinOps Hub | E3 | O1 | 2 | E1 |
| Google Cloud FinOps Hub | E3 | P2 | 0 | E1 |
| Google Cloud FinOps Hub | E3 | V1 | 0 | E1 |
| Google Cloud FinOps Hub | E5 | A1 | 0 | E1 |
| Google Cloud FinOps Hub | E5 | A2 | 0 | E1 |
| Google Cloud FinOps Hub | E5 | AD1 | 1 | E1 |
| Google Cloud FinOps Hub | E5 | AU1 | 1 | E1 |
| Google Cloud FinOps Hub | E5 | I1 | 2 | E1 |
| Google Cloud FinOps Hub | E5 | I2 | 1 | E1 |
| Google Cloud FinOps Hub | E5 | O1 | 2 | E1 |
| Google Cloud FinOps Hub | E5 | P2 | 0 | E1 |
| Google Cloud FinOps Hub | E5 | V1 | 0 | E1 |
| Google Cloud FinOps Hub | E6 | A1 | 0 | E1 |
| Google Cloud FinOps Hub | E6 | A2 | 0 | E1 |
| Google Cloud FinOps Hub | E6 | AD1 | 1 | E1 |
| Google Cloud FinOps Hub | E6 | AU1 | 1 | E1 |
| Google Cloud FinOps Hub | E6 | I1 | 2 | E1 |
| Google Cloud FinOps Hub | E6 | I2 | 1 | E1 |
| Google Cloud FinOps Hub | E6 | O1 | 2 | E1 |
| Google Cloud FinOps Hub | E6 | P2 | 0 | E1 |
| Google Cloud FinOps Hub | E6 | V1 | 0 | E1 |
| Kubecost | E5 | A1 | 2 | E3 |
| Kubecost | E5 | A2 | 1 | E3 |
| Kubecost | E5 | I1 | 2 | E3 |
| Kubecost | E5 | I2 | 2 | E3 |
| Kubecost | E5 | O1 | 2 | E3 |
| Kubecost | E5 | V1 | 2 | E3 |
| OpenCost | E5 | A1 | 2 | E3 |
| OpenCost | E5 | A2 | 1 | E3 |
| OpenCost | E5 | AU1 | 0 | E3 |
| OpenCost | E5 | I1 | 2 | E3 |
| OpenCost | E5 | I2 | 2 | E3 |
| OpenCost | E5 | O1 | 1 | E3 |
| OpenCost | E5 | V1 | 2 | E3 |
| StormForge | E5 | AU1 | 2 | E3 |
| StormForge | E5 | I1 | 1 | E3 |
| StormForge | E5 | I2 | 1 | E3 |
| StormForge | E5 | O1 | 2 | E3 |
| Vantage | E1 | A1 | 2 | E2 |
| Vantage | E1 | AD1 | 2 | E2 |
| Vantage | E1 | AU1 | 2 | E2 |
| Vantage | E1 | I1 | 2 | E2 |
| Vantage | E1 | I2 | 2 | E2 |
| Vantage | E1 | O1 | 2 | E2 |
| Vantage | E1 | V1 | 2 | E2 |
| Vantage | E5 | A1 | 2 | E2 |
| Vantage | E5 | AD1 | 2 | E2 |
| Vantage | E5 | AU1 | 2 | E2 |
| Vantage | E5 | I1 | 2 | E2 |
| Vantage | E5 | I2 | 2 | E2 |
| Vantage | E5 | O1 | 2 | E2 |
| Vantage | E5 | V1 | 2 | E2 |
| Vantage | E6 | A1 | 2 | E2 |
| Vantage | E6 | AD1 | 2 | E2 |
| Vantage | E6 | AU1 | 2 | E2 |
| Vantage | E6 | I1 | 2 | E2 |
| Vantage | E6 | I2 | 2 | E2 |
| Vantage | E6 | O1 | 2 | E2 |
| Vantage | E6 | V1 | 2 | E2 |
| nOps | E1 | A1 | 2 | E2 |
| nOps | E1 | A2 | 2 | E2 |
| nOps | E1 | AD1 | 2 | E2 |
| nOps | E1 | AU1 | 2 | E2 |
| nOps | E1 | I1 | 2 | E2 |
| nOps | E1 | O1 | 2 | E2 |
| nOps | E1 | P2 | 1 | E2 |
| nOps | E1 | V1 | 2 | E2 |
| nOps | E5 | A1 | 2 | E2 |
| nOps | E5 | A2 | 2 | E2 |
| nOps | E5 | AD1 | 2 | E2 |
| nOps | E5 | AU1 | 2 | E2 |
| nOps | E5 | I1 | 2 | E2 |
| nOps | E5 | O1 | 2 | E2 |
| nOps | E5 | P2 | 1 | E2 |
| nOps | E5 | V1 | 2 | E2 |
| nOps | E6 | A1 | 2 | E2 |
| nOps | E6 | A2 | 2 | E2 |
| nOps | E6 | AD1 | 2 | E2 |
| nOps | E6 | AU1 | 2 | E2 |
| nOps | E6 | I1 | 2 | E2 |
| nOps | E6 | O1 | 2 | E2 |
| nOps | E6 | P2 | 1 | E2 |
| nOps | E6 | V1 | 2 | E2 |

## Efecto en los resultados

| Escenario | Producto | S base antes | S base después | Cobertura antes | Cobertura después |
|---|---|---:|---:|---:|---:|
| E2 | AWS Cost Explorer | 51.85 | Insuf. | 100.0% | 22.2% |
| E3 | AWS Cost Explorer | 51.85 | Insuf. | 100.0% | 22.2% |
| E5 | AWS Cost Explorer | 51.85 | Insuf. | 100.0% | 22.2% |
| E6 | AWS Cost Explorer | 51.85 | Insuf. | 100.0% | 22.2% |
| E2 | AWS Cost Optimization Hub | 19.05 | Insuf. | 77.8% | 11.1% |
| E3 | AWS Cost Optimization Hub | 19.05 | Insuf. | 77.8% | 11.1% |
| E5 | AWS Cost Optimization Hub | 19.05 | Insuf. | 77.8% | 11.1% |
| E6 | AWS Cost Optimization Hub | 19.05 | Insuf. | 77.8% | 11.1% |
| E2 | Azure Cost Management | 51.85 | Insuf. | 100.0% | 22.2% |
| E3 | Azure Cost Management | 51.85 | Insuf. | 100.0% | 22.2% |
| E5 | Azure Cost Management | 51.85 | Insuf. | 100.0% | 22.2% |
| E6 | Azure Cost Management | 51.85 | Insuf. | 100.0% | 22.2% |
| E2 | Google Cloud Billing | 38.89 | Insuf. | 100.0% | 22.2% |
| E3 | Google Cloud Billing | 38.89 | Insuf. | 100.0% | 22.2% |
| E5 | Google Cloud Billing | 38.89 | Insuf. | 100.0% | 22.2% |
| E6 | Google Cloud Billing | 38.89 | Insuf. | 100.0% | 22.2% |
| E2 | Google Cloud FinOps Hub | 23.81 | Insuf. | 77.8% | 11.1% |
| E3 | Google Cloud FinOps Hub | 23.81 | Insuf. | 77.8% | 11.1% |
| E5 | Google Cloud FinOps Hub | 23.81 | Insuf. | 77.8% | 11.1% |
| E6 | Google Cloud FinOps Hub | 23.81 | Insuf. | 77.8% | 11.1% |
| E1 | Cloudability | Insuf. | Insuf. | 44.4% | 0.0% |
| E5 | Cloudability | Insuf. | Insuf. | 44.4% | 0.0% |
| E6 | Cloudability | Insuf. | Insuf. | 44.4% | 0.0% |
| E1 | CloudHealth | Insuf. | Insuf. | 66.7% | 11.1% |
| E5 | CloudHealth | Insuf. | Insuf. | 66.7% | 11.1% |
| E6 | CloudHealth | Insuf. | Insuf. | 66.7% | 11.1% |
| E1 | CloudZero | Insuf. | Insuf. | 44.4% | 11.1% |
| E3 | CloudZero | Insuf. | Insuf. | 44.4% | 11.1% |
| E5 | CloudZero | Insuf. | Insuf. | 44.4% | 11.1% |
| E6 | CloudZero | Insuf. | Insuf. | 44.4% | 11.1% |
| E1 | Vantage | Insuf. | Insuf. | 33.3% | 0.0% |
| E5 | Vantage | Insuf. | Insuf. | 33.3% | 0.0% |
| E6 | Vantage | Insuf. | Insuf. | 33.3% | 0.0% |
| E1 | Finout | Insuf. | Insuf. | 44.4% | 11.1% |
| E5 | Finout | Insuf. | Insuf. | 44.4% | 11.1% |
| E6 | Finout | Insuf. | Insuf. | 44.4% | 11.1% |
| E1 | nOps | 59.52 | Insuf. | 77.8% | 11.1% |
| E5 | nOps | 59.52 | Insuf. | 77.8% | 11.1% |
| E6 | nOps | 59.52 | Insuf. | 77.8% | 11.1% |
| E5 | OpenCost | 33.33 | Insuf. | 77.8% | 22.2% |
| E5 | Kubecost | Insuf. | Insuf. | 55.6% | 11.1% |
| E5 | Cast AI | Insuf. | Insuf. | 33.3% | 11.1% |
| E5 | StormForge | Insuf. | Insuf. | 33.3% | 0.0% |

## Lectura de este resultado

Quedan 10 de 61 pares con puntaje calculable. No es una pérdida de trabajo: es la medida real de lo investigado. La evidencia recogida sostiene una evaluación por producto en su escenario de origen, y esta pasada deja de presentar como 61 evaluaciones lo que son 17.

El trabajo pendiente queda cuantificado: 338 celdas por investigar con evidencia propia del escenario. Cada una necesita documentación oficial que responda la pregunta observable del indicador **para las entradas y salidas de ese escenario**, no para el producto en general.
