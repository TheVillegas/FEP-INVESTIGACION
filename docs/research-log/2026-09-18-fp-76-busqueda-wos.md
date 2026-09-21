# FP-76 — Registro de la búsqueda WoS y preparación del cribado

- **Fecha:** 2026-09-18
- **Responsable:** Danilo Álvarez (validación humana); asistencia IA para control de calidad y preparación de la matriz.
- **Checklist de referencia:** `FEP TINV/FP-76/control/FP-76 - pendientes para Listo.md`, Pasos 1–3.

## Paso 1 — Evidencia de búsqueda congelada

| Campo | Valor |
|---|---|
| Archivo original | `FEP TINV/Revision papers.xls` (no modificado) |
| SHA-256 | `a0835239f0588ff4057b5e643d58e0eda6a7d9a246f7a4410e63674650a3a1ee` |
| Tamaño | 1.190.912 bytes |
| Base | Web of Science Core Collection (hoja exportada `savedrecs`) |
| Registros recuperados | 348 |
| Campos exportados | 72 columnas WoS, incluidas título, autores, fuente, año, resumen, palabras clave de autor y Keywords Plus, tipo documental, WoS Categories, Research Areas, Web of Science Index, citaciones WoS Core y totales, DOI y UT (Unique WOS ID) |
| Campo de búsqueda | Topic (TS) |
| Fecha y hora de consulta | 2026-09-18 12:00 (declarada por Danilo; la columna `Date of Export` viene vacía) |
| Selección de campos exportados | Identificación bibliográfica: Author(s), Title, Source, ISSN, Document Type, Language, WoS Editions. Relevancia: Abstract, Keywords, WoS Categories, Research Areas. Indicadores: Times Cited Count, Cited Reference Count, Open Access. Deduplicación: Authors Identifiers, IDS Number. Consistente con la exportación: los campos no seleccionados (Cited References, Addresses, Funding Orgs) vienen vacíos en los 348 registros. |
| Período aplicado | La exportación real cubre Publication Years 2023–2027 (declarado por Danilo). Años observados: 2023 (72), 2024 (104), 2025 (102), 2026 (67), 2027 (3). Esto es inconsistente con la ventana primaria de evidencia 2023–2026: los tres registros de 2027 quedan sin cambios hasta que una política humana resuelva su tratamiento. |
| Tipos documentales e idiomas | Sin filtros (declarado por Danilo; consistente con la exportación: 347 en inglés y 1 en ucraniano; incluye Article, Proceedings Paper, Review, Early Access y 1 retractado) |

### Topic exacto

```text
(
  (
    "cloud computing"
    OR "cloud service*"
    OR "cloud infrastructure"
    OR "public cloud"
    OR "cloud resource*"
    OR "cloud-based application*"
  )
  AND
  (
    FinOps
    OR PricingOps
    OR "cloud cost*"
    OR "cost-aware"
    OR "cost awareness"
    OR "cost management"
    OR "cost optimization"
    OR "cost optimisation"
    OR "budget-aware"
    OR "budget constrain*"
    OR "cloud pricing"
    OR "pricing polic*"
    OR "price intelligence"
    OR "price forecast*"
    OR "cost forecast*"
    OR "cost estimation"
  )
)
```

El SHA-256 del original se comprobó antes y después de generar la copia de trabajo, con el mismo resultado.

## Paso 2 — Calidad de la exportación

- 348 filas bibliográficas, sin contar el encabezado; coincide con el total observado en WoS.
- Duplicados exactos por DOI normalizado, UT y título normalizado: **0**.
- Posibles duplicados por título similar (similitud ≥ 0,85): **0**.
- Campos incompletos (no se completaron por inferencia):
  - sin DOI: 9;
  - sin palabras clave de autor: 6;
  - sin WoS Categories: 2;
  - sin Research Areas: 2.
- Alertas para el cribado:
  - 1 publicación retractada: DOI `10.3233/JIFS-234951`;
  - 5 registros *Early Access*;
  - 3 registros con año 2027, fuera de la ventana 2023–2026.
- Tipos documentales: Article 234; Proceedings Paper 99; Review 9; Article; Early Access 5; Article; Retracted Publication 1.

## Procedencia WoS de las fuentes ya utilizadas

Las seis referencias usadas en FP-190 y FP-189 están en la exportación. Todas figuran en Science Citation Index Expanded (SCI-EXPANDED):

| Uso | Referencia | DOI | UT | ID_FP76 |
|---|---|---|---|---|
| Primaria FP-190 | Cho (2026) | `10.3390/app16073302` | WOS:001738550000001 | FP76-019 |
| Primaria FP-190 | Fragiadakis et al. (2024) | `10.3390/app142411946` | WOS:001384311100001 | FP76-043 |
| Primaria FP-190 | Feitosa et al. (2024) | `10.1016/j.jss.2024.112112` | WOS:001249486500001 | FP76-041 |
| Secundaria FP-189 | Cheng et al. (2024), GeoScale | `10.1109/TPDS.2024.3366533` | WOS:001181441600003 | FP76-151 |
| Secundaria FP-189 | Smendowski & Nawrocki (2024) | `10.1016/j.knosys.2024.112489` | WOS:001313769600001 | FP76-089 |
| Secundaria FP-189 | Stupar & Huljenic (2023) | `10.1186/s13677-023-00389-8` | WOS:000934526300001 | FP76-037 |

Esto confirma su registro en WoS. No se infiere indexación en Scopus ni en SciELO.

## Paso 3 — Matriz de cribado

- **Copia de trabajo:** `FEP TINV/FP-76/evidencia/Revision papers - cribado FP-76.xlsx`.
- **Hojas:**
  - `cribado`: ID_FP76, columnas de cribado, columnas derivadas y las 72 columnas originales sin cambios;
  - `calidad`: inventario por columna y resumen;
  - `procedencia`: hash, metadatos y campos de búsqueda pendientes;
  - `leyenda`: estados, A1–A7 y B1–B7 transcritos de `Etapa 1 - FP-190.md`.
- **Validaciones:**
  - `Estado_cribado` admite solo los estados controlados; todos los registros comienzan en `Pendiente`;
  - A1–A7 admiten `C`, `CP`, `PE` o `NC`;
  - B1–B7 admiten enteros de 0 a 3;
  - `Puntaje_B` suma solo cuando los siete criterios B están completos.
- **Reproducibilidad:** script local `FEP TINV/scripts/build_fp76_matrix.py`.

## Exclusiones previas al cribado

Decisión de Danilo, 2026-09-18. Las filas quedan en la matriz con estado `Excluir` y ocultas; no se eliminan, para conservar la trazabilidad de los 348 registros.

| ID_FP76 | Motivo |
|---|---|
| FP76-330 | Idioma ucraniano: fuera del alcance de lectura del equipo |
| FP76-341 | Publicación retractada según WoS (`10.3233/JIFS-234951`): no admisible como evidencia (A5) |

Quedan 346 registros para el cribado A1–A7.

## Paso 4 — Cribado de títulos y resúmenes (propuesta IA, pendiente de validación humana)

Se aplicaron A1–A7 a los 346 registros con una rúbrica común derivada de `Etapa 1 - FP-190.md`
(Zona A líneas 357–388; solapamientos, definición de tendencia y filtros líneas 715–892).

**Regla de armonización.** La Zona A ya cubre "Optimización cloud" y "Herramientas y plataformas".
Por eso un algoritmo de scheduling, placement, asignación de recursos, autoscaling, offloading o caching
—normalmente evaluado en simulación— donde el costo monetario es un objetivo más junto a makespan,
energía, latencia o QoS, se excluye por A6. Pasa solo si el resumen muestra un mecanismo económico
distinto: mercado de precios (spot, reservas, compromisos), presupuesto o guardrail explícito, pronóstico
o estimación de costo previa al despliegue, asignación/showback, compensación costo–energía–emisiones con
costo monetario medido, economía unitaria, o evidencia de adopción real.

Esta regla se agregó después de que la primera pasada resultara inconsistente: un revisor excluyó 24 de 87
registros y otro 73 de 87 sobre el mismo tipo de paper. Los registros del primer revisor que no habían sido
excluidos se volvieron a evaluar con la regla ya aplicada.

### Resultado

| Estado | Registros |
|---|---|
| Excluir | 277 (incluye las 2 exclusiones previas al cribado) |
| Incluir para texto completo | 44 |
| Consultar | 19 |
| Reserva | 8 |

Primer filtro que falla en las exclusiones: A6 en 147 registros, A1 en 108, A7 en 7, A2 en 7, A3 en 5 y A5 en 1.

### Tendencias candidatas propuestas

| Etiqueta | Registros para texto completo |
|---|---|
| T2 Inteligencia y análisis de precios cloud | 10 |
| Nueva: Compromisos/descuentos y spot | 9 |
| T3 Costos shift-left en IaC | 7 |
| Nueva: FinOps agéntico/automatizado | 5 |
| Nueva: Multi-cloud/broker por costo | 4 |
| Nueva: Costo-energía-emisiones (GreenOps) | 3 |
| Nueva: Asignación/showback de costos | 2 |
| T1 Guardrails presupuestarios | 2 |
| Nueva: Autoscaling cost-aware | 1 |
| Nueva: Economía unitaria GenAI/LLM | 1 |

Las tres tendencias vigentes de FP-190 sobreviven al cribado y aparecen cinco etiquetas nuevas que no
estaban en la lista de diez candidatos de la Etapa 2. Esto no cambia la selección: el Paso 9 la revisa y la
decisión es humana.

### Estado de las fuentes ya utilizadas

| ID_FP76 | Fuente | Resultado del cribado |
|---|---|---|
| FP76-019 | Cho (2026) | Incluir para texto completo — T1 |
| FP76-041 | Feitosa et al. (2024) | Incluir para texto completo — T3 |
| FP76-043 | Fragiadakis et al. (2024) | Incluir para texto completo — T2 |
| FP76-089 | Smendowski & Nawrocki (2024) | Incluir para texto completo — T2 |
| FP76-037 | Stupar & Huljenic (2023) | Consultar — T3, frontera con arquitectura/TCO |
| FP76-151 | Cheng et al. (2024), GeoScale | Excluir por A6: autoscaling con presupuesto como una restricción más |

FP76-151 se usa hoy en FP-189 solo como contexto temático por metadata, no como evidencia. El cribado
propone excluirlo como candidato de tendencia; ambas cosas son compatibles, pero conviene decidirlo
explícitamente en el Paso 8.

### Cómo quedó registrado

Cada fila lleva A1–A7, estado, motivo de exclusión con el primer filtro que falla, tendencia candidata,
cadena causal y tipo de evidencia. En `Notas_verificacion` quedó `Propuesta IA 2026-09-18` con el nivel de
confianza. Antes del checkpoint de 2026-09-20, ninguna de estas decisiones estaba validada; el checklist exige
validación humana del cribado (§8.1).

## Verificación de textos completos, primera ola (2026-09-20)

13 PDF inventariados y verificados contra su propio texto. Inventario: DOI del PDF coincide con la matriz
en los 13; 0 duplicados por hash; ningún archivo ajeno, incompleto ni retractado. Diez están en
`FEP TINV/FP-76/papers`. Los 13 PDF se conservan sin renombrar ni modificar.

| ID | Págs | DOI verificado en el PDF |
|---|---|---|
| FP76-002 | 37 | `10.7717/peerj-cs.3964` |
| FP76-019 | 48 | `10.3390/app16073302` |
| FP76-037 | 32 | `10.1186/s13677-023-00389-8` |
| FP76-041 | 14 | `10.1016/j.jss.2024.112112` |
| FP76-043 | 20 | `10.3390/app142411946` |
| FP76-080 | 18 | `10.1016/j.jocs.2024.102292` |
| FP76-100 | 12 | `10.1145/3676151.3719353` |
| FP76-117 | 14 | `10.1007/s11761-025-00475-6` |
| FP76-134 | 20 | `10.18267/j.aip.313` |
| FP76-195 | 22 | `10.3389/frai.2026.1750992` |
| FP76-230 | 7 | `10.1145/3555776.3577718` |
| FP76-289 | 27 | `10.1007/s11042-023-17549-2` |
| FP76-332 | 16 | `10.1016/j.future.2026.108760` |

El UT de WoS no es verificable dentro del PDF; se conserva el de la exportación.

### Hallazgo principal: FP76-043 no demuestra pronóstico de precios

El texto completo de Fragiadakis et al. (2024) contiene un análisis hedónico transversal de factores de
precio (Caso 1, pp. 15–16) y un clustering K-Means para comparar costos (Caso 2, pp. 16–17). La
"predicción de precios" figura como capacidad del framework, pero **no se demuestra empíricamente**, y el
propio trabajo futuro (p. 19) pide incorporar aprendizaje automático predictivo. FP76-043 es una de las
tres fuentes vigentes y sostiene T2, cuya etiqueta actual es "Inteligencia y análisis de precios cloud".

Consecuencia pendiente de decisión humana: o la tendencia se apoya en otra fuente que sí demuestre
pronóstico (FP76-117 pronostica precios spot de AWS, aunque sin cifra económica y con autocorrelación
severa en los residuos, p. 12), o la etiqueta se acota a "inteligencia y análisis de políticas de precios".

### Cambios de puntaje propuestos (ninguno aplicado)

| ID | B actual | Total | B propuesto | Total | Motivo verificado |
|---|---|---|---|---|---|
| FP76-019 | 3,2,3,3,2,2,2 | 17 | B2→3 | 18 | Valida con traza real Google ClusterData 2011, no solo simulación |
| FP76-037 | 2,2,2,3,2,2,1 | 14 | B1→3 | 15 | Reducción 92,93%–95,39% y tabla de precios USD, p. 26 |
| FP76-041 | 1,3,3,3,3,3,3 | 19 | B1→2 | 20 | Solo una magnitud anecdótica (80% en un commit citado, p. 6) |
| FP76-043 | 2,3,2,3,1,2,2 | 15 | B1→3, B5→2 | 17 | USD 0,25–1,75/hora por categoría (p. 17); sección de limitaciones (p. 19) |
| FP76-100 | 2,3,3,3,3,3,3 | 20 | B1→3 | **21** | Descuentos 27–55% (Tabla 2, p. 4); 1,1% de ahorro y 4,3% de capacidad ociosa (pp. 7–8) |
| FP76-195 | 3,3,1,2,3,3,2 | 17 | B1→2 | 16 | El 85% proviene de una cita externa, no de sus 18 estudios |
| FP76-230 | 2,2,1,3,1,1,2 | 12 | B1→3, B2→3 | 14 | USD 6,12 y 11,56 mensuales con precios reales de facturación (pp. 5–6) |
| FP76-289 | 3,2,1,3,1,1,2 | 13 | B1→2 | 12 | El 94% del resumen no es trazable en el cuerpo (§5.1–5.4, pp. 18–23) |

Sin cambios: FP76-002, FP76-080, FP76-117, FP76-134, FP76-332.

### Cifras verificadas con página

- FP76-019: BD es más de 100× más rápido que NSGA-II con N=10.000 (10²–10³ ms contra 10⁵ ms), p. 32 y p. 45. Confirma el registro previo de FP-189.
- FP76-037: reducción de costo de 92,93%–95,39% frente a la peor configuración simulada, p. 26.
- FP76-041: 70% de commits en una categoría y un ejemplo anecdótico de 80%, p. 6.
- FP76-043: USD 0,25/hora (xsmall) contra USD 1,75/hora (large), p. 17.
- FP76-080: ganancia relativa de 0% a 93,897% por tipo de VM con precios reales de GCP del 5-11-2023, pp. 14–16.
- FP76-100: descuentos de 27–37% a un año y 50–55% a tres años, p. 4; ahorro propio de 1,1%, p. 7; 4,3% de capacidad comprometida sin usar, p. 8.
- FP76-117: MAPE por modelo y producto, pp. 9–11; Durbin-Watson con autocorrelación severa, p. 12.
- FP76-134: R² de 0,639 entre costo y exactitud, p. 1; precios de lista EC2 us-east-1 de noviembre de 2025, p. 18.
- FP76-195: 85% de reducción citado en pp. 14 y 16–17; 30–40% de Goyal et al. 2021, p. 1.
- FP76-230: USD 6,12 y USD 11,56 mensuales, pp. 5–6, Tablas 3–6.
- FP76-289: 94% de cumplimiento y 29% de reducción de makespan solo en el resumen, p. 1.
- FP76-332: USD 11,64/hora contra USD 6,29/hora, p. 2; 31,9% y 31,2% de mejora de eficiencia de costo, pp. 1, 12 y 14.

### Sobreinterpretaciones prohibidas

1. FP76-195: no atribuir el 85% a la síntesis de sus 18 estudios; proviene de Pillai et al. (2024), externo al corpus.
2. FP76-289: no presentar el 94% como resultado uniforme; el cuerpo muestra violaciones de presupuesto en CyberShake y Montage con intervalos largos.
3. FP76-100: las cifras en dólares de las figuras 8 y 9 son ilustrativas sobre demanda normalizada, no gasto real de Snowflake.
4. FP76-041: el 80% es una cita anecdótica, no un ahorro promedio del conjunto.
5. FP76-037: el 92,93%–95,39% se mide contra el peor caso simulado, no contra un promedio de mercado, y proviene de CloudSim con 256 configuraciones sintéticas.
6. FP76-043: no afirmar que valida pronóstico temporal de precios.
7. FP76-117: no presentar los MAPE bajos como precisión real; los propios autores los atribuyen a autocorrelación.
8. FP76-134: el costo por hora es tarifa de lista EC2 sin descuentos, no precio pagado.
9. FP76-080: no extrapolar el 93,897% fuera de HPC y GCP.
10. FP76-332: no generalizar a multirregión, multiproveedor ni modelos MoE.
11. FP76-230: no presentar USD 6,12 y 11,56 mensuales como ahorro sustancial; son cerca de 2–3% del costo mensual de una aplicación demo.
12. FP76-002: el 19% es la proporción de estudios que reporta algún resultado económico, no una cifra de ahorro.

### Fechas editoriales dobles

FP76-332 (ShuntServe): recibido 15-04-2026, aceptado 07-08-2026, disponible en línea 17-08-2026 (Early
Access), con publicación final asignada al volumen 186 (2027). Ambas fechas quedan registradas.

### Estado recomendado

Los 13 se recomiendan como **mantener candidato**. Ninguno baja a Reserva ni se excluye. Los estados,
puntajes y etiquetas **no se modificaron**: esperan decisión humana.

## Paso 4 (cierre) y Paso 5 — Puntuación B1–B7 (2026-09-20)

Decisiones humanas aplicadas antes de puntuar: FP76-002 pasa a `Incluir`; FP76-007 se rescata de la
auditoría A6 (A6 pasa de NC a CP, mecanismo de mercado spot); FP76-091 queda excluido por A7 (dominio
HPC) aunque su mecanismo económico se reconoce; FP76-151 (GeoScale) queda excluido de la selección y se
conserva como contexto bibliográfico; FP76-304 y FP76-307 quedan excluidos. Estado: 51 `Incluir`,
10 `Reserva`, 287 `Excluir`.

Se aplicó la Capa B a los 51 candidatos con la escala aprobada 0–3, sin ponderación, máximo 21, y la
regla de selección `B1 >= 2 y B2 >= 2`. Las puntuaciones ordenan; no seleccionan.

### Resultado

- Seleccionables: 27 de 51.
- No seleccionables: 24, de los cuales 23 fallan **solo** por B1 y uno (FP76-284) por B2.
- Prioridad de lectura propuesta: alta 21, media 14, baja 16.

### Observación de criterio que requiere decisión humana

B1 se operacionalizó como "efecto económico explicable y medible", y en la práctica se puntuó 1 cuando el
resumen no reporta una magnitud monetaria o porcentual. Eso bloquea sistemáticamente a la evidencia
conductual y cualitativa, que es justamente la que mejor demuestra un patrón de cambio:

| ID | Puntaje | Qué aporta | Por qué falla B1 |
|---|---|---|---|
| FP76-041 Feitosa et al. (fuente vigente de T3) | 19 | Minería de 152.000 repositorios; demuestra conducta de conciencia de costos | No cuantifica el efecto monetario |
| FP76-100 Shaved Ice | 19 | Estudio real de tres años sobre compromisos | El resumen no da la cifra de ahorro |
| FP76-199 Catálogo de antipatrones IaC | 16 | Taxonomía práctica con antipatrones | Es cualitativo, sin medición monetaria |
| FP76-017 OPTIC | 15 | Única evidencia sólida de asignación/showback | Mide exactitud de SQL, no gasto |
| FP76-043 Fragiadakis (fuente vigente de T2) | 14 | Framework de decisión sobre políticas de precios | No reporta magnitud económica |

Con el criterio literal, T3 queda con una sola fuente seleccionable y la mejor evidencia de esa tendencia
queda fuera. Dos de las tres fuentes que FP-190 ya usa resultan no seleccionables.

Interpretación alternativa posible, sujeta a decisión humana: B1 mide si el efecto económico **puede**
explicarse y medirse, no si el resumen ya trae la cifra. Bajo esa lectura, la mayoría de estos casos
subirían a B1=2 y el texto completo confirmaría o refutaría la magnitud. La decisión debe registrarse
antes de congelar la lista, porque cambia qué papers se descargan.

### Cobertura por tendencia (puntaje máximo y seleccionables)

| Tendencia | Candidatos | Seleccionables | Máximo |
|---|---|---|---|
| Nueva: FinOps agéntico/automatizado | 5 | 4 | 20 |
| Nueva: Economía unitaria GenAI/LLM | 2 | 2 | 20 |
| T2 Inteligencia y análisis de precios cloud | 12 | 7 | 19 |
| Nueva: Compromisos/descuentos y spot | 10 | 5 | 19 |
| Nueva: Costo-energía-emisiones (GreenOps) | 4 | 3 | 19 |
| T3 Costos shift-left en IaC | 8 | 1 | 19 |
| Nueva: Multi-cloud/broker por costo | 5 | 3 | 18 |
| T1 Guardrails presupuestarios | 2 | 2 | 17 |
| Nueva: Asignación/showback de costos | 2 | 0 | 15 |
| Nueva: Autoscaling cost-aware | 1 | 0 | 15 |

Las puntuaciones, su justificación, la incertidumbre declarada y la prioridad quedaron en la matriz, en
las columnas B1–B7 y en `Notas_verificacion`. `Puntaje_B` se calcula por fórmula en las 51 filas.

## Checkpoint B1 — interpretación humana aprobada y recalibración (2026-09-20)

Danilo aprobó que B1 no exige una cifra en el resumen. B1=3 requiere efecto económico directo cuantificado y contextualizado con unidad/comparador; B1=2, efecto directo operacionalizable/medible cuya magnitud requiere texto completo; B1=1, variable indirecta, proxy, ambigua o insuficientemente definida; B1=0, sin efecto económico identificable. B2 conserva la fuerza de evidencia.

Se revisaron los 51 registros `Incluir para texto completo` con título, resumen, palabras clave y cadena causal. Antes de cada cambio se preservaron B1 y racional previos en `Notas_verificacion`. Cambiaron de B1=1 a B1=2: `FP76-001`, `FP76-007`, `FP76-015`, `FP76-017`, `FP76-037`, `FP76-043`, `FP76-046`, `FP76-100`, `FP76-116`, `FP76-117`, `FP76-130`, `FP76-191`, `FP76-192`, `FP76-204`, `FP76-230`, `FP76-255`, `FP76-259`, `FP76-281`, `FP76-284`, `FP76-329` y `FP76-344`. B2–B7 no cambiaron: no se observó error demostrable de ingreso.

`FP76-041`, `FP76-150` y `FP76-199` siguen en B1=1 porque describen conducta de conciencia de costos o catálogos cualitativos de patrones, no un gasto/ahorro directo observado. `FP76-284` queda no seleccionable por B2=1. Los puntajes se recalcularon con fórmula y valor cacheado; la regla `B1>=2 && B2>=2` cambia de 27 a 47 seleccionables y de 24 a 4 no seleccionables.

Cobertura provisional: T2 12/12; compromisos/descuentos y spot 10/10; T3 shift-left 4/8; FinOps agéntico 5/5; GreenOps 4/4; asignación/showback 2/2; multi-cloud/broker 5/5; guardrails 2/2; autoscaling 1/1; economía unitaria GenAI/LLM 2/2. Las justificaciones, incertidumbre y prioridad de lectura de cada cambio están en la matriz. La lista de 47 PDF es **provisional**: este checkpoint no la congela ni autoriza descarga; magnitud, unidad y comparador de B1=2 requieren texto completo.

## Auditoría de las exclusiones A6 (2026-09-20)

Universo: 147 registros donde A6 fue el primer filtro en fallar. Se revisó una muestra de 36 (24%)
**dirigida y ponderada por riesgo**, no estadísticamente representativa: las 21 de confianza media o
baja más 15 de confianza alta repartidas por tipo de solapamiento, año y tipo documental. Cubre 2023
(8), 2024 (12), 2025 (8) y 2026 (8); 24 artículos y 12 trabajos de actas. Por ese diseño no se
extrapola el resultado de 3/36 al universo; **111 filas A6 permanecen sin auditar**.

Dos auditores independientes evaluaron la muestra **a ciegas**, sin ver la decisión previa, respondiendo
una sola pregunta: ¿existe un mecanismo económico distinto, o es optimización técnica de Zona A?

### Resultado

| Señal de auditoría | Registros |
|---|---|
| Mantener exclusión | 33 |
| Bandera / propuesta de rescate | 3 |

Las tres banderas no necesariamente son desacuerdos del auditor con la clasificación previa: señalan
un mecanismo A6 que requería disposición humana. No se calcula ni extrapola una tasa de desacuerdo.
Las banderas no se concentran en un estrato: una venía de confianza baja, una de media y una de alta.

### Banderas / propuestas de rescate y disposición humana

| ID | Año | Título | Mecanismo económico identificado | Tendencia |
|---|---|---|---|---|
| FP76-007 | 2023 | Cost-optimized scheduling for Microservices in Kubernetes | Uso deliberado de instancias spot como mecanismo de mercado | Nueva: Compromisos/descuentos y spot |
| FP76-091 | 2026 | Evaluating Paramount Iterations as a Performance Proxy for HPC | Estimación de costo relativo entre configuraciones antes del despliegue | T3 Costos shift-left en IaC |
| FP76-151 | 2024 | GeoScale: Microservice Autoscaling With Cost Budget | Guardrail de presupuesto de largo plazo aplicado en tiempo de ejecución | T1 Guardrails presupuestarios |

Disposición aprobada por Danilo el 2026-09-20:

- `FP76-007`: pasa de `Excluir` a `Incluir para texto completo`; `A6=CP` y `PDF_requerido=Sí`.
- `FP76-091`: permanece `Excluir`; se registra el mecanismo A6 reconocido, pero falla A7 por dominio HPC.
- `FP76-151`: permanece `Excluir` y solo como contexto bibliográfico; se preserva la decisión humana previa y se registra el desafío planteado por la auditoría ciega.

Observaciones registradas por los auditores:

- FP76-091 tiene un mecanismo económico genuino, pero su dominio es HPC. La auditoría solo respondió la
  pregunta de A6; A7 (escala manejable) podría excluirlo igualmente.
- FP76-151 contradice la decisión humana del 2026-09-20, que lo mantiene excluido de la selección y lo
  conserva solo como contexto bibliográfico. **La decisión humana prevalece** mientras no se revise.
- Casos límite marcados sin rescatar: FP76-333 (facturación por percentil 95), FP76-059 (presupuesto como
  criterio de no violación), FP76-318 (dos modalidades de cobro), FP76-135 (despliegue real, 4% de TCO),
  FP76-163 y FP76-186 (presupuesto como parámetro interno del metaheurístico).

## Discrepancia detectada

`docs/fp-190/etapas-1-2-delimitacion-y-candidatos-borrador.md`, línea 36, exige mínimos en **B2 y B5**. El plan aprobado (`Etapa 1 - FP-190.md`, líneas 896–898 y 927) exige al menos 2 puntos en **B1 y B2**. Se corregirá en FP-190 durante el Paso 9, con registro del cambio.

## Checkpoint — disposición humana de `Consultar` (2026-09-20)

Danilo aprobó localmente la disposición de los 19 registros `Consultar`. La matriz conserva en
`Notas_verificacion` la propuesta IA de 2026-09-18 y agrega la aprobación humana fechada; no se modificaron
los 72 campos originales de WoS ni se eliminaron filas.

| Disposición aprobada | ID_FP76 |
|---|---|
| Incluir para texto completo | FP76-001, FP76-037, FP76-134, FP76-143, FP76-159 |
| Reserva | FP76-006, FP76-050, FP76-086, FP76-092, FP76-243 |
| Excluir | FP76-013, FP76-058, FP76-109, FP76-160, FP76-182, FP76-245, FP76-260, FP76-300, FP76-310 |

`FP76-151` (Cheng et al., GeoScale) queda **excluido de la selección** y retenido **solo como contexto bibliográfico**;
no es evidencia seleccionada.

### Conteo posterior

| Estado | Registros |
|---|---:|
| Incluir para texto completo | 49 |
| Reserva | 13 |
| Excluir | 286 |
| Consultar | 0 |
| Total | 348 |
| Duplicados | 0 |

## Checkpoint — disposición humana de `Reserva` (2026-09-20)

Danilo aprobó localmente la disposición de los 13 registros `Reserva`. La matriz conserva la propuesta IA de
2026-09-18 y las aprobaciones humanas anteriores en `Notas_verificacion`; no se modificaron los 72 campos
originales de WoS ni se eliminaron filas.

| Disposición aprobada | ID_FP76 |
|---|---|
| Incluir para texto completo (`PDF_requerido=Sí`) | FP76-002 |
| Excluir | FP76-304, FP76-307 |
| Reserva | FP76-006, FP76-036, FP76-050, FP76-051, FP76-060, FP76-086, FP76-092, FP76-243, FP76-290, FP76-316 |

### Conteo posterior

| Estado | Registros |
|---|---:|
| Incluir para texto completo | 50 |
| Reserva | 10 |
| Excluir | 288 |
| Consultar | 0 |
| Total | 348 |
| Duplicados | 0 |

## Política temporal aprobada (2026-09-20)

Danilo aprobó que un registro WoS con fecha de *Early Access* en 2026 satisface la ventana primaria de
evidencia 2023–2026 aunque su publicación final pertenezca a 2027. Esta política no amplía la ventana de
búsqueda: conserva 2023–2026 como ventana primaria y registra por separado ambos campos originales de WoS.

| ID_FP76 | Publicación final WoS | Early Access WoS | Disposición y fundamento |
|---|---|---|---|
| FP76-240 | 2027 | No disponible | Permanece `Excluir`; no satisface la ventana primaria y además falla A6. |
| FP76-275 | JAN 2027 | AUG 2026 | La recencia sí satisface la ventana por *Early Access* 2026; permanece `Excluir` exclusivamente por solapamiento A6. |
| FP76-332 | JAN 2027 | AUG 2026 | Califica por *Early Access* 2026 y permanece `Incluir para texto completo`. |

La matriz conserva las decisiones e historial previos en `Notas_verificacion`; no se modificaron los campos
WoS originales. Conteo actual: **51** `Incluir para texto completo`, **10** `Reserva`, **287** `Excluir`, **0**
`Consultar`; **348** registros en total y **0** duplicados.

## Pendiente

## Checkpoint — primera ola de textos completos congelada (2026-09-20)

Danilo aprobó localmente la primera ola de 30 textos completos, registrada en
`FEP TINV/FP-76/control/FP-76 - lista prioritaria de textos completos.md`. La matriz conserva las 348 filas, los 72
campos WoS, fórmulas, validaciones, filtros, estados de cribado y B1–B7. Solo se ajustó
`PDF_requerido`: `Sí` para `FP76-001`, `002`, `007`, `015`, `017`, `019`, `028`, `037`, `041`, `043`,
`057`, `070`, `080`, `100`, `116`, `117`, `130`, `134`, `191`, `192`, `195`, `230`, `255`, `259`, `281`,
`289`, `329`, `332`, `342` y `344`; `No` para los otros 21 registros con estado `Incluir para texto completo`.
Las notas preservan el historial y agregan la aprobación humana fechada.

Disponibilidad observada sin descargar: solo Cho (`FP76-019`), Feitosa (`FP76-041`) y Fragiadakis
(`FP76-043`) ya tienen PDF local; los otros 27 quedan pendientes de descarga. `FP76-041` permanece como
ancla/contexto de texto completo pese a B1=1 y no es seleccionable todavía. `FP76-259` mantiene su
etiqueta T2 actual, con relabel humano pendiente hacia un mecanismo de dinámicas de costo serverless.

**Siguiente paso:** recuperar y verificar los 30 textos completos —identidad, método, muestra, páginas,
magnitud, unidad, denominador, comparador y límites— antes de usar evidencia final o modificar la
selección humana de tendencias.

## Checkpoint — disponibilidad de textos completos decidida por Danilo (2026-09-20)

Danilo decidió que la verificación de texto completo se limita a los **13** PDF disponibles localmente:
`FP76-002`, `019`, `037`, `041`, `043`, `080`, `100`, `117`, `134`, `195`, `230`, `289` y `332`.

Los otros **17** IDs de la primera ola —`FP76-001`, `007`, `015`, `017`, `028`, `057`, `070`, `116`,
`130`, `191`, `192`, `255`, `259`, `281`, `329`, `342` y `344`— quedan con `Texto completo no disponible`.
No se planifica recuperación adicional para ellos y no pueden respaldar afirmaciones primarias. En
particular, `FP76-259` no se usa por indisponibilidad de texto completo; esta decisión no se fundamenta
en que sea un libro.

**Siguiente paso:** verificar identidad, método, muestra, páginas, magnitud, unidad, denominador,
comparador y límites únicamente en los 13 textos completos disponibles antes de usar evidencia final.

## Checkpoint — decisiones humanas finales tras 13 textos completos (2026-09-20)

Danilo aprobó localmente las cuatro decisiones siguientes; los valores/racionales previos se preservan en `Notas_verificacion`.

1. T2 se renombra exactamente **`T2 Inteligencia y análisis de precios cloud`**. El pronóstico queda como sublínea limitada, no como etiqueta paraguas.
2. Política B1 final: B1 evalúa si el efecto económico es **directo y medible**; no exige una cifra en título/resumen, que puede confirmarse en texto completo. Cambios selectivos: `FP76-100` B1 2→3, total 21; `FP76-019` B2 2→3, total 18; `FP76-037` B1 2→3, total 15; `FP76-230` B1 2→3 y B2 2→3, total 14; `FP76-195` B1 3→2, total 16; `FP76-289` B1 3→2, total 12; `FP76-043` B5 1→2 (B1 permanece 2), total 16. `FP76-041` conserva B1=1 y total 19.
3. `FP76-289` pasa de `Incluir para texto completo` a `Reserva`. Su PDF sigue verificado y `PDF_requerido=Sí`; el titular 94% no es trazable en el cuerpo, que reporta violaciones presupuestarias. Se conserva como advertencia/contexto y no se excluye.
4. Conteo vigente: **50** `Incluir para texto completo`, **11** `Reserva`, **287** `Excluir`, **0** `Consultar`; **348** total. Entre los 13 PDF disponibles hay **12 candidatos** y **1 Reserva** (`FP76-289`). Los 17 no disponibles no cambian.

Estas decisiones actualizan solo la matriz y los artefactos locales de planificación; no actualizan entregables finales FP-190, FP-189, FP-191 ni FP-192.

Con este checkpoint quedó completada la verificación de los **13** textos disponibles: **12** continuaron como candidatos y `FP76-289` quedó en Reserva/contexto. En ese momento, el siguiente paso era comparar las tendencias con la evidencia verificada; la selección final resultante se registra a continuación.

## Selección final humana de tendencias (2026-09-20)

Danilo aprobó localmente y sin nueva recuperación exactamente cuatro tendencias: (1) **Compromisos, descuentos y capacidad spot**, mecanismo descuento por compromiso versus ociosidad, `FP76-100`, confianza alta; la fuente única exige separar el 1,1 % contrafactual sobre traza real de los descuentos nominales de 27–55 %. (2) **T2 Inteligencia y análisis de precios cloud**, asimetrías de tipo/región/modalidad, `FP76-080` y `FP76-002`, confianza media-alta. Forecasting queda sublínea limitada: `FP76-117` tiene autocorrelación y `FP76-043` no demuestra forecast. (3) **T3 Conciencia de costos *shift-left* en IaC**, decisión temprana de configuración/diseño, `FP76-041` conductual y `FP76-037` de magnitud simulada, confianza media; no hay ahorro productivo medido y `FP76-041` mantiene B1=1. (4) **Economía unitaria de GenAI/LLM**, costo por token/solicitud/inferencia/valor, `FP76-134` y `FP76-332`, confianza media-alta; conservar precios de lista y límite AWS `us-west-2`.

Selección multi-cloud/proveedor es sublínea; T1 guardrails y FinOps agéntico son contexto; `FP76-289` continúa Reserva/contexto. El alcance permanece en 13 textos verificados (12 candidatos y una Reserva) y 17 no disponibles, sin nueva recuperación. Los estados/puntajes no cambian: 50 Incluir, 11 Reserva, 287 Excluir y 0 Consultar (348 total).

## Validación humana de Versión 3 (2026-09-20)

Danilo validó humanamente la Versión 3, incluida la prosa final de análisis, discusión, aporte, conclusiones y recomendaciones, además de la autoría y justificación del cuestionario. La validación queda registrada solo de forma local y no implica aprobación de equipo ni docente. Siguen pendientes FP-180, confirmaciones FP-53/FP-54/FP-56, entrega Drive/Jira, QA final, transiciones de estado y autorización de commit/push.
