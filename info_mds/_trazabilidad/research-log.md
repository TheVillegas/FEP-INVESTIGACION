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
