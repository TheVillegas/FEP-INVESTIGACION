# Consolidado conceptual de FP-169 y FP-170

> **Base conceptual preparada para revisión humana.** Este documento es un punto de entrega para FP-171, no el glosario final ni el mapa conceptual terminado. No declara completas las tareas en Jira.

## Documentos y conexión

- **FP-170:** [[fp-170 Asignacion de costos]] — propiedad del gasto, metadatos, reparto, cobertura y efecto financiero.
- **FP-169:** [[fp-169 Economia unitaria]] — costo por transacción, cliente, solicitud y token, con alcance y poblaciones explícitos.

La relación que debe conservarse es **asignación → costo asignado → costo unitario**: las reglas atribuyen gasto a un ámbito; ese costo constituye el numerador que se relaciona con su actividad durante el mismo periodo. El *showback* comunica la atribución y el *chargeback* la incorpora formalmente al presupuesto o contabilidad; ninguno reemplaza el cálculo de economía unitaria. Esta secuencia orienta el futuro mapa, pero no constituye su entrega completa.

## Verificación y pendientes

- [x] Contraste con las páginas oficiales de Allocation, Unit Economics e Invoicing & Chargeback; fuente acotada adicional para tokens y caché.
- [x] Diferenciación entre costo compartido, estado no asignado y retención central identificada.
- [x] Separación de tasa unitaria de reparto, peso adimensional y porcentaje de cobertura.
- [x] Cuatro métricas con numerador, denominador, unidad, periodo, inclusión y fuente; tratamiento de fallos, clientes únicos, caché y denominador cero.
- [x] Fórmulas derivadas identificadas como formulación del documento, sin inventar datos, tarifas ni resultados.
- [ ] Revisión académica humana y aprobación de las definiciones.
- [ ] Ejemplos numéricos reproducibles con datos verificados y compatibilidad con FP-52 exigidos originalmente en FP-169: **no cumplidos; diferidos por el alcance conceptual explícito**. No se incorporó caso aplicado para ninguna de las dos tareas.
- [ ] Completar registro bibliográfico de las fuentes adicionales y revisar la URL de la fuente 002, sin alterar aquí la matriz.

## Terminología para desarrollar en FP-171

Inventario de términos y ubicaciones, no definiciones finales del glosario. Las traducciones son etiquetas de trabajo; las fórmulas locales no se presentan como terminología normativa.

| Términos en español / inglés | Sección de origen | Fuente para desarrollar la entrada |
|---|---|---|
| Asignación de costos / cost allocation; etiquetado / tagging; centro de costo / cost center | FP-170: Asignación de costos y Etiquetado | Allocation [A] |
| Costos directos / direct costs; compartidos / shared costs; no asignados / unallocated costs; retención central / centrally budgeted shared costs | FP-170: Costos compartidos | Allocation [A] |
| Presentación informativa de costos / showback; imputación interna formal / chargeback | FP-170: Showback frente a chargeback | Invoicing & Chargeback [B] |
| Conductor / allocation driver; tasa unitaria de reparto / unit allocation rate; peso / allocation weight; cobertura / allocation coverage | FP-170: Tasa de asignación | Allocation [A] y formulaciones locales explícitas |
| Economía unitaria / unit economics; costo unitario / unit cost; costo con cargas completas / fully loaded cost | FP-169: Alcance y base del costo | Unit Economics [C] |
| Transacción de negocio / business transaction; cliente atendido / served customer; solicitud / request | FP-169: Cuatro métricas y sus poblaciones | Unit Economics [C] y elecciones operativas locales |
| Token de entrada / input token; token de salida / output token; almacenamiento de contexto en caché / prompt caching | FP-169: Tokens: medición y facturación | Fuente de tokens [D] |

## Límite de la entrega siguiente

FP-171 requiere **un glosario consistente y sustentado en fuentes, además de un mapa conceptual**. Permanecen pendientes su redacción, la integración terminológica con FP-167/FP-168, los enlaces al informe y la articulación compartida con FP-53, FP-54 y FP-56. Los documentos existentes de fases y personas se leyeron solo como contexto y no se modificaron. No se realizó análisis comparativo, recomendaciones ni conclusiones académicas.

## Fuentes verificadas

[A] FinOps Foundation. *Allocation*. https://www.finops.org/framework/capabilities/allocation/. Matriz: 002; URL canónica distinta de la registrada.

[B] FinOps Foundation. *Invoicing & Chargeback*. https://www.finops.org/framework/capabilities/invoicing-chargeback/. Sin fila independiente en el CSV consultado.

[C] FinOps Foundation. *Unit Economics*. https://www.finops.org/framework/capabilities/unit-economics/. Matriz: 003.

[D] FinOps Foundation. *GenAI FinOps: How Token Pricing Really Works*. https://www.finops.org/wg/genai-finops-how-token-pricing-really-works/. Sin fila independiente en el CSV consultado.

Consulta: 2026-09-17. Trazabilidad por tarea: [[../papers/info_mds/_trazabilidad/research-log|Bitácora de investigación]], registros 10 y 11. La referencia académica de Tak et al. en FP-170 se conserva como antecedente, sin una nueva revisión del artículo en esta intervención.
