# FP-53 — Cuestionario colaborativo

**Rama:** `docs/fp-53-cuestionario` · **Issue:** [#45](https://github.com/TheVillegas/FEP-INVESTIGACION/issues/45) · **Jira:** FP-53

Cuestionario del trabajo de investigación TI-06 FinOps construido en conjunto: cada integrante redacta las preguntas de su tema en su propio archivo dentro de `preguntas/`, y `cuestionario-maestro.md` consolida las secciones sin reescribirlas.

## Regla de autoría (rúbrica 6.1, obligatoria)

La redacción de **preguntas, opciones, respuestas y justificaciones** es de **autoría humana exclusiva**. La IA no redacta contenido del cuestionario; solo estructura, consolida y documenta. Cualquier uso de IA debe quedar registrado en `docs/research-log/` con nivel de asistencia, herramienta, prompt y validación humana.

## Cómo colaborar

1. Trabajá en la rama `docs/fp-53-cuestionario` (o en una rama derivada y abrí un PR).
2. Editá **solo tu archivo** en `preguntas/`. Si tu tema no tiene archivo, copiá `_plantilla-tema.md` con el nombre `fp-<n>-<tema>.md` y avisá para actualizar este índice y el del maestro.
3. Seguí el formato de pregunta de la plantilla (4 opciones + respuesta + justificación), igual al del cuestionario de FP-76.
4. No modifiques archivos de otros temas; los ajustes cruzados se resuelven en el maestro.
5. Registrá tus decisiones y el uso de IA en la bitácora.

## Archivos y responsables

| Archivo | Tema | Responsable | Estado |
|---|---|---|---|
| `cuestionario-maestro.md` | Consolidado | José (líder FP-53) | Pendiente de aportes |
| `preguntas/fp-49-marco-conceptual-finops.md` | Fases, personas, asignación, economía unitaria, glosario | José | Pendiente de redacción humana |
| `preguntas/fp-50-maestro-finops.md` | Libro maestro FinOps (workbook TINV-04) | Cristofer | Pendiente de redacción humana |
| `preguntas/fp-52-escenarios-metodologia-tco.md` | Escenarios, metodología comparativa, línea base TCO | Lucas | Pendiente de redacción humana |
| `preguntas/fp-76-tendencias.md` | Tendencias y base de evidencia | Danilo | Insumo humano en `origin/docs/fp-76-final-delivery`; integración con confirmación pendiente |

> El mapeo de responsables proviene de la planificación del equipo vigente en la última sesión de Jira consultada. Si el reparto cambió, ajustá esta tabla y el índice del maestro.

## Separación clave / aplicación

El maestro incluye respuestas y justificaciones (clave de la persona facilitadora). Para aplicar el cuestionario se prepara una copia sin respuestas ni justificaciones. La separación se arma al cierre, cuando todas las secciones estén completas.

## Criterios de cierre

- [ ] Cada sección tiene preguntas redactadas y justificadas por su integrante.
- [ ] Ningún contenido del cuestionario fue redactado por IA (bitácora al día).
- [ ] El maestro integra todas las secciones sin reescribirlas.
- [ ] Clave de respuestas y copia de aplicación separadas.
- [ ] `git diff --check` limpio y PR vinculado al issue #45 aprobado.
