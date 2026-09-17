# FP-180 — IBM Cloud Cost Estimator evaluado en E4

> Generado por `apply_ibm_e4.py` el 2026-09-16. Queda a validacion humana.

## Por que

FP-177 §4 admite herramientas nativas en E4 «cuando soporten estimacion previa». IBM Cloud Cost Estimator es exactamente eso, y toda la evidencia recogida para el producto describe estimacion antes del despliegue.

Estaba presente solo en E1, E2, E3, E5 y E6 por pertenecer a la categoria nativa, y no puntuaba en ninguno. Sus ceros en Visibilidad y Asignacion son correctos —una calculadora no desglosa gasto real— pero lo median contra un escenario que no es el suyo.

**El producto no se reclasifica**: sigue siendo cloud nativa, y ahora tambien se evalua donde FP-177 lo admite. Eso resuelve la tension registrada en `alternativas-adicionales.md` sin tocar la poblacion acordada.

## Resultado

**S linea base 38.89 (Basic), cobertura 75.0%.**

Criterios criticos de E4: cumple Precio e Integracion.

## Estado de E4 tras esta pasada

| Producto | S linea base | Banda | Cobertura |
|---|---:|---|---:|
| Infracost | 47.22 | Basic | 75.0% |
| IBM Cloud Cost Estimator | 38.89 | Basic | 75.0% |
| AWS Pricing Calculator | 35.71 | Basic | 87.5% |
| Azure Pricing Calculator | 30.56 | Basic | 75.0% |
| Cloud Custodian | 19.05 | Basic | 77.8% |

Con esta incorporacion, E4 permite comparar entre si las tres calculadoras nativas de estimacion previa —AWS, Azure e IBM— en el escenario que les corresponde.
