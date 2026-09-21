# Bitácora de investigación — FP-189, verificación de fuentes para FP-190

> **Estado:** trazabilidad de asistencia IA para un paquete de verificación. No habilita trasladar texto asistido a análisis comparativo, criterios, conclusiones, recomendaciones, aporte propio/discusión crítica ni cuestionario; esas piezas requieren autoría y validación humana.

## Registro

- **Fuente / afirmación:** Verificación documental acotada de las tres fuentes seleccionadas humanamente para FP-190: Cho (guardrails temporales), Fragiadakis et al. (PricingOps) y Feitosa et al. (conciencia de costos en IaC). Se registraron identidad bibliográfica, DOI, fechas, método/muestra, cifras con unidades y contexto, límites, tensiones de alcance, solapamiento y estado de procedencia de bases.
- **Enlace, cita o ubicación de la evidencia:** [`../fp-189/verificacion-fuentes-fp190.md`](../fp-189/verificacion-fuentes-fp190.md) y suplemento [`../../FP-48 TINV02/verificacion-fp76-tendencias.md`](../../FP-48%20TINV02/verificacion-fp76-tendencias.md).
- **Integrante responsable:** Pendiente de asignación y aprobación humana.
- **Fecha (AAAA-MM-DD):** 2026-09-18.
- **Verificación realizada:** Se extrajo texto directamente de los tres PDF locales con `pdftotext -layout`, se contrastó contra sus Markdown y se verificaron DOI, fechas y paginación: Cho 48 pp.; Fragiadakis et al. 20 pp.; Feitosa et al. 14 pp. Se calcularon SHA-256 de los PDF: `2918b2c7ab97313a8fc8eab935b5aa17159fdcdd5044c8fb243e023cd29f22a9` (Cho), `c1d5ef901666cfed798ff7e16afc708e6e1405356c0d3c893651010e6d7b0422` (Fragiadakis et al.) y `75b16a7c89c72d5be9edc9fcd3d6f4f8157d68c0cbb809e1d3cceb00d2064cfd` (Feitosa et al.). Para GeoScale, Smendowski & Nawrocki y Stupar & Huljenic se consultó únicamente metadata DOI por content negotiation; el registro DOI de Stupar además expuso resumen. No se leyó texto completo de esos tres externos.
- **Nivel de asistencia de IA (0-3):** 3 — generación sustancial de documentación de trazabilidad y síntesis de evidencia. La revisión de los originales, interpretación académica y toda redacción académica final siguen siendo humanas.
- **Herramienta y versión (si aplica):** Pi coding agent; versión/modelo no expuestos de forma segura. Herramientas locales: lectura de archivos, Bash, `pdftotext`, `sha256sum`, Python y consulta DOI con `curl`.
- **Identificador del modelo (si aplica):** No expuesto de forma segura en esta sesión.
- **Resumen del prompt:** Crear un paquete de verificación independiente para las tres tendencias de FP-190 usando PDF y Markdown locales; comprobar identidad, fechas, métodos/muestras, cifras/unidades/contexto, límites, solapamiento y resultado; conservar GeoScale, Smendowski & Nawrocki y Stupar & Huljenic como corroboración secundaria sin sobreafirmar; registrar que Google Scholar es procedencia del libro y que Scopus/WoS/SciELO no se verificaron directamente; no redactar análisis comparativo ni secciones de autoría humana.
- **Decisión relevante tomada a partir de la interacción (o "sin decisión"):** Sin decisión académica. Se aplicó la regla de trazabilidad: afirmaciones de las tres fuentes locales quedan `Verificada con límites`; procedencia Scopus/WoS/SciELO queda `Pendiente`; evidencia externa se limita explícitamente a metadata o metadata+resumen.
- **Fundamento o evidencia de la decisión:** PDF locales citados abajo y delimitaciones de página en el paquete FP-189. La matriz FP-48 registra las fuentes como obtenidas vía Google Scholar; esta ejecución no verificó registros de artículo en Scopus/WoS/SciELO, por lo que no declara ni niega indexación.
- **Evidencia adjunta o enlace al historial:** Este registro; `docs/fp-189/verificacion-fuentes-fp190.md`; `FP-48 TINV02/verificacion-fp76-tendencias.md`; historial Git y comprobaciones de ruta/diff de la ejecución.
- **Registro de ENGRAM Cloud (enlace o identificador, si aplica):** No disponible en esta ejecución.
- **Validación humana (nombre, fecha y resultado):** **Pendiente.** Una persona responsable debe: revisar cada PDF y página de cifra antes de uso; verificar directamente registro/procedencia en Scopus, WoS o SciELO según exigencia docente; confirmar la lectura primaria de las fuentes externas si se pretende usarlas más allá de metadata/resumen; y aprobar o corregir límites/solapamientos. Hasta esa evidencia, el paquete no habilita uso académico final.

## Rutas primarias consultadas

- `FP-48 TINV02/Papers academicos - FP-48/03_Cho_2026_FinOps_Budget_Optimization.pdf`
- `FP-48 TINV02/Papers academicos - FP-48/markdown/03_Cho_2026_FinOps_Budget_Optimization.md`
- `FP-48 TINV02/Papers academicos - FP-48/applsci-14-11946-v2.pdf`
- `FP-48 TINV02/Papers academicos - FP-48/markdown/applsci-14-11946-v2.md`
- `FP-48 TINV02/Papers academicos - FP-48/Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications An exploratory study.pdf`
- `FP-48 TINV02/Papers academicos - FP-48/markdown/Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications An exploratory study.md`
- `FP-48 TINV02/TINV_Matriz_de_Fuentes_FP-126_actualizada_2026-09-15.xlsx`

## Límites conocidos

- La comprobación bibliográfica primaria es local y no prueba indexación de base de datos.
- Las cifras de Cho son del simulador/traza calibrada y deben conservar su protocolo; las de Fragiadakis et al. son bundles/precios de una instantánea Q3–Q4 2023; las de Feitosa et al. son unidades textuales de repositorios Terraform abiertos, no gasto realizado.
- La corroboración externa no proporciona una segunda verificación de método, muestra o resultado hasta que una persona lea y registre los textos primarios.
