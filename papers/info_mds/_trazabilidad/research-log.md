# Bitácora de investigación

> Registro académico de generación y síntesis con IA para lectura personal. No es una exportación del chat. La incorporación de cualquier afirmación, cifra o referencia al informe exige verificación en la fuente original.

## Registro 1

- **Fuente / afirmación:** Solicitud inicial de convertir los 14 PDF en Markdown y producir una síntesis estructurada de cada paper.
- **Enlace, cita o ubicación de la evidencia:** `papers-pdf/` e `info_mds/`.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-13.
- **Verificación realizada:** Verificación técnica automatizada de cantidad, estructura y correspondencia de nombres; validación académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — generación sustancial de síntesis y conversión documental para lectura personal.
- **Herramienta y versión (si aplica):** OpenCode / modelo configurado por el entorno.
- **Identificador del modelo (si aplica):** OpenCode / modelo configurado por el entorno.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  quiero que leas los pdfs en la carpeta de papers y me generes archivos md por cada uno, y lo guardes en la carpeta de info_mds, esa será nuestra zona de trabajo para artefactos.

  Despues de eso quiero que me hagas un resumen estrcuturado por cada uno colocando lo siguiente:

  1. titulo 
  2. autor-fecha 
  3.problema que trata 
  4. que quiere hacer
  5. como lo hace
  6. resultados
  7. discusion/trabajo futuro
  8.Conclusion
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Crear un Markdown por PDF, conservar el nombre base y separar síntesis de la extracción completa.
- **Fundamento o evidencia de la decisión:** Pedido explícito del usuario; estructura requerida de ocho apartados.
- **Evidencia adjunta o enlace al historial:** `info_mds/INDEX.md` y los 14 documentos enlazados allí.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente**.

## Registro 2

- **Fuente / afirmación:** Revisión de reglas académicas, matriz de fuentes e INV-01; clasificación de las síntesis por pilar.
- **Enlace, cita o ubicación de la evidencia:** `reglas/INVESTIGACION/Indicaciones Trabajo de Investigacion 2026.md`, `reglas/templates/research-log.md`, `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv` y `docs/INV-01.md`.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-13.
- **Verificación realizada:** Clasificación contrastada con las filas P1/P2/P3 del CSV; discrepancias bibliográficas contrastadas con las portadas de los PDF; validación académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — generación sustancial de síntesis, organización y extracción para lectura personal.
- **Herramienta y versión (si aplica):** OpenCode / modelo configurado por el entorno.
- **Identificador del modelo (si aplica):** OpenCode / modelo configurado por el entorno.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  revisa la carpeta de reglas y lee las restricciones de manejo del enotrno y la trazabilidad, despues de eso, continua haciendo un resumen estrcuturado como te pedi en el prompt anterior, que son para lectura mia.

  Quiero que veas el archivo csv y empieces a categorizar en grupos los resumenes, así sé para que pilar son y corresponde, revisa el archivo de inv-01 para más info preliminar
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Aplicar la pertenencia única del CSV; tratar los nombres de P1/P2/P3 como interpretaciones preliminares; conservar Tivive como fuera de alcance; usar el año y la autoría bibliográfica visibles en cada PDF.
- **Fundamento o evidencia de la decisión:** Regla de un pilar por fuente en el CSV; ausencia de Tivive en la matriz; portadas y datos editoriales de Manurung, Megahed, ATLAS y Turkkan.
- **Evidencia adjunta o enlace al historial:** `info_mds/INDEX.md` y metadatos de clasificación al inicio de cada síntesis.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente**.

## Registro 3 — FP-168

- **Fuente / afirmación:** Revisión académica de roles y áreas que colaboran en decisiones de costo cloud, con responsabilidades, beneficios, objetivos, métricas candidatas, cargos habituales y una tabla comparativa transpuesta.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Roles y participacion.md`; `info_mds/_trazabilidad/research-log.md`; `docs/research-log/2026-09-16-fp-168-roles-y-areas-finops.md` (bitácora previa migrada y retirada); https://www.finops.org/framework/personas/; https://www.finops.org/framework/persona/engineering/; https://www.finops.org/framework/persona/finance/; https://www.finops.org/framework/persona/procurement/; https://www.finops.org/framework/persona/product/; https://www.finops.org/framework/persona/finops-practitioner/; https://www.finops.org/framework/persona/leadership/. Fuentes web consultadas el 2026-09-16. También se verificó que `https://www.finops.org/framework/persona/business/` devolvía 404, por lo que no se usó como fuente.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-16.
- **Verificación realizada:** Se contrastó la estructura vigente de las páginas oficiales —objetivo principal, objetivos, desafíos, métricas clave, beneficios y roles habituales— para Ingeniería, Finanzas, Compras, Producto, FinOps Practitioner y Liderazgo. Se comprobó la ausencia de una página vigente separada para Negocio; sus ejemplos quedaron identificados como propuestas derivadas del contexto verificado. Validación académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — reestructuración, síntesis y redacción sustancial asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode + orquestador.
- **Identificador del modelo (si aplica):** `openai/gpt-5.6-sol`.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Corregir FP-168 siguiendo la convención de info_mds/_trazabilidad/research-log.md. Reescribir únicamente FP-49/Roles y participacion.md con siete áreas FinOps; incluir para cada una un párrafo de responsabilidad y flujo, mini-párrafos de beneficios, objetivos y métricas candidatas, y exactamente tres roles reales de industria. Verificar la estructura y el contenido de las páginas oficiales vigentes de FinOps Foundation. Cerrar con una tabla transpuesta cuyas columnas sean las áreas. Migrar la trazabilidad previa al registro canónico y eliminar solo el log no conforme creado para esta tarea. No actualizar Jira, no hacer commit y no dar la tarea por completada.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Mantener mini-párrafos detallados por área; presentar las métricas como indicadores candidatos pendientes de adopción y datos del caso; limitar cada área a exactamente tres cargos habituales; ubicar las referencias antes de una tabla final transpuesta; y migrar la trazabilidad de FP-168 al registro canónico, retirando el log separado no conforme.
- **Fundamento o evidencia de la decisión:** Corrección explícita del usuario y estructura observada en las páginas oficiales de personas FinOps. La relación con el caso se mantuvo adaptable porque no se conocen proveedor, carga, autoridad, presupuestos ni asignaciones del equipo.
- **Evidencia adjunta o enlace al historial:** Salida en `FP-49/Roles y participacion.md`. La bitácora previa `docs/research-log/2026-09-16-fp-168-roles-y-areas-finops.md` fue migrada a este registro y eliminada. No se actualizó Jira FP-168, no se marcó la tarea como completada y no se realizó commit.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente**.

## Decisiones y límites del trabajo

- Las síntesis se basan exclusivamente en el PDF correspondiente. El CSV se usa únicamente para clasificar y comprobar discrepancias bibliográficas; INV-01 se usa solo para la relación preliminar.
- La sección “Conclusión del paper” resume lo sostenido por sus autores y no constituye una conclusión ni recomendación del grupo.
- El texto extraído conserva el contenido textual por página. Figuras, diseño multicolumna, tablas y ecuaciones pueden perder fidelidad visual; cada documento incluye una advertencia antes de la extracción.
- No se generaron análisis comparativos, recomendaciones, aporte propio, discusión crítica ni preguntas del cuestionario, porque las reglas reservan esas partes a autoría humana.
- **Estado de validación humana global:** pendiente.

## Registro 4 — FP-168 (continuación)

- **Fuente / afirmación:** Continuación de FP-168 para documentar exclusivamente la categoría oficial *Allied Personas* mediante una introducción y tres líneas descriptivas por persona, sin alterar el texto previamente revisado.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Roles y participacion.md`; `info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/personas/. Fuente web oficial consultada el 2026-09-16.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-16.
- **Verificación realizada:** La página oficial clasificó como *Allied Personas* a ITAM, ITFM, Sustainability, ITSM / ITIL y Security. Se verificó que cada persona apareciera una sola vez y tuviera exactamente tres viñetas. Los 12 897 bytes previos del documento conservaron el SHA-256 `f8ada58142b222e82d5e7710f8eea03612752750e262a2f6c1b5577882819152` después del anexo. La página de clasificación no presentó enlaces a fichas individuales para estas cinco personas; por ello no se inventaron ni utilizaron URL adicionales. Validación académica humana de la sección nueva pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — investigación oficial, síntesis y redacción sustancial asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode `openai/gpt-5.6-sol` + orquestador `openai/gpt-5.6-sol`.
- **Identificador del modelo (si aplica):** OpenCode `openai/gpt-5.6-sol`; orquestador `openai/gpt-5.6-sol`.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  FP-168 continuación: anexar únicamente al final de FP-49/Roles y participacion.md; el texto revisado queda congelado. Añadir una introducción y exactamente tres líneas por cada Allied Persona oficial vigente, con fuentes oficiales, sin modificar el contenido previo.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Distinguir la clasificación del framework de cualquier asignación del equipo del curso; documentar exactamente ITAM, ITFM, Sustainability, ITSM / ITIL y Security; y usar como única referencia la página oficial consultada, porque no enlazó fichas individuales.
- **Fundamento o evidencia de la decisión:** Instrucción explícita de preservar el documento revisado y clasificación vigente observada en la página oficial de Personas de FinOps Foundation.
- **Evidencia adjunta o enlace al historial:** Salida anexada en `FP-49/Roles y participacion.md`; trazabilidad añadida en `info_mds/_trazabilidad/research-log.md`. No se modificó texto previo, no se actualizó Jira, no se marcó la tarea como completada y no se realizó commit.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para la nueva sección Allied Personas**.

## Registro 5 — FP-168 (continuación)

- **Fuente / afirmación:** Revisión quirúrgica del anexo de personas para incorporar la categoría oficial *Core Personas* y reestructurar exclusivamente la categoría *Allied Personas*, preservando sin cambios todo el contenido anterior.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Roles y participacion.md`; `info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/personas/. Fuente web oficial consultada el 2026-09-16.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-16.
- **Verificación realizada:** La página oficial confirmó las categorías *Core Personas* y *Allied Personas*, y mantuvo como personas aliadas a ITAM, ITFM, Sustainability, ITSM / ITIL y Security. Se verificó un único párrafo de cuatro oraciones para *Core Personas* y, para cada persona aliada, un párrafo descriptivo y exactamente tres responsabilidades. Los 11 883 bytes anteriores al encabezado previo `## Allied Personas` conservaron el SHA-256 `f57eba743844380953aa57a52c1b3a870419b84cbfe91c7d5bfcda4dbefe34f6` antes y después de la revisión. Validación académica humana del anexo revisado pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — verificación oficial, síntesis y redacción sustancial asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode `openai/gpt-5.6-sol` + orquestador `openai/gpt-5.6-sol`.
- **Identificador del modelo (si aplica):** OpenCode `openai/gpt-5.6-sol`; orquestador `openai/gpt-5.6-sol`.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Revisar únicamente el anexo de personas de FP-168: preservar byte por byte todo lo anterior al encabezado existente de Allied Personas; añadir un párrafo compacto de Core Personas; reescribir las cinco Allied Personas oficiales con un párrafo y tres responsabilidades cada una; usar solo la página oficial de Personas; y registrar la continuación en la bitácora canónica sin Jira, finalización ni commit.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Explicar *Core Personas* en un único párrafo sin convertir la clasificación en asignaciones del equipo ni en una RACI rígida; y presentar cada *Allied Persona* mediante un párrafo cohesivo seguido por tres responsabilidades concretas que apoyan el ciclo FinOps sin atribuirle la propiedad completa de una fase.
- **Fundamento o evidencia de la decisión:** Instrucción explícita del usuario y clasificación vigente observada en la página oficial de Personas de FinOps Foundation.
- **Evidencia adjunta o enlace al historial:** Anexo revisado en `FP-49/Roles y participacion.md`; trazabilidad añadida en `info_mds/_trazabilidad/research-log.md`. El contenido previo, incluida la tabla y sus referencias, permaneció intacto. No se actualizó Jira FP-168, no se marcó la tarea como completada y no se realizó commit.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para el anexo revisado de personas**.

## Registro 6 — FP-168 (continuación)

- **Fuente / afirmación:** Reorganización exclusivamente estructural de la información de FP-168 después de su revisión humana, sin expansión, resumen, paráfrasis, corrección ni investigación factual.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Roles y participacion.md`; `info_mds/_trazabilidad/research-log.md`. No se consultaron fuentes externas porque no se realizó investigación factual.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-16.
- **Verificación realizada:** Se compararon antes y después 91 bloques sustantivos, correspondientes a 87 bloques únicos, como multiconjuntos no ordenados después de retirar únicamente marcadores de encabezado y espacios circundantes. Ambos multiconjuntos produjeron el SHA-256 `ee93171513b1e00f6f26fb453850ef4950d60e6de1b23c45deb2007ee2f0914c`, con cero bloques faltantes, añadidos o modificados. También se verificó un único H1, se leyó nuevamente el archivo final y se ejecutó `git diff --check`.
- **Nivel de asistencia de IA (0-3):** 2 — organización y estructuración documental asistidas por IA, sin generación ni modificación de contenido sustantivo.
- **Herramienta y versión (si aplica):** OpenCode `openai/gpt-5.6-sol` + orquestador `openai/gpt-5.6-sol`.
- **Identificador del modelo (si aplica):** OpenCode `openai/gpt-5.6-sol`; orquestador `openai/gpt-5.6-sol`.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Reorganizar únicamente la estructura de FP-49/Roles y participacion.md después de la revisión humana, preservando exactamente todo el contenido sustantivo; consolidar las referencias al final; validar la preservación mediante un multiconjunto no ordenado de bloques; y registrar la continuación en la bitácora canónica sin Jira, finalización ni commit.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Usar `Core Personas` como único H1 sin añadir un título nuevo; conservar los nombres existentes de todas las áreas y personas; mantener la tabla como bloque intacto después de las áreas principales; ubicar *Allied Personas* después de la tabla; y consolidar al final las referencias existentes bajo `Referencias`, conservando `Referencias de personas` como subsección y manteniendo intactos los identificadores `[1]` a `[7]` y `[A1]`.
- **Fundamento o evidencia de la decisión:** Instrucción explícita de realizar una edición solo estructural sobre información revisada personalmente por el usuario y de no efectuar cambios semánticos. No se añadieron las secciones ausentes de Negocio ni de flujo de colaboración porque hacerlo habría exigido contenido nuevo.
- **Evidencia adjunta o enlace al historial:** Resultado estructural en `FP-49/Roles y participacion.md`; trazabilidad añadida únicamente en `info_mds/_trazabilidad/research-log.md`. La información revisada por el usuario se retuvo sin cambios sustantivos; el resultado estructural queda pendiente de confirmación del usuario. No se actualizó Jira FP-168, no se marcó la tarea como completada y no se realizó commit.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** La información fue revisada previamente por el usuario; **la organización estructural resultante queda pendiente de confirmación**.

## Registro 7 — Revisión de FP-169 y FP-170

- **Fuente / afirmación:** Investigación documental acotada para preparar un mapa de trabajo humano de FP-169 (economía unitaria) y FP-170 (etiquetado y asignación de costos), sin redactar los entregables finales.
- **Enlace, cita o ubicación de la evidencia:** Jira FP-169 y FP-170, con FP-51 y FP-52 consultados únicamente como límites y dependencias; `FP-49/Roles y participacion.md`; `FP-49/Las fases de FinOps.md`; `docs/INV-01.md`; `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`; `info_mds/P1/Tak et al. - 2017 - Resource Accounting of Shared IT Resources in Multi-Tenant Clouds.md`; `info_mds/P1/Manurung y Aji - 2026 - Evaluating the Implementation of the FinOps Framework for Cloud Infrastructure Cost Management A Ca.md`; `reglas/INVESTIGACION/Indicaciones Trabajo de Investigacion 2026.md`; `docs/fp-182/arquitectura-y-supuestos-borrador.md` y `docs/fp-183/modelo-tco-linea-base-5-anos.xlsx` en el commit histórico `ba2fba2` de `origin/docs/fp182-fp183-tco` —no presentes en la rama de trabajo `FP-49`—; `FP-48 TINV02/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm` en esa misma referencia histórica; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/framework/capabilities/unit-economics/; https://www.finops.org/framework/capabilities/invoicing-chargeback/; https://focus.finops.org/docs/specification/v1-4/; https://opencost.io/docs/. Fuentes web oficiales consultadas el 2026-09-16.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-16.
- **Verificación realizada:** Se contrastaron los requisitos de Jira con la pauta, el esquema de INV-01, las fuentes oficiales registradas como 002, 003, 005 y 014 en la matriz, las secciones originales extraídas de Tak y Manurung, y los artefactos históricos de FP-182/FP-183. Se verificó que la rama actual no contiene `docs/fp-182/` ni `docs/fp-183/`; la referencia histórica propone Azure Container Apps y conserva todos los volúmenes como hipótesis editables pendientes de validación humana. El libro histórico registra seis tarifas de CPU, memoria y solicitudes por región como verificadas en FP-48, pero mantiene seis partidas sin precio por región y bloquea la interpretación del TCO total. Las páginas oficiales vigentes sustentan Unit Economics, Allocation e Invoicing & Chargeback; OpenCost queda limitado a contextos Kubernetes. Tak aporta una base causal para recursos compartidos, no una política FinOps de reparto; Manurung aporta evidencia empírica de brechas, no definiciones normativas. Validación académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 2 — búsqueda, contraste, estructuración y mapa de trabajo para revisión humana; no se generó texto final de FP-169 ni FP-170.
- **Herramienta y versión (si aplica):** OpenCode + orquestador.
- **Identificador del modelo (si aplica):** `openai/gpt-5.6-sol`.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Realizar una investigación documental acotada, en español, para revisar FP-169 y FP-170 de modo que el usuario pueda ejecutarlas. No usar SDD, no redactar los entregables finales, no editar Jira ni estados, no modificar entregables existentes, planillas o salidas, y no hacer commit. La única mutación permitida es añadir un registro secuencial a la bitácora canónica. Revisar FP-49, la matriz de fuentes, INV-01, los originales extraídos de Tak y Manurung, los artefactos disponibles de FP-52 y las fuentes oficiales de FinOps Foundation, FOCUS y OpenCost; distinguir datos verificados, supuestos, marcadores y vacíos. Entregar en chat un mapa de trabajo de FP-169 y FP-170 con fórmulas simbólicas, datos requeridos, dependencias, vacíos, orden recomendado, listas de preparación y fuentes exactas.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Limitar el resultado a una evaluación ejecutiva en chat; separar economía unitaria, asignación y evaluación ponderada; no convertir supuestos históricos de FP-52 en datos del caso; y dejar las definiciones operativas, conductores de reparto, alcance de costos y política showback/chargeback sujetos a decisión humana de ONEBYTE.
- **Fundamento o evidencia de la decisión:** Instrucción explícita del usuario, estados incompletos de los artefactos históricos y reglas académicas que reservan cifras, análisis comparativo, conclusiones y recomendaciones a fuentes verificadas y autoría humana.
- **Evidencia adjunta o enlace al historial:** Evaluación entregada en el chat de esta interacción. Hallazgos pendientes: definición humana de transacción, cliente atendido y solicitud válida; alcance del numerador; periodo; tratamiento de tokens de entrada/salida; taxonomía y obligatoriedad de etiquetas; centros de costo; inventario de costos directos, compartidos y no asignados; conductores de reparto; y decisión financiera entre showback y chargeback. No se editaron Jira ni estados, no se redactó texto final de FP-169/FP-170, no se modificaron planillas ni entregables existentes y no se realizó commit.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente**.

## Registro 8 — FP-170

- **Fuente / afirmación:** Primer borrador académico y conceptual sobre etiquetado, asignación de costos, costos directos, compartidos y no asignados, y diferencias entre *showback* y *chargeback*, con un método reproducible y un ejemplo hipotético adaptable a ONEBYTE.
- **Enlace, cita o ubicación de la evidencia:** Jira FP-170; `FP-49/Asignacion de costos.md`; `FP-49/Las fases de FinOps.md`; `FP-49/Roles y participacion.md`; `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`; `info_mds/P1/Tak et al. - 2017 - Resource Accounting of Shared IT Resources in Multi-Tenant Clouds.md`; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/framework/capabilities/invoicing-chargeback/. Fuentes web oficiales consultadas el 2026-09-16.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-16.
- **Verificación realizada:** Se contrastaron los criterios de Jira FP-170 con las páginas oficiales vigentes de Allocation e Invoicing & Chargeback, la fuente 002 y la fila académica sin ID numérico de Tak et al. en la matriz FP-48, y la extracción original del artículo: ecuación (1), sección 3, p. 305, apartados sobre uso no atribuible y limitaciones. Se comprobó de forma independiente que la tasa hipotética es USD 0.0012 por solicitud; las asignaciones son USD 840 y USD 360; los costos cargados totales son USD 2,840 y USD 1,360; los costos directos y compartidos suman USD 4,200; con USD 200 no asignados la factura suma USD 4,400; y la cobertura es 95.45 %. También se validaron las columnas de las tablas Markdown y `git diff --check`. Validación académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — verificación de fuentes, estructuración, cálculos y redacción sustancial de un borrador para revisión humana.
- **Herramienta y versión (si aplica):** OpenCode `openai/gpt-5.6-sol` + orquestador `openai/gpt-5.6-sol`.
- **Identificador del modelo (si aplica):** OpenCode `openai/gpt-5.6-sol`; orquestador `openai/gpt-5.6-sol`.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  empecemos
  ```

  Intención contextual: iniciar FP-170 después de revisar FP-169/FP-170 y aceptar el orden recomendado, produciendo solo un primer borrador revisable sobre etiquetado y asignación de costos, sin declarar finalización ni aprobación.
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Separar metadatos de reglas de asignación; presentar `owner`, `product`, `environment` y `cost_center` únicamente como taxonomía mínima propuesta y pendiente de aprobación; distinguir costos compartidos de costos no asignados; no jerarquizar *showback* y *chargeback*; utilizar solicitudes como conductor exclusivamente hipotético; mantener el costo no asignado fuera del reparto; y limitar Tak et al. a sustento técnico causal, no a política normativa FinOps.
- **Fundamento o evidencia de la decisión:** Criterios de Jira FP-170, definiciones oficiales vigentes de FinOps Foundation y evidencia técnica de Tak et al. La fuente 002 de FP-48 registra Allocation; la página Invoicing & Chargeback no tiene una fila independiente; Tak et al. aparece en una fila académica sin ID numérico. El artículo usa Xen 3.1.4 y declara limitaciones sobre memoria, caché, *buffering*, I/O físico e interferencia, por lo que no se extrapoló como política del caso.
- **Evidencia adjunta o enlace al historial:** Borrador en `FP-49/Asignacion de costos.md` y este registro canónico. Pendientes de revisión humana: productos y destinos reales, periodo, conjuntos compartidos, conductores, etiquetas, responsables, excepciones, política de *showback*/*chargeback* y fuentes de datos. No se actualizó Jira FP-170 ni su estado, no se realizó evaluación ponderada de FP-51, no se modificaron planillas, no se hizo commit y no se editaron otros entregables.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para el borrador de FP-170**.

## Registro 9 — FP-170 (ajuste de alcance)

- **Fuente / afirmación:** Corrección del alcance del borrador de FP-170 para concentrarlo exclusivamente en la macrotarea conceptual de asignación de costos, etiquetado, costos compartidos, *showback* frente a *chargeback* y tasa de asignación. Esta intervención corresponde a una microtarea ejecutada paso a paso; por indicación expresa del usuario, el trabajo de caso aplicado se difiere y se retira de este artefacto.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Asignacion de costos.md`; `info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/framework/capabilities/invoicing-chargeback/; `info_mds/P1/Tak et al. - 2017 - Resource Accounting of Shared IT Resources in Multi-Tenant Clouds.md`. Las fuentes externas conservan la fecha de consulta verificada del 2026-09-16; no se realizó nueva investigación externa.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se leyó el borrador vigente y se eliminó su encuadre aplicado, junto con referencias organizacionales, destinos de ejemplo, importes, cálculos numéricos, cobertura y la sección de datos por validar. Se conservaron las cinco áreas conceptuales solicitadas, las fórmulas simbólicas `r=S/sum(q_i)` y `A_i=r*q_i`, la comprobación de conservación, la tabla comparativa de tres columnas y las salvedades de atribución técnica de Tak et al. Se verificaron términos excluidos, encabezados, columnas de tabla y `git diff --check`. Revisión académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — corrección de alcance, reorganización y redacción sustancial asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode `openai/gpt-5.6-sol` + orquestador `openai/gpt-5.6-sol`.
- **Identificador del modelo (si aplica):** OpenCode `openai/gpt-5.6-sol`; orquestador `openai/gpt-5.6-sol`.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Corregir el alcance de FP-170: olvidar el caso aplicado y concentrar FP-49/Asignacion de costos.md en la macrotarea conceptual, porque las microtareas se trabajan paso a paso. Mantener únicamente asignación de costos, etiquetado, costos compartidos, showback frente a chargeback y tasa de asignación; retirar referencias organizacionales, ejemplos de productos, cifras, cálculos de cobertura y datos por validar. Reorganizar el documento de forma concisa, conservar solo citas verificadas y fórmulas simbólicas, y añadir el Registro 9 a la bitácora canónica. No usar SDD, no modificar Jira ni estados, no declarar finalización, no hacer commit y no editar otros entregables.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Limitar el documento al alcance conceptual de la macrotarea y retirar de este artefacto todo desarrollo aplicado o numérico por dirección explícita del usuario. Mantener la diferencia entre metadatos y política de asignación, la distinción entre costos directos, compartidos y no asignados, la neutralidad entre *showback* y *chargeback*, y únicamente la tasa, asignación y conservación en forma simbólica.
- **Fundamento o evidencia de la decisión:** Corrección explícita del usuario sobre el alcance y continuidad paso a paso de las microtareas; definiciones oficiales ya verificadas de FinOps Foundation y atribución técnica acotada de Tak et al.
- **Evidencia adjunta o enlace al historial:** Alcance conceptual revisado en `FP-49/Asignacion de costos.md` y trazabilidad añadida en este registro canónico. El trabajo aplicado queda diferido y fue retirado de este artefacto por indicación del usuario. No se actualizó Jira FP-170 ni su estado, no se declaró finalización, no se realizó commit, no se incorporó contenido de economía unitaria de FP-169, no se realizó comparación o priorización de FP-51 y no se editaron otros entregables.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para el ajuste conceptual de FP-170**.

## Registro 10 — FP-169

- **Fuente / afirmación:** Desarrollo conceptual de economía unitaria con costo por transacción, cliente, solicitud y token de IA; definiciones simbólicas y ficha de entradas para reproducibilidad, sin caso aplicado ni cifras generadas.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Economia unitaria.md`; `FP-49/Asignacion de costos.md`; `FP-49/Consolidado conceptual y preparacion de FP-171.md`; `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`; https://www.finops.org/framework/capabilities/unit-economics/; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/. Fuentes oficiales consultadas el 2026-09-17.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Lectura de todos los Markdown vigentes de FP-49, bitácora canónica y matriz; contraste con Definition y Functional Activities de Unit Economics y con las secciones conceptuales de tokens y Prompt Caching. Se verificaron alcance del numerador, periodo común, clientes únicos atendidos, transacciones exitosas frente a intentos técnicos, costos de fallos, denominador cero y no duplicación de entrada en caché. Relectura de los documentos generados: tabla de cuatro métricas y ocho columnas, encabezados, referencias y destinos de enlaces locales; fórmulas en notación compatible con Obsidian. `git diff --check` y `git diff --no-index --check` para los documentos no rastreados no reportaron errores de espacios; únicamente advertencias de conversión LF/CRLF. No se efectuó validación visual en Obsidian ni validación numérica con datos reales. Requisitos de Jira tomados del encargo, sin nueva consulta ni modificación de Jira.
- **Nivel de asistencia de IA (0-3):** 3 — investigación oficial, síntesis, formulación simbólica y redacción sustancial asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode; versión de la aplicación no disponible. Skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; resolución `paths-injected`.
- **Identificador del modelo (si aplica):** `openai/gpt-6-astra`, identificado por el entorno para esta ejecución y el orquestador; no se infirió a partir de registros anteriores.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  qué es el chargeback? puedes continuar con la otra tarea y verificar y realizar un consolidado para ya dejar listo las 2 fp y poder realizar la fp-171 y dejar un glosario de terminos
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Mantener el alcance conceptual paso a paso solicitado, sin caso aplicado; separar costo medio por token de tarifa del proveedor y de costo marginal; definir poblaciones explícitas sin convertirlas en requisitos universales. Preparar solo un inventario terminológico y una conexión conceptual para FP-171, no su entrega final.
- **Fundamento o evidencia de la decisión:** Alcance explícito vigente del usuario y fuentes oficiales verificadas. La matriz registra Unit Economics como 003 y Allocation como 002; la fuente sobre tokens no tiene fila independiente en el CSV consultado. Las fórmulas son elaboración matemática identificada del documento, no citas textuales. No se adoptaron tarifas ni generalizaciones numéricas del artículo de tokens.
- **Evidencia adjunta o enlace al historial:** Nuevo `FP-49/Economia unitaria.md` y consolidado en `FP-49/Consolidado conceptual y preparacion de FP-171.md`. Base conceptual preparada, pendiente de revisión humana. Los ejemplos numéricos reproducibles con datos verificados y compatibilidad aplicada con FP-52 permanecen sin cumplir por el alcance acordado; no puede declararse completa FP-169. FP-171 aún requiere glosario y mapa conceptual, integración con el informe y articulación con FP-53/FP-54/FP-56. No se modificaron FP-167/FP-168, Jira, estados ni matriz; no se realizó commit ni SDD.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 654 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para FP-169 y el consolidado preparatorio**.

## Registro 11 — FP-170 (verificación conceptual y consolidado)

- **Fuente / afirmación:** Clarificación de chargeback como imputación interna formal y diferenciación entre tasa unitaria de reparto, peso y cobertura de asignación; revisión del estado no asignado frente a la naturaleza compartida y la retención central.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Asignacion de costos.md`; `FP-49/Economia unitaria.md`; `FP-49/Consolidado conceptual y preparacion de FP-171.md`; `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/framework/capabilities/invoicing-chargeback/; https://www.finops.org/framework/capabilities/unit-economics/. Fuentes oficiales consultadas nuevamente el 2026-09-17.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se contrastaron Definition, estrategias de costos compartidos y métricas de Allocation con la distinción formal showback/chargeback de Invoicing & Chargeback. La identidad de conservación se comprobó algebraicamente: sumar `A_i=S*q_i/sum(q)` reproduce `S` cuando el denominador es positivo; no se usaron importes ni mediciones. Se explicitó el tratamiento central en la cobertura, la homogeneidad de periodo y unidades, conductores no negativos y conciliación de redondeos. Relectura de tabla de tres columnas, encabezados, enlaces y delimitadores matemáticos; comprobaciones de espacios con Git para archivos rastreados y no rastreados sin errores. `git diff --exit-code` confirmó ausencia de diferencias en los documentos de fases y personas. El antecedente de Tak et al. se conservó sin una nueva verificación del artículo. No se probó el renderizado en Obsidian.
- **Nivel de asistencia de IA (0-3):** 3 — contraste conceptual, ajustes puntuales y consolidación documental asistidos por IA.
- **Herramienta y versión (si aplica):** OpenCode; versión de la aplicación no disponible. Skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; resolución `paths-injected`.
- **Identificador del modelo (si aplica):** `openai/gpt-6-astra`, identificado por el entorno para esta ejecución y el orquestador; no se infirió a partir de registros anteriores.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  qué es el chargeback? puedes continuar con la otra tarea y verificar y realizar un consolidado para ya dejar listo las 2 fp y poder realizar la fp-171 y dejar un glosario de terminos
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Preservar el documento conceptual existente con correcciones acotadas; mantener la tasa de reparto y desambiguarla de la cobertura sin reintroducir cálculos aplicados. El costo central con destino identificado se considera asignado en la cobertura general declarada, no distribuido a productos. Chargeback no implica necesariamente un pago externo adicional.
- **Fundamento o evidencia de la decisión:** Definiciones oficiales verificadas y solicitud de consolidar las dos tareas manteniendo el alcance conceptual. La fila 002 conserva `https://framework.finops.org/framework/capabilities/allocation/`, diferente de la URL canónica consultada; Invoicing & Chargeback carece de fila independiente. Ambos vacíos se documentan sin modificar la matriz.
- **Evidencia adjunta o enlace al historial:** Correcciones en `FP-49/Asignacion de costos.md` y entrega preparatoria conjunta en `FP-49/Consolidado conceptual y preparacion de FP-171.md`. No se incorporó caso aplicado ni se declaró completa FP-170. FP-171 permanece pendiente como glosario sustentado y mapa conceptual; no se crearon enlaces de integración al informe o entregas compartidas inexistentes. Los cambios preexistentes de `.obsidian/` y la historia de la bitácora se preservaron. No se modificó Jira ni se realizó commit o SDD.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 654 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para las aclaraciones de FP-170 y el consolidado**.

## Registro 12 — FP-167 y FP-168 (publicación de issues en GitHub)

- **Fuente / afirmación:** Publicación de dos issues para documentar los entregables FP-167 y FP-168 declarados listos y revisados por el usuario, sin modificar sus contenidos ni atribuir una aprobación técnica de GitHub, integración en master o cumplimiento integral de la pauta académica.
- **Enlace, cita o ubicación de la evidencia:** https://github.com/TheVillegas/FEP-INVESTIGACION/issues/28 (FP-167); https://github.com/TheVillegas/FEP-INVESTIGACION/issues/29 (FP-168); https://asistec.atlassian.net/browse/FP-167; https://asistec.atlassian.net/browse/FP-168; `FP-49/fp-167 Las fases de FinOps.md`; `FP-49/fp-168 Roles y participacion.md`. Evidencia publicada contrastada en el commit `5746dde137854fc17ebf15111f86e00d881464f8`, bajo las rutas anteriores `FP-49/Las fases de FinOps.md` y `FP-49/Roles y participacion.md`; los nuevos nombres todavía corresponden a cambios locales.
- **Integrante responsable:** Pendiente de completar por el equipo; no se infiere una identidad académica a partir de la cuenta autenticada de GitHub.
- **Fecha (AAAA-MM-DD):** 2026-09-17. Hora local verificada después de confirmar la segunda publicación: `2026-09-17T13:58:06.3701137-03:00`.
- **Verificación realizada:** Se verificaron repositorio, rama predeterminada master, disponibilidad de issues, permiso WRITE, formulario `.github/ISSUE_TEMPLATE/research-documentation.yml` y etiqueta declarada existente `type:docs`. La consulta de duplicados abiertos y cerrados inicial no encontró resultados; antes de FP-168 se repitió su consulta y solo apareció #28 por una mención contextual, no como entrega equivalente. Los blobs de los archivos locales renombrados coincidieron con la evidencia publicada: `86b0b82d7d529d8b79993540a94b38a96c2488f9` para FP-167 y `d91fcfdf1a09dcc972133b6c2a80f87d395b8954` para FP-168. Se verificaron los siete controles del formulario, enlaces, trazabilidad y consentimiento; el escaneo de privacidad previo a cada intento no detectó hallazgos. Se realizó un único intento de creación por issue, con resultado final confirmado para ambas, estado OPEN y etiqueta `type:docs`.
- **Incidente de verificación y resolución:** La primera lectura de #28 presentó una discrepancia y detuvo las mutaciones. El diagnóstico de solo lectura reprodujo que PowerShell 5.1 decodificaba los bytes UTF-8 de GitHub CLI como CP850: el primer carácter alterado fue `U+00F3`, convertido en `U+251C U+2502`. La lectura explícita UTF-8 coincidió exactamente con el payload original conservado, normalizando únicamente CRLF y saltos de línea finales. SHA-256 normalizado de FP-167: `e6d1abd4eb5347c9b69647df49ea4b37c7c2b73554ee4f269d18a31083495640`. No se recreó ni editó #28. FP-168 se publicó con decodificación UTF-8 explícita limitada al proceso y comparación exacta de identidad, título y cuerpo; SHA-256 normalizado: `ce9719f63bf57f52e3e3821f4a056b4c94539e05bac2d47a1e1e18ab42640bfc`. No se cambiaron configuraciones globales de codificación.
- **Nivel de asistencia de IA (0-3):** 3 — redacción sustancial de las issues y de este registro, publicación y verificación automatizada; no se modificó el contenido académico de los entregables.
- **Herramienta y versión (si aplica):** OpenCode, versión de la aplicación no disponible; GitHub CLI 2.101.0; PowerShell 5.1 y Python 3.13.13 para diagnóstico y verificación. Skills `issue-creation`, `comment-writer` y `cognitive-doc-design`, resolución `paths-injected`.
- **Identificador del modelo (si aplica):** `openai/gpt-6-astra`, identificado por el entorno para esta ejecución y el orquestador; no se infiere a partir de modelos registrados en intervenciones anteriores.
- **Prompt exacto (texto o enlace a evidencia):** Solicitud humana y aclaración conservadas de esta interacción:

  ```text
  generame issues para la 167 y 168 que están listas, ahora yo verificaré las 169-171 t te comento despues
  ```

  ```text
  issues en github, mala mia
  ```

  Consentimiento explícito para ambas afirmaciones de seguridad y aclaración de rama principal:

  ```text
  Confirmo para ambas, la rama principal es master
  ```

  Instrucción delegada exacta de la continuación final, diferenciada de las palabras del usuario:

  ```text
  Issue28 outcome now definitively resolved confirmed via exact UTF8 readback matching original payload. Resume existing human authorization FP168 create ONLY, no recreate/edit #28. Same exact approved form/security checkbox scope and repository. Use UTF8 explicit decoding in process only not persistent global changes. Prior duplicate lookup reusable scoped FP168 while current (FP167 known existing); if need read-only fresh confirm no FP168 duplicate. Final privacy scan then one mutation attempt and verify. On confirmed append canonical traceability for both #28 and new FP168 URL recording exact human consent, diagnostic resolved CP850 mismatch, no edits FP169-171. Preserve dirty files. No rebase or commits your task. Return confirmed/no_write/unknown, URLs and exact file changed.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Documentar las entregas y la revisión declarada mediante issues abiertas, sin cierre automático, etiquetas de aprobación ni cambios de flujo. Conservar enlaces a una revisión realmente publicada y distinguir los renombres locales. Resolver la verificación de codificación antes de continuar; no reintentar ni duplicar la primera publicación.
- **Fundamento o evidencia de la decisión:** Autorización expresa del usuario, afirmación obligatoria del formulario confirmada para ambas issues y comparación exacta de los cuerpos publicados con sus payloads originales.
- **Evidencia adjunta o enlace al historial:** Issues #28 y #29 enlazadas anteriormente y este registro canónico. Los archivos temporales con cuerpos y respuestas se mantuvieron fuera del repositorio con permisos exclusivos del propietario, se eliminaron al finalizar y se verificó su ausencia. Se preservan íntegramente las entradas anteriores de esta bitácora y todos los cambios preexistentes del usuario. No se modificaron Jira, FP-169, FP-170 ni FP-171; no se realizó stage, commit, push ni rebase. La única modificación local de esta intervención es este registro añadido.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observaciones 664, 666 y 668 del proyecto `fep-investigacion`: detención inicial, diagnóstico resuelto y segunda publicación confirmada.
- **Validación humana (nombre, fecha y resultado):** Revisión del usuario confirmada en esta interacción para los entregables FP-167 y FP-168; consentimiento de seguridad para ambas issues confirmado el 2026-09-17. Nombre del responsable académico pendiente de completar. No se atribuye revisión humana previa del texto final de las issues ni validación global de otros entregables. FP-169, FP-170 y FP-171 permanecen pendientes de revisión del usuario.

## Registro 13 — Rebase de FP-49 y estado local de Obsidian

- **Fuente / afirmación:** Actualización de la base de FP-49 mediante rebase sobre `origin/master`, restauración del trabajo local conservado y retirada del seguimiento de Git de la configuración local de Obsidian, sin eliminar sus archivos del disco.
- **Enlace, cita o ubicación de la evidencia:** Rama `FP-49`; `.gitignore:4`; índice de Git; `info_mds/_trazabilidad/research-log.md`; referencias de respaldo indicadas a continuación.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17. Hora local de verificación: `2026-09-17 14:16:15 -03:00`.
- **Verificación realizada:** Árbol limpio antes del rebase; `git fetch origin` sin poda; rebase de tres commits sin conflictos; restauración mediante `git stash apply --index` del stash original sin conflictos. `origin/master` es ancestro del nuevo HEAD. Los blobs de Git restaurados de economía unitaria, la bitácora previa a este anexo y el workspace coincidieron con el stash original. Los dos Markdown renombrados conservaron sus blobs normalizados por Git; sus hashes de bytes sin filtros difieren del stash, con `core.autocrlf=true` ya existente, por lo que no se afirma identidad binaria de sus finales de línea. El PDF conservó su blob sin filtros. Las dos rutas antiguas siguen eliminadas del árbol de trabajo y sus reemplazos siguen sin stage. Antes de retirar Obsidian no había cambios preparados en el índice. Después, `git ls-files -- .obsidian` no devuelve archivos; `git check-ignore --no-index -v` confirma la regla existente para los cuatro archivos, y `Test-Path` confirma que siguen presentes. Comprobaciones `git diff --check` y `git diff --cached --check` sin errores antes del anexo. Estas verificaciones no constituyen revisión académica ni visual de los entregables.
- **Nivel de asistencia de IA (0-3):** 2 — mantenimiento técnico del repositorio y documentación de evidencia; sin generación de contenido académico.
- **Herramienta y versión (si aplica):** OpenCode, versión de la aplicación no disponible; Git y PowerShell. Skill `cognitive-doc-design`, resolución `paths-injected`.
- **Identificador del modelo (si aplica):** OpenCode y orquestador `openai/gpt-6-astra`, identificado por el entorno.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  ya cerré obsidian, pero igual puedes hacer un gitignore de la carpeta de datos de obsidian y da igual
  ```

  Contexto autorizado previamente: rebase de FP-49 sobre `origin/master`, preservando los cambios locales; retirada de Obsidian del índice sin borrar archivos locales y sin commit ni push.
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Reutilizar `.obsidian/`, ya presente en `.gitignore`, sin editar ni preparar ese archivo. Ejecutar únicamente `git rm --cached -r -- .obsidian` para dejar de rastrear sus cuatro archivos. Sus eliminaciones quedan preparadas en el índice para un futuro commit autorizado; los archivos locales se conservan y la retirada todavía no está publicada. No reaplicar automáticamente el segundo stash sobre el workspace restaurado.
- **Fundamento o evidencia de la decisión:** Autorización explícita del usuario y regla de exclusión existente; preservación del trabajo mediante rama de respaldo y dos stashes retenidos, sin `pop`, `drop`, `clear`, reset ni resolución inferida de conflictos.
- **Evidencia adjunta o enlace al historial:** HEAD anterior `5746dde137854fc17ebf15111f86e00d881464f8`; HEAD nuevo `95041f650e4afa7f5f2f996644e874d45da38d29`; `origin/master` verificado `b74652ad686b7f01e1d96f02b9c56d0e569128e5`. Respaldo `backup/FP-49-before-master-rebase-3028e38598554eb8a136e95feb5793c6`, que conserva el HEAD anterior. Stash original `e3cd44a41aef416c2710dc3b5ad629d49e47cd63`; segundo stash de modificación concurrente de Obsidian `c749f875faede55611dd9e5da9c7800bc0a342e8`. Divergencia resultante respecto de `origin/FP-49`: 35 commits locales y 3 remotos exclusivos. No se realizó commit adicional ni push; no se modificaron Jira, configuración de Git ni prosa de FP-169, FP-170 o FP-171. No se ejecutaron builds ni normalizadores. Este registro es el único anexo documental de la operación y conserva el Registro 12 restaurado.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 673 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** Autorización de la operación recibida; revisión humana del estado final pendiente. No se atribuye validación académica de los contenidos restaurados.

## Registro 14 — FP-170 (revisión conceptual de arquitectura)

- **Fuente / afirmación:** Revisión conceptual de solo lectura sobre la conveniencia de estructurar FP-170 a partir del dominio oficial *Understand Usage & Cost* y sus capacidades vigentes, con evaluación específica de la ubicación pedagógica de *showback* y *chargeback*. No se redactó ni modificó el entregable.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Asignacion de costos.md`; `papers/info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/domains/understand-usage-cost/; https://www.finops.org/framework/capabilities/data-ingestion/; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/framework/capabilities/reporting-analytics/; https://www.finops.org/framework/capabilities/anomaly-management/; https://www.finops.org/framework/capabilities/invoicing-chargeback/. Fuentes web oficiales consultadas el 2026-09-17.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17. Hora local de verificación: `2026-09-17 15:23:37 -03:00`.
- **Verificación realizada:** Se consultaron las cinco páginas oficiales solicitadas y, por ser necesaria para resolver la ubicación de *showback*/*chargeback*, la página vigente *Invoicing & Chargeback*. La página del dominio enumera exactamente cuatro capacidades: *Data Ingestion*, *Allocation*, *Reporting & Analytics* y *Anomaly Management*. Se verificó que *Allocation* define tres estrategias primarias —asignación, etiquetado/metadatos y costos compartidos—; que *Reporting & Analytics* incluye *showback reporting* entre sus casos de uso; y que *Invoicing & Chargeback* pertenece actualmente al dominio *Manage the FinOps Practice*, distingue la comunicación informativa de la imputación contable formal y declara que *showback* es necesario mientras *chargeback* depende de la política contable. También se comprobó que las capacidades intercambian requisitos y retroalimentación: no constituyen una secuencia rígida. *Anomaly Management* depende de datos, metadatos de asignación y análisis, y devuelve necesidades de metadatos y ajustes aprendidos, por lo que se recomienda representarla como bucle continuo. La página vigente usa *Data Ingestion*, mientras enlaza como antecedente la denominación anterior *Data Ingestion & Normalization*; *Reporting & Analytics* reemplaza la capacidad anterior *Data Analysis and Showback*; y *Allocation* enlaza antecedentes separados de *Cost Allocation (Metadata & Hierarchy)* y *Managing Shared Cost*. Validación académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 2 — contraste de fuentes oficiales y recomendación de arquitectura conceptual para decisión humana, sin redacción del entregable.
- **Herramienta y versión (si aplica):** OpenCode; versión de la aplicación no disponible. Skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; resolución `paths-injected`.
- **Identificador del modelo (si aplica):** Modelo padre de OpenCode `openai/gpt-6-astra`, indicado expresamente para esta intervención.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Read-only conceptual verification + canonical traceability append only, no deliverable edits yet. Repo C:\Users\joche\Jose_cosas\Uni\10_semestre\Fep2.1\FEP-INVESTIGACION. User wants to iterate allocation concept before unit economics and asks whether to structure it around official FinOps domain Understand Usage & Cost with Data Ingestion, Allocation, Reporting & Analytics, Anomaly Management, possibly basic showback/chargeback concepts before. Exact URLs provided:
  https://www.finops.org/framework/domains/understand-usage-cost/
  https://www.finops.org/framework/capabilities/data-ingestion/
  https://www.finops.org/framework/capabilities/allocation/
  https://www.finops.org/framework/capabilities/reporting-analytics/
  https://www.finops.org/framework/capabilities/anomaly-management/
  Use webfetch all five current official pages. Also verify official Invoicing & Chargeback page already known if necessary: https://www.finops.org/framework/capabilities/invoicing-chargeback/. Read CURRENT FP-49/Asignacion de costos.md and no other deliverable unless necessary. No edits to it now.
  Goal: Return concise Spanish architecture recommendation, not final prose. Verify exact current domain/capability relationship and beware official site update/version drift. Answer whether proposed approach is sound, what order is cognitively and conceptually best, and boundaries to avoid scope creep beyond FP170. Explicitly assess whether showback/chargeback should go before capabilities, inside Reporting, or after allocation/reporting as downstream communication/accounting outcomes. Distinguish pedagogical prereq from process sequence. Don't invent strict sequential workflow if framework says capabilities interact. Explain anomaly management as continuous feedback if evidence supports, not merely step4. Suggest exact proposed section outline for the document and approximate depth: domain intro, data ingestion brief, allocation detailed, reporting brief, anomaly brief, basic concepts where best, shared costs + rate. Protect next FP169: unit economics can be mentioned as downstream metric but not developed.
  Citations: exact URL and official heading/claim, paraphrase no fake quotations. Flag terminology changes (e.g. domain name or capability names). Max ~800 words response to parent.
  Traceability: canonical info_mds/_trazabilidad/research-log.md only; preserve entries, append next Registro14 conceptual review current Get-Date, exact user's latest prompt (can quote verbatim), current OpenCode parent model openai/gpt-6-astra, all URLs, findings/recommended structure, no deliverable edit/Jira/commit, pending user structure decision. Follow exact convention. If Git is dirty preserve all other changes and no stage.
  Skills load C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md. No registry. No CodeGraph for docs. Save significant verified framework discovery via mem_save project fep-investigacion if available. Return sources, recommendation, proposed outline, trace update, skill_resolution paths-injected.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Recomendar una arquitectura pedagógica que abra con el dominio, adelante una distinción mínima entre asignación, *showback* y *chargeback* para evitar confusiones, y luego desarrolle brevemente *Data Ingestion*, en profundidad *Allocation*, brevemente *Reporting & Analytics* y *Anomaly Management* como retroalimentación continua. Ubicar la explicación completa de *showback* después de asignación y dentro de la transición a reportes; presentar *chargeback* después como resultado contable posterior y externo al conjunto de capacidades del dominio. Reservar economía unitaria para FP-169 y mencionarla únicamente como uso descendente de costos asignados.
- **Fundamento o evidencia de la decisión:** La estructura vigente del dominio y las dependencias bidireccionales declaradas en las páginas oficiales. *Reporting & Analytics* produce *showback reporting*; *Invoicing & Chargeback* recibe asignación y reportes y pertenece a otro dominio; *Anomaly Management* necesita datos, metadatos y análisis, y aporta retroalimentación a asignación e ingestión. La organización propuesta distingue el orden de exposición del lector de un flujo operativo que el framework no declara lineal.
- **Evidencia adjunta o enlace al historial:** Recomendación arquitectónica entregada en el chat de esta interacción y este único anexo en la bitácora canónica. No se editó `FP-49/Asignacion de costos.md` ni otro entregable; no se modificó Jira; no se hizo stage, commit o push; y se preservaron todos los cambios locales preexistentes. Queda pendiente la decisión humana sobre la estructura antes de redactar el documento.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 676 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para la estructura propuesta de FP-170**.

## Registro 15 — FP-170 (implementación documental de la arquitectura de asignación)

- **Fuente / afirmación:** Reestructuración conceptual de `FP-49/Asignacion de costos.md` a partir del dominio oficial *Understand Usage & Cost*, con *Allocation* como núcleo, *showback* como resultado de *Reporting & Analytics*, *chargeback* como imputación formal posterior y *Anomaly Management* como retroalimentación continua.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Asignacion de costos.md`; `papers/info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/domains/understand-usage-cost/; https://www.finops.org/framework/capabilities/data-ingestion/; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/framework/capabilities/reporting-analytics/; https://www.finops.org/framework/capabilities/anomaly-management/; https://www.finops.org/framework/capabilities/invoicing-chargeback/. Fuentes oficiales consultadas el 2026-09-17.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17. Hora local previa a la edición: `2026-09-17 15:34:37 -03:00`.
- **Verificación realizada:** Lectura completa del documento de asignación y lectura de la convención y cola vigente de esta bitácora antes de editar. La revisión estructural posterior confirmó: título e introducción dentro del dominio; las cuatro capacidades vigentes y su relación interactiva, no lineal; tabla anticipatoria de conceptos; *Data Ingestion* como fundamento breve; desarrollo principal de *Allocation* con jerarquías, etiquetas, costos directos, compartidos y no asignados, conductores, tasa, cobertura y conservación; *Reporting & Analytics* con tratamiento completo de *showback*; *chargeback* separado como resultado contable fuera del dominio; anomalías como ciclo de retroalimentación; y una única relación compacta que difiere economía unitaria a FP-169. Se contrastó el diff únicamente de los dos archivos autorizados y se ejecutó `git diff --check` limitado a ellos. Esta verificación documental proporcional no constituye revisión académica humana ni revisión nativa automatizada.
- **Nivel de asistencia de IA (0-3):** 3 — reestructuración y redacción sustancial del documento, preservando el contenido conceptual útil existente y sin introducir casos empresariales ni datos aplicados.
- **Herramienta y versión (si aplica):** OpenCode, versión de la aplicación no disponible; Git y PowerShell para verificación. Skill `cognitive-doc-design`, resolución `paths-injected`.
- **Identificador del modelo (si aplica):** `openai/gpt-5.6-sol`, identificado por el entorno para esta ejecución.
- **Prompt exacto (texto o enlace a evidencia):** Confirmación humana e instrucción exacta de esta interacción:

  ```text
  Direct documentation implementation, no SDD. Repo C:\Users\joche\Jose_cosas\Uni\10_semestre\Fep2.1\FEP-INVESTIGACION. User confirmed relocation under papers/ is intentional; PRESERVE all moves/deletions/untracked content, Obsidian staged deletions, renamed docs, PDF, and all dirty state. No staging/commit/push/Jira. User wants to focus now on iterating cost allocation before unit economics and accepted approach based on FinOps domain Understand Usage & Cost plus basic showback/chargeback.
  Edit only:
  1) FP-49/Asignacion de costos.md
  2) papers/info_mds/_trazabilidad/research-log.md append Registro15 (new canonical moved location)
  Do not edit FP-49/Economia unitaria.md or any other content.
  First read current allocation doc fully and current tail/convention of research log. Preserve useful human-authored content and improve via smallest coherent restructure, not broad rewrite. Technical artifact language: neutral professional Spanish, not Rioplatense persona.
  Verified official evidence from previous task:
  - Understand Usage & Cost currently contains exactly Data Ingestion, Allocation, Reporting & Analytics, Anomaly Management. They interact; do NOT present a mandatory linear process.
  - Reporting & Analytics includes Produce Showback reporting.
  - Invoicing & Chargeback belongs to Manage the FinOps Practice; showback is necessary for FinOps, chargeback depends on accounting policy and does not automatically indicate higher maturity.
  - Anomaly Management depends on cost/usage data, allocation metadata, reporting and returns feedback; present continuous loop, not step4.
  - Current terminology changed: Data Ingestion (old Data Ingestion & Normalization), Reporting & Analytics (old Data Analysis and Showback), Allocation consolidates old Cost Allocation Metadata & Hierarchy + Managing Shared Cost. No need emphasize history unless references note benefits.
  Official URLs:
  https://www.finops.org/framework/domains/understand-usage-cost/
  https://www.finops.org/framework/capabilities/data-ingestion/
  https://www.finops.org/framework/capabilities/allocation/
  https://www.finops.org/framework/capabilities/reporting-analytics/
  https://www.finops.org/framework/capabilities/anomaly-management/
  https://www.finops.org/framework/capabilities/invoicing-chargeback/
  Document target architecture:
  - Clear title/introduction placing Allocation within Understand Usage & Cost; name all 4 capabilities and explicitly say relationship is interactive, not rigid sequence.
  - Brief basic concepts table early: allocation, direct cost, shared cost, unallocated cost, showback, chargeback. Keep anticipatory definitions short.
  - Data Ingestion as informational foundation, brief 2 paras, cost/usage/metadata, quality/granularity/normalization; no ETL/FOCUS deep dive.
  - Allocation is 50-60% and principal: strategy, hierarchy/labels/metadata, direct/unallocated, shared cost allocation, allocation drivers; rate/coverage/denominator if existing, conservation principle. Explain labels support allocation but are not the only mechanism. Do not invent company cases/data/calculations.
  - Reporting & Analytics brief, showback complete here; include visibility and assigned/unallocated views.
  - Chargeback separate after reporting as downstream formal accounting/budget imputation, not Reporting capability and outside domain; distinguish showback precisely.
  - Anomaly Management continuous feedback; brief.
  - Final relation to unit economics exactly one compact paragraph/sentence, deferring denominators/formulas/metrics to FP169.
  - Add references to exact official URLs and consultation date 2026-09-17, if doc existing citation convention permits. Claims must be attributable, no fake quotes.
  - Keep scope boundaries explicit. Avoid “pipeline” diagram implying strict sequence; if a conceptual relationship list/diagram is useful use arrows with feedback and caveat.
  - Keep document cognitively scannable but not shallow. No applied examples because user said don't invent applied cases.
  Trace Registro15: exact user confirmation latest prompt plus continuation context; acknowledge moves intentional, list only two edited files, sources, conceptual decisions, structural readback, no commit/push/stage/Jira, validation limitations. Preserve Registro14 and all prior entries.
  Use apply_patch only. Before patch verify target parent exists. After: read back both exact edited sections/files as needed, git diff limited to these two files, diff --check ONLY target files. Confirm no semantic diff in Economia and no other new changes from worker. Passive docs only: structural readback is complete proportional verification; do not start native review.
  Load C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md before work. If important decision/discovery save mem_save project fep-investigacion. Return status, concise summary, section outline, exact files, verification, diff stats and `skill_resolution: paths-injected`.
  ```

  Contexto de continuación aplicado: la verificación oficial del Registro 14 se reutilizó como evidencia ya contrastada; la relocalización bajo `papers/`, incluidos movimientos, eliminaciones, contenido no rastreado, eliminaciones preparadas de Obsidian, documentos renombrados y PDF, fue confirmada por el usuario como intencional y debía preservarse íntegramente.
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Adoptar una arquitectura pedagógica, no procesal, centrada en *Allocation*. Adelantar definiciones mínimas para reducir ambigüedad; mantener *Data Ingestion*, reportes y anomalías en profundidad proporcional; separar *chargeback* por pertenecer a otro dominio; y reservar el desarrollo de economía unitaria para FP-169.
- **Fundamento o evidencia de la decisión:** Las páginas oficiales citadas y la verificación documentada en el Registro 14 establecen la composición vigente del dominio, la producción de *showback reporting*, la ubicación de *Invoicing & Chargeback* y las dependencias con retroalimentación entre capacidades.
- **Evidencia adjunta o enlace al historial:** Se editaron exclusivamente `FP-49/Asignacion de costos.md` y `papers/info_mds/_trazabilidad/research-log.md`. Se preservaron el Registro 14 y entradas anteriores, así como toda la relocalización intencional y el estado sucio preexistente. No se modificó `FP-49/Economia unitaria.md` durante esta intervención; no se realizó stage, commit, push ni operación en Jira.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 678 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** Pendiente. La estructura y la redacción implementadas requieren revisión académica humana.

## Registro 16 — FP-170 (simplificación de tasa, cobertura y conservación)

- **Fuente / afirmación:** Simplificación de la sección sobre tasa, cobertura y conservación para explicar sus conceptos en lenguaje directo y mediante ejemplos breves, sin la formulación algebraica desarrollada previamente.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Asignacion de costos.md`; `papers/info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/capabilities/allocation/. Fuente oficial consultada nuevamente el 2026-09-17.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se comprobó en la página oficial vigente que la estrategia de costos compartidos describe conceptualmente repartos fijos, proporcionales y mediante indicadores sustitutos. La misma página también incluye, en bloques separados de indicadores, fórmulas porcentuales y un ejemplo numérico de reparto por gasto; no exige una fórmula de tasa unitaria. Se retiraron del documento las fórmulas en LaTeX, la derivación algebraica y la referencia a una ecuación en la cita de Tak et al.; se reemplazaron por explicaciones directas de tasa unitaria, conservación, cobertura, redondeos, ausencia de conductor válido, total de uso cero y tratamiento declarado de créditos o reembolsos. Los ejemplos de USD 1.000 repartidos entre 1.000 unidades y de USD 9.000 con destino sobre USD 10.000 totales son explícitamente hipotéticos e ilustrativos: no representan datos del proyecto ni de una empresa. Se realizó la relectura completa de la subsección editada y de este Registro 16, se revisó el diff y el resumen estadístico limitado a los dos archivos autorizados y se ejecutó `git diff --check` sobre esos mismos archivos. No se inició una revisión nativa por tratarse de una edición documental pasiva; la revisión académica humana permanece pendiente.
- **Nivel de asistencia de IA (0-3):** 3 — verificación de fuente, simplificación conceptual, redacción y trazabilidad asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode, versión de la aplicación no disponible; Git y PowerShell para verificación. Skill `cognitive-doc-design`, resolución `paths-injected`.
- **Identificador del modelo (si aplica):** Modelo padre `openai/gpt-5.6-sol`, indicado por el entorno para esta intervención.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Focused direct documentation edit, no SDD. Repo C:\Users\joche\Jose_cosas\Uni\10_semestre\Fep2.1\FEP-INVESTIGACION. User exact request: `simplifica la seccion de tasas, trata de explciar todo en palabras o ejemplos, evita usar formulas a no ser que sea estricto, porque la pagina fuente no veo que tenga formulas`. Verify official current Allocation page https://www.finops.org/framework/capabilities/allocation/ specifically whether formulas/rates are explicitly present; report source fact accurately. Then edit only:
  1) FP-49/Asignacion de costos.md — the focused subsection currently `### Tasa, cobertura y conservación` and any directly dependent wording/reference necessary.
  2) papers/info_mds/_trazabilidad/research-log.md — append next Registro16.
  Preserve user's intentional folder moves and all unrelated dirty state. No stage/commit/push/Jira. Do not edit Economia unitaria or other sections except the minimum dependency needed.
  Artifact language neutral professional Spanish. Apply smallest complete patch using apply_patch.
  Content goal:
  - Remove LaTeX/display formulas and algebraic derivation unless source strictly requires it (likely it does not).
  - Explain in plain language: allocation rate as a practical unit rate for distributing a selected shared-cost pool using a chosen driver; it is NOT allocation coverage.
  - One short explicitly hypothetical/illustrative example with simple numbers and no claim about project/company data: e.g. shared pool $1,000, total 1,000 usage units -> $1/unit; destination using300units receives300. Choose wording that is accessible and unambiguous.
  - Explain conservation plainly: amounts distributed plus intentionally retained amount must equal starting pool; reconcile rounding.
  - Explain coverage plainly with one short example: if9000 of10000 have valid destination, coverage90%; distinguish an explicitly central destination from product-level distribution.
  - Keep edge conditions concise: no usable driver or total zero means do not force division; retain/document until valid rule; credits/refunds can distort percentage and need declared treatment.
  - Keep Tak et al. paragraph if still valuable, tighten connection; do not claim the paper defines FinOps policy.
  - Do not reintroduce formula references in citations; note official Allocation source describes strategies conceptually rather than supplying these formulas, if appropriate.
  - Preserve citation numbering unless a reference is removed. Avoid unnecessary jargon. The section should be materially shorter than current lines56-86.
  Trace Registro16 at moved canonical path: exact user prompt, official URL verification, what removed/replaced, illustrative-example caveat, exact files, readback/diff check, no stage/commit/push/Jira, pending human review. Parent model openai/gpt-5.6-sol.
  Verification: full readback of edited subsection and Registro16, `git diff --check` limited targets, target diff/stat. Confirm no other new worker changes. Passive docs structural readback only; no native review.
  Load C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md first. Save significant decision via mem_save project fep-investigacion if available. Return concise summary and skill_resolution paths-injected.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Sustituir la notación algebraica por definiciones operativas y dos ejemplos hipotéticos breves; mantener separados tasa unitaria y cobertura; y conservar el aporte de Tak et al. únicamente como sustento técnico para distinguir uso atribuible y no atribuible, no como política FinOps.
- **Fundamento o evidencia de la decisión:** Solicitud explícita del usuario y contraste con la página oficial vigente de *Allocation*. La página contiene algunas fórmulas en sus bloques de indicadores, pero su estrategia de costos compartidos no exige la formulación algebraica retirada del documento.
- **Evidencia adjunta o enlace al historial:** Se editaron exclusivamente `FP-49/Asignacion de costos.md` y `papers/info_mds/_trazabilidad/research-log.md`. Se preservaron la relocalización intencional y todo el estado sucio ajeno a esta intervención. No se modificó `FP-49/Economia unitaria.md`; no se realizó stage, commit, push ni operación en Jira.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 681 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para la simplificación de tasa, cobertura y conservación**.

## Registro 17 — FP-169 (revisión conceptual posterior a la asignación)

- **Fuente / afirmación:** Revisión conceptual de solo lectura de FP-169 después de la reestructuración de FP-170, centrada en costo por transacción, cliente atendido, solicitud y token de IA, y en el costo unitario como métrica de producto. No se redactó ni modificó el entregable de economía unitaria.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Economia unitaria.md`; `FP-49/fp-170 Asignacion de costos.md`; `papers/info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/capabilities/unit-economics/; https://www.finops.org/framework/domains/quantify-business-value/; https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/; https://www.finops.org/wg/genai-finops-vs-cloud-finops/. Fuentes oficiales consultadas el 2026-09-17.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17. Hora local de verificación: `2026-09-17 16:03:47 -03:00`.
- **Verificación realizada:** Se leyó completamente el documento vigente de economía unitaria y se contrastó con la capacidad oficial *Unit Economics*, su dominio vigente *Quantify Business Value* y dos materiales oficiales de FinOps para GenAI. La capacidad ubica *Unit Economics* dentro de *Quantify Business Value*, diferencia métricas de eficiencia de recursos y métricas de negocio, y enumera como ejemplos costo por transacción, cliente, solicitud de servicio y token. También indica que las métricas deben definirse según objetivos organizacionales, documentar fuentes, supuestos e inclusiones de costo, analizarse como tendencias dentro de un alcance definido y apoyar decisiones de diseño, arquitectura, ubicación de cargas, empaquetado, precios, hoja de ruta, margen y valor. El material de GenAI confirma que entrada, salida, modalidad, modelo, caché y forma de acceso pueden tener tratamientos económicos diferentes, y recomienda desplazar la atención desde el precio bruto por token hacia el costo del caso de uso y del resultado exitoso. No se verificaron tarifas de proveedores ni se asumió que categorías comerciales concretas sean universales. Revisión académica humana pendiente.
- **Nivel de asistencia de IA (0-3):** 2 — contraste de fuentes oficiales, evaluación crítica del borrador y propuesta de arquitectura conceptual para decisión humana, sin edición del entregable.
- **Herramienta y versión (si aplica):** OpenCode, versión de la aplicación no disponible. Skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; resolución `paths-injected`.
- **Identificador del modelo (si aplica):** Modelo padre `openai/gpt-5.6-sol`, indicado por el entorno para esta intervención.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Read-only conceptual review + trace append, no deliverable edit yet. Repo C:\Users\joche\Jose_cosas\Uni\10_semestre\Fep2.1\FEP-INVESTIGACION. User asks: `ahora sí, revisemos de nuevo la: economía unitaria: costo por transacción, por cliente atendido, por solicitud y por token de IA; el costo unitario como métrica de producto.` They want to review FP169 after FP170 allocation. Current canonical trace log is `papers/info_mds/_trazabilidad/research-log.md`; relocation is intentional. Preserve all dirty state; no stage/commit/push/Jira.
  Read current `FP-49/Economia unitaria.md` fully. Fetch current official FinOps Framework sources, starting with likely canonical:
  - https://www.finops.org/framework/capabilities/unit-economics/
  - relevant current domain page linked from that capability (do not guess final domain; follow official page)
  - if official FinOps for AI material directly supports token-based unit cost, fetch it; otherwise state official evidence gap instead of inventing.
  Use only authoritative official source claims and distinguish our analytical recommendations. Verify current capability/domain names and any examples/KPIs. Beware site version drift.
  Return concise Spanish conceptual review and proposed architecture, no final prose and no edit to Economia. Assess each denominator:
  - transaction: define completed business event and scope/period consistency;
  - customer served: define active/served customer in period and beware heterogeneity/segment mix;
  - request: technical activity metric, possibly useful operationally but not automatically business value; define successful vs attempted and retries/internal requests;
  - AI token: input/output/cached/reasoning or provider categories may have different prices; don't naively aggregate if official/provider pricing differs; distinguish model API cost from total product-serving cost including supporting infrastructure where applicable. Do not assert unsupported categories as universal if official evidence absent.
  Explain unit cost as product metric: combines allocated cost numerator with product-relevant volume denominator; used for trend, product design/tradeoffs, pricing/margin/value conversations, not solely infrastructure efficiency. Maintain boundary with FP170: allocation provides numerator; FP169 chooses denominator and interpretation. Avoid duplicating allocation mechanics. Assess whether one generic strict ratio statement is useful or if words/examples are enough, considering user's immediately prior preference for plain language and formulas only when essential.
  Recommend section outline and what current content to retain/remove/clarify. No invented company data/cases; illustrative examples may be suggested but explicitly hypothetical. Include risks: denominator gaming, mix effects, quality/reliability tradeoff, partial cost scope, unit mismatch, low-volume volatility, token cost vs value.
  Traceability: append next Registro17 to `papers/info_mds/_trazabilidad/research-log.md`, exact user prompt, sources/claims, conceptual recommendation, no deliverable edit, pending human decision, no stage/commit/push/Jira. Model parent openai/gpt-5.6-sol. Preserve all prior entries.
  Load C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md. No CodeGraph for docs. Save important verified discovery via mem_save project fep-investigacion. Return sources, review, proposed outline, current-doc issues, trace update, `skill_resolution: paths-injected`.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Recomendar que FP-169 se organice desde el costo unitario como métrica de producto y no como catálogo de cocientes. FP-170 entrega el numerador mediante costos atribuibles y asignados; FP-169 selecciona un denominador coherente con la decisión de producto, define su población y explica la interpretación. Mantener una sola relación genérica —costo del alcance y periodo dividido por unidades del mismo alcance y periodo— y desarrollar las cuatro métricas principalmente con palabras, reglas de conteo, límites y riesgos. Tratar transacción y cliente atendido como métricas de negocio; solicitud y token como señales técnicas que requieren conexión explícita con resultados. Separar las clases de tokens cuando sus tarifas o semánticas difieran y presentar el agregado únicamente como promedio ponderado documentado, no como tarifa del proveedor ni como medida suficiente de valor.
- **Fundamento o evidencia de la decisión:** La capacidad oficial distingue métricas técnicas de eficiencia y métricas de negocio, exige alinearlas con objetivos, datos y decisiones, y prioriza tendencias dentro de alcances definidos. El dominio *Quantify Business Value* exige relacionar costo con valor y desempeño. Los materiales oficiales de GenAI muestran que el precio por token varía según clase, modalidad, modelo y acceso, y que el costo económico relevante debe observar el caso de uso completo y el resultado exitoso. La arquitectura propuesta aplica esas fuentes al borrador; las reglas concretas de conteo, segmentación y presentación son recomendaciones analíticas pendientes de aprobación humana.
- **Evidencia adjunta o enlace al historial:** Revisión conceptual y esquema propuesto entregados en el chat de esta interacción; este Registro 17 es la única modificación realizada. No se editó `FP-49/Economia unitaria.md` ni otro entregable, no se modificó Jira y no se realizó stage, commit o push. Se preservó íntegramente la relocalización intencional y todo el estado sucio preexistente.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 683 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para la arquitectura conceptual propuesta de FP-169**.

## Registro 18 — FP-169 (implementación documental de economía unitaria)

- **Fuente / afirmación:** Reestructuración conceptual de FP-169 para presentar la economía unitaria como métrica de producto dentro del dominio oficial *Quantify Business Value*, diferenciando métricas de negocio y técnicas y manteniendo a FP-170 como origen del costo asignado.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/Economia unitaria.md`; `FP-49/fp-170 Asignacion de costos.md`; `papers/info_mds/_trazabilidad/research-log.md`; https://www.finops.org/framework/capabilities/unit-economics/; https://www.finops.org/framework/domains/quantify-business-value/; https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/; https://www.finops.org/wg/genai-finops-vs-cloud-finops/. Fuentes oficiales consultadas el 2026-09-17.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se leyó completamente el documento vigente y la convención de esta bitácora antes de editar. La relectura estructural posterior confirmó: ubicación de *Unit Economics* dentro de *Quantify Business Value*; separación entre el numerador asignado por FP-170 y el denominador definido por FP-169; costo por transacción completada y por cliente atendido como métricas de negocio; costo por solicitud y por token como métricas técnicas; criterio explícito para intentos, éxitos, reintentos, llamadas internas y duplicados; preservación de categorías de tokens cuando su precio o semántica difieren; distinción entre costo del modelo o API y costo total de servir el producto; usos para tendencias y decisiones de producto; riesgos de interpretación; y ficha mínima de reproducibilidad. Se retiraron las cuatro formulaciones específicas y la identidad detallada de tokens, se dejó una única relación genérica expresada en palabras y se reemplazó la tabla de ocho columnas por una lista de comprobación compacta. Esta verificación documental proporcional no constituye revisión académica humana.
- **Nivel de asistencia de IA (0-3):** 3 — reestructuración, síntesis y redacción sustancial asistidas por IA a partir de fuentes oficiales verificadas.
- **Herramienta y versión (si aplica):** OpenCode, versión de la aplicación no disponible; Git y PowerShell para verificación. Skill `cognitive-doc-design`, resolución `paths-injected`.
- **Identificador del modelo (si aplica):** Modelo padre `openai/gpt-5.6-sol`, indicado por el entorno para esta intervención.
- **Prompt exacto (texto o enlace a evidencia):** Aprobación humana exacta de la estructura propuesta en el Registro 17:

  ```text
  aplicalo
  ```

  Contexto aplicado: intervención documental directa y enfocada, sin SDD; edición exclusiva de `FP-49/Economia unitaria.md` y anexo de este Registro 18; preservación de la relocalización intencional bajo `papers/`, eliminaciones preparadas de Obsidian, documentos renombrados, PDF y todo el estado sucio no relacionado; sin stage, commit, push ni Jira.
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Organizar FP-169 desde el costo por unidad como métrica de producto; usar el costo asignado por FP-170 sin duplicar sus mecanismos; definir de forma operativa las cuatro poblaciones; presentar las métricas técnicas como señales que requieren conexión con resultados; conservar la distinción entre costo directo y costo con cargas completas; y limitar la formulación a una relación genérica en lenguaje directo.
- **Fundamento o evidencia de la decisión:** Aprobación expresa del usuario y evidencia oficial verificada en el Registro 17. *Unit Economics* distingue métricas técnicas y de negocio y las vincula con decisiones; *Quantify Business Value* enmarca la relación entre costo y valor; los materiales de GenAI sustentan la preservación de categorías con tratamientos económicos diferentes y la evaluación del costo del caso de uso y del resultado, sin imponer comportamientos universales de proveedores.
- **Evidencia adjunta o enlace al historial:** Se editaron exclusivamente `FP-49/Economia unitaria.md` y `papers/info_mds/_trazabilidad/research-log.md`. Se preservaron los Registros 17 y anteriores, toda la relocalización intencional y el estado sucio ajeno a esta intervención. `FP-49/fp-170 Asignacion de costos.md` permaneció sin cambios. No se realizó stage, commit, push ni operación en Jira.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Observación 684 del proyecto `fep-investigacion`.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para la estructura y redacción implementadas en FP-169**.

## Registro 19 — Verificación de FP-167 a FP-170 y creación de FP-171

- **Fuente / afirmación:** Verificación estructural de los cuatro entregables conceptuales actuales y creación de un glosario y mapa de relaciones para integrarlos, manteniendo visibles las cuestiones académicas no resueltas.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/fp-167 Las fases de FinOps.md`; `FP-49/fp-168 Roles y participacion.md`; `FP-49/fp-169 Economia unitaria.md`; `FP-49/fp-170 Asignacion de costos.md`; `FP-49/Consolidado conceptual y preparacion de FP-171.md`; `FP-49/fp-171 Glosario conceptual y mapa de relaciones FinOps.md`; `papers/info_mds/_trazabilidad/research-log.md`; `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`.
- **Integrante responsable:** Pendiente de completar por el equipo.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se leyeron íntegramente los cuatro entregables actuales y el consolidado preparatorio antes de escribir. También se leyó la cola más reciente de esta bitácora y se verificó que el directorio padre `FP-49` existiera. Los cuatro documentos fueron leídos y revisados estructuralmente, y FP-171 se creó a partir de ellos. Se confirmó que la matriz de fuentes existe en la ruta indicada. La integración conserva las etiquetas oficiales de fases, personas, dominio y capacidades; distingue `Fuente oficial`, `Formulación local` e `Integración conceptual del proyecto`; marca como locales las formulaciones de tasa, cobertura, conservación y conteo; separa el ciclo de fases de la red de capacidades; y representa asignación, showback, chargeback, costo unitario, caso de uso y resultado exitoso sin imponer una secuencia operativa. Se mantuvieron visibles la discrepancia de seis Core Personas actuales frente a siete áreas históricas, la normalización pendiente de terminología, la discrepancia del host canónico de Allocation en la matriz, el handoff antiguo del consolidado y la revisión académica pendiente. No se pretendió resolver ninguno de esos puntos.
- **Decisiones relevantes tomadas:** Crear únicamente `FP-49/fp-171 Glosario conceptual y mapa de relaciones FinOps.md` y anexar este `Registro 19` al log canónico. No modificar ninguno de los cuatro entregables existentes ni el consolidado preparatorio. No inventar una séptima Core Persona oficial; no presentar las reglas locales de FP-169/FP-170 como definiciones normativas; no agregar fórmulas, datos aplicados, tarifas o resultados; no crear enlaces a FP-53, FP-54 ni FP-56; y mantener *chargeback* como imputación interna formal fuera del dominio `Understand Usage & Cost`.
- **Fundamento o evidencia de la decisión:** Lectura directa de los cuatro documentos y del consolidado actuales, validaciones oficiales ya registradas en los documentos y en los registros previos, y existencia comprobada de la matriz de fuentes. FP-167 enmarca el ciclo; FP-168 documenta personas; FP-170 aporta el costo asignado y el vocabulario de Allocation; FP-169 define denominadores, poblaciones e interpretación. Las flechas del mapa son dependencias, intercambios o retroalimentación conceptuales, no un orden obligatorio.
- **Nivel de asistencia de IA (0-3):** 3 — lectura estructural, integración conceptual, redacción del glosario y mapa, y trazabilidad asistidas por IA; revisión académica humana pendiente.
- **Herramienta y versión (si aplica):** OpenCode; skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; resolución `paths-injected`. Se usó `apply_patch` para la única creación y el único anexo autorizados.
- **Identificador del modelo (si aplica):** `openai/gpt-5.6-sol`, modelo padre de esta intervención.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  ya, ahora quiero que verifiques los 4 entregables y realices la fp-171
  ```

- **Contexto de continuación:** La intervención parte de la aprobación previa aplicada a FP-169 y de la confirmación humana de que las relocalizaciones bajo `papers/` son intencionales. Se preservaron las eliminaciones preparadas de `.obsidian`, los archivos no rastreados, los documentos renombrados y el consolidado modificado existente.
- **Evidencia adjunta o enlace al historial:** El archivo nuevo es `FP-49/fp-171 Glosario conceptual y mapa de relaciones FinOps.md`; el único registro actualizado es `papers/info_mds/_trazabilidad/research-log.md`. No se editaron los cuatro entregables actuales ni `FP-49/Consolidado conceptual y preparacion de FP-171.md`. No se hizo stage, commit, push, Jira ni revisión nativa; la verificación posterior queda limitada a lectura completa, `git diff --check` de los dos objetivos y revisión del estado de Git.
- **Validación humana (nombre, fecha y resultado):** **Pendiente para FP-171 y para las formulaciones locales, la normalización terminológica, la discrepancia de personas y el estado académico conjunto.**

## Registro 20 — Normalización documental de FP-167 a FP-171

- **Fuente / afirmación:** Normalización de los cinco entregables conceptuales para dejarlos como documentos de información verificada, con terminología canónica, exactamente seis *Core Personas* oficiales y límites de alcance alineados con la rúbrica de `docs/INV-01.md`.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/fp-167 Las fases de FinOps.md`; `FP-49/fp-168 Roles y participacion.md`; `FP-49/fp-169 Economia unitaria.md`; `FP-49/fp-170 Asignacion de costos.md`; `FP-49/fp-171 Glosario conceptual y mapa de relaciones FinOps.md`; `FP-49/Consolidado conceptual y preparacion de FP-171.md`; `papers/info_mds/_trazabilidad/research-log.md`; `docs/INV-01.md`; `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`; https://www.finops.org/framework/phases/; https://www.finops.org/framework/principles/; https://www.finops.org/framework/personas/; https://www.finops.org/framework/persona/engineering/; https://www.finops.org/framework/persona/finance/; https://www.finops.org/framework/persona/procurement/; https://www.finops.org/framework/persona/product/; https://www.finops.org/framework/persona/finops-practitioner/; https://www.finops.org/framework/persona/leadership/; https://www.finops.org/framework/domains/understand-usage-cost/; https://www.finops.org/framework/capabilities/data-ingestion/; https://www.finops.org/framework/capabilities/allocation/; https://www.finops.org/framework/capabilities/reporting-analytics/; https://www.finops.org/framework/capabilities/anomaly-management/; https://www.finops.org/framework/capabilities/invoicing-chargeback/; https://www.finops.org/framework/capabilities/unit-economics/; https://www.finops.org/framework/domains/quantify-business-value/; https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/; https://www.finops.org/wg/genai-finops-vs-cloud-finops/. Fuentes oficiales consultadas y registradas el 2026-09-17.
- **Integrante responsable:** No inferido por esta intervención.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se leyeron completos los cinco entregables, el consolidado, `docs/INV-01.md`, la matriz de fuentes y la cola vigente de esta bitácora antes de editar. Se reemplazaron los marcadores de borrador por el estado neutral `Documento de información verificada.`; se conservaron las limitaciones sobre ausencia de datos aplicados y resultados medidos; se normalizaron Engineering, Finance, Procurement, Product, FinOps Practitioner y Leadership como las seis *Core Personas*; se etiquetaron las reglas operativas de FP-169 y FP-170 como formulaciones del proyecto; se eliminaron referencias no utilizadas de FP-167; se normalizaron categorías de métricas; se actualizaron etiquetas canónicas en el mapa de FP-171; y se corrigió el enlace del consolidado hacia la bitácora relocalizada bajo `papers/`. La matriz no se modificó. La verificación no constituye validación experimental, resultados del proyecto ni revisión visual en Obsidian.
- **Nivel de asistencia de IA (0-3):** 3 — lectura, contraste documental, normalización terminológica, edición y trazabilidad asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode; skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; `skill_resolution: paths-injected`.
- **Identificador del modelo (si aplica):** `openai/gpt-5.6-sol`, modelo padre de esta intervención.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  1- corrige a las 6 personas core.
  2- ya son documentos verificados de informacion
  3- lo ideal es dejar todo en base a las fuentes y lo que pidee la rubrica
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Adoptar exactamente seis *Core Personas* oficiales; usar `Procurement (Adquisiciones)`, `Product (Producto)`, `FinOps Practitioner (Profesional de FinOps)` y `Leadership (Liderazgo)` sin crear una persona `Business`; marcar las reglas locales como formulaciones del proyecto; mantener los cinco documentos en alcance conceptual; y tratar la referencia histórica a siete áreas como no normativa.
- **Fundamento o evidencia de la decisión:** Clasificación vigente de *Core Personas* en las páginas oficiales, terminología y capacidades oficiales citadas, y requisitos de alcance de `docs/INV-01.md`. La matriz de fuentes se consultó como evidencia, pero no se modificó; tampoco se inventaron datos aplicados, tarifas, resultados ni conclusiones.
- **Evidencia adjunta o enlace al historial:** Se editaron exclusivamente los cinco entregables `FP-49/fp-167 Las fases de FinOps.md`, `FP-49/fp-168 Roles y participacion.md`, `FP-49/fp-169 Economia unitaria.md`, `FP-49/fp-170 Asignacion de costos.md` y `FP-49/fp-171 Glosario conceptual y mapa de relaciones FinOps.md`; el consolidado solo recibió la corrección de su ruta a la bitácora canónica; y este Registro 20 se anexó al log relocalizado. Se preservaron eliminaciones, renombres, contenido no rastreado y demás estado sucio preexistente. No se modificó la matriz, Jira ni los documentos fuente; no se realizó stage, commit o push.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** La información queda verificada documentalmente contra las fuentes citadas; no se infiere validación académica, experimental ni resultados aplicados del proyecto.

## Registro 21 — Limpieza residual de FP-167 a FP-171

- **Fuente / afirmación:** Limpieza editorial y terminológica de inconsistencias residuales en los documentos conceptuales de FP-167 a FP-171, manteniéndolos como documentos de información verificada y dentro del alcance conceptual acordado.
- **Enlace, cita o ubicación de la evidencia:** `FP-49/fp-167 Las fases de FinOps.md`; `FP-49/fp-169 Economia unitaria.md`; `FP-49/fp-170 Asignacion de costos.md`; `FP-49/fp-171 Glosario conceptual y mapa de relaciones FinOps.md`; `FP-49/fp-168 Roles y participacion.md` y `FP-49/Consolidado conceptual y preparacion de FP-171.md` solo como lectura de control; `docs/INV-01.md`; `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`; https://www.finops.org/framework/phases/; https://www.finops.org/framework/personas/; https://www.finops.org/framework/capabilities/unit-economics/.
- **Integrante responsable:** No inferido por esta intervención.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se añadió el título Markdown de FP-167 y se corrigieron únicamente la redacción y los acentos evidentes de la oración sobre demanda cloud, SaaS e IA; se confirmó la cobertura de Informar, Optimizar y Operar. En FP-169 se usaron las categorías oficiales `Business Unit Metrics` y `Resource Efficiency Unit Metrics`, conservando las cuatro métricas y sus explicaciones sin ampliar fórmulas ni casos. En FP-169 y FP-170 se eliminaron las etiquetas obsoletas `FP-48` y se remitió a la matriz vigente mediante su ruta exacta; la matriz no se editó. En FP-171 se eliminó la mención documental a una supuesta séptima área, se dejó explícita la clasificación oficial de seis *Core Personas*, se conservaron las conexiones representativas del mapa con una nota de alcance no exhaustivo y se actualizaron `Technical metric` y `Business metric` a `Resource Efficiency Unit Metric` y `Business Unit Metric`, con sus traducciones de trabajo. FP-168 y el consolidado preparatorio solo fueron leídos; no se alteró la historia previa de esta bitácora.
- **Nivel de asistencia de IA (0-3):** 3 — lectura, contraste de fuentes, edición puntual y trazabilidad asistidas por IA.
- **Herramienta y versión (si aplica):** OpenCode; skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; resolución `paths-injected`; cambios aplicados únicamente con `apply_patch`.
- **Identificador del modelo (si aplica):** `openai/gpt-5.6-sol`, modelo padre de esta intervención.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  1- corrige a las 6 personas core.
  2- ya son documentos verificados de informacion
  3- lo ideal es dejar todo en base a las fuentes y lo que pidee la rubrica
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Adoptar exactamente seis *Core Personas* oficiales, sin una persona `Business`; usar las categorías actuales de Unit Economics; corregir solo inconsistencias editoriales y referencias obsoletas; y conservar el alcance conceptual y las limitaciones ya declaradas por la rúbrica.
- **Fundamento o evidencia de la decisión:** Clasificación oficial de personas y fases de FinOps Foundation, categorías explícitas de la capacidad oficial *Unit Economics* —métricas de eficiencia de recursos y métricas de unidad de negocio—, ruta vigente de la matriz de fuentes y límites de `docs/INV-01.md`. No se añadieron TCO, precios regionales, análisis de sensibilidad, VAN/TIR, herramientas, cuestionario, datos aplicados ni contenido de autoría de IA.
- **Evidencia adjunta o enlace al historial:** Los archivos modificados fueron exactamente `FP-49/fp-167 Las fases de FinOps.md`, `FP-49/fp-169 Economia unitaria.md`, `FP-49/fp-170 Asignacion de costos.md`, `FP-49/fp-171 Glosario conceptual y mapa de relaciones FinOps.md` y este `papers/info_mds/_trazabilidad/research-log.md`. No se modificaron `FP-49/fp-168 Roles y participacion.md`, `FP-49/Consolidado conceptual y preparacion de FP-171.md` ni `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`. No se realizó stage, commit, push, Jira ni restauración de rutas antiguas.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Registro interno del proyecto; identificador no incorporado para evitar datos de entorno.
- **Validación humana (nombre, fecha y resultado):** La comprobación fue documental y estructural. Permanece pendiente la validación académica humana, cualquier validación experimental o aplicada, y la comprobación visual nativa en Obsidian; no se atribuyen resultados del proyecto.

## Registro 22 — Acotación de una formulación no respaldada en FP-167

- **Fuente / afirmación:** Se acotó el detalle no respaldado que vinculaba el consumo cloud con SaaS, IA y un supuesto formato “elástico”; se dejó una formulación neutral y respaldada por la página oficial de fases sobre la variabilidad del consumo de la nube, la revisión periódica de la información de costos y uso, la identificación de cambios y la orientación de decisiones [1].
- **Enlace, cita o ubicación de la evidencia:** `FP-49/fp-167 Las fases de FinOps.md`, sección `Informar`; `papers/info_mds/_trazabilidad/research-log.md`, Registro 22; [1] FinOps Foundation, FinOps Phases: https://www.finops.org/framework/phases/.
- **Integrante responsable:** No inferido por esta intervención.
- **Fecha (AAAA-MM-DD):** 2026-09-17.
- **Verificación realizada:** Se leyó el párrafo vigente de `Informar` y la cola de esta bitácora antes de editar. Se reemplazó únicamente la oración sobre SaaS, IA y el formato “elástico” por `Como el consumo de la nube puede variar, la información sobre costos y uso debe revisarse periódicamente para identificar cambios y orientar las decisiones [1].`; se conservaron el título, el estado y toda la demás prosa de FP-167. Después del parche se realizó lectura estructural del párrafo cambiado y de este Registro 22, se comprobó mediante búsqueda que FP-167 ya no conserva una afirmación específica sobre SaaS/IA y se ejecutó `git diff --check` limitado a los dos archivos objetivo. No se realizaron otros cambios.
- **Nivel de asistencia de IA (0-3):** 3 — lectura, contraste de fuente, edición puntual y trazabilidad asistidos por IA.
- **Herramienta y versión (si aplica):** OpenCode; skill `cognitive-doc-design` cargado desde `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md`; `skill_resolution: paths-injected`; cambios aplicados únicamente con `apply_patch`.
- **Identificador del modelo (si aplica):** `openai/gpt-5.6-sol`, modelo padre de esta intervención.
- **Prompt exacto (texto o enlace a evidencia):**

  ```text
  Small direct documentation cleanup, no SDD. Repo C:\Users\joche\Jose_cosas\Uni\10_semestre\Fep2.1\FEP-INVESTIGACION. User's standing decisions: six official Core Personas; FP167–FP171 are verified information documents; content must be based on official sources and rubric. Preserve all unrelated dirty state and intentional moves/renames. No stage/commit/push/Jira.
  Edit only `FP-49/fp-167 Las fases de FinOps.md` and append next `Registro 22` to `papers/info_mds/_trazabilidad/research-log.md`. Load `C:\Users\joche\.config\opencode\skills\cognitive-doc-design\SKILL.md` first.
  Read current FP167 line around the Informar section and log tail. Replace only the current uncited/over-specific sentence about SaaS/IA and `formato elástico` with a concise, neutral, source-backed formulation about variable cloud consumption requiring periodic review of cost/usage information to identify changes and guide decisions, citing [1]. Do not add SaaS/AI claims if not directly supported by the cited phases page. Keep title/status and all other prose unchanged.
  Append Registro22 preserving all prior entries, stating that this unsupported detail was narrowed to source-backed wording, exact user directive context, exact files, no other edits, no stage/commit/push/Jira, structural readback and diff check, parent model `openai/gpt-5.6-sol`, skill path/resolution, and no experimental/applied claims. Do not alter historical records.
  After patch: read the changed paragraph and Registro22; grep FP167 for SaaS/IA only if confirming no over-specific claim remains; run git diff --check limited to the two targets; ensure no other files changed by worker. Passive documentation structural verification only. Save significant discovery to Engram project `fep-investigacion` if available. Return exact change and `skill_resolution: paths-injected`.
  ```

- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Reducir el detalle no respaldado a una formulación directamente apoyada por [1], sin incorporar afirmaciones específicas sobre SaaS o IA; conservar sin cambios el título, el estado y la demás redacción del documento.
- **Fundamento o evidencia de la decisión:** La página oficial de fases vincula la revisión continua de Informar con el carácter variable del consumo tecnológico y con el uso de información precisa para validar impactos y orientar decisiones basadas en datos. La redacción aplicada se mantiene conceptual y no afirma datos, resultados, validación experimental ni aplicación en el proyecto.
- **Evidencia adjunta o enlace al historial:** Se editaron exclusivamente `FP-49/fp-167 Las fases de FinOps.md` y `papers/info_mds/_trazabilidad/research-log.md`; se preservaron el estado sucio no relacionado y los movimientos o renombres intencionales. No se modificó ningún otro archivo. No se realizó stage, commit, push ni Jira.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** Descubrimiento significativo guardado en Engram del proyecto `fep-investigacion`, sin incorporar identificadores de entorno.
- **Validación humana (nombre, fecha y resultado):** No se infiere validación humana, experimental o aplicada, ni resultados del proyecto. La verificación de esta intervención fue únicamente documental y estructural.
