# FP-188 — Recomendación técnica y económica

## Objective
Redactar una recomendación técnica y económica condicionada para TINV-06, integrando la arquitectura, el TCO, las palancas FinOps, la comparación regional, la sensibilidad y el flujo de caja de FP-182 a FP-187.

## Problem
Los artefactos previos contienen resultados separados y todavía provisionales. FP-188 debe convertirlos en una decisión trazable sin presentar proxies como datos internos ni cerrar la selección regional antes de validar latencia, residencia de datos y requisitos de disponibilidad.

## Why
Jira FP-188 exige una recomendación final derivada de cálculos verificados, con compensaciones, incertidumbres y condiciones de validez explícitas.

## Scope
- Crear `docs/fp-188/recomendacion-tecnica-economica.md`.
- Integrar FP-182, FP-183, FP-184, FP-185, FP-186 y FP-187.
- Recomendar arquitectura base, región preferente condicionada y palancas FinOps.
- Presentar TCO, ahorro bruto, VAN, TIR y PRI con trazabilidad.
- Mapear evidencia académica y fuentes oficiales.
- Documentar riesgos, límites y validaciones pendientes.

## Constraints
- La arquitectura de FP-182 es ilustrativa, no productiva aprobada.
- Los valores de FP-187 son proxies públicos y estimaciones de ingeniería.
- No inventar latencia, residencia, SLA, WACC, costo empresa ni timesheets.
- No modificar los modelos fuente de FP-182 a FP-187.
- No presentar la recomendación como aprobación de inversión, proveedor o despliegue.

## Authorized scope
- Crear el documento de recomendación de FP-188.
- Ejecutar verificaciones locales de consistencia, enlaces y cifras.
- No actualizar Jira, GitHub ni crear PR en esta tarea sin autorización separada.

## Acceptance criteria
- [x] Existe una recomendación explícita y condicionada que separa la selección regional de la rentabilidad de la optimización FinOps.
- [x] Cada conclusión enlaza con FP-182 a FP-187 o con una fuente académica/oficial.
- [x] Se explican los trade-offs entre Chile Central y East US.
- [x] Se interpretan TCO, ahorro, sensibilidad, VAN, TIR y PRI sin ocultar proxies.
- [x] Se documentan riesgos y condiciones que podrían cambiar la decisión.
- [x] El documento incluye resumen ejecutivo y matriz de trazabilidad.
- [x] No hay cifras que contradigan los artefactos fuente.

## Applicable checks
- [x] Verificar existencia de todos los artefactos referenciados. Evidencia: 16 rutas locales resueltas, 0 faltantes.
- [x] Reconciliar cifras publicadas contra `docs/fp-187/flujo-caja-van-tir-fp-187.xlsx` y `docs/fp-186/resultados.json`. Evidencia: `verify_fp187.mjs` reporta `errors: []`; VAN/TIR documentados coinciden.
- [x] Comprobar que los enlaces externos estén presentes y que las rutas locales sean relativas. Evidencia: 16 enlaces locales resueltos, 0 faltantes.
- [x] Revisar Markdown y escanear marcadores de borrador no explicados. Evidencia: `git diff --check` limpio y sin TODO/TBD/PLACEHOLDER.

## Progress
- [x] F188-01 Consolidar evidencia y restricciones.
- [x] F188-02 Redactar recomendación y matriz de decisión.
- [x] F188-03 Verificar cifras, trazabilidad y formato.
- [x] F188-04 Corregir la lógica de decisión regional, explicitar la entrega a FP-54/FP-56 y reforzar la trazabilidad académica.

## Verification evidence
- `docs/fp-188/recomendacion-tecnica-economica.md` creado con 158 líneas.
- `node .codex-work/fp187/verify_fp187.mjs`: `errors: []`; controles de auditoría OK/PROVISIONAL.
- Validación de rutas locales: 16 enlaces, 0 faltantes.
- Validación de privacidad: sin rutas absolutas ni secretos.
- Auditoría posterior: el VAN de FP-187 mide la intervención FinOps dentro de cada región y no justifica preferir Chile sobre East US; la conclusión debe separar ambas decisiones.
- Corrección F188-04 verificada: East US queda como default económico cuando supera los gates; Chile queda condicionado por residencia, latencia, contrato o riesgo operativo.
- Validación posterior: 16 enlaces locales resueltos, 0 faltantes; entrega a FP-54/FP-56 declarada; `verify_fp187.mjs` sin errores; `git diff --check` limpio.

## Next step
Revisión humana de la recomendación, validación de latencia/residencia/HA/SLA y sustitución de proxies financieros antes de cambiar el estado de Jira o preparar el PR.
