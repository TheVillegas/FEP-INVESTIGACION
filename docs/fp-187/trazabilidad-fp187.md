# FP-187 — Trazabilidad de flujo de caja, VAN y TIR

## Estado

Modelo actualizado con proxies públicos verificables y estimaciones de ingeniería explícitas. Los resultados son aptos para discusión académica, pero deben sustituirse por datos internos antes de usarse como presupuesto o cotización.

## Dependencias

- FP-183: costos cloud mensuales base por Chile Central y East US.
- FP-184: ahorro bruto combinado de las tres palancas: USD 1,453.152 en Chile Central y USD 936.48 en East US.
- FP-48: papers académicos usados para método, trazabilidad y discusión FinOps; no se usan como cotización de precios.

## Decisiones de modelación

- Horizonte: 60 meses.
- Mes 0: costo de implementación de la optimización. La inversión de migración se fija en USD 0 porque el análisis incremental parte de la arquitectura cloud ya modelada; esto evita duplicar el TCO.
- Meses 1–60: costos cloud de FP-183 y ahorro bruto mensual de FP-184.
- Tasa anual provisional: 5.5%, tomada como proxy público de la Tasa Social de Descuento 2026 del MDSF; tasa mensual = (1 + tasa anual)^(1/12) - 1.
- VAN bruto: valor presente del ahorro cloud antes de implementación.
- VAN incremental: flujo de ahorro menos operación FinOps mensual y costo de implementación en mes 0.
- TIR incremental: TIR mensual del flujo neto anualizada como (1 + TIR mensual)^12 - 1.
- Tarifa proxy: ingreso medio neto mensual de personas ocupadas con educación universitaria (INE ESI 2024) dividido por 182 h/mes y por CLP 954.85/USD.
- Esfuerzo de implementación: 50 h por escenario, desglosado en revisión/plan, rightsizing, programación, retención de logs, control y documentación.
- Operación incremental: 1 h/mes por escenario, desglosada en revisión de costo/uso, anomalías/reporte y seguimiento.
- Chile Central y East US son alternativas; sus costos de implementación no se suman entre sí.

## Evidencia oficial

- Azure Container Apps billing: https://learn.microsoft.com/en-us/azure/container-apps/billing
- PostgreSQL Flexible Server compute: https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-compute
- Azure bandwidth: https://azure.microsoft.com/en-us/pricing/details/bandwidth/
- Azure Monitor workspace design: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design
- MDSF, Precios Sociales Vigentes 2026 (TSD 5.5%): https://sni.gob.cl/wp-content/uploads/Precios-Sociales-2026.pdf
- INE, ESI 2024 (ingreso universitario CLP 1,483,153/mes): https://www.ine.gob.cl/docs/default-source/encuesta-suplementaria-de-ingresos/publicaciones-y-anuarios/s%C3%ADntesis-de-resultados/2024/esi2024.pdf
- Dirección del Trabajo, jornada máxima 42 h/semana desde 2026-04-26: https://www.dt.gob.cl/portal/1626/w3-propertyname-2556.html
- Banco Central de Chile, dólar observado CLP 954.85/USD al 2026-09-17: https://si3.bcentral.cl/siete/ES/Siete/Cuadro/CAP_TIPO_CAMBIO/MN_TIPO_CAMBIO4/DOLAR_OBS_ADO?idSerie=F073.TCO.PRE.Z.D
- FinOps Foundation, Usage Optimization: https://www.finops.org/framework/capabilities/usage-optimization/
- FinOps Foundation, Planning & Estimating: https://www.finops.org/framework/capabilities/planning-estimating/
- Paper FP-48 `01_Manurung_Aji_2025_FinOps_Implementation.md`, líneas 140–174 y 213–290: sustenta monitoreo, rightsizing, gobernanza y operación; no aporta tarifas del proyecto.

## Limitaciones y siguiente validación

- La tarifa es una aproximación de ingreso neto, no costo empresa cargado; probablemente subestima cotizaciones, beneficios y overhead.
- Las 50 h de implementación y 1 h/mes de operación son estimaciones bottom-up del escenario académico, no observaciones de timesheets.
- El modelo usa USD constantes y excluye impuestos, inflación y valor residual; cualquier cambio de base exige recalcular.
- Reemplazar tasa, tarifa y horas por datos internos cuando existan. Hasta entonces, Jira debe describir el resultado como proxy provisional.