# Sección 05 LaTeX — Caso aplicado TINV-06

## Objective
Redactar y verificar la sección 05 del informe académico OneByte usando los resultados trazables de FP-182 a FP-188, sin presentar supuestos o proxies como mediciones reales.

## Problem
`Secciones/05-CasoAplicado-TINV.tex` contiene únicamente encabezados. Los resultados existen en artefactos separados y deben sintetizarse en una narrativa académica compacta, coherente y compilable.

## Why
El informe necesita exponer arquitectura, TCO, optimizaciones, comparación regional, sensibilidad y evaluación financiera del caso aplicado.

## Scope
- Editar únicamente la sección 05 del proyecto LaTeX y los archivos auxiliares estrictamente necesarios para compilar/verificar.
- Integrar FP-182 a FP-188.
- Distinguir precios oficiales, supuestos de escenario, proxies financieros y validaciones pendientes.
- Generar y revisar el PDF compilado.

## Constraints
- No inventar usuarios, latencia, consumo observado, SLA, WACC ni costos internos.
- Mantener los resultados en USD y horizonte de 60 meses.
- No modificar los modelos FP-182 a FP-188.
- No presentar el escenario ilustrativo como arquitectura productiva aprobada.
- No completar la discusión/conclusión de la sección 06.

## Authorized scope
- Modificar `C:/Users/Abduzcan0/Downloads/Trabajo_de_Investigación___OneByte/Secciones/05-CasoAplicado-TINV.tex`.
- Compilar el proyecto LaTeX y corregir errores de la sección 05.
- Crear artefactos temporales de renderizado para QA.

## Acceptance criteria
- [x] La sección desarrolla todos sus apartados con narrativa, tablas y resultados.
- [x] Los valores concilian con FP-182 a FP-188.
- [x] Cada dato se identifica como oficial, supuesto, proxy o pendiente cuando corresponde.
- [x] La selección regional se distingue de la rentabilidad de la optimización FinOps.
- [x] El proyecto compila con XeLaTeX sin errores bloqueantes.
- [x] El PDF renderizado no presenta texto cortado, solapamientos ni tablas ilegibles en la sección 05.

## Applicable checks
- Compilación repetida con `latexmk -xelatex`.
- Revisión de log para errores, referencias rotas y cajas desbordadas.
- Extracción de texto para comprobar cifras y encabezados.
- Renderizado de las páginas de la sección 05 a PNG y revisión visual.

## Progress
- [x] LTX05-01 Consolidar valores y estados de evidencia.
- [x] LTX05-02 Redactar la sección 05 completa.
- [x] LTX05-03 Compilar y corregir errores o desbordamientos.
- [x] LTX05-04 Renderizar y verificar visualmente el resultado.

## Verification evidence
- Cifras reconciliadas con los documentos de trazabilidad FP-182, FP-183, FP-184, FP-186, FP-187 y la recomendación FP-188.
- La sección conserva los 15 apartados previstos y añade narrativa y tablas sin modificar los modelos fuente.
- `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex` finalizó correctamente y generó un PDF de 15 páginas.
- `main.log` no contiene `Overfull`, `Undefined control sequence`, `LaTeX Error` ni referencias indefinidas.
- La sección 05 ocupa exactamente las páginas físicas 8--11; la sección 06 comienza en la página física 12.
- Las cuatro páginas fueron renderizadas a PNG y revisadas visualmente: sin recortes, solapamientos ni tablas ilegibles.

## Next step
Revisión humana de contenido y, en una iteración posterior, integración de citas y bibliografía.
