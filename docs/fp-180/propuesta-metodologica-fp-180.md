# FP-180 — Decisiones metodológicas

> **Estado:** Las cuatro decisiones de esta página fueron **resueltas por el responsable de
> FP-51 el 2026-09-17** y están aplicadas a la matriz. Quedan a **ratificación del equipo**, que
> es el nivel de confirmación que FP-177 declara para sus propios artefactos.
> Documento estructurado con asistencia de IA.

## Por qué existe este documento

Cada artefacto de FP-177 cierra declarando qué fue **confirmado por consenso del equipo**. Esa
declaración es trazabilidad de quién decidió qué, y la jerarquía de evidencia de FP-177 §2.1 define
qué fuentes son admisibles.

La auditoría y el completado de la matriz de FP-180 obligaron a resolver cuatro situaciones que
FP-177 **no cubre explícitamente**. Resolverlas era inevitable: sin una regla, la matriz no se puede
calcular ni poblar. Pero la regla elegida no podía quedar respaldada por el criterio de quien
ejecutó el trabajo, y por eso se documentaron aquí con su fundamento y su efecto medido antes de
aplicarse.

Los defectos corregidos y las pasadas de investigación están descritos en
`estado-matriz-comparativa.md`; el detalle celda por celda, en los informes de cada pasada.

**Una decisión anterior fue retirada.** Durante la corrección se usó una convención llamada
«escenario ancla»: la evidencia de un producto valía solo en el escenario donde su categoría es
actor principal. Era un atajo para no rehacer la investigación por escenario. Al levantarse la
restricción de plazo, se abandonó y se hizo el trabajo que FP-177 §1 pide: evidencia propia por par
producto × escenario. Ya no forma parte de la metodología aplicada.

---

## Decisión 1 — Un criterio crítico sin evidencia deja al par sin banda

### El vacío

FP-177 §5 fija dos criterios críticos por escenario con exigencia `C_c ≥ 1` y dice que «un
incumplimiento crítico se informa junto al puntaje y no se oculta con la media». Eso regula un
criterio **medido y reprobado**. No dice nada sobre un criterio crítico que **nunca se midió**.

### Lo decidido

Un criterio crítico que aplica y quedó sin evidencia **retira la banda comparativa del par**. El
puntaje se conserva y se informa, pero el par no recibe banda ni entra en la recomendación de ese
escenario.

Un criterio crítico marcado `NA` **no cuenta** para esta regla: `NA` significa que el escenario no
se lo exige a ese producto —como hace FP-177 §4 con las nativas en E2, admitidas solo «para la
parte de su proveedor»— y eso es un alcance declarado, no un hueco de evidencia.

### Fundamento

Es la única salida coherente con el resto de la metodología. Revisados todos los mecanismos de
FP-177 que tratan la ausencia, el patrón es constante: **cuando no se puede verificar algo, se
retira la conclusión; nunca se inventa una penalización**.

| Situación | Qué hace FP-177 |
|---|---|
| Indicador sin evidencia | Sale del cálculo y reduce cobertura; **no se convierte en cero** |
| Criterio con un indicador en `NE` | Deja de estar evidenciado y pierde su peso en la cobertura |
| Cobertura bajo 70% | *Insufficient evidence* y **no recibe banda comparativa** |
| Indicador `NA` | Sale y renormaliza «para no atribuir valor a lo desconocido» |
| Evidencia solo comercial | Tope de 1: limita, no anula |
| Cobertura frente a banda | «La condición de cobertura prevalece sobre cualquier banda» |

La última fila es casi el mismo caso: ya existe un mecanismo donde una condición de verificación
anula la banda sin tocar el puntaje. Tratar el crítico sin evidencia como incumplimiento sería
convertir `NE` en `0`, que la metodología prohíbe; dejar la banda intacta sería atribuir valor a lo
desconocido, que la renormalización busca evitar.

### Efecto verificado

En E6, Azure Cost Management (47,62) y Google Cloud Billing (30,95) alcanzaban cobertura suficiente
**sin tener evaluados Visibilidad ni Integración, los dos criterios críticos de ese escenario**.
Ambos pasan a «Sin banda (crítico sin evidencia)», conservando su puntaje. E6 queda con dos
productos recomendables: Vantage y AWS Cost Explorer, que sí tienen verificado el componente de red.

---

## Decisión 2 — Productos separados, no suites por proveedor

### El vacío

FP-177 §2.2 define `0` como ausencia verificada y `NA` como no aplicable, pero no resuelve el caso
de un producto que verificadamente no cumple una función **porque otro producto del mismo proveedor
la cumple**. La matriz de indicadores incluye una columna de «prevención de doble conteo», que puede
leerse como respaldo para excluir esas funciones del producto angosto.

### Lo decidido

Los productos se evalúan **por separado**, como los lista la población. Una función que el producto
verificadamente no cumple se puntúa `0`, aunque exista en otro producto del mismo proveedor.

### Fundamento

`escenarios-uso-y-poblacion-evaluada-borrador.md` §2 establece que «la agrupación se conserva
**exactamente** según la decisión de alcance de FP-51» y enumera los cinco productos cloud nativos
como entradas individuales. La ficha de FP-51 los nombra igual, y FP-177 §1 fija la unidad de
resultado en producto × escenario.

FP-177 no discute el caso de la suite: no lo rechazó, no lo consideró. La decisión no se apoya en
una prohibición, sino en no apartarse del alcance acordado. La prevención de doble conteo opera
**entre indicadores** de una misma evaluación, no entre productos distintos de la población.

### Efecto verificado

AWS Cost Optimization Hub pasa de **66,67 (Solid)** a **19,05 (Basic)**. Con `NA`, el peso de
Visibilidad y Asignación —22% del total— se repartía entre los criterios donde el producto sí
puntúa, y quedaba por encima de AWS Cost Explorer (51,85), que sí cubre ambos.

### Inconsistencia que obliga a declarar

**FP-126 registra tres herramientas nativas, no cinco**: trata a AWS y a Google como un producto
cada uno. FP-51 y FP-177 las separan. Son dos artefactos del proyecto con poblaciones distintas, y
la diferencia debe quedar declarada en el informe aunque la decisión se sostenga en FP-51 y FP-177,
que son los que definen la población de la comparación.

### Limitación que obliga a declarar

Con productos separados, E1 muestra incumplimientos críticos en AWS Cost Optimization Hub y Google
Cloud FinOps Hub que **no son un juicio sobre el proveedor**: son componentes de optimización
evaluados en un escenario de visibilidad y asignación. FP-181 debe decirlo explícitamente.

---

## Decisión 3 — La evidencia de un escenario puede subsumir a otro, declarándolo

### El vacío

Al abandonar el escenario ancla había que decidir si la evidencia recogida para un escenario sostiene
el valor de un indicador en otro. FP-177 exige entradas propias del escenario, pero no dice qué
ocurre cuando una capacidad documentada para un contexto **incluye lógicamente** al otro.

### Lo decidido

Una capacidad documentada para un escenario más exigente sostiene el valor en uno menos exigente,
**siempre que el argumento de inclusión se registre en la celda**. No es copiar un valor: es
declarar por qué la evidencia citada alcanza.

El caso típico: una plataforma que consolida y desglosa costo entre varios proveedores (E2)
necesariamente lo hace para uno solo (E1). Donde la capacidad no subsume, la celda no se toca. Por
eso la evidencia de E2 **no** se trasladó a E3: consolidar proveedores no dice nada sobre leer un
clúster, y por eso CloudZero se evaluó en E3 contra su documentación de Kubernetes.

### Fundamento

Es el método que reemplazó al atajo del ancla, y se apoya en que la unidad de FP-177 es producto ×
escenario: lo que se evalúa es la capacidad del producto frente a las entradas del escenario, y una
capacidad mayor cubre una menor del mismo tipo. La diferencia con el ancla es que aquí hay un
argumento explícito y auditable por celda, no una convención general.

### Alcance

Sostiene la mayor parte de los pares poblados. Si se rechaza, esas celdas vuelven a `NE`.

---

## Decisión 4 — Cada escenario tiene indicadores que no admiten subsunción

### El vacío

Corolario de la anterior: si la evidencia puede subsumir, hay que definir qué **nunca** puede
hacerlo, para que ningún escenario quede satisfecho por capacidades verificadas para otro.

### Lo decidido

En cada escenario, los indicadores que expresan lo que ese escenario evalúa se puntúan **solo con
evidencia propia**:

| Escenario | Exige evidencia propia | Por qué |
|---|---|---|
| E1 | A1 | Sus salidas incluyen el gasto no asignado y el showback, que ningún otro escenario pide |
| E2 | P1 y P2 | Precio es criterio crítico y estaba sin evaluar en tres de cuatro plataformas |
| E5 | A2 | La regla de reparto del costo compartido es lo que define la atribución multi-tenant |
| E6 | V1 e I1 | El costo de red por flujo distingue al escenario y son sus dos críticos |

En E6 se aplicó la forma más estricta: sin evidencia propia sobre costo de red, esos indicadores
quedan en `NE` aunque el producto tenga desglose documentado en otro lado. Es lo que dejó a Azure y
a Google Cloud Billing sin sus críticos evaluados, y lo que la decisión 1 convierte en «sin banda».

### Fundamento

Sin esta restricción, la subsunción de la decisión 3 vaciaría de sentido a los escenarios: cualquier
producto con capacidades generales documentadas quedaría evaluado en todos. La combinación de ambas
decisiones preserva la unidad producto × escenario: lo común se subsume con argumento, lo propio se
investiga.

---

## Aplicación de la condición de elegibilidad de E4

La condición de elegibilidad de E4 —nativas «cuando soporten estimación previa»— habilitaba un caso
que la matriz no cubría: **IBM Cloud Cost Estimator cumple esa condición y no estaba evaluado en
E4**. Toda su evidencia describe estimación previa al despliegue, es decir corresponde a E4 y no a
E1, donde figuraba únicamente por pertenecer a la categoría nativa.

Se aplicó el 2026-09-17. El producto **no se reclasifica**: sigue siendo cloud nativa y ahora
también se evalúa donde FP-177 lo admite. Sus indicadores sin objeto antes del despliegue pasan a
`NA`, con el mismo criterio ya aplicado a Infracost y a las calculadoras de AWS y Azure.

Eso resuelve la tensión registrada en `alternativas-adicionales.md` sin tocar la población acordada:
el producto no estaba mal categorizado, estaba evaluado en el escenario equivocado. Entra con
**38,89 (Basic)** y cobertura 75%, cumpliendo los dos criterios críticos de E4, y deja el escenario
con las tres calculadoras nativas de estimación previa —AWS, Azure e IBM— comparables entre sí.

La decisión no requirió criterio nuevo: se deriva del texto de FP-177 §4.

---

## Registro de decisiones

| Decisión | Estado | Resuelta por | Fecha |
|---|---|---|---|
| 1 — Crítico sin evidencia retira la banda | Aplicada | Responsable de FP-51 | 2026-09-17 |
| 2 — Productos separados | Aplicada | Responsable de FP-51 | 2026-09-17 |
| 3 — Subsunción declarada entre escenarios | Aplicada | Responsable de FP-51 | 2026-09-17 |
| 4 — Indicadores con evidencia propia por escenario | Aplicada | Responsable de FP-51 | 2026-09-17 |
| Escenario ancla | **Retirada**; reemplazada por las decisiones 3 y 4 | Responsable de FP-51 | 2026-09-17 |
| IBM Cloud Cost Estimator en E4 | Aplicada; derivada del texto de FP-177 §4 | Responsable de FP-51 | 2026-09-17 |

| Ratificación del equipo | Estado | Confirmada por | Fecha |
|---|---|---|---|
| Decisiones 1 a 4 | Pendiente | | |
