# FP-180 — Primera pasada de investigación: escenario E2

> Generado por `apply_e2_research.py` el 2026-09-16. Evidencia verificada contra documentación oficial de cada producto. Queda a validación humana.

## Por qué E2 primero

E2 —consolidación multinube y comparación de precios— es el escenario donde comparar plataformas es el aporte central de FP-51, y tenía **un solo par puntuado** (nOps). El análisis de cobertura mostró que era también el más barato de desbloquear: cuatro plataformas necesitaban entre una y cuatro celdas para cruzar el umbral del 70%.

## Regla de alcance aplicada al escribir cada valor

Los indicadores independientes del escenario (V2, O2, AU2, M1, M2, AD2, P1, D1, D2 — propiedades del producto) se escriben en todos los escenarios del producto, porque una sola investigación los sostiene. Los dependientes del escenario (V1, A1, A2, O1, AU1, I1, I2, AD1) se escriben solo en E2, porque la evidencia se leyó contra las entradas y salidas de E2.

## Celdas completadas (10 únicas, 33 filas)

| Producto | Indicador | Valor | Fuente |
|---|---|---:|---|
| CloudHealth | AD1 | 2 | https://techdocs.broadcom.com/us/en/vmware-tanzu/cloudhealth/tanzu-cloudhealth/saas/tnz-cloudhealth/using-and-managing-tanzu-cloudhealth-managing-classic-organizations-if-applicable.html |
| CloudZero | V2 | 2 | https://docs.cloudzero.com/docs/costformation-allocating-shared-costs |
| CloudZero | AD2 | 2 | https://docs.cloudzero.com/docs/cloudzero |
| CloudZero | I2 | 2 | https://docs.cloudzero.com/docs/integrations |
| Vantage | V2 | 2 | https://docs.vantage.sh/cost_reports |
| Vantage | M2 | 2 | https://docs.vantage.sh/usage_based_reporting |
| Vantage | AD2 | 2 | https://docs.vantage.sh/vantage_university |
| Vantage | A2 | 2 | https://docs.vantage.sh/vantage_university_cost_allocation |
| Finout | V2 | 2 | https://docs.finout.io/user-guide/inform/megabill |
| Finout | AD2 | 2 | https://docs.finout.io/user-guide/operate/tag-governance |

## Celdas que no se pudieron completar

| Producto | Indicador | Motivo |
|---|---|---|
| Finout | D2 | No se encontró documentación oficial que describa dependencias propietarias ni un camino de salida o configuración reversible. La documentación de API cubre el acceso programático al dato (D1), no la reversibilidad del acoplamiento. Se mantiene NE. |
| Finout | AU1 | La documentación oficial de CostGuard describe generación de recomendaciones y permisos de gestión, pero no describe ejecución ni bloqueo de acciones de costo. Como la ausencia no está afirmada explícitamente, corresponde NE y no 0. Ruta alternativa evaluada para desbloquear Finout; tampoco se pudo cerrar con evidencia disponible. |

## Efecto en los resultados

| Escenario | Producto | Antes | Después | Cobertura antes | Cobertura después |
|---|---|---|---|---:|---:|
| E2 | CloudHealth | Insufficient evidence | 54.76 (Solid) | 66.7% | 77.8% |
| E2 | CloudZero | Insufficient evidence | 57.14 (Solid) | 44.4% | 77.8% |
| E1 | Vantage | Insufficient evidence | Insufficient evidence | 0.0% | 11.1% |
| E2 | Vantage | Insufficient evidence | 66.67 (Solid) | 33.3% | 77.8% |
| E5 | Vantage | Insufficient evidence | Insufficient evidence | 0.0% | 11.1% |
| E6 | Vantage | Insufficient evidence | Insufficient evidence | 0.0% | 11.1% |
| E2 | Finout | Insufficient evidence | Insufficient evidence | 44.4% | 66.7% |

## Nota sobre Finout

Finout recibió dos de las tres celdas que necesitaba (V2 y AD2), pero **sigue por debajo del umbral**. Su tercer criterio más barato era Dependencia, y no existe documentación oficial de dependencias propietarias ni de camino de salida; la ruta alternativa (Automatización, vía CostGuard) tampoco se pudo cerrar, porque la documentación no describe ejecución ni bloqueo de acciones. Ninguna de las dos se rellenó con un valor inventado.

Tras esta pasada, E2 tiene 4 pares puntuados.
