# Asignación de costos en FinOps

> **Borrador conceptual pendiente de revisión humana.**

La asignación de costos en FinOps relaciona el gasto cloud con los destinos que lo consumen o se benefician de él. Transforma datos de facturación y uso en información sobre propiedad, consumo y responsabilidad [1].

## Asignación de costos

La **asignación de costos** atribuye un costo a un destino, como un producto, servicio, equipo, unidad organizativa o centro de costo. Ese destino representa la propiedad económica del consumo y no necesariamente coincide con quien administra el recurso. La atribución puede apoyarse en cuentas, jerarquías, etiquetas, datos de consumo u otras evidencias [1].

Su finalidad es mostrar qué gasto corresponde a cada destino y bajo qué criterio. Esto permite que los responsables comprendan el consumo asociado a su ámbito y aporta trazabilidad: una cifra atribuida debe relacionarse con una fuente, un destino y una regla explícita.

La asignación favorece la rendición de cuentas al identificar responsabilidades sobre el consumo. Sin embargo, atribuir un costo no implica realizar un cargo contable; esa diferencia corresponde a los mecanismos de *showback* y *chargeback* [2].

## Etiquetado

El **etiquetado** incorpora metadatos a cuentas, recursos o registros de consumo. Ejemplos genéricos son `owner`, para el responsable; `product`, para el producto o servicio; `environment`, para el entorno; y `cost_center`, para el destino financiero. Son categorías mínimas de identificación, no una taxonomía adoptada.

Las etiquetas facilitan clasificar y agrupar costos, y pueden aportar evidencia para una asignación directa o delimitar un reparto [1]. Su utilidad depende de la cobertura y consistencia de sus valores.

Una etiqueta no equivale a una política de asignación. El metadato describe el recurso o consumo; la política establece qué costos se distribuyen, hacia qué destinos, mediante qué regla y durante qué periodo. En servicios compartidos, conocer el responsable o entorno no determina cómo repartir el costo.

## Costos compartidos

Los costos pueden ser **directos** o **compartidos** por su relación con los destinos; **no asignado** describe su estado de atribución, no una tercera naturaleza excluyente. El directo se atribuye a un destino sin reparto. El compartido beneficia a varios destinos y puede agruparse en un fondo para distribuirse. El no asignado aún no tiene una atribución válida, por falta de evidencia o de una regla implementada [1].

Los fondos compartidos reúnen costos de capacidades, plataformas o servicios comunes. Su distribución requiere un **conductor de asignación** que represente la participación de cada destino. Puede basarse en mediciones de uso o en un indicador sustituto con una relación causal comprensible respecto del costo.

Un costo no asignado no debe confundirse con uno compartido. En el compartido se conoce la naturaleza común del gasto; en el no asignado falta información o un mecanismo aplicado para atribuirlo. La práctica de *informed ignore* permite retener centralmente un costo compartido mediante una decisión consciente de no distribuirlo, sin clasificarlo como costo no identificado [1].

## Showback frente a chargeback

| Aspecto | Showback | Chargeback |
|---|---|---|
| Tratamiento | Presenta el costo asignado a cada destino. | Traslada o registra el costo asignado en presupuestos o sistemas financieros. |
| Efecto financiero | Informativo; no produce por sí mismo un cargo interno. | Produce un cargo formal sujeto a conciliación financiera. |
| Propósito | Dar visibilidad sobre consumo, propiedad y reglas de atribución. | Reflejar la atribución en la responsabilidad presupuestaria o contable. |
| Condición | Requiere datos y reglas comprensibles para los destinatarios. | Requiere además destinos financieros, cierres y mecanismos de corrección. |

Ambos mecanismos utilizan información de asignación, pero difieren en su efecto. El *showback* comunica los costos sin transferirlos contablemente; el *chargeback* los incorpora a un proceso financiero formal. Ninguno es inherentemente superior ni representa por sí solo un mayor nivel de madurez. La elección depende del propósito de la información y de la política financiera aplicable [2].

En este contexto, **chargeback significa imputación formal interna del gasto a un presupuesto o centro de costo**. No exige un pago externo adicional: el pago de la factura al proveedor y la distribución interna de esa responsabilidad son procesos distintos [2].

## Tasa de asignación

Para un fondo de costos compartidos de monto $S$, se define un conductor $q_i$ para cada destino $i$. Aquí, **tasa de asignación** significa **tasa unitaria de reparto**, no porcentaje de cobertura del gasto. Las siguientes expresiones son una formulación matemática del documento basada en el reparto proporcional descrito en [1], no una cita textual:

$$
r = \frac{S}{\sum_i q_i}
$$

El costo asignado a cada destino se obtiene mediante:

$$
A_i = r \times q_i
$$

La comprobación de conservación exige que la suma de las asignaciones reproduzca el fondo distribuido:

$$
\sum_i A_i = S
$$

Los conductores deben ser no negativos, estar medidos en la misma unidad y periodo, y cumplir $\sum_i q_i>0$. La tasa $r$ se expresa en moneda por unidad del conductor; el **peso de reparto** $w_i=q_i/\sum_j q_j$ es adimensional y permite escribir $A_i=S w_i$. Si el conductor es gasto, $r$ es una razón monetaria, no cobertura. Los redondeos deben conciliarse para conservar el fondo efectivamente distribuido; el costo retenido centralmente no forma parte de ese fondo.

La **cobertura de asignación** responde a otra pregunta: qué proporción del costo total tiene destino identificado conforme a la política y granularidad declaradas [1]. Su formulación en este documento es:

$$
\text{Cobertura} = \frac{C_{\text{asignado}}}{C_{\text{total}}}\times 100\%
$$

Ambos costos deben compartir alcance, periodo, moneda y base contable, con $C_{\text{total}}>0$. Aquí se incluye en $C_{\text{asignado}}$ el costo retenido en un destino central explícitamente identificado; no equivale a cobertura de reparto a productos. Si se mide esta última, el costo central permanece fuera del numerador y debe informarse por separado. Con créditos negativos, la razón neta puede dejar de comportarse como una proporción entre cero y cien; se documenta ese tratamiento sin ocultarlo mediante ajustes arbitrarios.

Entre los conductores candidatos se encuentran solicitudes, tiempo de CPU, capacidad de almacenamiento, usuarios activos o gasto directo. La selección del conductor depende de su capacidad para representar la causa o el grado de uso del servicio compartido, de su medición consistente y de su comprensión por quienes revisan la asignación. Un indicador disponible pero desvinculado del consumo puede producir una distribución formalmente calculable sin una atribución causal suficiente.

Tak et al. describen el uso total de un recurso compartido como la combinación del uso atribuible a las entidades y una porción no atribuible —ecuación (1), sección 3, p. 305—, lo que aporta evidencia técnica para separar componentes y comprobar la conservación [3]. Su método no define una política normativa de asignación FinOps: fue evaluado en un entorno Xen y presenta limitaciones relacionadas con memoria, caché, *buffering* e interferencias entre cargas [3].

## Referencias

[1] FinOps Foundation. *Allocation*. https://www.finops.org/framework/capabilities/allocation/. Fuente oficial consultada nuevamente el 2026-09-17. Registrada en la matriz FP-48 como fuente 002; la URL canónica vigente difiere de la consignada originalmente en esa fila.

[2] FinOps Foundation. *Invoicing & Chargeback*. https://www.finops.org/framework/capabilities/invoicing-chargeback/. Fuente oficial consultada nuevamente el 2026-09-17. La matriz FP-48 no le asigna una fila independiente; la fuente 002 registra los términos *showback* y *chargeback* dentro de Allocation.

[3] Tak, B. C., Kwon, Y. y Urgaonkar, B. (2017). “Resource Accounting of Shared IT Resources in Multi-Tenant Clouds”. *IEEE Transactions on Services Computing*, 10(2), 302-315. https://doi.org/10.1109/TSC.2015.2453980. Evidencia utilizada: ecuación (1), sección 3, p. 305, y secciones 5.2-5.3 sobre uso no atribuible y limitaciones. Registrada en la matriz FP-48 en la fila académica titulada con el nombre del artículo, sin ID numérico asignado.
