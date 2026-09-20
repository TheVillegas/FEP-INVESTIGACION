# FP-76 — Análisis comparativo, discusión crítica, aporte propio, conclusiones, recomendaciones y cuestionario

**Versión 3 — validada humanamente por Danilo.** 2026-09-20.

**Estado: validación humana de Danilo completada el 2026-09-20.** Esta validación no sustituye la
ratificación metodológica pendiente de FP-180 ni implica aprobación de equipo o docente.

**Cambios de esta revisión:** se incorporan las cinco salvedades finales aprobadas por Danilo: se explicita
que E0–E4 es una propuesta preliminar del equipo, sin validación externa y no un estándar FinOps; el umbral
E3 se identifica como precaución normativa para este trabajo; se documenta la asimetría de la evidencia y la
obligación de conservarla en resúmenes y diapositivas; se agrega trazabilidad bibliográfica completa de los
13 IDs; y se separa el cuestionario maestro de una copia de aplicación. Se conserva la reclasificación de
FP76-100 y FP76-019 a `E2 con datos de producción`, el nivel E4 vacío, las acotaciones sobre el estado del
campo y GenAI, la cadena T3 compuesta entre dos fuentes y los distractores equilibrados.

**Alcance de evidencia:** 13 textos completos verificados contra su PDF (12 candidatos y FP76-289 como
contexto). Toda cifra lleva página. Los 17 textos no disponibles quedan fuera por decisión de alcance y no
sustentan ninguna afirmación de este documento.

**Selección de tendencias cerrada (aprobada 2026-09-20):** cuatro tendencias.

1. Compromisos, descuentos y capacidad spot.
2. T2 Inteligencia y análisis de precios cloud.
3. T3 Conciencia de costos *shift-left* en IaC.
4. Economía unitaria de GenAI/LLM.

Pronóstico de precios y selección multi-cloud o de proveedor quedan como **sublíneas**. Guardrails
presupuestarios, FinOps agéntico y FP76-289 quedan como **contexto**.

**Política B1 vigente:** B1 evalúa si el efecto económico es directo y medible; la cifra no necesita figurar
en el título ni en el resumen y puede confirmarse en el texto completo.

---

## 1. Análisis comparativo

### 1.1 Tendencias seleccionadas y su base de evidencia

| # | Tendencia | Fuentes verificadas | Naturaleza de la evidencia | Puntaje B |
|---|---|---|---|---|
| 1 | Compromisos, descuentos y capacidad spot | FP76-100 | Traza real de producción de tres años, multi-nube; resultado contrafactual, no ahorro facturado | 21 |
| 2 | T2 Inteligencia y análisis de precios cloud | FP76-080, FP76-002, FP76-117, FP76-043 | Precios reales, revisión sistemática, pronóstico y análisis de políticas | 18, 19, 18, 16 |
| 3 | T3 Conciencia de costos *shift-left* en IaC | FP76-041, FP76-037 | Minería de repositorios y simulación calibrada | 19, 15 |
| 4 | Economía unitaria de GenAI/LLM | FP76-134, FP76-332 | Evaluación en plataforma real y sistema evaluado en AWS | 20, 18 |

**Líneas no seleccionadas y su tratamiento**

| Línea | Tratamiento | Fuente verificada | Motivo |
|---|---|---|---|
| Pronóstico de precios | Sublínea de T2 | FP76-117 | Autocorrelación severa declarada por los autores (p. 12) |
| Multi-cloud o broker por costo | Sublínea de selección de proveedor | FP76-230 | Ahorro verificado de magnitud baja: 6,12 y 11,56 USD mensuales (pp. 5–6) |
| Guardrails presupuestarios | Contexto | FP76-019 | Fuente primaria sólida, sin corroboración verificada |
| FinOps agéntico o automatizado | Contexto | FP76-195 | Única fuente verificada es una revisión cuya cifra principal es externa |
| Advertencia metodológica | Contexto, en Reserva | FP76-289 | El 94% del resumen no es trazable en el cuerpo |

### 1.2 Comparación por cadena causal

| Tendencia | Cambio observable | Mecanismo económico | Variable observable | Respuesta FinOps |
|---|---|---|---|---|
| Compromisos y spot | Cargas multi-nube dinámicas frente a mercados de compromiso | Descuento por compromiso contra riesgo de capacidad ociosa | Descuento efectivo y porcentaje de capacidad comprometida sin usar | Definir nivel y escalonamiento de compromisos |
| T2 Precios cloud | Estructuras de precio heterogéneas entre tipos, regiones y modalidades | Asimetría de precio entre configuraciones equivalentes | Precio por hora y ganancia relativa por tipo de instancia | Plan de reservas y selección informada de configuración |
| T3 Shift-left en IaC | El costo empieza a decidirse en el artefacto de infraestructura | Decisión temprana de configuración antes del despliegue | Proporción de cambios con intención de costo y costo estimado por configuración | Revisión de costos en diseño y en *pull request* |
| GenAI unitaria | Aparición de nuevos objetos de costo: token, solicitud e inferencia | Costo por unidad de valor entregada | Costo por hora y por unidad, exactitud por dólar | Elegir modalidad de despliegue e infraestructura interrumpible |

Las cuatro pueden representarse mediante la cadena `cambio → mecanismo económico → variable observable →
respuesta FinOps`. En T3 sus componentes provienen de **dos fuentes distintas** y no constituyen una
validación integrada: FP76-041 aporta el cambio observable y FP76-037 la magnitud, obtenida en simulación.

### 1.3 Comparación por calidad de evidencia

| Eje | Compromisos y spot | T2 Precios | T3 Shift-left | GenAI unitaria |
|---|---|---|---|---|
| Entorno | Traza de producción real, resultado contrafactual | Precios reales de proveedor | Repositorios reales y simulación | Plataforma real |
| Trazabilidad de cifras | Alta, con denominador explícito | Alta en FP76-080 | Partida entre dos fuentes | Alta |
| Efecto económico directo | Sí | Sí, concentrado en una fuente | No agregado | Sí |
| Dependencia de simulación | Baja | Baja | **Alta en FP76-037** | Baja |
| Dependencia de revisiones | Nula | Media, por FP76-002 | Nula | Nula |
| Evidencia contradictoria interna | Ahorro propio modesto frente al descuento nominal | **FP76-043 no pronostica; FP76-117 con autocorrelación** | Ninguna fuente mide ahorro productivo | Unidades no homogéneas entre plataformas |
| Diversidad de fuentes verificadas | 1 | 4 | 2 | 2 |
| Riesgo de sobreinterpretación | Medio | **Alto** | Medio | Medio |

### 1.4 Cifras verificadas

**Compromisos, descuentos y capacidad spot — FP76-100**
- Descuentos de mercado de 27–37% a un año y 50–55% a tres años, según proveedor y familia de instancia (Tabla 2, p. 4).
- Bajo demanda cuesta aproximadamente 2,1 veces el precio del compromiso a tres años (p. 4).
- Ahorro propio del escalonamiento de compromisos: 1,1% frente al escenario de compromiso plano (p. 7).
- Capacidad comprometida sin usar en el nivel óptimo: 4,3% (p. 8).
- Datos: traza multi-nube de Snowflake de aproximadamente tres años, publicada de forma normalizada.

**T2 Inteligencia y análisis de precios cloud — FP76-080, FP76-002, FP76-117, FP76-043**
- Ganancia relativa de 0% a 93,897% según tipo de máquina, con precios reales de GCP del 5 de noviembre de 2023 (Tablas 7–9, pp. 14–16).
- Mejora de 31,4% en RMSE del modelo TFT frente al mejor método base (FP76-080, p. 1).
- Solo 19% de los estudios primarios revisados, 14 de 75, mide un resultado económico; el 81% restante reporta únicamente métricas técnicas (FP76-002, p. 26).
- Precios verificados por categoría: 0,25 USD/hora en *xsmall* frente a 1,75 USD/hora en *large* (FP76-043, p. 17).
- Error de pronóstico por modelo y producto en MAPE (FP76-117, pp. 9–11), con autocorrelación severa de residuos declarada por los propios autores (p. 12).

**T3 Conciencia de costos shift-left en IaC — FP76-041, FP76-037**
- 70% de los *commits* pertinentes corresponde a una categoría de conciencia de costos (FP76-041, p. 6).
- Ejemplo anecdótico citado en un *commit*: reducción de 80% en costos de métricas (p. 6). No es una medición del estudio.
- Reducción de costo de 92,93% a 95,39% frente a la peor configuración simulada, con tabla de precios en dólares (FP76-037, p. 26), obtenida en CloudSim sobre 256 configuraciones sintéticas.
- Los modelos de costo y calidad de servicio de FP76-037 se calibran con mediciones reales de laboratorio sobre dos aplicaciones (pp. 15–16).

**Economía unitaria de GenAI/LLM — FP76-134, FP76-332**
- Costo por hora de 11,64 USD frente a 6,29 USD en el ejemplo motivador (FP76-332, p. 2).
- 27,16, 17,05 y 18,15 USD por ventana de 50 minutos según configuración (p. 11).
- Mejora de eficiencia de costo de 31,9% y 31,2% frente al uso exclusivo de instancias bajo demanda (pp. 1, 12 y 14).
- Correlación entre costo y exactitud: R² de 0,639; entre tamaño de modelo y exactitud: R² de 0,727 (FP76-134, p. 1).
- Comparación serverless contra BYOC en seis dimensiones, incluida disponibilidad de 34,4% frente a 32 de 32 y observabilidad de aproximadamente 12 métricas frente a más de 42 (Tabla 12, p. 16).

**Contexto — FP76-019 y FP76-230**
- FP76-019: el método propuesto es más de 100 veces más rápido que NSGA-II con N igual a 10.000, del orden de 10² a 10³ milisegundos por decisión frente a 10⁵ (p. 32, reiterado en p. 45), validado con traza real Google ClusterData 2011.
- FP76-230: ahorros de 6,12 y 11,56 USD mensuales medidos con APIs reales de facturación sobre aplicaciones de demostración (pp. 5–6).

### 1.5 Solapamiento entre las tendencias seleccionadas

- **Compromisos** y **T2 precios** comparten el objeto precio. Frontera adoptada: T2 analiza la estructura de precios; compromisos decide la contratación y administra su riesgo.
- **GenAI unitaria** usa capacidad interrumpible en FP76-332, lo que la acerca a compromisos. Frontera adoptada: GenAI mide costo por unidad de valor entregada; compromisos mide costo por capacidad reservada.
- **T3 shift-left** se distingue por el momento de la decisión: antes del despliegue, no durante la operación.
- Los guardrails presupuestarios, que quedan como contexto, se distinguen de compromisos porque limitan en ejecución en lugar de comprar por adelantado.

---

## 2. Discusión crítica

### 2.1 La brecha entre lo que se promete y lo que se mide

El hallazgo de fondo no pertenece a ninguna tendencia en particular, sino al estado del campo: **solo 19% de
los estudios primarios sobre optimización de costos cloud mide un resultado económico** (FP76-002, p. 26).
El 81% restante se limita a métricas técnicas. Dentro de ese corpus, la mayoría de los trabajos que se
presentan como optimización de costos optimiza *proxies* técnicos y asume, sin demostrarlo, que el ahorro se
sigue.

Ese número es coherente con el resultado del cribado de FP-76: de 348 registros recuperados, 147 se
excluyeron porque el costo aparecía como un objetivo más junto a *makespan*, energía o latencia. No es un
artefacto del filtro aplicado, sino un patrón observado en el corpus revisado por FP76-002 y en el cribado
realizado para FP-76. El universo observado no equivale a toda la literatura de FinOps.

### 2.2 Tres formas distintas de decir "ahorro"

La verificación de textos completos mostró que la palabra ahorro encubre tres cosas incompatibles:

1. **Descuento contractual de mercado**, verificable en la lista de precios del proveedor. Ejemplo: 50–55%
   por compromiso a tres años (FP76-100, Tabla 2, p. 4). Es real, pero es un precio, no un resultado.
2. **Ahorro medido sobre datos de consumo reales**, con dos grados internos: el contrafactual, calculado
   sobre una traza real de producción sin implementar la decisión, como el 1,1% por escalonamiento de
   compromisos (FP76-100, p. 7); y el facturado, medido sobre gasto efectivo, como los 6,12 y 11,56 USD
   mensuales por migración (FP76-230, pp. 5–6), obtenidos en aplicaciones de demostración.
3. **Ahorro potencial simulado**, calculado contra un peor caso construido. Ejemplo: 92,93% a 95,39%
   (FP76-037, p. 26), donde el comparador es la configuración más cara de un espacio de 256 alternativas
   sintéticas.

La distancia entre el primero y el segundo es el punto crítico y suele quedar invisible. FP76-100 documenta
descuentos nominales de hasta 55%, pero su propio resultado de optimización es 1,1%: **el descuento grande ya
estaba capturado; lo que queda por optimizar es el margen**. Un informe que cite el 55% como resultado
alcanzable estaría construyendo una afirmación falsa con datos verdaderos.

### 2.3 Cuando la cifra más citada no pertenece al estudio que la cita

FP76-195 encabeza sus resultados con "hasta 85% de reducción de costos" (pp. 14 y 16–17). Esa cifra **no
proviene de sus 18 estudios primarios**: proviene de una fuente externa citada, ausente de su tabla de
estudios incluidos. La revisión no la produjo ni la validó, la transporta. Atribuirla a la síntesis fabrica
una autoridad inexistente.

El caso no es aislado. FP76-289 declara 94% de cumplimiento de presupuesto en su resumen (p. 1), pero ese
número no aparece en el cuerpo, y sus secciones de resultados muestran violaciones de presupuesto en dos de
los flujos evaluados bajo intervalos largos de aprovisionamiento (pp. 18–23). Por eso pasó a Reserva y se
conserva como advertencia, no como evidencia.

### 2.4 El pronóstico de precios es más frágil de lo que aparenta

La sublínea de pronóstico enfrenta dos problemas encadenados:

- **FP76-043** no pronostica. Su Caso 1 es una regresión hedónica transversal de factores de precio
  (pp. 15–16) y su Caso 2 es *clustering* K-Means para comparar costos (pp. 16–17). La predicción figura
  como capacidad del framework y su propio trabajo futuro pide incorporar aprendizaje automático predictivo
  (p. 19).
- **FP76-117** sí pronostica precios spot de AWS y reporta errores bajos en MAPE (pp. 9–11), pero su propia
  prueba de Durbin-Watson revela autocorrelación severa en los residuos (p. 12). Los autores lo declaran: un
  error bajo es compatible con un modelo que repite el último valor observado, no con capacidad predictiva
  genuina.

Consecuencia directa: **en la evidencia verificada no existe un caso que demuestre que pronosticar precios
cloud produce un ahorro medido**. Sí existe análisis de precios que lo produce, FP76-080, que es una cosa
distinta. Por eso la tendencia se llama inteligencia y análisis de precios, y el pronóstico queda como
sublínea acotada.

### 2.5 La evidencia conductual no es inferior, es otra cosa

FP76-041 demuestra que los equipos modifican artefactos de infraestructura con intención explícita de costo:
70% de los *commits* pertinentes cae en esa categoría (p. 6). No cuantifica cuánto se ahorra, y por eso
conserva B1 igual a 1. Aun así es la única evidencia verificada de que **el cambio de conducta está
ocurriendo**.

Probar que una tendencia existe y probar que rinde son preguntas distintas que requieren métodos distintos.
La minería de repositorios responde la primera; la simulación calibrada de FP76-037 responde parcialmente la
segunda. Juntas forman la cadena de T3; por separado, ninguna la completa. Esa dependencia es la principal
debilidad declarada de esta tendencia.

### 2.6 Lo que la evidencia disponible no permite afirmar

- Que el *shift-left* en IaC produzca ahorro medible en producción. Ninguna fuente verificada lo midió.
- Que el pronóstico de precios mejore decisiones de compra. No hay caso con resultado económico.
- Que los guardrails presupuestarios constituyan una práctica difundida. Hay un trabajo sólido, no un patrón.
- Que la automatización agéntica de FinOps tenga efecto verificado.
- Que multi-cloud por costo sea económicamente significativo a escala: los ahorros verificados equivalen a
  cerca de 2–3% del costo mensual de una aplicación de demostración (FP76-230, pp. 5–6).

### 2.7 Límite declarado de esta discusión

Esta lectura se apoya en 13 textos completos verificados. Los 17 restantes de la lista priorizada quedaron
fuera de alcance por decisión explícita y no se planifica su recuperación. Entre ellos hay candidatos con
puntaje alto en compromisos y spot, en GreenOps y en FinOps agéntico, de modo que **la jerarquía entre
tendencias podría verse distinta con más lectura**. Lo que no depende del volumen de fuentes es la
distinción entre descuento, ahorro observado y ahorro simulado, porque es metodológica.

---

## 3. Aporte propio

### 3.1 El problema que motiva el aporte

Durante el cribado de 348 registros y la verificación de 13 textos completos apareció un patrón repetido:
las fuentes mezclan niveles de evidencia económica incompatibles y el lector los recibe como equivalentes.
Un descuento de lista, un ahorro simulado contra un peor caso y un ahorro observado en producción se
presentan con el mismo formato de porcentaje.

En los marcos y fuentes revisados en este trabajo no se identificó un criterio explícito equivalente para
decidir **cuánto peso dar a una cifra de ahorro según cómo fue obtenida**.

### 3.2 Propuesta preliminar de clasificación: escala de trazabilidad económica E0–E4

El equipo propone, de forma preliminar y sin validación externa, clasificar toda afirmación de ahorro en cinco
niveles según su origen y su comparador. **E0–E4 no es un estándar FinOps ni un marco validado externamente**:
es una herramienta de trabajo de este equipo para esta revisión.

| Nivel | Nombre | Qué es | Comparador | Uso admisible |
|---|---|---|---|---|
| **E0** | Afirmación comercial o no trazable | Porcentaje sin método ni comparador verificable | Ninguno | Solo para formular preguntas |
| **E1** | Precio de lista | Diferencia entre tarifas publicadas | Otra tarifa publicada | Estimar techo teórico |
| **E2** | Ahorro modelado o contrafactual | Resultado de modelo, simulación o cálculo contrafactual, aunque use datos reales como insumo | Peor caso, base construida o escenario no implementado | Priorizar experimentos |
| **E3** | Ahorro observado acotado | Medición real sobre gasto o consumo tras implementar la decisión, en entorno controlado o aplicación no productiva | Estado previo real | Sustentar un piloto |
| **E4** | Ahorro facturado en producción | Medición sobre gasto efectivo y sostenido de cargas productivas tras la implementación | Estado previo real y sostenido | Sustentar decisión de inversión |

Dentro de E2 se distingue una banda superior, **E2 con datos de producción**, para resultados contrafactuales
calculados sobre trazas reales. Usan datos de consumo genuinos, pero la decisión nunca se implementó y, por
lo tanto, no hay gasto facturado que comparar.

Clasificación de la evidencia verificada de FP-76:

| Fuente | Cifra | Nivel |
|---|---|---|
| FP76-100, descuentos 27–55% (p. 4) | Tarifa de compromiso | **E1** |
| FP76-100, 1,1% por escalonamiento (p. 7) | Optimización contrafactual sobre traza real normalizada de tres años; no hay gasto facturado tras implementar | **E2 con datos de producción** |
| FP76-080, 0–93,897% de ganancia relativa (pp. 14–16) | Plan calculado sobre precios reales | **E2 con insumo E1** |
| FP76-037, 92,93–95,39% (p. 26) | Simulación contra peor caso | **E2** |
| FP76-332, 31,9% y 31,2% (pp. 1, 12, 14) | Medición en AWS us-west-2 | **E3** |
| FP76-134, costo por hora (p. 18) | Precios de lista EC2 sin descuentos | **E1** |
| FP76-230, 6,12 y 11,56 USD mensuales (pp. 5–6) | Facturación real, aplicación de demostración | **E3** |
| FP76-019, reducción de violaciones (p. 31) | Resultado computacional con traza real Google ClusterData 2011 como insumo; su cifra de "más de 100 veces" (p. 32) es velocidad de cómputo frente a NSGA-II, no ahorro económico | **E2 con datos de producción** |
| FP76-041, 80% en un *commit* (p. 6) | Cita anecdótica | **E0** |
| FP76-195, 85% (p. 14) | Cifra externa transportada | **E0** |
| FP76-289, 94% (p. 1) | No trazable en el cuerpo | **E0** |

### 3.3 Regla de uso propuesta

El umbral E3 de esta sección es una **precaución normativa adoptada por el equipo para este trabajo**; no es
un umbral universal demostrado empíricamente ni una prescripción de FinOps.

1. Ninguna recomendación de inversión se sostiene con evidencia por debajo de **E3**.
2. Una tendencia requiere al menos una fuente **E3 o E4** para presentarse como sustentada para decidir;
   **E1 y E2** la acompañan y permiten admitirla como tendencia, pero no sostienen una inversión.
3. Toda cifra citada se acompaña de su nivel, su comparador y su página.
4. Elevar el nivel de una cifra en la redacción, por ejemplo citar un E1 como si fuera E4, se trata como
   error de evidencia y no como decisión de estilo.

### 3.4 Aplicación a las tendencias seleccionadas

| Tendencia seleccionada | Mejor nivel verificado | Lectura |
|---|---|---|
| Economía unitaria GenAI/LLM | **E3** (FP76-332) | Única de las cuatro que alcanza el umbral para sustentar un piloto |
| Compromisos, descuentos y spot | **E2 con datos de producción** (FP76-100) | Mejor calidad de datos de entrada del conjunto, pero resultado contrafactual y fuente única |
| T2 Inteligencia y análisis de precios | **E2 con insumo E1** (FP76-080) | Sustentada como análisis, no como promesa de ahorro |
| T3 Shift-left en IaC | **E2** (FP76-037), acompañada de evidencia conductual E0 | Sustentada como cambio observable, no como magnitud |

**Ninguna de las cuatro alcanza E4 y solo una alcanza E3.** El nivel E4 queda vacío en todo el corpus
verificado: no hay, entre los 13 textos, una medición de gasto facturado y sostenido tras implementar una
decisión FinOps. Esa ausencia es en sí misma un resultado de la revisión y es consistente con el 19% de
FP76-002.

Conviene ser explícito sobre la relación entre ambos marcos: la selección de las cuatro tendencias se decidió
con el marco A/B aprobado en la Etapa 1, no con esta escala. La escala se aplica después y mide otra cosa,
la madurez de la evidencia disponible para decidir. Leídas juntas, muestran que las cuatro tendencias están
correctamente admitidas como tendencias y que, al mismo tiempo, solo una sostiene hoy una decisión de
inversión.

La escala hace visible algo que el puntaje B no distingue: **dos fuentes con puntajes similares pueden tener
capacidad de decisión muy distinta**. FP76-041 suma 19 puntos con B1 igual a 1 y nivel E0 en su única
magnitud; FP76-100 suma 21 con nivel E2 sobre datos de producción. Ambos son buenos trabajos y ninguno de
los dos, por sí solo, sostiene una decisión de inversión.

### 3.5 Aplicación al caso del equipo

La línea base económica del equipo compara Chile Central, 23.256,32 USD, con East US, 16.474,60 USD, a 60
meses: una prima regional cercana a 41%. La escala permite formular la pregunta correcta: **ninguna de las
tendencias seleccionadas produce, con evidencia E3 o E4, un ahorro del orden de esa prima**. El mejor
resultado calculado sobre datos de producción es 1,1% (FP76-100, p. 7) y el mayor medido en entorno real es
31,9% sobre una carga específica de inferencia (FP76-332, p. 1).

Esto ordena la decisión: la elección de región es una decisión estructural de magnitud mayor que cualquier
optimización operacional documentada en esta revisión. La evidencia revisada no demuestra que las prácticas
FinOps evaluadas compensen una diferencia estructural de localización de esa magnitud. Nota de alcance: esa línea
base proviene de FP-187/188 con proxies provisionales, de modo que la comparación es de orden de magnitud y
no un cálculo definitivo.

---

## 4. Conclusiones

1. **En el corpus revisado, la investigación sobre costos cloud mide poco lo económico.** Solo 19% de los
   estudios primarios revisados por FP76-002 reporta un resultado económico (p. 26), y el cribado de FP-76
   muestra el mismo patrón. Es una limitación del universo observado, no una afirmación sobre toda la
   literatura FinOps.
2. **Compromisos, descuentos y capacidad spot tiene los mejores datos de entrada del conjunto.** Es la única
   con una traza longitudinal de producción de tres años y multi-nube, más descuentos contractuales
   verificables. Su resultado propio de 1,1% es contrafactual: se calcula sobre esa traza, sin implementar la
   decisión, de modo que no constituye ahorro facturado (FP76-100, p. 7).
3. **El margen incremental estimado de optimización es mucho menor que el descuento nominal.** Frente a descuentos de lista
   de hasta 55%, la optimización del nivel de compromiso rinde 1,1% adicional y deja 4,3% de capacidad
   comprometida sin usar (FP76-100, pp. 4, 7 y 8).
4. **El pronóstico de precios no está demostrado como palanca económica.** FP76-043 no pronostica y FP76-117
   declara autocorrelación severa (p. 12). Por eso T2 se define como inteligencia y análisis de precios, con
   el pronóstico como sublínea acotada.
5. **La economía unitaria de GenAI es la línea más nueva y la mejor cubierta dentro de esta ola.** Dentro de
   la primera ola seleccionada, fue la única línea cuyos dos candidatos priorizados tuvieron texto completo
   disponible y verificado, y ambos reportan cifras propias, con 31,9% de mejora de eficiencia de costo
   medida en AWS (FP76-332). No debe entenderse como cobertura exhaustiva de la literatura sobre GenAI.
6. **El shift-left en IaC está probado como conducta, no como ahorro.** FP76-041 demuestra que ocurre y
   FP76-037 estima cuánto podría rendir, pero en simulación contra un peor caso.
7. **Los guardrails presupuestarios quedaron como contexto por falta de corroboración.** FP76-019 es sólido;
   su único acompañante fue descartado como evidencia por no ser trazable.
8. **Tres cifras que circulan como resultados no lo son:** el 85% de FP76-195, el 94% de FP76-289 y el 80%
   de FP76-041. Las tres quedan registradas como sobreinterpretaciones prohibidas.
9. **La capacidad de decisión de una fuente no coincide con su puntaje.** La escala E0–E4 es una propuesta
   preliminar del equipo para este trabajo, no un estándar FinOps ni un marco validado externamente; separa
   ambas cosas y muestra que **solo una de las cuatro tendencias seleccionadas, economía unitaria de GenAI,
   alcanza hoy nivel E3, y ninguna alcanza E4**. No hay en los 13 textos verificados una medición de gasto
   facturado y sostenido tras implementar una decisión FinOps.

---

## 5. Recomendaciones

### 5.1 Uso de la evidencia en el informe

1. Acompañar cada cifra con su nivel E0–E4, su comparador y su página.
2. No citar descuentos de lista como ahorro alcanzable; en particular, no presentar el 55% de FP76-100 como
   resultado de una práctica FinOps.
3. No citar cifras simuladas sin nombrar el comparador, en particular el 92,93–95,39% de FP76-037, cuyo
   comparador es el peor caso de un espacio sintético.
4. No atribuir a una revisión las cifras que solo transporta; el 85% de FP76-195 pertenece a una fuente
   externa.
5. No presentar los MAPE bajos de FP76-117 como precisión real sin exponer la autocorrelación declarada.
6. Declarar explícitamente que en T3 la cadena causal se compone entre dos fuentes distintas y no constituye
   una validación integrada.
7. Declarar el alcance cerrado en 13 textos verificados y 17 no disponibles como limitación del trabajo.
8. Conservar en todo resumen, diapositiva o comunicación la asimetría de evidencia: compromisos y spot se
   apoyan en una sola fuente; T3 reparte su cadena entre dos estudios; y el efecto económico de T2 se
   concentra en FP76-080.

### 5.2 Práctica FinOps para la organización del caso

8. Medir la capacidad comprometida sin usar. Es la variable que FP76-100 identifica como el costo real del
   compromiso y rara vez se monitorea.
9. Tratar la decisión de región como decisión estructural y separada: la prima regional de la línea base
   supera cualquier ahorro operacional verificado en esta revisión.
10. Incorporar revisión de costos en el artefacto de infraestructura antes del despliegue, aceptando que su
    beneficio está probado como conducta y no como magnitud.
11. Si se despliegan cargas de inferencia, medir costo por unidad de valor, por token o por solicitud, y no
    solo costo por hora de instancia.
12. Exigir nivel E3 o E4 antes de comprometer inversión. Hoy solo economía unitaria de GenAI lo alcanza, de
    modo que las otras tres tendencias corresponden a experimentación acotada y medición propia antes de
    cualquier compromiso de gasto.
13. Cerrar la brecha E4 con medición propia: registrar gasto facturado antes y después de cada cambio
    implementado, que es exactamente el dato que ninguna fuente verificada aporta.

### 5.3 Cierre de FP-76

14. Registrar en FP-189 las tres sobreinterpretaciones prohibidas y la corrección sobre FP76-043.
15. Reflejar en FP-190 la selección de cuatro tendencias, con sus sublíneas y su contexto.
16. Entregar a FP-191 las cifras con su nivel E0–E4 y a FP-192 las tensiones documentadas en la sección 2.
17. Cerrar la ratificación metodológica pendiente de FP-180 antes del informe final.

---

## 6. Trazabilidad bibliográfica final

La siguiente tabla mapea los 13 IDs verificados citados en este documento a los campos bibliográficos del
libro **[`Revision papers - cribado FP-76.xlsx`](../evidencia/Revision%20papers%20-%20cribado%20FP-76.xlsx)**. Se transcriben título, año, fuente o sede y DOI; si un campo
no estuviera disponible se marcaría como **No disponible en el libro**. En estos 13 registros no faltan esos
cuatro campos.

| ID | Título completo | Año | Fuente o sede | DOI |
|---|---|---:|---|---|
| FP76-002 | Bridging FinOps practice and machine learning research: a systematic review of cloud cost optimization | 2026 | PEERJ COMPUTER SCIENCE | 10.7717/peerj-cs.3964 |
| FP76-019 | FinOps-Aware Budget-Constrained Optimization for Cloud Resource Management | 2026 | APPLIED SCIENCES-BASEL | 10.3390/app16073302 |
| FP76-037 | Model-based cloud service deployment optimisation method for minimisation of application service operational cost | 2023 | JOURNAL OF CLOUD COMPUTING-ADVANCES SYSTEMS AND APPLICATIONS | 10.1186/s13677-023-00389-8 |
| FP76-041 | Mining for cost awareness in the infrastructure as code artifacts of cloud-based applications: An exploratory study | 2024 | JOURNAL OF SYSTEMS AND SOFTWARE | 10.1016/j.jss.2024.112112 |
| FP76-043 | Cloud PricingOps: A Decision Support Framework to Explore Pricing Policies of Cloud Services | 2024 | APPLIED SCIENCES-BASEL | 10.3390/app142411946 |
| FP76-080 | FinOps-driven optimization of cloud resource usage for high-performance computing using machine learning | 2024 | JOURNAL OF COMPUTATIONAL SCIENCE | 10.1016/j.jocs.2024.102292 |
| FP76-100 | Shaved Ice: Optimal Compute Resource Commitments for Dynamic Multi-Cloud Workloads | 2025 | PROCEEDINGS OF THE 16TH ACM/SPEC INTERNATIONAL CONFERENCE ON PERFORMANCE ENGINEERING, ICPE 2025 | 10.1145/3676151.3719353 |
| FP76-117 | Forecasting AWS Spot Prices: Comparative Analysis of Deep Learning Architectures and Residual Auto-Correlation | 2025 | SERVICE ORIENTED COMPUTING AND APPLICATIONS | 10.1007/s11761-025-00475-6 |
| FP76-134 | Cloud-Based Large Language Model Deployment: A Comparative Analysis of Serverless and Bring-Your-Own-Container Architectures | 2026 | ACTA INFORMATICA PRAGENSIA | 10.18267/j.aip.313 |
| FP76-195 | AI-driven optimization in cloud computing: a systematic review of cost, resource management, and security | 2026 | FRONTIERS IN ARTIFICIAL INTELLIGENCE | 10.3389/frai.2026.1750992 |
| FP76-230 | COSTA: A cost-driven solution for migrating applications in multi-cloud environments | 2023 | 38TH ANNUAL ACM SYMPOSIUM ON APPLIED COMPUTING, SAC 2023 | 10.1145/3555776.3577718 |
| FP76-289 | Budget-based resource provisioning and scheduling algorithm for scientific workflows on IaaS cloud | 2023 | MULTIMEDIA TOOLS AND APPLICATIONS | 10.1007/s11042-023-17549-2 |
| FP76-332 | ShuntServe: Cost-efficient LLM serving on heterogeneous spot GPU clusters | 2027 | FUTURE GENERATION COMPUTER SYSTEMS-THE INTERNATIONAL JOURNAL OF ESCIENCE | 10.1016/j.future.2026.108760 |

## 7. Cuestionario

**Esta versión maestra incluye la clave de respuestas y sus justificaciones.** Para aplicar el cuestionario,
se debe preparar una copia que elimine las respuestas y justificaciones y conservar por separado esta clave
para la persona facilitadora.

**Pregunta 1.** Según la revisión sistemática de FP76-002, ¿qué proporción de los estudios primarios sobre
optimización de costos cloud reporta un resultado económico medido?

- a) Cerca de 41%
- b) Cerca de 81%
- c) Cerca de 19%
- d) Cerca de 63%

*Respuesta: c.* FP76-002 documenta que 14 de 75 estudios primarios reporta un resultado económico (p. 26).
El 81% es la proporción complementaria: los estudios que solo reportan métricas técnicas.

**Pregunta 2.** Una organización obtiene 50% de descuento sobre la tarifa bajo demanda al firmar un
compromiso a tres años. ¿Cómo debe interpretarse ese 50% en un informe FinOps?

- a) Como ahorro atribuible a la práctica FinOps, siempre que la utilización del compromiso supere el 95%
- b) Como ahorro observado, dado que proviene de tarifas publicadas y verificables del proveedor
- c) Como ahorro potencial, equivalente al que produciría una optimización del nivel de compromiso
- d) Como precio contractual; el ahorro atribuible a la optimización es el margen adicional sobre esa tarifa

*Respuesta: d.* FP76-100 separa ambos planos: descuentos de 27–55% según plazo (Tabla 2, p. 4) frente a una
mejora propia de 1,1% por escalonamiento del compromiso (p. 7). El descuento es la condición de partida, no
el resultado de la práctica.

**Pregunta 3.** Según FP76-100, ¿qué costo relevante aparece al sobredimensionar un compromiso de capacidad?

- a) El recargo por conversión anticipada del plan contratado
- b) La capacidad comprometida que se paga y no se utiliza
- c) La pérdida del descuento por volumen aplicable a la capacidad bajo demanda
- d) El costo de transferencia entre zonas al redistribuir la carga comprometida

*Respuesta: b.* En el nivel óptimo del estudio queda 4,3% de capacidad comprometida sin usar (p. 8), y por
encima de ese nivel la fracción no utilizada crece. El estudio no compara de forma exhaustiva todos los
costos posibles de un compromiso.

**Pregunta 4.** Un modelo de pronóstico de precios spot reporta un MAPE muy bajo, pero su prueba de
Durbin-Watson indica autocorrelación severa en los residuos. ¿Qué corresponde concluir?

- a) El error bajo puede ser un artefacto estadístico y no evidencia de capacidad predictiva
- b) El modelo capta bien la estacionalidad de la serie, y la autocorrelación lo confirma
- c) La autocorrelación afecta los intervalos de confianza, pero no la validez del pronóstico puntual
- d) El problema es de tamaño de muestra y se corrige reentrenando con una serie más larga

*Respuesta: a.* Es lo que declaran los propios autores de FP76-117 (p. 12): un error bajo es compatible con
un modelo que repite el último valor observado. Por eso el pronóstico quedó como sublínea acotada.

**Pregunta 5.** ¿Qué demuestra la minería de artefactos de infraestructura como código respecto del
*shift-left* de costos?

- a) Que el 70% de los repositorios analizados redujo su gasto cloud
- b) Que la práctica rinde cerca de 80% de ahorro en el costo de métricas
- c) Que la intención de costo aparece solo en proyectos con práctica FinOps formalizada
- d) Que existe una conducta observable de conciencia de costos, sin cuantificar el ahorro que produce

*Respuesta: d.* FP76-041 clasifica 70% de los *commits* pertinentes como conciencia de costos (p. 6). Ese
porcentaje mide proporción de cambios, no de repositorios ni de ahorro; el 80% del texto es una cita
anecdótica de un solo *commit*.

**Pregunta 6.** Un estudio reporta una reducción de costos de 92,93% a 95,39% obtenida en simulación. ¿Qué
dato resulta imprescindible para interpretar esa cifra?

- a) El tamaño del espacio de configuraciones evaluado
- b) La versión del simulador y los parámetros de calibración empleados
- c) El comparador utilizado y el entorno en que se obtuvo el resultado
- d) La distribución de precios de proveedor usada para alimentar el modelo

*Respuesta: c.* En FP76-037 el comparador es la peor configuración de un espacio simulado de 256
alternativas en CloudSim (p. 26). Las otras opciones aportan contexto, pero sin comparador la cifra sugiere
un ahorro alcanzable que nunca fue observado.

**Pregunta 7.** ¿Qué distingue la economía unitaria de GenAI de la optimización de costos tradicional?

- a) Introduce nuevos objetos de costo, como token o inferencia, y vincula costo con calidad entregada
- b) Sustituye el costo por hora de instancia por el costo por acelerador asignado
- c) Mide el costo del modelo en lugar del costo de la infraestructura que lo ejecuta
- d) Traslada el costo variable al proveedor mediante modalidades serverless

*Respuesta: a.* FP76-134 relaciona costo con exactitud, con R² de 0,639 (p. 1), y FP76-332 mide eficiencia de
costo por ventana de servicio (pp. 11 y 14). La opción d describe un cambio de modalidad, no una unidad
económica nueva.

**Pregunta 8.** Una revisión sistemática encabeza sus resultados con "hasta 85% de reducción de costos", pero
esa cifra proviene de una fuente citada y no de los estudios que sintetiza. ¿Cómo debe tratarse?

- a) Como resultado de la revisión, dado que superó su proceso de selección
- b) Como dato validado del corpus, porque la revisión lo incorporó al citarlo
- c) Como estimación del extremo superior del rango reportado por los estudios incluidos
- d) Como cifra de la fuente original citada, sin atribuirla a la síntesis de la revisión

*Respuesta: d.* Es el caso de FP76-195 (pp. 14 y 16–17): la cifra proviene de una fuente externa ausente de
su tabla de estudios incluidos, de modo que la revisión la transporta pero no la produce ni la valida.

**Pregunta 9.** Según la escala E0–E4 propuesta en este trabajo, ¿qué nivel mínimo se exige para sustentar
una decisión de inversión?

- a) E2 con datos de producción, cuando el cálculo se apoya en una traza real
- b) E3, un ahorro observado tras implementar la decisión en un entorno acotado
- c) E4 exclusivamente, porque solo el gasto facturado en producción es concluyente
- d) Cualquier nivel, siempre que la cifra declare comparador, unidad y página

*Respuesta: b.* La escala es una propuesta preliminar del equipo para este trabajo, no un estándar FinOps ni
un marco validado; reserva E1 y E2 para acompañar y exige E3 o E4 para sustentar inversión. Ese umbral es una
precaución normativa del equipo, no una regla universal demostrada empíricamente. La opción a describe
justamente el nivel que alcanzan FP76-100 y FP76-019, insuficiente para decidir.

**Pregunta 10.** La línea base del equipo muestra una prima regional cercana a 41% entre Chile Central y East
US a 60 meses, comparada como orden de magnitud. ¿Qué conclusión se sigue de la evidencia verificada?

- a) La prima se compensa combinando compromisos de capacidad con economía unitaria de inferencia
- b) La prima se compensa si las cargas de inferencia se ejecutan sobre capacidad interrumpible
- c) Ninguna tendencia verificada alcanza un ahorro de ese orden, por lo que la región es una decisión previa
- d) La prima regional puede compararse directamente con cualquier porcentaje de ahorro, sin considerar diferencias de carga, método o entorno

*Respuesta: c.* El mejor resultado calculado sobre datos de producción es 1,1% (FP76-100, p. 7) y el mayor
medido en entorno real es 31,9% sobre una carga específica de inferencia (FP76-332, p. 1). La comparación
vale como orden de magnitud y exige declarar las diferencias de carga, método y entorno, que es justamente
lo que la opción d omite.

---

## Limitaciones declaradas

1. El alcance de evidencia está cerrado en 13 textos completos verificados.
2. La escala E0–E4 es una propuesta preliminar del equipo para este trabajo, no un estándar FinOps ni un
   marco establecido o validado externamente, y no ha sido aplicada por evaluadores independientes. La
   frontera entre E2 con datos de producción y E3 es un juicio de este trabajo: separa el resultado
   contrafactual sobre datos reales de la medición posterior a implementar la decisión. El umbral E3 es una
   precaución normativa del equipo, no un umbral universal demostrado empíricamente.
3. Ninguna fuente verificada alcanza E4, de modo que las recomendaciones de la sección 5.2 se apoyan en
   evidencia E2 y E3 y requieren medición propia antes de comprometer gasto.
4. La comparación con la línea base económica del equipo usa proxies provisionales de FP-187/188 y vale como
   orden de magnitud, no como comparación homogénea entre escenarios.
5. Tres de las cuatro tendencias seleccionadas se apoyan en una o dos fuentes verificadas; solo T2 alcanza
   cuatro.
6. En T3 la cadena causal se compone entre dos fuentes distintas, no constituye una validación integrada y
   ninguna de las dos mide ahorro en producción.
7. La fuerza de evidencia es asimétrica: compromisos y spot dependen de una sola fuente; T3 distribuye su
   cadena entre dos estudios; y el efecto económico de T2 se concentra en FP76-080. Esta salvedad debe
   conservarse en resúmenes, diapositivas y cualquier comunicación derivada.
