# FP-181 — Análisis comparativo y recomendaciones por escenario

> **Estado:** Documento estructurado con asistencia de IA a partir de la matriz de FP-180.
> Queda pendiente el criterio de término que exige que **el razonamiento sea elaborado y revisado
> por el grupo**, y la ratificación de las cuatro decisiones metodológicas descritas en
> `docs/fp-180/propuesta-metodologica-fp-180.md`. Ninguna recomendación de este documento debe
> darse por definitiva antes de esas dos cosas.

Entregable para FP-54 (informe final TI-06) y FP-56 (presentación y defensa).

---

## 1. Cómo se debe leer este análisis

El puntaje `S` de la matriz **no es una nota de calidad del producto**. Es el grado en que la
documentación oficial de una herramienta responde nueve preguntas observables, bajo las entradas de
un escenario concreto y con una fecha de corte. Tres consecuencias prácticas:

**Un puntaje bajo puede significar dos cosas distintas.** Que el producto haga poco de lo que el
escenario pide, o que haga otra cosa. AWS Cost Optimization Hub obtiene 19,05 en E1 no porque sea
deficiente, sino porque es un componente de recomendaciones evaluado en un escenario de visibilidad
y asignación. Lo mismo vale para Google Cloud FinOps Hub.

**Comparar entre escenarios no tiene sentido.** Los 31 pares puntuados son producto × escenario. Un
57,14 en E3 y un 56,25 en E1 no son comparables entre sí.

**La ausencia de evidencia no es ausencia de capacidad.** Es la regla explícita de FP-177 §2.1, y en
esta matriz pesa: 54 de 85 pares no alcanzan el 70% de cobertura y quedan sin puntaje. Eso no dice
que esos productos sean peores.

---

## 2. Sensibilidad a las ponderaciones

FP-177 define que la sensibilidad es material si cambia el nivel descriptivo o el orden **entre
herramientas comparables dentro del mismo escenario y categoría**. Se evaluaron los nueve grupos
comparables que existen en la matriz. **Cuatro presentan sensibilidad material, y en los cuatro el
cambio es de orden, no de banda.**

| Grupo | Orden con pesos iguales | Orden con perfil de sensibilidad |
|---|---|---|
| E1 · Cloud nativa | **AWS Cost Explorer** > Azure Cost Management | **Azure Cost Management** > AWS Cost Explorer |
| E1 · Multicloud | Vantage > **nOps** > CloudZero | Vantage > **CloudZero** > nOps |
| E2 · Multicloud | Vantage > **nOps** > CloudZero | Vantage > **CloudZero** > nOps |
| E5 · Cloud nativa | **AWS Cost Explorer** > Azure Cost Management | **Azure Cost Management** > AWS Cost Explorer |

Ningún producto cambia de banda en ningún escenario: las bandas son estables.

### Qué significa

**El orden entre AWS Cost Explorer y Azure Cost Management no es robusto.** Empatan exactamente en
51,85 con pesos iguales, y el desempate depende del perfil elegido: el de sensibilidad da más peso a
Visibilidad, Asignación y Optimización, y Azure tiene ventaja en Optimización (1,5 contra 1,0).
**Afirmar que uno es superior al otro en E1 o E5 no está sustentado por esta evidencia.**

**El orden entre nOps y CloudZero tampoco lo es.** Se separan por menos de un punto y el perfil de
pesos los intercambia. Son perfiles distintos, no uno mejor: nOps tiene automatización y multinube
fuertes con Precio débil; CloudZero tiene visibilidad, asignación y precio fuertes pero **no ejecuta
acciones**.

**Lo que sí resiste ambos perfiles:** Vantage encabeza E1, E2, E5 y E6; Infracost encabeza E4;
CloudZero encabeza E3. Esos tres liderazgos son robustos a la ponderación.

Los cinco grupos restantes —E3 Kubernetes, E4, E5 Multicloud, E6 Cloud nativa— no presentan
sensibilidad material.

---

## 3. Interpretación por escenario

### E1 — Visibilidad y asignación en nube única

Nueve productos evaluados, el escenario con más evidencia y el único con cobertura del 100% en
varios productos.

**Lo que muestra la evidencia.** Las tres herramientas nativas cubren bien visibilidad (2,0) e
integración (2,0), pero se separan en asignación: AWS y Azure alcanzan 2,0 mientras **Google Cloud
Billing queda en 0,5 e incumple el criterio crítico de Asignación**. La causa está documentada por
el propio proveedor y es la diferencia más nítida del escenario: Google no ofrece una regla nativa
de reparto de costo compartido y recomienda resolverlo por proceso interno de la organización.

Las plataformas multinube puntúan más alto que las nativas, pero la comparación es engañosa si se
lee como «son mejores»: obtienen valor en Multicloud (2,0) que las nativas tienen en 0,0 por diseño,
y en E1 ese criterio no es crítico. Su ventaja real está en otra parte: **gestionan el gasto no
asignado de forma explícita**, que es una de las dos salidas que E1 espera.

**Compensación principal.** CloudZero obtiene 2,0 en ocho criterios y **0,0 en Automatización**: su
propia documentación declara que solo recomienda, no ejecuta. Es la compensación más marcada de la
matriz —máxima visibilidad y asignación a cambio de ninguna capacidad de acción— y no aparece en el
puntaje agregado.

**Riesgo.** Los dos componentes de optimización (AWS Cost Optimization Hub, Google Cloud FinOps Hub)
incumplen ambos criterios críticos. No es un defecto: es que no son herramientas de este escenario.

### E2 — Consolidación multinube y comparación de precios

Cuatro plataformas, todas con cobertura de 78% a 89%.

**Lo que muestra la evidencia.** Las cuatro consolidan varios proveedores y las cuatro tienen el
criterio Precio evaluado, de modo que la comparación es legítima. Vantage lidera en ambos perfiles
con 2,0 parejo en ocho criterios.

**Compensación principal.** Igual que en E1: CloudZero compite de igual a igual salvo en
Automatización, donde tiene 0,0. Para una organización que quiera consolidar y además actuar, esa
diferencia es decisiva y no se ve en la distancia de puntaje (58,33 contra 66,67).

**Riesgo del escenario.** Las herramientas nativas **no son alternativa aquí**: FP-177 las admite
solo «para la parte de su proveedor», y ninguna alcanza el umbral de cobertura en E2. Quien opere
multinube no puede resolverlo con las consolas nativas.

### E3 — Optimización y automatización en Kubernetes

El escenario más débil en evidencia: tres productos, y **dos de los tres incumplen criterios
críticos**.

**Lo que muestra la evidencia.** Kubecost es el único que cumple los dos críticos del escenario:
tiene Optimización 1,5 y Automatización 2,0, esta última con una salvaguarda explícita —sus APIs
solo reducen recursos, nunca los aumentan—. CloudZero lidera en puntaje (57,14) pero **incumple
Automatización con 0,0**, y OpenCost incumple los dos.

**Compensación principal.** Es el escenario donde el puntaje más engaña. CloudZero puntúa más alto
que Kubecost (57,14 contra 50,00) y sin embargo, para el propósito declarado de E3 —detectar y
operar recomendaciones—, Kubecost es el único de los tres que lo cumple. El incumplimiento crítico
debe leerse antes que el puntaje.

**Riesgo.** **Cuatro de las seis herramientas de la categoría Kubernetes no alcanzan cobertura
suficiente** —Cast AI, PerfectScale, StormForge y ScaleOps—, de modo que el escenario compara dos de
seis. Es la comparación más incompleta de la matriz, y conviene declararlo antes que cualquier
recomendación de E3.

### E4 — Estimación y política antes del despliegue

Cinco productos, el escenario más completo en proporción: todos los elegibles puntúan.

**Lo que muestra la evidencia.** Infracost lidera en ambos perfiles y es el único con Precio 2,0 e
integración documentada al flujo de revisión de cambios de infraestructura. Las tres calculadoras
nativas —IBM, AWS y Azure— quedan por debajo y se diferencian entre sí por integración: IBM es la
única con la estimación incorporada al paso de validación del proyecto, lo que explica su ventaja
sobre las otras dos.

**Compensación principal.** Las calculadoras son gratuitas y de uso inmediato, pero tienen
Optimización 0,0 y Automatización 0,0: estiman, no detectan desperdicio ni bloquean despliegues.
Infracost cuesta más en esfuerzo de integración y entrega control real sobre el cambio.

**Riesgo.** **Cloud Custodian incumple el criterio crítico de Precio** y arrastra la tensión de
clasificación ya señalada: su documentación lo describe como motor de políticas sobre recursos ya
desplegados, no como herramienta de estimación previa. Su presencia en E4 responde a la población
acordada, no a la evidencia.

### E5 — Atribución en servicio compartido o multi-tenant

Seis productos. El escenario donde la diferencia entre proveedores es más concreta.

**Lo que muestra la evidencia.** Las tres nativas alcanzan cobertura del 100%, pero se separan
exactamente en lo que el escenario evalúa. AWS documenta reglas de reparto con tres métodos
—proporcional, fijo y equitativo— y límites declarados; Azure documenta reglas equivalentes con
distribución pareja o proporcional; **Google Cloud Billing no tiene regla nativa** y su documentación
lo reconoce, recomendando resolverlo fuera de la herramienta.

Las tres plataformas multinube cubren el escenario con reglas propias y, además, hacen visible la
porción no atribuible, que es una de las salidas que E5 exige.

**Compensación principal.** Las nativas alcanzan cobertura del 100% y las multinube 89%, pero las
multinube ganan en la calidad del reparto: Vantage documenta literalmente el caso de bases de datos
multi-tenant y garantiza que cada costo se asigne una sola vez.

### E6 — Carga distribuida y científica de gran escala

Cuatro productos con puntaje, **dos de ellos sin banda**.

**Lo que muestra la evidencia.** Solo Vantage y AWS Cost Explorer tienen verificado el componente
que distingue a este escenario: el costo de red por flujo. Vantage documenta reportes de flujo con
costo estimado por ruta de tráfico y reasigna los cargos agregados al recurso que los originó; AWS
expone la transferencia de datos de forma granular en el CUR, distinguiendo tráfico entre regiones,
entre zonas y de CloudFront.

**Azure Cost Management y Google Cloud Billing conservan puntaje pero quedan sin banda**, porque sus
dos criterios críticos —Visibilidad e Integración— no fueron verificados con evidencia propia de
red. No significa que no puedan hacerlo: significa que no se verificó, y la metodología no permite
recomendar sobre lo no verificado.

---

## 4. Recomendaciones condicionadas

Cada recomendación depende de condiciones explícitas. Ninguna es una recomendación de compra.

**Si la organización opera en una sola nube y necesita visibilidad y asignación (E1):** la
herramienta nativa del proveedor cubre el escenario con la evidencia más completa de la matriz, sin
costo de licencia adicional. **Con una excepción condicionada:** si el proveedor es Google Cloud y
se requiere showback o chargeback por entidad, la evidencia muestra una limitación documentada en el
reparto de costo compartido, y conviene evaluar una plataforma multinube aunque se use una sola nube.

**Si se requiere gestionar explícitamente el gasto no asignado (E1, E5):** las plataformas
multinube tienen ventaja documentada. Vantage y CloudZero calculan y exponen la porción no
atribuible; CloudHealth separa costos directos de indirectos.

**Si la organización opera dos o más nubes (E2):** las consolas nativas no resuelven el escenario.
Entre las plataformas, Vantage lidera de forma robusta a la ponderación. **Condición:** si además se
necesita ejecución automática de acciones de costo, CloudZero queda descartado pese a su puntaje,
porque su documentación declara que solo recomienda.

**Si se necesita optimizar y automatizar en Kubernetes (E3):** Kubecost es la única de las tres
evaluadas que cumple los dos criterios críticos, y además es el único producto de toda la población
—junto con AWS Pricing Calculator— que documenta su camino de salida. **Condición:** si solo se
necesita visibilidad de costo de clúster sin automatización, OpenCost la cubre con licencia abierta.

**Si se necesita estimar costo antes del despliegue (E4):** Infracost si la estimación debe
integrarse al flujo de revisión de cambios y condicionar decisiones; una calculadora nativa si basta
una estimación puntual para presupuestar, en cuyo caso IBM tiene la integración más completa al
flujo de proyecto.

**Si se necesita atribuir costo en servicios compartidos (E5):** AWS y Azure resuelven el escenario
de forma nativa con reglas de reparto documentadas. Google Cloud requiere complemento externo.

**Si la carga es distribuida y el costo de red es relevante (E6):** solo Vantage y AWS Cost Explorer
tienen ese componente verificado. Para Azure y Google no hay base para recomendar ni para
descartar: falta evidencia.

---

## 5. Hallazgos transversales

**La industria FinOps no documenta cómo salir de ella.** De los 25 productos evaluados, **21 no
documentan sus dependencias propietarias ni un camino de salida**. Solo Kubecost y AWS Pricing
Calculator lo hacen, y ambos comparten el rasgo de ser autoalojado o de alcance acotado. Es el
hallazgo más incómodo del trabajo: el criterio de dependencia, que toda organización debería evaluar
antes de comprometerse con una plataforma de costos, es precisamente el que ningún proveedor
comercial explica. **Ninguna de las plataformas multinube líderes tiene ese criterio evidenciado.**

**Los tres grandes proveedores se diferencian de forma documentada en reparto de costo compartido.**
AWS y Azure ofrecen reglas nativas con métodos declarados; Google Cloud no, y lo reconoce en su
propia documentación. Es una diferencia verificable entre proveedores, no una impresión.

**Los proveedores dividen la función de la misma manera.** Los tres separan una herramienta amplia
de visibilidad y asignación de un componente angosto de recomendaciones. Esa simetría sugiere una
convención de mercado, y explica por qué evaluar los componentes por separado produce puntajes bajos
que no son juicios sobre el proveedor.

**Ningún indicador de ningún producto alcanzó el valor 3.** FP-177 exige doble evidencia para ese
nivel —documentación primaria más estudio independiente, demostración reproducible o verificación
práctica— y este trabajo dispuso solo de documentación oficial. El techo de 2 es una limitación del
método aplicado, no del mercado.

---

## 6. Limitaciones

1. **Las cuatro decisiones metodológicas están pendientes de ratificación del equipo.** Si alguna
   cambia, cambian los números de este análisis.
2. **54 de 85 pares no alcanzan el umbral de cobertura** y quedan sin puntaje. El motivo está
   registrado celda por celda, pero la comparación es parcial en E3 y en las alternativas
   adicionales.
3. **Toda la evidencia es documentación oficial publicada**, sin acceso práctico a las consolas ni a
   cuentas reales. Ningún indicador puede superar el valor 2.
4. **Cloudability quedó excluida** de la comparación: la documentación técnica de IBM Docs devolvió
   error 403 en todos los intentos, y con evidencia solo comercial ningún indicador supera 1.
5. **Sensibilidad material en cuatro de nueve grupos comparables**, detallada en §2. Los órdenes
   AWS/Azure y nOps/CloudZero no deben presentarse como ranking.
6. **Dos artefactos del proyecto declaran poblaciones distintas**: FP-126 registra tres herramientas
   nativas y FP-51 con FP-177 registran cinco.
7. **Los precios de adquisición no entran en el puntaje.** El criterio Precio de FP-177 mide la
   transparencia de los costos que la herramienta reporta, no cuánto cuesta la herramienta. Esa
   información existe y está en la matriz de precios de FP-126, y debe presentarse por separado en
   el informe.
8. **La evidencia tiene fecha de corte 2026-09-16.** Precios, funciones y documentación cambian.

---

## 7. Qué debe hacer el grupo antes de dar esto por cerrado

El criterio de término de FP-181 exige que el razonamiento sea **elaborado y revisado por el grupo**.
Este documento es un insumo estructurado para esa revisión, no su reemplazo. Concretamente, el
equipo debería pronunciarse sobre:

- Las cuatro decisiones metodológicas de FP-180, especialmente la que retira la banda cuando un
  criterio crítico quedó sin evidencia.
- Si las recomendaciones condicionadas de §4 reflejan el criterio del grupo o solo la lectura de la
  evidencia.
- Si E3 se presenta con tres productos o se completa antes la investigación de los tres pendientes.
- Cómo se presenta la matriz de precios de FP-126 junto a este análisis, dado que responden
  preguntas distintas.

---

## Anexo — Tabla de resultados para FP-54 y FP-56

Cifras tomadas directamente de la matriz de FP-180 al 2026-09-16. Los gráficos por escenario
están en la hoja «Graficos» del libro y se generan de estos mismos datos, de modo que
coinciden con esta tabla.

### E1 — criterios críticos: Visibilidad y Asignacion

| Producto | Categoría | S base | S sens. | Banda | Cobertura | Observación |
|---|---|---:|---:|---|---:|---|
| Vantage | Multicloud | 66.67 | 66.67 | Solid | 89% | — |
| nOps | Multicloud | 59.52 | 58.84 | Solid | 78% | — |
| CloudZero | Multicloud | 58.33 | 59.50 | Solid | 89% | — |
| CloudHealth | Multicloud | 56.25 | 56.63 | Solid | 89% | — |
| Azure Cost Management | Cloud nativa | 51.85 | 54.00 | Solid | 100% | — |
| AWS Cost Explorer | Cloud nativa | 51.85 | 53.17 | Solid | 100% | — |
| Google Cloud Billing | Cloud nativa | 38.89 | 37.67 | Basic | 100% | incumple Asignacion |
| Google Cloud FinOps Hub | Cloud nativa | 23.81 | 22.89 | Basic | 78% | incumple Visibilidad, Asignacion |
| AWS Cost Optimization Hub | Cloud nativa | 19.05 | 19.61 | Basic | 78% | incumple Visibilidad, Asignacion |

### E2 — criterios críticos: Multicloud y Precio

| Producto | Categoría | S base | S sens. | Banda | Cobertura | Observación |
|---|---|---:|---:|---|---:|---|
| Vantage | Multicloud | 66.67 | 66.67 | Solid | 89% | — |
| nOps | Multicloud | 59.52 | 58.84 | Solid | 78% | — |
| CloudZero | Multicloud | 58.33 | 59.50 | Solid | 89% | — |
| CloudHealth | Multicloud | 56.25 | 56.63 | Solid | 89% | — |

### E3 — criterios críticos: Optimizacion y Automatizacion

| Producto | Categoría | S base | S sens. | Banda | Cobertura | Observación |
|---|---|---:|---:|---|---:|---|
| CloudZero | Multicloud | 57.14 | 58.44 | Solid | 78% | incumple Automatizacion |
| Kubecost | Kubernetes | 50.00 | 50.62 | Solid | 78% | — |
| OpenCost | Kubernetes | 33.33 | 34.58 | Basic | 78% | incumple Optimizacion, Automatizacion |

### E4 — criterios críticos: Precio y Integracion

| Producto | Categoría | S base | S sens. | Banda | Cobertura | Observación |
|---|---|---:|---:|---|---:|---|
| Infracost | Estimacion temprana | 47.22 | 49.76 | Basic | 75% | — |
| IBM Cloud Cost Estimator | Cloud nativa | 38.89 | 42.38 | Basic | 75% | — |
| AWS Pricing Calculator | Estimacion temprana | 35.71 | 35.93 | Basic | 88% | — |
| Azure Pricing Calculator | Estimacion temprana | 30.56 | 32.86 | Basic | 75% | — |
| Cloud Custodian | Estimacion temprana | 19.05 | 16.67 | Basic | 78% | incumple Precio |

### E5 — criterios críticos: Asignacion y Visibilidad

| Producto | Categoría | S base | S sens. | Banda | Cobertura | Observación |
|---|---|---:|---:|---|---:|---|
| Vantage | Multicloud | 66.67 | 66.67 | Solid | 89% | — |
| CloudZero | Multicloud | 58.33 | 59.50 | Solid | 89% | — |
| CloudHealth | Multicloud | 56.25 | 56.63 | Solid | 89% | — |
| Azure Cost Management | Cloud nativa | 51.85 | 54.00 | Solid | 100% | — |
| AWS Cost Explorer | Cloud nativa | 51.85 | 53.17 | Solid | 100% | — |
| Google Cloud Billing | Cloud nativa | 40.74 | 40.17 | Basic | 100% | — |

### E6 — criterios críticos: Visibilidad y Integracion

| Producto | Categoría | S base | S sens. | Banda | Cobertura | Observación |
|---|---|---:|---:|---|---:|---|
| Vantage | Multicloud | 66.67 | 66.67 | Solid | 89% | — |
| AWS Cost Explorer | Cloud nativa | 51.85 | 53.17 | Solid | 100% | — |
| Azure Cost Management | Cloud nativa | 47.62 | 49.78 | — | 78% | **sin banda** — crítico sin evidencia: Visibilidad, Integracion |
| Google Cloud Billing | Cloud nativa | 30.95 | 28.00 | — | 78% | **sin banda** — crítico sin evidencia: Visibilidad, Integracion |

