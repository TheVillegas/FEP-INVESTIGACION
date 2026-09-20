# FP-180 — Solicitud de ratificación para Pablo Andrés Silva Reinoso

## Propósito y alcance

Registrar la ratificación de las cuatro reglas metodológicas ya aplicadas a la matriz FP-180. Esta solicitud **no aprueba automáticamente las recomendaciones de FP-181**: esas recomendaciones siguen requiriendo elaboración y revisión del grupo.

Son decisiones que requieren ratificación las decisiones 1–4. Son consecuencias informativas o aplicaciones ya derivadas: el retiro del escenario ancla, la incorporación de IBM Cloud Cost Estimator en E4, los resultados medidos y la limitación de población FP-126 frente a FP-51/FP-177.

| Decisión | Regla aplicada | Efecto medido | Consecuencia si se rechaza |
|---|---|---|---|
| 1 — Crítico sin evidencia | Un criterio crítico aplicable sin evidencia retira banda y recomendación; conserva puntaje. | E6: Azure Cost Management (47,62) y Google Cloud Billing (30,95) quedan sin banda; Vantage y AWS Cost Explorer permanecen recomendables. | Recalcular bandas y recomendaciones de E6; no tratar `NE` como valor. |
| 2 — Productos separados | Cada producto se evalúa individualmente; una función que no cumple recibe `0`, aunque otro producto del proveedor la cumpla. | AWS Cost Optimization Hub: 66,67/Solid → 19,05/Basic. | Reagrupar productos y recalcular población y puntajes. |
| 3 — Subsunción declarada | Evidencia de un escenario más exigente puede sostener uno menos exigente solo con argumento explícito en la celda. | Sostiene la mayor parte de los pares poblados. | Las celdas subsumidas vuelven a `NE`; baja cobertura y resultados. |
| 4 — Evidencia propia | E1-A1, E2-P1/P2, E5-A2 y E6-V1/I1 requieren evidencia propia del escenario. | E6 deja sin evidencia propia los críticos de Azure y Google Cloud Billing; aplica la decisión 1. | Recalcular esas celdas; se pierde la separación semántica de escenarios. |

## Respuestas de ratificación

1. **¿Apruebas la Decisión 1: que un criterio crítico aplicable sin evidencia retire la banda comparativa y la recomendación, conservando el puntaje? Sí/No.**
   Respuesta: ________  Fecha: ________  Observaciones: ________________________________________

2. **¿Apruebas la Decisión 2: que los productos se evalúen individualmente, aunque pertenezcan al mismo proveedor, puntuando `0` las funciones que el producto evaluado no cumple? Sí/No.**
   Respuesta: ________  Fecha: ________  Observaciones: ________________________________________

3. **¿Apruebas la Decisión 3: que evidencia de un escenario más exigente pueda subsumir uno menos exigente únicamente cuando el argumento de inclusión quede registrado en la celda? Sí/No.**
   Respuesta: ________  Fecha: ________  Observaciones: ________________________________________

4. **¿Apruebas la Decisión 4: que E1-A1, E2-P1/P2, E5-A2 y E6-V1/I1 requieran evidencia propia del escenario? Sí/No.**
   Respuesta: ________  Fecha: ________  Observaciones: ________________________________________

5. **¿Confirmas que el escenario ancla queda retirado y no debe usarse para interpretar la matriz vigente? Sí/No.**
   Respuesta: ________  Fecha: ________  Observaciones: ________________________________________

6. **¿Confirmas que IBM Cloud Cost Estimator permanece clasificado como herramienta cloud nativa y se evalúa también en E4, con 38,89, banda Basic y 75% de cobertura? Sí/No.**
   Respuesta: ________  Fecha: ________  Observaciones: ________________________________________

7. **¿Aceptas que la diferencia de población entre FP-126 (tres nativas) y FP-51/FP-177 (cinco nativas) se declare como limitación, sin alterar la población comparativa vigente? Sí/No.**
   Respuesta: ________  Fecha: ________  Observaciones: ________________________________________

## Evidencia auditada

- `docs/fp-180/propuesta-metodologica-fp-180.md`, «Decisión 1» a «Decisión 4», «Aplicación de la condición de elegibilidad de E4» y «Registro de decisiones».
- `docs/fp-180/ibm-cost-estimator-e4.md`, «Por que» y «Resultado».
- `docs/fp-177/escenarios-uso-y-poblacion-evaluada-borrador.md`, §§1–2 y §4 (en particular E4).
- `FP-48 TINV02/TINV_Matriz_de_Fuentes_FP-126_actualizada_2026-09-15.xlsx`, población de herramientas nativas; la divergencia se documenta en `docs/fp-180/propuesta-metodologica-fp-180.md`, «Decisión 2 — Inconsistencia que obliga a declarar».
- `docs/fp-180/estado-matriz-comparativa.md`, §§8–10 y §12.
- `docs/fp-181/analisis-y-recomendaciones.md`, §§4, 6 y 7.

## Mensaje listo para enviar

Pablo, solicitamos tu ratificación de las cuatro decisiones metodológicas ya aplicadas a FP-180. El escenario ancla fue retirado; IBM Cloud Cost Estimator se evalúa también en E4 por la elegibilidad de FP-177 §4 (38,89, Basic, 75% de cobertura); y la diferencia FP-126 versus FP-51/FP-177 se declarará como limitación. Por favor responde Sí/No a los siete puntos de este documento. Esta ratificación no aprueba automáticamente las recomendaciones de FP-181.

## Actualizaciones posteriores a la aprobación

- Registrar nombre, respuestas, fecha y observaciones en este documento y en el registro de ratificación de `propuesta-metodologica-fp-180.md`.
- Marcar como ratificadas las decisiones 1–4 en `estado-matriz-comparativa.md` y actualizar las referencias pendientes de FP-181.
- Mantener en FP-181 la revisión humana separada de sus recomendaciones y la limitación FP-126 frente a FP-51/FP-177.
- Corregir **después de la ratificación**, sin resolverlo silenciosamente ahora, la inconsistencia descubierta en `estado-matriz-comparativa.md`: el encabezado declara 30 pares con puntaje de 85, mientras §10 declara el estado vigente de 31 pares con puntaje de 86.
