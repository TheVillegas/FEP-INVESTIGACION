# FP-191 — Hoja de entrega de evidencia: impacto económico y solapamiento

> **Uso acotado.** Esta hoja conserva evidencia verificada, límites y puntos de enlace para revisión humana. No contiene una comparación final, puntuación, juicio, conclusión, recomendación, aporte propio ni texto de cuestionario. No traslade su redacción asistida a secciones de autoría humana exclusiva.

## Estado y retenciones

| Campo | Registro |
|---|---|
| Tendencias incluidas | Exactamente cuatro, aprobadas por Danilo el 2026-09-20: compromisos, descuentos y capacidad spot; T2 Inteligencia y análisis de precios cloud; T3 conciencia de costos *shift-left* en IaC; y economía unitaria de GenAI/LLM. La selección provisional de tres del 2026-09-18 queda preservada como historia en FP-190. |
| Decisión humana de inclusión | **Registrada, no generada por esta hoja:** Danilo aprobó las cuatro tendencias el 2026-09-20. La decisión habilita este registro de evidencia; no cierra sus brechas ni constituye aceptación académica final. |
| Fuente verificadora utilizable | [FP-189](../fp-189/verificacion-fuentes-fp190.md), con estado de las afirmaciones `Verificada con límites`. |
| Retención de procedencia | **Scopus/WoS/SciELO: pendiente.** FP-189 confirmó PDF locales, DOI, fechas, método y cifras delimitadas; la matriz registra obtención mediante Google Scholar, pero esta ejecución no verificó directamente registros en Scopus, Web of Science ni SciELO. No se afirma ni se niega indexación. |
| Regla monetaria | Ninguna cifra de esta hoja representa ahorro, gasto, tarifa vigente, cotización, forecast validado ni impacto monetario realizado. |

## Variables de enlace con los artefactos base

Estas son variables ya presentes en FP-172/177/180/182–188 que pueden recibir evidencia contextual, sin recalcularlas ni transferir resultados entre artefactos.

| Bloque base | Variables o unidades ya documentadas | Límite de uso en esta hoja |
|---|---|---|
| FP-172 | Palanca, mecanismo, supuesto, condición, riesgo, fuente y fecha; ejemplos monetarios ilustrativos. | No convierte una palanca en resultado monetario ni reemplaza tarifas oficiales reproducibles. |
| FP-177/FP-180 | Escenario, producto × escenario, fecha de corte, región, moneda, unidad, entradas equivalentes, evidencia por indicador y estados `0/1/2/3/NE/NA`. | No crea indicador, puntaje, elegibilidad ni capacidad de producto. |
| FP-182–FP-184 | Región, horizonte, configuración de recurso, uso/horas, vCPU, vCores, GiB, GB/mes, unidades de precio, TCO y ahorro bruto modelados. | No modifica supuestos, precios, configuración ni ahorros de escenario. |
| FP-185–FP-188 | Comparación regional, sensibilidad, flujo incremental, tasa, horas, tarifa proxy, restricciones y condiciones registradas. | No valida proxies ni usa estos valores para afirmar una decisión o efecto de las tendencias. |

## Fichas de evidencia y decisión (histórico provisional 2026-09-18)

Las tres fichas que siguen preservan la selección provisional; no mantienen T1 guardrails como tendencia vigente. El inventario de cuatro líneas aprobado el 2026-09-20 se registra al final de esta hoja.

### 1. Guardrails temporales de presupuesto estricto — Cho (2026)

| Campo | Registro verificable |
|---|---|
| Inclusión humana | Seleccionada en FP-190 el 2026-09-18; pendiente la aceptación académica humana y la comprobación de procedencia Scopus/WoS/SciELO. |
| Mecanismo económico observado | El trabajo formula optimización de recursos con presupuesto *run-rate* por ventana y un *compliance gate*: la variable de presupuesto restringe candidatos de resizing. Es un mecanismo de factibilidad temporal, no una medición de ahorro realizado. |
| Variables observables y unidades | Ventana: 20 min; horizonte: 18 ventanas; muestras de demanda: 4 por ventana (5 min); pool: 15 tipos de VM; flota: 50 VM; CPU: vCPU; memoria: GiB; precios: unidades normalizadas por hora. Traza complementaria: 24 h, 288 ventanas de 5 min y 50 VM. |
| Evidencia numérica y contexto obligatorio | BD alcanza **0,0 %** de violación candidata desde `α ≥ 0,6`: tasa *pre-gate* sintética, media±DE de diez semillas y presupuesto *run-rate* por ventana. En otro escenario, tasa de cambio: **53,95 %** Greedy frente a **7,80 %** BD (`ρ=2`), con presupuestos temporalmente deshabilitados para aislar estabilidad. A `N=10.000`, BD ronda `10²–10³ ms` por decisión y NSGA-II `10⁵ ms`, bajo hardware/configuración fijos. Fuente: [FP-189 §1](../fp-189/verificacion-fuentes-fp190.md#1-guardrails-temporales-de-presupuesto-estricto--cho-2026). |
| Riesgos y límites | Predomina simulación; la traza se calibra y no mide gasto ni SLA productivo. El artículo excluye SLA/latencia explícitos, costos heterogéneos de migración e incertidumbre de forecast. **Cho usa unidades de precio normalizadas por hora, no tarifas monetarias publicables.** |
| Frontera exacta de solapamiento | **FP-172:** comparte resizing/rightsizing, pero esta ficha solo retiene semántica de presupuesto temporal, inviabilidad estructural y *compliance gate*; no reutiliza ni añade una palanca. **FP-177/FP-180:** no evalúa producto, escenario ni indicador, incluido E3. **FP-182–FP-188:** no altera región, carga, precios, TCO, ahorro bruto, sensibilidad ni flujo incremental del caso ilustrativo. |
| Integración posterior posible, solo como entrada de evidencia | Asociar el concepto de presupuesto por ventana con las variables existentes de uso/horas, vCPU, vCores, GiB, período y supuesto de FP-172/182–187, manteniendo la unidad normalizada separada de USD y de tarifas. |

### 2. Inteligencia y pronóstico de precios cloud — Fragiadakis et al. (2024)

| Campo | Registro verificable |
|---|---|
| Inclusión humana | Seleccionada en FP-190 el 2026-09-18; pendiente la aceptación académica humana y la comprobación de procedencia Scopus/WoS/SciELO. |
| Mecanismo económico observado | CloudPricingOps propone apoyo a decisiones para analizar políticas, comparar costos y explorar predicción de precios a partir de atributos de servicios y precios recolectados. El mecanismo conecta configuración/precio con análisis; no demuestra un ahorro ni la exactitud de un forecast. |
| Variables observables y unidades | Bundles IaaS/CaaS/PaaS; CPU, memoria, almacenamiento, región y opción reservada/spot; período de recolección Q3–Q4 2023; precio de ejemplos en USD/h. |
| Evidencia numérica y contexto obligatorio | Dataset: **589** bundles IaaS, **640** CaaS y **806** PaaS, obtenidos de calculadoras oficiales de seis proveedores en Q3–Q4 2023. La Fig. 7 muestra aproximadamente **USD 0,25/h** para `xsmall` y **USD 1,75/h** para `large`: promedios de categorías de *clustering* CPU-RAM/almacenamiento, no tarifa vigente, precio homogéneo ni ahorro pronosticado. Fuente: [FP-189 §2](../fp-189/verificacion-fuentes-fp190.md#2-inteligencia-y-pronóstico-de-precios-cloud--fragiadakis-et-al-2024). |
| Riesgos y límites | Las observaciones son instantáneas de configuración/precio, no serie longitudinal. Calidad/actualidad de datos, precios dinámicos, supuestos de regresión y elección de clúster limitan el alcance. **CloudPricingOps respalda inteligencia de precios, pero no demuestra exactitud de forecast.** |
| Frontera exacta de solapamiento | **FP-172:** no reemplaza palancas ni tarifas oficiales. **FP-177/FP-180:** coincide con E2 y los indicadores de precio solo en el tema de comparación; esta ficha no puntúa herramientas, clasifica proveedores ni usa CloudPricingOps como prueba de capacidad o exactitud de pronóstico. **FP-182–FP-188:** no sustituye precios fechados, moneda, región, unidades, contratos ni resultados del TCO/modelos regionales. |
| Integración posterior posible, solo como entrada de evidencia | Vincular con los campos existentes de proveedor, región, moneda, período, unidad, configuración, supuestos de normalización y fecha de corte de FP-177/180/182–188; conservar explícitamente la no-equivalencia funcional y el carácter no longitudinal del dataset. |

### 3. Conciencia de costos *shift-left* en IaC — Feitosa et al. (2024)

| Campo | Registro verificable |
|---|---|
| Inclusión humana | Seleccionada en FP-190 el 2026-09-18; pendiente la aceptación académica humana y la comprobación de procedencia Scopus/WoS/SciELO. |
| Mecanismo económico observado | El estudio examina cómo preocupaciones y acciones de costo aparecen en artefactos Terraform, commits, issues y discusiones públicas antes o durante cambios de infraestructura. Registra evidencia textual de conciencia/decisión; no mide el efecto económico posterior. |
| Variables observables y unidades | Repositorios, archivos Terraform, commits, issues, etiquetas/códigos y discusiones; las unidades de análisis son artefactos y textos, no USD, horas facturadas, ahorro ni gasto realizado. |
| Evidencia numérica y contexto obligatorio | Cribado: **152.735** repositorios; **2.010 repositorios** con **6.116 commits** potencialmente relacionados; después de retirar forks y cambios ajenos a Terraform, **2.045 commits** fueron inspeccionados manualmente y **538** resultaron pertinentes, provenientes de 434 repositorios. También se seleccionaron **208 issues** de 89 repositorios. Aproximadamente **70 %** de los commits seleccionados/codificados documenta acciones concretas de ahorro. Son conteos de etapas y denominadores distintos; no se suman ni representan organizaciones. Fuente: [FP-189 §3](../fp-189/verificacion-fuentes-fp190.md#3-conciencia-de-costos-shift-left-en-iac--feitosa-et-al-2024). |
| Riesgos y límites | Repositorios abiertos, Terraform, términos de búsqueda y codificación limitan generalización; hay amenazas de selección y subjetividad. **Feitosa mide texto y artefactos, no ahorros realizados, gasto facturado, efecto causal ni desempeño de una herramienta.** |
| Frontera exacta de solapamiento | **FP-172:** no incorpora una palanca ni cuantifica su efecto. **FP-177/FP-180:** toca E4 solo como contexto de cambios IaC; no evalúa Infracost, Cloud Custodian u otro producto, ni crea puntuación, política o estimación previa. **FP-182–FP-188:** no cambia configuración, horas, tarifas, TCO, ahorro, sensibilidad, VAN/TIR ni sus proxies. |
| Integración posterior posible, solo como entrada de evidencia | Asociar los artefactos IaC y los campos de cambio, región, recurso, supuesto de precio y regla de política ya definidos para E4/FP-182–FP-187, diferenciando siempre evidencia textual de una medición de factura o ahorro. |

## Mapa de entrega posterior: entradas de evidencia, no texto final

| Destino | Paquete que puede recibir | Exclusiones obligatorias |
|---|---|---|
| FP-54 | Referencias a las tres fichas, sus variables, citas contextuales, límites, retención Scopus/WoS/SciELO y enlaces a FP-189/FP-172/177/180/182–188. | No transferir como análisis comparativo, criterio, conclusión, recomendación, aporte propio ni cuestionario; no trasladar cifras normalizadas/simuladas/textuales como resultados monetarios. |
| FP-56 | Trazabilidad visual o de defensa de: decisión humana de inclusión, mecanismo acotado, unidad de medida, evidencia contextual, límite y procedencia pendiente. | No presentar forecasting exacto, ahorro realizado, tarifa vigente, evaluación de producto o decisión final derivada de estas fichas. |

## Campos reservados para autoría humana exclusiva

| Campo | Registro |
|---|---|
| Validación humana de cada fuente, página y procedencia | **Pendiente:** nombre, fecha, resultado y evidencia de Scopus/WoS/SciELO. |
| Juicio comparativo final | **Solo humano — sin completar.** |
| Recomendación final | **Solo humana — sin completar.** |
| Aporte propio/discusión crítica | **Solo humano — sin completar.** |
| Texto o justificación de cuestionario | **Solo humano — sin completar.** |

## Actualización FP-76 — cuatro tendencias aprobadas (2026-09-20)

Esta tabla sustituye para alcance vigente las tres inclusiones provisionales de la cabecera, que permanecen arriba como registro histórico. Es un inventario de mecanismos y variables, no comparación ni juicio final.

| Tendencia | Mecanismo y variables observables | Evidencia/certeza y límite económico | Frontera de solapamiento |
|---|---|---|---|
| Compromisos, descuentos y capacidad spot | Descuento por compromiso frente a capacidad ociosa; descuento nominal, resultado contrafactual y fracción de capacidad sin uso. | `FP76-100`, confianza alta; 1,1 % contrafactual sobre traza real frente a descuentos 27–55 %. Una fuente concentra la evidencia y las medidas no son intercambiables. | No convierte reservas/spot en una palanca nueva de FP-172 ni en recomendación de compra. |
| T2 Inteligencia y análisis de precios cloud | Tipo de servicio, región, modalidad y precio/configuración; forecasting solo sublínea. | `FP76-080` y `FP76-002`, confianza media-alta. `FP76-117` limita forecast por autocorrelación; `FP76-043` no acredita forecast. | No clasifica proveedores ni reemplaza E2, tarifas fechadas o normalización de FP-177/180/182–188. |
| T3 Conciencia de costos *shift-left* en IaC | Decisión temprana en configuración/diseño; artefactos IaC, cambios y costos simulados. | `FP76-041` conductual + `FP76-037` magnitud simulada; confianza media. Sin ahorro productivo medido; `FP76-041` B1=1. | No evalúa herramientas E4 ni transforma una acción IaC en TCO/ahorro realizado. |
| Economía unitaria de GenAI/LLM | Costo por token, solicitud, inferencia o valor; arquitectura/carga y unidad de servicio. | `FP76-134` y `FP76-332`, confianza media-alta. Retener precios de lista y límite AWS `us-west-2`. | No extiende resultados a precio pagado, multirregión/multiproveedor ni a LLMOps técnico fuera del alcance FinOps. |

T1 guardrails, FinOps agéntico y `FP76-289` son contexto (este último Reserva); forecasting y selección multi-cloud/proveedor son sublíneas. La base cerrada es 13 textos verificados, con 17 no disponibles y sin nueva recuperación.

## Niveles E0–E4 de la Versión 3 validada (2026-09-20)

La clasificación siguiente enlaza la evidencia con la escala preliminar del equipo; no es un estándar FinOps ni tiene validación externa. Danilo validó humanamente la Versión 3 el 2026-09-20, sin aprobación atribuida a equipo o docente.

| Tendencia | Evidencia y nivel correcto | Límite obligatorio |
|---|---|---|
| Compromisos, descuentos y capacidad spot | `FP76-100`: descuentos 27–55 % = **E1**; optimización de 1,1 % sobre traza real = **E2 con datos de producción**. | El 1,1 % es contrafactual, no ahorro facturado ni E3/E4; fuente única. |
| T2 Inteligencia y análisis de precios cloud | `FP76-080`: ganancia calculada sobre precios reales = **E2 con insumo E1**; `FP76-043`: ejemplos de precio = **E1**. | `FP76-117` no demuestra resultado económico y conserva autocorrelación; `FP76-043` no demuestra forecast. |
| T3 Conciencia de costos *shift-left* en IaC | `FP76-041`: cita anecdótica de 80 % = **E0**; `FP76-037`: reducción simulada = **E2**. | La conducta de `041` no es ahorro productivo; la magnitud de `037` es simulada y no hay E3/E4. |
| Economía unitaria de GenAI/LLM | `FP76-134`: precios de lista = **E1**; `FP76-332`: medición posterior en AWS = **E3**. | E3 es acotado a su entorno/carga; no equivale a gasto facturado y sostenido en producción. |

Ninguna tendencia alcanza **E4**; solo economía unitaria de GenAI/LLM alcanza **E3**. E1 y E2 no sostienen por sí solos una decisión de inversión bajo la precaución normativa de la Versión 3.
