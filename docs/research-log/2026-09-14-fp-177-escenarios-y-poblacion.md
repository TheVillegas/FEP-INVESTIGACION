# Bitácora de investigación

## Registro

- **Fuente / afirmación:** Borrador estructurado de escenarios de uso y población evaluada para FP-177. El artefacto propone escenarios comparables y cobertura cualitativa; no constituye metodología aprobada ni evaluación o puntuación de proveedores.
- **Enlace, cita o ubicación de la evidencia:** Artefacto generado: `docs/fp-177/escenarios-uso-y-poblacion-evaluada-borrador.md`. Fuentes originales consultadas: `FP-48 TINV02/Papers academicos - FP-48/01_Manurung_Aji_2025_FinOps_Implementation.pdf` (pp. 709–718); `FP-48 TINV02/Papers academicos - FP-48/applsci-14-11946-v2.pdf` (§3.1, pp. 6–7); `FP-48 TINV02/Papers academicos - FP-48/s41781-024-00128-x.pdf` (resumen y §§2–4); `FP-48 TINV02/Papers academicos - FP-48/04_Resource_Accounting_of_Shared_IT_Resources_in_Multi-Tenant_Clouds.pdf` (pp. 302–307); `FP-48 TINV02/Papers academicos - FP-48/Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications An exploratory study.pdf` (§1). Para re-chequeo de extracción se usaron sus salidas Markdown en `FP-48 TINV02/Papers academicos - FP-48/markdown/`.
- **Integrante responsable:** Pendiente de asignación humana.
- **Fecha (AAAA-MM-DD):** 2026-09-14.
- **Verificación realizada:** Se contrastaron los perfiles y límites declarados contra los Markdown extraídos: seis arquitectos y organizaciones de Manurung y Aji; colaboración de roles y análisis de precios en Cloud PricingOps; caso distribuido ATLAS/CERN; atribución multi-tenant; e IaC/Terraform. Las citas del borrador apuntan a nombres de PDF originales, no a rutas de caché. Se distinguió explícitamente evidencia académica de decisiones de alcance de Jira.
- **Nivel de asistencia de IA (0-3):** 3 — generación sustancial de un borrador estructurado para revisión; sin aprobación metodológica ni conclusiones comparativas.
- **Herramienta y versión (si aplica):** Pi coding agent; versión no expuesta de forma segura en esta sesión. Herramientas usadas: lectura de archivos y búsqueda local; CodeGraph MCP intentado, sin respuesta por tiempo de espera.
- **Identificador del modelo (si aplica):** `gpt-5.6-terra` (PI_MODEL); proveedor: `openai-codex` (PI_PROVIDER).
- **Prompt exacto (texto o enlace a evidencia):**
  > Dale entonces lo que ahora deberias realizar, debido a que ya mapeaste correcto el excel con los pdf correcto? es que definamos los escenarios de uso y poblacion evaluada
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Contexto confirmado: GENERAL, no específico de ONEBYTE. Población confirmada: productos y perfiles de usuario/organización. Se preservó la agrupación de productos definida en FP-51: herramientas cloud nativas, plataformas multicloud, herramientas de Kubernetes y herramientas de estimación temprana/políticas; FOCUS queda como estándar transversal. `Cloud Custodian` se clasifica definitivamente en estimación temprana/políticas por su función de *policy-as-code* para gobierno y control preventivo; esta clasificación no prueba por sí misma capacidades de estimación. Las restricciones Jira fueron retiradas de FP-51 y FP-177–181 a solicitud de la persona usuaria.
- **Fundamento o evidencia de la decisión:** Alcance y decisiones aportados por la interacción; evidencia académica mapeada indicada arriba. Los nueve criterios de cobertura (visibilidad, asignación, optimización, automatización, multicloud, integración, adopción, precio y dependencia) corresponden al alcance de Jira FP-177, no a un ranking derivado de los artículos.
- **Evidencia adjunta o enlace al historial:** `docs/fp-177/escenarios-uso-y-poblacion-evaluada-borrador.md`; este registro; referencias Jira FP-51 y FP-177–181.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** No disponible en esta ejecución.
- **Validación humana (nombre, fecha y resultado):** Alcance, población, escenarios y clasificación de `Cloud Custodian` confirmados por consenso del equipo. La confirmación recibida no identifica votantes ni fecha; no se infieren esos datos. La IA estructuró el artefacto y no tomó la decisión humana.

> Según el punto 6.1, no registrés contenido generado por IA para el análisis comparativo y los criterios, las conclusiones y recomendaciones, el párrafo de aporte propio o discusión crítica, ni la redacción y justificaciones del cuestionario: esas partes requieren autoría humana exclusiva.

---

## Sesión de decisión — metodología y matriz FP-177

- **Fuente / afirmación:** Decisiones humanas seleccionadas para el borrador de metodología comparativa y matriz de FP-177. El registro conserva la decisión y sus límites; no es una evaluación comparativa, conclusión ni recomendación de productos.
- **Enlace, cita o ubicación de la evidencia:** `docs/fp-177/metodologia-comparativa-borrador.md`; `docs/fp-177/matriz-criterios-y-ponderaciones-borrador.md`; `docs/fp-177/escenarios-uso-y-poblacion-evaluada-borrador.md`. Respaldo metodológico acotado: `FP-48 TINV02/Papers academicos - FP-48/01_Manurung_Aji_2025_FinOps_Implementation.pdf`, sección **Methodology**, p. 712 (escala Crawl/Walk/Run de 1–3 y uso de media aritmética para dominios FinOps). No se atribuyen los nueve criterios, el cero, los pesos ni los umbrales al artículo.
- **Integrante responsable:** Pendiente de asignación humana.
- **Fecha (AAAA-MM-DD):** 2026-09-14.
- **Verificación realizada:** Se revisó la extracción Markdown del PDF de Manurung y Aji en los pasajes equivalentes a líneas 188–198 y 360–373: el texto declara Crawl=1 manual/reactivo, Walk=2 definido/proactivo, Run=3 automatizado/data-driven, y describe promedio aritmético de dominios. Se citó el PDF original y sección/página verificadas. Material comercial, si se usa luego para un producto, debe identificarse y no puede sostener un puntaje mayor que 1 por sí solo.
- **Nivel de asistencia de IA (0-3):** 3 — estructuración sustancial de artefactos bajo decisiones humanas confirmadas; la IA no aprobó ni aplicó la metodología a productos.
- **Herramienta y versión (si aplica):** Pi coding agent; versión no expuesta de forma segura. Herramientas usadas: lectura y escritura local; CodeGraph MCP intentado para exploración y agotó el tiempo de espera.
- **Identificador del modelo (si aplica):** `gpt-5.6-terra` (PI_MODEL); proveedor: `openai-codex` (PI_PROVIDER).
- **Prompt exacto (texto o enlace a evidencia):**
  > Podriamos generar la metodologia, matriz, y Ponnderaciones correcto? Osea bajo mi criterio primero me haces pregunta sy vamos descidiendo
  >
  > Encuentro correcto usar la media arimetica - Media aritmética: usada por Manurung y Aji para combinar dominios FinOps. Es la opción más transparente.
- **Decisión relevante tomada a partir de la interacción:** Una matriz común para todos los escenarios; escala 0–3 con `NE` separado, donde 0 es adaptación FP-177 y 1–3 sigue Crawl/Walk/Run; 2–4 indicadores observables por criterio y media aritmética interna; línea base igualitaria exacta `100/9 %`; perfil de sensibilidad 15/15/15/12/10/10/8/8/7; resultados por escenario elegible, no ranking universal; `NE` excluido y cobertura mínima 70 %; `NA` justificado antes y renormalizado; conjuntos críticos confirmados con mínimo 1; jerarquía mixta de evidencia y tope 1 para evidencia solo comercial; doble evidencia para 3; normalización 0–100 y bandas; sensibilidad material por cambio de nivel u orden comparable. El método quedó confirmado por consenso del equipo; no se registraron votantes ni fecha en la confirmación y no se infieren.
- **Fundamento o evidencia de la decisión:** Selección humana explícita en cuestionarios de esta sesión. El único apoyo académico aplicado de forma acotada es la escala 1–3 y el promedio aritmético de dominios en Manurung y Aji; los pesos son perfil normativo humano y no derivación del paper.
- **Evidencia adjunta o enlace al historial:** Los tres artefactos FP-177 citados arriba y la conversación de decisión de esta sesión.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** No disponible en esta ejecución.
- **Validación humana (nombre, fecha y resultado):** Criterios, perfiles de peso, escala, conjuntos críticos y método general confirmados por consenso del equipo. La confirmación recibida no identifica votantes ni fecha; no se infieren esos datos. La IA estructuró los borradores y no realizó la aprobación humana.

---

## Consolidación de decisiones humanas — FP-126, FP-177 y FP-179

- **Fuente / afirmación:** Confirmación humana de que FP-178 está listo y de que la matriz FP-126 recibida en `master` es la fuente final para resolver la alternativa multicloud antes registrada como Densify.
- **Enlace, cita o ubicación de la evidencia:** `FP-48 TINV02/TINV_Matriz_de_Fuentes_FP-126_actualizada_2026-09-15.xlsx`, hoja `Alternativas`, fila de plataformas multicloud `Adicional 2`; `docs/fp-179/alternative-verification.md`; artefactos de `docs/fp-177/`.
- **Integrante responsable:** Equipo, por consenso confirmado; no se identifican integrantes individuales.
- **Fecha (AAAA-MM-DD):** No registrada en la confirmación; no se infiere.
- **Verificación realizada:** Inspección de solo lectura del XML del libro final. La hoja `Alternativas` registra literalmente `Densify` como `Adicional 2` de plataformas multicloud y `Cloud Custodian` como herramienta base de estimación temprana para políticas como código.
- **Nivel de asistencia de IA (0-3):** 2 — localización de las entradas del libro y actualización estructural de la documentación. La IA no decidió la inclusión de Densify, la clasificación de Cloud Custodian ni el consenso metodológico.
- **Herramienta y versión (si aplica):** Pi coding agent; Python estándar (`zipfile` y XML) para inspección de solo lectura del XLSX.
- **Identificador del modelo (si aplica):** `gpt-5.6-terra` (PI_MODEL); proveedor: `openai-codex` (PI_PROVIDER).
- **Decisión relevante tomada a partir de la interacción:** Conservar literalmente Densify como decisión final de la matriz y documentar su limitación técnica: su inclusión no constituye validación externa como plataforma FinOps multicloud. Clasificar definitivamente Cloud Custodian en estimación temprana/políticas. Retirar los bloques y estados de aprobación pendientes de FP-177 porque alcance y método fueron confirmados por consenso del equipo, sin inventar votantes ni fechas.
- **Fundamento o evidencia de la decisión:** Decisión humana explícita. La evidencia técnica preservada en FP-179 indica que la URL registrada de Densify resuelve a Kubex y documenta optimización de recursos Kubernetes; por ello se conserva la distinción entre inclusión literal de matriz y verificación de capacidad.
- **Evidencia adjunta o enlace al historial:** Libro final FP-126 y artefactos indicados arriba.
- **Validación humana (nombre, fecha y resultado):** Consenso del equipo confirmado por la persona usuaria; no se proporcionaron nombres ni fecha y no se infieren. Resultado: decisiones aplicables a la documentación.