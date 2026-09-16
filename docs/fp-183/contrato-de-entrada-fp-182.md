# Contrato de entrada FP-182 → FP-183

| Grupo | Valor recibido | Estado | Observación |
|---|---|---|---|
| Arquitectura | API web sobre Azure Container Apps Consumption | Validado para modelación | Escenario ilustrativo TI-06, no sistema productivo documentado. |
| Regiones | Chile Central y East US | Validado para modelación | Mismo diseño lógico. |
| Horizonte y moneda | 60 meses, USD | Validado | Sin FX ni impuestos. |
| Producción | 1 vCPU, 2 GiB, 730 h, 1 M solicitudes/mes | Supuesto editable | Franquicias mensuales aplicadas primero a producción. |
| No producción | 0,5 vCPU, 1 GiB, 264 h, 0,1 M solicitudes/mes | Supuesto editable | Escala a cero fuera de ventana. |
| PostgreSQL | General Purpose, 2 vCores, 100 GiB | Corregido | 1 vCore no es desplegable en GP. HA desactivada. |
| Objetos | 500 GB, crecimiento 20 % anual | Supuesto editable | Operaciones/lecturas pendientes y excluidas. |
| Red | 200 GB/mes; 100 GB gratis | Corregido | Tarifa continental Premium Global Network. |
| Observabilidad | 50 GB/mes Basic Logs, 30 días | Supuesto editable | Consultas/retención adicional excluidas. |
| Backup | Automático, 7 días, 0 GiB excedente | Corregido | Sin Azure Backup LTR ni GRS. |
| Licencias | Sin terceros | No aplica justificado | PostgreSQL open source. |
| Soporte | Azure Basic Support | No aplica justificado | Plan pago no requerido en el escenario base. |
| Interzona | 0 GB | No aplica justificado | HA desactivada. |
| Operaciones | Horas/mes y USD/h | **Pendiente** | Bloquea el TCO económico completo. |
| Aprobación | Revisión humana | **Pendiente** | El modelo no sustituye aprobación del equipo. |

## Regla de comparabilidad

Arquitectura, demanda, período, moneda y reglas de cálculo permanecen iguales. Solo cambian tarifas y condiciones regionales documentadas. Toda excepción debe quedar visible en `Fuentes y Cotizaciones`.
