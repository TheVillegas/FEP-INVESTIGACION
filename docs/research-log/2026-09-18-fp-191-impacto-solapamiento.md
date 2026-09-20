# Bitácora de investigación — FP-191, impacto económico y solapamiento

> **Estado:** trazabilidad de asistencia IA para una hoja de evidencia/decisión. No habilita trasladar contenido asistido a análisis comparativo, criterios, conclusiones, recomendaciones, aporte propio/discusión crítica ni cuestionario; esas piezas requieren autoría y validación humana.

## Registro

- **Fuente / afirmación:** Hoja FP-191 que entrega evidencia delimitada de las tres tendencias seleccionadas humanamente: Cho (2026), Fragiadakis et al. (2024) y Feitosa et al. (2024). Registra decisión de inclusión preexistente, mecanismo económico, variables/unidades, cifras verificadas con contexto, límites, frontera de solapamiento e integración posterior solo como entrada de evidencia.
- **Enlace, cita o ubicación de la evidencia:** [`../fp-191/impacto-economico-y-solapamiento.md`](../fp-191/impacto-economico-y-solapamiento.md); fuentes verificadas en [`../fp-189/verificacion-fuentes-fp190.md`](../fp-189/verificacion-fuentes-fp190.md); decisión humana en [`../fp-190/etapas-1-2-delimitacion-y-candidatos-borrador.md`](../fp-190/etapas-1-2-delimitacion-y-candidatos-borrador.md).
- **Integrante responsable:** Pendiente de asignación y aprobación humana.
- **Fecha (AAAA-MM-DD):** 2026-09-18.
- **Verificación realizada:** Se reutilizaron exclusivamente las tres fuentes y las afirmaciones ya delimitadas como `Verificada con límites` en FP-189. Se contrastaron los enlaces de integración contra FP-172, FP-177, FP-180 y FP-182–FP-188 para definir fronteras sin recalcular ni modificar sus variables. Se conserva la retención: la ejecución de FP-189 no verificó registros directos en Scopus, Web of Science ni SciELO.
- **Nivel de asistencia de IA (0-3):** 3 — generación sustancial de la hoja estructurada y de esta trazabilidad; no se produjo texto académico final.
- **Herramienta y versión (si aplica):** Pi coding agent; versión/modelo no expuestos de forma segura. Herramientas locales: lectura de archivos, Bash y comprobaciones de rutas/enlaces y diff.
- **Identificador del modelo (si aplica):** No expuesto de forma segura en esta sesión.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Create an AI-assisted evidence handoff for FP-191 at `docs/fp-191/impacto-economico-y-solapamiento.md` and a traceability entry at `docs/research-log/2026-09-18-fp-191-impacto-solapamiento.md`. These are the only allowed edit surfaces. Use only the three human-selected trends and the verified evidence in `docs/fp-189/verificacion-fuentes-fp190.md`, plus existing FP-172/177/182–188 baseline variables. Respect the strict README restriction: do NOT write final comparative analysis, criteria, conclusions, recommendations, own-contribution prose, or questionnaire text. Instead produce a structured evidence/decision worksheet that records: human inclusion decision; economic mechanism; observable variables and units; verified numeric evidence with context; risks and limitations; exact overlap boundary; possible downstream integration points; and blank/explicitly human-only fields for final comparative judgment and recommendation. Do not invent monetary impacts. Make clear: Cho uses normalized hourly price units and mostly simulation; CloudPricingOps supports pricing intelligence but not demonstrated forecast accuracy; Feitosa measures text/artifacts, not realized savings. Include the Scopus/WoS/SciELO provenance hold. Explain why each selected trend does not unjustifiably duplicate FP-172/177/180/182–188. Add handoff mapping to FP-54 and FP-56, but only as evidence inputs. Record actual AI assistance in the research log. Run path/link checks and `git diff --check`; return whether technical FP-191 criteria are met and what human-only judgments remain.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Sin decisión académica nueva. Se registró la decisión humana ya fechada en FP-190 y se mantuvieron vacíos los campos de juicio comparativo y recomendación final.
- **Fundamento o evidencia de la decisión:** FP-190 documenta la selección humana exacta de tres tendencias. FP-189 limita las afirmaciones, unidades, cifras y procedencia. FP-172/177/180/182–188 contienen variables de base que esta hoja solo referencia como posibles entradas, sin transferir resultados ni crear impactos monetarios.
- **Evidencia adjunta o enlace al historial:** Este registro; `docs/fp-191/impacto-economico-y-solapamiento.md`; `docs/fp-189/verificacion-fuentes-fp190.md`; comprobaciones locales de ruta/enlace y `git diff --check` de esta ejecución.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** No disponible en esta ejecución.
- **Validación humana (nombre, fecha y resultado):** **Pendiente.** Una persona responsable debe revisar cada PDF y página de cifra; verificar procedencia en Scopus, WoS o SciELO según exigencia docente; aprobar o corregir los límites y fronteras de solapamiento; y redactar de forma independiente cualquier juicio comparativo, recomendación, aporte propio/discusión crítica o cuestionario.

## Límites conservados

- Cho: simulación predominante y precios normalizados por hora; no es tarifa publicable ni ahorro realizado.
- CloudPricingOps: sustenta inteligencia/análisis de precios; sus casos verificables no aportan una métrica de exactitud de forecast.
- Feitosa et al.: unidades textuales y artefactos Terraform abiertos; no mide gasto facturado, ahorro realizado ni causalidad.
- La procedencia Scopus/WoS/SciELO sigue pendiente y no se infiere desde Google Scholar.
