# FP-187 — Trazabilidad de flujo de caja, VAN y TIR

## Estado

Modelo inicial creado para revisión. El VAN/TIR incremental queda pendiente mientras no se validen tasa, inversión inicial, horas/tarifa operativa y costos de implementación.

## Dependencias

- FP-183: costos cloud mensuales base por Chile Central y East US.
- FP-184: ahorro bruto combinado de las tres palancas: USD 1,453.152 en Chile Central y USD 936.48 en East US.
- FP-48: papers académicos usados para método, trazabilidad y discusión FinOps; no se usan como cotización de precios.

## Decisiones de modelación

- Horizonte: 60 meses.
- Mes 0: inversión inicial e implementación, actualmente vacías.
- Meses 1–60: costos cloud de FP-183 y ahorro bruto mensual de FP-184.
- Tasa anual provisional: 12%; tasa mensual calculada como (1 + tasa anual)^(1/12) - 1.
- VAN bruto: valor presente del ahorro cloud antes de implementación.
- VAN incremental: VAN bruto menos implementación inicial.
- TIR incremental: TIR mensual anualizada; queda vacía si no hay inversión inicial positiva.
- Los costos operativos se muestran como parámetros y no se convierten en cero cuando están vacíos.

## Evidencia oficial

- Azure Container Apps billing: https://learn.microsoft.com/en-us/azure/container-apps/billing
- PostgreSQL Flexible Server compute: https://learn.microsoft.com/en-us/azure/postgresql/compute-storage/concepts-compute
- Azure bandwidth: https://azure.microsoft.com/en-us/pricing/details/bandwidth/
- Azure Monitor workspace design: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design

## Limitaciones y siguiente validación

- Completar inversión inicial, costo de implementación, horas operativas, tarifa y tasa financiera con el grupo.
- Revisar si existen impuestos, inflación, tipo de cambio, valor residual o ingresos incrementales fuera del alcance actual.
- No mover FP-187 a Done hasta defender la conexión entre TCO, flujo de caja, VAN y TIR.