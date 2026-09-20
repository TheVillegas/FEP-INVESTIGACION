# Economía unitaria en FinOps

> **Estado:** Documento de información verificada. El alcance es conceptual y no contiene datos reales, cálculos aplicados ni resultados del proyecto. Las reglas de conteo, alcance e interpretación operativa son formulaciones del proyecto; no constituyen definiciones universales de la fuente.

La capacidad **Unit Economics** forma parte del dominio **Quantify Business Value** del FinOps Framework. Su propósito es relacionar costos con unidades técnicas o de negocio que permitan comprender la eficiencia, la sostenibilidad y el valor de un producto o servicio [1, 2]. Una métrica unitaria expresa el costo atribuible a un alcance y periodo dividido entre las unidades observadas en ese mismo alcance y periodo.

## El costo por unidad como métrica de producto

FP-170 proporciona el numerador mediante el costo asignado al producto, servicio o proceso. FP-169 selecciona el denominador, define qué se cuenta y explica qué decisión puede apoyar. Esta separación evita repetir aquí las reglas de etiquetado, reparto y conciliación desarrolladas en [[fp-170 Asignacion de costos]].

El numerador debe indicar si comprende solo costos directos o un **costo con cargas completas** (*fully loaded cost*). Este último puede incorporar, cuando corresponda, infraestructura compartida, datos, observabilidad, soporte y otros componentes asignados. Ambas vistas son válidas para preguntas distintas, pero no son comparables si sus inclusiones cambian sin declararlo. También deben mantenerse explícitos la moneda, la base del costo, el periodo, los descuentos, los créditos y las exclusiones.

El denominador representa una población definida, no cualquier volumen disponible. Numerador y denominador deben corresponder al mismo producto o proceso, periodo y población. El resultado es un promedio útil para observar tendencias y diferencias documentadas; por sí solo no demuestra rentabilidad, calidad, causalidad ni valor obtenido [1].

## Métricas de unidad de negocio (Business Unit Metrics)

### Costo por transacción completada

Relaciona el costo asignado al proceso con la cantidad de transacciones de negocio completadas. Antes de calcularlo se debe definir:

- qué evento representa una finalización válida;
- qué estados se excluyen por cancelación o incompletitud;
- qué clave evita contar dos veces la misma transacción; y
- qué alcance y periodo comparten el costo y las finalizaciones.

Los intentos fallidos y los reintentos no aumentan el número de transacciones completadas, pero sus costos permanecen en el numerador cuando pertenecen al proceso medido. Por ello, una variación puede reflejar cambios de eficiencia, confiabilidad, demanda o composición de transacciones; la razón aislada no identifica la causa.

### Costo por cliente atendido

Relaciona el costo asignado con clientes únicos que recibieron el servicio durante el periodo. “Cliente atendido” debe definirse mediante un evento verificable de actividad o prestación; no equivale automáticamente al total histórico de cuentas registradas. Cada identidad se cuenta una sola vez dentro del periodo y el criterio de unicidad debe permanecer estable.

La mezcla de segmentos puede alterar el promedio: clientes con necesidades, niveles de servicio o intensidad de uso distintos no consumen necesariamente los mismos recursos. Cuando esa heterogeneidad sea relevante, el resultado se presenta por segmentos comparables o se acompaña con la composición de la población, sin ocultar el promedio general.

## Métricas de eficiencia de recursos (Resource Efficiency Unit Metrics)

### Costo por solicitud

Relaciona el costo asignado con solicitudes observadas en un punto técnico definido. La ficha de la métrica debe escoger y nombrar el criterio de conteo: solicitudes intentadas, solicitudes exitosas u otra población delimitada. Contar intentos, como hacía una definición previa, es una elección posible y no un criterio universal.

La telemetría debe distinguir solicitudes originales, reintentos, llamadas internas y registros duplicados. Un reintento real puede contarse como otro intento si esa es la población declarada; un duplicado de observabilidad no representa actividad adicional. La métrica ayuda a analizar eficiencia operativa, pero una solicitud no equivale necesariamente a una transacción ni a un resultado de negocio [1].

### Costo por token de IA

Relaciona un costo declarado con los tokens procesados durante el mismo alcance y periodo. Los registros del proveedor o de la plataforma pueden separar categorías con precios o semánticas diferentes. Cuando existan esas diferencias, se conservan las categorías reportadas y se documenta cualquier agregación; no se supone una clasificación universal ni se suman contadores que se solapen [3].

Conviene distinguir dos vistas:

- **Costo del modelo o API por token:** considera los cargos del servicio de IA incluidos en la medición.
- **Costo total de servir el producto por token:** añade, cuando corresponda, infraestructura, datos, observabilidad y otros costos de soporte previamente asignados.

El segundo es un costo medio del producto bajo el alcance declarado, no la tarifa del proveedor ni el costo marginal de un token adicional. El costo por token tampoco representa automáticamente valor: una reducción puede coincidir con respuestas menos útiles, menor calidad o más intentos para completar el mismo resultado. Los materiales de FinOps para GenAI recomiendan conectar el consumo técnico con el costo del caso de uso y del resultado exitoso [3, 4].

## Cómo apoya decisiones de producto

Las métricas unitarias permiten:

- observar tendencias dentro de un alcance estable;
- evaluar decisiones de diseño y arquitectura;
- informar conversaciones de empaquetado y precios;
- analizar margen y sostenibilidad económica; y
- relacionar el costo con resultados y valor de producto [1, 2].

La razón no debe utilizarse como explicación causal por sí sola. Una variación requiere revisar volumen, mezcla de segmentos, calidad, confiabilidad, alcance del costo y cambios técnicos antes de atribuirla a una decisión concreta.

## Riesgos y controles de interpretación

| Riesgo | Control mínimo |
|---|---|
| Manipulación del denominador | Congelar la definición, la clave de unicidad y los estados incluidos; versionar todo cambio. |
| Efecto de mezcla | Acompañar el promedio con segmentos comparables cuando la población sea heterogénea. |
| Degradación de calidad o confiabilidad | Revisar la métrica junto con resultados, errores, reintentos y controles de calidad. |
| Alcance parcial del costo | Declarar si la vista es directa o con cargas completas, con inclusiones y exclusiones. |
| Periodos, poblaciones o unidades incompatibles | Conciliar alcance, fechas, zona horaria, moneda y unidad antes del cálculo. |
| Volatilidad por bajo volumen | Identificar periodos con pocas unidades y evitar conclusiones a partir de cambios aislados. |
| Confusión entre costo por token y valor | Relacionar el consumo técnico con el caso de uso y el resultado; no usar tokens como sustituto automático de valor. |

## Ficha mínima para reproducibilidad

Cada medición debe conservar:

- [ ] nombre, propósito, versión, responsable y decisión que pretende apoyar;
- [ ] producto, servicio o proceso, población, periodo y zona horaria;
- [ ] fuente del costo, moneda, base, inclusiones, exclusiones y referencia a la asignación de FP-170;
- [ ] evento contado, estados, clave de unicidad, filtros y tratamiento de fallos, reintentos y duplicados;
- [ ] para tokens, modelo, fuente del contador, categorías preservadas y reglas de agregación;
- [ ] consulta o procedimiento reproducible, controles de conciliación y precisión del resultado; y
- [ ] métricas de calidad, confiabilidad o resultado utilizadas para interpretar el costo unitario.

Si el denominador es cero, el costo por unidad es **indefinido** y se excluye de agregaciones que requieran una razón, indicando la convención aplicada. Un dato ausente no equivale a actividad nula. El costo se conserva y se informa por separado hasta contar con una población válida.

## Referencias

[1] FinOps Foundation. *Unit Economics*. https://www.finops.org/framework/capabilities/unit-economics/. Fuente oficial consultada el 2026-09-17; registrada como fuente 003 en la matriz de fuentes vigente.

[2] FinOps Foundation. *Quantify Business Value*. https://www.finops.org/framework/domains/quantify-business-value/. Fuente oficial consultada el 2026-09-17.

[3] FinOps Foundation. *GenAI FinOps: How Token Pricing Really Works*. https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/. Fuente oficial consultada el 2026-09-17; utilizada para diferencias de medición y precio entre categorías, sin generalizarlas a todos los proveedores.

[4] FinOps Foundation. *GenAI FinOps vs. Cloud FinOps*. https://www.finops.org/wg/genai-finops-vs-cloud-finops/. Fuente oficial consultada el 2026-09-17; utilizada para relacionar el costo técnico con el caso de uso y el resultado.

Matriz contrastada: `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`.
