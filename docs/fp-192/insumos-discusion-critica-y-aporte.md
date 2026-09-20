# FP-192 — Insumos restringidos para discusión crítica y aporte

> **Estado de uso:** paquete de evidencia asistida para revisión humana. No es discusión crítica, aporte propio, conclusión, recomendación, criterio, cuestionario ni texto listo para entrega. Cada eventual uso académico exige validación humana fechada. La procedencia directa en Scopus/WoS/SciELO permanece **pendiente**; no se infiere indexación desde Google Scholar. [FP-189, criterio y procedencia](../fp-189/verificacion-fuentes-fp190.md#criterio-y-procedencia) · [FP-191, estado y retenciones](../fp-191/impacto-economico-y-solapamiento.md#estado-y-retenciones)

## Regla de lectura y campos reservados

| Tipo de contenido | Estado en este paquete |
|---|---|
| Evidencia comprobada con contexto | Solo las tarjetas y bloques que enlazan a FP-189/FP-191. |
| Posible inferencia a evaluar | **Sin completar:** la formula y contrasta una persona responsable. |
| Opinión, decisión, discusión crítica, aporte propio, conclusión o recomendación | **Solo humano — en blanco.** |
| Pregunta, opciones o justificación de cuestionario | **Prohibido en este paquete — solo humano.** |

La evidencia no prueba ahorro realizado, tarifa vigente, exactitud de pronóstico, desempeño de producto ni una decisión final. [FP-191, regla monetaria](../fp-191/impacto-economico-y-solapamiento.md#estado-y-retenciones) · [FP-191, campos reservados](../fp-191/impacto-economico-y-solapamiento.md#campos-reservados-para-autoría-humana-exclusiva)

## Tarjetas de evidencia de las tendencias seleccionadas (histórico provisional 2026-09-18)

Estas tres tarjetas se retienen como insumos históricos; no mantienen T1 guardrails como selección vigente. Los únicos insumos de alcance actual son los cuatro del bloque de actualización FP-76 al final.

### 1. Guardrails temporales de presupuesto estricto — Cho (2026)

**Fuente y estado.** Afirmaciones delimitadas como `Verificada con límites`; la comprobación de procedencia Scopus/WoS/SciELO sigue pendiente. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) · [FP-191 §1](../fp-191/impacto-economico-y-solapamiento.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026)

| Campo | Evidencia o reserva |
|---|---|
| Evidencia comprobada | BC-VMR evalúa resizing online con presupuesto *run-rate* por ventana y *compliance gate*, comparando BD con Static, Greedy, PRG y, según el experimento, NSGA-II. El simulador usa ventanas de 20 min, horizonte de 18 ventanas, cuatro muestras de 5 min, pool de 15 tipos de VM, flota predeterminada de 50 VM, barrida de 50–10.000 VM y diez semillas. La comprobación complementaria usa 24 h de Google Cluster Data, 288 ventanas de 5 min y 50 VM construidas desde pares de tareas; su p95 se calibra aproximadamente al 70 % de la capacidad máxima. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) |
| Cifra con contexto obligatorio | `0,0 %` de violación candidata desde `α ≥ 0,6` es tasa *pre-gate* sintética expresada como media±DE de diez semillas; `53,95 %` frente a `7,80 %` es tasa de cambio para Greedy y BD con `ρ=2` en un escenario que deshabilita presupuesto para aislar estabilidad; la comparación de `10²–10³ ms` frente a `10⁵ ms` corresponde al controlador con `N=10.000` y configuración fija. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) |
| Unidad/frontera | CPU en vCPU, memoria en GiB y precios normalizados por hora; no son tarifas monetarias publicables. La traza calibrada no mide gasto ni SLA de producción. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) · [FP-191 §1](../fp-191/impacto-economico-y-solapamiento.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) |
| Limitaciones | Simulación predominante; no incorpora SLA/latencia explícitos, costos heterogéneos de migración ni incertidumbre de pronóstico. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) |
| Posible inferencia a evaluar por humano | **[En blanco]** |
| Opinión/decisión humana | **[En blanco]** |

### 2. Inteligencia y pronóstico de precios cloud — Fragiadakis et al. (2024)

**Fuente y estado.** Afirmaciones delimitadas como `Verificada con límites`; la comprobación de procedencia Scopus/WoS/SciELO sigue pendiente. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) · [FP-191 §2](../fp-191/impacto-economico-y-solapamiento.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024)

| Campo | Evidencia o reserva |
|---|---|
| Evidencia comprobada | CloudPricingOps declara análisis de política, comparación y predicción de precios. Los casos verificables usan OLS y comparan K-Means con DBSCAN y *clustering* jerárquico, seleccionando K-Means para el caso de comparación; no constituyen una evaluación cuantificada de exactitud de pronóstico. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) |
| Cifra con contexto obligatorio | El dataset Q3–Q4 2023 contiene `589` bundles IaaS, `640` CaaS y `806` PaaS de calculadoras oficiales de seis proveedores. Los aproximadamente `USD 0,25/h` (`xsmall`) y `USD 1,75/h` (`large`) son promedios de categorías de *clustering*, no tarifa vigente, comparación homogénea ni ahorro pronosticado. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) |
| Unidad/frontera | Los atributos incluyen CPU, memoria, almacenamiento, región y opciones reservada/spot; las observaciones son instantáneas de configuración/precio, no una serie longitudinal validada. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) · [FP-191 §2](../fp-191/impacto-economico-y-solapamiento.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) |
| Limitaciones | Calidad/actualidad de datos, precios dinámicos, supuestos de regresión y selección de clúster limitan el alcance. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) |
| Posible inferencia a evaluar por humano | **[En blanco]** |
| Opinión/decisión humana | **[En blanco]** |

### 3. Conciencia de costos *shift-left* en IaC — Feitosa et al. (2024)

**Fuente y estado.** Afirmaciones delimitadas como `Verificada con límites`; la comprobación de procedencia Scopus/WoS/SciELO sigue pendiente. [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024) · [FP-191 §3](../fp-191/impacto-economico-y-solapamiento.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024)

| Campo | Evidencia o reserva |
|---|---|
| Evidencia comprobada | Estudio exploratorio de minería de repositorios GitHub con Terraform. Dos investigadores codificaron y un tercero validó; el equipo resolvió conflictos y complementó la codificación inductiva/deductiva con LDA y triangulación de Stack Overflow. El proceso produjo 14 etiquetas. Las unidades analizadas son artefactos y textos de commits/issues/discusiones, no gasto facturado ni intervención causal. [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024) · [FP-191 §3](../fp-191/impacto-economico-y-solapamiento.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024) |
| Cifra con contexto obligatorio | El cribado partió de `152.735` repositorios; produjo `2.010` repositorios con `6.116` commits potenciales, `2.045` commits inspeccionados y `538` pertinentes de 434 repositorios; también `208` issues de 89 repositorios. Aproximadamente `70 %` refiere a commits seleccionados/codificados con acciones de ahorro, no a organizaciones ni a todos los cambios IaC. [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024) |
| Unidad/frontera | Repositorios abiertos, archivos Terraform, commits, issues, etiquetas y discusiones son las unidades; no representan USD, horas facturadas, ahorro realizado ni efecto de herramienta. [FP-191 §3](../fp-191/impacto-economico-y-solapamiento.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024) |
| Limitaciones | Términos de búsqueda, selección de repositorios abiertos/Terraform, codificación y triangulación limitan generalización y pueden incorporar subjetividad. [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024) |
| Posible inferencia a evaluar por humano | **[En blanco]** |
| Opinión/decisión humana | **[En blanco]** |

## Tensiones, contradicciones y límites que deben conservarse

| Tema | Registro restringido | Campo humano |
|---|---|---|
| Alcance de presupuesto | La tasa candidata *pre-gate* no equivale a cumplimiento post-despliegue u organizacional; la inviabilidad estructural mantiene violaciones post-gate. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) | **[Interpretación crítica en blanco]** |
| “Predicción” de precios | El framework nombra predicción, mientras que los casos verificables son OLS y *clustering* sin métrica de error de *forecast*. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) | **[Interpretación crítica en blanco]** |
| Alcance de *shift-left* | La posible aplicabilidad al desarrollo cloud general queda limitada por Terraform, repositorios abiertos, términos y discusiones públicas. [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024) | **[Interpretación crítica en blanco]** |
| Comparabilidad entre tendencias | Las tres fuentes usan unidades y diseños distintos (simulación/traza calibrada; instantáneas de precios; textos/artefactos); no se habilita una comparación monetaria directa. [FP-191, regla monetaria y fichas](../fp-191/impacto-economico-y-solapamiento.md#estado-y-retenciones) | **[Criterio humano en blanco]** |
| Procedencia académica | La procedencia directa Scopus/WoS/SciELO no se verificó para ninguna de las tres fuentes. [FP-189, criterio y procedencia](../fp-189/verificacion-fuentes-fp190.md#criterio-y-procedencia) | **[Validación de base en blanco]** |

## Andamiaje de redacción humana (1–1,5 páginas; solo títulos y presupuesto)

> Uso exclusivo de autoría humana. Los rótulos siguientes no contienen prosa final ni posición académica.

1. **Delimitación de evidencia y procedencia** — ~60–80 palabras
2. **Discusión crítica: guardrails temporales de presupuesto** — ~110–140 palabras
3. **Discusión crítica: inteligencia y pronóstico de precios cloud** — ~110–140 palabras
4. **Discusión crítica: conciencia de costos *shift-left* en IaC** — ~110–140 palabras
5. **Tensiones, comparabilidad y límites transversales** — ~80–110 palabras
6. **Aporte propio y decisión de cierre** — ~60–90 palabras

**Total orientativo:** ~530–700 palabras. **Texto humano:** **[en blanco]**.

## Conceptos neutrales para explorar en cuestionario (no son preguntas, opciones ni justificaciones)

- Visibilidad de presupuesto por período operativo. [FP-191 §1](../fp-191/impacto-economico-y-solapamiento.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026)
- Información de configuración y precio para comparación. [FP-191 §2](../fp-191/impacto-economico-y-solapamiento.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024)
- Consideración de costos en cambios de infraestructura como código. [FP-191 §3](../fp-191/impacto-economico-y-solapamiento.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024)

## Bloques de evidencia para presentación

### Bloque A — Guardrails temporales

- **Fuente/método:** Cho (2026), comparación de BD con Static/Greedy/PRG/NSGA-II en simulación de resizing online y traza complementaria calibrada. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026)
- **Dato con contexto:** `0,0 %` es violación candidata *pre-gate* desde `α ≥ 0,6`, como media±DE de diez semillas bajo presupuesto *run-rate* por ventana; `7,80 %` es tasa de cambio de BD con `ρ=2` en el escenario oscilatorio. [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026)
- **Límite visible:** precios normalizados; no tarifa, ahorro realizado ni SLA productivo. [FP-191 §1](../fp-191/impacto-economico-y-solapamiento.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026)

### Bloque B — Inteligencia de precios

- **Fuente/método:** Fragiadakis et al. (2024), OLS y comparación de K-Means con DBSCAN/*clustering* jerárquico sobre instantáneas Q3–Q4 2023. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024)
- **Dato con contexto:** `589/640/806` bundles IaaS/CaaS/PaaS; no serie longitudinal. [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024)
- **Límite visible:** sin métrica verificada de exactitud de *forecast*. [FP-191 §2](../fp-191/impacto-economico-y-solapamiento.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024)

### Bloque C — Conciencia de costos en IaC

- **Fuente/método:** Feitosa et al. (2024), minería exploratoria de Terraform con codificación por dos investigadores, validación de un tercero, resolución de conflictos, LDA y triangulación de Stack Overflow; 14 etiquetas resultantes. [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024)
- **Dato con contexto:** `538` commits pertinentes y `208` issues; el ~`70 %` tiene como denominador commits seleccionados/codificados. [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024)
- **Límite visible:** evidencia textual, no ahorro facturado ni causalidad. [FP-191 §3](../fp-191/impacto-economico-y-solapamiento.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024)

## Handoff a FP-53, FP-54 y FP-56

| Destino | Material que puede recibir | Retención / acción humana |
|---|---|---|
| FP-53 | Referencia a este paquete y a las tres tarjetas, sin afirmación sustantiva adicional. La relación específica no está definida en FP-189/FP-191. [FP-189, cierre técnico](../fp-189/verificacion-fuentes-fp190.md#cierre-técnico-y-retenciones) · [FP-191, mapa de entrega](../fp-191/impacto-economico-y-solapamiento.md#mapa-de-entrega-posterior-entradas-de-evidencia-no-texto-final) | Confirmar humanamente destino, alcance y uso permitido antes de transferir. |
| FP-54 | Referencias a fichas, variables, límites, retención de procedencia y citas contextuales como entradas de evidencia. [FP-191, mapa de entrega](../fp-191/impacto-economico-y-solapamiento.md#mapa-de-entrega-posterior-entradas-de-evidencia-no-texto-final) | No transferir análisis comparativo, criterio, conclusión, recomendación, aporte propio ni cuestionario. |
| FP-56 | Trazabilidad visual/de defensa de selección humana, mecanismo acotado, unidad, evidencia contextual, límite y procedencia pendiente. [FP-191, mapa de entrega](../fp-191/impacto-economico-y-solapamiento.md#mapa-de-entrega-posterior-entradas-de-evidencia-no-texto-final) | No presentar exactitud de *forecast*, ahorro realizado, tarifa vigente, evaluación de producto ni decisión final. |

## Lista de validación humana antes de cualquier uso

- [ ] Revisar PDF original, página, DOI, fecha, método, muestra, unidad y contexto de cada dato usado. [FP-189, cierre técnico](../fp-189/verificacion-fuentes-fp190.md#cierre-técnico-y-retenciones)
- [ ] Verificar directamente la procedencia/indexación de cada artículo en Scopus, WoS o SciELO según la exigencia docente; registrar persona, fecha y evidencia. [FP-189, criterio y procedencia](../fp-189/verificacion-fuentes-fp190.md#criterio-y-procedencia)
- [ ] Mantener las fronteras: simulación/precios normalizados de Cho; falta de exactitud de *forecast* de CloudPricingOps; evidencia textual sin ahorro/causalidad de Feitosa. [FP-191 §1](../fp-191/impacto-economico-y-solapamiento.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026) · [FP-191 §2](../fp-191/impacto-economico-y-solapamiento.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024) · [FP-191 §3](../fp-191/impacto-economico-y-solapamiento.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024)
- [ ] Redactar de forma humana e independiente la discusión crítica, aporte propio, conclusión, recomendación, criterios y cualquier cuestionario. [FP-191, campos reservados](../fp-191/impacto-economico-y-solapamiento.md#campos-reservados-para-autoría-humana-exclusiva)
- [ ] Confirmar humanamente la recepción y el alcance de FP-53, FP-54 y FP-56; no asumir que el enlace implica aceptación. [FP-191, mapa de entrega](../fp-191/impacto-economico-y-solapamiento.md#mapa-de-entrega-posterior-entradas-de-evidencia-no-texto-final)

## Actualización de insumos FP-76 — alcance final aprobado (2026-09-20)

Solo insumos, tensiones y límites para lectura humana; no contiene discusión crítica, aporte, análisis comparativo, conclusión, recomendación ni cuestionario.

| Línea aprobada | Insumo verificable | Tensión/límite a conservar | Campo humano |
|---|---|---|---|
| Compromisos, descuentos y capacidad spot | `FP76-100`: compromiso/descuento frente a ociosidad; 1,1 % de ahorro propio observado y 27–55 % de descuentos nominales. | Concentración en una fuente; descuento nominal no equivale a ahorro observado. | **[En blanco]** |
| T2 Inteligencia y análisis de precios cloud | `FP76-080` y `FP76-002`: asimetrías de tipo, región y modalidad. | Forecasting es limitado: autocorrelación en `FP76-117`; `FP76-043` no demuestra forecast. | **[En blanco]** |
| T3 Conciencia de costos *shift-left* en IaC | `FP76-041` registra conducta; `FP76-037` aporta magnitud simulada. | No hay ahorro productivo medido; `FP76-041` conserva B1=1 y simulación no es producción. | **[En blanco]** |
| Economía unitaria de GenAI/LLM | `FP76-134` y `FP76-332`: costo por token, solicitud, inferencia o valor. | Precios de lista y límite de generalización AWS `us-west-2`. | **[En blanco]** |

T1 guardrails y FinOps agéntico quedan como contexto; `FP76-289` es Reserva/contexto. Forecasting y selección multi-cloud/proveedor no son líneas autónomas. La evidencia se limita a 13 textos verificados; los 17 no disponibles no aportan evidencia primaria y no habrá nueva recuperación.

## Estado de autoría humana — Versión 3 (2026-09-20)

Las secciones de análisis comparativo, discusión crítica, aporte propio, conclusiones, recomendaciones y cuestionario ya existen en la [`Versión 3 validada`](<../../../FP-76 - analisis, discusion, aporte, conclusiones y cuestionario (FINAL).md>). Danilo las redactó y validó humanamente el 2026-09-20, incluida la justificación del cuestionario. Este paquete las reconoce como contenido humano y **no las reproduce, reautoriza ni modifica**. La validación no implica aprobación de equipo o docente; permanecen separadas las retenciones de FP-180, destinos FP-53/54/56, Drive/Jira y QA final.
