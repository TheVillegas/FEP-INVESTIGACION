# FP-53 — Cuestionario colaborativo (feature doc)

**Rama:** `docs/fp-53-cuestionario`
**Jira:** FP-53 (TINV) — armar el cuestionario del trabajo de investigación TI-06 FinOps.
**Issue GitHub:** [#45](https://github.com/TheVillegas/FEP-INVESTIGACION/issues/45) (`type:docs`; `status:approved` pendiente del equipo).
**Líder:** José. **Modelo:** cada integrante aporta preguntas de su tema; el formulario se desarrolla en conjunto.

## Objetivo

Construir el cuestionario del informe como entregable colaborativo: una estructura por tema/integrante donde cada responsable redacta sus preguntas y justificaciones (autoría humana exclusiva, rúbrica 6.1), y un consolidado maestro que integre las partes sin reescribirlas.

## Restricciones

- **Rúbrica 6.1:** la redacción de las preguntas y sus justificaciones es de autoría humana exclusiva. La IA solo organiza estructura, trazabilidad, consolidación e integración de contenido humano.
- El cuestionario de FP-76 (10 preguntas, Versión 3 validada por Danilo 2026-09-20) vive en `origin/docs/fp-76-final-delivery` y aún no está en master. Solo puede integrarse como copia textual del contenido humano, con confirmación humana de destino y alcance (handoff FP-192 así lo exige).
- No se inventan preguntas, opciones ni justificaciones.

## Insumos identificados

- `origin/docs/fp-76-final-delivery:docs/fp-76/analisis-discusion-aporte-conclusiones-cuestionario.md` §7 — 10 preguntas humanas con clave y justificaciones (formato: 4 opciones + respuesta + justificación).
- `origin/docs/fp-76-final-delivery:docs/fp-192/insumos-discusion-critica-y-aporte.md` — handoff a FP-53/54/56 con confirmación humana pendiente.
- `FP-49/` (FP-167–FP-171, ya en master) — tema de José: fases, personas, asignación, economía unitaria, glosario.
- `docs/fp-177`, `docs/fp-180`, `docs/fp-182`, `docs/fp-183`, `docs/fp-185`, `docs/fp-186`, `docs/fp-187`, `docs/fp-188` — temas de escenarios/metodología/TCO.
- `FP-50/TINV-04_FinOps_maestro*.xlsx` — maestro FinOps.

## Estructura propuesta (a confirmar)

- `docs/fp-53/README.md` — proceso de colaboración y convenciones.
- `docs/fp-53/preguntas/<tema>.md` — un archivo por integrante/tema; cada uno redacta solo su archivo (evita conflictos de merge).
- `docs/fp-53/cuestionario-maestro.md` — consolidado que integra las secciones humanas, separando clave de respuestas de copia de aplicación.
- Bitácora: entrada en `docs/research-log/` con el uso de IA declarado.

## Tareas

1. Crear rama `docs/fp-53-cuestionario` desde `master`. — `docs/fp-53-cuestionario` ✅
2. Tracking ODD (este archivo) y espejo Engram. — `odd/fp53-cuestionario/tasks` (obs 889) ✅
3. Confirmar con el usuario estructura de secciones, mapeo tema/integrante y alcance Jira. ✅ (archivo por tema + maestro; alcance inferido; seguridad confirmada)
4. Crear issue GitHub `docs: FP-53 ...` con el formulario del repo. ✅ #45 con `type:docs`
5. Crear scaffold `docs/fp-53/` con índice, archivos por tema y convenciones de redacción humana. ✅ (README, maestro, plantilla, 4 temas)
6. Registrar entrada de bitácora con uso de IA. ✅ `docs/research-log/2026-09-20-fp-53-cuestionario-scaffold.md`
7. Commit de unidad de trabajo en la rama (sin push; push/PR quedan a decisión del usuario). ✅ `fd08f08`

## Evidencia de commits

| Commit | Qué cierra |
|---|---|
| `fd08f08` | Tarea 7: scaffold (README, maestro, plantilla, 4 temas) + bitácora + tracking |
