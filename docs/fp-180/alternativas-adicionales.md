# FP-180 — Alternativas adicionales incorporadas

> Generado por `add_alternatives.py` el 2026-09-16. Evidencia verificada contra documentación oficial. Queda a validación humana.

## Por qué

El criterio de término de FP-51 no pide registrar las alternativas, pide compararlas: «Las alternativas son comparadas bajo el mismo escenario». FP-126 las registró y FP-179 las auditó, pero la matriz nunca las puntuó. Esta pasada incorpora las ocho bajo la misma metodología que el resto de la población.

## Resultado por alternativa

| Alternativa | Categoría | Escenario ancla | Cobertura | Resultado |
|---|---|---|---:|---|
| OCI Cost Analysis | Cloud nativa | E1 | 55.6% | Insufficient evidence |
| IBM Cloud Cost Estimator | Cloud nativa | E1 | 66.7% | Insufficient evidence |
| Harness Cloud Cost Management | Multicloud | E2 | 11.1% | Insufficient evidence |
| Densify | Multicloud | E2 | 33.3% | Insufficient evidence |
| PerfectScale | Kubernetes | E3 | 22.2% | Insufficient evidence |
| ScaleOps | Kubernetes | E3 | 22.2% | Insufficient evidence |
| AWS Pricing Calculator | Estimacion temprana | E4 | 62.5% | Insufficient evidence |
| Azure Pricing Calculator | Estimacion temprana | E4 | 50.0% | Insufficient evidence |

Ninguna alcanza el 70% de cobertura con la investigación de esta pasada, que consistió en una o dos consultas de documentación oficial por producto. Dos quedan a una sola celda del umbral: IBM Cloud Cost Estimator necesita O2 y AWS Pricing Calculator necesita D2.

## Reglas aplicadas

- Ninguna celda queda en blanco: lo que no se encontró en fuentes oficiales o aprobadas del proyecto se registra como `NE` con su motivo.
- La evidencia exclusivamente comercial limita el indicador a 1, según FP-177 §2.1.
- Ningún indicador alcanza 3: eso exige doble evidencia y esta pasada dispone solo de documentación primaria.
- Los indicadores dependientes del escenario se puntúan solo en el escenario ancla del producto; en los demás quedan `NE` a la espera de evidencia propia.

## Observaciones para el equipo

**IBM Cloud Cost Estimator**

Tension de clasificacion registrada para el equipo: FP-126 y FP-179 lo situan entre las herramientas nativas, cuya categoria ancla en E1 (visibilidad y asignacion en nube unica), pero su funcion documentada es la estimacion previa al despliegue. Sus indicadores de visibilidad y asignacion se puntuan 0 por ausencia verificada, no por deficiencia del producto. Se sugiere revisar si corresponde reubicarlo en estimacion temprana, igual que la tension ya registrada para Cloud Custodian.

**Densify**

Reserva de FP-179 confirmada: la auditoria de alternativas advirtio que Densify no queda validado como plataforma FinOps multinube. La documentacion revisada en esta pasada lo confirma: el producto se presenta como Kubex, «full-stack AI-driven K8s resource optimization, from container to node to scale group», es decir optimizacion de recursos de Kubernetes y no gestion financiera multinube. Sus indicadores de visibilidad, asignacion y multinube se puntuan 0 por ausencia verificada frente al alcance de E2. Se mantiene en la poblacion por decision de la matriz final de FP-126, y su inclusion no valida la capacidad de la categoria.

**ScaleOps**

Limite de evidencia registrado: FP-179 ya advirtio que la evidencia de ScaleOps es una declaracion del proveedor. En esta pasada no se localizo documentacion tecnica oficial indexada fuera del sitio comercial, por lo que, aplicando FP-177 seccion 2.1 («si un indicador cuenta solo con evidencia comercial, su puntaje maximo es 1»), ningun indicador de ScaleOps supera el valor 1. Si el equipo accede a documentacion tecnica del producto, estos valores deben revisarse.
