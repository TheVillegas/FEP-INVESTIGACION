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
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Contexto confirmado: GENERAL, no específico de ONEBYTE. Población confirmada: productos y perfiles de usuario/organización. Se preservó la agrupación de productos definida en FP-51: herramientas cloud nativas, plataformas multicloud, herramientas de Kubernetes y herramientas de estimación temprana/políticas; FOCUS queda como estándar transversal. `Cloud Custodian` queda pendiente de clasificación humana por ser *policy-as-code* y no principalmente una herramienta de estimación. Las restricciones Jira fueron retiradas de FP-51 y FP-177–181 a solicitud de la persona usuaria; el equipo conserva la validación final.
- **Fundamento o evidencia de la decisión:** Alcance y decisiones aportados por la interacción; evidencia académica mapeada indicada arriba. Los nueve criterios de cobertura (visibilidad, asignación, optimización, automatización, multicloud, integración, adopción, precio y dependencia) corresponden al alcance de Jira FP-177, no a un ranking derivado de los artículos.
- **Evidencia adjunta o enlace al historial:** `docs/fp-177/escenarios-uso-y-poblacion-evaluada-borrador.md`; este registro; referencias Jira FP-51 y FP-177–181.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** No disponible en esta ejecución.
- **Validación humana (nombre, fecha y resultado):** **Pendiente de validación humana.** El equipo debe aprobar, modificar o rechazar cada escenario y confirmar población, productos, datos mínimos y clasificación de `Cloud Custodian` antes de usar el borrador como metodología.

> Según el punto 6.1, no registrés contenido generado por IA para el análisis comparativo y los criterios, las conclusiones y recomendaciones, el párrafo de aporte propio o discusión crítica, ni la redacción y justificaciones del cuestionario: esas partes requieren autoría humana exclusiva.

---

## Sesión de decisión — metodología y matriz FP-177

- **Fuente / afirmación:** Decisiones humanas seleccionadas para el borrador de metodología comparativa y matriz de FP-177. El registro conserva la decisión y sus límites; no es una evaluación comparativa, conclusión ni recomendación de productos.
- **Enlace, cita o ubicación de la evidencia:** `docs/fp-177/metodologia-comparativa-borrador.md`; `docs/fp-177/matriz-criterios-y-ponderaciones-borrador.md`; `docs/fp-177/escenarios-uso-y-poblacion-evaluada-borrador.md`. Respaldo metodológico acotado: `FP-48 TINV02/Papers academicos - FP-48/01_Manurung_Aji_2025_FinOps_Implementation.pdf`, sección **Methodology**, p. 712 (escala Crawl/Walk/Run de 1–3 y uso de media aritmética para dominios FinOps). No se atribuyen los nueve criterios, el cero, los pesos ni los umbrales al artículo.
- **Integrante responsable:** Pendiente de asignación humana.
- **Fecha (AAAA-MM-DD):** 2026-09-14.
- **Verificación realizada:** Se revisó la extracción Markdown del PDF de Manurung y Aji en los pasajes equivalentes a líneas 188–198 y 360–373: el texto declara Crawl=1 manual/reactivo, Walk=2 definido/proactivo, Run=3 automatizado/data-driven, y describe promedio aritmético de dominios. Se citó el PDF original y sección/página verificadas. Material comercial, si se usa luego para un producto, debe identificarse y no puede sostener un puntaje mayor que 1 por sí solo.
- **Nivel de asistencia de IA (0-3):** 3 — estructuración sustancial de borradores bajo decisiones seleccionadas; aprobación y aplicación metodológica pendientes de humanos.
- **Herramienta y versión (si aplica):** Pi coding agent; versión no expuesta de forma segura. Herramientas usadas: lectura y escritura local; CodeGraph MCP intentado para exploración y agotó el tiempo de espera.
- **Identificador del modelo (si aplica):** `gpt-5.6-terra` (PI_MODEL); proveedor: `openai-codex` (PI_PROVIDER).
- **Prompt exacto (texto o enlace a evidencia):**
  > Podriamos generar la metodologia, matriz, y Ponnderaciones correcto? Osea bajo mi criterio primero me haces pregunta sy vamos descidiendo
  >
  > Encuentro correcto usar la media arimetica - Media aritmética: usada por Manurung y Aji para combinar dominios FinOps. Es la opción más transparente.
- **Decisión relevante tomada a partir de la interacción:** Una matriz común para todos los escenarios; escala 0–3 con `NE` separado, donde 0 es adaptación FP-177 y 1–3 sigue Crawl/Walk/Run; 2–4 indicadores observables por criterio y media aritmética interna; línea base igualitaria exacta `100/9 %`; perfil de sensibilidad 15/15/15/12/10/10/8/8/7; resultados por escenario elegible, no ranking universal; `NE` excluido y cobertura mínima 70 %; `NA` justificado antes y renormalizado; conjuntos críticos propuestos con mínimo 1; jerarquía mixta de evidencia y tope 1 para evidencia solo comercial; doble evidencia para 3; normalización 0–100 y bandas; sensibilidad material por cambio de nivel u orden comparable; aprobación por mayoría simple con trazabilidad de revisión.
- **Fundamento o evidencia de la decisión:** Selección humana explícita en cuestionarios de esta sesión. El único apoyo académico aplicado de forma acotada es la escala 1–3 y el promedio aritmético de dominios en Manurung y Aji; los pesos son perfil normativo humano y no derivación del paper.
- **Evidencia adjunta o enlace al historial:** Los tres artefactos FP-177 citados arriba y la conversación de decisión de esta sesión.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** No disponible en esta ejecución.
- **Validación humana (nombre, fecha y resultado):** **Pendiente de validación humana.** Se deben aprobar/modificar/rechazar criterios, perfiles de peso, escala, conjuntos críticos y método general antes de puntuar productos.
