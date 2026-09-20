# Asignación de costos en FinOps

> **Estado:** Documento de información verificada. El alcance es conceptual y no contiene datos aplicados, resultados ni una política de asignación para una organización concreta. Las taxonomías, conductores y reglas operativas se presentan como formulaciones del proyecto, no como políticas universales.

La asignación de costos relaciona el gasto cloud con los destinos que lo consumen o se benefician de él. Dentro del framework de FinOps, pertenece al dominio *Understand Usage & Cost*, que reúne cuatro capacidades vigentes: *Data Ingestion*, *Allocation*, *Reporting & Analytics* y *Anomaly Management* [1]. Estas capacidades intercambian datos, metadatos, análisis y retroalimentación; el orden de exposición de este documento es pedagógico y no representa un proceso lineal obligatorio.

El alcance se limita a los conceptos necesarios para comprender la asignación, sus insumos, sus resultados informativos y su relación con la detección de anomalías. La imputación contable se distingue como un resultado posterior, y los denominadores, fórmulas y métricas de economía unitaria se reservan para FP-169.

## Conceptos básicos

| Concepto | Definición breve |
|---|---|
| Asignación | Atribución de un costo a un destino mediante evidencia y reglas explícitas. |
| Costo directo | Costo atribuible a un único destino sin necesidad de reparto. |
| Costo compartido | Costo que beneficia a varios destinos y requiere una decisión de distribución o retención central. |
| Costo no asignado | Costo que todavía no tiene un destino válido conforme a la política declarada. |
| *Showback* | Comunicación informativa del costo asignado, sin producir por sí misma un cargo interno. |
| *Chargeback* | Imputación formal del costo asignado a presupuestos o sistemas financieros. |

## Data Ingestion: fundamento informacional

*Data Ingestion* obtiene y prepara los datos de costo, uso y metadatos que necesitan las demás capacidades del dominio [2]. La asignación depende de que esos registros permitan relacionar importes y consumo con cuentas, recursos, jerarquías u otros identificadores pertinentes.

La calidad, granularidad y normalización de los datos condicionan qué atribuciones pueden sostenerse y compararse. Una regla de asignación no corrige por sí sola registros incompletos, periodos incompatibles o metadatos inconsistentes; esos límites deben quedar visibles para no presentar una precisión que la fuente no permite [2].

## Allocation: estrategia de asignación

### Destinos, reglas y trazabilidad

La **asignación de costos** atribuye un costo a un destino, como un producto, servicio, equipo, unidad organizativa o centro de costo. Ese destino representa la propiedad económica del consumo y no necesariamente coincide con quien administra el recurso. La atribución puede apoyarse en cuentas, jerarquías, etiquetas, datos de consumo u otras evidencias [3].

Su finalidad es mostrar qué gasto corresponde a cada destino y bajo qué criterio. Esto permite que los responsables comprendan el consumo asociado a su ámbito y aporta trazabilidad: una cifra atribuida debe relacionarse con una fuente, un destino y una regla explícita. La estrategia debe declarar alcance, periodo, granularidad, jerarquía de destinos y tratamiento de excepciones para que la asignación sea comprensible y repetible [3].

La asignación favorece la rendición de cuentas al identificar responsabilidades sobre el consumo. Sin embargo, atribuir un costo no implica realizar un cargo contable; esa diferencia corresponde a los mecanismos de *showback* y *chargeback* [4, 6].

### Jerarquías, etiquetas y metadatos

El **etiquetado** incorpora metadatos a cuentas, recursos o registros de consumo. Ejemplos genéricos son `owner`, para el responsable; `product`, para el producto o servicio; `environment`, para el entorno; y `cost_center`, para el destino financiero. Son categorías mínimas de identificación, no una taxonomía adoptada.

Las etiquetas facilitan clasificar y agrupar costos, y pueden aportar evidencia para una asignación directa o delimitar un reparto [3]. Su utilidad depende de la cobertura y consistencia de sus valores. No son el único mecanismo: la asignación también puede utilizar jerarquías de cuentas, relaciones entre recursos, dimensiones del proveedor, datos de consumo y reglas complementarias.

Una etiqueta no equivale a una política de asignación. El metadato describe el recurso o consumo; la política establece qué costos se distribuyen, hacia qué destinos, mediante qué regla y durante qué periodo. En servicios compartidos, conocer el responsable o entorno no determina cómo repartir el costo.

### Costos directos, compartidos y no asignados

Los costos pueden ser **directos** o **compartidos** por su relación con los destinos; **no asignado** describe su estado de atribución, no una tercera naturaleza excluyente. El directo se atribuye a un destino sin reparto. El compartido beneficia a varios destinos y puede agruparse en un fondo para distribuirse. El no asignado aún no tiene una atribución válida, por falta de evidencia o de una regla implementada [3].

Un costo no asignado no debe confundirse con uno compartido. En el compartido se conoce la naturaleza común del gasto; en el no asignado falta información o un mecanismo aplicado para atribuirlo. La práctica de *informed ignore* permite retener centralmente un costo compartido mediante una decisión consciente de no distribuirlo, sin clasificarlo como costo no identificado [3].

### Costos compartidos y conductores de asignación

Los fondos compartidos reúnen costos de capacidades, plataformas o servicios comunes. Su distribución requiere un **conductor de asignación** que represente la participación de cada destino. Puede basarse en mediciones de uso o en un indicador sustituto con una relación causal comprensible respecto del costo.

Entre los conductores candidatos se encuentran solicitudes, tiempo de CPU, capacidad de almacenamiento, usuarios activos o gasto directo. La selección del conductor depende de su capacidad para representar la causa o el grado de uso del servicio compartido, de su medición consistente y de su comprensión por quienes revisan la asignación. Un indicador disponible pero desvinculado del consumo puede producir una distribución formalmente calculable sin una atribución causal suficiente.

### Tasa, cobertura y conservación

La **tasa de asignación** es un valor práctico por unidad que permite distribuir un fondo compartido mediante el conductor elegido; no es la cobertura de asignación. Por ejemplo, si un fondo hipotético de USD 1.000 se reparte entre 1.000 unidades de uso, la tasa es de USD 1 por unidad. Un destino que utilizó 300 unidades recibe USD 300. Estas cifras son solo ilustrativas y no representan datos del proyecto ni de una empresa.

La **conservación** exige que lo distribuido entre los destinos, más cualquier importe retenido de manera intencional, coincida con el fondo inicial. Las diferencias pequeñas producidas por redondeos deben conciliarse y quedar documentadas.

La **cobertura de asignación** responde a una pregunta distinta: qué parte del costo total tiene un destino válido según la política y la granularidad declaradas [3]. Si USD 9.000 de un total de USD 10.000 tienen destino válido, la cobertura es del 90 %. Un importe retenido en un destino central explícito puede contar como costo con destino en la cobertura general, pero no como costo distribuido a productos; ambas vistas deben diferenciarse.

Si no existe un conductor utilizable o el total medido es cero, no se debe forzar el reparto: el importe se retiene y documenta hasta contar con una regla válida. Los créditos y reembolsos pueden distorsionar los porcentajes, por lo que la política debe indicar si se tratan de forma neta, bruta o separada.

La página oficial vigente describe de forma conceptual repartos fijos, proporcionales y basados en indicadores sustitutos. También presenta, en bloques separados de indicadores, fórmulas porcentuales y un ejemplo numérico de reparto por gasto, pero no establece como requisito una fórmula de tasa unitaria [3]. Tak et al. aportan una base técnica para distinguir uso atribuible y no atribuible en recursos compartidos, pero no definen una política FinOps y su evaluación en Xen presenta limitaciones de medición e interferencia entre cargas [7].

## Reporting & Analytics: visibilidad y showback

*Reporting & Analytics* transforma los datos de costo y uso en vistas comprensibles para los destinatarios e incluye la producción de reportes de *showback* [4]. Para sostener la transparencia de la asignación, los reportes deben permitir distinguir al menos el costo asignado a cada destino, el costo compartido distribuido o retenido y el costo que permanece no asignado, junto con el alcance y periodo de la vista.

El **showback** comunica los costos asignados y las reglas que los sustentan, pero no transfiere esos importes contablemente. Su propósito es dar visibilidad sobre consumo, propiedad y responsabilidad, de modo que los destinatarios puedan interpretar y cuestionar la información presentada [4, 6].

## Chargeback: imputación formal posterior

El **chargeback** utiliza la información de asignación y reporte para trasladar o registrar costos en presupuestos, centros de costo o sistemas financieros. A diferencia del *showback*, produce una imputación interna formal y requiere políticas contables, destinos financieros, conciliación, cierres y mecanismos de corrección [6]. No exige un pago externo adicional: el pago de la factura al proveedor y la distribución interna de esa responsabilidad son procesos distintos.

*Invoicing & Chargeback* pertenece al dominio *Manage the FinOps Practice*, no a *Understand Usage & Cost* [6]. El *showback* es necesario para comunicar el costo en FinOps, mientras que adoptar *chargeback* depende de la política contable de la organización y no indica automáticamente un nivel superior de madurez [6].

## Anomaly Management: retroalimentación continua

*Anomaly Management* identifica e investiga variaciones inesperadas a partir de datos de costo y uso, metadatos de asignación y capacidades de análisis [5]. No constituye un cuarto paso posterior a los reportes: opera como un ciclo continuo que puede revelar problemas de calidad de datos, atribuciones incorrectas o reglas que requieren revisión.

La relación conceptual es interactiva: la ingestión aporta datos; la asignación aporta contexto de propiedad; los reportes hacen visibles los resultados; y la gestión de anomalías devuelve hallazgos que pueden exigir ajustes en datos, metadatos, reglas o vistas [1, 5].

## Relación con economía unitaria

La economía unitaria puede utilizar costos previamente asignados como numerador, pero la elección de denominadores, fórmulas y métricas corresponde a FP-169 y queda fuera del alcance de este documento.

## Referencias

[1] FinOps Foundation. *Understand Usage & Cost*. https://www.finops.org/framework/domains/understand-usage-cost/. Fuente oficial consultada el 2026-09-17.

[2] FinOps Foundation. *Data Ingestion*. https://www.finops.org/framework/capabilities/data-ingestion/. Fuente oficial consultada el 2026-09-17.

[3] FinOps Foundation. *Allocation*. https://www.finops.org/framework/capabilities/allocation/. Fuente oficial consultada nuevamente el 2026-09-17. Registrada en la matriz de fuentes vigente como fuente 002; la URL canónica vigente difiere de la consignada originalmente en esa fila.

[4] FinOps Foundation. *Reporting & Analytics*. https://www.finops.org/framework/capabilities/reporting-analytics/. Fuente oficial consultada el 2026-09-17.

[5] FinOps Foundation. *Anomaly Management*. https://www.finops.org/framework/capabilities/anomaly-management/. Fuente oficial consultada el 2026-09-17.

[6] FinOps Foundation. *Invoicing & Chargeback*. https://www.finops.org/framework/capabilities/invoicing-chargeback/. Fuente oficial consultada nuevamente el 2026-09-17. La matriz de fuentes vigente no le asigna una fila independiente; la fuente 002 registra los términos *showback* y *chargeback* dentro de Allocation.

[7] Tak, B. C., Kwon, Y. y Urgaonkar, B. (2017). “Resource Accounting of Shared IT Resources in Multi-Tenant Clouds”. *IEEE Transactions on Services Computing*, 10(2), 302-315. https://doi.org/10.1109/TSC.2015.2453980. Evidencia utilizada: sección 3, p. 305, y secciones 5.2-5.3 sobre uso no atribuible y limitaciones. Registrada en la matriz de fuentes vigente en la fila académica titulada con el nombre del artículo, sin ID numérico asignado.

Matriz contrastada: `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`.
