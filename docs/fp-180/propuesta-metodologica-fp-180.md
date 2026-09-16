# FP-180 — Propuesta metodológica para confirmación del equipo

> **Estado:** Propuesta. Las tres decisiones de esta página **no están confirmadas por consenso del
> equipo**; se aplicaron a la matriz para poder cuantificar su efecto y quedan sujetas a revisión.
> Documento estructurado con asistencia de IA.

## Por qué existe este documento

Cada artefacto de FP-177 cierra declarando qué fue **confirmado por consenso del equipo**: los
criterios, la escala, los pesos y los conjuntos críticos. Esa declaración es trazabilidad de quién
decidió qué, y la jerarquía de evidencia de FP-177 §2.1 define qué fuentes son admisibles.

La auditoría de la matriz de FP-180 encontró dos defectos de fondo cuya corrección exigió resolver
situaciones que FP-177 **no cubre explícitamente**. Resolverlas es inevitable —sin una regla, la
matriz no se puede calcular—, pero la regla elegida no puede quedar respaldada por el criterio de
quien ejecutó la corrección. Este documento expone cada decisión con su fundamento y su efecto
numérico, para que el equipo la confirme, la modifique o la rechace por escrito.

Los defectos corregidos están descritos en `estado-matriz-comparativa.md` §7 y §8; el detalle celda
por celda, en `correcciones-aplicadas.md` y `celdas-heredadas.md`.

---

## Decisión 1 — Productos separados, no suites por proveedor

### El vacío

FP-177 §2.2 define `0` como ausencia verificada y `NA` como no aplicable, pero no resuelve el caso de
un producto que verificadamente no cumple una función **porque otro producto del mismo proveedor la
cumple**. La matriz de indicadores agrega una columna de «prevención de doble conteo», que puede
leerse como respaldo para excluir esas funciones del producto angosto.

La primera pasada aplicó esa lectura: marcó `NA` los indicadores de Visibilidad, Asignación, Precio y
Dependencia de AWS Cost Optimization Hub y de Google Cloud FinOps Hub, con la justificación «esa
función corresponde a Cost Explorer / Cloud Billing».

### Lo decidido

Los productos se evalúan **por separado**, como los lista la población. Una función que el producto
verificadamente no cumple se puntúa `0`, aunque exista en otro producto del mismo proveedor.

### Fundamento

`docs/fp-177/escenarios-uso-y-poblacion-evaluada-borrador.md` §2 establece que «la agrupación se
conserva **exactamente** según la decisión de alcance de FP-51» y enumera los cinco productos cloud
nativos como entradas individuales. La ficha de FP-51 los nombra igual, y FP-177 §1 fija la unidad de
resultado en producto × escenario.

FP-177 no discute el caso de la suite: no lo rechazó, no lo consideró. La decisión no se apoya en una
prohibición, sino en no apartarse del alcance acordado.

La prevención de doble conteo de la matriz opera **entre indicadores** de una misma evaluación («una
integración no prueba adopción»), no entre productos distintos de la población.

### Efecto verificado

Mismo producto, misma evidencia, solo cambiando `NA` por `0`: AWS Cost Optimization Hub pasa de
**66,67 (Solid)** a **19,05 (Basic)**. Con `NA`, el peso de Visibilidad y Asignación —22% del total—
se repartía entre los criterios donde el producto sí puntúa, y quedaba por encima de AWS Cost
Explorer (51,85), que sí cubre ambos.

Comparación en E1 bajo cada opción:

| Productos separados (decidido) | S | Suites por proveedor (descartada) | S |
|---|---:|---|---:|
| AWS Cost Explorer | 51,85 | AWS (suite) | 55,56 |
| Azure Cost Management | 51,85 | Azure Cost Management | 51,85 |
| Google Cloud Billing | 38,89 ⚠ | Google Cloud (suite) | 48,15 ⚠ |
| Google Cloud FinOps Hub | 23,81 ⚠ | | |
| AWS Cost Optimization Hub | 19,05 ⚠ | | |

⚠ incumple un criterio crítico de E1.

### Limitación que obliga a declarar

Con productos separados, E1 muestra tres incumplimientos críticos de cinco productos, y **dos de
ellos no son un juicio sobre el proveedor**: AWS Cost Optimization Hub y Google Cloud FinOps Hub son
componentes de optimización evaluados en un escenario de visibilidad y asignación. FP-181 debe
declararlo explícitamente para que el informe no induzca la lectura de que AWS o Google ofrecen un
producto deficiente.

---

## Decisión 2 — Escenario ancla por categoría

### El vacío

La evidencia de la matriz se recogió **describiendo el producto en general, no un escenario**: por eso
fue replicable a todos sus escenarios. Se verificó que cada producto tiene exactamente el mismo
número de celdas puntuadas en todos sus escenarios (AWS Cost Explorer: 18 en E1, E2, E3, E5 y E6), de
modo que **no es posible inferir desde el libro en qué escenario se investigó cada valor**.

Como FP-177 §1 exige evidencia propia de las entradas de cada escenario, hubo que decidir en cuál de
ellos esa evidencia general se considera válida.

### Lo decidido

Cada producto conserva sus valores en el escenario donde FP-177 §4 sitúa a su categoría como actor
principal, y pasa a `NE` en los demás:

| Categoría | Escenario ancla |
|---|---|
| Herramientas cloud nativas | E1 |
| Plataformas multicloud | E2 |
| Herramientas de Kubernetes | E3 |
| Estimación temprana / políticas | E4 |

### Fundamento

Es una **convención declarada, no un hallazgo**. No se descubrió dónde se investigó cada valor: se
eligió dónde considerarlo válido, y se eligió el escenario en que cada categoría es el actor
principal del diseño de escenarios de FP-177 §4.

Se probó una alternativa —anclar por producto, en el escenario con más celdas puntuadas— y no
discrimina: al ser réplicas exactas, todos los escenarios de un producto empatan. La prueba es
circular y no aporta criterio.

### Efecto verificado

No cambia cuántos pares puntúan (9 en cualquier variante), sino **en qué escenario aparece el único
puntaje de cada producto**. Con esta convención, nOps puntúa en E2; si el ancla de multicloud fuera
E1, nOps puntuaría en E1 y E2 quedaría sin ningún par evaluable.

### Qué necesita el equipo verificar

Si quien ejecutó la investigación recuerda haber tenido un escenario concreto en mente para alguna
categoría, ese escenario debe reemplazar al ancla propuesta para esa categoría.

---

## Decisión 3 — Nueve indicadores dependientes del escenario

### El vacío

FP-177 no clasifica sus indicadores en dependientes e independientes del escenario. Para marcar los
valores heredados hubo que establecer esa clasificación.

### Lo decidido

Se consideran dependientes del escenario nueve indicadores: **V1, A1, A2, O1, AU1, I1, I2, AD1 y
P2**. Los otros nueve —V2, O2, AU2, M1, M2, AD2, P1, D1, D2— describen propiedades del producto y
conservan su valor en todos los escenarios.

### Fundamento

Cuatro se clasifican por el **texto literal** de su pregunta observable en la matriz de FP-177:

| Indicador | Texto que nombra el escenario |
|---|---|
| O1 | detecta desperdicio «relevante al escenario» |
| I1 | integra «los datos requeridos … del escenario» |
| I2 | se integra con «el flujo de trabajo relevante» |
| AD1 | soporta acceso «para los roles del escenario» |

Los otros cinco se clasifican **por criterio**, no por texto literal:

| Indicador | Razón |
|---|---|
| V1 | La unidad de desglose cambia: cuenta/proyecto en E1, namespace en E3, entidad en E5 |
| A1 | La entidad de asignación es la del escenario |
| A2 | Las reglas de reparto compartido son centrales en E5 y marginales en E1 |
| AU1 | Las acciones de costo controladas son las del escenario |
| P2 | La estimación o comparación es contextual al escenario |

### Efecto verificado

**Ninguno sobre los resultados.** Se probaron tres variantes y las tres dan 9 pares calculables de 60:

| Indicadores dependientes | Pares calculables | Celdas a investigar |
|---|---:|---:|
| Solo los 4 literales | 9 | 157 |
| Los 9 (decidido) | 9 | 338 |
| Los 18 | 9 | 599 |

La razón es que basta un indicador en `NE` para que su criterio completo deje de estar evidenciado:
con los 4 literales ya caen Optimización, Integración y Adopción, y la cobertura baja del 70% igual.

La decisión no afecta ningún puntaje del informe; afecta **el tamaño declarado del trabajo
pendiente**. Se eligieron los nueve porque, cuando se investiguen E5 y E6, V1 y A1 sí variarán por
escenario, y conservarlos replicados reintroduciría el defecto corregido.

---

## Punto abierto que FP-181 debe resolver

FP-177 §5 obliga a informar el incumplimiento de un criterio crítico junto al puntaje, pero **no
define si descalifica al producto para ese escenario**. Se propone que un incumplimiento crítico
impida recomendar ese producto para ese escenario, cualquiera sea su puntaje; de lo contrario el
conjunto de criterios críticos no cumple ninguna función. Requiere confirmación del equipo.

---

## Registro de confirmación

| Decisión | Estado | Confirmada por | Fecha |
|---|---|---|---|
| 1 — Productos separados | Propuesta | | |
| 2 — Ancla por categoría | Propuesta | | |
| 3 — Nueve indicadores dependientes | Propuesta | | |
| Criterio crítico descalifica (FP-181) | Propuesta | | |
