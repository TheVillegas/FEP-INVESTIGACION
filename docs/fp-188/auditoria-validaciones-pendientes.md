# Auditoría de validaciones pendientes de TINV-06

## Resultado

Se revisaron los artefactos locales de FP-172 y FP-182 a FP-188 con corte al 21-09-2026. Los 17 registros existen en la matriz consolidada. Ninguno dispone todavía de toda la medición, dato interno o aprobación formal necesaria para presentarse como validación productiva; por lo tanto, el resultado formal sigue siendo **0 cerrados y 17 pendientes**.

La revisión ampliada encontró evidencia parcial reutilizable para **13 de los 17 registros**. Esa evidencia ya permite precargar valores, configuración o contexto sin inventar datos. VAL-01, VAL-02, VAL-08 y VAL-09 siguen sin un valor medido o aprobado que pueda precargarse. El procedimiento exacto para cerrar cada registro está documentado en [`plan-cierre-17-validaciones.md`](plan-cierre-17-validaciones.md).

Las 13 precargas quedaron incorporadas en `docs/fp-188/matriz-validacion-insumos-tinv06.xlsx`. Las 17 filas conservan el estado `Pendiente humano`; la precarga aporta contexto y valores provisionales, pero no equivale a cierre.

Esta auditoría confirma la ausencia de evidencia; no reemplaza la aprobación del responsable indicado ni convierte supuestos o proxies en datos reales.

## Valores que ya pueden precargarse

| ID | Valor o evidencia reutilizable | Clasificación correcta | Límite |
|---|---|---|---|
| STO-03 | Blob Hot LRS, 500 GB iniciales y 20 % de crecimiento anual | Supuesto documentado | No informa cantidad ni tipo de operaciones. |
| OBS-03 | Basic Logs, 50 GB/mes, 30 días; escenario optimizado de 40 GB/mes | Supuesto/estimación | No informa consultas, GB escaneados ni retención adicional. |
| OPT-04 | 50 h totales; 10 h no producción y 8 h logs identificables | Estimación de ingeniería | Egress y horas comunes no tienen asignación aprobada; no completar B17:C19 automáticamente. |
| FIN-10 | 5,5 % anual | Proxy público MDSF | No es WACC de ONEBYTE. |
| FIN-11 | USD 8,534526164/h | Proxy público derivado | No es costo empresa cargado. |
| FIN-12 | 50 h por alternativa regional | Estimación de ingeniería | No son horas reales ni aprobadas. |
| FIN-13 | 1 h/mes por alternativa regional | Estimación de ingeniería | No son horas reales ni aprobadas. |
| VAL-03 | Inventario de Container Apps, PostgreSQL, Blob y Monitor en Chile Central | Contexto técnico | Falta aprobación servicio por servicio. |
| VAL-04 | Inventario equivalente en East US y riesgo de transferencia internacional | Contexto técnico | Falta aprobación contractual/legal. |
| VAL-05 | Backup automático de PostgreSQL por siete días, sin LTR/GRS | Configuración base | No permite inferir RPO ni RTO. |
| VAL-06 | Línea base sin HA; SLA público de referencia de 99,9 % | Supuesto documentado | Falta aceptación de Arquitectura/Continuidad. |
| VAL-07 | Azure Basic Support, USD 0 adicional en el escenario base | No aplica justificado para el escenario | Debe reabrirse si la cobertura requerida exige soporte pago. |
| VAL-10 | Escenario Azure completo, dos regiones, 60 meses y USD | Escenario documentado | Falta aprobación formal del equipo. |

## Detalle

| ID | Validación requerida | Evidencia encontrada | Resultado | Responsable requerido |
|---|---|---|---|---|
| STO-03 | Operaciones Blob | La arquitectura excluye operaciones por falta de volumen; no hay telemetría de lecturas, escrituras, listados o recuperación. | Pendiente | Datos / Aplicación |
| OBS-03 | Consultas y retención adicional de Monitor | El modelo valoriza ingesta y excluye consultas/retención adicional; no hay volumen medido. | Pendiente | SRE / Seguridad |
| OPT-04 | Costo por palanca | FP-187 contiene 50 h totales estimadas, pero no un costo u horas aprobadas por palanca. | Pendiente | Equipo técnico / Finanzas |
| FIN-10 | WACC o tasa interna | Existe una Tasa Social de Descuento pública de 5,5 %, no un WACC corporativo aprobado. | Pendiente | Finanzas |
| FIN-11 | Costo empresa cargado | Existe un proxy de USD 8,53/h derivado de ingreso neto público, no costo empresa. | Pendiente | Finanzas / RR. HH. |
| FIN-12 | Horas reales de implementación | Existen 50 h bottom-up estimadas; no hay aprobación ni timesheets. | Pendiente | Equipo técnico |
| FIN-13 | Horas reales de operación | Existe 1 h/mes estimada; no hay aprobación ni timesheets. | Pendiente | Operación / FinOps |
| VAL-01 | Latencia medida en Chile Central | La proximidad es una hipótesis; no hay medición desde población y dependencias objetivo. | Pendiente | SRE / Redes |
| VAL-02 | Latencia medida en East US | No hay medición desde población y dependencias objetivo. | Pendiente | SRE / Redes |
| VAL-03 | Residencia aprobada en Chile Central | La alternativa está descrita, pero no existe aprobación servicio por servicio. | Pendiente | Legal / Seguridad / Datos |
| VAL-04 | Residencia aprobada en East US | Se advierte la transferencia internacional, pero no existe aprobación contractual o legal. | Pendiente | Legal / Seguridad / Datos |
| VAL-05 | RPO/RTO aprobados | Se modela backup de siete días; no se definieron RPO, RTO ni retención obligatoria. | Pendiente | Continuidad / Negocio |
| VAL-06 | Requisito de HA | La línea base sin HA y el SLA público de referencia están documentados; no existe aceptación del negocio. | Pendiente | Arquitectura / Continuidad |
| VAL-07 | Soporte pagado | No existe decisión sobre plan, cobertura ni costo de soporte. | Pendiente | Operación / Finanzas |
| VAL-08 | SLO de latencia | No existe umbral, percentil ni población aprobados para evaluar las regiones. | Pendiente | Producto / SRE |
| VAL-09 | Métricas reales de rendimiento | No hay telemetría de CPU, memoria, conexiones, errores, throughput y latencia. | Pendiente | SRE / DBA |
| VAL-10 | Aprobación del escenario ilustrativo | El escenario está documentado como académico e ilustrativo, pero no hay aprobación formal del equipo. | Pendiente | Equipo del proyecto |

## Evidencia que sí quedó validada

- Los 17 registros están presentes y correctamente identificados como `Pendiente humano` en la matriz consolidada.
- Las ausencias no se convierten en cero ni se incluyen como cargos ficticios.
- La línea base sin HA, las exclusiones de Blob/Monitor y los proxies financieros están declarados explícitamente.
- El PRI descontado de FP-187 queda calculado con el flujo descontado acumulado: Chile Central recupera en el mes 30 y East US no recupera dentro de 60 meses bajo los proxies actuales.

## Regla de cierre

Cada registro solo puede cambiar a validado cuando el responsable entregue la medición, valor o aprobación correspondiente. Los papers y páginas públicas respaldan método, tarifas de lista o proxies, pero no pueden sustituir telemetría, WACC, costo empresa, timesheets ni decisiones de arquitectura y cumplimiento de ONEBYTE.
