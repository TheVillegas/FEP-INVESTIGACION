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

## Decisiones y límites del trabajo

- Las síntesis se basan exclusivamente en el PDF correspondiente. El CSV se usa únicamente para clasificar y comprobar discrepancias bibliográficas; INV-01 se usa solo para la relación preliminar.
- La sección “Conclusión del paper” resume lo sostenido por sus autores y no constituye una conclusión ni recomendación del grupo.
- El texto extraído conserva el contenido textual por página. Figuras, diseño multicolumna, tablas y ecuaciones pueden perder fidelidad visual; cada documento incluye una advertencia antes de la extracción.
- No se generaron análisis comparativos, recomendaciones, aporte propio, discusión crítica ni preguntas del cuestionario, porque las reglas reservan esas partes a autoría humana.
- **Estado de validación humana global:** pendiente.
