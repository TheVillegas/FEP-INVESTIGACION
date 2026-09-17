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
- No inventar horas, tarifas, costos de implementación ni tasa financiera: usar parámetros visibles con valores provisionales y marcar validación humana.
- No duplicar costos ya incluidos en FP-183.
- Separar gasto cloud, ahorro bruto y flujo neto.
- El workbook debe poder recalcularse modificando los supuestos.
- No modificar FP-183 ni FP-184.

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

## Applicable checks
- Verificar fórmulas con @oai/artifact-tool.
- Comprobar ausencia de errores de fórmula.
- Reconciliar 60 meses y totales regionales mediante Python/bundled runtime.
- Inspección visual del resumen y supuestos.

## Progress
- [x] F187-01 Diseñar workbook y supuestos.
- [x] F187-02 Autorizar operación de artefacto y construir workbook.
- [x] F187-03 Verificar cálculos y visualización. Evidencia: `verify_fp187.mjs` reporta `errors: []`; base Chile 23,256.321466, East US 16,474.602675; ahorros FP-184 Chile 1,453.152, East US 936.48; VAN bruto 1,104.10 y 711.53; inspección visual de `resumen.png` sin defectos.
- [x] F187-04 Documentar trazabilidad y actualizar Jira. Trazabilidad creada y comentario 10590 registrado en FP-187; no se hizo transición a Done.

## Next step
Validar con el grupo la tasa financiera, inversión inicial, costos de implementación y operación; después recalcular VAN/TIR incremental antes de cerrar el issue.

