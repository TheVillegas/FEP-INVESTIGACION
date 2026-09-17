# Economía unitaria en FinOps

> **FP-169 — Borrador conceptual pendiente de revisión humana.** Sin caso aplicado, importes ni volúmenes inventados. Las definiciones y fórmulas preparan el trabajo posterior, pero no satisfacen todavía los ejemplos numéricos reproducibles del requisito original.

La **economía unitaria** relaciona el gasto tecnológico con unidades de actividad o valor. FinOps Foundation distingue métricas técnicas, como costo por solicitud o token, de métricas de negocio, como costo por transacción o cliente. El costo unitario permite expresar cuánto costo corresponde, en promedio, a una unidad definida; por sí solo no mide rentabilidad ni demuestra valor obtenido [1].

## Alcance y base del costo

Se define $s$ como el ámbito delimitado por producto o servicio, entorno y población atendida; $p$ es el intervalo de medición con inicio, fin y zona horaria explícitos. $C_{s,p}$ representa el costo atribuible a ese ámbito durante ese periodo, en una moneda declarada. No corresponde dividir el gasto de toda una organización por la actividad de un único servicio.

El numerador puede representar costo directo o costo con componentes indirectos y compartidos asignados. Una vista de **costo con cargas completas** (*fully loaded cost*) identifica todos los componentes incluidos y sus exclusiones: no basta con sumar únicamente la factura del modelo de IA. La asignación previa se desarrolla en [[Asignacion de costos]] [1, 2].

La base de costo también se declara: facturado, efectivo o amortizado, según el propósito y los datos disponibles. Si se distribuye un compromiso entre periodos, se documenta esa transformación; no se impone una base universal. Descuentos, créditos, impuestos, soporte y conversiones monetarias requieren tratamiento explícito y consistente. Un crédito puede producir costo neto negativo: se informa como ajuste financiero, no como consumo negativo ni prueba automática de eficiencia.

## Cuatro métricas y sus poblaciones

Las fórmulas siguientes son **formulaciones matemáticas del documento a partir del concepto de costo unitario de [1]**, no citas literales ni resultados medidos. Cada fila utiliza un $s$ específico y el mismo $p$ para numerador y denominador. Las fuentes de datos son entradas requeridas, todavía no incorporadas.

| Métrica | Fórmula | Numerador | Denominador | Unidad | Periodo | Inclusión definida | Fuente conceptual y datos requeridos |
|---|---|---|---|---|---|---|---|
| Costo por transacción | $C_{s,p}/N_{\mathrm{tx},s,p}$ | Costo de operar el proceso de negocio delimitado | Transacciones de negocio completadas exitosamente y únicas | Moneda/transacción | $p$ | El costo conserva fallos y reintentos del proceso; estos no suman transacciones exitosas | [1, 2]; costos asignados y registro de resultados de negocio |
| Costo por cliente | $C_{s,p}/N_{\mathrm{cli},s,p}$ | Costo de atender la población delimitada | Clientes únicos con actividad de servicio registrada en $p$ | Moneda/cliente atendido en $p$ | $p$ | Cada cliente se cuenta una vez; no se usa el inventario histórico de registrados | [1, 2]; costos y registro de actividad con identidad estable |
| Costo por solicitud | $C_{s,p}/N_{\mathrm{req},s,p}$ | Costo de servir el punto técnico delimitado | Intentos de solicitud recibidos en ese punto | Moneda/solicitud | $p$ | Incluye intentos exitosos, fallidos y reintentos; elimina duplicados de registro, no intentos reales | [1]; costos y telemetría de solicitudes |
| Costo por token de IA | $C_{s,p}/T_{s,p}$ | Costo del servicio de IA según la base declarada | Tokens de entrada y salida contabilizados sin solapamiento | Moneda/token | $p$ | Entrada reutilizada se cuenta una vez dentro de la entrada; costos de caché se distinguen | [1, 3]; costos, medición de tokens y clases de facturación |

Estas poblaciones son elecciones operativas explícitas para las definiciones, no obligaciones universales de FinOps. Una solicitud técnica no equivale a una transacción: una operación de negocio puede generar varios intentos. Si se utiliza solo solicitudes exitosas, cambia el nombre del denominador; el costo de los fallos permanece incluido cuando pertenece al proceso medido. Para clientes, otro criterio de actividad exige declarar el evento que habilita el conteo, no sustituir silenciosamente clientes atendidos por cuentas registradas.

## Tokens: medición y facturación

En modelos de texto, un token es una unidad de procesamiento de fragmentos de texto; no equivale necesariamente a una palabra. Su conteo depende del modelo y del mecanismo de tokenización. Entrada, salida y reutilización de contexto en caché pueden tener tratamientos económicos diferentes; la escritura y lectura de caché también pueden originar cargos distintos [3].

Para una medición que informa entrada total $I$, entrada reutilizada $H$ como subconjunto de $I$, y salida $O$, se define:

$$
T_{s,p}=I_{s,p}+O_{s,p},\qquad I_{s,p}=(I_{s,p}-H_{s,p})+H_{s,p}
$$

Esta identidad requiere $0\leq H_{s,p}\leq I_{s,p}$ y confirmar la semántica del registro. No se suma $H$ nuevamente a $I$. Para el costo, se concilian por separado entrada no almacenada, lectura de caché, escritura cuando corresponda y salida. Los cargos por almacenamiento o capacidad se conservan en su unidad original, sin convertirlos ficticiamente en tokens.

El cociente agregado $C_{s,p}/T_{s,p}$ es un **costo medio**, no la tarifa unitaria del proveedor. Puede incluir infraestructura y costos compartidos; tampoco estima por sí solo el costo marginal de un token adicional. Expresarlo por millón de tokens solo cambia la escala mediante $10^6 C_{s,p}/T_{s,p}$, no lo transforma en precio de lista.

## Entradas mínimas para reproducibilidad

Cada cálculo posterior debe conservar una ficha con:

- **Identificación:** métrica, versión, ámbito $s$, responsable y periodo $p$.
- **Costo:** fuente y filas de origen, moneda, base, inclusiones, exclusiones y versión de las reglas de asignación.
- **Actividad:** fuente, evento contado, clave de unicidad, estado, filtros y tratamiento de reintentos; en IA, modelo y semántica de clases y contadores.
- **Transformación:** consulta o procedimiento reproducible, conciliación de totales, numerador, denominador y precisión del resultado.

Si el denominador es cero, el cociente es **indefinido**, no cero. Datos ausentes tampoco equivalen a actividad nula. Se conserva el costo y se informa por qué no puede calcularse la métrica. Los ejemplos con datos verificados y su compatibilidad aplicada con FP-52 quedan fuera del alcance acordado; FP-169 no se declara completa.

## Referencias

[1] FinOps Foundation. *Unit Economics*, secciones Definition y Functional Activities. https://www.finops.org/framework/capabilities/unit-economics/. Fuente 003 de la matriz FP-48.

[2] FinOps Foundation. *Allocation*, sección Definition. https://www.finops.org/framework/capabilities/allocation/. Fuente 002; el CSV conserva una URL anterior.

[3] FinOps Foundation. *GenAI FinOps: How Token Pricing Really Works*, secciones Not All Tokens Are Created Equal y Prompt Caching. https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/. Sin fila independiente en el CSV consultado; registro pendiente. Se utiliza para distinciones conceptuales, no para tarifas ni generalizaciones numéricas.

Fuentes oficiales consultadas el 2026-09-17. Matriz contrastada: `docs/TINV_Matriz_de_Fuentes_final_2026-09-13.xlsm - Matriz de Fuentes.csv`.
