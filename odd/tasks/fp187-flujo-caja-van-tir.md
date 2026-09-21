# FP-187 — Flujo de caja, VAN y TIR

## Objective
Traducir el TCO base y el escenario optimizado de FP-183/FP-184 a un flujo de caja mensual de 60 meses y calcular VAN/TIR de forma reproducible.

## Problem
FP-52 exige demostrar el efecto económico de FinOps sobre la propuesta, pero FP-187 aún no tiene un modelo financiero que separe inversión inicial, costos recurrentes, ahorros y supuestos financieros.

## Why
Completar la evaluación económica de TINV-06 sin duplicar el TCO ni ocultar supuestos pendientes.

## Scope
- Crear docs/fp-187/flujo-caja-van-tir-fp-187.xlsx.
- Modelar escenarios base y optimizado para Chile Central y East US.
- Usar 60 meses, moneda USD y los totales conciliados con FP-183/FP-184.
- Exponer tasa de descuento, inversión inicial, costos operativos y costos de implementación como parámetros.
- Calcular flujo neto acumulado, VAN y TIR con fórmulas reproducibles.
- Añadir trazabilidad a FP-183, FP-184, papers FP-48 y fuentes oficiales.
- Crear docs/fp-187/trazabilidad-fp187.md.

## Constraints
- No presentar horas, tarifas, costos de implementación ni tasa financiera como datos internos reales cuando no existen: usar proxies públicos y estimaciones de ingeniería visibles, trazables y reemplazables.
- No duplicar costos ya incluidos en FP-183.
- Separar gasto cloud, ahorro bruto y flujo neto.
- El workbook debe poder recalcularse modificando los supuestos.
- No modificar FP-183 ni FP-184.
- No convertir una ausencia de medición o aprobación humana en una validación positiva.

## Authorized scope
- Crear workbook y trazabilidad de FP-187.
- Ejecutar verificaciones locales del workbook.
- Actualizar Jira FP-187 con el resultado y sus limitaciones.
- No cerrar FP-187 como Done sin validación humana de supuestos financieros.

## Acceptance criteria
- [x] Flujo mensual de 60 meses para ambos escenarios y regiones.
- [x] VAN bruto calculado desde el ahorro mensual; VAN/TIR incremental quedan condicionados a inversión inicial validada, sin duplicar TCO.
- [x] Supuestos de tasa, inversión inicial, costos operativos e implementación visibles.
- [x] Totales base concilian con FP-183 y ahorros con FP-184.
- [x] Hoja Auditoría sin errores de fórmula.
- [x] Trazabilidad y limitaciones documentadas.
- [x] Jira FP-187 actualizado con comentario 10590; el issue permanece abierto para validación humana.
- [x] Los inputs pendientes se completan con proxies públicos verificables y una estimación de esfuerzo desglosada, claramente marcada como provisional.
- [x] El VAN/TIR incremental descuenta implementación y operación FinOps incremental, y mantiene inversión inicial separada para evitar doble conteo.

## Applicable checks
- Verificar fórmulas con @oai/artifact-tool.
- Comprobar ausencia de errores de fórmula.
- Reconciliar 60 meses y totales regionales mediante Python/bundled runtime.
- Inspección visual del resumen y supuestos.

## Progress
- [x] F187-01 Diseñar workbook y supuestos.
- [x] F187-02 Autorizar operación de artefacto y construir workbook.
- [x] F187-03 Verificar cálculos y visualización. Evidencia vigente: `verify_fp187.mjs` reporta `errors: []`; base Chile 23,256.321466, East US 16,474.602675; ahorros FP-184 Chile 1,453.152, East US 936.48; VAN bruto con tasa proxy 5.5%: 1,272.06 y 819.77; inspección visual de las seis hojas sin defectos materiales.
- [x] F187-04 Documentar trazabilidad y actualizar Jira. Trazabilidad creada y comentario 10590 registrado en FP-187; no se hizo transición a Done.
- [x] F187-05 Incorporar proxies públicos para tasa, mano de obra y tipo de cambio; documentar horas de implementación/operación y recalcular VAN/TIR neto. Evidencia: MDSF 5.5%, INE CLP 1,483,153/mes, DT 42 h/semana, BCCh CLP 954.85/USD; tarifa proxy USD 8.5345/h; implementación 50 h (USD 426.73) y operación 1 h/mes. VAN neto: Chile USD 397.07, East US -USD 55.21; TIR anual: 43.91% y -0.21%; `errors: []` y controles de Auditoría OK/PROVISIONAL.
- [x] F187-06 Auditar los 17 registros pendientes contra los artefactos actuales y documentar cuáles tienen evidencia suficiente, cuáles son exclusiones de alcance y cuáles todavía requieren medición o aprobación humana. Evidencia: `docs/fp-188/auditoria-validaciones-pendientes.md`; resultado 0 cerrados y 17 pendientes porque no existen mediciones, datos internos o aprobaciones formales en el repositorio.
- [x] F187-07 Incorporar al workbook el PRI descontado reproducible por región mediante flujo descontado acumulado y exponer el resultado en Resumen y Auditoría. Evidencia: `Resumen!K5:K6`, `Flujo mensual!X7:AA67` y `Auditoría!A14:E15`; Chile mes 30, East US no recupera en 60 meses; controles `OK`, sin errores de fórmula. Prueba en copia: elevar `Supuestos!B35` de 8 h a 80 h cambia Chile a no recupera, confirmando recalculación dinámica.
- [x] F187-08 Sincronizar la trazabilidad, la matriz consolidada y la recomendación FP-188 con el resultado verificado, sin presentar proxies como datos internos aprobados. Evidencia: trazabilidad FP-187, matriz consolidada con auditoría al 21-09-2026, checklist FP-188, sección 05 LaTeX y PDF completo actualizados.

## Next step
El cálculo del PRI y la auditoría documental están completados. Mantener la etiqueta provisional y los 17 registros pendientes hasta que los responsables entreguen datos internos, mediciones o aprobaciones formales; después recalcular FP-183 a FP-188 y revisar la recomendación.
