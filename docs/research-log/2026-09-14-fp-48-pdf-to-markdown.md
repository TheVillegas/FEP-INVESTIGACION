# Bitácora de investigación

## Registro

- **Fuente / afirmación:** Conversión mecánica de 14 PDFs académicos de FP-48 a archivos Markdown para su revisión humana posterior. No se generó análisis académico ni contenido para secciones de autoría humana.
- **Enlace, cita o ubicación de la evidencia:** `FP-48 TINV02/Papers academicos - FP-48/` (fuentes PDF) y `FP-48 TINV02/Papers academicos - FP-48/markdown/` (14 entregables Markdown).
- **Integrante responsable:** Pendiente de asignación humana.
- **Fecha (AAAA-MM-DD):** 2026-09-14.
- **Verificación realizada:** `find` confirmó 14 PDFs y 14 `.md`; `wc -m` confirmó que cada salida contiene más de 200 caracteres (mínimo: 19.270).
- **Nivel de asistencia de IA (0-3):** 1 — asistencia superficial: ejecución y trazabilidad de una conversión documental solicitada.
- **Herramienta y versión (si aplica):** `~/bin/tomd` (versión no expuesta por el ejecutable); skill `doc-to-markdown` v1.0; motor MarkItDown (versión no reportada).
- **Identificador del modelo (si aplica):** `gpt-5.6-terra` (PI_MODEL); proveedor: `openai-codex` (PI_PROVIDER).
- **Prompt exacto (texto o enlace a evidencia):**
  > Hola oye sabes que quiero empezar a revisar el trabajo de investigacion para ello te deje los documentos de FP-48 /home/thevillegas/Documentos/UNIVERSIDAD-CURSOS/FEP-INVESTIGACION/FP-48\ TINV02
  > El tema es que los papers los debemos transformar a mardown con nuestra skill y la matriz de investigacion es formato excel. Ademas de que no se si estoyy seguro si tenemos actualizados y enrollados al proyecto de fep mediante /home/thevillegas/Documentos/UNIVERSIDAD-CURSOS/FEP-INVESTIGACION/docs/onboarding-engram-cloud-windows.md
  > Mediante nuestro mmismo archivo, ademas de que creo que al abrir una terminal creo que no nos carga de forma automatica el token como pasa con el proyecto de fep, por lo cual la sincroizacion de nuestras memorias al proyecto engram cloud no sera fidedigna. Una vez realizado esos dos trabajos la idea es poder empezar a empezar la tarea FP-147, Y recordar que para todo debemos dejar explicito /home/thevillegas/Documentos/UNIVERSIDAD-CURSOS/FEP-INVESTIGACION/Anexo\ Declaración\ de\ Uso\ de\ IA\ -\ ONEBYTE\ -\ TI-06.md
  > Por lo cual se usa engram cloud para tener mejor control del prompt y las desiciones que toma la IA, te parece?
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Se aplicó exclusivamente el flujo de conversión solicitado: conservar PDFs sin cambios, generar Markdown en `markdown/`, preservar los nombres identificadores de las fuentes y marcar como falla cualquier salida menor a aproximadamente 200 caracteres. No se tomó ninguna decisión académica.
- **Fundamento o evidencia de la decisión:** Solicitud explícita de conversión y reglas de `doc-to-markdown`; las 14 conversiones finalizaron correctamente y superaron el umbral de longitud.
- **Evidencia adjunta o enlace al historial:** `FP-48 TINV02/Papers academicos - FP-48/markdown/`; este registro.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** No disponible en esta ejecución.
- **Validación humana (nombre, fecha y resultado):** **Pending human validation** — revisar fidelidad de extracción, tablas, ecuaciones y referencias contra cada PDF antes de usar los archivos en el trabajo académico.

> Según el punto 6.1, no registrés contenido generado por IA para el análisis comparativo y los criterios, las conclusiones y recomendaciones, el párrafo de aporte propio o discusión crítica, ni la redacción y justificaciones del cuestionario: esas partes requieren autoría humana exclusiva.
