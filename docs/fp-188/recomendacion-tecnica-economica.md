# FP-188 — Recomendación técnica y económica de TINV-06

Este documento convierte los resultados de FP-182 a FP-187 en una recomendación condicionada para el escenario ilustrativo de TINV-06. La recomendación es defendible para discusión académica, pero no constituye aprobación de arquitectura productiva, proveedor, presupuesto ni despliegue.

> **Recomendación:** mantener la arquitectura común de Azure Container Apps + PostgreSQL Flexible Server + Blob Storage + Azure Monitor. Si ambas regiones cumplen los mismos requisitos de latencia, residencia de datos, HA y SLA, **East US es la opción económica predeterminada**. **Chile Central debe seleccionarse cuando las restricciones técnicas, regulatorias o contractuales requieran operar en Chile**; dentro de ese escenario, el paquete FinOps evaluado presenta VAN positivo con los proxies actuales. Las palancas deben desplegarse de forma gradual y medible, y el rightsizing de PostgreSQL requiere evidencia de rendimiento antes de aplicarse.

## Quick path

1. Confirmar las restricciones de latencia, residencia de datos, HA/SLA y soporte.
2. Sustituir la tasa, tarifa y horas proxy de FP-187 por datos internos o aprobar formalmente su uso académico.
3. Ejecutar una prueba de rendimiento antes de modificar vCPU/vCores.
4. Recalcular VAN, TIR y PRI con los inputs validados.
5. Seleccionar Chile Central o East US aplicando los gates de decisión de este documento.

## 1. Base técnica común

| Capa | Configuración evaluada | Condición para mantenerla |
|---|---|---|
| Aplicación | Azure Container Apps Consumption, 1 vCPU y 2 GiB en producción | Medir rendimiento, escalado y disponibilidad durante el piloto. |
| No producción | 0,5 vCPU, 1 GiB y ventana de 264 h/mes | Mantener apagado programado solo si no afecta pruebas ni soporte. |
| Datos | PostgreSQL Flexible Server General Purpose, 2 vCores, 100 GiB | No hacer rightsizing sin métricas de CPU, memoria, conexiones y latencia. |
| Objetos | Blob Storage Hot LRS, 500 GB iniciales y 20% de crecimiento anual | Validar operaciones y requisitos de redundancia. |
| Observabilidad | Azure Monitor Basic Logs, 50 GB/mes y retención de 30 días | Medir consultas, retención efectiva y cobertura operativa. |
| Respaldo | Backup automático de PostgreSQL, 7 días, sin LTR/GRS en la base | Confirmar RPO/RTO y obligación de residencia antes de excluir geo-redundancia. |

La arquitectura es la misma en ambas regiones para que la comparación sea incremental. FP-182 la define como escenario ilustrativo; no se debe leer como diseño productivo aprobado.

## 2. Evidencia económica actual

Los valores siguientes provienen de los artefactos verificados. FP-187 usa proxies públicos y estimaciones bottom-up, por lo que los resultados son provisionales.

| Indicador a 60 meses | Chile Central | East US | Interpretación |
|---|---:|---:|---|
| TCO cloud base | USD 23.256,32 | USD 16.474,60 | East US es aproximadamente 29,2% menor en gasto base. |
| Ahorro bruto de FP-184 | USD 1.453,15 | USD 936,48 | Chile tiene mayor ahorro bruto por las mismas palancas. |
| Operación FinOps modelada | USD 512,07 | USD 512,07 | Proxy de 1 h/mes por escenario. |
| Implementación modelada | USD 426,73 | USD 426,73 | Proxy de 50 h por escenario. |
| Costo optimizado + operación + implementación | USD 22.741,97 | USD 16.476,92 | East US conserva una ventaja de USD 6.265,05 bajo los mismos proxies. |
| VAN incremental | USD 397,07 | USD -55,21 | Chile crea valor con los proxies; East US no alcanza la tasa exigida. |
| TIR incremental anual | 43,91% | -0,21% | Indicador complementario; no sustituye al VAN. |
| PRI descontado | Mes 30 | No recupera en 60 meses | Fórmula visible en FP-187: primer cruce no negativo del flujo descontado acumulado. |

### Lectura económica

- **East US** minimiza tanto el TCO cloud base como el costo total optimizado con los proxies actuales.
- **Chile Central** tiene mayor costo regional, pero concentra mayor ahorro de las palancas evaluadas y el paquete FinOps presenta VAN incremental positivo.
- El VAN incremental de FP-187 evalúa si conviene ejecutar la optimización **dentro de cada región**; no compara Chile Central contra East US ni convierte a Chile en la región más económica.
- La selección regional debe resolverse primero con residencia, latencia, HA/SLA y costo total comparable. Después se decide qué palancas FinOps aplicar en la región seleccionada.
- La tasa de 5,5% es una proxy pública de la Tasa Social de Descuento MDSF 2026, no el WACC corporativo.

## 3. Recomendación regional condicionada

| Gate | Chile Central | East US | Regla de decisión |
|---|---|---|---|
| Residencia de datos | Opción preferente si se exige proximidad o residencia en Chile | Válida solo si la política permite operar fuera de Chile | Un requisito regulatorio o contractual prevalece sobre el ahorro. |
| Latencia | Pendiente de medir; hipótesis favorable por proximidad | Pendiente de medir desde usuarios y dependencias | No cerrar región sin medición contra el SLO. |
| TCO total comparable | Mayor | Menor | East US es el default económico si ambas regiones superan los gates técnicos. |
| VAN incremental del paquete FinOps | Positivo | Negativo | En Chile conviene el paquete modelado; en East US debe reducirse su costo, aumentar su ahorro o rediseñarse antes de aplicarlo completo. |
| HA, backup y SLA | Requieren validación específica | Tiene opciones de HA y geo-backup distintas | Comparar configuraciones equivalentes, no solo precios. |

### Decisión recomendada

1. **Default económico:** East US, si no existen restricciones de residencia, cumple el SLO y ofrece una configuración de HA/SLA equivalente.
2. **Opción condicionada:** Chile Central, cuando residencia, latencia, contrato o riesgo operativo exijan operar en Chile; en ese caso, ejecutar gradualmente el paquete FinOps porque su VAN incremental es positivo con los proxies actuales.
3. **Optimización en East US:** no ejecutar automáticamente el paquete completo modelado. Primero reducir esfuerzo, aumentar ahorro o validar inputs hasta obtener VAN no negativo.
4. **No decisión todavía:** si faltan mediciones de latencia o los datos internos modifican el WACC, el costo de operación, las horas de implementación o el requisito de HA.

## 4. Plan de adopción de FinOps

### Fase 0 — Validación

- Confirmar propietario de costos, presupuesto y responsables de operación.
- Sustituir la tarifa proxy por costo empresa o timesheets.
- Validar WACC, inversión de migración y esfuerzo por palanca.
- Confirmar volúmenes de operaciones Blob, consultas de Monitor, HA, soporte y residencia.

### Fase 1 — Palancas de bajo riesgo

- Programar apagado de no producción dentro de ventanas aprobadas.
- Reducir retención o ingesta de logs solo con requisitos de auditoría confirmados.
- Controlar egress y etiquetar costos por aplicación, ambiente y responsable.
- Medir ahorro real versus la línea base de FP-183.

### Fase 2 — Rightsizing controlado

- Probar vCPU y vCores alternativos en un entorno controlado.
- Medir CPU, memoria, conexiones, latencia, errores y throughput.
- Aplicar el cambio solo si mantiene el SLO y el ahorro supera el costo de operación.
- Recalcular FP-186 y FP-187 después de la medición.

## 5. Sensibilidad y riesgos

FP-186 identifica como drivers principales los **vCores de PostgreSQL en producción** y la **vCPU de producción**. Por ello, la recomendación no debe basarse únicamente en el punto base.

| Riesgo | Efecto posible | Mitigación |
|---|---|---|
| Rightsizing sin pruebas | Degradación de latencia o disponibilidad | Experimento controlado y rollback. |
| Egress mayor al supuesto | Aumento del TCO y reducción del VAN | Medición de tráfico y topología antes de contratar. |
| HA/SLA requerido | Aumento de cómputo, storage y operación | Escenario separado con configuraciones equivalentes. |
| Residencia de datos | East US podría quedar descartado | Validación legal y contractual por servicio. |
| Proxy laboral subestimado | VAN sobreestimado | Usar costo empresa y timesheets. |
| Tasa no representativa | VAN/TIR no comparables con decisión interna | Sustituir por WACC o tasa exigida aprobada. |
| Datos de precios cambiantes | TCO desactualizado | Registrar fecha y refrescar fuentes antes de decidir. |

## 6. Matriz de trazabilidad

| Resultado usado | Fuente | Uso en la recomendación |
|---|---|---|
| Arquitectura, componentes y límites | [FP-182](../fp-182/arquitectura-y-supuestos-borrador.md) | Define el caso comparable y sus exclusiones. |
| TCO base regional | [FP-183 README](../fp-183/README.md), [modelo TCO](../fp-183/modelo-tco-linea-base-5-anos.xlsx) | Establece la línea base de costos a 60 meses. |
| Palancas y ahorro bruto | [FP-184 trazabilidad](../fp-184/trazabilidad-fp184.md), [workbook optimizado](../fp-184/escenario-optimizado-fp-184.xlsx) | Sustenta scheduling, logs y egress. |
| Comparación regional | [FP-185 workbook](../fp-185/comparacion-regional-santiago-eastus.xlsx) | Contrasta costo y configuración por región. |
| Sensibilidad | [FP-186 sensibilidad](../fp-186/sensibilidad.html), [trazabilidad](../fp-186/trazabilidad-fp186.md) | Identifica drivers y condiciones de cambio. |
| VAN, TIR y flujo incremental | [FP-187 workbook](../fp-187/flujo-caja-van-tir-fp-187.xlsx), [trazabilidad](../fp-187/trazabilidad-fp187.md) | Prioriza VAN y explicita proxies financieros. |

## 7. Papers y fuentes metodológicas

Los papers respaldan el método de decisión y optimización; no sustituyen precios oficiales ni datos internos.

| Evidencia | Aporte |
|---|---|
| [Manurung y Aji (2025)](<../../FP-48 TINV02/Papers academicos - FP-48/markdown/01_Manurung_Aji_2025_FinOps_Implementation.md>) | Ownership de costos, presupuesto, gobernanza y rightsizing. |
| [Cho (2026)](<../../FP-48 TINV02/Papers academicos - FP-48/markdown/03_Cho_2026_FinOps_Budget_Optimization.md>) | Restricciones presupuestarias, estabilidad y riesgo operacional. |
| [Optimization of Resource Provisioning Cost in Cloud Computing](<../../FP-48 TINV02/Papers academicos - FP-48/markdown/05_Optimization of Resource Provisioning Cost in Cloud Computing.md>) | Incertidumbre de demanda/precio y provisión de recursos. |
| [Cloud egress and TCO study](<../../FP-48 TINV02/Papers academicos - FP-48/markdown/s41781-024-00128-x.md>) | Materialidad del egress y análisis de TCO. |
| [Design of Experiments-Based Adaptive Scheduling](<../../FP-48 TINV02/Papers academicos - FP-48/markdown/Design of Experiments-Based Adaptive Scheduling in.md>) | Necesidad de validar rendimiento y costo mediante experimentación. |
| [Applied Sciences 14-11946](<../../FP-48 TINV02/Papers academicos - FP-48/markdown/applsci-14-11946-v2.md>) | Comparación de políticas de precio y planificación FinOps. |

Fuentes públicas usadas en los modelos: [Azure Container Apps billing](https://learn.microsoft.com/en-us/azure/container-apps/billing), [PostgreSQL Flexible Server compute](https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-compute), [Azure Bandwidth](https://azure.microsoft.com/en-us/pricing/details/bandwidth/), [MDSF Precios Sociales 2026](https://sni.gob.cl/wp-content/uploads/Precios-Sociales-2026.pdf), [INE ESI 2024](https://www.ine.gob.cl/docs/default-source/encuesta-suplementaria-de-ingresos/publicaciones-y-anuarios/s%C3%ADntesis-de-resultados/2024/esi2024.pdf), [Dirección del Trabajo](https://www.dt.gob.cl/portal/1626/w3-propertyname-2556.html) y [Banco Central de Chile](https://si3.bcentral.cl/siete/ES/Siete/Cuadro/CAP_TIPO_CAMBIO/MN_TIPO_CAMBIO4/DOLAR_OBS_ADO?idSerie=F073.TCO.PRE.Z.D).

## 8. Condiciones de validez

La recomendación cambia si ocurre cualquiera de estos eventos:

- La residencia de datos obliga a una región específica.
- La latencia medida incumple el SLO.
- Se exige HA, geo-backup o soporte pago no modelado.
- El costo empresa o la implementación real reducen el VAN de Chile a cero o menos.
- Se valida un costo de migración distinto de cero.
- Los precios o franquicias vigentes cambian.

Hasta completar esas validaciones, el resultado correcto es una **recomendación condicionada**, no una orden de despliegue.

## 9. Checklist de cierre

- [ ] Latencia medida desde la población objetivo.
- [ ] Residencia, HA, RPO/RTO y SLA aprobados.
- [ ] WACC o tasa financiera interna validada.
- [ ] Costo empresa y horas reales de implementación/operación validados.
- [x] PRI incorporado al workbook de FP-187 y verificado en `Resumen!K5:K6`, `Flujo mensual!X7:AA67` y `Auditoría!A14:E15`.
- [ ] Sensibilidad recalculada con inputs internos.
- [ ] Recomendación revisada por responsables técnico y financiero.

La revisión documental de los 17 registros pendientes está en `docs/fp-188/auditoria-validaciones-pendientes.md`. El procedimiento, evidencia mínima y destino de actualización para cada registro están en `docs/fp-188/plan-cierre-17-validaciones.md`. La auditoría confirma que siguen faltando datos o aprobaciones humanas; los valores precargables solo mantienen operativo el escenario académico y no los sustituyen.

## Referencia de seguimiento

- Jira: FP-188 — Redactar la recomendación técnica y económica.
- GitHub: [Issue #27](https://github.com/TheVillegas/FEP-INVESTIGACION/issues/27).
- Entrega aguas abajo: usar esta recomendación y sus condiciones como entrada técnica-económica de FP-54 y FP-56; no trasladar los proxies como valores aprobados.
