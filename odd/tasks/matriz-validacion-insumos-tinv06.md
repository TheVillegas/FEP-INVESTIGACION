# Matriz de validación de insumos TINV-06

## Objetivo

Consolidar en un único workbook los inputs usados por FP-182 a FP-188, su valor, unidad, estado de evidencia, fuente, fecha, dependencia Jira y acción pendiente.

## Problema y por qué

Los entregables contienen datos oficiales, supuestos del escenario académico, proxies públicos, exclusiones justificadas y validaciones humanas pendientes. Sin una matriz común, es fácil presentar un proxy como dato real o perder la trazabilidad entre tareas.

## Alcance autorizado

- Leer los artefactos locales del repositorio.
- Crear un workbook nuevo; no modificar los modelos fuente.
- Completar todo input respaldable y mantener visibles los faltantes reales.
- Actualizar la sección 05 del informe LaTeX en `C:/Users/Abduzcan0/Downloads/Trabajo_de_Investigación___OneByte/Secciones/05-CasoAplicado-TINV.tex` para reflejar la matriz y declarar límites de la evidencia.

## Restricciones

- No convertir ausencias en cero.
- No presentar supuestos o proxies como mediciones reales.
- Conservar la fecha y el artefacto fuente.
- Usar los papers solo como sustento metodológico, no como cotización.

## Tareas

- [x] `MAT-01` Extraer inputs y estados de FP-172 y FP-182 a FP-188.
  - Evidencia: artefactos Markdown y XLSX inspeccionados en el repositorio.
- [x] `MAT-02` Construir la matriz consolidada con resumen y fuentes.
  - Evidencia: workbook de una hoja con 94 registros, filtros, validación de estado y conteos por categoría.
- [x] `MAT-03` Verificar fórmulas, totales, estados y ausencia de errores.
  - Evidencia: 94 IDs únicos; conteos reconciliados 25 oficiales, 25 supuestos, 3 proxies, 6 estimaciones, 15 derivados, 17 pendientes y 3 no aplicables; escaneo con 0 errores.
- [x] `MAT-04` Renderizar y revisar visualmente todas las hojas.
  - Evidencia: se revisaron los bloques superior, medio y final de la hoja `Matriz`; encabezados, fechas, estados y valores permanecen legibles.
- [x] `MAT-05` Actualizar la sección 05 del informe con el estado de evidencia y las limitaciones financieras.
  - Evidencia: `C:/Users/Abduzcan0/Downloads/Trabajo_de_Investigación___OneByte/Secciones/05-CasoAplicado-TINV.tex` sincronizada con los 94 registros y siete estados de evidencia; compilación XeLaTeX exitosa en copia temporal y revisión visual de las cinco páginas de la sección (PDF, páginas 8–12). Se amplió el presupuesto editorial a cinco páginas y se evitó dejar aislado el título de §5.5.
- [x] `MAT-06` Entregar el PDF completo compilado desde la fuente LaTeX actualizada.
  - Evidencia: `output/pdf/onebyte-informe-actualizado-2026-09-21.pdf`; se reabrió con `pdfinfo` (16 páginas, A4), se comprobó la presencia de los contenidos de la sección y se revisaron visualmente las páginas 7–13. El `main.pdf` original se conservó sin cambios.
- [x] `MAT-07` Clasificar las 17 validaciones según la evidencia realmente disponible en el repositorio.
  - Evidencia: `docs/fp-188/auditoria-validaciones-pendientes.md` distingue 13 registros con precarga parcial y 4 sin valor medido o aprobado reutilizable.
- [x] `MAT-08` Completar los valores provisionales respaldados y definir un procedimiento reproducible para cada faltante.
  - Evidencia: `docs/fp-188/plan-cierre-17-validaciones.md` registra valor disponible, límite, método de cierre, evidencia mínima y destino para los 17 IDs.
- [x] `MAT-09` Verificar que ningún supuesto, proxy o decisión académica quede presentado como medición o aprobación productiva.
  - Evidencia: verificación automatizada de presencia de los 17 IDs, revisión de estados y `git diff --check` sin errores.
- [x] `MAT-10` Precargar en la matriz XLSX los valores respaldados de las 13 validaciones con evidencia parcial.
  - Evidencia: `docs/fp-188/matriz-validacion-insumos-tinv06.xlsx`; se completaron valor, unidad, fuente y acción restante sin cambiar el estado formal.
- [x] `MAT-11` Verificar que las 13 filas conserven estado pendiente y que las cuatro validaciones sin valor permanezcan vacías.
  - Evidencia: inspecciones Artifact Tool de `A34:M40`, `A64:M64`, `A80:M83` y `A95:M104`; 17 estados `Pendiente humano`, VAL-01/02/08/09 vacías y escaneo de fórmulas con cero errores.

## Criterios de aceptación

- Cada fila tiene ID, grupo, input, valor, unidad, estado, fuente, fecha, Jira, acción pendiente e impacto.
- Los valores oficiales, supuestos, proxies, exclusiones y pendientes se distinguen visualmente.
- El resumen cuenta los estados mediante fórmulas.
- El archivo final se exporta como XLSX y pasa inspección de errores y revisión visual.

## Verificaciones aplicables

- Reconciliación puntual con FP-183, FP-184, FP-185, FP-186 y FP-187.
- Recálculo y escaneo de errores de fórmula.
- Render de cada hoja y revisión de legibilidad.

## Progreso y siguiente paso

La matriz XLSX quedó actualizada y verificada con 13 precargas respaldadas. VAL-01, VAL-02, VAL-08 y VAL-09 permanecen vacías porque el repositorio no contiene medición o aprobación reutilizable. Las 17 conservan estado `Pendiente humano`, por lo que ninguna se presenta como validación productiva cerrada. El siguiente paso es obtener la evidencia indicada en `docs/fp-188/plan-cierre-17-validaciones.md`.
