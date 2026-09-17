# FP-180 — Criterio Precio de E2 completado

> Generado por `apply_e2_price.py` el 2026-09-16. Evidencia verificada contra documentacion oficial. Queda a validacion humana.

## Por que

Precio es uno de los dos criterios criticos de E2 y estaba sin evidenciar en CloudHealth, CloudZero y Vantage: solo nOps lo tenia medido. Eso producia la distorsion que esta matriz busca evitar — Vantage superaba a nOps siendo que nOps era el unico medido en el criterio donde saco su nota mas baja.

Conviene recordar que P1 y P2 **no miden cuanto cuesta la herramienta**. P1 pregunta si expone precio, moneda, region, unidad, periodo y supuestos de los costos que reporta; P2, si permite estimar o comparar componentes sin ocultar los limites de la equivalencia. El precio de adquisicion de cada herramienta es un artefacto distinto: la matriz de precios de FP-126.

## Celdas completadas (6 unicas, 16 filas)

| Producto | Indicador | Valor | Fuente |
|---|---|---:|---|
| CloudHealth | P1 | 2 | https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/tnz-cloudhealth/working-with-reports-and-recommendation-of-tanzu-cloudhealth-cost-reports.html |
| CloudHealth | P2 | 2 | https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/cloudhealth/saas/index/working-with-reports-and-recommendation-of-tanzu-cloudhealth-working-with-reports-recommendations/working-with-reports-and-recommendation-of-tanzu-cloudhealth-aws-rightsizing-new.html |
| CloudZero | P1 | 2 | https://docs.cloudzero.com/docs/cost-types |
| CloudZero | P2 | 2 | https://docs.cloudzero.com/docs/cost-types |
| Vantage | P1 | 2 | https://docs.vantage.sh/data_dictionary |
| Vantage | P2 | 2 | https://docs.vantage.sh/cost_recommendations |

## Efecto en los resultados

| Escenario | Producto | Antes | Despues | Cobertura antes | Cobertura despues |
|---|---|---|---|---:|---:|
| E2 | CloudHealth | 54.76 (Solid) | 56.25 (Solid) | 77.8% | 88.9% |
| E2 | CloudZero | 57.14 (Solid) | 58.33 (Solid) | 77.8% | 88.9% |
| E2 | Vantage | 66.67 (Solid) | 66.67 (Solid) | 77.8% | 88.9% |
