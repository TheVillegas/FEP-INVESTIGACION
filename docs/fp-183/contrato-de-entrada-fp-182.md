# Contrato de entrada de FP-182 para FP-183

FP-182 debe entregar los datos aprobados que permitan calcular el TCO de la misma arquitectura en Chile Central y East US. Este contrato **no define valores**.

## Regla de entrega

Cada campo debe indicar responsable, estado y fuente. Estado permitido: `Pendiente`, `Validado` o `No aplica justificado`. Un campo requerido sin valor validado bloquea el cálculo correspondiente.

| Grupo | Campo requerido | Unidad / formato | Responsable | Estado | Validación |
|---|---|---|---|---|---|
| Arquitectura | Componentes y cantidad por entorno | inventario y unidades | FP-182 | Pendiente | Corresponde a una arquitectura idéntica en ambas regiones. |
| Supuestos técnicos | Configuración, dependencias y restricciones técnicas que afectan consumo | lista estructurada; unidad aplicable | FP-182 | Pendiente | Cada supuesto se vincula a un componente o categoría de costo. |
| Usuarios y demanda | Usuarios, solicitudes y patrón horario/mensual | usuarios; solicitudes/mes; perfil temporal | FP-182 | Pendiente | Horizonte y granularidad explícitos; sin proyecciones implícitas. |
| Cómputo | Perfil de recursos, réplicas, horas y escalado de cada componente | vCPU, GiB, réplicas, horas/mes | FP-182 | Pendiente | Cubre producción y no producción; consistente con la arquitectura. |
| Almacenamiento | Tipo, capacidad, transacciones, IOPS y retención | GiB, operaciones/mes, IOPS, meses | FP-182 | Pendiente | Separa datos, backups, logs y artefactos cuando aplique. |
| Transferencia/red | Tráfico de entrada/salida e interregional; servicios de red | GiB/mes; solicitudes/mes | FP-182 | Pendiente | Origen, destino y dirección identificados. |
| Licencias | Productos, métricas de licencia y elegibilidad de beneficio | licencia/mes; núcleo; usuario u otra métrica | FP-182 | Pendiente | Incluye solo derechos confirmados; exclusiones documentadas. |
| Soporte | Plan de soporte y métrica de cobro | plan; USD/mes o porcentaje | FP-182 | Pendiente | Plan aplicable a ambas regiones y base de cálculo declarada. |
| No producción | Entornos, tamaño, horario y reglas de apagado | entorno; porcentaje o horas/mes | FP-182 | Pendiente | Diferenciado de producción sin alterar la arquitectura base. |
| Operaciones | Actividades, horas, roles y herramientas operativas | horas/mes; tarifa/hora; unidad/mes | FP-182 | Pendiente | Incluye operación, monitoreo, respaldo y soporte operativo acordados. |
| SLA | Objetivos y mecanismos que impactan costo | porcentaje; descripción | FP-182 | Pendiente | Relacionado con redundancia, disponibilidad y recuperación. |
| Financiero | Moneda base, tipo de cambio y regla de actualización | ISO 4217; fecha; regla | FP-182 | Pendiente | Misma moneda base, fecha de corte y regla para ambas regiones. |
| Exclusiones | Costos, servicios o actividades fuera de alcance | lista con justificación | FP-182 | Pendiente | No deja categorías de costo ambiguas. |

## Metadatos obligatorios de precios

Para cada precio usado en el catálogo, registrar:

| Campo | Requisito de validación |
|---|---|
| SKU o producto | Identificador y nombre comercial inequívocos. |
| Región | `Chile Central` o `East US`; no usar precio global sin justificación. |
| Moneda | Código ISO 4217 y moneda base de conversión si difiere. |
| Unidad | Unidad facturable exacta: hora, vCPU-segundo, GiB/mes, operación u otra. |
| Fecha | Fecha de consulta y vigencia/precio efectivo si está disponible. |
| URL oficial | Enlace oficial de Microsoft/Azure o documento oficial aplicable. |

## Restricciones de comparabilidad

- Usar la misma arquitectura, demanda, periodo de 60 meses, SLA y reglas operativas en ambas regiones.
- Diferenciar solo variables regionales justificadas, como precio, moneda, disponibilidad o transferencia explícitamente documentada.
- Normalizar unidades, moneda base, fecha de corte y redondeo antes de comparar.
- No mezclar precios de fechas, SKUs, modalidades de compra ni entornos sin trazabilidad.
- Toda excepción debe indicar motivo, impacto y aprobación de FP-182.
