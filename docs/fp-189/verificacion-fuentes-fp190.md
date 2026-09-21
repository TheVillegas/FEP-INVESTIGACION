# FP-189 — verificación independiente de fuentes para las tendencias seleccionadas de FP-190

> **Alcance y resguardo académico.** Este paquete verifica trazabilidad bibliográfica y alcance de evidencia. No es análisis comparativo, conclusión, recomendación, aporte propio ni texto de cuestionario. Las fuentes primarias locales se leyeron contra sus PDF; las extracciones Markdown son ayudas de localización, no sustitutos del original. La aceptación académica y cualquier reutilización requieren validación humana fechada.

## Criterio y procedencia

- `Verificada con límites` significa que identidad, fechas, método y las afirmaciones delimitadas abajo se contrastaron en el PDF local original. No significa que el resultado sea generalizable ni que pruebe una tendencia por sí solo.
- `Pendiente` significa que no se verificó en esta ejecución. En particular, la matriz FP-48 registra las tres fuentes locales como obtenidas mediante **Google Scholar**; esta ejecución **no** verificó directamente los registros de los artículos en Scopus, Web of Science (WoS) ni SciELO. Eso es una retención de procedencia de base de datos para uso académico final, no una afirmación de ausencia de indexación.
- Las comprobaciones de PDF se hicieron con `pdftotext -layout`; se confirmaron DOI, fecha y paginación del original local: Cho 48 pp.; Fragiadakis et al. 20 pp.; Feitosa et al. 14 pp. Las rutas y sus SHA-256 se conservan en la bitácora FP-189.

| Fuente primaria local | Identidad/fecha | Método, muestra y cifras delimitadas | Estado de afirmaciones | Procedencia en bases |
|---|---|---|---|---|
| Cho (2026), `10.3390/app16073302` | Verificada con límites | Verificada con límites | Verificada con límites | **Pendiente** |
| Fragiadakis et al. (2024), `10.3390/app142411946` | Verificada con límites | Verificada con límites | Verificada con límites | **Pendiente** |
| Feitosa et al. (2024), `10.1016/j.jss.2024.112112` | Verificada con límites | Verificada con límites | Verificada con límites | **Pendiente** |

## 1. Guardrails temporales de presupuesto estricto — Cho (2026)

### Identidad y fuente primaria

- **Referencia comprobada:** Cho, Choong-Hee. *FinOps-Aware Budget-Constrained Optimization for Cloud Resource Management*. *Applied Sciences* **16** (2026), 3302. DOI: [`10.3390/app16073302`](https://doi.org/10.3390/app16073302).
- **Fechas en el PDF:** recibido 2026-02-24; revisado 2026-03-11; aceptado 2026-03-27; publicado 2026-03-29.
- **Original y ayuda de lectura:** `FP-48 TINV02/Papers academicos - FP-48/03_Cho_2026_FinOps_Budget_Optimization.pdf`, pp. 1–48; extracción correspondiente `.../markdown/03_Cho_2026_FinOps_Budget_Optimization.md`.

### Método, muestra y unidades comprobados

El trabajo formula BC-VMR y compara el solver Budget-aware Dual (BD) con Static, Greedy, PRG y, según el experimento, NSGA-II. La evaluación principal es un **simulador** de resizing online: ventana de 20 min, horizonte de 18 ventanas, cuatro muestras de demanda por ventana (5 min), pool de 15 tipos VM, flota predeterminada de 50 VM y diez semillas; la barrida de tamaño usa 50 a 10.000 VM. CPU se expresa en vCPU, memoria en GiB y los precios por hora son unidades normalizadas, no tarifas monetarias publicables (pp. 8–9, 24–30).

La comprobación complementaria con traza usa Google Cluster Data (2011): un segmento contiguo de 24 h, 288 ventanas de 5 min y 50 VM construidas desde pares `(job_id, task_index)`. La p95 de la traza se calibra aproximadamente al 70 % de la capacidad máxima del pool (16 vCPU/32 GB); por ello no es una medición de gasto ni de SLA de una organización productiva (pp. 43–45).

### Afirmaciones, cifras y contexto exacto

| Afirmación que puede rastrearse | Verificación y contexto obligatorio |
|---|---|
| BD alcanza **0,0 %** de violación candidata desde `α ≥ 0,6`. | **Verificada con límites.** Es la tasa **pre-gate** de candidatos del experimento sintético bajo presupuesto run-rate por ventana, media±DE de diez semillas; no equivale a cumplimiento post-despliegue ni a cumplimiento organizacional. El PDF mantiene violaciones post-gate solo cuando la ventana es estructuralmente inviable (pp. 35–37, 45–46). |
| La tasa de cambio baja de **53,95 %** (Greedy) a **7,80 %** (BD, `ρ=2`). | **Verificada con límites.** Es tasa media de cambio de configuración en el escenario sintético oscilatorio de la Fig. 10, con presupuestos temporalmente **deshabilitados** para aislar estabilidad; no mide ahorro realizado, tiempo de migración ni operación en producción (pp. 41–43). |
| BD es más de 100× más rápido que NSGA-II a escala grande. | **Verificada con límites.** Bajo hardware/configuración fijos y `N=10.000`, el texto reporta BD alrededor de `10²–10³ ms` por decisión y NSGA-II alrededor de `10⁵ ms`; es una comparación de optimización de controlador, no latencia end-to-end ni prueba independiente de costo (pp. 31–33, 45). |

### Contraste, límites y solapamiento

- No se detectó contradicción numérica interna entre el resumen y las secciones de resultados: las cifras del resumen se acotan a los escenarios anteriores. Sí sería una sobreextensión trasladarlas a presupuestos acumulativos, a todos los valores de `ρ`, o a producción.
- El análisis formal de regret/violación se limita al modelo run-rate bajo relajación continua; los modelos temporalmente acoplados se evalúan empíricamente. Predomina el simulador y el propio artículo excluye SLA/latencia explícitos, costos de migración heterogéneos e incertidumbre de pronóstico (pp. 23–24, 45–46).
- El solapamiento con FP-172 es el resizing/rightsizing como palanca. La evidencia utilizable aquí queda delimitada a semánticas de presupuesto temporal, inviabilidad estructural y protocolo común de compliance gate; no prueba una palanca estándar ni justifica adoptar su solver.

**Resultado de la fuente:** afirmaciones delimitadas `Verificada con límites`; procedencia Scopus/WoS/SciELO `Pendiente`.

## 2. Inteligencia y pronóstico de precios cloud — Fragiadakis et al. (2024)

### Identidad y fuente primaria

- **Referencia comprobada:** Fragiadakis, George; Tsadimas, Anargyros; Filiopoulou, Evangelia; Kousiouris, George; Michalakelis, Christos; Nikolaidou, Mara. *Cloud PricingOps: A Decision Support Framework to Explore Pricing Policies of Cloud Services*. *Applied Sciences* **14** (2024), 11946. DOI: [`10.3390/app142411946`](https://doi.org/10.3390/app142411946).
- **Fechas en el PDF:** recibido 2024-11-14; revisado 2024-12-08; aceptado 2024-12-10; publicado 2024-12-20.
- **Original y ayuda de lectura:** `FP-48 TINV02/Papers academicos - FP-48/applsci-14-11946-v2.pdf`, pp. 1–20; extracción `.../markdown/applsci-14-11946-v2.md`.

### Método, muestra y unidades comprobados

Es una propuesta de framework/sistema de apoyo a decisiones con tres capacidades: análisis de política de precios, comparación de costos y predicción de precios. Presenta dos casos: OLS para análisis de atributos de precio y clustering (K-Means elegido frente a DBSCAN y clustering jerárquico) para comparación; no presenta un caso de evaluación de un pronóstico temporal con resultados de exactitud.

Los datos reales proceden de calculadoras oficiales de AWS, Azure, Google Cloud, IBM Cloud, Alibaba Cloud y DigitalOcean, recolectados en Q3–Q4 de 2023. El conjunto contiene 589 bundles IaaS, 640 CaaS y 806 PaaS; sus atributos incluyen CPU, memoria, almacenamiento, región y opciones como reservada/spot. Son instantáneas de configuración/precio, no una serie de precios longitudinal validada (pp. 14–17).

### Afirmaciones, cifras y contexto exacto

| Afirmación que puede rastrearse | Verificación y contexto obligatorio |
|---|---|
| CloudPricingOps integra análisis de política, comparación y predicción de precios. | **Verificada con límites.** Es la capacidad/diseño declarado del framework; los dos casos demostrados en el PDF son OLS y clustering, no una demostración cuantificada de precisión de forecast (pp. 1, 6–14, 19). |
| Las muestras son **589 IaaS / 640 CaaS / 806 PaaS**. | **Verificada con límites.** Son cantidades de bundles de los datasets Q3–Q4 2023, no número de empresas, regiones equivalentes ni observaciones de una serie temporal (pp. 14–15). |
| La Fig. 7 muestra aproximadamente **USD 0,25/h** para `xsmall` y **USD 1,75/h** para `large`. | **Verificada con límites.** Son ejemplos de promedios de categorías de clustering CPU-RAM/almacenamiento; el pasaje no los convierte en precio vigente, comparación homogénea entre proveedores ni ahorro pronosticado (pp. 17–18). |

### Contraste, límites y solapamiento

- Hay una tensión de alcance que debe conservarse: el artículo nombra *price prediction* como capacidad, pero sus casos verificables son análisis OLS y clustering; no se informó una cifra de error de forecast en los casos. Por tanto, el PDF sustenta un framework para explorar precios, no exactitud ni superioridad de un pronóstico.
- Los autores limitan la fiabilidad a calidad/actualidad de datos; advierten que regresión puede simplificar relaciones, K-Means depende de número de clústeres y los precios dinámicos requieren actualización frecuente (p. 19).
- El solapamiento con FP-177 E2 es comparación de precios. La frontera de esta fuente es el análisis estructurado y la posible predicción de políticas; no debe reutilizarse como ranking de proveedores, tarifa actual o resultado de forecasting.

**Resultado de la fuente:** afirmaciones delimitadas `Verificada con límites`; procedencia Scopus/WoS/SciELO `Pendiente`.

## 3. Conciencia de costos *shift-left* en IaC — Feitosa et al. (2024)

### Identidad y fuente primaria

- **Referencia comprobada:** Feitosa, Daniel; Penca, Matei-Tudor; Berardi, Massimiliano; Boza, Rares-Dorian; Andrikopoulos, Vasilios. *Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications: An exploratory study*. *The Journal of Systems & Software* **215** (2024), 112112. DOI: [`10.1016/j.jss.2024.112112`](https://doi.org/10.1016/j.jss.2024.112112).
- **Fechas en el PDF:** recibido 2023-12-18; revisado 2024-04-10; aceptado 2024-05-22; disponible en línea 2024-05-24.
- **Original y ayuda de lectura:** `FP-48 TINV02/Papers academicos - FP-48/Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications An exploratory study.pdf`, pp. 1–14; extracción Markdown homónima.

### Método, muestra y unidades comprobados

Es un estudio exploratorio de minería de repositorios abiertos de GitHub con artefactos Terraform. De 152.735 repositorios tras filtrar archivos `.tf`/`.tf.json`, la búsqueda por stems de costo obtuvo 2.010 repositorios con 6.116 commits potencialmente relacionados. Después de retirar forks y cambios que no modificaban Terraform quedaron 2.045 commits, que se inspeccionaron manualmente; de ellos se seleccionaron 538 commits pertinentes de 434 repositorios. Además, se seleccionaron 208 issues de 89 repositorios. La codificación abierta/inductiva fue realizada por dos investigadores y validada por un tercero, con resolución de conflictos por el equipo; se complementó con codificación deductiva, LDA y triangulación de discusiones Terraform en Stack Overflow (pp. 1–5, 9–11).

Las unidades son textos de commits/issues y discusiones, no costos facturados, intervención experimental, empresas encuestadas ni efecto causal de una práctica *shift-left*. Aproximadamente 70 % de los commits codificados documenta acciones concretas para ahorrar costos; esa proporción se refiere a los commits ya seleccionados como pertinentes, no a 70 % de todos los repositorios Terraform (p. 6).

### Afirmaciones, cifras y contexto exacto

| Afirmación que puede rastrearse | Verificación y contexto obligatorio |
|---|---|
| Hay evidencia empírica de preocupaciones y acciones de costo en artefactos Terraform abiertos. | **Verificada con límites.** El corpus seleccionado contiene 538 commits y 208 issues codificados; los autores identifican 14 etiquetas y hallan discusiones complementarias. No permite estimar adopción poblacional ni ahorro financiero (pp. 1, 4–8). |
| El cribado partió de **152.735** repositorios y produjo **2.010** hits, **538** commits y **208** issues analizados. | **Verificada con límites.** Son conteos de etapas distintas de filtrado/codificación; no deben sumarse ni presentarse como muestra de 152.735 organizaciones (pp. 1, 3–5). |
| Aproximadamente **70 %** de los commits documenta acciones para ahorrar costo. | **Verificada con límites.** La unidad y denominador son los commits seleccionados/codificados de la Fig. 4; la cifra no representa todos los cambios IaC ni prueba reducción de gasto (p. 6). |

### Contraste, límites y solapamiento

- No hay contradicción factual interna, pero la frase del resumen de que los hallazgos “pueden ser aplicables” al desarrollo cloud general debe leerse frente a los límites: Terraform, repositorios abiertos, palabras clave elegidas y discusiones públicas. El artículo solicita ampliar a otros orquestadores, repositorios cerrados, código fuente y pull requests (pp. 11–13).
- Amenazas explícitas: selección de términos puede omitir tópicos; el constructo y la codificación pueden incorporar subjetividad; la triangulación de Stack Overflow tiene amenazas propias. La selección de artefactos/repo limita generalización (pp. 12–13).
- El solapamiento con FP-177 E4 es estimación/política previa al despliegue. Esta fuente solo respalda evidencia textual de conciencia y decisiones de costo en IaC; no evalúa una herramienta, política de despliegue, ahorro conseguido ni obligatoriedad de *shift-left*.

**Resultado de la fuente:** afirmaciones delimitadas `Verificada con límites`; procedencia Scopus/WoS/SciELO `Pendiente`.

## Corroboración externa secundaria: límite estricto de evidencia

Estas referencias no sustituyen las tres fuentes primarias. En esta ejecución se recuperó únicamente metadata bibliográfica por DOI y, solo para Stupar & Huljenic, un resumen expuesto por el registro DOI. No se leyeron PDF/textos completos, no se verificaron muestras, métodos, cifras, resultados ni indexación en Scopus/WoS/SciELO.

| Referencia externa | Lo que sí quedó comprobado | Afirmación que puede hacerse / prohibición de sobrealcance |
|---|---|---|
| Cheng et al. (2024), *GeoScale: Microservice Autoscaling With Cost Budget in Geo-Distributed Edge Clouds*, *IEEE Transactions on Parallel and Distributed Systems*, DOI [`10.1109/TPDS.2024.3366533`](https://doi.org/10.1109/TPDS.2024.3366533) | **Solo metadata:** autoría, título, revista y año/mes de emisión (2024-04). | El título lo hace contexto temático de autoscaling con presupuesto en edge geo-distribuido. No se afirma que corrobore el método, tasas de violación, escalabilidad o aplicabilidad de Cho. |
| Smendowski & Nawrocki (2024), *Optimizing multi-time series forecasting for enhanced cloud resource utilization based on machine learning*, *Knowledge-Based Systems*, DOI [`10.1016/j.knosys.2024.112489`](https://doi.org/10.1016/j.knosys.2024.112489) | **Solo metadata:** autoría, título, revista y año/mes de emisión (2024-11). | El título lo hace contexto temático de forecasting multiserie y utilización cloud. No se afirma exactitud, datos, comparación de precios, resultado FinOps ni corroboración de CloudPricingOps. |
| Stupar & Huljenic (2023), *Model-based cloud service deployment optimisation method for minimisation of application service operational cost*, *Journal of Cloud Computing*, DOI [`10.1186/s13677-023-00389-8`](https://doi.org/10.1186/s13677-023-00389-8) | **Metadata y resumen del registro DOI:** autoría, título, revista, fecha 2023-02-18 y que el resumen presenta un enfoque de optimización para proveedores de aplicaciones cloud. | Puede registrarse como antecedente de optimización de costo operativo en despliegue. No se afirma evidencia sobre repositorios Terraform, conciencia de costos, conducta *shift-left*, método, muestra o efecto de Feitosa sin lectura primaria humana. |

## Cierre técnico y retenciones

- **Cobertura técnica FP-189:** las tres identidades, DOI, fechas, método/muestra, cifras con unidad/contexto, límites, tensiones de alcance y solapamientos quedaron documentados con estado `Verificada con límites`. Las corroboraciones externas quedaron etiquetadas según el nivel realmente leído.
- **Bloqueado para aceptación académica final:** validar humanamente PDF, citas y delimitación; verificar directamente procedencia/indexación de los tres artículos en las bases exigidas; decidir si la evidencia externa requiere lectura primaria; y no transferir este texto asistido a secciones de autoría humana exclusiva.

## Extensión FP-76 — verificación independiente para la decisión final del 2026-09-20

Esta extensión conserva las tres fichas históricas anteriores, pero distingue el nivel realmente verificado de las fuentes usadas en la selección final. La aprobación humana de alcance no eleva una fuente secundaria/contextual a evidencia primaria ni resuelve procedencia Scopus/SciELO.

| Tendencia final | Fuentes y nivel | Mecanismo/estado verificable | Contradicciones y límites que no se deben perder |
|---|---|---|---|
| Compromisos, descuentos y capacidad spot | **Primaria:** `FP76-100` (texto completo verificado). | Compromiso con descuento versus riesgo de capacidad ociosa; confianza alta. | Una sola fuente concentra la línea. Los descuentos nominales son **27–55 %**, mientras el ahorro propio observado es **1,1 %**; no son la misma medida ni se infiere ahorro generalizable. |
| T2 Inteligencia y análisis de precios cloud | **Primarias:** `FP76-080` y `FP76-002` (textos completos verificados). **Secundaria/sublinea:** `FP76-117`. **Contexto/no-forecast:** `FP76-043`. | Análisis de asimetrías por tipo, región y modalidad; confianza media-alta. | Forecasting no es el paraguas: `FP76-117` reporta autocorrelación severa y `FP76-043` declara predicción pero no la evalúa. Comparar precios no equivale a seleccionar proveedor ni a una tarifa vigente. |
| T3 Conciencia de costos *shift-left* en IaC | **Primaria conductual:** `FP76-041`; **secundaria de magnitud simulada:** `FP76-037` (ambos textos completos verificados). | Decisión de costo temprana en configuración/diseño; confianza media. | `FP76-041` conserva `B1=1` y no mide ahorro productivo. `FP76-037` mide magnitud simulada, no producción; ninguna fuente convierte conducta IaC en ahorro realizado. |
| Economía unitaria de GenAI/LLM | **Primarias:** `FP76-134` y `FP76-332` (textos completos verificados). | Costo por token, solicitud, inferencia o valor; confianza media-alta. | Conservar precios de lista y el límite de generalización AWS `us-west-2`; no convertir resultados de arquitectura/carga en precio pagado universal. |

**Contexto excluido de evidencia primaria final.** T1 guardrails y FinOps agéntico son contexto, no tendencias seleccionadas. `FP76-289` permanece Reserva/contexto: el titular de 94 % no es trazable en el cuerpo y el cuerpo reporta violaciones presupuestarias. Forecasting y selección multi-cloud/proveedor permanecen sublíneas. La cobertura se cerró en 13 textos verificados; 17 textos no disponibles no sustentan afirmaciones primarias y no habrá nueva recuperación.

## Integración de Versión 3 validada por Danilo (2026-09-20)

La Versión 3 fue validada humanamente por Danilo el 2026-09-20. Esta constancia no implica aprobación de equipo ni docente, ni sustituye las retenciones de procedencia o la ratificación FP-180.

**Tres sobreinterpretaciones prohibidas.** No atribuir el 85 % a la síntesis de `FP76-195` (es una cifra externa transportada); no presentar el 94 % de `FP76-289` como resultado trazable o uniforme (el cuerpo reporta violaciones); ni convertir el 80 % citado en un *commit* de `FP76-041` en ahorro promedio del estudio. Además, `FP76-043` no valida pronóstico temporal: sus casos verificables son regresión hedónica transversal y *clustering*; el aprendizaje predictivo queda como trabajo futuro.

**Caveat E0–E4.** La escala E0–E4 de la Versión 3 es una propuesta preliminar del equipo para esta revisión, sin validación externa; no es un estándar FinOps. E2 con datos de producción sigue siendo contrafactual y no es E3; E3 exige medición posterior a implementar en un entorno acotado; E4 exige gasto facturado y sostenido en producción. Entre los 13 textos verificados no hay evidencia E4.
